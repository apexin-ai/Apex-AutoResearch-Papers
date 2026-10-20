# Research conversation: Search for and read PathFinder-PRM (arXiv 2505.19706, May 2025) — "Error Typing for Smarter Rewards: Improving Process R

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a91780e1d5a06a47f.jsonl`
- **Structured JSON:** [`a7a0ecc1d37880caa3be.json`](../../sessions/a7/a7a0ecc1d37880caa3be.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

39 recorded events

### User

_source line 1 · 2026-05-27T22:23:42.202Z_

Search for and read PathFinder-PRM (arXiv 2505.19706, May 2025) — "Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision". 

I need to understand:
1. Exactly how do they define and use their {math, consistency} error types?
2. What is their training mechanism — how are typed labels converted into training signals? Dual heads? Auxiliary loss? Embedding-based?
3. What were their actual gains broken down: +2.2 on PRMBench and +1.5 on prm@8 — were these over strong baselines?
4. Did they report inter-annotator agreement for their error types?
5. What were their ablation results — how much did each error type contribute?
6. Any limitations they discussed about extending to more categories?

This is important because a reviewer says our multimodal extension is incremental over PathFinder-PRM. I need to understand exactly what they did to differentiate convincingly.

Use WebSearch and WebFetch. Report detailed technical findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "11c0ed01-00cd-4aa6-94b3-6d386d5b1cba",
  "agentId": "a91780e1d5a06a47f",
  "type": "user",
  "uuid": "10ddd384-a59a-4341-a96f-6020a59de2cb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-27T22:23:42.206Z_

```json
{
  "parentUuid": "10ddd384-a59a-4341-a96f-6020a59de2cb",
  "isSidechain": true,
  "agentId": "a91780e1d5a06a47f",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": []
  },
  "type": "attachment",
  "uuid": "2a864cc7-d1e2-46fc-b4fb-718e5ddacef7",
  "timestamp": "2026-05-27T22:23:42.206Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-27T22:23:42.207Z_

```json
{
  "parentUuid": "2a864cc7-d1e2-46fc-b4fb-718e5ddacef7",
  "isSidechain": true,
  "agentId": "a91780e1d5a06a47f",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "0e327d18-c7bd-4b89-a4b7-e685cacedb09",
  "timestamp": "2026-05-27T22:23:42.207Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-27T22:23:44.408Z_



I'll search for this paper and gather detailed technical information. Let me start by loading the necessary tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e327d18-c7bd-4b89-a4b7-e685cacedb09",
  "isSidechain": true,
  "agentId": "a91780e1d5a06a47f",
  "requestId": "req_011CbTrcrNtEfF6PiDFHFrVn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aae4e730-85b9-4f8a-854a-d533ac0d1ff4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018gzFrBga1A5HaXVSxncosE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1560,
      "cache_read_input_tokens": 7411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1560,
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

_source line 5 · 2026-05-27T22:23:44.820Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0142iM8vLbNvJzRjHMCbA4Sh`</summary>

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
  "parentUuid": "aae4e730-85b9-4f8a-854a-d533ac0d1ff4",
  "isSidechain": true,
  "agentId": "a91780e1d5a06a47f",
  "requestId": "req_011CbTrcrNtEfF6PiDFHFrVn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc160b59-1127-44e8-923c-a35caf0d29e0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018gzFrBga1A5HaXVSxncosE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1560,
      "cache_read_input_tokens": 7411,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1560
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 102,
          "cache_read_input_tokens": 7411,
          "cache_creation_input_tokens": 1560,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1560,
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

_source line 6 · 2026-05-27T22:23:44.822Z_

<details><summary>↩ Tool result · `toolu_0142iM8vLbNvJzRjHMCbA4Sh`</summary>

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
  "parentUuid": "dc160b59-1127-44e8-923c-a35caf0d29e0",
  "isSidechain": true,
  "promptId": "11c0ed01-00cd-4aa6-94b3-6d386d5b1cba",
  "agentId": "a91780e1d5a06a47f",
  "type": "user",
  "uuid": "8fb94999-e659-4aaf-aec2-8fdb3f46ccfe",
  "sourceToolAssistantUUID": "dc160b59-1127-44e8-923c-a35caf0d29e0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-27T22:23:47.121Z_



Now let me search for the paper and fetch it from arXiv simultaneously.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fb94999-e659-4aaf-aec2-8fdb3f46ccfe",
  "isSidechain": true,
  "agentId": "a91780e1d5a06a47f",
  "requestId": "req_011CbTrd3oio3kZ1JEK1XJHC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb0c6ee3-4af5-4407-a562-561d22ea2ace",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QHkUMKhN5jXeoSSHjpw9by",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 8971,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1124,
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

_source line 8 · 2026-05-27T22:23:48.111Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Lzo6rJrHWhwZfG5jM6gfdU`</summary>

```json
{
  "query": "PathFinder-PRM arXiv 2505.19706 \"Error Typing for Smarter Rewards\" process reward model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb0c6ee3-4af5-4407-a562-561d22ea2ace",
  "isSidechain": true,
  "agentId": "a91780e1d5a06a47f",
  "requestId": "req_011CbTrd3oio3kZ1JEK1XJHC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bbba4327-b8cd-4845-97cd-15ad3b055341",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QHkUMKhN5jXeoSSHjpw9by",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 8971,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1124,
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

_source line 9 · 2026-05-27T22:23:48.583Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0194uiQe59sWsba83aQ9mD8S`</summary>

```json
{
  "query": "PathFinder-PRM error-aware hierarchical supervision process reward model math consistency error types 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbba4327-b8cd-4845-97cd-15ad3b055341",
  "isSidechain": true,
  "agentId": "a91780e1d5a06a47f",
  "requestId": "req_011CbTrd3oio3kZ1JEK1XJHC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9190ab00-7cfe-4dd0-9f08-9cf78d5f13ee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QHkUMKhN5jXeoSSHjpw9by",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 8971,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1124,
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

_source line 10 · 2026-05-27T22:23:49.798Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AhQZvoMfsFJNGLr3EhEJpv`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.19706",
  "prompt": "Extract the full abstract, author list, and any detailed information about the paper's methodology, error types, training mechanism, results, ablations, and limitations. Get every technical detail available on this page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9190ab00-7cfe-4dd0-9f08-9cf78d5f13ee",
  "isSidechain": true,
  "agentId": "a91780e1d5a06a47f",
  "requestId": "req_011CbTrd3oio3kZ1JEK1XJHC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4767d510-76b1-4182-9361-3e58aef9c425",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QHkUMKhN5jXeoSSHjpw9by",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 8971,
      "output_tokens": 260,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1124
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 260,
          "cache_read_input_tokens": 8971,
          "cache_creation_input_tokens": 1124,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1124,
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

_source line 11 · 2026-05-27T22:23:55.955Z_

<details><summary>↩ Tool result · `toolu_0194uiQe59sWsba83aQ9mD8S`</summary>

```text
Web search results for query: "PathFinder-PRM error-aware hierarchical supervision process reward model math consistency error types 2025"

Links: [{"title":"[2505.19706] Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision","url":"https://arxiv.org/abs/2505.19706"},{"title":"Process-Supervised Reward Model","url":"https://www.emergentmind.com/topics/process-supervised-reward-model-prm"},{"title":"GitHub - declare-lab/PathFinder-PRM: This repository contains the official implementation of Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision.","url":"https://github.com/declare-lab/PathFinder-PRM"},{"title":"Improving Process Reward Models with Error-Aware ...","url":"https://arxiv.org/pdf/2505.19706"},{"title":"Process-supervised Reward Models (PRMs)","url":"https://www.emergentmind.com/topics/process-supervised-reward-models-prm"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/html/2510.08049v3"},{"title":"GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub","url":"https://github.com/RyanLiu112/Awesome-Process-Reward-Models"},{"title":"Process Reward Models: Step-Level Feedback for LLMs","url":"https://www.emergentmind.com/topics/process-reward-models-prm"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process","url":"https://arxiv.org/pdf/2510.08049"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Process+Reward+Models+%28PRMs%29"}]

Based on the search results, here's comprehensive information about PathFinder-PRM:

## Overview

PathFinder-PRM is a novel hierarchical, error-aware discriminative Process Reward Model (PRM) that first classifies math and consistency errors at each step, then combines these fine-grained signals to estimate step correctness.

## Error Types

The model uses three-dimensional step-level error labels: Math, Consistency, and Optimality. The model first classifies step-level errors into Math and Consistency categories, followed by estimating step Optimality.

## Training and Data

To train PathFinder-PRM, a 400K-sample dataset was constructed by enriching the human-annotated PRM800K corpus and RLHFlow Mistral traces with three-dimensional step-level labels.

## Performance Results

On PRMBench, PathFinder-PRM achieves a state-of-the-art PRMScore of 67.7, outperforming the prior best (65.5) while using 3 times less data. When applied to reward guided greedy search, the model yields prm@8 48.3, a +1.5 point gain over the strongest baseline.

## Key Benefits

The results highlight the value of decoupling feedback prediction into discrete reasoning components. The hierarchical model explicitly decomposes errors into math and consistency dimensions before reward assignment, increasing interpretability and data efficiency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9190ab00-7cfe-4dd0-9f08-9cf78d5f13ee",
  "isSidechain": true,
  "promptId": "11c0ed01-00cd-4aa6-94b3-6d386d5b1cba",
  "agentId": "a91780e1d5a06a47f",
  "type": "user",
  "uuid": "c4d2f5f3-b6da-435f-a5e9-d961d48acd89",
  "sourceToolAssistantUUID": "9190ab00-7cfe-4dd0-9f08-9cf78d5f13ee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-27T22:23:57.941Z_

<details><summary>↩ Tool result · `toolu_01AhQZvoMfsFJNGLr3EhEJpv`</summary>

```text
# PathFinder-PRM Paper Analysis

## Full Abstract
"Large Language Models (LLMs) are prone to hallucination, especially during multi-hop and reasoning-intensive tasks such as mathematical problem solving. While Outcome Reward Models verify only final answers, Process Reward Models (PRMs) score each intermediate step to steer generation toward coherent solutions. We introduce PathFinder-PRM, a novel hierarchical, error-aware discriminative PRM that first classifies math and consistency errors at each step, then combines these fine-grained signals to estimate step correctness. To train PathFinder-PRM, we construct a 400K-sample dataset by enriching the human-annotated PRM800K corpus and RLHFlow Mistral traces with three-dimensional step-level labels. On PRMBench, PathFinder-PRM achieves a new state-of-the-art PRMScore of 67.7, outperforming the prior best (65.5) while using 3 times less data. When applied to reward guided greedy search, our model yields prm@8 48.3, a +1.5 point gain over the strongest baseline. These results demonstrate that decoupled error detection and reward estimation not only boost fine-grained error detection but also substantially improve end-to-end, reward-guided mathematical reasoning with greater data efficiency."

## Author List
- Tej Deep Pala
- Panshul Sharma
- Amir Zadeh
- Chuan Li
- Soujanya Poria

## Key Technical Details

**Core Innovation:** The model employs a hierarchical approach that "first classifies math and consistency errors at each step, then combines these fine-grained signals to estimate step correctness."

**Error Types:** Two-dimensional error classification system:
- Mathematical errors
- Consistency errors

**Training Data:** 400K-sample dataset created by enriching two existing corpora with step-level annotations

**Results:**
- PRMScore: 67.7 (vs. prior 65.5)
- Data efficiency: 3× less data required
- End-to-end performance: prm@8 score of 48.3 (+1.5 improvement)

**Submission Date:** May 26, 2025

**License:** CC-BY-SA 4.0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4767d510-76b1-4182-9361-3e58aef9c425",
  "isSidechain": true,
  "promptId": "11c0ed01-00cd-4aa6-94b3-6d386d5b1cba",
  "agentId": "a91780e1d5a06a47f",
  "type": "user",
  "uuid": "45eec1bb-3eed-46f1-a16d-1abd95e6271f",
  "sourceToolAssistantUUID": "4767d510-76b1-4182-9361-3e58aef9c425",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-27T22:23:59.270Z_

<details><summary>↩ Tool result · `toolu_01Lzo6rJrHWhwZfG5jM6gfdU`</summary>

```text
Web search results for query: "PathFinder-PRM arXiv 2505.19706 "Error Typing for Smarter Rewards" process reward model"

Links: [{"title":"[2505.19706] Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision","url":"https://arxiv.org/abs/2505.19706"},{"title":"declare-lab/PathFinder-PRM-7B · Hugging Face","url":"https://huggingface.co/declare-lab/PathFinder-PRM-7B"},{"title":"arXiv:2505.19706v1 [cs.CL] 26 May 2025","url":"https://arxiv.org/pdf/2505.19706"},{"title":"GitHub - declare-lab/PathFinder-PRM: This repository contains the official implementation of Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision.","url":"https://github.com/declare-lab/PathFinder-PRM"},{"title":"GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub","url":"https://github.com/RyanLiu112/Awesome-Process-Reward-Models"},{"title":"Self-supervised Process Reward Model (SPRM)","url":"https://www.emergentmind.com/topics/self-supervised-process-reward-model-sprm-125c6af6-1a1e-478a-bd22-9e34fc4f589d"},{"title":"Process-Supervised Reward Model","url":"https://www.emergentmind.com/topics/process-supervised-reward-model-prm"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process","url":"https://arxiv.org/pdf/2510.08049"}]

Based on the search results, here's what I found about PathFinder-PRM (arXiv 2505.19706):

## Overview

PathFinder-PRM is a novel hierarchical, error-aware discriminative PRM that first classifies math and consistency errors at each step, then combines these fine-grained signals to estimate step correctness.

## Problem It Addresses

Large Language Models (LLMs) are prone to hallucination, especially during multi-hop and reasoning-intensive tasks such as mathematical problem solving. While Outcome Reward Models verify only final answers, Process Reward Models (PRMs) score each intermediate step to steer generation toward coherent solutions.

## Key Innovation

Instead of treating evaluation as a single correct-or-wrong decision, PathFinder-PRM-7B breaks down its error judgment into 2 parts: whether the reasoning is mathematically correct, and logically consistent. It predicts these aspects separately and then combines them to decide if the current reasoning steps leads to a correct final solution.

## Training Data and Performance

The authors constructed a 400K-sample dataset by enriching the human-annotated PRM800K corpus and RLHFlow Mistral traces with three-dimensional step-level labels. On PRMBench, PathFinder-PRM achieves a new state-of-the-art PRMScore of 67.7, outperforming the prior best (65.5) while using 3 times less data. When applied to reward guided greedy search, the model yields prm@8 48.3, a +1.5 point gain over the strongest baseline.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbba4327-b8cd-4845-97cd-15ad3b055341",
  "isSidechain": true,
  "promptId": "11c0ed01-00cd-4aa6-94b3-6d386d5b1cba",
  "agentId": "a91780e1d5a06a47f",
  "type": "user",
  "uuid": "f4478a89-ee8a-4870-934d-70389d4ccbf2",
  "sourceToolAssistantUUID": "bbba4327-b8cd-4845-97cd-15ad3b055341",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-27T22:24:02.584Z_

Good, I have the overview. Now let me fetch the full paper PDF and the GitHub repository for detailed technical information about the training mechanism, ablations, and error type definitions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4478a89-ee8a-4870-934d-70389d4ccbf2",
  "isSidechain": true,
  "agentId": "a91780e1d5a06a47f",
  "requestId": "req_011CbTre7RHbuU4YnW3ePpH7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "caf572a9-3e80-41c1-a836-3d360163e72c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PkV375smys8KiYm4SnT1Zf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1406,
      "cache_creation_input_tokens": 1134,
      "cache_read_input_tokens": 10095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1134,
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

_source line 15 · 2026-05-27T22:24:08.701Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Li4nxxpzzE56ibyjruR8p6`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2505.19706",
  "prompt": "Extract ALL technical details from this paper. I need:\n\n1. EXACT definitions of math errors and consistency errors - how are they formally defined? What constitutes each type? Any taxonomy or subcategories?\n\n2. TRAINING MECHANISM - How are the typed error labels converted into training signals? Do they use dual classification heads? Auxiliary losses? What is the loss function? How does the hierarchical architecture work exactly? What is the model architecture - is it embedding-based, head-based?\n\n3. FULL RESULTS TABLES - All numbers from PRMBench and prm@8 evaluations. What were the baselines? What were the exact baseline scores?\n\n4. INTER-ANNOTATOR AGREEMENT - Did they measure agreement for their error type annotations? Any kappa scores or agreement rates?\n\n5. ABLATION RESULTS - How much did each error type (math vs consistency) contribute individually? What ablations did they run?\n\n6. LIMITATIONS - What do they say about extending to more error categories? Any discussed limitations?\n\n7. Dataset construction details - how were the 400K samples labeled?\n\nExtract every detail, equation, table, and number you can find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "caf572a9-3e80-41c1-a836-3d360163e72c",
  "isSidechain": true,
  "agentId": "a91780e1d5a06a47f",
  "requestId": "req_011CbTre7RHbuU4YnW3ePpH7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d1db9f2c-9be5-4bb8-a657-fa097bd26389",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PkV375smys8KiYm4SnT1Zf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1406,
      "cache_creation_input_tokens": 1134,
      "cache_read_input_tokens": 10095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1134,
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

_source line 16 · 2026-05-27T22:24:10.296Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FToyvAaaSeZPPrJ7cV8Z2d`</summary>

```json
{
  "url": "https://github.com/declare-lab/PathFinder-PRM",
  "prompt": "Extract all technical details about the PathFinder-PRM implementation. What is the model architecture? How are the error type heads implemented? What loss functions are used? What training configuration? How is the hierarchical prediction done? Any details about the dual heads or multi-task training setup."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1db9f2c-9be5-4bb8-a657-fa097bd26389",
  "isSidechain": true,
  "agentId": "a91780e1d5a06a47f",
  "requestId": "req_011CbTre7RHbuU4YnW3ePpH7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "65747ece-5a63-4774-b38b-3006680fc4e6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PkV375smys8KiYm4SnT1Zf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1406,
      "cache_creation_input_tokens": 1134,
      "cache_read_input_tokens": 10095,
      "output_tokens": 498,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1134
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1406,
          "output_tokens": 498,
          "cache_read_input_tokens": 10095,
          "cache_creation_input_tokens": 1134,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1134,
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

_source line 17 · 2026-05-27T22:24:16.052Z_

<details><summary>↩ Tool result · `toolu_01Li4nxxpzzE56ibyjruR8p6`</summary>

```text
# Technical Details Extraction - Error Typing for Process Reward Models

## 1. ERROR TYPE DEFINITIONS

The paper defines two primary error categories:

**Math Errors**: Computational or logical mistakes in mathematical reasoning steps where the solution approach is sound but execution fails.

**Consistency Errors**: Violations of logical coherence where the reasoning contradicts previously established facts or assumptions within the solution.

The document references these as components of hierarchical supervision but the extracted PDF content doesn't contain the complete formal taxonomy with subcategories.

## 2. TRAINING MECHANISM

The paper employs a hierarchical architecture with:

- **Dual-head structure**: Separate classification heads for error typing and overall step quality
- **Loss function approach**: Combines auxiliary loss for error type classification with primary reward modeling loss
- **Architecture details**: Uses embedding-based representations with hierarchical supervision signals

Specific loss function equations and exact architectural specifications are not clearly rendered in the accessible portions of the PDF.

## 3. RESULTS TABLES

The document references evaluation on **PRMBench** and **prm@8** benchmarks. Key performance metrics are mentioned but specific numerical tables with baseline comparisons are embedded in compressed PDF streams that don't extract cleanly. The paper reports results across 14 pages of content with multiple benchmark evaluations.

## 4. INTER-ANNOTATOR AGREEMENT

The extracted content does not contain explicit inter-annotator agreement metrics (kappa scores or agreement percentages) for the error type annotations in the accessible sections.

## 5. ABLATION RESULTS

The paper structure indicates ablation studies examining individual contributions of math vs. consistency error signals, but specific ablation numbers aren't clearly extracted from the PDF content.

## 6. LIMITATIONS

The document acknowledges extending to additional error categories beyond the two main types, though comprehensive limitation discussion requires accessing the full appendices (A-E referenced in the document).

## 7. DATASET CONSTRUCTION

Reference to "400K samples" or labeling procedures isn't explicitly visible in the extracted content. The paper has substantial appendix material covering data annotation protocols.

**Note**: This PDF extraction is incomplete due to compression. For complete technical specifications, direct PDF viewing is necessary.

[Binary content (application/pdf, 1MB) also saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/b0104aa9-f62f-48d7-93dc-722aa4bbc136/tool-results/webfetch-1779920648718-genlgp.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1db9f2c-9be5-4bb8-a657-fa097bd26389",
  "isSidechain": true,
  "promptId": "11c0ed01-00cd-4aa6-94b3-6d386d5b1cba",
  "agentId": "a91780e1d5a06a47f",
  "type": "user",
  "uuid": "9df52439-42f1-4539-997f-f51a2908a549",
  "sourceToolAssistantUUID": "d1db9f2c-9be5-4bb8-a657-fa097bd26389",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-27T22:24:16.926Z_

<details><summary>↩ Tool result · `toolu_01FToyvAaaSeZPPrJ7cV8Z2d`</summary>

```text
# PathFinder-PRM Technical Details

Based on the provided GitHub repository content, I cannot extract the specific technical implementation details you requested.

## What's Available

The repository page contains:
- **High-level overview**: "PathFinder-PRM, a novel hierarchical, error‑aware discriminative PRM that first classifies math and consistency errors at each step"
- **Dataset information**: 400K samples with three-dimensional step-level labels (Math, Consistency, Optimality)
- **Performance metrics**: PRMScore of 67.7 on PRMBench
- **Project structure**: References to Dataset Generation, PRM Training, and PRM Evaluation modules

## What's Missing

The page itself does not provide:
- Model architecture specifics
- Implementation details for error type heads
- Loss function definitions
- Training hyperparameters
- Hierarchical prediction mechanism details
- Multi-task training configuration

## Where to Find Details

The repository README directs readers to separate documentation files:
- `src/data_generation/README.md`
- `src/training/README.md`
- `src/evaluation/README.md`

Additionally, the full technical specification would likely be in the associated paper (arXiv:2505.19706), which isn't included in the provided content.

To obtain the architectural and implementation details, you would need to access either the individual module documentation or the research paper directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65747ece-5a63-4774-b38b-3006680fc4e6",
  "isSidechain": true,
  "promptId": "11c0ed01-00cd-4aa6-94b3-6d386d5b1cba",
  "agentId": "a91780e1d5a06a47f",
  "type": "user",
  "uuid": "1beacbb5-3000-461a-8df5-3ea8e705ea76",
  "sourceToolAssistantUUID": "65747ece-5a63-4774-b38b-3006680fc4e6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-27T22:24:19.828Z_

The PDF extraction was incomplete. Let me try fetching the HTML version of the paper and also look at the specific source code for implementation details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1beacbb5-3000-461a-8df5-3ea8e705ea76",
  "isSidechain": true,
  "agentId": "a91780e1d5a06a47f",
  "requestId": "req_011CbTrfQrZ1FDupVo8CtmuH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "276862fc-d11e-4b8e-a9ea-73ae6280bf47",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UsKVv9mXGAaGyuddXnVPoN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2842,
      "cache_read_input_tokens": 11229,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2842,
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

_source line 20 · 2026-05-27T22:24:25.062Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SyJzemDhT6dFn75MDeYd31`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.19706",
  "prompt": "Extract ALL technical details from this paper. I need EVERYTHING:\n\n1. EXACT definitions of math errors vs consistency errors - formal definitions, subcategories, examples\n2. The COMPLETE training mechanism - loss functions (exact equations), architecture (dual heads vs single head), how error type predictions feed into reward estimation, hierarchical structure\n3. ALL results tables with ALL baseline numbers - PRMBench scores, prm@8 scores, every baseline model and its score\n4. Inter-annotator agreement metrics if any\n5. ALL ablation results - contribution of each error type, each component\n6. Limitations section - what do they say about extending to more categories\n7. Dataset construction - how were labels generated, what LLM was used for annotation, annotation pipeline details\n8. The three-dimensional labels: math, consistency, and optimality - how is optimality defined?\n9. Any equations for the loss function or training objective\n\nGet every number, every table, every equation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "276862fc-d11e-4b8e-a9ea-73ae6280bf47",
  "isSidechain": true,
  "agentId": "a91780e1d5a06a47f",
  "requestId": "req_011CbTrfQrZ1FDupVo8CtmuH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "425a3001-4d90-4e95-b6f4-65c0714910a6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UsKVv9mXGAaGyuddXnVPoN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2842,
      "cache_read_input_tokens": 11229,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2842,
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

_source line 21 · 2026-05-27T22:24:25.072Z_

<details><summary>↩ Tool result · `toolu_01SyJzemDhT6dFn75MDeYd31`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "425a3001-4d90-4e95-b6f4-65c0714910a6",
  "isSidechain": true,
  "promptId": "11c0ed01-00cd-4aa6-94b3-6d386d5b1cba",
  "agentId": "a91780e1d5a06a47f",
  "type": "user",
  "uuid": "000face7-161a-4465-a224-a8d99da557a4",
  "sourceToolAssistantUUID": "425a3001-4d90-4e95-b6f4-65c0714910a6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-27T22:24:26.310Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MBswfVkLgg7KXP1hwP2RWS`</summary>

```json
{
  "url": "https://github.com/declare-lab/PathFinder-PRM/blob/main/src/training/README.md",
  "prompt": "Extract all training details: model architecture, loss functions, how error types are used in training, multi-task learning setup, hyperparameters, how the hierarchical prediction works."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "000face7-161a-4465-a224-a8d99da557a4",
  "isSidechain": true,
  "agentId": "a91780e1d5a06a47f",
  "requestId": "req_011CbTrfQrZ1FDupVo8CtmuH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa1491d0-17b7-4286-bf34-9253cbbf9eea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UsKVv9mXGAaGyuddXnVPoN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2842,
      "cache_read_input_tokens": 11229,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2842,
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

_source line 23 · 2026-05-27T22:24:30.606Z_

<details><summary>↩ Tool result · `toolu_01MBswfVkLgg7KXP1hwP2RWS`</summary>

```text
# PathFinder-PRM Training Details

Based on the provided README, here's what can be extracted:

## Available Information

**Model Architecture:**
The system uses "Qwen/Qwen2.5-7B-Instruct as the base model" with customizations including special tokens `<+>`, `<->`, and `&lt;extra>` integrated into the embedding layer.

**Dataset:**
Training uses "PathFinder-600K," accessible via Hugging Face at `declare-lab/PathFinder-600K`.

**Infrastructure:**
The training employs "DeepSpeed for memory optimization" with a Zero-2 configuration available in `training_configs/deepspeed_zero2.yaml`.

## Information Not Provided

The README does not contain specific details about:
- Loss functions
- How error types are utilized during training
- Multi-task learning architecture
- Specific hyperparameter values
- Hierarchical prediction mechanics

## Recommendation

For comprehensive technical details on loss functions, error-aware supervision, and hierarchical prediction structures, you would need to consult the actual training scripts (`train_prm.sh`, `prepare_model.py`) or the referenced research paper (arXiv:2505.19706), which appears to document the full methodology behind error typing for process reward models.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa1491d0-17b7-4286-bf34-9253cbbf9eea",
  "isSidechain": true,
  "promptId": "11c0ed01-00cd-4aa6-94b3-6d386d5b1cba",
  "agentId": "a91780e1d5a06a47f",
  "type": "user",
  "uuid": "7c0cfffe-d3fa-4458-af6c-4c8dad50f1bb",
  "sourceToolAssistantUUID": "fa1491d0-17b7-4286-bf34-9253cbbf9eea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-27T22:24:33.212Z_

The HTML version doesn't exist. Let me try alternative approaches to get the full paper details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c0cfffe-d3fa-4458-af6c-4c8dad50f1bb",
  "isSidechain": true,
  "agentId": "a91780e1d5a06a47f",
  "requestId": "req_011CbTrgRK7Ypcnb2zS1P3z3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "438db124-76e1-4602-9f37-f6f05ec5bf8a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AdcUP4b4RxA2FxHqPQHgif",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 842,
      "cache_read_input_tokens": 14071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 842,
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

_source line 25 · 2026-05-27T22:24:34.858Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XqcgECHxX9vCwFpUt9uCTr`</summary>

```json
{
  "url": "https://huggingface.co/papers/2505.19706",
  "prompt": "Extract ALL technical details about PathFinder-PRM. I need: error type definitions (math vs consistency), training mechanism (loss functions, architecture, dual heads), all results tables with baseline comparisons, ablation results, inter-annotator agreement, limitations, dataset construction details. Get every number and technical detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "438db124-76e1-4602-9f37-f6f05ec5bf8a",
  "isSidechain": true,
  "agentId": "a91780e1d5a06a47f",
  "requestId": "req_011CbTrgRK7Ypcnb2zS1P3z3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03983810-4846-4176-85f2-bc6661c14456",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AdcUP4b4RxA2FxHqPQHgif",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 842,
      "cache_read_input_tokens": 14071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 842,
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

_source line 26 · 2026-05-27T22:24:35.599Z_

<details><summary>↩ Tool result · `toolu_01XqcgECHxX9vCwFpUt9uCTr`</summary>

```text
&lt;persisted-output>
Output too large (56.1KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/b0104aa9-f62f-48d7-93dc-722aa4bbc136/tool-results/toolu_01XqcgECHxX9vCwFpUt9uCTr.txt

Preview (first 2KB):
# Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision

Tej Deep Pala&lt;sup>1&lt;/sup>, Panshul Sharma&lt;sup>1&lt;/sup>  
Amir Zadeh&lt;sup>2&lt;/sup>, Chuan Li&lt;sup>2&lt;/sup>, Soujanya Poria&lt;sup>1&lt;/sup>

&lt;sup>1&lt;/sup>Singapore University of Technology and Design

&lt;sup>2&lt;/sup>Lambda Labs

## Abstract

Large Language Models (LLMs) are prone to hallucination, especially during multi-hop and reasoning-intensive tasks such as mathematical problem solving. While Outcome Reward Models verify only final answers, Process Reward Models (PRMs) score each intermediate step to steer generation toward coherent solutions. We introduce PathFinder-PRM, a novel hierarchical, error-aware discriminative PRM that first classifies math and consistency errors at each step, then combines these fine-grained signals to estimate step correctness. To train PathFinder-PRM, we construct a 400K-sample dataset by enriching the human-annotated PRM800K corpus and RLHFlow Mistral traces with three-dimensional step-level labels. On PRMBench, PathFinder-PRM achieves a new state-of-the-art PRMScore of 67.7, outperforming the prior best (65.5) while using 3× less data. When applied to reward guided greedy search, our model yields prm@8 48.3, a +1.5 point gain over the strongest baseline. These results demonstrate that decoupled error detection and reward estimation not only boost fine-grained error detection but also substantially improve end-to-end, reward-guided mathematical reasoning with greater data efficiency&lt;sup>1&lt;/sup>.

## 1 Introduction

...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03983810-4846-4176-85f2-bc6661c14456",
  "isSidechain": true,
  "promptId": "11c0ed01-00cd-4aa6-94b3-6d386d5b1cba",
  "agentId": "a91780e1d5a06a47f",
  "type": "user",
  "uuid": "5fe2a7cc-bf37-456e-b496-06b709a5b0dd",
  "sourceToolAssistantUUID": "03983810-4846-4176-85f2-bc6661c14456",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-27T22:24:35.631Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B78csjUwekhrfjaiGiRuok`</summary>

```json
{
  "query": "PathFinder-PRM hierarchical dual head loss function math error consistency error optimality label training architecture ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5fe2a7cc-bf37-456e-b496-06b709a5b0dd",
  "isSidechain": true,
  "agentId": "a91780e1d5a06a47f",
  "requestId": "req_011CbTrgRK7Ypcnb2zS1P3z3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d78d087-5c0b-40fd-93f7-39a93095dabd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AdcUP4b4RxA2FxHqPQHgif",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 842,
      "cache_read_input_tokens": 14071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 842,
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

_source line 28 · 2026-05-27T22:24:36.430Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0118nwv9HMNmdDQ86WjHBmZq`</summary>

```json
{
  "query": "PathFinder-PRM PRMBench 67.7 baseline comparison ReasonEval Math-Shepherd Qwen ablation error type contribution"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d78d087-5c0b-40fd-93f7-39a93095dabd",
  "isSidechain": true,
  "agentId": "a91780e1d5a06a47f",
  "requestId": "req_011CbTrgRK7Ypcnb2zS1P3z3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d0346d27-091d-4a5b-9194-358cd32c76b2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AdcUP4b4RxA2FxHqPQHgif",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 842,
      "cache_read_input_tokens": 14071,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 842
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 292,
          "cache_read_input_tokens": 14071,
          "cache_creation_input_tokens": 842,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 842,
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

_source line 29 · 2026-05-27T22:24:43.397Z_

<details><summary>↩ Tool result · `toolu_0118nwv9HMNmdDQ86WjHBmZq`</summary>

```text
Web search results for query: "PathFinder-PRM PRMBench 67.7 baseline comparison ReasonEval Math-Shepherd Qwen ablation error type contribution"

Links: [{"title":"PRMBench: Benchmark for Process-level Math Reasoning","url":"https://www.emergentmind.com/topics/prmbench"},{"title":"Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision","url":"https://arxiv.org/pdf/2505.19706"},{"title":"R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://arxiv.org/html/2503.21295v1"},{"title":"[Literature Review] R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://www.themoonlight.io/en/review/r-prm-reasoning-driven-process-reward-modeling"},{"title":"Know What You Don’t Know: Uncertainty Calibration of Process Reward Models","url":"https://arxiv.org/html/2506.09338"},{"title":"declare-lab/PathFinder-PRM-7B · Hugging Face","url":"https://huggingface.co/declare-lab/PathFinder-PRM-7B"},{"title":"GitHub - LightChen233/Awesome-Long-Chain-of-Thought-Reasoning: Latest Advances on Long Chain-of-Thought Reasoning · GitHub","url":"https://github.com/LightChen233/Awesome-Long-Chain-of-Thought-Reasoning"},{"title":"PRMBENCH: A Fine-grained and Challenging Benchmark ...","url":"https://aclanthology.org/2025.acl-long.1230.pdf"},{"title":"[Literature Review] Socratic-PRMBench: Benchmarking Process Reward Models with Systematic Reasoning Patterns","url":"https://www.themoonlight.io/en/review/socratic-prmbench-benchmarking-process-reward-models-with-systematic-reasoning-patterns"}]

Based on the search results, I found relevant information about PathFinder-PRM, PRMBench, and the baseline comparisons you're asking about:

## PathFinder-PRM Performance

PathFinder-PRM achieves a new state-of-the-art PRMScore of 67.7 on PRMBench, outperforming the prior best (65.5) while using 3× less data. PathFinder-PRM's explicit decoupling of error-type detection from reward estimation leads to a PRMScore of 67.7 with three times less data than previous bests.

## Baseline Comparisons

Top open-source PRMs (e.g., ReasonEval-34B, Qwen2.5-Math-PRM-7B) score 60–65. This provides context for the baseline performance that PathFinder-PRM improves upon.

## Error Type Contributions

PathFinder-PRM classifies each step to detect the presence of math or consistency errors, and combines these fine-grained error labels to produce a final reward score. Error Type Challenges include simplicity detection which lags with sub-50 scores widely observed, while soundness and sensitivity are better, but domain, confidence, and "trap" errors remain difficult.

The key innovation is that decoupled error detection and reward estimation not only boost fine-grained error detection but also substantially improve end-to-end, reward-guided mathematical reasoning with greater data efficiency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0346d27-091d-4a5b-9194-358cd32c76b2",
  "isSidechain": true,
  "promptId": "11c0ed01-00cd-4aa6-94b3-6d386d5b1cba",
  "agentId": "a91780e1d5a06a47f",
  "type": "user",
  "uuid": "7c22d3bb-5afe-49cd-a158-2bb5e834c47c",
  "sourceToolAssistantUUID": "d0346d27-091d-4a5b-9194-358cd32c76b2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-27T22:25:01.178Z_

<details><summary>↩ Tool result · `toolu_01B78csjUwekhrfjaiGiRuok`</summary>

```text
Web search results for query: "PathFinder-PRM hierarchical dual head loss function math error consistency error optimality label training architecture ablation"

Links: [{"title":"Hierarchical Dual-Head Model for Suicide Risk Assessment via MentalRoBERTa","url":"https://arxiv.org/pdf/2510.20085"},{"title":"PRM-D* Method for Mobile Robot Path Planning","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10098883/"},{"title":"PRM path smoothening by circular arc fillet method for mobile robot   navigation","url":"https://arxiv.org/pdf/2112.03604"},{"title":"LightDPH: Lightweight Dual-Projection-Head Hierarchical Contrastive Learning for Skin Lesion Classification | Journal of Healthcare Informatics Research | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s41666-024-00174-5"},{"title":"Pathfinder: A parallel quasi-Newton algorithm for reaching regions of high probability mass | Statistical Modeling, Causal Inference, and Social Science","url":"https://statmodeling.stat.columbia.edu/2021/08/10/pathfinder-a-parallel-quasi-newton-algorithm-for-reaching-regions-of-high-probability-mass/"}]

The initial search returned results related to different topics (suicide risk assessment, robot path planning, and Pathfinder MCMC). Let me search more specifically for the PathFinder-PRM model you mentioned.

Links: [{"title":"GitHub - declare-lab/PathFinder-PRM: This repository contains the official implementation of Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision.","url":"https://github.com/declare-lab/PathFinder-PRM"},{"title":"Improving Process Reward Models with Error-Aware ...","url":"https://arxiv.org/pdf/2505.19706"},{"title":"Process-supervised Reward Models (PRMs)","url":"https://www.emergentmind.com/topics/process-supervised-reward-models-prm"},{"title":"Process Reward Models: Step-Level Feedback for LLMs","url":"https://www.emergentmind.com/topics/process-reward-models-prm"},{"title":"Pathfinder: open source software for analyzing spatial navigation search strategies","url":"https://www.biorxiv.org/content/10.1101/715961.full.pdf"},{"title":"Error Estimation of Pathfinder Version 5.3 Level-3C SST ...","url":"https://www.mdpi.com/2072-4292/12/4/590"},{"title":"PRM path smoothening by circular arc fillet method for mobile robot   navigation","url":"https://arxiv.org/pdf/2112.03604"},{"title":"Accelerating Neuron Reconstruction with PATHFINDER","url":"https://www.biorxiv.org/content/10.1101/2025.05.16.654254.full.pdf"}]

Great! I found relevant information about PathFinder-PRM. Let me search for more specific details about the architecture and ablation studies.

Links: [{"title":"Running an Ablation Study — pykeen 1.11.2-dev documentation","url":"https://pykeen.readthedocs.io/en/latest/tutorial/running_ablation.html"},{"title":"Training strategy over architecture: A systematic ablation study for Spartina detection from aerial imagery with small geospatial datasets","url":"https://archimer.ifremer.fr/doc/01014/112588/"},{"title":"Evaluation of a Minimally Invasive Image-Guided Surgery System for Hepatic Ablation Procedures","url":"https://clinicaltrials.gov/study/NCT01238666"},{"title":"FreePRM: Training Process Reward Models Without Ground Truth Process Labels","url":"https://arxiv.org/pdf/2506.03570"},{"title":"Efficient PRM Training Data Synthesis via Formal Verification","url":"https://arxiv.org/pdf/2505.15960"},{"title":"Ablation Studies: The Operating System for Trustworthy AI Decisions | by Adnan Masood, PhD. | Medium","url":"https://medium.com/@adnanmasood/ablation-studies-the-operating-system-for-trustworthy-ai-decisions-b99300d3bd32"},{"title":"Feasibility of a Minimally Invasive Image-Guided Surgery System for Hepatic Procedures","url":"https://clinicaltrials.gov/study/NCT01286428"}]

Let me search more specifically for the PathFinder-PRM paper with the exact details you're asking about.

Links: [{"title":"HAL Id: hal-05448955 https://hal.science/hal-05448955v1","url":"https://hal.science/hal-05448955v1/document"},{"title":"GitHub - declare-lab/PathFinder-PRM: This repository contains the official implementation of Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision.","url":"https://github.com/declare-lab/PathFinder-PRM"},{"title":"Pathfinder Paper | PDF | Linear Programming | Function (Mathematics)","url":"https://www.scribd.com/document/705283253/Pathfinder-paper"},{"title":"Pathfinder: open source software for analyzing spatial navigation search strategies","url":"https://www.biorxiv.org/content/10.1101/715961.full.pdf"},{"title":"declare-lab/PathFinder-PRM-7B · Hugging Face","url":"https://huggingface.co/declare-lab/PathFinder-PRM-7B"},{"title":"PRM path smoothening by circular arc fillet method for mobile robot   navigation","url":"https://arxiv.org/pdf/2112.03604"},{"title":"Accelerating Neuron Reconstruction with PATHFINDER","url":"https://www.biorxiv.org/content/10.1101/2025.05.16.654254.full.pdf"}]

Perfect! I found detailed information about PathFinder-PRM. Let me search for more specific details about the loss function and ablation studies from the paper.

Links: [{"title":"[2505.19706] Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision","url":"https://arxiv.org/abs/2505.19706"},{"title":"arXiv:2505.19706v1 [cs.CL] 26 May 2025","url":"https://arxiv.org/pdf/2505.19706"},{"title":"PathFinder: Advancing Path Loss Prediction for Single-to-Multi-Transmitter Scenario","url":"https://arxiv.org/pdf/2512.14150"},{"title":"FunReason: Enhancing Large Language Models’ Function Calling via Self-Refinement Multiscale Loss and Automated Data Refinement","url":"https://arxiv.org/html/2505.20192v1"},{"title":"System and method for loss function metalearning for faster, more accurate training, and smaller datasets","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12026624"}]

Based on my web searches, I found comprehensive information about PathFinder-PRM. Here's what I discovered:

## PathFinder-PRM Overview

PathFinder-PRM is a novel hierarchical, error-aware discriminative PRM that first classifies math and consistency errors at each step, then combines these fine-grained signals to estimate step correctness.

## Architecture and Design

A single language modeling head is used without any task-specific heads. During the first forward pass, the input is constructed as: [PRM Input], Math: &lt;mask>, Consistency: &lt;mask>, where the two special &lt;mask> tokens represent the target positions for Math and Consistency labels.

The motivation behind this design is to minimize error cascading between dependent predictions. Specifically, the aim is to predict Math and Consistency labels independently in the first forward pass to prevent the Consistency prediction from being influenced by the previously generated Math label.

## Training Labels

The correctness label of each step is mapped to a three-dimensional vector. Each component of the vector is either zero or one. The first component is the accuracy of the mathematical reasoning, the second is consistency, and the third is correctness, which includes the lack of redundancy.

## Training Data and Performance

A 400K-sample dataset was constructed by enriching the human-annotated PRM800K corpus and RLHFlow Mistral traces with three-dimensional step-level labels.

On PRMBench, PathFinder-PRM achieves a state-of-the-art PRMScore of 67.7, outperforming the prior best (65.5) while using 3 times less data. When applied to reward guided greedy search, the model yields prm@8 48.3, a +1.5 point gain over the strongest baseline.

While I found information about the model's architecture and training approach, the search results don't contain specific details about the complete loss function mathematical formulation or detailed ablation study tables from the paper. For those specific technical details, you may want to refer directly to the full paper on arXiv (2505.19706).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d78d087-5c0b-40fd-93f7-39a93095dabd",
  "isSidechain": true,
  "promptId": "11c0ed01-00cd-4aa6-94b3-6d386d5b1cba",
  "agentId": "a91780e1d5a06a47f",
  "type": "user",
  "uuid": "96823ed0-7821-4cf4-aedd-2b21f186a724",
  "sourceToolAssistantUUID": "6d78d087-5c0b-40fd-93f7-39a93095dabd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-27T22:25:03.974Z_

I got a large output from HuggingFace. Let me read that file and also fetch more details from additional sources.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96823ed0-7821-4cf4-aedd-2b21f186a724",
  "isSidechain": true,
  "agentId": "a91780e1d5a06a47f",
  "requestId": "req_011CbTrig5BLsxrqcSgHLHpq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8966cc96-3b24-47a4-a3b0-4a54659416e5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zmKjnC4VUXZ2moL87s535",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 877,
      "cache_creation_input_tokens": 3134,
      "cache_read_input_tokens": 14913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3134,
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

_source line 32 · 2026-05-27T22:25:04.744Z_

<details open><summary>🔧 Tool call — Read · `toolu_01V3CKr6uRUoaKfsqbKon3y4`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/b0104aa9-f62f-48d7-93dc-722aa4bbc136/tool-results/toolu_01XqcgECHxX9vCwFpUt9uCTr.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8966cc96-3b24-47a4-a3b0-4a54659416e5",
  "isSidechain": true,
  "agentId": "a91780e1d5a06a47f",
  "requestId": "req_011CbTrig5BLsxrqcSgHLHpq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "02ab4ca8-6cbb-428d-86b2-c377726b4b5e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zmKjnC4VUXZ2moL87s535",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 877,
      "cache_creation_input_tokens": 3134,
      "cache_read_input_tokens": 14913,
      "output_tokens": 157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3134
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 877,
          "output_tokens": 157,
          "cache_read_input_tokens": 14913,
          "cache_creation_input_tokens": 3134,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3134,
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

_source line 33 · 2026-05-27T22:25:05.229Z_

<details><summary>↩ Tool result · `toolu_01V3CKr6uRUoaKfsqbKon3y4`</summary>

````text
1	# Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision
2	
3	Tej Deep Pala&lt;sup>1&lt;/sup>, Panshul Sharma&lt;sup>1&lt;/sup>  
4	Amir Zadeh&lt;sup>2&lt;/sup>, Chuan Li&lt;sup>2&lt;/sup>, Soujanya Poria&lt;sup>1&lt;/sup>
5	
6	&lt;sup>1&lt;/sup>Singapore University of Technology and Design
7	
8	&lt;sup>2&lt;/sup>Lambda Labs
9	
10	## Abstract
11	
12	Large Language Models (LLMs) are prone to hallucination, especially during multi-hop and reasoning-intensive tasks such as mathematical problem solving. While Outcome Reward Models verify only final answers, Process Reward Models (PRMs) score each intermediate step to steer generation toward coherent solutions. We introduce PathFinder-PRM, a novel hierarchical, error-aware discriminative PRM that first classifies math and consistency errors at each step, then combines these fine-grained signals to estimate step correctness. To train PathFinder-PRM, we construct a 400K-sample dataset by enriching the human-annotated PRM800K corpus and RLHFlow Mistral traces with three-dimensional step-level labels. On PRMBench, PathFinder-PRM achieves a new state-of-the-art PRMScore of 67.7, outperforming the prior best (65.5) while using 3× less data. When applied to reward guided greedy search, our model yields prm@8 48.3, a +1.5 point gain over the strongest baseline. These results demonstrate that decoupled error detection and reward estimation not only boost fine-grained error detection but also substantially improve end-to-end, reward-guided mathematical reasoning with greater data efficiency&lt;sup>1&lt;/sup>.
13	
14	## 1 Introduction
15	
16	Large language models (LLMs) have achieved remarkable success on many natural language tasks, including open-ended generation and complex reasoning (Brown et al., 2020; Wei et al., 2022). However, they remain prone to *hallucinations* and subtle logical errors when generating multi-step solutions, particularly in domains such as mathematical problem solving (Wang et al., 2023; Zheng et al., 2024). Traditional outcome-only verifiers (Outcome Reward Models) can check a final answer but fail
17	
18	to catch intermediate missteps that lead reasoning astray (Wang et al., 2024b).
19	
20	To address this gap, *Process Reward Models* (PRMs) have been proposed, which assign individual rewards to each reasoning step. (Uesato et al., 2022; Liu et al., 2025). As such, PRMs can filter out erroneous chains of thought and guide generation toward more reliable reasoning trajectories (Lightman et al., 2023; Zhang et al., 2025).
21	
22	Recent interest in explicitly reasoning-centric LLMs such as DeepSeek-R1 and OpenAI’s GPT-o series models underscores the field’s growing emphasis on human-like thinking and the ability to flexibly scale test-time compute (Guo et al., 2025; OpenAI, 2025). These models demonstrate extended deliberation and use structured reasoning traces to solve complex problems. In such settings, effective *process supervision* is crucial: rather than merely verifying a final answer, it must guide and correct the reasoning process at every step, ensuring logical coherence and factual accuracy throughout. PRMs are thus an essential component in aligning reasoning LLMs with reliable multi-step reasoning.
23	
24	Despite recent advances, current PRMs still struggle with fine-grained error types. For example, the PRMBench benchmark reveals that many state-of-the-art PRMs fall short of detecting subtler faults such as non-redundancy violations, domain inconsistencies, or deceptive logical steps (Song et al., 2025). Moreover, existing methods typically combine *error detection* (is this step wrong?) with *path optimality* (how helpful is this step in reaching the solution?) in a single prediction, leaving each signal underutilized (Zhang et al., 2025; Xia et al., 2025).
25	
26	In this work, we argue that error detection and value estimation are complementary but distinct objectives. By decoupling them into two sequential subtasks, first explicitly identifying specific error categories and using those error signals to
27	
28	&lt;sup>1&lt;/sup>Code: &lt;https://github.com/declare-lab/PathFinder-PRM>&lt;table border="1">
29	&lt;thead>
30	&lt;tr>
31	&lt;th>Question:&lt;/th>
32	&lt;th>Existing PRMs&lt;/th>
33	&lt;th>PathFinder-PRM&lt;/th>
34	&lt;/tr>
35	&lt;/thead>
36	&lt;tbody>
37	&lt;tr>
38	&lt;td>
39	&lt;b>Question:&lt;/b> Weng earns $12 an hour for babysitting. Yesterday, she just did 50 minutes of babysitting. How much did she earn?&lt;br/>
40	&lt;b>Solution Steps:&lt;/b>&lt;br/>
41	          Weng earns &lt;math>12/60 = 0.2&lt;/math> dollars per minute.&lt;br/>
42	&lt;span style="color: green;">Correct Step&lt;/span>&lt;br/>
43	&lt;br/>
44	          Let's first calculate how much Weng earns per minute,&lt;br/>
45	&lt;span style="color: red;">Redundant Step&lt;/span>&lt;br/>
46	&lt;br/>
47	          Weng earns &lt;math>12/60 = 0.4&lt;/math> dollars per minute.&lt;br/>
48	&lt;span style="color: red;">Calculation Error&lt;/span>&lt;br/>
49	&lt;br/>
50	          Weng earns &lt;math>12/50 = 0.24&lt;/math> dollars per minute.&lt;br/>
51	&lt;span style="color: red;">Inconsistent with Question&lt;/span>
52	&lt;/td>
53	&lt;td>
54	&lt;br/>
55	          0.85&lt;br/>
56	&lt;br/>
57	          0.63&lt;br/>
58	&lt;br/>
59	          0.46&lt;br/>
60	&lt;br/>
61	          0.35
62	        &lt;/td>
63	&lt;td>
64	&lt;br/>
65	&lt;b>PathFinder-PRM&lt;/b>&lt;br/>
66	&lt;br/>
67	          Math &lt;span style="color: green;">✔&lt;/span> →&lt;br/>
68	          Consistency &lt;span style="color: green;">✔&lt;/span> → 0.95&lt;br/>
69	&lt;br/>
70	          Math &lt;span style="color: green;">✔&lt;/span> →&lt;br/>
71	          Consistency &lt;span style="color: green;">✔&lt;/span> → 0.37&lt;br/>
72	&lt;br/>
73	          Math &lt;span style="color: red;">✘&lt;/span> →&lt;br/>
74	          Consistency &lt;span style="color: green;">✔&lt;/span> → 0&lt;br/>
75	&lt;br/>
76	          Math &lt;span style="color: green;">✔&lt;/span> →&lt;br/>
77	          Consistency &lt;span style="color: red;">✘&lt;/span> → 0
78	        &lt;/td>
79	&lt;/tr>
80	&lt;/tbody>
81	&lt;/table>
82	
83	Figure 1: Comparing the Methodology of Existing PRMs against PathFinder-PRM.
84	
85	compute a step-level reward, we can obtain richer supervision and stronger guidance for downstream generation (depicted in Figure 1). To this end, we introduce PathFinder-PRM, an error-aware hierarchical PRM that (1) classifies each step to detect the presence of math or consistency errors, and (2) combines these fine-grained error labels to produce a final reward score.
86	
87	We construct a new training corpus by augmenting the human-annotated *PRM800K* (Lightman et al., 2023) and automated RLHFlow Mistral data (Xiong et al., 2024) with our three-dimensional labels, yielding around 400K richly annotated reasoning trajectories.
88	
89	Our experiments on ProcessBench (Zheng et al., 2024), PRMBench (Song et al., 2025), and a suite of end-to-end math benchmarks show that PathFinder-PRM not only establishes the new state of the art among PRMs trained on PRM800K-only data but also continues to scale gracefully when incorporating additional automated annotations.
90	
91	### Contributions
92	
93	- • We propose PathFinder-PRM, the first hierarchical PRM that explicitly types errors into *math* and *consistency* categories before estimating step optimality.
94	- • We curate a multi-source dataset of 400K mathematical reasoning trajectories with three-dimensional step-level labels, combining PRM800K and RLHFlow data under our unified schema.
95	
96	- • We demonstrate that error-aware hierarchical supervision yields substantial gains on ProcessBench and PRMBench, and leads to more accurate and robust end-to-end math problem solving under reward-guided search.
97	
98	## 2 Related Works
99	
100	**Process Reward Models:** Process reward models (PRMs) evaluate the quality of intermediate steps in reasoning processes. PRMs are a core component of test-time scaling, enabling small policy models to outperform much larger models on reasoning tasks by reinforcing productive reasoning pathways (Liu et al., 2025). Most recent work on PRMs has varied along two primary axes: (1) the choice of the base model architecture and (2) the methods used to synthesize step-level supervision labels (Wang et al., 2024b; Zhang et al., 2025; Khalifa et al., 2025). Discriminative PRMs are designed to classify the correctness of individual process steps within reasoning trajectories (Uesato et al., 2022). Corresponding training data synthesis approaches include gold human step-level annotations (Lightman et al., 2023), Monte Carlo estimation (Wang et al., 2024b; Luo et al., 2024), and consensus filtering methods (Zhang et al., 2025). Generative PRMs scale verifier compute, utilizing the language modeling head of the PRMs to generate a chain of thought (CoT) before producing step-level correctness classifications. Associated training data is typically obtained by filtering LLM-as-a-judge reasoning traces against human step-level labels (Khalifa et al., 2025; She et al., 2025)or relative progress estimation (Zhao et al., 2025).
101	
102	**Limitations of Current PRMs:** Current PRMs face significant challenges in detecting nuanced error types. Although frontier models excel at identifying obvious mistakes (Zheng et al., 2024), their performance deteriorates markedly when confronted with more subtle error types. The recently introduced PRMBench benchmark demonstrates this limitation, revealing substantial performance drops across fine-grained error categories such as redundancy, circular logic, step inconsistency and domain inconsistency (Song et al., 2025).
103	
104	### 3 Methodology
105	
106	#### 3.1 Task: Math Process Reward Modeling
107	
108	The primary task of a Process Reward Model in mathematical problem solving is to evaluate the correctness of each intermediate reasoning step generated by an LLM. Unlike ORMs, which assess only the final answer, PRMs evaluate at the step level, enabling fine-grained supervision and improved interpretability.
109	
110	Formally, given a multi-step solution  $\mathcal{S} = \{s_1, s_2, \dots, s_T\}$  produced by a language model for a math problem  $Q$ , the PRM assigns a scalar reward  $r_t \in \mathbb{R}$  to each step  $s_t$ , reflecting its mathematical and logical correctness. These rewards serve two main purposes:
111	
112	1. 1. **Error Detection:** By evaluating each step individually, PRMs can identify inaccurate or hallucinated reasoning in the solution process, even when the final answer may coincidentally be correct.
113	2. 2. **Guidance Toward Correct Solutions:** The step-level feedback provided by PRMs can be used to steer generation policies, in reinforcement learning or reward-guided generation, towards valid and logically coherent trajectories, thereby improving the overall quality of generated solutions.
114	
115	Process Reward Models enhance the robustness of mathematical reasoning systems by aligning training and inference with process-based correctness, rather than relying only on outcome validation.
116	
117	#### 3.2 PathFinder-PRM
118	
119	Existing Process Reward Models tackle both error detection and optimal path guidance jointly. Given a mathematical problem  $Q$  and a sequence
120	
121	of solution steps generated by a policy model,  $\mathcal{S} = \{s_1, s_2, \dots, s_T\}$ , these models assign each step a reward score conditioned on the question and all previous steps:
122	
123	$$R_t = \text{PRM}(Q, \mathcal{S}_{&lt;t}, s_t).$$
124	
125	where  $\mathcal{S}_{&lt;t} = \{s_1, s_2, \dots, s_{t-1}\}$ . The resulting score implicitly reflects both the presence of errors in  $s_t$  and its contribution towards a correct solution.
126	
127	In contrast, our approach takes a hierarchical perspective by decomposing the reward assignment into two sequential subtasks: (a) detecting errors in each reasoning step, and (b) using the error information to inform step optimality. Specifically, we first categorize errors into two types:
128	
129	1. 1. **Math Errors:** mistakes in arithmetic or algebraic manipulation, incorrect formula application, or invalid implications.
130	2. 2. **Consistency Errors:** logical inconsistencies with the question, prior steps, or established constraints.
131	
132	As seen in Figure 1, PathFinder-PRM performs two forward passes per step. In the first pass, it predicts the correctness probabilities for the two error types,  $M_t$  and  $C_t$ . In the second pass, it estimates the step’s reward  $R_t$ , explicitly conditioned on the detected error labels:
133	
134	$$M_t, C_t = \text{PathFinder-PRM}(Q, \mathcal{S}_{&lt;t}, s_t),$$
135	
136	$$R_t = \text{PathFinder-PRM}(Q, \mathcal{S}_{&lt;t}, s_t, M_t, C_t).$$
137	
138	By structuring reward modeling hierarchically, PathFinder-PRM leverages fine-grained error signals to improve reward estimation, while maintaining a clear separation between error detection and correct path guidance. We provide further details regarding the inference design in Appendix C
139	
140	To investigate this, we propose the following hypothesis:
141	
142	**Hypothesis:** A hierarchical supervision strategy—first detecting error types, then using them to compute rewards—is more effective than existing methods that compute rewards directly without identifying the presence of errors explicitly.
143	
144	#### 3.3 Creating the PathFinder-PRM Dataset
145	
146	The PathFinder-PRM dataset includes step-level fine-grained labels across three categories: (1) *mathematical reasoning accuracy*, (2) *consistency* with prior steps and mathematical domain, and (3) *step correctness*. Here, the third category*step correctness* identifies whether a step is both error-free and optimally contributes to solving the problem. For each process step, we assign a three-dimensional categorical score vector  $\mathbf{c}_t = (c_t^{\text{math}}, c_t^{\text{consistency}}, c_t^{\text{correctness}})$ , where each component  $c_t^{(i)} \in \{0, 1\}$  represents a binary label for the respective category. We construct this dataset by leveraging two existing datasets: the PRM800k (Lightman et al., 2023) and Mistral-PRM-Data by RLHFlow (Xiong et al., 2024). These datasets contain step-level correctness annotations generated through human evaluation and Monte Carlo estimation, respectively.
147	
148	**PRM800K Integration:** The original PRM800k dataset contains over 800,000 gold step-level correctness labels  $l_t \in \{-1, 0, 1\}$  for each reasoning step  $s_t$ . We transform each correctness label into our categorical score vector as follows:
149	
150	- • Steps with  $l_t = 1$  (correct and optimal) are mapped to  $\mathbf{c}_t = (1, 1, 1)$ .
151	- • Steps with  $l_t = 0$  (correct but suboptimal) are mapped to  $\mathbf{c}_t = (1, 1, 0)$ .
152	
153	This mapping reflects our interpretation that human labels  $l_t \in \{0, 1\}$  indicate error-free reasoning, with  $l_t = 0$  specifically denoting non-optimal process steps. For erroneous steps ( $l_t = -1$ ), the original correctness labels provide insufficient information to determine scores across our three evaluation categories. Therefore, we employ DeepSeek-R1-Distill-Qwen-32 B to generate binary labels for each category for these steps (DeepSeek-AI, 2025). To maintain dataset quality, we subsequently filter out samples with categorical score vectors that are inconsistent with  $-1$  human annotated labels (i.e.,  $\mathbf{c}_t = (1, 1, 1)$ ).
154	
155	**Mistral-PRM-Data Integration:** Since this dataset lacks gold standard step-level correctness labels, we utilize DeepSeek-R1-Distill-Qwen-32B to assign binary categorical labels to a small, randomly selected subset of process steps. To ensure data quality, we implement a consistency filtering mechanism. This removes score assignments that are logically incompatible with the existing Monte Carlo (MC) estimation labels. Specifically:
156	
157	- • For steps with MC estimation '+' labels (indicating positive assessment), we retain only samples with assignments of  $\mathbf{c}_t = (1, 1, 1)$ .
158	- • For steps with MC estimation '-' labels (indicating negative assessment), we retain sam-
159	
160	ples with categorizations where at least one component equals 0, i.e.,  $\mathbf{c}_t \neq (1, 1, 1)$ .
161	
162	In totality, the PathFinder-PRM dataset contains about 400K reasoning trajectory samples with step-level categorical score vectors  $\mathbf{c}_t$ . Of these 400K trajectories, approximately 345K are sourced from PRM800k and the other 55K reasoning paths are sourced from Mistral-PRM-Data. We train two variants of the model, PathFinder-PRM-7B and PathFinder-PRM-7B-PRM800k trained on the full dataset and just the PRM800K subset respectively.
163	
164	### 3.4 Training Recipe for PathFinder-PRM
165	
166	Previous studies demonstrate that a model’s mathematical reasoning ability correlates with its performance as a process reward model (Xia et al., 2025). Consequently, we initialize PathFinder-PRM from Qwen2.5-Math-7B-Instruct, which achieves state-of-the-art results on multiple math benchmarks (Yang et al., 2024). Unlike recent PRMs that swap the language modeling head for a scalar value head (Zhang et al., 2025; Xia et al., 2025; Tan et al., 2025), we preserve the original LM architecture and extend the tokenizer with two special tokens,  $\langle + \rangle$  and  $\langle - \rangle$ , to represent positive and negative step labels.
167	
168	**Training Objective** Each training example is structured in two parts, mirroring the inference passes:
169	
170	#### 1. Error Detection Target:
171	
172	Prompt + Math:  $\langle + \rangle / \langle - \rangle$ , Consistency:  $\langle + \rangle / \langle - \rangle$
173	
174	#### 2. Reward Estimation Target: Append the predicted error labels and the token
175	
176	Prompt + Math: [Math label], Consistency: [Consistency Label] + Correctness:  $\langle + \rangle / \langle - \rangle$
177	
178	For each sample, we compute the cross-entropy loss only on these label tokens.
179	
180	## 4 Experimental Setup
181	
182	### 4.1 Evaluation Benchmarks
183	
184	For math steps error detection, we use ProcessBench and PRMBench. **ProcessBench** is a benchmark designed to evaluate language models’ ability to identify errors in mathematical reasoning processes. It comprises 3,400 test cases, primarily&lt;table border="1">
185	&lt;thead>
186	&lt;tr>
187	&lt;th rowspan="2">Model&lt;/th>
188	&lt;th colspan="3">Simplicity&lt;/th>
189	&lt;th colspan="5">Soundness&lt;/th>
190	&lt;th colspan="4">Sensitivity&lt;/th>
191	&lt;th rowspan="2">Overall&lt;/th>
192	&lt;/tr>
193	&lt;tr>
194	&lt;th>NR.&lt;/th>
195	&lt;th>NCL.&lt;/th>
196	&lt;th>Avg.&lt;/th>
197	&lt;th>ES.&lt;/th>
198	&lt;th>SC.&lt;/th>
199	&lt;th>DC.&lt;/th>
200	&lt;th>CI.&lt;/th>
201	&lt;th>Avg.&lt;/th>
202	&lt;th>PS.&lt;/th>
203	&lt;th>DR.&lt;/th>
204	&lt;th>MS.&lt;/th>
205	&lt;th>Avg.&lt;/th>
206	&lt;/tr>
207	&lt;/thead>
208	&lt;tbody>
209	&lt;tr>
210	&lt;td colspan="14">&lt;b>LLM-as-judge, Open-source Language Models&lt;/b>&lt;/td>
211	&lt;/tr>
212	&lt;tr>
213	&lt;td>Qwen-2.5-Math-72B*&lt;/td>
214	&lt;td>55.3&lt;/td>
215	&lt;td>54.9&lt;/td>
216	&lt;td>55.1&lt;/td>
217	&lt;td>55.5&lt;/td>
218	&lt;td>71.6&lt;/td>
219	&lt;td>58.1&lt;/td>
220	&lt;td>59.1&lt;/td>
221	&lt;td>61.1&lt;/td>
222	&lt;td>47.4&lt;/td>
223	&lt;td>53.8&lt;/td>
224	&lt;td>&lt;b>100.0&lt;/b>&lt;/td>
225	&lt;td>67.1&lt;/td>
226	&lt;td>57.4&lt;/td>
227	&lt;/tr>
228	&lt;tr>
229	&lt;td>QwQ-Preview-32B*&lt;/td>
230	&lt;td>&lt;b>57.2&lt;/b>&lt;/td>
231	&lt;td>&lt;b>55.6&lt;/b>&lt;/td>
232	&lt;td>&lt;b>56.4&lt;/b>&lt;/td>
233	&lt;td>&lt;b>67.4&lt;/b>&lt;/td>
234	&lt;td>&lt;b>72.3&lt;/b>&lt;/td>
235	&lt;td>&lt;b>66.2&lt;/b>&lt;/td>
236	&lt;td>&lt;b>66.9&lt;/b>&lt;/td>
237	&lt;td>&lt;b>68.2&lt;/b>&lt;/td>
238	&lt;td>&lt;b>57.8&lt;/b>&lt;/td>
239	&lt;td>&lt;b>62.7&lt;/b>&lt;/td>
240	&lt;td>&lt;b>100.0&lt;/b>&lt;/td>
241	&lt;td>&lt;b>73.5&lt;/b>&lt;/td>
242	&lt;td>&lt;b>63.6&lt;/b>&lt;/td>
243	&lt;/tr>
244	&lt;tr>
245	&lt;td colspan="14">&lt;b>LLM-as-judge, Proprietary Language Models&lt;/b>&lt;/td>
246	&lt;/tr>
247	&lt;tr>
248	&lt;td>GPT-4o*&lt;/td>
249	&lt;td>57.0&lt;/td>
250	&lt;td>62.4&lt;/td>
251	&lt;td>59.7&lt;/td>
252	&lt;td>72.0&lt;/td>
253	&lt;td>69.7&lt;/td>
254	&lt;td>70.7&lt;/td>
255	&lt;td>71.1&lt;/td>
256	&lt;td>70.9&lt;/td>
257	&lt;td>&lt;b>62.5&lt;/b>&lt;/td>
258	&lt;td>&lt;b>65.7&lt;/b>&lt;/td>
259	&lt;td>99.2&lt;/td>
260	&lt;td>&lt;b>75.8&lt;/b>&lt;/td>
261	&lt;td>66.8&lt;/td>
262	&lt;/tr>
263	&lt;tr>
264	&lt;td>Gemini-2.0-flash-exp*&lt;/td>
265	&lt;td>67.2&lt;/td>
266	&lt;td>58.1&lt;/td>
267	&lt;td>62.7&lt;/td>
268	&lt;td>70.4&lt;/td>
269	&lt;td>65.7&lt;/td>
270	&lt;td>66.0&lt;/td>
271	&lt;td>67.3&lt;/td>
272	&lt;td>67.3&lt;/td>
273	&lt;td>61.8&lt;/td>
274	&lt;td>66.2&lt;/td>
275	&lt;td>98.2&lt;/td>
276	&lt;td>75.4&lt;/td>
277	&lt;td>66.0&lt;/td>
278	&lt;/tr>
279	&lt;tr>
280	&lt;td>Gemini-2.0-thinking-exp-1219*&lt;/td>
281	&lt;td>&lt;b>68.5&lt;/b>&lt;/td>
282	&lt;td>&lt;b>63.8&lt;/b>&lt;/td>
283	&lt;td>&lt;b>66.2&lt;/b>&lt;/td>
284	&lt;td>&lt;b>72.9&lt;/b>&lt;/td>
285	&lt;td>&lt;b>71.3&lt;/b>&lt;/td>
286	&lt;td>&lt;b>71.0&lt;/b>&lt;/td>
287	&lt;td>&lt;b>71.8&lt;/b>&lt;/td>
288	&lt;td>&lt;b>71.8&lt;/b>&lt;/td>
289	&lt;td>60.3&lt;/td>
290	&lt;td>&lt;b>65.7&lt;/b>&lt;/td>
291	&lt;td>&lt;b>99.8&lt;/b>&lt;/td>
292	&lt;td>75.3&lt;/td>
293	&lt;td>&lt;b>68.8&lt;/b>&lt;/td>
294	&lt;/tr>
295	&lt;tr>
296	&lt;td colspan="14">&lt;b>Discriminative Process Reward Models&lt;/b>&lt;/td>
297	&lt;/tr>
298	&lt;tr>
299	&lt;td>Math-Shepherd-7B*&lt;/td>
300	&lt;td>44.0&lt;/td>
301	&lt;td>50.3&lt;/td>
302	&lt;td>47.1&lt;/td>
303	&lt;td>49.4&lt;/td>
304	&lt;td>44.5&lt;/td>
305	&lt;td>41.3&lt;/td>
306	&lt;td>47.7&lt;/td>
307	&lt;td>45.7&lt;/td>
308	&lt;td>47.2&lt;/td>
309	&lt;td>48.6&lt;/td>
310	&lt;td>86.1&lt;/td>
311	&lt;td>60.7&lt;/td>
312	&lt;td>47.0&lt;/td>
313	&lt;/tr>
314	&lt;tr>
315	&lt;td>Math-PSA-7B&lt;sup>†&lt;/sup>&lt;/td>
316	&lt;td>47.6&lt;/td>
317	&lt;td>55.1&lt;/td>
318	&lt;td>51.3&lt;/td>
319	&lt;td>56.5&lt;/td>
320	&lt;td>49.4&lt;/td>
321	&lt;td>47.1&lt;/td>
322	&lt;td>54.2&lt;/td>
323	&lt;td>51.8&lt;/td>
324	&lt;td>51.7&lt;/td>
325	&lt;td>54.1&lt;/td>
326	&lt;td>88.9&lt;/td>
327	&lt;td>64.9&lt;/td>
328	&lt;td>52.3&lt;/td>
329	&lt;/tr>
330	&lt;tr>
331	&lt;td>RLHFlow-Mistral-8B*&lt;/td>
332	&lt;td>46.1&lt;/td>
333	&lt;td>47.3&lt;/td>
334	&lt;td>46.7&lt;/td>
335	&lt;td>56.6&lt;/td>
336	&lt;td>55.1&lt;/td>
337	&lt;td>54.4&lt;/td>
338	&lt;td>63.8&lt;/td>
339	&lt;td>57.5&lt;/td>
340	&lt;td>51.5&lt;/td>
341	&lt;td>56.2&lt;/td>
342	&lt;td>97.9&lt;/td>
343	&lt;td>68.5&lt;/td>
344	&lt;td>54.4&lt;/td>
345	&lt;/tr>
346	&lt;tr>
347	&lt;td>RLHFlow-DeepSeek-8B*&lt;/td>
348	&lt;td>46.4&lt;/td>
349	&lt;td>48.9&lt;/td>
350	&lt;td>47.6&lt;/td>
351	&lt;td>55.7&lt;/td>
352	&lt;td>55.0&lt;/td>
353	&lt;td>53.2&lt;/td>
354	&lt;td>66.2&lt;/td>
355	&lt;td>57.5&lt;/td>
356	&lt;td>49.0&lt;/td>
357	&lt;td>55.4&lt;/td>
358	&lt;td>&lt;b>99.8&lt;/b>&lt;/td>
359	&lt;td>68.1&lt;/td>
360	&lt;td>54.2&lt;/td>
361	&lt;/tr>
362	&lt;tr>
363	&lt;td>Lemma-PRM800k-7B*&lt;/td>
364	&lt;td>49.3&lt;/td>
365	&lt;td>53.4&lt;/td>
366	&lt;td>51.4&lt;/td>
367	&lt;td>56.4&lt;/td>
368	&lt;td>47.1&lt;/td>
369	&lt;td>46.7&lt;/td>
370	&lt;td>53.3&lt;/td>
371	&lt;td>50.9&lt;/td>
372	&lt;td>51.0&lt;/td>
373	&lt;td>53.5&lt;/td>
374	&lt;td>93.6&lt;/td>
375	&lt;td>66.0&lt;/td>
376	&lt;td>52.0&lt;/td>
377	&lt;/tr>
378	&lt;tr>
379	&lt;td>Skywork-PRM-7B*&lt;/td>
380	&lt;td>35.7&lt;/td>
381	&lt;td>41.2&lt;/td>
382	&lt;td>38.4&lt;/td>
383	&lt;td>36.7&lt;/td>
384	&lt;td>29.1&lt;/td>
385	&lt;td>30.6&lt;/td>
386	&lt;td>34.4&lt;/td>
387	&lt;td>32.7&lt;/td>
388	&lt;td>36.8&lt;/td>
389	&lt;td>37.4&lt;/td>
390	&lt;td>88.8&lt;/td>
391	&lt;td>54.3&lt;/td>
392	&lt;td>36.2&lt;/td>
393	&lt;/tr>
394	&lt;tr>
395	&lt;td>ReasonEval-7B*&lt;/td>
396	&lt;td>&lt;b>61.0&lt;/b>&lt;/td>
397	&lt;td>50.1&lt;/td>
398	&lt;td>55.5&lt;/td>
399	&lt;td>62.1&lt;/td>
400	&lt;td>65.9&lt;/td>
401	&lt;td>61.5&lt;/td>
402	&lt;td>66.0&lt;/td>
403	&lt;td>63.9&lt;/td>
404	&lt;td>55.6&lt;/td>
405	&lt;td>58.0&lt;/td>
406	&lt;td>99.5&lt;/td>
407	&lt;td>71.0&lt;/td>
408	&lt;td>60.0&lt;/td>
409	&lt;/tr>
410	&lt;tr>
411	&lt;td>Qwen2.5-Math-7B-PRM800K&lt;sup>†&lt;/sup>&lt;/td>
412	&lt;td>48.6&lt;/td>
413	&lt;td>47.8&lt;/td>
414	&lt;td>48.2&lt;/td>
415	&lt;td>62.1&lt;/td>
416	&lt;td>59.4&lt;/td>
417	&lt;td>58.7&lt;/td>
418	&lt;td>68.5&lt;/td>
419	&lt;td>62.2&lt;/td>
420	&lt;td>52.9&lt;/td>
421	&lt;td>64.0&lt;/td>
422	&lt;td>&lt;b>99.8&lt;/b>&lt;/td>
423	&lt;td>72.2&lt;/td>
424	&lt;td>58.3&lt;/td>
425	&lt;/tr>
426	&lt;tr>
427	&lt;td>Qwen2.5-Math-PRM-7B*&lt;/td>
428	&lt;td>49.0&lt;/td>
429	&lt;td>55.1&lt;/td>
430	&lt;td>52.1&lt;/td>
431	&lt;td>71.8&lt;/td>
432	&lt;td>67.3&lt;/td>
433	&lt;td>66.3&lt;/td>
434	&lt;td>&lt;b>78.5&lt;/b>&lt;/td>
435	&lt;td>71.0&lt;/td>
436	&lt;td>57.6&lt;/td>
437	&lt;td>69.1&lt;/td>
438	&lt;td>99.7&lt;/td>
439	&lt;td>75.5&lt;/td>
440	&lt;td>65.5&lt;/td>
441	&lt;/tr>
442	&lt;tr>
443	&lt;td>⊗ Pathfinder-PRM-7B-PRM800K&lt;br/>w/o Separate Subtask Prediction&lt;/td>
444	&lt;td>51.5&lt;/td>
445	&lt;td>61.3&lt;/td>
446	&lt;td>56.4&lt;/td>
447	&lt;td>69.7&lt;/td>
448	&lt;td>67.6&lt;/td>
449	&lt;td>65.9&lt;/td>
450	&lt;td>71.9&lt;/td>
451	&lt;td>68.8&lt;/td>
452	&lt;td>58.7&lt;/td>
453	&lt;td>66.6&lt;/td>
454	&lt;td>99.4&lt;/td>
455	&lt;td>74.9&lt;/td>
456	&lt;td>65.0&lt;/td>
457	&lt;/tr>
458	&lt;tr>
459	&lt;td>&lt;/td>
460	&lt;td>58.9&lt;/td>
461	&lt;td>&lt;b>66.7&lt;/b>&lt;/td>
462	&lt;td>&lt;b>62.8&lt;/b>&lt;/td>
463	&lt;td>68.6&lt;/td>
464	&lt;td>62.4&lt;/td>
465	&lt;td>62.4&lt;/td>
466	&lt;td>66.7&lt;/td>
467	&lt;td>65.0&lt;/td>
468	&lt;td>60.2&lt;/td>
469	&lt;td>64.9&lt;/td>
470	&lt;td>97.8&lt;/td>
471	&lt;td>74.3&lt;/td>
472	&lt;td>64.4&lt;/td>
473	&lt;/tr>
474	&lt;tr>
475	&lt;td>⊗ Pathfinder-PRM-7B&lt;br/>w/o Separate Error Categories&lt;/td>
476	&lt;td>52.1&lt;/td>
477	&lt;td>65.8&lt;/td>
478	&lt;td>58.9&lt;/td>
479	&lt;td>73.1&lt;/td>
480	&lt;td>68.7&lt;/td>
481	&lt;td>66.3&lt;/td>
482	&lt;td>75.0&lt;/td>
483	&lt;td>70.8&lt;/td>
484	&lt;td>&lt;b>61.7&lt;/b>&lt;/td>
485	&lt;td>&lt;b>69.8&lt;/b>&lt;/td>
486	&lt;td>99.2&lt;/td>
487	&lt;td>&lt;b>76.9&lt;/b>&lt;/td>
488	&lt;td>&lt;b>67.7&lt;/b>&lt;/td>
489	&lt;/tr>
490	&lt;tr>
491	&lt;td>&lt;/td>
492	&lt;td>51.7&lt;/td>
493	&lt;td>62.0&lt;/td>
494	&lt;td>56.9&lt;/td>
495	&lt;td>&lt;b>73.2&lt;/b>&lt;/td>
496	&lt;td>&lt;b>70.0&lt;/b>&lt;/td>
497	&lt;td>&lt;b>66.9&lt;/b>&lt;/td>
498	&lt;td>75.8&lt;/td>
499	&lt;td>&lt;b>71.5&lt;/b>&lt;/td>
500	&lt;td>60.3&lt;/td>
501	&lt;td>69.2&lt;/td>
502	&lt;td>99.6&lt;/td>
503	&lt;td>76.4&lt;/td>
504	&lt;td>67.3&lt;/td>
505	&lt;/tr>
506	&lt;tr>
507	&lt;td>&lt;/td>
508	&lt;td>57.9&lt;/td>
509	&lt;td>66.4&lt;/td>
510	&lt;td>62.1&lt;/td>
511	&lt;td>69.1&lt;/td>
512	&lt;td>62.6&lt;/td>
513	&lt;td>62.2&lt;/td>
514	&lt;td>68.7&lt;/td>
515	&lt;td>65.7&lt;/td>
516	&lt;td>61.0&lt;/td>
517	&lt;td>65.4&lt;/td>
518	&lt;td>98.2&lt;/td>
519	&lt;td>74.9&lt;/td>
520	&lt;td>64.9&lt;/td>
521	&lt;/tr>
522	&lt;/tbody>
523	&lt;/table>
524	
525	Table 1: Performance on **PRMBench**. Results marked with \* and † come from Song et al. and She et al. respectively. Bold text denotes the best results within each category. ⊗ represents the models we trained.
526	
527	sourced from different math reasoning benchmarks. Each case includes a step-by-step solution annotated by human experts to indicate the earliest step containing an error or to confirm the correctness of all steps. Models are tasked with pinpointing the first erroneous step in a solution or affirming the solution’s correctness. **PRMBench** is a fine-grained benchmark aimed at evaluating Process-Level Reward Models (PRMs) on their capability to detect nuanced errors in reasoning steps. It consists of 6,216 problems with a total of 83,456 step-level labels, assessing models across multiple dimensions: Simplicity (non-redundancy, non-circular logic), Soundness (empirical soundness, step consistency, domain consistency, confidence invariance), and Sensitivity (prerequisite sensitivity, deception resistance, multi-solution consistency). The benchmark uses both synthetic and human-verified data, with rigorous quality control measures, including manual verification of a subset of data. A composite metric, PRMScore, is introduced, combining positive and negative F1 scores for a balanced evaluation.
528	
529	To evaluate the effectiveness of Pathfinder-PRM in guiding step-by-step mathematical problem-solving, we employ it to assign
530	
531	scores to individual reasoning steps generated by large language models (LLMs), selecting only those with the highest overall rewards to build upon. This evaluation is conducted across several widely recognized math reasoning benchmarks, including AIME24, AMC23, MATH, Olympiad Bench, College MATH, and Minerva MATH&lt;sup>2&lt;/sup>.
532	
533	## 4.2 Baselines
534	
535	Our evaluation utilizes a diverse set of discriminative process reward models from recent literature as baselines: *Math-Shepherd* (Wang et al., 2024b), *Math-PSA* (Wang et al., 2024a), *RLHFlow-Mistral* and *RLHFlow-DeepSeek* (Xiong et al., 2024), *Skywork-PRM-7b* (o1 Team, 2024), *ReasonEval-7B* (Xia et al., 2025), *Lemma-PRM800k-7B* (Sun et al., 2024), *Qwen2.5-Math-PRM-7B* and *Qwen2.5-Math-7B-PRM800K* (Zhang et al., 2025). We selected these baselines to cover a diverse range of training regimes, including models trained on human annotations, automated annotations, and hybrid approaches, as well as varying scales of training data.
536	
537	&lt;sup>2&lt;/sup>Following (She et al., 2025), we use their subset of 200 test samples for Olympiad Bench and College MATH.**Performance Comparison Across Benchmarks of Models Trained on Similar-sized Dataset**
538	
539	Figure 2: Performance comparison of language models across three benchmarks. The PathFinder-PRM-7B model (gray) shows the highest performance across all benchmarks.
540	
541	## 5 Results
542	
543	### 5.1 Main Results
544	
545	**PathFinder-PRM-7B is the SOTA for PRMBench:** Table 1 shows the PRM-Bench results of the selected baselines, PathFinder-PRM-variants as well as LLM-as-judge performance of strong open-source and proprietary LLMs. In the discriminative PRM category, PathFinder-PRM-7B achieves the highest overall PRM score (67.7), outperforming Qwen2.5-Math-PRM-7B (65.5) and ReasonEval-7B (60.0). The variant PathFinder-PRM-7B-PRM800K, trained on a fraction of our dataset, achieves a competitive score of 65.0. Notably, PathFinder-PRM-7B outperforms nearly all LLM-as-Judge models, including GPT-4o, QwQ-Preview-32B and Gemini-2.0-flash-exp. PRMBench is a benchmark designed to test a model’s ability to detect subtle and complex errors. Our results affirm that our hierarchical PRM approach enables the model to detect these nuanced errors, leading to stronger process-level understanding and supervision.
546	
547	**PathFinder-PRM Excels on ProcessBench:** Table 2 presents F1 results on ProcessBench. When trained exclusively on PRM800K, PathFinder-PRM-7B-PRM800K attains an average F1 of 65.2, beating the previous best (Qwen2.5-Math-7B-PRM800K, 58.5) by 6.7 points and outperforming all other PRM800K-only baselines across every category: GSM8K (+5.9), MATH (+8.7), Olympiad Bench (+8.0) and
548	
549	OmniMath (+12.3).
550	
551	Leveraging a larger, mixed human + auto-annotated dataset further boosts performance. PathFinder-PRM-7B achieves an average F1 of 69.5, setting new state-of-the-art among mixed-data models and closing the gap to the top automated-annotation model (Qwen2.5-Math-PRM-7B\*, 73.5) to just 4 points. Notably, PathFinder-PRM-7B also leads in every individual benchmark—GSM8K (77.9), MATH (75.3), Olympiad Bench (65.0), and OmniMath (59.7), demonstrating the scalability and robustness of our hierarchical reward modeling approach.
552	
553	**Improved Reward-Guided Search with Better PRMs:** Finally, we assess the utility of our PRM in guiding solution search. Using Qwen2.5-Instruct-7B as a generator and ranking sampled steps in completions using our PRM, Table 3 shows that PathFinder-PRM-7B yields the highest average prm@8 score (48.25), outperforming Qwen2.5-Math-PRM-7B (46.8). The advantage holds across tasks, including challenging subsets such as AIME24 and College MATH, indicating better inductive bias and alignment with ground-truth solution quality.
554	
555	**PathFinder-PRM is Competitive to Qwen2.5-Math-PRM-7B Despite Using  $\tilde{3}\times$  Less Data:** Although Qwen2.5-Math-PRM-7B was trained on roughly 1.5M automated annotations, our PathFinder-PRM-7B, trained on only  $\sim 400K$  samples, matches or exceeds its performance in key benchmarks&lt;table border="1">
556	&lt;thead>
557	&lt;tr>
558	&lt;th>Model&lt;/th>
559	&lt;th># Samples&lt;/th>
560	&lt;th>GSM8K&lt;/th>
561	&lt;th>MATH&lt;/th>
562	&lt;th>Olympiad Bench&lt;/th>
563	&lt;th>OmniMath&lt;/th>
564	&lt;th>Avg. F1&lt;/th>
565	&lt;/tr>
566	&lt;/thead>
567	&lt;tbody>
568	&lt;tr>
569	&lt;td colspan="7">&lt;b>Trained on Automated Annotation Data&lt;/b>&lt;/td>
570	&lt;/tr>
571	&lt;tr>
572	&lt;td>Math-Shepherd-7B*&lt;/td>
573	&lt;td>445K&lt;/td>
574	&lt;td>47.9&lt;/td>
575	&lt;td>29.5&lt;/td>
576	&lt;td>24.8&lt;/td>
577	&lt;td>23.8&lt;/td>
578	&lt;td>31.5&lt;/td>
579	&lt;/tr>
580	&lt;tr>
581	&lt;td>RLHFlow-Mistral-8B*&lt;/td>
582	&lt;td>273K&lt;/td>
583	&lt;td>50.4&lt;/td>
584	&lt;td>33.4&lt;/td>
585	&lt;td>13.8&lt;/td>
586	&lt;td>15.8&lt;/td>
587	&lt;td>28.4&lt;/td>
588	&lt;/tr>
589	&lt;tr>
590	&lt;td>RLHFlow-DeepSeek-8B*&lt;/td>
591	&lt;td>253K&lt;/td>
592	&lt;td>38.8&lt;/td>
593	&lt;td>33.8&lt;/td>
594	&lt;td>16.9&lt;/td>
595	&lt;td>16.9&lt;/td>
596	&lt;td>26.6&lt;/td>
597	&lt;/tr>
598	&lt;tr>
599	&lt;td>Qwen2.5-Math-PRM-7B*&lt;/td>
600	&lt;td>~1.5M&lt;/td>
601	&lt;td>&lt;b>82.4&lt;/b>&lt;/td>
602	&lt;td>&lt;b>77.6&lt;/b>&lt;/td>
603	&lt;td>&lt;b>67.5&lt;/b>&lt;/td>
604	&lt;td>&lt;b>66.3&lt;/b>&lt;/td>
605	&lt;td>&lt;b>73.5&lt;/b>&lt;/td>
606	&lt;/tr>
607	&lt;tr>
608	&lt;td colspan="7">&lt;b>Trained on Human Annotated Data (PRM800K)&lt;/b>&lt;/td>
609	&lt;/tr>
610	&lt;tr>
611	&lt;td>Llemma-PRM800K-7B&lt;/td>
612	&lt;td>~350K&lt;/td>
613	&lt;td>48.4&lt;/td>
614	&lt;td>43.1&lt;/td>
615	&lt;td>28.5&lt;/td>
616	&lt;td>33.4&lt;/td>
617	&lt;td>38.4&lt;/td>
618	&lt;/tr>
619	&lt;tr>
620	&lt;td>ReasonEval-7B&lt;sup>†&lt;/sup>&lt;/td>
621	&lt;td>~350K&lt;/td>
622	&lt;td>41.0&lt;/td>
623	&lt;td>48.9&lt;/td>
624	&lt;td>36.7&lt;/td>
625	&lt;td>37.4&lt;/td>
626	&lt;td>41.0&lt;/td>
627	&lt;/tr>
628	&lt;tr>
629	&lt;td>Qwen2.5-Math-7B-PRM800K*&lt;/td>
630	&lt;td>264K&lt;/td>
631	&lt;td>68.2&lt;/td>
632	&lt;td>62.6&lt;/td>
633	&lt;td>50.7&lt;/td>
634	&lt;td>44.3&lt;/td>
635	&lt;td>58.5&lt;/td>
636	&lt;/tr>
637	&lt;tr>
638	&lt;td>PathFinder-PRM-7B-PRM800K&lt;/td>
639	&lt;td>~350K&lt;/td>
640	&lt;td>&lt;u>74.1&lt;/u>&lt;/td>
641	&lt;td>&lt;u>71.3&lt;/u>&lt;/td>
642	&lt;td>58.7&lt;/td>
643	&lt;td>56.6&lt;/td>
644	&lt;td>&lt;u>65.2&lt;/u>&lt;/td>
645	&lt;/tr>
646	&lt;tr>
647	&lt;td>w/o Separate Subtask Prediction&lt;/td>
648	&lt;td>&lt;/td>
649	&lt;td>71.4&lt;/td>
650	&lt;td>71.1&lt;/td>
651	&lt;td>&lt;u>59.2&lt;/u>&lt;/td>
652	&lt;td>&lt;u>58.0&lt;/u>&lt;/td>
653	&lt;td>64.9&lt;/td>
654	&lt;/tr>
655	&lt;tr>
656	&lt;td colspan="7">&lt;b>Trained on a Mix of Human and Automated Annotation Data&lt;/b>&lt;/td>
657	&lt;/tr>
658	&lt;tr>
659	&lt;td>Math-PSA-7B&lt;sup>†&lt;/sup>&lt;/td>
660	&lt;td>~860K&lt;/td>
661	&lt;td>62.4&lt;/td>
662	&lt;td>41.9&lt;/td>
663	&lt;td>31.5&lt;/td>
664	&lt;td>25.2&lt;/td>
665	&lt;td>40.3&lt;/td>
666	&lt;/tr>
667	&lt;tr>
668	&lt;td>Skywork-PRM-7B*&lt;/td>
669	&lt;td>unk&lt;/td>
670	&lt;td>70.8&lt;/td>
671	&lt;td>53.6&lt;/td>
672	&lt;td>22.9&lt;/td>
673	&lt;td>21.0&lt;/td>
674	&lt;td>42.1&lt;/td>
675	&lt;/tr>
676	&lt;tr>
677	&lt;td>⊗ PathFinder-PRM-7B&lt;/td>
678	&lt;td>~400K&lt;/td>
679	&lt;td>&lt;u>77.9&lt;/u>&lt;/td>
680	&lt;td>&lt;u>75.3&lt;/u>&lt;/td>
681	&lt;td>&lt;u>65.0&lt;/u>&lt;/td>
682	&lt;td>&lt;u>59.7&lt;/u>&lt;/td>
683	&lt;td>&lt;u>69.5&lt;/u>&lt;/td>
684	&lt;/tr>
685	&lt;tr>
686	&lt;td>w/o Separate Error Categories&lt;/td>
687	&lt;td>&lt;/td>
688	&lt;td>76.1&lt;/td>
689	&lt;td>73.8&lt;/td>
690	&lt;td>61.4&lt;/td>
691	&lt;td>56.6&lt;/td>
692	&lt;td>67.0&lt;/td>
693	&lt;/tr>
694	&lt;tr>
695	&lt;td>w/o Separate Subtask Prediction&lt;/td>
696	&lt;td>&lt;/td>
697	&lt;td>73.9&lt;/td>
698	&lt;td>72.6&lt;/td>
699	&lt;td>63.9&lt;/td>
700	&lt;td>59.9&lt;/td>
701	&lt;td>67.6&lt;/td>
702	&lt;/tr>
703	&lt;/tbody>
704	&lt;/table>
705	
706	Table 2: Performance (F1) on ProcessBench. Results marked with \* come from Zhang et al.. The best performance across all categories is in **bold** and the best performance within a category is underlined. # Samples denotes the number of training samples used by each model.
707	
708	&lt;table border="1">
709	&lt;thead>
710	&lt;tr>
711	&lt;th>Setting&lt;/th>
712	&lt;th>AIME24&lt;/th>
713	&lt;th>AMC23&lt;/th>
714	&lt;th>MATH&lt;/th>
715	&lt;th>Olympiad Bench&lt;/th>
716	&lt;th>College MATH&lt;/th>
717	&lt;th>Minerva MATH&lt;/th>
718	&lt;th>Avg.&lt;/th>
719	&lt;/tr>
720	&lt;/thead>
721	&lt;tbody>
722	&lt;tr>
723	&lt;td>pass@1*&lt;/td>
724	&lt;td>11.2&lt;/td>
725	&lt;td>47.8&lt;/td>
726	&lt;td>73.0&lt;/td>
727	&lt;td>38.0&lt;/td>
728	&lt;td>38.6&lt;/td>
729	&lt;td>37.2&lt;/td>
730	&lt;td>41.0&lt;/td>
731	&lt;/tr>
732	&lt;tr>
733	&lt;td>major@8*&lt;/td>
734	&lt;td>20.0&lt;/td>
735	&lt;td>57.5&lt;/td>
736	&lt;td>79.6&lt;/td>
737	&lt;td>47.0&lt;/td>
738	&lt;td>41.5&lt;/td>
739	&lt;td>42.7&lt;/td>
740	&lt;td>48.0&lt;/td>
741	&lt;/tr>
742	&lt;tr>
743	&lt;td>pass@8*&lt;/td>
744	&lt;td>33.3&lt;/td>
745	&lt;td>82.5&lt;/td>
746	&lt;td>88.8&lt;/td>
747	&lt;td>58.5&lt;/td>
748	&lt;td>47.5&lt;/td>
749	&lt;td>57.7&lt;/td>
750	&lt;td>61.4&lt;/td>
751	&lt;/tr>
752	&lt;tr>
753	&lt;td colspan="8">&lt;b>Reward Guided Search (prm@8)&lt;/b>&lt;/td>
754	&lt;/tr>
755	&lt;tr>
756	&lt;td>Math-Shepherd-7B*&lt;/td>
757	&lt;td>13.3&lt;/td>
758	&lt;td>52.5&lt;/td>
759	&lt;td>74.6&lt;/td>
760	&lt;td>38.5&lt;/td>
761	&lt;td>36.5&lt;/td>
762	&lt;td>41.2&lt;/td>
763	&lt;td>42.8&lt;/td>
764	&lt;/tr>
765	&lt;tr>
766	&lt;td>Math-PSA-7B*&lt;/td>
767	&lt;td>6.7&lt;/td>
768	&lt;td>57.5&lt;/td>
769	&lt;td>79.8&lt;/td>
770	&lt;td>42.5&lt;/td>
771	&lt;td>41.0&lt;/td>
772	&lt;td>39.3&lt;/td>
773	&lt;td>44.5&lt;/td>
774	&lt;/tr>
775	&lt;tr>
776	&lt;td>RLHFlow-PRM-Mistral-8B*&lt;/td>
777	&lt;td>10.0&lt;/td>
778	&lt;td>57.5&lt;/td>
779	&lt;td>73.4&lt;/td>
780	&lt;td>37.5&lt;/td>
781	&lt;td>38.0&lt;/td>
782	&lt;td>41.2&lt;/td>
783	&lt;td>42.9&lt;/td>
784	&lt;/tr>
785	&lt;tr>
786	&lt;td>RLHFlow-PRM-DeepSeek-8B*&lt;/td>
787	&lt;td>13.3&lt;/td>
788	&lt;td>52.5&lt;/td>
789	&lt;td>74.8&lt;/td>
790	&lt;td>39.5&lt;/td>
791	&lt;td>37.0&lt;/td>
792	&lt;td>40.8&lt;/td>
793	&lt;td>43.0&lt;/td>
794	&lt;/tr>
795	&lt;tr>
796	&lt;td>Lemma-PRM800k-7B*&lt;/td>
797	&lt;td>13.3&lt;/td>
798	&lt;td>57.5&lt;/td>
799	&lt;td>73.8&lt;/td>
800	&lt;td>40.0&lt;/td>
801	&lt;td>36.5&lt;/td>
802	&lt;td>38.2&lt;/td>
803	&lt;td>43.2&lt;/td>
804	&lt;/tr>
805	&lt;tr>
806	&lt;td>Skywork-PRM-7B*&lt;/td>
807	&lt;td>10.0&lt;/td>
808	&lt;td>57.5&lt;/td>
809	&lt;td>77.8&lt;/td>
810	&lt;td>41.5&lt;/td>
811	&lt;td>39.0&lt;/td>
812	&lt;td>43.4&lt;/td>
813	&lt;td>44.9&lt;/td>
814	&lt;/tr>
815	&lt;tr>
816	&lt;td>ReasonEval-7B*&lt;/td>
817	&lt;td>3.3&lt;/td>
818	&lt;td>55.0&lt;/td>
819	&lt;td>73.0&lt;/td>
820	&lt;td>37.5&lt;/td>
821	&lt;td>35.5&lt;/td>
822	&lt;td>37.9&lt;/td>
823	&lt;td>40.4&lt;/td>
824	&lt;/tr>
825	&lt;tr>
826	&lt;td>Qwen2.5-Math-7B-PRM800K*&lt;/td>
827	&lt;td>&lt;b>23.3&lt;/b>&lt;/td>
828	&lt;td>45.0&lt;/td>
829	&lt;td>78.2&lt;/td>
830	&lt;td>42.0&lt;/td>
831	&lt;td>35.5&lt;/td>
832	&lt;td>38.6&lt;/td>
833	&lt;td>43.8&lt;/td>
834	&lt;/tr>
835	&lt;tr>
836	&lt;td>Qwen2.5-Math-PRM-7B*&lt;/td>
837	&lt;td>16.7&lt;/td>
838	&lt;td>60.0&lt;/td>
839	&lt;td>&lt;b>81.0&lt;/b>&lt;/td>
840	&lt;td>43.5&lt;/td>
841	&lt;td>39.0&lt;/td>
842	&lt;td>40.4&lt;/td>
843	&lt;td>46.8&lt;/td>
844	&lt;/tr>
845	&lt;tr>
846	&lt;td>⊗ PathFinder-PRM-7B-PRM800K&lt;/td>
847	&lt;td>20.0&lt;/td>
848	&lt;td>55.0&lt;/td>
849	&lt;td>79.0&lt;/td>
850	&lt;td>36.0&lt;/td>
851	&lt;td>55.0&lt;/td>
852	&lt;td>36.4&lt;/td>
853	&lt;td>46.9&lt;/td>
854	&lt;/tr>
855	&lt;tr>
856	&lt;td>w/o Separate Subtask Prediction&lt;/td>
857	&lt;td>6.6&lt;/td>
858	&lt;td>55.0&lt;/td>
859	&lt;td>82.2&lt;/td>
860	&lt;td>36.0&lt;/td>
861	&lt;td>53.5&lt;/td>
862	&lt;td>36.0&lt;/td>
863	&lt;td>45.0&lt;/td>
864	&lt;/tr>
865	&lt;tr>
866	&lt;td>⊗ PathFinder-PRM-7B&lt;/td>
867	&lt;td>20&lt;/td>
868	&lt;td>62.5&lt;/td>
869	&lt;td>78.8&lt;/td>
870	&lt;td>36.5&lt;/td>
871	&lt;td>55.0&lt;/td>
872	&lt;td>36.7&lt;/td>
873	&lt;td>&lt;b>48.3&lt;/b>&lt;/td>
874	&lt;/tr>
875	&lt;tr>
876	&lt;td>w/o Separate Error Categories&lt;/td>
877	&lt;td>13.3&lt;/td>
878	&lt;td>52.5&lt;/td>
879	&lt;td>80.4&lt;/td>
880	&lt;td>35.5&lt;/td>
881	&lt;td>53.5&lt;/td>
882	&lt;td>37.5&lt;/td>
883	&lt;td>45.4&lt;/td>
884	&lt;/tr>
885	&lt;tr>
886	&lt;td>w/o Separate Subtask Prediction&lt;/td>
887	&lt;td>10.0&lt;/td>
888	&lt;td>55.0&lt;/td>
889	&lt;td>81.6&lt;/td>
890	&lt;td>37.0&lt;/td>
891	&lt;td>53.5&lt;/td>
892	&lt;td>36.0&lt;/td>
893	&lt;td>45.5&lt;/td>
894	&lt;/tr>
895	&lt;/tbody>
896	&lt;/table>
897	
898	Table 3: The performance of PRM guided greedy search with Qwen2.5-7B-Instruct as the policy model. Results marked with \* come from She et al.
899	
900	and reward-guided search. On ProcessBench, PathFinder-PRM-7B performs competitively to Qwen2.5-Math-PRM-7B in average F1 69.5 vs 73.5 despite using less than one-third of the data. More importantly, PathFinder-PRM-7B surpasses Qwen2.5-Math-PRM-7B on PRMBench overall (67.7 vs 65.5), and drives higher pass@8 in reward-guided greedy search (48.3 vs. 46.8). This demonstrates that our hierarchical, error-aware training yields more data-efficient and robust PRMs, achieving superior process supervision with far fewer samples.
901	
902	As shown in Figure 2, when comparing against PRMs trained on similarly sized datasets, PathFinder-PRM consistently achieves superior performance across all benchmarks. Figure 3 presents the performance of various PRMs on PRMBench. The results demonstrate that PathFinder-PRM not only surpasses other PRMs trained on comparably sized datasets but also outperforms Math-PSA and Qwen-2.5-Math-PRM, despite those models being trained on 2–3 times more data.Figure 3: PRMBench Overall PRMscore against the data scales of different baselines and PathFinder-PRM variants.
903	
904	## 5.2 Ablations
905	
906	In our approach, we made two main claims: (1) decoupling the subtasks of Error Detection and Correct Path Guidance, and (2) categorizing errors into two prominent error categories in math will boost PRM performance. To verify these claims, we performed ablation experiments by modifying parts of our method:
907	
908	1. 1. **PathFinder-PRM w/o Separate Subtask Prediction:** Following existing PRM approaches, we trained the model to jointly learn to tackle both error detection and correct path guidance using only the step correctness labels.
909	2. 2. **PathFinder-PRM w/o Separate Error Categories:** In this approach, we still do a hierarchical prediction but we modify step 1. Instead of detecting the presence of 2 error categories, we combined the categories and predicted the presence of an error in the step.
910	
911	**PathFinder-PRM Benefits from Separating Error Categories:** On ProcessBench, explicitly distinguishing math and consistency errors yields a clear overall boost: PathFinder-PRM-7B scores 69.5 Avg. F1, versus 67.0 for the PathFinder-PRM-7B w/o Separate Error Categories. We also observe a similar drop in performance on PRMBench, the PathFinder-PRM w/o Separate Error Categories shows a small drop in performance (0.4 points) compared to PathFinder-PRM-7B
912	
913	Crucially, reward-guided search highlights the practical impact of error typing: when ranking eight candidate solutions, PathFinder-PRM-7B achieves 48.3 prm@8, compared to just 45.4
914	
915	for PathFinder-PRM w/o Separate Error Categories (+2.9 points). This jump in real-world problem-solving performance highlights that fine-grained error signals not only improve diagnostic metrics but can also translate directly into selecting higher-quality solution paths.
916	
917	**PathFinder-PRM Benefits from Error-Aware Hierarchical Supervision:** Across ProcessBench, PRMBench, and reward-guided search, PathFinder-PRM consistently outperforms the PathFinder-PRM w/o separate subtask prediction, demonstrating the importance of hierarchical modeling of the subtasks. On ProcessBench, PathFinder-PRM-7B improves from 67.6 to 69.5 F1 (+1.9), and on PRMBench, from 64.9 to 67.7 (+2.8). In reward-guided search, the improvement is similarly clear: 48.3 prm@8 versus 45.5. These results highlight the value of decoupling feedback prediction into discrete reasoning components.
918	
919	**Scalable Performance with Additional Training Data:** Training on an additional 50K samples from a broader, automatically annotated dataset greatly boosted the performance of PathFinder-PRM and helped it reach state-of-the-art performance. PathFinder-PRM-7B outperforms PathFinder-PRM-7B-PRM800K across ProcessBench, PRMBench, and reward-guided greedy search, demonstrating the benefits of scaling beyond PRM800K dataset. On ProcessBench, PathFinder-PRM-7B achieves 69.5 Avg.F1 versus 65.2, while on PRMBench it improves from 65.0 to 67.7 F1. In reward-guided search, PathFinder-PRM-7B raises pass@8 from 46.9 to 48.3. These gains highlight that error-aware hierarchical modeling scales well with increased data diversity and quantity, enabling stronger generalization and robustness.
920	
921	A key distinction is that the 50K additional data was collected using Mistral-7B as a generator, while PRM800K was produced using a fine-tuned GPT-4 model. Exposure to reasoning traces from a smaller and weaker model may have helped PathFinder-PRM better learn to recognize and correct common failure patterns, contributing to improved robustness and generalization across benchmarks. We leave a deeper investigation of this hypothesis to future work.## Conclusion
922	
923	In this work, we introduced PathFinder-PRM, a hierarchical discriminative process reward model that decouples error detection from step optimality guidance, classifying math and consistency errors before computing step rewards. Our evaluation and ablation trials demonstrate that error-aware hierarchical supervision yields notable improvements on PRM benchmarks, with PathFinder-PRM-7B achieving state-of-the-art performance among discriminative PRMs on PRMBench and strong results on ProcessBench despite using less than three times the data used to train the current best performing model. A similar performance boost is observed in reward-guided search evaluation, affirming our hypothesis about the efficacy of hierarchical error-aware reward generation. Our approach is, therefore, a promising direction for more robust and interpretable process reward models, with potential for further gains when scaled to larger architectures.
924	
925	## Limitations
926	
927	Due to computational constraints, our experiments were limited to 7B models. While this scale provides a strong foundation for evaluating our proposed methodology, we hypothesise that larger models could further enhance modeling accuracy and better leverage process supervision signals due to their improved mathematical reasoning capabilities.
928	
929	## References
930	
931	Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel Ziegler, Jeffrey Wu, Clemens Winter, and 12 others. 2020. [Language models are few-shot learners](#). In *Advances in Neural Information Processing Systems*, volume 33, pages 1877–1901. Curran Associates, Inc.
932	
933	DeepSeek-AI. 2025. [Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning](#). *Preprint*, arXiv:2501.12948.
934	
935	Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, and 1 others. 2025. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. *arXiv preprint arXiv:2501.12948*.
936	
937	Muhammad Khalifa, Rishabh Agarwal, Lajanugen Logeswaran, Jaekyeom Kim, Hao Peng, Moontae Lee, Honglak Lee, and Lu Wang. 2025. [Process reward models that think](#). *arXiv preprint arXiv:2504.16828*.
938	
939	Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. 2023. Let’s verify step by step. *arXiv preprint arXiv:2305.20050*.
940	
941	Runze Liu, Junqi Gao, Jian Zhao, Kaiyan Zhang, Xiu Li, Biqing Qi, Wanli Ouyang, and Bowen Zhou. 2025. Can 1b llm surpass 405b llm? rethinking compute-optimal test-time scaling. *arXiv preprint arXiv:2502.06703*.
942	
943	Liangchen Luo, Yinxiao Liu, Rosanne Liu, Samrat Phatale, Meiqi Guo, Harsh Lara, Yunxuan Li, Lei Shu, Yun Zhu, Lei Meng, Jiao Sun, and Abhinav Rastogi. 2024. [Improve mathematical reasoning in language models by automated process supervision](#). *Preprint*, arXiv:2406.06592.
944	
945	Skywork o1 Team. 2024. Skywork-o1 open series. &lt;https://huggingface.co/Skywork>. Accessed: 2025-05-18.
946	
947	OpenAI. 2025. [Introducing openai o3 and o4-mini](#). Accessed: 2025-05-19.
948	
949	Shuaijie She, Junxiao Liu, Yifeng Liu, Jiajun Chen, Xin Huang, and Shujian Huang. 2025. R-prm: Reasoning-driven process reward modeling. *arXiv preprint arXiv:2503.21295*.
950	
951	Mingyang Song, Zhaochen Su, Xiaoye Qu, Jiawei Zhou, and Yu Cheng. 2025. Prmbench: A fine-grained and challenging benchmark for process-level reward models. *arXiv preprint arXiv:2501.03124*.
952	
953	Zhiqing Sun, Longhui Yu, Yikang Shen, Weiyang Liu, Yiming Yang, Sean Welleck, and Chuang Gan. 2024. Easy-to-hard generalization: Scalable alignment beyond human supervision. *arXiv preprint arXiv:2403.09472*.
954	
955	Xiaoyu Tan, Tianchu Yao, Chao Qu, Bin Li, Minghao Yang, Dakuan Lu, Haozhe Wang, Xihe Qiu, Wei Chu, Yinghui Xu, and 1 others. 2025. Aurora: Automated training framework of universal process reward models via ensemble prompting and reverse verification. *arXiv preprint arXiv:2502.11520*.
956	
957	Jonathan Uesato, Nate Kushman, Ramana Kumar, Francis Song, Noah Siegel, Lisa Wang, Antonia Creswell, Geoffrey Irving, and Irina Higgins. 2022. [Solving math word problems with process- and outcome-based feedback](#). *Preprint*, arXiv:2211.14275.
958	
959	Jun Wang, Meng Fang, Ziyu Wan, Muning Wen, Jiachen Zhu, Anjie Liu, Ziqin Gong, Yan Song, Lei Chen, Lionel M Ni, and 1 others. 2024a. Openrr: An open source framework for advanced reasoning with large language models. *arXiv preprint arXiv:2410.09671*.Peiyi Wang, Lei Li, Zhihong Shao, Runxin Xu, Damai Dai, Yifei Li, Deli Chen, Yu Wu, and Zhifang Sui. 2024b. [Math-shepherd: Verify and reinforce llms step-by-step without human annotations](#). In *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, page 9426–9439. Association for Computational Linguistics.
960	
961	Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. 2023. [Self-consistency improves chain of thought reasoning in language models](#). *Preprint*, arXiv:2203.11171.
962	
963	Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, brian ichter, Fei Xia, Ed Chi, Quoc V Le, and Denny Zhou. 2022. [Chain-of-thought prompting elicits reasoning in large language models](#). In *Advances in Neural Information Processing Systems*, volume 35, pages 24824–24837. Curran Associates, Inc.
964	
965	Thomas Wolf, Lysandre Debut, Victor Sanh, Julien Chaumond, Clement Delangue, Anthony Moi, Pieric Cistac, Tim Rault, Rémi Louf, Morgan Funtowicz, Joe Davison, Sam Shleifer, Patrick von Platen, Clara Ma, Yacine Jernite, Julien Plu, Canwen Xu, Teven Le Scao, Sylvain Gugger, and 3 others. 2020. [Transformers: State-of-the-art natural language processing](#). In *Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing: System Demonstrations*, pages 38–45, Online. Association for Computational Linguistics.
966	
967	Shijie Xia, Xuefeng Li, Yixin Liu, Tongshuang Wu, and Pengfei Liu. 2025. Evaluating mathematical reasoning beyond accuracy. In *Proceedings of the AAAI Conference on Artificial Intelligence*, volume 39, pages 27723–27730.
968	
969	Wei Xiong, Hanning Zhang, Nan Jiang, and Tong Zhang. 2024. An implementation of generative prm. &lt;https://github.com/RLHFlow/RLHF-Reward-Modeling>.
970	
971	An Yang, Beichen Zhang, Binyuan Hui, Bofei Gao, Bowen Yu, Chengpeng Li, Dayiheng Liu, Jianhong Tu, Jingren Zhou, Junyang Lin, Keming Lu, Mingfeng Xue, Runji Lin, Tianyu Liu, Xingzhang Ren, and Zhenru Zhang. 2024. Qwen2.5-math technical report: Toward mathematical expert model via self-improvement. *arXiv preprint arXiv:2409.12122*.
972	
973	Zhenru Zhang, Chujie Zheng, Yangzhen Wu, Beichen Zhang, Runji Lin, Bowen Yu, Dayiheng Liu, Jingren Zhou, and Junyang Lin. 2025. The lessons of developing process reward models in mathematical reasoning. *arXiv preprint arXiv:2501.07301*.
974	
975	Jian Zhao, Runze Liu, Kaiyan Zhang, Zhimu Zhou, Junqi Gao, Dong Li, Jiafei Lyu, Zhouyi Qian, Biqing Qi, Xiu Li, and Bowen Zhou. 2025. Genprm: Scaling test-time compute of process reward models via generative reasoning. *arXiv preprint arXiv:2504.00891*.
976	
977	Chujie Zheng, Zhenru Zhang, Beichen Zhang, Runji Lin, Keming Lu, Bowen Yu, Dayiheng Liu, Jingren Zhou, and Junyang Lin. 2024. [Processbench: Identifying process errors in mathematical reasoning](#). *Preprint*, arXiv:2412.06559.## A Extended Results
978	
979	### A.1 ProcessBench
980	
981	Table 4 contains the extended evaluation on ProcessBench with LLM-as-Judge Baselines using both Proprietary and Open-Source Language Models.
982	
983	&lt;table border="1">
984	&lt;thead>
985	&lt;tr>
986	&lt;th>Model&lt;/th>
987	&lt;th># Samples&lt;/th>
988	&lt;th>GSM8K&lt;/th>
989	&lt;th>MATH&lt;/th>
990	&lt;th>Olympiad Bench&lt;/th>
991	&lt;th>OmniMath&lt;/th>
992	&lt;th>Avg. F1&lt;/th>
993	&lt;/tr>
994	&lt;/thead>
995	&lt;tbody>
996	&lt;tr>
997	&lt;td colspan="7">&lt;i>LLM-as-judge, Proprietary language models&lt;/i>&lt;/td>
998	&lt;/tr>
999	&lt;tr>
1000	&lt;td>GPT-4o*&lt;/td>
1001	&lt;td>unk&lt;/td>
1002	&lt;td>79.2&lt;/td>
1003	&lt;td>63.6&lt;/td>
1004	&lt;td>51.4&lt;/td>
1005	&lt;td>53.5&lt;/td>
1006	&lt;td>61.9&lt;/td>
1007	&lt;/tr>
1008	&lt;tr>
1009	&lt;td>o1-mini*&lt;/td>
1010	&lt;td>unk&lt;/td>
1011	&lt;td>&lt;b>93.2&lt;/b>&lt;/td>
1012	&lt;td>88.9&lt;/td>
1013	&lt;td>87.2&lt;/td>
1014	&lt;td>82.4&lt;/td>
1015	&lt;td>87.9&lt;/td>
1016	&lt;/tr>
1017	&lt;tr>
1018	&lt;td colspan="7">&lt;i>LLM-as-judge, Open-source language models&lt;/i>&lt;/td>
1019	&lt;/tr>
1020	&lt;tr>
1021	&lt;td>Llama-3.3-70B-Instruct*&lt;/td>
1022	&lt;td>unk&lt;/td>
1023	&lt;td>82.9&lt;/td>
1024	&lt;td>59.4&lt;/td>
1025	&lt;td>46.7&lt;/td>
1026	&lt;td>43.0&lt;/td>
1027	&lt;td>58.0&lt;/td>
1028	&lt;/tr>
1029	&lt;tr>
1030	&lt;td>Qwen2.5-Math-72B-Instruct*&lt;/td>
1031	&lt;td>unk&lt;/td>
1032	&lt;td>65.8&lt;/td>
1033	&lt;td>52.1&lt;/td>
1034	&lt;td>32.5&lt;/td>
1035	&lt;td>31.7&lt;/td>
1036	&lt;td>45.5&lt;/td>
1037	&lt;/tr>
1038	&lt;tr>
1039	&lt;td>Qwen2.5-72B-Instruct*&lt;/td>
1040	&lt;td>unk&lt;/td>
1041	&lt;td>76.2&lt;/td>
1042	&lt;td>61.8&lt;/td>
1043	&lt;td>54.6&lt;/td>
1044	&lt;td>52.2&lt;/td>
1045	&lt;td>61.2&lt;/td>
1046	&lt;/tr>
1047	&lt;tr>
1048	&lt;td colspan="7">&lt;i>Discriminative Process Reward Models&lt;/i>&lt;/td>
1049	&lt;/tr>
1050	&lt;tr>
1051	&lt;td colspan="7">&lt;b>Trained on Automated Annotation Data&lt;/b>&lt;/td>
1052	&lt;/tr>
1053	&lt;tr>
1054	&lt;td>Math-Shepherd-7B*&lt;/td>
1055	&lt;td>445K&lt;/td>
1056	&lt;td>47.9&lt;/td>
1057	&lt;td>29.5&lt;/td>
1058	&lt;td>24.8&lt;/td>
1059	&lt;td>23.8&lt;/td>
1060	&lt;td>31.5&lt;/td>
1061	&lt;/tr>
1062	&lt;tr>
1063	&lt;td>RLHFlow-Mistral-8B*&lt;/td>
1064	&lt;td>273K&lt;/td>
1065	&lt;td>50.4&lt;/td>
1066	&lt;td>33.4&lt;/td>
1067	&lt;td>13.8&lt;/td>
1068	&lt;td>15.8&lt;/td>
1069	&lt;td>28.4&lt;/td>
1070	&lt;/tr>
1071	&lt;tr>
1072	&lt;td>RLHFlow-DeepSeek-8B*&lt;/td>
1073	&lt;td>253K&lt;/td>
1074	&lt;td>38.8&lt;/td>
1075	&lt;td>33.8&lt;/td>
1076	&lt;td>16.9&lt;/td>
1077	&lt;td>16.9&lt;/td>
1078	&lt;td>26.6&lt;/td>
1079	&lt;/tr>
1080	&lt;tr>
1081	&lt;td>Qwen2.5-Math-PRM-7B*&lt;/td>
1082	&lt;td>~1.5M&lt;/td>
1083	&lt;td>&lt;b>82.4&lt;/b>&lt;/td>
1084	&lt;td>&lt;b>77.6&lt;/b>&lt;/td>
1085	&lt;td>&lt;b>67.5&lt;/b>&lt;/td>
1086	&lt;td>&lt;b>66.3&lt;/b>&lt;/td>
1087	&lt;td>&lt;b>73.5&lt;/b>&lt;/td>
1088	&lt;/tr>
1089	&lt;tr>
1090	&lt;td colspan="7">&lt;b>Trained on Human Annotated Data (PRM800K)&lt;/b>&lt;/td>
1091	&lt;/tr>
1092	&lt;tr>
1093	&lt;td>Llemma-PRM800K-7B&lt;/td>
1094	&lt;td>~350K&lt;/td>
1095	&lt;td>48.4&lt;/td>
1096	&lt;td>43.1&lt;/td>
1097	&lt;td>28.5&lt;/td>
1098	&lt;td>33.4&lt;/td>
1099	&lt;td>38.4&lt;/td>
1100	&lt;/tr>
1101	&lt;tr>
1102	&lt;td>ReasonEval-7B&lt;sup>†&lt;/sup>&lt;/td>
1103	&lt;td>~350K&lt;/td>
1104	&lt;td>41.0&lt;/td>
1105	&lt;td>48.9&lt;/td>
1106	&lt;td>36.7&lt;/td>
1107	&lt;td>37.4&lt;/td>
1108	&lt;td>41.0&lt;/td>
1109	&lt;/tr>
1110	&lt;tr>
1111	&lt;td>Qwen2.5-Math-7B-PRM800K*&lt;/td>
1112	&lt;td>264K&lt;/td>
1113	&lt;td>68.2&lt;/td>
1114	&lt;td>62.6&lt;/td>
1115	&lt;td>50.7&lt;/td>
1116	&lt;td>44.3&lt;/td>
1117	&lt;td>58.5&lt;/td>
1118	&lt;/tr>
1119	&lt;tr>
1120	&lt;td>PathFinder-PRM-7B-PRM800K&lt;/td>
1121	&lt;td>~350K&lt;/td>
1122	&lt;td>&lt;u>74.1&lt;/u>&lt;/td>
1123	&lt;td>&lt;u>71.3&lt;/u>&lt;/td>
1124	&lt;td>58.7&lt;/td>
1125	&lt;td>56.6&lt;/td>
1126	&lt;td>&lt;u>65.2&lt;/u>&lt;/td>
1127	&lt;/tr>
1128	&lt;tr>
1129	&lt;td>w/o Separate Subtask Prediction&lt;/td>
1130	&lt;td>&lt;/td>
1131	&lt;td>71.4&lt;/td>
1132	&lt;td>71.1&lt;/td>
1133	&lt;td>&lt;u>59.2&lt;/u>&lt;/td>
1134	&lt;td>&lt;u>58.0&lt;/u>&lt;/td>
1135	&lt;td>64.9&lt;/td>
1136	&lt;/tr>
1137	&lt;tr>
1138	&lt;td colspan="7">&lt;b>Trained on a Mix of Human and Automated Annotation Data&lt;/b>&lt;/td>
1139	&lt;/tr>
1140	&lt;tr>
1141	&lt;td>Math-PSA-7B&lt;sup>†&lt;/sup>&lt;/td>
1142	&lt;td>~860K&lt;/td>
1143	&lt;td>62.4&lt;/td>
1144	&lt;td>41.9&lt;/td>
1145	&lt;td>31.5&lt;/td>
1146	&lt;td>25.2&lt;/td>
1147	&lt;td>40.3&lt;/td>
1148	&lt;/tr>
1149	&lt;tr>
1150	&lt;td>Skywork-PRM-7B*&lt;/td>
1151	&lt;td>unk&lt;/td>
1152	&lt;td>70.8&lt;/td>
1153	&lt;td>53.6&lt;/td>
1154	&lt;td>22.9&lt;/td>
1155	&lt;td>21.0&lt;/td>
1156	&lt;td>42.1&lt;/td>
1157	&lt;/tr>
1158	&lt;tr>
1159	&lt;td>⊗ PathFinder-PRM-7B&lt;/td>
1160	&lt;td>~400K&lt;/td>
1161	&lt;td>&lt;u>77.9&lt;/u>&lt;/td>
1162	&lt;td>&lt;u>75.3&lt;/u>&lt;/td>
1163	&lt;td>&lt;u>65.0&lt;/u>&lt;/td>
1164	&lt;td>&lt;u>59.7&lt;/u>&lt;/td>
1165	&lt;td>&lt;u>69.5&lt;/u>&lt;/td>
1166	&lt;/tr>
1167	&lt;tr>
1168	&lt;td>w/o Separate Error Categories&lt;/td>
1169	&lt;td>&lt;/td>
1170	&lt;td>76.1&lt;/td>
1171	&lt;td>73.8&lt;/td>
1172	&lt;td>61.4&lt;/td>
1173	&lt;td>56.6&lt;/td>
1174	&lt;td>67.0&lt;/td>
1175	&lt;/tr>
1176	&lt;tr>
1177	&lt;td>w/o Separate Subtask Prediction&lt;/td>
1178	&lt;td>&lt;/td>
1179	&lt;td>73.9&lt;/td>
1180	&lt;td>72.6&lt;/td>
1181	&lt;td>63.9&lt;/td>
1182	&lt;td>59.9&lt;/td>
1183	&lt;td>67.6&lt;/td>
1184	&lt;/tr>
1185	&lt;/tbody>
1186	&lt;/table>
1187	
1188	Table 4: Performance (F1) on ProcessBench. Results marked with \* come from Zhang et al.. The best performance across all categories is in **bold** and the best performance within a category is underlined.
1189	
1190	## B Scaling Effects of Additional RLHFlow Mistral Data
1191	
1192	To further probe the effects of training data scaling, we increased the amount of RLHFlow Mistral data from 50K to 200K samples and retrained PathFinder-PRM. As shown in Table 5, this increase from 400K to 550K total training samples did not result in improved performance. In fact, we observe a slight drop across all benchmarks: ProcessBench performance decreased from 69.5 to 68.75 Avg.F1, PRMBench from 67.7 to 67.4, and reward-guided search accuracy dropped from 48.3 to 47.5.
1193	
1194	These findings suggest that the benefits of augmenting training with weaker model-generated traces (e.g., from Mistral-7B) may saturate quickly. Simply increasing the volume of such data does not necessarily lead to improved generalization, and may even slightly degrade performance. This underscores the importance of data quality and the nuanced role of diversity over quantity in training PRMs. We leave further study into effective feedback curation and dataset composition to future work.
1195	
1196	&lt;table border="1">
1197	&lt;thead>
1198	&lt;tr>
1199	&lt;th>Model&lt;/th>
1200	&lt;th># Total samples&lt;/th>
1201	&lt;th># Mistral samples&lt;/th>
1202	&lt;th>ProcessBench&lt;/th>
1203	&lt;th>PRMBench&lt;/th>
1204	&lt;th>Reward Guided Search (PRM@8)&lt;/th>
1205	&lt;/tr>
1206	&lt;/thead>
1207	&lt;tbody>
1208	&lt;tr>
1209	&lt;td>PathFinder-PRM-7B-PRM800K&lt;/td>
1210	&lt;td>350K&lt;/td>
1211	&lt;td>0&lt;/td>
1212	&lt;td>65.2&lt;/td>
1213	&lt;td>65.0&lt;/td>
1214	&lt;td>46.9&lt;/td>
1215	&lt;/tr>
1216	&lt;tr>
1217	&lt;td>PathFinder-PRM-7B&lt;/td>
1218	&lt;td>400K&lt;/td>
1219	&lt;td>50K&lt;/td>
1220	&lt;td>69.5&lt;/td>
1221	&lt;td>67.7&lt;/td>
1222	&lt;td>48.3&lt;/td>
1223	&lt;/tr>
1224	&lt;tr>
1225	&lt;td>PathFinder-PRM-7B&lt;/td>
1226	&lt;td>550K&lt;/td>
1227	&lt;td>200K&lt;/td>
1228	&lt;td>68.75&lt;/td>
1229	&lt;td>67.4&lt;/td>
1230	&lt;td>47.5&lt;/td>
1231	&lt;/tr>
1232	&lt;/tbody>
1233	&lt;/table>
1234	
1235	Table 5: Effect of scaling RLHFlow Mistral data on PathFinder-PRM performance.## C Design Choice: Two Forward Passes over Autoregressive Multi-Token Prediction
1236	
1237	In PathFinder-PRM, we adopt a two-forward-pass approach to predict intermediate error labels—Math Error and Consistency Error—followed by a final reward score for correctness. This contrasts with autoregressive decoding, which would generate all three labels sequentially. The motivation behind this design is to minimize error cascading between dependent predictions. Specifically, we aim to predict Math and Consistency labels independently in the first forward pass to prevent the Consistency prediction from being influenced by the previously generated Math label. This is a potential issue in the autoregressive setup since each token depends on the ones before it.
1238	
1239	In our setup, a single language modeling head is used without any task-specific heads. During the first forward pass, we construct the input as: [PRM Input], Math: &lt;mask>, Consistency: &lt;mask>, where the two special &lt;mask> tokens represent the target positions for Math and Consistency labels. The model is trained to produce the correct label tokens at these masked positions, allowing us to decode both predictions simultaneously without one influencing the other.
1240	
1241	In the second forward pass, we supply the previously predicted Math and Consistency tokens in place, and append a third &lt;mask> token to infer the final correctness label: [PRM Input], Math: predicted\_label, Consistency: predicted\_label, Correctness: &lt;mask>. The probability corresponding to the positive reward token at the final mask position is then used as the model’s output reward score.
1242	
1243	This inference method avoids sequential decoding and uses only masked forward passes, enabling clearer modular supervision and avoiding implicit dependency leakage between intermediate labels. During training, a similar masked format is used. This clean separation helps PathFinder-PRM to better capture independent error signals and contributes to its robustness.
1244	
1245	---
1246	
1247	**Algorithm 1** PathFinder-PRM Inference via Two Forward Passes
1248	
1249	---
1250	
1251	**Require:** Prompt  $P$ , PathFinder-PRM
1252	
1253	```
1254	1: // First Forward Pass: Predict Math and Consistency Labels
1255	2:  $Input_1 \leftarrow concatenate(P, "Math: &lt;mask>", "Consistency: &lt;mask>")$ 
1256	3:  $Logits_1 \leftarrow PathFinder-PRM.forward(Input_1)$ 
1257	4:  $pred_{math} \leftarrow argmax(Logits_1 \text{ at Math mask position})$ 
1258	5:  $pred_{consistency} \leftarrow argmax(Logits_1 \text{ at Consistency mask position})$ 
1259	
1260	6: // Second Forward Pass: Predict Correctness/Reward Label
1261	7:  $Input_2 \leftarrow concatenate(P, "Math: ", pred_{math},$ 
1262	   "Consistency: ", pred_{consistency},
1263	   "Correctness: &lt;mask>")
1264	
1265	8:  $Logits_2 \leftarrow PathFinder-PRM.forward(Input_2)$ 
1266	9:  $reward_{prob} \leftarrow softmax(Logits_2 \text{ at Correctness mask position})$ 
1267	10:  $pred_{reward} \leftarrow reward_{prob} \text{ of } \langle + \rangle \text{ token}$ 
1268	11: return  $pred_{math}, pred_{consistency}, pred_{reward}$ 
1269	```
1270	
1271	---## D Data Annotation Prompt
1272	
1273	The prompt below was utilized with DeepSeek-R1-Distill-Qwen-32B to synthesize the 3-dimensional categorical score vectors assigned to each sample in the dataset used to train PathFinder-PRM
1274	
1275	### Prompt for dataset labelling
1276	
1277	You are an analytical math instructor grading a student's work. Think step-by-step through your analysis. Below is the math question, the previous steps by the student, and the current step to evaluate.
1278	
1279	{context}
1280	
1281	Your task is to rigorously examine the current step and determine if it contains ANY mathematical errors. Assign binary scores (0 = wrong, 1 = correct) based on three criteria:
1282	
1283	A) Mathematical logic — Is the current step, **on its own**, mathematically valid? Check for: • Calculation errors • Incorrect formula application • Invalid operations or simplifications • Algebra mistakes or sign errors • Incorrect assertions
1284	
1285	B) Consistency — Is the current step logically consistent with: • Established ground truth • Previous steps • Any constraints or conditions established earlier • The mathematical domain applicable to this problem
1286	
1287	C) Simplicity and optimality — is this step an efficient next step toward the solution? Check for: • Redundant statements: factually correct statements that do not help progress toward the solution. • Circular logic: does this step come to a conclusion already previously established? • Non-clarity: Are the assertions made in this step ambiguous in a way that obscures their purpose? • Optimality: is the **idea** of this step the near optimal approach one would take to solve the problem?
1288	
1289	Double check all listed criterion here explicitly in your reasoning. In your analysis, be sensitive to subtle issues like missing pre-requisites/assumptions, correct-looking statements with slight errors and high confidence statements containing errors.
1290	
1291	### IMPORTANT POINTS:
1292	
1293	- If you find ANY error, even a minor one, you **MUST** assign a score of 0 to the appropriate criteria. Be skeptical and verify all claims thoroughly.
1294	
1295	- For incorrect steps, wherever possible, attempt to categorize the issue as violating **one of the three criterion** (i.e., assign score 0 to **only one category**). Assign multiple 0 scores only for serious errors.
1296	
1297	You must format your answer as below:
1298	
1299	Reasoning:
1300	
1301	{{Provide detailed analysis, showing all verification steps and explicitly identifying any errors found}}
1302	
1303	Final answers:
1304	
1305	Score A:
1306	
1307	{{0 or 1 only}}
1308	
1309	Score B:
1310	
1311	{{0 or 1 only}}
1312	
1313	Score C:
1314	
1315	{{0 or 1 only}}### E Training HyperParameters
1316	
1317	Table 6 contains the hyperparameters used to train PathFinder-PRM. We used the Transformers library Trainer implementation to train our model in a seq-to-seq manner (Wolf et al., 2020).
1318	
1319	&lt;table border="1">&lt;thead>&lt;tr>&lt;th>Parameter&lt;/th>&lt;th>Value&lt;/th>&lt;/tr>&lt;/thead>&lt;tbody>&lt;tr>&lt;td>Model&lt;/td>&lt;td>QwenQwen2.5-Math-7B-Instruct&lt;/td>&lt;/tr>&lt;tr>&lt;td>Torch Data type&lt;/td>&lt;td>bfloat16&lt;/td>&lt;/tr>&lt;tr>&lt;td>Attention Implementation&lt;/td>&lt;td>flash attention 2&lt;/td>&lt;/tr>&lt;tr>&lt;td>Per-device Train Batch Size&lt;/td>&lt;td>2&lt;/td>&lt;/tr>&lt;tr>&lt;td>Gradient Accumulation Steps&lt;/td>&lt;td>32&lt;/td>&lt;/tr>&lt;tr>&lt;td>Learning Rate&lt;/td>&lt;td>1.0e-05&lt;/td>&lt;/tr>&lt;tr>&lt;td>Number of Training Epochs&lt;/td>&lt;td>4&lt;/td>&lt;/tr>&lt;tr>&lt;td>LR Scheduler Type&lt;/td>&lt;td>cosine&lt;/td>&lt;/tr>&lt;tr>&lt;td>Max Gradient Norm&lt;/td>&lt;td>1.0&lt;/td>&lt;/tr>&lt;tr>&lt;td>Warmup Ratio&lt;/td>&lt;td>0.1&lt;/td>&lt;/tr>&lt;tr>&lt;td>Seed&lt;/td>&lt;td>42&lt;/td>&lt;/tr>&lt;tr>&lt;td>BF16&lt;/td>&lt;td>true&lt;/td>&lt;/tr>&lt;tr>&lt;td>Optimizer&lt;/td>&lt;td>adam&lt;/td>&lt;/tr>&lt;tr>&lt;td>Gradient Checkpointing&lt;/td>&lt;td>True&lt;/td>&lt;/tr>&lt;/tbody>&lt;/table>
1320	
1321	Table 6: Training Configuration for Qwen2.5-Math-7B-Instruct.
1322	
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02ab4ca8-6cbb-428d-86b2-c377726b4b5e",
  "isSidechain": true,
  "promptId": "11c0ed01-00cd-4aa6-94b3-6d386d5b1cba",
  "agentId": "a91780e1d5a06a47f",
  "type": "user",
  "uuid": "2cfeca03-f38d-4e17-bcfb-96f050fa512a",
  "sourceToolAssistantUUID": "02ab4ca8-6cbb-428d-86b2-c377726b4b5e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-27T22:25:09.191Z_

I now have the complete paper content. Let me also check for any information about inter-annotator agreement.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cfeca03-f38d-4e17-bcfb-96f050fa512a",
  "isSidechain": true,
  "agentId": "a91780e1d5a06a47f",
  "requestId": "req_011CbTriyShmNkF2bZb4Z4kt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b82770d2-107e-4331-98ea-b937b81e9bd1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EqqFwUenQdH9a2haTssC8x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25646,
      "cache_read_input_tokens": 18047,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25646,
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

_source line 35 · 2026-05-27T22:25:10.134Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013Spbm7uJ9Em2Go1Kd1uYuJ`</summary>

```json
{
  "query": "\"PathFinder-PRM\" inter-annotator agreement kappa annotation quality human evaluation error type reliability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b82770d2-107e-4331-98ea-b937b81e9bd1",
  "isSidechain": true,
  "agentId": "a91780e1d5a06a47f",
  "requestId": "req_011CbTriyShmNkF2bZb4Z4kt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12dc3410-7522-487c-847b-112855cc1e30",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EqqFwUenQdH9a2haTssC8x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25646,
      "cache_read_input_tokens": 18047,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25646,
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

_source line 36 · 2026-05-27T22:25:11.491Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WkS1WvHxxNm4gds4pzwur3`</summary>

```json
{
  "url": "https://huggingface.co/declare-lab/PathFinder-PRM-7B",
  "prompt": "Extract all technical details about the model: architecture, how error types are handled, any mention of annotation quality, inter-annotator agreement, model card details, limitations, and any other technical information."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12dc3410-7522-487c-847b-112855cc1e30",
  "isSidechain": true,
  "agentId": "a91780e1d5a06a47f",
  "requestId": "req_011CbTriyShmNkF2bZb4Z4kt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11983891-3b8e-416a-bb45-3f3c622760a9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EqqFwUenQdH9a2haTssC8x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25646,
      "cache_read_input_tokens": 18047,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25646,
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

_source line 37 · 2026-05-27T22:25:17.738Z_

<details><summary>↩ Tool result · `toolu_013Spbm7uJ9Em2Go1Kd1uYuJ`</summary>

```text
Web search results for query: ""PathFinder-PRM" inter-annotator agreement kappa annotation quality human evaluation error type reliability"

Links: [{"title":"Inter-Annotator Agreement: Building Datasets | Keymakr","url":"https://keymakr.com/blog/measuring-inter-annotator-agreement-building-trustworthy-datasets/"},{"title":"+ CS140 February 28, 2017 Inter annotator agreement","url":"https://www.cs.brandeis.edu/~cs140b/CS140b_slides/CS140_Lect_7_InterAnnotatorAgreement.pdf"},{"title":"Inter-annotator Agreement | OpenTrain Glossary","url":"https://www.opentrain.ai/glossary/inter-annotator-agreement/"},{"title":"Assessing Inter-Annotator Agreement for Medical Image Segmentation - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10062409/"},{"title":"Inter-Annotator Agreement: a key metric in Labeling","url":"https://www.innovatiana.com/en/post/inter-annotator-agreement"},{"title":"DiPietro-Hazari Kappa: A Novel Metric for Assessing Labeling Quality via   Annotation","url":"https://arxiv.org/pdf/2209.08243"},{"title":"Inter-Annotator Agreement: An Introduction to Cohen’s Kappa Statistic | by Surge AI | Medium","url":"https://surge-ai.medium.com/inter-annotator-agreement-an-introduction-to-cohens-kappa-statistic-dcc15ffa5ac4"}]

Based on my search results, I found information about inter-annotator agreement, kappa coefficients, and annotation quality evaluation. However, the search did not return specific results about "PathFinder-PRM" as a dataset or project.

Here's what I found regarding the general concepts in your query:

**Inter-Annotator Agreement and Kappa:**

Inter-annotator agreement is a statistical measure used to assess the degree to which different annotators give consistent labels or ratings to the same items within a dataset. Common statistical measures used to assess inter-annotator agreement include Cohen's Kappa, Fleiss' Kappa, and the Intraclass Correlation Coefficient, each suitable for different types of data and annotation scenarios.

**Annotation Quality and Reliability:**

High inter-annotator agreement indicates reliable, high-quality data, as it suggests that the labeling is clear and unambiguous, and that different human annotators interpret the data similarly. Low agreement may indicate issues with the data, the complexity of the task, or the clarity of the annotation guidelines.

**Error Analysis:**

By regularly checking the Inter Annotator Agreement, it is possible to identify trends and recurring problems in the evaluations and optimize the annotation process by implementing corrective measures over time to improve the reliability of dataset evaluations.

If you're looking for specific information about the PathFinder-PRM dataset or project, could you provide additional context about what this refers to? That might help me conduct a more targeted search.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12dc3410-7522-487c-847b-112855cc1e30",
  "isSidechain": true,
  "promptId": "11c0ed01-00cd-4aa6-94b3-6d386d5b1cba",
  "agentId": "a91780e1d5a06a47f",
  "type": "user",
  "uuid": "b41eb80d-94e3-4280-a3a1-9736e0f95ae1",
  "sourceToolAssistantUUID": "12dc3410-7522-487c-847b-112855cc1e30",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-27T22:25:25.102Z_

<details><summary>↩ Tool result · `toolu_01WkS1WvHxxNm4gds4pzwur3`</summary>

````text
# PathFinder-PRM-7B: Technical Details

## Model Architecture & Design

**Core Architecture:**
- **Type:** Hierarchical Discriminative Process Reward Model (PRM)
- **Base Model:** Qwen/Qwen2.5-Math-7B-Instruct (7B parameters)
- **Tensor Type:** BF16
- **Model Size:** 8B params

**Hierarchical Error Classification:**
The model breaks down error judgment into **two separate components**:
1. **Mathematical Correctness** - whether reasoning is mathematically valid
2. **Logical Consistency** - whether steps follow logically
3. **Final Decision** - combines both to determine if reasoning leads to correct solution

This is done through a **two-stage inference approach**:
- **Stage 1:** Evaluates math reasoning and consistency using mask tokens
- **Stage 2:** Predicts overall correctness based on Stage 1 results

## Training Data & Annotation

**Dataset Composition:**
- **PRM800K** - High-quality human annotated data
- **PathFinder-600K dataset** - Additional automatically annotated samples (~400K total samples used)
- Combined approach enables robustness to common failure patterns

**Note:** The page does not explicitly mention inter-annotator agreement metrics or specific annotation quality measurements.

## Technical Implementation Details

### Special Tokens
```python
pos_token_id = tokenizer.encode("<+>")[0]      # Positive prediction
neg_token_id = tokenizer.encode("<->")[0]      # Negative prediction
mask_token_id = tokenizer.encode("&lt;extra>")[0] # Mask for predictions
```

### Two-Forward-Pass Inference

**Stage 1 - Math & Consistency Evaluation:**
```python
# Detects &lt;extra> mask tokens and predicts <+> or <->
masked_logits = outputs.logits[shifted_mask][:, allowed_token_ids]
predicted_indices = masked_logits.argmax(dim=-1)

if '<->' in decoded_tokens:
    return -1  # Error found
```

**Stage 2 - Overall Correctness Scoring:**
```python
# Replaces mask tokens with predictions
# Adds "Correctness: &lt;extra>" to input
# Returns probability score via softmax
probs_pos_neg = F.softmax(restricted_logits, dim=-1)
return probs_pos_neg[0][0].cpu().item()  # Returns score [0-1]
```

## Evaluation Benchmarks

**Benchmarks Tested:**
- ProcessBench (GSM8K, MATH, Olympiad, OmniMath)
- PRMBench (Simplicity, Soundness, Sensitivity metrics)
- Reward-Guided Greedy Search with:
  - MATH500
  - AIME24
  - AMC23
  - Minerva Math
  - Olympiad Bench
  - College Math

## Performance Results

### PRMBench Overall Scores
| Model | Score |
|-------|-------|
| PathFinder-PRM-7B | **67.7** |
| Qwen2.5-Math-PRM-7B | 65.5 |
| ReasonEval-7B | 60.0 |

**Strengths:**
- Best "Simplicity" (58.9) - efficient error detection
- Best "Sensitivity" (76.9) - catches subtle errors
- Competitive "Soundness" (70.8)

### ProcessBench Results (Avg. F1)
| Model | Score |
|-------|-------|
| Qwen2.5-Math-PRM-7B | 73.5 (1.5M samples) |
| **PathFinder-PRM-7B** | **69.5** (~400K samples) |

### Reward-Guided Greedy Search (PRM@8)
| Metric | PathFinder-PRM-7B | Benchmark |
|--------|-------------------|-----------|
| Average | **48.3** | Best open-source |
| AIME24 | **20.0** | Best |
| College Math | **55.0** | Best |

## Limitations & Trade-offs

**Explicitly Stated:**
- Performs ~4 points lower than Qwen2.5-Math-PRM-7B on ProcessBench (which uses 3x more training data)
- Lower performance on Olympiad (36.5) and Minerva (36.7) in Reward-Guided Search compared to other benchmarks

**Implicit Limitations (not stated):**
- Model card does not explicitly detail failure modes or known limitations
- No inter-annotator agreement statistics provided
- No discussion of edge cases or failure patterns

## License & Resources

- **License:** MIT
- **Repository:** https://github.com/declare-lab/PathFinder-PRM
- **Paper:** https://arxiv.org/abs/2505.19706 (2505.19706)
- **Organization:** Deep Cognition and Language Research (DeCLaRe) Lab
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11983891-3b8e-416a-bb45-3f3c622760a9",
  "isSidechain": true,
  "promptId": "11c0ed01-00cd-4aa6-94b3-6d386d5b1cba",
  "agentId": "a91780e1d5a06a47f",
  "type": "user",
  "uuid": "6944c175-45fd-426e-a472-4268700254a9",
  "sourceToolAssistantUUID": "11983891-3b8e-416a-bb45-3f3c622760a9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-27T22:26:34.795Z_

I now have comprehensive information. Let me compile the detailed technical findings.

---

Here is my detailed technical analysis of PathFinder-PRM (arXiv 2505.19706):

---

## 1. Error Type Definitions

PathFinder-PRM defines exactly **two** error categories, plus a third "correctness/optimality" label:

**Math Errors:** Mistakes in arithmetic or algebraic manipulation, incorrect formula application, or invalid implications. This covers computational errors -- the step's *execution* is wrong even if the approach is sound.

**Consistency Errors:** Logical inconsistencies with the question, prior steps, or established constraints. This covers *coherence* violations -- the step contradicts something previously established or the problem statement itself.

**Correctness (Step Optimality):** The third dimension in their label vector captures whether a step is both error-free AND optimally contributes to solving the problem. This accounts for redundant statements, circular logic, ambiguity, and sub-optimal approaches.

Each step gets a three-dimensional binary vector: `c_t = (c_t^math, c_t^consistency, c_t^correctness)` where each component is in {0, 1}.

Important nuance from their annotation prompt (Appendix D): The LLM annotator (DeepSeek-R1-Distill-Qwen-32B) is instructed that "for incorrect steps, wherever possible, attempt to categorize the issue as violating **one of the three criterion** (i.e., assign score 0 to **only one category**). Assign multiple 0 scores only for serious errors." This means they deliberately push toward single-category attribution.

---

## 2. Training Mechanism -- This is Critical for Your Rebuttal

**No dual heads. No auxiliary loss. No separate classification heads.** This is a key architectural point.

They use **a single language modeling head** (the standard LM head of Qwen2.5-Math-7B-Instruct) and extend the tokenizer with three special tokens: `<+>` (positive), `<->` (negative), `&lt;extra>` (mask).

**Two-forward-pass design at inference (and mirrored during training):**

- **Pass 1:** Input is constructed as `[PRM Input], Math: &lt;mask>, Consistency: &lt;mask>`. The model predicts `<+>` or `<->` at both mask positions *simultaneously* in a single forward pass. The key design choice: Math and Consistency are predicted *independently* (not autoregressively) to prevent error cascading -- they explicitly state they want to avoid the Consistency prediction being influenced by the Math label.

- **Pass 2:** The predicted Math and Consistency labels are filled in, and a third mask is appended: `[PRM Input], Math: &lt;predicted_label>, Consistency: &lt;predicted_label>, Correctness: &lt;mask>`. The softmax probability of the `<+>` token at the Correctness mask position becomes the final reward score.

**Training objective:** Standard cross-entropy loss computed *only on the label tokens* (the masked positions). Each training example has two parts mirroring the two inference passes:
1. Error Detection Target: `Prompt + Math: <+>/<->, Consistency: <+>/<->`
2. Reward Estimation Target: `Prompt + Math: [label], Consistency: [label] + Correctness: <+>/<->`

**Training hyperparameters:** Qwen2.5-Math-7B-Instruct base, bfloat16, flash attention 2, batch size 2 per device, gradient accumulation 32, LR 1e-5, 4 epochs, cosine schedule, warmup ratio 0.1, DeepSpeed Zero-2.

**This is architecturally elegant but simple** -- there are no separate heads, no multi-task loss weighting, no embedding-based classifiers. It is all done through the language modeling objective with masked token prediction.

---

## 3. Results Breakdown -- Were Gains Over Strong Baselines?

### PRMBench (Overall PRMScore):
| Model | Score |
|---|---|
| **PathFinder-PRM-7B** | **67.7** |
| Qwen2.5-Math-PRM-7B (trained on ~1.5M samples) | 65.5 |
| ReasonEval-7B | 60.0 |
| Qwen2.5-Math-7B-PRM800K | 58.3 |
| RLHFlow-Mistral-8B | 54.4 |
| Math-Shepherd-7B | 47.0 |

The +2.2 gain over Qwen2.5-Math-PRM-7B is indeed over the **strongest discriminative PRM baseline**, which itself was trained on ~1.5M samples (3x more data). PathFinder-PRM also beat all LLM-as-judge models except Gemini-2.0-thinking-exp (68.8). So GPT-4o (66.8) and QwQ-Preview-32B (63.6) were beaten.

### prm@8 (Reward-Guided Greedy Search, avg across 6 benchmarks):
| Model | Avg |
|---|---|
| **PathFinder-PRM-7B** | **48.3** |
| PathFinder-PRM-7B-PRM800K | 46.9 |
| Qwen2.5-Math-PRM-7B | 46.8 |
| Skywork-PRM-7B | 44.9 |
| Math-PSA-7B | 44.5 |

The +1.5 gain (48.3 vs 46.8) is over Qwen2.5-Math-PRM-7B, which was the strongest baseline. This is a legitimate strong baseline -- it uses 3x more training data.

### ProcessBench (Avg F1):
| Model | Avg F1 |
|---|---|
| Qwen2.5-Math-PRM-7B (~1.5M samples) | 73.5 |
| **PathFinder-PRM-7B (~400K samples)** | **69.5** |
| PathFinder-PRM-7B-PRM800K | 65.2 |
| Qwen2.5-Math-7B-PRM800K | 58.5 |

On ProcessBench, they are actually 4 points *behind* Qwen2.5-Math-PRM-7B, but with 3x less data. Within the PRM800K-only category, their gain over the best baseline (Qwen2.5-Math-7B-PRM800K) is massive: +6.7 F1.

---

## 4. Inter-Annotator Agreement

**They did NOT report inter-annotator agreement.** There is no kappa score, no human agreement measurement anywhere in the paper or appendices. The error type labels for erroneous steps were generated entirely by DeepSeek-R1-Distill-Qwen-32B (an LLM), not human annotators. Their quality control was limited to **consistency filtering** -- removing labels that are logically incompatible with existing human/MC labels (e.g., filtering out cases where DeepSeek labels a step as (1,1,1) when the human label was -1).

**This is a significant gap you can exploit in your rebuttal.** Their error taxonomy is validated only indirectly through downstream task performance, not through any human agreement study on the error types themselves.

---

## 5. Ablation Results -- Detailed Breakdown

Two ablations were run:

### Ablation A: "w/o Separate Error Categories" (merge Math + Consistency into a single error detection step, but keep hierarchical structure)
- ProcessBench: 67.0 vs 69.5 full model (-2.5 F1)
- PRMBench: 67.3 vs 67.7 full model (-0.4 PRMScore, very small)
- prm@8: 45.4 vs 48.3 full model (**-2.9 points** -- the biggest ablation effect)

### Ablation B: "w/o Separate Subtask Prediction" (remove hierarchy entirely, predict correctness directly as traditional PRMs do)
- ProcessBench: 67.6 vs 69.5 full model (-1.9 F1)
- PRMBench: 64.9 vs 67.7 full model (-2.8 PRMScore)
- prm@8: 45.5 vs 48.3 full model (-2.8 points)

**Key takeaway for your rebuttal:** The separation into two error categories (Math vs Consistency) has a *modest* effect on diagnostic benchmarks (only -0.4 on PRMBench) but a larger effect on downstream reward-guided search (-2.9 on prm@8). The hierarchical structure itself (Ablation B) matters more for PRMBench (-2.8). So the *category decomposition* specifically is less validated on the fine-grained detection benchmark and more validated on the end-to-end task.

### Data Scaling Ablation (Appendix B):
Increasing RLHFlow Mistral data from 50K to 200K (total 550K) actually *hurt* performance slightly:
- ProcessBench: 69.5 -> 68.75
- PRMBench: 67.7 -> 67.4
- prm@8: 48.3 -> 47.5

This shows diminishing/negative returns from more weak-model data.

---

## 6. Limitations and Extension to More Categories

The paper's stated limitations are narrow:
- **Only 7B models tested** due to compute constraints.
- **No discussion of extending to more error categories.** This is a notable omission. They chose exactly two categories (Math, Consistency) without justifying why two is optimal or exploring finer-grained taxonomies.

**Implicit limitations you can highlight:**
1. **No inter-annotator agreement** -- the error taxonomy is not validated by humans.
2. **Text-only, math-only** -- no multimodal reasoning, no non-mathematical domains.
3. **LLM-generated labels** -- the three-dimensional labels for erroneous steps come entirely from DeepSeek-R1-Distill-Qwen-32B, creating a dependency on that model's judgment quality.
4. **Two-forward-pass cost** -- doubles inference compute per step.
5. **No analysis of error type confusion** -- they never report how often Math errors are mislabeled as Consistency errors or vice versa.
6. **Fixed binary taxonomy** -- their annotation prompt explicitly discourages multi-category errors ("assign score 0 to only one category"), which may oversimplify real error patterns.
7. **The modest ablation gain from category separation on PRMBench** (only -0.4) suggests the error typing itself may not be the primary driver of gains -- the hierarchical structure may matter more.

---

## Differentiation Points for Your Rebuttal

Based on this analysis, here are concrete angles to argue your multimodal extension is NOT incremental:

1. **Their error taxonomy is minimal and unvalidated** -- two categories with no human agreement study. A multimodal extension inherently requires new error categories (visual grounding errors, cross-modal consistency errors, spatial reasoning errors) that PathFinder-PRM's framework does not address.

2. **Their architecture is text-only by design** -- the two-forward-pass masked prediction scheme over `<+>/<->` tokens is tightly coupled to text-based reasoning chains. Extending to multimodal inputs requires fundamentally different design choices for how error signals are extracted from visual content.

3. **They never discuss extensibility** -- the paper contains no analysis of whether their approach generalizes to more categories, different domains, or different modalities. The data scaling ablation even shows fragility.

4. **The error type decomposition itself is a modest contributor** -- their own ablation shows only -0.4 on PRMBench from removing category separation. The hierarchical structure (error detection before reward) is the bigger contributor. If your work proposes novel hierarchical structures for multimodal settings, that is a distinct contribution.

5. **Their annotation pipeline is math-specific** -- the prompt template, the label definitions, and the filtering logic are all designed around mathematical text reasoning. Multimodal error types require entirely different annotation frameworks.

Sources:
- [PathFinder-PRM Paper (arXiv:2505.19706)](https://arxiv.org/abs/2505.19706)
- [PathFinder-PRM PDF](https://arxiv.org/pdf/2505.19706)
- [PathFinder-PRM GitHub Repository](https://github.com/declare-lab/PathFinder-PRM)
- [PathFinder-PRM-7B Model Card on HuggingFace](https://huggingface.co/declare-lab/PathFinder-PRM-7B)
- [HuggingFace Papers Page for 2505.19706](https://huggingface.co/papers/2505.19706)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6944c175-45fd-426e-a472-4268700254a9",
  "isSidechain": true,
  "agentId": "a91780e1d5a06a47f",
  "requestId": "req_011CbTrkSK1P51nrqzthEDyR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6c4c0154-2868-45ea-ac8d-4315618a21d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b0104aa9-f62f-48d7-93dc-722aa4bbc136",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fiv1UGPdSBKDupt1o569wr",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2218,
      "cache_read_input_tokens": 43693,
      "output_tokens": 3140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2218
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3140,
          "cache_read_input_tokens": 43693,
          "cache_creation_input_tokens": 2218,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2218,
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
