# Research conversation: You are a senior ML researcher performing a deep analysis of a published paper. **Today's date: 2026-05-27 (UTC).** ## Y

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 2
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-3/16b54da6-26d0-4432-a11f-ea44d2bee85d.jsonl`
- **Structured JSON:** [`175ec38a61514bfdb359.json`](../../sessions/17/175ec38a61514bfdb359.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T16:02:11.455Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T16:02:11.455Z",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d",
  "content": "You are a senior ML researcher performing a deep analysis of a published paper.\n\n**Today's date: 2026-05-27 (UTC).**\n\n## Your goal\n\nAnalyze this paper NOT just for what it does, but for **HOW it innovates** — what can we learn from its approach to doing research? What made this paper good enough for a top venue?\n\n## Research context\n\nWe are generating ideas in the area of: **Bridging Informal and Formal Mathematical Reasoning — Autoformalization and Proof Verification**\n\n## Paper to analyze\n\n{\n  \"title\": \"Seed-Prover: Deep and Broad Reasoning for Automated Theorem Proving\",\n  \"authors\": \"Luoxin Chen et al. (ByteDance Seed)\",\n  \"venue\": \"arXiv 2025\",\n  \"url\": \"https://arxiv.org/abs/2507.23726\",\n  \"why_important\": \"Solved 5/6 IMO 2025 problems formally — the strongest known formal reasoning system. Saturated miniF2F and achieved >50% on PutnamBench, far exceeding prior work.\",\n  \"one_line_summary\": \"A lemma-style whole-proof reasoning system that uses iterative refinement with Lean feedback and self-summarization, proving 78.1% of past IMO problems and 5/6 of IMO 2025.\"\n}\n\n## Instructions\n\n1. **Deep read**: Use WebFetch to read this paper's full abstract, introduction, method section, and conclusion on arXiv or OpenReview. If it's on OpenReview, also read the reviewer comments and author responses.\n\n2. **Analyze the innovation structure**: Don't just summarize — dissect HOW the authors arrived at their contribution:\n   - What gap did they identify and HOW did they find it?\n   - What was the key insight that others missed?\n   - How did they formulate the problem differently from prior work?\n   - What existing technique did they adapt/combine/simplify?\n\n3. **Learn from reviewers**: If you can find reviewer comments, extract:\n   - What did reviewers praise most?\n   - What concerns were raised and how were they addressed?\n   - What would have made this paper even stronger?\n\n## Output format\n\nOutput a single JSON object:\n{\n  \"title\": \"Paper title\",\n  \"venue\": \"Where published\",\n  \"problem_identification\": \"What gap/problem did they identify? How did they find it? (2-3 sentences)\",\n  \"key_insight\": \"The core intellectual contribution — the aha moment (1-2 sentences)\",\n  \"innovation_type\": \"new_formulation | new_technique | new_benchmark | simplification | cross_domain | combination | scaling | analysis\",\n  \"method_summary\": \"Technical approach in 3-5 sentences — enough to understand the machinery\",\n  \"what_makes_it_good\": \"Why did this paper get accepted? What would reviewers have liked? (2-3 sentences)\",\n  \"limitations_acknowledged\": \"What gaps did the authors themselves identify? (1-2 sentences)\",\n  \"open_questions\": \"What follow-up questions does this paper raise? What remains unsolved? (2-3 bullet points)\",\n  \"building_blocks\": [\"List of methods/tools/datasets used that could be reused\"],\n  \"reviewer_feedback_summary\": \"If found on OpenReview: key praise and concerns. Otherwise: null\",\n  \"relevance_to_seed\": \"How does this paper relate to our research area? What can we learn from it? (1-2 sentences)\"\n}\n\nBe analytical, not descriptive. We want to learn the CRAFT of doing good research, not just know what this paper did."
}
```

---

### Runtime record

_source line 2 · 2026-05-27T16:02:11.459Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T16:02:11.459Z",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d"
}
```

---

## Round 1

26 recorded events

### User

_source line 3 · 2026-05-27T16:02:11.511Z_

You are a senior ML researcher performing a deep analysis of a published paper.

**Today's date: 2026-05-27 (UTC).**

## Your goal

Analyze this paper NOT just for what it does, but for **HOW it innovates** — what can we learn from its approach to doing research? What made this paper good enough for a top venue?

## Research context

We are generating ideas in the area of: **Bridging Informal and Formal Mathematical Reasoning — Autoformalization and Proof Verification**

## Paper to analyze

{
  "title": "Seed-Prover: Deep and Broad Reasoning for Automated Theorem Proving",
  "authors": "Luoxin Chen et al. (ByteDance Seed)",
  "venue": "arXiv 2025",
  "url": "https://arxiv.org/abs/2507.23726",
  "why_important": "Solved 5/6 IMO 2025 problems formally — the strongest known formal reasoning system. Saturated miniF2F and achieved >50% on PutnamBench, far exceeding prior work.",
  "one_line_summary": "A lemma-style whole-proof reasoning system that uses iterative refinement with Lean feedback and self-summarization, proving 78.1% of past IMO problems and 5/6 of IMO 2025."
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
  "promptId": "90291295-f415-450f-a2ae-7009e730e84a",
  "type": "user",
  "uuid": "9fa13e06-ac34-4cd7-828b-65b323a1ec0f",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T16:02:11.510Z_

```json
{
  "parentUuid": "9fa13e06-ac34-4cd7-828b-65b323a1ec0f",
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
  "uuid": "4c19c155-8a28-490b-a02a-9f8dde5a8cd1",
  "timestamp": "2026-05-27T16:02:11.510Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T16:02:11.510Z_

```json
{
  "parentUuid": "4c19c155-8a28-490b-a02a-9f8dde5a8cd1",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "1268a4ba-eb00-41d1-adfa-82e66513a6a3",
  "timestamp": "2026-05-27T16:02:11.510Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d",
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
  "aiTitle": "Analyze Seed-Prover paper for research innovation",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d"
}
```

---

### Assistant

_source line 7 · 2026-05-27T16:02:14.312Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to analyze the paper "Seed-Prover: Deep and Broad Reasoning for Automated Theorem Proving" from arXiv. Let me fetch the paper to read its content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1268a4ba-eb00-41d1-adfa-82e66513a6a3",
  "isSidechain": false,
  "requestId": "req_011CbTMXV1yommkswNB2zjyF",
  "type": "assistant",
  "uuid": "53ed2bf5-1d12-4b8e-8879-b14577bc07f9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C2SxNnBiRcYrNee4oG47eG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2216,
      "cache_read_input_tokens": 11014,
      "output_tokens": 156,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2216,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 156,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 2216,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2216
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

_source line 8 · 2026-05-27T16:02:14.943Z_

I'll start by fetching the paper from arXiv to read its full content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53ed2bf5-1d12-4b8e-8879-b14577bc07f9",
  "isSidechain": false,
  "requestId": "req_011CbTMXV1yommkswNB2zjyF",
  "type": "assistant",
  "uuid": "df231f18-d8e6-466b-9162-3198f441c99c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C2SxNnBiRcYrNee4oG47eG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2216,
      "cache_read_input_tokens": 11014,
      "output_tokens": 156,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2216,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 156,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 2216,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2216
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

_source line 9 · 2026-05-27T16:02:15.251Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QHPhdpgXk2ThaPsHEkvarU`</summary>

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
  "parentUuid": "df231f18-d8e6-466b-9162-3198f441c99c",
  "isSidechain": false,
  "requestId": "req_011CbTMXV1yommkswNB2zjyF",
  "type": "assistant",
  "uuid": "6fb031fe-9ec2-4057-b5e2-606dff7c015f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C2SxNnBiRcYrNee4oG47eG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2216,
      "cache_read_input_tokens": 11014,
      "output_tokens": 156,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2216,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 156,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 2216,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2216
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

_source line 10 · 2026-05-27T16:02:15.260Z_

<details><summary>↩ Tool result · `toolu_01QHPhdpgXk2ThaPsHEkvarU`</summary>

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
  "parentUuid": "6fb031fe-9ec2-4057-b5e2-606dff7c015f",
  "isSidechain": false,
  "promptId": "90291295-f415-450f-a2ae-7009e730e84a",
  "type": "user",
  "uuid": "cc5c3f8e-4c2d-4043-b6e9-17f7221daff3",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "6fb031fe-9ec2-4057-b5e2-606dff7c015f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-27T16:02:18.101Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me fetch the paper from arXiv. I'll fetch both the abstract page and the full PDF (via the HTML version).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc5c3f8e-4c2d-4043-b6e9-17f7221daff3",
  "isSidechain": false,
  "requestId": "req_011CbTMXmFJBA9mVNm55oUNo",
  "type": "assistant",
  "uuid": "f7951ee3-68b8-47e4-a213-4e32137ca281",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V5KEerVcFkNRDyqzn35yaR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 676,
      "cache_read_input_tokens": 13230,
      "output_tokens": 372,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 676,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 372,
          "cache_read_input_tokens": 13230,
          "cache_creation_input_tokens": 676,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 676
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

_source line 12 · 2026-05-27T16:02:18.601Z_

Now let me fetch the paper content from multiple sources in parallel to get comprehensive coverage.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7951ee3-68b8-47e4-a213-4e32137ca281",
  "isSidechain": false,
  "requestId": "req_011CbTMXmFJBA9mVNm55oUNo",
  "type": "assistant",
  "uuid": "c528b99e-42a2-4c39-8145-e7fd31d0d516",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V5KEerVcFkNRDyqzn35yaR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 676,
      "cache_read_input_tokens": 13230,
      "output_tokens": 372,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 676,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 372,
          "cache_read_input_tokens": 13230,
          "cache_creation_input_tokens": 676,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 676
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

_source line 13 · 2026-05-27T16:02:20.618Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0169DN5ooZ9e5vJjVqKxNDy6`</summary>

```json
{
  "url": "https://arxiv.org/abs/2507.23726",
  "prompt": "Extract the full abstract, author list, and any other metadata available on this arXiv page for the paper \"Seed-Prover\". Include all text content visible on the page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c528b99e-42a2-4c39-8145-e7fd31d0d516",
  "isSidechain": false,
  "requestId": "req_011CbTMXmFJBA9mVNm55oUNo",
  "type": "assistant",
  "uuid": "3b875089-ca19-4754-9b87-1f0c54eb6221",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V5KEerVcFkNRDyqzn35yaR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 676,
      "cache_read_input_tokens": 13230,
      "output_tokens": 372,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 676,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 372,
          "cache_read_input_tokens": 13230,
          "cache_creation_input_tokens": 676,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 676
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

_source line 14 · 2026-05-27T16:02:26.852Z_

<details><summary>↩ Tool result · `toolu_01U2ZKjwqN5AFNUHAQQS7FyP`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0e1b1a9-a730-4368-bbec-c7305239d950",
  "isSidechain": false,
  "promptId": "90291295-f415-450f-a2ae-7009e730e84a",
  "type": "user",
  "uuid": "d8b96d74-6e94-4ee6-ac68-2207914b908c",
  "toolUseResult": {
    "bytes": 0,
    "code": 404,
    "codeText": "Not Found",
    "result": "The server returned HTTP 404 Not Found.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.",
    "durationMs": 6,
    "url": "https://arxiv.org/html/2507.23726"
  },
  "sourceToolAssistantUUID": "c0e1b1a9-a730-4368-bbec-c7305239d950",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-27T16:02:26.842Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01U2ZKjwqN5AFNUHAQQS7FyP`</summary>

```json
{
  "url": "https://arxiv.org/html/2507.23726",
  "prompt": "Extract the COMPLETE text of this paper, focusing especially on: \n1. The full Introduction section - what problem they identify, what gap they found, what prior work missed\n2. The full Method/Approach section - all technical details of their system architecture, training pipeline, inference strategy\n3. The Results section - key numbers, comparisons, ablations\n4. The Conclusion/Discussion section - limitations, future work\n5. Any details about their training data, reward models, or reinforcement learning setup\n\nBe as comprehensive as possible. Include all technical details, equations references, and specific numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b875089-ca19-4754-9b87-1f0c54eb6221",
  "isSidechain": false,
  "requestId": "req_011CbTMXmFJBA9mVNm55oUNo",
  "type": "assistant",
  "uuid": "c0e1b1a9-a730-4368-bbec-c7305239d950",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V5KEerVcFkNRDyqzn35yaR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 676,
      "cache_read_input_tokens": 13230,
      "output_tokens": 372,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 676,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 372,
          "cache_read_input_tokens": 13230,
          "cache_creation_input_tokens": 676,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 676
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

_source line 16 · 2026-05-27T16:02:28.177Z_

<details><summary>↩ Tool result · `toolu_0169DN5ooZ9e5vJjVqKxNDy6`</summary>

```text
# Seed-Prover: Paper Metadata and Abstract

## Title
Seed-Prover: Deep and Broad Reasoning for Automated Theorem Proving

## arXiv Identifier
arXiv:2507.23726 [cs.AI]

## Submission Information
- **Initial submission:** July 31, 2025
- **Latest version:** August 1, 2025 (v2)
- **Submitter:** Wenlei Shi

## Author List
The paper includes 36 authors, including Luoxin Chen, Jinming Gu, Liankai Huang, Wenhao Huang, Zhicheng Jiang, Allan Jie, Xiaoran Jin, Xing Jin, Chenggang Li, Kaijing Ma, Cheng Ren, Jiawei Shen, Wenlei Shi, Tong Sun, He Sun, Jiahui Wang, Siran Wang, Zhihong Wang, Chenrui Wei, Shufa Wei, Yonghui Wu, Yuchen Wu, Yihang Xia, Huajian Xin, Fan Yang, Huaiyuan Ying, Hongyi Yuan, Zheng Yuan, Tianyang Zhan, Chi Zhang, Yue Zhang, Ge Zhang, Tianyun Zhao, Jianqiu Zhao, Yichi Zhou, and Thomas Hanwen Zhu.

## Abstract Summary
The research presents a system for automated theorem proving using LLMs. The work introduces "a lemma-style whole-proof reasoning model" capable of iteratively refining proofs using Lean feedback and self-summarization. Key achievements include proving 78.1% of formalized IMO problems, saturating MiniF2F benchmark, and exceeding 50% on PutnamBench. A companion geometry engine was developed, and the systems solved 5 of 6 IMO 2025 problems.

## Subject Classification
- Artificial Intelligence (cs.AI)
- Computation and Language (cs.CL)

## License
Creative Commons Attribution 4.0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b875089-ca19-4754-9b87-1f0c54eb6221",
  "isSidechain": false,
  "promptId": "90291295-f415-450f-a2ae-7009e730e84a",
  "type": "user",
  "uuid": "2d744216-3bb9-4d9e-ad2d-1983be4bcd69",
  "toolUseResult": {
    "bytes": 51426,
    "code": 200,
    "codeText": "OK",
    "result": "# Seed-Prover: Paper Metadata and Abstract\n\n## Title\nSeed-Prover: Deep and Broad Reasoning for Automated Theorem Proving\n\n## arXiv Identifier\narXiv:2507.23726 [cs.AI]\n\n## Submission Information\n- **Initial submission:** July 31, 2025\n- **Latest version:** August 1, 2025 (v2)\n- **Submitter:** Wenlei Shi\n\n## Author List\nThe paper includes 36 authors, including Luoxin Chen, Jinming Gu, Liankai Huang, Wenhao Huang, Zhicheng Jiang, Allan Jie, Xiaoran Jin, Xing Jin, Chenggang Li, Kaijing Ma, Cheng Ren, Jiawei Shen, Wenlei Shi, Tong Sun, He Sun, Jiahui Wang, Siran Wang, Zhihong Wang, Chenrui Wei, Shufa Wei, Yonghui Wu, Yuchen Wu, Yihang Xia, Huajian Xin, Fan Yang, Huaiyuan Ying, Hongyi Yuan, Zheng Yuan, Tianyang Zhan, Chi Zhang, Yue Zhang, Ge Zhang, Tianyun Zhao, Jianqiu Zhao, Yichi Zhou, and Thomas Hanwen Zhu.\n\n## Abstract Summary\nThe research presents a system for automated theorem proving using LLMs. The work introduces \"a lemma-style whole-proof reasoning model\" capable of iteratively refining proofs using Lean feedback and self-summarization. Key achievements include proving 78.1% of formalized IMO problems, saturating MiniF2F benchmark, and exceeding 50% on PutnamBench. A companion geometry engine was developed, and the systems solved 5 of 6 IMO 2025 problems.\n\n## Subject Classification\n- Artificial Intelligence (cs.AI)\n- Computation and Language (cs.CL)\n\n## License\nCreative Commons Attribution 4.0",
    "durationMs": 7553,
    "url": "https://arxiv.org/abs/2507.23726"
  },
  "sourceToolAssistantUUID": "3b875089-ca19-4754-9b87-1f0c54eb6221",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-27T16:02:30.970Z_

<details><summary>Logged reasoning block</summary>

```text
The HTML version returned a 404. Let me try the PDF version or another format.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d744216-3bb9-4d9e-ad2d-1983be4bcd69",
  "isSidechain": false,
  "requestId": "req_011CbTMYi93ZMyy9rtxJxaAL",
  "type": "assistant",
  "uuid": "ba68ca2f-8039-41bb-84ae-fada08c2fe85",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bar2AZx5ZX7gb5b67vytha",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 899,
      "cache_read_input_tokens": 13906,
      "output_tokens": 386,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 899,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 85,
          "output_tokens": 386,
          "cache_read_input_tokens": 13906,
          "cache_creation_input_tokens": 899,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 899
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

_source line 18 · 2026-05-27T16:02:31.465Z_

The HTML version isn't available yet. Let me try the PDF and also check for any related blog posts or detailed descriptions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba68ca2f-8039-41bb-84ae-fada08c2fe85",
  "isSidechain": false,
  "requestId": "req_011CbTMYi93ZMyy9rtxJxaAL",
  "type": "assistant",
  "uuid": "5e708f5c-b9dd-46a0-84ef-31f6f018a61d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bar2AZx5ZX7gb5b67vytha",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 899,
      "cache_read_input_tokens": 13906,
      "output_tokens": 386,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 899,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 85,
          "output_tokens": 386,
          "cache_read_input_tokens": 13906,
          "cache_creation_input_tokens": 899,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 899
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

_source line 19 · 2026-05-27T16:02:33.416Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01F8zGDhdBmWXQok4AoRMCCq`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2507.23726",
  "prompt": "Extract the COMPLETE text of this paper, focusing especially on:\n1. The full Introduction section - what problem they identify, what gap they found, what prior work missed\n2. The full Method/Approach section - all technical details of their system architecture, training pipeline, inference strategy\n3. The Results section - key numbers, comparisons, ablations\n4. The Conclusion/Discussion section - limitations, future work\n5. Any details about their training data, reward models, or reinforcement learning setup\n\nBe as comprehensive as possible. Include all technical details and specific numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e708f5c-b9dd-46a0-84ef-31f6f018a61d",
  "isSidechain": false,
  "requestId": "req_011CbTMYi93ZMyy9rtxJxaAL",
  "type": "assistant",
  "uuid": "67d29b3b-a27d-42f9-8044-9ebdd8e96ba4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bar2AZx5ZX7gb5b67vytha",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 899,
      "cache_read_input_tokens": 13906,
      "output_tokens": 386,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 899,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 85,
          "output_tokens": 386,
          "cache_read_input_tokens": 13906,
          "cache_creation_input_tokens": 899,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 899
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

_source line 20 · 2026-05-27T16:02:34.714Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Eoo44M97TYRQG72kvWdqHs`</summary>

```json
{
  "url": "https://arxiv.org/html/2507.23726v2",
  "prompt": "Extract the COMPLETE text of this paper. I need all sections: Introduction, Method, Related Work, Experiments, Results, Ablation Studies, Discussion, Conclusion. Include all technical details, training procedures, architecture choices, benchmark numbers, and limitations discussed. Be maximally comprehensive."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67d29b3b-a27d-42f9-8044-9ebdd8e96ba4",
  "isSidechain": false,
  "requestId": "req_011CbTMYi93ZMyy9rtxJxaAL",
  "type": "assistant",
  "uuid": "1136e40b-f160-4e10-b752-08dfb16c0dcd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bar2AZx5ZX7gb5b67vytha",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 899,
      "cache_read_input_tokens": 13906,
      "output_tokens": 386,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 899,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 85,
          "output_tokens": 386,
          "cache_read_input_tokens": 13906,
          "cache_creation_input_tokens": 899,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 899
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

_source line 21 · 2026-05-27T16:02:34.879Z_

<details><summary>↩ Tool result · `toolu_01Eoo44M97TYRQG72kvWdqHs`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1136e40b-f160-4e10-b752-08dfb16c0dcd",
  "isSidechain": false,
  "promptId": "90291295-f415-450f-a2ae-7009e730e84a",
  "type": "user",
  "uuid": "b5d44589-ca23-4a7f-95bc-79517ccf7453",
  "toolUseResult": {
    "bytes": 0,
    "code": 404,
    "codeText": "Not Found",
    "result": "The server returned HTTP 404 Not Found.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.",
    "durationMs": 161,
    "url": "https://arxiv.org/html/2507.23726v2"
  },
  "sourceToolAssistantUUID": "1136e40b-f160-4e10-b752-08dfb16c0dcd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-27 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "b5d44589-ca23-4a7f-95bc-79517ccf7453",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze Seed-Prover paper for research innovation",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d"
}
```

---

### Tool result

_source line 24 · 2026-05-27T16:02:47.689Z_

<details><summary>↩ Tool result · `toolu_01F8zGDhdBmWXQok4AoRMCCq`</summary>

```text
# Seed-Prover: Deep and Broad Reasoning for Automated Theorem Proving

## Overview

This paper introduces Seed-Prover, a system designed for automated theorem proving (ATP) in formal mathematics using large language models. The work addresses fundamental challenges in applying LLMs to formal proof generation.

## Introduction & Problem Identification

The authors identify that while recent advances like DeepSeek-R1 and OpenAI o1 have shown promise in mathematical reasoning, translating this to formal theorem proving remains challenging. The key gap is that existing approaches struggle with the depth and breadth required for complex formal proofs.

The paper notes that prior work has pursued either "deep reasoning" (exploring solution paths thoroughly) or "broad search" (exploring many alternatives), but rarely both simultaneously. This limitation constrains performance on benchmark problems like miniF2F.

## Method & Architecture

### System Components

Seed-Prover employs a multi-faceted approach combining:

1. **Proof Search Strategy**: The system implements both depth-first exploration with reasoning tokens and breadth-first best-first search using tree structures

2. **Tactic Generation**: Uses language models to generate Lean 4 tactics (formal proof commands) conditioned on:
   - Current proof state
   - Previous successful tactics
   - Contextual information from related theorems

3. **Reward Modeling**: Implements separate reward models for:
   - Intermediate progress signals
   - Proof completion
   - Training stability using RL

### Training Pipeline

The paper describes a multi-stage training approach:

- **Supervised Fine-tuning (SFT)**: Initial training on successful proof traces from existing formal math datasets
- **Reinforcement Learning**: Uses process-level rewards based on proof state progression rather than just final outcomes
- **Data Curation**: Selective sampling from BigMath and Lean GitHub datasets, with quality filtering

### Inference Strategy

At inference, the system:
- Allocates compute tokens between reasoning depth and search breadth
- Uses best-first tree search guided by learned value estimates
- Implements backtracking with adaptive search depth limits
- Applies self-correction mechanisms when tactics fail

## Results & Empirical Performance

### Key Numbers

On the miniF2F benchmark:
- Achieves "state-of-the-art" results compared to prior ATP systems
- Shows significant improvements over baseline LLM approaches on formal theorem proving
- Demonstrates gains from both depth (reasoning) and breadth (search) components

The paper includes comparisons showing that:
- Systems using only breadth-first search plateau early
- Pure depth-first reasoning without search guidance underperforms
- Combined approach yields multiplicative gains

### Ablation Studies

Critical ablations demonstrate:
- Reward model quality directly impacts training efficiency
- Allocation of tokens between reasoning and search affects performance across problem difficulty ranges
- RL training provides larger gains than SFT alone

## Technical Details

### Data & Training

- Uses approximately 100K+ formal proof examples from curated sources
- Implements importance sampling to balance proof difficulty
- Applies loss weighting based on proof complexity
- Training conducted with distributed computing across multiple GPUs

### Model Architecture

- Built on transformer-based language models (specifics suggest use of ByteDance's internal models based on author affiliations)
- Custom vocabulary optimized for Lean syntax
- Special tokens for proof state representation and tactic sequences

## Discussion & Limitations

The authors acknowledge:

1. **Computational Cost**: The system requires significant compute for inference compared to pure neural approaches
2. **Formal Language Specificity**: Current work targets Lean 4; generalization to other proof assistants uncertain
3. **Scalability Questions**: Unknown how approach scales to very-long-horizon proofs requiring 100+ tactics
4. **Human Interpretability**: Generated proofs may lack pedagogical clarity despite formal correctness

## Contributions

Key innovations include:
- Integrated depth-breadth reasoning architecture for formal ATP
- Process-reward RL training methodology adapted for proof search
- Empirical demonstration that combined reasoning + search significantly outperforms isolated approaches
- Open-sourced implementation enabling community evaluation

The work represents significant progress toward practical AI-assisted formal mathematics, though substantial challenges remain in scaling to industrial-strength verification tasks.

[Binary content (application/pdf, 596.9KB) also saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/16b54da6-26d0-4432-a11f-ea44d2bee85d/tool-results/webfetch-1779897753435-mgp0ud.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67d29b3b-a27d-42f9-8044-9ebdd8e96ba4",
  "isSidechain": false,
  "promptId": "90291295-f415-450f-a2ae-7009e730e84a",
  "type": "user",
  "uuid": "5738c4f7-e30f-4808-a941-8d7ec9dfae4d",
  "toolUseResult": {
    "bytes": 611244,
    "code": 200,
    "codeText": "OK",
    "result": "# Seed-Prover: Deep and Broad Reasoning for Automated Theorem Proving\n\n## Overview\n\nThis paper introduces Seed-Prover, a system designed for automated theorem proving (ATP) in formal mathematics using large language models. The work addresses fundamental challenges in applying LLMs to formal proof generation.\n\n## Introduction & Problem Identification\n\nThe authors identify that while recent advances like DeepSeek-R1 and OpenAI o1 have shown promise in mathematical reasoning, translating this to formal theorem proving remains challenging. The key gap is that existing approaches struggle with the depth and breadth required for complex formal proofs.\n\nThe paper notes that prior work has pursued either \"deep reasoning\" (exploring solution paths thoroughly) or \"broad search\" (exploring many alternatives), but rarely both simultaneously. This limitation constrains performance on benchmark problems like miniF2F.\n\n## Method & Architecture\n\n### System Components\n\nSeed-Prover employs a multi-faceted approach combining:\n\n1. **Proof Search Strategy**: The system implements both depth-first exploration with reasoning tokens and breadth-first best-first search using tree structures\n\n2. **Tactic Generation**: Uses language models to generate Lean 4 tactics (formal proof commands) conditioned on:\n   - Current proof state\n   - Previous successful tactics\n   - Contextual information from related theorems\n\n3. **Reward Modeling**: Implements separate reward models for:\n   - Intermediate progress signals\n   - Proof completion\n   - Training stability using RL\n\n### Training Pipeline\n\nThe paper describes a multi-stage training approach:\n\n- **Supervised Fine-tuning (SFT)**: Initial training on successful proof traces from existing formal math datasets\n- **Reinforcement Learning**: Uses process-level rewards based on proof state progression rather than just final outcomes\n- **Data Curation**: Selective sampling from BigMath and Lean GitHub datasets, with quality filtering\n\n### Inference Strategy\n\nAt inference, the system:\n- Allocates compute tokens between reasoning depth and search breadth\n- Uses best-first tree search guided by learned value estimates\n- Implements backtracking with adaptive search depth limits\n- Applies self-correction mechanisms when tactics fail\n\n## Results & Empirical Performance\n\n### Key Numbers\n\nOn the miniF2F benchmark:\n- Achieves \"state-of-the-art\" results compared to prior ATP systems\n- Shows significant improvements over baseline LLM approaches on formal theorem proving\n- Demonstrates gains from both depth (reasoning) and breadth (search) components\n\nThe paper includes comparisons showing that:\n- Systems using only breadth-first search plateau early\n- Pure depth-first reasoning without search guidance underperforms\n- Combined approach yields multiplicative gains\n\n### Ablation Studies\n\nCritical ablations demonstrate:\n- Reward model quality directly impacts training efficiency\n- Allocation of tokens between reasoning and search affects performance across problem difficulty ranges\n- RL training provides larger gains than SFT alone\n\n## Technical Details\n\n### Data & Training\n\n- Uses approximately 100K+ formal proof examples from curated sources\n- Implements importance sampling to balance proof difficulty\n- Applies loss weighting based on proof complexity\n- Training conducted with distributed computing across multiple GPUs\n\n### Model Architecture\n\n- Built on transformer-based language models (specifics suggest use of ByteDance's internal models based on author affiliations)\n- Custom vocabulary optimized for Lean syntax\n- Special tokens for proof state representation and tactic sequences\n\n## Discussion & Limitations\n\nThe authors acknowledge:\n\n1. **Computational Cost**: The system requires significant compute for inference compared to pure neural approaches\n2. **Formal Language Specificity**: Current work targets Lean 4; generalization to other proof assistants uncertain\n3. **Scalability Questions**: Unknown how approach scales to very-long-horizon proofs requiring 100+ tactics\n4. **Human Interpretability**: Generated proofs may lack pedagogical clarity despite formal correctness\n\n## Contributions\n\nKey innovations include:\n- Integrated depth-breadth reasoning architecture for formal ATP\n- Process-reward RL training methodology adapted for proof search\n- Empirical demonstration that combined reasoning + search significantly outperforms isolated approaches\n- Open-sourced implementation enabling community evaluation\n\nThe work represents significant progress toward practical AI-assisted formal mathematics, though substantial challenges remain in scaling to industrial-strength verification tasks.\n\n[Binary content (application/pdf, 596.9KB) also saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/16b54da6-26d0-4432-a11f-ea44d2bee85d/tool-results/webfetch-1779897753435-mgp0ud.pdf]",
    "durationMs": 14268,
    "url": "https://arxiv.org/pdf/2507.23726"
  },
  "sourceToolAssistantUUID": "67d29b3b-a27d-42f9-8044-9ebdd8e96ba4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-27T16:02:51.090Z_

<details><summary>Logged reasoning block</summary>

```text
I got some content from the PDF but it's a summary rather than the full text. Let me try to read the actual PDF that was saved, and also search for more detailed information about this paper - blog posts, etc.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5738c4f7-e30f-4808-a941-8d7ec9dfae4d",
  "isSidechain": false,
  "requestId": "req_011CbTMa9fjdrprUjiKtxweL",
  "type": "assistant",
  "uuid": "13b34747-0369-44fd-9de0-f65495dac848",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvqndJtFZyZKQd74sb5gzi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 1539,
      "cache_read_input_tokens": 14805,
      "output_tokens": 342,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1539,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 85,
          "output_tokens": 342,
          "cache_read_input_tokens": 14805,
          "cache_creation_input_tokens": 1539,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1539
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

_source line 26 · 2026-05-27T16:02:51.675Z_

Good, I got a PDF saved. Let me read it directly and also search for additional details about this paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13b34747-0369-44fd-9de0-f65495dac848",
  "isSidechain": false,
  "requestId": "req_011CbTMa9fjdrprUjiKtxweL",
  "type": "assistant",
  "uuid": "fdf753b4-e00b-4fd0-a54d-98f952a2de4c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvqndJtFZyZKQd74sb5gzi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 1539,
      "cache_read_input_tokens": 14805,
      "output_tokens": 342,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1539,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 85,
          "output_tokens": 342,
          "cache_read_input_tokens": 14805,
          "cache_creation_input_tokens": 1539,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1539
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

_source line 27 · 2026-05-27T16:02:52.545Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HPgYpxoueYFswVV9YfXSa8`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/16b54da6-26d0-4432-a11f-ea44d2bee85d/tool-results/webfetch-1779897753435-mgp0ud.pdf",
  "pages": "1-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdf753b4-e00b-4fd0-a54d-98f952a2de4c",
  "isSidechain": false,
  "requestId": "req_011CbTMa9fjdrprUjiKtxweL",
  "type": "assistant",
  "uuid": "8fff50a3-f6cf-4cf8-9dcc-eb47667b2a9a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvqndJtFZyZKQd74sb5gzi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 1539,
      "cache_read_input_tokens": 14805,
      "output_tokens": 342,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1539,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 85,
          "output_tokens": 342,
          "cache_read_input_tokens": 14805,
          "cache_creation_input_tokens": 1539,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1539
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

_source line 28 · 2026-05-27T16:02:53.186Z_

<details><summary>↩ Tool result · `toolu_01HPgYpxoueYFswVV9YfXSa8`</summary>

```text
PDF pages extracted: 10 page(s) from /home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/16b54da6-26d0-4432-a11f-ea44d2bee85d/tool-results/webfetch-1779897753435-mgp0ud.pdf (596.9KB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8fff50a3-f6cf-4cf8-9dcc-eb47667b2a9a",
  "isSidechain": false,
  "promptId": "90291295-f415-450f-a2ae-7009e730e84a",
  "type": "user",
  "uuid": "eca96c11-45c3-4801-8244-a252276282ef",
  "toolUseResult": {
    "type": "parts",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/16b54da6-26d0-4432-a11f-ea44d2bee85d/tool-results/webfetch-1779897753435-mgp0ud.pdf",
      "originalSize": 611244,
      "outputDir": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/16b54da6-26d0-4432-a11f-ea44d2bee85d/tool-results/pdf-4fc032a6-7f33-490f-971e-a4bff7a99605",
      "count": 10
    }
  },
  "sourceToolAssistantUUID": "8fff50a3-f6cf-4cf8-9dcc-eb47667b2a9a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

## Round 2

16 recorded events

### User

_source line 29 · 2026-05-27T16:02:53.184Z_

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eca96c11-45c3-4801-8244-a252276282ef",
  "isSidechain": false,
  "promptId": "90291295-f415-450f-a2ae-7009e730e84a",
  "type": "user",
  "isMeta": true,
  "uuid": "50d0f68d-cc67-43cb-849b-f8a4e39a6f2c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-27T16:02:53.924Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015nZhZ6EiKyS7zPsFT65rkC`</summary>

```json
{
  "url": "https://huggingface.co/papers/2507.23726",
  "prompt": "Extract all details about the Seed-Prover paper. Include the full abstract, any discussion, and all technical details mentioned. This is the paper about automated theorem proving from ByteDance that solved 5/6 IMO 2025 problems."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50d0f68d-cc67-43cb-849b-f8a4e39a6f2c",
  "isSidechain": false,
  "requestId": "req_011CbTMa9fjdrprUjiKtxweL",
  "type": "assistant",
  "uuid": "7e63e546-a34a-48e5-a9db-d65717b10735",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvqndJtFZyZKQd74sb5gzi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 1539,
      "cache_read_input_tokens": 14805,
      "output_tokens": 342,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1539,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 85,
          "output_tokens": 342,
          "cache_read_input_tokens": 14805,
          "cache_creation_input_tokens": 1539,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1539
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
  "leafUuid": "7e63e546-a34a-48e5-a9db-d65717b10735",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze Seed-Prover paper for research innovation",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d"
}
```

---

### Tool result

_source line 33 · 2026-05-27T16:02:54.630Z_

<details><summary>↩ Tool result · `toolu_015nZhZ6EiKyS7zPsFT65rkC`</summary>

```text
# Seed-Prover: Deep and Broad Reasoning for Automated Theorem Proving

ByteDance Seed AI4Math

## Abstract

LLMs have demonstrated strong mathematical reasoning abilities by leveraging reinforcement learning with long chain-of-thought, yet they continue to struggle with theorem proving due to the lack of clear supervision signals when solely using natural language. Dedicated domain-specific languages like Lean provide clear supervision via formal verification of proofs, enabling effective training through reinforcement learning. In this work, we propose **Seed-Prover**, a lemma-style whole-proof reasoning model. Seed-Prover can iteratively refine its proof based on Lean feedback, proved lemmas, and self-summarization. To solve IMO-level contest problems, we design three test-time inference strategies that enable both deep and broad reasoning. Seed-Prover proves 78.1% of formalized past IMO problems, saturates MiniF2F, and achieves over 50% on PutnamBench, outperforming the previous state-of-the-art by a large margin. To address the lack of geometry support in Lean, we introduce a geometry reasoning engine **Seed-Geometry**, which outperforms previous formal geometry engines. We use these two systems to participate in IMO 2025 and fully prove 5 out of 6 problems. This work represents a significant advancement in automated mathematical reasoning, demonstrating the effectiveness of formal verification with long chain-of-thought reasoning.

Project Page: &lt;https://github.com/ByteDance-Seed/Seed-Prover>

Figure 1 Growth in MiniF2F-Test performance over time.# 1 Introduction

Recent advances in large language models (LLMs) have shown extending reasoning lengths through natural language can significantly boost performance on math benchmarks such as MATH and AIME [4, 11]. Training such models requires reinforcement learning (RL) on verifiable answers. It is extremely difficult to automatically, or even manually, verify a proof in natural language since each step must be carefully checked for correctness [13]. This poses significant challenges for applying reinforcement learning to the training of large language models to prove mathematical statements. Unlike natural language, formal languages such as Lean can provide a clear and automatic signal on the correctness of a formalized proof. A noteworthy work from AlphaProof [3] uses Lean to successfully solve 3 problems from the 2024 International Mathematical Olympiad (IMO). AlphaProof demonstrates that LLMs using formal language are capable of proving very challenging problems that LLMs using natural language fail to prove.

There are two types of LLM formal provers, step-level provers [3, 14, 22, 23, 25] and whole-proof generation provers [5, 24]. Step-level provers incrementally generate Lean code line-by-line. While this enables close interaction with the Lean environment, it requires special scaffolding to generate a complete Lean proof, and the interaction is often too granular to allow high-level reasoning. In contrast, whole-proof models generate an entire Lean proof at once, but typically lack interaction with the Lean compiler. Recent work has shown that combining whole-proof models with long chain-of-thought reasoning [9, 15, 21] substantially outperforms step-level provers. In this work, we propose **Seed-Prover**, a whole-proof model with following features:

- • **Lemma-Style Proving:** Seed-Prover tries to generate useful intermediate lemmas before proving the main statement. These lemmas serve as shared knowledge across different inference paths.
- • **Iterative Proof Refinement:** Seed-Prover iteratively refines its proof based on Lean compiler feedback, previous proved lemmas, and self-summarization.
- • **Test-Time Scaling:** We implement a three-tiered inference strategy that enables Seed-Prover to think both deeply and broadly—allocating thinking budget to fine details while exploring interesting properties.
- • **SOTA Performance:** Seed-Prover proves 5 out of 6 problems in IMO 2025, saturates MiniF2F [31] (shown in Figure 1), and outperforms prior work by up to  $3\times$  on multiple formal benchmarks.

Due to the lack of sufficient geometry support in Lean, Seed-Prover incorporates a dedicated geometry reasoning engine **Seed-Geometry**. Similar to existing line of efforts in AlphaGeometry [2, 19] and TongGeometry [30], Seed-Geometry follows the forward-chaining design in the reasoning engine implementation, where the system derives all known facts by checking applicable rules until closure is reached. By backward-tracing fact dependencies, Seed-Geometry identifies the minimum dependency relations in a geometry problem’s configuration, separating the problem context from the auxiliary constructions necessary to prove a problem. Using statistics derived from more than past 20 years of math olympiad competitions, Seed-Geometry performs extensive search in the geometry space defined by its dedicated domain-specific language and establishes a repository of 230 million unique geometry problems requiring auxiliaries. A Seed model trained on such dedicated geometry data becomes an exceptionally effective neuro-symbolic geometry prover, where it fills in the missing auxiliary geometry elements and the geometry reasoning engine performs step-by-step forward-chaining, completing the final proof of a problem. In experiments, Seed-Geometry solves 43 of the IMO-AG-50 (*vs.* 42 by AlphaGeometry 2), a benchmark that curates geometry problems of IMO from 2000 to 2024. It also sets a new state-of-the-art on the IMO shortlist geometry problems from 2000 to 2022, and notably solves the geometry problem of IMO 2025 under just 2 seconds.

## 2 Approach

Here we introduce the two systems we used in IMO 2025, Seed-Geometry and Seed-Prover.

### 2.1 Seed-Geometry

Seed-Geometry builds on the success of TongGeometry [30] and performs a major redesign. From a global perspective, both systems leverage trained neural models to complete missing auxiliary constructions andspecialized reasoning engines to forward-chain derivation. However, Seed-Geometry is a substantial upgrade over TongGeometry in the following aspects.

### 2.1.1 Extended Domain-Specific Language

Seed-Geometry constructs geometric diagrams in the principle of ruler-and-compass construction. However, plain ruler-and-compass construction steps can be long and cumbersome, making the language representation of the constructions overly verbose, introducing unnecessary burden on both the neural processing of Transformer-based large language model and the symbolic derivation of the backend engine. To mitigate these issues, Seed-Geometry groups particular action sequences into specific actions, making the representation of the problem concise enough. Of particular note, Seed-Geometry has several such composite actions: isogonal conjugate with respect to a triangle and a point, exsimilitude center of two circles, insimilitude center of two circles. All three actions can be represented with primitive ruler-and-compass actions; yet the construction sequence in itself is non-trivial and unnecessarily clumsy.

### 2.1.2 Extremely Fast Reasoning Engine

Seed-Geometry improved its reasoning engine’s performance by rewriting its backend in C++ and making it accessible to Python users through Pybind11. This change led to roughly 100-fold speed increase compared to the Python implementation in TongGeometry. The C++ implementation handles memory more efficiently and benefits from compiler optimizations, allowing for much faster **deep** searches within the reasoning engine. This is particularly crucial because the engine’s forward-chaining design typically slows down considerably when the search tree expands widely at deeper levels.

### 2.1.3 Exceptional Large Language Model

Seed-Geometry utilizes a high-performing large language model from the Seed family [17]. This particular Seed model has undergone extensive pre-training on vast datasets of coding and mathematics, granting it a wide array of specialized skills. The specific model size was chosen considering the number of data tokens. We considered training two models in an actor–critic setup initially: the policy model that proposed possible next auxiliary element to construct and a value model that predicted the number of steps to go from the state. However, we note from preliminary experiments that a single Seed model serving as the policy would suffice, contradicting the design of both a policy model and a value model in existing work [30]. We also note that a policy model unspecialized to the specific goal makes both training and solving more manageable and therefore, we only trained the model on pairs of problem context and auxiliaries, without the target fact goal in the prompt.

### 2.1.4 Extensive Search

When presented with a new problem, Seed-Geometry first transforms the representation into a canonical form. If the reasoning backend successfully finds the goal fact to prove in the reasoning process, the problem is considered immediately solved. Otherwise, Seed-Geometry initiates a search process. In particular, Seed-Geometry employs beam search, with the policy model generating proposals for each beam in the buffer. With the extremely fast reasoning engine, Seed-Geometry supports running each new generated proposal in time. If any one of the proposal leads to the proof, the problem is considered proven; otherwise we select the top few proposals for the next step of expansion in the search tree based on each proposal’s cumulative negative log likelihood. The search process terminates until a fixed number of steps have been consumed. Seed-Geometry’s search process is made efficient and scalable. Compared to TongGeometry, Seed-Geometry’s solving process supports a distributed setup where each GPU process communicates with each other and blocked only at the beam selection point. Each GPU process is also equipped with a CPU thread pool that asynchronously executes the reasoning step during language model inference such that the reasoning cost can be overlapped with language model inference.&lt;table border="1">
&lt;thead>
&lt;tr>
&lt;th>Whole proof&lt;/th>
&lt;th>Lemma-style&lt;/th>
&lt;/tr>
&lt;/thead>
&lt;tbody>
&lt;tr>
&lt;td>
&lt;pre>
theorem eg : 1 + 2 = 3 := by
  have h0 : 1 + 1 = 2 := by
    ring

  have h1 : 1 + (1 + 1) = 3 := by
    ring

  linarith [h0, h1]

#print axioms eg
&lt;/pre>
&lt;/td>
&lt;td>
&lt;pre>
lemma round1_h0 : 1 + 1 = 2 := by
  ring

lemma round1_h1 : 1 + (1 + 1) = 3 := by
  ring

theorem eg : 1 + 2 = 3 := by
  linarith [round1_h0, round1_h1]

#print axioms eg
&lt;/pre>
&lt;/td>
&lt;/tr>
&lt;/tbody>
&lt;/table>

Figure 2 An example of whole proof and lemma-style proof in Lean 4.

## 2.2 Seed-Prover

Seed-Prover is a large language model specialized in formal reasoning in Lean 4. Its most significant distinction from prior work lies in its adoption of lemma-style proving as the proof paradigm, which places **lemmas** at the center of the reasoning process. This approach offers several key advantages: it enables clear identification of lemmas that have and have not been proved, indicating the progress made in solving the main problem; lemmas can be processed independently and combined freely; lemmas from different inference trajectories can be combined to address more challenging problems. Both the training and inference procedures of Seed-Prover are designed around lemmas.

### 2.2.1 Lemma-Style Proving

Previous works [9, 15, 21] trained the model to generate whole proofs starting with the keyword *theorem*. In contrast, we first require the model to generate some useful lemmas—each introduced by the keyword *lemma*—before generating the main proof using *theorem* by applying the generated lemmas. An example is shown in Figure 2. This lemma-style proof provides following merits. First, it allows clear identification of the lemmas that have been successfully proved, and those that need further refinement. Second, lemmas are modular—they can be compiled independently, stored independently, and combined freely. Additionally, proofs of lemmas may provide inspiration to the model for proving unproved lemmas and the main problem. To enable this workflow, we establish a lemma pool for each difficult problem, which stores comprehensive data from all our inference runs, including lemma statements, lemma names, complete proofs, proof difficulties, and dependency relations. The lemma pool is typically used to (1) retrieve the most relevant lemmas by name or formal statement; (2) sample the most difficult lemmas according to their proof difficulty.

### 2.2.2 Conjecture Proposing

When tackling challenging contest-level math problems, human contestants often identify interesting properties of the problem and use them to guide their reasoning. Seed-Prover is trained to propose such potentially useful properties by chain-of-thought reasoning. Notably, this process differs from chain-of-thought reasoning to solve the problem directly; rather, it emphasizes broad exploration of the problem space without committing to a particular approach. Take functional equations as an example: one might conjecture that the function is *injective*, *surjective*, *bijective*, *monotonic*, or *periodic*—all without engaging in deep, targeted reasoning about the problem itself. In a sense, many useful properties of a problem may be enumerated before full problem resolution. The proposer module accepts an unsolved problem and, optionally, some already proved lemmas as input, and generates 10–50 candidate conjectures about properties of the problem. Proposing multiple conjectures in parallel significantly increases diversity and the likelihood of covering the valuable properties. For each problem, we may repeat this process multiple times to create a large conjecture pool.

This approach differs from Draft, Sketch, Prove [7], which presumes the ability to fully solve the problem upfront. In contrast, our method performs broad exploratory searches over the problem space enabling**Figure 3** The workflows of single-pass whole proof generation, light, and medium inference settings.

discovery of useful properties, which makes it possible to solve problems that the model cannot solve directly in natural language.

### 2.2.3 Training

To enable seamless interaction between Seed-Prover and Lean, we adopt multi-stage, multi-task reinforcement learning (RL) based on VAPO [29]. The RL reward is 1 if the formal statement is successfully proven, and 0 otherwise. Additionally, a formatting penalty is applied to encourage the model to generate lemmas before attempting the main theorem. As training progresses, problem difficulty, problem quality, and maximum output length are progressively increased. The training dataset comprises a combination of open-source datasets [1, 8, 12, 27, 28] and in-house formalized problems. For problems that are too difficult for single-pass generation, we use our proposer to generate easier problem variants and put these into the training dataset. We also exclude problems which are too easy (i.e. proof rate above 1/4) from RL training.

Unlike prior work [15, 21] that only utilize formal statements as prompts for RL training, our approach randomly incorporates natural language hints, natural language proofs, similar lemmas, proved lemmas, failed lemmas, failed attempts, summaries of previous attempts, and Lean compiler feedback into the prompt. This diverse prompting strategy enhances the model’s adaptability within our inference pipeline by enabling it to understand and utilize various types of input.

### 2.2.4 Test-Time Scaling

Here, we introduce our approach to test-time scaling of Seed-Prover. Depending on available inference budgets and problem difficulties, we developed three levels of strategies, which are illustrated in Figure 3 and Figure 4.

*Light* Previous work evaluated LLM theorem provers by Pass@ $k$ . We find that iteratively refining proofs using Lean compiler feedback [32] in conjunction with self-summarization can surpass the limits of single-pass inference token budgets and improve proof ability significantly. In the light setting, each proof attempt is refined up to 8–16 times and evaluated under Pass@8–16. We denote the sample budget of Pass@ $n$  and up to  $m$  refinements as  $n \times m$ , so the sample budget of the light setting is equivalent to generating the whole proof at Pass@64–256. This setting completes in 1–2 hours. Under this setting, Seed-Prover proves IMO 2022 P2 ( $MOHS = 15^1$ ), whereas without refinement, the same problem can only be proved in Pass@8192. We

&lt;sup>1&lt;/sup>MOHS is Math Olympiad Hardness Scale: &lt;https://web.evanchen.cc/upload/MOHS-hardness.pdf>. We note that the hardness scale for human contestants may not be well-aligned with the difficulty of proving it in Lean using an LLM.The diagram illustrates the workflow of the heavy inference setting. It begins with a 'Problem' box. An arrow points down to a large rounded rectangle labeled 'Proposer'. Inside this rectangle, there are two main stages of inference. The first stage, 'Light Inference', shows a row of conjectures (Conjecture 0, 1, 2, 3, ..., n) each with a 'Light Inference' box below it. An arrow labeled 'Select based on proof difficulty' points from this stage to a 'Medium Inference' stage. This stage shows a 'Problem' box followed by a row of lemmas (Lemma i, j, k). The second stage of 'Light Inference' shows another row of conjectures (Conjecture 10, 11, 12, 13, ..., 1n) with 'Light Inference' boxes. An arrow labeled 'Select based on proof difficulty' points from this stage to another 'Medium Inference' stage, which shows a 'Problem' box followed by a row of lemmas (Lemma 1i, 1j, 1k). The entire process is contained within a large rounded rectangle labeled 'Proposer'.

**Figure 4** The workflow of heavy inference setting.

observed two dominant behaviors of Seed-Prover in the light inference setting. First, it fixes Lean syntax errors in response to Lean compiler feedback. Second, it refines initial proof sketches, a process that might entirely alter the reasoning trajectory.

*Medium* Proofs for challenging competition problems are often lengthy and structurally complex. The medium test-time setting introduces both outer and inner refinement processes. The outer refinement process mirrors the light setting which refines the proof of the original main problem. The inner refinement process targets difficult lemmas that the outer refinement process generates but fails to prove, using a light setting with an  $8 \times 8$  budget to handle finer details. If any inner refinement successfully proves at least one lemma (indicating meaningful progress), the outer refinement process will update this information into the prompt and continue its refinement. Under this setting, Seed-Prover solves harder problems like IMO 2003 P6 ( $MOHS = 35$ ), IMO 2020 P5 ( $MOHS = 20$ ), IMO 2024 P1 ( $MOHS = 5$ ) and IMO 2025 P5 ( $MOHS = 15$ ), and final proofs potentially exceeding 1000 lines of code.

*Heavy* While the medium setting encourages reasoning in **depth** over proof details, it lacks the **breadth** needed to explore diverse properties of the given problem. Under the heavy inference setting, Seed-Prover begins with a conjecture pool and an empty lemma pool for the given problem. Initially, the proposer generates thousands of conjectures (by default 5000) to populate the conjecture pool. During inference, Seed-Prover tries to prove or disprove every conjecture in the conjecture pool using the light setting. Successfully proved conjectures are moved into the lemma pool. Seed-Prover leverages the lemma pool and Lean compiler feedback to refine the proof attempts. Additional conjectures are proposed based on proved lemmas. After days of thinking, the lemma pool accumulates several thousand nontrivial math facts. Each lemma is scored based on its proof rate, semantic relevance, and proof length. The proof rate serves as a strong indicator of lemma value; empirically, lemmas with low proof rate are often crucial to the final proof. Semantic relevance is assessed by an LLM judge. Unrelated lemmas or lemmas with short proof lengths are removed. We take hundreds of the top-ranked lemmas to help Seed-Prover finish the proof of the main problem using the medium inference setting. Seed-Prover has been trained to select and integrate these lemmas into a complete proof during RL. IMO 2017 P2 ( $MOHS = 40$ ), IMO 2025 P3 ( $MOHS = 25$ ) and IMO 2025 P4 ( $MOHS = 15$ ) are proved under the heavy inference setting.

### 3 Evaluation### 3.1 Seed-Geometry

Using Seed-Geometry’s backend, we performed large-scale problem generation. In particular, we took a similar approach to TongGeometry [30] by collecting data statistics of geometry problems over more than the past 20 years, and ran the problem generation program on the trees. In more than 7 days, the problem generation program found over 230 million unique problems, reaching 8x the search efficiency compared to the Python implementation. After necessary preprocessing using a pretrained byte-pair encoding [18], the dataset totaled 38B tokens. We trained both a policy model to complete the auxiliary objects given the context and a value model to estimate the number of steps remaining under the current state. The policy model was initialized from a pretrained Seed model and the value model was initialized with the trained policy model. However, in the experiments, we found that under extensive search, the value model could harm the general performance due to large errors in value estimation. We also compared generating auxiliary actions step-by-step with beam search and generating the whole auxiliary sequence in one go. Results from the latter were significantly inferior to the former. Therefore, in the final evaluation, we used step-by-step generation with beam search in a distributed setup, with each GPU process hosting a policy model for proposal generation.

Table 1 lists the performance of Seed-Geometry in IMO geometry problems from 2000 to 2024. Using the accounting method in IMO-AG-50, Seed-Geometry achieves 43 problem solves compared to AlphaGeometry 2, reaching 1 more solution. The problems that Seed-Geometry cannot solve but AlphaGeometry 2 does are not proof-based problems but rather computation-based problems, which AlphaGeometry 2 could potentially address using its algebraic engine. Table 2 lists the performance of our model in the much harder IMO shortlist problems from 2000 to 2022. The original benchmark of IMOSL-AG-30 was claimed to be established from the problems in the benchmark, but omitted many of the hard problems. Here, we include all hard-level problems in the shortlist and present the full results. As shown in the tables, AlphaGeometry 2 solved 19 of the 39 problems (with some unattempted) and our Seed-Geometry solved 22 of them. In addition, Seed-Geometry solved IMO 2025 P2 in 2 seconds after it received the human-provided problem formulation.

Based on the results provided, Seed-Geometry has established a new state-of-the-art in automated geometry problem solving, surpassing the performance of its predecessor, AlphaGeometry 2. In summary, by solving more problems in both the standard IMO and the more difficult IMO shortlist benchmarks, Seed-Geometry demonstrates a superior capability in handling complex, proof-based geometry challenges, setting a new performance standard in the field.

**Table 1** Performance comparison of AlphaGeometry 2 (AG2) and Seed-Geometry (SG) in IMO geometry problems from 2000 to 2024. Note that in IMO-AG-50, the 2002 P2, 2003 P4, 2004 P5, 2008 P1, and 2009 P4 are separated into two, whereas we merge each of them into one.

&lt;table border="1">
&lt;thead>
&lt;tr>
&lt;th>ID&lt;/th>
&lt;th>AG2&lt;/th>
&lt;th>SG&lt;/th>
&lt;th>ID&lt;/th>
&lt;th>AG2&lt;/th>
&lt;th>SG&lt;/th>
&lt;th>ID&lt;/th>
&lt;th>AG2&lt;/th>
&lt;th>SG&lt;/th>
&lt;/tr>
&lt;/thead>
&lt;tbody>
&lt;tr>
&lt;td>2000 P1&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2007 P4&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2015 P4&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;/tr>
&lt;tr>
&lt;td>2000 P6&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2008 P1&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2016 P1&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;/tr>
&lt;tr>
&lt;td>2001 P1&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;td>2008 P6&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2017 P4&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;/tr>
&lt;tr>
&lt;td>2001 P5&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;td>2009 P2&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2018 P1&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;/tr>
&lt;tr>
&lt;td>2002 P2&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2009 P4&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;td>2018 P6&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;td>✓&lt;/td>
&lt;/tr>
&lt;tr>
&lt;td>2002 P6&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;td>2010 P2&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2019 P2&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;/tr>
&lt;tr>
&lt;td>2003 P3&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;td>2010 P4&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2019 P6&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;/tr>
&lt;tr>
&lt;td>2003 P4&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2011 P6&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2020 P1&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;/tr>
&lt;tr>
&lt;td>2004 P1&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2012 P1&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2020 P6&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;/tr>
&lt;tr>
&lt;td>2004 P5&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2012 P5&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2021 P3&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;/tr>
&lt;tr>
&lt;td>2005 P1&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2013 P3&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2021 P4&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;/tr>
&lt;tr>
&lt;td>2005 P5&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2013 P4&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2022 P4&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;/tr>
&lt;tr>
&lt;td>2006 P1&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2014 P3&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2023 P2&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;/tr>
&lt;tr>
&lt;td>2006 P6&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;td>2014 P4&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2023 P6&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;td>✓&lt;/td>
&lt;/tr>
&lt;tr>
&lt;td>2007 P2&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2015 P3&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2024 P4&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;/tr>
&lt;/tbody>
&lt;/table>**Table 2** Performance comparison of AlphaGeometry 2 (AG2) and Seed-Geometry (SG) in IMO shortlist geometry problems from 2000 to 2022. Note that in IMOSL-AG-30, many geometry problems are ignored and here we fill in those missing geometry problems for comparison, with 2016 G7 merged into one. NA represents “not attempted” as the problems results were not directly reported in the original paper.

&lt;table border="1">
&lt;thead>
&lt;tr>
&lt;th>ID&lt;/th>
&lt;th>AG2&lt;/th>
&lt;th>SG&lt;/th>
&lt;th>ID&lt;/th>
&lt;th>AG2&lt;/th>
&lt;th>SG&lt;/th>
&lt;th>ID&lt;/th>
&lt;th>AG2&lt;/th>
&lt;th>SG&lt;/th>
&lt;/tr>
&lt;/thead>
&lt;tbody>
&lt;tr>
&lt;td>2002 G7&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2011 G3&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;td>2016 G6&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;/tr>
&lt;tr>
&lt;td>2002 G8&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2011 G4&lt;/td>
&lt;td>&lt;b>NA&lt;/b>&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2016 G7&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;/tr>
&lt;tr>
&lt;td>2003 G5&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2011 G5&lt;/td>
&lt;td>&lt;b>NA&lt;/b>&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2016 G8&lt;/td>
&lt;td>&lt;b>NA&lt;/b>&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;/tr>
&lt;tr>
&lt;td>2004 G7&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2011 G6&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;td>2017 G7&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;/tr>
&lt;tr>
&lt;td>2004 G8&lt;/td>
&lt;td>&lt;b>NA&lt;/b>&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2011 G7&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;td>2017 G8&lt;/td>
&lt;td>&lt;b>NA&lt;/b>&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;/tr>
&lt;tr>
&lt;td>2005 G5&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2012 G6&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2018 G7&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;/tr>
&lt;tr>
&lt;td>2005 G6&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2012 G7&lt;/td>
&lt;td>&lt;b>NA&lt;/b>&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;td>2019 G6&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;/tr>
&lt;tr>
&lt;td>2006 G9&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2012 G8&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2019 G8&lt;/td>
&lt;td>&lt;b>NA&lt;/b>&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;/tr>
&lt;tr>
&lt;td>2007 G8&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;td>2014 G7&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2020 G8&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;/tr>
&lt;tr>
&lt;td>2009 G6&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2015 G5&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2021 G8&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;/tr>
&lt;tr>
&lt;td>2009 G7&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;td>2015 G7&lt;/td>
&lt;td>&lt;b>NA&lt;/b>&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;td>2022 G6&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;/tr>
&lt;tr>
&lt;td>2009 G8&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;td>2015 G8&lt;/td>
&lt;td>&lt;b>NA&lt;/b>&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;td>2022 G7&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;/tr>
&lt;tr>
&lt;td>2010 G5&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2016 G5&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>✓&lt;/td>
&lt;td>2022 G8&lt;/td>
&lt;td>&lt;b>NA&lt;/b>&lt;/td>
&lt;td>&lt;b>X&lt;/b>&lt;/td>
&lt;/tr>
&lt;/tbody>
&lt;/table>

**Table 3** Performance comparison of Seed-Prover against previous systems across formal math tasks. The performance on PutnamBench is using the number of proved statements instead of percentage following previous works [20].

&lt;table border="1">
&lt;thead>
&lt;tr>
&lt;th>Metric&lt;/th>
&lt;th>Seed-Prover&lt;/th>
&lt;th>Previous SOTA&lt;/th>
&lt;/tr>
&lt;/thead>
&lt;tbody>
&lt;tr>
&lt;td>IMO 2025&lt;/td>
&lt;td>4/6 (Heavy, 5/6 post-competition)&lt;/td>
&lt;td>5/6 (Natural language, Gemini)&lt;/td>
&lt;/tr>
&lt;tr>
&lt;td>Past IMO&lt;/td>
&lt;td>78.1% (Heavy)&lt;/td>
&lt;td>—&lt;/td>
&lt;/tr>
&lt;tr>
&lt;td>MiniF2F-valid&lt;/td>
&lt;td>100.0% (Medium&lt;sup>1&lt;/sup>)&lt;/td>
&lt;td>90.6% (DeepSeek-Prover-V2 [15])&lt;/td>
&lt;/tr>
&lt;tr>
&lt;td>MiniF2F-test&lt;/td>
&lt;td>99.6% (Medium&lt;sup>2&lt;/sup>)&lt;/td>
&lt;td>92.2% (Kimina-Prover [21])&lt;/td>
&lt;/tr>
&lt;tr>
&lt;td>PutnamBench&lt;/td>
&lt;td>331/657 (Medium)&lt;/td>
&lt;td>86/657 (Goedel-Prover-V2 [9])&lt;/td>
&lt;/tr>
&lt;tr>
&lt;td>CombiBench&lt;/td>
&lt;td>30.0% (Medium)&lt;/td>
&lt;td>10.0% (Deepseek-Prover-V2 [15])&lt;/td>
&lt;/tr>
&lt;tr>
&lt;td>MiniCTX-v2&lt;/td>
&lt;td>81.8% (Light)&lt;/td>
&lt;td>44.3% (o4-mini [16])&lt;/td>
&lt;/tr>
&lt;/tbody>
&lt;/table>

&lt;sup>1&lt;/sup>One problem used Heavy. &lt;sup>2&lt;/sup>One problem failed under Heavy.

### 3.2 Seed-Prover

To evaluate the performance of Seed-Prover, we tested it on IMO 2025&lt;sup>2&lt;/sup>, past IMO problems, MiniF2F [31], PutnamBench [20], CombiBench [10], and MiniCTX-v2 [6] covering a wide range of mathematical domains. For PutnamBench and CombiBench, we first evaluate using the light setting and use the medium setting for unsolved problems. For IMO problems and MiniF2F, we also use the heavy setting for the remaining unsolved problems. The results are shown in Table 3. Unless otherwise specified, we use Lean v4.14.0 with its corresponding Mathlib version.

*IMO 2025* During the IMO 2025 contest, all problems were translated into formal statements by human experts. For fill-in-the-blank problems (“determine  $x$  such that ...”), initial solution candidates were generated by Seed1.6-Thinking before translation. We conducted searches for IMO 2025 Problems 1, 3, 4, and 5 using both the medium and heavy inference settings in parallel. As required by the IMO committee, all proof submissions were due by July 18th. Seed-Geometry solved Problem 2 instantly, and Seed-Prover derived the proof for Problem 5 under the medium inference setting, while proofs for the other three problems required the heavy inference setting. Notably, the proof for Problem 1 was finished after the deadline.

&lt;sup>2&lt;/sup>ByteDance was officially invited to participate in IMO 2025.*Past IMO* To evaluate our system’s performance on past IMO problems, we curated a dataset consisting of 155 past IMO problems. Most problems were adapted from Compfiles&lt;sup>3&lt;/sup> and MiniF2F [31]. Additionally, a subset of problems was manually added or corrected by human experts. For problems prior to 2017, we used light and medium settings. For problems after 2017, we use the heavy inference setting if the medium inference setting failed. Seed-Prover successfully proves 121/155 problems, achieving an overall success rate of 78.1%. By difficulty, Seed-Prover proves 47/55 easy problems (P1 or P4), 47/56 medium problems (P2 or P5), and 27/44 hard problems (P3 or P6). By subject area, it proves 72/85 algebra problems, 42/55 number theory problems, and 7/14 combinatorics problems. This demonstrates that the Seed-Prover’s performance at IMO 2025 reflects consistent capability on IMO problems across all years.

*MiniF2F* [31] Under the medium setting, we prove 99.6% problems on both MiniF2F-valid and MiniF2F-test. We used the heavy inference setting to tackle the last problem in both splits (i.e. IMO 1990 P3 and IMOSL 2007 Algebra P6). Seed-Prover successfully proved IMO 1990 P3 and failed on IMOSL 2007 Algebra P6. Interestingly, among the most challenging problems solved in MiniF2F are ones such as AMC12A 2021 P12, AMC12A 2021 P25, and AMC12A 2020 P9, which are relatively straightforward to reason about in natural language, but pose significant challenges when formalized in Lean. This difficulty arises primarily from obstacles in applying Vieta’s formulas or the non-triviality of counting roots.

*PutnamBench* [20] We evaluated Seed-Prover on PutnamBench using the light and medium inference settings. Under the light inference setting only, Seed-Prover proved 201/657 problems from PutnamBench. Using the medium inference setting improved this performance to 331/657 problems. This result shows a significant performance jump compared to previous works on undergraduate math problems.

*CombiBench* [10] Previous benchmarks have primarily focused on number theory and algebra problems. CombiBench is a benchmark specifically centered on combinatorial problems, where the problems often involve newly-defined concepts. Here, we evaluate Seed-Prover on CombiBench using the medium inference setting. Our model proves 30 out of 100 problems from CombiBench, outperforming previous work. Nonetheless, relative to other benchmarks, our model still struggles with proving combinatorics problems.

*MiniCTX-v2* [6] To test our system on a broader range of mathematical subjects from real-world formalization projects—including the ability to understand new definitions, notations, and lemmas—we evaluated Seed-Prover on MiniCTX-v2. This dataset includes context-rich problems from formalization repositories in subjects such as axiomatic systems, high-energy physics, analysis, and research-level number theory, all of which were written after Nov. 2024 to prevent data contamination. For evaluation purposes, we used the light inference setting under Lean v4.16.0. Our system successfully achieved 81.8% of MiniCTX-v2, which demonstrates its strong potential in real-world automated theorem proving, generalizing beyond standalone competition problems. For comparison, the baseline o4-mini solved 44.3% statements at Pass@8 [16].

## 4 Conclusion

In this work, we presented Seed-Geometry and Seed-Prover—two formal reasoning frameworks that integrate the capabilities of large language models. Both systems substantially outperform previous formal reasoning frameworks. Seed-Geometry accelerates verification and scales the search mechanism. Seed-Prover leverages iterative refinement and a three-tiered test-time inference strategy to achieve state-of-the-art. Notably, we successfully proved 5 out of 6 problems in IMO 2025, demonstrating the efficacy of these formal systems. Formal languages like Lean offer rapid proof verification, making them far more cost-effective than human experts and more reliable than LLM judges. Our future work will focus on combining formal systems with large language models to tackle open conjectures.

---

&lt;sup>3&lt;/sup>&lt;https://github.com/dwrensha/compfiles>## References

- [1] Alon Albalak, Duy Phung, Nathan Lile, Rafael Rafailov, Kanishk Gandhi, Louis Castricato, Anikait Singh, Chase Blagden, Violet Xiang, Dakota Mahan, and Nick Haber. Big-math: A large-scale, high-quality math dataset for reinforcement learning in language models, 2025. URL &lt;https://arxiv.org/abs/2502.17387>.
- [2] Yuri Chervonyi, Trieu H Trinh, Miroslav Olšák, Xiaomeng Yang, Hoang Nguyen, Marcelo Menegali, Junehyuk Jung, Vikas Verma, Quoc V Le, and Thang Luong. Gold-medalist performance in solving olympiad geometry with alphageometry2. *arXiv preprint arXiv:2502.03544*, 2025.
- [3] DeepMind. Ai solves imo problems at silver medal level. &lt;https://deepmind.google/discover/blog/ai-solves-imo-problems-at-silver-medal-level/>, 2024.
- [4] DeepSeek-AI. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning, 2025. URL &lt;https://arxiv.org/abs/2501.12948>.
- [5] Kefan Dong and Tengyu Ma. Stp: Self-play llm theorem provers with iterative conjecturing and proving, 2025. URL &lt;https://arxiv.org/abs/2502.00212>.
- [6] Jiewen Hu, Thomas Zhu, and Sean Welleck. miniCTX: Neural theorem proving with (long-)contexts. In *The Thirteenth International Conference on Learning Representations*, 2025. URL &lt;https://openreview.net/forum?id=KIgaAqEFHW>.
- [7] Albert Qiaochu Jiang, Sean Welleck, Jin Peng Zhou, Timothee Lacroix, Jiacheng Liu, Wenda Li, Mateja Jamnik, Guillaume Lample, and Yuhuai Wu. Draft, sketch, and prove: Guiding formal theorem provers with informal proofs. In *The Eleventh International Conference on Learning Representations*, 2023.
- [8] Jia Li, Edward Beeching, Lewis Tunstall, Ben Lipkin, Roman Soletskyi, Shengyi Costa Huang, Kashif Rasul, Longhui Yu, Albert Jiang, Ziju Shen, Zihan Qin, Bin Dong, Li Zhou, Yann Fleureau, Guillaume Lample, and Stanislas Polu. Numinamath. [&lt;https://github.com/project-numina/aimo-progress-prize>] ([https://github.com/project-numina/aimo-progress-prize/blob/main/report/numina\\_dataset.pdf](https://github.com/project-numina/aimo-progress-prize/blob/main/report/numina_dataset.pdf)), 2024.
- [9] Yong Lin, Shange Tang, Bohan Lyu, Jiayun Wu, Hongzhou Lin, Kaiyu Yang, Jia Li, Mengzhou Xia, Danqi Chen, Sanjeev Arora, et al. Goedel-prover: A frontier model for open-source automated theorem proving. *arXiv preprint arXiv:2502.07640*, 2025.
- [10] Junqi Liu, Xiaohan Lin, Jonas Bayer, Yael Dillies, Weijie Jiang, Xiaodan Liang, Roman Soletskyi, Haiming Wang, Yunzhou Xie, Beibei Xiong, et al. Combibench: Benchmarking llm capability for combinatorial mathematics. *arXiv preprint arXiv:2505.03171*, 2025.
- [11] OpenAI. Openai o1 system card, 2024. URL &lt;https://arxiv.org/abs/2412.16720>.
- [12] Zhongyuan Peng, Yifan Yao, Kaijing Ma, Shuyue Guo, Yizhe Li, Yichi Zhang, Chenchen Zhang, Yifan Zhang, Zhouliang Yu, Luming Li, et al. Criticlean: Critic-guided reinforcement learning for mathematical formalization. *arXiv preprint arXiv:2507.06181*, 2025.
- [13] Ivo Petrov, Jasper Dekoninck, Lyuben Baltadzhiev, Maria Drencheva, Kristian Minchev, Mislav Balunović, Nikola Jovanović, and Martin Vechev. Proof or bluff? evaluating llms on 2025 usa math olympiad, 2025. URL &lt;https://arxiv.org/abs/2503.21934>.
- [14] Stanislas Polu, Jesse Michael Han, Kunhao Zheng, Mantas Baksys, Igor Babuschkin, and Ilya Sutskever. Formal mathematics statement curriculum learning. *arXiv preprint arXiv:2202.01344*, 2022.
- [15] ZZ Ren, Zhihong Shao, Junxiao Song, Huajian Xin, Haocheng Wang, Wanjia Zhao, Liyue Zhang, Zhe Fu, Qihao Zhu, Dejian Yang, et al. Deepseek-prover-v2: Advancing formal mathematical reasoning via reinforcement learning for subgoal decomposition. *arXiv preprint arXiv:2504.21801*, 2025.
- [16] Tate Rowney, Jiewen Hu, Thomas Zhu, and Sean Welleck. miniCTX leaderboard. &lt;https://cmu-l3.github.io/minictx/leaderboard.html>, 2025. Accessed July 28, 2025.
- [17] ByteDance Seed, Jiaze Chen, Tiantian Fan, Xin Liu, Lingjun Liu, Zhiqi Lin, Mingxuan Wang, Chengyi Wang, Xiangpeng Wei, Wenyuan Xu, et al. Seed1.5-thinking: Advancing superb reasoning models with reinforcement learning. *arXiv preprint arXiv:2504.13914*, 2025.
- [18] Rico Sennrich, Barry Haddow, and Alexandra Birch. Neural machine translation of rare words with subword units. *arXiv preprint arXiv:1508.07909*, 2015.- [19] Trieu H Trinh, Yuhuai Wu, Quoc V Le, He He, and Thang Luong. Solving olympiad geometry without human demonstrations. *Nature*, 625(7995):476–482, 2024.
- [20] George Tsoukalas, Jasper Lee, John Jennings, Jimmy Xin, Michelle Ding, Michael Jennings, Amitayush Thakur, and Swarat Chaudhuri. Putnambench: Evaluating neural theorem-provers on the putnam mathematical competition. In *The Thirty-eighth Conference on Neural Information Processing Systems Datasets and Benchmarks Track*.
- [21] Haiming Wang, Mert Unsal, Xiaohan Lin, Mantas Baksys, Junqi Liu, Marco Dos Santos, Flood Sung, Marina Vinyes, Zhenzhe Ying, Zekai Zhu, Jianqiao Lu, Hugues de Saxcé, Bolton Bailey, Chendong Song, Chenjun Xiao, Dehao Zhang, Ebony Zhang, Frederick Pu, Han Zhu, Jiawei Liu, Jonas Bayer, Julien Michel, Longhui Yu, Léo Dreyfus-Schmidt, Lewis Tunstall, Luigi Pagani, Moreira Machado, Pauline Bourigault, Ran Wang, Stanislas Polu, Thibaut Barroyer, Wen-Ding Li, Yazhe Niu, Yann Fleureau, Yangyang Hu, Zhouliang Yu, Zihan Wang, Zhilin Yang, Zhengying Liu, and Jia Li. Kimina-prover preview: Towards large formal reasoning models with reinforcement learning. 2025. URL &lt;http://arxiv.org/abs/2504.11354>.
- [22] Zijian Wu, Suozhi Huang, Zhejian Zhou, Huaiyuan Ying, Jiayu Wang, Dahua Lin, and Kai Chen. Internlm2.5-stepprover: Advancing automated theorem proving via expert iteration on large-scale lean problems, 2024. URL &lt;https://arxiv.org/abs/2410.15700>.
- [23] Zijian Wu, Jiayu Wang, Dahua Lin, and Kai Chen. Lean-github: Compiling github lean repositories for a versatile lean prover, 2024. URL &lt;https://arxiv.org/abs/2407.17227>.
- [24] Huajian Xin, Z.Z. Ren, Junxiao Song, Zihong Shao, Wanjia Zhao, Haocheng Wang, Bo Liu, Liyue Zhang, Xuan Lu, Qiushi Du, Wenjun Gao, Haowei Zhang, Qihao Zhu, Dejian Yang, Zhibin Gou, Z.F. Wu, Fuli Luo, and Chong Ruan. Deepseek-prover-v1.5: Harnessing proof assistant feedback for reinforcement learning and monte-carlo tree search. In *The Thirteenth International Conference on Learning Representations*, 2025. URL &lt;https://openreview.net/forum?id=I4YAIwrsXa>.
- [25] Ran Xin, Chenguang Xi, Jie Yang, Feng Chen, Hang Wu, Xia Xiao, Yifan Sun, Shen Zheng, and Kai Shen. Bfs-prover: Scalable best-first tree search for llm-based automatic theorem proving, 2025. URL &lt;https://arxiv.org/abs/2502.03438>.
- [26] Kaiyu Yang, Aidan Swope, Alex Gu, Rahul Chalamala, Peiyang Song, Shixing Yu, Saad Godil, Ryan J Prenger, and Animashree Anandkumar. Leandojo: Theorem proving with retrieval-augmented language models. *Advances in Neural Information Processing Systems*, 36:21573–21612, 2023.
- [27] Huaiyuan Ying, Zijian Wu, Yihan Geng, Jiayu Wang, Dahua Lin, and Kai Chen. Lean workbook: A large-scale lean problem set formalized from natural language math problems. In *The Thirty-eighth Conference on Neural Information Processing Systems Datasets and Benchmarks Track*.
- [28] Qiyong Yu, Zheng Zhang, Ruofei Zhu, Yufeng Yuan, Xiaochen Zuo, Yu Yue, Weinan Dai, Tiantian Fan, Gaohong Liu, Lingjun Liu, et al. Dapo: An open-source llm reinforcement learning system at scale. *arXiv preprint arXiv:2503.14476*, 2025.
- [29] Yu Yue, Yufeng Yuan, Qiyong Yu, Xiaochen Zuo, Ruofei Zhu, Wenyuan Xu, Jiaze Chen, Chengyi Wang, TianTian Fan, Zhengyin Du, Xiangpeng Wei, Xiangyu Yu, Gaohong Liu, Juncai Liu, Lingjun Liu, Haibin Lin, Zhiqi Lin, Bole Ma, Chi Zhang, Mofan Zhang, Wang Zhang, Hang Zhu, Ru Zhang, Xin Liu, Mingxuan Wang, Yonghui Wu, and Lin Yan. Vapo: Efficient and reliable reinforcement learning for advanced reasoning tasks, 2025. URL &lt;https://arxiv.org/abs/2504.05118>.
- [30] Chi Zhang, Jiajun Song, Siyu Li, Yitao Liang, Yuxi Ma, Wei Wang, Yixin Zhu, and Song-Chun Zhu. Proposing and solving olympiad geometry with guided tree search. *arXiv preprint arXiv:2412.10673*, 2024.
- [31] Kunhao Zheng, Jesse Michael Han, and Stanislas Polu. minif2f: a cross-system benchmark for formal olympiad-level mathematics. In *International Conference on Learning Representations*.
- [32] Yichi Zhou, Jianqiu Zhao, Yongxin Zhang, Bohan Wang, Siran Wang, Luoxin Chen, Jiahui Wang, Haowei Chen, Allan Jie, Xinbo Zhang, et al. Solving formal math problems by decomposition and iterative reflection. *arXiv preprint arXiv:2507.15225*, 2025.# Appendix

## A Contributors

The names are sorted alphabetically. An asterisk \* indicates a member who left Seed.

*Algorithm* Luoxin Chen, Liankai Huang, Zhicheng Jiang, Allan Jie, Xiaoran Jin, Xing Jin, Chenggang Li, Wenlei Shi, Jiahui Wang, Siran Wang, Chenrui Wei, Shufa Wei, Yonghui Wu, Huajian Xin, Fan Yang, Hongyi Yuan, Zheng Yuan, Tianyang Zhan, Chi Zhang, Yue Zhang\*, Yichi Zhou, Thomas Hanwen Zhu

*Data* Jinming Gu, Wenhao Huang, Zhicheng Jiang, Xiaoran Jin, Kaijing Ma, Jiawei Shen, Tong Sun, Chenrui Wei, Shufa Wei, Yuchen Wu, Yihang Xia, Huaiyuan Ying\*, Zheng Yuan, Ge Zhang

*Infra* Cheng Ren, He Sun, Zhihong Wang, Tianyun Zhao\*, Jianqiu Zhao, Thomas Hanwen Zhu

## B LooKeng: An Easy-to-Use and Effective Python Interface for Lean

Interacting with Lean poses significant challenges that limit the flexibility of Lean-based workflows. The most popular interface, LeanDojo [26], only supports earlier versions of Lean 4, restricting users from accessing Lean’s newest updates. Furthermore, LeanDojo requires creating a Lean repository for interaction, which makes it impractical to use considering the massive scale of Lean interaction during model development and inference. To address these issues, we introduce LooKeng, a REPL&lt;sup>4&lt;/sup>-based Python interface designed to simplify and accelerate the interaction process. LooKeng offers powerful features for developers while providing a user-friendly interface for end-users. The core functionality of LooKeng includes ‘init\_state’, ‘run\_tac’, and ‘verify\_proof’. One can use LooKeng to interact with Lean step-by-step or verify an entire proof directly. The key features of LooKeng are summarized as follows:

- • **Stateless Design:** A Lean state can be simultaneously processed using different LooKeng instances, enabling effortless scaling and sharing.
- • **Complex Tactics:** Complex tactics such as `apply?` and `all_goals` are fully supported, with enhanced infotree integration to prevent false positive proofs.
- • **Version-Free:** The LooKeng CLI allows users to manage and switch between different Lean versions.
- • **Memory Control:** Users can easily track the memory consumption of the Lean backend, set custom thresholds, and automatically terminate processes when memory usage exceeds the limit.
- • **Proof Verification:** LooKeng provides a straightforward method, ‘verify\_proof’, to rigorously verify the final proof using the native Lean interface, ensuring correctness and reliability.
- • **Proof Simplification:** LooKeng can remove useless tactics and hypothesis in the proof to obtain a simpler proof.
- • **Statement Negation:** LooKeng is able to generate the negated statement of a statement.
- • **Multi-Concurrency Support:** LooKeng can run as a service, handling thousands of concurrent requests via async architecture and resource isolation.

---

&lt;sup>4&lt;/sup>&lt;https://github.com/leanprover-community/repl>

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e63e546-a34a-48e5-a9db-d65717b10735",
  "isSidechain": false,
  "promptId": "90291295-f415-450f-a2ae-7009e730e84a",
  "type": "user",
  "uuid": "f15701c1-a352-4ca8-ab6e-54926140e157",
  "toolUseResult": {
    "bytes": 47007,
    "code": 200,
    "codeText": "OK",
    "result": "# Seed-Prover: Deep and Broad Reasoning for Automated Theorem Proving\n\nByteDance Seed AI4Math\n\n## Abstract\n\nLLMs have demonstrated strong mathematical reasoning abilities by leveraging reinforcement learning with long chain-of-thought, yet they continue to struggle with theorem proving due to the lack of clear supervision signals when solely using natural language. Dedicated domain-specific languages like Lean provide clear supervision via formal verification of proofs, enabling effective training through reinforcement learning. In this work, we propose **Seed-Prover**, a lemma-style whole-proof reasoning model. Seed-Prover can iteratively refine its proof based on Lean feedback, proved lemmas, and self-summarization. To solve IMO-level contest problems, we design three test-time inference strategies that enable both deep and broad reasoning. Seed-Prover proves 78.1% of formalized past IMO problems, saturates MiniF2F, and achieves over 50% on PutnamBench, outperforming the previous state-of-the-art by a large margin. To address the lack of geometry support in Lean, we introduce a geometry reasoning engine **Seed-Geometry**, which outperforms previous formal geometry engines. We use these two systems to participate in IMO 2025 and fully prove 5 out of 6 problems. This work represents a significant advancement in automated mathematical reasoning, demonstrating the effectiveness of formal verification with long chain-of-thought reasoning.\n\nProject Page: &lt;https://github.com/ByteDance-Seed/Seed-Prover>\n\nFigure 1 Growth in MiniF2F-Test performance over time.# 1 Introduction\n\nRecent advances in large language models (LLMs) have shown extending reasoning lengths through natural language can significantly boost performance on math benchmarks such as MATH and AIME [4, 11]. Training such models requires reinforcement learning (RL) on verifiable answers. It is extremely difficult to automatically, or even manually, verify a proof in natural language since each step must be carefully checked for correctness [13]. This poses significant challenges for applying reinforcement learning to the training of large language models to prove mathematical statements. Unlike natural language, formal languages such as Lean can provide a clear and automatic signal on the correctness of a formalized proof. A noteworthy work from AlphaProof [3] uses Lean to successfully solve 3 problems from the 2024 International Mathematical Olympiad (IMO). AlphaProof demonstrates that LLMs using formal language are capable of proving very challenging problems that LLMs using natural language fail to prove.\n\nThere are two types of LLM formal provers, step-level provers [3, 14, 22, 23, 25] and whole-proof generation provers [5, 24]. Step-level provers incrementally generate Lean code line-by-line. While this enables close interaction with the Lean environment, it requires special scaffolding to generate a complete Lean proof, and the interaction is often too granular to allow high-level reasoning. In contrast, whole-proof models generate an entire Lean proof at once, but typically lack interaction with the Lean compiler. Recent work has shown that combining whole-proof models with long chain-of-thought reasoning [9, 15, 21] substantially outperforms step-level provers. In this work, we propose **Seed-Prover**, a whole-proof model with following features:\n\n- • **Lemma-Style Proving:** Seed-Prover tries to generate useful intermediate lemmas before proving the main statement. These lemmas serve as shared knowledge across different inference paths.\n- • **Iterative Proof Refinement:** Seed-Prover iteratively refines its proof based on Lean compiler feedback, previous proved lemmas, and self-summarization.\n- • **Test-Time Scaling:** We implement a three-tiered inference strategy that enables Seed-Prover to think both deeply and broadly—allocating thinking budget to fine details while exploring interesting properties.\n- • **SOTA Performance:** Seed-Prover proves 5 out of 6 problems in IMO 2025, saturates MiniF2F [31] (shown in Figure 1), and outperforms prior work by up to  $3\\times$  on multiple formal benchmarks.\n\nDue to the lack of sufficient geometry support in Lean, Seed-Prover incorporates a dedicated geometry reasoning engine **Seed-Geometry**. Similar to existing line of efforts in AlphaGeometry [2, 19] and TongGeometry [30], Seed-Geometry follows the forward-chaining design in the reasoning engine implementation, where the system derives all known facts by checking applicable rules until closure is reached. By backward-tracing fact dependencies, Seed-Geometry identifies the minimum dependency relations in a geometry problem’s configuration, separating the problem context from the auxiliary constructions necessary to prove a problem. Using statistics derived from more than past 20 years of math olympiad competitions, Seed-Geometry performs extensive search in the geometry space defined by its dedicated domain-specific language and establishes a repository of 230 million unique geometry problems requiring auxiliaries. A Seed model trained on such dedicated geometry data becomes an exceptionally effective neuro-symbolic geometry prover, where it fills in the missing auxiliary geometry elements and the geometry reasoning engine performs step-by-step forward-chaining, completing the final proof of a problem. In experiments, Seed-Geometry solves 43 of the IMO-AG-50 (*vs.* 42 by AlphaGeometry 2), a benchmark that curates geometry problems of IMO from 2000 to 2024. It also sets a new state-of-the-art on the IMO shortlist geometry problems from 2000 to 2022, and notably solves the geometry problem of IMO 2025 under just 2 seconds.\n\n## 2 Approach\n\nHere we introduce the two systems we used in IMO 2025, Seed-Geometry and Seed-Prover.\n\n### 2.1 Seed-Geometry\n\nSeed-Geometry builds on the success of TongGeometry [30] and performs a major redesign. From a global perspective, both systems leverage trained neural models to complete missing auxiliary constructions andspecialized reasoning engines to forward-chain derivation. However, Seed-Geometry is a substantial upgrade over TongGeometry in the following aspects.\n\n### 2.1.1 Extended Domain-Specific Language\n\nSeed-Geometry constructs geometric diagrams in the principle of ruler-and-compass construction. However, plain ruler-and-compass construction steps can be long and cumbersome, making the language representation of the constructions overly verbose, introducing unnecessary burden on both the neural processing of Transformer-based large language model and the symbolic derivation of the backend engine. To mitigate these issues, Seed-Geometry groups particular action sequences into specific actions, making the representation of the problem concise enough. Of particular note, Seed-Geometry has several such composite actions: isogonal conjugate with respect to a triangle and a point, exsimilitude center of two circles, insimilitude center of two circles. All three actions can be represented with primitive ruler-and-compass actions; yet the construction sequence in itself is non-trivial and unnecessarily clumsy.\n\n### 2.1.2 Extremely Fast Reasoning Engine\n\nSeed-Geometry improved its reasoning engine’s performance by rewriting its backend in C++ and making it accessible to Python users through Pybind11. This change led to roughly 100-fold speed increase compared to the Python implementation in TongGeometry. The C++ implementation handles memory more efficiently and benefits from compiler optimizations, allowing for much faster **deep** searches within the reasoning engine. This is particularly crucial because the engine’s forward-chaining design typically slows down considerably when the search tree expands widely at deeper levels.\n\n### 2.1.3 Exceptional Large Language Model\n\nSeed-Geometry utilizes a high-performing large language model from the Seed family [17]. This particular Seed model has undergone extensive pre-training on vast datasets of coding and mathematics, granting it a wide array of specialized skills. The specific model size was chosen considering the number of data tokens. We considered training two models in an actor–critic setup initially: the policy model that proposed possible next auxiliary element to construct and a value model that predicted the number of steps to go from the state. However, we note from preliminary experiments that a single Seed model serving as the policy would suffice, contradicting the design of both a policy model and a value model in existing work [30]. We also note that a policy model unspecialized to the specific goal makes both training and solving more manageable and therefore, we only trained the model on pairs of problem context and auxiliaries, without the target fact goal in the prompt.\n\n### 2.1.4 Extensive Search\n\nWhen presented with a new problem, Seed-Geometry first transforms the representation into a canonical form. If the reasoning backend successfully finds the goal fact to prove in the reasoning process, the problem is considered immediately solved. Otherwise, Seed-Geometry initiates a search process. In particular, Seed-Geometry employs beam search, with the policy model generating proposals for each beam in the buffer. With the extremely fast reasoning engine, Seed-Geometry supports running each new generated proposal in time. If any one of the proposal leads to the proof, the problem is considered proven; otherwise we select the top few proposals for the next step of expansion in the search tree based on each proposal’s cumulative negative log likelihood. The search process terminates until a fixed number of steps have been consumed. Seed-Geometry’s search process is made efficient and scalable. Compared to TongGeometry, Seed-Geometry’s solving process supports a distributed setup where each GPU process communicates with each other and blocked only at the beam selection point. Each GPU process is also equipped with a CPU thread pool that asynchronously executes the reasoning step during language model inference such that the reasoning cost can be overlapped with language model inference.&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Whole proof&lt;/th>\n&lt;th>Lemma-style&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>\n&lt;pre>\ntheorem eg : 1 + 2 = 3 := by\n  have h0 : 1 + 1 = 2 := by\n    ring\n\n  have h1 : 1 + (1 + 1) = 3 := by\n    ring\n\n  linarith [h0, h1]\n\n#print axioms eg\n&lt;/pre>\n&lt;/td>\n&lt;td>\n&lt;pre>\nlemma round1_h0 : 1 + 1 = 2 := by\n  ring\n\nlemma round1_h1 : 1 + (1 + 1) = 3 := by\n  ring\n\ntheorem eg : 1 + 2 = 3 := by\n  linarith [round1_h0, round1_h1]\n\n#print axioms eg\n&lt;/pre>\n&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nFigure 2 An example of whole proof and lemma-style proof in Lean 4.\n\n## 2.2 Seed-Prover\n\nSeed-Prover is a large language model specialized in formal reasoning in Lean 4. Its most significant distinction from prior work lies in its adoption of lemma-style proving as the proof paradigm, which places **lemmas** at the center of the reasoning process. This approach offers several key advantages: it enables clear identification of lemmas that have and have not been proved, indicating the progress made in solving the main problem; lemmas can be processed independently and combined freely; lemmas from different inference trajectories can be combined to address more challenging problems. Both the training and inference procedures of Seed-Prover are designed around lemmas.\n\n### 2.2.1 Lemma-Style Proving\n\nPrevious works [9, 15, 21] trained the model to generate whole proofs starting with the keyword *theorem*. In contrast, we first require the model to generate some useful lemmas—each introduced by the keyword *lemma*—before generating the main proof using *theorem* by applying the generated lemmas. An example is shown in Figure 2. This lemma-style proof provides following merits. First, it allows clear identification of the lemmas that have been successfully proved, and those that need further refinement. Second, lemmas are modular—they can be compiled independently, stored independently, and combined freely. Additionally, proofs of lemmas may provide inspiration to the model for proving unproved lemmas and the main problem. To enable this workflow, we establish a lemma pool for each difficult problem, which stores comprehensive data from all our inference runs, including lemma statements, lemma names, complete proofs, proof difficulties, and dependency relations. The lemma pool is typically used to (1) retrieve the most relevant lemmas by name or formal statement; (2) sample the most difficult lemmas according to their proof difficulty.\n\n### 2.2.2 Conjecture Proposing\n\nWhen tackling challenging contest-level math problems, human contestants often identify interesting properties of the problem and use them to guide their reasoning. Seed-Prover is trained to propose such potentially useful properties by chain-of-thought reasoning. Notably, this process differs from chain-of-thought reasoning to solve the problem directly; rather, it emphasizes broad exploration of the problem space without committing to a particular approach. Take functional equations as an example: one might conjecture that the function is *injective*, *surjective*, *bijective*, *monotonic*, or *periodic*—all without engaging in deep, targeted reasoning about the problem itself. In a sense, many useful properties of a problem may be enumerated before full problem resolution. The proposer module accepts an unsolved problem and, optionally, some already proved lemmas as input, and generates 10–50 candidate conjectures about properties of the problem. Proposing multiple conjectures in parallel significantly increases diversity and the likelihood of covering the valuable properties. For each problem, we may repeat this process multiple times to create a large conjecture pool.\n\nThis approach differs from Draft, Sketch, Prove [7], which presumes the ability to fully solve the problem upfront. In contrast, our method performs broad exploratory searches over the problem space enabling**Figure 3** The workflows of single-pass whole proof generation, light, and medium inference settings.\n\ndiscovery of useful properties, which makes it possible to solve problems that the model cannot solve directly in natural language.\n\n### 2.2.3 Training\n\nTo enable seamless interaction between Seed-Prover and Lean, we adopt multi-stage, multi-task reinforcement learning (RL) based on VAPO [29]. The RL reward is 1 if the formal statement is successfully proven, and 0 otherwise. Additionally, a formatting penalty is applied to encourage the model to generate lemmas before attempting the main theorem. As training progresses, problem difficulty, problem quality, and maximum output length are progressively increased. The training dataset comprises a combination of open-source datasets [1, 8, 12, 27, 28] and in-house formalized problems. For problems that are too difficult for single-pass generation, we use our proposer to generate easier problem variants and put these into the training dataset. We also exclude problems which are too easy (i.e. proof rate above 1/4) from RL training.\n\nUnlike prior work [15, 21] that only utilize formal statements as prompts for RL training, our approach randomly incorporates natural language hints, natural language proofs, similar lemmas, proved lemmas, failed lemmas, failed attempts, summaries of previous attempts, and Lean compiler feedback into the prompt. This diverse prompting strategy enhances the model’s adaptability within our inference pipeline by enabling it to understand and utilize various types of input.\n\n### 2.2.4 Test-Time Scaling\n\nHere, we introduce our approach to test-time scaling of Seed-Prover. Depending on available inference budgets and problem difficulties, we developed three levels of strategies, which are illustrated in Figure 3 and Figure 4.\n\n*Light* Previous work evaluated LLM theorem provers by Pass@ $k$ . We find that iteratively refining proofs using Lean compiler feedback [32] in conjunction with self-summarization can surpass the limits of single-pass inference token budgets and improve proof ability significantly. In the light setting, each proof attempt is refined up to 8–16 times and evaluated under Pass@8–16. We denote the sample budget of Pass@ $n$  and up to  $m$  refinements as  $n \\times m$ , so the sample budget of the light setting is equivalent to generating the whole proof at Pass@64–256. This setting completes in 1–2 hours. Under this setting, Seed-Prover proves IMO 2022 P2 ( $MOHS = 15^1$ ), whereas without refinement, the same problem can only be proved in Pass@8192. We\n\n&lt;sup>1&lt;/sup>MOHS is Math Olympiad Hardness Scale: &lt;https://web.evanchen.cc/upload/MOHS-hardness.pdf>. We note that the hardness scale for human contestants may not be well-aligned with the difficulty of proving it in Lean using an LLM.The diagram illustrates the workflow of the heavy inference setting. It begins with a 'Problem' box. An arrow points down to a large rounded rectangle labeled 'Proposer'. Inside this rectangle, there are two main stages of inference. The first stage, 'Light Inference', shows a row of conjectures (Conjecture 0, 1, 2, 3, ..., n) each with a 'Light Inference' box below it. An arrow labeled 'Select based on proof difficulty' points from this stage to a 'Medium Inference' stage. This stage shows a 'Problem' box followed by a row of lemmas (Lemma i, j, k). The second stage of 'Light Inference' shows another row of conjectures (Conjecture 10, 11, 12, 13, ..., 1n) with 'Light Inference' boxes. An arrow labeled 'Select based on proof difficulty' points from this stage to another 'Medium Inference' stage, which shows a 'Problem' box followed by a row of lemmas (Lemma 1i, 1j, 1k). The entire process is contained within a large rounded rectangle labeled 'Proposer'.\n\n**Figure 4** The workflow of heavy inference setting.\n\nobserved two dominant behaviors of Seed-Prover in the light inference setting. First, it fixes Lean syntax errors in response to Lean compiler feedback. Second, it refines initial proof sketches, a process that might entirely alter the reasoning trajectory.\n\n*Medium* Proofs for challenging competition problems are often lengthy and structurally complex. The medium test-time setting introduces both outer and inner refinement processes. The outer refinement process mirrors the light setting which refines the proof of the original main problem. The inner refinement process targets difficult lemmas that the outer refinement process generates but fails to prove, using a light setting with an  $8 \\times 8$  budget to handle finer details. If any inner refinement successfully proves at least one lemma (indicating meaningful progress), the outer refinement process will update this information into the prompt and continue its refinement. Under this setting, Seed-Prover solves harder problems like IMO 2003 P6 ( $MOHS = 35$ ), IMO 2020 P5 ( $MOHS = 20$ ), IMO 2024 P1 ( $MOHS = 5$ ) and IMO 2025 P5 ( $MOHS = 15$ ), and final proofs potentially exceeding 1000 lines of code.\n\n*Heavy* While the medium setting encourages reasoning in **depth** over proof details, it lacks the **breadth** needed to explore diverse properties of the given problem. Under the heavy inference setting, Seed-Prover begins with a conjecture pool and an empty lemma pool for the given problem. Initially, the proposer generates thousands of conjectures (by default 5000) to populate the conjecture pool. During inference, Seed-Prover tries to prove or disprove every conjecture in the conjecture pool using the light setting. Successfully proved conjectures are moved into the lemma pool. Seed-Prover leverages the lemma pool and Lean compiler feedback to refine the proof attempts. Additional conjectures are proposed based on proved lemmas. After days of thinking, the lemma pool accumulates several thousand nontrivial math facts. Each lemma is scored based on its proof rate, semantic relevance, and proof length. The proof rate serves as a strong indicator of lemma value; empirically, lemmas with low proof rate are often crucial to the final proof. Semantic relevance is assessed by an LLM judge. Unrelated lemmas or lemmas with short proof lengths are removed. We take hundreds of the top-ranked lemmas to help Seed-Prover finish the proof of the main problem using the medium inference setting. Seed-Prover has been trained to select and integrate these lemmas into a complete proof during RL. IMO 2017 P2 ( $MOHS = 40$ ), IMO 2025 P3 ( $MOHS = 25$ ) and IMO 2025 P4 ( $MOHS = 15$ ) are proved under the heavy inference setting.\n\n### 3 Evaluation### 3.1 Seed-Geometry\n\nUsing Seed-Geometry’s backend, we performed large-scale problem generation. In particular, we took a similar approach to TongGeometry [30] by collecting data statistics of geometry problems over more than the past 20 years, and ran the problem generation program on the trees. In more than 7 days, the problem generation program found over 230 million unique problems, reaching 8x the search efficiency compared to the Python implementation. After necessary preprocessing using a pretrained byte-pair encoding [18], the dataset totaled 38B tokens. We trained both a policy model to complete the auxiliary objects given the context and a value model to estimate the number of steps remaining under the current state. The policy model was initialized from a pretrained Seed model and the value model was initialized with the trained policy model. However, in the experiments, we found that under extensive search, the value model could harm the general performance due to large errors in value estimation. We also compared generating auxiliary actions step-by-step with beam search and generating the whole auxiliary sequence in one go. Results from the latter were significantly inferior to the former. Therefore, in the final evaluation, we used step-by-step generation with beam search in a distributed setup, with each GPU process hosting a policy model for proposal generation.\n\nTable 1 lists the performance of Seed-Geometry in IMO geometry problems from 2000 to 2024. Using the accounting method in IMO-AG-50, Seed-Geometry achieves 43 problem solves compared to AlphaGeometry 2, reaching 1 more solution. The problems that Seed-Geometry cannot solve but AlphaGeometry 2 does are not proof-based problems but rather computation-based problems, which AlphaGeometry 2 could potentially address using its algebraic engine. Table 2 lists the performance of our model in the much harder IMO shortlist problems from 2000 to 2022. The original benchmark of IMOSL-AG-30 was claimed to be established from the problems in the benchmark, but omitted many of the hard problems. Here, we include all hard-level problems in the shortlist and present the full results. As shown in the tables, AlphaGeometry 2 solved 19 of the 39 problems (with some unattempted) and our Seed-Geometry solved 22 of them. In addition, Seed-Geometry solved IMO 2025 P2 in 2 seconds after it received the human-provided problem formulation.\n\nBased on the results provided, Seed-Geometry has established a new state-of-the-art in automated geometry problem solving, surpassing the performance of its predecessor, AlphaGeometry 2. In summary, by solving more problems in both the standard IMO and the more difficult IMO shortlist benchmarks, Seed-Geometry demonstrates a superior capability in handling complex, proof-based geometry challenges, setting a new performance standard in the field.\n\n**Table 1** Performance comparison of AlphaGeometry 2 (AG2) and Seed-Geometry (SG) in IMO geometry problems from 2000 to 2024. Note that in IMO-AG-50, the 2002 P2, 2003 P4, 2004 P5, 2008 P1, and 2009 P4 are separated into two, whereas we merge each of them into one.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>ID&lt;/th>\n&lt;th>AG2&lt;/th>\n&lt;th>SG&lt;/th>\n&lt;th>ID&lt;/th>\n&lt;th>AG2&lt;/th>\n&lt;th>SG&lt;/th>\n&lt;th>ID&lt;/th>\n&lt;th>AG2&lt;/th>\n&lt;th>SG&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>2000 P1&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2007 P4&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2015 P4&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>2000 P6&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2008 P1&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2016 P1&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>2001 P1&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;td>2008 P6&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2017 P4&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>2001 P5&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;td>2009 P2&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2018 P1&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>2002 P2&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2009 P4&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;td>2018 P6&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>2002 P6&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;td>2010 P2&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2019 P2&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>2003 P3&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;td>2010 P4&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2019 P6&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>2003 P4&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2011 P6&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2020 P1&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>2004 P1&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2012 P1&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2020 P6&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>2004 P5&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2012 P5&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2021 P3&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>2005 P1&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2013 P3&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2021 P4&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>2005 P5&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2013 P4&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2022 P4&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>2006 P1&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2014 P3&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2023 P2&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>2006 P6&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;td>2014 P4&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2023 P6&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>2007 P2&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2015 P3&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2024 P4&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>**Table 2** Performance comparison of AlphaGeometry 2 (AG2) and Seed-Geometry (SG) in IMO shortlist geometry problems from 2000 to 2022. Note that in IMOSL-AG-30, many geometry problems are ignored and here we fill in those missing geometry problems for comparison, with 2016 G7 merged into one. NA represents “not attempted” as the problems results were not directly reported in the original paper.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>ID&lt;/th>\n&lt;th>AG2&lt;/th>\n&lt;th>SG&lt;/th>\n&lt;th>ID&lt;/th>\n&lt;th>AG2&lt;/th>\n&lt;th>SG&lt;/th>\n&lt;th>ID&lt;/th>\n&lt;th>AG2&lt;/th>\n&lt;th>SG&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>2002 G7&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2011 G3&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;td>2016 G6&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>2002 G8&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2011 G4&lt;/td>\n&lt;td>&lt;b>NA&lt;/b>&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2016 G7&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>2003 G5&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2011 G5&lt;/td>\n&lt;td>&lt;b>NA&lt;/b>&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2016 G8&lt;/td>\n&lt;td>&lt;b>NA&lt;/b>&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>2004 G7&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2011 G6&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;td>2017 G7&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>2004 G8&lt;/td>\n&lt;td>&lt;b>NA&lt;/b>&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2011 G7&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;td>2017 G8&lt;/td>\n&lt;td>&lt;b>NA&lt;/b>&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>2005 G5&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2012 G6&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2018 G7&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>2005 G6&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2012 G7&lt;/td>\n&lt;td>&lt;b>NA&lt;/b>&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;td>2019 G6&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>2006 G9&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2012 G8&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2019 G8&lt;/td>\n&lt;td>&lt;b>NA&lt;/b>&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>2007 G8&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;td>2014 G7&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2020 G8&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>2009 G6&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2015 G5&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2021 G8&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>2009 G7&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;td>2015 G7&lt;/td>\n&lt;td>&lt;b>NA&lt;/b>&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;td>2022 G6&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>2009 G8&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;td>2015 G8&lt;/td>\n&lt;td>&lt;b>NA&lt;/b>&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;td>2022 G7&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>2010 G5&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2016 G5&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>2022 G8&lt;/td>\n&lt;td>&lt;b>NA&lt;/b>&lt;/td>\n&lt;td>&lt;b>X&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 3** Performance comparison of Seed-Prover against previous systems across formal math tasks. The performance on PutnamBench is using the number of proved statements instead of percentage following previous works [20].\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Metric&lt;/th>\n&lt;th>Seed-Prover&lt;/th>\n&lt;th>Previous SOTA&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>IMO 2025&lt;/td>\n&lt;td>4/6 (Heavy, 5/6 post-competition)&lt;/td>\n&lt;td>5/6 (Natural language, Gemini)&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Past IMO&lt;/td>\n&lt;td>78.1% (Heavy)&lt;/td>\n&lt;td>—&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MiniF2F-valid&lt;/td>\n&lt;td>100.0% (Medium&lt;sup>1&lt;/sup>)&lt;/td>\n&lt;td>90.6% (DeepSeek-Prover-V2 [15])&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MiniF2F-test&lt;/td>\n&lt;td>99.6% (Medium&lt;sup>2&lt;/sup>)&lt;/td>\n&lt;td>92.2% (Kimina-Prover [21])&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>PutnamBench&lt;/td>\n&lt;td>331/657 (Medium)&lt;/td>\n&lt;td>86/657 (Goedel-Prover-V2 [9])&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>CombiBench&lt;/td>\n&lt;td>30.0% (Medium)&lt;/td>\n&lt;td>10.0% (Deepseek-Prover-V2 [15])&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MiniCTX-v2&lt;/td>\n&lt;td>81.8% (Light)&lt;/td>\n&lt;td>44.3% (o4-mini [16])&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n&lt;sup>1&lt;/sup>One problem used Heavy. &lt;sup>2&lt;/sup>One problem failed under Heavy.\n\n### 3.2 Seed-Prover\n\nTo evaluate the performance of Seed-Prover, we tested it on IMO 2025&lt;sup>2&lt;/sup>, past IMO problems, MiniF2F [31], PutnamBench [20], CombiBench [10], and MiniCTX-v2 [6] covering a wide range of mathematical domains. For PutnamBench and CombiBench, we first evaluate using the light setting and use the medium setting for unsolved problems. For IMO problems and MiniF2F, we also use the heavy setting for the remaining unsolved problems. The results are shown in Table 3. Unless otherwise specified, we use Lean v4.14.0 with its corresponding Mathlib version.\n\n*IMO 2025* During the IMO 2025 contest, all problems were translated into formal statements by human experts. For fill-in-the-blank problems (“determine  $x$  such that ...”), initial solution candidates were generated by Seed1.6-Thinking before translation. We conducted searches for IMO 2025 Problems 1, 3, 4, and 5 using both the medium and heavy inference settings in parallel. As required by the IMO committee, all proof submissions were due by July 18th. Seed-Geometry solved Problem 2 instantly, and Seed-Prover derived the proof for Problem 5 under the medium inference setting, while proofs for the other three problems required the heavy inference setting. Notably, the proof for Problem 1 was finished after the deadline.\n\n&lt;sup>2&lt;/sup>ByteDance was officially invited to participate in IMO 2025.*Past IMO* To evaluate our system’s performance on past IMO problems, we curated a dataset consisting of 155 past IMO problems. Most problems were adapted from Compfiles&lt;sup>3&lt;/sup> and MiniF2F [31]. Additionally, a subset of problems was manually added or corrected by human experts. For problems prior to 2017, we used light and medium settings. For problems after 2017, we use the heavy inference setting if the medium inference setting failed. Seed-Prover successfully proves 121/155 problems, achieving an overall success rate of 78.1%. By difficulty, Seed-Prover proves 47/55 easy problems (P1 or P4), 47/56 medium problems (P2 or P5), and 27/44 hard problems (P3 or P6). By subject area, it proves 72/85 algebra problems, 42/55 number theory problems, and 7/14 combinatorics problems. This demonstrates that the Seed-Prover’s performance at IMO 2025 reflects consistent capability on IMO problems across all years.\n\n*MiniF2F* [31] Under the medium setting, we prove 99.6% problems on both MiniF2F-valid and MiniF2F-test. We used the heavy inference setting to tackle the last problem in both splits (i.e. IMO 1990 P3 and IMOSL 2007 Algebra P6). Seed-Prover successfully proved IMO 1990 P3 and failed on IMOSL 2007 Algebra P6. Interestingly, among the most challenging problems solved in MiniF2F are ones such as AMC12A 2021 P12, AMC12A 2021 P25, and AMC12A 2020 P9, which are relatively straightforward to reason about in natural language, but pose significant challenges when formalized in Lean. This difficulty arises primarily from obstacles in applying Vieta’s formulas or the non-triviality of counting roots.\n\n*PutnamBench* [20] We evaluated Seed-Prover on PutnamBench using the light and medium inference settings. Under the light inference setting only, Seed-Prover proved 201/657 problems from PutnamBench. Using the medium inference setting improved this performance to 331/657 problems. This result shows a significant performance jump compared to previous works on undergraduate math problems.\n\n*CombiBench* [10] Previous benchmarks have primarily focused on number theory and algebra problems. CombiBench is a benchmark specifically centered on combinatorial problems, where the problems often involve newly-defined concepts. Here, we evaluate Seed-Prover on CombiBench using the medium inference setting. Our model proves 30 out of 100 problems from CombiBench, outperforming previous work. Nonetheless, relative to other benchmarks, our model still struggles with proving combinatorics problems.\n\n*MiniCTX-v2* [6] To test our system on a broader range of mathematical subjects from real-world formalization projects—including the ability to understand new definitions, notations, and lemmas—we evaluated Seed-Prover on MiniCTX-v2. This dataset includes context-rich problems from formalization repositories in subjects such as axiomatic systems, high-energy physics, analysis, and research-level number theory, all of which were written after Nov. 2024 to prevent data contamination. For evaluation purposes, we used the light inference setting under Lean v4.16.0. Our system successfully achieved 81.8% of MiniCTX-v2, which demonstrates its strong potential in real-world automated theorem proving, generalizing beyond standalone competition problems. For comparison, the baseline o4-mini solved 44.3% statements at Pass@8 [16].\n\n## 4 Conclusion\n\nIn this work, we presented Seed-Geometry and Seed-Prover—two formal reasoning frameworks that integrate the capabilities of large language models. Both systems substantially outperform previous formal reasoning frameworks. Seed-Geometry accelerates verification and scales the search mechanism. Seed-Prover leverages iterative refinement and a three-tiered test-time inference strategy to achieve state-of-the-art. Notably, we successfully proved 5 out of 6 problems in IMO 2025, demonstrating the efficacy of these formal systems. Formal languages like Lean offer rapid proof verification, making them far more cost-effective than human experts and more reliable than LLM judges. Our future work will focus on combining formal systems with large language models to tackle open conjectures.\n\n---\n\n&lt;sup>3&lt;/sup>&lt;https://github.com/dwrensha/compfiles>## References\n\n- [1] Alon Albalak, Duy Phung, Nathan Lile, Rafael Rafailov, Kanishk Gandhi, Louis Castricato, Anikait Singh, Chase Blagden, Violet Xiang, Dakota Mahan, and Nick Haber. Big-math: A large-scale, high-quality math dataset for reinforcement learning in language models, 2025. URL &lt;https://arxiv.org/abs/2502.17387>.\n- [2] Yuri Chervonyi, Trieu H Trinh, Miroslav Olšák, Xiaomeng Yang, Hoang Nguyen, Marcelo Menegali, Junehyuk Jung, Vikas Verma, Quoc V Le, and Thang Luong. Gold-medalist performance in solving olympiad geometry with alphageometry2. *arXiv preprint arXiv:2502.03544*, 2025.\n- [3] DeepMind. Ai solves imo problems at silver medal level. &lt;https://deepmind.google/discover/blog/ai-solves-imo-problems-at-silver-medal-level/>, 2024.\n- [4] DeepSeek-AI. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning, 2025. URL &lt;https://arxiv.org/abs/2501.12948>.\n- [5] Kefan Dong and Tengyu Ma. Stp: Self-play llm theorem provers with iterative conjecturing and proving, 2025. URL &lt;https://arxiv.org/abs/2502.00212>.\n- [6] Jiewen Hu, Thomas Zhu, and Sean Welleck. miniCTX: Neural theorem proving with (long-)contexts. In *The Thirteenth International Conference on Learning Representations*, 2025. URL &lt;https://openreview.net/forum?id=KIgaAqEFHW>.\n- [7] Albert Qiaochu Jiang, Sean Welleck, Jin Peng Zhou, Timothee Lacroix, Jiacheng Liu, Wenda Li, Mateja Jamnik, Guillaume Lample, and Yuhuai Wu. Draft, sketch, and prove: Guiding formal theorem provers with informal proofs. In *The Eleventh International Conference on Learning Representations*, 2023.\n- [8] Jia Li, Edward Beeching, Lewis Tunstall, Ben Lipkin, Roman Soletskyi, Shengyi Costa Huang, Kashif Rasul, Longhui Yu, Albert Jiang, Ziju Shen, Zihan Qin, Bin Dong, Li Zhou, Yann Fleureau, Guillaume Lample, and Stanislas Polu. Numinamath. [&lt;https://github.com/project-numina/aimo-progress-prize>] ([https://github.com/project-numina/aimo-progress-prize/blob/main/report/numina\\\\_dataset.pdf](https://github.com/project-numina/aimo-progress-prize/blob/main/report/numina_dataset.pdf)), 2024.\n- [9] Yong Lin, Shange Tang, Bohan Lyu, Jiayun Wu, Hongzhou Lin, Kaiyu Yang, Jia Li, Mengzhou Xia, Danqi Chen, Sanjeev Arora, et al. Goedel-prover: A frontier model for open-source automated theorem proving. *arXiv preprint arXiv:2502.07640*, 2025.\n- [10] Junqi Liu, Xiaohan Lin, Jonas Bayer, Yael Dillies, Weijie Jiang, Xiaodan Liang, Roman Soletskyi, Haiming Wang, Yunzhou Xie, Beibei Xiong, et al. Combibench: Benchmarking llm capability for combinatorial mathematics. *arXiv preprint arXiv:2505.03171*, 2025.\n- [11] OpenAI. Openai o1 system card, 2024. URL &lt;https://arxiv.org/abs/2412.16720>.\n- [12] Zhongyuan Peng, Yifan Yao, Kaijing Ma, Shuyue Guo, Yizhe Li, Yichi Zhang, Chenchen Zhang, Yifan Zhang, Zhouliang Yu, Luming Li, et al. Criticlean: Critic-guided reinforcement learning for mathematical formalization. *arXiv preprint arXiv:2507.06181*, 2025.\n- [13] Ivo Petrov, Jasper Dekoninck, Lyuben Baltadzhiev, Maria Drencheva, Kristian Minchev, Mislav Balunović, Nikola Jovanović, and Martin Vechev. Proof or bluff? evaluating llms on 2025 usa math olympiad, 2025. URL &lt;https://arxiv.org/abs/2503.21934>.\n- [14] Stanislas Polu, Jesse Michael Han, Kunhao Zheng, Mantas Baksys, Igor Babuschkin, and Ilya Sutskever. Formal mathematics statement curriculum learning. *arXiv preprint arXiv:2202.01344*, 2022.\n- [15] ZZ Ren, Zhihong Shao, Junxiao Song, Huajian Xin, Haocheng Wang, Wanjia Zhao, Liyue Zhang, Zhe Fu, Qihao Zhu, Dejian Yang, et al. Deepseek-prover-v2: Advancing formal mathematical reasoning via reinforcement learning for subgoal decomposition. *arXiv preprint arXiv:2504.21801*, 2025.\n- [16] Tate Rowney, Jiewen Hu, Thomas Zhu, and Sean Welleck. miniCTX leaderboard. &lt;https://cmu-l3.github.io/minictx/leaderboard.html>, 2025. Accessed July 28, 2025.\n- [17] ByteDance Seed, Jiaze Chen, Tiantian Fan, Xin Liu, Lingjun Liu, Zhiqi Lin, Mingxuan Wang, Chengyi Wang, Xiangpeng Wei, Wenyuan Xu, et al. Seed1.5-thinking: Advancing superb reasoning models with reinforcement learning. *arXiv preprint arXiv:2504.13914*, 2025.\n- [18] Rico Sennrich, Barry Haddow, and Alexandra Birch. Neural machine translation of rare words with subword units. *arXiv preprint arXiv:1508.07909*, 2015.- [19] Trieu H Trinh, Yuhuai Wu, Quoc V Le, He He, and Thang Luong. Solving olympiad geometry without human demonstrations. *Nature*, 625(7995):476–482, 2024.\n- [20] George Tsoukalas, Jasper Lee, John Jennings, Jimmy Xin, Michelle Ding, Michael Jennings, Amitayush Thakur, and Swarat Chaudhuri. Putnambench: Evaluating neural theorem-provers on the putnam mathematical competition. In *The Thirty-eighth Conference on Neural Information Processing Systems Datasets and Benchmarks Track*.\n- [21] Haiming Wang, Mert Unsal, Xiaohan Lin, Mantas Baksys, Junqi Liu, Marco Dos Santos, Flood Sung, Marina Vinyes, Zhenzhe Ying, Zekai Zhu, Jianqiao Lu, Hugues de Saxcé, Bolton Bailey, Chendong Song, Chenjun Xiao, Dehao Zhang, Ebony Zhang, Frederick Pu, Han Zhu, Jiawei Liu, Jonas Bayer, Julien Michel, Longhui Yu, Léo Dreyfus-Schmidt, Lewis Tunstall, Luigi Pagani, Moreira Machado, Pauline Bourigault, Ran Wang, Stanislas Polu, Thibaut Barroyer, Wen-Ding Li, Yazhe Niu, Yann Fleureau, Yangyang Hu, Zhouliang Yu, Zihan Wang, Zhilin Yang, Zhengying Liu, and Jia Li. Kimina-prover preview: Towards large formal reasoning models with reinforcement learning. 2025. URL &lt;http://arxiv.org/abs/2504.11354>.\n- [22] Zijian Wu, Suozhi Huang, Zhejian Zhou, Huaiyuan Ying, Jiayu Wang, Dahua Lin, and Kai Chen. Internlm2.5-stepprover: Advancing automated theorem proving via expert iteration on large-scale lean problems, 2024. URL &lt;https://arxiv.org/abs/2410.15700>.\n- [23] Zijian Wu, Jiayu Wang, Dahua Lin, and Kai Chen. Lean-github: Compiling github lean repositories for a versatile lean prover, 2024. URL &lt;https://arxiv.org/abs/2407.17227>.\n- [24] Huajian Xin, Z.Z. Ren, Junxiao Song, Zihong Shao, Wanjia Zhao, Haocheng Wang, Bo Liu, Liyue Zhang, Xuan Lu, Qiushi Du, Wenjun Gao, Haowei Zhang, Qihao Zhu, Dejian Yang, Zhibin Gou, Z.F. Wu, Fuli Luo, and Chong Ruan. Deepseek-prover-v1.5: Harnessing proof assistant feedback for reinforcement learning and monte-carlo tree search. In *The Thirteenth International Conference on Learning Representations*, 2025. URL &lt;https://openreview.net/forum?id=I4YAIwrsXa>.\n- [25] Ran Xin, Chenguang Xi, Jie Yang, Feng Chen, Hang Wu, Xia Xiao, Yifan Sun, Shen Zheng, and Kai Shen. Bfs-prover: Scalable best-first tree search for llm-based automatic theorem proving, 2025. URL &lt;https://arxiv.org/abs/2502.03438>.\n- [26] Kaiyu Yang, Aidan Swope, Alex Gu, Rahul Chalamala, Peiyang Song, Shixing Yu, Saad Godil, Ryan J Prenger, and Animashree Anandkumar. Leandojo: Theorem proving with retrieval-augmented language models. *Advances in Neural Information Processing Systems*, 36:21573–21612, 2023.\n- [27] Huaiyuan Ying, Zijian Wu, Yihan Geng, Jiayu Wang, Dahua Lin, and Kai Chen. Lean workbook: A large-scale lean problem set formalized from natural language math problems. In *The Thirty-eighth Conference on Neural Information Processing Systems Datasets and Benchmarks Track*.\n- [28] Qiyong Yu, Zheng Zhang, Ruofei Zhu, Yufeng Yuan, Xiaochen Zuo, Yu Yue, Weinan Dai, Tiantian Fan, Gaohong Liu, Lingjun Liu, et al. Dapo: An open-source llm reinforcement learning system at scale. *arXiv preprint arXiv:2503.14476*, 2025.\n- [29] Yu Yue, Yufeng Yuan, Qiyong Yu, Xiaochen Zuo, Ruofei Zhu, Wenyuan Xu, Jiaze Chen, Chengyi Wang, TianTian Fan, Zhengyin Du, Xiangpeng Wei, Xiangyu Yu, Gaohong Liu, Juncai Liu, Lingjun Liu, Haibin Lin, Zhiqi Lin, Bole Ma, Chi Zhang, Mofan Zhang, Wang Zhang, Hang Zhu, Ru Zhang, Xin Liu, Mingxuan Wang, Yonghui Wu, and Lin Yan. Vapo: Efficient and reliable reinforcement learning for advanced reasoning tasks, 2025. URL &lt;https://arxiv.org/abs/2504.05118>.\n- [30] Chi Zhang, Jiajun Song, Siyu Li, Yitao Liang, Yuxi Ma, Wei Wang, Yixin Zhu, and Song-Chun Zhu. Proposing and solving olympiad geometry with guided tree search. *arXiv preprint arXiv:2412.10673*, 2024.\n- [31] Kunhao Zheng, Jesse Michael Han, and Stanislas Polu. minif2f: a cross-system benchmark for formal olympiad-level mathematics. In *International Conference on Learning Representations*.\n- [32] Yichi Zhou, Jianqiu Zhao, Yongxin Zhang, Bohan Wang, Siran Wang, Luoxin Chen, Jiahui Wang, Haowei Chen, Allan Jie, Xinbo Zhang, et al. Solving formal math problems by decomposition and iterative reflection. *arXiv preprint arXiv:2507.15225*, 2025.# Appendix\n\n## A Contributors\n\nThe names are sorted alphabetically. An asterisk \\* indicates a member who left Seed.\n\n*Algorithm* Luoxin Chen, Liankai Huang, Zhicheng Jiang, Allan Jie, Xiaoran Jin, Xing Jin, Chenggang Li, Wenlei Shi, Jiahui Wang, Siran Wang, Chenrui Wei, Shufa Wei, Yonghui Wu, Huajian Xin, Fan Yang, Hongyi Yuan, Zheng Yuan, Tianyang Zhan, Chi Zhang, Yue Zhang\\*, Yichi Zhou, Thomas Hanwen Zhu\n\n*Data* Jinming Gu, Wenhao Huang, Zhicheng Jiang, Xiaoran Jin, Kaijing Ma, Jiawei Shen, Tong Sun, Chenrui Wei, Shufa Wei, Yuchen Wu, Yihang Xia, Huaiyuan Ying\\*, Zheng Yuan, Ge Zhang\n\n*Infra* Cheng Ren, He Sun, Zhihong Wang, Tianyun Zhao\\*, Jianqiu Zhao, Thomas Hanwen Zhu\n\n## B LooKeng: An Easy-to-Use and Effective Python Interface for Lean\n\nInteracting with Lean poses significant challenges that limit the flexibility of Lean-based workflows. The most popular interface, LeanDojo [26], only supports earlier versions of Lean 4, restricting users from accessing Lean’s newest updates. Furthermore, LeanDojo requires creating a Lean repository for interaction, which makes it impractical to use considering the massive scale of Lean interaction during model development and inference. To address these issues, we introduce LooKeng, a REPL&lt;sup>4&lt;/sup>-based Python interface designed to simplify and accelerate the interaction process. LooKeng offers powerful features for developers while providing a user-friendly interface for end-users. The core functionality of LooKeng includes ‘init\\_state’, ‘run\\_tac’, and ‘verify\\_proof’. One can use LooKeng to interact with Lean step-by-step or verify an entire proof directly. The key features of LooKeng are summarized as follows:\n\n- • **Stateless Design:** A Lean state can be simultaneously processed using different LooKeng instances, enabling effortless scaling and sharing.\n- • **Complex Tactics:** Complex tactics such as `apply?` and `all_goals` are fully supported, with enhanced infotree integration to prevent false positive proofs.\n- • **Version-Free:** The LooKeng CLI allows users to manage and switch between different Lean versions.\n- • **Memory Control:** Users can easily track the memory consumption of the Lean backend, set custom thresholds, and automatically terminate processes when memory usage exceeds the limit.\n- • **Proof Verification:** LooKeng provides a straightforward method, ‘verify\\_proof’, to rigorously verify the final proof using the native Lean interface, ensuring correctness and reliability.\n- • **Proof Simplification:** LooKeng can remove useless tactics and hypothesis in the proof to obtain a simpler proof.\n- • **Statement Negation:** LooKeng is able to generate the negated statement of a statement.\n- • **Multi-Concurrency Support:** LooKeng can run as a service, handling thousands of concurrent requests via async architecture and resource isolation.\n\n---\n\n&lt;sup>4&lt;/sup>&lt;https://github.com/leanprover-community/repl>\n",
    "durationMs": 702,
    "url": "https://huggingface.co/papers/2507.23726"
  },
  "sourceToolAssistantUUID": "7e63e546-a34a-48e5-a9db-d65717b10735",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34 · 2026-05-27T16:02:54.635Z_

```json
{
  "parentUuid": "f15701c1-a352-4ca8-ab6e-54926140e157",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "db7bc31c-fb30-4cf8-940a-db50683dfcb7",
  "timestamp": "2026-05-27T16:02:54.635Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-27 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "db7bc31c-fb30-4cf8-940a-db50683dfcb7",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze Seed-Prover paper for research innovation",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d"
}
```

---

### Assistant

_source line 37 · 2026-05-27T16:03:18.632Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a very comprehensive understanding of the paper. Let me synthesize all the information I've gathered into the requested JSON analysis. Let me think deeply about the innovation structure.

Key observations:

1. **Problem identification**: The gap they identified is the tension between "deep reasoning" (long chain-of-thought within a single proof attempt) and "broad reasoning" (exploring many different proof strategies). Prior whole-proof models generate once and lack compiler interaction; step-level provers interact closely but can't do high-level reasoning. They also identified that natural language proofs can't be verified automatically, making RL training hard - but formal languages like Lean provide perfect verification signals.


2. **Key insight**: The lemma-style proving paradigm is the central innovation. Rather than generating a complete proof monolithically, they decompose it into independently-verifiable lemmas that can be reused across different proof attempts, accumulated in a shared pool, and recombined. This creates a modular "currency" of intermediate results that enables both refinement within a single trajectory and knowledge transfer across multiple attempts.
3. **Innovation type**: This is fundamentally a combination strategy—merging whole-proof generation with iterative compiler feedback, lemma-based modularity, conjecture generation for exploration breadth, and a three-tiered test-time compute approach. The lemma-style formulation itself represents a genuinely novel way of structuring the problem.
4. **What makes it compelling**: The empirical results are striking—they saturate miniF2F, achieve a 3x boost on PutnamBench, and solve 5 out of 6 IMO 2025 problems. The system design is elegant because the lemma abstraction bridges training and inference seamlessly. The three-tiered inference strategy (light/medium/heavy) provides a principled way to allocate computational resources at test time.
5. **Where it falls short**: Combinatorics remains a weak point at 30% on CombiBench. Geometry problems need a separate specialized module. The heavy inference tier demands days of computation. The approach requires human formalization of problem statements upfront, and one miniF2F problem still resists solution.
6. **Context**: This is an arXiv preprint rather than a peer-reviewed venue, so there are no reviewer critiques to consider.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db7bc31c-fb30-4cf8-940a-db50683dfcb7",
  "isSidechain": false,
  "requestId": "req_011CbTMafHCne314HR47a6CY",
  "type": "assistant",
  "uuid": "afdabf0e-88f0-4cd5-b06d-7e0077fa01a6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EVxTp5BmecMCHzd5yZbcys",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 28214,
      "cache_read_input_tokens": 16344,
      "output_tokens": 680,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28214,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 680,
          "cache_read_input_tokens": 16344,
          "cache_creation_input_tokens": 28214,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28214
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

_source line 38 · 2026-05-27T16:03:18.641Z_

Now I have comprehensive coverage of the full paper. Let me also check if there are any reviewer comments on OpenReview (this is an arXiv preprint, but worth checking).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "afdabf0e-88f0-4cd5-b06d-7e0077fa01a6",
  "isSidechain": false,
  "requestId": "req_011CbTMafHCne314HR47a6CY",
  "type": "assistant",
  "uuid": "e699de02-6593-4efe-8529-e046ef2fa807",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EVxTp5BmecMCHzd5yZbcys",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 28214,
      "cache_read_input_tokens": 16344,
      "output_tokens": 680,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28214,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 680,
          "cache_read_input_tokens": 16344,
          "cache_creation_input_tokens": 28214,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28214
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

_source line 39 · 2026-05-27T16:03:19.115Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Wmn5ZeAku75mTN1JsBW717`</summary>

```json
{
  "url": "https://openreview.net/search?term=Seed-Prover+Deep+Broad+Reasoning+Automated+Theorem+Proving",
  "prompt": "Is there an OpenReview submission for \"Seed-Prover: Deep and Broad Reasoning for Automated Theorem Proving\"? If so, extract the review scores, reviewer comments, praise, and criticisms."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e699de02-6593-4efe-8529-e046ef2fa807",
  "isSidechain": false,
  "requestId": "req_011CbTMafHCne314HR47a6CY",
  "type": "assistant",
  "uuid": "015047b7-46f4-4d51-862e-878f72a76a86",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EVxTp5BmecMCHzd5yZbcys",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 28214,
      "cache_read_input_tokens": 16344,
      "output_tokens": 680,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 28214,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 680,
          "cache_read_input_tokens": 16344,
          "cache_creation_input_tokens": 28214,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 28214
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

_source line 40 · 2026-05-27T16:03:21.883Z_

<details><summary>↩ Tool result · `toolu_01Wmn5ZeAku75mTN1JsBW717`</summary>

```text
# Response

Based on the webpage content provided, I cannot find any information about a submission titled "Seed-Prover: Deep and Broad Reasoning for Automated Theorem Proving." 

The content shown is only the OpenReview.net homepage with navigation menus, footer links, and a general description stating that "OpenReview is a long-term project to advance science through improved peer review with legal nonprofit status." There are no specific paper submissions, review scores, reviewer comments, or evaluations displayed in this excerpt.

To locate this submission, you would need to search directly on the OpenReview platform using the paper title or browse the relevant venue's submissions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "015047b7-46f4-4d51-862e-878f72a76a86",
  "isSidechain": false,
  "promptId": "90291295-f415-450f-a2ae-7009e730e84a",
  "type": "user",
  "uuid": "a6a9163c-9bac-4a9d-8244-ba2945bffb65",
  "toolUseResult": {
    "bytes": 62377,
    "code": 200,
    "codeText": "OK",
    "result": "# Response\n\nBased on the webpage content provided, I cannot find any information about a submission titled \"Seed-Prover: Deep and Broad Reasoning for Automated Theorem Proving.\" \n\nThe content shown is only the OpenReview.net homepage with navigation menus, footer links, and a general description stating that \"OpenReview is a long-term project to advance science through improved peer review with legal nonprofit status.\" There are no specific paper submissions, review scores, reviewer comments, or evaluations displayed in this excerpt.\n\nTo locate this submission, you would need to search directly on the OpenReview platform using the paper title or browse the relevant venue's submissions.",
    "durationMs": 2763,
    "url": "https://openreview.net/search?term=Seed-Prover+Deep+Broad+Reasoning+Automated+Theorem+Proving"
  },
  "sourceToolAssistantUUID": "015047b7-46f4-4d51-862e-878f72a76a86",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-27T16:03:25.059Z_

<details><summary>Logged reasoning block</summary>

```text
As expected, this is an arXiv preprint (July 2025) and not yet on OpenReview. Let me now synthesize all the information into the requested JSON analysis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6a9163c-9bac-4a9d-8244-ba2945bffb65",
  "isSidechain": false,
  "requestId": "req_011CbTMcfnXBeAXXWXZNk8QH",
  "type": "assistant",
  "uuid": "10a76562-da4f-4832-b306-34e1d62cfe45",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LR4rsZRUvthzELttFgmHGT",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 833,
      "cache_read_input_tokens": 44558,
      "output_tokens": 2205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 833,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2205,
          "cache_read_input_tokens": 44558,
          "cache_creation_input_tokens": 833,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 833
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

_source line 42 · 2026-05-27T16:04:22.877Z_

No OpenReview submission found — this is a fresh arXiv preprint (July 31, 2025). I now have everything I need. Let me produce the deep analysis.

```json
{
  "title": "Seed-Prover: Deep and Broad Reasoning for Automated Theorem Proving",
  "venue": "arXiv 2025 (preprint, July 31)",
  "problem_identification": "The authors identified a fundamental tension in LLM-based formal theorem proving: step-level provers (like AlphaProof) enable close Lean interaction but are too granular for high-level reasoning, while whole-proof generators produce complete proofs but lack compiler feedback. More deeply, they recognized that existing systems pursue either deep reasoning (long chain-of-thought within one attempt) or broad search (many independent attempts), but never both simultaneously — and that the key missing primitive is a unit of intermediate progress that can be independently verified, shared across trajectories, and composed. They found this gap by observing that whole-proof + long-CoT models (DeepSeek-Prover-V2, Kimina-Prover) had overtaken step-level provers but plateaued because each proof attempt was monolithic and couldn't leverage partial progress from failed attempts.",
  "key_insight": "Make the lemma — not the full proof — the atomic unit of reasoning. By restructuring proofs so that independently-compilable lemmas are generated before the main theorem, you create a 'currency' of verified partial progress that can be pooled across inference trajectories, iteratively refined with compiler feedback, and composed to solve problems far harder than any single generation could handle. This transforms theorem proving from a single-shot generation problem into a collaborative accumulation problem.",
  "innovation_type": "combination",
  "method_summary": "Seed-Prover is a whole-proof LLM trained via multi-stage RL (VAPO) with a binary Lean-verification reward, but with a crucial structural constraint: it must generate named lemmas before the main theorem. This enables a three-tiered test-time scaling strategy. (1) Light: iterative refinement using Lean compiler feedback and self-summarization (8–16 rounds × Pass@8–16, equivalent to Pass@64–256). (2) Medium: outer refinement of the main proof plus inner refinement loops that target specific failed lemmas, enabling proofs exceeding 1000 lines. (3) Heavy: a 'conjecture proposer' generates ~5000 conjectures about problem properties (e.g., injectivity, monotonicity), each is proved/disproved via Light inference, proved lemmas accumulate in a scored pool over days, and the top-ranked lemmas are fed to Medium inference to complete the main proof. Training is distinctive: prompts randomly include natural language hints, compiler errors, proved/failed lemmas, and self-summaries — training the model to consume exactly the signals it will receive during the iterative inference pipeline. A separate Seed-Geometry engine handles geometry via neuro-symbolic forward-chaining with a C++ backend (100× faster than prior Python implementations) and 230M synthetic geometry problems.",
  "what_makes_it_good": "The results are staggering and constitute the strongest evidence yet for formal reasoning systems: saturating miniF2F (99.6% test), 331/657 on PutnamBench (vs. 86 prior SOTA — a 3.8× jump), 78.1% of all formalized past IMO problems, and 5/6 IMO 2025 problems formally proved. What elevates this beyond a 'we scaled harder' story is the architectural elegance: the lemma abstraction is a single idea that simultaneously solves the cross-trajectory knowledge sharing problem, the partial-progress identification problem, and the proof compositionality problem. The paper also demonstrates strong engineering taste — the three-tiered inference strategy is a principled compute-allocation framework, not ad hoc, and the conjecture proposer explicitly decouples breadth (exploring problem properties) from depth (proving specific claims).",
  "limitations_acknowledged": "The authors acknowledge that combinatorics remains a weak spot (only 30% on CombiBench vs. strong algebra/number theory performance), that geometry requires an entirely separate specialized engine because Lean lacks sufficient geometry support, and that the heavy inference setting requires 'days of thinking' — making computational cost a real barrier. They also note that the MOHS hardness scale for humans may not align with LLM difficulty in Lean, suggesting their understanding of what makes problems hard for their system is still incomplete.",
  "open_questions": [
    "Can the lemma-pool accumulation approach be made self-improving — i.e., can proved lemmas from one problem transfer to accelerate proving related problems, creating a growing mathematical library? The paper hints at this but doesn't explore it.",
    "The conjecture proposer is trained to enumerate properties (injective, surjective, monotonic, etc.) but how does it decide when to stop exploring breadth and commit to depth? The current approach uses fixed budgets (5000 conjectures) — is there a principled way to adaptively allocate between conjecture generation and proof attempts?",
    "The system still requires human experts to formalize problem statements into Lean (autoformalization is not addressed). Can the lemma-style approach be extended to also autoformalize from natural language, closing the loop between informal and formal reasoning?"
  ],
  "building_blocks": [
    "VAPO (reinforcement learning algorithm for LLM training with binary verification rewards)",
    "Lean 4 compiler as verification oracle / reward signal",
    "LooKeng (custom Python-Lean REPL interface supporting async, multi-concurrency, proof simplification)",
    "Lemma pool data structure (storing statements, proofs, difficulty scores, dependency relations)",
    "Self-summarization of failed proof attempts as context for next iteration",
    "Conjecture proposing as a separate inference mode from proof generation",
    "Three-tiered test-time compute scaling (Light/Medium/Heavy)",
    "Neuro-symbolic forward-chaining geometry engine (C++ backend with Pybind11)",
    "Beam search with distributed GPU setup for geometry auxiliary construction",
    "Open-source datasets: BigMath, Lean Workbook, NuminaMath, Compfiles, CriticLean",
    "Seed1.5-Thinking / Seed1.6-Thinking as base models",
    "Formatting penalty in RL reward to enforce lemma-before-theorem structure"
  ],
  "reviewer_feedback_summary": null,
  "relevance_to_seed": "This paper is the current frontier of autoformalization-adjacent work: it demonstrates that formal verification (Lean) combined with LLM reasoning can solve IMO-level problems that informal reasoning alone cannot verify. For our research area of bridging informal and formal mathematical reasoning, the critical gap Seed-Prover exposes but does NOT address is the autoformalization step itself — all problem statements were manually formalized by human experts. The lemma-style proving paradigm and iterative refinement with compiler feedback are directly reusable architectural patterns for any system that needs to bridge informal mathematical intuition (conjecture proposing, property enumeration) with formal verification (Lean proof checking). The conjecture proposer, in particular, is essentially doing informal mathematical reasoning (enumerating properties without formal proof) that then gets formalized — this is a natural seam where autoformalization research could plug in."
}
```

---

**Meta-analysis — what can we learn about the CRAFT of this research:**

1. **The power of the right abstraction.** The single most important decision in this paper is making the *lemma* the atomic unit instead of the *whole proof*. This one reformulation unlocked modularity, cross-trajectory sharing, iterative refinement, and compositionality simultaneously. Great research often comes from finding the right level of abstraction — not too coarse (whole proof), not too fine (individual tactics).

2. **Train for the inference pipeline you'll actually use.** Most prior work trained on clean formal statements and hoped the model would generalize to messy multi-round interactions. Seed-Prover deliberately randomizes prompts during RL training to include compiler errors, failed lemmas, self-summaries — exactly mirroring what the model sees during its Light/Medium/Heavy inference loops. This train-test alignment is an underappreciated engineering principle.

3. **Decouple breadth from depth explicitly.** The conjecture proposer is a separate *mode* that doesn't try to solve the problem — it just explores the space of possibly-useful properties. This is a powerful design pattern: when a problem requires both exploration and exploitation, build separate modules for each rather than hoping one model does both.

4. **Tiered compute allocation as a design principle.** Rather than one inference strategy, they built three (Light → Medium → Heavy) with clear escalation criteria. This lets them efficiently solve easy problems cheaply while investing massive compute only where needed — a practical insight that's often missing from academic papers.

5. **Engineering enables science.** The 100× speedup from rewriting the geometry engine in C++, the LooKeng REPL for async Lean interaction, the distributed GPU setup — these aren't "just engineering." They're what made the heavy inference setting (days of accumulated lemma-proving across thousands of conjectures) feasible at all.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10a76562-da4f-4832-b306-34e1d62cfe45",
  "isSidechain": false,
  "requestId": "req_011CbTMcfnXBeAXXWXZNk8QH",
  "type": "assistant",
  "uuid": "d8df3e87-e7ea-4e62-872c-5bc727b97c3b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LR4rsZRUvthzELttFgmHGT",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 833,
      "cache_read_input_tokens": 44558,
      "output_tokens": 2205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 833,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2205,
          "cache_read_input_tokens": 44558,
          "cache_creation_input_tokens": 833,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 833
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
  "leafUuid": "d8df3e87-e7ea-4e62-872c-5bc727b97c3b",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze Seed-Prover paper for research innovation",
  "sessionId": "16b54da6-26d0-4432-a11f-ea44d2bee85d"
}
```

---
