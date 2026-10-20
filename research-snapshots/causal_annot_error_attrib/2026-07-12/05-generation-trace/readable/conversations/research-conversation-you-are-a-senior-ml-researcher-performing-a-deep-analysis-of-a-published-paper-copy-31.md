# Research conversation: You are a senior ML researcher performing a deep analysis of a published paper. **Today's date: 2026-05-28 (UTC).** ## Y

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 2
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-1/d13ca6d2-ab23-4990-8414-c3096bb93ab5.jsonl`
- **Structured JSON:** [`1ca484383524c38ea59a.json`](../../sessions/1c/1ca484383524c38ea59a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T05:06:07.295Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T05:06:07.295Z",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5",
  "content": "You are a senior ML researcher performing a deep analysis of a published paper.\n\n**Today's date: 2026-05-28 (UTC).**\n\n## Your goal\n\nAnalyze this paper NOT just for what it does, but for **HOW it innovates** — what can we learn from its approach to doing research? What made this paper good enough for a top venue?\n\n## Research context\n\nWe are generating ideas in the area of: **Process Reward Models for Mathematical Reasoning — Step-Level Verification and Credit Assignment**\n\n## Paper to analyze\n\n{\n  \"title\": \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\",\n  \"authors\": \"Zhao et al. (Tsinghua University)\",\n  \"venue\": \"AAAI 2026\",\n  \"url\": \"https://arxiv.org/abs/2504.00891\",\n  \"why_important\": \"AAAI 2026; reframes process verification as a generative CoT task with code verification; 1.5B GenPRM outperforms GPT-4o and 7B GenPRM surpasses Qwen2.5-Math-PRM-72B\",\n  \"one_line_summary\": \"Proposes a generative process reward model that performs explicit chain-of-thought reasoning with code verification before judging each step, enabling dramatic test-time compute scaling.\"\n}\n\n## Instructions\n\n1. **Deep read**: Use WebFetch to read this paper's full abstract, introduction, method section, and conclusion on arXiv or OpenReview. If it's on OpenReview, also read the reviewer comments and author responses.\n\n2. **Analyze the innovation structure**: Don't just summarize — dissect HOW the authors arrived at their contribution:\n   - What gap did they identify and HOW did they find it?\n   - What was the key insight that others missed?\n   - How did they formulate the problem differently from prior work?\n   - What existing technique did they adapt/combine/simplify?\n\n3. **Learn from reviewers**: If you can find reviewer comments, extract:\n   - What did reviewers praise most?\n   - What concerns were raised and how were they addressed?\n   - What would have made this paper even stronger?\n\n## Output format\n\nOutput a single JSON object:\n{\n  \"title\": \"Paper title\",\n  \"venue\": \"Where published\",\n  \"problem_identification\": \"What gap/problem did they identify? How did they find it? (2-3 sentences)\",\n  \"key_insight\": \"The core intellectual contribution — the aha moment (1-2 sentences)\",\n  \"innovation_type\": \"new_formulation | new_technique | new_benchmark | simplification | cross_domain | combination | scaling | analysis\",\n  \"method_summary\": \"Technical approach in 3-5 sentences — enough to understand the machinery\",\n  \"what_makes_it_good\": \"Why did this paper get accepted? What would reviewers have liked? (2-3 sentences)\",\n  \"limitations_acknowledged\": \"What gaps did the authors themselves identify? (1-2 sentences)\",\n  \"open_questions\": \"What follow-up questions does this paper raise? What remains unsolved? (2-3 bullet points)\",\n  \"building_blocks\": [\"List of methods/tools/datasets used that could be reused\"],\n  \"reviewer_feedback_summary\": \"If found on OpenReview: key praise and concerns. Otherwise: null\",\n  \"relevance_to_seed\": \"How does this paper relate to our research area? What can we learn from it? (1-2 sentences)\"\n}\n\nBe analytical, not descriptive. We want to learn the CRAFT of doing good research, not just know what this paper did."
}
```

---

### Runtime record

_source line 2 · 2026-05-28T05:06:07.299Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T05:06:07.299Z",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5"
}
```

---

## Round 1

23 recorded events

### User

_source line 3 · 2026-05-28T05:06:07.337Z_

You are a senior ML researcher performing a deep analysis of a published paper.

**Today's date: 2026-05-28 (UTC).**

## Your goal

Analyze this paper NOT just for what it does, but for **HOW it innovates** — what can we learn from its approach to doing research? What made this paper good enough for a top venue?

## Research context

We are generating ideas in the area of: **Process Reward Models for Mathematical Reasoning — Step-Level Verification and Credit Assignment**

## Paper to analyze

{
  "title": "GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning",
  "authors": "Zhao et al. (Tsinghua University)",
  "venue": "AAAI 2026",
  "url": "https://arxiv.org/abs/2504.00891",
  "why_important": "AAAI 2026; reframes process verification as a generative CoT task with code verification; 1.5B GenPRM outperforms GPT-4o and 7B GenPRM surpasses Qwen2.5-Math-PRM-72B",
  "one_line_summary": "Proposes a generative process reward model that performs explicit chain-of-thought reasoning with code verification before judging each step, enabling dramatic test-time compute scaling."
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
  "promptId": "a37d06a3-a1b2-4f5b-ba56-06aaf32ddf9c",
  "type": "user",
  "uuid": "88253dea-749b-4263-99ce-46e36da98144",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T05:06:07.336Z_

```json
{
  "parentUuid": "88253dea-749b-4263-99ce-46e36da98144",
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
  "uuid": "8b1315c0-954b-49b7-a5c4-2ea4d4960f83",
  "timestamp": "2026-05-28T05:06:07.336Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T05:06:07.336Z_

```json
{
  "parentUuid": "8b1315c0-954b-49b7-a5c4-2ea4d4960f83",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "73e54c4d-f19c-4cfb-9edf-15feed782940",
  "timestamp": "2026-05-28T05:06:07.336Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5",
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
  "aiTitle": "Analyze GenPRM paper innovation and research craft",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5"
}
```

---

### Assistant

_source line 7 · 2026-05-28T05:06:13.679Z_

<details><summary>Logged reasoning block</summary>

```text
Let me fetch the paper from arXiv to get the full details, and also check if it's available on OpenReview for reviewer comments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73e54c4d-f19c-4cfb-9edf-15feed782940",
  "isSidechain": false,
  "requestId": "req_011CbUPJhMm3Tsji48vomqzw",
  "type": "assistant",
  "uuid": "698db627-bd6d-4a8f-bb91-8f9dd7dfce23",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014AyLSyGcHRKeCKoR59cNbH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2217,
      "cache_read_input_tokens": 11014,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2217,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 122,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 2217,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2217
          },
          "type": "message"
        }
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

_source line 8 · 2026-05-28T05:06:13.791Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012aFdKk4oP7TLYPCQTQYjhz`</summary>

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
  "parentUuid": "698db627-bd6d-4a8f-bb91-8f9dd7dfce23",
  "isSidechain": false,
  "requestId": "req_011CbUPJhMm3Tsji48vomqzw",
  "type": "assistant",
  "uuid": "84e16dec-a0be-476f-9429-4192e8e4d307",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014AyLSyGcHRKeCKoR59cNbH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2217,
      "cache_read_input_tokens": 11014,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2217,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 122,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 2217,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2217
          },
          "type": "message"
        }
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

_source line 9 · 2026-05-28T05:06:13.799Z_

<details><summary>↩ Tool result · `toolu_012aFdKk4oP7TLYPCQTQYjhz`</summary>

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
  "parentUuid": "84e16dec-a0be-476f-9429-4192e8e4d307",
  "isSidechain": false,
  "promptId": "a37d06a3-a1b2-4f5b-ba56-06aaf32ddf9c",
  "type": "user",
  "uuid": "111a6e9a-b45f-481d-a3a3-b0d9c0839383",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "84e16dec-a0be-476f-9429-4192e8e4d307",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-28T05:06:17.239Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me fetch the paper from arXiv. I'll fetch both the abstract page and the HTML version for the full paper content, and also check OpenReview for any reviews.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "111a6e9a-b45f-481d-a3a3-b0d9c0839383",
  "isSidechain": false,
  "requestId": "req_011CbUPKBC5W7fiNn34U4Zqa",
  "type": "assistant",
  "uuid": "2b75c05b-e2c9-4be2-baf9-d4480178b434",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KuzsiQFEBo48ZFZiiii3Er",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 642,
      "cache_read_input_tokens": 13231,
      "output_tokens": 331,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 642,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 331,
          "cache_read_input_tokens": 13231,
          "cache_creation_input_tokens": 642,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 642
          },
          "type": "message"
        }
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

_source line 11 · 2026-05-28T05:06:18.742Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NzxrJQ8LXCzvCeL15vVArc`</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.00891",
  "prompt": "Extract the full abstract, author list, and any other metadata available on this page for the paper \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\". Get every detail available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b75c05b-e2c9-4be2-baf9-d4480178b434",
  "isSidechain": false,
  "requestId": "req_011CbUPKBC5W7fiNn34U4Zqa",
  "type": "assistant",
  "uuid": "31246487-ce30-4a04-b509-acb113333635",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KuzsiQFEBo48ZFZiiii3Er",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 642,
      "cache_read_input_tokens": 13231,
      "output_tokens": 331,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 642,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 331,
          "cache_read_input_tokens": 13231,
          "cache_creation_input_tokens": 642,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 642
          },
          "type": "message"
        }
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

_source line 12 · 2026-05-28T05:06:20.878Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017LpxaBgEczcUXTrQqDGmX4`</summary>

```json
{
  "url": "https://arxiv.org/html/2504.00891",
  "prompt": "Extract the FULL content of this paper, focusing on: 1) Introduction (complete), 2) Method section (complete technical details), 3) Experiments and results (key findings, tables, ablations), 4) Related work, 5) Conclusion and limitations. Preserve all technical details, equations, training procedures, dataset descriptions, and architectural choices. Be as thorough as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31246487-ce30-4a04-b509-acb113333635",
  "isSidechain": false,
  "requestId": "req_011CbUPKBC5W7fiNn34U4Zqa",
  "type": "assistant",
  "uuid": "2d62d4a0-3089-4b20-9398-83fa056c696e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KuzsiQFEBo48ZFZiiii3Er",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 642,
      "cache_read_input_tokens": 13231,
      "output_tokens": 331,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 642,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 331,
          "cache_read_input_tokens": 13231,
          "cache_creation_input_tokens": 642,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 642
          },
          "type": "message"
        }
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

_source line 13 · 2026-05-28T05:06:20.890Z_

<details><summary>↩ Tool result · `toolu_017LpxaBgEczcUXTrQqDGmX4`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d62d4a0-3089-4b20-9398-83fa056c696e",
  "isSidechain": false,
  "promptId": "a37d06a3-a1b2-4f5b-ba56-06aaf32ddf9c",
  "type": "user",
  "uuid": "491e7093-d645-401a-bc05-10c254c03902",
  "toolUseResult": {
    "bytes": 0,
    "code": 404,
    "codeText": "Not Found",
    "result": "The server returned HTTP 404 Not Found.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.",
    "durationMs": 10,
    "url": "https://arxiv.org/html/2504.00891"
  },
  "sourceToolAssistantUUID": "2d62d4a0-3089-4b20-9398-83fa056c696e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-28T05:06:24.577Z_

<details><summary>↩ Tool result · `toolu_01NzxrJQ8LXCzvCeL15vVArc`</summary>

```text
# GenPRM Paper Metadata

**Title:** GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning

**ArXiv ID:** 2504.00891

**Category:** Computer Science > Computation and Language (cs.CL)

**Submission Date:** April 1, 2025 (v1); Last revised April 5, 2025 (v2)

## Authors
Jian Zhao, Runze Liu, Kaiyan Zhang, Zhimu Zhou, Junqi Gao, Dong Li, Jiafei Lyu, Zhouyi Qian, Biqing Qi, Xiu Li, Bowen Zhou

## Abstract Summary
The paper introduces GenPRM, a generative process reward model utilizing Chain-of-Thought reasoning with code verification. Key contributions include:

- Addressing three challenges in current Process Reward Models: limited process supervision, scalar value prediction constraints, and inability to scale test-time compute
- Proposing Relative Progress Estimation and a rationale synthesis framework incorporating code verification
- Achieving strong performance on ProcessBench and mathematical reasoning tasks with only 23K training samples
- Demonstrating that smaller GenPRM models outperform significantly larger competitors

**Notable Results:** A 1.5B GenPRM surpasses GPT-4o, while a 7B variant "surpasses Qwen2.5-Math-PRM-72B on ProcessBench"

**DOI:** https://doi.org/10.48550/arXiv.2504.00891

**Availability:** Code, models, and data promised at author's repository
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31246487-ce30-4a04-b509-acb113333635",
  "isSidechain": false,
  "promptId": "a37d06a3-a1b2-4f5b-ba56-06aaf32ddf9c",
  "type": "user",
  "uuid": "63968176-83dd-45a4-b2c6-9082603fcb1a",
  "toolUseResult": {
    "bytes": 47432,
    "code": 200,
    "codeText": "OK",
    "result": "# GenPRM Paper Metadata\n\n**Title:** GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\n\n**ArXiv ID:** 2504.00891\n\n**Category:** Computer Science > Computation and Language (cs.CL)\n\n**Submission Date:** April 1, 2025 (v1); Last revised April 5, 2025 (v2)\n\n## Authors\nJian Zhao, Runze Liu, Kaiyan Zhang, Zhimu Zhou, Junqi Gao, Dong Li, Jiafei Lyu, Zhouyi Qian, Biqing Qi, Xiu Li, Bowen Zhou\n\n## Abstract Summary\nThe paper introduces GenPRM, a generative process reward model utilizing Chain-of-Thought reasoning with code verification. Key contributions include:\n\n- Addressing three challenges in current Process Reward Models: limited process supervision, scalar value prediction constraints, and inability to scale test-time compute\n- Proposing Relative Progress Estimation and a rationale synthesis framework incorporating code verification\n- Achieving strong performance on ProcessBench and mathematical reasoning tasks with only 23K training samples\n- Demonstrating that smaller GenPRM models outperform significantly larger competitors\n\n**Notable Results:** A 1.5B GenPRM surpasses GPT-4o, while a 7B variant \"surpasses Qwen2.5-Math-PRM-72B on ProcessBench\"\n\n**DOI:** https://doi.org/10.48550/arXiv.2504.00891\n\n**Availability:** Code, models, and data promised at author's repository",
    "durationMs": 5829,
    "url": "https://arxiv.org/abs/2504.00891"
  },
  "sourceToolAssistantUUID": "31246487-ce30-4a04-b509-acb113333635",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-28T05:06:27.576Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QDWZbBZ5h8RERt72rtiNzE`</summary>

```json
{
  "url": "https://arxiv.org/html/2504.00891v2",
  "prompt": "Extract the FULL content of this paper, focusing on: 1) Introduction (complete), 2) Method section (complete technical details), 3) Experiments and results (key findings, tables, ablations), 4) Related work, 5) Conclusion and limitations. Preserve all technical details, equations, training procedures, dataset descriptions, and architectural choices. Be as thorough as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63968176-83dd-45a4-b2c6-9082603fcb1a",
  "isSidechain": false,
  "requestId": "req_011CbUPKxwQt4j2rKtxGnwWq",
  "type": "assistant",
  "uuid": "b0075e86-4df5-45ba-848e-b1546378121f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EXDVfJk42RzAsC3q8R6rhx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 742,
      "cache_read_input_tokens": 13873,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 742,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 85,
          "output_tokens": 326,
          "cache_read_input_tokens": 13873,
          "cache_creation_input_tokens": 742,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 742
          },
          "type": "message"
        }
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

_source line 16 · 2026-05-28T05:06:27.594Z_

<details><summary>↩ Tool result · `toolu_01QDWZbBZ5h8RERt72rtiNzE`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0075e86-4df5-45ba-848e-b1546378121f",
  "isSidechain": false,
  "promptId": "a37d06a3-a1b2-4f5b-ba56-06aaf32ddf9c",
  "type": "user",
  "uuid": "d4389fb7-eba7-4c2d-b457-ace92dc5326e",
  "toolUseResult": {
    "bytes": 0,
    "code": 404,
    "codeText": "Not Found",
    "result": "The server returned HTTP 404 Not Found.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.",
    "durationMs": 13,
    "url": "https://arxiv.org/html/2504.00891v2"
  },
  "sourceToolAssistantUUID": "b0075e86-4df5-45ba-848e-b1546378121f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-28T05:06:29.957Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SyJD7Lxuk8hdq9Mi5sLCLn`</summary>

```json
{
  "url": "https://openreview.net/search?term=GenPRM+Scaling+Test-Time+Compute+Process+Reward+Models+Generative+Reasoning&venue=AAAI.org/2026",
  "prompt": "Find the OpenReview page for the paper \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\". Extract any reviewer comments, scores, and author responses if available. Also extract the direct URL to the paper's review page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4389fb7-eba7-4c2d-b457-ace92dc5326e",
  "isSidechain": false,
  "requestId": "req_011CbUPKxwQt4j2rKtxGnwWq",
  "type": "assistant",
  "uuid": "a3bd1c4b-09ec-4d2c-b69f-b12f2aa6aba2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EXDVfJk42RzAsC3q8R6rhx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 742,
      "cache_read_input_tokens": 13873,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 742,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 85,
          "output_tokens": 326,
          "cache_read_input_tokens": 13873,
          "cache_creation_input_tokens": 742,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 742
          },
          "type": "message"
        }
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

_source line 18 · 2026-05-28T05:06:32.503Z_

<details><summary>↩ Tool result · `toolu_01SyJD7Lxuk8hdq9Mi5sLCLn`</summary>

```text
I apologize, but I cannot complete this request based on the provided content. The webpage excerpt you've shared only contains OpenReview's navigation menu, footer information, and general site descriptions. It does not include:

- Any specific paper titled "GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning"
- Reviewer comments or scores
- Author responses
- A direct URL to that paper's review page

To find this information, you would need to:

1. Visit OpenReview.net directly
2. Use their search function to locate the specific paper
3. Navigate to the paper's review page, where reviewer comments and scores would be displayed

I can only extract and summarize information present in the content provided to me.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3bd1c4b-09ec-4d2c-b69f-b12f2aa6aba2",
  "isSidechain": false,
  "promptId": "a37d06a3-a1b2-4f5b-ba56-06aaf32ddf9c",
  "type": "user",
  "uuid": "3e145ee8-0bb8-4aa8-af83-08cbaf24ce97",
  "toolUseResult": {
    "bytes": 62532,
    "code": 200,
    "codeText": "OK",
    "result": "I apologize, but I cannot complete this request based on the provided content. The webpage excerpt you've shared only contains OpenReview's navigation menu, footer information, and general site descriptions. It does not include:\n\n- Any specific paper titled \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\"\n- Reviewer comments or scores\n- Author responses\n- A direct URL to that paper's review page\n\nTo find this information, you would need to:\n\n1. Visit OpenReview.net directly\n2. Use their search function to locate the specific paper\n3. Navigate to the paper's review page, where reviewer comments and scores would be displayed\n\nI can only extract and summarize information present in the content provided to me.",
    "durationMs": 2544,
    "url": "https://openreview.net/search?term=GenPRM+Scaling+Test-Time+Compute+Process+Reward+Models+Generative+Reasoning&venue=AAAI.org/2026"
  },
  "sourceToolAssistantUUID": "a3bd1c4b-09ec-4d2c-b69f-b12f2aa6aba2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-28T05:06:37.285Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TNT3W7fxePzYRfswA95hy8`</summary>

```json
{
  "url": "https://www.arxiv.org/pdf/2504.00891",
  "prompt": "Extract the FULL content of this paper, focusing on ALL of the following sections with maximum detail: 1) Introduction - full text, all cited problems, motivation, contributions list. 2) Method/Approach section - complete technical details including Relative Progress Estimation, rationale synthesis framework, code verification, training procedure, data generation pipeline. 3) Experiments - all benchmarks, baselines, main results tables, ablation studies. 4) Related Work. 5) Conclusion and Limitations. Preserve equations, algorithm descriptions, dataset sizes, model architectures, and all quantitative results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e145ee8-0bb8-4aa8-af83-08cbaf24ce97",
  "isSidechain": false,
  "requestId": "req_011CbUPLZ9xMJ93U3d6Ec9fB",
  "type": "assistant",
  "uuid": "0bc9aa69-3533-477e-8135-b1b1a486017b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TF626QT2hhR6Hf2r7Ts3uy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 690,
      "cache_read_input_tokens": 14615,
      "output_tokens": 210,
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
          "output_tokens": 210,
          "cache_read_input_tokens": 14615,
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

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-28 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "0bc9aa69-3533-477e-8135-b1b1a486017b",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze GenPRM paper innovation and research craft",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5"
}
```

---

### Tool result

_source line 22 · 2026-05-28T05:06:44.643Z_

<details><summary>↩ Tool result · `toolu_01TNT3W7fxePzYRfswA95hy8`</summary>

```text
I appreciate you sharing this content, but I need to clarify what I'm seeing: the provided material appears to be raw PDF object stream data (encoded/compressed PDF internals) rather than readable paper text.

The content shows PDF metadata and embedded compressed streams (objects 109-293) but lacks the actual extracted, human-readable text of the paper sections you've requested.

**To help effectively, I would need:**

1. **Plain text or readable PDF** - The paper content in a format I can parse (not compressed PDF streams)
2. **Confirmation of the paper title** - To ensure I'm addressing the correct work
3. **Specific sections** - If you have particular areas of interest beyond the full extraction request

**What I can offer instead:**

- If you can provide the paper in readable format, I'll extract:
  - Full Introduction (contributions, motivation, problems addressed)
  - Complete Method section (technical approach, algorithms, data pipelines)
  - Experiments (benchmarks, results tables, ablation studies)
  - Related Work and Conclusion
  - All equations and quantitative findings

- I'll maintain the 125-character quote limit and proper attribution
- I'll avoid reproducing copyrighted material while preserving essential technical content

**Please share:** A readable version of the paper (PDF text layer, markdown export, or plain text), and I'll provide comprehensive extraction following your guidelines.

[Binary content (application/pdf, 1.3MB) also saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/d13ca6d2-ab23-4990-8414-c3096bb93ab5/tool-results/webfetch-1779944797543-vsae79.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0bc9aa69-3533-477e-8135-b1b1a486017b",
  "isSidechain": false,
  "promptId": "a37d06a3-a1b2-4f5b-ba56-06aaf32ddf9c",
  "type": "user",
  "uuid": "72223c8d-4dd0-4bc3-9e05-d12451cec0a8",
  "toolUseResult": {
    "bytes": 1397815,
    "code": 200,
    "codeText": "OK",
    "result": "I appreciate you sharing this content, but I need to clarify what I'm seeing: the provided material appears to be raw PDF object stream data (encoded/compressed PDF internals) rather than readable paper text.\n\nThe content shows PDF metadata and embedded compressed streams (objects 109-293) but lacks the actual extracted, human-readable text of the paper sections you've requested.\n\n**To help effectively, I would need:**\n\n1. **Plain text or readable PDF** - The paper content in a format I can parse (not compressed PDF streams)\n2. **Confirmation of the paper title** - To ensure I'm addressing the correct work\n3. **Specific sections** - If you have particular areas of interest beyond the full extraction request\n\n**What I can offer instead:**\n\n- If you can provide the paper in readable format, I'll extract:\n  - Full Introduction (contributions, motivation, problems addressed)\n  - Complete Method section (technical approach, algorithms, data pipelines)\n  - Experiments (benchmarks, results tables, ablation studies)\n  - Related Work and Conclusion\n  - All equations and quantitative findings\n\n- I'll maintain the 125-character quote limit and proper attribution\n- I'll avoid reproducing copyrighted material while preserving essential technical content\n\n**Please share:** A readable version of the paper (PDF text layer, markdown export, or plain text), and I'll provide comprehensive extraction following your guidelines.\n\n[Binary content (application/pdf, 1.3MB) also saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/d13ca6d2-ab23-4990-8414-c3096bb93ab5/tool-results/webfetch-1779944797543-vsae79.pdf]",
    "durationMs": 7354,
    "url": "https://www.arxiv.org/pdf/2504.00891"
  },
  "sourceToolAssistantUUID": "0bc9aa69-3533-477e-8135-b1b1a486017b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-28T05:06:47.395Z_

<details><summary>Logged reasoning block</summary>

```text
Let me try to read the downloaded PDF file, and also try fetching via the Hugging Face papers page or other sources.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72223c8d-4dd0-4bc3-9e05-d12451cec0a8",
  "isSidechain": false,
  "requestId": "req_011CbUPMSiHWvTgqSSUtdUA3",
  "type": "assistant",
  "uuid": "96d13348-745a-42b3-a61c-af4fb7a823ef",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0122oTxTyrv1ydvHgJ27Pk4F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 611,
      "cache_read_input_tokens": 15305,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 611,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 293,
          "cache_read_input_tokens": 15305,
          "cache_creation_input_tokens": 611,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 611
          },
          "type": "message"
        }
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

_source line 24 · 2026-05-28T05:06:48.363Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Wrq8fBv83x5fuXVLdfj8Yw`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/d13ca6d2-ab23-4990-8414-c3096bb93ab5/tool-results/webfetch-1779944797543-vsae79.pdf",
  "pages": "1-5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96d13348-745a-42b3-a61c-af4fb7a823ef",
  "isSidechain": false,
  "requestId": "req_011CbUPMSiHWvTgqSSUtdUA3",
  "type": "assistant",
  "uuid": "c73873d0-f0ac-4df3-9700-871a4416d56a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0122oTxTyrv1ydvHgJ27Pk4F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 611,
      "cache_read_input_tokens": 15305,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 611,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 293,
          "cache_read_input_tokens": 15305,
          "cache_creation_input_tokens": 611,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 611
          },
          "type": "message"
        }
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

_source line 25 · 2026-05-28T05:06:48.968Z_

<details><summary>↩ Tool result · `toolu_01Wrq8fBv83x5fuXVLdfj8Yw`</summary>

```text
PDF pages extracted: 5 page(s) from /home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/d13ca6d2-ab23-4990-8414-c3096bb93ab5/tool-results/webfetch-1779944797543-vsae79.pdf (1.3MB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c73873d0-f0ac-4df3-9700-871a4416d56a",
  "isSidechain": false,
  "promptId": "a37d06a3-a1b2-4f5b-ba56-06aaf32ddf9c",
  "type": "user",
  "uuid": "c54f1cd7-6405-4d59-98bc-3fe2cddc3002",
  "toolUseResult": {
    "type": "parts",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/d13ca6d2-ab23-4990-8414-c3096bb93ab5/tool-results/webfetch-1779944797543-vsae79.pdf",
      "originalSize": 1397815,
      "outputDir": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/d13ca6d2-ab23-4990-8414-c3096bb93ab5/tool-results/pdf-3a006ca8-ae95-4b08-a0f1-02061bfa01ba",
      "count": 5
    }
  },
  "sourceToolAssistantUUID": "c73873d0-f0ac-4df3-9700-871a4416d56a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

## Round 2

22 recorded events

### User

_source line 26 · 2026-05-28T05:06:48.966Z_

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
  "parentUuid": "c54f1cd7-6405-4d59-98bc-3fe2cddc3002",
  "isSidechain": false,
  "promptId": "a37d06a3-a1b2-4f5b-ba56-06aaf32ddf9c",
  "type": "user",
  "isMeta": true,
  "uuid": "6a64b3bd-6a3b-47d9-9c9d-a03488088597",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-28T05:06:49.736Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GSHgkEVx98FPEy2wEtpX5x`</summary>

```json
{
  "url": "https://huggingface.co/papers/2504.00891",
  "prompt": "Extract ALL available information about this paper \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\". Get the full abstract, any summary, discussion comments, and all details available on this page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a64b3bd-6a3b-47d9-9c9d-a03488088597",
  "isSidechain": false,
  "requestId": "req_011CbUPMSiHWvTgqSSUtdUA3",
  "type": "assistant",
  "uuid": "1891e816-1b5c-482e-a265-1ee101444438",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0122oTxTyrv1ydvHgJ27Pk4F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 611,
      "cache_read_input_tokens": 15305,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 611,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 293,
          "cache_read_input_tokens": 15305,
          "cache_creation_input_tokens": 611,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 611
          },
          "type": "message"
        }
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

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-28 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "1891e816-1b5c-482e-a265-1ee101444438",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze GenPRM paper innovation and research craft",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5"
}
```

---

### Tool result

_source line 30 · 2026-05-28T05:06:50.669Z_

<details><summary>↩ Tool result · `toolu_01GSHgkEVx98FPEy2wEtpX5x`</summary>

```text
&lt;persisted-output>
Output too large (87.1KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/d13ca6d2-ab23-4990-8414-c3096bb93ab5/tool-results/toolu_01GSHgkEVx98FPEy2wEtpX5x.txt

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
  "parentUuid": "1891e816-1b5c-482e-a265-1ee101444438",
  "isSidechain": false,
  "promptId": "a37d06a3-a1b2-4f5b-ba56-06aaf32ddf9c",
  "type": "user",
  "uuid": "68422d5f-eb09-4767-9d08-aa2b8857f6e5",
  "toolUseResult": {
    "bytes": 89347,
    "code": 200,
    "codeText": "OK",
    "result": "# GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\n\nJian Zhao&lt;sup>1,3\\*&lt;/sup>, Runze Liu&lt;sup>1,2\\*†&lt;/sup>, Kaiyan Zhang&lt;sup>1&lt;/sup>, Zhimu Zhou&lt;sup>3&lt;/sup>, Junqi Gao&lt;sup>4&lt;/sup>, Dong Li&lt;sup>4&lt;/sup>, Jiafei Lyu&lt;sup>1&lt;/sup>, Zhouyi Qian&lt;sup>4&lt;/sup>, Biqing Qi&lt;sup>2‡&lt;/sup>, Xiu Li&lt;sup>1‡&lt;/sup> and Bowen Zhou&lt;sup>1,2‡&lt;/sup>\n\n&lt;sup>1&lt;/sup>Tsinghua University, &lt;sup>2&lt;/sup>Shanghai AI Laboratory, &lt;sup>3&lt;/sup>BUPT, &lt;sup>4&lt;/sup>Harbin Institute of Technology\n\nRecent advancements in Large Language Models (LLMs) have shown that it is promising to utilize Process Reward Models (PRMs) as verifiers to enhance the performance of LLMs. However, current PRMs face three key challenges: (1) limited process supervision and generalization capabilities, (2) dependence on scalar value prediction without leveraging the generative abilities of LLMs, and (3) inability to scale the test-time compute of PRMs. In this work, we introduce GenPRM, a generative process reward model that performs explicit Chain-of-Thought (CoT) reasoning with code verification before providing judgment for each reasoning step. To obtain high-quality process supervision labels and rationale data, we propose Relative Progress Estimation (RPE) and a rationale synthesis framework that incorporates code verification. Experimental results on ProcessBench and several mathematical reasoning tasks show that GenPRM significantly outperforms prior PRMs with only **23K** training data from **MATH** dataset. Through test-time scaling, a **1.5B** GenPRM outperforms **GPT-4o**, and a **7B** GenPRM surpasses **Qwen2.5-Math-PRM-72B** on ProcessBench. Additionally, GenPRM demonstrates strong abilities to serve as a critic model for policy model refinement. This work establishes a new paradigm for process supervision that bridges the gap between PRMs and critic models in LLMs. Our code, model, and data are available in &lt;https://ryanliu112.github.io/GenPRM>.\n\n**Figure 1: GenPRM achieves state-of-the-art performance across multiple benchmarks in two key roles: (a) As a verifier:** GenPRM-7B outperforms all classification-based PRMs of comparable size and even surpasses **Qwen2.5-Math-PRM-72B** via test-time scaling. **(b) As a critic:** GenPRM-7B demonstrates superior critique capabilities, achieving **3.4x** greater performance gains than DeepSeek-R1-Distill-Qwen-7B after 3 refinement iterations.\n\n\\* Equal contribution\n\n† Project lead & Work done during an internship at Shanghai AI Laboratory\n\n‡ Corresponding authors: Biqing Qi (qibiqing@pjlab.org.cn), Xiu Li (li.xiu@sz.tsinghua.edu.cn), and Bowen Zhou (zhoubowen@tsinghua.edu.cn)The diagram illustrates the architectural differences between classification-based PRMs and GenPRM. On the left, under the heading 'Classification-based PRM', two models are shown: 'Discriminative PRM' and 'Direct Generative PRM'. The Discriminative PRM consists of a 'value head' that outputs a score of 0.9, marked with a green checkmark. The Direct Generative PRM outputs a 'Yes' label, which is then converted to a score of 0.8, also marked with a green checkmark. On the right, under the heading 'Generative PRM (Ours)', the 'GenPRM' model is shown. It branches into three parallel paths, each consisting of a yellow circle (CoT Verification) followed by a green circle (Code Verification) and a 'Yes' or 'No' label. The top path outputs 'Yes', the middle path outputs 'No', and the bottom path outputs 'No'. These three paths converge into a final score of 0.2, which is marked with a red 'X'. A legend at the bottom identifies the yellow circle as 'CoT Verification' and the green circle as 'Code Verification'.\n\nFigure 2: Comparison between GenPRM (right) and previous classification-based PRMs (left).\n\n## 1. Introduction\n\nLarge Language Models (LLMs) have shown significant advances in recent years (OpenAI, 2023; Anthropic, 2023; OpenAI, 2024a,b; DeepSeek-AI et al., 2025). As OpenAI o1 demonstrates the great effectiveness of scaling test-time compute (OpenAI, 2024a), an increasing number of researches focus on Test-Time Scaling (TTS) methods to improve the reasoning performance of LLMs (Snell et al., 2025; Liu et al., 2025).\n\nEffective TTS requires high-quality verifiers, such as Process Reward Models (PRMs) (Liu et al., 2025). However, existing PRMs face several limitations. They exhibit limited process supervision capabilities and struggle to generalize across different models and tasks (Zheng et al., 2024; Zhang et al., 2025c; Liu et al., 2025). Furthermore, most current approaches train PRMs as classifiers that output scalar values, neglecting the natural language generation abilities of LLMs, which are pre-trained on extensive corpora. This classifier-based modeling inherently prevents PRMs from leveraging test-time scaling methods to enhance process supervision capabilities. These limitations lead us to the following research question: *How can generative modeling enhance the process supervision capabilities of PRMs while enabling test-time scaling?*\n\nIn this work, we address these challenges through a generative process reward model, named GenPRM. Specifically, GenPRM differs from classification-based PRMs in that GenPRM redefines process supervision as a generative task rather than a discriminative scoring task by integrating Chain-of-Thought (CoT) (Wei et al., 2022) reasoning and code verification processes before providing final judgment. To improve conventional hard label estimation, we propose Relative Progress Estimation (RPE), which leverages a relative criterion for label estimation. Additionally, we introduce a rationale synthesis framework with code verification to obtain high-quality process supervision reasoning data. A comparison of our method with previous classification-based methods is presented in Figure 2.\n\nOur contributions can be summarized as follows:\n\n1. 1. We propose a generative process reward model that performs explicit CoT reasoning with code verification and utilizes Relative Progress Estimation to obtain accurate PRM labels.\n2. 2. Empirical results on ProcessBench and common mathematical reasoning tasks demonstrate that GenPRM outperforms prior classification-based PRMs. Additionally, smaller GenPRM models can surpass larger PRMs via TTS.\n3. 3. We provide a new perspective on PRMs in this work, fully leveraging their TTS capabilities, reshaping their applications, and opening new directions for future research in process supervision.## 2. Preliminaries\n\n### 2.1. Markov Decision Process\n\nFollowing [Liu et al. \\(2025\\)](#), we formulate the test-time scaling process with PRMs as a Markov Decision Process (MDP) defined by  $(\\mathcal{S}, \\mathcal{A}, P, r, \\gamma)$ , where  $\\mathcal{S}$  is the state space,  $\\mathcal{A}$  is the action space,  $P$  represents transition dynamics,  $r : \\mathcal{S} \\times \\mathcal{A} \\rightarrow \\mathbb{R}$  is the reward function, and  $\\gamma \\in [0, 1]$  is the discount factor. Starting with a prompt set  $\\mathcal{X}$  and an initial state  $s_1 = x \\sim \\mathcal{X}$ , the policy model  $\\pi_\\theta$  generates an action  $a_1 \\sim \\pi_\\theta(\\cdot | s_1)$ .&lt;sup>1&lt;/sup> Unlike traditional RL methods with stochastic transitions ([Liu et al., 2022, 2024](#)), transitions in LLMs are deterministic, i.e.,  $s_{t+1} = P(\\cdot | s_t, a_t) = [s_t, a_t]$ , where  $[\\cdot, \\cdot]$  denotes string concatenation. This process continues until the episode terminates (i.e., generating the [EOS] token), obtaining a trajectory of  $T$  steps:  $\\tau = \\{a_1, a_2, \\dots, a_T\\}$ . The goal is to optimize either the reward of each step (as in search-based methods) or the reward over the full response (as in Best-of-N sampling).\n\n### 2.2. Supervised Fine-Tuning\n\nSupervised Fine-Tuning (SFT) trains a model to predict the next token based on prior context. For a dataset  $\\mathcal{D}_{\\text{SFT}} = \\{(x^{(i)}, y^{(i)})\\}_{i=1}^N$ , the SFT loss is:\n\n$$\\mathcal{L}_{\\text{SFT}}(\\theta) = -\\mathbb{E}_{(x,y) \\sim \\mathcal{D}_{\\text{SFT}}} \\left[ \\sum_{t=1}^{|y|} \\log \\pi_\\theta(y_t | x, y_{1:t-1}) \\right], \\quad (1)$$\n\nwhere  $\\pi_\\theta$  represents a model with parameters  $\\theta$ .\n\n### 2.3. Test-Time Scaling\n\nIn this work, we consider two test-time scaling methods, including majority voting and Best-of-N.\n\n**Majority Voting.** Majority voting ([Wang et al., 2023](#)) selects the answer that appears the most frequently among all solutions.\n\n**Best-of-N.** Best-of-N (BoN) ([Brown et al., 2024](#); [Snell et al., 2025](#)) selects the best answer from  $N$  candidate solutions.\n\n## 3. Method\n\nIn this section, we first describe how to develop GenPRM and integrate the reasoning process with code verification. We then introduce how to scale test-time compute of policy models using GenPRM and apply TTS for GenPRM. Last, we present the improved label estimation method and data generation and filtering framework of GenPRM.\n\n### 3.1. GenPRM and Test-Time Scaling\n\n#### 3.1.1. From Discriminative PRM to Generative PRM\n\n**Discriminative PRM.** Assume we have a PRM dataset  $\\mathcal{D}_{\\text{Disc}} = \\{(s_t, a_t), r_t\\}$ , where  $r_t \\in \\{0, 1\\}$  for PRM labels with hard estimation. The discriminative PRM  $r_\\psi$  is trained via cross-entropy loss ([Skywork](#)\n\n&lt;sup>1&lt;/sup>Following [Snell et al. \\(2025\\)](#); [Liu et al. \\(2025\\)](#), we refer to models that generate solutions as policy models.The diagram illustrates the GenPRM framework, which consists of six key parts:\n\n- **① Solution Generation & MC Reward Estimation:** A math problem is solved by generating intermediate steps (a&lt;sub>11&lt;/sub>, a&lt;sub>21&lt;/sub>, a&lt;sub>31&lt;/sub>, a&lt;sub>12&lt;/sub>, a&lt;sub>22&lt;/sub>, a&lt;sub>32&lt;/sub>). Correct steps (q&lt;sub>1&lt;/sub>, q&lt;sub>2&lt;/sub>) are marked with blue circles, and incorrect steps (q&lt;sub>3&lt;/sub>) are marked with red circles. The MC score for a step is calculated as  $MC(s_{12}, a_{12}) = \\frac{2}{3}$ .\n- **② Relative Progress Estimation:** The process reward is estimated as  $P_t = \\frac{MC(s_t, a_t)}{MC(s_t)} \\geq \\epsilon$ . If the reward is high,  $\\hat{r}_t = 1$  (green checkmark), otherwise  $\\hat{r}_t = 0$  (red X).\n- **③ Rationale Synthesis:** A problem is analyzed using CoT (Chain of Thought) analysis to generate a rationale. This rationale is then verified using code verification (e.g., Python code) to check for potential errors. The final label is a judgement of Yes/No.\n- **④ GenPRM Training:** Data (23K) is used for SFT (Supervised Fine-Tuning) to train GenPRM. Consensus filtering is applied to the training data.\n- **⑤ Policy Model Test-Time Scaling:** The trained GenPRM functions as a verifier or critic. It can be used to verify a solution (GenPRM as a Verifier) or critique a solution (GenPRM as a Critic).\n- **⑥ GenPRM Test-Time Scaling:** The performance of GenPRM is improved through test-time scaling. Multiple steps are analyzed and verified, and their rewards are aggregated to produce a final reward  $r$ .\n\nLegend:\n\n- a Intermediate Step\n- q Correct Answer\n- q Incorrect Answer\n- r Single Reward Judgement\n- r Aggregated Reward Judgement\n\n**Figure 3: Overall framework of GenPRM.** Our framework consists of six key parts: ① The policy model generates solution steps, with MC scores estimated from rollout trajectories. ② Our proposed RPE derives accurate PRM labels. ③ High-quality process supervision data is synthesized through CoT reasoning augmented with code verification. ④ We apply consensus filtering followed by SFT to train GenPRM. ⑤ The trained GenPRM functions as a verifier or critic, enabling enhanced test-time scaling for policy models. ⑥ The performance of GenPRM further improves through test-time scaling.\n\no1 Team, 2024; Zhang et al., 2025c):\n\n$$\\mathcal{L}_{CE}(\\psi) = -\\mathbb{E}_{(s_t, a_t, r_t) \\sim \\mathcal{D}_{Disc}} [r_t \\log r_\\psi(s_t, a_t) + (1 - r_t) \\log(1 - r_\\psi(s_t, a_t))]. \\quad (2)$$\n\n**Direct Generative PRM.** With a dataset  $\\mathcal{D}_{Direct-Gen} = \\{(s_t, a_t), r_t\\}$ , where  $r_t$  is Yes for a correct step and No otherwise, the direct generative PRM (Xiong et al., 2024) is trained through SFT to predict Yes or No for each step. For step  $t$ , we use the probability of the Yes token as the predicted process reward  $\\hat{r}_t$ :\n\n$$\\hat{r}_t = r_\\psi(\\text{Yes} \\mid s_t, a_t). \\quad (3)$$\n\n**Generative PRM.** By equipping the direct generative PRM with an explicit reasoning process like CoT (Wei et al., 2022), we obtain a generative PRM. Let  $v_{1:t-1}$  denote the rationale from step 1 to  $t-1$  and  $v_t$  denote the rationale for step  $t$ . Assume we have a dataset  $\\mathcal{D}_{Gen} = \\{(s_t, a_t, v_{1:t-1}), (v_t, r_t)\\}$ . GenPRM learns to reason and verify each step via SFT on this dataset. The generative process reward  $\\hat{r}_t$  can be obtained via the following equation:\n\n$$\\hat{r}_t = r_\\psi(\\text{Yes} \\mid s_t, a_t, v_{1:t-1}, v_t), \\quad \\text{where } v_t \\sim r_\\psi(\\cdot \\mid s_t, a_t, v_{1:t-1}) \\quad (4)$$\n\n**Generative PRM with Code Verification.** If we only verify the reasoning step with CoT based on natural language, the process may lack robustness in certain complex scenarios (Zhu et al., 2024; Gou et al., 2024). The difference between the generative PRM and the generative PRM with code verification is that the latter generates code to verify the reasoning step by executing it and provides the judgment based on the execution results. At step  $t$ , after generating the rationale  $v_t$  containing CoT and code, we execute the code and obtain feedback  $f_t$ . Given the current state  $s_t$ , action  $a_t$ , previous rationales  $v_{1:t-1}$ , and previous corresponding execution feedback  $f_{1:t-1}$ , the PRM first generates therationale  $v_t$ . After execution and obtaining the feedback  $f_t$ , we compute the final generative process reward as follows:\n\n$$\\hat{r}_t = r_\\psi(\\text{Yes} \\mid s_t, a_t, v_{1:t-1}, f_{1:t-1}, v_t, f_t), \\quad \\text{where } v_t \\sim r_\\psi(\\cdot \\mid s_t, a_t, v_{1:t-1}, f_{1:t-1}) \\quad (5)$$\n\nIn the following sections, we refer to GenPRM as this generative PRM type with code verification. The effectiveness of CoT and code verification can be found in Section 4.4.\n\n### 3.1.2. Test-Time Scaling\n\n**Policy Model TTS: GenPRM as a Verifier.** To scale the test-time compute of policy models, we can sample multiple responses from policy models and then use GenPRM as a verifier to select the final answer (Snell et al., 2025) in the way of parallel TTS.\n\n**Policy Model TTS: GenPRM as a Critic.** By equipping the PRM with generative process supervision abilities, GenPRM can be naturally used as a critic model to refine the outputs of policy models and we can scale the refinement process with multiple turns in a sequential TTS manner.\n\n**GenPRM TTS.** When evaluating each solution step, we first sample  $N$  reasoning verification paths and then use majority voting to obtain the final prediction by averaging the rewards. For GenPRM without code verification, the rewards are computed as follows:\n\n$$\\hat{r}_t = \\frac{1}{N} \\sum_{i=1}^N r_\\psi(\\text{Yes} \\mid s_t, a_t, v_{1:t-1}^i, v_t^i). \\quad (6)$$\n\nAnd we can further incorporate code verification and execution feedback into this reasoning process:\n\n$$\\hat{r}_t = \\frac{1}{N} \\sum_{i=1}^N r_\\psi(\\text{Yes} \\mid s_t, a_t, v_{1:t-1}^i, f_{1:t-1}^i, v_t^i, f_t^i). \\quad (7)$$\n\nThen the rewards can be used for ranking the responses of policy models or be converted into binary labels through a threshold 0.5 for judging the correctness of the step. The discussion of using code verification can be found at Table 5.\n\n## 3.2. Synthesizing Data of GenPRM\n\nIn this section, we introduce our pipeline for synthesizing training data of GenPRM. The pipeline consists of three stages: (1) generating reasoning paths and obtaining PRM labels via Monte Carlo (MC) estimation; (2) evaluating the progress of each step via Relative Progress Estimation; and (3) synthesizing rationales with CoT and code verification, and inferring LLM-as-a-judge labels with consensus filtering.\n\n### 3.2.1. Solution Generation and Monte Carlo Estimation\n\n**Solution Generation with Step Forcing.** We utilize the 7.5K problems from the training set of the MATH dataset (Hendrycks et al., 2021) as the problem set. For each problem, we use Qwen2.5-7B-Instruct (Yang et al., 2024a) as the generation model to collect multiple solutions. Since using “\\n\\n” for step division does not consider the semantics of each step and may result in overly fine-grained division, we apply a step forcing approach to generate solutions. Specifically, we add “Step 1:” as the prefix for the generation model to complete the response. For a response with  $T$  reasoning steps, the format is as follows:### The response format with step forcing\n\nStep 1: {step content}\n\n...\n\nStep T: {step content}\n\nThe proportion of correct paths versus incorrect paths varies significantly depending on the difficulty of the problems. To ensure a sufficient number of correct and incorrect paths, we sample up to 2048 paths for both hard and easy problems. If no correct or incorrect paths are found after sampling 2048 responses, we discard the corresponding problems.\n\n**Balancing the Precision and Efficiency of MC Estimation.** Following Math-Shepherd (Wang et al., 2024b), we estimate the probability of correctness for each step using completion-based sampling. For each reasoning step  $s_t$ , we generate  $K$  completion trajectories using a completion model, specifically Qwen2.5-Math-7B-Instruct (Yang et al., 2024b), and use MC estimation to calculate the probability that the current step  $a_t$  is correct (Wang et al., 2024b; Zhang et al., 2025c):\n\n$$MC(s_t, a_t) = MC(s_{t+1}) = \\frac{1}{K} \\sum_{j=1}^K \\mathbb{1}(q_j = q^*), \\quad (8)$$\n\nwhere  $q_j$  is the answer of the  $j$ -th response,  $q^*$  is the ground-truth answer, and  $\\mathbb{1}$  is the indicator function. However, it is difficult for the completion model to reach the correct answer for hard problems even when the original step is correct, leading to incorrect results for MC estimation. To address this and balance the computation cost, we use a dynamic  $K$  based on the estimated Pass@1  $MC(s_1)$ :\n\n$$K = \\begin{cases} 128 & \\text{if } 0 \\leq MC(s_1) < 0.1, \\\\ 64 & \\text{if } 0.1 \\leq MC(s_1) < 0.9, \\\\ 32 & \\text{if } 0.9 \\leq MC(s_1) < 1. \\end{cases} \\quad (9)$$\n\n### 3.2.2. Relative Progress Estimation\n\nPrevious work has shown that hard label estimation is better than soft label estimation for PRMs (Zhang et al., 2025c). However, after MC estimation, we observe that although the MC score of many steps is greater than 0, the steps are incorrect, as also noted by Zhang et al. (2025c). On the other hand, we assume that a positive step should be both correct and beneficial. A reasoning step is considered as a beneficial one if it is easier to reach the correct answer by adding this step as the generation prefix. To address these issues, we propose Relative Progress Estimation (RPE), which shares a similar idea with relative advantage estimation in GRPO (Shao et al., 2024; DeepSeek-AI et al., 2025), to improve conventional hard label estimation.\n\nSpecifically, the MC score is an empirical estimation of the current state  $s_t$ . To evaluate the quality of the current action  $a_t$ , it is natural to compare the MC score of the next state  $s_{t+1}$  with that of the current state  $s_t$ , since  $s_{t+1} = [s_t, a_t]$ . For each response, if the first erroneous step is step  $t'$  (i.e.,  $MC(s_{t'}) = 0$ ), we set the MC score of the following steps to 0. Our RPE  $P_t$  for step  $t$  is defined as follows:\n\n$$P_t = \\frac{MC(s_t, a_t)}{MC(s_t)}, \\quad (10)$$\n\nwhere  $MC(s_1)$  is the estimated Pass@1 computed in the solution generation phase. However, we empirically find that using a strict criterion where progress is always greater than 1 leads to unsatisfactory performance, as shown in Table 3. To address this, we estimate the final reward label  $\\hat{r}_t$  byintroducing a threshold  $\\epsilon$ :\n\n$$\\hat{r}_t = \\begin{cases} 1 & \\text{if } P_t \\geq \\epsilon, \\\\ 0 & \\text{otherwise.} \\end{cases} \\quad (11)$$\n\nWe also discuss another form of relative progress  $P_t = MC(s_t, a_t) - MC(s_t)$  in Table 3 in Section 4.4.\n\n### 3.2.3. Rationale Generation, Verification and Filtering\n\nTo obtain high-quality rationale data, we use QwQ-32B (Qwen Team, 2025) as the rationale generation model and introduce a three-step pipeline that automatically generates and verifies the rationale of each reasoning step. Given a problem  $x$  with a ground-truth answer  $q^*$  and candidate steps  $\\{a_1, \\dots, a_T\\}$ , the generation and verification proceed as follows:\n\n**Step 1: Code-Based Rationale Generation.** To evaluate the correctness of  $a_t$ , we synthesize step-by-step CoT analysis. It has been shown that program-based reasoning improves verification outcomes (Zhu et al., 2024). Based on CoT analysis, we continue to synthesize code-based rationales to verify  $a_t$  based on the problem and historical steps  $\\{a_1, \\dots, a_{t-1}\\}$ . We prompt the rationale generation model to surround the CoT with `&lt;analyze>` and `&lt;/analyze>`, and the code with `&lt;verify>` and `&lt;/verify>`. The prompt for rationale generation is shown in Table A.2.\n\n**Step 2: Code Execution and Verification.** With the generated code, we execute it and obtain the feedback  $f_t$  for step  $t$ . The execution feedback is formatted as [Code output: {execution result}] and is concatenated to the generated CoT and code as the prefix for the subsequent generation. If the execution result is inconsistent with the generated CoT verification, we observe that QwQ-32B performs self-reflection behaviors until reaching a consensus.\n\n**Step 3: Label Judgment and Consensus Filtering.** After generating and verifying the rationale data of all candidate steps, the rationale generation model finally outputs a number. If all steps are inferred to be correct, the number will be -1, otherwise will be the index of the first erroneous step. For each solution, if there is at least one process label with RPE is not consistent with the labels generated by LLM-as-a-judge (Zheng et al., 2023), we discard the entire solution and only retain the one with all labels consistent. After consensus filtering, we discard approximately 51% of the data and finally obtain a dataset containing 23K problems with reasoning steps and rationale data.\n\n## 4. Experiments\n\nIn this section, we aim to answer the following questions:\n\n- • **Q1:** How does GenPRM perform compared with previous PRMs? (§4.2, §4.3)\n- • **Q2:** How does the performance of GenPRM scale with more test-time compute? (§4.2, §4.3)\n- • **Q3:** How does GenPRM benefit policy model test-time scaling? (§4.3)\n- • **Q4:** How do the components and hyperparameters influence GenPRM? (§4.4)\n\n### 4.1. Setup\n\n**Benchmarks.** We evaluate GenPRM and baseline methods on ProcessBench (Zheng et al., 2024), a benchmark designed to assess process supervision capabilities in mathematical reasoning tasks.&lt;sup>2&lt;/sup>\n\n&lt;sup>2&lt;/sup>Our evaluation code is adapted from &lt;https://github.com/QwenLM/ProcessBench>.Additionally, we conduct BoN and critic refinement experiments using MATH (Hendrycks et al., 2021), AMC23 (AI-MO, 2024b), AIME24 (AI-MO, 2024a), and Minerva Math (Lewkowycz et al., 2022). For BoN response generation, we employ Qwen2.5-Math-7B-Instruct (Yang et al., 2024b) and Gemma-3-12b-it (Gemma Team and Google DeepMind, 2025) as policy models. For policy model TTS with GenPRM as the critic, we use Gemma-3-12b-it (Gemma Team and Google DeepMind, 2025) and Qwen2.5-7B-Instruct (Yang et al., 2024a) as generators.\n\n**Baselines.** For ProcessBench and BoN experiments, we compare GenPRM with the following methods:\n\n- • **Math-Shepherd-PRM-7B** (Wang et al., 2024b): This method trains a PRM using hard labels computed based on MC estimation.\n- • **RLHFlow series** (Xiong et al., 2024): Includes RLHFlow-PRM-Mistral-8B and RLHFlow-PRM-Deepseek-8B.\n- • **Skywork-PRM series** (Skywork o1 Team, 2024): Comprises Skywork-PRM-1.5B and Skywork-PRM-7B.\n- • **EurusPRM** (Cui et al., 2025): EurusPRM-Stage1 and EurusPRM-Stage2 are trained as implicit PRMs (Yuan et al., 2024).\n- • **Qwen2.5-Math series** (Zheng et al., 2024; Zhang et al., 2025c): Qwen2.5-Math-7B-Math-Shepherd and Qwen2.5-Math-7B-PRM800K are trained with Math-Shepherd (Wang et al., 2024b) and PRM800K (Lightman et al., 2024), respectively. For Qwen2.5-Math-PRM-7B and Qwen2.5-Math-PRM-72B, the training data is applied consensus filtering using LLM-as-a-judge (Zheng et al., 2023).\n- • **RetrievalPRM-7B** (Zhu et al., 2025): The method enhances PRM with retrieved questions and corresponding steps.\n- • **Universal-PRM-7B** (Tan et al., 2025): The method proposes an automated framework using ensemble prompting and reverse verification.\n- • **Dyve-14B** (Zhong et al., 2025): This method dynamically applies fast or slow verification for each reasoning step.\n- • **Direct Generative PRM-7B**: The method trains a direct generative PRM with the original language head via SFT using the same data as GenPRM, but without CoT and code verification.\n\nFor critic experiments, we use the following methods for comparison:\n\n- • **Self-Refine** (Madaan et al., 2023): This method uses the generator to self-critique and refine the solution.\n- • **DeepSeek-R1-Distill-Qwen-7B** (DeepSeek-AI et al., 2025): This model is fine-tuned based on Qwen2.5-Math-7B (Yang et al., 2024a) using high-quality reasoning data generated by DeepSeek-R1 (DeepSeek-AI et al., 2025).\n\n**Implementation Details.** For RPE, we set  $\\epsilon = 0.8$  across all experiments, with ablation studies presented in Section 4.4. Rationale data is generated using QwQ-32B (Qwen Team, 2025) and the prompt template is shown in Table A.2. Our base models are from the DeepSeek-R1-Distill series (DeepSeek-AI et al., 2025), specifically the 1.5B, 7B, and 32B parameter variants. The training configuration for our method uses a batch size of 64 and a learning rate of  $2.0 \\times 10^{-6}$ . During evaluation, we employ a temperature of 0.6. For critique refinement experiments, we extract content within the `&lt;analyze>&lt;/analyze>` tags, focusing exclusively on steps predicted as negative by the policy model. The baseline methods utilize standardized prompt templates (detailed in Table A.2) to ensure consistent critique generation formats.**Table 1:** ProcessBench results reported with F1 scores. The results of GenPRM are shaded. For 1.5B PRMs, **bold** indicates the best Pass@1 or scores superior to GPT-4o. For 7-8B and 14-72B PRMs, **bold** denotes the best Pass@1 or scores superior to Qwen2.5-Math-PRM-72B.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Model&lt;/th>\n&lt;th># Samples&lt;/th>\n&lt;th>GSM8K&lt;/th>\n&lt;th>MATH&lt;/th>\n&lt;th>Olympiad Bench&lt;/th>\n&lt;th>Omni-MATH&lt;/th>\n&lt;th>Avg.&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>Proprietary LLMs (Critic)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GPT-4o-0806&lt;/td>\n&lt;td>unk&lt;/td>\n&lt;td>79.2&lt;/td>\n&lt;td>63.6&lt;/td>\n&lt;td>51.4&lt;/td>\n&lt;td>53.5&lt;/td>\n&lt;td>61.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>o1-mini&lt;/td>\n&lt;td>unk&lt;/td>\n&lt;td>93.2&lt;/td>\n&lt;td>88.9&lt;/td>\n&lt;td>87.2&lt;/td>\n&lt;td>82.4&lt;/td>\n&lt;td>87.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>PRMs (1.5B)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-1.5B&lt;/td>\n&lt;td>unk&lt;/td>\n&lt;td>&lt;b>59.0&lt;/b>&lt;/td>\n&lt;td>48.0&lt;/td>\n&lt;td>19.3&lt;/td>\n&lt;td>19.2&lt;/td>\n&lt;td>36.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-1.5B (Pass@1)&lt;/td>\n&lt;td>23K&lt;/td>\n&lt;td>52.8&lt;/td>\n&lt;td>&lt;b>66.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>55.1&lt;/b>&lt;/td>\n&lt;td>&lt;b>54.5&lt;/b>&lt;/td>\n&lt;td>&lt;b>57.3&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-1.5B (Maj@8)&lt;/td>\n&lt;td>23K&lt;/td>\n&lt;td>51.3&lt;/td>\n&lt;td>&lt;b>74.4&lt;/b>&lt;/td>\n&lt;td>&lt;b>65.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>62.5&lt;/b>&lt;/td>\n&lt;td>&lt;b>63.4&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>PRMs (7-8B)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Math-Shepherd-PRM-7B&lt;/td>\n&lt;td>445K&lt;/td>\n&lt;td>47.9&lt;/td>\n&lt;td>29.5&lt;/td>\n&lt;td>24.8&lt;/td>\n&lt;td>23.8&lt;/td>\n&lt;td>31.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RLHFlow-PRM-Mistral-8B&lt;/td>\n&lt;td>273K&lt;/td>\n&lt;td>50.4&lt;/td>\n&lt;td>33.4&lt;/td>\n&lt;td>13.8&lt;/td>\n&lt;td>15.8&lt;/td>\n&lt;td>28.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RLHFlow-PRM-Deepseek-8B&lt;/td>\n&lt;td>253K&lt;/td>\n&lt;td>38.8&lt;/td>\n&lt;td>33.8&lt;/td>\n&lt;td>16.9&lt;/td>\n&lt;td>16.9&lt;/td>\n&lt;td>26.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-7B&lt;/td>\n&lt;td>unk&lt;/td>\n&lt;td>70.8&lt;/td>\n&lt;td>53.6&lt;/td>\n&lt;td>22.9&lt;/td>\n&lt;td>21.0&lt;/td>\n&lt;td>42.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>EurusPRM-Stage1&lt;/td>\n&lt;td>463K&lt;/td>\n&lt;td>44.3&lt;/td>\n&lt;td>35.6&lt;/td>\n&lt;td>21.7&lt;/td>\n&lt;td>23.1&lt;/td>\n&lt;td>31.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>EurusPRM-Stage2&lt;/td>\n&lt;td>30K&lt;/td>\n&lt;td>47.3&lt;/td>\n&lt;td>35.7&lt;/td>\n&lt;td>21.2&lt;/td>\n&lt;td>20.9&lt;/td>\n&lt;td>31.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-Math-Shepherd&lt;/td>\n&lt;td>445K&lt;/td>\n&lt;td>62.5&lt;/td>\n&lt;td>31.6&lt;/td>\n&lt;td>13.7&lt;/td>\n&lt;td>7.7&lt;/td>\n&lt;td>28.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-PRM800K&lt;/td>\n&lt;td>264K&lt;/td>\n&lt;td>68.2&lt;/td>\n&lt;td>62.6&lt;/td>\n&lt;td>50.7&lt;/td>\n&lt;td>44.3&lt;/td>\n&lt;td>56.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-PRM-7B&lt;/td>\n&lt;td>~344K&lt;/td>\n&lt;td>82.4&lt;/td>\n&lt;td>77.6&lt;/td>\n&lt;td>67.5&lt;/td>\n&lt;td>66.3&lt;/td>\n&lt;td>73.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RetrievalPRM-7B&lt;/td>\n&lt;td>404K&lt;/td>\n&lt;td>74.6&lt;/td>\n&lt;td>71.1&lt;/td>\n&lt;td>60.2&lt;/td>\n&lt;td>57.3&lt;/td>\n&lt;td>65.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Universal-PRM-7B&lt;/td>\n&lt;td>unk&lt;/td>\n&lt;td>&lt;b>85.8&lt;/b>&lt;/td>\n&lt;td>77.7&lt;/td>\n&lt;td>67.6&lt;/td>\n&lt;td>66.4&lt;/td>\n&lt;td>74.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Direct Generative PRM-7B&lt;/td>\n&lt;td>23K&lt;/td>\n&lt;td>63.9&lt;/td>\n&lt;td>65.8&lt;/td>\n&lt;td>54.5&lt;/td>\n&lt;td>55.9&lt;/td>\n&lt;td>60.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-7B (Pass@1)&lt;/td>\n&lt;td>23K&lt;/td>\n&lt;td>78.7&lt;/td>\n&lt;td>&lt;b>80.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>72.2&lt;/b>&lt;/td>\n&lt;td>&lt;b>69.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>75.2&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-7B (Maj@8)&lt;/td>\n&lt;td>23K&lt;/td>\n&lt;td>81.0&lt;/td>\n&lt;td>&lt;b>85.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>78.4&lt;/b>&lt;/td>\n&lt;td>&lt;b>76.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>80.5&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>PRMs (14-72B)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Dyve-14B&lt;/td>\n&lt;td>117K&lt;/td>\n&lt;td>68.5&lt;/td>\n&lt;td>58.3&lt;/td>\n&lt;td>49.0&lt;/td>\n&lt;td>47.2&lt;/td>\n&lt;td>55.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-PRM-72B&lt;/td>\n&lt;td>~344K&lt;/td>\n&lt;td>&lt;b>87.3&lt;/b>&lt;/td>\n&lt;td>80.6&lt;/td>\n&lt;td>74.3&lt;/td>\n&lt;td>71.1&lt;/td>\n&lt;td>78.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-32B (Pass@1)&lt;/td>\n&lt;td>23K&lt;/td>\n&lt;td>83.1&lt;/td>\n&lt;td>&lt;b>81.7&lt;/b>&lt;/td>\n&lt;td>72.8&lt;/td>\n&lt;td>&lt;b>72.8&lt;/b>&lt;/td>\n&lt;td>77.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-32B (Maj@8)&lt;/td>\n&lt;td>23K&lt;/td>\n&lt;td>85.1&lt;/td>\n&lt;td>&lt;b>86.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>78.9&lt;/b>&lt;/td>\n&lt;td>&lt;b>80.1&lt;/b>&lt;/td>\n&lt;td>&lt;b>82.6&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n## 4.2. ProcessBench Results\n\n**GenPRM outperforms classification-based PRMs on ProcessBench.** As shown in Table 1, GenPRM-7B significantly outperforms direct generative PRM and surpasses **all** previous PRMs with parameters less than 72B on ProcessBench. Also, GenPRM-1.5B outperforms Skywork-PRM-1.5B by a large margin. It is noteworthy that GenPRM is trained with merely **23K** data from **MATH** (Hendrycks et al., 2021) only. By comparing the detailed results in Table 6, we can find that the performance gain of GenPRM mainly comes from the stronger abilities of finding **erroneous** steps and we provide concrete cases in Appendix C. These results demonstrating the superiority of generative modeling of PRM.\n\n**GenPRM enables smaller PRMs surpass 10 $\\times$  larger PRMs and GPT-4o via TTS.** We also compare the TTS results of GenPRM in Table 1 and find that GenPRM-1.5B surpasses GPT-4 and GenPRM-7B exceeds Qwen2.5-Math-PRM-72B on ProcessBench via simply majority voting, showing that scaling test-time compute is highly effective for GenPRM. We also find that the performance improvement of scaling the test-time compute on **harder** problems is larger than that of easier questions.### 4.3. Policy Model Test-Time Scaling Results\n\n**GenPRM as a Verifier.** The results in Figure 4 (a)-(d) show that GenPRM outperforms the baselines on MATH, AMC23, AIME24, and Minerva Math with Qwen2.5-Math-7B-Instruct (Yang et al., 2024b) as the generation model. The advantage of GenPRM becomes larger by scaling the test-time compute of GenPRM and the generation model. Figure 4 (e)-(h) demonstrates that GenPRM generalizes well to responses with Gemma-3-12b-it (Gemma Team and Google DeepMind, 2025) as the generation model.\n\n**Figure 4:** BoN results with different generation models on multiple mathematical benchmarks.\n\n**GenPRM as a Critic.** We also conduct experiments by using GenPRM as a critic to refine the outputs of the policy model. The results in Table 2 and Figure 1 (right) show that GenPRM exhibits strong critique abilities than the baselines, significantly improving the performance of the policy model and the performance continues to increase with more refinement based on the critic feedback.\n\n### 4.4. Analysis\n\n**Label Estimation Method and Criterion.** To explore how different label estimation influences GenPRM, we conduct experiments with the following methods: (1) hard label (Wang et al., 2024b; Zhang et al., 2025c); (2) RPE in (10); and (3) a RPE variant ( $P_t = MC(s_t, a_t) - MC(s_t)$ ). For the RPE and its variant, we use different thresholds  $\\epsilon$  for evaluation and set the labels as correct by checking whether  $P_t \\geq \\epsilon$ . The results in Table 3 show that RPE and its variant outperforms hard label estimation and RPE with  $\\epsilon = 0.8$  achieves the best result. By scaling test-time compute with majority voting, the results in Table 4 demonstrate that RPE with  $\\epsilon = 0.8$  still reaches the best.**Table 2:** Results of critique refinement experiments. The results of GenPRM are shaded. For each refinement turn, the highest values are **bolded**.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">Critic Model&lt;/th>\n&lt;th colspan=\"5\">Gemma-3-12b-it as Generator&lt;/th>\n&lt;th colspan=\"5\">Qwen2.5-7B-Instruct as Generator&lt;/th>\n&lt;th rowspan=\"2\">Avg.&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>AMC23&lt;/th>\n&lt;th>AIME24&lt;/th>\n&lt;th>MATH&lt;/th>\n&lt;th>Minerva Math&lt;/th>\n&lt;th>Avg.&lt;/th>\n&lt;th>AMC23&lt;/th>\n&lt;th>AIME24&lt;/th>\n&lt;th>MATH&lt;/th>\n&lt;th>Minerva Math&lt;/th>\n&lt;th>Avg.&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Zero-shot&lt;/td>\n&lt;td>64.1&lt;/td>\n&lt;td>15.8&lt;/td>\n&lt;td>83.8&lt;/td>\n&lt;td>31.9&lt;/td>\n&lt;td>48.9&lt;/td>\n&lt;td>51.6&lt;/td>\n&lt;td>7.1&lt;/td>\n&lt;td>76.2&lt;/td>\n&lt;td>34.5&lt;/td>\n&lt;td>42.4&lt;/td>\n&lt;td>45.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"12\" style=\"text-align: center;\">&lt;i>Turn 1&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Generator&lt;/td>\n&lt;td>66.6&lt;/td>\n&lt;td>15.8&lt;/td>\n&lt;td>84.7&lt;/td>\n&lt;td>33.3&lt;/td>\n&lt;td>50.1&lt;/td>\n&lt;td>50.6&lt;/td>\n&lt;td>8.0&lt;/td>\n&lt;td>76.8&lt;/td>\n&lt;td>34.0&lt;/td>\n&lt;td>42.4&lt;/td>\n&lt;td>46.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepSeek-R1-Distill-7B&lt;/td>\n&lt;td>69.1&lt;/td>\n&lt;td>17.9&lt;/td>\n&lt;td>84.6&lt;/td>\n&lt;td>33.0&lt;/td>\n&lt;td>51.2&lt;/td>\n&lt;td>50.6&lt;/td>\n&lt;td>6.3&lt;/td>\n&lt;td>77.7&lt;/td>\n&lt;td>34.7&lt;/td>\n&lt;td>42.3&lt;/td>\n&lt;td>46.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-7B&lt;/td>\n&lt;td>&lt;b>74.1&lt;/b>&lt;/td>\n&lt;td>&lt;b>19.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>86.0&lt;/b>&lt;/td>\n&lt;td>&lt;b>35.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>53.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>57.5&lt;/b>&lt;/td>\n&lt;td>&lt;b>8.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>80.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>36.5&lt;/b>&lt;/td>\n&lt;td>&lt;b>45.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>49.8&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"12\" style=\"text-align: center;\">&lt;i>Turn 2&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Generator&lt;/td>\n&lt;td>66.6&lt;/td>\n&lt;td>18.0&lt;/td>\n&lt;td>84.8&lt;/td>\n&lt;td>31.6&lt;/td>\n&lt;td>50.3&lt;/td>\n&lt;td>49.8&lt;/td>\n&lt;td>8.0&lt;/td>\n&lt;td>76.9&lt;/td>\n&lt;td>31.8&lt;/td>\n&lt;td>41.6&lt;/td>\n&lt;td>46.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepSeek-R1-Distill-7B&lt;/td>\n&lt;td>70.9&lt;/td>\n&lt;td>18.3&lt;/td>\n&lt;td>85.0&lt;/td>\n&lt;td>33.5&lt;/td>\n&lt;td>51.9&lt;/td>\n&lt;td>51.9&lt;/td>\n&lt;td>7.9&lt;/td>\n&lt;td>78.1&lt;/td>\n&lt;td>32.8&lt;/td>\n&lt;td>42.7&lt;/td>\n&lt;td>47.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-7B&lt;/td>\n&lt;td>&lt;b>75.0&lt;/b>&lt;/td>\n&lt;td>&lt;b>21.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>86.9&lt;/b>&lt;/td>\n&lt;td>&lt;b>35.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>54.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>59.4&lt;/b>&lt;/td>\n&lt;td>&lt;b>9.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>82.2&lt;/b>&lt;/td>\n&lt;td>&lt;b>35.0&lt;/b>&lt;/td>\n&lt;td>&lt;b>46.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>50.7&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"12\" style=\"text-align: center;\">&lt;i>Turn 3&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Generator&lt;/td>\n&lt;td>67.8&lt;/td>\n&lt;td>18.1&lt;/td>\n&lt;td>85.0&lt;/td>\n&lt;td>32.1&lt;/td>\n&lt;td>50.8&lt;/td>\n&lt;td>49.7&lt;/td>\n&lt;td>8.1&lt;/td>\n&lt;td>77.1&lt;/td>\n&lt;td>30.8&lt;/td>\n&lt;td>41.4&lt;/td>\n&lt;td>46.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepSeek-R1-Distill-7B&lt;/td>\n&lt;td>69.6&lt;/td>\n&lt;td>18.8&lt;/td>\n&lt;td>85.0&lt;/td>\n&lt;td>33.4&lt;/td>\n&lt;td>51.7&lt;/td>\n&lt;td>51.9&lt;/td>\n&lt;td>8.3&lt;/td>\n&lt;td>78.2&lt;/td>\n&lt;td>32.7&lt;/td>\n&lt;td>42.7&lt;/td>\n&lt;td>47.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-7B&lt;/td>\n&lt;td>&lt;b>76.2&lt;/b>&lt;/td>\n&lt;td>&lt;b>22.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>86.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>36.0&lt;/b>&lt;/td>\n&lt;td>&lt;b>55.4&lt;/b>&lt;/td>\n&lt;td>&lt;b>62.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>9.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>82.9&lt;/b>&lt;/td>\n&lt;td>&lt;b>34.9&lt;/b>&lt;/td>\n&lt;td>&lt;b>47.5&lt;/b>&lt;/td>\n&lt;td>&lt;b>51.5&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 3:** Results of GenPRM with different label estimation method and threshold on ProcessBench, reported with Pass@1. The best results are shown in **bold**.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Estimation Method&lt;/th>\n&lt;th>Positive Label Criterion&lt;/th>\n&lt;th>GSM8K&lt;/th>\n&lt;th>MATH&lt;/th>\n&lt;th>Olympiad Bench&lt;/th>\n&lt;th>Omni-MATH&lt;/th>\n&lt;th>Avg.&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>&lt;math>P_t = MC(s_t, a_t)&lt;/math> (hard label)&lt;/td>\n&lt;td>&lt;math>P_t &gt; 0&lt;/math>&lt;/td>\n&lt;td>72.9&lt;/td>\n&lt;td>78.9&lt;/td>\n&lt;td>&lt;b>73.2&lt;/b>&lt;/td>\n&lt;td>68.0&lt;/td>\n&lt;td>73.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"3\">&lt;math>P_t = MC(s_t, a_t) - MC(s_t)&lt;/math>&lt;/td>\n&lt;td>&lt;math>P_t \\geq -0.1&lt;/math>&lt;/td>\n&lt;td>77.3&lt;/td>\n&lt;td>79.9&lt;/td>\n&lt;td>70.8&lt;/td>\n&lt;td>68.5&lt;/td>\n&lt;td>74.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq -0.3&lt;/math>&lt;/td>\n&lt;td>76.8&lt;/td>\n&lt;td>79.6&lt;/td>\n&lt;td>71.1&lt;/td>\n&lt;td>69.0&lt;/td>\n&lt;td>74.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq -0.5&lt;/math>&lt;/td>\n&lt;td>75.8&lt;/td>\n&lt;td>80.2&lt;/td>\n&lt;td>72.8&lt;/td>\n&lt;td>68.6&lt;/td>\n&lt;td>74.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"4\">&lt;math>P_t = \\frac{MC(s_t, a_t)}{MC(s_t)}&lt;/math>&lt;/td>\n&lt;td>&lt;math>P_t \\geq 0.1&lt;/math>&lt;/td>\n&lt;td>74.8&lt;/td>\n&lt;td>78.7&lt;/td>\n&lt;td>71.6&lt;/td>\n&lt;td>68.7&lt;/td>\n&lt;td>73.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq 0.5&lt;/math>&lt;/td>\n&lt;td>75.7&lt;/td>\n&lt;td>79.2&lt;/td>\n&lt;td>70.4&lt;/td>\n&lt;td>68.5&lt;/td>\n&lt;td>73.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq 0.8&lt;/math>&lt;/td>\n&lt;td>&lt;b>78.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>80.3&lt;/b>&lt;/td>\n&lt;td>72.2&lt;/td>\n&lt;td>&lt;b>69.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>75.2&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq 1.0&lt;/math>&lt;/td>\n&lt;td>76.4&lt;/td>\n&lt;td>77.4&lt;/td>\n&lt;td>68.1&lt;/td>\n&lt;td>67.2&lt;/td>\n&lt;td>72.3&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 4:** Results of GenPRM with different label estimation method and threshold on ProcessBench, reported with Maj@8. The best results are shown in **bold**.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Estimation Method&lt;/th>\n&lt;th>Positive Label Criterion&lt;/th>\n&lt;th>GSM8K&lt;/th>\n&lt;th>MATH&lt;/th>\n&lt;th>Olympiad Bench&lt;/th>\n&lt;th>Omni-MATH&lt;/th>\n&lt;th>Avg.&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>&lt;math>P_t = MC(s_t, a_t)&lt;/math> (hard label)&lt;/td>\n&lt;td>&lt;math>P_t &gt; 0&lt;/math>&lt;/td>\n&lt;td>75.1&lt;/td>\n&lt;td>83.8&lt;/td>\n&lt;td>&lt;b>80.6&lt;/b>&lt;/td>\n&lt;td>74.4&lt;/td>\n&lt;td>78.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"3\">&lt;math>P_t = MC(s_t, a_t) - MC(s_t)&lt;/math>&lt;/td>\n&lt;td>&lt;math>P_t \\geq -0.1&lt;/math>&lt;/td>\n&lt;td>79.8&lt;/td>\n&lt;td>85.1&lt;/td>\n&lt;td>78.0&lt;/td>\n&lt;td>74.5&lt;/td>\n&lt;td>79.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq -0.3&lt;/math>&lt;/td>\n&lt;td>80.9&lt;/td>\n&lt;td>&lt;b>86.5&lt;/b>&lt;/td>\n&lt;td>78.1&lt;/td>\n&lt;td>75.0&lt;/td>\n&lt;td>80.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq -0.5&lt;/math>&lt;/td>\n&lt;td>78.1&lt;/td>\n&lt;td>85.6&lt;/td>\n&lt;td>79.1&lt;/td>\n&lt;td>73.4&lt;/td>\n&lt;td>79.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"4\">&lt;math>P_t = \\frac{MC(s_t, a_t)}{MC(s_t)}&lt;/math>&lt;/td>\n&lt;td>&lt;math>P_t \\geq 0.1&lt;/math>&lt;/td>\n&lt;td>77.0&lt;/td>\n&lt;td>84.6&lt;/td>\n&lt;td>78.1&lt;/td>\n&lt;td>75.3&lt;/td>\n&lt;td>78.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq 0.5&lt;/math>&lt;/td>\n&lt;td>78.0&lt;/td>\n&lt;td>85.2&lt;/td>\n&lt;td>78.2&lt;/td>\n&lt;td>74.3&lt;/td>\n&lt;td>78.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq 0.8&lt;/math>&lt;/td>\n&lt;td>81.0&lt;/td>\n&lt;td>85.7&lt;/td>\n&lt;td>78.4&lt;/td>\n&lt;td>&lt;b>76.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>80.5&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq 1.0&lt;/math>&lt;/td>\n&lt;td>&lt;b>81.1&lt;/b>&lt;/td>\n&lt;td>84.1&lt;/td>\n&lt;td>76.0&lt;/td>\n&lt;td>74.7&lt;/td>\n&lt;td>79.0&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Reasoning Components.** To understand how each reasoning component influence GenPRM, we conduct experiments by training GenPRM with: (1) CoT data only, (2) code verification data only, and (3) full data. During inference phase, we also compare several variants. For example, GenPRM trained with full data can be used to only verify each step with CoT only by stopping generation at `&lt;/analyze>` token. The results in Table 5 show that: (1) the improvement of GenPRM mainly comesfrom CoT reasoning; (2) generating code and reasoning with code execution result improves the process verification performance as well.\n\n**Table 5:** Results on ProcessBench of GenPRM with different reasoning components, reported with Maj@8. The best results are shown in **bold**.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th colspan=\"2\">Training&lt;/th>\n&lt;th colspan=\"3\">Inference&lt;/th>\n&lt;th rowspan=\"2\">GSM8K&lt;/th>\n&lt;th rowspan=\"2\">MATH&lt;/th>\n&lt;th rowspan=\"2\">Olympiad Bench&lt;/th>\n&lt;th rowspan=\"2\">Omni-MATH&lt;/th>\n&lt;th rowspan=\"2\">Avg.&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>CoT&lt;/th>\n&lt;th>Code&lt;/th>\n&lt;th>CoT&lt;/th>\n&lt;th>Code&lt;/th>\n&lt;th>Code Exec.&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>x&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>63.9&lt;/td>\n&lt;td>65.8&lt;/td>\n&lt;td>54.5&lt;/td>\n&lt;td>55.9&lt;/td>\n&lt;td>60.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>x&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>67.0&lt;/td>\n&lt;td>70.8&lt;/td>\n&lt;td>61.6&lt;/td>\n&lt;td>57.4&lt;/td>\n&lt;td>64.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>x&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>70.6&lt;/td>\n&lt;td>76.6&lt;/td>\n&lt;td>67.3&lt;/td>\n&lt;td>63.9&lt;/td>\n&lt;td>69.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>✓&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>76.4&lt;/td>\n&lt;td>83.0&lt;/td>\n&lt;td>&lt;b>80.5&lt;/b>&lt;/td>\n&lt;td>75.4&lt;/td>\n&lt;td>78.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"5\">✓&lt;/td>\n&lt;td rowspan=\"5\">✓&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>60.1&lt;/td>\n&lt;td>66.7&lt;/td>\n&lt;td>59.9&lt;/td>\n&lt;td>59.2&lt;/td>\n&lt;td>61.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>x&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>61.3&lt;/td>\n&lt;td>74.7&lt;/td>\n&lt;td>68.1&lt;/td>\n&lt;td>62.0&lt;/td>\n&lt;td>66.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>✓&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>78.8&lt;/td>\n&lt;td>85.1&lt;/td>\n&lt;td>78.7&lt;/td>\n&lt;td>74.9&lt;/td>\n&lt;td>79.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>&lt;b>81.0&lt;/b>&lt;/td>\n&lt;td>85.1&lt;/td>\n&lt;td>78.1&lt;/td>\n&lt;td>75.5&lt;/td>\n&lt;td>79.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>&lt;b>81.0&lt;/b>&lt;/td>\n&lt;td>&lt;b>85.7&lt;/b>&lt;/td>\n&lt;td>78.4&lt;/td>\n&lt;td>&lt;b>76.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>80.5&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n## 5. Related Work\n\n**Process Reward Models.** Process reward models have been proved to be effective for providing step-wise scores and are superior to outcome reward models in mathematical reasoning tasks (Uesato et al., 2022; Lightman et al., 2024). However, annotating a process supervision dataset such as PRM800K (Lightman et al., 2024) requires significant human costs. To mitigate this cost, prior works utilize Monte Carlo estimation (Wang et al., 2024b) and binary search (Luo et al., 2024) for automated label generation. Subsequent research improves PRMs through methods such as advantage modeling (Setlur et al., 2025),  $Q$ -value rankings (Li and Li, 2025), implicit entropy regularization (Zhang et al., 2024a), retrieval-augmented generation (Zhu et al., 2025), and fast-slow verification (Zhong et al., 2025). Furthermore, the community has developed high-quality open-source PRMs, including the RLHFlow series (Xiong et al., 2024), Math-psa (Wang et al., 2024a), Skywork series (Skywork o1 Team, 2024), and Qwen2.5-Math series (Zheng et al., 2024; Zhang et al., 2025c). Recently, a line of works focus on extending PRMs to other tasks, including coding (Zhang et al., 2024b), medical tasks (Jiang et al., 2025), agentic tasks (Choudhury, 2025), general domain tasks (Zhang et al., 2025a; Zeng et al., 2025), and multimodal tasks (Wang et al., 2025). Current studies also focus on benchmarking PRMs (Zheng et al., 2024; Song et al., 2025) to systematically evaluate their performance.\n\n**Large Language Model Test-Time Scaling.** Scaling test-time computation is an effective method for improving performance during the inference phase (OpenAI, 2024a,b; DeepSeek-AI et al., 2025). TTS is commonly implemented with external verifiers (e.g., ORMs and PRMs) or strategies (e.g., beam search and MCTS) (Wu et al., 2025; Snell et al., 2025; Beeching et al., 2024; Liu et al., 2025). In this work, we scale the test-time computation of a generative PRM with an explicit reasoning process and GenPRM can also serve as a verifier or a critic model in external TTS.\n\n**Enhancing the Generative Abilities of Reward Models.** Previous research has investigated methods to enhance the generative capabilities of reward models using CoT reasoning (Ankner et al., 2024; Zhang et al., 2025b; Mahan et al., 2024). For instance, CCloud reward models (Ankner et al., 2024) are trained to generate critiques for responses and predict rewards using an additional rewardhead. GenRM-CoT (Zhang et al., 2025b) and GenRM (Mahan et al., 2024) train generative reward models that perform CoT reasoning before making final predictions via SFT and preference learning, respectively. CTRL (Xie et al., 2025) demonstrates that critic models exhibit strong discriminative abilities when utilized as generative reward models. Prior to these works, GRM (Yang et al., 2024c) regularizes the hidden states of reward models with a text generation loss.\n\n## 6. Conclusion\n\nIn this work, we propose GenPRM, a generative process reward model that performs explicit reasoning and code verification for process supervision and enables scaling the test-time compute of PRMs. Experimental results on ProcessBench and several mathematical datasets show GenPRM outperforms prior PRMs. We also demonstrate that the performance of GenPRM increases via test-time scaling and GenPRM is effective as a critic model. We believe that this work provides perspectives on PRMs by demonstrating the strong TTS abilities of PRMs and extending the applications of PRMs.\n\n**Limitations.** First, GenPRM provides process supervision by generative reasoning, which introduces additional computation during inference phase. Future work will investigate how to prune the reasoning process dynamically (Zhong et al., 2025). Although GenPRM focuses mainly on mathematical reasoning tasks, it is worth to explore how to apply generative reasoning on coding and general reasoning tasks in the future (Zhang et al., 2025a). Additionally, it would be interesting to leverage RL to incentivize the generative reasoning abilities of GenPRM.\n\n## References\n\nAI-MO. AIME 2024, 2024a. URL &lt;https://huggingface.co/datasets/AI-MO/aimo-validation-aimo>.\n\nAI-MO. AMC 2023, 2024b. URL &lt;https://huggingface.co/datasets/AI-MO/aimo-validation-amc>.\n\nZachary Ankner, Mansheej Paul, Brandon Cui, Jonathan D Chang, and Prithviraj Ammanabrolu. Critique-out-Loud Reward Models. *arXiv preprint arXiv:2408.11791*, 2024.\n\nAnthropic. Introducing Claude, 2023. URL &lt;https://www.anthropic.com/index/introducing-claude/>.\n\nEdward Beeching, Lewis Tunstall, and Sasha Rush. Scaling Test-Time Compute with Open Models, 2024. URL &lt;https://huggingface.co/spaces/HuggingFaceH4/blogpost-scaling-test-time-compute>.\n\nBradley Brown, Jordan Juravsky, Ryan Ehrlich, Ronald Clark, Quoc V Le, Christopher Ré, and Azalia Mirhoseini. Large Language Monkeys: Scaling Inference Compute with Repeated Sampling. *arXiv preprint arXiv:2407.21787*, 2024.\n\nSanjiban Choudhury. Process Reward Models for LLM Agents: Practical Framework and Directions. *arXiv preprint arXiv:2502.10325*, 2025.\n\nGanqu Cui, Lifan Yuan, Zefan Wang, Hanbin Wang, Wendi Li, Bingxiang He, Yuchen Fan, Tianyu Yu, Qixin Xu, Weize Chen, et al. Process Reinforcement through Implicit Rewards. *arXiv preprint arXiv:2502.01456*, 2025.DeepSeek-AI, Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, Xiaokang Zhang, Xingkai Yu, Yu Wu, Z. F. Wu, Zhibin Gou, Zhihong Shao, Zhuoshu Li, Ziyi Gao, Aixin Liu, Bing Xue, Bingxuan Wang, Bochao Wu, Bei Feng, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chenyu Zhang, Chong Ruan, Damai Dai, Deli Chen, Dongjie Ji, Erhang Li, Fangyun Lin, Fucong Dai, Fuli Luo, Guangbo Hao, Guanting Chen, Guowei Li, H. Zhang, Han Bao, Hanwei Xu, Haocheng Wang, Honghui Ding, Huajian Xin, Huazuo Gao, Hui Qu, Hui Li, Jianzhong Guo, Jiashi Li, Jiawei Wang, Jingchang Chen, Jingyang Yuan, Junjie Qiu, Junlong Li, J. L. Cai, Jiaqi Ni, Jian Liang, Jin Chen, Kai Dong, Kai Hu, Kaige Gao, Kang Guan, Kexin Huang, Kuai Yu, Lean Wang, Lecong Zhang, Liang Zhao, Litong Wang, Liyue Zhang, Lei Xu, Leyi Xia, Mingchuan Zhang, Minghua Zhang, Minghui Tang, Meng Li, Miaojun Wang, Mingming Li, Ning Tian, Panpan Huang, Peng Zhang, Qiancheng Wang, Qinyu Chen, Qiushi Du, Ruiqi Ge, Ruisong Zhang, Ruizhe Pan, Runji Wang, R. J. Chen, R. L. Jin, Ruyi Chen, Shanghao Lu, Shangyan Zhou, Shanhuang Chen, Shengfeng Ye, Shiyu Wang, Shuiping Yu, Shunfeng Zhou, Shuting Pan, S. S. Li, Shuang Zhou, Shaoqing Wu, Shengfeng Ye, Tao Yun, Tian Pei, Tianyu Sun, T. Wang, Wangding Zeng, Wanjia Zhao, Wen Liu, Wenfeng Liang, Wenjun Gao, Wenqin Yu, Wentao Zhang, W. L. Xiao, Wei An, Xiaodong Liu, Xiaohan Wang, Xiaokang Chen, Xiaotao Nie, Xin Cheng, Xin Liu, Xin Xie, Xingchao Liu, Xinyu Yang, Xinyuan Li, Xuecheng Su, Xuheng Lin, X. Q. Li, Xiangyue Jin, Xiaojin Shen, Xiaosha Chen, Xiaowen Sun, Xiaoxiang Wang, Xinnan Song, Xinyi Zhou, Xianzu Wang, Xinxia Shan, Y. K. Li, Y. Q. Wang, Y. X. Wei, Yang Zhang, Yanhong Xu, Yao Li, Yao Zhao, Yaofeng Sun, Yaohui Wang, Yi Yu, Yichao Zhang, Yifan Shi, Yiliang Xiong, Ying He, Yishi Piao, Yisong Wang, Yixuan Tan, Yiyang Ma, Yiyuan Liu, Yongqiang Guo, Yuan Ou, Yuduan Wang, Yue Gong, Yuheng Zou, Yujia He, Yunfan Xiong, Yuxiang Luo, Yuxiang You, Yuxuan Liu, Yuyang Zhou, Y. X. Zhu, Yanhong Xu, Yanping Huang, Yaohui Li, Yi Zheng, Yuchen Zhu, Yunxian Ma, Ying Tang, Yukun Zha, Yuting Yan, Z. Z. Ren, Zehui Ren, Zhangli Sha, Zhe Fu, Zhean Xu, Zhenda Xie, Zhengyan Zhang, Zhewen Hao, Zhicheng Ma, Zhigang Yan, Zhiyu Wu, Zihui Gu, Zijia Zhu, Zijun Liu, Zilin Li, Ziwei Xie, Ziyang Song, Zizheng Pan, Zhen Huang, Zhipeng Xu, Zhongyu Zhang, and Zhen Zhang. DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning. *arXiv preprint arXiv:2501.12948*, 2025.\n\nGemma Team and Google DeepMind. Introducing Gemma 3: The most capable model you can run on a single GPU or TPU, March 2025. URL &lt;https://blog.google/technology/developers/gemma-3>.\n\nZhibin Gou, Zhihong Shao, Yeyun Gong, yelong shen, Yujiu Yang, Nan Duan, and Weizhu Chen. CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing. In *International Conference on Learning Representations (ICLR)*, 2024. URL &lt;https://openreview.net/forum?id=Sx038qxjek>.\n\nDan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. Measuring Mathematical Problem Solving With the MATH Dataset. In *Advances in Neural Information Processing Systems Datasets and Benchmarks Track (Round 2)*, 2021. URL &lt;https://openreview.net/forum?id=7Bywt2mQsCe>.\n\nShuyang Jiang, Yusheng Liao, Zhe Chen, Ya Zhang, Yanfeng Wang, and Yu Wang. MedS&lt;sup>3&lt;/sup>: Towards Medical Small Language Models with Self-Evolved Slow Thinking. *arXiv preprint arXiv:2501.12051*, 2025.\n\nAitor Lewkowycz, Anders Andreassen, David Dohan, Ethan Dyer, Henryk Michalewski, Vinay Ramasesh, Ambrose Slone, Cem Anil, Imanol Schlag, Theo Gutman-Solo, Yuhuai Wu, Behnam Neyshabur, Guy Gur-Ari, and Vedant Misra. Solving Quantitative Reasoning Problems with Language Models. In S. Koyejo, S. Mohamed, A. Agarwal, D. Belgrave, K. Cho, and A. Oh, editors,*Advances in Neural Information Processing Systems (NeurIPS)*, volume 35, pages 3843–3857. Curran Associates, Inc., 2022. URL [https://proceedings.neurips.cc/paper\\\\_files/paper/2022/file/18abbeef8cfe9203fdf9053c9c4fe191-Paper-Conference.pdf](https://proceedings.neurips.cc/paper_files/paper/2022/file/18abbeef8cfe9203fdf9053c9c4fe191-Paper-Conference.pdf).\n\nWendi Li and Yixuan Li. Process Reward Model with Q-value Rankings. In *International Conference on Learning Representations (ICLR)*, 2025. URL &lt;https://openreview.net/forum?id=wQEdh2cgEk>.\n\nHunter Lightman, Vineet Kosaraju, Yuri Burda, Harrison Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. Let’s Verify Step by Step. In *International Conference on Learning Representations (ICLR)*, 2024. URL &lt;https://openreview.net/forum?id=v8L0pN6E0i>.\n\nRunze Liu, Fengshuo Bai, Yali Du, and Yaodong Yang. Meta-Reward-Net: Implicitly Differentiable Reward Learning for Preference-based Reinforcement Learning. In *Advances in Neural Information Processing Systems (NeurIPS)*, volume 35, pages 22270–22284, 2022.\n\nRunze Liu, Yali Du, Fengshuo Bai, Jiafei Lyu, and Xiu Li. PEARL: Zero-shot Cross-task Preference Alignment and Robust Reward Learning for Robotic Manipulation. In Ruslan Salakhutdinov, Zico Kolter, Katherine Heller, Adrian Weller, Nuria Oliver, Jonathan Scarlett, and Felix Berkenkamp, editors, *International Conference on Machine Learning (ICML)*, volume 235 of *Proceedings of Machine Learning Research*, pages 30946–30964. PMLR, 21–27 Jul 2024. URL &lt;https://proceedings.mlr.press/v235/liu24o.html>.\n\nRunze Liu, Junqi Gao, Jian Zhao, Kaiyan Zhang, Xiu Li, Biqing Qi, Wanli Ouyang, and Bowen Zhou. Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling. *arXiv preprint arXiv:2502.06703*, 2025.\n\nLiangchen Luo, Yinxiao Liu, Rosanne Liu, Samrat Phatale, Harsh Lara, Yunxuan Li, Lei Shu, Yun Zhu, Lei Meng, Jiao Sun, et al. Improve Mathematical Reasoning in Language Models by Automated Process Supervision. *arXiv preprint arXiv:2406.06592*, 2024.\n\nAman Madaan, Niket Tandon, Prakash Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegr-effe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, Shashank Gupta, Bodhisattwa Prasad Majumder, Katherine Hermann, Sean Welleck, Amir Yazdanbakhsh, and Peter Clark. Self-Refine: Iterative Refinement with Self-Feedback. In A. Oh, T. Nau-mann, A. Globerson, K. Saenko, M. Hardt, and S. Levine, editors, *Advances in Neural Information Processing Systems (NeurIPS)*, volume 36, pages 46534–46594. Curran Associates, Inc., 2023. URL [https://proceedings.neurips.cc/paper\\\\_files/paper/2023/file/91edff07232fb1b55a505a9e9f6c0ff3-Paper-Conference.pdf](https://proceedings.neurips.cc/paper_files/paper/2023/file/91edff07232fb1b55a505a9e9f6c0ff3-Paper-Conference.pdf).\n\nDakota Mahan, Duy Van Phung, Rafael Rafailov, Chase Blagden, Nathan Lile, Louis Castricato, Jan-Philipp Fränken, Chelsea Finn, and Alon Albalak. Generative Reward Models. *arXiv preprint arXiv:2410.12832*, 2024.\n\nOpenAI. GPT-4 Technical Report. *arXiv preprint arXiv:2303.08774*, 2023.\n\nOpenAI. Learning to reason with LLMs, 2024a. URL &lt;https://openai.com/index/learning-to-reason-with-llms>.\n\nOpenAI. OpenAI o3-mini, 2024b. URL &lt;https://openai.com/index/openai-o3-mini>.\n\nQwen Team. QwQ-32B: Embracing the Power of Reinforcement Learning, March 2025. URL &lt;https://qwenlm.github.io/blog/qwq-32b>.Amrith Setlur, Chirag Nagpal, Adam Fisch, Xinyang Geng, Jacob Eisenstein, Rishabh Agarwal, Alekh Agarwal, Jonathan Berant, and Aviral Kumar. Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning. In *International Conference on Learning Representations (ICLR)*, 2025. URL &lt;https://openreview.net/forum?id=A6Y7AqlzLW>.\n\nZhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li, Y Wu, et al. DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models. *arXiv preprint arXiv:2402.03300*, 2024.\n\nSkywork o1 Team. Skywork-o1 Open Series. &lt;https://huggingface.co/Skywork>, November 2024. URL &lt;https://huggingface.co/Skywork>.\n\nCharlie Victor Snell, Jaehoon Lee, Kelvin Xu, and Aviral Kumar. Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning. In *International Conference on Learning Representations (ICLR)*, 2025. URL &lt;https://openreview.net/forum?id=4FWAwZtd2n>.\n\nMingyang Song, Zhaochen Su, Xiaoye Qu, Jiawei Zhou, and Yu Cheng. PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models. *arXiv preprint arXiv:2501.03124*, 2025.\n\nXiaoyu Tan, Tianchu Yao, Chao Qu, Bin Li, Minghao Yang, Dakuan Lu, Haozhe Wang, Xihe Qiu, Wei Chu, Yinghui Xu, et al. AURORA: Automated Training Framework of Universal Process Reward Models via Ensemble Prompting and Reverse Verification. *arXiv preprint arXiv:2502.11520*, 2025.\n\nJonathan Uesato, Nate Kushman, Ramana Kumar, Francis Song, Noah Siegel, Lisa Wang, Antonia Creswell, Geoffrey Irving, and Irina Higgins. Solving math word problems with process-and outcome-based feedback. *arXiv preprint arXiv:2211.14275*, 2022.\n\nJun Wang, Meng Fang, Ziyu Wan, Muning Wen, Jiachen Zhu, Anjie Liu, Ziqin Gong, Yan Song, Lei Chen, Lionel M Ni, et al. OpenR: An open source framework for advanced reasoning with large language models. *arXiv preprint arXiv:2410.09671*, 2024a.\n\nPeiyi Wang, Lei Li, Zhihong Shao, Runxin Xu, Damai Dai, Yifei Li, Deli Chen, Yu Wu, and Zhifang Sui. Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations. In *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 9426–9439, 2024b.\n\nWeiyun Wang, Zhangwei Gao, Lianjie Chen, Chen Zhe, Jinguo Zhu, Xiangyu Zhao, Yangzhou Liu, Yue Cao, Shenglong Ye, Xizhou Zhu, Lewei Lu, Haodong Duan, Yu Qiao, Jifeng Dai, and Wenhai Wang. VisualPRM: An Effective Process Reward Model for Multimodal Reasoning. *arXiv preprint arXiv:2503.10291*, 2025.\n\nXuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V Le, Ed H. Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. Self-Consistency Improves Chain of Thought Reasoning in Language Models. In *International Conference on Learning Representations (ICLR)*, 2023. URL &lt;https://openreview.net/forum?id=1PL1NIMMrw>.\n\nJason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models. In *Advances in neural information processing systems (NeurIPS)*, volume 35, pages 24824–24837, 2022.Yangzhen Wu, Zhiqing Sun, Shanda Li, Sean Welleck, and Yiming Yang. Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for LLM Problem-Solving. In *International Conference on Learning Representations (ICLR)*, 2025. URL &lt;https://openreview.net/forum?id=VNckp7JEHn>.\n\nZhihui Xie, Liyu Chen, Weichao Mao, Jingjing Xu, Lingpeng Kong, et al. Teaching Language Models to Critique via Reinforcement Learning. *arXiv preprint arXiv:2502.03492*, 2025.\n\nWei Xiong, Hanning Zhang, Nan Jiang, and Tong Zhang. An Implementation of Generative PRM. &lt;https://github.com/RLHFlow/RLHF-Reward-Modeling>, 2024.\n\nAn Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng Liu, Fei Huang, Haoran Wei, Huan Lin, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin Yang, Jiaxi Yang, Jingren Zhou, Junyang Lin, Kai Dang, Keming Lu, Keqin Bao, Kexin Yang, Le Yu, Mei Li, Mingfeng Xue, Pei Zhang, Qin Zhu, Rui Men, Runji Lin, Tianhao Li, Tingyu Xia, Xingzhang Ren, Xuancheng Ren, Yang Fan, Yang Su, Yichang Zhang, Yu Wan, Yuqiong Liu, Zeyu Cui, Zhenru Zhang, and Zihan Qiu. Qwen2.5 Technical Report. *arXiv preprint arXiv:2412.15115*, 2024a.\n\nAn Yang, Beichen Zhang, Binyuan Hui, Bofei Gao, Bowen Yu, Chengpeng Li, Dayiheng Liu, Jianhong Tu, Jingren Zhou, Junyang Lin, Keming Lu, Mingfeng Xue, Runji Lin, Tianyu Liu, Xingzhang Ren, and Zhenru Zhang. Qwen2.5-Math Technical Report: Toward Mathematical Expert Model via Self-Improvement. *arXiv preprint arXiv:2409.12122*, 2024b.\n\nRui Yang, Ruomeng Ding, Yong Lin, Huan Zhang, and Tong Zhang. Regularizing Hidden States Enables Learning Generalizable Reward Model for LLMs. In *Advances in Neural Information Processing Systems (NeurIPS)*, 2024c. URL &lt;https://openreview.net/forum?id=jwh9MHEfmY>.\n\nLifan Yuan, Wendi Li, Huayu Chen, Ganqu Cui, Ning Ding, Kaiyan Zhang, Bowen Zhou, Zhiyuan Liu, and Hao Peng. Free Process Rewards without Process Labels. *arXiv preprint arXiv:2412.01981*, 2024.\n\nThomas Zeng, Shuibai Zhang, Shutong Wu, Christian Classen, Daewon Chae, Ethan Ewer, Minjiae Lee, Heeju Kim, Wonjun Kang, Jackson Kunde, et al. VersaPRM: Multi-Domain Process Reward Model via Synthetic Reasoning Data. *arXiv preprint arXiv:2502.06737*, 2025.\n\nHanning Zhang, Pengcheng Wang, Shizhe Diao, Yong Lin, Rui Pan, Hanze Dong, Dylan Zhang, Pavlo Molchanov, and Tong Zhang. Entropy-Regularized Process Reward Model. *arXiv preprint arXiv:2412.11006*, 2024a.\n\nKaiyan Zhang, Jiayuan Zhang, Haoxin Li, Xuekai Zhu, Ermo Hua, Xingtai Lv, Ning Ding, Biqing Qi, and Bowen Zhou. OpenPRM: Building Open-domain Process-based Reward Models with Preference Trees. In *International Conference on Learning Representations (ICLR)*, 2025a. URL &lt;https://openreview.net/forum?id=fGIqGfmgkW>.\n\nLunjun Zhang, Arian Hosseini, Hritik Bansal, Mehran Kazemi, Aviral Kumar, and Rishabh Agarwal. Generative Verifiers: Reward Modeling as Next-Token Prediction. In *International Conference on Learning Representations (ICLR)*, 2025b. URL &lt;https://openreview.net/forum?id=Ccwp4tFETe>.\n\nYuxiang Zhang, Shangxi Wu, Yuqi Yang, Jiangming Shu, Jinlin Xiao, Chao Kong, and Jitao Sang. o1-Coder: an o1 Replication for Coding. *arXiv preprint arXiv:2412.00154*, 2024b.\n\nZhenru Zhang, Chujie Zheng, Yangzhen Wu, Beichen Zhang, Runji Lin, Bowen Yu, Dayiheng Liu, Jingren Zhou, and Junyang Lin. The Lessons of Developing Process Reward Models in Mathematical Reasoning. *arXiv preprint arXiv:2501.07301*, 2025c.Chujie Zheng, Zhenru Zhang, Beichen Zhang, Runji Lin, Keming Lu, Bowen Yu, Dayiheng Liu, Jingren Zhou, and Junyang Lin. ProcessBench: Identifying Process Errors in Mathematical Reasoning. *arXiv preprint arXiv:2412.06559*, 2024.\n\nLianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, Hao Zhang, Joseph E Gonzalez, and Ion Stoica. Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. In A. Oh, T. Nau-mann, A. Globerson, K. Saenko, M. Hardt, and S. Levine, editors, *Advances in Neural Information Processing Systems (NeurIPS)*, volume 36, pages 46595–46623. Curran Associates, Inc., 2023. URL [https://proceedings.neurips.cc/paper\\\\_files/paper/2023/file/91f18a1287b398d378ef22505bf41832-Paper-Datasets\\\\_and\\\\_Benchmarks.pdf](https://proceedings.neurips.cc/paper_files/paper/2023/file/91f18a1287b398d378ef22505bf41832-Paper-Datasets_and_Benchmarks.pdf).\n\nJianyuan Zhong, Zeju Li, Zhijian Xu, Xiangyu Wen, and Qiang Xu. Dyve: Thinking Fast and Slow for Dynamic Process Verification. *arXiv preprint arXiv:2502.11157*, 2025.\n\nJiachen Zhu, Congmin Zheng, Jianghao Lin, Kounianhua Du, Ying Wen, Yong Yu, Jun Wang, and Weinan Zhang. Retrieval-Augmented Process Reward Model for Generalizable Mathematical Reasoning. *arXiv preprint arXiv:2502.14361*, 2025.\n\nXuekai Zhu, Biqing Qi, Kaiyan Zhang, Xinwei Long, Zhouhan Lin, and Bowen Zhou. PaD: Program-aided Distillation Can Teach Small Models Reasoning Better than Chain-of-thought Fine-tuning. In Kevin Duh, Helena Gomez, and Steven Bethard, editors, *Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)*, pages 2571–2597, Mexico City, Mexico, June 2024. Association for Computational Linguistics. doi: 10.18653/v1/2024.naacl-long.142. URL &lt;https://aclanthology.org/2024.naacl-long.142/>.## A. Experimental Details\n\n### A.1. Scoring and Voting Methods\n\n**PRM-Last.** PRM-Last considers the process reward of the last step of the entire LLM response as the final score, i.e.,  $\\text{score} = r_T$ .\n\n**PRM-Avg.** PRM-Avg computes the mean process reward across all steps as the final score, i.e.,  $\\text{score} = \\frac{1}{T} \\sum_{t=1}^T r_t$ .\n\n**PRM-Min.** PRM-Min uses the minimum process reward across all steps as the final score, i.e.,  $\\text{score} = \\min_r \\{r_t\\}_{t=1}^T$ .\n\n### A.2. Implementation Details\n\nPrompt for CoT and code rationale generation is shown in Table A.2.\n\n#### Prompt for CoT and code rationale generation\n\n**[System]:**\n\nYou are a math teacher. Your task is to review and critique the paragraphs in solution step by step with python code.\n\n**[User]:**\n\nThe following is the math problem and a solution (split into paragraphs, enclosed with tags and indexed from 1):\n\n[Math Problem]\n\n{problem}\n\n[Solution]\n\n```\n&lt;paragraph_1>\n{solution_section_1}\n&lt;/paragraph_1>\n```\n\n...\n\n```\n&lt;paragraph_n>\n{solution_section_n}\n&lt;/paragraph_n>\n```\n\nYour task is to verify the correctness of paragraph in the solution. Split your verification by ‘### Paragraph {{ID}}’.\n\nYour verification for each paragraph should be constructed by 2 parts, wrapped by ‘&lt;analyze>&lt;/analyze>’ and ‘&lt;verify>&lt;/verify>’ separately.1. 1. In ‘`&lt;analyze>&lt;/analyze>`’ part, you need to analyze the reasoning process and explain why the paragraph is correct or incorrect in detail.\n2. 2. In ‘`&lt;verify>&lt;/verify>`’ part, you must write **Python code** in the form of ‘````python\\n{CODE}\\n````’ to verify every details that can be verified by code. You can import PyPI (i.e., ‘`sympy`’, ‘`scipy`’ and so on) to implement complicated calculation. Make sure to print the critic results in the code. Every code will be executed automatically by system. You need to analyze the ‘[Code Output]’ after code executing.\n\n>Pay attention that you must follow the format of ‘````python\\n{CODE}\\n````’ when you write the code, otherwise the code will not be executed.\n\nAfter all verifications, if you identify an error in a paragraph, return the **index** of the paragraph where the earliest error occurs\\*\\*. Otherwise, return the **index** of -1 (which typically denotes \"not found\"\\*\\*. Please put your final answer (i.e., the index) within box in the form of ‘`$\\boxed{{INDEX}}$`’.\n\nFollowing [Zheng et al. \\(2024\\)](#); [Zhang et al. \\(2025c\\)](#), we use the prompt in Table A.2 to evaluate LLM-as-a-judge methods on ProcessBench ([Zheng et al., 2024](#)).\n\n#### Evaluation prompt for LLM-as-a-judge methods on ProcessBench\n\nI will provide a math problem along with a solution. They will be formatted as follows:\n\n[Math Problem]\n\n```\n&lt;math_problem>\n...(math problem)...\n&lt;/math_problem>\n```\n\n[Solution]\n\n```\n&lt;paragraph_1>\n...(paragraph 1 of solution)...\n&lt;/paragraph_1>\n```\n\n...\n\n```\n&lt;paragraph_n>\n...(paragraph n of solution)...\n&lt;/paragraph_n>\n```\n\nYour task is to review each paragraph of the solution in sequence, analyzing, verifying, and critiquing the reasoning in detail. You need to provide the analyses and the conclusion in the following format:\n\n```\n&lt;analysis_1>\n...(analysis of paragraph 1)...\n&lt;/analysis_1>\n```...\n\n&lt;analysis\\_n>  \n ...(analysis of paragraph n)...  \n &lt;/analysis\\_n>\n\n&lt;conclusion>  \n Correct/Incorrect  \n &lt;/conclusion>\n\n\\* When you analyze each paragraph, you should use proper verification, recalculation, or reflection to indicate whether it is logically and mathematically valid. Please elaborate on the analysis process carefully.\n\n\\* If an error is detected in any paragraph, you should describe the nature and cause of the error in detail, and suggest how to correct the error or the correct approach. Once a paragraph is found to contain any error, stop further analysis of subsequent paragraphs (as they may depend on the identified error) and directly provide the conclusion of \"Incorrect.\"\n\nFor instance, given a solution of five paragraphs, if an error is found in the third paragraph, you should reply in the following format:\n\n&lt;analysis\\_1>  \n ...(analysis of paragraph 1)...  \n &lt;/analysis\\_1>\n\n&lt;analysis\\_2>  \n ...(analysis of paragraph 2)...  \n &lt;/analysis\\_2>\n\n&lt;analysis\\_3>  \n ...(analysis of paragraph 3; since an error is found here, also provide detailed critique and correction guideline)...  \n &lt;/analysis\\_3>\n\n&lt;conclusion>  \n Incorrect  \n &lt;/conclusion>\n\nNote that the analyses of paragraphs 4 and 5 should be skipped as the paragraph 3 has been found to contain an error.\n\n\\* Respond with your analyses and conclusion directly.\n\n---\n\nThe following is the math problem and the solution for you task:[Math Problem]\n\n{tagged\\_problem}\n\n[Solution]\n\n{tagged\\_response}\n\n#### Prompt for critique generation\n\n[User]:\n\nThe following is a math problem and my solution. Your task is to review and critique the paragraphs in solution step by step. Pay attention that you should not solve the problem and give the final answer. All of your task is to critique. Output your judgement of whether the paragraph is correct in the form of ‘ $\\boxed{\\{Yes|No\\}}$ ’ at the end of each paragraph verification:\n\n[Math Problem]\n\n{problem}\n\n[Solution]\n\n&lt;paragraph\\_{idx}>\n\n{solution\\_section}\n\n&lt;/paragraph\\_{idx}>\n\n## B. Additional Results\n\nWe provide full results of ProcessBench in Table 6.\n\n**Model Size.** We investigate the impact of model size on GenPRM by evaluating variants with 1.5B, 7B, and 32B parameters. As shown in Table 7, scaling the model from 1.5B to 7B parameters yields substantial performance gains (57.3  $\\rightarrow$  75.2 and 63.4  $\\rightarrow$  80.5). However, further increasing the model size to 32B provides only marginal improvements, suggesting that the 7B variant offers the best balance between efficiency and effectiveness.\n\n**Data Size.** To assess the influence of training data volume, we train GenPRM on progressively larger subsets of ProcessBench (25%, 50%, and 100% of the full dataset). Table 8 demonstrates that Pass@1 F1 scores improve rapidly with initial data increases, but the growth rate slows substantially with additional data.\n\n**Inference Tokens.** We provide statistics of the reasoning tokens per step and per response in Table 9.**Table 6:** Full results of critic models and PRMs on ProcessBench.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">Model&lt;/th>\n&lt;th colspan=\"3\">GSM8K&lt;/th>\n&lt;th colspan=\"3\">MATH&lt;/th>\n&lt;th colspan=\"3\">OlympiadBench&lt;/th>\n&lt;th colspan=\"3\">Omni-MATH&lt;/th>\n&lt;th rowspan=\"2\">Avg.&lt;br/>F1&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>Err.&lt;/th>\n&lt;th>Corr.&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;th>Err.&lt;/th>\n&lt;th>Corr.&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;th>Err.&lt;/th>\n&lt;th>Corr.&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;th>Err.&lt;/th>\n&lt;th>Corr.&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td colspan=\"14\" style=\"text-align: center;\">&lt;i>Proprietary LLMs (Critic)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GPT-4-0806&lt;/td>\n&lt;td>70.0&lt;/td>\n&lt;td>91.2&lt;/td>\n&lt;td>79.2&lt;/td>\n&lt;td>54.4&lt;/td>\n&lt;td>76.6&lt;/td>\n&lt;td>63.6&lt;/td>\n&lt;td>45.8&lt;/td>\n&lt;td>58.4&lt;/td>\n&lt;td>51.4&lt;/td>\n&lt;td>45.2&lt;/td>\n&lt;td>65.6&lt;/td>\n&lt;td>53.5&lt;/td>\n&lt;td>61.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>o1-mini&lt;/td>\n&lt;td>88.9&lt;/td>\n&lt;td>97.9&lt;/td>\n&lt;td>93.2&lt;/td>\n&lt;td>83.5&lt;/td>\n&lt;td>95.1&lt;/td>\n&lt;td>88.9&lt;/td>\n&lt;td>80.2&lt;/td>\n&lt;td>95.6&lt;/td>\n&lt;td>87.2&lt;/td>\n&lt;td>74.8&lt;/td>\n&lt;td>91.7&lt;/td>\n&lt;td>82.4&lt;/td>\n&lt;td>87.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"14\" style=\"text-align: center;\">&lt;i>Open-Source LLMs (Critic)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3-8B-Instruct&lt;/td>\n&lt;td>42.5&lt;/td>\n&lt;td>7.8&lt;/td>\n&lt;td>13.1&lt;/td>\n&lt;td>28.6&lt;/td>\n&lt;td>9.1&lt;/td>\n&lt;td>13.8&lt;/td>\n&lt;td>27.1&lt;/td>\n&lt;td>2.7&lt;/td>\n&lt;td>4.8&lt;/td>\n&lt;td>26.1&lt;/td>\n&lt;td>8.3&lt;/td>\n&lt;td>12.6&lt;/td>\n&lt;td>11.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3-70B-Instruct&lt;/td>\n&lt;td>35.7&lt;/td>\n&lt;td>96.9&lt;/td>\n&lt;td>52.2&lt;/td>\n&lt;td>13.0&lt;/td>\n&lt;td>93.3&lt;/td>\n&lt;td>22.8&lt;/td>\n&lt;td>12.0&lt;/td>\n&lt;td>92.0&lt;/td>\n&lt;td>21.2&lt;/td>\n&lt;td>11.2&lt;/td>\n&lt;td>91.7&lt;/td>\n&lt;td>20.0&lt;/td>\n&lt;td>29.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-8B-Instruct&lt;/td>\n&lt;td>44.4&lt;/td>\n&lt;td>6.2&lt;/td>\n&lt;td>10.9&lt;/td>\n&lt;td>41.9&lt;/td>\n&lt;td>2.7&lt;/td>\n&lt;td>5.1&lt;/td>\n&lt;td>32.4&lt;/td>\n&lt;td>1.5&lt;/td>\n&lt;td>2.8&lt;/td>\n&lt;td>32.0&lt;/td>\n&lt;td>0.8&lt;/td>\n&lt;td>1.6&lt;/td>\n&lt;td>5.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-70B-Instruct&lt;/td>\n&lt;td>64.3&lt;/td>\n&lt;td>89.6&lt;/td>\n&lt;td>74.9&lt;/td>\n&lt;td>35.4&lt;/td>\n&lt;td>75.6&lt;/td>\n&lt;td>48.2&lt;/td>\n&lt;td>35.1&lt;/td>\n&lt;td>69.9&lt;/td>\n&lt;td>46.7&lt;/td>\n&lt;td>30.7&lt;/td>\n&lt;td>61.8&lt;/td>\n&lt;td>41.0&lt;/td>\n&lt;td>52.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.3-70B-Instruct&lt;/td>\n&lt;td>72.5&lt;/td>\n&lt;td>96.9&lt;/td>\n&lt;td>82.9&lt;/td>\n&lt;td>43.3&lt;/td>\n&lt;td>94.6&lt;/td>\n&lt;td>59.4&lt;/td>\n&lt;td>31.0&lt;/td>\n&lt;td>94.1&lt;/td>\n&lt;td>46.7&lt;/td>\n&lt;td>28.2&lt;/td>\n&lt;td>90.5&lt;/td>\n&lt;td>43.0&lt;/td>\n&lt;td>58.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-Instruct&lt;/td>\n&lt;td>15.5&lt;/td>\n&lt;td>100.0&lt;/td>\n&lt;td>26.8&lt;/td>\n&lt;td>14.8&lt;/td>\n&lt;td>96.8&lt;/td>\n&lt;td>25.7&lt;/td>\n&lt;td>7.7&lt;/td>\n&lt;td>91.7&lt;/td>\n&lt;td>14.2&lt;/td>\n&lt;td>6.9&lt;/td>\n&lt;td>88.0&lt;/td>\n&lt;td>12.7&lt;/td>\n&lt;td>19.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-72B-Instruct&lt;/td>\n&lt;td>49.8&lt;/td>\n&lt;td>96.9&lt;/td>\n&lt;td>65.8&lt;/td>\n&lt;td>36.0&lt;/td>\n&lt;td>94.3&lt;/td>\n&lt;td>52.1&lt;/td>\n&lt;td>19.5&lt;/td>\n&lt;td>97.3&lt;/td>\n&lt;td>32.5&lt;/td>\n&lt;td>19.0&lt;/td>\n&lt;td>96.3&lt;/td>\n&lt;td>31.7&lt;/td>\n&lt;td>45.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-7B-Instruct&lt;/td>\n&lt;td>7.7&lt;/td>\n&lt;td>100.0&lt;/td>\n&lt;td>14.3&lt;/td>\n&lt;td>3.4&lt;/td>\n&lt;td>98.3&lt;/td>\n&lt;td>6.5&lt;/td>\n&lt;td>2.1&lt;/td>\n&lt;td>99.1&lt;/td>\n&lt;td>4.1&lt;/td>\n&lt;td>0.9&lt;/td>\n&lt;td>98.3&lt;/td>\n&lt;td>1.8&lt;/td>\n&lt;td>6.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-14B-Instruct&lt;/td>\n&lt;td>33.8&lt;/td>\n&lt;td>96.4&lt;/td>\n&lt;td>50.1&lt;/td>\n&lt;td>25.4&lt;/td>\n&lt;td>92.4&lt;/td>\n&lt;td>39.9&lt;/td>\n&lt;td>20.7&lt;/td>\n&lt;td>94.1&lt;/td>\n&lt;td>34.0&lt;/td>\n&lt;td>15.9&lt;/td>\n&lt;td>94.2&lt;/td>\n&lt;td>27.3&lt;/td>\n&lt;td>37.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-32B-Instruct&lt;/td>\n&lt;td>54.1&lt;/td>\n&lt;td>94.8&lt;/td>\n&lt;td>68.9&lt;/td>\n&lt;td>44.9&lt;/td>\n&lt;td>90.6&lt;/td>\n&lt;td>60.1&lt;/td>\n&lt;td>33.4&lt;/td>\n&lt;td>91.2&lt;/td>\n&lt;td>48.9&lt;/td>\n&lt;td>31.5&lt;/td>\n&lt;td>87.6&lt;/td>\n&lt;td>46.3&lt;/td>\n&lt;td>56.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-7B-Instruct&lt;/td>\n&lt;td>40.6&lt;/td>\n&lt;td>4.7&lt;/td>\n&lt;td>8.4&lt;/td>\n&lt;td>30.5&lt;/td>\n&lt;td>13.8&lt;/td>\n&lt;td>19.0&lt;/td>\n&lt;td>22.4&lt;/td>\n&lt;td>10.9&lt;/td>\n&lt;td>14.7&lt;/td>\n&lt;td>20.0&lt;/td>\n&lt;td>8.7&lt;/td>\n&lt;td>12.1&lt;/td>\n&lt;td>13.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-72B-Instruct&lt;/td>\n&lt;td>57.0&lt;/td>\n&lt;td>82.9&lt;/td>\n&lt;td>67.6&lt;/td>\n&lt;td>37.7&lt;/td>\n&lt;td>70.9&lt;/td>\n&lt;td>49.2&lt;/td>\n&lt;td>34.0&lt;/td>\n&lt;td>55.2&lt;/td>\n&lt;td>42.1&lt;/td>\n&lt;td>32.3&lt;/td>\n&lt;td>53.1&lt;/td>\n&lt;td>40.2&lt;/td>\n&lt;td>49.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct&lt;/td>\n&lt;td>40.6&lt;/td>\n&lt;td>33.2&lt;/td>\n&lt;td>36.5&lt;/td>\n&lt;td>30.8&lt;/td>\n&lt;td>45.1&lt;/td>\n&lt;td>36.6&lt;/td>\n&lt;td>26.5&lt;/td>\n&lt;td>33.9&lt;/td>\n&lt;td>29.7&lt;/td>\n&lt;td>26.2&lt;/td>\n&lt;td>28.6&lt;/td>\n&lt;td>27.4&lt;/td>\n&lt;td>32.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct&lt;/td>\n&lt;td>54.6&lt;/td>\n&lt;td>94.8&lt;/td>\n&lt;td>69.3&lt;/td>\n&lt;td>38.4&lt;/td>\n&lt;td>87.4&lt;/td>\n&lt;td>53.3&lt;/td>\n&lt;td>31.5&lt;/td>\n&lt;td>78.8&lt;/td>\n&lt;td>45.0&lt;/td>\n&lt;td>28.3&lt;/td>\n&lt;td>76.3&lt;/td>\n&lt;td>41.3&lt;/td>\n&lt;td>52.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct&lt;/td>\n&lt;td>49.3&lt;/td>\n&lt;td>97.9&lt;/td>\n&lt;td>65.6&lt;/td>\n&lt;td>36.7&lt;/td>\n&lt;td>95.8&lt;/td>\n&lt;td>53.1&lt;/td>\n&lt;td>25.3&lt;/td>\n&lt;td>95.9&lt;/td>\n&lt;td>40.0&lt;/td>\n&lt;td>24.1&lt;/td>\n&lt;td>92.5&lt;/td>\n&lt;td>38.3&lt;/td>\n&lt;td>49.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-72B-Instruct&lt;/td>\n&lt;td>62.8&lt;/td>\n&lt;td>96.9&lt;/td>\n&lt;td>76.2&lt;/td>\n&lt;td>46.3&lt;/td>\n&lt;td>93.1&lt;/td>\n&lt;td>61.8&lt;/td>\n&lt;td>38.7&lt;/td>\n&lt;td>92.6&lt;/td>\n&lt;td>54.6&lt;/td>\n&lt;td>36.6&lt;/td>\n&lt;td>90.9&lt;/td>\n&lt;td>52.2&lt;/td>\n&lt;td>61.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>QwQ-32B-Preview&lt;/td>\n&lt;td>81.6&lt;/td>\n&lt;td>95.3&lt;/td>\n&lt;td>88.0&lt;/td>\n&lt;td>78.1&lt;/td>\n&lt;td>79.3&lt;/td>\n&lt;td>78.7&lt;/td>\n&lt;td>61.4&lt;/td>\n&lt;td>54.6&lt;/td>\n&lt;td>57.8&lt;/td>\n&lt;td>55.7&lt;/td>\n&lt;td>68.0&lt;/td>\n&lt;td>61.3&lt;/td>\n&lt;td>71.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"14\" style=\"text-align: center;\">&lt;i>PRMs (1.5B)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-1.5B&lt;/td>\n&lt;td>50.2&lt;/td>\n&lt;td>71.5&lt;/td>\n&lt;td>59.0&lt;/td>\n&lt;td>37.9&lt;/td>\n&lt;td>65.2&lt;/td>\n&lt;td>48.0&lt;/td>\n&lt;td>15.4&lt;/td>\n&lt;td>26.0&lt;/td>\n&lt;td>19.3&lt;/td>\n&lt;td>13.6&lt;/td>\n&lt;td>32.8&lt;/td>\n&lt;td>19.2&lt;/td>\n&lt;td>36.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-1.5B (Pass@1)&lt;/td>\n&lt;td>37.0&lt;/td>\n&lt;td>92.7&lt;/td>\n&lt;td>52.8&lt;/td>\n&lt;td>57.1&lt;/td>\n&lt;td>80.1&lt;/td>\n&lt;td>66.6&lt;/td>\n&lt;td>47.0&lt;/td>\n&lt;td>66.5&lt;/td>\n&lt;td>55.1&lt;/td>\n&lt;td>45.2&lt;/td>\n&lt;td>68.7&lt;/td>\n&lt;td>54.5&lt;/td>\n&lt;td>57.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-1.5B (Maj@8)&lt;/td>\n&lt;td>34.8&lt;/td>\n&lt;td>97.4&lt;/td>\n&lt;td>51.3&lt;/td>\n&lt;td>64.7&lt;/td>\n&lt;td>87.7&lt;/td>\n&lt;td>74.4&lt;/td>\n&lt;td>57.2&lt;/td>\n&lt;td>76.1&lt;/td>\n&lt;td>65.3&lt;/td>\n&lt;td>51.3&lt;/td>\n&lt;td>80.1&lt;/td>\n&lt;td>62.5&lt;/td>\n&lt;td>63.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"14\" style=\"text-align: center;\">&lt;i>PRMs (7-8B)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Math-Shepherd-PRM-7B&lt;/td>\n&lt;td>32.4&lt;/td>\n&lt;td>91.7&lt;/td>\n&lt;td>47.9&lt;/td>\n&lt;td>18.0&lt;/td>\n&lt;td>82.0&lt;/td>\n&lt;td>29.5&lt;/td>\n&lt;td>15.0&lt;/td>\n&lt;td>71.1&lt;/td>\n&lt;td>24.8&lt;/td>\n&lt;td>14.2&lt;/td>\n&lt;td>73.0&lt;/td>\n&lt;td>23.8&lt;/td>\n&lt;td>31.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RLHFlow-PRM-Mistral-8B&lt;/td>\n&lt;td>33.8&lt;/td>\n&lt;td>99.0&lt;/td>\n&lt;td>50.4&lt;/td>\n&lt;td>21.7&lt;/td>\n&lt;td>72.2&lt;/td>\n&lt;td>33.4&lt;/td>\n&lt;td>8.2&lt;/td>\n&lt;td>43.1&lt;/td>\n&lt;td>13.8&lt;/td>\n&lt;td>9.6&lt;/td>\n&lt;td>45.2&lt;/td>\n&lt;td>15.8&lt;/td>\n&lt;td>28.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RLHFlow-PRM-Deepseek-8B&lt;/td>\n&lt;td>24.2&lt;/td>\n&lt;td>98.4&lt;/td>\n&lt;td>38.8&lt;/td>\n&lt;td>21.4&lt;/td>\n&lt;td>80.0&lt;/td>\n&lt;td>33.8&lt;/td>\n&lt;td>10.1&lt;/td>\n&lt;td>51.0&lt;/td>\n&lt;td>16.9&lt;/td>\n&lt;td>10.9&lt;/td>\n&lt;td>51.9&lt;/td>\n&lt;td>16.9&lt;/td>\n&lt;td>26.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-7B&lt;/td>\n&lt;td>61.8&lt;/td>\n&lt;td>82.9&lt;/td>\n&lt;td>70.8&lt;/td>\n&lt;td>43.8&lt;/td>\n&lt;td>62.2&lt;/td>\n&lt;td>53.6&lt;/td>\n&lt;td>17.9&lt;/td>\n&lt;td>31.9&lt;/td>\n&lt;td>22.9&lt;/td>\n&lt;td>14.0&lt;/td>\n&lt;td>41.9&lt;/td>\n&lt;td>21.0&lt;/td>\n&lt;td>42.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>EurusPRM-Stage1&lt;/td>\n&lt;td>46.9&lt;/td>\n&lt;td>42.0&lt;/td>\n&lt;td>44.3&lt;/td>\n&lt;td>33.3&lt;/td>\n&lt;td>38.2&lt;/td>\n&lt;td>35.6&lt;/td>\n&lt;td>23.9&lt;/td>\n&lt;td>19.8&lt;/td>\n&lt;td>21.7&lt;/td>\n&lt;td>21.9&lt;/td>\n&lt;td>24.5&lt;/td>\n&lt;td>23.1&lt;/td>\n&lt;td>31.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>EurusPRM-Stage2&lt;/td>\n&lt;td>51.2&lt;/td>\n&lt;td>44.0&lt;/td>\n&lt;td>47.3&lt;/td>\n&lt;td>36.4&lt;/td>\n&lt;td>35.0&lt;/td>\n&lt;td>35.7&lt;/td>\n&lt;td>25.7&lt;/td>\n&lt;td>18.0&lt;/td>\n&lt;td>21.2&lt;/td>\n&lt;td>23.1&lt;/td>\n&lt;td>19.1&lt;/td>\n&lt;td>20.9&lt;/td>\n&lt;td>31.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-Math-Shepherd&lt;/td>\n&lt;td>46.4&lt;/td>\n&lt;td>95.9&lt;/td>\n&lt;td>62.5&lt;/td>\n&lt;td>18.9&lt;/td>\n&lt;td>96.6&lt;/td>\n&lt;td>31.6&lt;/td>\n&lt;td>7.4&lt;/td>\n&lt;td>93.8&lt;/td>\n&lt;td>13.7&lt;/td>\n&lt;td>4.0&lt;/td>\n&lt;td>95.0&lt;/td>\n&lt;td>7.7&lt;/td>\n&lt;td>28.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-PRM800K&lt;/td>\n&lt;td>53.1&lt;/td>\n&lt;td>95.3&lt;/td>\n&lt;td>68.2&lt;/td>\n&lt;td>48.0&lt;/td>\n&lt;td>90.1&lt;/td>\n&lt;td>62.6&lt;/td>\n&lt;td>35.7&lt;/td>\n&lt;td>87.3&lt;/td>\n&lt;td>50.7&lt;/td>\n&lt;td>29.8&lt;/td>\n&lt;td>86.1&lt;/td>\n&lt;td>44.3&lt;/td>\n&lt;td>56.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-PRM-7B&lt;/td>\n&lt;td>72.0&lt;/td>\n&lt;td>96.4&lt;/td>\n&lt;td>82.4&lt;/td>\n&lt;td>68.0&lt;/td>\n&lt;td>90.4&lt;/td>\n&lt;td>77.6&lt;/td>\n&lt;td>55.7&lt;/td>\n&lt;td>85.5&lt;/td>\n&lt;td>67.5&lt;/td>\n&lt;td>55.2&lt;/td>\n&lt;td>83.0&lt;/td>\n&lt;td>66.3&lt;/td>\n&lt;td>73.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RetrievalPRM-7B&lt;/td>\n&lt;td>64.7&lt;/td>\n&lt;td>88.1&lt;/td>\n&lt;td>74.6&lt;/td>\n&lt;td>67.2&lt;/td>\n&lt;td>75.6&lt;/td>\n&lt;td>71.1&lt;/td>\n&lt;td>56.0&lt;/td>\n&lt;td>65.2&lt;/td>\n&lt;td>60.2&lt;/td>\n&lt;td>52.8&lt;/td>\n&lt;td>62.7&lt;/td>\n&lt;td>57.3&lt;/td>\n&lt;td>65.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Universal-PRM-7B&lt;/td>\n&lt;td>-&lt;/td>\n&lt;td>-&lt;/td>\n&lt;td>85.8&lt;/td>\n&lt;td>-&lt;/td>\n&lt;td>-&lt;/td>\n&lt;td>77.7&lt;/td>\n&lt;td>-&lt;/td>\n&lt;td>-&lt;/td>\n&lt;td>67.6&lt;/td>\n&lt;td>-&lt;/td>\n&lt;td>-&lt;/td>\n&lt;td>66.4&lt;/td>\n&lt;td>74.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Direct Generative PRM-7B&lt;/td>\n&lt;td>52.7&lt;/td>\n&lt;td>81.4&lt;/td>\n&lt;td>63.9&lt;/td>\n&lt;td>55.9&lt;/td>\n&lt;td>80.0&lt;/td>\n&lt;td>65.8&lt;/td>\n&lt;td>44.8&lt;/td>\n&lt;td>69.6&lt;/td>\n&lt;td>54.5&lt;/td>\n&lt;td>45.5&lt;/td>\n&lt;td>72.6&lt;/td>\n&lt;td>55.9&lt;/td>\n&lt;td>60.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-7B (Pass@1)&lt;/td>\n&lt;td>67.7&lt;/td>\n&lt;td>94.0&lt;/td>\n&lt;td>78.7&lt;/td>\n&lt;td>74.6&lt;/td>\n&lt;td>87.0&lt;/td>\n&lt;td>80.3&lt;/td>\n&lt;td>68.3&lt;/td>\n&lt;td>76.6&lt;/td>\n&lt;td>72.2&lt;/td>\n&lt;td>63.5&lt;/td>\n&lt;td>77.4&lt;/td>\n&lt;td>69.8&lt;/td>\n&lt;td>75.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-7B (Maj@8)&lt;/td>\n&lt;td>69.6&lt;/td>\n&lt;td>96.9&lt;/td>\n&lt;td>81.0&lt;/td>\n&lt;td>80.5&lt;/td>\n&lt;td>91.6&lt;/td>\n&lt;td>85.7&lt;/td>\n&lt;td>74.0&lt;/td>\n&lt;td>83.5&lt;/td>\n&lt;td>78.4&lt;/td>\n&lt;td>70.0&lt;/td>\n&lt;td>85.1&lt;/td>\n&lt;td>76.8&lt;/td>\n&lt;td>80.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"14\" style=\"text-align: center;\">&lt;i>PRMs (14-72B)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Dyve-14B&lt;/td>\n&lt;td>-&lt;/td>\n&lt;td>-&lt;/td>\n&lt;td>68.5&lt;/td>\n&lt;td>-&lt;/td>\n&lt;td>-&lt;/td>\n&lt;td>58.3&lt;/td>\n&lt;td>-&lt;/td>\n&lt;td>-&lt;/td>\n&lt;td>49.0&lt;/td>\n&lt;td>-&lt;/td>\n&lt;td>-&lt;/td>\n&lt;td>47.2&lt;/td>\n&lt;td>55.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-PRM-72B&lt;/td>\n&lt;td>78.7&lt;/td>\n&lt;td>97.9&lt;/td>\n&lt;td>87.3&lt;/td>\n&lt;td>74.2&lt;/td>\n&lt;td>88.2&lt;/td>\n&lt;td>80.6&lt;/td>\n&lt;td>67.9&lt;/td>\n&lt;td>82.0&lt;/td>\n&lt;td>74.3&lt;/td>\n&lt;td>64.8&lt;/td>\n&lt;td>78.8&lt;/td>\n&lt;td>71.1&lt;/td>\n&lt;td>78.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-32B (Pass@1)&lt;/td>\n&lt;td>73.1&lt;/td>\n&lt;td>96.4&lt;/td>\n&lt;td>83.1&lt;/td>\n&lt;td>79.4&lt;/td>\n&lt;td>84.1&lt;/td>\n&lt;td>81.7&lt;/td>\n&lt;td>73.4&lt;/td>\n&lt;td>72.2&lt;/td>\n&lt;td>72.8&lt;/td>\n&lt;td>70.3&lt;/td>\n&lt;td>75.5&lt;/td>\n&lt;td>72.8&lt;/td>\n&lt;td>77.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-32B (Maj@8)&lt;/td>\n&lt;td>74.9&lt;/td>\n&lt;td>98.5&lt;/td>\n&lt;td>85.1&lt;/td>\n&lt;td>84.0&lt;/td>\n&lt;td>88.7&lt;/td>\n&lt;td>86.3&lt;/td>\n&lt;td>79.0&lt;/td>\n&lt;td>78.8&lt;/td>\n&lt;td>78.9&lt;/td>\n&lt;td>76.3&lt;/td>\n&lt;td>84.2&lt;/td>\n&lt;td>80.1&lt;/td>\n&lt;td>82.6&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n## C. Cases\n\nIn this section, we analyze two cases to have a better understanding of GenPRM. The case in Figure 5 shows that the code execution feedback can correct the mistakes in CoT and enhance the process supervision abilities of GenPRM. The case in Figure 6 demonstrates that GenPRM provides accurate process supervision with CoT reasoning only.**Table 7:** Evaluation results of GenPRM with different sizes on ProcessBench.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Model Size&lt;/th>\n&lt;th>Metric&lt;/th>\n&lt;th>GSM8K&lt;/th>\n&lt;th>MATH&lt;/th>\n&lt;th>OlympiadBench&lt;/th>\n&lt;th>Omni-MATH&lt;/th>\n&lt;th>Avg.&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td rowspan=\"2\">1.5B&lt;/td>\n&lt;td>Pass@1&lt;/td>\n&lt;td>52.8&lt;/td>\n&lt;td>66.6&lt;/td>\n&lt;td>55.1&lt;/td>\n&lt;td>54.5&lt;/td>\n&lt;td>57.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Maj@8&lt;/td>\n&lt;td>81.0&lt;/td>\n&lt;td>74.4&lt;/td>\n&lt;td>65.3&lt;/td>\n&lt;td>62.5&lt;/td>\n&lt;td>63.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"2\">7B&lt;/td>\n&lt;td>Pass@1&lt;/td>\n&lt;td>78.7&lt;/td>\n&lt;td>80.3&lt;/td>\n&lt;td>72.2&lt;/td>\n&lt;td>69.8&lt;/td>\n&lt;td>75.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Maj@8&lt;/td>\n&lt;td>81.0&lt;/td>\n&lt;td>85.7&lt;/td>\n&lt;td>78.4&lt;/td>\n&lt;td>76.8&lt;/td>\n&lt;td>80.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"2\">32B&lt;/td>\n&lt;td>Pass@1&lt;/td>\n&lt;td>83.1&lt;/td>\n&lt;td>81.7&lt;/td>\n&lt;td>72.8&lt;/td>\n&lt;td>72.8&lt;/td>\n&lt;td>77.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Maj@8&lt;/td>\n&lt;td>85.1&lt;/td>\n&lt;td>86.3&lt;/td>\n&lt;td>78.9&lt;/td>\n&lt;td>80.1&lt;/td>\n&lt;td>82.6&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 8:** Evaluation results of GenPRM with different proportions of training data on ProcessBench.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Data Size&lt;/th>\n&lt;th>Metric&lt;/th>\n&lt;th>GSM8K&lt;/th>\n&lt;th>MATH&lt;/th>\n&lt;th>OlympiadBench&lt;/th>\n&lt;th>Omni-MATH&lt;/th>\n&lt;th>Avg.&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>25%&lt;/td>\n&lt;td>Pass@1&lt;/td>\n&lt;td>71.8&lt;/td>\n&lt;td>78.0&lt;/td>\n&lt;td>68.9&lt;/td>\n&lt;td>68.2&lt;/td>\n&lt;td>71.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>50%&lt;/td>\n&lt;td>Pass@1&lt;/td>\n&lt;td>78.1&lt;/td>\n&lt;td>80.6&lt;/td>\n&lt;td>71.5&lt;/td>\n&lt;td>67.6&lt;/td>\n&lt;td>74.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>100%&lt;/td>\n&lt;td>Pass@1&lt;/td>\n&lt;td>78.7&lt;/td>\n&lt;td>80.3&lt;/td>\n&lt;td>72.2&lt;/td>\n&lt;td>69.8&lt;/td>\n&lt;td>75.2&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 9:** Statistics of the output tokens of GenPRM.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>&lt;/th>\n&lt;th>MATH&lt;/th>\n&lt;th>AMC23&lt;/th>\n&lt;th>AIME24&lt;/th>\n&lt;th>Minerva Math&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Step&lt;/td>\n&lt;td>344.7&lt;/td>\n&lt;td>416.2&lt;/td>\n&lt;td>432.5&lt;/td>\n&lt;td>503.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Response&lt;/td>\n&lt;td>2771.4&lt;/td>\n&lt;td>3200.2&lt;/td>\n&lt;td>4112.9&lt;/td>\n&lt;td>4877.1&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>**Problem:****Simplify  $\\cos 54^\\circ \\cos 4^\\circ - \\cos 36^\\circ \\cos 86^\\circ$ .****Enter your answer is a trigonometric function evaluated at an integer, such as \"sin 7\". (The system will assume that the angle is in degrees.)****System:**\n\nYou are a math teacher. Your task is to review and critique the paragraphs in solution step by step.\n\n**User (Turn 1):**\n\nTo simplify the expression  $\\cos 54^\\circ \\cos 4^\\circ - \\cos 36^\\circ \\cos 86^\\circ$ , we start by using the identity  $\\cos(90^\\circ - x) = \\sin x$ . This allows us to rewrite  $\\cos 86^\\circ$  as  $\\sin 2^\\circ$ . Thus, the expression becomes:  $\\cos 54^\\circ \\cos 4^\\circ - \\cos 36^\\circ \\sin 2^\\circ$\n\n**Assistant (Turn 1):**\n\n&lt;analyze>\n\nThe first paragraph uses the identity  $\\cos(90^\\circ - x) = \\sin(x)$  to rewrite  $\\cos(86^\\circ)$  as  $\\sin(2^\\circ)$ . This is correct because  $86^\\circ$  is  $90^\\circ - 2^\\circ$ , so substituting  $x = 2^\\circ$  gives  $\\cos(86^\\circ) = \\sin(2^\\circ)$ . The substitution is valid here. The expression is correctly transformed into  $\\cos 54^\\circ \\cos 4^\\circ - \\cos 36^\\circ \\sin 2^\\circ$ . This step is accurate.\n\n&lt;/analyze>\n\n&lt;verify>\n\n```\nimport math\nimport sympy as sp\n# Define the angles in degrees\nangle1 = 54\nangle2 = 4\nangle3 = 36\nangle4 = 86\n# Compute cos(54°) and cos(86°) using sympy's cos function\ncos54 = sp.cos(sp.rad(angle1))\ncos86 = sp.cos(sp.rad(angle4))\nsin2 = sp.sin(sp.rad(2))\ncos36 = sp.cos(sp.rad(angle3))\n# Check if cos86° equals sin2°\nis_equal = sp.simplify(cos86 - sin2) == 0\nprint(f\"cos(86°) equals sin(2°)? {is_equal}\")\n# Check the transformed expression\ntransformed = sp.cos(sp.rad(angle1)) * sp.cos(sp.rad(angle2)) - sp.cos(sp.rad(angle3)) * sin2\noriginal = sp.cos(sp.rad(angle1)) * sp.cos(sp.rad(angle2)) - sp.cos(sp.rad(angle3)) * sp.cos(sp.rad(angle4))\nprint(f\"Original expression: {original}\")\nprint(f\"Transformed expression: {transformed}\")\n```\n\n[Code Output]\n\n```\ncos(86°) equals sin(2°)? False\nOriginal expression: -(1/4 + sqrt(5)/4)*cos(43*pi/90) + sqrt(5)/8 - sqrt(5)/8*cos(pi/45)\nTransformed expression: -(1/4 + sqrt(5)/4)*sin(pi/90) + sqrt(5)/8 - sqrt(5)/8*cos(pi/45)\n```\n\nWait, the output shows that  $\\cos(86^\\circ)$  is not exactly equal to  $\\sin(2^\\circ)$  in terms of exact symbolic comparison. However, numerically they are equal. Let me check with numerical values:\n\n```\nimport math\ncos86 = math.cos(math.radians(86))\nsin2 = math.sin(math.radians(2))\nprint(\"Are they equal numerically?\", math.isclose(cos86, sin2))\n```\n\n[Code Output]\n\nAre they equal numerically? False\n\nHmm, this is unexpected. Wait, maybe due to floating-point precision? Let me compute  $\\cos(86^\\circ)$  and  $\\sin(2^\\circ)$  numerically and see if they are equal.\n\nWait, let's compute  $\\cos(86^\\circ)$  and  $\\sin(2^\\circ)$ :\n\n```\ncos(86°) ≈ cos(86) ≈ 0.06975647374412537\nsin(2°) ≈ 0.03489949670250097\n```\n\nThese are not equal. So the initial assumption that  $\\cos(86^\\circ) = \\sin(2^\\circ)$  is incorrect. Therefore, the paragraph 1 is wrong. The error is in the trigonometric identity used here.\n\nWait, but according to the identity  $\\cos(90^\\circ - x) = \\sin(x)$ , so  $\\cos(86^\\circ) = \\cos(90^\\circ - 2^\\circ) = \\sin(2^\\circ)$ . However, numerically they are not equal. So there is a mistake here. The paragraph incorrectly applied the identity, leading to an incorrect substitution. The correct substitution should be  $\\cos(86^\\circ) = \\sin(2^\\circ)$ , but numerically they are not equal. So the error is in paragraph 1.\n\nWait, but maybe the problem is that the identity is correct, but the numerical check is wrong? Let me verify:\n\nWait,  $\\cos(86^\\circ)$  is  $\\cos(90^\\circ - 4^\\circ) = \\sin(4^\\circ)$ , not  $2^\\circ$ . Wait, no, wait:  $\\cos(90^\\circ - x) = \\sin(x)$ . So if angle is  $86^\\circ$ , then  $90^\\circ - 86^\\circ = 4^\\circ$ , so  $\\cos(86^\\circ) = \\sin(4^\\circ)$ . Wait, that's the opposite of what the paragraph says. The paragraph said  $\\cos(86^\\circ) = \\sin(2^\\circ)$ , but according to the identity, it should be  $\\sin(4^\\circ)$ . So that's the mistake. The paragraph incorrectly used  $2^\\circ$  instead of  $4^\\circ$ . That's a critical error.\n\nSo paragraph 1 is wrong because it used  $2^\\circ$  instead of  $4^\\circ$  in the substitution. Therefore, the code verification shows that the substitution is incorrect, leading to an incorrect expression. The error is in paragraph 1.\n\nSo the first paragraph is incorrect.\n\n&lt;/verify>\n\n&lt;output>\n\nJudgement:  $\\boxed{\\text{No}}$ \n\n&lt;/output>\n\nFigure 5: The first case of GenPRM.**Problem:****Compute the distance between the two foci of the ellipse  $x^2 + 4y^2 = 9$ .****System:**\n\nYou are a math teacher. Your task is to review and critique the paragraphs in solution step by step.\n\n-----\n\n**User (Turn 1):**\n\nSince  $x^2 + 4y^2 = 9$ , we divide both sides by 9 to obtain  $\\frac{x^2}{9} + \\frac{4y^2}{9} = 1$ .\n\n**Assistant (Turn 1):****&lt;analyze>**\n\nLet's analyze the Paragraph 1 step by step: 1. The original equation is given as  $x^2 + 4y^2 = 9$ . Dividing both sides by 9 is correct because the standard form of an ellipse requires the right-hand side to be 1. This results in  $\\frac{x^2}{9} + \\frac{4y^2}{9} = 1$ . 2. The semi-major axis  $a$  is correctly identified as 3 because the denominator under  $x^2$  is 9, so  $a^2 = 9$  leading to  $a = 3$ . 3. The semi-minor axis  $b$  is calculated as  $\\frac{3}{2}$ . Since the coefficient under  $y^2$  after division is  $\\frac{4}{9}$ , so  $b^2 = \\frac{9}{4}$  (since the denominator under  $y^2$  would be  $\\frac{9}{4}$ ), but wait, actually the equation after division is  $\\frac{x^2}{9} + \\frac{y^2}{(9/4)} = 1$ , so  $b^2 = 9/4$ , so  $b = 3/2$ . That part is correct. **So paragraph 1 is correct.**\n\n**&lt;/analyze>****&lt;output>**\n\nJudgement:  **$\\boxed{\\text{Yes}}$**\n\n**&lt;/output>****User (Turn 2)**\n\nThe distance between the two foci of an ellipse with semi-major axis  $a$  and semi-minor axis  $b$  is given by  $2c$ , where\n\n **$c = \\sqrt{a^2 - b^2} = \\sqrt{3^2 - \\left(\\frac{3}{2}\\right)^2} = \\sqrt{\\frac{27}{4} - \\frac{9}{4}} = \\sqrt{\\frac{18}{4}}$** \n **$\\frac{3\\sqrt{2}}{2}$** \n **$\\frac{3\\sqrt{2}}{2}$** \n**Assistant (Turn 2)****&lt;analyze>**\n\nLet's analyze the Paragraph 2 step by step: 1. The formula for the distance between foci is  $2c$ , where  $c = \\sqrt{a^2 - b^2}$ . This is correct for an ellipse with major axis along the x-axis (since the denominator under  $x^2$  is larger). 2. Plugging in  $a = 3$  and  $b = 3/2$ :\n\n$a^2 = 9$ ,  $b^2 = (3/2)^2 = 9/4$\n\n$c = \\sqrt{9 - 9/4} = \\sqrt{27/4}$  (Wait, 9 is 36/4, so  $36/4 - 9/4 = 27/4$ . So  $\\sqrt{27/4}$  is  $(3\\sqrt{3})/2$ , but in the solution they have  $\\sqrt{27/4 - 9/4} = \\sqrt{18/4}$ . Wait, hold on, that's an error! Wait,  $9 - 9/4 = 27/4$ , not  $18/4$ . Wait, 9 is 36/4, so  $36/4 - 9/4 = 27/4$ . Therefore  $\\sqrt{27/4}$  is  $(3\\sqrt{3})/2$ . But in the solution, they wrote  $\\sqrt{27/4 - 9/4} = \\sqrt{18/4}$ . Wait, that's wrong. The calculation inside the sqrt should be  $27/4$ , not  $18/4$ . So the error is here. Wait, but let me check again. Wait, the user's solution says  $\\sqrt{27/4 - 9/4}$  which is  $\\sqrt{18/4}$ . Wait, that's a mistake. So the error is in the arithmetic here. The correct calculation should be  $9 - (3/2)^2 = 9 - 2.25 = 6.75$ , which is  $27/4$ . So  $\\sqrt{27/4}$  is  $3\\sqrt{3}/2 \\approx 2.598$ , but the solution says  $\\sqrt{18/4}$  which is  $\\sqrt{4.5} \\approx 2.121$ . Therefore, there is an arithmetic mistake here. Therefore, paragraph 2 is incorrect. Wait, but maybe I made a mistake here? Let me recheck. The user's solution says:\n\n\" $c = \\sqrt{3^2 - (3/2)^2} = \\sqrt{27/4 - 9/4} = \\sqrt{18/4} = 3\\sqrt{2}/2$ .\"\n\nWait, 3 squared is 9, not 27. Wait, hold on, the user wrote  $3^2 - (3/2)^2 = 9 - (9/4) = (36/4 - 9/4) = 27/4$ . But in their calculation, they wrote  $\\sqrt{27/4 - 9/4}$  which would be  $\\sqrt{18/4}$ . Wait, that's a mistake. The correct expression is  $\\sqrt{9 - 9/4} = \\sqrt{27/4}$ . Therefore, the step where they wrote  $\\sqrt{27/4 - 9/4}$  is incorrect. The correct calculation is  $\\sqrt{9 - 9/4} = \\sqrt{27/4}$ . So the error is in the arithmetic here. **Therefore, paragraph 2 is incorrect.**\n\n**&lt;/analyze>****&lt;output>**\n\nJudgement:  **$\\boxed{\\text{No}}$**\n\n**&lt;/output>**\n\nFigure 6: The second case of GenPRM.\n",
    "durationMs": 928,
    "url": "https://huggingface.co/papers/2504.00891"
  },
  "sourceToolAssistantUUID": "1891e816-1b5c-482e-a265-1ee101444438",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
`````

</details>

---

### Runtime record

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-28 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "68422d5f-eb09-4767-9d08-aa2b8857f6e5",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze GenPRM paper innovation and research craft",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5"
}
```

---

### Tool call

_source line 33 · 2026-05-28T05:06:57.351Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XCD7jCCUtWAJ24xxpsZ6A7`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/d13ca6d2-ab23-4990-8414-c3096bb93ab5/tool-results/toolu_01GSHgkEVx98FPEy2wEtpX5x.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68422d5f-eb09-4767-9d08-aa2b8857f6e5",
  "isSidechain": false,
  "requestId": "req_011CbUPMtW4mNYuxiNG4ik3H",
  "type": "assistant",
  "uuid": "78031add-08e3-4a7c-98b7-6d0eb30b1da8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FyFYnBhVS3kvGd9zVjpWRE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7436,
      "cache_read_input_tokens": 15916,
      "output_tokens": 128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7436,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 128,
          "cache_read_input_tokens": 15916,
          "cache_creation_input_tokens": 7436,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7436
          },
          "type": "message"
        }
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

_source line 34 · 2026-05-28T05:06:57.851Z_

<details><summary>↩ Tool result · reported error · `toolu_01XCD7jCCUtWAJ24xxpsZ6A7`</summary>

```text
File content (37144 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "78031add-08e3-4a7c-98b7-6d0eb30b1da8",
  "isSidechain": false,
  "promptId": "a37d06a3-a1b2-4f5b-ba56-06aaf32ddf9c",
  "type": "user",
  "uuid": "33a45f5a-b173-40d9-a954-06d6d45efe70",
  "toolUseResult": "Error: File content (37144 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "78031add-08e3-4a7c-98b7-6d0eb30b1da8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-28T05:07:01.204Z_

<details open><summary>🔧 Tool call — Read · `toolu_01N6iC7HTKSo78tB5eBKTFkw`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/d13ca6d2-ab23-4990-8414-c3096bb93ab5/tool-results/toolu_01GSHgkEVx98FPEy2wEtpX5x.txt",
  "limit": 800,
  "offset": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33a45f5a-b173-40d9-a954-06d6d45efe70",
  "isSidechain": false,
  "requestId": "req_011CbUPNRPSQGDxEkfXFKszj",
  "type": "assistant",
  "uuid": "abf43550-7b71-4962-89c9-4b62e163ab36",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SDkTHVBTZysvWFZvENyfjo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 191,
      "cache_read_input_tokens": 23352,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 191,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 23352,
          "cache_creation_input_tokens": 191,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 191
          },
          "type": "message"
        }
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

_source line 36 · 2026-05-28T05:07:01.544Z_

<details><summary>↩ Tool result · `toolu_01N6iC7HTKSo78tB5eBKTFkw`</summary>

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
500	&lt;/tr>
501	&lt;tr>
502	&lt;td>DeepSeek-R1-Distill-7B&lt;/td>
503	&lt;td>69.1&lt;/td>
504	&lt;td>17.9&lt;/td>
505	&lt;td>84.6&lt;/td>
506	&lt;td>33.0&lt;/td>
507	&lt;td>51.2&lt;/td>
508	&lt;td>50.6&lt;/td>
509	&lt;td>6.3&lt;/td>
510	&lt;td>77.7&lt;/td>
511	&lt;td>34.7&lt;/td>
512	&lt;td>42.3&lt;/td>
513	&lt;td>46.8&lt;/td>
514	&lt;/tr>
515	&lt;tr>
516	&lt;td>GenPRM-7B&lt;/td>
517	&lt;td>&lt;b>74.1&lt;/b>&lt;/td>
518	&lt;td>&lt;b>19.6&lt;/b>&lt;/td>
519	&lt;td>&lt;b>86.0&lt;/b>&lt;/td>
520	&lt;td>&lt;b>35.3&lt;/b>&lt;/td>
521	&lt;td>&lt;b>53.8&lt;/b>&lt;/td>
522	&lt;td>&lt;b>57.5&lt;/b>&lt;/td>
523	&lt;td>&lt;b>8.3&lt;/b>&lt;/td>
524	&lt;td>&lt;b>80.6&lt;/b>&lt;/td>
525	&lt;td>&lt;b>36.5&lt;/b>&lt;/td>
526	&lt;td>&lt;b>45.7&lt;/b>&lt;/td>
527	&lt;td>&lt;b>49.8&lt;/b>&lt;/td>
528	&lt;/tr>
529	&lt;tr>
530	&lt;td colspan="12" style="text-align: center;">&lt;i>Turn 2&lt;/i>&lt;/td>
531	&lt;/tr>
532	&lt;tr>
533	&lt;td>Generator&lt;/td>
534	&lt;td>66.6&lt;/td>
535	&lt;td>18.0&lt;/td>
536	&lt;td>84.8&lt;/td>
537	&lt;td>31.6&lt;/td>
538	&lt;td>50.3&lt;/td>
539	&lt;td>49.8&lt;/td>
540	&lt;td>8.0&lt;/td>
541	&lt;td>76.9&lt;/td>
542	&lt;td>31.8&lt;/td>
543	&lt;td>41.6&lt;/td>
544	&lt;td>46.0&lt;/td>
545	&lt;/tr>
546	&lt;tr>
547	&lt;td>DeepSeek-R1-Distill-7B&lt;/td>
548	&lt;td>70.9&lt;/td>
549	&lt;td>18.3&lt;/td>
550	&lt;td>85.0&lt;/td>
551	&lt;td>33.5&lt;/td>
552	&lt;td>51.9&lt;/td>
553	&lt;td>51.9&lt;/td>
554	&lt;td>7.9&lt;/td>
555	&lt;td>78.1&lt;/td>
556	&lt;td>32.8&lt;/td>
557	&lt;td>42.7&lt;/td>
558	&lt;td>47.3&lt;/td>
559	&lt;/tr>
560	&lt;tr>
561	&lt;td>GenPRM-7B&lt;/td>
562	&lt;td>&lt;b>75.0&lt;/b>&lt;/td>
563	&lt;td>&lt;b>21.3&lt;/b>&lt;/td>
564	&lt;td>&lt;b>86.9&lt;/b>&lt;/td>
565	&lt;td>&lt;b>35.6&lt;/b>&lt;/td>
566	&lt;td>&lt;b>54.7&lt;/b>&lt;/td>
567	&lt;td>&lt;b>59.4&lt;/b>&lt;/td>
568	&lt;td>&lt;b>9.6&lt;/b>&lt;/td>
569	&lt;td>&lt;b>82.2&lt;/b>&lt;/td>
570	&lt;td>&lt;b>35.0&lt;/b>&lt;/td>
571	&lt;td>&lt;b>46.6&lt;/b>&lt;/td>
572	&lt;td>&lt;b>50.7&lt;/b>&lt;/td>
573	&lt;/tr>
574	&lt;tr>
575	&lt;td colspan="12" style="text-align: center;">&lt;i>Turn 3&lt;/i>&lt;/td>
576	&lt;/tr>
577	&lt;tr>
578	&lt;td>Generator&lt;/td>
579	&lt;td>67.8&lt;/td>
580	&lt;td>18.1&lt;/td>
581	&lt;td>85.0&lt;/td>
582	&lt;td>32.1&lt;/td>
583	&lt;td>50.8&lt;/td>
584	&lt;td>49.7&lt;/td>
585	&lt;td>8.1&lt;/td>
586	&lt;td>77.1&lt;/td>
587	&lt;td>30.8&lt;/td>
588	&lt;td>41.4&lt;/td>
589	&lt;td>46.1&lt;/td>
590	&lt;/tr>
591	&lt;tr>
592	&lt;td>DeepSeek-R1-Distill-7B&lt;/td>
593	&lt;td>69.6&lt;/td>
594	&lt;td>18.8&lt;/td>
595	&lt;td>85.0&lt;/td>
596	&lt;td>33.4&lt;/td>
597	&lt;td>51.7&lt;/td>
598	&lt;td>51.9&lt;/td>
599	&lt;td>8.3&lt;/td>
600	&lt;td>78.2&lt;/td>
601	&lt;td>32.7&lt;/td>
602	&lt;td>42.7&lt;/td>
603	&lt;td>47.2&lt;/td>
604	&lt;/tr>
605	&lt;tr>
606	&lt;td>GenPRM-7B&lt;/td>
607	&lt;td>&lt;b>76.2&lt;/b>&lt;/td>
608	&lt;td>&lt;b>22.8&lt;/b>&lt;/td>
609	&lt;td>&lt;b>86.7&lt;/b>&lt;/td>
610	&lt;td>&lt;b>36.0&lt;/b>&lt;/td>
611	&lt;td>&lt;b>55.4&lt;/b>&lt;/td>
612	&lt;td>&lt;b>62.7&lt;/b>&lt;/td>
613	&lt;td>&lt;b>9.3&lt;/b>&lt;/td>
614	&lt;td>&lt;b>82.9&lt;/b>&lt;/td>
615	&lt;td>&lt;b>34.9&lt;/b>&lt;/td>
616	&lt;td>&lt;b>47.5&lt;/b>&lt;/td>
617	&lt;td>&lt;b>51.5&lt;/b>&lt;/td>
618	&lt;/tr>
619	&lt;/tbody>
620	&lt;/table>
621	
622	**Table 3:** Results of GenPRM with different label estimation method and threshold on ProcessBench, reported with Pass@1. The best results are shown in **bold**.
623	
624	&lt;table border="1">
625	&lt;thead>
626	&lt;tr>
627	&lt;th>Estimation Method&lt;/th>
628	&lt;th>Positive Label Criterion&lt;/th>
629	&lt;th>GSM8K&lt;/th>
630	&lt;th>MATH&lt;/th>
631	&lt;th>Olympiad Bench&lt;/th>
632	&lt;th>Omni-MATH&lt;/th>
633	&lt;th>Avg.&lt;/th>
634	&lt;/tr>
635	&lt;/thead>
636	&lt;tbody>
637	&lt;tr>
638	&lt;td>&lt;math>P_t = MC(s_t, a_t)&lt;/math> (hard label)&lt;/td>
639	&lt;td>&lt;math>P_t &gt; 0&lt;/math>&lt;/td>
640	&lt;td>72.9&lt;/td>
641	&lt;td>78.9&lt;/td>
642	&lt;td>&lt;b>73.2&lt;/b>&lt;/td>
643	&lt;td>68.0&lt;/td>
644	&lt;td>73.2&lt;/td>
645	&lt;/tr>
646	&lt;tr>
647	&lt;td rowspan="3">&lt;math>P_t = MC(s_t, a_t) - MC(s_t)&lt;/math>&lt;/td>
648	&lt;td>&lt;math>P_t \geq -0.1&lt;/math>&lt;/td>
649	&lt;td>77.3&lt;/td>
650	&lt;td>79.9&lt;/td>
651	&lt;td>70.8&lt;/td>
652	&lt;td>68.5&lt;/td>
653	&lt;td>74.1&lt;/td>
654	&lt;/tr>
655	&lt;tr>
656	&lt;td>&lt;math>P_t \geq -0.3&lt;/math>&lt;/td>
657	&lt;td>76.8&lt;/td>
658	&lt;td>79.6&lt;/td>
659	&lt;td>71.1&lt;/td>
660	&lt;td>69.0&lt;/td>
661	&lt;td>74.1&lt;/td>
662	&lt;/tr>
663	&lt;tr>
664	&lt;td>&lt;math>P_t \geq -0.5&lt;/math>&lt;/td>
665	&lt;td>75.8&lt;/td>
666	&lt;td>80.2&lt;/td>
667	&lt;td>72.8&lt;/td>
668	&lt;td>68.6&lt;/td>
669	&lt;td>74.3&lt;/td>
670	&lt;/tr>
671	&lt;tr>
672	&lt;td rowspan="4">&lt;math>P_t = \frac{MC(s_t, a_t)}{MC(s_t)}&lt;/math>&lt;/td>
673	&lt;td>&lt;math>P_t \geq 0.1&lt;/math>&lt;/td>
674	&lt;td>74.8&lt;/td>
675	&lt;td>78.7&lt;/td>
676	&lt;td>71.6&lt;/td>
677	&lt;td>68.7&lt;/td>
678	&lt;td>73.5&lt;/td>
679	&lt;/tr>
680	&lt;tr>
681	&lt;td>&lt;math>P_t \geq 0.5&lt;/math>&lt;/td>
682	&lt;td>75.7&lt;/td>
683	&lt;td>79.2&lt;/td>
684	&lt;td>70.4&lt;/td>
685	&lt;td>68.5&lt;/td>
686	&lt;td>73.5&lt;/td>
687	&lt;/tr>
688	&lt;tr>
689	&lt;td>&lt;math>P_t \geq 0.8&lt;/math>&lt;/td>
690	&lt;td>&lt;b>78.7&lt;/b>&lt;/td>
691	&lt;td>&lt;b>80.3&lt;/b>&lt;/td>
692	&lt;td>72.2&lt;/td>
693	&lt;td>&lt;b>69.8&lt;/b>&lt;/td>
694	&lt;td>&lt;b>75.2&lt;/b>&lt;/td>
695	&lt;/tr>
696	&lt;tr>
697	&lt;td>&lt;math>P_t \geq 1.0&lt;/math>&lt;/td>
698	&lt;td>76.4&lt;/td>
699	&lt;td>77.4&lt;/td>
700	&lt;td>68.1&lt;/td>
701	&lt;td>67.2&lt;/td>
702	&lt;td>72.3&lt;/td>
703	&lt;/tr>
704	&lt;/tbody>
705	&lt;/table>
706	
707	**Table 4:** Results of GenPRM with different label estimation method and threshold on ProcessBench, reported with Maj@8. The best results are shown in **bold**.
708	
709	&lt;table border="1">
710	&lt;thead>
711	&lt;tr>
712	&lt;th>Estimation Method&lt;/th>
713	&lt;th>Positive Label Criterion&lt;/th>
714	&lt;th>GSM8K&lt;/th>
715	&lt;th>MATH&lt;/th>
716	&lt;th>Olympiad Bench&lt;/th>
717	&lt;th>Omni-MATH&lt;/th>
718	&lt;th>Avg.&lt;/th>
719	&lt;/tr>
720	&lt;/thead>
721	&lt;tbody>
722	&lt;tr>
723	&lt;td>&lt;math>P_t = MC(s_t, a_t)&lt;/math> (hard label)&lt;/td>
724	&lt;td>&lt;math>P_t &gt; 0&lt;/math>&lt;/td>
725	&lt;td>75.1&lt;/td>
726	&lt;td>83.8&lt;/td>
727	&lt;td>&lt;b>80.6&lt;/b>&lt;/td>
728	&lt;td>74.4&lt;/td>
729	&lt;td>78.5&lt;/td>
730	&lt;/tr>
731	&lt;tr>
732	&lt;td rowspan="3">&lt;math>P_t = MC(s_t, a_t) - MC(s_t)&lt;/math>&lt;/td>
733	&lt;td>&lt;math>P_t \geq -0.1&lt;/math>&lt;/td>
734	&lt;td>79.8&lt;/td>
735	&lt;td>85.1&lt;/td>
736	&lt;td>78.0&lt;/td>
737	&lt;td>74.5&lt;/td>
738	&lt;td>79.4&lt;/td>
739	&lt;/tr>
740	&lt;tr>
741	&lt;td>&lt;math>P_t \geq -0.3&lt;/math>&lt;/td>
742	&lt;td>80.9&lt;/td>
743	&lt;td>&lt;b>86.5&lt;/b>&lt;/td>
744	&lt;td>78.1&lt;/td>
745	&lt;td>75.0&lt;/td>
746	&lt;td>80.2&lt;/td>
747	&lt;/tr>
748	&lt;tr>
749	&lt;td>&lt;math>P_t \geq -0.5&lt;/math>&lt;/td>
750	&lt;td>78.1&lt;/td>
751	&lt;td>85.6&lt;/td>
752	&lt;td>79.1&lt;/td>
753	&lt;td>73.4&lt;/td>
754	&lt;td>79.1&lt;/td>
755	&lt;/tr>
756	&lt;tr>
757	&lt;td rowspan="4">&lt;math>P_t = \frac{MC(s_t, a_t)}{MC(s_t)}&lt;/math>&lt;/td>
758	&lt;td>&lt;math>P_t \geq 0.1&lt;/math>&lt;/td>
759	&lt;td>77.0&lt;/td>
760	&lt;td>84.6&lt;/td>
761	&lt;td>78.1&lt;/td>
762	&lt;td>75.3&lt;/td>
763	&lt;td>78.7&lt;/td>
764	&lt;/tr>
765	&lt;tr>
766	&lt;td>&lt;math>P_t \geq 0.5&lt;/math>&lt;/td>
767	&lt;td>78.0&lt;/td>
768	&lt;td>85.2&lt;/td>
769	&lt;td>78.2&lt;/td>
770	&lt;td>74.3&lt;/td>
771	&lt;td>78.9&lt;/td>
772	&lt;/tr>
773	&lt;tr>
774	&lt;td>&lt;math>P_t \geq 0.8&lt;/math>&lt;/td>
775	&lt;td>81.0&lt;/td>
776	&lt;td>85.7&lt;/td>
777	&lt;td>78.4&lt;/td>
778	&lt;td>&lt;b>76.8&lt;/b>&lt;/td>
779	&lt;td>&lt;b>80.5&lt;/b>&lt;/td>
780	&lt;/tr>
781	&lt;tr>
782	&lt;td>&lt;math>P_t \geq 1.0&lt;/math>&lt;/td>
783	&lt;td>&lt;b>81.1&lt;/b>&lt;/td>
784	&lt;td>84.1&lt;/td>
785	&lt;td>76.0&lt;/td>
786	&lt;td>74.7&lt;/td>
787	&lt;td>79.0&lt;/td>
788	&lt;/tr>
789	&lt;/tbody>
790	&lt;/table>
791	
792	**Reasoning Components.** To understand how each reasoning component influence GenPRM, we conduct experiments by training GenPRM with: (1) CoT data only, (2) code verification data only, and (3) full data. During inference phase, we also compare several variants. For example, GenPRM trained with full data can be used to only verify each step with CoT only by stopping generation at `&lt;/analyze>` token. The results in Table 5 show that: (1) the improvement of GenPRM mainly comesfrom CoT reasoning; (2) generating code and reasoning with code execution result improves the process verification performance as well.
793	
794	**Table 5:** Results on ProcessBench of GenPRM with different reasoning components, reported with Maj@8. The best results are shown in **bold**.
795	
796	&lt;table border="1">
797	&lt;thead>
798	&lt;tr>
799	&lt;th colspan="2">Training&lt;/th>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "abf43550-7b71-4962-89c9-4b62e163ab36",
  "isSidechain": false,
  "promptId": "a37d06a3-a1b2-4f5b-ba56-06aaf32ddf9c",
  "type": "user",
  "uuid": "63961e89-9b3e-439d-b9ab-bb06e4efa11c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/d13ca6d2-ab23-4990-8414-c3096bb93ab5/tool-results/toolu_01GSHgkEVx98FPEy2wEtpX5x.txt",
      "content": "# GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\n\nJian Zhao&lt;sup>1,3\\*&lt;/sup>, Runze Liu&lt;sup>1,2\\*†&lt;/sup>, Kaiyan Zhang&lt;sup>1&lt;/sup>, Zhimu Zhou&lt;sup>3&lt;/sup>, Junqi Gao&lt;sup>4&lt;/sup>, Dong Li&lt;sup>4&lt;/sup>, Jiafei Lyu&lt;sup>1&lt;/sup>, Zhouyi Qian&lt;sup>4&lt;/sup>, Biqing Qi&lt;sup>2‡&lt;/sup>, Xiu Li&lt;sup>1‡&lt;/sup> and Bowen Zhou&lt;sup>1,2‡&lt;/sup>\n\n&lt;sup>1&lt;/sup>Tsinghua University, &lt;sup>2&lt;/sup>Shanghai AI Laboratory, &lt;sup>3&lt;/sup>BUPT, &lt;sup>4&lt;/sup>Harbin Institute of Technology\n\nRecent advancements in Large Language Models (LLMs) have shown that it is promising to utilize Process Reward Models (PRMs) as verifiers to enhance the performance of LLMs. However, current PRMs face three key challenges: (1) limited process supervision and generalization capabilities, (2) dependence on scalar value prediction without leveraging the generative abilities of LLMs, and (3) inability to scale the test-time compute of PRMs. In this work, we introduce GenPRM, a generative process reward model that performs explicit Chain-of-Thought (CoT) reasoning with code verification before providing judgment for each reasoning step. To obtain high-quality process supervision labels and rationale data, we propose Relative Progress Estimation (RPE) and a rationale synthesis framework that incorporates code verification. Experimental results on ProcessBench and several mathematical reasoning tasks show that GenPRM significantly outperforms prior PRMs with only **23K** training data from **MATH** dataset. Through test-time scaling, a **1.5B** GenPRM outperforms **GPT-4o**, and a **7B** GenPRM surpasses **Qwen2.5-Math-PRM-72B** on ProcessBench. Additionally, GenPRM demonstrates strong abilities to serve as a critic model for policy model refinement. This work establishes a new paradigm for process supervision that bridges the gap between PRMs and critic models in LLMs. Our code, model, and data are available in &lt;https://ryanliu112.github.io/GenPRM>.\n\n**Figure 1: GenPRM achieves state-of-the-art performance across multiple benchmarks in two key roles: (a) As a verifier:** GenPRM-7B outperforms all classification-based PRMs of comparable size and even surpasses **Qwen2.5-Math-PRM-72B** via test-time scaling. **(b) As a critic:** GenPRM-7B demonstrates superior critique capabilities, achieving **3.4x** greater performance gains than DeepSeek-R1-Distill-Qwen-7B after 3 refinement iterations.\n\n\\* Equal contribution\n\n† Project lead & Work done during an internship at Shanghai AI Laboratory\n\n‡ Corresponding authors: Biqing Qi (qibiqing@pjlab.org.cn), Xiu Li (li.xiu@sz.tsinghua.edu.cn), and Bowen Zhou (zhoubowen@tsinghua.edu.cn)The diagram illustrates the architectural differences between classification-based PRMs and GenPRM. On the left, under the heading 'Classification-based PRM', two models are shown: 'Discriminative PRM' and 'Direct Generative PRM'. The Discriminative PRM consists of a 'value head' that outputs a score of 0.9, marked with a green checkmark. The Direct Generative PRM outputs a 'Yes' label, which is then converted to a score of 0.8, also marked with a green checkmark. On the right, under the heading 'Generative PRM (Ours)', the 'GenPRM' model is shown. It branches into three parallel paths, each consisting of a yellow circle (CoT Verification) followed by a green circle (Code Verification) and a 'Yes' or 'No' label. The top path outputs 'Yes', the middle path outputs 'No', and the bottom path outputs 'No'. These three paths converge into a final score of 0.2, which is marked with a red 'X'. A legend at the bottom identifies the yellow circle as 'CoT Verification' and the green circle as 'Code Verification'.\n\nFigure 2: Comparison between GenPRM (right) and previous classification-based PRMs (left).\n\n## 1. Introduction\n\nLarge Language Models (LLMs) have shown significant advances in recent years (OpenAI, 2023; Anthropic, 2023; OpenAI, 2024a,b; DeepSeek-AI et al., 2025). As OpenAI o1 demonstrates the great effectiveness of scaling test-time compute (OpenAI, 2024a), an increasing number of researches focus on Test-Time Scaling (TTS) methods to improve the reasoning performance of LLMs (Snell et al., 2025; Liu et al., 2025).\n\nEffective TTS requires high-quality verifiers, such as Process Reward Models (PRMs) (Liu et al., 2025). However, existing PRMs face several limitations. They exhibit limited process supervision capabilities and struggle to generalize across different models and tasks (Zheng et al., 2024; Zhang et al., 2025c; Liu et al., 2025). Furthermore, most current approaches train PRMs as classifiers that output scalar values, neglecting the natural language generation abilities of LLMs, which are pre-trained on extensive corpora. This classifier-based modeling inherently prevents PRMs from leveraging test-time scaling methods to enhance process supervision capabilities. These limitations lead us to the following research question: *How can generative modeling enhance the process supervision capabilities of PRMs while enabling test-time scaling?*\n\nIn this work, we address these challenges through a generative process reward model, named GenPRM. Specifically, GenPRM differs from classification-based PRMs in that GenPRM redefines process supervision as a generative task rather than a discriminative scoring task by integrating Chain-of-Thought (CoT) (Wei et al., 2022) reasoning and code verification processes before providing final judgment. To improve conventional hard label estimation, we propose Relative Progress Estimation (RPE), which leverages a relative criterion for label estimation. Additionally, we introduce a rationale synthesis framework with code verification to obtain high-quality process supervision reasoning data. A comparison of our method with previous classification-based methods is presented in Figure 2.\n\nOur contributions can be summarized as follows:\n\n1. 1. We propose a generative process reward model that performs explicit CoT reasoning with code verification and utilizes Relative Progress Estimation to obtain accurate PRM labels.\n2. 2. Empirical results on ProcessBench and common mathematical reasoning tasks demonstrate that GenPRM outperforms prior classification-based PRMs. Additionally, smaller GenPRM models can surpass larger PRMs via TTS.\n3. 3. We provide a new perspective on PRMs in this work, fully leveraging their TTS capabilities, reshaping their applications, and opening new directions for future research in process supervision.## 2. Preliminaries\n\n### 2.1. Markov Decision Process\n\nFollowing [Liu et al. \\(2025\\)](#), we formulate the test-time scaling process with PRMs as a Markov Decision Process (MDP) defined by  $(\\mathcal{S}, \\mathcal{A}, P, r, \\gamma)$ , where  $\\mathcal{S}$  is the state space,  $\\mathcal{A}$  is the action space,  $P$  represents transition dynamics,  $r : \\mathcal{S} \\times \\mathcal{A} \\rightarrow \\mathbb{R}$  is the reward function, and  $\\gamma \\in [0, 1]$  is the discount factor. Starting with a prompt set  $\\mathcal{X}$  and an initial state  $s_1 = x \\sim \\mathcal{X}$ , the policy model  $\\pi_\\theta$  generates an action  $a_1 \\sim \\pi_\\theta(\\cdot | s_1)$ .&lt;sup>1&lt;/sup> Unlike traditional RL methods with stochastic transitions ([Liu et al., 2022, 2024](#)), transitions in LLMs are deterministic, i.e.,  $s_{t+1} = P(\\cdot | s_t, a_t) = [s_t, a_t]$ , where  $[\\cdot, \\cdot]$  denotes string concatenation. This process continues until the episode terminates (i.e., generating the [EOS] token), obtaining a trajectory of  $T$  steps:  $\\tau = \\{a_1, a_2, \\dots, a_T\\}$ . The goal is to optimize either the reward of each step (as in search-based methods) or the reward over the full response (as in Best-of-N sampling).\n\n### 2.2. Supervised Fine-Tuning\n\nSupervised Fine-Tuning (SFT) trains a model to predict the next token based on prior context. For a dataset  $\\mathcal{D}_{\\text{SFT}} = \\{(x^{(i)}, y^{(i)})\\}_{i=1}^N$ , the SFT loss is:\n\n$$\\mathcal{L}_{\\text{SFT}}(\\theta) = -\\mathbb{E}_{(x,y) \\sim \\mathcal{D}_{\\text{SFT}}} \\left[ \\sum_{t=1}^{|y|} \\log \\pi_\\theta(y_t | x, y_{1:t-1}) \\right], \\quad (1)$$\n\nwhere  $\\pi_\\theta$  represents a model with parameters  $\\theta$ .\n\n### 2.3. Test-Time Scaling\n\nIn this work, we consider two test-time scaling methods, including majority voting and Best-of-N.\n\n**Majority Voting.** Majority voting ([Wang et al., 2023](#)) selects the answer that appears the most frequently among all solutions.\n\n**Best-of-N.** Best-of-N (BoN) ([Brown et al., 2024](#); [Snell et al., 2025](#)) selects the best answer from  $N$  candidate solutions.\n\n## 3. Method\n\nIn this section, we first describe how to develop GenPRM and integrate the reasoning process with code verification. We then introduce how to scale test-time compute of policy models using GenPRM and apply TTS for GenPRM. Last, we present the improved label estimation method and data generation and filtering framework of GenPRM.\n\n### 3.1. GenPRM and Test-Time Scaling\n\n#### 3.1.1. From Discriminative PRM to Generative PRM\n\n**Discriminative PRM.** Assume we have a PRM dataset  $\\mathcal{D}_{\\text{Disc}} = \\{(s_t, a_t), r_t\\}$ , where  $r_t \\in \\{0, 1\\}$  for PRM labels with hard estimation. The discriminative PRM  $r_\\psi$  is trained via cross-entropy loss ([Skywork](#)\n\n&lt;sup>1&lt;/sup>Following [Snell et al. \\(2025\\)](#); [Liu et al. \\(2025\\)](#), we refer to models that generate solutions as policy models.The diagram illustrates the GenPRM framework, which consists of six key parts:\n\n- **① Solution Generation & MC Reward Estimation:** A math problem is solved by generating intermediate steps (a&lt;sub>11&lt;/sub>, a&lt;sub>21&lt;/sub>, a&lt;sub>31&lt;/sub>, a&lt;sub>12&lt;/sub>, a&lt;sub>22&lt;/sub>, a&lt;sub>32&lt;/sub>). Correct steps (q&lt;sub>1&lt;/sub>, q&lt;sub>2&lt;/sub>) are marked with blue circles, and incorrect steps (q&lt;sub>3&lt;/sub>) are marked with red circles. The MC score for a step is calculated as  $MC(s_{12}, a_{12}) = \\frac{2}{3}$ .\n- **② Relative Progress Estimation:** The process reward is estimated as  $P_t = \\frac{MC(s_t, a_t)}{MC(s_t)} \\geq \\epsilon$ . If the reward is high,  $\\hat{r}_t = 1$  (green checkmark), otherwise  $\\hat{r}_t = 0$  (red X).\n- **③ Rationale Synthesis:** A problem is analyzed using CoT (Chain of Thought) analysis to generate a rationale. This rationale is then verified using code verification (e.g., Python code) to check for potential errors. The final label is a judgement of Yes/No.\n- **④ GenPRM Training:** Data (23K) is used for SFT (Supervised Fine-Tuning) to train GenPRM. Consensus filtering is applied to the training data.\n- **⑤ Policy Model Test-Time Scaling:** The trained GenPRM functions as a verifier or critic. It can be used to verify a solution (GenPRM as a Verifier) or critique a solution (GenPRM as a Critic).\n- **⑥ GenPRM Test-Time Scaling:** The performance of GenPRM is improved through test-time scaling. Multiple steps are analyzed and verified, and their rewards are aggregated to produce a final reward  $r$ .\n\nLegend:\n\n- a Intermediate Step\n- q Correct Answer\n- q Incorrect Answer\n- r Single Reward Judgement\n- r Aggregated Reward Judgement\n\n**Figure 3: Overall framework of GenPRM.** Our framework consists of six key parts: ① The policy model generates solution steps, with MC scores estimated from rollout trajectories. ② Our proposed RPE derives accurate PRM labels. ③ High-quality process supervision data is synthesized through CoT reasoning augmented with code verification. ④ We apply consensus filtering followed by SFT to train GenPRM. ⑤ The trained GenPRM functions as a verifier or critic, enabling enhanced test-time scaling for policy models. ⑥ The performance of GenPRM further improves through test-time scaling.\n\no1 Team, 2024; Zhang et al., 2025c):\n\n$$\\mathcal{L}_{CE}(\\psi) = -\\mathbb{E}_{(s_t, a_t, r_t) \\sim \\mathcal{D}_{Disc}} [r_t \\log r_\\psi(s_t, a_t) + (1 - r_t) \\log(1 - r_\\psi(s_t, a_t))]. \\quad (2)$$\n\n**Direct Generative PRM.** With a dataset  $\\mathcal{D}_{Direct-Gen} = \\{(s_t, a_t), r_t\\}$ , where  $r_t$  is Yes for a correct step and No otherwise, the direct generative PRM (Xiong et al., 2024) is trained through SFT to predict Yes or No for each step. For step  $t$ , we use the probability of the Yes token as the predicted process reward  $\\hat{r}_t$ :\n\n$$\\hat{r}_t = r_\\psi(\\text{Yes} \\mid s_t, a_t). \\quad (3)$$\n\n**Generative PRM.** By equipping the direct generative PRM with an explicit reasoning process like CoT (Wei et al., 2022), we obtain a generative PRM. Let  $v_{1:t-1}$  denote the rationale from step 1 to  $t-1$  and  $v_t$  denote the rationale for step  $t$ . Assume we have a dataset  $\\mathcal{D}_{Gen} = \\{(s_t, a_t, v_{1:t-1}), (v_t, r_t)\\}$ . GenPRM learns to reason and verify each step via SFT on this dataset. The generative process reward  $\\hat{r}_t$  can be obtained via the following equation:\n\n$$\\hat{r}_t = r_\\psi(\\text{Yes} \\mid s_t, a_t, v_{1:t-1}, v_t), \\quad \\text{where } v_t \\sim r_\\psi(\\cdot \\mid s_t, a_t, v_{1:t-1}) \\quad (4)$$\n\n**Generative PRM with Code Verification.** If we only verify the reasoning step with CoT based on natural language, the process may lack robustness in certain complex scenarios (Zhu et al., 2024; Gou et al., 2024). The difference between the generative PRM and the generative PRM with code verification is that the latter generates code to verify the reasoning step by executing it and provides the judgment based on the execution results. At step  $t$ , after generating the rationale  $v_t$  containing CoT and code, we execute the code and obtain feedback  $f_t$ . Given the current state  $s_t$ , action  $a_t$ , previous rationales  $v_{1:t-1}$ , and previous corresponding execution feedback  $f_{1:t-1}$ , the PRM first generates therationale  $v_t$ . After execution and obtaining the feedback  $f_t$ , we compute the final generative process reward as follows:\n\n$$\\hat{r}_t = r_\\psi(\\text{Yes} \\mid s_t, a_t, v_{1:t-1}, f_{1:t-1}, v_t, f_t), \\quad \\text{where } v_t \\sim r_\\psi(\\cdot \\mid s_t, a_t, v_{1:t-1}, f_{1:t-1}) \\quad (5)$$\n\nIn the following sections, we refer to GenPRM as this generative PRM type with code verification. The effectiveness of CoT and code verification can be found in Section 4.4.\n\n### 3.1.2. Test-Time Scaling\n\n**Policy Model TTS: GenPRM as a Verifier.** To scale the test-time compute of policy models, we can sample multiple responses from policy models and then use GenPRM as a verifier to select the final answer (Snell et al., 2025) in the way of parallel TTS.\n\n**Policy Model TTS: GenPRM as a Critic.** By equipping the PRM with generative process supervision abilities, GenPRM can be naturally used as a critic model to refine the outputs of policy models and we can scale the refinement process with multiple turns in a sequential TTS manner.\n\n**GenPRM TTS.** When evaluating each solution step, we first sample  $N$  reasoning verification paths and then use majority voting to obtain the final prediction by averaging the rewards. For GenPRM without code verification, the rewards are computed as follows:\n\n$$\\hat{r}_t = \\frac{1}{N} \\sum_{i=1}^N r_\\psi(\\text{Yes} \\mid s_t, a_t, v_{1:t-1}^i, v_t^i). \\quad (6)$$\n\nAnd we can further incorporate code verification and execution feedback into this reasoning process:\n\n$$\\hat{r}_t = \\frac{1}{N} \\sum_{i=1}^N r_\\psi(\\text{Yes} \\mid s_t, a_t, v_{1:t-1}^i, f_{1:t-1}^i, v_t^i, f_t^i). \\quad (7)$$\n\nThen the rewards can be used for ranking the responses of policy models or be converted into binary labels through a threshold 0.5 for judging the correctness of the step. The discussion of using code verification can be found at Table 5.\n\n## 3.2. Synthesizing Data of GenPRM\n\nIn this section, we introduce our pipeline for synthesizing training data of GenPRM. The pipeline consists of three stages: (1) generating reasoning paths and obtaining PRM labels via Monte Carlo (MC) estimation; (2) evaluating the progress of each step via Relative Progress Estimation; and (3) synthesizing rationales with CoT and code verification, and inferring LLM-as-a-judge labels with consensus filtering.\n\n### 3.2.1. Solution Generation and Monte Carlo Estimation\n\n**Solution Generation with Step Forcing.** We utilize the 7.5K problems from the training set of the MATH dataset (Hendrycks et al., 2021) as the problem set. For each problem, we use Qwen2.5-7B-Instruct (Yang et al., 2024a) as the generation model to collect multiple solutions. Since using “\\n\\n” for step division does not consider the semantics of each step and may result in overly fine-grained division, we apply a step forcing approach to generate solutions. Specifically, we add “Step 1:” as the prefix for the generation model to complete the response. For a response with  $T$  reasoning steps, the format is as follows:### The response format with step forcing\n\nStep 1: {step content}\n\n...\n\nStep T: {step content}\n\nThe proportion of correct paths versus incorrect paths varies significantly depending on the difficulty of the problems. To ensure a sufficient number of correct and incorrect paths, we sample up to 2048 paths for both hard and easy problems. If no correct or incorrect paths are found after sampling 2048 responses, we discard the corresponding problems.\n\n**Balancing the Precision and Efficiency of MC Estimation.** Following Math-Shepherd (Wang et al., 2024b), we estimate the probability of correctness for each step using completion-based sampling. For each reasoning step  $s_t$ , we generate  $K$  completion trajectories using a completion model, specifically Qwen2.5-Math-7B-Instruct (Yang et al., 2024b), and use MC estimation to calculate the probability that the current step  $a_t$  is correct (Wang et al., 2024b; Zhang et al., 2025c):\n\n$$MC(s_t, a_t) = MC(s_{t+1}) = \\frac{1}{K} \\sum_{j=1}^K \\mathbb{1}(q_j = q^*), \\quad (8)$$\n\nwhere  $q_j$  is the answer of the  $j$ -th response,  $q^*$  is the ground-truth answer, and  $\\mathbb{1}$  is the indicator function. However, it is difficult for the completion model to reach the correct answer for hard problems even when the original step is correct, leading to incorrect results for MC estimation. To address this and balance the computation cost, we use a dynamic  $K$  based on the estimated Pass@1  $MC(s_1)$ :\n\n$$K = \\begin{cases} 128 & \\text{if } 0 \\leq MC(s_1) < 0.1, \\\\ 64 & \\text{if } 0.1 \\leq MC(s_1) < 0.9, \\\\ 32 & \\text{if } 0.9 \\leq MC(s_1) < 1. \\end{cases} \\quad (9)$$\n\n### 3.2.2. Relative Progress Estimation\n\nPrevious work has shown that hard label estimation is better than soft label estimation for PRMs (Zhang et al., 2025c). However, after MC estimation, we observe that although the MC score of many steps is greater than 0, the steps are incorrect, as also noted by Zhang et al. (2025c). On the other hand, we assume that a positive step should be both correct and beneficial. A reasoning step is considered as a beneficial one if it is easier to reach the correct answer by adding this step as the generation prefix. To address these issues, we propose Relative Progress Estimation (RPE), which shares a similar idea with relative advantage estimation in GRPO (Shao et al., 2024; DeepSeek-AI et al., 2025), to improve conventional hard label estimation.\n\nSpecifically, the MC score is an empirical estimation of the current state  $s_t$ . To evaluate the quality of the current action  $a_t$ , it is natural to compare the MC score of the next state  $s_{t+1}$  with that of the current state  $s_t$ , since  $s_{t+1} = [s_t, a_t]$ . For each response, if the first erroneous step is step  $t'$  (i.e.,  $MC(s_{t'}) = 0$ ), we set the MC score of the following steps to 0. Our RPE  $P_t$  for step  $t$  is defined as follows:\n\n$$P_t = \\frac{MC(s_t, a_t)}{MC(s_t)}, \\quad (10)$$\n\nwhere  $MC(s_1)$  is the estimated Pass@1 computed in the solution generation phase. However, we empirically find that using a strict criterion where progress is always greater than 1 leads to unsatisfactory performance, as shown in Table 3. To address this, we estimate the final reward label  $\\hat{r}_t$  byintroducing a threshold  $\\epsilon$ :\n\n$$\\hat{r}_t = \\begin{cases} 1 & \\text{if } P_t \\geq \\epsilon, \\\\ 0 & \\text{otherwise.} \\end{cases} \\quad (11)$$\n\nWe also discuss another form of relative progress  $P_t = MC(s_t, a_t) - MC(s_t)$  in Table 3 in Section 4.4.\n\n### 3.2.3. Rationale Generation, Verification and Filtering\n\nTo obtain high-quality rationale data, we use QwQ-32B (Qwen Team, 2025) as the rationale generation model and introduce a three-step pipeline that automatically generates and verifies the rationale of each reasoning step. Given a problem  $x$  with a ground-truth answer  $q^*$  and candidate steps  $\\{a_1, \\dots, a_T\\}$ , the generation and verification proceed as follows:\n\n**Step 1: Code-Based Rationale Generation.** To evaluate the correctness of  $a_t$ , we synthesize step-by-step CoT analysis. It has been shown that program-based reasoning improves verification outcomes (Zhu et al., 2024). Based on CoT analysis, we continue to synthesize code-based rationales to verify  $a_t$  based on the problem and historical steps  $\\{a_1, \\dots, a_{t-1}\\}$ . We prompt the rationale generation model to surround the CoT with `&lt;analyze>` and `&lt;/analyze>`, and the code with `&lt;verify>` and `&lt;/verify>`. The prompt for rationale generation is shown in Table A.2.\n\n**Step 2: Code Execution and Verification.** With the generated code, we execute it and obtain the feedback  $f_t$  for step  $t$ . The execution feedback is formatted as [Code output: {execution result}] and is concatenated to the generated CoT and code as the prefix for the subsequent generation. If the execution result is inconsistent with the generated CoT verification, we observe that QwQ-32B performs self-reflection behaviors until reaching a consensus.\n\n**Step 3: Label Judgment and Consensus Filtering.** After generating and verifying the rationale data of all candidate steps, the rationale generation model finally outputs a number. If all steps are inferred to be correct, the number will be -1, otherwise will be the index of the first erroneous step. For each solution, if there is at least one process label with RPE is not consistent with the labels generated by LLM-as-a-judge (Zheng et al., 2023), we discard the entire solution and only retain the one with all labels consistent. After consensus filtering, we discard approximately 51% of the data and finally obtain a dataset containing 23K problems with reasoning steps and rationale data.\n\n## 4. Experiments\n\nIn this section, we aim to answer the following questions:\n\n- • **Q1:** How does GenPRM perform compared with previous PRMs? (§4.2, §4.3)\n- • **Q2:** How does the performance of GenPRM scale with more test-time compute? (§4.2, §4.3)\n- • **Q3:** How does GenPRM benefit policy model test-time scaling? (§4.3)\n- • **Q4:** How do the components and hyperparameters influence GenPRM? (§4.4)\n\n### 4.1. Setup\n\n**Benchmarks.** We evaluate GenPRM and baseline methods on ProcessBench (Zheng et al., 2024), a benchmark designed to assess process supervision capabilities in mathematical reasoning tasks.&lt;sup>2&lt;/sup>\n\n&lt;sup>2&lt;/sup>Our evaluation code is adapted from &lt;https://github.com/QwenLM/ProcessBench>.Additionally, we conduct BoN and critic refinement experiments using MATH (Hendrycks et al., 2021), AMC23 (AI-MO, 2024b), AIME24 (AI-MO, 2024a), and Minerva Math (Lewkowycz et al., 2022). For BoN response generation, we employ Qwen2.5-Math-7B-Instruct (Yang et al., 2024b) and Gemma-3-12b-it (Gemma Team and Google DeepMind, 2025) as policy models. For policy model TTS with GenPRM as the critic, we use Gemma-3-12b-it (Gemma Team and Google DeepMind, 2025) and Qwen2.5-7B-Instruct (Yang et al., 2024a) as generators.\n\n**Baselines.** For ProcessBench and BoN experiments, we compare GenPRM with the following methods:\n\n- • **Math-Shepherd-PRM-7B** (Wang et al., 2024b): This method trains a PRM using hard labels computed based on MC estimation.\n- • **RLHFlow series** (Xiong et al., 2024): Includes RLHFlow-PRM-Mistral-8B and RLHFlow-PRM-Deepseek-8B.\n- • **Skywork-PRM series** (Skywork o1 Team, 2024): Comprises Skywork-PRM-1.5B and Skywork-PRM-7B.\n- • **EurusPRM** (Cui et al., 2025): EurusPRM-Stage1 and EurusPRM-Stage2 are trained as implicit PRMs (Yuan et al., 2024).\n- • **Qwen2.5-Math series** (Zheng et al., 2024; Zhang et al., 2025c): Qwen2.5-Math-7B-Math-Shepherd and Qwen2.5-Math-7B-PRM800K are trained with Math-Shepherd (Wang et al., 2024b) and PRM800K (Lightman et al., 2024), respectively. For Qwen2.5-Math-PRM-7B and Qwen2.5-Math-PRM-72B, the training data is applied consensus filtering using LLM-as-a-judge (Zheng et al., 2023).\n- • **RetrievalPRM-7B** (Zhu et al., 2025): The method enhances PRM with retrieved questions and corresponding steps.\n- • **Universal-PRM-7B** (Tan et al., 2025): The method proposes an automated framework using ensemble prompting and reverse verification.\n- • **Dyve-14B** (Zhong et al., 2025): This method dynamically applies fast or slow verification for each reasoning step.\n- • **Direct Generative PRM-7B**: The method trains a direct generative PRM with the original language head via SFT using the same data as GenPRM, but without CoT and code verification.\n\nFor critic experiments, we use the following methods for comparison:\n\n- • **Self-Refine** (Madaan et al., 2023): This method uses the generator to self-critique and refine the solution.\n- • **DeepSeek-R1-Distill-Qwen-7B** (DeepSeek-AI et al., 2025): This model is fine-tuned based on Qwen2.5-Math-7B (Yang et al., 2024a) using high-quality reasoning data generated by DeepSeek-R1 (DeepSeek-AI et al., 2025).\n\n**Implementation Details.** For RPE, we set  $\\epsilon = 0.8$  across all experiments, with ablation studies presented in Section 4.4. Rationale data is generated using QwQ-32B (Qwen Team, 2025) and the prompt template is shown in Table A.2. Our base models are from the DeepSeek-R1-Distill series (DeepSeek-AI et al., 2025), specifically the 1.5B, 7B, and 32B parameter variants. The training configuration for our method uses a batch size of 64 and a learning rate of  $2.0 \\times 10^{-6}$ . During evaluation, we employ a temperature of 0.6. For critique refinement experiments, we extract content within the `&lt;analyze>&lt;/analyze>` tags, focusing exclusively on steps predicted as negative by the policy model. The baseline methods utilize standardized prompt templates (detailed in Table A.2) to ensure consistent critique generation formats.**Table 1:** ProcessBench results reported with F1 scores. The results of GenPRM are shaded. For 1.5B PRMs, **bold** indicates the best Pass@1 or scores superior to GPT-4o. For 7-8B and 14-72B PRMs, **bold** denotes the best Pass@1 or scores superior to Qwen2.5-Math-PRM-72B.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Model&lt;/th>\n&lt;th># Samples&lt;/th>\n&lt;th>GSM8K&lt;/th>\n&lt;th>MATH&lt;/th>\n&lt;th>Olympiad Bench&lt;/th>\n&lt;th>Omni-MATH&lt;/th>\n&lt;th>Avg.&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>Proprietary LLMs (Critic)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GPT-4o-0806&lt;/td>\n&lt;td>unk&lt;/td>\n&lt;td>79.2&lt;/td>\n&lt;td>63.6&lt;/td>\n&lt;td>51.4&lt;/td>\n&lt;td>53.5&lt;/td>\n&lt;td>61.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>o1-mini&lt;/td>\n&lt;td>unk&lt;/td>\n&lt;td>93.2&lt;/td>\n&lt;td>88.9&lt;/td>\n&lt;td>87.2&lt;/td>\n&lt;td>82.4&lt;/td>\n&lt;td>87.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>PRMs (1.5B)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-1.5B&lt;/td>\n&lt;td>unk&lt;/td>\n&lt;td>&lt;b>59.0&lt;/b>&lt;/td>\n&lt;td>48.0&lt;/td>\n&lt;td>19.3&lt;/td>\n&lt;td>19.2&lt;/td>\n&lt;td>36.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-1.5B (Pass@1)&lt;/td>\n&lt;td>23K&lt;/td>\n&lt;td>52.8&lt;/td>\n&lt;td>&lt;b>66.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>55.1&lt;/b>&lt;/td>\n&lt;td>&lt;b>54.5&lt;/b>&lt;/td>\n&lt;td>&lt;b>57.3&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-1.5B (Maj@8)&lt;/td>\n&lt;td>23K&lt;/td>\n&lt;td>51.3&lt;/td>\n&lt;td>&lt;b>74.4&lt;/b>&lt;/td>\n&lt;td>&lt;b>65.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>62.5&lt;/b>&lt;/td>\n&lt;td>&lt;b>63.4&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>PRMs (7-8B)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Math-Shepherd-PRM-7B&lt;/td>\n&lt;td>445K&lt;/td>\n&lt;td>47.9&lt;/td>\n&lt;td>29.5&lt;/td>\n&lt;td>24.8&lt;/td>\n&lt;td>23.8&lt;/td>\n&lt;td>31.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RLHFlow-PRM-Mistral-8B&lt;/td>\n&lt;td>273K&lt;/td>\n&lt;td>50.4&lt;/td>\n&lt;td>33.4&lt;/td>\n&lt;td>13.8&lt;/td>\n&lt;td>15.8&lt;/td>\n&lt;td>28.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RLHFlow-PRM-Deepseek-8B&lt;/td>\n&lt;td>253K&lt;/td>\n&lt;td>38.8&lt;/td>\n&lt;td>33.8&lt;/td>\n&lt;td>16.9&lt;/td>\n&lt;td>16.9&lt;/td>\n&lt;td>26.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-7B&lt;/td>\n&lt;td>unk&lt;/td>\n&lt;td>70.8&lt;/td>\n&lt;td>53.6&lt;/td>\n&lt;td>22.9&lt;/td>\n&lt;td>21.0&lt;/td>\n&lt;td>42.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>EurusPRM-Stage1&lt;/td>\n&lt;td>463K&lt;/td>\n&lt;td>44.3&lt;/td>\n&lt;td>35.6&lt;/td>\n&lt;td>21.7&lt;/td>\n&lt;td>23.1&lt;/td>\n&lt;td>31.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>EurusPRM-Stage2&lt;/td>\n&lt;td>30K&lt;/td>\n&lt;td>47.3&lt;/td>\n&lt;td>35.7&lt;/td>\n&lt;td>21.2&lt;/td>\n&lt;td>20.9&lt;/td>\n&lt;td>31.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-Math-Shepherd&lt;/td>\n&lt;td>445K&lt;/td>\n&lt;td>62.5&lt;/td>\n&lt;td>31.6&lt;/td>\n&lt;td>13.7&lt;/td>\n&lt;td>7.7&lt;/td>\n&lt;td>28.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-PRM800K&lt;/td>\n&lt;td>264K&lt;/td>\n&lt;td>68.2&lt;/td>\n&lt;td>62.6&lt;/td>\n&lt;td>50.7&lt;/td>\n&lt;td>44.3&lt;/td>\n&lt;td>56.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-PRM-7B&lt;/td>\n&lt;td>~344K&lt;/td>\n&lt;td>82.4&lt;/td>\n&lt;td>77.6&lt;/td>\n&lt;td>67.5&lt;/td>\n&lt;td>66.3&lt;/td>\n&lt;td>73.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RetrievalPRM-7B&lt;/td>\n&lt;td>404K&lt;/td>\n&lt;td>74.6&lt;/td>\n&lt;td>71.1&lt;/td>\n&lt;td>60.2&lt;/td>\n&lt;td>57.3&lt;/td>\n&lt;td>65.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Universal-PRM-7B&lt;/td>\n&lt;td>unk&lt;/td>\n&lt;td>&lt;b>85.8&lt;/b>&lt;/td>\n&lt;td>77.7&lt;/td>\n&lt;td>67.6&lt;/td>\n&lt;td>66.4&lt;/td>\n&lt;td>74.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Direct Generative PRM-7B&lt;/td>\n&lt;td>23K&lt;/td>\n&lt;td>63.9&lt;/td>\n&lt;td>65.8&lt;/td>\n&lt;td>54.5&lt;/td>\n&lt;td>55.9&lt;/td>\n&lt;td>60.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-7B (Pass@1)&lt;/td>\n&lt;td>23K&lt;/td>\n&lt;td>78.7&lt;/td>\n&lt;td>&lt;b>80.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>72.2&lt;/b>&lt;/td>\n&lt;td>&lt;b>69.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>75.2&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-7B (Maj@8)&lt;/td>\n&lt;td>23K&lt;/td>\n&lt;td>81.0&lt;/td>\n&lt;td>&lt;b>85.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>78.4&lt;/b>&lt;/td>\n&lt;td>&lt;b>76.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>80.5&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>PRMs (14-72B)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Dyve-14B&lt;/td>\n&lt;td>117K&lt;/td>\n&lt;td>68.5&lt;/td>\n&lt;td>58.3&lt;/td>\n&lt;td>49.0&lt;/td>\n&lt;td>47.2&lt;/td>\n&lt;td>55.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-PRM-72B&lt;/td>\n&lt;td>~344K&lt;/td>\n&lt;td>&lt;b>87.3&lt;/b>&lt;/td>\n&lt;td>80.6&lt;/td>\n&lt;td>74.3&lt;/td>\n&lt;td>71.1&lt;/td>\n&lt;td>78.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-32B (Pass@1)&lt;/td>\n&lt;td>23K&lt;/td>\n&lt;td>83.1&lt;/td>\n&lt;td>&lt;b>81.7&lt;/b>&lt;/td>\n&lt;td>72.8&lt;/td>\n&lt;td>&lt;b>72.8&lt;/b>&lt;/td>\n&lt;td>77.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-32B (Maj@8)&lt;/td>\n&lt;td>23K&lt;/td>\n&lt;td>85.1&lt;/td>\n&lt;td>&lt;b>86.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>78.9&lt;/b>&lt;/td>\n&lt;td>&lt;b>80.1&lt;/b>&lt;/td>\n&lt;td>&lt;b>82.6&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n## 4.2. ProcessBench Results\n\n**GenPRM outperforms classification-based PRMs on ProcessBench.** As shown in Table 1, GenPRM-7B significantly outperforms direct generative PRM and surpasses **all** previous PRMs with parameters less than 72B on ProcessBench. Also, GenPRM-1.5B outperforms Skywork-PRM-1.5B by a large margin. It is noteworthy that GenPRM is trained with merely **23K** data from **MATH** (Hendrycks et al., 2021) only. By comparing the detailed results in Table 6, we can find that the performance gain of GenPRM mainly comes from the stronger abilities of finding **erroneous** steps and we provide concrete cases in Appendix C. These results demonstrating the superiority of generative modeling of PRM.\n\n**GenPRM enables smaller PRMs surpass 10 $\\times$  larger PRMs and GPT-4o via TTS.** We also compare the TTS results of GenPRM in Table 1 and find that GenPRM-1.5B surpasses GPT-4 and GenPRM-7B exceeds Qwen2.5-Math-PRM-72B on ProcessBench via simply majority voting, showing that scaling test-time compute is highly effective for GenPRM. We also find that the performance improvement of scaling the test-time compute on **harder** problems is larger than that of easier questions.### 4.3. Policy Model Test-Time Scaling Results\n\n**GenPRM as a Verifier.** The results in Figure 4 (a)-(d) show that GenPRM outperforms the baselines on MATH, AMC23, AIME24, and Minerva Math with Qwen2.5-Math-7B-Instruct (Yang et al., 2024b) as the generation model. The advantage of GenPRM becomes larger by scaling the test-time compute of GenPRM and the generation model. Figure 4 (e)-(h) demonstrates that GenPRM generalizes well to responses with Gemma-3-12b-it (Gemma Team and Google DeepMind, 2025) as the generation model.\n\n**Figure 4:** BoN results with different generation models on multiple mathematical benchmarks.\n\n**GenPRM as a Critic.** We also conduct experiments by using GenPRM as a critic to refine the outputs of the policy model. The results in Table 2 and Figure 1 (right) show that GenPRM exhibits strong critique abilities than the baselines, significantly improving the performance of the policy model and the performance continues to increase with more refinement based on the critic feedback.\n\n### 4.4. Analysis\n\n**Label Estimation Method and Criterion.** To explore how different label estimation influences GenPRM, we conduct experiments with the following methods: (1) hard label (Wang et al., 2024b; Zhang et al., 2025c); (2) RPE in (10); and (3) a RPE variant ( $P_t = MC(s_t, a_t) - MC(s_t)$ ). For the RPE and its variant, we use different thresholds  $\\epsilon$  for evaluation and set the labels as correct by checking whether  $P_t \\geq \\epsilon$ . The results in Table 3 show that RPE and its variant outperforms hard label estimation and RPE with  $\\epsilon = 0.8$  achieves the best result. By scaling test-time compute with majority voting, the results in Table 4 demonstrate that RPE with  $\\epsilon = 0.8$  still reaches the best.**Table 2:** Results of critique refinement experiments. The results of GenPRM are shaded. For each refinement turn, the highest values are **bolded**.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">Critic Model&lt;/th>\n&lt;th colspan=\"5\">Gemma-3-12b-it as Generator&lt;/th>\n&lt;th colspan=\"5\">Qwen2.5-7B-Instruct as Generator&lt;/th>\n&lt;th rowspan=\"2\">Avg.&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>AMC23&lt;/th>\n&lt;th>AIME24&lt;/th>\n&lt;th>MATH&lt;/th>\n&lt;th>Minerva Math&lt;/th>\n&lt;th>Avg.&lt;/th>\n&lt;th>AMC23&lt;/th>\n&lt;th>AIME24&lt;/th>\n&lt;th>MATH&lt;/th>\n&lt;th>Minerva Math&lt;/th>\n&lt;th>Avg.&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Zero-shot&lt;/td>\n&lt;td>64.1&lt;/td>\n&lt;td>15.8&lt;/td>\n&lt;td>83.8&lt;/td>\n&lt;td>31.9&lt;/td>\n&lt;td>48.9&lt;/td>\n&lt;td>51.6&lt;/td>\n&lt;td>7.1&lt;/td>\n&lt;td>76.2&lt;/td>\n&lt;td>34.5&lt;/td>\n&lt;td>42.4&lt;/td>\n&lt;td>45.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"12\" style=\"text-align: center;\">&lt;i>Turn 1&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Generator&lt;/td>\n&lt;td>66.6&lt;/td>\n&lt;td>15.8&lt;/td>\n&lt;td>84.7&lt;/td>\n&lt;td>33.3&lt;/td>\n&lt;td>50.1&lt;/td>\n&lt;td>50.6&lt;/td>\n&lt;td>8.0&lt;/td>\n&lt;td>76.8&lt;/td>\n&lt;td>34.0&lt;/td>\n&lt;td>42.4&lt;/td>\n&lt;td>46.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepSeek-R1-Distill-7B&lt;/td>\n&lt;td>69.1&lt;/td>\n&lt;td>17.9&lt;/td>\n&lt;td>84.6&lt;/td>\n&lt;td>33.0&lt;/td>\n&lt;td>51.2&lt;/td>\n&lt;td>50.6&lt;/td>\n&lt;td>6.3&lt;/td>\n&lt;td>77.7&lt;/td>\n&lt;td>34.7&lt;/td>\n&lt;td>42.3&lt;/td>\n&lt;td>46.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-7B&lt;/td>\n&lt;td>&lt;b>74.1&lt;/b>&lt;/td>\n&lt;td>&lt;b>19.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>86.0&lt;/b>&lt;/td>\n&lt;td>&lt;b>35.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>53.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>57.5&lt;/b>&lt;/td>\n&lt;td>&lt;b>8.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>80.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>36.5&lt;/b>&lt;/td>\n&lt;td>&lt;b>45.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>49.8&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"12\" style=\"text-align: center;\">&lt;i>Turn 2&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Generator&lt;/td>\n&lt;td>66.6&lt;/td>\n&lt;td>18.0&lt;/td>\n&lt;td>84.8&lt;/td>\n&lt;td>31.6&lt;/td>\n&lt;td>50.3&lt;/td>\n&lt;td>49.8&lt;/td>\n&lt;td>8.0&lt;/td>\n&lt;td>76.9&lt;/td>\n&lt;td>31.8&lt;/td>\n&lt;td>41.6&lt;/td>\n&lt;td>46.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepSeek-R1-Distill-7B&lt;/td>\n&lt;td>70.9&lt;/td>\n&lt;td>18.3&lt;/td>\n&lt;td>85.0&lt;/td>\n&lt;td>33.5&lt;/td>\n&lt;td>51.9&lt;/td>\n&lt;td>51.9&lt;/td>\n&lt;td>7.9&lt;/td>\n&lt;td>78.1&lt;/td>\n&lt;td>32.8&lt;/td>\n&lt;td>42.7&lt;/td>\n&lt;td>47.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-7B&lt;/td>\n&lt;td>&lt;b>75.0&lt;/b>&lt;/td>\n&lt;td>&lt;b>21.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>86.9&lt;/b>&lt;/td>\n&lt;td>&lt;b>35.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>54.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>59.4&lt;/b>&lt;/td>\n&lt;td>&lt;b>9.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>82.2&lt;/b>&lt;/td>\n&lt;td>&lt;b>35.0&lt;/b>&lt;/td>\n&lt;td>&lt;b>46.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>50.7&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"12\" style=\"text-align: center;\">&lt;i>Turn 3&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Generator&lt;/td>\n&lt;td>67.8&lt;/td>\n&lt;td>18.1&lt;/td>\n&lt;td>85.0&lt;/td>\n&lt;td>32.1&lt;/td>\n&lt;td>50.8&lt;/td>\n&lt;td>49.7&lt;/td>\n&lt;td>8.1&lt;/td>\n&lt;td>77.1&lt;/td>\n&lt;td>30.8&lt;/td>\n&lt;td>41.4&lt;/td>\n&lt;td>46.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepSeek-R1-Distill-7B&lt;/td>\n&lt;td>69.6&lt;/td>\n&lt;td>18.8&lt;/td>\n&lt;td>85.0&lt;/td>\n&lt;td>33.4&lt;/td>\n&lt;td>51.7&lt;/td>\n&lt;td>51.9&lt;/td>\n&lt;td>8.3&lt;/td>\n&lt;td>78.2&lt;/td>\n&lt;td>32.7&lt;/td>\n&lt;td>42.7&lt;/td>\n&lt;td>47.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-7B&lt;/td>\n&lt;td>&lt;b>76.2&lt;/b>&lt;/td>\n&lt;td>&lt;b>22.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>86.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>36.0&lt;/b>&lt;/td>\n&lt;td>&lt;b>55.4&lt;/b>&lt;/td>\n&lt;td>&lt;b>62.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>9.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>82.9&lt;/b>&lt;/td>\n&lt;td>&lt;b>34.9&lt;/b>&lt;/td>\n&lt;td>&lt;b>47.5&lt;/b>&lt;/td>\n&lt;td>&lt;b>51.5&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 3:** Results of GenPRM with different label estimation method and threshold on ProcessBench, reported with Pass@1. The best results are shown in **bold**.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Estimation Method&lt;/th>\n&lt;th>Positive Label Criterion&lt;/th>\n&lt;th>GSM8K&lt;/th>\n&lt;th>MATH&lt;/th>\n&lt;th>Olympiad Bench&lt;/th>\n&lt;th>Omni-MATH&lt;/th>\n&lt;th>Avg.&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>&lt;math>P_t = MC(s_t, a_t)&lt;/math> (hard label)&lt;/td>\n&lt;td>&lt;math>P_t &gt; 0&lt;/math>&lt;/td>\n&lt;td>72.9&lt;/td>\n&lt;td>78.9&lt;/td>\n&lt;td>&lt;b>73.2&lt;/b>&lt;/td>\n&lt;td>68.0&lt;/td>\n&lt;td>73.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"3\">&lt;math>P_t = MC(s_t, a_t) - MC(s_t)&lt;/math>&lt;/td>\n&lt;td>&lt;math>P_t \\geq -0.1&lt;/math>&lt;/td>\n&lt;td>77.3&lt;/td>\n&lt;td>79.9&lt;/td>\n&lt;td>70.8&lt;/td>\n&lt;td>68.5&lt;/td>\n&lt;td>74.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq -0.3&lt;/math>&lt;/td>\n&lt;td>76.8&lt;/td>\n&lt;td>79.6&lt;/td>\n&lt;td>71.1&lt;/td>\n&lt;td>69.0&lt;/td>\n&lt;td>74.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq -0.5&lt;/math>&lt;/td>\n&lt;td>75.8&lt;/td>\n&lt;td>80.2&lt;/td>\n&lt;td>72.8&lt;/td>\n&lt;td>68.6&lt;/td>\n&lt;td>74.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"4\">&lt;math>P_t = \\frac{MC(s_t, a_t)}{MC(s_t)}&lt;/math>&lt;/td>\n&lt;td>&lt;math>P_t \\geq 0.1&lt;/math>&lt;/td>\n&lt;td>74.8&lt;/td>\n&lt;td>78.7&lt;/td>\n&lt;td>71.6&lt;/td>\n&lt;td>68.7&lt;/td>\n&lt;td>73.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq 0.5&lt;/math>&lt;/td>\n&lt;td>75.7&lt;/td>\n&lt;td>79.2&lt;/td>\n&lt;td>70.4&lt;/td>\n&lt;td>68.5&lt;/td>\n&lt;td>73.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq 0.8&lt;/math>&lt;/td>\n&lt;td>&lt;b>78.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>80.3&lt;/b>&lt;/td>\n&lt;td>72.2&lt;/td>\n&lt;td>&lt;b>69.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>75.2&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq 1.0&lt;/math>&lt;/td>\n&lt;td>76.4&lt;/td>\n&lt;td>77.4&lt;/td>\n&lt;td>68.1&lt;/td>\n&lt;td>67.2&lt;/td>\n&lt;td>72.3&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 4:** Results of GenPRM with different label estimation method and threshold on ProcessBench, reported with Maj@8. The best results are shown in **bold**.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Estimation Method&lt;/th>\n&lt;th>Positive Label Criterion&lt;/th>\n&lt;th>GSM8K&lt;/th>\n&lt;th>MATH&lt;/th>\n&lt;th>Olympiad Bench&lt;/th>\n&lt;th>Omni-MATH&lt;/th>\n&lt;th>Avg.&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>&lt;math>P_t = MC(s_t, a_t)&lt;/math> (hard label)&lt;/td>\n&lt;td>&lt;math>P_t &gt; 0&lt;/math>&lt;/td>\n&lt;td>75.1&lt;/td>\n&lt;td>83.8&lt;/td>\n&lt;td>&lt;b>80.6&lt;/b>&lt;/td>\n&lt;td>74.4&lt;/td>\n&lt;td>78.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"3\">&lt;math>P_t = MC(s_t, a_t) - MC(s_t)&lt;/math>&lt;/td>\n&lt;td>&lt;math>P_t \\geq -0.1&lt;/math>&lt;/td>\n&lt;td>79.8&lt;/td>\n&lt;td>85.1&lt;/td>\n&lt;td>78.0&lt;/td>\n&lt;td>74.5&lt;/td>\n&lt;td>79.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq -0.3&lt;/math>&lt;/td>\n&lt;td>80.9&lt;/td>\n&lt;td>&lt;b>86.5&lt;/b>&lt;/td>\n&lt;td>78.1&lt;/td>\n&lt;td>75.0&lt;/td>\n&lt;td>80.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq -0.5&lt;/math>&lt;/td>\n&lt;td>78.1&lt;/td>\n&lt;td>85.6&lt;/td>\n&lt;td>79.1&lt;/td>\n&lt;td>73.4&lt;/td>\n&lt;td>79.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"4\">&lt;math>P_t = \\frac{MC(s_t, a_t)}{MC(s_t)}&lt;/math>&lt;/td>\n&lt;td>&lt;math>P_t \\geq 0.1&lt;/math>&lt;/td>\n&lt;td>77.0&lt;/td>\n&lt;td>84.6&lt;/td>\n&lt;td>78.1&lt;/td>\n&lt;td>75.3&lt;/td>\n&lt;td>78.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq 0.5&lt;/math>&lt;/td>\n&lt;td>78.0&lt;/td>\n&lt;td>85.2&lt;/td>\n&lt;td>78.2&lt;/td>\n&lt;td>74.3&lt;/td>\n&lt;td>78.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq 0.8&lt;/math>&lt;/td>\n&lt;td>81.0&lt;/td>\n&lt;td>85.7&lt;/td>\n&lt;td>78.4&lt;/td>\n&lt;td>&lt;b>76.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>80.5&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq 1.0&lt;/math>&lt;/td>\n&lt;td>&lt;b>81.1&lt;/b>&lt;/td>\n&lt;td>84.1&lt;/td>\n&lt;td>76.0&lt;/td>\n&lt;td>74.7&lt;/td>\n&lt;td>79.0&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Reasoning Components.** To understand how each reasoning component influence GenPRM, we conduct experiments by training GenPRM with: (1) CoT data only, (2) code verification data only, and (3) full data. During inference phase, we also compare several variants. For example, GenPRM trained with full data can be used to only verify each step with CoT only by stopping generation at `&lt;/analyze>` token. The results in Table 5 show that: (1) the improvement of GenPRM mainly comesfrom CoT reasoning; (2) generating code and reasoning with code execution result improves the process verification performance as well.\n\n**Table 5:** Results on ProcessBench of GenPRM with different reasoning components, reported with Maj@8. The best results are shown in **bold**.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th colspan=\"2\">Training&lt;/th>",
      "numLines": 800,
      "startLine": 0,
      "totalLines": 2164
    }
  },
  "sourceToolAssistantUUID": "abf43550-7b71-4962-89c9-4b62e163ab36",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 37 · 2026-05-28T05:07:01.552Z_

```json
{
  "parentUuid": "63961e89-9b3e-439d-b9ab-bb06e4efa11c",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "1bbc7fd6-b071-4094-8eb2-a361b5f5bae8",
  "timestamp": "2026-05-28T05:07:01.552Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-28 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "1bbc7fd6-b071-4094-8eb2-a361b5f5bae8",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze GenPRM paper innovation and research craft",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5"
}
```

---

### Tool call

_source line 40 · 2026-05-28T05:07:07.788Z_

<details open><summary>🔧 Tool call — Read · `toolu_01E9RFLmm6B2xpZxgtpcGaV4`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/d13ca6d2-ab23-4990-8414-c3096bb93ab5/tool-results/toolu_01GSHgkEVx98FPEy2wEtpX5x.txt",
  "limit": 600,
  "offset": 800
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bbc7fd6-b071-4094-8eb2-a361b5f5bae8",
  "isSidechain": false,
  "requestId": "req_011CbUPNh1Y515nBfUYfDGSG",
  "type": "assistant",
  "uuid": "df00442e-7ad9-4db2-a442-aa3ed4edac30",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWtJRdfZEwD74TWcBh5KjD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17135,
      "cache_read_input_tokens": 23543,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17135,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 23543,
          "cache_creation_input_tokens": 17135,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17135
          },
          "type": "message"
        }
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

_source line 41 · 2026-05-28T05:07:08.081Z_

<details><summary>↩ Tool result · `toolu_01E9RFLmm6B2xpZxgtpcGaV4`</summary>

`````text
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
`````

</details>

<details><summary>Recorded metadata</summary>

`````json
{
  "recorded_role": "user",
  "parentUuid": "df00442e-7ad9-4db2-a442-aa3ed4edac30",
  "isSidechain": false,
  "promptId": "a37d06a3-a1b2-4f5b-ba56-06aaf32ddf9c",
  "type": "user",
  "uuid": "8e52e9ac-1711-4d7a-b289-0e35d4b2c3b1",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/d13ca6d2-ab23-4990-8414-c3096bb93ab5/tool-results/toolu_01GSHgkEVx98FPEy2wEtpX5x.txt",
      "content": "&lt;th colspan=\"2\">Training&lt;/th>\n&lt;th colspan=\"3\">Inference&lt;/th>\n&lt;th rowspan=\"2\">GSM8K&lt;/th>\n&lt;th rowspan=\"2\">MATH&lt;/th>\n&lt;th rowspan=\"2\">Olympiad Bench&lt;/th>\n&lt;th rowspan=\"2\">Omni-MATH&lt;/th>\n&lt;th rowspan=\"2\">Avg.&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>CoT&lt;/th>\n&lt;th>Code&lt;/th>\n&lt;th>CoT&lt;/th>\n&lt;th>Code&lt;/th>\n&lt;th>Code Exec.&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>x&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>63.9&lt;/td>\n&lt;td>65.8&lt;/td>\n&lt;td>54.5&lt;/td>\n&lt;td>55.9&lt;/td>\n&lt;td>60.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>x&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>67.0&lt;/td>\n&lt;td>70.8&lt;/td>\n&lt;td>61.6&lt;/td>\n&lt;td>57.4&lt;/td>\n&lt;td>64.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>x&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>70.6&lt;/td>\n&lt;td>76.6&lt;/td>\n&lt;td>67.3&lt;/td>\n&lt;td>63.9&lt;/td>\n&lt;td>69.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>✓&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>76.4&lt;/td>\n&lt;td>83.0&lt;/td>\n&lt;td>&lt;b>80.5&lt;/b>&lt;/td>\n&lt;td>75.4&lt;/td>\n&lt;td>78.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"5\">✓&lt;/td>\n&lt;td rowspan=\"5\">✓&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>60.1&lt;/td>\n&lt;td>66.7&lt;/td>\n&lt;td>59.9&lt;/td>\n&lt;td>59.2&lt;/td>\n&lt;td>61.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>x&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>61.3&lt;/td>\n&lt;td>74.7&lt;/td>\n&lt;td>68.1&lt;/td>\n&lt;td>62.0&lt;/td>\n&lt;td>66.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>✓&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>78.8&lt;/td>\n&lt;td>85.1&lt;/td>\n&lt;td>78.7&lt;/td>\n&lt;td>74.9&lt;/td>\n&lt;td>79.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>&lt;b>81.0&lt;/b>&lt;/td>\n&lt;td>85.1&lt;/td>\n&lt;td>78.1&lt;/td>\n&lt;td>75.5&lt;/td>\n&lt;td>79.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>&lt;b>81.0&lt;/b>&lt;/td>\n&lt;td>&lt;b>85.7&lt;/b>&lt;/td>\n&lt;td>78.4&lt;/td>\n&lt;td>&lt;b>76.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>80.5&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n## 5. Related Work\n\n**Process Reward Models.** Process reward models have been proved to be effective for providing step-wise scores and are superior to outcome reward models in mathematical reasoning tasks (Uesato et al., 2022; Lightman et al., 2024). However, annotating a process supervision dataset such as PRM800K (Lightman et al., 2024) requires significant human costs. To mitigate this cost, prior works utilize Monte Carlo estimation (Wang et al., 2024b) and binary search (Luo et al., 2024) for automated label generation. Subsequent research improves PRMs through methods such as advantage modeling (Setlur et al., 2025),  $Q$ -value rankings (Li and Li, 2025), implicit entropy regularization (Zhang et al., 2024a), retrieval-augmented generation (Zhu et al., 2025), and fast-slow verification (Zhong et al., 2025). Furthermore, the community has developed high-quality open-source PRMs, including the RLHFlow series (Xiong et al., 2024), Math-psa (Wang et al., 2024a), Skywork series (Skywork o1 Team, 2024), and Qwen2.5-Math series (Zheng et al., 2024; Zhang et al., 2025c). Recently, a line of works focus on extending PRMs to other tasks, including coding (Zhang et al., 2024b), medical tasks (Jiang et al., 2025), agentic tasks (Choudhury, 2025), general domain tasks (Zhang et al., 2025a; Zeng et al., 2025), and multimodal tasks (Wang et al., 2025). Current studies also focus on benchmarking PRMs (Zheng et al., 2024; Song et al., 2025) to systematically evaluate their performance.\n\n**Large Language Model Test-Time Scaling.** Scaling test-time computation is an effective method for improving performance during the inference phase (OpenAI, 2024a,b; DeepSeek-AI et al., 2025). TTS is commonly implemented with external verifiers (e.g., ORMs and PRMs) or strategies (e.g., beam search and MCTS) (Wu et al., 2025; Snell et al., 2025; Beeching et al., 2024; Liu et al., 2025). In this work, we scale the test-time computation of a generative PRM with an explicit reasoning process and GenPRM can also serve as a verifier or a critic model in external TTS.\n\n**Enhancing the Generative Abilities of Reward Models.** Previous research has investigated methods to enhance the generative capabilities of reward models using CoT reasoning (Ankner et al., 2024; Zhang et al., 2025b; Mahan et al., 2024). For instance, CCloud reward models (Ankner et al., 2024) are trained to generate critiques for responses and predict rewards using an additional rewardhead. GenRM-CoT (Zhang et al., 2025b) and GenRM (Mahan et al., 2024) train generative reward models that perform CoT reasoning before making final predictions via SFT and preference learning, respectively. CTRL (Xie et al., 2025) demonstrates that critic models exhibit strong discriminative abilities when utilized as generative reward models. Prior to these works, GRM (Yang et al., 2024c) regularizes the hidden states of reward models with a text generation loss.\n\n## 6. Conclusion\n\nIn this work, we propose GenPRM, a generative process reward model that performs explicit reasoning and code verification for process supervision and enables scaling the test-time compute of PRMs. Experimental results on ProcessBench and several mathematical datasets show GenPRM outperforms prior PRMs. We also demonstrate that the performance of GenPRM increases via test-time scaling and GenPRM is effective as a critic model. We believe that this work provides perspectives on PRMs by demonstrating the strong TTS abilities of PRMs and extending the applications of PRMs.\n\n**Limitations.** First, GenPRM provides process supervision by generative reasoning, which introduces additional computation during inference phase. Future work will investigate how to prune the reasoning process dynamically (Zhong et al., 2025). Although GenPRM focuses mainly on mathematical reasoning tasks, it is worth to explore how to apply generative reasoning on coding and general reasoning tasks in the future (Zhang et al., 2025a). Additionally, it would be interesting to leverage RL to incentivize the generative reasoning abilities of GenPRM.\n\n## References\n\nAI-MO. AIME 2024, 2024a. URL &lt;https://huggingface.co/datasets/AI-MO/aimo-validation-aimo>.\n\nAI-MO. AMC 2023, 2024b. URL &lt;https://huggingface.co/datasets/AI-MO/aimo-validation-amc>.\n\nZachary Ankner, Mansheej Paul, Brandon Cui, Jonathan D Chang, and Prithviraj Ammanabrolu. Critique-out-Loud Reward Models. *arXiv preprint arXiv:2408.11791*, 2024.\n\nAnthropic. Introducing Claude, 2023. URL &lt;https://www.anthropic.com/index/introducing-claude/>.\n\nEdward Beeching, Lewis Tunstall, and Sasha Rush. Scaling Test-Time Compute with Open Models, 2024. URL &lt;https://huggingface.co/spaces/HuggingFaceH4/blogpost-scaling-test-time-compute>.\n\nBradley Brown, Jordan Juravsky, Ryan Ehrlich, Ronald Clark, Quoc V Le, Christopher Ré, and Azalia Mirhoseini. Large Language Monkeys: Scaling Inference Compute with Repeated Sampling. *arXiv preprint arXiv:2407.21787*, 2024.\n\nSanjiban Choudhury. Process Reward Models for LLM Agents: Practical Framework and Directions. *arXiv preprint arXiv:2502.10325*, 2025.\n\nGanqu Cui, Lifan Yuan, Zefan Wang, Hanbin Wang, Wendi Li, Bingxiang He, Yuchen Fan, Tianyu Yu, Qixin Xu, Weize Chen, et al. Process Reinforcement through Implicit Rewards. *arXiv preprint arXiv:2502.01456*, 2025.DeepSeek-AI, Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, Xiaokang Zhang, Xingkai Yu, Yu Wu, Z. F. Wu, Zhibin Gou, Zhihong Shao, Zhuoshu Li, Ziyi Gao, Aixin Liu, Bing Xue, Bingxuan Wang, Bochao Wu, Bei Feng, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chenyu Zhang, Chong Ruan, Damai Dai, Deli Chen, Dongjie Ji, Erhang Li, Fangyun Lin, Fucong Dai, Fuli Luo, Guangbo Hao, Guanting Chen, Guowei Li, H. Zhang, Han Bao, Hanwei Xu, Haocheng Wang, Honghui Ding, Huajian Xin, Huazuo Gao, Hui Qu, Hui Li, Jianzhong Guo, Jiashi Li, Jiawei Wang, Jingchang Chen, Jingyang Yuan, Junjie Qiu, Junlong Li, J. L. Cai, Jiaqi Ni, Jian Liang, Jin Chen, Kai Dong, Kai Hu, Kaige Gao, Kang Guan, Kexin Huang, Kuai Yu, Lean Wang, Lecong Zhang, Liang Zhao, Litong Wang, Liyue Zhang, Lei Xu, Leyi Xia, Mingchuan Zhang, Minghua Zhang, Minghui Tang, Meng Li, Miaojun Wang, Mingming Li, Ning Tian, Panpan Huang, Peng Zhang, Qiancheng Wang, Qinyu Chen, Qiushi Du, Ruiqi Ge, Ruisong Zhang, Ruizhe Pan, Runji Wang, R. J. Chen, R. L. Jin, Ruyi Chen, Shanghao Lu, Shangyan Zhou, Shanhuang Chen, Shengfeng Ye, Shiyu Wang, Shuiping Yu, Shunfeng Zhou, Shuting Pan, S. S. Li, Shuang Zhou, Shaoqing Wu, Shengfeng Ye, Tao Yun, Tian Pei, Tianyu Sun, T. Wang, Wangding Zeng, Wanjia Zhao, Wen Liu, Wenfeng Liang, Wenjun Gao, Wenqin Yu, Wentao Zhang, W. L. Xiao, Wei An, Xiaodong Liu, Xiaohan Wang, Xiaokang Chen, Xiaotao Nie, Xin Cheng, Xin Liu, Xin Xie, Xingchao Liu, Xinyu Yang, Xinyuan Li, Xuecheng Su, Xuheng Lin, X. Q. Li, Xiangyue Jin, Xiaojin Shen, Xiaosha Chen, Xiaowen Sun, Xiaoxiang Wang, Xinnan Song, Xinyi Zhou, Xianzu Wang, Xinxia Shan, Y. K. Li, Y. Q. Wang, Y. X. Wei, Yang Zhang, Yanhong Xu, Yao Li, Yao Zhao, Yaofeng Sun, Yaohui Wang, Yi Yu, Yichao Zhang, Yifan Shi, Yiliang Xiong, Ying He, Yishi Piao, Yisong Wang, Yixuan Tan, Yiyang Ma, Yiyuan Liu, Yongqiang Guo, Yuan Ou, Yuduan Wang, Yue Gong, Yuheng Zou, Yujia He, Yunfan Xiong, Yuxiang Luo, Yuxiang You, Yuxuan Liu, Yuyang Zhou, Y. X. Zhu, Yanhong Xu, Yanping Huang, Yaohui Li, Yi Zheng, Yuchen Zhu, Yunxian Ma, Ying Tang, Yukun Zha, Yuting Yan, Z. Z. Ren, Zehui Ren, Zhangli Sha, Zhe Fu, Zhean Xu, Zhenda Xie, Zhengyan Zhang, Zhewen Hao, Zhicheng Ma, Zhigang Yan, Zhiyu Wu, Zihui Gu, Zijia Zhu, Zijun Liu, Zilin Li, Ziwei Xie, Ziyang Song, Zizheng Pan, Zhen Huang, Zhipeng Xu, Zhongyu Zhang, and Zhen Zhang. DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning. *arXiv preprint arXiv:2501.12948*, 2025.\n\nGemma Team and Google DeepMind. Introducing Gemma 3: The most capable model you can run on a single GPU or TPU, March 2025. URL &lt;https://blog.google/technology/developers/gemma-3>.\n\nZhibin Gou, Zhihong Shao, Yeyun Gong, yelong shen, Yujiu Yang, Nan Duan, and Weizhu Chen. CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing. In *International Conference on Learning Representations (ICLR)*, 2024. URL &lt;https://openreview.net/forum?id=Sx038qxjek>.\n\nDan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. Measuring Mathematical Problem Solving With the MATH Dataset. In *Advances in Neural Information Processing Systems Datasets and Benchmarks Track (Round 2)*, 2021. URL &lt;https://openreview.net/forum?id=7Bywt2mQsCe>.\n\nShuyang Jiang, Yusheng Liao, Zhe Chen, Ya Zhang, Yanfeng Wang, and Yu Wang. MedS&lt;sup>3&lt;/sup>: Towards Medical Small Language Models with Self-Evolved Slow Thinking. *arXiv preprint arXiv:2501.12051*, 2025.\n\nAitor Lewkowycz, Anders Andreassen, David Dohan, Ethan Dyer, Henryk Michalewski, Vinay Ramasesh, Ambrose Slone, Cem Anil, Imanol Schlag, Theo Gutman-Solo, Yuhuai Wu, Behnam Neyshabur, Guy Gur-Ari, and Vedant Misra. Solving Quantitative Reasoning Problems with Language Models. In S. Koyejo, S. Mohamed, A. Agarwal, D. Belgrave, K. Cho, and A. Oh, editors,*Advances in Neural Information Processing Systems (NeurIPS)*, volume 35, pages 3843–3857. Curran Associates, Inc., 2022. URL [https://proceedings.neurips.cc/paper\\\\_files/paper/2022/file/18abbeef8cfe9203fdf9053c9c4fe191-Paper-Conference.pdf](https://proceedings.neurips.cc/paper_files/paper/2022/file/18abbeef8cfe9203fdf9053c9c4fe191-Paper-Conference.pdf).\n\nWendi Li and Yixuan Li. Process Reward Model with Q-value Rankings. In *International Conference on Learning Representations (ICLR)*, 2025. URL &lt;https://openreview.net/forum?id=wQEdh2cgEk>.\n\nHunter Lightman, Vineet Kosaraju, Yuri Burda, Harrison Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. Let’s Verify Step by Step. In *International Conference on Learning Representations (ICLR)*, 2024. URL &lt;https://openreview.net/forum?id=v8L0pN6E0i>.\n\nRunze Liu, Fengshuo Bai, Yali Du, and Yaodong Yang. Meta-Reward-Net: Implicitly Differentiable Reward Learning for Preference-based Reinforcement Learning. In *Advances in Neural Information Processing Systems (NeurIPS)*, volume 35, pages 22270–22284, 2022.\n\nRunze Liu, Yali Du, Fengshuo Bai, Jiafei Lyu, and Xiu Li. PEARL: Zero-shot Cross-task Preference Alignment and Robust Reward Learning for Robotic Manipulation. In Ruslan Salakhutdinov, Zico Kolter, Katherine Heller, Adrian Weller, Nuria Oliver, Jonathan Scarlett, and Felix Berkenkamp, editors, *International Conference on Machine Learning (ICML)*, volume 235 of *Proceedings of Machine Learning Research*, pages 30946–30964. PMLR, 21–27 Jul 2024. URL &lt;https://proceedings.mlr.press/v235/liu24o.html>.\n\nRunze Liu, Junqi Gao, Jian Zhao, Kaiyan Zhang, Xiu Li, Biqing Qi, Wanli Ouyang, and Bowen Zhou. Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling. *arXiv preprint arXiv:2502.06703*, 2025.\n\nLiangchen Luo, Yinxiao Liu, Rosanne Liu, Samrat Phatale, Harsh Lara, Yunxuan Li, Lei Shu, Yun Zhu, Lei Meng, Jiao Sun, et al. Improve Mathematical Reasoning in Language Models by Automated Process Supervision. *arXiv preprint arXiv:2406.06592*, 2024.\n\nAman Madaan, Niket Tandon, Prakash Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegr-effe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, Shashank Gupta, Bodhisattwa Prasad Majumder, Katherine Hermann, Sean Welleck, Amir Yazdanbakhsh, and Peter Clark. Self-Refine: Iterative Refinement with Self-Feedback. In A. Oh, T. Nau-mann, A. Globerson, K. Saenko, M. Hardt, and S. Levine, editors, *Advances in Neural Information Processing Systems (NeurIPS)*, volume 36, pages 46534–46594. Curran Associates, Inc., 2023. URL [https://proceedings.neurips.cc/paper\\\\_files/paper/2023/file/91edff07232fb1b55a505a9e9f6c0ff3-Paper-Conference.pdf](https://proceedings.neurips.cc/paper_files/paper/2023/file/91edff07232fb1b55a505a9e9f6c0ff3-Paper-Conference.pdf).\n\nDakota Mahan, Duy Van Phung, Rafael Rafailov, Chase Blagden, Nathan Lile, Louis Castricato, Jan-Philipp Fränken, Chelsea Finn, and Alon Albalak. Generative Reward Models. *arXiv preprint arXiv:2410.12832*, 2024.\n\nOpenAI. GPT-4 Technical Report. *arXiv preprint arXiv:2303.08774*, 2023.\n\nOpenAI. Learning to reason with LLMs, 2024a. URL &lt;https://openai.com/index/learning-to-reason-with-llms>.\n\nOpenAI. OpenAI o3-mini, 2024b. URL &lt;https://openai.com/index/openai-o3-mini>.\n\nQwen Team. QwQ-32B: Embracing the Power of Reinforcement Learning, March 2025. URL &lt;https://qwenlm.github.io/blog/qwq-32b>.Amrith Setlur, Chirag Nagpal, Adam Fisch, Xinyang Geng, Jacob Eisenstein, Rishabh Agarwal, Alekh Agarwal, Jonathan Berant, and Aviral Kumar. Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning. In *International Conference on Learning Representations (ICLR)*, 2025. URL &lt;https://openreview.net/forum?id=A6Y7AqlzLW>.\n\nZhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li, Y Wu, et al. DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models. *arXiv preprint arXiv:2402.03300*, 2024.\n\nSkywork o1 Team. Skywork-o1 Open Series. &lt;https://huggingface.co/Skywork>, November 2024. URL &lt;https://huggingface.co/Skywork>.\n\nCharlie Victor Snell, Jaehoon Lee, Kelvin Xu, and Aviral Kumar. Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning. In *International Conference on Learning Representations (ICLR)*, 2025. URL &lt;https://openreview.net/forum?id=4FWAwZtd2n>.\n\nMingyang Song, Zhaochen Su, Xiaoye Qu, Jiawei Zhou, and Yu Cheng. PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models. *arXiv preprint arXiv:2501.03124*, 2025.\n\nXiaoyu Tan, Tianchu Yao, Chao Qu, Bin Li, Minghao Yang, Dakuan Lu, Haozhe Wang, Xihe Qiu, Wei Chu, Yinghui Xu, et al. AURORA: Automated Training Framework of Universal Process Reward Models via Ensemble Prompting and Reverse Verification. *arXiv preprint arXiv:2502.11520*, 2025.\n\nJonathan Uesato, Nate Kushman, Ramana Kumar, Francis Song, Noah Siegel, Lisa Wang, Antonia Creswell, Geoffrey Irving, and Irina Higgins. Solving math word problems with process-and outcome-based feedback. *arXiv preprint arXiv:2211.14275*, 2022.\n\nJun Wang, Meng Fang, Ziyu Wan, Muning Wen, Jiachen Zhu, Anjie Liu, Ziqin Gong, Yan Song, Lei Chen, Lionel M Ni, et al. OpenR: An open source framework for advanced reasoning with large language models. *arXiv preprint arXiv:2410.09671*, 2024a.\n\nPeiyi Wang, Lei Li, Zhihong Shao, Runxin Xu, Damai Dai, Yifei Li, Deli Chen, Yu Wu, and Zhifang Sui. Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations. In *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 9426–9439, 2024b.\n\nWeiyun Wang, Zhangwei Gao, Lianjie Chen, Chen Zhe, Jinguo Zhu, Xiangyu Zhao, Yangzhou Liu, Yue Cao, Shenglong Ye, Xizhou Zhu, Lewei Lu, Haodong Duan, Yu Qiao, Jifeng Dai, and Wenhai Wang. VisualPRM: An Effective Process Reward Model for Multimodal Reasoning. *arXiv preprint arXiv:2503.10291*, 2025.\n\nXuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V Le, Ed H. Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. Self-Consistency Improves Chain of Thought Reasoning in Language Models. In *International Conference on Learning Representations (ICLR)*, 2023. URL &lt;https://openreview.net/forum?id=1PL1NIMMrw>.\n\nJason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models. In *Advances in neural information processing systems (NeurIPS)*, volume 35, pages 24824–24837, 2022.Yangzhen Wu, Zhiqing Sun, Shanda Li, Sean Welleck, and Yiming Yang. Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for LLM Problem-Solving. In *International Conference on Learning Representations (ICLR)*, 2025. URL &lt;https://openreview.net/forum?id=VNckp7JEHn>.\n\nZhihui Xie, Liyu Chen, Weichao Mao, Jingjing Xu, Lingpeng Kong, et al. Teaching Language Models to Critique via Reinforcement Learning. *arXiv preprint arXiv:2502.03492*, 2025.\n\nWei Xiong, Hanning Zhang, Nan Jiang, and Tong Zhang. An Implementation of Generative PRM. &lt;https://github.com/RLHFlow/RLHF-Reward-Modeling>, 2024.\n\nAn Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng Liu, Fei Huang, Haoran Wei, Huan Lin, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin Yang, Jiaxi Yang, Jingren Zhou, Junyang Lin, Kai Dang, Keming Lu, Keqin Bao, Kexin Yang, Le Yu, Mei Li, Mingfeng Xue, Pei Zhang, Qin Zhu, Rui Men, Runji Lin, Tianhao Li, Tingyu Xia, Xingzhang Ren, Xuancheng Ren, Yang Fan, Yang Su, Yichang Zhang, Yu Wan, Yuqiong Liu, Zeyu Cui, Zhenru Zhang, and Zihan Qiu. Qwen2.5 Technical Report. *arXiv preprint arXiv:2412.15115*, 2024a.\n\nAn Yang, Beichen Zhang, Binyuan Hui, Bofei Gao, Bowen Yu, Chengpeng Li, Dayiheng Liu, Jianhong Tu, Jingren Zhou, Junyang Lin, Keming Lu, Mingfeng Xue, Runji Lin, Tianyu Liu, Xingzhang Ren, and Zhenru Zhang. Qwen2.5-Math Technical Report: Toward Mathematical Expert Model via Self-Improvement. *arXiv preprint arXiv:2409.12122*, 2024b.\n\nRui Yang, Ruomeng Ding, Yong Lin, Huan Zhang, and Tong Zhang. Regularizing Hidden States Enables Learning Generalizable Reward Model for LLMs. In *Advances in Neural Information Processing Systems (NeurIPS)*, 2024c. URL &lt;https://openreview.net/forum?id=jwh9MHEfmY>.\n\nLifan Yuan, Wendi Li, Huayu Chen, Ganqu Cui, Ning Ding, Kaiyan Zhang, Bowen Zhou, Zhiyuan Liu, and Hao Peng. Free Process Rewards without Process Labels. *arXiv preprint arXiv:2412.01981*, 2024.\n\nThomas Zeng, Shuibai Zhang, Shutong Wu, Christian Classen, Daewon Chae, Ethan Ewer, Minjiae Lee, Heeju Kim, Wonjun Kang, Jackson Kunde, et al. VersaPRM: Multi-Domain Process Reward Model via Synthetic Reasoning Data. *arXiv preprint arXiv:2502.06737*, 2025.\n\nHanning Zhang, Pengcheng Wang, Shizhe Diao, Yong Lin, Rui Pan, Hanze Dong, Dylan Zhang, Pavlo Molchanov, and Tong Zhang. Entropy-Regularized Process Reward Model. *arXiv preprint arXiv:2412.11006*, 2024a.\n\nKaiyan Zhang, Jiayuan Zhang, Haoxin Li, Xuekai Zhu, Ermo Hua, Xingtai Lv, Ning Ding, Biqing Qi, and Bowen Zhou. OpenPRM: Building Open-domain Process-based Reward Models with Preference Trees. In *International Conference on Learning Representations (ICLR)*, 2025a. URL &lt;https://openreview.net/forum?id=fGIqGfmgkW>.\n\nLunjun Zhang, Arian Hosseini, Hritik Bansal, Mehran Kazemi, Aviral Kumar, and Rishabh Agarwal. Generative Verifiers: Reward Modeling as Next-Token Prediction. In *International Conference on Learning Representations (ICLR)*, 2025b. URL &lt;https://openreview.net/forum?id=Ccwp4tFETe>.\n\nYuxiang Zhang, Shangxi Wu, Yuqi Yang, Jiangming Shu, Jinlin Xiao, Chao Kong, and Jitao Sang. o1-Coder: an o1 Replication for Coding. *arXiv preprint arXiv:2412.00154*, 2024b.\n\nZhenru Zhang, Chujie Zheng, Yangzhen Wu, Beichen Zhang, Runji Lin, Bowen Yu, Dayiheng Liu, Jingren Zhou, and Junyang Lin. The Lessons of Developing Process Reward Models in Mathematical Reasoning. *arXiv preprint arXiv:2501.07301*, 2025c.Chujie Zheng, Zhenru Zhang, Beichen Zhang, Runji Lin, Keming Lu, Bowen Yu, Dayiheng Liu, Jingren Zhou, and Junyang Lin. ProcessBench: Identifying Process Errors in Mathematical Reasoning. *arXiv preprint arXiv:2412.06559*, 2024.\n\nLianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, Hao Zhang, Joseph E Gonzalez, and Ion Stoica. Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. In A. Oh, T. Nau-mann, A. Globerson, K. Saenko, M. Hardt, and S. Levine, editors, *Advances in Neural Information Processing Systems (NeurIPS)*, volume 36, pages 46595–46623. Curran Associates, Inc., 2023. URL [https://proceedings.neurips.cc/paper\\\\_files/paper/2023/file/91f18a1287b398d378ef22505bf41832-Paper-Datasets\\\\_and\\\\_Benchmarks.pdf](https://proceedings.neurips.cc/paper_files/paper/2023/file/91f18a1287b398d378ef22505bf41832-Paper-Datasets_and_Benchmarks.pdf).\n\nJianyuan Zhong, Zeju Li, Zhijian Xu, Xiangyu Wen, and Qiang Xu. Dyve: Thinking Fast and Slow for Dynamic Process Verification. *arXiv preprint arXiv:2502.11157*, 2025.\n\nJiachen Zhu, Congmin Zheng, Jianghao Lin, Kounianhua Du, Ying Wen, Yong Yu, Jun Wang, and Weinan Zhang. Retrieval-Augmented Process Reward Model for Generalizable Mathematical Reasoning. *arXiv preprint arXiv:2502.14361*, 2025.\n\nXuekai Zhu, Biqing Qi, Kaiyan Zhang, Xinwei Long, Zhouhan Lin, and Bowen Zhou. PaD: Program-aided Distillation Can Teach Small Models Reasoning Better than Chain-of-thought Fine-tuning. In Kevin Duh, Helena Gomez, and Steven Bethard, editors, *Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)*, pages 2571–2597, Mexico City, Mexico, June 2024. Association for Computational Linguistics. doi: 10.18653/v1/2024.naacl-long.142. URL &lt;https://aclanthology.org/2024.naacl-long.142/>.## A. Experimental Details\n\n### A.1. Scoring and Voting Methods\n\n**PRM-Last.** PRM-Last considers the process reward of the last step of the entire LLM response as the final score, i.e.,  $\\text{score} = r_T$ .\n\n**PRM-Avg.** PRM-Avg computes the mean process reward across all steps as the final score, i.e.,  $\\text{score} = \\frac{1}{T} \\sum_{t=1}^T r_t$ .\n\n**PRM-Min.** PRM-Min uses the minimum process reward across all steps as the final score, i.e.,  $\\text{score} = \\min_r \\{r_t\\}_{t=1}^T$ .\n\n### A.2. Implementation Details\n\nPrompt for CoT and code rationale generation is shown in Table A.2.\n\n#### Prompt for CoT and code rationale generation\n\n**[System]:**\n\nYou are a math teacher. Your task is to review and critique the paragraphs in solution step by step with python code.\n\n**[User]:**\n\nThe following is the math problem and a solution (split into paragraphs, enclosed with tags and indexed from 1):\n\n[Math Problem]\n\n{problem}\n\n[Solution]\n\n```\n&lt;paragraph_1>\n{solution_section_1}\n&lt;/paragraph_1>\n```\n\n...\n\n```\n&lt;paragraph_n>\n{solution_section_n}\n&lt;/paragraph_n>\n```\n\nYour task is to verify the correctness of paragraph in the solution. Split your verification by ‘### Paragraph {{ID}}’.\n\nYour verification for each paragraph should be constructed by 2 parts, wrapped by ‘&lt;analyze>&lt;/analyze>’ and ‘&lt;verify>&lt;/verify>’ separately.1. 1. In ‘`&lt;analyze>&lt;/analyze>`’ part, you need to analyze the reasoning process and explain why the paragraph is correct or incorrect in detail.\n2. 2. In ‘`&lt;verify>&lt;/verify>`’ part, you must write **Python code** in the form of ‘````python\\n{CODE}\\n````’ to verify every details that can be verified by code. You can import PyPI (i.e., ‘`sympy`’, ‘`scipy`’ and so on) to implement complicated calculation. Make sure to print the critic results in the code. Every code will be executed automatically by system. You need to analyze the ‘[Code Output]’ after code executing.\n\n>Pay attention that you must follow the format of ‘````python\\n{CODE}\\n````’ when you write the code, otherwise the code will not be executed.\n\nAfter all verifications, if you identify an error in a paragraph, return the **index** of the paragraph where the earliest error occurs\\*\\*. Otherwise, return the **index** of -1 (which typically denotes \"not found\"\\*\\*. Please put your final answer (i.e., the index) within box in the form of ‘`$\\boxed{{INDEX}}$`’.\n\nFollowing [Zheng et al. \\(2024\\)](#); [Zhang et al. \\(2025c\\)](#), we use the prompt in Table A.2 to evaluate LLM-as-a-judge methods on ProcessBench ([Zheng et al., 2024](#)).\n\n#### Evaluation prompt for LLM-as-a-judge methods on ProcessBench\n\nI will provide a math problem along with a solution. They will be formatted as follows:\n\n[Math Problem]\n\n```\n&lt;math_problem>\n...(math problem)...\n&lt;/math_problem>\n```\n\n[Solution]\n\n```\n&lt;paragraph_1>\n...(paragraph 1 of solution)...\n&lt;/paragraph_1>\n```\n\n...\n\n```\n&lt;paragraph_n>\n...(paragraph n of solution)...\n&lt;/paragraph_n>\n```\n\nYour task is to review each paragraph of the solution in sequence, analyzing, verifying, and critiquing the reasoning in detail. You need to provide the analyses and the conclusion in the following format:\n\n```\n&lt;analysis_1>\n...(analysis of paragraph 1)...\n&lt;/analysis_1>\n```...\n\n&lt;analysis\\_n>  \n ...(analysis of paragraph n)...  \n &lt;/analysis\\_n>\n\n&lt;conclusion>  \n Correct/Incorrect  \n &lt;/conclusion>\n\n\\* When you analyze each paragraph, you should use proper verification, recalculation, or reflection to indicate whether it is logically and mathematically valid. Please elaborate on the analysis process carefully.\n\n\\* If an error is detected in any paragraph, you should describe the nature and cause of the error in detail, and suggest how to correct the error or the correct approach. Once a paragraph is found to contain any error, stop further analysis of subsequent paragraphs (as they may depend on the identified error) and directly provide the conclusion of \"Incorrect.\"\n\nFor instance, given a solution of five paragraphs, if an error is found in the third paragraph, you should reply in the following format:\n\n&lt;analysis\\_1>  \n ...(analysis of paragraph 1)...  \n &lt;/analysis\\_1>\n\n&lt;analysis\\_2>  \n ...(analysis of paragraph 2)...  \n &lt;/analysis\\_2>\n\n&lt;analysis\\_3>  \n ...(analysis of paragraph 3; since an error is found here, also provide detailed critique and correction guideline)...  \n &lt;/analysis\\_3>\n\n&lt;conclusion>  \n Incorrect  \n &lt;/conclusion>\n\nNote that the analyses of paragraphs 4 and 5 should be skipped as the paragraph 3 has been found to contain an error.\n\n\\* Respond with your analyses and conclusion directly.\n\n---\n\nThe following is the math problem and the solution for you task:[Math Problem]\n\n{tagged\\_problem}\n\n[Solution]\n\n{tagged\\_response}\n\n#### Prompt for critique generation\n\n[User]:\n\nThe following is a math problem and my solution. Your task is to review and critique the paragraphs in solution step by step. Pay attention that you should not solve the problem and give the final answer. All of your task is to critique. Output your judgement of whether the paragraph is correct in the form of ‘ $\\boxed{\\{Yes|No\\}}$ ’ at the end of each paragraph verification:\n\n[Math Problem]\n\n{problem}\n\n[Solution]\n\n&lt;paragraph\\_{idx}>\n\n{solution\\_section}\n\n&lt;/paragraph\\_{idx}>\n\n## B. Additional Results\n\nWe provide full results of ProcessBench in Table 6.\n\n**Model Size.** We investigate the impact of model size on GenPRM by evaluating variants with 1.5B, 7B, and 32B parameters. As shown in Table 7, scaling the model from 1.5B to 7B parameters yields substantial performance gains (57.3  $\\rightarrow$  75.2 and 63.4  $\\rightarrow$  80.5). However, further increasing the model size to 32B provides only marginal improvements, suggesting that the 7B variant offers the best balance between efficiency and effectiveness.\n\n**Data Size.** To assess the influence of training data volume, we train GenPRM on progressively larger subsets of ProcessBench (25%, 50%, and 100% of the full dataset). Table 8 demonstrates that Pass@1 F1 scores improve rapidly with initial data increases, but the growth rate slows substantially with additional data.\n\n**Inference Tokens.** We provide statistics of the reasoning tokens per step and per response in Table 9.**Table 6:** Full results of critic models and PRMs on ProcessBench.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">Model&lt;/th>\n&lt;th colspan=\"3\">GSM8K&lt;/th>\n&lt;th colspan=\"3\">MATH&lt;/th>\n&lt;th colspan=\"3\">OlympiadBench&lt;/th>\n&lt;th colspan=\"3\">Omni-MATH&lt;/th>\n&lt;th rowspan=\"2\">Avg.&lt;br/>F1&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>Err.&lt;/th>\n&lt;th>Corr.&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;th>Err.&lt;/th>\n&lt;th>Corr.&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;th>Err.&lt;/th>\n&lt;th>Corr.&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;th>Err.&lt;/th>\n&lt;th>Corr.&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td colspan=\"14\" style=\"text-align: center;\">&lt;i>Proprietary LLMs (Critic)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GPT-4-0806&lt;/td>\n&lt;td>70.0&lt;/td>\n&lt;td>91.2&lt;/td>\n&lt;td>79.2&lt;/td>\n&lt;td>54.4&lt;/td>\n&lt;td>76.6&lt;/td>\n&lt;td>63.6&lt;/td>\n&lt;td>45.8&lt;/td>\n&lt;td>58.4&lt;/td>\n&lt;td>51.4&lt;/td>\n&lt;td>45.2&lt;/td>\n&lt;td>65.6&lt;/td>\n&lt;td>53.5&lt;/td>\n&lt;td>61.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>o1-mini&lt;/td>\n&lt;td>88.9&lt;/td>\n&lt;td>97.9&lt;/td>\n&lt;td>93.2&lt;/td>\n&lt;td>83.5&lt;/td>\n&lt;td>95.1&lt;/td>\n&lt;td>88.9&lt;/td>\n&lt;td>80.2&lt;/td>\n&lt;td>95.6&lt;/td>\n&lt;td>87.2&lt;/td>\n&lt;td>74.8&lt;/td>\n&lt;td>91.7&lt;/td>\n&lt;td>82.4&lt;/td>\n&lt;td>87.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"14\" style=\"text-align: center;\">&lt;i>Open-Source LLMs (Critic)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3-8B-Instruct&lt;/td>\n&lt;td>42.5&lt;/td>\n&lt;td>7.8&lt;/td>\n&lt;td>13.1&lt;/td>\n&lt;td>28.6&lt;/td>\n&lt;td>9.1&lt;/td>\n&lt;td>13.8&lt;/td>\n&lt;td>27.1&lt;/td>\n&lt;td>2.7&lt;/td>\n&lt;td>4.8&lt;/td>\n&lt;td>26.1&lt;/td>\n&lt;td>8.3&lt;/td>\n&lt;td>12.6&lt;/td>\n&lt;td>11.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3-70B-Instruct&lt;/td>\n&lt;td>35.7&lt;/td>\n&lt;td>96.9&lt;/td>\n&lt;td>52.2&lt;/td>\n&lt;td>13.0&lt;/td>\n&lt;td>93.3&lt;/td>\n&lt;td>22.8&lt;/td>\n&lt;td>12.0&lt;/td>\n&lt;td>92.0&lt;/td>\n&lt;td>21.2&lt;/td>\n&lt;td>11.2&lt;/td>\n&lt;td>91.7&lt;/td>\n&lt;td>20.0&lt;/td>\n&lt;td>29.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-8B-Instruct&lt;/td>\n&lt;td>44.4&lt;/td>\n&lt;td>6.2&lt;/td>\n&lt;td>10.9&lt;/td>\n&lt;td>41.9&lt;/td>\n&lt;td>2.7&lt;/td>\n&lt;td>5.1&lt;/td>\n&lt;td>32.4&lt;/td>\n&lt;td>1.5&lt;/td>\n&lt;td>2.8&lt;/td>\n&lt;td>32.0&lt;/td>\n&lt;td>0.8&lt;/td>\n&lt;td>1.6&lt;/td>\n&lt;td>5.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-70B-Instruct&lt;/td>\n&lt;td>64.3&lt;/td>\n&lt;td>89.6&lt;/td>\n&lt;td>74.9&lt;/td>\n&lt;td>35.4&lt;/td>\n&lt;td>75.6&lt;/td>\n&lt;td>48.2&lt;/td>\n&lt;td>35.1&lt;/td>\n&lt;td>69.9&lt;/td>\n&lt;td>46.7&lt;/td>\n&lt;td>30.7&lt;/td>\n&lt;td>61.8&lt;/td>\n&lt;td>41.0&lt;/td>\n&lt;td>52.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.3-70B-Instruct&lt;/td>\n&lt;td>72.5&lt;/td>\n&lt;td>96.9&lt;/td>\n&lt;td>82.9&lt;/td>\n&lt;td>43.3&lt;/td>\n&lt;td>94.6&lt;/td>\n&lt;td>59.4&lt;/td>\n&lt;td>31.0&lt;/td>\n&lt;td>94.1&lt;/td>\n&lt;td>46.7&lt;/td>\n&lt;td>28.2&lt;/td>\n&lt;td>90.5&lt;/td>\n&lt;td>43.0&lt;/td>\n&lt;td>58.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-Instruct&lt;/td>\n&lt;td>15.5&lt;/td>\n&lt;td>100.0&lt;/td>\n&lt;td>26.8&lt;/td>\n&lt;td>14.8&lt;/td>\n&lt;td>96.8&lt;/td>\n&lt;td>25.7&lt;/td>\n&lt;td>7.7&lt;/td>\n&lt;td>91.7&lt;/td>\n&lt;td>14.2&lt;/td>\n&lt;td>6.9&lt;/td>\n&lt;td>88.0&lt;/td>\n&lt;td>12.7&lt;/td>\n&lt;td>19.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-72B-Instruct&lt;/td>\n&lt;td>49.8&lt;/td>\n&lt;td>96.9&lt;/td>\n&lt;td>65.8&lt;/td>\n&lt;td>36.0&lt;/td>\n&lt;td>94.3&lt;/td>\n&lt;td>52.1&lt;/td>\n&lt;td>19.5&lt;/td>\n&lt;td>97.3&lt;/td>\n&lt;td>32.5&lt;/td>\n&lt;td>19.0&lt;/td>\n&lt;td>96.3&lt;/td>\n&lt;td>31.7&lt;/td>\n&lt;td>45.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-7B-Instruct&lt;/td>\n&lt;td>7.7&lt;/td>\n&lt;td>100.0&lt;/td>\n&lt;td>14.3&lt;/td>\n&lt;td>3.4&lt;/td>\n&lt;td>98.3&lt;/td>\n&lt;td>6.5&lt;/td>\n&lt;td>2.1&lt;/td>\n&lt;td>99.1&lt;/td>\n&lt;td>4.1&lt;/td>\n&lt;td>0.9&lt;/td>\n&lt;td>98.3&lt;/td>\n&lt;td>1.8&lt;/td>\n&lt;td>6.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-14B-Instruct&lt;/td>\n&lt;td>33.8&lt;/td>\n&lt;td>96.4&lt;/td>\n&lt;td>50.1&lt;/td>\n&lt;td>25.4&lt;/td>\n&lt;td>92.4&lt;/td>",
      "numLines": 600,
      "startLine": 800,
      "totalLines": 2164
    }
  },
  "sourceToolAssistantUUID": "df00442e-7ad9-4db2-a442-aa3ed4edac30",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
`````

</details>

---

### Runtime record

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-28 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "8e52e9ac-1711-4d7a-b289-0e35d4b2c3b1",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze GenPRM paper innovation and research craft",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5"
}
```

---

### Assistant

_source line 44 · 2026-05-28T05:07:30.379Z_

<details><summary>Logged reasoning block</summary>

```text
I now have a very thorough understanding of the paper. Let me synthesize my analysis into the requested JSON format.

Key observations from my deep reading:

1. **Problem identification**: The authors identified three specific gaps in existing PRMs: (a) limited process supervision and generalization, (b) reliance on scalar value prediction (classifier-based) rather than leveraging LLM generative abilities, and (c) inability to scale test-time compute for PRMs themselves. The key framing was the question: "How can generative modeling enhance PRM capabilities while enabling test-time scaling?"

2. **Key insight**: By reframing process verification from a discriminative classification task to a generative reasoning task (with explicit CoT + code verification), PRMs inherit two critical properties: (a) they can reason about correctness rather than just scoring it, and (b) they become amenable to test-time scaling via majority voting over multiple verification paths. 

This represents a fundamental shift—moving PRMs from acting as classifiers to functioning as reasoners.

3. **Innovation type**: This is fundamentally a "new_formulation" combined with "combination". They combined CoT reasoning, code verification, and a novel label estimation method (RPE) into a unified generative PRM framework.

4. **Method details**: GenPRM generates explicit CoT reasoning plus Python code verification for each step, then outputs a Yes/No judgment. The Relative Progress Estimation metric measures whether a step meaningfully advances toward the solution by comparing the model's confidence on that step against its overall confidence, using a threshold of 0.8 to determine significance.

They use QwQ-32B to generate the reasoning and code rationales with execution feedback, then filter out about half the data where the RPE labels conflict with human judgments—leaving just 23K training samples. During inference, they sample multiple verification paths and use majority voting. The approach works both as a verifier for selecting the best outputs and as a critic for iterative refinement.

5. **What makes it good**: The efficiency is striking—only 23K training samples compared to 344K+ for competitors—yet the 1.5B model outperforms GPT-4o and the 7B version beats a 72B Qwen PRM. The ablations clearly show how each component contributes, and the dual-use capability as both verifier and critic adds practical flexibility.

6. **Limitations acknowledged**: The approach requires significant inference compute and focuses exclusively on math problems, though it could potentially benefit from reinforcement learning training.

The core building blocks are Monte Carlo estimation, step forcing, relative position embeddings, chain-of-thought reasoning, code verification, consensus filtering, supervised fine-tuning, majority voting, and best-of-N selection. I couldn't locate OpenReview reviews for this AAAI 2026 paper, so now I'm ready to construct the final JSON output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e52e9ac-1711-4d7a-b289-0e35d4b2c3b1",
  "isSidechain": false,
  "requestId": "req_011CbUPPAxoGns5eWkSHZmn9",
  "type": "assistant",
  "uuid": "e618235b-c0db-4fab-83ca-dccc51569e6f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KqzBfMNfwxaWUif2mrmC3R",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14630,
      "cache_read_input_tokens": 40678,
      "output_tokens": 2219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14630,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2219,
          "cache_read_input_tokens": 40678,
          "cache_creation_input_tokens": 14630,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14630
          },
          "type": "message"
        }
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

_source line 45 · 2026-05-28T05:08:09.760Z_

Now I have a comprehensive understanding of the paper. Let me compile the final analysis.

```json
{
  "title": "GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning",
  "venue": "AAAI 2026",
  "problem_identification": "The authors identified that existing PRMs are trained as classifiers outputting scalar values, which squanders the generative capabilities LLMs were pretrained for and structurally prevents applying test-time scaling to the verifier itself. They found this gap by observing an asymmetry: test-time scaling was being applied to policy models but never to the PRMs judging them, because discriminative scoring has no 'reasoning budget' knob to turn. They also noted that MC-based hard labels are noisy — steps with MC(s_t,a_t) > 0 can still be incorrect — motivating a relative rather than absolute labeling criterion.",
  "key_insight": "By recasting step-level verification from a single-token classification ('Yes'=0.8) into a full generative reasoning task (CoT analysis → code generation → code execution → judgment), the PRM becomes scalable at test time: you can sample N independent verification chains and majority-vote, allowing a 1.5B model to outperform GPT-4o through compute rather than parameters. The second insight is that correctness labels should measure relative progress (does this step increase solve probability?) rather than absolute reachability (can you solve from here?).",
  "innovation_type": "combination",
  "method_summary": "GenPRM reformulates process reward modeling as a generative task: given a problem and solution steps, it produces structured CoT analysis (in &lt;analyze> tags) followed by Python verification code (in &lt;verify> tags), executes the code, incorporates execution feedback, and then emits a Yes/No judgment whose token probability serves as the reward. Training data is synthesized via a three-stage pipeline: (1) step-forced solution generation from Qwen2.5-7B-Instruct with dynamic Monte Carlo estimation (K=32–128 completions depending on problem difficulty), (2) Relative Progress Estimation (RPE) that labels step t as positive iff MC(s_{t+1})/MC(s_t) ≥ 0.8, measuring whether the step increases solve probability relative to the prior state, and (3) rationale synthesis by QwQ-32B with code execution, followed by consensus filtering that discards solutions where RPE labels disagree with LLM-as-a-judge labels (~51% discarded), yielding only 23K high-quality training examples. The model is trained via standard SFT on DeepSeek-R1-Distill backbones. At inference, GenPRM scales via majority voting over N sampled verification paths per step, and can serve dually as a Best-of-N verifier or as an iterative critic that feeds step-level critiques back to the policy model.",
  "what_makes_it_good": "The paper succeeds because it delivers an outsized result from a simple, well-motivated reformulation: 23K training samples (vs. 344K+ for Qwen2.5-Math-PRM) and a 7B model beating a 72B competitor. The ablation design is excellent — Tables 3-5 systematically decompose contributions of RPE thresholds, CoT vs. code verification, and training-vs-inference component combinations, making the paper feel honest and reproducible. The dual verifier/critic framing broadens impact beyond ranking into iterative refinement, with Table 2 showing sustained gains over 3 refinement turns (3.4× improvement over DeepSeek-R1-Distill-7B).",
  "limitations_acknowledged": "The generative reasoning approach introduces substantial additional inference computation per step (the paper acknowledges needing dynamic pruning of the reasoning process). The method is validated only on mathematical reasoning and the authors note extension to coding and general reasoning tasks remains future work. They also suggest RL-based training could further improve GenPRM's generative reasoning abilities.",
  "open_questions": [
    "Can the generative verification paradigm transfer to domains without clean code-verifiability (e.g., commonsense reasoning, open-ended generation, scientific reasoning), where code execution cannot serve as an objective grounding signal?",
    "What is the compute-optimal tradeoff between scaling the policy model's test-time compute (more solution samples) vs. scaling the verifier's test-time compute (more verification chains per step)? The paper explores both axes but doesn't characterize the Pareto frontier.",
    "Can RL training (e.g., GRPO/PPO on verification accuracy) replace or augment the SFT-based training to produce self-improving verifiers, and would this reduce dependence on the QwQ-32B teacher for rationale synthesis?"
  ],
  "building_blocks": [
    "Monte Carlo step-level estimation with dynamic K based on problem difficulty",
    "Step forcing for semantic step segmentation in solution generation",
    "Relative Progress Estimation (ratio-based MC label refinement)",
    "QwQ-32B as rationale synthesis teacher model",
    "Structured CoT + code generation with execution feedback loop",
    "Consensus filtering between RPE labels and LLM-as-a-judge labels",
    "DeepSeek-R1-Distill backbone models (1.5B/7B/32B)",
    "ProcessBench evaluation framework",
    "Majority voting over sampled verification paths for TTS",
    "Dual-use verifier/critic architecture pattern",
    "MATH dataset (7.5K problems as source)",
    "Qwen2.5-7B-Instruct and Qwen2.5-Math-7B-Instruct for solution/completion generation"
  ],
  "reviewer_feedback_summary": null,
  "relevance_to_seed": "This paper directly advances the core of our research area — step-level verification and credit assignment — by demonstrating that the verification task itself should be treated as a reasoning problem rather than a classification problem. The RPE formulation (measuring relative progress rather than absolute reachability) offers a principled new approach to credit assignment that draws an elegant analogy to advantage estimation in RL (specifically GRPO). For our research, the key transferable lessons are: (1) converting discriminative reward modeling into generative reasoning unlocks test-time scaling as a free knob, (2) data quality via consensus filtering dramatically outperforms data quantity (23K vs 344K+), and (3) code verification provides a scalable, objective grounding signal that reduces reliance on noisy MC estimates."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e618235b-c0db-4fab-83ca-dccc51569e6f",
  "isSidechain": false,
  "requestId": "req_011CbUPPAxoGns5eWkSHZmn9",
  "type": "assistant",
  "uuid": "6329720a-d90f-483d-9cd4-caf371f9dfe3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KqzBfMNfwxaWUif2mrmC3R",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14630,
      "cache_read_input_tokens": 40678,
      "output_tokens": 2219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14630,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2219,
          "cache_read_input_tokens": 40678,
          "cache_creation_input_tokens": 14630,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14630
          },
          "type": "message"
        }
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

_source line 46_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-28 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "6329720a-d90f-483d-9cd4-caf371f9dfe3",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze GenPRM paper innovation and research craft",
  "sessionId": "d13ca6d2-ab23-4990-8414-c3096bb93ab5"
}
```

---
