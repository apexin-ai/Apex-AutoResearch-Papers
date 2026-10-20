# Research conversation: You are researching the paper "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning" by De

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a98155e9543b5a45d.jsonl`
- **Structured JSON:** [`1a84397f7aa213a94fa9.json`](../../sessions/1a/1a84397f7aa213a94fa9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

31 recorded events

### User

_source line 1 · 2026-05-29T05:30:54.391Z_

You are researching the paper "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning" by DeepSeek-AI (Nature 2025). URL: https://arxiv.org/abs/2501.12948

Tasks:
1. Use WebFetch to read the arxiv abstract page for this paper.
2. Use WebFetch to read the HTML version for method details (try https://arxiv.org/html/2501.12948).
3. Search for Nature publication details and any reviews/commentary using WebSearch.

For each source, extract:
- The exact problem/gap they identified
- Their key insight about pure RL for reasoning
- Technical method: GRPO algorithm details, how reward is structured, training pipeline (cold start, RL, rejection sampling, final RL)
- Emergent behaviors observed (self-reflection, verification, backtracking)
- Specific quantitative results on math benchmarks
- Any discussion of robustness or fragility of the resulting models

Return a detailed summary (under 1500 words) covering all the above points. Focus especially on GRPO details since that's the training paradigm our research aims to improve.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "a98155e9543b5a45d",
  "type": "user",
  "uuid": "bce23867-4846-4882-a631-bbaa4dba8855",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-29T05:30:54.403Z_

```json
{
  "parentUuid": "bce23867-4846-4882-a631-bbaa4dba8855",
  "isSidechain": true,
  "agentId": "a98155e9543b5a45d",
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
  "uuid": "88d61d52-9144-43e3-8455-521578eb30ae",
  "timestamp": "2026-05-29T05:30:54.403Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-29T05:30:54.404Z_

```json
{
  "parentUuid": "88d61d52-9144-43e3-8455-521578eb30ae",
  "isSidechain": true,
  "agentId": "a98155e9543b5a45d",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "95731c46-8ca5-49de-bcef-2fcaf942d009",
  "timestamp": "2026-05-29T05:30:54.404Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-29T05:31:00.152Z_



I'll start by fetching the tools I need, then gather information from multiple sources.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95731c46-8ca5-49de-bcef-2fcaf942d009",
  "isSidechain": true,
  "agentId": "a98155e9543b5a45d",
  "requestId": "req_011CbWK1ECwZc536i5pm9EjX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71131627-ee68-4aa5-b9fd-88575bc663e0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016KnFVd52g5MKZZoHiTHUJp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1603,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1603,
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

_source line 5 · 2026-05-29T05:31:00.682Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01FKYtzxXR8JkHJqzqE7Cev8`</summary>

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
  "parentUuid": "71131627-ee68-4aa5-b9fd-88575bc663e0",
  "isSidechain": true,
  "agentId": "a98155e9543b5a45d",
  "requestId": "req_011CbWK1ECwZc536i5pm9EjX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2bcef4d7-cf9e-4c4b-a857-add7fc12b7d3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016KnFVd52g5MKZZoHiTHUJp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1603,
      "cache_read_input_tokens": 7413,
      "output_tokens": 99,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1603
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 99,
          "cache_read_input_tokens": 7413,
          "cache_creation_input_tokens": 1603,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1603,
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

_source line 6 · 2026-05-29T05:31:00.687Z_

<details><summary>↩ Tool result · `toolu_01FKYtzxXR8JkHJqzqE7Cev8`</summary>

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
  "parentUuid": "2bcef4d7-cf9e-4c4b-a857-add7fc12b7d3",
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "a98155e9543b5a45d",
  "type": "user",
  "uuid": "8e2b8b65-aaae-45b0-88b8-3439fe3e29db",
  "sourceToolAssistantUUID": "2bcef4d7-cf9e-4c4b-a857-add7fc12b7d3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-29T05:31:02.916Z_



Now let me fetch all three sources in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e2b8b65-aaae-45b0-88b8-3439fe3e29db",
  "isSidechain": true,
  "agentId": "a98155e9543b5a45d",
  "requestId": "req_011CbWK1hKMUBPpfuBrx4dtD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa2fd58c-3384-4c20-a69f-7df61d3f4a70",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AeDazmMJ9Qmj9k6JoGiNsb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1121,
      "cache_read_input_tokens": 9016,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1121,
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

_source line 8 · 2026-05-29T05:31:05.732Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KaYT4s3eeZcDZEurQrCdka`</summary>

```json
{
  "url": "https://arxiv.org/abs/2501.12948",
  "prompt": "Extract ALL details from this paper abstract page: the full title, all authors, the complete abstract text, the exact problem/gap they identify, their key claims about reinforcement learning for reasoning, any mention of emergent behaviors, any quantitative results mentioned, and publication details (date, version, journal)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa2fd58c-3384-4c20-a69f-7df61d3f4a70",
  "isSidechain": true,
  "agentId": "a98155e9543b5a45d",
  "requestId": "req_011CbWK1hKMUBPpfuBrx4dtD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7fc043c2-eaaa-4015-b8fe-ff3031173cd1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AeDazmMJ9Qmj9k6JoGiNsb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1121,
      "cache_read_input_tokens": 9016,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1121,
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

_source line 9 · 2026-05-29T05:31:11.263Z_

<details><summary>↩ Tool result · `toolu_01KaYT4s3eeZcDZEurQrCdka`</summary>

```text
# DeepSeek-R1 Paper Details

## Full Title
"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"

## Authors
The paper lists 199+ authors from DeepSeek-AI, with primary contributors including Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, and Peiyi Wang among many others.

## Abstract Summary
The researchers demonstrate that reasoning abilities in large language models can be developed through pure reinforcement learning without requiring human-annotated reasoning trajectories, achieving superior performance on mathematics, coding, and STEM tasks.

## Problem/Gap Identified
The authors note that while chain-of-thought prompting has shown success, current approaches remain "heavily contingent upon extensive human-annotated demonstrations" and lack sufficient capability for complex problems.

## Key Claims About Reinforcement Learning
Their RL framework enables models to "achieve superior performance on verifiable tasks such as mathematics, coding competitions, and STEM fields" while surpassing "counterparts trained via conventional supervised learning."

## Emergent Behaviors
The framework "facilitates the emergent development of advanced reasoning patterns, such as self-reflection, verification, and dynamic strategy adaptation," which can subsequently guide smaller models.

## Publication Details
- **Submitted:** January 22, 2025 (v1); Revised January 4, 2026 (v2)
- **Journal:** Nature, volume 645, pages 633-638 (2025)
- **ArXiv ID:** 2501.12948
- **DOI:** 10.48550/arXiv.2501.12948
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7fc043c2-eaaa-4015-b8fe-ff3031173cd1",
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "a98155e9543b5a45d",
  "type": "user",
  "uuid": "d33fb87e-bfaa-4c68-bdda-37e6d9c9dbac",
  "sourceToolAssistantUUID": "7fc043c2-eaaa-4015-b8fe-ff3031173cd1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-29T05:31:12.026Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CD1quK1B6sp42k2iJBwFEL`</summary>

```json
{
  "url": "https://arxiv.org/html/2501.12948",
  "prompt": "Extract detailed technical information about: 1) The GRPO (Group Relative Policy Optimization) algorithm - how it works, its mathematical formulation, how it differs from PPO, how advantages are computed within groups. 2) The reward structure - what reward signals are used (accuracy, format, process rewards). 3) The full training pipeline stages: cold start data, RL training, rejection sampling, SFT, final RL. 4) Emergent behaviors observed during training (self-reflection, verification, backtracking, aha moments). 5) Specific quantitative results on math benchmarks (AIME 2024, MATH-500, etc.) and coding benchmarks. 6) Any discussion of reward hacking, training instability, language mixing, or fragility. 7) Distillation results to smaller models. Provide as much technical detail as possible including equations if present."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d33fb87e-bfaa-4c68-bdda-37e6d9c9dbac",
  "isSidechain": true,
  "agentId": "a98155e9543b5a45d",
  "requestId": "req_011CbWK1hKMUBPpfuBrx4dtD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3f413a52-dbac-453d-8ec0-8604c07495c2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AeDazmMJ9Qmj9k6JoGiNsb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1121,
      "cache_read_input_tokens": 9016,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1121,
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

_source line 11 · 2026-05-29T05:31:12.043Z_

<details><summary>↩ Tool result · `toolu_01CD1quK1B6sp42k2iJBwFEL`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f413a52-dbac-453d-8ec0-8604c07495c2",
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "a98155e9543b5a45d",
  "type": "user",
  "uuid": "1065cfd8-31b4-4e68-9726-a57858336b8c",
  "sourceToolAssistantUUID": "3f413a52-dbac-453d-8ec0-8604c07495c2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-29T05:31:12.489Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0126L4fLMeADkqnAGmhB7oGE`</summary>

```json
{
  "query": "DeepSeek-R1 Nature 2025 publication review commentary reinforcement learning reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1065cfd8-31b4-4e68-9726-a57858336b8c",
  "isSidechain": true,
  "agentId": "a98155e9543b5a45d",
  "requestId": "req_011CbWK1hKMUBPpfuBrx4dtD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5685b6e-0bd0-489a-832d-c272546875eb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AeDazmMJ9Qmj9k6JoGiNsb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1121,
      "cache_read_input_tokens": 9016,
      "output_tokens": 471,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1121
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 471,
          "cache_read_input_tokens": 9016,
          "cache_creation_input_tokens": 1121,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1121,
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

_source line 13 · 2026-05-29T05:31:21.037Z_

<details><summary>↩ Tool result · `toolu_0126L4fLMeADkqnAGmhB7oGE`</summary>

```text
Web search results for query: "DeepSeek-R1 Nature 2025 publication review commentary reinforcement learning reasoning"

Links: [{"title":"Examining methodological rigor, ethical governance, and scientific claims: a critical review of the DeepSeek-R1 study | Discover Artificial Intelligence | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s44163-026-01131-4"},{"title":"Behind the Scenes of DeepSeek-R1: A Landmark in AI Published in Nature | CSPaper Forum","url":"https://forum.cspaper.org/topic/160/behind-the-scenes-of-deepseek-r1-a-landmark-in-ai-published-in-nature"},{"title":"Deepseek Shatters Industry Norms with $294,000 Breakthrough That Landed on Nature - CTOL Digital Solutions","url":"https://www.ctol.digital/news/chinese-ai-lab-deepseek-first-language-model-published-nature/"},{"title":"DeepSeek-R1 Published in Nature (Vol. 645, Issue 8081, 18 Sept 2025) - CompositesAI - cdmHUB Community","url":"https://community.cdmhub.org/t/deepseek-r1-published-in-nature-vol-645-issue-8081-18-sept-2025/780"},{"title":"DeepSeek Debuts on Nature's Cover: Chinese Large Model Creates New History, Does What OpenAI Didn't Dare","url":"https://eu.36kr.com/en/p/3472036830091393"},{"title":"DeepSeek - R1 Paper Makes It to Nature's Cover, Corresponding Author: LIANG Wenfeng","url":"https://eu.36kr.com/en/p/3471061555959170"},{"title":"Commentary on “DeepSeek-R1 and GPT-4 are comparable in a complex diagnostic challenge: a historical control study”","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12825781/"},{"title":"Why DeepSeek‑R1 made Nature’s Cover this Month","url":"https://www.paulswider.com/p/why-deepseekr1-made-natures-cover"},{"title":"Commentary on “DeepSeek-R1 and GPT-4 are comparable in a complex diagnostic challenge: a historical control study”","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12695260/"}]

Based on the web search results, here's what I found about DeepSeek-R1's Nature 2025 publication:

## Publication Overview

In September 2025, the DeepSeek team published a paper in Nature introducing the DeepSeek-R1 inference model, which quickly garnered widespread attention from both academic and industrial communities. On September 17, 2025, the DeepSeek-R1 paper was officially published as a cover article in Nature, marking the first large language model (LLM) to undergo rigorous peer review and appear in a top-tier scientific journal.

## Key Achievement and Significance

As the first research on a large language model (LLM) from China to be featured on the cover of Nature, it was described as the world's first peer-reviewed mainstream large language model. It marks the first time a mainstream AI system has undergone the rigorous scrutiny of independent peer review, exposing detailed methodologies that industry giants have jealously guarded as trade secrets.

## Technical Approach

The work presents notable achievements, including a technically ambitious "pure RL" training approach that forgoes supervised fine-tuning, a clear multistage pipeline for capability building and alignment, and rigorous evaluation across a comprehensive suite of reasoning and safety benchmarks. The DeepSeek-R1 study appeared on the cover of Nature, with the striking tagline "Self-Help: Reinforcement learning teaches AI model to improve itself."

## Peer Review Process

DeepSeek's paper endured three rounds of peer review involving eight reviewers who generated 64 pages of reports and responses, supplemented by 83 pages of supplementary material, spanning from February 14 to July 17, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5685b6e-0bd0-489a-832d-c272546875eb",
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "a98155e9543b5a45d",
  "type": "user",
  "uuid": "e2b8c325-5f02-43f5-b283-7e0ec2ed2951",
  "sourceToolAssistantUUID": "f5685b6e-0bd0-489a-832d-c272546875eb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-29T05:31:25.428Z_

The HTML version returned a 404. Let me try the PDF-linked page and also fetch more technical details and commentary.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2b8c325-5f02-43f5-b283-7e0ec2ed2951",
  "isSidechain": true,
  "agentId": "a98155e9543b5a45d",
  "requestId": "req_011CbWK3CBTLnkhneSN9HVod",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cc00930e-9d55-421b-ab89-e8f51cbaa28a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KaLopqJk6miYYnBUQfDkck",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2014,
      "cache_read_input_tokens": 10137,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2014,
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

_source line 15 · 2026-05-29T05:31:31.607Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01H3oqwxFcR6TAPCNXGVyfqu`</summary>

```json
{
  "url": "https://arxiv.org/html/2501.12948v2",
  "prompt": "Extract detailed technical information about: 1) The GRPO (Group Relative Policy Optimization) algorithm - how it works, its mathematical formulation, how it differs from PPO, how advantages are computed within groups. 2) The reward structure - what reward signals are used (accuracy, format, process rewards). 3) The full training pipeline stages: cold start data, RL training, rejection sampling, SFT, final RL. 4) Emergent behaviors observed during training (self-reflection, verification, backtracking, aha moments). 5) Specific quantitative results on math benchmarks (AIME 2024, MATH-500, etc.) and coding benchmarks. 6) Any discussion of reward hacking, training instability, language mixing, or fragility. 7) Distillation results to smaller models."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc00930e-9d55-421b-ab89-e8f51cbaa28a",
  "isSidechain": true,
  "agentId": "a98155e9543b5a45d",
  "requestId": "req_011CbWK3CBTLnkhneSN9HVod",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "46284253-939c-46d4-8e8e-77a903d9a763",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KaLopqJk6miYYnBUQfDkck",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2014,
      "cache_read_input_tokens": 10137,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2014,
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

_source line 16 · 2026-05-29T05:31:31.621Z_

<details><summary>↩ Tool result · `toolu_01H3oqwxFcR6TAPCNXGVyfqu`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46284253-939c-46d4-8e8e-77a903d9a763",
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "a98155e9543b5a45d",
  "type": "user",
  "uuid": "84a730e2-58f5-457a-b362-cce54bba75fd",
  "sourceToolAssistantUUID": "46284253-939c-46d4-8e8e-77a903d9a763",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-29T05:31:34.031Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Lnh8FDigvjadX9vsN4kiCU`</summary>

```json
{
  "url": "https://link.springer.com/article/10.1007/s44163-026-01131-4",
  "prompt": "Extract any critical review points about DeepSeek-R1's methodology, including: limitations of GRPO, concerns about reward hacking, fragility of emergent behaviors, reproducibility issues, and any identified weaknesses in the training pipeline or evaluation. Also extract any discussion of the significance of the pure RL approach and how it compares to supervised approaches."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84a730e2-58f5-457a-b362-cce54bba75fd",
  "isSidechain": true,
  "agentId": "a98155e9543b5a45d",
  "requestId": "req_011CbWK3CBTLnkhneSN9HVod",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d08f438-e739-4d3f-804b-7efa17fc5015",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KaLopqJk6miYYnBUQfDkck",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2014,
      "cache_read_input_tokens": 10137,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2014,
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

_source line 18 · 2026-05-29T05:31:34.479Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N2RyaCtDNpzkzN5cTRc7zo`</summary>

```json
{
  "query": "DeepSeek-R1 GRPO algorithm details group relative policy optimization reward structure training pipeline technical"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d08f438-e739-4d3f-804b-7efa17fc5015",
  "isSidechain": true,
  "agentId": "a98155e9543b5a45d",
  "requestId": "req_011CbWK3CBTLnkhneSN9HVod",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a7a14e31-c8a0-473e-8c69-d7b7b7d52550",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KaLopqJk6miYYnBUQfDkck",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2014,
      "cache_read_input_tokens": 10137,
      "output_tokens": 499,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2014
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 499,
          "cache_read_input_tokens": 10137,
          "cache_creation_input_tokens": 2014,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2014,
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

_source line 19 · 2026-05-29T05:31:34.678Z_

<details><summary>↩ Tool result · `toolu_01Lnh8FDigvjadX9vsN4kiCU`</summary>

```text
REDIRECT DETECTED: The URL redirects to a different host.

Original URL: https://link.springer.com/article/10.1007/s44163-026-01131-4
Redirect URL: https://idp.springer.com/authorize?response_type=cookie&client_id=springerlink&redirect_uri=https%3A%2F%2Flink.springer.com%2Farticle%2F10.1007%2Fs44163-026-01131-4
Status: 303 See Other

To complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters:
- url: "https://idp.springer.com/authorize?response_type=cookie&client_id=springerlink&redirect_uri=https%3A%2F%2Flink.springer.com%2Farticle%2F10.1007%2Fs44163-026-01131-4"
- prompt: "Extract any critical review points about DeepSeek-R1's methodology, including: limitations of GRPO, concerns about reward hacking, fragility of emergent behaviors, reproducibility issues, and any identified weaknesses in the training pipeline or evaluation. Also extract any discussion of the significance of the pure RL approach and how it compares to supervised approaches."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d08f438-e739-4d3f-804b-7efa17fc5015",
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "a98155e9543b5a45d",
  "type": "user",
  "uuid": "2050fb51-873f-4404-8ba1-7a900452b2fa",
  "sourceToolAssistantUUID": "5d08f438-e739-4d3f-804b-7efa17fc5015",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-29T05:31:44.540Z_

<details><summary>↩ Tool result · `toolu_01N2RyaCtDNpzkzN5cTRc7zo`</summary>

```text
Web search results for query: "DeepSeek-R1 GRPO algorithm details group relative policy optimization reward structure training pipeline technical"

Links: [{"title":"GRPO - Group Relative Policy Optimization: How DeepSeek Trains Reasoning Models","url":"https://chessman7.substack.com/p/grpo-group-relative-policy-optimization"},{"title":"Understanding the DeepSeek R1 Paper · Hugging Face","url":"https://huggingface.co/learn/llm-course/chapter12/3"},{"title":"Understanding GRPO Optimization in DeepSeek R1: A Step-by-Step Breakdown with Examples | by Bing | Medium","url":"https://medium.com/@bingqian/understanding-grpo-optimization-in-deepseek-r1-a-step-by-step-breakdown-with-examples-c0f68fd97823"},{"title":"Demystifying Group Relative Policy Optimization: Its Policy Gradient is a U-Statistic","url":"https://arxiv.org/pdf/2603.01162"},{"title":"Bite: How Deepseek R1 was trained","url":"https://www.philschmid.de/deepseek-r1"},{"title":"Why GRPO is Important and How it Works","url":"https://ghost.oxen.ai/why-grpo-is-important-and-how-it-works/"},{"title":"deep-learning-pytorch-huggingface/training/mini-deepseek-r1-aha-grpo.ipynb at main · philschmid/deep-learning-pytorch-huggingface","url":"https://github.com/philschmid/deep-learning-pytorch-huggingface/blob/main/training/mini-deepseek-r1-aha-grpo.ipynb"},{"title":"Group Relative Policy Optimization (GRPO) Illustrated Breakdown | Ebrahim Pichka","url":"https://epichka.com/blog/2025/grpo/"},{"title":"Revisiting Group Relative Policy Optimization: Insights into On-Policy and Off-Policy Training","url":"https://arxiv.org/html/2505.22257v1"},{"title":"Group Relative Policy Optimization (GRPO)","url":"https://cameronrwolfe.substack.com/p/grpo"}]

I've found comprehensive information about DeepSeek-R1 and the GRPO algorithm. Here's a detailed breakdown:

## Overview

Group Relative Policy Optimization (GRPO) is a reinforcement learning algorithm to improve the reasoning capabilities of LLMs. GRPO is a core methodological component of DeepSeek-Math and DeepSeek-R1, and has become the talk of the town for Reinforcement Learning in Large Language Models due to its effectiveness and ease of training.

## Key Technical Differences from PPO

GRPO reduces memory requirements by 40-60% by eliminating the separate value function model. Unlike PPO, GRPO does not rely on a separate value function model, which simplifies training and reduces memory consumption, and uses the average reward of a group of outputs as a baseline.

The key innovations of GRPO are group sampling, relative advantage estimation, and the elimination of the value network.

## Reward Structure

The advantage of each solution within the group is computed relative to this baseline, and the reward is normalized within a group. R1-Zero uses RLVR with only verifiable reward signals, with two types of rewards: accuracy reward (evaluates whether the model's response is correct) and format reward (enforces a desired format on the model's output).

## Training Pipeline

DeepSeek created DeepSeek-R1-Zero, which skipped supervised fine-tuning altogether and used pure reinforcement learning with GRPO, leading to emergent behaviors like self-evaluation and "aha moments" where the model recognizes errors in its reasoning and corrects itself.

The R1 paper demonstrated how you can use GRPO to go from a base instruction following LLM (DeepSeek-v3) to a reasoning model (DeepSeek-R1).

## Performance and Efficiency

DeepSeek-R1's post-training requires only about 147K H800 GPU-hours – an order of magnitude lower than many contemporary large reasoning models, including OpenAI's o1 series. DeepSeek-R1 extended the GRPO approach beyond math to general reasoning tasks including coding, logical puzzles, and analytical problems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7a14e31-c8a0-473e-8c69-d7b7b7d52550",
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "a98155e9543b5a45d",
  "type": "user",
  "uuid": "f211b34c-6a83-4993-a385-16681afd2e89",
  "sourceToolAssistantUUID": "a7a14e31-c8a0-473e-8c69-d7b7b7d52550",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-29T05:31:46.591Z_

Let me get more technical details from the Hugging Face course page and one more source.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f211b34c-6a83-4993-a385-16681afd2e89",
  "isSidechain": true,
  "agentId": "a98155e9543b5a45d",
  "requestId": "req_011CbWK4vYft5pB8a2CYz4Cu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7e7fe229-2d5a-49b0-b3a4-bdde64aad24d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DuubND53ezs4Jjnj8Pxtnp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2019,
      "cache_read_input_tokens": 12151,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2019,
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

_source line 22 · 2026-05-29T05:31:51.963Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SXoiWFcAw7gLcAq2KDrsU8`</summary>

```json
{
  "url": "https://huggingface.co/learn/llm-course/chapter12/3",
  "prompt": "Extract ALL technical details about: 1) GRPO mathematical formulation - the objective function, how group advantages are computed, the clipping mechanism, KL divergence penalty. 2) The complete training pipeline for DeepSeek-R1 (all 4 stages: cold start, reasoning RL, rejection sampling + SFT, final RL). 3) How rewards are structured (accuracy rewards, format rewards, language consistency rewards). 4) Emergent behaviors (self-reflection, verification, aha moments, backtracking). 5) Specific benchmark results (AIME 2024, MATH-500, Codeforces, GPQA Diamond). 6) Distillation to smaller models. 7) Any discussion of failure modes, reward hacking, or instability."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e7fe229-2d5a-49b0-b3a4-bdde64aad24d",
  "isSidechain": true,
  "agentId": "a98155e9543b5a45d",
  "requestId": "req_011CbWK4vYft5pB8a2CYz4Cu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "48b99ffc-608c-432a-a251-6460b9ef6084",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DuubND53ezs4Jjnj8Pxtnp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2019,
      "cache_read_input_tokens": 12151,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2019,
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

_source line 23 · 2026-05-29T05:31:52.603Z_

<details><summary>↩ Tool result · `toolu_01SXoiWFcAw7gLcAq2KDrsU8`</summary>

````text
# Understanding the DeepSeek R1 Paper

This chapter is a crash course paper reading. We will walk through the paper in simple terms, and then we will break down the key concepts and takeaways.

DeepSeek R1 represents a significant advancement in language model training, particularly in developing reasoning capabilities through reinforcement learning. The paper introduces a new reinforcement learning algorithm called Group Relative Policy Optimization (GRPO).

![DeepSeek R1 Overview](https://huggingface.co/reasoning-course/images/resolve/main/grpo/4.png)

In the next chapter, we will build on this knowledge and implement GRPO in practice.

The initial goal of the paper was to explore whether pure reinforcement learning could develop reasoning capabilities without supervised fine-tuning. 

> [!TIP]
> Up until that point, all the popular LLMs required some supervised fine-tuning, which we explored in [chapter 11](/course/chapter11/1).

## The Breakthrough 'Aha' Moment

![The 'Aha Moment'](https://huggingface.co/reasoning-course/images/resolve/main/grpo/9.png)

One of the most remarkable discoveries in R1-Zero's training was the emergence of a phenomenon known as the "Aha Moment." This phenomenon is somewhat similar to how humans experience sudden realizations while problem-solving. Here's how it works:

1. Initial Attempt: The model makes an initial attempt at solving a problem
2. Recognition: It recognizes potential errors or inconsistencies
3. Self-Correction: It adjusts its approach based on this recognition
4. Explanation: It can explain why the new approach is better

This breakthrough resonates with learners and feels like a "Eureka" moment. It demonstrates learning rather than mere memorization, so let's take a moment to imagine what it feels like to have an "Aha" moment.

For example, imagine you're trying to solve a puzzle:
- First try: "This piece should go here based on the color"
- Recognition: "But wait, the shape doesn't quite fit"
- Correction: "Ah, it actually belongs over there"
- Explanation: "Because both the color and shape pattern match in this position"

This ability emerged naturally from RL training, without being explicitly programmed, demonstrating learning rather than mere memorization of a process from the training data.

The easiest way to understand the 'Aha' moment is to see it in action. Let's take a look at an example. In the chat below, we ask the model to solve a problem and the UI shows the model's thought process as it solves the problem.

If you want to try Deepseek's R1, you can also check out [Hugging Chat](https://huggingface.co/chat/models/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B).

## The Training Process

Training R1 was a multi-phase process. Let's break down the phases and the key innovations in each phase.

The final process results in two models:
- DeepSeek-R1-Zero: A model trained purely using reinforcement learning.
- DeepSeek-R1: A model that builds on the foundation of DeepSeek-R1-Zero and adds supervised fine-tuning.

| Feature | DeepSeek-R1-Zero | DeepSeek-R1 |
|---------|------------------|--------------|
| Training Approach | Pure RL | Multi-phase (SFT + RL) |
| Fine-tuning | None | Supervised fine-tuning |
| Reasoning Capability | Emergent | Enhanced |
| AIME Performance | 71.0% | 79.8% |
| Key Characteristics | Strong reasoning but readability issues | Better language consistency and readability |

While DeepSeek-R1-Zero demonstrates the potential of pure reinforcement learning for developing reasoning capabilities, DeepSeek-R1 builds upon this foundation with a more balanced approach that prioritizes both reasoning performance and usability.

The training process involves four phases:

1. Cold Start Phase
2. Reasoning RL Phase
3. Rejection Sampling Phase
4. Diverse RL Phase

Let's break down each phase:

### Cold Start Phase (Quality Foundation)

![Cold Start Phase](https://huggingface.co/reasoning-course/images/resolve/main/grpo/5.png)

This phase is designed to establish a strong foundation for the model's readability and response quality. It uses a small dataset of high-quality samples from R1-Zero to fine-tune the V3-Base model. Starting with the DeepSeek-V3-Base model, the team used thousands of validated, high-quality samples from R1-Zero for supervised fine-tuning. This innovative approach uses a small but high quality dataset to establish strong baseline readability and response quality.

### Reasoning RL Phase (Capability Building)

![Reasoning RL Phase](https://huggingface.co/reasoning-course/images/resolve/main/grpo/6.png)

The Reasoning RL Phase focuses on developing core reasoning capabilities across domains including mathematics, coding, science, and logic. This phase employs rule-based reinforcement learning, with rewards directly tied to solution correctness. 

Crucially, all the tasks in this phase are 'verifiable' so we can check if the model's answer is correct or not. For example, in the case of mathematics, we can check if the model's answer is correct by using a mathematical solver.

What makes this phase particularly innovative is its direct optimization approach that eliminates the need for a separate reward model, streamlining the training process.

### Rejection Sampling Phase (Quality Control)

![Rejection Sampling Phase](https://huggingface.co/reasoning-course/images/resolve/main/grpo/7.png)

During the Rejection Sampling Phase, the model generates samples which are then filtered through a quality control process. DeepSeek-V3 serves as the quality judge, evaluating outputs across a broad scope that extends beyond pure reasoning tasks. The filtered data is then used for supervised fine-tuning. This phase's innovation lies in its ability to combine multiple quality signals to ensure high-standard outputs.

### Diverse RL Phase (Broad Alignment)

![Diverse RL Phase](https://huggingface.co/reasoning-course/images/resolve/main/grpo/8.png)

The final Diverse RL Phase tackles multiple task types using a sophisticated hybrid approach. For deterministic tasks, it employs rule-based rewards, while subjective tasks are evaluated through LLM feedback. This phase aims to achieve human preference alignment through its innovative hybrid reward approach, combining the precision of rule-based systems with the flexibility of language model evaluation.

## The Algorithm: Group Relative Policy Optimization (GRPO)

Now that we have a good understanding of the training process, let's look at the algorithm that was used to train the model.

The authors describe GRPO as a breakthrough in model fine-tuning:

![GRPO Process](https://huggingface.co/reasoning-course/images/resolve/main/grpo/10.png)

GRPO's novelty lies in its capacity to "directly optimize for preference rectification." This signifies a more direct and efficient route to aligning the model with desired outputs, contrasting with traditional Reinforcement Learning algorithms such as PPO. Let's break down how GRPO works through its three main components.

### Group Formation: Creating Multiple Solutions

The first step in GRPO is remarkably intuitive - it's similar to how a student might solve a difficult problem by trying multiple approaches. When given a prompt, the model doesn't just generate one response; instead, it creates multiple attempts at solving the same problem (usually 4, 8, or 16 different attempts).

Imagine you're teaching a model to solve math problems. For a question about counting chickens on a farm, the model might generate several different solutions:
- One solution might break down the problem step by step: first counting total chickens, then subtracting roosters, and finally accounting for non-laying hens
- Another might use a different but equally valid approach
- Some attempts might contain mistakes or less efficient solutions

All these attempts are kept together as a group, much like having multiple students' solutions to compare and learn from.

![Group Formation](https://huggingface.co/reasoning-course/images/resolve/main/grpo/11.jpg)

### Preference Learning: Understanding What Makes a Good Solution

This is where GRPO really shines in its simplicity. Unlike other methods for RLHF that need always require a separate reward model to predict how good a solution might be, GRPO can use any function or model to evaluate the quality of a solution. For example, we could use a length function to reward shorter responses or a mathematical solver to reward accurate mathematical solutions.

The evaluation process looks at various aspects of each solution:
- Is the final answer correct?
- Did the solution follow proper formatting (like using the right XML tags)?
- Does the reasoning match the answer provided?

What makes this approach particularly clever is how it handles the scoring. Instead of just giving absolute scores, GRPO normalizes the rewards within each group. It uses a simple but effective formula for group relative advantage estimation:

```
Advantage = (reward - mean(group_rewards)) / std(group_rewards)
```

![Preference Learning](https://huggingface.co/reasoning-course/images/resolve/main/grpo/12.jpg)

This normalization is like grading on a curve, but for AI. It helps the model understand which solutions within the group were better or worse compared to their peers, rather than just looking at absolute scores.

### Optimization: Learning from Experience

The final step is where GRPO teaches the model to improve based on what it learned from evaluating the group of solutions. This process is both powerful and stable, using two main principles:

1. It encourages the model to produce more solutions like the successful ones while moving away from less effective approaches
2. It includes a safety mechanism (called KL divergence penalty) that prevents the model from changing too drastically all at once

This approach proves more stable than traditional methods because:
- It looks at multiple solutions together rather than comparing just two at a time
- The group-based normalization helps prevent issues with reward scaling
- The KL penalty acts like a safety net, ensuring the model doesn't forget what it already knows while learning new things

> [!TIP]
> GRPO's key innovations are:
> - Learning directly from any function or model, eliminating the reliance on a separate reward model.
> - Group-based learning, which is more stable and efficient than traditional methods like pairwise comparisons.

This breakdown is complex, but the key takeaway is that GRPO is a more efficient and stable way to train a model to reason. 

### GRPO Algorithm in Pseudocode

Now that we understand the key components of GRPO, let's look at the algorithm in pseudocode. This is a simplified version of the algorithm, but it captures the key ideas.

```
Input: 
- initial_policy: Starting model to be trained
- reward_function: Function that evaluates outputs
- training_prompts: Set of training examples
- group_size: Number of outputs per prompt (typically 4-16)

Algorithm GRPO:
1. For each training iteration:
   a. Set reference_policy = initial_policy (snapshot current policy)
   b. For each prompt in batch:
      i. Generate group_size different outputs using initial_policy
      ii. Compute rewards for each output using reward_function
      iii. Normalize rewards within group:
           normalized_advantage = (reward - mean(rewards)) / std(rewards)
      iv. Update policy by maximizing the clipped ratio:
          min(prob_ratio * normalized_advantage, 
              clip(prob_ratio, 1-epsilon, 1+epsilon) * normalized_advantage)
          - kl_weight * KL(initial_policy || reference_policy)
          
          where prob_ratio is current_prob / reference_prob

Output: Optimized policy model
```

This algorithm shows how GRPO combines group-based advantage estimation with policy optimization while maintaining stability through clipping and KL divergence constraints.

## Results and Impact

Now that we've explored the algorithm, let's look at the results. DeepSeek R1 achieves state-of-the-art performance across multiple domains:

| Domain | Key Results |
|--------|-------------|
| Mathematics | • 79.8% on AIME 2024• 97.3% on MATH-500 |
| Coding | • Codeforces Rating: 2029• LiveCodeBench: 65.9% |
| General Knowledge | • MMLU: 90.8%• GPQA Diamond: 71.5% |
| Language Tasks | • AlpacaEval 2.0: 87.6% win rate• FRAMES: 82.5% |

The model's practical impact extends beyond benchmarks through its cost-effective API pricing ($0.14 per million input tokens) and successful model distillation across various sizes (1.5B to 70B parameters). Notably, even the 7B model achieves 55.5% on AIME 2024, while the 70B distilled version approaches o1-mini performance on MATH-500 (94.5%), demonstrating effective capability preservation at different scales.

## Limitations and Challenges of GRPO

While GRPO represents a significant advancement in reinforcement learning for language models, it's important to understand its limitations and challenges:

- **Generation Cost**: Generating multiple completions (4-16) for each prompt increases computational requirements compared to methods that generate only one or two completions.
- **Batch Size Constraints**: The need to process groups of completions together can limit effective batch sizes, adding complexity to the training process and potentially slowing down training.
- **Reward Function Design**: The quality of training heavily depends on well-designed reward functions. Poorly designed rewards can lead to unintended behaviors or optimization for the wrong objectives.
- **Group Size Tradeoffs**: Choosing the optimal group size involves balancing diversity of solutions against computational cost. Too few samples may not provide enough diversity, while too many increase training time and resource requirements.
- **KL Divergence Tuning**: Finding the right balance for the KL divergence penalty requires careful tuning - too high and the model won't learn effectively, too low and it may diverge too far from its initial capabilities.

## Conclusion

The DeepSeek R1 paper represents a significant milestone in language model development. The Group Relative Policy Optimization (GRPO) algorithm has demonstrated that pure reinforcement learning can indeed develop strong reasoning capabilities, challenging previous assumptions about the necessity of supervised fine-tuning.

Perhaps most importantly, DeepSeek R1 has shown that it's possible to balance high performance with practical considerations like cost-effectiveness and accessibility. The successful distillation of the model's capabilities across different sizes, from 1.5B to 70B parameters, demonstrates a path forward for making advanced AI capabilities more widely available.

---

In the next section, we'll explore practical implementations of these concepts, focusing on how to leverage GRPO and RFTrans in your own language model development projects.

## Quiz

### 1. What is the main innovation of the DeepSeek R1 paper?

### 2. What are the four phases of the DeepSeek R1 training process?

### 3. What is the 'Aha Moment' phenomenon in R1-Zero's training?

### 4. How does GRPO's group formation work?

### 5. What is the key difference between DeepSeek-R1-Zero and DeepSeek-R1?


````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48b99ffc-608c-432a-a251-6460b9ef6084",
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "a98155e9543b5a45d",
  "type": "user",
  "uuid": "f829bd0a-8d56-4bbc-a3f9-0a73f17dec3b",
  "sourceToolAssistantUUID": "48b99ffc-608c-432a-a251-6460b9ef6084",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-29T05:31:54.554Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017YqqCxb2gQwv72MNM9hXu4`</summary>

```json
{
  "url": "https://www.paulswider.com/p/why-deepseekr1-made-natures-cover",
  "prompt": "Extract details about: 1) Why DeepSeek-R1 was significant enough for Nature's cover. 2) Any discussion of the peer review process. 3) Technical contributions highlighted. 4) Criticisms or limitations noted. 5) Robustness or fragility of the approach. 6) Any specific benchmark results or comparisons mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f829bd0a-8d56-4bbc-a3f9-0a73f17dec3b",
  "isSidechain": true,
  "agentId": "a98155e9543b5a45d",
  "requestId": "req_011CbWK4vYft5pB8a2CYz4Cu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "446dd016-5d52-4c5a-9066-1fd3351e9727",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DuubND53ezs4Jjnj8Pxtnp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2019,
      "cache_read_input_tokens": 12151,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2019,
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

_source line 25 · 2026-05-29T05:31:56.571Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JrwqLaddVSHnDv5ycwTN9Q`</summary>

```json
{
  "url": "https://epichka.com/blog/2025/grpo/",
  "prompt": "Extract the complete mathematical formulation of GRPO: the objective function equation, how group advantages A_i are computed, the normalization (mean and std within group), the clipping mechanism (epsilon), the KL divergence term (beta), and how it differs from PPO. Also extract any discussion of why GRPO works well for reasoning tasks and any practical implementation details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "446dd016-5d52-4c5a-9066-1fd3351e9727",
  "isSidechain": true,
  "agentId": "a98155e9543b5a45d",
  "requestId": "req_011CbWK4vYft5pB8a2CYz4Cu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d6fa60c7-2603-4f9c-aee3-478a4e13dfad",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DuubND53ezs4Jjnj8Pxtnp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2019,
      "cache_read_input_tokens": 12151,
      "output_tokens": 583,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2019
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 583,
          "cache_read_input_tokens": 12151,
          "cache_creation_input_tokens": 2019,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2019,
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

_source line 26 · 2026-05-29T05:32:00.489Z_

<details><summary>↩ Tool result · `toolu_017YqqCxb2gQwv72MNM9hXu4`</summary>

```text
# DeepSeek-R1 Analysis

## 1) Significance for Nature's Cover
DeepSeek-R1 earned Nature's feature because it "breaks the human‑trace ceiling" by demonstrating that answer-graded reinforcement learning can produce reasoning behaviors and distill them into smaller, open models—representing both scientific and industry disruption.

## 2) Peer Review Process
The article mentions the work was "peer‑reviewed" and "published online Sept 17, 2025" in Nature, but provides no discussion of the review process itself or timeline details.

## 3) Technical Contributions
The core innovation centers on teaching reasoning through pure reinforcement learning (RL) with rewards tied only to final correct answers, eliminating human step-by-step traces. The model uses GRPO (a PPO variant) and later adds supervised fine-tuning for readability, allowing the system to develop its own reasoning strategies including self-checking and verification.

## 4) Criticisms or Limitations
The document contains no noted criticisms or identified limitations of the approach.

## 5) Robustness or Fragility
No discussion of robustness or fragility is included in the provided content.

## 6) Benchmark Results
On AIME-2024, performance improved from 15.6% to 77.9% pass@1 during RL training, reaching 86.7% with self-consistency—demonstrating that "final-answer rewards alone can grow real reasoning."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "446dd016-5d52-4c5a-9066-1fd3351e9727",
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "a98155e9543b5a45d",
  "type": "user",
  "uuid": "df9f0a44-e751-40b9-8689-47e928076d28",
  "sourceToolAssistantUUID": "446dd016-5d52-4c5a-9066-1fd3351e9727",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-29T05:32:02.922Z_

<details><summary>↩ Tool result · `toolu_01JrwqLaddVSHnDv5ycwTN9Q`</summary>

```text
# GRPO Mathematical Formulation and Key Differences

## Core GRPO Objective Function

The complete GRPO objective is:

$$J_{GRPO}(\theta) = \frac{1}{G}\sum_{i=1}^G \frac{1}{|a_i|}\sum_{t=1}^{|a_i|} \left\{\min\left[\frac{\pi_\theta(a_{i,t} \mid s,a_{i, < t})}{\pi_{\theta_{old}}(a_{i, t}\mid s, a_{i, < t})}\hat{A}_{i,t}, \text{clip}\left(\frac{\pi_\theta(a_{i,t}\mid s, a_{i, < t})}{\pi_{\theta_{old}}(a_{i, t} \mid s, a_{i, < t})}, 1-\epsilon, 1+\epsilon\right)\hat{A}_{i,t}\right] - \beta D_{KL}[\pi_\theta \mid \mid \pi_{ref}]\right\}$$

## Advantage Estimation

Rather than employing a separate value network, GRPO "estimates baseline advantages by normalizing a group (batch) of rewards obtained from sampling multiple different outputs" from the reference policy for identical inputs.

The normalized advantage formula:
$$\hat{A}_{i,t} = \tilde{r}_i = \frac{r_i - \text{mean}(r)}{\text{std}(r)}$$

Per-token rewards include a reference model penalty:
$$r_t = r_\phi(q,a_{\leq t}) - \beta \log\frac{\pi_\theta(a_t \mid q,a_{< t})}{\pi_{ref}(a_t \mid q, a_{< t})}$$

## Key Differences from PPO

GRPO introduces "three key innovations: eliminates the need for a value network, uses group sampling for more efficient stable advantage estimation, uses a more conservative update mechanism through further penalizing both the objective and the rewards."

The clipping mechanism (parameter ε) and KL divergence penalty (parameter β) maintain conservative policy updates, analogous to PPO's safeguards.

## Reasoning Task Applicability

The document does not explicitly explain why GRPO works well for reasoning tasks, only noting DeepSeek's success with mathematical and complex reasoning models using this approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d6fa60c7-2603-4f9c-aee3-478a4e13dfad",
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "a98155e9543b5a45d",
  "type": "user",
  "uuid": "fe5b7f55-9771-48d3-bdcd-e295a60d204a",
  "sourceToolAssistantUUID": "d6fa60c7-2603-4f9c-aee3-478a4e13dfad",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-29T05:32:05.695Z_

Now let me get one final piece on the fragility/robustness discussion.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe5b7f55-9771-48d3-bdcd-e295a60d204a",
  "isSidechain": true,
  "agentId": "a98155e9543b5a45d",
  "requestId": "req_011CbWK6HBvEZHDm9xmyrPCK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f929167-5388-4cdb-ae3a-f5ef8c424e39",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J8DujR6ECTAAshNaG94BSB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5200,
      "cache_read_input_tokens": 14170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5200,
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

_source line 29 · 2026-05-29T05:32:06.326Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WDZSxFLG18YgsmTCCnE2gT`</summary>

```json
{
  "query": "DeepSeek-R1 reward hacking language mixing fragility limitations R1-Zero readability issues training instability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f929167-5388-4cdb-ae3a-f5ef8c424e39",
  "isSidechain": true,
  "agentId": "a98155e9543b5a45d",
  "requestId": "req_011CbWK6HBvEZHDm9xmyrPCK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "56dd9205-8139-4bb5-9056-d7e06c074538",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J8DujR6ECTAAshNaG94BSB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5200,
      "cache_read_input_tokens": 14170,
      "output_tokens": 95,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5200
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 95,
          "cache_read_input_tokens": 14170,
          "cache_creation_input_tokens": 5200,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5200,
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

_source line 30 · 2026-05-29T05:32:14.065Z_

<details><summary>↩ Tool result · `toolu_01WDZSxFLG18YgsmTCCnE2gT`</summary>

```text
Web search results for query: "DeepSeek-R1 reward hacking language mixing fragility limitations R1-Zero readability issues training instability"

Links: [{"title":"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning - HackMD","url":"https://hackmd.io/@shaoeChen/r1UWj4XYkx"},{"title":"Challenges in Ensuring AI Safety in DeepSeek-R1 Models: The Shortcomings   of Reinforcement Learning Strategies","url":"https://arxiv.org/pdf/2501.17030"},{"title":"The internal working of DeepSeek-R1 | Medium","url":"https://medium.com/@asma.fillatre/the-internal-working-of-deepseek-r1-9deb4a07bac1"},{"title":"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning","url":"https://arxiv.org/html/2501.12948v1"},{"title":"DeepSeek-R1 Explained In Detail. DeepSeek-R1: Incentivizing Reasoning… | by Amankaushik | Medium","url":"https://medium.com/@amasick/deepseek-r1-explained-in-detail-ac703f4a0984"},{"title":"Probing RLVR training instability through the lens of objective-level hacking","url":"https://arxiv.org/pdf/2602.01103"},{"title":"Paper Review: DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning | by Andrew Lukyanenko | Medium","url":"https://artgor.medium.com/paper-review-deepseek-r1-incentivizing-reasoning-capability-in-llms-via-reinforcement-learning-edf4343dcf3a"},{"title":"DeepSeek-R1: Incentivizing Reasoning Capability in Large Language Models via Reinforcement Learning — Paper Understanding | by DhanushKumar | Medium","url":"https://medium.com/@danushidk507/deepseek-r1-incentivizing-reasoning-capability-in-large-language-models-via-reinforcement-learning-9515a28a23ad"},{"title":"DeepSeek-R1: Incentivizing reasoning capability in LLMs via reinforcement learning · Pablo Stafforini","url":"https://stafforini.com/works/deepseek-ai-2025-deepseek-r-1-incentivizing/"}]

Based on the search results, here's what I found regarding DeepSeek-R1's limitations and challenges:

## Key Limitations and Issues

**Training Instability and Readability Problems:**
DeepSeek-R1-Zero training was conducted directly with reinforcement learning (RL), which resulted in unstable convergence during the initial stages. The model encounters challenges such as poor readability and language mixing.

**Specific Challenges with Pure RL Approach:**
Pure RL led to problems such as incoherent outputs, language mixing, and poor readability. Additionally, while RL improves reasoning capabilities, it faces challenges such as reward hacking, generalization failures, language mixing, and high computational costs.

**Solutions Implemented:**
To address these issues, DeepSeek-R1 incorporates multi-stage training and cold-start data before RL. The cold-start data is designed for readability, with a structured format addressing language mixing and lack of clarity observed in DeepSeek-R1-Zero.

**Performance Trade-offs:**
DeepSeek-R1-Zero relies solely on RL without supervised fine-tuning, achieving notable reasoning benchmarks but struggling with readability and language mixing, while DeepSeek-R1 incorporates a multi-stage training pipeline, starting with cold-start data and iterative RL, surpassing OpenAI-o1–1217 in reasoning tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56dd9205-8139-4bb5-9056-d7e06c074538",
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "a98155e9543b5a45d",
  "type": "user",
  "uuid": "acfe8f6f-01f0-458a-916c-095e80e4842a",
  "sourceToolAssistantUUID": "56dd9205-8139-4bb5-9056-d7e06c074538",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-29T05:33:12.913Z_

I now have comprehensive information from all sources. Here is the detailed summary.

---

## DeepSeek-R1: Detailed Research Summary

### Problem and Gap

DeepSeek-AI identified that while chain-of-thought prompting had shown promise for eliciting reasoning in LLMs, all existing approaches were heavily contingent on extensive human-annotated reasoning trajectories (step-by-step supervision). This created a bottleneck: producing high-quality reasoning traces is expensive, does not scale, and may inadvertently constrain the model's reasoning strategies to mimic human patterns rather than discover potentially superior ones. The core question they posed was whether pure reinforcement learning, without any supervised fine-tuning on reasoning demonstrations, could develop genuine reasoning capabilities from scratch.

### Key Insight: Pure RL for Reasoning

The central insight is that final-answer rewards alone -- without process supervision or human-written chain-of-thought data -- can grow real reasoning behaviors. By rewarding only correctness of the final answer on verifiable tasks (math, code), the model autonomously develops intermediate reasoning strategies including self-checking, backtracking, and dynamic strategy adaptation. This was first demonstrated with DeepSeek-R1-Zero (pure RL, no SFT), which improved AIME 2024 pass@1 from 15.6% to 71.0% during training, proving that supervised reasoning traces are not a prerequisite for reasoning capability.

### GRPO Algorithm: Technical Details

Group Relative Policy Optimization (GRPO) is the core training algorithm, a variant of PPO with three key innovations:

1. **Elimination of the value network.** Standard PPO requires a separate critic/value model of comparable size to the policy, roughly doubling memory. GRPO removes this entirely, reducing memory requirements by 40-60%.

2. **Group sampling and relative advantage estimation.** For each prompt, the model generates G outputs (typically 4-16). Each output receives a scalar reward. The advantage is computed by normalizing within the group:

   `A_i = (r_i - mean(r)) / std(r)`

   This "grading on a curve" approach provides a stable baseline without a learned value function.

3. **Conservative update mechanism.** The objective combines PPO-style clipped ratios with a KL divergence penalty against a reference policy:

   `J_GRPO(theta) = (1/G) * sum_i (1/|a_i|) * sum_t [ min( ratio * A_i, clip(ratio, 1-eps, 1+eps) * A_i ) - beta * D_KL(pi_theta || pi_ref) ]`

   where `ratio = pi_theta(a_t | s, a_{&lt;t}) / pi_theta_old(a_t | s, a_{&lt;t})`. The clipping (epsilon) and KL penalty (beta) together prevent catastrophic policy drift.

**Reward structure:** For R1-Zero, only two reward signals are used: (1) an accuracy reward checking whether the final answer is correct (binary, via mathematical solvers or code test cases), and (2) a format reward enforcing structured output (e.g., proper use of `&lt;think>` tags). Notably, no process reward model is used -- this is pure outcome-based reinforcement learning (RLVR).

### Training Pipeline (Four Stages)

**Stage 1 -- Cold Start (Quality Foundation):** DeepSeek-V3-Base is fine-tuned on thousands of validated high-quality reasoning samples collected from R1-Zero outputs. This small but curated SFT step addresses the readability and language-mixing problems observed in pure RL, establishing a readable baseline.

**Stage 2 -- Reasoning RL (Capability Building):** GRPO is applied on verifiable tasks (mathematics, coding, science, logic) using rule-based rewards tied to solution correctness. All tasks are chosen to be automatically verifiable, eliminating the need for a learned reward model.

**Stage 3 -- Rejection Sampling + SFT (Quality Control):** The RL-trained model generates many candidate solutions. DeepSeek-V3 acts as a quality judge, filtering outputs across diverse tasks (extending beyond pure reasoning). The filtered high-quality data is used for another round of supervised fine-tuning, broadening capability beyond verifiable domains.

**Stage 4 -- Diverse RL (Broad Alignment):** A final RL phase handles multiple task types with a hybrid reward approach: rule-based rewards for deterministic/verifiable tasks, and LLM-as-judge feedback for subjective tasks. This achieves human preference alignment across the full task distribution.

### Emergent Behaviors

During R1-Zero training (pure RL, no SFT), several behaviors emerged spontaneously:

- **Self-reflection:** The model learns to question its own intermediate answers ("But wait, let me reconsider...").
- **Verification:** It checks its solutions by substituting answers back or trying alternative approaches.
- **Backtracking:** When detecting errors, it abandons a reasoning path and restarts with a different strategy.
- **"Aha moments":** The model exhibits sudden realizations mid-chain, recognizing errors and correcting course -- analogous to human insight experiences. These were not programmed but emerged naturally from RL optimization.

### Quantitative Results

| Benchmark | DeepSeek-R1 Score |
|-----------|------------------|
| AIME 2024 | 79.8% pass@1 (86.7% with self-consistency) |
| MATH-500 | 97.3% |
| GPQA Diamond | 71.5% |
| Codeforces Rating | 2029 |
| LiveCodeBench | 65.9% |
| MMLU | 90.8% |
| AlpacaEval 2.0 | 87.6% win rate |

R1-Zero alone reached 71.0% on AIME 2024. The full R1 pipeline pushed this to 79.8%. Total post-training compute was approximately 147K H800 GPU-hours -- an order of magnitude below comparable systems like OpenAI's o1.

**Distillation:** Capabilities were successfully distilled to smaller models (1.5B to 70B parameters). The 7B distilled model achieves 55.5% on AIME 2024; the 70B version reaches 94.5% on MATH-500, approaching o1-mini performance.

### Fragility and Limitations

- **Language mixing:** R1-Zero exhibits chaotic mixing of languages (e.g., Chinese and English within a single chain of thought), a direct artifact of pure RL without language consistency constraints.
- **Readability degradation:** Pure RL outputs are often incoherent or poorly formatted, motivating the cold-start SFT stage.
- **Reward hacking risk:** The quality of training depends critically on well-designed reward functions; poorly specified rewards lead to unintended optimization. The paper addresses this partly through the format reward and multi-stage pipeline.
- **Training instability:** Early stages of R1-Zero training showed unstable convergence, requiring careful hyperparameter management (KL coefficient beta, clipping epsilon, group size).
- **GRPO-specific tradeoffs:** Generating 4-16 completions per prompt increases compute; group size selection involves balancing solution diversity against cost; KL divergence coefficient requires careful tuning (too high suppresses learning, too low causes policy collapse).
- **Safety concerns:** Independent analysis (arxiv 2501.17030) found shortcomings in RL-based safety alignment, with the model sometimes producing unsafe outputs that pure RL strategies failed to prevent.

### Publication Significance

Published as a Nature cover article (Volume 645, Issue 8081, September 18, 2025) with the tagline "Self-Help: Reinforcement learning teaches AI model to improve itself." It underwent three rounds of peer review with eight reviewers producing 64 pages of reports over five months (February-July 2025), supplemented by 83 pages of supplementary material. It is the first mainstream LLM to undergo rigorous peer review in a top-tier scientific journal.

---

Sources:
- [arXiv Abstract Page](https://arxiv.org/abs/2501.12948)
- [Hugging Face LLM Course - Understanding DeepSeek R1](https://huggingface.co/learn/llm-course/chapter12/3)
- [GRPO Illustrated Breakdown - Ebrahim Pichka](https://epichka.com/blog/2025/grpo/)
- [Why DeepSeek-R1 Made Nature's Cover - Paul Swider](https://www.paulswider.com/p/why-deepseekr1-made-natures-cover)
- [Critical Review - Springer Nature / Discover AI](https://link.springer.com/article/10.1007/s44163-026-01131-4)
- [CSPaper Forum - Behind the Scenes](https://forum.cspaper.org/topic/160/behind-the-scenes-of-deepseek-r1-a-landmark-in-ai-published-in-nature)
- [GRPO Substack Explainer](https://chessman7.substack.com/p/grpo-group-relative-policy-optimization)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acfe8f6f-01f0-458a-916c-095e80e4842a",
  "isSidechain": true,
  "agentId": "a98155e9543b5a45d",
  "requestId": "req_011CbWK76p7VnyUfQqbdUKZM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ffc861c-7455-451f-b6c7-85844a450da7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YDspj7R6dxqwJoUkVAxu6f",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1069,
      "cache_read_input_tokens": 19370,
      "output_tokens": 2177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1069
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2177,
          "cache_read_input_tokens": 19370,
          "cache_creation_input_tokens": 1069,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1069,
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
