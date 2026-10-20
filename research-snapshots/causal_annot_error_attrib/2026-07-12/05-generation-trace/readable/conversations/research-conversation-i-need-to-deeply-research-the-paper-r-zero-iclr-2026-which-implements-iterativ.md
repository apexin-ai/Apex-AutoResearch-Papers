# Research conversation: I need to deeply research the paper "R-Zero" (ICLR 2026) which implements iterative challenger-solver co-evolution via G

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a629672d73d886a3c.jsonl`
- **Structured JSON:** [`505546ae713b1c9c1a7b.json`](../../sessions/50/505546ae713b1c9c1a7b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

44 recorded events

### User

_source line 1 · 2026-05-28T05:07:58.174Z_

I need to deeply research the paper "R-Zero" (ICLR 2026) which implements iterative challenger-solver co-evolution via GRPO, achieving +6.49 on math reasoning. This is relevant to a research idea about PRM-diagnosed adaptive curriculum for generator-verifier co-improvement.

Please:
1. Search the web for "R-Zero ICLR 2026 challenger solver co-evolution GRPO"
2. Also try "R-Zero iterative self-improvement math reasoning 2026"
3. Try "R-Zero reinforcement learning co-evolution 2025 2026"
4. Fetch and read the actual paper once found
5. Report back:
   - Full title and authors
   - Core method: how does challenger-solver co-evolution work? What drives curriculum adaptation?
   - Is it uncertainty-based? How does it select/generate problems?
   - What's the training loop?
   - Key results
   - How does it compare to using PRM error taxonomy for curriculum?
   - Key limitations
   
Be thorough.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c7973f03-d621-459f-9572-b6284262bbbb",
  "agentId": "a629672d73d886a3c",
  "type": "user",
  "uuid": "3eabbb60-e0b9-42cc-bb20-092b6b104e3d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-28T05:07:58.177Z_

```json
{
  "parentUuid": "3eabbb60-e0b9-42cc-bb20-092b6b104e3d",
  "isSidechain": true,
  "agentId": "a629672d73d886a3c",
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
  "uuid": "e669a1ab-5616-4f3a-bfe2-b7e6cdafeb8d",
  "timestamp": "2026-05-28T05:07:58.177Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-28T05:07:58.177Z_

```json
{
  "parentUuid": "e669a1ab-5616-4f3a-bfe2-b7e6cdafeb8d",
  "isSidechain": true,
  "agentId": "a629672d73d886a3c",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "6f35f4d4-4132-48a0-b50c-e48463b7f961",
  "timestamp": "2026-05-28T05:07:58.177Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-28T05:08:00.819Z_



I'll conduct a thorough search for the R-Zero paper. Let me start by loading the web search and fetch tools, then run multiple searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f35f4d4-4132-48a0-b50c-e48463b7f961",
  "isSidechain": true,
  "agentId": "a629672d73d886a3c",
  "requestId": "req_011CbUPSs5dd3ctpLVimcJJB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "240a49bb-d081-4d2d-b344-b4dfde6f2729",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CbPGZCkXZh7TXbwDF5FWY5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1593,
      "cache_read_input_tokens": 7411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1593,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 5 · 2026-05-28T05:08:01.102Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018MP7RfVfp66qadH6oM4t1Z`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "240a49bb-d081-4d2d-b344-b4dfde6f2729",
  "isSidechain": true,
  "agentId": "a629672d73d886a3c",
  "requestId": "req_011CbUPSs5dd3ctpLVimcJJB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6c2217fe-5174-4c0e-9001-f89110646149",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CbPGZCkXZh7TXbwDF5FWY5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1593,
      "cache_read_input_tokens": 7411,
      "output_tokens": 114,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1593
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 114,
          "cache_read_input_tokens": 7411,
          "cache_creation_input_tokens": 1593,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1593,
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

_source line 6 · 2026-05-28T05:08:01.109Z_

<details><summary>↩ Tool result · `toolu_018MP7RfVfp66qadH6oM4t1Z`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

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
  "parentUuid": "6c2217fe-5174-4c0e-9001-f89110646149",
  "isSidechain": true,
  "promptId": "c7973f03-d621-459f-9572-b6284262bbbb",
  "agentId": "a629672d73d886a3c",
  "type": "user",
  "uuid": "4f1411cc-fe83-48da-9f5d-44aabb342137",
  "sourceToolAssistantUUID": "6c2217fe-5174-4c0e-9001-f89110646149",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-28T05:08:03.960Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f1411cc-fe83-48da-9f5d-44aabb342137",
  "isSidechain": true,
  "agentId": "a629672d73d886a3c",
  "requestId": "req_011CbUPT5tK8t9kRKNTduoHD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9d419950-948f-47e8-9df5-9fe48fc9c16e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lj4sMBQcvU3u3PJaaaVNHh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1136,
      "cache_read_input_tokens": 9004,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1136,
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

_source line 8 · 2026-05-28T05:08:04.417Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NpinixiZeuXUkQsDBy5HUR`</summary>

```json
{
  "query": "R-Zero ICLR 2026 challenger solver co-evolution GRPO"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d419950-948f-47e8-9df5-9fe48fc9c16e",
  "isSidechain": true,
  "agentId": "a629672d73d886a3c",
  "requestId": "req_011CbUPT5tK8t9kRKNTduoHD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "982914f0-d3c2-4260-ad7d-533ffa5d71cc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lj4sMBQcvU3u3PJaaaVNHh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1136,
      "cache_read_input_tokens": 9004,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1136,
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

_source line 9 · 2026-05-28T05:08:04.903Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ef6Ae7f7kLgEP595oddVNv`</summary>

```json
{
  "query": "R-Zero iterative self-improvement math reasoning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "982914f0-d3c2-4260-ad7d-533ffa5d71cc",
  "isSidechain": true,
  "agentId": "a629672d73d886a3c",
  "requestId": "req_011CbUPT5tK8t9kRKNTduoHD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "82d9a168-0e85-4505-92e3-de3115cb8486",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lj4sMBQcvU3u3PJaaaVNHh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1136,
      "cache_read_input_tokens": 9004,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1136
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 178,
          "cache_read_input_tokens": 9004,
          "cache_creation_input_tokens": 1136,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1136,
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

### Tool call

_source line 10 · 2026-05-28T05:08:04.907Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PZMG5kxtohtgtG6M9SRLw5`</summary>

```json
{
  "query": "R-Zero reinforcement learning co-evolution 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82d9a168-0e85-4505-92e3-de3115cb8486",
  "isSidechain": true,
  "agentId": "a629672d73d886a3c",
  "requestId": "req_011CbUPT5tK8t9kRKNTduoHD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ab3d430-26a9-4f64-b78f-eff66457d1ff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lj4sMBQcvU3u3PJaaaVNHh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1136,
      "cache_read_input_tokens": 9004,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1136
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 178,
          "cache_read_input_tokens": 9004,
          "cache_creation_input_tokens": 1136,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1136,
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

_source line 11 · 2026-05-28T05:08:11.031Z_

<details><summary>↩ Tool result · `toolu_01NpinixiZeuXUkQsDBy5HUR`</summary>

```text
Web search results for query: "R-Zero ICLR 2026 challenger solver co-evolution GRPO"

Links: [{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2508.05004"},{"title":"R-Zero: SELF-EVOLVING REASONING LLM","url":"https://openreview.net/pdf/c3487788910b4d304009a6766423d5a7f7604fb4.pdf"},{"title":"R-Zero: Self-Evolving Reasoning LLM from Zero Data","url":"https://arxiv.org/html/2508.05004v1"},{"title":"Technical Report R-Zero: Self-Evolving Reasoning LLM from Zero Data","url":"https://www.arxiv.org/pdf/2508.05004v1"},{"title":"R-Zero: Self-Evolving Reasoning LLM from Zero Data","url":"https://gptshop.ai/paper/RZero.pdf"},{"title":"GitHub - Chengsong-Huang/R-Zero: [ICLR2026] codes for R-Zero: Self-Evolving Reasoning LLM from Zero Data (https://www.arxiv.org/pdf/2508.05004) · GitHub","url":"https://github.com/Chengsong-Huang/R-Zero"},{"title":"R-Zero: Self-Evolving Reasoning LLM from Zero Data","url":"https://chengsong-huang.github.io/R-Zero.github.io/"},{"title":"R-Zero: Self-Evolving Reasoning LLM from Zero Data | OpenReview","url":"https://openreview.net/forum?id=96apU6YzSO"},{"title":"[2508.05004] R-Zero: Self-Evolving Reasoning LLM from Zero Data","url":"https://arxiv.org/abs/2508.05004"}]

Here are the search results for R-Zero ICLR 2026:

R-Zero is a framework that starts from a single base LLM and initializes two independent models with distinct roles—a Challenger and a Solver. These models are optimized separately and co-evolve through interaction: the Challenger is rewarded for proposing tasks near the edge of the Solver capability, and the Solver is rewarded for solving increasingly challenging tasks posed by the Challenger.

In the Challenger training phase, the Challenger is trained via Group Relative Policy Optimization (GRPO) to generate difficult questions. In the Solver training phase, the Solver is fine-tuned with GRPO on a filtered set of these challenging questions generated by the now-frozen Challenger, using the pseudo-labels voted by itself.

This iterative process allows the Challenger and Solver to co-evolve, leading to a progressively more capable Solver. This process yields a targeted, self-improving curriculum without any pre-existing tasks and labels.

R-Zero is a model-agnostic framework that consistently and iteratively improves the reasoning abilities of different backbone LLMs. For example, Qwen3-4B-Base model's average score on math benchmarks increased by a significant +6.49 points after three iterations of self-evolution.

The paper was published as a conference paper at ICLR 2026. The official code and implementation details are available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "982914f0-d3c2-4260-ad7d-533ffa5d71cc",
  "isSidechain": true,
  "promptId": "c7973f03-d621-459f-9572-b6284262bbbb",
  "agentId": "a629672d73d886a3c",
  "type": "user",
  "uuid": "89864862-135d-439c-b1f5-562298063197",
  "sourceToolAssistantUUID": "982914f0-d3c2-4260-ad7d-533ffa5d71cc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-28T05:08:12.571Z_

<details><summary>↩ Tool result · `toolu_01PZMG5kxtohtgtG6M9SRLw5`</summary>

```text
Web search results for query: "R-Zero reinforcement learning co-evolution 2025 2026"

Links: [{"title":"R-Zero: Self-Evolving Reasoning LLM from Zero Data","url":"https://arxiv.org/html/2508.05004v1"},{"title":"[2508.05004] R-Zero: Self-Evolving Reasoning LLM from Zero Data","url":"https://arxiv.org/abs/2508.05004"},{"title":"R-Zero: SELF-EVOLVING REASONING LLM","url":"https://arxiv.org/pdf/2508.05004"},{"title":"R-Zero: A Fully Autonomous AI Framework that Generates Its Own Training Data from Scratch - MarkTechPost","url":"https://www.marktechpost.com/2025/08/15/r-zero-a-fully-autonomous-ai-framework-that-generates-its-own-training-data-from-scratch/"},{"title":"Tool-R0: Self-Evolving LLM Agents for Tool-Learning from Zero Data","url":"https://arxiv.org/pdf/2602.21320"},{"title":"Intrinsic fluctuations of reinforcement learning promote cooperation","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9873645/"},{"title":"Co-Evolution of Predator-Prey Ecosystems by Reinforcement Learning Agents","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8069842/"}]

Based on the search results, here's what I found about R-Zero and reinforcement learning co-evolution:

## R-Zero: Self-Evolving Reasoning LLM

R-Zero is a fully autonomous framework that generates its own training data from scratch. Starting from a single base LLM, R-Zero initializes two independent models with distinct roles: a Challenger and a Solver.

### How It Works

The framework introduces a co-evolutionary dynamic between the two models: the Challenger is responsible for creating new, challenging reasoning tasks near the edge of the Solver's capability, while the Solver is trained to solve increasingly difficult problems posed by the Challenger, enabling the curriculum to be self-generated and adapted continuously to the model's evolving strengths and weaknesses.

### Key Innovation

R-Zero removes the reliance on external tasks and labels entirely. The framework characterizes co-evolutionary dynamics to identify both strengths and limitations, offering insights for future research.

### Performance

R-Zero can act as a mid-training method, as models first improved by this method achieve higher performance after fine-tuned on labeled data.

The research was published in September 2025, making it a recent development in the field of self-evolving language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ab3d430-26a9-4f64-b78f-eff66457d1ff",
  "isSidechain": true,
  "promptId": "c7973f03-d621-459f-9572-b6284262bbbb",
  "agentId": "a629672d73d886a3c",
  "type": "user",
  "uuid": "f7a0f288-8d33-4489-8026-d78171a4c11d",
  "sourceToolAssistantUUID": "1ab3d430-26a9-4f64-b78f-eff66457d1ff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-28T05:08:13.101Z_

<details><summary>↩ Tool result · `toolu_01Ef6Ae7f7kLgEP595oddVNv`</summary>

```text
Web search results for query: "R-Zero iterative self-improvement math reasoning 2026"

Links: [{"title":"R-Zero: Self-Evolving Reasoning LLM from Zero Data | OpenReview","url":"https://openreview.net/forum?id=96apU6YzSO"},{"title":"GitHub - Chengsong-Huang/R-Zero: [ICLR2026] codes for R-Zero: Self-Evolving Reasoning LLM from Zero Data (https://www.arxiv.org/pdf/2508.05004) · GitHub","url":"https://github.com/Chengsong-Huang/R-Zero"},{"title":"[2508.05004] R-Zero: Self-Evolving Reasoning LLM from Zero Data","url":"https://arxiv.org/abs/2508.05004"},{"title":"R-Zero: SELF-EVOLVING REASONING LLM","url":"https://arxiv.org/pdf/2508.05004"},{"title":"R-Zero: Self-Evolving Reasoning LLM from Zero Data","url":"https://arxiv.org/html/2508.05004"},{"title":"R-Zero: A Method For Training Reasoning LLMs With Zero Data Is Here","url":"https://www.intoai.pub/p/r-zero"},{"title":"R-Zero: Self-Evolving Reasoning LLM from Zero Data - ArXivIQ","url":"https://arxiviq.substack.com/p/r-zero-self-evolving-reasoning-llm"},{"title":"R-Zero: Self-Evolving Reasoning LLM from Zero Data","url":"https://chengsong-huang.github.io/R-Zero.github.io/"},{"title":"R-Zero : Train LLMs with No data. R-Zero: Self-Evolving Reasoning LLM… | by Mehul Gupta | Data Science in Your Pocket | Medium","url":"https://medium.com/data-science-in-your-pocket/r-zero-train-llms-with-no-data-4d5c43cb454c"},{"title":"rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking | OpenReview","url":"https://openreview.net/forum?id=5zwF1GizFa"}]

Based on the search results, here's what I found about R-Zero:

## Overview

R-Zero is a fully autonomous framework that generates its own training data from scratch. R-Zero is a novel framework that enables LLMs to improve their reasoning abilities autonomously, without needing any pre-existing tasks or labels.

## How It Works

R-Zero initializes two independent models with distinct roles, a Challenger and a Solver. These models are optimized separately and co-evolve through interaction: the Challenger is rewarded for proposing tasks near the edge of the Solver capability, and the Solver is rewarded for solving increasingly challenging problems.

The Challenger is first trained to generate difficult questions based on a reward signal derived from the uncertainty of the frozen Solver. Next, the Solver is fine-tuned on a filtered set of challenging questions generated by the now-frozen Challenger. This process iteratively results in co-evolution and improvements of both these LLM versions.

## Performance Results

R-Zero is a model-agnostic framework, consistently and iteratively improving the reasoning abilities of different backbone LLMs. For example, Qwen3-4B-Base model's average score on math benchmarks increased by a significant +6.49 points after three iterations of self-evolution.

The reasoning skills learned through math-focused questions can generalize to complex general-domain tasks, with models trained using R-Zero showing significant improvements on general domain reasoning benchmarks like MMLU-Pro and SuperGPQA.

The work is set to be published at ICLR 2026 according to the GitHub repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "82d9a168-0e85-4505-92e3-de3115cb8486",
  "isSidechain": true,
  "promptId": "c7973f03-d621-459f-9572-b6284262bbbb",
  "agentId": "a629672d73d886a3c",
  "type": "user",
  "uuid": "ba86f77e-9f1e-4844-ad6a-4fa64eb79eec",
  "sourceToolAssistantUUID": "82d9a168-0e85-4505-92e3-de3115cb8486",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-28T05:08:15.911Z_

Excellent, I've found the paper. Now let me fetch the actual paper content and the project page for detailed information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba86f77e-9f1e-4844-ad6a-4fa64eb79eec",
  "isSidechain": true,
  "agentId": "a629672d73d886a3c",
  "requestId": "req_011CbUPTxuPy3YvemQVryk6W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5e17eea-6966-44cb-98b9-d648aa9df656",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LN8ebD4bx7uDUh3sNFaZeS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 696,
      "cache_creation_input_tokens": 1984,
      "cache_read_input_tokens": 10140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1984,
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

_source line 15 · 2026-05-28T05:08:16.839Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01F9imUi7wheFY585qCvAEtf`</summary>

```json
{
  "url": "https://arxiv.org/abs/2508.05004",
  "prompt": "Extract the full title, all authors, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5e17eea-6966-44cb-98b9-d648aa9df656",
  "isSidechain": true,
  "agentId": "a629672d73d886a3c",
  "requestId": "req_011CbUPTxuPy3YvemQVryk6W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "231347d2-1ab0-492b-967d-30c2f53c3d7b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LN8ebD4bx7uDUh3sNFaZeS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 696,
      "cache_creation_input_tokens": 1984,
      "cache_read_input_tokens": 10140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1984,
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

_source line 16 · 2026-05-28T05:08:20.746Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WqjDJcupQ2WTLRKCSGWnVe`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.05004v1",
  "prompt": "Extract ALL detailed information from this paper including: 1) Full method description - how does the Challenger-Solver co-evolution work step by step? 2) How is the Challenger reward defined? What is the uncertainty-based reward? 3) How is the Solver trained? 4) What is the exact training loop / algorithm? 5) How are problems selected/filtered? 6) All experimental results and benchmarks. 7) All ablation studies. 8) All limitations discussed. 9) How does curriculum adaptation work? 10) Any comparison to PRM or process reward models? Be extremely thorough and include all mathematical formulations if present."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "231347d2-1ab0-492b-967d-30c2f53c3d7b",
  "isSidechain": true,
  "agentId": "a629672d73d886a3c",
  "requestId": "req_011CbUPTxuPy3YvemQVryk6W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11f2c80f-5574-4e08-9592-d7284bf39f5a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LN8ebD4bx7uDUh3sNFaZeS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 696,
      "cache_creation_input_tokens": 1984,
      "cache_read_input_tokens": 10140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1984,
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

_source line 17 · 2026-05-28T05:08:21.513Z_

<details><summary>↩ Tool result · `toolu_01F9imUi7wheFY585qCvAEtf`</summary>

```text
# R-Zero Paper Details

**Full Title:**
"R-Zero: Self-Evolving Reasoning LLM from Zero Data"

**Authors:**
Chengsong Huang, Wenhao Yu, Xiaoyang Wang, Hongming Zhang, Zongxia Li, Ruosen Li, Jiaxin Huang, Haitao Mi, and Dong Yu

**Complete Abstract:**
The paper describes an autonomous framework enabling large language models to "generate its own training data from scratch." The system uses two specialized models—a Challenger and a Solver—that co-evolve through interaction. The Challenger proposes tasks at the edge of the Solver's capabilities, while the Solver tackles increasingly difficult challenges. This creates a self-improving curriculum without requiring pre-existing human-labeled tasks. Results demonstrate substantial reasoning improvements across different model sizes, including gains of +6.49 on mathematical reasoning and +7.54 on general reasoning benchmarks for the Qwen3-4B-Base model.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "231347d2-1ab0-492b-967d-30c2f53c3d7b",
  "isSidechain": true,
  "promptId": "c7973f03-d621-459f-9572-b6284262bbbb",
  "agentId": "a629672d73d886a3c",
  "type": "user",
  "uuid": "1b2db701-52b4-452a-8b89-a6d8daab5e12",
  "sourceToolAssistantUUID": "231347d2-1ab0-492b-967d-30c2f53c3d7b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-28T05:08:21.634Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KyiQDrodnNpW5iG1wsa7jJ`</summary>

```json
{
  "url": "https://chengsong-huang.github.io/R-Zero.github.io/",
  "prompt": "Extract all details about R-Zero including method description, results, and any additional information not in the paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b2db701-52b4-452a-8b89-a6d8daab5e12",
  "isSidechain": true,
  "agentId": "a629672d73d886a3c",
  "requestId": "req_011CbUPTxuPy3YvemQVryk6W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1e4a844-aff1-49db-9764-59103af9ede8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LN8ebD4bx7uDUh3sNFaZeS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 696,
      "cache_creation_input_tokens": 1984,
      "cache_read_input_tokens": 10140,
      "output_tokens": 424,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1984
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 696,
          "output_tokens": 424,
          "cache_read_input_tokens": 10140,
          "cache_creation_input_tokens": 1984,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1984,
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

_source line 19 · 2026-05-28T05:08:26.867Z_

<details><summary>↩ Tool result · `toolu_01KyiQDrodnNpW5iG1wsa7jJ`</summary>

```text
# R-Zero: Self-Evolving Reasoning LLM Overview

## Core Concept
R-Zero is a framework enabling large language models to autonomously improve reasoning abilities without pre-existing datasets. The system features a co-evolutionary dynamic between two model instances working in tandem.

## Method Components

**The Challenger Role:** This model generates problems calibrated at "the edge of the Solver's current abilities," creating an adaptive curriculum that progressively increases difficulty.

**The Solver Role:** This instance tackles increasingly challenging tasks, learning through iterative refinement.

**Data Generation Process:** The Solver's multiple attempts undergo majority voting to establish pseudo-labels, generating training data for fine-tuning without external annotation.

## Key Results

The framework demonstrated substantial gains across benchmarks:

- **Qwen3-8B mathematical reasoning:** Performance improved from 49.18 to 54.69 across three iterations (+5.51 points)
- **General-domain transfer:** Average scores improved by +3.81 points, indicating successful skill generalization beyond mathematics
- **Progressive improvement:** Each iteration showed consistent gains, validating the co-evolutionary approach

## Research Significance

The RL-trained Challenger proved essential—the performance jump from baseline to iteration one confirmed that intelligent curriculum design substantially outperforms standard approaches. Results confirm the method enhances underlying model capabilities rather than merely teaching domain-specific content.

**Institutions involved:** Tencent AI Seattle Lab, Washington University in St. Louis, University of Maryland, and University of Texas at Dallas
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1e4a844-aff1-49db-9764-59103af9ede8",
  "isSidechain": true,
  "promptId": "c7973f03-d621-459f-9572-b6284262bbbb",
  "agentId": "a629672d73d886a3c",
  "type": "user",
  "uuid": "2a754250-ebf8-41ff-aa10-afd6526615fa",
  "sourceToolAssistantUUID": "a1e4a844-aff1-49db-9764-59103af9ede8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-28T05:08:48.931Z_

<details><summary>↩ Tool result · `toolu_01WqjDJcupQ2WTLRKCSGWnVe`</summary>

```text
# R-Zero: Comprehensive Analysis

## 1) Full Method Description

R-Zero implements a co-evolutionary framework where two models initialized from the same base LLM assume distinct roles:

**Challenger (Q_θ)**: Generates synthetic math problems designed to be at the edge of the Solver's capabilities.

**Solver (S_φ)**: Answers increasingly difficult questions generated by the Challenger.

The iterative loop operates as:
1. Challenger training via GRPO using uncertainty-based rewards
2. Dataset construction through filtering and majority voting
3. Solver training via GRPO on curated problem sets
4. Repeat for multiple iterations

The framework operates entirely without human labels or pre-existing task corpora, creating a self-contained improvement cycle.

## 2) Challenger Reward Definition

The Challenger receives a **composite reward signal** combining three components:

**Uncertainty Reward:**
The primary signal measures when the Solver is maximally uncertain. For generated question x, the framework samples m responses from the frozen Solver, determines the majority-vote pseudo-label ỹ(x), and computes empirical accuracy p̂(x;S_φ). The uncertainty reward is defined as:

r_uncertainty(x;φ) = 1 - 2|p̂(x;S_φ) - 1/2|

This function peaks when the Solver's success probability approaches 50%, incentivizing "edge of capability" problems. The authors provide theoretical justification grounded in KL divergence bounds, noting that "the right-hand side of the inequality, which is proportional to the reward variance, is maximized precisely when p̂=0.5."

**Repetition Penalty:**
Encourages diversity using BLEU score similarity. Pairwise distances d_ij = 1 - BLEU(x_i, x_j) are computed with threshold τ_BLEU = 0.5. Questions are clustered using agglomerative hierarchical clustering (average linkage), then penalized: r_rep(x_i) = λ|C_k|/B, where λ=1, |C_k| is cluster size, and B is batch size.

**Format Check Penalty:**
Questions lacking proper &lt;question>&lt;/question> tags receive immediate reward of 0.

**Final Composite Reward:**
r_i = max(0, r_uncertainty(x_i;φ) - r_rep(x_i))

## 3) Solver Training

The Solver uses Group Relative Policy Optimization (GRPO) on the curated dataset S with binary verification rewards:

r_j = {1 if answer matches pseudo-label ỹ_i; 0 otherwise}

For each question in S, the Solver generates multiple answers and receives rewards based on exact match to the majority-voted answer. The policy is updated via GRPO loss minimization using the same advantage normalization as the Challenger, but with simpler, deterministic reward signals based on correctness verification.

## 4) Exact Training Loop / Algorithm

**Per Iteration:**

1. **Challenger Phase:** Train Q_θ via GRPO using frozen S_φ
   - Generate N=8,000 candidate questions
   - Compute rewards: uncertainty (m=10 samples), repetition penalty, format check
   - Apply GRPO loss with KL regularization (β=10^-2)
   - Maximum 5 training steps, 4 rollouts per step

2. **Dataset Construction:** Filter generated questions
   - Sample m=10 answers from current Solver for each question
   - Determine pseudo-label via majority vote
   - Retain questions where 3-7 answers match pseudo-label (δ=0.25)
   - This filtering removes overly easy and overly hard problems

3. **Solver Phase:** Fine-tune S_φ on dataset S
   - Train via GRPO with binary correctness rewards
   - Global batch size 128, learning rate 1×10^-6
   - Maximum 15 training steps, 5 rollouts per step
   - KL penalty coefficient λ_KL = 1×10^-2

4. **Repeat:** Freeze Challenger, begin next iteration

## 5) Problem Selection/Filtering Strategy

The filtering mechanism operates on two levels:

**Consistency-Based Filtering:** For each candidate question, the framework computes p̂_i (proportion of Solver answers matching majority vote). Only questions satisfying |p̂_i - 1/2| ≤ δ (with δ=0.25) are retained. This band [0.25, 0.75] discards problems where Solver agreement is too high (too easy) or too low (ambiguous/ill-posed).

The authors note this filtering "acts as an implicit quality control mechanism. Since pseudo-labels are derived from majority vote, a very low empirical correctness p̂_i often indicates that the question itself is ambiguous, ill-posed, or that the resulting pseudo-label is unreliable."

**Diversity Enforcement:** The repetition penalty uses BLEU-based clustering to prevent redundant problem generation within batches.

## 6) Experimental Results

**Mathematical Reasoning Benchmarks** (Table 1):

On Qwen3-4B-Base across seven benchmarks (AMC, Minerva, MATH-500, GSM8K, Olympiad-Bench, AIME-2024, AIME-2025):
- Base Model: 42.58 average
- After 3 iterations: 49.07 average
- **Improvement: +6.49 points**

Qwen3-8B-Base:
- Base: 49.18 → After iteration 3: 54.69 (+5.51)

OctoThinker-3B:
- Base: 26.64 → Iteration 3: 29.32 (+2.68)

OctoThinker-8B:
- Base: 36.41 → Iteration 3: 38.52 (+2.11)

**General Domain Reasoning** (Table 2):

Improvements on MMLU-Pro, SuperGPQA, and BBEH demonstrate transfer learning:
- Qwen3-4B-Base general average: 27.10 → 34.64 (+7.54)
- Qwen3-8B-Base general average: 34.49 → 38.73 (+4.24)

The framework shows that "training language models on reasoning-intensive domains, such as mathematics, can lead to improvements in general-domain capabilities."

## 7) Ablation Studies (Table 3)

Tested on Qwen3-4B-Base:

| Ablation | Math AVG | General AVG | Impact |
|----------|----------|-------------|--------|
| Full R-Zero | 48.06 | 30.41 | Baseline |
| w/o RL-Challenger | 44.36 | 26.32 | -3.7 / -4.1 |
| w/o Repetition Penalty | 45.76 | 27.56 | -2.3 / -2.9 |
| w/o Filtering | 47.35 | 24.26 | -0.7 / -6.1 |

The **largest degradation** occurs when disabling Challenger's RL training, demonstrating the criticality of co-evolutionary curriculum generation. Removing filtering causes particularly severe damage to general reasoning (-6.1 points), suggesting quality control is essential.

## 8) Limitations Discussed

**Data Quality Degradation:** Table 4 reveals a critical vulnerability—pseudo-label accuracy systematically declines across iterations:
- Iteration 1: 79.0% accuracy
- Iteration 2: 69.0%
- Iteration 3: 63.0%

The authors acknowledge this "decline in data quality is a critical trade-off and a potential bottleneck for the framework's ultimate performance."

**Domain Restrictions:** The framework excels in domains with objective correctness verification (mathematics). The conclusion states: "The core mechanism of R-Zero is currently suited for domains where correctness can be objectively determined. Extending this self-evolutionary paradigm to open-ended generative tasks, such as creative writing or dialogue, where evaluation is subjective, remains a significant hurdle."

**Performance Ceiling:** While iterative improvements occur, gains plateau—suggesting fundamental limits in the co-evolutionary dynamics without external validation mechanisms.

**Pseudo-Label Reliability:** As problems increase in difficulty, majority voting becomes less reliable, undermining training signal quality.

## 9) Curriculum Adaptation Mechanism

Curriculum adaptation operates through the **uncertainty reward function's dynamic calibration**:

Each iteration, the Challenger targets questions where p̂ ≈ 0.5 (50% Solver success rate). As the Solver improves, previously challenging questions become easier, causing their uncertainty reward to decrease. Simultaneously, the Challenger must generate harder problems to maintain the 50% target, creating natural progression.

The filtering mechanism reinforces this by discarding questions outside the [0.25, 0.75] correctness band, ensuring the training set remains calibrated to current capabilities.

**Observable Pattern:** Table 4 demonstrates this—evaluating a fixed Solver (Iter 1) against evolved question sets shows declining performance (59.0% → 47.0%), confirming the Challenger successfully increases problem difficulty each iteration.

## 10) Comparison to Process Reward Models (PRM)

**No direct PRM comparison provided.** The paper does not discuss Process Reward Models. Instead, it focuses on outcome-based verification through majority voting and RLVR (Reinforcement Learning with Verifiable Rewards). 

The framework uses **binary correctness signals** (final answer matches pseudo-label), not step-wise process verification. This distinguishes R-Zero from PRM approaches, which would evaluate intermediate reasoning steps. The authors note their approach provides "rule-based verifier" functionality for domains with deterministic correctness criteria, which differs fundamentally from PRM's trajectory-level evaluation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11f2c80f-5574-4e08-9592-d7284bf39f5a",
  "isSidechain": true,
  "promptId": "c7973f03-d621-459f-9572-b6284262bbbb",
  "agentId": "a629672d73d886a3c",
  "type": "user",
  "uuid": "0cd6ed13-a96f-4d42-b015-af042aacd15a",
  "sourceToolAssistantUUID": "11f2c80f-5574-4e08-9592-d7284bf39f5a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-28T05:08:51.939Z_

Good, I have extensive information. Let me now fetch the OpenReview page for reviewer comments and additional details, and also check the GitHub repository for implementation specifics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cd6ed13-a96f-4d42-b015-af042aacd15a",
  "isSidechain": true,
  "agentId": "a629672d73d886a3c",
  "requestId": "req_011CbUPWc3cVE4VET9sHNxUV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b01e0c07-7e83-43f4-b521-83ff2c344f4d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JFgngbdRxHJUPerCFPH9WN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 366,
      "cache_creation_input_tokens": 3847,
      "cache_read_input_tokens": 12124,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3847,
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

_source line 22 · 2026-05-28T05:08:53.843Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YRNaT3GBPV7BrR1qBroBGx`</summary>

```json
{
  "url": "https://openreview.net/forum?id=96apU6YzSO",
  "prompt": "Extract all reviewer comments, scores, strengths, weaknesses, and the meta-review for this paper. Include all discussion points and any author rebuttals."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b01e0c07-7e83-43f4-b521-83ff2c344f4d",
  "isSidechain": true,
  "agentId": "a629672d73d886a3c",
  "requestId": "req_011CbUPWc3cVE4VET9sHNxUV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a44c4c23-fe48-4523-9a90-a204ff4b1c1e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JFgngbdRxHJUPerCFPH9WN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 366,
      "cache_creation_input_tokens": 3847,
      "cache_read_input_tokens": 12124,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3847,
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

_source line 23 · 2026-05-28T05:08:54.574Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01K7T3L4s6B2yQExmakrUQf7`</summary>

```json
{
  "url": "https://github.com/Chengsong-Huang/R-Zero",
  "prompt": "Extract all implementation details including: training scripts, hyperparameters, model configurations, data generation pipeline, and any details about the Challenger and Solver training process not in the paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a44c4c23-fe48-4523-9a90-a204ff4b1c1e",
  "isSidechain": true,
  "agentId": "a629672d73d886a3c",
  "requestId": "req_011CbUPWc3cVE4VET9sHNxUV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f6a5252c-b031-4474-90f2-1dde6d60950c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JFgngbdRxHJUPerCFPH9WN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 366,
      "cache_creation_input_tokens": 3847,
      "cache_read_input_tokens": 12124,
      "output_tokens": 260,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3847
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 366,
          "output_tokens": 260,
          "cache_read_input_tokens": 12124,
          "cache_creation_input_tokens": 3847,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3847,
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

_source line 24 · 2026-05-28T05:08:58.120Z_

<details><summary>↩ Tool result · `toolu_01YRNaT3GBPV7BrR1qBroBGx`</summary>

```text
# R-Zero Paper Review Information

Based on the provided web page content, I cannot extract reviewer comments, scores, strengths, weaknesses, or meta-reviews. 

The page displays only the paper's **title, abstract, and metadata**:

- **Paper:** "R-Zero: Self-Evolving Reasoning LLM from Zero Data"
- **Authors:** Chengsong Huang, Wenhao Yu, and colleagues
- **Venue:** ICLR 2026 Conference
- **Status:** Published January 26, 2026; Last modified April 11, 2026
- **Classification:** Poster presentation

The abstract indicates the work proposes "a data-free method to improve LLM reasoning ability" through a "Challenger-Solver" co-evolution framework, achieving notable performance gains on reasoning benchmarks.

**What's Missing:** The provided content does not include the review section, discussion threads, author rebuttals, or scoring information typically found on OpenReview papers. To access this information, you would need to visit the full OpenReview page directly or request additional page content that contains the peer review materials.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a44c4c23-fe48-4523-9a90-a204ff4b1c1e",
  "isSidechain": true,
  "promptId": "c7973f03-d621-459f-9572-b6284262bbbb",
  "agentId": "a629672d73d886a3c",
  "type": "user",
  "uuid": "96c81798-a176-4fe7-81d6-016ecbed21b1",
  "sourceToolAssistantUUID": "a44c4c23-fe48-4523-9a90-a204ff4b1c1e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-28T05:09:02.193Z_

<details><summary>↩ Tool result · `toolu_01K7T3L4s6B2yQExmakrUQf7`</summary>

```text
# R-Zero Implementation Details

Based on the GitHub repository content provided, here are the implementation details available:

## Training Architecture

The framework implements a **co-evolutionary loop** with two model instances:

- **Challenger**: "Its job is to probe the Solver for weaknesses and generate challenging problems that are right at the edge of its capabilities."
- **Solver**: "Its goal is to continuously improve by solving the increasingly difficult tasks posed by the Challenger."

## Key Training Techniques

The system uses "majority voting for pseudo-labels and relative policy optimization to guide the learning."

## Hardware Requirements

"All our experiments were conducted on an 8-GPU server, using models that can run on a single GPU (e.g., 4B or 8B)."

## Data Pipeline & Storage

The framework organizes outputs into these directories:
- `evaluation`
- `models`
- `generated_question`
- `temp_results`

All artifacts save to the `STORAGE_PATH` environment variable, with datasets also uploaded to Hugging Face.

## Known Issues

The developers note: "This is likely due to a strange bug in the math_verify lib, which can cause an infinite loop when processing certain answers." They added timeout controls as mitigation.

## Dependencies & Base Framework

The implementation is "directly based on the great work of EasyR1" and references evaluation methods from General-Reasoner.

The actual hyperparameters, detailed training scripts, and specific model configurations are not detailed in this README—those would require examining the actual code files in the repository.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6a5252c-b031-4474-90f2-1dde6d60950c",
  "isSidechain": true,
  "promptId": "c7973f03-d621-459f-9572-b6284262bbbb",
  "agentId": "a629672d73d886a3c",
  "type": "user",
  "uuid": "240445e9-fe54-4ca3-a17f-b26da01f5a8c",
  "sourceToolAssistantUUID": "f6a5252c-b031-4474-90f2-1dde6d60950c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-28T05:09:04.950Z_

Let me search for a few more specific details -- the theoretical justification and any comparison to related curriculum learning approaches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "240445e9-fe54-4ca3-a17f-b26da01f5a8c",
  "isSidechain": true,
  "agentId": "a629672d73d886a3c",
  "requestId": "req_011CbUPXanF6nBCFGTYL8MDo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "730d8129-5c27-4444-b009-39378be78ee3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016JCTU13aw6b8SZN8AcC45s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1281,
      "cache_read_input_tokens": 15971,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1281,
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

_source line 27 · 2026-05-28T05:09:05.427Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012gkNCsBh4myBSfdSsGMaxH`</summary>

```json
{
  "query": "R-Zero paper theoretical justification uncertainty reward KL divergence challenger training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "730d8129-5c27-4444-b009-39378be78ee3",
  "isSidechain": true,
  "agentId": "a629672d73d886a3c",
  "requestId": "req_011CbUPXanF6nBCFGTYL8MDo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f6b72510-2c6f-4a57-9277-f677baa0411b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016JCTU13aw6b8SZN8AcC45s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1281,
      "cache_read_input_tokens": 15971,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1281,
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

_source line 28 · 2026-05-28T05:09:05.924Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NpXsGRL7H92raxmiQrj5Kf`</summary>

```json
{
  "query": "\"R-Zero\" comparison \"process reward model\" PRM curriculum learning math reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6b72510-2c6f-4a57-9277-f677baa0411b",
  "isSidechain": true,
  "agentId": "a629672d73d886a3c",
  "requestId": "req_011CbUPXanF6nBCFGTYL8MDo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d2b45da2-3dd5-4aba-82ed-308b6e256ff5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016JCTU13aw6b8SZN8AcC45s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1281,
      "cache_read_input_tokens": 15971,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1281
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 141,
          "cache_read_input_tokens": 15971,
          "cache_creation_input_tokens": 1281,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1281,
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

_source line 29 · 2026-05-28T05:09:13.583Z_

<details><summary>↩ Tool result · `toolu_012gkNCsBh4myBSfdSsGMaxH`</summary>

```text
Web search results for query: "R-Zero paper theoretical justification uncertainty reward KL divergence challenger training"

Links: [{"title":"R-Zero: Self-Evolving Reasoning LLM from Zero Data","url":"https://arxiv.org/html/2508.05004v1"},{"title":"R-Zero: SELF-EVOLVING REASONING LLM","url":"https://arxiv.org/pdf/2508.05004"},{"title":"R-Zero: A Method For Training Reasoning LLMs With Zero Data Is Here","url":"https://www.intoai.pub/p/r-zero"},{"title":"The Choice of Divergence: A Neglected Key to Mitigating Diversity Collapse in Reinforcement Learning with Verifiable Reward","url":"https://arxiv.org/html/2509.07430v1"},{"title":"The Choice of Divergence: A Neglected Key to Mitigating Diversity Collapse in Reinforcement Learning with Verifiable Reward","url":"https://arxiv.org/pdf/2509.07430"},{"title":"Catastrophic Goodhart: regularizing RLHF with KL divergence does not   mitigate heavy-tailed reward misspecification","url":"https://arxiv.org/pdf/2407.14503"}]

Based on the search results, here's what I found about the R-Zero paper's theoretical justification for uncertainty reward and KL divergence in challenger training:

## Theoretical Justification for Uncertainty Reward

The analysis is grounded in recent work that formally establishes that the most efficient training occurs when a learner is exposed to tasks at the frontier of its capabilities. The uncertainty reward function is proportional to 1-2|p̂(x;Sφ)-1/2|, which is maximized when the Solver's success probability is 50%.

## KL Divergence Connection

The KL divergence between the Solver and optimal policy (DKL(Sφ||S*)) is lower-bounded by the variance of the Solver's reward. For binary reward signals, this lower bound is maximized precisely when the success probability equals 0.5.

## KL Divergence in Training

The policy is updated using a clipped surrogate objective regularized by a KL-divergence penalty to constrain policy drift. This applies to both the Solver and Challenger components of the framework.

The core insight is that by targeting tasks where the Solver has approximately 50% success rate—representing the frontier of its capabilities—the framework maximizes the learning potential as quantified by KL divergence to the optimal policy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6b72510-2c6f-4a57-9277-f677baa0411b",
  "isSidechain": true,
  "promptId": "c7973f03-d621-459f-9572-b6284262bbbb",
  "agentId": "a629672d73d886a3c",
  "type": "user",
  "uuid": "3d1ab122-1628-4784-b207-c4cc8fb3c586",
  "sourceToolAssistantUUID": "f6b72510-2c6f-4a57-9277-f677baa0411b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-28T05:09:19.564Z_

<details><summary>↩ Tool result · `toolu_01NpXsGRL7H92raxmiQrj5Kf`</summary>

```text
Web search results for query: ""R-Zero" comparison "process reward model" PRM curriculum learning math reasoning"

Links: [{"title":"R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://arxiv.org/html/2503.21295v1"},{"title":"R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://arxiv.org/pdf/2503.21295"},{"title":"Good Learners Think Their Thinking: Generative PRM Makes Large Reasoning Model More Efficient Math Learner","url":"https://arxiv.org/pdf/2507.23317"},{"title":"More Bang for the Buck: Process Reward Modeling with Entropy-Driven Uncertainty","url":"https://arxiv.org/pdf/2503.22233"},{"title":"Unlocking Multimodal Mathematical Reasoning via Process Reward Model","url":"https://arxiv.org/pdf/2501.04686"},{"title":"R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://github.com/NJUNLP/R-PRM"},{"title":"[2503.21295] R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://arxiv.org/abs/2503.21295"},{"title":"[Literature Review] R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://www.themoonlight.io/en/review/r-prm-reasoning-driven-process-reward-modeling"},{"title":"Adversarial Training for Process Reward Models","url":"https://arxiv.org/pdf/2511.22888"},{"title":"The Lessons of Developing Process Reward Models in Mathematical Reasoning","url":"https://arxiv.org/pdf/2501.07301"}]

The search results don't show information about "R-Zero" specifically. The results primarily discuss "R-PRM" (Reasoning-Driven Process Reward Modeling) and other PRM-related research. Let me search more specifically for R-Zero:

Links: [{"title":"R-Zero: Self-Evolving Reasoning LLM from Zero Data","url":"https://chengsong-huang.github.io/R-Zero.github.io/"},{"title":"R-Zero: Self-Evolving Reasoning LLM from Zero Data | OpenReview","url":"https://openreview.net/forum?id=96apU6YzSO"},{"title":"R-Zero: SELF-EVOLVING REASONING LLM","url":"https://arxiv.org/pdf/2508.05004"},{"title":"R-Zero: Self-Evolving Reasoning LLM from Zero Data","url":"https://arxiv.org/html/2508.05004v1"},{"title":"Paper page - R-Zero: Self-Evolving Reasoning LLM from Zero Data","url":"https://huggingface.co/papers/2508.05004"},{"title":"GitHub - Chengsong-Huang/R-Zero: [ICLR2026] codes for R-Zero: Self-Evolving Reasoning LLM from Zero Data (https://www.arxiv.org/pdf/2508.05004) · GitHub","url":"https://github.com/Chengsong-Huang/R-Zero"},{"title":"[2508.05004] R-Zero: Self-Evolving Reasoning LLM from Zero Data","url":"https://arxiv.org/abs/2508.05004"},{"title":"R-Zero: A Method For Training Reasoning LLMs With Zero Data Is Here","url":"https://www.intoai.pub/p/r-zero"},{"title":"R-Zero : Train LLMs with No data. R-Zero: Self-Evolving Reasoning LLM… | by Mehul Gupta | Data Science in Your Pocket | Medium","url":"https://medium.com/data-science-in-your-pocket/r-zero-train-llms-with-no-data-4d5c43cb454c"}]

Based on the search results, I can now provide you with comprehensive information about R-Zero and how it relates to process reward models and curriculum learning:

## R-Zero Overview

R-Zero is a fully autonomous framework that generates its own training data from scratch. Starting from a single base LLM, R-Zero initializes two independent models with distinct roles – a Challenger and a Solver. These models are optimized separately and co-evolve through interaction: the Challenger is rewarded for proposing tasks near the edge of the Solver's capability, and the Solver is rewarded for solving increasingly challenging tasks posed by the Challenger.

## Curriculum Learning Approach

This process yields a targeted, self-improving curriculum without any pre-existing tasks and labels. The framework operates without traditional human-curated data, making it fundamentally different from conventional training approaches.

## Comparison with Process Reward Models (PRMs)

While the search results show R-Zero takes a different approach, there's a distinction: Process Reward Models (PRMs) have been proposed to improve models' reasoning ability by evaluating each reasoning step in a fine-grained manner, identifying and mitigating process errors, while also exhibiting stronger generalization capabilities. 

R-Zero, by contrast, focuses on autonomously generating curriculum through a co-evolutionary challenge-solution dynamic rather than using external reward models for step-level evaluation.

## Performance on Math Reasoning

R-Zero substantially improves reasoning capability across different backbone LLMs, e.g., boosting the Qwen3-4B-Base by +6.49 on math-reasoning benchmarks and +7.54 on general-domain reasoning benchmarks. The reasoning skills learned through math-focused questions can generalize to complex general-domain tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2b45da2-3dd5-4aba-82ed-308b6e256ff5",
  "isSidechain": true,
  "promptId": "c7973f03-d621-459f-9572-b6284262bbbb",
  "agentId": "a629672d73d886a3c",
  "type": "user",
  "uuid": "a2d6fe30-2baf-41e5-985b-36c46805995e",
  "sourceToolAssistantUUID": "d2b45da2-3dd5-4aba-82ed-308b6e256ff5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-28T05:09:22.943Z_

Let me also fetch the blog post for any additional analysis, and search for how R-Zero relates to the specific idea of PRM-diagnosed curriculum.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2d6fe30-2baf-41e5-985b-36c46805995e",
  "isSidechain": true,
  "agentId": "a629672d73d886a3c",
  "requestId": "req_011CbUPYs4Jq8U16cZtbSPBt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e079cb12-aa63-41ea-8a5f-6ec31fa746c1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VeQGEKKiDUpgRY8KzKFKfk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2187,
      "cache_read_input_tokens": 17252,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2187,
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

_source line 32 · 2026-05-28T05:09:24.416Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011YvbRdBB1nyFrXoPAEn6Q3`</summary>

```json
{
  "url": "https://www.intoai.pub/p/r-zero",
  "prompt": "Extract all details about R-Zero's method, results, limitations, and analysis. Include any discussion of related work, comparisons to other methods, and insights about the co-evolutionary dynamics."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e079cb12-aa63-41ea-8a5f-6ec31fa746c1",
  "isSidechain": true,
  "agentId": "a629672d73d886a3c",
  "requestId": "req_011CbUPYs4Jq8U16cZtbSPBt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1eb959f8-30e1-44fe-8a68-26b0e93ad1bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VeQGEKKiDUpgRY8KzKFKfk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2187,
      "cache_read_input_tokens": 17252,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2187,
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

_source line 33 · 2026-05-28T05:09:25.004Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018v5nXRrrg9DghGNqHNsrJx`</summary>

```json
{
  "query": "R-Zero self-evolving related work STILL AbsoluteZero self-play curriculum generation reasoning LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1eb959f8-30e1-44fe-8a68-26b0e93ad1bb",
  "isSidechain": true,
  "agentId": "a629672d73d886a3c",
  "requestId": "req_011CbUPYs4Jq8U16cZtbSPBt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d3f3e4ea-e122-4179-8dad-ad31317c282d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VeQGEKKiDUpgRY8KzKFKfk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2187,
      "cache_read_input_tokens": 17252,
      "output_tokens": 213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2187
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 213,
          "cache_read_input_tokens": 17252,
          "cache_creation_input_tokens": 2187,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2187,
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

_source line 34 · 2026-05-28T05:09:31.989Z_

<details><summary>↩ Tool result · `toolu_011YvbRdBB1nyFrXoPAEn6Q3`</summary>

```text
# R-Zero: Self-Evolving LLM Framework Analysis

## Core Method

R-Zero employs a **self-play approach** where two versions of a single LLM take distinct roles:

- **Challenger (Q(θ))**: Generates mathematical problems targeting the edge of solver capability
- **Solver (S(Φ))**: Attempts to solve generated problems

The system operates autonomously without external training data or human annotations, representing what researchers call "label-free reinforcement learning."

## Key Technical Components

**Challenger Training:**
The framework uses an "uncertainty reward" that peaks when the Solver achieves approximately 50% accuracy on generated questions—the optimal difficulty sweet spot. A repetition penalty prevents the Challenger from generating similar problems repeatedly. The system enforces format validation through an "incorrect format penalty" requiring proper XML-style tags.

**Dataset Creation:**
Questions are filtered based on the criterion: "keep only those questions where the Solver's accuracy is close to 50%, within a margin of δ." This filtering discards overly easy or difficult problems.

**Solver Enhancement:**
The Solver receives binary rewards (correct/incorrect) and undergoes fine-tuning using GRPO loss, which includes clipping and KL divergence penalties to maintain stability.

## Performance Results

Testing on Qwen and OctoThinker model families showed:
- Consistent performance gains across mathematical benchmarks (MATH, GSM8K, AIME)
- Largest improvements occurred in initial iterations
- Transfer effects: Mathematical training improved general-domain reasoning on benchmarks like MMLU

## Limitations & Scope

The framework currently focuses on domains where correctness can be objectively verified (mathematical reasoning). Expanding toward open-ended reasoning tasks remains a future challenge, as verifiers for such problems don't currently exist.

## Related Work Context

R-Zero builds upon self-play methodologies and label-free RL approaches, advancing beyond previous self-challenging methods that required external verifiers for task validation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1eb959f8-30e1-44fe-8a68-26b0e93ad1bb",
  "isSidechain": true,
  "promptId": "c7973f03-d621-459f-9572-b6284262bbbb",
  "agentId": "a629672d73d886a3c",
  "type": "user",
  "uuid": "7a0b3524-673d-4603-b1ca-4145d9de9306",
  "sourceToolAssistantUUID": "1eb959f8-30e1-44fe-8a68-26b0e93ad1bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-28T05:09:35.083Z_

<details><summary>↩ Tool result · `toolu_018v5nXRrrg9DghGNqHNsrJx`</summary>

```text
Web search results for query: "R-Zero self-evolving related work STILL AbsoluteZero self-play curriculum generation reasoning LLM"

Links: [{"title":"R-Zero: Self-Evolving Reasoning LLM from Zero Data","url":"https://arxiv.org/html/2508.05004v1"},{"title":"(PDF) Absolute Zero: Reinforced Self-play Reasoning with Zero Data","url":"https://www.researchgate.net/publication/391493002_Absolute_Zero_Reinforced_Self-play_Reasoning_with_Zero_Data"},{"title":"R-Zero: Self-Evolving Reasoning LLM from Zero Data | OpenReview","url":"https://openreview.net/forum?id=96apU6YzSO"},{"title":"R-Zero: SELF-EVOLVING REASONING LLM","url":"https://arxiv.org/pdf/2508.05004"},{"title":"[2508.05004] R-Zero: Self-Evolving Reasoning LLM from Zero Data","url":"https://arxiv.org/abs/2508.05004"},{"title":"R-Zero: Self-Evolving Reasoning LLM from Zero Data","url":"https://chengsong-huang.github.io/R-Zero.github.io/"},{"title":"[2505.03335] Absolute Zero: Reinforced Self-play Reasoning with Zero Data","url":"https://arxiv.org/abs/2505.03335"},{"title":"Paper page - Absolute Zero: Reinforced Self-play Reasoning with Zero Data","url":"https://huggingface.co/papers/2505.03335"},{"title":"Absolute Zero: Reinforced Self-play Reasoning with Zero Data | OpenReview","url":"https://openreview.net/forum?id=neZSGqhxDa"}]

Based on the search results, I found information about both R-Zero and Absolute Zero, two related frameworks for self-evolving reasoning in large language models:

## R-Zero: Self-Evolving Reasoning LLM

R-Zero is a fully autonomous framework that generates its own training data from scratch. It initializes two independent models with distinct roles, a Challenger and a Solver, which are optimized separately and co-evolve through interaction: the Challenger is rewarded for proposing tasks near the edge of the Solver capability, and the Solver is rewarded for solving increasingly challenging tasks posed by the Challenger. This process yields a targeted, self-improving curriculum without any pre-existing tasks and labels.

The work distinguishes itself by extending this paradigm to general reasoning domains that lack verifiable environments, instead learning from a reward signal derived from the model's own internal consistency.

## Absolute Zero: Reinforced Self-Play Reasoning

Absolute Zero Reasoner (AZR) is a system that self-evolves its training curriculum and reasoning ability by using a code executor to both validate proposed code reasoning tasks and verify answers, serving as an unified source of verifiable reward to guide open-ended yet grounded learning. Within this self-play training paradigm, the model learns from three distinct type of coding tasks, which corresponding to three fundamental modes of reasoning: abduction, deduction and induction.

Both frameworks address the limitation that existing methods for training self-evolving LLMs still rely heavily on vast human-curated tasks and labels, enabling models to generate and learn from their own training experiences.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d3f3e4ea-e122-4179-8dad-ad31317c282d",
  "isSidechain": true,
  "promptId": "c7973f03-d621-459f-9572-b6284262bbbb",
  "agentId": "a629672d73d886a3c",
  "type": "user",
  "uuid": "2dc01404-808c-450c-a87b-e16bc465820f",
  "sourceToolAssistantUUID": "d3f3e4ea-e122-4179-8dad-ad31317c282d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-28T05:09:38.394Z_

Now I have comprehensive information. Let me also do one more targeted search for how R-Zero compares to PRM-based approaches for curriculum design specifically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2dc01404-808c-450c-a87b-e16bc465820f",
  "isSidechain": true,
  "agentId": "a629672d73d886a3c",
  "requestId": "req_011CbUPa1NeUmRfgPv5DA4wm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9995ea8b-b6f1-49bb-8754-a51bad4c09bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YBPPxs3iymHA3kNNfEvZNA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1531,
      "cache_read_input_tokens": 19439,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1531,
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

_source line 37 · 2026-05-28T05:09:39.089Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B1XbHoTguvAnB66hdL28hT`</summary>

```json
{
  "query": "PRM error taxonomy adaptive curriculum generator verifier co-training math reasoning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9995ea8b-b6f1-49bb-8754-a51bad4c09bb",
  "isSidechain": true,
  "agentId": "a629672d73d886a3c",
  "requestId": "req_011CbUPa1NeUmRfgPv5DA4wm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fdee7dcd-c075-41fc-8620-ad64389e9b3c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YBPPxs3iymHA3kNNfEvZNA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1531,
      "cache_read_input_tokens": 19439,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1531,
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

### Tool result

_source line 38 · 2026-05-28T05:09:49.185Z_

<details><summary>↩ Tool result · `toolu_01B1XbHoTguvAnB66hdL28hT`</summary>

```text
Web search results for query: "PRM error taxonomy adaptive curriculum generator verifier co-training math reasoning 2025 2026"

Links: [{"title":"Adversarial Training for Process Reward Models","url":"https://arxiv.org/html/2511.22888"},{"title":"A Survey on Verifying Reasoning Chains Generated by ...","url":"https://hal.science/hal-05448955v1/document"},{"title":"GM-PRM: A Generative Multimodal Process Reward Model for Multimodal Mathematical Reasoning","url":"https://arxiv.org/pdf/2508.04088"},{"title":"Adversarial Training for Process Reward Models","url":"https://arxiv.org/pdf/2511.22888"},{"title":"Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision","url":"https://arxiv.org/pdf/2505.19706"},{"title":"Bidirectional Curriculum Generation: A Multi-Agent Framework for Data-Efficient Mathematical Reasoning","url":"https://arxiv.org/pdf/2603.05120"},{"title":"enhancing llm reasoning with adversarial reinforce","url":"https://arxiv.org/pdf/2512.16917"},{"title":"Good Learners Think Their Thinking: Generative PRM Makes Large Reasoning Model More Efficient Math Learner","url":"https://arxiv.org/pdf/2507.23317"}]

Based on the search results, I found several relevant recent papers on Process Reward Models (PRMs) and related techniques for mathematical reasoning. Here are the key findings:

## Adversarial Training for Process Reward Models (APRM)

A Generator learns to produce reasoning errors to deceive a PRM, while the PRM concurrently learns to detect them, yielding progressively harder negatives that improve robustness and generalization to novel errors without requiring manual step-level labels. This yields a dynamic curriculum of negatives, continuously adapting to the PRM's blind spots rather than relying on fixed heuristics.

## Error Taxonomy and Generative Models

PathFinder-PRM is a generative PRM that takes error types into account when scoring mathematical reasoning. Additionally, some models deconstruct steps into three critical aspects: step intent, image alignment, and reasoning logic, and are trained to identify errors and generate refined, corrected versions of incorrect steps.

## Curriculum Learning Approaches

A Bidirectional Curriculum Generation framework uses a multi-agent ecosystem to establish a closed feedback loop, dynamically generating data by either complicating problems or simplifying them to repair specific reasoning failures.

These papers from 2025-2026 represent recent advances in combining error taxonomy, adaptive curriculum generation, verifier models, and co-training approaches for improving mathematical reasoning with language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fdee7dcd-c075-41fc-8620-ad64389e9b3c",
  "isSidechain": true,
  "promptId": "c7973f03-d621-459f-9572-b6284262bbbb",
  "agentId": "a629672d73d886a3c",
  "type": "user",
  "uuid": "7bd10e4c-817e-4783-bb51-899c2f3a59a3",
  "sourceToolAssistantUUID": "fdee7dcd-c075-41fc-8620-ad64389e9b3c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-28T05:09:52.395Z_

I now have a thorough picture. Let me also quickly look at the Adversarial PRM paper and the error-taxonomy paper since they are directly relevant to the comparison you need.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bd10e4c-817e-4783-bb51-899c2f3a59a3",
  "isSidechain": true,
  "agentId": "a629672d73d886a3c",
  "requestId": "req_011CbUPb3h5SYcNeG916Wyy2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "73c2330e-93d2-4f48-a780-94a83a77472e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8rSGus1VkhaNgg3efLjty",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 878,
      "cache_read_input_tokens": 20970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 878,
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

_source line 40 · 2026-05-28T05:09:53.344Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018iPfdQhSW5Sqxuisf9SpNp`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.22888",
  "prompt": "Extract the title, authors, and abstract of this adversarial PRM paper. How does it compare to R-Zero's approach?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73c2330e-93d2-4f48-a780-94a83a77472e",
  "isSidechain": true,
  "agentId": "a629672d73d886a3c",
  "requestId": "req_011CbUPb3h5SYcNeG916Wyy2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "321bd1ee-203c-4d1c-b0c1-bf6fd476566d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8rSGus1VkhaNgg3efLjty",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 878,
      "cache_read_input_tokens": 20970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 878,
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

_source line 41 · 2026-05-28T05:09:53.918Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FdTERaxvY8AWdJL9vBdXCv`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.19706",
  "prompt": "Extract the title, authors, abstract, and key method details of this error-typing PRM paper. How does it use error taxonomy for process reward modeling?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "321bd1ee-203c-4d1c-b0c1-bf6fd476566d",
  "isSidechain": true,
  "agentId": "a629672d73d886a3c",
  "requestId": "req_011CbUPb3h5SYcNeG916Wyy2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b1b3b23-6211-4f33-872b-89527d91f036",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8rSGus1VkhaNgg3efLjty",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 878,
      "cache_read_input_tokens": 20970,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 878
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 247,
          "cache_read_input_tokens": 20970,
          "cache_creation_input_tokens": 878,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 878,
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

_source line 42 · 2026-05-28T05:09:57.191Z_

<details><summary>↩ Tool result · `toolu_018iPfdQhSW5Sqxuisf9SpNp`</summary>

```text
# Adversarial Training for Process Reward Models

**Title:** Adversarial Training for Process Reward Models

**Authors:** Gurusha Juneja, Deepak Nathani, William Yang Wang

**Abstract:** The paper introduces a framework where "a Generator ($G$) learns to produce reasoning errors to deceive a PRM ($R$), while $R$ concurrently learns to detect them." This adversarial interaction creates progressively harder training examples, enabling improved robustness without manual step-level annotations. The approach achieves +3.4 percentage point gains on mathematical reasoning benchmarks and +5.3 pp on out-of-distribution tasks.

## Comparison to R-Zero's Approach

I cannot provide a meaningful comparison to R-Zero's approach based on the provided content. The arXiv page excerpt contains no references to R-Zero or discussion of related methodologies. To address this comparison accurately, I would need access to either R-Zero's publication or sections of this paper that discuss related work and competing approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "321bd1ee-203c-4d1c-b0c1-bf6fd476566d",
  "isSidechain": true,
  "promptId": "c7973f03-d621-459f-9572-b6284262bbbb",
  "agentId": "a629672d73d886a3c",
  "type": "user",
  "uuid": "1936b272-c25b-4eef-a4a5-fce0f9574ced",
  "sourceToolAssistantUUID": "321bd1ee-203c-4d1c-b0c1-bf6fd476566d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-28T05:10:02.249Z_

<details><summary>↩ Tool result · `toolu_01FdTERaxvY8AWdJL9vBdXCv`</summary>

```text
# PathFinder-PRM: Error-Typing for Process Reward Models

## Title
"Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision"

## Authors
Tej Deep Pala, Panshul Sharma, Amir Zadeh, Chuan Li, and Soujanya Poria

## Abstract Summary
The paper addresses hallucination issues in LLMs during mathematical reasoning tasks. While outcome reward models only check final answers, their approach evaluates each intermediate step. The key innovation is a novel system that uses fine-grained error classification to improve step-level scoring.

## Key Method Details

**Core Approach:**
The model first categorizes two error types—mathematical errors and consistency issues—at each reasoning step, then synthesizes these signals to determine step correctness. This decoupled approach enables more nuanced evaluation than traditional binary correctness judgments.

**Training Data:**
The researchers enriched existing datasets with "three-dimensional step-level labels," creating a 400K-sample training corpus from human-annotated sources and model traces.

**Results:**
On PRMBench, their system achieved a score of 67.7, surpassing the previous benchmark of 65.5 while requiring substantially less training data, demonstrating improved efficiency in error detection and mathematical reasoning guidance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b1b3b23-6211-4f33-872b-89527d91f036",
  "isSidechain": true,
  "promptId": "c7973f03-d621-459f-9572-b6284262bbbb",
  "agentId": "a629672d73d886a3c",
  "type": "user",
  "uuid": "5c37a271-fc86-4fb1-9552-cb3bd859dc04",
  "sourceToolAssistantUUID": "0b1b3b23-6211-4f33-872b-89527d91f036",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-28T05:11:16.519Z_

I now have all the information needed for a comprehensive report. Here is the full analysis:

---

## R-Zero: Self-Evolving Reasoning LLM from Zero Data -- Deep Research Report

### Full Citation

**Title:** R-Zero: Self-Evolving Reasoning LLM from Zero Data

**Authors:** Chengsong Huang, Wenhao Yu, Xiaoyang Wang, Hongming Zhang, Zongxia Li, Ruosen Li, Jiaxin Huang, Haitao Mi, Dong Yu

**Affiliations:** Tencent AI Seattle Lab, Washington University in St. Louis, University of Maryland, University of Texas at Dallas

**Venue:** ICLR 2026 (Poster), published January 26, 2026. arXiv: 2508.05004

---

### Core Method: Challenger-Solver Co-Evolution

R-Zero starts from a single base LLM and forks it into two independent models:

- **Challenger (Q_theta):** Generates math problems calibrated to the Solver's current capability frontier.
- **Solver (S_phi):** Attempts to solve the Challenger's problems and improves through GRPO.

The models alternate training in a frozen-partner scheme: when one trains, the other is frozen. This creates a co-evolutionary dynamic where increasing Solver skill forces the Challenger to generate harder problems, and harder problems push the Solver to improve further.

---

### What Drives Curriculum Adaptation: The Uncertainty Reward

The Challenger's reward is explicitly **uncertainty-based**. For a generated question x, the framework samples m=10 responses from the frozen Solver, computes empirical accuracy p_hat(x; S_phi) via majority vote, and applies:

**r_uncertainty(x; phi) = 1 - 2|p_hat(x; S_phi) - 0.5|**

This peaks at p_hat = 0.5 (50% Solver success rate), directly targeting the "zone of proximal development" -- problems the Solver can sometimes but not always solve.

**Theoretical justification:** The authors prove a connection via KL divergence bounds: D_KL(S_phi || S*) is lower-bounded by a quantity proportional to reward variance, which for binary rewards is maximized precisely when p_hat = 0.5. So targeting 50% success maximizes the information-theoretic learning potential.

**Additional reward components:**
- **Repetition penalty:** Uses BLEU-based agglomerative clustering to penalize duplicate/similar questions. r_rep(x_i) = lambda * |C_k| / B (cluster size / batch size, threshold tau_BLEU = 0.5).
- **Format penalty:** Questions lacking proper XML tags get reward 0.

**Composite reward:** r_i = max(0, r_uncertainty(x_i; phi) - r_rep(x_i))

---

### The Full Training Loop (Per Iteration)

**Step 1 -- Challenger Training:**
- Train Q_theta via GRPO using the frozen Solver S_phi
- Generate N=8,000 candidate questions
- Score each with the composite uncertainty + diversity reward
- Max 5 training steps, 4 rollouts per step
- KL regularization beta = 10^-2

**Step 2 -- Dataset Construction (Filtering):**
- For each candidate question, sample m=10 Solver answers
- Determine pseudo-label y_hat via majority vote
- Retain only questions where 3-7 out of 10 answers match the pseudo-label (i.e., |p_hat - 0.5| <= delta, with delta = 0.25)
- This discards too-easy problems (near 100% accuracy) AND too-hard/ill-posed problems (near 0% accuracy or ambiguous)

**Step 3 -- Solver Training:**
- Train S_phi via GRPO on the filtered dataset
- Binary reward: 1 if answer matches pseudo-label, 0 otherwise
- Global batch size 128, learning rate 1e-6
- Max 15 training steps, 5 rollouts per step
- KL penalty lambda_KL = 1e-2

**Step 4 -- Repeat** for multiple iterations (paper reports 3 iterations).

---

### Key Results

**Mathematical Reasoning (7 benchmarks: AMC, Minerva, MATH-500, GSM8K, Olympiad-Bench, AIME-2024, AIME-2025):**

| Model | Base | After 3 Iterations | Gain |
|---|---|---|---|
| Qwen3-4B-Base | 42.58 | 49.07 | **+6.49** |
| Qwen3-8B-Base | 49.18 | 54.69 | +5.51 |
| OctoThinker-3B | 26.64 | 29.32 | +2.68 |
| OctoThinker-8B | 36.41 | 38.52 | +2.11 |

**General Domain Transfer (MMLU-Pro, SuperGPQA, BBEH):**

| Model | Base | After 3 Iterations | Gain |
|---|---|---|---|
| Qwen3-4B-Base | 27.10 | 34.64 | **+7.54** |
| Qwen3-8B-Base | 34.49 | 38.73 | +4.24 |

**Key finding:** Math-focused training generalizes to non-math reasoning tasks, with even larger gains on general benchmarks than on math for Qwen3-4B.

**Mid-training utility:** R-Zero can serve as a mid-training method -- models first improved by R-Zero achieve higher performance when subsequently fine-tuned on labeled data.

**Ablation Results (Qwen3-4B-Base, 1 iteration):**

| Variant | Math AVG | General AVG |
|---|---|---|
| Full R-Zero | 48.06 | 30.41 |
| w/o RL-Challenger (random questions) | 44.36 (-3.7) | 26.32 (-4.1) |
| w/o Repetition Penalty | 45.76 (-2.3) | 27.56 (-2.9) |
| w/o Filtering | 47.35 (-0.7) | 24.26 (-6.1) |

The RL-trained Challenger is the most critical component. Removing filtering is catastrophic for general-domain transfer (-6.1 points).

---

### Is It Uncertainty-Based? How Does It Select Problems?

**Yes, it is fundamentally uncertainty-based.** The entire Challenger reward and filtering pipeline is built around the Solver's empirical uncertainty:

1. **Generation incentive:** The uncertainty reward directly maximizes when p_hat = 0.5.
2. **Selection filter:** Only questions with p_hat in [0.25, 0.75] survive to the training set.
3. **Dynamic calibration:** As the Solver improves across iterations, previously challenging questions become easy (p_hat rises), so the Challenger must generate harder problems to maintain the 50% target. Table 4 in the paper confirms this -- evaluating Iteration 1's Solver against progressively harder question sets shows declining performance (59% -> 47%).

The uncertainty is measured purely at the **outcome level** (final answer correctness), NOT at the process/step level.

---

### Comparison to PRM Error Taxonomy for Curriculum

This is where R-Zero and your PRM-diagnosed adaptive curriculum idea diverge significantly:

**R-Zero's approach:**
- **Outcome-level uncertainty:** Binary correct/incorrect via majority vote on final answers
- **No error diagnosis:** Does not examine WHY the Solver fails -- just THAT it fails ~50% of the time
- **Domain-agnostic signal:** The 50% uncertainty target is a generic difficulty proxy
- **No step-level feedback:** The Solver receives no information about which reasoning steps went wrong

**PRM error taxonomy approach (your idea):**
- **Process-level diagnosis:** Identifies specific error types (computational errors, logical gaps, conceptual misunderstandings, etc.) at each reasoning step
- **Targeted curriculum:** Can generate problems that specifically exercise weak reasoning sub-skills
- **Richer signal:** The error taxonomy provides a structured understanding of failure modes, enabling more efficient curriculum design
- **Verifier co-improvement:** The PRM itself improves as it sees more diverse error patterns

**Where R-Zero is weaker and a PRM approach could help:**
1. **Pseudo-label degradation:** R-Zero's biggest limitation is that pseudo-label accuracy drops from 79% to 63% across iterations. A PRM could provide more reliable verification by checking reasoning steps, not just final answers.
2. **Blind curriculum:** R-Zero generates problems at the right difficulty level but doesn't know what KIND of errors the Solver makes. A PRM-diagnosed approach could identify that the Solver specifically struggles with, say, modular arithmetic or geometric reasoning, and generate targeted problems.
3. **Wasted samples:** R-Zero discards questions outside the [0.25, 0.75] band. With process-level diagnosis, even "too hard" problems could provide learning signal by identifying which step fails.
4. **Plateau risk:** R-Zero's gains diminish across iterations partly because the Challenger lacks information about error structure. PRM diagnosis could help sustain improvement by continuously finding new weakness categories.

**Where R-Zero has advantages over PRM-based curriculum:**
1. **Zero data requirement:** No need for step-level annotations to train the PRM.
2. **Simplicity:** Binary uncertainty is a clean, theoretically grounded signal.
3. **No verifier bootstrapping problem:** PRMs need training data; R-Zero bootstraps entirely from the base model.
4. **Computational efficiency:** No need to run a separate PRM inference for each reasoning step.

**Relevant recent work bridging these approaches:**
- "Adversarial Training for Process Reward Models" (Juneja et al.) uses a Generator-PRM co-training scheme similar in spirit to R-Zero but at the process level.
- "Error Typing for Smarter Rewards" (PathFinder-PRM) uses fine-grained error taxonomy (mathematical errors, consistency issues) for step-level scoring.
- "Bidirectional Curriculum Generation" uses multi-agent frameworks to dynamically generate data by complicating or simplifying problems based on specific reasoning failures.

---

### Key Limitations

1. **Pseudo-label quality degradation:** Accuracy drops from 79% -> 69% -> 63% across 3 iterations. This is the paper's self-identified "critical bottleneck." As problems get harder, majority voting becomes unreliable.

2. **Domain restriction:** Only works for tasks with objective verifiability (math). Cannot extend to creative writing, open-ended reasoning, or tasks where correctness is subjective.

3. **Performance plateau:** Gains diminish with each iteration, suggesting fundamental limits to the co-evolutionary dynamic without external grounding.

4. **No process-level understanding:** The framework treats the Solver as a black box -- it knows difficulty but not error structure.

5. **Scale constraints:** All experiments used 3B-8B models on 8 GPUs. Scaling behavior to larger models is unknown.

6. **Diversity math_verify bug:** The implementation encountered an infinite loop bug in the math_verify library, requiring timeout workarounds (noted in the GitHub repo).

7. **Compared to Absolute Zero (concurrent work):** Absolute Zero uses a code executor for verifiable rewards across abduction/deduction/induction tasks, providing a more domain-flexible framework than R-Zero's math-only approach.

---

### Summary for Your Research Idea

R-Zero validates the core premise that challenger-solver co-evolution with uncertainty-based curriculum adaptation works for improving math reasoning. However, its reliance on **outcome-level** uncertainty (p_hat = 0.5 targeting) is both its strength (simplicity, zero data) and its weakness (no error diagnosis, pseudo-label degradation, blind curriculum).

Your PRM-diagnosed adaptive curriculum idea directly addresses R-Zero's main limitations by: (a) replacing unreliable majority-vote pseudo-labels with process-level verification, (b) adding error-type awareness to curriculum generation so the Challenger can target specific weaknesses, and (c) potentially sustaining improvement beyond R-Zero's plateau by continuously discovering new error categories. The key challenge for your approach will be bootstrapping the PRM without human step-level annotations -- potentially solvable by initializing with R-Zero's outcome-level approach and gradually adding process-level refinement.

Sources:
- [R-Zero: Self-Evolving Reasoning LLM from Zero Data (arXiv)](https://arxiv.org/abs/2508.05004)
- [R-Zero HTML version](https://arxiv.org/html/2508.05004v1)
- [R-Zero OpenReview](https://openreview.net/forum?id=96apU6YzSO)
- [R-Zero GitHub Repository](https://github.com/Chengsong-Huang/R-Zero)
- [R-Zero Project Page](https://chengsong-huang.github.io/R-Zero.github.io/)
- [R-Zero: A Method For Training Reasoning LLMs With Zero Data](https://www.intoai.pub/p/r-zero)
- [Adversarial Training for Process Reward Models](https://arxiv.org/abs/2511.22888)
- [Error Typing for Smarter Rewards (PathFinder-PRM)](https://arxiv.org/abs/2505.19706)
- [Absolute Zero: Reinforced Self-play Reasoning with Zero Data](https://arxiv.org/abs/2505.03335)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c37a271-fc86-4fb1-9552-cb3bd859dc04",
  "isSidechain": true,
  "agentId": "a629672d73d886a3c",
  "requestId": "req_011CbUPc1Ycv7G9mFwYosU3M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7fe09746-670b-4d23-9dd1-c154af410cb1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7945f29-9935-49f0-9154-fa3c8c76e1ef",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FJ4NW3H1ywwTSjXfDRs5w6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 835,
      "cache_read_input_tokens": 21848,
      "output_tokens": 3291,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 835
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3291,
          "cache_read_input_tokens": 21848,
          "cache_creation_input_tokens": 835,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 835,
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
