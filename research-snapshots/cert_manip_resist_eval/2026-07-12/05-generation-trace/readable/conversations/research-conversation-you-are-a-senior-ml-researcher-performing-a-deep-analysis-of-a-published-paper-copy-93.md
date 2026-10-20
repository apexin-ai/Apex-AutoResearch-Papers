# Research conversation: You are a senior ML researcher performing a deep analysis of a published paper. **Today's date: 2026-05-27 (UTC).** ## Y

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 52
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/85dae6a1-bcc0-4c8f-97a6-84608d21f8c6.jsonl`
- **Structured JSON:** [`d192fdced38b47bac308.json`](../../sessions/d1/d192fdced38b47bac308.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T16:03:39.517Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T16:03:39.517Z",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "content": "You are a senior ML researcher performing a deep analysis of a published paper.\n\n**Today's date: 2026-05-27 (UTC).**\n\n## Your goal\n\nAnalyze this paper NOT just for what it does, but for **HOW it innovates** — what can we learn from its approach to doing research? What made this paper good enough for a top venue?\n\n## Research context\n\nWe are generating ideas in the area of: **Multi-Modal Mathematical Reasoning — Integrating Visual, Symbolic, and Textual Understanding**\n\n## Paper to analyze\n\n{\n  \"title\": \"MM-Eureka: Exploring the Frontiers of Multimodal Reasoning with Rule-based Reinforcement Learning\",\n  \"authors\": \"Fanqing Meng et al.\",\n  \"venue\": \"arXiv 2025\",\n  \"url\": \"https://arxiv.org/abs/2503.07365\",\n  \"why_important\": \"Successfully reproduces DeepSeek-R1's 'aha moment' in multimodal reasoning; open-source 7B/32B models competitive with InternVL2.5-78B; introduced MMK12 dataset; widely adopted\",\n  \"one_line_summary\": \"Applies rule-based reinforcement learning with the MMK12 dataset and a two-stage training strategy to achieve multimodal math reasoning performance competitive with models 10× larger.\"\n}\n\n## Instructions\n\n1. **Deep read**: Use WebFetch to read this paper's full abstract, introduction, method section, and conclusion on arXiv or OpenReview. If it's on OpenReview, also read the reviewer comments and author responses.\n\n2. **Analyze the innovation structure**: Don't just summarize — dissect HOW the authors arrived at their contribution:\n   - What gap did they identify and HOW did they find it?\n   - What was the key insight that others missed?\n   - How did they formulate the problem differently from prior work?\n   - What existing technique did they adapt/combine/simplify?\n\n3. **Learn from reviewers**: If you can find reviewer comments, extract:\n   - What did reviewers praise most?\n   - What concerns were raised and how were they addressed?\n   - What would have made this paper even stronger?\n\n## Output format\n\nOutput a single JSON object:\n{\n  \"title\": \"Paper title\",\n  \"venue\": \"Where published\",\n  \"problem_identification\": \"What gap/problem did they identify? How did they find it? (2-3 sentences)\",\n  \"key_insight\": \"The core intellectual contribution — the aha moment (1-2 sentences)\",\n  \"innovation_type\": \"new_formulation | new_technique | new_benchmark | simplification | cross_domain | combination | scaling | analysis\",\n  \"method_summary\": \"Technical approach in 3-5 sentences — enough to understand the machinery\",\n  \"what_makes_it_good\": \"Why did this paper get accepted? What would reviewers have liked? (2-3 sentences)\",\n  \"limitations_acknowledged\": \"What gaps did the authors themselves identify? (1-2 sentences)\",\n  \"open_questions\": \"What follow-up questions does this paper raise? What remains unsolved? (2-3 bullet points)\",\n  \"building_blocks\": [\"List of methods/tools/datasets used that could be reused\"],\n  \"reviewer_feedback_summary\": \"If found on OpenReview: key praise and concerns. Otherwise: null\",\n  \"relevance_to_seed\": \"How does this paper relate to our research area? What can we learn from it? (1-2 sentences)\"\n}\n\nBe analytical, not descriptive. We want to learn the CRAFT of doing good research, not just know what this paper did."
}
```

---

### Runtime record

_source line 2 · 2026-05-27T16:03:39.520Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T16:03:39.520Z",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6"
}
```

---

## Round 1

50 recorded events

### User

_source line 3 · 2026-05-27T16:03:39.571Z_

You are a senior ML researcher performing a deep analysis of a published paper.

**Today's date: 2026-05-27 (UTC).**

## Your goal

Analyze this paper NOT just for what it does, but for **HOW it innovates** — what can we learn from its approach to doing research? What made this paper good enough for a top venue?

## Research context

We are generating ideas in the area of: **Multi-Modal Mathematical Reasoning — Integrating Visual, Symbolic, and Textual Understanding**

## Paper to analyze

{
  "title": "MM-Eureka: Exploring the Frontiers of Multimodal Reasoning with Rule-based Reinforcement Learning",
  "authors": "Fanqing Meng et al.",
  "venue": "arXiv 2025",
  "url": "https://arxiv.org/abs/2503.07365",
  "why_important": "Successfully reproduces DeepSeek-R1's 'aha moment' in multimodal reasoning; open-source 7B/32B models competitive with InternVL2.5-78B; introduced MMK12 dataset; widely adopted",
  "one_line_summary": "Applies rule-based reinforcement learning with the MMK12 dataset and a two-stage training strategy to achieve multimodal math reasoning performance competitive with models 10× larger."
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
  "promptId": "6e9b4775-3324-430a-aeff-baabf4898966",
  "type": "user",
  "uuid": "74ffc95d-1dfc-476d-bab8-352053988f4e",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T16:03:39.571Z_

```json
{
  "parentUuid": "74ffc95d-1dfc-476d-bab8-352053988f4e",
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
  "uuid": "ea4c8eb1-a827-44aa-8b5c-3531f419e566",
  "timestamp": "2026-05-27T16:03:39.571Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T16:03:39.571Z_

```json
{
  "parentUuid": "ea4c8eb1-a827-44aa-8b5c-3531f419e566",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "3c4f9b1b-c29a-4c9a-8e19-2b0ff7de4c1d",
  "timestamp": "2026-05-27T16:03:39.571Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
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
  "aiTitle": "Analyze MM-Eureka multimodal reasoning paper",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6"
}
```

---

### Assistant

_source line 7 · 2026-05-27T16:03:43.206Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to do a deep analysis of the paper "MM-Eureka: Exploring the Frontiers of Multimodal Reasoning with Rule-based Reinforcement Learning" (arXiv 2503.07365). Let me fetch the paper content first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c4f9b1b-c29a-4c9a-8e19-2b0ff7de4c1d",
  "isSidechain": false,
  "requestId": "req_011CbTMdyZdf8REUQ71g43Bj",
  "type": "assistant",
  "uuid": "58ce77fa-3657-4d55-8d18-9e79a7ee7a81",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hd5MhYfnh4wTVSJ7PMXjYL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2213,
      "cache_read_input_tokens": 11014,
      "output_tokens": 152,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2213,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 152,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 2213,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2213
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

_source line 8 · 2026-05-27T16:03:43.328Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MdwFYLn8xhZ7YcYiKVr942`</summary>

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
  "parentUuid": "58ce77fa-3657-4d55-8d18-9e79a7ee7a81",
  "isSidechain": false,
  "requestId": "req_011CbTMdyZdf8REUQ71g43Bj",
  "type": "assistant",
  "uuid": "856e6314-c0ff-4342-a245-ca6e7fbfd603",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hd5MhYfnh4wTVSJ7PMXjYL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2213,
      "cache_read_input_tokens": 11014,
      "output_tokens": 152,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2213,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 152,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 2213,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2213
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

_source line 9 · 2026-05-27T16:03:43.349Z_

<details><summary>↩ Tool result · `toolu_01MdwFYLn8xhZ7YcYiKVr942`</summary>

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
  "parentUuid": "856e6314-c0ff-4342-a245-ca6e7fbfd603",
  "isSidechain": false,
  "promptId": "6e9b4775-3324-430a-aeff-baabf4898966",
  "type": "user",
  "uuid": "7b2bba7a-2099-4165-9408-ac9d0b948cc9",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "856e6314-c0ff-4342-a245-ca6e7fbfd603",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-27T16:03:46.827Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me fetch the paper from arXiv. I'll fetch both the abstract page and the HTML version of the paper for more detail.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b2bba7a-2099-4165-9408-ac9d0b948cc9",
  "isSidechain": false,
  "requestId": "req_011CbTMeFnhFbv6UX2yGvLDC",
  "type": "assistant",
  "uuid": "01ec947d-e80a-4cec-aaff-0af0a8a21e39",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011fA6bkiXiAe7QH311gkZbs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 672,
      "cache_read_input_tokens": 13227,
      "output_tokens": 343,
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
          "input_tokens": 3,
          "output_tokens": 343,
          "cache_read_input_tokens": 13227,
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

_source line 11 · 2026-05-27T16:03:47.357Z_

Let me fetch the paper content from multiple sources to get a comprehensive view.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01ec947d-e80a-4cec-aaff-0af0a8a21e39",
  "isSidechain": false,
  "requestId": "req_011CbTMeFnhFbv6UX2yGvLDC",
  "type": "assistant",
  "uuid": "ec13df97-b97a-4aea-a771-f3c2b8530b08",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011fA6bkiXiAe7QH311gkZbs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 672,
      "cache_read_input_tokens": 13227,
      "output_tokens": 343,
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
          "input_tokens": 3,
          "output_tokens": 343,
          "cache_read_input_tokens": 13227,
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

_source line 12 · 2026-05-27T16:03:48.911Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MKhevB1BVed2SXryH4vnBF`</summary>

```json
{
  "url": "https://arxiv.org/abs/2503.07365",
  "prompt": "Extract the full abstract, author list, and any other metadata visible on this page (submission date, categories, etc.). Return everything verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec13df97-b97a-4aea-a771-f3c2b8530b08",
  "isSidechain": false,
  "requestId": "req_011CbTMeFnhFbv6UX2yGvLDC",
  "type": "assistant",
  "uuid": "0d86be9b-72b5-4ce6-a6b2-8151e2d632ae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011fA6bkiXiAe7QH311gkZbs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 672,
      "cache_read_input_tokens": 13227,
      "output_tokens": 343,
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
          "input_tokens": 3,
          "output_tokens": 343,
          "cache_read_input_tokens": 13227,
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

_source line 13 · 2026-05-27T16:03:51.621Z_

<details><summary>↩ Tool result · `toolu_01X4dxCqXHMcm5pNMza1phpj`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36be79a1-1994-4fd7-98c4-60fa49ccac94",
  "isSidechain": false,
  "promptId": "6e9b4775-3324-430a-aeff-baabf4898966",
  "type": "user",
  "uuid": "07fbef5b-b756-4d60-8356-4554e019898a",
  "toolUseResult": {
    "bytes": 0,
    "code": 404,
    "codeText": "Not Found",
    "result": "The server returned HTTP 404 Not Found.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.",
    "durationMs": 6,
    "url": "https://arxiv.org/html/2503.07365"
  },
  "sourceToolAssistantUUID": "36be79a1-1994-4fd7-98c4-60fa49ccac94",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-27T16:03:51.612Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01X4dxCqXHMcm5pNMza1phpj`</summary>

```json
{
  "url": "https://arxiv.org/html/2503.07365",
  "prompt": "Extract the FULL text of the following sections of this paper, preserving all detail:\n1. Introduction (complete)\n2. Related Work (complete)\n3. Method / Approach section (complete — including all subsections about dataset construction, training strategy, reward design, etc.)\n4. Experiments / Results (complete — including all tables, ablations, and analysis)\n5. Conclusion and Limitations\n\nReturn as much text as possible. Do NOT summarize — I need the full content."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d86be9b-72b5-4ce6-a6b2-8151e2d632ae",
  "isSidechain": false,
  "requestId": "req_011CbTMeFnhFbv6UX2yGvLDC",
  "type": "assistant",
  "uuid": "36be79a1-1994-4fd7-98c4-60fa49ccac94",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011fA6bkiXiAe7QH311gkZbs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 672,
      "cache_read_input_tokens": 13227,
      "output_tokens": 343,
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
          "input_tokens": 3,
          "output_tokens": 343,
          "cache_read_input_tokens": 13227,
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

_source line 15 · 2026-05-27T16:03:54.796Z_

<details><summary>↩ Tool result · `toolu_01MKhevB1BVed2SXryH4vnBF`</summary>

```text
# MM-Eureka Research Paper Metadata

**Title:** MM-Eureka: Exploring the Frontiers of Multimodal Reasoning with Rule-based Reinforcement Learning

**ArXiv ID:** 2503.07365

**Category:** Computer Vision and Pattern Recognition (cs.CV)

**Submission Dates:**
- v1: March 10, 2025
- v2: April 15, 2025 (current version)

**Authors:** Fanqing Meng, Lingxiao Du, Zongkai Liu, Zhixiang Zhou, Quanfeng Lu, Daocheng Fu, Tiancheng Han, Botian Shi, Wenhai Wang, Junjun He, Kaipeng Zhang, Ping Luo, Yu Qiao, Qiaosheng Zhang, Wenqi Shao

**Abstract Summary:**
The work introduces the MMK12 dataset and MM-EUREKA models (7B and 32B parameters). These use "rule-based reinforcement learning on MMK12, utilizing online filtering and two-stage training strategy to enhance training stability." The models demonstrate strong performance in multimodal mathematical reasoning, comparing favorably against InternVL2.5 variants and approaching o1-level capabilities in multidisciplinary tasks.

**License:** CC BY 4.0

**Code/Data Availability:** Open-sourced materials available through GitHub (ModalMinds/MM-EUREKA)

**DOI:** https://doi.org/10.48550/arXiv.2503.07365
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d86be9b-72b5-4ce6-a6b2-8151e2d632ae",
  "isSidechain": false,
  "promptId": "6e9b4775-3324-430a-aeff-baabf4898966",
  "type": "user",
  "uuid": "0b326566-13b1-4c6c-87e5-cab611c4e44d",
  "toolUseResult": {
    "bytes": 48670,
    "code": 200,
    "codeText": "OK",
    "result": "# MM-Eureka Research Paper Metadata\n\n**Title:** MM-Eureka: Exploring the Frontiers of Multimodal Reasoning with Rule-based Reinforcement Learning\n\n**ArXiv ID:** 2503.07365\n\n**Category:** Computer Vision and Pattern Recognition (cs.CV)\n\n**Submission Dates:**\n- v1: March 10, 2025\n- v2: April 15, 2025 (current version)\n\n**Authors:** Fanqing Meng, Lingxiao Du, Zongkai Liu, Zhixiang Zhou, Quanfeng Lu, Daocheng Fu, Tiancheng Han, Botian Shi, Wenhai Wang, Junjun He, Kaipeng Zhang, Ping Luo, Yu Qiao, Qiaosheng Zhang, Wenqi Shao\n\n**Abstract Summary:**\nThe work introduces the MMK12 dataset and MM-EUREKA models (7B and 32B parameters). These use \"rule-based reinforcement learning on MMK12, utilizing online filtering and two-stage training strategy to enhance training stability.\" The models demonstrate strong performance in multimodal mathematical reasoning, comparing favorably against InternVL2.5 variants and approaching o1-level capabilities in multidisciplinary tasks.\n\n**License:** CC BY 4.0\n\n**Code/Data Availability:** Open-sourced materials available through GitHub (ModalMinds/MM-EUREKA)\n\n**DOI:** https://doi.org/10.48550/arXiv.2503.07365",
    "durationMs": 5882,
    "url": "https://arxiv.org/abs/2503.07365"
  },
  "sourceToolAssistantUUID": "0d86be9b-72b5-4ce6-a6b2-8151e2d632ae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-27T16:03:57.910Z_

<details><summary>Logged reasoning block</summary>

```text
The HTML version returned a 404. Let me try the PDF version or another format.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b326566-13b1-4c6c-87e5-cab611c4e44d",
  "isSidechain": false,
  "requestId": "req_011CbTMf6TPvdsY4J6VEXie2",
  "type": "assistant",
  "uuid": "9134543f-b8df-4ac4-b177-0ed05ab50150",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018hqxt981QiqoEitam2uZzM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 13899,
      "output_tokens": 346,
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
          "input_tokens": 85,
          "output_tokens": 346,
          "cache_read_input_tokens": 13899,
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

### Assistant

_source line 17 · 2026-05-27T16:03:58.834Z_

The HTML version isn't available. Let me try the PDF and also check for any related blog posts or detailed discussions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9134543f-b8df-4ac4-b177-0ed05ab50150",
  "isSidechain": false,
  "requestId": "req_011CbTMf6TPvdsY4J6VEXie2",
  "type": "assistant",
  "uuid": "a051bbec-a2d1-4363-ac30-19fd90449de4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018hqxt981QiqoEitam2uZzM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 13899,
      "output_tokens": 346,
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
          "input_tokens": 85,
          "output_tokens": 346,
          "cache_read_input_tokens": 13899,
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

### Tool call

_source line 18 · 2026-05-27T16:04:01.072Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Cfxaohp22EazEoVny9fYAX`</summary>

```json
{
  "url": "https://arxiv.org/html/2503.07365v2",
  "prompt": "Extract the FULL text of ALL sections of this paper, preserving all detail. I need:\n1. Introduction (complete)\n2. Related Work (complete)  \n3. Method / Approach (complete — all subsections)\n4. Experiments / Results (complete — all tables, ablations)\n5. Conclusion and Limitations\n6. Any appendix content\n\nDo NOT summarize. Return as much raw text as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a051bbec-a2d1-4363-ac30-19fd90449de4",
  "isSidechain": false,
  "requestId": "req_011CbTMf6TPvdsY4J6VEXie2",
  "type": "assistant",
  "uuid": "7ae49261-420d-49ae-ad2e-5a3fd6cd47e4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018hqxt981QiqoEitam2uZzM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 13899,
      "output_tokens": 346,
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
          "input_tokens": 85,
          "output_tokens": 346,
          "cache_read_input_tokens": 13899,
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

_source line 19 · 2026-05-27T16:04:01.363Z_

<details><summary>↩ Tool result · `toolu_01Cfxaohp22EazEoVny9fYAX`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7ae49261-420d-49ae-ad2e-5a3fd6cd47e4",
  "isSidechain": false,
  "promptId": "6e9b4775-3324-430a-aeff-baabf4898966",
  "type": "user",
  "uuid": "13271332-7575-4080-a1e0-81825564530f",
  "toolUseResult": {
    "bytes": 0,
    "code": 404,
    "codeText": "Not Found",
    "result": "The server returned HTTP 404 Not Found.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.",
    "durationMs": 284,
    "url": "https://arxiv.org/html/2503.07365v2"
  },
  "sourceToolAssistantUUID": "7ae49261-420d-49ae-ad2e-5a3fd6cd47e4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-27T16:04:02.277Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HFFofpuhyWNsYCPDGes1qM`</summary>

```json
{
  "url": "https://github.com/ModalMinds/MM-EUREKA",
  "prompt": "Extract ALL content from this README: project description, method overview, dataset details (MMK12), training strategy, model results, any technical details about the approach, links to papers, models, datasets. Return everything."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13271332-7575-4080-a1e0-81825564530f",
  "isSidechain": false,
  "requestId": "req_011CbTMf6TPvdsY4J6VEXie2",
  "type": "assistant",
  "uuid": "b61d7c2d-cc5a-49fb-afcf-9e9031d01608",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018hqxt981QiqoEitam2uZzM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 13899,
      "output_tokens": 346,
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
          "input_tokens": 85,
          "output_tokens": 346,
          "cache_read_input_tokens": 13899,
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

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-27 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "b61d7c2d-cc5a-49fb-afcf-9e9031d01608",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze MM-Eureka multimodal reasoning paper",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6"
}
```

---

### Tool result

_source line 23 · 2026-05-27T16:04:12.570Z_

<details><summary>↩ Tool result · `toolu_01HFFofpuhyWNsYCPDGes1qM`</summary>

```text
# MM-EUREKA: Comprehensive Project Overview

## Project Description
MM-EUREKA represents research into multimodal reasoning through rule-based reinforcement learning. The initiative successfully extends large-scale RL techniques to vision-language models, advancing K12 and mathematical reasoning capabilities.

## Core Models Released
- **MM-Eureka-Qwen-7B**: Achieves 66.1 on MMK12, 73.0 on MathVista
- **MM-Eureka-Qwen-32B**: Scores 72.3 on MMK12, 74.8 on MathVista, 73.4 on WeMath
- **MM-Eureka-CPGD-Qwen-7B**: Alternative training variant using novel optimization

## Key Technical Improvements

**Algorithmic enhancements**:
- Online filtering for experience selection based on accuracy metrics
- ADORA (Adaptive Online Rollout Adjustment)
- DAPO loss implementation
- CPGD: "Clipped Policy Gradient Optimization with Policy Drift"—featuring clipping mechanisms and policy drift regularization

**Architecture changes**:
- Transitioned from InternVL to Qwen2.5-VL foundation
- Frozen Vision Transformer during training
- Replaced RLOO with GRPO algorithm

## MMK12 Dataset
"15k diverse and high-quality samples and 2k MCQs for Math, Physics, Chemistry, Biology" available on Hugging Face. Provides evaluation and training capabilities for multidisciplinary K12 reasoning.

## Training Strategy
- Online accuracy filtering with configurable bounds
- No KL divergence term during training
- Distributed training via Ray with vLLM integration
- Hybrid engine support with colocation options

## Performance Benchmarks

| Model | MathVista | WeMath | MMK12 |
|-------|-----------|--------|-------|
| MM-Eureka-Qwen-7B | 73.0 | 66.1 | 64.5 |
| MM-Eureka-Qwen-32B | 74.8 | 73.4 | 72.2 |
| Qwen2.5-VL-72B | 74.8 | 72.4 | 70.5 |

## Resources
- **Technical Reports**: MM_EUREKA_Tech_Report.pdf, CPGD_Tech_Report.pdf
- **ArXiv Links**: 2503.07365 (MM-Eureka), 2505.12504 (CPGD), 2505.13427 (MM-PRM)
- **Models**: Available on Hugging Face under FanqingM and Zkkkai accounts
- **Code Repository**: github.com/ModalMinds/MM-EUREKA (qwen branch)
- **Dataset**: huggingface.co/datasets/FanqingM/MMK12

## Building Upon
The project extends OpenRLHF framework, incorporating vision-language capabilities and multimodal RL support. Credits acknowledged to vLLM, InternVL, and Qwen2.5-VL projects.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b61d7c2d-cc5a-49fb-afcf-9e9031d01608",
  "isSidechain": false,
  "promptId": "6e9b4775-3324-430a-aeff-baabf4898966",
  "type": "user",
  "uuid": "afc21ea4-6b93-4928-ab86-c58f6aad222c",
  "toolUseResult": {
    "bytes": 353755,
    "code": 200,
    "codeText": "OK",
    "result": "# MM-EUREKA: Comprehensive Project Overview\n\n## Project Description\nMM-EUREKA represents research into multimodal reasoning through rule-based reinforcement learning. The initiative successfully extends large-scale RL techniques to vision-language models, advancing K12 and mathematical reasoning capabilities.\n\n## Core Models Released\n- **MM-Eureka-Qwen-7B**: Achieves 66.1 on MMK12, 73.0 on MathVista\n- **MM-Eureka-Qwen-32B**: Scores 72.3 on MMK12, 74.8 on MathVista, 73.4 on WeMath\n- **MM-Eureka-CPGD-Qwen-7B**: Alternative training variant using novel optimization\n\n## Key Technical Improvements\n\n**Algorithmic enhancements**:\n- Online filtering for experience selection based on accuracy metrics\n- ADORA (Adaptive Online Rollout Adjustment)\n- DAPO loss implementation\n- CPGD: \"Clipped Policy Gradient Optimization with Policy Drift\"—featuring clipping mechanisms and policy drift regularization\n\n**Architecture changes**:\n- Transitioned from InternVL to Qwen2.5-VL foundation\n- Frozen Vision Transformer during training\n- Replaced RLOO with GRPO algorithm\n\n## MMK12 Dataset\n\"15k diverse and high-quality samples and 2k MCQs for Math, Physics, Chemistry, Biology\" available on Hugging Face. Provides evaluation and training capabilities for multidisciplinary K12 reasoning.\n\n## Training Strategy\n- Online accuracy filtering with configurable bounds\n- No KL divergence term during training\n- Distributed training via Ray with vLLM integration\n- Hybrid engine support with colocation options\n\n## Performance Benchmarks\n\n| Model | MathVista | WeMath | MMK12 |\n|-------|-----------|--------|-------|\n| MM-Eureka-Qwen-7B | 73.0 | 66.1 | 64.5 |\n| MM-Eureka-Qwen-32B | 74.8 | 73.4 | 72.2 |\n| Qwen2.5-VL-72B | 74.8 | 72.4 | 70.5 |\n\n## Resources\n- **Technical Reports**: MM_EUREKA_Tech_Report.pdf, CPGD_Tech_Report.pdf\n- **ArXiv Links**: 2503.07365 (MM-Eureka), 2505.12504 (CPGD), 2505.13427 (MM-PRM)\n- **Models**: Available on Hugging Face under FanqingM and Zkkkai accounts\n- **Code Repository**: github.com/ModalMinds/MM-EUREKA (qwen branch)\n- **Dataset**: huggingface.co/datasets/FanqingM/MMK12\n\n## Building Upon\nThe project extends OpenRLHF framework, incorporating vision-language capabilities and multimodal RL support. Credits acknowledged to vLLM, InternVL, and Qwen2.5-VL projects.",
    "durationMs": 10291,
    "url": "https://github.com/ModalMinds/MM-EUREKA"
  },
  "sourceToolAssistantUUID": "b61d7c2d-cc5a-49fb-afcf-9e9031d01608",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-27T16:04:16.431Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I got the GitHub README info. Let me now try to get the actual paper content. Let me try the PDF directly or use a paper reading service.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "afc21ea4-6b93-4928-ab86-c58f6aad222c",
  "isSidechain": false,
  "requestId": "req_011CbTMgQT9fbpCHQqJcomqv",
  "type": "assistant",
  "uuid": "947ec3c0-6117-4968-8469-5180e8efe2a9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G7cCWvaD6U1Da9KWkNcaPG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1290,
      "cache_read_input_tokens": 14635,
      "output_tokens": 273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1290,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 273,
          "cache_read_input_tokens": 14635,
          "cache_creation_input_tokens": 1290,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1290
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

_source line 25 · 2026-05-27T16:04:17.187Z_

Good. Let me now try to access the paper PDF and also look for any detailed discussions or reviews.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "947ec3c0-6117-4968-8469-5180e8efe2a9",
  "isSidechain": false,
  "requestId": "req_011CbTMgQT9fbpCHQqJcomqv",
  "type": "assistant",
  "uuid": "c628e1fc-4119-4824-a4dc-9e1ac7286977",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G7cCWvaD6U1Da9KWkNcaPG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1290,
      "cache_read_input_tokens": 14635,
      "output_tokens": 273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1290,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 273,
          "cache_read_input_tokens": 14635,
          "cache_creation_input_tokens": 1290,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1290
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

_source line 26 · 2026-05-27T16:04:18.317Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DbzT4gbxGKu5dwfUSimpvE`</summary>

```json
{
  "url": "https://papers.cool/arxiv/2503.07365",
  "prompt": "Extract ALL content about this paper: the full abstract, introduction, method details, results, conclusion, and any community discussion or analysis. Return everything available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c628e1fc-4119-4824-a4dc-9e1ac7286977",
  "isSidechain": false,
  "requestId": "req_011CbTMgQT9fbpCHQqJcomqv",
  "type": "assistant",
  "uuid": "861f901d-cf4d-4624-8365-5cd34e7deab3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G7cCWvaD6U1Da9KWkNcaPG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1290,
      "cache_read_input_tokens": 14635,
      "output_tokens": 273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1290,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 273,
          "cache_read_input_tokens": 14635,
          "cache_creation_input_tokens": 1290,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1290
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

_source line 27 · 2026-05-27T16:04:19.086Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KEj67Agphd4njkFJNjphT6`</summary>

```json
{
  "url": "https://huggingface.co/papers/2503.07365",
  "prompt": "Extract all information about this paper: summary, discussion comments, upvotes, any community feedback or analysis. Return everything."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "861f901d-cf4d-4624-8365-5cd34e7deab3",
  "isSidechain": false,
  "requestId": "req_011CbTMgQT9fbpCHQqJcomqv",
  "type": "assistant",
  "uuid": "2fecf04b-858d-4325-a197-922048a48455",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G7cCWvaD6U1Da9KWkNcaPG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1290,
      "cache_read_input_tokens": 14635,
      "output_tokens": 273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1290,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 273,
          "cache_read_input_tokens": 14635,
          "cache_creation_input_tokens": 1290,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1290
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

_source line 28 · 2026-05-27T16:04:19.764Z_

<details><summary>↩ Tool result · `toolu_01KEj67Agphd4njkFJNjphT6`</summary>

```text
&lt;persisted-output>
Output too large (80.2KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/85dae6a1-bcc0-4c8f-97a6-84608d21f8c6/tool-results/toolu_01KEj67Agphd4njkFJNjphT6.txt

Preview (first 2KB):
# MM-EUREKA: EXPLORING THE FRONTIERS OF MULTIMODAL REASONING WITH RULE-BASED REINFORCEMENT LEARNING

Fanqing Meng\* Lingxiao Du\* Zongkai Liu\* Zhixiang Zhou\* Quanfeng Lu

Tiancheng Han Daocheng Fu Botian Shi Wenhai Wang Junjun He

Kaipeng Zhang Ping Luo Yu Qiao Qiaosheng Zhang† Wenqi Shao†

Shanghai AI Laboratory Shanghai Innovation Institute  
Shanghai Jiao Tong University The University of Hong Kong

## ABSTRACT

DeepSeek R1, and o1 have demonstrated powerful reasoning capabilities in the text domain through stable large-scale reinforcement learning. To enable broader applications, some works have attempted to transfer these capabilities to multimodal reasoning. However, these efforts have been limited by the limited difficulty of selected tasks and relatively small training scales, making it challenging to demonstrate strong multimodal reasoning abilities. To address this gap, we introduce the MMK12 dataset and MM-Eureka with 7B and 32B parameters. The former is a high-quality multimodal mathematics reasoning dataset featuring diverse knowledge domains with human-verified answers and solution processes. The latter is a multimodal model employing rule-based reinforcement learning on MMK12, utilizing online filtering and two-stage training strategy to enhance training stability. MM-Eureka demonstrates remarkable performance gains in multimodal mathematical reasoning, outperforming previous powerful models like InternVL2.5-78B or InternVL2.5-38B-MPO. In particular, MM-Eureka achieves competitive or superior performance compared to both open-source and closed-source models, and trails slightly behind o1 in multidisciplinary reasoning tasks. We open-source our complete pipeline to foster further research in this area. We release all our codes, models, data, etc. at &lt;https://github.com/ModalMinds/MM-EUREKA>

## 1 INTRODUCTION

...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "2fecf04b-858d-4325-a197-922048a48455",
  "isSidechain": false,
  "promptId": "6e9b4775-3324-430a-aeff-baabf4898966",
  "type": "user",
  "uuid": "650c1efe-7c78-4703-a9db-0edfdce5d4a0",
  "toolUseResult": {
    "bytes": 82276,
    "code": 200,
    "codeText": "OK",
    "result": "# MM-EUREKA: EXPLORING THE FRONTIERS OF MULTIMODAL REASONING WITH RULE-BASED REINFORCEMENT LEARNING\n\nFanqing Meng\\* Lingxiao Du\\* Zongkai Liu\\* Zhixiang Zhou\\* Quanfeng Lu\n\nTiancheng Han Daocheng Fu Botian Shi Wenhai Wang Junjun He\n\nKaipeng Zhang Ping Luo Yu Qiao Qiaosheng Zhang† Wenqi Shao†\n\nShanghai AI Laboratory Shanghai Innovation Institute  \nShanghai Jiao Tong University The University of Hong Kong\n\n## ABSTRACT\n\nDeepSeek R1, and o1 have demonstrated powerful reasoning capabilities in the text domain through stable large-scale reinforcement learning. To enable broader applications, some works have attempted to transfer these capabilities to multimodal reasoning. However, these efforts have been limited by the limited difficulty of selected tasks and relatively small training scales, making it challenging to demonstrate strong multimodal reasoning abilities. To address this gap, we introduce the MMK12 dataset and MM-Eureka with 7B and 32B parameters. The former is a high-quality multimodal mathematics reasoning dataset featuring diverse knowledge domains with human-verified answers and solution processes. The latter is a multimodal model employing rule-based reinforcement learning on MMK12, utilizing online filtering and two-stage training strategy to enhance training stability. MM-Eureka demonstrates remarkable performance gains in multimodal mathematical reasoning, outperforming previous powerful models like InternVL2.5-78B or InternVL2.5-38B-MPO. In particular, MM-Eureka achieves competitive or superior performance compared to both open-source and closed-source models, and trails slightly behind o1 in multidisciplinary reasoning tasks. We open-source our complete pipeline to foster further research in this area. We release all our codes, models, data, etc. at &lt;https://github.com/ModalMinds/MM-EUREKA>\n\n## 1 INTRODUCTION\n\nLarge-scale reinforcement learning (RL) (Sutton et al., 1998) has demonstrated remarkable progress in improving the reasoning ability of Large Language Models (LLMs), particularly in the math and code domains (OpenAI, 2024; DeepSeek-AI et al., 2025). Recent research, such as o1 (OpenAI, 2024) and DeepSeek-R1 (DeepSeek-AI et al., 2025), shows that large-scale RL can achieve breakthrough improvements in complex reasoning tasks during post-training phases, sometimes even without supervised fine-tuning (SFT) (Radford et al., 2019). Despite great success in the text domain, many real-world reasoning tasks such as interpreting scientific diagrams and geometrical reasoning can only be effectively solved with the image input. However, transferring large-scale RL techniques that work well for LLMs to multimodal scenarios remains underexplored.\n\nRecently, many works in the community have attempted to transfer the rule-based RL used in DeepSeek-R1 to multimodal scenarios. However, these works explore relatively small model sizes and fail to achieve stable training over extended periods like DeepSeek-R1. For instance, R1-V (Chen et al., 2025) demonstrates improvements only in simple counting tasks, which covers limited\n\n† Corresponding Authors: shaowenqi@pjlab.org.cn; zhangqiaosheng@pjlab.org.cn\n\n\\* Equal contributionFigure 1: The overview of our proposed MMK12 and MM-Eureka. MMK12 training set has diverse multimodal mathematical questions with verified answer and process, while its evaluation set has multiple-choice questions for each discipline including math, physics, chemistry, and biology. MM-Eureka built on MMK12 has powerful performance in multimodal reasoning and it also exists aha-moment like DeepSeek R1.\n\ncomplexity, while the model size remains modest. LMM-R1 (Peng et al., 2025) achieves gains in accuracy reward for geometric reasoning; however, such success has not been verified in large-scale training with image-text data. Although Kimi k1.5 (Team et al., 2025a) has achieved competitive results in multimodal reasoning, it has not open-sourced its model or training data to the community. Therefore, how to achieve stable rule-based RL training in the multimodal reasoning domain remains an important and unsolved problem for the open-source community.\n\nTo address this gap, as shown in Figure 1, we first collect MMK12\\*, a high-quality and diverse multimodal mathematical reasoning dataset. Subsequently, we implement MM-Eureka with two variants based on the MMK12 training set, i.e. MM-Eureka-7B built on Qwen2.5-VL-Instruct-7B and MM-Eureka-32B built on Qwen2.5-VL-Instruct-32B, which demonstrate excellent performance in multidisciplinary multimodal reasoning. For instance, MM-Eureka-7B achieves 66.1 on MMK12 evaluation sets, only 0.2 points below Intern2.5-VL-78B. On MathVista, it reaches 73.0, even surpassing InternVL2.5-VL-78B. MM-Eureka-32B demonstrates stronger performance, scoring 72.3 on multidisciplinary K12 evaluation sets, which exceeds both Qwen2.5-VL-72B’s 70.3 and closed-source models like Gemini2-Flash, ranking second only to o1’s 73.9. On commonly used multimodal mathematical reasoning benchmarks, MM-Eureka-32B achieves 73.4 on WeMath, outperforming all open-source models and most closed-source models including Claude3.7 Sonnet. On MathVista, it reaches 74.8, surpassing all open-source and closed-source models. Both variants demonstrate significant improvements in multidisciplinary K12 and mathematical reasoning performance, outperforming most open-source models of similar sizes.\n\n\\*K12 refers to the full span of primary and secondary education, and the K12 evaluation sets used in our work primarily contain questions from the secondary level.Specifically, despite growing interest in multimodal reasoning models, high-quality datasets for multimodal mathematical reasoning remain scarce. For example, Geo3k (Lu et al., 2021) and RCOT (Deng et al., 2024) focus only on geometry problems. Although MAVIS (Zhang et al., 2024b) comprises data involving geometry and functions, it consists of synthetic data, lacking diversity in images and questions. To this end, we construct MMK12, a K12-level multimodal mathematical reasoning dataset. The training set covers a wide range of domains, including functions, geometry, and equations, spanning from elementary through high school curricula. For evaluation, MMK12 includes four disciplines: mathematics, physics, chemistry, and biology. To facilitate testing, we collect 500 multimodal multiple-choice questions for each discipline and carefully verify that there is no overlap with the training set.\n\nSubsequently, to achieve stable rule-based RL training over extended periods, we utilize the online filter strategy from PRIME (Cui et al., 2025) that dynamically filters prompts with zero advantage during training, e.g., those answered either completely correctly or incorrectly. For MM-Eureka-32B, we further introduce a two-stage training strategy: the first stage leverages MMK12 by RL without KL divergence to develop the model’s general reasoning abilities while reducing training cost; the second stage fine-tunes the model on Geo3k with KL regularization to mitigate domain-specific deficiencies and enhance training stability. We use the GRPO (DeepSeek-AI et al., 2025) as our basic RL approach, which offers higher efficiency compared to the commonly used PPO (Schulman et al., 2017b). These strategies enable us to achieve stable, long-horizon RL training and consistent performance gains for both 7B and 32B model variants, while maintaining high training efficiency.\n\nThrough the journey of developing MM-Eureka, we have several findings. **First**, it is difficult for the model to acquire new knowledge through RL training. Instead, performance improvements come from increasing the probability that the model generates correct answers during inference. **Second**, we discover that simple rule-based RL exhibits outstanding generalization capabilities. Training solely on mathematical data leads to simultaneous improvements in physics, chemistry, biology, and other disciplines. **Third**, rule-based RL generalizes better than other post-training strategies such as SFT (Ouyang et al., 2022) and COT SFT (Guo et al., 2024) across various tasks.\n\nOur goal is to share our implementation experiences and complete the open-source pipeline with the community, including data, code, and models. We believe this comprehensive open-source framework would help the community better explore the multimodal reasoning task. The main contributions are summarized as follows:\n\n- • We utilize an online filter strategy and introduce a two-stage training strategy to address the collapse issues encountered during RL training of large-scale VLMs, achieving stable rule-based RL training for large-scale VLMs.\n- • We present MM-Eureka-7B and MM-Eureka-32B. Extensive experimental results on various downstream tasks demonstrate that they are top performers among open-source models in the multimodal reasoning domain. For example, MM-Eureka-32B scores only 1.7 points below o1 on the multidisciplinary evaluation set of MMK12; MM-Eureka-7B achieves 73.0 on MathVista (Lu et al., 2024), surpassing InternVL2.5-78B (Chen et al., 2024).\n- • We open-source all our models, code, and collected high-quality multimodal mathematical reasoning data. Compared to existing open-source repositories, we support a wider range of RL algorithms and include much higher-quality data.\n\n## 2 RELATED WORK\n\n### 2.1 LANGUAGE REASONING MODEL\n\nLLMs have demonstrated impressive performance across a wide range of tasks, yet more complex challenges require these models to exhibit human-like reasoning capabilities. As a result, enhancing the reasoning ability of LLMs has become a critical research focus. Reinforcement Learning from Human Feedback (RLHF), particularly Proximal Policy Optimization (PPO) (Schulman et al., 2017a), has shown promise in enabling LLMs to learn reasoning abilities effectively. However, the PPO training process is computationally intensive and complex, prompting the development of simplified alternatives such as Direct Preference Optimization (DPO) (Rafailov et al., 2023). WhileDPO alleviates some training difficulties, its reliance on offline data can limit model performance. To address these limitations, methods like Group Relative Policy Optimization (GRPO) (DeepSeek-AI et al., 2025), REINFORCE Leave-One-Out (RLOO) (Kool et al., 2019; Ahmadian et al., 2024), and Reinforce++ (Hu, 2025) have been introduced. Notably, Deepseek R1 (DeepSeek-AI et al., 2025) reveals that pure RL can encourage LLMs to actively engage in reasoning, including self-reflection and error correction. Despite these advancements, research on improving the reasoning capabilities of multimodal large models remains relatively scarce, highlighting an important direction for future exploration.\n\n## 2.2 VISION-LANGUAGE REASONING MODEL\n\nCurrently, the leading models in multimodal reasoning are closed-source systems such as GPT-4o (Hurst et al., 2024) and Kimi-VL (Team et al., 2025b). In contrast, the open-source community remains noticeably behind, still in the early stages of exploration. Recent concurrent efforts have begun to explore the use of RL to enhance the visual reasoning capabilities of vision-language reasoning models (VLMs), aiming to trigger an “Aha Moment” in visual reasoning. LMM-R1 (Peng et al., 2025) strengthens visual reasoning through a two-stage rule-based RL approach; however, its primary reasoning performance gains are derived from text-only datasets rather than genuinely multimodal datasets. R1-V (Chen et al., 2025) investigates rule-based RL within specific subdomains, such as geometric reasoning and object counting tasks, but falls short of addressing more complex reasoning challenges. Reason-RFT (Tan et al., 2025), on the other hand, relies on SFT with COT reasoning activation data to achieve an effective cold start before the RL training phase. In this paper, our objective is to develop an effective, stable, and comprehensive open-source training pipeline for multimodal reasoning models, including datasets, code, and models. Our work aims to advance the growth and innovation of the open-source community.\n\n## 3 MMK12: MULTIMODAL MATHEMATIC K12-LEVEL DATASET\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>&lt;/th>\n&lt;th>Scope&lt;/th>\n&lt;th>Type&lt;/th>\n&lt;th>Img. Source&lt;/th>\n&lt;th>QA Source&lt;/th>\n&lt;th>CoT Answer Source&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>MAVIS (Zhang et al., 2024b)&lt;/td>\n&lt;td>Geo &amp; Func&lt;/td>\n&lt;td>MCQ &amp; FB&lt;/td>\n&lt;td>Synthetic&lt;/td>\n&lt;td>Synthetic Engine&lt;/td>\n&lt;td>GPT-4o&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Geo3k (Lu et al., 2021)&lt;/td>\n&lt;td>Geo&lt;/td>\n&lt;td>FB&lt;/td>\n&lt;td>Real world&lt;/td>\n&lt;td>Real world&lt;/td>\n&lt;td>None&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RCOT (Deng et al., 2024)&lt;/td>\n&lt;td>Geo&lt;/td>\n&lt;td>MCQ &amp; FB&lt;/td>\n&lt;td>Synthetic&lt;/td>\n&lt;td>Synthetic Engine&lt;/td>\n&lt;td>GPT-4o&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MultiMath (Peng et al., 2024)&lt;/td>\n&lt;td>Diverse&lt;/td>\n&lt;td>MCQ &amp; FB&lt;/td>\n&lt;td>Real World&lt;/td>\n&lt;td>GPT-4o&lt;/td>\n&lt;td>GPT-4o&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MMK12&lt;/td>\n&lt;td>Diverse&lt;/td>\n&lt;td>FB&lt;/td>\n&lt;td>Real World&lt;/td>\n&lt;td>Real World&lt;/td>\n&lt;td>Real World&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nTable 1: Comparison of dataset characteristics with other multimodal mathematical reasoning datasets. MMK12 comprises more diverse and high quality questions, with guaranteed correct answers and solution processes.\n\nAs shown in Table 1, current multimodal mathematical reasoning datasets have limited scope and face challenges in ensuring answer correctness. For instance, while RCOT and MAVIS maintain answer accuracy through synthetic engine-generated QA pairs, this approach restricts problem diversity. Geo3k manually collected 3,000 geometry problems with verified answers, but it focuses solely on geometry examples. Although MultiMath gathers problems from real-world scenarios to ensure diversity, its reference answers generated by GPT-4o cannot guarantee correctness.\n\nTo address these limitations, we introduce MMK12, a new dataset comprising over 15,000 multimodal mathematical reasoning problems across a wide range of domains, including geometry, functions, and graphical reasoning. Each problem is accompanied by a standard reference answer and a detailed step-by-step solution to ensure both accuracy and interpretability.\n\nIn the following, we describe the construction and cleaning process of MMK12. As illustrated in Figure 2, we first collect a diverse set of multimodal mathematics problems and corresponding answers from a variety of Chinese mathematics textbooks and examination papers, covering grades from elementary to high school. These questions, answers, and COT processes are subsequently translated and refined into English, with the help of LLM. To minimize false positives during training, we retain only fill-in-the-blank problems. Besides, we use Math-Verify&lt;sup>†&lt;/sup> to parse\n\n&lt;sup>†&lt;/sup>&lt;https://github.com/huggingface/Math-Verify>The diagram illustrates the MMK12 construction pipeline. It begins with a collection of diverse K12-level multimodal math problems from various sources, including PDF, CSV, DOCX, and HTML files, along with images. These are processed through two parallel paths: 'Manual Annotation' and 'LLM Translation & Refinement'. The 'Manual Annotation' path involves human experts reviewing the data, while the 'LLM Translation & Refinement' path uses Large Language Models (LLMs) to translate the content into standardized English. The resulting 'Structured Data' is then subjected to a verification process. This process includes a 'Fill-in-the-blank?' check, which leads to 'Math-Verify' and 'Image size' checks, and a 'Multiple-choice?' check, which leads to 'Question type' and 'Single Image' checks. The final output is the 'MMK12 Training Dataset' and the 'MMK12 Benchmark'.\n\nFigure 2: The construction overview of MMK12. We collect diverse K12-level multimodal math problems from multiple sources, convert them to standardized English using LLMs, and verify all content for accuracy. The resulting MMK12 dataset includes a training set of 15,616 samples and a test set with 500 multiple-choice questions each for math, physics, chemistry, and biology.\n\nthe answer, ensuring data reliability for RL training. For the MMK12 evaluation set, we follow a similar construction procedure, but exclusively select multiple-choice questions to facilitate reliable and efficient evaluation.\n\nIn total, the MMK12 training dataset comprises 15,616 multimodal fill-in-the-blank mathematics problems, including 455 from elementary school, 9,776 from middle school, and 5,385 from high school. Each sample includes the question, an image, the final answer, and a CoT-formatted solution process. The MMK12 evaluation set has 2,000 multimodal multiple-choice questions, including math, physics, chemistry, and biology. Each item includes a question, a corresponding image, and the correct answer choice. Some examples in MMK12 are shown in Figure 1.\n\nMMK12 encompasses mathematical problems across various knowledge domains, including geometry, functions, spatial reasoning, and more. Some important categories are introduced as follows:\n\n- • **Function Reasoning:** This task requires models to understand function concepts, analyze function graphs and expressions, and apply function properties to solve problems. This type of reasoning develops the model’s ability to comprehend abstract mathematical concepts, fostering its capability to identify function characteristics, determine critical points, and analyze function behavior.\n- • **Geometric Reasoning:** This task involves applying spatial relationships, geometric theorems, and properties of shapes. Through geometric reasoning training, models enhance their spatial visualization, logical deduction, and formalization abilities for geometry problems, enabling them to solve complex problems in both plane and solid geometry.\n- • **Pattern Reasoning:** This type of task focuses on understanding flow diagrams and recognizing patterns in visual sequences. Models need to discover patterns, predict rule-based changes, or understand logical relationships in visual content. This task examines the model’s pattern recognition abilities, inductive reasoning skills, and visual logical thinking.\n\nBenefiting from a standardized data construction process with substantial human involvement and verification, MMK12 ensures both diversity in questions and correctness in answers and solution processes, making it suitable for various training methods such as RL and SFT for multimodal mathematical reasoning models. The MMK12 evaluation set also provides a convenient and accurate means to test models’ multidisciplinary reasoning capabilities.\n\n## 4 METHOD\n\n### 4.1 BASIC SETTINGS\n\nWe employ Qwen2.5-VL (Bai et al., 2023) with 7B and 32B as the base models. Our RL algorithm is similar to DeepSeek-R1 (DeepSeek-AI et al., 2025), using rule-based format rewards  $r_{\\text{format}} \\in \\{0, 0.5\\}$ , accuracy rewards  $r_{\\text{accuracy}} \\in \\{0, 1\\}$  as reward function and GRPO as base RL algorithm for training. Furthermore, we develop a multimodal input RL framework based on OpenRLHF (Hu et al., 2024), which is compatible with commonly used models such as InternVL (Chen et al., 2024) and QwenVL, supporting various model sizes and RL algorithms. In the following sections, we provide detailed settings for our RL training.## 4.2 REWARD FUNCTION\n\nFollowing DeepSeek-R1, we also adopt the simple rule-based reward function rather than using outcome or process reward models, thereby alleviating reward hacking (Gao et al., 2022). Specifically, we use two types of rewards: accuracy reward and format reward. The former uses Math-Verify to extract the answer from model responses and compare it with the reference one, returning 1 or 0 based on correctness; the latter checks whether the response follows the specified format (`&lt;think>...&lt;/think>&lt;answer>...&lt;/answer>`), returning 0.5 or 0 based on compliance. We find that this simple and sparse reward is sufficient to significantly improve the model’s multimodal reasoning ability.\n\n## 4.3 ADVANTAGE ESTIMATION AND POLICY UPDATE\n\nGroup Relative Policy Optimization (GRPO) (DeepSeek-AI et al., 2025) is a widely adopted RL algorithm that eliminates the need for training a complex critic model by leveraging intra-group relative performance to optimize the policy model. Specifically, for each query  $\\mathbf{x}$ , the model generates a group of  $G$  responses  $\\{\\mathbf{y}^{(1)}, \\mathbf{y}^{(2)}, \\dots, \\mathbf{y}^{(G)}\\}$ . Subsequently, for each query with  $G$  responses, GRPO computes the relative advantage of each response based on their rewards, which are determined by a reward model, as follows:\n\n$$A^{(i)} = \\frac{r^{(i)} - \\text{mean}(\\{r^{(j)}\\}_{j=1}^G)}{\\text{std}(\\{r^{(j)}\\}_{j=1}^G)}, \\quad i = 1, \\dots, G.$$\n\nUsing the computed advantages, GRPO then optimizes the policy via the PPO-clip loss augmented with a directly imposed KL penalty term:\n\n$$J_{\\text{PPO}}(\\theta) = -\\mathbb{E}_{\\mathbf{x} \\sim \\mathcal{D}, \\{\\mathbf{y}^{(i)}\\}_{i=1}^G \\sim \\pi_\\theta(\\cdot | \\mathbf{x})} \\left[ \\frac{1}{G} \\sum_{i=1}^G \\frac{1}{|\\mathbf{y}^{(i)}|} \\sum_{t=1}^{|\\mathbf{y}^{(i)}|} \\left( \\min \\left( r^{i,t}(\\theta) A^{(i)}, \\text{clip}(r^{i,t}(\\theta), 1 - \\epsilon, 1 + \\epsilon) A^{(i)} \\right) - \\beta D_{\\text{KL}}^{i,t}(\\pi_\\theta, \\pi_{\\text{ref}}) \\right) \\right], \\quad (1)$$\n\nwhere\n\n$$r^{i,t}(\\theta) = \\frac{\\pi_\\theta(y_t^{(i)} | \\mathbf{x}, \\mathbf{y}_{&lt;t}^{(i)})}{\\pi_{\\theta_{\\text{old}}}(y_t^{(i)} | \\mathbf{x}, \\mathbf{y}_{&lt;t}^{(i)})} \\text{ and } D_{\\text{KL}}^{i,t}(\\pi_\\theta, \\pi_{\\text{ref}}) = \\frac{\\pi_{\\text{ref}}(y_t^{(i)} | \\mathbf{x}, \\mathbf{y}_{&lt;t}^{(i)})}{\\pi_\\theta(y_t^{(i)} | \\mathbf{x}, \\mathbf{y}_{&lt;t}^{(i)})} - 1 - \\log \\frac{\\pi_{\\text{ref}}(y_t^{(i)} | \\mathbf{x}, \\mathbf{y}_{&lt;t}^{(i)})}{\\pi_\\theta(y_t^{(i)} | \\mathbf{x}, \\mathbf{y}_{&lt;t}^{(i)})}.$$\n\nIn addition, to mitigate loss spikes during training caused by excessively large policy ratios combined with negative advantages, we further constrain the policy ratio within  $[0, c]$  beforehand, i.e., we replace  $r^{i,t}(\\theta)$  with  $\\text{clip}(r^{i,t}(\\theta), 0, c)$  in Eq.(1). In practice, we set the default value of  $c$  to 3.\n\n## 4.4 ONLINE FILTERING\n\nTo further enhance training stability, we adopt the online prompt filtering strategy proposed in PRIME (Cui et al., 2025). To ensure sufficient gradient information throughout RL training, we filter out prompts with responses that are either completely correct or completely incorrect during training, as their corresponding advantages under GRPO are zero. The detailed process is shown in Algorithm 1.\n\nWe present an ablation study on the online filtering mechanism in Figure 3. Models trained with the online filter strategy maintain relatively stable trends in both the accuracy-based reward and response length throughout training. In contrast, models without the online filter show an initial improvement in accuracy, but soon experience a sharp decline, with accuracy eventually approaching zero and response lengths significantly shortening in the later stages. These findings suggest that the online filter plays an important role in stabilizing RL training and can help prevent model collapse during optimization.\n\n## 4.5 TWO-STAGE TRAINING\n\nDuring RL training of MM-Eureka-32B, we observe that maintaining training stability becomes increasingly challenging as model size scales up. Specifically, we find that models tend to experience**Algorithm 1** Online Filter\n\n**Input:** Prompt dataset  $\\mathcal{D}$ ; initial policy  $\\pi_\\theta$ ; reward model  $R$ ; buffer size  $N_B$ ; hyperparameters  $K_1, K_2, G, \\epsilon_{\\text{acc}}^{\\text{lower}}, \\epsilon_{\\text{acc}}^{\\text{upper}}$\n\n**Output:**  $\\pi_\\theta$\n\n```\n\n1: Buffer  $\\mathcal{B} \\leftarrow \\{\\}$ \n2: for iteration = 1, ...,  $K_1$  do\n3:   Sample a batch of prompts  $\\mathcal{Q} \\sim \\mathcal{D}$ \n4:   for each prompt  $\\mathbf{x} \\in \\mathcal{Q}$  do\n5:     Generate  $G$  responses  $\\{\\mathbf{y}^{(i)}\\}_{i=1}^G \\sim \\pi_\\theta(\\cdot|\\mathbf{x})$ \n6:     Compute the reward  $r^{(i)} = R(\\mathbf{x}, \\mathbf{y}^{(i)})$  for  $i = 1, \\dots, G$ \n7:     Compute the accuracy  $\\mathcal{C}_{\\mathbf{x}} = |\\{\\mathbf{y}^{(i)} | r^{(i)} = 1\\}|$ \n8:     if  $\\epsilon_{\\text{acc}}^{\\text{lower}} \\leq \\mathcal{C}_{\\mathbf{x}} \\leq \\epsilon_{\\text{acc}}^{\\text{upper}}$  then\n9:       Add the sample to the buffer  $\\mathcal{B} \\leftarrow \\mathcal{B} \\cup \\{(\\mathbf{x}, \\mathbf{y}^{(i)}, r^{(i)})\\}_{i=1}^G$ \n10:    end if\n11:  end for\n12:  if  $|\\mathcal{B}| \\geq N_B$  then\n13:    for Epoch = 1, ...,  $K_2$  do\n14:      Update policy  $\\pi_\\theta$  on  $\\mathcal{B}[0:N_B]$  by any RL algorithm\n15:    end for\n16:    Buffer  $\\mathcal{B} \\leftarrow \\{\\}$ \n17:  end if\n18: end for\n\n```\n\nFigure 3: Comparison of the use of online filtering. Using online filter makes the RL training more stable in the long term, with consistently increasing accuracy reward and response length.\n\nsudden collapse during training, characterized by an abrupt drop of the accuracy reward to near-zero values, as shown in Figure 5 (a). After analysis, we find that these collapses are usually preceded by sharp increases in the policy ratio (indicating excessively large updates from old to new policies) like Figure 5 (c). Additionally, unlike the 7B model which shows comprehensive improvement when trained solely on K12 data, the 32B model trained only on MMK12 exhibits performance degradation in specific domains such as geometry.\n\nTo address these challenges, we propose a two-stage training strategy for large models. In the first stage, we apply the GRPO algorithm without KL regularization, using MMK12 data collected as detailed in Section 3 to broadly enhance the model’s general reasoning capabilities. In the second stage, we incorporate a KL divergence into GRPO to constrain update magnitudes and improve training stability. Concurrently, we augment the training set with domain-specific Geo3k data to address identified performance gaps. As shown in Section 6.3, this two-stage approach enables stable training and yields further performance gains across nearly all evaluated benchmarks.\n\n## 5 EXPERIMENTS\n\nWe present our experimental setup in Section 5.1, where we indicate the training details. After that, we provide an overview of the selected baselines and evaluation benchmarks in Section 5.2 and Section 5.3, we demonstrate the superior effectiveness of MM-Eureka-7B and MM-Eureka-32B through extensive experiments in Section 5.4.## 5.1 EXPERIMENTS SETUP\n\nWe design our prompt template following the format used in DeepSeek-R1, wherein the system prompt explicitly specifies the required output structure, including the use of `&lt;answer>` tags to separate the reasoning process from the final answer. Detailed prompt configurations are provided in Table 2.\n\nFor training hyperparameters, both the rollout batch size and training batch size are set to 128, with 8 rollouts generated per sample. Sampling is conducted with a temperature of 1.0 to encourage response diversity, and optimization is performed using a learning rate of  $1 \\times 10^{-6}$ . Besides, for MM-Eureka-32B, we adopt a two-stage training scheme. In Stage 1, KL divergence is disabled to promote exploration and policy flexibility during the early phase. In Stage 2, a small KL penalty  $1 \\times 10^{-3}$  is introduced to stabilize training.\n\nTable 2: Prompt setting for MM-Eureka.\n\n---\n\n**SYSTEM:** Solve the question. The user asks a question, and you solve it. You first think about the reasoning process in the mind and then provide the user with the answer. The answer is in latex format and wrapped in `$...$`. The final answer must be wrapped using the `\\boxed{}` command. The answer should be enclosed within `&lt;answer>&lt;/answer>` tags, i.e., Since  $1+1=2$ , so the answer is  $\\boxed{2}$ . `&lt;answer>`The answer is  $\\boxed{2}$ `&lt;/answer>`, which means the final answer assistant’s output should start with `&lt;answer>` and end with `&lt;/answer>`.\n\n**USER:** `&lt;image><{{question}}&lt;/image>`\n\n---\n\n## 5.2 BASELINES\n\nTo comprehensively evaluate the effectiveness of MM-Eureka, we compare it against a diverse set of baselines, including both closed-source and open-source systems.\n\n**Closed-Source Models.** We include several leading proprietary models in our comparison. GPT-4o (Hurst et al., 2024), Claude3.7-Sonnet (Anthropic, 2024), and Gemini2-flash (Team et al., 2023) are general-purpose multimodal models without dedicated reasoning optimization, while o1 (OpenAI, 2024) is explicitly designed to enhance reasoning capabilities. These models serve as strong references for the current state of the art.\n\n**Open-Source General Models.** This group comprises high-capacity vision-language models trained for general purposes, including Qwen-2.5-VL (Bai et al., 2023) and InternVL2.5 (Chen et al., 2024) across various model sizes (7B to 78B). These models are primarily pretrained or instruction-tuned on large-scale image-text datasets. They offer a baseline for evaluating the impact of reasoning-specific post-training.\n\n**Open-Source Reasoning Models.** We further include open-source models explicitly fine-tuned for reasoning, such as InternVL2.5-MPO variants (Wang et al., 2024b), QVQ-72B-Preview (Team, 2024), Adora-7B (Gui & Ren, 2025), R1-Onevision (Yang et al., 2025), and OpenVLThinker (Deng et al., 2025). These models employ various strategies, including SFT (Ouyang et al., 2022), DPO (Rafailov et al., 2023), and rule-based reinforcement learning. They represent the most competitive open-source efforts in multimodal reasoning.\n\n## 5.3 BENCHMARKS\n\nTo assess the performance of our model, we conduct evaluations on multiple benchmark datasets, including MathVista(testmini) (Lu et al., 2024), MathVerse(testmini) (Zhang et al., 2024a), MathVision(test) (Wang et al., 2024a), OlympiadBench(EN-OE split) (He et al., 2024) and WeMath (Qiao et al., 2024). MathVista is one of the most widely used multimodal mathematical benchmarks, offering a diverse set of problems that span general visual question answering, figure question answering, logic, algebra, and geometry. MathVerse, on the other hand, focuses specifically on themodel’s ability to comprehend images, with tasks categorized into areas such as algebra and geometry. MathVision takes this a step further by emphasizing more abstract visual understanding, testing the model’s capacity for recognizing and reasoning beyond conventional mathematical contexts. OlympiadBench presents graduate-level mathematical competition problems, from which we select the English questions for evaluation. WeMath complements these by providing fine-grained diagnostic insights into model reasoning behavior, using a large-scale, hierarchically annotated problem set to assess knowledge mastery and generalization.\n\nBeyond these established benchmarks, both our model and the baselines are further evaluated on the proposed MMK12 Benchmark, as introduced in Section 3. Unlike OlympiadBench, which targets advanced graduate-level mathematical reasoning, MMK12 focuses on assessing the model’s ability to solve fundamental multimodal multidisciplinary problems commonly encountered in K12 education. MMK12 enables a comprehensive evaluation of a model’s ability across disciplines beyond mathematics.\n\nDuring evaluation, we adopt greedy decoding with a temperature of 0, ensuring deterministic outputs. We do not use beam search, and both top- $p$  and top- $k$  sampling are disabled.\n\n#### 5.4 QUANTITATIVE RESULTS\n\nIn this section, we demonstrate the superiority of MM-Eureka through its performance on the benchmarks introduced in Section 5.3. For the multimodal mathematical evaluation sets, we primarily use official results or results provided in VLMEvalKit (Duan et al., 2024) for baseline comparisons. When such results are unavailable, we conduct evaluations using the testing methodologies provided in VLMEvalKit within our vllm-based (Kwon et al., 2023) inference framework. Specifically, for o1, due to resource constraints, we randomly sample only 500 instances for testing. For the MMK12 evaluation set, considering it consists entirely of multiple-choice questions, we use the same Chain-of-Thought prompt structure from WeMath (Qiao et al., 2024) to test models within our inference framework. Because WeMath also consists entirely of multiple-choice questions. Results evaluated by ourselves are presented in *italics*.\n\n**Mathematics** In Table 3, we present a comprehensive summary of MM-Eurekas’ performance across different multimodal mathematical reasoning tasks. It demonstrates that both MM-Eureka-7B and MM-Eureka-32B consistently outperform similar-sized open-source baselines across almost all tasks. In particular, MM-Eureka-7B achieves 73.0 on Mathvista, surpassing InternVL-78B by 0.7% and the reasoning-focused InternVL2.5-38B-MPO by 0.2%. On WeMath, it similarly approaches the performance of InternVL-78B. MM-Eureka-32B exceeds all current open-source models of comparable size on all benchmarks except MathVision, with average performance approaching Qwen-72B-Instruct. It even outperforms the closed-source model Claude3.7 Sonnet on WeMath. In summary, MM-Eureka establishes itself as the top performer among same-sized open-source models across almost all multimodal mathematical reasoning tasks, regardless of whether considering the 7B or 32B version.\n\nHowever, when compared to closed-source models, MM-Eureka-32B still shows considerable performance gaps. While it outperforms o1 on Mathvista, it lags significantly behind closed-source multimodal reasoning models like o1 on more challenging benchmarks such as Mathvision or OlympiadBench.\n\n**MMK12** Beyond validating our model’s superiority on widely-used multimodal mathematical reasoning benchmarks like MathVista, it is necessary to test its capabilities and generalization across multidisciplinary reasoning domains using questions absent from the training set (e.g., physics, chemistry, and biology). For this purpose, we employ the MMK12 dataset constructed in Section 3, which can effectively measure models’ multimodal reasoning capabilities across multiple disciplines.\n\nAs shown in Table 4, MM-Eureka-32B demonstrates multidisciplinary capabilities only marginally behind o1 by 1.7%, while outperforming larger-scale models such as Qwen-2.5-VL-72B and\n\n&lt;sup>†&lt;/sup>Results of o1 based on random sampling of 500 test instances due to resource constraints.\n\n&lt;sup>‡&lt;/sup>Results of R1-Onevision in Mathvision is 23.5 from our evaluation, which is far behind its official report as 29.9.Table 3: Performance comparison across different multimodal mathematical benchmarks. Bold indicates the top performer with the open-source models, while underline indicates the second best performer within open-source models. For some official results that are relatively different from our evaluation results, we mark our test results after ’/’.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Model&lt;/th>\n&lt;th>MathVista&lt;/th>\n&lt;th>MathVerse&lt;/th>\n&lt;th>Mathvision&lt;/th>\n&lt;th>OlypamidBench&lt;/th>\n&lt;th>WeMath&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td colspan=\"6\">&lt;b>Closed-Source Models&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Claude3.7-Sonnet&lt;/td>\n&lt;td>66.8&lt;/td>\n&lt;td>52.0&lt;/td>\n&lt;td>41.3&lt;/td>\n&lt;td>48.9&lt;/td>\n&lt;td>72.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GPT-4o&lt;/td>\n&lt;td>63.8&lt;/td>\n&lt;td>50.2&lt;/td>\n&lt;td>30.4&lt;/td>\n&lt;td>35.0&lt;/td>\n&lt;td>68.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>o1&lt;/td>\n&lt;td>73.9&lt;/td>\n&lt;td>57.0&lt;/td>\n&lt;td>60.3&lt;/td>\n&lt;td>68.0*&lt;/td>\n&lt;td>98.7*&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Gemini2-flash&lt;/td>\n&lt;td>70.4&lt;/td>\n&lt;td>59.3&lt;/td>\n&lt;td>41.3&lt;/td>\n&lt;td>51.0&lt;/td>\n&lt;td>71.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"6\">&lt;b>Open-Source General Models&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>InternVL2.5-VL-8B&lt;/td>\n&lt;td>64.4&lt;/td>\n&lt;td>39.5&lt;/td>\n&lt;td>19.7&lt;/td>\n&lt;td>12.3&lt;/td>\n&lt;td>53.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen-2.5-VL-7B&lt;/td>\n&lt;td>68.2&lt;/td>\n&lt;td>47.9&lt;/td>\n&lt;td>25.4&lt;/td>\n&lt;td>20.2&lt;/td>\n&lt;td>62.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>InternVL2.5-VL-38B&lt;/td>\n&lt;td>71.9&lt;/td>\n&lt;td>49.4&lt;/td>\n&lt;td>31.8&lt;/td>\n&lt;td>32.0&lt;/td>\n&lt;td>67.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen-2.5-VL-32B&lt;/td>\n&lt;td>74.7/71.7&lt;/td>\n&lt;td>49.9&lt;/td>\n&lt;td>&lt;b>40.1&lt;/b>&lt;/td>\n&lt;td>30.0&lt;/td>\n&lt;td>69.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>InternVL2.5-VL-78B&lt;/td>\n&lt;td>72.3&lt;/td>\n&lt;td>51.7&lt;/td>\n&lt;td>32.2&lt;/td>\n&lt;td>31.1&lt;/td>\n&lt;td>66.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen-2.5-VL-72B&lt;/td>\n&lt;td>&lt;b>74.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>57.6&lt;/b>&lt;/td>\n&lt;td>&lt;u>38.1&lt;/u>&lt;/td>\n&lt;td>&lt;b>40.4&lt;/b>&lt;/td>\n&lt;td>&lt;u>72.4&lt;/u>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"6\">&lt;b>Open-Source Reasoning Models&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>InternVL2.5-8B-MPO&lt;/td>\n&lt;td>68.9&lt;/td>\n&lt;td>35.5&lt;/td>\n&lt;td>21.5&lt;/td>\n&lt;td>7.8&lt;/td>\n&lt;td>53.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>InternVL2.5-38B-MPO&lt;/td>\n&lt;td>73.8&lt;/td>\n&lt;td>46.5&lt;/td>\n&lt;td>32.3&lt;/td>\n&lt;td>25.6&lt;/td>\n&lt;td>66.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>QVQ-72B-Preview&lt;/td>\n&lt;td>71.4&lt;/td>\n&lt;td>48.2&lt;/td>\n&lt;td>35.9&lt;/td>\n&lt;td>33.2&lt;/td>\n&lt;td>65.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Adora-7B&lt;/td>\n&lt;td>73.5&lt;/td>\n&lt;td>50.1&lt;/td>\n&lt;td>23.0&lt;/td>\n&lt;td>20.1&lt;/td>\n&lt;td>64.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>R1-Onevision-7B&lt;/td>\n&lt;td>64.1&lt;/td>\n&lt;td>47.1&lt;/td>\n&lt;td>29.9/23.5&lt;/td>\n&lt;td>17.3&lt;/td>\n&lt;td>61.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>OpenVLThinker-7B&lt;/td>\n&lt;td>70.2&lt;/td>\n&lt;td>47.9&lt;/td>\n&lt;td>25.3&lt;/td>\n&lt;td>20.1&lt;/td>\n&lt;td>64.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"6\">&lt;b>Ours&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MM-Eureka-7B&lt;/td>\n&lt;td>73.0&lt;/td>\n&lt;td>50.3&lt;/td>\n&lt;td>26.9&lt;/td>\n&lt;td>20.1&lt;/td>\n&lt;td>66.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MM-Eureka-32B&lt;/td>\n&lt;td>&lt;b>74.8&lt;/b>&lt;/td>\n&lt;td>&lt;u>56.5&lt;/u>&lt;/td>\n&lt;td>34.4&lt;/td>\n&lt;td>&lt;u>35.9&lt;/u>&lt;/td>\n&lt;td>&lt;b>73.4&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nGemini2-Flash-Thinking. MM-Eureka-7B also surpasses several similarly-sized multimodal reasoning models, including OpenVLThinker-7B, with overall performance exceeding InternVL2.5-VL-78B and only slightly behind Qwen-2.5-VL-32B. Additionally, we observe several interesting findings: 1) Despite being trained exclusively on fill-in-the-blank questions, our models maintain strong instruction-following abilities for multiple-choice questions with improved performance. 2) Even with training solely on mathematics problems, the models exhibit enhanced capabilities in physics, chemistry, and biology. Specifically, MM-Eureka-7B shows improvements of 9.8% and 11.2% in chemistry and biology, respectively, demonstrating the remarkable generalization capacity of our straightforward RL strategy.\n\n## 5.5 QUALITATIVE RESULTS\n\nAppendix A illustrates representative examples comparing MM-Eureka-32B with its base model Qwen2.5-VL-32B-Instruct across four subjects: mathematics, physics, chemistry, and biology. These qualitative cases reveal that our model, after reinforcement learning, demonstrates significantly enhanced reasoning capabilities. Specifically, MM-Eureka-32B is able to better apply known concepts and perform multi-step deduction to arrive at the correct answers. In contrast, the base model often shows surface-level understanding—it may recall relevant facts but fails to apply them coherently in the problem-solving context.\n\nFor instance, in the physics example (Figure 7), the question involves analyzing the instantaneous contact force between two objects placed on a vertical spring. While both models recognize key physical quantities such as mass, weight, and spring force, only MM-Eureka-32B correctly applies Newton’s second law to derive the acceleration of the system and compute the contact force. It identifies that the net external force due to the added mass leads to a downward acceleration, and accurately calculates the resulting contact force between object A and B as  $24N$ . In contrast, the base model Qwen2.5-VL-32B-Instruct incorrectly concludes that the contact force equals the full weightTable 4: Performance comparison across different disciplines in MMK12. Bold indicates the top performer with the open-source models, while underline indicates the second best performer within open-source models.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Model&lt;/th>\n&lt;th>Mathematics&lt;/th>\n&lt;th>Physics&lt;/th>\n&lt;th>Chemistry&lt;/th>\n&lt;th>Biology&lt;/th>\n&lt;th>Avg.&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td colspan=\"6\">&lt;b>Closed-Source Models&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Claude3.7-Sonnet&lt;/td>\n&lt;td>57.4&lt;/td>\n&lt;td>53.4&lt;/td>\n&lt;td>55.4&lt;/td>\n&lt;td>55.0&lt;/td>\n&lt;td>55.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GPT-4o&lt;/td>\n&lt;td>55.8&lt;/td>\n&lt;td>41.2&lt;/td>\n&lt;td>47.0&lt;/td>\n&lt;td>55.4&lt;/td>\n&lt;td>49.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>o1&lt;/td>\n&lt;td>81.6&lt;/td>\n&lt;td>68.8&lt;/td>\n&lt;td>71.4&lt;/td>\n&lt;td>74.0&lt;/td>\n&lt;td>73.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Gemini2-flash&lt;/td>\n&lt;td>76.8&lt;/td>\n&lt;td>53.6&lt;/td>\n&lt;td>64.6&lt;/td>\n&lt;td>66.0&lt;/td>\n&lt;td>65.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"6\">&lt;b>Open-Source General Models&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>InternVL2.5-VL-8B&lt;/td>\n&lt;td>46.8&lt;/td>\n&lt;td>35.0&lt;/td>\n&lt;td>50.0&lt;/td>\n&lt;td>50.8&lt;/td>\n&lt;td>45.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen-2.5-VL-7B&lt;/td>\n&lt;td>58.4&lt;/td>\n&lt;td>45.4&lt;/td>\n&lt;td>56.4&lt;/td>\n&lt;td>54.0&lt;/td>\n&lt;td>53.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>InternVL2.5-VL-38B&lt;/td>\n&lt;td>61.6&lt;/td>\n&lt;td>49.8&lt;/td>\n&lt;td>60.4&lt;/td>\n&lt;td>60.0&lt;/td>\n&lt;td>58.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen-2.5-VL-32B&lt;/td>\n&lt;td>71.6&lt;/td>\n&lt;td>59.4&lt;/td>\n&lt;td>69.6&lt;/td>\n&lt;td>66.6&lt;/td>\n&lt;td>66.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>InternVL2.5-VL-78B&lt;/td>\n&lt;td>59.8&lt;/td>\n&lt;td>53.2&lt;/td>\n&lt;td>68.0&lt;/td>\n&lt;td>65.2&lt;/td>\n&lt;td>61.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen-2.5-VL-72B&lt;/td>\n&lt;td>&lt;b>75.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>64.8&lt;/b>&lt;/td>\n&lt;td>69.6&lt;/td>\n&lt;td>72.0&lt;/td>\n&lt;td>70.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"6\">&lt;b>Open-Source Reasoning Models&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>InternVL2.5-8B-MPO&lt;/td>\n&lt;td>26.6&lt;/td>\n&lt;td>25.0&lt;/td>\n&lt;td>42.4&lt;/td>\n&lt;td>44.0&lt;/td>\n&lt;td>34.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>InternVL2.5-38B-MPO&lt;/td>\n&lt;td>41.4&lt;/td>\n&lt;td>42.8&lt;/td>\n&lt;td>55.8&lt;/td>\n&lt;td>53.2&lt;/td>\n&lt;td>48.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>QVQ-72B-Preview&lt;/td>\n&lt;td>61.4&lt;/td>\n&lt;td>57.4&lt;/td>\n&lt;td>62.6&lt;/td>\n&lt;td>64.4&lt;/td>\n&lt;td>61.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Adora&lt;/td>\n&lt;td>63.6&lt;/td>\n&lt;td>50.6&lt;/td>\n&lt;td>59.0&lt;/td>\n&lt;td>59.0&lt;/td>\n&lt;td>58.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>R1-Onevision&lt;/td>\n&lt;td>44.8&lt;/td>\n&lt;td>33.8&lt;/td>\n&lt;td>39.8&lt;/td>\n&lt;td>40.8&lt;/td>\n&lt;td>39.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>OpenVLThinker-7&lt;/td>\n&lt;td>63.0&lt;/td>\n&lt;td>53.8&lt;/td>\n&lt;td>60.6&lt;/td>\n&lt;td>65.0&lt;/td>\n&lt;td>60.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"6\">&lt;b>Ours&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MM-Eureka-7B&lt;/td>\n&lt;td>71.2&lt;/td>\n&lt;td>56.2&lt;/td>\n&lt;td>65.2&lt;/td>\n&lt;td>65.2&lt;/td>\n&lt;td>64.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MM-Eureka-32B&lt;/td>\n&lt;td>&lt;u>74.6&lt;/u>&lt;/td>\n&lt;td>&lt;u>62.0&lt;/u>&lt;/td>\n&lt;td>&lt;b>75.4&lt;/b>&lt;/td>\n&lt;td>&lt;b>76.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>72.2&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nof object B (i.e.,  $40N$ ), failing to consider the transient acceleration of the system and misapplying Newtonian mechanics.\n\nThese examples highlight MM-Eureka’s improved ability to perform reasoning and its potential to generalize reasoning patterns across disciplines. Further cases in mathematics, chemistry, and biology show similar trends, where our model more effectively breaks down problems into intermediate steps and synthesizes knowledge to reach accurate conclusions.\n\n## 6 DISCUSSION\n\n### 6.1 ARE KNOWLEDGE AND REASONING DECOUPLED?\n\nFigure 4 presents the distribution of correct answers across 8 responses from the Qwen-2.5-VL-32B and MM-Eureka-32B models on the Mathematics dataset. It is evident that, for problems that were initially answered correctly at least once, Eureka shows a significant improvement in accuracy. However, the number of problems that initially had zero correct answers remains nearly unchanged. We hypothesize that this improvement is due to Eureka’s improved reasoning capabilities, developed through RL training, allowing it to better leverage existing knowledge and thus improve the accuracy on partially understood problems. Nonetheless, relying solely on reasoning is insufficient to solve problems the model originally cannot answer, which is why the accuracy for problems with zero correct answers remains almost unchanged.\n\nFigure ?? shows the responses from Qwen-2.5-VL-32B and MM-Eureka-32B to the same question from Mathematics (the full version is provided in Appendix). From the responses, we observe that although Qwen possesses the necessary knowledge to answer the question, it still struggles to provide the correct answer. In contrast, Eureka is able to better reason with the available knowledge and derive the correct answer. Table 5 further illustrates that, despite Eureka’s training set beingFigure 4: Distribution of correct answers across 8 responses from Qwen-2.5-VL-32B and MM-Eureka-32B on *Mathematics*.\n\nfocused only on mathematics, it also demonstrates a notable improvement in answering questions from other domains such as physics, chemistry, and biology.\n\nOur experimental results to some extent support the view that knowledge and reasoning in LLMs/VLMs can be decoupled, and to some extent indicate that learning knowledge and learning reasoning can be conducted separately during the training process. Therefore, a key direction for future research is to explore how to generalize the reasoning capabilities, developed from data like mathematics—where logic is clear, responses are structured, and answers are verifiable—into broader, more general domains.\n\n## 6.2 RL GENERALIZES BETTER THAN SFT\n\nWe maintain consistent settings with our RL training to compare different post-training strategies including SFT and COT SFT. Using the ms-swift framework (Zhao et al., 2024), we conduct both SFT and COT SFT training for 10 epochs with identical data. As shown in Table 5, results demonstrate that RL exhibits superior generalization compared to SFT or COT SFT approaches, particularly with more significant improvements on OOD test sets such as Physics, Chemistry, and Biology. Furthermore, RL enhances the model’s reasoning capabilities more effectively—while SFT and COT SFT fail to substantially improve performance on mathematics and physics problems, RL training increases the model’s scores in mathematics and physics by 12.8 and 10.8 points respectively.\n\nTable 5: Performance comparison of different training methods on MMK12. In terms of both enhancing mathematical capabilities and generalizing to other disciplines, RL significantly outperforms SFT or COT SFT.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Model&lt;/th>\n&lt;th>Mathematics&lt;/th>\n&lt;th>Physics&lt;/th>\n&lt;th>Chemistry&lt;/th>\n&lt;th>Biology&lt;/th>\n&lt;th>Avg.&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Qwen-2.5-VL-7B&lt;/td>\n&lt;td>58.4&lt;/td>\n&lt;td>45.4&lt;/td>\n&lt;td>56.4&lt;/td>\n&lt;td>54.0&lt;/td>\n&lt;td>53.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>+ SFT&lt;/td>\n&lt;td>56.6&lt;/td>\n&lt;td>50.0&lt;/td>\n&lt;td>63.2&lt;/td>\n&lt;td>61.2&lt;/td>\n&lt;td>57.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>+ COT SFT&lt;/td>\n&lt;td>59.2&lt;/td>\n&lt;td>46.0&lt;/td>\n&lt;td>62.2&lt;/td>\n&lt;td>61.2&lt;/td>\n&lt;td>57.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>+ RL&lt;/td>\n&lt;td>&lt;b>71.2&lt;/b>&lt;/td>\n&lt;td>&lt;b>56.2&lt;/b>&lt;/td>\n&lt;td>&lt;b>65.2&lt;/b>&lt;/td>\n&lt;td>&lt;b>65.0&lt;/b>&lt;/td>\n&lt;td>&lt;b>64.5&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n## 6.3 TWO-STAGE TRAINING\n\nIn Section 4.5, we introduce a two-stage RL training strategy. Stage 1 employs K12 data to enhance general knowledge reasoning capabilities, while stage 2 utilizes Geo3k data to address specific performance gaps. Additionally, we omit the KL divergence in stage one to accelerate training and then incorporate it in stage two to maintain training stability.Figure 5: (a) MM-Eureka-32B tends to experience sudden training collapse during RL training, manifested as accuracy reward approaching zero. (b) During the second training phase, adding KL divergence leads to more stable training with steadily increasing accuracy rewards. (c) The stabilizing effect of KL divergence in the second phase may be attributed to the stabilization of the policy ratio, as ratio instability often leads to training collapse.\n\nAs shown in Figure 5 (a), continuous training without KL divergence often leads to sudden model collapse. We identify this phenomenon results from ratio instability (excessive updates in the new policy). As shown in Figures 5 (b) and (c), which present training metrics with and without the use of KL divergence in the second stage, a sharp fluctuation in the ratio is observed when the model begins to collapse. To mitigate this issue of ratio instability, we introduce a KL divergence term during the second stage of training, which helps to stabilize the learning dynamics.\n\nFurthermore, Table 6 demonstrates that after the first training stage, despite overall performance improvements, capabilities in certain specific domains actually decline, as evidenced by MathVista’s geometry problem solving(GPS) score dropping from 74.0 to 56.7. To address this, we implement second-stage training using Geo3k, which yields further improvements across multiple mathematical benchmarks.\n\nTable 6: Performance comparison across multimodal mathematical benchmarks of the two stage training strategy. The second phase of training enhances various capabilities of the model following the first phase, with particularly significant improvements in geometric reasoning abilities.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Model&lt;/th>\n&lt;th>Data Scale&lt;/th>\n&lt;th>MathVista&lt;/th>\n&lt;th>MathVista(GPS)&lt;/th>\n&lt;th>MathVerse&lt;/th>\n&lt;th>Mathvision&lt;/th>\n&lt;th>WeMath&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Stage1&lt;/td>\n&lt;td>15k&lt;/td>\n&lt;td>72.0&lt;/td>\n&lt;td>56.7&lt;/td>\n&lt;td>56.4&lt;/td>\n&lt;td>33.6&lt;/td>\n&lt;td>&lt;b>73.5&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Stage2&lt;/td>\n&lt;td>2k&lt;/td>\n&lt;td>&lt;b>74.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>70.2&lt;/b>&lt;/td>\n&lt;td>&lt;b>56.5&lt;/b>&lt;/td>\n&lt;td>&lt;b>34.4&lt;/b>&lt;/td>\n&lt;td>73.4&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n## 7 CONCLUSION\n\nOur work aims at developing a powerful model for multimodal reasoning. To achieve this, we first propose MMK12, which is a high quality multimodal reasoning mathematical dataset collected by ourselves. Moreover, we utilize online filter and propose a two-stage training strategy to make the rule-based reinforcement learning training more stable and efficient. Finally, we propose MM-Eureka-7B and MM-Eureka-32B, both are the top performers within the similar size models in multimodal reasoning tasks. Especially for multidisciplinary reasoning tasks, MM-Eureka-32B surpasses almost all open-source models and closed-source models, which is only slightly behind o1.\n\n## 8 ACKNOWLEDGEMENTS\n\nWe acknowledge the outstanding open-source contributions from vLLM, LMM-R1, and Open-RLHF. We also extend our gratitude to DeepSeek-R1, InternVL, and QwenVL for their open-source techniques and base models, which have enabled us to further our exploration.\n\n## REFERENCES\n\nArash Ahmadian, Chris Cremer, Matthias Gallé, Marzieh Fadaee, Julia Kreutzer, Olivier Pietquin, Ahmet Üstün, and Sara Hooker. Back to basics: Revisiting reinforce-style optimization for learning from human feedback in llms. In *Proceedings of the 62nd Annual Meeting of the Association*for *Computational Linguistics (Volume 1: Long Papers)*, ACL 2024, pp. 12248–12267. Association for Computational Linguistics, 2024.\n\nAnthropic. Claude 3.7 sonnet. &lt;https://www.anthropic.com/claude>, 2024. Accessed: 2025-04-14.\n\nJinze Bai, Shuai Bai, Shusheng Yang, Shijie Wang, Sinan Tan, Peng Wang, Junyang Lin, Chang Zhou, and Jingren Zhou. Qwen-vl: A versatile vision-language model for understanding, localization, text reading, and beyond, 2023. URL &lt;https://arxiv.org/abs/2308.12966>.\n\nLiang Chen, Lei Li, Haozhe Zhao, Yifan Song, and Vinci. R1-v: Reinforcing super generalization ability in vision-language models with less than \\$3. &lt;https://github.com/Deep-Agent/R1-V>, 2025. Accessed: 2025-02-02.\n\nZhe Chen, Weiyun Wang, Yue Cao, Yangzhou Liu, Zhangwei Gao, Erfei Cui, Jinguo Zhu, Shenglong Ye, Hao Tian, Zhaoyang Liu, et al. Expanding performance boundaries of open-source multimodal models with model, data, and test-time scaling. *arXiv preprint arXiv:2412.05271*, 2024.\n\nGanqu Cui, Lifan Yuan, Zefan Wang, Hanbin Wang, Wendi Li, Bingxiang He, Yuchen Fan, Tianyu Yu, Qixin Xu, Weize Chen, Jiarui Yuan, Huayu Chen, Kaiyan Zhang, Xingtai Lv, Shuo Wang, Yuan Yao, Xu Han, Hao Peng, Yu Cheng, Zhiyuan Liu, Maosong Sun, Bowen Zhou, and Ning Ding. Process reinforcement through implicit rewards, 2025. URL &lt;https://arxiv.org/abs/2502.01456>.\n\nDeepSeek-AI, Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, Xiaokang Zhang, Xingkai Yu, Yu Wu, Z. F. Wu, Zhibin Gou, Zhihong Shao, Zhuoshu Li, Ziyi Gao, Aixin Liu, Bing Xue, Bingxuan Wang, Bochao Wu, Bei Feng, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chenyu Zhang, Chong Ruan, Damai Dai, Deli Chen, Dongjie Ji, Erhang Li, Fangyun Lin, Fucong Dai, Fuli Luo, Guangbo Hao, Guanting Chen, Guowei Li, H. Zhang, Han Bao, Hanwei Xu, Haocheng Wang, Honghui Ding, Huajian Xin, Huazuo Gao, Hui Qu, Hui Li, Jianzhong Guo, Jiashi Li, Jiawei Wang, Jingchang Chen, Jingyang Yuan, Junjie Qiu, Junlong Li, J. L. Cai, Jiaqi Ni, Jian Liang, Jin Chen, Kai Dong, Kai Hu, Kaige Gao, Kang Guan, Kexin Huang, Kuai Yu, Lean Wang, Lecong Zhang, Liang Zhao, Litong Wang, Liyue Zhang, Lei Xu, Leyi Xia, Mingchuan Zhang, Minghua Zhang, Minghui Tang, Meng Li, Miaojun Wang, Mingming Li, Ning Tian, Panpan Huang, Peng Zhang, Qiancheng Wang, Qinyu Chen, Qiushi Du, Ruiqi Ge, Ruisong Zhang, Ruizhe Pan, Runji Wang, R. J. Chen, R. L. Jin, Ruyi Chen, Shanghao Lu, Shangyan Zhou, Shanhuang Chen, Shengfeng Ye, Shiyu Wang, Shuiping Yu, Shunfeng Zhou, Shuting Pan, S. S. Li, Shuang Zhou, Shaoqing Wu, Shengfeng Ye, Tao Yun, Tian Pei, Tianyu Sun, T. Wang, Wangding Zeng, Wanjia Zhao, Wen Liu, Wenfeng Liang, Wenjun Gao, Wenqin Yu, Wentao Zhang, W. L. Xiao, Wei An, Xiaodong Liu, Xiaohan Wang, Xiaokang Chen, Xiaotao Nie, Xin Cheng, Xin Liu, Xin Xie, Xingchao Liu, Xinyu Yang, Xinyuan Li, Xuecheng Su, Xuheng Lin, X. Q. Li, Xiangyue Jin, Xiaojin Shen, Xiaosha Chen, Xiaowen Sun, Xiaoxiang Wang, Xinnan Song, Xinyi Zhou, Xianzu Wang, Xinxia Shan, Y. K. Li, Y. Q. Wang, Y. X. Wei, Yang Zhang, Yanhong Xu, Yao Li, Yao Zhao, Yaofeng Sun, Yaohui Wang, Yi Yu, Yichao Zhang, Yifan Shi, Yiliang Xiong, Ying He, Yishi Piao, Yisong Wang, Yixuan Tan, Yiyang Ma, Yiyuan Liu, Yongqiang Guo, Yuan Ou, Yuduan Wang, Yue Gong, Yuheng Zou, Yujia He, Yunfan Xiong, Yuxiang Luo, Yuxiang You, Yuxuan Liu, Yuyang Zhou, Y. X. Zhu, Yanhong Xu, Yanping Huang, Yaohui Li, Yi Zheng, Yuchen Zhu, Yunxian Ma, Ying Tang, Yukun Zha, Yuting Yan, Z. Z. Ren, Zehui Ren, Zhangli Sha, Zhe Fu, Zhean Xu, Zhenda Xie, Zhengyan Zhang, Zhewen Hao, Zhicheng Ma, Zhigang Yan, Zhiyu Wu, Zihui Gu, Zijia Zhu, Zijun Liu, Zilin Li, Ziwei Xie, Ziyang Song, Zizheng Pan, Zhen Huang, Zhipeng Xu, Zhongyu Zhang, and Zhen Zhang. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning, 2025. URL &lt;https://arxiv.org/abs/2501.12948>.\n\nLinger Deng, Yuliang Liu, Bohan Li, Dongliang Luo, Liang Wu, Chengquan Zhang, Pengyuan Lyu, Ziyang Zhang, Gang Zhang, Errui Ding, et al. R-cot: Reverse chain-of-thought problem generation for geometric reasoning in large multimodal models. *arXiv preprint arXiv:2410.17885*, 2024.Yihe Deng, Hritik Bansal, Fan Yin, Nanyun Peng, Wei Wang, and Kai-Wei Chang. Openvlthinker: An early exploration to complex vision-language reasoning via iterative self-improvement, 2025. URL &lt;https://arxiv.org/abs/2503.17352>.\n\nHaodong Duan, Junming Yang, Yuxuan Qiao, Xinyu Fang, Lin Chen, Yuan Liu, Xiaoyi Dong, Yuhang Zang, Pan Zhang, Jiaqi Wang, et al. Vlmevalkit: An open-source toolkit for evaluating large multi-modality models. In *Proceedings of the 32nd ACM international conference on multimedia*, pp. 11198–11201, 2024.\n\nLeo Gao, John Schulman, and Jacob Hilton. Scaling laws for reward model overoptimization, 2022. URL &lt;https://arxiv.org/abs/2210.10760>.\n\nLujun Gui and Qingnan Ren. Training reasoning model with dynamic advantage estimation on reinforcement learning. [https://www.notion.so/Training\\\\_Reasoning\\\\_Model\\\\_with\\\\_Dynamic\\\\_Advantage\\\\_Estimation\\\\_on\\\\_Reinforcement\\\\_Learning\\\\_1a830cc0904681fa9df3e076b6557a3e](https://www.notion.so/Training_Reasoning_Model_with_Dynamic_Advantage_Estimation_on_Reinforcement_Learning_1a830cc0904681fa9df3e076b6557a3e), 2025. Notion Blog.\n\nJarvis Guo, Tuney Zheng, Yuelin Bai, Bo Li, Yubo Wang, King Zhu, Yizhi Li, Graham Neubig, Wenhu Chen, and Xiang Yue. Mammoth-vl: Eliciting multimodal reasoning with instruction tuning at scale, 2024. URL &lt;https://arxiv.org/abs/2412.05237>.\n\nChaoqun He, Renjie Luo, Yuzhuo Bai, Shengding Hu, Zhen Leng Thai, Junhao Shen, Jinyi Hu, Xu Han, Yujie Huang, Yuxiang Zhang, Jie Liu, Lei Qi, Zhiyuan Liu, and Maosong Sun. Olympiadbench: A challenging benchmark for promoting agi with olympiad-level bilingual multimodal scientific problems, 2024. URL &lt;https://arxiv.org/abs/2402.14008>.\n\nJian Hu. Reinforce++: A simple and efficient approach for aligning large language models. *arXiv preprint arXiv:2501.03262*, 2025.\n\nJian Hu, Xibin Wu, Zilin Zhu, Xianyu, Weixun Wang, Dehao Zhang, and Yu Cao. Openrlhf: An easy-to-use, scalable and high-performance rlhf framework, 2024. URL &lt;https://arxiv.org/abs/2405.11143>.\n\nAaron Hurst, Adam Lerer, Adam P Goucher, Adam Perelman, Aditya Ramesh, Aidan Clark, AJ Ostrow, Akila Welihinda, Alan Hayes, Alec Radford, et al. Gpt-4o system card. *arXiv preprint arXiv:2410.21276*, 2024.\n\nWouter Kool, Herke van Hoof, and Max Welling. Buy 4 REINFORCE samples, get a baseline for free! In *Deep Reinforcement Learning Meets Structured Prediction, ICLR 2019 Workshop*. OpenReview.net, 2019.\n\nWoosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E. Gonzalez, Hao Zhang, and Ion Stoica. Efficient memory management for large language model serving with pagedattention. In *Proceedings of the ACM SIGOPS 29th Symposium on Operating Systems Principles*, 2023.\n\nPan Lu, Ran Gong, Shibiao Jiang, Liang Qiu, Siyuan Huang, Xiaodan Liang, and Song-Chun Zhu. Inter-gps: Interpretable geometry problem solving with formal language and symbolic reasoning. *arXiv preprint arXiv:2105.04165*, 2021.\n\nPan Lu, Hritik Bansal, Tony Xia, Jiacheng Liu, Chunyuan Li, Hannaneh Hajishirzi, Hao Cheng, Kai-Wei Chang, Michel Galley, and Jianfeng Gao. Mathvista: Evaluating mathematical reasoning of foundation models in visual contexts, 2024. URL &lt;https://arxiv.org/abs/2310.02255>.\n\nOpenAI. Introducing openai o1. &lt;https://openai.com/o1/>, 2024. Accessed: 2024-10-02.\n\nLong Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser Kelton, Luke Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul Christiano, Jan Leike, and Ryan Lowe. Training language models to follow instructions with human feedback, 2022. URL &lt;https://arxiv.org/abs/2203.02155>.Shuai Peng, Di Fu, Liangcai Gao, Xiuqin Zhong, Hongguang Fu, and Zhi Tang. Multi-math: Bridging visual and mathematical reasoning for large language models. *arXiv preprint arXiv:2409.00147*, 2024.\n\nYingZhe Peng, Gongrui Zhang, Xin Geng, and Xu Yang. Lmm-r1. &lt;https://github.com/TideDra/lmm-r1>, 2025. Accessed: 2025-02-13.\n\nRunqi Qiao, Qiuna Tan, Guanting Dong, Minhui Wu, Chong Sun, Xiaoshuai Song, Zhuoma Gongque, Shanglin Lei, Zhe Wei, Miaoxuan Zhang, Runfeng Qiao, Yifan Zhang, Xiao Zong, Yida Xu, Muxi Diao, Zhimin Bao, Chen Li, and Honggang Zhang. We-math: Does your large multimodal model achieve human-like mathematical reasoning? *CoRR*, abs/2407.01284, 2024. doi: 10.48550/ARXIV.2407.01284. URL &lt;https://doi.org/10.48550/arXiv.2407.01284>.\n\nAlec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, Ilya Sutskever, et al. Language models are unsupervised multitask learners. *OpenAI blog*, 1(8):9, 2019.\n\nRafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and Chelsea Finn. Direct preference optimization: Your language model is secretly a reward model. *Advances in Neural Information Processing Systems*, 36:53728–53741, 2023.\n\nJohn Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms, 2017a. URL &lt;https://arxiv.org/abs/1707.06347>.\n\nJohn Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. *arXiv preprint arXiv:1707.06347*, 2017b.\n\nRichard S Sutton, Andrew G Barto, et al. *Reinforcement learning: An introduction*, volume 1. MIT press Cambridge, 1998.\n\nHuajie Tan, Yuheng Ji, Xiaoshuai Hao, Minglan Lin, Pengwei Wang, Zhongyuan Wang, and Shanghang Zhang. Reason-rft: Reinforcement fine-tuning for visual reasoning, 2025. URL &lt;https://arxiv.org/abs/2503.20752>.\n\nGemini Team, Rohan Anil, Sebastian Borgeaud, Jean-Baptiste Alayrac, Jiahui Yu, Radu Soricut, Johan Schalkwyk, Andrew M Dai, Anja Hauth, Katie Millican, et al. Gemini: a family of highly capable multimodal models. *arXiv preprint arXiv:2312.11805*, 2023.\n\nKimi Team, Angang Du, Bofei Gao, Bowei Xing, Changjiu Jiang, Cheng Chen, Cheng Li, Chenjun Xiao, Chenzhuang Du, Chonghua Liao, Chuning Tang, Congcong Wang, Dehao Zhang, Enming Yuan, Enzhe Lu, Fengxiang Tang, Flood Sung, Guangda Wei, Guokun Lai, Haiqing Guo, Han Zhu, Hao Ding, Hao Hu, Hao Yang, Hao Zhang, Haotian Yao, Haotian Zhao, Haoyu Lu, Haoze Li, Haozhen Yu, Hongcheng Gao, Huabin Zheng, Huan Yuan, Jia Chen, Jianhang Guo, Jianlin Su, Jianzhou Wang, Jie Zhao, Jin Zhang, Jingyuan Liu, Junjie Yan, Junyan Wu, Lidong Shi, Ling Ye, Longhui Yu, Mengnan Dong, Neo Zhang, Ningchen Ma, Qiwei Pan, Qucheng Gong, Shaowei Liu, Shengling Ma, Shupeng Wei, Sihan Cao, Siying Huang, Tao Jiang, Weihao Gao, Weimin Xiong, Weiran He, Weixiao Huang, Wenhao Wu, Wenyang He, Xianghui Wei, Xianqing Jia, Xingzhe Wu, Xinran Xu, Xinxing Zu, Xinyu Zhou, Xuehai Pan, Y. Charles, Yang Li, Yangyang Hu, Yangyang Liu, Yanru Chen, Yejie Wang, Yibo Liu, Yidao Qin, Yifeng Liu, Ying Yang, Yiping Bao, Yulun Du, Yuxin Wu, Yuzhi Wang, Zaida Zhou, Zhaoji Wang, Zhaowei Li, Zhen Zhu, Zheng Zhang, Zhexu Wang, Zhilin Yang, Zhiqi Huang, Zihao Huang, Ziyao Xu, and Zonghan Yang. Kimi k1.5: Scaling reinforcement learning with llms, 2025a. URL &lt;https://arxiv.org/abs/2501.12599>.\n\nKimi Team, Angang Du, Bohong Yin, Bowei Xing, Bowen Qu, Bowen Wang, Cheng Chen, Chenlin Zhang, Chenzhuang Du, Chu Wei, Congcong Wang, Dehao Zhang, Dikang Du, Dongliang Wang, Enming Yuan, Enzhe Lu, Fang Li, Flood Sung, Guangda Wei, Guokun Lai, Han Zhu, Hao Ding, Hao Hu, Hao Yang, Hao Zhang, Haoning Wu, Haotian Yao, Haoyu Lu, Heng Wang, Hongcheng Gao, Huabin Zheng, Jiaming Li, Jianlin Su, Jianzhou Wang, Jiaqi Deng, Jiezhong Qiu, Jin Xie, Jinhong Wang, Jingyuan Liu, Junjie Yan, Kun Ouyang, Liang Chen, Lin Sui, Longhui Yu, Mengfan Dong, Mengnan Dong, Nuo Xu, Pengyu Cheng, Qizheng Gu, Runjie Zhou, Shaowei Liu, Sihan Cao, Tao Yu, Tianhui Song, Tongtong Bai, Wei Song, Weiran He, Weixiao Huang, WeixinXu, Xiaokun Yuan, Xingcheng Yao, Xingzhe Wu, Xinxing Zu, Xinyu Zhou, Xinyuan Wang, Y. Charles, Yan Zhong, Yang Li, Yangyang Hu, Yanru Chen, Yejie Wang, Yibo Liu, Yibo Miao, Yidao Qin, Yimin Chen, Yiping Bao, Yiqin Wang, Yongsheng Kang, Yuanxin Liu, Yulun Du, Yuxin Wu, Yuzhi Wang, Yuzi Yan, Zaida Zhou, Zhaowei Li, Zhejun Jiang, Zheng Zhang, Zhilin Yang, Zhiqi Huang, Zihao Huang, Zijia Zhao, and Ziwei Chen. Kimi-VL technical report, 2025b. URL &lt;https://arxiv.org/abs/2504.07491>.\n\nQwen Team. Qvq: To see the world with wisdom, December 2024. URL &lt;https://qwenlm.github.io/blog/qvq-72b-preview/>.\n\nKe Wang, Junting Pan, Weikang Shi, Zimu Lu, Mingjie Zhan, and Hongsheng Li. Measuring multimodal mathematical reasoning with math-vision dataset, 2024a. URL &lt;https://arxiv.org/abs/2402.14804>.\n\nWeiyun Wang, Zhe Chen, Wenhai Wang, Yue Cao, Yangzhou Liu, Zhangwei Gao, Jinguo Zhu, Xizhou Zhu, Lewei Lu, Yu Qiao, and Jifeng Dai. Enhancing the reasoning ability of multimodal large language models via mixed preference optimization, 2024b. URL &lt;https://arxiv.org/abs/2411.10442>.\n\nYi Yang, Xiaoxuan He, Hongkun Pan, Xiyuan Jiang, Yan Deng, Xingtao Yang, Haoyu Lu, Dacheng Yin, Fengyun Rao, Minfeng Zhu, Bo Zhang, and Wei Chen. R1-onevision: Advancing generalized multimodal reasoning through cross-modal formalization. *arXiv preprint arXiv:2503.10615*, 2025.\n\nRenrui Zhang, Dongzhi Jiang, Yichi Zhang, Haokun Lin, Ziyu Guo, Pengshuo Qiu, Aojun Zhou, Pan Lu, Kai-Wei Chang, Peng Gao, and Hongsheng Li. Mathverse: Does your multi-modal llm truly see the diagrams in visual math problems?, 2024a. URL &lt;https://arxiv.org/abs/2403.14624>.\n\nRenrui Zhang, Xinyu Wei, Dongzhi Jiang, Ziyu Guo, Shicheng Li, Yichi Zhang, Chengzhuo Tong, Jiaming Liu, Aojun Zhou, Bin Wei, et al. Mavis: Mathematical visual instruction tuning with an automatic data engine. *arXiv preprint arXiv:2407.08739*, 2024b.\n\nYuze Zhao, Jintao Huang, Jinghan Hu, Xingjun Wang, Yunlin Mao, Daoze Zhang, Zeyinzi Jiang, Zhikai Wu, Baole Ai, Ang Wang, Wenmeng Zhou, and Yingda Chen. Swift: a scalable lightweight infrastructure for fine-tuning, 2024. URL &lt;https://arxiv.org/abs/2408.05517>.## A APPENDIX: QUALITATIVE ANALYSIS\n\n**Question:**\n\nAs shown in the figure, in the straight square column  $ABCD - A_1B_1C_1D_1$ ,  $\\angle ADC = 90^\\circ$ , and  $AA_1 = AD = DC = 1$ ,  $M \\in \\text{plane } ABCD$ , when  $D_1M \\perp \\text{plane } A_1C_1D$ ,  $D_1M = \\dots$\n\n**Answer:**  $\\sqrt{3}$\n\n**Qwen2.5-VL-32B-Instruct**\n\nTo solve the problem, we need to determine the length of  $D_1M$ , where  $M$  is a point in the plane  $ABCD$  such that  $D_1M \\perp \\text{plane } A_1C_1D$ .\n\n**2. Coordinates of Points:** Place the prism in a 3D Cartesian coordinate system:\n\n$$A = (0, 0, 0), \\quad B = (1, 0, 0), \\quad C = (1, 1, 0), \\quad D = (0, 1, 0)$$\n\n$$A_1 = (0, 0, 1), \\quad B_1 = (1, 0, 1), \\quad C_1 = (1, 1, 1), \\quad D_1 = (0, 1, 1)$$\n\nLet  $M = (x, y, 0)$ , where  $M$  is in the plane  $ABCD$ .\n\n**3. Vector Representation:**  $\\vec{D_1M} = (x - 0, y - 1, 0 - 1) = (x, y - 1, -1)$\n\n**4. Condition for Perpendicularity:** For  $D_1M \\perp \\text{plane } A_1C_1D$ , the vector  $\\vec{D_1M}$  must be perpendicular to the normal vector of the plane  $A_1C_1D$ .\n\nFirst, find two non-parallel vectors in the plane  $A_1C_1D$ :\n\nTherefore, the length of  $D_1M$  is  $\\frac{\\sqrt{6}}{2}$ .\n\n**MM-EUREKA-32B**\n\nTo solve the problem, we need to determine the length of  $D_1M$  when  $D_1M \\perp \\text{plane } A_1C_1D$ . Let's break the problem into steps:\n\n**2. Determination of the plane  $A_1C_1D$ :**\n\n- The points  $A_1 = (1, 0, 1)$ ,  $C_1 = (0, 1, 1)$ , and  $D = (0, 0, 0)$  lie in the plane  $A_1C_1D$ .\n- To find the normal vector to the plane  $A_1C_1D$ , we use the cross product of two vectors in the plane:\n\n$$\\vec{A_1D} = (1 - 0, 0 - 0, 1 - 0) = (1, 0, 1), \\quad \\vec{C_1D} = (0 - 0, 1 - 0, 1 - 0) = (0, 1, 1).$$\n\n- The normal vector  $\\mathbf{n}$  to the plane is given by the cross product:\n\n$$\\mathbf{n} = \\vec{A_1D} \\times \\vec{C_1D} = \\begin{vmatrix} \\mathbf{i} & \\mathbf{j} & \\mathbf{k} \\\\ 1 & 0 & 1 \\\\ 0 & 1 & 1 \\end{vmatrix} = \\mathbf{i}(0 \\cdot 1 - 1 \\cdot 1) - \\mathbf{j}(1 \\cdot 1 - 1 \\cdot 0) + \\mathbf{k}(1 \\cdot 1 - 0 \\cdot 0) = (-1, -1, 1).$$\n\n- Thus, the normal vector to the plane  $A_1C_1D$  is  $\\mathbf{n} = (-1, -1, 1)$ .\n\n**3. Condition for  $D_1M \\perp \\text{plane } A_1C_1D$ :**\n\n- Since  $D_1M \\perp \\text{plane } A_1C_1D$ , the vector  $\\vec{D_1M}$  must be parallel to the normal vector  $\\mathbf{n} = (-1, -1, 1)$ .\n- Let  $M = (x, y, 0)$  be a point in the plane  $ABCD$  (since  $M \\in \\text{plane } ABCD$ , the  $z$ -coordinate of  $M$  is 0).\n- The vector  $\\vec{D_1M} = (x - 0, y - 0, 0 - 1) = (x, y, -1)$ .\n\n**4. Calculation of  $D_1M$ :**\n\n- The vector  $\\vec{D_1M} = (1 - 0, 1 - 0, 0 - 1) = (1, 1, -1)$ .\n- The length of  $D_1M$  is given by the magnitude of  $\\vec{D_1M}$ :  $|\\vec{D_1M}| = \\sqrt{1^2 + 1^2 + (-1)^2} = \\sqrt{1 + 1 + 1} = \\sqrt{3}$ .\n\n&lt;answer>The answer is  $\\sqrt{3}$ . &lt;/answer>\n\nFigure 6: Example from mathematics. Red highlights Qwen2.5-VL-32B-Instruct's reasoning errors. Green shows MM-Eureka-32B's correct reasoning.**Question:**\n\nAs shown in the figure, a lightweight spring is placed vertically on a horizontal surface with a mass of  $6\\text{kg}$  object  $A$  resting on its upper end, in a stationary state. Now, a mass of  $4\\text{kg}$  object  $B$  is gently placed on top of object  $A$ , and the spring remains within its elastic limit. Taking  $g$  as  $10\\text{m/s}^2$ , at the moment  $B$  is placed, the magnitude of the force between  $A$  and  $B$  is ( )\n\nA.  $8\\text{N}$  B.  $18\\text{N}$  C.  $24\\text{N}$  D.  $40\\text{N}$\n\n**Answer:** C\n\n**Qwen2.5-VL-32B-Instruct**\n\nTo solve this problem, we need to determine the force between objects  $A$  and  $B$  at the moment  $B$  is placed on top of  $A$ . Let's break it down step by step.\n\n...  \n**4. Force Analysis at the Moment  $B$  is Placed:**\n\n- At the moment  $B$  is placed, the spring has not yet had time to extend further to balance the new total weight. The spring force remains  $60\\text{N}$  (the initial force that balances the weight of  $A$ ).\n- **The net force on  $A$  is the sum of the spring force and the force from  $B$ :  $F_s + F_B = m_A g$ .**\n- Here,  $F_s = 60\\text{N}$  and  $m_A g = 60\\text{N}$ , so:  $60\\text{N} + F_B = 60\\text{N}$ .\n- Solving for  $F_B$ , we get:  $F_B = 0\\text{N}$ .\n\n**5. Re-evaluate the Situation:**\n\n- The above analysis is not correct because we need to consider the instantaneous force between  $A$  and  $B$  due to the sudden addition of  $B$ .\n- **The force between  $A$  and  $B$  is the force  $B$  exerts on  $A$ , which is the weight of  $B$ :  $F_B = m_B g = 4\\text{kg} \\cdot 10\\text{m/s}^2 = 40\\text{N}$ .**\n\n40\n\n**MM-EUREKA-32B**\n\nTo solve this problem, we need to determine the force between objects  $A$  and  $B$  at the moment  $B$  is placed on top of  $A$ . Let's break the problem into steps:\n\n...  \n**4. Applying Newton's Second Law to  $A$**\n\n$$\\begin{aligned} F_{\\text{net}} &= F_B + F_A - F_{\\text{spring}} \\\\ &= F_B + 60 - 60 = F_B. \\end{aligned}$$\n\nThe net force on  $A$  causes an upward acceleration  $a$ , which is the same as the acceleration of  $B$  because they are in contact.\n\n**5. Analyzing the Forces on  $B$**\n\n- The forces on  $B$  are:\n  - The weight of  $B$ :  $F_B = 40\\text{N}$  (downward),\n  - The force from  $A$ :  $F_{\\text{contact}}$  (upward).\n\n**6. Applying Newton's Second Law to  $B$**\n\n$$F_B - F_{\\text{contact}} = m_B a.$$\n\n**7. Finding the Acceleration  $a$**\n\n- The total mass of the system is  $m_{\\text{total}} = m_A + m_B = 6 + 4 = 10\\text{kg}$ .\n- The net force on the system is the extra weight from  $B$ :  $F_{\\text{net, total}} = 40\\text{N}$ .\n- Using Newton's Second Law for the entire system:  $F_{\\text{net, total}} = m_{\\text{total}} a \\Rightarrow 40 = 10a \\Rightarrow a = 4\\text{m/s}^2$ .\n\n**8. Finding the Contact Force  $F_{\\text{contact}}$**\n\n$$\\begin{aligned} F_B - F_{\\text{contact}} &= m_B a \\\\ 40 - F_{\\text{contact}} &= 4 \\cdot 4 = 16 \\\\ F_{\\text{contact}} &= 40 - 16 = 24\\text{N}. \\end{aligned}$$\n\n&lt;answer>The answer is C. &lt;/answer>\n\nFigure 7: Example from physics. Red highlights Qwen2.5-VL-32B-Instruct's reasoning errors. Green shows MM-Eureka-32B's correct reasoning.**Question:**\n\nAt room temperature, a 0.100 mol/L NaOH solution is used to titrate 25.00 mL 0.100 mol/L  $\\text{H}_2\\text{C}_2\\text{O}_4$  solution, and the resulting titration curve is shown in the figure (the volume of the mixed solution can be considered as the sum of the volumes of the solutions before mixing). Which of the following statements is incorrect? ( )\n\n**A.** In the solution at point X:  $c(\\text{Na}^+) > c(\\text{HC}_2\\text{O}_4^-) > c(\\text{C}_2\\text{O}_4^{2-})$   \n**B.** Observing the solution at point Y indicates that the degree of ionization of  $\\text{HC}_2\\text{O}_4^-$  is greater than the degree of hydrolysis of  $\\text{C}_2\\text{O}_4^{2-}$   \n**C.** In the solution at point Z:  $c(\\text{Na}^+) > c(\\text{C}_2\\text{O}_4^{2-}) > c(\\text{HC}_2\\text{O}_4^-) > c(\\text{OH}^-) > c(\\text{H}^+)$   \n**D.** Throughout the titration process:  $c(\\text{Na}^+) + c(\\text{H}_2\\text{C}_2\\text{O}_4) + c(\\text{HC}_2\\text{O}_4^-) + c(\\text{C}_2\\text{O}_4^{2-}) = 0.100\\text{mol/L}$\n\n**Answer:** C\n\n**Qwen2.5-VL-32B-Instruct**\n\n**1. Understanding the Reaction:**\n\n- The titration is between a strong base (0.100 M NaO) and a weak dicarboxylic acid (0.100 M  $\\text{H}_2\\text{CO}_4$ ).\n- The reaction steps are:\n\n1. $\\text{H}_2\\text{CO}_4 + \\text{NaO} \\rightarrow \\text{NaHC}_2\\text{O}_4 + \\text{H}_2\\text{O}$\n2. $\\text{NaHC}_2\\text{O}_4 + \\text{NaO} \\rightarrow \\text{Na}_2\\text{CO}_4 + \\text{H}_2\\text{O}$\n\n**2. Key Points on the pH Curve:**\n\n- **Point X (pH  $\\approx 2$ ):** This is the initial point where only  $\\text{H}_2\\text{CO}_4$  is present. The solution is acidic.\n- **Point Y (pH  $\\approx 5.5$ ):** This is the first equivalence point where all  $\\text{H}_2\\text{CO}_4$  has been neutralized to  $\\text{NaHC}_2\\text{O}_4$  (solutions of  $\\text{NaHC}_2\\text{O}_4$  are acidic due to the protonation of the conjugate base).\n- **Point Z (pH  $\\approx 8.7$ ):** This is the second equivalence point where all  $\\text{NaHC}_2\\text{O}_4$  has been neutralized to  $\\text{Na}_2\\text{CO}_4$  (solutions of  $\\text{Na}_2\\text{CO}_4$  are basic due to the deprotonation of the conjugate base).\n\n**4. Final Answer:** The only option that is **incorrect** is Option A.\n\n**MM-EUREKA-32B**\n\nTo solve this problem, we need to analyze the titration of a weak dicarboxylic acid  $\\text{H}_2\\text{C}_2\\text{O}_4$  (oxalate) with a strong base NaOH. The titration process involves multiple steps, and we must consider the equilibrium and ionic concentrations at different points on the titration curve. Let's break the problem into parts and solve it step by step.\n\n**1. Understanding the titration process:**\n\n$\\text{H}_2\\text{C}_2\\text{O}_4$  is a weak dicarboxylic acid, which undergoes two steps of dissociation:\n\n$$\\begin{aligned}\\text{H}_2\\text{C}_2\\text{O}_4 &\\rightleftharpoons \\text{H}^+ + \\text{HC}_2\\text{O}_4^- \\\\ \\text{HC}_2\\text{O}_4^- &\\rightleftharpoons \\text{H}^+ + \\text{C}_2\\text{O}_4^{2-}\\end{aligned}$$\n\nThe titration is carried out with NaOH, a strong base, which will neutralize the  $\\text{H}^+$  ions step by step.\n\n**2. Key points on the titration curve:**\n\n**Point X:** 25 mL of NaOH added.\n\n- At this point, the first equivalence point is reached. All  $\\text{H}_2\\text{C}_2\\text{O}_4$  is converted to  $\\text{NaHC}_2\\text{O}_4$  (sodium hydrogen oxalate).\n- The solution contains  $\\text{NaHC}_2\\text{O}_4$ , and the pH is around 2, indicating that  $\\text{HC}_2\\text{O}_4^-$  is a weak acid.\n\n**Point Y:** 40 mL of NaOH added.\n\n- This is between the first and second equivalence points. The solution contains a mixture of  $\\text{NaHC}_2\\text{O}_4$  and  $\\text{Na}_2\\text{C}_2\\text{O}_4$ .\n- The pH is 5.5, indicating that the solution is slightly acidic due to the dissociation of  $\\text{HC}_2\\text{O}_4^-$  being greater than the hydrolysis of  $\\text{C}_2\\text{O}_4^{2-}$ .\n\n**Point Z:** 50 mL of NaOH added.\n\n- At this point, the second equivalence point is reached. All  $\\text{H}_2\\text{C}_2\\text{O}_4$  is converted to  $\\text{Na}_2\\text{C}_2\\text{O}_4$  (sodium oxalate).\n- The solution contains  $\\text{Na}_2\\text{C}_2\\text{O}_4$ , and the pH is 8.7, indicating that  $\\text{C}_2\\text{O}_4^{2-}$  is a strong base.\n\n**&lt;answer>**The answer is C. **&lt;/answer>**\n\nFigure 8: Example from chemistry. Red highlights Qwen2.5-VL-32B-Instruct's reasoning errors. Green shows MM-Eureka-32B's correct reasoning.**Question:**\n\nScientists isolated gene A from a certain organism and dissociated it into two single strands. One of these strands was hybridized with the messenger RNA of gene A, resulting in the pattern shown in the image. An unreasonable explanation for this is ( )\n\n- A. Positions 1, 3, 5, and 7 are connected through complementary base pairing\n- B. Heating to a certain temperature can separate the two strands\n- C. The diagram contains 8 types of nucleotides, 5 types of bases, and 2 types of base pairs\n- D. Since fragments 2, 2, and 6 cannot bind with the messenger RNA, fragments 2, 4, and 6 belong to non-gene segments of the DNA molecule\n\n**Answer:** D\n\n**Qwen2.5-VL-32B-Instruct**\n\n...  \n**2. Analyzing Each Option:**\n\n...  \n**Option C: The figure contains 8 types of nucleotides, 5 types of bases, and 2 types of base pairings**\n\n- • In the context of RNA and DNA, there are 4 types of nucleotides in each (A, U, G, C for RNA; A, T, G, C for DNA). When they anneal, the possible base pairings are A-T (or A-U), and G-C. This means there are 4 types of nucleotides per molecule, 5 types of bases (A, T, U, G, C), and 2 types of base pairings (A-T/U, G-C).\n- • **The statement that there are 8 types of nucleotides is unreasonable because there are only 4 types of nucleotides in each (DNA and RNA).**\n\n**Option D: Since segments 2, 4, and 6 cannot bind with the messenger RNA, segments 2, 4, and 6 belong to non-gene segments of the DNA molecule**\n\n- • This is reasonable because segments 2, 4, and 6 do not anneal with the mRNA, which suggests that these segments do not code for the protein and are likely non-coding (non-gene) segments of the DNA.\n\nC\n\n**MM-EUREKA-32B**\n\nTo solve this problem, we need to analyze the image and combine it with the principle of hybridization between DNA and messenger RNA (mRNA). Let's reason step by step:\n\n...  \n**2. Analyzing the options:**\n\n...  \n**C. The image contains 8 types of nucleotides, 5 types of bases, and 2 types of base pairings:**\n\n- • Nucleotides:\n  - – DNA contains 4 types of deoxyribonucleotides (dA, dT, dC, dG)\n  - – mRNA contains 4 types of ribonucleotides (A, U, C, G)\n  - – Total: 8 types of nucleotides.\n- • Bases:\n  - – DNA contains 4 bases (A, T, C, G)\n  - – mRNA contains 4 bases (A, U, C, G)\n  - – Since U replaces T in RNA, there are only 5 distinct bases (A, T/U, C, G).\n- • Base pairing:\n  - – In DNA-mRNA hybridization, the pairings are A-U, T-A, C-G, G-C.\n  - – However, only A-U and C-G actually form during hybridization.\n  - – Thus, only 2 types of base pairings exist.\n\n**D. Since fragments 2, 4, and 6 do not hybridize with mRNA, they belong to non-genic segments of DNA:**\n\n- • The unhybridized regions (2, 4, 6) do not pair with mRNA, but this does not directly imply that they are non-genic segments.\n- • In genomic DNA, unpaired regions could be non-coding parts of a gene (e.g., introns, enhancers), or regulatory regions.\n- • Therefore, we cannot conclude that they are non-genic simply because they do not hybridize.\n\n**3. Conclusion:**\n\n- • Option D is incorrect because we cannot determine from hybridization alone that these regions are non-genic.\n\n&lt;answer>The answer is  D. &lt;/answer>\n\nFigure 9: Example from biology. Red highlights Qwen2.5-VL-32B-Instruct's reasoning errors. Green shows MM-Eureka-32B's correct reasoning.**Question:**\n\nAt room temperature, a 0.100 mol/L NaOH solution is used to titrate 25.00 mL 0.100 mol/L  $\\text{H}_2\\text{C}_2\\text{O}_4$  solution, and the resulting titration curve is shown in the figure (the volume of the mixed solution can be considered as the sum of the volumes of the solutions before mixing).\n\nWhich of the following statements is incorrect? ( )\n\nA. In the solution at point X:  $c(\\text{Na}^+) > c(\\text{HC}_2\\text{O}_4^-) > c(\\text{C}_2\\text{O}_4^{2-})$   \n B. Observing the solution at point Y indicates that the degree of ionization of  $\\text{HC}_2\\text{O}_4^-$  is greater than the degree of hydrolysis of  $\\text{C}_2\\text{O}_4^{2-}$   \n C. In the solution at point Z:  $c(\\text{Na}^+) > c(\\text{C}_2\\text{O}_4^{2-}) > c(\\text{HC}_2\\text{O}_4^-) > c(\\text{OH}^-) > c(\\text{H}^+)$   \n D. Throughout the titration process:  $c(\\text{Na}^+) + c(\\text{H}_2\\text{C}_2\\text{O}_4) + c(\\text{HC}_2\\text{O}_4^-) + c(\\text{C}_2\\text{O}_4^{2-}) = 0.100\\text{mol/L}$\n\nAnswer: C\n\n**Qwen2.5-VL-32B-Instruct**\n\n**1. Understanding the Reaction:**\n\n- The titration is between a strong base (0.100 M NaO) and a weak dicarboxylic acid (0.100 M  $\\text{H}_2\\text{CO}_4$ ).\n- The reaction steps are:\n  1. $\\text{H}_2\\text{CO}_4 + \\text{NaO} \\rightarrow \\text{NaHC}_2\\text{O}_4 + \\text{H}_2\\text{O}$\n  2. $\\text{NaHC}_2\\text{O}_4 + \\text{NaO} \\rightarrow \\text{Na}_2\\text{CO}_4 + \\text{H}_2\\text{O}$\n\n**2. Key Points on the pH Curve:**\n\n- **Point X (pH ≈ 2):** This is the initial point where only  $\\text{H}_2\\text{CO}_4$  is present. The solution is acidic.\n- **Point Y (pH ≈ 5.5):** This is the first equivalence point where all  $\\text{H}_2\\text{CO}_4$  has been neutralized to  $\\text{NaHC}_2\\text{O}_4$  (solutions of  $\\text{NaHC}_2\\text{O}_4$  are acidic due to the protonation of the conjugate base).\n- **Point Z (pH ≈ 8.7):** This is the second equivalence point where all  $\\text{NaHC}_2\\text{O}_4$  has been neutralized to  $\\text{Na}_2\\text{CO}_4$  (solutions of  $\\text{Na}_2\\text{CO}_4$  are basic due to the deprotonation of the conjugate base).\n\n4. Final Answer: The only option that is **incorrect** is Option **A**.\n\n**MM-EUREKA**\n\nTo solve this problem, we need to analyze the titration of a weak dicarboxylic acid  $\\text{H}_2\\text{C}_2\\text{O}_4$  (oxalate) with a strong base NaOH. The titration process involves multiple steps, and we must consider the equilibrium and ionic concentrations at different points on the titration curve. Let's break the problem into parts and solve it step by step.\n\n**1. Understanding the titration process:**\n\n$\\text{H}_2\\text{C}_2\\text{O}_4$  is a weak dicarboxylic acid, which undergoes two steps of dissociation:\n\n$$\\text{H}_2\\text{C}_2\\text{O}_4 \\rightleftharpoons \\text{H}^+ + \\text{HC}_2\\text{O}_4^-$$\n\n$$\\text{HC}_2\\text{O}_4^- \\rightleftharpoons \\text{H}^+ + \\text{C}_2\\text{O}_4^{2-}$$\n\nThe titration is carried out with NaOH, a strong base, which will neutralize the  $\\text{H}^+$  ions step by step.\n\n**2. Key points on the titration curve:**\n\n**Point X:** 25 mL of NaOH added.\n\n- At this point, the first equivalence point is reached. All  $\\text{H}_2\\text{C}_2\\text{O}_4$  is converted to  $\\text{NaHC}_2\\text{O}_4$  (sodium hydrogen oxalate).\n- The solution contains  $\\text{NaHC}_2\\text{O}_4$ , and the pH is around 2, indicating that  $\\text{HC}_2\\text{O}_4^-$  is a weak acid.\n\n**Point Y:** 40 mL of NaOH added.\n\n- This is between the first and second equivalence points. The solution contains a mixture of  $\\text{NaHC}_2\\text{O}_4$  and  $\\text{Na}_2\\text{C}_2\\text{O}_4$ .\n- The pH is 5.5, indicating that the solution is slightly acidic due to the dissociation of  $\\text{HC}_2\\text{O}_4^-$  being greater than the hydrolysis of  $\\text{C}_2\\text{O}_4^{2-}$ .\n\n**Point Z:** 50 mL of NaOH added.\n\n- At this point, the second equivalence point is reached. All  $\\text{H}_2\\text{C}_2\\text{O}_4$  is converted to  $\\text{Na}_2\\text{C}_2\\text{O}_4$  (sodium oxalate).\n- The solution contains  $\\text{Na}_2\\text{C}_2\\text{O}_4$ , and the pH is 8.7, indicating that  $\\text{C}_2\\text{O}_4^{2-}$  is a strong base.\n\n&lt;answer>The answer is **C**. &lt;/answer>\n",
    "durationMs": 672,
    "url": "https://huggingface.co/papers/2503.07365"
  },
  "sourceToolAssistantUUID": "2fecf04b-858d-4325-a197-922048a48455",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-27 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "650c1efe-7c78-4703-a9db-0edfdce5d4a0",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze MM-Eureka multimodal reasoning paper",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6"
}
```

---

### Tool result

_source line 31 · 2026-05-27T16:04:22.160Z_

<details><summary>↩ Tool result · `toolu_01DbzT4gbxGKu5dwfUSimpvE`</summary>

```text
# MM-Eureka Paper Summary

Based on the webpage content provided, here's what's available about this paper:

## Basic Information
- **Title**: MM-Eureka: Exploring the Frontiers of Multimodal Reasoning with Rule-based Reinforcement Learning
- **ArXiv ID**: 2503.07365
- **Published**: March 10, 2025
- **Category**: Computer Vision and Pattern Recognition

## Key Details

**Authors**: Fanqing Meng, Lingxiao Du, Zongkai Liu, and 12 additional researchers

**Overview**: The paper introduces two main contributions—the MMK12 dataset and MM-EUREKA models (7B and 32B parameters). According to the abstract, MM-EUREKA represents "a multimodal model employing rule-based reinforcement learning" designed to advance multimodal reasoning capabilities.

**Motivation**: The authors note that while models like DeepSeek R1 and o1 demonstrated strong text-based reasoning, extending these capabilities to multimodal tasks has been limited by "limited difficulty of selected tasks and relatively small training scales."

**Performance**: The models reportedly "outperform previous powerful models like InternVL2.5-78B or InternVL2.5-38B-MPO" and achieve "competitive or superior performance compared to both open-source and closed-source models."

**Availability**: The complete pipeline, code, models, and data are open-sourced at https://github.com/ModalMinds/MM-EUREKA
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "861f901d-cf4d-4624-8365-5cd34e7deab3",
  "isSidechain": false,
  "promptId": "6e9b4775-3324-430a-aeff-baabf4898966",
  "type": "user",
  "uuid": "8444b6ff-e546-43a9-a447-a0c7a30f82e6",
  "toolUseResult": {
    "bytes": 17672,
    "code": 200,
    "codeText": "OK",
    "result": "# MM-Eureka Paper Summary\n\nBased on the webpage content provided, here's what's available about this paper:\n\n## Basic Information\n- **Title**: MM-Eureka: Exploring the Frontiers of Multimodal Reasoning with Rule-based Reinforcement Learning\n- **ArXiv ID**: 2503.07365\n- **Published**: March 10, 2025\n- **Category**: Computer Vision and Pattern Recognition\n\n## Key Details\n\n**Authors**: Fanqing Meng, Lingxiao Du, Zongkai Liu, and 12 additional researchers\n\n**Overview**: The paper introduces two main contributions—the MMK12 dataset and MM-EUREKA models (7B and 32B parameters). According to the abstract, MM-EUREKA represents \"a multimodal model employing rule-based reinforcement learning\" designed to advance multimodal reasoning capabilities.\n\n**Motivation**: The authors note that while models like DeepSeek R1 and o1 demonstrated strong text-based reasoning, extending these capabilities to multimodal tasks has been limited by \"limited difficulty of selected tasks and relatively small training scales.\"\n\n**Performance**: The models reportedly \"outperform previous powerful models like InternVL2.5-78B or InternVL2.5-38B-MPO\" and achieve \"competitive or superior performance compared to both open-source and closed-source models.\"\n\n**Availability**: The complete pipeline, code, models, and data are open-sourced at https://github.com/ModalMinds/MM-EUREKA",
    "durationMs": 3839,
    "url": "https://papers.cool/arxiv/2503.07365"
  },
  "sourceToolAssistantUUID": "861f901d-cf4d-4624-8365-5cd34e7deab3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-27T16:04:22.164Z_

```json
{
  "parentUuid": "8444b6ff-e546-43a9-a447-a0c7a30f82e6",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "f51262d0-fff1-4e00-b223-4f9f115e8455",
  "timestamp": "2026-05-27T16:04:22.164Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 33 · 2026-05-27T16:04:25.281Z_

<details><summary>Logged reasoning block</summary>

```text
I got a large output saved to a file. Let me read that file to get the full paper content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f51262d0-fff1-4e00-b223-4f9f115e8455",
  "isSidechain": false,
  "requestId": "req_011CbTMh7RjzVhzfQXZJrqJm",
  "type": "assistant",
  "uuid": "d7f27f28-a816-412d-8d01-52be2caa8d23",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PH7uX8RiYWFEeGkFCvF9MT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 608,
      "cache_creation_input_tokens": 751,
      "cache_read_input_tokens": 15925,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 751,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 608,
          "output_tokens": 201,
          "cache_read_input_tokens": 15925,
          "cache_creation_input_tokens": 751,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 751
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

_source line 34 · 2026-05-27T16:04:25.283Z_

Excellent! The full paper content was saved. Let me read it in chunks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7f27f28-a816-412d-8d01-52be2caa8d23",
  "isSidechain": false,
  "requestId": "req_011CbTMh7RjzVhzfQXZJrqJm",
  "type": "assistant",
  "uuid": "1390f855-a45c-4683-9a8e-d0b04f6d6685",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PH7uX8RiYWFEeGkFCvF9MT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 608,
      "cache_creation_input_tokens": 751,
      "cache_read_input_tokens": 15925,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 751,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 608,
          "output_tokens": 201,
          "cache_read_input_tokens": 15925,
          "cache_creation_input_tokens": 751,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 751
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

_source line 35 · 2026-05-27T16:04:26.285Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LzrfDXbtZP6cGkNsiiHEMV`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/85dae6a1-bcc0-4c8f-97a6-84608d21f8c6/tool-results/toolu_01KEj67Agphd4njkFJNjphT6.txt",
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1390f855-a45c-4683-9a8e-d0b04f6d6685",
  "isSidechain": false,
  "requestId": "req_011CbTMh7RjzVhzfQXZJrqJm",
  "type": "assistant",
  "uuid": "fa2e1461-2035-4314-a5df-8efd9070505b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PH7uX8RiYWFEeGkFCvF9MT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 608,
      "cache_creation_input_tokens": 751,
      "cache_read_input_tokens": 15925,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 751,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 608,
          "output_tokens": 201,
          "cache_read_input_tokens": 15925,
          "cache_creation_input_tokens": 751,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 751
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

_source line 36 · 2026-05-27T16:04:26.568Z_

<details><summary>↩ Tool result · `toolu_01LzrfDXbtZP6cGkNsiiHEMV`</summary>

````text
1	# MM-EUREKA: EXPLORING THE FRONTIERS OF MULTIMODAL REASONING WITH RULE-BASED REINFORCEMENT LEARNING
2	
3	Fanqing Meng\* Lingxiao Du\* Zongkai Liu\* Zhixiang Zhou\* Quanfeng Lu
4	
5	Tiancheng Han Daocheng Fu Botian Shi Wenhai Wang Junjun He
6	
7	Kaipeng Zhang Ping Luo Yu Qiao Qiaosheng Zhang† Wenqi Shao†
8	
9	Shanghai AI Laboratory Shanghai Innovation Institute  
10	Shanghai Jiao Tong University The University of Hong Kong
11	
12	## ABSTRACT
13	
14	DeepSeek R1, and o1 have demonstrated powerful reasoning capabilities in the text domain through stable large-scale reinforcement learning. To enable broader applications, some works have attempted to transfer these capabilities to multimodal reasoning. However, these efforts have been limited by the limited difficulty of selected tasks and relatively small training scales, making it challenging to demonstrate strong multimodal reasoning abilities. To address this gap, we introduce the MMK12 dataset and MM-Eureka with 7B and 32B parameters. The former is a high-quality multimodal mathematics reasoning dataset featuring diverse knowledge domains with human-verified answers and solution processes. The latter is a multimodal model employing rule-based reinforcement learning on MMK12, utilizing online filtering and two-stage training strategy to enhance training stability. MM-Eureka demonstrates remarkable performance gains in multimodal mathematical reasoning, outperforming previous powerful models like InternVL2.5-78B or InternVL2.5-38B-MPO. In particular, MM-Eureka achieves competitive or superior performance compared to both open-source and closed-source models, and trails slightly behind o1 in multidisciplinary reasoning tasks. We open-source our complete pipeline to foster further research in this area. We release all our codes, models, data, etc. at &lt;https://github.com/ModalMinds/MM-EUREKA>
15	
16	## 1 INTRODUCTION
17	
18	Large-scale reinforcement learning (RL) (Sutton et al., 1998) has demonstrated remarkable progress in improving the reasoning ability of Large Language Models (LLMs), particularly in the math and code domains (OpenAI, 2024; DeepSeek-AI et al., 2025). Recent research, such as o1 (OpenAI, 2024) and DeepSeek-R1 (DeepSeek-AI et al., 2025), shows that large-scale RL can achieve breakthrough improvements in complex reasoning tasks during post-training phases, sometimes even without supervised fine-tuning (SFT) (Radford et al., 2019). Despite great success in the text domain, many real-world reasoning tasks such as interpreting scientific diagrams and geometrical reasoning can only be effectively solved with the image input. However, transferring large-scale RL techniques that work well for LLMs to multimodal scenarios remains underexplored.
19	
20	Recently, many works in the community have attempted to transfer the rule-based RL used in DeepSeek-R1 to multimodal scenarios. However, these works explore relatively small model sizes and fail to achieve stable training over extended periods like DeepSeek-R1. For instance, R1-V (Chen et al., 2025) demonstrates improvements only in simple counting tasks, which covers limited
21	
22	† Corresponding Authors: shaowenqi@pjlab.org.cn; zhangqiaosheng@pjlab.org.cn
23	
24	\* Equal contributionFigure 1: The overview of our proposed MMK12 and MM-Eureka. MMK12 training set has diverse multimodal mathematical questions with verified answer and process, while its evaluation set has multiple-choice questions for each discipline including math, physics, chemistry, and biology. MM-Eureka built on MMK12 has powerful performance in multimodal reasoning and it also exists aha-moment like DeepSeek R1.
25	
26	complexity, while the model size remains modest. LMM-R1 (Peng et al., 2025) achieves gains in accuracy reward for geometric reasoning; however, such success has not been verified in large-scale training with image-text data. Although Kimi k1.5 (Team et al., 2025a) has achieved competitive results in multimodal reasoning, it has not open-sourced its model or training data to the community. Therefore, how to achieve stable rule-based RL training in the multimodal reasoning domain remains an important and unsolved problem for the open-source community.
27	
28	To address this gap, as shown in Figure 1, we first collect MMK12\*, a high-quality and diverse multimodal mathematical reasoning dataset. Subsequently, we implement MM-Eureka with two variants based on the MMK12 training set, i.e. MM-Eureka-7B built on Qwen2.5-VL-Instruct-7B and MM-Eureka-32B built on Qwen2.5-VL-Instruct-32B, which demonstrate excellent performance in multidisciplinary multimodal reasoning. For instance, MM-Eureka-7B achieves 66.1 on MMK12 evaluation sets, only 0.2 points below Intern2.5-VL-78B. On MathVista, it reaches 73.0, even surpassing InternVL2.5-VL-78B. MM-Eureka-32B demonstrates stronger performance, scoring 72.3 on multidisciplinary K12 evaluation sets, which exceeds both Qwen2.5-VL-72B’s 70.3 and closed-source models like Gemini2-Flash, ranking second only to o1’s 73.9. On commonly used multimodal mathematical reasoning benchmarks, MM-Eureka-32B achieves 73.4 on WeMath, outperforming all open-source models and most closed-source models including Claude3.7 Sonnet. On MathVista, it reaches 74.8, surpassing all open-source and closed-source models. Both variants demonstrate significant improvements in multidisciplinary K12 and mathematical reasoning performance, outperforming most open-source models of similar sizes.
29	
30	\*K12 refers to the full span of primary and secondary education, and the K12 evaluation sets used in our work primarily contain questions from the secondary level.Specifically, despite growing interest in multimodal reasoning models, high-quality datasets for multimodal mathematical reasoning remain scarce. For example, Geo3k (Lu et al., 2021) and RCOT (Deng et al., 2024) focus only on geometry problems. Although MAVIS (Zhang et al., 2024b) comprises data involving geometry and functions, it consists of synthetic data, lacking diversity in images and questions. To this end, we construct MMK12, a K12-level multimodal mathematical reasoning dataset. The training set covers a wide range of domains, including functions, geometry, and equations, spanning from elementary through high school curricula. For evaluation, MMK12 includes four disciplines: mathematics, physics, chemistry, and biology. To facilitate testing, we collect 500 multimodal multiple-choice questions for each discipline and carefully verify that there is no overlap with the training set.
31	
32	Subsequently, to achieve stable rule-based RL training over extended periods, we utilize the online filter strategy from PRIME (Cui et al., 2025) that dynamically filters prompts with zero advantage during training, e.g., those answered either completely correctly or incorrectly. For MM-Eureka-32B, we further introduce a two-stage training strategy: the first stage leverages MMK12 by RL without KL divergence to develop the model’s general reasoning abilities while reducing training cost; the second stage fine-tunes the model on Geo3k with KL regularization to mitigate domain-specific deficiencies and enhance training stability. We use the GRPO (DeepSeek-AI et al., 2025) as our basic RL approach, which offers higher efficiency compared to the commonly used PPO (Schulman et al., 2017b). These strategies enable us to achieve stable, long-horizon RL training and consistent performance gains for both 7B and 32B model variants, while maintaining high training efficiency.
33	
34	Through the journey of developing MM-Eureka, we have several findings. **First**, it is difficult for the model to acquire new knowledge through RL training. Instead, performance improvements come from increasing the probability that the model generates correct answers during inference. **Second**, we discover that simple rule-based RL exhibits outstanding generalization capabilities. Training solely on mathematical data leads to simultaneous improvements in physics, chemistry, biology, and other disciplines. **Third**, rule-based RL generalizes better than other post-training strategies such as SFT (Ouyang et al., 2022) and COT SFT (Guo et al., 2024) across various tasks.
35	
36	Our goal is to share our implementation experiences and complete the open-source pipeline with the community, including data, code, and models. We believe this comprehensive open-source framework would help the community better explore the multimodal reasoning task. The main contributions are summarized as follows:
37	
38	- • We utilize an online filter strategy and introduce a two-stage training strategy to address the collapse issues encountered during RL training of large-scale VLMs, achieving stable rule-based RL training for large-scale VLMs.
39	- • We present MM-Eureka-7B and MM-Eureka-32B. Extensive experimental results on various downstream tasks demonstrate that they are top performers among open-source models in the multimodal reasoning domain. For example, MM-Eureka-32B scores only 1.7 points below o1 on the multidisciplinary evaluation set of MMK12; MM-Eureka-7B achieves 73.0 on MathVista (Lu et al., 2024), surpassing InternVL2.5-78B (Chen et al., 2024).
40	- • We open-source all our models, code, and collected high-quality multimodal mathematical reasoning data. Compared to existing open-source repositories, we support a wider range of RL algorithms and include much higher-quality data.
41	
42	## 2 RELATED WORK
43	
44	### 2.1 LANGUAGE REASONING MODEL
45	
46	LLMs have demonstrated impressive performance across a wide range of tasks, yet more complex challenges require these models to exhibit human-like reasoning capabilities. As a result, enhancing the reasoning ability of LLMs has become a critical research focus. Reinforcement Learning from Human Feedback (RLHF), particularly Proximal Policy Optimization (PPO) (Schulman et al., 2017a), has shown promise in enabling LLMs to learn reasoning abilities effectively. However, the PPO training process is computationally intensive and complex, prompting the development of simplified alternatives such as Direct Preference Optimization (DPO) (Rafailov et al., 2023). WhileDPO alleviates some training difficulties, its reliance on offline data can limit model performance. To address these limitations, methods like Group Relative Policy Optimization (GRPO) (DeepSeek-AI et al., 2025), REINFORCE Leave-One-Out (RLOO) (Kool et al., 2019; Ahmadian et al., 2024), and Reinforce++ (Hu, 2025) have been introduced. Notably, Deepseek R1 (DeepSeek-AI et al., 2025) reveals that pure RL can encourage LLMs to actively engage in reasoning, including self-reflection and error correction. Despite these advancements, research on improving the reasoning capabilities of multimodal large models remains relatively scarce, highlighting an important direction for future exploration.
47	
48	## 2.2 VISION-LANGUAGE REASONING MODEL
49	
50	Currently, the leading models in multimodal reasoning are closed-source systems such as GPT-4o (Hurst et al., 2024) and Kimi-VL (Team et al., 2025b). In contrast, the open-source community remains noticeably behind, still in the early stages of exploration. Recent concurrent efforts have begun to explore the use of RL to enhance the visual reasoning capabilities of vision-language reasoning models (VLMs), aiming to trigger an “Aha Moment” in visual reasoning. LMM-R1 (Peng et al., 2025) strengthens visual reasoning through a two-stage rule-based RL approach; however, its primary reasoning performance gains are derived from text-only datasets rather than genuinely multimodal datasets. R1-V (Chen et al., 2025) investigates rule-based RL within specific subdomains, such as geometric reasoning and object counting tasks, but falls short of addressing more complex reasoning challenges. Reason-RFT (Tan et al., 2025), on the other hand, relies on SFT with COT reasoning activation data to achieve an effective cold start before the RL training phase. In this paper, our objective is to develop an effective, stable, and comprehensive open-source training pipeline for multimodal reasoning models, including datasets, code, and models. Our work aims to advance the growth and innovation of the open-source community.
51	
52	## 3 MMK12: MULTIMODAL MATHEMATIC K12-LEVEL DATASET
53	
54	&lt;table border="1">
55	&lt;thead>
56	&lt;tr>
57	&lt;th>&lt;/th>
58	&lt;th>Scope&lt;/th>
59	&lt;th>Type&lt;/th>
60	&lt;th>Img. Source&lt;/th>
61	&lt;th>QA Source&lt;/th>
62	&lt;th>CoT Answer Source&lt;/th>
63	&lt;/tr>
64	&lt;/thead>
65	&lt;tbody>
66	&lt;tr>
67	&lt;td>MAVIS (Zhang et al., 2024b)&lt;/td>
68	&lt;td>Geo &amp; Func&lt;/td>
69	&lt;td>MCQ &amp; FB&lt;/td>
70	&lt;td>Synthetic&lt;/td>
71	&lt;td>Synthetic Engine&lt;/td>
72	&lt;td>GPT-4o&lt;/td>
73	&lt;/tr>
74	&lt;tr>
75	&lt;td>Geo3k (Lu et al., 2021)&lt;/td>
76	&lt;td>Geo&lt;/td>
77	&lt;td>FB&lt;/td>
78	&lt;td>Real world&lt;/td>
79	&lt;td>Real world&lt;/td>
80	&lt;td>None&lt;/td>
81	&lt;/tr>
82	&lt;tr>
83	&lt;td>RCOT (Deng et al., 2024)&lt;/td>
84	&lt;td>Geo&lt;/td>
85	&lt;td>MCQ &amp; FB&lt;/td>
86	&lt;td>Synthetic&lt;/td>
87	&lt;td>Synthetic Engine&lt;/td>
88	&lt;td>GPT-4o&lt;/td>
89	&lt;/tr>
90	&lt;tr>
91	&lt;td>MultiMath (Peng et al., 2024)&lt;/td>
92	&lt;td>Diverse&lt;/td>
93	&lt;td>MCQ &amp; FB&lt;/td>
94	&lt;td>Real World&lt;/td>
95	&lt;td>GPT-4o&lt;/td>
96	&lt;td>GPT-4o&lt;/td>
97	&lt;/tr>
98	&lt;tr>
99	&lt;td>MMK12&lt;/td>
100	&lt;td>Diverse&lt;/td>
101	&lt;td>FB&lt;/td>
102	&lt;td>Real World&lt;/td>
103	&lt;td>Real World&lt;/td>
104	&lt;td>Real World&lt;/td>
105	&lt;/tr>
106	&lt;/tbody>
107	&lt;/table>
108	
109	Table 1: Comparison of dataset characteristics with other multimodal mathematical reasoning datasets. MMK12 comprises more diverse and high quality questions, with guaranteed correct answers and solution processes.
110	
111	As shown in Table 1, current multimodal mathematical reasoning datasets have limited scope and face challenges in ensuring answer correctness. For instance, while RCOT and MAVIS maintain answer accuracy through synthetic engine-generated QA pairs, this approach restricts problem diversity. Geo3k manually collected 3,000 geometry problems with verified answers, but it focuses solely on geometry examples. Although MultiMath gathers problems from real-world scenarios to ensure diversity, its reference answers generated by GPT-4o cannot guarantee correctness.
112	
113	To address these limitations, we introduce MMK12, a new dataset comprising over 15,000 multimodal mathematical reasoning problems across a wide range of domains, including geometry, functions, and graphical reasoning. Each problem is accompanied by a standard reference answer and a detailed step-by-step solution to ensure both accuracy and interpretability.
114	
115	In the following, we describe the construction and cleaning process of MMK12. As illustrated in Figure 2, we first collect a diverse set of multimodal mathematics problems and corresponding answers from a variety of Chinese mathematics textbooks and examination papers, covering grades from elementary to high school. These questions, answers, and COT processes are subsequently translated and refined into English, with the help of LLM. To minimize false positives during training, we retain only fill-in-the-blank problems. Besides, we use Math-Verify&lt;sup>†&lt;/sup> to parse
116	
117	&lt;sup>†&lt;/sup>&lt;https://github.com/huggingface/Math-Verify>The diagram illustrates the MMK12 construction pipeline. It begins with a collection of diverse K12-level multimodal math problems from various sources, including PDF, CSV, DOCX, and HTML files, along with images. These are processed through two parallel paths: 'Manual Annotation' and 'LLM Translation & Refinement'. The 'Manual Annotation' path involves human experts reviewing the data, while the 'LLM Translation & Refinement' path uses Large Language Models (LLMs) to translate the content into standardized English. The resulting 'Structured Data' is then subjected to a verification process. This process includes a 'Fill-in-the-blank?' check, which leads to 'Math-Verify' and 'Image size' checks, and a 'Multiple-choice?' check, which leads to 'Question type' and 'Single Image' checks. The final output is the 'MMK12 Training Dataset' and the 'MMK12 Benchmark'.
118	
119	Figure 2: The construction overview of MMK12. We collect diverse K12-level multimodal math problems from multiple sources, convert them to standardized English using LLMs, and verify all content for accuracy. The resulting MMK12 dataset includes a training set of 15,616 samples and a test set with 500 multiple-choice questions each for math, physics, chemistry, and biology.
120	
121	the answer, ensuring data reliability for RL training. For the MMK12 evaluation set, we follow a similar construction procedure, but exclusively select multiple-choice questions to facilitate reliable and efficient evaluation.
122	
123	In total, the MMK12 training dataset comprises 15,616 multimodal fill-in-the-blank mathematics problems, including 455 from elementary school, 9,776 from middle school, and 5,385 from high school. Each sample includes the question, an image, the final answer, and a CoT-formatted solution process. The MMK12 evaluation set has 2,000 multimodal multiple-choice questions, including math, physics, chemistry, and biology. Each item includes a question, a corresponding image, and the correct answer choice. Some examples in MMK12 are shown in Figure 1.
124	
125	MMK12 encompasses mathematical problems across various knowledge domains, including geometry, functions, spatial reasoning, and more. Some important categories are introduced as follows:
126	
127	- • **Function Reasoning:** This task requires models to understand function concepts, analyze function graphs and expressions, and apply function properties to solve problems. This type of reasoning develops the model’s ability to comprehend abstract mathematical concepts, fostering its capability to identify function characteristics, determine critical points, and analyze function behavior.
128	- • **Geometric Reasoning:** This task involves applying spatial relationships, geometric theorems, and properties of shapes. Through geometric reasoning training, models enhance their spatial visualization, logical deduction, and formalization abilities for geometry problems, enabling them to solve complex problems in both plane and solid geometry.
129	- • **Pattern Reasoning:** This type of task focuses on understanding flow diagrams and recognizing patterns in visual sequences. Models need to discover patterns, predict rule-based changes, or understand logical relationships in visual content. This task examines the model’s pattern recognition abilities, inductive reasoning skills, and visual logical thinking.
130	
131	Benefiting from a standardized data construction process with substantial human involvement and verification, MMK12 ensures both diversity in questions and correctness in answers and solution processes, making it suitable for various training methods such as RL and SFT for multimodal mathematical reasoning models. The MMK12 evaluation set also provides a convenient and accurate means to test models’ multidisciplinary reasoning capabilities.
132	
133	## 4 METHOD
134	
135	### 4.1 BASIC SETTINGS
136	
137	We employ Qwen2.5-VL (Bai et al., 2023) with 7B and 32B as the base models. Our RL algorithm is similar to DeepSeek-R1 (DeepSeek-AI et al., 2025), using rule-based format rewards  $r_{\text{format}} \in \{0, 0.5\}$ , accuracy rewards  $r_{\text{accuracy}} \in \{0, 1\}$  as reward function and GRPO as base RL algorithm for training. Furthermore, we develop a multimodal input RL framework based on OpenRLHF (Hu et al., 2024), which is compatible with commonly used models such as InternVL (Chen et al., 2024) and QwenVL, supporting various model sizes and RL algorithms. In the following sections, we provide detailed settings for our RL training.## 4.2 REWARD FUNCTION
138	
139	Following DeepSeek-R1, we also adopt the simple rule-based reward function rather than using outcome or process reward models, thereby alleviating reward hacking (Gao et al., 2022). Specifically, we use two types of rewards: accuracy reward and format reward. The former uses Math-Verify to extract the answer from model responses and compare it with the reference one, returning 1 or 0 based on correctness; the latter checks whether the response follows the specified format (`&lt;think>...&lt;/think>&lt;answer>...&lt;/answer>`), returning 0.5 or 0 based on compliance. We find that this simple and sparse reward is sufficient to significantly improve the model’s multimodal reasoning ability.
140	
141	## 4.3 ADVANTAGE ESTIMATION AND POLICY UPDATE
142	
143	Group Relative Policy Optimization (GRPO) (DeepSeek-AI et al., 2025) is a widely adopted RL algorithm that eliminates the need for training a complex critic model by leveraging intra-group relative performance to optimize the policy model. Specifically, for each query  $\mathbf{x}$ , the model generates a group of  $G$  responses  $\{\mathbf{y}^{(1)}, \mathbf{y}^{(2)}, \dots, \mathbf{y}^{(G)}\}$ . Subsequently, for each query with  $G$  responses, GRPO computes the relative advantage of each response based on their rewards, which are determined by a reward model, as follows:
144	
145	$$A^{(i)} = \frac{r^{(i)} - \text{mean}(\{r^{(j)}\}_{j=1}^G)}{\text{std}(\{r^{(j)}\}_{j=1}^G)}, \quad i = 1, \dots, G.$$
146	
147	Using the computed advantages, GRPO then optimizes the policy via the PPO-clip loss augmented with a directly imposed KL penalty term:
148	
149	$$J_{\text{PPO}}(\theta) = -\mathbb{E}_{\mathbf{x} \sim \mathcal{D}, \{\mathbf{y}^{(i)}\}_{i=1}^G \sim \pi_\theta(\cdot | \mathbf{x})} \left[ \frac{1}{G} \sum_{i=1}^G \frac{1}{|\mathbf{y}^{(i)}|} \sum_{t=1}^{|\mathbf{y}^{(i)}|} \left( \min \left( r^{i,t}(\theta) A^{(i)}, \text{clip}(r^{i,t}(\theta), 1 - \epsilon, 1 + \epsilon) A^{(i)} \right) - \beta D_{\text{KL}}^{i,t}(\pi_\theta, \pi_{\text{ref}}) \right) \right], \quad (1)$$
150	
151	where
152	
153	$$r^{i,t}(\theta) = \frac{\pi_\theta(y_t^{(i)} | \mathbf{x}, \mathbf{y}_{&lt;t}^{(i)})}{\pi_{\theta_{\text{old}}}(y_t^{(i)} | \mathbf{x}, \mathbf{y}_{&lt;t}^{(i)})} \text{ and } D_{\text{KL}}^{i,t}(\pi_\theta, \pi_{\text{ref}}) = \frac{\pi_{\text{ref}}(y_t^{(i)} | \mathbf{x}, \mathbf{y}_{&lt;t}^{(i)})}{\pi_\theta(y_t^{(i)} | \mathbf{x}, \mathbf{y}_{&lt;t}^{(i)})} - 1 - \log \frac{\pi_{\text{ref}}(y_t^{(i)} | \mathbf{x}, \mathbf{y}_{&lt;t}^{(i)})}{\pi_\theta(y_t^{(i)} | \mathbf{x}, \mathbf{y}_{&lt;t}^{(i)})}.$$
154	
155	In addition, to mitigate loss spikes during training caused by excessively large policy ratios combined with negative advantages, we further constrain the policy ratio within  $[0, c]$  beforehand, i.e., we replace  $r^{i,t}(\theta)$  with  $\text{clip}(r^{i,t}(\theta), 0, c)$  in Eq.(1). In practice, we set the default value of  $c$  to 3.
156	
157	## 4.4 ONLINE FILTERING
158	
159	To further enhance training stability, we adopt the online prompt filtering strategy proposed in PRIME (Cui et al., 2025). To ensure sufficient gradient information throughout RL training, we filter out prompts with responses that are either completely correct or completely incorrect during training, as their corresponding advantages under GRPO are zero. The detailed process is shown in Algorithm 1.
160	
161	We present an ablation study on the online filtering mechanism in Figure 3. Models trained with the online filter strategy maintain relatively stable trends in both the accuracy-based reward and response length throughout training. In contrast, models without the online filter show an initial improvement in accuracy, but soon experience a sharp decline, with accuracy eventually approaching zero and response lengths significantly shortening in the later stages. These findings suggest that the online filter plays an important role in stabilizing RL training and can help prevent model collapse during optimization.
162	
163	## 4.5 TWO-STAGE TRAINING
164	
165	During RL training of MM-Eureka-32B, we observe that maintaining training stability becomes increasingly challenging as model size scales up. Specifically, we find that models tend to experience**Algorithm 1** Online Filter
166	
167	**Input:** Prompt dataset  $\mathcal{D}$ ; initial policy  $\pi_\theta$ ; reward model  $R$ ; buffer size  $N_B$ ; hyperparameters  $K_1, K_2, G, \epsilon_{\text{acc}}^{\text{lower}}, \epsilon_{\text{acc}}^{\text{upper}}$
168	
169	**Output:**  $\pi_\theta$
170	
171	```
172	
173	1: Buffer  $\mathcal{B} \leftarrow \{\}$ 
174	2: for iteration = 1, ...,  $K_1$  do
175	3:   Sample a batch of prompts  $\mathcal{Q} \sim \mathcal{D}$ 
176	4:   for each prompt  $\mathbf{x} \in \mathcal{Q}$  do
177	5:     Generate  $G$  responses  $\{\mathbf{y}^{(i)}\}_{i=1}^G \sim \pi_\theta(\cdot|\mathbf{x})$ 
178	6:     Compute the reward  $r^{(i)} = R(\mathbf{x}, \mathbf{y}^{(i)})$  for  $i = 1, \dots, G$ 
179	7:     Compute the accuracy  $\mathcal{C}_{\mathbf{x}} = |\{\mathbf{y}^{(i)} | r^{(i)} = 1\}|$ 
180	8:     if  $\epsilon_{\text{acc}}^{\text{lower}} \leq \mathcal{C}_{\mathbf{x}} \leq \epsilon_{\text{acc}}^{\text{upper}}$  then
181	9:       Add the sample to the buffer  $\mathcal{B} \leftarrow \mathcal{B} \cup \{(\mathbf{x}, \mathbf{y}^{(i)}, r^{(i)})\}_{i=1}^G$ 
182	10:    end if
183	11:  end for
184	12:  if  $|\mathcal{B}| \geq N_B$  then
185	13:    for Epoch = 1, ...,  $K_2$  do
186	14:      Update policy  $\pi_\theta$  on  $\mathcal{B}[0:N_B]$  by any RL algorithm
187	15:    end for
188	16:    Buffer  $\mathcal{B} \leftarrow \{\}$ 
189	17:  end if
190	18: end for
191	
192	```
193	
194	Figure 3: Comparison of the use of online filtering. Using online filter makes the RL training more stable in the long term, with consistently increasing accuracy reward and response length.
195	
196	sudden collapse during training, characterized by an abrupt drop of the accuracy reward to near-zero values, as shown in Figure 5 (a). After analysis, we find that these collapses are usually preceded by sharp increases in the policy ratio (indicating excessively large updates from old to new policies) like Figure 5 (c). Additionally, unlike the 7B model which shows comprehensive improvement when trained solely on K12 data, the 32B model trained only on MMK12 exhibits performance degradation in specific domains such as geometry.
197	
198	To address these challenges, we propose a two-stage training strategy for large models. In the first stage, we apply the GRPO algorithm without KL regularization, using MMK12 data collected as detailed in Section 3 to broadly enhance the model’s general reasoning capabilities. In the second stage, we incorporate a KL divergence into GRPO to constrain update magnitudes and improve training stability. Concurrently, we augment the training set with domain-specific Geo3k data to address identified performance gaps. As shown in Section 6.3, this two-stage approach enables stable training and yields further performance gains across nearly all evaluated benchmarks.
199	
200	## 5 EXPERIMENTS
201	
202	We present our experimental setup in Section 5.1, where we indicate the training details. After that, we provide an overview of the selected baselines and evaluation benchmarks in Section 5.2 and Section 5.3, we demonstrate the superior effectiveness of MM-Eureka-7B and MM-Eureka-32B through extensive experiments in Section 5.4.## 5.1 EXPERIMENTS SETUP
203	
204	We design our prompt template following the format used in DeepSeek-R1, wherein the system prompt explicitly specifies the required output structure, including the use of `&lt;answer>` tags to separate the reasoning process from the final answer. Detailed prompt configurations are provided in Table 2.
205	
206	For training hyperparameters, both the rollout batch size and training batch size are set to 128, with 8 rollouts generated per sample. Sampling is conducted with a temperature of 1.0 to encourage response diversity, and optimization is performed using a learning rate of  $1 \times 10^{-6}$ . Besides, for MM-Eureka-32B, we adopt a two-stage training scheme. In Stage 1, KL divergence is disabled to promote exploration and policy flexibility during the early phase. In Stage 2, a small KL penalty  $1 \times 10^{-3}$  is introduced to stabilize training.
207	
208	Table 2: Prompt setting for MM-Eureka.
209	
210	---
211	
212	**SYSTEM:** Solve the question. The user asks a question, and you solve it. You first think about the reasoning process in the mind and then provide the user with the answer. The answer is in latex format and wrapped in `$...$`. The final answer must be wrapped using the `\boxed{}` command. The answer should be enclosed within `&lt;answer>&lt;/answer>` tags, i.e., Since  $1+1=2$ , so the answer is  $\boxed{2}$ . `&lt;answer>`The answer is  $\boxed{2}$ `&lt;/answer>`, which means the final answer assistant’s output should start with `&lt;answer>` and end with `&lt;/answer>`.
213	
214	**USER:** `&lt;image><{{question}}&lt;/image>`
215	
216	---
217	
218	## 5.2 BASELINES
219	
220	To comprehensively evaluate the effectiveness of MM-Eureka, we compare it against a diverse set of baselines, including both closed-source and open-source systems.
221	
222	**Closed-Source Models.** We include several leading proprietary models in our comparison. GPT-4o (Hurst et al., 2024), Claude3.7-Sonnet (Anthropic, 2024), and Gemini2-flash (Team et al., 2023) are general-purpose multimodal models without dedicated reasoning optimization, while o1 (OpenAI, 2024) is explicitly designed to enhance reasoning capabilities. These models serve as strong references for the current state of the art.
223	
224	**Open-Source General Models.** This group comprises high-capacity vision-language models trained for general purposes, including Qwen-2.5-VL (Bai et al., 2023) and InternVL2.5 (Chen et al., 2024) across various model sizes (7B to 78B). These models are primarily pretrained or instruction-tuned on large-scale image-text datasets. They offer a baseline for evaluating the impact of reasoning-specific post-training.
225	
226	**Open-Source Reasoning Models.** We further include open-source models explicitly fine-tuned for reasoning, such as InternVL2.5-MPO variants (Wang et al., 2024b), QVQ-72B-Preview (Team, 2024), Adora-7B (Gui & Ren, 2025), R1-Onevision (Yang et al., 2025), and OpenVLThinker (Deng et al., 2025). These models employ various strategies, including SFT (Ouyang et al., 2022), DPO (Rafailov et al., 2023), and rule-based reinforcement learning. They represent the most competitive open-source efforts in multimodal reasoning.
227	
228	## 5.3 BENCHMARKS
229	
230	To assess the performance of our model, we conduct evaluations on multiple benchmark datasets, including MathVista(testmini) (Lu et al., 2024), MathVerse(testmini) (Zhang et al., 2024a), MathVision(test) (Wang et al., 2024a), OlympiadBench(EN-OE split) (He et al., 2024) and WeMath (Qiao et al., 2024). MathVista is one of the most widely used multimodal mathematical benchmarks, offering a diverse set of problems that span general visual question answering, figure question answering, logic, algebra, and geometry. MathVerse, on the other hand, focuses specifically on themodel’s ability to comprehend images, with tasks categorized into areas such as algebra and geometry. MathVision takes this a step further by emphasizing more abstract visual understanding, testing the model’s capacity for recognizing and reasoning beyond conventional mathematical contexts. OlympiadBench presents graduate-level mathematical competition problems, from which we select the English questions for evaluation. WeMath complements these by providing fine-grained diagnostic insights into model reasoning behavior, using a large-scale, hierarchically annotated problem set to assess knowledge mastery and generalization.
231	
232	Beyond these established benchmarks, both our model and the baselines are further evaluated on the proposed MMK12 Benchmark, as introduced in Section 3. Unlike OlympiadBench, which targets advanced graduate-level mathematical reasoning, MMK12 focuses on assessing the model’s ability to solve fundamental multimodal multidisciplinary problems commonly encountered in K12 education. MMK12 enables a comprehensive evaluation of a model’s ability across disciplines beyond mathematics.
233	
234	During evaluation, we adopt greedy decoding with a temperature of 0, ensuring deterministic outputs. We do not use beam search, and both top- $p$  and top- $k$  sampling are disabled.
235	
236	#### 5.4 QUANTITATIVE RESULTS
237	
238	In this section, we demonstrate the superiority of MM-Eureka through its performance on the benchmarks introduced in Section 5.3. For the multimodal mathematical evaluation sets, we primarily use official results or results provided in VLMEvalKit (Duan et al., 2024) for baseline comparisons. When such results are unavailable, we conduct evaluations using the testing methodologies provided in VLMEvalKit within our vllm-based (Kwon et al., 2023) inference framework. Specifically, for o1, due to resource constraints, we randomly sample only 500 instances for testing. For the MMK12 evaluation set, considering it consists entirely of multiple-choice questions, we use the same Chain-of-Thought prompt structure from WeMath (Qiao et al., 2024) to test models within our inference framework. Because WeMath also consists entirely of multiple-choice questions. Results evaluated by ourselves are presented in *italics*.
239	
240	**Mathematics** In Table 3, we present a comprehensive summary of MM-Eurekas’ performance across different multimodal mathematical reasoning tasks. It demonstrates that both MM-Eureka-7B and MM-Eureka-32B consistently outperform similar-sized open-source baselines across almost all tasks. In particular, MM-Eureka-7B achieves 73.0 on Mathvista, surpassing InternVL-78B by 0.7% and the reasoning-focused InternVL2.5-38B-MPO by 0.2%. On WeMath, it similarly approaches the performance of InternVL-78B. MM-Eureka-32B exceeds all current open-source models of comparable size on all benchmarks except MathVision, with average performance approaching Qwen-72B-Instruct. It even outperforms the closed-source model Claude3.7 Sonnet on WeMath. In summary, MM-Eureka establishes itself as the top performer among same-sized open-source models across almost all multimodal mathematical reasoning tasks, regardless of whether considering the 7B or 32B version.
241	
242	However, when compared to closed-source models, MM-Eureka-32B still shows considerable performance gaps. While it outperforms o1 on Mathvista, it lags significantly behind closed-source multimodal reasoning models like o1 on more challenging benchmarks such as Mathvision or OlympiadBench.
243	
244	**MMK12** Beyond validating our model’s superiority on widely-used multimodal mathematical reasoning benchmarks like MathVista, it is necessary to test its capabilities and generalization across multidisciplinary reasoning domains using questions absent from the training set (e.g., physics, chemistry, and biology). For this purpose, we employ the MMK12 dataset constructed in Section 3, which can effectively measure models’ multimodal reasoning capabilities across multiple disciplines.
245	
246	As shown in Table 4, MM-Eureka-32B demonstrates multidisciplinary capabilities only marginally behind o1 by 1.7%, while outperforming larger-scale models such as Qwen-2.5-VL-72B and
247	
248	&lt;sup>†&lt;/sup>Results of o1 based on random sampling of 500 test instances due to resource constraints.
249	
250	&lt;sup>‡&lt;/sup>Results of R1-Onevision in Mathvision is 23.5 from our evaluation, which is far behind its official report as 29.9.Table 3: Performance comparison across different multimodal mathematical benchmarks. Bold indicates the top performer with the open-source models, while underline indicates the second best performer within open-source models. For some official results that are relatively different from our evaluation results, we mark our test results after ’/’.
251	
252	&lt;table border="1">
253	&lt;thead>
254	&lt;tr>
255	&lt;th>Model&lt;/th>
256	&lt;th>MathVista&lt;/th>
257	&lt;th>MathVerse&lt;/th>
258	&lt;th>Mathvision&lt;/th>
259	&lt;th>OlypamidBench&lt;/th>
260	&lt;th>WeMath&lt;/th>
261	&lt;/tr>
262	&lt;/thead>
263	&lt;tbody>
264	&lt;tr>
265	&lt;td colspan="6">&lt;b>Closed-Source Models&lt;/b>&lt;/td>
266	&lt;/tr>
267	&lt;tr>
268	&lt;td>Claude3.7-Sonnet&lt;/td>
269	&lt;td>66.8&lt;/td>
270	&lt;td>52.0&lt;/td>
271	&lt;td>41.3&lt;/td>
272	&lt;td>48.9&lt;/td>
273	&lt;td>72.6&lt;/td>
274	&lt;/tr>
275	&lt;tr>
276	&lt;td>GPT-4o&lt;/td>
277	&lt;td>63.8&lt;/td>
278	&lt;td>50.2&lt;/td>
279	&lt;td>30.4&lt;/td>
280	&lt;td>35.0&lt;/td>
281	&lt;td>68.8&lt;/td>
282	&lt;/tr>
283	&lt;tr>
284	&lt;td>o1&lt;/td>
285	&lt;td>73.9&lt;/td>
286	&lt;td>57.0&lt;/td>
287	&lt;td>60.3&lt;/td>
288	&lt;td>68.0*&lt;/td>
289	&lt;td>98.7*&lt;/td>
290	&lt;/tr>
291	&lt;tr>
292	&lt;td>Gemini2-flash&lt;/td>
293	&lt;td>70.4&lt;/td>
294	&lt;td>59.3&lt;/td>
295	&lt;td>41.3&lt;/td>
296	&lt;td>51.0&lt;/td>
297	&lt;td>71.4&lt;/td>
298	&lt;/tr>
299	&lt;tr>
300	&lt;td colspan="6">&lt;b>Open-Source General Models&lt;/b>&lt;/td>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "fa2e1461-2035-4314-a5df-8efd9070505b",
  "isSidechain": false,
  "promptId": "6e9b4775-3324-430a-aeff-baabf4898966",
  "type": "user",
  "uuid": "384a999b-4118-4f65-90d3-a5e7e9169bb6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/85dae6a1-bcc0-4c8f-97a6-84608d21f8c6/tool-results/toolu_01KEj67Agphd4njkFJNjphT6.txt",
      "content": "# MM-EUREKA: EXPLORING THE FRONTIERS OF MULTIMODAL REASONING WITH RULE-BASED REINFORCEMENT LEARNING\n\nFanqing Meng\\* Lingxiao Du\\* Zongkai Liu\\* Zhixiang Zhou\\* Quanfeng Lu\n\nTiancheng Han Daocheng Fu Botian Shi Wenhai Wang Junjun He\n\nKaipeng Zhang Ping Luo Yu Qiao Qiaosheng Zhang† Wenqi Shao†\n\nShanghai AI Laboratory Shanghai Innovation Institute  \nShanghai Jiao Tong University The University of Hong Kong\n\n## ABSTRACT\n\nDeepSeek R1, and o1 have demonstrated powerful reasoning capabilities in the text domain through stable large-scale reinforcement learning. To enable broader applications, some works have attempted to transfer these capabilities to multimodal reasoning. However, these efforts have been limited by the limited difficulty of selected tasks and relatively small training scales, making it challenging to demonstrate strong multimodal reasoning abilities. To address this gap, we introduce the MMK12 dataset and MM-Eureka with 7B and 32B parameters. The former is a high-quality multimodal mathematics reasoning dataset featuring diverse knowledge domains with human-verified answers and solution processes. The latter is a multimodal model employing rule-based reinforcement learning on MMK12, utilizing online filtering and two-stage training strategy to enhance training stability. MM-Eureka demonstrates remarkable performance gains in multimodal mathematical reasoning, outperforming previous powerful models like InternVL2.5-78B or InternVL2.5-38B-MPO. In particular, MM-Eureka achieves competitive or superior performance compared to both open-source and closed-source models, and trails slightly behind o1 in multidisciplinary reasoning tasks. We open-source our complete pipeline to foster further research in this area. We release all our codes, models, data, etc. at &lt;https://github.com/ModalMinds/MM-EUREKA>\n\n## 1 INTRODUCTION\n\nLarge-scale reinforcement learning (RL) (Sutton et al., 1998) has demonstrated remarkable progress in improving the reasoning ability of Large Language Models (LLMs), particularly in the math and code domains (OpenAI, 2024; DeepSeek-AI et al., 2025). Recent research, such as o1 (OpenAI, 2024) and DeepSeek-R1 (DeepSeek-AI et al., 2025), shows that large-scale RL can achieve breakthrough improvements in complex reasoning tasks during post-training phases, sometimes even without supervised fine-tuning (SFT) (Radford et al., 2019). Despite great success in the text domain, many real-world reasoning tasks such as interpreting scientific diagrams and geometrical reasoning can only be effectively solved with the image input. However, transferring large-scale RL techniques that work well for LLMs to multimodal scenarios remains underexplored.\n\nRecently, many works in the community have attempted to transfer the rule-based RL used in DeepSeek-R1 to multimodal scenarios. However, these works explore relatively small model sizes and fail to achieve stable training over extended periods like DeepSeek-R1. For instance, R1-V (Chen et al., 2025) demonstrates improvements only in simple counting tasks, which covers limited\n\n† Corresponding Authors: shaowenqi@pjlab.org.cn; zhangqiaosheng@pjlab.org.cn\n\n\\* Equal contributionFigure 1: The overview of our proposed MMK12 and MM-Eureka. MMK12 training set has diverse multimodal mathematical questions with verified answer and process, while its evaluation set has multiple-choice questions for each discipline including math, physics, chemistry, and biology. MM-Eureka built on MMK12 has powerful performance in multimodal reasoning and it also exists aha-moment like DeepSeek R1.\n\ncomplexity, while the model size remains modest. LMM-R1 (Peng et al., 2025) achieves gains in accuracy reward for geometric reasoning; however, such success has not been verified in large-scale training with image-text data. Although Kimi k1.5 (Team et al., 2025a) has achieved competitive results in multimodal reasoning, it has not open-sourced its model or training data to the community. Therefore, how to achieve stable rule-based RL training in the multimodal reasoning domain remains an important and unsolved problem for the open-source community.\n\nTo address this gap, as shown in Figure 1, we first collect MMK12\\*, a high-quality and diverse multimodal mathematical reasoning dataset. Subsequently, we implement MM-Eureka with two variants based on the MMK12 training set, i.e. MM-Eureka-7B built on Qwen2.5-VL-Instruct-7B and MM-Eureka-32B built on Qwen2.5-VL-Instruct-32B, which demonstrate excellent performance in multidisciplinary multimodal reasoning. For instance, MM-Eureka-7B achieves 66.1 on MMK12 evaluation sets, only 0.2 points below Intern2.5-VL-78B. On MathVista, it reaches 73.0, even surpassing InternVL2.5-VL-78B. MM-Eureka-32B demonstrates stronger performance, scoring 72.3 on multidisciplinary K12 evaluation sets, which exceeds both Qwen2.5-VL-72B’s 70.3 and closed-source models like Gemini2-Flash, ranking second only to o1’s 73.9. On commonly used multimodal mathematical reasoning benchmarks, MM-Eureka-32B achieves 73.4 on WeMath, outperforming all open-source models and most closed-source models including Claude3.7 Sonnet. On MathVista, it reaches 74.8, surpassing all open-source and closed-source models. Both variants demonstrate significant improvements in multidisciplinary K12 and mathematical reasoning performance, outperforming most open-source models of similar sizes.\n\n\\*K12 refers to the full span of primary and secondary education, and the K12 evaluation sets used in our work primarily contain questions from the secondary level.Specifically, despite growing interest in multimodal reasoning models, high-quality datasets for multimodal mathematical reasoning remain scarce. For example, Geo3k (Lu et al., 2021) and RCOT (Deng et al., 2024) focus only on geometry problems. Although MAVIS (Zhang et al., 2024b) comprises data involving geometry and functions, it consists of synthetic data, lacking diversity in images and questions. To this end, we construct MMK12, a K12-level multimodal mathematical reasoning dataset. The training set covers a wide range of domains, including functions, geometry, and equations, spanning from elementary through high school curricula. For evaluation, MMK12 includes four disciplines: mathematics, physics, chemistry, and biology. To facilitate testing, we collect 500 multimodal multiple-choice questions for each discipline and carefully verify that there is no overlap with the training set.\n\nSubsequently, to achieve stable rule-based RL training over extended periods, we utilize the online filter strategy from PRIME (Cui et al., 2025) that dynamically filters prompts with zero advantage during training, e.g., those answered either completely correctly or incorrectly. For MM-Eureka-32B, we further introduce a two-stage training strategy: the first stage leverages MMK12 by RL without KL divergence to develop the model’s general reasoning abilities while reducing training cost; the second stage fine-tunes the model on Geo3k with KL regularization to mitigate domain-specific deficiencies and enhance training stability. We use the GRPO (DeepSeek-AI et al., 2025) as our basic RL approach, which offers higher efficiency compared to the commonly used PPO (Schulman et al., 2017b). These strategies enable us to achieve stable, long-horizon RL training and consistent performance gains for both 7B and 32B model variants, while maintaining high training efficiency.\n\nThrough the journey of developing MM-Eureka, we have several findings. **First**, it is difficult for the model to acquire new knowledge through RL training. Instead, performance improvements come from increasing the probability that the model generates correct answers during inference. **Second**, we discover that simple rule-based RL exhibits outstanding generalization capabilities. Training solely on mathematical data leads to simultaneous improvements in physics, chemistry, biology, and other disciplines. **Third**, rule-based RL generalizes better than other post-training strategies such as SFT (Ouyang et al., 2022) and COT SFT (Guo et al., 2024) across various tasks.\n\nOur goal is to share our implementation experiences and complete the open-source pipeline with the community, including data, code, and models. We believe this comprehensive open-source framework would help the community better explore the multimodal reasoning task. The main contributions are summarized as follows:\n\n- • We utilize an online filter strategy and introduce a two-stage training strategy to address the collapse issues encountered during RL training of large-scale VLMs, achieving stable rule-based RL training for large-scale VLMs.\n- • We present MM-Eureka-7B and MM-Eureka-32B. Extensive experimental results on various downstream tasks demonstrate that they are top performers among open-source models in the multimodal reasoning domain. For example, MM-Eureka-32B scores only 1.7 points below o1 on the multidisciplinary evaluation set of MMK12; MM-Eureka-7B achieves 73.0 on MathVista (Lu et al., 2024), surpassing InternVL2.5-78B (Chen et al., 2024).\n- • We open-source all our models, code, and collected high-quality multimodal mathematical reasoning data. Compared to existing open-source repositories, we support a wider range of RL algorithms and include much higher-quality data.\n\n## 2 RELATED WORK\n\n### 2.1 LANGUAGE REASONING MODEL\n\nLLMs have demonstrated impressive performance across a wide range of tasks, yet more complex challenges require these models to exhibit human-like reasoning capabilities. As a result, enhancing the reasoning ability of LLMs has become a critical research focus. Reinforcement Learning from Human Feedback (RLHF), particularly Proximal Policy Optimization (PPO) (Schulman et al., 2017a), has shown promise in enabling LLMs to learn reasoning abilities effectively. However, the PPO training process is computationally intensive and complex, prompting the development of simplified alternatives such as Direct Preference Optimization (DPO) (Rafailov et al., 2023). WhileDPO alleviates some training difficulties, its reliance on offline data can limit model performance. To address these limitations, methods like Group Relative Policy Optimization (GRPO) (DeepSeek-AI et al., 2025), REINFORCE Leave-One-Out (RLOO) (Kool et al., 2019; Ahmadian et al., 2024), and Reinforce++ (Hu, 2025) have been introduced. Notably, Deepseek R1 (DeepSeek-AI et al., 2025) reveals that pure RL can encourage LLMs to actively engage in reasoning, including self-reflection and error correction. Despite these advancements, research on improving the reasoning capabilities of multimodal large models remains relatively scarce, highlighting an important direction for future exploration.\n\n## 2.2 VISION-LANGUAGE REASONING MODEL\n\nCurrently, the leading models in multimodal reasoning are closed-source systems such as GPT-4o (Hurst et al., 2024) and Kimi-VL (Team et al., 2025b). In contrast, the open-source community remains noticeably behind, still in the early stages of exploration. Recent concurrent efforts have begun to explore the use of RL to enhance the visual reasoning capabilities of vision-language reasoning models (VLMs), aiming to trigger an “Aha Moment” in visual reasoning. LMM-R1 (Peng et al., 2025) strengthens visual reasoning through a two-stage rule-based RL approach; however, its primary reasoning performance gains are derived from text-only datasets rather than genuinely multimodal datasets. R1-V (Chen et al., 2025) investigates rule-based RL within specific subdomains, such as geometric reasoning and object counting tasks, but falls short of addressing more complex reasoning challenges. Reason-RFT (Tan et al., 2025), on the other hand, relies on SFT with COT reasoning activation data to achieve an effective cold start before the RL training phase. In this paper, our objective is to develop an effective, stable, and comprehensive open-source training pipeline for multimodal reasoning models, including datasets, code, and models. Our work aims to advance the growth and innovation of the open-source community.\n\n## 3 MMK12: MULTIMODAL MATHEMATIC K12-LEVEL DATASET\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>&lt;/th>\n&lt;th>Scope&lt;/th>\n&lt;th>Type&lt;/th>\n&lt;th>Img. Source&lt;/th>\n&lt;th>QA Source&lt;/th>\n&lt;th>CoT Answer Source&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>MAVIS (Zhang et al., 2024b)&lt;/td>\n&lt;td>Geo &amp; Func&lt;/td>\n&lt;td>MCQ &amp; FB&lt;/td>\n&lt;td>Synthetic&lt;/td>\n&lt;td>Synthetic Engine&lt;/td>\n&lt;td>GPT-4o&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Geo3k (Lu et al., 2021)&lt;/td>\n&lt;td>Geo&lt;/td>\n&lt;td>FB&lt;/td>\n&lt;td>Real world&lt;/td>\n&lt;td>Real world&lt;/td>\n&lt;td>None&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RCOT (Deng et al., 2024)&lt;/td>\n&lt;td>Geo&lt;/td>\n&lt;td>MCQ &amp; FB&lt;/td>\n&lt;td>Synthetic&lt;/td>\n&lt;td>Synthetic Engine&lt;/td>\n&lt;td>GPT-4o&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MultiMath (Peng et al., 2024)&lt;/td>\n&lt;td>Diverse&lt;/td>\n&lt;td>MCQ &amp; FB&lt;/td>\n&lt;td>Real World&lt;/td>\n&lt;td>GPT-4o&lt;/td>\n&lt;td>GPT-4o&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MMK12&lt;/td>\n&lt;td>Diverse&lt;/td>\n&lt;td>FB&lt;/td>\n&lt;td>Real World&lt;/td>\n&lt;td>Real World&lt;/td>\n&lt;td>Real World&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nTable 1: Comparison of dataset characteristics with other multimodal mathematical reasoning datasets. MMK12 comprises more diverse and high quality questions, with guaranteed correct answers and solution processes.\n\nAs shown in Table 1, current multimodal mathematical reasoning datasets have limited scope and face challenges in ensuring answer correctness. For instance, while RCOT and MAVIS maintain answer accuracy through synthetic engine-generated QA pairs, this approach restricts problem diversity. Geo3k manually collected 3,000 geometry problems with verified answers, but it focuses solely on geometry examples. Although MultiMath gathers problems from real-world scenarios to ensure diversity, its reference answers generated by GPT-4o cannot guarantee correctness.\n\nTo address these limitations, we introduce MMK12, a new dataset comprising over 15,000 multimodal mathematical reasoning problems across a wide range of domains, including geometry, functions, and graphical reasoning. Each problem is accompanied by a standard reference answer and a detailed step-by-step solution to ensure both accuracy and interpretability.\n\nIn the following, we describe the construction and cleaning process of MMK12. As illustrated in Figure 2, we first collect a diverse set of multimodal mathematics problems and corresponding answers from a variety of Chinese mathematics textbooks and examination papers, covering grades from elementary to high school. These questions, answers, and COT processes are subsequently translated and refined into English, with the help of LLM. To minimize false positives during training, we retain only fill-in-the-blank problems. Besides, we use Math-Verify&lt;sup>†&lt;/sup> to parse\n\n&lt;sup>†&lt;/sup>&lt;https://github.com/huggingface/Math-Verify>The diagram illustrates the MMK12 construction pipeline. It begins with a collection of diverse K12-level multimodal math problems from various sources, including PDF, CSV, DOCX, and HTML files, along with images. These are processed through two parallel paths: 'Manual Annotation' and 'LLM Translation & Refinement'. The 'Manual Annotation' path involves human experts reviewing the data, while the 'LLM Translation & Refinement' path uses Large Language Models (LLMs) to translate the content into standardized English. The resulting 'Structured Data' is then subjected to a verification process. This process includes a 'Fill-in-the-blank?' check, which leads to 'Math-Verify' and 'Image size' checks, and a 'Multiple-choice?' check, which leads to 'Question type' and 'Single Image' checks. The final output is the 'MMK12 Training Dataset' and the 'MMK12 Benchmark'.\n\nFigure 2: The construction overview of MMK12. We collect diverse K12-level multimodal math problems from multiple sources, convert them to standardized English using LLMs, and verify all content for accuracy. The resulting MMK12 dataset includes a training set of 15,616 samples and a test set with 500 multiple-choice questions each for math, physics, chemistry, and biology.\n\nthe answer, ensuring data reliability for RL training. For the MMK12 evaluation set, we follow a similar construction procedure, but exclusively select multiple-choice questions to facilitate reliable and efficient evaluation.\n\nIn total, the MMK12 training dataset comprises 15,616 multimodal fill-in-the-blank mathematics problems, including 455 from elementary school, 9,776 from middle school, and 5,385 from high school. Each sample includes the question, an image, the final answer, and a CoT-formatted solution process. The MMK12 evaluation set has 2,000 multimodal multiple-choice questions, including math, physics, chemistry, and biology. Each item includes a question, a corresponding image, and the correct answer choice. Some examples in MMK12 are shown in Figure 1.\n\nMMK12 encompasses mathematical problems across various knowledge domains, including geometry, functions, spatial reasoning, and more. Some important categories are introduced as follows:\n\n- • **Function Reasoning:** This task requires models to understand function concepts, analyze function graphs and expressions, and apply function properties to solve problems. This type of reasoning develops the model’s ability to comprehend abstract mathematical concepts, fostering its capability to identify function characteristics, determine critical points, and analyze function behavior.\n- • **Geometric Reasoning:** This task involves applying spatial relationships, geometric theorems, and properties of shapes. Through geometric reasoning training, models enhance their spatial visualization, logical deduction, and formalization abilities for geometry problems, enabling them to solve complex problems in both plane and solid geometry.\n- • **Pattern Reasoning:** This type of task focuses on understanding flow diagrams and recognizing patterns in visual sequences. Models need to discover patterns, predict rule-based changes, or understand logical relationships in visual content. This task examines the model’s pattern recognition abilities, inductive reasoning skills, and visual logical thinking.\n\nBenefiting from a standardized data construction process with substantial human involvement and verification, MMK12 ensures both diversity in questions and correctness in answers and solution processes, making it suitable for various training methods such as RL and SFT for multimodal mathematical reasoning models. The MMK12 evaluation set also provides a convenient and accurate means to test models’ multidisciplinary reasoning capabilities.\n\n## 4 METHOD\n\n### 4.1 BASIC SETTINGS\n\nWe employ Qwen2.5-VL (Bai et al., 2023) with 7B and 32B as the base models. Our RL algorithm is similar to DeepSeek-R1 (DeepSeek-AI et al., 2025), using rule-based format rewards  $r_{\\text{format}} \\in \\{0, 0.5\\}$ , accuracy rewards  $r_{\\text{accuracy}} \\in \\{0, 1\\}$  as reward function and GRPO as base RL algorithm for training. Furthermore, we develop a multimodal input RL framework based on OpenRLHF (Hu et al., 2024), which is compatible with commonly used models such as InternVL (Chen et al., 2024) and QwenVL, supporting various model sizes and RL algorithms. In the following sections, we provide detailed settings for our RL training.## 4.2 REWARD FUNCTION\n\nFollowing DeepSeek-R1, we also adopt the simple rule-based reward function rather than using outcome or process reward models, thereby alleviating reward hacking (Gao et al., 2022). Specifically, we use two types of rewards: accuracy reward and format reward. The former uses Math-Verify to extract the answer from model responses and compare it with the reference one, returning 1 or 0 based on correctness; the latter checks whether the response follows the specified format (`&lt;think>...&lt;/think>&lt;answer>...&lt;/answer>`), returning 0.5 or 0 based on compliance. We find that this simple and sparse reward is sufficient to significantly improve the model’s multimodal reasoning ability.\n\n## 4.3 ADVANTAGE ESTIMATION AND POLICY UPDATE\n\nGroup Relative Policy Optimization (GRPO) (DeepSeek-AI et al., 2025) is a widely adopted RL algorithm that eliminates the need for training a complex critic model by leveraging intra-group relative performance to optimize the policy model. Specifically, for each query  $\\mathbf{x}$ , the model generates a group of  $G$  responses  $\\{\\mathbf{y}^{(1)}, \\mathbf{y}^{(2)}, \\dots, \\mathbf{y}^{(G)}\\}$ . Subsequently, for each query with  $G$  responses, GRPO computes the relative advantage of each response based on their rewards, which are determined by a reward model, as follows:\n\n$$A^{(i)} = \\frac{r^{(i)} - \\text{mean}(\\{r^{(j)}\\}_{j=1}^G)}{\\text{std}(\\{r^{(j)}\\}_{j=1}^G)}, \\quad i = 1, \\dots, G.$$\n\nUsing the computed advantages, GRPO then optimizes the policy via the PPO-clip loss augmented with a directly imposed KL penalty term:\n\n$$J_{\\text{PPO}}(\\theta) = -\\mathbb{E}_{\\mathbf{x} \\sim \\mathcal{D}, \\{\\mathbf{y}^{(i)}\\}_{i=1}^G \\sim \\pi_\\theta(\\cdot | \\mathbf{x})} \\left[ \\frac{1}{G} \\sum_{i=1}^G \\frac{1}{|\\mathbf{y}^{(i)}|} \\sum_{t=1}^{|\\mathbf{y}^{(i)}|} \\left( \\min \\left( r^{i,t}(\\theta) A^{(i)}, \\text{clip}(r^{i,t}(\\theta), 1 - \\epsilon, 1 + \\epsilon) A^{(i)} \\right) - \\beta D_{\\text{KL}}^{i,t}(\\pi_\\theta, \\pi_{\\text{ref}}) \\right) \\right], \\quad (1)$$\n\nwhere\n\n$$r^{i,t}(\\theta) = \\frac{\\pi_\\theta(y_t^{(i)} | \\mathbf{x}, \\mathbf{y}_{&lt;t}^{(i)})}{\\pi_{\\theta_{\\text{old}}}(y_t^{(i)} | \\mathbf{x}, \\mathbf{y}_{&lt;t}^{(i)})} \\text{ and } D_{\\text{KL}}^{i,t}(\\pi_\\theta, \\pi_{\\text{ref}}) = \\frac{\\pi_{\\text{ref}}(y_t^{(i)} | \\mathbf{x}, \\mathbf{y}_{&lt;t}^{(i)})}{\\pi_\\theta(y_t^{(i)} | \\mathbf{x}, \\mathbf{y}_{&lt;t}^{(i)})} - 1 - \\log \\frac{\\pi_{\\text{ref}}(y_t^{(i)} | \\mathbf{x}, \\mathbf{y}_{&lt;t}^{(i)})}{\\pi_\\theta(y_t^{(i)} | \\mathbf{x}, \\mathbf{y}_{&lt;t}^{(i)})}.$$\n\nIn addition, to mitigate loss spikes during training caused by excessively large policy ratios combined with negative advantages, we further constrain the policy ratio within  $[0, c]$  beforehand, i.e., we replace  $r^{i,t}(\\theta)$  with  $\\text{clip}(r^{i,t}(\\theta), 0, c)$  in Eq.(1). In practice, we set the default value of  $c$  to 3.\n\n## 4.4 ONLINE FILTERING\n\nTo further enhance training stability, we adopt the online prompt filtering strategy proposed in PRIME (Cui et al., 2025). To ensure sufficient gradient information throughout RL training, we filter out prompts with responses that are either completely correct or completely incorrect during training, as their corresponding advantages under GRPO are zero. The detailed process is shown in Algorithm 1.\n\nWe present an ablation study on the online filtering mechanism in Figure 3. Models trained with the online filter strategy maintain relatively stable trends in both the accuracy-based reward and response length throughout training. In contrast, models without the online filter show an initial improvement in accuracy, but soon experience a sharp decline, with accuracy eventually approaching zero and response lengths significantly shortening in the later stages. These findings suggest that the online filter plays an important role in stabilizing RL training and can help prevent model collapse during optimization.\n\n## 4.5 TWO-STAGE TRAINING\n\nDuring RL training of MM-Eureka-32B, we observe that maintaining training stability becomes increasingly challenging as model size scales up. Specifically, we find that models tend to experience**Algorithm 1** Online Filter\n\n**Input:** Prompt dataset  $\\mathcal{D}$ ; initial policy  $\\pi_\\theta$ ; reward model  $R$ ; buffer size  $N_B$ ; hyperparameters  $K_1, K_2, G, \\epsilon_{\\text{acc}}^{\\text{lower}}, \\epsilon_{\\text{acc}}^{\\text{upper}}$\n\n**Output:**  $\\pi_\\theta$\n\n```\n\n1: Buffer  $\\mathcal{B} \\leftarrow \\{\\}$ \n2: for iteration = 1, ...,  $K_1$  do\n3:   Sample a batch of prompts  $\\mathcal{Q} \\sim \\mathcal{D}$ \n4:   for each prompt  $\\mathbf{x} \\in \\mathcal{Q}$  do\n5:     Generate  $G$  responses  $\\{\\mathbf{y}^{(i)}\\}_{i=1}^G \\sim \\pi_\\theta(\\cdot|\\mathbf{x})$ \n6:     Compute the reward  $r^{(i)} = R(\\mathbf{x}, \\mathbf{y}^{(i)})$  for  $i = 1, \\dots, G$ \n7:     Compute the accuracy  $\\mathcal{C}_{\\mathbf{x}} = |\\{\\mathbf{y}^{(i)} | r^{(i)} = 1\\}|$ \n8:     if  $\\epsilon_{\\text{acc}}^{\\text{lower}} \\leq \\mathcal{C}_{\\mathbf{x}} \\leq \\epsilon_{\\text{acc}}^{\\text{upper}}$  then\n9:       Add the sample to the buffer  $\\mathcal{B} \\leftarrow \\mathcal{B} \\cup \\{(\\mathbf{x}, \\mathbf{y}^{(i)}, r^{(i)})\\}_{i=1}^G$ \n10:    end if\n11:  end for\n12:  if  $|\\mathcal{B}| \\geq N_B$  then\n13:    for Epoch = 1, ...,  $K_2$  do\n14:      Update policy  $\\pi_\\theta$  on  $\\mathcal{B}[0:N_B]$  by any RL algorithm\n15:    end for\n16:    Buffer  $\\mathcal{B} \\leftarrow \\{\\}$ \n17:  end if\n18: end for\n\n```\n\nFigure 3: Comparison of the use of online filtering. Using online filter makes the RL training more stable in the long term, with consistently increasing accuracy reward and response length.\n\nsudden collapse during training, characterized by an abrupt drop of the accuracy reward to near-zero values, as shown in Figure 5 (a). After analysis, we find that these collapses are usually preceded by sharp increases in the policy ratio (indicating excessively large updates from old to new policies) like Figure 5 (c). Additionally, unlike the 7B model which shows comprehensive improvement when trained solely on K12 data, the 32B model trained only on MMK12 exhibits performance degradation in specific domains such as geometry.\n\nTo address these challenges, we propose a two-stage training strategy for large models. In the first stage, we apply the GRPO algorithm without KL regularization, using MMK12 data collected as detailed in Section 3 to broadly enhance the model’s general reasoning capabilities. In the second stage, we incorporate a KL divergence into GRPO to constrain update magnitudes and improve training stability. Concurrently, we augment the training set with domain-specific Geo3k data to address identified performance gaps. As shown in Section 6.3, this two-stage approach enables stable training and yields further performance gains across nearly all evaluated benchmarks.\n\n## 5 EXPERIMENTS\n\nWe present our experimental setup in Section 5.1, where we indicate the training details. After that, we provide an overview of the selected baselines and evaluation benchmarks in Section 5.2 and Section 5.3, we demonstrate the superior effectiveness of MM-Eureka-7B and MM-Eureka-32B through extensive experiments in Section 5.4.## 5.1 EXPERIMENTS SETUP\n\nWe design our prompt template following the format used in DeepSeek-R1, wherein the system prompt explicitly specifies the required output structure, including the use of `&lt;answer>` tags to separate the reasoning process from the final answer. Detailed prompt configurations are provided in Table 2.\n\nFor training hyperparameters, both the rollout batch size and training batch size are set to 128, with 8 rollouts generated per sample. Sampling is conducted with a temperature of 1.0 to encourage response diversity, and optimization is performed using a learning rate of  $1 \\times 10^{-6}$ . Besides, for MM-Eureka-32B, we adopt a two-stage training scheme. In Stage 1, KL divergence is disabled to promote exploration and policy flexibility during the early phase. In Stage 2, a small KL penalty  $1 \\times 10^{-3}$  is introduced to stabilize training.\n\nTable 2: Prompt setting for MM-Eureka.\n\n---\n\n**SYSTEM:** Solve the question. The user asks a question, and you solve it. You first think about the reasoning process in the mind and then provide the user with the answer. The answer is in latex format and wrapped in `$...$`. The final answer must be wrapped using the `\\boxed{}` command. The answer should be enclosed within `&lt;answer>&lt;/answer>` tags, i.e., Since  $1+1=2$ , so the answer is  $\\boxed{2}$ . `&lt;answer>`The answer is  $\\boxed{2}$ `&lt;/answer>`, which means the final answer assistant’s output should start with `&lt;answer>` and end with `&lt;/answer>`.\n\n**USER:** `&lt;image><{{question}}&lt;/image>`\n\n---\n\n## 5.2 BASELINES\n\nTo comprehensively evaluate the effectiveness of MM-Eureka, we compare it against a diverse set of baselines, including both closed-source and open-source systems.\n\n**Closed-Source Models.** We include several leading proprietary models in our comparison. GPT-4o (Hurst et al., 2024), Claude3.7-Sonnet (Anthropic, 2024), and Gemini2-flash (Team et al., 2023) are general-purpose multimodal models without dedicated reasoning optimization, while o1 (OpenAI, 2024) is explicitly designed to enhance reasoning capabilities. These models serve as strong references for the current state of the art.\n\n**Open-Source General Models.** This group comprises high-capacity vision-language models trained for general purposes, including Qwen-2.5-VL (Bai et al., 2023) and InternVL2.5 (Chen et al., 2024) across various model sizes (7B to 78B). These models are primarily pretrained or instruction-tuned on large-scale image-text datasets. They offer a baseline for evaluating the impact of reasoning-specific post-training.\n\n**Open-Source Reasoning Models.** We further include open-source models explicitly fine-tuned for reasoning, such as InternVL2.5-MPO variants (Wang et al., 2024b), QVQ-72B-Preview (Team, 2024), Adora-7B (Gui & Ren, 2025), R1-Onevision (Yang et al., 2025), and OpenVLThinker (Deng et al., 2025). These models employ various strategies, including SFT (Ouyang et al., 2022), DPO (Rafailov et al., 2023), and rule-based reinforcement learning. They represent the most competitive open-source efforts in multimodal reasoning.\n\n## 5.3 BENCHMARKS\n\nTo assess the performance of our model, we conduct evaluations on multiple benchmark datasets, including MathVista(testmini) (Lu et al., 2024), MathVerse(testmini) (Zhang et al., 2024a), MathVision(test) (Wang et al., 2024a), OlympiadBench(EN-OE split) (He et al., 2024) and WeMath (Qiao et al., 2024). MathVista is one of the most widely used multimodal mathematical benchmarks, offering a diverse set of problems that span general visual question answering, figure question answering, logic, algebra, and geometry. MathVerse, on the other hand, focuses specifically on themodel’s ability to comprehend images, with tasks categorized into areas such as algebra and geometry. MathVision takes this a step further by emphasizing more abstract visual understanding, testing the model’s capacity for recognizing and reasoning beyond conventional mathematical contexts. OlympiadBench presents graduate-level mathematical competition problems, from which we select the English questions for evaluation. WeMath complements these by providing fine-grained diagnostic insights into model reasoning behavior, using a large-scale, hierarchically annotated problem set to assess knowledge mastery and generalization.\n\nBeyond these established benchmarks, both our model and the baselines are further evaluated on the proposed MMK12 Benchmark, as introduced in Section 3. Unlike OlympiadBench, which targets advanced graduate-level mathematical reasoning, MMK12 focuses on assessing the model’s ability to solve fundamental multimodal multidisciplinary problems commonly encountered in K12 education. MMK12 enables a comprehensive evaluation of a model’s ability across disciplines beyond mathematics.\n\nDuring evaluation, we adopt greedy decoding with a temperature of 0, ensuring deterministic outputs. We do not use beam search, and both top- $p$  and top- $k$  sampling are disabled.\n\n#### 5.4 QUANTITATIVE RESULTS\n\nIn this section, we demonstrate the superiority of MM-Eureka through its performance on the benchmarks introduced in Section 5.3. For the multimodal mathematical evaluation sets, we primarily use official results or results provided in VLMEvalKit (Duan et al., 2024) for baseline comparisons. When such results are unavailable, we conduct evaluations using the testing methodologies provided in VLMEvalKit within our vllm-based (Kwon et al., 2023) inference framework. Specifically, for o1, due to resource constraints, we randomly sample only 500 instances for testing. For the MMK12 evaluation set, considering it consists entirely of multiple-choice questions, we use the same Chain-of-Thought prompt structure from WeMath (Qiao et al., 2024) to test models within our inference framework. Because WeMath also consists entirely of multiple-choice questions. Results evaluated by ourselves are presented in *italics*.\n\n**Mathematics** In Table 3, we present a comprehensive summary of MM-Eurekas’ performance across different multimodal mathematical reasoning tasks. It demonstrates that both MM-Eureka-7B and MM-Eureka-32B consistently outperform similar-sized open-source baselines across almost all tasks. In particular, MM-Eureka-7B achieves 73.0 on Mathvista, surpassing InternVL-78B by 0.7% and the reasoning-focused InternVL2.5-38B-MPO by 0.2%. On WeMath, it similarly approaches the performance of InternVL-78B. MM-Eureka-32B exceeds all current open-source models of comparable size on all benchmarks except MathVision, with average performance approaching Qwen-72B-Instruct. It even outperforms the closed-source model Claude3.7 Sonnet on WeMath. In summary, MM-Eureka establishes itself as the top performer among same-sized open-source models across almost all multimodal mathematical reasoning tasks, regardless of whether considering the 7B or 32B version.\n\nHowever, when compared to closed-source models, MM-Eureka-32B still shows considerable performance gaps. While it outperforms o1 on Mathvista, it lags significantly behind closed-source multimodal reasoning models like o1 on more challenging benchmarks such as Mathvision or OlympiadBench.\n\n**MMK12** Beyond validating our model’s superiority on widely-used multimodal mathematical reasoning benchmarks like MathVista, it is necessary to test its capabilities and generalization across multidisciplinary reasoning domains using questions absent from the training set (e.g., physics, chemistry, and biology). For this purpose, we employ the MMK12 dataset constructed in Section 3, which can effectively measure models’ multimodal reasoning capabilities across multiple disciplines.\n\nAs shown in Table 4, MM-Eureka-32B demonstrates multidisciplinary capabilities only marginally behind o1 by 1.7%, while outperforming larger-scale models such as Qwen-2.5-VL-72B and\n\n&lt;sup>†&lt;/sup>Results of o1 based on random sampling of 500 test instances due to resource constraints.\n\n&lt;sup>‡&lt;/sup>Results of R1-Onevision in Mathvision is 23.5 from our evaluation, which is far behind its official report as 29.9.Table 3: Performance comparison across different multimodal mathematical benchmarks. Bold indicates the top performer with the open-source models, while underline indicates the second best performer within open-source models. For some official results that are relatively different from our evaluation results, we mark our test results after ’/’.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Model&lt;/th>\n&lt;th>MathVista&lt;/th>\n&lt;th>MathVerse&lt;/th>\n&lt;th>Mathvision&lt;/th>\n&lt;th>OlypamidBench&lt;/th>\n&lt;th>WeMath&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td colspan=\"6\">&lt;b>Closed-Source Models&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Claude3.7-Sonnet&lt;/td>\n&lt;td>66.8&lt;/td>\n&lt;td>52.0&lt;/td>\n&lt;td>41.3&lt;/td>\n&lt;td>48.9&lt;/td>\n&lt;td>72.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GPT-4o&lt;/td>\n&lt;td>63.8&lt;/td>\n&lt;td>50.2&lt;/td>\n&lt;td>30.4&lt;/td>\n&lt;td>35.0&lt;/td>\n&lt;td>68.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>o1&lt;/td>\n&lt;td>73.9&lt;/td>\n&lt;td>57.0&lt;/td>\n&lt;td>60.3&lt;/td>\n&lt;td>68.0*&lt;/td>\n&lt;td>98.7*&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Gemini2-flash&lt;/td>\n&lt;td>70.4&lt;/td>\n&lt;td>59.3&lt;/td>\n&lt;td>41.3&lt;/td>\n&lt;td>51.0&lt;/td>\n&lt;td>71.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"6\">&lt;b>Open-Source General Models&lt;/b>&lt;/td>",
      "numLines": 300,
      "startLine": 1,
      "totalLines": 1106
    }
  },
  "sourceToolAssistantUUID": "fa2e1461-2035-4314-a5df-8efd9070505b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 37_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-27 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "384a999b-4118-4f65-90d3-a5e7e9169bb6",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze MM-Eureka multimodal reasoning paper",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6"
}
```

---

### Tool call

_source line 39 · 2026-05-27T16:04:32.459Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XYWsJQGJHStEfM6fq3xGwY`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/85dae6a1-bcc0-4c8f-97a6-84608d21f8c6/tool-results/toolu_01KEj67Agphd4njkFJNjphT6.txt",
  "offset": 300,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "384a999b-4118-4f65-90d3-a5e7e9169bb6",
  "isSidechain": false,
  "requestId": "req_011CbTMhSJoGwc3QR2bEYxyD",
  "type": "assistant",
  "uuid": "1ccf7036-611a-4cd7-a408-a4e59e750013",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NVQuLG5XtzSvwcJ1Z7yuaX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11454,
      "cache_read_input_tokens": 16676,
      "output_tokens": 163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11454,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 163,
          "cache_read_input_tokens": 16676,
          "cache_creation_input_tokens": 11454,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11454
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

_source line 40 · 2026-05-27T16:04:32.465Z_

<details><summary>↩ Tool result · `toolu_01XYWsJQGJHStEfM6fq3xGwY`</summary>

```text
300	&lt;td colspan="6">&lt;b>Open-Source General Models&lt;/b>&lt;/td>
301	&lt;/tr>
302	&lt;tr>
303	&lt;td>InternVL2.5-VL-8B&lt;/td>
304	&lt;td>64.4&lt;/td>
305	&lt;td>39.5&lt;/td>
306	&lt;td>19.7&lt;/td>
307	&lt;td>12.3&lt;/td>
308	&lt;td>53.5&lt;/td>
309	&lt;/tr>
310	&lt;tr>
311	&lt;td>Qwen-2.5-VL-7B&lt;/td>
312	&lt;td>68.2&lt;/td>
313	&lt;td>47.9&lt;/td>
314	&lt;td>25.4&lt;/td>
315	&lt;td>20.2&lt;/td>
316	&lt;td>62.1&lt;/td>
317	&lt;/tr>
318	&lt;tr>
319	&lt;td>InternVL2.5-VL-38B&lt;/td>
320	&lt;td>71.9&lt;/td>
321	&lt;td>49.4&lt;/td>
322	&lt;td>31.8&lt;/td>
323	&lt;td>32.0&lt;/td>
324	&lt;td>67.5&lt;/td>
325	&lt;/tr>
326	&lt;tr>
327	&lt;td>Qwen-2.5-VL-32B&lt;/td>
328	&lt;td>74.7/71.7&lt;/td>
329	&lt;td>49.9&lt;/td>
330	&lt;td>&lt;b>40.1&lt;/b>&lt;/td>
331	&lt;td>30.0&lt;/td>
332	&lt;td>69.1&lt;/td>
333	&lt;/tr>
334	&lt;tr>
335	&lt;td>InternVL2.5-VL-78B&lt;/td>
336	&lt;td>72.3&lt;/td>
337	&lt;td>51.7&lt;/td>
338	&lt;td>32.2&lt;/td>
339	&lt;td>31.1&lt;/td>
340	&lt;td>66.3&lt;/td>
341	&lt;/tr>
342	&lt;tr>
343	&lt;td>Qwen-2.5-VL-72B&lt;/td>
344	&lt;td>&lt;b>74.8&lt;/b>&lt;/td>
345	&lt;td>&lt;b>57.6&lt;/b>&lt;/td>
346	&lt;td>&lt;u>38.1&lt;/u>&lt;/td>
347	&lt;td>&lt;b>40.4&lt;/b>&lt;/td>
348	&lt;td>&lt;u>72.4&lt;/u>&lt;/td>
349	&lt;/tr>
350	&lt;tr>
351	&lt;td colspan="6">&lt;b>Open-Source Reasoning Models&lt;/b>&lt;/td>
352	&lt;/tr>
353	&lt;tr>
354	&lt;td>InternVL2.5-8B-MPO&lt;/td>
355	&lt;td>68.9&lt;/td>
356	&lt;td>35.5&lt;/td>
357	&lt;td>21.5&lt;/td>
358	&lt;td>7.8&lt;/td>
359	&lt;td>53.5&lt;/td>
360	&lt;/tr>
361	&lt;tr>
362	&lt;td>InternVL2.5-38B-MPO&lt;/td>
363	&lt;td>73.8&lt;/td>
364	&lt;td>46.5&lt;/td>
365	&lt;td>32.3&lt;/td>
366	&lt;td>25.6&lt;/td>
367	&lt;td>66.2&lt;/td>
368	&lt;/tr>
369	&lt;tr>
370	&lt;td>QVQ-72B-Preview&lt;/td>
371	&lt;td>71.4&lt;/td>
372	&lt;td>48.2&lt;/td>
373	&lt;td>35.9&lt;/td>
374	&lt;td>33.2&lt;/td>
375	&lt;td>65.4&lt;/td>
376	&lt;/tr>
377	&lt;tr>
378	&lt;td>Adora-7B&lt;/td>
379	&lt;td>73.5&lt;/td>
380	&lt;td>50.1&lt;/td>
381	&lt;td>23.0&lt;/td>
382	&lt;td>20.1&lt;/td>
383	&lt;td>64.2&lt;/td>
384	&lt;/tr>
385	&lt;tr>
386	&lt;td>R1-Onevision-7B&lt;/td>
387	&lt;td>64.1&lt;/td>
388	&lt;td>47.1&lt;/td>
389	&lt;td>29.9/23.5&lt;/td>
390	&lt;td>17.3&lt;/td>
391	&lt;td>61.8&lt;/td>
392	&lt;/tr>
393	&lt;tr>
394	&lt;td>OpenVLThinker-7B&lt;/td>
395	&lt;td>70.2&lt;/td>
396	&lt;td>47.9&lt;/td>
397	&lt;td>25.3&lt;/td>
398	&lt;td>20.1&lt;/td>
399	&lt;td>64.3&lt;/td>
400	&lt;/tr>
401	&lt;tr>
402	&lt;td colspan="6">&lt;b>Ours&lt;/b>&lt;/td>
403	&lt;/tr>
404	&lt;tr>
405	&lt;td>MM-Eureka-7B&lt;/td>
406	&lt;td>73.0&lt;/td>
407	&lt;td>50.3&lt;/td>
408	&lt;td>26.9&lt;/td>
409	&lt;td>20.1&lt;/td>
410	&lt;td>66.1&lt;/td>
411	&lt;/tr>
412	&lt;tr>
413	&lt;td>MM-Eureka-32B&lt;/td>
414	&lt;td>&lt;b>74.8&lt;/b>&lt;/td>
415	&lt;td>&lt;u>56.5&lt;/u>&lt;/td>
416	&lt;td>34.4&lt;/td>
417	&lt;td>&lt;u>35.9&lt;/u>&lt;/td>
418	&lt;td>&lt;b>73.4&lt;/b>&lt;/td>
419	&lt;/tr>
420	&lt;/tbody>
421	&lt;/table>
422	
423	Gemini2-Flash-Thinking. MM-Eureka-7B also surpasses several similarly-sized multimodal reasoning models, including OpenVLThinker-7B, with overall performance exceeding InternVL2.5-VL-78B and only slightly behind Qwen-2.5-VL-32B. Additionally, we observe several interesting findings: 1) Despite being trained exclusively on fill-in-the-blank questions, our models maintain strong instruction-following abilities for multiple-choice questions with improved performance. 2) Even with training solely on mathematics problems, the models exhibit enhanced capabilities in physics, chemistry, and biology. Specifically, MM-Eureka-7B shows improvements of 9.8% and 11.2% in chemistry and biology, respectively, demonstrating the remarkable generalization capacity of our straightforward RL strategy.
424	
425	## 5.5 QUALITATIVE RESULTS
426	
427	Appendix A illustrates representative examples comparing MM-Eureka-32B with its base model Qwen2.5-VL-32B-Instruct across four subjects: mathematics, physics, chemistry, and biology. These qualitative cases reveal that our model, after reinforcement learning, demonstrates significantly enhanced reasoning capabilities. Specifically, MM-Eureka-32B is able to better apply known concepts and perform multi-step deduction to arrive at the correct answers. In contrast, the base model often shows surface-level understanding—it may recall relevant facts but fails to apply them coherently in the problem-solving context.
428	
429	For instance, in the physics example (Figure 7), the question involves analyzing the instantaneous contact force between two objects placed on a vertical spring. While both models recognize key physical quantities such as mass, weight, and spring force, only MM-Eureka-32B correctly applies Newton’s second law to derive the acceleration of the system and compute the contact force. It identifies that the net external force due to the added mass leads to a downward acceleration, and accurately calculates the resulting contact force between object A and B as  $24N$ . In contrast, the base model Qwen2.5-VL-32B-Instruct incorrectly concludes that the contact force equals the full weightTable 4: Performance comparison across different disciplines in MMK12. Bold indicates the top performer with the open-source models, while underline indicates the second best performer within open-source models.
430	
431	&lt;table border="1">
432	&lt;thead>
433	&lt;tr>
434	&lt;th>Model&lt;/th>
435	&lt;th>Mathematics&lt;/th>
436	&lt;th>Physics&lt;/th>
437	&lt;th>Chemistry&lt;/th>
438	&lt;th>Biology&lt;/th>
439	&lt;th>Avg.&lt;/th>
440	&lt;/tr>
441	&lt;/thead>
442	&lt;tbody>
443	&lt;tr>
444	&lt;td colspan="6">&lt;b>Closed-Source Models&lt;/b>&lt;/td>
445	&lt;/tr>
446	&lt;tr>
447	&lt;td>Claude3.7-Sonnet&lt;/td>
448	&lt;td>57.4&lt;/td>
449	&lt;td>53.4&lt;/td>
450	&lt;td>55.4&lt;/td>
451	&lt;td>55.0&lt;/td>
452	&lt;td>55.3&lt;/td>
453	&lt;/tr>
454	&lt;tr>
455	&lt;td>GPT-4o&lt;/td>
456	&lt;td>55.8&lt;/td>
457	&lt;td>41.2&lt;/td>
458	&lt;td>47.0&lt;/td>
459	&lt;td>55.4&lt;/td>
460	&lt;td>49.9&lt;/td>
461	&lt;/tr>
462	&lt;tr>
463	&lt;td>o1&lt;/td>
464	&lt;td>81.6&lt;/td>
465	&lt;td>68.8&lt;/td>
466	&lt;td>71.4&lt;/td>
467	&lt;td>74.0&lt;/td>
468	&lt;td>73.9&lt;/td>
469	&lt;/tr>
470	&lt;tr>
471	&lt;td>Gemini2-flash&lt;/td>
472	&lt;td>76.8&lt;/td>
473	&lt;td>53.6&lt;/td>
474	&lt;td>64.6&lt;/td>
475	&lt;td>66.0&lt;/td>
476	&lt;td>65.2&lt;/td>
477	&lt;/tr>
478	&lt;tr>
479	&lt;td colspan="6">&lt;b>Open-Source General Models&lt;/b>&lt;/td>
480	&lt;/tr>
481	&lt;tr>
482	&lt;td>InternVL2.5-VL-8B&lt;/td>
483	&lt;td>46.8&lt;/td>
484	&lt;td>35.0&lt;/td>
485	&lt;td>50.0&lt;/td>
486	&lt;td>50.8&lt;/td>
487	&lt;td>45.6&lt;/td>
488	&lt;/tr>
489	&lt;tr>
490	&lt;td>Qwen-2.5-VL-7B&lt;/td>
491	&lt;td>58.4&lt;/td>
492	&lt;td>45.4&lt;/td>
493	&lt;td>56.4&lt;/td>
494	&lt;td>54.0&lt;/td>
495	&lt;td>53.6&lt;/td>
496	&lt;/tr>
497	&lt;tr>
498	&lt;td>InternVL2.5-VL-38B&lt;/td>
499	&lt;td>61.6&lt;/td>
500	&lt;td>49.8&lt;/td>
501	&lt;td>60.4&lt;/td>
502	&lt;td>60.0&lt;/td>
503	&lt;td>58.0&lt;/td>
504	&lt;/tr>
505	&lt;tr>
506	&lt;td>Qwen-2.5-VL-32B&lt;/td>
507	&lt;td>71.6&lt;/td>
508	&lt;td>59.4&lt;/td>
509	&lt;td>69.6&lt;/td>
510	&lt;td>66.6&lt;/td>
511	&lt;td>66.8&lt;/td>
512	&lt;/tr>
513	&lt;tr>
514	&lt;td>InternVL2.5-VL-78B&lt;/td>
515	&lt;td>59.8&lt;/td>
516	&lt;td>53.2&lt;/td>
517	&lt;td>68.0&lt;/td>
518	&lt;td>65.2&lt;/td>
519	&lt;td>61.6&lt;/td>
520	&lt;/tr>
521	&lt;tr>
522	&lt;td>Qwen-2.5-VL-72B&lt;/td>
523	&lt;td>&lt;b>75.6&lt;/b>&lt;/td>
524	&lt;td>&lt;b>64.8&lt;/b>&lt;/td>
525	&lt;td>69.6&lt;/td>
526	&lt;td>72.0&lt;/td>
527	&lt;td>70.5&lt;/td>
528	&lt;/tr>
529	&lt;tr>
530	&lt;td colspan="6">&lt;b>Open-Source Reasoning Models&lt;/b>&lt;/td>
531	&lt;/tr>
532	&lt;tr>
533	&lt;td>InternVL2.5-8B-MPO&lt;/td>
534	&lt;td>26.6&lt;/td>
535	&lt;td>25.0&lt;/td>
536	&lt;td>42.4&lt;/td>
537	&lt;td>44.0&lt;/td>
538	&lt;td>34.5&lt;/td>
539	&lt;/tr>
540	&lt;tr>
541	&lt;td>InternVL2.5-38B-MPO&lt;/td>
542	&lt;td>41.4&lt;/td>
543	&lt;td>42.8&lt;/td>
544	&lt;td>55.8&lt;/td>
545	&lt;td>53.2&lt;/td>
546	&lt;td>48.3&lt;/td>
547	&lt;/tr>
548	&lt;tr>
549	&lt;td>QVQ-72B-Preview&lt;/td>
550	&lt;td>61.4&lt;/td>
551	&lt;td>57.4&lt;/td>
552	&lt;td>62.6&lt;/td>
553	&lt;td>64.4&lt;/td>
554	&lt;td>61.5&lt;/td>
555	&lt;/tr>
556	&lt;tr>
557	&lt;td>Adora&lt;/td>
558	&lt;td>63.6&lt;/td>
559	&lt;td>50.6&lt;/td>
560	&lt;td>59.0&lt;/td>
561	&lt;td>59.0&lt;/td>
562	&lt;td>58.1&lt;/td>
563	&lt;/tr>
564	&lt;tr>
565	&lt;td>R1-Onevision&lt;/td>
566	&lt;td>44.8&lt;/td>
567	&lt;td>33.8&lt;/td>
568	&lt;td>39.8&lt;/td>
569	&lt;td>40.8&lt;/td>
570	&lt;td>39.8&lt;/td>
571	&lt;/tr>
572	&lt;tr>
573	&lt;td>OpenVLThinker-7&lt;/td>
574	&lt;td>63.0&lt;/td>
575	&lt;td>53.8&lt;/td>
576	&lt;td>60.6&lt;/td>
577	&lt;td>65.0&lt;/td>
578	&lt;td>60.6&lt;/td>
579	&lt;/tr>
580	&lt;tr>
581	&lt;td colspan="6">&lt;b>Ours&lt;/b>&lt;/td>
582	&lt;/tr>
583	&lt;tr>
584	&lt;td>MM-Eureka-7B&lt;/td>
585	&lt;td>71.2&lt;/td>
586	&lt;td>56.2&lt;/td>
587	&lt;td>65.2&lt;/td>
588	&lt;td>65.2&lt;/td>
589	&lt;td>64.5&lt;/td>
590	&lt;/tr>
591	&lt;tr>
592	&lt;td>MM-Eureka-32B&lt;/td>
593	&lt;td>&lt;u>74.6&lt;/u>&lt;/td>
594	&lt;td>&lt;u>62.0&lt;/u>&lt;/td>
595	&lt;td>&lt;b>75.4&lt;/b>&lt;/td>
596	&lt;td>&lt;b>76.8&lt;/b>&lt;/td>
597	&lt;td>&lt;b>72.2&lt;/b>&lt;/td>
598	&lt;/tr>
599	&lt;/tbody>
600	&lt;/table>
601	
602	of object B (i.e.,  $40N$ ), failing to consider the transient acceleration of the system and misapplying Newtonian mechanics.
603	
604	These examples highlight MM-Eureka’s improved ability to perform reasoning and its potential to generalize reasoning patterns across disciplines. Further cases in mathematics, chemistry, and biology show similar trends, where our model more effectively breaks down problems into intermediate steps and synthesizes knowledge to reach accurate conclusions.
605	
606	## 6 DISCUSSION
607	
608	### 6.1 ARE KNOWLEDGE AND REASONING DECOUPLED?
609	
610	Figure 4 presents the distribution of correct answers across 8 responses from the Qwen-2.5-VL-32B and MM-Eureka-32B models on the Mathematics dataset. It is evident that, for problems that were initially answered correctly at least once, Eureka shows a significant improvement in accuracy. However, the number of problems that initially had zero correct answers remains nearly unchanged. We hypothesize that this improvement is due to Eureka’s improved reasoning capabilities, developed through RL training, allowing it to better leverage existing knowledge and thus improve the accuracy on partially understood problems. Nonetheless, relying solely on reasoning is insufficient to solve problems the model originally cannot answer, which is why the accuracy for problems with zero correct answers remains almost unchanged.
611	
612	Figure ?? shows the responses from Qwen-2.5-VL-32B and MM-Eureka-32B to the same question from Mathematics (the full version is provided in Appendix). From the responses, we observe that although Qwen possesses the necessary knowledge to answer the question, it still struggles to provide the correct answer. In contrast, Eureka is able to better reason with the available knowledge and derive the correct answer. Table 5 further illustrates that, despite Eureka’s training set beingFigure 4: Distribution of correct answers across 8 responses from Qwen-2.5-VL-32B and MM-Eureka-32B on *Mathematics*.
613	
614	focused only on mathematics, it also demonstrates a notable improvement in answering questions from other domains such as physics, chemistry, and biology.
615	
616	Our experimental results to some extent support the view that knowledge and reasoning in LLMs/VLMs can be decoupled, and to some extent indicate that learning knowledge and learning reasoning can be conducted separately during the training process. Therefore, a key direction for future research is to explore how to generalize the reasoning capabilities, developed from data like mathematics—where logic is clear, responses are structured, and answers are verifiable—into broader, more general domains.
617	
618	## 6.2 RL GENERALIZES BETTER THAN SFT
619	
620	We maintain consistent settings with our RL training to compare different post-training strategies including SFT and COT SFT. Using the ms-swift framework (Zhao et al., 2024), we conduct both SFT and COT SFT training for 10 epochs with identical data. As shown in Table 5, results demonstrate that RL exhibits superior generalization compared to SFT or COT SFT approaches, particularly with more significant improvements on OOD test sets such as Physics, Chemistry, and Biology. Furthermore, RL enhances the model’s reasoning capabilities more effectively—while SFT and COT SFT fail to substantially improve performance on mathematics and physics problems, RL training increases the model’s scores in mathematics and physics by 12.8 and 10.8 points respectively.
621	
622	Table 5: Performance comparison of different training methods on MMK12. In terms of both enhancing mathematical capabilities and generalizing to other disciplines, RL significantly outperforms SFT or COT SFT.
623	
624	&lt;table border="1">
625	&lt;thead>
626	&lt;tr>
627	&lt;th>Model&lt;/th>
628	&lt;th>Mathematics&lt;/th>
629	&lt;th>Physics&lt;/th>
630	&lt;th>Chemistry&lt;/th>
631	&lt;th>Biology&lt;/th>
632	&lt;th>Avg.&lt;/th>
633	&lt;/tr>
634	&lt;/thead>
635	&lt;tbody>
636	&lt;tr>
637	&lt;td>Qwen-2.5-VL-7B&lt;/td>
638	&lt;td>58.4&lt;/td>
639	&lt;td>45.4&lt;/td>
640	&lt;td>56.4&lt;/td>
641	&lt;td>54.0&lt;/td>
642	&lt;td>53.5&lt;/td>
643	&lt;/tr>
644	&lt;tr>
645	&lt;td>+ SFT&lt;/td>
646	&lt;td>56.6&lt;/td>
647	&lt;td>50.0&lt;/td>
648	&lt;td>63.2&lt;/td>
649	&lt;td>61.2&lt;/td>
650	&lt;td>57.7&lt;/td>
651	&lt;/tr>
652	&lt;tr>
653	&lt;td>+ COT SFT&lt;/td>
654	&lt;td>59.2&lt;/td>
655	&lt;td>46.0&lt;/td>
656	&lt;td>62.2&lt;/td>
657	&lt;td>61.2&lt;/td>
658	&lt;td>57.1&lt;/td>
659	&lt;/tr>
660	&lt;tr>
661	&lt;td>+ RL&lt;/td>
662	&lt;td>&lt;b>71.2&lt;/b>&lt;/td>
663	&lt;td>&lt;b>56.2&lt;/b>&lt;/td>
664	&lt;td>&lt;b>65.2&lt;/b>&lt;/td>
665	&lt;td>&lt;b>65.0&lt;/b>&lt;/td>
666	&lt;td>&lt;b>64.5&lt;/b>&lt;/td>
667	&lt;/tr>
668	&lt;/tbody>
669	&lt;/table>
670	
671	## 6.3 TWO-STAGE TRAINING
672	
673	In Section 4.5, we introduce a two-stage RL training strategy. Stage 1 employs K12 data to enhance general knowledge reasoning capabilities, while stage 2 utilizes Geo3k data to address specific performance gaps. Additionally, we omit the KL divergence in stage one to accelerate training and then incorporate it in stage two to maintain training stability.Figure 5: (a) MM-Eureka-32B tends to experience sudden training collapse during RL training, manifested as accuracy reward approaching zero. (b) During the second training phase, adding KL divergence leads to more stable training with steadily increasing accuracy rewards. (c) The stabilizing effect of KL divergence in the second phase may be attributed to the stabilization of the policy ratio, as ratio instability often leads to training collapse.
674	
675	As shown in Figure 5 (a), continuous training without KL divergence often leads to sudden model collapse. We identify this phenomenon results from ratio instability (excessive updates in the new policy). As shown in Figures 5 (b) and (c), which present training metrics with and without the use of KL divergence in the second stage, a sharp fluctuation in the ratio is observed when the model begins to collapse. To mitigate this issue of ratio instability, we introduce a KL divergence term during the second stage of training, which helps to stabilize the learning dynamics.
676	
677	Furthermore, Table 6 demonstrates that after the first training stage, despite overall performance improvements, capabilities in certain specific domains actually decline, as evidenced by MathVista’s geometry problem solving(GPS) score dropping from 74.0 to 56.7. To address this, we implement second-stage training using Geo3k, which yields further improvements across multiple mathematical benchmarks.
678	
679	Table 6: Performance comparison across multimodal mathematical benchmarks of the two stage training strategy. The second phase of training enhances various capabilities of the model following the first phase, with particularly significant improvements in geometric reasoning abilities.
680	
681	&lt;table border="1">
682	&lt;thead>
683	&lt;tr>
684	&lt;th>Model&lt;/th>
685	&lt;th>Data Scale&lt;/th>
686	&lt;th>MathVista&lt;/th>
687	&lt;th>MathVista(GPS)&lt;/th>
688	&lt;th>MathVerse&lt;/th>
689	&lt;th>Mathvision&lt;/th>
690	&lt;th>WeMath&lt;/th>
691	&lt;/tr>
692	&lt;/thead>
693	&lt;tbody>
694	&lt;tr>
695	&lt;td>Stage1&lt;/td>
696	&lt;td>15k&lt;/td>
697	&lt;td>72.0&lt;/td>
698	&lt;td>56.7&lt;/td>
699	&lt;td>56.4&lt;/td>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ccf7036-611a-4cd7-a408-a4e59e750013",
  "isSidechain": false,
  "promptId": "6e9b4775-3324-430a-aeff-baabf4898966",
  "type": "user",
  "uuid": "4e2f5d07-d7be-49a4-948e-b5f1d0d59c93",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/85dae6a1-bcc0-4c8f-97a6-84608d21f8c6/tool-results/toolu_01KEj67Agphd4njkFJNjphT6.txt",
      "content": "&lt;td colspan=\"6\">&lt;b>Open-Source General Models&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>InternVL2.5-VL-8B&lt;/td>\n&lt;td>64.4&lt;/td>\n&lt;td>39.5&lt;/td>\n&lt;td>19.7&lt;/td>\n&lt;td>12.3&lt;/td>\n&lt;td>53.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen-2.5-VL-7B&lt;/td>\n&lt;td>68.2&lt;/td>\n&lt;td>47.9&lt;/td>\n&lt;td>25.4&lt;/td>\n&lt;td>20.2&lt;/td>\n&lt;td>62.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>InternVL2.5-VL-38B&lt;/td>\n&lt;td>71.9&lt;/td>\n&lt;td>49.4&lt;/td>\n&lt;td>31.8&lt;/td>\n&lt;td>32.0&lt;/td>\n&lt;td>67.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen-2.5-VL-32B&lt;/td>\n&lt;td>74.7/71.7&lt;/td>\n&lt;td>49.9&lt;/td>\n&lt;td>&lt;b>40.1&lt;/b>&lt;/td>\n&lt;td>30.0&lt;/td>\n&lt;td>69.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>InternVL2.5-VL-78B&lt;/td>\n&lt;td>72.3&lt;/td>\n&lt;td>51.7&lt;/td>\n&lt;td>32.2&lt;/td>\n&lt;td>31.1&lt;/td>\n&lt;td>66.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen-2.5-VL-72B&lt;/td>\n&lt;td>&lt;b>74.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>57.6&lt;/b>&lt;/td>\n&lt;td>&lt;u>38.1&lt;/u>&lt;/td>\n&lt;td>&lt;b>40.4&lt;/b>&lt;/td>\n&lt;td>&lt;u>72.4&lt;/u>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"6\">&lt;b>Open-Source Reasoning Models&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>InternVL2.5-8B-MPO&lt;/td>\n&lt;td>68.9&lt;/td>\n&lt;td>35.5&lt;/td>\n&lt;td>21.5&lt;/td>\n&lt;td>7.8&lt;/td>\n&lt;td>53.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>InternVL2.5-38B-MPO&lt;/td>\n&lt;td>73.8&lt;/td>\n&lt;td>46.5&lt;/td>\n&lt;td>32.3&lt;/td>\n&lt;td>25.6&lt;/td>\n&lt;td>66.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>QVQ-72B-Preview&lt;/td>\n&lt;td>71.4&lt;/td>\n&lt;td>48.2&lt;/td>\n&lt;td>35.9&lt;/td>\n&lt;td>33.2&lt;/td>\n&lt;td>65.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Adora-7B&lt;/td>\n&lt;td>73.5&lt;/td>\n&lt;td>50.1&lt;/td>\n&lt;td>23.0&lt;/td>\n&lt;td>20.1&lt;/td>\n&lt;td>64.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>R1-Onevision-7B&lt;/td>\n&lt;td>64.1&lt;/td>\n&lt;td>47.1&lt;/td>\n&lt;td>29.9/23.5&lt;/td>\n&lt;td>17.3&lt;/td>\n&lt;td>61.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>OpenVLThinker-7B&lt;/td>\n&lt;td>70.2&lt;/td>\n&lt;td>47.9&lt;/td>\n&lt;td>25.3&lt;/td>\n&lt;td>20.1&lt;/td>\n&lt;td>64.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"6\">&lt;b>Ours&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MM-Eureka-7B&lt;/td>\n&lt;td>73.0&lt;/td>\n&lt;td>50.3&lt;/td>\n&lt;td>26.9&lt;/td>\n&lt;td>20.1&lt;/td>\n&lt;td>66.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MM-Eureka-32B&lt;/td>\n&lt;td>&lt;b>74.8&lt;/b>&lt;/td>\n&lt;td>&lt;u>56.5&lt;/u>&lt;/td>\n&lt;td>34.4&lt;/td>\n&lt;td>&lt;u>35.9&lt;/u>&lt;/td>\n&lt;td>&lt;b>73.4&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nGemini2-Flash-Thinking. MM-Eureka-7B also surpasses several similarly-sized multimodal reasoning models, including OpenVLThinker-7B, with overall performance exceeding InternVL2.5-VL-78B and only slightly behind Qwen-2.5-VL-32B. Additionally, we observe several interesting findings: 1) Despite being trained exclusively on fill-in-the-blank questions, our models maintain strong instruction-following abilities for multiple-choice questions with improved performance. 2) Even with training solely on mathematics problems, the models exhibit enhanced capabilities in physics, chemistry, and biology. Specifically, MM-Eureka-7B shows improvements of 9.8% and 11.2% in chemistry and biology, respectively, demonstrating the remarkable generalization capacity of our straightforward RL strategy.\n\n## 5.5 QUALITATIVE RESULTS\n\nAppendix A illustrates representative examples comparing MM-Eureka-32B with its base model Qwen2.5-VL-32B-Instruct across four subjects: mathematics, physics, chemistry, and biology. These qualitative cases reveal that our model, after reinforcement learning, demonstrates significantly enhanced reasoning capabilities. Specifically, MM-Eureka-32B is able to better apply known concepts and perform multi-step deduction to arrive at the correct answers. In contrast, the base model often shows surface-level understanding—it may recall relevant facts but fails to apply them coherently in the problem-solving context.\n\nFor instance, in the physics example (Figure 7), the question involves analyzing the instantaneous contact force between two objects placed on a vertical spring. While both models recognize key physical quantities such as mass, weight, and spring force, only MM-Eureka-32B correctly applies Newton’s second law to derive the acceleration of the system and compute the contact force. It identifies that the net external force due to the added mass leads to a downward acceleration, and accurately calculates the resulting contact force between object A and B as  $24N$ . In contrast, the base model Qwen2.5-VL-32B-Instruct incorrectly concludes that the contact force equals the full weightTable 4: Performance comparison across different disciplines in MMK12. Bold indicates the top performer with the open-source models, while underline indicates the second best performer within open-source models.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Model&lt;/th>\n&lt;th>Mathematics&lt;/th>\n&lt;th>Physics&lt;/th>\n&lt;th>Chemistry&lt;/th>\n&lt;th>Biology&lt;/th>\n&lt;th>Avg.&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td colspan=\"6\">&lt;b>Closed-Source Models&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Claude3.7-Sonnet&lt;/td>\n&lt;td>57.4&lt;/td>\n&lt;td>53.4&lt;/td>\n&lt;td>55.4&lt;/td>\n&lt;td>55.0&lt;/td>\n&lt;td>55.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GPT-4o&lt;/td>\n&lt;td>55.8&lt;/td>\n&lt;td>41.2&lt;/td>\n&lt;td>47.0&lt;/td>\n&lt;td>55.4&lt;/td>\n&lt;td>49.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>o1&lt;/td>\n&lt;td>81.6&lt;/td>\n&lt;td>68.8&lt;/td>\n&lt;td>71.4&lt;/td>\n&lt;td>74.0&lt;/td>\n&lt;td>73.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Gemini2-flash&lt;/td>\n&lt;td>76.8&lt;/td>\n&lt;td>53.6&lt;/td>\n&lt;td>64.6&lt;/td>\n&lt;td>66.0&lt;/td>\n&lt;td>65.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"6\">&lt;b>Open-Source General Models&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>InternVL2.5-VL-8B&lt;/td>\n&lt;td>46.8&lt;/td>\n&lt;td>35.0&lt;/td>\n&lt;td>50.0&lt;/td>\n&lt;td>50.8&lt;/td>\n&lt;td>45.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen-2.5-VL-7B&lt;/td>\n&lt;td>58.4&lt;/td>\n&lt;td>45.4&lt;/td>\n&lt;td>56.4&lt;/td>\n&lt;td>54.0&lt;/td>\n&lt;td>53.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>InternVL2.5-VL-38B&lt;/td>\n&lt;td>61.6&lt;/td>\n&lt;td>49.8&lt;/td>\n&lt;td>60.4&lt;/td>\n&lt;td>60.0&lt;/td>\n&lt;td>58.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen-2.5-VL-32B&lt;/td>\n&lt;td>71.6&lt;/td>\n&lt;td>59.4&lt;/td>\n&lt;td>69.6&lt;/td>\n&lt;td>66.6&lt;/td>\n&lt;td>66.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>InternVL2.5-VL-78B&lt;/td>\n&lt;td>59.8&lt;/td>\n&lt;td>53.2&lt;/td>\n&lt;td>68.0&lt;/td>\n&lt;td>65.2&lt;/td>\n&lt;td>61.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen-2.5-VL-72B&lt;/td>\n&lt;td>&lt;b>75.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>64.8&lt;/b>&lt;/td>\n&lt;td>69.6&lt;/td>\n&lt;td>72.0&lt;/td>\n&lt;td>70.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"6\">&lt;b>Open-Source Reasoning Models&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>InternVL2.5-8B-MPO&lt;/td>\n&lt;td>26.6&lt;/td>\n&lt;td>25.0&lt;/td>\n&lt;td>42.4&lt;/td>\n&lt;td>44.0&lt;/td>\n&lt;td>34.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>InternVL2.5-38B-MPO&lt;/td>\n&lt;td>41.4&lt;/td>\n&lt;td>42.8&lt;/td>\n&lt;td>55.8&lt;/td>\n&lt;td>53.2&lt;/td>\n&lt;td>48.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>QVQ-72B-Preview&lt;/td>\n&lt;td>61.4&lt;/td>\n&lt;td>57.4&lt;/td>\n&lt;td>62.6&lt;/td>\n&lt;td>64.4&lt;/td>\n&lt;td>61.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Adora&lt;/td>\n&lt;td>63.6&lt;/td>\n&lt;td>50.6&lt;/td>\n&lt;td>59.0&lt;/td>\n&lt;td>59.0&lt;/td>\n&lt;td>58.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>R1-Onevision&lt;/td>\n&lt;td>44.8&lt;/td>\n&lt;td>33.8&lt;/td>\n&lt;td>39.8&lt;/td>\n&lt;td>40.8&lt;/td>\n&lt;td>39.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>OpenVLThinker-7&lt;/td>\n&lt;td>63.0&lt;/td>\n&lt;td>53.8&lt;/td>\n&lt;td>60.6&lt;/td>\n&lt;td>65.0&lt;/td>\n&lt;td>60.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"6\">&lt;b>Ours&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MM-Eureka-7B&lt;/td>\n&lt;td>71.2&lt;/td>\n&lt;td>56.2&lt;/td>\n&lt;td>65.2&lt;/td>\n&lt;td>65.2&lt;/td>\n&lt;td>64.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MM-Eureka-32B&lt;/td>\n&lt;td>&lt;u>74.6&lt;/u>&lt;/td>\n&lt;td>&lt;u>62.0&lt;/u>&lt;/td>\n&lt;td>&lt;b>75.4&lt;/b>&lt;/td>\n&lt;td>&lt;b>76.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>72.2&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nof object B (i.e.,  $40N$ ), failing to consider the transient acceleration of the system and misapplying Newtonian mechanics.\n\nThese examples highlight MM-Eureka’s improved ability to perform reasoning and its potential to generalize reasoning patterns across disciplines. Further cases in mathematics, chemistry, and biology show similar trends, where our model more effectively breaks down problems into intermediate steps and synthesizes knowledge to reach accurate conclusions.\n\n## 6 DISCUSSION\n\n### 6.1 ARE KNOWLEDGE AND REASONING DECOUPLED?\n\nFigure 4 presents the distribution of correct answers across 8 responses from the Qwen-2.5-VL-32B and MM-Eureka-32B models on the Mathematics dataset. It is evident that, for problems that were initially answered correctly at least once, Eureka shows a significant improvement in accuracy. However, the number of problems that initially had zero correct answers remains nearly unchanged. We hypothesize that this improvement is due to Eureka’s improved reasoning capabilities, developed through RL training, allowing it to better leverage existing knowledge and thus improve the accuracy on partially understood problems. Nonetheless, relying solely on reasoning is insufficient to solve problems the model originally cannot answer, which is why the accuracy for problems with zero correct answers remains almost unchanged.\n\nFigure ?? shows the responses from Qwen-2.5-VL-32B and MM-Eureka-32B to the same question from Mathematics (the full version is provided in Appendix). From the responses, we observe that although Qwen possesses the necessary knowledge to answer the question, it still struggles to provide the correct answer. In contrast, Eureka is able to better reason with the available knowledge and derive the correct answer. Table 5 further illustrates that, despite Eureka’s training set beingFigure 4: Distribution of correct answers across 8 responses from Qwen-2.5-VL-32B and MM-Eureka-32B on *Mathematics*.\n\nfocused only on mathematics, it also demonstrates a notable improvement in answering questions from other domains such as physics, chemistry, and biology.\n\nOur experimental results to some extent support the view that knowledge and reasoning in LLMs/VLMs can be decoupled, and to some extent indicate that learning knowledge and learning reasoning can be conducted separately during the training process. Therefore, a key direction for future research is to explore how to generalize the reasoning capabilities, developed from data like mathematics—where logic is clear, responses are structured, and answers are verifiable—into broader, more general domains.\n\n## 6.2 RL GENERALIZES BETTER THAN SFT\n\nWe maintain consistent settings with our RL training to compare different post-training strategies including SFT and COT SFT. Using the ms-swift framework (Zhao et al., 2024), we conduct both SFT and COT SFT training for 10 epochs with identical data. As shown in Table 5, results demonstrate that RL exhibits superior generalization compared to SFT or COT SFT approaches, particularly with more significant improvements on OOD test sets such as Physics, Chemistry, and Biology. Furthermore, RL enhances the model’s reasoning capabilities more effectively—while SFT and COT SFT fail to substantially improve performance on mathematics and physics problems, RL training increases the model’s scores in mathematics and physics by 12.8 and 10.8 points respectively.\n\nTable 5: Performance comparison of different training methods on MMK12. In terms of both enhancing mathematical capabilities and generalizing to other disciplines, RL significantly outperforms SFT or COT SFT.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Model&lt;/th>\n&lt;th>Mathematics&lt;/th>\n&lt;th>Physics&lt;/th>\n&lt;th>Chemistry&lt;/th>\n&lt;th>Biology&lt;/th>\n&lt;th>Avg.&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Qwen-2.5-VL-7B&lt;/td>\n&lt;td>58.4&lt;/td>\n&lt;td>45.4&lt;/td>\n&lt;td>56.4&lt;/td>\n&lt;td>54.0&lt;/td>\n&lt;td>53.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>+ SFT&lt;/td>\n&lt;td>56.6&lt;/td>\n&lt;td>50.0&lt;/td>\n&lt;td>63.2&lt;/td>\n&lt;td>61.2&lt;/td>\n&lt;td>57.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>+ COT SFT&lt;/td>\n&lt;td>59.2&lt;/td>\n&lt;td>46.0&lt;/td>\n&lt;td>62.2&lt;/td>\n&lt;td>61.2&lt;/td>\n&lt;td>57.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>+ RL&lt;/td>\n&lt;td>&lt;b>71.2&lt;/b>&lt;/td>\n&lt;td>&lt;b>56.2&lt;/b>&lt;/td>\n&lt;td>&lt;b>65.2&lt;/b>&lt;/td>\n&lt;td>&lt;b>65.0&lt;/b>&lt;/td>\n&lt;td>&lt;b>64.5&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n## 6.3 TWO-STAGE TRAINING\n\nIn Section 4.5, we introduce a two-stage RL training strategy. Stage 1 employs K12 data to enhance general knowledge reasoning capabilities, while stage 2 utilizes Geo3k data to address specific performance gaps. Additionally, we omit the KL divergence in stage one to accelerate training and then incorporate it in stage two to maintain training stability.Figure 5: (a) MM-Eureka-32B tends to experience sudden training collapse during RL training, manifested as accuracy reward approaching zero. (b) During the second training phase, adding KL divergence leads to more stable training with steadily increasing accuracy rewards. (c) The stabilizing effect of KL divergence in the second phase may be attributed to the stabilization of the policy ratio, as ratio instability often leads to training collapse.\n\nAs shown in Figure 5 (a), continuous training without KL divergence often leads to sudden model collapse. We identify this phenomenon results from ratio instability (excessive updates in the new policy). As shown in Figures 5 (b) and (c), which present training metrics with and without the use of KL divergence in the second stage, a sharp fluctuation in the ratio is observed when the model begins to collapse. To mitigate this issue of ratio instability, we introduce a KL divergence term during the second stage of training, which helps to stabilize the learning dynamics.\n\nFurthermore, Table 6 demonstrates that after the first training stage, despite overall performance improvements, capabilities in certain specific domains actually decline, as evidenced by MathVista’s geometry problem solving(GPS) score dropping from 74.0 to 56.7. To address this, we implement second-stage training using Geo3k, which yields further improvements across multiple mathematical benchmarks.\n\nTable 6: Performance comparison across multimodal mathematical benchmarks of the two stage training strategy. The second phase of training enhances various capabilities of the model following the first phase, with particularly significant improvements in geometric reasoning abilities.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Model&lt;/th>\n&lt;th>Data Scale&lt;/th>\n&lt;th>MathVista&lt;/th>\n&lt;th>MathVista(GPS)&lt;/th>\n&lt;th>MathVerse&lt;/th>\n&lt;th>Mathvision&lt;/th>\n&lt;th>WeMath&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Stage1&lt;/td>\n&lt;td>15k&lt;/td>\n&lt;td>72.0&lt;/td>\n&lt;td>56.7&lt;/td>\n&lt;td>56.4&lt;/td>",
      "numLines": 400,
      "startLine": 300,
      "totalLines": 1106
    }
  },
  "sourceToolAssistantUUID": "1ccf7036-611a-4cd7-a408-a4e59e750013",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-27T16:04:38.942Z_

<details open><summary>🔧 Tool call — Read · `toolu_019cpJx88FCj4crvJKKzinDM`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/85dae6a1-bcc0-4c8f-97a6-84608d21f8c6/tool-results/toolu_01KEj67Agphd4njkFJNjphT6.txt",
  "offset": 695,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e2f5d07-d7be-49a4-948e-b5f1d0d59c93",
  "isSidechain": false,
  "requestId": "req_011CbTMhsnyX3jyZURhZYLmp",
  "type": "assistant",
  "uuid": "ce0c8521-5767-43ef-9b74-44e08121ce3c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R1P9Ek1L2pEFkRPQuNnFxs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6077,
      "cache_read_input_tokens": 28130,
      "output_tokens": 163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6077,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 163,
          "cache_read_input_tokens": 28130,
          "cache_creation_input_tokens": 6077,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6077
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

_source line 42 · 2026-05-27T16:04:39.217Z_

<details><summary>↩ Tool result · `toolu_019cpJx88FCj4crvJKKzinDM`</summary>

```text
695	&lt;td>Stage1&lt;/td>
696	&lt;td>15k&lt;/td>
697	&lt;td>72.0&lt;/td>
698	&lt;td>56.7&lt;/td>
699	&lt;td>56.4&lt;/td>
700	&lt;td>33.6&lt;/td>
701	&lt;td>&lt;b>73.5&lt;/b>&lt;/td>
702	&lt;/tr>
703	&lt;tr>
704	&lt;td>Stage2&lt;/td>
705	&lt;td>2k&lt;/td>
706	&lt;td>&lt;b>74.8&lt;/b>&lt;/td>
707	&lt;td>&lt;b>70.2&lt;/b>&lt;/td>
708	&lt;td>&lt;b>56.5&lt;/b>&lt;/td>
709	&lt;td>&lt;b>34.4&lt;/b>&lt;/td>
710	&lt;td>73.4&lt;/td>
711	&lt;/tr>
712	&lt;/tbody>
713	&lt;/table>
714	
715	## 7 CONCLUSION
716	
717	Our work aims at developing a powerful model for multimodal reasoning. To achieve this, we first propose MMK12, which is a high quality multimodal reasoning mathematical dataset collected by ourselves. Moreover, we utilize online filter and propose a two-stage training strategy to make the rule-based reinforcement learning training more stable and efficient. Finally, we propose MM-Eureka-7B and MM-Eureka-32B, both are the top performers within the similar size models in multimodal reasoning tasks. Especially for multidisciplinary reasoning tasks, MM-Eureka-32B surpasses almost all open-source models and closed-source models, which is only slightly behind o1.
718	
719	## 8 ACKNOWLEDGEMENTS
720	
721	We acknowledge the outstanding open-source contributions from vLLM, LMM-R1, and Open-RLHF. We also extend our gratitude to DeepSeek-R1, InternVL, and QwenVL for their open-source techniques and base models, which have enabled us to further our exploration.
722	
723	## REFERENCES
724	
725	Arash Ahmadian, Chris Cremer, Matthias Gallé, Marzieh Fadaee, Julia Kreutzer, Olivier Pietquin, Ahmet Üstün, and Sara Hooker. Back to basics: Revisiting reinforce-style optimization for learning from human feedback in llms. In *Proceedings of the 62nd Annual Meeting of the Association*for *Computational Linguistics (Volume 1: Long Papers)*, ACL 2024, pp. 12248–12267. Association for Computational Linguistics, 2024.
726	
727	Anthropic. Claude 3.7 sonnet. &lt;https://www.anthropic.com/claude>, 2024. Accessed: 2025-04-14.
728	
729	Jinze Bai, Shuai Bai, Shusheng Yang, Shijie Wang, Sinan Tan, Peng Wang, Junyang Lin, Chang Zhou, and Jingren Zhou. Qwen-vl: A versatile vision-language model for understanding, localization, text reading, and beyond, 2023. URL &lt;https://arxiv.org/abs/2308.12966>.
730	
731	Liang Chen, Lei Li, Haozhe Zhao, Yifan Song, and Vinci. R1-v: Reinforcing super generalization ability in vision-language models with less than \$3. &lt;https://github.com/Deep-Agent/R1-V>, 2025. Accessed: 2025-02-02.
732	
733	Zhe Chen, Weiyun Wang, Yue Cao, Yangzhou Liu, Zhangwei Gao, Erfei Cui, Jinguo Zhu, Shenglong Ye, Hao Tian, Zhaoyang Liu, et al. Expanding performance boundaries of open-source multimodal models with model, data, and test-time scaling. *arXiv preprint arXiv:2412.05271*, 2024.
734	
735	Ganqu Cui, Lifan Yuan, Zefan Wang, Hanbin Wang, Wendi Li, Bingxiang He, Yuchen Fan, Tianyu Yu, Qixin Xu, Weize Chen, Jiarui Yuan, Huayu Chen, Kaiyan Zhang, Xingtai Lv, Shuo Wang, Yuan Yao, Xu Han, Hao Peng, Yu Cheng, Zhiyuan Liu, Maosong Sun, Bowen Zhou, and Ning Ding. Process reinforcement through implicit rewards, 2025. URL &lt;https://arxiv.org/abs/2502.01456>.
736	
737	DeepSeek-AI, Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, Xiaokang Zhang, Xingkai Yu, Yu Wu, Z. F. Wu, Zhibin Gou, Zhihong Shao, Zhuoshu Li, Ziyi Gao, Aixin Liu, Bing Xue, Bingxuan Wang, Bochao Wu, Bei Feng, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chenyu Zhang, Chong Ruan, Damai Dai, Deli Chen, Dongjie Ji, Erhang Li, Fangyun Lin, Fucong Dai, Fuli Luo, Guangbo Hao, Guanting Chen, Guowei Li, H. Zhang, Han Bao, Hanwei Xu, Haocheng Wang, Honghui Ding, Huajian Xin, Huazuo Gao, Hui Qu, Hui Li, Jianzhong Guo, Jiashi Li, Jiawei Wang, Jingchang Chen, Jingyang Yuan, Junjie Qiu, Junlong Li, J. L. Cai, Jiaqi Ni, Jian Liang, Jin Chen, Kai Dong, Kai Hu, Kaige Gao, Kang Guan, Kexin Huang, Kuai Yu, Lean Wang, Lecong Zhang, Liang Zhao, Litong Wang, Liyue Zhang, Lei Xu, Leyi Xia, Mingchuan Zhang, Minghua Zhang, Minghui Tang, Meng Li, Miaojun Wang, Mingming Li, Ning Tian, Panpan Huang, Peng Zhang, Qiancheng Wang, Qinyu Chen, Qiushi Du, Ruiqi Ge, Ruisong Zhang, Ruizhe Pan, Runji Wang, R. J. Chen, R. L. Jin, Ruyi Chen, Shanghao Lu, Shangyan Zhou, Shanhuang Chen, Shengfeng Ye, Shiyu Wang, Shuiping Yu, Shunfeng Zhou, Shuting Pan, S. S. Li, Shuang Zhou, Shaoqing Wu, Shengfeng Ye, Tao Yun, Tian Pei, Tianyu Sun, T. Wang, Wangding Zeng, Wanjia Zhao, Wen Liu, Wenfeng Liang, Wenjun Gao, Wenqin Yu, Wentao Zhang, W. L. Xiao, Wei An, Xiaodong Liu, Xiaohan Wang, Xiaokang Chen, Xiaotao Nie, Xin Cheng, Xin Liu, Xin Xie, Xingchao Liu, Xinyu Yang, Xinyuan Li, Xuecheng Su, Xuheng Lin, X. Q. Li, Xiangyue Jin, Xiaojin Shen, Xiaosha Chen, Xiaowen Sun, Xiaoxiang Wang, Xinnan Song, Xinyi Zhou, Xianzu Wang, Xinxia Shan, Y. K. Li, Y. Q. Wang, Y. X. Wei, Yang Zhang, Yanhong Xu, Yao Li, Yao Zhao, Yaofeng Sun, Yaohui Wang, Yi Yu, Yichao Zhang, Yifan Shi, Yiliang Xiong, Ying He, Yishi Piao, Yisong Wang, Yixuan Tan, Yiyang Ma, Yiyuan Liu, Yongqiang Guo, Yuan Ou, Yuduan Wang, Yue Gong, Yuheng Zou, Yujia He, Yunfan Xiong, Yuxiang Luo, Yuxiang You, Yuxuan Liu, Yuyang Zhou, Y. X. Zhu, Yanhong Xu, Yanping Huang, Yaohui Li, Yi Zheng, Yuchen Zhu, Yunxian Ma, Ying Tang, Yukun Zha, Yuting Yan, Z. Z. Ren, Zehui Ren, Zhangli Sha, Zhe Fu, Zhean Xu, Zhenda Xie, Zhengyan Zhang, Zhewen Hao, Zhicheng Ma, Zhigang Yan, Zhiyu Wu, Zihui Gu, Zijia Zhu, Zijun Liu, Zilin Li, Ziwei Xie, Ziyang Song, Zizheng Pan, Zhen Huang, Zhipeng Xu, Zhongyu Zhang, and Zhen Zhang. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning, 2025. URL &lt;https://arxiv.org/abs/2501.12948>.
738	
739	Linger Deng, Yuliang Liu, Bohan Li, Dongliang Luo, Liang Wu, Chengquan Zhang, Pengyuan Lyu, Ziyang Zhang, Gang Zhang, Errui Ding, et al. R-cot: Reverse chain-of-thought problem generation for geometric reasoning in large multimodal models. *arXiv preprint arXiv:2410.17885*, 2024.Yihe Deng, Hritik Bansal, Fan Yin, Nanyun Peng, Wei Wang, and Kai-Wei Chang. Openvlthinker: An early exploration to complex vision-language reasoning via iterative self-improvement, 2025. URL &lt;https://arxiv.org/abs/2503.17352>.
740	
741	Haodong Duan, Junming Yang, Yuxuan Qiao, Xinyu Fang, Lin Chen, Yuan Liu, Xiaoyi Dong, Yuhang Zang, Pan Zhang, Jiaqi Wang, et al. Vlmevalkit: An open-source toolkit for evaluating large multi-modality models. In *Proceedings of the 32nd ACM international conference on multimedia*, pp. 11198–11201, 2024.
742	
743	Leo Gao, John Schulman, and Jacob Hilton. Scaling laws for reward model overoptimization, 2022. URL &lt;https://arxiv.org/abs/2210.10760>.
744	
745	Lujun Gui and Qingnan Ren. Training reasoning model with dynamic advantage estimation on reinforcement learning. [https://www.notion.so/Training\\_Reasoning\\_Model\\_with\\_Dynamic\\_Advantage\\_Estimation\\_on\\_Reinforcement\\_Learning\\_1a830cc0904681fa9df3e076b6557a3e](https://www.notion.so/Training_Reasoning_Model_with_Dynamic_Advantage_Estimation_on_Reinforcement_Learning_1a830cc0904681fa9df3e076b6557a3e), 2025. Notion Blog.
746	
747	Jarvis Guo, Tuney Zheng, Yuelin Bai, Bo Li, Yubo Wang, King Zhu, Yizhi Li, Graham Neubig, Wenhu Chen, and Xiang Yue. Mammoth-vl: Eliciting multimodal reasoning with instruction tuning at scale, 2024. URL &lt;https://arxiv.org/abs/2412.05237>.
748	
749	Chaoqun He, Renjie Luo, Yuzhuo Bai, Shengding Hu, Zhen Leng Thai, Junhao Shen, Jinyi Hu, Xu Han, Yujie Huang, Yuxiang Zhang, Jie Liu, Lei Qi, Zhiyuan Liu, and Maosong Sun. Olympiadbench: A challenging benchmark for promoting agi with olympiad-level bilingual multimodal scientific problems, 2024. URL &lt;https://arxiv.org/abs/2402.14008>.
750	
751	Jian Hu. Reinforce++: A simple and efficient approach for aligning large language models. *arXiv preprint arXiv:2501.03262*, 2025.
752	
753	Jian Hu, Xibin Wu, Zilin Zhu, Xianyu, Weixun Wang, Dehao Zhang, and Yu Cao. Openrlhf: An easy-to-use, scalable and high-performance rlhf framework, 2024. URL &lt;https://arxiv.org/abs/2405.11143>.
754	
755	Aaron Hurst, Adam Lerer, Adam P Goucher, Adam Perelman, Aditya Ramesh, Aidan Clark, AJ Ostrow, Akila Welihinda, Alan Hayes, Alec Radford, et al. Gpt-4o system card. *arXiv preprint arXiv:2410.21276*, 2024.
756	
757	Wouter Kool, Herke van Hoof, and Max Welling. Buy 4 REINFORCE samples, get a baseline for free! In *Deep Reinforcement Learning Meets Structured Prediction, ICLR 2019 Workshop*. OpenReview.net, 2019.
758	
759	Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E. Gonzalez, Hao Zhang, and Ion Stoica. Efficient memory management for large language model serving with pagedattention. In *Proceedings of the ACM SIGOPS 29th Symposium on Operating Systems Principles*, 2023.
760	
761	Pan Lu, Ran Gong, Shibiao Jiang, Liang Qiu, Siyuan Huang, Xiaodan Liang, and Song-Chun Zhu. Inter-gps: Interpretable geometry problem solving with formal language and symbolic reasoning. *arXiv preprint arXiv:2105.04165*, 2021.
762	
763	Pan Lu, Hritik Bansal, Tony Xia, Jiacheng Liu, Chunyuan Li, Hannaneh Hajishirzi, Hao Cheng, Kai-Wei Chang, Michel Galley, and Jianfeng Gao. Mathvista: Evaluating mathematical reasoning of foundation models in visual contexts, 2024. URL &lt;https://arxiv.org/abs/2310.02255>.
764	
765	OpenAI. Introducing openai o1. &lt;https://openai.com/o1/>, 2024. Accessed: 2024-10-02.
766	
767	Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser Kelton, Luke Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul Christiano, Jan Leike, and Ryan Lowe. Training language models to follow instructions with human feedback, 2022. URL &lt;https://arxiv.org/abs/2203.02155>.Shuai Peng, Di Fu, Liangcai Gao, Xiuqin Zhong, Hongguang Fu, and Zhi Tang. Multi-math: Bridging visual and mathematical reasoning for large language models. *arXiv preprint arXiv:2409.00147*, 2024.
768	
769	YingZhe Peng, Gongrui Zhang, Xin Geng, and Xu Yang. Lmm-r1. &lt;https://github.com/TideDra/lmm-r1>, 2025. Accessed: 2025-02-13.
770	
771	Runqi Qiao, Qiuna Tan, Guanting Dong, Minhui Wu, Chong Sun, Xiaoshuai Song, Zhuoma Gongque, Shanglin Lei, Zhe Wei, Miaoxuan Zhang, Runfeng Qiao, Yifan Zhang, Xiao Zong, Yida Xu, Muxi Diao, Zhimin Bao, Chen Li, and Honggang Zhang. We-math: Does your large multimodal model achieve human-like mathematical reasoning? *CoRR*, abs/2407.01284, 2024. doi: 10.48550/ARXIV.2407.01284. URL &lt;https://doi.org/10.48550/arXiv.2407.01284>.
772	
773	Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, Ilya Sutskever, et al. Language models are unsupervised multitask learners. *OpenAI blog*, 1(8):9, 2019.
774	
775	Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and Chelsea Finn. Direct preference optimization: Your language model is secretly a reward model. *Advances in Neural Information Processing Systems*, 36:53728–53741, 2023.
776	
777	John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms, 2017a. URL &lt;https://arxiv.org/abs/1707.06347>.
778	
779	John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. *arXiv preprint arXiv:1707.06347*, 2017b.
780	
781	Richard S Sutton, Andrew G Barto, et al. *Reinforcement learning: An introduction*, volume 1. MIT press Cambridge, 1998.
782	
783	Huajie Tan, Yuheng Ji, Xiaoshuai Hao, Minglan Lin, Pengwei Wang, Zhongyuan Wang, and Shanghang Zhang. Reason-rft: Reinforcement fine-tuning for visual reasoning, 2025. URL &lt;https://arxiv.org/abs/2503.20752>.
784	
785	Gemini Team, Rohan Anil, Sebastian Borgeaud, Jean-Baptiste Alayrac, Jiahui Yu, Radu Soricut, Johan Schalkwyk, Andrew M Dai, Anja Hauth, Katie Millican, et al. Gemini: a family of highly capable multimodal models. *arXiv preprint arXiv:2312.11805*, 2023.
786	
787	Kimi Team, Angang Du, Bofei Gao, Bowei Xing, Changjiu Jiang, Cheng Chen, Cheng Li, Chenjun Xiao, Chenzhuang Du, Chonghua Liao, Chuning Tang, Congcong Wang, Dehao Zhang, Enming Yuan, Enzhe Lu, Fengxiang Tang, Flood Sung, Guangda Wei, Guokun Lai, Haiqing Guo, Han Zhu, Hao Ding, Hao Hu, Hao Yang, Hao Zhang, Haotian Yao, Haotian Zhao, Haoyu Lu, Haoze Li, Haozhen Yu, Hongcheng Gao, Huabin Zheng, Huan Yuan, Jia Chen, Jianhang Guo, Jianlin Su, Jianzhou Wang, Jie Zhao, Jin Zhang, Jingyuan Liu, Junjie Yan, Junyan Wu, Lidong Shi, Ling Ye, Longhui Yu, Mengnan Dong, Neo Zhang, Ningchen Ma, Qiwei Pan, Qucheng Gong, Shaowei Liu, Shengling Ma, Shupeng Wei, Sihan Cao, Siying Huang, Tao Jiang, Weihao Gao, Weimin Xiong, Weiran He, Weixiao Huang, Wenhao Wu, Wenyang He, Xianghui Wei, Xianqing Jia, Xingzhe Wu, Xinran Xu, Xinxing Zu, Xinyu Zhou, Xuehai Pan, Y. Charles, Yang Li, Yangyang Hu, Yangyang Liu, Yanru Chen, Yejie Wang, Yibo Liu, Yidao Qin, Yifeng Liu, Ying Yang, Yiping Bao, Yulun Du, Yuxin Wu, Yuzhi Wang, Zaida Zhou, Zhaoji Wang, Zhaowei Li, Zhen Zhu, Zheng Zhang, Zhexu Wang, Zhilin Yang, Zhiqi Huang, Zihao Huang, Ziyao Xu, and Zonghan Yang. Kimi k1.5: Scaling reinforcement learning with llms, 2025a. URL &lt;https://arxiv.org/abs/2501.12599>.
788	
789	Kimi Team, Angang Du, Bohong Yin, Bowei Xing, Bowen Qu, Bowen Wang, Cheng Chen, Chenlin Zhang, Chenzhuang Du, Chu Wei, Congcong Wang, Dehao Zhang, Dikang Du, Dongliang Wang, Enming Yuan, Enzhe Lu, Fang Li, Flood Sung, Guangda Wei, Guokun Lai, Han Zhu, Hao Ding, Hao Hu, Hao Yang, Hao Zhang, Haoning Wu, Haotian Yao, Haoyu Lu, Heng Wang, Hongcheng Gao, Huabin Zheng, Jiaming Li, Jianlin Su, Jianzhou Wang, Jiaqi Deng, Jiezhong Qiu, Jin Xie, Jinhong Wang, Jingyuan Liu, Junjie Yan, Kun Ouyang, Liang Chen, Lin Sui, Longhui Yu, Mengfan Dong, Mengnan Dong, Nuo Xu, Pengyu Cheng, Qizheng Gu, Runjie Zhou, Shaowei Liu, Sihan Cao, Tao Yu, Tianhui Song, Tongtong Bai, Wei Song, Weiran He, Weixiao Huang, WeixinXu, Xiaokun Yuan, Xingcheng Yao, Xingzhe Wu, Xinxing Zu, Xinyu Zhou, Xinyuan Wang, Y. Charles, Yan Zhong, Yang Li, Yangyang Hu, Yanru Chen, Yejie Wang, Yibo Liu, Yibo Miao, Yidao Qin, Yimin Chen, Yiping Bao, Yiqin Wang, Yongsheng Kang, Yuanxin Liu, Yulun Du, Yuxin Wu, Yuzhi Wang, Yuzi Yan, Zaida Zhou, Zhaowei Li, Zhejun Jiang, Zheng Zhang, Zhilin Yang, Zhiqi Huang, Zihao Huang, Zijia Zhao, and Ziwei Chen. Kimi-VL technical report, 2025b. URL &lt;https://arxiv.org/abs/2504.07491>.
790	
791	Qwen Team. Qvq: To see the world with wisdom, December 2024. URL &lt;https://qwenlm.github.io/blog/qvq-72b-preview/>.
792	
793	Ke Wang, Junting Pan, Weikang Shi, Zimu Lu, Mingjie Zhan, and Hongsheng Li. Measuring multimodal mathematical reasoning with math-vision dataset, 2024a. URL &lt;https://arxiv.org/abs/2402.14804>.
794	
795	Weiyun Wang, Zhe Chen, Wenhai Wang, Yue Cao, Yangzhou Liu, Zhangwei Gao, Jinguo Zhu, Xizhou Zhu, Lewei Lu, Yu Qiao, and Jifeng Dai. Enhancing the reasoning ability of multimodal large language models via mixed preference optimization, 2024b. URL &lt;https://arxiv.org/abs/2411.10442>.
796	
797	Yi Yang, Xiaoxuan He, Hongkun Pan, Xiyuan Jiang, Yan Deng, Xingtao Yang, Haoyu Lu, Dacheng Yin, Fengyun Rao, Minfeng Zhu, Bo Zhang, and Wei Chen. R1-onevision: Advancing generalized multimodal reasoning through cross-modal formalization. *arXiv preprint arXiv:2503.10615*, 2025.
798	
799	Renrui Zhang, Dongzhi Jiang, Yichi Zhang, Haokun Lin, Ziyu Guo, Pengshuo Qiu, Aojun Zhou, Pan Lu, Kai-Wei Chang, Peng Gao, and Hongsheng Li. Mathverse: Does your multi-modal llm truly see the diagrams in visual math problems?, 2024a. URL &lt;https://arxiv.org/abs/2403.14624>.
800	
801	Renrui Zhang, Xinyu Wei, Dongzhi Jiang, Ziyu Guo, Shicheng Li, Yichi Zhang, Chengzhuo Tong, Jiaming Liu, Aojun Zhou, Bin Wei, et al. Mavis: Mathematical visual instruction tuning with an automatic data engine. *arXiv preprint arXiv:2407.08739*, 2024b.
802	
803	Yuze Zhao, Jintao Huang, Jinghan Hu, Xingjun Wang, Yunlin Mao, Daoze Zhang, Zeyinzi Jiang, Zhikai Wu, Baole Ai, Ang Wang, Wenmeng Zhou, and Yingda Chen. Swift: a scalable lightweight infrastructure for fine-tuning, 2024. URL &lt;https://arxiv.org/abs/2408.05517>.## A APPENDIX: QUALITATIVE ANALYSIS
804	
805	**Question:**
806	
807	As shown in the figure, in the straight square column  $ABCD - A_1B_1C_1D_1$ ,  $\angle ADC = 90^\circ$ , and  $AA_1 = AD = DC = 1$ ,  $M \in \text{plane } ABCD$ , when  $D_1M \perp \text{plane } A_1C_1D$ ,  $D_1M = \dots$
808	
809	**Answer:**  $\sqrt{3}$
810	
811	**Qwen2.5-VL-32B-Instruct**
812	
813	To solve the problem, we need to determine the length of  $D_1M$ , where  $M$  is a point in the plane  $ABCD$  such that  $D_1M \perp \text{plane } A_1C_1D$ .
814	
815	**2. Coordinates of Points:** Place the prism in a 3D Cartesian coordinate system:
816	
817	$$A = (0, 0, 0), \quad B = (1, 0, 0), \quad C = (1, 1, 0), \quad D = (0, 1, 0)$$
818	
819	$$A_1 = (0, 0, 1), \quad B_1 = (1, 0, 1), \quad C_1 = (1, 1, 1), \quad D_1 = (0, 1, 1)$$
820	
821	Let  $M = (x, y, 0)$ , where  $M$  is in the plane  $ABCD$ .
822	
823	**3. Vector Representation:**  $\vec{D_1M} = (x - 0, y - 1, 0 - 1) = (x, y - 1, -1)$
824	
825	**4. Condition for Perpendicularity:** For  $D_1M \perp \text{plane } A_1C_1D$ , the vector  $\vec{D_1M}$  must be perpendicular to the normal vector of the plane  $A_1C_1D$ .
826	
827	First, find two non-parallel vectors in the plane  $A_1C_1D$ :
828	
829	Therefore, the length of  $D_1M$  is  $\frac{\sqrt{6}}{2}$ .
830	
831	**MM-EUREKA-32B**
832	
833	To solve the problem, we need to determine the length of  $D_1M$  when  $D_1M \perp \text{plane } A_1C_1D$ . Let's break the problem into steps:
834	
835	**2. Determination of the plane  $A_1C_1D$ :**
836	
837	- The points  $A_1 = (1, 0, 1)$ ,  $C_1 = (0, 1, 1)$ , and  $D = (0, 0, 0)$  lie in the plane  $A_1C_1D$ .
838	- To find the normal vector to the plane  $A_1C_1D$ , we use the cross product of two vectors in the plane:
839	
840	$$\vec{A_1D} = (1 - 0, 0 - 0, 1 - 0) = (1, 0, 1), \quad \vec{C_1D} = (0 - 0, 1 - 0, 1 - 0) = (0, 1, 1).$$
841	
842	- The normal vector  $\mathbf{n}$  to the plane is given by the cross product:
843	
844	$$\mathbf{n} = \vec{A_1D} \times \vec{C_1D} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{vmatrix} = \mathbf{i}(0 \cdot 1 - 1 \cdot 1) - \mathbf{j}(1 \cdot 1 - 1 \cdot 0) + \mathbf{k}(1 \cdot 1 - 0 \cdot 0) = (-1, -1, 1).$$
845	
846	- Thus, the normal vector to the plane  $A_1C_1D$  is  $\mathbf{n} = (-1, -1, 1)$ .
847	
848	**3. Condition for  $D_1M \perp \text{plane } A_1C_1D$ :**
849	
850	- Since  $D_1M \perp \text{plane } A_1C_1D$ , the vector  $\vec{D_1M}$  must be parallel to the normal vector  $\mathbf{n} = (-1, -1, 1)$ .
851	- Let  $M = (x, y, 0)$  be a point in the plane  $ABCD$  (since  $M \in \text{plane } ABCD$ , the  $z$ -coordinate of  $M$  is 0).
852	- The vector  $\vec{D_1M} = (x - 0, y - 0, 0 - 1) = (x, y, -1)$ .
853	
854	**4. Calculation of  $D_1M$ :**
855	
856	- The vector  $\vec{D_1M} = (1 - 0, 1 - 0, 0 - 1) = (1, 1, -1)$ .
857	- The length of  $D_1M$  is given by the magnitude of  $\vec{D_1M}$ :  $|\vec{D_1M}| = \sqrt{1^2 + 1^2 + (-1)^2} = \sqrt{1 + 1 + 1} = \sqrt{3}$ .
858	
859	&lt;answer>The answer is  $\sqrt{3}$ . &lt;/answer>
860	
861	Figure 6: Example from mathematics. Red highlights Qwen2.5-VL-32B-Instruct's reasoning errors. Green shows MM-Eureka-32B's correct reasoning.**Question:**
862	
863	As shown in the figure, a lightweight spring is placed vertically on a horizontal surface with a mass of  $6\text{kg}$  object  $A$  resting on its upper end, in a stationary state. Now, a mass of  $4\text{kg}$  object  $B$  is gently placed on top of object  $A$ , and the spring remains within its elastic limit. Taking  $g$  as  $10\text{m/s}^2$ , at the moment  $B$  is placed, the magnitude of the force between  $A$  and  $B$  is ( )
864	
865	A.  $8\text{N}$  B.  $18\text{N}$  C.  $24\text{N}$  D.  $40\text{N}$
866	
867	**Answer:** C
868	
869	**Qwen2.5-VL-32B-Instruct**
870	
871	To solve this problem, we need to determine the force between objects  $A$  and  $B$  at the moment  $B$  is placed on top of  $A$ . Let's break it down step by step.
872	
873	...  
874	**4. Force Analysis at the Moment  $B$  is Placed:**
875	
876	- At the moment  $B$  is placed, the spring has not yet had time to extend further to balance the new total weight. The spring force remains  $60\text{N}$  (the initial force that balances the weight of  $A$ ).
877	- **The net force on  $A$  is the sum of the spring force and the force from  $B$ :  $F_s + F_B = m_A g$ .**
878	- Here,  $F_s = 60\text{N}$  and  $m_A g = 60\text{N}$ , so:  $60\text{N} + F_B = 60\text{N}$ .
879	- Solving for  $F_B$ , we get:  $F_B = 0\text{N}$ .
880	
881	**5. Re-evaluate the Situation:**
882	
883	- The above analysis is not correct because we need to consider the instantaneous force between  $A$  and  $B$  due to the sudden addition of  $B$ .
884	- **The force between  $A$  and  $B$  is the force  $B$  exerts on  $A$ , which is the weight of  $B$ :  $F_B = m_B g = 4\text{kg} \cdot 10\text{m/s}^2 = 40\text{N}$ .**
885	
886	40
887	
888	**MM-EUREKA-32B**
889	
890	To solve this problem, we need to determine the force between objects  $A$  and  $B$  at the moment  $B$  is placed on top of  $A$ . Let's break the problem into steps:
891	
892	...  
893	**4. Applying Newton's Second Law to  $A$**
894	
895	$$\begin{aligned} F_{\text{net}} &= F_B + F_A - F_{\text{spring}} \\ &= F_B + 60 - 60 = F_B. \end{aligned}$$
896	
897	The net force on  $A$  causes an upward acceleration  $a$ , which is the same as the acceleration of  $B$  because they are in contact.
898	
899	**5. Analyzing the Forces on  $B$**
900	
901	- The forces on  $B$  are:
902	  - The weight of  $B$ :  $F_B = 40\text{N}$  (downward),
903	  - The force from  $A$ :  $F_{\text{contact}}$  (upward).
904	
905	**6. Applying Newton's Second Law to  $B$**
906	
907	$$F_B - F_{\text{contact}} = m_B a.$$
908	
909	**7. Finding the Acceleration  $a$**
910	
911	- The total mass of the system is  $m_{\text{total}} = m_A + m_B = 6 + 4 = 10\text{kg}$ .
912	- The net force on the system is the extra weight from  $B$ :  $F_{\text{net, total}} = 40\text{N}$ .
913	- Using Newton's Second Law for the entire system:  $F_{\text{net, total}} = m_{\text{total}} a \Rightarrow 40 = 10a \Rightarrow a = 4\text{m/s}^2$ .
914	
915	**8. Finding the Contact Force  $F_{\text{contact}}$**
916	
917	$$\begin{aligned} F_B - F_{\text{contact}} &= m_B a \\ 40 - F_{\text{contact}} &= 4 \cdot 4 = 16 \\ F_{\text{contact}} &= 40 - 16 = 24\text{N}. \end{aligned}$$
918	
919	&lt;answer>The answer is C. &lt;/answer>
920	
921	Figure 7: Example from physics. Red highlights Qwen2.5-VL-32B-Instruct's reasoning errors. Green shows MM-Eureka-32B's correct reasoning.**Question:**
922	
923	At room temperature, a 0.100 mol/L NaOH solution is used to titrate 25.00 mL 0.100 mol/L  $\text{H}_2\text{C}_2\text{O}_4$  solution, and the resulting titration curve is shown in the figure (the volume of the mixed solution can be considered as the sum of the volumes of the solutions before mixing). Which of the following statements is incorrect? ( )
924	
925	**A.** In the solution at point X:  $c(\text{Na}^+) > c(\text{HC}_2\text{O}_4^-) > c(\text{C}_2\text{O}_4^{2-})$   
926	**B.** Observing the solution at point Y indicates that the degree of ionization of  $\text{HC}_2\text{O}_4^-$  is greater than the degree of hydrolysis of  $\text{C}_2\text{O}_4^{2-}$   
927	**C.** In the solution at point Z:  $c(\text{Na}^+) > c(\text{C}_2\text{O}_4^{2-}) > c(\text{HC}_2\text{O}_4^-) > c(\text{OH}^-) > c(\text{H}^+)$   
928	**D.** Throughout the titration process:  $c(\text{Na}^+) + c(\text{H}_2\text{C}_2\text{O}_4) + c(\text{HC}_2\text{O}_4^-) + c(\text{C}_2\text{O}_4^{2-}) = 0.100\text{mol/L}$
929	
930	**Answer:** C
931	
932	**Qwen2.5-VL-32B-Instruct**
933	
934	**1. Understanding the Reaction:**
935	
936	- The titration is between a strong base (0.100 M NaO) and a weak dicarboxylic acid (0.100 M  $\text{H}_2\text{CO}_4$ ).
937	- The reaction steps are:
938	
939	1. $\text{H}_2\text{CO}_4 + \text{NaO} \rightarrow \text{NaHC}_2\text{O}_4 + \text{H}_2\text{O}$
940	2. $\text{NaHC}_2\text{O}_4 + \text{NaO} \rightarrow \text{Na}_2\text{CO}_4 + \text{H}_2\text{O}$
941	
942	**2. Key Points on the pH Curve:**
943	
944	- **Point X (pH  $\approx 2$ ):** This is the initial point where only  $\text{H}_2\text{CO}_4$  is present. The solution is acidic.
945	- **Point Y (pH  $\approx 5.5$ ):** This is the first equivalence point where all  $\text{H}_2\text{CO}_4$  has been neutralized to  $\text{NaHC}_2\text{O}_4$  (solutions of  $\text{NaHC}_2\text{O}_4$  are acidic due to the protonation of the conjugate base).
946	- **Point Z (pH  $\approx 8.7$ ):** This is the second equivalence point where all  $\text{NaHC}_2\text{O}_4$  has been neutralized to  $\text{Na}_2\text{CO}_4$  (solutions of  $\text{Na}_2\text{CO}_4$  are basic due to the deprotonation of the conjugate base).
947	
948	**4. Final Answer:** The only option that is **incorrect** is Option A.
949	
950	**MM-EUREKA-32B**
951	
952	To solve this problem, we need to analyze the titration of a weak dicarboxylic acid  $\text{H}_2\text{C}_2\text{O}_4$  (oxalate) with a strong base NaOH. The titration process involves multiple steps, and we must consider the equilibrium and ionic concentrations at different points on the titration curve. Let's break the problem into parts and solve it step by step.
953	
954	**1. Understanding the titration process:**
955	
956	$\text{H}_2\text{C}_2\text{O}_4$  is a weak dicarboxylic acid, which undergoes two steps of dissociation:
957	
958	$$\begin{aligned}\text{H}_2\text{C}_2\text{O}_4 &\rightleftharpoons \text{H}^+ + \text{HC}_2\text{O}_4^- \\ \text{HC}_2\text{O}_4^- &\rightleftharpoons \text{H}^+ + \text{C}_2\text{O}_4^{2-}\end{aligned}$$
959	
960	The titration is carried out with NaOH, a strong base, which will neutralize the  $\text{H}^+$  ions step by step.
961	
962	**2. Key points on the titration curve:**
963	
964	**Point X:** 25 mL of NaOH added.
965	
966	- At this point, the first equivalence point is reached. All  $\text{H}_2\text{C}_2\text{O}_4$  is converted to  $\text{NaHC}_2\text{O}_4$  (sodium hydrogen oxalate).
967	- The solution contains  $\text{NaHC}_2\text{O}_4$ , and the pH is around 2, indicating that  $\text{HC}_2\text{O}_4^-$  is a weak acid.
968	
969	**Point Y:** 40 mL of NaOH added.
970	
971	- This is between the first and second equivalence points. The solution contains a mixture of  $\text{NaHC}_2\text{O}_4$  and  $\text{Na}_2\text{C}_2\text{O}_4$ .
972	- The pH is 5.5, indicating that the solution is slightly acidic due to the dissociation of  $\text{HC}_2\text{O}_4^-$  being greater than the hydrolysis of  $\text{C}_2\text{O}_4^{2-}$ .
973	
974	**Point Z:** 50 mL of NaOH added.
975	
976	- At this point, the second equivalence point is reached. All  $\text{H}_2\text{C}_2\text{O}_4$  is converted to  $\text{Na}_2\text{C}_2\text{O}_4$  (sodium oxalate).
977	- The solution contains  $\text{Na}_2\text{C}_2\text{O}_4$ , and the pH is 8.7, indicating that  $\text{C}_2\text{O}_4^{2-}$  is a strong base.
978	
979	**&lt;answer>**The answer is C. **&lt;/answer>**
980	
981	Figure 8: Example from chemistry. Red highlights Qwen2.5-VL-32B-Instruct's reasoning errors. Green shows MM-Eureka-32B's correct reasoning.**Question:**
982	
983	Scientists isolated gene A from a certain organism and dissociated it into two single strands. One of these strands was hybridized with the messenger RNA of gene A, resulting in the pattern shown in the image. An unreasonable explanation for this is ( )
984	
985	- A. Positions 1, 3, 5, and 7 are connected through complementary base pairing
986	- B. Heating to a certain temperature can separate the two strands
987	- C. The diagram contains 8 types of nucleotides, 5 types of bases, and 2 types of base pairs
988	- D. Since fragments 2, 2, and 6 cannot bind with the messenger RNA, fragments 2, 4, and 6 belong to non-gene segments of the DNA molecule
989	
990	**Answer:** D
991	
992	**Qwen2.5-VL-32B-Instruct**
993	
994	...  
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce0c8521-5767-43ef-9b74-44e08121ce3c",
  "isSidechain": false,
  "promptId": "6e9b4775-3324-430a-aeff-baabf4898966",
  "type": "user",
  "uuid": "7f1c20b7-dc3b-4deb-92a4-aa07298c9ac4",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/85dae6a1-bcc0-4c8f-97a6-84608d21f8c6/tool-results/toolu_01KEj67Agphd4njkFJNjphT6.txt",
      "content": "&lt;td>Stage1&lt;/td>\n&lt;td>15k&lt;/td>\n&lt;td>72.0&lt;/td>\n&lt;td>56.7&lt;/td>\n&lt;td>56.4&lt;/td>\n&lt;td>33.6&lt;/td>\n&lt;td>&lt;b>73.5&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Stage2&lt;/td>\n&lt;td>2k&lt;/td>\n&lt;td>&lt;b>74.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>70.2&lt;/b>&lt;/td>\n&lt;td>&lt;b>56.5&lt;/b>&lt;/td>\n&lt;td>&lt;b>34.4&lt;/b>&lt;/td>\n&lt;td>73.4&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n## 7 CONCLUSION\n\nOur work aims at developing a powerful model for multimodal reasoning. To achieve this, we first propose MMK12, which is a high quality multimodal reasoning mathematical dataset collected by ourselves. Moreover, we utilize online filter and propose a two-stage training strategy to make the rule-based reinforcement learning training more stable and efficient. Finally, we propose MM-Eureka-7B and MM-Eureka-32B, both are the top performers within the similar size models in multimodal reasoning tasks. Especially for multidisciplinary reasoning tasks, MM-Eureka-32B surpasses almost all open-source models and closed-source models, which is only slightly behind o1.\n\n## 8 ACKNOWLEDGEMENTS\n\nWe acknowledge the outstanding open-source contributions from vLLM, LMM-R1, and Open-RLHF. We also extend our gratitude to DeepSeek-R1, InternVL, and QwenVL for their open-source techniques and base models, which have enabled us to further our exploration.\n\n## REFERENCES\n\nArash Ahmadian, Chris Cremer, Matthias Gallé, Marzieh Fadaee, Julia Kreutzer, Olivier Pietquin, Ahmet Üstün, and Sara Hooker. Back to basics: Revisiting reinforce-style optimization for learning from human feedback in llms. In *Proceedings of the 62nd Annual Meeting of the Association*for *Computational Linguistics (Volume 1: Long Papers)*, ACL 2024, pp. 12248–12267. Association for Computational Linguistics, 2024.\n\nAnthropic. Claude 3.7 sonnet. &lt;https://www.anthropic.com/claude>, 2024. Accessed: 2025-04-14.\n\nJinze Bai, Shuai Bai, Shusheng Yang, Shijie Wang, Sinan Tan, Peng Wang, Junyang Lin, Chang Zhou, and Jingren Zhou. Qwen-vl: A versatile vision-language model for understanding, localization, text reading, and beyond, 2023. URL &lt;https://arxiv.org/abs/2308.12966>.\n\nLiang Chen, Lei Li, Haozhe Zhao, Yifan Song, and Vinci. R1-v: Reinforcing super generalization ability in vision-language models with less than \\$3. &lt;https://github.com/Deep-Agent/R1-V>, 2025. Accessed: 2025-02-02.\n\nZhe Chen, Weiyun Wang, Yue Cao, Yangzhou Liu, Zhangwei Gao, Erfei Cui, Jinguo Zhu, Shenglong Ye, Hao Tian, Zhaoyang Liu, et al. Expanding performance boundaries of open-source multimodal models with model, data, and test-time scaling. *arXiv preprint arXiv:2412.05271*, 2024.\n\nGanqu Cui, Lifan Yuan, Zefan Wang, Hanbin Wang, Wendi Li, Bingxiang He, Yuchen Fan, Tianyu Yu, Qixin Xu, Weize Chen, Jiarui Yuan, Huayu Chen, Kaiyan Zhang, Xingtai Lv, Shuo Wang, Yuan Yao, Xu Han, Hao Peng, Yu Cheng, Zhiyuan Liu, Maosong Sun, Bowen Zhou, and Ning Ding. Process reinforcement through implicit rewards, 2025. URL &lt;https://arxiv.org/abs/2502.01456>.\n\nDeepSeek-AI, Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, Xiaokang Zhang, Xingkai Yu, Yu Wu, Z. F. Wu, Zhibin Gou, Zhihong Shao, Zhuoshu Li, Ziyi Gao, Aixin Liu, Bing Xue, Bingxuan Wang, Bochao Wu, Bei Feng, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chenyu Zhang, Chong Ruan, Damai Dai, Deli Chen, Dongjie Ji, Erhang Li, Fangyun Lin, Fucong Dai, Fuli Luo, Guangbo Hao, Guanting Chen, Guowei Li, H. Zhang, Han Bao, Hanwei Xu, Haocheng Wang, Honghui Ding, Huajian Xin, Huazuo Gao, Hui Qu, Hui Li, Jianzhong Guo, Jiashi Li, Jiawei Wang, Jingchang Chen, Jingyang Yuan, Junjie Qiu, Junlong Li, J. L. Cai, Jiaqi Ni, Jian Liang, Jin Chen, Kai Dong, Kai Hu, Kaige Gao, Kang Guan, Kexin Huang, Kuai Yu, Lean Wang, Lecong Zhang, Liang Zhao, Litong Wang, Liyue Zhang, Lei Xu, Leyi Xia, Mingchuan Zhang, Minghua Zhang, Minghui Tang, Meng Li, Miaojun Wang, Mingming Li, Ning Tian, Panpan Huang, Peng Zhang, Qiancheng Wang, Qinyu Chen, Qiushi Du, Ruiqi Ge, Ruisong Zhang, Ruizhe Pan, Runji Wang, R. J. Chen, R. L. Jin, Ruyi Chen, Shanghao Lu, Shangyan Zhou, Shanhuang Chen, Shengfeng Ye, Shiyu Wang, Shuiping Yu, Shunfeng Zhou, Shuting Pan, S. S. Li, Shuang Zhou, Shaoqing Wu, Shengfeng Ye, Tao Yun, Tian Pei, Tianyu Sun, T. Wang, Wangding Zeng, Wanjia Zhao, Wen Liu, Wenfeng Liang, Wenjun Gao, Wenqin Yu, Wentao Zhang, W. L. Xiao, Wei An, Xiaodong Liu, Xiaohan Wang, Xiaokang Chen, Xiaotao Nie, Xin Cheng, Xin Liu, Xin Xie, Xingchao Liu, Xinyu Yang, Xinyuan Li, Xuecheng Su, Xuheng Lin, X. Q. Li, Xiangyue Jin, Xiaojin Shen, Xiaosha Chen, Xiaowen Sun, Xiaoxiang Wang, Xinnan Song, Xinyi Zhou, Xianzu Wang, Xinxia Shan, Y. K. Li, Y. Q. Wang, Y. X. Wei, Yang Zhang, Yanhong Xu, Yao Li, Yao Zhao, Yaofeng Sun, Yaohui Wang, Yi Yu, Yichao Zhang, Yifan Shi, Yiliang Xiong, Ying He, Yishi Piao, Yisong Wang, Yixuan Tan, Yiyang Ma, Yiyuan Liu, Yongqiang Guo, Yuan Ou, Yuduan Wang, Yue Gong, Yuheng Zou, Yujia He, Yunfan Xiong, Yuxiang Luo, Yuxiang You, Yuxuan Liu, Yuyang Zhou, Y. X. Zhu, Yanhong Xu, Yanping Huang, Yaohui Li, Yi Zheng, Yuchen Zhu, Yunxian Ma, Ying Tang, Yukun Zha, Yuting Yan, Z. Z. Ren, Zehui Ren, Zhangli Sha, Zhe Fu, Zhean Xu, Zhenda Xie, Zhengyan Zhang, Zhewen Hao, Zhicheng Ma, Zhigang Yan, Zhiyu Wu, Zihui Gu, Zijia Zhu, Zijun Liu, Zilin Li, Ziwei Xie, Ziyang Song, Zizheng Pan, Zhen Huang, Zhipeng Xu, Zhongyu Zhang, and Zhen Zhang. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning, 2025. URL &lt;https://arxiv.org/abs/2501.12948>.\n\nLinger Deng, Yuliang Liu, Bohan Li, Dongliang Luo, Liang Wu, Chengquan Zhang, Pengyuan Lyu, Ziyang Zhang, Gang Zhang, Errui Ding, et al. R-cot: Reverse chain-of-thought problem generation for geometric reasoning in large multimodal models. *arXiv preprint arXiv:2410.17885*, 2024.Yihe Deng, Hritik Bansal, Fan Yin, Nanyun Peng, Wei Wang, and Kai-Wei Chang. Openvlthinker: An early exploration to complex vision-language reasoning via iterative self-improvement, 2025. URL &lt;https://arxiv.org/abs/2503.17352>.\n\nHaodong Duan, Junming Yang, Yuxuan Qiao, Xinyu Fang, Lin Chen, Yuan Liu, Xiaoyi Dong, Yuhang Zang, Pan Zhang, Jiaqi Wang, et al. Vlmevalkit: An open-source toolkit for evaluating large multi-modality models. In *Proceedings of the 32nd ACM international conference on multimedia*, pp. 11198–11201, 2024.\n\nLeo Gao, John Schulman, and Jacob Hilton. Scaling laws for reward model overoptimization, 2022. URL &lt;https://arxiv.org/abs/2210.10760>.\n\nLujun Gui and Qingnan Ren. Training reasoning model with dynamic advantage estimation on reinforcement learning. [https://www.notion.so/Training\\\\_Reasoning\\\\_Model\\\\_with\\\\_Dynamic\\\\_Advantage\\\\_Estimation\\\\_on\\\\_Reinforcement\\\\_Learning\\\\_1a830cc0904681fa9df3e076b6557a3e](https://www.notion.so/Training_Reasoning_Model_with_Dynamic_Advantage_Estimation_on_Reinforcement_Learning_1a830cc0904681fa9df3e076b6557a3e), 2025. Notion Blog.\n\nJarvis Guo, Tuney Zheng, Yuelin Bai, Bo Li, Yubo Wang, King Zhu, Yizhi Li, Graham Neubig, Wenhu Chen, and Xiang Yue. Mammoth-vl: Eliciting multimodal reasoning with instruction tuning at scale, 2024. URL &lt;https://arxiv.org/abs/2412.05237>.\n\nChaoqun He, Renjie Luo, Yuzhuo Bai, Shengding Hu, Zhen Leng Thai, Junhao Shen, Jinyi Hu, Xu Han, Yujie Huang, Yuxiang Zhang, Jie Liu, Lei Qi, Zhiyuan Liu, and Maosong Sun. Olympiadbench: A challenging benchmark for promoting agi with olympiad-level bilingual multimodal scientific problems, 2024. URL &lt;https://arxiv.org/abs/2402.14008>.\n\nJian Hu. Reinforce++: A simple and efficient approach for aligning large language models. *arXiv preprint arXiv:2501.03262*, 2025.\n\nJian Hu, Xibin Wu, Zilin Zhu, Xianyu, Weixun Wang, Dehao Zhang, and Yu Cao. Openrlhf: An easy-to-use, scalable and high-performance rlhf framework, 2024. URL &lt;https://arxiv.org/abs/2405.11143>.\n\nAaron Hurst, Adam Lerer, Adam P Goucher, Adam Perelman, Aditya Ramesh, Aidan Clark, AJ Ostrow, Akila Welihinda, Alan Hayes, Alec Radford, et al. Gpt-4o system card. *arXiv preprint arXiv:2410.21276*, 2024.\n\nWouter Kool, Herke van Hoof, and Max Welling. Buy 4 REINFORCE samples, get a baseline for free! In *Deep Reinforcement Learning Meets Structured Prediction, ICLR 2019 Workshop*. OpenReview.net, 2019.\n\nWoosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E. Gonzalez, Hao Zhang, and Ion Stoica. Efficient memory management for large language model serving with pagedattention. In *Proceedings of the ACM SIGOPS 29th Symposium on Operating Systems Principles*, 2023.\n\nPan Lu, Ran Gong, Shibiao Jiang, Liang Qiu, Siyuan Huang, Xiaodan Liang, and Song-Chun Zhu. Inter-gps: Interpretable geometry problem solving with formal language and symbolic reasoning. *arXiv preprint arXiv:2105.04165*, 2021.\n\nPan Lu, Hritik Bansal, Tony Xia, Jiacheng Liu, Chunyuan Li, Hannaneh Hajishirzi, Hao Cheng, Kai-Wei Chang, Michel Galley, and Jianfeng Gao. Mathvista: Evaluating mathematical reasoning of foundation models in visual contexts, 2024. URL &lt;https://arxiv.org/abs/2310.02255>.\n\nOpenAI. Introducing openai o1. &lt;https://openai.com/o1/>, 2024. Accessed: 2024-10-02.\n\nLong Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser Kelton, Luke Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul Christiano, Jan Leike, and Ryan Lowe. Training language models to follow instructions with human feedback, 2022. URL &lt;https://arxiv.org/abs/2203.02155>.Shuai Peng, Di Fu, Liangcai Gao, Xiuqin Zhong, Hongguang Fu, and Zhi Tang. Multi-math: Bridging visual and mathematical reasoning for large language models. *arXiv preprint arXiv:2409.00147*, 2024.\n\nYingZhe Peng, Gongrui Zhang, Xin Geng, and Xu Yang. Lmm-r1. &lt;https://github.com/TideDra/lmm-r1>, 2025. Accessed: 2025-02-13.\n\nRunqi Qiao, Qiuna Tan, Guanting Dong, Minhui Wu, Chong Sun, Xiaoshuai Song, Zhuoma Gongque, Shanglin Lei, Zhe Wei, Miaoxuan Zhang, Runfeng Qiao, Yifan Zhang, Xiao Zong, Yida Xu, Muxi Diao, Zhimin Bao, Chen Li, and Honggang Zhang. We-math: Does your large multimodal model achieve human-like mathematical reasoning? *CoRR*, abs/2407.01284, 2024. doi: 10.48550/ARXIV.2407.01284. URL &lt;https://doi.org/10.48550/arXiv.2407.01284>.\n\nAlec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, Ilya Sutskever, et al. Language models are unsupervised multitask learners. *OpenAI blog*, 1(8):9, 2019.\n\nRafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and Chelsea Finn. Direct preference optimization: Your language model is secretly a reward model. *Advances in Neural Information Processing Systems*, 36:53728–53741, 2023.\n\nJohn Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms, 2017a. URL &lt;https://arxiv.org/abs/1707.06347>.\n\nJohn Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. *arXiv preprint arXiv:1707.06347*, 2017b.\n\nRichard S Sutton, Andrew G Barto, et al. *Reinforcement learning: An introduction*, volume 1. MIT press Cambridge, 1998.\n\nHuajie Tan, Yuheng Ji, Xiaoshuai Hao, Minglan Lin, Pengwei Wang, Zhongyuan Wang, and Shanghang Zhang. Reason-rft: Reinforcement fine-tuning for visual reasoning, 2025. URL &lt;https://arxiv.org/abs/2503.20752>.\n\nGemini Team, Rohan Anil, Sebastian Borgeaud, Jean-Baptiste Alayrac, Jiahui Yu, Radu Soricut, Johan Schalkwyk, Andrew M Dai, Anja Hauth, Katie Millican, et al. Gemini: a family of highly capable multimodal models. *arXiv preprint arXiv:2312.11805*, 2023.\n\nKimi Team, Angang Du, Bofei Gao, Bowei Xing, Changjiu Jiang, Cheng Chen, Cheng Li, Chenjun Xiao, Chenzhuang Du, Chonghua Liao, Chuning Tang, Congcong Wang, Dehao Zhang, Enming Yuan, Enzhe Lu, Fengxiang Tang, Flood Sung, Guangda Wei, Guokun Lai, Haiqing Guo, Han Zhu, Hao Ding, Hao Hu, Hao Yang, Hao Zhang, Haotian Yao, Haotian Zhao, Haoyu Lu, Haoze Li, Haozhen Yu, Hongcheng Gao, Huabin Zheng, Huan Yuan, Jia Chen, Jianhang Guo, Jianlin Su, Jianzhou Wang, Jie Zhao, Jin Zhang, Jingyuan Liu, Junjie Yan, Junyan Wu, Lidong Shi, Ling Ye, Longhui Yu, Mengnan Dong, Neo Zhang, Ningchen Ma, Qiwei Pan, Qucheng Gong, Shaowei Liu, Shengling Ma, Shupeng Wei, Sihan Cao, Siying Huang, Tao Jiang, Weihao Gao, Weimin Xiong, Weiran He, Weixiao Huang, Wenhao Wu, Wenyang He, Xianghui Wei, Xianqing Jia, Xingzhe Wu, Xinran Xu, Xinxing Zu, Xinyu Zhou, Xuehai Pan, Y. Charles, Yang Li, Yangyang Hu, Yangyang Liu, Yanru Chen, Yejie Wang, Yibo Liu, Yidao Qin, Yifeng Liu, Ying Yang, Yiping Bao, Yulun Du, Yuxin Wu, Yuzhi Wang, Zaida Zhou, Zhaoji Wang, Zhaowei Li, Zhen Zhu, Zheng Zhang, Zhexu Wang, Zhilin Yang, Zhiqi Huang, Zihao Huang, Ziyao Xu, and Zonghan Yang. Kimi k1.5: Scaling reinforcement learning with llms, 2025a. URL &lt;https://arxiv.org/abs/2501.12599>.\n\nKimi Team, Angang Du, Bohong Yin, Bowei Xing, Bowen Qu, Bowen Wang, Cheng Chen, Chenlin Zhang, Chenzhuang Du, Chu Wei, Congcong Wang, Dehao Zhang, Dikang Du, Dongliang Wang, Enming Yuan, Enzhe Lu, Fang Li, Flood Sung, Guangda Wei, Guokun Lai, Han Zhu, Hao Ding, Hao Hu, Hao Yang, Hao Zhang, Haoning Wu, Haotian Yao, Haoyu Lu, Heng Wang, Hongcheng Gao, Huabin Zheng, Jiaming Li, Jianlin Su, Jianzhou Wang, Jiaqi Deng, Jiezhong Qiu, Jin Xie, Jinhong Wang, Jingyuan Liu, Junjie Yan, Kun Ouyang, Liang Chen, Lin Sui, Longhui Yu, Mengfan Dong, Mengnan Dong, Nuo Xu, Pengyu Cheng, Qizheng Gu, Runjie Zhou, Shaowei Liu, Sihan Cao, Tao Yu, Tianhui Song, Tongtong Bai, Wei Song, Weiran He, Weixiao Huang, WeixinXu, Xiaokun Yuan, Xingcheng Yao, Xingzhe Wu, Xinxing Zu, Xinyu Zhou, Xinyuan Wang, Y. Charles, Yan Zhong, Yang Li, Yangyang Hu, Yanru Chen, Yejie Wang, Yibo Liu, Yibo Miao, Yidao Qin, Yimin Chen, Yiping Bao, Yiqin Wang, Yongsheng Kang, Yuanxin Liu, Yulun Du, Yuxin Wu, Yuzhi Wang, Yuzi Yan, Zaida Zhou, Zhaowei Li, Zhejun Jiang, Zheng Zhang, Zhilin Yang, Zhiqi Huang, Zihao Huang, Zijia Zhao, and Ziwei Chen. Kimi-VL technical report, 2025b. URL &lt;https://arxiv.org/abs/2504.07491>.\n\nQwen Team. Qvq: To see the world with wisdom, December 2024. URL &lt;https://qwenlm.github.io/blog/qvq-72b-preview/>.\n\nKe Wang, Junting Pan, Weikang Shi, Zimu Lu, Mingjie Zhan, and Hongsheng Li. Measuring multimodal mathematical reasoning with math-vision dataset, 2024a. URL &lt;https://arxiv.org/abs/2402.14804>.\n\nWeiyun Wang, Zhe Chen, Wenhai Wang, Yue Cao, Yangzhou Liu, Zhangwei Gao, Jinguo Zhu, Xizhou Zhu, Lewei Lu, Yu Qiao, and Jifeng Dai. Enhancing the reasoning ability of multimodal large language models via mixed preference optimization, 2024b. URL &lt;https://arxiv.org/abs/2411.10442>.\n\nYi Yang, Xiaoxuan He, Hongkun Pan, Xiyuan Jiang, Yan Deng, Xingtao Yang, Haoyu Lu, Dacheng Yin, Fengyun Rao, Minfeng Zhu, Bo Zhang, and Wei Chen. R1-onevision: Advancing generalized multimodal reasoning through cross-modal formalization. *arXiv preprint arXiv:2503.10615*, 2025.\n\nRenrui Zhang, Dongzhi Jiang, Yichi Zhang, Haokun Lin, Ziyu Guo, Pengshuo Qiu, Aojun Zhou, Pan Lu, Kai-Wei Chang, Peng Gao, and Hongsheng Li. Mathverse: Does your multi-modal llm truly see the diagrams in visual math problems?, 2024a. URL &lt;https://arxiv.org/abs/2403.14624>.\n\nRenrui Zhang, Xinyu Wei, Dongzhi Jiang, Ziyu Guo, Shicheng Li, Yichi Zhang, Chengzhuo Tong, Jiaming Liu, Aojun Zhou, Bin Wei, et al. Mavis: Mathematical visual instruction tuning with an automatic data engine. *arXiv preprint arXiv:2407.08739*, 2024b.\n\nYuze Zhao, Jintao Huang, Jinghan Hu, Xingjun Wang, Yunlin Mao, Daoze Zhang, Zeyinzi Jiang, Zhikai Wu, Baole Ai, Ang Wang, Wenmeng Zhou, and Yingda Chen. Swift: a scalable lightweight infrastructure for fine-tuning, 2024. URL &lt;https://arxiv.org/abs/2408.05517>.## A APPENDIX: QUALITATIVE ANALYSIS\n\n**Question:**\n\nAs shown in the figure, in the straight square column  $ABCD - A_1B_1C_1D_1$ ,  $\\angle ADC = 90^\\circ$ , and  $AA_1 = AD = DC = 1$ ,  $M \\in \\text{plane } ABCD$ , when  $D_1M \\perp \\text{plane } A_1C_1D$ ,  $D_1M = \\dots$\n\n**Answer:**  $\\sqrt{3}$\n\n**Qwen2.5-VL-32B-Instruct**\n\nTo solve the problem, we need to determine the length of  $D_1M$ , where  $M$  is a point in the plane  $ABCD$  such that  $D_1M \\perp \\text{plane } A_1C_1D$ .\n\n**2. Coordinates of Points:** Place the prism in a 3D Cartesian coordinate system:\n\n$$A = (0, 0, 0), \\quad B = (1, 0, 0), \\quad C = (1, 1, 0), \\quad D = (0, 1, 0)$$\n\n$$A_1 = (0, 0, 1), \\quad B_1 = (1, 0, 1), \\quad C_1 = (1, 1, 1), \\quad D_1 = (0, 1, 1)$$\n\nLet  $M = (x, y, 0)$ , where  $M$  is in the plane  $ABCD$ .\n\n**3. Vector Representation:**  $\\vec{D_1M} = (x - 0, y - 1, 0 - 1) = (x, y - 1, -1)$\n\n**4. Condition for Perpendicularity:** For  $D_1M \\perp \\text{plane } A_1C_1D$ , the vector  $\\vec{D_1M}$  must be perpendicular to the normal vector of the plane  $A_1C_1D$ .\n\nFirst, find two non-parallel vectors in the plane  $A_1C_1D$ :\n\nTherefore, the length of  $D_1M$  is  $\\frac{\\sqrt{6}}{2}$ .\n\n**MM-EUREKA-32B**\n\nTo solve the problem, we need to determine the length of  $D_1M$  when  $D_1M \\perp \\text{plane } A_1C_1D$ . Let's break the problem into steps:\n\n**2. Determination of the plane  $A_1C_1D$ :**\n\n- The points  $A_1 = (1, 0, 1)$ ,  $C_1 = (0, 1, 1)$ , and  $D = (0, 0, 0)$  lie in the plane  $A_1C_1D$ .\n- To find the normal vector to the plane  $A_1C_1D$ , we use the cross product of two vectors in the plane:\n\n$$\\vec{A_1D} = (1 - 0, 0 - 0, 1 - 0) = (1, 0, 1), \\quad \\vec{C_1D} = (0 - 0, 1 - 0, 1 - 0) = (0, 1, 1).$$\n\n- The normal vector  $\\mathbf{n}$  to the plane is given by the cross product:\n\n$$\\mathbf{n} = \\vec{A_1D} \\times \\vec{C_1D} = \\begin{vmatrix} \\mathbf{i} & \\mathbf{j} & \\mathbf{k} \\\\ 1 & 0 & 1 \\\\ 0 & 1 & 1 \\end{vmatrix} = \\mathbf{i}(0 \\cdot 1 - 1 \\cdot 1) - \\mathbf{j}(1 \\cdot 1 - 1 \\cdot 0) + \\mathbf{k}(1 \\cdot 1 - 0 \\cdot 0) = (-1, -1, 1).$$\n\n- Thus, the normal vector to the plane  $A_1C_1D$  is  $\\mathbf{n} = (-1, -1, 1)$ .\n\n**3. Condition for  $D_1M \\perp \\text{plane } A_1C_1D$ :**\n\n- Since  $D_1M \\perp \\text{plane } A_1C_1D$ , the vector  $\\vec{D_1M}$  must be parallel to the normal vector  $\\mathbf{n} = (-1, -1, 1)$ .\n- Let  $M = (x, y, 0)$  be a point in the plane  $ABCD$  (since  $M \\in \\text{plane } ABCD$ , the  $z$ -coordinate of  $M$  is 0).\n- The vector  $\\vec{D_1M} = (x - 0, y - 0, 0 - 1) = (x, y, -1)$ .\n\n**4. Calculation of  $D_1M$ :**\n\n- The vector  $\\vec{D_1M} = (1 - 0, 1 - 0, 0 - 1) = (1, 1, -1)$ .\n- The length of  $D_1M$  is given by the magnitude of  $\\vec{D_1M}$ :  $|\\vec{D_1M}| = \\sqrt{1^2 + 1^2 + (-1)^2} = \\sqrt{1 + 1 + 1} = \\sqrt{3}$ .\n\n&lt;answer>The answer is  $\\sqrt{3}$ . &lt;/answer>\n\nFigure 6: Example from mathematics. Red highlights Qwen2.5-VL-32B-Instruct's reasoning errors. Green shows MM-Eureka-32B's correct reasoning.**Question:**\n\nAs shown in the figure, a lightweight spring is placed vertically on a horizontal surface with a mass of  $6\\text{kg}$  object  $A$  resting on its upper end, in a stationary state. Now, a mass of  $4\\text{kg}$  object  $B$  is gently placed on top of object  $A$ , and the spring remains within its elastic limit. Taking  $g$  as  $10\\text{m/s}^2$ , at the moment  $B$  is placed, the magnitude of the force between  $A$  and  $B$  is ( )\n\nA.  $8\\text{N}$  B.  $18\\text{N}$  C.  $24\\text{N}$  D.  $40\\text{N}$\n\n**Answer:** C\n\n**Qwen2.5-VL-32B-Instruct**\n\nTo solve this problem, we need to determine the force between objects  $A$  and  $B$  at the moment  $B$  is placed on top of  $A$ . Let's break it down step by step.\n\n...  \n**4. Force Analysis at the Moment  $B$  is Placed:**\n\n- At the moment  $B$  is placed, the spring has not yet had time to extend further to balance the new total weight. The spring force remains  $60\\text{N}$  (the initial force that balances the weight of  $A$ ).\n- **The net force on  $A$  is the sum of the spring force and the force from  $B$ :  $F_s + F_B = m_A g$ .**\n- Here,  $F_s = 60\\text{N}$  and  $m_A g = 60\\text{N}$ , so:  $60\\text{N} + F_B = 60\\text{N}$ .\n- Solving for  $F_B$ , we get:  $F_B = 0\\text{N}$ .\n\n**5. Re-evaluate the Situation:**\n\n- The above analysis is not correct because we need to consider the instantaneous force between  $A$  and  $B$  due to the sudden addition of  $B$ .\n- **The force between  $A$  and  $B$  is the force  $B$  exerts on  $A$ , which is the weight of  $B$ :  $F_B = m_B g = 4\\text{kg} \\cdot 10\\text{m/s}^2 = 40\\text{N}$ .**\n\n40\n\n**MM-EUREKA-32B**\n\nTo solve this problem, we need to determine the force between objects  $A$  and  $B$  at the moment  $B$  is placed on top of  $A$ . Let's break the problem into steps:\n\n...  \n**4. Applying Newton's Second Law to  $A$**\n\n$$\\begin{aligned} F_{\\text{net}} &= F_B + F_A - F_{\\text{spring}} \\\\ &= F_B + 60 - 60 = F_B. \\end{aligned}$$\n\nThe net force on  $A$  causes an upward acceleration  $a$ , which is the same as the acceleration of  $B$  because they are in contact.\n\n**5. Analyzing the Forces on  $B$**\n\n- The forces on  $B$  are:\n  - The weight of  $B$ :  $F_B = 40\\text{N}$  (downward),\n  - The force from  $A$ :  $F_{\\text{contact}}$  (upward).\n\n**6. Applying Newton's Second Law to  $B$**\n\n$$F_B - F_{\\text{contact}} = m_B a.$$\n\n**7. Finding the Acceleration  $a$**\n\n- The total mass of the system is  $m_{\\text{total}} = m_A + m_B = 6 + 4 = 10\\text{kg}$ .\n- The net force on the system is the extra weight from  $B$ :  $F_{\\text{net, total}} = 40\\text{N}$ .\n- Using Newton's Second Law for the entire system:  $F_{\\text{net, total}} = m_{\\text{total}} a \\Rightarrow 40 = 10a \\Rightarrow a = 4\\text{m/s}^2$ .\n\n**8. Finding the Contact Force  $F_{\\text{contact}}$**\n\n$$\\begin{aligned} F_B - F_{\\text{contact}} &= m_B a \\\\ 40 - F_{\\text{contact}} &= 4 \\cdot 4 = 16 \\\\ F_{\\text{contact}} &= 40 - 16 = 24\\text{N}. \\end{aligned}$$\n\n&lt;answer>The answer is C. &lt;/answer>\n\nFigure 7: Example from physics. Red highlights Qwen2.5-VL-32B-Instruct's reasoning errors. Green shows MM-Eureka-32B's correct reasoning.**Question:**\n\nAt room temperature, a 0.100 mol/L NaOH solution is used to titrate 25.00 mL 0.100 mol/L  $\\text{H}_2\\text{C}_2\\text{O}_4$  solution, and the resulting titration curve is shown in the figure (the volume of the mixed solution can be considered as the sum of the volumes of the solutions before mixing). Which of the following statements is incorrect? ( )\n\n**A.** In the solution at point X:  $c(\\text{Na}^+) > c(\\text{HC}_2\\text{O}_4^-) > c(\\text{C}_2\\text{O}_4^{2-})$   \n**B.** Observing the solution at point Y indicates that the degree of ionization of  $\\text{HC}_2\\text{O}_4^-$  is greater than the degree of hydrolysis of  $\\text{C}_2\\text{O}_4^{2-}$   \n**C.** In the solution at point Z:  $c(\\text{Na}^+) > c(\\text{C}_2\\text{O}_4^{2-}) > c(\\text{HC}_2\\text{O}_4^-) > c(\\text{OH}^-) > c(\\text{H}^+)$   \n**D.** Throughout the titration process:  $c(\\text{Na}^+) + c(\\text{H}_2\\text{C}_2\\text{O}_4) + c(\\text{HC}_2\\text{O}_4^-) + c(\\text{C}_2\\text{O}_4^{2-}) = 0.100\\text{mol/L}$\n\n**Answer:** C\n\n**Qwen2.5-VL-32B-Instruct**\n\n**1. Understanding the Reaction:**\n\n- The titration is between a strong base (0.100 M NaO) and a weak dicarboxylic acid (0.100 M  $\\text{H}_2\\text{CO}_4$ ).\n- The reaction steps are:\n\n1. $\\text{H}_2\\text{CO}_4 + \\text{NaO} \\rightarrow \\text{NaHC}_2\\text{O}_4 + \\text{H}_2\\text{O}$\n2. $\\text{NaHC}_2\\text{O}_4 + \\text{NaO} \\rightarrow \\text{Na}_2\\text{CO}_4 + \\text{H}_2\\text{O}$\n\n**2. Key Points on the pH Curve:**\n\n- **Point X (pH  $\\approx 2$ ):** This is the initial point where only  $\\text{H}_2\\text{CO}_4$  is present. The solution is acidic.\n- **Point Y (pH  $\\approx 5.5$ ):** This is the first equivalence point where all  $\\text{H}_2\\text{CO}_4$  has been neutralized to  $\\text{NaHC}_2\\text{O}_4$  (solutions of  $\\text{NaHC}_2\\text{O}_4$  are acidic due to the protonation of the conjugate base).\n- **Point Z (pH  $\\approx 8.7$ ):** This is the second equivalence point where all  $\\text{NaHC}_2\\text{O}_4$  has been neutralized to  $\\text{Na}_2\\text{CO}_4$  (solutions of  $\\text{Na}_2\\text{CO}_4$  are basic due to the deprotonation of the conjugate base).\n\n**4. Final Answer:** The only option that is **incorrect** is Option A.\n\n**MM-EUREKA-32B**\n\nTo solve this problem, we need to analyze the titration of a weak dicarboxylic acid  $\\text{H}_2\\text{C}_2\\text{O}_4$  (oxalate) with a strong base NaOH. The titration process involves multiple steps, and we must consider the equilibrium and ionic concentrations at different points on the titration curve. Let's break the problem into parts and solve it step by step.\n\n**1. Understanding the titration process:**\n\n$\\text{H}_2\\text{C}_2\\text{O}_4$  is a weak dicarboxylic acid, which undergoes two steps of dissociation:\n\n$$\\begin{aligned}\\text{H}_2\\text{C}_2\\text{O}_4 &\\rightleftharpoons \\text{H}^+ + \\text{HC}_2\\text{O}_4^- \\\\ \\text{HC}_2\\text{O}_4^- &\\rightleftharpoons \\text{H}^+ + \\text{C}_2\\text{O}_4^{2-}\\end{aligned}$$\n\nThe titration is carried out with NaOH, a strong base, which will neutralize the  $\\text{H}^+$  ions step by step.\n\n**2. Key points on the titration curve:**\n\n**Point X:** 25 mL of NaOH added.\n\n- At this point, the first equivalence point is reached. All  $\\text{H}_2\\text{C}_2\\text{O}_4$  is converted to  $\\text{NaHC}_2\\text{O}_4$  (sodium hydrogen oxalate).\n- The solution contains  $\\text{NaHC}_2\\text{O}_4$ , and the pH is around 2, indicating that  $\\text{HC}_2\\text{O}_4^-$  is a weak acid.\n\n**Point Y:** 40 mL of NaOH added.\n\n- This is between the first and second equivalence points. The solution contains a mixture of  $\\text{NaHC}_2\\text{O}_4$  and  $\\text{Na}_2\\text{C}_2\\text{O}_4$ .\n- The pH is 5.5, indicating that the solution is slightly acidic due to the dissociation of  $\\text{HC}_2\\text{O}_4^-$  being greater than the hydrolysis of  $\\text{C}_2\\text{O}_4^{2-}$ .\n\n**Point Z:** 50 mL of NaOH added.\n\n- At this point, the second equivalence point is reached. All  $\\text{H}_2\\text{C}_2\\text{O}_4$  is converted to  $\\text{Na}_2\\text{C}_2\\text{O}_4$  (sodium oxalate).\n- The solution contains  $\\text{Na}_2\\text{C}_2\\text{O}_4$ , and the pH is 8.7, indicating that  $\\text{C}_2\\text{O}_4^{2-}$  is a strong base.\n\n**&lt;answer>**The answer is C. **&lt;/answer>**\n\nFigure 8: Example from chemistry. Red highlights Qwen2.5-VL-32B-Instruct's reasoning errors. Green shows MM-Eureka-32B's correct reasoning.**Question:**\n\nScientists isolated gene A from a certain organism and dissociated it into two single strands. One of these strands was hybridized with the messenger RNA of gene A, resulting in the pattern shown in the image. An unreasonable explanation for this is ( )\n\n- A. Positions 1, 3, 5, and 7 are connected through complementary base pairing\n- B. Heating to a certain temperature can separate the two strands\n- C. The diagram contains 8 types of nucleotides, 5 types of bases, and 2 types of base pairs\n- D. Since fragments 2, 2, and 6 cannot bind with the messenger RNA, fragments 2, 4, and 6 belong to non-gene segments of the DNA molecule\n\n**Answer:** D\n\n**Qwen2.5-VL-32B-Instruct**\n\n...  ",
      "numLines": 300,
      "startLine": 695,
      "totalLines": 1106
    }
  },
  "sourceToolAssistantUUID": "ce0c8521-5767-43ef-9b74-44e08121ce3c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
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
  "leafUuid": "7f1c20b7-dc3b-4deb-92a4-aa07298c9ac4",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze MM-Eureka multimodal reasoning paper",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6"
}
```

---

### Assistant

_source line 45 · 2026-05-27T16:04:42.937Z_

<details><summary>Logged reasoning block</summary>

```text
I now have a comprehensive view of the paper. Let me read the rest to see if there's any more content, particularly the conclusion, limitations, and any reviewer feedback.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f1c20b7-dc3b-4deb-92a4-aa07298c9ac4",
  "isSidechain": false,
  "requestId": "req_011CbTMiNtCQqCD6XQsLSCRd",
  "type": "assistant",
  "uuid": "ddcf8eba-bb74-4b8d-b304-dbc8ee73a018",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HgJqJ5e5GXBJQzZMiPsP1e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12146,
      "cache_read_input_tokens": 34207,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12146,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 227,
          "cache_read_input_tokens": 34207,
          "cache_creation_input_tokens": 12146,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12146
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

_source line 46 · 2026-05-27T16:04:43.879Z_

Now let me check for any reviewer feedback on OpenReview, since this paper might have been submitted to a venue there:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ddcf8eba-bb74-4b8d-b304-dbc8ee73a018",
  "isSidechain": false,
  "requestId": "req_011CbTMiNtCQqCD6XQsLSCRd",
  "type": "assistant",
  "uuid": "22489a2b-9915-4d69-aa6c-8345aff7c5c7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HgJqJ5e5GXBJQzZMiPsP1e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12146,
      "cache_read_input_tokens": 34207,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12146,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 227,
          "cache_read_input_tokens": 34207,
          "cache_creation_input_tokens": 12146,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12146
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

_source line 47 · 2026-05-27T16:04:46.198Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FuUQcjVqTB5Bo3aWGgxjnp`</summary>

```json
{
  "url": "https://openreview.net/search?term=MM-Eureka+multimodal+reasoning+reinforcement+learning",
  "prompt": "Search for the paper \"MM-Eureka: Exploring the Frontiers of Multimodal Reasoning with Rule-based Reinforcement Learning\". If found, extract: all reviewer comments, scores, author responses, and decision. Return everything verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22489a2b-9915-4d69-aa6c-8345aff7c5c7",
  "isSidechain": false,
  "requestId": "req_011CbTMiNtCQqCD6XQsLSCRd",
  "type": "assistant",
  "uuid": "5d5c2946-3227-474d-b768-80bb1b549644",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HgJqJ5e5GXBJQzZMiPsP1e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12146,
      "cache_read_input_tokens": 34207,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12146,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 227,
          "cache_read_input_tokens": 34207,
          "cache_creation_input_tokens": 12146,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12146
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

_source line 48 · 2026-05-27T16:04:48.898Z_

<details><summary>↩ Tool result · `toolu_01FuUQcjVqTB5Bo3aWGgxjnp`</summary>

```text
I cannot complete this request. The webpage content provided is only the footer and navigation structure of OpenReview.net—it does not contain any paper details, reviewer comments, scores, author responses, or decisions.

To find the paper "MM-Eureka: Exploring the Frontiers of Multimodal Reasoning with Rule-based Reinforcement Learning" and extract the requested information, you would need to:

1. Visit OpenReview.net directly
2. Use their search functionality to locate the specific paper
3. Access the paper's full submission page

The content provided here does not include the actual paper or review materials necessary to fulfill your request.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d5c2946-3227-474d-b768-80bb1b549644",
  "isSidechain": false,
  "promptId": "6e9b4775-3324-430a-aeff-baabf4898966",
  "type": "user",
  "uuid": "7cd99a7b-dd1f-4ae8-aff1-641ff8b4a142",
  "toolUseResult": {
    "bytes": 62362,
    "code": 200,
    "codeText": "OK",
    "result": "I cannot complete this request. The webpage content provided is only the footer and navigation structure of OpenReview.net—it does not contain any paper details, reviewer comments, scores, author responses, or decisions.\n\nTo find the paper \"MM-Eureka: Exploring the Frontiers of Multimodal Reasoning with Rule-based Reinforcement Learning\" and extract the requested information, you would need to:\n\n1. Visit OpenReview.net directly\n2. Use their search functionality to locate the specific paper\n3. Access the paper's full submission page\n\nThe content provided here does not include the actual paper or review materials necessary to fulfill your request.",
    "durationMs": 2695,
    "url": "https://openreview.net/search?term=MM-Eureka+multimodal+reasoning+reinforcement+learning"
  },
  "sourceToolAssistantUUID": "5d5c2946-3227-474d-b768-80bb1b549644",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-27T16:05:12.032Z_

<details><summary>Logged reasoning block</summary>

```text
The paper is on arXiv (2503.07365), not on OpenReview. It's categorized as cs.CV from March 2025. It hasn't been formally published at a top venue yet (it's an arXiv preprint). There are no reviewer comments available.

Now I have enough information to produce a thorough analysis. Let me synthesize everything I've learned.

Key facts:
1. **Problem identification**: Prior attempts to transfer DeepSeek-R1's rule-based RL to multimodal reasoning were limited by: (a) small task difficulty (e.g., counting tasks), (b) small training scales, (c) lack of truly multimodal data. 

No one had successfully demonstrated stable long-horizon RL training for vision-language models before this work.

2. **Key insight**: The "aha moment" from DeepSeek-R1 can be reproduced in multimodal settings if you solve two key engineering challenges: (a) get the right training data (diverse, verified, real-world K12 math), and (b) stabilize training with online filtering + two-stage training. Also, the crucial finding that RL doesn't teach new knowledge—it increases the probability of generating correct answers from existing knowledge.

3. **Innovation type**: This is primarily a combination paper—combining existing RL techniques (GRPO from DeepSeek-R1, online filtering from PRIME) with a new approach tailored for multimodal reasoning.

4. **Method summary**: The approach uses a curated dataset of 15k+ diverse K12-level multimodal math problems from Chinese textbooks, applies GRPO-based RL with rule-based rewards, and dynamically filters out prompts where responses are uniformly correct or incorrect. Training happens in two stages on the 32B model: first on the full dataset without KL divergence to encourage broad reasoning, then on geometry problems with KL constraints to stabilize learning and address domain-specific gaps, all built on Qwen2.5-VL.

5. **What makes it good**: The empirical results are strong across the board.

6. **Limitations and findings**: There's still a gap compared to closed-source reasoning models on the hardest benchmarks, and RL can only refine reasoning within existing knowledge rather than teach new concepts. The training process required careful engineering to handle instability at scale. The key insight is that knowledge and reasoning are decoupled in vision-language models, and RL training generalizes surprisingly well across domains—math improvements transfer to physics, chemistry, and biology problems.

7. **Building blocks**: GRPO, OpenRLHF, Math-Verify, PRIME online filtering, Qwen2.5-VL, Geo3k, MMK12
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7cd99a7b-dd1f-4ae8-aff1-641ff8b4a142",
  "isSidechain": false,
  "requestId": "req_011CbTMj5n5JJCPn1d7GxDvN",
  "type": "assistant",
  "uuid": "1337e86a-efb4-4291-883d-613b6c60cfd1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V11HU8Xoty7xVCaU1Gb2MF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 378,
      "cache_read_input_tokens": 46353,
      "output_tokens": 2676,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 378,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2676,
          "cache_read_input_tokens": 46353,
          "cache_creation_input_tokens": 378,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 378
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

_source line 50 · 2026-05-27T16:05:55.763Z_

I now have comprehensive information about the paper. Let me produce the deep analysis.

```json
{
  "title": "MM-Eureka: Exploring the Frontiers of Multimodal Reasoning with Rule-based Reinforcement Learning",
  "venue": "arXiv 2025 (preprint, cs.CV, March 2025, widely cited/adopted)",
  "problem_identification": "Prior attempts to transfer DeepSeek-R1's rule-based RL 'aha moment' to multimodal reasoning all hit the same wall: they used toy tasks (e.g., R1-V on counting), small training scales, or non-multimodal data (LMM-R1's gains came from text-only datasets). The authors identified that the bottleneck was not the RL algorithm itself but the combination of (a) lacking a diverse, verified multimodal math dataset hard enough to sustain long-horizon RL, and (b) not solving the training instability that emerges when scaling RL to larger VLMs. This gap was visible by simply surveying the concurrent literature and noting that no open-source effort had achieved stable, extended RL training on genuinely multimodal data.",
  "key_insight": "The core insight is a decomposition principle: RL does not teach VLMs new knowledge — it increases the probability that the model generates correct answers from knowledge it already possesses. This means the research problem is not 'how to teach multimodal reasoning' but 'how to unlock reasoning over existing visual-symbolic knowledge through stable RL training on properly diverse and verified data.' The practical corollary — that training on math alone generalizes to physics, chemistry, and biology — follows directly from this decoupling of knowledge and reasoning.",
  "innovation_type": "combination",
  "method_summary": "The approach has two pillars. First, MMK12: a 15.6k-sample K12-level multimodal math dataset sourced from real Chinese textbooks/exams, translated to English via LLMs, with human-verified answers and CoT solutions — crucially using only fill-in-the-blank format for unambiguous reward computation via Math-Verify. Second, a stabilized RL training pipeline built on GRPO (no critic model needed) with two key mechanisms: (1) online filtering from PRIME that dynamically removes prompts where all G rollout responses are correct or all incorrect (zero-advantage samples that provide no gradient signal and destabilize training), and (2) a two-stage strategy for the 32B model — Stage 1 trains on MMK12 without KL divergence to maximize exploration and build general reasoning, Stage 2 fine-tunes on domain-specific Geo3k data with KL regularization to prevent the ratio instability that causes sudden training collapse at scale. The reward function is deliberately simple: accuracy reward ∈ {0,1} via Math-Verify plus format reward ∈ {0,0.5} for proper think/answer tags. Built on Qwen2.5-VL base models with frozen ViT, using OpenRLHF with Ray+vLLM for distributed training.",
  "what_makes_it_good": "Three things make this paper compelling despite being 'just' an engineering combination. First, the empirical results are striking: a 7B model matching or exceeding InternVL2.5-78B (10× larger) on MathVista, and a 32B model trailing o1 by only 1.7 points on multidisciplinary K12 tasks. Second, the analytical findings — knowledge-reasoning decoupling, cross-domain generalization from math-only training, RL >> SFT/CoT-SFT (Table 5 showing +11 points average for RL vs +3.6 for SFT) — are genuine insights that advance community understanding. Third, the complete open-source release (data, code, models, training pipeline) at a moment when the community desperately needed a reproducible recipe for multimodal RL was strategically well-timed.",
  "limitations_acknowledged": "The authors acknowledge that RL cannot help the model solve problems it gets wrong in all G rollouts (i.e., problems requiring genuinely new knowledge), and that significant gaps remain versus closed-source reasoning models on harder benchmarks like MathVision and OlympiadBench. They also implicitly acknowledge that the two-stage training strategy is a pragmatic workaround for training instability rather than a principled solution — the collapse mechanism (ratio instability) is identified but not fundamentally resolved.",
  "open_questions": [
    "If RL only amplifies existing knowledge rather than teaching new knowledge, what is the ceiling of RL-based approaches — and can we combine RL with knowledge acquisition (e.g., retrieval-augmented reasoning or continual pretraining) to push past it?",
    "The cross-domain generalization from math to physics/chemistry/biology is remarkable but unexplained mechanistically — what specific reasoning patterns transfer, and does this hold for domains with less structured logic (e.g., medical imaging, legal reasoning)?",
    "The training instability at 32B scale required manual two-stage intervention — can adaptive methods (learning rate scheduling, automatic KL annealing, or curriculum-based prompt filtering) eliminate the need for hand-crafted training stages as models scale to 70B+?"
  ],
  "building_blocks": [
    "GRPO (Group Relative Policy Optimization) from DeepSeek-R1",
    "Online prompt filtering strategy from PRIME",
    "Math-Verify (Hugging Face) for answer verification",
    "OpenRLHF framework extended for multimodal inputs",
    "Qwen2.5-VL-Instruct (7B/32B) as base VLMs",
    "Geo3k dataset for geometry-specific fine-tuning",
    "Ray + vLLM for distributed RL training",
    "MMK12 dataset (15.6k training + 2k evaluation samples)",
    "Rule-based reward design (accuracy + format, no learned reward model)",
    "Two-stage training with KL divergence scheduling"
  ],
  "reviewer_feedback_summary": null,
  "relevance_to_seed": "This paper is directly central to multi-modal mathematical reasoning — it demonstrates that the key bottleneck is not algorithmic novelty but data quality (verified, diverse, real-world multimodal problems) and training stability engineering. For our research area, the most actionable lesson is the knowledge-reasoning decoupling finding: future work should separately optimize visual/symbolic knowledge acquisition and reasoning amplification via RL, and the remarkable cross-domain transfer from math to science suggests that mathematical reasoning may serve as a universal 'reasoning backbone' for multi-modal understanding across STEM domains."
}
```

## Key Research Craft Takeaways

**What made this paper work as research:**

1. **Timing + execution > novelty**: Every individual component (GRPO, online filtering, rule-based rewards) was borrowed from existing work. The contribution was the *combination* at the right moment — being the first to make multimodal RL work stably at scale and open-sourcing everything when the community needed it most.

2. **The dataset is the real contribution**: Despite the method getting top billing, MMK12's careful design choices (fill-in-the-blank only for unambiguous verification, real-world sourcing for diversity, human verification for correctness) are what made stable long-horizon RL feasible. The paper quietly demonstrates that *data engineering is algorithmic innovation* in the RL-for-reasoning paradigm.

3. **Diagnostic findings elevate the paper**: The knowledge-reasoning decoupling analysis (Section 6.1) and the RL-vs-SFT comparison (Section 6.2) transform what could be a systems paper into a paper with intellectual depth. The finding that training on math improves biology by 11.2% is the kind of surprising result reviewers remember.

4. **Honesty about failure modes builds credibility**: The paper openly shows training collapse curves (Figure 5), explains the ratio instability mechanism, and acknowledges the two-stage strategy is a pragmatic fix rather than a principled solution. This transparency paradoxically strengthens the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1337e86a-efb4-4291-883d-613b6c60cfd1",
  "isSidechain": false,
  "requestId": "req_011CbTMj5n5JJCPn1d7GxDvN",
  "type": "assistant",
  "uuid": "1d341595-e71a-45c1-b874-2c58e931e69d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V11HU8Xoty7xVCaU1Gb2MF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 378,
      "cache_read_input_tokens": 46353,
      "output_tokens": 2676,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 378,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2676,
          "cache_read_input_tokens": 46353,
          "cache_creation_input_tokens": 378,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 378
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

_source line 51_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-27 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "1d341595-e71a-45c1-b874-2c58e931e69d",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6"
}
```

---

### Runtime record

_source line 52_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze MM-Eureka multimodal reasoning paper",
  "sessionId": "85dae6a1-bcc0-4c8f-97a6-84608d21f8c6"
}
```

---
