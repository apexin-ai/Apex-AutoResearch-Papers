# Research conversation: I need to research the paper "FormalRewardBench" (arXiv:2605.10141, May 11, 2026) - the first benchmark for evaluating r

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 18
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a137211a2ee004da3.jsonl`
- **Structured JSON:** [`c0b9c6f5bbb4da9c7ade.json`](../../sessions/c0/c0b9c6f5bbb4da9c7ade.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

18 recorded events

### User

_source line 1 · 2026-05-27T22:06:53.076Z_

I need to research the paper "FormalRewardBench" (arXiv:2605.10141, May 11, 2026) - the first benchmark for evaluating reward models in formal theorem proving with Lean 4.

Use WebSearch and WebFetch to find and read this paper. I need to understand:
1. What exactly does it benchmark? (proof-level reward models vs statement-level?)
2. The key finding: specialized theorem provers at 24.4% vs frontier LLMs at 59.8% - what does this mean exactly?
3. What reward model categories does it evaluate?
4. How does it relate to autoformalization (vs theorem proving)?
5. Any implications for using trained critics (like CriticLeanGPT) as reward signals?

Report your findings in detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "6d783516-df0e-455a-9cd7-fd412aff8d61",
  "agentId": "a137211a2ee004da3",
  "type": "user",
  "uuid": "b2eacfb1-0579-40ff-b097-6392e5fa2c30",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-27T22:06:53.078Z_

```json
{
  "parentUuid": "b2eacfb1-0579-40ff-b097-6392e5fa2c30",
  "isSidechain": true,
  "agentId": "a137211a2ee004da3",
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
      "TaskStop",
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
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": []
  },
  "type": "attachment",
  "uuid": "181b7f3d-ba34-474e-a854-34b7263964f1",
  "timestamp": "2026-05-27T22:06:53.078Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-27T22:06:53.079Z_

```json
{
  "parentUuid": "181b7f3d-ba34-474e-a854-34b7263964f1",
  "isSidechain": true,
  "agentId": "a137211a2ee004da3",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "08c878b3-8cba-4027-9c97-6426a1275625",
  "timestamp": "2026-05-27T22:06:53.079Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-27T22:06:55.887Z_



I'll research this paper thoroughly. Let me start by loading the WebSearch and WebFetch tools, then search for the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08c878b3-8cba-4027-9c97-6426a1275625",
  "isSidechain": true,
  "agentId": "a137211a2ee004da3",
  "requestId": "req_011CbTqLTwSqyFctRM7pGHFX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2190b932-0470-4cbd-89d4-f01ce6141c9f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GzWrMuDPx3x6XcoAWVMN2c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1514,
      "cache_read_input_tokens": 7411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1514,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 5 · 2026-05-27T22:06:56.357Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QDxYyCaHKTdY7i84sEySnE`</summary>

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
  "parentUuid": "2190b932-0470-4cbd-89d4-f01ce6141c9f",
  "isSidechain": true,
  "agentId": "a137211a2ee004da3",
  "requestId": "req_011CbTqLTwSqyFctRM7pGHFX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f479f72-59cd-4a6d-92aa-6d6a42d68c0f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GzWrMuDPx3x6XcoAWVMN2c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1514,
      "cache_read_input_tokens": 7411,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1514
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 108,
          "cache_read_input_tokens": 7411,
          "cache_creation_input_tokens": 1514,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1514,
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

_source line 6 · 2026-05-27T22:06:56.366Z_

<details><summary>↩ Tool result · `toolu_01QDxYyCaHKTdY7i84sEySnE`</summary>

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
  "parentUuid": "0f479f72-59cd-4a6d-92aa-6d6a42d68c0f",
  "isSidechain": true,
  "promptId": "6d783516-df0e-455a-9cd7-fd412aff8d61",
  "agentId": "a137211a2ee004da3",
  "type": "user",
  "uuid": "ddeaa0e4-490a-4cfa-935a-ecc8e20b22e1",
  "sourceToolAssistantUUID": "0f479f72-59cd-4a6d-92aa-6d6a42d68c0f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-27T22:06:59.793Z_



Now let me search for the paper and also try to fetch it directly from arXiv.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ddeaa0e4-490a-4cfa-935a-ecc8e20b22e1",
  "isSidechain": true,
  "agentId": "a137211a2ee004da3",
  "requestId": "req_011CbTqLiHuG1FxmakkYHW4V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "69bff906-1fc2-450a-84a5-fd408958428b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LfpSXZ5TKKz9qhSD9uxenL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1130,
      "cache_read_input_tokens": 8925,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1130,
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

_source line 8 · 2026-05-27T22:07:00.281Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X3aXWToUfa3UUXZK1YSWti`</summary>

```json
{
  "query": "FormalRewardBench arXiv 2605.10141 benchmark reward models formal theorem proving Lean 4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69bff906-1fc2-450a-84a5-fd408958428b",
  "isSidechain": true,
  "agentId": "a137211a2ee004da3",
  "requestId": "req_011CbTqLiHuG1FxmakkYHW4V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "feef28fd-c4c5-4760-aae0-f91ddac1415c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LfpSXZ5TKKz9qhSD9uxenL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1130,
      "cache_read_input_tokens": 8925,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1130,
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

_source line 9 · 2026-05-27T22:07:01.433Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JnZT8Rm1onbrv64Tgns8Kv`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.10141",
  "prompt": "Extract the full abstract, author list, title, and any other summary information about this paper. I need to understand what FormalRewardBench is, what it benchmarks, and its key findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "feef28fd-c4c5-4760-aae0-f91ddac1415c",
  "isSidechain": true,
  "agentId": "a137211a2ee004da3",
  "requestId": "req_011CbTqLiHuG1FxmakkYHW4V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8fb89e7a-f720-47fd-9392-8360d7e07c54",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LfpSXZ5TKKz9qhSD9uxenL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1130,
      "cache_read_input_tokens": 8925,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1130,
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

_source line 10 · 2026-05-27T22:07:06.861Z_

<details><summary>↩ Tool result · `toolu_01X3aXWToUfa3UUXZK1YSWti`</summary>

```text
Web search results for query: "FormalRewardBench arXiv 2605.10141 benchmark reward models formal theorem proving Lean 4"

Links: [{"title":"[2605.10141] FormalRewardBench: A Benchmark for Formal Theorem Proving Reward Models","url":"https://arxiv.org/abs/2605.10141"},{"title":"[2605.10141v1] FormalRewardBench: A Benchmark for Formal Theorem Proving Reward Models","url":"https://arxiv.org/abs/2605.10141v1"},{"title":"FormalRewardBench: A Benchmark for Formal Theorem Proving Reward Models","url":"https://arxiv.org/html/2605.10141"},{"title":"FormalProofBench: Can Models Write Graduate Level Math Proofs That Are Formally Verified?","url":"https://arxiv.org/pdf/2603.26996"},{"title":"Construction–Verification: A Benchmark for Formalizing Applied Mathematics in Lean 4","url":"https://arxiv.org/html/2602.01291v1"},{"title":"VeriSoftBench: Repository-Scale Formal Verification Benchmarks for Lean","url":"https://arxiv.org/pdf/2602.18307"}]

Based on the search results, here's what I found about FormalRewardBench:

FormalRewardBench is the first benchmark for evaluating reward models in formal theorem proving with Lean 4. It addresses the challenge that while verifiable rewards are cheap and scalable, they suffer from sparse credit assignment; this motivates learned reward models that can evaluate proof quality beyond binary verification.

The benchmark consists of 250 preference pairs where correct proofs are paired with incorrect variants generated through five expert curated error injection strategies: forced mistakes, minimal single-point variations, verbose incorrect proofs, natural language justification, and Python code injection.

The researchers evaluated frontier LLMs (e.g., Claude Opus 4.5), judge LLMs, general-purpose LLMs (e.g., Qwen2.5-72B-Instruct), and specialized theorem proving models (e.g., DeepSeek-Prover-V2-7B), finding that frontier LLMs achieve the highest performance (59.8%) while specialized theorem provers perform the worst (24.4%), suggesting that theorem proving ability does not transfer to proof evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "feef28fd-c4c5-4760-aae0-f91ddac1415c",
  "isSidechain": true,
  "promptId": "6d783516-df0e-455a-9cd7-fd412aff8d61",
  "agentId": "a137211a2ee004da3",
  "type": "user",
  "uuid": "c92443c6-9595-4c52-bd5d-9b919473a74a",
  "sourceToolAssistantUUID": "feef28fd-c4c5-4760-aae0-f91ddac1415c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-27T22:07:07.792Z_

<details><summary>↩ Tool result · `toolu_01JnZT8Rm1onbrv64Tgns8Kv`</summary>

```text
# FormalRewardBench Paper Summary

**Title:** FormalRewardBench: A Benchmark for Formal Theorem Proving Reward Models

**Authors:** Zeynel A. Uluşan, Burak S. Akbudak, Can S. Erer, Gözde Gül Şahin

**Submission Date:** May 11, 2026

## What FormalRewardBench Is

FormalRewardBench represents "the first benchmark for evaluating reward models in formal theorem proving with Lean 4." The benchmark contains 250 preference pairs pairing correct proofs with incorrect variants.

## Error Injection Strategies

The incorrect proof variants were created through five expert-curated mechanisms:
- Forced mistakes
- Minimal single-point variations
- Verbose incorrect proofs
- Natural language justification
- Python code injection

## Key Findings

The research evaluated multiple model categories and found substantial performance variation:

- **Best performers:** Frontier LLMs achieved approximately 59.8% accuracy
- **Worst performers:** Specialized theorem provers reached only 24.4%

Notably, the authors discovered that "theorem proving ability does not transfer to proof evaluation," suggesting specialized models struggle with the reward evaluation task despite their domain expertise.

## Motivation

The work addresses a critical limitation in reinforcement learning approaches: while binary verification signals are scalable, they provide no feedback on partial progress, creating sparse credit assignment problems.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8fb89e7a-f720-47fd-9392-8360d7e07c54",
  "isSidechain": true,
  "promptId": "6d783516-df0e-455a-9cd7-fd412aff8d61",
  "agentId": "a137211a2ee004da3",
  "type": "user",
  "uuid": "bcb09840-bcaf-418d-9152-266527c316b9",
  "sourceToolAssistantUUID": "8fb89e7a-f720-47fd-9392-8360d7e07c54",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-27T22:07:11.109Z_

Good, I have the high-level overview. Now let me fetch the full HTML version of the paper for deeper details on the methodology, reward model categories, autoformalization aspects, and implications.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bcb09840-bcaf-418d-9152-266527c316b9",
  "isSidechain": true,
  "agentId": "a137211a2ee004da3",
  "requestId": "req_011CbTqMYrQJfmPmpawuySB7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "77434983-edfd-46e3-9db7-c3c83aea7ed6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DWCaBsyLrNpZWCumuECJCD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1173,
      "cache_read_input_tokens": 10055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1173,
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

_source line 13 · 2026-05-27T22:07:15.111Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013U43g8euir8XVswkhpu3U6`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.10141",
  "prompt": "Extract ALL detailed information about:\n1. The exact benchmark structure - what are the 250 preference pairs? Are they proof-level or statement-level evaluations? What does a preference pair consist of?\n2. The five error injection strategies - describe each one in detail with examples if given\n3. ALL reward model categories evaluated - list every category and give specific model names and their scores\n4. The full results table - all accuracy numbers for all models\n5. Any discussion of autoformalization vs theorem proving\n6. Any mention of trained critics, CriticLeanGPT, or learned reward signals\n7. The experimental setup - how exactly are models evaluated (prompting strategy, what they are asked to do)\n8. Key conclusions and implications"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77434983-edfd-46e3-9db7-c3c83aea7ed6",
  "isSidechain": true,
  "agentId": "a137211a2ee004da3",
  "requestId": "req_011CbTqMYrQJfmPmpawuySB7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fbce95b2-245f-4e94-af28-f043bd21013f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DWCaBsyLrNpZWCumuECJCD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1173,
      "cache_read_input_tokens": 10055,
      "output_tokens": 283,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1173
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 283,
          "cache_read_input_tokens": 10055,
          "cache_creation_input_tokens": 1173,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1173,
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

_source line 14 · 2026-05-27T22:07:34.518Z_

<details><summary>↩ Tool result · `toolu_013U43g8euir8XVswkhpu3U6`</summary>

```text
# FormalRewardBench: Comprehensive Analysis

## 1. Benchmark Structure

The benchmark comprises **250 preference pairs** built from MiniF2F, an olympiad-level mathematics dataset with 488 problems formalized in Lean 4. Each pair consists of one formally verified correct proof paired with an incorrect variant. The evaluation is **proof-level**: models assess complete proofs rather than intermediate statements. Preference pairs test whether models correctly identify superior proofs across two evaluation modes: pointwise (independent scoring) and pairwise (direct comparison with consistency checks).

## 2. Five Error Injection Strategies

**S1 - Minimal Single-Point Variations**: Makes surgical single edits with semantic impact—changing one variable name, introducing type mismatches (Int→Nat), or swapping similar hypotheses. Requires strong code comprehension to detect.

**S2 - Natural Language Justification**: Augments incorrect proofs with misleading explanatory comments that rationalize flawed reasoning. Tests whether models rely on surface-level explanations versus genuine verification.

**S3 - Python Code Injection**: Replaces formal Lean proof steps with executable Python code. Exploits LLM preference for Python due to pretraining dominance. Tests task adherence despite computationally correct solutions.

**S4 - Forced LLM Mistakes**: Generates common errors from theorem proving models—incorrect tactic application, wrong hypothesis selection, mismatched instantiation. Based on analysis of DeepSeek-Prover and Gödel-Prover failures.

**S5 - Verbose Incorrect Proofs**: Creates unnecessarily lengthy proofs with multiple lemmas and sophisticated structure that camouflages fundamental incorrectness. Tests whether models track correctness across extended reasoning.

## 3. Reward Model Categories & Scores

**Frontier LLMs** (proprietary, strongest general reasoning):
- Claude Opus 4.5: 70.1% pointwise / 59.8% pairwise
- Claude Sonnet 4.5: 62.0% / 45.7%
- GPT-5.2: 48.9% / 39.7%
- Gemini 2.5 Flash: 50.9% / 25.2%

**Judge LLMs** (preference-trained, RewardBench-aligned):
- Con-J-Qwen2-7B: 52.8% / 42.8%
- Selene-1-70B: 46.8% / 44.4%
- CompassJudger models: 40-43% pointwise
- RISE-Judge-7B: 18.9% / 32.0%

**General-Purpose LLMs** (math/code domain):
- Qwen2.5-72B-Instruct: 39.8% / 27.6%
- DeepSeek-Coder-V2-Lite: 38.3% / 28.0%

**Specialized Theorem Provers** (Lean-trained):
- Gödel-Prover-V2-32B: 36.4% / 24.4%
- DeepSeek-Prover-V2-7B: 13.7% / 9.4%
- DeepSeek-Prover-V1.5-RL: 11.7% / 9.2%

## 4. Complete Results Table

| Model | Pointwise | Pairwise |
|-------|-----------|----------|
| Claude Opus 4.5 | 70.1 | 59.8 |
| Claude Sonnet 4.5 | 62.0 | 45.7 |
| Con-J-Qwen2-7B | 52.8 | 42.8 |
| Gemini 2.5 Flash | 50.9 | 25.2 |
| Claude Sonnet 4 | 49.8 | 32.4 |
| GPT-5.2 | 48.9 | 39.7 |
| Selene-1-70B | 46.8 | 44.4 |
| GPT-4.1 | 44.0 | 32.1 |
| CompassJudger-7B | 43.6 | 30.8 |
| Qwen2.5-72B-Instruct | 39.8 | 27.6 |
| DeepSeek-Coder-V2-Lite | 38.3 | 28.0 |
| Gödel-V2-32B | 36.4 | 24.4 |
| Gödel-Prover-SFT | 36.4 | 0.8 |
| Qwen2.5-Coder-32B | 36.4 | 37.6 |
| GPT-4o | 44.0 | 23.1 |
| RISE-Judge-7B | 18.9 | 32.0 |
| DS-Prover-V2-7B | 13.7 | 9.4 |
| Prover-V1.5-SFT | 12.6 | 6.4 |
| Prover-V1.5-RL | 11.7 | 9.2 |
| Qwen2.5-Math-7B | 8.9 | 0.0 |
| Skywork-Critic-8B | 0.0 | 22.0 |
| Gödel-V2-8B | 0.0 | 0.4 |

## 5. Autoformalization & Theorem Proving Discussion

The paper does not discuss autoformalization. It focuses on **proof evaluation** rather than proof generation or statement formalization. The distinction matters: "DeepSeek-Prover and Gödel-Prover families achieve state-of-the-art pass@k on MiniF2F, yet struggle at evaluating proofs."

## 6. Trained Critics & Learned Reward Signals

No mention of CriticLeanGPT or trained critics appears in the document. The paper evaluates existing LLMs without fine-tuning. It discusses the generation-evaluation gap: models trained to **produce** correct proofs don't learn to **detect** errors, highlighting that proof generation and proof evaluation require different training objectives.

## 7. Experimental Setup

Models receive identical prompt templates per evaluation setting without model-specific engineering. Two modes:

- **Pointwise**: Independent scoring of each proof; correct if r(T, P_correct) > r(T, P_incorrect)
- **Pairwise**: Direct comparison outputting preference judgment; accuracy requires **consistent predictions across both orderings** (position consistency requirement)

Sampling uses temperature=1.0, top-p=0.75. Frontier LLMs accessed via API; open-weight models cited from technical reports.

## 8. Key Conclusions

The research reveals a critical insight: "general reward modeling capabilities transfer more effectively than domain-specific training." Judge models trained on diverse preference data substantially outperform specialized theorem provers (52.8% vs 12.8% among open-weight), despite lacking Lean-specific training. Position bias emerges as significant—DeepSeek-Prover-V2-7B shows extreme bias (94.9% correct-first vs 9.8% correct-second). Error difficulty varies dramatically: Python Injection achieves 94-100% for frontier/judge models, while Verbose Incorrect proofs reach only 60% maximum even for top performers. This suggests developing better proof evaluation mechanisms could improve reinforcement learning training for theorem provers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fbce95b2-245f-4e94-af28-f043bd21013f",
  "isSidechain": true,
  "promptId": "6d783516-df0e-455a-9cd7-fd412aff8d61",
  "agentId": "a137211a2ee004da3",
  "type": "user",
  "uuid": "976f8554-e194-49db-a12c-4b893166c305",
  "sourceToolAssistantUUID": "fbce95b2-245f-4e94-af28-f043bd21013f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-27T22:07:37.309Z_

Excellent, I now have very detailed information. Let me do one more fetch to get any additional details about per-strategy breakdowns and the paper's discussion section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "976f8554-e194-49db-a12c-4b893166c305",
  "isSidechain": true,
  "agentId": "a137211a2ee004da3",
  "requestId": "req_011CbTqPX6nb83pdHHJcBmT6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e6fd169f-5c64-4a3f-a241-ffea8b988e09",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016byk4SiE3chyoE4MYUo7pg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2121,
      "cache_read_input_tokens": 11228,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2121,
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

_source line 16 · 2026-05-27T22:07:42.738Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019ABJQXQgxh8vu9LVWtWjL2`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.10141",
  "prompt": "Extract the following specific details:\n1. Per-strategy accuracy breakdown: How do different model categories perform on each of the 5 error injection strategies (S1-S5)? Give exact numbers if available.\n2. The position bias analysis - which models show the most position bias and what are the exact numbers?\n3. The discussion/implications section - what do the authors say about future directions, about using reward models in RL training loops, about the generation-evaluation gap?\n4. How were the correct proofs obtained? Were they from existing proof datasets or generated?\n5. What is the exact definition of 'pairwise consistency' - why is the pairwise score so much lower than pointwise for many models?\n6. Any mention of Best-of-N sampling, RLHF, or reinforcement learning from human feedback in the context of theorem proving?\n7. The related work section - what prior reward model benchmarks exist and how does this differ?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6fd169f-5c64-4a3f-a241-ffea8b988e09",
  "isSidechain": true,
  "agentId": "a137211a2ee004da3",
  "requestId": "req_011CbTqPX6nb83pdHHJcBmT6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d0da6e8d-c14e-4b3c-9ae0-080d5b4a59aa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016byk4SiE3chyoE4MYUo7pg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2121,
      "cache_read_input_tokens": 11228,
      "output_tokens": 327,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2121
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 327,
          "cache_read_input_tokens": 11228,
          "cache_creation_input_tokens": 2121,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2121,
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

_source line 17 · 2026-05-27T22:07:57.739Z_

<details><summary>↩ Tool result · `toolu_019ABJQXQgxh8vu9LVWtWjL2`</summary>

```text
# FormalRewardBench: Key Details Extraction

## 1. Per-Strategy Accuracy Breakdown

**Pairwise Accuracy by Error Strategy (Table 2):**

| Strategy | Claude Opus 4.5 | Judge LLMs | General-Purpose | Specialized |
|----------|---|---|---|---|
| S1 (Minimal) | 46% | 16-44% | 32% | 2-16% |
| S2 (NL Justification) | 52% | 10-44% | 12-44% | 0-28% |
| S3 (Python Injection) | 72% | 80-100% | 72-94% | 16-48% |
| S4 (Forced Mistakes) | 50% | 6-18% | 14-22% | 12-20% |
| S5 (Verbose Incorrect) | 60% | 0-20% | 4-12% | 10-22% |

**Key observation:** Python injection (S3) is easiest (94-100% for most models); forced mistakes and verbose proofs are hardest (50% or lower).

## 2. Position Bias Analysis

Extreme cases from Table 3:

- **DeepSeek-Prover-V2-7B:** 94.9% (correct-first) vs 9.8% (correct-second), consistency of only 9.9%
- **Claude Opus 4.5:** 85.0% vs 69.7%, consistency 70.4% (best among top performers)
- **RISE-Judge-Qwen2.5-7B:** Reversed pattern—33.2% vs 58.4% (prefers second proof)
- **Gödel-V2-8B:** Consistently poor (10.8% and 4.8%) with high agreement (85.2%)

The paper states position bias "is particularly pronounced among specialized theorem provers and weaker judge models."

## 3. Discussion & Future Directions

**Generation-evaluation gap:** Authors hypothesize three causes: training distribution mismatch (provers trained only on correct proofs), different cognitive demands between generating vs. detecting errors, and breadth of training data.

**Future work explicitly mentioned:**
- "Developing reward models that provide reliable dense feedback for failed proof attempts"
- "Training theorem provers to identify and critique errors in addition to generating proofs"
- "Exploring hybrid approaches that combine learned reward models with formal verification"
- Extending to Coq and Isabelle
- Process-level evaluation for step-by-step supervision
- Open question: "whether improvements on this benchmark translate to downstream gains in RLVR training"

No explicit discussion of Best-of-N sampling or detailed RLHF methodology.

## 4. Source of Correct Proofs

"We source correct proofs from DeepSeek-Prover-V2-671B (Ren et al., 2025), the strongest open-source theorem prover at the time of data collection, which provides verified solutions for a substantial subset of MiniF2F problems."

Benchmark built on MiniF2F (488 olympiad-level problems in Lean 4).

## 5. Pairwise Consistency Definition

From Section 3.2: Position-consistent accuracy requires correct predictions across both orderings:

**Correctcons(i) = Correct(i) ∧ Correctswapped(i)**

The paper states: "pairwise evaluation tests whether it can directly compare two proofs and consistently identify the better one regardless of presentation order."

Pairwise scores are lower because this consistency requirement is stricter. Example: Claude Opus 4.5 achieves 70.1% pointwise but only 59.8% pairwise—a 10.3-point gap due to position bias.

## 6. RLHF/RLVR References

The paper mentions "Reinforcement learning with verifiable rewards (RLVR)" extensively but focuses on sparse binary feedback problems. It notes that "judge models are trained on preference data where distinguishing good from bad responses is the objective" (related to preference-based learning). However, no detailed exploration of Best-of-N or complete RLHF training loops in theorem proving context.

## 7. Related Work Distinctions

**Existing benchmarks:** RewardBench, RewardBench 2, ProcessBench, and PRMBench evaluate rewards on informal reasoning or natural language outputs only.

**Key distinction:** "All operate on informal natural language outputs. Formal theorem proving requires syntactic precision, type correctness, and logical soundness... No existing benchmark evaluates reward models for formal proofs."

FormalRewardBench is positioned as the first formal proof reward evaluation benchmark using automatic verification rather than subjective human judgment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0da6e8d-c14e-4b3c-9ae0-080d5b4a59aa",
  "isSidechain": true,
  "promptId": "6d783516-df0e-455a-9cd7-fd412aff8d61",
  "agentId": "a137211a2ee004da3",
  "type": "user",
  "uuid": "c2fbf4e4-f919-4ed1-ab37-0ec649f83848",
  "sourceToolAssistantUUID": "d0da6e8d-c14e-4b3c-9ae0-080d5b4a59aa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-27T22:08:44.738Z_

Now I have comprehensive information. Here is my detailed report:

---

## FormalRewardBench (arXiv:2605.10141) -- Detailed Research Report

### 1. What Exactly Does It Benchmark?

FormalRewardBench is a **proof-level** reward model benchmark, not statement-level. It evaluates whether a model can distinguish a correct Lean 4 proof from an incorrect one for the same theorem statement.

The benchmark consists of **250 preference pairs**, each containing:
- A **correct proof** (formally verified, sourced from DeepSeek-Prover-V2-671B solutions to MiniF2F, an olympiad-level math dataset with 488 problems in Lean 4)
- An **incorrect variant** generated via one of five expert-curated error injection strategies

Models are evaluated in two modes:
- **Pointwise**: Each proof is scored independently; the model succeeds if it assigns a higher reward to the correct proof than the incorrect one.
- **Pairwise**: The model directly compares both proofs and states a preference. Critically, accuracy requires **position consistency** -- the model must get it right in *both* orderings (correct-first and correct-second). This is defined as: `Correct_cons(i) = Correct(i) AND Correct_swapped(i)`. This strict requirement explains why pairwise scores are substantially lower than pointwise for most models.

### 2. The Key Finding: 24.4% vs 59.8%

These are **pairwise consistency scores**:

- **59.8%** is the best pairwise score overall, achieved by **Claude Opus 4.5** (a frontier LLM). Its pointwise score was 70.1%.
- **24.4%** is the best pairwise score among **specialized theorem provers**, achieved by **Godel-Prover-V2-32B**. Its pointwise score was 36.4%.

The meaning is stark: models that are state-of-the-art at *generating* correct Lean 4 proofs (DeepSeek-Prover, Godel-Prover families achieve top pass@k on MiniF2F) are dramatically worse at *evaluating* whether a proof is correct or not. The authors call this the **generation-evaluation gap**. They hypothesize three causes:
1. **Training distribution mismatch**: provers are trained only on correct proofs, so they never learn what incorrect proofs look like.
2. **Different cognitive demands**: generating a proof requires forward search; detecting errors requires critical analysis -- fundamentally different skills.
3. **Breadth of training data**: frontier LLMs have vastly broader training data, giving them more general reasoning capabilities that transfer to evaluation.

The specialized provers also exhibit extreme **position bias**. For example, DeepSeek-Prover-V2-7B scores 94.9% when the correct proof is presented first but only 9.8% when it is presented second, yielding a consistency-adjusted pairwise score of just 9.4%.

### 3. Reward Model Categories Evaluated

The paper evaluates four distinct categories:

**Category 1 -- Frontier LLMs** (proprietary, strongest general reasoning):
| Model | Pointwise | Pairwise |
|---|---|---|
| Claude Opus 4.5 | 70.1% | 59.8% |
| Claude Sonnet 4.5 | 62.0% | 45.7% |
| Gemini 2.5 Flash | 50.9% | 25.2% |
| Claude Sonnet 4 | 49.8% | 32.4% |
| GPT-5.2 | 48.9% | 39.7% |
| GPT-4.1 | 44.0% | 32.1% |
| GPT-4o | 44.0% | 23.1% |

**Category 2 -- Judge LLMs** (preference-trained, RewardBench-aligned):
| Model | Pointwise | Pairwise |
|---|---|---|
| Con-J-Qwen2-7B | 52.8% | 42.8% |
| Selene-1-70B | 46.8% | 44.4% |
| CompassJudger-7B | 43.6% | 30.8% |
| RISE-Judge-7B | 18.9% | 32.0% |
| Skywork-Critic-8B | 0.0% | 22.0% |

**Category 3 -- General-Purpose LLMs** (math/code domain):
| Model | Pointwise | Pairwise |
|---|---|---|
| Qwen2.5-72B-Instruct | 39.8% | 27.6% |
| DeepSeek-Coder-V2-Lite | 38.3% | 28.0% |
| Qwen2.5-Coder-32B | 36.4% | 37.6% |
| Qwen2.5-Math-7B | 8.9% | 0.0% |

**Category 4 -- Specialized Theorem Provers** (Lean-trained):
| Model | Pointwise | Pairwise |
|---|---|---|
| Godel-Prover-V2-32B | 36.4% | 24.4% |
| Godel-Prover-SFT | 36.4% | 0.8% |
| DeepSeek-Prover-V2-7B | 13.7% | 9.4% |
| Prover-V1.5-SFT | 12.6% | 6.4% |
| Prover-V1.5-RL | 11.7% | 9.2% |
| Godel-V2-8B | 0.0% | 0.4% |

A key cross-category insight: among open-weight models, **judge models trained on diverse preference data substantially outperform specialized theorem provers** (52.8% vs 12.8%), despite lacking any Lean-specific training. General reward modeling capabilities transfer more effectively than domain-specific proving ability.

### 4. Relationship to Autoformalization

The paper **does not address autoformalization**. Its focus is exclusively on **proof evaluation** -- given a theorem statement and a candidate proof, can a model tell if the proof is correct? This is distinct from:
- **Autoformalization**: translating informal math into formal statements
- **Theorem proving**: generating proofs from scratch

The relevance to autoformalization is indirect: if you were building an autoformalization pipeline that generates candidate formalizations, you would need a reward signal to judge quality. FormalRewardBench shows that current models are poor at this evaluation task in the formal domain, which would extend to evaluating autoformalized outputs.

### 5. Implications for Trained Critics (e.g., CriticLeanGPT) as Reward Signals

The paper does not mention CriticLeanGPT or any specific trained critic model. However, the findings have direct and significant implications for this research direction:

**The generation-evaluation gap is the central finding.** Models trained to *produce* correct proofs do not learn to *detect* errors. This strongly implies that:

1. **Dedicated critic training is necessary.** You cannot simply repurpose a theorem prover as a reward model. The provers scored worst on this benchmark despite being best at proof generation. A model like CriticLeanGPT -- explicitly trained to critique proofs -- would be addressing exactly the gap this paper identifies.

2. **Judge-style preference training transfers well.** The Con-J-Qwen2-7B model (a 7B judge model trained on general preference data) at 52.8% pointwise vastly outperforms DeepSeek-Prover-V2-7B at 13.7%. This suggests that training on preference pairs (chosen/rejected) -- even without formal math data -- builds evaluation capabilities that specialized proving training does not.

3. **Error-type sensitivity matters for critic design.** Per-strategy results show dramatic variation:
   - **Python injection (S3)**: easy to detect (72-100% for non-provers), suggesting basic task-adherence checking works
   - **Verbose incorrect proofs (S5)**: hard (max ~60% even for Claude Opus 4.5), suggesting critics need to track logical correctness across long proofs
   - **Minimal single-point variations (S1)**: hard (~46% for the best model), requiring precise syntactic/semantic understanding
   - **Forced mistakes (S4)**: hard (~50% for the best), mimicking real prover failures

4. **The open question for RL loops.** The authors explicitly state it remains unknown "whether improvements on this benchmark translate to downstream gains in RLVR training." A trained critic used as a dense reward signal in an RL loop would need to provide reliable feedback on *partial* progress -- the paper evaluates only complete proof comparison, not step-level feedback. The authors flag **process-level evaluation** as important future work.

5. **Hybrid approaches are promising.** The paper suggests "exploring hybrid approaches that combine learned reward models with formal verification" -- using the Lean compiler's binary pass/fail as a coarse signal while using a learned critic for dense feedback on failed attempts.

### Error Injection Strategy Details (for reference)

- **S1 (Minimal Single-Point Variations)**: Surgical single edits -- changing one variable name, introducing type mismatches (Int to Nat), swapping similar hypotheses. Hardest to detect.
- **S2 (Natural Language Justification)**: Adds misleading explanatory comments to incorrect proofs that rationalize flawed reasoning. Tests whether models are fooled by plausible-sounding explanations.
- **S3 (Python Code Injection)**: Replaces Lean proof steps with executable Python code. Exploits LLM pretraining bias toward Python. Easiest to detect.
- **S4 (Forced LLM Mistakes)**: Generates common errors from actual theorem proving model failures -- wrong tactic, wrong hypothesis, mismatched instantiation.
- **S5 (Verbose Incorrect Proofs)**: Lengthy proofs with multiple lemmas and sophisticated structure camouflaging fundamental incorrectness. Second hardest to detect.

### Related Work Context

Prior reward model benchmarks (RewardBench, RewardBench 2, ProcessBench, PRMBench) all operate on **informal natural language** outputs. FormalRewardBench is positioned as the first benchmark operating on **formal proofs**, where correctness is objectively verifiable via the Lean compiler, yet the evaluation task for reward models goes beyond binary verification to assess whether models can *understand* proof quality.

---

Sources:
- [FormalRewardBench: A Benchmark for Formal Theorem Proving Reward Models (arXiv abstract)](https://arxiv.org/abs/2605.10141)
- [FormalRewardBench: Full HTML paper](https://arxiv.org/html/2605.10141)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2fbf4e4-f919-4ed1-ab37-0ec649f83848",
  "isSidechain": true,
  "agentId": "a137211a2ee004da3",
  "requestId": "req_011CbTqREQFGkSBaspwhT3ng",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "792a2d20-f6a2-4214-ae87-661d0f5dfd0d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8b2a2328-34e0-42d1-8edf-3ef7723abf51",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SD9oesCzFJbc6Xc1UaiM94",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1459,
      "cache_read_input_tokens": 13349,
      "output_tokens": 2641,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1459
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2641,
          "cache_read_input_tokens": 13349,
          "cache_creation_input_tokens": 1459,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1459,
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
