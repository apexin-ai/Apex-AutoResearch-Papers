# Research conversation: You are a senior ML researcher performing a deep analysis of a published paper. **Today's date: 2026-05-27 (UTC).** ## Y

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 63
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-1/2d2f5f70-a94f-402d-8c92-8c562e7598cd.jsonl`
- **Structured JSON:** [`1584aa7eaa57f5367c4a.json`](../../sessions/15/1584aa7eaa57f5367c4a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T15:22:08.721Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T15:22:08.721Z",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "content": "You are a senior ML researcher performing a deep analysis of a published paper.\n\n**Today's date: 2026-05-27 (UTC).**\n\n## Your goal\n\nAnalyze this paper NOT just for what it does, but for **HOW it innovates** — what can we learn from its approach to doing research? What made this paper good enough for a top venue?\n\n## Research context\n\nWe are generating ideas in the area of: **Process Reward Models for Mathematical Reasoning — Step-Level Verification and Credit Assignment**\n\n## Paper to analyze\n\n{\n  \"title\": \"Let's Verify Step by Step\",\n  \"authors\": \"Hunter Lightman et al.\",\n  \"venue\": \"ICLR 2024\",\n  \"url\": \"https://arxiv.org/abs/2305.20050\",\n  \"why_important\": \"Foundational paper from OpenAI; introduced PRM800K (800K human step-level labels); established that process supervision significantly outperforms outcome supervision; extremely highly cited (1000+ citations); defined the field\",\n  \"one_line_summary\": \"Demonstrates that training reward models with step-level human feedback (process supervision) significantly outperforms outcome-only supervision on the MATH benchmark, and releases the PRM800K dataset.\"\n}\n\n## Instructions\n\n1. **Deep read**: Use WebFetch to read this paper's full abstract, introduction, method section, and conclusion on arXiv or OpenReview. If it's on OpenReview, also read the reviewer comments and author responses.\n\n2. **Analyze the innovation structure**: Don't just summarize — dissect HOW the authors arrived at their contribution:\n   - What gap did they identify and HOW did they find it?\n   - What was the key insight that others missed?\n   - How did they formulate the problem differently from prior work?\n   - What existing technique did they adapt/combine/simplify?\n\n3. **Learn from reviewers**: If you can find reviewer comments, extract:\n   - What did reviewers praise most?\n   - What concerns were raised and how were they addressed?\n   - What would have made this paper even stronger?\n\n## Output format\n\nOutput a single JSON object:\n{\n  \"title\": \"Paper title\",\n  \"venue\": \"Where published\",\n  \"problem_identification\": \"What gap/problem did they identify? How did they find it? (2-3 sentences)\",\n  \"key_insight\": \"The core intellectual contribution — the aha moment (1-2 sentences)\",\n  \"innovation_type\": \"new_formulation | new_technique | new_benchmark | simplification | cross_domain | combination | scaling | analysis\",\n  \"method_summary\": \"Technical approach in 3-5 sentences — enough to understand the machinery\",\n  \"what_makes_it_good\": \"Why did this paper get accepted? What would reviewers have liked? (2-3 sentences)\",\n  \"limitations_acknowledged\": \"What gaps did the authors themselves identify? (1-2 sentences)\",\n  \"open_questions\": \"What follow-up questions does this paper raise? What remains unsolved? (2-3 bullet points)\",\n  \"building_blocks\": [\"List of methods/tools/datasets used that could be reused\"],\n  \"reviewer_feedback_summary\": \"If found on OpenReview: key praise and concerns. Otherwise: null\",\n  \"relevance_to_seed\": \"How does this paper relate to our research area? What can we learn from it? (1-2 sentences)\"\n}\n\nBe analytical, not descriptive. We want to learn the CRAFT of doing good research, not just know what this paper did."
}
```

---

### Runtime record

_source line 2 · 2026-05-27T15:22:08.725Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T15:22:08.725Z",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd"
}
```

---

## Round 1

61 recorded events

### User

_source line 3 · 2026-05-27T15:22:08.763Z_

You are a senior ML researcher performing a deep analysis of a published paper.

**Today's date: 2026-05-27 (UTC).**

## Your goal

Analyze this paper NOT just for what it does, but for **HOW it innovates** — what can we learn from its approach to doing research? What made this paper good enough for a top venue?

## Research context

We are generating ideas in the area of: **Process Reward Models for Mathematical Reasoning — Step-Level Verification and Credit Assignment**

## Paper to analyze

{
  "title": "Let's Verify Step by Step",
  "authors": "Hunter Lightman et al.",
  "venue": "ICLR 2024",
  "url": "https://arxiv.org/abs/2305.20050",
  "why_important": "Foundational paper from OpenAI; introduced PRM800K (800K human step-level labels); established that process supervision significantly outperforms outcome supervision; extremely highly cited (1000+ citations); defined the field",
  "one_line_summary": "Demonstrates that training reward models with step-level human feedback (process supervision) significantly outperforms outcome-only supervision on the MATH benchmark, and releases the PRM800K dataset."
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
  "promptId": "847a487e-d454-4fe9-b1b6-24705f0c37b0",
  "type": "user",
  "uuid": "28e20f89-36f8-4504-8cdd-2d5150943ca7",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T15:22:08.762Z_

```json
{
  "parentUuid": "28e20f89-36f8-4504-8cdd-2d5150943ca7",
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
  "uuid": "7b701aae-761f-418b-b52b-af210550d20e",
  "timestamp": "2026-05-27T15:22:08.762Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T15:22:08.762Z_

```json
{
  "parentUuid": "7b701aae-761f-418b-b52b-af210550d20e",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "98a39ee2-5b0f-40af-8c72-5b6b0c64d35a",
  "timestamp": "2026-05-27T15:22:08.762Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
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
  "aiTitle": "Analyze OpenAI's process reward models paper",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd"
}
```

---

### Assistant

_source line 7 · 2026-05-27T15:22:12.153Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to analyze the paper "Let's Verify Step by Step" by Hunter Lightman et al. (ICLR 2024). I need to fetch the paper from arXiv and also check OpenReview for reviewer comments. Let me start by fetching the paper and reviewer comments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98a39ee2-5b0f-40af-8c72-5b6b0c64d35a",
  "isSidechain": false,
  "requestId": "req_011CbTJUNDGjpGmSMf8wefd5",
  "type": "assistant",
  "uuid": "f9054a36-077a-4394-a608-661589e79473",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EhbunGwmZLcnbEotbhVdaq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2184,
      "cache_read_input_tokens": 11014,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2184,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 158,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 2184,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2184
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

_source line 8 · 2026-05-27T15:22:12.590Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011fjimHLqd7LyP3Jk8HqN7h`</summary>

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
  "parentUuid": "f9054a36-077a-4394-a608-661589e79473",
  "isSidechain": false,
  "requestId": "req_011CbTJUNDGjpGmSMf8wefd5",
  "type": "assistant",
  "uuid": "2632a2a4-8e33-43e0-97fb-e90b5359f00a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EhbunGwmZLcnbEotbhVdaq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2184,
      "cache_read_input_tokens": 11014,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2184,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 158,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 2184,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2184
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

_source line 9 · 2026-05-27T15:22:12.599Z_

<details><summary>↩ Tool result · `toolu_011fjimHLqd7LyP3Jk8HqN7h`</summary>

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
  "parentUuid": "2632a2a4-8e33-43e0-97fb-e90b5359f00a",
  "isSidechain": false,
  "promptId": "847a487e-d454-4fe9-b1b6-24705f0c37b0",
  "type": "user",
  "uuid": "cb774a80-d309-42a0-a5a3-53331a286cc2",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "2632a2a4-8e33-43e0-97fb-e90b5359f00a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-27T15:22:14.959Z_

Now let me fetch the paper from arXiv and also search for OpenReview comments in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb774a80-d309-42a0-a5a3-53331a286cc2",
  "isSidechain": false,
  "requestId": "req_011CbTJUenfpJgM5XppuHA7F",
  "type": "assistant",
  "uuid": "719f8c2f-c025-4497-a817-f95f359c8980",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GJUqP6N2pPXc5L8LBUwcZ8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 678,
      "cache_read_input_tokens": 13198,
      "output_tokens": 440,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 678,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 440,
          "cache_read_input_tokens": 13198,
          "cache_creation_input_tokens": 678,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 678
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

_source line 11 · 2026-05-27T15:22:16.364Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FQFnVz4hEbg4gGEQK1Cjkr`</summary>

```json
{
  "url": "https://arxiv.org/abs/2305.20050",
  "prompt": "Extract the full abstract, and any information about the paper including authors, submission dates, and version history. Return everything verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "719f8c2f-c025-4497-a817-f95f359c8980",
  "isSidechain": false,
  "requestId": "req_011CbTJUenfpJgM5XppuHA7F",
  "type": "assistant",
  "uuid": "7cb97bc4-7442-40f1-9705-3eb34766a778",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GJUqP6N2pPXc5L8LBUwcZ8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 678,
      "cache_read_input_tokens": 13198,
      "output_tokens": 440,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 678,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 440,
          "cache_read_input_tokens": 13198,
          "cache_creation_input_tokens": 678,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 678
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

_source line 12 · 2026-05-27T15:22:19.182Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RNPyGqqSwPu7wBFTFDtmaE`</summary>

```json
{
  "url": "https://arxiv.org/html/2305.20050",
  "prompt": "Extract the FULL text of this paper. I need: (1) the complete Introduction section, (2) the complete Methods/Approach section, (3) the complete Results/Experiments section, (4) the complete Discussion/Conclusion section, and (5) any Limitations section. Preserve all details about process supervision vs outcome supervision, PRM800K dataset, MATH benchmark results, and training methodology. Be as thorough as possible — do not summarize, extract the actual text."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7cb97bc4-7442-40f1-9705-3eb34766a778",
  "isSidechain": false,
  "requestId": "req_011CbTJUenfpJgM5XppuHA7F",
  "type": "assistant",
  "uuid": "0f4fdb7d-eeca-4ad8-b143-e83b31f8982c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GJUqP6N2pPXc5L8LBUwcZ8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 678,
      "cache_read_input_tokens": 13198,
      "output_tokens": 440,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 678,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 440,
          "cache_read_input_tokens": 13198,
          "cache_creation_input_tokens": 678,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 678
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

_source line 13 · 2026-05-27T15:22:19.191Z_

<details><summary>↩ Tool result · `toolu_01RNPyGqqSwPu7wBFTFDtmaE`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f4fdb7d-eeca-4ad8-b143-e83b31f8982c",
  "isSidechain": false,
  "promptId": "847a487e-d454-4fe9-b1b6-24705f0c37b0",
  "type": "user",
  "uuid": "a23d25f7-e11d-4045-a84a-bafe2f9be863",
  "toolUseResult": {
    "bytes": 0,
    "code": 404,
    "codeText": "Not Found",
    "result": "The server returned HTTP 404 Not Found.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.",
    "durationMs": 6,
    "url": "https://arxiv.org/html/2305.20050"
  },
  "sourceToolAssistantUUID": "0f4fdb7d-eeca-4ad8-b143-e83b31f8982c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-27T15:22:21.315Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01P4YAbPa8zMMyTQs6nj2Kuq`</summary>

```json
{
  "url": "https://openreview.net/forum?id=v8L0pN6EOi",
  "prompt": "Extract ALL reviewer comments, scores, and author responses for this paper \"Let's Verify Step by Step\". I need: (1) each reviewer's summary, (2) their strengths/weaknesses assessment, (3) their scores/ratings, (4) any author rebuttals or responses. Be thorough and complete."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a23d25f7-e11d-4045-a84a-bafe2f9be863",
  "isSidechain": false,
  "requestId": "req_011CbTJUenfpJgM5XppuHA7F",
  "type": "assistant",
  "uuid": "d513cb69-7d78-4783-855a-6bb85f462752",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GJUqP6N2pPXc5L8LBUwcZ8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 678,
      "cache_read_input_tokens": 13198,
      "output_tokens": 440,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 678,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 440,
          "cache_read_input_tokens": 13198,
          "cache_creation_input_tokens": 678,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 678
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

_source line 15 · 2026-05-27T15:22:23.381Z_

<details><summary>↩ Tool result · `toolu_01FQFnVz4hEbg4gGEQK1Cjkr`</summary>

```text
# Paper Information: "Let's Verify Step by Step"

**arXiv ID:** 2305.20050

**Submission Date:** 31 May 2023

**Version History:**
- [v1] Wed, 31 May 2023 17:24:00 UTC (10,363 KB)

**Authors:**
Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, Karl Cobbe

**Subject Classification:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Computation and Language (cs.CL)

**Full Abstract:**

"In recent years, large language models have greatly improved in their ability to perform complex multi-step reasoning. However, even state-of-the-art models still regularly produce logical mistakes. To train more reliable models, we can turn either to outcome supervision, which provides feedback for a final result, or process supervision, which provides feedback for each intermediate reasoning step. Given the importance of training reliable models, and given the high cost of human feedback, it is important to carefully compare the both methods. Recent work has already begun this comparison, but many questions still remain. We conduct our own investigation, finding that process supervision significantly outperforms outcome supervision for training models to solve problems from the challenging MATH dataset. Our process-supervised model solves 78% of problems from a representative subset of the MATH test set. Additionally, we show that active learning significantly improves the efficacy of process supervision. To support related research, we also release PRM800K, the complete dataset of 800,000 step-level human feedback labels used to train our best reward model."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7cb97bc4-7442-40f1-9705-3eb34766a778",
  "isSidechain": false,
  "promptId": "847a487e-d454-4fe9-b1b6-24705f0c37b0",
  "type": "user",
  "uuid": "abc3b930-07a7-4f30-91fa-1db5fe9739ea",
  "toolUseResult": {
    "bytes": 47056,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Information: \"Let's Verify Step by Step\"\n\n**arXiv ID:** 2305.20050\n\n**Submission Date:** 31 May 2023\n\n**Version History:**\n- [v1] Wed, 31 May 2023 17:24:00 UTC (10,363 KB)\n\n**Authors:**\nHunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, Karl Cobbe\n\n**Subject Classification:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Computation and Language (cs.CL)\n\n**Full Abstract:**\n\n\"In recent years, large language models have greatly improved in their ability to perform complex multi-step reasoning. However, even state-of-the-art models still regularly produce logical mistakes. To train more reliable models, we can turn either to outcome supervision, which provides feedback for a final result, or process supervision, which provides feedback for each intermediate reasoning step. Given the importance of training reliable models, and given the high cost of human feedback, it is important to carefully compare the both methods. Recent work has already begun this comparison, but many questions still remain. We conduct our own investigation, finding that process supervision significantly outperforms outcome supervision for training models to solve problems from the challenging MATH dataset. Our process-supervised model solves 78% of problems from a representative subset of the MATH test set. Additionally, we show that active learning significantly improves the efficacy of process supervision. To support related research, we also release PRM800K, the complete dataset of 800,000 step-level human feedback labels used to train our best reward model.\"",
    "durationMs": 7012,
    "url": "https://arxiv.org/abs/2305.20050"
  },
  "sourceToolAssistantUUID": "7cb97bc4-7442-40f1-9705-3eb34766a778",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-27T15:22:24.744Z_

<details><summary>↩ Tool result · `toolu_01P4YAbPa8zMMyTQs6nj2Kuq`</summary>

```text
# Reviewer Comments and Scores - Not Available

Based on the webpage content provided, I cannot extract reviewer comments, scores, or author responses for "Let's Verify Step by Step."

**Why:** The page displays only the paper's metadata and abstract—publication details, author names, and a brief summary stating the work uses "step-level human feedback to build a robust verifier of LLM reasoning that gets 78% accuracy on a subset of the MATH test set."

The actual peer review section containing individual reviewer assessments, ratings, and rebuttals is not included in the provided HTML content. To access this information, you would need to:

1. Visit the full OpenReview page directly at the paper's URL
2. Scroll to the "Reviews" or "Peer Review" section
3. Review individual reviewer reports and any author responses

OpenReview typically displays these elements on the live page, but they were not captured in the text provided here.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d513cb69-7d78-4783-855a-6bb85f462752",
  "isSidechain": false,
  "promptId": "847a487e-d454-4fe9-b1b6-24705f0c37b0",
  "type": "user",
  "uuid": "08b47cc5-ae0f-4c48-964b-d336ca8dd983",
  "toolUseResult": {
    "bytes": 87937,
    "code": 200,
    "codeText": "OK",
    "result": "# Reviewer Comments and Scores - Not Available\n\nBased on the webpage content provided, I cannot extract reviewer comments, scores, or author responses for \"Let's Verify Step by Step.\"\n\n**Why:** The page displays only the paper's metadata and abstract—publication details, author names, and a brief summary stating the work uses \"step-level human feedback to build a robust verifier of LLM reasoning that gets 78% accuracy on a subset of the MATH test set.\"\n\nThe actual peer review section containing individual reviewer assessments, ratings, and rebuttals is not included in the provided HTML content. To access this information, you would need to:\n\n1. Visit the full OpenReview page directly at the paper's URL\n2. Scroll to the \"Reviews\" or \"Peer Review\" section\n3. Review individual reviewer reports and any author responses\n\nOpenReview typically displays these elements on the live page, but they were not captured in the text provided here.",
    "durationMs": 3427,
    "url": "https://openreview.net/forum?id=v8L0pN6EOi"
  },
  "sourceToolAssistantUUID": "d513cb69-7d78-4783-855a-6bb85f462752",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-27T15:22:30.822Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0157Vi131dYwVizydyG4FiyQ`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2305.20050",
  "prompt": "Extract the FULL text of this paper \"Let's Verify Step by Step\". I need ALL sections including: Introduction, Related Work, Methods (process supervision, outcome supervision, data collection, PRM800K), Experiments/Results, Discussion, Conclusion, and Limitations. Capture every technical detail about: how process reward models (PRMs) vs outcome reward models (ORMs) are defined and trained, how step-level labels were collected, the active learning approach, the MATH benchmark evaluation methodology (best-of-N, majority voting), the main results and ablations, and all discussed limitations and future directions. Be maximally thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08b47cc5-ae0f-4c48-964b-d336ca8dd983",
  "isSidechain": false,
  "requestId": "req_011CbTJVYQifh8su5MyN9gZD",
  "type": "assistant",
  "uuid": "9bb4160e-092b-40af-b9c4-9c183f1c67e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nc7kbjJ6mAxKSYqP8f4Evc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1178,
      "cache_read_input_tokens": 13876,
      "output_tokens": 345,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1178,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 345,
          "cache_read_input_tokens": 13876,
          "cache_creation_input_tokens": 1178,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1178
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

_source line 18 · 2026-05-27T15:22:32.041Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SKfV2eD4kmXnDzvKeAY2Lh`</summary>

```json
{
  "url": "https://openreview.net/forum?id=v8L0pN6EOi&noteId=v8L0pN6EOi",
  "prompt": "Extract ALL reviewer comments, ratings, and author responses for this ICLR 2024 paper. I need every review with strengths, weaknesses, questions, scores, and any rebuttals."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9bb4160e-092b-40af-b9c4-9c183f1c67e3",
  "isSidechain": false,
  "requestId": "req_011CbTJVYQifh8su5MyN9gZD",
  "type": "assistant",
  "uuid": "52205278-7023-4564-95b9-2a233e5b31a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nc7kbjJ6mAxKSYqP8f4Evc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1178,
      "cache_read_input_tokens": 13876,
      "output_tokens": 345,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1178,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 345,
          "cache_read_input_tokens": 13876,
          "cache_creation_input_tokens": 1178,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1178
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

_source line 19_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-27 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "52205278-7023-4564-95b9-2a233e5b31a1",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze OpenAI's process reward models paper",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd"
}
```

---

### Tool result

_source line 21 · 2026-05-27T15:22:36.102Z_

<details><summary>↩ Tool result · `toolu_01SKfV2eD4kmXnDzvKeAY2Lh`</summary>

```text
# Review Information Not Available

The webpage content provided contains only the paper's landing page on OpenReview, which displays:

- **Title:** "Let's Verify Step by Step"
- **Authors:** Hunter Lightman, Vineet Kosaraju, Yuri Burda, and others
- **Publication:** ICLR 2024 poster (January 16, 2024)
- **TL;DR:** Research on using "step-level human feedback to build a robust verifier of LLM reasoning that gets 78% accuracy"

**However, the actual peer review comments, ratings, and author responses are not included in this content.** To access reviewer feedback, you would need to:

1. Visit the full OpenReview page directly
2. Look for dedicated "Reviews" or "Comments" sections
3. Check for "Author Responses" or "Rebuttal" tabs

The provided content only shows the paper's abstract and metadata, not the peer review discussion thread that typically appears on OpenReview publication pages.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52205278-7023-4564-95b9-2a233e5b31a1",
  "isSidechain": false,
  "promptId": "847a487e-d454-4fe9-b1b6-24705f0c37b0",
  "type": "user",
  "uuid": "45b7c688-a5aa-471b-b960-fb6cea48c095",
  "toolUseResult": {
    "bytes": 88020,
    "code": 200,
    "codeText": "OK",
    "result": "# Review Information Not Available\n\nThe webpage content provided contains only the paper's landing page on OpenReview, which displays:\n\n- **Title:** \"Let's Verify Step by Step\"\n- **Authors:** Hunter Lightman, Vineet Kosaraju, Yuri Burda, and others\n- **Publication:** ICLR 2024 poster (January 16, 2024)\n- **TL;DR:** Research on using \"step-level human feedback to build a robust verifier of LLM reasoning that gets 78% accuracy\"\n\n**However, the actual peer review comments, ratings, and author responses are not included in this content.** To access reviewer feedback, you would need to:\n\n1. Visit the full OpenReview page directly\n2. Look for dedicated \"Reviews\" or \"Comments\" sections\n3. Check for \"Author Responses\" or \"Rebuttal\" tabs\n\nThe provided content only shows the paper's abstract and metadata, not the peer review discussion thread that typically appears on OpenReview publication pages.",
    "durationMs": 4056,
    "url": "https://openreview.net/forum?id=v8L0pN6EOi&noteId=v8L0pN6EOi"
  },
  "sourceToolAssistantUUID": "52205278-7023-4564-95b9-2a233e5b31a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-27T15:22:44.953Z_

<details><summary>↩ Tool result · `toolu_0157Vi131dYwVizydyG4FiyQ`</summary>

```text
I appreciate your request, but I need to be transparent about what I'm encountering: the content you've provided appears to be a corrupted or heavily compressed PDF file (indicated by the `%PDF-1.5` header and compressed stream data), not readable text.

I cannot extract meaningful content from this compressed binary format. To help you effectively, I would need:

1. **A readable text version** of the paper (plain text, properly formatted PDF, or HTML)
2. **The paper title and authors** so I can reference it correctly
3. **A direct link** to the published paper if available

**What I can tell you:** Based on your description, you're asking for a comprehensive extraction of "Let's Verify Step by Step" — a paper about process reward models (PRMs) versus outcome reward models (ORMs), likely including the PRM800K dataset and MATH benchmark evaluation.

**My recommendation:** 
- Try downloading the paper from arXiv or the publisher's site in a readable format
- Use a PDF text extraction tool first
- Then share the readable text, and I'll provide the thorough technical summary you've requested while respecting the 125-character quote limit and proper attribution

I'm happy to help once I can access the actual content!

[Binary content (application/pdf, 4.2MB) also saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/2d2f5f70-a94f-402d-8c92-8c562e7598cd/tool-results/webfetch-1779895350860-g4dtxd.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9bb4160e-092b-40af-b9c4-9c183f1c67e3",
  "isSidechain": false,
  "promptId": "847a487e-d454-4fe9-b1b6-24705f0c37b0",
  "type": "user",
  "uuid": "09836266-6c23-4d54-b375-f3371520a1da",
  "toolUseResult": {
    "bytes": 4384742,
    "code": 200,
    "codeText": "OK",
    "result": "I appreciate your request, but I need to be transparent about what I'm encountering: the content you've provided appears to be a corrupted or heavily compressed PDF file (indicated by the `%PDF-1.5` header and compressed stream data), not readable text.\n\nI cannot extract meaningful content from this compressed binary format. To help you effectively, I would need:\n\n1. **A readable text version** of the paper (plain text, properly formatted PDF, or HTML)\n2. **The paper title and authors** so I can reference it correctly\n3. **A direct link** to the published paper if available\n\n**What I can tell you:** Based on your description, you're asking for a comprehensive extraction of \"Let's Verify Step by Step\" — a paper about process reward models (PRMs) versus outcome reward models (ORMs), likely including the PRM800K dataset and MATH benchmark evaluation.\n\n**My recommendation:** \n- Try downloading the paper from arXiv or the publisher's site in a readable format\n- Use a PDF text extraction tool first\n- Then share the readable text, and I'll provide the thorough technical summary you've requested while respecting the 125-character quote limit and proper attribution\n\nI'm happy to help once I can access the actual content!\n\n[Binary content (application/pdf, 4.2MB) also saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/2d2f5f70-a94f-402d-8c92-8c562e7598cd/tool-results/webfetch-1779895350860-g4dtxd.pdf]",
    "durationMs": 14127,
    "url": "https://arxiv.org/pdf/2305.20050"
  },
  "sourceToolAssistantUUID": "9bb4160e-092b-40af-b9c4-9c183f1c67e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-27T15:22:48.264Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0159FKXUdWRWca5nqYSXLJzC`</summary>

```json
{
  "url": "https://openreview.net/notes?forum=v8L0pN6EOi",
  "prompt": "Extract ALL reviewer comments, ratings, strengths, weaknesses, questions, and author responses for the paper \"Let's Verify Step by Step\" at ICLR 2024."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09836266-6c23-4d54-b375-f3371520a1da",
  "isSidechain": false,
  "requestId": "req_011CbTJX2pJ4JCJZG4RUy491",
  "type": "assistant",
  "uuid": "2802d131-ec7f-4632-8c88-602d71741a63",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NiFq1R6BHiU2kYhQ5svrsL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 259,
      "cache_creation_input_tokens": 740,
      "cache_read_input_tokens": 15054,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 740,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 259,
          "output_tokens": 227,
          "cache_read_input_tokens": 15054,
          "cache_creation_input_tokens": 740,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 740
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

_source line 24 · 2026-05-27T15:22:48.425Z_

<details><summary>↩ Tool result · `toolu_0159FKXUdWRWca5nqYSXLJzC`</summary>

```text
The server returned HTTP 400 Bad Request.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2802d131-ec7f-4632-8c88-602d71741a63",
  "isSidechain": false,
  "promptId": "847a487e-d454-4fe9-b1b6-24705f0c37b0",
  "type": "user",
  "uuid": "ce55702f-230d-41bd-99e1-6368361ff113",
  "toolUseResult": {
    "bytes": 0,
    "code": 400,
    "codeText": "Bad Request",
    "result": "The server returned HTTP 400 Bad Request.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.",
    "durationMs": 158,
    "url": "https://openreview.net/notes?forum=v8L0pN6EOi"
  },
  "sourceToolAssistantUUID": "2802d131-ec7f-4632-8c88-602d71741a63",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-27T15:22:49.424Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013TtUKGCYNmgDrVhKrDXSjt`</summary>

```json
{
  "url": "https://api.openreview.net/notes?forum=v8L0pN6EOi",
  "prompt": "Extract ALL review data including reviewer comments, scores, strengths, weaknesses, questions, and author responses. Return everything you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce55702f-230d-41bd-99e1-6368361ff113",
  "isSidechain": false,
  "requestId": "req_011CbTJX2pJ4JCJZG4RUy491",
  "type": "assistant",
  "uuid": "f08984df-0cd2-4f15-ba59-43c681b24953",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NiFq1R6BHiU2kYhQ5svrsL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 259,
      "cache_creation_input_tokens": 740,
      "cache_read_input_tokens": 15054,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 740,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 259,
          "output_tokens": 227,
          "cache_read_input_tokens": 15054,
          "cache_creation_input_tokens": 740,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 740
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

_source line 26 · 2026-05-27T15:22:51.363Z_

<details><summary>↩ Tool result · `toolu_013TtUKGCYNmgDrVhKrDXSjt`</summary>

```text
# Review Data Extraction Result

Based on the provided web page content, there is **no review data to extract**. The JSON response indicates:

- **Notes**: Empty array (no entries)
- **Count**: 0 (no records present)

The page contains no reviewer comments, scores, strengths, weaknesses, questions, or author responses to analyze or report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f08984df-0cd2-4f15-ba59-43c681b24953",
  "isSidechain": false,
  "promptId": "847a487e-d454-4fe9-b1b6-24705f0c37b0",
  "type": "user",
  "uuid": "cc0e311c-57d9-4c17-b0e8-fe9e217a1a92",
  "toolUseResult": {
    "bytes": 22,
    "code": 200,
    "codeText": "OK",
    "result": "# Review Data Extraction Result\n\nBased on the provided web page content, there is **no review data to extract**. The JSON response indicates:\n\n- **Notes**: Empty array (no entries)\n- **Count**: 0 (no records present)\n\nThe page contains no reviewer comments, scores, strengths, weaknesses, questions, or author responses to analyze or report.",
    "durationMs": 1936,
    "url": "https://api.openreview.net/notes?forum=v8L0pN6EOi"
  },
  "sourceToolAssistantUUID": "f08984df-0cd2-4f15-ba59-43c681b24953",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-27T15:22:54.353Z_

<details><summary>Logged reasoning block</summary>

```text
Let me try a different approach to get the OpenReview reviews and also try to get the paper content from a different source.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc0e311c-57d9-4c17-b0e8-fe9e217a1a92",
  "isSidechain": false,
  "requestId": "req_011CbTJXWC5Tg2PwTtDAubuE",
  "type": "assistant",
  "uuid": "b41242ff-9b5d-429a-81b7-c861bedf15cf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012MN5XAV7YG99VG4vhtcXeL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 15794,
      "output_tokens": 416,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 679,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 416,
          "cache_read_input_tokens": 15794,
          "cache_creation_input_tokens": 679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 679
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

_source line 28 · 2026-05-27T15:22:54.923Z_

Let me try the OpenReview API with the correct parameters and also get the paper content from an alternative source.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b41242ff-9b5d-429a-81b7-c861bedf15cf",
  "isSidechain": false,
  "requestId": "req_011CbTJXWC5Tg2PwTtDAubuE",
  "type": "assistant",
  "uuid": "0fc12413-2422-40ea-8ef3-0cb265121866",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012MN5XAV7YG99VG4vhtcXeL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 15794,
      "output_tokens": 416,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 679,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 416,
          "cache_read_input_tokens": 15794,
          "cache_creation_input_tokens": 679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 679
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

_source line 29 · 2026-05-27T15:22:56.792Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JuJ8rg7kn8XdH9jpxBrX7b`</summary>

```json
{
  "url": "https://api.openreview.net/notes?forum=v8L0pN6EOi&details=replyCount,writable,revisions,original,overwriting,invitation,tags,directReplies",
  "prompt": "Extract ALL review data. Look for any notes that are reviews, including reviewer comments, scores, strengths, weaknesses, and author responses. Return everything."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0fc12413-2422-40ea-8ef3-0cb265121866",
  "isSidechain": false,
  "requestId": "req_011CbTJXWC5Tg2PwTtDAubuE",
  "type": "assistant",
  "uuid": "d1469b36-4236-4e2f-b48c-2a8d2cdddc8d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012MN5XAV7YG99VG4vhtcXeL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 15794,
      "output_tokens": 416,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 679,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 416,
          "cache_read_input_tokens": 15794,
          "cache_creation_input_tokens": 679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 679
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

_source line 30 · 2026-05-27T15:22:58.584Z_

<details><summary>↩ Tool result · `toolu_01JuJ8rg7kn8XdH9jpxBrX7b`</summary>

```text
# Review Data Extraction Results

Based on the provided web page content, there is **no review data to extract**.

The JSON response shows:
- Empty notes array: `[]`
- Count of zero: `0`
- Data retrieved from cache

The page contains no reviewer comments, scores, strengths, weaknesses, author responses, or any other review-related information.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1469b36-4236-4e2f-b48c-2a8d2cdddc8d",
  "isSidechain": false,
  "promptId": "847a487e-d454-4fe9-b1b6-24705f0c37b0",
  "type": "user",
  "uuid": "4bf72028-b834-4ccd-a38f-aed043bf1744",
  "toolUseResult": {
    "bytes": 39,
    "code": 200,
    "codeText": "OK",
    "result": "# Review Data Extraction Results\n\nBased on the provided web page content, there is **no review data to extract**.\n\nThe JSON response shows:\n- Empty notes array: `[]`\n- Count of zero: `0`\n- Data retrieved from cache\n\nThe page contains no reviewer comments, scores, strengths, weaknesses, author responses, or any other review-related information.",
    "durationMs": 1789,
    "url": "https://api.openreview.net/notes?forum=v8L0pN6EOi&details=replyCount,writable,revisions,original,overwriting,invitation,tags,directReplies"
  },
  "sourceToolAssistantUUID": "d1469b36-4236-4e2f-b48c-2a8d2cdddc8d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-27T15:22:58.681Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01M6kSTMTsvWpw4teapFsD9D`</summary>

```json
{
  "url": "https://api.openreview.net/notes/search?query=Let%27s+Verify+Step+by+Step&source=forum&limit=50",
  "prompt": "Find the OpenReview forum ID and all associated review notes for the paper \"Let's Verify Step by Step\"."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bf72028-b834-4ccd-a38f-aed043bf1744",
  "isSidechain": false,
  "requestId": "req_011CbTJXWC5Tg2PwTtDAubuE",
  "type": "assistant",
  "uuid": "6163e674-cbb5-4625-bd92-8870757224db",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012MN5XAV7YG99VG4vhtcXeL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 15794,
      "output_tokens": 416,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 679,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 416,
          "cache_read_input_tokens": 15794,
          "cache_creation_input_tokens": 679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 679
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

_source line 32 · 2026-05-27T15:22:59.464Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01E4nuwrRycqiA7GsnaaPNGX`</summary>

```json
{
  "url": "https://huggingface.co/papers/2305.20050",
  "prompt": "Extract any discussion, summary, or analysis of the paper \"Let's Verify Step by Step\" available on this page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6163e674-cbb5-4625-bd92-8870757224db",
  "isSidechain": false,
  "requestId": "req_011CbTJXWC5Tg2PwTtDAubuE",
  "type": "assistant",
  "uuid": "95c45704-4556-46ba-839c-f48aa3dc6e7b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012MN5XAV7YG99VG4vhtcXeL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 15794,
      "output_tokens": 416,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 679,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 416,
          "cache_read_input_tokens": 15794,
          "cache_creation_input_tokens": 679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 679
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

_source line 33 · 2026-05-27T15:23:00.225Z_

<details><summary>↩ Tool result · `toolu_01E4nuwrRycqiA7GsnaaPNGX`</summary>

```text
&lt;persisted-output>
Output too large (78.6KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/2d2f5f70-a94f-402d-8c92-8c562e7598cd/tool-results/toolu_01E4nuwrRycqiA7GsnaaPNGX.txt

Preview (first 2KB):
# Let’s Verify Step by Step

Hunter Lightman\*    Vineet Kosaraju\*    Yura Burda\*    Harri Edwards  
 Bowen Baker    Teddy Lee    Jan Leike    John Schulman    Ilya Sutskever  
 Karl Cobbe\*  
 OpenAI

## Abstract

In recent years, large language models have greatly improved in their ability to perform complex multi-step reasoning. However, even state-of-the-art models still regularly produce logical mistakes. To train more reliable models, we can turn either to outcome supervision, which provides feedback for a final result, or process supervision, which provides feedback for each intermediate reasoning step. Given the importance of training reliable models, and given the high cost of human feedback, it is important to carefully compare the both methods. Recent work has already begun this comparison, but many questions still remain. We conduct our own investigation, finding that process supervision significantly outperforms outcome supervision for training models to solve problems from the challenging MATH dataset. Our process-supervised model solves 78% of problems from a representative subset of the MATH test set. Additionally, we show that active learning significantly improves the efficacy of process supervision. To support related research, we also release PRM800K, the complete dataset of 800,000 step-level human feedback labels used to train our best reward model.

## 1 Introduction

...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "95c45704-4556-46ba-839c-f48aa3dc6e7b",
  "isSidechain": false,
  "promptId": "847a487e-d454-4fe9-b1b6-24705f0c37b0",
  "type": "user",
  "uuid": "8cd701de-3f6c-4d41-b395-fa538fe274bd",
  "toolUseResult": {
    "bytes": 80520,
    "code": 200,
    "codeText": "OK",
    "result": "# Let’s Verify Step by Step\n\nHunter Lightman\\*    Vineet Kosaraju\\*    Yura Burda\\*    Harri Edwards  \n Bowen Baker    Teddy Lee    Jan Leike    John Schulman    Ilya Sutskever  \n Karl Cobbe\\*  \n OpenAI\n\n## Abstract\n\nIn recent years, large language models have greatly improved in their ability to perform complex multi-step reasoning. However, even state-of-the-art models still regularly produce logical mistakes. To train more reliable models, we can turn either to outcome supervision, which provides feedback for a final result, or process supervision, which provides feedback for each intermediate reasoning step. Given the importance of training reliable models, and given the high cost of human feedback, it is important to carefully compare the both methods. Recent work has already begun this comparison, but many questions still remain. We conduct our own investigation, finding that process supervision significantly outperforms outcome supervision for training models to solve problems from the challenging MATH dataset. Our process-supervised model solves 78% of problems from a representative subset of the MATH test set. Additionally, we show that active learning significantly improves the efficacy of process supervision. To support related research, we also release PRM800K, the complete dataset of 800,000 step-level human feedback labels used to train our best reward model.\n\n## 1 Introduction\n\nLarge language models are capable of solving tasks that require complex multi-step reasoning by generating solutions in a step-by-step chain-of-thought format (Nye et al., 2021; Wei et al., 2022; Kojima et al., 2022). However, even state-of-the-art models are prone to producing falsehoods — they exhibit a tendency to invent facts in moments of uncertainty (Bubeck et al., 2023). These *hallucinations* (Maynez et al., 2020) are particularly problematic in domains that require multi-step reasoning, since a single logical error is enough to derail a much larger solution. Detecting and mitigating hallucinations is essential to improve reasoning capabilities.\n\n---\n\n\\*Primary authors. Correspondence to: Karl Cobbe &lt;karl@openai.com>One effective method involves training reward models to discriminate between desirable and undesirable outputs. The reward model can then be used in a reinforcement learning pipeline (Ziegler et al., 2019; Stiennon et al., 2020; Nakano et al., 2021; Ouyang et al., 2022) or to perform search via rejection sampling (Nichols et al., 2020; Shen et al., 2021; Cobbe et al., 2021). While these techniques are useful, the resulting system is only as reliable as the reward model itself. It is therefore important that we study how to most effectively train reliable reward models.\n\nIn closely related work, Uesato et al. (2022) describe two distinct methods for training reward models: outcome supervision and process supervision. Outcome-supervised reward models (ORMs) are trained using only the final result of the model’s chain-of-thought, while process-supervised reward models (PRMs) receive feedback for each step in the chain-of-thought. There are compelling reasons to favor process supervision. It provides more precise feedback, since it specifies the exact location of any errors that occur. It also has several advantages relevant to AI alignment: it is easier for humans to interpret, and it more directly rewards models for following a human-endorsed chain-of-thought. Within the domain of logical reasoning, models trained with outcome supervision regularly use incorrect reasoning to reach the correct final answer (Zelikman et al., 2022; Creswell et al., 2022). Process supervision has been shown to mitigate this misaligned behavior (Uesato et al., 2022).\n\nDespite these advantages, Uesato et al. (2022) found that outcome supervision and process supervision led to similar final performance in the domain of grade school math. We conduct our own detailed comparison of outcome and process supervision, with three main differences: we use a more capable base model, we use significantly more human feedback, and we train and test on the more challenging MATH dataset (Hendrycks et al., 2021).\n\nOur main contributions are as follows:\n\n1. 1. We show that process supervision can train much more reliable reward models than outcome supervision. We use our state-of-the-art PRM to solve 78.2% of problems from a representative subset of the MATH test set.\n2. 2. We show that a large reward model can reliably approximate human supervision for smaller reward models, and that it can be used to efficiently conduct large-scale data collection ablations.\n3. 3. We show that active learning leads to a  $2.6\\times$  improvement in the data efficiency of process supervision.\n4. 4. We release our full process supervision dataset, PRM800K, to promote related research.## 2 Methods\n\nWe perform a comparison of outcome and process supervision, following a similar methodology to Uesato et al. (2022). Outcome supervision can be provided without humans, since all problems in the MATH dataset have automatically checkable answers. In contrast, there is no simple way to automate process supervision. We therefore rely on human data-labelers to provide process supervision, specifically by labelling the correctness of each step in model-generated solutions.\n\nWe conduct experiments in two separate regimes: large-scale and small-scale. Each has its own advantages, and they offer complimentary perspectives. At large-scale, we finetune all models from GPT-4 (OpenAI, 2023). We focus on advancing the state-of-the-art by training the most reliable ORM and PRM possible. Unfortunately the training sets for these reward models are not directly comparable, for reasons we will discuss in Section 3. These models are therefore not ideal for making an apples-to-apples comparison of outcome and process supervision. To address this flaw, we also train models at small-scale, where we can conduct a more direct comparison. In order to remove our dependence on costly human feedback, we use a large-scale model to supervise small-scale model training. This setup enables us to conduct several important ablations that would otherwise be infeasible.\n\n### 2.1 Scope\n\nAt each model scale, we use a single fixed model to generate all solutions. We call this model the *generator*. We do not attempt to improve the generator with reinforcement learning (RL). When we discuss outcome and process supervision, we are specifically referring to the supervision given to the reward model. We do not discuss any supervision the generator would receive from the reward model if trained with RL. Although finetuning the generator with RL is a natural next step, it is intentionally not the focus of this work.\n\nWe instead focus exclusively on how to train the most reliable reward model possible. We evaluate a reward model by its ability to perform best-of-N search over uniformly sampled solutions from the generator. For each test problem we select the solution ranked highest by the reward model, automatically grade it based on its final answer, and report the fraction that are correct. A reward model that is more reliable will select the correct solution more often.\n\n### 2.2 Base Models\n\nAll large-scale models are finetuned from the base GPT-4 model (OpenAI, 2023). This model has been pretrained solely to predict the next token; it has not been pretrained with any Reinforcement Learning from Human Feedback (RLHF) (Christiano et al., 2017). The small-scale base models are similar in design to GPT-4, but they were pretrained with roughly 200 times less compute. As an additional pretraining step, we finetune all models on a dataset of roughly 1.5BThe denominator of a fraction is 7 less than 3 times the numerator. If the fraction is equivalent to  $2/5$ , what is the numerator of the fraction? (Answer: )\n\n😞 😊 😊 Let's call the numerator  $x$ .\n\n😞 😊 😊 So the denominator is  $3x-7$ .\n\n😞 😊 😊 We know that  $x/(3x-7) = 2/5$ .\n\n😞 😊 😊 So  $5x = 2(3x-7)$ .\n\n😞 😊 😊  $5x = 6x - 14$ .\n\n😞 😊 😊 So  $x = 7$ .\n\nFigure 1: A screenshot of the interface used to collect feedback for each step in a solution.\n\nmath-relevant tokens, which we call MathMix. Similar to Lewkowycz et al. (2022), we find that this improves the model’s mathematical reasoning capabilities. Details on how this dataset was constructed can be found in Appendix A.\n\n## 2.3 Generator\n\nTo make parsing individual steps easier, we train the generator to produce solutions in a newline delimited step-by-step format. Specifically, we few-shot generate solutions to MATH training problems, filter to those that reach the correct final answer, and finetune the base model on this dataset for a single epoch. This step is not intended to teach the generator new skills; it is intended only to teach the generator to produce solutions in the desired format.\n\n## 2.4 Data Collection\n\nTo collect process supervision data, we present human data-labelers with step-by-step solutions to MATH problems sampled by the large-scale generator. Their task is to assign each step in the solution a label of *positive*, *negative*, or *neutral*, as shown in Figure 1. A positive label indicates that the step is correct and reasonable. A negative label indicates that the step is either incorrect or unreasonable. A neutral label indicates ambiguity. In practice, a step may be labelled neutral if it is subtly misleading, or if it is a poor suggestion that is technically still valid. We permit neutral labels since this allows us to defer the decision about how to handle ambiguity: at test time, we can treat neutral labels as either positive or negative. A more detailed description of the labelling instructions is provided in Appendix D.\n\nWe label solutions exclusively from the large-scale generator in order to maximize the value of our limited human-data resource. We refer to the entire dataset of step-level labels collected as PRM800K. The PRM800K training set contains 800K step-level labels across 75K solutions to 12K problems. Tominimize overfitting, we include data from 4.5K MATH test problems in the PRM800K training set, and we therefore evaluate our models only on the remaining 500 MATH test problems. More details about this test set can be found in Appendix C.\n\nDuring data collection, we must decide which solutions to surface to data-labelers. The most straightforward strategy is to uniformly surface solutions produced by the generator. However, if we surface solutions that make obvious errors, the human feedback we get is less valuable. We would prefer to surface solutions that are more likely to fool our best reward model. To that end, we attempt to strategically select which solutions to show data-labelers. Specifically, we choose to surface *convincing wrong-answer* solutions. We use the term *convincing* to refer to solutions that are rated highly by our current best PRM, and we use *wrong-answer* to refer to solutions that reach an incorrect final answer. We use this slightly verbose phrasing to emphasize the fact that correctness is determined solely by checking the final answer, a process which occasionally leads to misgraded solutions. We expect to gain more information from labeling convincing wrong-answer solutions, since we know the PRM is mistaken about at least one step in each such solution.\n\nIn addition to using this selection strategy, we also iteratively re-train our PRM using the latest data at several points in the data collection process. At each iteration, we generate  $N$  solutions per problem and surface only the top  $K$  most convincing wrong-answer solutions to data-labelers. We experiment with either applying this top- $K$  filtering at a problem level ( $K$  solutions per problem) or globally across the dataset ( $K$  solutions in total, unequally distributed among problems). Since the data collection process is expensive, it was not feasible to conduct at-scale ablations of these decisions. However, we perform several surrogate ablations in Section 4, using our largest PRM as a labelling oracle for a smaller PRM. More details about data collection can be found in Appendix B.\n\n## 2.5 Outcome-supervised Reward Models (ORMs)\n\nWe train ORMs following a similar methodology to Cobbe et al. (2021). We uniformly sample a fixed number of solutions per problem from the generator, and we train the ORM to predict whether each solution is correct or incorrect. In practice, we usually determine correctness by automatically checking the final answer, but in principle these labels could be provided by humans. At test time, we use the ORM’s prediction at the final token as the overall score for the solution. We note the automatic grading used to determine ORM targets is not perfectly reliable: *false positives* solutions that reach the correct answer with incorrect reasoning will be misgraded. We discuss additional ORM training details in Appendix E.\n\n## 2.6 Process-supervised Reward Models (PRMs)\n\nWe train PRMs to predict the correctness of each step after the last token in each step. This prediction takes the form of a single token, and we maximize theLet  $x^8 + 3x^4 - 4 = p_1(x)p_2(x) \\cdots p_k(x)$ , where each non-constant polynomial  $p_i(x)$  is monic with integer coefficients, and cannot be factored further over the integers. Compute  $p_1(1) + p_2(1) + \\cdots + p_k(1)$ .\n\nI notice that the given polynomial has even degree and only even powers of  $x$ , so I can try to make a substitution to simplify it.\n\nLet  $y = x^4$ , then the polynomial becomes  $y^2 + 3y - 4$ , which is a quadratic equation.\n\nI can factor this quadratic equation as  $(y + 4)(y - 1)$ , so the original polynomial is  $(x^4 + 4)(x^4 - 1)$ .\n\nNow I need to factor each of these factors further, if possible, over the integers.\n\nFor the first factor,  $x^4 + 4$ , I recall the Sophie Germain identity, which says that  $a^4 + 4b^4 = (a^2 + 2b^2 + 2ab)(a^2 + 2b^2 - 2ab)$ .\n\nApplying this identity with  $a = x$  and  $b = 1$ , I get  $x^4 + 4 = (x^2 + 2x + 2)(x^2 - 2x + 2)$ .\n\nFor the second factor,  $x^4 - 1$ , I can use the difference of squares formula, which says that  $a^2 - b^2 = (a + b)(a - b)$ .\n\nApplying this formula with  $a = x^2$  and  $b = 1$ , I get  $x^4 - 1 = (x^2 + 1)(x^2 - 1)$ .\n\nThen I can apply the difference of squares formula again with  $a = x$  and  $b = 1$ , to get  $x^2 - 1 = (x + 1)(x - 1)$ .\n\nSo the original polynomial is  $(x^4 + 4)(x^4 - 1) = (x^2 + 2x + 2)(x^2 - 2x + 2)(x^2 + 1)(x + 1)(x - 1)$ .\n\nThese are all the irreducible factors over the integers, so  $p_1(x) = x^2 + 2x + 2$ ,  $p_2(x) = x^2 - 2x + 2$ ,  $p_3(x) = x^2 + 1$ ,  $p_4(x) = x + 1$ , and  $p_5(x) = x - 1$ .\n\nTo find the sum of their values at  $x = 1$ , I just need to plug in  $x = 1$  into each factor and add them up.\n\nI get  $p_1(1) = 1^2 + 2 \\cdot 1 + 2 = 5$ ,  $p_2(1) = 1^2 - 2 \\cdot 1 + 2 = 1$ ,  $p_3(1) = 1^2 + 1 = 2$ ,  $p_4(1) = 1 + 1 = 2$ , and  $p_5(1) = 1 - 1 = 0$ .\n\nSo the final answer is  $5 + 1 + 2 + 2 + 0 = 10$ .\n\nAnswer: 10\n\nLet  $x^8 + 3x^4 - 4 = p_1(x)p_2(x) \\cdots p_k(x)$ , where each non-constant polynomial  $p_i(x)$  is monic with integer coefficients, and cannot be factored further over the integers. Compute  $p_1(1) + p_2(1) + \\cdots + p_k(1)$ .\n\nThis problem is about factoring a polynomial over the integers, which can be a tricky task.\n\nOne possible strategy is to look for rational roots of the polynomial, using the rational root theorem.\n\nHowever, that would involve checking a lot of possible factors of  $-4$ , and there is no guarantee that the polynomial has any rational roots at all.\n\nAnother possible strategy is to use some algebraic tricks to simplify the polynomial or reduce its degree.\n\nI notice that the polynomial has only even powers of  $x$ , so I can try to substitute  $y = x^2$  and see what happens.\n\nThen the polynomial becomes  $y^4 + 3y^2 - 4$ , which is a quadratic equation in  $y^2$ .\n\nI can try to factor this quadratic equation by looking for two numbers that multiply to  $-4$  and add to  $3$ .\n\nThose numbers are  $4$  and  $-1$ , so I can write  $y^4 + 3y^2 - 4 = (y^2 + 4)(y^2 - 1)$ .\n\nNow I can substitute back  $x^2 = y$  and get  $x^8 + 3x^4 - 4 = (x^4 + 4)(x^4 - 1)$ .\n\nThis looks promising, because I have reduced the degree of the factors from  $8$  to  $4$ .\n\nI can try to factor each of these factors further, using the difference of squares formula.\n\nI get  $x^8 + 3x^4 - 4 = (x^4 + 4)(x^2 - 2)(x^2 + 1)(x^2 - 1)$ .\n\nI can apply the difference of squares formula again to the last factor and get  $x^8 + 3x^4 - 4 = (x^4 + 4)(x^2 - 2)(x^2 + 1)(x + 1)(x - 1)$ .\n\nNow I have factored the polynomial completely into monic linear and quadratic factors with integer coefficients.\n\nThese are the  $p_i(x)$ 's that the problem is asking for.\n\nTo find the sum of their values at  $x = 1$ , I just need to plug in  $x = 1$  into each factor and add them up.\n\nI get  $p_1(1) + p_2(1) + \\cdots + p_5(1) = (1^4 + 4)(1^2 - 2)(1^2 + 1)(1 + 1)(1 - 1)$ .\n\nSimplifying, I get  $p_1(1) + p_2(1) + \\cdots + p_5(1) = (5)(-1)(2)(2)(0)$ .\n\nMultiplying, I get  $p_1(1) + p_2(1) + \\cdots + p_5(1) = 0$ .\n\nAnswer: 0\n\nFigure 2: Two solutions to the same problem, graded by the PRM. The solution on the left is correct while the solution on the right is incorrect. A green background indicates a high PRM score, and a red background indicates a low score. The PRM correctly identifies the mistake in the incorrect solution.\n\nlog-likelihood of these target tokens during training. The PRM can therefore be trained in a standard language model pipeline without any special accommodations. To determine the step-level predictions at test time, it suffices to perform a single PRM forward pass over the whole solution. We visualize large-scale PRM scores for two different solutions in Figure 2. To compare multiple solutions, it is necessary to compute a single score for each solution. This is an important but straightforward detail: we define the PRM score for a solution to be the probability that every step is correct under the PRM. We implement this as the product of the correctness probabilities for each step. We describe other possible scoring strategies and additional PRM training details in Appendix F.\n\nWhen we provide process supervision, we deliberately choose to supervise only up to the first incorrect step. This makes the comparison between outcome and process supervision more straightforward. For correct solutions, both methods provide the same information, namely that every step is correct. For incorrect solutions, both methods reveal the existence of at least one mistake, and process supervision additionally reveals the precise location of that mistake. If we were to provide additional process supervision beyond the first mistake, then process supervision would have an even greater information advantage. This decision also keeps the labelling cost similar for humans: without relying on an easy-to-check final answer, determining the correctness of a solution is equivalent to identifying its first mistake. While most MATH problems do have easy-to-check final answers, we expect this to not remain true in more complex domains.&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>&lt;/th>\n&lt;th>ORM&lt;/th>\n&lt;th>PRM&lt;/th>\n&lt;th>Majority Voting&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>% Solved (Best-of-1860)&lt;/td>\n&lt;td>72.4&lt;/td>\n&lt;td>&lt;b>78.2&lt;/b>&lt;/td>\n&lt;td>69.6&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nFigure 3: A comparison of outcome-supervised and process-supervised reward models, evaluated by their ability to search over many test solutions. Majority voting is shown as a strong baseline. For  $N \\leq 1000$ , we visualize the variance across many subsamples of the 1860 solutions we generated in total per problem.\n\n### 3 Large-scale Supervision\n\nWe train the large-scale PRM using the step-level labels in PRM800K. To ensure the large-scale ORM baseline is as strong as possible, we train on 100 uniform samples per problem from the generator. This means the ORM training set has no overlap with PRM800K, and it is an order of magnitude larger. Although these two training sets are not directly comparable, each represents our best attempt to advance the state-of-the-art with each form of supervision. We note that training the ORM solely on PRM800K solutions would be problematic, since our active learning strategy has heavily biased the dataset towards wrong-answer solutions. We did explore training the ORM on a superset of PRM800K solutions, by mixing in uniformly sampled solutions, but we found that this did not improve ORM performance.\n\nFigure 3 shows how the best-of-N performance of each reward model varies as a function of N. Since majority voting is known to be a strong baseline (Wang et al., 2022; Lewkowycz et al., 2022), we also include this method as a point of comparison. While the ORM performs slightly better than the majority voting baseline, the PRM strongly outperforms both. Not only does the PRM reach higher performance for all values of N, but the performance gap widens as N increases. This indicates that the PRM is more effective than both the ORM and majority voting at searching over a large number of model-generated solutions.(a) Four series of reward models trained using different data collection strategies, compared across training sets of varying sizes.\n\n(b) Three reward models trained on 200 samples/problem using different forms of supervision, compared across many test-time compute budgets.\n\nFigure 4: A comparison of different forms of outcome and process supervision. Mean and standard deviation is shown across three seeds.\n\nWe experimented with using RM-weighted voting (Li et al., 2022; Uesato et al., 2022) to combine the benefits of the PRM and majority voting, but this did not noticeably improve performance. We use a specific subset of the MATH test set for evaluation, which we describe in Appendix C. We further break down these results by problem difficulty in Appendix G.\n\n## 4 Small-scale Synthetic Supervision\n\nWe find that the PRM outperforms the ORM at large-scale, but this result alone paints an incomplete picture. To better compare outcome and process supervision, there are two confounding factors that must be isolated. First, the training sets for the ORM and the PRM are not directly comparable: the PRM training set was constructed using active learning, is biased towards answer-incorrect solutions, and is an order of magnitude smaller. Second, the final-answer grading will provide positive labels to spurious solutions that reach the correct final answer despite incorrect reasoning. This could damage ORM performance, an effect we may or may not want to attribute to outcome supervision more generally.\n\nDue to the high cost of collecting human feedback, we cannot easily ablate these factors using human labelers. We instead perform the relevant ablations by using the large-scale PRM to supervise smaller models. This setup enables us to simulate a large amount of data collection at a modest cost. For the remainder of this section, we refer to the large-scale PRM from Section 3 as PRM&lt;sub>large&lt;/sub>.## 4.1 Process vs Outcome Supervision\n\nWe now conduct a direct comparison of outcome and process supervision. We first sample between 1 and 200 solutions per problem from a small-scale generator. For each dataset, we provide three forms of supervision: process supervision from  $\\text{PRM}_{\\text{large}}$ , outcome supervision from  $\\text{PRM}_{\\text{large}}$ , and outcome supervision from final-answer checking. The choice of supervision is the only difference between these three series of reward models, which are otherwise trained on identical datasets. See Appendix H for more details about how  $\\text{PRM}_{\\text{large}}$  is used for outcome and process supervision.\n\nIn Figure 4a, we evaluate each reward model by its best-of-500 selection. We see that process supervision significantly outperforms both forms of outcome supervision at all data collection scales. In Figure 4b, we evaluate the best reward model from each series by its best-of-N performance across different values of N. We see that using  $\\text{PRM}_{\\text{large}}$  for outcome supervision is noticeably more effective than final-answer checking. This can be explained by the fact that  $\\text{PRM}_{\\text{large}}$  provides better supervision for solutions that reach the correct final answer using incorrect reasoning.\n\nIt is not clear whether supervision by  $\\text{PRM}_{\\text{large}}$  or by final-answer checking represents the more appropriate outcome supervision baseline. While final-answer supervision is more explicitly outcome based, its main weakness — the existence of false positives — is arguably over-emphasized in the MATH dataset. Outcome supervision by  $\\text{PRM}_{\\text{large}}$  better represents outcome supervision in domains that are less susceptible to false positives. We consider outcome supervision by  $\\text{PRM}_{\\text{large}}$  to be the more relevant baseline, but we encourage the reader to draw their own conclusions.\n\n## 4.2 Active Learning\n\nFinally, we investigate the impact of active learning. We train a small-scale reward model,  $\\text{PRM}_{\\text{selector}}$ , on a single sample from each problem, and we use this model to score 1000 samples per problem. To train each of our larger reward models, we select  $N$  samples per problem such that 80% are the most convincing (according to  $\\text{PRM}_{\\text{selector}}$ ) wrong-answer samples, and 20% are the most convincing samples that remain (right- or wrong-answer). We score the selected samples with  $\\text{PRM}_{\\text{large}}$  and train on those scores. This process ensures that all samples are relatively convincing under  $\\text{PRM}_{\\text{selector}}$ , that a large fraction are known to contain at least one mistake, and that our overall dataset is not too heavily biased toward wrong-answer solutions. Performance of this data labelling scheme is shown in Figure 4a. By comparing the slopes of the line of best fit with and without active learning, we estimate that this form of active learning is approximately 2.6x more data efficient than uniform data labelling. We note that the model trained on the largest active learning dataset (200 samples per problem) appears to slightly underperform the expected trend line. Our best explanation for this observation is that 200 samples represents a significant fraction of the overall selection pool (1000 samples) and that this&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>&lt;/th>\n&lt;th>ORM&lt;/th>\n&lt;th>PRM&lt;/th>\n&lt;th>Majority Vote&lt;/th>\n&lt;th># Problems&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>AP Calculus&lt;/td>\n&lt;td>68.9%&lt;/td>\n&lt;td>&lt;b>86.7%&lt;/b>&lt;/td>\n&lt;td>80.0%&lt;/td>\n&lt;td>45&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>AP Chemistry&lt;/td>\n&lt;td>68.9%&lt;/td>\n&lt;td>&lt;b>80.0%&lt;/b>&lt;/td>\n&lt;td>71.7%&lt;/td>\n&lt;td>60&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>AP Physics&lt;/td>\n&lt;td>77.8%&lt;/td>\n&lt;td>&lt;b>86.7%&lt;/b>&lt;/td>\n&lt;td>82.2%&lt;/td>\n&lt;td>45&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>AMC10/12&lt;/td>\n&lt;td>49.1%&lt;/td>\n&lt;td>&lt;b>53.2%&lt;/b>&lt;/td>\n&lt;td>32.8%&lt;/td>\n&lt;td>84&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Aggregate&lt;/td>\n&lt;td>63.8%&lt;/td>\n&lt;td>&lt;b>72.9%&lt;/b>&lt;/td>\n&lt;td>61.3%&lt;/td>\n&lt;td>234&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nTable 1: We measure out-of-distribution generalization using recent STEM tests. We evaluate the outcome-supervised RM, the process-supervised RM, and majority voting using 100 test samples per problem.\n\nrelative lack of diversity limits the possible upside from active learning.\n\nWe also performed a preliminary investigation into the impact of iteratively retraining  $\\text{PRM}_{\\text{selector}}$  throughout data collection. Between iterations, we retrained  $\\text{PRM}_{\\text{selector}}$  using all currently labeled data. Unfortunately, we observed instability in this process which we were unable to diagnose. The resulting reward models performed no better than the models described above. We expect some form of iterative retraining to be beneficial in active learning, but we currently have no concrete evidence to support this claim. We consider this a compelling direction for future research.\n\n## 5 OOD Generalization\n\nTo get some measure of out-of-distribution generalization, we evaluate our large-scale ORM and PRM on a held-out set of 224 STEM questions, pulled from the most recent AP Physics, AP Calculus, AP Chemistry, AMC10, and AMC12 exams. Since these tests were released after the pre-training dataset was compiled, we can have high confidence that the model has not seen these problems. We report the best-of-100 performance of the ORM, PRM and majority voting in Table 1. We observe results similar to those in Section 3: the PRM outperforms both the ORM and majority voting. This shows us that the PRM can tolerate a modest amount of distribution shift and that its strong performance holds up on fresh test questions.\n\n## 6 Discussion\n\n### 6.1 Credit Assignment\n\nOne clear advantage of process supervision is that it provides more precise feedback than outcome supervision. A reward model trained with outcome supervision faces a difficult credit-assignment task — to generalize well, it must determine where an incorrect solution went wrong. This is particularly difficult for hard problems: most model-generated solutions contain an error somewhere, so the marginal value of a negative label from outcome supervision is low. Incontrast, process supervision provides a richer signal: it specifies both how many of the first steps were in fact correct, as well as the precise location of the incorrect step. Process supervision makes credit assignment easier, and we believe that this explains its strong performance.\n\n## 6.2 Alignment Impact\n\nProcess supervision has several advantages over outcome supervision related to AI alignment. Process supervision is more likely to produce interpretable reasoning, since it encourages models to follow a process endorsed by humans. Process supervision is also inherently safer: it directly rewards an aligned chain-of-thought rather than relying on outcomes as a proxy for aligned behavior (Stuhlmüller and Byun, 2022). In contrast, outcome supervision is harder to scrutinize, and the preferences conveyed are less precise. In the worst case, the use of outcomes as an imperfect proxy could lead to models that become misaligned after learning to exploit the reward signal (Uesato et al., 2022; Cotra, 2022; Everitt et al., 2017).\n\nIn some cases, safer methods for AI systems can lead to reduced performance (Ouyang et al., 2022; Askell et al., 2021), a cost which is known as an alignment tax. In general, any alignment tax may hinder the adoption of alignment methods, due to pressure to deploy the most capable model. Our results show that process supervision in fact incurs a negative alignment tax. This could lead to increased adoption of process supervision, which we believe would have positive alignment side-effects. It is unknown how broadly these results will generalize beyond the domain of math, and we consider it important for future work to explore the impact of process supervision in other domains.\n\n## 6.3 Test Set Contamination\n\nThe test set of the MATH dataset contains problems that are discussed in several online venues, and it is likely that some of these problems appear in the pretraining dataset for our models. We attempted to remove all MATH problems from our MathMix dataset using string-matching heuristics, but since humans can post hard-to-detect rephrasings of a problem online, it is difficult to make any strong guarantees about the overlap between MathMix and the MATH dataset.\n\nIn our experience inspecting model-generated solutions, we saw no clear signs of our models memorizing MATH problems. However, it is impossible to rule out subtle forms of memorization that would slip past manual inspection, and it is still possible that some degree of contamination has slightly inflated our performance on the MATH test set. Even in that case, we would expect any contamination to manifest similarly across all methods, and that the relative comparisons made throughout this work would remain mostly unaffected.\n\nWe also note that the PRM regularly surfaces correct solutions to MATH problems that have a low single-digit percentage solve-rate under the generator, some examples of which can be seen in Appendix I. The generator’s lowsolve-rate is an additional indication that it has not encountered such problems via test set contamination. Our generalization results from Section 5 further strengthen our claim that test set contamination has not significantly impacted this work, since we observe qualitatively similar results on problems that are guaranteed to be uncontaminated.\n\n## 7 Related Work\n\n### 7.1 Outcome vs Process Supervision\n\nIn work closely related to our own, Uesato et al. (2022) compare the impact of outcome and process supervision in the domain of grade school math. They found that both methods led to similar final-answer error rates, and that process supervision achieved those results with less data. While our core methodology is very similar, there are three main details that differ. First, we use a more capable model to collect PRM800K dataset and to perform our large-scale experiments. However, our small-scale results in Section 4 suggest that large-scale models are not necessary to observe benefits from process supervision. Second, we evaluate on the MATH dataset, which is significantly more challenging than GSM8K. Third, we collect a much larger quantity of process supervision data.\n\nOn the surface, the results from Uesato et al. (2022) may seem to conflict with our claim that process supervision leads to better performance. However, we believe the apparent conflict can be explained by the difference in the scale of the supervision. The data scaling trend in Figure 4a suggests that a small amount of process supervision and a large amount of outcome supervision do in fact lead to similar performance, consistent with the results from Uesato et al. (2022). The trend also shows that process supervision beats outcome supervision when scaled up, even when judged based solely on outcomes. This is consistent with our results in Section 3. We believe these results make a strong case for using process supervision.\n\n### 7.2 Synthetic Supervision\n\nSimilar to our work in Section 4, Gao et al. (2022) use a large reward model to supervise the training of smaller models. They study the over-optimization that occurs during RLHF, with experiments that require large quantities of human preference data. To work around this challenge, they use a gold-standard reward model to replace human feedback. Our use of a large-scale reward model to supervise smaller reward models shares similarities with their approach.\n\n### 7.3 Natural Language Reasoning\n\nSeveral recent studies that have examined the reasoning ability of large language models are implicitly relevant to our work. Lewkowycz et al. (2022) showed that finetuning models on a large corpus of technical content led to significantly improved performance on MATH. Wang et al. (2022) showed that *self-consistency*leads to remarkably strong performance on many reasoning benchmarks, notably without requiring any additional finetuning. Wei et al. (2022) and Nye et al. (2021) demonstrate the importance of explicitly performing intermediate reasoning steps via a *chain of thought* or a *scratchpad* in order to solve tasks that require multi-step reasoning. Kojima et al. (2022) show that models are able to perform this behavior zero-shot, conditioned only on a simple prompt.\n\n## 8 Conclusion\n\nWe have shown that process supervision can be used to train much more reliable reward models than outcome supervision in the domain of mathematical reasoning. We have also shown that active learning can be used to lower the cost of human data collection by surfacing only the most valuable model completions for human feedback. We release PRM800K, the full dataset of human feedback used to train our state-of-the-art reward model, with the hope that removing this significant barrier to entry will catalyze related research on the alignment of large language models. We believe that process supervision is currently under-explored, and we are excited for future work to more deeply investigate the extent to which these methods generalize.\n\n## Acknowledgements\n\nWe thank Joshua Achiam, Mark Chen, Jonathan Gordon, Dan Hendrycks, Lukasz Kaiser, Oleg Murk, Ben Sokolowsky, Francis Song, and Jonathan Uesato for valuable feedback and thoughtful discussions; Giambattista Parascandolo and Daniel Selsam for their contributions to the MathMix dataset; Jonathan Ward for contributing to the data collection interface; Wojciech Zaremba for encouraging us to scale up data collection; Peter Hoeschele and Aris Kostantinidis for supporting our data collection; the research acceleration and supercomputing teams at OpenAI for providing infrastructure support; and the team at Scale and the many data-labelers who created PRM800K.\n\n## References\n\n- A. Askell, Y. Bai, A. Chen, D. Drain, D. Ganguli, T. Henighan, A. Jones, N. Joseph, B. Mann, N. DasSarma, et al. A general language assistant as a laboratory for alignment. *arXiv preprint arXiv:2112.00861*, 2021.\n- S. Bubeck, V. Chandrasekaran, R. Eldan, J. Gehrke, E. Horvitz, E. Kamar, P. Lee, Y. T. Lee, Y. Li, S. Lundberg, et al. Sparks of artificial general intelligence: Early experiments with gpt-4. *arXiv preprint arXiv:2303.12712*, 2023.P. F. Christiano, J. Leike, T. Brown, M. Martic, S. Legg, and D. Amodei. Deep reinforcement learning from human preferences. *Advances in neural information processing systems*, 30, 2017.\n\nK. Cobbe, V. Kosaraju, M. Bavarian, M. Chen, H. Jun, L. Kaiser, M. Plappert, J. Tworek, J. Hilton, R. Nakano, et al. Training verifiers to solve math word problems. *arXiv preprint arXiv:2110.14168*, 2021.\n\nA. Cotra. Without specific countermeasures, the easiest path to transformative AI likely leads to AI takeover. &lt;https://www.alignmentforum.org/posts/pRkFkzwKZ2zfa3R6H/without-specific-countermeasures-the-easiest-path-to>, 2022.\n\nA. Creswell, M. Shanahan, and I. Higgins. Selection-inference: Exploiting large language models for interpretable logical reasoning. *arXiv preprint arXiv:2205.09712*, 2022.\n\nT. Everitt, V. Krakovna, L. Orseau, M. Hutter, and S. Legg. Reinforcement learning with a corrupted reward channel. *arXiv preprint arXiv:1705.08417*, 2017.\n\nL. Gao, J. Schulman, and J. Hilton. Scaling laws for reward model overoptimization. *arXiv preprint arXiv:2210.10760*, 2022.\n\nD. Hendrycks, C. Burns, S. Kadavath, A. Arora, S. Basart, E. Tang, D. Song, and J. Steinhardt. Measuring mathematical problem solving with the math dataset. *arXiv preprint arXiv:2103.03874*, 2021.\n\nT. Kojima, S. S. Gu, M. Reid, Y. Matsuo, and Y. Iwasawa. Large language models are zero-shot reasoners. *arXiv preprint arXiv:2205.11916*, 2022.\n\nA. Lewkowycz, A. Andreassen, D. Dohan, E. Dyer, H. Michalewski, V. Ramasesh, A. Slone, C. Anil, I. Schlag, T. Gutman-Solo, et al. Solving quantitative reasoning problems with language models. *arXiv preprint arXiv:2206.14858*, 2022.\n\nY. Li, Z. Lin, S. Zhang, Q. Fu, B. Chen, J.-G. Lou, and W. Chen. On the advance of making language models better reasoners. *arXiv preprint arXiv:2206.02336*, 2022.\n\nJ. Maynez, S. Narayan, B. Bohnet, and R. McDonald. On faithfulness and factuality in abstractive summarization. *arXiv preprint arXiv:2005.00661*, 2020.\n\nR. Nakano, J. Hilton, S. Balaji, J. Wu, L. Ouyang, C. Kim, C. Hesse, S. Jain, V. Kosaraju, W. Saunders, et al. Webgpt: Browser-assisted question-answering with human feedback. *arXiv preprint arXiv:2112.09332*, 2021.\n\nE. Nichols, L. Gao, and R. Gomez. Collaborative storytelling with large-scale neural language models. In *Proceedings of the 13th ACM SIGGRAPH Conference on Motion, Interaction and Games*, pages 1–10, 2020.M. Nye, A. J. Andreassen, G. Gur-Ari, H. Michalewski, J. Austin, D. Bieber, D. Dohan, A. Lewkowycz, M. Bosma, D. Luan, et al. Show your work: Scratchpads for intermediate computation with language models. *arXiv preprint arXiv:2112.00114*, 2021.\n\nOpenAI. Gpt-4 technical report. *arXiv preprint arXiv:2303.08774*, 2023.\n\nL. Ouyang, J. Wu, X. Jiang, D. Almeida, C. L. Wainwright, P. Mishkin, C. Zhang, S. Agarwal, K. Slama, A. Ray, et al. Training language models to follow instructions with human feedback. *arXiv preprint arXiv:2203.02155*, 2022.\n\nJ. Shen, Y. Yin, L. Li, L. Shang, X. Jiang, M. Zhang, and Q. Liu. Generate & rank: A multi-task framework for math word problems. *arXiv preprint arXiv:2109.03034*, 2021.\n\nN. Stiennon, L. Ouyang, J. Wu, D. Ziegler, R. Lowe, C. Voss, A. Radford, D. Amodei, and P. F. Christiano. Learning to summarize with human feedback. *Advances in Neural Information Processing Systems*, 33:3008–3021, 2020.\n\nA. Stuhlmüller and J. Byun. Supervise process, not outcomes. &lt;https://ought.org/updates/2022-04-06-process>, 2022.\n\nJ. Uesato, N. Kushman, R. Kumar, F. Song, N. Siegel, L. Wang, A. Creswell, G. Irving, and I. Higgins. Solving math word problems with process-and outcome-based feedback. *arXiv preprint arXiv:2211.14275*, 2022.\n\nX. Wang, J. Wei, D. Schuurmans, Q. Le, E. Chi, and D. Zhou. Self-consistency improves chain of thought reasoning in language models. *arXiv preprint arXiv:2203.11171*, 2022.\n\nJ. Wei, X. Wang, D. Schuurmans, M. Bosma, E. Chi, Q. Le, and D. Zhou. Chain of thought prompting elicits reasoning in large language models. *arXiv preprint arXiv:2201.11903*, 2022.\n\nE. Zelikman, Y. Wu, J. Mu, and N. Goodman. Star: Bootstrapping reasoning with reasoning. *Advances in Neural Information Processing Systems*, 35: 15476–15488, 2022.\n\nD. M. Ziegler, N. Stiennon, J. Wu, T. B. Brown, A. Radford, D. Amodei, P. Christiano, and G. Irving. Fine-tuning language models from human preferences. *arXiv preprint arXiv:1909.08593*, 2019.## A MathMix\n\nSimilar to Lewkowycz et al. (2022) we construct a large-scale dataset of high-quality math-relevant tokens for use in a lightweight pretraining stage, before finetuning on comparably smaller datasets like MATH and PRM800K. This dataset, which we call MathMix, has two main differences compared to the one used to train Minerva. First, it is smaller and more aggressively filtered to high-quality math problem-solving content, and second, it does not explicitly mix in general language data.\n\nMinerva was trained on 38.5B tokens of arXiv documents and webscraper pages with LaTeX content, while MathMix consists of a smaller set of 1.5B tokens containing individual math problems and their solutions, free-form text discussing math problems and concepts, and synthetic data (Table 2). While Minerva was pretrained on a dataset with 5% general natural language data, we chose not to mix in any natural language data explicitly, primarily because MathMix already contains plenty of natural language data.\n\n&lt;table border=\"1\">&lt;thead>&lt;tr>&lt;th>Data type&lt;/th>&lt;th>Token count&lt;/th>&lt;th>Present in pretraining?&lt;/th>&lt;/tr>&lt;/thead>&lt;tbody>&lt;tr>&lt;td>Math problems and solutions&lt;/td>&lt;td>~ 275M&lt;/td>&lt;td>No&lt;/td>&lt;/tr>&lt;tr>&lt;td>Free-form math discussion text (1)&lt;/td>&lt;td>~ 430M&lt;/td>&lt;td>No&lt;/td>&lt;/tr>&lt;tr>&lt;td>Free-form math discussion text (2)&lt;/td>&lt;td>~ 450M&lt;/td>&lt;td>Yes&lt;/td>&lt;/tr>&lt;tr>&lt;td>Synthetic data (1)&lt;/td>&lt;td>~ 30M&lt;/td>&lt;td>No&lt;/td>&lt;/tr>&lt;tr>&lt;td>Synthetic data (2)&lt;/td>&lt;td>~ 100M&lt;/td>&lt;td>Yes&lt;/td>&lt;/tr>&lt;tr>&lt;td>Critiques grading data&lt;/td>&lt;td>~ 500M&lt;/td>&lt;td>No&lt;/td>&lt;/tr>&lt;/tbody>&lt;/table>\n\nTable 2: MathMix dataset components.\n\nNote that when training smaller models, as in Section 4, we use a slightly smaller variant of MathMix that excludes the critiques data and only consists of 1B tokens. For our large models experiments, we train on MathMix for roughly 3B tokens (2 epochs). For our small models experiments, we train for 6 epochs (roughly 6.6B tokens).\n\nWe apply a set of decontamination checks on MathMix against the test split of the MATH dataset, including stripping out LaTeX and searching for matching n-grams, but we can make no strong guarantees on the efficacy of this decontamination. As discussed in Section 6.3, we would not expect the relative comparisons made throughout this work to be significantly impacted by test set contamination.## B PRM800K\n\nWe collected 1,085,590 step-level labels over 101,599 solution samples. We present the whole unfiltered dataset as PRM800K. During training we discard labels used for quality control, as well as any step-level labels for which the labeler was unable to complete the task. The filtered dataset contains about 800,000 step-level labels over 75,000 solutions. The full PRM800K dataset is available at &lt;https://github.com/openai/prm800k>.\n\nThe data collection was split into two separate phases. In phase 1, we collected labels for multiple alternative completions at each step of a solution. This seeded our dataset but was cumbersome—for many steps the alternatives were repetitive, and we found labelers spent a lot of time supervising long uninteresting solutions. As a result, the step-level labels we collected in this phase are more repetitive than those collected later. In total, phase 1 represents about 5% of PRM800K, or about 40,000 step-level labels.\n\nThe majority of our labels were collected as part of phase 2, during which we scaled up and streamlined the data collection process. Phase 2 data collection is split into 10 generations. For each generation, we sample  $N$  solutions per problem from the generator. We rank these solutions with our current best PRM and surface the highest scoring wrong-answer solutions to our labelers. We retrain this PRM between each generation using all the latest data. This active learning strategy changes the balance of our data considerably. Though we sometimes surfaced correct solutions (either by manually injecting correct solutions or because of errors in our automatic grading), the vast majority of the labels we collected in this phase are for incorrect solutions. Table 3 breaks down the balance of correct/incorrect steps and solutions between the different phases of data collection. Though we mostly collected labels on incorrect solutions, we still collected many labels for correct individual steps. In fact, our small-scale ablations in Section 4.2 suggest that this active learning strategy, which favors labelling high-scoring wrong-answer solutions, improves performance despite the resulting imbalance in the dataset.\n\n&lt;table border=\"1\">&lt;thead>&lt;tr>&lt;th>&lt;/th>&lt;th>phase 1&lt;/th>&lt;th>phase 2&lt;/th>&lt;th>combined&lt;/th>&lt;/tr>&lt;/thead>&lt;tbody>&lt;tr>&lt;td>% end in correct solution&lt;/td>&lt;td>85.1&lt;/td>&lt;td>13.2&lt;/td>&lt;td>14.2&lt;/td>&lt;/tr>&lt;tr>&lt;td>% correct steps&lt;/td>&lt;td>58.6&lt;/td>&lt;td>74.1&lt;/td>&lt;td>73.1&lt;/td>&lt;/tr>&lt;/tbody>&lt;/table>\n\nTable 3: Distribution of positive/negative steps/solutions.\n\nSome of our phase 2 questions are intended for quality control. For a quality control question, researchers mark which steps are reasonable to label as incorrect. Then we assess that labelers are able to consistently mark those steps as incorrect. Prior to starting on phase 2, we required all labelers to label 30 quality control questions. This served as a screening test, and we only admitted labelers that agreed with our gold labels at least 75% of the time.\n\nWe then designated 10-20 problems per generation as additional quality control questions, and we randomly served them to labelers as they workedthrough the task. We used the results of this continuous quality control to remove labelers whose quality slipped too far, as well as to prepare educational material on common mistakes in order to improve labeler alignment with our instructions.\n\n## C Evaluation\n\nAs we scaled up the project, we began having to collect labels on multiple solutions for the same training problem. In order to avoid the risk of over-fitting on the 7,500 MATH training problems, we expanded the training set to include 4,500 MATH test split problems. We therefore evaluate our models only on the remaining 500 held-out problems. We selected these 500 test problems uniformly at random. In Figure 5, we show that the distribution of difficulty levels and subjects in this subset is representative of the MATH test set as a whole. The specific test set we used can be found at &lt;https://github.com/openai/prm800k>. We leave it for future work to explore how many distinct training problems are actually necessary, and how quickly our methods overfit to the training set.\n\nFigure 5: Two histograms comparing the distribution of problem difficulty levels and subjects in both the original MATH test set and in our 500 problem test subset.## D Labelling Instructions\n\nLabelers were tasked to look at steps in a solution and label each one as **positive**, **negative**, or **neutral**. A step is considered **neutral** if it is appropriate in context, reasonable, correct, and contains only computations that can be verified easily. A step is **positive** if it is **neutral** and also progresses towards the solution. All other steps are considered **negative**. Labelers were not given reference solutions, but they were given the ground truth final answers. We chose not to provide reference solutions to avoid biasing them towards one particular path to the solution. We chose to provide ground truth final answers since this information can sometimes help labelers resolve their own misunderstandings.\n\nIn phase 1, labelers were permitted to enter their own steps in the case that all candidate steps were **negative**. Then the solution would progress from a randomly selected **positive** step (or **neutral** if there were no **positive** ones). This often resulted in trajectories that got stuck in endless sequences of **neutral** steps that said reasonable things but made frustratingly slow progress towards a solution or **negative** steps that needed constant human supervision. In phase 2, we pre-generate whole solutions and end the task as soon as the first **negative** step is encountered. The full instructions given to labelers can be found at &lt;https://github.com/openai/prm800k/tree/main/prm800k/instructions>.\n\n## E ORM Training Details\n\nWe train outcome-supervised reward models in the same manner as token-level verifiers from Cobbe et al. (2021), with a few subtle differences to hyperparameters. In particular, we only train for a single epoch on each dataset of model samples and reward model labels, without dropout, and without jointly learning a language modeling objective. We find that performance is not sensitive to most other hyperparameters, within a reasonable range.\n\nTo collect model samples, we simply sample uniformly from the generator at a temperature of 1.0 without applying any rebalancing of positives or negatives. At training time, the reward model makes predictions for every token in the context. The target for each token in a solution is the same, based on whether the solution is labelled correct or incorrect. At test time, we simply use the score of the final token in the completion as the overall score of the solution. We note that this setup is identical to the way token-level verifiers were trained in Cobbe et al. (2021).## F PRM Details\n\n### F.1 Training\n\nWe train our PRMs by fine-tuning the MathMix model to predict the probability of positive, negative, and neutral labels given a solution prefix ending in one of our labeled steps. We sweep over hyperparameters using a dataset containing the first  $\\sim 10\\%$  of PRM800K. Fine-tuning an LLM from its ordinary language modeling task to a classification task like this is a large distribution shift, and we found low learning rates were important to stable PRM training.\n\nAll of our PRMs are trained for 2 epochs. On smaller datasets (such as in phase 1 and the first few generations of phase 2) this improves the final performance over training for just 1 epoch. Additional epochs, up to some point, don't noticeably help or hurt performance. On larger datasets, the benefits of 2 epoch training diminishes, but we continue doing it for consistency.\n\n### F.2 Scoring\n\nThere are multiple ways of using the PRM to score solutions. In general, we produce a single solution-level score by performing a reduction over step-level scores, where the step-level score is the probability that the step's label is positive. This involves two specific implementation decisions. First, when determining a step-level score, we either consider a neutral label to be positive or negative. Second, when determining a solution-level score, we either use the minimum or the product over step-level scores as a reduction.\n\nWe show results from all four scoring strategies in Table 4. The best performing strategy is to take the product of step-level scores and to consider the neutrals as positives, but the difference in performance between all strategies is minor. Throughout the rest of this work, we consider neutral steps to be positive, and we define the solution score to be the product of step-level scores. Using the product instead of the minimum as the reduction does create a slight bias against solutions with a larger number of steps.\n\n&lt;table>&lt;thead>&lt;tr>&lt;th>&lt;/th>&lt;th>product&lt;/th>&lt;th>minimum&lt;/th>&lt;/tr>&lt;/thead>&lt;tbody>&lt;tr>&lt;td>neutral = positive&lt;/td>&lt;td>78.2%&lt;/td>&lt;td>77.6%&lt;/td>&lt;/tr>&lt;tr>&lt;td>neutral = negative&lt;/td>&lt;td>77.4%&lt;/td>&lt;td>77.8%&lt;/td>&lt;/tr>&lt;/tbody>&lt;/table>\n\nTable 4: Best-of-1860 test performance using the PRM with four different scoring strategies.## G Difficulty Breakdown\n\nWe show performance of our ORM and PRM on each quintile of the MATH dataset. We determine quintiles based on the pass rate under the generator. It is interesting to note that the performance gap is not only apparent on high difficulty problems: it is in fact apparent across all difficulties. For the lowest difficulty problems, we see that it is possible to find adversarial examples that fool the ORM, since the ORM’s performance slightly decreases as the number of samples increases. In contrast, the PRM remains highly robust over this same set of samples.\n\nWe also see that increasing the number of samples has the largest positive effect on the highest difficulty problems. This is to be expected, since a large number of generator samples may be required to find a true and convincing solution to a hard problem.\n\nFigure 6: A breakdown of ORM vs PRM performance by problem difficulty.## H Synthetic Supervision Details\n\nWe can use  $\\text{PRM}_{\\text{large}}$  to provide either outcome or process supervision for smaller models. We determine the labels for individual steps based on the step-level probabilities outputted by  $\\text{PRM}_{\\text{large}}$ . To do this, we set an arbitrary threshold: any step that  $\\text{PRM}_{\\text{large}}$  assigns a negative label with greater than 20% probability is considered incorrect. We choose this threshold based on the observation that  $\\text{PRM}_{\\text{large}}$  is slightly miscalibrated in the direction of favoring positive labels.\n\nTo provide process supervision for a solution, we directly return the step-level labels (positive or negative) provided by  $\\text{PRM}_{\\text{large}}$ , up until the first step that is marked as negative. This mimics our true human data collection process. To provide outcome supervision, we mark the solution as correct if and only if  $\\text{PRM}_{\\text{large}}$  considers every step to be correct (using the same thresholding logic).# I PRM Visualizations\n\nAll examples shown come from the large-scale generator (GPT-4). We note the pass-rate under the generator to give some sense of the difficulty of these problems.\n\n## I.1 True Positives\n\nThese cherry-picked examples show the best-of-1860 solution from the generator as ranked by the large-scale PRM.\n\nProblem 1. Generator pass-rate: 0.1%. This challenging trigonometry problem requires applying several identities in a not-at-all obvious succession. Most solution attempts fail, because it is hard to choose which identities are actually helpful. Though successful solutions to this problem are rare, the reward model correctly recognizes when a valid chain-of-thought has been found.\n\nSimplify  $\\tan 100^\\circ + 4 \\sin 100^\\circ$ .\n\nI notice that the angle 100 degrees is not a special angle, so I will need to use some trigonometric identities to simplify this expression.\n\nI recall that  $\\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}$  and  $\\sin 2\\theta = 2 \\sin \\theta \\cos \\theta$ .\n\nI can use these identities to rewrite the expression as  $\\frac{\\sin 100^\\circ}{\\cos 100^\\circ} + 4 \\sin 100^\\circ$ .\n\nI can combine the terms by finding a common denominator of  $\\cos 100^\\circ$ .\n\nI get  $\\frac{\\sin 100^\\circ + 4 \\sin 100^\\circ \\cos 100^\\circ}{\\cos 100^\\circ}$ .\n\nI can simplify the numerator by using the double angle identity again, but in reverse.\n\nI get  $\\frac{\\sin 100^\\circ + 2 \\sin 200^\\circ}{\\cos 100^\\circ}$ .\n\nI notice that 200 degrees is the same as 180 degrees plus 20 degrees, so I can use the sum angle identity for sine.\n\nI get  $\\frac{\\sin 100^\\circ + 2(\\sin 180^\\circ \\cos 20^\\circ + \\cos 180^\\circ \\sin 20^\\circ)}{\\cos 100^\\circ}$ .\n\nI recall that  $\\sin 180^\\circ = 0$  and  $\\cos 180^\\circ = -1$ , so I can simplify further.\n\nI get  $\\frac{\\sin 100^\\circ - 2 \\sin 20^\\circ}{\\cos 100^\\circ}$ .\n\nI notice that 100 degrees is the same as 90 degrees plus 10 degrees, so I can use the sum angle identity for sine and cosine.\n\nI get  $\\frac{(\\sin 90^\\circ \\cos 10^\\circ + \\cos 90^\\circ \\sin 10^\\circ) - 2 \\sin 20^\\circ}{(\\cos 90^\\circ \\cos 10^\\circ - \\sin 90^\\circ \\sin 10^\\circ)}$ .\n\nI recall that  $\\sin 90^\\circ = 1$  and  $\\cos 90^\\circ = 0$ , so I can simplify further.\n\nI get  $\\frac{\\cos 10^\\circ - 2 \\sin 20^\\circ}{-\\sin 10^\\circ}$ .\n\nI can simplify the sign by multiplying the numerator and denominator by -1.\n\nI get  $\\frac{2 \\sin 20^\\circ - \\cos 10^\\circ}{\\sin 10^\\circ}$ .\n\nI notice that 20 degrees is the same as 30 degrees minus 10 degrees, so I can use the difference angle identity for sine.\n\nI get  $\\frac{2(\\sin 30^\\circ \\cos 10^\\circ - \\cos 30^\\circ \\sin 10^\\circ) - \\cos 10^\\circ}{\\sin 10^\\circ}$ .\n\nI recall that  $\\sin 30^\\circ = \\frac{1}{2}$  and  $\\cos 30^\\circ = \\frac{\\sqrt{3}}{2}$ , so I can simplify further.\n\nI get  $\\frac{\\cos 10^\\circ - \\sqrt{3} \\sin 10^\\circ - \\cos 10^\\circ}{\\sin 10^\\circ}$ .\n\nI can cancel out the  $\\cos 10^\\circ$  terms in the numerator.\n\nI get  $\\frac{-\\sqrt{3} \\sin 10^\\circ}{\\sin 10^\\circ}$ .\n\nI can cancel out the  $\\sin 10^\\circ$  terms in the numerator and denominator.\n\nI get  $-\\sqrt{3}$ .\n\nAnswer:  $-\\sqrt{3}$Problem 2. Generator pass-rate: 5.8%. In step 7 and 8, the generator starts performing guess-and-check. This is a common place the model might hallucinate, by claiming a particular guess is successful when it isn't. In this case, the reward model verifies each step and determines that the chain-of-thought is correct.\n\nFind the unique odd integer  $t$  such that  $0 < t < 23$  and  $t + 2$  is the inverse of  $t$  modulo 23.\n\nI need to find an odd integer  $t$  that satisfies the congruence  $t + 2 \\equiv t^{-1} \\pmod{23}$ .\n\nTo do that, I can multiply both sides by  $t$  and get  $t^2 + 2t \\equiv 1 \\pmod{23}$ .\n\nThen I can complete the square by adding and subtracting  $(2/2)^2 = 1$  to the left side and get  $(t + 1)^2 - 1 \\equiv 1 \\pmod{23}$ .\n\nSimplifying, I get  $(t + 1)^2 \\equiv 2 \\pmod{23}$ .\n\nNow I need to find a square root of 2 modulo 23.\n\nI can try some values of  $t + 1$  and see if they work.\n\nFor example, if  $t + 1 = 3$ , then  $(t + 1)^2 = 9 \\not\\equiv 2 \\pmod{23}$ .\n\nIf  $t + 1 = 5$ , then  $(t + 1)^2 = 25 \\equiv 2 \\pmod{23}$ .\n\nSo one possible value of  $t$  is  $t = 5 - 1 = 4$ .\n\nBut this is not odd, so I need to find another one.\n\nI know that if  $t + 1$  is a square root of 2 modulo 23, then so is  $-t - 1$ .\n\nSo I can try  $-t - 1 = 5$  and get  $t = -6$ .\n\nBut this is negative, so I need to add 23 to get a positive value.\n\nSo another possible value of  $t$  is  $t = -6 + 23 = 17$ .\n\nThis is odd and satisfies the original congruence, so this is the unique solution.\n\nAnswer: 17\n\nProblem 3. Generator pass-rate: 1.7%. The generator successfully applies several trigonometric identities to simplify the expression.\n\nFind the degree measure of the least positive angle  $\\theta$  for which\n\n$$\\tan \\theta = \\frac{\\cos 5^\\circ \\cos 20^\\circ + \\cos 35^\\circ \\cos 50^\\circ - \\sin 5^\\circ \\sin 20^\\circ - \\sin 35^\\circ \\sin 50^\\circ}{\\sin 5^\\circ \\cos 20^\\circ - \\sin 35^\\circ \\cos 50^\\circ + \\cos 5^\\circ \\sin 20^\\circ - \\cos 35^\\circ \\sin 50^\\circ}.$$\n\nI notice that the numerator and denominator of the fraction are both sums of products of cosine and sine functions of angles that add up to 25 degrees or 85 degrees.\n\nThis suggests that I might be able to use some trigonometric identities to simplify the expression.\n\nFor example, I recall that  $\\cos(A + B) = \\cos A \\cos B - \\sin A \\sin B$  and  $\\sin(A + B) = \\sin A \\cos B + \\cos A \\sin B$ .\n\nIf I apply these identities to the terms in the numerator, I get  $\\cos 5^\\circ \\cos 20^\\circ + \\cos 35^\\circ \\cos 50^\\circ - \\sin 5^\\circ \\sin 20^\\circ - \\sin 35^\\circ \\sin 50^\\circ = \\cos(5^\\circ + 20^\\circ) + \\cos(35^\\circ + 50^\\circ) = \\cos 25^\\circ + \\cos 85^\\circ$ .\n\nSimilarly, if I apply these identities to the terms in the denominator, I get  $\\sin 5^\\circ \\cos 20^\\circ - \\sin 35^\\circ \\cos 50^\\circ + \\cos 5^\\circ \\sin 20^\\circ - \\cos 35^\\circ \\sin 50^\\circ = \\sin(5^\\circ + 20^\\circ) - \\sin(35^\\circ + 50^\\circ) = \\sin 25^\\circ - \\sin 85^\\circ$ .\n\nNow I have  $\\tan \\theta = \\frac{\\cos 25^\\circ + \\cos 85^\\circ}{\\sin 25^\\circ - \\sin 85^\\circ}$ .\n\nI wonder if I can simplify this fraction further.\n\nI recall another trigonometric identity that says  $\\cos A + \\cos B = 2 \\cos \\frac{A+B}{2} \\cos \\frac{A-B}{2}$ .\n\nIf I apply this identity to the numerator, I get  $\\cos 25^\\circ + \\cos 85^\\circ = 2 \\cos \\frac{25^\\circ + 85^\\circ}{2} \\cos \\frac{25^\\circ - 85^\\circ}{2} = 2 \\cos 55^\\circ \\cos(-30^\\circ)$ .\n\nI also recall that  $\\cos(-\\theta) = \\cos \\theta$ , so I can write  $\\cos(-30^\\circ) = \\cos 30^\\circ$ .\n\nSimilarly, I recall another trigonometric identity that says  $\\sin A - \\sin B = 2 \\cos \\frac{A+B}{2} \\sin \\frac{A-B}{2}$ .\n\nIf I apply this identity to the denominator, I get  $\\sin 25^\\circ - \\sin 85^\\circ = 2 \\cos \\frac{25^\\circ + 85^\\circ}{2} \\sin \\frac{25^\\circ - 85^\\circ}{2} = 2 \\cos 55^\\circ \\sin(-30^\\circ)$ .\n\nI also recall that  $\\sin(-\\theta) = -\\sin \\theta$ , so I can write  $\\sin(-30^\\circ) = -\\sin 30^\\circ$ .\n\nNow I have  $\\tan \\theta = \\frac{2 \\cos 55^\\circ \\cos 30^\\circ}{2 \\cos 55^\\circ (-\\sin 30^\\circ)} = \\frac{-\\cos 30^\\circ}{\\sin 30^\\circ}$ .\n\nI know that  $\\cos 30^\\circ = \\frac{\\sqrt{3}}{2}$  and  $\\sin 30^\\circ = \\frac{1}{2}$ , so I can simplify this to  $\\tan \\theta = -\\frac{\\sqrt{3}}{1} = -\\sqrt{3}$ .\n\nI also know that  $\\tan \\theta$  is negative in the second and fourth quadrants, and that  $\\tan \\theta = -\\sqrt{3}$  when  $\\theta$  is  $120^\\circ$  or  $300^\\circ$ .\n\nTherefore, the least positive angle  $\\theta$  for which  $\\tan \\theta = -\\sqrt{3}$  is  $120^\\circ$ .\n\nAnswer: 120Problem 4. Generator pass-rate: 4.5%. Here, the generator successfully performs a complex series of polynomial factorizations. The use of the Sophie-Germain identity in step 5 is an important step that could be considered insightful.\n\nLet\n\n$$x^8 + 3x^4 - 4 = p_1(x)p_2(x) \\cdots p_k(x),$$\n\nwhere each non-constant polynomial  $p_i(x)$  is monic with integer coefficients, and cannot be factored further over the integers. Compute  $p_1(1) + p_2(1) + \\cdots + p_k(1)$ .\n\nI notice that the given polynomial has even degree and only even powers of  $x$ , so I can try to make a substitution to simplify it:\n\nLet  $y = x^4$ , then the polynomial becomes  $y^2 + 3y - 4$ , which is a quadratic equation.\n\nI can factor this quadratic equation as  $(y + 4)(y - 1)$ , so the original polynomial is  $(x^4 + 4)(x^4 - 1)$ .\n\nNow I need to factor each of these factors further, if possible, over the integers.\n\nFor the first factor,  $x^4 + 4$ , I recall the Sophie Germain identity, which says that  $a^4 + 4b^4 = (a^2 + 2b^2 + 2ab)(a^2 + 2b^2 - 2ab)$ .\n\nApplying this identity with  $a = x$  and  $b = 1$ , I get  $x^4 + 4 = (x^2 + 2x + 2)(x^2 - 2x + 2)$ .\n\nFor the second factor,  $x^4 - 1$ , I can use the difference of squares formula, which says that  $a^2 - b^2 = (a + b)(a - b)$ .\n\nApplying this formula with  $a = x^2$  and  $b = 1$ , I get  $x^4 - 1 = (x^2 + 1)(x^2 - 1)$ .\n\nThen I can apply the difference of squares formula again with  $a = x$  and  $b = 1$ , to get  $x^2 - 1 = (x + 1)(x - 1)$ .\n\nSo the original polynomial is  $(x^4 + 4)(x^4 - 1) = (x^2 + 2x + 2)(x^2 - 2x + 2)(x^2 + 1)(x + 1)(x - 1)$ .\n\nThese are all the irreducible factors over the integers, so  $p_1(x) = x^2 + 2x + 2$ ,  $p_2(x) = x^2 - 2x + 2$ ,  $p_3(x) = x^2 + 1$ ,  $p_4(x) = x + 1$ , and  $p_5(x) = x - 1$ .\n\nTo find the sum of their values at  $x = 1$ , I just need to plug in  $x = 1$  into each factor and add them up.\n\nI get  $p_1(1) = 1^2 + 2 \\cdot 1 + 2 = 5$ ,  $p_2(1) = 1^2 - 2 \\cdot 1 + 2 = 1$ ,  $p_3(1) = 1^2 + 1 = 2$ ,  $p_4(1) = 1 + 1 = 2$ , and  $p_5(1) = 1 - 1 = 0$ .\n\nSo the final answer is  $5 + 1 + 2 + 2 + 0 = 10$ .\n\nAnswer: 10\n\n## I.2 True Negatives\n\nProblem 5. Generator pass-rate: 4.5%. The generator attempts to use the difference of squares formula in step 12 on an expression that isn't in fact a difference of squares. The reward model catches this mistake.\n\nLet\n\n$$x^8 + 3x^4 - 4 = p_1(x)p_2(x) \\cdots p_k(x),$$\n\nwhere each non-constant polynomial  $p_i(x)$  is monic with integer coefficients, and cannot be factored further over the integers. Compute  $p_1(1) + p_2(1) + \\cdots + p_k(1)$ .\n\nThis problem is about factoring a polynomial over the integers, which can be a tricky task.\n\nOne possible strategy is to look for rational roots of the polynomial, using the rational root theorem.\n\nHowever, that would involve checking a lot of possible factors of  $-4$ , and there is no guarantee that the polynomial has any rational roots at all.\n\nAnother possible strategy is to use some algebraic tricks to simplify the polynomial or reduce its degree.\n\nI notice that the polynomial has only even powers of  $x$ , so I can try to substitute  $y = x^4$  and see what happens.\n\nThen the polynomial becomes  $y^2 + 3y - 4$ , which is a quadratic equation in  $y$ .\n\nI can try to factor this quadratic equation by looking for two numbers that multiply to  $-4$  and add to 3.\n\nThose numbers are 4 and  $-1$ , so I can write  $y^2 + 3y - 4 = (y + 4)(y - 1)$ .\n\nNow I can substitute back  $x^4 = y$  and get  $x^8 + 3x^4 - 4 = (x^4 + 4)(x^4 - 1)$ .\n\nThis looks promising, because I have reduced the degree of the factors from 8 to 4.\n\nI can try to factor each of these factors further, using the difference of squares formula.\n\nI get  $x^8 + 3x^4 - 4 = (x^4 + 2)(x^4 - 2)(x^2 + 1)(x^2 - 1)$ .\n\nI can apply the difference of squares formula again to the last factor and get  $x^8 + 3x^4 - 4 = (x^4 + 2)(x^2 - 2)(x^2 + 1)(x + 1)(x - 1)$ .\n\nNow I have factored the polynomial completely into monic linear and quadratic factors with integer coefficients.\n\nThese are the  $p_i(x)$ 's that the problem is asking for.\n\nTo find the sum of their values at  $x = 1$ , I just need to plug in  $x = 1$  into each factor and add them up.\n\nI get  $p_1(1) + p_2(1) + \\cdots + p_k(1) = (1^4 + 2)(1^4 - 2)(1^2 + 1)(1 + 1)(1 - 1)$ .\n\nSimplifying, I get  $p_1(1) + p_2(1) + \\cdots + p_k(1) = (3)(-1)(2)(2)(0)$ .\n\nMultiplying, I get  $p_1(1) + p_2(1) + \\cdots + p_k(1) = 0$ .\n\nAnswer: 0Problem 6. Generator pass-rate: 93.5%. In step 7, the generator makes an incorrect attempt to simplify an expression. The reward model catches this mistake.\n\nA class of 30 students recently took a test. If 20 students scored 80, 8 students scored 90, and 2 students scored 100, then what was the class average (the mean) on this test?\n\nTo find the class average, I need to add up all the scores and divide by the number of students.\n\nI can use a shortcut to add up the scores, since they are grouped by value.\n\nFor example, instead of adding  $80 + 80 + \\dots + 80$  twenty times, I can just multiply 80 by 20 to get the same result.\n\nSimilarly, I can multiply 90 by 8 and 100 by 2 to get the sums of those groups.\n\nSo, the total sum of the scores is  $80 * 20 + 90 * 8 + 100 * 2$ .\n\nI can use the distributive property of multiplication to simplify this expression.\n\nIt is equivalent to  $80 * (20 + 1) + 90 * 8 + 100$ .\n\nThat is,  $80 * 21 + 720 + 100$ .\n\nI can do the arithmetic in my head or use a calculator.\n\n$80 * 21$  is 1680, so the total sum is  $1680 + 720 + 100$ , which is 2500.\n\nNow, to find the average, I need to divide 2500 by 30, the number of students.\n\nI can use long division or a calculator for this step.\n\n2500 divided by 30 is 83.33, repeating.\n\nThis means that the class average is 83.33, or 83 and one-third.\n\nAnswer: 83.33\n\nProblem 7. Generator pass-rate: 48.0%. In step 11, the generator makes a simple calculation error. The reward model catches this mistake.\n\nIf  $A$  is the sum of the positive divisors of 500, what is the sum of the distinct prime divisors of  $A$ ?\n\nI notice that  $500 = 2^2 \\cdot 5^3$ , so its positive divisors are of the form  $2^a \\cdot 5^b$ , where  $a \\in \\{0, 1, 2\\}$  and  $b \\in \\{0, 1, 2, 3\\}$ .\n\nTo find the sum of these divisors, I can use a formula that involves the geometric series: if  $p$  is a prime number and  $n$  is a nonnegative integer, then the sum of the powers of  $p$  from 0 to  $n$  is  $\\frac{p^{n+1}-1}{p-1}$ .\n\nSo, the sum of the powers of 2 from 0 to 2 is  $\\frac{2^3-1}{2-1} = 7$ , and the sum of the powers of 5 from 0 to 3 is  $\\frac{5^4-1}{5-1} = 156$ .\n\nBy the distributive property, the sum of the divisors of 500 is the product of these two sums:  $A = 7 \\cdot 156 = 1092$ .\n\nNow, I need to find the sum of the distinct prime divisors of  $A$ .\n\nI can try to factor  $A$  into primes by trial division.\n\nI notice that  $A$  is divisible by 2, so I divide by 2 and get 546.\n\nI repeat this process and divide by 2 again, getting 273.\n\nNow, 273 is not divisible by 2, so I try the next prime, 3.\n\nI see that 273 is divisible by 3, so I divide by 3 and get 91.\n\nI divide by 3 again, getting 31.\n\nNow, 31 is a prime number, so I have found all the prime factors of  $A$ :  $A = 2^2 \\cdot 3^2 \\cdot 31$ .\n\nThe sum of the distinct prime divisors of  $A$  is  $2 + 3 + 31 = 36$ .\n\nAnswer: 36Problem 8. Generator pass-rate: 5.8%. The justification in step 8 is strange, but the reward model lets it slide. In step 9, though, the model incorrectly factors the expression. The reward model catches this mistake.\n\nFind the unique odd integer  $t$  such that  $0 < t < 23$  and  $t + 2$  is the inverse of  $t$  modulo 23.\n\nI need to find an odd integer  $t$  between 0 and 23 such that  $t + 2$  is the inverse of  $t$  modulo 23.\n\nThat means that  $t$  and  $t + 2$  multiply to give 1 modulo 23.\n\nI can write this as  $t(t + 2) \\equiv 1 \\pmod{23}$ .\n\nI can try to guess and check values of  $t$  until I find one that works, but that might take a long time.\n\nI can also try to use some properties of modular arithmetic to simplify the equation.\n\nFor example, I can subtract 23 from  $t + 2$  and still get the same remainder modulo 23.\n\nSo I can write  $t(t + 2) \\equiv t(t - 21) \\pmod{23}$ .\n\nThis looks simpler, because now I have a difference of two multiples of  $t$ .\n\nI can factor out  $t$  and get  $t(t - 21) \\equiv t(1 - 21) \\pmod{23}$ .\n\nNow I can divide both sides by  $t$ , as long as  $t$  is not a multiple of 23.\n\nThis gives me  $t - 21 \\equiv 1 - 21 \\pmod{23}$ .\n\nI can simplify this further by adding 21 to both sides.\n\nThis gives me  $t \\equiv 1 \\pmod{23}$ .\n\nThis means that  $t$  has the same remainder as 1 when divided by 23.\n\nThe smallest positive value of  $t$  that satisfies this is  $t = 1$ .\n\nThis is also an odd integer, so it meets the criteria of the problem.\n\nI can check that  $t = 1$  works by plugging it into the original equation.\n\nI get  $1(1 + 2) \\equiv 1 \\pmod{23}$ , which is true.\n\nTherefore, the unique odd integer  $t$  that satisfies the given conditions is  $t = 1$ .\n\nAnswer: 1\n\n### I.3 False Positives\n\nProblem 9. Generator pass-rate: 18.5%. The generator makes a subtle counting error in step 9. On the surface, it appears reasonable to claim that there are 5 ways to exchange the same colored ball since there are 5 colors. However, this undercounts by a factor of 2, since Bob has 2 choices for which ball to return to Alice. The reward model is fooled by this mistake.\n\nBob and Alice each have a bag that contains one ball of each of the colors, blue, green, orange, red, and violet. Alice randomly selects one ball from her bag and puts it into Bob's bag. Bob then randomly selects one ball from his bag and puts it into Alice's bag. What is the probability that after this process the contents of the two bags are the same?\n\nTo find the probability of an event, I need to divide the number of favorable outcomes by the number of possible outcomes.\n\nIn this case, the event is that the contents of the two bags are the same after the process.\n\nSo I need to count how many ways this can happen, and how many ways the process can happen in total.\n\nI will start with the total number of ways the process can happen.\n\nAlice can choose any of the five balls in her bag, and Bob can choose any of the six balls in his bag.\n\nSo the total number of ways the process can happen is 5 times 6, which is 30.\n\nNow I will count how many ways the contents of the two bags can be the same after the process.\n\nThis means that Alice and Bob must have exchanged the same color of ball.\n\nThere are five colors, so there are five ways they can exchange the same color of ball. ERROR\n\nTherefore, the number of favorable outcomes is 5.\n\nSo the probability of the event is 5 divided by 30, which simplifies to 1/6.\n\nAnswer: 1/6Problem 10. Generator pass-rate: 17.6%. In step 13, the generator attempts to simplify the equation by combining like terms. It correctly moves and combines the linear terms to the left-hand side, but then mistakenly leaves the right-hand side untouched. The reward model is fooled by this mistake.\n\nDenali and Nate work for a dog walking business and are paid for each dog they walk. Denali is responsible for 16 dogs and Nate is responsible for 12 dogs. Under the company's new policy, they will be assigned or unassigned new dogs in groups of  $x$  dogs. The ratio of Denali's pay to Nate's pay would be the same if Denali started walking  $4x$  more dogs and Nate stayed at 12 dogs or if  $x$  of Nate's dogs were reassigned to Denali. Find  $x$  if  $x \\neq 0$ .\n\nI need to find a value of  $x$  that makes the ratio of Denali's pay to Nate's pay the same in two different scenarios.  \n I can assume that the pay per dog is constant, so the ratio of their pay is the same as the ratio of the number of dogs they walk.  \n Let me write an equation for the first scenario, where Denali walks  $4x$  more dogs and Nate stays at 12 dogs.  \n The ratio of Denali's dogs to Nate's dogs is  $\\frac{16+4x}{12}$ .  \n Now let me write an equation for the second scenario, where  $x$  of Nate's dogs are reassigned to Denali.  \n The ratio of Denali's dogs to Nate's dogs is  $\\frac{16+x}{12-x}$ .  \n I want these two ratios to be equal, so I can set them equal to each other and solve for  $x$ .  \n I get  $\\frac{16+4x}{12} = \\frac{16+x}{12-x}$ .  \n I can cross-multiply and simplify this equation.  \n I get  $(16+4x)(12-x) = (16+x)(12)$ .  \n Expanding the brackets, I get  $192 - 16x + 48x - 4x^2 = 192 + 12x$ .  \n Subtracting 192 from both sides, I get  $-16x + 48x - 4x^2 = 12x$ .  \n Rearranging the terms, I get  $-4x^2 + 20x = 12x$ . ERROR  \n Subtracting  $12x$  from both sides, I get  $-4x^2 + 8x = 0$ .  \n I can factor out  $-4x$  from both terms, and get  $-4x(x-2) = 0$ .  \n This means that either  $-4x = 0$  or  $x-2 = 0$ .  \n Solving for  $x$ , I get  $x = 0$  or  $x = 2$ .  \n However, the problem says that  $x \\neq 0$ , so I can ignore that solution.  \n Therefore, the only valid solution is  $x = 2$ .  \n Answer: 2\n\nProblem 11. Generator pass-rate: 13.4%. The generator attempts to perform long division, but in step 16, it forgets to include the leading zeros in the repeating part of the decimal. The reward model is fooled by this mistake.\n\nWhen converting  $\\frac{31}{1111}$  to a decimal, the decimal turns out to be a repeating decimal. How many digits repeat in this repeating decimal? For example, if you get the repeating decimal  $0.\\overline{123}$ , then your answer should be 3, and if you get 0.4367, your answer should be 1.\n\nTo convert a fraction to a decimal, I can divide the numerator by the denominator using long division.  \n I'll start by writing 31 over 11111 and bring down a zero.  \n Then I'll ask, how many times does 11111 go into 310?  \n Well, it doesn't go in evenly, so I'll write a zero above the decimal point and bring down another zero.  \n Now I have 3100.  \n How many times does 11111 go into 3100?  \n Still zero, so I'll write another zero above the decimal point and bring down another zero.  \n Now I have 31000.  \n How many times does 11111 go into 31000?  \n Ah, now I can see that it goes in twice, so I'll write a 2 above the decimal point and subtract 22222 from 31000 to get 8778.  \n I'll bring down another zero and ask, how many times does 11111 go into 87780?  \n It goes in seven times, so I'll write a 7 above the decimal point and subtract 77777 from 87780 to get 10003.  \n I'll bring down another zero and ask, how many times does 11111 go into 100030?  \n It goes in nine times, so I'll write a 9 above the decimal point and subtract 99999 from 100030 to get 31.  \n Wait a minute, I'm back to where I started! That means the decimal will repeat from here on.  \n So I'll put a bar over the 279 to indicate that it repeats indefinitely. ERROR  \n The decimal is  $0.00279$  with a bar over 279.  \n The question asks how many digits repeat in this repeating decimal.  \n I can see that there are three digits that repeat: 2, 7, and 9.  \n So the answer is 3.  \n Answer: 3Problem 12. Generator pass-rate: 9.1%. In step 4, the generator falsely claims that the sequence repeats itself every 12 terms, when it's in fact every 10 terms. This sort of counting mistake occasionally fools the reward model.\n\nGiven that\n\n$$\\begin{aligned}x_1 &= 211, \\\\x_2 &= 375, \\\\x_3 &= 420, \\\\x_4 &= 523, \\text{ and} \\\\x_n &= x_{n-1} - x_{n-2} + x_{n-3} - x_{n-4} \\text{ when } n \\geq 5,\\end{aligned}$$\n\nfind the value of  $x_{531} + x_{753} + x_{975}$ .\n\nThis is a problem involving a recursive sequence, where each term depends on the previous four terms.\n\nOne way to approach this problem is to look for a pattern or a formula that can help us find any term of the sequence without having to compute all the previous terms.\n\nTo do that, let's write down the first few terms of the sequence and see if we notice anything:\n\n$$\\begin{aligned}x_1 &= 211, \\\\x_2 &= 375, \\\\x_3 &= 420, \\\\x_4 &= 523, \\\\x_5 &= x_4 - x_3 + x_2 - x_1 = 523 - 420 + 375 - 211 = 267, \\\\x_6 &= x_5 - x_4 + x_3 - x_2 = 267 - 523 + 420 - 375 = -211, \\\\x_7 &= x_6 - x_5 + x_4 - x_3 = -211 - 267 + 523 - 420 = -375, \\\\x_8 &= x_7 - x_6 + x_5 - x_4 = -375 - (-211) + 267 - 523 = -420, \\\\x_9 &= x_8 - x_7 + x_6 - x_5 = -420 - (-375) + (-211) - 267 = -523, \\\\x_{10} &= x_9 - x_8 + x_7 - x_6 = -523 - (-420) + (-375) - (-211) = -267, \\\\x_{11} &= x_{10} - x_9 + x_8 - x_7 = -267 - (-523) + (-420) - (-375) = 211, \\\\x_{12} &= x_{11} - x_{10} + x_9 - x_8 = 211 - (-267) + (-523) - (-420) = 375, \\\\x_{13} &= x_{12} - x_{11} + x_{10} - x_9 = 375 - 211 + (-267) - (-523) = 420, \\\\x_{14} &= x_{13} - x_{12} + x_{11} - x_{10} = 420 - 375 + 211 - (-267) = 523.\\end{aligned}$$\n\nWe can see that the sequence repeats itself every 12 terms, starting from  $x_{14}$  ERROR\n\nThis means that we can find any term of the sequence by finding its remainder when divided by 12, and then looking up the corresponding term in the first cycle.\n\nFor example, to find  $x_{531}$ , we can divide 531 by 12 and get a quotient of 44 and a remainder of 3.\n\nThis means that  $x_{531}$  is the same as  $x_3$ , which is 420.\n\nSimilarly, we can find  $x_{753}$  and  $x_{975}$  by dividing them by 12 and looking up their remainders.\n\nWe get that  $x_{753}$  has a remainder of 9, so it is the same as  $x_9$ , which is -523.\n\nAnd  $x_{975}$  has a remainder of 3, so it is the same as  $x_3$ , which is 420.\n\nTherefore, the value of  $x_{531} + x_{753} + x_{975}$  is  $420 + (-523) + 420 = 317$ .\n\nAnswer: 317\n",
    "durationMs": 755,
    "url": "https://huggingface.co/papers/2305.20050"
  },
  "sourceToolAssistantUUID": "95c45704-4556-46ba-839c-f48aa3dc6e7b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-27 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "8cd701de-3f6c-4d41-b395-fa538fe274bd",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze OpenAI's process reward models paper",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd"
}
```

---

### Tool result

_source line 36 · 2026-05-27T15:23:04.842Z_

<details><summary>↩ Tool result · `toolu_01M6kSTMTsvWpw4teapFsD9D`</summary>

```text
I've searched through the provided web page content carefully, but I cannot find any paper titled "Let's Verify Step by Step" or its associated OpenReview forum ID and review notes.

The content includes various papers with "step" in their titles from different conferences (ICLR, NeurIPS, ACL), but none match the specific paper you're asking about. To locate this paper and its reviews, you would need to:

1. Search directly on OpenReview.net
2. Check the paper's official conference proceedings page
3. Verify the exact title spelling and author information

If you have additional details about the paper (authors, conference, year), I'd be happy to help search through relevant content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6163e674-cbb5-4625-bd92-8870757224db",
  "isSidechain": false,
  "promptId": "847a487e-d454-4fe9-b1b6-24705f0c37b0",
  "type": "user",
  "uuid": "096c99fc-cf84-47a2-992c-f60515f29d7f",
  "toolUseResult": {
    "bytes": 118893,
    "code": 200,
    "codeText": "OK",
    "result": "I've searched through the provided web page content carefully, but I cannot find any paper titled \"Let's Verify Step by Step\" or its associated OpenReview forum ID and review notes.\n\nThe content includes various papers with \"step\" in their titles from different conferences (ICLR, NeurIPS, ACL), but none match the specific paper you're asking about. To locate this paper and its reviews, you would need to:\n\n1. Search directly on OpenReview.net\n2. Check the paper's official conference proceedings page\n3. Verify the exact title spelling and author information\n\nIf you have additional details about the paper (authors, conference, year), I'd be happy to help search through relevant content.",
    "durationMs": 6156,
    "url": "https://api.openreview.net/notes/search?query=Let%27s+Verify+Step+by+Step&source=forum&limit=50"
  },
  "sourceToolAssistantUUID": "6163e674-cbb5-4625-bd92-8870757224db",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 37 · 2026-05-27T15:23:04.845Z_

```json
{
  "parentUuid": "096c99fc-cf84-47a2-992c-f60515f29d7f",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "a5593b1d-6f2a-4cbe-a39b-1c8da9b76bb6",
  "timestamp": "2026-05-27T15:23:04.845Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 38 · 2026-05-27T15:23:07.652Z_

The paper content was saved. Let me read the full extracted text:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5593b1d-6f2a-4cbe-a39b-1c8da9b76bb6",
  "isSidechain": false,
  "requestId": "req_011CbTJYVt1PgkhpVPnta1J6",
  "type": "assistant",
  "uuid": "785e385f-6f74-43b3-96bc-e5b0f4f8fd69",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Be9BTmmqQ69gaaxZexrpob",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 458,
      "cache_creation_input_tokens": 804,
      "cache_read_input_tokens": 16473,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 804,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 458,
          "output_tokens": 143,
          "cache_read_input_tokens": 16473,
          "cache_creation_input_tokens": 804,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 804
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

_source line 39 · 2026-05-27T15:23:08.101Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KEaoei2T6ohdq6qUi9dCLE`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/2d2f5f70-a94f-402d-8c92-8c562e7598cd/tool-results/toolu_01E4nuwrRycqiA7GsnaaPNGX.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "785e385f-6f74-43b3-96bc-e5b0f4f8fd69",
  "isSidechain": false,
  "requestId": "req_011CbTJYVt1PgkhpVPnta1J6",
  "type": "assistant",
  "uuid": "50a4ea63-f2ea-4bbf-88d4-1664a72d1614",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Be9BTmmqQ69gaaxZexrpob",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 458,
      "cache_creation_input_tokens": 804,
      "cache_read_input_tokens": 16473,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 804,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 458,
          "output_tokens": 143,
          "cache_read_input_tokens": 16473,
          "cache_creation_input_tokens": 804,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 804
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

_source line 40 · 2026-05-27T15:23:08.444Z_

<details><summary>↩ Tool result · `toolu_01KEaoei2T6ohdq6qUi9dCLE`</summary>

```text
1	# Let’s Verify Step by Step
2	
3	Hunter Lightman\*    Vineet Kosaraju\*    Yura Burda\*    Harri Edwards  
4	 Bowen Baker    Teddy Lee    Jan Leike    John Schulman    Ilya Sutskever  
5	 Karl Cobbe\*  
6	 OpenAI
7	
8	## Abstract
9	
10	In recent years, large language models have greatly improved in their ability to perform complex multi-step reasoning. However, even state-of-the-art models still regularly produce logical mistakes. To train more reliable models, we can turn either to outcome supervision, which provides feedback for a final result, or process supervision, which provides feedback for each intermediate reasoning step. Given the importance of training reliable models, and given the high cost of human feedback, it is important to carefully compare the both methods. Recent work has already begun this comparison, but many questions still remain. We conduct our own investigation, finding that process supervision significantly outperforms outcome supervision for training models to solve problems from the challenging MATH dataset. Our process-supervised model solves 78% of problems from a representative subset of the MATH test set. Additionally, we show that active learning significantly improves the efficacy of process supervision. To support related research, we also release PRM800K, the complete dataset of 800,000 step-level human feedback labels used to train our best reward model.
11	
12	## 1 Introduction
13	
14	Large language models are capable of solving tasks that require complex multi-step reasoning by generating solutions in a step-by-step chain-of-thought format (Nye et al., 2021; Wei et al., 2022; Kojima et al., 2022). However, even state-of-the-art models are prone to producing falsehoods — they exhibit a tendency to invent facts in moments of uncertainty (Bubeck et al., 2023). These *hallucinations* (Maynez et al., 2020) are particularly problematic in domains that require multi-step reasoning, since a single logical error is enough to derail a much larger solution. Detecting and mitigating hallucinations is essential to improve reasoning capabilities.
15	
16	---
17	
18	\*Primary authors. Correspondence to: Karl Cobbe &lt;karl@openai.com>One effective method involves training reward models to discriminate between desirable and undesirable outputs. The reward model can then be used in a reinforcement learning pipeline (Ziegler et al., 2019; Stiennon et al., 2020; Nakano et al., 2021; Ouyang et al., 2022) or to perform search via rejection sampling (Nichols et al., 2020; Shen et al., 2021; Cobbe et al., 2021). While these techniques are useful, the resulting system is only as reliable as the reward model itself. It is therefore important that we study how to most effectively train reliable reward models.
19	
20	In closely related work, Uesato et al. (2022) describe two distinct methods for training reward models: outcome supervision and process supervision. Outcome-supervised reward models (ORMs) are trained using only the final result of the model’s chain-of-thought, while process-supervised reward models (PRMs) receive feedback for each step in the chain-of-thought. There are compelling reasons to favor process supervision. It provides more precise feedback, since it specifies the exact location of any errors that occur. It also has several advantages relevant to AI alignment: it is easier for humans to interpret, and it more directly rewards models for following a human-endorsed chain-of-thought. Within the domain of logical reasoning, models trained with outcome supervision regularly use incorrect reasoning to reach the correct final answer (Zelikman et al., 2022; Creswell et al., 2022). Process supervision has been shown to mitigate this misaligned behavior (Uesato et al., 2022).
21	
22	Despite these advantages, Uesato et al. (2022) found that outcome supervision and process supervision led to similar final performance in the domain of grade school math. We conduct our own detailed comparison of outcome and process supervision, with three main differences: we use a more capable base model, we use significantly more human feedback, and we train and test on the more challenging MATH dataset (Hendrycks et al., 2021).
23	
24	Our main contributions are as follows:
25	
26	1. 1. We show that process supervision can train much more reliable reward models than outcome supervision. We use our state-of-the-art PRM to solve 78.2% of problems from a representative subset of the MATH test set.
27	2. 2. We show that a large reward model can reliably approximate human supervision for smaller reward models, and that it can be used to efficiently conduct large-scale data collection ablations.
28	3. 3. We show that active learning leads to a  $2.6\times$  improvement in the data efficiency of process supervision.
29	4. 4. We release our full process supervision dataset, PRM800K, to promote related research.## 2 Methods
30	
31	We perform a comparison of outcome and process supervision, following a similar methodology to Uesato et al. (2022). Outcome supervision can be provided without humans, since all problems in the MATH dataset have automatically checkable answers. In contrast, there is no simple way to automate process supervision. We therefore rely on human data-labelers to provide process supervision, specifically by labelling the correctness of each step in model-generated solutions.
32	
33	We conduct experiments in two separate regimes: large-scale and small-scale. Each has its own advantages, and they offer complimentary perspectives. At large-scale, we finetune all models from GPT-4 (OpenAI, 2023). We focus on advancing the state-of-the-art by training the most reliable ORM and PRM possible. Unfortunately the training sets for these reward models are not directly comparable, for reasons we will discuss in Section 3. These models are therefore not ideal for making an apples-to-apples comparison of outcome and process supervision. To address this flaw, we also train models at small-scale, where we can conduct a more direct comparison. In order to remove our dependence on costly human feedback, we use a large-scale model to supervise small-scale model training. This setup enables us to conduct several important ablations that would otherwise be infeasible.
34	
35	### 2.1 Scope
36	
37	At each model scale, we use a single fixed model to generate all solutions. We call this model the *generator*. We do not attempt to improve the generator with reinforcement learning (RL). When we discuss outcome and process supervision, we are specifically referring to the supervision given to the reward model. We do not discuss any supervision the generator would receive from the reward model if trained with RL. Although finetuning the generator with RL is a natural next step, it is intentionally not the focus of this work.
38	
39	We instead focus exclusively on how to train the most reliable reward model possible. We evaluate a reward model by its ability to perform best-of-N search over uniformly sampled solutions from the generator. For each test problem we select the solution ranked highest by the reward model, automatically grade it based on its final answer, and report the fraction that are correct. A reward model that is more reliable will select the correct solution more often.
40	
41	### 2.2 Base Models
42	
43	All large-scale models are finetuned from the base GPT-4 model (OpenAI, 2023). This model has been pretrained solely to predict the next token; it has not been pretrained with any Reinforcement Learning from Human Feedback (RLHF) (Christiano et al., 2017). The small-scale base models are similar in design to GPT-4, but they were pretrained with roughly 200 times less compute. As an additional pretraining step, we finetune all models on a dataset of roughly 1.5BThe denominator of a fraction is 7 less than 3 times the numerator. If the fraction is equivalent to  $2/5$ , what is the numerator of the fraction? (Answer: )
44	
45	😞 😊 😊 Let's call the numerator  $x$ .
46	
47	😞 😊 😊 So the denominator is  $3x-7$ .
48	
49	😞 😊 😊 We know that  $x/(3x-7) = 2/5$ .
50	
51	😞 😊 😊 So  $5x = 2(3x-7)$ .
52	
53	😞 😊 😊  $5x = 6x - 14$ .
54	
55	😞 😊 😊 So  $x = 7$ .
56	
57	Figure 1: A screenshot of the interface used to collect feedback for each step in a solution.
58	
59	math-relevant tokens, which we call MathMix. Similar to Lewkowycz et al. (2022), we find that this improves the model’s mathematical reasoning capabilities. Details on how this dataset was constructed can be found in Appendix A.
60	
61	## 2.3 Generator
62	
63	To make parsing individual steps easier, we train the generator to produce solutions in a newline delimited step-by-step format. Specifically, we few-shot generate solutions to MATH training problems, filter to those that reach the correct final answer, and finetune the base model on this dataset for a single epoch. This step is not intended to teach the generator new skills; it is intended only to teach the generator to produce solutions in the desired format.
64	
65	## 2.4 Data Collection
66	
67	To collect process supervision data, we present human data-labelers with step-by-step solutions to MATH problems sampled by the large-scale generator. Their task is to assign each step in the solution a label of *positive*, *negative*, or *neutral*, as shown in Figure 1. A positive label indicates that the step is correct and reasonable. A negative label indicates that the step is either incorrect or unreasonable. A neutral label indicates ambiguity. In practice, a step may be labelled neutral if it is subtly misleading, or if it is a poor suggestion that is technically still valid. We permit neutral labels since this allows us to defer the decision about how to handle ambiguity: at test time, we can treat neutral labels as either positive or negative. A more detailed description of the labelling instructions is provided in Appendix D.
68	
69	We label solutions exclusively from the large-scale generator in order to maximize the value of our limited human-data resource. We refer to the entire dataset of step-level labels collected as PRM800K. The PRM800K training set contains 800K step-level labels across 75K solutions to 12K problems. Tominimize overfitting, we include data from 4.5K MATH test problems in the PRM800K training set, and we therefore evaluate our models only on the remaining 500 MATH test problems. More details about this test set can be found in Appendix C.
70	
71	During data collection, we must decide which solutions to surface to data-labelers. The most straightforward strategy is to uniformly surface solutions produced by the generator. However, if we surface solutions that make obvious errors, the human feedback we get is less valuable. We would prefer to surface solutions that are more likely to fool our best reward model. To that end, we attempt to strategically select which solutions to show data-labelers. Specifically, we choose to surface *convincing wrong-answer* solutions. We use the term *convincing* to refer to solutions that are rated highly by our current best PRM, and we use *wrong-answer* to refer to solutions that reach an incorrect final answer. We use this slightly verbose phrasing to emphasize the fact that correctness is determined solely by checking the final answer, a process which occasionally leads to misgraded solutions. We expect to gain more information from labeling convincing wrong-answer solutions, since we know the PRM is mistaken about at least one step in each such solution.
72	
73	In addition to using this selection strategy, we also iteratively re-train our PRM using the latest data at several points in the data collection process. At each iteration, we generate  $N$  solutions per problem and surface only the top  $K$  most convincing wrong-answer solutions to data-labelers. We experiment with either applying this top- $K$  filtering at a problem level ( $K$  solutions per problem) or globally across the dataset ( $K$  solutions in total, unequally distributed among problems). Since the data collection process is expensive, it was not feasible to conduct at-scale ablations of these decisions. However, we perform several surrogate ablations in Section 4, using our largest PRM as a labelling oracle for a smaller PRM. More details about data collection can be found in Appendix B.
74	
75	## 2.5 Outcome-supervised Reward Models (ORMs)
76	
77	We train ORMs following a similar methodology to Cobbe et al. (2021). We uniformly sample a fixed number of solutions per problem from the generator, and we train the ORM to predict whether each solution is correct or incorrect. In practice, we usually determine correctness by automatically checking the final answer, but in principle these labels could be provided by humans. At test time, we use the ORM’s prediction at the final token as the overall score for the solution. We note the automatic grading used to determine ORM targets is not perfectly reliable: *false positives* solutions that reach the correct answer with incorrect reasoning will be misgraded. We discuss additional ORM training details in Appendix E.
78	
79	## 2.6 Process-supervised Reward Models (PRMs)
80	
81	We train PRMs to predict the correctness of each step after the last token in each step. This prediction takes the form of a single token, and we maximize theLet  $x^8 + 3x^4 - 4 = p_1(x)p_2(x) \cdots p_k(x)$ , where each non-constant polynomial  $p_i(x)$  is monic with integer coefficients, and cannot be factored further over the integers. Compute  $p_1(1) + p_2(1) + \cdots + p_k(1)$ .
82	
83	I notice that the given polynomial has even degree and only even powers of  $x$ , so I can try to make a substitution to simplify it.
84	
85	Let  $y = x^4$ , then the polynomial becomes  $y^2 + 3y - 4$ , which is a quadratic equation.
86	
87	I can factor this quadratic equation as  $(y + 4)(y - 1)$ , so the original polynomial is  $(x^4 + 4)(x^4 - 1)$ .
88	
89	Now I need to factor each of these factors further, if possible, over the integers.
90	
91	For the first factor,  $x^4 + 4$ , I recall the Sophie Germain identity, which says that  $a^4 + 4b^4 = (a^2 + 2b^2 + 2ab)(a^2 + 2b^2 - 2ab)$ .
92	
93	Applying this identity with  $a = x$  and  $b = 1$ , I get  $x^4 + 4 = (x^2 + 2x + 2)(x^2 - 2x + 2)$ .
94	
95	For the second factor,  $x^4 - 1$ , I can use the difference of squares formula, which says that  $a^2 - b^2 = (a + b)(a - b)$ .
96	
97	Applying this formula with  $a = x^2$  and  $b = 1$ , I get  $x^4 - 1 = (x^2 + 1)(x^2 - 1)$ .
98	
99	Then I can apply the difference of squares formula again with  $a = x$  and  $b = 1$ , to get  $x^2 - 1 = (x + 1)(x - 1)$ .
100	
101	So the original polynomial is  $(x^4 + 4)(x^4 - 1) = (x^2 + 2x + 2)(x^2 - 2x + 2)(x^2 + 1)(x + 1)(x - 1)$ .
102	
103	These are all the irreducible factors over the integers, so  $p_1(x) = x^2 + 2x + 2$ ,  $p_2(x) = x^2 - 2x + 2$ ,  $p_3(x) = x^2 + 1$ ,  $p_4(x) = x + 1$ , and  $p_5(x) = x - 1$ .
104	
105	To find the sum of their values at  $x = 1$ , I just need to plug in  $x = 1$  into each factor and add them up.
106	
107	I get  $p_1(1) = 1^2 + 2 \cdot 1 + 2 = 5$ ,  $p_2(1) = 1^2 - 2 \cdot 1 + 2 = 1$ ,  $p_3(1) = 1^2 + 1 = 2$ ,  $p_4(1) = 1 + 1 = 2$ , and  $p_5(1) = 1 - 1 = 0$ .
108	
109	So the final answer is  $5 + 1 + 2 + 2 + 0 = 10$ .
110	
111	Answer: 10
112	
113	Let  $x^8 + 3x^4 - 4 = p_1(x)p_2(x) \cdots p_k(x)$ , where each non-constant polynomial  $p_i(x)$  is monic with integer coefficients, and cannot be factored further over the integers. Compute  $p_1(1) + p_2(1) + \cdots + p_k(1)$ .
114	
115	This problem is about factoring a polynomial over the integers, which can be a tricky task.
116	
117	One possible strategy is to look for rational roots of the polynomial, using the rational root theorem.
118	
119	However, that would involve checking a lot of possible factors of  $-4$ , and there is no guarantee that the polynomial has any rational roots at all.
120	
121	Another possible strategy is to use some algebraic tricks to simplify the polynomial or reduce its degree.
122	
123	I notice that the polynomial has only even powers of  $x$ , so I can try to substitute  $y = x^2$  and see what happens.
124	
125	Then the polynomial becomes  $y^4 + 3y^2 - 4$ , which is a quadratic equation in  $y^2$ .
126	
127	I can try to factor this quadratic equation by looking for two numbers that multiply to  $-4$  and add to  $3$ .
128	
129	Those numbers are  $4$  and  $-1$ , so I can write  $y^4 + 3y^2 - 4 = (y^2 + 4)(y^2 - 1)$ .
130	
131	Now I can substitute back  $x^2 = y$  and get  $x^8 + 3x^4 - 4 = (x^4 + 4)(x^4 - 1)$ .
132	
133	This looks promising, because I have reduced the degree of the factors from  $8$  to  $4$ .
134	
135	I can try to factor each of these factors further, using the difference of squares formula.
136	
137	I get  $x^8 + 3x^4 - 4 = (x^4 + 4)(x^2 - 2)(x^2 + 1)(x^2 - 1)$ .
138	
139	I can apply the difference of squares formula again to the last factor and get  $x^8 + 3x^4 - 4 = (x^4 + 4)(x^2 - 2)(x^2 + 1)(x + 1)(x - 1)$ .
140	
141	Now I have factored the polynomial completely into monic linear and quadratic factors with integer coefficients.
142	
143	These are the  $p_i(x)$ 's that the problem is asking for.
144	
145	To find the sum of their values at  $x = 1$ , I just need to plug in  $x = 1$  into each factor and add them up.
146	
147	I get  $p_1(1) + p_2(1) + \cdots + p_5(1) = (1^4 + 4)(1^2 - 2)(1^2 + 1)(1 + 1)(1 - 1)$ .
148	
149	Simplifying, I get  $p_1(1) + p_2(1) + \cdots + p_5(1) = (5)(-1)(2)(2)(0)$ .
150	
151	Multiplying, I get  $p_1(1) + p_2(1) + \cdots + p_5(1) = 0$ .
152	
153	Answer: 0
154	
155	Figure 2: Two solutions to the same problem, graded by the PRM. The solution on the left is correct while the solution on the right is incorrect. A green background indicates a high PRM score, and a red background indicates a low score. The PRM correctly identifies the mistake in the incorrect solution.
156	
157	log-likelihood of these target tokens during training. The PRM can therefore be trained in a standard language model pipeline without any special accommodations. To determine the step-level predictions at test time, it suffices to perform a single PRM forward pass over the whole solution. We visualize large-scale PRM scores for two different solutions in Figure 2. To compare multiple solutions, it is necessary to compute a single score for each solution. This is an important but straightforward detail: we define the PRM score for a solution to be the probability that every step is correct under the PRM. We implement this as the product of the correctness probabilities for each step. We describe other possible scoring strategies and additional PRM training details in Appendix F.
158	
159	When we provide process supervision, we deliberately choose to supervise only up to the first incorrect step. This makes the comparison between outcome and process supervision more straightforward. For correct solutions, both methods provide the same information, namely that every step is correct. For incorrect solutions, both methods reveal the existence of at least one mistake, and process supervision additionally reveals the precise location of that mistake. If we were to provide additional process supervision beyond the first mistake, then process supervision would have an even greater information advantage. This decision also keeps the labelling cost similar for humans: without relying on an easy-to-check final answer, determining the correctness of a solution is equivalent to identifying its first mistake. While most MATH problems do have easy-to-check final answers, we expect this to not remain true in more complex domains.&lt;table border="1">
160	&lt;thead>
161	&lt;tr>
162	&lt;th>&lt;/th>
163	&lt;th>ORM&lt;/th>
164	&lt;th>PRM&lt;/th>
165	&lt;th>Majority Voting&lt;/th>
166	&lt;/tr>
167	&lt;/thead>
168	&lt;tbody>
169	&lt;tr>
170	&lt;td>% Solved (Best-of-1860)&lt;/td>
171	&lt;td>72.4&lt;/td>
172	&lt;td>&lt;b>78.2&lt;/b>&lt;/td>
173	&lt;td>69.6&lt;/td>
174	&lt;/tr>
175	&lt;/tbody>
176	&lt;/table>
177	
178	Figure 3: A comparison of outcome-supervised and process-supervised reward models, evaluated by their ability to search over many test solutions. Majority voting is shown as a strong baseline. For  $N \leq 1000$ , we visualize the variance across many subsamples of the 1860 solutions we generated in total per problem.
179	
180	### 3 Large-scale Supervision
181	
182	We train the large-scale PRM using the step-level labels in PRM800K. To ensure the large-scale ORM baseline is as strong as possible, we train on 100 uniform samples per problem from the generator. This means the ORM training set has no overlap with PRM800K, and it is an order of magnitude larger. Although these two training sets are not directly comparable, each represents our best attempt to advance the state-of-the-art with each form of supervision. We note that training the ORM solely on PRM800K solutions would be problematic, since our active learning strategy has heavily biased the dataset towards wrong-answer solutions. We did explore training the ORM on a superset of PRM800K solutions, by mixing in uniformly sampled solutions, but we found that this did not improve ORM performance.
183	
184	Figure 3 shows how the best-of-N performance of each reward model varies as a function of N. Since majority voting is known to be a strong baseline (Wang et al., 2022; Lewkowycz et al., 2022), we also include this method as a point of comparison. While the ORM performs slightly better than the majority voting baseline, the PRM strongly outperforms both. Not only does the PRM reach higher performance for all values of N, but the performance gap widens as N increases. This indicates that the PRM is more effective than both the ORM and majority voting at searching over a large number of model-generated solutions.(a) Four series of reward models trained using different data collection strategies, compared across training sets of varying sizes.
185	
186	(b) Three reward models trained on 200 samples/problem using different forms of supervision, compared across many test-time compute budgets.
187	
188	Figure 4: A comparison of different forms of outcome and process supervision. Mean and standard deviation is shown across three seeds.
189	
190	We experimented with using RM-weighted voting (Li et al., 2022; Uesato et al., 2022) to combine the benefits of the PRM and majority voting, but this did not noticeably improve performance. We use a specific subset of the MATH test set for evaluation, which we describe in Appendix C. We further break down these results by problem difficulty in Appendix G.
191	
192	## 4 Small-scale Synthetic Supervision
193	
194	We find that the PRM outperforms the ORM at large-scale, but this result alone paints an incomplete picture. To better compare outcome and process supervision, there are two confounding factors that must be isolated. First, the training sets for the ORM and the PRM are not directly comparable: the PRM training set was constructed using active learning, is biased towards answer-incorrect solutions, and is an order of magnitude smaller. Second, the final-answer grading will provide positive labels to spurious solutions that reach the correct final answer despite incorrect reasoning. This could damage ORM performance, an effect we may or may not want to attribute to outcome supervision more generally.
195	
196	Due to the high cost of collecting human feedback, we cannot easily ablate these factors using human labelers. We instead perform the relevant ablations by using the large-scale PRM to supervise smaller models. This setup enables us to simulate a large amount of data collection at a modest cost. For the remainder of this section, we refer to the large-scale PRM from Section 3 as PRM&lt;sub>large&lt;/sub>.## 4.1 Process vs Outcome Supervision
197	
198	We now conduct a direct comparison of outcome and process supervision. We first sample between 1 and 200 solutions per problem from a small-scale generator. For each dataset, we provide three forms of supervision: process supervision from  $\text{PRM}_{\text{large}}$ , outcome supervision from  $\text{PRM}_{\text{large}}$ , and outcome supervision from final-answer checking. The choice of supervision is the only difference between these three series of reward models, which are otherwise trained on identical datasets. See Appendix H for more details about how  $\text{PRM}_{\text{large}}$  is used for outcome and process supervision.
199	
200	In Figure 4a, we evaluate each reward model by its best-of-500 selection. We see that process supervision significantly outperforms both forms of outcome supervision at all data collection scales. In Figure 4b, we evaluate the best reward model from each series by its best-of-N performance across different values of N. We see that using  $\text{PRM}_{\text{large}}$  for outcome supervision is noticeably more effective than final-answer checking. This can be explained by the fact that  $\text{PRM}_{\text{large}}$  provides better supervision for solutions that reach the correct final answer using incorrect reasoning.
201	
202	It is not clear whether supervision by  $\text{PRM}_{\text{large}}$  or by final-answer checking represents the more appropriate outcome supervision baseline. While final-answer supervision is more explicitly outcome based, its main weakness — the existence of false positives — is arguably over-emphasized in the MATH dataset. Outcome supervision by  $\text{PRM}_{\text{large}}$  better represents outcome supervision in domains that are less susceptible to false positives. We consider outcome supervision by  $\text{PRM}_{\text{large}}$  to be the more relevant baseline, but we encourage the reader to draw their own conclusions.
203	
204	## 4.2 Active Learning
205	
206	Finally, we investigate the impact of active learning. We train a small-scale reward model,  $\text{PRM}_{\text{selector}}$ , on a single sample from each problem, and we use this model to score 1000 samples per problem. To train each of our larger reward models, we select  $N$  samples per problem such that 80% are the most convincing (according to  $\text{PRM}_{\text{selector}}$ ) wrong-answer samples, and 20% are the most convincing samples that remain (right- or wrong-answer). We score the selected samples with  $\text{PRM}_{\text{large}}$  and train on those scores. This process ensures that all samples are relatively convincing under  $\text{PRM}_{\text{selector}}$ , that a large fraction are known to contain at least one mistake, and that our overall dataset is not too heavily biased toward wrong-answer solutions. Performance of this data labelling scheme is shown in Figure 4a. By comparing the slopes of the line of best fit with and without active learning, we estimate that this form of active learning is approximately 2.6x more data efficient than uniform data labelling. We note that the model trained on the largest active learning dataset (200 samples per problem) appears to slightly underperform the expected trend line. Our best explanation for this observation is that 200 samples represents a significant fraction of the overall selection pool (1000 samples) and that this&lt;table border="1">
207	&lt;thead>
208	&lt;tr>
209	&lt;th>&lt;/th>
210	&lt;th>ORM&lt;/th>
211	&lt;th>PRM&lt;/th>
212	&lt;th>Majority Vote&lt;/th>
213	&lt;th># Problems&lt;/th>
214	&lt;/tr>
215	&lt;/thead>
216	&lt;tbody>
217	&lt;tr>
218	&lt;td>AP Calculus&lt;/td>
219	&lt;td>68.9%&lt;/td>
220	&lt;td>&lt;b>86.7%&lt;/b>&lt;/td>
221	&lt;td>80.0%&lt;/td>
222	&lt;td>45&lt;/td>
223	&lt;/tr>
224	&lt;tr>
225	&lt;td>AP Chemistry&lt;/td>
226	&lt;td>68.9%&lt;/td>
227	&lt;td>&lt;b>80.0%&lt;/b>&lt;/td>
228	&lt;td>71.7%&lt;/td>
229	&lt;td>60&lt;/td>
230	&lt;/tr>
231	&lt;tr>
232	&lt;td>AP Physics&lt;/td>
233	&lt;td>77.8%&lt;/td>
234	&lt;td>&lt;b>86.7%&lt;/b>&lt;/td>
235	&lt;td>82.2%&lt;/td>
236	&lt;td>45&lt;/td>
237	&lt;/tr>
238	&lt;tr>
239	&lt;td>AMC10/12&lt;/td>
240	&lt;td>49.1%&lt;/td>
241	&lt;td>&lt;b>53.2%&lt;/b>&lt;/td>
242	&lt;td>32.8%&lt;/td>
243	&lt;td>84&lt;/td>
244	&lt;/tr>
245	&lt;tr>
246	&lt;td>Aggregate&lt;/td>
247	&lt;td>63.8%&lt;/td>
248	&lt;td>&lt;b>72.9%&lt;/b>&lt;/td>
249	&lt;td>61.3%&lt;/td>
250	&lt;td>234&lt;/td>
251	&lt;/tr>
252	&lt;/tbody>
253	&lt;/table>
254	
255	Table 1: We measure out-of-distribution generalization using recent STEM tests. We evaluate the outcome-supervised RM, the process-supervised RM, and majority voting using 100 test samples per problem.
256	
257	relative lack of diversity limits the possible upside from active learning.
258	
259	We also performed a preliminary investigation into the impact of iteratively retraining  $\text{PRM}_{\text{selector}}$  throughout data collection. Between iterations, we retrained  $\text{PRM}_{\text{selector}}$  using all currently labeled data. Unfortunately, we observed instability in this process which we were unable to diagnose. The resulting reward models performed no better than the models described above. We expect some form of iterative retraining to be beneficial in active learning, but we currently have no concrete evidence to support this claim. We consider this a compelling direction for future research.
260	
261	## 5 OOD Generalization
262	
263	To get some measure of out-of-distribution generalization, we evaluate our large-scale ORM and PRM on a held-out set of 224 STEM questions, pulled from the most recent AP Physics, AP Calculus, AP Chemistry, AMC10, and AMC12 exams. Since these tests were released after the pre-training dataset was compiled, we can have high confidence that the model has not seen these problems. We report the best-of-100 performance of the ORM, PRM and majority voting in Table 1. We observe results similar to those in Section 3: the PRM outperforms both the ORM and majority voting. This shows us that the PRM can tolerate a modest amount of distribution shift and that its strong performance holds up on fresh test questions.
264	
265	## 6 Discussion
266	
267	### 6.1 Credit Assignment
268	
269	One clear advantage of process supervision is that it provides more precise feedback than outcome supervision. A reward model trained with outcome supervision faces a difficult credit-assignment task — to generalize well, it must determine where an incorrect solution went wrong. This is particularly difficult for hard problems: most model-generated solutions contain an error somewhere, so the marginal value of a negative label from outcome supervision is low. Incontrast, process supervision provides a richer signal: it specifies both how many of the first steps were in fact correct, as well as the precise location of the incorrect step. Process supervision makes credit assignment easier, and we believe that this explains its strong performance.
270	
271	## 6.2 Alignment Impact
272	
273	Process supervision has several advantages over outcome supervision related to AI alignment. Process supervision is more likely to produce interpretable reasoning, since it encourages models to follow a process endorsed by humans. Process supervision is also inherently safer: it directly rewards an aligned chain-of-thought rather than relying on outcomes as a proxy for aligned behavior (Stuhlmüller and Byun, 2022). In contrast, outcome supervision is harder to scrutinize, and the preferences conveyed are less precise. In the worst case, the use of outcomes as an imperfect proxy could lead to models that become misaligned after learning to exploit the reward signal (Uesato et al., 2022; Cotra, 2022; Everitt et al., 2017).
274	
275	In some cases, safer methods for AI systems can lead to reduced performance (Ouyang et al., 2022; Askell et al., 2021), a cost which is known as an alignment tax. In general, any alignment tax may hinder the adoption of alignment methods, due to pressure to deploy the most capable model. Our results show that process supervision in fact incurs a negative alignment tax. This could lead to increased adoption of process supervision, which we believe would have positive alignment side-effects. It is unknown how broadly these results will generalize beyond the domain of math, and we consider it important for future work to explore the impact of process supervision in other domains.
276	
277	## 6.3 Test Set Contamination
278	
279	The test set of the MATH dataset contains problems that are discussed in several online venues, and it is likely that some of these problems appear in the pretraining dataset for our models. We attempted to remove all MATH problems from our MathMix dataset using string-matching heuristics, but since humans can post hard-to-detect rephrasings of a problem online, it is difficult to make any strong guarantees about the overlap between MathMix and the MATH dataset.
280	
281	In our experience inspecting model-generated solutions, we saw no clear signs of our models memorizing MATH problems. However, it is impossible to rule out subtle forms of memorization that would slip past manual inspection, and it is still possible that some degree of contamination has slightly inflated our performance on the MATH test set. Even in that case, we would expect any contamination to manifest similarly across all methods, and that the relative comparisons made throughout this work would remain mostly unaffected.
282	
283	We also note that the PRM regularly surfaces correct solutions to MATH problems that have a low single-digit percentage solve-rate under the generator, some examples of which can be seen in Appendix I. The generator’s lowsolve-rate is an additional indication that it has not encountered such problems via test set contamination. Our generalization results from Section 5 further strengthen our claim that test set contamination has not significantly impacted this work, since we observe qualitatively similar results on problems that are guaranteed to be uncontaminated.
284	
285	## 7 Related Work
286	
287	### 7.1 Outcome vs Process Supervision
288	
289	In work closely related to our own, Uesato et al. (2022) compare the impact of outcome and process supervision in the domain of grade school math. They found that both methods led to similar final-answer error rates, and that process supervision achieved those results with less data. While our core methodology is very similar, there are three main details that differ. First, we use a more capable model to collect PRM800K dataset and to perform our large-scale experiments. However, our small-scale results in Section 4 suggest that large-scale models are not necessary to observe benefits from process supervision. Second, we evaluate on the MATH dataset, which is significantly more challenging than GSM8K. Third, we collect a much larger quantity of process supervision data.
290	
291	On the surface, the results from Uesato et al. (2022) may seem to conflict with our claim that process supervision leads to better performance. However, we believe the apparent conflict can be explained by the difference in the scale of the supervision. The data scaling trend in Figure 4a suggests that a small amount of process supervision and a large amount of outcome supervision do in fact lead to similar performance, consistent with the results from Uesato et al. (2022). The trend also shows that process supervision beats outcome supervision when scaled up, even when judged based solely on outcomes. This is consistent with our results in Section 3. We believe these results make a strong case for using process supervision.
292	
293	### 7.2 Synthetic Supervision
294	
295	Similar to our work in Section 4, Gao et al. (2022) use a large reward model to supervise the training of smaller models. They study the over-optimization that occurs during RLHF, with experiments that require large quantities of human preference data. To work around this challenge, they use a gold-standard reward model to replace human feedback. Our use of a large-scale reward model to supervise smaller reward models shares similarities with their approach.
296	
297	### 7.3 Natural Language Reasoning
298	
299	Several recent studies that have examined the reasoning ability of large language models are implicitly relevant to our work. Lewkowycz et al. (2022) showed that finetuning models on a large corpus of technical content led to significantly improved performance on MATH. Wang et al. (2022) showed that *self-consistency*leads to remarkably strong performance on many reasoning benchmarks, notably without requiring any additional finetuning. Wei et al. (2022) and Nye et al. (2021) demonstrate the importance of explicitly performing intermediate reasoning steps via a *chain of thought* or a *scratchpad* in order to solve tasks that require multi-step reasoning. Kojima et al. (2022) show that models are able to perform this behavior zero-shot, conditioned only on a simple prompt.
300	
301	## 8 Conclusion
302	
303	We have shown that process supervision can be used to train much more reliable reward models than outcome supervision in the domain of mathematical reasoning. We have also shown that active learning can be used to lower the cost of human data collection by surfacing only the most valuable model completions for human feedback. We release PRM800K, the full dataset of human feedback used to train our state-of-the-art reward model, with the hope that removing this significant barrier to entry will catalyze related research on the alignment of large language models. We believe that process supervision is currently under-explored, and we are excited for future work to more deeply investigate the extent to which these methods generalize.
304	
305	## Acknowledgements
306	
307	We thank Joshua Achiam, Mark Chen, Jonathan Gordon, Dan Hendrycks, Lukasz Kaiser, Oleg Murk, Ben Sokolowsky, Francis Song, and Jonathan Uesato for valuable feedback and thoughtful discussions; Giambattista Parascandolo and Daniel Selsam for their contributions to the MathMix dataset; Jonathan Ward for contributing to the data collection interface; Wojciech Zaremba for encouraging us to scale up data collection; Peter Hoeschele and Aris Kostantinidis for supporting our data collection; the research acceleration and supercomputing teams at OpenAI for providing infrastructure support; and the team at Scale and the many data-labelers who created PRM800K.
308	
309	## References
310	
311	- A. Askell, Y. Bai, A. Chen, D. Drain, D. Ganguli, T. Henighan, A. Jones, N. Joseph, B. Mann, N. DasSarma, et al. A general language assistant as a laboratory for alignment. *arXiv preprint arXiv:2112.00861*, 2021.
312	- S. Bubeck, V. Chandrasekaran, R. Eldan, J. Gehrke, E. Horvitz, E. Kamar, P. Lee, Y. T. Lee, Y. Li, S. Lundberg, et al. Sparks of artificial general intelligence: Early experiments with gpt-4. *arXiv preprint arXiv:2303.12712*, 2023.P. F. Christiano, J. Leike, T. Brown, M. Martic, S. Legg, and D. Amodei. Deep reinforcement learning from human preferences. *Advances in neural information processing systems*, 30, 2017.
313	
314	K. Cobbe, V. Kosaraju, M. Bavarian, M. Chen, H. Jun, L. Kaiser, M. Plappert, J. Tworek, J. Hilton, R. Nakano, et al. Training verifiers to solve math word problems. *arXiv preprint arXiv:2110.14168*, 2021.
315	
316	A. Cotra. Without specific countermeasures, the easiest path to transformative AI likely leads to AI takeover. &lt;https://www.alignmentforum.org/posts/pRkFkzwKZ2zfa3R6H/without-specific-countermeasures-the-easiest-path-to>, 2022.
317	
318	A. Creswell, M. Shanahan, and I. Higgins. Selection-inference: Exploiting large language models for interpretable logical reasoning. *arXiv preprint arXiv:2205.09712*, 2022.
319	
320	T. Everitt, V. Krakovna, L. Orseau, M. Hutter, and S. Legg. Reinforcement learning with a corrupted reward channel. *arXiv preprint arXiv:1705.08417*, 2017.
321	
322	L. Gao, J. Schulman, and J. Hilton. Scaling laws for reward model overoptimization. *arXiv preprint arXiv:2210.10760*, 2022.
323	
324	D. Hendrycks, C. Burns, S. Kadavath, A. Arora, S. Basart, E. Tang, D. Song, and J. Steinhardt. Measuring mathematical problem solving with the math dataset. *arXiv preprint arXiv:2103.03874*, 2021.
325	
326	T. Kojima, S. S. Gu, M. Reid, Y. Matsuo, and Y. Iwasawa. Large language models are zero-shot reasoners. *arXiv preprint arXiv:2205.11916*, 2022.
327	
328	A. Lewkowycz, A. Andreassen, D. Dohan, E. Dyer, H. Michalewski, V. Ramasesh, A. Slone, C. Anil, I. Schlag, T. Gutman-Solo, et al. Solving quantitative reasoning problems with language models. *arXiv preprint arXiv:2206.14858*, 2022.
329	
330	Y. Li, Z. Lin, S. Zhang, Q. Fu, B. Chen, J.-G. Lou, and W. Chen. On the advance of making language models better reasoners. *arXiv preprint arXiv:2206.02336*, 2022.
331	
332	J. Maynez, S. Narayan, B. Bohnet, and R. McDonald. On faithfulness and factuality in abstractive summarization. *arXiv preprint arXiv:2005.00661*, 2020.
333	
334	R. Nakano, J. Hilton, S. Balaji, J. Wu, L. Ouyang, C. Kim, C. Hesse, S. Jain, V. Kosaraju, W. Saunders, et al. Webgpt: Browser-assisted question-answering with human feedback. *arXiv preprint arXiv:2112.09332*, 2021.
335	
336	E. Nichols, L. Gao, and R. Gomez. Collaborative storytelling with large-scale neural language models. In *Proceedings of the 13th ACM SIGGRAPH Conference on Motion, Interaction and Games*, pages 1–10, 2020.M. Nye, A. J. Andreassen, G. Gur-Ari, H. Michalewski, J. Austin, D. Bieber, D. Dohan, A. Lewkowycz, M. Bosma, D. Luan, et al. Show your work: Scratchpads for intermediate computation with language models. *arXiv preprint arXiv:2112.00114*, 2021.
337	
338	OpenAI. Gpt-4 technical report. *arXiv preprint arXiv:2303.08774*, 2023.
339	
340	L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. L. Wainwright, P. Mishkin, C. Zhang, S. Agarwal, K. Slama, A. Ray, et al. Training language models to follow instructions with human feedback. *arXiv preprint arXiv:2203.02155*, 2022.
341	
342	J. Shen, Y. Yin, L. Li, L. Shang, X. Jiang, M. Zhang, and Q. Liu. Generate & rank: A multi-task framework for math word problems. *arXiv preprint arXiv:2109.03034*, 2021.
343	
344	N. Stiennon, L. Ouyang, J. Wu, D. Ziegler, R. Lowe, C. Voss, A. Radford, D. Amodei, and P. F. Christiano. Learning to summarize with human feedback. *Advances in Neural Information Processing Systems*, 33:3008–3021, 2020.
345	
346	A. Stuhlmüller and J. Byun. Supervise process, not outcomes. &lt;https://ought.org/updates/2022-04-06-process>, 2022.
347	
348	J. Uesato, N. Kushman, R. Kumar, F. Song, N. Siegel, L. Wang, A. Creswell, G. Irving, and I. Higgins. Solving math word problems with process-and outcome-based feedback. *arXiv preprint arXiv:2211.14275*, 2022.
349	
350	X. Wang, J. Wei, D. Schuurmans, Q. Le, E. Chi, and D. Zhou. Self-consistency improves chain of thought reasoning in language models. *arXiv preprint arXiv:2203.11171*, 2022.
351	
352	J. Wei, X. Wang, D. Schuurmans, M. Bosma, E. Chi, Q. Le, and D. Zhou. Chain of thought prompting elicits reasoning in large language models. *arXiv preprint arXiv:2201.11903*, 2022.
353	
354	E. Zelikman, Y. Wu, J. Mu, and N. Goodman. Star: Bootstrapping reasoning with reasoning. *Advances in Neural Information Processing Systems*, 35: 15476–15488, 2022.
355	
356	D. M. Ziegler, N. Stiennon, J. Wu, T. B. Brown, A. Radford, D. Amodei, P. Christiano, and G. Irving. Fine-tuning language models from human preferences. *arXiv preprint arXiv:1909.08593*, 2019.## A MathMix
357	
358	Similar to Lewkowycz et al. (2022) we construct a large-scale dataset of high-quality math-relevant tokens for use in a lightweight pretraining stage, before finetuning on comparably smaller datasets like MATH and PRM800K. This dataset, which we call MathMix, has two main differences compared to the one used to train Minerva. First, it is smaller and more aggressively filtered to high-quality math problem-solving content, and second, it does not explicitly mix in general language data.
359	
360	Minerva was trained on 38.5B tokens of arXiv documents and webscraper pages with LaTeX content, while MathMix consists of a smaller set of 1.5B tokens containing individual math problems and their solutions, free-form text discussing math problems and concepts, and synthetic data (Table 2). While Minerva was pretrained on a dataset with 5% general natural language data, we chose not to mix in any natural language data explicitly, primarily because MathMix already contains plenty of natural language data.
361	
362	&lt;table border="1">&lt;thead>&lt;tr>&lt;th>Data type&lt;/th>&lt;th>Token count&lt;/th>&lt;th>Present in pretraining?&lt;/th>&lt;/tr>&lt;/thead>&lt;tbody>&lt;tr>&lt;td>Math problems and solutions&lt;/td>&lt;td>~ 275M&lt;/td>&lt;td>No&lt;/td>&lt;/tr>&lt;tr>&lt;td>Free-form math discussion text (1)&lt;/td>&lt;td>~ 430M&lt;/td>&lt;td>No&lt;/td>&lt;/tr>&lt;tr>&lt;td>Free-form math discussion text (2)&lt;/td>&lt;td>~ 450M&lt;/td>&lt;td>Yes&lt;/td>&lt;/tr>&lt;tr>&lt;td>Synthetic data (1)&lt;/td>&lt;td>~ 30M&lt;/td>&lt;td>No&lt;/td>&lt;/tr>&lt;tr>&lt;td>Synthetic data (2)&lt;/td>&lt;td>~ 100M&lt;/td>&lt;td>Yes&lt;/td>&lt;/tr>&lt;tr>&lt;td>Critiques grading data&lt;/td>&lt;td>~ 500M&lt;/td>&lt;td>No&lt;/td>&lt;/tr>&lt;/tbody>&lt;/table>
363	
364	Table 2: MathMix dataset components.
365	
366	Note that when training smaller models, as in Section 4, we use a slightly smaller variant of MathMix that excludes the critiques data and only consists of 1B tokens. For our large models experiments, we train on MathMix for roughly 3B tokens (2 epochs). For our small models experiments, we train for 6 epochs (roughly 6.6B tokens).
367	
368	We apply a set of decontamination checks on MathMix against the test split of the MATH dataset, including stripping out LaTeX and searching for matching n-grams, but we can make no strong guarantees on the efficacy of this decontamination. As discussed in Section 6.3, we would not expect the relative comparisons made throughout this work to be significantly impacted by test set contamination.## B PRM800K
369	
370	We collected 1,085,590 step-level labels over 101,599 solution samples. We present the whole unfiltered dataset as PRM800K. During training we discard labels used for quality control, as well as any step-level labels for which the labeler was unable to complete the task. The filtered dataset contains about 800,000 step-level labels over 75,000 solutions. The full PRM800K dataset is available at &lt;https://github.com/openai/prm800k>.
371	
372	The data collection was split into two separate phases. In phase 1, we collected labels for multiple alternative completions at each step of a solution. This seeded our dataset but was cumbersome—for many steps the alternatives were repetitive, and we found labelers spent a lot of time supervising long uninteresting solutions. As a result, the step-level labels we collected in this phase are more repetitive than those collected later. In total, phase 1 represents about 5% of PRM800K, or about 40,000 step-level labels.
373	
374	The majority of our labels were collected as part of phase 2, during which we scaled up and streamlined the data collection process. Phase 2 data collection is split into 10 generations. For each generation, we sample  $N$  solutions per problem from the generator. We rank these solutions with our current best PRM and surface the highest scoring wrong-answer solutions to our labelers. We retrain this PRM between each generation using all the latest data. This active learning strategy changes the balance of our data considerably. Though we sometimes surfaced correct solutions (either by manually injecting correct solutions or because of errors in our automatic grading), the vast majority of the labels we collected in this phase are for incorrect solutions. Table 3 breaks down the balance of correct/incorrect steps and solutions between the different phases of data collection. Though we mostly collected labels on incorrect solutions, we still collected many labels for correct individual steps. In fact, our small-scale ablations in Section 4.2 suggest that this active learning strategy, which favors labelling high-scoring wrong-answer solutions, improves performance despite the resulting imbalance in the dataset.
375	
376	&lt;table border="1">&lt;thead>&lt;tr>&lt;th>&lt;/th>&lt;th>phase 1&lt;/th>&lt;th>phase 2&lt;/th>&lt;th>combined&lt;/th>&lt;/tr>&lt;/thead>&lt;tbody>&lt;tr>&lt;td>% end in correct solution&lt;/td>&lt;td>85.1&lt;/td>&lt;td>13.2&lt;/td>&lt;td>14.2&lt;/td>&lt;/tr>&lt;tr>&lt;td>% correct steps&lt;/td>&lt;td>58.6&lt;/td>&lt;td>74.1&lt;/td>&lt;td>73.1&lt;/td>&lt;/tr>&lt;/tbody>&lt;/table>
377	
378	Table 3: Distribution of positive/negative steps/solutions.
379	
380	Some of our phase 2 questions are intended for quality control. For a quality control question, researchers mark which steps are reasonable to label as incorrect. Then we assess that labelers are able to consistently mark those steps as incorrect. Prior to starting on phase 2, we required all labelers to label 30 quality control questions. This served as a screening test, and we only admitted labelers that agreed with our gold labels at least 75% of the time.
381	
382	We then designated 10-20 problems per generation as additional quality control questions, and we randomly served them to labelers as they workedthrough the task. We used the results of this continuous quality control to remove labelers whose quality slipped too far, as well as to prepare educational material on common mistakes in order to improve labeler alignment with our instructions.
383	
384	## C Evaluation
385	
386	As we scaled up the project, we began having to collect labels on multiple solutions for the same training problem. In order to avoid the risk of over-fitting on the 7,500 MATH training problems, we expanded the training set to include 4,500 MATH test split problems. We therefore evaluate our models only on the remaining 500 held-out problems. We selected these 500 test problems uniformly at random. In Figure 5, we show that the distribution of difficulty levels and subjects in this subset is representative of the MATH test set as a whole. The specific test set we used can be found at &lt;https://github.com/openai/prm800k>. We leave it for future work to explore how many distinct training problems are actually necessary, and how quickly our methods overfit to the training set.
387	
388	Figure 5: Two histograms comparing the distribution of problem difficulty levels and subjects in both the original MATH test set and in our 500 problem test subset.## D Labelling Instructions
389	
390	Labelers were tasked to look at steps in a solution and label each one as **positive**, **negative**, or **neutral**. A step is considered **neutral** if it is appropriate in context, reasonable, correct, and contains only computations that can be verified easily. A step is **positive** if it is **neutral** and also progresses towards the solution. All other steps are considered **negative**. Labelers were not given reference solutions, but they were given the ground truth final answers. We chose not to provide reference solutions to avoid biasing them towards one particular path to the solution. We chose to provide ground truth final answers since this information can sometimes help labelers resolve their own misunderstandings.
391	
392	In phase 1, labelers were permitted to enter their own steps in the case that all candidate steps were **negative**. Then the solution would progress from a randomly selected **positive** step (or **neutral** if there were no **positive** ones). This often resulted in trajectories that got stuck in endless sequences of **neutral** steps that said reasonable things but made frustratingly slow progress towards a solution or **negative** steps that needed constant human supervision. In phase 2, we pre-generate whole solutions and end the task as soon as the first **negative** step is encountered. The full instructions given to labelers can be found at &lt;https://github.com/openai/prm800k/tree/main/prm800k/instructions>.
393	
394	## E ORM Training Details
395	
396	We train outcome-supervised reward models in the same manner as token-level verifiers from Cobbe et al. (2021), with a few subtle differences to hyperparameters. In particular, we only train for a single epoch on each dataset of model samples and reward model labels, without dropout, and without jointly learning a language modeling objective. We find that performance is not sensitive to most other hyperparameters, within a reasonable range.
397	
398	To collect model samples, we simply sample uniformly from the generator at a temperature of 1.0 without applying any rebalancing of positives or negatives. At training time, the reward model makes predictions for every token in the context. The target for each token in a solution is the same, based on whether the solution is labelled correct or incorrect. At test time, we simply use the score of the final token in the completion as the overall score of the solution. We note that this setup is identical to the way token-level verifiers were trained in Cobbe et al. (2021).## F PRM Details
399	
400	### F.1 Training
401	
402	We train our PRMs by fine-tuning the MathMix model to predict the probability of positive, negative, and neutral labels given a solution prefix ending in one of our labeled steps. We sweep over hyperparameters using a dataset containing the first  $\sim 10\%$  of PRM800K. Fine-tuning an LLM from its ordinary language modeling task to a classification task like this is a large distribution shift, and we found low learning rates were important to stable PRM training.
403	
404	All of our PRMs are trained for 2 epochs. On smaller datasets (such as in phase 1 and the first few generations of phase 2) this improves the final performance over training for just 1 epoch. Additional epochs, up to some point, don't noticeably help or hurt performance. On larger datasets, the benefits of 2 epoch training diminishes, but we continue doing it for consistency.
405	
406	### F.2 Scoring
407	
408	There are multiple ways of using the PRM to score solutions. In general, we produce a single solution-level score by performing a reduction over step-level scores, where the step-level score is the probability that the step's label is positive. This involves two specific implementation decisions. First, when determining a step-level score, we either consider a neutral label to be positive or negative. Second, when determining a solution-level score, we either use the minimum or the product over step-level scores as a reduction.
409	
410	We show results from all four scoring strategies in Table 4. The best performing strategy is to take the product of step-level scores and to consider the neutrals as positives, but the difference in performance between all strategies is minor. Throughout the rest of this work, we consider neutral steps to be positive, and we define the solution score to be the product of step-level scores. Using the product instead of the minimum as the reduction does create a slight bias against solutions with a larger number of steps.
411	
412	&lt;table>&lt;thead>&lt;tr>&lt;th>&lt;/th>&lt;th>product&lt;/th>&lt;th>minimum&lt;/th>&lt;/tr>&lt;/thead>&lt;tbody>&lt;tr>&lt;td>neutral = positive&lt;/td>&lt;td>78.2%&lt;/td>&lt;td>77.6%&lt;/td>&lt;/tr>&lt;tr>&lt;td>neutral = negative&lt;/td>&lt;td>77.4%&lt;/td>&lt;td>77.8%&lt;/td>&lt;/tr>&lt;/tbody>&lt;/table>
413	
414	Table 4: Best-of-1860 test performance using the PRM with four different scoring strategies.## G Difficulty Breakdown
415	
416	We show performance of our ORM and PRM on each quintile of the MATH dataset. We determine quintiles based on the pass rate under the generator. It is interesting to note that the performance gap is not only apparent on high difficulty problems: it is in fact apparent across all difficulties. For the lowest difficulty problems, we see that it is possible to find adversarial examples that fool the ORM, since the ORM’s performance slightly decreases as the number of samples increases. In contrast, the PRM remains highly robust over this same set of samples.
417	
418	We also see that increasing the number of samples has the largest positive effect on the highest difficulty problems. This is to be expected, since a large number of generator samples may be required to find a true and convincing solution to a hard problem.
419	
420	Figure 6: A breakdown of ORM vs PRM performance by problem difficulty.## H Synthetic Supervision Details
421	
422	We can use  $\text{PRM}_{\text{large}}$  to provide either outcome or process supervision for smaller models. We determine the labels for individual steps based on the step-level probabilities outputted by  $\text{PRM}_{\text{large}}$ . To do this, we set an arbitrary threshold: any step that  $\text{PRM}_{\text{large}}$  assigns a negative label with greater than 20% probability is considered incorrect. We choose this threshold based on the observation that  $\text{PRM}_{\text{large}}$  is slightly miscalibrated in the direction of favoring positive labels.
423	
424	To provide process supervision for a solution, we directly return the step-level labels (positive or negative) provided by  $\text{PRM}_{\text{large}}$ , up until the first step that is marked as negative. This mimics our true human data collection process. To provide outcome supervision, we mark the solution as correct if and only if  $\text{PRM}_{\text{large}}$  considers every step to be correct (using the same thresholding logic).# I PRM Visualizations
425	
426	All examples shown come from the large-scale generator (GPT-4). We note the pass-rate under the generator to give some sense of the difficulty of these problems.
427	
428	## I.1 True Positives
429	
430	These cherry-picked examples show the best-of-1860 solution from the generator as ranked by the large-scale PRM.
431	
432	Problem 1. Generator pass-rate: 0.1%. This challenging trigonometry problem requires applying several identities in a not-at-all obvious succession. Most solution attempts fail, because it is hard to choose which identities are actually helpful. Though successful solutions to this problem are rare, the reward model correctly recognizes when a valid chain-of-thought has been found.
433	
434	Simplify  $\tan 100^\circ + 4 \sin 100^\circ$ .
435	
436	I notice that the angle 100 degrees is not a special angle, so I will need to use some trigonometric identities to simplify this expression.
437	
438	I recall that  $\tan \theta = \frac{\sin \theta}{\cos \theta}$  and  $\sin 2\theta = 2 \sin \theta \cos \theta$ .
439	
440	I can use these identities to rewrite the expression as  $\frac{\sin 100^\circ}{\cos 100^\circ} + 4 \sin 100^\circ$ .
441	
442	I can combine the terms by finding a common denominator of  $\cos 100^\circ$ .
443	
444	I get  $\frac{\sin 100^\circ + 4 \sin 100^\circ \cos 100^\circ}{\cos 100^\circ}$ .
445	
446	I can simplify the numerator by using the double angle identity again, but in reverse.
447	
448	I get  $\frac{\sin 100^\circ + 2 \sin 200^\circ}{\cos 100^\circ}$ .
449	
450	I notice that 200 degrees is the same as 180 degrees plus 20 degrees, so I can use the sum angle identity for sine.
451	
452	I get  $\frac{\sin 100^\circ + 2(\sin 180^\circ \cos 20^\circ + \cos 180^\circ \sin 20^\circ)}{\cos 100^\circ}$ .
453	
454	I recall that  $\sin 180^\circ = 0$  and  $\cos 180^\circ = -1$ , so I can simplify further.
455	
456	I get  $\frac{\sin 100^\circ - 2 \sin 20^\circ}{\cos 100^\circ}$ .
457	
458	I notice that 100 degrees is the same as 90 degrees plus 10 degrees, so I can use the sum angle identity for sine and cosine.
459	
460	I get  $\frac{(\sin 90^\circ \cos 10^\circ + \cos 90^\circ \sin 10^\circ) - 2 \sin 20^\circ}{(\cos 90^\circ \cos 10^\circ - \sin 90^\circ \sin 10^\circ)}$ .
461	
462	I recall that  $\sin 90^\circ = 1$  and  $\cos 90^\circ = 0$ , so I can simplify further.
463	
464	I get  $\frac{\cos 10^\circ - 2 \sin 20^\circ}{-\sin 10^\circ}$ .
465	
466	I can simplify the sign by multiplying the numerator and denominator by -1.
467	
468	I get  $\frac{2 \sin 20^\circ - \cos 10^\circ}{\sin 10^\circ}$ .
469	
470	I notice that 20 degrees is the same as 30 degrees minus 10 degrees, so I can use the difference angle identity for sine.
471	
472	I get  $\frac{2(\sin 30^\circ \cos 10^\circ - \cos 30^\circ \sin 10^\circ) - \cos 10^\circ}{\sin 10^\circ}$ .
473	
474	I recall that  $\sin 30^\circ = \frac{1}{2}$  and  $\cos 30^\circ = \frac{\sqrt{3}}{2}$ , so I can simplify further.
475	
476	I get  $\frac{\cos 10^\circ - \sqrt{3} \sin 10^\circ - \cos 10^\circ}{\sin 10^\circ}$ .
477	
478	I can cancel out the  $\cos 10^\circ$  terms in the numerator.
479	
480	I get  $\frac{-\sqrt{3} \sin 10^\circ}{\sin 10^\circ}$ .
481	
482	I can cancel out the  $\sin 10^\circ$  terms in the numerator and denominator.
483	
484	I get  $-\sqrt{3}$ .
485	
486	Answer:  $-\sqrt{3}$Problem 2. Generator pass-rate: 5.8%. In step 7 and 8, the generator starts performing guess-and-check. This is a common place the model might hallucinate, by claiming a particular guess is successful when it isn't. In this case, the reward model verifies each step and determines that the chain-of-thought is correct.
487	
488	Find the unique odd integer  $t$  such that  $0 < t < 23$  and  $t + 2$  is the inverse of  $t$  modulo 23.
489	
490	I need to find an odd integer  $t$  that satisfies the congruence  $t + 2 \equiv t^{-1} \pmod{23}$ .
491	
492	To do that, I can multiply both sides by  $t$  and get  $t^2 + 2t \equiv 1 \pmod{23}$ .
493	
494	Then I can complete the square by adding and subtracting  $(2/2)^2 = 1$  to the left side and get  $(t + 1)^2 - 1 \equiv 1 \pmod{23}$ .
495	
496	Simplifying, I get  $(t + 1)^2 \equiv 2 \pmod{23}$ .
497	
498	Now I need to find a square root of 2 modulo 23.
499	
500	I can try some values of  $t + 1$  and see if they work.
501	
502	For example, if  $t + 1 = 3$ , then  $(t + 1)^2 = 9 \not\equiv 2 \pmod{23}$ .
503	
504	If  $t + 1 = 5$ , then  $(t + 1)^2 = 25 \equiv 2 \pmod{23}$ .
505	
506	So one possible value of  $t$  is  $t = 5 - 1 = 4$ .
507	
508	But this is not odd, so I need to find another one.
509	
510	I know that if  $t + 1$  is a square root of 2 modulo 23, then so is  $-t - 1$ .
511	
512	So I can try  $-t - 1 = 5$  and get  $t = -6$ .
513	
514	But this is negative, so I need to add 23 to get a positive value.
515	
516	So another possible value of  $t$  is  $t = -6 + 23 = 17$ .
517	
518	This is odd and satisfies the original congruence, so this is the unique solution.
519	
520	Answer: 17
521	
522	Problem 3. Generator pass-rate: 1.7%. The generator successfully applies several trigonometric identities to simplify the expression.
523	
524	Find the degree measure of the least positive angle  $\theta$  for which
525	
526	$$\tan \theta = \frac{\cos 5^\circ \cos 20^\circ + \cos 35^\circ \cos 50^\circ - \sin 5^\circ \sin 20^\circ - \sin 35^\circ \sin 50^\circ}{\sin 5^\circ \cos 20^\circ - \sin 35^\circ \cos 50^\circ + \cos 5^\circ \sin 20^\circ - \cos 35^\circ \sin 50^\circ}.$$
527	
528	I notice that the numerator and denominator of the fraction are both sums of products of cosine and sine functions of angles that add up to 25 degrees or 85 degrees.
529	
530	This suggests that I might be able to use some trigonometric identities to simplify the expression.
531	
532	For example, I recall that  $\cos(A + B) = \cos A \cos B - \sin A \sin B$  and  $\sin(A + B) = \sin A \cos B + \cos A \sin B$ .
533	
534	If I apply these identities to the terms in the numerator, I get  $\cos 5^\circ \cos 20^\circ + \cos 35^\circ \cos 50^\circ - \sin 5^\circ \sin 20^\circ - \sin 35^\circ \sin 50^\circ = \cos(5^\circ + 20^\circ) + \cos(35^\circ + 50^\circ) = \cos 25^\circ + \cos 85^\circ$ .
535	
536	Similarly, if I apply these identities to the terms in the denominator, I get  $\sin 5^\circ \cos 20^\circ - \sin 35^\circ \cos 50^\circ + \cos 5^\circ \sin 20^\circ - \cos 35^\circ \sin 50^\circ = \sin(5^\circ + 20^\circ) - \sin(35^\circ + 50^\circ) = \sin 25^\circ - \sin 85^\circ$ .
537	
538	Now I have  $\tan \theta = \frac{\cos 25^\circ + \cos 85^\circ}{\sin 25^\circ - \sin 85^\circ}$ .
539	
540	I wonder if I can simplify this fraction further.
541	
542	I recall another trigonometric identity that says  $\cos A + \cos B = 2 \cos \frac{A+B}{2} \cos \frac{A-B}{2}$ .
543	
544	If I apply this identity to the numerator, I get  $\cos 25^\circ + \cos 85^\circ = 2 \cos \frac{25^\circ + 85^\circ}{2} \cos \frac{25^\circ - 85^\circ}{2} = 2 \cos 55^\circ \cos(-30^\circ)$ .
545	
546	I also recall that  $\cos(-\theta) = \cos \theta$ , so I can write  $\cos(-30^\circ) = \cos 30^\circ$ .
547	
548	Similarly, I recall another trigonometric identity that says  $\sin A - \sin B = 2 \cos \frac{A+B}{2} \sin \frac{A-B}{2}$ .
549	
550	If I apply this identity to the denominator, I get  $\sin 25^\circ - \sin 85^\circ = 2 \cos \frac{25^\circ + 85^\circ}{2} \sin \frac{25^\circ - 85^\circ}{2} = 2 \cos 55^\circ \sin(-30^\circ)$ .
551	
552	I also recall that  $\sin(-\theta) = -\sin \theta$ , so I can write  $\sin(-30^\circ) = -\sin 30^\circ$ .
553	
554	Now I have  $\tan \theta = \frac{2 \cos 55^\circ \cos 30^\circ}{2 \cos 55^\circ (-\sin 30^\circ)} = \frac{-\cos 30^\circ}{\sin 30^\circ}$ .
555	
556	I know that  $\cos 30^\circ = \frac{\sqrt{3}}{2}$  and  $\sin 30^\circ = \frac{1}{2}$ , so I can simplify this to  $\tan \theta = -\frac{\sqrt{3}}{1} = -\sqrt{3}$ .
557	
558	I also know that  $\tan \theta$  is negative in the second and fourth quadrants, and that  $\tan \theta = -\sqrt{3}$  when  $\theta$  is  $120^\circ$  or  $300^\circ$ .
559	
560	Therefore, the least positive angle  $\theta$  for which  $\tan \theta = -\sqrt{3}$  is  $120^\circ$ .
561	
562	Answer: 120Problem 4. Generator pass-rate: 4.5%. Here, the generator successfully performs a complex series of polynomial factorizations. The use of the Sophie-Germain identity in step 5 is an important step that could be considered insightful.
563	
564	Let
565	
566	$$x^8 + 3x^4 - 4 = p_1(x)p_2(x) \cdots p_k(x),$$
567	
568	where each non-constant polynomial  $p_i(x)$  is monic with integer coefficients, and cannot be factored further over the integers. Compute  $p_1(1) + p_2(1) + \cdots + p_k(1)$ .
569	
570	I notice that the given polynomial has even degree and only even powers of  $x$ , so I can try to make a substitution to simplify it:
571	
572	Let  $y = x^4$ , then the polynomial becomes  $y^2 + 3y - 4$ , which is a quadratic equation.
573	
574	I can factor this quadratic equation as  $(y + 4)(y - 1)$ , so the original polynomial is  $(x^4 + 4)(x^4 - 1)$ .
575	
576	Now I need to factor each of these factors further, if possible, over the integers.
577	
578	For the first factor,  $x^4 + 4$ , I recall the Sophie Germain identity, which says that  $a^4 + 4b^4 = (a^2 + 2b^2 + 2ab)(a^2 + 2b^2 - 2ab)$ .
579	
580	Applying this identity with  $a = x$  and  $b = 1$ , I get  $x^4 + 4 = (x^2 + 2x + 2)(x^2 - 2x + 2)$ .
581	
582	For the second factor,  $x^4 - 1$ , I can use the difference of squares formula, which says that  $a^2 - b^2 = (a + b)(a - b)$ .
583	
584	Applying this formula with  $a = x^2$  and  $b = 1$ , I get  $x^4 - 1 = (x^2 + 1)(x^2 - 1)$ .
585	
586	Then I can apply the difference of squares formula again with  $a = x$  and  $b = 1$ , to get  $x^2 - 1 = (x + 1)(x - 1)$ .
587	
588	So the original polynomial is  $(x^4 + 4)(x^4 - 1) = (x^2 + 2x + 2)(x^2 - 2x + 2)(x^2 + 1)(x + 1)(x - 1)$ .
589	
590	These are all the irreducible factors over the integers, so  $p_1(x) = x^2 + 2x + 2$ ,  $p_2(x) = x^2 - 2x + 2$ ,  $p_3(x) = x^2 + 1$ ,  $p_4(x) = x + 1$ , and  $p_5(x) = x - 1$ .
591	
592	To find the sum of their values at  $x = 1$ , I just need to plug in  $x = 1$  into each factor and add them up.
593	
594	I get  $p_1(1) = 1^2 + 2 \cdot 1 + 2 = 5$ ,  $p_2(1) = 1^2 - 2 \cdot 1 + 2 = 1$ ,  $p_3(1) = 1^2 + 1 = 2$ ,  $p_4(1) = 1 + 1 = 2$ , and  $p_5(1) = 1 - 1 = 0$ .
595	
596	So the final answer is  $5 + 1 + 2 + 2 + 0 = 10$ .
597	
598	Answer: 10
599	
600	## I.2 True Negatives
601	
602	Problem 5. Generator pass-rate: 4.5%. The generator attempts to use the difference of squares formula in step 12 on an expression that isn't in fact a difference of squares. The reward model catches this mistake.
603	
604	Let
605	
606	$$x^8 + 3x^4 - 4 = p_1(x)p_2(x) \cdots p_k(x),$$
607	
608	where each non-constant polynomial  $p_i(x)$  is monic with integer coefficients, and cannot be factored further over the integers. Compute  $p_1(1) + p_2(1) + \cdots + p_k(1)$ .
609	
610	This problem is about factoring a polynomial over the integers, which can be a tricky task.
611	
612	One possible strategy is to look for rational roots of the polynomial, using the rational root theorem.
613	
614	However, that would involve checking a lot of possible factors of  $-4$ , and there is no guarantee that the polynomial has any rational roots at all.
615	
616	Another possible strategy is to use some algebraic tricks to simplify the polynomial or reduce its degree.
617	
618	I notice that the polynomial has only even powers of  $x$ , so I can try to substitute  $y = x^4$  and see what happens.
619	
620	Then the polynomial becomes  $y^2 + 3y - 4$ , which is a quadratic equation in  $y$ .
621	
622	I can try to factor this quadratic equation by looking for two numbers that multiply to  $-4$  and add to 3.
623	
624	Those numbers are 4 and  $-1$ , so I can write  $y^2 + 3y - 4 = (y + 4)(y - 1)$ .
625	
626	Now I can substitute back  $x^4 = y$  and get  $x^8 + 3x^4 - 4 = (x^4 + 4)(x^4 - 1)$ .
627	
628	This looks promising, because I have reduced the degree of the factors from 8 to 4.
629	
630	I can try to factor each of these factors further, using the difference of squares formula.
631	
632	I get  $x^8 + 3x^4 - 4 = (x^4 + 2)(x^4 - 2)(x^2 + 1)(x^2 - 1)$ .
633	
634	I can apply the difference of squares formula again to the last factor and get  $x^8 + 3x^4 - 4 = (x^4 + 2)(x^2 - 2)(x^2 + 1)(x + 1)(x - 1)$ .
635	
636	Now I have factored the polynomial completely into monic linear and quadratic factors with integer coefficients.
637	
638	These are the  $p_i(x)$ 's that the problem is asking for.
639	
640	To find the sum of their values at  $x = 1$ , I just need to plug in  $x = 1$  into each factor and add them up.
641	
642	I get  $p_1(1) + p_2(1) + \cdots + p_k(1) = (1^4 + 2)(1^4 - 2)(1^2 + 1)(1 + 1)(1 - 1)$ .
643	
644	Simplifying, I get  $p_1(1) + p_2(1) + \cdots + p_k(1) = (3)(-1)(2)(2)(0)$ .
645	
646	Multiplying, I get  $p_1(1) + p_2(1) + \cdots + p_k(1) = 0$ .
647	
648	Answer: 0Problem 6. Generator pass-rate: 93.5%. In step 7, the generator makes an incorrect attempt to simplify an expression. The reward model catches this mistake.
649	
650	A class of 30 students recently took a test. If 20 students scored 80, 8 students scored 90, and 2 students scored 100, then what was the class average (the mean) on this test?
651	
652	To find the class average, I need to add up all the scores and divide by the number of students.
653	
654	I can use a shortcut to add up the scores, since they are grouped by value.
655	
656	For example, instead of adding  $80 + 80 + \dots + 80$  twenty times, I can just multiply 80 by 20 to get the same result.
657	
658	Similarly, I can multiply 90 by 8 and 100 by 2 to get the sums of those groups.
659	
660	So, the total sum of the scores is  $80 * 20 + 90 * 8 + 100 * 2$ .
661	
662	I can use the distributive property of multiplication to simplify this expression.
663	
664	It is equivalent to  $80 * (20 + 1) + 90 * 8 + 100$ .
665	
666	That is,  $80 * 21 + 720 + 100$ .
667	
668	I can do the arithmetic in my head or use a calculator.
669	
670	$80 * 21$  is 1680, so the total sum is  $1680 + 720 + 100$ , which is 2500.
671	
672	Now, to find the average, I need to divide 2500 by 30, the number of students.
673	
674	I can use long division or a calculator for this step.
675	
676	2500 divided by 30 is 83.33, repeating.
677	
678	This means that the class average is 83.33, or 83 and one-third.
679	
680	Answer: 83.33
681	
682	Problem 7. Generator pass-rate: 48.0%. In step 11, the generator makes a simple calculation error. The reward model catches this mistake.
683	
684	If  $A$  is the sum of the positive divisors of 500, what is the sum of the distinct prime divisors of  $A$ ?
685	
686	I notice that  $500 = 2^2 \cdot 5^3$ , so its positive divisors are of the form  $2^a \cdot 5^b$ , where  $a \in \{0, 1, 2\}$  and  $b \in \{0, 1, 2, 3\}$ .
687	
688	To find the sum of these divisors, I can use a formula that involves the geometric series: if  $p$  is a prime number and  $n$  is a nonnegative integer, then the sum of the powers of  $p$  from 0 to  $n$  is  $\frac{p^{n+1}-1}{p-1}$ .
689	
690	So, the sum of the powers of 2 from 0 to 2 is  $\frac{2^3-1}{2-1} = 7$ , and the sum of the powers of 5 from 0 to 3 is  $\frac{5^4-1}{5-1} = 156$ .
691	
692	By the distributive property, the sum of the divisors of 500 is the product of these two sums:  $A = 7 \cdot 156 = 1092$ .
693	
694	Now, I need to find the sum of the distinct prime divisors of  $A$ .
695	
696	I can try to factor  $A$  into primes by trial division.
697	
698	I notice that  $A$  is divisible by 2, so I divide by 2 and get 546.
699	
700	I repeat this process and divide by 2 again, getting 273.
701	
702	Now, 273 is not divisible by 2, so I try the next prime, 3.
703	
704	I see that 273 is divisible by 3, so I divide by 3 and get 91.
705	
706	I divide by 3 again, getting 31.
707	
708	Now, 31 is a prime number, so I have found all the prime factors of  $A$ :  $A = 2^2 \cdot 3^2 \cdot 31$ .
709	
710	The sum of the distinct prime divisors of  $A$  is  $2 + 3 + 31 = 36$ .
711	
712	Answer: 36Problem 8. Generator pass-rate: 5.8%. The justification in step 8 is strange, but the reward model lets it slide. In step 9, though, the model incorrectly factors the expression. The reward model catches this mistake.
713	
714	Find the unique odd integer  $t$  such that  $0 < t < 23$  and  $t + 2$  is the inverse of  $t$  modulo 23.
715	
716	I need to find an odd integer  $t$  between 0 and 23 such that  $t + 2$  is the inverse of  $t$  modulo 23.
717	
718	That means that  $t$  and  $t + 2$  multiply to give 1 modulo 23.
719	
720	I can write this as  $t(t + 2) \equiv 1 \pmod{23}$ .
721	
722	I can try to guess and check values of  $t$  until I find one that works, but that might take a long time.
723	
724	I can also try to use some properties of modular arithmetic to simplify the equation.
725	
726	For example, I can subtract 23 from  $t + 2$  and still get the same remainder modulo 23.
727	
728	So I can write  $t(t + 2) \equiv t(t - 21) \pmod{23}$ .
729	
730	This looks simpler, because now I have a difference of two multiples of  $t$ .
731	
732	I can factor out  $t$  and get  $t(t - 21) \equiv t(1 - 21) \pmod{23}$ .
733	
734	Now I can divide both sides by  $t$ , as long as  $t$  is not a multiple of 23.
735	
736	This gives me  $t - 21 \equiv 1 - 21 \pmod{23}$ .
737	
738	I can simplify this further by adding 21 to both sides.
739	
740	This gives me  $t \equiv 1 \pmod{23}$ .
741	
742	This means that  $t$  has the same remainder as 1 when divided by 23.
743	
744	The smallest positive value of  $t$  that satisfies this is  $t = 1$ .
745	
746	This is also an odd integer, so it meets the criteria of the problem.
747	
748	I can check that  $t = 1$  works by plugging it into the original equation.
749	
750	I get  $1(1 + 2) \equiv 1 \pmod{23}$ , which is true.
751	
752	Therefore, the unique odd integer  $t$  that satisfies the given conditions is  $t = 1$ .
753	
754	Answer: 1
755	
756	### I.3 False Positives
757	
758	Problem 9. Generator pass-rate: 18.5%. The generator makes a subtle counting error in step 9. On the surface, it appears reasonable to claim that there are 5 ways to exchange the same colored ball since there are 5 colors. However, this undercounts by a factor of 2, since Bob has 2 choices for which ball to return to Alice. The reward model is fooled by this mistake.
759	
760	Bob and Alice each have a bag that contains one ball of each of the colors, blue, green, orange, red, and violet. Alice randomly selects one ball from her bag and puts it into Bob's bag. Bob then randomly selects one ball from his bag and puts it into Alice's bag. What is the probability that after this process the contents of the two bags are the same?
761	
762	To find the probability of an event, I need to divide the number of favorable outcomes by the number of possible outcomes.
763	
764	In this case, the event is that the contents of the two bags are the same after the process.
765	
766	So I need to count how many ways this can happen, and how many ways the process can happen in total.
767	
768	I will start with the total number of ways the process can happen.
769	
770	Alice can choose any of the five balls in her bag, and Bob can choose any of the six balls in his bag.
771	
772	So the total number of ways the process can happen is 5 times 6, which is 30.
773	
774	Now I will count how many ways the contents of the two bags can be the same after the process.
775	
776	This means that Alice and Bob must have exchanged the same color of ball.
777	
778	There are five colors, so there are five ways they can exchange the same color of ball. ERROR
779	
780	Therefore, the number of favorable outcomes is 5.
781	
782	So the probability of the event is 5 divided by 30, which simplifies to 1/6.
783	
784	Answer: 1/6Problem 10. Generator pass-rate: 17.6%. In step 13, the generator attempts to simplify the equation by combining like terms. It correctly moves and combines the linear terms to the left-hand side, but then mistakenly leaves the right-hand side untouched. The reward model is fooled by this mistake.
785	
786	Denali and Nate work for a dog walking business and are paid for each dog they walk. Denali is responsible for 16 dogs and Nate is responsible for 12 dogs. Under the company's new policy, they will be assigned or unassigned new dogs in groups of  $x$  dogs. The ratio of Denali's pay to Nate's pay would be the same if Denali started walking  $4x$  more dogs and Nate stayed at 12 dogs or if  $x$  of Nate's dogs were reassigned to Denali. Find  $x$  if  $x \neq 0$ .
787	
788	I need to find a value of  $x$  that makes the ratio of Denali's pay to Nate's pay the same in two different scenarios.  
789	 I can assume that the pay per dog is constant, so the ratio of their pay is the same as the ratio of the number of dogs they walk.  
790	 Let me write an equation for the first scenario, where Denali walks  $4x$  more dogs and Nate stays at 12 dogs.  
791	 The ratio of Denali's dogs to Nate's dogs is  $\frac{16+4x}{12}$ .  
792	 Now let me write an equation for the second scenario, where  $x$  of Nate's dogs are reassigned to Denali.  
793	 The ratio of Denali's dogs to Nate's dogs is  $\frac{16+x}{12-x}$ .  
794	 I want these two ratios to be equal, so I can set them equal to each other and solve for  $x$ .  
795	 I get  $\frac{16+4x}{12} = \frac{16+x}{12-x}$ .  
796	 I can cross-multiply and simplify this equation.  
797	 I get  $(16+4x)(12-x) = (16+x)(12)$ .  
798	 Expanding the brackets, I get  $192 - 16x + 48x - 4x^2 = 192 + 12x$ .  
799	 Subtracting 192 from both sides, I get  $-16x + 48x - 4x^2 = 12x$ .  
800	 Rearranging the terms, I get  $-4x^2 + 20x = 12x$ . ERROR  
801	 Subtracting  $12x$  from both sides, I get  $-4x^2 + 8x = 0$ .  
802	 I can factor out  $-4x$  from both terms, and get  $-4x(x-2) = 0$ .  
803	 This means that either  $-4x = 0$  or  $x-2 = 0$ .  
804	 Solving for  $x$ , I get  $x = 0$  or  $x = 2$ .  
805	 However, the problem says that  $x \neq 0$ , so I can ignore that solution.  
806	 Therefore, the only valid solution is  $x = 2$ .  
807	 Answer: 2
808	
809	Problem 11. Generator pass-rate: 13.4%. The generator attempts to perform long division, but in step 16, it forgets to include the leading zeros in the repeating part of the decimal. The reward model is fooled by this mistake.
810	
811	When converting  $\frac{31}{1111}$  to a decimal, the decimal turns out to be a repeating decimal. How many digits repeat in this repeating decimal? For example, if you get the repeating decimal  $0.\overline{123}$ , then your answer should be 3, and if you get 0.4367, your answer should be 1.
812	
813	To convert a fraction to a decimal, I can divide the numerator by the denominator using long division.  
814	 I'll start by writing 31 over 11111 and bring down a zero.  
815	 Then I'll ask, how many times does 11111 go into 310?  
816	 Well, it doesn't go in evenly, so I'll write a zero above the decimal point and bring down another zero.  
817	 Now I have 3100.  
818	 How many times does 11111 go into 3100?  
819	 Still zero, so I'll write another zero above the decimal point and bring down another zero.  
820	 Now I have 31000.  
821	 How many times does 11111 go into 31000?  
822	 Ah, now I can see that it goes in twice, so I'll write a 2 above the decimal point and subtract 22222 from 31000 to get 8778.  
823	 I'll bring down another zero and ask, how many times does 11111 go into 87780?  
824	 It goes in seven times, so I'll write a 7 above the decimal point and subtract 77777 from 87780 to get 10003.  
825	 I'll bring down another zero and ask, how many times does 11111 go into 100030?  
826	 It goes in nine times, so I'll write a 9 above the decimal point and subtract 99999 from 100030 to get 31.  
827	 Wait a minute, I'm back to where I started! That means the decimal will repeat from here on.  
828	 So I'll put a bar over the 279 to indicate that it repeats indefinitely. ERROR  
829	 The decimal is  $0.00279$  with a bar over 279.  
830	 The question asks how many digits repeat in this repeating decimal.  
831	 I can see that there are three digits that repeat: 2, 7, and 9.  
832	 So the answer is 3.  
833	 Answer: 3Problem 12. Generator pass-rate: 9.1%. In step 4, the generator falsely claims that the sequence repeats itself every 12 terms, when it's in fact every 10 terms. This sort of counting mistake occasionally fools the reward model.
834	
835	Given that
836	
837	$$\begin{aligned}x_1 &= 211, \\x_2 &= 375, \\x_3 &= 420, \\x_4 &= 523, \text{ and} \\x_n &= x_{n-1} - x_{n-2} + x_{n-3} - x_{n-4} \text{ when } n \geq 5,\end{aligned}$$
838	
839	find the value of  $x_{531} + x_{753} + x_{975}$ .
840	
841	This is a problem involving a recursive sequence, where each term depends on the previous four terms.
842	
843	One way to approach this problem is to look for a pattern or a formula that can help us find any term of the sequence without having to compute all the previous terms.
844	
845	To do that, let's write down the first few terms of the sequence and see if we notice anything:
846	
847	$$\begin{aligned}x_1 &= 211, \\x_2 &= 375, \\x_3 &= 420, \\x_4 &= 523, \\x_5 &= x_4 - x_3 + x_2 - x_1 = 523 - 420 + 375 - 211 = 267, \\x_6 &= x_5 - x_4 + x_3 - x_2 = 267 - 523 + 420 - 375 = -211, \\x_7 &= x_6 - x_5 + x_4 - x_3 = -211 - 267 + 523 - 420 = -375, \\x_8 &= x_7 - x_6 + x_5 - x_4 = -375 - (-211) + 267 - 523 = -420, \\x_9 &= x_8 - x_7 + x_6 - x_5 = -420 - (-375) + (-211) - 267 = -523, \\x_{10} &= x_9 - x_8 + x_7 - x_6 = -523 - (-420) + (-375) - (-211) = -267, \\x_{11} &= x_{10} - x_9 + x_8 - x_7 = -267 - (-523) + (-420) - (-375) = 211, \\x_{12} &= x_{11} - x_{10} + x_9 - x_8 = 211 - (-267) + (-523) - (-420) = 375, \\x_{13} &= x_{12} - x_{11} + x_{10} - x_9 = 375 - 211 + (-267) - (-523) = 420, \\x_{14} &= x_{13} - x_{12} + x_{11} - x_{10} = 420 - 375 + 211 - (-267) = 523.\end{aligned}$$
848	
849	We can see that the sequence repeats itself every 12 terms, starting from  $x_{14}$  ERROR
850	
851	This means that we can find any term of the sequence by finding its remainder when divided by 12, and then looking up the corresponding term in the first cycle.
852	
853	For example, to find  $x_{531}$ , we can divide 531 by 12 and get a quotient of 44 and a remainder of 3.
854	
855	This means that  $x_{531}$  is the same as  $x_3$ , which is 420.
856	
857	Similarly, we can find  $x_{753}$  and  $x_{975}$  by dividing them by 12 and looking up their remainders.
858	
859	We get that  $x_{753}$  has a remainder of 9, so it is the same as  $x_9$ , which is -523.
860	
861	And  $x_{975}$  has a remainder of 3, so it is the same as  $x_3$ , which is 420.
862	
863	Therefore, the value of  $x_{531} + x_{753} + x_{975}$  is  $420 + (-523) + 420 = 317$ .
864	
865	Answer: 317
866	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50a4ea63-f2ea-4bbf-88d4-1664a72d1614",
  "isSidechain": false,
  "promptId": "847a487e-d454-4fe9-b1b6-24705f0c37b0",
  "type": "user",
  "uuid": "ebad8f4e-52f8-4fdd-8de9-02801e586928",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/2d2f5f70-a94f-402d-8c92-8c562e7598cd/tool-results/toolu_01E4nuwrRycqiA7GsnaaPNGX.txt",
      "content": "# Let’s Verify Step by Step\n\nHunter Lightman\\*    Vineet Kosaraju\\*    Yura Burda\\*    Harri Edwards  \n Bowen Baker    Teddy Lee    Jan Leike    John Schulman    Ilya Sutskever  \n Karl Cobbe\\*  \n OpenAI\n\n## Abstract\n\nIn recent years, large language models have greatly improved in their ability to perform complex multi-step reasoning. However, even state-of-the-art models still regularly produce logical mistakes. To train more reliable models, we can turn either to outcome supervision, which provides feedback for a final result, or process supervision, which provides feedback for each intermediate reasoning step. Given the importance of training reliable models, and given the high cost of human feedback, it is important to carefully compare the both methods. Recent work has already begun this comparison, but many questions still remain. We conduct our own investigation, finding that process supervision significantly outperforms outcome supervision for training models to solve problems from the challenging MATH dataset. Our process-supervised model solves 78% of problems from a representative subset of the MATH test set. Additionally, we show that active learning significantly improves the efficacy of process supervision. To support related research, we also release PRM800K, the complete dataset of 800,000 step-level human feedback labels used to train our best reward model.\n\n## 1 Introduction\n\nLarge language models are capable of solving tasks that require complex multi-step reasoning by generating solutions in a step-by-step chain-of-thought format (Nye et al., 2021; Wei et al., 2022; Kojima et al., 2022). However, even state-of-the-art models are prone to producing falsehoods — they exhibit a tendency to invent facts in moments of uncertainty (Bubeck et al., 2023). These *hallucinations* (Maynez et al., 2020) are particularly problematic in domains that require multi-step reasoning, since a single logical error is enough to derail a much larger solution. Detecting and mitigating hallucinations is essential to improve reasoning capabilities.\n\n---\n\n\\*Primary authors. Correspondence to: Karl Cobbe &lt;karl@openai.com>One effective method involves training reward models to discriminate between desirable and undesirable outputs. The reward model can then be used in a reinforcement learning pipeline (Ziegler et al., 2019; Stiennon et al., 2020; Nakano et al., 2021; Ouyang et al., 2022) or to perform search via rejection sampling (Nichols et al., 2020; Shen et al., 2021; Cobbe et al., 2021). While these techniques are useful, the resulting system is only as reliable as the reward model itself. It is therefore important that we study how to most effectively train reliable reward models.\n\nIn closely related work, Uesato et al. (2022) describe two distinct methods for training reward models: outcome supervision and process supervision. Outcome-supervised reward models (ORMs) are trained using only the final result of the model’s chain-of-thought, while process-supervised reward models (PRMs) receive feedback for each step in the chain-of-thought. There are compelling reasons to favor process supervision. It provides more precise feedback, since it specifies the exact location of any errors that occur. It also has several advantages relevant to AI alignment: it is easier for humans to interpret, and it more directly rewards models for following a human-endorsed chain-of-thought. Within the domain of logical reasoning, models trained with outcome supervision regularly use incorrect reasoning to reach the correct final answer (Zelikman et al., 2022; Creswell et al., 2022). Process supervision has been shown to mitigate this misaligned behavior (Uesato et al., 2022).\n\nDespite these advantages, Uesato et al. (2022) found that outcome supervision and process supervision led to similar final performance in the domain of grade school math. We conduct our own detailed comparison of outcome and process supervision, with three main differences: we use a more capable base model, we use significantly more human feedback, and we train and test on the more challenging MATH dataset (Hendrycks et al., 2021).\n\nOur main contributions are as follows:\n\n1. 1. We show that process supervision can train much more reliable reward models than outcome supervision. We use our state-of-the-art PRM to solve 78.2% of problems from a representative subset of the MATH test set.\n2. 2. We show that a large reward model can reliably approximate human supervision for smaller reward models, and that it can be used to efficiently conduct large-scale data collection ablations.\n3. 3. We show that active learning leads to a  $2.6\\times$  improvement in the data efficiency of process supervision.\n4. 4. We release our full process supervision dataset, PRM800K, to promote related research.## 2 Methods\n\nWe perform a comparison of outcome and process supervision, following a similar methodology to Uesato et al. (2022). Outcome supervision can be provided without humans, since all problems in the MATH dataset have automatically checkable answers. In contrast, there is no simple way to automate process supervision. We therefore rely on human data-labelers to provide process supervision, specifically by labelling the correctness of each step in model-generated solutions.\n\nWe conduct experiments in two separate regimes: large-scale and small-scale. Each has its own advantages, and they offer complimentary perspectives. At large-scale, we finetune all models from GPT-4 (OpenAI, 2023). We focus on advancing the state-of-the-art by training the most reliable ORM and PRM possible. Unfortunately the training sets for these reward models are not directly comparable, for reasons we will discuss in Section 3. These models are therefore not ideal for making an apples-to-apples comparison of outcome and process supervision. To address this flaw, we also train models at small-scale, where we can conduct a more direct comparison. In order to remove our dependence on costly human feedback, we use a large-scale model to supervise small-scale model training. This setup enables us to conduct several important ablations that would otherwise be infeasible.\n\n### 2.1 Scope\n\nAt each model scale, we use a single fixed model to generate all solutions. We call this model the *generator*. We do not attempt to improve the generator with reinforcement learning (RL). When we discuss outcome and process supervision, we are specifically referring to the supervision given to the reward model. We do not discuss any supervision the generator would receive from the reward model if trained with RL. Although finetuning the generator with RL is a natural next step, it is intentionally not the focus of this work.\n\nWe instead focus exclusively on how to train the most reliable reward model possible. We evaluate a reward model by its ability to perform best-of-N search over uniformly sampled solutions from the generator. For each test problem we select the solution ranked highest by the reward model, automatically grade it based on its final answer, and report the fraction that are correct. A reward model that is more reliable will select the correct solution more often.\n\n### 2.2 Base Models\n\nAll large-scale models are finetuned from the base GPT-4 model (OpenAI, 2023). This model has been pretrained solely to predict the next token; it has not been pretrained with any Reinforcement Learning from Human Feedback (RLHF) (Christiano et al., 2017). The small-scale base models are similar in design to GPT-4, but they were pretrained with roughly 200 times less compute. As an additional pretraining step, we finetune all models on a dataset of roughly 1.5BThe denominator of a fraction is 7 less than 3 times the numerator. If the fraction is equivalent to  $2/5$ , what is the numerator of the fraction? (Answer: )\n\n😞 😊 😊 Let's call the numerator  $x$ .\n\n😞 😊 😊 So the denominator is  $3x-7$ .\n\n😞 😊 😊 We know that  $x/(3x-7) = 2/5$ .\n\n😞 😊 😊 So  $5x = 2(3x-7)$ .\n\n😞 😊 😊  $5x = 6x - 14$ .\n\n😞 😊 😊 So  $x = 7$ .\n\nFigure 1: A screenshot of the interface used to collect feedback for each step in a solution.\n\nmath-relevant tokens, which we call MathMix. Similar to Lewkowycz et al. (2022), we find that this improves the model’s mathematical reasoning capabilities. Details on how this dataset was constructed can be found in Appendix A.\n\n## 2.3 Generator\n\nTo make parsing individual steps easier, we train the generator to produce solutions in a newline delimited step-by-step format. Specifically, we few-shot generate solutions to MATH training problems, filter to those that reach the correct final answer, and finetune the base model on this dataset for a single epoch. This step is not intended to teach the generator new skills; it is intended only to teach the generator to produce solutions in the desired format.\n\n## 2.4 Data Collection\n\nTo collect process supervision data, we present human data-labelers with step-by-step solutions to MATH problems sampled by the large-scale generator. Their task is to assign each step in the solution a label of *positive*, *negative*, or *neutral*, as shown in Figure 1. A positive label indicates that the step is correct and reasonable. A negative label indicates that the step is either incorrect or unreasonable. A neutral label indicates ambiguity. In practice, a step may be labelled neutral if it is subtly misleading, or if it is a poor suggestion that is technically still valid. We permit neutral labels since this allows us to defer the decision about how to handle ambiguity: at test time, we can treat neutral labels as either positive or negative. A more detailed description of the labelling instructions is provided in Appendix D.\n\nWe label solutions exclusively from the large-scale generator in order to maximize the value of our limited human-data resource. We refer to the entire dataset of step-level labels collected as PRM800K. The PRM800K training set contains 800K step-level labels across 75K solutions to 12K problems. Tominimize overfitting, we include data from 4.5K MATH test problems in the PRM800K training set, and we therefore evaluate our models only on the remaining 500 MATH test problems. More details about this test set can be found in Appendix C.\n\nDuring data collection, we must decide which solutions to surface to data-labelers. The most straightforward strategy is to uniformly surface solutions produced by the generator. However, if we surface solutions that make obvious errors, the human feedback we get is less valuable. We would prefer to surface solutions that are more likely to fool our best reward model. To that end, we attempt to strategically select which solutions to show data-labelers. Specifically, we choose to surface *convincing wrong-answer* solutions. We use the term *convincing* to refer to solutions that are rated highly by our current best PRM, and we use *wrong-answer* to refer to solutions that reach an incorrect final answer. We use this slightly verbose phrasing to emphasize the fact that correctness is determined solely by checking the final answer, a process which occasionally leads to misgraded solutions. We expect to gain more information from labeling convincing wrong-answer solutions, since we know the PRM is mistaken about at least one step in each such solution.\n\nIn addition to using this selection strategy, we also iteratively re-train our PRM using the latest data at several points in the data collection process. At each iteration, we generate  $N$  solutions per problem and surface only the top  $K$  most convincing wrong-answer solutions to data-labelers. We experiment with either applying this top- $K$  filtering at a problem level ( $K$  solutions per problem) or globally across the dataset ( $K$  solutions in total, unequally distributed among problems). Since the data collection process is expensive, it was not feasible to conduct at-scale ablations of these decisions. However, we perform several surrogate ablations in Section 4, using our largest PRM as a labelling oracle for a smaller PRM. More details about data collection can be found in Appendix B.\n\n## 2.5 Outcome-supervised Reward Models (ORMs)\n\nWe train ORMs following a similar methodology to Cobbe et al. (2021). We uniformly sample a fixed number of solutions per problem from the generator, and we train the ORM to predict whether each solution is correct or incorrect. In practice, we usually determine correctness by automatically checking the final answer, but in principle these labels could be provided by humans. At test time, we use the ORM’s prediction at the final token as the overall score for the solution. We note the automatic grading used to determine ORM targets is not perfectly reliable: *false positives* solutions that reach the correct answer with incorrect reasoning will be misgraded. We discuss additional ORM training details in Appendix E.\n\n## 2.6 Process-supervised Reward Models (PRMs)\n\nWe train PRMs to predict the correctness of each step after the last token in each step. This prediction takes the form of a single token, and we maximize theLet  $x^8 + 3x^4 - 4 = p_1(x)p_2(x) \\cdots p_k(x)$ , where each non-constant polynomial  $p_i(x)$  is monic with integer coefficients, and cannot be factored further over the integers. Compute  $p_1(1) + p_2(1) + \\cdots + p_k(1)$ .\n\nI notice that the given polynomial has even degree and only even powers of  $x$ , so I can try to make a substitution to simplify it.\n\nLet  $y = x^4$ , then the polynomial becomes  $y^2 + 3y - 4$ , which is a quadratic equation.\n\nI can factor this quadratic equation as  $(y + 4)(y - 1)$ , so the original polynomial is  $(x^4 + 4)(x^4 - 1)$ .\n\nNow I need to factor each of these factors further, if possible, over the integers.\n\nFor the first factor,  $x^4 + 4$ , I recall the Sophie Germain identity, which says that  $a^4 + 4b^4 = (a^2 + 2b^2 + 2ab)(a^2 + 2b^2 - 2ab)$ .\n\nApplying this identity with  $a = x$  and  $b = 1$ , I get  $x^4 + 4 = (x^2 + 2x + 2)(x^2 - 2x + 2)$ .\n\nFor the second factor,  $x^4 - 1$ , I can use the difference of squares formula, which says that  $a^2 - b^2 = (a + b)(a - b)$ .\n\nApplying this formula with  $a = x^2$  and  $b = 1$ , I get  $x^4 - 1 = (x^2 + 1)(x^2 - 1)$ .\n\nThen I can apply the difference of squares formula again with  $a = x$  and  $b = 1$ , to get  $x^2 - 1 = (x + 1)(x - 1)$ .\n\nSo the original polynomial is  $(x^4 + 4)(x^4 - 1) = (x^2 + 2x + 2)(x^2 - 2x + 2)(x^2 + 1)(x + 1)(x - 1)$ .\n\nThese are all the irreducible factors over the integers, so  $p_1(x) = x^2 + 2x + 2$ ,  $p_2(x) = x^2 - 2x + 2$ ,  $p_3(x) = x^2 + 1$ ,  $p_4(x) = x + 1$ , and  $p_5(x) = x - 1$ .\n\nTo find the sum of their values at  $x = 1$ , I just need to plug in  $x = 1$  into each factor and add them up.\n\nI get  $p_1(1) = 1^2 + 2 \\cdot 1 + 2 = 5$ ,  $p_2(1) = 1^2 - 2 \\cdot 1 + 2 = 1$ ,  $p_3(1) = 1^2 + 1 = 2$ ,  $p_4(1) = 1 + 1 = 2$ , and  $p_5(1) = 1 - 1 = 0$ .\n\nSo the final answer is  $5 + 1 + 2 + 2 + 0 = 10$ .\n\nAnswer: 10\n\nLet  $x^8 + 3x^4 - 4 = p_1(x)p_2(x) \\cdots p_k(x)$ , where each non-constant polynomial  $p_i(x)$  is monic with integer coefficients, and cannot be factored further over the integers. Compute  $p_1(1) + p_2(1) + \\cdots + p_k(1)$ .\n\nThis problem is about factoring a polynomial over the integers, which can be a tricky task.\n\nOne possible strategy is to look for rational roots of the polynomial, using the rational root theorem.\n\nHowever, that would involve checking a lot of possible factors of  $-4$ , and there is no guarantee that the polynomial has any rational roots at all.\n\nAnother possible strategy is to use some algebraic tricks to simplify the polynomial or reduce its degree.\n\nI notice that the polynomial has only even powers of  $x$ , so I can try to substitute  $y = x^2$  and see what happens.\n\nThen the polynomial becomes  $y^4 + 3y^2 - 4$ , which is a quadratic equation in  $y^2$ .\n\nI can try to factor this quadratic equation by looking for two numbers that multiply to  $-4$  and add to  $3$ .\n\nThose numbers are  $4$  and  $-1$ , so I can write  $y^4 + 3y^2 - 4 = (y^2 + 4)(y^2 - 1)$ .\n\nNow I can substitute back  $x^2 = y$  and get  $x^8 + 3x^4 - 4 = (x^4 + 4)(x^4 - 1)$ .\n\nThis looks promising, because I have reduced the degree of the factors from  $8$  to  $4$ .\n\nI can try to factor each of these factors further, using the difference of squares formula.\n\nI get  $x^8 + 3x^4 - 4 = (x^4 + 4)(x^2 - 2)(x^2 + 1)(x^2 - 1)$ .\n\nI can apply the difference of squares formula again to the last factor and get  $x^8 + 3x^4 - 4 = (x^4 + 4)(x^2 - 2)(x^2 + 1)(x + 1)(x - 1)$ .\n\nNow I have factored the polynomial completely into monic linear and quadratic factors with integer coefficients.\n\nThese are the  $p_i(x)$ 's that the problem is asking for.\n\nTo find the sum of their values at  $x = 1$ , I just need to plug in  $x = 1$  into each factor and add them up.\n\nI get  $p_1(1) + p_2(1) + \\cdots + p_5(1) = (1^4 + 4)(1^2 - 2)(1^2 + 1)(1 + 1)(1 - 1)$ .\n\nSimplifying, I get  $p_1(1) + p_2(1) + \\cdots + p_5(1) = (5)(-1)(2)(2)(0)$ .\n\nMultiplying, I get  $p_1(1) + p_2(1) + \\cdots + p_5(1) = 0$ .\n\nAnswer: 0\n\nFigure 2: Two solutions to the same problem, graded by the PRM. The solution on the left is correct while the solution on the right is incorrect. A green background indicates a high PRM score, and a red background indicates a low score. The PRM correctly identifies the mistake in the incorrect solution.\n\nlog-likelihood of these target tokens during training. The PRM can therefore be trained in a standard language model pipeline without any special accommodations. To determine the step-level predictions at test time, it suffices to perform a single PRM forward pass over the whole solution. We visualize large-scale PRM scores for two different solutions in Figure 2. To compare multiple solutions, it is necessary to compute a single score for each solution. This is an important but straightforward detail: we define the PRM score for a solution to be the probability that every step is correct under the PRM. We implement this as the product of the correctness probabilities for each step. We describe other possible scoring strategies and additional PRM training details in Appendix F.\n\nWhen we provide process supervision, we deliberately choose to supervise only up to the first incorrect step. This makes the comparison between outcome and process supervision more straightforward. For correct solutions, both methods provide the same information, namely that every step is correct. For incorrect solutions, both methods reveal the existence of at least one mistake, and process supervision additionally reveals the precise location of that mistake. If we were to provide additional process supervision beyond the first mistake, then process supervision would have an even greater information advantage. This decision also keeps the labelling cost similar for humans: without relying on an easy-to-check final answer, determining the correctness of a solution is equivalent to identifying its first mistake. While most MATH problems do have easy-to-check final answers, we expect this to not remain true in more complex domains.&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>&lt;/th>\n&lt;th>ORM&lt;/th>\n&lt;th>PRM&lt;/th>\n&lt;th>Majority Voting&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>% Solved (Best-of-1860)&lt;/td>\n&lt;td>72.4&lt;/td>\n&lt;td>&lt;b>78.2&lt;/b>&lt;/td>\n&lt;td>69.6&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nFigure 3: A comparison of outcome-supervised and process-supervised reward models, evaluated by their ability to search over many test solutions. Majority voting is shown as a strong baseline. For  $N \\leq 1000$ , we visualize the variance across many subsamples of the 1860 solutions we generated in total per problem.\n\n### 3 Large-scale Supervision\n\nWe train the large-scale PRM using the step-level labels in PRM800K. To ensure the large-scale ORM baseline is as strong as possible, we train on 100 uniform samples per problem from the generator. This means the ORM training set has no overlap with PRM800K, and it is an order of magnitude larger. Although these two training sets are not directly comparable, each represents our best attempt to advance the state-of-the-art with each form of supervision. We note that training the ORM solely on PRM800K solutions would be problematic, since our active learning strategy has heavily biased the dataset towards wrong-answer solutions. We did explore training the ORM on a superset of PRM800K solutions, by mixing in uniformly sampled solutions, but we found that this did not improve ORM performance.\n\nFigure 3 shows how the best-of-N performance of each reward model varies as a function of N. Since majority voting is known to be a strong baseline (Wang et al., 2022; Lewkowycz et al., 2022), we also include this method as a point of comparison. While the ORM performs slightly better than the majority voting baseline, the PRM strongly outperforms both. Not only does the PRM reach higher performance for all values of N, but the performance gap widens as N increases. This indicates that the PRM is more effective than both the ORM and majority voting at searching over a large number of model-generated solutions.(a) Four series of reward models trained using different data collection strategies, compared across training sets of varying sizes.\n\n(b) Three reward models trained on 200 samples/problem using different forms of supervision, compared across many test-time compute budgets.\n\nFigure 4: A comparison of different forms of outcome and process supervision. Mean and standard deviation is shown across three seeds.\n\nWe experimented with using RM-weighted voting (Li et al., 2022; Uesato et al., 2022) to combine the benefits of the PRM and majority voting, but this did not noticeably improve performance. We use a specific subset of the MATH test set for evaluation, which we describe in Appendix C. We further break down these results by problem difficulty in Appendix G.\n\n## 4 Small-scale Synthetic Supervision\n\nWe find that the PRM outperforms the ORM at large-scale, but this result alone paints an incomplete picture. To better compare outcome and process supervision, there are two confounding factors that must be isolated. First, the training sets for the ORM and the PRM are not directly comparable: the PRM training set was constructed using active learning, is biased towards answer-incorrect solutions, and is an order of magnitude smaller. Second, the final-answer grading will provide positive labels to spurious solutions that reach the correct final answer despite incorrect reasoning. This could damage ORM performance, an effect we may or may not want to attribute to outcome supervision more generally.\n\nDue to the high cost of collecting human feedback, we cannot easily ablate these factors using human labelers. We instead perform the relevant ablations by using the large-scale PRM to supervise smaller models. This setup enables us to simulate a large amount of data collection at a modest cost. For the remainder of this section, we refer to the large-scale PRM from Section 3 as PRM&lt;sub>large&lt;/sub>.## 4.1 Process vs Outcome Supervision\n\nWe now conduct a direct comparison of outcome and process supervision. We first sample between 1 and 200 solutions per problem from a small-scale generator. For each dataset, we provide three forms of supervision: process supervision from  $\\text{PRM}_{\\text{large}}$ , outcome supervision from  $\\text{PRM}_{\\text{large}}$ , and outcome supervision from final-answer checking. The choice of supervision is the only difference between these three series of reward models, which are otherwise trained on identical datasets. See Appendix H for more details about how  $\\text{PRM}_{\\text{large}}$  is used for outcome and process supervision.\n\nIn Figure 4a, we evaluate each reward model by its best-of-500 selection. We see that process supervision significantly outperforms both forms of outcome supervision at all data collection scales. In Figure 4b, we evaluate the best reward model from each series by its best-of-N performance across different values of N. We see that using  $\\text{PRM}_{\\text{large}}$  for outcome supervision is noticeably more effective than final-answer checking. This can be explained by the fact that  $\\text{PRM}_{\\text{large}}$  provides better supervision for solutions that reach the correct final answer using incorrect reasoning.\n\nIt is not clear whether supervision by  $\\text{PRM}_{\\text{large}}$  or by final-answer checking represents the more appropriate outcome supervision baseline. While final-answer supervision is more explicitly outcome based, its main weakness — the existence of false positives — is arguably over-emphasized in the MATH dataset. Outcome supervision by  $\\text{PRM}_{\\text{large}}$  better represents outcome supervision in domains that are less susceptible to false positives. We consider outcome supervision by  $\\text{PRM}_{\\text{large}}$  to be the more relevant baseline, but we encourage the reader to draw their own conclusions.\n\n## 4.2 Active Learning\n\nFinally, we investigate the impact of active learning. We train a small-scale reward model,  $\\text{PRM}_{\\text{selector}}$ , on a single sample from each problem, and we use this model to score 1000 samples per problem. To train each of our larger reward models, we select  $N$  samples per problem such that 80% are the most convincing (according to  $\\text{PRM}_{\\text{selector}}$ ) wrong-answer samples, and 20% are the most convincing samples that remain (right- or wrong-answer). We score the selected samples with  $\\text{PRM}_{\\text{large}}$  and train on those scores. This process ensures that all samples are relatively convincing under  $\\text{PRM}_{\\text{selector}}$ , that a large fraction are known to contain at least one mistake, and that our overall dataset is not too heavily biased toward wrong-answer solutions. Performance of this data labelling scheme is shown in Figure 4a. By comparing the slopes of the line of best fit with and without active learning, we estimate that this form of active learning is approximately 2.6x more data efficient than uniform data labelling. We note that the model trained on the largest active learning dataset (200 samples per problem) appears to slightly underperform the expected trend line. Our best explanation for this observation is that 200 samples represents a significant fraction of the overall selection pool (1000 samples) and that this&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>&lt;/th>\n&lt;th>ORM&lt;/th>\n&lt;th>PRM&lt;/th>\n&lt;th>Majority Vote&lt;/th>\n&lt;th># Problems&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>AP Calculus&lt;/td>\n&lt;td>68.9%&lt;/td>\n&lt;td>&lt;b>86.7%&lt;/b>&lt;/td>\n&lt;td>80.0%&lt;/td>\n&lt;td>45&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>AP Chemistry&lt;/td>\n&lt;td>68.9%&lt;/td>\n&lt;td>&lt;b>80.0%&lt;/b>&lt;/td>\n&lt;td>71.7%&lt;/td>\n&lt;td>60&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>AP Physics&lt;/td>\n&lt;td>77.8%&lt;/td>\n&lt;td>&lt;b>86.7%&lt;/b>&lt;/td>\n&lt;td>82.2%&lt;/td>\n&lt;td>45&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>AMC10/12&lt;/td>\n&lt;td>49.1%&lt;/td>\n&lt;td>&lt;b>53.2%&lt;/b>&lt;/td>\n&lt;td>32.8%&lt;/td>\n&lt;td>84&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Aggregate&lt;/td>\n&lt;td>63.8%&lt;/td>\n&lt;td>&lt;b>72.9%&lt;/b>&lt;/td>\n&lt;td>61.3%&lt;/td>\n&lt;td>234&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nTable 1: We measure out-of-distribution generalization using recent STEM tests. We evaluate the outcome-supervised RM, the process-supervised RM, and majority voting using 100 test samples per problem.\n\nrelative lack of diversity limits the possible upside from active learning.\n\nWe also performed a preliminary investigation into the impact of iteratively retraining  $\\text{PRM}_{\\text{selector}}$  throughout data collection. Between iterations, we retrained  $\\text{PRM}_{\\text{selector}}$  using all currently labeled data. Unfortunately, we observed instability in this process which we were unable to diagnose. The resulting reward models performed no better than the models described above. We expect some form of iterative retraining to be beneficial in active learning, but we currently have no concrete evidence to support this claim. We consider this a compelling direction for future research.\n\n## 5 OOD Generalization\n\nTo get some measure of out-of-distribution generalization, we evaluate our large-scale ORM and PRM on a held-out set of 224 STEM questions, pulled from the most recent AP Physics, AP Calculus, AP Chemistry, AMC10, and AMC12 exams. Since these tests were released after the pre-training dataset was compiled, we can have high confidence that the model has not seen these problems. We report the best-of-100 performance of the ORM, PRM and majority voting in Table 1. We observe results similar to those in Section 3: the PRM outperforms both the ORM and majority voting. This shows us that the PRM can tolerate a modest amount of distribution shift and that its strong performance holds up on fresh test questions.\n\n## 6 Discussion\n\n### 6.1 Credit Assignment\n\nOne clear advantage of process supervision is that it provides more precise feedback than outcome supervision. A reward model trained with outcome supervision faces a difficult credit-assignment task — to generalize well, it must determine where an incorrect solution went wrong. This is particularly difficult for hard problems: most model-generated solutions contain an error somewhere, so the marginal value of a negative label from outcome supervision is low. Incontrast, process supervision provides a richer signal: it specifies both how many of the first steps were in fact correct, as well as the precise location of the incorrect step. Process supervision makes credit assignment easier, and we believe that this explains its strong performance.\n\n## 6.2 Alignment Impact\n\nProcess supervision has several advantages over outcome supervision related to AI alignment. Process supervision is more likely to produce interpretable reasoning, since it encourages models to follow a process endorsed by humans. Process supervision is also inherently safer: it directly rewards an aligned chain-of-thought rather than relying on outcomes as a proxy for aligned behavior (Stuhlmüller and Byun, 2022). In contrast, outcome supervision is harder to scrutinize, and the preferences conveyed are less precise. In the worst case, the use of outcomes as an imperfect proxy could lead to models that become misaligned after learning to exploit the reward signal (Uesato et al., 2022; Cotra, 2022; Everitt et al., 2017).\n\nIn some cases, safer methods for AI systems can lead to reduced performance (Ouyang et al., 2022; Askell et al., 2021), a cost which is known as an alignment tax. In general, any alignment tax may hinder the adoption of alignment methods, due to pressure to deploy the most capable model. Our results show that process supervision in fact incurs a negative alignment tax. This could lead to increased adoption of process supervision, which we believe would have positive alignment side-effects. It is unknown how broadly these results will generalize beyond the domain of math, and we consider it important for future work to explore the impact of process supervision in other domains.\n\n## 6.3 Test Set Contamination\n\nThe test set of the MATH dataset contains problems that are discussed in several online venues, and it is likely that some of these problems appear in the pretraining dataset for our models. We attempted to remove all MATH problems from our MathMix dataset using string-matching heuristics, but since humans can post hard-to-detect rephrasings of a problem online, it is difficult to make any strong guarantees about the overlap between MathMix and the MATH dataset.\n\nIn our experience inspecting model-generated solutions, we saw no clear signs of our models memorizing MATH problems. However, it is impossible to rule out subtle forms of memorization that would slip past manual inspection, and it is still possible that some degree of contamination has slightly inflated our performance on the MATH test set. Even in that case, we would expect any contamination to manifest similarly across all methods, and that the relative comparisons made throughout this work would remain mostly unaffected.\n\nWe also note that the PRM regularly surfaces correct solutions to MATH problems that have a low single-digit percentage solve-rate under the generator, some examples of which can be seen in Appendix I. The generator’s lowsolve-rate is an additional indication that it has not encountered such problems via test set contamination. Our generalization results from Section 5 further strengthen our claim that test set contamination has not significantly impacted this work, since we observe qualitatively similar results on problems that are guaranteed to be uncontaminated.\n\n## 7 Related Work\n\n### 7.1 Outcome vs Process Supervision\n\nIn work closely related to our own, Uesato et al. (2022) compare the impact of outcome and process supervision in the domain of grade school math. They found that both methods led to similar final-answer error rates, and that process supervision achieved those results with less data. While our core methodology is very similar, there are three main details that differ. First, we use a more capable model to collect PRM800K dataset and to perform our large-scale experiments. However, our small-scale results in Section 4 suggest that large-scale models are not necessary to observe benefits from process supervision. Second, we evaluate on the MATH dataset, which is significantly more challenging than GSM8K. Third, we collect a much larger quantity of process supervision data.\n\nOn the surface, the results from Uesato et al. (2022) may seem to conflict with our claim that process supervision leads to better performance. However, we believe the apparent conflict can be explained by the difference in the scale of the supervision. The data scaling trend in Figure 4a suggests that a small amount of process supervision and a large amount of outcome supervision do in fact lead to similar performance, consistent with the results from Uesato et al. (2022). The trend also shows that process supervision beats outcome supervision when scaled up, even when judged based solely on outcomes. This is consistent with our results in Section 3. We believe these results make a strong case for using process supervision.\n\n### 7.2 Synthetic Supervision\n\nSimilar to our work in Section 4, Gao et al. (2022) use a large reward model to supervise the training of smaller models. They study the over-optimization that occurs during RLHF, with experiments that require large quantities of human preference data. To work around this challenge, they use a gold-standard reward model to replace human feedback. Our use of a large-scale reward model to supervise smaller reward models shares similarities with their approach.\n\n### 7.3 Natural Language Reasoning\n\nSeveral recent studies that have examined the reasoning ability of large language models are implicitly relevant to our work. Lewkowycz et al. (2022) showed that finetuning models on a large corpus of technical content led to significantly improved performance on MATH. Wang et al. (2022) showed that *self-consistency*leads to remarkably strong performance on many reasoning benchmarks, notably without requiring any additional finetuning. Wei et al. (2022) and Nye et al. (2021) demonstrate the importance of explicitly performing intermediate reasoning steps via a *chain of thought* or a *scratchpad* in order to solve tasks that require multi-step reasoning. Kojima et al. (2022) show that models are able to perform this behavior zero-shot, conditioned only on a simple prompt.\n\n## 8 Conclusion\n\nWe have shown that process supervision can be used to train much more reliable reward models than outcome supervision in the domain of mathematical reasoning. We have also shown that active learning can be used to lower the cost of human data collection by surfacing only the most valuable model completions for human feedback. We release PRM800K, the full dataset of human feedback used to train our state-of-the-art reward model, with the hope that removing this significant barrier to entry will catalyze related research on the alignment of large language models. We believe that process supervision is currently under-explored, and we are excited for future work to more deeply investigate the extent to which these methods generalize.\n\n## Acknowledgements\n\nWe thank Joshua Achiam, Mark Chen, Jonathan Gordon, Dan Hendrycks, Lukasz Kaiser, Oleg Murk, Ben Sokolowsky, Francis Song, and Jonathan Uesato for valuable feedback and thoughtful discussions; Giambattista Parascandolo and Daniel Selsam for their contributions to the MathMix dataset; Jonathan Ward for contributing to the data collection interface; Wojciech Zaremba for encouraging us to scale up data collection; Peter Hoeschele and Aris Kostantinidis for supporting our data collection; the research acceleration and supercomputing teams at OpenAI for providing infrastructure support; and the team at Scale and the many data-labelers who created PRM800K.\n\n## References\n\n- A. Askell, Y. Bai, A. Chen, D. Drain, D. Ganguli, T. Henighan, A. Jones, N. Joseph, B. Mann, N. DasSarma, et al. A general language assistant as a laboratory for alignment. *arXiv preprint arXiv:2112.00861*, 2021.\n- S. Bubeck, V. Chandrasekaran, R. Eldan, J. Gehrke, E. Horvitz, E. Kamar, P. Lee, Y. T. Lee, Y. Li, S. Lundberg, et al. Sparks of artificial general intelligence: Early experiments with gpt-4. *arXiv preprint arXiv:2303.12712*, 2023.P. F. Christiano, J. Leike, T. Brown, M. Martic, S. Legg, and D. Amodei. Deep reinforcement learning from human preferences. *Advances in neural information processing systems*, 30, 2017.\n\nK. Cobbe, V. Kosaraju, M. Bavarian, M. Chen, H. Jun, L. Kaiser, M. Plappert, J. Tworek, J. Hilton, R. Nakano, et al. Training verifiers to solve math word problems. *arXiv preprint arXiv:2110.14168*, 2021.\n\nA. Cotra. Without specific countermeasures, the easiest path to transformative AI likely leads to AI takeover. &lt;https://www.alignmentforum.org/posts/pRkFkzwKZ2zfa3R6H/without-specific-countermeasures-the-easiest-path-to>, 2022.\n\nA. Creswell, M. Shanahan, and I. Higgins. Selection-inference: Exploiting large language models for interpretable logical reasoning. *arXiv preprint arXiv:2205.09712*, 2022.\n\nT. Everitt, V. Krakovna, L. Orseau, M. Hutter, and S. Legg. Reinforcement learning with a corrupted reward channel. *arXiv preprint arXiv:1705.08417*, 2017.\n\nL. Gao, J. Schulman, and J. Hilton. Scaling laws for reward model overoptimization. *arXiv preprint arXiv:2210.10760*, 2022.\n\nD. Hendrycks, C. Burns, S. Kadavath, A. Arora, S. Basart, E. Tang, D. Song, and J. Steinhardt. Measuring mathematical problem solving with the math dataset. *arXiv preprint arXiv:2103.03874*, 2021.\n\nT. Kojima, S. S. Gu, M. Reid, Y. Matsuo, and Y. Iwasawa. Large language models are zero-shot reasoners. *arXiv preprint arXiv:2205.11916*, 2022.\n\nA. Lewkowycz, A. Andreassen, D. Dohan, E. Dyer, H. Michalewski, V. Ramasesh, A. Slone, C. Anil, I. Schlag, T. Gutman-Solo, et al. Solving quantitative reasoning problems with language models. *arXiv preprint arXiv:2206.14858*, 2022.\n\nY. Li, Z. Lin, S. Zhang, Q. Fu, B. Chen, J.-G. Lou, and W. Chen. On the advance of making language models better reasoners. *arXiv preprint arXiv:2206.02336*, 2022.\n\nJ. Maynez, S. Narayan, B. Bohnet, and R. McDonald. On faithfulness and factuality in abstractive summarization. *arXiv preprint arXiv:2005.00661*, 2020.\n\nR. Nakano, J. Hilton, S. Balaji, J. Wu, L. Ouyang, C. Kim, C. Hesse, S. Jain, V. Kosaraju, W. Saunders, et al. Webgpt: Browser-assisted question-answering with human feedback. *arXiv preprint arXiv:2112.09332*, 2021.\n\nE. Nichols, L. Gao, and R. Gomez. Collaborative storytelling with large-scale neural language models. In *Proceedings of the 13th ACM SIGGRAPH Conference on Motion, Interaction and Games*, pages 1–10, 2020.M. Nye, A. J. Andreassen, G. Gur-Ari, H. Michalewski, J. Austin, D. Bieber, D. Dohan, A. Lewkowycz, M. Bosma, D. Luan, et al. Show your work: Scratchpads for intermediate computation with language models. *arXiv preprint arXiv:2112.00114*, 2021.\n\nOpenAI. Gpt-4 technical report. *arXiv preprint arXiv:2303.08774*, 2023.\n\nL. Ouyang, J. Wu, X. Jiang, D. Almeida, C. L. Wainwright, P. Mishkin, C. Zhang, S. Agarwal, K. Slama, A. Ray, et al. Training language models to follow instructions with human feedback. *arXiv preprint arXiv:2203.02155*, 2022.\n\nJ. Shen, Y. Yin, L. Li, L. Shang, X. Jiang, M. Zhang, and Q. Liu. Generate & rank: A multi-task framework for math word problems. *arXiv preprint arXiv:2109.03034*, 2021.\n\nN. Stiennon, L. Ouyang, J. Wu, D. Ziegler, R. Lowe, C. Voss, A. Radford, D. Amodei, and P. F. Christiano. Learning to summarize with human feedback. *Advances in Neural Information Processing Systems*, 33:3008–3021, 2020.\n\nA. Stuhlmüller and J. Byun. Supervise process, not outcomes. &lt;https://ought.org/updates/2022-04-06-process>, 2022.\n\nJ. Uesato, N. Kushman, R. Kumar, F. Song, N. Siegel, L. Wang, A. Creswell, G. Irving, and I. Higgins. Solving math word problems with process-and outcome-based feedback. *arXiv preprint arXiv:2211.14275*, 2022.\n\nX. Wang, J. Wei, D. Schuurmans, Q. Le, E. Chi, and D. Zhou. Self-consistency improves chain of thought reasoning in language models. *arXiv preprint arXiv:2203.11171*, 2022.\n\nJ. Wei, X. Wang, D. Schuurmans, M. Bosma, E. Chi, Q. Le, and D. Zhou. Chain of thought prompting elicits reasoning in large language models. *arXiv preprint arXiv:2201.11903*, 2022.\n\nE. Zelikman, Y. Wu, J. Mu, and N. Goodman. Star: Bootstrapping reasoning with reasoning. *Advances in Neural Information Processing Systems*, 35: 15476–15488, 2022.\n\nD. M. Ziegler, N. Stiennon, J. Wu, T. B. Brown, A. Radford, D. Amodei, P. Christiano, and G. Irving. Fine-tuning language models from human preferences. *arXiv preprint arXiv:1909.08593*, 2019.## A MathMix\n\nSimilar to Lewkowycz et al. (2022) we construct a large-scale dataset of high-quality math-relevant tokens for use in a lightweight pretraining stage, before finetuning on comparably smaller datasets like MATH and PRM800K. This dataset, which we call MathMix, has two main differences compared to the one used to train Minerva. First, it is smaller and more aggressively filtered to high-quality math problem-solving content, and second, it does not explicitly mix in general language data.\n\nMinerva was trained on 38.5B tokens of arXiv documents and webscraper pages with LaTeX content, while MathMix consists of a smaller set of 1.5B tokens containing individual math problems and their solutions, free-form text discussing math problems and concepts, and synthetic data (Table 2). While Minerva was pretrained on a dataset with 5% general natural language data, we chose not to mix in any natural language data explicitly, primarily because MathMix already contains plenty of natural language data.\n\n&lt;table border=\"1\">&lt;thead>&lt;tr>&lt;th>Data type&lt;/th>&lt;th>Token count&lt;/th>&lt;th>Present in pretraining?&lt;/th>&lt;/tr>&lt;/thead>&lt;tbody>&lt;tr>&lt;td>Math problems and solutions&lt;/td>&lt;td>~ 275M&lt;/td>&lt;td>No&lt;/td>&lt;/tr>&lt;tr>&lt;td>Free-form math discussion text (1)&lt;/td>&lt;td>~ 430M&lt;/td>&lt;td>No&lt;/td>&lt;/tr>&lt;tr>&lt;td>Free-form math discussion text (2)&lt;/td>&lt;td>~ 450M&lt;/td>&lt;td>Yes&lt;/td>&lt;/tr>&lt;tr>&lt;td>Synthetic data (1)&lt;/td>&lt;td>~ 30M&lt;/td>&lt;td>No&lt;/td>&lt;/tr>&lt;tr>&lt;td>Synthetic data (2)&lt;/td>&lt;td>~ 100M&lt;/td>&lt;td>Yes&lt;/td>&lt;/tr>&lt;tr>&lt;td>Critiques grading data&lt;/td>&lt;td>~ 500M&lt;/td>&lt;td>No&lt;/td>&lt;/tr>&lt;/tbody>&lt;/table>\n\nTable 2: MathMix dataset components.\n\nNote that when training smaller models, as in Section 4, we use a slightly smaller variant of MathMix that excludes the critiques data and only consists of 1B tokens. For our large models experiments, we train on MathMix for roughly 3B tokens (2 epochs). For our small models experiments, we train for 6 epochs (roughly 6.6B tokens).\n\nWe apply a set of decontamination checks on MathMix against the test split of the MATH dataset, including stripping out LaTeX and searching for matching n-grams, but we can make no strong guarantees on the efficacy of this decontamination. As discussed in Section 6.3, we would not expect the relative comparisons made throughout this work to be significantly impacted by test set contamination.## B PRM800K\n\nWe collected 1,085,590 step-level labels over 101,599 solution samples. We present the whole unfiltered dataset as PRM800K. During training we discard labels used for quality control, as well as any step-level labels for which the labeler was unable to complete the task. The filtered dataset contains about 800,000 step-level labels over 75,000 solutions. The full PRM800K dataset is available at &lt;https://github.com/openai/prm800k>.\n\nThe data collection was split into two separate phases. In phase 1, we collected labels for multiple alternative completions at each step of a solution. This seeded our dataset but was cumbersome—for many steps the alternatives were repetitive, and we found labelers spent a lot of time supervising long uninteresting solutions. As a result, the step-level labels we collected in this phase are more repetitive than those collected later. In total, phase 1 represents about 5% of PRM800K, or about 40,000 step-level labels.\n\nThe majority of our labels were collected as part of phase 2, during which we scaled up and streamlined the data collection process. Phase 2 data collection is split into 10 generations. For each generation, we sample  $N$  solutions per problem from the generator. We rank these solutions with our current best PRM and surface the highest scoring wrong-answer solutions to our labelers. We retrain this PRM between each generation using all the latest data. This active learning strategy changes the balance of our data considerably. Though we sometimes surfaced correct solutions (either by manually injecting correct solutions or because of errors in our automatic grading), the vast majority of the labels we collected in this phase are for incorrect solutions. Table 3 breaks down the balance of correct/incorrect steps and solutions between the different phases of data collection. Though we mostly collected labels on incorrect solutions, we still collected many labels for correct individual steps. In fact, our small-scale ablations in Section 4.2 suggest that this active learning strategy, which favors labelling high-scoring wrong-answer solutions, improves performance despite the resulting imbalance in the dataset.\n\n&lt;table border=\"1\">&lt;thead>&lt;tr>&lt;th>&lt;/th>&lt;th>phase 1&lt;/th>&lt;th>phase 2&lt;/th>&lt;th>combined&lt;/th>&lt;/tr>&lt;/thead>&lt;tbody>&lt;tr>&lt;td>% end in correct solution&lt;/td>&lt;td>85.1&lt;/td>&lt;td>13.2&lt;/td>&lt;td>14.2&lt;/td>&lt;/tr>&lt;tr>&lt;td>% correct steps&lt;/td>&lt;td>58.6&lt;/td>&lt;td>74.1&lt;/td>&lt;td>73.1&lt;/td>&lt;/tr>&lt;/tbody>&lt;/table>\n\nTable 3: Distribution of positive/negative steps/solutions.\n\nSome of our phase 2 questions are intended for quality control. For a quality control question, researchers mark which steps are reasonable to label as incorrect. Then we assess that labelers are able to consistently mark those steps as incorrect. Prior to starting on phase 2, we required all labelers to label 30 quality control questions. This served as a screening test, and we only admitted labelers that agreed with our gold labels at least 75% of the time.\n\nWe then designated 10-20 problems per generation as additional quality control questions, and we randomly served them to labelers as they workedthrough the task. We used the results of this continuous quality control to remove labelers whose quality slipped too far, as well as to prepare educational material on common mistakes in order to improve labeler alignment with our instructions.\n\n## C Evaluation\n\nAs we scaled up the project, we began having to collect labels on multiple solutions for the same training problem. In order to avoid the risk of over-fitting on the 7,500 MATH training problems, we expanded the training set to include 4,500 MATH test split problems. We therefore evaluate our models only on the remaining 500 held-out problems. We selected these 500 test problems uniformly at random. In Figure 5, we show that the distribution of difficulty levels and subjects in this subset is representative of the MATH test set as a whole. The specific test set we used can be found at &lt;https://github.com/openai/prm800k>. We leave it for future work to explore how many distinct training problems are actually necessary, and how quickly our methods overfit to the training set.\n\nFigure 5: Two histograms comparing the distribution of problem difficulty levels and subjects in both the original MATH test set and in our 500 problem test subset.## D Labelling Instructions\n\nLabelers were tasked to look at steps in a solution and label each one as **positive**, **negative**, or **neutral**. A step is considered **neutral** if it is appropriate in context, reasonable, correct, and contains only computations that can be verified easily. A step is **positive** if it is **neutral** and also progresses towards the solution. All other steps are considered **negative**. Labelers were not given reference solutions, but they were given the ground truth final answers. We chose not to provide reference solutions to avoid biasing them towards one particular path to the solution. We chose to provide ground truth final answers since this information can sometimes help labelers resolve their own misunderstandings.\n\nIn phase 1, labelers were permitted to enter their own steps in the case that all candidate steps were **negative**. Then the solution would progress from a randomly selected **positive** step (or **neutral** if there were no **positive** ones). This often resulted in trajectories that got stuck in endless sequences of **neutral** steps that said reasonable things but made frustratingly slow progress towards a solution or **negative** steps that needed constant human supervision. In phase 2, we pre-generate whole solutions and end the task as soon as the first **negative** step is encountered. The full instructions given to labelers can be found at &lt;https://github.com/openai/prm800k/tree/main/prm800k/instructions>.\n\n## E ORM Training Details\n\nWe train outcome-supervised reward models in the same manner as token-level verifiers from Cobbe et al. (2021), with a few subtle differences to hyperparameters. In particular, we only train for a single epoch on each dataset of model samples and reward model labels, without dropout, and without jointly learning a language modeling objective. We find that performance is not sensitive to most other hyperparameters, within a reasonable range.\n\nTo collect model samples, we simply sample uniformly from the generator at a temperature of 1.0 without applying any rebalancing of positives or negatives. At training time, the reward model makes predictions for every token in the context. The target for each token in a solution is the same, based on whether the solution is labelled correct or incorrect. At test time, we simply use the score of the final token in the completion as the overall score of the solution. We note that this setup is identical to the way token-level verifiers were trained in Cobbe et al. (2021).## F PRM Details\n\n### F.1 Training\n\nWe train our PRMs by fine-tuning the MathMix model to predict the probability of positive, negative, and neutral labels given a solution prefix ending in one of our labeled steps. We sweep over hyperparameters using a dataset containing the first  $\\sim 10\\%$  of PRM800K. Fine-tuning an LLM from its ordinary language modeling task to a classification task like this is a large distribution shift, and we found low learning rates were important to stable PRM training.\n\nAll of our PRMs are trained for 2 epochs. On smaller datasets (such as in phase 1 and the first few generations of phase 2) this improves the final performance over training for just 1 epoch. Additional epochs, up to some point, don't noticeably help or hurt performance. On larger datasets, the benefits of 2 epoch training diminishes, but we continue doing it for consistency.\n\n### F.2 Scoring\n\nThere are multiple ways of using the PRM to score solutions. In general, we produce a single solution-level score by performing a reduction over step-level scores, where the step-level score is the probability that the step's label is positive. This involves two specific implementation decisions. First, when determining a step-level score, we either consider a neutral label to be positive or negative. Second, when determining a solution-level score, we either use the minimum or the product over step-level scores as a reduction.\n\nWe show results from all four scoring strategies in Table 4. The best performing strategy is to take the product of step-level scores and to consider the neutrals as positives, but the difference in performance between all strategies is minor. Throughout the rest of this work, we consider neutral steps to be positive, and we define the solution score to be the product of step-level scores. Using the product instead of the minimum as the reduction does create a slight bias against solutions with a larger number of steps.\n\n&lt;table>&lt;thead>&lt;tr>&lt;th>&lt;/th>&lt;th>product&lt;/th>&lt;th>minimum&lt;/th>&lt;/tr>&lt;/thead>&lt;tbody>&lt;tr>&lt;td>neutral = positive&lt;/td>&lt;td>78.2%&lt;/td>&lt;td>77.6%&lt;/td>&lt;/tr>&lt;tr>&lt;td>neutral = negative&lt;/td>&lt;td>77.4%&lt;/td>&lt;td>77.8%&lt;/td>&lt;/tr>&lt;/tbody>&lt;/table>\n\nTable 4: Best-of-1860 test performance using the PRM with four different scoring strategies.## G Difficulty Breakdown\n\nWe show performance of our ORM and PRM on each quintile of the MATH dataset. We determine quintiles based on the pass rate under the generator. It is interesting to note that the performance gap is not only apparent on high difficulty problems: it is in fact apparent across all difficulties. For the lowest difficulty problems, we see that it is possible to find adversarial examples that fool the ORM, since the ORM’s performance slightly decreases as the number of samples increases. In contrast, the PRM remains highly robust over this same set of samples.\n\nWe also see that increasing the number of samples has the largest positive effect on the highest difficulty problems. This is to be expected, since a large number of generator samples may be required to find a true and convincing solution to a hard problem.\n\nFigure 6: A breakdown of ORM vs PRM performance by problem difficulty.## H Synthetic Supervision Details\n\nWe can use  $\\text{PRM}_{\\text{large}}$  to provide either outcome or process supervision for smaller models. We determine the labels for individual steps based on the step-level probabilities outputted by  $\\text{PRM}_{\\text{large}}$ . To do this, we set an arbitrary threshold: any step that  $\\text{PRM}_{\\text{large}}$  assigns a negative label with greater than 20% probability is considered incorrect. We choose this threshold based on the observation that  $\\text{PRM}_{\\text{large}}$  is slightly miscalibrated in the direction of favoring positive labels.\n\nTo provide process supervision for a solution, we directly return the step-level labels (positive or negative) provided by  $\\text{PRM}_{\\text{large}}$ , up until the first step that is marked as negative. This mimics our true human data collection process. To provide outcome supervision, we mark the solution as correct if and only if  $\\text{PRM}_{\\text{large}}$  considers every step to be correct (using the same thresholding logic).# I PRM Visualizations\n\nAll examples shown come from the large-scale generator (GPT-4). We note the pass-rate under the generator to give some sense of the difficulty of these problems.\n\n## I.1 True Positives\n\nThese cherry-picked examples show the best-of-1860 solution from the generator as ranked by the large-scale PRM.\n\nProblem 1. Generator pass-rate: 0.1%. This challenging trigonometry problem requires applying several identities in a not-at-all obvious succession. Most solution attempts fail, because it is hard to choose which identities are actually helpful. Though successful solutions to this problem are rare, the reward model correctly recognizes when a valid chain-of-thought has been found.\n\nSimplify  $\\tan 100^\\circ + 4 \\sin 100^\\circ$ .\n\nI notice that the angle 100 degrees is not a special angle, so I will need to use some trigonometric identities to simplify this expression.\n\nI recall that  $\\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta}$  and  $\\sin 2\\theta = 2 \\sin \\theta \\cos \\theta$ .\n\nI can use these identities to rewrite the expression as  $\\frac{\\sin 100^\\circ}{\\cos 100^\\circ} + 4 \\sin 100^\\circ$ .\n\nI can combine the terms by finding a common denominator of  $\\cos 100^\\circ$ .\n\nI get  $\\frac{\\sin 100^\\circ + 4 \\sin 100^\\circ \\cos 100^\\circ}{\\cos 100^\\circ}$ .\n\nI can simplify the numerator by using the double angle identity again, but in reverse.\n\nI get  $\\frac{\\sin 100^\\circ + 2 \\sin 200^\\circ}{\\cos 100^\\circ}$ .\n\nI notice that 200 degrees is the same as 180 degrees plus 20 degrees, so I can use the sum angle identity for sine.\n\nI get  $\\frac{\\sin 100^\\circ + 2(\\sin 180^\\circ \\cos 20^\\circ + \\cos 180^\\circ \\sin 20^\\circ)}{\\cos 100^\\circ}$ .\n\nI recall that  $\\sin 180^\\circ = 0$  and  $\\cos 180^\\circ = -1$ , so I can simplify further.\n\nI get  $\\frac{\\sin 100^\\circ - 2 \\sin 20^\\circ}{\\cos 100^\\circ}$ .\n\nI notice that 100 degrees is the same as 90 degrees plus 10 degrees, so I can use the sum angle identity for sine and cosine.\n\nI get  $\\frac{(\\sin 90^\\circ \\cos 10^\\circ + \\cos 90^\\circ \\sin 10^\\circ) - 2 \\sin 20^\\circ}{(\\cos 90^\\circ \\cos 10^\\circ - \\sin 90^\\circ \\sin 10^\\circ)}$ .\n\nI recall that  $\\sin 90^\\circ = 1$  and  $\\cos 90^\\circ = 0$ , so I can simplify further.\n\nI get  $\\frac{\\cos 10^\\circ - 2 \\sin 20^\\circ}{-\\sin 10^\\circ}$ .\n\nI can simplify the sign by multiplying the numerator and denominator by -1.\n\nI get  $\\frac{2 \\sin 20^\\circ - \\cos 10^\\circ}{\\sin 10^\\circ}$ .\n\nI notice that 20 degrees is the same as 30 degrees minus 10 degrees, so I can use the difference angle identity for sine.\n\nI get  $\\frac{2(\\sin 30^\\circ \\cos 10^\\circ - \\cos 30^\\circ \\sin 10^\\circ) - \\cos 10^\\circ}{\\sin 10^\\circ}$ .\n\nI recall that  $\\sin 30^\\circ = \\frac{1}{2}$  and  $\\cos 30^\\circ = \\frac{\\sqrt{3}}{2}$ , so I can simplify further.\n\nI get  $\\frac{\\cos 10^\\circ - \\sqrt{3} \\sin 10^\\circ - \\cos 10^\\circ}{\\sin 10^\\circ}$ .\n\nI can cancel out the  $\\cos 10^\\circ$  terms in the numerator.\n\nI get  $\\frac{-\\sqrt{3} \\sin 10^\\circ}{\\sin 10^\\circ}$ .\n\nI can cancel out the  $\\sin 10^\\circ$  terms in the numerator and denominator.\n\nI get  $-\\sqrt{3}$ .\n\nAnswer:  $-\\sqrt{3}$Problem 2. Generator pass-rate: 5.8%. In step 7 and 8, the generator starts performing guess-and-check. This is a common place the model might hallucinate, by claiming a particular guess is successful when it isn't. In this case, the reward model verifies each step and determines that the chain-of-thought is correct.\n\nFind the unique odd integer  $t$  such that  $0 < t < 23$  and  $t + 2$  is the inverse of  $t$  modulo 23.\n\nI need to find an odd integer  $t$  that satisfies the congruence  $t + 2 \\equiv t^{-1} \\pmod{23}$ .\n\nTo do that, I can multiply both sides by  $t$  and get  $t^2 + 2t \\equiv 1 \\pmod{23}$ .\n\nThen I can complete the square by adding and subtracting  $(2/2)^2 = 1$  to the left side and get  $(t + 1)^2 - 1 \\equiv 1 \\pmod{23}$ .\n\nSimplifying, I get  $(t + 1)^2 \\equiv 2 \\pmod{23}$ .\n\nNow I need to find a square root of 2 modulo 23.\n\nI can try some values of  $t + 1$  and see if they work.\n\nFor example, if  $t + 1 = 3$ , then  $(t + 1)^2 = 9 \\not\\equiv 2 \\pmod{23}$ .\n\nIf  $t + 1 = 5$ , then  $(t + 1)^2 = 25 \\equiv 2 \\pmod{23}$ .\n\nSo one possible value of  $t$  is  $t = 5 - 1 = 4$ .\n\nBut this is not odd, so I need to find another one.\n\nI know that if  $t + 1$  is a square root of 2 modulo 23, then so is  $-t - 1$ .\n\nSo I can try  $-t - 1 = 5$  and get  $t = -6$ .\n\nBut this is negative, so I need to add 23 to get a positive value.\n\nSo another possible value of  $t$  is  $t = -6 + 23 = 17$ .\n\nThis is odd and satisfies the original congruence, so this is the unique solution.\n\nAnswer: 17\n\nProblem 3. Generator pass-rate: 1.7%. The generator successfully applies several trigonometric identities to simplify the expression.\n\nFind the degree measure of the least positive angle  $\\theta$  for which\n\n$$\\tan \\theta = \\frac{\\cos 5^\\circ \\cos 20^\\circ + \\cos 35^\\circ \\cos 50^\\circ - \\sin 5^\\circ \\sin 20^\\circ - \\sin 35^\\circ \\sin 50^\\circ}{\\sin 5^\\circ \\cos 20^\\circ - \\sin 35^\\circ \\cos 50^\\circ + \\cos 5^\\circ \\sin 20^\\circ - \\cos 35^\\circ \\sin 50^\\circ}.$$\n\nI notice that the numerator and denominator of the fraction are both sums of products of cosine and sine functions of angles that add up to 25 degrees or 85 degrees.\n\nThis suggests that I might be able to use some trigonometric identities to simplify the expression.\n\nFor example, I recall that  $\\cos(A + B) = \\cos A \\cos B - \\sin A \\sin B$  and  $\\sin(A + B) = \\sin A \\cos B + \\cos A \\sin B$ .\n\nIf I apply these identities to the terms in the numerator, I get  $\\cos 5^\\circ \\cos 20^\\circ + \\cos 35^\\circ \\cos 50^\\circ - \\sin 5^\\circ \\sin 20^\\circ - \\sin 35^\\circ \\sin 50^\\circ = \\cos(5^\\circ + 20^\\circ) + \\cos(35^\\circ + 50^\\circ) = \\cos 25^\\circ + \\cos 85^\\circ$ .\n\nSimilarly, if I apply these identities to the terms in the denominator, I get  $\\sin 5^\\circ \\cos 20^\\circ - \\sin 35^\\circ \\cos 50^\\circ + \\cos 5^\\circ \\sin 20^\\circ - \\cos 35^\\circ \\sin 50^\\circ = \\sin(5^\\circ + 20^\\circ) - \\sin(35^\\circ + 50^\\circ) = \\sin 25^\\circ - \\sin 85^\\circ$ .\n\nNow I have  $\\tan \\theta = \\frac{\\cos 25^\\circ + \\cos 85^\\circ}{\\sin 25^\\circ - \\sin 85^\\circ}$ .\n\nI wonder if I can simplify this fraction further.\n\nI recall another trigonometric identity that says  $\\cos A + \\cos B = 2 \\cos \\frac{A+B}{2} \\cos \\frac{A-B}{2}$ .\n\nIf I apply this identity to the numerator, I get  $\\cos 25^\\circ + \\cos 85^\\circ = 2 \\cos \\frac{25^\\circ + 85^\\circ}{2} \\cos \\frac{25^\\circ - 85^\\circ}{2} = 2 \\cos 55^\\circ \\cos(-30^\\circ)$ .\n\nI also recall that  $\\cos(-\\theta) = \\cos \\theta$ , so I can write  $\\cos(-30^\\circ) = \\cos 30^\\circ$ .\n\nSimilarly, I recall another trigonometric identity that says  $\\sin A - \\sin B = 2 \\cos \\frac{A+B}{2} \\sin \\frac{A-B}{2}$ .\n\nIf I apply this identity to the denominator, I get  $\\sin 25^\\circ - \\sin 85^\\circ = 2 \\cos \\frac{25^\\circ + 85^\\circ}{2} \\sin \\frac{25^\\circ - 85^\\circ}{2} = 2 \\cos 55^\\circ \\sin(-30^\\circ)$ .\n\nI also recall that  $\\sin(-\\theta) = -\\sin \\theta$ , so I can write  $\\sin(-30^\\circ) = -\\sin 30^\\circ$ .\n\nNow I have  $\\tan \\theta = \\frac{2 \\cos 55^\\circ \\cos 30^\\circ}{2 \\cos 55^\\circ (-\\sin 30^\\circ)} = \\frac{-\\cos 30^\\circ}{\\sin 30^\\circ}$ .\n\nI know that  $\\cos 30^\\circ = \\frac{\\sqrt{3}}{2}$  and  $\\sin 30^\\circ = \\frac{1}{2}$ , so I can simplify this to  $\\tan \\theta = -\\frac{\\sqrt{3}}{1} = -\\sqrt{3}$ .\n\nI also know that  $\\tan \\theta$  is negative in the second and fourth quadrants, and that  $\\tan \\theta = -\\sqrt{3}$  when  $\\theta$  is  $120^\\circ$  or  $300^\\circ$ .\n\nTherefore, the least positive angle  $\\theta$  for which  $\\tan \\theta = -\\sqrt{3}$  is  $120^\\circ$ .\n\nAnswer: 120Problem 4. Generator pass-rate: 4.5%. Here, the generator successfully performs a complex series of polynomial factorizations. The use of the Sophie-Germain identity in step 5 is an important step that could be considered insightful.\n\nLet\n\n$$x^8 + 3x^4 - 4 = p_1(x)p_2(x) \\cdots p_k(x),$$\n\nwhere each non-constant polynomial  $p_i(x)$  is monic with integer coefficients, and cannot be factored further over the integers. Compute  $p_1(1) + p_2(1) + \\cdots + p_k(1)$ .\n\nI notice that the given polynomial has even degree and only even powers of  $x$ , so I can try to make a substitution to simplify it:\n\nLet  $y = x^4$ , then the polynomial becomes  $y^2 + 3y - 4$ , which is a quadratic equation.\n\nI can factor this quadratic equation as  $(y + 4)(y - 1)$ , so the original polynomial is  $(x^4 + 4)(x^4 - 1)$ .\n\nNow I need to factor each of these factors further, if possible, over the integers.\n\nFor the first factor,  $x^4 + 4$ , I recall the Sophie Germain identity, which says that  $a^4 + 4b^4 = (a^2 + 2b^2 + 2ab)(a^2 + 2b^2 - 2ab)$ .\n\nApplying this identity with  $a = x$  and  $b = 1$ , I get  $x^4 + 4 = (x^2 + 2x + 2)(x^2 - 2x + 2)$ .\n\nFor the second factor,  $x^4 - 1$ , I can use the difference of squares formula, which says that  $a^2 - b^2 = (a + b)(a - b)$ .\n\nApplying this formula with  $a = x^2$  and  $b = 1$ , I get  $x^4 - 1 = (x^2 + 1)(x^2 - 1)$ .\n\nThen I can apply the difference of squares formula again with  $a = x$  and  $b = 1$ , to get  $x^2 - 1 = (x + 1)(x - 1)$ .\n\nSo the original polynomial is  $(x^4 + 4)(x^4 - 1) = (x^2 + 2x + 2)(x^2 - 2x + 2)(x^2 + 1)(x + 1)(x - 1)$ .\n\nThese are all the irreducible factors over the integers, so  $p_1(x) = x^2 + 2x + 2$ ,  $p_2(x) = x^2 - 2x + 2$ ,  $p_3(x) = x^2 + 1$ ,  $p_4(x) = x + 1$ , and  $p_5(x) = x - 1$ .\n\nTo find the sum of their values at  $x = 1$ , I just need to plug in  $x = 1$  into each factor and add them up.\n\nI get  $p_1(1) = 1^2 + 2 \\cdot 1 + 2 = 5$ ,  $p_2(1) = 1^2 - 2 \\cdot 1 + 2 = 1$ ,  $p_3(1) = 1^2 + 1 = 2$ ,  $p_4(1) = 1 + 1 = 2$ , and  $p_5(1) = 1 - 1 = 0$ .\n\nSo the final answer is  $5 + 1 + 2 + 2 + 0 = 10$ .\n\nAnswer: 10\n\n## I.2 True Negatives\n\nProblem 5. Generator pass-rate: 4.5%. The generator attempts to use the difference of squares formula in step 12 on an expression that isn't in fact a difference of squares. The reward model catches this mistake.\n\nLet\n\n$$x^8 + 3x^4 - 4 = p_1(x)p_2(x) \\cdots p_k(x),$$\n\nwhere each non-constant polynomial  $p_i(x)$  is monic with integer coefficients, and cannot be factored further over the integers. Compute  $p_1(1) + p_2(1) + \\cdots + p_k(1)$ .\n\nThis problem is about factoring a polynomial over the integers, which can be a tricky task.\n\nOne possible strategy is to look for rational roots of the polynomial, using the rational root theorem.\n\nHowever, that would involve checking a lot of possible factors of  $-4$ , and there is no guarantee that the polynomial has any rational roots at all.\n\nAnother possible strategy is to use some algebraic tricks to simplify the polynomial or reduce its degree.\n\nI notice that the polynomial has only even powers of  $x$ , so I can try to substitute  $y = x^4$  and see what happens.\n\nThen the polynomial becomes  $y^2 + 3y - 4$ , which is a quadratic equation in  $y$ .\n\nI can try to factor this quadratic equation by looking for two numbers that multiply to  $-4$  and add to 3.\n\nThose numbers are 4 and  $-1$ , so I can write  $y^2 + 3y - 4 = (y + 4)(y - 1)$ .\n\nNow I can substitute back  $x^4 = y$  and get  $x^8 + 3x^4 - 4 = (x^4 + 4)(x^4 - 1)$ .\n\nThis looks promising, because I have reduced the degree of the factors from 8 to 4.\n\nI can try to factor each of these factors further, using the difference of squares formula.\n\nI get  $x^8 + 3x^4 - 4 = (x^4 + 2)(x^4 - 2)(x^2 + 1)(x^2 - 1)$ .\n\nI can apply the difference of squares formula again to the last factor and get  $x^8 + 3x^4 - 4 = (x^4 + 2)(x^2 - 2)(x^2 + 1)(x + 1)(x - 1)$ .\n\nNow I have factored the polynomial completely into monic linear and quadratic factors with integer coefficients.\n\nThese are the  $p_i(x)$ 's that the problem is asking for.\n\nTo find the sum of their values at  $x = 1$ , I just need to plug in  $x = 1$  into each factor and add them up.\n\nI get  $p_1(1) + p_2(1) + \\cdots + p_k(1) = (1^4 + 2)(1^4 - 2)(1^2 + 1)(1 + 1)(1 - 1)$ .\n\nSimplifying, I get  $p_1(1) + p_2(1) + \\cdots + p_k(1) = (3)(-1)(2)(2)(0)$ .\n\nMultiplying, I get  $p_1(1) + p_2(1) + \\cdots + p_k(1) = 0$ .\n\nAnswer: 0Problem 6. Generator pass-rate: 93.5%. In step 7, the generator makes an incorrect attempt to simplify an expression. The reward model catches this mistake.\n\nA class of 30 students recently took a test. If 20 students scored 80, 8 students scored 90, and 2 students scored 100, then what was the class average (the mean) on this test?\n\nTo find the class average, I need to add up all the scores and divide by the number of students.\n\nI can use a shortcut to add up the scores, since they are grouped by value.\n\nFor example, instead of adding  $80 + 80 + \\dots + 80$  twenty times, I can just multiply 80 by 20 to get the same result.\n\nSimilarly, I can multiply 90 by 8 and 100 by 2 to get the sums of those groups.\n\nSo, the total sum of the scores is  $80 * 20 + 90 * 8 + 100 * 2$ .\n\nI can use the distributive property of multiplication to simplify this expression.\n\nIt is equivalent to  $80 * (20 + 1) + 90 * 8 + 100$ .\n\nThat is,  $80 * 21 + 720 + 100$ .\n\nI can do the arithmetic in my head or use a calculator.\n\n$80 * 21$  is 1680, so the total sum is  $1680 + 720 + 100$ , which is 2500.\n\nNow, to find the average, I need to divide 2500 by 30, the number of students.\n\nI can use long division or a calculator for this step.\n\n2500 divided by 30 is 83.33, repeating.\n\nThis means that the class average is 83.33, or 83 and one-third.\n\nAnswer: 83.33\n\nProblem 7. Generator pass-rate: 48.0%. In step 11, the generator makes a simple calculation error. The reward model catches this mistake.\n\nIf  $A$  is the sum of the positive divisors of 500, what is the sum of the distinct prime divisors of  $A$ ?\n\nI notice that  $500 = 2^2 \\cdot 5^3$ , so its positive divisors are of the form  $2^a \\cdot 5^b$ , where  $a \\in \\{0, 1, 2\\}$  and  $b \\in \\{0, 1, 2, 3\\}$ .\n\nTo find the sum of these divisors, I can use a formula that involves the geometric series: if  $p$  is a prime number and  $n$  is a nonnegative integer, then the sum of the powers of  $p$  from 0 to  $n$  is  $\\frac{p^{n+1}-1}{p-1}$ .\n\nSo, the sum of the powers of 2 from 0 to 2 is  $\\frac{2^3-1}{2-1} = 7$ , and the sum of the powers of 5 from 0 to 3 is  $\\frac{5^4-1}{5-1} = 156$ .\n\nBy the distributive property, the sum of the divisors of 500 is the product of these two sums:  $A = 7 \\cdot 156 = 1092$ .\n\nNow, I need to find the sum of the distinct prime divisors of  $A$ .\n\nI can try to factor  $A$  into primes by trial division.\n\nI notice that  $A$  is divisible by 2, so I divide by 2 and get 546.\n\nI repeat this process and divide by 2 again, getting 273.\n\nNow, 273 is not divisible by 2, so I try the next prime, 3.\n\nI see that 273 is divisible by 3, so I divide by 3 and get 91.\n\nI divide by 3 again, getting 31.\n\nNow, 31 is a prime number, so I have found all the prime factors of  $A$ :  $A = 2^2 \\cdot 3^2 \\cdot 31$ .\n\nThe sum of the distinct prime divisors of  $A$  is  $2 + 3 + 31 = 36$ .\n\nAnswer: 36Problem 8. Generator pass-rate: 5.8%. The justification in step 8 is strange, but the reward model lets it slide. In step 9, though, the model incorrectly factors the expression. The reward model catches this mistake.\n\nFind the unique odd integer  $t$  such that  $0 < t < 23$  and  $t + 2$  is the inverse of  $t$  modulo 23.\n\nI need to find an odd integer  $t$  between 0 and 23 such that  $t + 2$  is the inverse of  $t$  modulo 23.\n\nThat means that  $t$  and  $t + 2$  multiply to give 1 modulo 23.\n\nI can write this as  $t(t + 2) \\equiv 1 \\pmod{23}$ .\n\nI can try to guess and check values of  $t$  until I find one that works, but that might take a long time.\n\nI can also try to use some properties of modular arithmetic to simplify the equation.\n\nFor example, I can subtract 23 from  $t + 2$  and still get the same remainder modulo 23.\n\nSo I can write  $t(t + 2) \\equiv t(t - 21) \\pmod{23}$ .\n\nThis looks simpler, because now I have a difference of two multiples of  $t$ .\n\nI can factor out  $t$  and get  $t(t - 21) \\equiv t(1 - 21) \\pmod{23}$ .\n\nNow I can divide both sides by  $t$ , as long as  $t$  is not a multiple of 23.\n\nThis gives me  $t - 21 \\equiv 1 - 21 \\pmod{23}$ .\n\nI can simplify this further by adding 21 to both sides.\n\nThis gives me  $t \\equiv 1 \\pmod{23}$ .\n\nThis means that  $t$  has the same remainder as 1 when divided by 23.\n\nThe smallest positive value of  $t$  that satisfies this is  $t = 1$ .\n\nThis is also an odd integer, so it meets the criteria of the problem.\n\nI can check that  $t = 1$  works by plugging it into the original equation.\n\nI get  $1(1 + 2) \\equiv 1 \\pmod{23}$ , which is true.\n\nTherefore, the unique odd integer  $t$  that satisfies the given conditions is  $t = 1$ .\n\nAnswer: 1\n\n### I.3 False Positives\n\nProblem 9. Generator pass-rate: 18.5%. The generator makes a subtle counting error in step 9. On the surface, it appears reasonable to claim that there are 5 ways to exchange the same colored ball since there are 5 colors. However, this undercounts by a factor of 2, since Bob has 2 choices for which ball to return to Alice. The reward model is fooled by this mistake.\n\nBob and Alice each have a bag that contains one ball of each of the colors, blue, green, orange, red, and violet. Alice randomly selects one ball from her bag and puts it into Bob's bag. Bob then randomly selects one ball from his bag and puts it into Alice's bag. What is the probability that after this process the contents of the two bags are the same?\n\nTo find the probability of an event, I need to divide the number of favorable outcomes by the number of possible outcomes.\n\nIn this case, the event is that the contents of the two bags are the same after the process.\n\nSo I need to count how many ways this can happen, and how many ways the process can happen in total.\n\nI will start with the total number of ways the process can happen.\n\nAlice can choose any of the five balls in her bag, and Bob can choose any of the six balls in his bag.\n\nSo the total number of ways the process can happen is 5 times 6, which is 30.\n\nNow I will count how many ways the contents of the two bags can be the same after the process.\n\nThis means that Alice and Bob must have exchanged the same color of ball.\n\nThere are five colors, so there are five ways they can exchange the same color of ball. ERROR\n\nTherefore, the number of favorable outcomes is 5.\n\nSo the probability of the event is 5 divided by 30, which simplifies to 1/6.\n\nAnswer: 1/6Problem 10. Generator pass-rate: 17.6%. In step 13, the generator attempts to simplify the equation by combining like terms. It correctly moves and combines the linear terms to the left-hand side, but then mistakenly leaves the right-hand side untouched. The reward model is fooled by this mistake.\n\nDenali and Nate work for a dog walking business and are paid for each dog they walk. Denali is responsible for 16 dogs and Nate is responsible for 12 dogs. Under the company's new policy, they will be assigned or unassigned new dogs in groups of  $x$  dogs. The ratio of Denali's pay to Nate's pay would be the same if Denali started walking  $4x$  more dogs and Nate stayed at 12 dogs or if  $x$  of Nate's dogs were reassigned to Denali. Find  $x$  if  $x \\neq 0$ .\n\nI need to find a value of  $x$  that makes the ratio of Denali's pay to Nate's pay the same in two different scenarios.  \n I can assume that the pay per dog is constant, so the ratio of their pay is the same as the ratio of the number of dogs they walk.  \n Let me write an equation for the first scenario, where Denali walks  $4x$  more dogs and Nate stays at 12 dogs.  \n The ratio of Denali's dogs to Nate's dogs is  $\\frac{16+4x}{12}$ .  \n Now let me write an equation for the second scenario, where  $x$  of Nate's dogs are reassigned to Denali.  \n The ratio of Denali's dogs to Nate's dogs is  $\\frac{16+x}{12-x}$ .  \n I want these two ratios to be equal, so I can set them equal to each other and solve for  $x$ .  \n I get  $\\frac{16+4x}{12} = \\frac{16+x}{12-x}$ .  \n I can cross-multiply and simplify this equation.  \n I get  $(16+4x)(12-x) = (16+x)(12)$ .  \n Expanding the brackets, I get  $192 - 16x + 48x - 4x^2 = 192 + 12x$ .  \n Subtracting 192 from both sides, I get  $-16x + 48x - 4x^2 = 12x$ .  \n Rearranging the terms, I get  $-4x^2 + 20x = 12x$ . ERROR  \n Subtracting  $12x$  from both sides, I get  $-4x^2 + 8x = 0$ .  \n I can factor out  $-4x$  from both terms, and get  $-4x(x-2) = 0$ .  \n This means that either  $-4x = 0$  or  $x-2 = 0$ .  \n Solving for  $x$ , I get  $x = 0$  or  $x = 2$ .  \n However, the problem says that  $x \\neq 0$ , so I can ignore that solution.  \n Therefore, the only valid solution is  $x = 2$ .  \n Answer: 2\n\nProblem 11. Generator pass-rate: 13.4%. The generator attempts to perform long division, but in step 16, it forgets to include the leading zeros in the repeating part of the decimal. The reward model is fooled by this mistake.\n\nWhen converting  $\\frac{31}{1111}$  to a decimal, the decimal turns out to be a repeating decimal. How many digits repeat in this repeating decimal? For example, if you get the repeating decimal  $0.\\overline{123}$ , then your answer should be 3, and if you get 0.4367, your answer should be 1.\n\nTo convert a fraction to a decimal, I can divide the numerator by the denominator using long division.  \n I'll start by writing 31 over 11111 and bring down a zero.  \n Then I'll ask, how many times does 11111 go into 310?  \n Well, it doesn't go in evenly, so I'll write a zero above the decimal point and bring down another zero.  \n Now I have 3100.  \n How many times does 11111 go into 3100?  \n Still zero, so I'll write another zero above the decimal point and bring down another zero.  \n Now I have 31000.  \n How many times does 11111 go into 31000?  \n Ah, now I can see that it goes in twice, so I'll write a 2 above the decimal point and subtract 22222 from 31000 to get 8778.  \n I'll bring down another zero and ask, how many times does 11111 go into 87780?  \n It goes in seven times, so I'll write a 7 above the decimal point and subtract 77777 from 87780 to get 10003.  \n I'll bring down another zero and ask, how many times does 11111 go into 100030?  \n It goes in nine times, so I'll write a 9 above the decimal point and subtract 99999 from 100030 to get 31.  \n Wait a minute, I'm back to where I started! That means the decimal will repeat from here on.  \n So I'll put a bar over the 279 to indicate that it repeats indefinitely. ERROR  \n The decimal is  $0.00279$  with a bar over 279.  \n The question asks how many digits repeat in this repeating decimal.  \n I can see that there are three digits that repeat: 2, 7, and 9.  \n So the answer is 3.  \n Answer: 3Problem 12. Generator pass-rate: 9.1%. In step 4, the generator falsely claims that the sequence repeats itself every 12 terms, when it's in fact every 10 terms. This sort of counting mistake occasionally fools the reward model.\n\nGiven that\n\n$$\\begin{aligned}x_1 &= 211, \\\\x_2 &= 375, \\\\x_3 &= 420, \\\\x_4 &= 523, \\text{ and} \\\\x_n &= x_{n-1} - x_{n-2} + x_{n-3} - x_{n-4} \\text{ when } n \\geq 5,\\end{aligned}$$\n\nfind the value of  $x_{531} + x_{753} + x_{975}$ .\n\nThis is a problem involving a recursive sequence, where each term depends on the previous four terms.\n\nOne way to approach this problem is to look for a pattern or a formula that can help us find any term of the sequence without having to compute all the previous terms.\n\nTo do that, let's write down the first few terms of the sequence and see if we notice anything:\n\n$$\\begin{aligned}x_1 &= 211, \\\\x_2 &= 375, \\\\x_3 &= 420, \\\\x_4 &= 523, \\\\x_5 &= x_4 - x_3 + x_2 - x_1 = 523 - 420 + 375 - 211 = 267, \\\\x_6 &= x_5 - x_4 + x_3 - x_2 = 267 - 523 + 420 - 375 = -211, \\\\x_7 &= x_6 - x_5 + x_4 - x_3 = -211 - 267 + 523 - 420 = -375, \\\\x_8 &= x_7 - x_6 + x_5 - x_4 = -375 - (-211) + 267 - 523 = -420, \\\\x_9 &= x_8 - x_7 + x_6 - x_5 = -420 - (-375) + (-211) - 267 = -523, \\\\x_{10} &= x_9 - x_8 + x_7 - x_6 = -523 - (-420) + (-375) - (-211) = -267, \\\\x_{11} &= x_{10} - x_9 + x_8 - x_7 = -267 - (-523) + (-420) - (-375) = 211, \\\\x_{12} &= x_{11} - x_{10} + x_9 - x_8 = 211 - (-267) + (-523) - (-420) = 375, \\\\x_{13} &= x_{12} - x_{11} + x_{10} - x_9 = 375 - 211 + (-267) - (-523) = 420, \\\\x_{14} &= x_{13} - x_{12} + x_{11} - x_{10} = 420 - 375 + 211 - (-267) = 523.\\end{aligned}$$\n\nWe can see that the sequence repeats itself every 12 terms, starting from  $x_{14}$  ERROR\n\nThis means that we can find any term of the sequence by finding its remainder when divided by 12, and then looking up the corresponding term in the first cycle.\n\nFor example, to find  $x_{531}$ , we can divide 531 by 12 and get a quotient of 44 and a remainder of 3.\n\nThis means that  $x_{531}$  is the same as  $x_3$ , which is 420.\n\nSimilarly, we can find  $x_{753}$  and  $x_{975}$  by dividing them by 12 and looking up their remainders.\n\nWe get that  $x_{753}$  has a remainder of 9, so it is the same as  $x_9$ , which is -523.\n\nAnd  $x_{975}$  has a remainder of 3, so it is the same as  $x_3$ , which is 420.\n\nTherefore, the value of  $x_{531} + x_{753} + x_{975}$  is  $420 + (-523) + 420 = 317$ .\n\nAnswer: 317\n",
      "numLines": 866,
      "startLine": 1,
      "totalLines": 866
    }
  },
  "sourceToolAssistantUUID": "50a4ea63-f2ea-4bbf-88d4-1664a72d1614",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
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
  "leafUuid": "ebad8f4e-52f8-4fdd-8de9-02801e586928",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze OpenAI's process reward models paper",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd"
}
```

---

### Assistant

_source line 43 · 2026-05-27T15:23:11.937Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent! I now have the full paper content. Let me also try to get the OpenReview reviews one more time with a different approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebad8f4e-52f8-4fdd-8de9-02801e586928",
  "isSidechain": false,
  "requestId": "req_011CbTJYmGxhx77Y1AA53c1F",
  "type": "assistant",
  "uuid": "710d871d-7421-4bd0-8af9-af8c363e967f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PAYSKAaVL42i6HngB2WMc7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26866,
      "cache_read_input_tokens": 17277,
      "output_tokens": 377,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26866,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 377,
          "cache_read_input_tokens": 17277,
          "cache_creation_input_tokens": 26866,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26866
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

_source line 44 · 2026-05-27T15:23:12.427Z_

Now let me try to get the OpenReview reviews via the API:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "710d871d-7421-4bd0-8af9-af8c363e967f",
  "isSidechain": false,
  "requestId": "req_011CbTJYmGxhx77Y1AA53c1F",
  "type": "assistant",
  "uuid": "f48abd15-8613-47ec-a114-03603447b06a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PAYSKAaVL42i6HngB2WMc7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26866,
      "cache_read_input_tokens": 17277,
      "output_tokens": 377,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26866,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 377,
          "cache_read_input_tokens": 17277,
          "cache_creation_input_tokens": 26866,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26866
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

_source line 45 · 2026-05-27T15:23:14.780Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Y7XiBqkGwxhNByjUwKXMga`</summary>

```json
{
  "url": "https://api.openreview.net/notes?invitation=ICLR.cc/2024/Conference/Submission*/Official_Review&content.title=Let%27s+Verify+Step+by+Step&limit=10",
  "prompt": "Extract all review data including reviewer comments, scores, strengths, weaknesses, and questions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f48abd15-8613-47ec-a114-03603447b06a",
  "isSidechain": false,
  "requestId": "req_011CbTJYmGxhx77Y1AA53c1F",
  "type": "assistant",
  "uuid": "69b8b857-8a81-44ab-9a3a-1204fbd77b3f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PAYSKAaVL42i6HngB2WMc7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26866,
      "cache_read_input_tokens": 17277,
      "output_tokens": 377,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26866,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 377,
          "cache_read_input_tokens": 17277,
          "cache_creation_input_tokens": 26866,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26866
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

_source line 46 · 2026-05-27T15:23:17.460Z_

<details><summary>↩ Tool result · reported error · `toolu_01HWSLvY2oJVvzQG8MpkMWsY`</summary>

```text
This Bash command contains multiple operations. The following parts require approval: curl -s "https://api.openreview.net/notes?forum=v8L0pN6EOi&trash=true&details=replyCount,writable,revisions,original,overwriting,invitation,tags,directReplies", python3 -c "import sys,json; d=json.load(sys.stdin); print(json.dumps(d, indent=2)[:5000])" || echo "Failed to parse"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32b86e2e-d655-439e-850d-b69fb671e04d",
  "isSidechain": false,
  "promptId": "847a487e-d454-4fe9-b1b6-24705f0c37b0",
  "type": "user",
  "uuid": "b0c364c2-2fff-48cc-8089-d25735f2edfe",
  "toolUseResult": "Error: This Bash command contains multiple operations. The following parts require approval: curl -s \"https://api.openreview.net/notes?forum=v8L0pN6EOi&trash=true&details=replyCount,writable,revisions,original,overwriting,invitation,tags,directReplies\", python3 -c \"import sys,json; d=json.load(sys.stdin); print(json.dumps(d, indent=2)[:5000])\" || echo \"Failed to parse\"",
  "sourceToolAssistantUUID": "32b86e2e-d655-439e-850d-b69fb671e04d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-27T15:23:14.944Z_

<details><summary>↩ Tool result · `toolu_01Y7XiBqkGwxhNByjUwKXMga`</summary>

```text
The server returned HTTP 400 Bad Request.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69b8b857-8a81-44ab-9a3a-1204fbd77b3f",
  "isSidechain": false,
  "promptId": "847a487e-d454-4fe9-b1b6-24705f0c37b0",
  "type": "user",
  "uuid": "a3232b59-20be-4391-8e33-96b1c7f16b59",
  "toolUseResult": {
    "bytes": 0,
    "code": 400,
    "codeText": "Bad Request",
    "result": "The server returned HTTP 400 Bad Request.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.",
    "durationMs": 162,
    "url": "https://api.openreview.net/notes?invitation=ICLR.cc/2024/Conference/Submission*/Official_Review&content.title=Let%27s+Verify+Step+by+Step&limit=10"
  },
  "sourceToolAssistantUUID": "69b8b857-8a81-44ab-9a3a-1204fbd77b3f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-27T15:23:17.420Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01HWSLvY2oJVvzQG8MpkMWsY`</summary>

```json
{
  "command": "curl -s \"https://api.openreview.net/notes?forum=v8L0pN6EOi&trash=true&details=replyCount,writable,revisions,original,overwriting,invitation,tags,directReplies\" 2>/dev/null | python3 -c \"import sys,json; d=json.load(sys.stdin); print(json.dumps(d, indent=2)[:5000])\" 2>/dev/null || echo \"Failed to parse\"",
  "description": "Fetch OpenReview API data for the paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3232b59-20be-4391-8e33-96b1c7f16b59",
  "isSidechain": false,
  "requestId": "req_011CbTJYmGxhx77Y1AA53c1F",
  "type": "assistant",
  "uuid": "32b86e2e-d655-439e-850d-b69fb671e04d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PAYSKAaVL42i6HngB2WMc7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26866,
      "cache_read_input_tokens": 17277,
      "output_tokens": 377,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26866,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 377,
          "cache_read_input_tokens": 17277,
          "cache_creation_input_tokens": 26866,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26866
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

_source line 49 · 2026-05-27T15:23:22.618Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01VrdbzU4H8CVij3YrvtgpeK`</summary>

```json
{
  "command": "curl -s \"https://api.openreview.net/notes?forum=v8L0pN6EOi\" | python3 -c \"import sys,json; d=json.load(sys.stdin); print(json.dumps(d, indent=2)[:8000])\"",
  "description": "Fetch OpenReview forum data via API"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0c364c2-2fff-48cc-8089-d25735f2edfe",
  "isSidechain": false,
  "requestId": "req_011CbTJZS4LiYjDRC9cAH1zC",
  "type": "assistant",
  "uuid": "773103e1-0195-4356-b56e-3486db085be4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YXSgTPEZzVc5g5Um73iCXE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 609,
      "cache_read_input_tokens": 44143,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 609,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 143,
          "cache_read_input_tokens": 44143,
          "cache_creation_input_tokens": 609,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 609
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

_source line 50 · 2026-05-27T15:23:22.633Z_

<details><summary>↩ Tool result · reported error · `toolu_01VrdbzU4H8CVij3YrvtgpeK`</summary>

```text
This Bash command contains multiple operations. The following parts require approval: curl -s "https://api.openreview.net/notes?forum=v8L0pN6EOi", python3 -c "import sys,json; d=json.load(sys.stdin); print(json.dumps(d, indent=2)[:8000])"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "773103e1-0195-4356-b56e-3486db085be4",
  "isSidechain": false,
  "promptId": "847a487e-d454-4fe9-b1b6-24705f0c37b0",
  "type": "user",
  "uuid": "a91e89bc-455f-4df9-bffc-005dd49c43a6",
  "toolUseResult": "Error: This Bash command contains multiple operations. The following parts require approval: curl -s \"https://api.openreview.net/notes?forum=v8L0pN6EOi\", python3 -c \"import sys,json; d=json.load(sys.stdin); print(json.dumps(d, indent=2)[:8000])\"",
  "sourceToolAssistantUUID": "773103e1-0195-4356-b56e-3486db085be4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-27T15:23:25.731Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01V3MrvFRizvDB2CoRgiSFbg`</summary>

```json
{
  "command": "curl -s \"https://api.openreview.net/notes?forum=v8L0pN6EOi\"",
  "description": "Fetch OpenReview forum data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a91e89bc-455f-4df9-bffc-005dd49c43a6",
  "isSidechain": false,
  "requestId": "req_011CbTJZq3x8DFh6vxLS5qb8",
  "type": "assistant",
  "uuid": "e28e1c6f-4b92-4020-9801-bb226549b5a6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dt1ofRUUvrEhyG8Tcc4afL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 243,
      "cache_read_input_tokens": 44752,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 243,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 102,
          "cache_read_input_tokens": 44752,
          "cache_creation_input_tokens": 243,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 243
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

_source line 52 · 2026-05-27T15:23:25.739Z_

<details><summary>↩ Tool result · reported error · `toolu_01V3MrvFRizvDB2CoRgiSFbg`</summary>

```text
This command requires approval
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e28e1c6f-4b92-4020-9801-bb226549b5a6",
  "isSidechain": false,
  "promptId": "847a487e-d454-4fe9-b1b6-24705f0c37b0",
  "type": "user",
  "uuid": "8d0b0e6d-0342-439c-981c-16e4cb26b065",
  "toolUseResult": "Error: This command requires approval",
  "sourceToolAssistantUUID": "e28e1c6f-4b92-4020-9801-bb226549b5a6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-27T15:23:29.532Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011V2L515z7vEv63mH43FmUY`</summary>

```json
{
  "url": "https://api.openreview.net/notes?content.venue=ICLR+2024+poster&content.title=Let%27s+Verify+Step+by+Step",
  "prompt": "Find the paper ID and any review notes associated with \"Let's Verify Step by Step\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d0b0e6d-0342-439c-981c-16e4cb26b065",
  "isSidechain": false,
  "requestId": "req_011CbTJa3gibzmHiscSUpEXy",
  "type": "assistant",
  "uuid": "aa3029e8-c9da-44a0-8506-ce15e742195d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CEbC6Ghc4g96up5psa86rQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 126,
      "cache_read_input_tokens": 44995,
      "output_tokens": 130,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 126,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 130,
          "cache_read_input_tokens": 44995,
          "cache_creation_input_tokens": 126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 126
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

_source line 54 · 2026-05-27T15:23:31.191Z_

<details><summary>↩ Tool result · `toolu_011V2L515z7vEv63mH43FmUY`</summary>

```text
Based on the provided web page content, there is **no information available** about a paper titled "Let's Verify Step by Step."

The page shows an empty data structure with no notes recorded and a count of zero entries, indicating that this particular paper is not currently in the system or database being queried.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa3029e8-c9da-44a0-8506-ce15e742195d",
  "isSidechain": false,
  "promptId": "847a487e-d454-4fe9-b1b6-24705f0c37b0",
  "type": "user",
  "uuid": "79ca1ea5-3d5c-4b6a-9b97-baab1bc4dee0",
  "toolUseResult": {
    "bytes": 22,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the provided web page content, there is **no information available** about a paper titled \"Let's Verify Step by Step.\"\n\nThe page shows an empty data structure with no notes recorded and a count of zero entries, indicating that this particular paper is not currently in the system or database being queried.",
    "durationMs": 1656,
    "url": "https://api.openreview.net/notes?content.venue=ICLR+2024+poster&content.title=Let%27s+Verify+Step+by+Step"
  },
  "sourceToolAssistantUUID": "aa3029e8-c9da-44a0-8506-ce15e742195d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-27T15:23:34.504Z_

<details><summary>Logged reasoning block</summary>

```text
Let me try looking for the ICLR 2024 reviews via the v2 API since OpenReview migrated to a newer API.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79ca1ea5-3d5c-4b6a-9b97-baab1bc4dee0",
  "isSidechain": false,
  "requestId": "req_011CbTJaSdboDW4XNxquKd4G",
  "type": "assistant",
  "uuid": "ded9bdd0-b545-4f91-bf35-3da70b5178c8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WeMhEAQWiWAaShjQqXxBKi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 205,
      "cache_read_input_tokens": 45121,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 205,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 45121,
          "cache_creation_input_tokens": 205,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 205
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

_source line 56 · 2026-05-27T15:23:36.359Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Lqcp99qgSoqb6racWtwbuu`</summary>

```json
{
  "url": "https://api2.openreview.net/notes?forum=v8L0pN6EOi",
  "prompt": "Extract ALL data from this API response. I need every review, comment, score, and author response for the paper \"Let's Verify Step by Step\". Return the full JSON content with all review details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ded9bdd0-b545-4f91-bf35-3da70b5178c8",
  "isSidechain": false,
  "requestId": "req_011CbTJaSdboDW4XNxquKd4G",
  "type": "assistant",
  "uuid": "7e76fa24-88a7-4738-b851-8d6f9ceeb5f9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WeMhEAQWiWAaShjQqXxBKi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 205,
      "cache_read_input_tokens": 45121,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 205,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 45121,
          "cache_creation_input_tokens": 205,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 205
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

_source line 57 · 2026-05-27T15:23:43.493Z_

<details><summary>↩ Tool result · `toolu_01Lqcp99qgSoqb6racWtwbuu`</summary>

```text
# Paper Review Data: "Let's Verify Step by Step"

## Decision
**Status:** Accept (poster)
**Decision Date:** January 10, 2025

## Meta-Review Summary
The area chair recommended acceptance despite reproducibility concerns, citing the paper's "novel approach to training, strong empirical results, and dataset contribution."

## Individual Reviews

### Reviewer 5YZq (Rating: 8/10 - Accept)
- **Strengths:** Thorough investigation comparing supervision methods; active learning enhancement; dataset release
- **Weakness:** Experiments limited to exam datasets
- **Key Quote:** "This work offers an independent and thorough investigation into the superiority of outcome supervision versus process supervision methods"

### Reviewer 4gd2 (Rating: 3/10 - Reject)
- **Concerns:** Limited novelty (dense rewards well-studied in RL); narrow scope (math only); lack of RLHF application
- **Key Insight:** Questioned whether step-level rewards on small sets outperform outcome-level rewards on large sets under equal budgets

### Reviewer HKpB (Rating: 5/10 - Marginally Below Threshold)
- **Issues:** Limited domain exploration; RLHF not applied; unclear generalization
- **Key Quote:** "It would be better to explore different tasks"

### Reviewer DxcT (Rating: 6/10 - Marginally Above Threshold)
- **Main Concerns:** Reproducibility issues (model sizes undisclosed); limited domain scope
- **Positive Note:** Strong empirical results on MATH dataset (78.2% accuracy)

## Author Responses

Authors addressed reproducibility by noting small-scale results should be reproducible on open models, while large-scale results represent frontier research. They provided evidence of generalization to chemistry and physics in Table 1 and reframed process supervision as cost-efficient reward training.

## Dataset Contribution
**PRM800K:** 800,000 step-level human feedback labels for process supervision research
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e76fa24-88a7-4738-b851-8d6f9ceeb5f9",
  "isSidechain": false,
  "promptId": "847a487e-d454-4fe9-b1b6-24705f0c37b0",
  "type": "user",
  "uuid": "ded55823-569e-4504-84f7-75474195b3b8",
  "toolUseResult": {
    "bytes": 23986,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Review Data: \"Let's Verify Step by Step\"\n\n## Decision\n**Status:** Accept (poster)\n**Decision Date:** January 10, 2025\n\n## Meta-Review Summary\nThe area chair recommended acceptance despite reproducibility concerns, citing the paper's \"novel approach to training, strong empirical results, and dataset contribution.\"\n\n## Individual Reviews\n\n### Reviewer 5YZq (Rating: 8/10 - Accept)\n- **Strengths:** Thorough investigation comparing supervision methods; active learning enhancement; dataset release\n- **Weakness:** Experiments limited to exam datasets\n- **Key Quote:** \"This work offers an independent and thorough investigation into the superiority of outcome supervision versus process supervision methods\"\n\n### Reviewer 4gd2 (Rating: 3/10 - Reject)\n- **Concerns:** Limited novelty (dense rewards well-studied in RL); narrow scope (math only); lack of RLHF application\n- **Key Insight:** Questioned whether step-level rewards on small sets outperform outcome-level rewards on large sets under equal budgets\n\n### Reviewer HKpB (Rating: 5/10 - Marginally Below Threshold)\n- **Issues:** Limited domain exploration; RLHF not applied; unclear generalization\n- **Key Quote:** \"It would be better to explore different tasks\"\n\n### Reviewer DxcT (Rating: 6/10 - Marginally Above Threshold)\n- **Main Concerns:** Reproducibility issues (model sizes undisclosed); limited domain scope\n- **Positive Note:** Strong empirical results on MATH dataset (78.2% accuracy)\n\n## Author Responses\n\nAuthors addressed reproducibility by noting small-scale results should be reproducible on open models, while large-scale results represent frontier research. They provided evidence of generalization to chemistry and physics in Table 1 and reframed process supervision as cost-efficient reward training.\n\n## Dataset Contribution\n**PRM800K:** 800,000 step-level human feedback labels for process supervision research",
    "durationMs": 7129,
    "url": "https://api2.openreview.net/notes?forum=v8L0pN6EOi"
  },
  "sourceToolAssistantUUID": "7e76fa24-88a7-4738-b851-8d6f9ceeb5f9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 58 · 2026-05-27T15:24:06.748Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need to produce a thorough analysis. Let me compile this into the requested JSON format.

Key findings from my reading:

1. **Problem identification**: The paper identified that prior work (Uesato et al., 2022) had found process and outcome supervision to be roughly equivalent, but this was tested at small scale on easy problems (GSM8K). The authors hypothesized that scaling up process supervision on harder problems would reveal its advantages.

2. **Key insight**: Process supervision provides more precise credit assignment — it tells the model exactly WHERE reasoning went wrong, not just that the final answer was wrong. This is especially important for hard problems where most solutions contain errors somewhere.


3. **Innovation type**: The core contribution combines a new large-scale benchmark (PRM800K) with systematic scaling and analysis. While process supervision itself wasn't novel, the scale of labeling (800K examples with GPT-4), the dataset release, and the comprehensive comparison against outcome supervision were new.

4. **Method summary**: The approach involved training solution generators on the MATH dataset, then collecting fine-grained human labels at the step level to identify which reasoning steps were correct or incorrect. They used active learning to focus labeling efforts on the trickiest cases—solutions that reached wrong answers but seemed plausible—and trained process reward models to predict correctness at each step.

5. **What makes it good**: The empirical gains are substantial (78.2% for PRMs versus 72.4% for outcome-only models on best-of-1860 selection), and releasing the PRM800K dataset removed a major barrier for future work. The experimental design carefully separates concerns by running large-scale comparisons for state-of-the-art results alongside smaller controlled ablations, and the framing around alignment and the "negative alignment tax" adds conceptual depth.

6. **Limitations**: The evaluation is restricted to mathematics, the large-scale results depend on GPT-4 and aren't reproducible, they didn't investigate using the PRM to guide reinforcement learning, and the approach requires expensive human labeling at scale.

7. **Open questions**: Whether this generalizes to other domains, whether process supervision can be automated, and what happens when you incorporate the PRM into RL training.

8. **Reviewer feedback**: One reviewer gave it 8/10 and highlighted the thoroughness of the work.

The other reviewers had mixed reactions—one criticized the limited novelty given prior work on dense rewards in RL and the narrow scope, another wanted to see results across different tasks, and a third raised reproducibility concerns despite acknowledging the strong empirical results. The area chair ultimately accepted it, emphasizing the novel approach, strong results, and dataset contribution as decisive factors.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ded55823-569e-4504-84f7-75474195b3b8",
  "isSidechain": false,
  "requestId": "req_011CbTJbMK9TRYxyy5RNxt1t",
  "type": "assistant",
  "uuid": "09ae4b90-e24a-4b66-8cc5-05d1877b85cd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S4Zjd1rCCXqD6iC7zeeUEy",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 650,
      "cache_read_input_tokens": 45326,
      "output_tokens": 2558,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 650,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2558,
          "cache_read_input_tokens": 45326,
          "cache_creation_input_tokens": 650,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 650
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

_source line 59 · 2026-05-27T15:24:49.774Z_

I now have the full paper content and all four reviewer assessments. Let me compose the analysis:

```json
{
  "title": "Let's Verify Step by Step",
  "venue": "ICLR 2024 (Poster)",

  "problem_identification": "Uesato et al. (2022) had compared process vs. outcome supervision on GSM8K and found them roughly equivalent — but that comparison used a weaker model, less data, and an easier benchmark. The authors recognized this left a critical question unresolved: does process supervision's theoretical advantage in credit assignment actually manifest when you scale up the supervision, use a more capable base model, and test on genuinely hard problems (MATH)? They found the gap by identifying that the prior null result was an artifact of under-scaling, not a fundamental limitation.",

  "key_insight": "Process supervision makes the credit-assignment problem dramatically easier for the reward model: instead of forcing it to figure out WHERE in a long chain-of-thought an error occurred (outcome supervision), you directly tell it the location of the first mistake, which provides a strictly richer training signal. This advantage compounds on harder problems where most solutions contain errors, making negative outcome labels nearly uninformative while process labels remain precise.",

  "innovation_type": "combination",

  "method_summary": "The authors fine-tune GPT-4 as a generator to produce step-by-step MATH solutions, then train two types of reward models on those solutions: an ORM trained on binary correct/incorrect final-answer labels, and a PRM trained on human-provided step-level correctness labels (positive/negative/neutral for each reasoning step). The PRM scores a full solution as the product of per-step correctness probabilities and is evaluated via best-of-N rejection sampling. A key methodological contribution is their active learning pipeline: they iteratively retrain the PRM and preferentially surface 'convincing wrong-answer' solutions (highly-rated by the current PRM but reaching incorrect final answers) to human labelers, achieving a 2.6× data efficiency gain. To isolate confounding factors (dataset composition, false positive contamination), they also conduct small-scale controlled ablations using the large PRM as a synthetic oracle for training smaller PRMs, enabling apples-to-apples comparison on identical data.",

  "what_makes_it_good": "The paper succeeds because it makes a clean, decision-relevant empirical claim (process > outcome, 78.2% vs 72.4% on MATH) backed by careful experimental design that separates frontier results (large-scale) from controlled science (small-scale ablations with synthetic supervision). The release of PRM800K — 800K human step-level labels — was a massive community contribution that removed a significant barrier to entry for an entire subfield; this dataset became the standard benchmark for subsequent PRM research. The alignment framing ('negative alignment tax' — the safer method is also the better-performing one) gave the paper impact beyond the ML methods community.",

  "limitations_acknowledged": "The authors explicitly note that all results are in the math domain and it is unknown whether they generalize; that large-scale experiments are not reproducible due to the GPT-4 base model; that they intentionally did not explore using the PRM for RL-based generator finetuning (only best-of-N search); and that iterative active learning showed unexplained instability they could not diagnose.",

  "open_questions": [
    "Can process supervision be effectively automated (removing the human labeling bottleneck) — e.g., via Monte Carlo rollout estimation, model self-verification, or synthetic step-level labels from stronger models — without losing the quality advantage over outcome supervision?",
    "Does the process > outcome advantage hold when the reward model is used for RL-based policy optimization (not just best-of-N reranking), and does it change the scaling dynamics or reward hacking behavior?",
    "How does the advantage of process supervision generalize to domains where step correctness is ambiguous or not easily decomposable (e.g., creative writing, open-ended reasoning, code generation with complex dependencies), and what is the right granularity of 'steps' in such domains?"
  ],

  "building_blocks": [
    "PRM800K dataset (800K human step-level labels on 75K solutions to 12K MATH problems)",
    "Best-of-N rejection sampling as a reward model evaluation protocol",
    "Active learning via 'convincing wrong-answer' solution selection for data-efficient human labeling",
    "Product-of-step-probabilities as solution-level PRM scoring function",
    "Large-model-as-oracle for controlled small-scale ablations (synthetic supervision)",
    "MathMix pretraining corpus (1.5B math-relevant tokens)",
    "MATH dataset (Hendrycks et al., 2021) as a challenging reasoning benchmark",
    "Step-level label taxonomy: positive / negative / neutral with labeling only up to first error"
  ],

  "reviewer_feedback_summary": "Reviewer 5YZq (8, Accept) praised the thoroughness of the investigation, active learning contribution, and dataset release. Reviewer 4gd2 (3, Reject) argued limited novelty since dense rewards are well-studied in RL, questioned whether equal-budget comparisons truly favor process supervision, and wanted to see RLHF application. Reviewer HKpB (5, Marginally Below) wanted exploration beyond math and application to RLHF. Reviewer DxcT (6, Marginally Above) flagged reproducibility concerns (undisclosed model sizes) but acknowledged strong empirical results. The AC overruled the two negative reviews, accepting based on 'novel approach to training, strong empirical results, and dataset contribution.' Authors responded that small-scale results are reproducible on open models, pointed to Table 1's OOD generalization to physics/chemistry, and reframed process supervision as a cost-efficient paradigm. The key takeaway: the paper survived mixed reviews largely on the strength of its empirical contribution and dataset release — the reviewers who objected wanted broader scope and RL application, which became exactly the follow-up research agenda for the field.",

  "relevance_to_seed": "This is THE foundational paper for the Process Reward Models research area — it defined the PRM/ORM dichotomy, established the empirical case for process supervision, created the standard benchmark dataset (PRM800K), and identified the core open problems (automation of step-level labels, RL integration, domain generalization) that subsequent work directly addresses. Any research on step-level verification and credit assignment either builds on this paper's framework, dataset, or open questions; understanding its methodology and limitations is essential for identifying genuine gaps versus already-explored territory."
}
```

---

### Key Craft Lessons for Researchers

1. **Revisit "null results" at scale**: The most important move was recognizing that Uesato et al.'s finding of "no difference" was scale-dependent. This is a repeatable research strategy — when a prior comparison finds no difference with limited resources, scaling up the comparison can break the tie.

2. **Separate your experiment into "frontier" and "controlled"**: The dual large-scale / small-scale design was clever — large-scale for impressive headline numbers, small-scale with synthetic oracles for rigorous ablations. This let them make both a practical and a scientific contribution in one paper.

3. **Release the expensive artifact**: The decision to release PRM800K was arguably more impactful than the experimental result itself. 800K human labels represent hundreds of thousands of dollars — by releasing this, they created a moat of citations and made themselves the reference point for the field.

4. **Frame technical work with broader impact**: The "negative alignment tax" framing (the aligned method also performs better) elevated this from a methods paper to a paper with alignment implications, broadening the audience and reviewer goodwill.

5. **Active learning as a meta-contribution**: The "convincing wrong-answer" selection strategy is independently reusable and was responsible for 2.6× efficiency gains — it shows that HOW you collect data matters as much as how much you collect.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09ae4b90-e24a-4b66-8cc5-05d1877b85cd",
  "isSidechain": false,
  "requestId": "req_011CbTJbMK9TRYxyy5RNxt1t",
  "type": "assistant",
  "uuid": "eb399410-2629-49f3-b568-6db899817ff6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S4Zjd1rCCXqD6iC7zeeUEy",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 650,
      "cache_read_input_tokens": 45326,
      "output_tokens": 2558,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 650,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2558,
          "cache_read_input_tokens": 45326,
          "cache_creation_input_tokens": 650,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 650
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

_source line 60_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-27 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "eb399410-2629-49f3-b568-6db899817ff6",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd"
}
```

---

### Runtime record

_source line 61_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze OpenAI's process reward models paper",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd"
}
```

---

### Runtime record

_source line 62_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-27 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "eb399410-2629-49f3-b568-6db899817ff6",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd"
}
```

---

### Runtime record

_source line 63_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze OpenAI's process reward models paper",
  "sessionId": "2d2f5f70-a94f-402d-8c92-8c562e7598cd"
}
```

---
