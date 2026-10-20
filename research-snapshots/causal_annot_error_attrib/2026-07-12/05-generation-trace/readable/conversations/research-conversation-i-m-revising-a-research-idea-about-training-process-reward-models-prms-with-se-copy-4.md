# Research conversation: I'm revising a research idea about training Process Reward Models (PRMs) with search-objective losses (differentiable be

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-aef7cd42e386f60aa.jsonl`
- **Structured JSON:** [`45629cce1eed52c3dd8c.json`](../../sessions/45/45629cce1eed52c3dd8c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

28 recorded events

### User

_source line 1 · 2026-05-27T17:51:09.030Z_

I'm revising a research idea about training Process Reward Models (PRMs) with search-objective losses (differentiable beam search). Reviewers flagged three more missing related works. Please research ALL THREE:

1. "From Curiosity to Caution" (arXiv 2604.04648, Apr 2026) - applies pessimistic reward correction for Best-of-N to mitigate reward hacking
2. "Learning Generative Selection for Best-of-N" (arXiv 2602.02143, Feb 2026) - trains selection models via RL for search
3. "Inference-Aware Fine-Tuning for Best-of-N Sampling" (ICLR 2025, arXiv 2412.15287) - generator-side analog of inference-aware training

For each paper:
- Search for it using WebSearch
- Fetch and read it using WebFetch on its arXiv page
- Report: core approach, training objective, key results, how it differs from training a PRM with end-to-end search-objective loss via differentiable beam search, and its limitations

Be thorough but concise for each paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "cfe7962d-223e-4b12-9480-c455cf84546f",
  "agentId": "aef7cd42e386f60aa",
  "type": "user",
  "uuid": "d3668561-0dd7-4b79-baf9-fb90b20e380d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-27T17:51:09.036Z_

```json
{
  "parentUuid": "d3668561-0dd7-4b79-baf9-fb90b20e380d",
  "isSidechain": true,
  "agentId": "aef7cd42e386f60aa",
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
  "uuid": "8f5050fc-3b4e-4493-ac2f-67a8fecb1968",
  "timestamp": "2026-05-27T17:51:09.036Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-27T17:51:09.037Z_

```json
{
  "parentUuid": "8f5050fc-3b4e-4493-ac2f-67a8fecb1968",
  "isSidechain": true,
  "agentId": "aef7cd42e386f60aa",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c0d6f127-8fc9-45d7-8460-ea8c1736388b",
  "timestamp": "2026-05-27T17:51:09.037Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-27T17:51:13.265Z_



I'll research all three papers. Let me start by loading the WebSearch and WebFetch tools, then search for all three papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0d6f127-8fc9-45d7-8460-ea8c1736388b",
  "isSidechain": true,
  "agentId": "aef7cd42e386f60aa",
  "requestId": "req_011CbTVqPcyKDt1Jf7XDzeuc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e2b8e024-1394-4876-8e75-1a76de6b9ea9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SZKcoxAqGyD9gPqA8vds3k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1616,
      "cache_read_input_tokens": 7411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1616,
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

_source line 5 · 2026-05-27T17:51:13.413Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015w4qBRbwbPTHi6JKBts6u8`</summary>

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
  "parentUuid": "e2b8e024-1394-4876-8e75-1a76de6b9ea9",
  "isSidechain": true,
  "agentId": "aef7cd42e386f60aa",
  "requestId": "req_011CbTVqPcyKDt1Jf7XDzeuc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "601cd8ab-715d-40be-a547-51abb50689e9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SZKcoxAqGyD9gPqA8vds3k",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1616,
      "cache_read_input_tokens": 7411,
      "output_tokens": 111,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1616
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 111,
          "cache_read_input_tokens": 7411,
          "cache_creation_input_tokens": 1616,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1616,
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

_source line 6 · 2026-05-27T17:51:13.418Z_

<details><summary>↩ Tool result · `toolu_015w4qBRbwbPTHi6JKBts6u8`</summary>

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
  "parentUuid": "601cd8ab-715d-40be-a547-51abb50689e9",
  "isSidechain": true,
  "promptId": "cfe7962d-223e-4b12-9480-c455cf84546f",
  "agentId": "aef7cd42e386f60aa",
  "type": "user",
  "uuid": "7e049243-4bb6-459a-8be1-df666c5a0e88",
  "sourceToolAssistantUUID": "601cd8ab-715d-40be-a547-51abb50689e9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-27T17:51:22.056Z_



Now let me search for all three papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e049243-4bb6-459a-8be1-df666c5a0e88",
  "isSidechain": true,
  "agentId": "aef7cd42e386f60aa",
  "requestId": "req_011CbTVqiak2iTwPkj7crdhr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e1c8142b-0b22-459e-8c16-875e7d7debf8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WshXe5LWc8opA2qNTMJF1Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 9027,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1133,
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

_source line 8 · 2026-05-27T17:51:23.003Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QwQjyiwCMVGaSM5t7ducRt`</summary>

```json
{
  "query": "arXiv 2604.04648 \"From Curiosity to Caution\" pessimistic reward correction Best-of-N"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1c8142b-0b22-459e-8c16-875e7d7debf8",
  "isSidechain": true,
  "agentId": "aef7cd42e386f60aa",
  "requestId": "req_011CbTVqiak2iTwPkj7crdhr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d3e3f4ed-97ec-4381-9a9f-76515249b218",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WshXe5LWc8opA2qNTMJF1Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 9027,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1133,
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

_source line 9 · 2026-05-27T17:51:24.002Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QMS2dkN2boN1ZwHrUtmamw`</summary>

```json
{
  "query": "arXiv 2602.02143 \"Learning Generative Selection for Best-of-N\" RL selection models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3e3f4ed-97ec-4381-9a9f-76515249b218",
  "isSidechain": true,
  "agentId": "aef7cd42e386f60aa",
  "requestId": "req_011CbTVqiak2iTwPkj7crdhr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1013dde-0fa6-4e8e-9196-88ceb9dcd1f5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WshXe5LWc8opA2qNTMJF1Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 9027,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1133,
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

_source line 10 · 2026-05-27T17:51:24.968Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013Vgxme9VcdgCVteMZU3jxS`</summary>

```json
{
  "query": "arXiv 2412.15287 \"Inference-Aware Fine-Tuning for Best-of-N Sampling\" ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1013dde-0fa6-4e8e-9196-88ceb9dcd1f5",
  "isSidechain": true,
  "agentId": "aef7cd42e386f60aa",
  "requestId": "req_011CbTVqiak2iTwPkj7crdhr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e2f4cdd-9908-4530-b6a0-0bfa3ae31d36",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WshXe5LWc8opA2qNTMJF1Y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 9027,
      "output_tokens": 226,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1133
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 226,
          "cache_read_input_tokens": 9027,
          "cache_creation_input_tokens": 1133,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1133,
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

_source line 11 · 2026-05-27T17:51:30.200Z_

<details><summary>↩ Tool result · `toolu_01QwQjyiwCMVGaSM5t7ducRt`</summary>

```text
Web search results for query: "arXiv 2604.04648 "From Curiosity to Caution" pessimistic reward correction Best-of-N"

Links: [{"title":"From Curiosity to Caution: Mitigating Reward Hacking for Best-of-𝑁 with Pessimism","url":"https://arxiv.org/html/2604.04648"},{"title":"[2604.04648] From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism","url":"https://arxiv.org/abs/2604.04648"},{"title":"From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism","url":"https://arxiv.org/pdf/2604.04648"},{"title":"Best-of-Tails: Bridging Optimism and Pessimism in Inference-Time Alignment","url":"https://arxiv.org/pdf/2603.06797"},{"title":"Learning a Pessimistic Reward Model in RLHF","url":"https://arxiv.org/pdf/2505.20556"}]

I found the paper! Here's what I can tell you about arXiv 2604.04648:

**Title:** From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism

**Authors:** Zhuohao Yu, Zhiwei Steven Wu (Carnegie Mellon University), and Adam Block (Columbia University)

**Main Topic:** The paper addresses Best-of-N (BoN) sampling, where N candidate responses are generated, scored according to a reward model, and the highest-scoring response is selected. While this approach can improve performance, it is vulnerable to reward hacking, where performance degrades as N increases due to the selection of responses that exploit imperfections in the reward model instead of genuinely improving generation quality.

**Proposed Solution:** The work explores the principle of pessimism in RL, which uses lower confidence bounds on value estimates to avoid out-of-distribution actions with uncertain reward estimates. The approach, called caution, can be seen as the reverse of curiosity: where curiosity rewards prediction error as a signal of novelty, caution penalizes prediction error as a signal of distributional uncertainty. Caution trains an error model on typical responses and uses its prediction error to lower reward estimates for atypical ones.

**Results:** Using the pessimistic approach, reward-hacking is substantially mitigated, with performance improving monotonically with N, achieving a 15.5% boost over the final accuracy of the reward model alone.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d3e3f4ed-97ec-4381-9a9f-76515249b218",
  "isSidechain": true,
  "promptId": "cfe7962d-223e-4b12-9480-c455cf84546f",
  "agentId": "aef7cd42e386f60aa",
  "type": "user",
  "uuid": "728164e5-90b2-4699-89e0-6bddf12a465b",
  "sourceToolAssistantUUID": "d3e3f4ed-97ec-4381-9a9f-76515249b218",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-27T17:51:31.609Z_

<details><summary>↩ Tool result · `toolu_013Vgxme9VcdgCVteMZU3jxS`</summary>

```text
Web search results for query: "arXiv 2412.15287 "Inference-Aware Fine-Tuning for Best-of-N Sampling" ICLR 2025"

Links: [{"title":"Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models","url":"https://proceedings.iclr.cc/paper_files/paper/2025/hash/c40bed606c51c8e827c1ba75aa2da054-Abstract-Conference.html"},{"title":"ICLR Poster Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models","url":"https://iclr.cc/virtual/2025/poster/30849"},{"title":"[2412.15287] Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models","url":"https://arxiv.org/abs/2412.15287"},{"title":"Inference-Aware Fine-Tuning for Best-of-N Sampling in ...","url":"https://arxiv.org/pdf/2412.15287"},{"title":"Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models","url":"https://arxiv.org/html/2412.15287v1"},{"title":"Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241215287C/abstract"},{"title":"Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models | alphaXiv","url":"https://www.alphaxiv.org/abs/2412.15287"},{"title":"Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=77gQUdQhE7"},{"title":"[PDF] Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Inference-Aware-Fine-Tuning-for-Best-of-N-Sampling-Chow-Tennenholtz/53106a642a12b05753ebe9ffca62d8efb0670281"},{"title":"Paper page - Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models","url":"https://huggingface.co/papers/2412.15287"}]

I found the paper you're looking for! Here's what I found:

## Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models

The paper arXiv:2412.15287 was submitted on December 18, 2024, with the most recent version (v2) on November 25, 2025, and it is part of the International Conference on Representation Learning 2025 (ICLR 2025) Conference.

**Main Contribution:**

The paper proposes a novel inference-aware fine-tuning paradigm, in which the model is fine-tuned in a manner that directly optimizes the performance of the inference-time strategy. The authors devise the first imitation learning and reinforcement learning (RL) methods for BoN-aware fine-tuning, overcoming the challenging, non-differentiable argmax operator within BoN.

**Key Findings:**

The authors empirically demonstrate that their BoN-aware models implicitly learn a meta-strategy that interleaves best responses with more diverse responses that might be better suited to a test-time input -- a process reminiscent of the exploration-exploitation trade-off in RL.

**Authors:** Yinlam Chow, Guy Tennenholtz, Izzeddin Gur, Vincent Zhuang, Bo Dai, Sridhar Thiagarajan, Craig Boutilier, Rishabh Agarwal, Aviral Kumar, and Aleksandra Faust.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e2f4cdd-9908-4530-b6a0-0bfa3ae31d36",
  "isSidechain": true,
  "promptId": "cfe7962d-223e-4b12-9480-c455cf84546f",
  "agentId": "aef7cd42e386f60aa",
  "type": "user",
  "uuid": "c97a45f1-a8cd-4840-99f5-87ef05b87ca9",
  "sourceToolAssistantUUID": "8e2f4cdd-9908-4530-b6a0-0bfa3ae31d36",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-27T17:51:32.085Z_

<details><summary>↩ Tool result · `toolu_01QMS2dkN2boN1ZwHrUtmamw`</summary>

```text
Web search results for query: "arXiv 2602.02143 "Learning Generative Selection for Best-of-N" RL selection models"

Links: [{"title":"[2602.02143] Learning Generative Selection for Best-of-N","url":"https://arxiv.org/abs/2602.02143"},{"title":"2026-2-3 Learning Generative Selection for Best-of-N","url":"https://arxiv.org/pdf/2602.02143"},{"title":"Learning Generative Selection for Best-of-N","url":"https://arxiv.org/html/2602.02143"},{"title":"Learning Generative Selection for Best-of-N | Read Paper...","url":"https://bytez.com/docs/arxiv/2602.02143/paper"},{"title":"GenSelect: A Generative Approach to Best-of-N","url":"https://arxiv.org/pdf/2507.17797"},{"title":"Learning to Choose or Choosing to Learn: Best-of-N vs. Supervised Fine-Tuning for Bit String Generation","url":"https://arxiv.org/pdf/2505.17288"},{"title":"[2507.17797] GenSelect: A Generative Approach to Best-of-N","url":"https://arxiv.org/abs/2507.17797"},{"title":"The Best of N Worlds: Aligning Reinforcement Learning with Best-of-N Sampling via max@k Optimisation","url":"https://arxiv.org/pdf/2510.23393"}]

Based on the search results, I found information about arXiv paper 2602.02143 on "Learning Generative Selection for Best-of-N":

## Paper Overview

The paper addresses the limitation that scaling test-time compute via parallel sampling can substantially improve LLM reasoning, but is often limited by Best-of-N selection quality.

## Main Contribution

Generative selection methods, such as GenSelect, address this bottleneck, yet strong selection performance remains largely limited to large models. The authors show that small reasoning models can acquire strong GenSelect capabilities through targeted reinforcement learning.

## Methodology

The researchers synthesize selection tasks from large-scale math and code instruction datasets by filtering to instances with both correct and incorrect candidate solutions, and train 1.7B-parameter models with DAPO to reward correct selections.

## Evaluation Results

Across math (AIME24, AIME25, HMMT25) and code (LiveCodeBench) reasoning benchmarks, their RL-trained GenSelect models consistently outperform prompting and majority voting baselines.

The paper was submitted to arXiv on February 2, 2026, and includes 8 authors led by Shubham Toshniwal.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1013dde-0fa6-4e8e-9196-88ceb9dcd1f5",
  "isSidechain": true,
  "promptId": "cfe7962d-223e-4b12-9480-c455cf84546f",
  "agentId": "aef7cd42e386f60aa",
  "type": "user",
  "uuid": "4b6fbb65-f4c2-449c-bf6c-40b0019f32f5",
  "sourceToolAssistantUUID": "f1013dde-0fa6-4e8e-9196-88ceb9dcd1f5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-27T17:51:35.035Z_

Good, I found all three papers. Now let me fetch the full content from each paper's arXiv HTML page in parallel to get detailed information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b6fbb65-f4c2-449c-bf6c-40b0019f32f5",
  "isSidechain": true,
  "agentId": "aef7cd42e386f60aa",
  "requestId": "req_011CbTVs6D2MHBjjktC53h9K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "31bb9bd5-cd14-4a97-8f83-163f865c95f3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H6zVB4B5ySPxZ4cKQ8EP1o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1024,
      "cache_creation_input_tokens": 1589,
      "cache_read_input_tokens": 10160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1589,
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

_source line 15 · 2026-05-27T17:51:39.286Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Lojj5Px1CcVfnNmikcLQz2`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.04648",
  "prompt": "Extract the following details from this paper in full detail:\n1. The core approach and method (how pessimistic reward correction works, what is the \"caution\" mechanism, how the error model is trained)\n2. The exact training objective / loss function used\n3. Key quantitative results (numbers, baselines, benchmarks)\n4. Limitations discussed by the authors\n5. How does this relate to training reward models or process reward models? Does it modify the reward model training or only the inference-time selection?\n6. What is their theoretical contribution?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31bb9bd5-cd14-4a97-8f83-163f865c95f3",
  "isSidechain": true,
  "agentId": "aef7cd42e386f60aa",
  "requestId": "req_011CbTVs6D2MHBjjktC53h9K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f559c8ee-1016-4d18-be98-367aaa732abc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H6zVB4B5ySPxZ4cKQ8EP1o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1024,
      "cache_creation_input_tokens": 1589,
      "cache_read_input_tokens": 10160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1589,
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

_source line 16 · 2026-05-27T17:51:41.686Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Pu6A1a6w3aKXvN4o5tzYDY`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.02143",
  "prompt": "Extract the following details from this paper in full detail:\n1. The core approach and method (how generative selection works, how RL training is done, what is DAPO, what are the selection tasks)\n2. The exact training objective / loss function used\n3. Key quantitative results (numbers, baselines, benchmarks)\n4. Limitations discussed by the authors\n5. How does this relate to training process reward models? Does it replace the PRM with a generative selector?\n6. What model sizes and architectures are used?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f559c8ee-1016-4d18-be98-367aaa732abc",
  "isSidechain": true,
  "agentId": "aef7cd42e386f60aa",
  "requestId": "req_011CbTVs6D2MHBjjktC53h9K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f4cc6ca-050a-4015-a09b-7b515bd5ea6d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H6zVB4B5ySPxZ4cKQ8EP1o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1024,
      "cache_creation_input_tokens": 1589,
      "cache_read_input_tokens": 10160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1589,
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

_source line 17 · 2026-05-27T17:51:44.216Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016gXPgLNvX4nBDKwAosevGC`</summary>

```json
{
  "url": "https://arxiv.org/html/2412.15287v1",
  "prompt": "Extract the following details from this paper in full detail:\n1. The core approach and method (how inference-aware fine-tuning works, how they handle the non-differentiable argmax in BoN, what is the imitation learning method, what is the RL method)\n2. The exact training objective / loss function used (both IL and RL variants)\n3. Key quantitative results (numbers, baselines, benchmarks)\n4. Limitations discussed by the authors\n5. How does this relate to training process reward models or verifiers? Is this a generator-side or verifier-side approach?\n6. What is the exploration-exploitation trade-off they observe?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f4cc6ca-050a-4015-a09b-7b515bd5ea6d",
  "isSidechain": true,
  "agentId": "aef7cd42e386f60aa",
  "requestId": "req_011CbTVs6D2MHBjjktC53h9K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5dfdc98-d264-45ec-b9be-0854e47cc76a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H6zVB4B5ySPxZ4cKQ8EP1o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1024,
      "cache_creation_input_tokens": 1589,
      "cache_read_input_tokens": 10160,
      "output_tokens": 633,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1589
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1024,
          "output_tokens": 633,
          "cache_read_input_tokens": 10160,
          "cache_creation_input_tokens": 1589,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1589,
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

_source line 18 · 2026-05-27T17:51:54.269Z_

<details><summary>↩ Tool result · `toolu_01Lojj5Px1CcVfnNmikcLQz2`</summary>

```text
# Paper Analysis: From Curiosity to Caution

## 1. Core Approach and Method

The paper introduces **caution**, an inference-time mechanism to mitigate reward hacking in Best-of-N (BoN) sampling. Rather than modifying the reward model itself, the approach applies pessimism at the reward estimation level.

**The Caution Mechanism:**
- Trains a lightweight predictor network to match frozen feature representations from the reward model on in-distribution responses
- At inference, uses prediction error as an uncertainty signal: larger errors indicate out-of-distribution (OOD) responses
- Computes a pessimistic reward estimate by subtracting uncertainty-weighted penalties from the base reward model's scores

The method conceptually inverts "curiosity" from RL—where prediction error signals novelty worth exploring—to penalize distributional uncertainty instead.

## 2. Training Objective and Loss Function

The predictor network is trained via supervised learning on in-distribution data:

**Loss function:** ℒ(θ) = E[(||P_θ(x,y) - T(x,y)||²)]

Where:
- P_θ is the trainable predictor network
- T(x,y) extracts layer L features from the frozen reward model
- Training uses responses sampled from the base language model on benchmark prompts
- No labeled data required—only prompts and model generations

At inference, the final selection uses: r̂_LCB(x,y) = r̂(x,y) - λ·||P_θ(x,y) - T(x,y)||²

## 3. Key Quantitative Results

**Main findings on GSM8K:**
- Caution achieves 82.6% peak accuracy vs. 79.3% for standard BoN
- Final accuracy at N=512: 81.1% (caution) vs. 71.5% (reward model alone)
- Performance degradation: only 1.5 percentage points vs. 7.7 for standard BoN

**Out-of-distribution evaluations:**
- MATH-500: Pessimism-only reaches 13.6% peak with 1.7pt degradation
- BigBench-Hard: Demonstrates robustness across domains despite training only on GSM8K

**Ablation results:**
- Lightweight predictor architectures outperform full networks (82.2% vs 80.3%)
- Distilling reward model features substantially outperforms random network distillation across all λ values

## 4. Limitations Discussed

The authors acknowledge:
- Analysis is primarily empirical in naturalistic settings; theoretical results require simplified linear assumptions
- Method is less effective when reward models fail catastrophically (BigBench-Hard case)
- Requires careful balance between reconstruction accuracy and novelty sensitivity—lighter architectures work better than overly flexible ones
- Uncertainty estimates become less reliable on substantially OOD domains, though robustness is reasonably good

## 5. Relationship to Reward Model Training

**Critical distinction:** This work operates entirely at inference time and does NOT modify reward model training. The approach:
- Takes existing, fixed reward models as given
- Trains only a separate, lightweight predictor network on responses sampled from the base LM
- Does not retrain, fine-tune, or ensemble reward models
- Works as a post-hoc selection mechanism compatible with any reward model

This contrasts with training-time approaches that improve reward model quality directly.

## 6. Theoretical Contribution

**Main theoretical result (Theorem 1 informal statement):**

For a simplified linear setting with Gaussian distributions, if an uncertainty estimate α satisfies certain bounds on OOD detection, then pessimistic selection strictly improves over standard BoN:

E[r⋆(y_ipess) - r⋆(y_î)] ≳ √log(N)

The bound grows with sampling budget N (unlike BoN's performance degradation), proving pessimism monotonically outperforms in this abstraction. The authors also provide guarantees that Random Network Distillation-style prediction errors can approximate OOD detection in both linear and two-layer ReLU settings, though these require substantial embedding dimension relative to intrinsic problem dimensionality.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f559c8ee-1016-4d18-be98-367aaa732abc",
  "isSidechain": true,
  "promptId": "cfe7962d-223e-4b12-9480-c455cf84546f",
  "agentId": "aef7cd42e386f60aa",
  "type": "user",
  "uuid": "09fc98dc-e6cd-4698-ba85-f81a108beca6",
  "sourceToolAssistantUUID": "f559c8ee-1016-4d18-be98-367aaa732abc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-27T17:51:57.231Z_

<details><summary>↩ Tool result · `toolu_01Pu6A1a6w3aKXvN4o5tzYDY`</summary>

```text
# Learning Generative Selection for Best-of-N: Key Details

## 1. Core Approach and Method

**Generative Selection Framework:**
The paper introduces a method where small models learn to explicitly select the best candidate solution from multiple options. Rather than scoring candidates independently, the model performs "reasoning over NN responses, posing this aggregation as a reasoning problem."

**How It Works:**
Given N candidate solutions to a problem, the model analyzes them and outputs the index of the best solution, formatted as: "Judgment [IDX]" where IDX ranges from 0 to N-1.

**RL Training Specifics:**
- Uses the DAPO algorithm with on-policy selection generation
- Trains on synthetic selection tasks constructed from math and coding datasets
- Tasks filtered to include both correct and incorrect solutions with ≤50% pass rates
- Rewards models for correctly identifying the best solution among imperfect candidates

**Selection Task Construction:**
For math: 37K problems from OpenMathReasoning where the base model achieves <50% pass rate. Generates 2-16 candidate solutions per problem using symbolic verification (Math-Verify). For code: Uses OpenCodeReasoning problems with unit tests for correctness labels. Both domains enforce at least one correct solution and cap correct candidates at 50% for difficulty.

## 2. Training Objective / Loss Function

The document does not explicitly state the loss function equations or formal optimization objective. It only specifies that DAPO is used "with on-policy selection generation" and models are "rewarded for selecting a correct solution among imperfect candidates." The specific reward signal structure and loss formulation are referenced but not detailed.

## 3. Key Quantitative Results

**Performance on Qwen3-1.7B Generations (Math):**
- AIME24: RL-trained 1.7B achieves 65.00% vs. 48.75% for prompting baseline
- AIME25: 54.17% (RL) vs. 38.33% (prompting)
- HMMT25: 36.25% (RL) vs. 26.67% (prompting)

**Generalization to Stronger Models:**
When selecting from Qwen3-8B generations:
- AIME25: RL-trained 1.7B reaches 78.33%, approaching 8B prompting at 78.33%
- HMMT25: RL-trained 1.7B achieves 56.25% vs. 55.83% for 8B prompting

**Code Performance (LiveCodeBench v6):**
- RL math model: 36.45%
- RL code model: 36.84%
- Both outperform prompting but underperform larger models

**Baseline Comparisons:**
Pass@8 (oracle maximum): 70% (math), 45.59% (code). Majority voting: 63.33% (math), N/A (code).

## 4. Limitations Discussed

**Code Domain Challenges:**
The authors attribute smaller code gains to two factors: "(1) correctness signals derived from unit tests are noisier and less exhaustive than symbolic math verification" and "(2) code selection requires broader semantic coverage than math—including algorithmic structure, edge-case handling, complexity constraints."

**Cross-domain Transfer Asymmetry:**
"Training on math selection data improves code selection, whereas training on code yields limited improvements on math." Code training shows "noisier dynamics and earlier saturation."

**Model Size Constraints:**
The 1.7B model struggles with GenSelect prompting alone due to "the smaller 1.7B parameter count, which may cause the model to overfit to typical solution-generation tasks and fail to generalize to the GenSelect instructions."

## 5. Relationship to Process Reward Models

This approach differs fundamentally from traditional process reward models (PRMs). Rather than scoring intermediate reasoning steps, generative selection evaluates complete final solutions by comparing them and selecting the best one. The paper positions this as complementary to verification-based methods: "In contrast, synthesis-based aggregation produces new outputs that typically require re-running verification...In contrast, selection can be substantially easier to train with reinforcement learning: since rewards are defined over selected candidates, correctness labels can be precomputed."

This does not replace PRMs but offers an alternative selection mechanism—it's a generative comparative approach rather than step-level reward modeling.

## 6. Model Sizes and Architectures

**Primary Model:**
Qwen3-1.7B (the focus of the work)

**Comparison Baselines:**
- Qwen3-4B
- Qwen3-8B

**Training Infrastructure:**
VeRL framework on NVIDIA H100 GPUs. Configuration: batch size 128, learning rate 1×10⁻⁶, AdamW optimizer, temperature 1.5, top-p 1.0, max output 16,384 tokens.

No custom architecture modifications are mentioned; standard transformer parameters are used.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f4cc6ca-050a-4015-a09b-7b515bd5ea6d",
  "isSidechain": true,
  "promptId": "cfe7962d-223e-4b12-9480-c455cf84546f",
  "agentId": "aef7cd42e386f60aa",
  "type": "user",
  "uuid": "53eaa739-1179-4647-bb62-36cc87a05c9a",
  "sourceToolAssistantUUID": "8f4cc6ca-050a-4015-a09b-7b515bd5ea6d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-27T17:52:01.388Z_

<details><summary>↩ Tool result · `toolu_016gXPgLNvX4nBDKwAosevGC`</summary>

```text
# Inference-Aware Fine-Tuning for Best-of-N Sampling: Core Details

## 1. Core Approach and Method

**Inference-Aware Fine-Tuning Paradigm:**
The authors propose training LLMs by explicitly considering the inference strategy (Best-of-N) during training, rather than training in a strategy-agnostic manner. This closes the gap between how models are trained versus deployed.

**Handling Non-Differentiable ArgMax:**
The key technical innovation addresses the non-differentiability of the argmax operator in BoN. They derive a variational approximation of the BoN policy:

π_bon(y|x) ∝ π(y|x) · exp(λ_N Q_π(x,y))

where Q_π represents the "win-rate" - the probability a response outperforms samples from the base policy according to verifier score r. This transforms the discrete selection problem into a continuous optimization problem.

**Imitation Learning Method (BoN-SFT):**
Supervised fine-tuning maximizes likelihood of expert data while incorporating inference-awareness. The gradient update combines: (1) likelihood maximization over expert data, (2) alignment with verifier score rankings, (3) regularization against overfitting to base policy samples.

**RL Methods:**
- **BoN-RL-V**: General RL formulation sampling from BoN policy distribution to optimize environment reward
- **BoN-RLB**: Binary reward variant with closed-form solution providing asymmetric weighting between correct/incorrect responses
- **BoN-RLB(P)**: Positive-only variant for scenarios where negative examples are unavailable

## 2. Training Objectives

**BoN-SFT Objective (Lemma 1):**
The gradient incorporates likelihood term plus inference-awareness term with win-rate weighting and partition function regularization.

**BoN-RL Objective (Lemma 2):**
Uses REINFORCE-style gradient: ∇_θJ(θ) = E[∇_θ log π_θ(x,y) · (R(x,y) - b(x))], where samples y are drawn from BoN policy rather than base policy.

**BoN-RLB Objective (Lemma 3):**
For binary rewards, employs asymmetric weighting: g^+_N(p) = N·p^(N-1)/(1-p^N) for correct responses and g^-(p) = N·p/(1-p) for incorrect responses, where p = P_fail(x).

## 3. Key Quantitative Results

**Math Benchmarks (Gemma 2B):**
- Bo32 accuracy improved from 26.8% → 30.8% (BoN-RL-V)
- pass@32 improved from 60.0% → 67.0% (BoN-RL-S)

**Code Benchmarks (Gemma 2B):**
- pass@16 on HumanEval: 61.6% → 67.1% (BoN-RLB(P))

**Held-out benchmarks:**
Consistent improvements on Functional MATH and MathOdyssey demonstrate generalization.

**Baselines compared against:**
STaR, standard RL with verifier feedback, RL with environment feedback, standard SFT, base model with BoN.

## 4. Limitations

Authors acknowledge:
- Sample inefficiency in general BoN-RL (mitigated via distillation in appendix)
- BoN-RL-V doesn't significantly improve pass@N metrics compared to base model
- Inference-unaware RL baselines suffer from reward hacking issues
- Relying solely on temperature/sample adjustment has limitations without direct training

## 5. Generator vs. Verifier Side

**This is a generator-side approach.** The method fine-tunes the LLM policy (generator) to produce outputs better suited for BoN inference. The verifier r(x,y) is used during training as a signal but the optimization targets the base policy π. The approach explicitly trains models to generate "more diverse responses that might be better suited to test-time inputs."

## 6. Exploration-Exploitation Trade-off

**Empirical Co-scaling Discovery:**
Analysis of Gemma 2B on MATH reveals a tradeoff: "easier problems have small (T*, N*), while harder problems require larger (T*, N*) for exploration." Lower temperatures favor exploitation (small N optimal), while higher temperatures enable exploration (larger N needed).

**Implicit Exploration via BoN-RLB:**
The asymmetric weighting scheme in BoN-RLB drives exploration through gradient redistribution—when high-likelihood regions produce errors, probability mass redistributes across alternative solutions, forcing the model to explore beyond established patterns while maintaining exploitation of successful strategies.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5dfdc98-d264-45ec-b9be-0854e47cc76a",
  "isSidechain": true,
  "promptId": "cfe7962d-223e-4b12-9480-c455cf84546f",
  "agentId": "aef7cd42e386f60aa",
  "type": "user",
  "uuid": "0cc48af7-f27c-4632-9405-6f28798c2d2b",
  "sourceToolAssistantUUID": "e5dfdc98-d264-45ec-b9be-0854e47cc76a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-27T17:52:06.907Z_

I now have detailed information on all three papers. Let me also fetch some additional details on the first paper's relationship to PRM training and the second paper's DAPO algorithm details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cc48af7-f27c-4632-9405-6f28798c2d2b",
  "isSidechain": true,
  "agentId": "aef7cd42e386f60aa",
  "requestId": "req_011CbTVuFSTRYnNRRfg68LNJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8d700a4f-431a-433c-a7aa-1d0ee62efb9c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WxQdpWxFs5RyjyQ1LmbSga",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5118,
      "cache_read_input_tokens": 11749,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5118,
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

_source line 22 · 2026-05-27T17:52:08.343Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TknWbWPYWTTXBGsdxzMxhC`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.04648",
  "prompt": "Extract the full abstract of this paper. Also identify: who are the authors, what is the exact date of submission, and what are the key keywords or topics?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d700a4f-431a-433c-a7aa-1d0ee62efb9c",
  "isSidechain": true,
  "agentId": "aef7cd42e386f60aa",
  "requestId": "req_011CbTVuFSTRYnNRRfg68LNJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f11b0921-8b3d-47e9-a804-c31b05aaeea3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WxQdpWxFs5RyjyQ1LmbSga",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5118,
      "cache_read_input_tokens": 11749,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5118,
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

_source line 23 · 2026-05-27T17:52:09.265Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MxQsMmPBQWAbR4UC9o2bss`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.02143",
  "prompt": "Extract the full abstract of this paper. Also identify: who are the authors, what is the exact date of submission, and what are the key topics?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f11b0921-8b3d-47e9-a804-c31b05aaeea3",
  "isSidechain": true,
  "agentId": "aef7cd42e386f60aa",
  "requestId": "req_011CbTVuFSTRYnNRRfg68LNJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6cc9ae0a-5466-4c18-9dfb-c74c2a7c6571",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WxQdpWxFs5RyjyQ1LmbSga",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5118,
      "cache_read_input_tokens": 11749,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5118,
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

_source line 24 · 2026-05-27T17:52:09.872Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01G5bXU3NqASv9w1tMZBGThM`</summary>

```json
{
  "url": "https://arxiv.org/abs/2412.15287",
  "prompt": "Extract the full abstract of this paper. Also identify: who are the authors, what is the exact date of submission, and what are the key topics?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6cc9ae0a-5466-4c18-9dfb-c74c2a7c6571",
  "isSidechain": true,
  "agentId": "aef7cd42e386f60aa",
  "requestId": "req_011CbTVuFSTRYnNRRfg68LNJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0db88f52-d800-4dbe-8eec-8b4f5a870e62",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WxQdpWxFs5RyjyQ1LmbSga",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5118,
      "cache_read_input_tokens": 11749,
      "output_tokens": 346,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5118
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 346,
          "cache_read_input_tokens": 11749,
          "cache_creation_input_tokens": 5118,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5118,
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

_source line 25 · 2026-05-27T17:52:15.014Z_

<details><summary>↩ Tool result · `toolu_01TknWbWPYWTTXBGsdxzMxhC`</summary>

```text
# Paper Summary: Reward Hacking Mitigation in Best-of-N Sampling

## Full Abstract
"Inference-time compute scaling has emerged as a powerful paradigm for improving language model performance on a wide range of tasks, but the question of how best to use the additional compute remains open. A popular approach is BoN sampling, where N candidate responses are generated, scored according to a reward model, and the highest-scoring response is selected. While this approach can improve performance, it is vulnerable to reward hacking, where performance degrades as N increases due to the selection of responses that exploit imperfections in the reward model instead of genuinely improving generation quality. Prior attempts to mitigate reward hacking, via stronger reward models or heavy-handed distributional regularization, either fail to fully address over-optimization or are too conservative to exploit additional compute. In this work, we explore the principle of pessimism in RL, which uses lower confidence bounds on value estimates to avoid OOD actions with uncertain reward estimates. Our approach, termed as caution, can be seen as the reverse of curiosity: where curiosity rewards prediction error as a signal of novelty, caution penalizes prediction error as a signal of distributional uncertainty. Practically, caution trains an error model on typical responses and uses its prediction error to lower reward estimates for atypical ones. Our extensive empirical evaluation demonstrates that caution is a simple, computationally efficient approach that substantially mitigates reward hacking in BoN sampling. We also provide a theoretical analysis in a simplified linear setting, which shows that caution provably improves over the standard BoN approach."

## Key Details

**Authors:** Zhuohao Yu, Zhiwei Steven Wu, Adam Block

**Submission Date:** April 6, 2026

**Primary Keywords/Topics:** 
- Reward hacking mitigation
- Best-of-N sampling
- Language model optimization
- Pessimism in reinforcement learning
- Out-of-distribution detection
- Inference-time compute scaling
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f11b0921-8b3d-47e9-a804-c31b05aaeea3",
  "isSidechain": true,
  "promptId": "cfe7962d-223e-4b12-9480-c455cf84546f",
  "agentId": "aef7cd42e386f60aa",
  "type": "user",
  "uuid": "0281a826-a5ae-49ed-8e64-d7088096a4ec",
  "sourceToolAssistantUUID": "f11b0921-8b3d-47e9-a804-c31b05aaeea3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-27T17:52:15.226Z_

<details><summary>↩ Tool result · `toolu_01MxQsMmPBQWAbR4UC9o2bss`</summary>

```text
# Paper Summary

## Full Abstract
"Scaling test-time compute via parallel sampling can substantially improve LLM reasoning, but is often limited by Best-of-N selection quality. Generative selection methods, such as GenSelect, address this bottleneck, yet strong selection performance remains largely limited to large models. We show that small reasoning models can acquire strong GenSelect capabilities through targeted reinforcement learning. To this end, we synthesize selection tasks from large-scale math and code instruction datasets by filtering to instances with both correct and incorrect candidate solutions, and train 1.7B-parameter models with DAPO to reward correct selections. Across math (AIME24, AIME25, HMMT25) and code (LiveCodeBench) reasoning benchmarks, our models consistently outperform prompting and majority-voting baselines, often approaching or exceeding much larger models. Moreover, these gains generalize to selecting outputs from stronger models despite training only on outputs from weaker models. Overall, our results establish reinforcement learning as a scalable way to unlock strong generative selection in small models, enabling efficient test-time scaling."

## Authors
Shubham Toshniwal, Aleksander Ficek, Siddhartha Jain, Wei Du, Vahid Noroozi, Sadegh Mahdavi, Somshubra Majumdar, and Igor Gitman

## Submission Date
February 2, 2026

## Key Topics
- Generative selection methods for large language models
- Best-of-N selection optimization
- Reinforcement learning (DAPO training)
- Small model capabilities on math and code reasoning benchmarks
- Test-time compute scaling
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6cc9ae0a-5466-4c18-9dfb-c74c2a7c6571",
  "isSidechain": true,
  "promptId": "cfe7962d-223e-4b12-9480-c455cf84546f",
  "agentId": "aef7cd42e386f60aa",
  "type": "user",
  "uuid": "de6d61ff-9065-4181-874d-03f296f9a41d",
  "sourceToolAssistantUUID": "6cc9ae0a-5466-4c18-9dfb-c74c2a7c6571",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-27T17:52:16.487Z_

<details><summary>↩ Tool result · `toolu_01G5bXU3NqASv9w1tMZBGThM`</summary>

```text
# Paper Summary

## Full Abstract
"Recent studies have indicated that effectively utilizing inference-time compute is crucial for attaining better performance from large language models (LLMs). In this work, we propose a novel inference-aware fine-tuning paradigm, in which the model is fine-tuned in a manner that directly optimizes the performance of the inference-time strategy. We study this paradigm using the simple yet effective Best-of-N (BoN) inference strategy, in which a verifier selects the best out of a set of LLM-generated responses. We devise the first imitation learning and reinforcement learning (RL) methods for BoN-aware fine-tuning, overcoming the challenging, non-differentiable argmax operator within BoN. We empirically demonstrate that our BoN-aware models implicitly learn a meta-strategy that interleaves best responses with more diverse responses that might be better suited to a test-time input -- a process reminiscent of the exploration-exploitation trade-off in RL. Our experiments demonstrate the effectiveness of BoN-aware fine-tuning in terms of improved performance and inference-time compute. In particular, we show that our methods improve the Bo32 performance of Gemma 2B on Hendrycks MATH from 26.8% to 30.8%, and pass@32 from 60.0% to 67.0%, as well as the pass@16 on HumanEval from 61.6% to 67.1%."

## Authors
Yinlam Chow, Guy Tennenholtz, Izzeddin Gur, Vincent Zhuang, Bo Dai, Sridhar Thiagarajan, Craig Boutilier, Rishabh Agarwal, Aviral Kumar, and Aleksandra Faust

## Submission Date
December 18, 2024

## Key Topics
- Inference-time optimization for language models
- Best-of-N sampling strategies
- Fine-tuning methods combining imitation learning and reinforcement learning
- Exploration-exploitation dynamics in model training
- Performance improvements on mathematical and code generation benchmarks
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0db88f52-d800-4dbe-8eec-8b4f5a870e62",
  "isSidechain": true,
  "promptId": "cfe7962d-223e-4b12-9480-c455cf84546f",
  "agentId": "aef7cd42e386f60aa",
  "type": "user",
  "uuid": "b82a4e7c-e871-4a3f-a8e9-83ac558d7df3",
  "sourceToolAssistantUUID": "0db88f52-d800-4dbe-8eec-8b4f5a870e62",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-27T17:53:29.367Z_

I now have comprehensive information on all three papers. Here is the full analysis:

---

## Paper 1: "From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism"

**arXiv 2604.04648, April 2026 | Authors: Zhuohao Yu, Zhiwei Steven Wu (CMU), Adam Block (Columbia)**

**Core Approach:** The paper addresses reward hacking in Best-of-N (BoN) sampling, where increasing N eventually degrades performance because the reward model selects OOD responses that exploit its imperfections. The authors propose "caution" -- the inverse of curiosity-driven exploration. They train a lightweight predictor network to reconstruct frozen internal features of the reward model on in-distribution responses. At inference time, high prediction error signals an OOD response, and a penalty is applied:

`r_LCB(x,y) = r(x,y) - lambda * ||P_theta(x,y) - T(x,y)||^2`

where `P_theta` is the predictor, `T` extracts layer-L features from the frozen reward model, and `lambda` controls pessimism strength.

**Training Objective:** The predictor is trained with a simple MSE reconstruction loss on in-distribution data: `L(theta) = E[||P_theta(x,y) - T(x,y)||^2]`. No labeled data is required -- only prompts and base-model generations. The reward model itself is never retrained.

**Key Results:** On GSM8K, caution achieves 82.6% peak accuracy vs. 79.3% for standard BoN. At N=512, caution retains 81.1% vs. 71.5% for the uncorrected reward model (only 1.5pp degradation vs. 7.7pp). The method generalizes to MATH-500 and BigBench-Hard despite training only on GSM8K data. Theoretically, in a linear setting, pessimistic selection provably improves over standard BoN with gains growing as sqrt(log N).

**Difference from PRM + differentiable beam search:** This is purely an inference-time correction applied to an existing, frozen reward model. It never modifies the reward model's training objective and does not make the search procedure differentiable. It is agnostic to whether the reward model is an ORM or PRM. In contrast, training a PRM with end-to-end search-objective loss via differentiable beam search directly optimizes the reward model parameters so its scores produce good search outcomes. Caution is a complementary, post-hoc fix; differentiable beam search is a fundamentally different training paradigm.

**Limitations:** Primarily empirical validation in naturalistic settings; theoretical results rely on simplified linear assumptions. Less effective when reward models fail catastrophically. Requires tuning the architecture capacity of the predictor (lighter is better). Uncertainty estimates degrade on substantially OOD domains.

---

## Paper 2: "Learning Generative Selection for Best-of-N"

**arXiv 2602.02143, February 2026 | Authors: Shubham Toshniwal, Aleksander Ficek, Siddhartha Jain, Wei Du, Vahid Noroozi, Sadegh Mahdavi, Somshubra Majumdar, Igor Gitman**

**Core Approach:** Instead of scoring candidates independently (as a PRM/ORM does), this paper frames selection as a generative reasoning problem. Given N candidate solutions, a small LLM reads all of them and outputs the index of the best one (formatted as "Judgment [IDX]"). The key contribution is showing that small models (1.7B parameters) can acquire strong generative selection (GenSelect) capabilities through targeted RL training.

**Training Objective:** They construct synthetic selection tasks from math (OpenMathReasoning, 37K problems) and code (OpenCodeReasoning) datasets, filtering for problems where the base model achieves <50% pass rate so that both correct and incorrect solutions exist. They train Qwen3-1.7B using DAPO (a variant of on-policy RL) with binary reward: +1 for selecting a correct solution, 0 otherwise. Configuration: batch size 128, LR 1e-6, AdamW, temperature 1.5, max 16K output tokens, trained on H100s using the VeRL framework.

**Key Results:** On AIME24: 65.0% (RL-trained 1.7B) vs. 48.75% (prompting baseline). On AIME25: 54.17% vs. 38.33%. On HMMT25: 36.25% vs. 26.67%. Remarkably, the RL-trained 1.7B model selecting from Qwen3-8B generations matches or exceeds 8B-model prompting on several benchmarks, demonstrating cross-scale generalization. On LiveCodeBench: ~36.8% for RL models vs. lower prompting baselines.

**Difference from PRM + differentiable beam search:** This replaces the score-and-rank paradigm entirely with a generative comparative approach. The selector reasons over all N complete solutions simultaneously rather than scoring each independently. It does not assign per-step or per-solution scalar rewards. It cannot provide step-level process supervision, and it requires generating all candidates first before selection. Differentiable beam search with a PRM, by contrast, trains a reward model that provides step-level scores used to guide search, and it optimizes the reward model end-to-end through the search procedure. The generative selection approach is fundamentally incompatible with tree-search or beam-search paradigms where candidates are pruned at intermediate steps.

**Limitations:** Code domain gains are smaller due to noisier correctness signals from unit tests. Asymmetric cross-domain transfer (math training helps code but not vice versa). The 1.7B model struggles with GenSelect via prompting alone -- RL training is essential. The method requires all N candidates to be fully generated before selection, making it inapplicable to process-level pruning during generation.

---

## Paper 3: "Inference-Aware Fine-Tuning for Best-of-N Sampling"

**ICLR 2025, arXiv 2412.15287, December 2024 | Authors: Yinlam Chow, Guy Tennenholtz, Izzeddin Gur, Vincent Zhuang, Bo Dai, Sridhar Thiagarajan, Craig Boutilier, Rishabh Agarwal, Aviral Kumar, Aleksandra Faust (Google DeepMind)**

**Core Approach:** This is a generator-side approach. Instead of improving the verifier/reward model, it fine-tunes the LLM policy to produce outputs that are better suited for BoN selection at inference time. The key technical challenge is that BoN involves a non-differentiable argmax. They derive a variational approximation of the BoN policy: `pi_bon(y|x) ~ pi(y|x) * exp(lambda_N * Q_pi(x,y))`, where `Q_pi` is the win-rate (probability a response beats other samples according to verifier score). This transforms the discrete argmax into a continuous optimization target.

**Training Objectives:**
- *BoN-SFT (Imitation Learning):* SFT gradient augmented with an inference-awareness term that weights examples by their win-rate under the BoN policy, plus regularization.
- *BoN-RL-V:* REINFORCE-style gradient sampling from the BoN policy distribution rather than the base policy, optimizing environment reward.
- *BoN-RLB:* Binary reward variant with asymmetric weighting -- correct responses weighted by `g_N^+(p) = N*p^(N-1)/(1-p^N)` and incorrect by `g_N^-(p) = N*p/(1-p)`, where `p` is the failure probability. This drives redistribution of probability mass.
- *BoN-RLB(P):* Positive-only variant when negatives are unavailable.

**Key Results:** On Gemma 2B / Hendrycks MATH: Bo32 accuracy 26.8% -> 30.8% (BoN-RL-V); pass@32 60.0% -> 67.0% (BoN-RL-S). On HumanEval: pass@16 61.6% -> 67.1% (BoN-RLB(P)). Improvements generalize to held-out benchmarks (Functional MATH, MathOdyssey). The models implicitly learn a meta-strategy that interleaves high-quality responses with diverse exploratory responses -- harder problems require higher temperature and larger N (exploration), while easier problems need small N (exploitation).

**Difference from PRM + differentiable beam search:** This is the generator-side analog -- it modifies the generator policy to be aware of inference-time search, while your work modifies the verifier/PRM to be aware of search. Both share the philosophy of "inference-aware training" but optimize different components. Key differences: (1) This paper assumes a fixed verifier and tunes the generator; differentiable beam search assumes a fixed generator and tunes the PRM. (2) This paper handles only flat BoN (sample N, pick best), not structured tree search or beam search with step-level scoring. (3) This paper's approximation replaces argmax with a soft variational form; differentiable beam search makes the beam selection itself differentiable. (4) This paper cannot provide process-level supervision signals.

**Limitations:** Sample inefficiency in the general BoN-RL variant. BoN-RL-V does not significantly improve pass@N metrics. Inference-unaware RL baselines suffer from reward hacking. The method is limited to flat BoN -- it does not extend to more complex search procedures like beam search or tree search. It requires a pre-existing verifier and only optimizes the generator distribution, not the scoring function.

---

## Summary of How All Three Differ from Your Approach (PRM + Differentiable Beam Search)

| Aspect | Your Approach | Paper 1 (Caution) | Paper 2 (GenSelect) | Paper 3 (BoN-Aware FT) |
|---|---|---|---|---|
| **What is optimized** | PRM parameters | Nothing (inference-time correction) | Selector LLM via RL | Generator LLM policy |
| **Training signal flows through search** | Yes (differentiable) | No | No (flat selection) | Approximately (variational) |
| **Search type** | Beam search (structured, step-level) | Flat BoN | Flat BoN | Flat BoN |
| **Process-level supervision** | Yes | No | No | No |
| **Modifies reward/verifier** | Yes (end-to-end) | No (post-hoc penalty) | Replaces with generative selector | No (fixed verifier) |
| **Handles reward hacking** | Implicitly (search-aligned scores) | Explicitly (pessimistic correction) | N/A | Partially (via exploration) |

All three papers operate in the flat Best-of-N regime with complete responses, while your approach uniquely targets structured, step-level beam search with end-to-end differentiable training of the PRM. Paper 1 is the most complementary (could be applied on top of any PRM). Paper 3 is the closest philosophically (inference-aware training), but optimizes the opposite component (generator vs. verifier). Paper 2 is the most orthogonal, replacing scoring-based selection entirely with generative reasoning.

Sources:
- [From Curiosity to Caution (arXiv)](https://arxiv.org/abs/2604.04648)
- [From Curiosity to Caution (HTML)](https://arxiv.org/html/2604.04648)
- [Learning Generative Selection for Best-of-N (arXiv)](https://arxiv.org/abs/2602.02143)
- [Learning Generative Selection for Best-of-N (HTML)](https://arxiv.org/html/2602.02143)
- [Inference-Aware Fine-Tuning (arXiv)](https://arxiv.org/abs/2412.15287)
- [Inference-Aware Fine-Tuning (ICLR 2025)](https://proceedings.iclr.cc/paper_files/paper/2025/hash/c40bed606c51c8e827c1ba75aa2da054-Abstract-Conference.html)
- [Inference-Aware Fine-Tuning (OpenReview)](https://openreview.net/forum?id=77gQUdQhE7)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b82a4e7c-e871-4a3f-a8e9-83ac558d7df3",
  "isSidechain": true,
  "agentId": "aef7cd42e386f60aa",
  "requestId": "req_011CbTVvMy9ZT7MJCGzCoduE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f980653b-2682-4414-853f-72150dbe4baf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8280eabe-3ac4-4f74-b6f8-8256a49b890b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019HKVJkT6zV8NGmNeRL8Xaq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1732,
      "cache_read_input_tokens": 16867,
      "output_tokens": 3047,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1732
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3047,
          "cache_read_input_tokens": 16867,
          "cache_creation_input_tokens": 1732,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1732,
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
