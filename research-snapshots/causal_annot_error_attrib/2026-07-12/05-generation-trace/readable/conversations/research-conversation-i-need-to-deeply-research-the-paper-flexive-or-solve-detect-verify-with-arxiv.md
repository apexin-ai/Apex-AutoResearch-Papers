# Research conversation: I need to deeply research the paper "FlexiVe" or "Solve-Detect-Verify" with arXiv ID 2505.11966 (May 2025). This paper r

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a9f50be13f2913edb.jsonl`
- **Structured JSON:** [`584da6364c6217651894.json`](../../sessions/58/584da6364c6217651894.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

41 recorded events

### User

_source line 1 · 2026-05-28T02:48:59.874Z_

I need to deeply research the paper "FlexiVe" or "Solve-Detect-Verify" with arXiv ID 2505.11966 (May 2025). This paper reportedly achieves 80.8% avg F1 on ProcessBench (Moderate Compute) and 86.3% (High Compute), making it the current open-source SOTA on ProcessBench for process reward modeling.

Please:
1. Search for and fetch the full paper from arXiv (https://arxiv.org/abs/2505.11966)
2. Find out: exact title, authors, method details, how it does fast/slow verification allocation, how GRPO is used, whether it operates at solution-level or step-level, what model it uses, key results on ProcessBench and other benchmarks
3. Search for any related discussions, citations, or follow-up work
4. Check if it has been accepted to any venue

I need detailed technical understanding of how FlexiVe works, especially:
- How does it allocate between fast and slow verification?
- Is it truly solution-level only, or does it have any step-level component?
- How does its GRPO training differ from standard GRPO?
- What are its limitations that step-level routing could address?

Report in detail (500+ words).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "893c21bf-c2a9-4d7f-b44e-6410c59daba9",
  "agentId": "a9f50be13f2913edb",
  "type": "user",
  "uuid": "aa84f765-3cc0-478a-ac35-94d8922b9283",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-28T02:48:59.878Z_

```json
{
  "parentUuid": "aa84f765-3cc0-478a-ac35-94d8922b9283",
  "isSidechain": true,
  "agentId": "a9f50be13f2913edb",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": []
  },
  "type": "attachment",
  "uuid": "29b369c9-e7f6-4901-ba52-6387a9963719",
  "timestamp": "2026-05-28T02:48:59.878Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-28T02:48:59.879Z_

```json
{
  "parentUuid": "29b369c9-e7f6-4901-ba52-6387a9963719",
  "isSidechain": true,
  "agentId": "a9f50be13f2913edb",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "a097cce7-4f87-4f5d-9000-833feea2b5ea",
  "timestamp": "2026-05-28T02:48:59.879Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-28T02:49:02.300Z_



I'll research this paper thoroughly by fetching the arXiv page and searching for related discussions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a097cce7-4f87-4f5d-9000-833feea2b5ea",
  "isSidechain": true,
  "agentId": "a9f50be13f2913edb",
  "requestId": "req_011CbUCrDDxEFwzNB8CAE56u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be2b4ced-4fec-429d-931f-6eb3c27d2996",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UrvvH9sdxhC6YwVBhkZtF7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9061,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9061,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-28T02:49:02.826Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01S1T2BySvP9mtxXpykLoFzy`</summary>

```json
{
  "query": "select:WebFetch,WebSearch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be2b4ced-4fec-429d-931f-6eb3c27d2996",
  "isSidechain": true,
  "agentId": "a9f50be13f2913edb",
  "requestId": "req_011CbUCrDDxEFwzNB8CAE56u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5df4cb81-af9c-4084-9423-645fed027879",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UrvvH9sdxhC6YwVBhkZtF7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9061,
      "cache_read_input_tokens": 0,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9061
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 101,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 9061,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9061,
            "ephemeral_1h_input_tokens": 0
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

_source line 6 · 2026-05-28T02:49:02.831Z_

<details><summary>↩ Tool result · `toolu_01S1T2BySvP9mtxXpykLoFzy`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```

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
  "parentUuid": "5df4cb81-af9c-4084-9423-645fed027879",
  "isSidechain": true,
  "promptId": "893c21bf-c2a9-4d7f-b44e-6410c59daba9",
  "agentId": "a9f50be13f2913edb",
  "type": "user",
  "uuid": "1161b530-82b8-4f43-9677-34c10a424bd7",
  "sourceToolAssistantUUID": "5df4cb81-af9c-4084-9423-645fed027879",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-28T02:49:06.198Z_



Now let me fetch the paper and search for related discussions in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1161b530-82b8-4f43-9677-34c10a424bd7",
  "isSidechain": true,
  "agentId": "a9f50be13f2913edb",
  "requestId": "req_011CbUCrSAKqUtN8kugMtw8i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "212fe58d-c41e-4ede-85a0-6a38e056318d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CfSHR3kn2Kk4DdHmMoRtoK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1123,
      "cache_read_input_tokens": 9061,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1123,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-28T02:49:08.132Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NrkxKzVC12q16FQECVmyVu`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.11966",
  "prompt": "Extract the full paper details: exact title, all authors, abstract, submission date, any venue acceptance information, and all content visible on the page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "212fe58d-c41e-4ede-85a0-6a38e056318d",
  "isSidechain": true,
  "agentId": "a9f50be13f2913edb",
  "requestId": "req_011CbUCrSAKqUtN8kugMtw8i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7bc97fbc-0e11-4384-86ec-972d20bbe229",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CfSHR3kn2Kk4DdHmMoRtoK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1123,
      "cache_read_input_tokens": 9061,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1123,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-28T02:49:11.946Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011zbWHX5QTGLSdY6LBJTVot`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.11966",
  "prompt": "Extract the COMPLETE paper content including: 1) Full title and authors, 2) Abstract, 3) All sections including introduction, method/approach details, training procedure (especially GRPO details), fast vs slow verification allocation mechanism, solution-level vs step-level details, model architecture, 4) All experimental results especially on ProcessBench and other benchmarks, 5) Ablation studies, 6) Limitations, 7) Related work discussion. Be as detailed as possible about the technical method."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bc97fbc-0e11-4384-86ec-972d20bbe229",
  "isSidechain": true,
  "agentId": "a9f50be13f2913edb",
  "requestId": "req_011CbUCrSAKqUtN8kugMtw8i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "743358e4-a402-4249-b50b-18ac1c1bbcc2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CfSHR3kn2Kk4DdHmMoRtoK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1123,
      "cache_read_input_tokens": 9061,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1123,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-28T02:49:11.956Z_

<details><summary>↩ Tool result · `toolu_011zbWHX5QTGLSdY6LBJTVot`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "743358e4-a402-4249-b50b-18ac1c1bbcc2",
  "isSidechain": true,
  "promptId": "893c21bf-c2a9-4d7f-b44e-6410c59daba9",
  "agentId": "a9f50be13f2913edb",
  "type": "user",
  "uuid": "4aa457d2-f7b5-449e-8777-6d46e8204bb0",
  "sourceToolAssistantUUID": "743358e4-a402-4249-b50b-18ac1c1bbcc2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-28T02:49:13.360Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K4epgqQKj4bT3UoAWGuqUH`</summary>

```json
{
  "query": "FlexiVe \"Solve-Detect-Verify\" arXiv 2505.11966 process reward model verification"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4aa457d2-f7b5-449e-8777-6d46e8204bb0",
  "isSidechain": true,
  "agentId": "a9f50be13f2913edb",
  "requestId": "req_011CbUCrSAKqUtN8kugMtw8i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70055f9d-b03d-4211-b3db-fee1c06bf5ad",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CfSHR3kn2Kk4DdHmMoRtoK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1123,
      "cache_read_input_tokens": 9061,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1123,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-28T02:49:13.426Z_

<details><summary>↩ Tool result · `toolu_01NrkxKzVC12q16FQECVmyVu`</summary>

```text
# Paper Details

**Title:** Solve-Detect-Verify: Inference-Time Scaling with Flexible Generative Verifier

**Authors:** Jianyuan Zhong, Zeju Li, Zhijian Xu, Xiangyu Wen, Kezhi Li, Qiang Xu

**Submission Date:** May 17, 2025

**arXiv Identifier:** 2505.11966 [cs.AI]

**Venue Acceptance:** No acceptance information provided (preprint status)

## Abstract Summary

The researchers address the challenge of balancing accuracy against computational cost in LLM reasoning tasks. They introduce "FlexiVe," a generative verifier that "flexibly balances computational resources between rapid, reliable fast thinking and meticulous slow thinking." The proposed Solve-Detect-Verify pipeline intelligently identifies when solutions are complete and triggers focused verification with targeted feedback. 

Testing on ProcessBench demonstrated superior error-detection capabilities. Performance on mathematical reasoning benchmarks (AIME 2024, AIME 2025, CNMO) showed improvements over baseline approaches in both reasoning accuracy and inference efficiency, presenting "a scalable and effective solution to enhance LLM reasoning at test time."

**License:** CC BY 4.0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7bc97fbc-0e11-4384-86ec-972d20bbe229",
  "isSidechain": true,
  "promptId": "893c21bf-c2a9-4d7f-b44e-6410c59daba9",
  "agentId": "a9f50be13f2913edb",
  "type": "user",
  "uuid": "7f4c3a7c-aa61-4d47-8a68-02cb798f3c9d",
  "sourceToolAssistantUUID": "7bc97fbc-0e11-4384-86ec-972d20bbe229",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-28T02:49:13.702Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QM31PCMwPsvtfJpztS4a8o`</summary>

```json
{
  "query": "FlexiVe ProcessBench SOTA 2025 flexible verification math reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f4c3a7c-aa61-4d47-8a68-02cb798f3c9d",
  "isSidechain": true,
  "agentId": "a9f50be13f2913edb",
  "requestId": "req_011CbUCrSAKqUtN8kugMtw8i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf5f894d-ec23-4100-bc43-9528134ee3eb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CfSHR3kn2Kk4DdHmMoRtoK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1123,
      "cache_read_input_tokens": 9061,
      "output_tokens": 415,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1123
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 415,
          "cache_read_input_tokens": 9061,
          "cache_creation_input_tokens": 1123,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1123,
            "ephemeral_1h_input_tokens": 0
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

_source line 14 · 2026-05-28T02:49:21.263Z_

<details><summary>↩ Tool result · `toolu_01QM31PCMwPsvtfJpztS4a8o`</summary>

```text
Web search results for query: "FlexiVe ProcessBench SOTA 2025 flexible verification math reasoning"

Links: [{"title":"Paper page - Solve-Detect-Verify: Inference-Time Scaling with Flexible Generative Verifier","url":"https://huggingface.co/papers/2505.11966"},{"title":"ProcessBench: Identifying Process Errors in Mathematical Reasoning","url":"https://www.researchgate.net/publication/394269497_ProcessBench_Identifying_Process_Errors_in_Mathematical_Reasoning"},{"title":"[2505.11966] Solve-Detect-Verify: Inference-Time Scaling with Flexible Generative Verifier","url":"https://arxiv.org/abs/2505.11966"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf/236432358408701ce93737e4dc4753be75b1d696.pdf"},{"title":"Solve-Detect-Verify: Inference-Time Scaling with Flexible ...","url":"https://arxiv.org/pdf/2505.11966"},{"title":"Solve-Detect-Verify: Inference-Time Scaling with Flexible Generative Verifier | OpenReview","url":"https://openreview.net/forum?id=iPn5Ejloxm"},{"title":"ProcessBench: Identifying Process Errors in Mathematical Reasoning","url":"https://arxiv.org/pdf/2412.06559"},{"title":"AIME 2024 and AIME 2025 Benchmarks","url":"https://www.emergentmind.com/topics/aime-2024-and-aime-2025-benchmarks"},{"title":"Dyve: Thinking Fast and Slow for Dynamic Process Verification","url":"https://arxiv.org/pdf/2502.11157"}]

Based on the search results, here's what I found about FlexiVe, ProcessBench, and their relationship to SOTA (state-of-the-art) results in flexible verification for math reasoning:

## Overview

FlexiVe is a novel generative verifier that flexibly balances computational resources between rapid, reliable fast thinking and meticulous slow thinking using a Flexible Allocation of Verification Budget strategy.

## ProcessBench Results

FlexiVe achieves superior accuracy in pinpointing errors within reasoning traces on ProcessBench. More specifically, FlexiVe establishes a new open-source state-of-the-art on ProcessBench, outperforming the much larger GenPRM-32B while requiring ~2.3x fewer TFLOPS with 15x less training data.

## Mathematical Reasoning Performance

On challenging mathematical reasoning benchmarks (AIME 2024, AIME 2025, and CNMO), the full approach outperforms baselines like self-consistency in reasoning accuracy and inference efficiency. Additionally, the Solve-Detect-Verify pipeline integrates an early stopping detector, a scalable generative verifier that balances "fast" and "slow" verification, and a flexible verification budget, improving accuracy from 67.5% to >83% at scale and reducing token consumption via early exit and adaptive verification.

## Training Approach

FlexiVe, RL-trained on only 1,526 samples, generalized effectively, highlighting RL's advantage in fostering robust verifiers capable of handling diverse reasoning styles and complexities, even with significantly less data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf5f894d-ec23-4100-bc43-9528134ee3eb",
  "isSidechain": true,
  "promptId": "893c21bf-c2a9-4d7f-b44e-6410c59daba9",
  "agentId": "a9f50be13f2913edb",
  "type": "user",
  "uuid": "c03b1623-ea01-49b4-93a8-7ad7f75a4938",
  "sourceToolAssistantUUID": "cf5f894d-ec23-4100-bc43-9528134ee3eb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-28T02:49:22.679Z_

<details><summary>↩ Tool result · `toolu_01K4epgqQKj4bT3UoAWGuqUH`</summary>

```text
Web search results for query: "FlexiVe "Solve-Detect-Verify" arXiv 2505.11966 process reward model verification"

Links: [{"title":"[2505.11966] Solve-Detect-Verify: Inference-Time Scaling with Flexible Generative Verifier","url":"https://arxiv.org/abs/2505.11966"},{"title":"Solve-Detect-Verify: Inference-Time Scaling with Flexible ...","url":"https://arxiv.org/pdf/2505.11966"},{"title":"(PDF) Solve-Detect-Verify: Inference-Time Scaling with Flexible Generative Verifier","url":"https://www.researchgate.net/publication/391878031_Solve-Detect-Verify_Inference-Time_Scaling_with_Flexible_Generative_Verifier"},{"title":"Paper page - Solve-Detect-Verify: Inference-Time Scaling with Flexible Generative Verifier","url":"https://huggingface.co/papers/2505.11966"},{"title":"Process Reward Models That Think","url":"https://arxiv.org/pdf/2504.16828"},{"title":"Uncertainty-Aware Step-wise Verification with Generative Reward Models","url":"https://arxiv.org/pdf/2502.11250"}]

Based on the search results, here's what I found about the FlexiVe "Solve-Detect-Verify" paper:

FlexiVe is a novel generative verifier that flexibly balances computational resources between rapid, reliable fast thinking and meticulous slow thinking using a Flexible Allocation of Verification Budget strategy. The Solve-Detect-Verify pipeline is an efficient inference-time scaling framework that intelligently integrates FlexiVe, proactively identifying solution completion points to trigger targeted verification and provide focused solver feedback.

The paper, authored by researchers from The Chinese University of Hong Kong, addresses how large language model reasoning for complex tasks involves a trade-off between solution accuracy and computational efficiency, with verification further complicating this by introducing its own trade-off: sophisticated Generative Reward Models (GenRMs) can be computationally prohibitive if naively integrated with LLMs at test-time, while simpler, faster methods may lack reliability.

On the Math benchmark, the FlexiVe verifier with the Flex@8 configuration attains a higher F1 score while generating approximately 3x fewer tokens than the baseline.

The paper was submitted to arXiv on May 17, 2025, with the identifier 2505.11966.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70055f9d-b03d-4211-b3db-fee1c06bf5ad",
  "isSidechain": true,
  "promptId": "893c21bf-c2a9-4d7f-b44e-6410c59daba9",
  "agentId": "a9f50be13f2913edb",
  "type": "user",
  "uuid": "0c228622-bb34-4eab-b5e1-577bb333aa8f",
  "sourceToolAssistantUUID": "70055f9d-b03d-4211-b3db-fee1c06bf5ad",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-28T02:49:25.358Z_

Let me now fetch the PDF and the OpenReview page, plus the HuggingFace discussion page for more details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c228622-bb34-4eab-b5e1-577bb333aa8f",
  "isSidechain": true,
  "agentId": "a9f50be13f2913edb",
  "requestId": "req_011CbUCstmVrv78AsNcVXsbn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a4df1e32-9092-4ae5-b47d-331048aef5f7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016EWRF1w7enoYCkjYMRz7gf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 894,
      "cache_creation_input_tokens": 1472,
      "cache_read_input_tokens": 10184,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1472,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-28T02:49:33.049Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Egck6qXm8UYdvKdCrxhYmD`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2505.11966",
  "prompt": "Extract ALL technical details from this paper. I need:\n1. COMPLETE method description of FlexiVe - how fast thinking vs slow thinking works, what the model actually does in each mode\n2. The Flexible Allocation of Verification Budget (FAVB) strategy - exact mechanism for deciding fast vs slow\n3. GRPO training details - how many samples, what reward signal, how it differs from standard GRPO, training data composition\n4. The Solve-Detect-Verify pipeline - each component, how early stopping detector works, how verification feedback is provided to solver\n5. Whether verification is solution-level or step-level - exact granularity\n6. Base model used (e.g., Qwen2.5-7B-Instruct or similar)\n7. ALL ProcessBench results with exact numbers (F1 scores for different compute levels, comparison with other methods like GenPRM)\n8. ALL results on AIME 2024, AIME 2025, CNMO benchmarks\n9. Ablation studies - what components were ablated and results\n10. Token efficiency comparisons\n11. Limitations discussed by authors\n12. Any step-level components or lack thereof"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4df1e32-9092-4ae5-b47d-331048aef5f7",
  "isSidechain": true,
  "agentId": "a9f50be13f2913edb",
  "requestId": "req_011CbUCstmVrv78AsNcVXsbn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e6c65692-2e1d-4dcb-9fb6-a1ef9af0f6d2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016EWRF1w7enoYCkjYMRz7gf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 894,
      "cache_creation_input_tokens": 1472,
      "cache_read_input_tokens": 10184,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1472,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-28T02:49:34.849Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014DNFWgTrLqnPetKtJWRhqR`</summary>

```json
{
  "url": "https://openreview.net/forum?id=iPn5Ejloxm",
  "prompt": "Extract all information about this paper submission: venue, acceptance status, reviewer scores, reviewer comments, any discussion. Is this paper accepted or rejected? What venue is it submitted to?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6c65692-2e1d-4dcb-9fb6-a1ef9af0f6d2",
  "isSidechain": true,
  "agentId": "a9f50be13f2913edb",
  "requestId": "req_011CbUCstmVrv78AsNcVXsbn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc8697ea-8213-4346-83e1-e1be54fd2436",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016EWRF1w7enoYCkjYMRz7gf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 894,
      "cache_creation_input_tokens": 1472,
      "cache_read_input_tokens": 10184,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1472,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-28T02:49:36.385Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DpcTZQWCmnJDmcj7DQbZ9V`</summary>

```json
{
  "url": "https://huggingface.co/papers/2505.11966",
  "prompt": "Extract all discussion, comments, upvotes, and any community feedback about this paper. Are there any related models or code released?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc8697ea-8213-4346-83e1-e1be54fd2436",
  "isSidechain": true,
  "agentId": "a9f50be13f2913edb",
  "requestId": "req_011CbUCstmVrv78AsNcVXsbn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a5d7909-115e-4e6e-80cc-c2956dcf4e75",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016EWRF1w7enoYCkjYMRz7gf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 894,
      "cache_creation_input_tokens": 1472,
      "cache_read_input_tokens": 10184,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1472,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-28T02:49:36.962Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L9228TzMPbFThtMaWPQRB6`</summary>

```json
{
  "query": "FlexiVe \"Solve-Detect-Verify\" GRPO training verification budget allocation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a5d7909-115e-4e6e-80cc-c2956dcf4e75",
  "isSidechain": true,
  "agentId": "a9f50be13f2913edb",
  "requestId": "req_011CbUCstmVrv78AsNcVXsbn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "632663b8-12ac-4aae-ad19-cc76963644aa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016EWRF1w7enoYCkjYMRz7gf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 894,
      "cache_creation_input_tokens": 1472,
      "cache_read_input_tokens": 10184,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1472,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-28T02:49:37.108Z_

<details><summary>↩ Tool result · `toolu_01DpcTZQWCmnJDmcj7DQbZ9V`</summary>

```text
&lt;persisted-output>
Output too large (64.7KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/13f2f0f6-9a9f-4b22-8071-05196d59bedf/tool-results/toolu_01DpcTZQWCmnJDmcj7DQbZ9V.txt

Preview (first 2KB):
# Solve-Detect-Verify : Inference-Time Scaling with Flexible Generative Verifier

Jianyuan Zhong\*, Zeju Li\*, Zhijian Xu, Xiangyu Wen, Kezhi Li, Qiang Xu†

The Chinese University of Hong Kong

{jyzhong, zjli24, zjxu21, xywen22, kzli24, qxu}@cse.cuhk.edu.hk

## Abstract

Large Language Model (LLM) reasoning for complex tasks inherently involves a trade-off between solution accuracy and computational efficiency. The subsequent step of verification, while intended to improve performance, further complicates this landscape by introducing its own challenging trade-off: sophisticated Generative Reward Models (GenRMs) can be computationally prohibitive if naively integrated with LLMs at test-time, while simpler, faster methods may lack reliability. To overcome these challenges, we introduce *FlexiVe*, a novel generative verifier that flexibly balances computational resources between rapid, reliable “fast thinking” and meticulous “slow thinking” using a Flexible Allocation of Verification Budget strategy. We further propose the *Solve-Detect-Verify* pipeline, an efficient inference-time scaling framework that intelligently integrates *FlexiVe*, proactively identifying solution completion points to trigger targeted verification and provide focused solver feedback. Experiments show *FlexiVe* achieves superior accuracy in pinpointing errors within reasoning traces on ProcessBench. Furthermore, on challenging mathematical reasoning benchmarks (AIME 2024, AIME 2025, and CNMO), our full approach outperforms baselines like self-consistency in reasoning accuracy and inference efficiency. Our system offers a scalable and effective solution to enhance LLM reasoning at test time.

...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a5d7909-115e-4e6e-80cc-c2956dcf4e75",
  "isSidechain": true,
  "promptId": "893c21bf-c2a9-4d7f-b44e-6410c59daba9",
  "agentId": "a9f50be13f2913edb",
  "type": "user",
  "uuid": "b5f7bfb2-9db3-454c-9cf8-d8354f72f6ed",
  "sourceToolAssistantUUID": "9a5d7909-115e-4e6e-80cc-c2956dcf4e75",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-28T02:49:38.239Z_

<details><summary>↩ Tool result · `toolu_014DNFWgTrLqnPetKtJWRhqR`</summary>

```text
# Paper Submission Summary

**Venue:** ICLR 2026 Conference

**Acceptance Status:** Withdrawn Submission

**Reviewer Scores & Comments:** Not available in the provided content

**Discussion:** Not visible in the provided content

## Key Details

The paper titled "Solve-Detect-Verify: Inference-Time Scaling with Flexible Generative Verifier" was submitted to ICLR 2026 but has been withdrawn. The submission was last modified on January 6, 2026, and is marked as a "Withdrawn Submission" with access available to "Everyone."

The paper introduces FlexiVe, a generative verifier that "dynamically allocates compute between rapid 'fast thinking' and deliberative 'slow thinking.'" The authors claim their approach achieves 83.3% accuracy on AIME 2024 while requiring significantly fewer computational resources than comparable methods.

No reviewer scores, detailed feedback, or discussion comments are included in the webpage content provided.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc8697ea-8213-4346-83e1-e1be54fd2436",
  "isSidechain": true,
  "promptId": "893c21bf-c2a9-4d7f-b44e-6410c59daba9",
  "agentId": "a9f50be13f2913edb",
  "type": "user",
  "uuid": "f420b27e-0346-4ea6-bab5-9c72a5cf1d8b",
  "sourceToolAssistantUUID": "bc8697ea-8213-4346-83e1-e1be54fd2436",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-28T02:49:43.356Z_

<details><summary>↩ Tool result · `toolu_01L9228TzMPbFThtMaWPQRB6`</summary>

```text
Web search results for query: "FlexiVe "Solve-Detect-Verify" GRPO training verification budget allocation 2025"

Links: [{"title":"Paper page - Solve-Detect-Verify: Inference-Time Scaling with Flexible Generative Verifier","url":"https://huggingface.co/papers/2505.11966"},{"title":"Solve-Detect-Verify: Inference-Time Scaling with Flexible ...","url":"https://arxiv.org/pdf/2505.11966"},{"title":"Solve-Detect-Verify: Inference-Time Scaling with Flexible Generative Verifier | OpenReview","url":"https://openreview.net/forum?id=iPn5Ejloxm"},{"title":"(PDF) Solve-Detect-Verify: Inference-Time Scaling with Flexible Generative Verifier","url":"https://www.researchgate.net/publication/391878031_Solve-Detect-Verify_Inference-Time_Scaling_with_Flexible_Generative_Verifier"},{"title":"[2505.11966] Solve-Detect-Verify: Inference-Time Scaling with Flexible Generative Verifier","url":"https://arxiv.org/abs/2505.11966"},{"title":"Trust but Verify! A Survey on Verification Design for Test-time Scaling","url":"https://arxiv.org/html/2508.16665v3"},{"title":"GRPO++: Tricks for Making RL Actually Work","url":"https://cameronrwolfe.substack.com/p/grpo-tricks"},{"title":"The Engineering Handbook for GRPO + LoRA with Verl: Training Qwen2.5 on Multi-GPU","url":"https://huggingface.co/blog/Weyaxi/engineering-handbook-grpo-lora-with-verl"},{"title":"2025-11-18 Scaling Generative Verifiers For Natural Language","url":"https://arxiv.org/pdf/2511.13027"},{"title":"GRPO-LEAD: A Difficulty-Aware Reinforcement Learning ...","url":"https://aclanthology.org/2025.emnlp-main.287.pdf"}]

Based on the search results, I found relevant information about FlexiVe's "Solve-Detect-Verify" framework and its GRPO training approach:

## FlexiVe Overview

FlexiVe is a novel generative verifier and the Solve-Detect-Verify pipeline designed to address the trade-off between accuracy and computational efficiency in Large Language Model (LLM) reasoning.

## Verification Budget Allocation

FlexiVe dynamically balances "fast thinking" (rapid, resource-efficient error diagnosis) and "slow thinking" (meticulous, computationally-intensive analysis) using a Flexible Allocation of Verification Budget strategy. This strategy first uses efficient, parallel assessments to gauge verification difficulty before escalating to deeper analysis if needed.

## GRPO Training

FlexiVe is trained using Group Relative Policy Optimization (GRPO) for mistake detection. GRPO optimizes the model's generation policy by maximizing a composite reward defined as Ri = Rcorrect + Rlength.

## Performance Results

On challenging mathematical reasoning benchmarks (AIME 2024, AIME 2025, and CNMO), the full approach outperforms baselines like self-consistency in reasoning accuracy and inference efficiency.

The search results did not contain specific information about budget allocation numbers for 2025, but they do detail the framework's architecture and training methodology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "632663b8-12ac-4aae-ad19-cc76963644aa",
  "isSidechain": true,
  "promptId": "893c21bf-c2a9-4d7f-b44e-6410c59daba9",
  "agentId": "a9f50be13f2913edb",
  "type": "user",
  "uuid": "5d655222-183a-45d6-9d00-41dc680838ba",
  "sourceToolAssistantUUID": "632663b8-12ac-4aae-ad19-cc76963644aa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-28T02:49:45.304Z_

<details><summary>↩ Tool result · `toolu_01Egck6qXm8UYdvKdCrxhYmD`</summary>

```text
# Technical Details from "Solve-Detect-Verify: Inference-Time Scaling with Flexible Generative Verifier"

## 1. FlexiVe Method Overview
The paper introduces a flexible verifier framework that operates in two modes during inference:
- **Fast thinking**: Direct solution generation with minimal verification
- **Slow thinking**: Extended reasoning with comprehensive verification feedback

The verifier dynamically allocates computational budget based on problem difficulty, enabling efficient inference-time scaling.

## 2. Flexible Allocation of Verification Budget (FAVB)
The exact mechanism for fast vs. slow allocation operates as follows:
- The detector assesses solution confidence and problem complexity early in generation
- Problems receiving low confidence scores trigger "slow" mode with full verification
- High-confidence cases use minimal verification overhead
- Budget allocation is continuous rather than binary, optimizing token usage per problem

## 3. GRPO Training Details
Training specifications include:
- Reward signal derives from correct/incorrect solution classification
- Data composition combines multiple mathematical benchmarks
- The training differs from standard GRPO by incorporating explicit verification feedback as reward conditioning
- Sampling strategy emphasizes diverse problem difficulties
- Training data includes mathematical reasoning tasks requiring step-level supervision signals

## 4. Solve-Detect-Verify Pipeline

**Components:**
- **Solver**: Generates initial solution attempts
- **Detector**: Early-stopping mechanism assessing generation confidence
- **Verifier**: Evaluates solution correctness and provides feedback

**Early stopping detector**: Monitors token-level probability scores and error patterns; triggers verification when confidence drops below adaptive thresholds determined during training.

**Feedback provision**: The verifier returns binary correctness signals that feed back into the solver for iterative refinement when solutions are flagged as potentially incorrect.

## 5. Verification Granularity
Verification operates at the **solution-level** with error detection capabilities. The paper indicates verification targets complete solution correctness rather than intermediate step validation, though error detection implies some intermediate analysis.

## 6. Base Model
The paper references experiments on models compatible with instruction-following formats. Specific base model identifiers appear in experimental setup sections but primary focus is on demonstrating the framework's effectiveness across multiple scales.

## 7. ProcessBench Results
The paper evaluates on ProcessBench with the following approach:
- Tests at varying computational budgets (different token allocation levels)
- Compares F1 scores against baseline methods
- Results show improvements when matching token budgets with standard verifier approaches
- Specific numerical comparisons include evaluations against GenPRM and reward-model baselines

## 8. AIME & Mathematical Benchmark Results
Evaluation includes:
- AIME 2024 and AIME 2025 test sets
- CNMO (Chinese mathematical olympiad) benchmarks
- Results demonstrate improved accuracy when verification budget scales with problem difficulty
- Performance gains are measured in percentage-point improvements over single-pass generation

## 9. Ablation Studies
Components tested in ablation include:
- Effect of detector presence vs. always-fast and always-slow baselines
- Impact of verification feedback on solver performance
- Contribution of GRPO training versus supervised fine-tuning
- Results isolate the importance of adaptive budget allocation

## 10. Token Efficiency
The framework achieves efficiency through:
- Selective deep verification: "only hard problems receive extended reasoning"
- Reduced overhead on easy problems through confidence-based early termination
- Overall token savings compared to fixed-budget verification across all problems
- Efficiency gains measured as accuracy per token spent

## 11. Limitations Discussed
Authors acknowledge:
- Detector accuracy limitations on edge-case problems
- Potential false positives in confidence assessment
- Computational overhead of maintaining dual reasoning modes
- Generalization questions to out-of-distribution problem types

## 12. Step-Level Components
The paper employs primarily **solution-level** verification without explicit step-by-step intermediate supervision. However, the error detection mechanism suggests implicit step analysis for identifying failure points, though this remains subordinate to overall solution correctness assessment.

[Binary content (application/pdf, 870.9KB) also saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/13f2f0f6-9a9f-4b22-8071-05196d59bedf/tool-results/webfetch-1779936573068-0j8eyv.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6c65692-2e1d-4dcb-9fb6-a1ef9af0f6d2",
  "isSidechain": true,
  "promptId": "893c21bf-c2a9-4d7f-b44e-6410c59daba9",
  "agentId": "a9f50be13f2913edb",
  "type": "user",
  "uuid": "a25cf56c-e55b-4340-b036-fcb1c3f05288",
  "sourceToolAssistantUUID": "e6c65692-2e1d-4dcb-9fb6-a1ef9af0f6d2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-28T02:49:51.027Z_

Let me read the full persisted output from HuggingFace which contains the paper content, and also fetch additional details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a25cf56c-e55b-4340-b036-fcb1c3f05288",
  "isSidechain": true,
  "agentId": "a9f50be13f2913edb",
  "requestId": "req_011CbUCuZVvy4sX1mvFUGFix",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a6ad3144-9fe6-48a2-911f-4b8d9b6a107a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RW7oiyrTDtYVTM6uZf3XfW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1716,
      "cache_creation_input_tokens": 2658,
      "cache_read_input_tokens": 11656,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2658,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-28T02:49:54.579Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VJTRVtJKYwsAygxjsyxHPz`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/13f2f0f6-9a9f-4b22-8071-05196d59bedf/tool-results/toolu_01DpcTZQWCmnJDmcj7DQbZ9V.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6ad3144-9fe6-48a2-911f-4b8d9b6a107a",
  "isSidechain": true,
  "agentId": "a9f50be13f2913edb",
  "requestId": "req_011CbUCuZVvy4sX1mvFUGFix",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f94bed9-7482-438e-8e99-9a99685d83bf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RW7oiyrTDtYVTM6uZf3XfW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1716,
      "cache_creation_input_tokens": 2658,
      "cache_read_input_tokens": 11656,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2658
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1716,
          "output_tokens": 158,
          "cache_read_input_tokens": 11656,
          "cache_creation_input_tokens": 2658,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2658,
            "ephemeral_1h_input_tokens": 0
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

_source line 27 · 2026-05-28T02:49:54.894Z_

<details><summary>↩ Tool result · `toolu_01VJTRVtJKYwsAygxjsyxHPz`</summary>

````text
1	# Solve-Detect-Verify : Inference-Time Scaling with Flexible Generative Verifier
2	
3	Jianyuan Zhong\*, Zeju Li\*, Zhijian Xu, Xiangyu Wen, Kezhi Li, Qiang Xu†
4	
5	The Chinese University of Hong Kong
6	
7	{jyzhong, zjli24, zjxu21, xywen22, kzli24, qxu}@cse.cuhk.edu.hk
8	
9	## Abstract
10	
11	Large Language Model (LLM) reasoning for complex tasks inherently involves a trade-off between solution accuracy and computational efficiency. The subsequent step of verification, while intended to improve performance, further complicates this landscape by introducing its own challenging trade-off: sophisticated Generative Reward Models (GenRMs) can be computationally prohibitive if naively integrated with LLMs at test-time, while simpler, faster methods may lack reliability. To overcome these challenges, we introduce *FlexiVe*, a novel generative verifier that flexibly balances computational resources between rapid, reliable “fast thinking” and meticulous “slow thinking” using a Flexible Allocation of Verification Budget strategy. We further propose the *Solve-Detect-Verify* pipeline, an efficient inference-time scaling framework that intelligently integrates *FlexiVe*, proactively identifying solution completion points to trigger targeted verification and provide focused solver feedback. Experiments show *FlexiVe* achieves superior accuracy in pinpointing errors within reasoning traces on ProcessBench. Furthermore, on challenging mathematical reasoning benchmarks (AIME 2024, AIME 2025, and CNMO), our full approach outperforms baselines like self-consistency in reasoning accuracy and inference efficiency. Our system offers a scalable and effective solution to enhance LLM reasoning at test time.
12	
13	Figure 1: Performance Scaling Analysis. **(Left)** On the AIME2024 benchmark, our inference-time scaling framework, *Solve-Detect-Verify*, achieves higher accuracy while requiring approximately **4x fewer solutions** compared to baseline approaches. Since DeepSeek-R1-Distill-Qwen-14B does not report performance from  $k = 2 \dots 32$ , we connect two dots with a dotted straight line. **(Right)** On the Math benchmark, our verifier *FlexiVe* (specifically with the Flex@8 configuration) attains a higher F1 score while generating approximately **3x fewer tokens** than the baseline.
14	
15	\* Equal contribution.
16	
17	† Corresponding author.# 1 Introduction
18	
19	Recent advances in Large Language Models (LLMs) have significantly enhanced their capabilities in tackling complex reasoning tasks, primarily through the explicit generation of step-by-step reasoning traces [1, 2]. This shift towards deeper, more analytical "System 2" processes [3–7], while crucial for improving solution accuracy, inherently presents a fundamental trade-off with computational efficiency. Models often produce verbose reasoning, including redundant steps or "overthinking" [8], where extensive intermediate computations needed for higher accuracy incur substantial costs, sometimes for only marginal gains. This landscape highlights the ongoing challenge of balancing accuracy and efficiency in LLM reasoning, necessitating more sophisticated mechanisms for both generating solutions and verifying their correctness.
20	
21	The need to ensure the reliability of these reasoning traces through verification further complicates the aforementioned accuracy-efficiency balance [9]. While robust verification is crucial for enhancing LLM capabilities, existing methods introduce their own challenging trade-offs. For example, Generative Reward Models (GenRMs) promise detailed step-level feedback [10, 11], but often at the cost of significant computational overhead or naive and expensive integration [12]. Conversely, highly token-efficient mechanisms like "NoThinking" [13], when adapted for *verification*, can achieve substantial token reduction (e.g., 27x-40x fewer tokens, see Figure 2) but suffer a severe drop in error precision (e.g., to 39-56% on mathematical benchmarks), leading to unreliable judgments. This underscores the critical demand for verifiers that can effectively reconcile speed with high reliability.
22	
23	This initial efficiency challenge within the reasoning process itself is further exacerbated when LLMs exhibit prolonged "self-correction" behavior. Models frequently generate hesitation words or phrases (e.g., "hmm", "let me double check") and redundant internal verification steps even after a correct intermediate solution might have been implicitly reached [8]. This continued generation, as models "overthink" a problem, incurs substantial computational costs for little to no gain in final accuracy. An effective system must therefore also address these redundancies by intelligently discerning when a solution is likely complete.
24	
25	This complex interplay of trade-offs in reasoning and verification reveals a clear methodological gap: there is a pressing need for (1) a flexible verifier that can dynamically adapt its computational effort to the complexity of the verification task, balancing inference speed with accuracy, and (2) an intelligent inference-time pipeline that strategically deploys such a verifier and streamlines the overall reasoning process by curtailing unnecessary computation. To address these compounded challenges, we introduce two main contributions:
26	
27	We propose *FlexiVe* (**Flexible Generative Verifier**), a novel generative verification method that dynamically adjusts its computational resources. *FlexiVe* employs a rapid, resource-efficient "fast thinking" mode, optimized for concise error diagnosis through techniques like Group Relative Policy Optimization (GRPO) [6, 14], and a thorough, computationally-intensive "slow thinking" mode. The transition between these modes is governed by a Flexible Allocation of Verification Budget strategy; this strategy first uses efficient, parallelizable assessments of the entire reasoning trace to gauge verification difficulty, escalating to deeper analysis only when initial consensus is low, thereby allowing *FlexiVe* to analyze entire reasoning traces efficiently and pinpoint errors with high precision, unlike verifiers that operate on a per-step basis [15].
28	
29	To effectively leverage *FlexiVe*, we introduce the *Solve-Detect-Verify* pipeline, a novel inference-time scaling framework. This pipeline features a lightweight assessment mechanism that continuously monitors the solver LLM's reasoning trace for cues of solution completeness. Upon detecting a potentially complete solution, the pipeline pauses generation and invokes *FlexiVe* for targeted verification. If validated, the solution is finalized, saving further computation. If errors are found, *FlexiVe*'s focused feedback guides the solver towards refining its reasoning.
30	
31	Extensive experiments validate both contributions. *FlexiVe* demonstrates superior accuracy in identifying and pinpointing errors within reasoning traces compared to existing verification methods on benchmarks like ProcessBench [16]. The integrated *Solve-Detect-Verify* pipeline significantly outperforms widely-adopted inference-time strategies, such as self-consistency [17], in both reasoning accuracy and token efficiency on challenging mathematical reasoning benchmarks, including AIME 2024 [18], AIME 2025 [19]. Our work presents a scalable and effective approach to enhance the reliability and efficiency of complex LLM reasoning at test time, illustrated in Figure 1. The remainderof this paper details our methodology, presents comprehensive experimental results, discusses related work, and concludes with future directions.
32	
33	Figure 2: Empirical motivation for efficient verification and generation strategies. **(Left)** Comparison of error precision and token usage between *NoThinking* and *Thinking* verification on GSM8K and Math (ProcessBench). While *NoThinking* significantly reduces tokens, its error precision is substantially lower, suggesting high false positive rate. **(Right)** Accuracy and token usage comparison between generating a full solution (*Full Thinking*) and halting generation early upon detecting a complete intermediate solution (*First Solution*) on AIME 2024 and AIME 2025. Early detection offers significant token reduction with comparable accuracy.
34	
35	## 2 Related Work
36	
37	**Inference-Time Scaling Strategies.** To navigate the inherent accuracy-efficiency trade-off in LLM reasoning, various inference-time scaling strategies increase compute at test time, such as Best-of-N sampling, self-consistency [17], and tree-based searches [20, 21]. While often improving accuracy, these methods can be computationally intensive and may not optimally integrate verification, sometimes exacerbating inefficiencies like “overthinking” [8]. The need for robust verification within these scaled approaches [9, 22, 23] underscores that simply increasing generation is insufficient, calling for intelligent frameworks like *Solve-Detect-Verify* to strategically manage both generation and verification.
38	
39	**Generative Process Verifiers.** While crucial for accuracy, verifiers themselves can complicate the LLM reasoning trade-off. Expressive generative verifiers like Generative Reward Models (GenRMs) and Process Reward Models (PRMs) [24–26, 11, 10] offer detailed feedback but are often computationally demanding [12], and SFT-based training may limit generalization [27]. Even dynamic approaches like Dyve [15], with “fast” and “slow” modes, face challenges, as per-step verification can accumulate significant overhead. In contrast, *FlexiVe*’s holistic trace analysis with dynamic budget allocation aims for a more cost-effective balance, efficiently pinpointing errors with high precision.
40	
41	**Thinking Fast and Slow in Reasoning Language Models.** Kahneman’s dual-process theory [3] informs approaches to balancing deliberate System 2-like reasoning with efficiency in LLMs [4]. While some methods target generation efficiency (e.g., adaptive computation [28, 29], pruning [30]), extreme token reduction like the “NoThinking” mechanism [13] highlights the **verification dilemma**: when applied to *verification*, such efficiency can lead to low precision (Figure 2). *FlexiVe*’s dual-mode “fast” and “slow thinking” is inspired by these concepts, but its “fast thinking” is specifically optimized for *reliable* error diagnosis via Reinforcement Learning [6]. This, combined with dynamic budget allocation, seeks a more robust and efficient balance than verification strategies that are either consistently expensive or unreliably fast.
42	
43	```
44	
45	graph TD
46	    A[User Query / Problem] --> B["&lt;beginning_of_thinking>"]
47	    B --> C["Okay, I think I have finished thinking."]
48	    C --> D["&lt;/end_of_thinking>"]
49	    D --> E[Final Answer Generation]
50	  
51	```
52	
53	Figure 3: The *NoThinking* mechanism bypasses explicit thought generation, using a template to fill the thinking phase.### 3 Method
54	
55	#### 3.1 Problem Formulation
56	
57	**System Components** Our inference-time scaling framework uses two primary Large Language Model (LLM) components: a solver LLM and *FlexiVe*, our specialized generative verifier. Both are reasoning-capable models. The solver, an off-the-shelf LLM, generates initial candidate solutions without modification. *FlexiVe* is specifically trained for verification, with its architecture and training detailed in Section 3.2.
58	
59	**Reasoning Trace Segmentation** A reasoning trace  $S_{trace}$  is parsed into an ordered sequence of  $N_s$  steps,  $S_{trace} = (step_1, \dots, step_{N_s})$ . Each  $step_i$  is a contiguous text segment delineated by predefined "hesitation keywords" (e.g., "hmm," as might be listed Figure 12 in the appendix), marking transitions between keywords or the trace's start/end. This segmented trace forms the input for verification.
60	
61	**Verifier Operation and Output** The task of the verifier is to assess the correctness of the solver's reasoning trace  $S_{trace}$ . Different verifier architectures approach this differently, as illustrated in Figure 4. For example, a standard Generative Reward Model (GenRM) might perform a single, comprehensive "long thinking" pass over the entire query and trace to output a binary judgment. Process-focused variants like GenPRM often conduct sequential, step-by-step verification, which can be computationally intensive. In our framework, the steps from  $S_{trace}$  are formatted using a critic template [16] to create an input prompt for *FlexiVe*. Unlike per-step verifiers,
62	
63	Figure 4: Comparison of verification mechanisms. Standard GenRMs holistically assess a trace. GenPRMs often verify step-by-step. *FlexiVe* (Ours) uses an adaptive approach on the entire trace, with initial parallel fast evaluations deciding if deeper, slow verification is needed.
64	
65	verifiers, *FlexiVe* evaluates the entire trace but employs a dynamic strategy (detailed in Section 3.2) to modulate its computational effort. It outputs  $V_{out} = (F, idx_{pred})$ , where  $F$  is a textual error analysis and  $idx_{pred}$  is the predicted index of the first error. Consistent with its training,  $idx_{pred} = -1$  signifies no errors. This  $V_{out}$  informs decisions within our *Solve-Detect-Verify*.
66	
67	#### 3.2 FlexiVe
68	
69	*FlexiVe* is a generative verifier that dynamically modulates computational effort during test-time verification, operating in "fast thinking" and "slow thinking" modes. The fast thinking mode, inspired by Ma et al. [13] and enhanced with Reinforcement Finetuning, generates significantly shorter outputs 27x-40x in Figure 2) than the conventional slow thinking mode's detailed trace. Our Flexible Allocation of Verification Budget scheme manages these modes to leverage fast thinking's efficiency.
70	
71	**Reinforcement Training** *FlexiVe* is trained using Group Relative Policy Optimization (GRPO) [6]. In this framework, a base reasoning model fine-tuned on a mistake detection task predicts either the index of the first error ( $idx_{gt}$ ) or returns  $-1$  if the reasoning is correct. GRPO optimizes the model's generation policy by maximizing a composite reward defined as  $R_i = R_{correct} + R_{length}$ .
72	
73	The correctness reward  $R_{correct}$  is defined by
74	
75	$$R_{correct}(idx_{pred}, idx_{gt}) = \begin{cases} 1.0 & \text{if } idx_{pred} = idx_{gt} \\ 0.0 & \text{otherwise} \end{cases}, \quad (1)$$
76	
77	assigning a binary score based on the match between the predicted and true error indices.
78	
79	The length adjustment reward  $R_{length}$  modulates the response length  $L$  relative to  $idx_{gt}$  and is given by  $R_{length} = -P(L, idx_{gt})$ , where  $P(L, idx_{gt})$  is the length penalty function.$$P(L, idx_{gt}) = \begin{cases} \min(P_{max}, c_{fast} \cdot \max(0, L - L_{fast})) & \text{if } idx_{gt} = -1 \\ \min(P_{max}, c_{under} \cdot \max(0, L_{slow\_min} - L)) & \text{if } idx_{gt} \neq -1 \\ + \min(P_{max}, c_{cover} \cdot \max(0, L - L_{slow\_max})) & \text{if } idx_{gt} \neq -1 \end{cases} \quad (2)$$
80	
81	In Equation 2, when  $idx_{gt} = -1$ , responses exceeding the target length  $L_{fast}$  are penalized, thereby promoting “fast thinking” in the absence of errors. Conversely, if  $idx_{gt} \neq -1$ , lengths outside the interval  $[L_{slow\_min}, L_{slow\_max}]$  are penalized to encourage “detailed thinking” during error analysis. Training involves sampling  $G$  outputs per prompt, computing each reward, and calculating advantages relative to the group’s average as in Shao et al. [6].
82	
83	**Flexible Allocation of Verification Budget** *FlexiVe* dynamically allocates its verification budget. The core intuition is thus to leverage inexpensive, parallelizable probes to gauge verification difficulty upfront, and only escalate to more resource-intensive analysis when these probes indicate ambiguity or complexity, thereby tailoring computational effort to the specific needs of each verification instance. Initially, it performs  $k$  “fast thinking” verification runs. The consensus among these runs is measured by the agreement ratio:
84	
85	$$R_{\text{agreement}} = \frac{\max_i a_i}{k}, \quad (3)$$
86	
87	where  $a_i$  is the count of the most frequent outcome (using fuzzy error index matching). If this ratio meets a predefined threshold  $\tau$  ( $R_{\text{agreement}} \geq \tau$ ), the consensus result from the fast phase,  $V_{\text{fast}}$ , is accepted. Otherwise,  $\max(1, k/8)$  additional, resource-intensive “slow thinking” runs are triggered to produce the final outcome  $V_{\text{slow}}$ . The overall verification result  $V$  is thus determined by:
88	
89	$$V = \begin{cases} V_{\text{fast}}, & \text{if } R_{\text{agreement}} \geq \tau, \\ V_{\text{slow}}, & \text{otherwise.} \end{cases} \quad (4)$$
90	
91	This adaptive strategy optimizes computational cost by reserving intensive verification only for cases where initial fast assessments lack sufficient agreement. Crucially, this decision logic and the subsequent verification (whether fast or slow) are applied to the reasoning trace as a whole, rather than on a per-step basis as in some prior dynamic verifiers like Dyve [15]. By evaluating the entire trace with a dynamically chosen verification depth, *FlexiVe* aims to avoid the accumulated cost of per-step decisions, potentially offering better scalability and efficiency, especially for longer or more complex reasoning processes. The intuition is to use a quick, broad assessment first, and only invest significant resources when this initial assessment signals higher uncertainty or difficulty.
92	
93	### 3.3 Solve-Detect-Verify
94	
95	*Solve-Detect-Verify* is a multi-component framework designed to enhance the reasoning accuracy and efficiency of Large Language Models (LLMs). The pipeline integrates distinct modules: an initial solution generation phase (Solve), a mid-stream reasoning monitoring and management stage (Detect), and a combined validation and conditional refinement process (Verify and Refine). The complete pipeline is summarized in Algorithm A.2, with detailed implementation provided in Appendix. The conceptual framework of the pipeline is as follows:
96	
97	**Solve** The ‘Solve’ stage initiates the process, wherein the solver LLM is tasked with generating an initial, step-by-step candidate solution ( $S_1$ ) to a given problem. This stage forms the foundational attempt at problem-solving, producing a complete reasoning trace and a final answer for subsequent evaluation.
98	
99	**Detect** The ‘Detect’ module continuously monitors LLM output for predefined hesitation keywords (Figure 12 in the Appendix). Upon detecting a keyword, generation pauses, and the LLM is prompted (Figure 13 in the Appendix) to assess solution completeness via log-probabilities ( $-\log p(\text{Yes})$ )
100	
101	---
102	
103	#### Algorithm 1 Solve-Detect Stage of *Solve-Detect-Verify*
104	
105	---
106	
107	**Input:** Problem  $P$ , Solver  $M_{\text{solve}}$   
108	**Output:** Candidate Solution  $S_1$
109	
110	```
111	
112	1: procedure SOLVEDETECT( $P, M_{\text{solve}}$ )
113	2:    $S_1 \leftarrow \emptyset$ 
114	3:    $\text{stop\_flag} \leftarrow \text{false}$ 
115	4:   for  $k = 1$  to  $L_{\text{max}}$  do ▷  $L_{\text{max}}$  is max length
116	5:      $t_k \sim M_{\text{solve}}(\cdot | P, S_1^{(k-1)})$ 
117	6:      $S_1^{(k)} \leftarrow S_1^{(k-1)} \oplus t_k$ 
118	7:     if  $t_k = \text{EOS}$  then
119	8:        $\text{stop\_flag} \leftarrow \text{true}$ 
120	9:     if  $S_1^{(k)}$  ends with  $kw \in \mathcal{K}_{\text{hesitation}}$  then
121	10:       $\text{logp}_{\text{Yes}} \leftarrow -\log p_{M_{\text{solve}}}(\text{Yes} | \text{Prompt}_{\text{complete}}(S_1^{(k)}))$ 
122	11:       $\text{logp}_{\text{No}} \leftarrow -\log p_{M_{\text{solve}}}(\text{No} | \text{Prompt}_{\text{complete}}(S_1^{(k)}))$ 
123	12:      if  $\text{logp}_{\text{Yes}} > \text{logp}_{\text{No}}$  then ▷ Compare log-probs
124	13:         $\text{stop\_flag} \leftarrow \text{true}$  ▷ Solution complete
125	14:      if  $\text{stop\_flag}$  then
126	15:        break
127	16:       $S_1 \leftarrow S_1^{(k)}$ 
128	17:   return  $S_1$ 
129	
130	```
131	
132	---vs.  $-\log p(\text{No})$ ). This check efficiently reuses over 90% of the generation prefix, preserving the Key-Value (KV) cache and minimizing computation overheads. If reasoning is deemed complete, the pipeline advances to ‘Verify and Refine’; otherwise, generation resumes. This adaptive monitoring reduces overhead and enables early verification.
133	
134	**Verify and Refine** Upon full generation or early completion detected by the ‘Detect’ module, the candidate solution  $S_1$  is assessed by *FlexiVe*, which identifies any errors and their specific step  $idx_{pred}$ . A validated  $S_1$  directly becomes the final output. If an error is found in  $S_1$ , *FlexiVe*’s diagnostic feedback ( $F_1$ ) guides the solver LLM to generate a single new candidate solution,  $S_2$ , aiming to correct the error by exploring an alternative reasoning path. This refined solution  $S_2$  is then accepted as the final output, without requiring an additional validation round. This integrated approach of validation followed by conditional, feedback-driven refinement ensures a balance between rigorous solution assessment and efficient improvement.
135	
136	## 4 Experiments
137	
138	Our experiments are designed to achieve two primary goals. First, we evaluate the performance and efficiency of *FlexiVe* as a standalone generative verifier, analyzing its scaling properties compared to baseline approaches. Second, we assess the effectiveness of our *Solve-Detect-Verify* in enhancing the reasoning accuracy and computational efficiency of LLMs on complex mathematical tasks, comparing it against standard inference-time strategies.
139	
140	### 4.1 Experimental Setup
141	
142	For detailed experimental configurations, including hyperparameter settings for all models and full dataset statistics, please refer to Appendix A.1.
143	
144	**FlexiVe Training** *FlexiVe* is initialized from DeepSeek-R1-Distill-Qwen-14B [6] and trained for mistake detection using Group Relative Policy Optimization (GRPO) [6] on 90% of the BIG-Bench Mistake dataset [31], with 10% for validation. All the NoThinking mechanism are activated for all input problem and reasoning traces pair to ensure that the training was performed in ‘fast mode’ for targeted improvement. The objective, optimizing a composite reward, uses LORA PEFT [32] ( $r = 16, \alpha = 32$ ) and AdamW [33]. Key GRPO parameters include  $G = 14$  samples per input and a KL coefficient of 0.04. All experiments are conducted on  $8 \times$  NVIDIA A800-SXM4-80GB GPUs.
145	
146	**Evaluation Tasks and Datasets** We assess *FlexiVe*’s step-level verification capability, measured by F1 score, on the comprehensive ProcessBench benchmark [16]. ProcessBench includes diverse mathematical reasoning datasets such as GSM8K, MATH, OlympiadBench, and OmniMATH. For the full *Solve-Detect-Verify*, we evaluate end-to-end task accuracy and token efficiency on particularly challenging mathematical datasets: AIME (2024, 2025) [18, 19], AMC, CNMO [34], and OlympiadBench. Especially, All token counts in the results refer exclusively to the output tokens generated by the LLM, in the entire testing dataset.
147	
148	**Baselines** On ProcessBench, *FlexiVe*’s performance is compared against established Process Reward Models (PRMs) from [16], as detailed in Table 4. We also include a comparison with a token-efficient ‘NoThinking’ verification approach, similar to that described in [13], which represents a simpler, non-deliberative verification strategy. For evaluating the *Solve-Detect-Verify*, DeepSeek-R1 14B and 32B models [6] serve as the base "worker" LLMs. The pipeline’s performance is benchmarked against: (1) the direct output of the worker LLM, representing a standard prompting baseline, and (2) Self-Consistency with majority voting [17], a widely recognized inference-time technique for enhancing LLM reasoning by sampling multiple solutions.
149	
150	### 4.2 FlexiVe Performance and Scaling Analysis
151	
152	This section evaluates *FlexiVe*’s error identification accuracy on ProcessBench [16] and its efficiency on subsets GSM8K and MATH. We test *FlexiVe* in several configurations: *FlexiVe* (**Flex@k**) uses adaptive verification, starting with  $k$  initial "fast" verification samples and dynamically deciding whether to escalate to more thorough verification; *FlexiVe* (**Think@k**) employs  $k$  samples from *FlexiVe*’s deliberative "slow thinking" verification process with majority vote, designed for higher accuracy at a typically higher computational cost; and *FlexiVe* (**NoThinking@k**) represents *FlexiVe* in a purely "fast thinking" or non-deliberative mode using  $k$  samples with majority vote, analogous to the ‘NoThinking’ baseline but with *FlexiVe*’s architecture. The "Moderate Compute" and "HighTable 1: ProcessBench results reported with F1 scores. Results for *FlexiVe* are highlighted . **bold** indicates the best in the sub category. All *FlexiVe* variants are trained on only 1526 samples.
153	
154	&lt;table border="1">
155	&lt;thead>
156	&lt;tr>
157	&lt;th>Model&lt;/th>
158	&lt;th># Samples&lt;/th>
159	&lt;th>GSM8K&lt;/th>
160	&lt;th>MATH&lt;/th>
161	&lt;th>Olympiad Bench&lt;/th>
162	&lt;th>Omni-MATH&lt;/th>
163	&lt;th>Avg.&lt;/th>
164	&lt;/tr>
165	&lt;/thead>
166	&lt;tbody>
167	&lt;tr>
168	&lt;td colspan="7" style="text-align: center;">&lt;i>Proprietary Models&lt;/i>&lt;/td>
169	&lt;/tr>
170	&lt;tr>
171	&lt;td>GPT-4o-0806&lt;/td>
172	&lt;td>unk&lt;/td>
173	&lt;td>79.2&lt;/td>
174	&lt;td>63.6&lt;/td>
175	&lt;td>51.4&lt;/td>
176	&lt;td>53.5&lt;/td>
177	&lt;td>61.9&lt;/td>
178	&lt;/tr>
179	&lt;tr>
180	&lt;td>o1-mini&lt;/td>
181	&lt;td>unk&lt;/td>
182	&lt;td>93.2&lt;/td>
183	&lt;td>88.9&lt;/td>
184	&lt;td>87.2&lt;/td>
185	&lt;td>82.4&lt;/td>
186	&lt;td>87.9&lt;/td>
187	&lt;/tr>
188	&lt;tr>
189	&lt;td colspan="7" style="text-align: center;">&lt;i>Open Source Models (7-8B)&lt;/i>&lt;/td>
190	&lt;/tr>
191	&lt;tr>
192	&lt;td>Qwen2.5-Math-PRM-7B&lt;/td>
193	&lt;td>~344K&lt;/td>
194	&lt;td>82.4&lt;/td>
195	&lt;td>77.6&lt;/td>
196	&lt;td>67.5&lt;/td>
197	&lt;td>66.3&lt;/td>
198	&lt;td>73.5&lt;/td>
199	&lt;/tr>
200	&lt;tr>
201	&lt;td>RetrievalPRM-7B&lt;/td>
202	&lt;td>404K&lt;/td>
203	&lt;td>74.6&lt;/td>
204	&lt;td>71.1&lt;/td>
205	&lt;td>60.2&lt;/td>
206	&lt;td>57.3&lt;/td>
207	&lt;td>65.8&lt;/td>
208	&lt;/tr>
209	&lt;tr>
210	&lt;td>Universal-PRM-7B&lt;/td>
211	&lt;td>unk&lt;/td>
212	&lt;td>85.8&lt;/td>
213	&lt;td>77.7&lt;/td>
214	&lt;td>67.6&lt;/td>
215	&lt;td>66.4&lt;/td>
216	&lt;td>74.3&lt;/td>
217	&lt;/tr>
218	&lt;tr>
219	&lt;td>Direct Generative PRM-7B&lt;/td>
220	&lt;td>23K&lt;/td>
221	&lt;td>63.9&lt;/td>
222	&lt;td>65.8&lt;/td>
223	&lt;td>54.5&lt;/td>
224	&lt;td>55.9&lt;/td>
225	&lt;td>60.0&lt;/td>
226	&lt;/tr>
227	&lt;tr>
228	&lt;td>GenPRM-7B w/ Code Exec (Pass@1)&lt;/td>
229	&lt;td>23K&lt;/td>
230	&lt;td>78.7&lt;/td>
231	&lt;td>80.3&lt;/td>
232	&lt;td>72.2&lt;/td>
233	&lt;td>69.8&lt;/td>
234	&lt;td>75.2&lt;/td>
235	&lt;/tr>
236	&lt;tr>
237	&lt;td>GenPRM-7B w/ Code Exec (Maj@8)&lt;/td>
238	&lt;td>23K&lt;/td>
239	&lt;td>81.0&lt;/td>
240	&lt;td>85.7&lt;/td>
241	&lt;td>78.4&lt;/td>
242	&lt;td>76.8&lt;/td>
243	&lt;td>80.5&lt;/td>
244	&lt;/tr>
245	&lt;tr>
246	&lt;td colspan="7" style="text-align: center;">&lt;i>Open Source Models (14-32B) w/ Moderate Compute&lt;/i>&lt;/td>
247	&lt;/tr>
248	&lt;tr>
249	&lt;td>Dyve-14B&lt;/td>
250	&lt;td>117K&lt;/td>
251	&lt;td>68.5&lt;/td>
252	&lt;td>58.3&lt;/td>
253	&lt;td>49.0&lt;/td>
254	&lt;td>47.2&lt;/td>
255	&lt;td>55.8&lt;/td>
256	&lt;/tr>
257	&lt;tr>
258	&lt;td>GenPRM-32B w/o Code Exec (Maj@8)&lt;/td>
259	&lt;td>23K&lt;/td>
260	&lt;td>78.8&lt;/td>
261	&lt;td>&lt;u>85.1&lt;/u>&lt;/td>
262	&lt;td>78.7&lt;/td>
263	&lt;td>&lt;u>74.9&lt;/u>&lt;/td>
264	&lt;td>79.3&lt;/td>
265	&lt;/tr>
266	&lt;tr>
267	&lt;td>&lt;i>FlexiVe&lt;/i> (Flex@32)&lt;/td>
268	&lt;td>&lt;b>1526&lt;/b>&lt;/td>
269	&lt;td>82.8&lt;/td>
270	&lt;td>83.3&lt;/td>
271	&lt;td>79.2&lt;/td>
272	&lt;td>73.4&lt;/td>
273	&lt;td>79.7&lt;/td>
274	&lt;/tr>
275	&lt;tr>
276	&lt;td>&lt;i>FlexiVe&lt;/i> (Flex@128)&lt;/td>
277	&lt;td>&lt;b>1526&lt;/b>&lt;/td>
278	&lt;td>&lt;b>83.0&lt;/b>&lt;/td>
279	&lt;td>&lt;b>85.0&lt;/b>&lt;/td>
280	&lt;td>&lt;b>80.0&lt;/b>&lt;/td>
281	&lt;td>&lt;b>75.2&lt;/b>&lt;/td>
282	&lt;td>&lt;b>80.8&lt;/b>&lt;/td>
283	&lt;/tr>
284	&lt;tr>
285	&lt;td colspan="7" style="text-align: center;">&lt;i>Open Source Models (14-32B) w/ High Compute&lt;/i>&lt;/td>
286	&lt;/tr>
287	&lt;tr>
288	&lt;td>GenPRM-32B (Pass@1) w/ Code Exec&lt;/td>
289	&lt;td>23K&lt;/td>
290	&lt;td>83.1&lt;/td>
291	&lt;td>81.7&lt;/td>
292	&lt;td>72.8&lt;/td>
293	&lt;td>72.8&lt;/td>
294	&lt;td>77.6&lt;/td>
295	&lt;/tr>
296	&lt;tr>
297	&lt;td>GenPRM-32B (Maj@8) w/ Code Exec&lt;/td>
298	&lt;td>23K&lt;/td>
299	&lt;td>85.1&lt;/td>
300	&lt;td>86.3&lt;/td>
301	&lt;td>78.9&lt;/td>
302	&lt;td>80.1&lt;/td>
303	&lt;td>82.6&lt;/td>
304	&lt;/tr>
305	&lt;tr>
306	&lt;td>&lt;i>FlexiVe&lt;/i> (Think@64)&lt;/td>
307	&lt;td>&lt;b>1526&lt;/b>&lt;/td>
308	&lt;td>&lt;b>88.1&lt;/b>&lt;/td>
309	&lt;td>&lt;b>90.1&lt;/b>&lt;/td>
310	&lt;td>&lt;b>86.7&lt;/b>&lt;/td>
311	&lt;td>&lt;b>80.4&lt;/b>&lt;/td>
312	&lt;td>&lt;b>86.3&lt;/b>&lt;/td>
313	&lt;/tr>
314	&lt;/tbody>
315	&lt;/table>
316	
317	Compute" categories in Table 4 are broadly defined by the number of verification samples or overall inference cost, with "High Compute" settings involving more extensive verification efforts.
318	
319	### Verification Accuracy on ProcessBench
320	
321	Table 4 (with *FlexiVe* results highlighted in violet ) details the F1 scores for *FlexiVe* compared to various baselines. In the "Moderate Compute" setting, *FlexiVe* (Flex@128) achieves a strong average F1 score of 80.8%, with a notable 85.0% on the MATH dataset. This performance surpasses the GenPRM-32B (Maj@8) model (without code execution), which scores 79.3% average F1, despite *FlexiVe* being trained on significantly fewer samples (1,526 vs. 23K). The *FlexiVe* (Flex@32) configuration also demonstrates competitive performance with a 79.7% average F1 score.
322	
323	In the "High Compute" setting, *FlexiVe* (Think@64), utilizing its deliberative "slow thinking" mode, achieves exceptional F1
324	
325	scores of 88.1% on GSM8K and 90.1% on MATH. This performance notably exceeds that of the compute-intensive GenPRM-32B (Maj@8) model with code execution (which scores 85.1% on GSM8K and 86.3% on MATH). These results highlight that *FlexiVe* 's sophisticated deliberative verification (Think@64), despite its own computational demands, can achieve superior accuracy
326	
327	Figure 5: F1 score vs. verification tokens on GSM8K (left) and MATH (right). *FlexiVe* (Flex@k, green circles) demonstrates higher F1 for similar token costs than DeepSeek-R1-Distill-Qwen-14B (blue triangles, baseline verifier), both outperforming the token-efficient *FlexiVe* (NoThinking variant, red squares). X-axis denote the number of token generated across the entire test set.compared to other large verifiers, even those augmented with code execution. This underscores the effectiveness of *FlexiVe*’s architecture and training, even when scaled to more intensive verification tasks. The significantly smaller training data requirement for *FlexiVe* across all its configurations further emphasizes its sample efficiency.
328	
329	**Efficiency and Budget Scaling (GSM8K & MATH)** Figure 5 depicts the accuracy-cost trade-off. On both GSM8K and MATH, *FlexiVe* (Flex@k) (green circles) provides a better F1 score for comparable token usage than the baseline verifier, DeepSeek-R1-Distill-Qwen-14B (DS14B, blue triangles). While both *FlexiVe* (Flex@k) and DS14B reach higher peak F1 scores, the *FlexiVe* (NoThinking@k) variant (red squares) is considerably more token-frugal, albeit with a lower F1 ceiling.
330	
331	### 4.3 Scaling *Solve-Detect-Verify* for Enhanced Performance
332	
333	We evaluate *Solve-Detect-Verify* on AIME2024 [18], AIME2025 [19], and CNMO [34] to understand its scaling properties. We explore two primary scaling dimensions: first, varying *FlexiVe*’s verification budget within a single pipeline execution, and second, generating multiple candidate solutions from the worker LLM, each processed by *Solve-Detect-Verify*.
334	
335	#### Scaling *FlexiVe* Verification Budget (Flex@N) in a Single Pipeline Run
336	
337	We first analyze scaling *FlexiVe*’s internal verification budget (‘Flex@N’, representing N fast-thinking verification samples post-extraction) within a single pipeline pass. In figure 6, the ‘w/o Flex’ setup (‘Solve + Detect’) significantly cuts token usage, token ratio 0.67 on AIME2024 and 0.43 on CNMO, but can reduce accuracy, notably on CNMO (44.4% vs. 55.5% baseline). Integrating *FlexiVe* verification, particularly ‘Flex@8’, substantially boosts accuracy over baseline on AIME2024 (73.3% vs. 56.6%) and AIME2025 (50.0% vs. 43.3%), and matches baseline accuracy on CNMO (55.5%).
338	
339	Crucially, these ‘Flex@8’ configurations use fewer tokens than the baseline (e.g., 0.96 AIME2024, 0.80 CNMO token ratio), demonstrating *Solve-Detect-Verify*’s token-efficient accuracy gains. However, CNMO’s less consistent improvement with N suggests that varying only the verifier budget might not universally ensure peak performance.
340	
341	**Scaling Solver and Verifier via Multiple Solutions** To achieve more consistent gains and higher peak accuracies, we scale compute by generating multiple solutions from the solver, each verified by *FlexiVe*. On the AIME2024 benchmark (Figure 1, left panel), this strategy yields significant and consistent accuracy improvements as more solutions are processed: accuracy climbs from 67.5% (1 solution) to over 83% (16 solutions). This approach effectively leverages increased solver compute, with *FlexiVe* identifying the correct solution among candidates, demonstrating a robust path to superior performance, especially for top-tier accuracy. This underscores our takeaway in Figure 7: for optimal results with *Solve-Detect-Verify*, scaling solver LLM’s compute is as important as scaling *FlexiVe*’s verification capabilities.
342	
343	#### Takeaway for *Solve-Detect-Verify* scaling
344	
345	With *Solve-Detect-Verify*, scaling solver LLM’s compute is as important as scaling *FlexiVe*’s.
346	
347	Figure 7: A take away highlights the symbiotic relationship.
348	
349	Figure 6: Impact of scaling *FlexiVe*’s verification budget (Flex@N) within a single *Solve-Detect-Verify* execution on Pass@1 Accuracy vs. Token Usage Ratio relative to DeepSeek R1 14B. Benchmarks are color/linestyle distinguished.## 4.4 Extended Analysis
350	
351	**Component Performance Comparison** An ablation study assessed individual component impacts. For *FlexiVe*, we used Flex@4; for NoThinking, maj@8; and for both the DeepSeek-R1-Distill-Qwen-14B baseline and *FlexiVe*’s deliberative mode, Think@1, ensuring roughly comparable computational budgets. Figure 8 shows that *FlexiVe*’s Reinforcement Learning (RL) training not only matches or slightly exceeds the baseline verifier’s performance under similar compute but also significantly outperforms when *FlexiVe* engages its “thinking” mode. This is crucial: though trained with RL primarily leveraging its efficient “NoThinking” (fast) mode, *FlexiVe* generalizes effectively to improve verification in its more deliberative “thinking” mode, underscoring its RL-trained robustness and adaptability.
352	
353	**RL vs. SFT** We compared our RL approach with traditional SFT for training verifiers. The SFT baseline used 10,000 reasoning paths with problems from OpenO1 [35] and generated by DeepSeek-R1-Distill-Qwen-14B. They are labeled via LLM-based judging as [16]. Findings (Figure 9) suggest SFT lack generalization. Reasoning traces in benchmarks like ProcessBench, often from weaker, non-thinking LLMs, are shorter and less complex. This led to performance drops for SFT verifier on more diverse processes. In contrast, *FlexiVe*, RL-trained on only 1,526 BIG-Bench Mistake [31] problems, showed strong generalization. This highlights RL’s advantage in fostering robust verifiers with significantly less data than typical SFT.
354	
355	## 5 Limitations
356	
357	While *FlexiVe* and *Solve-Detect-Verify* demonstrate promising advancements, several avenues warrant future investigation to enhance their robustness and broaden their applicability. The generalization of *FlexiVe* is inherently linked to its training data diversity, and our current validation, primarily on mathematical reasoning due to computational constraints, invites further cross-domain exploration (e.g., in program synthesis or commonsense QA). The empirically-set parameters ( $k, \tau$ ) for *FlexiVe*’s dynamic budget allocation would benefit from a comprehensive sensitivity analysis and the development of automated tuning guidelines to maximize practical adoption. Furthermore, although *Solve-Detect-Verify* is designed for efficiency—with mechanisms like KV cache reuse in its heuristic ‘Detect’ stage—its multi-component nature and dynamic mode-switching introduce inherent computational overhead. We believe this overhead could be substantially mitigated, and overall performance significantly boosted, through optimized implementations, potentially leveraging advanced inference engines like vLLM [36] or SGLang [37]; advancing this represents a valuable direction for community exploration to fully realize the benefits of such dynamic reasoning systems. Addressing these aspects will be key to the continued development and deployment of sophisticated, efficient, and widely applicable verified reasoning frameworks.
358	
359	## 6 Conclusion
360	
361	We introduce *FlexiVe*, a dynamic verifier balancing computational cost and accuracy, integrated into the *Solve-Detect-Verify* pipeline for efficient LLM reasoning enhancement. Experiments confirm that our pipeline, leveraging *FlexiVe*, achieves significant gains in both accuracy and token efficiency over baselines, highlighting flexible verification and intelligent pipeline design as a scalable path toward more reliable and efficient complex reasoning in LLMs.
362	
363	Figure 8: Ablation: Component impact on GSM8K/MATH (%). *FlexiVe* (Think) excels; *FlexiVe* (Flex@4) also surpasses NoThinking (maj@8) and DS-R1-14B (Think@1).
364	
365	Figure 9: RL (*FlexiVe*) vs. SFT (DeepSeek-R1-Distill-Qwen-14B) on GSM8K/MATH. RL-trained *FlexiVe*, especially in thinking mode, shows superior generalization over the SFT baseline.## References
366	
367	- [1] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le, and Denny Zhou. Chain-of-thought prompting elicits reasoning in large language models. In *Advances in Neural Information Processing Systems*, volume 35, pages 24824–24837. Curran Associates, Inc., 2022.
368	- [2] Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yutaka Matsuo, and Yusuke Iwasawa. Large language models are zero-shot reasoners. *arXiv preprint arXiv:2205.11916*, 2022.
369	- [3] Daniel Kahneman. *Thinking, fast and slow*. Farrar, Straus and Giroux, 2011.
370	- [4] Zhong-Zhi Li, Haotian Wang, Kaiyan Zhang, Yancheng He, Yujia Xie, Yuxiang Huang, Zhengliang Shi, HongCheng Li, Wenxuan Wang, Zhiwei He, Dian Yu, Haitao Mi, Dong Yu, Jie Tang, and AnBo Zhang. From system 1 to system 2: A survey of reasoning large language models. *arXiv preprint arXiv:2502.17419*, 2025.
371	- [5] OpenAI. Reasoning models. &lt;https://platform.openai.com/docs/guides/reasoning>, 2024. Accessed: May 7, 2025.
372	- [6] Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, Y. K. Li, Y. Wu, and Daya Guo. Deepseekmath: Pushing the limits of mathematical reasoning in open language models, 2024. URL &lt;https://arxiv.org/abs/2402.03300>.
373	- [7] Google. Gemini 2.5 pro preview: even better coding performance. &lt;https://developers.googleblog.com/en/gemini-2-5-pro-io-improved-coding-performance/>, May 2025. Accessed: May 7, 2025.
374	- [8] Xingyu Chen, Jiahao Xu, Tian Liang, Zhiwei He, Jianhui Pang, Dian Yu, Linfeng Song, Qiuizhi Liu, Mengfei Zhou, Zhuosheng Zhang, Rui Wang, Zhaopeng Tu, Haitao Mi, and Dong Yu. Do not think that much for 2+3=? on the overthinking of o1-like llms. *arXiv preprint arXiv:2412.21187*, 2024.
375	- [9] Jiefeng Chen, Jie Ren, Xinyun Chen, Chengrun Yang, Ruoxi Sun, and Sercan Ö. Arik. SETS: Leveraging self-verification and self-correction for improved test-time scaling. *arXiv preprint arXiv:2501.19306*, 2025.
376	- [10] Zijun Liu, Peiyi Wang, Runxin Xu, Shirong Ma, Chong Ruan, Peng Li, Yang Liu, and Yu Wu. Inference-time scaling for generalist reward modeling, 2025. URL &lt;https://arxiv.org/abs/2504.02495>.
377	- [11] Lunjun Zhang, Arian Hosseini, Hritik Bansal, Mehran Kazemi, Aviral Kumar, and Rishabh Agarwal. Generative verifiers: Reward modeling as next-token prediction, 2025. URL &lt;https://arxiv.org/abs/2408.15240>.
378	- [12] Nishad Singhi, Hritik Bansal, Arian Hosseini, Aditya Grover, Kai-Wei Chang, Marcus Rohrbach, and Anna Rohrbach. When to solve, when to verify: Compute-optimal problem solving and generative verification for llm reasoning, 2025. URL &lt;https://arxiv.org/abs/2504.01005>.
379	- [13] Wenjie Ma, Jingxuan He, Charlie Snell, Tyler Griggs, Sewon Min, and Matei Zaharia. Reasoning models can be effective without thinking, 2025. URL &lt;https://arxiv.org/abs/2504.09858>.
380	- [14] Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, Y.K. Li, Y. Wu, and Daya Guo. Deepseekmath: Pushing the limits of mathematical reasoning in open language models, 2024. URL &lt;https://arxiv.org/abs/2402.03300v3>.
381	- [15] Jianyuan Zhong, Zeju Li, Zhijian Xu, Xiangyu Wen, and Qiang Xu. Dyve: Thinking fast and slow for dynamic process verification, 2025. URL &lt;https://arxiv.org/abs/2502.11157>.- [16] Chujie Zheng, Zhenru Zhang, Beichen Zhang, Runji Lin, Keming Lu, Bowen Yu, Dayiheng Liu, Jingren Zhou, and Junyang Lin. Processbench: Identifying process errors in mathematical reasoning, 2024. URL &lt;https://arxiv.org/abs/2412.06559>.
382	- [17] Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. Self-consistency improves chain of thought reasoning in language models. In *International Conference on Learning Representations (ICLR)*, 2023.
383	- [18] Aime 2024 dataset card. 2024. URL [https://huggingface.co/datasets/HuggingFaceH4/aime\\_2024](https://huggingface.co/datasets/HuggingFaceH4/aime_2024).
384	- [19] Aime 2025 dataset card. 2025. URL &lt;https://huggingface.co/datasets/opencompass/AIME2025>.
385	- [20] Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Sha, Thomas L Chen, Boyuan Rius, Yuxuan Du, Yang Liu, Zipeng Jiang, Tushar Han, et al. Tree of thoughts: Deliberate problem solving with large language models. In *Advances in Neural Information Processing Systems (NeurIPS)*, volume 36, 2023.
386	- [21] Noah Xie, AI AUTOdidax, M Sarmad Parvez, Michael Song, Zhenqiao Zhang, Ziyu Chen, Shrimai Joshi, Robert Gmyr, Yufan Li, Siyuan Li, et al. Reflexion: Language agents with verbal reinforcement learning. In *Advances in Neural Information Processing Systems (NeurIPS)*, volume 36, 2023.
387	- [22] Aman Madaan, Niket Tandon, Prakash Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, et al. Self-refine: Iterative refinement with self-feedback. In *Advances in Neural Information Processing Systems (NeurIPS)*, volume 36, 2023.
388	- [23] Zhaofeng Gou, Zhibo Liu, Jiacheng Xu, Hong Beaver Zhou, Shwai Zhang, Keyan Zhao, Weize Wang, and Chang Liu. Critic: Large language models can self-critique and self-correct their own novice mistakes. In *International Conference on Learning Representations (ICLR)*.
389	- [24] Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cognome. Let’s verify step by step. *arXiv preprint arXiv:2305.20050*, 2023.
390	- [25] Michal Pikwalec, Konrad Słowik, Thomas Zomphos, Piotr Michalak, Mateusz Błaszczyc, Emilia Kosson, Paweł Topolski, Piotr Stańczyk, Adam Zomphos, Jakub Błajdo, Jan Miłkowski, Kyriacos Szymański, Sebastian Jaszczur, Konrad GALIAS, et al. Prover: Process-based reward-model for verifiable reasoning. In *International Conference on Learning Representations (ICLR)*, 2024.
391	- [26] Daniel Saunders, Kevin Stuhlmüller, Amanda Askell, Nelson Smith, Benjamin Dominé, Dylan Drain, Albert Chen, Catherine Olsson, Long Ouyang, Evan Hubinger, et al. Self-critiquing models for assisting human evaluators. *arXiv preprint arXiv:2206.05802*, 2022.
392	- [27] Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training language models to follow instructions with human feedback. In *Advances in Neural Information Processing Systems (NeurIPS)*, volume 35, pages 27730–27744, 2022.
393	- [28] Alex Graves. Adaptive computation time for recurrent neural networks. *arXiv preprint arXiv:1603.08983*, 2016.
394	- [29] Shuming Diao, Sendi Chen, Nathanael Schärli, and Ankur Bapna. Blackmamba: Bit-masking for sparse and efficient attention. *arXiv preprint arXiv:2310.01409*, 2023.
395	- [30] Penghao Zhou, Zialan Huang, Bei Chen, Qian Zhang, Yonatan Bisk, Baolin Peng, Jianfeng Wang, and Chen Zhu. Condensed composite cone (c3) a geometric approach to pruning chain-of-thought. In *Findings of the Association for Computational Linguistics: EMNLP 2023*, pages 13126–13141, 2023.- [31] Gladys Tyen, Hassan Mansoor, Victor Carbune, Peter Chen, and Tony Mak. LLMs cannot find reasoning errors, but can correct them given the error location. In *Findings of the Association for Computational Linguistics: ACL 2024*, pages 13894–13908, Bangkok, Thailand, August 2024. Association for Computational Linguistics. doi: 10.18653/v1/2024.findings-acl.826. URL &lt;https://aclanthology.org/2024.findings-acl.826>.
396	- [32] Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen. LoRA: Low-rank adaptation of large language models. In *International Conference on Learning Representations (ICLR)*, 2022. URL &lt;https://openreview.net/forum?id=nZeVKeeFYf9>.
397	- [33] Ilya Loshchilov and Frank Hutter. Decoupled weight decay regularization. In *International Conference on Learning Representations (ICLR)*, 2019. URL &lt;https://openreview.net/forum?id=Bkg6RiCqY7>.
398	- [34] Junnan Liu, Hongwei Liu, Linchen Xiao, Ziyi Wang, Kuikun Liu, Songyang Gao, Wenwei Zhang, Songyang Zhang, and Kai Chen. Are your llms capable of stable reasoning? *arXiv preprint arXiv:2412.13147*, 2024.
399	- [35] O1-OPEN Team. Openo1-sft-ultra dataset. &lt;https://huggingface.co/datasets/O1-OPEN/OpenO1-SFT-Ultra>, 2024. Accessed: May 14, 2025.
400	- [36] Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E. Gonzalez, Hao Lee, and Ion Stoica. Efficient memory management for large language model serving with pagedattention. In *Proceedings of the ACM SIGOPS 29th Symposium on Operating Systems Principles (SOSP '23)*, page 1013–1029, New York, NY, USA, 2023. Association for Computing Machinery. doi: 10.1145/3600006.3613165. URL &lt;https://doi.org/10.1145/3600006.3613165>.
401	- [37] Lianmin Zheng, Siyuan Zhuang, Zhuohan Li, Cody Hao Yu, Lequn Li, Haotian Chen, Joseph E. Gonzalez, Ion Stoica, and Jonathan Ragan-Kelley. SGLang: Efficient and expressive structured generation for large language models. In *Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (EACL 2024)*, pages 1053–1071, St. Julian’s, Malta, 2024. Association for Computational Linguistics. URL &lt;https://aclanthology.org/2024.eacl-long.63>.
402	- [38] Thomas Wolf, Lysandre Debut, Victor Sanh, Julien Chaumond, Clement Delangue, Anthony Moi, Pierric Cistac, Tim Rault, Remi Louf, Morgan Funtowicz, Joe Davison, Sam Shleifer, Patrick von Platen, Clara Ma, Yacine Jernite, Julien Plu, Canwen Xu, Teven Le Scao, Sylvain Gugger, Mariama Drame, Quentin Lhoest, and Alexander M. Rush. Transformers: State-of-the-Art natural language processing. In *Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing: System Demonstrations*, pages 38–45, Online, October 2020. Association for Computational Linguistics. URL &lt;https://www.aclweb.org/anthology/2020.emnlp-demos.6>.
403	- [39] Leandro von Werra, Lewis Schmid, Thomas Wolf, and Lewis Tunstall. Trl: Transformer reinforcement learning. &lt;https://github.com/huggingface/trl>, 2020-2024.
404	- [40] Lukas Biewald. Experiment tracking with weights and biases. &lt;https://wandb.ai>, 2020. URL &lt;https://www.wandb.com/>. Software available from wandb.com.
405	- [41] Wenjie Ma, Jingxuan He, Charlie Snell, Tyler Griggs, Sewon Min, and Matei Zaharia. Reasoning models can be effective without thinking. *arXiv preprint arXiv:2504.09858*, 2025.## A Appendix
406	
407	### A.1 Extended Experimental Setup
408	
409	**FlexiVe Training.** We train FlexiVe using Group Relative Policy Optimization (GRPO) [6] on a mistake detection task. The policy  $\pi_\theta$  is initialized from the DeepSeek-R1-Distill-Qwen-14B model [6]. We utilize the BIG-Bench Mistake dataset [31], reserving 90% for training and 10% for validation. The training objective is to predict the index of the first reasoning error ( $idx_{gt}$ ) or output -1 if the trace is correct, optimized using the composite reward detailed in Section 4 (main paper). Parameter-Efficient Fine-Tuning (PEFT) is employed via LoRA [32] with rank  $r = 16$  and  $\alpha = 32$ , targeting the attention projection layers. Optimization is performed using AdamW [33] with a learning rate of  $5 \times 10^{-6}$  and gradient checkpointing. For GRPO, we sample  $G = 14$  outputs per input, and the KL coefficient is set to 0.04. Training is managed using the `transformers` [38] and `trl` [39] libraries, with experiment tracking via Weights & Biases [40].
410	
411	**Evaluation Tasks and Datasets.** For FlexiVe **evaluation**, to assess its step-level verification capabilities, we use the ProcessBench benchmark [16]. This includes diverse mathematical reasoning datasets such as GSM8K, MATH, OlympiadBench, and OmniMATH. Performance is measured using the F1 score for identifying the first erroneous step. For Solve-Detect-Verify **pipeline evaluation**, to assess end-to-end effectiveness, we use a suite of challenging mathematical reasoning datasets: AIME (2024 and 2025) [18, 19], AMC (mentioned in main text, details can be added if necessary), CNMO [34], and OlympiadBench (also used for FlexiVe evaluation). AIME is a prestigious high school mathematics competition known for its challenging mathematical problems, and contains problems from the American Invitational Mathematics Examination (AIME) 2024 and 2025. The CNMO Benchmark evaluates AI on China’s National Mathematical Olympiad problems, focusing on advanced proof-based problem-solving. On these tasks, we measure final task accuracy and computational efficiency (e.g., total tokens).
412	
413	**Baselines.** For FlexiVe **baselines** on ProcessBench, we compare against state-of-the-art Process Reward Models (PRMs) as reported in [16] and the ‘NoThinking’ verification approach adapted from [41] (or your specific citation, e.g., [13]). For our Solve-Detect-Verify **pipeline**, we use DeepSeek-R1 14B [6] as the base worker LLMs. The full pipeline is compared against: (1) the worker LM generating solutions directly (potentially with the ‘Detect’ mechanism only), and (2) the Self-Consistency method [17] applied to the worker LM.
414	
415	### A.2 Solve-Detect-Verify Pipeline Implementation Details
416	
417	The Solve-Detect-Verify pipeline is implemented with a specific two-attempt strategy derived from our Python codebase, emphasizing adaptive verification and intelligent solution generation. Algorithm 2 outlines this refined flow. Key components like solution generation with hesitation detection and adaptive verification are encapsulated in helper functions for clarity.---
418	
419	**Algorithm 2** Solve-Detect-Verify Pipeline (Reflecting Python Implementation Logic)
420	
421	---
422	
423	**Require:** Problem  $P$ , Verification Parameters  $\Theta_V = (k_{fast}, \tau_{agree}, k_{slow})$ , Best-of-N  $N_{BoN}$
424	
425	```
426	1:  $S_{final} \leftarrow \text{NIL}$ 
427	2:                                      $\triangleright$  — Attempt 1: Initial Solve and Adaptive Verification —
428	3:  $Prompt_1 \leftarrow \text{FormatInitialPrompt}(P)$ 
429	4:  $S_1 \leftarrow \text{GenerateSolutionWithDetection}(LLM, Prompt_1)$   $\triangleright$  Handles streaming, hesitation
430	   detection, and continuation
431	5:  $(\text{is\_valid}_1, \text{error\_step}_1, F_1) \leftarrow \text{AdaptiveVerify}(P, S_1, \Theta_V)$   $\triangleright$  Uses  $k_{fast}, \tau_{agree}, k_{slow}$ 
432	6: if  $\text{is\_valid}_1 = \text{True}$  then
433	7:    $S_{final} \leftarrow S_1$ 
434	8: else  $\triangleright$  Attempt 1 failed or was deemed invalid by verification
435	9:    $\triangleright$  — Attempt 2: Retry with Best-of-N (BoN) —
436	10:   $Prompt_2 \leftarrow \text{FormatRetryPromptWithFeedback}(P, S_1, F_1)$ 
437	11:   $Solutions_{candidates} \leftarrow []$ ;  $Answers_{candidates} \leftarrow []$ 
438	12:  for  $i = 1$  to  $N_{BoN}$  do
439	13:     $S_{cand} \leftarrow \text{GenerateSolutionWithDetection}(LLM, Prompt_2)$ 
440	14:    Add  $S_{cand}$  to  $Solutions_{candidates}$ 
441	15:     $Ans_{cand} \leftarrow \text{ExtractFinalAnswer}(S_{cand})$ 
442	16:    Add  $Ans_{cand}$  to  $Answers_{candidates}$ 
443	17:     $(Ans_{majority}, S_{voted}) \leftarrow \text{MajorityVote}(Answers_{candidates}, Solutions_{candidates})$ 
444	18:     $S_{final} \leftarrow S_{voted}$   $\triangleright$  BoN result is used directly without re-verification as per Python code
445	19: if  $S_{final}$  is NIL and  $S_1$  is not NIL then  $\triangleright$  Fallback if BoN stage wasn't reached or produced
446	   nothing, but  $S_1$  exists
447	20:    $S_{final} \leftarrow S_1$ 
448	21: Evaluate  $S_{final}$  against ground truth.
449	22: return  $S_{final}$ , Evaluation Metrics, Total Compute Cost
450	```
451	
452	---
453	
454	**Key Helper Functions:**
455	
456	- • **GenerateSolutionWithDetection(LLM, Prompt):** This function generates a solution by streaming tokens from the LLM. It incorporates the hesitation detection mechanism (detailed below in the "Detect" section) to identify potential points of self-correction or solution completion. If hesitation is detected and the solution is deemed complete by an internal check, generation might be paused and then explicitly continued to ensure the full thought process is captured before final truncation.
457	- • **AdaptiveVerify(P, S,  $\Theta_V$ ):** This function performs verification on solution  $S$  for problem  $P$ . It first conducts  $k_{fast}$  "fast thinking" verifications. If the agreement ratio among these (based on exact error step matching) meets or exceeds  $\tau_{agree}$ , their consensus result is returned. Otherwise, it proceeds to  $k_{slow}$  (e.g.,  $\lceil k_{fast}/4 \rceil$ ) "slow thinking" verifications, and their consensus is returned.
458	- • **FormatInitialPrompt, FormatRetryPromptWithFeedback, ExtractFinalAnswer, MajorityVote:** Standard utility functions for formatting prompts (see Figure 10 for initial prompt and Figure 11 for retry prompt), extracting answers, and performing majority voting.
459	
460	**Solve** Given a math problem  $x$ , we employ DeepSeek-R1-14B as a step-by-step solution proposer (the LLM in `GenerateSolutionWithDetection`) using an initial prompt like the one in Figure 10. The prompt is sent in streaming chat-completion mode, and tokens are appended sequentially to a buffer. If the initial solution attempt requires refinement based on verification feedback, a retry prompt like the one in Figure 11 is used.
461	
462	**Detect** The `GenerateSolutionWithDetection` function incorporates a mechanism to detect hesitation during reasoning. LLMs often employ hesitation words (e.g., "hmm", "let me verify") to self-verify. We observe that models may continue generating redundant checks even after reaching a solution. To decide when to truncate these overthinking situations and reduce redundant tokens, we use a streaming detection framework.
463	
464	We first define the set of hesitation cues, shown in Figure 12.### LLM Initial Solver Prompt
465	
466	```
467	The following is a math problem:  
468	[Math Problem]  
469	{question}  
470	Solve it step by step. For each step, you should use \n\n in the end.  
471	Please put your final answer (i.e., the index) in \boxed{{}}.
472	```
473	
474	Figure 10: LLM Initial Solver Prompt (Appendix). This prompt structure is utilized by the `FormatInitialPrompt` helper function.
475	
476	### LLM Retry Prompt with Feedback (Guided Solver)
477	
478	```
479	The following is a math problem:  
480	[Math Problem]  
481	{question}  
482	  
483	You previously attempted to solve this problem, and your solution was:  
484	[Previous Solution]  
485	{previous_solution_S1}  
486	  
487	That solution was reviewed, and the feedback is:  
488	[Verification Feedback]  
489	{verifier_feedback_F1}  
490	  
491	Please carefully consider the feedback and correct your solution. \\  
492	Provide a complete, new solution with clear reasoning steps. \\  
493	Please put your final answer (i.e., the index) in \boxed{{}}.
494	```
495	
496	Figure 11: LLM Retry Prompt with Feedback (Appendix). This prompt structure is utilized by the `FormatRetryPromptWithFeedback` helper function. Placeholders such as `{question}`, `{previous_solution_S1}`, and `{verifier_feedback_F1}` are dynamically populated.
497	
498	As each token  $t$  arrives during solution generation, if the end of the current reasoning sequence matches any hesitation keyword  $k \in \mathcal{K}$  (where  $\mathcal{K}$  is the set from Figure 12), we suspend the primary LLM proposer and trigger a detection process. A Detector LLM (which can be the same base model with a specific prompt) evaluates the current reasoning context using the prompt in Figure 13 to check whether a complete solution (including the final answer) has been reached. For efficiency, the Detector LLM is prompted to respond with only one token ("Yes" or "No") and minimal internal thought, for example:
499	
500	`&lt;think> Okay, I think I have finished thinking. &lt;/think>`
501	
502	To improve decision robustness, we compare the log-probabilities of "Yes" and "No" from the Detector LLM's top token predictions. If  $\log p(\text{Yes}) > \log p(\text{No})$ , we conclude that the current reasoning contains a complete solution. If hesitation was detected and the solution deemed complete, the generation might be explicitly continued (as per the Python code's 'continue-after-detected' logic) to capture any final utterances before concluding that segment of generation. The overall generation process then decides whether to terminate or proceed based on the pipeline's state.
503	
504	### A.3 Scaling of FlexiVe Modes on ProcessBench
505	
506	This section details the performance and token usage of FlexiVe when operating in its deliberative "With Thinking" (`Think@k`) mode versus its efficient "Without Thinking" (`NoThinking@k`) mode. The experiments were conducted on subsets of the ProcessBench benchmark (GSM8K, MATH, OlympiadBench, and OmniMATH) across various sampling budgets ( $k$ ).
507	
508	Table 2 shows the F1 scores and total token consumption for FlexiVe in "With Thinking" mode. This mode generally achieves higher F1 scores, especially as the sampling budget  $k$  increases, but at a significantly higher token cost.#### LLM Detection Prompt
509	
510	Wait, double-check, Alternatively, Hmm, Let me check,  
511	Alright, make sure, Another way, Let me verify, to confirm,  
512	Looking back, But wait
513	
514	Figure 12: A representative set of hesitation keywords monitored in the reasoning trace to detect potential solution completion (Appendix). (Requires customtakeaway environment definition.)
515	
516	#### LLM Detection Prompt
517	
518	You are a solution completeness checker.  
519	Given current solution to a math problem, determine if it is a complete  
520	solution (i.e., contains a final answer).  
521	Respond with exactly one word: 'Yes' if complete, 'No' otherwise.
522	
523	Figure 13: LLM Detection Prompt (Appendix).
524	
525	Conversely, Table 3 presents the results for the "Without Thinking" mode. This mode is significantly more token-efficient, though it generally results in lower F1 scores compared to the "With Thinking" mode at equivalent sampling budgets. The trade-off between accuracy and computational cost is evident when comparing these two modes.
526	
527	**Token Efficiency Summary** The "Without Thinking" mode demonstrates substantial token savings compared to the "With Thinking" mode:
528	
529	- • **GSM8K:** "Without Thinking" uses approximately 84.5% fewer tokens.
530	- • **MATH:** "Without Thinking" uses approximately 71.0% fewer tokens.
531	- • **OlympiadBench:** "Without Thinking" uses approximately 77.6% fewer tokens.
532	- • **OmniMATH:** "Without Thinking" uses approximately 76.8% fewer tokens.
533	- • **Average:** On average, the "Without Thinking" mode uses approximately 77.5% fewer tokens than the "With Thinking" mode across these datasets.
534	
535	This highlights the efficiency of the "NoThinking@k" approach for scenarios where computational budget is a primary constraint, while "Think@k" is preferable for achieving higher accuracy when more resources are available. The adaptive FlexiVe (Flex@k) mode, discussed in the main paper (Section 4.2), aims to balance these two extremes.
536	
537	### A.3.1 Supplementary Figures and Tables from Main Text Comments
538	
539	Table 2: Performance of FlexiVe "With Thinking" (Think@k) under different sampling budgets ( $k$ ) on ProcessBench subsets. Tokens are total generated across the respective test set.
540	
541	&lt;table border="1">&lt;thead>&lt;tr>&lt;th rowspan="2">Voting Budget (&lt;math>k&lt;/math>)&lt;/th>&lt;th colspan="2">GSM8K&lt;/th>&lt;th colspan="2">MATH&lt;/th>&lt;th colspan="2">OlympiadBench&lt;/th>&lt;th colspan="2">OmniMATH&lt;/th>&lt;/tr>&lt;tr>&lt;th>F1 (%)&lt;/th>&lt;th>Tokens&lt;/th>&lt;th>F1 (%)&lt;/th>&lt;th>Tokens&lt;/th>&lt;th>F1 (%)&lt;/th>&lt;th>Tokens&lt;/th>&lt;th>F1 (%)&lt;/th>&lt;th>Tokens&lt;/th>&lt;/tr>&lt;/thead>&lt;tbody>&lt;tr>&lt;td>2&lt;/td>&lt;td>82.3&lt;/td>&lt;td>2,412,972&lt;/td>&lt;td>81.9&lt;/td>&lt;td>5,209,255&lt;/td>&lt;td>78.0&lt;/td>&lt;td>8,428,333&lt;/td>&lt;td>71.3&lt;/td>&lt;td>7,055,913&lt;/td>&lt;/tr>&lt;tr>&lt;td>4&lt;/td>&lt;td>86.7&lt;/td>&lt;td>4,773,358&lt;/td>&lt;td>86.4&lt;/td>&lt;td>10,416,363&lt;/td>&lt;td>84.3&lt;/td>&lt;td>16,779,943&lt;/td>&lt;td>76.9&lt;/td>&lt;td>14,283,830&lt;/td>&lt;/tr>&lt;tr>&lt;td>8&lt;/td>&lt;td>86.4&lt;/td>&lt;td>9,534,029&lt;/td>&lt;td>88.9&lt;/td>&lt;td>20,913,932&lt;/td>&lt;td>85.4&lt;/td>&lt;td>33,417,171&lt;/td>&lt;td>78.9&lt;/td>&lt;td>28,633,370&lt;/td>&lt;/tr>&lt;tr>&lt;td>16&lt;/td>&lt;td>87.6&lt;/td>&lt;td>19,169,102&lt;/td>&lt;td>89.7&lt;/td>&lt;td>41,778,727&lt;/td>&lt;td>86.5&lt;/td>&lt;td>66,852,313&lt;/td>&lt;td>80.1&lt;/td>&lt;td>57,096,638&lt;/td>&lt;/tr>&lt;tr>&lt;td>32&lt;/td>&lt;td>87.7&lt;/td>&lt;td>38,055,768&lt;/td>&lt;td>89.7&lt;/td>&lt;td>83,807,676&lt;/td>&lt;td>86.7&lt;/td>&lt;td>133,587,678&lt;/td>&lt;td>80.6&lt;/td>&lt;td>114,215,045&lt;/td>&lt;/tr>&lt;tr>&lt;td>64&lt;/td>&lt;td>87.8&lt;/td>&lt;td>76,325,097&lt;/td>&lt;td>90.1&lt;/td>&lt;td>167,497,140&lt;/td>&lt;td>86.7&lt;/td>&lt;td>267,287,483&lt;/td>&lt;td>80.4&lt;/td>&lt;td>228,408,308&lt;/td>&lt;/tr>&lt;tr>&lt;td>128&lt;/td>&lt;td>88.1&lt;/td>&lt;td>152,675,054&lt;/td>&lt;td>90.0&lt;/td>&lt;td>335,401,726&lt;/td>&lt;td>86.7&lt;/td>&lt;td>534,138,821&lt;/td>&lt;td>80.5&lt;/td>&lt;td>456,401,199&lt;/td>&lt;/tr>&lt;/tbody>&lt;/table>Table 3: Performance of *FlexiVe* "Without Thinking" (NoThinking@k) under different sampling budgets ( $k$ ) on ProcessBench subsets. Tokens are total generated across the respective test set.
542	
543	&lt;table border="1">
544	&lt;thead>
545	&lt;tr>
546	&lt;th rowspan="2">Voting Budget (&lt;math>k&lt;/math>)&lt;/th>
547	&lt;th colspan="2">GSM8K&lt;/th>
548	&lt;th colspan="2">MATH&lt;/th>
549	&lt;th colspan="2">OlympiadBench&lt;/th>
550	&lt;th colspan="2">OmniMATH&lt;/th>
551	&lt;/tr>
552	&lt;tr>
553	&lt;th>F1 (%)&lt;/th>
554	&lt;th>Tokens&lt;/th>
555	&lt;th>F1 (%)&lt;/th>
556	&lt;th>Tokens&lt;/th>
557	&lt;th>F1 (%)&lt;/th>
558	&lt;th>Tokens&lt;/th>
559	&lt;th>F1 (%)&lt;/th>
560	&lt;th>Tokens&lt;/th>
561	&lt;/tr>
562	&lt;/thead>
563	&lt;tbody>
564	&lt;tr>
565	&lt;td>2&lt;/td>
566	&lt;td>61.5&lt;/td>
567	&lt;td>362,849&lt;/td>
568	&lt;td>57.2&lt;/td>
569	&lt;td>1,516,537&lt;/td>
570	&lt;td>49.0&lt;/td>
571	&lt;td>1,879,631&lt;/td>
572	&lt;td>50.5&lt;/td>
573	&lt;td>1,634,222&lt;/td>
574	&lt;/tr>
575	&lt;tr>
576	&lt;td>4&lt;/td>
577	&lt;td>66.8&lt;/td>
578	&lt;td>737,332&lt;/td>
579	&lt;td>61.3&lt;/td>
580	&lt;td>3,040,918&lt;/td>
581	&lt;td>53.8&lt;/td>
582	&lt;td>3,725,119&lt;/td>
583	&lt;td>52.5&lt;/td>
584	&lt;td>3,317,988&lt;/td>
585	&lt;/tr>
586	&lt;tr>
587	&lt;td>8&lt;/td>
588	&lt;td>66.7&lt;/td>
589	&lt;td>1,490,192&lt;/td>
590	&lt;td>62.8&lt;/td>
591	&lt;td>6,090,996&lt;/td>
592	&lt;td>55.2&lt;/td>
593	&lt;td>7,505,333&lt;/td>
594	&lt;td>53.6&lt;/td>
595	&lt;td>6,626,085&lt;/td>
596	&lt;/tr>
597	&lt;tr>
598	&lt;td>16&lt;/td>
599	&lt;td>66.8&lt;/td>
600	&lt;td>2,973,364&lt;/td>
601	&lt;td>64.3&lt;/td>
602	&lt;td>12,107,246&lt;/td>
603	&lt;td>55.9&lt;/td>
604	&lt;td>15,025,214&lt;/td>
605	&lt;td>54.2&lt;/td>
606	&lt;td>13,258,722&lt;/td>
607	&lt;/tr>
608	&lt;tr>
609	&lt;td>32&lt;/td>
610	&lt;td>66.5&lt;/td>
611	&lt;td>5,936,588&lt;/td>
612	&lt;td>64.4&lt;/td>
613	&lt;td>24,247,615&lt;/td>
614	&lt;td>55.9&lt;/td>
615	&lt;td>29,940,405&lt;/td>
616	&lt;td>54.7&lt;/td>
617	&lt;td>26,531,060&lt;/td>
618	&lt;/tr>
619	&lt;tr>
620	&lt;td>64&lt;/td>
621	&lt;td>66.8&lt;/td>
622	&lt;td>11,833,305&lt;/td>
623	&lt;td>64.2&lt;/td>
624	&lt;td>48,501,840&lt;/td>
625	&lt;td>56.1&lt;/td>
626	&lt;td>59,802,922&lt;/td>
627	&lt;td>54.0&lt;/td>
628	&lt;td>52,945,921&lt;/td>
629	&lt;/tr>
630	&lt;tr>
631	&lt;td>128&lt;/td>
632	&lt;td>66.7&lt;/td>
633	&lt;td>23,715,112&lt;/td>
634	&lt;td>65.0&lt;/td>
635	&lt;td>96,833,463&lt;/td>
636	&lt;td>56.3&lt;/td>
637	&lt;td>119,821,725&lt;/td>
638	&lt;td>54.1&lt;/td>
639	&lt;td>105,854,677&lt;/td>
640	&lt;/tr>
641	&lt;/tbody>
642	&lt;/table>
643	
644	Table 4: ProcessBench results reported with F1 scores. Results for *FlexiVe* are highlighted . **bold** indicates the best in the sub category. All *FlexiVe* variants are trained on only 1526 samples.
645	
646	&lt;table border="1">
647	&lt;thead>
648	&lt;tr>
649	&lt;th>Model&lt;/th>
650	&lt;th># Samples&lt;/th>
651	&lt;th>GSM8K&lt;/th>
652	&lt;th>MATH&lt;/th>
653	&lt;th>Olympiad Bench&lt;/th>
654	&lt;th>Omni-MATH&lt;/th>
655	&lt;th>Avg.&lt;/th>
656	&lt;/tr>
657	&lt;/thead>
658	&lt;tbody>
659	&lt;tr>
660	&lt;td colspan="7" style="text-align: center;">&lt;i>Proprietary Models&lt;/i>&lt;/td>
661	&lt;/tr>
662	&lt;tr>
663	&lt;td>GPT-4o-0806&lt;/td>
664	&lt;td>unk&lt;/td>
665	&lt;td>79.2&lt;/td>
666	&lt;td>63.6&lt;/td>
667	&lt;td>51.4&lt;/td>
668	&lt;td>53.5&lt;/td>
669	&lt;td>61.9&lt;/td>
670	&lt;/tr>
671	&lt;tr>
672	&lt;td>o1-mini&lt;/td>
673	&lt;td>unk&lt;/td>
674	&lt;td>93.2&lt;/td>
675	&lt;td>88.9&lt;/td>
676	&lt;td>87.2&lt;/td>
677	&lt;td>82.4&lt;/td>
678	&lt;td>87.9&lt;/td>
679	&lt;/tr>
680	&lt;tr>
681	&lt;td colspan="7" style="text-align: center;">&lt;i>Open Source Models (1.5B)&lt;/i>&lt;/td>
682	&lt;/tr>
683	&lt;tr>
684	&lt;td>Skywork-PRM-1.5B&lt;/td>
685	&lt;td>unk&lt;/td>
686	&lt;td>59.0&lt;/td>
687	&lt;td>48.0&lt;/td>
688	&lt;td>19.3&lt;/td>
689	&lt;td>19.2&lt;/td>
690	&lt;td>36.4&lt;/td>
691	&lt;/tr>
692	&lt;tr>
693	&lt;td>GenPRM-1.5B (Pass@1) w/ Code Exec&lt;/td>
694	&lt;td>23K&lt;/td>
695	&lt;td>52.8&lt;/td>
696	&lt;td>66.6&lt;/td>
697	&lt;td>55.1&lt;/td>
698	&lt;td>54.5&lt;/td>
699	&lt;td>57.3&lt;/td>
700	&lt;/tr>
701	&lt;tr>
702	&lt;td colspan="7" style="text-align: center;">&lt;i>Open Source Models (7-8B)&lt;/i>&lt;/td>
703	&lt;/tr>
704	&lt;tr>
705	&lt;td>Math-Shepherd-PRM-7B&lt;/td>
706	&lt;td>445K&lt;/td>
707	&lt;td>47.9&lt;/td>
708	&lt;td>29.5&lt;/td>
709	&lt;td>24.8&lt;/td>
710	&lt;td>23.8&lt;/td>
711	&lt;td>31.5&lt;/td>
712	&lt;/tr>
713	&lt;tr>
714	&lt;td>RLHFlow-PRM-Mistral-8B&lt;/td>
715	&lt;td>273K&lt;/td>
716	&lt;td>50.4&lt;/td>
717	&lt;td>33.4&lt;/td>
718	&lt;td>13.8&lt;/td>
719	&lt;td>15.8&lt;/td>
720	&lt;td>28.4&lt;/td>
721	&lt;/tr>
722	&lt;tr>
723	&lt;td>EurusPRM-Stage2&lt;/td>
724	&lt;td>30K&lt;/td>
725	&lt;td>47.3&lt;/td>
726	&lt;td>35.7&lt;/td>
727	&lt;td>21.2&lt;/td>
728	&lt;td>20.9&lt;/td>
729	&lt;td>31.3&lt;/td>
730	&lt;/tr>
731	&lt;tr>
732	&lt;td>Qwen2.5-Math-PRM-7B&lt;/td>
733	&lt;td>~344K&lt;/td>
734	&lt;td>82.4&lt;/td>
735	&lt;td>77.6&lt;/td>
736	&lt;td>67.5&lt;/td>
737	&lt;td>66.3&lt;/td>
738	&lt;td>73.5&lt;/td>
739	&lt;/tr>
740	&lt;tr>
741	&lt;td>RetrievalPRM-7B&lt;/td>
742	&lt;td>404K&lt;/td>
743	&lt;td>74.6&lt;/td>
744	&lt;td>71.1&lt;/td>
745	&lt;td>60.2&lt;/td>
746	&lt;td>57.3&lt;/td>
747	&lt;td>65.8&lt;/td>
748	&lt;/tr>
749	&lt;tr>
750	&lt;td>Universal-PRM-7B&lt;/td>
751	&lt;td>unk&lt;/td>
752	&lt;td>85.8&lt;/td>
753	&lt;td>77.7&lt;/td>
754	&lt;td>67.6&lt;/td>
755	&lt;td>66.4&lt;/td>
756	&lt;td>74.3&lt;/td>
757	&lt;/tr>
758	&lt;tr>
759	&lt;td>Direct Generative PRM-7B&lt;/td>
760	&lt;td>23K&lt;/td>
761	&lt;td>63.9&lt;/td>
762	&lt;td>65.8&lt;/td>
763	&lt;td>54.5&lt;/td>
764	&lt;td>55.9&lt;/td>
765	&lt;td>60.0&lt;/td>
766	&lt;/tr>
767	&lt;tr>
768	&lt;td>GenPRM-7B w/ Code Exec (Pass@1)&lt;/td>
769	&lt;td>23K&lt;/td>
770	&lt;td>78.7&lt;/td>
771	&lt;td>80.3&lt;/td>
772	&lt;td>72.2&lt;/td>
773	&lt;td>69.8&lt;/td>
774	&lt;td>75.2&lt;/td>
775	&lt;/tr>
776	&lt;tr>
777	&lt;td>GenPRM-7B w/ Code Exec (Maj@8)&lt;/td>
778	&lt;td>23K&lt;/td>
779	&lt;td>81.0&lt;/td>
780	&lt;td>85.7&lt;/td>
781	&lt;td>78.4&lt;/td>
782	&lt;td>76.8&lt;/td>
783	&lt;td>80.5&lt;/td>
784	&lt;/tr>
785	&lt;tr>
786	&lt;td colspan="7" style="text-align: center;">&lt;i>Open Source Models (14-32B) w/ Moderate Compute&lt;/i>&lt;/td>
787	&lt;/tr>
788	&lt;tr>
789	&lt;td>Dyve-14B&lt;/td>
790	&lt;td>117K&lt;/td>
791	&lt;td>68.5&lt;/td>
792	&lt;td>58.3&lt;/td>
793	&lt;td>49.0&lt;/td>
794	&lt;td>47.2&lt;/td>
795	&lt;td>55.8&lt;/td>
796	&lt;/tr>
797	&lt;tr>
798	&lt;td>GenPRM-32B w/o Code Exec (Maj@8)&lt;/td>
799	&lt;td>23K&lt;/td>
800	&lt;td>78.8&lt;/td>
801	&lt;td>85.1&lt;/td>
802	&lt;td>78.7&lt;/td>
803	&lt;td>74.9&lt;/td>
804	&lt;td>79.3&lt;/td>
805	&lt;/tr>
806	&lt;tr>
807	&lt;td>&lt;i>FlexiVe&lt;/i> (Flex@32)&lt;/td>
808	&lt;td>&lt;b>1526&lt;/b>&lt;/td>
809	&lt;td>82.8&lt;/td>
810	&lt;td>83.3&lt;/td>
811	&lt;td>79.2&lt;/td>
812	&lt;td>73.4&lt;/td>
813	&lt;td>79.7&lt;/td>
814	&lt;/tr>
815	&lt;tr>
816	&lt;td>&lt;i>FlexiVe&lt;/i> (Flex@128)&lt;/td>
817	&lt;td>&lt;b>1526&lt;/b>&lt;/td>
818	&lt;td>&lt;b>83.0&lt;/b>&lt;/td>
819	&lt;td>&lt;b>85.0&lt;/b>&lt;/td>
820	&lt;td>&lt;b>80.0&lt;/b>&lt;/td>
821	&lt;td>&lt;b>75.2&lt;/b>&lt;/td>
822	&lt;td>&lt;b>80.8&lt;/b>&lt;/td>
823	&lt;/tr>
824	&lt;tr>
825	&lt;td colspan="7" style="text-align: center;">&lt;i>Open Source Models (14-32B) w/ High Compute&lt;/i>&lt;/td>
826	&lt;/tr>
827	&lt;tr>
828	&lt;td>GenPRM-32B (Pass@1) w/ Code Exec&lt;/td>
829	&lt;td>23K&lt;/td>
830	&lt;td>83.1&lt;/td>
831	&lt;td>81.7&lt;/td>
832	&lt;td>72.8&lt;/td>
833	&lt;td>72.8&lt;/td>
834	&lt;td>77.6&lt;/td>
835	&lt;/tr>
836	&lt;tr>
837	&lt;td>GenPRM-32B (Maj@8) w/ Code Exec&lt;/td>
838	&lt;td>23K&lt;/td>
839	&lt;td>85.1&lt;/td>
840	&lt;td>86.3&lt;/td>
841	&lt;td>78.9&lt;/td>
842	&lt;td>80.1&lt;/td>
843	&lt;td>82.6&lt;/td>
844	&lt;/tr>
845	&lt;tr>
846	&lt;td>&lt;i>FlexiVe&lt;/i> (Think@64)&lt;/td>
847	&lt;td>&lt;b>1526&lt;/b>&lt;/td>
848	&lt;td>&lt;b>88.1&lt;/b>&lt;/td>
849	&lt;td>&lt;b>90.1&lt;/b>&lt;/td>
850	&lt;td>&lt;b>86.7&lt;/b>&lt;/td>
851	&lt;td>&lt;b>80.4&lt;/b>&lt;/td>
852	&lt;td>&lt;b>86.3&lt;/b>&lt;/td>
853	&lt;/tr>
854	&lt;/tbody>
855	&lt;/table>Figure 14: F1 score scaling with voting budget  $k$  on GSM8K (left) and MATH (right). FlexiVe (Flex@ $k$ , green circles) improves with larger  $k$ , performing comparably or better than DS14B (blue triangles, baseline verifier), while both surpass the FlexiVe (NoThinking variant, red squares). (Previously commented out from main text).
856	
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f94bed9-7482-438e-8e99-9a99685d83bf",
  "isSidechain": true,
  "promptId": "893c21bf-c2a9-4d7f-b44e-6410c59daba9",
  "agentId": "a9f50be13f2913edb",
  "type": "user",
  "uuid": "0e3e1240-76a4-4d29-a333-3df466210fb8",
  "sourceToolAssistantUUID": "5f94bed9-7482-438e-8e99-9a99685d83bf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-28T02:49:57.813Z_

Now let me search for any citations, follow-up work, and the connection to Dyve (which appears to be from the same authors).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e3e1240-76a4-4d29-a333-3df466210fb8",
  "isSidechain": true,
  "agentId": "a9f50be13f2913edb",
  "requestId": "req_011CbUCvGWztenBcXPhvGs9f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b8a189c4-37cb-4aec-8bc3-b8a5bb8c6a5e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P6dtJsz8QbgLK7veFvhhBT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25672,
      "cache_read_input_tokens": 14314,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25672,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-28T02:49:59.318Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EE7LX9ZjqMyTW5j5HH1vrn`</summary>

```json
{
  "query": "FlexiVe Dyve same authors \"Jianyuan Zhong\" \"Qiang Xu\" CUHK process verification 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8a189c4-37cb-4aec-8bc3-b8a5bb8c6a5e",
  "isSidechain": true,
  "agentId": "a9f50be13f2913edb",
  "requestId": "req_011CbUCvGWztenBcXPhvGs9f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af53e817-18d5-4f4a-b74c-122e02c6cecf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P6dtJsz8QbgLK7veFvhhBT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25672,
      "cache_read_input_tokens": 14314,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25672,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-28T02:49:59.814Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014yawQaMQPPKPYzY9wHGLJs`</summary>

```json
{
  "query": "arxiv 2505.11966 citations cited by follow-up work 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af53e817-18d5-4f4a-b74c-122e02c6cecf",
  "isSidechain": true,
  "agentId": "a9f50be13f2913edb",
  "requestId": "req_011CbUCvGWztenBcXPhvGs9f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bfcdbe95-6336-407c-b902-b3da03939e62",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P6dtJsz8QbgLK7veFvhhBT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25672,
      "cache_read_input_tokens": 14314,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25672,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-28T02:50:04.553Z_

<details><summary>↩ Tool result · `toolu_014yawQaMQPPKPYzY9wHGLJs`</summary>

```text
Web search results for query: "arxiv 2505.11966 citations cited by follow-up work 2025 2026"

Links: [{"title":"Dual-Model LLM Ensemble via Web Chat Interfaces Reaches Near-Perfect Sensitivity for Systematic-Review Screening: A Multi-Domain Validation with Equivalence to API Access","url":"https://www.medrxiv.org/content/10.1101/2025.11.03.25339455.full.pdf"},{"title":"Evaluating General-Purpose LLMs for Patient-Facing Use: Dermatology-Centered Systematic Review and Meta-Analysis","url":"https://www.medrxiv.org/content/10.1101/2025.08.11.25333149.full.pdf"},{"title":"Non-Steroidal or Opioid Analgesia Use for Children With Musculoskeletal Injuries","url":"https://clinicaltrials.gov/study/NCT03767933"},{"title":"Triaging and Referring in Adjacent General and Emergency Departments","url":"https://clinicaltrials.gov/study/NCT03793972"},{"title":"Compound Deception in Elite Peer Review: A Failure Mode Taxonomy of 100 Fabricated Citations at NeurIPS 2025","url":"https://arxiv.org/pdf/2602.05930"},{"title":"The Silent Author in Urology: Quantifying Large Language Model Influence at the Corpus Level","url":"https://www.medrxiv.org/content/10.1101/2025.07.21.25331681.full.pdf"}]

The search results don't contain specific information about arxiv paper 2505.11966 or its citations and follow-up work. The results returned are unrelated papers from 2025-2026 in various domains (medical, dermatology, clinical trials) but nothing specific to the arxiv identifier you mentioned.

To find information about that specific arxiv paper and its citations/follow-up work, you might want to:

1. Visit the arxiv paper directly at: https://arxiv.org/abs/2505.11966
2. Check arxiv's citation tracking features or use Google Scholar (scholar.google.com) with the arxiv ID
3. Use Semantic Scholar (semanticscholar.org) which has good citation tracking features

Would you like me to try a different search approach, or do you have more specific information about the paper's title or authors that might help narrow down the search?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bfcdbe95-6336-407c-b902-b3da03939e62",
  "isSidechain": true,
  "promptId": "893c21bf-c2a9-4d7f-b44e-6410c59daba9",
  "agentId": "a9f50be13f2913edb",
  "type": "user",
  "uuid": "63644305-b324-4e19-97c6-4a714fc489f4",
  "sourceToolAssistantUUID": "bfcdbe95-6336-407c-b902-b3da03939e62",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-28T02:50:06.983Z_

<details><summary>↩ Tool result · `toolu_01EE7LX9ZjqMyTW5j5HH1vrn`</summary>

```text
Web search results for query: "FlexiVe Dyve same authors "Jianyuan Zhong" "Qiang Xu" CUHK process verification 2025"

Links: [{"title":"(PDF) Solve-Detect-Verify: Inference-Time Scaling with Flexible Generative Verifier","url":"https://www.researchgate.net/publication/391878031_Solve-Detect-Verify_Inference-Time_Scaling_with_Flexible_Generative_Verifier"},{"title":"arXiv:2505.11966v1 [cs.AI] 17 May 2025","url":"https://arxiv.org/pdf/2505.11966"},{"title":"[2502.11157] Dyve: Thinking Fast and Slow for Dynamic Process Verification","url":"https://arxiv.org/abs/2502.11157"},{"title":"Dyve: Thinking Fast and Slow for Dynamic Process Verification","url":"https://arxiv.org/html/2502.11157"},{"title":"Dyve: Thinking Fast and Slow for Dynamic Process Verification - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1136/"},{"title":"Thinking Fast and Slow for Dynamic Process Verification","url":"https://aclanthology.org/2025.emnlp-main.1136.pdf"},{"title":"Solve-Detect-Verify: Inference-Time Scaling with Flexible Generative Verifier | OpenReview","url":"https://openreview.net/forum?id=iPn5Ejloxm"},{"title":"Jianyuan Zhong","url":"https://www.catalyzex.com/author/Jianyuan%20Zhong"},{"title":"Qiang Xu – CUHK CSE","url":"https://www.cse.cuhk.edu.hk/people/faculty/qiang-xu/"},{"title":"Qiang Xu","url":"https://openreview.net/profile?id=~Qiang_Xu1"}]

Based on the search results, I found two related papers with the same authors from CUHK that focus on process verification:

## FlexiVe and Dyve Papers

Both papers are authored by Jianyuan Zhong and Qiang Xu from The Chinese University of Hong Kong, along with co-authors Zeju Li, Zhijian Xu, Xiangyu Wen, and Kezhi Li.

**1. Dyve: Thinking Fast and Slow for Dynamic Process Verification**

Dyve is a dynamic process verifier that enhances reasoning error detection in large language models by integrating fast and slow thinking, inspired by Kahneman's Systems Theory. It leverages a novel step-wise consensus-filtered process supervision technique, combining Monte Carlo estimation with LLM based evaluation, and experimental results on ProcessBench and the MATH dataset confirm that Dyve significantly outperforms existing process-based verifiers.

**2. FlexiVe (Solve-Detect-Verify): Inference-Time Scaling with Flexible Generative Verifier**

FlexiVe is a novel generative verifier that flexibly balances computational resources between rapid, reliable fast thinking and meticulous slow thinking using a Flexible Allocation of Verification Budget strategy, and the Solve-Detect-Verify pipeline is an efficient inference-time scaling framework that intelligently integrates FlexiVe. Experiments show FlexiVe achieves superior accuracy in pinpointing errors within reasoning traces on ProcessBench.

Both papers were published in 2025 and address the challenge of balancing accuracy and computational efficiency in LLM process verification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af53e817-18d5-4f4a-b74c-122e02c6cecf",
  "isSidechain": true,
  "promptId": "893c21bf-c2a9-4d7f-b44e-6410c59daba9",
  "agentId": "a9f50be13f2913edb",
  "type": "user",
  "uuid": "e9e3419e-8c32-45e2-b389-b64e49ea82ea",
  "sourceToolAssistantUUID": "af53e817-18d5-4f4a-b74c-122e02c6cecf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-28T02:50:14.666Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JXZsvgQGhYWyDhsBXxcYU4`</summary>

```json
{
  "query": "site:semanticscholar.org \"Solve-Detect-Verify\" OR \"FlexiVe\" flexible generative verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9e3419e-8c32-45e2-b389-b64e49ea82ea",
  "isSidechain": true,
  "agentId": "a9f50be13f2913edb",
  "requestId": "req_011CbUCwRp8U955513BMgcuJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ea2b49ac-03a4-4ded-8da2-5b0484bc6798",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NZLzvt4H3TNBHgqb1AkmLs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 635,
      "cache_creation_input_tokens": 1104,
      "cache_read_input_tokens": 39986,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1104,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 56,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-28T02:50:15.907Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HeM4baWWdr2TAw11fRzZDk`</summary>

```json
{
  "url": "https://api.semanticscholar.org/graph/v1/paper/ArXiv:2505.11966?fields=citationCount,citations.title,citations.year,citations.externalIds",
  "prompt": "Extract all citation information: how many papers cite this work, and list the titles and years of all citing papers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea2b49ac-03a4-4ded-8da2-5b0484bc6798",
  "isSidechain": true,
  "agentId": "a9f50be13f2913edb",
  "requestId": "req_011CbUCwRp8U955513BMgcuJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b7bca0e-7a4f-4e02-8c16-a19e01d9d0e0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NZLzvt4H3TNBHgqb1AkmLs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 635,
      "cache_creation_input_tokens": 1104,
      "cache_read_input_tokens": 39986,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1104,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 56,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-28T02:50:16.272Z_

<details><summary>↩ Tool result · `toolu_01HeM4baWWdr2TAw11fRzZDk`</summary>

```text
The server returned HTTP 429 Too Many Requests.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b7bca0e-7a4f-4e02-8c16-a19e01d9d0e0",
  "isSidechain": true,
  "promptId": "893c21bf-c2a9-4d7f-b44e-6410c59daba9",
  "agentId": "a9f50be13f2913edb",
  "type": "user",
  "uuid": "81485a50-8090-42cb-8bb2-e18ee3b2c683",
  "sourceToolAssistantUUID": "6b7bca0e-7a4f-4e02-8c16-a19e01d9d0e0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-28T02:50:23.459Z_

<details><summary>↩ Tool result · `toolu_01JXZsvgQGhYWyDhsBXxcYU4`</summary>

```text
Web search results for query: "site:semanticscholar.org "Solve-Detect-Verify" OR "FlexiVe" flexible generative verifier"

Links: [{"title":"Solve-Detect-Verify: Inference-Time Scaling with Flexible Generative Verifier | OpenReview","url":"https://openreview.net/forum?id=iPn5Ejloxm"},{"title":"(PDF) Solve-Detect-Verify: Inference-Time Scaling with Flexible Generative Verifier","url":"https://www.researchgate.net/publication/391878031_Solve-Detect-Verify_Inference-Time_Scaling_with_Flexible_Generative_Verifier"},{"title":"[2505.11966] Solve-Detect-Verify: Inference-Time Scaling with Flexible Generative Verifier","url":"https://arxiv.org/abs/2505.11966"},{"title":"Paper page - Solve-Detect-Verify: Inference-Time Scaling with Flexible Generative Verifier","url":"https://huggingface.co/papers/2505.11966"},{"title":"Solve-Detect-Verify: Inference-Time Scaling with Flexible ...","url":"https://arxiv.org/pdf/2505.11966"},{"title":"Trust but Verify! A Survey on Verification Design for Test-time Scaling","url":"https://arxiv.org/html/2508.16665v1"}]

I found relevant results about "Solve-Detect-Verify" and "FlexiVe" flexible generative verifier. Here's what the search returned:

## Overview

Large Language Model (LLM) reasoning for complex tasks involves a trade-off between solution accuracy and computational efficiency, and verification further complicates this by introducing its own challenging trade-off: sophisticated Generative Reward Models can be computationally prohibitive if naively integrated with LLMs at test-time, while simpler, faster methods may lack reliability.

## FlexiVe

FlexiVe is a novel generative verifier that flexibly balances computational resources between rapid, reliable fast thinking and meticulous slow thinking using a Flexible Allocation of Verification Budget strategy. The training strategy uses Reinforcement Learning (GRPO) to specifically enhance the reliability of the fast mode, and remarkably, this targeted training generalizes, elevating the slow mode to state-of-the-art performance.

## Solve-Detect-Verify Pipeline

The Solve-Detect-Verify pipeline is an efficient inference-time scaling framework that intelligently integrates FlexiVe, proactively identifying solution completion points to trigger targeted verification and provide focused solver feedback. The pipeline consists of three stages: Solve (an LLM generates an initial solution), Detect (a lightweight mechanism monitors the LLM's output for hesitation keywords and uses log-probabilities to assess if a solution is complete), and Verify and Refine (FlexiVe assesses the candidate solution—if correct, it's finalized; if errors are found, FlexiVe's feedback guides the solver to generate a single new, refined solution).

The research paper was published in May 2025 (arxiv ID: 2505.11966).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea2b49ac-03a4-4ded-8da2-5b0484bc6798",
  "isSidechain": true,
  "promptId": "893c21bf-c2a9-4d7f-b44e-6410c59daba9",
  "agentId": "a9f50be13f2913edb",
  "type": "user",
  "uuid": "bcff19d4-c5de-4150-8c5d-cc2e40cdc6cb",
  "sourceToolAssistantUUID": "ea2b49ac-03a4-4ded-8da2-5b0484bc6798",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-28T02:50:27.116Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013CmD818GqpqySENvihPC3e`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.16665v3",
  "prompt": "Find any mention of FlexiVe or Solve-Detect-Verify or arXiv 2505.11966 in this survey paper. Extract the context in which it is discussed and what the survey says about it."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bcff19d4-c5de-4150-8c5d-cc2e40cdc6cb",
  "isSidechain": true,
  "agentId": "a9f50be13f2913edb",
  "requestId": "req_011CbUCxNfQ9qfB6RbqGR7Y2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "22e3a068-0d8f-488b-8730-83a254716fb9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013PpSNd8dMVqUP2Bojq4MVQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 87,
      "cache_creation_input_tokens": 1648,
      "cache_read_input_tokens": 41090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1648,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 62,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-28T02:50:27.895Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Eysusgxs5agU3c5A6GzKn4`</summary>

```json
{
  "query": "\"process reward model\" ProcessBench SOTA leaderboard 2025 2026 comparison FlexiVe GenPRM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22e3a068-0d8f-488b-8730-83a254716fb9",
  "isSidechain": true,
  "agentId": "a9f50be13f2913edb",
  "requestId": "req_011CbUCxNfQ9qfB6RbqGR7Y2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "13ac63ac-02c2-4d08-8d9c-54b85e40b3c7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013PpSNd8dMVqUP2Bojq4MVQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 87,
      "cache_creation_input_tokens": 1648,
      "cache_read_input_tokens": 41090,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1648
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 87,
          "output_tokens": 196,
          "cache_read_input_tokens": 41090,
          "cache_creation_input_tokens": 1648,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1648,
            "ephemeral_1h_input_tokens": 0
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

_source line 39 · 2026-05-28T02:50:34.989Z_

<details><summary>↩ Tool result · `toolu_013CmD818GqpqySENvihPC3e`</summary>

```text
# Mentions of FlexiVe and Solve-Detect-Verify

## FlexiVe

**Context:** FlexiVe is discussed in Section 3.4 (Reasoning-Based Generative Verifiers) as an adaptive verification framework.

**What the survey says:**
The paper describes FlexiVe as proposing "adaptive verification frameworks that tailor compute usage to the complexity of the instance." It notes that FlexiVe "use[s] Group Relative Policy Optimization (GRPO) to train a process verifier" with a composite reward function. One component encourages correct verification while another "penalizes unnecessarily long outputs," incentivizing the verifier to "dynamically switch between fast and slow modes based on task difficulty."

The survey also includes FlexiVe (Zhong et al., 2025a) in Table 1 and Table 4 as an approach that trains "a LRM as dynamic verifier with RL alternating between fast and slow thinking."

## Solve-Detect-Verify / arXiv 2505.11966

**Finding:** The arXiv identifier 2505.11966 is not directly mentioned in this survey document. However, the reference appears to correspond to FlexiVe based on the citation pattern, though the exact paper may be referenced under a different identifier in the bibliography.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22e3a068-0d8f-488b-8730-83a254716fb9",
  "isSidechain": true,
  "promptId": "893c21bf-c2a9-4d7f-b44e-6410c59daba9",
  "agentId": "a9f50be13f2913edb",
  "type": "user",
  "uuid": "4d3ab595-04b4-49a4-aeae-96482db89733",
  "sourceToolAssistantUUID": "22e3a068-0d8f-488b-8730-83a254716fb9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-28T02:50:40.101Z_

<details><summary>↩ Tool result · `toolu_01Eysusgxs5agU3c5A6GzKn4`</summary>

```text
Web search results for query: ""process reward model" ProcessBench SOTA leaderboard 2025 2026 comparison FlexiVe GenPRM"

Links: [{"title":"GenPRM: Scaling Test-Time Compute of Process Reward Models via   Generative Reasoning","url":"https://arxiv.org/pdf/2504.00891"},{"title":"Efficient Process Reward Model Training via Active Learning","url":"https://arxiv.org/pdf/2504.10559"},{"title":"FreePRM: Training Process Reward Models Without Ground Truth Process Labels","url":"https://arxiv.org/pdf/2506.03570"},{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://arxiv.org/pdf/2501.03124"},{"title":"Process Reward Models That Think","url":"https://arxiv.org/pdf/2504.16828"}]

I found some relevant information about process reward models and ProcessBench benchmarks. Let me search specifically for FlexiVe to get more complete information:

Links: [{"title":"Retrieval-Augmented Process Reward Model for ...","url":"https://aclanthology.org/2025.findings-acl.444.pdf"},{"title":"GitHub - JLZhong23/awesome-reward-models · GitHub","url":"https://github.com/JLZhong23/awesome-reward-models"},{"title":"Process Reward Models: Step-Level Feedback for LLMs","url":"https://www.emergentmind.com/topics/process-reward-models-prm"},{"title":"The Lessons of Developing Process Reward Models in Mathematical Reasoning - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.547/"},{"title":"GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub","url":"https://github.com/RyanLiu112/Awesome-Process-Reward-Models"},{"title":"Process-supervised Reward Models (PRMs)","url":"https://www.emergentmind.com/topics/process-supervised-reward-models-prms"},{"title":"Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning","url":"https://arxiv.org/pdf/2509.26578"},{"title":"Process Reward Models That Think | OpenReview","url":"https://openreview.net/forum?id=V727xqBYIW"}]

Based on my web search results, I've found relevant information about process reward models and the ProcessBench benchmark, though I notice the search results don't contain specific information about "FlexiVe" as mentioned in your query. Here's what I found:

## GenPRM Performance on ProcessBench

GenPRM-7B surpasses Qwen2.5-Math-PRM-72B on ProcessBench through test-time scaling, demonstrating strong performance among recent process reward models.

## SOTA Results (2025)

ACTPRM achieves a new state-of-the-art PRM on ProcessBench (75.0%) and PRMBench (65.5%) compared with same sized models.

## Other Notable Models on ProcessBench

- THINKPRM beats baselines on ProcessBench, MATH-500, and AIME '24 under best-of-N selection and reward-guided search
- FreePRM achieves an average F1 score of 53.0% on ProcessBench, outperforming fully supervised PRM trained on Math-Shepherd by +24.1%

## Process Reward Models Overview

Process-supervised Reward Models supplant the outcome-only signal of traditional reward modeling with stepwise supervision over each partial state or action in a chain-of-thought (CoT) trajectory.

Unfortunately, my search results do not contain specific information about a model or approach called "FlexiVe" in the context of process reward models. If you have more details about FlexiVe or would like me to search for additional information, please let me know!


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13ac63ac-02c2-4d08-8d9c-54b85e40b3c7",
  "isSidechain": true,
  "promptId": "893c21bf-c2a9-4d7f-b44e-6410c59daba9",
  "agentId": "a9f50be13f2913edb",
  "type": "user",
  "uuid": "aa90b4fe-3671-492f-b3ce-0afeea8085bb",
  "sourceToolAssistantUUID": "13ac63ac-02c2-4d08-8d9c-54b85e40b3c7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-28T02:52:12.394Z_

I now have comprehensive information about this paper. Here is the detailed report.

---

## Detailed Research Report: FlexiVe / Solve-Detect-Verify (arXiv 2505.11966)

### Basic Information

**Full Title:** "Solve-Detect-Verify: Inference-Time Scaling with Flexible Generative Verifier"

**Authors:** Jianyuan Zhong\*, Zeju Li\* (co-first authors), Zhijian Xu, Xiangyu Wen, Kezhi Li, Qiang Xu (corresponding author) -- all from The Chinese University of Hong Kong (CUHK).

**Submitted:** May 17, 2025 to arXiv (cs.AI). License: CC BY 4.0.

**Venue status:** The paper was submitted to **ICLR 2026** but was **withdrawn** (last modified January 6, 2026, per OpenReview). No acceptance at any venue as of the information available.

**Predecessor work:** The same lead authors (Zhong, Li, Xu, Wen, Xu) previously published **Dyve: Thinking Fast and Slow for Dynamic Process Verification** (arXiv 2502.11157), which was accepted at **EMNLP 2025**. FlexiVe is explicitly positioned as an improvement over Dyve -- the paper critiques Dyve's per-step verification as accumulating significant overhead.

---

### Method: How FlexiVe Works

FlexiVe is a **generative verifier** with two operating modes -- "fast thinking" and "slow thinking" -- governed by a **Flexible Allocation of Verification Budget (FAVB)** strategy. It is integrated into a three-stage **Solve-Detect-Verify** pipeline.

#### The Two Modes

- **Fast thinking (NoThinking mode):** Inspired by Ma et al. (2025), the model bypasses explicit chain-of-thought reasoning during verification. A template fills the thinking phase (e.g., `&lt;beginning_of_thinking> Okay, I think I have finished thinking. &lt;/end_of_thinking>`), producing outputs that are **27x-40x shorter** than slow mode. Despite this brevity, FlexiVe's fast mode is made reliable through RL training (see below).

- **Slow thinking (standard reasoning mode):** The model generates full deliberative reasoning traces during verification, producing detailed error analysis. This is computationally expensive but more accurate per-sample.

#### Flexible Allocation of Verification Budget (FAVB) -- The Core Mechanism

This is the key innovation for balancing fast and slow verification:

1. **Initial fast probing:** Run `k` parallel "fast thinking" verification passes on the entire reasoning trace.
2. **Compute agreement ratio:** `R_agreement = max_i(a_i) / k`, where `a_i` counts the most frequent outcome using fuzzy error index matching.
3. **Decision threshold:** If `R_agreement >= tau` (a predefined threshold), accept the consensus result from the fast phase (`V_fast`). Otherwise, trigger `max(1, k/8)` additional "slow thinking" runs and use their consensus (`V_slow`).

This means easy-to-verify solutions (where fast probes agree) get verified cheaply, while ambiguous cases are escalated to expensive slow verification. The decision is made at the **whole-trace level**, not per-step.

#### Solution-Level vs. Step-Level: A Critical Distinction

FlexiVe operates at the **solution level (whole-trace analysis)**, not step-by-step. The paper explicitly states: "this decision logic and the subsequent verification (whether fast or slow) are applied to the reasoning trace as a whole, rather than on a per-step basis as in some prior dynamic verifiers like Dyve." The verifier takes the entire reasoning trace, formatted with a critic template, and outputs `V_out = (F, idx_pred)` where `F` is textual error analysis and `idx_pred` is the predicted index of the first erroneous step (or -1 if no errors).

So while the **output** identifies a specific step index (making it useful for process-level error detection on ProcessBench), the **verification process itself** analyzes the whole trace holistically in a single pass. This is fundamentally different from Dyve or GenPRM which verify step-by-step sequentially. The key trade-off: whole-trace analysis avoids the accumulated cost of per-step decisions but may miss fine-grained step interactions that sequential verification could catch.

---

### GRPO Training: How It Differs from Standard GRPO

**Base model:** DeepSeek-R1-Distill-Qwen-14B (a 14B parameter model).

**Training data:** Only **1,526 samples** from the BIG-Bench Mistake dataset (90% train, 10% validation). This is remarkably small compared to baselines (GenPRM uses 23K, Qwen2.5-Math-PRM uses ~344K, Math-Shepherd uses 445K).

**Training setup:** LoRA PEFT (r=16, alpha=32) targeting attention projection layers. AdamW optimizer with lr=5e-6. G=14 samples per input for GRPO. KL coefficient=0.04. Trained on 8x NVIDIA A800-SXM4-80GB GPUs.

**Key difference from standard GRPO -- the composite reward:**

The reward function is `R_i = R_correct + R_length`, where:

- **R_correct:** Binary reward (1.0 if predicted error index matches ground truth, 0.0 otherwise). Standard correctness signal.

- **R_length (the novel part):** A length penalty that **differentiates between correct and incorrect traces:**
  - When `idx_gt = -1` (no error): Penalizes responses exceeding `L_fast`, promoting concise "fast thinking" for correct traces.
  - When `idx_gt != -1` (error exists): Penalizes responses shorter than `L_slow_min` OR longer than `L_slow_max`, encouraging "detailed thinking" within a target range for error cases.

This dual-objective reward is what teaches FlexiVe to naturally produce short outputs when traces are correct (fast mode) and longer, more detailed analysis when errors exist (slow mode). **Crucially, all training is performed in "fast mode" (NoThinking activated)**, yet this targeted RL training generalizes to also improve the slow thinking mode -- a finding the authors highlight as a key result.

**Why RL over SFT:** The paper includes an ablation comparing RL (GRPO) vs. SFT. An SFT baseline trained on 10,000 samples from OpenO1 with LLM-based labels showed poor generalization. ProcessBench traces come from weaker, non-thinking LLMs and are shorter/less complex. SFT overfit to its training distribution, while RL with only 1,526 samples generalized effectively across diverse reasoning styles.

---

### The Solve-Detect-Verify Pipeline

**Stage 1 -- Solve:** DeepSeek-R1-14B (or 32B) generates an initial step-by-step solution.

**Stage 2 -- Detect:** A lightweight streaming monitor watches for "hesitation keywords" (e.g., "hmm", "let me verify", "wait", "double-check", "let me check", "but wait" -- 12 keywords listed). When detected, the system queries the same LLM with a one-token completion prompt ("Is this a complete solution? Yes/No") using log-probability comparison. This reuses >90% of the KV cache, adding minimal overhead. If the solution is deemed complete, generation stops early, saving tokens from "overthinking."

**Stage 3 -- Verify and Refine:** FlexiVe verifies the candidate solution. If valid, it becomes the final answer. If errors are found, FlexiVe's diagnostic feedback (error analysis + step index) is formatted into a retry prompt that guides the solver to generate one corrected solution. This second attempt uses Best-of-N with majority voting (no re-verification). There is no iterative loop -- at most two attempts.

---

### Key Results

#### ProcessBench (Error Detection F1 Scores)

**Moderate Compute:**
| Model | Training Data | GSM8K | MATH | OlympiadBench | OmniMATH | Avg |
|-------|--------------|-------|------|---------------|----------|-----|
| GenPRM-32B w/o Code (Maj@8) | 23K | 78.8 | 85.1 | 78.7 | 74.9 | 79.3 |
| FlexiVe (Flex@32) | **1,526** | 82.8 | 83.3 | 79.2 | 73.4 | 79.7 |
| FlexiVe (Flex@128) | **1,526** | **83.0** | **85.0** | **80.0** | **75.2** | **80.8** |

**High Compute:**
| Model | Training Data | GSM8K | MATH | OlympiadBench | OmniMATH | Avg |
|-------|--------------|-------|------|---------------|----------|-----|
| GenPRM-32B w/ Code (Maj@8) | 23K | 85.1 | 86.3 | 78.9 | 80.1 | 82.6 |
| FlexiVe (Think@64) | **1,526** | **88.1** | **90.1** | **86.7** | **80.4** | **86.3** |

The **80.8% avg F1 (Moderate Compute)** and **86.3% avg F1 (High Compute)** figures are confirmed. FlexiVe (Think@64) surpasses GenPRM-32B with code execution despite being a 14B model trained on 15x less data. Only the proprietary o1-mini (87.9%) exceeds it among all models tested.

#### Mathematical Reasoning Benchmarks
- **AIME 2024:** Solve-Detect-Verify achieves 83.3% with 16 solutions, up from 56.6% baseline (single pass) and 73.3% with Flex@8 single pipeline. Achieves higher accuracy with ~4x fewer solutions than baselines.
- **AIME 2025:** 50.0% with Flex@8 single pipeline vs. 43.3% baseline.
- **CNMO:** Matches baseline (55.5%) with Flex@8 while using only 0.80x the tokens.

#### Token Efficiency
- Flex@8 on MATH achieves higher F1 with ~3x fewer tokens than the baseline verifier.
- NoThinking mode uses ~77.5% fewer tokens on average across datasets.
- The Detect module alone (without verification) reduces token usage to 0.67x on AIME2024 and 0.43x on CNMO.

---

### Limitations and What Step-Level Routing Could Address

The authors identify several limitations:

1. **Domain generalization:** Validated only on mathematical reasoning. Cross-domain applicability (code, commonsense QA) is untested.
2. **Empirical hyperparameters:** The threshold `tau` and initial budget `k` are set empirically without principled tuning guidelines.
3. **Multi-component overhead:** The pipeline's dynamic mode-switching introduces inherent overhead that could be reduced with optimized inference engines (vLLM, SGLang).
4. **Training data diversity:** Generalization is inherently linked to training data diversity (only BIG-Bench Mistake was used).

**What step-level routing could address that FlexiVe cannot:**

- **Granular error localization:** FlexiVe's holistic trace analysis may miss subtle errors in individual steps that are masked by the overall trace appearing reasonable. Step-level verification can catch errors that are locally detectable but globally ambiguous.
- **Partial credit / early stopping in verification:** With step-level routing, verification can stop as soon as an error is found in an early step, rather than always processing the entire trace. Conversely, if only the final steps are suspect, only those need deep analysis.
- **Heterogeneous step difficulty:** Within a single solution, some steps may be trivial (arithmetic) while others are conceptually difficult (insight steps). Step-level routing could allocate fast verification to easy steps and slow verification to hard steps, something FlexiVe's trace-level decision cannot do.
- **CNMO inconsistency:** The paper notes that on CNMO, varying only the verifier budget "might not universally ensure peak performance," suggesting the whole-trace approach struggles with certain problem types where fine-grained step analysis would help.
- **The Flex@128 vs Think@64 gap:** Flex@128 (moderate compute, adaptive) achieves 80.8% avg F1, while Think@64 (high compute, all-slow) reaches 86.3%. The 5.5-point gap suggests that the fast-mode probes miss errors that slow verification catches -- a step-level routing approach could more surgically apply slow verification to specific suspicious steps rather than requiring full slow verification of the entire trace.

---

### Citations and Impact

The paper is cited in the survey "Trust but Verify! A Survey on Verification Design for Test-time Scaling" (arXiv 2508.16665), which discusses FlexiVe in its section on reasoning-based generative verifiers and includes it in comparative tables. The same first author (Jianyuan Zhong) also maintains an "awesome-reward-models" repository on GitHub. Despite being withdrawn from ICLR 2026, the paper has received attention on HuggingFace Papers and ResearchGate.

Sources:
- [arXiv Abstract](https://arxiv.org/abs/2505.11966)
- [arXiv PDF](https://arxiv.org/pdf/2505.11966)
- [OpenReview (ICLR 2026 - Withdrawn)](https://openreview.net/forum?id=iPn5Ejloxm)
- [HuggingFace Papers](https://huggingface.co/papers/2505.11966)
- [Dyve (predecessor, EMNLP 2025)](https://arxiv.org/abs/2502.11157)
- [Trust but Verify Survey citing FlexiVe](https://arxiv.org/html/2508.16665v3)
- [ResearchGate](https://www.researchgate.net/publication/391878031_Solve-Detect-Verify_Inference-Time_Scaling_with_Flexible_Generative_Verifier)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa90b4fe-3671-492f-b3ce-0afeea8085bb",
  "isSidechain": true,
  "agentId": "a9f50be13f2913edb",
  "requestId": "req_011CbUCybnTegB1J71HVzVHE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2ffaa6ad-f248-4d5d-85ea-14cd30b966ad",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13f2f0f6-9a9f-4b22-8071-05196d59bedf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DbCgjB2xbz2ZkyGhS6PGoJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1628,
      "cache_read_input_tokens": 42738,
      "output_tokens": 3527,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1628
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3527,
          "cache_read_input_tokens": 42738,
          "cache_creation_input_tokens": 1628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1628,
            "ephemeral_1h_input_tokens": 0
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
