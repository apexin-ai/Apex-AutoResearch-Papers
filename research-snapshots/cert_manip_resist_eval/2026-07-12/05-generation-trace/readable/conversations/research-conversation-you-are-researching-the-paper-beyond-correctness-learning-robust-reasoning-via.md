# Research conversation: You are researching the paper "Beyond Correctness: Learning Robust Reasoning via Transfer (RLTR)" by Lee et al. (arXiv 2

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-afe027cf2c088322c.jsonl`
- **Structured JSON:** [`4cc9f8e29a031ad09dca.json`](../../sessions/4c/4cc9f8e29a031ad09dca.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

22 recorded events

### User

_source line 1 · 2026-05-29T05:31:05.934Z_

You are researching the paper "Beyond Correctness: Learning Robust Reasoning via Transfer (RLTR)" by Lee et al. (arXiv 2026). URL: https://arxiv.org/abs/2602.08489

Tasks:
1. Use WebFetch to read the arxiv abstract page for this paper.
2. Use WebFetch to read the HTML version for method details (try https://arxiv.org/html/2602.08489).
3. Search for any reviews, discussion, or citation context for this paper using WebSearch.

For each source, extract:
- The exact problem/gap they identified (what's wrong with standard RL correctness reward)
- Their key insight about "transfer reward" and reasoning robustness
- Technical method: how transfer reward works (partial reasoning prefixes guiding separate models), how this encourages stable reasoning
- The claim about 2.5x fewer training steps
- Specific quantitative results on math benchmarks
- How they define/measure "robustness" vs our invariance-based definition

Return a detailed summary (under 1500 words). This paper is a key comparison since it also addresses reasoning robustness in RL training but uses a different mechanism than consistency regularization.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "afe027cf2c088322c",
  "type": "user",
  "uuid": "e736205d-7339-4c62-abc9-6fdaba9cf1b1",
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

_source line 2 · 2026-05-29T05:31:05.937Z_

```json
{
  "parentUuid": "e736205d-7339-4c62-abc9-6fdaba9cf1b1",
  "isSidechain": true,
  "agentId": "afe027cf2c088322c",
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
  "uuid": "f1498ade-64c4-470f-8487-6daa91affcdd",
  "timestamp": "2026-05-29T05:31:05.937Z",
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

_source line 3 · 2026-05-29T05:31:05.938Z_

```json
{
  "parentUuid": "f1498ade-64c4-470f-8487-6daa91affcdd",
  "isSidechain": true,
  "agentId": "afe027cf2c088322c",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5557b137-176c-417a-9155-4dabc0551a58",
  "timestamp": "2026-05-29T05:31:05.938Z",
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

_source line 4 · 2026-05-29T05:31:09.701Z_



I'll research this paper by fetching the arxiv page, HTML version, and searching for discussions. Let me start by loading the WebFetch and WebSearch tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5557b137-176c-417a-9155-4dabc0551a58",
  "isSidechain": true,
  "agentId": "afe027cf2c088322c",
  "requestId": "req_011CbWK25V6kJQbqSfqEsiA7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4309070d-ba99-47c4-a0b0-c13a91cb0c9e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011a5JqaYSDtTJtAuVR3RFJF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1608,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1608,
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

_source line 5 · 2026-05-29T05:31:09.925Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KRRwji1MGDPGXq394x4fdy`</summary>

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
  "parentUuid": "4309070d-ba99-47c4-a0b0-c13a91cb0c9e",
  "isSidechain": true,
  "agentId": "afe027cf2c088322c",
  "requestId": "req_011CbWK25V6kJQbqSfqEsiA7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "62715029-dfc4-4ffd-816d-146a56cf2919",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011a5JqaYSDtTJtAuVR3RFJF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1608,
      "cache_read_input_tokens": 7413,
      "output_tokens": 116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1608
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 116,
          "cache_read_input_tokens": 7413,
          "cache_creation_input_tokens": 1608,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1608,
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

_source line 6 · 2026-05-29T05:31:09.929Z_

<details><summary>↩ Tool result · `toolu_01KRRwji1MGDPGXq394x4fdy`</summary>

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
  "parentUuid": "62715029-dfc4-4ffd-816d-146a56cf2919",
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "afe027cf2c088322c",
  "type": "user",
  "uuid": "b3c0d45b-2198-440f-94a7-51308a57356a",
  "sourceToolAssistantUUID": "62715029-dfc4-4ffd-816d-146a56cf2919",
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

_source line 7 · 2026-05-29T05:31:12.094Z_



Now let me fetch all three sources in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3c0d45b-2198-440f-94a7-51308a57356a",
  "isSidechain": true,
  "agentId": "afe027cf2c088322c",
  "requestId": "req_011CbWK2Nih2aCu3i5bbvAkq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a2b2afea-15a0-42cd-80d4-f86cab3a61b1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CSJoQ7v3YH2fWktaKpk7bB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1138,
      "cache_read_input_tokens": 9021,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1138,
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

_source line 8 · 2026-05-29T05:31:14.882Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BGsfGLEWyfGYsvmeT5ZSyR`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.08489",
  "prompt": "Extract the full abstract, paper title, authors, and any other metadata from this arxiv abstract page for the paper \"Beyond Correctness: Learning Robust Reasoning via Transfer\". Include the exact problem statement, key contributions, and any quantitative results mentioned in the abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2b2afea-15a0-42cd-80d4-f86cab3a61b1",
  "isSidechain": true,
  "agentId": "afe027cf2c088322c",
  "requestId": "req_011CbWK2Nih2aCu3i5bbvAkq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "06e3c450-0f51-464e-a701-765c97164164",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CSJoQ7v3YH2fWktaKpk7bB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1138,
      "cache_read_input_tokens": 9021,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1138,
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

_source line 9 · 2026-05-29T05:31:19.209Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01G1isbKgfvwp3p5fa29y2sW`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.08489",
  "prompt": "Extract detailed information about the paper's method, including: 1) The exact problem/gap they identify with standard RL correctness reward for reasoning. 2) Their key insight about \"transfer reward\" and reasoning robustness. 3) Technical details of how transfer reward works (partial reasoning prefixes, guiding separate models). 4) How they define and measure \"robustness\". 5) Any claims about training efficiency (e.g. 2.5x fewer training steps). 6) Specific quantitative results on math benchmarks (exact numbers, percentages, benchmark names). 7) Experimental setup details. 8) Comparisons to baselines."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06e3c450-0f51-464e-a701-765c97164164",
  "isSidechain": true,
  "agentId": "afe027cf2c088322c",
  "requestId": "req_011CbWK2Nih2aCu3i5bbvAkq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf315807-cf01-49cc-a0a2-cc26db2632f6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CSJoQ7v3YH2fWktaKpk7bB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1138,
      "cache_read_input_tokens": 9021,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1138,
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

_source line 10 · 2026-05-29T05:31:19.639Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B9bDhEmLxqPKZHuS2QVH99`</summary>

```json
{
  "query": "\"Beyond Correctness: Learning Robust Reasoning via Transfer\" RLTR Lee 2026 arxiv review discussion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf315807-cf01-49cc-a0a2-cc26db2632f6",
  "isSidechain": true,
  "agentId": "afe027cf2c088322c",
  "requestId": "req_011CbWK2Nih2aCu3i5bbvAkq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "90d582ba-87b2-48d5-89f9-6d7125553aca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CSJoQ7v3YH2fWktaKpk7bB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1138,
      "cache_read_input_tokens": 9021,
      "output_tokens": 418,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1138
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 418,
          "cache_read_input_tokens": 9021,
          "cache_creation_input_tokens": 1138,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1138,
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

_source line 11 · 2026-05-29T05:31:19.977Z_

<details><summary>↩ Tool result · `toolu_01BGsfGLEWyfGYsvmeT5ZSyR`</summary>

```text
# Paper Metadata & Summary

**Title:** Beyond Correctness: Learning Robust Reasoning via Transfer

**Authors:** Hyunseok Lee, Soheil Abbasloo, Jihoon Tack, Jinwoo Shin

**arXiv ID:** 2602.08489

**Submission Date:** February 9, 2026

**Subjects:** Machine Learning (cs.LG); Computation and Language (cs.CL)

---

## Problem Statement

The authors identify a gap in existing reinforcement learning approaches for LLMs: "its focus on final answer correctness leaves a critical gap: it does not ensure the robustness of the reasoning process itself." Current methods optimize for answer accuracy but neglect whether reasoning remains meaningful across different contexts.

## Key Contribution

The team introduces RLTR (Reinforcement Learning with Transferable Reward), which operationalizes robustness through transfer rewards. This approach "tests whether a partial reasoning prefix from one model can guide a separate model to the correct answer," encouraging stable and generalizable reasoning.

## Quantitative Results

- **MATH500 benchmark:** Achieves a +3.6 percentage point gain in Maj@64 compared to RLVR
- **Training efficiency:** Matches RLVR's average accuracy using roughly 2.5x fewer training steps
- **Additional benefit:** Improves sampling consistency alongside final answer accuracy
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06e3c450-0f51-464e-a701-765c97164164",
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "afe027cf2c088322c",
  "type": "user",
  "uuid": "7411b0eb-6ff5-4964-94b8-4c59725c6b7a",
  "sourceToolAssistantUUID": "06e3c450-0f51-464e-a701-765c97164164",
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

_source line 12 · 2026-05-29T05:31:28.047Z_

<details><summary>↩ Tool result · `toolu_01B9bDhEmLxqPKZHuS2QVH99`</summary>

```text
Web search results for query: ""Beyond Correctness: Learning Robust Reasoning via Transfer" RLTR Lee 2026 arxiv review discussion"

Links: [{"title":"Beyond Correctness: Learning Robust Reasoning via Transfer","url":"https://arxiv.org/html/2602.08489"},{"title":"[2602.08489] Beyond Correctness: Learning Robust Reasoning via Transfer","url":"https://arxiv.org/abs/2602.08489"},{"title":"Beyond Correctness: Learning Robust Reasoning via Transfer","url":"https://www.arxiv.org/pdf/2602.08489"},{"title":"Beyond High-Entropy Exploration: Correctness-Aware Low-Entropy Segment-Based Advantage Shaping for Reasoning LLMs","url":"https://arxiv.org/pdf/2512.00908"},{"title":"Beyond Correctness: Confidence-Aware Reward Modeling for Enhancing Large Language Model Reasoning","url":"https://arxiv.org/html/2511.07483"},{"title":"Beyond Correctness: Exposing LLM-generated Logical Flaws in Reasoning via Multi-step Automated Theorem Proving","url":"https://arxiv.org/html/2512.23511v1"},{"title":"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training","url":"https://arxiv.org/html/2509.03403v1"}]

I found the paper! Here's what I discovered about "Beyond Correctness: Learning Robust Reasoning via Transfer":

## Overview

The paper introduces Reinforcement Learning with Transferable Reward (RLTR), which operationalizes robustness via transfer reward that tests whether a partial reasoning prefix from one model can guide a separate model to the correct answer.

## Key Motivation

While Reinforcement Learning with Verifiable Rewards (RLVR) has recently strengthened LLM reasoning, its focus on final answer correctness leaves a critical gap: it does not ensure the robustness of the reasoning process itself. The authors adopt the philosophical view that robust reasoning should remain useful beyond the mind that produced it, and treat reasoning as a form of meaning transfer that must survive truncation, reinterpretation, and continuation.

## Key Results

RLTR encourages LLMs to produce reasoning that is stable, interpretable, and genuinely generalizable, while improving sampling consistency and improving final-answer accuracy, and reaching comparable performance in substantially fewer training steps. For example, on MATH-500, RLTR achieves a +3.6%p gain in Maj@64 compared to RLVR and matches RLVR's average accuracy with roughly 2.5× fewer training steps.

## Evaluation

The paper evaluates on two medium-difficulty math reasoning benchmarks, MATH-500 and GSM8K, as well as two more challenging benchmarks, AIME2024 and AMC23.

The paper was published on arxiv on February 9, 2026, with ID 2602.08489.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "90d582ba-87b2-48d5-89f9-6d7125553aca",
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "afe027cf2c088322c",
  "type": "user",
  "uuid": "c8f52700-737a-47c9-a9a9-5c15d837d86c",
  "sourceToolAssistantUUID": "90d582ba-87b2-48d5-89f9-6d7125553aca",
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

_source line 13 · 2026-05-29T05:31:38.168Z_

<details><summary>↩ Tool result · `toolu_01G1isbKgfvwp3p5fa29y2sW`</summary>

````text
# RLTR: Learning Robust Reasoning via Transfer - Detailed Analysis

## 1. Problem Identified with Standard RL Correctness Reward

The paper identifies a critical gap in RLVR (Reinforcement Learning with Verifiable Reward): "RLVR optimizes reasoning solely through final-answer correctness, leaving a critical dimension of reasoning quality underexplored: the robustness of the reasoning process itself."

They observe that while RLVR improves single-sample accuracy, it actually degrades multi-sample consistency. Specifically, on MATH-500, RLVR's Maj@16 performance decreased from 81.2% (base model) to 80.2%, suggesting reasoning becomes brittle with more samples.

## 2. Key Insight: Transfer Reward and Robustness

The core concept is **reasoning transferability**: "the extent to which a reasoning prefix produced by one model can be completed by another model to reach a verifiably correct answer."

Their philosophical motivation is compelling: "robust reasoning should remain useful beyond the mind that produced it." They operationalize this by truncating generated reasoning and asking a separate receiver model to complete it successfully.

## 3. Technical Implementation of Transfer Reward

**Process:**
- Generator model produces full reasoning: `y_gen ~ M_gen(·|x)`
- Reasoning is truncated at ratio τ ∈ (0,1]: `ℓ = ⌊τ|y_gen|⌋`
- Frozen receiver model completes it: `y_rcv ~ M_rcv(·|x, y_gen[:ℓ])`
- Transfer reward checks if receiver reaches correct answer: `R_trans = 𝟙[answer(y_rcv) = y_gt]`

They sample τ uniformly between 0.3 and 0.9 to prevent overfitting to fixed truncation boundaries.

**Combined Reward:**
```
R_RLTR = R_RLVR + t·R_trans
```
where t is the transfer reward weight.

## 4. How Robustness is Defined and Measured

Robustness is operationalized through two metrics:

- **Majority Voting (Maj@K)**: Consensus correctness across K stochastic samples. Higher Maj@K indicates more consistent reasoning across variations.
- **Transferability**: Direct measurement of whether truncated prefixes enable receiver models to reach correct answers at various truncation ratios (0.3-0.9).

The paper shows these correlate: "transferability follows Maj@64" across training dynamics, providing evidence their approach captures genuine robustness.

## 5. Training Efficiency Claims

Major efficiency claim: "RLTR matches RLVR's average accuracy with roughly 2.5×2.5 fewer training steps" on MATH-500.

From Figure 2(a) and Table 4: RLTR reaches 76.8% accuracy in 40 training steps, while RLVR requires 100 steps for 76.2% accuracy. Despite adding ~7% per-step computational overhead via receiver inference, total FLOPs to reach comparable performance are reduced by approximately 57%.

## 6. Quantitative Results on Math Benchmarks

**Moderate-Difficulty Tasks:**

| Benchmark | Metric | Base | RLVR | RLTR |
|-----------|--------|------|------|------|
| MATH-500 | Acc. | 71.0% | 76.2% | 77.0% |
| MATH-500 | Maj@64 | 82.6% | 82.2% | 84.2% |
| GSM8K | Acc. | 89.1% | 89.4% | 92.0% |
| GSM8K | Maj@64 | 93.3% | 92.9% | 94.2% |

**Hard Benchmarks:**

| Benchmark | Metric | Base | RLVR | RLTR |
|-----------|--------|------|------|------|
| AIME2024 | Acc. | 9.8% | 11.6% | 14.8% |
| AIME2024 | Maj@64 | 16.7% | 18.9% | 21.1% |
| AMC23 | Acc. | 46.2% | 52.8% | 53.5% |
| AMC23 | Maj@64 | 60.8% | 61.7% | 67.5% |

The gains are most pronounced on harder benchmarks. For AMC23, they improve Maj@64 by +5.8 percentage points versus RLVR.

## 7. Experimental Setup Details

**Training Configuration:**
- Generator: Qwen2.5-7B-Instruct
- Receiver: Qwen2.5-3B-Instruct (primary)
- Training data: 3K MATH subset (difficulty ≥ 3)
- Hyperparameters: reward weights a=0.1 (answer), t=1.0 (transfer)
- Algorithm: GRPO (Group Relative Policy Optimization)
- Truncation ratio sampling: uniform between 0.3-0.9

**Evaluation:**
- Metrics: Average accuracy and Maj@K (K ∈ {4,16,64})
- Temperature: T=1.0 for consistent sampling
- Three random seeds with averaged results
- Benchmarks: MATH-500 (in-distribution), GSM8K, AMC23, AIME2024, GPQA (all out-of-distribution except MATH-500)

## 8. Comparisons to Baselines

**Primary Baseline:** RLVR with identical initialization, training data, and evaluation protocol.

**Key Comparative Findings:**

1. **Consistency Over Accuracy**: RLVR prioritizes single-sample accuracy but creates brittle reasoning. RLTR trades minimal accuracy gains for substantial consistency improvements (Maj@64 gains of 2-6 points).

2. **Ablation Results**: 
   - Increasing transfer reward weight (t) improves high-K metrics substantially
   - Receiver model capacity matters for robustness; stronger receivers improve Maj@K more than single-sample accuracy
   - With (a=0.1, t=1.0), Maj@64 improves from 82.2% to 84.2% on MATH-500

3. **Diversity Preservation**: Unlike RLVR which reduces Pass@K (at-least-one-correct metric), RLTR preserves meaningful solution diversity while improving consistency.

4. **Generalization**: Results hold across different LLM families (tested Llama3.1-8B) and domains (GPQA scientific reasoning benchmark).
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf315807-cf01-49cc-a0a2-cc26db2632f6",
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "afe027cf2c088322c",
  "type": "user",
  "uuid": "d96ef4de-862d-437a-9e92-75cf1b966dc0",
  "sourceToolAssistantUUID": "bf315807-cf01-49cc-a0a2-cc26db2632f6",
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

_source line 14 · 2026-05-29T05:31:42.327Z_

Let me search for more discussion and citation context around this paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d96ef4de-862d-437a-9e92-75cf1b966dc0",
  "isSidechain": true,
  "agentId": "afe027cf2c088322c",
  "requestId": "req_011CbWK4TfQ4oBpR7W67Cwwe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf2403c9-1c25-4c73-a7e0-fbace9a051ca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01658oWB5A9Tebu9jgSHwA8s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 757,
      "cache_creation_input_tokens": 2422,
      "cache_read_input_tokens": 10159,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2422,
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

_source line 15 · 2026-05-29T05:31:42.744Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KqbuG35knfWVnwb8X2Ncw8`</summary>

```json
{
  "query": "RLTR \"transfer reward\" reasoning robustness LLM reinforcement learning 2026 discussion blog"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf2403c9-1c25-4c73-a7e0-fbace9a051ca",
  "isSidechain": true,
  "agentId": "afe027cf2c088322c",
  "requestId": "req_011CbWK4TfQ4oBpR7W67Cwwe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e435bd0-2be3-40ec-9c69-5b837ed3f033",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01658oWB5A9Tebu9jgSHwA8s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 757,
      "cache_creation_input_tokens": 2422,
      "cache_read_input_tokens": 10159,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2422,
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

_source line 16 · 2026-05-29T05:31:43.305Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KH68yrwAasoRG8aHPE9JCT`</summary>

```json
{
  "query": "arxiv 2602.08489 cited by discussion reasoning robustness RL training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e435bd0-2be3-40ec-9c69-5b837ed3f033",
  "isSidechain": true,
  "agentId": "afe027cf2c088322c",
  "requestId": "req_011CbWK4TfQ4oBpR7W67Cwwe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f5ab907-d66c-4cb3-9332-ade477a79d37",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01658oWB5A9Tebu9jgSHwA8s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 757,
      "cache_creation_input_tokens": 2422,
      "cache_read_input_tokens": 10159,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2422,
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

_source line 17 · 2026-05-29T05:31:49.830Z_

<details><summary>↩ Tool result · `toolu_01KH68yrwAasoRG8aHPE9JCT`</summary>

```text
Web search results for query: "arxiv 2602.08489 cited by discussion reasoning robustness RL training"

Links: [{"title":"[2602.08489] Beyond Correctness: Learning Robust Reasoning via Transfer","url":"https://arxiv.org/abs/2602.08489"},{"title":"Beyond Correctness: Learning Robust Reasoning via Transfer","url":"https://www.arxiv.org/pdf/2602.08489"},{"title":"Reasoning as an Adaptive Defense for Safety","url":"https://arxiv.org/pdf/2507.00971"},{"title":"Escaping the Verifier: Learning to Reason via Demonstrations","url":"https://arxiv.org/pdf/2511.21667"},{"title":"On the Interplay of Pre-Training, Mid-Training, and RL on Reasoning Language Models","url":"https://arxiv.org/pdf/2512.07783"},{"title":"Robust Reinforcement Learning using Adversarial Populations","url":"https://arxiv.org/pdf/2008.01825"},{"title":"RL for Reasoning by Adaptively Revealing Rationales","url":"https://arxiv.org/html/2506.18110v1"},{"title":"Feasible Adversarial Robust Reinforcement Learning for Underspecified   Environments","url":"https://arxiv.org/pdf/2207.09597"},{"title":"ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models","url":"https://arxiv.org/pdf/2505.24864"}]

Based on the search results, I found the arxiv paper 2602.08489:

**The paper is titled "Beyond Correctness: Learning Robust Reasoning via Transfer" and addresses how Reinforcement Learning with Verifiable Rewards (RLVR) has strengthened LLM reasoning, but does not ensure the robustness of the reasoning process itself.**

The authors introduce Reinforcement Learning with Transferable Reward (RLTR), which operationalizes robustness via transfer reward that tests whether a partial reasoning prefix from one model can guide a separate model to the correct answer. This approach encourages LLMs to produce reasoning that is stable, interpretable, and genuinely generalizable, improving sampling consistency while improving final answer accuracy.

RLTR is described as the first RLVR framework that directly incentivizes LLMs to produce reasoning traces that are transferable across models. For example, on AMC23, RLTR improves Maj@64 from 61.7 to 67.5 compared to RLVR.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f5ab907-d66c-4cb3-9332-ade477a79d37",
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "afe027cf2c088322c",
  "type": "user",
  "uuid": "1902fd12-c713-46a0-9fbd-a8c9b8c43941",
  "sourceToolAssistantUUID": "2f5ab907-d66c-4cb3-9332-ade477a79d37",
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

_source line 18 · 2026-05-29T05:31:51.549Z_

<details><summary>↩ Tool result · `toolu_01KqbuG35knfWVnwb8X2Ncw8`</summary>

```text
Web search results for query: "RLTR "transfer reward" reasoning robustness LLM reinforcement learning 2026 discussion blog"

Links: [{"title":"Beyond Correctness: Learning Robust Reasoning via Transfer","url":"https://arxiv.org/html/2602.08489"},{"title":"Beyond Correctness: Learning Robust Reasoning via Transfer","url":"https://www.arxiv.org/pdf/2602.08489"},{"title":"[2602.08489] Beyond Correctness: Learning Robust Reasoning via Transfer","url":"https://arxiv.org/abs/2602.08489"},{"title":"LLM RLVR: Optimizing with Verifiable Rewards","url":"https://www.emergentmind.com/topics/llm-rlvr"},{"title":"Towards Generalizable Reasoning: Group Causal Counterfactual Policy Optimization for LLM Reasoning","url":"https://arxiv.org/pdf/2602.06475"},{"title":"Enhanced LLM Reasoning by Optimizing Reward Functions with Search-Driven Reinforcement Learning","url":"https://arxiv.org/html/2605.02073v1"},{"title":"[2602.09305] Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation","url":"https://arxiv.org/abs/2602.09305"},{"title":"Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation","url":"https://arxiv.org/html/2602.09305v1"}]

Based on the search results, here's what I found about RLTR and related discussions:

## RLTR: Reinforcement Learning with Transferable Reward

RLTR (Reinforcement Learning with Transferable Reward) introduces a method that operationalizes robustness via transfer reward, which tests whether a partial reasoning prefix from one model can guide a separate model to the correct answer.

The approach treats reasoning as a form of meaning transfer that must survive truncation, reinterpretation, and continuation. This encourages LLMs to produce reasoning that is stable, interpretable, and genuinely generalizable.

## Performance Results

On MATH-500, RLTR achieves a +3.6% gain in Maj@64 compared to RLVR and matches RLVR's average accuracy with roughly 2.5× fewer training steps. The approach improves sampling consistency while improving final-answer accuracy, and it reaches comparable performance in substantially fewer training steps.

## Related Research Context

The search results also reveal broader 2026 discussions around LLM reasoning robustness, including extensions like Contrastive Policy Optimization (CLIPO) that augment verifiable reward signals and help reinforce structural invariances across math and QA benchmarks.

These findings appear in recent academic preprints from February 2026, representing cutting-edge work in reinforcement learning for LLM reasoning robustness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e435bd0-2be3-40ec-9c69-5b837ed3f033",
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "afe027cf2c088322c",
  "type": "user",
  "uuid": "afc6499e-89aa-416a-9cf5-8e7742033f2c",
  "sourceToolAssistantUUID": "1e435bd0-2be3-40ec-9c69-5b837ed3f033",
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

_source line 19 · 2026-05-29T05:31:53.991Z_

Let me also try to find any community discussion or blog posts about this paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "afc6499e-89aa-416a-9cf5-8e7742033f2c",
  "isSidechain": true,
  "agentId": "afe027cf2c088322c",
  "requestId": "req_011CbWK5SRm9HLAWwbYJdR9k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2ee3e3d-061b-4e3e-81f3-34dc697ca0c1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RbEUvn5hrg2djRxp3RLQb2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 661,
      "cache_creation_input_tokens": 1649,
      "cache_read_input_tokens": 12581,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1649,
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

_source line 20 · 2026-05-29T05:31:54.437Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017XwQVwLd7jf4z7yBfd1CML`</summary>

```json
{
  "query": "\"reasoning robustness\" \"transfer reward\" RLVR consistency Maj@64 Qwen training efficiency 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2ee3e3d-061b-4e3e-81f3-34dc697ca0c1",
  "isSidechain": true,
  "agentId": "afe027cf2c088322c",
  "requestId": "req_011CbWK5SRm9HLAWwbYJdR9k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc1ed52f-91a6-4a92-9306-dafa67288d87",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RbEUvn5hrg2djRxp3RLQb2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 661,
      "cache_creation_input_tokens": 1649,
      "cache_read_input_tokens": 12581,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1649
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 661,
          "output_tokens": 97,
          "cache_read_input_tokens": 12581,
          "cache_creation_input_tokens": 1649,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1649,
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

_source line 21 · 2026-05-29T05:32:02.685Z_

<details><summary>↩ Tool result · `toolu_017XwQVwLd7jf4z7yBfd1CML`</summary>

```text
Web search results for query: ""reasoning robustness" "transfer reward" RLVR consistency Maj@64 Qwen training efficiency 2026"

Links: [{"title":"Beyond Correctness: Learning Robust Reasoning via Transfer","url":"https://www.arxiv.org/pdf/2602.08489"},{"title":"Beyond Correctness: Learning Robust Reasoning via Transfer","url":"https://arxiv.org/html/2602.08489"},{"title":"[2602.08489] Beyond Correctness: Learning Robust Reasoning via Transfer","url":"https://arxiv.org/abs/2602.08489"},{"title":"Efficient Reasoning via Reward Model","url":"https://arxiv.org/pdf/2511.09158"},{"title":"JudgeRLVR: Judge First, Generate Second for Efficient Reasoning","url":"https://arxiv.org/pdf/2601.08468"},{"title":"Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs","url":"https://arxiv.org/html/2506.14245v2"}]

I found relevant research! The search results include a 2026 paper titled "Beyond Correctness: Learning Robust Reasoning via Transfer" that directly addresses your query terms.

## Key Findings

The paper introduces Reinforcement Learning with Transferable Reward (RLTR), which operationalizes robustness via transfer reward that tests whether a partial reasoning prefix from one model can guide a separate model to the correct answer.

### Consistency and Maj@64 Performance

RLVR shows a clear drop in transferability at later training stages even when average accuracy remains stable, and this drop coincides with a degradation in Maj@64, suggesting that RLVR can become less consistent over training. In contrast, RLTR improves transferability together with Maj@64, implying that the transfer-based reward promotes reasoning traces that are both reusable under cross-model continuation and more reliably reproducible.

### Training Efficiency with Qwen

On MATH500, RLTR achieves a +3.6%p gain in Maj@64 compared to RLVR and matches RLVR's average accuracy with roughly 2.5x fewer training steps. When varying receiver models including Qwen-3B, Qwen-3B yields the best Maj@64 results (84.2), and a higher-capacity receiver can provide a more informative transfer signal that improves high-k consistency under majority voting.

The paper was published in February 2026 and addresses all the key concepts in your query: reasoning robustness, transfer reward, RLVR consistency, Maj@64 performance, Qwen models, and training efficiency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc1ed52f-91a6-4a92-9306-dafa67288d87",
  "isSidechain": true,
  "promptId": "76f1366f-40a2-4dae-a639-d8c8a80dcb55",
  "agentId": "afe027cf2c088322c",
  "type": "user",
  "uuid": "66c52ce1-f5f6-4ee4-96c6-52bd1538aad0",
  "sourceToolAssistantUUID": "bc1ed52f-91a6-4a92-9306-dafa67288d87",
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

_source line 22 · 2026-05-29T05:32:51.114Z_

I now have comprehensive information from all sources. Here is the detailed summary.

---

## Summary: "Beyond Correctness: Learning Robust Reasoning via Transfer (RLTR)" — Lee et al., arXiv 2602.08489 (Feb 2026)

**Authors:** Hyunseok Lee, Soheil Abbasloo, Jihoon Tack, Jinwoo Shin

### Problem / Gap Identified

The paper targets a specific failure mode of RLVR (Reinforcement Learning with Verifiable Rewards): while RLVR improves single-sample accuracy on math reasoning tasks, it optimizes solely for final-answer correctness and ignores the quality and robustness of the intermediate reasoning process. Their key empirical observation is that RLVR actually *degrades* multi-sample consistency. On MATH-500, the base Qwen2.5-7B-Instruct model achieves 81.2% Maj@16, but after RLVR training this drops to 80.2%. Similarly, transferability of reasoning traces declines at later RLVR training stages even as average accuracy plateaus. This means RLVR produces brittle reasoning — correct answers arrived at via fragile chains that do not generalize or remain stable across stochastic sampling.

### Key Insight: Transfer Reward

The central philosophical claim is that "robust reasoning should remain useful beyond the mind that produced it." They operationalize this through *reasoning transferability*: if a reasoning trace is genuinely robust, then a partial prefix of that trace should be completable by a different, independent model to reach the correct answer. If a reasoning prefix only "works" for the specific model that generated it (relying on idiosyncratic shortcuts or unstable intermediate steps), a separate receiver model will fail to complete it correctly. This creates a natural test of reasoning quality that goes beyond answer correctness.

### Technical Method: How Transfer Reward Works

The RLTR framework adds a transfer reward on top of the standard RLVR answer-correctness reward:

1. **Generator model** (being trained, e.g., Qwen2.5-7B-Instruct) produces a full reasoning trace `y_gen` for problem `x`.
2. **Truncation**: The trace is truncated at a randomly sampled ratio `τ ~ Uniform(0.3, 0.9)`, yielding prefix `y_gen[:ℓ]` where `ℓ = floor(τ * |y_gen|)`.
3. **Receiver model** (frozen, separate, e.g., Qwen2.5-3B-Instruct) attempts to complete the truncated prefix: `y_rcv ~ M_rcv(·|x, y_gen[:ℓ])`.
4. **Transfer reward**: `R_trans = 1` if the receiver's completion reaches the correct answer, `0` otherwise.
5. **Combined reward**: `R_RLTR = R_RLVR + t * R_trans`, with hyperparameters `a=0.1` (answer weight) and `t=1.0` (transfer weight).

The random truncation ratio prevents overfitting to a fixed boundary. The receiver model is kept frozen throughout training. Training uses GRPO (Group Relative Policy Optimization) on a 3K subset of MATH (difficulty >= 3).

The computational overhead is approximately 7% per training step due to receiver inference, but total FLOPs to reach comparable performance are reduced by ~57% due to the 2.5x fewer steps needed.

### Training Efficiency Claim

RLTR matches RLVR's average accuracy on MATH-500 with roughly **2.5x fewer training steps**. Specifically, RLTR reaches 76.8% accuracy in 40 steps, while RLVR requires 100 steps for 76.2%. Despite the per-step overhead from receiver inference, the net compute is substantially lower.

### Quantitative Results

**Moderate-difficulty benchmarks:**
- MATH-500: Acc 77.0% vs 76.2% (RLVR), Maj@64 84.2% vs 82.2% (RLVR) — a **+2.0pp Maj@64 gain**
- GSM8K: Acc 92.0% vs 89.4% (RLVR), Maj@64 94.2% vs 92.9% (RLVR)

**Hard benchmarks (where gains are most pronounced):**
- AIME2024: Acc 14.8% vs 11.6% (RLVR), Maj@64 21.1% vs 18.9% (RLVR)
- AMC23: Acc 53.5% vs 52.8% (RLVR), Maj@64 67.5% vs 61.7% (RLVR) — a **+5.8pp Maj@64 gain**

Notably, RLVR often *decreases* Maj@K relative to the base model (e.g., MATH-500 Maj@64: base 82.6% -> RLVR 82.2%), while RLTR consistently improves it (82.6% -> 84.2%).

The paper also shows generalization to Llama3.1-8B and to GPQA (scientific reasoning), confirming cross-family and cross-domain robustness.

### How They Define/Measure Robustness

RLTR defines robustness through two complementary lenses:

1. **Majority voting consistency (Maj@K)**: Whether the model converges to the correct answer across K independent stochastic samples (K in {4, 16, 64}). Higher Maj@K means more consistent reasoning.
2. **Transferability**: Whether truncated reasoning prefixes enable a separate receiver model to reach correct answers, measured across truncation ratios 0.3-0.9.

They show these metrics correlate: transferability tracks Maj@64 across training dynamics, providing evidence that cross-model transferability captures genuine reasoning robustness.

### Comparison to Invariance-Based Robustness

RLTR's robustness definition differs meaningfully from consistency/invariance-based approaches. Rather than measuring whether the *same* model produces consistent outputs across perturbed inputs (invariance under input transformation), RLTR measures whether reasoning traces are *transferable across models* (invariance under model substitution). Their robustness is about the reasoning trace being a self-contained, interpretable artifact that any competent model can follow — not about the generator's stability under input perturbation. This is a complementary but distinct mechanism: consistency regularization asks "does the same model reason similarly on similar inputs?" while RLTR asks "can a different model follow this reasoning?" Both encourage stable, non-degenerate reasoning but through different pressures. RLTR does not explicitly enforce invariance to input paraphrasing, augmentation, or distribution shift — it operates entirely at the level of reasoning trace quality as judged by cross-model completion.

### Key Takeaways for Comparison

- RLTR is the most directly relevant prior work for any project addressing reasoning robustness in RL training
- It uses an *external signal* (receiver model completion) rather than *internal consistency* (same-model agreement across perturbations)
- The Maj@K metric is shared and can serve as a common evaluation axis
- The 2.5x training efficiency gain and the observation that RLVR *degrades* consistency are important baselines to cite
- The two approaches (transfer reward vs. consistency regularization) are potentially complementary and could be combined

Sources:
- [arXiv Abstract](https://arxiv.org/abs/2602.08489)
- [arXiv HTML Full Paper](https://arxiv.org/html/2602.08489)
- [Emergent Mind RLVR Topic](https://www.emergentmind.com/topics/llm-rlvr)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66c52ce1-f5f6-4ee4-96c6-52bd1538aad0",
  "isSidechain": true,
  "agentId": "afe027cf2c088322c",
  "requestId": "req_011CbWK6GBtdqKFdD5FUbLqy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "152d108f-93ee-4849-a02d-0f2232053b78",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5a7a1069-aaa7-4692-b429-b8501e411ab6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RLb12wuWrtRmW4aWpogNVz",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 14230,
      "output_tokens": 1888,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1432
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1888,
          "cache_read_input_tokens": 14230,
          "cache_creation_input_tokens": 1432,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1432,
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
