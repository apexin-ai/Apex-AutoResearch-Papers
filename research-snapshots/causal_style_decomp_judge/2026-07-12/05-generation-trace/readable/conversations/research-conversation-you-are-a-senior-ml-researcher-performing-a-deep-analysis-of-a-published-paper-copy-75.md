# Research conversation: You are a senior ML researcher performing a deep analysis of a published paper. **Today's date: 2026-05-27 (UTC).** ## Y

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 58
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-3/6db262d6-dcf8-4dbf-b94b-349936024bbc.jsonl`
- **Structured JSON:** [`cd007e0f5c743a6c8c79.json`](../../sessions/cd/cd007e0f5c743a6c8c79.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T15:57:08.619Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T15:57:08.619Z",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "content": "You are a senior ML researcher performing a deep analysis of a published paper.\n\n**Today's date: 2026-05-27 (UTC).**\n\n## Your goal\n\nAnalyze this paper NOT just for what it does, but for **HOW it innovates** — what can we learn from its approach to doing research? What made this paper good enough for a top venue?\n\n## Research context\n\nWe are generating ideas in the area of: **Bridging Informal and Formal Mathematical Reasoning — Autoformalization and Proof Verification**\n\n## Paper to analyze\n\n{\n  \"title\": \"Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction\",\n  \"authors\": \"Yong Lin et al. (Princeton, NVIDIA, Caltech)\",\n  \"venue\": \"arXiv 2025\",\n  \"url\": \"https://arxiv.org/abs/2508.03613\",\n  \"why_important\": \"SOTA open-source prover at 8B scale matching 671B models. Introduces scaffolded data synthesis, verifier-guided self-correction, and model averaging — each widely adopted.\",\n  \"one_line_summary\": \"Extends Goedel-Prover with progressive difficulty scaffolding, Lean-compiler-guided self-correction, and model averaging, reaching 90.4% on miniF2F at 32B scale while the 8B model matches DeepSeek-Prover-V2-671B.\"\n}\n\n## Instructions\n\n1. **Deep read**: Use WebFetch to read this paper's full abstract, introduction, method section, and conclusion on arXiv or OpenReview. If it's on OpenReview, also read the reviewer comments and author responses.\n\n2. **Analyze the innovation structure**: Don't just summarize — dissect HOW the authors arrived at their contribution:\n   - What gap did they identify and HOW did they find it?\n   - What was the key insight that others missed?\n   - How did they formulate the problem differently from prior work?\n   - What existing technique did they adapt/combine/simplify?\n\n3. **Learn from reviewers**: If you can find reviewer comments, extract:\n   - What did reviewers praise most?\n   - What concerns were raised and how were they addressed?\n   - What would have made this paper even stronger?\n\n## Output format\n\nOutput a single JSON object:\n{\n  \"title\": \"Paper title\",\n  \"venue\": \"Where published\",\n  \"problem_identification\": \"What gap/problem did they identify? How did they find it? (2-3 sentences)\",\n  \"key_insight\": \"The core intellectual contribution — the aha moment (1-2 sentences)\",\n  \"innovation_type\": \"new_formulation | new_technique | new_benchmark | simplification | cross_domain | combination | scaling | analysis\",\n  \"method_summary\": \"Technical approach in 3-5 sentences — enough to understand the machinery\",\n  \"what_makes_it_good\": \"Why did this paper get accepted? What would reviewers have liked? (2-3 sentences)\",\n  \"limitations_acknowledged\": \"What gaps did the authors themselves identify? (1-2 sentences)\",\n  \"open_questions\": \"What follow-up questions does this paper raise? What remains unsolved? (2-3 bullet points)\",\n  \"building_blocks\": [\"List of methods/tools/datasets used that could be reused\"],\n  \"reviewer_feedback_summary\": \"If found on OpenReview: key praise and concerns. Otherwise: null\",\n  \"relevance_to_seed\": \"How does this paper relate to our research area? What can we learn from it? (1-2 sentences)\"\n}\n\nBe analytical, not descriptive. We want to learn the CRAFT of doing good research, not just know what this paper did."
}
```

---

### Runtime record

_source line 2 · 2026-05-27T15:57:08.623Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T15:57:08.623Z",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc"
}
```

---

## Round 1

56 recorded events

### User

_source line 3 · 2026-05-27T15:57:08.669Z_

You are a senior ML researcher performing a deep analysis of a published paper.

**Today's date: 2026-05-27 (UTC).**

## Your goal

Analyze this paper NOT just for what it does, but for **HOW it innovates** — what can we learn from its approach to doing research? What made this paper good enough for a top venue?

## Research context

We are generating ideas in the area of: **Bridging Informal and Formal Mathematical Reasoning — Autoformalization and Proof Verification**

## Paper to analyze

{
  "title": "Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction",
  "authors": "Yong Lin et al. (Princeton, NVIDIA, Caltech)",
  "venue": "arXiv 2025",
  "url": "https://arxiv.org/abs/2508.03613",
  "why_important": "SOTA open-source prover at 8B scale matching 671B models. Introduces scaffolded data synthesis, verifier-guided self-correction, and model averaging — each widely adopted.",
  "one_line_summary": "Extends Goedel-Prover with progressive difficulty scaffolding, Lean-compiler-guided self-correction, and model averaging, reaching 90.4% on miniF2F at 32B scale while the 8B model matches DeepSeek-Prover-V2-671B."
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
  "promptId": "918f738b-eddd-4a71-9661-57e87bd9f8ed",
  "type": "user",
  "uuid": "47b962aa-36e9-4953-bd1d-54d3974dc236",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T15:57:08.668Z_

```json
{
  "parentUuid": "47b962aa-36e9-4953-bd1d-54d3974dc236",
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
  "uuid": "6ba66875-af58-4150-84fa-0d81819268f4",
  "timestamp": "2026-05-27T15:57:08.668Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T15:57:08.668Z_

```json
{
  "parentUuid": "6ba66875-af58-4150-84fa-0d81819268f4",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "305f0026-fcd9-4bf4-b3eb-6fa1580674db",
  "timestamp": "2026-05-27T15:57:08.668Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
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
  "aiTitle": "Analyze Goedel-Prover-V2 paper innovation",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc"
}
```

---

### Assistant

_source line 7 · 2026-05-27T15:57:11.850Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to analyze the paper "Goedel-Prover-V2" from arXiv. Let me fetch the paper details first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "305f0026-fcd9-4bf4-b3eb-6fa1580674db",
  "isSidechain": false,
  "requestId": "req_011CbTM9AD2ggvQqi9fdhMPY",
  "type": "assistant",
  "uuid": "1f9ddaf7-1dbc-4dab-a859-7fd286499cab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X9dXmknM4TEHUtYutC3tj7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2244,
      "cache_read_input_tokens": 11014,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2244,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 126,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 2244,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2244
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

_source line 8 · 2026-05-27T15:57:12.193Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011kJhixJ8nSyG4VnH6gxWhC`</summary>

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
  "parentUuid": "1f9ddaf7-1dbc-4dab-a859-7fd286499cab",
  "isSidechain": false,
  "requestId": "req_011CbTM9AD2ggvQqi9fdhMPY",
  "type": "assistant",
  "uuid": "1a6d3cfc-716d-436c-95a7-f1050254a6de",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X9dXmknM4TEHUtYutC3tj7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2244,
      "cache_read_input_tokens": 11014,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2244,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 126,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 2244,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2244
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

_source line 9 · 2026-05-27T15:57:12.201Z_

<details><summary>↩ Tool result · `toolu_011kJhixJ8nSyG4VnH6gxWhC`</summary>

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
  "parentUuid": "1a6d3cfc-716d-436c-95a7-f1050254a6de",
  "isSidechain": false,
  "promptId": "918f738b-eddd-4a71-9661-57e87bd9f8ed",
  "type": "user",
  "uuid": "3a8257dc-16dd-4c82-a6b7-34e75705408e",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "1a6d3cfc-716d-436c-95a7-f1050254a6de",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-27T15:57:15.417Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me fetch the paper from arXiv. I'll fetch both the abstract page and the full paper PDF.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a8257dc-16dd-4c82-a6b7-34e75705408e",
  "isSidechain": false,
  "requestId": "req_011CbTM9Rt7DMhdiFNN4qJL5",
  "type": "assistant",
  "uuid": "84915e10-b82c-4d49-b082-2ebd4b1ce517",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019YZreZqjVoqGAUJ2MWK4ve",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 646,
      "cache_read_input_tokens": 13258,
      "output_tokens": 353,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 646,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 353,
          "cache_read_input_tokens": 13258,
          "cache_creation_input_tokens": 646,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 646
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

_source line 11 · 2026-05-27T15:57:16.085Z_

Now let me fetch the paper content from multiple sources in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84915e10-b82c-4d49-b082-2ebd4b1ce517",
  "isSidechain": false,
  "requestId": "req_011CbTM9Rt7DMhdiFNN4qJL5",
  "type": "assistant",
  "uuid": "d61e0048-b37a-406a-b4f4-b06f74d37b80",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019YZreZqjVoqGAUJ2MWK4ve",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 646,
      "cache_read_input_tokens": 13258,
      "output_tokens": 353,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 646,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 353,
          "cache_read_input_tokens": 13258,
          "cache_creation_input_tokens": 646,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 646
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

_source line 12 · 2026-05-27T15:57:17.525Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019Z8P4xLVM7moFiJ6j7A2oo`</summary>

```json
{
  "url": "https://arxiv.org/abs/2508.03613",
  "prompt": "Extract the full abstract, list of authors, and any other metadata available on this arXiv page for the paper \"Goedel-Prover-V2\". Give me everything verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d61e0048-b37a-406a-b4f4-b06f74d37b80",
  "isSidechain": false,
  "requestId": "req_011CbTM9Rt7DMhdiFNN4qJL5",
  "type": "assistant",
  "uuid": "bfba9f4e-400d-4640-8713-8583c340d359",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019YZreZqjVoqGAUJ2MWK4ve",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 646,
      "cache_read_input_tokens": 13258,
      "output_tokens": 353,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 646,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 353,
          "cache_read_input_tokens": 13258,
          "cache_creation_input_tokens": 646,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 646
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

_source line 13 · 2026-05-27T15:57:21.986Z_

<details><summary>↩ Tool result · `toolu_01BUvqZgDWi8MfmsQ3Up9Zvr`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53293372-a24f-4b4e-890e-66e6235d4588",
  "isSidechain": false,
  "promptId": "918f738b-eddd-4a71-9661-57e87bd9f8ed",
  "type": "user",
  "uuid": "a6681a2b-f137-4a7a-8fdb-977205756edd",
  "toolUseResult": {
    "bytes": 0,
    "code": 404,
    "codeText": "Not Found",
    "result": "The server returned HTTP 404 Not Found.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.",
    "durationMs": 6,
    "url": "https://arxiv.org/html/2508.03613"
  },
  "sourceToolAssistantUUID": "53293372-a24f-4b4e-890e-66e6235d4588",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-27T15:57:21.978Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BUvqZgDWi8MfmsQ3Up9Zvr`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.03613",
  "prompt": "Extract the FULL content of this paper, focusing especially on:\n1. The complete Introduction section\n2. The complete Method/Approach section (all subsections)\n3. The complete Results/Experiments section\n4. The complete Conclusion/Discussion section\n5. Any Related Work section\n\nPreserve all technical details, equations, algorithm descriptions, and specifics about their approach including scaffolded data synthesis, self-correction, and model averaging. Be as comprehensive as possible - do not summarize, extract the actual text."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bfba9f4e-400d-4640-8713-8583c340d359",
  "isSidechain": false,
  "requestId": "req_011CbTM9Rt7DMhdiFNN4qJL5",
  "type": "assistant",
  "uuid": "53293372-a24f-4b4e-890e-66e6235d4588",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019YZreZqjVoqGAUJ2MWK4ve",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 646,
      "cache_read_input_tokens": 13258,
      "output_tokens": 353,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 646,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 353,
          "cache_read_input_tokens": 13258,
          "cache_creation_input_tokens": 646,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 646
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

_source line 15 · 2026-05-27T15:57:25.758Z_

<details><summary>↩ Tool result · `toolu_019Z8P4xLVM7moFiJ6j7A2oo`</summary>

```text
# Goedel-Prover-V2 Paper Metadata

**Title:** "Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction"

**Authors:** Yong Lin, Shange Tang, Bohan Lyu, Ziran Yang, Jui-Hui Chung, Haoyu Zhao, Lai Jiang, Yihan Geng, Jiawei Ge, Jingruo Sun, Jiayun Wu, Jiri Gesi, Ximing Lu, David Acuna, Kaiyu Yang, Hongzhou Lin, Yejin Choi, Danqi Chen, Sanjeev Arora, Chi Jin

**arXiv Identifier:** 2508.03613

**Submission Date:** August 5, 2025

**Field:** Computer Science > Machine Learning (cs.LG); Artificial Intelligence (cs.AI)

**Abstract (Verbatim):** "We introduce Goedel-Prover-V2, a series of open-source language models that set a new state-of-the-art in automated theorem proving. Built on the standard expert iteration and reinforcement learning pipeline, our approach incorporates three key innovations: (1) Scaffolded data synthesis: We generate synthetic tasks of increasing difficulty to train the model to master increasingly complex theorems; (2) Verifier-guided self-correction: We enable the model to iteratively revise its proofs by leveraging feedback from the Lean compiler; (3) Model averaging: We merge model checkpoints to mitigate the decrease in model output diversity in later stages of training."

**Additional Metadata:**
- Document length: 24 pages, 10 figures, 4 tables
- License: Creative Commons Zero 1.0 Public Domain
- DOI: https://doi.org/10.48550/arXiv.2508.03613
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bfba9f4e-400d-4640-8713-8583c340d359",
  "isSidechain": false,
  "promptId": "918f738b-eddd-4a71-9661-57e87bd9f8ed",
  "type": "user",
  "uuid": "d12f591b-2e84-4efe-b9ee-ebfa0ff1cd58",
  "toolUseResult": {
    "bytes": 51636,
    "code": 200,
    "codeText": "OK",
    "result": "# Goedel-Prover-V2 Paper Metadata\n\n**Title:** \"Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction\"\n\n**Authors:** Yong Lin, Shange Tang, Bohan Lyu, Ziran Yang, Jui-Hui Chung, Haoyu Zhao, Lai Jiang, Yihan Geng, Jiawei Ge, Jingruo Sun, Jiayun Wu, Jiri Gesi, Ximing Lu, David Acuna, Kaiyu Yang, Hongzhou Lin, Yejin Choi, Danqi Chen, Sanjeev Arora, Chi Jin\n\n**arXiv Identifier:** 2508.03613\n\n**Submission Date:** August 5, 2025\n\n**Field:** Computer Science > Machine Learning (cs.LG); Artificial Intelligence (cs.AI)\n\n**Abstract (Verbatim):** \"We introduce Goedel-Prover-V2, a series of open-source language models that set a new state-of-the-art in automated theorem proving. Built on the standard expert iteration and reinforcement learning pipeline, our approach incorporates three key innovations: (1) Scaffolded data synthesis: We generate synthetic tasks of increasing difficulty to train the model to master increasingly complex theorems; (2) Verifier-guided self-correction: We enable the model to iteratively revise its proofs by leveraging feedback from the Lean compiler; (3) Model averaging: We merge model checkpoints to mitigate the decrease in model output diversity in later stages of training.\"\n\n**Additional Metadata:**\n- Document length: 24 pages, 10 figures, 4 tables\n- License: Creative Commons Zero 1.0 Public Domain\n- DOI: https://doi.org/10.48550/arXiv.2508.03613",
    "durationMs": 8230,
    "url": "https://arxiv.org/abs/2508.03613"
  },
  "sourceToolAssistantUUID": "bfba9f4e-400d-4640-8713-8583c340d359",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-27T15:57:28.456Z_

<details><summary>Logged reasoning block</summary>

```text
The HTML version isn't available. Let me try the PDF version instead, and also check if there's an OpenReview page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d12f591b-2e84-4efe-b9ee-ebfa0ff1cd58",
  "isSidechain": false,
  "requestId": "req_011CbTMAR8F2hApTz9S9cnif",
  "type": "assistant",
  "uuid": "622fbb35-17c8-4a9f-a521-fa2cb71160ee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0153bvQhA5WaFX88AR6T6m1M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 838,
      "cache_read_input_tokens": 13904,
      "output_tokens": 404,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 838,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 85,
          "output_tokens": 404,
          "cache_read_input_tokens": 13904,
          "cache_creation_input_tokens": 838,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 838
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

_source line 17 · 2026-05-27T15:57:28.960Z_

The HTML version isn't available. Let me try the PDF and also check for OpenReview reviews.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "622fbb35-17c8-4a9f-a521-fa2cb71160ee",
  "isSidechain": false,
  "requestId": "req_011CbTMAR8F2hApTz9S9cnif",
  "type": "assistant",
  "uuid": "8af4f864-5bc8-4ad0-bb83-0bb38edf54bc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0153bvQhA5WaFX88AR6T6m1M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 838,
      "cache_read_input_tokens": 13904,
      "output_tokens": 404,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 838,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 85,
          "output_tokens": 404,
          "cache_read_input_tokens": 13904,
          "cache_creation_input_tokens": 838,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 838
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

_source line 18 · 2026-05-27T15:57:32.305Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HC3PtBdMiN1VMSYawuTfBM`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2508.03613",
  "prompt": "Extract the FULL content of this paper \"Goedel-Prover-V2\", focusing especially on:\n1. The complete Introduction section - what problem they identify, what gaps exist, motivation\n2. The complete Method/Approach section with ALL subsections - scaffolded data synthesis, self-correction, model averaging, expert iteration, RL details\n3. The Experiments/Results section - benchmarks, ablations, key numbers\n4. The Conclusion/Discussion section\n5. Related Work section\n6. Any limitations or future work discussion\n\nPreserve ALL technical details, algorithm descriptions, training procedures, dataset details, and specific numbers. Be maximally comprehensive."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8af4f864-5bc8-4ad0-bb83-0bb38edf54bc",
  "isSidechain": false,
  "requestId": "req_011CbTMAR8F2hApTz9S9cnif",
  "type": "assistant",
  "uuid": "b7524434-f87d-461e-b58b-cbbe5144d7f2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0153bvQhA5WaFX88AR6T6m1M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 838,
      "cache_read_input_tokens": 13904,
      "output_tokens": 404,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 838,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 85,
          "output_tokens": 404,
          "cache_read_input_tokens": 13904,
          "cache_creation_input_tokens": 838,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 838
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

_source line 19 · 2026-05-27T15:57:33.309Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Fz2SruTCQgWdRHysSUy1fD`</summary>

```json
{
  "url": "https://openreview.net/search?term=Goedel-Prover-V2",
  "prompt": "Search for the paper \"Goedel-Prover-V2\" on OpenReview. Extract any reviewer comments, scores, or discussion if available. If no results found, say so."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7524434-f87d-461e-b58b-cbbe5144d7f2",
  "isSidechain": false,
  "requestId": "req_011CbTMAR8F2hApTz9S9cnif",
  "type": "assistant",
  "uuid": "87d14fa5-312e-4eb9-9b41-cee51550023b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0153bvQhA5WaFX88AR6T6m1M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 838,
      "cache_read_input_tokens": 13904,
      "output_tokens": 404,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 838,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 85,
          "output_tokens": 404,
          "cache_read_input_tokens": 13904,
          "cache_creation_input_tokens": 838,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 838
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

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-27 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "87d14fa5-312e-4eb9-9b41-cee51550023b",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze Goedel-Prover-V2 paper innovation",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc"
}
```

---

### Tool result

_source line 22 · 2026-05-27T15:57:35.576Z_

<details><summary>↩ Tool result · `toolu_01Fz2SruTCQgWdRHysSUy1fD`</summary>

```text
Based on the web page content provided, I cannot find any search results or information about a paper titled "Goedel-Prover-V2." 

The content shown is from OpenReview.net's homepage and navigation menu, which includes general site information, links to venues, and footer details. It does not contain search results or any paper-specific content such as reviewer comments, scores, or discussions.

To find information about "Goedel-Prover-V2," you would need to perform an actual search on the OpenReview platform using their search functionality.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87d14fa5-312e-4eb9-9b41-cee51550023b",
  "isSidechain": false,
  "promptId": "918f738b-eddd-4a71-9661-57e87bd9f8ed",
  "type": "user",
  "uuid": "a0e3ee3f-af77-40b5-bf6c-6496d401fba0",
  "toolUseResult": {
    "bytes": 62238,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the web page content provided, I cannot find any search results or information about a paper titled \"Goedel-Prover-V2.\" \n\nThe content shown is from OpenReview.net's homepage and navigation menu, which includes general site information, links to venues, and footer details. It does not contain search results or any paper-specific content such as reviewer comments, scores, or discussions.\n\nTo find information about \"Goedel-Prover-V2,\" you would need to perform an actual search on the OpenReview platform using their search functionality.",
    "durationMs": 2264,
    "url": "https://openreview.net/search?term=Goedel-Prover-V2"
  },
  "sourceToolAssistantUUID": "87d14fa5-312e-4eb9-9b41-cee51550023b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-27T15:57:46.907Z_

<details><summary>↩ Tool result · `toolu_01HC3PtBdMiN1VMSYawuTfBM`</summary>

```text
# Goedel-Prover-V2: Scaling Formal Theorem Proving

## Overview
This paper presents Goedel-Prover-V2, a system for scaling formal theorem proving in Lean 4 through sophisticated data synthesis and self-correction mechanisms.

## Introduction & Problem Formulation

The authors identify a critical gap in formal theorem proving: while large language models show promise, they struggle with the complexity of formal mathematical reasoning. The paper notes that existing approaches lack systematic methods for generating high-quality training data and improving model performance through iterative refinement.

The motivation centers on three key challenges:
- **Data scarcity**: Limited availability of formal proofs for training
- **Distribution mismatch**: Gap between informal reasoning and formal proof requirements
- **Iterative improvement**: Difficulty in systematically correcting and refining generated proofs

## Methodology

### 1. Scaffolded Data Synthesis

The system employs multi-stage data generation rather than single-pass synthesis:

- **Stage 1**: Generate initial informal proof sketches
- **Stage 2**: Convert sketches to formal specifications with intermediate steps
- **Stage 3**: Create detailed formal proofs with explicit tactic sequences

This scaffolding approach reduces the semantic gap between natural language and formal mathematics, making the learning task more tractable.

### 2. Self-Correction Mechanism

The framework implements an error-aware refinement loop:

- Models generate candidate proofs
- A formal verification engine identifies failures
- Specific error patterns are highlighted
- The model learns to correct common mistakes through annotated examples

This process creates a feedback loop where failed attempts become learning opportunities rather than discarded outputs.

### 3. Model Averaging & Ensemble Methods

Rather than relying on single model outputs, the approach combines:

- Multiple model checkpoints with different training trajectories
- Diverse generation strategies (different temperature settings, beam widths)
- Voting mechanisms for proof verification

This ensemble strategy improves robustness and success rates across benchmark problems.

### 4. Expert Iteration Training

The training procedure alternates between:

- **Expert phase**: Use verified successful proofs to fine-tune the model
- **Exploration phase**: Generate new candidate proofs, identify failures
- **Refinement**: Incorporate corrected examples back into training data

This cycle progressively expands the model's proof repertoire while maintaining accuracy.

### 5. Reinforcement Learning Integration

The system incorporates RL objectives:

- **Reward signal**: Successful proof verification provides immediate feedback
- **Exploration bonus**: Encourages attempting novel proof strategies
- **Trajectory optimization**: Weights paths leading to valid proofs more heavily

## Experiments & Results

### Benchmarks Evaluated

- **miniF2F test set**: Formal mathematics problems from competitions
- **Putnam benchmark**: High-difficulty university-level problems
- **IMO subset**: International Mathematical Olympiad problems adapted to Lean 4

### Key Performance Metrics

The system demonstrates substantial improvements over baseline approaches:

- Achieves approximately 40% solve rate on miniF2F test set
- Shows 25-30% improvement from scaffolded data synthesis alone
- Model averaging contributes 10-15% additional gains
- Self-correction provides 5-8% boost to overall performance

### Ablation Studies

Systematic removal of components reveals:

- **Scaffolding impact**: Reduces proof generation failures by ~30%
- **Self-correction value**: Adds 4-6 percentage points to accuracy
- **Ensemble contribution**: Provides consistent 8-12% improvement
- **RL fine-tuning**: Contributes 3-5% final performance gain

### Baseline Comparisons

The paper compares against:

- Standard supervised fine-tuning on formal proofs
- Tree-search methods without data synthesis
- Single-model approaches without ensemble techniques
- Previous Goedel-Prover-V1 system

Goedel-Prover-V2 consistently outperforms these baselines across all tested benchmarks.

## Technical Implementation Details

### Training Data Construction

The system synthesizes training data through:

- Automatic informal-to-formal conversion pipelines
- Tactic sequence generation using intermediate specifications
- Error annotation from failed verification attempts
- Diverse proof path enumeration for complex theorems

### Model Architecture

- Based on transformer-based language models fine-tuned for Lean 4
- Extended context windows to accommodate longer proofs
- Special tokenization for mathematical symbols and tactic language
- Attention mechanisms optimized for proof structure understanding

### Verification Engine

- Integrates with Lean 4 kernel for proof checking
- Provides structured error messages for failed proofs
- Tracks which tactic sequences lead to dead ends
- Enables targeted training on corrective examples

## Limitations & Future Directions

The authors acknowledge several constraints:

- Performance remains below expert mathematician level on hardest problems
- Computational cost of ensemble methods and RL training is substantial
- Generalization to completely novel problem domains remains challenging
- Some formal proof techniques (advanced induction strategies) require deeper architectural innovations

Future work directions include:

- Extending to other formal systems beyond Lean 4
- Developing more sophisticated proof search heuristics
- Creating hybrid systems combining learning with symbolic proof search
- Scaling to even larger theorem repositories for pre-training

## Conclusion

Goedel-Prover-V2 demonstrates that systematic data synthesis, self-correction, and ensemble methods significantly advance formal theorem proving capabilities. The combination of scaffolded training data and iterative refinement provides a scalable path toward automated mathematical reasoning in formal systems. The work establishes new benchmarks for computational theorem proving while revealing remaining challenges in fully automated mathematical discovery.

[Binary content (application/pdf, 2.3MB) also saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/6db262d6-dcf8-4dbf-b94b-349936024bbc/tool-results/webfetch-1779897452331-d4cutv.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b7524434-f87d-461e-b58b-cbbe5144d7f2",
  "isSidechain": false,
  "promptId": "918f738b-eddd-4a71-9661-57e87bd9f8ed",
  "type": "user",
  "uuid": "9bad8bf1-b9d5-49fd-8669-4b2d17095bf6",
  "toolUseResult": {
    "bytes": 2454445,
    "code": 200,
    "codeText": "OK",
    "result": "# Goedel-Prover-V2: Scaling Formal Theorem Proving\n\n## Overview\nThis paper presents Goedel-Prover-V2, a system for scaling formal theorem proving in Lean 4 through sophisticated data synthesis and self-correction mechanisms.\n\n## Introduction & Problem Formulation\n\nThe authors identify a critical gap in formal theorem proving: while large language models show promise, they struggle with the complexity of formal mathematical reasoning. The paper notes that existing approaches lack systematic methods for generating high-quality training data and improving model performance through iterative refinement.\n\nThe motivation centers on three key challenges:\n- **Data scarcity**: Limited availability of formal proofs for training\n- **Distribution mismatch**: Gap between informal reasoning and formal proof requirements\n- **Iterative improvement**: Difficulty in systematically correcting and refining generated proofs\n\n## Methodology\n\n### 1. Scaffolded Data Synthesis\n\nThe system employs multi-stage data generation rather than single-pass synthesis:\n\n- **Stage 1**: Generate initial informal proof sketches\n- **Stage 2**: Convert sketches to formal specifications with intermediate steps\n- **Stage 3**: Create detailed formal proofs with explicit tactic sequences\n\nThis scaffolding approach reduces the semantic gap between natural language and formal mathematics, making the learning task more tractable.\n\n### 2. Self-Correction Mechanism\n\nThe framework implements an error-aware refinement loop:\n\n- Models generate candidate proofs\n- A formal verification engine identifies failures\n- Specific error patterns are highlighted\n- The model learns to correct common mistakes through annotated examples\n\nThis process creates a feedback loop where failed attempts become learning opportunities rather than discarded outputs.\n\n### 3. Model Averaging & Ensemble Methods\n\nRather than relying on single model outputs, the approach combines:\n\n- Multiple model checkpoints with different training trajectories\n- Diverse generation strategies (different temperature settings, beam widths)\n- Voting mechanisms for proof verification\n\nThis ensemble strategy improves robustness and success rates across benchmark problems.\n\n### 4. Expert Iteration Training\n\nThe training procedure alternates between:\n\n- **Expert phase**: Use verified successful proofs to fine-tune the model\n- **Exploration phase**: Generate new candidate proofs, identify failures\n- **Refinement**: Incorporate corrected examples back into training data\n\nThis cycle progressively expands the model's proof repertoire while maintaining accuracy.\n\n### 5. Reinforcement Learning Integration\n\nThe system incorporates RL objectives:\n\n- **Reward signal**: Successful proof verification provides immediate feedback\n- **Exploration bonus**: Encourages attempting novel proof strategies\n- **Trajectory optimization**: Weights paths leading to valid proofs more heavily\n\n## Experiments & Results\n\n### Benchmarks Evaluated\n\n- **miniF2F test set**: Formal mathematics problems from competitions\n- **Putnam benchmark**: High-difficulty university-level problems\n- **IMO subset**: International Mathematical Olympiad problems adapted to Lean 4\n\n### Key Performance Metrics\n\nThe system demonstrates substantial improvements over baseline approaches:\n\n- Achieves approximately 40% solve rate on miniF2F test set\n- Shows 25-30% improvement from scaffolded data synthesis alone\n- Model averaging contributes 10-15% additional gains\n- Self-correction provides 5-8% boost to overall performance\n\n### Ablation Studies\n\nSystematic removal of components reveals:\n\n- **Scaffolding impact**: Reduces proof generation failures by ~30%\n- **Self-correction value**: Adds 4-6 percentage points to accuracy\n- **Ensemble contribution**: Provides consistent 8-12% improvement\n- **RL fine-tuning**: Contributes 3-5% final performance gain\n\n### Baseline Comparisons\n\nThe paper compares against:\n\n- Standard supervised fine-tuning on formal proofs\n- Tree-search methods without data synthesis\n- Single-model approaches without ensemble techniques\n- Previous Goedel-Prover-V1 system\n\nGoedel-Prover-V2 consistently outperforms these baselines across all tested benchmarks.\n\n## Technical Implementation Details\n\n### Training Data Construction\n\nThe system synthesizes training data through:\n\n- Automatic informal-to-formal conversion pipelines\n- Tactic sequence generation using intermediate specifications\n- Error annotation from failed verification attempts\n- Diverse proof path enumeration for complex theorems\n\n### Model Architecture\n\n- Based on transformer-based language models fine-tuned for Lean 4\n- Extended context windows to accommodate longer proofs\n- Special tokenization for mathematical symbols and tactic language\n- Attention mechanisms optimized for proof structure understanding\n\n### Verification Engine\n\n- Integrates with Lean 4 kernel for proof checking\n- Provides structured error messages for failed proofs\n- Tracks which tactic sequences lead to dead ends\n- Enables targeted training on corrective examples\n\n## Limitations & Future Directions\n\nThe authors acknowledge several constraints:\n\n- Performance remains below expert mathematician level on hardest problems\n- Computational cost of ensemble methods and RL training is substantial\n- Generalization to completely novel problem domains remains challenging\n- Some formal proof techniques (advanced induction strategies) require deeper architectural innovations\n\nFuture work directions include:\n\n- Extending to other formal systems beyond Lean 4\n- Developing more sophisticated proof search heuristics\n- Creating hybrid systems combining learning with symbolic proof search\n- Scaling to even larger theorem repositories for pre-training\n\n## Conclusion\n\nGoedel-Prover-V2 demonstrates that systematic data synthesis, self-correction, and ensemble methods significantly advance formal theorem proving capabilities. The combination of scaffolded training data and iterative refinement provides a scalable path toward automated mathematical reasoning in formal systems. The work establishes new benchmarks for computational theorem proving while revealing remaining challenges in fully automated mathematical discovery.\n\n[Binary content (application/pdf, 2.3MB) also saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/6db262d6-dcf8-4dbf-b94b-349936024bbc/tool-results/webfetch-1779897452331-d4cutv.pdf]",
    "durationMs": 14596,
    "url": "https://arxiv.org/pdf/2508.03613"
  },
  "sourceToolAssistantUUID": "b7524434-f87d-461e-b58b-cbbe5144d7f2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-27T15:57:50.939Z_

<details><summary>Logged reasoning block</summary>

```text
The PDF extraction gave me a somewhat generic summary rather than the actual paper content. The numbers seem off - the paper claims 90.4% on miniF2F at 32B, but the extraction says ~40%. Let me try to get more specific details from the paper. Let me also try fetching from other sources for more precise information.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9bad8bf1-b9d5-49fd-8669-4b2d17095bf6",
  "isSidechain": false,
  "requestId": "req_011CbTMByZAMk4hsSaotytEH",
  "type": "assistant",
  "uuid": "7b4031b4-7d87-4dfd-aaad-cabb852f62e0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019td2Yufa5gnjMaHmK2UeRN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 155,
      "cache_creation_input_tokens": 1886,
      "cache_read_input_tokens": 14742,
      "output_tokens": 746,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1886,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 155,
          "output_tokens": 746,
          "cache_read_input_tokens": 14742,
          "cache_creation_input_tokens": 1886,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1886
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

_source line 25 · 2026-05-27T15:57:51.858Z_

The PDF extraction gave me a high-level summary but some numbers look off (the abstract mentions 90.4% on miniF2F, not 40%). Let me get more precise details from the actual paper content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b4031b4-7d87-4dfd-aaad-cabb852f62e0",
  "isSidechain": false,
  "requestId": "req_011CbTMByZAMk4hsSaotytEH",
  "type": "assistant",
  "uuid": "96536a35-bbee-4d7c-a4a0-cc0785c08fac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019td2Yufa5gnjMaHmK2UeRN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 155,
      "cache_creation_input_tokens": 1886,
      "cache_read_input_tokens": 14742,
      "output_tokens": 746,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1886,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 155,
          "output_tokens": 746,
          "cache_read_input_tokens": 14742,
          "cache_creation_input_tokens": 1886,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1886
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

_source line 26 · 2026-05-27T15:57:59.120Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DMw1qYEQsKUb1NvkHzT7i5`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2508.03613",
  "prompt": "I need EXACT numbers and specific technical details from this paper. Please extract:\n\n1. EXACT benchmark results: What are the precise percentages on miniF2F-test, ProofNet, PutnamBench, and any other benchmarks? For both 8B and 32B models.\n2. How does the 8B model compare to DeepSeek-Prover-V2-671B specifically?\n3. What base models were used (QwQ-32B, DeepSeek, etc.)?\n4. EXACT details of scaffolded data synthesis: How many stages? What exactly is generated at each stage? How many theorems/proofs?\n5. EXACT details of the self-correction mechanism: How does Lean compiler feedback work? How many correction rounds?\n6. EXACT details of model averaging: What checkpoints are merged? What technique (SLERP, linear, etc.)?\n7. Expert iteration details: How many rounds? What was the data pipeline?\n8. RL details: What algorithm (GRPO, PPO, etc.)? What reward signal?\n9. What datasets were used for training data synthesis (Mathlib, etc.)?\n10. Key ablation numbers showing contribution of each component.\n\nGive me the REAL numbers from the paper, not approximations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96536a35-bbee-4d7c-a4a0-cc0785c08fac",
  "isSidechain": false,
  "requestId": "req_011CbTMByZAMk4hsSaotytEH",
  "type": "assistant",
  "uuid": "396333ad-21da-4a65-9697-b57682bcc8d9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019td2Yufa5gnjMaHmK2UeRN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 155,
      "cache_creation_input_tokens": 1886,
      "cache_read_input_tokens": 14742,
      "output_tokens": 746,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1886,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 155,
          "output_tokens": 746,
          "cache_read_input_tokens": 14742,
          "cache_creation_input_tokens": 1886,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1886
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

_source line 27 · 2026-05-27T15:58:03.813Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QJeUvyMXAhCxLZ2tC2RqWw`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2508.03613",
  "prompt": "Extract the Introduction and Related Work sections of this paper verbatim or near-verbatim. I need to understand:\n\n1. What specific gaps in prior work do they identify? What sentences describe the limitations of existing approaches?\n2. How do they position their work relative to DeepSeek-Prover-V2, Kimina-Prover, InternLM-Prover, and other baselines?\n3. What is their stated main contribution — the exact claims they make?\n4. Any discussion of why previous data synthesis approaches were insufficient\n5. The specific motivation for each of their three innovations (scaffolding, self-correction, model averaging)\n6. Their discussion of the \"diversity collapse\" problem in later training stages\n\nPlease be precise and quote directly from the paper where possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "396333ad-21da-4a65-9697-b57682bcc8d9",
  "isSidechain": false,
  "requestId": "req_011CbTMByZAMk4hsSaotytEH",
  "type": "assistant",
  "uuid": "955e55bc-178e-438c-af8d-422cfada3b30",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019td2Yufa5gnjMaHmK2UeRN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 155,
      "cache_creation_input_tokens": 1886,
      "cache_read_input_tokens": 14742,
      "output_tokens": 746,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1886,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 155,
          "output_tokens": 746,
          "cache_read_input_tokens": 14742,
          "cache_creation_input_tokens": 1886,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1886
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

_source line 28 · 2026-05-27T15:58:04.883Z_

<details><summary>↩ Tool result · `toolu_01DMw1qYEQsKUb1NvkHzT7i5`</summary>

```text
I appreciate your detailed request, but I must be transparent: **the PDF content provided is heavily compressed and encoded** (it's the raw PDF object stream data), making it impossible to extract the specific numerical results you're requesting with confidence.

What I can confirm from the metadata:
- **Title**: "Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction"
- **Authors**: 20 researchers including Yong Lin, Danqi Chen, Sanjeev Arora, Chi Jin
- **ArXiv ID**: 2508.03613v1

**Why I cannot provide the specific numbers you need:**

The actual paper content in the provided data is compressed/flattened into stream objects that require decompression. The document structure shows references to figures, tables (caption.1 through caption.22), and citations, but the readable text content where your requested metrics would appear is not accessible in this format.

**What you should do:**

1. Download the PDF directly from [arXiv 2508.03613](https://arxiv.org/abs/2508.03613)
2. Check the GitHub repository referenced: https://github.com/Goedel-LM/Goedel-Prover-V2
3. Look specifically for:
   - Table results on miniF2F-test, ProofNet, PutnamBench
   - Section 4 (typically contains experimental results)
   - Appendix for detailed ablations

I won't guess at numbers when you've explicitly requested exact figures—that would be misleading for your research.

[Binary content (application/pdf, 2.3MB) also saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/6db262d6-dcf8-4dbf-b94b-349936024bbc/tool-results/webfetch-1779897452331-d4cutv.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "396333ad-21da-4a65-9697-b57682bcc8d9",
  "isSidechain": false,
  "promptId": "918f738b-eddd-4a71-9661-57e87bd9f8ed",
  "type": "user",
  "uuid": "8dd7e1ea-1f36-4ed5-8fb0-23621d965007",
  "toolUseResult": {
    "bytes": 2454445,
    "code": 200,
    "codeText": "OK",
    "result": "I appreciate your detailed request, but I must be transparent: **the PDF content provided is heavily compressed and encoded** (it's the raw PDF object stream data), making it impossible to extract the specific numerical results you're requesting with confidence.\n\nWhat I can confirm from the metadata:\n- **Title**: \"Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction\"\n- **Authors**: 20 researchers including Yong Lin, Danqi Chen, Sanjeev Arora, Chi Jin\n- **ArXiv ID**: 2508.03613v1\n\n**Why I cannot provide the specific numbers you need:**\n\nThe actual paper content in the provided data is compressed/flattened into stream objects that require decompression. The document structure shows references to figures, tables (caption.1 through caption.22), and citations, but the readable text content where your requested metrics would appear is not accessible in this format.\n\n**What you should do:**\n\n1. Download the PDF directly from [arXiv 2508.03613](https://arxiv.org/abs/2508.03613)\n2. Check the GitHub repository referenced: https://github.com/Goedel-LM/Goedel-Prover-V2\n3. Look specifically for:\n   - Table results on miniF2F-test, ProofNet, PutnamBench\n   - Section 4 (typically contains experimental results)\n   - Appendix for detailed ablations\n\nI won't guess at numbers when you've explicitly requested exact figures—that would be misleading for your research.\n\n[Binary content (application/pdf, 2.3MB) also saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/6db262d6-dcf8-4dbf-b94b-349936024bbc/tool-results/webfetch-1779897452331-d4cutv.pdf]",
    "durationMs": 5759,
    "url": "https://arxiv.org/pdf/2508.03613"
  },
  "sourceToolAssistantUUID": "396333ad-21da-4a65-9697-b57682bcc8d9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-27T15:58:13.180Z_

<details><summary>↩ Tool result · `toolu_01QJeUvyMXAhCxLZ2tC2RqWw`</summary>

```text
# Analysis of Goedel-Prover-V2 Introduction and Related Work

I cannot extract the Introduction and Related Work sections verbatim from this PDF due to the document's compressed/encoded format in the provided content. The text appears as PDF object streams rather than readable plain text, making direct extraction impractical.

However, I can provide guidance on what you're seeking:

**To access these sections directly, I recommend:**
1. Opening the PDF at https://arxiv.org/abs/2508.03613v1
2. Reading pages 1-3 for Introduction and Related Work
3. Using the paper's table of contents (visible in the PDF outline)

**What the paper appears to address** (based on metadata and structure):
- The title "Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction" indicates three main contributions: scaffolding mechanisms, self-correction techniques, and likely ensemble/averaging approaches
- The author list includes researchers from major AI labs (Google DeepMind, OpenAI affiliates, Princeton)
- The paper compares against recent baselines mentioned in your query (DeepSeek-Prover-V2, Kimina-Prover, etc.)

**For precise quotations and gap analysis**, accessing the rendered PDF directly would be significantly more effective than working from the encoded source material provided. The paper includes a GitHub repository link (https://github.com/Goedel-LM/Goedel-Prover-V2) which may also contain supplementary materials.

Would you like me to help with anything else regarding this research direction?

[Binary content (application/pdf, 2.3MB) also saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/6db262d6-dcf8-4dbf-b94b-349936024bbc/tool-results/webfetch-1779897452331-d4cutv.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "955e55bc-178e-438c-af8d-422cfada3b30",
  "isSidechain": false,
  "promptId": "918f738b-eddd-4a71-9661-57e87bd9f8ed",
  "type": "user",
  "uuid": "d09a5668-a048-4c4e-a29f-ebb95c1b82d9",
  "toolUseResult": {
    "bytes": 2454445,
    "code": 200,
    "codeText": "OK",
    "result": "# Analysis of Goedel-Prover-V2 Introduction and Related Work\n\nI cannot extract the Introduction and Related Work sections verbatim from this PDF due to the document's compressed/encoded format in the provided content. The text appears as PDF object streams rather than readable plain text, making direct extraction impractical.\n\nHowever, I can provide guidance on what you're seeking:\n\n**To access these sections directly, I recommend:**\n1. Opening the PDF at https://arxiv.org/abs/2508.03613v1\n2. Reading pages 1-3 for Introduction and Related Work\n3. Using the paper's table of contents (visible in the PDF outline)\n\n**What the paper appears to address** (based on metadata and structure):\n- The title \"Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction\" indicates three main contributions: scaffolding mechanisms, self-correction techniques, and likely ensemble/averaging approaches\n- The author list includes researchers from major AI labs (Google DeepMind, OpenAI affiliates, Princeton)\n- The paper compares against recent baselines mentioned in your query (DeepSeek-Prover-V2, Kimina-Prover, etc.)\n\n**For precise quotations and gap analysis**, accessing the rendered PDF directly would be significantly more effective than working from the encoded source material provided. The paper includes a GitHub repository link (https://github.com/Goedel-LM/Goedel-Prover-V2) which may also contain supplementary materials.\n\nWould you like me to help with anything else regarding this research direction?\n\n[Binary content (application/pdf, 2.3MB) also saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/6db262d6-dcf8-4dbf-b94b-349936024bbc/tool-results/webfetch-1779897452331-d4cutv.pdf]",
    "durationMs": 9363,
    "url": "https://arxiv.org/pdf/2508.03613"
  },
  "sourceToolAssistantUUID": "955e55bc-178e-438c-af8d-422cfada3b30",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-27T15:58:13.184Z_

```json
{
  "parentUuid": "d09a5668-a048-4c4e-a29f-ebb95c1b82d9",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "8756fab4-7bbe-4531-bcd2-040fe915c068",
  "timestamp": "2026-05-27T15:58:13.184Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 31 · 2026-05-27T15:58:20.351Z_

<details><summary>Logged reasoning block</summary>

```text
The PDF extraction isn't working well. Let me try alternative approaches - maybe the GitHub repo README or other blog posts about this paper can give me more precise details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8756fab4-7bbe-4531-bcd2-040fe915c068",
  "isSidechain": false,
  "requestId": "req_011CbTMDutTHsCmPkrAQSVGX",
  "type": "assistant",
  "uuid": "a6468953-b4d5-4a2e-8044-e66b82e78beb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GL9hYgvKzkHzmHdvZ6fTcu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1959,
      "cache_read_input_tokens": 16628,
      "output_tokens": 426,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1959,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 426,
          "cache_read_input_tokens": 16628,
          "cache_creation_input_tokens": 1959,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1959
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

_source line 32 · 2026-05-27T15:58:20.705Z_

The PDF isn't extracting well. Let me try alternative sources for the detailed content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6468953-b4d5-4a2e-8044-e66b82e78beb",
  "isSidechain": false,
  "requestId": "req_011CbTMDutTHsCmPkrAQSVGX",
  "type": "assistant",
  "uuid": "b6ab6384-86cb-474e-ab1c-a3674ab90226",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GL9hYgvKzkHzmHdvZ6fTcu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1959,
      "cache_read_input_tokens": 16628,
      "output_tokens": 426,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1959,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 426,
          "cache_read_input_tokens": 16628,
          "cache_creation_input_tokens": 1959,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1959
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

_source line 33 · 2026-05-27T15:58:24.013Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AFcw2jKfkHmXw6S8UbZb7v`</summary>

```json
{
  "url": "https://github.com/Goedel-LM/Goedel-Prover-V2",
  "prompt": "Extract ALL content from this GitHub README for Goedel-Prover-V2. I need:\n1. All benchmark results and comparison tables\n2. Technical details of the method (scaffolded data synthesis, self-correction, model averaging)\n3. Training details (base models, datasets, number of training iterations)\n4. Any specific numbers about performance on miniF2F, ProofNet, PutnamBench\n5. How the 8B model compares to DeepSeek-Prover-V2-671B\n6. Links to model weights or training data\n\nBe comprehensive - extract everything available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6ab6384-86cb-474e-ab1c-a3674ab90226",
  "isSidechain": false,
  "requestId": "req_011CbTMDutTHsCmPkrAQSVGX",
  "type": "assistant",
  "uuid": "8da5a5f7-c2eb-4835-9cfe-453734531749",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GL9hYgvKzkHzmHdvZ6fTcu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1959,
      "cache_read_input_tokens": 16628,
      "output_tokens": 426,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1959,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 426,
          "cache_read_input_tokens": 16628,
          "cache_creation_input_tokens": 1959,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1959
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

_source line 34 · 2026-05-27T15:58:25.406Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Tq8krFT3t8xgN1SnQrexGw`</summary>

```json
{
  "url": "https://huggingface.co/papers/2508.03613",
  "prompt": "Extract all content about the paper \"Goedel-Prover-V2\" from this Hugging Face papers page. I need:\n1. The full abstract\n2. Any community discussion or comments\n3. Any key results mentioned\n4. Links to models or datasets\nBe comprehensive."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8da5a5f7-c2eb-4835-9cfe-453734531749",
  "isSidechain": false,
  "requestId": "req_011CbTMDutTHsCmPkrAQSVGX",
  "type": "assistant",
  "uuid": "9aa0d3e3-ff8c-4aeb-b753-b503fb38a700",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GL9hYgvKzkHzmHdvZ6fTcu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1959,
      "cache_read_input_tokens": 16628,
      "output_tokens": 426,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1959,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 426,
          "cache_read_input_tokens": 16628,
          "cache_creation_input_tokens": 1959,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1959
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

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-27 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "9aa0d3e3-ff8c-4aeb-b753-b503fb38a700",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze Goedel-Prover-V2 paper innovation",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc"
}
```

---

### Tool result

_source line 37 · 2026-05-27T15:58:26.090Z_

<details><summary>↩ Tool result · `toolu_01Tq8krFT3t8xgN1SnQrexGw`</summary>

```text
&lt;persisted-output>
Output too large (77.8KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/6db262d6-dcf8-4dbf-b94b-349936024bbc/tool-results/toolu_01Tq8krFT3t8xgN1SnQrexGw.txt

Preview (first 2KB):
# GOEDEL-PROVER-V2: SCALING FORMAL THEOREM PROVING WITH SCAFFOLDED DATA SYNTHESIS AND SELF-CORRECTION

Yong Lin&lt;sup>1\*&lt;/sup>, Shange Tang&lt;sup>1 2\*&lt;/sup>, Bohan Lyu&lt;sup>3\*&lt;/sup>, Ziran Yang&lt;sup>1\*&lt;/sup>, Jui-Hui Chung&lt;sup>1\*&lt;/sup>,  
 Haoyu Zhao&lt;sup>1\*&lt;/sup>, Lai Jiang&lt;sup>7\*&lt;/sup>, Yihan Geng&lt;sup>8\*&lt;/sup>, Jiawei Ge&lt;sup>1&lt;/sup>, Jingruo Sun&lt;sup>4&lt;/sup>,  
 Jiayun Wu&lt;sup>3&lt;/sup>, Jiri Gesi&lt;sup>6 †&lt;/sup>, Ximing Lu&lt;sup>2&lt;/sup>, David Acuna&lt;sup>2&lt;/sup>, Kaiyu Yang&lt;sup>5 ‡&lt;/sup>,  
 Hongzhou Lin&lt;sup>6 \*†&lt;/sup>, Yejin Choi&lt;sup>2 4&lt;/sup>, Danqi Chen&lt;sup>1&lt;/sup>, Sanjeev Arora&lt;sup>1&lt;/sup>, Chi Jin&lt;sup>1\*&lt;/sup>

&lt;sup>1&lt;/sup>Princeton Language and Intelligence, Princeton University &lt;sup>2&lt;/sup>NVIDIA  
&lt;sup>3&lt;/sup>Tsinghua University &lt;sup>4&lt;/sup>Stanford University &lt;sup>5&lt;/sup>Meta FAIR &lt;sup>6&lt;/sup>Amazon  
&lt;sup>7&lt;/sup>Shanghai Jiao Tong University &lt;sup>8&lt;/sup>Peking University

## ABSTRACT

We introduce Goedel-Prover-V2, a series of open-source language models that set a new state-of-the-art in automated theorem proving. Built on the standard expert iteration and reinforcement learning pipeline, our approach incorporates three key innovations: (1) Scaffolded data synthesis: We generate synthetic tasks of increasing difficulty to train the model to master increasingly complex theorems; (2) Verifier-guided self-correction: We enable the model to iteratively revise its proofs by leveraging feedback from the Lean compiler; (3) Model averaging: We merge model checkpoints to mitigate the decrease in model output diversity in later stages of training. Our small model, Goedel-Prover-V2-8B, reaches 84.6% pass@32 on MiniF2F and outperforms DeepSeek-Prover-V2-671B under the same metric, despite being 80X smaller. Our flagship model, Goedel-Prover-V2-32B, achieves 88.1% on MiniF2F at pass@32 in standard mode and 90.4% in self-correction mode, outperforming prior SOTA by a large margin. Additionally, our flagship model solves 86 problems on PutnamBench at pass@184, securing th
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```````json
{
  "recorded_role": "user",
  "parentUuid": "9aa0d3e3-ff8c-4aeb-b753-b503fb38a700",
  "isSidechain": false,
  "promptId": "918f738b-eddd-4a71-9661-57e87bd9f8ed",
  "type": "user",
  "uuid": "1289f6dd-4d2d-4df9-b4f1-4158a26a626b",
  "toolUseResult": {
    "bytes": 79897,
    "code": 200,
    "codeText": "OK",
    "result": "# GOEDEL-PROVER-V2: SCALING FORMAL THEOREM PROVING WITH SCAFFOLDED DATA SYNTHESIS AND SELF-CORRECTION\n\nYong Lin&lt;sup>1\\*&lt;/sup>, Shange Tang&lt;sup>1 2\\*&lt;/sup>, Bohan Lyu&lt;sup>3\\*&lt;/sup>, Ziran Yang&lt;sup>1\\*&lt;/sup>, Jui-Hui Chung&lt;sup>1\\*&lt;/sup>,  \n Haoyu Zhao&lt;sup>1\\*&lt;/sup>, Lai Jiang&lt;sup>7\\*&lt;/sup>, Yihan Geng&lt;sup>8\\*&lt;/sup>, Jiawei Ge&lt;sup>1&lt;/sup>, Jingruo Sun&lt;sup>4&lt;/sup>,  \n Jiayun Wu&lt;sup>3&lt;/sup>, Jiri Gesi&lt;sup>6 †&lt;/sup>, Ximing Lu&lt;sup>2&lt;/sup>, David Acuna&lt;sup>2&lt;/sup>, Kaiyu Yang&lt;sup>5 ‡&lt;/sup>,  \n Hongzhou Lin&lt;sup>6 \\*†&lt;/sup>, Yejin Choi&lt;sup>2 4&lt;/sup>, Danqi Chen&lt;sup>1&lt;/sup>, Sanjeev Arora&lt;sup>1&lt;/sup>, Chi Jin&lt;sup>1\\*&lt;/sup>\n\n&lt;sup>1&lt;/sup>Princeton Language and Intelligence, Princeton University &lt;sup>2&lt;/sup>NVIDIA  \n&lt;sup>3&lt;/sup>Tsinghua University &lt;sup>4&lt;/sup>Stanford University &lt;sup>5&lt;/sup>Meta FAIR &lt;sup>6&lt;/sup>Amazon  \n&lt;sup>7&lt;/sup>Shanghai Jiao Tong University &lt;sup>8&lt;/sup>Peking University\n\n## ABSTRACT\n\nWe introduce Goedel-Prover-V2, a series of open-source language models that set a new state-of-the-art in automated theorem proving. Built on the standard expert iteration and reinforcement learning pipeline, our approach incorporates three key innovations: (1) Scaffolded data synthesis: We generate synthetic tasks of increasing difficulty to train the model to master increasingly complex theorems; (2) Verifier-guided self-correction: We enable the model to iteratively revise its proofs by leveraging feedback from the Lean compiler; (3) Model averaging: We merge model checkpoints to mitigate the decrease in model output diversity in later stages of training. Our small model, Goedel-Prover-V2-8B, reaches 84.6% pass@32 on MiniF2F and outperforms DeepSeek-Prover-V2-671B under the same metric, despite being 80X smaller. Our flagship model, Goedel-Prover-V2-32B, achieves 88.1% on MiniF2F at pass@32 in standard mode and 90.4% in self-correction mode, outperforming prior SOTA by a large margin. Additionally, our flagship model solves 86 problems on PutnamBench at pass@184, securing the first place among open-source models on the leaderboard, surpassing DeepSeek-Prover-V2-671B’s record of solving 47 problems by pass@1024 with a significantly smaller model size and compute budget. At the time of its release (July–August 2025), Goedel-Prover-V2 achieves the strongest overall performance among all open-source theorem provers. It also ranks among the top-performing models—including closed-source systems with publicly reported performance—under a constrained test-time compute budget. Our models, code, and data are released at &lt;https://github.com/Goedel-LM/Goedel-Prover-V2>.\n\n## 1 INTRODUCTION\n\nAutomated theorem proving (ATP) is a grand challenge for AI, requiring the construction of step-by-step, machine-verifiable proofs in formal languages like Lean (De Moura et al., 2015; Moura & Ullrich, 2021). Unlike reasoning in natural language, ATP demands a completely rigorous logical flow, which poses an exceptional challenge for AI systems. The field has advanced rapidly in recent years; for example, DeepMind’s AlphaProof (Google DeepMind, 2024) and AlphaGeometry (Trinh et al., 2024; Chervonyi et al., 2025) demonstrated that AI systems are capable of achieving IMO (International Math Olympiad) medal-level performance. Furthermore, open-source efforts such as DeepSeek-Prover-V2 (Ren et al., 2025) and Kimina-Prover (Wang et al., 2025) have achieved impressive results on benchmarks like MiniF2F (Zheng et al., 2021) and PutnamBench (Tsoukalas et al., 2024), demonstrating the effectiveness of leveraging the reasoning ability of LLMs through\n\n\\*Core Contributor.\n\n†This work is independent of and outside of the work at Amazon.\n\n‡All experiments and data processing were conducted outside Meta.Figure 1: Performance of Goedel-Prover-V2 on different benchmarks under pass@32.\n\nchain-of-thoughts. These successes, however, typically depend on massive models (e.g., DeepSeek-Prover-V2 has 671B parameters) or computationally intensive inference (e.g., the concurrent work Seed-Prover (Chen et al., 2025)), which involves complex search algorithms and enormous search budgets.\n\nIn this work we introduce Goedel-Prover-V2, a new series of open-source models for automated theorem proving in Lean that establish a new state-of-the-art in both performance and computational efficiency. The models are capable of generating whole proof and leveraging verifier feedback for iterative self-correction. Our flagship 32B model achieves 88.1% pass@32 on the MiniF2F benchmark, improving to 90.4% with self-correction. This performance surpasses both the concurrent 72B Kimina-Prover and the previous SOTA 671B DeepSeek-Prover-V2, while using significantly fewer parameters (Figure 1). On the more challenging PutnamBench, our model solves 44 problems (57 with self-correction), more than doubling the number solved by DeepSeek-Prover-V2 under the same metric. The efficiency of our approach is further underscored by our 8B model, which alone outperforms the 671B DeepSeek-Prover-V2 on MiniF2F despite being nearly 80 times smaller. At the time of its release (July–August 2025), Goedel-Prover-V2 achieves the strongest overall performance among all open-source theorem provers. It also ranks among the top-performing models—including closed-source systems with publicly reported performance—under small test-time compute budgets.\n\nThe key to these gains lies in novel design across the framework, data, and training pipelines. We highlight the main components below:\n\n- • **Verifier-guided self-correction:** Framework-wise, we incorporate feedback from the Lean compiler (verifier) into the model input to enable the error-correction ability of our theorem prover (*verifier-guided self-correction*). While correcting errors based on verifier feedback has been studied in theorem proving (First et al., 2023) and coding (Olausson et al., 2024; Chen et al., 2024; Bouzenia et al., 2024), we further incorporate this into models that generate long chain-of-thought (CoT) reasoning, which is effective for complex reasoning tasks such as ATP (Jaech et al., 2024; Guo et al., 2025; Wang et al., 2025; Ren et al., 2025).\n- • **Scaffolded data synthesis:** Successfully combining long CoT with verifier-guided error correction requires special efforts on curating data. In addition to formalizing existing math problems and curating data for error correction, we augment our training statement set through *scaffolded data synthesis*. This technique creates math problems at an appropriate difficulty level to provide the model with better learning signals.\n- • **Model averaging:** Our training recipe extends beyond standard expert iteration and reinforcement learning. We also apply *model averaging* (Wortsman et al., 2022b) to mitigate the decrease in model output diversity that can occur in the later stages of training.\n\nOverall, our results demonstrate that the frontier of formal theorem proving can be advanced without access to extremely large models, a vast computational resources, or proprietary technology. We hopethat our open-source theorem prover series, Goedel-Prover-V2, will enable the community to build upon them and accelerate progress toward AI systems that can reliably solve and verify complex mathematical problems, and ultimately bridge the long-standing divide between intuitive human reasoning and formal proof verification.\n\nThe following paper is organized as follows: in Section 2, we introduce our main methods to train Goedel-Prover-V2, including the verifier-guided self-correction framework (Section 2.1), scaffolded data synthesis (Section 2.2), and the training pipeline (Section 2.3). In Section 3, we present the evaluation results on Goedel-Prover-V2, including evaluation on both standard and our curated benchmarks (Section 3.3), scaling behavior under different test-time budgets (Section 3.4), and a study of reinforcement learning and model averaging (Section 3.6). Finally, we review the previous works (Section 4) and discuss the connection with Goedel-Prover-V2.\n\n## 2 METHOD\n\nIn this section, we present our method in detail. We start with the key framework innovation compared to the previous vanilla whole-proof generation methods (e.g. DeepSeek-Prover-V2) by utilizing the feedback from the Lean compiler to guide the proof-correction procedure (Section 2.1). Then, in Section 2.2, we demonstrate how to curate the training data (statements), with an emphasis on augmenting the data through scaffolded data synthesis. Based on the curated data, we present the details of training our theorem prover in Section 2.3, which includes supervised fine-tuning (SFT), reinforcement learning (RL), and model averaging. Section 2.4 provides a summary of the overall framework.\n\n### 2.1 CHAIN-OF-THOUGHT AND SELF-CORRECTION\n\nPrevailing paradigms for whole-proof generation in automated theorem proving have largely been “end-to-end,” where a model generates a complete formal proof from a theorem statement in a single pass (Xin et al., 2024b; Lin et al., 2025; Dong & Ma, 2025). Recent work has significantly advanced this approach by leveraging the long-chain-of-thought reasoning capabilities of large models (Wang et al., 2025; Ren et al., 2025).\n\nA key distinction between informal and formal proof generation lies in the availability and utilization of compilation (verification) feedback from proof assistants like Lean or Coq. Humans naturally leverage such feedback to iteratively revise their proofs. Recent works have shown that integrating the verifier’s error messages or tactic verification outcomes into proof generation significantly improves synthesis accuracy (First et al., 2023).\n\nOur framework formalizes this intuition by explicitly incorporating verifier feedback within the whole-proof generation loop. We structure the pipeline so that, after an initial proof attempt, verification failures are parsed and communicated back into the model as corrective guidance. The model then generates proof repairs, leading to an iterative self-correction process.\n\n### 2.2 CURATING FORMAL STATEMENTS\n\nIn this part, we detail our methods for curating a large, high-quality dataset of Lean 4 statements, which is essential for expert iteration and RL in formal theorem proving. We start with the formalizer training, which is the core of translating existing math problems written in natural language into Lean statements. We then present our scaffolded data synthesis pipeline that creates math problems at an appropriate difficulty level, which includes a lightweight formal-based method that utilizes the Lean system, and an informal-based system for large-scale data augmentation.\n\n**Formalizer Training.** Existing Lean datasets (e.g., Goedel-Pset-v1) contain many low-quality problems—human evaluation on a sampled subset shows that over 80% of unsolved problems are incorrectly formalized. This highlights the need for stronger formalizers. We train our formalizer using the standard expert iteration pipeline, which combines Lean syn-\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Name&lt;/th>\n&lt;th>Pass&lt;/th>\n&lt;th>Failed&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Kimina-autoformalizer&lt;/td>\n&lt;td>161&lt;/td>\n&lt;td>139&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Godel-Formalizer-V2&lt;/td>\n&lt;td>228&lt;/td>\n&lt;td>72&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nTable 1: Comparison of different formalizers on 300 Omni-math problems.Figure 2: Our **informal-based scaffolded data synthesis pipeline** with three parts: (1) informal statement generation; (2) formalization and quality checking; and (3) negation and difficulty filtering.\n\ntax checks and semantic evaluation via LLMs to assess translation quality. Only statements that pass both checks are included in the next iteration of SFT. Details of the LLM semantic evaluation prompt are provided in Appendix C.\n\nTo initialize expert iteration, we prompt Claude Sonnet 4 to generate 50K formalized statements, along with corresponding reasoning traces. Incorporating reasoning capability enables our formalizer to outperform previous models such as Goedel-Formalizer-V1 and Kimina-Autoformalizer, which lack this feature.\n\nWe evaluate our model Goedel-Formalizer-V2 and Kimina-Autoformalizer on a benchmark of 300 OmniMath problems. Results are shown in Table 1.\n\n**Formal-based scaffolded data synthesis.** When the prover fails to find a proof for a challenging problem, we can still leverage the proof attempt to generate simpler, related problems. The intuition is that even an incorrect proof attempt may introduce valid subgoals that represent easier subproblems. We utilize a powerful tactic in Lean, `extract_goal`, to capture the unsolved states of a proof. These extracted goals (together with the preconditions), which are well-formed mathematical statements, are then used to augment our training data for the next phase. Since an extracted statement is not guaranteed to be provable, we also include its negation, thereby training the model to recognize both true and false propositions.\n\n**Informal-based scaffolded data synthesis.** Another way of scaffolded data synthesis is to leverage the current LLMs’ mathematical reasoning ability in natural language, to create math statements at the right level for the model to learn. For a given problem, we prompt an LLM (Qwen3-32B) to generate simpler/sub-problems if it is unsolved, or harder variants if it is already solved. To improve generation quality, we first have the LLM attempt a natural language solution to the original problem, using its output as context. The generated informal statements are then formalized into Lean by the formalization pipeline we described in **Formalizer Training**. To avoid the inference overhead of incorrect or trivial statements, we use an LLM-based filter that assesses each statement for correctness and difficulty, where trivial or mathematically incorrect statements are discarded (the negation of incorrect statements are also added to the dataset). This filtering process significantly accelerates data synthesis, with a minor trade-off in potentially discarding some valid statements due to LLM judgment errors. The prompts and further details are in Appendix D.\n\n### 2.3 TRAINING ALGORITHMS\n\n**Supervised fine-tuning and expert iteration.** We follow the standard pipeline of Expert Iteration by iterating between using the model to conduct large-scale inference on the statement sets, collectingThe diagram illustrates the model training pipeline. It starts with a **Formal Statement** box. From this box, three paths emerge:\n \n\n- An orange arrow labeled **Distill** leads to a box labeled **Deepseek-Prover-V2-7B/671B**.\n- An orange arrow labeled **Scaffolded Data Synthesis** leads to **Dataset S&lt;sub>3&lt;/sub>**.\n- An orange arrow labeled **Self-Correct** leads to a box labeled **Deepseek-Prover-V2-671B**.\n\n From the **Deepseek-Prover-V2-7B/671B** box, an orange arrow labeled **Distill** leads to **Dataset S&lt;sub>1&lt;/sub>**. From the **Deepseek-Prover-V2-671B** box, an orange arrow labeled **Self-Correct** leads to **Corrected Proof**. A dashed arrow points from **Corrected Proof** to **Dataset S&lt;sub>2&lt;/sub>**.\n   \n The training stages are represented by blue boxes:\n \n\n- **SFT-S&lt;sub>1&lt;/sub>** receives an orange arrow from **Dataset S&lt;sub>1&lt;/sub>** and a blue arrow labeled **SFT** from **Dataset S&lt;sub>1&lt;/sub>**.\n- **SFT-S&lt;sub>2&lt;/sub>-AVG** receives an orange arrow from **Dataset S&lt;sub>2&lt;/sub>** and a blue arrow labeled **SFT+AVG** from **Dataset S&lt;sub>2&lt;/sub>**.\n- **SFT-S&lt;sub>3&lt;/sub>-AVG** receives an orange arrow from **Dataset S&lt;sub>3&lt;/sub>** and a blue arrow labeled **SFT+AVG** from **Dataset S&lt;sub>3&lt;/sub>**.\n- **RL+AVG** receives a blue arrow labeled **RL+AVG** from **SFT-S&lt;sub>2&lt;/sub>-AVG** and a blue arrow labeled **RL+AVG** from **SFT-S&lt;sub>3&lt;/sub>-AVG**.\n\n Dashed arrows also indicate a flow from **Dataset S&lt;sub>1&lt;/sub>** to **Dataset S&lt;sub>2&lt;/sub>** and from **Dataset S&lt;sub>2&lt;/sub>** to **Dataset S&lt;sub>3&lt;/sub>**.\n\nFigure 3: The overall workflow of model training. “+AVG” denotes that the trained model is averaged with the base model after training. “RL+AVG” is the final output model. Detailed descriptions are provided in Section 2.4.\n\ncorrect proofs with reasoning traces, and fine-tuning the model further by Supervised Fine-tuning (SFT) on the collected samples.\n\n**Reinforcement learning.** We aim to train a model capable of generating complete proofs and correcting its own errors via verifier-guided self-correction. To this end, we adopt an efficient hybrid strategy. We first sample multiple complete proofs in parallel. For each sampled proof, we perform serial self-correction, generating one correction per round. This serial correction process aligns well with RL, which optimizes expected reward and has been shown to improve single-shot (pass@1) accuracy (Shao et al., 2024; Yue et al., 2025).\n\nOur RL implementation adopts a multi-task setup (illustrated in Appendix Figure 9): 50% of the inputs are used for whole proof generation, and the remaining 50% for first-round self-correction. We train for a single epoch, using approximately 46K and 67K unique inputs for the 8B and 32B models, respectively. On the algorithmic side, we use a hybrid GRPO-based approach (Shao et al., 2024). Compared to vanilla GRPO, our method removes group normalization as suggested by Dr.GRPO (Liu et al., 2025) to avoid inherent bias on length, incorporates clip-higher, overlong penalties, and dynamic sampling from DAPO (Yu et al., 2025), and excludes the KL regularization term from the objective to encourage exploration. A key observation is that question difficulty significantly impacts RL training. To address this, we modify the dynamic sampling strategy to only include problems with pass rates in the range  $(0, 0.75]$  during optimization. For further implementation details, see Appendix E.1.\n\n**Model averaging for enhanced diversity.** We observed that in the later stages of SFT and RL, the model’s diversity decreases. This is reflected by an increase in pass@1 but a decline in pass@N for larger values of N, such as N=32. We adopt model averaging to enhance model diversity (Wortsman et al., 2022b;a; Lin et al., 2023a;b; Dang et al., 2025). Specifically, let the parameters of the base model be denoted as  $\\theta_0$ , and those of the fine-tuned model as  $\\theta$ . We use the combined model parameters defined as  $(1 - \\alpha)\\theta_0 + \\alpha\\theta$ , where  $\\alpha \\in (0, 1)$ . Existing literature has demonstrated that this simple approach can significantly improve the feature diversity of the final model. Our observations also confirm that this method effectively enhances pass@N. We perform model averaging at each stage of the process. Specifically, we apply model averaging after completing SFT and use the averaged model as the starting point for RL. Once RL is completed, we perform model averaging again and use this averaged model as the final model.\n\n## 2.4 WHOLE PIPELINE: PUTTING EVERYTHING TOGETHER\n\nThe pipeline consists of the following steps:\n\n- • We utilize Deepseek-Prover-V2-7B and Deepseek-Prover-V2-671B to perform large-scale inference, producing an initial supervised fine-tuning (SFT) dataset  $S_1$  for complete proof generation.- • We employ  $S_1$  to conduct SFT on both Qwen3-8B and Qwen3-32B, resulting in fine-tuned models SFT- $S_1$  for both the 8B and 32B variants&lt;sup>1&lt;/sup>.\n- • Using SFT- $S_1$  and Deepseek-Prover-V2-671B, we annotate self-correction data. The self-correction data from Deepseek-Prover-V2-671B is inferred using NeMo-Skills&lt;sup>2&lt;/sup> with 144 H100s. This data is then incorporated back into  $S_1$  to create an enhanced dataset  $S_2$ . We subsequently perform SFT on both model sizes using  $S_2$ , yielding improved models SFT- $S_2$ . We perform model averaging between SFT- $S_2$  and the base model for both the 8B and 32B models, resulting in SFT- $S_2$ -AVG.\n- • We perform scaffolded data synthesis with SFT- $S_2$ -AVG to generate the dataset  $S_3$ . Continuing the SFT process, we further improve the models by training SFT- $S_2$ -AVG on  $S_3$ , yielding SFT- $S_3$ , and subsequently obtain the averaged model SFT- $S_3$ -AVG.\n- • We apply reinforcement learning to the SFT- $S_3$ -AVG and conduct model averaging and obtain the final model RL-AVG.\n\nThe overall workflow is illustrated in Fig. 3.\n\n### 3 EVALUATION\n\nThis section presents our experiment results on Goedel-Prover-V2. We first discuss our evaluation benchmarks (Section 3.1). Then, we discuss our main evaluation results on the selected benchmarks (Section 3.3), and correspondingly the scaling behavior (Section 3.4). Finally, we investigate the performance of reinforcement learning and model averaging (Section 3.6).\n\n#### 3.1 BENCHMARKS\n\n**MiniF2F.** MiniF2F (Zheng et al., 2021) consists of 488 problem statements (244 validation and 244 test problems) in Lean. The problems are drawn from high-school level competitions including the AMC, AIME, and the International Mathematical Olympiad (IMO). We use the version of MiniF2F provided by Kimina (Wang et al., 2025)&lt;sup>3&lt;/sup>, which has some incorrect statements fixed.\n\n**PutnamBench.** PutnamBench (Tsoukalas et al., 2024) focuses on college-level mathematics competition problems that are sourced from the William Lowell Putnam Mathematical Competition years 1962 - 2023. PutnamBench comprises 644 problems, covering algebra, analysis, number theory, geometry, combinatorics, probability, and set theory.\n\n**MathOlympiadBench.** We constructed MathOlympiadBench, which comprises 360 human-verified formalizations of Olympiad-level mathematical problems, sourced from Compfiles&lt;sup>4&lt;/sup> and IMOSLLearn4 repository&lt;sup>5&lt;/sup>. It contains 158 IMO problems from 1959 to 2024, 131 IMO shortlist problems covering 2006 to 2023, 68 national mathematical Olympiad problems, and 3 additional mathematical puzzles. The statistic of problem categories in MathOlympiadBench is presented in Figure 4, and Figure 5 visualizes humans’ formalizing and solving status of IMO problems in MathOlympiadBench. See Appendix A for more details of MathOlympiadBench and its comparison with MiniF2F.\n\n#### 3.2 EVALUATED METHODS\n\nFollowing previous works (Xin et al., 2024b; Lin et al., 2025; Dong & Ma, 2025; Ren et al., 2025) the evaluations are done under Lean 4.9.0-rc1. For the first round of whole-proof generation, the max token length of the model is set to be 30,000. For the verifier-guided error-correction, we sequentially conduct 2 additional rounds of self-correction, given the verifier’s feedback on the previous attempt. The total number of tokens in the self-correction mode is set to be 40,000. We report the pass@N metric.\n\n&lt;sup>1&lt;/sup>We use &lt;https://github.com/hiyouga/LLaMA-Factory> for SFT.\n\n&lt;sup>2&lt;/sup>&lt;https://github.com/NVIDIA/NeMo-Skills>\n\n&lt;sup>3&lt;/sup>[https://huggingface.co/datasets/AI-MO/minif2f\\\\_test](https://huggingface.co/datasets/AI-MO/minif2f_test)\n\n&lt;sup>4&lt;/sup>&lt;https://dwrensha.github.io/compfiles/imo.html>\n\n&lt;sup>5&lt;/sup>&lt;https://github.com/mortarsanjaya/IMOSLLearn4>Figure 4: Distribution of problems in MathOlympiadBench by category.\n\nFigure 5: Community’s achievement on IMO problems by year and problem index. Each cell represents a problem:  $\\square$  statement not formalized,  $\\blacksquare$  not solved, and  $\\blacksquare$  solved.\n\n### 3.3 MAIN RESULTS\n\nTable 2: Performance of different whole-proof generation methods on MiniF2F test split.  $\\dagger$  denotes concurrent work\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Method&lt;/th>\n&lt;th>Budget&lt;/th>\n&lt;th>Performance&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Goedel-Prover-SFT (Lin et al., 2025)&lt;/td>\n&lt;td>32&lt;br/>3200&lt;/td>\n&lt;td>&lt;math>57.6\\% \\pm 0.7\\%&lt;/math>&lt;br/>62.7%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>STP (Dong &amp; Ma, 2025)&lt;/td>\n&lt;td>128&lt;br/>3200&lt;br/>25600&lt;/td>\n&lt;td>&lt;math>61.2\\% \\pm 0.6\\%&lt;/math>&lt;br/>&lt;math>65.0\\% \\pm 0.5\\%&lt;/math>&lt;br/>67.6%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Kimina-Prover-Preview-72B (Wang et al., 2025)&lt;/td>\n&lt;td>32&lt;br/>8192&lt;/td>\n&lt;td>68.85%&lt;br/>80.74%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepSeek-Prover-V2-7B (Ren et al., 2025)&lt;/td>\n&lt;td>32&lt;br/>8192&lt;/td>\n&lt;td>&lt;math>75.6\\% \\pm 0.5\\%&lt;/math>&lt;br/>82.0%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepSeek-Prover-V2-671B&lt;/td>\n&lt;td>32&lt;br/>8192&lt;/td>\n&lt;td>&lt;math>82.4\\% \\pm 0.6\\%&lt;/math>&lt;br/>88.9%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Kimina-Prover-8B&lt;math>^\\dagger&lt;/math> (Wang et al., 2025)&lt;/td>\n&lt;td>32&lt;/td>\n&lt;td>78.3%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Kimina-Prover-70B&lt;math>^\\dagger&lt;/math>&lt;/td>\n&lt;td>32&lt;br/>1024&lt;/td>\n&lt;td>84.0%&lt;br/>87.7%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>w/ TTRL&lt;/td>\n&lt;td>unknown&lt;/td>\n&lt;td>92.2%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Goedel-Prover-V2-8B&lt;/td>\n&lt;td>32&lt;br/>1024&lt;br/>8192&lt;/td>\n&lt;td>&lt;math>84.6\\% \\pm 0.6\\%&lt;/math>&lt;br/>87.9%&lt;br/>90.2%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>w/ self-correction&lt;/td>\n&lt;td>32&lt;br/>1024&lt;/td>\n&lt;td>&lt;math>86.7\\% \\pm 0.2\\%&lt;/math>&lt;br/>89.3%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Goedel-Prover-V2-32B&lt;/td>\n&lt;td>32&lt;br/>1024&lt;br/>8192&lt;/td>\n&lt;td>&lt;math>88.1\\% \\pm 0.8\\%&lt;/math>&lt;br/>91.8%&lt;br/>92.2%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>w/ self-correction&lt;/td>\n&lt;td>32&lt;br/>1024&lt;/td>\n&lt;td>&lt;math>90.4\\% \\pm 0.6\\%&lt;/math>&lt;br/>92.6%&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nThe evaluation results of Goedel-Prover-V2 on MiniF2F are summarized in Table 2, and results on PutnamBench are shown in Table 3. The results for MathOlympiadBench are presented in the rightmost figure of Figure 1. Below, we summarize and discuss the results.\n\n**High performance at modest scale.** Our 32B model achieves pass@32 accuracy of 88.1% on MiniF2F, with 90.4% after 2 rounds of error-correction, exceeding the previous state-of-the-art DeepSeek-Prover-V2-671B’s 82.4% while using far fewer parameters. Even the 8B variant achieves84.6%, nearly matching or outperforming Kimina-Prover-70B’s results under the same inference budget, and outperforming the previous SOTA DeepSeek-Prover-V2-671B on MiniF2F, with a significant smaller model size. On PutnamBench, our 32B model solves 43 problems under pass@32, nearly doubling the DeepSeek-Prover-V2-671B model’s performance under the same budget. With error-correction, Goedel-Prover-V2-32B solves 57 problems under pass@32, outperforming DeepSeek-Prover-V2-671B under pass@1024. Under pass@184 and error correction, Goedel-Prover-V2-32B solves 86 on PutnamBench, securing the best open-source theorem prover on the leaderboard.\n\nTable 3: Comparison of different models on PutnamBench. Our Goedel-Prover-V2 with compiler-guided self-correction solves 86 problems from PutnamBench, improving the previous SOTA (DeepSeek-Prover-V2) by 39 more problems, and securing the best open-source model on the leaderboard.\\*\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>#&lt;/th>\n&lt;th>Model&lt;/th>\n&lt;th>num-solved&lt;/th>\n&lt;th>open-source&lt;/th>\n&lt;th>compute&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>1&lt;/td>\n&lt;td>&lt;b>Godel-Prover-V2 (self-correction mode)&lt;/b>&lt;/td>\n&lt;td>86&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>pass@184&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>1&lt;/td>\n&lt;td>&lt;b>Godel-Prover-V2 (self-correction mode)&lt;/b>&lt;/td>\n&lt;td>57&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>pass@32&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>1&lt;/td>\n&lt;td>&lt;b>Godel-Prover-V2&lt;/b>&lt;/td>\n&lt;td>43&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>pass@32&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>2&lt;/td>\n&lt;td>DeepSeek-Prover-V2&lt;/td>\n&lt;td>47&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>pass@1024&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>2&lt;/td>\n&lt;td>DeepSeek-Prover-V2&lt;/td>\n&lt;td>22&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>pass@32&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>3&lt;/td>\n&lt;td>DSP+&lt;/td>\n&lt;td>23&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>pass@128&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>4&lt;/td>\n&lt;td>Bourbaki&lt;/td>\n&lt;td>14&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>pass@512&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>5&lt;/td>\n&lt;td>Kimina-Prover-7B-Distill&lt;/td>\n&lt;td>10&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>pass@192&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>6&lt;/td>\n&lt;td>Self-play Theorem Prover&lt;/td>\n&lt;td>8&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>pass@3200&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>7&lt;/td>\n&lt;td>Godel-Prover-SFT&lt;/td>\n&lt;td>7&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>pass@512&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>8&lt;/td>\n&lt;td>ABEL&lt;/td>\n&lt;td>7&lt;/td>\n&lt;td>×&lt;/td>\n&lt;td>pass@596&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n\\* A concurrent work, Seed Prover (Chen et al., 2025), successfully solved 331 problems on PutnamBench. However, the prover is not open-source, and it is not clear what the computational budget is at test time (which is expected to be much larger than ours).\n\n**Efficacy of verifier-guided self-correction.** Adding self-correction provides a consistent gain of approximately 2 percentage points in pass@32 for both models on MiniF2F. On PutnamBench, error correction leads to 14 more solves under pass@32. This demonstrates that integrating Lean compiler feedback into a long-chain-of-thought revision pipeline enables the model to identify errors and repair them effectively.\n\n**Sample-efficient inference.** Unlike prior models such as Kimina-Prover and DeepSeek-Prover-V2, which rely heavily on large sampling budgets or test-time reinforcement learning to reach peak accuracy, Goedel-Prover-V2 attains very high pass@N with minimal inference overhead (N=32 or 64), indicating that the model internalizes powerful reasoning strategies during training. The sample efficiency, together with the relatively small size, makes Goedel-Prover-V2 series a very good candidate for the community to develop new algorithms and test on different benchmarks.\n\n### 3.4 SCALING ANALYSIS\n\nFigure 6 and Table 4 illustrate the scaling behavior of Goedel-Prover-V2 (8B and 32B variants) across different inference budgets, compared against DeepSeek-Prover-V2 (7B and 671B) and Kimina-Prover-72B. At the lower sampling regime (pass@32), Goedel-Prover-V2-32B already achieves 88.1%, notably surpassing DeepSeek-Prover-V2-671B (82.4%) and Kimina-Prover-72B (84.0%). This advantage persists across inference budgets, with our self-correction mode providing approximately a 2-point performance improvement under pass@32 and pass@64, peaking at 92.6% at pass@8192. The smaller 8B model also demonstrates strong scalability, surpassing the 671B DeepSeek model at all budgets.\n\nFigure 6: Scaling behavior on MiniF2F test split.&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Model&lt;/th>\n&lt;th>32&lt;/th>\n&lt;th>64&lt;/th>\n&lt;th>128&lt;/th>\n&lt;th>256&lt;/th>\n&lt;th>512&lt;/th>\n&lt;th>1024&lt;/th>\n&lt;th>2048&lt;/th>\n&lt;th>4096&lt;/th>\n&lt;th>8192&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>32B (self-correction mode)&lt;/td>\n&lt;td>90.4&lt;/td>\n&lt;td>91.4&lt;/td>\n&lt;td>91.9&lt;/td>\n&lt;td>92.3&lt;/td>\n&lt;td>92.4&lt;/td>\n&lt;td>92.6&lt;/td>\n&lt;td>—&lt;/td>\n&lt;td>—&lt;/td>\n&lt;td>—&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>32B&lt;/td>\n&lt;td>88.1&lt;/td>\n&lt;td>89.8&lt;/td>\n&lt;td>90.5&lt;/td>\n&lt;td>91.0&lt;/td>\n&lt;td>91.6&lt;/td>\n&lt;td>91.8&lt;/td>\n&lt;td>92.0&lt;/td>\n&lt;td>92.2&lt;/td>\n&lt;td>92.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>8B (self-correction mode)&lt;/td>\n&lt;td>86.7&lt;/td>\n&lt;td>86.9&lt;/td>\n&lt;td>87.4&lt;/td>\n&lt;td>88.0&lt;/td>\n&lt;td>88.5&lt;/td>\n&lt;td>89.3&lt;/td>\n&lt;td>—&lt;/td>\n&lt;td>—&lt;/td>\n&lt;td>—&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>8B&lt;/td>\n&lt;td>84.6&lt;/td>\n&lt;td>86.1&lt;/td>\n&lt;td>86.5&lt;/td>\n&lt;td>87.0&lt;/td>\n&lt;td>87.4&lt;/td>\n&lt;td>87.9&lt;/td>\n&lt;td>88.5&lt;/td>\n&lt;td>89.3&lt;/td>\n&lt;td>90.2&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nTable 4: The performance (%) of Goedel-Prover-V2 on MiniF2F across different compute budget.\n\nThese results indicate that Goedel-Prover-V2 efficiently internalizes reasoning during training, requiring fewer inference samples to achieve comparable or superior accuracy. Furthermore, the consistent gains from verifier-guided self-correction across all inference budgets further underscore the value of combining error correction with long-chain-of-thought reasoning in formal theorem proving.\n\n### 3.5 ANALYSIS OF SELF-CORRECTION\n\nIn our main experiments, self-correction was conducted for a maximum of 2 rounds with a 40k token context length. To further explore its capabilities, we used YaRN (Peng et al., 2024) to extend the context length to 128k tokens and allowed up to 5 revision iterations. We conducted a series of experiments on the MiniF2F benchmark at pass@32, the results of which are presented in Figure 7. Alongside our standard prompting setup (Self Correction), we performed two ablation studies: (1) removing the specific compiler error messages (w/o Error Messages), and (2) removing the chain-of-thought from previous attempts, retaining only the formal proof (w/o Previous CoTs).\n\nFigure 7: Ablation study on self-correction with extended context length and revision iterations on the MiniF2F test split at pass@32.\n\nThe results show that removing compiler feedback significantly lowers performance, confirming that specific error messages are crucial for effective revision. Similarly, removing the reasoning from previous attempts also slightly degrades performance, indicating that retaining the chain-of-thought from prior rounds is beneficial. Furthermore, with an extended context and more revision iterations, the full self-correction model’s pass@32 accuracy on MiniF2F reaches an average of 92.7%, which surpasses the 92.2% performance of the model without self-correction at pass@8192, highlighting the sample efficiency of our iterative revision process.\n\n### 3.6 RL AND MODEL AVERAGING\n\nWe systematically evaluate the impact of RL steps and model averaging strategies on the performance of Goedel-Prover-V2. Specifically, for RL checkpoints at steps 60, 80, and 90, we apply model averaging with coefficients  $\\alpha = 0.6, 0.7, 0.8, 0.9$  (where  $\\alpha$  is the weight of the base model). We assess each averaged model in both vanilla (whole-proof generation) and correction (with self-correction) settings, evaluating both pass@1 and pass@N, as visualized in Figure 8.\n\nFor both vanilla and correction settings, pass@1 consistently increases as the number of RL steps grows. For vanilla pass@N, performance stabilizes at higher RL steps, whereas in the correction setting, pass@N continues to improve. This indicates that correction benefits more from RL, likely due to the shortage of high-quality self-correction data in the SFT stages.\n\nExamining different values of  $\\alpha$ , we observe that a higher proportion of the base model (i.e., lower  $\\alpha$ ) leads to lower pass@1, but pass@N first rises and then falls as  $\\alpha$  increases. There exists an optimal model averaging ratio that maximizes pass@N. This trend holds for both vanilla and correction settings, with the improvement being more pronounced for correction. This suggests that model averaging not only improves sample diversity but also amplifies the benefits of RL-driven self-correction.Figure 8: The effects of varying RL steps and model averaging ratios on the pass@1 and pass@32 performance of models, both with and without correction.\n\n## 4 RELATED WORKS\n\n**Formal Theorem Proving as Whole Proof Generation.** Inspired by the success of end-to-end reasoning in informal LLMs, recent foundational work in formal theorem proving has adopted a similar strategy: generating entire Lean proofs in a single pass. While informal reasoning models often struggle with step verification—producing fluent yet logically flawed arguments (Petrov et al., 2025)—formal settings like Lean (De Moura et al., 2015) offer a precise and executable verifier that enforces correctness. Leveraging this, models such as DeepSeek-Prover (Xin et al., 2024a), Goedel Prover (Lin et al., 2025), and Kimina Prover (Wang et al., 2025) demonstrate that end-to-end generation can produce formally verified proofs that are immediately checkable by the Lean proof assistant. This paradigm retains the global coherence and simplicity of sequence generation while grounding outputs in verifiable formal logic.\n\n**Formal Theorem Proving using Proof Search.** In contrast to end-to-end generation, proof search-based methods guide the model to incrementally construct proofs by exploring derivation paths with verifier feedback at each step. Recent systems such as InternLM2.5-StepProver (Wu et al., 2024), Hunyuan Prover (Li et al., 2024), DeepSeek-Prover v1.5 (Xin et al., 2024b), and BFS Prover (Xin et al., 2025) employ tree search algorithms—such as Monte Carlo Tree Search or breadth-first search—to explore multiple proof trajectories and iteratively assemble valid proofs. While this strategy improves correctness, it comes at the cost of significantly higher computational overhead, as the model must evaluate and verify a large number of partial branches. Recently, hybrid methods, which use a general-purpose (strong) LLM to write the proof sketch and query theorem provers to fill in the proof for small steps, also emerged (DSP+ (Cao et al., 2025) and the concurrent work Delta-Prover (Zhou et al., 2025)). However, these works usually require the LLM to be very large and powerful, where DSP+ uses 671B DeepSeek-R1 (Guo et al., 2025) or DeepSeek-V3 (Liu et al., 2024), and Delta-Prover uses Gemini (Comanici et al., 2025). Notably, Seed-Prover (Chen et al., 2025) employs a wide range of techniques, including extensive test-time search and refinement, and achieves IMO medal-level performance. However, it requires substantial computational resources.\n\n**Self-Repair and Verifier-Guided Refinement.** While tree-based proof search improves correctness, its high computational cost has motivated the development of more efficient mechanisms for guiding search and enabling self-refinement. One direction explores how auxiliary signals or intermediate structures can streamline the reasoning process. Jiang et al. (2023); Gloeckle et al. (2024); Cao et al. (2025) bridge informal and formal reasoning by using informal sketches as a skeleton for formal proof generation, while Yang et al. (2024) employs retrieval-augmented generation (RAG) to retrieve relevant theorems from formal libraries during proof construction. Other approaches, such as Ji et al. (2025), implement self-verification and iterative refinement loops, allowing models to autonomously revise candidate proofs using verifier feedback.\n\nVerifier-in-the-loop strategies in recent works (Baba et al., 2025; Zhou et al., 2025; Ren et al., 2025; Wang et al., 2025; Chen et al., 2025), also highlight the benefits of interactive feedback, improving success rates through iterative correction rather than brute-force search. These methods collectivelypoint to a more flexible and scalable paradigm: enabling the model to diagnose and repair its own outputs with minimal external supervision.\n\nGoedel-Prover-V2 builds on this trajectory by adopting a self-revision framework, where the model iteratively proposes and refines candidate proofs until they satisfy the Lean checker. This architecture draws inspiration from general-purpose self-repair frameworks in coding and reasoning (Yao et al., 2023; Shinn et al., 2023; First et al., 2023; Olausson et al., 2024; Chen et al., 2024; Bouzenia et al., 2024), bringing their iterative refinement loop into the domain of formal mathematics with long chain-of-thought reasoning.\n\n## 5 CONCLUSION AND DISCUSSION\n\nIn this work, we introduced **Goedel-Prover-V2**, a series of state-of-the-art open-source theorem provers that significantly advance automated formal proof generation. Our key innovation is the integration of long-chain-of-thought reasoning with compiler-guided self-correction, addressing a crucial gap overlooked by prior methods. Through scaffolded data synthesis, SFT and RL training, and model averaging, our models achieve state-of-the-art performance among open-source provers. In particular, our 32B model achieves 88.1% on MiniF2F at pass@32 and benefits further from self-correction and reaching 90.4% on MiniF2F at pass@32, outperforming larger models with lower inference cost. Moreover, our 8B model also outperforms the previous SOTA DeepSeek-Prover-V2-671B under pass@32 on MiniF2F with a significant smaller model size.\n\nWe also investigate a proof repair strategy as a test-time alternative to standard pass@k sampling. Instead of regenerating an entire failed proof, our method corrects only the faulty segment. We use Lean 4’s compiler feedback and the `extract_goal` tactic to isolate the unsolved subgoal, prompt the prover to solve it independently, and then reinsert the correct solution into the original proof. On the MiniF2F benchmark, this approach improves the amortized budget scaling curve by 1–2 percentage points, highlighting inference-time scaling strategies as a key direction for future work.\n\nBy open-sourcing all trained models, we aim to catalyze further advancements in formal reasoning research. We envision that the release of Goedel-Prover-V2 will not only establish a new benchmark for automated theorem proving but also provide a practical, efficient platform upon which future innovations can be built.\n\n## ACKNOWLEDGEMENT\n\nThis project was the result of a close collaborative effort by all authors, and every major component benefited from joint discussion and iteration. The author would like to thank Igor Gitman for support with the curation of self-correction data.\n\nHZ and SA acknowledge the support from Schmidt, Darpa, ONR, and NSF. CJ acknowledges the support from NSF-OAC-2411299, NSF-IIS-2239297, and Princeton AI Lab Seed Fund.\n\n## REFERENCES\n\nKaito Baba, Chaoran Liu, Shuhei Kurita, and Akiyoshi Sannai. Prover agent: An agent-based framework for formal mathematical proofs. *arXiv preprint arXiv:2506.19923*, 2025.\n\nIslem Bouzenia, Premkumar Devanbu, and Michael Pradel. Repairagent: An autonomous, llm-based agent for program repair. *arXiv preprint arXiv:2403.17134*, 2024.\n\nChenrui Cao, Liangcheng Song, Zenan Li, Xinyi Le, Xian Zhang, Hui Xue, and Fan Yang. Reviving dsp for advanced theorem proving in the era of reasoning models. *arXiv preprint arXiv:2506.11487*, 2025.\n\nLuoxin Chen, Jinming Gu, Liankai Huang, Wenhao Huang, Zhicheng Jiang, Allan Jie, Xiaoran Jin, Xing Jin, Chenggang Li, Kaijing Ma, Cheng Ren, Jiawei Shen, Wenlei Shi, Tong Sun, He Sun, Jiahui Wang, Siran Wang, Zhihong Wang, Chenrui Wei, Shufa Wei, Yonghui Wu, Yuchen Wu, Yihang Xia, Huajian Xin, Fan Yang, Huaiyuan Ying, Hongyi Yuan, Zheng Yuan, Tianyang Zhan, Chi Zhang, Yue Zhang, Ge Zhang, Tianyun Zhao, Jianqiu Zhao, Yichi Zhou, and Thomas HanwenZhu. Seed-prover: Deep and broad reasoning for automated theorem proving, 2025. URL &lt;https://arxiv.org/abs/2507.23726>.\n\nXinyun Chen, Maxwell Lin, Nathanael Schärli, and Denny Zhou. Teaching large language models to self-debug. In *The Twelfth International Conference on Learning Representations*, 2024.\n\nYuri Chervonyi, Trieu H Trinh, Miroslav Olšák, Xiaomeng Yang, Hoang Nguyen, Marcelo Menegali, Junehyuk Jung, Vikas Verma, Quoc V Le, and Thang Luong. Gold-medalist performance in solving olympiad geometry with AlphaGeometry2. *arXiv preprint arXiv:2502.03544*, 2025.\n\nGheorghe Comanici, Eric Bieber, Mike Schaeckermann, Ice Pasupat, Noveen Sachdeva, Inderjit Dhillon, Marcel Blstein, Ori Ram, Dan Zhang, Evan Rosen, et al. Gemini 2.5: Pushing the frontier with advanced reasoning, multimodality, long context, and next generation agentic capabilities. *arXiv preprint arXiv:2507.06261*, 2025.\n\nXingyu Dang, Christina Baek, J Zico Kolter, and Aditi Raghunathan. Assessing diversity collapse in reasoning. In *Scaling Self-Improving Foundation Models without Human Supervision*, 2025.\n\nLeonardo De Moura, Soonho Kong, Jeremy Avigad, Floris Van Doorn, and Jakob von Raumer. The lean theorem prover (system description). In *Automated Deduction-CADE-25: 25th International Conference on Automated Deduction, Berlin, Germany, August 1-7, 2015, Proceedings 25*, pp. 378–388. Springer, 2015.\n\nKefan Dong and Tengyu Ma. STP: Self-play LLM theorem provers with iterative conjecturing and proving. In *International Conference on Machine Learning (ICML)*, 2025.\n\nEmily First, Markus N Rabe, Talia Ringer, and Yuriy Brun. Baldur: Whole-proof generation and repair with large language models. In *ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering (ESEC/FSE)*, 2023.\n\nFabian Gloeckle, Jannis Limperg, Gabriel Synnaeve, and Amaury Hayat. Abel: Sample efficient online reinforcement learning for neural theorem proving. In *The 4th Workshop on Mathematical Reasoning and AI at NeurIPS'24*, 2024.\n\nGoogle DeepMind. AI achieves silver-medal standard solving international mathematical olympiad problems. &lt;https://deepmind.google/discover/blog/ai-solves-imo-problems-at-silver-medal-level/>, 2024.\n\nDaya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. *arXiv preprint arXiv:2501.12948*, 2025.\n\nAaron Jaech, Adam Kalai, Adam Lerer, Adam Richardson, Ahmed El-Kishky, Aiden Low, Alec Helyar, Aleksander Madry, Alex Beutel, Alex Carney, et al. Openai o1 system card. *arXiv preprint arXiv:2412.16720*, 2024.\n\nXingguang Ji, Yahui Liu, Qi Wang, Jingyuan Zhang, Yang Yue, Rui Shi, Chenxi Sun, Fuzheng Zhang, Guorui Zhou, and Kun Gai. Leanabell-prover-v2: Verifier-integrated reasoning for formal theorem proving via reinforcement learning. *arXiv preprint arXiv:2507.08649*, 2025.\n\nAlbert Qiaochu Jiang, Sean Welleck, Jin Peng Zhou, Timothee Lacroix, Jiacheng Liu, Wenda Li, Mateja Jamnik, Guillaume Lample, and Yuhuai Wu. Draft, sketch, and prove: Guiding formal theorem provers with informal proofs. In *The Eleventh International Conference on Learning Representations*, 2023.\n\nYang Li, Dong Du, Linfeng Song, Chen Li, Weikang Wang, Tao Yang, and Haitao Mi. Hunyuanprover: A scalable data synthesis framework and guided tree search for automated theorem proving. *arXiv preprint arXiv:2412.20735*, 2024.\n\nYong Lin, Hangyu Lin, Wei Xiong, Shizhe Diao, Jianmeng Liu, Jipeng Zhang, Rui Pan, Haoxiang Wang, Wenbin Hu, Hanning Zhang, et al. Mitigating the alignment tax of rlhf. *arXiv preprint arXiv:2309.06256*, 2023a.Yong Lin, Lu Tan, Yifan Hao, Honam Wong, Hanze Dong, Weizhong Zhang, Yujiu Yang, and Tong Zhang. Spurious feature diversification improves out-of-distribution generalization. *arXiv preprint arXiv:2309.17230*, 2023b.\n\nYong Lin, Shange Tang, Bohan Lyu, Jiayun Wu, Hongzhou Lin, Kaiyu Yang, Jia Li, Mengzhou Xia, Danqi Chen, Sanjeev Arora, et al. Goedel-Prover: A frontier model for open-source automated theorem proving. *arXiv preprint arXiv:2502.07640*, 2025.\n\nAixin Liu, Bei Feng, Bing Xue, Bingxuan Wang, Bochao Wu, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chenyu Zhang, Chong Ruan, et al. Deepseek-v3 technical report. *arXiv preprint arXiv:2412.19437*, 2024.\n\nZichen Liu, Changyu Chen, Wenjun Li, Penghui Qi, Tianyu Pang, Chao Du, Wee Sun Lee, and Min Lin. Understanding r1-zero-like training: A critical perspective. *arXiv preprint arXiv:2503.20783*, 2025.\n\nLeonardo de Moura and Sebastian Ullrich. The Lean 4 theorem prover and programming language. In *International Conference on Automated Deduction (CADE)*, 2021.\n\nTheo X. Olausson, Jeevana Priya Inala, Chenglong Wang, Jianfeng Gao, and Armando Solar-Lezama. Is self-repair a silver bullet for code generation? In *The Twelfth International Conference on Learning Representations*, 2024.\n\nBowen Peng, Jeffrey Quesnelle, Honglu Fan, and Enrico Shippole. YaRN: Efficient context window extension of large language models. In *The Twelfth International Conference on Learning Representations*, 2024. URL &lt;https://openreview.net/forum?id=wHBfxhZulu>.\n\nIvo Petrov, Jasper Dekoninck, Lyuben Baltadzhiev, Maria Drencheva, Kristian Minchev, Mislav Balunović, Nikola Jovanović, and Martin Vechev. Proof or bluff? evaluating llms on 2025 usa math olympiad. *arXiv preprint arXiv:2503.21934*, 2025.\n\nZZ Ren, Zhihong Shao, Junxiao Song, Huajian Xin, Haocheng Wang, Wanjia Zhao, Liyue Zhang, Zhe Fu, Qihao Zhu, Dejian Yang, et al. Deepseek-prover-v2: Advancing formal mathematical reasoning via reinforcement learning for subgoal decomposition. *arXiv preprint arXiv:2504.21801*, 2025.\n\nZhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li, Y Wu, et al. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. *arXiv preprint arXiv:2402.03300*, 2024.\n\nGuangming Sheng, Chi Zhang, Zilingfeng Ye, Xibin Wu, Wang Zhang, Ru Zhang, Yanghua Peng, Haibin Lin, and Chuan Wu. Hybridflow: A flexible and efficient rlhf framework. *arXiv preprint arXiv: 2409.19256*, 2024.\n\nNoah Shinn, Federico Cassano, Ashwin Gopinath, Karthik R Narasimhan, and Shunyu Yao. Reflexion: language agents with verbal reinforcement learning. In *Thirty-seventh Conference on Neural Information Processing Systems*, 2023.\n\nTrieu H Trinh, Yuhuai Wu, Quoc V Le, He He, and Thang Luong. Solving olympiad geometry without human demonstrations. *Nature*, 625(7995):476–482, 2024.\n\nGeorge Tsoukalas, Jasper Lee, John Jennings, Jimmy Xin, Michelle Ding, Michael Jennings, Amitayush Thakur, and Swarat Chaudhuri. Putnambench: Evaluating neural theorem-provers on the putnam mathematical competition. *arXiv preprint arXiv:2407.11214*, 2024.\n\nHaiming Wang, Mert Unsal, Xiaohan Lin, Mantas Baksys, Junqi Liu, Marco Dos Santos, Flood Sung, Marina Vinyes, Zhenzhe Ying, Zekai Zhu, et al. Kimina-prover preview: Towards large formal reasoning models with reinforcement learning. *arXiv preprint arXiv:2504.11354*, 2025.\n\nMitchell Wortsman, Gabriel Ilharco, Samir Ya Gadre, Rebecca Roelofs, Raphael Gontijo-Lopes, Ari S Morcos, Hongseok Namkoong, Ali Farhadi, Yair Carmon, Simon Kornblith, et al. Model soups: averaging weights of multiple fine-tuned models improves accuracy without increasing inference time. In *International conference on machine learning*, pp. 23965–23998. PMLR, 2022a.Mitchell Wortsman, Gabriel Ilharco, Jong Wook Kim, Mike Li, Simon Kornblith, Rebecca Roelofs, Raphael Gontijo Lopes, Hannaneh Hajishirzi, Ali Farhadi, Hongseok Namkoong, et al. Robust fine-tuning of zero-shot models. In *Proceedings of the IEEE/CVF conference on computer vision and pattern recognition*, pp. 7959–7971, 2022b.\n\nZijian Wu, Suozhi Huang, Zhejian Zhou, Huaiyuan Ying, Jiayu Wang, Dahua Lin, and Kai Chen. InternLM2.5-StepProver: Advancing automated theorem proving via expert iteration on large-scale lean problems. *arXiv preprint arXiv:2410.15700*, 2024.\n\nHuajian Xin, Daya Guo, Zhihong Shao, Zhizhou Ren, Qihao Zhu, Bo Liu, Chong Ruan, Wenda Li, and Xiaodan Liang. Deepseek-prover: Advancing theorem proving in llms through large-scale synthetic data. *arXiv preprint arXiv:2405.14333*, 2024a.\n\nHuajian Xin, ZZ Ren, Junxiao Song, Zhihong Shao, Wanjia Zhao, Haocheng Wang, Bo Liu, Liyue Zhang, Xuan Lu, Qiushi Du, et al. Deepseek-prover-v1.5: Harnessing proof assistant feedback for reinforcement learning and monte-carlo tree search. *arXiv preprint arXiv:2408.08152*, 2024b.\n\nRan Xin, Chenguang Xi, Jie Yang, Feng Chen, Hang Wu, Xia Xiao, Yifan Sun, Shen Zheng, and Ming Ding. BFS-prover: Scalable best-first tree search for LLM-based automatic theorem proving. In *Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics*, 2025.\n\nKaiyu Yang, Aidan Swope, Alex Gu, Rahul Chalamala, Peiyang Song, Shixing Yu, Saad Godil, Ryan J Prenger, and Animashree Anandkumar. Leandojo: Theorem proving with retrieval-augmented language models. *Advances in Neural Information Processing Systems*, 36, 2024.\n\nShunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, and Karthik R Narasimhan. Tree of thoughts: Deliberate problem solving with large language models. In *Thirty-seventh Conference on Neural Information Processing Systems*, 2023.\n\nQiyong Yu, Zheng Zhang, Ruofei Zhu, Yufeng Yuan, Xiaochen Zuo, Yu Yue, Weinan Dai, Tiantian Fan, Gaohong Liu, Lingjun Liu, et al. Dapo: An open-source llm reinforcement learning system at scale. *arXiv preprint arXiv:2503.14476*, 2025.\n\nYang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Shiji Song, and Gao Huang. Does reinforcement learning really incentivize reasoning capacity in llms beyond the base model? *arXiv preprint arXiv:2504.13837*, 2025.\n\nKunhao Zheng, Jesse Michael Han, and Stanislas Polu. Minif2f: a cross-system benchmark for formal olympiad-level mathematics. *arXiv preprint arXiv:2109.00110*, 2021.\n\nYichi Zhou, Jianqiu Zhao, Yongxin Zhang, Bohan Wang, Siran Wang, Luoxin Chen, Jiahui Wang, Haowei Chen, Allan Jie, Xinbo Zhang, et al. Solving formal math problems by decomposition and iterative reflection. *arXiv preprint arXiv:2507.15225*, 2025.APPENDIXA DETAILS OF MATHOLYMPIADBENCH\n\nMathOlympiadBench is human-processed to eliminate several issues presented in the source problems: 1. incomplete problem statements, 2. distribution across multiple files, 3. multiple theorems per problem, and 4. incompatibility with the commonly used Mathlib. The verification process ensures that each problem contains exactly one formal theorem with its corresponding informal statement, and confirms that all formal statements can pass the compilation with the `sorry` tactic.\n\nWe compared the IMO problems shared between MathOlympiadBench and MiniF2F, and identified at least 3 cases in MiniF2F exhibiting issues such as: 1. the formal statement to be proved is strictly weaker than the informal statement, and 2. the formal statement does not match the informal statement. Notably, similar issues are not observed for these problems in MathOlympiadBench.\n\nIn the following, we present three case studies comparing the problem formalizations in MiniF2F and MathOlympiadBench.\n\nA.1 IMO 1981, PROBLEM 6: SPECIFIC VALUE VS. GENERAL FORMULA\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>MiniF2F&lt;/th>\n&lt;th>MathOlympiadBench&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>\n&lt;pre>1 /--\n2 The function &lt;math>f(x,y)&lt;/math> satisfies\n3\n4 (1) &lt;math>f(0,y) = y + 1&lt;/math>,\n5\n6 (2) &lt;math>f(x+1,0) = f(x,1)&lt;/math>,\n7\n8 (3) &lt;math>f(x+1,y+1) = f(x,f(x+1,y))&lt;/math>,\n9\n10 for all non-negative integers &lt;math>x,y&lt;/math>\n11 . Determine &lt;math>f(4,1981)&lt;/math>.\n12 -/\n13 theorem imo_1981_p6 (f : &lt;math>\\mathbb{N} \\rightarrow \\mathbb{N} \\rightarrow&lt;/math>\n14 &lt;math>\\mathbb{N}&lt;/math>)\n15 (h0 : &lt;math>\\forall y, f\\ 0\\ y = y + 1&lt;/math>)\n16 (h1 : &lt;math>\\forall x, f\\ (x + 1)\\ 0 = f\\ x\\ 1&lt;/math>)\n17 (h2 : &lt;math>\\forall x\\ y, f\\ (x + 1)\\ (y + 1) =&lt;/math>\n18 &lt;math>f\\ x\\ (f\\ (x + 1)\\ y)) :\n19 &lt;math>\\forall y, f\\ 4\\ (y + 1) = 2 \\wedge (f\\ 4\\ y +&lt;/math>\n20 &lt;math>3) - 3 := by&lt;/math>&lt;/math>&lt;/pre>\n&lt;/td>\n&lt;td>\n&lt;pre>1 /-!\n2 # International Mathematical\n3   Olympiad 1981, Problem 6\n4\n5 Suppose that &lt;math>f : \\mathbb{N} \\times \\mathbb{N} \\rightarrow \\mathbb{N}&lt;/math>\n6 satisfies\n7\n8 1) &lt;math>f\\ (0, y) = y + 1&lt;/math>\n9 2) &lt;math>f\\ (x + 1, 0) = f\\ (x, 1)&lt;/math>,\n10 3) &lt;math>f\\ (x + 1, y + 1) = f\\ (x, f\\ (x&lt;/math>\n11 &lt;math>+ 1, y))&lt;/math>\n12\n13 for all &lt;math>x\\ y \\in \\mathbb{N}&lt;/math>.\n14\n15 Determine &lt;math>f\\ (4, 1981)&lt;/math>.\n16 -/\n17\n18 def no_eval (x : &lt;math>\\mathbb{N}&lt;/math>) : &lt;math>\\mathbb{N} := x&lt;/math>\n19 abbrev solution_value : &lt;math>\\mathbb{N} :=&lt;/math>\n20 no_eval ((2^·)^[1984] 1 - 3)\n21\n22 theorem imo1981_p6 (f : &lt;math>\\mathbb{N} \\rightarrow \\mathbb{N} \\rightarrow&lt;/math>\n23 &lt;math>\\mathbb{N}&lt;/math>)\n24 (h1 : &lt;math>\\forall y, f\\ 0\\ y = y + 1&lt;/math>)\n25 (h2 : &lt;math>\\forall x, f\\ (x + 1)\\ 0 = f\\ x\\ 1&lt;/math>)\n26 (h3 : &lt;math>\\forall x\\ y, f\\ (x + 1)\\ (y + 1) =&lt;/math>\n27 &lt;math>f\\ x\\ (f\\ (x + 1)\\ y)) :\n28 f\\ 4\\ 1981 = solution_value :=\n29 sorry&lt;/math>&lt;/pre>\n&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nThe informal statement requires computing the exact value of  $f(4, 1981)$ , a specific number. However, the MiniF2F formalization only asks to prove a general recurrence relation, which is an intermediate step in the solution process. This discrepancy can make the formal proof substantially easier than solving the original problem. In contrast, MathOlympiadBench faithfully translates the original problem into formal language, requiring the proof of the final numerical value as demanded by the IMO statement.A.2 IMO 1983, PROBLEM 6: INCOMPLETE VS. FULL CONDITION\n\n```\n\nMiniF2F\n1  /-- Let a, b and c be the lengths\n2  of the sides of a triangle.\n3  Prove that\n4\n5  a^2b(a-b) + b^2c(b-c) + c^2a(c-a) ≥ 0.\n6\n7  Determine when equality occurs.\n8  -/\n9\n10 theorem imo_1983_p6 (a b c : ℝ)\n11   (h0 : 0 < a ∧ 0 < b ∧ 0 < c)\n12   (h1 : c < a + b) (h2 : b < a +\n13   c)\n14   (h3 : a < b + c) :\n15   0 ≤ a^2*b*(a-b) + b^2*c*(b-c) +\n16   c^2*a*(c-a) := by\n\n```\n\n```\n\nMathOlympiadBench\n1  /-!\n2  # International Mathematical\n3  Olympiad 1983, Problem 6\n4\n5  Suppose that a,b,c are the side\n6  lengths of a triangle. Prove\n7  that\n8\n9  a^2b(a-b) + b^2c(b-c) + c^2a(c-a) ≥ 0.\n10\n11  Determine when equality occurs.\n12  -/\n13\n14 abbrev EqualityCondition (a b c :\n15   ℝ) : Prop :=\n16   a = b ∧ a = c\n17\n18 theorem imo1983_p6\n19   (T : Affine.Triangle ℝ\n20   (EuclideanSpace ℝ (Fin 2))) :\n21   let a := dist (T.points 1)\n22   (T.points 2)\n23   let b := dist (T.points 0)\n24   (T.points 2)\n25   let c := dist (T.points 0)\n26   (T.points 1)\n27   0 ≤ a^2*b*(a-b) + b^2*c*(b-c) +\n28   c^2*a*(c-a) ∧\n29   (0 = a^2*b*(a-b) + b^2*c*(b-c) +\n30   c^2*a*(c-a) ↔\n31   EqualityCondition a b c) :=\n32   sorry\n\n```\n\nThe informal statement has two parts: proving an inequality and determining the condition for equality. The MiniF2F version only formalizes the inequality, completely omitting the second part of the problem. In contrast, MathOlympiadBench provides a complete formalization.A.3 IMO 1962, PROBLEM 2: INFORMAL & FORMAL STATEMENT MISMATCH\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>MiniF2F&lt;/th>\n&lt;th>MathOlympiadBench&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>\n&lt;pre>1 /-- Determine all real numbers x\n2   which satisfy the inequality:\n3\n4   &lt;math>\\sqrt{\\sqrt{3-x}-\\sqrt{x+1}} &gt; \\frac{1}{2}&lt;/math>\n5\n6   Show that it is &lt;math>\\left[-1, 1 - \\frac{\\sqrt{127}}{32}\\right)&lt;/math>.\n7   -/\n8\n9   theorem imo_1962_p2 (x : ℝ) (h0 :\n10      0 ≤ 3 - x) (h1 : 0 ≤ x + 1)\n11      (h2 : 1 / 2 &lt; Real.sqrt (3 -\n12      x) - Real.sqrt (x + 1)) : -1 ≤\n13      x ∧ x &lt; 1 - Real.sqrt 31 / 8\n14      := sorry&lt;/pre>\n&lt;/td>\n&lt;td>\n&lt;pre>1 /-!\n2 # International Mathematical\n3   Olympiad 1962, Problem 2\n4\n5 Determine all real numbers x\n6   which satisfy\n7\n8   &lt;math>\\sqrt{3-x}-\\sqrt{x+1} &gt; \\frac{1}{2}&lt;/math>.\n9   -/\n10\n11 abbrev SolutionSet : Set ℝ :=\n12     Set.Ico (-1) (1 - &lt;math>\\sqrt{31} / 8&lt;/math>)\n13\n14 theorem imo1962_p2 (x : ℝ) :\n15   x ∈ SolutionSet ↔\n16   x ≤ 3 ∧ -1 ≤ x ∧ 1/2 &lt; &lt;math>\\sqrt{(3-x)}&lt;/math>\n17   - &lt;math>\\sqrt{(x+1)}&lt;/math> := sorry&lt;/pre>\n&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nFor this problem, the original inequality appears in two different versions&lt;sup>6&lt;/sup>: one as  $\\sqrt{3-x}-\\sqrt{x+1} > \\frac{1}{2}$  and another as  $\\sqrt{\\sqrt{3-x}-\\sqrt{x+1}} > \\frac{1}{2}$ . In MiniF2F, the informal statement uses the latter (the nested square root version), but the formal statement is based on the former (the simpler difference of square roots), resulting in a mismatch between the informal and formal statements. In contrast, MathOlympiadBench ensures that both the informal and formal statements consistently correspond to the same version of the problem.\n\nB FORMAL NEGATION\n\nWe attempt to disprove unsolved statements by proving their logical negation. This is achieved by parsing the Lean 4 statements as follows.\n\n&lt;table border=\"1\">\n&lt;tbody>\n&lt;tr>\n&lt;td>\n&lt;pre>1 theorem fourIsPrime (a : ℕ) (ha : a = 4) : a.Prime := by sorry\n2 theorem fourIsPrimeNeg : ¬ ∃ (a : ℕ) (ha : a = 4), a.Prime := by sorry&lt;/pre>\n&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nC DETAILS FOR JUDGING FORMALIZATION\n\nHere is the exact prompt for LLM judging the faithfulness of formalization.\n\n&lt;table border=\"1\">\n&lt;tbody>\n&lt;tr>\n&lt;td>\n&lt;p>You will receive a math problem consisting of its natural language statement along with its formal statement in LEAN 4.&lt;/p>\n&lt;p>Please evaluate whether the formal LEAN statement appropriately translates the natural language statement based on the following criteria:&lt;/p>\n&lt;ol>\n&lt;li>1. Key Elements: The problem's essential components are correctly represented in LEAN code.&lt;/li>\n&lt;li>2. Mathematical Accuracy: The translation preserves the accuracy of the mathematical content.&lt;/li>\n&lt;li>3. Structural Fidelity: The translation aligns closely with the original problem, maintaining its structure and purpose.&lt;/li>\n&lt;/ol>\n&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n&lt;sup>6&lt;/sup>Please refer to: [https://artofproblemsolving.com/wiki/index.php/1962\\\\_IMO\\\\_Problems/Problem\\\\_2](https://artofproblemsolving.com/wiki/index.php/1962_IMO_Problems/Problem_2).4. Comprehensiveness: All assumptions, conditions, and goals present in the natural language statement are included in the LEAN translation.\n\nYour answer should be in the following format:\n\nThought: [Your Answer]\n\nJudgement: [Your Answer, one of {Appropriate, Inappropriate}]\n\n---\n\nFollowing are the example problems label for the reasonability of their translation.\n\n# Example 1:\n\n## Original natural language statement of the problem:\n\nFor the graph of a certain quadratic  $y = ax^2 + bx + c$ , the vertex of the parabola is  $(2, 10)$ , and one of the  $x$ -intercepts is  $(1, 0)$ . What is the  $x$ -coordinate of the other  $x$ -intercept?\n\n## Translated formal statement:\n\n```\n\n```lean\ntheorem quadratic_other_intercept\n  (f : ℝ → ℝ)\n  (a b c : ℝ)\n  (h_quad : ∀ x, f x = a * x^2 + b * x + c)\n  (h_vertex : f 2 = 10 ∧ ∀ x, f x ≤ f 2)    -- vertex at (2,10)\n  (h_intercept1 : f 1 = 0) :                -- x-intercept at (1,0)\n  f 3 = 0 := by                             -- other x-intercept at\n  (3, 0)\n```\n\n```\n\nThought: The Lean translation of the problem is appropriate because it accurately captures the intent and reasoning of the original problem. The problem's key elements, such as the vertex, axis of symmetry, and  $x$ -intercepts of the quadratic function, are correctly translated into Lean code. The logical flow of the proof mirrors the original reasoning, starting with the symmetry property of the quadratic function and using it to determine the second  $x$ -intercept. The mathematical accuracy is preserved, as the proof correctly applies the vertex property and symmetry to arrive at the solution. Furthermore, the translation aligns well with the original problem in natural language, maintaining fidelity to its structure and purpose. Overall, the translation is both faithful and complete, making it an appropriate representation of the original problem.\n\nJudgement: Appropriate\n\n# Example 2:\n\n## Original natural language statement of the problem:\n\nDraw a tangent line from the point  $(4, 3)$  to the circle  $(x - 2)^2 + (y - 1)^2 = 1$ . What is the equation of the line that passes through the two tangent points?\n\n## Translated formal statement:\n\n```\n\n```lean\ntheorem tangent_line_equation (x y : ℝ) :\n  let P : ℝ × ℝ := (4, 3)    -- Point P\n  let C : ℝ × ℝ := (2, 1)    -- Center of first circle\n\n``````\n\nlet r : ℝ := 1           -- Radius of first circle\n-- Points (x,y) satisfying both circle equations\nlet on_first_circle := (x - 2)^2 + (y - 1)^2 = 1\nlet on_second_circle := (x - 3)^2 + (y - 2)^2 = 2\n-- If point is on both circles\non_first_circle ∧ on_second_circle →\n-- Then it lies on the line 2x + 2y - 7 = 0\n2*x + 2*y - 7 = 0 := by\n```\n\n```\n\nThought: The Lean translation of the problem is inappropriate because it fundamentally changes the intent of the original problem. The original problem asks to derive the equation of the tangent line passing through the intersection points of two circles, but the translation assumes the equation  $(2x + 2y - 7 = 0)$  is already given and instead asks to prove that the intersection points lie on this line. This shifts the problem from a construction task to a verification task, losing the original problem's focus on deriving the result through geometric and algebraic reasoning. Additionally, the translation omits the key reasoning step of subtracting the circle equations to derive the line equation, which is central to the original problem. As a result, the translation fails to accurately represent the problem's intent and educational value, making it an incomplete and inappropriate representation.\n\nJudgement: Inappropriate\n\nExample3:\n\n## Original natural language statement of the problem:\n\nIf  $a, b, c, d > 0$  and  $abcd = 1$ , prove that  $\\frac{1}{a+b+c+1} + \\frac{1}{b+c+d+1} + \\frac{1}{c+d+a+1} + \\frac{1}{d+a+b+1} \\leq \\frac{1}{a+3} + \\frac{1}{b+3} + \\frac{1}{c+3} + \\frac{1}{d+3}$\n\n## Translated formal statement:\n\n```\n\n```lean4\ntheorem lean_workbook_49553 (a b c d : ℝ) (habc : a * b * c * d = 1) :\n  (1 / (a + b + c + 1) + 1 / (b + c + d + 1) + 1 / (c + d + a + 1) +\n  1 / (d + a + b + 1)) ≤ (1 / (a + 3) + 1 / (b + 3) + 1 / (c + 3) + 1\n  / (d + 3)) := by sorry\n```\n\n```\n\nThought: The Lean translation of the problem is inappropriate because the condition  $a, b, c, d > 0$  is ignored in the formal statement.\n\nJudgement: Inappropriate\n\nExample4:\n\n## Original natural language statement of the problem:\n\nIf  $a = b = c = 2$  so  $\\sum_{cyc} \\frac{(a-1)^2}{a^2+2} = \\frac{1}{2}$ . We'll prove that  $\\frac{1}{2}$  is the answer.\n\n## Translated formal statement:\n\n```\n\n```lean4\ntheorem lean_workbook_plus_1478 (a b c : ℝ) (ha : a = 2) (hb : b = 2)\n  (hc : c = 2) : (a - 1) ^ 2 / (a ^ 2 + 2) + (b - 1) ^ 2 / (b ^ 2 +\n  2) + (c - 1) ^ 2 / (c ^ 2 + 2) = 1 / 2 := by sorry\n```\n\n``````\n\nThought: The Lean translation of the problem is appropriate because it\naccurately captures the assumptions and the goal in the natural\nlanguage statement.\n\nJudgement: Appropriate\n\n## Original natural language statement of the problem:\n\n{informal_statement}\n\n## Translated formal statement:\n```lean4\n{formal_statement}\n```\n\n```\n\n## D DETAILS FOR INFORMAL-BASED SCAFFOLDED DATA SYNTHESIS\n\nIn this section, we provide all the details for informal-based scaffolded data synthesis. We start with the prompt template for different LLM queries, including the prompt template to generate harder variant, simpler/sub-problem, as well as the prompt template to judge the simplicity and correctness. Then, we provide more details for the synthesis pipeline.\n\n**Prompt template for solving the original problem** Note that for both input with natural language problem and statement written in Lean, we use the same prompt because we find that general-purpose models can understand the Lean although they cannot generate the whole proof correctly.\n\n```\n\nSolve the following math problem probably written in Lean 4:\n{problem}\nProvide a detailed solution. Note that you don't need to prove the\nproblem in Lean 4, just provide a detailed solution in natural\nlanguage or math notation.\n\n```\n\n### Prompt template for generating sub/simpler problems\n\n```\n\nI will give you a math problem along with its full solution.\nYour task is to generate simpler problems which may enable a student to\nbuild up the skills to solve the given problem. Each simpler\nproblem should reflect the idea of a core step in the solution.\nEach generated problem must:\n(1) Be completely self-contained and standalone: it should be clearly\nstated as an independent question that someone could read and work\non without seeing the original problem and the other generated\nproblems.\n(2) Be purely proof-based: stated explicitly as a question of the form\n\"Prove that...\".\n(3) Be related to the core steps in the solution of the original\nproblem or reflect the core idea, and should not be just trivial\nand straightforward derivation, plug-in calculation, or solving\nsimple equations.\nAfter generating the problems, carefully evaluate your own output and\nperform the following checks:\n(1) Ensure each problem is fully self-contained: check that it does not\nrely on undefined variables, terms, or concepts from the original\nproblem or other problems.\n(2) Ensure the set of problems is diverse, covering different steps or\naspects of the original reasoning.\n(3) Ensure that the problems are not too simple or trivial, and that\nthey require a meaningful proof. Avoid trivial and straightforward\nderivation, plug-in calculation, or solving simple equations.\n\n``````\nWrap each final selected problem between the tags &lt;newproblem> and\n&lt;/newproblem> to make it easy to extract.\nDo not include anything else.\nProblem: {problem}\nSolution: {solution}\n```\n\n### Prompt template for generating harder variant of problems\n\n```\nI now have a math problem and its solution at hand, and I would like\nyou to modify the problem to generate a diverse set of new problems\nbased on it. Below is the problem (probably written in Lean 4):\n---\n{problem}\n---\n```\n\nBelow is the solution:\n\n```\n---\n{solution}\n---\n```\n\nNow I would like you to generate at least 10 new math problems, each\nclearly different from the original. For example, you can make the\nfollowing modifications to make the problem different:\n\n- Change the number in the original problem to generate a new problem.\n- Transform the algebraic formula such that it needs more\n  simplification. For example, change  $\\cos(x)$  in the original problem\n  into  $1 - 2 \\sin(x/2)^2$ .\n- Add more terms in the inequality. For example, the original problem need\n  to show that  $f(x)$  is non-negative, you transform the problem into\n   $f(x) + (1/x - a)^2$  is non-negative, or  $f(x) \\cdot (x - b)^2$  is\n  non-negative.\n- Lift a real variable into a complex number, a vector or even matrix.\n  For example previously when solving quadratic equation in real\n  space, you now change it to complex field, which might lead to\n  slightly different solutions. Or the original problem considers\n  planer geometry, you modify the problem into 3 dimensional geometry.\n- Substitute a variable into a more complex algebraic form, which\n  includes but not limited to changeing a variable into a polynomial,\n  exponential, logarithm, or even trigonometry. For example, you\n  change variable  $x$  in the original problem into  $y^2$  or even  $y^n$  in\n  the new problem. Another example is that you are given some\n  condition like  $a + b + c = 1$  where  $a, b, c$  are all positive, and\n  you need to show  $f(a, b, c)$  is non-negative. You can change the\n  condition into  $x y + y z + z x = x y z$  with  $x, y, z$  positive, which\n  is equivalent to  $1/x + 1/y + 1/z = 1$ , and modify the statement to\n  show that  $f(1/x, 1/y, 1/z)$  is non-negative.\n- Use the conclusion in the problem as a step to solve another problem.\n  For example, the original problem need to solve equation  $f(x) = 0$ ,\n  where  $x$  is the variable. Now you change it to solve  $f(\\exp(x)) = 0$ ,\n   $f(\\ln(x)) = 0$ , or  $f(\\cos(x)) = 0$ , or even  $f(x^2) = 0$ .\n\nThese are just some example transformations you can try, and you are\nnot limited to these transformations. Do not overcomplicate the\nproblem, and it is acceptable to make simple transformations. The\nnew math problem should not be simpler than the example problems I\nprovided, i.e., you should not simplify the original problem and\nmake it the new problem.\n\nEach generated problem must:\n\n1. (1) Be purely proof-based: stated explicitly as a question of the form\n   \"Prove ...that\". Do not generate problems that ask to \"determine\",\n   \"compute\", \"evaluate\", \"find\", or similar.\n2. (2) Be completely self-contained and standalone.\n3. (3) Be mathematically valid and solvable.\n4. (4) Be meaningfully different to ensure diversity.Wrap each generated problem between the tags `&lt;newproblem>` and `&lt;/newproblem>` to make it easy to extract.  \n Do not include anything else.\n\n### Prompt template to judge the correctness and simplicity of the synthesized statement\n\nI will give you a math problem written in Lean 4, and I will ask you to determine (1) whether the problem is correct or not; and (2) whether the problem is too simple to prove or disprove in Lean 4. Here is a list of too simple problems in Lean 4: simple calculations, simple algebraic manipulations, solving single variable linear equations (by just a 1-step calculation), and inequalities proved by an easy sum-of-squares technique. However, do not include inequality proving with the square root since that might be more complex. Please do not label other problems, such as other more complex inequalities, limits, and integrals, as simple problems. Also, please do not label problems that deals with integers (more related to number theory), higher order roots, complex numbers, matrices, polynomials, group, finite-sum, or functional equations (e.g. Let  $f$  be a function such that  $f(x^2) = xf(x)$  for all  $x \\in \\mathbb{R}$ . Prove that  $f$  is an odd function, i.e.,  $f(-x) = -f(x)$  for all  $x \\in \\mathbb{R}$ .), since these problems might shed lights on other hard problems.\n\nPlease carefully analyze the problem and provide an explanation of your reasoning.\n\nFor judging the correctness, if the problem is correct, respond with \"yes\"; if the problem is incorrect, respond with \"no\"; if you are not sure, respond with \"unsure\".\n\nFor judging the simplicity, if the problem is too simple to prove or disprove in Lean 4, respond with \"yes\"; if the problem is not too simple, respond with \"no\"; if you are not sure, respond with \"unsure\". Please refer to the list of too-simple problems I provided.\n\nWrap your judgment between `&lt;judge>` and `&lt;/judge>` to make it easy to extract. You should first answer yes or no to the correctness and then answer yes or no to the simplicity, separated by a comma. For example, if you think the problem is correct and not too simple, you should respond with `&lt;judge>yes, no&lt;/judge>`. If you are not sure about the correctness, you can respond with `&lt;judge>unsure, no&lt;/judge>` because at least this problem is not simple. If you think the problem is incorrect but it is not too easy to disprove, you can respond with `&lt;judge>no, no&lt;/judge>`. If you think the problem is correct but too simple to prove or disprove, you can respond with `&lt;judge>yes, yes&lt;/judge>`. Again, when judging the simplicity, please do not label inequality proving with the square root as simple, since that might be more complex than expected. Please do not include problems such as more complex inequalities, or problems that include limits, and integrals. Also, please do not label problems that deals with integers (more related to number theory), higher order roots, complex numbers, matrices, polynomials, group, finite-sum, or functional equations, as simple problems, since these notions are more likely to related to hard problems and proving problems related to these concepts in Lean 4 might not be easy even if the problem is straight-forward in natural language.\n\nDo not include anything else.  \n Problem: {formal\\_statement}\n\n**More details for informal-based scaffolded data synthesis** In the following part, we discuss some of the design choices and details for the scaffolded data synthesis pipeline.\n\n1. 1. **(Informal statements generation.)** For the informal statements generation, one design choice is whether to generate multiple questions during the same inference, or to generatemultiple times while only generating 1 (or very few) questions during one inference. From our experiment, we observe that for the Qwen3-32B model, generating multiple questions during the same inference is better, since the generated questions are likely to be different. Otherwise, there might be very similar questions among different generations. Besides, we also find that repeatedly generating a single problem multiple times doesn't significantly increase the number of different problems. Thus, for efficiency considerations, we only query the LLM (Qwen3-32B) once for generating multiple hard variants/simple problems of a given math problem.\n\n1. 2. **(Formalization and quality checking.)** For each generated informal statement, we call the trained formalizer to formalize the problem twice. Then, we then query Qwen3-8B for 3 times for each formalization, and decide if the formalization is aligned with the informal statement using majority voting (among three queries). We decide to formalize each informal statement twice in order to balance the efficiency and the number of generated problems. We only keep at most one formalization for each generated informal statement.\n2. 3. **(Negation and difficulty filtering.)** For each formalization, we query Qwen3-32B for 4 times, where each inference judges the correctness and the simplicity simultaneously. The final correctness is judged by strict majority voting among the 4 judges, while the final simplicity is determined if all 4 judges think the problem is easy. We use such strict criteria to minimize the probability of discarding hard and valuable problems. The efficiency for the judging is high, even if we call Qwen3-32B 4 times for each formalization, since a lot of the time Qwen3-32B enters the “fast thinking” mode (no long chain-of-thought for reasoning).\n3. 4. **(Final deduplication.)** At the end of the pipeline, we filter out duplicated statements under exact match.\n\n## E RL TRAINING DETAILS\n\nWe further explain our RL training in detail.\n\n### E.1 RL IMPLEMENTATION\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>&lt;/th>\n&lt;th>&lt;/th>\n&lt;th>Input&lt;/th>\n&lt;th>Rollout&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>(1) Vanilla RL&lt;/td>\n&lt;td>&lt;b>Single-Task&lt;/b>&lt;/td>\n&lt;td>Question&lt;/td>\n&lt;td>Answer&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>(2) Tool-assisted RL&lt;/td>\n&lt;td>&lt;b>Complex Inefficient&lt;/b>&lt;/td>\n&lt;td>Question&lt;/td>\n&lt;td>Tool Using → Feedback → Answer&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>(3) Ours&lt;/td>\n&lt;td>&lt;b>Multi-Task Efficient&lt;/b>&lt;/td>\n&lt;td>Question → Answer → Feedback&lt;/td>\n&lt;td>Answer → Self-Correction&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nFigure 9: Illustrative figure for our multi-task RL. This pipeline improves models’ performance on both the whole proof and the self-correction at the same time without additional design on the framework or algorithm.\n\nWe begin by collecting 50K challenging statements and 50K self-correction samples. Each self-correction sample contains a statement, a output generated by the SFT model, and an associated error message. During RL training, we consumed approximately 46K and 64K unique inputs for the 8B and 32B models on 1 epoch, respectively. We use the VeRL framework (Sheng et al., 2024) with several key setups: We adopt a batch size of 128 and n of 8 for parallel rollouts and reward function calls (via the Lean compiler), while using a mini-batch size of 32, accepting a certain degree of off-policy training in exchange for a higher frequency of policy optimization. For the dynamic sampling, we set the over-sample batch size equal to three times of train batch size and filter out inputs with a pass rate equal to 0 or higher than 0.75. We use a maximum prompt length of 16K for those long inputs in the self-correction task. We set the maximum response length to 24K to support a reasonably sized reasoning trajectory while staying within the Qwen3 model’s native 40K contextwindow, ensuring generation quality. We enable the overlong penalty with a 4K overlong buffer and set the overlong penalty factor to 1. We use token-averaged policy loss and do not use KL divergence or entropy terms in our training objective.\n\nFigure 10: Training curves comparing 32B and 8B models: training rewards (top row) and generation lengths (bottom row) for whole proof completion and self-correction tasks. Note that the rewards are averaged over all generated rollouts, including those then filtered by the dynamic sampling strategy, thus reflecting the policy improvement.\n\n## E.2 FURTHER DISCUSSION ON RL\n\nFor the design of training with self-correction, we explored both tool-use and multi-turn reinforcement learning. However, the former not only requires a dedicated tool-calling design, but also demands strong model capability to follow the tool-calling protocol, especially in complex and lengthy formal language scenarios like Lean, which is particularly challenging for our relatively small model. Meanwhile, multi-turn approaches introduce various engineering challenges, especially on the rollout engine side, such as asynchronous generation. Moreover, on the algorithm side, the effectiveness and efficiency of multi-turn RL still require further validation. We have explored some preliminary approaches, but they remain immature. Therefore, we adopt a more straightforward implementation that is natively integrated into the current RL framework, as illustrated in Figure 9. In this setup, we have two different type of inputs for RL and detailed training curves are shown in Figure 10. Furthermore, for the algorithmic design, like the advantage estimator, we explored different popular GRPO variants but did not observe significant differences.\n",
    "durationMs": 679,
    "url": "https://huggingface.co/papers/2508.03613"
  },
  "sourceToolAssistantUUID": "9aa0d3e3-ff8c-4aeb-b753-b503fb38a700",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```````

</details>

---

### Runtime record

_source line 38_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-27 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "1289f6dd-4d2d-4df9-b4f1-4158a26a626b",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze Goedel-Prover-V2 paper innovation",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc"
}
```

---

### Tool result

_source line 40 · 2026-05-27T15:58:34.227Z_

<details><summary>↩ Tool result · `toolu_01AFcw2jKfkHmXw6S8UbZb7v`</summary>

```text
# Goedel-Prover-V2: Comprehensive Extraction

## 1. BENCHMARK RESULTS & PERFORMANCE

**MiniF2F Performance:**
- Goedel-Prover-V2-32B: 88.0% at Pass@32 (standard mode)
- Goedel-Prover-V2-32B: 90.4% at Pass@32 (self-correction mode)
- Goedel-Prover-V2-8B: 84.6% at Pass@32
- Reference: DeepSeek-Prover-V2-671B baseline for comparison

**PutnamBench Leaderboard (Table 1):**
- Goedel-Prover-V2-32B (self-correction): 86 problems solved at Pass@192
- Goedel-Prover-V2-32B (self-correction): 57 problems at Pass@32
- Goedel-Prover-V2-32B (standard): 43 problems at Pass@32
- DeepSeek-Prover-V2-671B: 47 problems at Pass@1024

**MathOlympiadBench:**
- New benchmark containing "360 IMO-level problems"
- Sources: Compfiles and IMOSLLean4 repositories
- Composition: 158 IMO problems (1959-2024), 131 IMO shortlist problems, 68 regional Olympiad problems, 3 puzzles

## 2. TECHNICAL METHODOLOGY

Three core innovations described:

1. **Scaffolded Data Synthesis**: "Generate synthetic proof tasks of increasing difficulty to progressively train"
2. **Verifier-guided Self-correction**: "Model learns to iteratively revise its own proofs by leveraging feedback from Lean's compiler"
3. **Model Averaging**: "Combine multiple model checkpoints to improve robustness"

Self-correction operates with "two rounds," maintaining modest computational efficiency with total output increasing "from the standard 32K to 40K tokens."

## 3. MODEL SPECIFICATIONS

**Available Models:**
- Goedel-Prover-V2-32B (flagship)
- Goedel-Prover-V2-8B (smaller variant)

**Base Technology:** Built on "standard expert iteration and reinforcement learning pipeline"

**Size Comparison:** 8B model is "nearly 100 times smaller in model size" than DeepSeek-Prover-V2-671B while matching its performance

## 4. TRAINING ENVIRONMENT

**Lean Version:** Lean 4 version 4.9

**Dependencies:** Python 3.10, Mathlib4 (specified commit: 2f65ba7)

**Code Composition:** Jupyter Notebook 95.5%, Python 4.0%, Shell 0.5%

## 5. DOWNLOAD RESOURCES

**Model Weights:**
- Goedel-Prover-V2-32B: [Hugging Face link provided]
- Goedel-Prover-V2-8B: [Hugging Face link provided]

**Dataset:**
- MathOlympiadBench: [Hugging Face link provided]

## 6. KEY COMPARISONS

The 8B model "matches the performance of prior state-of-the-art DeepSeek-Prover-V2-671B" on MiniF2F despite massive size differential. The 32B variant "outperforms prior SOTA DeepSeek-Prover-V2-671B and concurrent work Kimina-Prover-72B by a large margin."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8da5a5f7-c2eb-4835-9cfe-453734531749",
  "isSidechain": false,
  "promptId": "918f738b-eddd-4a71-9661-57e87bd9f8ed",
  "type": "user",
  "uuid": "08adcda3-436e-4b00-b067-93c3d68344d8",
  "toolUseResult": {
    "bytes": 322318,
    "code": 200,
    "codeText": "OK",
    "result": "# Goedel-Prover-V2: Comprehensive Extraction\n\n## 1. BENCHMARK RESULTS & PERFORMANCE\n\n**MiniF2F Performance:**\n- Goedel-Prover-V2-32B: 88.0% at Pass@32 (standard mode)\n- Goedel-Prover-V2-32B: 90.4% at Pass@32 (self-correction mode)\n- Goedel-Prover-V2-8B: 84.6% at Pass@32\n- Reference: DeepSeek-Prover-V2-671B baseline for comparison\n\n**PutnamBench Leaderboard (Table 1):**\n- Goedel-Prover-V2-32B (self-correction): 86 problems solved at Pass@192\n- Goedel-Prover-V2-32B (self-correction): 57 problems at Pass@32\n- Goedel-Prover-V2-32B (standard): 43 problems at Pass@32\n- DeepSeek-Prover-V2-671B: 47 problems at Pass@1024\n\n**MathOlympiadBench:**\n- New benchmark containing \"360 IMO-level problems\"\n- Sources: Compfiles and IMOSLLean4 repositories\n- Composition: 158 IMO problems (1959-2024), 131 IMO shortlist problems, 68 regional Olympiad problems, 3 puzzles\n\n## 2. TECHNICAL METHODOLOGY\n\nThree core innovations described:\n\n1. **Scaffolded Data Synthesis**: \"Generate synthetic proof tasks of increasing difficulty to progressively train\"\n2. **Verifier-guided Self-correction**: \"Model learns to iteratively revise its own proofs by leveraging feedback from Lean's compiler\"\n3. **Model Averaging**: \"Combine multiple model checkpoints to improve robustness\"\n\nSelf-correction operates with \"two rounds,\" maintaining modest computational efficiency with total output increasing \"from the standard 32K to 40K tokens.\"\n\n## 3. MODEL SPECIFICATIONS\n\n**Available Models:**\n- Goedel-Prover-V2-32B (flagship)\n- Goedel-Prover-V2-8B (smaller variant)\n\n**Base Technology:** Built on \"standard expert iteration and reinforcement learning pipeline\"\n\n**Size Comparison:** 8B model is \"nearly 100 times smaller in model size\" than DeepSeek-Prover-V2-671B while matching its performance\n\n## 4. TRAINING ENVIRONMENT\n\n**Lean Version:** Lean 4 version 4.9\n\n**Dependencies:** Python 3.10, Mathlib4 (specified commit: 2f65ba7)\n\n**Code Composition:** Jupyter Notebook 95.5%, Python 4.0%, Shell 0.5%\n\n## 5. DOWNLOAD RESOURCES\n\n**Model Weights:**\n- Goedel-Prover-V2-32B: [Hugging Face link provided]\n- Goedel-Prover-V2-8B: [Hugging Face link provided]\n\n**Dataset:**\n- MathOlympiadBench: [Hugging Face link provided]\n\n## 6. KEY COMPARISONS\n\nThe 8B model \"matches the performance of prior state-of-the-art DeepSeek-Prover-V2-671B\" on MiniF2F despite massive size differential. The 32B variant \"outperforms prior SOTA DeepSeek-Prover-V2-671B and concurrent work Kimina-Prover-72B by a large margin.\"",
    "durationMs": 10209,
    "url": "https://github.com/Goedel-LM/Goedel-Prover-V2"
  },
  "sourceToolAssistantUUID": "8da5a5f7-c2eb-4835-9cfe-453734531749",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-27T15:58:37.326Z_

<details><summary>Logged reasoning block</summary>

```text
The HuggingFace page has the full paper content. Let me read the persisted output file to get the complete paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08adcda3-436e-4b00-b067-93c3d68344d8",
  "isSidechain": false,
  "requestId": "req_011CbTMFU3FNzjWPGhKfvaej",
  "type": "assistant",
  "uuid": "00d65842-a18e-4dd0-8a80-dc5001036bfe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178ockG6kkGiiCne8PCNs3P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 863,
      "cache_creation_input_tokens": 1319,
      "cache_read_input_tokens": 18587,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1319,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 863,
          "output_tokens": 196,
          "cache_read_input_tokens": 18587,
          "cache_creation_input_tokens": 1319,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1319
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

_source line 42 · 2026-05-27T15:58:37.832Z_

Excellent! The HuggingFace page has the full paper text. Let me read the complete content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00d65842-a18e-4dd0-8a80-dc5001036bfe",
  "isSidechain": false,
  "requestId": "req_011CbTMFU3FNzjWPGhKfvaej",
  "type": "assistant",
  "uuid": "c06d963d-6a14-470f-8e6c-df33f58e1ffb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178ockG6kkGiiCne8PCNs3P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 863,
      "cache_creation_input_tokens": 1319,
      "cache_read_input_tokens": 18587,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1319,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 863,
          "output_tokens": 196,
          "cache_read_input_tokens": 18587,
          "cache_creation_input_tokens": 1319,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1319
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

_source line 43 · 2026-05-27T15:58:38.208Z_

<details open><summary>🔧 Tool call — Read · `toolu_01APAZzvB9FZU2Q9H2kkwjK9`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/6db262d6-dcf8-4dbf-b94b-349936024bbc/tool-results/toolu_01Tq8krFT3t8xgN1SnQrexGw.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c06d963d-6a14-470f-8e6c-df33f58e1ffb",
  "isSidechain": false,
  "requestId": "req_011CbTMFU3FNzjWPGhKfvaej",
  "type": "assistant",
  "uuid": "fe980eaf-94f1-4ecd-ae4d-38d746c1cfe5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178ockG6kkGiiCne8PCNs3P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 863,
      "cache_creation_input_tokens": 1319,
      "cache_read_input_tokens": 18587,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1319,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 863,
          "output_tokens": 196,
          "cache_read_input_tokens": 18587,
          "cache_creation_input_tokens": 1319,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1319
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

_source line 44 · 2026-05-27T15:58:38.580Z_

<details><summary>↩ Tool result · reported error · `toolu_01APAZzvB9FZU2Q9H2kkwjK9`</summary>

```text
File content (25252 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe980eaf-94f1-4ecd-ae4d-38d746c1cfe5",
  "isSidechain": false,
  "promptId": "918f738b-eddd-4a71-9661-57e87bd9f8ed",
  "type": "user",
  "uuid": "4380d381-091f-4f1e-b92c-0fbceead4018",
  "toolUseResult": "Error: File content (25252 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "fe980eaf-94f1-4ecd-ae4d-38d746c1cfe5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-27T15:58:41.620Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XYRsEZ7TMzsFPeEBxrkPje`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/6db262d6-dcf8-4dbf-b94b-349936024bbc/tool-results/toolu_01Tq8krFT3t8xgN1SnQrexGw.txt",
  "offset": 0,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4380d381-091f-4f1e-b92c-0fbceead4018",
  "isSidechain": false,
  "requestId": "req_011CbTMFnUmQKNeg9ETZ3qZJ",
  "type": "assistant",
  "uuid": "64eae359-35cf-482c-bdab-96d75791e811",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B3wvpBMBHVorWd9uBPWx61",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 19906,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1119,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 162,
          "cache_read_input_tokens": 19906,
          "cache_creation_input_tokens": 1119,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1119
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

_source line 46 · 2026-05-27T15:58:41.894Z_

<details><summary>↩ Tool result · `toolu_01XYRsEZ7TMzsFPeEBxrkPje`</summary>

```text
0	# GOEDEL-PROVER-V2: SCALING FORMAL THEOREM PROVING WITH SCAFFOLDED DATA SYNTHESIS AND SELF-CORRECTION
1	
2	Yong Lin&lt;sup>1\*&lt;/sup>, Shange Tang&lt;sup>1 2\*&lt;/sup>, Bohan Lyu&lt;sup>3\*&lt;/sup>, Ziran Yang&lt;sup>1\*&lt;/sup>, Jui-Hui Chung&lt;sup>1\*&lt;/sup>,  
3	 Haoyu Zhao&lt;sup>1\*&lt;/sup>, Lai Jiang&lt;sup>7\*&lt;/sup>, Yihan Geng&lt;sup>8\*&lt;/sup>, Jiawei Ge&lt;sup>1&lt;/sup>, Jingruo Sun&lt;sup>4&lt;/sup>,  
4	 Jiayun Wu&lt;sup>3&lt;/sup>, Jiri Gesi&lt;sup>6 †&lt;/sup>, Ximing Lu&lt;sup>2&lt;/sup>, David Acuna&lt;sup>2&lt;/sup>, Kaiyu Yang&lt;sup>5 ‡&lt;/sup>,  
5	 Hongzhou Lin&lt;sup>6 \*†&lt;/sup>, Yejin Choi&lt;sup>2 4&lt;/sup>, Danqi Chen&lt;sup>1&lt;/sup>, Sanjeev Arora&lt;sup>1&lt;/sup>, Chi Jin&lt;sup>1\*&lt;/sup>
6	
7	&lt;sup>1&lt;/sup>Princeton Language and Intelligence, Princeton University &lt;sup>2&lt;/sup>NVIDIA  
8	&lt;sup>3&lt;/sup>Tsinghua University &lt;sup>4&lt;/sup>Stanford University &lt;sup>5&lt;/sup>Meta FAIR &lt;sup>6&lt;/sup>Amazon  
9	&lt;sup>7&lt;/sup>Shanghai Jiao Tong University &lt;sup>8&lt;/sup>Peking University
10	
11	## ABSTRACT
12	
13	We introduce Goedel-Prover-V2, a series of open-source language models that set a new state-of-the-art in automated theorem proving. Built on the standard expert iteration and reinforcement learning pipeline, our approach incorporates three key innovations: (1) Scaffolded data synthesis: We generate synthetic tasks of increasing difficulty to train the model to master increasingly complex theorems; (2) Verifier-guided self-correction: We enable the model to iteratively revise its proofs by leveraging feedback from the Lean compiler; (3) Model averaging: We merge model checkpoints to mitigate the decrease in model output diversity in later stages of training. Our small model, Goedel-Prover-V2-8B, reaches 84.6% pass@32 on MiniF2F and outperforms DeepSeek-Prover-V2-671B under the same metric, despite being 80X smaller. Our flagship model, Goedel-Prover-V2-32B, achieves 88.1% on MiniF2F at pass@32 in standard mode and 90.4% in self-correction mode, outperforming prior SOTA by a large margin. Additionally, our flagship model solves 86 problems on PutnamBench at pass@184, securing the first place among open-source models on the leaderboard, surpassing DeepSeek-Prover-V2-671B’s record of solving 47 problems by pass@1024 with a significantly smaller model size and compute budget. At the time of its release (July–August 2025), Goedel-Prover-V2 achieves the strongest overall performance among all open-source theorem provers. It also ranks among the top-performing models—including closed-source systems with publicly reported performance—under a constrained test-time compute budget. Our models, code, and data are released at &lt;https://github.com/Goedel-LM/Goedel-Prover-V2>.
14	
15	## 1 INTRODUCTION
16	
17	Automated theorem proving (ATP) is a grand challenge for AI, requiring the construction of step-by-step, machine-verifiable proofs in formal languages like Lean (De Moura et al., 2015; Moura & Ullrich, 2021). Unlike reasoning in natural language, ATP demands a completely rigorous logical flow, which poses an exceptional challenge for AI systems. The field has advanced rapidly in recent years; for example, DeepMind’s AlphaProof (Google DeepMind, 2024) and AlphaGeometry (Trinh et al., 2024; Chervonyi et al., 2025) demonstrated that AI systems are capable of achieving IMO (International Math Olympiad) medal-level performance. Furthermore, open-source efforts such as DeepSeek-Prover-V2 (Ren et al., 2025) and Kimina-Prover (Wang et al., 2025) have achieved impressive results on benchmarks like MiniF2F (Zheng et al., 2021) and PutnamBench (Tsoukalas et al., 2024), demonstrating the effectiveness of leveraging the reasoning ability of LLMs through
18	
19	\*Core Contributor.
20	
21	†This work is independent of and outside of the work at Amazon.
22	
23	‡All experiments and data processing were conducted outside Meta.Figure 1: Performance of Goedel-Prover-V2 on different benchmarks under pass@32.
24	
25	chain-of-thoughts. These successes, however, typically depend on massive models (e.g., DeepSeek-Prover-V2 has 671B parameters) or computationally intensive inference (e.g., the concurrent work Seed-Prover (Chen et al., 2025)), which involves complex search algorithms and enormous search budgets.
26	
27	In this work we introduce Goedel-Prover-V2, a new series of open-source models for automated theorem proving in Lean that establish a new state-of-the-art in both performance and computational efficiency. The models are capable of generating whole proof and leveraging verifier feedback for iterative self-correction. Our flagship 32B model achieves 88.1% pass@32 on the MiniF2F benchmark, improving to 90.4% with self-correction. This performance surpasses both the concurrent 72B Kimina-Prover and the previous SOTA 671B DeepSeek-Prover-V2, while using significantly fewer parameters (Figure 1). On the more challenging PutnamBench, our model solves 44 problems (57 with self-correction), more than doubling the number solved by DeepSeek-Prover-V2 under the same metric. The efficiency of our approach is further underscored by our 8B model, which alone outperforms the 671B DeepSeek-Prover-V2 on MiniF2F despite being nearly 80 times smaller. At the time of its release (July–August 2025), Goedel-Prover-V2 achieves the strongest overall performance among all open-source theorem provers. It also ranks among the top-performing models—including closed-source systems with publicly reported performance—under small test-time compute budgets.
28	
29	The key to these gains lies in novel design across the framework, data, and training pipelines. We highlight the main components below:
30	
31	- • **Verifier-guided self-correction:** Framework-wise, we incorporate feedback from the Lean compiler (verifier) into the model input to enable the error-correction ability of our theorem prover (*verifier-guided self-correction*). While correcting errors based on verifier feedback has been studied in theorem proving (First et al., 2023) and coding (Olausson et al., 2024; Chen et al., 2024; Bouzenia et al., 2024), we further incorporate this into models that generate long chain-of-thought (CoT) reasoning, which is effective for complex reasoning tasks such as ATP (Jaech et al., 2024; Guo et al., 2025; Wang et al., 2025; Ren et al., 2025).
32	- • **Scaffolded data synthesis:** Successfully combining long CoT with verifier-guided error correction requires special efforts on curating data. In addition to formalizing existing math problems and curating data for error correction, we augment our training statement set through *scaffolded data synthesis*. This technique creates math problems at an appropriate difficulty level to provide the model with better learning signals.
33	- • **Model averaging:** Our training recipe extends beyond standard expert iteration and reinforcement learning. We also apply *model averaging* (Wortsman et al., 2022b) to mitigate the decrease in model output diversity that can occur in the later stages of training.
34	
35	Overall, our results demonstrate that the frontier of formal theorem proving can be advanced without access to extremely large models, a vast computational resources, or proprietary technology. We hopethat our open-source theorem prover series, Goedel-Prover-V2, will enable the community to build upon them and accelerate progress toward AI systems that can reliably solve and verify complex mathematical problems, and ultimately bridge the long-standing divide between intuitive human reasoning and formal proof verification.
36	
37	The following paper is organized as follows: in Section 2, we introduce our main methods to train Goedel-Prover-V2, including the verifier-guided self-correction framework (Section 2.1), scaffolded data synthesis (Section 2.2), and the training pipeline (Section 2.3). In Section 3, we present the evaluation results on Goedel-Prover-V2, including evaluation on both standard and our curated benchmarks (Section 3.3), scaling behavior under different test-time budgets (Section 3.4), and a study of reinforcement learning and model averaging (Section 3.6). Finally, we review the previous works (Section 4) and discuss the connection with Goedel-Prover-V2.
38	
39	## 2 METHOD
40	
41	In this section, we present our method in detail. We start with the key framework innovation compared to the previous vanilla whole-proof generation methods (e.g. DeepSeek-Prover-V2) by utilizing the feedback from the Lean compiler to guide the proof-correction procedure (Section 2.1). Then, in Section 2.2, we demonstrate how to curate the training data (statements), with an emphasis on augmenting the data through scaffolded data synthesis. Based on the curated data, we present the details of training our theorem prover in Section 2.3, which includes supervised fine-tuning (SFT), reinforcement learning (RL), and model averaging. Section 2.4 provides a summary of the overall framework.
42	
43	### 2.1 CHAIN-OF-THOUGHT AND SELF-CORRECTION
44	
45	Prevailing paradigms for whole-proof generation in automated theorem proving have largely been “end-to-end,” where a model generates a complete formal proof from a theorem statement in a single pass (Xin et al., 2024b; Lin et al., 2025; Dong & Ma, 2025). Recent work has significantly advanced this approach by leveraging the long-chain-of-thought reasoning capabilities of large models (Wang et al., 2025; Ren et al., 2025).
46	
47	A key distinction between informal and formal proof generation lies in the availability and utilization of compilation (verification) feedback from proof assistants like Lean or Coq. Humans naturally leverage such feedback to iteratively revise their proofs. Recent works have shown that integrating the verifier’s error messages or tactic verification outcomes into proof generation significantly improves synthesis accuracy (First et al., 2023).
48	
49	Our framework formalizes this intuition by explicitly incorporating verifier feedback within the whole-proof generation loop. We structure the pipeline so that, after an initial proof attempt, verification failures are parsed and communicated back into the model as corrective guidance. The model then generates proof repairs, leading to an iterative self-correction process.
50	
51	### 2.2 CURATING FORMAL STATEMENTS
52	
53	In this part, we detail our methods for curating a large, high-quality dataset of Lean 4 statements, which is essential for expert iteration and RL in formal theorem proving. We start with the formalizer training, which is the core of translating existing math problems written in natural language into Lean statements. We then present our scaffolded data synthesis pipeline that creates math problems at an appropriate difficulty level, which includes a lightweight formal-based method that utilizes the Lean system, and an informal-based system for large-scale data augmentation.
54	
55	**Formalizer Training.** Existing Lean datasets (e.g., Goedel-Pset-v1) contain many low-quality problems—human evaluation on a sampled subset shows that over 80% of unsolved problems are incorrectly formalized. This highlights the need for stronger formalizers. We train our formalizer using the standard expert iteration pipeline, which combines Lean syn-
56	
57	&lt;table border="1">
58	&lt;thead>
59	&lt;tr>
60	&lt;th>Name&lt;/th>
61	&lt;th>Pass&lt;/th>
62	&lt;th>Failed&lt;/th>
63	&lt;/tr>
64	&lt;/thead>
65	&lt;tbody>
66	&lt;tr>
67	&lt;td>Kimina-autoformalizer&lt;/td>
68	&lt;td>161&lt;/td>
69	&lt;td>139&lt;/td>
70	&lt;/tr>
71	&lt;tr>
72	&lt;td>Godel-Formalizer-V2&lt;/td>
73	&lt;td>228&lt;/td>
74	&lt;td>72&lt;/td>
75	&lt;/tr>
76	&lt;/tbody>
77	&lt;/table>
78	
79	Table 1: Comparison of different formalizers on 300 Omni-math problems.Figure 2: Our **informal-based scaffolded data synthesis pipeline** with three parts: (1) informal statement generation; (2) formalization and quality checking; and (3) negation and difficulty filtering.
80	
81	tax checks and semantic evaluation via LLMs to assess translation quality. Only statements that pass both checks are included in the next iteration of SFT. Details of the LLM semantic evaluation prompt are provided in Appendix C.
82	
83	To initialize expert iteration, we prompt Claude Sonnet 4 to generate 50K formalized statements, along with corresponding reasoning traces. Incorporating reasoning capability enables our formalizer to outperform previous models such as Goedel-Formalizer-V1 and Kimina-Autoformalizer, which lack this feature.
84	
85	We evaluate our model Goedel-Formalizer-V2 and Kimina-Autoformalizer on a benchmark of 300 OmniMath problems. Results are shown in Table 1.
86	
87	**Formal-based scaffolded data synthesis.** When the prover fails to find a proof for a challenging problem, we can still leverage the proof attempt to generate simpler, related problems. The intuition is that even an incorrect proof attempt may introduce valid subgoals that represent easier subproblems. We utilize a powerful tactic in Lean, `extract_goal`, to capture the unsolved states of a proof. These extracted goals (together with the preconditions), which are well-formed mathematical statements, are then used to augment our training data for the next phase. Since an extracted statement is not guaranteed to be provable, we also include its negation, thereby training the model to recognize both true and false propositions.
88	
89	**Informal-based scaffolded data synthesis.** Another way of scaffolded data synthesis is to leverage the current LLMs’ mathematical reasoning ability in natural language, to create math statements at the right level for the model to learn. For a given problem, we prompt an LLM (Qwen3-32B) to generate simpler/sub-problems if it is unsolved, or harder variants if it is already solved. To improve generation quality, we first have the LLM attempt a natural language solution to the original problem, using its output as context. The generated informal statements are then formalized into Lean by the formalization pipeline we described in **Formalizer Training**. To avoid the inference overhead of incorrect or trivial statements, we use an LLM-based filter that assesses each statement for correctness and difficulty, where trivial or mathematically incorrect statements are discarded (the negation of incorrect statements are also added to the dataset). This filtering process significantly accelerates data synthesis, with a minor trade-off in potentially discarding some valid statements due to LLM judgment errors. The prompts and further details are in Appendix D.
90	
91	### 2.3 TRAINING ALGORITHMS
92	
93	**Supervised fine-tuning and expert iteration.** We follow the standard pipeline of Expert Iteration by iterating between using the model to conduct large-scale inference on the statement sets, collectingThe diagram illustrates the model training pipeline. It starts with a **Formal Statement** box. From this box, three paths emerge:
94	 
95	
96	- An orange arrow labeled **Distill** leads to a box labeled **Deepseek-Prover-V2-7B/671B**.
97	- An orange arrow labeled **Scaffolded Data Synthesis** leads to **Dataset S&lt;sub>3&lt;/sub>**.
98	- An orange arrow labeled **Self-Correct** leads to a box labeled **Deepseek-Prover-V2-671B**.
99	
100	 From the **Deepseek-Prover-V2-7B/671B** box, an orange arrow labeled **Distill** leads to **Dataset S&lt;sub>1&lt;/sub>**. From the **Deepseek-Prover-V2-671B** box, an orange arrow labeled **Self-Correct** leads to **Corrected Proof**. A dashed arrow points from **Corrected Proof** to **Dataset S&lt;sub>2&lt;/sub>**.
101	   
102	 The training stages are represented by blue boxes:
103	 
104	
105	- **SFT-S&lt;sub>1&lt;/sub>** receives an orange arrow from **Dataset S&lt;sub>1&lt;/sub>** and a blue arrow labeled **SFT** from **Dataset S&lt;sub>1&lt;/sub>**.
106	- **SFT-S&lt;sub>2&lt;/sub>-AVG** receives an orange arrow from **Dataset S&lt;sub>2&lt;/sub>** and a blue arrow labeled **SFT+AVG** from **Dataset S&lt;sub>2&lt;/sub>**.
107	- **SFT-S&lt;sub>3&lt;/sub>-AVG** receives an orange arrow from **Dataset S&lt;sub>3&lt;/sub>** and a blue arrow labeled **SFT+AVG** from **Dataset S&lt;sub>3&lt;/sub>**.
108	- **RL+AVG** receives a blue arrow labeled **RL+AVG** from **SFT-S&lt;sub>2&lt;/sub>-AVG** and a blue arrow labeled **RL+AVG** from **SFT-S&lt;sub>3&lt;/sub>-AVG**.
109	
110	 Dashed arrows also indicate a flow from **Dataset S&lt;sub>1&lt;/sub>** to **Dataset S&lt;sub>2&lt;/sub>** and from **Dataset S&lt;sub>2&lt;/sub>** to **Dataset S&lt;sub>3&lt;/sub>**.
111	
112	Figure 3: The overall workflow of model training. “+AVG” denotes that the trained model is averaged with the base model after training. “RL+AVG” is the final output model. Detailed descriptions are provided in Section 2.4.
113	
114	correct proofs with reasoning traces, and fine-tuning the model further by Supervised Fine-tuning (SFT) on the collected samples.
115	
116	**Reinforcement learning.** We aim to train a model capable of generating complete proofs and correcting its own errors via verifier-guided self-correction. To this end, we adopt an efficient hybrid strategy. We first sample multiple complete proofs in parallel. For each sampled proof, we perform serial self-correction, generating one correction per round. This serial correction process aligns well with RL, which optimizes expected reward and has been shown to improve single-shot (pass@1) accuracy (Shao et al., 2024; Yue et al., 2025).
117	
118	Our RL implementation adopts a multi-task setup (illustrated in Appendix Figure 9): 50% of the inputs are used for whole proof generation, and the remaining 50% for first-round self-correction. We train for a single epoch, using approximately 46K and 67K unique inputs for the 8B and 32B models, respectively. On the algorithmic side, we use a hybrid GRPO-based approach (Shao et al., 2024). Compared to vanilla GRPO, our method removes group normalization as suggested by Dr.GRPO (Liu et al., 2025) to avoid inherent bias on length, incorporates clip-higher, overlong penalties, and dynamic sampling from DAPO (Yu et al., 2025), and excludes the KL regularization term from the objective to encourage exploration. A key observation is that question difficulty significantly impacts RL training. To address this, we modify the dynamic sampling strategy to only include problems with pass rates in the range  $(0, 0.75]$  during optimization. For further implementation details, see Appendix E.1.
119	
120	**Model averaging for enhanced diversity.** We observed that in the later stages of SFT and RL, the model’s diversity decreases. This is reflected by an increase in pass@1 but a decline in pass@N for larger values of N, such as N=32. We adopt model averaging to enhance model diversity (Wortsman et al., 2022b;a; Lin et al., 2023a;b; Dang et al., 2025). Specifically, let the parameters of the base model be denoted as  $\theta_0$ , and those of the fine-tuned model as  $\theta$ . We use the combined model parameters defined as  $(1 - \alpha)\theta_0 + \alpha\theta$ , where  $\alpha \in (0, 1)$ . Existing literature has demonstrated that this simple approach can significantly improve the feature diversity of the final model. Our observations also confirm that this method effectively enhances pass@N. We perform model averaging at each stage of the process. Specifically, we apply model averaging after completing SFT and use the averaged model as the starting point for RL. Once RL is completed, we perform model averaging again and use this averaged model as the final model.
121	
122	## 2.4 WHOLE PIPELINE: PUTTING EVERYTHING TOGETHER
123	
124	The pipeline consists of the following steps:
125	
126	- • We utilize Deepseek-Prover-V2-7B and Deepseek-Prover-V2-671B to perform large-scale inference, producing an initial supervised fine-tuning (SFT) dataset  $S_1$  for complete proof generation.- • We employ  $S_1$  to conduct SFT on both Qwen3-8B and Qwen3-32B, resulting in fine-tuned models SFT- $S_1$  for both the 8B and 32B variants&lt;sup>1&lt;/sup>.
127	- • Using SFT- $S_1$  and Deepseek-Prover-V2-671B, we annotate self-correction data. The self-correction data from Deepseek-Prover-V2-671B is inferred using NeMo-Skills&lt;sup>2&lt;/sup> with 144 H100s. This data is then incorporated back into  $S_1$  to create an enhanced dataset  $S_2$ . We subsequently perform SFT on both model sizes using  $S_2$ , yielding improved models SFT- $S_2$ . We perform model averaging between SFT- $S_2$  and the base model for both the 8B and 32B models, resulting in SFT- $S_2$ -AVG.
128	- • We perform scaffolded data synthesis with SFT- $S_2$ -AVG to generate the dataset  $S_3$ . Continuing the SFT process, we further improve the models by training SFT- $S_2$ -AVG on  $S_3$ , yielding SFT- $S_3$ , and subsequently obtain the averaged model SFT- $S_3$ -AVG.
129	- • We apply reinforcement learning to the SFT- $S_3$ -AVG and conduct model averaging and obtain the final model RL-AVG.
130	
131	The overall workflow is illustrated in Fig. 3.
132	
133	### 3 EVALUATION
134	
135	This section presents our experiment results on Goedel-Prover-V2. We first discuss our evaluation benchmarks (Section 3.1). Then, we discuss our main evaluation results on the selected benchmarks (Section 3.3), and correspondingly the scaling behavior (Section 3.4). Finally, we investigate the performance of reinforcement learning and model averaging (Section 3.6).
136	
137	#### 3.1 BENCHMARKS
138	
139	**MiniF2F.** MiniF2F (Zheng et al., 2021) consists of 488 problem statements (244 validation and 244 test problems) in Lean. The problems are drawn from high-school level competitions including the AMC, AIME, and the International Mathematical Olympiad (IMO). We use the version of MiniF2F provided by Kimina (Wang et al., 2025)&lt;sup>3&lt;/sup>, which has some incorrect statements fixed.
140	
141	**PutnamBench.** PutnamBench (Tsoukalas et al., 2024) focuses on college-level mathematics competition problems that are sourced from the William Lowell Putnam Mathematical Competition years 1962 - 2023. PutnamBench comprises 644 problems, covering algebra, analysis, number theory, geometry, combinatorics, probability, and set theory.
142	
143	**MathOlympiadBench.** We constructed MathOlympiadBench, which comprises 360 human-verified formalizations of Olympiad-level mathematical problems, sourced from Compfiles&lt;sup>4&lt;/sup> and IMOSLLearn4 repository&lt;sup>5&lt;/sup>. It contains 158 IMO problems from 1959 to 2024, 131 IMO shortlist problems covering 2006 to 2023, 68 national mathematical Olympiad problems, and 3 additional mathematical puzzles. The statistic of problem categories in MathOlympiadBench is presented in Figure 4, and Figure 5 visualizes humans’ formalizing and solving status of IMO problems in MathOlympiadBench. See Appendix A for more details of MathOlympiadBench and its comparison with MiniF2F.
144	
145	#### 3.2 EVALUATED METHODS
146	
147	Following previous works (Xin et al., 2024b; Lin et al., 2025; Dong & Ma, 2025; Ren et al., 2025) the evaluations are done under Lean 4.9.0-rc1. For the first round of whole-proof generation, the max token length of the model is set to be 30,000. For the verifier-guided error-correction, we sequentially conduct 2 additional rounds of self-correction, given the verifier’s feedback on the previous attempt. The total number of tokens in the self-correction mode is set to be 40,000. We report the pass@N metric.
148	
149	&lt;sup>1&lt;/sup>We use &lt;https://github.com/hiyouga/LLaMA-Factory> for SFT.
150	
151	&lt;sup>2&lt;/sup>&lt;https://github.com/NVIDIA/NeMo-Skills>
152	
153	&lt;sup>3&lt;/sup>[https://huggingface.co/datasets/AI-MO/minif2f\\_test](https://huggingface.co/datasets/AI-MO/minif2f_test)
154	
155	&lt;sup>4&lt;/sup>&lt;https://dwrensha.github.io/compfiles/imo.html>
156	
157	&lt;sup>5&lt;/sup>&lt;https://github.com/mortarsanjaya/IMOSLLearn4>Figure 4: Distribution of problems in MathOlympiadBench by category.
158	
159	Figure 5: Community’s achievement on IMO problems by year and problem index. Each cell represents a problem:  $\square$  statement not formalized,  $\blacksquare$  not solved, and  $\blacksquare$  solved.
160	
161	### 3.3 MAIN RESULTS
162	
163	Table 2: Performance of different whole-proof generation methods on MiniF2F test split.  $\dagger$  denotes concurrent work
164	
165	&lt;table border="1">
166	&lt;thead>
167	&lt;tr>
168	&lt;th>Method&lt;/th>
169	&lt;th>Budget&lt;/th>
170	&lt;th>Performance&lt;/th>
171	&lt;/tr>
172	&lt;/thead>
173	&lt;tbody>
174	&lt;tr>
175	&lt;td>Goedel-Prover-SFT (Lin et al., 2025)&lt;/td>
176	&lt;td>32&lt;br/>3200&lt;/td>
177	&lt;td>&lt;math>57.6\% \pm 0.7\%&lt;/math>&lt;br/>62.7%&lt;/td>
178	&lt;/tr>
179	&lt;tr>
180	&lt;td>STP (Dong &amp; Ma, 2025)&lt;/td>
181	&lt;td>128&lt;br/>3200&lt;br/>25600&lt;/td>
182	&lt;td>&lt;math>61.2\% \pm 0.6\%&lt;/math>&lt;br/>&lt;math>65.0\% \pm 0.5\%&lt;/math>&lt;br/>67.6%&lt;/td>
183	&lt;/tr>
184	&lt;tr>
185	&lt;td>Kimina-Prover-Preview-72B (Wang et al., 2025)&lt;/td>
186	&lt;td>32&lt;br/>8192&lt;/td>
187	&lt;td>68.85%&lt;br/>80.74%&lt;/td>
188	&lt;/tr>
189	&lt;tr>
190	&lt;td>DeepSeek-Prover-V2-7B (Ren et al., 2025)&lt;/td>
191	&lt;td>32&lt;br/>8192&lt;/td>
192	&lt;td>&lt;math>75.6\% \pm 0.5\%&lt;/math>&lt;br/>82.0%&lt;/td>
193	&lt;/tr>
194	&lt;tr>
195	&lt;td>DeepSeek-Prover-V2-671B&lt;/td>
196	&lt;td>32&lt;br/>8192&lt;/td>
197	&lt;td>&lt;math>82.4\% \pm 0.6\%&lt;/math>&lt;br/>88.9%&lt;/td>
198	&lt;/tr>
199	&lt;tr>
200	&lt;td>Kimina-Prover-8B&lt;math>^\dagger&lt;/math> (Wang et al., 2025)&lt;/td>
201	&lt;td>32&lt;/td>
202	&lt;td>78.3%&lt;/td>
203	&lt;/tr>
204	&lt;tr>
205	&lt;td>Kimina-Prover-70B&lt;math>^\dagger&lt;/math>&lt;/td>
206	&lt;td>32&lt;br/>1024&lt;/td>
207	&lt;td>84.0%&lt;br/>87.7%&lt;/td>
208	&lt;/tr>
209	&lt;tr>
210	&lt;td>w/ TTRL&lt;/td>
211	&lt;td>unknown&lt;/td>
212	&lt;td>92.2%&lt;/td>
213	&lt;/tr>
214	&lt;tr>
215	&lt;td>Goedel-Prover-V2-8B&lt;/td>
216	&lt;td>32&lt;br/>1024&lt;br/>8192&lt;/td>
217	&lt;td>&lt;math>84.6\% \pm 0.6\%&lt;/math>&lt;br/>87.9%&lt;br/>90.2%&lt;/td>
218	&lt;/tr>
219	&lt;tr>
220	&lt;td>w/ self-correction&lt;/td>
221	&lt;td>32&lt;br/>1024&lt;/td>
222	&lt;td>&lt;math>86.7\% \pm 0.2\%&lt;/math>&lt;br/>89.3%&lt;/td>
223	&lt;/tr>
224	&lt;tr>
225	&lt;td>Goedel-Prover-V2-32B&lt;/td>
226	&lt;td>32&lt;br/>1024&lt;br/>8192&lt;/td>
227	&lt;td>&lt;math>88.1\% \pm 0.8\%&lt;/math>&lt;br/>91.8%&lt;br/>92.2%&lt;/td>
228	&lt;/tr>
229	&lt;tr>
230	&lt;td>w/ self-correction&lt;/td>
231	&lt;td>32&lt;br/>1024&lt;/td>
232	&lt;td>&lt;math>90.4\% \pm 0.6\%&lt;/math>&lt;br/>92.6%&lt;/td>
233	&lt;/tr>
234	&lt;/tbody>
235	&lt;/table>
236	
237	The evaluation results of Goedel-Prover-V2 on MiniF2F are summarized in Table 2, and results on PutnamBench are shown in Table 3. The results for MathOlympiadBench are presented in the rightmost figure of Figure 1. Below, we summarize and discuss the results.
238	
239	**High performance at modest scale.** Our 32B model achieves pass@32 accuracy of 88.1% on MiniF2F, with 90.4% after 2 rounds of error-correction, exceeding the previous state-of-the-art DeepSeek-Prover-V2-671B’s 82.4% while using far fewer parameters. Even the 8B variant achieves84.6%, nearly matching or outperforming Kimina-Prover-70B’s results under the same inference budget, and outperforming the previous SOTA DeepSeek-Prover-V2-671B on MiniF2F, with a significant smaller model size. On PutnamBench, our 32B model solves 43 problems under pass@32, nearly doubling the DeepSeek-Prover-V2-671B model’s performance under the same budget. With error-correction, Goedel-Prover-V2-32B solves 57 problems under pass@32, outperforming DeepSeek-Prover-V2-671B under pass@1024. Under pass@184 and error correction, Goedel-Prover-V2-32B solves 86 on PutnamBench, securing the best open-source theorem prover on the leaderboard.
240	
241	Table 3: Comparison of different models on PutnamBench. Our Goedel-Prover-V2 with compiler-guided self-correction solves 86 problems from PutnamBench, improving the previous SOTA (DeepSeek-Prover-V2) by 39 more problems, and securing the best open-source model on the leaderboard.\*
242	
243	&lt;table border="1">
244	&lt;thead>
245	&lt;tr>
246	&lt;th>#&lt;/th>
247	&lt;th>Model&lt;/th>
248	&lt;th>num-solved&lt;/th>
249	&lt;th>open-source&lt;/th>
250	&lt;th>compute&lt;/th>
251	&lt;/tr>
252	&lt;/thead>
253	&lt;tbody>
254	&lt;tr>
255	&lt;td>1&lt;/td>
256	&lt;td>&lt;b>Godel-Prover-V2 (self-correction mode)&lt;/b>&lt;/td>
257	&lt;td>86&lt;/td>
258	&lt;td>✓&lt;/td>
259	&lt;td>pass@184&lt;/td>
260	&lt;/tr>
261	&lt;tr>
262	&lt;td>1&lt;/td>
263	&lt;td>&lt;b>Godel-Prover-V2 (self-correction mode)&lt;/b>&lt;/td>
264	&lt;td>57&lt;/td>
265	&lt;td>✓&lt;/td>
266	&lt;td>pass@32&lt;/td>
267	&lt;/tr>
268	&lt;tr>
269	&lt;td>1&lt;/td>
270	&lt;td>&lt;b>Godel-Prover-V2&lt;/b>&lt;/td>
271	&lt;td>43&lt;/td>
272	&lt;td>✓&lt;/td>
273	&lt;td>pass@32&lt;/td>
274	&lt;/tr>
275	&lt;tr>
276	&lt;td>2&lt;/td>
277	&lt;td>DeepSeek-Prover-V2&lt;/td>
278	&lt;td>47&lt;/td>
279	&lt;td>✓&lt;/td>
280	&lt;td>pass@1024&lt;/td>
281	&lt;/tr>
282	&lt;tr>
283	&lt;td>2&lt;/td>
284	&lt;td>DeepSeek-Prover-V2&lt;/td>
285	&lt;td>22&lt;/td>
286	&lt;td>✓&lt;/td>
287	&lt;td>pass@32&lt;/td>
288	&lt;/tr>
289	&lt;tr>
290	&lt;td>3&lt;/td>
291	&lt;td>DSP+&lt;/td>
292	&lt;td>23&lt;/td>
293	&lt;td>✓&lt;/td>
294	&lt;td>pass@128&lt;/td>
295	&lt;/tr>
296	&lt;tr>
297	&lt;td>4&lt;/td>
298	&lt;td>Bourbaki&lt;/td>
299	&lt;td>14&lt;/td>
300	&lt;td>✓&lt;/td>
301	&lt;td>pass@512&lt;/td>
302	&lt;/tr>
303	&lt;tr>
304	&lt;td>5&lt;/td>
305	&lt;td>Kimina-Prover-7B-Distill&lt;/td>
306	&lt;td>10&lt;/td>
307	&lt;td>✓&lt;/td>
308	&lt;td>pass@192&lt;/td>
309	&lt;/tr>
310	&lt;tr>
311	&lt;td>6&lt;/td>
312	&lt;td>Self-play Theorem Prover&lt;/td>
313	&lt;td>8&lt;/td>
314	&lt;td>✓&lt;/td>
315	&lt;td>pass@3200&lt;/td>
316	&lt;/tr>
317	&lt;tr>
318	&lt;td>7&lt;/td>
319	&lt;td>Godel-Prover-SFT&lt;/td>
320	&lt;td>7&lt;/td>
321	&lt;td>✓&lt;/td>
322	&lt;td>pass@512&lt;/td>
323	&lt;/tr>
324	&lt;tr>
325	&lt;td>8&lt;/td>
326	&lt;td>ABEL&lt;/td>
327	&lt;td>7&lt;/td>
328	&lt;td>×&lt;/td>
329	&lt;td>pass@596&lt;/td>
330	&lt;/tr>
331	&lt;/tbody>
332	&lt;/table>
333	
334	\* A concurrent work, Seed Prover (Chen et al., 2025), successfully solved 331 problems on PutnamBench. However, the prover is not open-source, and it is not clear what the computational budget is at test time (which is expected to be much larger than ours).
335	
336	**Efficacy of verifier-guided self-correction.** Adding self-correction provides a consistent gain of approximately 2 percentage points in pass@32 for both models on MiniF2F. On PutnamBench, error correction leads to 14 more solves under pass@32. This demonstrates that integrating Lean compiler feedback into a long-chain-of-thought revision pipeline enables the model to identify errors and repair them effectively.
337	
338	**Sample-efficient inference.** Unlike prior models such as Kimina-Prover and DeepSeek-Prover-V2, which rely heavily on large sampling budgets or test-time reinforcement learning to reach peak accuracy, Goedel-Prover-V2 attains very high pass@N with minimal inference overhead (N=32 or 64), indicating that the model internalizes powerful reasoning strategies during training. The sample efficiency, together with the relatively small size, makes Goedel-Prover-V2 series a very good candidate for the community to develop new algorithms and test on different benchmarks.
339	
340	### 3.4 SCALING ANALYSIS
341	
342	Figure 6 and Table 4 illustrate the scaling behavior of Goedel-Prover-V2 (8B and 32B variants) across different inference budgets, compared against DeepSeek-Prover-V2 (7B and 671B) and Kimina-Prover-72B. At the lower sampling regime (pass@32), Goedel-Prover-V2-32B already achieves 88.1%, notably surpassing DeepSeek-Prover-V2-671B (82.4%) and Kimina-Prover-72B (84.0%). This advantage persists across inference budgets, with our self-correction mode providing approximately a 2-point performance improvement under pass@32 and pass@64, peaking at 92.6% at pass@8192. The smaller 8B model also demonstrates strong scalability, surpassing the 671B DeepSeek model at all budgets.
343	
344	Figure 6: Scaling behavior on MiniF2F test split.&lt;table border="1">
345	&lt;thead>
346	&lt;tr>
347	&lt;th>Model&lt;/th>
348	&lt;th>32&lt;/th>
349	&lt;th>64&lt;/th>
350	&lt;th>128&lt;/th>
351	&lt;th>256&lt;/th>
352	&lt;th>512&lt;/th>
353	&lt;th>1024&lt;/th>
354	&lt;th>2048&lt;/th>
355	&lt;th>4096&lt;/th>
356	&lt;th>8192&lt;/th>
357	&lt;/tr>
358	&lt;/thead>
359	&lt;tbody>
360	&lt;tr>
361	&lt;td>32B (self-correction mode)&lt;/td>
362	&lt;td>90.4&lt;/td>
363	&lt;td>91.4&lt;/td>
364	&lt;td>91.9&lt;/td>
365	&lt;td>92.3&lt;/td>
366	&lt;td>92.4&lt;/td>
367	&lt;td>92.6&lt;/td>
368	&lt;td>—&lt;/td>
369	&lt;td>—&lt;/td>
370	&lt;td>—&lt;/td>
371	&lt;/tr>
372	&lt;tr>
373	&lt;td>32B&lt;/td>
374	&lt;td>88.1&lt;/td>
375	&lt;td>89.8&lt;/td>
376	&lt;td>90.5&lt;/td>
377	&lt;td>91.0&lt;/td>
378	&lt;td>91.6&lt;/td>
379	&lt;td>91.8&lt;/td>
380	&lt;td>92.0&lt;/td>
381	&lt;td>92.2&lt;/td>
382	&lt;td>92.2&lt;/td>
383	&lt;/tr>
384	&lt;tr>
385	&lt;td>8B (self-correction mode)&lt;/td>
386	&lt;td>86.7&lt;/td>
387	&lt;td>86.9&lt;/td>
388	&lt;td>87.4&lt;/td>
389	&lt;td>88.0&lt;/td>
390	&lt;td>88.5&lt;/td>
391	&lt;td>89.3&lt;/td>
392	&lt;td>—&lt;/td>
393	&lt;td>—&lt;/td>
394	&lt;td>—&lt;/td>
395	&lt;/tr>
396	&lt;tr>
397	&lt;td>8B&lt;/td>
398	&lt;td>84.6&lt;/td>
399	&lt;td>86.1&lt;/td>
400	&lt;td>86.5&lt;/td>
401	&lt;td>87.0&lt;/td>
402	&lt;td>87.4&lt;/td>
403	&lt;td>87.9&lt;/td>
404	&lt;td>88.5&lt;/td>
405	&lt;td>89.3&lt;/td>
406	&lt;td>90.2&lt;/td>
407	&lt;/tr>
408	&lt;/tbody>
409	&lt;/table>
410	
411	Table 4: The performance (%) of Goedel-Prover-V2 on MiniF2F across different compute budget.
412	
413	These results indicate that Goedel-Prover-V2 efficiently internalizes reasoning during training, requiring fewer inference samples to achieve comparable or superior accuracy. Furthermore, the consistent gains from verifier-guided self-correction across all inference budgets further underscore the value of combining error correction with long-chain-of-thought reasoning in formal theorem proving.
414	
415	### 3.5 ANALYSIS OF SELF-CORRECTION
416	
417	In our main experiments, self-correction was conducted for a maximum of 2 rounds with a 40k token context length. To further explore its capabilities, we used YaRN (Peng et al., 2024) to extend the context length to 128k tokens and allowed up to 5 revision iterations. We conducted a series of experiments on the MiniF2F benchmark at pass@32, the results of which are presented in Figure 7. Alongside our standard prompting setup (Self Correction), we performed two ablation studies: (1) removing the specific compiler error messages (w/o Error Messages), and (2) removing the chain-of-thought from previous attempts, retaining only the formal proof (w/o Previous CoTs).
418	
419	Figure 7: Ablation study on self-correction with extended context length and revision iterations on the MiniF2F test split at pass@32.
420	
421	The results show that removing compiler feedback significantly lowers performance, confirming that specific error messages are crucial for effective revision. Similarly, removing the reasoning from previous attempts also slightly degrades performance, indicating that retaining the chain-of-thought from prior rounds is beneficial. Furthermore, with an extended context and more revision iterations, the full self-correction model’s pass@32 accuracy on MiniF2F reaches an average of 92.7%, which surpasses the 92.2% performance of the model without self-correction at pass@8192, highlighting the sample efficiency of our iterative revision process.
422	
423	### 3.6 RL AND MODEL AVERAGING
424	
425	We systematically evaluate the impact of RL steps and model averaging strategies on the performance of Goedel-Prover-V2. Specifically, for RL checkpoints at steps 60, 80, and 90, we apply model averaging with coefficients  $\alpha = 0.6, 0.7, 0.8, 0.9$  (where  $\alpha$  is the weight of the base model). We assess each averaged model in both vanilla (whole-proof generation) and correction (with self-correction) settings, evaluating both pass@1 and pass@N, as visualized in Figure 8.
426	
427	For both vanilla and correction settings, pass@1 consistently increases as the number of RL steps grows. For vanilla pass@N, performance stabilizes at higher RL steps, whereas in the correction setting, pass@N continues to improve. This indicates that correction benefits more from RL, likely due to the shortage of high-quality self-correction data in the SFT stages.
428	
429	Examining different values of  $\alpha$ , we observe that a higher proportion of the base model (i.e., lower  $\alpha$ ) leads to lower pass@1, but pass@N first rises and then falls as  $\alpha$  increases. There exists an optimal model averaging ratio that maximizes pass@N. This trend holds for both vanilla and correction settings, with the improvement being more pronounced for correction. This suggests that model averaging not only improves sample diversity but also amplifies the benefits of RL-driven self-correction.Figure 8: The effects of varying RL steps and model averaging ratios on the pass@1 and pass@32 performance of models, both with and without correction.
430	
431	## 4 RELATED WORKS
432	
433	**Formal Theorem Proving as Whole Proof Generation.** Inspired by the success of end-to-end reasoning in informal LLMs, recent foundational work in formal theorem proving has adopted a similar strategy: generating entire Lean proofs in a single pass. While informal reasoning models often struggle with step verification—producing fluent yet logically flawed arguments (Petrov et al., 2025)—formal settings like Lean (De Moura et al., 2015) offer a precise and executable verifier that enforces correctness. Leveraging this, models such as DeepSeek-Prover (Xin et al., 2024a), Goedel Prover (Lin et al., 2025), and Kimina Prover (Wang et al., 2025) demonstrate that end-to-end generation can produce formally verified proofs that are immediately checkable by the Lean proof assistant. This paradigm retains the global coherence and simplicity of sequence generation while grounding outputs in verifiable formal logic.
434	
435	**Formal Theorem Proving using Proof Search.** In contrast to end-to-end generation, proof search-based methods guide the model to incrementally construct proofs by exploring derivation paths with verifier feedback at each step. Recent systems such as InternLM2.5-StepProver (Wu et al., 2024), Hunyuan Prover (Li et al., 2024), DeepSeek-Prover v1.5 (Xin et al., 2024b), and BFS Prover (Xin et al., 2025) employ tree search algorithms—such as Monte Carlo Tree Search or breadth-first search—to explore multiple proof trajectories and iteratively assemble valid proofs. While this strategy improves correctness, it comes at the cost of significantly higher computational overhead, as the model must evaluate and verify a large number of partial branches. Recently, hybrid methods, which use a general-purpose (strong) LLM to write the proof sketch and query theorem provers to fill in the proof for small steps, also emerged (DSP+ (Cao et al., 2025) and the concurrent work Delta-Prover (Zhou et al., 2025)). However, these works usually require the LLM to be very large and powerful, where DSP+ uses 671B DeepSeek-R1 (Guo et al., 2025) or DeepSeek-V3 (Liu et al., 2024), and Delta-Prover uses Gemini (Comanici et al., 2025). Notably, Seed-Prover (Chen et al., 2025) employs a wide range of techniques, including extensive test-time search and refinement, and achieves IMO medal-level performance. However, it requires substantial computational resources.
436	
437	**Self-Repair and Verifier-Guided Refinement.** While tree-based proof search improves correctness, its high computational cost has motivated the development of more efficient mechanisms for guiding search and enabling self-refinement. One direction explores how auxiliary signals or intermediate structures can streamline the reasoning process. Jiang et al. (2023); Gloeckle et al. (2024); Cao et al. (2025) bridge informal and formal reasoning by using informal sketches as a skeleton for formal proof generation, while Yang et al. (2024) employs retrieval-augmented generation (RAG) to retrieve relevant theorems from formal libraries during proof construction. Other approaches, such as Ji et al. (2025), implement self-verification and iterative refinement loops, allowing models to autonomously revise candidate proofs using verifier feedback.
438	
439	Verifier-in-the-loop strategies in recent works (Baba et al., 2025; Zhou et al., 2025; Ren et al., 2025; Wang et al., 2025; Chen et al., 2025), also highlight the benefits of interactive feedback, improving success rates through iterative correction rather than brute-force search. These methods collectivelypoint to a more flexible and scalable paradigm: enabling the model to diagnose and repair its own outputs with minimal external supervision.
440	
441	Goedel-Prover-V2 builds on this trajectory by adopting a self-revision framework, where the model iteratively proposes and refines candidate proofs until they satisfy the Lean checker. This architecture draws inspiration from general-purpose self-repair frameworks in coding and reasoning (Yao et al., 2023; Shinn et al., 2023; First et al., 2023; Olausson et al., 2024; Chen et al., 2024; Bouzenia et al., 2024), bringing their iterative refinement loop into the domain of formal mathematics with long chain-of-thought reasoning.
442	
443	## 5 CONCLUSION AND DISCUSSION
444	
445	In this work, we introduced **Goedel-Prover-V2**, a series of state-of-the-art open-source theorem provers that significantly advance automated formal proof generation. Our key innovation is the integration of long-chain-of-thought reasoning with compiler-guided self-correction, addressing a crucial gap overlooked by prior methods. Through scaffolded data synthesis, SFT and RL training, and model averaging, our models achieve state-of-the-art performance among open-source provers. In particular, our 32B model achieves 88.1% on MiniF2F at pass@32 and benefits further from self-correction and reaching 90.4% on MiniF2F at pass@32, outperforming larger models with lower inference cost. Moreover, our 8B model also outperforms the previous SOTA DeepSeek-Prover-V2-671B under pass@32 on MiniF2F with a significant smaller model size.
446	
447	We also investigate a proof repair strategy as a test-time alternative to standard pass@k sampling. Instead of regenerating an entire failed proof, our method corrects only the faulty segment. We use Lean 4’s compiler feedback and the `extract_goal` tactic to isolate the unsolved subgoal, prompt the prover to solve it independently, and then reinsert the correct solution into the original proof. On the MiniF2F benchmark, this approach improves the amortized budget scaling curve by 1–2 percentage points, highlighting inference-time scaling strategies as a key direction for future work.
448	
449	By open-sourcing all trained models, we aim to catalyze further advancements in formal reasoning research. We envision that the release of Goedel-Prover-V2 will not only establish a new benchmark for automated theorem proving but also provide a practical, efficient platform upon which future innovations can be built.
450	
451	## ACKNOWLEDGEMENT
452	
453	This project was the result of a close collaborative effort by all authors, and every major component benefited from joint discussion and iteration. The author would like to thank Igor Gitman for support with the curation of self-correction data.
454	
455	HZ and SA acknowledge the support from Schmidt, Darpa, ONR, and NSF. CJ acknowledges the support from NSF-OAC-2411299, NSF-IIS-2239297, and Princeton AI Lab Seed Fund.
456	
457	## REFERENCES
458	
459	Kaito Baba, Chaoran Liu, Shuhei Kurita, and Akiyoshi Sannai. Prover agent: An agent-based framework for formal mathematical proofs. *arXiv preprint arXiv:2506.19923*, 2025.
460	
461	Islem Bouzenia, Premkumar Devanbu, and Michael Pradel. Repairagent: An autonomous, llm-based agent for program repair. *arXiv preprint arXiv:2403.17134*, 2024.
462	
463	Chenrui Cao, Liangcheng Song, Zenan Li, Xinyi Le, Xian Zhang, Hui Xue, and Fan Yang. Reviving dsp for advanced theorem proving in the era of reasoning models. *arXiv preprint arXiv:2506.11487*, 2025.
464	
465	Luoxin Chen, Jinming Gu, Liankai Huang, Wenhao Huang, Zhicheng Jiang, Allan Jie, Xiaoran Jin, Xing Jin, Chenggang Li, Kaijing Ma, Cheng Ren, Jiawei Shen, Wenlei Shi, Tong Sun, He Sun, Jiahui Wang, Siran Wang, Zhihong Wang, Chenrui Wei, Shufa Wei, Yonghui Wu, Yuchen Wu, Yihang Xia, Huajian Xin, Fan Yang, Huaiyuan Ying, Hongyi Yuan, Zheng Yuan, Tianyang Zhan, Chi Zhang, Yue Zhang, Ge Zhang, Tianyun Zhao, Jianqiu Zhao, Yichi Zhou, and Thomas HanwenZhu. Seed-prover: Deep and broad reasoning for automated theorem proving, 2025. URL &lt;https://arxiv.org/abs/2507.23726>.
466	
467	Xinyun Chen, Maxwell Lin, Nathanael Schärli, and Denny Zhou. Teaching large language models to self-debug. In *The Twelfth International Conference on Learning Representations*, 2024.
468	
469	Yuri Chervonyi, Trieu H Trinh, Miroslav Olšák, Xiaomeng Yang, Hoang Nguyen, Marcelo Menegali, Junehyuk Jung, Vikas Verma, Quoc V Le, and Thang Luong. Gold-medalist performance in solving olympiad geometry with AlphaGeometry2. *arXiv preprint arXiv:2502.03544*, 2025.
470	
471	Gheorghe Comanici, Eric Bieber, Mike Schaeckermann, Ice Pasupat, Noveen Sachdeva, Inderjit Dhillon, Marcel Blstein, Ori Ram, Dan Zhang, Evan Rosen, et al. Gemini 2.5: Pushing the frontier with advanced reasoning, multimodality, long context, and next generation agentic capabilities. *arXiv preprint arXiv:2507.06261*, 2025.
472	
473	Xingyu Dang, Christina Baek, J Zico Kolter, and Aditi Raghunathan. Assessing diversity collapse in reasoning. In *Scaling Self-Improving Foundation Models without Human Supervision*, 2025.
474	
475	Leonardo De Moura, Soonho Kong, Jeremy Avigad, Floris Van Doorn, and Jakob von Raumer. The lean theorem prover (system description). In *Automated Deduction-CADE-25: 25th International Conference on Automated Deduction, Berlin, Germany, August 1-7, 2015, Proceedings 25*, pp. 378–388. Springer, 2015.
476	
477	Kefan Dong and Tengyu Ma. STP: Self-play LLM theorem provers with iterative conjecturing and proving. In *International Conference on Machine Learning (ICML)*, 2025.
478	
479	Emily First, Markus N Rabe, Talia Ringer, and Yuriy Brun. Baldur: Whole-proof generation and repair with large language models. In *ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering (ESEC/FSE)*, 2023.
480	
481	Fabian Gloeckle, Jannis Limperg, Gabriel Synnaeve, and Amaury Hayat. Abel: Sample efficient online reinforcement learning for neural theorem proving. In *The 4th Workshop on Mathematical Reasoning and AI at NeurIPS'24*, 2024.
482	
483	Google DeepMind. AI achieves silver-medal standard solving international mathematical olympiad problems. &lt;https://deepmind.google/discover/blog/ai-solves-imo-problems-at-silver-medal-level/>, 2024.
484	
485	Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. *arXiv preprint arXiv:2501.12948*, 2025.
486	
487	Aaron Jaech, Adam Kalai, Adam Lerer, Adam Richardson, Ahmed El-Kishky, Aiden Low, Alec Helyar, Aleksander Madry, Alex Beutel, Alex Carney, et al. Openai o1 system card. *arXiv preprint arXiv:2412.16720*, 2024.
488	
489	Xingguang Ji, Yahui Liu, Qi Wang, Jingyuan Zhang, Yang Yue, Rui Shi, Chenxi Sun, Fuzheng Zhang, Guorui Zhou, and Kun Gai. Leanabell-prover-v2: Verifier-integrated reasoning for formal theorem proving via reinforcement learning. *arXiv preprint arXiv:2507.08649*, 2025.
490	
491	Albert Qiaochu Jiang, Sean Welleck, Jin Peng Zhou, Timothee Lacroix, Jiacheng Liu, Wenda Li, Mateja Jamnik, Guillaume Lample, and Yuhuai Wu. Draft, sketch, and prove: Guiding formal theorem provers with informal proofs. In *The Eleventh International Conference on Learning Representations*, 2023.
492	
493	Yang Li, Dong Du, Linfeng Song, Chen Li, Weikang Wang, Tao Yang, and Haitao Mi. Hunyuanprover: A scalable data synthesis framework and guided tree search for automated theorem proving. *arXiv preprint arXiv:2412.20735*, 2024.
494	
495	Yong Lin, Hangyu Lin, Wei Xiong, Shizhe Diao, Jianmeng Liu, Jipeng Zhang, Rui Pan, Haoxiang Wang, Wenbin Hu, Hanning Zhang, et al. Mitigating the alignment tax of rlhf. *arXiv preprint arXiv:2309.06256*, 2023a.Yong Lin, Lu Tan, Yifan Hao, Honam Wong, Hanze Dong, Weizhong Zhang, Yujiu Yang, and Tong Zhang. Spurious feature diversification improves out-of-distribution generalization. *arXiv preprint arXiv:2309.17230*, 2023b.
496	
497	Yong Lin, Shange Tang, Bohan Lyu, Jiayun Wu, Hongzhou Lin, Kaiyu Yang, Jia Li, Mengzhou Xia, Danqi Chen, Sanjeev Arora, et al. Goedel-Prover: A frontier model for open-source automated theorem proving. *arXiv preprint arXiv:2502.07640*, 2025.
498	
499	Aixin Liu, Bei Feng, Bing Xue, Bingxuan Wang, Bochao Wu, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chenyu Zhang, Chong Ruan, et al. Deepseek-v3 technical report. *arXiv preprint arXiv:2412.19437*, 2024.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "64eae359-35cf-482c-bdab-96d75791e811",
  "isSidechain": false,
  "promptId": "918f738b-eddd-4a71-9661-57e87bd9f8ed",
  "type": "user",
  "uuid": "552a41fa-41b2-4084-b8dc-a171b7ff7d8d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/6db262d6-dcf8-4dbf-b94b-349936024bbc/tool-results/toolu_01Tq8krFT3t8xgN1SnQrexGw.txt",
      "content": "# GOEDEL-PROVER-V2: SCALING FORMAL THEOREM PROVING WITH SCAFFOLDED DATA SYNTHESIS AND SELF-CORRECTION\n\nYong Lin&lt;sup>1\\*&lt;/sup>, Shange Tang&lt;sup>1 2\\*&lt;/sup>, Bohan Lyu&lt;sup>3\\*&lt;/sup>, Ziran Yang&lt;sup>1\\*&lt;/sup>, Jui-Hui Chung&lt;sup>1\\*&lt;/sup>,  \n Haoyu Zhao&lt;sup>1\\*&lt;/sup>, Lai Jiang&lt;sup>7\\*&lt;/sup>, Yihan Geng&lt;sup>8\\*&lt;/sup>, Jiawei Ge&lt;sup>1&lt;/sup>, Jingruo Sun&lt;sup>4&lt;/sup>,  \n Jiayun Wu&lt;sup>3&lt;/sup>, Jiri Gesi&lt;sup>6 †&lt;/sup>, Ximing Lu&lt;sup>2&lt;/sup>, David Acuna&lt;sup>2&lt;/sup>, Kaiyu Yang&lt;sup>5 ‡&lt;/sup>,  \n Hongzhou Lin&lt;sup>6 \\*†&lt;/sup>, Yejin Choi&lt;sup>2 4&lt;/sup>, Danqi Chen&lt;sup>1&lt;/sup>, Sanjeev Arora&lt;sup>1&lt;/sup>, Chi Jin&lt;sup>1\\*&lt;/sup>\n\n&lt;sup>1&lt;/sup>Princeton Language and Intelligence, Princeton University &lt;sup>2&lt;/sup>NVIDIA  \n&lt;sup>3&lt;/sup>Tsinghua University &lt;sup>4&lt;/sup>Stanford University &lt;sup>5&lt;/sup>Meta FAIR &lt;sup>6&lt;/sup>Amazon  \n&lt;sup>7&lt;/sup>Shanghai Jiao Tong University &lt;sup>8&lt;/sup>Peking University\n\n## ABSTRACT\n\nWe introduce Goedel-Prover-V2, a series of open-source language models that set a new state-of-the-art in automated theorem proving. Built on the standard expert iteration and reinforcement learning pipeline, our approach incorporates three key innovations: (1) Scaffolded data synthesis: We generate synthetic tasks of increasing difficulty to train the model to master increasingly complex theorems; (2) Verifier-guided self-correction: We enable the model to iteratively revise its proofs by leveraging feedback from the Lean compiler; (3) Model averaging: We merge model checkpoints to mitigate the decrease in model output diversity in later stages of training. Our small model, Goedel-Prover-V2-8B, reaches 84.6% pass@32 on MiniF2F and outperforms DeepSeek-Prover-V2-671B under the same metric, despite being 80X smaller. Our flagship model, Goedel-Prover-V2-32B, achieves 88.1% on MiniF2F at pass@32 in standard mode and 90.4% in self-correction mode, outperforming prior SOTA by a large margin. Additionally, our flagship model solves 86 problems on PutnamBench at pass@184, securing the first place among open-source models on the leaderboard, surpassing DeepSeek-Prover-V2-671B’s record of solving 47 problems by pass@1024 with a significantly smaller model size and compute budget. At the time of its release (July–August 2025), Goedel-Prover-V2 achieves the strongest overall performance among all open-source theorem provers. It also ranks among the top-performing models—including closed-source systems with publicly reported performance—under a constrained test-time compute budget. Our models, code, and data are released at &lt;https://github.com/Goedel-LM/Goedel-Prover-V2>.\n\n## 1 INTRODUCTION\n\nAutomated theorem proving (ATP) is a grand challenge for AI, requiring the construction of step-by-step, machine-verifiable proofs in formal languages like Lean (De Moura et al., 2015; Moura & Ullrich, 2021). Unlike reasoning in natural language, ATP demands a completely rigorous logical flow, which poses an exceptional challenge for AI systems. The field has advanced rapidly in recent years; for example, DeepMind’s AlphaProof (Google DeepMind, 2024) and AlphaGeometry (Trinh et al., 2024; Chervonyi et al., 2025) demonstrated that AI systems are capable of achieving IMO (International Math Olympiad) medal-level performance. Furthermore, open-source efforts such as DeepSeek-Prover-V2 (Ren et al., 2025) and Kimina-Prover (Wang et al., 2025) have achieved impressive results on benchmarks like MiniF2F (Zheng et al., 2021) and PutnamBench (Tsoukalas et al., 2024), demonstrating the effectiveness of leveraging the reasoning ability of LLMs through\n\n\\*Core Contributor.\n\n†This work is independent of and outside of the work at Amazon.\n\n‡All experiments and data processing were conducted outside Meta.Figure 1: Performance of Goedel-Prover-V2 on different benchmarks under pass@32.\n\nchain-of-thoughts. These successes, however, typically depend on massive models (e.g., DeepSeek-Prover-V2 has 671B parameters) or computationally intensive inference (e.g., the concurrent work Seed-Prover (Chen et al., 2025)), which involves complex search algorithms and enormous search budgets.\n\nIn this work we introduce Goedel-Prover-V2, a new series of open-source models for automated theorem proving in Lean that establish a new state-of-the-art in both performance and computational efficiency. The models are capable of generating whole proof and leveraging verifier feedback for iterative self-correction. Our flagship 32B model achieves 88.1% pass@32 on the MiniF2F benchmark, improving to 90.4% with self-correction. This performance surpasses both the concurrent 72B Kimina-Prover and the previous SOTA 671B DeepSeek-Prover-V2, while using significantly fewer parameters (Figure 1). On the more challenging PutnamBench, our model solves 44 problems (57 with self-correction), more than doubling the number solved by DeepSeek-Prover-V2 under the same metric. The efficiency of our approach is further underscored by our 8B model, which alone outperforms the 671B DeepSeek-Prover-V2 on MiniF2F despite being nearly 80 times smaller. At the time of its release (July–August 2025), Goedel-Prover-V2 achieves the strongest overall performance among all open-source theorem provers. It also ranks among the top-performing models—including closed-source systems with publicly reported performance—under small test-time compute budgets.\n\nThe key to these gains lies in novel design across the framework, data, and training pipelines. We highlight the main components below:\n\n- • **Verifier-guided self-correction:** Framework-wise, we incorporate feedback from the Lean compiler (verifier) into the model input to enable the error-correction ability of our theorem prover (*verifier-guided self-correction*). While correcting errors based on verifier feedback has been studied in theorem proving (First et al., 2023) and coding (Olausson et al., 2024; Chen et al., 2024; Bouzenia et al., 2024), we further incorporate this into models that generate long chain-of-thought (CoT) reasoning, which is effective for complex reasoning tasks such as ATP (Jaech et al., 2024; Guo et al., 2025; Wang et al., 2025; Ren et al., 2025).\n- • **Scaffolded data synthesis:** Successfully combining long CoT with verifier-guided error correction requires special efforts on curating data. In addition to formalizing existing math problems and curating data for error correction, we augment our training statement set through *scaffolded data synthesis*. This technique creates math problems at an appropriate difficulty level to provide the model with better learning signals.\n- • **Model averaging:** Our training recipe extends beyond standard expert iteration and reinforcement learning. We also apply *model averaging* (Wortsman et al., 2022b) to mitigate the decrease in model output diversity that can occur in the later stages of training.\n\nOverall, our results demonstrate that the frontier of formal theorem proving can be advanced without access to extremely large models, a vast computational resources, or proprietary technology. We hopethat our open-source theorem prover series, Goedel-Prover-V2, will enable the community to build upon them and accelerate progress toward AI systems that can reliably solve and verify complex mathematical problems, and ultimately bridge the long-standing divide between intuitive human reasoning and formal proof verification.\n\nThe following paper is organized as follows: in Section 2, we introduce our main methods to train Goedel-Prover-V2, including the verifier-guided self-correction framework (Section 2.1), scaffolded data synthesis (Section 2.2), and the training pipeline (Section 2.3). In Section 3, we present the evaluation results on Goedel-Prover-V2, including evaluation on both standard and our curated benchmarks (Section 3.3), scaling behavior under different test-time budgets (Section 3.4), and a study of reinforcement learning and model averaging (Section 3.6). Finally, we review the previous works (Section 4) and discuss the connection with Goedel-Prover-V2.\n\n## 2 METHOD\n\nIn this section, we present our method in detail. We start with the key framework innovation compared to the previous vanilla whole-proof generation methods (e.g. DeepSeek-Prover-V2) by utilizing the feedback from the Lean compiler to guide the proof-correction procedure (Section 2.1). Then, in Section 2.2, we demonstrate how to curate the training data (statements), with an emphasis on augmenting the data through scaffolded data synthesis. Based on the curated data, we present the details of training our theorem prover in Section 2.3, which includes supervised fine-tuning (SFT), reinforcement learning (RL), and model averaging. Section 2.4 provides a summary of the overall framework.\n\n### 2.1 CHAIN-OF-THOUGHT AND SELF-CORRECTION\n\nPrevailing paradigms for whole-proof generation in automated theorem proving have largely been “end-to-end,” where a model generates a complete formal proof from a theorem statement in a single pass (Xin et al., 2024b; Lin et al., 2025; Dong & Ma, 2025). Recent work has significantly advanced this approach by leveraging the long-chain-of-thought reasoning capabilities of large models (Wang et al., 2025; Ren et al., 2025).\n\nA key distinction between informal and formal proof generation lies in the availability and utilization of compilation (verification) feedback from proof assistants like Lean or Coq. Humans naturally leverage such feedback to iteratively revise their proofs. Recent works have shown that integrating the verifier’s error messages or tactic verification outcomes into proof generation significantly improves synthesis accuracy (First et al., 2023).\n\nOur framework formalizes this intuition by explicitly incorporating verifier feedback within the whole-proof generation loop. We structure the pipeline so that, after an initial proof attempt, verification failures are parsed and communicated back into the model as corrective guidance. The model then generates proof repairs, leading to an iterative self-correction process.\n\n### 2.2 CURATING FORMAL STATEMENTS\n\nIn this part, we detail our methods for curating a large, high-quality dataset of Lean 4 statements, which is essential for expert iteration and RL in formal theorem proving. We start with the formalizer training, which is the core of translating existing math problems written in natural language into Lean statements. We then present our scaffolded data synthesis pipeline that creates math problems at an appropriate difficulty level, which includes a lightweight formal-based method that utilizes the Lean system, and an informal-based system for large-scale data augmentation.\n\n**Formalizer Training.** Existing Lean datasets (e.g., Goedel-Pset-v1) contain many low-quality problems—human evaluation on a sampled subset shows that over 80% of unsolved problems are incorrectly formalized. This highlights the need for stronger formalizers. We train our formalizer using the standard expert iteration pipeline, which combines Lean syn-\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Name&lt;/th>\n&lt;th>Pass&lt;/th>\n&lt;th>Failed&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Kimina-autoformalizer&lt;/td>\n&lt;td>161&lt;/td>\n&lt;td>139&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Godel-Formalizer-V2&lt;/td>\n&lt;td>228&lt;/td>\n&lt;td>72&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nTable 1: Comparison of different formalizers on 300 Omni-math problems.Figure 2: Our **informal-based scaffolded data synthesis pipeline** with three parts: (1) informal statement generation; (2) formalization and quality checking; and (3) negation and difficulty filtering.\n\ntax checks and semantic evaluation via LLMs to assess translation quality. Only statements that pass both checks are included in the next iteration of SFT. Details of the LLM semantic evaluation prompt are provided in Appendix C.\n\nTo initialize expert iteration, we prompt Claude Sonnet 4 to generate 50K formalized statements, along with corresponding reasoning traces. Incorporating reasoning capability enables our formalizer to outperform previous models such as Goedel-Formalizer-V1 and Kimina-Autoformalizer, which lack this feature.\n\nWe evaluate our model Goedel-Formalizer-V2 and Kimina-Autoformalizer on a benchmark of 300 OmniMath problems. Results are shown in Table 1.\n\n**Formal-based scaffolded data synthesis.** When the prover fails to find a proof for a challenging problem, we can still leverage the proof attempt to generate simpler, related problems. The intuition is that even an incorrect proof attempt may introduce valid subgoals that represent easier subproblems. We utilize a powerful tactic in Lean, `extract_goal`, to capture the unsolved states of a proof. These extracted goals (together with the preconditions), which are well-formed mathematical statements, are then used to augment our training data for the next phase. Since an extracted statement is not guaranteed to be provable, we also include its negation, thereby training the model to recognize both true and false propositions.\n\n**Informal-based scaffolded data synthesis.** Another way of scaffolded data synthesis is to leverage the current LLMs’ mathematical reasoning ability in natural language, to create math statements at the right level for the model to learn. For a given problem, we prompt an LLM (Qwen3-32B) to generate simpler/sub-problems if it is unsolved, or harder variants if it is already solved. To improve generation quality, we first have the LLM attempt a natural language solution to the original problem, using its output as context. The generated informal statements are then formalized into Lean by the formalization pipeline we described in **Formalizer Training**. To avoid the inference overhead of incorrect or trivial statements, we use an LLM-based filter that assesses each statement for correctness and difficulty, where trivial or mathematically incorrect statements are discarded (the negation of incorrect statements are also added to the dataset). This filtering process significantly accelerates data synthesis, with a minor trade-off in potentially discarding some valid statements due to LLM judgment errors. The prompts and further details are in Appendix D.\n\n### 2.3 TRAINING ALGORITHMS\n\n**Supervised fine-tuning and expert iteration.** We follow the standard pipeline of Expert Iteration by iterating between using the model to conduct large-scale inference on the statement sets, collectingThe diagram illustrates the model training pipeline. It starts with a **Formal Statement** box. From this box, three paths emerge:\n \n\n- An orange arrow labeled **Distill** leads to a box labeled **Deepseek-Prover-V2-7B/671B**.\n- An orange arrow labeled **Scaffolded Data Synthesis** leads to **Dataset S&lt;sub>3&lt;/sub>**.\n- An orange arrow labeled **Self-Correct** leads to a box labeled **Deepseek-Prover-V2-671B**.\n\n From the **Deepseek-Prover-V2-7B/671B** box, an orange arrow labeled **Distill** leads to **Dataset S&lt;sub>1&lt;/sub>**. From the **Deepseek-Prover-V2-671B** box, an orange arrow labeled **Self-Correct** leads to **Corrected Proof**. A dashed arrow points from **Corrected Proof** to **Dataset S&lt;sub>2&lt;/sub>**.\n   \n The training stages are represented by blue boxes:\n \n\n- **SFT-S&lt;sub>1&lt;/sub>** receives an orange arrow from **Dataset S&lt;sub>1&lt;/sub>** and a blue arrow labeled **SFT** from **Dataset S&lt;sub>1&lt;/sub>**.\n- **SFT-S&lt;sub>2&lt;/sub>-AVG** receives an orange arrow from **Dataset S&lt;sub>2&lt;/sub>** and a blue arrow labeled **SFT+AVG** from **Dataset S&lt;sub>2&lt;/sub>**.\n- **SFT-S&lt;sub>3&lt;/sub>-AVG** receives an orange arrow from **Dataset S&lt;sub>3&lt;/sub>** and a blue arrow labeled **SFT+AVG** from **Dataset S&lt;sub>3&lt;/sub>**.\n- **RL+AVG** receives a blue arrow labeled **RL+AVG** from **SFT-S&lt;sub>2&lt;/sub>-AVG** and a blue arrow labeled **RL+AVG** from **SFT-S&lt;sub>3&lt;/sub>-AVG**.\n\n Dashed arrows also indicate a flow from **Dataset S&lt;sub>1&lt;/sub>** to **Dataset S&lt;sub>2&lt;/sub>** and from **Dataset S&lt;sub>2&lt;/sub>** to **Dataset S&lt;sub>3&lt;/sub>**.\n\nFigure 3: The overall workflow of model training. “+AVG” denotes that the trained model is averaged with the base model after training. “RL+AVG” is the final output model. Detailed descriptions are provided in Section 2.4.\n\ncorrect proofs with reasoning traces, and fine-tuning the model further by Supervised Fine-tuning (SFT) on the collected samples.\n\n**Reinforcement learning.** We aim to train a model capable of generating complete proofs and correcting its own errors via verifier-guided self-correction. To this end, we adopt an efficient hybrid strategy. We first sample multiple complete proofs in parallel. For each sampled proof, we perform serial self-correction, generating one correction per round. This serial correction process aligns well with RL, which optimizes expected reward and has been shown to improve single-shot (pass@1) accuracy (Shao et al., 2024; Yue et al., 2025).\n\nOur RL implementation adopts a multi-task setup (illustrated in Appendix Figure 9): 50% of the inputs are used for whole proof generation, and the remaining 50% for first-round self-correction. We train for a single epoch, using approximately 46K and 67K unique inputs for the 8B and 32B models, respectively. On the algorithmic side, we use a hybrid GRPO-based approach (Shao et al., 2024). Compared to vanilla GRPO, our method removes group normalization as suggested by Dr.GRPO (Liu et al., 2025) to avoid inherent bias on length, incorporates clip-higher, overlong penalties, and dynamic sampling from DAPO (Yu et al., 2025), and excludes the KL regularization term from the objective to encourage exploration. A key observation is that question difficulty significantly impacts RL training. To address this, we modify the dynamic sampling strategy to only include problems with pass rates in the range  $(0, 0.75]$  during optimization. For further implementation details, see Appendix E.1.\n\n**Model averaging for enhanced diversity.** We observed that in the later stages of SFT and RL, the model’s diversity decreases. This is reflected by an increase in pass@1 but a decline in pass@N for larger values of N, such as N=32. We adopt model averaging to enhance model diversity (Wortsman et al., 2022b;a; Lin et al., 2023a;b; Dang et al., 2025). Specifically, let the parameters of the base model be denoted as  $\\theta_0$ , and those of the fine-tuned model as  $\\theta$ . We use the combined model parameters defined as  $(1 - \\alpha)\\theta_0 + \\alpha\\theta$ , where  $\\alpha \\in (0, 1)$ . Existing literature has demonstrated that this simple approach can significantly improve the feature diversity of the final model. Our observations also confirm that this method effectively enhances pass@N. We perform model averaging at each stage of the process. Specifically, we apply model averaging after completing SFT and use the averaged model as the starting point for RL. Once RL is completed, we perform model averaging again and use this averaged model as the final model.\n\n## 2.4 WHOLE PIPELINE: PUTTING EVERYTHING TOGETHER\n\nThe pipeline consists of the following steps:\n\n- • We utilize Deepseek-Prover-V2-7B and Deepseek-Prover-V2-671B to perform large-scale inference, producing an initial supervised fine-tuning (SFT) dataset  $S_1$  for complete proof generation.- • We employ  $S_1$  to conduct SFT on both Qwen3-8B and Qwen3-32B, resulting in fine-tuned models SFT- $S_1$  for both the 8B and 32B variants&lt;sup>1&lt;/sup>.\n- • Using SFT- $S_1$  and Deepseek-Prover-V2-671B, we annotate self-correction data. The self-correction data from Deepseek-Prover-V2-671B is inferred using NeMo-Skills&lt;sup>2&lt;/sup> with 144 H100s. This data is then incorporated back into  $S_1$  to create an enhanced dataset  $S_2$ . We subsequently perform SFT on both model sizes using  $S_2$ , yielding improved models SFT- $S_2$ . We perform model averaging between SFT- $S_2$  and the base model for both the 8B and 32B models, resulting in SFT- $S_2$ -AVG.\n- • We perform scaffolded data synthesis with SFT- $S_2$ -AVG to generate the dataset  $S_3$ . Continuing the SFT process, we further improve the models by training SFT- $S_2$ -AVG on  $S_3$ , yielding SFT- $S_3$ , and subsequently obtain the averaged model SFT- $S_3$ -AVG.\n- • We apply reinforcement learning to the SFT- $S_3$ -AVG and conduct model averaging and obtain the final model RL-AVG.\n\nThe overall workflow is illustrated in Fig. 3.\n\n### 3 EVALUATION\n\nThis section presents our experiment results on Goedel-Prover-V2. We first discuss our evaluation benchmarks (Section 3.1). Then, we discuss our main evaluation results on the selected benchmarks (Section 3.3), and correspondingly the scaling behavior (Section 3.4). Finally, we investigate the performance of reinforcement learning and model averaging (Section 3.6).\n\n#### 3.1 BENCHMARKS\n\n**MiniF2F.** MiniF2F (Zheng et al., 2021) consists of 488 problem statements (244 validation and 244 test problems) in Lean. The problems are drawn from high-school level competitions including the AMC, AIME, and the International Mathematical Olympiad (IMO). We use the version of MiniF2F provided by Kimina (Wang et al., 2025)&lt;sup>3&lt;/sup>, which has some incorrect statements fixed.\n\n**PutnamBench.** PutnamBench (Tsoukalas et al., 2024) focuses on college-level mathematics competition problems that are sourced from the William Lowell Putnam Mathematical Competition years 1962 - 2023. PutnamBench comprises 644 problems, covering algebra, analysis, number theory, geometry, combinatorics, probability, and set theory.\n\n**MathOlympiadBench.** We constructed MathOlympiadBench, which comprises 360 human-verified formalizations of Olympiad-level mathematical problems, sourced from Compfiles&lt;sup>4&lt;/sup> and IMOSLLearn4 repository&lt;sup>5&lt;/sup>. It contains 158 IMO problems from 1959 to 2024, 131 IMO shortlist problems covering 2006 to 2023, 68 national mathematical Olympiad problems, and 3 additional mathematical puzzles. The statistic of problem categories in MathOlympiadBench is presented in Figure 4, and Figure 5 visualizes humans’ formalizing and solving status of IMO problems in MathOlympiadBench. See Appendix A for more details of MathOlympiadBench and its comparison with MiniF2F.\n\n#### 3.2 EVALUATED METHODS\n\nFollowing previous works (Xin et al., 2024b; Lin et al., 2025; Dong & Ma, 2025; Ren et al., 2025) the evaluations are done under Lean 4.9.0-rc1. For the first round of whole-proof generation, the max token length of the model is set to be 30,000. For the verifier-guided error-correction, we sequentially conduct 2 additional rounds of self-correction, given the verifier’s feedback on the previous attempt. The total number of tokens in the self-correction mode is set to be 40,000. We report the pass@N metric.\n\n&lt;sup>1&lt;/sup>We use &lt;https://github.com/hiyouga/LLaMA-Factory> for SFT.\n\n&lt;sup>2&lt;/sup>&lt;https://github.com/NVIDIA/NeMo-Skills>\n\n&lt;sup>3&lt;/sup>[https://huggingface.co/datasets/AI-MO/minif2f\\\\_test](https://huggingface.co/datasets/AI-MO/minif2f_test)\n\n&lt;sup>4&lt;/sup>&lt;https://dwrensha.github.io/compfiles/imo.html>\n\n&lt;sup>5&lt;/sup>&lt;https://github.com/mortarsanjaya/IMOSLLearn4>Figure 4: Distribution of problems in MathOlympiadBench by category.\n\nFigure 5: Community’s achievement on IMO problems by year and problem index. Each cell represents a problem:  $\\square$  statement not formalized,  $\\blacksquare$  not solved, and  $\\blacksquare$  solved.\n\n### 3.3 MAIN RESULTS\n\nTable 2: Performance of different whole-proof generation methods on MiniF2F test split.  $\\dagger$  denotes concurrent work\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Method&lt;/th>\n&lt;th>Budget&lt;/th>\n&lt;th>Performance&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Goedel-Prover-SFT (Lin et al., 2025)&lt;/td>\n&lt;td>32&lt;br/>3200&lt;/td>\n&lt;td>&lt;math>57.6\\% \\pm 0.7\\%&lt;/math>&lt;br/>62.7%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>STP (Dong &amp; Ma, 2025)&lt;/td>\n&lt;td>128&lt;br/>3200&lt;br/>25600&lt;/td>\n&lt;td>&lt;math>61.2\\% \\pm 0.6\\%&lt;/math>&lt;br/>&lt;math>65.0\\% \\pm 0.5\\%&lt;/math>&lt;br/>67.6%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Kimina-Prover-Preview-72B (Wang et al., 2025)&lt;/td>\n&lt;td>32&lt;br/>8192&lt;/td>\n&lt;td>68.85%&lt;br/>80.74%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepSeek-Prover-V2-7B (Ren et al., 2025)&lt;/td>\n&lt;td>32&lt;br/>8192&lt;/td>\n&lt;td>&lt;math>75.6\\% \\pm 0.5\\%&lt;/math>&lt;br/>82.0%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepSeek-Prover-V2-671B&lt;/td>\n&lt;td>32&lt;br/>8192&lt;/td>\n&lt;td>&lt;math>82.4\\% \\pm 0.6\\%&lt;/math>&lt;br/>88.9%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Kimina-Prover-8B&lt;math>^\\dagger&lt;/math> (Wang et al., 2025)&lt;/td>\n&lt;td>32&lt;/td>\n&lt;td>78.3%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Kimina-Prover-70B&lt;math>^\\dagger&lt;/math>&lt;/td>\n&lt;td>32&lt;br/>1024&lt;/td>\n&lt;td>84.0%&lt;br/>87.7%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>w/ TTRL&lt;/td>\n&lt;td>unknown&lt;/td>\n&lt;td>92.2%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Goedel-Prover-V2-8B&lt;/td>\n&lt;td>32&lt;br/>1024&lt;br/>8192&lt;/td>\n&lt;td>&lt;math>84.6\\% \\pm 0.6\\%&lt;/math>&lt;br/>87.9%&lt;br/>90.2%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>w/ self-correction&lt;/td>\n&lt;td>32&lt;br/>1024&lt;/td>\n&lt;td>&lt;math>86.7\\% \\pm 0.2\\%&lt;/math>&lt;br/>89.3%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Goedel-Prover-V2-32B&lt;/td>\n&lt;td>32&lt;br/>1024&lt;br/>8192&lt;/td>\n&lt;td>&lt;math>88.1\\% \\pm 0.8\\%&lt;/math>&lt;br/>91.8%&lt;br/>92.2%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>w/ self-correction&lt;/td>\n&lt;td>32&lt;br/>1024&lt;/td>\n&lt;td>&lt;math>90.4\\% \\pm 0.6\\%&lt;/math>&lt;br/>92.6%&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nThe evaluation results of Goedel-Prover-V2 on MiniF2F are summarized in Table 2, and results on PutnamBench are shown in Table 3. The results for MathOlympiadBench are presented in the rightmost figure of Figure 1. Below, we summarize and discuss the results.\n\n**High performance at modest scale.** Our 32B model achieves pass@32 accuracy of 88.1% on MiniF2F, with 90.4% after 2 rounds of error-correction, exceeding the previous state-of-the-art DeepSeek-Prover-V2-671B’s 82.4% while using far fewer parameters. Even the 8B variant achieves84.6%, nearly matching or outperforming Kimina-Prover-70B’s results under the same inference budget, and outperforming the previous SOTA DeepSeek-Prover-V2-671B on MiniF2F, with a significant smaller model size. On PutnamBench, our 32B model solves 43 problems under pass@32, nearly doubling the DeepSeek-Prover-V2-671B model’s performance under the same budget. With error-correction, Goedel-Prover-V2-32B solves 57 problems under pass@32, outperforming DeepSeek-Prover-V2-671B under pass@1024. Under pass@184 and error correction, Goedel-Prover-V2-32B solves 86 on PutnamBench, securing the best open-source theorem prover on the leaderboard.\n\nTable 3: Comparison of different models on PutnamBench. Our Goedel-Prover-V2 with compiler-guided self-correction solves 86 problems from PutnamBench, improving the previous SOTA (DeepSeek-Prover-V2) by 39 more problems, and securing the best open-source model on the leaderboard.\\*\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>#&lt;/th>\n&lt;th>Model&lt;/th>\n&lt;th>num-solved&lt;/th>\n&lt;th>open-source&lt;/th>\n&lt;th>compute&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>1&lt;/td>\n&lt;td>&lt;b>Godel-Prover-V2 (self-correction mode)&lt;/b>&lt;/td>\n&lt;td>86&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>pass@184&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>1&lt;/td>\n&lt;td>&lt;b>Godel-Prover-V2 (self-correction mode)&lt;/b>&lt;/td>\n&lt;td>57&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>pass@32&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>1&lt;/td>\n&lt;td>&lt;b>Godel-Prover-V2&lt;/b>&lt;/td>\n&lt;td>43&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>pass@32&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>2&lt;/td>\n&lt;td>DeepSeek-Prover-V2&lt;/td>\n&lt;td>47&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>pass@1024&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>2&lt;/td>\n&lt;td>DeepSeek-Prover-V2&lt;/td>\n&lt;td>22&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>pass@32&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>3&lt;/td>\n&lt;td>DSP+&lt;/td>\n&lt;td>23&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>pass@128&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>4&lt;/td>\n&lt;td>Bourbaki&lt;/td>\n&lt;td>14&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>pass@512&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>5&lt;/td>\n&lt;td>Kimina-Prover-7B-Distill&lt;/td>\n&lt;td>10&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>pass@192&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>6&lt;/td>\n&lt;td>Self-play Theorem Prover&lt;/td>\n&lt;td>8&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>pass@3200&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>7&lt;/td>\n&lt;td>Godel-Prover-SFT&lt;/td>\n&lt;td>7&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>pass@512&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>8&lt;/td>\n&lt;td>ABEL&lt;/td>\n&lt;td>7&lt;/td>\n&lt;td>×&lt;/td>\n&lt;td>pass@596&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n\\* A concurrent work, Seed Prover (Chen et al., 2025), successfully solved 331 problems on PutnamBench. However, the prover is not open-source, and it is not clear what the computational budget is at test time (which is expected to be much larger than ours).\n\n**Efficacy of verifier-guided self-correction.** Adding self-correction provides a consistent gain of approximately 2 percentage points in pass@32 for both models on MiniF2F. On PutnamBench, error correction leads to 14 more solves under pass@32. This demonstrates that integrating Lean compiler feedback into a long-chain-of-thought revision pipeline enables the model to identify errors and repair them effectively.\n\n**Sample-efficient inference.** Unlike prior models such as Kimina-Prover and DeepSeek-Prover-V2, which rely heavily on large sampling budgets or test-time reinforcement learning to reach peak accuracy, Goedel-Prover-V2 attains very high pass@N with minimal inference overhead (N=32 or 64), indicating that the model internalizes powerful reasoning strategies during training. The sample efficiency, together with the relatively small size, makes Goedel-Prover-V2 series a very good candidate for the community to develop new algorithms and test on different benchmarks.\n\n### 3.4 SCALING ANALYSIS\n\nFigure 6 and Table 4 illustrate the scaling behavior of Goedel-Prover-V2 (8B and 32B variants) across different inference budgets, compared against DeepSeek-Prover-V2 (7B and 671B) and Kimina-Prover-72B. At the lower sampling regime (pass@32), Goedel-Prover-V2-32B already achieves 88.1%, notably surpassing DeepSeek-Prover-V2-671B (82.4%) and Kimina-Prover-72B (84.0%). This advantage persists across inference budgets, with our self-correction mode providing approximately a 2-point performance improvement under pass@32 and pass@64, peaking at 92.6% at pass@8192. The smaller 8B model also demonstrates strong scalability, surpassing the 671B DeepSeek model at all budgets.\n\nFigure 6: Scaling behavior on MiniF2F test split.&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Model&lt;/th>\n&lt;th>32&lt;/th>\n&lt;th>64&lt;/th>\n&lt;th>128&lt;/th>\n&lt;th>256&lt;/th>\n&lt;th>512&lt;/th>\n&lt;th>1024&lt;/th>\n&lt;th>2048&lt;/th>\n&lt;th>4096&lt;/th>\n&lt;th>8192&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>32B (self-correction mode)&lt;/td>\n&lt;td>90.4&lt;/td>\n&lt;td>91.4&lt;/td>\n&lt;td>91.9&lt;/td>\n&lt;td>92.3&lt;/td>\n&lt;td>92.4&lt;/td>\n&lt;td>92.6&lt;/td>\n&lt;td>—&lt;/td>\n&lt;td>—&lt;/td>\n&lt;td>—&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>32B&lt;/td>\n&lt;td>88.1&lt;/td>\n&lt;td>89.8&lt;/td>\n&lt;td>90.5&lt;/td>\n&lt;td>91.0&lt;/td>\n&lt;td>91.6&lt;/td>\n&lt;td>91.8&lt;/td>\n&lt;td>92.0&lt;/td>\n&lt;td>92.2&lt;/td>\n&lt;td>92.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>8B (self-correction mode)&lt;/td>\n&lt;td>86.7&lt;/td>\n&lt;td>86.9&lt;/td>\n&lt;td>87.4&lt;/td>\n&lt;td>88.0&lt;/td>\n&lt;td>88.5&lt;/td>\n&lt;td>89.3&lt;/td>\n&lt;td>—&lt;/td>\n&lt;td>—&lt;/td>\n&lt;td>—&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>8B&lt;/td>\n&lt;td>84.6&lt;/td>\n&lt;td>86.1&lt;/td>\n&lt;td>86.5&lt;/td>\n&lt;td>87.0&lt;/td>\n&lt;td>87.4&lt;/td>\n&lt;td>87.9&lt;/td>\n&lt;td>88.5&lt;/td>\n&lt;td>89.3&lt;/td>\n&lt;td>90.2&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nTable 4: The performance (%) of Goedel-Prover-V2 on MiniF2F across different compute budget.\n\nThese results indicate that Goedel-Prover-V2 efficiently internalizes reasoning during training, requiring fewer inference samples to achieve comparable or superior accuracy. Furthermore, the consistent gains from verifier-guided self-correction across all inference budgets further underscore the value of combining error correction with long-chain-of-thought reasoning in formal theorem proving.\n\n### 3.5 ANALYSIS OF SELF-CORRECTION\n\nIn our main experiments, self-correction was conducted for a maximum of 2 rounds with a 40k token context length. To further explore its capabilities, we used YaRN (Peng et al., 2024) to extend the context length to 128k tokens and allowed up to 5 revision iterations. We conducted a series of experiments on the MiniF2F benchmark at pass@32, the results of which are presented in Figure 7. Alongside our standard prompting setup (Self Correction), we performed two ablation studies: (1) removing the specific compiler error messages (w/o Error Messages), and (2) removing the chain-of-thought from previous attempts, retaining only the formal proof (w/o Previous CoTs).\n\nFigure 7: Ablation study on self-correction with extended context length and revision iterations on the MiniF2F test split at pass@32.\n\nThe results show that removing compiler feedback significantly lowers performance, confirming that specific error messages are crucial for effective revision. Similarly, removing the reasoning from previous attempts also slightly degrades performance, indicating that retaining the chain-of-thought from prior rounds is beneficial. Furthermore, with an extended context and more revision iterations, the full self-correction model’s pass@32 accuracy on MiniF2F reaches an average of 92.7%, which surpasses the 92.2% performance of the model without self-correction at pass@8192, highlighting the sample efficiency of our iterative revision process.\n\n### 3.6 RL AND MODEL AVERAGING\n\nWe systematically evaluate the impact of RL steps and model averaging strategies on the performance of Goedel-Prover-V2. Specifically, for RL checkpoints at steps 60, 80, and 90, we apply model averaging with coefficients  $\\alpha = 0.6, 0.7, 0.8, 0.9$  (where  $\\alpha$  is the weight of the base model). We assess each averaged model in both vanilla (whole-proof generation) and correction (with self-correction) settings, evaluating both pass@1 and pass@N, as visualized in Figure 8.\n\nFor both vanilla and correction settings, pass@1 consistently increases as the number of RL steps grows. For vanilla pass@N, performance stabilizes at higher RL steps, whereas in the correction setting, pass@N continues to improve. This indicates that correction benefits more from RL, likely due to the shortage of high-quality self-correction data in the SFT stages.\n\nExamining different values of  $\\alpha$ , we observe that a higher proportion of the base model (i.e., lower  $\\alpha$ ) leads to lower pass@1, but pass@N first rises and then falls as  $\\alpha$  increases. There exists an optimal model averaging ratio that maximizes pass@N. This trend holds for both vanilla and correction settings, with the improvement being more pronounced for correction. This suggests that model averaging not only improves sample diversity but also amplifies the benefits of RL-driven self-correction.Figure 8: The effects of varying RL steps and model averaging ratios on the pass@1 and pass@32 performance of models, both with and without correction.\n\n## 4 RELATED WORKS\n\n**Formal Theorem Proving as Whole Proof Generation.** Inspired by the success of end-to-end reasoning in informal LLMs, recent foundational work in formal theorem proving has adopted a similar strategy: generating entire Lean proofs in a single pass. While informal reasoning models often struggle with step verification—producing fluent yet logically flawed arguments (Petrov et al., 2025)—formal settings like Lean (De Moura et al., 2015) offer a precise and executable verifier that enforces correctness. Leveraging this, models such as DeepSeek-Prover (Xin et al., 2024a), Goedel Prover (Lin et al., 2025), and Kimina Prover (Wang et al., 2025) demonstrate that end-to-end generation can produce formally verified proofs that are immediately checkable by the Lean proof assistant. This paradigm retains the global coherence and simplicity of sequence generation while grounding outputs in verifiable formal logic.\n\n**Formal Theorem Proving using Proof Search.** In contrast to end-to-end generation, proof search-based methods guide the model to incrementally construct proofs by exploring derivation paths with verifier feedback at each step. Recent systems such as InternLM2.5-StepProver (Wu et al., 2024), Hunyuan Prover (Li et al., 2024), DeepSeek-Prover v1.5 (Xin et al., 2024b), and BFS Prover (Xin et al., 2025) employ tree search algorithms—such as Monte Carlo Tree Search or breadth-first search—to explore multiple proof trajectories and iteratively assemble valid proofs. While this strategy improves correctness, it comes at the cost of significantly higher computational overhead, as the model must evaluate and verify a large number of partial branches. Recently, hybrid methods, which use a general-purpose (strong) LLM to write the proof sketch and query theorem provers to fill in the proof for small steps, also emerged (DSP+ (Cao et al., 2025) and the concurrent work Delta-Prover (Zhou et al., 2025)). However, these works usually require the LLM to be very large and powerful, where DSP+ uses 671B DeepSeek-R1 (Guo et al., 2025) or DeepSeek-V3 (Liu et al., 2024), and Delta-Prover uses Gemini (Comanici et al., 2025). Notably, Seed-Prover (Chen et al., 2025) employs a wide range of techniques, including extensive test-time search and refinement, and achieves IMO medal-level performance. However, it requires substantial computational resources.\n\n**Self-Repair and Verifier-Guided Refinement.** While tree-based proof search improves correctness, its high computational cost has motivated the development of more efficient mechanisms for guiding search and enabling self-refinement. One direction explores how auxiliary signals or intermediate structures can streamline the reasoning process. Jiang et al. (2023); Gloeckle et al. (2024); Cao et al. (2025) bridge informal and formal reasoning by using informal sketches as a skeleton for formal proof generation, while Yang et al. (2024) employs retrieval-augmented generation (RAG) to retrieve relevant theorems from formal libraries during proof construction. Other approaches, such as Ji et al. (2025), implement self-verification and iterative refinement loops, allowing models to autonomously revise candidate proofs using verifier feedback.\n\nVerifier-in-the-loop strategies in recent works (Baba et al., 2025; Zhou et al., 2025; Ren et al., 2025; Wang et al., 2025; Chen et al., 2025), also highlight the benefits of interactive feedback, improving success rates through iterative correction rather than brute-force search. These methods collectivelypoint to a more flexible and scalable paradigm: enabling the model to diagnose and repair its own outputs with minimal external supervision.\n\nGoedel-Prover-V2 builds on this trajectory by adopting a self-revision framework, where the model iteratively proposes and refines candidate proofs until they satisfy the Lean checker. This architecture draws inspiration from general-purpose self-repair frameworks in coding and reasoning (Yao et al., 2023; Shinn et al., 2023; First et al., 2023; Olausson et al., 2024; Chen et al., 2024; Bouzenia et al., 2024), bringing their iterative refinement loop into the domain of formal mathematics with long chain-of-thought reasoning.\n\n## 5 CONCLUSION AND DISCUSSION\n\nIn this work, we introduced **Goedel-Prover-V2**, a series of state-of-the-art open-source theorem provers that significantly advance automated formal proof generation. Our key innovation is the integration of long-chain-of-thought reasoning with compiler-guided self-correction, addressing a crucial gap overlooked by prior methods. Through scaffolded data synthesis, SFT and RL training, and model averaging, our models achieve state-of-the-art performance among open-source provers. In particular, our 32B model achieves 88.1% on MiniF2F at pass@32 and benefits further from self-correction and reaching 90.4% on MiniF2F at pass@32, outperforming larger models with lower inference cost. Moreover, our 8B model also outperforms the previous SOTA DeepSeek-Prover-V2-671B under pass@32 on MiniF2F with a significant smaller model size.\n\nWe also investigate a proof repair strategy as a test-time alternative to standard pass@k sampling. Instead of regenerating an entire failed proof, our method corrects only the faulty segment. We use Lean 4’s compiler feedback and the `extract_goal` tactic to isolate the unsolved subgoal, prompt the prover to solve it independently, and then reinsert the correct solution into the original proof. On the MiniF2F benchmark, this approach improves the amortized budget scaling curve by 1–2 percentage points, highlighting inference-time scaling strategies as a key direction for future work.\n\nBy open-sourcing all trained models, we aim to catalyze further advancements in formal reasoning research. We envision that the release of Goedel-Prover-V2 will not only establish a new benchmark for automated theorem proving but also provide a practical, efficient platform upon which future innovations can be built.\n\n## ACKNOWLEDGEMENT\n\nThis project was the result of a close collaborative effort by all authors, and every major component benefited from joint discussion and iteration. The author would like to thank Igor Gitman for support with the curation of self-correction data.\n\nHZ and SA acknowledge the support from Schmidt, Darpa, ONR, and NSF. CJ acknowledges the support from NSF-OAC-2411299, NSF-IIS-2239297, and Princeton AI Lab Seed Fund.\n\n## REFERENCES\n\nKaito Baba, Chaoran Liu, Shuhei Kurita, and Akiyoshi Sannai. Prover agent: An agent-based framework for formal mathematical proofs. *arXiv preprint arXiv:2506.19923*, 2025.\n\nIslem Bouzenia, Premkumar Devanbu, and Michael Pradel. Repairagent: An autonomous, llm-based agent for program repair. *arXiv preprint arXiv:2403.17134*, 2024.\n\nChenrui Cao, Liangcheng Song, Zenan Li, Xinyi Le, Xian Zhang, Hui Xue, and Fan Yang. Reviving dsp for advanced theorem proving in the era of reasoning models. *arXiv preprint arXiv:2506.11487*, 2025.\n\nLuoxin Chen, Jinming Gu, Liankai Huang, Wenhao Huang, Zhicheng Jiang, Allan Jie, Xiaoran Jin, Xing Jin, Chenggang Li, Kaijing Ma, Cheng Ren, Jiawei Shen, Wenlei Shi, Tong Sun, He Sun, Jiahui Wang, Siran Wang, Zhihong Wang, Chenrui Wei, Shufa Wei, Yonghui Wu, Yuchen Wu, Yihang Xia, Huajian Xin, Fan Yang, Huaiyuan Ying, Hongyi Yuan, Zheng Yuan, Tianyang Zhan, Chi Zhang, Yue Zhang, Ge Zhang, Tianyun Zhao, Jianqiu Zhao, Yichi Zhou, and Thomas HanwenZhu. Seed-prover: Deep and broad reasoning for automated theorem proving, 2025. URL &lt;https://arxiv.org/abs/2507.23726>.\n\nXinyun Chen, Maxwell Lin, Nathanael Schärli, and Denny Zhou. Teaching large language models to self-debug. In *The Twelfth International Conference on Learning Representations*, 2024.\n\nYuri Chervonyi, Trieu H Trinh, Miroslav Olšák, Xiaomeng Yang, Hoang Nguyen, Marcelo Menegali, Junehyuk Jung, Vikas Verma, Quoc V Le, and Thang Luong. Gold-medalist performance in solving olympiad geometry with AlphaGeometry2. *arXiv preprint arXiv:2502.03544*, 2025.\n\nGheorghe Comanici, Eric Bieber, Mike Schaeckermann, Ice Pasupat, Noveen Sachdeva, Inderjit Dhillon, Marcel Blstein, Ori Ram, Dan Zhang, Evan Rosen, et al. Gemini 2.5: Pushing the frontier with advanced reasoning, multimodality, long context, and next generation agentic capabilities. *arXiv preprint arXiv:2507.06261*, 2025.\n\nXingyu Dang, Christina Baek, J Zico Kolter, and Aditi Raghunathan. Assessing diversity collapse in reasoning. In *Scaling Self-Improving Foundation Models without Human Supervision*, 2025.\n\nLeonardo De Moura, Soonho Kong, Jeremy Avigad, Floris Van Doorn, and Jakob von Raumer. The lean theorem prover (system description). In *Automated Deduction-CADE-25: 25th International Conference on Automated Deduction, Berlin, Germany, August 1-7, 2015, Proceedings 25*, pp. 378–388. Springer, 2015.\n\nKefan Dong and Tengyu Ma. STP: Self-play LLM theorem provers with iterative conjecturing and proving. In *International Conference on Machine Learning (ICML)*, 2025.\n\nEmily First, Markus N Rabe, Talia Ringer, and Yuriy Brun. Baldur: Whole-proof generation and repair with large language models. In *ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering (ESEC/FSE)*, 2023.\n\nFabian Gloeckle, Jannis Limperg, Gabriel Synnaeve, and Amaury Hayat. Abel: Sample efficient online reinforcement learning for neural theorem proving. In *The 4th Workshop on Mathematical Reasoning and AI at NeurIPS'24*, 2024.\n\nGoogle DeepMind. AI achieves silver-medal standard solving international mathematical olympiad problems. &lt;https://deepmind.google/discover/blog/ai-solves-imo-problems-at-silver-medal-level/>, 2024.\n\nDaya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. *arXiv preprint arXiv:2501.12948*, 2025.\n\nAaron Jaech, Adam Kalai, Adam Lerer, Adam Richardson, Ahmed El-Kishky, Aiden Low, Alec Helyar, Aleksander Madry, Alex Beutel, Alex Carney, et al. Openai o1 system card. *arXiv preprint arXiv:2412.16720*, 2024.\n\nXingguang Ji, Yahui Liu, Qi Wang, Jingyuan Zhang, Yang Yue, Rui Shi, Chenxi Sun, Fuzheng Zhang, Guorui Zhou, and Kun Gai. Leanabell-prover-v2: Verifier-integrated reasoning for formal theorem proving via reinforcement learning. *arXiv preprint arXiv:2507.08649*, 2025.\n\nAlbert Qiaochu Jiang, Sean Welleck, Jin Peng Zhou, Timothee Lacroix, Jiacheng Liu, Wenda Li, Mateja Jamnik, Guillaume Lample, and Yuhuai Wu. Draft, sketch, and prove: Guiding formal theorem provers with informal proofs. In *The Eleventh International Conference on Learning Representations*, 2023.\n\nYang Li, Dong Du, Linfeng Song, Chen Li, Weikang Wang, Tao Yang, and Haitao Mi. Hunyuanprover: A scalable data synthesis framework and guided tree search for automated theorem proving. *arXiv preprint arXiv:2412.20735*, 2024.\n\nYong Lin, Hangyu Lin, Wei Xiong, Shizhe Diao, Jianmeng Liu, Jipeng Zhang, Rui Pan, Haoxiang Wang, Wenbin Hu, Hanning Zhang, et al. Mitigating the alignment tax of rlhf. *arXiv preprint arXiv:2309.06256*, 2023a.Yong Lin, Lu Tan, Yifan Hao, Honam Wong, Hanze Dong, Weizhong Zhang, Yujiu Yang, and Tong Zhang. Spurious feature diversification improves out-of-distribution generalization. *arXiv preprint arXiv:2309.17230*, 2023b.\n\nYong Lin, Shange Tang, Bohan Lyu, Jiayun Wu, Hongzhou Lin, Kaiyu Yang, Jia Li, Mengzhou Xia, Danqi Chen, Sanjeev Arora, et al. Goedel-Prover: A frontier model for open-source automated theorem proving. *arXiv preprint arXiv:2502.07640*, 2025.\n\nAixin Liu, Bei Feng, Bing Xue, Bingxuan Wang, Bochao Wu, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chenyu Zhang, Chong Ruan, et al. Deepseek-v3 technical report. *arXiv preprint arXiv:2412.19437*, 2024.",
      "numLines": 500,
      "startLine": 0,
      "totalLines": 1092
    }
  },
  "sourceToolAssistantUUID": "64eae359-35cf-482c-bdab-96d75791e811",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-27 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "552a41fa-41b2-4084-b8dc-a171b7ff7d8d",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze Goedel-Prover-V2 paper innovation",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc"
}
```

---

### Assistant

_source line 49 · 2026-05-27T15:58:46.688Z_

<details><summary>Logged reasoning block</summary>

```text
Let me continue reading the rest of the file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "552a41fa-41b2-4084-b8dc-a171b7ff7d8d",
  "isSidechain": false,
  "requestId": "req_011CbTMG2fYXw1GyLjY39mKY",
  "type": "assistant",
  "uuid": "c33d934c-0e3e-4d36-a8bc-d441d0465270",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LWrhPaBEsvBW3F9GA3Qe5o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15601,
      "cache_read_input_tokens": 21025,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15601,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 202,
          "cache_read_input_tokens": 21025,
          "cache_creation_input_tokens": 15601,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15601
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

_source line 50 · 2026-05-27T15:58:47.181Z_

Let me read the rest of the file to get the remaining content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c33d934c-0e3e-4d36-a8bc-d441d0465270",
  "isSidechain": false,
  "requestId": "req_011CbTMG2fYXw1GyLjY39mKY",
  "type": "assistant",
  "uuid": "9db08b83-9208-41d9-9800-0d95cc8e2678",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LWrhPaBEsvBW3F9GA3Qe5o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15601,
      "cache_read_input_tokens": 21025,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15601,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 202,
          "cache_read_input_tokens": 21025,
          "cache_creation_input_tokens": 15601,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15601
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

_source line 51 · 2026-05-27T15:58:50.249Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CvaDixksuQDZARPYAMjHRL`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/6db262d6-dcf8-4dbf-b94b-349936024bbc/tool-results/toolu_01Tq8krFT3t8xgN1SnQrexGw.txt",
  "offset": 500,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9db08b83-9208-41d9-9800-0d95cc8e2678",
  "isSidechain": false,
  "requestId": "req_011CbTMG2fYXw1GyLjY39mKY",
  "type": "assistant",
  "uuid": "57449196-73e3-4228-9f9c-ad6b8d84aa1b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LWrhPaBEsvBW3F9GA3Qe5o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15601,
      "cache_read_input_tokens": 21025,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15601,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 202,
          "cache_read_input_tokens": 21025,
          "cache_creation_input_tokens": 15601,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15601
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

_source line 52 · 2026-05-27T15:58:50.255Z_

<details><summary>↩ Tool result · `toolu_01CvaDixksuQDZARPYAMjHRL`</summary>

```````text
500	Aixin Liu, Bei Feng, Bing Xue, Bingxuan Wang, Bochao Wu, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chenyu Zhang, Chong Ruan, et al. Deepseek-v3 technical report. *arXiv preprint arXiv:2412.19437*, 2024.
501	
502	Zichen Liu, Changyu Chen, Wenjun Li, Penghui Qi, Tianyu Pang, Chao Du, Wee Sun Lee, and Min Lin. Understanding r1-zero-like training: A critical perspective. *arXiv preprint arXiv:2503.20783*, 2025.
503	
504	Leonardo de Moura and Sebastian Ullrich. The Lean 4 theorem prover and programming language. In *International Conference on Automated Deduction (CADE)*, 2021.
505	
506	Theo X. Olausson, Jeevana Priya Inala, Chenglong Wang, Jianfeng Gao, and Armando Solar-Lezama. Is self-repair a silver bullet for code generation? In *The Twelfth International Conference on Learning Representations*, 2024.
507	
508	Bowen Peng, Jeffrey Quesnelle, Honglu Fan, and Enrico Shippole. YaRN: Efficient context window extension of large language models. In *The Twelfth International Conference on Learning Representations*, 2024. URL &lt;https://openreview.net/forum?id=wHBfxhZulu>.
509	
510	Ivo Petrov, Jasper Dekoninck, Lyuben Baltadzhiev, Maria Drencheva, Kristian Minchev, Mislav Balunović, Nikola Jovanović, and Martin Vechev. Proof or bluff? evaluating llms on 2025 usa math olympiad. *arXiv preprint arXiv:2503.21934*, 2025.
511	
512	ZZ Ren, Zhihong Shao, Junxiao Song, Huajian Xin, Haocheng Wang, Wanjia Zhao, Liyue Zhang, Zhe Fu, Qihao Zhu, Dejian Yang, et al. Deepseek-prover-v2: Advancing formal mathematical reasoning via reinforcement learning for subgoal decomposition. *arXiv preprint arXiv:2504.21801*, 2025.
513	
514	Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li, Y Wu, et al. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. *arXiv preprint arXiv:2402.03300*, 2024.
515	
516	Guangming Sheng, Chi Zhang, Zilingfeng Ye, Xibin Wu, Wang Zhang, Ru Zhang, Yanghua Peng, Haibin Lin, and Chuan Wu. Hybridflow: A flexible and efficient rlhf framework. *arXiv preprint arXiv: 2409.19256*, 2024.
517	
518	Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik R Narasimhan, and Shunyu Yao. Reflexion: language agents with verbal reinforcement learning. In *Thirty-seventh Conference on Neural Information Processing Systems*, 2023.
519	
520	Trieu H Trinh, Yuhuai Wu, Quoc V Le, He He, and Thang Luong. Solving olympiad geometry without human demonstrations. *Nature*, 625(7995):476–482, 2024.
521	
522	George Tsoukalas, Jasper Lee, John Jennings, Jimmy Xin, Michelle Ding, Michael Jennings, Amitayush Thakur, and Swarat Chaudhuri. Putnambench: Evaluating neural theorem-provers on the putnam mathematical competition. *arXiv preprint arXiv:2407.11214*, 2024.
523	
524	Haiming Wang, Mert Unsal, Xiaohan Lin, Mantas Baksys, Junqi Liu, Marco Dos Santos, Flood Sung, Marina Vinyes, Zhenzhe Ying, Zekai Zhu, et al. Kimina-prover preview: Towards large formal reasoning models with reinforcement learning. *arXiv preprint arXiv:2504.11354*, 2025.
525	
526	Mitchell Wortsman, Gabriel Ilharco, Samir Ya Gadre, Rebecca Roelofs, Raphael Gontijo-Lopes, Ari S Morcos, Hongseok Namkoong, Ali Farhadi, Yair Carmon, Simon Kornblith, et al. Model soups: averaging weights of multiple fine-tuned models improves accuracy without increasing inference time. In *International conference on machine learning*, pp. 23965–23998. PMLR, 2022a.Mitchell Wortsman, Gabriel Ilharco, Jong Wook Kim, Mike Li, Simon Kornblith, Rebecca Roelofs, Raphael Gontijo Lopes, Hannaneh Hajishirzi, Ali Farhadi, Hongseok Namkoong, et al. Robust fine-tuning of zero-shot models. In *Proceedings of the IEEE/CVF conference on computer vision and pattern recognition*, pp. 7959–7971, 2022b.
527	
528	Zijian Wu, Suozhi Huang, Zhejian Zhou, Huaiyuan Ying, Jiayu Wang, Dahua Lin, and Kai Chen. InternLM2.5-StepProver: Advancing automated theorem proving via expert iteration on large-scale lean problems. *arXiv preprint arXiv:2410.15700*, 2024.
529	
530	Huajian Xin, Daya Guo, Zhihong Shao, Zhizhou Ren, Qihao Zhu, Bo Liu, Chong Ruan, Wenda Li, and Xiaodan Liang. Deepseek-prover: Advancing theorem proving in llms through large-scale synthetic data. *arXiv preprint arXiv:2405.14333*, 2024a.
531	
532	Huajian Xin, ZZ Ren, Junxiao Song, Zhihong Shao, Wanjia Zhao, Haocheng Wang, Bo Liu, Liyue Zhang, Xuan Lu, Qiushi Du, et al. Deepseek-prover-v1.5: Harnessing proof assistant feedback for reinforcement learning and monte-carlo tree search. *arXiv preprint arXiv:2408.08152*, 2024b.
533	
534	Ran Xin, Chenguang Xi, Jie Yang, Feng Chen, Hang Wu, Xia Xiao, Yifan Sun, Shen Zheng, and Ming Ding. BFS-prover: Scalable best-first tree search for LLM-based automatic theorem proving. In *Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics*, 2025.
535	
536	Kaiyu Yang, Aidan Swope, Alex Gu, Rahul Chalamala, Peiyang Song, Shixing Yu, Saad Godil, Ryan J Prenger, and Animashree Anandkumar. Leandojo: Theorem proving with retrieval-augmented language models. *Advances in Neural Information Processing Systems*, 36, 2024.
537	
538	Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, and Karthik R Narasimhan. Tree of thoughts: Deliberate problem solving with large language models. In *Thirty-seventh Conference on Neural Information Processing Systems*, 2023.
539	
540	Qiyong Yu, Zheng Zhang, Ruofei Zhu, Yufeng Yuan, Xiaochen Zuo, Yu Yue, Weinan Dai, Tiantian Fan, Gaohong Liu, Lingjun Liu, et al. Dapo: An open-source llm reinforcement learning system at scale. *arXiv preprint arXiv:2503.14476*, 2025.
541	
542	Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Shiji Song, and Gao Huang. Does reinforcement learning really incentivize reasoning capacity in llms beyond the base model? *arXiv preprint arXiv:2504.13837*, 2025.
543	
544	Kunhao Zheng, Jesse Michael Han, and Stanislas Polu. Minif2f: a cross-system benchmark for formal olympiad-level mathematics. *arXiv preprint arXiv:2109.00110*, 2021.
545	
546	Yichi Zhou, Jianqiu Zhao, Yongxin Zhang, Bohan Wang, Siran Wang, Luoxin Chen, Jiahui Wang, Haowei Chen, Allan Jie, Xinbo Zhang, et al. Solving formal math problems by decomposition and iterative reflection. *arXiv preprint arXiv:2507.15225*, 2025.APPENDIXA DETAILS OF MATHOLYMPIADBENCH
547	
548	MathOlympiadBench is human-processed to eliminate several issues presented in the source problems: 1. incomplete problem statements, 2. distribution across multiple files, 3. multiple theorems per problem, and 4. incompatibility with the commonly used Mathlib. The verification process ensures that each problem contains exactly one formal theorem with its corresponding informal statement, and confirms that all formal statements can pass the compilation with the `sorry` tactic.
549	
550	We compared the IMO problems shared between MathOlympiadBench and MiniF2F, and identified at least 3 cases in MiniF2F exhibiting issues such as: 1. the formal statement to be proved is strictly weaker than the informal statement, and 2. the formal statement does not match the informal statement. Notably, similar issues are not observed for these problems in MathOlympiadBench.
551	
552	In the following, we present three case studies comparing the problem formalizations in MiniF2F and MathOlympiadBench.
553	
554	A.1 IMO 1981, PROBLEM 6: SPECIFIC VALUE VS. GENERAL FORMULA
555	
556	&lt;table border="1">
557	&lt;thead>
558	&lt;tr>
559	&lt;th>MiniF2F&lt;/th>
560	&lt;th>MathOlympiadBench&lt;/th>
561	&lt;/tr>
562	&lt;/thead>
563	&lt;tbody>
564	&lt;tr>
565	&lt;td>
566	&lt;pre>1 /--
567	2 The function &lt;math>f(x,y)&lt;/math> satisfies
568	3
569	4 (1) &lt;math>f(0,y) = y + 1&lt;/math>,
570	5
571	6 (2) &lt;math>f(x+1,0) = f(x,1)&lt;/math>,
572	7
573	8 (3) &lt;math>f(x+1,y+1) = f(x,f(x+1,y))&lt;/math>,
574	9
575	10 for all non-negative integers &lt;math>x,y&lt;/math>
576	11 . Determine &lt;math>f(4,1981)&lt;/math>.
577	12 -/
578	13 theorem imo_1981_p6 (f : &lt;math>\mathbb{N} \rightarrow \mathbb{N} \rightarrow&lt;/math>
579	14 &lt;math>\mathbb{N}&lt;/math>)
580	15 (h0 : &lt;math>\forall y, f\ 0\ y = y + 1&lt;/math>)
581	16 (h1 : &lt;math>\forall x, f\ (x + 1)\ 0 = f\ x\ 1&lt;/math>)
582	17 (h2 : &lt;math>\forall x\ y, f\ (x + 1)\ (y + 1) =&lt;/math>
583	18 &lt;math>f\ x\ (f\ (x + 1)\ y)) :
584	19 &lt;math>\forall y, f\ 4\ (y + 1) = 2 \wedge (f\ 4\ y +&lt;/math>
585	20 &lt;math>3) - 3 := by&lt;/math>&lt;/math>&lt;/pre>
586	&lt;/td>
587	&lt;td>
588	&lt;pre>1 /-!
589	2 # International Mathematical
590	3   Olympiad 1981, Problem 6
591	4
592	5 Suppose that &lt;math>f : \mathbb{N} \times \mathbb{N} \rightarrow \mathbb{N}&lt;/math>
593	6 satisfies
594	7
595	8 1) &lt;math>f\ (0, y) = y + 1&lt;/math>
596	9 2) &lt;math>f\ (x + 1, 0) = f\ (x, 1)&lt;/math>,
597	10 3) &lt;math>f\ (x + 1, y + 1) = f\ (x, f\ (x&lt;/math>
598	11 &lt;math>+ 1, y))&lt;/math>
599	12
600	13 for all &lt;math>x\ y \in \mathbb{N}&lt;/math>.
601	14
602	15 Determine &lt;math>f\ (4, 1981)&lt;/math>.
603	16 -/
604	17
605	18 def no_eval (x : &lt;math>\mathbb{N}&lt;/math>) : &lt;math>\mathbb{N} := x&lt;/math>
606	19 abbrev solution_value : &lt;math>\mathbb{N} :=&lt;/math>
607	20 no_eval ((2^·)^[1984] 1 - 3)
608	21
609	22 theorem imo1981_p6 (f : &lt;math>\mathbb{N} \rightarrow \mathbb{N} \rightarrow&lt;/math>
610	23 &lt;math>\mathbb{N}&lt;/math>)
611	24 (h1 : &lt;math>\forall y, f\ 0\ y = y + 1&lt;/math>)
612	25 (h2 : &lt;math>\forall x, f\ (x + 1)\ 0 = f\ x\ 1&lt;/math>)
613	26 (h3 : &lt;math>\forall x\ y, f\ (x + 1)\ (y + 1) =&lt;/math>
614	27 &lt;math>f\ x\ (f\ (x + 1)\ y)) :
615	28 f\ 4\ 1981 = solution_value :=
616	29 sorry&lt;/math>&lt;/pre>
617	&lt;/td>
618	&lt;/tr>
619	&lt;/tbody>
620	&lt;/table>
621	
622	The informal statement requires computing the exact value of  $f(4, 1981)$ , a specific number. However, the MiniF2F formalization only asks to prove a general recurrence relation, which is an intermediate step in the solution process. This discrepancy can make the formal proof substantially easier than solving the original problem. In contrast, MathOlympiadBench faithfully translates the original problem into formal language, requiring the proof of the final numerical value as demanded by the IMO statement.A.2 IMO 1983, PROBLEM 6: INCOMPLETE VS. FULL CONDITION
623	
624	```
625	
626	MiniF2F
627	1  /-- Let a, b and c be the lengths
628	2  of the sides of a triangle.
629	3  Prove that
630	4
631	5  a^2b(a-b) + b^2c(b-c) + c^2a(c-a) ≥ 0.
632	6
633	7  Determine when equality occurs.
634	8  -/
635	9
636	10 theorem imo_1983_p6 (a b c : ℝ)
637	11   (h0 : 0 < a ∧ 0 < b ∧ 0 < c)
638	12   (h1 : c < a + b) (h2 : b < a +
639	13   c)
640	14   (h3 : a < b + c) :
641	15   0 ≤ a^2*b*(a-b) + b^2*c*(b-c) +
642	16   c^2*a*(c-a) := by
643	
644	```
645	
646	```
647	
648	MathOlympiadBench
649	1  /-!
650	2  # International Mathematical
651	3  Olympiad 1983, Problem 6
652	4
653	5  Suppose that a,b,c are the side
654	6  lengths of a triangle. Prove
655	7  that
656	8
657	9  a^2b(a-b) + b^2c(b-c) + c^2a(c-a) ≥ 0.
658	10
659	11  Determine when equality occurs.
660	12  -/
661	13
662	14 abbrev EqualityCondition (a b c :
663	15   ℝ) : Prop :=
664	16   a = b ∧ a = c
665	17
666	18 theorem imo1983_p6
667	19   (T : Affine.Triangle ℝ
668	20   (EuclideanSpace ℝ (Fin 2))) :
669	21   let a := dist (T.points 1)
670	22   (T.points 2)
671	23   let b := dist (T.points 0)
672	24   (T.points 2)
673	25   let c := dist (T.points 0)
674	26   (T.points 1)
675	27   0 ≤ a^2*b*(a-b) + b^2*c*(b-c) +
676	28   c^2*a*(c-a) ∧
677	29   (0 = a^2*b*(a-b) + b^2*c*(b-c) +
678	30   c^2*a*(c-a) ↔
679	31   EqualityCondition a b c) :=
680	32   sorry
681	
682	```
683	
684	The informal statement has two parts: proving an inequality and determining the condition for equality. The MiniF2F version only formalizes the inequality, completely omitting the second part of the problem. In contrast, MathOlympiadBench provides a complete formalization.A.3 IMO 1962, PROBLEM 2: INFORMAL & FORMAL STATEMENT MISMATCH
685	
686	&lt;table border="1">
687	&lt;thead>
688	&lt;tr>
689	&lt;th>MiniF2F&lt;/th>
690	&lt;th>MathOlympiadBench&lt;/th>
691	&lt;/tr>
692	&lt;/thead>
693	&lt;tbody>
694	&lt;tr>
695	&lt;td>
696	&lt;pre>1 /-- Determine all real numbers x
697	2   which satisfy the inequality:
698	3
699	4   &lt;math>\sqrt{\sqrt{3-x}-\sqrt{x+1}} &gt; \frac{1}{2}&lt;/math>
700	5
701	6   Show that it is &lt;math>\left[-1, 1 - \frac{\sqrt{127}}{32}\right)&lt;/math>.
702	7   -/
703	8
704	9   theorem imo_1962_p2 (x : ℝ) (h0 :
705	10      0 ≤ 3 - x) (h1 : 0 ≤ x + 1)
706	11      (h2 : 1 / 2 &lt; Real.sqrt (3 -
707	12      x) - Real.sqrt (x + 1)) : -1 ≤
708	13      x ∧ x &lt; 1 - Real.sqrt 31 / 8
709	14      := sorry&lt;/pre>
710	&lt;/td>
711	&lt;td>
712	&lt;pre>1 /-!
713	2 # International Mathematical
714	3   Olympiad 1962, Problem 2
715	4
716	5 Determine all real numbers x
717	6   which satisfy
718	7
719	8   &lt;math>\sqrt{3-x}-\sqrt{x+1} &gt; \frac{1}{2}&lt;/math>.
720	9   -/
721	10
722	11 abbrev SolutionSet : Set ℝ :=
723	12     Set.Ico (-1) (1 - &lt;math>\sqrt{31} / 8&lt;/math>)
724	13
725	14 theorem imo1962_p2 (x : ℝ) :
726	15   x ∈ SolutionSet ↔
727	16   x ≤ 3 ∧ -1 ≤ x ∧ 1/2 &lt; &lt;math>\sqrt{(3-x)}&lt;/math>
728	17   - &lt;math>\sqrt{(x+1)}&lt;/math> := sorry&lt;/pre>
729	&lt;/td>
730	&lt;/tr>
731	&lt;/tbody>
732	&lt;/table>
733	
734	For this problem, the original inequality appears in two different versions&lt;sup>6&lt;/sup>: one as  $\sqrt{3-x}-\sqrt{x+1} > \frac{1}{2}$  and another as  $\sqrt{\sqrt{3-x}-\sqrt{x+1}} > \frac{1}{2}$ . In MiniF2F, the informal statement uses the latter (the nested square root version), but the formal statement is based on the former (the simpler difference of square roots), resulting in a mismatch between the informal and formal statements. In contrast, MathOlympiadBench ensures that both the informal and formal statements consistently correspond to the same version of the problem.
735	
736	B FORMAL NEGATION
737	
738	We attempt to disprove unsolved statements by proving their logical negation. This is achieved by parsing the Lean 4 statements as follows.
739	
740	&lt;table border="1">
741	&lt;tbody>
742	&lt;tr>
743	&lt;td>
744	&lt;pre>1 theorem fourIsPrime (a : ℕ) (ha : a = 4) : a.Prime := by sorry
745	2 theorem fourIsPrimeNeg : ¬ ∃ (a : ℕ) (ha : a = 4), a.Prime := by sorry&lt;/pre>
746	&lt;/td>
747	&lt;/tr>
748	&lt;/tbody>
749	&lt;/table>
750	
751	C DETAILS FOR JUDGING FORMALIZATION
752	
753	Here is the exact prompt for LLM judging the faithfulness of formalization.
754	
755	&lt;table border="1">
756	&lt;tbody>
757	&lt;tr>
758	&lt;td>
759	&lt;p>You will receive a math problem consisting of its natural language statement along with its formal statement in LEAN 4.&lt;/p>
760	&lt;p>Please evaluate whether the formal LEAN statement appropriately translates the natural language statement based on the following criteria:&lt;/p>
761	&lt;ol>
762	&lt;li>1. Key Elements: The problem's essential components are correctly represented in LEAN code.&lt;/li>
763	&lt;li>2. Mathematical Accuracy: The translation preserves the accuracy of the mathematical content.&lt;/li>
764	&lt;li>3. Structural Fidelity: The translation aligns closely with the original problem, maintaining its structure and purpose.&lt;/li>
765	&lt;/ol>
766	&lt;/td>
767	&lt;/tr>
768	&lt;/tbody>
769	&lt;/table>
770	
771	&lt;sup>6&lt;/sup>Please refer to: [https://artofproblemsolving.com/wiki/index.php/1962\\_IMO\\_Problems/Problem\\_2](https://artofproblemsolving.com/wiki/index.php/1962_IMO_Problems/Problem_2).4. Comprehensiveness: All assumptions, conditions, and goals present in the natural language statement are included in the LEAN translation.
772	
773	Your answer should be in the following format:
774	
775	Thought: [Your Answer]
776	
777	Judgement: [Your Answer, one of {Appropriate, Inappropriate}]
778	
779	---
780	
781	Following are the example problems label for the reasonability of their translation.
782	
783	# Example 1:
784	
785	## Original natural language statement of the problem:
786	
787	For the graph of a certain quadratic  $y = ax^2 + bx + c$ , the vertex of the parabola is  $(2, 10)$ , and one of the  $x$ -intercepts is  $(1, 0)$ . What is the  $x$ -coordinate of the other  $x$ -intercept?
788	
789	## Translated formal statement:
790	
791	```
792	
793	```lean
794	theorem quadratic_other_intercept
795	  (f : ℝ → ℝ)
796	  (a b c : ℝ)
797	  (h_quad : ∀ x, f x = a * x^2 + b * x + c)
798	  (h_vertex : f 2 = 10 ∧ ∀ x, f x ≤ f 2)    -- vertex at (2,10)
799	  (h_intercept1 : f 1 = 0) :                -- x-intercept at (1,0)
800	  f 3 = 0 := by                             -- other x-intercept at
801	  (3, 0)
802	```
803	
804	```
805	
806	Thought: The Lean translation of the problem is appropriate because it accurately captures the intent and reasoning of the original problem. The problem's key elements, such as the vertex, axis of symmetry, and  $x$ -intercepts of the quadratic function, are correctly translated into Lean code. The logical flow of the proof mirrors the original reasoning, starting with the symmetry property of the quadratic function and using it to determine the second  $x$ -intercept. The mathematical accuracy is preserved, as the proof correctly applies the vertex property and symmetry to arrive at the solution. Furthermore, the translation aligns well with the original problem in natural language, maintaining fidelity to its structure and purpose. Overall, the translation is both faithful and complete, making it an appropriate representation of the original problem.
807	
808	Judgement: Appropriate
809	
810	# Example 2:
811	
812	## Original natural language statement of the problem:
813	
814	Draw a tangent line from the point  $(4, 3)$  to the circle  $(x - 2)^2 + (y - 1)^2 = 1$ . What is the equation of the line that passes through the two tangent points?
815	
816	## Translated formal statement:
817	
818	```
819	
820	```lean
821	theorem tangent_line_equation (x y : ℝ) :
822	  let P : ℝ × ℝ := (4, 3)    -- Point P
823	  let C : ℝ × ℝ := (2, 1)    -- Center of first circle
824	
825	``````
826	
827	let r : ℝ := 1           -- Radius of first circle
828	-- Points (x,y) satisfying both circle equations
829	let on_first_circle := (x - 2)^2 + (y - 1)^2 = 1
830	let on_second_circle := (x - 3)^2 + (y - 2)^2 = 2
831	-- If point is on both circles
832	on_first_circle ∧ on_second_circle →
833	-- Then it lies on the line 2x + 2y - 7 = 0
834	2*x + 2*y - 7 = 0 := by
835	```
836	
837	```
838	
839	Thought: The Lean translation of the problem is inappropriate because it fundamentally changes the intent of the original problem. The original problem asks to derive the equation of the tangent line passing through the intersection points of two circles, but the translation assumes the equation  $(2x + 2y - 7 = 0)$  is already given and instead asks to prove that the intersection points lie on this line. This shifts the problem from a construction task to a verification task, losing the original problem's focus on deriving the result through geometric and algebraic reasoning. Additionally, the translation omits the key reasoning step of subtracting the circle equations to derive the line equation, which is central to the original problem. As a result, the translation fails to accurately represent the problem's intent and educational value, making it an incomplete and inappropriate representation.
840	
841	Judgement: Inappropriate
842	
843	Example3:
844	
845	## Original natural language statement of the problem:
846	
847	If  $a, b, c, d > 0$  and  $abcd = 1$ , prove that  $\frac{1}{a+b+c+1} + \frac{1}{b+c+d+1} + \frac{1}{c+d+a+1} + \frac{1}{d+a+b+1} \leq \frac{1}{a+3} + \frac{1}{b+3} + \frac{1}{c+3} + \frac{1}{d+3}$
848	
849	## Translated formal statement:
850	
851	```
852	
853	```lean4
854	theorem lean_workbook_49553 (a b c d : ℝ) (habc : a * b * c * d = 1) :
855	  (1 / (a + b + c + 1) + 1 / (b + c + d + 1) + 1 / (c + d + a + 1) +
856	  1 / (d + a + b + 1)) ≤ (1 / (a + 3) + 1 / (b + 3) + 1 / (c + 3) + 1
857	  / (d + 3)) := by sorry
858	```
859	
860	```
861	
862	Thought: The Lean translation of the problem is inappropriate because the condition  $a, b, c, d > 0$  is ignored in the formal statement.
863	
864	Judgement: Inappropriate
865	
866	Example4:
867	
868	## Original natural language statement of the problem:
869	
870	If  $a = b = c = 2$  so  $\sum_{cyc} \frac{(a-1)^2}{a^2+2} = \frac{1}{2}$ . We'll prove that  $\frac{1}{2}$  is the answer.
871	
872	## Translated formal statement:
873	
874	```
875	
876	```lean4
877	theorem lean_workbook_plus_1478 (a b c : ℝ) (ha : a = 2) (hb : b = 2)
878	  (hc : c = 2) : (a - 1) ^ 2 / (a ^ 2 + 2) + (b - 1) ^ 2 / (b ^ 2 +
879	  2) + (c - 1) ^ 2 / (c ^ 2 + 2) = 1 / 2 := by sorry
880	```
881	
882	``````
883	
884	Thought: The Lean translation of the problem is appropriate because it
885	accurately captures the assumptions and the goal in the natural
886	language statement.
887	
888	Judgement: Appropriate
889	
890	## Original natural language statement of the problem:
891	
892	{informal_statement}
893	
894	## Translated formal statement:
895	```lean4
896	{formal_statement}
897	```
898	
899	```
```````

</details>

<details><summary>Recorded metadata</summary>

```````json
{
  "recorded_role": "user",
  "parentUuid": "57449196-73e3-4228-9f9c-ad6b8d84aa1b",
  "isSidechain": false,
  "promptId": "918f738b-eddd-4a71-9661-57e87bd9f8ed",
  "type": "user",
  "uuid": "8c82f0af-8b19-4490-bf7b-30d01652301f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/6db262d6-dcf8-4dbf-b94b-349936024bbc/tool-results/toolu_01Tq8krFT3t8xgN1SnQrexGw.txt",
      "content": "Aixin Liu, Bei Feng, Bing Xue, Bingxuan Wang, Bochao Wu, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chenyu Zhang, Chong Ruan, et al. Deepseek-v3 technical report. *arXiv preprint arXiv:2412.19437*, 2024.\n\nZichen Liu, Changyu Chen, Wenjun Li, Penghui Qi, Tianyu Pang, Chao Du, Wee Sun Lee, and Min Lin. Understanding r1-zero-like training: A critical perspective. *arXiv preprint arXiv:2503.20783*, 2025.\n\nLeonardo de Moura and Sebastian Ullrich. The Lean 4 theorem prover and programming language. In *International Conference on Automated Deduction (CADE)*, 2021.\n\nTheo X. Olausson, Jeevana Priya Inala, Chenglong Wang, Jianfeng Gao, and Armando Solar-Lezama. Is self-repair a silver bullet for code generation? In *The Twelfth International Conference on Learning Representations*, 2024.\n\nBowen Peng, Jeffrey Quesnelle, Honglu Fan, and Enrico Shippole. YaRN: Efficient context window extension of large language models. In *The Twelfth International Conference on Learning Representations*, 2024. URL &lt;https://openreview.net/forum?id=wHBfxhZulu>.\n\nIvo Petrov, Jasper Dekoninck, Lyuben Baltadzhiev, Maria Drencheva, Kristian Minchev, Mislav Balunović, Nikola Jovanović, and Martin Vechev. Proof or bluff? evaluating llms on 2025 usa math olympiad. *arXiv preprint arXiv:2503.21934*, 2025.\n\nZZ Ren, Zhihong Shao, Junxiao Song, Huajian Xin, Haocheng Wang, Wanjia Zhao, Liyue Zhang, Zhe Fu, Qihao Zhu, Dejian Yang, et al. Deepseek-prover-v2: Advancing formal mathematical reasoning via reinforcement learning for subgoal decomposition. *arXiv preprint arXiv:2504.21801*, 2025.\n\nZhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li, Y Wu, et al. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. *arXiv preprint arXiv:2402.03300*, 2024.\n\nGuangming Sheng, Chi Zhang, Zilingfeng Ye, Xibin Wu, Wang Zhang, Ru Zhang, Yanghua Peng, Haibin Lin, and Chuan Wu. Hybridflow: A flexible and efficient rlhf framework. *arXiv preprint arXiv: 2409.19256*, 2024.\n\nNoah Shinn, Federico Cassano, Ashwin Gopinath, Karthik R Narasimhan, and Shunyu Yao. Reflexion: language agents with verbal reinforcement learning. In *Thirty-seventh Conference on Neural Information Processing Systems*, 2023.\n\nTrieu H Trinh, Yuhuai Wu, Quoc V Le, He He, and Thang Luong. Solving olympiad geometry without human demonstrations. *Nature*, 625(7995):476–482, 2024.\n\nGeorge Tsoukalas, Jasper Lee, John Jennings, Jimmy Xin, Michelle Ding, Michael Jennings, Amitayush Thakur, and Swarat Chaudhuri. Putnambench: Evaluating neural theorem-provers on the putnam mathematical competition. *arXiv preprint arXiv:2407.11214*, 2024.\n\nHaiming Wang, Mert Unsal, Xiaohan Lin, Mantas Baksys, Junqi Liu, Marco Dos Santos, Flood Sung, Marina Vinyes, Zhenzhe Ying, Zekai Zhu, et al. Kimina-prover preview: Towards large formal reasoning models with reinforcement learning. *arXiv preprint arXiv:2504.11354*, 2025.\n\nMitchell Wortsman, Gabriel Ilharco, Samir Ya Gadre, Rebecca Roelofs, Raphael Gontijo-Lopes, Ari S Morcos, Hongseok Namkoong, Ali Farhadi, Yair Carmon, Simon Kornblith, et al. Model soups: averaging weights of multiple fine-tuned models improves accuracy without increasing inference time. In *International conference on machine learning*, pp. 23965–23998. PMLR, 2022a.Mitchell Wortsman, Gabriel Ilharco, Jong Wook Kim, Mike Li, Simon Kornblith, Rebecca Roelofs, Raphael Gontijo Lopes, Hannaneh Hajishirzi, Ali Farhadi, Hongseok Namkoong, et al. Robust fine-tuning of zero-shot models. In *Proceedings of the IEEE/CVF conference on computer vision and pattern recognition*, pp. 7959–7971, 2022b.\n\nZijian Wu, Suozhi Huang, Zhejian Zhou, Huaiyuan Ying, Jiayu Wang, Dahua Lin, and Kai Chen. InternLM2.5-StepProver: Advancing automated theorem proving via expert iteration on large-scale lean problems. *arXiv preprint arXiv:2410.15700*, 2024.\n\nHuajian Xin, Daya Guo, Zhihong Shao, Zhizhou Ren, Qihao Zhu, Bo Liu, Chong Ruan, Wenda Li, and Xiaodan Liang. Deepseek-prover: Advancing theorem proving in llms through large-scale synthetic data. *arXiv preprint arXiv:2405.14333*, 2024a.\n\nHuajian Xin, ZZ Ren, Junxiao Song, Zhihong Shao, Wanjia Zhao, Haocheng Wang, Bo Liu, Liyue Zhang, Xuan Lu, Qiushi Du, et al. Deepseek-prover-v1.5: Harnessing proof assistant feedback for reinforcement learning and monte-carlo tree search. *arXiv preprint arXiv:2408.08152*, 2024b.\n\nRan Xin, Chenguang Xi, Jie Yang, Feng Chen, Hang Wu, Xia Xiao, Yifan Sun, Shen Zheng, and Ming Ding. BFS-prover: Scalable best-first tree search for LLM-based automatic theorem proving. In *Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics*, 2025.\n\nKaiyu Yang, Aidan Swope, Alex Gu, Rahul Chalamala, Peiyang Song, Shixing Yu, Saad Godil, Ryan J Prenger, and Animashree Anandkumar. Leandojo: Theorem proving with retrieval-augmented language models. *Advances in Neural Information Processing Systems*, 36, 2024.\n\nShunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, and Karthik R Narasimhan. Tree of thoughts: Deliberate problem solving with large language models. In *Thirty-seventh Conference on Neural Information Processing Systems*, 2023.\n\nQiyong Yu, Zheng Zhang, Ruofei Zhu, Yufeng Yuan, Xiaochen Zuo, Yu Yue, Weinan Dai, Tiantian Fan, Gaohong Liu, Lingjun Liu, et al. Dapo: An open-source llm reinforcement learning system at scale. *arXiv preprint arXiv:2503.14476*, 2025.\n\nYang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Shiji Song, and Gao Huang. Does reinforcement learning really incentivize reasoning capacity in llms beyond the base model? *arXiv preprint arXiv:2504.13837*, 2025.\n\nKunhao Zheng, Jesse Michael Han, and Stanislas Polu. Minif2f: a cross-system benchmark for formal olympiad-level mathematics. *arXiv preprint arXiv:2109.00110*, 2021.\n\nYichi Zhou, Jianqiu Zhao, Yongxin Zhang, Bohan Wang, Siran Wang, Luoxin Chen, Jiahui Wang, Haowei Chen, Allan Jie, Xinbo Zhang, et al. Solving formal math problems by decomposition and iterative reflection. *arXiv preprint arXiv:2507.15225*, 2025.APPENDIXA DETAILS OF MATHOLYMPIADBENCH\n\nMathOlympiadBench is human-processed to eliminate several issues presented in the source problems: 1. incomplete problem statements, 2. distribution across multiple files, 3. multiple theorems per problem, and 4. incompatibility with the commonly used Mathlib. The verification process ensures that each problem contains exactly one formal theorem with its corresponding informal statement, and confirms that all formal statements can pass the compilation with the `sorry` tactic.\n\nWe compared the IMO problems shared between MathOlympiadBench and MiniF2F, and identified at least 3 cases in MiniF2F exhibiting issues such as: 1. the formal statement to be proved is strictly weaker than the informal statement, and 2. the formal statement does not match the informal statement. Notably, similar issues are not observed for these problems in MathOlympiadBench.\n\nIn the following, we present three case studies comparing the problem formalizations in MiniF2F and MathOlympiadBench.\n\nA.1 IMO 1981, PROBLEM 6: SPECIFIC VALUE VS. GENERAL FORMULA\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>MiniF2F&lt;/th>\n&lt;th>MathOlympiadBench&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>\n&lt;pre>1 /--\n2 The function &lt;math>f(x,y)&lt;/math> satisfies\n3\n4 (1) &lt;math>f(0,y) = y + 1&lt;/math>,\n5\n6 (2) &lt;math>f(x+1,0) = f(x,1)&lt;/math>,\n7\n8 (3) &lt;math>f(x+1,y+1) = f(x,f(x+1,y))&lt;/math>,\n9\n10 for all non-negative integers &lt;math>x,y&lt;/math>\n11 . Determine &lt;math>f(4,1981)&lt;/math>.\n12 -/\n13 theorem imo_1981_p6 (f : &lt;math>\\mathbb{N} \\rightarrow \\mathbb{N} \\rightarrow&lt;/math>\n14 &lt;math>\\mathbb{N}&lt;/math>)\n15 (h0 : &lt;math>\\forall y, f\\ 0\\ y = y + 1&lt;/math>)\n16 (h1 : &lt;math>\\forall x, f\\ (x + 1)\\ 0 = f\\ x\\ 1&lt;/math>)\n17 (h2 : &lt;math>\\forall x\\ y, f\\ (x + 1)\\ (y + 1) =&lt;/math>\n18 &lt;math>f\\ x\\ (f\\ (x + 1)\\ y)) :\n19 &lt;math>\\forall y, f\\ 4\\ (y + 1) = 2 \\wedge (f\\ 4\\ y +&lt;/math>\n20 &lt;math>3) - 3 := by&lt;/math>&lt;/math>&lt;/pre>\n&lt;/td>\n&lt;td>\n&lt;pre>1 /-!\n2 # International Mathematical\n3   Olympiad 1981, Problem 6\n4\n5 Suppose that &lt;math>f : \\mathbb{N} \\times \\mathbb{N} \\rightarrow \\mathbb{N}&lt;/math>\n6 satisfies\n7\n8 1) &lt;math>f\\ (0, y) = y + 1&lt;/math>\n9 2) &lt;math>f\\ (x + 1, 0) = f\\ (x, 1)&lt;/math>,\n10 3) &lt;math>f\\ (x + 1, y + 1) = f\\ (x, f\\ (x&lt;/math>\n11 &lt;math>+ 1, y))&lt;/math>\n12\n13 for all &lt;math>x\\ y \\in \\mathbb{N}&lt;/math>.\n14\n15 Determine &lt;math>f\\ (4, 1981)&lt;/math>.\n16 -/\n17\n18 def no_eval (x : &lt;math>\\mathbb{N}&lt;/math>) : &lt;math>\\mathbb{N} := x&lt;/math>\n19 abbrev solution_value : &lt;math>\\mathbb{N} :=&lt;/math>\n20 no_eval ((2^·)^[1984] 1 - 3)\n21\n22 theorem imo1981_p6 (f : &lt;math>\\mathbb{N} \\rightarrow \\mathbb{N} \\rightarrow&lt;/math>\n23 &lt;math>\\mathbb{N}&lt;/math>)\n24 (h1 : &lt;math>\\forall y, f\\ 0\\ y = y + 1&lt;/math>)\n25 (h2 : &lt;math>\\forall x, f\\ (x + 1)\\ 0 = f\\ x\\ 1&lt;/math>)\n26 (h3 : &lt;math>\\forall x\\ y, f\\ (x + 1)\\ (y + 1) =&lt;/math>\n27 &lt;math>f\\ x\\ (f\\ (x + 1)\\ y)) :\n28 f\\ 4\\ 1981 = solution_value :=\n29 sorry&lt;/math>&lt;/pre>\n&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nThe informal statement requires computing the exact value of  $f(4, 1981)$ , a specific number. However, the MiniF2F formalization only asks to prove a general recurrence relation, which is an intermediate step in the solution process. This discrepancy can make the formal proof substantially easier than solving the original problem. In contrast, MathOlympiadBench faithfully translates the original problem into formal language, requiring the proof of the final numerical value as demanded by the IMO statement.A.2 IMO 1983, PROBLEM 6: INCOMPLETE VS. FULL CONDITION\n\n```\n\nMiniF2F\n1  /-- Let a, b and c be the lengths\n2  of the sides of a triangle.\n3  Prove that\n4\n5  a^2b(a-b) + b^2c(b-c) + c^2a(c-a) ≥ 0.\n6\n7  Determine when equality occurs.\n8  -/\n9\n10 theorem imo_1983_p6 (a b c : ℝ)\n11   (h0 : 0 < a ∧ 0 < b ∧ 0 < c)\n12   (h1 : c < a + b) (h2 : b < a +\n13   c)\n14   (h3 : a < b + c) :\n15   0 ≤ a^2*b*(a-b) + b^2*c*(b-c) +\n16   c^2*a*(c-a) := by\n\n```\n\n```\n\nMathOlympiadBench\n1  /-!\n2  # International Mathematical\n3  Olympiad 1983, Problem 6\n4\n5  Suppose that a,b,c are the side\n6  lengths of a triangle. Prove\n7  that\n8\n9  a^2b(a-b) + b^2c(b-c) + c^2a(c-a) ≥ 0.\n10\n11  Determine when equality occurs.\n12  -/\n13\n14 abbrev EqualityCondition (a b c :\n15   ℝ) : Prop :=\n16   a = b ∧ a = c\n17\n18 theorem imo1983_p6\n19   (T : Affine.Triangle ℝ\n20   (EuclideanSpace ℝ (Fin 2))) :\n21   let a := dist (T.points 1)\n22   (T.points 2)\n23   let b := dist (T.points 0)\n24   (T.points 2)\n25   let c := dist (T.points 0)\n26   (T.points 1)\n27   0 ≤ a^2*b*(a-b) + b^2*c*(b-c) +\n28   c^2*a*(c-a) ∧\n29   (0 = a^2*b*(a-b) + b^2*c*(b-c) +\n30   c^2*a*(c-a) ↔\n31   EqualityCondition a b c) :=\n32   sorry\n\n```\n\nThe informal statement has two parts: proving an inequality and determining the condition for equality. The MiniF2F version only formalizes the inequality, completely omitting the second part of the problem. In contrast, MathOlympiadBench provides a complete formalization.A.3 IMO 1962, PROBLEM 2: INFORMAL & FORMAL STATEMENT MISMATCH\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>MiniF2F&lt;/th>\n&lt;th>MathOlympiadBench&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>\n&lt;pre>1 /-- Determine all real numbers x\n2   which satisfy the inequality:\n3\n4   &lt;math>\\sqrt{\\sqrt{3-x}-\\sqrt{x+1}} &gt; \\frac{1}{2}&lt;/math>\n5\n6   Show that it is &lt;math>\\left[-1, 1 - \\frac{\\sqrt{127}}{32}\\right)&lt;/math>.\n7   -/\n8\n9   theorem imo_1962_p2 (x : ℝ) (h0 :\n10      0 ≤ 3 - x) (h1 : 0 ≤ x + 1)\n11      (h2 : 1 / 2 &lt; Real.sqrt (3 -\n12      x) - Real.sqrt (x + 1)) : -1 ≤\n13      x ∧ x &lt; 1 - Real.sqrt 31 / 8\n14      := sorry&lt;/pre>\n&lt;/td>\n&lt;td>\n&lt;pre>1 /-!\n2 # International Mathematical\n3   Olympiad 1962, Problem 2\n4\n5 Determine all real numbers x\n6   which satisfy\n7\n8   &lt;math>\\sqrt{3-x}-\\sqrt{x+1} &gt; \\frac{1}{2}&lt;/math>.\n9   -/\n10\n11 abbrev SolutionSet : Set ℝ :=\n12     Set.Ico (-1) (1 - &lt;math>\\sqrt{31} / 8&lt;/math>)\n13\n14 theorem imo1962_p2 (x : ℝ) :\n15   x ∈ SolutionSet ↔\n16   x ≤ 3 ∧ -1 ≤ x ∧ 1/2 &lt; &lt;math>\\sqrt{(3-x)}&lt;/math>\n17   - &lt;math>\\sqrt{(x+1)}&lt;/math> := sorry&lt;/pre>\n&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nFor this problem, the original inequality appears in two different versions&lt;sup>6&lt;/sup>: one as  $\\sqrt{3-x}-\\sqrt{x+1} > \\frac{1}{2}$  and another as  $\\sqrt{\\sqrt{3-x}-\\sqrt{x+1}} > \\frac{1}{2}$ . In MiniF2F, the informal statement uses the latter (the nested square root version), but the formal statement is based on the former (the simpler difference of square roots), resulting in a mismatch between the informal and formal statements. In contrast, MathOlympiadBench ensures that both the informal and formal statements consistently correspond to the same version of the problem.\n\nB FORMAL NEGATION\n\nWe attempt to disprove unsolved statements by proving their logical negation. This is achieved by parsing the Lean 4 statements as follows.\n\n&lt;table border=\"1\">\n&lt;tbody>\n&lt;tr>\n&lt;td>\n&lt;pre>1 theorem fourIsPrime (a : ℕ) (ha : a = 4) : a.Prime := by sorry\n2 theorem fourIsPrimeNeg : ¬ ∃ (a : ℕ) (ha : a = 4), a.Prime := by sorry&lt;/pre>\n&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nC DETAILS FOR JUDGING FORMALIZATION\n\nHere is the exact prompt for LLM judging the faithfulness of formalization.\n\n&lt;table border=\"1\">\n&lt;tbody>\n&lt;tr>\n&lt;td>\n&lt;p>You will receive a math problem consisting of its natural language statement along with its formal statement in LEAN 4.&lt;/p>\n&lt;p>Please evaluate whether the formal LEAN statement appropriately translates the natural language statement based on the following criteria:&lt;/p>\n&lt;ol>\n&lt;li>1. Key Elements: The problem's essential components are correctly represented in LEAN code.&lt;/li>\n&lt;li>2. Mathematical Accuracy: The translation preserves the accuracy of the mathematical content.&lt;/li>\n&lt;li>3. Structural Fidelity: The translation aligns closely with the original problem, maintaining its structure and purpose.&lt;/li>\n&lt;/ol>\n&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n&lt;sup>6&lt;/sup>Please refer to: [https://artofproblemsolving.com/wiki/index.php/1962\\\\_IMO\\\\_Problems/Problem\\\\_2](https://artofproblemsolving.com/wiki/index.php/1962_IMO_Problems/Problem_2).4. Comprehensiveness: All assumptions, conditions, and goals present in the natural language statement are included in the LEAN translation.\n\nYour answer should be in the following format:\n\nThought: [Your Answer]\n\nJudgement: [Your Answer, one of {Appropriate, Inappropriate}]\n\n---\n\nFollowing are the example problems label for the reasonability of their translation.\n\n# Example 1:\n\n## Original natural language statement of the problem:\n\nFor the graph of a certain quadratic  $y = ax^2 + bx + c$ , the vertex of the parabola is  $(2, 10)$ , and one of the  $x$ -intercepts is  $(1, 0)$ . What is the  $x$ -coordinate of the other  $x$ -intercept?\n\n## Translated formal statement:\n\n```\n\n```lean\ntheorem quadratic_other_intercept\n  (f : ℝ → ℝ)\n  (a b c : ℝ)\n  (h_quad : ∀ x, f x = a * x^2 + b * x + c)\n  (h_vertex : f 2 = 10 ∧ ∀ x, f x ≤ f 2)    -- vertex at (2,10)\n  (h_intercept1 : f 1 = 0) :                -- x-intercept at (1,0)\n  f 3 = 0 := by                             -- other x-intercept at\n  (3, 0)\n```\n\n```\n\nThought: The Lean translation of the problem is appropriate because it accurately captures the intent and reasoning of the original problem. The problem's key elements, such as the vertex, axis of symmetry, and  $x$ -intercepts of the quadratic function, are correctly translated into Lean code. The logical flow of the proof mirrors the original reasoning, starting with the symmetry property of the quadratic function and using it to determine the second  $x$ -intercept. The mathematical accuracy is preserved, as the proof correctly applies the vertex property and symmetry to arrive at the solution. Furthermore, the translation aligns well with the original problem in natural language, maintaining fidelity to its structure and purpose. Overall, the translation is both faithful and complete, making it an appropriate representation of the original problem.\n\nJudgement: Appropriate\n\n# Example 2:\n\n## Original natural language statement of the problem:\n\nDraw a tangent line from the point  $(4, 3)$  to the circle  $(x - 2)^2 + (y - 1)^2 = 1$ . What is the equation of the line that passes through the two tangent points?\n\n## Translated formal statement:\n\n```\n\n```lean\ntheorem tangent_line_equation (x y : ℝ) :\n  let P : ℝ × ℝ := (4, 3)    -- Point P\n  let C : ℝ × ℝ := (2, 1)    -- Center of first circle\n\n``````\n\nlet r : ℝ := 1           -- Radius of first circle\n-- Points (x,y) satisfying both circle equations\nlet on_first_circle := (x - 2)^2 + (y - 1)^2 = 1\nlet on_second_circle := (x - 3)^2 + (y - 2)^2 = 2\n-- If point is on both circles\non_first_circle ∧ on_second_circle →\n-- Then it lies on the line 2x + 2y - 7 = 0\n2*x + 2*y - 7 = 0 := by\n```\n\n```\n\nThought: The Lean translation of the problem is inappropriate because it fundamentally changes the intent of the original problem. The original problem asks to derive the equation of the tangent line passing through the intersection points of two circles, but the translation assumes the equation  $(2x + 2y - 7 = 0)$  is already given and instead asks to prove that the intersection points lie on this line. This shifts the problem from a construction task to a verification task, losing the original problem's focus on deriving the result through geometric and algebraic reasoning. Additionally, the translation omits the key reasoning step of subtracting the circle equations to derive the line equation, which is central to the original problem. As a result, the translation fails to accurately represent the problem's intent and educational value, making it an incomplete and inappropriate representation.\n\nJudgement: Inappropriate\n\nExample3:\n\n## Original natural language statement of the problem:\n\nIf  $a, b, c, d > 0$  and  $abcd = 1$ , prove that  $\\frac{1}{a+b+c+1} + \\frac{1}{b+c+d+1} + \\frac{1}{c+d+a+1} + \\frac{1}{d+a+b+1} \\leq \\frac{1}{a+3} + \\frac{1}{b+3} + \\frac{1}{c+3} + \\frac{1}{d+3}$\n\n## Translated formal statement:\n\n```\n\n```lean4\ntheorem lean_workbook_49553 (a b c d : ℝ) (habc : a * b * c * d = 1) :\n  (1 / (a + b + c + 1) + 1 / (b + c + d + 1) + 1 / (c + d + a + 1) +\n  1 / (d + a + b + 1)) ≤ (1 / (a + 3) + 1 / (b + 3) + 1 / (c + 3) + 1\n  / (d + 3)) := by sorry\n```\n\n```\n\nThought: The Lean translation of the problem is inappropriate because the condition  $a, b, c, d > 0$  is ignored in the formal statement.\n\nJudgement: Inappropriate\n\nExample4:\n\n## Original natural language statement of the problem:\n\nIf  $a = b = c = 2$  so  $\\sum_{cyc} \\frac{(a-1)^2}{a^2+2} = \\frac{1}{2}$ . We'll prove that  $\\frac{1}{2}$  is the answer.\n\n## Translated formal statement:\n\n```\n\n```lean4\ntheorem lean_workbook_plus_1478 (a b c : ℝ) (ha : a = 2) (hb : b = 2)\n  (hc : c = 2) : (a - 1) ^ 2 / (a ^ 2 + 2) + (b - 1) ^ 2 / (b ^ 2 +\n  2) + (c - 1) ^ 2 / (c ^ 2 + 2) = 1 / 2 := by sorry\n```\n\n``````\n\nThought: The Lean translation of the problem is appropriate because it\naccurately captures the assumptions and the goal in the natural\nlanguage statement.\n\nJudgement: Appropriate\n\n## Original natural language statement of the problem:\n\n{informal_statement}\n\n## Translated formal statement:\n```lean4\n{formal_statement}\n```\n\n```",
      "numLines": 400,
      "startLine": 500,
      "totalLines": 1092
    }
  },
  "sourceToolAssistantUUID": "57449196-73e3-4228-9f9c-ad6b8d84aa1b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```````

</details>

---

### Runtime record

_source line 53_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-27 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "8c82f0af-8b19-4490-bf7b-30d01652301f",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc"
}
```

---

### Runtime record

_source line 54_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze Goedel-Prover-V2 paper innovation",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc"
}
```

---

### Assistant

_source line 55 · 2026-05-27T15:59:09.743Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the paper. Let me also try to find any additional details about the RL approach and model averaging that I might have missed.

Let me compile my analysis now. I have all the key information:

1. **Problem identification**: They identify three gaps: (a) data scarcity for formal proofs, (b) existing provers don't leverage verifier feedback systematically for long-CoT models, (c) diversity collapse during later training stages.

2. **Key insight**: The combination of three relatively simple ideas - scaffolded data synthesis (creating problems at the right difficulty level), verifier-guided self-correction (using Lean compiler feedback), and model averaging (to combat diversity collapse) - can enable much smaller models to match/exceed much larger ones.
   
3. **Innovation type**: This is primarily a "combination" innovation - combining existing techniques in a novel way, plus some scaling insights.

4. **Method details**: They use Qwen3-8B and Qwen3-32B as base models, distilled from DeepSeek-Prover variants. The scaffolded data synthesis approach extracts subgoals from failed proofs and generates easier/harder problem variants using LLMs. Self-correction runs for 2 rounds using Lean compiler feedback to extend reasoning from 32K to 40K tokens, and they apply model averaging with a weighted combination to preserve diversity across training.

5. **Results**: The 8B model achieves 84.6% pass@32 on MiniF2F, outperforming the much larger DeepSeek-Prover-V2-671B at 82.4%, while the 32B reaches 88.1% and 90.4% with self-correction. On PutnamBench they solve 86 problems compared to 47 for the larger baseline, and they introduce a new MathOlympiadBench benchmark.

6. This is an arXiv preprint without OpenReview reviews yet, so I'll proceed with analyzing what's presented.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c82f0af-8b19-4490-bf7b-30d01652301f",
  "isSidechain": false,
  "requestId": "req_011CbTMGenwEUXP47xGrYseR",
  "type": "assistant",
  "uuid": "3c8620ba-527c-46db-9bf2-6155d323bd72",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011haWxMaG9UUBEGNx2ZXrwV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8394,
      "cache_read_input_tokens": 36626,
      "output_tokens": 2721,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8394,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2721,
          "cache_read_input_tokens": 36626,
          "cache_creation_input_tokens": 8394,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8394
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

_source line 56 · 2026-05-27T16:00:02.113Z_

Now I have comprehensive coverage of the paper. Let me compile the deep analysis.

```json
{
  "title": "Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction",
  "venue": "arXiv preprint (2508.03613), August 2025 — not yet peer-reviewed at a top venue",
  "problem_identification": "The authors identified that frontier theorem provers (DeepSeek-Prover-V2-671B, Seed-Prover) achieve strong results but depend on massive models or computationally intensive test-time search, making them impractical for community iteration. They pinpointed three specific bottlenecks: (1) existing data synthesis produced low-quality formalizations (>80% of unsolved problems in prior datasets like Goedel-Pset-v1 were incorrectly formalized), (2) whole-proof generation methods were 'end-to-end' and discarded valuable verifier feedback signals, and (3) expert iteration and RL training progressively collapsed output diversity (pass@1 increases but pass@N decreases). Each gap was found through empirical observation during their training pipeline development, not from theoretical analysis.",
  "key_insight": "The core insight is that you can trade model scale for training pipeline sophistication: by generating training problems at the right difficulty level (scaffolding), teaching the model to iteratively repair proofs using compiler feedback (self-correction), and counteracting the diversity collapse inherent in later-stage fine-tuning (model averaging), an 8B model can match a 671B model. The particularly clever move is using failed proof attempts productively — extracting subgoals from incomplete proofs via Lean's `extract_goal` tactic to generate easier related problems, turning failures into training signal.",
  "innovation_type": "combination",
  "method_summary": "Built on Qwen3-8B/32B base models, the pipeline has four stages. Stage S1: distill proofs from DeepSeek-Prover-V2-7B/671B to create initial SFT data. Stage S2: annotate self-correction data by having models attempt proofs, collecting Lean compiler errors, and training the model to revise (2 rounds, expanding context from 32K to 40K tokens). Stage S3: scaffolded data synthesis via two mechanisms — formal-based (using `extract_goal` to capture unsolved subgoals from failed proofs as new easier problems, plus their negations) and informal-based (prompting Qwen3-32B to generate easier sub-problems for unsolved theorems or harder variants of solved ones, then formalizing them). After each SFT stage, model averaging with the base model ((1-α)θ₀ + αθ) restores output diversity. Final RL uses a hybrid GRPO approach (incorporating Dr.GRPO's removal of group normalization, DAPO's dynamic sampling restricted to problems with pass rates in (0, 0.75], and no KL regularization) with 50% whole-proof and 50% self-correction tasks. Model averaging is applied again after RL.",
  "what_makes_it_good": "The paper succeeds because it achieves a dramatic efficiency result (80× smaller model matching SOTA) through a combination of individually well-motivated, cleanly ablatable techniques rather than a single monolithic insight. Each component addresses a specific, empirically identified failure mode — scaffolding addresses data difficulty mismatch, self-correction addresses wasted verifier feedback, model averaging addresses diversity collapse — and the ablations clearly show each contributes (self-correction adds ~2% on MiniF2F, scaffolding enables training on harder problems, model averaging optimizes the pass@1 vs pass@N tradeoff). The work is also extremely well-executed: open-source models, code, data, and a new carefully curated benchmark (MathOlympiadBench) that exposes quality issues in MiniF2F.",
  "limitations_acknowledged": "The authors note that performance remains below expert mathematician level on the hardest problems, and that their approach still requires significant compute for distillation from DeepSeek-Prover-V2-671B. They also flag that inference-time scaling strategies (proof repair via subgoal extraction) show promising 1-2% gains but are not yet fully explored. The self-correction mechanism is limited to 2 rounds with 40K tokens in main experiments.",
  "open_questions": [
    "Can the scaffolded data synthesis loop be made fully autonomous — iteratively generating harder problems as the model improves — creating a self-play curriculum without relying on initial distillation from a much larger teacher model?",
    "The model averaging technique (linear interpolation with base model) is surprisingly effective at restoring diversity but theoretically underspecified — what is it actually doing in the loss landscape, and could more sophisticated merging strategies (e.g., task arithmetic, TIES) do even better?",
    "Self-correction with extended context (128K tokens, 5 rounds) reaches 92.7% on MiniF2F at pass@32, matching pass@8192 without correction — this suggests self-correction is a more sample-efficient form of test-time compute. What is the theoretical relationship between correction rounds and sampling budget, and can this be formalized?"
  ],
  "building_blocks": [
    "Lean 4 compiler as a verifier/reward signal",
    "Lean's `extract_goal` tactic for subgoal extraction from failed proofs",
    "Expert iteration (iterative SFT on model-generated successful proofs)",
    "GRPO with Dr.GRPO and DAPO modifications for RL",
    "Model averaging / weight interpolation with base model for diversity",
    "Qwen3-8B/32B as base models",
    "DeepSeek-Prover-V2-7B/671B for initial distillation",
    "LLM-based formalization pipeline (Claude Sonnet 4 for initial seed, then expert iteration)",
    "LLM-based difficulty scaffolding (Qwen3-32B generates easier/harder problem variants)",
    "YaRN for context window extension to 128K",
    "LLaMA-Factory for SFT training",
    "NeMo-Skills for large-scale inference (144 H100s)",
    "MathOlympiadBench (360 human-verified IMO-level formalizations)",
    "Negation of unproved statements as training data augmentation"
  ],
  "reviewer_feedback_summary": null,
  "relevance_to_seed": "This paper is directly at the heart of bridging informal and formal mathematical reasoning. Its scaffolded data synthesis pipeline — generating informal problem variants with an LLM, formalizing them, then filtering — is essentially an autoformalization system used as a data engine. The self-correction mechanism demonstrates that compiler feedback can be productively integrated into long-CoT generation, offering a template for how verification signals can guide informal-to-formal translation. Most importantly, the paper shows that the autoformalization bottleneck (>80% error rate in prior datasets) can be substantially reduced through expert iteration on the formalizer itself, and that the formal-informal bridge can be crossed bidirectionally (informal→formal for data synthesis, formal→informal via subgoal extraction)."
}
```

---

## Analytical Commentary: What Can We Learn About the *Craft* of This Research?

**1. The "productize failures" principle.** The most intellectually interesting move in this paper is taking *failed proof attempts* and turning them into training data via `extract_goal`. This isn't just recycling — it's recognizing that a wrong proof often contains correct sub-lemmas. This is a generalizable research pattern: when your system fails, ask what partial successes are embedded in the failure.

**2. Combination papers need a unifying diagnosis.** This paper combines three techniques (scaffolding, self-correction, model averaging), which risks feeling like a "bag of tricks." What saves it is that each technique targets a *named, empirically demonstrated failure mode* — data quality, wasted feedback, diversity collapse. The lesson: combination papers succeed when each ingredient solves a specific diagnosed problem, not when they're thrown together hoping for synergy.

**3. The efficiency framing wins.** An 8B model matching a 671B model is a far more compelling narrative than "we improved SOTA by 6%." The paper is structured around this efficiency story, making the contribution feel significant even though the individual techniques are adaptations of known methods.

**4. Infrastructure as contribution.** The MathOlympiadBench benchmark, with its careful documentation of errors in MiniF2F (weakened formalizations, missing conditions, statement mismatches), adds lasting value beyond the model itself. Papers that both advance a metric *and* improve how that metric is measured are harder to dismiss.

**5. Open-source completeness as credibility.** Releasing models, code, training data, and the benchmark makes the claims reproducible and the components reusable — this is increasingly a de facto requirement for ML systems papers to be taken seriously.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c8620ba-527c-46db-9bf2-6155d323bd72",
  "isSidechain": false,
  "requestId": "req_011CbTMGenwEUXP47xGrYseR",
  "type": "assistant",
  "uuid": "d3eaba2d-f2bc-4d5f-af81-f1f287358d84",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011haWxMaG9UUBEGNx2ZXrwV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8394,
      "cache_read_input_tokens": 36626,
      "output_tokens": 2721,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8394,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2721,
          "cache_read_input_tokens": 36626,
          "cache_creation_input_tokens": 8394,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8394
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

_source line 57_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-27 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "d3eaba2d-f2bc-4d5f-af81-f1f287358d84",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc"
}
```

---

### Runtime record

_source line 58_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze Goedel-Prover-V2 paper innovation",
  "sessionId": "6db262d6-dcf8-4dbf-b94b-349936024bbc"
}
```

---
