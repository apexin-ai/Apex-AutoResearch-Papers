# Research conversation: Research "Think-RM" - a reward model that achieves SOTA on RM-Bench via long-horizon reasoning in generative reward mode

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ae0e3790c0ea07cd1.jsonl`
- **Structured JSON:** [`f9110cc8aa0895277d25.json`](../../sessions/f9/f9110cc8aa0895277d25.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

21 recorded events

### User

_source line 1 · 2026-05-27T18:59:27.239Z_

Research "Think-RM" - a reward model that achieves SOTA on RM-Bench via long-horizon reasoning in generative reward models with RLHF training. It was apparently published at NeurIPS 2025. I need to understand:
1. What exactly does Think-RM do? How does it use long-horizon reasoning?
2. What training approach does it use (RLHF, RL, SFT)?
3. Does it address calibration?
4. What are its key results and which benchmarks?
5. How does it relate to process reward models / step-level verification?
6. Does it use advantage functions?

Search using multiple queries:
- "Think-RM NeurIPS 2025 reward model reasoning"
- "Think-RM long-horizon generative reward model RLHF"
- "Think-RM RM-Bench state of the art"

Read the actual paper if you can find it on arxiv or openreview. Report in detail (300-400 words).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c5cb5cdd-3dff-45de-89b1-a6d7b6dd5ec9",
  "agentId": "ae0e3790c0ea07cd1",
  "type": "user",
  "uuid": "741a55e4-4aa3-4e2e-a063-511649016293",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "dcea932a-9616-44e0-aedf-dc75f9c4b48a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-27T18:59:27.242Z_

```json
{
  "parentUuid": "741a55e4-4aa3-4e2e-a063-511649016293",
  "isSidechain": true,
  "agentId": "ae0e3790c0ea07cd1",
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
  "uuid": "e233e535-e65c-4010-9027-b98d74c822d0",
  "timestamp": "2026-05-27T18:59:27.242Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "dcea932a-9616-44e0-aedf-dc75f9c4b48a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-27T18:59:27.242Z_

```json
{
  "parentUuid": "e233e535-e65c-4010-9027-b98d74c822d0",
  "isSidechain": true,
  "agentId": "ae0e3790c0ea07cd1",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5636c0b6-3810-40cc-bb60-dde62bca0a6e",
  "timestamp": "2026-05-27T18:59:27.242Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "dcea932a-9616-44e0-aedf-dc75f9c4b48a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-27T18:59:29.997Z_



I'll search for the Think-RM paper using multiple queries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5636c0b6-3810-40cc-bb60-dde62bca0a6e",
  "isSidechain": true,
  "agentId": "ae0e3790c0ea07cd1",
  "requestId": "req_011CbTb3VDz7M2J4e39NMish",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "38fab7da-680a-4886-b03e-b2c9937bed68",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "dcea932a-9616-44e0-aedf-dc75f9c4b48a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PQjy7gFdaHqDxhSeEeCtZ5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1573,
      "cache_read_input_tokens": 7411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1573,
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

_source line 5 · 2026-05-27T18:59:30.477Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012TdQ6PmXUPs7T5ZaQyMT17`</summary>

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
  "parentUuid": "38fab7da-680a-4886-b03e-b2c9937bed68",
  "isSidechain": true,
  "agentId": "ae0e3790c0ea07cd1",
  "requestId": "req_011CbTb3VDz7M2J4e39NMish",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5224df6b-7dde-4d8c-8f67-af12c103f1f8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "dcea932a-9616-44e0-aedf-dc75f9c4b48a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PQjy7gFdaHqDxhSeEeCtZ5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1573,
      "cache_read_input_tokens": 7411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1573,
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

_source line 6 · 2026-05-27T18:59:30.486Z_

<details><summary>↩ Tool result · `toolu_012TdQ6PmXUPs7T5ZaQyMT17`</summary>

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
  "parentUuid": "5224df6b-7dde-4d8c-8f67-af12c103f1f8",
  "isSidechain": true,
  "promptId": "c5cb5cdd-3dff-45de-89b1-a6d7b6dd5ec9",
  "agentId": "ae0e3790c0ea07cd1",
  "type": "user",
  "uuid": "3dfd9f14-fb12-480f-ae1d-ad76851ac0ca",
  "sourceToolAssistantUUID": "5224df6b-7dde-4d8c-8f67-af12c103f1f8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "dcea932a-9616-44e0-aedf-dc75f9c4b48a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-27T18:59:33.082Z_



Now let me run multiple searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3dfd9f14-fb12-480f-ae1d-ad76851ac0ca",
  "isSidechain": true,
  "agentId": "ae0e3790c0ea07cd1",
  "requestId": "req_011CbTb3k4htM7rzbcjz756f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1744111c-8ae9-4010-aeef-8a861ef17a5d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "dcea932a-9616-44e0-aedf-dc75f9c4b48a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5NePoxL93RkGoM6h7r6fR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1117,
      "cache_read_input_tokens": 8984,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1117,
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

_source line 8 · 2026-05-27T18:59:33.550Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JCTTrndbRQjLCvuCvvP93g`</summary>

```json
{
  "query": "Think-RM NeurIPS 2025 reward model reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1744111c-8ae9-4010-aeef-8a861ef17a5d",
  "isSidechain": true,
  "agentId": "ae0e3790c0ea07cd1",
  "requestId": "req_011CbTb3k4htM7rzbcjz756f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d85ed59-93b3-4fc6-b974-14403716dacf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "dcea932a-9616-44e0-aedf-dc75f9c4b48a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5NePoxL93RkGoM6h7r6fR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1117,
      "cache_read_input_tokens": 8984,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1117,
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

_source line 9 · 2026-05-27T18:59:34.020Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G1AvWqJVttJ3Zibwad785B`</summary>

```json
{
  "query": "Think-RM long-horizon generative reward model RLHF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d85ed59-93b3-4fc6-b974-14403716dacf",
  "isSidechain": true,
  "agentId": "ae0e3790c0ea07cd1",
  "requestId": "req_011CbTb3k4htM7rzbcjz756f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a4e502e-7f34-4efb-b685-e72108072e30",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "dcea932a-9616-44e0-aedf-dc75f9c4b48a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5NePoxL93RkGoM6h7r6fR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1117,
      "cache_read_input_tokens": 8984,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1117
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 174,
          "cache_read_input_tokens": 8984,
          "cache_creation_input_tokens": 1117,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1117,
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

_source line 10 · 2026-05-27T18:59:34.032Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QrBvRfBAN8cTZgTUT17kjS`</summary>

```json
{
  "query": "Think-RM RM-Bench state of the art"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a4e502e-7f34-4efb-b685-e72108072e30",
  "isSidechain": true,
  "agentId": "ae0e3790c0ea07cd1",
  "requestId": "req_011CbTb3k4htM7rzbcjz756f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad326ebb-b153-4085-8659-a6bf8b313aec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "dcea932a-9616-44e0-aedf-dc75f9c4b48a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5NePoxL93RkGoM6h7r6fR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1117,
      "cache_read_input_tokens": 8984,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1117
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 174,
          "cache_read_input_tokens": 8984,
          "cache_creation_input_tokens": 1117,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1117,
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

_source line 11 · 2026-05-27T18:59:40.823Z_

<details><summary>↩ Tool result · `toolu_01JCTTrndbRQjLCvuCvvP93g`</summary>

```text
Web search results for query: "Think-RM NeurIPS 2025 reward model reasoning"

Links: [{"title":"Think-RM: Enabling Long-Horizon Reasoning in Generative Reward Models | OpenReview","url":"https://openreview.net/forum?id=UfQAFbP6xq"},{"title":"GitHub - IlgeeHong/Think-RM: [NeurIPS 2025] Think-RM: Enabling Long-Horizon Reasoning in Generative Reward Models","url":"https://github.com/IlgeeHong/Think-RM"},{"title":"Think-RM: Enabling Long-Horizon Reasoning in Generative Reward Models","url":"https://openreview.net/pdf?id=UfQAFbP6xq"},{"title":"NeurIPS Poster Think-RM: Enabling Long-Horizon Reasoning in Generative Reward Models","url":"https://neurips.cc/virtual/2025/poster/117753"},{"title":"Think-RM: Enabling Long-Horizon Reasoning in Generative Reward Models","url":"https://think-rm.github.io/"},{"title":"NeurIPS Poster Reward Reasoning Models","url":"https://neurips.cc/virtual/2025/poster/117713"},{"title":"Think Twice: Branch-and-Rethink Reasoning Reward Model","url":"https://arxiv.org/pdf/2510.23596"},{"title":"RM-R1: Reward Modeling as Reasoning","url":"https://arxiv.org/pdf/2505.02387"},{"title":"Libra: Assessing and Improving Reward Model by Learning to Think","url":"https://arxiv.org/pdf/2507.21645"}]

Based on the search results, here's what I found about Think-RM:

## Overview

Think-RM is a training framework that enables long-horizon reasoning in generative reward models by modeling an internal thinking process. It was presented as a NeurIPS 2025 poster, and the work addresses key challenges in reinforcement learning from human feedback (RLHF).

## Problem It Solves

A core challenge in RLHF is constructing accurate reward signals, where conventional Bradley-Terry reward models often suffer from sensitivity to data size and coverage, as well as vulnerability to reward hacking. Existing generative reward models rely on shallow, vertically scaled reasoning, limiting their capacity to handle nuanced or complex tasks, and their pairwise preference outputs are incompatible with standard RLHF algorithms that require pointwise reward signals.

## Key Features

Rather than producing structured, externally provided rationales, Think-RM generates flexible, self-guided reasoning traces that support advanced capabilities such as self-reflection, hypothetical reasoning, and divergent reasoning.

To elicit these reasoning abilities, the model is first warmed-up by supervised fine-tuning over long CoT data, then further improved by rule-based reinforcement learning.

Additionally, a novel pairwise RLHF pipeline directly optimizes policies using pairwise preference rewards, eliminating the need for pointwise reward conversion.

The code, datasets, and models are publicly available on GitHub at https://github.com/IlgeeHong/Think-RM.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d85ed59-93b3-4fc6-b974-14403716dacf",
  "isSidechain": true,
  "promptId": "c5cb5cdd-3dff-45de-89b1-a6d7b6dd5ec9",
  "agentId": "ae0e3790c0ea07cd1",
  "type": "user",
  "uuid": "a216c646-25a9-48e8-b969-ee2a0ba2ec41",
  "sourceToolAssistantUUID": "5d85ed59-93b3-4fc6-b974-14403716dacf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "dcea932a-9616-44e0-aedf-dc75f9c4b48a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-27T18:59:40.951Z_

<details><summary>↩ Tool result · `toolu_01G1AvWqJVttJ3Zibwad785B`</summary>

```text
Web search results for query: "Think-RM long-horizon generative reward model RLHF"

Links: [{"title":"Paper page - Think-RM: Enabling Long-Horizon Reasoning in Generative Reward Models","url":"https://huggingface.co/papers/2505.16265"},{"title":"[2505.16265] Think-RM: Enabling Long-Horizon Reasoning in Generative Reward Models","url":"https://arxiv.org/abs/2505.16265"},{"title":"Think-RM: Enabling Long-Horizon Reasoning in Generative Reward Models","url":"https://arxiv.org/html/2505.16265v1"},{"title":"Think-RM: Enabling Long-Horizon Reasoning in Generative Reward Models | OpenReview","url":"https://openreview.net/forum?id=UfQAFbP6xq"},{"title":"NeurIPS Poster Think-RM: Enabling Long-Horizon Reasoning in Generative Reward Models","url":"https://neurips.cc/virtual/2025/poster/117753"},{"title":"Think-RM: Enabling Long-Horizon Reasoning in Generative Reward Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/think-rm-enabling-long-horizon-reasoning-generative"},{"title":"Think-RM: Enabling Long-Horizon Reasoning in Generative Reward Models","url":"https://openreview.net/pdf?id=UfQAFbP6xq"}]

Based on the search results, here's what Think-RM is:

## Overview

Think-RM is a training framework that enables long-horizon reasoning in generative reward models (GenRMs) by modeling an internal thinking process.

## Key Problem Being Addressed

A core challenge in RLHF is constructing accurate reward signals, where conventional Bradley-Terry reward models (BT RMs) often suffer from sensitivity to data size and coverage, as well as vulnerability to reward hacking. Existing GenRMs rely on shallow, vertically scaled reasoning, limiting their capacity to handle nuanced or complex (reasoning-intensive) tasks.

## How Think-RM Works

Rather than producing structured, externally provided rationales, Think-RM generates flexible, self-guided reasoning traces that support advanced capabilities such as self-reflection, hypothetical reasoning, and divergent reasoning. The models are first warmed-up by supervised fine-tuning (SFT) over long CoT (chain-of-thought) data, then further improved through rule-based reinforcement learning (RL).

## Novel RLHF Pipeline

Think-RM proposes a novel pairwise RLHF pipeline that directly optimizes policies using pairwise preference rewards, eliminating the need for pointwise reward conversion and enabling more effective use of Think-RM outputs.

## Results

Think-RM achieves state-of-the-art results on RM-Bench, outperforming both BT RM and vertically scaled GenRM by 8%, and when combined with the pairwise RLHF pipeline, demonstrates superior end-policy performance compared to traditional approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a4e502e-7f34-4efb-b685-e72108072e30",
  "isSidechain": true,
  "promptId": "c5cb5cdd-3dff-45de-89b1-a6d7b6dd5ec9",
  "agentId": "ae0e3790c0ea07cd1",
  "type": "user",
  "uuid": "ff23a6af-9141-4058-8a9c-386d2b5fab1e",
  "sourceToolAssistantUUID": "9a4e502e-7f34-4efb-b685-e72108072e30",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "dcea932a-9616-44e0-aedf-dc75f9c4b48a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-27T18:59:41.240Z_

<details><summary>↩ Tool result · `toolu_01QrBvRfBAN8cTZgTUT17kjS`</summary>

```text
Web search results for query: "Think-RM RM-Bench state of the art"

Links: [{"title":"[2505.16265] Think-RM: Enabling Long-Horizon Reasoning in Generative Reward Models","url":"https://arxiv.org/abs/2505.16265"},{"title":"Think-RM: Enabling Long-Horizon Reasoning in Generative Reward Models","url":"https://arxiv.org/pdf/2505.16265"},{"title":"Think Twice: Branch-and-Rethink Reasoning Reward Model","url":"https://arxiv.org/html/2510.23596"},{"title":"Paper page - RM-Bench: Benchmarking Reward Models of Language Models with Subtlety and Style","url":"https://huggingface.co/papers/2410.16184"},{"title":"RM-Bench: Evaluating Reward Models for Alignment","url":"https://www.emergentmind.com/topics/rm-bench"},{"title":"RM-Bench: Benchmarking Reward Models of Language Models with Subtlety   and Style","url":"https://arxiv.org/pdf/2410.16184"},{"title":"[Quick Review] RM-Bench: Benchmarking Reward Models of Language Models with Subtlety and Style","url":"https://liner.com/review/rmbench-benchmarking-reward-models-of-language-models-with-subtlety-and"},{"title":"RM-Bench: Benchmarking Reward Models of Language Models with Subtlety and Style","url":"https://proceedings.iclr.cc/paper_files/paper/2025/hash/6da1eec80095dc5937f7716db15aca4b-Abstract-Conference.html"},{"title":"RM-Bench: Benchmarking Reward Models of Language Models with Subtlety and Style","url":"https://arxiv.org/html/2410.16184v1"},{"title":"Libra: Assessing and Improving Reward Model by Learning to Think","url":"https://arxiv.org/pdf/2507.21645"}]

Based on the search results, here's what I found about Think-RM and RM-Bench:

## Think-RM and State-of-the-Art Performance

Think-RM achieves state-of-the-art results on RM-Bench, outperforming both BT RM and vertically scaled GenRM by 8%. The model achieves state-of-the-art performance among all publicly available RMs under 10B using only 6K training data.

## About Think-RM

Generative reward models (GenRMs) generate chain-of-thought (CoT) rationales followed by a final reward, but existing GenRMs rely on shallow, vertically scaled reasoning, limiting their capacity to handle nuanced or complex tasks. Think-RM addresses this by enabling long-horizon reasoning in generative reward models.

Think-RM proposes a novel pairwise RLHF pipeline that directly optimizes policies using pairwise preference rewards, and when combined with this pipeline, demonstrates superior end-policy performance compared to traditional approaches.

## RM-Bench Benchmark

RM-Bench is a benchmark designed to evaluate reward models based on their sensitivity to subtle content differences and resistance to style biases. Results reveal that even state-of-the-art models achieve an average performance of only 46.6%, which falls short of random-level accuracy (50%) when faced with style bias interference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad326ebb-b153-4085-8659-a6bf8b313aec",
  "isSidechain": true,
  "promptId": "c5cb5cdd-3dff-45de-89b1-a6d7b6dd5ec9",
  "agentId": "ae0e3790c0ea07cd1",
  "type": "user",
  "uuid": "4d231b24-4445-4a3b-80e2-7e51804d767a",
  "sourceToolAssistantUUID": "ad326ebb-b153-4085-8659-a6bf8b313aec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "dcea932a-9616-44e0-aedf-dc75f9c4b48a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-27T18:59:44.210Z_

Good, I found the paper. Let me now fetch the full paper content from arxiv and the project page for more details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d231b24-4445-4a3b-80e2-7e51804d767a",
  "isSidechain": true,
  "agentId": "ae0e3790c0ea07cd1",
  "requestId": "req_011CbTb4Wzg4FXEut8Z3a1Ws",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e8f87ae2-c81b-4571-9f8a-154299e75df7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "dcea932a-9616-44e0-aedf-dc75f9c4b48a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HvxuBuhGqfcVSu6F6LyvUj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2661,
      "cache_read_input_tokens": 10101,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2661,
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

_source line 15 · 2026-05-27T18:59:46.554Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018Kbna9X7ogVuTzTa4nbz28`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.16265",
  "prompt": "Extract the full abstract, all details about the method (training procedure, SFT, RL, pairwise RLHF pipeline), results on benchmarks (RM-Bench, RewardBench, etc.), whether it addresses calibration, whether it uses advantage functions, how it relates to process reward models or step-level verification, and any key numbers/percentages from experiments."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8f87ae2-c81b-4571-9f8a-154299e75df7",
  "isSidechain": true,
  "agentId": "ae0e3790c0ea07cd1",
  "requestId": "req_011CbTb4Wzg4FXEut8Z3a1Ws",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b43b95b9-58b3-4315-8207-14d71de79a65",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "dcea932a-9616-44e0-aedf-dc75f9c4b48a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HvxuBuhGqfcVSu6F6LyvUj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2661,
      "cache_read_input_tokens": 10101,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2661,
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

_source line 16 · 2026-05-27T18:59:48.907Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BaQ5PnUmTKqo1EshthaEu9`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.16265v1",
  "prompt": "Extract all technical details about Think-RM including: (1) the full training pipeline (SFT warmup, RL phase, rule-based RL details), (2) what benchmarks are used and exact numbers, (3) whether it addresses calibration of reward models, (4) whether it uses advantage functions, (5) how it relates to process reward models (PRMs) or step-level verification, (6) the pairwise RLHF pipeline details, (7) what base models are used, (8) training data size, (9) comparison to baselines. Be as detailed as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b43b95b9-58b3-4315-8207-14d71de79a65",
  "isSidechain": true,
  "agentId": "ae0e3790c0ea07cd1",
  "requestId": "req_011CbTb4Wzg4FXEut8Z3a1Ws",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac97f1f0-e9f2-4a81-99c7-3e879b2e8b67",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "dcea932a-9616-44e0-aedf-dc75f9c4b48a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HvxuBuhGqfcVSu6F6LyvUj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2661,
      "cache_read_input_tokens": 10101,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2661,
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

_source line 17 · 2026-05-27T18:59:49.815Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015WAU8HeXrrZZgrnfRB5dQW`</summary>

```json
{
  "url": "https://think-rm.github.io/",
  "prompt": "Extract all technical details, results, methodology overview, and key findings about Think-RM from this project page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac97f1f0-e9f2-4a81-99c7-3e879b2e8b67",
  "isSidechain": true,
  "agentId": "ae0e3790c0ea07cd1",
  "requestId": "req_011CbTb4Wzg4FXEut8Z3a1Ws",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "365c92ab-6932-46a1-91d9-867e47e903ae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "dcea932a-9616-44e0-aedf-dc75f9c4b48a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HvxuBuhGqfcVSu6F6LyvUj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2661,
      "cache_read_input_tokens": 10101,
      "output_tokens": 475,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2661
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 475,
          "cache_read_input_tokens": 10101,
          "cache_creation_input_tokens": 2661,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2661,
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

_source line 18 · 2026-05-27T18:59:52.146Z_

<details><summary>↩ Tool result · `toolu_018Kbna9X7ogVuTzTa4nbz28`</summary>

```text
# Think-RM: Long-Horizon Reasoning in Generative Reward Models

## Full Abstract
The paper presents Think-RM, a framework enabling extended reasoning capabilities in generative reward models (GenRMs). Rather than relying on shallow, structured rationales, the approach generates flexible, self-guided reasoning traces supporting self-reflection, hypothetical reasoning, and divergent thinking. The authors employ supervised fine-tuning on long chain-of-thought data followed by rule-based reinforcement learning. They introduce a novel pairwise RLHF pipeline that directly optimizes policies using pairwise preference rewards, avoiding pointwise conversion. Think-RM achieves state-of-the-art performance on RM-Bench, outperforming both Bradley-Terry reward models and vertically scaled GenRMs by 8%, with superior end-policy performance when combined with the new RLHF approach.

## Key Methodological Components

**Training Procedure:** "Rather than producing structured, externally provided rationales, Think-RM generates flexible, self-guided reasoning traces that support advanced capabilities such as self-reflection, hypothetical reasoning, and divergent reasoning."

**Two-Stage Training:** Supervised fine-tuning (SFT) on extended chain-of-thought data, followed by rule-based reinforcement learning to enhance long-horizon abilities.

**Novel RLHF Pipeline:** A pairwise RLHF approach that "directly optimizes policies using pairwise preference rewards, eliminating the need for pointwise reward conversion."

## Results & Benchmarks
- **RM-Bench performance:** 8% improvement over both Bradley-Terry and vertically scaled GenRM baselines
- Demonstrates superior end-policy performance compared to traditional approaches

## Notable Gaps in Available Information
The provided webpage excerpt does not include specific details about calibration, advantage functions, comparisons to process reward models, or results on other benchmarks like RewardBench.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b43b95b9-58b3-4315-8207-14d71de79a65",
  "isSidechain": true,
  "promptId": "c5cb5cdd-3dff-45de-89b1-a6d7b6dd5ec9",
  "agentId": "ae0e3790c0ea07cd1",
  "type": "user",
  "uuid": "e8715fae-340c-4866-abfe-43e158155b71",
  "sourceToolAssistantUUID": "b43b95b9-58b3-4315-8207-14d71de79a65",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "dcea932a-9616-44e0-aedf-dc75f9c4b48a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-27T18:59:54.086Z_

<details><summary>↩ Tool result · `toolu_015WAU8HeXrrZZgrnfRB5dQW`</summary>

```text
# Think-RM: Technical Summary

## Core Innovation
Think-RM advances generative reward models (GenRMs) by enabling extended reasoning capabilities. Rather than relying on structured rationales, the system generates "flexible, self-guided reasoning traces" supporting self-reflection, hypothetical reasoning, and divergent analysis.

## Methodology
The training framework operates in two phases:
1. **Warm-up**: Supervised fine-tuning using extended chain-of-thought data, with length-based filtering of training examples
2. **Enhancement**: Rule-based reinforcement learning to strengthen long-horizon reasoning abilities

A novel pairwise RLHF pipeline directly optimizes policies using preference rewards, eliminating conversion to pointwise signals.

## Key Results
- **RM-Bench**: Outperforms Bradley-Terry reward models and vertically scaled GenRMs by 8%
- **In-distribution tasks**: Superior performance on HelpSteer2-Preference evaluations
- **Distribution shift**: Maintains effectiveness on moderately shifted tasks (HelpSteer3-Preference)
- **Out-of-distribution**: Competitive results on RewardBench and RMBench benchmarks

## Technical Advancement
The system extends single chain-of-thought trajectories from hundreds to thousands of tokens, enabling handling of reasoning-intensive tasks that conventional reward models struggle with.

## Artifacts
- [ArXiv Paper (2505.16265)](https://www.arxiv.org/pdf/2505.16265)
- [GitHub Repository](https://github.com/IlgeeHong/Think-RM)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "365c92ab-6932-46a1-91d9-867e47e903ae",
  "isSidechain": true,
  "promptId": "c5cb5cdd-3dff-45de-89b1-a6d7b6dd5ec9",
  "agentId": "ae0e3790c0ea07cd1",
  "type": "user",
  "uuid": "28cc14cc-33af-4df8-a16f-a30e5d63841c",
  "sourceToolAssistantUUID": "365c92ab-6932-46a1-91d9-867e47e903ae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "dcea932a-9616-44e0-aedf-dc75f9c4b48a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-27T19:00:05.346Z_

<details><summary>↩ Tool result · `toolu_01BaQ5PnUmTKqo1EshthaEu9`</summary>

```text
# Technical Details of Think-RM

## (1) Full Training Pipeline

**SFT Warm-up Phase:**
The framework begins by generating multiple long CoT trajectories using QwQ-32B (M=10 trajectories per instance). For each instance, "the trajectory with the longest R̂ᵢⱼ among those satisfying ŝᵢⱼ=sᵢ" is selected for training. The SFT objective combines preference prediction and reasoning generation through maximum likelihood estimation over 5 epochs.

**Rule-based RL Phase:**
Following SFT, the model undergoes reinforcement learning using GRPO (Group Relative Policy Optimization) with accuracy-based rewards. For binary outputs, reward=1.0 for correct predictions, 0.0 otherwise. For multiclass outputs, reward=1.0 for exact matches, 0.5 when preference direction matches correctly. This phase runs for 1-2 epochs with rollout batch size 512 and KL coefficient β=1e-4.

## (2) Benchmarks and Performance Numbers

**In-Distribution (HelpSteer2-Preference):**
- Binary Think-RM (SFT+RL): 73.28% average accuracy
- Outperforms CoT-GenRM (ground truth): 72.03%

**Moderate Distribution Shift (HelpSteer3-Preference):**
- Binary Think-RM: 73.28% average accuracy

**Out-of-Distribution - RewardBench:**
- Binary Think-RM (SFT+RL): 86.35% average
- Multiclass: 84.49% average
- Improvements of 10%+ in "Chat Hard" subcategory

**Out-of-Distribution - RM-Bench:**
- Binary Think-RM: 75.06% average (8% improvement over baselines)
- Math domain: 12% improvement over CoT-GenRMs
- Chat: 66.41%, Code: 54.68%, Safety: 91.51%

## (3) Calibration of Reward Models

The document does not explicitly address calibration of reward models. Focus remains on accuracy metrics rather than confidence calibration or uncertainty quantification.

## (4) Advantage Functions

Yes, the pairwise RLHF pipeline employs advantage estimation. "We compute Â̂ᵢ based on our pairwise difference matrix D: Â̂ᵢ=∑ⱼ₌₁ᴳdᵢⱼ/√(G/2(G-1)∑ᵢ,ⱼdᵢⱼ²+Gϵ)" This derives from standard advantage estimation relationships in GRPO.

## (5) Relation to Process Reward Models (PRMs)

Think-RM differs fundamentally from step-level verification. Rather than evaluating intermediate reasoning steps, it generates "flexible, self-guided reasoning traces" within a single trajectory. The framework enables "self-reflection, hypothetical reasoning, and divergent reasoning" but operates at the trajectory level rather than step-by-step verification common in PRMs.

## (6) Pairwise RLHF Pipeline Details

The novel pipeline constructs a "skew-symmetric matrix D∈ℝ⁽ᴳᴮ⁾ˣ⁽ᴳᴮ⁾" for preference strength across response pairs. For multiclass output s∈{-3,-2,-1,1,2,3}, entries are defined as dᵢⱼ=-s, dⱼᵢ=-dᵢⱼ. For binary preferences, weighting incorporates reasoning length: dᵢⱼ=-s̃/|R̂|, treating longer reasoning chains as indicating "more ambiguous comparisons" with smaller reward differences.

## (7) Base Models

**Reward Model Training:** Llama-3.1-8B-Instruct (selected for computational efficiency)

**Reasoning Provider:** QwQ-32B generates the long CoT trajectories for SFT warm-up data

## (8) Training Data Size

- **HelpSteer2-Preference source:** 10K prompt-response pairs
- **Binary preference dataset:** 6K examples after filtering instances where all generated preferences disagreed with ground truth
- **Multiclass preference dataset:** 4K examples
- **RLHF training:** 3K randomly sampled prompts from HH-RLHF

## (9) Comparison to Baselines

**Key Comparisons:**

- **vs. Bradley-Terry (BT) RM:** Think-RM achieves 73.28% vs. 71.88% on HelpSteer2 binary tasks, demonstrating robustness in low-data regimes where "BT RMs often overfit to specific patterns"
- **vs. CoT-GenRM (ground truth):** 81.53% vs. 80.97% binary accuracy on in-distribution
- **vs. Vertical Scaling:** Think-RM's horizontal scaling outperforms CoT-GenRMs with 16-sample majority voting on RM-Bench (75.06% vs. 68.55%)
- **vs. Pointwise RLHF:** Pairwise RLHF with Think-RM achieves 31.94% length-controlled win rate on AlpacaEval2 versus 27.49% with traditional BT RM approaches

All models trained on identical 6K/4K datasets ensure fair comparison within respective categories.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac97f1f0-e9f2-4a81-99c7-3e879b2e8b67",
  "isSidechain": true,
  "promptId": "c5cb5cdd-3dff-45de-89b1-a6d7b6dd5ec9",
  "agentId": "ae0e3790c0ea07cd1",
  "type": "user",
  "uuid": "fe691d90-924f-4759-97eb-f05ad0c0aa1f",
  "sourceToolAssistantUUID": "ac97f1f0-e9f2-4a81-99c7-3e879b2e8b67",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "dcea932a-9616-44e0-aedf-dc75f9c4b48a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-27T19:00:25.335Z_

I now have comprehensive details. Here is the detailed report.

---

## Think-RM: Enabling Long-Horizon Reasoning in Generative Reward Models

**Paper:** arXiv 2505.16265, accepted at NeurIPS 2025. Base model: Llama-3.1-8B-Instruct.

**What it does.** Think-RM is a framework that upgrades generative reward models (GenRMs) from shallow chain-of-thought (CoT) rationales to long-horizon, self-guided reasoning traces spanning hundreds to thousands of tokens. Instead of structured, externally provided rationales, Think-RM generates flexible internal "thinking" that supports self-reflection, hypothetical reasoning, and divergent reasoning -- enabling it to handle nuanced preference judgments that conventional reward models struggle with.

**Training pipeline.** Think-RM uses a two-stage approach. (1) **SFT warm-up:** QwQ-32B generates 10 long CoT trajectories per instance from 10K prompt-response pairs (HelpSteer2-Preference). The longest correct trajectory is selected, yielding 6K binary and 4K multiclass training examples. The model is fine-tuned for 5 epochs. (2) **Rule-based RL:** The model then undergoes GRPO (Group Relative Policy Optimization) with accuracy-based rewards (1.0 for correct, 0.0 for incorrect; 0.5 for partial matches in multiclass), running 1-2 epochs with rollout batch size 512 and KL coefficient 1e-4. So the training is SFT + RL, not classical RLHF for the reward model itself.

**Pairwise RLHF pipeline.** A key contribution is a novel downstream RLHF pipeline that directly uses Think-RM's pairwise preference outputs to train policies, bypassing the lossy conversion to pointwise rewards. It constructs a skew-symmetric preference-strength matrix and derives advantage estimates from it: the advantage for response i is computed as the normalized sum of pairwise differences. For binary outputs, longer reasoning chains are treated as indicating more ambiguous comparisons, weighting rewards inversely by reasoning length. So yes, **it does use advantage functions** -- specifically a pairwise-derived advantage estimator.

**Calibration.** The paper does **not** explicitly address reward model calibration or confidence calibration. Its focus is on accuracy and downstream policy performance rather than uncertainty quantification.

**Relation to process reward models.** Think-RM is fundamentally different from PRMs/step-level verification. It does not evaluate intermediate reasoning steps of the policy's output. Instead, the "long-horizon reasoning" refers to the reward model's own internal deliberation -- it thinks longer before rendering a judgment on entire response pairs, operating at the trajectory level.

**Key results.** On **RM-Bench**, Think-RM achieves 75.06% (8% above baselines), with a 12% improvement in math. On **RewardBench**, it scores 86.35% (binary), with 10%+ gains on the "Chat Hard" subcategory. It outperforms CoT-GenRMs even with 16-sample majority voting (75.06% vs 68.55%). On downstream policy training, pairwise RLHF with Think-RM achieves 31.94% length-controlled win rate on **AlpacaEval2** versus 27.49% for traditional BT RM approaches. All results use only 6K training examples on an 8B-parameter model, achieving SOTA among publicly available RMs under 10B.

Sources:
- [Think-RM on arXiv](https://arxiv.org/abs/2505.16265)
- [Think-RM HTML paper](https://arxiv.org/html/2505.16265v1)
- [Think-RM OpenReview](https://openreview.net/forum?id=UfQAFbP6xq)
- [Think-RM Project Page](https://think-rm.github.io/)
- [Think-RM GitHub](https://github.com/IlgeeHong/Think-RM)
- [NeurIPS 2025 Poster](https://neurips.cc/virtual/2025/poster/117753)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe691d90-924f-4759-97eb-f05ad0c0aa1f",
  "isSidechain": true,
  "agentId": "ae0e3790c0ea07cd1",
  "requestId": "req_011CbTb6J5MRjS3dDJACEdsZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1d90ce7a-1efc-4d7e-9763-97620f62e46c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "dcea932a-9616-44e0-aedf-dc75f9c4b48a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017q72KoKTxogYJgkDgthfNU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 389,
      "cache_creation_input_tokens": 2281,
      "cache_read_input_tokens": 12762,
      "output_tokens": 1007,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2281
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 389,
          "output_tokens": 1007,
          "cache_read_input_tokens": 12762,
          "cache_creation_input_tokens": 2281,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2281,
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
