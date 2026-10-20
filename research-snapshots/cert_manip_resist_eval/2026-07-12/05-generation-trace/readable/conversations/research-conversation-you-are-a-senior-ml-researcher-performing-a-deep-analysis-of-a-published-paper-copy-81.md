# Research conversation: You are a senior ML researcher performing a deep analysis of a published paper. **Today's date: 2026-05-27 (UTC).** ## Y

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-3/0243be30-7aad-4e4c-9062-bffffcde4a0d.jsonl`
- **Structured JSON:** [`960f1492c82868921a1d.json`](../../sessions/96/960f1492c82868921a1d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T16:08:11.130Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T16:08:11.130Z",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d",
  "content": "You are a senior ML researcher performing a deep analysis of a published paper.\n\n**Today's date: 2026-05-27 (UTC).**\n\n## Your goal\n\nAnalyze this paper NOT just for what it does, but for **HOW it innovates** — what can we learn from its approach to doing research? What made this paper good enough for a top venue?\n\n## Research context\n\nWe are generating ideas in the area of: **Multi-Modal Mathematical Reasoning — Integrating Visual, Symbolic, and Textual Understanding**\n\n## Paper to analyze\n\n{\n  \"title\": \"MM-PRM: Enhancing Multimodal Mathematical Reasoning with Scalable Step-Level Supervision\",\n  \"authors\": \"Lingxiao Du et al.\",\n  \"venue\": \"arXiv 2025\",\n  \"url\": \"https://arxiv.org/abs/2505.13427\",\n  \"why_important\": \"Scalable MCTS-based pipeline generating 700K+ step-level annotations without human labeling; significant OOD improvements; complements URSA's process supervision approach\",\n  \"one_line_summary\": \"Uses Monte Carlo Tree Search to automatically generate 700K+ step-level annotations for training a multimodal process reward model, achieving significant gains on both in-domain and out-of-domain benchmarks.\"\n}\n\n## Instructions\n\n1. **Deep read**: Use WebFetch to read this paper's full abstract, introduction, method section, and conclusion on arXiv or OpenReview. If it's on OpenReview, also read the reviewer comments and author responses.\n\n2. **Analyze the innovation structure**: Don't just summarize — dissect HOW the authors arrived at their contribution:\n   - What gap did they identify and HOW did they find it?\n   - What was the key insight that others missed?\n   - How did they formulate the problem differently from prior work?\n   - What existing technique did they adapt/combine/simplify?\n\n3. **Learn from reviewers**: If you can find reviewer comments, extract:\n   - What did reviewers praise most?\n   - What concerns were raised and how were they addressed?\n   - What would have made this paper even stronger?\n\n## Output format\n\nOutput a single JSON object:\n{\n  \"title\": \"Paper title\",\n  \"venue\": \"Where published\",\n  \"problem_identification\": \"What gap/problem did they identify? How did they find it? (2-3 sentences)\",\n  \"key_insight\": \"The core intellectual contribution — the aha moment (1-2 sentences)\",\n  \"innovation_type\": \"new_formulation | new_technique | new_benchmark | simplification | cross_domain | combination | scaling | analysis\",\n  \"method_summary\": \"Technical approach in 3-5 sentences — enough to understand the machinery\",\n  \"what_makes_it_good\": \"Why did this paper get accepted? What would reviewers have liked? (2-3 sentences)\",\n  \"limitations_acknowledged\": \"What gaps did the authors themselves identify? (1-2 sentences)\",\n  \"open_questions\": \"What follow-up questions does this paper raise? What remains unsolved? (2-3 bullet points)\",\n  \"building_blocks\": [\"List of methods/tools/datasets used that could be reused\"],\n  \"reviewer_feedback_summary\": \"If found on OpenReview: key praise and concerns. Otherwise: null\",\n  \"relevance_to_seed\": \"How does this paper relate to our research area? What can we learn from it? (1-2 sentences)\"\n}\n\nBe analytical, not descriptive. We want to learn the CRAFT of doing good research, not just know what this paper did."
}
```

---

### Runtime record

_source line 2 · 2026-05-27T16:08:11.133Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T16:08:11.133Z",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d"
}
```

---

## Round 1

40 recorded events

### User

_source line 3 · 2026-05-27T16:08:11.145Z_

You are a senior ML researcher performing a deep analysis of a published paper.

**Today's date: 2026-05-27 (UTC).**

## Your goal

Analyze this paper NOT just for what it does, but for **HOW it innovates** — what can we learn from its approach to doing research? What made this paper good enough for a top venue?

## Research context

We are generating ideas in the area of: **Multi-Modal Mathematical Reasoning — Integrating Visual, Symbolic, and Textual Understanding**

## Paper to analyze

{
  "title": "MM-PRM: Enhancing Multimodal Mathematical Reasoning with Scalable Step-Level Supervision",
  "authors": "Lingxiao Du et al.",
  "venue": "arXiv 2025",
  "url": "https://arxiv.org/abs/2505.13427",
  "why_important": "Scalable MCTS-based pipeline generating 700K+ step-level annotations without human labeling; significant OOD improvements; complements URSA's process supervision approach",
  "one_line_summary": "Uses Monte Carlo Tree Search to automatically generate 700K+ step-level annotations for training a multimodal process reward model, achieving significant gains on both in-domain and out-of-domain benchmarks."
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
  "promptId": "de34c998-fd7f-4a40-bbbf-9dd4b01a6eef",
  "type": "user",
  "uuid": "f4d00e70-0a0d-4285-b331-bd64d86ef4c9",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T16:08:11.144Z_

```json
{
  "parentUuid": "f4d00e70-0a0d-4285-b331-bd64d86ef4c9",
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
  "uuid": "5b0848d1-c239-4c8f-957c-e9195823de3a",
  "timestamp": "2026-05-27T16:08:11.144Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T16:08:11.144Z_

```json
{
  "parentUuid": "5b0848d1-c239-4c8f-957c-e9195823de3a",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "0a9ae1f2-d772-455e-b792-39ddccb6eba0",
  "timestamp": "2026-05-27T16:08:11.144Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d",
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
  "aiTitle": "Analyze MM-PRM paper for research methodology",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d"
}
```

---

### Assistant

_source line 7 · 2026-05-27T16:08:14.108Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to analyze a paper called "MM-PRM: Enhancing Multimodal Mathematical Reasoning with Scalable Step-Level Supervision" from arXiv. Let me fetch the paper details first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a9ae1f2-d772-455e-b792-39ddccb6eba0",
  "isSidechain": false,
  "requestId": "req_011CbTMyzeRnNPg5ZmvbWXhA",
  "type": "assistant",
  "uuid": "3fb16290-b86a-4325-82a6-d55f585239f0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018oZKQxr5a5x8bdwbQQa3K8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2196,
      "cache_read_input_tokens": 11014,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2196,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 140,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 2196,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2196
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

_source line 8 · 2026-05-27T16:08:14.350Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Qu3g99EQn8ZSJ8JmGdqkth`</summary>

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
  "parentUuid": "3fb16290-b86a-4325-82a6-d55f585239f0",
  "isSidechain": false,
  "requestId": "req_011CbTMyzeRnNPg5ZmvbWXhA",
  "type": "assistant",
  "uuid": "d50d9ef4-a9aa-4396-86e8-870960ea5814",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018oZKQxr5a5x8bdwbQQa3K8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2196,
      "cache_read_input_tokens": 11014,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2196,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 140,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 2196,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2196
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

_source line 9 · 2026-05-27T16:08:14.362Z_

<details><summary>↩ Tool result · `toolu_01Qu3g99EQn8ZSJ8JmGdqkth`</summary>

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
  "parentUuid": "d50d9ef4-a9aa-4396-86e8-870960ea5814",
  "isSidechain": false,
  "promptId": "de34c998-fd7f-4a40-bbbf-9dd4b01a6eef",
  "type": "user",
  "uuid": "05c0129b-2121-4c7a-b880-ebc9d6b3ca13",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "d50d9ef4-a9aa-4396-86e8-870960ea5814",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-27T16:08:18.031Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me fetch the paper from arXiv. I'll fetch both the abstract page and the full paper PDF (via HTML version).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05c0129b-2121-4c7a-b880-ebc9d6b3ca13",
  "isSidechain": false,
  "requestId": "req_011CbTMzEqTLHQNV93AxPH6U",
  "type": "assistant",
  "uuid": "f4fa406c-9e3e-4da8-96da-e73fc9ccd55d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PZPg6Wj9tESpMqYs8wZRt7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 660,
      "cache_read_input_tokens": 13210,
      "output_tokens": 343,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 660,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 343,
          "cache_read_input_tokens": 13210,
          "cache_creation_input_tokens": 660,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 660
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

_source line 11 · 2026-05-27T16:08:19.899Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VcmPbv8UawYPQiDw9tVv4c`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.13427",
  "prompt": "Extract the full abstract, author list, and any other metadata available on this arXiv page for the paper MM-PRM. Include the full abstract text verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4fa406c-9e3e-4da8-96da-e73fc9ccd55d",
  "isSidechain": false,
  "requestId": "req_011CbTMzEqTLHQNV93AxPH6U",
  "type": "assistant",
  "uuid": "ca3fb994-77f2-46c3-a7f7-3aa527443dc5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PZPg6Wj9tESpMqYs8wZRt7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 660,
      "cache_read_input_tokens": 13210,
      "output_tokens": 343,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 660,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 343,
          "cache_read_input_tokens": 13210,
          "cache_creation_input_tokens": 660,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 660
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

_source line 12 · 2026-05-27T16:08:23.664Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01E1MqRa6jswEY3Rp6ddcUVP`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.13427",
  "prompt": "Extract the FULL text of the following sections from this paper, as completely as possible:\n1. Introduction (full text)\n2. Method / Approach section (full text, including all subsections)\n3. Experiments / Results (key results, tables, ablation findings)\n4. Conclusion and Limitations\n5. Related Work (key points about what prior work existed)\n\nBe as thorough and detailed as possible. Include specific numbers, equations, dataset names, model names, and technical details. Do NOT summarize — extract the actual content."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca3fb994-77f2-46c3-a7f7-3aa527443dc5",
  "isSidechain": false,
  "requestId": "req_011CbTMzEqTLHQNV93AxPH6U",
  "type": "assistant",
  "uuid": "1fadfcd5-87a8-4e47-a184-7b51892adb58",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PZPg6Wj9tESpMqYs8wZRt7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 660,
      "cache_read_input_tokens": 13210,
      "output_tokens": 343,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 660,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 343,
          "cache_read_input_tokens": 13210,
          "cache_creation_input_tokens": 660,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 660
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

_source line 13 · 2026-05-27T16:08:23.826Z_

<details><summary>↩ Tool result · `toolu_01E1MqRa6jswEY3Rp6ddcUVP`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1fadfcd5-87a8-4e47-a184-7b51892adb58",
  "isSidechain": false,
  "promptId": "de34c998-fd7f-4a40-bbbf-9dd4b01a6eef",
  "type": "user",
  "uuid": "5d4c8034-afe2-427e-b2f6-e50768fd3900",
  "toolUseResult": {
    "bytes": 0,
    "code": 404,
    "codeText": "Not Found",
    "result": "The server returned HTTP 404 Not Found.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.",
    "durationMs": 159,
    "url": "https://arxiv.org/html/2505.13427"
  },
  "sourceToolAssistantUUID": "1fadfcd5-87a8-4e47-a184-7b51892adb58",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-27T16:08:24.976Z_

<details><summary>↩ Tool result · `toolu_01VcmPbv8UawYPQiDw9tVv4c`</summary>

```text
# MM-PRM Paper Metadata

**Title:** MM-PRM: Enhancing Multimodal Mathematical Reasoning with Scalable Step-Level Supervision

**Authors:** Lingxiao Du, Fanqing Meng, Zongkai Liu, Zhixiang Zhou, Ping Luo, Qiaosheng Zhang, Wenqi Shao

**arXiv ID:** 2505.13427

**Submission Date:** May 19, 2025 (v1); June 5, 2025 (v2)

**Subject Areas:** Artificial Intelligence (cs.AI); Computer Vision and Pattern Recognition (cs.CV)

**Abstract:**

The research addresses limitations in multimodal large language models' ability to handle complex reasoning tasks. The authors introduce MM-PRM, a process reward model using an "automated, scalable framework." They develop MM-Policy, a multimodal reasoning model, and MM-K12, a dataset of "10,000 multimodal math problems with verifiable answers." 

Using "Monte Carlo Tree Search (MCTS)-based pipeline," the team generated "over 700k step-level annotations without human labeling." The resulting model was evaluated on multiple benchmarks including OlympiadBench and MathVista, demonstrating improved logical consistency. The authors emphasize that "process supervision is a powerful tool" for enhancing multimodal reasoning systems and have released code and data publicly.

**License:** CC BY 4.0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca3fb994-77f2-46c3-a7f7-3aa527443dc5",
  "isSidechain": false,
  "promptId": "de34c998-fd7f-4a40-bbbf-9dd4b01a6eef",
  "type": "user",
  "uuid": "97062ea3-0501-403a-a327-f577db9ae3cd",
  "toolUseResult": {
    "bytes": 47379,
    "code": 200,
    "codeText": "OK",
    "result": "# MM-PRM Paper Metadata\n\n**Title:** MM-PRM: Enhancing Multimodal Mathematical Reasoning with Scalable Step-Level Supervision\n\n**Authors:** Lingxiao Du, Fanqing Meng, Zongkai Liu, Zhixiang Zhou, Ping Luo, Qiaosheng Zhang, Wenqi Shao\n\n**arXiv ID:** 2505.13427\n\n**Submission Date:** May 19, 2025 (v1); June 5, 2025 (v2)\n\n**Subject Areas:** Artificial Intelligence (cs.AI); Computer Vision and Pattern Recognition (cs.CV)\n\n**Abstract:**\n\nThe research addresses limitations in multimodal large language models' ability to handle complex reasoning tasks. The authors introduce MM-PRM, a process reward model using an \"automated, scalable framework.\" They develop MM-Policy, a multimodal reasoning model, and MM-K12, a dataset of \"10,000 multimodal math problems with verifiable answers.\" \n\nUsing \"Monte Carlo Tree Search (MCTS)-based pipeline,\" the team generated \"over 700k step-level annotations without human labeling.\" The resulting model was evaluated on multiple benchmarks including OlympiadBench and MathVista, demonstrating improved logical consistency. The authors emphasize that \"process supervision is a powerful tool\" for enhancing multimodal reasoning systems and have released code and data publicly.\n\n**License:** CC BY 4.0",
    "durationMs": 5074,
    "url": "https://arxiv.org/abs/2505.13427"
  },
  "sourceToolAssistantUUID": "ca3fb994-77f2-46c3-a7f7-3aa527443dc5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-27T16:08:28.453Z_

<details><summary>Logged reasoning block</summary>

```text
The HTML version wasn't available. Let me try fetching the PDF version or another format.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97062ea3-0501-403a-a327-f577db9ae3cd",
  "isSidechain": false,
  "requestId": "req_011CbTN11fDj4dvkmcmci7kb",
  "type": "assistant",
  "uuid": "e753c7e8-900c-4f45-ac1d-5eaf98e411a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RgX5pHa9TqxVR2bh6BZnPw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 708,
      "cache_read_input_tokens": 13870,
      "output_tokens": 393,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 708,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 85,
          "output_tokens": 393,
          "cache_read_input_tokens": 13870,
          "cache_creation_input_tokens": 708,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 708
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

_source line 16 · 2026-05-27T16:08:29.443Z_

The HTML version returned 404. Let me try the PDF via an alternative route and also check for any OpenReview listing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e753c7e8-900c-4f45-ac1d-5eaf98e411a1",
  "isSidechain": false,
  "requestId": "req_011CbTN11fDj4dvkmcmci7kb",
  "type": "assistant",
  "uuid": "16edfed0-fe27-4466-ae3d-0dfe77a296d9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RgX5pHa9TqxVR2bh6BZnPw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 708,
      "cache_read_input_tokens": 13870,
      "output_tokens": 393,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 708,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 85,
          "output_tokens": 393,
          "cache_read_input_tokens": 13870,
          "cache_creation_input_tokens": 708,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 708
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

_source line 17 · 2026-05-27T16:08:30.933Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TpWpEePy4Sfma13ZKGhxwP`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.13427v2",
  "prompt": "Extract the FULL text of the following sections from this paper, as completely as possible:\n1. Introduction (full text)\n2. Method / Approach section (full text, including all subsections)\n3. Experiments / Results (key results, tables, ablation findings)\n4. Conclusion and Limitations\n5. Related Work (key points about what prior work existed)\n\nBe as thorough and detailed as possible. Include specific numbers, equations, dataset names, model names, and technical details. Do NOT summarize — extract the actual content."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16edfed0-fe27-4466-ae3d-0dfe77a296d9",
  "isSidechain": false,
  "requestId": "req_011CbTN11fDj4dvkmcmci7kb",
  "type": "assistant",
  "uuid": "d089a52b-e425-4496-8ed7-3357b17bd8ea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RgX5pHa9TqxVR2bh6BZnPw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 708,
      "cache_read_input_tokens": 13870,
      "output_tokens": 393,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 708,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 85,
          "output_tokens": 393,
          "cache_read_input_tokens": 13870,
          "cache_creation_input_tokens": 708,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 708
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

_source line 18 · 2026-05-27T16:08:31.239Z_

<details><summary>↩ Tool result · `toolu_01TpWpEePy4Sfma13ZKGhxwP`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d089a52b-e425-4496-8ed7-3357b17bd8ea",
  "isSidechain": false,
  "promptId": "de34c998-fd7f-4a40-bbbf-9dd4b01a6eef",
  "type": "user",
  "uuid": "0a3af465-4756-49a7-ad2f-65b435ca9df8",
  "toolUseResult": {
    "bytes": 0,
    "code": 404,
    "codeText": "Not Found",
    "result": "The server returned HTTP 404 Not Found.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.",
    "durationMs": 300,
    "url": "https://arxiv.org/html/2505.13427v2"
  },
  "sourceToolAssistantUUID": "d089a52b-e425-4496-8ed7-3357b17bd8ea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-27T16:08:32.748Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0163ef1wnARQCpYv9kSctKXs`</summary>

```json
{
  "url": "https://openreview.net/search?term=MM-PRM+Enhancing+Multimodal+Mathematical+Reasoning",
  "prompt": "Search for the paper \"MM-PRM: Enhancing Multimodal Mathematical Reasoning with Scalable Step-Level Supervision\". If found, extract the link to the paper's forum page where reviews and author responses would be available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a3af465-4756-49a7-ad2f-65b435ca9df8",
  "isSidechain": false,
  "requestId": "req_011CbTN11fDj4dvkmcmci7kb",
  "type": "assistant",
  "uuid": "5f82071d-5e7a-44f6-b5d5-a00c511ffc0f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RgX5pHa9TqxVR2bh6BZnPw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 708,
      "cache_read_input_tokens": 13870,
      "output_tokens": 393,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 708,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 85,
          "output_tokens": 393,
          "cache_read_input_tokens": 13870,
          "cache_creation_input_tokens": 708,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 708
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

_source line 20 · 2026-05-27T16:08:35.922Z_

<details><summary>↩ Tool result · `toolu_0163ef1wnARQCpYv9kSctKXs`</summary>

```text
I cannot locate the paper "MM-PRM: Enhancing Multimodal Mathematical Reasoning with Scalable Step-Level Supervision" in the provided web page content.

The content shown is from OpenReview.net's main navigation and footer sections, which only displays general site information such as login options, venue links, and policies. It does not contain search results or specific paper details.

To find this paper, you would need to:
1. Visit OpenReview.net directly
2. Use their search functionality to query the paper title
3. Navigate to the resulting forum page for reviews and author responses
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f82071d-5e7a-44f6-b5d5-a00c511ffc0f",
  "isSidechain": false,
  "promptId": "de34c998-fd7f-4a40-bbbf-9dd4b01a6eef",
  "type": "user",
  "uuid": "dfe12242-467e-4a73-859f-d746c8282f65",
  "toolUseResult": {
    "bytes": 62353,
    "code": 200,
    "codeText": "OK",
    "result": "I cannot locate the paper \"MM-PRM: Enhancing Multimodal Mathematical Reasoning with Scalable Step-Level Supervision\" in the provided web page content.\n\nThe content shown is from OpenReview.net's main navigation and footer sections, which only displays general site information such as login options, venue links, and policies. It does not contain search results or specific paper details.\n\nTo find this paper, you would need to:\n1. Visit OpenReview.net directly\n2. Use their search functionality to query the paper title\n3. Navigate to the resulting forum page for reviews and author responses",
    "durationMs": 3171,
    "url": "https://openreview.net/search?term=MM-PRM+Enhancing+Multimodal+Mathematical+Reasoning"
  },
  "sourceToolAssistantUUID": "5f82071d-5e7a-44f6-b5d5-a00c511ffc0f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-27 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "dfe12242-467e-4a73-859f-d746c8282f65",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze MM-PRM paper for research methodology",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d"
}
```

---

### Assistant

_source line 23 · 2026-05-27T16:08:38.779Z_

<details><summary>Logged reasoning block</summary>

```text
Let me try to access the paper through the PDF or through the Hugging Face papers page, which sometimes has better content extraction.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfe12242-467e-4a73-859f-d746c8282f65",
  "isSidechain": false,
  "requestId": "req_011CbTN1pPasTK9xnoMHedXC",
  "type": "assistant",
  "uuid": "3ebe93b7-425a-4fad-aafb-5a980da0dfda",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ADuUWmrxQnowX3b9KuhBt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 724,
      "cache_read_input_tokens": 14578,
      "output_tokens": 294,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 724,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 294,
          "cache_read_input_tokens": 14578,
          "cache_creation_input_tokens": 724,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 724
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

_source line 24 · 2026-05-27T16:08:40.331Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CJZk2jcExqUgc2uZJAKdou`</summary>

```json
{
  "url": "https://huggingface.co/papers/2505.13427",
  "prompt": "Extract all available information about the paper MM-PRM from this Hugging Face papers page. Include the abstract, any discussion, and any linked resources (datasets, models, code)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ebe93b7-425a-4fad-aafb-5a980da0dfda",
  "isSidechain": false,
  "requestId": "req_011CbTN1pPasTK9xnoMHedXC",
  "type": "assistant",
  "uuid": "2b55a73d-6116-46b2-891c-3c17bbec9fcf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ADuUWmrxQnowX3b9KuhBt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 724,
      "cache_read_input_tokens": 14578,
      "output_tokens": 294,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 724,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 294,
          "cache_read_input_tokens": 14578,
          "cache_creation_input_tokens": 724,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 724
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

_source line 25 · 2026-05-27T16:08:41.296Z_

<details><summary>↩ Tool result · `toolu_01CJZk2jcExqUgc2uZJAKdou`</summary>

```text
&lt;persisted-output>
Output too large (59.4KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/0243be30-7aad-4e4c-9062-bffffcde4a0d/tool-results/toolu_01CJZk2jcExqUgc2uZJAKdou.txt

Preview (first 2KB):
# MM-PRM: Enhancing Multimodal Mathematical Reasoning with Scalable Step-Level Supervision

Lingxiao Du&lt;sup>1,\*&lt;/sup> Fanqing Meng&lt;sup>1,3,\*&lt;/sup> Zongkai Liu&lt;sup>2,\*&lt;/sup> Zhixiang Zhou&lt;sup>2,\*&lt;/sup>  
Ping Luo&lt;sup>4&lt;/sup> Qiaosheng Zhang&lt;sup>1,2,†&lt;/sup> Wenqi Shao&lt;sup>1,2,†&lt;/sup>

&lt;sup>1&lt;/sup>Shanghai AI Laboratory &lt;sup>2&lt;/sup>Shanghai Innovation Institute  
&lt;sup>3&lt;/sup>Shanghai Jiao Tong University &lt;sup>4&lt;/sup>The University of Hong Kong

## Abstract

While Multimodal Large Language Models (MLLMs) have achieved impressive progress in vision-language understanding, they still struggle with complex multi-step reasoning, often producing logically inconsistent or partially correct solutions. A key limitation lies in the lack of fine-grained supervision over intermediate reasoning steps. To address this, we propose MM-PRM, a process reward model trained within a fully automated, scalable framework. We first build MM-Policy, a strong multimodal model trained on diverse mathematical reasoning data. Then, we construct MM-K12, a curated dataset of 10,000 multimodal math problems with verifiable answers, which serves as seed data. Leveraging a Monte Carlo Tree Search (MCTS)-based pipeline, we generate over 700k step-level annotations without human labeling. The resulting PRM is used to score candidate reasoning paths in the Best-of-N inference setup and achieves significant improvements across both in-domain (MM-K12 test set) and out-of-domain (OlympiadBench, MathVista, etc.) benchmarks. Further analysis confirms the effectiveness of soft labels, smaller learning rates, and path diversity in optimizing PRM performance. MM-PRM demonstrates that process supervision is a powerful tool for enhancing the logical robustness of multimodal reasoning systems. We release all our codes and data at &lt;https://github.com/ModalMinds/MM-PRM>.

## 1 Introduction

...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b55a73d-6116-46b2-891c-3c17bbec9fcf",
  "isSidechain": false,
  "promptId": "de34c998-fd7f-4a40-bbbf-9dd4b01a6eef",
  "type": "user",
  "uuid": "2b0db963-9cf8-4e9a-8653-bbc4dd20a779",
  "toolUseResult": {
    "bytes": 60917,
    "code": 200,
    "codeText": "OK",
    "result": "# MM-PRM: Enhancing Multimodal Mathematical Reasoning with Scalable Step-Level Supervision\n\nLingxiao Du&lt;sup>1,\\*&lt;/sup> Fanqing Meng&lt;sup>1,3,\\*&lt;/sup> Zongkai Liu&lt;sup>2,\\*&lt;/sup> Zhixiang Zhou&lt;sup>2,\\*&lt;/sup>  \nPing Luo&lt;sup>4&lt;/sup> Qiaosheng Zhang&lt;sup>1,2,†&lt;/sup> Wenqi Shao&lt;sup>1,2,†&lt;/sup>\n\n&lt;sup>1&lt;/sup>Shanghai AI Laboratory &lt;sup>2&lt;/sup>Shanghai Innovation Institute  \n&lt;sup>3&lt;/sup>Shanghai Jiao Tong University &lt;sup>4&lt;/sup>The University of Hong Kong\n\n## Abstract\n\nWhile Multimodal Large Language Models (MLLMs) have achieved impressive progress in vision-language understanding, they still struggle with complex multi-step reasoning, often producing logically inconsistent or partially correct solutions. A key limitation lies in the lack of fine-grained supervision over intermediate reasoning steps. To address this, we propose MM-PRM, a process reward model trained within a fully automated, scalable framework. We first build MM-Policy, a strong multimodal model trained on diverse mathematical reasoning data. Then, we construct MM-K12, a curated dataset of 10,000 multimodal math problems with verifiable answers, which serves as seed data. Leveraging a Monte Carlo Tree Search (MCTS)-based pipeline, we generate over 700k step-level annotations without human labeling. The resulting PRM is used to score candidate reasoning paths in the Best-of-N inference setup and achieves significant improvements across both in-domain (MM-K12 test set) and out-of-domain (OlympiadBench, MathVista, etc.) benchmarks. Further analysis confirms the effectiveness of soft labels, smaller learning rates, and path diversity in optimizing PRM performance. MM-PRM demonstrates that process supervision is a powerful tool for enhancing the logical robustness of multimodal reasoning systems. We release all our codes and data at &lt;https://github.com/ModalMinds/MM-PRM>.\n\n## 1 Introduction\n\nThe rapid advancement of Large Language Models (LLMs) [1, 2, 3, 4, 5, 6, 7, 8, 9] has significantly improved performance on a wide range of natural language processing tasks, including general reasoning and mathematical problem-solving. In parallel, the development of Multimodal Large Language Models (MLLMs) [10, 11, 12, 13, 14, 15, 16, 17, 18] has unlocked new capabilities in vision-language understanding, showing promising results in areas such as image captioning and visual question answering (VQA). However, despite their impressive capabilities in perception and basic reasoning, MLLMs still struggle with complex multi-step reasoning tasks, particularly in mathematics. These shortcomings often manifest as broken logical chains, inaccurate intermediate steps, or cases that produce incorrect intermediate steps while still occasionally arriving at the correct final answer—a phenomenon that introduces high false-positive rates and undermines interpretability.\n\nTo address this issue, reward modeling [19, 20, 21, 22] has emerged as a promising paradigm. Reward models (RMs) play a central role in reinforcement learning from human feedback (RLHF) [23, 24, 25, 26, 27, 28], and can also be used at inference time to select among multiple candidate responses using Test-Time Scaling (TTS) [29, 30, 31, 32, 33, 34, 35, 36, 37] strategies such as Best-of-N (BoN). In general, reward models for reasoning tasks can be broadly categorized into two types: Outcome Reward Models (ORMs) and Process Reward Models (PRMs). ORMs [19, 20] provide\n\n\\*Equal contribution\n\n†Corresponding Authors: shaowenqi@pjlab.org.cn; zhangqiaosheng@pjlab.org.cnscalar feedback only on the final answer, overlooking the quality of the intermediate reasoning steps. This limits their ability to guide the model toward robust reasoning paths. In contrast, PRMs [38, 39, 21, 31, 40, 41] offer a more fine-grained approach by evaluating each reasoning step, enabling more accurate and interpretable feedback.\n\nSome recent works have explored process reward models for mathematical reasoning in pure text. PRM800k [39] manually constructs a large-scale dataset with step-level correctness labels, which is hard to scale. MathShepherd [31] adopts Monte Carlo estimation to label reasoning steps by evaluating whether continuations from a given step lead to the correct answer, but its efficiency is relatively low. OmegaPRM [41] introduces a Monte Carlo Tree Search (MCTS)-based framework that enables efficient automated generation of process supervision data. However, all these works focus on mathematical reasoning in pure text. In the field of multimodal mathematical reasoning, how to design an efficient framework for process supervision data generation and stably train process reward models remains a challenging problem.\n\nTo address these challenges, we propose **MM-PRM**, a powerful process reward model that effectively handles both in-domain and out-of-domain problems. Specifically, we first collect a large-scale, high-quality reasoning dataset and refine its format to train a policy model called **MM-Policy** with strong reasoning abilities and well-structured output. Inspired by OmegaPRM, we then establish an efficient multimodal process annotation framework. We first collect 10k high-quality K-12-level multimodal mathematical reasoning samples, named **MM-K12**. Starting with only 10k math problems as seed data, our framework automatically generates over 700k step-level annotations without any human supervision. Finally, we train MM-PRM with these data and evaluate its performance on multiple benchmarks using the BoN approach.\n\nMM-PRM demonstrates strong performance and generalization across multiple benchmarks. Although we only use process data generated from K-12-level math problems for training, MM-PRM achieves remarkable results with MM-Policy on benchmarks such as MathVista that improves from 62.93% to 67.60%. In addition, even though MM-PRM is trained on data produced by MM-Policy, it still delivers competitive results on other models like InternVL2.5-8B and InternVL2.5-78B. For instance, on the self-collected MM-K12 test set, InternVL2.5-8B improves from 27.01% to 37.80%, and on MathVerse, InternVL2.5-78B improves from 50.18% to 54.47%. These results highlight MM-PRM’s ability to generalize both across datasets and across model size, despite being trained on limited and fixed data sources.\n\nFinally, we provide a detailed discussion on key factors in PRM training, including learning rate and the choice between soft labels and hard labels. We find that the following factors are essential for stable PRM training: (1) using a small learning rate to ensure stable optimization; (2) adopting soft labels instead of hard thresholding to reduce noise and preserve step-wise uncertainty.\n\nIn summary, our contributions are as follows:\n\n- • We collect and release **MM-K12**, a curated multimodal math dataset containing 10,000 seed problems and 500 test problems, all verified to contain unique, checkable answers.\n- • We build a policy model named **MM-Policy** using a large corpus of mathematical reasoning data, and develop a fully automated, MCTS-based pipeline for scalable process supervision generation. Leveraging MM-Policy and only 10k seed problems from MM-K12, our framework produces over 700k step-level annotations without human supervision. Based on this, we train **MM-PRM**, which demonstrates strong performance across multiple benchmarks—for example, boosting accuracy on the MM-K12 test set from 33.92% to 42.80%, on MathVista from 62.93% to 67.60%, and on OlympiadBench from 15.41% to 24.00%.\n- • We provide a detailed discussion on the settings of key parameters such as the type of process labels and the learning rate. We summarize the key factors for stable PRM training, which can help the community train PRM models more effectively.\n\n## 2 Related work\n\n### 2.1 Mathematical reasoning and reward modeling in LLMs\n\nMathematical reasoning has become a focal point in evaluating the deep logical abilities of LLMs. [19, 42]. Unlike general language tasks, mathematical problems demand precise multi-step reasoningand logical coherence, motivating approaches like Chain-of-Thought (CoT) prompting[43] and Self-Consistency sampling [44]. Supervised fine-tuning (SFT) with structured solution datasets further reinforces reasoning performance, as demonstrated by models like Qwen [2], InternLM [7], and Gemini [3]. More recently, reinforcement learning (RL)-based optimization, exemplified by OpenAI’s o1 [45] and DeepSeek R1 [9], has emerged as a powerful strategy that surpassing SFT-only baselines.\n\nHowever, despite these advances, current LLMs still frequently produce logically inconsistent reasoning steps or false-positive solutions. To address this issue, reward modeling techniques have emerged. Traditional Outcome Reward Models (ORMs)[19, 20], which assign rewards based solely on the final answer, fail to detect flawed intermediate reasoning. Process Reward Models (PRMs)[39, 31, 40, 41] overcome this limitation by explicitly providing step-level supervision, significantly improving logical coherence. Representative works such as PRM800K [39], MathShepherd [31], and MiPS [40] have demonstrated the effectiveness of PRMs in enhancing mathematical reasoning. During the preparation of this manuscript, we became aware of a concurrent effort, URSA [46], which also explores PRM training. While both approaches share some methodological similarities in PRM construction, our work places greater emphasis on building a scalable PRM pipeline and analyzing training dynamics, whereas URSA focuses more on integrating PRMs into RL.\n\nOverall, PRMs have become an essential approach for improving the robustness and logical consistency of LLM reasoning through fine-grained, step-level evaluation.\n\n## 2.2 Process supervision data construction\n\nTraining PRMs requires large-scale, high-quality step-level annotations that indicate the correctness of each intermediate reasoning step. However, most publicly available datasets focus solely on final answers, making it challenging to obtain supervision signals for reasoning quality. Existing process supervision construction methods can be broadly categorized into three classes:\n\n**Manual Annotation.** The earliest efforts, such as PRM800K [39], relied on human experts to label each reasoning step. While this yields high-quality annotations, the approach is costly, time-consuming, and difficult to scale—particularly for domains like mathematics where expert knowledge is required.\n\n**Monte Carlo Estimation.** Works like MathShepherd [31] and MiPS [40] automate supervision by sampling multiple rollouts from each reasoning prefix and estimating step correctness based on the proportion of successful completions. If continuations from a given step often lead to correct answers, that step is considered reliable. This method is simple but suffers from label instability due to high variance in sampled rollouts—especially on long or complex reasoning chains.\n\n**Monte Carlo Tree Search (MCTS).** To address these limitations, OmegaPRM [41] introduces a structured, search-based alternative. Using a divide-and-conquer MCTS algorithm, it efficiently identifies the first error in a reasoning chain and constructs a tree of reasoning paths with dynamically updated statistics. This approach improves annotation stability, better handles deep reasoning tasks, and generates large volumes of fine-grained supervision from limited seed data without human input.\n\nEach method reflects a trade-off between cost, scalability, and label fidelity. Among them, MCTS-based approaches have recently emerged as the most effective strategy for generating robust and scalable process supervision, especially for multi-step mathematical reasoning tasks.\n\n# 3 Method\n\n## 3.1 Overview\n\nWe present a scalable and fully automated framework for training PRMs tailored to multimodal mathematical reasoning. Our approach addresses two critical bottlenecks in prior work: **the lack of step-level supervision** and the **inefficiency of data generation in complex reasoning tasks**. To overcome these challenges, we introduce a structured three-stage pipeline that enables fine-grained reward modeling without any human annotation. As shown in Figure 1, the framework comprises three interconnected stages as follows:Figure 1: Overview of our automated three-stage framework for training MM-PRM: supervised policy model construction, MCTS-based process supervision data generation, and step-level reward model training.\n\n1. (1) **Policy Model Construction**, where a multimodal policy model is trained to generate high-quality reasoning traces following the CoT paradigm.\n2. (2) **Process Supervision Data Generation**, where we use a MCTS-based engine, OmegaPRM [41], to efficiently identify reasoning flaws and produce step-level reward labels at scale.\n3. (3) **Process Reward Model Training**, where a PRM is trained to evaluate each reasoning step and provide dense feedback.\n\nThis end-to-end design ensures that process supervision can be generated, modeled, and applied in a fully closed loop. It significantly improves reasoning quality and robustness, especially in tasks requiring long logical chains. In Sections 3.2–3.3 below, we elaborate on these three stages.\n\n### 3.2 Policy model construction\n\nThe policy model serves as the foundation of our framework, responsible for generating candidate reasoning trajectories given multimodal math problems. These trajectories are later evaluated and labeled to form step-level supervision for training the PRM. Ensuring that the policy model produces logically coherent and structurally complete outputs is thus essential for the effectiveness of the entire system.\n\nTo train the policy model, we curated a large-scale, high-quality dataset of mathematical problems spanning a wide range of topics and difficulty levels. Our dataset integrates samples from over a dozen public math datasets, including R-CoT [47], MAVIS [48], MathV360K [49], NuminaMath [50], and DART-Math [51], with problems ranging from elementary school arithmetic to advanced geometry and statistics. The full list of data sources and sample counts used for training is provided in Appendix A.\n\nOnce collected, all data undergo rigorous cleaning and format standardization. Visual and textual content are paired explicitly, and reasoning traces are reformatted to follow a structured CoT schema, with each logical step clearly marked using structured tags such as `&lt;step>&lt;/step>`, and the final conclusion labeled with `&lt;answer>&lt;/answer>`. To enhance quality and clarity, we leveraged a strong instruction-tuned language model (i.e., Qwen2.5-72B-Instruct [2]) to parse original solutions and restructure them into coherent, modular steps. This structured representation not only enhances model learnability but also lays the foundation for generating step-level reward labels in the next stage. The prompt used for solution restructuring is provided in Appendix B.With this cleaned and annotated corpus of over 5 million examples, we fine-tuned a strong open-source multimodal model, InternVL2.5-8B [16], using supervised learning. This ensures that the model learns to produce logically sound and well-structured outputs that conform to the CoT reasoning pattern.\n\nThe resulting model not only delivers high-quality reasoning trajectories for downstream data annotation but also supports inference-time use cases such as BoN selection with reward-based reranking. Its strong generative ability and logical consistency form the cornerstone of our scalable process supervision framework.\n\n### 3.3 Process supervision data generation\n\nTo enable fine-grained supervision for step-level reasoning, we adopt an automated process annotation pipeline based on the OmegaPRM [41] framework. OmegaPRM introduces a MCTS-based mechanism for efficiently identifying and labeling intermediate reasoning steps with confidence estimates. Although originally developed for textual mathematical reasoning, we adapt and extend this framework to handle multimodal inputs.\n\nOur process begins with collecting a curated dataset of 10,000 multimodal math problems from real-world named **MM-K12**—consisting of 5,000 fill-in-the-blank and 5,000 multiple-choice questions. These problems span a range of curriculum topics from elementary to high school and serve as seed instances for process supervision generation. All examples in MM-K12 are carefully filtered to ensure that each question includes meaningful visual input and has a unique, verifiable answer, making them well-suited for structured reasoning and reward modeling. In addition, MM-K12 also provides an independent test set of 500 problems, constructed under the same criteria, which we use to evaluate in-distribution performance later. For each problem, the policy model produces multiple candidate solutions following the CoT paradigm, and these reasoning paths form the raw material for subsequent reward annotation.\n\nTo evaluate the correctness of each intermediate step, we follow OmegaPRM’s hierarchical rollout and search protocol. Specifically, we generate multiple completions (rollouts) from partial prefixes and estimate the correctness of a given step based on whether its downstream completions reach the correct final answer. By applying binary search, the algorithm efficiently pinpoints the earliest step at which the reasoning begins to deviate. These supervision signals are then aggregated within a structured state-action tree, which records the Monte Carlo (MC) estimates and other statistics at each reasoning state. In our implementation, we maintain the full multimodal context—including both textual and visual components—throughout the tree construction and search process.\n\nImportantly, our adaptation retains the efficiency of OmegaPRM’s divide-and-conquer search while enabling reward supervision for reasoning steps that are conditioned on complex visual stimuli. Through this pipeline, we generate over 700,000 step-level annotations from only 10k seed questions, without requiring manual labeling. The resulting dataset provides dense, high-quality process supervision aligned with real-world multimodal reasoning.\n\n### 3.4 Process reward model training\n\nWith large-scale step-level supervision in place, we proceed to train a PRM that can assess the quality of reasoning steps given a multimodal context. The PRM is designed to serve as a fine-grained critic, assigning a reward score to each intermediate step conditioned on its preceding reasoning context that enables both test-time scaling and potential RL applications.\n\n#### 3.4.1 Labeling strategy\n\nA central design decision in PRM training lies in how to formulate supervision signals from the MC estimations [41, 32]. Rather than adopting hard binary label (e.g.,  $\\hat{y} = 1[\\text{MC}(s) > \\tau]$ ), we use soft label, directly taking the MC scores as continuous supervision targets.\n\nThis choice is motivated by the observation that the MC score reflects more than the correctness of an intermediate step. It also encodes factors such as problem difficulty, step criticality, and distributional uncertainty in the policy model’s rollouts. For instance, a reasoning step within a highly ambiguous or visually complex problem may yield lower MC scores even if the logic is fundamentally sound. In such cases, hard-thresholding may misrepresent the step’s quality, introducing noise into training. Bycontrast, soft labels preserve the probabilistic nuance and enable smoother learning dynamics, more details will be discussed in section 5.3\n\nFormally, for each reasoning step  $x_t$  in a path  $x = [x_1, x_2, \\dots, x_T]$ , we assign a supervision target  $\\hat{y}_t = \\text{MC}(x_{&lt;t}) \\in [0, 1]$ , where  $\\text{MC}(x_{&lt;t})$  denotes the estimated probability that a correct final answer can be reached from this partial path.\n\n### 3.4.2 Model design and training objective\n\nTo model the prediction task, we treat the PRM as a classifier operating on each reasoning step. Given a multimodal input  $q$  and a generated reasoning trace  $[x_1, x_2, \\dots, x_T]$ , we interleave a special marker token, denoted  $\\sigma$ , after each step, producing an input sequence of the form:\n\n$$[q, x_1, \\sigma, x_2, \\sigma, \\dots, x_T, \\sigma].$$\n\nIn our implementation,  $\\sigma$  is instantiated as the token  $\\langle \\text{prm} \\rangle$ . At each occurrence of  $\\sigma$ , the model is tasked with producing a scalar confidence score indicating the likelihood that the immediately preceding step is logically correct. Formally, let  $z_{\\text{Yes}}^{(i)}$  and  $z_{\\text{No}}^{(i)}$  denote the unnormalized logits for binary labels ‘‘Yes’’ (correct) and ‘‘No’’ (incorrect) at the  $i$ -th occurrence of  $\\sigma$ . The model’s predicted probability is computed via softmax:\n\n$$p^{(i)} = \\frac{\\exp(z_{\\text{Yes}}^{(i)})}{\\exp(z_{\\text{Yes}}^{(i)}) + \\exp(z_{\\text{No}}^{(i)})}.$$\n\nThe training objective is to minimize the **cross-entropy loss** between the predicted scores  $p^{(i)}$  and the soft labels  $\\hat{y}^{(i)}$ , across all scoring points:\n\n$$\\mathcal{L}_{\\text{PRM}} = - \\sum_{i=1}^T \\left[ \\hat{y}^{(i)} \\cdot \\log p^{(i)} + (1 - \\hat{y}^{(i)}) \\cdot \\log(1 - p^{(i)}) \\right].$$\n\nThis formulation guides the model to make fine-grained assessments of reasoning steps, assigning higher confidence to those with stronger evidence of correctness.\n\n## 4 Experiments\n\n### 4.1 Experiments setup\n\nTo validate the effectiveness of our proposed process reward modeling framework, we conduct a series of experiments, carefully configured to ensure fair, scalable, and reproducible results.\n\n**Policy model construction.** Our policy model (i.e., MM-Policy) is initialized from the multimodal backbone InternVL 2.5-8B and fine-tuned using approximately 4 million cleaned, structured math problems. The model is trained for 1 epoch with a batch size of 128 and a learning rate of 4e-5, updating only the language module while keeping the vision encoder frozen.\n\n**Process supervision data generation.** We adapt the OmegaPRM[41] pipeline for multimodal reasoning and apply it to MM-K12 (10k samples). Using MCTS-based structured rollouts, we generate approximately 747,000 step-level annotations. The sampling parameters are tuned for balance between diversity and efficiency:  $temperature = 1.0$ ,  $top_k = 50$ ,  $top_p = 0.9$ , exploration coefficient  $c_{\\text{puct}} = 0.125$ , and up to 200 search steps or 1,000 total rollouts per problem.\n\n**Process reward model training.** We initialize the PRM from the fine-tuned policy model and train it for 1 epochs with a batch size of 512 and a learning rate of 4e-6.\n\n### 4.2 Evaluation strategies and benchmarks\n\nTo assess the effectiveness of the proposed MM-PRM in improving reasoning quality, we adopt the BoN evaluation protocol. For each test problem, the policy model generates  $N = 16$  candidate reasoning paths independently. The PRM then scores each path step-by-step, producing a sequence of floating-point values representing the predicted quality of each intermediate step, the path with the highest score is selected as the final answer.Since PRM outputs a vector of step-wise confidence scores for each candidate path, a crucial component of our evaluation is the *aggregation function* [40] used to compress this vector into a scalar. We explore a diverse set of aggregation functions, including Min, Average, Max, SumLogPr (i.e., sum of log-probabilities), SumLogOdds (i.e., sum of log-odds), and MeanOdds (i.e., mean odds), each function captures different aspects of path quality. Additionally, a Random baseline is used for comparison, where the final answer is randomly sampled from the same set of 16 candidates. Formal definitions of all aggregation functions are provided in Appendix C.\n\nWe evaluate performance using answer accuracy, defined as the proportion of final selected answers that match the ground truth. This metric directly reflects MM-PRM’s utility in guiding the selection of correct reasoning paths. To comprehensively evaluate our model’s performance and generalization, we conduct experiments on a range of multimodal math benchmarks, including MM-K12 (test set), OlympiadBench (OE\\_MM\\_maths\\_en\\_COMP) [52], MathVista(testmini) [53], MathVerse(testmini) [54], and MathVision(test) [55]. The MM-K12 test set serves as an in-distribution evaluation. For out-of-distribution assessment, we use the OE\\_MM\\_maths\\_en\\_COMP split of OlympiadBench, which contains open-ended multimodal questions from international math competitions, closely related in format to MM-K12 but significantly harder. To further test generalization, we include MathVista, which covers a wide range of visual mathematical tasks; MathVerse, which emphasizes understanding structured visual content; and MathVision, which targets abstract visual reasoning. These benchmarks provide a diverse and rigorous setting to measure both performance and generalization of our process reward modeling framework.\n\n### 4.3 Quantitative results\n\nTable 1: Performance improvements across various benchmarks when applying the MM-PRM to different models.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Model&lt;/th>\n&lt;th>MM-K12&lt;/th>\n&lt;th>OlympiadBench&lt;/th>\n&lt;th>MathVista&lt;/th>\n&lt;th>MathVerse&lt;/th>\n&lt;th>MathVision&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>MM-Policy&lt;/td>\n&lt;td>33.92&lt;/td>\n&lt;td>15.41&lt;/td>\n&lt;td>62.93&lt;/td>\n&lt;td>42.99&lt;/td>\n&lt;td>21.74&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>+MM-PRM&lt;/td>\n&lt;td>42.80&lt;/td>\n&lt;td>24.00&lt;/td>\n&lt;td>67.60&lt;/td>\n&lt;td>46.27&lt;/td>\n&lt;td>27.11&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;/td>\n&lt;td>&lt;b>+8.88&lt;/b>&lt;/td>\n&lt;td>&lt;b>+8.59&lt;/b>&lt;/td>\n&lt;td>&lt;b>+4.67&lt;/b>&lt;/td>\n&lt;td>&lt;b>+3.28&lt;/b>&lt;/td>\n&lt;td>&lt;b>+5.37&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>InternVL2.5-8B&lt;/td>\n&lt;td>27.01&lt;/td>\n&lt;td>5.23&lt;/td>\n&lt;td>56.43&lt;/td>\n&lt;td>36.26&lt;/td>\n&lt;td>10.04&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>+MM-PRM&lt;/td>\n&lt;td>37.80&lt;/td>\n&lt;td>15.33&lt;/td>\n&lt;td>63.50&lt;/td>\n&lt;td>42.56&lt;/td>\n&lt;td>19.41&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;/td>\n&lt;td>&lt;b>+10.79&lt;/b>&lt;/td>\n&lt;td>&lt;b>+10.10&lt;/b>&lt;/td>\n&lt;td>&lt;b>+7.07&lt;/b>&lt;/td>\n&lt;td>&lt;b>+6.30&lt;/b>&lt;/td>\n&lt;td>&lt;b>+9.37&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>InternVL2.5-26B&lt;/td>\n&lt;td>28.01&lt;/td>\n&lt;td>14.46&lt;/td>\n&lt;td>60.02&lt;/td>\n&lt;td>37.83&lt;/td>\n&lt;td>20.76&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>+MM-PRM&lt;/td>\n&lt;td>38.00&lt;/td>\n&lt;td>24.67&lt;/td>\n&lt;td>64.50&lt;/td>\n&lt;td>44.19&lt;/td>\n&lt;td>25.63&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;/td>\n&lt;td>&lt;b>+9.99&lt;/b>&lt;/td>\n&lt;td>&lt;b>+10.21&lt;/b>&lt;/td>\n&lt;td>&lt;b>+4.25&lt;/b>&lt;/td>\n&lt;td>&lt;b>+6.36&lt;/b>&lt;/td>\n&lt;td>&lt;b>+4.87&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>InternVL2.5-38B&lt;/td>\n&lt;td>40.34&lt;/td>\n&lt;td>29.57&lt;/td>\n&lt;td>68.32&lt;/td>\n&lt;td>47.94&lt;/td>\n&lt;td>29.70&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>+MM-PRM&lt;/td>\n&lt;td>52.40&lt;/td>\n&lt;td>32.67&lt;/td>\n&lt;td>71.10&lt;/td>\n&lt;td>52.61&lt;/td>\n&lt;td>32.99&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;/td>\n&lt;td>&lt;b>+12.06&lt;/b>&lt;/td>\n&lt;td>&lt;b>+3.10&lt;/b>&lt;/td>\n&lt;td>&lt;b>+2.78&lt;/b>&lt;/td>\n&lt;td>&lt;b>+4.67&lt;/b>&lt;/td>\n&lt;td>&lt;b>+3.29&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>InternVL2.5-78B&lt;/td>\n&lt;td>42.24&lt;/td>\n&lt;td>30.98&lt;/td>\n&lt;td>69.48&lt;/td>\n&lt;td>50.18&lt;/td>\n&lt;td>31.50&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>+MM-PRM&lt;/td>\n&lt;td>48.80&lt;/td>\n&lt;td>34.67&lt;/td>\n&lt;td>73.20&lt;/td>\n&lt;td>54.47&lt;/td>\n&lt;td>33.26&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;/td>\n&lt;td>&lt;b>+6.56&lt;/b>&lt;/td>\n&lt;td>&lt;b>+3.69&lt;/b>&lt;/td>\n&lt;td>&lt;b>+3.72&lt;/b>&lt;/td>\n&lt;td>&lt;b>+4.29&lt;/b>&lt;/td>\n&lt;td>&lt;b>+1.76&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nWe evaluate the effectiveness of MM-PRM by applying it to a range of policy models and testing its impact across multiple multimodal math benchmarks.\n\nAcross all models, MM-PRM yields substantial performance improvements. For example, when applied to MM-Policy on the MM-K12 test set, accuracy improves from 33.92% to 42.80%, and similar gains are observed with InternVL2.5-8B, where performance rises from 27.01% to 37.80%. These results confirm that MM-PRM is highly effective at identifying high-quality reasoning paths.\n\nBeyond in-domain settings, we observe that MM-PRM also generalizes well to larger models and more challenging datasets. As shown in Table 1, applying MM-PRM to InternVL2.5-78B improves accuracy on OlympiadBench from 30.98% to 34.67%, and on MathVerse from 50.18% to 54.47%. Despite being trained only on the small MM-K12 seed dataset and with a fixed policy model(i.e., MM-Policy), MM-PRM consistently enhances reasoning accuracy across diverse benchmarks and models. This demonstrates the potential of scalable step-level reward modeling to improve mathematical**Question**\n\nAs shown in the figure, it is known that  $AB \\parallel CD$ ,  $CE$  bisect  $\\angle ACD$ , and intersects  $AB$  at  $E$ ,  $\\angle A = 118^\\circ$ . Then  $\\angle AEC = ?$\n\n**Solution**\n\n( $\\hat{A} = 0.83$ ) Identify the relationship between the angles formed by the parallel lines and the transversal. Since  $AB \\parallel CD$  and  $\\angle A = 118^\\circ$ , We can use the property of parallel lines and transversals to determine the measure of  $\\angle ACD$ . The angles on a straight line sum up to  $180^\\circ$ . So:  $\\angle ACD = 180^\\circ - \\angle A = 180^\\circ - 118^\\circ = 62^\\circ$\n\n( $\\hat{A} = 0.68$ ) Use the angle bisector property. Since  $CE$  bisect  $\\angle ACD$ , it divides  $\\angle ACD$  into two equal angles. Therefore:  $\\angle ACE = \\frac{\\angle ACD}{2} = \\frac{62^\\circ}{2} = 31^\\circ$\n\n( $\\hat{A} = 0.02$ ) Determine  $\\angle AEC$  using the exterior angle theorem. In  $\\triangle AEC$ ,  $\\angle AEC$  is an exterior angle and is equal to the sum of the two non-adjacent interior angles  $\\angle A$  and  $\\angle ACE$ . However, since  $\\angle AEC$  is directly opposite  $\\angle ACE$  and  $\\angle A$  is the exterior angle, we can use the fact that the exterior angle is the sum of the two non-adjacent interior angles:  $\\angle AEC = \\angle A - \\angle ACE = 118^\\circ - 31^\\circ = 87^\\circ$\n\n( $\\hat{A} = 0.01$ ) Answer: The Final Answer is 87\n\nFigure 2: Qualitative example of MM-PRM accurately identifying error steps in multimodal reasoning process.\n\nreasoning in a model-agnostic and data-efficient manner. Detailed evaluation results across all aggregation functions are provided in Appendix D.\n\n#### 4.4 Qualitative results\n\nTo further illustrate the behavior of MM-PRM, we present a qualitative example involving a geometry problem with parallel lines and an angle bisector. As shown in Figure 2, the policy model generates a four-step reasoning path, which ultimately leads to an incorrect final answer.\n\nThe PRM assigns high scores to the first two steps (0.83 and 0.68), indicating that they are logically sound. In contrast, Step-3 receives a very low score (0.02), signaling that the model has identified a significant reasoning error at this point. This flawed step leads directly to an incorrect conclusion in Step-4.\n\nThis example demonstrates that MM-PRM is capable of detecting localized logical errors within a reasoning chain, such fine-grained judgment is crucial in selecting high-quality reasoning trajectories and filtering out those with subtle but critical flaws.\n\n## 5 Discussion\n\nFigure 3: (a) Effect of the number of candidate reasoning paths on answer accuracy under Best-of-N inference. Increasing the number of candidates allows the PRM to select higher-quality reasoning trajectories. (b) Effect of learning rate on PRM performance. Small learning rates yield better accuracy, with performance peaking at  $4 \\times 10^{-6}$## 5.1 Candidate path’s impact on PRM performance\n\nSince the PRM operates purely as a selector in the BoN framework, its performance is inherently bounded by the diversity and quality of candidate reasoning paths produced by the policy model. In other words, PRM cannot improve a flawed generation in BoN—it can only choose among the available options. Therefore, the number of reasoning paths generated per problem directly affects its potential to identify a correct and coherent solution.\n\nTo study this effect, we vary the number of generated reasoning paths  $N \\in \\{2, 2^2, 2^3, 2^4\\}$  and measure the corresponding answer accuracy under the aggregation strategy MeanOdds. As shown in Figure 3(a), increasing  $N$  consistently improves MM-PRM’s performance across both test sets. On the MM-K12 test set, accuracy improves from 38.6% at  $N = 2$  to 42.8% at  $N = 16$ , with gains tapering off beyond  $N = 8$ . In contrast, on OlympiadBench, accuracy increases more steadily—from 18.4% to 24.0%—as  $N$  grows. This suggests that for harder, more diverse tasks, having a larger pool of reasoning paths is critical for PRM to identify valid solutions.\n\n## 5.2 Learning rate\n\nAs noted in [39], finetuning a PRM shifts the language models’ objective from generation to discrimination, making learning rate a critical factor. Smaller learning rates are often preferred to maintain stability and preserve pretrained knowledge.\n\nWe evaluate MM-PRM trained under different learning rates on the MM-K12 test set using MeanOdds aggregator. As shown in Figure 3(b), performance peaks at  $4e-6$ —about one-tenth the learning rate typically used in supervised fine-tuning—then drops sharply at higher values. This confirms that a moderate, conservative learning rate leads to better training, while overly large values degrade accuracy.\n\n## 5.3 Soft label vs. Hard label\n\nTable 2: The performance comparisons of soft label vs. hard label.\n\n&lt;table border=\"1\">&lt;thead>&lt;tr>&lt;th>Labeling Strategy&lt;/th>&lt;th>Min&lt;/th>&lt;th>Average&lt;/th>&lt;th>Max&lt;/th>&lt;th>SumLogPr&lt;/th>&lt;th>SumLogOdds&lt;/th>&lt;th>MeanOdds&lt;/th>&lt;/tr>&lt;/thead>&lt;tbody>&lt;tr>&lt;td>Soft Label&lt;/td>&lt;td>37.4&lt;/td>&lt;td>43.0&lt;/td>&lt;td>43.4&lt;/td>&lt;td>42.0&lt;/td>&lt;td>43.2&lt;/td>&lt;td>42.8&lt;/td>&lt;/tr>&lt;tr>&lt;td>Hard Label&lt;/td>&lt;td>36.8&lt;/td>&lt;td>34.4&lt;/td>&lt;td>35.6&lt;/td>&lt;td>36.0&lt;/td>&lt;td>33.8&lt;/td>&lt;td>37.0&lt;/td>&lt;/tr>&lt;/tbody>&lt;/table>\n\nAs discussed in section 3.4.1, we adopt soft label—i.e., real-valued MC scores—as supervision for step-level reward modeling. Unlike hard label, soft label retain uncertainty and allow the model to learn more nuanced representations of reasoning quality.\n\nTo assess this design choice, we compare soft label with hard label thresholding, where steps with  $MC > 0$  are treated as correct, and others as incorrect, following the protocol in [41, 56].\n\nAs shown in Table 2, soft-label training consistently outperforms hard-label training across all aggregation strategies. For instance, under the Average aggregator, soft labels yield 43% accuracy on MM-K12 test set, compared to 34.4% with hard labels. Similar improvements are observed with SumLogOdds (43.2% vs. 33.8%) and MeanOdds (42.8% vs. 37.0%).\n\n## 6 Conclusion\n\nIn this work, we introduce MM-PRM, a process reward model built upon a scalable framework for multimodal mathematical process reward modeling that enables step-level supervision without human annotation. By leveraging a multimodal policy model and an MCTS-based data generation pipeline, we construct over 700k process-level labels from only 10k K-12 math problems in our MM-K12 dataset. Our trained PRM significantly improves reasoning accuracy in BoN inference across both standard and challenging benchmarks, and demonstrates strong generalization to new datasets and models. Extensive analysis further confirms the importance of soft labeling, conservative learning rates, and sufficient path diversity. MM-PRM highlights the value of process supervision for enhancing multimodal mathematical problem-solving.## References\n\n- [1] Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. Gpt-4 technical report. *arXiv preprint arXiv:2303.08774*, 2023.\n- [2] Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang, Xiaodong Deng, Yang Fan, Wenbin Ge, Yu Han, Fei Huang, et al. Qwen technical report. *arXiv preprint arXiv:2309.16609*, 2023.\n- [3] Gemini Team, Rohan Anil, Sebastian Borgeaud, Jean-Baptiste Alayrac, Jiahui Yu, Radu Soricut, Johan Schalkwyk, Andrew M Dai, Anja Hauth, Katie Millican, et al. Gemini: a family of highly capable multimodal models. *arXiv preprint arXiv:2312.11805*, 2023.\n- [4] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, et al. Llama: Open and efficient foundation language models. *arXiv preprint arXiv:2302.13971*, 2023.\n- [5] Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al. Llama 2: Open foundation and fine-tuned chat models. *arXiv preprint arXiv:2307.09288*, 2023.\n- [6] Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Alex Vaughan, et al. The llama 3 herd of models. *arXiv preprint arXiv:2407.21783*, 2024.\n- [7] InternLM Team. Internlm: A multilingual language model with progressively enhanced capabilities. &lt;https://github.com/InternLM/InternLM-techreport>, 2023.\n- [8] Zheng Cai, Maosong Cao, Haojiong Chen, Kai Chen, Keyu Chen, Xin Chen, Xun Chen, Zehui Chen, Zhi Chen, Pei Chu, et al. Internlm2 technical report. *arXiv preprint arXiv:2403.17297*, 2024.\n- [9] Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. *arXiv preprint arXiv:2501.12948*, 2025.\n- [10] Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. Visual instruction tuning. *Advances in neural information processing systems*, 36:34892–34916, 2023.\n- [11] Yuan Yao, Tianyu Yu, Ao Zhang, Chongyi Wang, Junbo Cui, Hongji Zhu, Tianchi Cai, Haoyu Li, Weilin Zhao, Zhihui He, et al. Minicpm-v: A gpt-4v level mllm on your phone. *arXiv preprint arXiv:2408.01800*, 2024.\n- [12] Zhe Chen, Weiyun Wang, Yue Cao, Yangzhou Liu, Zhangwei Gao, Erfei Cui, Jinguo Zhu, Shenglong Ye, Hao Tian, Zhaoyang Liu, et al. Expanding performance boundaries of open-source multimodal models with model, data, and test-time scaling. *arXiv preprint arXiv:2412.05271*, 2024.\n- [13] Weiyun Wang, Zhe Chen, Wenhai Wang, Yue Cao, Yangzhou Liu, Zhangwei Gao, Jinguo Zhu, Xizhou Zhu, Lewei Lu, Yu Qiao, and Jifeng Dai. Enhancing the reasoning ability of multimodal large language models via mixed preference optimization. *arXiv preprint arXiv:2411.10442*, 2024.\n- [14] Zhangwei Gao, Zhe Chen, Erfei Cui, Yiming Ren, Weiyun Wang, Jinguo Zhu, Hao Tian, Shenglong Ye, Junjun He, Xizhou Zhu, et al. Mini-internvl: a flexible-transfer pocket multi-modal model with 5% parameters and 90% performance. *Visual Intelligence*, 2(1):1–17, 2024.\n- [15] Zhe Chen, Weiyun Wang, Hao Tian, Shenglong Ye, Zhangwei Gao, Erfei Cui, Wenwen Tong, Kongzhi Hu, Jiapeng Luo, Zheng Ma, et al. How far are we to gpt-4v? closing the gap to commercial multimodal models with open-source suites. *Science China Information Sciences*, 67(12):220101, 2024.\n- [16] Zhe Chen, Jiannan Wu, Wenhai Wang, Weijie Su, Guo Chen, Sen Xing, Muyan Zhong, Qinglong Zhang, Xizhou Zhu, Lewei Lu, et al. Internvl: Scaling up vision foundation models and aligning for generic visual-linguistic tasks. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, pages 24185–24198, 2024.\n- [17] Jinze Bai, Shuai Bai, Shusheng Yang, Shijie Wang, Sinan Tan, Peng Wang, Junyang Lin, Chang Zhou, and Jingren Zhou. Qwen-vl: A versatile vision-language model for understanding, localization, text reading, and beyond. *arXiv preprint arXiv:2308.12966*, 2023.\n- [18] Kimi Team, Angang Du, Bofei Gao, Bowei Xing, Changjiu Jiang, Cheng Chen, Cheng Li, Chenjun Xiao, Chenzhuang Du, Chonghua Liao, et al. Kimi k1. 5: Scaling reinforcement learning with llms. *arXiv preprint arXiv:2501.12599*, 2025.\n- [19] Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, et al. Training verifiers to solve math word problems. *arXiv preprint arXiv:2110.14168*, 2021.\n- [20] Fei Yu, Anningzhe Gao, and Benyou Wang. Ovm, outcome-supervised value models for planning in mathematical reasoning. *arXiv preprint arXiv:2311.09724*, 2023.- [21] Jonathan Uesato, Nate Kushman, Ramana Kumar, Francis Song, Noah Siegel, Lisa Wang, Antonia Creswell, Geoffrey Irving, and Irina Higgins. Solving math word problems with process-and outcome-based feedback. *arXiv preprint arXiv:2211.14275*, 2022.\n- [22] Yuhang Zang, Xiaoyi Dong, Pan Zhang, Yuhang Cao, Ziyu Liu, Shengyuan Ding, Shenxi Wu, Yubo Ma, Haodong Duan, Wenwei Zhang, et al. Internlm-xcomposer2. 5-reward: A simple yet effective multi-modal reward model. *arXiv preprint arXiv:2501.12368*, 2025.\n- [23] Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training language models to follow instructions with human feedback. *Advances in neural information processing systems*, 35:27730–27744, 2022.\n- [24] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. *arXiv preprint arXiv:1707.06347*, 2017.\n- [25] Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li, Y Wu, et al. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. *arXiv preprint arXiv:2402.03300*, 2024.\n- [26] Xin Lai, Zhuotao Tian, Yukang Chen, Senqiao Yang, Xiangru Peng, and Jiaya Jia. Step-dpo: Step-wise preference optimization for long-chain reasoning of llms. *arXiv preprint arXiv:2406.18629*, 2024.\n- [27] Weiyun Wang, Zhe Chen, Wenhai Wang, Yue Cao, Yangzhou Liu, Zhangwei Gao, Jinguo Zhu, Xizhou Zhu, Lewei Lu, Yu Qiao, et al. Enhancing the reasoning ability of multimodal large language models via mixed preference optimization. *arXiv preprint arXiv:2411.10442*, 2024.\n- [28] Richard Yuanzhe Pang, Weizhe Yuan, He He, Kyunghyun Cho, Sainbayar Sukhbaatar, and Jason Weston. Iterative reasoning preference optimization. *Advances in Neural Information Processing Systems*, 37:116617–116637, 2024.\n- [29] Hanze Dong, Wei Xiong, Bo Pang, Haoxiang Wang, Han Zhao, Yingbo Zhou, Nan Jiang, Doyen Sahoo, Caiming Xiong, and Tong Zhang. Rlhf workflow: From reward modeling to online rlhf. *arXiv preprint arXiv:2405.07863*, 2024.\n- [30] Charlie Snell, Jaehoon Lee, Kelvin Xu, and Aviral Kumar. Scaling llm test-time compute optimally can be more effective than scaling model parameters. *arXiv preprint arXiv:2408.03314*, 2024.\n- [31] Peiyi Wang, Lei Li, Zhihong Shao, RX Xu, Damai Dai, Yifei Li, Deli Chen, Yu Wu, and Zhifang Sui. Math-shepherd: Verify and reinforce llms step-by-step without human annotations. *arXiv preprint arXiv:2312.08935*, 2023.\n- [32] Zhenru Zhang, Chujie Zheng, Yangzhen Wu, Beichen Zhang, Runji Lin, Bowen Yu, Dayiheng Liu, Jingren Zhou, and Junyang Lin. The lessons of developing process reward models in mathematical reasoning. *arXiv preprint arXiv:2501.07301*, 2025.\n- [33] Xidong Feng, Ziyu Wan, Muning Wen, Stephen Marcus McAleer, Ying Wen, Weinan Zhang, and Jun Wang. Alphazero-like tree-search can guide large language model decoding and training. *arXiv preprint arXiv:2309.17179*, 2023.\n- [34] Jikun Kang, Xin Zhe Li, Xi Chen, Amirreza Kazemi, Qianyi Sun, Boxing Chen, Dong Li, Xu He, Quan He, Feng Wen, et al. Mindstar: Enhancing math reasoning in pre-trained llms at inference time. *arXiv preprint arXiv:2405.16265*, 2024.\n- [35] Qianli Ma, Haotian Zhou, Tingkai Liu, Jianbo Yuan, Pengfei Liu, Yang You, and Hongxia Yang. Let’s reward step by step: Step-level reward model as the navigators for reasoning. *arXiv preprint arXiv:2310.10080*, 2023.\n- [36] Ye Tian, Baolin Peng, Linfeng Song, Lifeng Jin, Dian Yu, Lei Han, Haitao Mi, and Dong Yu. Toward self-improvement of llms via imagination, searching, and criticizing. *Advances in Neural Information Processing Systems*, 37:52723–52748, 2024.\n- [37] Dan Zhang, Sining Zhoubian, Ziniu Hu, Yisong Yue, Yuxiao Dong, and Jie Tang. Rest-mcts\\*: Llm self-training via process reward guided tree search. *Advances in Neural Information Processing Systems*, 37:64735–64772, 2024.\n- [38] Yifei Li, Zeqi Lin, Shizhuo Zhang, Qiang Fu, Bei Chen, Jian-Guang Lou, and Weizhu Chen. Making large language models better reasoners with step-aware verifier. *arXiv preprint arXiv:2206.02336*, 2022.\n- [39] Hunter Lightman, Vineet Kosaraju, Yuri Burda, Harrison Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. Let’s verify step by step. In *The Twelfth International Conference on Learning Representations*, 2023.\n- [40] Zihan Wang, Yunxuan Li, Yuexin Wu, Liangchen Luo, Le Hou, Hongkun Yu, and Jingbo Shang. Multi-step problem solving through a verifier: An empirical analysis on model-induced process supervision. *arXiv preprint arXiv:2402.02658*, 2024.- [41] Liangchen Luo, Yinxiao Liu, Rosanne Liu, Samrat Phatale, Meiqi Guo, Harsh Lara, Yunxuan Li, Lei Shu, Yun Zhu, Lei Meng, et al. Improve mathematical reasoning in language models by automated process supervision. *arXiv preprint arXiv:2406.06592*, 2024.\n- [42] Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. Measuring mathematical problem solving with the math dataset. *arXiv preprint arXiv:2103.03874*, 2021.\n- [43] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models. *Advances in neural information processing systems*, 35:24824–24837, 2022.\n- [44] Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. Self-consistency improves chain of thought reasoning in language models. *arXiv preprint arXiv:2203.11171*, 2022.\n- [45] Aaron Jaech, Adam Kalai, Adam Lerer, Adam Richardson, Ahmed El-Kishky, Aiden Low, Alec Hel-yar, Aleksander Madry, Alex Beutel, Alex Carney, et al. Openai o1 system card. *arXiv preprint arXiv:2412.16720*, 2024.\n- [46] Ruilin Luo, Zhuofan Zheng, Yifan Wang, Yiyao Yu, Xinzhe Ni, Zicheng Lin, Jin Zeng, and Yujiu Yang. Ursa: Understanding and verifying chain-of-thought reasoning in multimodal mathematics. *arXiv preprint arXiv:2501.04686*, 2025.\n- [47] Linger Deng, Yuliang Liu, Bohan Li, Dongliang Luo, Liang Wu, Chengquan Zhang, Pengyuan Lyu, Ziyang Zhang, Gang Zhang, Errui Ding, et al. R-cot: Reverse chain-of-thought problem generation for geometric reasoning in large multimodal models. *arXiv preprint arXiv:2410.17885*, 2024.\n- [48] Renrui Zhang, Xinyu Wei, Dongzhi Jiang, Ziyu Guo, Shicheng Li, Yichi Zhang, Chengzhuo Tong, Jiaming Liu, Aojun Zhou, Bin Wei, et al. Mavis: Mathematical visual instruction tuning with an automatic data engine. *arXiv preprint arXiv:2407.08739*, 2024.\n- [49] Wenhao Shi, Zhiqiang Hu, Yi Bin, Junhua Liu, Yang Yang, See-Kiong Ng, Lidong Bing, and Roy Ka-Wei Lee. Math-llava: Bootstrapping mathematical reasoning for multimodal large language models. *arXiv preprint arXiv:2406.17294*, 2024.\n- [50] Jia Li, Edward Beeching, Lewis Tunstall, Ben Lipkin, Roman Soletskyi, Shengyi Huang, Kashif Rasul, Longhui Yu, Albert Q Jiang, Ziju Shen, et al. Numinamath: The largest public dataset in ai4maths with 860k pairs of competition math problems and solutions. *Hugging Face repository*, 13:9, 2024.\n- [51] Yuxuan Tong, Xiwen Zhang, Rui Wang, Ruidong Wu, and Junxian He. Dart-math: Difficulty-aware rejection tuning for mathematical problem-solving. *Advances in Neural Information Processing Systems*, 37:7821–7846, 2024.\n- [52] Chaoqun He, Renjie Luo, Yuzhuo Bai, Shengding Hu, Zhen Leng Thai, Junhao Shen, Jinyi Hu, Xu Han, Yujie Huang, Yuxiang Zhang, et al. Olympiadbench: A challenging benchmark for promoting agi with olympiad-level bilingual multimodal scientific problems. *arXiv preprint arXiv:2402.14008*, 2024.\n- [53] Pan Lu, Hritik Bansal, Tony Xia, Jiacheng Liu, Chunyuan Li, Hannaneh Hajishirzi, Hao Cheng, Kai-Wei Chang, Michel Galley, and Jianfeng Gao. Mathvista: Evaluating mathematical reasoning of foundation models in visual contexts. *arXiv preprint arXiv:2310.02255*, 2023.\n- [54] Renrui Zhang, Dongzhi Jiang, Yichi Zhang, Haokun Lin, Ziyu Guo, Pengshuo Qiu, Aojun Zhou, Pan Lu, Kai-Wei Chang, Yu Qiao, et al. Mathverse: Does your multi-modal llm truly see the diagrams in visual math problems? In *European Conference on Computer Vision*, pages 169–186. Springer, 2024.\n- [55] Ke Wang, Junting Pan, Weikang Shi, Zimu Lu, Houxing Ren, Aojun Zhou, Mingjie Zhan, and Hong-sheng Li. Measuring multimodal mathematical reasoning with math-vision dataset. *Advances in Neural Information Processing Systems*, 37:95095–95169, 2024.\n- [56] Jun Wang, Meng Fang, Ziyu Wan, Muning Wen, Jiachen Zhu, Anjie Liu, Ziqin Gong, Yan Song, Lei Chen, Lionel M Ni, et al. Openr: An open source framework for advanced reasoning with large language models. *arXiv preprint arXiv:2410.09671*, 2024.\n- [57] Shuai Peng, Di Fu, Liangcai Gao, Xiuqin Zhong, Hongguang Fu, and Zhi Tang. Multimath: Bridging visual and mathematical reasoning for large language models. *arXiv preprint arXiv:2409.00147*, 2024.\n- [58] Lei Li, Yuqi Wang, Runxin Xu, Peiyi Wang, Xiachong Feng, Lingpeng Kong, and Qi Liu. Multimodal arxiv: A dataset for improving scientific comprehension of large vision-language models. *arXiv preprint arXiv:2403.00231*, 2024.\n- [59] Wenwen Zhuang, Xin Huang, Xiantao Zhang, and Jin Zeng. Math-puma: Progressive upward multimodal alignment to enhance mathematical reasoning. In *Proceedings of the AAAI Conference on Artificial Intelligence*, volume 39, pages 26183–26191, 2025.- [60] Wenqi Zhang, Zhenglin Cheng, Yuanyu He, Mengna Wang, Yongliang Shen, Zeqi Tan, Guiyang Hou, Mingqian He, Yanna Ma, Weiming Lu, et al. Multimodal self-instruct: Synthetic abstract image and visual reasoning instruction using language model. *arXiv preprint arXiv:2407.07053*, 2024.\n- [61] Erfei Cui, Yinan He, Zheng Ma, Zhe Chen, Hao Tian, Weiyun Wang, Kunchang Li, Yi Wang, Wenhai Wang, Xizhou Zhu, Lewei Lu, Tong Lu, Yali Wang, Limin Wang, Yu Qiao, and Jifeng Dai. Sharegpt-4o: Comprehensive multimodal annotations with gpt-4o, 2024.\n- [62] Cyrile Delestre Tom Agonnoude, 2024.\n- [63] Aida Amini, Saadia Gabriel, Peter Lin, Rik Koncel-Kedziorski, Yejin Choi, and Hannaneh Hajishirzi. Mathqa: Towards interpretable math word problem solving with operation-based formalisms. *arXiv preprint arXiv:1905.13319*, 2019.\n- [64] PawanKrd. math-gpt-4o-200k. *Hugging Face repository*, 2024.\n- [65] Xiang Yue, Xingwei Qu, Ge Zhang, Yao Fu, Wenhao Huang, Huan Sun, Yu Su, and Wenhui Chen. Mammoth: Building math generalist models through hybrid instruction tuning. *arXiv preprint arXiv:2309.05653*, 2023.## Appendix\n\n### A Policy Model training data\n\nTable 3 summarizes the datasets and sample counts used to train the policy model.\n\nTable 3: Data sources and sample counts used for policy model training.\n\n&lt;table border=\"1\">&lt;thead>&lt;tr>&lt;th>Dataset&lt;/th>&lt;th>Sample Count&lt;/th>&lt;/tr>&lt;/thead>&lt;tbody>&lt;tr>&lt;td>R-CoT [47]&lt;/td>&lt;td>201,781&lt;/td>&lt;/tr>&lt;tr>&lt;td>MAVIS [48]&lt;/td>&lt;td>29,551&lt;/td>&lt;/tr>&lt;tr>&lt;td>multimath-300k [57]&lt;/td>&lt;td>224,747&lt;/td>&lt;/tr>&lt;tr>&lt;td>Multimodal ArXiv [58]&lt;/td>&lt;td>99,772&lt;/td>&lt;/tr>&lt;tr>&lt;td>MathV360K [49]&lt;/td>&lt;td>338,721&lt;/td>&lt;/tr>&lt;tr>&lt;td>Math-PUMA [59]&lt;/td>&lt;td>1,111,939&lt;/td>&lt;/tr>&lt;tr>&lt;td>Multi-modal-Self-instruct [60]&lt;/td>&lt;td>64,807&lt;/td>&lt;/tr>&lt;tr>&lt;td>MMPR [13]&lt;/td>&lt;td>1,055,796&lt;/td>&lt;/tr>&lt;tr>&lt;td>ShareGPT-4o [61]&lt;/td>&lt;td>57,289&lt;/td>&lt;/tr>&lt;tr>&lt;td>table-vqa [62]&lt;/td>&lt;td>80,054&lt;/td>&lt;/tr>&lt;tr>&lt;td>MathQA [63]&lt;/td>&lt;td>27,923&lt;/td>&lt;/tr>&lt;tr>&lt;td>GSM8K [19]&lt;/td>&lt;td>7,413&lt;/td>&lt;/tr>&lt;tr>&lt;td>DART-Math [51]&lt;/td>&lt;td>574,305&lt;/td>&lt;/tr>&lt;tr>&lt;td>math-gpt-4o-200k [64]&lt;/td>&lt;td>196,032&lt;/td>&lt;/tr>&lt;tr>&lt;td>NuminaMath-CoT [50]&lt;/td>&lt;td>807,883&lt;/td>&lt;/tr>&lt;tr>&lt;td>MathInstruct [65]&lt;/td>&lt;td>257,755&lt;/td>&lt;/tr>&lt;tr>&lt;td>&lt;b>Total&lt;/b>&lt;/td>&lt;td>&lt;b>5,135,768&lt;/b>&lt;/td>&lt;/tr>&lt;/tbody>&lt;/table>\n\n### B Prompt template for data cleaning\n\nThe prompt template used for data cleaning is shown below. Before generating logical steps and the final answer, the language model is first instructed to explicitly identify the key knowledge points involved in the problem, along with brief explanations. This two-stage prompting strategy enhances the model’s understanding of the question prior to solution restructuring.\n\nUsing the information provided, identify and summarize the key knowledge points required to solve the problem and rewrite the original answer with a detailed reasoning process based on the input answer.\n\nProvide a clear explanation of each knowledge point by stating its name followed by a colon (:), and then presenting the detailed Explanation on the same line.\n\nWhen explaining the knowledge point, DO NOT reference or describe the original question, answer, or answer details. Focus solely on explaining the knowledge points.\n\nBesides, rewrite the original answer to include detailed reasoning and answer. Do not change the final answer and always refer to the input answer.\n\nOutput Format:\n\nIn order to answer this question, we first need to have the following prior knowledge:\n\n{{Substitute with name of knowledge point 1}}: {{Substitute with Explanation of knowledge point 1}},  \n{{Substitute with name of knowledge point 2}}: {{Substitute with Explanation of knowledge point 2}},...\n\nWe answer this based on prior knowledge as follows:\n\nSolution: Refined answer with detailed reasoning. Use Step 1, Step 2 to divide the steps. Remember do not change the final answer and always refer to the input answer.\n\nAnswer: The Final Answer is {{Substitute with final answer}}.\n\nInput Information:\n\nQuestion: {question}\n\nAnswer: {answer}\n\n## C Aggregation function definitions\n\nIn the BoN inference setup, each reasoning path is assigned a vector of step-level scores predicted by the PRM. To compare and rank these paths, we apply an aggregation function to compress each score vector into a single scalar value, following the design considerations discussed in [40]. The following aggregation strategies are used in our experiments:\n\n- • Min: Computes the minimum of all step scores:\n\n$$\\text{score}(r_j) = \\min\\{p_1^{(j)}, p_2^{(j)}, \\dots, p_{T_j}^{(j)}\\}$$\n\n- • Max: Computes the maximum of all step scores:\n\n$$\\text{score}(r_j) = \\max\\{p_1^{(j)}, p_2^{(j)}, \\dots, p_{T_j}^{(j)}\\}$$\n\n- • Average: Computes the arithmetic mean of all step scores:\n\n$$\\text{score}(r_j) = \\frac{1}{T_j} \\sum_{i=1}^{T_j} p_i^{(j)}$$\n\n- • SumLogPr: Computes the sum of log-probabilities of all step scores:\n\n$$\\text{score}(r_j) = \\sum_{i=1}^{T_j} \\log p_i^{(j)} = \\log \\prod_{i=1}^{T_j} p_i^{(j)}$$\n\n- • SumLogOdds: Computes the sum of log-odds of all step scores:\n\n$$\\text{score}(r_j) = \\sum_{i=1}^{T_j} \\log \\frac{p_i^{(j)}}{1 - p_i^{(j)}}$$\n\n- • MeanOdds: Computes the mean of odds-transformed step scores:\n\n$$\\text{score}(r_j) = \\frac{1}{T_j} \\sum_{i=1}^{T_j} \\frac{p_i^{(j)}}{1 - p_i^{(j)}}$$\n\nHere,  $r_j$  denotes the  $j$ -th reasoning path consisting of  $T_j$  steps, and  $p_i^{(j)} \\in (0, 1)$  is the predicted correctness probability of the  $i$ -th step in that path.## D Full evaluation results\n\n### D.1 MM-Policy\n\nTable 4: Performance comparison of various aggregators on various benchmarks for MM-Policy. Top performer is in **bold**.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Benchmark&lt;/th>\n&lt;th>Random&lt;/th>\n&lt;th>Min&lt;/th>\n&lt;th>Average&lt;/th>\n&lt;th>Max&lt;/th>\n&lt;th>SumLogPr&lt;/th>\n&lt;th>SumLogOdds&lt;/th>\n&lt;th>MeanOdds&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>MM-K12&lt;/td>\n&lt;td>33.9&lt;/td>\n&lt;td>37.4&lt;/td>\n&lt;td>43.0&lt;/td>\n&lt;td>&lt;b>43.4&lt;/b>&lt;/td>\n&lt;td>42.0&lt;/td>\n&lt;td>43.2&lt;/td>\n&lt;td>42.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>OlympiadBench&lt;/td>\n&lt;td>15.4&lt;/td>\n&lt;td>23.3&lt;/td>\n&lt;td>20.0&lt;/td>\n&lt;td>&lt;b>24.7&lt;/b>&lt;/td>\n&lt;td>22.7&lt;/td>\n&lt;td>24.0&lt;/td>\n&lt;td>24.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MathVista&lt;/td>\n&lt;td>62.9&lt;/td>\n&lt;td>66.0&lt;/td>\n&lt;td>67.2&lt;/td>\n&lt;td>&lt;b>67.7&lt;/b>&lt;/td>\n&lt;td>66.4&lt;/td>\n&lt;td>&lt;b>67.7&lt;/b>&lt;/td>\n&lt;td>67.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MathVerse&lt;/td>\n&lt;td>43.0&lt;/td>\n&lt;td>46.0&lt;/td>\n&lt;td>48.0&lt;/td>\n&lt;td>46.1&lt;/td>\n&lt;td>47.3&lt;/td>\n&lt;td>&lt;b>48.0&lt;/b>&lt;/td>\n&lt;td>46.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MathVision&lt;/td>\n&lt;td>21.7&lt;/td>\n&lt;td>25.8&lt;/td>\n&lt;td>26.7&lt;/td>\n&lt;td>26.9&lt;/td>\n&lt;td>25.4&lt;/td>\n&lt;td>26.3&lt;/td>\n&lt;td>&lt;b>27.1&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n### D.2 InternVL-8B\n\nTable 5: Performance comparison of various aggregators on various benchmarks for InternVL-8B. Top performer is in **bold**.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Benchmark&lt;/th>\n&lt;th>Random&lt;/th>\n&lt;th>Min&lt;/th>\n&lt;th>Average&lt;/th>\n&lt;th>Max&lt;/th>\n&lt;th>SumLogPr&lt;/th>\n&lt;th>SumLogOdds&lt;/th>\n&lt;th>MeanOdds&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>MM-K12&lt;/td>\n&lt;td>27.0&lt;/td>\n&lt;td>34.8&lt;/td>\n&lt;td>36.0&lt;/td>\n&lt;td>35.8&lt;/td>\n&lt;td>31.2&lt;/td>\n&lt;td>34.2&lt;/td>\n&lt;td>&lt;b>37.8&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>OlympiadBench&lt;/td>\n&lt;td>5.2&lt;/td>\n&lt;td>2.7&lt;/td>\n&lt;td>15.3&lt;/td>\n&lt;td>&lt;b>16.7&lt;/b>&lt;/td>\n&lt;td>2.0&lt;/td>\n&lt;td>1.3&lt;/td>\n&lt;td>15.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MathVista&lt;/td>\n&lt;td>56.4&lt;/td>\n&lt;td>63.4&lt;/td>\n&lt;td>62.8&lt;/td>\n&lt;td>62.6&lt;/td>\n&lt;td>61.0&lt;/td>\n&lt;td>62.0&lt;/td>\n&lt;td>&lt;b>63.5&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MathVerse&lt;/td>\n&lt;td>36.3&lt;/td>\n&lt;td>41.8&lt;/td>\n&lt;td>&lt;b>42.8&lt;/b>&lt;/td>\n&lt;td>41.1&lt;/td>\n&lt;td>42.0&lt;/td>\n&lt;td>42.8&lt;/td>\n&lt;td>42.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MathVision&lt;/td>\n&lt;td>10.0&lt;/td>\n&lt;td>6.1&lt;/td>\n&lt;td>18.4&lt;/td>\n&lt;td>&lt;b>20.6&lt;/b>&lt;/td>\n&lt;td>3.8&lt;/td>\n&lt;td>4.8&lt;/td>\n&lt;td>19.4&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n### D.3 InternVL-26B\n\nTable 6: Performance comparison of various aggregators on various benchmarks for InternVL-26B. Top performer is in **bold**.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Benchmark&lt;/th>\n&lt;th>Random&lt;/th>\n&lt;th>Min&lt;/th>\n&lt;th>Average&lt;/th>\n&lt;th>Max&lt;/th>\n&lt;th>SumLogPr&lt;/th>\n&lt;th>SumLogOdds&lt;/th>\n&lt;th>MeanOdds&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>MM-K12&lt;/td>\n&lt;td>28.0&lt;/td>\n&lt;td>&lt;b>38.0&lt;/b>&lt;/td>\n&lt;td>37.2&lt;/td>\n&lt;td>35.4&lt;/td>\n&lt;td>32.0&lt;/td>\n&lt;td>33.0&lt;/td>\n&lt;td>&lt;b>38.0&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>OlympiadBench&lt;/td>\n&lt;td>14.5&lt;/td>\n&lt;td>16.0&lt;/td>\n&lt;td>23.3&lt;/td>\n&lt;td>22.0&lt;/td>\n&lt;td>16.7&lt;/td>\n&lt;td>16.7&lt;/td>\n&lt;td>24.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MathVista&lt;/td>\n&lt;td>60.0&lt;/td>\n&lt;td>63.9&lt;/td>\n&lt;td>&lt;b>64.6&lt;/b>&lt;/td>\n&lt;td>64.4&lt;/td>\n&lt;td>62.8&lt;/td>\n&lt;td>64.2&lt;/td>\n&lt;td>64.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MathVerse&lt;/td>\n&lt;td>37.8&lt;/td>\n&lt;td>42.0&lt;/td>\n&lt;td>44.2&lt;/td>\n&lt;td>&lt;b>44.3&lt;/b>&lt;/td>\n&lt;td>40.1&lt;/td>\n&lt;td>41.5&lt;/td>\n&lt;td>44.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MathVision&lt;/td>\n&lt;td>20.8&lt;/td>\n&lt;td>23.3&lt;/td>\n&lt;td>24.1&lt;/td>\n&lt;td>24.9&lt;/td>\n&lt;td>20.6&lt;/td>\n&lt;td>22.0&lt;/td>\n&lt;td>&lt;b>25.6&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n### D.4 InternVL-38B\n\nTable 7: Performance comparison of various aggregators on various benchmarks for InternVL-38B. Top performer is in **bold**.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Benchmark&lt;/th>\n&lt;th>Random&lt;/th>\n&lt;th>Min&lt;/th>\n&lt;th>Average&lt;/th>\n&lt;th>Max&lt;/th>\n&lt;th>SumLogPr&lt;/th>\n&lt;th>SumLogOdds&lt;/th>\n&lt;th>MeanOdds&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>MM-K12&lt;/td>\n&lt;td>40.3&lt;/td>\n&lt;td>46.8&lt;/td>\n&lt;td>51.0&lt;/td>\n&lt;td>49.8&lt;/td>\n&lt;td>42.8&lt;/td>\n&lt;td>46.6&lt;/td>\n&lt;td>&lt;b>52.4&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>OlympiadBench&lt;/td>\n&lt;td>29.6&lt;/td>\n&lt;td>29.3&lt;/td>\n&lt;td>34.0&lt;/td>\n&lt;td>&lt;b>34.7&lt;/b>&lt;/td>\n&lt;td>28.0&lt;/td>\n&lt;td>30.0&lt;/td>\n&lt;td>32.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MathVista&lt;/td>\n&lt;td>68.3&lt;/td>\n&lt;td>70.5&lt;/td>\n&lt;td>&lt;b>71.1&lt;/b>&lt;/td>\n&lt;td>70.5&lt;/td>\n&lt;td>69.2&lt;/td>\n&lt;td>70.1&lt;/td>\n&lt;td>&lt;b>71.1&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MathVerse&lt;/td>\n&lt;td>47.9&lt;/td>\n&lt;td>50.4&lt;/td>\n&lt;td>51.9&lt;/td>\n&lt;td>51.1&lt;/td>\n&lt;td>51.1&lt;/td>\n&lt;td>52.7&lt;/td>\n&lt;td>&lt;b>52.6&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MathVision&lt;/td>\n&lt;td>29.7&lt;/td>\n&lt;td>29.1&lt;/td>\n&lt;td>32.6&lt;/td>\n&lt;td>&lt;b>33.6&lt;/b>&lt;/td>\n&lt;td>30.6&lt;/td>\n&lt;td>31.3&lt;/td>\n&lt;td>33.0&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>## D.5 InternVL-78B\n\nTable 8: Performance comparison of various aggregators on various benchmarks for InternVL-78B. Top performer is in **bold**.\n\n&lt;table border=\"1\">&lt;thead>&lt;tr>&lt;th>Benchmark&lt;/th>&lt;th>Random&lt;/th>&lt;th>Min&lt;/th>&lt;th>Average&lt;/th>&lt;th>Max&lt;/th>&lt;th>SumLogPr&lt;/th>&lt;th>SumLogOdds&lt;/th>&lt;th>MeanOdds&lt;/th>&lt;/tr>&lt;/thead>&lt;tbody>&lt;tr>&lt;td>MM-K12&lt;/td>&lt;td>42.2&lt;/td>&lt;td>46.2&lt;/td>&lt;td>47.2&lt;/td>&lt;td>47.2&lt;/td>&lt;td>45.0&lt;/td>&lt;td>46.8&lt;/td>&lt;td>&lt;b>48.8&lt;/b>&lt;/td>&lt;/tr>&lt;tr>&lt;td>OlympiadBench&lt;/td>&lt;td>31.0&lt;/td>&lt;td>33.3&lt;/td>&lt;td>35.3&lt;/td>&lt;td>&lt;b>34.7&lt;/b>&lt;/td>&lt;td>33.3&lt;/td>&lt;td>&lt;b>34.7&lt;/b>&lt;/td>&lt;td>&lt;b>34.7&lt;/b>&lt;/td>&lt;/tr>&lt;tr>&lt;td>MathVista&lt;/td>&lt;td>69.5&lt;/td>&lt;td>71.7&lt;/td>&lt;td>73.4&lt;/td>&lt;td>72.4&lt;/td>&lt;td>&lt;b>73.9&lt;/b>&lt;/td>&lt;td>73.6&lt;/td>&lt;td>73.2&lt;/td>&lt;/tr>&lt;tr>&lt;td>MathVerse&lt;/td>&lt;td>50.2&lt;/td>&lt;td>53.4&lt;/td>&lt;td>55.0&lt;/td>&lt;td>54.2&lt;/td>&lt;td>54.3&lt;/td>&lt;td>&lt;b>55.1&lt;/b>&lt;/td>&lt;td>54.5&lt;/td>&lt;/tr>&lt;tr>&lt;td>MathVision&lt;/td>&lt;td>31.5&lt;/td>&lt;td>30.1&lt;/td>&lt;td>33.5&lt;/td>&lt;td>&lt;b>33.6&lt;/b>&lt;/td>&lt;td>31.8&lt;/td>&lt;td>32.4&lt;/td>&lt;td>33.3&lt;/td>&lt;/tr>&lt;/tbody>&lt;/table>\n\n## E Limitations\n\nWhile our proposed framework demonstrates strong performance and generalization across multiple benchmarks, it also has several limitations: (1) Due to computational constraints, we conduct training only on the InternVL series with 8B parameters, without exploring larger models or architectures from other model families. This restricts our ability to fully assess how PRM training behavior scales with model size or generalizes across different backbones. (2) The seed data used for process supervision generation is limited in diversity, as it consists solely of K-12 math problems. As a result, the PRM may be less exposed to advanced mathematical domains or visual formats beyond the scope of standard educational settings. We leave broader model coverage and more diverse seed data construction as promising directions for future work.\n",
    "durationMs": 960,
    "url": "https://huggingface.co/papers/2505.13427"
  },
  "sourceToolAssistantUUID": "2b55a73d-6116-46b2-891c-3c17bbec9fcf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-27T16:08:41.727Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Hbk3NerdUmw94JLVQbEs6c`</summary>

```json
{
  "url": "https://paper-reader.com/paper/2505.13427",
  "prompt": "Extract the FULL text of all sections from this paper MM-PRM, including:\n1. Introduction\n2. Method / Approach (all subsections)\n3. Experiments and Results (all tables and numbers)\n4. Conclusion and Limitations\nBe as thorough and detailed as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b0db963-9cf8-4e9a-8653-bbc4dd20a779",
  "isSidechain": false,
  "requestId": "req_011CbTN1pPasTK9xnoMHedXC",
  "type": "assistant",
  "uuid": "7cce7330-f580-492c-a31b-80463185a80a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ADuUWmrxQnowX3b9KuhBt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 724,
      "cache_read_input_tokens": 14578,
      "output_tokens": 294,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 724,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 294,
          "cache_read_input_tokens": 14578,
          "cache_creation_input_tokens": 724,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 724
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

_source line 27_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-27 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "7cce7330-f580-492c-a31b-80463185a80a",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze MM-PRM paper for research methodology",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d"
}
```

---

### Tool result

_source line 29 · 2026-05-27T16:08:41.929Z_

<details><summary>↩ Tool result · reported error · `toolu_01Hbk3NerdUmw94JLVQbEs6c`</summary>

```text
ECONNREFUSED
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7cce7330-f580-492c-a31b-80463185a80a",
  "isSidechain": false,
  "promptId": "de34c998-fd7f-4a40-bbbf-9dd4b01a6eef",
  "type": "user",
  "uuid": "c19aac98-58ef-4185-8ca8-39b846f35d1a",
  "toolUseResult": "Error: ECONNREFUSED",
  "sourceToolAssistantUUID": "7cce7330-f580-492c-a31b-80463185a80a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-27T16:08:49.220Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Sf7gfAkwQWx2eVeuyALPL2`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/0243be30-7aad-4e4c-9062-bffffcde4a0d/tool-results/toolu_01CJZk2jcExqUgc2uZJAKdou.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c19aac98-58ef-4185-8ca8-39b846f35d1a",
  "isSidechain": false,
  "requestId": "req_011CbTN2G5B1oVSKPhvmBeZg",
  "type": "assistant",
  "uuid": "19b5f523-a18f-4eaf-9ac2-0427b5461736",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KHTZYPGy6L8xnX1quA2Qfe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 985,
      "cache_read_input_tokens": 15302,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 985,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 129,
          "cache_read_input_tokens": 15302,
          "cache_creation_input_tokens": 985,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 985
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

_source line 31 · 2026-05-27T16:08:49.508Z_

<details><summary>↩ Tool result · `toolu_01Sf7gfAkwQWx2eVeuyALPL2`</summary>

```text
1	# MM-PRM: Enhancing Multimodal Mathematical Reasoning with Scalable Step-Level Supervision
2	
3	Lingxiao Du&lt;sup>1,\*&lt;/sup> Fanqing Meng&lt;sup>1,3,\*&lt;/sup> Zongkai Liu&lt;sup>2,\*&lt;/sup> Zhixiang Zhou&lt;sup>2,\*&lt;/sup>  
4	Ping Luo&lt;sup>4&lt;/sup> Qiaosheng Zhang&lt;sup>1,2,†&lt;/sup> Wenqi Shao&lt;sup>1,2,†&lt;/sup>
5	
6	&lt;sup>1&lt;/sup>Shanghai AI Laboratory &lt;sup>2&lt;/sup>Shanghai Innovation Institute  
7	&lt;sup>3&lt;/sup>Shanghai Jiao Tong University &lt;sup>4&lt;/sup>The University of Hong Kong
8	
9	## Abstract
10	
11	While Multimodal Large Language Models (MLLMs) have achieved impressive progress in vision-language understanding, they still struggle with complex multi-step reasoning, often producing logically inconsistent or partially correct solutions. A key limitation lies in the lack of fine-grained supervision over intermediate reasoning steps. To address this, we propose MM-PRM, a process reward model trained within a fully automated, scalable framework. We first build MM-Policy, a strong multimodal model trained on diverse mathematical reasoning data. Then, we construct MM-K12, a curated dataset of 10,000 multimodal math problems with verifiable answers, which serves as seed data. Leveraging a Monte Carlo Tree Search (MCTS)-based pipeline, we generate over 700k step-level annotations without human labeling. The resulting PRM is used to score candidate reasoning paths in the Best-of-N inference setup and achieves significant improvements across both in-domain (MM-K12 test set) and out-of-domain (OlympiadBench, MathVista, etc.) benchmarks. Further analysis confirms the effectiveness of soft labels, smaller learning rates, and path diversity in optimizing PRM performance. MM-PRM demonstrates that process supervision is a powerful tool for enhancing the logical robustness of multimodal reasoning systems. We release all our codes and data at &lt;https://github.com/ModalMinds/MM-PRM>.
12	
13	## 1 Introduction
14	
15	The rapid advancement of Large Language Models (LLMs) [1, 2, 3, 4, 5, 6, 7, 8, 9] has significantly improved performance on a wide range of natural language processing tasks, including general reasoning and mathematical problem-solving. In parallel, the development of Multimodal Large Language Models (MLLMs) [10, 11, 12, 13, 14, 15, 16, 17, 18] has unlocked new capabilities in vision-language understanding, showing promising results in areas such as image captioning and visual question answering (VQA). However, despite their impressive capabilities in perception and basic reasoning, MLLMs still struggle with complex multi-step reasoning tasks, particularly in mathematics. These shortcomings often manifest as broken logical chains, inaccurate intermediate steps, or cases that produce incorrect intermediate steps while still occasionally arriving at the correct final answer—a phenomenon that introduces high false-positive rates and undermines interpretability.
16	
17	To address this issue, reward modeling [19, 20, 21, 22] has emerged as a promising paradigm. Reward models (RMs) play a central role in reinforcement learning from human feedback (RLHF) [23, 24, 25, 26, 27, 28], and can also be used at inference time to select among multiple candidate responses using Test-Time Scaling (TTS) [29, 30, 31, 32, 33, 34, 35, 36, 37] strategies such as Best-of-N (BoN). In general, reward models for reasoning tasks can be broadly categorized into two types: Outcome Reward Models (ORMs) and Process Reward Models (PRMs). ORMs [19, 20] provide
18	
19	\*Equal contribution
20	
21	†Corresponding Authors: shaowenqi@pjlab.org.cn; zhangqiaosheng@pjlab.org.cnscalar feedback only on the final answer, overlooking the quality of the intermediate reasoning steps. This limits their ability to guide the model toward robust reasoning paths. In contrast, PRMs [38, 39, 21, 31, 40, 41] offer a more fine-grained approach by evaluating each reasoning step, enabling more accurate and interpretable feedback.
22	
23	Some recent works have explored process reward models for mathematical reasoning in pure text. PRM800k [39] manually constructs a large-scale dataset with step-level correctness labels, which is hard to scale. MathShepherd [31] adopts Monte Carlo estimation to label reasoning steps by evaluating whether continuations from a given step lead to the correct answer, but its efficiency is relatively low. OmegaPRM [41] introduces a Monte Carlo Tree Search (MCTS)-based framework that enables efficient automated generation of process supervision data. However, all these works focus on mathematical reasoning in pure text. In the field of multimodal mathematical reasoning, how to design an efficient framework for process supervision data generation and stably train process reward models remains a challenging problem.
24	
25	To address these challenges, we propose **MM-PRM**, a powerful process reward model that effectively handles both in-domain and out-of-domain problems. Specifically, we first collect a large-scale, high-quality reasoning dataset and refine its format to train a policy model called **MM-Policy** with strong reasoning abilities and well-structured output. Inspired by OmegaPRM, we then establish an efficient multimodal process annotation framework. We first collect 10k high-quality K-12-level multimodal mathematical reasoning samples, named **MM-K12**. Starting with only 10k math problems as seed data, our framework automatically generates over 700k step-level annotations without any human supervision. Finally, we train MM-PRM with these data and evaluate its performance on multiple benchmarks using the BoN approach.
26	
27	MM-PRM demonstrates strong performance and generalization across multiple benchmarks. Although we only use process data generated from K-12-level math problems for training, MM-PRM achieves remarkable results with MM-Policy on benchmarks such as MathVista that improves from 62.93% to 67.60%. In addition, even though MM-PRM is trained on data produced by MM-Policy, it still delivers competitive results on other models like InternVL2.5-8B and InternVL2.5-78B. For instance, on the self-collected MM-K12 test set, InternVL2.5-8B improves from 27.01% to 37.80%, and on MathVerse, InternVL2.5-78B improves from 50.18% to 54.47%. These results highlight MM-PRM’s ability to generalize both across datasets and across model size, despite being trained on limited and fixed data sources.
28	
29	Finally, we provide a detailed discussion on key factors in PRM training, including learning rate and the choice between soft labels and hard labels. We find that the following factors are essential for stable PRM training: (1) using a small learning rate to ensure stable optimization; (2) adopting soft labels instead of hard thresholding to reduce noise and preserve step-wise uncertainty.
30	
31	In summary, our contributions are as follows:
32	
33	- • We collect and release **MM-K12**, a curated multimodal math dataset containing 10,000 seed problems and 500 test problems, all verified to contain unique, checkable answers.
34	- • We build a policy model named **MM-Policy** using a large corpus of mathematical reasoning data, and develop a fully automated, MCTS-based pipeline for scalable process supervision generation. Leveraging MM-Policy and only 10k seed problems from MM-K12, our framework produces over 700k step-level annotations without human supervision. Based on this, we train **MM-PRM**, which demonstrates strong performance across multiple benchmarks—for example, boosting accuracy on the MM-K12 test set from 33.92% to 42.80%, on MathVista from 62.93% to 67.60%, and on OlympiadBench from 15.41% to 24.00%.
35	- • We provide a detailed discussion on the settings of key parameters such as the type of process labels and the learning rate. We summarize the key factors for stable PRM training, which can help the community train PRM models more effectively.
36	
37	## 2 Related work
38	
39	### 2.1 Mathematical reasoning and reward modeling in LLMs
40	
41	Mathematical reasoning has become a focal point in evaluating the deep logical abilities of LLMs. [19, 42]. Unlike general language tasks, mathematical problems demand precise multi-step reasoningand logical coherence, motivating approaches like Chain-of-Thought (CoT) prompting[43] and Self-Consistency sampling [44]. Supervised fine-tuning (SFT) with structured solution datasets further reinforces reasoning performance, as demonstrated by models like Qwen [2], InternLM [7], and Gemini [3]. More recently, reinforcement learning (RL)-based optimization, exemplified by OpenAI’s o1 [45] and DeepSeek R1 [9], has emerged as a powerful strategy that surpassing SFT-only baselines.
42	
43	However, despite these advances, current LLMs still frequently produce logically inconsistent reasoning steps or false-positive solutions. To address this issue, reward modeling techniques have emerged. Traditional Outcome Reward Models (ORMs)[19, 20], which assign rewards based solely on the final answer, fail to detect flawed intermediate reasoning. Process Reward Models (PRMs)[39, 31, 40, 41] overcome this limitation by explicitly providing step-level supervision, significantly improving logical coherence. Representative works such as PRM800K [39], MathShepherd [31], and MiPS [40] have demonstrated the effectiveness of PRMs in enhancing mathematical reasoning. During the preparation of this manuscript, we became aware of a concurrent effort, URSA [46], which also explores PRM training. While both approaches share some methodological similarities in PRM construction, our work places greater emphasis on building a scalable PRM pipeline and analyzing training dynamics, whereas URSA focuses more on integrating PRMs into RL.
44	
45	Overall, PRMs have become an essential approach for improving the robustness and logical consistency of LLM reasoning through fine-grained, step-level evaluation.
46	
47	## 2.2 Process supervision data construction
48	
49	Training PRMs requires large-scale, high-quality step-level annotations that indicate the correctness of each intermediate reasoning step. However, most publicly available datasets focus solely on final answers, making it challenging to obtain supervision signals for reasoning quality. Existing process supervision construction methods can be broadly categorized into three classes:
50	
51	**Manual Annotation.** The earliest efforts, such as PRM800K [39], relied on human experts to label each reasoning step. While this yields high-quality annotations, the approach is costly, time-consuming, and difficult to scale—particularly for domains like mathematics where expert knowledge is required.
52	
53	**Monte Carlo Estimation.** Works like MathShepherd [31] and MiPS [40] automate supervision by sampling multiple rollouts from each reasoning prefix and estimating step correctness based on the proportion of successful completions. If continuations from a given step often lead to correct answers, that step is considered reliable. This method is simple but suffers from label instability due to high variance in sampled rollouts—especially on long or complex reasoning chains.
54	
55	**Monte Carlo Tree Search (MCTS).** To address these limitations, OmegaPRM [41] introduces a structured, search-based alternative. Using a divide-and-conquer MCTS algorithm, it efficiently identifies the first error in a reasoning chain and constructs a tree of reasoning paths with dynamically updated statistics. This approach improves annotation stability, better handles deep reasoning tasks, and generates large volumes of fine-grained supervision from limited seed data without human input.
56	
57	Each method reflects a trade-off between cost, scalability, and label fidelity. Among them, MCTS-based approaches have recently emerged as the most effective strategy for generating robust and scalable process supervision, especially for multi-step mathematical reasoning tasks.
58	
59	# 3 Method
60	
61	## 3.1 Overview
62	
63	We present a scalable and fully automated framework for training PRMs tailored to multimodal mathematical reasoning. Our approach addresses two critical bottlenecks in prior work: **the lack of step-level supervision** and the **inefficiency of data generation in complex reasoning tasks**. To overcome these challenges, we introduce a structured three-stage pipeline that enables fine-grained reward modeling without any human annotation. As shown in Figure 1, the framework comprises three interconnected stages as follows:Figure 1: Overview of our automated three-stage framework for training MM-PRM: supervised policy model construction, MCTS-based process supervision data generation, and step-level reward model training.
64	
65	1. (1) **Policy Model Construction**, where a multimodal policy model is trained to generate high-quality reasoning traces following the CoT paradigm.
66	2. (2) **Process Supervision Data Generation**, where we use a MCTS-based engine, OmegaPRM [41], to efficiently identify reasoning flaws and produce step-level reward labels at scale.
67	3. (3) **Process Reward Model Training**, where a PRM is trained to evaluate each reasoning step and provide dense feedback.
68	
69	This end-to-end design ensures that process supervision can be generated, modeled, and applied in a fully closed loop. It significantly improves reasoning quality and robustness, especially in tasks requiring long logical chains. In Sections 3.2–3.3 below, we elaborate on these three stages.
70	
71	### 3.2 Policy model construction
72	
73	The policy model serves as the foundation of our framework, responsible for generating candidate reasoning trajectories given multimodal math problems. These trajectories are later evaluated and labeled to form step-level supervision for training the PRM. Ensuring that the policy model produces logically coherent and structurally complete outputs is thus essential for the effectiveness of the entire system.
74	
75	To train the policy model, we curated a large-scale, high-quality dataset of mathematical problems spanning a wide range of topics and difficulty levels. Our dataset integrates samples from over a dozen public math datasets, including R-CoT [47], MAVIS [48], MathV360K [49], NuminaMath [50], and DART-Math [51], with problems ranging from elementary school arithmetic to advanced geometry and statistics. The full list of data sources and sample counts used for training is provided in Appendix A.
76	
77	Once collected, all data undergo rigorous cleaning and format standardization. Visual and textual content are paired explicitly, and reasoning traces are reformatted to follow a structured CoT schema, with each logical step clearly marked using structured tags such as `&lt;step>&lt;/step>`, and the final conclusion labeled with `&lt;answer>&lt;/answer>`. To enhance quality and clarity, we leveraged a strong instruction-tuned language model (i.e., Qwen2.5-72B-Instruct [2]) to parse original solutions and restructure them into coherent, modular steps. This structured representation not only enhances model learnability but also lays the foundation for generating step-level reward labels in the next stage. The prompt used for solution restructuring is provided in Appendix B.With this cleaned and annotated corpus of over 5 million examples, we fine-tuned a strong open-source multimodal model, InternVL2.5-8B [16], using supervised learning. This ensures that the model learns to produce logically sound and well-structured outputs that conform to the CoT reasoning pattern.
78	
79	The resulting model not only delivers high-quality reasoning trajectories for downstream data annotation but also supports inference-time use cases such as BoN selection with reward-based reranking. Its strong generative ability and logical consistency form the cornerstone of our scalable process supervision framework.
80	
81	### 3.3 Process supervision data generation
82	
83	To enable fine-grained supervision for step-level reasoning, we adopt an automated process annotation pipeline based on the OmegaPRM [41] framework. OmegaPRM introduces a MCTS-based mechanism for efficiently identifying and labeling intermediate reasoning steps with confidence estimates. Although originally developed for textual mathematical reasoning, we adapt and extend this framework to handle multimodal inputs.
84	
85	Our process begins with collecting a curated dataset of 10,000 multimodal math problems from real-world named **MM-K12**—consisting of 5,000 fill-in-the-blank and 5,000 multiple-choice questions. These problems span a range of curriculum topics from elementary to high school and serve as seed instances for process supervision generation. All examples in MM-K12 are carefully filtered to ensure that each question includes meaningful visual input and has a unique, verifiable answer, making them well-suited for structured reasoning and reward modeling. In addition, MM-K12 also provides an independent test set of 500 problems, constructed under the same criteria, which we use to evaluate in-distribution performance later. For each problem, the policy model produces multiple candidate solutions following the CoT paradigm, and these reasoning paths form the raw material for subsequent reward annotation.
86	
87	To evaluate the correctness of each intermediate step, we follow OmegaPRM’s hierarchical rollout and search protocol. Specifically, we generate multiple completions (rollouts) from partial prefixes and estimate the correctness of a given step based on whether its downstream completions reach the correct final answer. By applying binary search, the algorithm efficiently pinpoints the earliest step at which the reasoning begins to deviate. These supervision signals are then aggregated within a structured state-action tree, which records the Monte Carlo (MC) estimates and other statistics at each reasoning state. In our implementation, we maintain the full multimodal context—including both textual and visual components—throughout the tree construction and search process.
88	
89	Importantly, our adaptation retains the efficiency of OmegaPRM’s divide-and-conquer search while enabling reward supervision for reasoning steps that are conditioned on complex visual stimuli. Through this pipeline, we generate over 700,000 step-level annotations from only 10k seed questions, without requiring manual labeling. The resulting dataset provides dense, high-quality process supervision aligned with real-world multimodal reasoning.
90	
91	### 3.4 Process reward model training
92	
93	With large-scale step-level supervision in place, we proceed to train a PRM that can assess the quality of reasoning steps given a multimodal context. The PRM is designed to serve as a fine-grained critic, assigning a reward score to each intermediate step conditioned on its preceding reasoning context that enables both test-time scaling and potential RL applications.
94	
95	#### 3.4.1 Labeling strategy
96	
97	A central design decision in PRM training lies in how to formulate supervision signals from the MC estimations [41, 32]. Rather than adopting hard binary label (e.g.,  $\hat{y} = 1[\text{MC}(s) > \tau]$ ), we use soft label, directly taking the MC scores as continuous supervision targets.
98	
99	This choice is motivated by the observation that the MC score reflects more than the correctness of an intermediate step. It also encodes factors such as problem difficulty, step criticality, and distributional uncertainty in the policy model’s rollouts. For instance, a reasoning step within a highly ambiguous or visually complex problem may yield lower MC scores even if the logic is fundamentally sound. In such cases, hard-thresholding may misrepresent the step’s quality, introducing noise into training. Bycontrast, soft labels preserve the probabilistic nuance and enable smoother learning dynamics, more details will be discussed in section 5.3
100	
101	Formally, for each reasoning step  $x_t$  in a path  $x = [x_1, x_2, \dots, x_T]$ , we assign a supervision target  $\hat{y}_t = \text{MC}(x_{&lt;t}) \in [0, 1]$ , where  $\text{MC}(x_{&lt;t})$  denotes the estimated probability that a correct final answer can be reached from this partial path.
102	
103	### 3.4.2 Model design and training objective
104	
105	To model the prediction task, we treat the PRM as a classifier operating on each reasoning step. Given a multimodal input  $q$  and a generated reasoning trace  $[x_1, x_2, \dots, x_T]$ , we interleave a special marker token, denoted  $\sigma$ , after each step, producing an input sequence of the form:
106	
107	$$[q, x_1, \sigma, x_2, \sigma, \dots, x_T, \sigma].$$
108	
109	In our implementation,  $\sigma$  is instantiated as the token  $\langle \text{prm} \rangle$ . At each occurrence of  $\sigma$ , the model is tasked with producing a scalar confidence score indicating the likelihood that the immediately preceding step is logically correct. Formally, let  $z_{\text{Yes}}^{(i)}$  and  $z_{\text{No}}^{(i)}$  denote the unnormalized logits for binary labels ‘‘Yes’’ (correct) and ‘‘No’’ (incorrect) at the  $i$ -th occurrence of  $\sigma$ . The model’s predicted probability is computed via softmax:
110	
111	$$p^{(i)} = \frac{\exp(z_{\text{Yes}}^{(i)})}{\exp(z_{\text{Yes}}^{(i)}) + \exp(z_{\text{No}}^{(i)})}.$$
112	
113	The training objective is to minimize the **cross-entropy loss** between the predicted scores  $p^{(i)}$  and the soft labels  $\hat{y}^{(i)}$ , across all scoring points:
114	
115	$$\mathcal{L}_{\text{PRM}} = - \sum_{i=1}^T \left[ \hat{y}^{(i)} \cdot \log p^{(i)} + (1 - \hat{y}^{(i)}) \cdot \log(1 - p^{(i)}) \right].$$
116	
117	This formulation guides the model to make fine-grained assessments of reasoning steps, assigning higher confidence to those with stronger evidence of correctness.
118	
119	## 4 Experiments
120	
121	### 4.1 Experiments setup
122	
123	To validate the effectiveness of our proposed process reward modeling framework, we conduct a series of experiments, carefully configured to ensure fair, scalable, and reproducible results.
124	
125	**Policy model construction.** Our policy model (i.e., MM-Policy) is initialized from the multimodal backbone InternVL 2.5-8B and fine-tuned using approximately 4 million cleaned, structured math problems. The model is trained for 1 epoch with a batch size of 128 and a learning rate of 4e-5, updating only the language module while keeping the vision encoder frozen.
126	
127	**Process supervision data generation.** We adapt the OmegaPRM[41] pipeline for multimodal reasoning and apply it to MM-K12 (10k samples). Using MCTS-based structured rollouts, we generate approximately 747,000 step-level annotations. The sampling parameters are tuned for balance between diversity and efficiency:  $temperature = 1.0$ ,  $top_k = 50$ ,  $top_p = 0.9$ , exploration coefficient  $c_{\text{puct}} = 0.125$ , and up to 200 search steps or 1,000 total rollouts per problem.
128	
129	**Process reward model training.** We initialize the PRM from the fine-tuned policy model and train it for 1 epochs with a batch size of 512 and a learning rate of 4e-6.
130	
131	### 4.2 Evaluation strategies and benchmarks
132	
133	To assess the effectiveness of the proposed MM-PRM in improving reasoning quality, we adopt the BoN evaluation protocol. For each test problem, the policy model generates  $N = 16$  candidate reasoning paths independently. The PRM then scores each path step-by-step, producing a sequence of floating-point values representing the predicted quality of each intermediate step, the path with the highest score is selected as the final answer.Since PRM outputs a vector of step-wise confidence scores for each candidate path, a crucial component of our evaluation is the *aggregation function* [40] used to compress this vector into a scalar. We explore a diverse set of aggregation functions, including Min, Average, Max, SumLogPr (i.e., sum of log-probabilities), SumLogOdds (i.e., sum of log-odds), and MeanOdds (i.e., mean odds), each function captures different aspects of path quality. Additionally, a Random baseline is used for comparison, where the final answer is randomly sampled from the same set of 16 candidates. Formal definitions of all aggregation functions are provided in Appendix C.
134	
135	We evaluate performance using answer accuracy, defined as the proportion of final selected answers that match the ground truth. This metric directly reflects MM-PRM’s utility in guiding the selection of correct reasoning paths. To comprehensively evaluate our model’s performance and generalization, we conduct experiments on a range of multimodal math benchmarks, including MM-K12 (test set), OlympiadBench (OE\_MM\_maths\_en\_COMP) [52], MathVista(testmini) [53], MathVerse(testmini) [54], and MathVision(test) [55]. The MM-K12 test set serves as an in-distribution evaluation. For out-of-distribution assessment, we use the OE\_MM\_maths\_en\_COMP split of OlympiadBench, which contains open-ended multimodal questions from international math competitions, closely related in format to MM-K12 but significantly harder. To further test generalization, we include MathVista, which covers a wide range of visual mathematical tasks; MathVerse, which emphasizes understanding structured visual content; and MathVision, which targets abstract visual reasoning. These benchmarks provide a diverse and rigorous setting to measure both performance and generalization of our process reward modeling framework.
136	
137	### 4.3 Quantitative results
138	
139	Table 1: Performance improvements across various benchmarks when applying the MM-PRM to different models.
140	
141	&lt;table border="1">
142	&lt;thead>
143	&lt;tr>
144	&lt;th>Model&lt;/th>
145	&lt;th>MM-K12&lt;/th>
146	&lt;th>OlympiadBench&lt;/th>
147	&lt;th>MathVista&lt;/th>
148	&lt;th>MathVerse&lt;/th>
149	&lt;th>MathVision&lt;/th>
150	&lt;/tr>
151	&lt;/thead>
152	&lt;tbody>
153	&lt;tr>
154	&lt;td>MM-Policy&lt;/td>
155	&lt;td>33.92&lt;/td>
156	&lt;td>15.41&lt;/td>
157	&lt;td>62.93&lt;/td>
158	&lt;td>42.99&lt;/td>
159	&lt;td>21.74&lt;/td>
160	&lt;/tr>
161	&lt;tr>
162	&lt;td>+MM-PRM&lt;/td>
163	&lt;td>42.80&lt;/td>
164	&lt;td>24.00&lt;/td>
165	&lt;td>67.60&lt;/td>
166	&lt;td>46.27&lt;/td>
167	&lt;td>27.11&lt;/td>
168	&lt;/tr>
169	&lt;tr>
170	&lt;td>&lt;/td>
171	&lt;td>&lt;b>+8.88&lt;/b>&lt;/td>
172	&lt;td>&lt;b>+8.59&lt;/b>&lt;/td>
173	&lt;td>&lt;b>+4.67&lt;/b>&lt;/td>
174	&lt;td>&lt;b>+3.28&lt;/b>&lt;/td>
175	&lt;td>&lt;b>+5.37&lt;/b>&lt;/td>
176	&lt;/tr>
177	&lt;tr>
178	&lt;td>InternVL2.5-8B&lt;/td>
179	&lt;td>27.01&lt;/td>
180	&lt;td>5.23&lt;/td>
181	&lt;td>56.43&lt;/td>
182	&lt;td>36.26&lt;/td>
183	&lt;td>10.04&lt;/td>
184	&lt;/tr>
185	&lt;tr>
186	&lt;td>+MM-PRM&lt;/td>
187	&lt;td>37.80&lt;/td>
188	&lt;td>15.33&lt;/td>
189	&lt;td>63.50&lt;/td>
190	&lt;td>42.56&lt;/td>
191	&lt;td>19.41&lt;/td>
192	&lt;/tr>
193	&lt;tr>
194	&lt;td>&lt;/td>
195	&lt;td>&lt;b>+10.79&lt;/b>&lt;/td>
196	&lt;td>&lt;b>+10.10&lt;/b>&lt;/td>
197	&lt;td>&lt;b>+7.07&lt;/b>&lt;/td>
198	&lt;td>&lt;b>+6.30&lt;/b>&lt;/td>
199	&lt;td>&lt;b>+9.37&lt;/b>&lt;/td>
200	&lt;/tr>
201	&lt;tr>
202	&lt;td>InternVL2.5-26B&lt;/td>
203	&lt;td>28.01&lt;/td>
204	&lt;td>14.46&lt;/td>
205	&lt;td>60.02&lt;/td>
206	&lt;td>37.83&lt;/td>
207	&lt;td>20.76&lt;/td>
208	&lt;/tr>
209	&lt;tr>
210	&lt;td>+MM-PRM&lt;/td>
211	&lt;td>38.00&lt;/td>
212	&lt;td>24.67&lt;/td>
213	&lt;td>64.50&lt;/td>
214	&lt;td>44.19&lt;/td>
215	&lt;td>25.63&lt;/td>
216	&lt;/tr>
217	&lt;tr>
218	&lt;td>&lt;/td>
219	&lt;td>&lt;b>+9.99&lt;/b>&lt;/td>
220	&lt;td>&lt;b>+10.21&lt;/b>&lt;/td>
221	&lt;td>&lt;b>+4.25&lt;/b>&lt;/td>
222	&lt;td>&lt;b>+6.36&lt;/b>&lt;/td>
223	&lt;td>&lt;b>+4.87&lt;/b>&lt;/td>
224	&lt;/tr>
225	&lt;tr>
226	&lt;td>InternVL2.5-38B&lt;/td>
227	&lt;td>40.34&lt;/td>
228	&lt;td>29.57&lt;/td>
229	&lt;td>68.32&lt;/td>
230	&lt;td>47.94&lt;/td>
231	&lt;td>29.70&lt;/td>
232	&lt;/tr>
233	&lt;tr>
234	&lt;td>+MM-PRM&lt;/td>
235	&lt;td>52.40&lt;/td>
236	&lt;td>32.67&lt;/td>
237	&lt;td>71.10&lt;/td>
238	&lt;td>52.61&lt;/td>
239	&lt;td>32.99&lt;/td>
240	&lt;/tr>
241	&lt;tr>
242	&lt;td>&lt;/td>
243	&lt;td>&lt;b>+12.06&lt;/b>&lt;/td>
244	&lt;td>&lt;b>+3.10&lt;/b>&lt;/td>
245	&lt;td>&lt;b>+2.78&lt;/b>&lt;/td>
246	&lt;td>&lt;b>+4.67&lt;/b>&lt;/td>
247	&lt;td>&lt;b>+3.29&lt;/b>&lt;/td>
248	&lt;/tr>
249	&lt;tr>
250	&lt;td>InternVL2.5-78B&lt;/td>
251	&lt;td>42.24&lt;/td>
252	&lt;td>30.98&lt;/td>
253	&lt;td>69.48&lt;/td>
254	&lt;td>50.18&lt;/td>
255	&lt;td>31.50&lt;/td>
256	&lt;/tr>
257	&lt;tr>
258	&lt;td>+MM-PRM&lt;/td>
259	&lt;td>48.80&lt;/td>
260	&lt;td>34.67&lt;/td>
261	&lt;td>73.20&lt;/td>
262	&lt;td>54.47&lt;/td>
263	&lt;td>33.26&lt;/td>
264	&lt;/tr>
265	&lt;tr>
266	&lt;td>&lt;/td>
267	&lt;td>&lt;b>+6.56&lt;/b>&lt;/td>
268	&lt;td>&lt;b>+3.69&lt;/b>&lt;/td>
269	&lt;td>&lt;b>+3.72&lt;/b>&lt;/td>
270	&lt;td>&lt;b>+4.29&lt;/b>&lt;/td>
271	&lt;td>&lt;b>+1.76&lt;/b>&lt;/td>
272	&lt;/tr>
273	&lt;/tbody>
274	&lt;/table>
275	
276	We evaluate the effectiveness of MM-PRM by applying it to a range of policy models and testing its impact across multiple multimodal math benchmarks.
277	
278	Across all models, MM-PRM yields substantial performance improvements. For example, when applied to MM-Policy on the MM-K12 test set, accuracy improves from 33.92% to 42.80%, and similar gains are observed with InternVL2.5-8B, where performance rises from 27.01% to 37.80%. These results confirm that MM-PRM is highly effective at identifying high-quality reasoning paths.
279	
280	Beyond in-domain settings, we observe that MM-PRM also generalizes well to larger models and more challenging datasets. As shown in Table 1, applying MM-PRM to InternVL2.5-78B improves accuracy on OlympiadBench from 30.98% to 34.67%, and on MathVerse from 50.18% to 54.47%. Despite being trained only on the small MM-K12 seed dataset and with a fixed policy model(i.e., MM-Policy), MM-PRM consistently enhances reasoning accuracy across diverse benchmarks and models. This demonstrates the potential of scalable step-level reward modeling to improve mathematical**Question**
281	
282	As shown in the figure, it is known that  $AB \parallel CD$ ,  $CE$  bisect  $\angle ACD$ , and intersects  $AB$  at  $E$ ,  $\angle A = 118^\circ$ . Then  $\angle AEC = ?$
283	
284	**Solution**
285	
286	( $\hat{A} = 0.83$ ) Identify the relationship between the angles formed by the parallel lines and the transversal. Since  $AB \parallel CD$  and  $\angle A = 118^\circ$ , We can use the property of parallel lines and transversals to determine the measure of  $\angle ACD$ . The angles on a straight line sum up to  $180^\circ$ . So:  $\angle ACD = 180^\circ - \angle A = 180^\circ - 118^\circ = 62^\circ$
287	
288	( $\hat{A} = 0.68$ ) Use the angle bisector property. Since  $CE$  bisect  $\angle ACD$ , it divides  $\angle ACD$  into two equal angles. Therefore:  $\angle ACE = \frac{\angle ACD}{2} = \frac{62^\circ}{2} = 31^\circ$
289	
290	( $\hat{A} = 0.02$ ) Determine  $\angle AEC$  using the exterior angle theorem. In  $\triangle AEC$ ,  $\angle AEC$  is an exterior angle and is equal to the sum of the two non-adjacent interior angles  $\angle A$  and  $\angle ACE$ . However, since  $\angle AEC$  is directly opposite  $\angle ACE$  and  $\angle A$  is the exterior angle, we can use the fact that the exterior angle is the sum of the two non-adjacent interior angles:  $\angle AEC = \angle A - \angle ACE = 118^\circ - 31^\circ = 87^\circ$
291	
292	( $\hat{A} = 0.01$ ) Answer: The Final Answer is 87
293	
294	Figure 2: Qualitative example of MM-PRM accurately identifying error steps in multimodal reasoning process.
295	
296	reasoning in a model-agnostic and data-efficient manner. Detailed evaluation results across all aggregation functions are provided in Appendix D.
297	
298	#### 4.4 Qualitative results
299	
300	To further illustrate the behavior of MM-PRM, we present a qualitative example involving a geometry problem with parallel lines and an angle bisector. As shown in Figure 2, the policy model generates a four-step reasoning path, which ultimately leads to an incorrect final answer.
301	
302	The PRM assigns high scores to the first two steps (0.83 and 0.68), indicating that they are logically sound. In contrast, Step-3 receives a very low score (0.02), signaling that the model has identified a significant reasoning error at this point. This flawed step leads directly to an incorrect conclusion in Step-4.
303	
304	This example demonstrates that MM-PRM is capable of detecting localized logical errors within a reasoning chain, such fine-grained judgment is crucial in selecting high-quality reasoning trajectories and filtering out those with subtle but critical flaws.
305	
306	## 5 Discussion
307	
308	Figure 3: (a) Effect of the number of candidate reasoning paths on answer accuracy under Best-of-N inference. Increasing the number of candidates allows the PRM to select higher-quality reasoning trajectories. (b) Effect of learning rate on PRM performance. Small learning rates yield better accuracy, with performance peaking at  $4 \times 10^{-6}$## 5.1 Candidate path’s impact on PRM performance
309	
310	Since the PRM operates purely as a selector in the BoN framework, its performance is inherently bounded by the diversity and quality of candidate reasoning paths produced by the policy model. In other words, PRM cannot improve a flawed generation in BoN—it can only choose among the available options. Therefore, the number of reasoning paths generated per problem directly affects its potential to identify a correct and coherent solution.
311	
312	To study this effect, we vary the number of generated reasoning paths  $N \in \{2, 2^2, 2^3, 2^4\}$  and measure the corresponding answer accuracy under the aggregation strategy MeanOdds. As shown in Figure 3(a), increasing  $N$  consistently improves MM-PRM’s performance across both test sets. On the MM-K12 test set, accuracy improves from 38.6% at  $N = 2$  to 42.8% at  $N = 16$ , with gains tapering off beyond  $N = 8$ . In contrast, on OlympiadBench, accuracy increases more steadily—from 18.4% to 24.0%—as  $N$  grows. This suggests that for harder, more diverse tasks, having a larger pool of reasoning paths is critical for PRM to identify valid solutions.
313	
314	## 5.2 Learning rate
315	
316	As noted in [39], finetuning a PRM shifts the language models’ objective from generation to discrimination, making learning rate a critical factor. Smaller learning rates are often preferred to maintain stability and preserve pretrained knowledge.
317	
318	We evaluate MM-PRM trained under different learning rates on the MM-K12 test set using MeanOdds aggregator. As shown in Figure 3(b), performance peaks at  $4e-6$ —about one-tenth the learning rate typically used in supervised fine-tuning—then drops sharply at higher values. This confirms that a moderate, conservative learning rate leads to better training, while overly large values degrade accuracy.
319	
320	## 5.3 Soft label vs. Hard label
321	
322	Table 2: The performance comparisons of soft label vs. hard label.
323	
324	&lt;table border="1">&lt;thead>&lt;tr>&lt;th>Labeling Strategy&lt;/th>&lt;th>Min&lt;/th>&lt;th>Average&lt;/th>&lt;th>Max&lt;/th>&lt;th>SumLogPr&lt;/th>&lt;th>SumLogOdds&lt;/th>&lt;th>MeanOdds&lt;/th>&lt;/tr>&lt;/thead>&lt;tbody>&lt;tr>&lt;td>Soft Label&lt;/td>&lt;td>37.4&lt;/td>&lt;td>43.0&lt;/td>&lt;td>43.4&lt;/td>&lt;td>42.0&lt;/td>&lt;td>43.2&lt;/td>&lt;td>42.8&lt;/td>&lt;/tr>&lt;tr>&lt;td>Hard Label&lt;/td>&lt;td>36.8&lt;/td>&lt;td>34.4&lt;/td>&lt;td>35.6&lt;/td>&lt;td>36.0&lt;/td>&lt;td>33.8&lt;/td>&lt;td>37.0&lt;/td>&lt;/tr>&lt;/tbody>&lt;/table>
325	
326	As discussed in section 3.4.1, we adopt soft label—i.e., real-valued MC scores—as supervision for step-level reward modeling. Unlike hard label, soft label retain uncertainty and allow the model to learn more nuanced representations of reasoning quality.
327	
328	To assess this design choice, we compare soft label with hard label thresholding, where steps with  $MC > 0$  are treated as correct, and others as incorrect, following the protocol in [41, 56].
329	
330	As shown in Table 2, soft-label training consistently outperforms hard-label training across all aggregation strategies. For instance, under the Average aggregator, soft labels yield 43% accuracy on MM-K12 test set, compared to 34.4% with hard labels. Similar improvements are observed with SumLogOdds (43.2% vs. 33.8%) and MeanOdds (42.8% vs. 37.0%).
331	
332	## 6 Conclusion
333	
334	In this work, we introduce MM-PRM, a process reward model built upon a scalable framework for multimodal mathematical process reward modeling that enables step-level supervision without human annotation. By leveraging a multimodal policy model and an MCTS-based data generation pipeline, we construct over 700k process-level labels from only 10k K-12 math problems in our MM-K12 dataset. Our trained PRM significantly improves reasoning accuracy in BoN inference across both standard and challenging benchmarks, and demonstrates strong generalization to new datasets and models. Extensive analysis further confirms the importance of soft labeling, conservative learning rates, and sufficient path diversity. MM-PRM highlights the value of process supervision for enhancing multimodal mathematical problem-solving.## References
335	
336	- [1] Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. Gpt-4 technical report. *arXiv preprint arXiv:2303.08774*, 2023.
337	- [2] Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang, Xiaodong Deng, Yang Fan, Wenbin Ge, Yu Han, Fei Huang, et al. Qwen technical report. *arXiv preprint arXiv:2309.16609*, 2023.
338	- [3] Gemini Team, Rohan Anil, Sebastian Borgeaud, Jean-Baptiste Alayrac, Jiahui Yu, Radu Soricut, Johan Schalkwyk, Andrew M Dai, Anja Hauth, Katie Millican, et al. Gemini: a family of highly capable multimodal models. *arXiv preprint arXiv:2312.11805*, 2023.
339	- [4] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, et al. Llama: Open and efficient foundation language models. *arXiv preprint arXiv:2302.13971*, 2023.
340	- [5] Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al. Llama 2: Open foundation and fine-tuned chat models. *arXiv preprint arXiv:2307.09288*, 2023.
341	- [6] Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Alex Vaughan, et al. The llama 3 herd of models. *arXiv preprint arXiv:2407.21783*, 2024.
342	- [7] InternLM Team. Internlm: A multilingual language model with progressively enhanced capabilities. &lt;https://github.com/InternLM/InternLM-techreport>, 2023.
343	- [8] Zheng Cai, Maosong Cao, Haojiong Chen, Kai Chen, Keyu Chen, Xin Chen, Xun Chen, Zehui Chen, Zhi Chen, Pei Chu, et al. Internlm2 technical report. *arXiv preprint arXiv:2403.17297*, 2024.
344	- [9] Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. *arXiv preprint arXiv:2501.12948*, 2025.
345	- [10] Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. Visual instruction tuning. *Advances in neural information processing systems*, 36:34892–34916, 2023.
346	- [11] Yuan Yao, Tianyu Yu, Ao Zhang, Chongyi Wang, Junbo Cui, Hongji Zhu, Tianchi Cai, Haoyu Li, Weilin Zhao, Zhihui He, et al. Minicpm-v: A gpt-4v level mllm on your phone. *arXiv preprint arXiv:2408.01800*, 2024.
347	- [12] Zhe Chen, Weiyun Wang, Yue Cao, Yangzhou Liu, Zhangwei Gao, Erfei Cui, Jinguo Zhu, Shenglong Ye, Hao Tian, Zhaoyang Liu, et al. Expanding performance boundaries of open-source multimodal models with model, data, and test-time scaling. *arXiv preprint arXiv:2412.05271*, 2024.
348	- [13] Weiyun Wang, Zhe Chen, Wenhai Wang, Yue Cao, Yangzhou Liu, Zhangwei Gao, Jinguo Zhu, Xizhou Zhu, Lewei Lu, Yu Qiao, and Jifeng Dai. Enhancing the reasoning ability of multimodal large language models via mixed preference optimization. *arXiv preprint arXiv:2411.10442*, 2024.
349	- [14] Zhangwei Gao, Zhe Chen, Erfei Cui, Yiming Ren, Weiyun Wang, Jinguo Zhu, Hao Tian, Shenglong Ye, Junjun He, Xizhou Zhu, et al. Mini-internvl: a flexible-transfer pocket multi-modal model with 5% parameters and 90% performance. *Visual Intelligence*, 2(1):1–17, 2024.
350	- [15] Zhe Chen, Weiyun Wang, Hao Tian, Shenglong Ye, Zhangwei Gao, Erfei Cui, Wenwen Tong, Kongzhi Hu, Jiapeng Luo, Zheng Ma, et al. How far are we to gpt-4v? closing the gap to commercial multimodal models with open-source suites. *Science China Information Sciences*, 67(12):220101, 2024.
351	- [16] Zhe Chen, Jiannan Wu, Wenhai Wang, Weijie Su, Guo Chen, Sen Xing, Muyan Zhong, Qinglong Zhang, Xizhou Zhu, Lewei Lu, et al. Internvl: Scaling up vision foundation models and aligning for generic visual-linguistic tasks. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, pages 24185–24198, 2024.
352	- [17] Jinze Bai, Shuai Bai, Shusheng Yang, Shijie Wang, Sinan Tan, Peng Wang, Junyang Lin, Chang Zhou, and Jingren Zhou. Qwen-vl: A versatile vision-language model for understanding, localization, text reading, and beyond. *arXiv preprint arXiv:2308.12966*, 2023.
353	- [18] Kimi Team, Angang Du, Bofei Gao, Bowei Xing, Changjiu Jiang, Cheng Chen, Cheng Li, Chenjun Xiao, Chenzhuang Du, Chonghua Liao, et al. Kimi k1. 5: Scaling reinforcement learning with llms. *arXiv preprint arXiv:2501.12599*, 2025.
354	- [19] Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, et al. Training verifiers to solve math word problems. *arXiv preprint arXiv:2110.14168*, 2021.
355	- [20] Fei Yu, Anningzhe Gao, and Benyou Wang. Ovm, outcome-supervised value models for planning in mathematical reasoning. *arXiv preprint arXiv:2311.09724*, 2023.- [21] Jonathan Uesato, Nate Kushman, Ramana Kumar, Francis Song, Noah Siegel, Lisa Wang, Antonia Creswell, Geoffrey Irving, and Irina Higgins. Solving math word problems with process-and outcome-based feedback. *arXiv preprint arXiv:2211.14275*, 2022.
356	- [22] Yuhang Zang, Xiaoyi Dong, Pan Zhang, Yuhang Cao, Ziyu Liu, Shengyuan Ding, Shenxi Wu, Yubo Ma, Haodong Duan, Wenwei Zhang, et al. Internlm-xcomposer2. 5-reward: A simple yet effective multi-modal reward model. *arXiv preprint arXiv:2501.12368*, 2025.
357	- [23] Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training language models to follow instructions with human feedback. *Advances in neural information processing systems*, 35:27730–27744, 2022.
358	- [24] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. *arXiv preprint arXiv:1707.06347*, 2017.
359	- [25] Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li, Y Wu, et al. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. *arXiv preprint arXiv:2402.03300*, 2024.
360	- [26] Xin Lai, Zhuotao Tian, Yukang Chen, Senqiao Yang, Xiangru Peng, and Jiaya Jia. Step-dpo: Step-wise preference optimization for long-chain reasoning of llms. *arXiv preprint arXiv:2406.18629*, 2024.
361	- [27] Weiyun Wang, Zhe Chen, Wenhai Wang, Yue Cao, Yangzhou Liu, Zhangwei Gao, Jinguo Zhu, Xizhou Zhu, Lewei Lu, Yu Qiao, et al. Enhancing the reasoning ability of multimodal large language models via mixed preference optimization. *arXiv preprint arXiv:2411.10442*, 2024.
362	- [28] Richard Yuanzhe Pang, Weizhe Yuan, He He, Kyunghyun Cho, Sainbayar Sukhbaatar, and Jason Weston. Iterative reasoning preference optimization. *Advances in Neural Information Processing Systems*, 37:116617–116637, 2024.
363	- [29] Hanze Dong, Wei Xiong, Bo Pang, Haoxiang Wang, Han Zhao, Yingbo Zhou, Nan Jiang, Doyen Sahoo, Caiming Xiong, and Tong Zhang. Rlhf workflow: From reward modeling to online rlhf. *arXiv preprint arXiv:2405.07863*, 2024.
364	- [30] Charlie Snell, Jaehoon Lee, Kelvin Xu, and Aviral Kumar. Scaling llm test-time compute optimally can be more effective than scaling model parameters. *arXiv preprint arXiv:2408.03314*, 2024.
365	- [31] Peiyi Wang, Lei Li, Zhihong Shao, RX Xu, Damai Dai, Yifei Li, Deli Chen, Yu Wu, and Zhifang Sui. Math-shepherd: Verify and reinforce llms step-by-step without human annotations. *arXiv preprint arXiv:2312.08935*, 2023.
366	- [32] Zhenru Zhang, Chujie Zheng, Yangzhen Wu, Beichen Zhang, Runji Lin, Bowen Yu, Dayiheng Liu, Jingren Zhou, and Junyang Lin. The lessons of developing process reward models in mathematical reasoning. *arXiv preprint arXiv:2501.07301*, 2025.
367	- [33] Xidong Feng, Ziyu Wan, Muning Wen, Stephen Marcus McAleer, Ying Wen, Weinan Zhang, and Jun Wang. Alphazero-like tree-search can guide large language model decoding and training. *arXiv preprint arXiv:2309.17179*, 2023.
368	- [34] Jikun Kang, Xin Zhe Li, Xi Chen, Amirreza Kazemi, Qianyi Sun, Boxing Chen, Dong Li, Xu He, Quan He, Feng Wen, et al. Mindstar: Enhancing math reasoning in pre-trained llms at inference time. *arXiv preprint arXiv:2405.16265*, 2024.
369	- [35] Qianli Ma, Haotian Zhou, Tingkai Liu, Jianbo Yuan, Pengfei Liu, Yang You, and Hongxia Yang. Let’s reward step by step: Step-level reward model as the navigators for reasoning. *arXiv preprint arXiv:2310.10080*, 2023.
370	- [36] Ye Tian, Baolin Peng, Linfeng Song, Lifeng Jin, Dian Yu, Lei Han, Haitao Mi, and Dong Yu. Toward self-improvement of llms via imagination, searching, and criticizing. *Advances in Neural Information Processing Systems*, 37:52723–52748, 2024.
371	- [37] Dan Zhang, Sining Zhoubian, Ziniu Hu, Yisong Yue, Yuxiao Dong, and Jie Tang. Rest-mcts\*: Llm self-training via process reward guided tree search. *Advances in Neural Information Processing Systems*, 37:64735–64772, 2024.
372	- [38] Yifei Li, Zeqi Lin, Shizhuo Zhang, Qiang Fu, Bei Chen, Jian-Guang Lou, and Weizhu Chen. Making large language models better reasoners with step-aware verifier. *arXiv preprint arXiv:2206.02336*, 2022.
373	- [39] Hunter Lightman, Vineet Kosaraju, Yuri Burda, Harrison Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. Let’s verify step by step. In *The Twelfth International Conference on Learning Representations*, 2023.
374	- [40] Zihan Wang, Yunxuan Li, Yuexin Wu, Liangchen Luo, Le Hou, Hongkun Yu, and Jingbo Shang. Multi-step problem solving through a verifier: An empirical analysis on model-induced process supervision. *arXiv preprint arXiv:2402.02658*, 2024.- [41] Liangchen Luo, Yinxiao Liu, Rosanne Liu, Samrat Phatale, Meiqi Guo, Harsh Lara, Yunxuan Li, Lei Shu, Yun Zhu, Lei Meng, et al. Improve mathematical reasoning in language models by automated process supervision. *arXiv preprint arXiv:2406.06592*, 2024.
375	- [42] Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. Measuring mathematical problem solving with the math dataset. *arXiv preprint arXiv:2103.03874*, 2021.
376	- [43] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models. *Advances in neural information processing systems*, 35:24824–24837, 2022.
377	- [44] Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. Self-consistency improves chain of thought reasoning in language models. *arXiv preprint arXiv:2203.11171*, 2022.
378	- [45] Aaron Jaech, Adam Kalai, Adam Lerer, Adam Richardson, Ahmed El-Kishky, Aiden Low, Alec Hel-yar, Aleksander Madry, Alex Beutel, Alex Carney, et al. Openai o1 system card. *arXiv preprint arXiv:2412.16720*, 2024.
379	- [46] Ruilin Luo, Zhuofan Zheng, Yifan Wang, Yiyao Yu, Xinzhe Ni, Zicheng Lin, Jin Zeng, and Yujiu Yang. Ursa: Understanding and verifying chain-of-thought reasoning in multimodal mathematics. *arXiv preprint arXiv:2501.04686*, 2025.
380	- [47] Linger Deng, Yuliang Liu, Bohan Li, Dongliang Luo, Liang Wu, Chengquan Zhang, Pengyuan Lyu, Ziyang Zhang, Gang Zhang, Errui Ding, et al. R-cot: Reverse chain-of-thought problem generation for geometric reasoning in large multimodal models. *arXiv preprint arXiv:2410.17885*, 2024.
381	- [48] Renrui Zhang, Xinyu Wei, Dongzhi Jiang, Ziyu Guo, Shicheng Li, Yichi Zhang, Chengzhuo Tong, Jiaming Liu, Aojun Zhou, Bin Wei, et al. Mavis: Mathematical visual instruction tuning with an automatic data engine. *arXiv preprint arXiv:2407.08739*, 2024.
382	- [49] Wenhao Shi, Zhiqiang Hu, Yi Bin, Junhua Liu, Yang Yang, See-Kiong Ng, Lidong Bing, and Roy Ka-Wei Lee. Math-llava: Bootstrapping mathematical reasoning for multimodal large language models. *arXiv preprint arXiv:2406.17294*, 2024.
383	- [50] Jia Li, Edward Beeching, Lewis Tunstall, Ben Lipkin, Roman Soletskyi, Shengyi Huang, Kashif Rasul, Longhui Yu, Albert Q Jiang, Ziju Shen, et al. Numinamath: The largest public dataset in ai4maths with 860k pairs of competition math problems and solutions. *Hugging Face repository*, 13:9, 2024.
384	- [51] Yuxuan Tong, Xiwen Zhang, Rui Wang, Ruidong Wu, and Junxian He. Dart-math: Difficulty-aware rejection tuning for mathematical problem-solving. *Advances in Neural Information Processing Systems*, 37:7821–7846, 2024.
385	- [52] Chaoqun He, Renjie Luo, Yuzhuo Bai, Shengding Hu, Zhen Leng Thai, Junhao Shen, Jinyi Hu, Xu Han, Yujie Huang, Yuxiang Zhang, et al. Olympiadbench: A challenging benchmark for promoting agi with olympiad-level bilingual multimodal scientific problems. *arXiv preprint arXiv:2402.14008*, 2024.
386	- [53] Pan Lu, Hritik Bansal, Tony Xia, Jiacheng Liu, Chunyuan Li, Hannaneh Hajishirzi, Hao Cheng, Kai-Wei Chang, Michel Galley, and Jianfeng Gao. Mathvista: Evaluating mathematical reasoning of foundation models in visual contexts. *arXiv preprint arXiv:2310.02255*, 2023.
387	- [54] Renrui Zhang, Dongzhi Jiang, Yichi Zhang, Haokun Lin, Ziyu Guo, Pengshuo Qiu, Aojun Zhou, Pan Lu, Kai-Wei Chang, Yu Qiao, et al. Mathverse: Does your multi-modal llm truly see the diagrams in visual math problems? In *European Conference on Computer Vision*, pages 169–186. Springer, 2024.
388	- [55] Ke Wang, Junting Pan, Weikang Shi, Zimu Lu, Houxing Ren, Aojun Zhou, Mingjie Zhan, and Hong-sheng Li. Measuring multimodal mathematical reasoning with math-vision dataset. *Advances in Neural Information Processing Systems*, 37:95095–95169, 2024.
389	- [56] Jun Wang, Meng Fang, Ziyu Wan, Muning Wen, Jiachen Zhu, Anjie Liu, Ziqin Gong, Yan Song, Lei Chen, Lionel M Ni, et al. Openr: An open source framework for advanced reasoning with large language models. *arXiv preprint arXiv:2410.09671*, 2024.
390	- [57] Shuai Peng, Di Fu, Liangcai Gao, Xiuqin Zhong, Hongguang Fu, and Zhi Tang. Multimath: Bridging visual and mathematical reasoning for large language models. *arXiv preprint arXiv:2409.00147*, 2024.
391	- [58] Lei Li, Yuqi Wang, Runxin Xu, Peiyi Wang, Xiachong Feng, Lingpeng Kong, and Qi Liu. Multimodal arxiv: A dataset for improving scientific comprehension of large vision-language models. *arXiv preprint arXiv:2403.00231*, 2024.
392	- [59] Wenwen Zhuang, Xin Huang, Xiantao Zhang, and Jin Zeng. Math-puma: Progressive upward multimodal alignment to enhance mathematical reasoning. In *Proceedings of the AAAI Conference on Artificial Intelligence*, volume 39, pages 26183–26191, 2025.- [60] Wenqi Zhang, Zhenglin Cheng, Yuanyu He, Mengna Wang, Yongliang Shen, Zeqi Tan, Guiyang Hou, Mingqian He, Yanna Ma, Weiming Lu, et al. Multimodal self-instruct: Synthetic abstract image and visual reasoning instruction using language model. *arXiv preprint arXiv:2407.07053*, 2024.
393	- [61] Erfei Cui, Yinan He, Zheng Ma, Zhe Chen, Hao Tian, Weiyun Wang, Kunchang Li, Yi Wang, Wenhai Wang, Xizhou Zhu, Lewei Lu, Tong Lu, Yali Wang, Limin Wang, Yu Qiao, and Jifeng Dai. Sharegpt-4o: Comprehensive multimodal annotations with gpt-4o, 2024.
394	- [62] Cyrile Delestre Tom Agonnoude, 2024.
395	- [63] Aida Amini, Saadia Gabriel, Peter Lin, Rik Koncel-Kedziorski, Yejin Choi, and Hannaneh Hajishirzi. Mathqa: Towards interpretable math word problem solving with operation-based formalisms. *arXiv preprint arXiv:1905.13319*, 2019.
396	- [64] PawanKrd. math-gpt-4o-200k. *Hugging Face repository*, 2024.
397	- [65] Xiang Yue, Xingwei Qu, Ge Zhang, Yao Fu, Wenhao Huang, Huan Sun, Yu Su, and Wenhui Chen. Mammoth: Building math generalist models through hybrid instruction tuning. *arXiv preprint arXiv:2309.05653*, 2023.## Appendix
398	
399	### A Policy Model training data
400	
401	Table 3 summarizes the datasets and sample counts used to train the policy model.
402	
403	Table 3: Data sources and sample counts used for policy model training.
404	
405	&lt;table border="1">&lt;thead>&lt;tr>&lt;th>Dataset&lt;/th>&lt;th>Sample Count&lt;/th>&lt;/tr>&lt;/thead>&lt;tbody>&lt;tr>&lt;td>R-CoT [47]&lt;/td>&lt;td>201,781&lt;/td>&lt;/tr>&lt;tr>&lt;td>MAVIS [48]&lt;/td>&lt;td>29,551&lt;/td>&lt;/tr>&lt;tr>&lt;td>multimath-300k [57]&lt;/td>&lt;td>224,747&lt;/td>&lt;/tr>&lt;tr>&lt;td>Multimodal ArXiv [58]&lt;/td>&lt;td>99,772&lt;/td>&lt;/tr>&lt;tr>&lt;td>MathV360K [49]&lt;/td>&lt;td>338,721&lt;/td>&lt;/tr>&lt;tr>&lt;td>Math-PUMA [59]&lt;/td>&lt;td>1,111,939&lt;/td>&lt;/tr>&lt;tr>&lt;td>Multi-modal-Self-instruct [60]&lt;/td>&lt;td>64,807&lt;/td>&lt;/tr>&lt;tr>&lt;td>MMPR [13]&lt;/td>&lt;td>1,055,796&lt;/td>&lt;/tr>&lt;tr>&lt;td>ShareGPT-4o [61]&lt;/td>&lt;td>57,289&lt;/td>&lt;/tr>&lt;tr>&lt;td>table-vqa [62]&lt;/td>&lt;td>80,054&lt;/td>&lt;/tr>&lt;tr>&lt;td>MathQA [63]&lt;/td>&lt;td>27,923&lt;/td>&lt;/tr>&lt;tr>&lt;td>GSM8K [19]&lt;/td>&lt;td>7,413&lt;/td>&lt;/tr>&lt;tr>&lt;td>DART-Math [51]&lt;/td>&lt;td>574,305&lt;/td>&lt;/tr>&lt;tr>&lt;td>math-gpt-4o-200k [64]&lt;/td>&lt;td>196,032&lt;/td>&lt;/tr>&lt;tr>&lt;td>NuminaMath-CoT [50]&lt;/td>&lt;td>807,883&lt;/td>&lt;/tr>&lt;tr>&lt;td>MathInstruct [65]&lt;/td>&lt;td>257,755&lt;/td>&lt;/tr>&lt;tr>&lt;td>&lt;b>Total&lt;/b>&lt;/td>&lt;td>&lt;b>5,135,768&lt;/b>&lt;/td>&lt;/tr>&lt;/tbody>&lt;/table>
406	
407	### B Prompt template for data cleaning
408	
409	The prompt template used for data cleaning is shown below. Before generating logical steps and the final answer, the language model is first instructed to explicitly identify the key knowledge points involved in the problem, along with brief explanations. This two-stage prompting strategy enhances the model’s understanding of the question prior to solution restructuring.
410	
411	Using the information provided, identify and summarize the key knowledge points required to solve the problem and rewrite the original answer with a detailed reasoning process based on the input answer.
412	
413	Provide a clear explanation of each knowledge point by stating its name followed by a colon (:), and then presenting the detailed Explanation on the same line.
414	
415	When explaining the knowledge point, DO NOT reference or describe the original question, answer, or answer details. Focus solely on explaining the knowledge points.
416	
417	Besides, rewrite the original answer to include detailed reasoning and answer. Do not change the final answer and always refer to the input answer.
418	
419	Output Format:
420	
421	In order to answer this question, we first need to have the following prior knowledge:
422	
423	{{Substitute with name of knowledge point 1}}: {{Substitute with Explanation of knowledge point 1}},  
424	{{Substitute with name of knowledge point 2}}: {{Substitute with Explanation of knowledge point 2}},...
425	
426	We answer this based on prior knowledge as follows:
427	
428	Solution: Refined answer with detailed reasoning. Use Step 1, Step 2 to divide the steps. Remember do not change the final answer and always refer to the input answer.
429	
430	Answer: The Final Answer is {{Substitute with final answer}}.
431	
432	Input Information:
433	
434	Question: {question}
435	
436	Answer: {answer}
437	
438	## C Aggregation function definitions
439	
440	In the BoN inference setup, each reasoning path is assigned a vector of step-level scores predicted by the PRM. To compare and rank these paths, we apply an aggregation function to compress each score vector into a single scalar value, following the design considerations discussed in [40]. The following aggregation strategies are used in our experiments:
441	
442	- • Min: Computes the minimum of all step scores:
443	
444	$$\text{score}(r_j) = \min\{p_1^{(j)}, p_2^{(j)}, \dots, p_{T_j}^{(j)}\}$$
445	
446	- • Max: Computes the maximum of all step scores:
447	
448	$$\text{score}(r_j) = \max\{p_1^{(j)}, p_2^{(j)}, \dots, p_{T_j}^{(j)}\}$$
449	
450	- • Average: Computes the arithmetic mean of all step scores:
451	
452	$$\text{score}(r_j) = \frac{1}{T_j} \sum_{i=1}^{T_j} p_i^{(j)}$$
453	
454	- • SumLogPr: Computes the sum of log-probabilities of all step scores:
455	
456	$$\text{score}(r_j) = \sum_{i=1}^{T_j} \log p_i^{(j)} = \log \prod_{i=1}^{T_j} p_i^{(j)}$$
457	
458	- • SumLogOdds: Computes the sum of log-odds of all step scores:
459	
460	$$\text{score}(r_j) = \sum_{i=1}^{T_j} \log \frac{p_i^{(j)}}{1 - p_i^{(j)}}$$
461	
462	- • MeanOdds: Computes the mean of odds-transformed step scores:
463	
464	$$\text{score}(r_j) = \frac{1}{T_j} \sum_{i=1}^{T_j} \frac{p_i^{(j)}}{1 - p_i^{(j)}}$$
465	
466	Here,  $r_j$  denotes the  $j$ -th reasoning path consisting of  $T_j$  steps, and  $p_i^{(j)} \in (0, 1)$  is the predicted correctness probability of the  $i$ -th step in that path.## D Full evaluation results
467	
468	### D.1 MM-Policy
469	
470	Table 4: Performance comparison of various aggregators on various benchmarks for MM-Policy. Top performer is in **bold**.
471	
472	&lt;table border="1">
473	&lt;thead>
474	&lt;tr>
475	&lt;th>Benchmark&lt;/th>
476	&lt;th>Random&lt;/th>
477	&lt;th>Min&lt;/th>
478	&lt;th>Average&lt;/th>
479	&lt;th>Max&lt;/th>
480	&lt;th>SumLogPr&lt;/th>
481	&lt;th>SumLogOdds&lt;/th>
482	&lt;th>MeanOdds&lt;/th>
483	&lt;/tr>
484	&lt;/thead>
485	&lt;tbody>
486	&lt;tr>
487	&lt;td>MM-K12&lt;/td>
488	&lt;td>33.9&lt;/td>
489	&lt;td>37.4&lt;/td>
490	&lt;td>43.0&lt;/td>
491	&lt;td>&lt;b>43.4&lt;/b>&lt;/td>
492	&lt;td>42.0&lt;/td>
493	&lt;td>43.2&lt;/td>
494	&lt;td>42.8&lt;/td>
495	&lt;/tr>
496	&lt;tr>
497	&lt;td>OlympiadBench&lt;/td>
498	&lt;td>15.4&lt;/td>
499	&lt;td>23.3&lt;/td>
500	&lt;td>20.0&lt;/td>
501	&lt;td>&lt;b>24.7&lt;/b>&lt;/td>
502	&lt;td>22.7&lt;/td>
503	&lt;td>24.0&lt;/td>
504	&lt;td>24.0&lt;/td>
505	&lt;/tr>
506	&lt;tr>
507	&lt;td>MathVista&lt;/td>
508	&lt;td>62.9&lt;/td>
509	&lt;td>66.0&lt;/td>
510	&lt;td>67.2&lt;/td>
511	&lt;td>&lt;b>67.7&lt;/b>&lt;/td>
512	&lt;td>66.4&lt;/td>
513	&lt;td>&lt;b>67.7&lt;/b>&lt;/td>
514	&lt;td>67.6&lt;/td>
515	&lt;/tr>
516	&lt;tr>
517	&lt;td>MathVerse&lt;/td>
518	&lt;td>43.0&lt;/td>
519	&lt;td>46.0&lt;/td>
520	&lt;td>48.0&lt;/td>
521	&lt;td>46.1&lt;/td>
522	&lt;td>47.3&lt;/td>
523	&lt;td>&lt;b>48.0&lt;/b>&lt;/td>
524	&lt;td>46.3&lt;/td>
525	&lt;/tr>
526	&lt;tr>
527	&lt;td>MathVision&lt;/td>
528	&lt;td>21.7&lt;/td>
529	&lt;td>25.8&lt;/td>
530	&lt;td>26.7&lt;/td>
531	&lt;td>26.9&lt;/td>
532	&lt;td>25.4&lt;/td>
533	&lt;td>26.3&lt;/td>
534	&lt;td>&lt;b>27.1&lt;/b>&lt;/td>
535	&lt;/tr>
536	&lt;/tbody>
537	&lt;/table>
538	
539	### D.2 InternVL-8B
540	
541	Table 5: Performance comparison of various aggregators on various benchmarks for InternVL-8B. Top performer is in **bold**.
542	
543	&lt;table border="1">
544	&lt;thead>
545	&lt;tr>
546	&lt;th>Benchmark&lt;/th>
547	&lt;th>Random&lt;/th>
548	&lt;th>Min&lt;/th>
549	&lt;th>Average&lt;/th>
550	&lt;th>Max&lt;/th>
551	&lt;th>SumLogPr&lt;/th>
552	&lt;th>SumLogOdds&lt;/th>
553	&lt;th>MeanOdds&lt;/th>
554	&lt;/tr>
555	&lt;/thead>
556	&lt;tbody>
557	&lt;tr>
558	&lt;td>MM-K12&lt;/td>
559	&lt;td>27.0&lt;/td>
560	&lt;td>34.8&lt;/td>
561	&lt;td>36.0&lt;/td>
562	&lt;td>35.8&lt;/td>
563	&lt;td>31.2&lt;/td>
564	&lt;td>34.2&lt;/td>
565	&lt;td>&lt;b>37.8&lt;/b>&lt;/td>
566	&lt;/tr>
567	&lt;tr>
568	&lt;td>OlympiadBench&lt;/td>
569	&lt;td>5.2&lt;/td>
570	&lt;td>2.7&lt;/td>
571	&lt;td>15.3&lt;/td>
572	&lt;td>&lt;b>16.7&lt;/b>&lt;/td>
573	&lt;td>2.0&lt;/td>
574	&lt;td>1.3&lt;/td>
575	&lt;td>15.3&lt;/td>
576	&lt;/tr>
577	&lt;tr>
578	&lt;td>MathVista&lt;/td>
579	&lt;td>56.4&lt;/td>
580	&lt;td>63.4&lt;/td>
581	&lt;td>62.8&lt;/td>
582	&lt;td>62.6&lt;/td>
583	&lt;td>61.0&lt;/td>
584	&lt;td>62.0&lt;/td>
585	&lt;td>&lt;b>63.5&lt;/b>&lt;/td>
586	&lt;/tr>
587	&lt;tr>
588	&lt;td>MathVerse&lt;/td>
589	&lt;td>36.3&lt;/td>
590	&lt;td>41.8&lt;/td>
591	&lt;td>&lt;b>42.8&lt;/b>&lt;/td>
592	&lt;td>41.1&lt;/td>
593	&lt;td>42.0&lt;/td>
594	&lt;td>42.8&lt;/td>
595	&lt;td>42.6&lt;/td>
596	&lt;/tr>
597	&lt;tr>
598	&lt;td>MathVision&lt;/td>
599	&lt;td>10.0&lt;/td>
600	&lt;td>6.1&lt;/td>
601	&lt;td>18.4&lt;/td>
602	&lt;td>&lt;b>20.6&lt;/b>&lt;/td>
603	&lt;td>3.8&lt;/td>
604	&lt;td>4.8&lt;/td>
605	&lt;td>19.4&lt;/td>
606	&lt;/tr>
607	&lt;/tbody>
608	&lt;/table>
609	
610	### D.3 InternVL-26B
611	
612	Table 6: Performance comparison of various aggregators on various benchmarks for InternVL-26B. Top performer is in **bold**.
613	
614	&lt;table border="1">
615	&lt;thead>
616	&lt;tr>
617	&lt;th>Benchmark&lt;/th>
618	&lt;th>Random&lt;/th>
619	&lt;th>Min&lt;/th>
620	&lt;th>Average&lt;/th>
621	&lt;th>Max&lt;/th>
622	&lt;th>SumLogPr&lt;/th>
623	&lt;th>SumLogOdds&lt;/th>
624	&lt;th>MeanOdds&lt;/th>
625	&lt;/tr>
626	&lt;/thead>
627	&lt;tbody>
628	&lt;tr>
629	&lt;td>MM-K12&lt;/td>
630	&lt;td>28.0&lt;/td>
631	&lt;td>&lt;b>38.0&lt;/b>&lt;/td>
632	&lt;td>37.2&lt;/td>
633	&lt;td>35.4&lt;/td>
634	&lt;td>32.0&lt;/td>
635	&lt;td>33.0&lt;/td>
636	&lt;td>&lt;b>38.0&lt;/b>&lt;/td>
637	&lt;/tr>
638	&lt;tr>
639	&lt;td>OlympiadBench&lt;/td>
640	&lt;td>14.5&lt;/td>
641	&lt;td>16.0&lt;/td>
642	&lt;td>23.3&lt;/td>
643	&lt;td>22.0&lt;/td>
644	&lt;td>16.7&lt;/td>
645	&lt;td>16.7&lt;/td>
646	&lt;td>24.7&lt;/td>
647	&lt;/tr>
648	&lt;tr>
649	&lt;td>MathVista&lt;/td>
650	&lt;td>60.0&lt;/td>
651	&lt;td>63.9&lt;/td>
652	&lt;td>&lt;b>64.6&lt;/b>&lt;/td>
653	&lt;td>64.4&lt;/td>
654	&lt;td>62.8&lt;/td>
655	&lt;td>64.2&lt;/td>
656	&lt;td>64.5&lt;/td>
657	&lt;/tr>
658	&lt;tr>
659	&lt;td>MathVerse&lt;/td>
660	&lt;td>37.8&lt;/td>
661	&lt;td>42.0&lt;/td>
662	&lt;td>44.2&lt;/td>
663	&lt;td>&lt;b>44.3&lt;/b>&lt;/td>
664	&lt;td>40.1&lt;/td>
665	&lt;td>41.5&lt;/td>
666	&lt;td>44.2&lt;/td>
667	&lt;/tr>
668	&lt;tr>
669	&lt;td>MathVision&lt;/td>
670	&lt;td>20.8&lt;/td>
671	&lt;td>23.3&lt;/td>
672	&lt;td>24.1&lt;/td>
673	&lt;td>24.9&lt;/td>
674	&lt;td>20.6&lt;/td>
675	&lt;td>22.0&lt;/td>
676	&lt;td>&lt;b>25.6&lt;/b>&lt;/td>
677	&lt;/tr>
678	&lt;/tbody>
679	&lt;/table>
680	
681	### D.4 InternVL-38B
682	
683	Table 7: Performance comparison of various aggregators on various benchmarks for InternVL-38B. Top performer is in **bold**.
684	
685	&lt;table border="1">
686	&lt;thead>
687	&lt;tr>
688	&lt;th>Benchmark&lt;/th>
689	&lt;th>Random&lt;/th>
690	&lt;th>Min&lt;/th>
691	&lt;th>Average&lt;/th>
692	&lt;th>Max&lt;/th>
693	&lt;th>SumLogPr&lt;/th>
694	&lt;th>SumLogOdds&lt;/th>
695	&lt;th>MeanOdds&lt;/th>
696	&lt;/tr>
697	&lt;/thead>
698	&lt;tbody>
699	&lt;tr>
700	&lt;td>MM-K12&lt;/td>
701	&lt;td>40.3&lt;/td>
702	&lt;td>46.8&lt;/td>
703	&lt;td>51.0&lt;/td>
704	&lt;td>49.8&lt;/td>
705	&lt;td>42.8&lt;/td>
706	&lt;td>46.6&lt;/td>
707	&lt;td>&lt;b>52.4&lt;/b>&lt;/td>
708	&lt;/tr>
709	&lt;tr>
710	&lt;td>OlympiadBench&lt;/td>
711	&lt;td>29.6&lt;/td>
712	&lt;td>29.3&lt;/td>
713	&lt;td>34.0&lt;/td>
714	&lt;td>&lt;b>34.7&lt;/b>&lt;/td>
715	&lt;td>28.0&lt;/td>
716	&lt;td>30.0&lt;/td>
717	&lt;td>32.7&lt;/td>
718	&lt;/tr>
719	&lt;tr>
720	&lt;td>MathVista&lt;/td>
721	&lt;td>68.3&lt;/td>
722	&lt;td>70.5&lt;/td>
723	&lt;td>&lt;b>71.1&lt;/b>&lt;/td>
724	&lt;td>70.5&lt;/td>
725	&lt;td>69.2&lt;/td>
726	&lt;td>70.1&lt;/td>
727	&lt;td>&lt;b>71.1&lt;/b>&lt;/td>
728	&lt;/tr>
729	&lt;tr>
730	&lt;td>MathVerse&lt;/td>
731	&lt;td>47.9&lt;/td>
732	&lt;td>50.4&lt;/td>
733	&lt;td>51.9&lt;/td>
734	&lt;td>51.1&lt;/td>
735	&lt;td>51.1&lt;/td>
736	&lt;td>52.7&lt;/td>
737	&lt;td>&lt;b>52.6&lt;/b>&lt;/td>
738	&lt;/tr>
739	&lt;tr>
740	&lt;td>MathVision&lt;/td>
741	&lt;td>29.7&lt;/td>
742	&lt;td>29.1&lt;/td>
743	&lt;td>32.6&lt;/td>
744	&lt;td>&lt;b>33.6&lt;/b>&lt;/td>
745	&lt;td>30.6&lt;/td>
746	&lt;td>31.3&lt;/td>
747	&lt;td>33.0&lt;/td>
748	&lt;/tr>
749	&lt;/tbody>
750	&lt;/table>## D.5 InternVL-78B
751	
752	Table 8: Performance comparison of various aggregators on various benchmarks for InternVL-78B. Top performer is in **bold**.
753	
754	&lt;table border="1">&lt;thead>&lt;tr>&lt;th>Benchmark&lt;/th>&lt;th>Random&lt;/th>&lt;th>Min&lt;/th>&lt;th>Average&lt;/th>&lt;th>Max&lt;/th>&lt;th>SumLogPr&lt;/th>&lt;th>SumLogOdds&lt;/th>&lt;th>MeanOdds&lt;/th>&lt;/tr>&lt;/thead>&lt;tbody>&lt;tr>&lt;td>MM-K12&lt;/td>&lt;td>42.2&lt;/td>&lt;td>46.2&lt;/td>&lt;td>47.2&lt;/td>&lt;td>47.2&lt;/td>&lt;td>45.0&lt;/td>&lt;td>46.8&lt;/td>&lt;td>&lt;b>48.8&lt;/b>&lt;/td>&lt;/tr>&lt;tr>&lt;td>OlympiadBench&lt;/td>&lt;td>31.0&lt;/td>&lt;td>33.3&lt;/td>&lt;td>35.3&lt;/td>&lt;td>&lt;b>34.7&lt;/b>&lt;/td>&lt;td>33.3&lt;/td>&lt;td>&lt;b>34.7&lt;/b>&lt;/td>&lt;td>&lt;b>34.7&lt;/b>&lt;/td>&lt;/tr>&lt;tr>&lt;td>MathVista&lt;/td>&lt;td>69.5&lt;/td>&lt;td>71.7&lt;/td>&lt;td>73.4&lt;/td>&lt;td>72.4&lt;/td>&lt;td>&lt;b>73.9&lt;/b>&lt;/td>&lt;td>73.6&lt;/td>&lt;td>73.2&lt;/td>&lt;/tr>&lt;tr>&lt;td>MathVerse&lt;/td>&lt;td>50.2&lt;/td>&lt;td>53.4&lt;/td>&lt;td>55.0&lt;/td>&lt;td>54.2&lt;/td>&lt;td>54.3&lt;/td>&lt;td>&lt;b>55.1&lt;/b>&lt;/td>&lt;td>54.5&lt;/td>&lt;/tr>&lt;tr>&lt;td>MathVision&lt;/td>&lt;td>31.5&lt;/td>&lt;td>30.1&lt;/td>&lt;td>33.5&lt;/td>&lt;td>&lt;b>33.6&lt;/b>&lt;/td>&lt;td>31.8&lt;/td>&lt;td>32.4&lt;/td>&lt;td>33.3&lt;/td>&lt;/tr>&lt;/tbody>&lt;/table>
755	
756	## E Limitations
757	
758	While our proposed framework demonstrates strong performance and generalization across multiple benchmarks, it also has several limitations: (1) Due to computational constraints, we conduct training only on the InternVL series with 8B parameters, without exploring larger models or architectures from other model families. This restricts our ability to fully assess how PRM training behavior scales with model size or generalizes across different backbones. (2) The seed data used for process supervision generation is limited in diversity, as it consists solely of K-12 math problems. As a result, the PRM may be less exposed to advanced mathematical domains or visual formats beyond the scope of standard educational settings. We leave broader model coverage and more diverse seed data construction as promising directions for future work.
759	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19b5f523-a18f-4eaf-9ac2-0427b5461736",
  "isSidechain": false,
  "promptId": "de34c998-fd7f-4a40-bbbf-9dd4b01a6eef",
  "type": "user",
  "uuid": "9590c609-7744-4015-826d-3a92cbde2fca",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/0243be30-7aad-4e4c-9062-bffffcde4a0d/tool-results/toolu_01CJZk2jcExqUgc2uZJAKdou.txt",
      "content": "# MM-PRM: Enhancing Multimodal Mathematical Reasoning with Scalable Step-Level Supervision\n\nLingxiao Du&lt;sup>1,\\*&lt;/sup> Fanqing Meng&lt;sup>1,3,\\*&lt;/sup> Zongkai Liu&lt;sup>2,\\*&lt;/sup> Zhixiang Zhou&lt;sup>2,\\*&lt;/sup>  \nPing Luo&lt;sup>4&lt;/sup> Qiaosheng Zhang&lt;sup>1,2,†&lt;/sup> Wenqi Shao&lt;sup>1,2,†&lt;/sup>\n\n&lt;sup>1&lt;/sup>Shanghai AI Laboratory &lt;sup>2&lt;/sup>Shanghai Innovation Institute  \n&lt;sup>3&lt;/sup>Shanghai Jiao Tong University &lt;sup>4&lt;/sup>The University of Hong Kong\n\n## Abstract\n\nWhile Multimodal Large Language Models (MLLMs) have achieved impressive progress in vision-language understanding, they still struggle with complex multi-step reasoning, often producing logically inconsistent or partially correct solutions. A key limitation lies in the lack of fine-grained supervision over intermediate reasoning steps. To address this, we propose MM-PRM, a process reward model trained within a fully automated, scalable framework. We first build MM-Policy, a strong multimodal model trained on diverse mathematical reasoning data. Then, we construct MM-K12, a curated dataset of 10,000 multimodal math problems with verifiable answers, which serves as seed data. Leveraging a Monte Carlo Tree Search (MCTS)-based pipeline, we generate over 700k step-level annotations without human labeling. The resulting PRM is used to score candidate reasoning paths in the Best-of-N inference setup and achieves significant improvements across both in-domain (MM-K12 test set) and out-of-domain (OlympiadBench, MathVista, etc.) benchmarks. Further analysis confirms the effectiveness of soft labels, smaller learning rates, and path diversity in optimizing PRM performance. MM-PRM demonstrates that process supervision is a powerful tool for enhancing the logical robustness of multimodal reasoning systems. We release all our codes and data at &lt;https://github.com/ModalMinds/MM-PRM>.\n\n## 1 Introduction\n\nThe rapid advancement of Large Language Models (LLMs) [1, 2, 3, 4, 5, 6, 7, 8, 9] has significantly improved performance on a wide range of natural language processing tasks, including general reasoning and mathematical problem-solving. In parallel, the development of Multimodal Large Language Models (MLLMs) [10, 11, 12, 13, 14, 15, 16, 17, 18] has unlocked new capabilities in vision-language understanding, showing promising results in areas such as image captioning and visual question answering (VQA). However, despite their impressive capabilities in perception and basic reasoning, MLLMs still struggle with complex multi-step reasoning tasks, particularly in mathematics. These shortcomings often manifest as broken logical chains, inaccurate intermediate steps, or cases that produce incorrect intermediate steps while still occasionally arriving at the correct final answer—a phenomenon that introduces high false-positive rates and undermines interpretability.\n\nTo address this issue, reward modeling [19, 20, 21, 22] has emerged as a promising paradigm. Reward models (RMs) play a central role in reinforcement learning from human feedback (RLHF) [23, 24, 25, 26, 27, 28], and can also be used at inference time to select among multiple candidate responses using Test-Time Scaling (TTS) [29, 30, 31, 32, 33, 34, 35, 36, 37] strategies such as Best-of-N (BoN). In general, reward models for reasoning tasks can be broadly categorized into two types: Outcome Reward Models (ORMs) and Process Reward Models (PRMs). ORMs [19, 20] provide\n\n\\*Equal contribution\n\n†Corresponding Authors: shaowenqi@pjlab.org.cn; zhangqiaosheng@pjlab.org.cnscalar feedback only on the final answer, overlooking the quality of the intermediate reasoning steps. This limits their ability to guide the model toward robust reasoning paths. In contrast, PRMs [38, 39, 21, 31, 40, 41] offer a more fine-grained approach by evaluating each reasoning step, enabling more accurate and interpretable feedback.\n\nSome recent works have explored process reward models for mathematical reasoning in pure text. PRM800k [39] manually constructs a large-scale dataset with step-level correctness labels, which is hard to scale. MathShepherd [31] adopts Monte Carlo estimation to label reasoning steps by evaluating whether continuations from a given step lead to the correct answer, but its efficiency is relatively low. OmegaPRM [41] introduces a Monte Carlo Tree Search (MCTS)-based framework that enables efficient automated generation of process supervision data. However, all these works focus on mathematical reasoning in pure text. In the field of multimodal mathematical reasoning, how to design an efficient framework for process supervision data generation and stably train process reward models remains a challenging problem.\n\nTo address these challenges, we propose **MM-PRM**, a powerful process reward model that effectively handles both in-domain and out-of-domain problems. Specifically, we first collect a large-scale, high-quality reasoning dataset and refine its format to train a policy model called **MM-Policy** with strong reasoning abilities and well-structured output. Inspired by OmegaPRM, we then establish an efficient multimodal process annotation framework. We first collect 10k high-quality K-12-level multimodal mathematical reasoning samples, named **MM-K12**. Starting with only 10k math problems as seed data, our framework automatically generates over 700k step-level annotations without any human supervision. Finally, we train MM-PRM with these data and evaluate its performance on multiple benchmarks using the BoN approach.\n\nMM-PRM demonstrates strong performance and generalization across multiple benchmarks. Although we only use process data generated from K-12-level math problems for training, MM-PRM achieves remarkable results with MM-Policy on benchmarks such as MathVista that improves from 62.93% to 67.60%. In addition, even though MM-PRM is trained on data produced by MM-Policy, it still delivers competitive results on other models like InternVL2.5-8B and InternVL2.5-78B. For instance, on the self-collected MM-K12 test set, InternVL2.5-8B improves from 27.01% to 37.80%, and on MathVerse, InternVL2.5-78B improves from 50.18% to 54.47%. These results highlight MM-PRM’s ability to generalize both across datasets and across model size, despite being trained on limited and fixed data sources.\n\nFinally, we provide a detailed discussion on key factors in PRM training, including learning rate and the choice between soft labels and hard labels. We find that the following factors are essential for stable PRM training: (1) using a small learning rate to ensure stable optimization; (2) adopting soft labels instead of hard thresholding to reduce noise and preserve step-wise uncertainty.\n\nIn summary, our contributions are as follows:\n\n- • We collect and release **MM-K12**, a curated multimodal math dataset containing 10,000 seed problems and 500 test problems, all verified to contain unique, checkable answers.\n- • We build a policy model named **MM-Policy** using a large corpus of mathematical reasoning data, and develop a fully automated, MCTS-based pipeline for scalable process supervision generation. Leveraging MM-Policy and only 10k seed problems from MM-K12, our framework produces over 700k step-level annotations without human supervision. Based on this, we train **MM-PRM**, which demonstrates strong performance across multiple benchmarks—for example, boosting accuracy on the MM-K12 test set from 33.92% to 42.80%, on MathVista from 62.93% to 67.60%, and on OlympiadBench from 15.41% to 24.00%.\n- • We provide a detailed discussion on the settings of key parameters such as the type of process labels and the learning rate. We summarize the key factors for stable PRM training, which can help the community train PRM models more effectively.\n\n## 2 Related work\n\n### 2.1 Mathematical reasoning and reward modeling in LLMs\n\nMathematical reasoning has become a focal point in evaluating the deep logical abilities of LLMs. [19, 42]. Unlike general language tasks, mathematical problems demand precise multi-step reasoningand logical coherence, motivating approaches like Chain-of-Thought (CoT) prompting[43] and Self-Consistency sampling [44]. Supervised fine-tuning (SFT) with structured solution datasets further reinforces reasoning performance, as demonstrated by models like Qwen [2], InternLM [7], and Gemini [3]. More recently, reinforcement learning (RL)-based optimization, exemplified by OpenAI’s o1 [45] and DeepSeek R1 [9], has emerged as a powerful strategy that surpassing SFT-only baselines.\n\nHowever, despite these advances, current LLMs still frequently produce logically inconsistent reasoning steps or false-positive solutions. To address this issue, reward modeling techniques have emerged. Traditional Outcome Reward Models (ORMs)[19, 20], which assign rewards based solely on the final answer, fail to detect flawed intermediate reasoning. Process Reward Models (PRMs)[39, 31, 40, 41] overcome this limitation by explicitly providing step-level supervision, significantly improving logical coherence. Representative works such as PRM800K [39], MathShepherd [31], and MiPS [40] have demonstrated the effectiveness of PRMs in enhancing mathematical reasoning. During the preparation of this manuscript, we became aware of a concurrent effort, URSA [46], which also explores PRM training. While both approaches share some methodological similarities in PRM construction, our work places greater emphasis on building a scalable PRM pipeline and analyzing training dynamics, whereas URSA focuses more on integrating PRMs into RL.\n\nOverall, PRMs have become an essential approach for improving the robustness and logical consistency of LLM reasoning through fine-grained, step-level evaluation.\n\n## 2.2 Process supervision data construction\n\nTraining PRMs requires large-scale, high-quality step-level annotations that indicate the correctness of each intermediate reasoning step. However, most publicly available datasets focus solely on final answers, making it challenging to obtain supervision signals for reasoning quality. Existing process supervision construction methods can be broadly categorized into three classes:\n\n**Manual Annotation.** The earliest efforts, such as PRM800K [39], relied on human experts to label each reasoning step. While this yields high-quality annotations, the approach is costly, time-consuming, and difficult to scale—particularly for domains like mathematics where expert knowledge is required.\n\n**Monte Carlo Estimation.** Works like MathShepherd [31] and MiPS [40] automate supervision by sampling multiple rollouts from each reasoning prefix and estimating step correctness based on the proportion of successful completions. If continuations from a given step often lead to correct answers, that step is considered reliable. This method is simple but suffers from label instability due to high variance in sampled rollouts—especially on long or complex reasoning chains.\n\n**Monte Carlo Tree Search (MCTS).** To address these limitations, OmegaPRM [41] introduces a structured, search-based alternative. Using a divide-and-conquer MCTS algorithm, it efficiently identifies the first error in a reasoning chain and constructs a tree of reasoning paths with dynamically updated statistics. This approach improves annotation stability, better handles deep reasoning tasks, and generates large volumes of fine-grained supervision from limited seed data without human input.\n\nEach method reflects a trade-off between cost, scalability, and label fidelity. Among them, MCTS-based approaches have recently emerged as the most effective strategy for generating robust and scalable process supervision, especially for multi-step mathematical reasoning tasks.\n\n# 3 Method\n\n## 3.1 Overview\n\nWe present a scalable and fully automated framework for training PRMs tailored to multimodal mathematical reasoning. Our approach addresses two critical bottlenecks in prior work: **the lack of step-level supervision** and the **inefficiency of data generation in complex reasoning tasks**. To overcome these challenges, we introduce a structured three-stage pipeline that enables fine-grained reward modeling without any human annotation. As shown in Figure 1, the framework comprises three interconnected stages as follows:Figure 1: Overview of our automated three-stage framework for training MM-PRM: supervised policy model construction, MCTS-based process supervision data generation, and step-level reward model training.\n\n1. (1) **Policy Model Construction**, where a multimodal policy model is trained to generate high-quality reasoning traces following the CoT paradigm.\n2. (2) **Process Supervision Data Generation**, where we use a MCTS-based engine, OmegaPRM [41], to efficiently identify reasoning flaws and produce step-level reward labels at scale.\n3. (3) **Process Reward Model Training**, where a PRM is trained to evaluate each reasoning step and provide dense feedback.\n\nThis end-to-end design ensures that process supervision can be generated, modeled, and applied in a fully closed loop. It significantly improves reasoning quality and robustness, especially in tasks requiring long logical chains. In Sections 3.2–3.3 below, we elaborate on these three stages.\n\n### 3.2 Policy model construction\n\nThe policy model serves as the foundation of our framework, responsible for generating candidate reasoning trajectories given multimodal math problems. These trajectories are later evaluated and labeled to form step-level supervision for training the PRM. Ensuring that the policy model produces logically coherent and structurally complete outputs is thus essential for the effectiveness of the entire system.\n\nTo train the policy model, we curated a large-scale, high-quality dataset of mathematical problems spanning a wide range of topics and difficulty levels. Our dataset integrates samples from over a dozen public math datasets, including R-CoT [47], MAVIS [48], MathV360K [49], NuminaMath [50], and DART-Math [51], with problems ranging from elementary school arithmetic to advanced geometry and statistics. The full list of data sources and sample counts used for training is provided in Appendix A.\n\nOnce collected, all data undergo rigorous cleaning and format standardization. Visual and textual content are paired explicitly, and reasoning traces are reformatted to follow a structured CoT schema, with each logical step clearly marked using structured tags such as `&lt;step>&lt;/step>`, and the final conclusion labeled with `&lt;answer>&lt;/answer>`. To enhance quality and clarity, we leveraged a strong instruction-tuned language model (i.e., Qwen2.5-72B-Instruct [2]) to parse original solutions and restructure them into coherent, modular steps. This structured representation not only enhances model learnability but also lays the foundation for generating step-level reward labels in the next stage. The prompt used for solution restructuring is provided in Appendix B.With this cleaned and annotated corpus of over 5 million examples, we fine-tuned a strong open-source multimodal model, InternVL2.5-8B [16], using supervised learning. This ensures that the model learns to produce logically sound and well-structured outputs that conform to the CoT reasoning pattern.\n\nThe resulting model not only delivers high-quality reasoning trajectories for downstream data annotation but also supports inference-time use cases such as BoN selection with reward-based reranking. Its strong generative ability and logical consistency form the cornerstone of our scalable process supervision framework.\n\n### 3.3 Process supervision data generation\n\nTo enable fine-grained supervision for step-level reasoning, we adopt an automated process annotation pipeline based on the OmegaPRM [41] framework. OmegaPRM introduces a MCTS-based mechanism for efficiently identifying and labeling intermediate reasoning steps with confidence estimates. Although originally developed for textual mathematical reasoning, we adapt and extend this framework to handle multimodal inputs.\n\nOur process begins with collecting a curated dataset of 10,000 multimodal math problems from real-world named **MM-K12**—consisting of 5,000 fill-in-the-blank and 5,000 multiple-choice questions. These problems span a range of curriculum topics from elementary to high school and serve as seed instances for process supervision generation. All examples in MM-K12 are carefully filtered to ensure that each question includes meaningful visual input and has a unique, verifiable answer, making them well-suited for structured reasoning and reward modeling. In addition, MM-K12 also provides an independent test set of 500 problems, constructed under the same criteria, which we use to evaluate in-distribution performance later. For each problem, the policy model produces multiple candidate solutions following the CoT paradigm, and these reasoning paths form the raw material for subsequent reward annotation.\n\nTo evaluate the correctness of each intermediate step, we follow OmegaPRM’s hierarchical rollout and search protocol. Specifically, we generate multiple completions (rollouts) from partial prefixes and estimate the correctness of a given step based on whether its downstream completions reach the correct final answer. By applying binary search, the algorithm efficiently pinpoints the earliest step at which the reasoning begins to deviate. These supervision signals are then aggregated within a structured state-action tree, which records the Monte Carlo (MC) estimates and other statistics at each reasoning state. In our implementation, we maintain the full multimodal context—including both textual and visual components—throughout the tree construction and search process.\n\nImportantly, our adaptation retains the efficiency of OmegaPRM’s divide-and-conquer search while enabling reward supervision for reasoning steps that are conditioned on complex visual stimuli. Through this pipeline, we generate over 700,000 step-level annotations from only 10k seed questions, without requiring manual labeling. The resulting dataset provides dense, high-quality process supervision aligned with real-world multimodal reasoning.\n\n### 3.4 Process reward model training\n\nWith large-scale step-level supervision in place, we proceed to train a PRM that can assess the quality of reasoning steps given a multimodal context. The PRM is designed to serve as a fine-grained critic, assigning a reward score to each intermediate step conditioned on its preceding reasoning context that enables both test-time scaling and potential RL applications.\n\n#### 3.4.1 Labeling strategy\n\nA central design decision in PRM training lies in how to formulate supervision signals from the MC estimations [41, 32]. Rather than adopting hard binary label (e.g.,  $\\hat{y} = 1[\\text{MC}(s) > \\tau]$ ), we use soft label, directly taking the MC scores as continuous supervision targets.\n\nThis choice is motivated by the observation that the MC score reflects more than the correctness of an intermediate step. It also encodes factors such as problem difficulty, step criticality, and distributional uncertainty in the policy model’s rollouts. For instance, a reasoning step within a highly ambiguous or visually complex problem may yield lower MC scores even if the logic is fundamentally sound. In such cases, hard-thresholding may misrepresent the step’s quality, introducing noise into training. Bycontrast, soft labels preserve the probabilistic nuance and enable smoother learning dynamics, more details will be discussed in section 5.3\n\nFormally, for each reasoning step  $x_t$  in a path  $x = [x_1, x_2, \\dots, x_T]$ , we assign a supervision target  $\\hat{y}_t = \\text{MC}(x_{&lt;t}) \\in [0, 1]$ , where  $\\text{MC}(x_{&lt;t})$  denotes the estimated probability that a correct final answer can be reached from this partial path.\n\n### 3.4.2 Model design and training objective\n\nTo model the prediction task, we treat the PRM as a classifier operating on each reasoning step. Given a multimodal input  $q$  and a generated reasoning trace  $[x_1, x_2, \\dots, x_T]$ , we interleave a special marker token, denoted  $\\sigma$ , after each step, producing an input sequence of the form:\n\n$$[q, x_1, \\sigma, x_2, \\sigma, \\dots, x_T, \\sigma].$$\n\nIn our implementation,  $\\sigma$  is instantiated as the token  $\\langle \\text{prm} \\rangle$ . At each occurrence of  $\\sigma$ , the model is tasked with producing a scalar confidence score indicating the likelihood that the immediately preceding step is logically correct. Formally, let  $z_{\\text{Yes}}^{(i)}$  and  $z_{\\text{No}}^{(i)}$  denote the unnormalized logits for binary labels ‘‘Yes’’ (correct) and ‘‘No’’ (incorrect) at the  $i$ -th occurrence of  $\\sigma$ . The model’s predicted probability is computed via softmax:\n\n$$p^{(i)} = \\frac{\\exp(z_{\\text{Yes}}^{(i)})}{\\exp(z_{\\text{Yes}}^{(i)}) + \\exp(z_{\\text{No}}^{(i)})}.$$\n\nThe training objective is to minimize the **cross-entropy loss** between the predicted scores  $p^{(i)}$  and the soft labels  $\\hat{y}^{(i)}$ , across all scoring points:\n\n$$\\mathcal{L}_{\\text{PRM}} = - \\sum_{i=1}^T \\left[ \\hat{y}^{(i)} \\cdot \\log p^{(i)} + (1 - \\hat{y}^{(i)}) \\cdot \\log(1 - p^{(i)}) \\right].$$\n\nThis formulation guides the model to make fine-grained assessments of reasoning steps, assigning higher confidence to those with stronger evidence of correctness.\n\n## 4 Experiments\n\n### 4.1 Experiments setup\n\nTo validate the effectiveness of our proposed process reward modeling framework, we conduct a series of experiments, carefully configured to ensure fair, scalable, and reproducible results.\n\n**Policy model construction.** Our policy model (i.e., MM-Policy) is initialized from the multimodal backbone InternVL 2.5-8B and fine-tuned using approximately 4 million cleaned, structured math problems. The model is trained for 1 epoch with a batch size of 128 and a learning rate of 4e-5, updating only the language module while keeping the vision encoder frozen.\n\n**Process supervision data generation.** We adapt the OmegaPRM[41] pipeline for multimodal reasoning and apply it to MM-K12 (10k samples). Using MCTS-based structured rollouts, we generate approximately 747,000 step-level annotations. The sampling parameters are tuned for balance between diversity and efficiency:  $temperature = 1.0$ ,  $top_k = 50$ ,  $top_p = 0.9$ , exploration coefficient  $c_{\\text{puct}} = 0.125$ , and up to 200 search steps or 1,000 total rollouts per problem.\n\n**Process reward model training.** We initialize the PRM from the fine-tuned policy model and train it for 1 epochs with a batch size of 512 and a learning rate of 4e-6.\n\n### 4.2 Evaluation strategies and benchmarks\n\nTo assess the effectiveness of the proposed MM-PRM in improving reasoning quality, we adopt the BoN evaluation protocol. For each test problem, the policy model generates  $N = 16$  candidate reasoning paths independently. The PRM then scores each path step-by-step, producing a sequence of floating-point values representing the predicted quality of each intermediate step, the path with the highest score is selected as the final answer.Since PRM outputs a vector of step-wise confidence scores for each candidate path, a crucial component of our evaluation is the *aggregation function* [40] used to compress this vector into a scalar. We explore a diverse set of aggregation functions, including Min, Average, Max, SumLogPr (i.e., sum of log-probabilities), SumLogOdds (i.e., sum of log-odds), and MeanOdds (i.e., mean odds), each function captures different aspects of path quality. Additionally, a Random baseline is used for comparison, where the final answer is randomly sampled from the same set of 16 candidates. Formal definitions of all aggregation functions are provided in Appendix C.\n\nWe evaluate performance using answer accuracy, defined as the proportion of final selected answers that match the ground truth. This metric directly reflects MM-PRM’s utility in guiding the selection of correct reasoning paths. To comprehensively evaluate our model’s performance and generalization, we conduct experiments on a range of multimodal math benchmarks, including MM-K12 (test set), OlympiadBench (OE\\_MM\\_maths\\_en\\_COMP) [52], MathVista(testmini) [53], MathVerse(testmini) [54], and MathVision(test) [55]. The MM-K12 test set serves as an in-distribution evaluation. For out-of-distribution assessment, we use the OE\\_MM\\_maths\\_en\\_COMP split of OlympiadBench, which contains open-ended multimodal questions from international math competitions, closely related in format to MM-K12 but significantly harder. To further test generalization, we include MathVista, which covers a wide range of visual mathematical tasks; MathVerse, which emphasizes understanding structured visual content; and MathVision, which targets abstract visual reasoning. These benchmarks provide a diverse and rigorous setting to measure both performance and generalization of our process reward modeling framework.\n\n### 4.3 Quantitative results\n\nTable 1: Performance improvements across various benchmarks when applying the MM-PRM to different models.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Model&lt;/th>\n&lt;th>MM-K12&lt;/th>\n&lt;th>OlympiadBench&lt;/th>\n&lt;th>MathVista&lt;/th>\n&lt;th>MathVerse&lt;/th>\n&lt;th>MathVision&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>MM-Policy&lt;/td>\n&lt;td>33.92&lt;/td>\n&lt;td>15.41&lt;/td>\n&lt;td>62.93&lt;/td>\n&lt;td>42.99&lt;/td>\n&lt;td>21.74&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>+MM-PRM&lt;/td>\n&lt;td>42.80&lt;/td>\n&lt;td>24.00&lt;/td>\n&lt;td>67.60&lt;/td>\n&lt;td>46.27&lt;/td>\n&lt;td>27.11&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;/td>\n&lt;td>&lt;b>+8.88&lt;/b>&lt;/td>\n&lt;td>&lt;b>+8.59&lt;/b>&lt;/td>\n&lt;td>&lt;b>+4.67&lt;/b>&lt;/td>\n&lt;td>&lt;b>+3.28&lt;/b>&lt;/td>\n&lt;td>&lt;b>+5.37&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>InternVL2.5-8B&lt;/td>\n&lt;td>27.01&lt;/td>\n&lt;td>5.23&lt;/td>\n&lt;td>56.43&lt;/td>\n&lt;td>36.26&lt;/td>\n&lt;td>10.04&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>+MM-PRM&lt;/td>\n&lt;td>37.80&lt;/td>\n&lt;td>15.33&lt;/td>\n&lt;td>63.50&lt;/td>\n&lt;td>42.56&lt;/td>\n&lt;td>19.41&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;/td>\n&lt;td>&lt;b>+10.79&lt;/b>&lt;/td>\n&lt;td>&lt;b>+10.10&lt;/b>&lt;/td>\n&lt;td>&lt;b>+7.07&lt;/b>&lt;/td>\n&lt;td>&lt;b>+6.30&lt;/b>&lt;/td>\n&lt;td>&lt;b>+9.37&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>InternVL2.5-26B&lt;/td>\n&lt;td>28.01&lt;/td>\n&lt;td>14.46&lt;/td>\n&lt;td>60.02&lt;/td>\n&lt;td>37.83&lt;/td>\n&lt;td>20.76&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>+MM-PRM&lt;/td>\n&lt;td>38.00&lt;/td>\n&lt;td>24.67&lt;/td>\n&lt;td>64.50&lt;/td>\n&lt;td>44.19&lt;/td>\n&lt;td>25.63&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;/td>\n&lt;td>&lt;b>+9.99&lt;/b>&lt;/td>\n&lt;td>&lt;b>+10.21&lt;/b>&lt;/td>\n&lt;td>&lt;b>+4.25&lt;/b>&lt;/td>\n&lt;td>&lt;b>+6.36&lt;/b>&lt;/td>\n&lt;td>&lt;b>+4.87&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>InternVL2.5-38B&lt;/td>\n&lt;td>40.34&lt;/td>\n&lt;td>29.57&lt;/td>\n&lt;td>68.32&lt;/td>\n&lt;td>47.94&lt;/td>\n&lt;td>29.70&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>+MM-PRM&lt;/td>\n&lt;td>52.40&lt;/td>\n&lt;td>32.67&lt;/td>\n&lt;td>71.10&lt;/td>\n&lt;td>52.61&lt;/td>\n&lt;td>32.99&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;/td>\n&lt;td>&lt;b>+12.06&lt;/b>&lt;/td>\n&lt;td>&lt;b>+3.10&lt;/b>&lt;/td>\n&lt;td>&lt;b>+2.78&lt;/b>&lt;/td>\n&lt;td>&lt;b>+4.67&lt;/b>&lt;/td>\n&lt;td>&lt;b>+3.29&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>InternVL2.5-78B&lt;/td>\n&lt;td>42.24&lt;/td>\n&lt;td>30.98&lt;/td>\n&lt;td>69.48&lt;/td>\n&lt;td>50.18&lt;/td>\n&lt;td>31.50&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>+MM-PRM&lt;/td>\n&lt;td>48.80&lt;/td>\n&lt;td>34.67&lt;/td>\n&lt;td>73.20&lt;/td>\n&lt;td>54.47&lt;/td>\n&lt;td>33.26&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;/td>\n&lt;td>&lt;b>+6.56&lt;/b>&lt;/td>\n&lt;td>&lt;b>+3.69&lt;/b>&lt;/td>\n&lt;td>&lt;b>+3.72&lt;/b>&lt;/td>\n&lt;td>&lt;b>+4.29&lt;/b>&lt;/td>\n&lt;td>&lt;b>+1.76&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nWe evaluate the effectiveness of MM-PRM by applying it to a range of policy models and testing its impact across multiple multimodal math benchmarks.\n\nAcross all models, MM-PRM yields substantial performance improvements. For example, when applied to MM-Policy on the MM-K12 test set, accuracy improves from 33.92% to 42.80%, and similar gains are observed with InternVL2.5-8B, where performance rises from 27.01% to 37.80%. These results confirm that MM-PRM is highly effective at identifying high-quality reasoning paths.\n\nBeyond in-domain settings, we observe that MM-PRM also generalizes well to larger models and more challenging datasets. As shown in Table 1, applying MM-PRM to InternVL2.5-78B improves accuracy on OlympiadBench from 30.98% to 34.67%, and on MathVerse from 50.18% to 54.47%. Despite being trained only on the small MM-K12 seed dataset and with a fixed policy model(i.e., MM-Policy), MM-PRM consistently enhances reasoning accuracy across diverse benchmarks and models. This demonstrates the potential of scalable step-level reward modeling to improve mathematical**Question**\n\nAs shown in the figure, it is known that  $AB \\parallel CD$ ,  $CE$  bisect  $\\angle ACD$ , and intersects  $AB$  at  $E$ ,  $\\angle A = 118^\\circ$ . Then  $\\angle AEC = ?$\n\n**Solution**\n\n( $\\hat{A} = 0.83$ ) Identify the relationship between the angles formed by the parallel lines and the transversal. Since  $AB \\parallel CD$  and  $\\angle A = 118^\\circ$ , We can use the property of parallel lines and transversals to determine the measure of  $\\angle ACD$ . The angles on a straight line sum up to  $180^\\circ$ . So:  $\\angle ACD = 180^\\circ - \\angle A = 180^\\circ - 118^\\circ = 62^\\circ$\n\n( $\\hat{A} = 0.68$ ) Use the angle bisector property. Since  $CE$  bisect  $\\angle ACD$ , it divides  $\\angle ACD$  into two equal angles. Therefore:  $\\angle ACE = \\frac{\\angle ACD}{2} = \\frac{62^\\circ}{2} = 31^\\circ$\n\n( $\\hat{A} = 0.02$ ) Determine  $\\angle AEC$  using the exterior angle theorem. In  $\\triangle AEC$ ,  $\\angle AEC$  is an exterior angle and is equal to the sum of the two non-adjacent interior angles  $\\angle A$  and  $\\angle ACE$ . However, since  $\\angle AEC$  is directly opposite  $\\angle ACE$  and  $\\angle A$  is the exterior angle, we can use the fact that the exterior angle is the sum of the two non-adjacent interior angles:  $\\angle AEC = \\angle A - \\angle ACE = 118^\\circ - 31^\\circ = 87^\\circ$\n\n( $\\hat{A} = 0.01$ ) Answer: The Final Answer is 87\n\nFigure 2: Qualitative example of MM-PRM accurately identifying error steps in multimodal reasoning process.\n\nreasoning in a model-agnostic and data-efficient manner. Detailed evaluation results across all aggregation functions are provided in Appendix D.\n\n#### 4.4 Qualitative results\n\nTo further illustrate the behavior of MM-PRM, we present a qualitative example involving a geometry problem with parallel lines and an angle bisector. As shown in Figure 2, the policy model generates a four-step reasoning path, which ultimately leads to an incorrect final answer.\n\nThe PRM assigns high scores to the first two steps (0.83 and 0.68), indicating that they are logically sound. In contrast, Step-3 receives a very low score (0.02), signaling that the model has identified a significant reasoning error at this point. This flawed step leads directly to an incorrect conclusion in Step-4.\n\nThis example demonstrates that MM-PRM is capable of detecting localized logical errors within a reasoning chain, such fine-grained judgment is crucial in selecting high-quality reasoning trajectories and filtering out those with subtle but critical flaws.\n\n## 5 Discussion\n\nFigure 3: (a) Effect of the number of candidate reasoning paths on answer accuracy under Best-of-N inference. Increasing the number of candidates allows the PRM to select higher-quality reasoning trajectories. (b) Effect of learning rate on PRM performance. Small learning rates yield better accuracy, with performance peaking at  $4 \\times 10^{-6}$## 5.1 Candidate path’s impact on PRM performance\n\nSince the PRM operates purely as a selector in the BoN framework, its performance is inherently bounded by the diversity and quality of candidate reasoning paths produced by the policy model. In other words, PRM cannot improve a flawed generation in BoN—it can only choose among the available options. Therefore, the number of reasoning paths generated per problem directly affects its potential to identify a correct and coherent solution.\n\nTo study this effect, we vary the number of generated reasoning paths  $N \\in \\{2, 2^2, 2^3, 2^4\\}$  and measure the corresponding answer accuracy under the aggregation strategy MeanOdds. As shown in Figure 3(a), increasing  $N$  consistently improves MM-PRM’s performance across both test sets. On the MM-K12 test set, accuracy improves from 38.6% at  $N = 2$  to 42.8% at  $N = 16$ , with gains tapering off beyond  $N = 8$ . In contrast, on OlympiadBench, accuracy increases more steadily—from 18.4% to 24.0%—as  $N$  grows. This suggests that for harder, more diverse tasks, having a larger pool of reasoning paths is critical for PRM to identify valid solutions.\n\n## 5.2 Learning rate\n\nAs noted in [39], finetuning a PRM shifts the language models’ objective from generation to discrimination, making learning rate a critical factor. Smaller learning rates are often preferred to maintain stability and preserve pretrained knowledge.\n\nWe evaluate MM-PRM trained under different learning rates on the MM-K12 test set using MeanOdds aggregator. As shown in Figure 3(b), performance peaks at  $4e-6$ —about one-tenth the learning rate typically used in supervised fine-tuning—then drops sharply at higher values. This confirms that a moderate, conservative learning rate leads to better training, while overly large values degrade accuracy.\n\n## 5.3 Soft label vs. Hard label\n\nTable 2: The performance comparisons of soft label vs. hard label.\n\n&lt;table border=\"1\">&lt;thead>&lt;tr>&lt;th>Labeling Strategy&lt;/th>&lt;th>Min&lt;/th>&lt;th>Average&lt;/th>&lt;th>Max&lt;/th>&lt;th>SumLogPr&lt;/th>&lt;th>SumLogOdds&lt;/th>&lt;th>MeanOdds&lt;/th>&lt;/tr>&lt;/thead>&lt;tbody>&lt;tr>&lt;td>Soft Label&lt;/td>&lt;td>37.4&lt;/td>&lt;td>43.0&lt;/td>&lt;td>43.4&lt;/td>&lt;td>42.0&lt;/td>&lt;td>43.2&lt;/td>&lt;td>42.8&lt;/td>&lt;/tr>&lt;tr>&lt;td>Hard Label&lt;/td>&lt;td>36.8&lt;/td>&lt;td>34.4&lt;/td>&lt;td>35.6&lt;/td>&lt;td>36.0&lt;/td>&lt;td>33.8&lt;/td>&lt;td>37.0&lt;/td>&lt;/tr>&lt;/tbody>&lt;/table>\n\nAs discussed in section 3.4.1, we adopt soft label—i.e., real-valued MC scores—as supervision for step-level reward modeling. Unlike hard label, soft label retain uncertainty and allow the model to learn more nuanced representations of reasoning quality.\n\nTo assess this design choice, we compare soft label with hard label thresholding, where steps with  $MC > 0$  are treated as correct, and others as incorrect, following the protocol in [41, 56].\n\nAs shown in Table 2, soft-label training consistently outperforms hard-label training across all aggregation strategies. For instance, under the Average aggregator, soft labels yield 43% accuracy on MM-K12 test set, compared to 34.4% with hard labels. Similar improvements are observed with SumLogOdds (43.2% vs. 33.8%) and MeanOdds (42.8% vs. 37.0%).\n\n## 6 Conclusion\n\nIn this work, we introduce MM-PRM, a process reward model built upon a scalable framework for multimodal mathematical process reward modeling that enables step-level supervision without human annotation. By leveraging a multimodal policy model and an MCTS-based data generation pipeline, we construct over 700k process-level labels from only 10k K-12 math problems in our MM-K12 dataset. Our trained PRM significantly improves reasoning accuracy in BoN inference across both standard and challenging benchmarks, and demonstrates strong generalization to new datasets and models. Extensive analysis further confirms the importance of soft labeling, conservative learning rates, and sufficient path diversity. MM-PRM highlights the value of process supervision for enhancing multimodal mathematical problem-solving.## References\n\n- [1] Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. Gpt-4 technical report. *arXiv preprint arXiv:2303.08774*, 2023.\n- [2] Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang, Xiaodong Deng, Yang Fan, Wenbin Ge, Yu Han, Fei Huang, et al. Qwen technical report. *arXiv preprint arXiv:2309.16609*, 2023.\n- [3] Gemini Team, Rohan Anil, Sebastian Borgeaud, Jean-Baptiste Alayrac, Jiahui Yu, Radu Soricut, Johan Schalkwyk, Andrew M Dai, Anja Hauth, Katie Millican, et al. Gemini: a family of highly capable multimodal models. *arXiv preprint arXiv:2312.11805*, 2023.\n- [4] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, et al. Llama: Open and efficient foundation language models. *arXiv preprint arXiv:2302.13971*, 2023.\n- [5] Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al. Llama 2: Open foundation and fine-tuned chat models. *arXiv preprint arXiv:2307.09288*, 2023.\n- [6] Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Alex Vaughan, et al. The llama 3 herd of models. *arXiv preprint arXiv:2407.21783*, 2024.\n- [7] InternLM Team. Internlm: A multilingual language model with progressively enhanced capabilities. &lt;https://github.com/InternLM/InternLM-techreport>, 2023.\n- [8] Zheng Cai, Maosong Cao, Haojiong Chen, Kai Chen, Keyu Chen, Xin Chen, Xun Chen, Zehui Chen, Zhi Chen, Pei Chu, et al. Internlm2 technical report. *arXiv preprint arXiv:2403.17297*, 2024.\n- [9] Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. *arXiv preprint arXiv:2501.12948*, 2025.\n- [10] Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. Visual instruction tuning. *Advances in neural information processing systems*, 36:34892–34916, 2023.\n- [11] Yuan Yao, Tianyu Yu, Ao Zhang, Chongyi Wang, Junbo Cui, Hongji Zhu, Tianchi Cai, Haoyu Li, Weilin Zhao, Zhihui He, et al. Minicpm-v: A gpt-4v level mllm on your phone. *arXiv preprint arXiv:2408.01800*, 2024.\n- [12] Zhe Chen, Weiyun Wang, Yue Cao, Yangzhou Liu, Zhangwei Gao, Erfei Cui, Jinguo Zhu, Shenglong Ye, Hao Tian, Zhaoyang Liu, et al. Expanding performance boundaries of open-source multimodal models with model, data, and test-time scaling. *arXiv preprint arXiv:2412.05271*, 2024.\n- [13] Weiyun Wang, Zhe Chen, Wenhai Wang, Yue Cao, Yangzhou Liu, Zhangwei Gao, Jinguo Zhu, Xizhou Zhu, Lewei Lu, Yu Qiao, and Jifeng Dai. Enhancing the reasoning ability of multimodal large language models via mixed preference optimization. *arXiv preprint arXiv:2411.10442*, 2024.\n- [14] Zhangwei Gao, Zhe Chen, Erfei Cui, Yiming Ren, Weiyun Wang, Jinguo Zhu, Hao Tian, Shenglong Ye, Junjun He, Xizhou Zhu, et al. Mini-internvl: a flexible-transfer pocket multi-modal model with 5% parameters and 90% performance. *Visual Intelligence*, 2(1):1–17, 2024.\n- [15] Zhe Chen, Weiyun Wang, Hao Tian, Shenglong Ye, Zhangwei Gao, Erfei Cui, Wenwen Tong, Kongzhi Hu, Jiapeng Luo, Zheng Ma, et al. How far are we to gpt-4v? closing the gap to commercial multimodal models with open-source suites. *Science China Information Sciences*, 67(12):220101, 2024.\n- [16] Zhe Chen, Jiannan Wu, Wenhai Wang, Weijie Su, Guo Chen, Sen Xing, Muyan Zhong, Qinglong Zhang, Xizhou Zhu, Lewei Lu, et al. Internvl: Scaling up vision foundation models and aligning for generic visual-linguistic tasks. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, pages 24185–24198, 2024.\n- [17] Jinze Bai, Shuai Bai, Shusheng Yang, Shijie Wang, Sinan Tan, Peng Wang, Junyang Lin, Chang Zhou, and Jingren Zhou. Qwen-vl: A versatile vision-language model for understanding, localization, text reading, and beyond. *arXiv preprint arXiv:2308.12966*, 2023.\n- [18] Kimi Team, Angang Du, Bofei Gao, Bowei Xing, Changjiu Jiang, Cheng Chen, Cheng Li, Chenjun Xiao, Chenzhuang Du, Chonghua Liao, et al. Kimi k1. 5: Scaling reinforcement learning with llms. *arXiv preprint arXiv:2501.12599*, 2025.\n- [19] Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, et al. Training verifiers to solve math word problems. *arXiv preprint arXiv:2110.14168*, 2021.\n- [20] Fei Yu, Anningzhe Gao, and Benyou Wang. Ovm, outcome-supervised value models for planning in mathematical reasoning. *arXiv preprint arXiv:2311.09724*, 2023.- [21] Jonathan Uesato, Nate Kushman, Ramana Kumar, Francis Song, Noah Siegel, Lisa Wang, Antonia Creswell, Geoffrey Irving, and Irina Higgins. Solving math word problems with process-and outcome-based feedback. *arXiv preprint arXiv:2211.14275*, 2022.\n- [22] Yuhang Zang, Xiaoyi Dong, Pan Zhang, Yuhang Cao, Ziyu Liu, Shengyuan Ding, Shenxi Wu, Yubo Ma, Haodong Duan, Wenwei Zhang, et al. Internlm-xcomposer2. 5-reward: A simple yet effective multi-modal reward model. *arXiv preprint arXiv:2501.12368*, 2025.\n- [23] Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training language models to follow instructions with human feedback. *Advances in neural information processing systems*, 35:27730–27744, 2022.\n- [24] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. *arXiv preprint arXiv:1707.06347*, 2017.\n- [25] Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li, Y Wu, et al. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. *arXiv preprint arXiv:2402.03300*, 2024.\n- [26] Xin Lai, Zhuotao Tian, Yukang Chen, Senqiao Yang, Xiangru Peng, and Jiaya Jia. Step-dpo: Step-wise preference optimization for long-chain reasoning of llms. *arXiv preprint arXiv:2406.18629*, 2024.\n- [27] Weiyun Wang, Zhe Chen, Wenhai Wang, Yue Cao, Yangzhou Liu, Zhangwei Gao, Jinguo Zhu, Xizhou Zhu, Lewei Lu, Yu Qiao, et al. Enhancing the reasoning ability of multimodal large language models via mixed preference optimization. *arXiv preprint arXiv:2411.10442*, 2024.\n- [28] Richard Yuanzhe Pang, Weizhe Yuan, He He, Kyunghyun Cho, Sainbayar Sukhbaatar, and Jason Weston. Iterative reasoning preference optimization. *Advances in Neural Information Processing Systems*, 37:116617–116637, 2024.\n- [29] Hanze Dong, Wei Xiong, Bo Pang, Haoxiang Wang, Han Zhao, Yingbo Zhou, Nan Jiang, Doyen Sahoo, Caiming Xiong, and Tong Zhang. Rlhf workflow: From reward modeling to online rlhf. *arXiv preprint arXiv:2405.07863*, 2024.\n- [30] Charlie Snell, Jaehoon Lee, Kelvin Xu, and Aviral Kumar. Scaling llm test-time compute optimally can be more effective than scaling model parameters. *arXiv preprint arXiv:2408.03314*, 2024.\n- [31] Peiyi Wang, Lei Li, Zhihong Shao, RX Xu, Damai Dai, Yifei Li, Deli Chen, Yu Wu, and Zhifang Sui. Math-shepherd: Verify and reinforce llms step-by-step without human annotations. *arXiv preprint arXiv:2312.08935*, 2023.\n- [32] Zhenru Zhang, Chujie Zheng, Yangzhen Wu, Beichen Zhang, Runji Lin, Bowen Yu, Dayiheng Liu, Jingren Zhou, and Junyang Lin. The lessons of developing process reward models in mathematical reasoning. *arXiv preprint arXiv:2501.07301*, 2025.\n- [33] Xidong Feng, Ziyu Wan, Muning Wen, Stephen Marcus McAleer, Ying Wen, Weinan Zhang, and Jun Wang. Alphazero-like tree-search can guide large language model decoding and training. *arXiv preprint arXiv:2309.17179*, 2023.\n- [34] Jikun Kang, Xin Zhe Li, Xi Chen, Amirreza Kazemi, Qianyi Sun, Boxing Chen, Dong Li, Xu He, Quan He, Feng Wen, et al. Mindstar: Enhancing math reasoning in pre-trained llms at inference time. *arXiv preprint arXiv:2405.16265*, 2024.\n- [35] Qianli Ma, Haotian Zhou, Tingkai Liu, Jianbo Yuan, Pengfei Liu, Yang You, and Hongxia Yang. Let’s reward step by step: Step-level reward model as the navigators for reasoning. *arXiv preprint arXiv:2310.10080*, 2023.\n- [36] Ye Tian, Baolin Peng, Linfeng Song, Lifeng Jin, Dian Yu, Lei Han, Haitao Mi, and Dong Yu. Toward self-improvement of llms via imagination, searching, and criticizing. *Advances in Neural Information Processing Systems*, 37:52723–52748, 2024.\n- [37] Dan Zhang, Sining Zhoubian, Ziniu Hu, Yisong Yue, Yuxiao Dong, and Jie Tang. Rest-mcts\\*: Llm self-training via process reward guided tree search. *Advances in Neural Information Processing Systems*, 37:64735–64772, 2024.\n- [38] Yifei Li, Zeqi Lin, Shizhuo Zhang, Qiang Fu, Bei Chen, Jian-Guang Lou, and Weizhu Chen. Making large language models better reasoners with step-aware verifier. *arXiv preprint arXiv:2206.02336*, 2022.\n- [39] Hunter Lightman, Vineet Kosaraju, Yuri Burda, Harrison Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. Let’s verify step by step. In *The Twelfth International Conference on Learning Representations*, 2023.\n- [40] Zihan Wang, Yunxuan Li, Yuexin Wu, Liangchen Luo, Le Hou, Hongkun Yu, and Jingbo Shang. Multi-step problem solving through a verifier: An empirical analysis on model-induced process supervision. *arXiv preprint arXiv:2402.02658*, 2024.- [41] Liangchen Luo, Yinxiao Liu, Rosanne Liu, Samrat Phatale, Meiqi Guo, Harsh Lara, Yunxuan Li, Lei Shu, Yun Zhu, Lei Meng, et al. Improve mathematical reasoning in language models by automated process supervision. *arXiv preprint arXiv:2406.06592*, 2024.\n- [42] Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. Measuring mathematical problem solving with the math dataset. *arXiv preprint arXiv:2103.03874*, 2021.\n- [43] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models. *Advances in neural information processing systems*, 35:24824–24837, 2022.\n- [44] Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. Self-consistency improves chain of thought reasoning in language models. *arXiv preprint arXiv:2203.11171*, 2022.\n- [45] Aaron Jaech, Adam Kalai, Adam Lerer, Adam Richardson, Ahmed El-Kishky, Aiden Low, Alec Hel-yar, Aleksander Madry, Alex Beutel, Alex Carney, et al. Openai o1 system card. *arXiv preprint arXiv:2412.16720*, 2024.\n- [46] Ruilin Luo, Zhuofan Zheng, Yifan Wang, Yiyao Yu, Xinzhe Ni, Zicheng Lin, Jin Zeng, and Yujiu Yang. Ursa: Understanding and verifying chain-of-thought reasoning in multimodal mathematics. *arXiv preprint arXiv:2501.04686*, 2025.\n- [47] Linger Deng, Yuliang Liu, Bohan Li, Dongliang Luo, Liang Wu, Chengquan Zhang, Pengyuan Lyu, Ziyang Zhang, Gang Zhang, Errui Ding, et al. R-cot: Reverse chain-of-thought problem generation for geometric reasoning in large multimodal models. *arXiv preprint arXiv:2410.17885*, 2024.\n- [48] Renrui Zhang, Xinyu Wei, Dongzhi Jiang, Ziyu Guo, Shicheng Li, Yichi Zhang, Chengzhuo Tong, Jiaming Liu, Aojun Zhou, Bin Wei, et al. Mavis: Mathematical visual instruction tuning with an automatic data engine. *arXiv preprint arXiv:2407.08739*, 2024.\n- [49] Wenhao Shi, Zhiqiang Hu, Yi Bin, Junhua Liu, Yang Yang, See-Kiong Ng, Lidong Bing, and Roy Ka-Wei Lee. Math-llava: Bootstrapping mathematical reasoning for multimodal large language models. *arXiv preprint arXiv:2406.17294*, 2024.\n- [50] Jia Li, Edward Beeching, Lewis Tunstall, Ben Lipkin, Roman Soletskyi, Shengyi Huang, Kashif Rasul, Longhui Yu, Albert Q Jiang, Ziju Shen, et al. Numinamath: The largest public dataset in ai4maths with 860k pairs of competition math problems and solutions. *Hugging Face repository*, 13:9, 2024.\n- [51] Yuxuan Tong, Xiwen Zhang, Rui Wang, Ruidong Wu, and Junxian He. Dart-math: Difficulty-aware rejection tuning for mathematical problem-solving. *Advances in Neural Information Processing Systems*, 37:7821–7846, 2024.\n- [52] Chaoqun He, Renjie Luo, Yuzhuo Bai, Shengding Hu, Zhen Leng Thai, Junhao Shen, Jinyi Hu, Xu Han, Yujie Huang, Yuxiang Zhang, et al. Olympiadbench: A challenging benchmark for promoting agi with olympiad-level bilingual multimodal scientific problems. *arXiv preprint arXiv:2402.14008*, 2024.\n- [53] Pan Lu, Hritik Bansal, Tony Xia, Jiacheng Liu, Chunyuan Li, Hannaneh Hajishirzi, Hao Cheng, Kai-Wei Chang, Michel Galley, and Jianfeng Gao. Mathvista: Evaluating mathematical reasoning of foundation models in visual contexts. *arXiv preprint arXiv:2310.02255*, 2023.\n- [54] Renrui Zhang, Dongzhi Jiang, Yichi Zhang, Haokun Lin, Ziyu Guo, Pengshuo Qiu, Aojun Zhou, Pan Lu, Kai-Wei Chang, Yu Qiao, et al. Mathverse: Does your multi-modal llm truly see the diagrams in visual math problems? In *European Conference on Computer Vision*, pages 169–186. Springer, 2024.\n- [55] Ke Wang, Junting Pan, Weikang Shi, Zimu Lu, Houxing Ren, Aojun Zhou, Mingjie Zhan, and Hong-sheng Li. Measuring multimodal mathematical reasoning with math-vision dataset. *Advances in Neural Information Processing Systems*, 37:95095–95169, 2024.\n- [56] Jun Wang, Meng Fang, Ziyu Wan, Muning Wen, Jiachen Zhu, Anjie Liu, Ziqin Gong, Yan Song, Lei Chen, Lionel M Ni, et al. Openr: An open source framework for advanced reasoning with large language models. *arXiv preprint arXiv:2410.09671*, 2024.\n- [57] Shuai Peng, Di Fu, Liangcai Gao, Xiuqin Zhong, Hongguang Fu, and Zhi Tang. Multimath: Bridging visual and mathematical reasoning for large language models. *arXiv preprint arXiv:2409.00147*, 2024.\n- [58] Lei Li, Yuqi Wang, Runxin Xu, Peiyi Wang, Xiachong Feng, Lingpeng Kong, and Qi Liu. Multimodal arxiv: A dataset for improving scientific comprehension of large vision-language models. *arXiv preprint arXiv:2403.00231*, 2024.\n- [59] Wenwen Zhuang, Xin Huang, Xiantao Zhang, and Jin Zeng. Math-puma: Progressive upward multimodal alignment to enhance mathematical reasoning. In *Proceedings of the AAAI Conference on Artificial Intelligence*, volume 39, pages 26183–26191, 2025.- [60] Wenqi Zhang, Zhenglin Cheng, Yuanyu He, Mengna Wang, Yongliang Shen, Zeqi Tan, Guiyang Hou, Mingqian He, Yanna Ma, Weiming Lu, et al. Multimodal self-instruct: Synthetic abstract image and visual reasoning instruction using language model. *arXiv preprint arXiv:2407.07053*, 2024.\n- [61] Erfei Cui, Yinan He, Zheng Ma, Zhe Chen, Hao Tian, Weiyun Wang, Kunchang Li, Yi Wang, Wenhai Wang, Xizhou Zhu, Lewei Lu, Tong Lu, Yali Wang, Limin Wang, Yu Qiao, and Jifeng Dai. Sharegpt-4o: Comprehensive multimodal annotations with gpt-4o, 2024.\n- [62] Cyrile Delestre Tom Agonnoude, 2024.\n- [63] Aida Amini, Saadia Gabriel, Peter Lin, Rik Koncel-Kedziorski, Yejin Choi, and Hannaneh Hajishirzi. Mathqa: Towards interpretable math word problem solving with operation-based formalisms. *arXiv preprint arXiv:1905.13319*, 2019.\n- [64] PawanKrd. math-gpt-4o-200k. *Hugging Face repository*, 2024.\n- [65] Xiang Yue, Xingwei Qu, Ge Zhang, Yao Fu, Wenhao Huang, Huan Sun, Yu Su, and Wenhui Chen. Mammoth: Building math generalist models through hybrid instruction tuning. *arXiv preprint arXiv:2309.05653*, 2023.## Appendix\n\n### A Policy Model training data\n\nTable 3 summarizes the datasets and sample counts used to train the policy model.\n\nTable 3: Data sources and sample counts used for policy model training.\n\n&lt;table border=\"1\">&lt;thead>&lt;tr>&lt;th>Dataset&lt;/th>&lt;th>Sample Count&lt;/th>&lt;/tr>&lt;/thead>&lt;tbody>&lt;tr>&lt;td>R-CoT [47]&lt;/td>&lt;td>201,781&lt;/td>&lt;/tr>&lt;tr>&lt;td>MAVIS [48]&lt;/td>&lt;td>29,551&lt;/td>&lt;/tr>&lt;tr>&lt;td>multimath-300k [57]&lt;/td>&lt;td>224,747&lt;/td>&lt;/tr>&lt;tr>&lt;td>Multimodal ArXiv [58]&lt;/td>&lt;td>99,772&lt;/td>&lt;/tr>&lt;tr>&lt;td>MathV360K [49]&lt;/td>&lt;td>338,721&lt;/td>&lt;/tr>&lt;tr>&lt;td>Math-PUMA [59]&lt;/td>&lt;td>1,111,939&lt;/td>&lt;/tr>&lt;tr>&lt;td>Multi-modal-Self-instruct [60]&lt;/td>&lt;td>64,807&lt;/td>&lt;/tr>&lt;tr>&lt;td>MMPR [13]&lt;/td>&lt;td>1,055,796&lt;/td>&lt;/tr>&lt;tr>&lt;td>ShareGPT-4o [61]&lt;/td>&lt;td>57,289&lt;/td>&lt;/tr>&lt;tr>&lt;td>table-vqa [62]&lt;/td>&lt;td>80,054&lt;/td>&lt;/tr>&lt;tr>&lt;td>MathQA [63]&lt;/td>&lt;td>27,923&lt;/td>&lt;/tr>&lt;tr>&lt;td>GSM8K [19]&lt;/td>&lt;td>7,413&lt;/td>&lt;/tr>&lt;tr>&lt;td>DART-Math [51]&lt;/td>&lt;td>574,305&lt;/td>&lt;/tr>&lt;tr>&lt;td>math-gpt-4o-200k [64]&lt;/td>&lt;td>196,032&lt;/td>&lt;/tr>&lt;tr>&lt;td>NuminaMath-CoT [50]&lt;/td>&lt;td>807,883&lt;/td>&lt;/tr>&lt;tr>&lt;td>MathInstruct [65]&lt;/td>&lt;td>257,755&lt;/td>&lt;/tr>&lt;tr>&lt;td>&lt;b>Total&lt;/b>&lt;/td>&lt;td>&lt;b>5,135,768&lt;/b>&lt;/td>&lt;/tr>&lt;/tbody>&lt;/table>\n\n### B Prompt template for data cleaning\n\nThe prompt template used for data cleaning is shown below. Before generating logical steps and the final answer, the language model is first instructed to explicitly identify the key knowledge points involved in the problem, along with brief explanations. This two-stage prompting strategy enhances the model’s understanding of the question prior to solution restructuring.\n\nUsing the information provided, identify and summarize the key knowledge points required to solve the problem and rewrite the original answer with a detailed reasoning process based on the input answer.\n\nProvide a clear explanation of each knowledge point by stating its name followed by a colon (:), and then presenting the detailed Explanation on the same line.\n\nWhen explaining the knowledge point, DO NOT reference or describe the original question, answer, or answer details. Focus solely on explaining the knowledge points.\n\nBesides, rewrite the original answer to include detailed reasoning and answer. Do not change the final answer and always refer to the input answer.\n\nOutput Format:\n\nIn order to answer this question, we first need to have the following prior knowledge:\n\n{{Substitute with name of knowledge point 1}}: {{Substitute with Explanation of knowledge point 1}},  \n{{Substitute with name of knowledge point 2}}: {{Substitute with Explanation of knowledge point 2}},...\n\nWe answer this based on prior knowledge as follows:\n\nSolution: Refined answer with detailed reasoning. Use Step 1, Step 2 to divide the steps. Remember do not change the final answer and always refer to the input answer.\n\nAnswer: The Final Answer is {{Substitute with final answer}}.\n\nInput Information:\n\nQuestion: {question}\n\nAnswer: {answer}\n\n## C Aggregation function definitions\n\nIn the BoN inference setup, each reasoning path is assigned a vector of step-level scores predicted by the PRM. To compare and rank these paths, we apply an aggregation function to compress each score vector into a single scalar value, following the design considerations discussed in [40]. The following aggregation strategies are used in our experiments:\n\n- • Min: Computes the minimum of all step scores:\n\n$$\\text{score}(r_j) = \\min\\{p_1^{(j)}, p_2^{(j)}, \\dots, p_{T_j}^{(j)}\\}$$\n\n- • Max: Computes the maximum of all step scores:\n\n$$\\text{score}(r_j) = \\max\\{p_1^{(j)}, p_2^{(j)}, \\dots, p_{T_j}^{(j)}\\}$$\n\n- • Average: Computes the arithmetic mean of all step scores:\n\n$$\\text{score}(r_j) = \\frac{1}{T_j} \\sum_{i=1}^{T_j} p_i^{(j)}$$\n\n- • SumLogPr: Computes the sum of log-probabilities of all step scores:\n\n$$\\text{score}(r_j) = \\sum_{i=1}^{T_j} \\log p_i^{(j)} = \\log \\prod_{i=1}^{T_j} p_i^{(j)}$$\n\n- • SumLogOdds: Computes the sum of log-odds of all step scores:\n\n$$\\text{score}(r_j) = \\sum_{i=1}^{T_j} \\log \\frac{p_i^{(j)}}{1 - p_i^{(j)}}$$\n\n- • MeanOdds: Computes the mean of odds-transformed step scores:\n\n$$\\text{score}(r_j) = \\frac{1}{T_j} \\sum_{i=1}^{T_j} \\frac{p_i^{(j)}}{1 - p_i^{(j)}}$$\n\nHere,  $r_j$  denotes the  $j$ -th reasoning path consisting of  $T_j$  steps, and  $p_i^{(j)} \\in (0, 1)$  is the predicted correctness probability of the  $i$ -th step in that path.## D Full evaluation results\n\n### D.1 MM-Policy\n\nTable 4: Performance comparison of various aggregators on various benchmarks for MM-Policy. Top performer is in **bold**.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Benchmark&lt;/th>\n&lt;th>Random&lt;/th>\n&lt;th>Min&lt;/th>\n&lt;th>Average&lt;/th>\n&lt;th>Max&lt;/th>\n&lt;th>SumLogPr&lt;/th>\n&lt;th>SumLogOdds&lt;/th>\n&lt;th>MeanOdds&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>MM-K12&lt;/td>\n&lt;td>33.9&lt;/td>\n&lt;td>37.4&lt;/td>\n&lt;td>43.0&lt;/td>\n&lt;td>&lt;b>43.4&lt;/b>&lt;/td>\n&lt;td>42.0&lt;/td>\n&lt;td>43.2&lt;/td>\n&lt;td>42.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>OlympiadBench&lt;/td>\n&lt;td>15.4&lt;/td>\n&lt;td>23.3&lt;/td>\n&lt;td>20.0&lt;/td>\n&lt;td>&lt;b>24.7&lt;/b>&lt;/td>\n&lt;td>22.7&lt;/td>\n&lt;td>24.0&lt;/td>\n&lt;td>24.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MathVista&lt;/td>\n&lt;td>62.9&lt;/td>\n&lt;td>66.0&lt;/td>\n&lt;td>67.2&lt;/td>\n&lt;td>&lt;b>67.7&lt;/b>&lt;/td>\n&lt;td>66.4&lt;/td>\n&lt;td>&lt;b>67.7&lt;/b>&lt;/td>\n&lt;td>67.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MathVerse&lt;/td>\n&lt;td>43.0&lt;/td>\n&lt;td>46.0&lt;/td>\n&lt;td>48.0&lt;/td>\n&lt;td>46.1&lt;/td>\n&lt;td>47.3&lt;/td>\n&lt;td>&lt;b>48.0&lt;/b>&lt;/td>\n&lt;td>46.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MathVision&lt;/td>\n&lt;td>21.7&lt;/td>\n&lt;td>25.8&lt;/td>\n&lt;td>26.7&lt;/td>\n&lt;td>26.9&lt;/td>\n&lt;td>25.4&lt;/td>\n&lt;td>26.3&lt;/td>\n&lt;td>&lt;b>27.1&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n### D.2 InternVL-8B\n\nTable 5: Performance comparison of various aggregators on various benchmarks for InternVL-8B. Top performer is in **bold**.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Benchmark&lt;/th>\n&lt;th>Random&lt;/th>\n&lt;th>Min&lt;/th>\n&lt;th>Average&lt;/th>\n&lt;th>Max&lt;/th>\n&lt;th>SumLogPr&lt;/th>\n&lt;th>SumLogOdds&lt;/th>\n&lt;th>MeanOdds&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>MM-K12&lt;/td>\n&lt;td>27.0&lt;/td>\n&lt;td>34.8&lt;/td>\n&lt;td>36.0&lt;/td>\n&lt;td>35.8&lt;/td>\n&lt;td>31.2&lt;/td>\n&lt;td>34.2&lt;/td>\n&lt;td>&lt;b>37.8&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>OlympiadBench&lt;/td>\n&lt;td>5.2&lt;/td>\n&lt;td>2.7&lt;/td>\n&lt;td>15.3&lt;/td>\n&lt;td>&lt;b>16.7&lt;/b>&lt;/td>\n&lt;td>2.0&lt;/td>\n&lt;td>1.3&lt;/td>\n&lt;td>15.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MathVista&lt;/td>\n&lt;td>56.4&lt;/td>\n&lt;td>63.4&lt;/td>\n&lt;td>62.8&lt;/td>\n&lt;td>62.6&lt;/td>\n&lt;td>61.0&lt;/td>\n&lt;td>62.0&lt;/td>\n&lt;td>&lt;b>63.5&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MathVerse&lt;/td>\n&lt;td>36.3&lt;/td>\n&lt;td>41.8&lt;/td>\n&lt;td>&lt;b>42.8&lt;/b>&lt;/td>\n&lt;td>41.1&lt;/td>\n&lt;td>42.0&lt;/td>\n&lt;td>42.8&lt;/td>\n&lt;td>42.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MathVision&lt;/td>\n&lt;td>10.0&lt;/td>\n&lt;td>6.1&lt;/td>\n&lt;td>18.4&lt;/td>\n&lt;td>&lt;b>20.6&lt;/b>&lt;/td>\n&lt;td>3.8&lt;/td>\n&lt;td>4.8&lt;/td>\n&lt;td>19.4&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n### D.3 InternVL-26B\n\nTable 6: Performance comparison of various aggregators on various benchmarks for InternVL-26B. Top performer is in **bold**.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Benchmark&lt;/th>\n&lt;th>Random&lt;/th>\n&lt;th>Min&lt;/th>\n&lt;th>Average&lt;/th>\n&lt;th>Max&lt;/th>\n&lt;th>SumLogPr&lt;/th>\n&lt;th>SumLogOdds&lt;/th>\n&lt;th>MeanOdds&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>MM-K12&lt;/td>\n&lt;td>28.0&lt;/td>\n&lt;td>&lt;b>38.0&lt;/b>&lt;/td>\n&lt;td>37.2&lt;/td>\n&lt;td>35.4&lt;/td>\n&lt;td>32.0&lt;/td>\n&lt;td>33.0&lt;/td>\n&lt;td>&lt;b>38.0&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>OlympiadBench&lt;/td>\n&lt;td>14.5&lt;/td>\n&lt;td>16.0&lt;/td>\n&lt;td>23.3&lt;/td>\n&lt;td>22.0&lt;/td>\n&lt;td>16.7&lt;/td>\n&lt;td>16.7&lt;/td>\n&lt;td>24.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MathVista&lt;/td>\n&lt;td>60.0&lt;/td>\n&lt;td>63.9&lt;/td>\n&lt;td>&lt;b>64.6&lt;/b>&lt;/td>\n&lt;td>64.4&lt;/td>\n&lt;td>62.8&lt;/td>\n&lt;td>64.2&lt;/td>\n&lt;td>64.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MathVerse&lt;/td>\n&lt;td>37.8&lt;/td>\n&lt;td>42.0&lt;/td>\n&lt;td>44.2&lt;/td>\n&lt;td>&lt;b>44.3&lt;/b>&lt;/td>\n&lt;td>40.1&lt;/td>\n&lt;td>41.5&lt;/td>\n&lt;td>44.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MathVision&lt;/td>\n&lt;td>20.8&lt;/td>\n&lt;td>23.3&lt;/td>\n&lt;td>24.1&lt;/td>\n&lt;td>24.9&lt;/td>\n&lt;td>20.6&lt;/td>\n&lt;td>22.0&lt;/td>\n&lt;td>&lt;b>25.6&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n### D.4 InternVL-38B\n\nTable 7: Performance comparison of various aggregators on various benchmarks for InternVL-38B. Top performer is in **bold**.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Benchmark&lt;/th>\n&lt;th>Random&lt;/th>\n&lt;th>Min&lt;/th>\n&lt;th>Average&lt;/th>\n&lt;th>Max&lt;/th>\n&lt;th>SumLogPr&lt;/th>\n&lt;th>SumLogOdds&lt;/th>\n&lt;th>MeanOdds&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>MM-K12&lt;/td>\n&lt;td>40.3&lt;/td>\n&lt;td>46.8&lt;/td>\n&lt;td>51.0&lt;/td>\n&lt;td>49.8&lt;/td>\n&lt;td>42.8&lt;/td>\n&lt;td>46.6&lt;/td>\n&lt;td>&lt;b>52.4&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>OlympiadBench&lt;/td>\n&lt;td>29.6&lt;/td>\n&lt;td>29.3&lt;/td>\n&lt;td>34.0&lt;/td>\n&lt;td>&lt;b>34.7&lt;/b>&lt;/td>\n&lt;td>28.0&lt;/td>\n&lt;td>30.0&lt;/td>\n&lt;td>32.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MathVista&lt;/td>\n&lt;td>68.3&lt;/td>\n&lt;td>70.5&lt;/td>\n&lt;td>&lt;b>71.1&lt;/b>&lt;/td>\n&lt;td>70.5&lt;/td>\n&lt;td>69.2&lt;/td>\n&lt;td>70.1&lt;/td>\n&lt;td>&lt;b>71.1&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MathVerse&lt;/td>\n&lt;td>47.9&lt;/td>\n&lt;td>50.4&lt;/td>\n&lt;td>51.9&lt;/td>\n&lt;td>51.1&lt;/td>\n&lt;td>51.1&lt;/td>\n&lt;td>52.7&lt;/td>\n&lt;td>&lt;b>52.6&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MathVision&lt;/td>\n&lt;td>29.7&lt;/td>\n&lt;td>29.1&lt;/td>\n&lt;td>32.6&lt;/td>\n&lt;td>&lt;b>33.6&lt;/b>&lt;/td>\n&lt;td>30.6&lt;/td>\n&lt;td>31.3&lt;/td>\n&lt;td>33.0&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>## D.5 InternVL-78B\n\nTable 8: Performance comparison of various aggregators on various benchmarks for InternVL-78B. Top performer is in **bold**.\n\n&lt;table border=\"1\">&lt;thead>&lt;tr>&lt;th>Benchmark&lt;/th>&lt;th>Random&lt;/th>&lt;th>Min&lt;/th>&lt;th>Average&lt;/th>&lt;th>Max&lt;/th>&lt;th>SumLogPr&lt;/th>&lt;th>SumLogOdds&lt;/th>&lt;th>MeanOdds&lt;/th>&lt;/tr>&lt;/thead>&lt;tbody>&lt;tr>&lt;td>MM-K12&lt;/td>&lt;td>42.2&lt;/td>&lt;td>46.2&lt;/td>&lt;td>47.2&lt;/td>&lt;td>47.2&lt;/td>&lt;td>45.0&lt;/td>&lt;td>46.8&lt;/td>&lt;td>&lt;b>48.8&lt;/b>&lt;/td>&lt;/tr>&lt;tr>&lt;td>OlympiadBench&lt;/td>&lt;td>31.0&lt;/td>&lt;td>33.3&lt;/td>&lt;td>35.3&lt;/td>&lt;td>&lt;b>34.7&lt;/b>&lt;/td>&lt;td>33.3&lt;/td>&lt;td>&lt;b>34.7&lt;/b>&lt;/td>&lt;td>&lt;b>34.7&lt;/b>&lt;/td>&lt;/tr>&lt;tr>&lt;td>MathVista&lt;/td>&lt;td>69.5&lt;/td>&lt;td>71.7&lt;/td>&lt;td>73.4&lt;/td>&lt;td>72.4&lt;/td>&lt;td>&lt;b>73.9&lt;/b>&lt;/td>&lt;td>73.6&lt;/td>&lt;td>73.2&lt;/td>&lt;/tr>&lt;tr>&lt;td>MathVerse&lt;/td>&lt;td>50.2&lt;/td>&lt;td>53.4&lt;/td>&lt;td>55.0&lt;/td>&lt;td>54.2&lt;/td>&lt;td>54.3&lt;/td>&lt;td>&lt;b>55.1&lt;/b>&lt;/td>&lt;td>54.5&lt;/td>&lt;/tr>&lt;tr>&lt;td>MathVision&lt;/td>&lt;td>31.5&lt;/td>&lt;td>30.1&lt;/td>&lt;td>33.5&lt;/td>&lt;td>&lt;b>33.6&lt;/b>&lt;/td>&lt;td>31.8&lt;/td>&lt;td>32.4&lt;/td>&lt;td>33.3&lt;/td>&lt;/tr>&lt;/tbody>&lt;/table>\n\n## E Limitations\n\nWhile our proposed framework demonstrates strong performance and generalization across multiple benchmarks, it also has several limitations: (1) Due to computational constraints, we conduct training only on the InternVL series with 8B parameters, without exploring larger models or architectures from other model families. This restricts our ability to fully assess how PRM training behavior scales with model size or generalizes across different backbones. (2) The seed data used for process supervision generation is limited in diversity, as it consists solely of K-12 math problems. As a result, the PRM may be less exposed to advanced mathematical domains or visual formats beyond the scope of standard educational settings. We leave broader model coverage and more diverse seed data construction as promising directions for future work.\n",
      "numLines": 759,
      "startLine": 1,
      "totalLines": 759
    }
  },
  "sourceToolAssistantUUID": "19b5f523-a18f-4eaf-9ac2-0427b5461736",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-27 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "9590c609-7744-4015-826d-3a92cbde2fca",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze MM-PRM paper for research methodology",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d"
}
```

---

### Assistant

_source line 34 · 2026-05-27T16:09:22.127Z_

<details><summary>Logged reasoning block</summary>

```text
I now have the full paper content. Let me also check if there's a GitHub repo to understand the project better and see if there are any additional details.

Now let me analyze the paper carefully and construct the JSON output.

Let me think through each dimension:

**Problem Identification:**
The gap they identified: PRMs existed for text-only math reasoning (PRM800K, MathShepherd, OmegaPRM), but nobody had built a scalable process reward model for *multimodal* mathematical reasoning. The key bottleneck was: (1) no step-level supervision data existed for multimodal math, and (2) generating such data in the multimodal setting was inefficient. 

They discovered this gap by noticing that multimodal language models struggle with multi-step reasoning—they produce broken logical chains and incorrect intermediate steps that sometimes still lead to correct final answers, creating high false-positive rates. While PRMs had proven effective for text-only math, the multimodal domain lacked both the necessary data and the methodological framework.

**Key Insight:**
The key insight was that MCTS-based process supervision (OmegaPRM), originally developed for text-only math, could be adapted to multimodal settings by maintaining full visual context throughout the tree search process. Combined with a small but carefully curated seed dataset (10K problems) and soft labeling, this could generate massive step-level annotations (700K+) that generalize across models and benchmarks.

**Innovation Type:**
The main innovation is adapting text-only PRM techniques to the multimodal domain, combined with scaling from 10K seed problems to 700K annotations and systematic analysis of training dynamics like soft versus hard labels and learning rates.

**Method Summary:**
The approach involves fine-tuning a multimodal policy model on a large corpus of math examples with structured reasoning chains, then curating a smaller high-quality dataset and using an adapted MCTS pipeline to generate extensive step-level supervision data.

**Training and Evaluation:**
They train the PRM using soft continuous labels from Monte Carlo rollouts with a conservative learning rate, then evaluate performance through best-of-N sampling with different aggregation strategies.

**Strengths:**
The work demonstrates strong results across multiple benchmarks and model sizes, with an entirely automated pipeline requiring no human annotation. Notably, PRMs trained on smaller models and K-12 data transfer effectively to larger models and more challenging olympiad-level problems, and the authors released both code and datasets.

**Gaps:**
The approach was only explored with one model family at a specific scale, and the seed data comes exclusively from K-12 mathematics, which may limit applicability to more specialized mathematical domains.

**Open questions:**
Whether the PRM can drive reinforcement learning beyond just selecting best outputs, how performance scales with different amounts and types of seed data, and whether this multimodal process supervision works for reasoning tasks outside mathematics.

**Key components:**
The approach builds on the OmegaPRM framework with InternVL2.5 models, uses Qwen2.5 for data cleaning, structures reasoning with step-level tags, and evaluates through best-of-N with various aggregation methods.

**Relevance:**
This directly tackles multimodal mathematical reasoning with a scalable, automated process supervision method that shows visual context significantly improves step-level verification.

Constructing the final JSON output...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9590c609-7744-4015-826d-3a92cbde2fca",
  "isSidechain": false,
  "requestId": "req_011CbTN2qFxF3k6kF897LJ17",
  "type": "assistant",
  "uuid": "74550ca3-9284-4453-be25-e56a0d8aef7e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xv3tygnDHkYXjGJ5uJxXPu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22016,
      "cache_read_input_tokens": 16287,
      "output_tokens": 1167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22016,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1167,
          "cache_read_input_tokens": 16287,
          "cache_creation_input_tokens": 22016,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22016
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

_source line 35 · 2026-05-27T16:09:22.129Z_

Now I have the complete paper. Let me also check if there are reviewer comments on OpenReview for any venue submission:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74550ca3-9284-4453-be25-e56a0d8aef7e",
  "isSidechain": false,
  "requestId": "req_011CbTN2qFxF3k6kF897LJ17",
  "type": "assistant",
  "uuid": "5ccadde6-4067-43cd-b490-eadcce7a9cde",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xv3tygnDHkYXjGJ5uJxXPu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22016,
      "cache_read_input_tokens": 16287,
      "output_tokens": 1167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22016,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1167,
          "cache_read_input_tokens": 16287,
          "cache_creation_input_tokens": 22016,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22016
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

_source line 36 · 2026-05-27T16:09:23.352Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DsBm3MzgFRMxvL3ZpS1x1z`</summary>

```json
{
  "url": "https://openreview.net/search?term=MM-PRM+multimodal+process+reward",
  "prompt": "Search for any paper titled \"MM-PRM\" or related to \"multimodal process reward model\" by Lingxiao Du. If found, provide the forum URL so I can read reviewer comments."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ccadde6-4067-43cd-b490-eadcce7a9cde",
  "isSidechain": false,
  "requestId": "req_011CbTN2qFxF3k6kF897LJ17",
  "type": "assistant",
  "uuid": "7fe87db9-ea58-496b-b58a-c2f8b718dfdf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xv3tygnDHkYXjGJ5uJxXPu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22016,
      "cache_read_input_tokens": 16287,
      "output_tokens": 1167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22016,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1167,
          "cache_read_input_tokens": 16287,
          "cache_creation_input_tokens": 22016,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22016
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

_source line 37 · 2026-05-27T16:09:34.068Z_

<details><summary>↩ Tool result · `toolu_01DsBm3MzgFRMxvL3ZpS1x1z`</summary>

```text
I appreciate your interest in finding that research paper, but I'm unable to help based on the provided content. The webpage excerpt you shared only contains OpenReview's navigation menu and footer information—it doesn't include any search results or paper listings.

To locate the "MM-PRM" paper or work by Lingxiao Du on multimodal process reward models, you would need to:

1. Visit OpenReview.net directly
2. Use their search functionality to look for the paper title or author name
3. Browse relevant venue pages where such research might be posted

The current content doesn't contain the specific paper information you're seeking.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7fe87db9-ea58-496b-b58a-c2f8b718dfdf",
  "isSidechain": false,
  "promptId": "de34c998-fd7f-4a40-bbbf-9dd4b01a6eef",
  "type": "user",
  "uuid": "314fb625-e9bf-4b83-8327-c3f042f95711",
  "toolUseResult": {
    "bytes": 62286,
    "code": 200,
    "codeText": "OK",
    "result": "I appreciate your interest in finding that research paper, but I'm unable to help based on the provided content. The webpage excerpt you shared only contains OpenReview's navigation menu and footer information—it doesn't include any search results or paper listings.\n\nTo locate the \"MM-PRM\" paper or work by Lingxiao Du on multimodal process reward models, you would need to:\n\n1. Visit OpenReview.net directly\n2. Use their search functionality to look for the paper title or author name\n3. Browse relevant venue pages where such research might be posted\n\nThe current content doesn't contain the specific paper information you're seeking.",
    "durationMs": 10711,
    "url": "https://openreview.net/search?term=MM-PRM+multimodal+process+reward"
  },
  "sourceToolAssistantUUID": "7fe87db9-ea58-496b-b58a-c2f8b718dfdf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 38 · 2026-05-27T16:09:34.074Z_

```json
{
  "parentUuid": "314fb625-e9bf-4b83-8327-c3f042f95711",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "a4ce86c9-5f5a-42ad-9bdd-cb362c73c92d",
  "timestamp": "2026-05-27T16:09:34.074Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 39 · 2026-05-27T16:09:37.948Z_

<details><summary>Logged reasoning block</summary>

```text
No reviewer comments available on OpenReview. This is an arXiv paper (not peer-reviewed at a venue yet as of the paper date). Let me now compose the final analysis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4ce86c9-5f5a-42ad-9bdd-cb362c73c92d",
  "isSidechain": false,
  "requestId": "req_011CbTN67Dj2HWLBojBELhC3",
  "type": "assistant",
  "uuid": "2369fd43-8d2a-410d-844d-73e5d3458e6c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015GPNP58oFkuYytv4bw432N",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 38303,
      "output_tokens": 1925,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1413,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1925,
          "cache_read_input_tokens": 38303,
          "cache_creation_input_tokens": 1413,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1413
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

_source line 40 · 2026-05-27T16:10:27.047Z_

No reviewer comments found — this is an arXiv preprint without a confirmed venue submission on OpenReview. Now I have everything I need. Here's my deep analysis:

```json
{
  "title": "MM-PRM: Enhancing Multimodal Mathematical Reasoning with Scalable Step-Level Supervision",
  "venue": "arXiv 2025 (preprint, not yet peer-reviewed at a top venue)",

  "problem_identification": "Process reward models (PRMs) had proven highly effective for text-only math reasoning (PRM800K, MathShepherd, OmegaPRM), but the multimodal domain had zero infrastructure for step-level supervision — no datasets, no annotation pipelines, no trained PRMs. The authors identified this gap by observing that MLLMs produce 'false-positive' solutions (wrong intermediate steps that accidentally reach correct answers), a failure mode that outcome-only reward models cannot detect. The insight that multimodal math has fundamentally the same step-verification need as text-only math, but lacks all the tooling, is what defined the contribution space.",

  "key_insight": "MCTS-based process supervision, originally designed for text-only math (OmegaPRM), can be adapted to multimodal settings by maintaining full visual context throughout the tree search — and a surprisingly small seed dataset (10K problems) is sufficient to generate 700K+ step-level annotations that generalize across both unseen benchmarks and models 10x larger than the one that generated the data. The second crucial insight is that soft labels (continuous MC scores) dramatically outperform hard binary labels because they preserve information about problem difficulty and step criticality that binary thresholding destroys.",

  "innovation_type": "cross_domain",

  "method_summary": "The framework has three stages. (1) Policy Model Construction: fine-tune InternVL2.5-8B on 5.1M curated math examples with CoT formatting enforced via Qwen2.5-72B-Instruct restructuring, producing MM-Policy with structured &lt;step>/&lt;answer> outputs. (2) Process Supervision Data Generation: curate MM-K12, a 10K-problem multimodal math dataset (5K fill-in-blank + 5K multiple-choice, K-12 level, each verified to have a unique checkable answer); adapt OmegaPRM's MCTS pipeline to maintain full multimodal context during tree search, using binary search to efficiently pinpoint the first erroneous step; generate 747K step-level annotations with continuous MC scores. (3) PRM Training: initialize from MM-Policy, insert &lt;prm> tokens after each step, train a Yes/No classifier head with cross-entropy loss against soft MC labels at learning rate 4e-6 (10x lower than SFT). At inference, generate N=16 candidate paths and select via Best-of-N with aggregation functions (MeanOdds performs best overall).",

  "what_makes_it_good": "Three things elevate this work beyond a straightforward adaptation. First, the generalization results are striking: a PRM trained on 8B-model data from K-12 problems improves a 78B model on olympiad-level benchmarks (+3.69% OlympiadBench, +3.72% MathVista), proving the reward signal is not model- or difficulty-specific. Second, the 70x amplification ratio (10K seeds → 700K annotations) demonstrates genuine scalability without human labeling. Third, the systematic ablations on soft vs. hard labels (+8.6% absolute on Average aggregation), learning rate sensitivity, and path diversity provide actionable training recipes that the community can immediately reuse, transforming a methods paper into a practical handbook.",

  "limitations_acknowledged": "The authors explicitly note two gaps: (1) PRM training was only conducted at 8B scale on the InternVL family — they did not train larger PRMs or test on architectures beyond InternVL; (2) seed data is limited to K-12 math, potentially limiting coverage of advanced mathematical domains or unusual visual formats.",

  "open_questions": [
    "Can this PRM be used as a reward signal for RL training (e.g., PPO/GRPO) rather than just Best-of-N selection? The concurrent work URSA explores this direction but with different PRM construction — integrating the two approaches could yield compounding gains.",
    "How does PRM quality scale with seed data diversity? The 10K K-12 seeds already generalize to olympiad-level problems — would adding even 1K competition-level seeds disproportionately improve hard-problem performance, or are the returns diminishing?",
    "The MCTS pipeline maintains visual context but treats images as fixed inputs throughout the tree. Could step-level visual re-grounding (re-attending to different image regions at each reasoning step) produce richer supervision signals, especially for geometry and diagram-heavy problems?"
  ],

  "building_blocks": [
    "OmegaPRM MCTS framework (divide-and-conquer binary search for first-error identification)",
    "InternVL2.5 model family (8B through 78B, used as both policy and PRM backbone)",
    "Qwen2.5-72B-Instruct (for automated CoT restructuring during data cleaning)",
    "MM-K12 dataset (10K seed + 500 test, curated multimodal math with verifiable answers)",
    "Structured CoT formatting with &lt;step>&lt;/step> and &lt;answer>&lt;/answer> tags",
    "Best-of-N evaluation protocol with 6 aggregation functions (MeanOdds, SumLogOdds, etc.)",
    "Soft label training strategy (continuous MC scores as supervision targets)",
    "Special &lt;prm> token insertion for step-level classification",
    "15+ public math datasets aggregated for policy training (R-CoT, MAVIS, MathV360K, NuminaMath, DART-Math, etc.)"
  ],

  "reviewer_feedback_summary": null,

  "relevance_to_seed": "This paper directly addresses the core challenge of our research area — integrating visual, symbolic, and textual understanding for mathematical reasoning — by showing that process-level supervision is the missing ingredient for multimodal math. The key transferable lesson is architectural: you don't need multimodal-specific innovations in the reward model itself; you need a scalable pipeline that preserves visual context during supervision generation. The soft-label finding and the cross-model generalization result (small-model PRM improving large models) are immediately actionable for anyone building multimodal reasoning systems."
}
```

---

### Meta-Analysis: What Can We Learn About the *Craft* of This Research?

**1. The "Infrastructure Transfer" Pattern.** The strongest move in this paper is recognizing that a proven text-only pipeline (OmegaPRM) was blocked from multimodal adoption not by any fundamental incompatibility, but by missing infrastructure — no curated seed dataset, no structured output format, no multimodal-aware tree search. The research contribution is less about algorithmic novelty and more about *building the missing plumbing* and proving it works. This is a high-impact, underappreciated research pattern: find a technique that works in domain A, identify the concrete engineering gaps preventing its use in domain B, and fill them systematically.

**2. The "Small Seed, Large Harvest" Scaling Story.** The 10K → 700K amplification is the paper's most compelling number. It works because the authors invested heavily in seed quality (verified unique answers, meaningful visual input, balanced question types) rather than seed quantity. The lesson: when building data generation pipelines, constraint quality at the seed level is more valuable than scale.

**3. Ablations as First-Class Contributions.** The soft-vs-hard label comparison (+8.6% absolute) and learning rate analysis are arguably more useful to the community than the headline benchmark numbers. They turn a "we built X and it works" paper into a "here's how to build X correctly" paper — which is why it likely received attention despite being a relatively straightforward adaptation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2369fd43-8d2a-410d-844d-73e5d3458e6c",
  "isSidechain": false,
  "requestId": "req_011CbTN67Dj2HWLBojBELhC3",
  "type": "assistant",
  "uuid": "18461290-0fd2-4adc-b931-b1e9ff73f254",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015GPNP58oFkuYytv4bw432N",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 38303,
      "output_tokens": 1925,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1413,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1925,
          "cache_read_input_tokens": 38303,
          "cache_creation_input_tokens": 1413,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1413
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

_source line 41_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-27 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "18461290-0fd2-4adc-b931-b1e9ff73f254",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze MM-PRM paper for research methodology",
  "sessionId": "0243be30-7aad-4e4c-9062-bffffcde4a0d"
}
```

---
