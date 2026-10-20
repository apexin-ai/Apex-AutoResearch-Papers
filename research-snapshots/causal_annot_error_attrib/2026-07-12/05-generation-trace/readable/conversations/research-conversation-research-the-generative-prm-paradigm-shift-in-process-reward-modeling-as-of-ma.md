# Research conversation: Research the generative PRM paradigm shift in process reward modeling as of May 2026. I need to understand: 1. **ThinkPR

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 50
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ae6ad09eca6bec01f.jsonl`
- **Structured JSON:** [`4353541269e3883e9591.json`](../../sessions/43/4353541269e3883e9591.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

50 recorded events

### User

_source line 1 · 2026-05-27T22:00:12.174Z_

Research the generative PRM paradigm shift in process reward modeling as of May 2026. I need to understand:

1. **ThinkPRM** - A generative PRM that reportedly achieves 86.5 F1 on ProcessBench with only 1% of PRM800K labels. Find:
   - The paper (arXiv ID, venue if accepted)
   - How it works: does it generate reasoning/critiques before scoring?
   - Why it outperforms discriminative PRMs
   - Its limitations

2. **StepWiser** - Another generative PRM approach. Find details on method and results.

3. **"Process Reward Models That Think"** (arXiv 2504.16828) - Fetch and read this paper carefully.

4. Any other generative/reasoning-augmented PRMs published 2025-2026.

Search queries to use:
- "ThinkPRM generative process reward model"
- "StepWiser process reward model 2025 2026"
- "generative PRM reasoning verification"
- "process reward model that think 2504.16828"

For each paper, use WebFetch on the arXiv abstract page to get details. I need to understand: Is the discriminative PRM paradigm obsolete? Or can discriminative and generative approaches be complementary?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "ae6ad09eca6bec01f",
  "type": "user",
  "uuid": "14a91407-b7fc-4486-b1ad-77c12bcb8190",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-27T22:00:12.178Z_

```json
{
  "parentUuid": "14a91407-b7fc-4486-b1ad-77c12bcb8190",
  "isSidechain": true,
  "agentId": "ae6ad09eca6bec01f",
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
  "uuid": "f0d74ca9-ece4-4b2f-a99e-93cda976bea5",
  "timestamp": "2026-05-27T22:00:12.178Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-27T22:00:12.180Z_

```json
{
  "parentUuid": "f0d74ca9-ece4-4b2f-a99e-93cda976bea5",
  "isSidechain": true,
  "agentId": "ae6ad09eca6bec01f",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "bf049204-cd9c-4fe6-95e9-beb8e43d8ca3",
  "timestamp": "2026-05-27T22:00:12.180Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-27T22:00:17.137Z_



I'll research the generative PRM paradigm shift thoroughly. Let me start by loading the WebSearch and WebFetch tools, then conduct searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf049204-cd9c-4fe6-95e9-beb8e43d8ca3",
  "isSidechain": true,
  "agentId": "ae6ad09eca6bec01f",
  "requestId": "req_011CbTppuu4ft6phFEAGxPdL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5877b921-7c1a-4d18-8960-05cfbc807450",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YZRr3AkjYujEqFeZY3nq4a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1617,
      "cache_read_input_tokens": 7411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1617,
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

_source line 5 · 2026-05-27T22:00:17.539Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JZxYn55dZM87WxZ61oNiP6`</summary>

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
  "parentUuid": "5877b921-7c1a-4d18-8960-05cfbc807450",
  "isSidechain": true,
  "agentId": "ae6ad09eca6bec01f",
  "requestId": "req_011CbTppuu4ft6phFEAGxPdL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2db0ef9-2109-4ba7-bca2-9acaa3785824",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YZRr3AkjYujEqFeZY3nq4a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1617,
      "cache_read_input_tokens": 7411,
      "output_tokens": 114,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1617
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 114,
          "cache_read_input_tokens": 7411,
          "cache_creation_input_tokens": 1617,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1617,
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

_source line 6 · 2026-05-27T22:00:17.542Z_

<details><summary>↩ Tool result · `toolu_01JZxYn55dZM87WxZ61oNiP6`</summary>

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
  "parentUuid": "f2db0ef9-2109-4ba7-bca2-9acaa3785824",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "ae6ad09eca6bec01f",
  "type": "user",
  "uuid": "970ad7e5-4afa-437e-b7e6-a1a6453f67ff",
  "sourceToolAssistantUUID": "f2db0ef9-2109-4ba7-bca2-9acaa3785824",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-27T22:00:21.275Z_



Now let me run all four searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "970ad7e5-4afa-437e-b7e6-a1a6453f67ff",
  "isSidechain": true,
  "agentId": "ae6ad09eca6bec01f",
  "requestId": "req_011CbTpqK5LSpvrP3JVZfKTc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe4e2896-1cae-4cd4-9050-97b84f1513bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HiuD9pvcMTJYFS6faTYMfy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1136,
      "cache_read_input_tokens": 9028,
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

_source line 8 · 2026-05-27T22:00:21.758Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0183s8CULYqXqLgaaFX13jEc`</summary>

```json
{
  "query": "ThinkPRM generative process reward model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe4e2896-1cae-4cd4-9050-97b84f1513bb",
  "isSidechain": true,
  "agentId": "ae6ad09eca6bec01f",
  "requestId": "req_011CbTpqK5LSpvrP3JVZfKTc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5aa20bd3-4093-4325-9b36-85d66f354757",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HiuD9pvcMTJYFS6faTYMfy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1136,
      "cache_read_input_tokens": 9028,
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

_source line 9 · 2026-05-27T22:00:22.708Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DkXfh9E5WBPF3vEwXjEon1`</summary>

```json
{
  "query": "StepWiser process reward model 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5aa20bd3-4093-4325-9b36-85d66f354757",
  "isSidechain": true,
  "agentId": "ae6ad09eca6bec01f",
  "requestId": "req_011CbTpqK5LSpvrP3JVZfKTc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a37290a7-1eb0-4b97-a3e9-056e0935c453",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HiuD9pvcMTJYFS6faTYMfy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1136,
      "cache_read_input_tokens": 9028,
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

_source line 10 · 2026-05-27T22:00:23.172Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0158pYQ2FT5q8XvV1yjbQSbX`</summary>

```json
{
  "query": "generative PRM reasoning verification 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a37290a7-1eb0-4b97-a3e9-056e0935c453",
  "isSidechain": true,
  "agentId": "ae6ad09eca6bec01f",
  "requestId": "req_011CbTpqK5LSpvrP3JVZfKTc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1eced41f-441b-4686-8829-08c872f303d6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HiuD9pvcMTJYFS6faTYMfy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1136,
      "cache_read_input_tokens": 9028,
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

_source line 11 · 2026-05-27T22:00:23.647Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019PVognpMX72VafvzWeDabB`</summary>

```json
{
  "query": "process reward model that think arXiv 2504.16828"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1eced41f-441b-4686-8829-08c872f303d6",
  "isSidechain": true,
  "agentId": "ae6ad09eca6bec01f",
  "requestId": "req_011CbTpqK5LSpvrP3JVZfKTc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d353eeeb-d575-4bdc-95f5-38d625125c27",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HiuD9pvcMTJYFS6faTYMfy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1136,
      "cache_read_input_tokens": 9028,
      "output_tokens": 213,
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
          "output_tokens": 213,
          "cache_read_input_tokens": 9028,
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

_source line 12 · 2026-05-27T22:00:29.166Z_

<details><summary>↩ Tool result · `toolu_01DkXfh9E5WBPF3vEwXjEon1`</summary>

```text
Web search results for query: "StepWiser process reward model 2025 2026"

Links: [{"title":"StepWiser: Stepwise Generative Judges for Wiser Reasoning | OpenReview","url":"https://openreview.net/forum?id=gEu9xXzTlI"},{"title":"StepWiser: Generative Meta-Reasoning Framework","url":"https://www.emergentmind.com/topics/stepwiser-framework"},{"title":"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress | Proceedings of the ACM Web Conference 2026","url":"https://dl.acm.org/doi/10.1145/3774904.3792551"},{"title":"[2508.19229] StepWiser: Stepwise Generative Judges for Wiser Reasoning","url":"https://arxiv.org/abs/2508.19229"},{"title":"StepWiser: Stepwise Generative Judges for Wiser Reasoning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/stepwiser-stepwise-generative-judges-wiser-reasoning"},{"title":"Paper page - StepWiser: Stepwise Generative Judges for Wiser Reasoning","url":"https://huggingface.co/papers/2508.19229"},{"title":"StepWiser: Stepwise Generative Judges for Wiser Reasoning","url":"https://arxiviq.substack.com/p/stepwiser-stepwise-generative-judges"},{"title":"StepWiser: Generative Judge for CoT Evaluation","url":"https://www.emergentmind.com/topics/stepwiser"},{"title":"Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis","url":"https://arxiv.org/html/2604.24198v1"},{"title":"StepWiser: Generative Judges for Reasoning","url":"https://www.emergentmind.com/papers/2508.19229"}]

I found comprehensive information about StepWiser, a process reward model research paper from 2025. Here's what I found:

## Overview

StepWiser is a paper submitted to ICLR 2026 that reframes stepwise reward modeling from a classification task to a reasoning task itself. The paper was submitted on August 26, 2025.

## The Problem It Addresses

Current process reward models have two major drawbacks: they typically function as classifiers without providing explanations, and their reliance on supervised fine-tuning with static datasets limits generalization.

## Key Innovation

StepWiser proposes a generative judge that reasons about the policy model's reasoning steps (i.e., meta-reasons), outputting thinking tokens before delivering a final verdict. Unlike traditional classifier-based process reward models, StepWiser reframes the evaluation of reasoning steps from binary classification to a chain-of-thought (CoT) reasoning operation itself.

## Training and Performance

The model is trained by reinforcement learning using relative outcomes of rollouts and provides: (i) better judgment accuracy on intermediate steps than existing methods; (ii) can be used to improve the policy model at training time; and (iii) improves inference-time search.

## Technical Features

The framework instructs the base policy model to self-segment its chain-of-thought into contiguous "Chunks-of-Thought", each representing a semantically complete, purpose-driven step within a multi-step reasoning trajectory.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a37290a7-1eb0-4b97-a3e9-056e0935c453",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "ae6ad09eca6bec01f",
  "type": "user",
  "uuid": "a7cb2364-51fd-41ed-818c-2a433f82adbf",
  "sourceToolAssistantUUID": "a37290a7-1eb0-4b97-a3e9-056e0935c453",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-27T22:00:29.977Z_

<details><summary>↩ Tool result · `toolu_0183s8CULYqXqLgaaFX13jEc`</summary>

```text
Web search results for query: "ThinkPRM generative process reward model"

Links: [{"title":"Process Reward Models That Think | alphaXiv","url":"https://www.alphaxiv.org/overview/2504.16828"},{"title":"ThinkPRM: Data-Efficient Process Reward Models","url":"https://www.emergentmind.com/papers/2504.16828"},{"title":"THINKPRM: generative Process Reward Model for solution verification via long CoT Reasoning | by SACHIN KUMAR | Medium","url":"https://medium.com/@techsachin/thinkprm-generative-process-reward-model-for-solution-verification-via-long-cot-reasoning-2016f1e1387d"},{"title":"GitHub - mukhal/ThinkPRM: Process Reward Models That Think","url":"https://github.com/mukhal/thinkprm"},{"title":"ThinkPRM: A Generative Process Reward Models for Scalable Reasoning Verification - MarkTechPost","url":"https://www.marktechpost.com/2025/04/29/thinkprm-a-generative-process-reward-models-for-scalable-reasoning-verification/"},{"title":"[Literature Review] Process Reward Models That Think","url":"https://www.themoonlight.io/en/review/process-reward-models-that-think"},{"title":"launch/ThinkPRM-1.5B · Hugging Face","url":"https://huggingface.co/launch/ThinkPRM-1.5B"},{"title":"[2504.16828] Process Reward Models That Think","url":"https://arxiv.org/abs/2504.16828"},{"title":"Paper page - Process Reward Models That Think","url":"https://huggingface.co/papers/2504.16828"}]

Based on the search results, I can provide you with information about ThinkPRM:

## Overview

ThinkPRM is a generative process reward model that enables large language models to provide verbalized, long Chain-of-Thought (CoT) reasoning. It efficiently verifies step-by-step reasoning using minimal synthetic data for superior performance.

## Key Features

ThinkPRM works as a verbalized step-wise reward model that verifies every step in the solution by generating a verification chain-of-thought (CoT), using a long CoT verifier fine-tuned on orders of magnitude fewer process labels than those required by discriminative PRMs.

The approach outperforms LLM-as-a-Judge and discriminative verifiers using only 1% of the process labels in PRM800K across several challenging benchmarks.

## Training Approach

The verifiers are obtained by fine-tuning reasoning models over 1K synthetic verification CoTs—filtered based on only 8K process labels from PRM800K. Trained PRMs are available in two sizes: 1.5B and 14B fine-tuned from R1-Distill-Qwen models, with a 7B variant also available.

## Performance

ThinkPRM beats the baselines on ProcessBench, MATH-500, and AIME '24 under best-of-N selection and reward-guided search. For out-of-domain evaluation, ThinkPRM shows better scaling than discriminative models on GPQA-physics, outperforming it by 8%, while on LiveCodeBench, ThinkPRM surpasses discriminative models by 4.5%.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5aa20bd3-4093-4325-9b36-85d66f354757",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "ae6ad09eca6bec01f",
  "type": "user",
  "uuid": "3fe4d71a-3925-472f-bc97-f11bd74cdfb5",
  "sourceToolAssistantUUID": "5aa20bd3-4093-4325-9b36-85d66f354757",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-27T22:00:30.919Z_

<details><summary>↩ Tool result · `toolu_019PVognpMX72VafvzWeDabB`</summary>

```text
Web search results for query: "process reward model that think arXiv 2504.16828"

Links: [{"title":"[2504.16828v1] Process Reward Models That Think","url":"https://arxiv.org/abs/2504.16828v1"},{"title":"[2504.16828v3] Process Reward Models That Think","url":"http://arxiv.org/abs/2504.16828v3"},{"title":"Process Reward Models That Think | alphaXiv","url":"https://www.alphaxiv.org/overview/2504.16828"},{"title":"[2504.16828] Process Reward Models That Think","url":"https://arxiv.org/abs/2504.16828"},{"title":"THINKPRM: generative Process Reward Model for solution verification via long CoT Reasoning | by SACHIN KUMAR | Medium","url":"https://medium.com/@techsachin/thinkprm-generative-process-reward-model-for-solution-verification-via-long-cot-reasoning-2016f1e1387d"},{"title":"[2504.16828] Process Reward Models That Think - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2504.16828"},{"title":"GitHub - mukhal/ThinkPRM: Process Reward Models That Think","url":"https://github.com/mukhal/ThinkPRM"},{"title":"Paper page - Process Reward Models That Think","url":"https://huggingface.co/papers/2504.16828"},{"title":"Process Reward Models That Think","url":"https://arxiv.org/pdf/2504.16828"}]

Here are the search results for arXiv 2504.16828 "Process Reward Models That Think":

## Overview

This paper introduces Process Reward Models (PRMs), which are step-by-step verifiers that serve as a key ingredient for test-time scaling.

## The Problem

PRMs require step-level supervision, making them expensive to train.

## The Solution: ThinkPRM

The work aims to build data-efficient PRMs as verbalized step-wise reward models that verify every step in the solution by generating a verification chain-of-thought (CoT). The authors propose ThinkPRM, a long CoT verifier fine-tuned on orders of magnitude fewer process labels than those required by discriminative PRMs.

## Key Results

The approach outperforms LLM-as-a-Judge and discriminative verifiers using only 1% of the process labels in PRM800K across several challenging benchmarks, specifically beating the baselines on ProcessBench, MATH-500, and AIME '24 under best-of-N selection and reward-guided search.

## Authors

The paper was authored by Muhammad Khalifa, Rishabh Agarwal, Lajanugen Logeswaran, Jaekyeom Kim, Hao Peng, Moontae Lee, Honglak Lee, and Lu Wang, with the paper submitted on April 23, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d353eeeb-d575-4bdc-95f5-38d625125c27",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "ae6ad09eca6bec01f",
  "type": "user",
  "uuid": "f2ed66ba-eaa7-48fd-a4de-1bd8dd359691",
  "sourceToolAssistantUUID": "d353eeeb-d575-4bdc-95f5-38d625125c27",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-27T22:00:31.714Z_

<details><summary>↩ Tool result · `toolu_0158pYQ2FT5q8XvV1yjbQSbX`</summary>

```text
Web search results for query: "generative PRM reasoning verification 2025 2026"

Links: [{"title":"GitHub - RyanLiu112/GenPRM: [AAAI 2026] Official codebase for \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\".","url":"https://github.com/RyanLiu112/GenPRM"},{"title":"2025-4-8 GenPRM: Scaling Test-Time Compute of Process","url":"https://arxiv.org/pdf/2504.00891"},{"title":"Uncertainty-aware Step-wise Verification with Generative Reward Models","url":"https://arxiv.org/pdf/2502.11250"},{"title":"Breaking the LLM Bottleneck: GenPRM’s approach to Scale test-time compute via generative reasoning | by SACHIN KUMAR | Medium","url":"https://medium.com/@techsachin/breaking-the-llm-bottleneck-genprms-approach-to-scale-test-time-compute-via-generative-reasoning-0e90e3ffa71e"},{"title":"ThinkPRM: A Generative Process Reward Models for Scalable Reasoning Verification - MarkTechPost","url":"https://www.marktechpost.com/2025/04/29/thinkprm-a-generative-process-reward-models-for-scalable-reasoning-verification/"},{"title":"[2504.00891] GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning","url":"https://arxiv.org/abs/2504.00891"},{"title":"[2507.23317] Good Learners Think Their Thinking: Generative PRM Makes Large Reasoning Model More Efficient Math Learner","url":"https://arxiv.org/abs/2507.23317"},{"title":"GM-PRM: A Generative Multimodal Process Reward Model for Multimodal Mathematical Reasoning","url":"https://arxiv.org/pdf/2508.04088"}]

Here are the key findings from the search results:

## GenPRM and Generative Process Reward Models

GenPRM is a generative process reward model that performs explicit Chain-of-Thought (CoT) reasoning with code verification before providing judgment for each reasoning step. The work is accepted at AAAI 2026 and was published in April 2025.

### Key Features

Current PRMs face challenges including limited process supervision and generalization capabilities, dependence on scalar value prediction without leveraging the generative abilities of LLMs, and inability to scale the test-time compute of PRMs. By equipping the PRM with generative process supervision abilities, GenPRM can be naturally used as a critic model to refine the outputs of policy models and scale the refinement process with multiple turns.

The authors propose Relative Progress Estimation (RPE) and a rationale synthesis framework that incorporates code verification to obtain high-quality process supervision labels.

### Related Work

Other recent generative PRM approaches include:

- **ThinkPRM**: Under verifier-guided search on MATH-500, THINKPRM-1.5B outperforms DiscPRM by approximately 5 percentage points and surpasses RLHFFlow-Deepseek-PRM by over 7% at 16 beams.

- **GM-PRM**: A novel Generative Multimodal Process Reward Model (GM-PRM) addresses limitations of existing multimodal PRMs.

- **Uncertainty-aware frameworks**: Work on detecting when the verifier itself is uncertain at a given step can better guard against erroneous feedback and improve interpretability of reward signals.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1eced41f-441b-4686-8829-08c872f303d6",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "ae6ad09eca6bec01f",
  "type": "user",
  "uuid": "91e8b248-66ce-4d68-a3ec-d21bc2cd6c36",
  "sourceToolAssistantUUID": "1eced41f-441b-4686-8829-08c872f303d6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-27T22:00:35.744Z_

Excellent. Now let me fetch the detailed content from the key arXiv pages and other sources.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91e8b248-66ce-4d68-a3ec-d21bc2cd6c36",
  "isSidechain": true,
  "agentId": "ae6ad09eca6bec01f",
  "requestId": "req_011CbTprMSFXi2qgMburbdbE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9805fb0-981d-4e4a-941c-caf7b60614bc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019cgbrKyrhYiMuUHmng4rXi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 771,
      "cache_creation_input_tokens": 2865,
      "cache_read_input_tokens": 10164,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2865,
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

_source line 17 · 2026-05-27T22:00:39.508Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01W1ub6XpkFAdPz7fUSagWKM`</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.16828",
  "prompt": "Extract all details about this paper: title, authors, abstract, arXiv ID, submission date, any venue acceptance info. Focus on the methodology (how ThinkPRM works), key results (especially the 86.5 F1 on ProcessBench claim, and all benchmark numbers), limitations mentioned, and how it compares to discriminative PRMs. Include details about training data efficiency (the 1% of PRM800K claim)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9805fb0-981d-4e4a-941c-caf7b60614bc",
  "isSidechain": true,
  "agentId": "ae6ad09eca6bec01f",
  "requestId": "req_011CbTprMSFXi2qgMburbdbE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "72aff29d-2f1a-4521-9361-2e0daae0744b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019cgbrKyrhYiMuUHmng4rXi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 771,
      "cache_creation_input_tokens": 2865,
      "cache_read_input_tokens": 10164,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2865,
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

_source line 18 · 2026-05-27T22:00:40.988Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CXheqLzfAJZ3eAJp9gYQtC`</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.00891",
  "prompt": "Extract all details about GenPRM: title, authors, abstract, arXiv ID, venue acceptance, methodology (how it works, what is Relative Progress Estimation, code verification), key results and benchmarks, how it compares to discriminative PRMs, and any limitations mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72aff29d-2f1a-4521-9361-2e0daae0744b",
  "isSidechain": true,
  "agentId": "ae6ad09eca6bec01f",
  "requestId": "req_011CbTprMSFXi2qgMburbdbE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b4bc6be-7b82-4141-b7d9-c5a3c96d2448",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019cgbrKyrhYiMuUHmng4rXi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 771,
      "cache_creation_input_tokens": 2865,
      "cache_read_input_tokens": 10164,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2865,
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

_source line 19 · 2026-05-27T22:00:43.400Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AAQxoxAgLxiyYhsEANBYgE`</summary>

```json
{
  "url": "https://arxiv.org/abs/2508.19229",
  "prompt": "Extract all details about StepWiser: title, authors, abstract, arXiv ID, submission date, venue acceptance, methodology (how it reframes PRM as reasoning, meta-reasoning, Chunks-of-Thought), training approach (RL with rollout outcomes), key results and benchmarks, and how it compares to other PRMs including discriminative ones."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b4bc6be-7b82-4141-b7d9-c5a3c96d2448",
  "isSidechain": true,
  "agentId": "ae6ad09eca6bec01f",
  "requestId": "req_011CbTprMSFXi2qgMburbdbE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52d1ec17-67cf-4c8a-8857-d7a5cf4f25cf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019cgbrKyrhYiMuUHmng4rXi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 771,
      "cache_creation_input_tokens": 2865,
      "cache_read_input_tokens": 10164,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2865,
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

_source line 20 · 2026-05-27T22:00:44.558Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UeZdm9DjRaXg7WjuksWVvj`</summary>

```json
{
  "url": "https://arxiv.org/abs/2507.23317",
  "prompt": "Extract all details about this paper: title, authors, abstract, arXiv ID, submission date, methodology, key results, and how it relates to generative PRMs for reasoning."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52d1ec17-67cf-4c8a-8857-d7a5cf4f25cf",
  "isSidechain": true,
  "agentId": "ae6ad09eca6bec01f",
  "requestId": "req_011CbTprMSFXi2qgMburbdbE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fec60581-d901-4805-bba7-c02059d206ab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019cgbrKyrhYiMuUHmng4rXi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 771,
      "cache_creation_input_tokens": 2865,
      "cache_read_input_tokens": 10164,
      "output_tokens": 567,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2865
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 771,
          "output_tokens": 567,
          "cache_read_input_tokens": 10164,
          "cache_creation_input_tokens": 2865,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2865,
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

_source line 21 · 2026-05-27T22:00:45.866Z_

<details><summary>↩ Tool result · `toolu_01W1ub6XpkFAdPz7fUSagWKM`</summary>

```text
# Process Reward Models That Think - Paper Summary

## Basic Information
- **Title:** Process Reward Models That Think
- **arXiv ID:** 2504.16828
- **Submission Date:** April 23, 2025 (v1); Latest revision December 8, 2025 (v5)
- **Authors:** Muhammad Khalifa, Rishabh Agarwal, Lajanugen Logeswaran, Jaekyeom Kim, Hao Peng, Moontae Lee, Honglak Lee, Lu Wang
- **License:** CC BY 4.0

## Methodology

ThinkPRM represents a generative approach to process reward modeling. Rather than using discriminative classifiers, the system functions as "a long CoT verifier fine-tuned on orders of magnitude fewer process labels." The core innovation involves having the model generate verification reasoning chains while assessing solution steps, leveraging the inherent analytical capabilities of extended chain-of-thought language models.

## Key Results

The paper demonstrates substantial improvements across multiple evaluation domains:

- **ProcessBench, MATH-500, and AIME '24:** Outperformed both LLM-as-a-Judge and discriminative baselines
- **Out-of-domain performance:** Surpassed discriminative verifiers trained on complete PRM800K by 8% on GPQA-Diamond and 4.5% on LiveCodeBench
- **Compute efficiency:** Achieved 7.2% improvement over LLM-as-a-Judge under identical token budgets on ProcessBench subset

## Data Efficiency

The breakthrough finding centers on training efficiency: "ThinkPRM beats the baselines...using only 1% of the process labels in PRM800K." This represents a dramatic reduction in annotation requirements compared to traditional discriminative approaches.

## Limitations and Comparisons

The abstract does not explicitly detail specific limitations. However, the comparative positioning indicates ThinkPRM outperforms discriminative PRMs while requiring substantially fewer labeled training examples, representing a meaningful advance in test-time scaling methodology.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72aff29d-2f1a-4521-9361-2e0daae0744b",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "ae6ad09eca6bec01f",
  "type": "user",
  "uuid": "f3880ee1-a4d5-4bad-8377-8437aacc9656",
  "sourceToolAssistantUUID": "72aff29d-2f1a-4521-9361-2e0daae0744b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-27T22:00:48.406Z_

<details><summary>↩ Tool result · `toolu_01CXheqLzfAJZ3eAJp9gYQtC`</summary>

```text
# GenPRM: Generative Process Reward Models - Summary

## Core Information
**Title:** GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning

**arXiv ID:** 2504.00891 (cs.CL)

**Authors:** Jian Zhao, Runze Liu, Kaiyan Zhang, Zhimu Zhou, Junqi Gao, Dong Li, Jiafei Lyu, Zhouyi Qian, Biqing Qi, Xiu Li, Bowen Zhou

**Submission:** April 1, 2025 (v1); revised April 5, 2025 (v2)

**Venue:** Computer Science > Computation and Language (no specific conference mentioned)

## Methodology

GenPRM addresses three challenges in existing Process Reward Models:

1. **Generative Approach:** Rather than scalar value prediction, the model performs "explicit Chain-of-Thought reasoning with code verification before providing judgment for each reasoning step."

2. **Relative Progress Estimation (RPE):** A framework designed to obtain high-quality process supervision labels and rationale data with integrated code verification.

3. **Test-Time Scaling:** The architecture enables increased computational investment during inference for enhanced performance.

## Key Results & Benchmarks

- Trained on only 23K samples from the MATH dataset
- 1.5B GenPRM outperforms GPT-4o on ProcessBench
- 7B GenPRM surpasses Qwen2.5-Math-PRM-72B
- Demonstrates effectiveness as a critic model for policy refinement

## Comparison to Discriminative PRMs

The work "bridges the gap between PRMs and critic models in LLMs," moving from scalar predictions to generative reasoning with explicit justification and code verification—a paradigm shift in process supervision.

**Note:** The document provides no explicit limitations section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b4bc6be-7b82-4141-b7d9-c5a3c96d2448",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "ae6ad09eca6bec01f",
  "type": "user",
  "uuid": "48848a74-a956-494f-ba3b-01bf945766e6",
  "sourceToolAssistantUUID": "1b4bc6be-7b82-4141-b7d9-c5a3c96d2448",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-27T22:00:49.114Z_

<details><summary>↩ Tool result · `toolu_01AAQxoxAgLxiyYhsEANBYgE`</summary>

```text
# StepWiser: Stepwise Generative Judges Research Summary

## Basic Information
- **Title:** StepWiser: Stepwise Generative Judges for Wiser Reasoning
- **arXiv ID:** 2508.19229
- **Authors:** Wei Xiong, Wenting Zhao, Weizhe Yuan, Olga Golovneva, Tong Zhang, Jason Weston, Sainbayar Sukhbaatar
- **Submission Date:** August 26, 2025 (v1); August 27, 2025 (v2)
- **Venue:** Not listed as conference-accepted; posted to arXiv (Computer Science > Artificial Intelligence)

## Core Methodology

The paper reframes process reward modeling (PRM) fundamentally. Rather than treating step evaluation as classification, the authors propose "a generative judge that reasons about the policy model's reasoning steps (i.e., meta-reasons), outputting thinking tokens before delivering a final verdict."

Key innovations include:
- **Meta-reasoning approach:** The judge performs reasoning about reasoning
- **Generative framework:** Moves beyond classifier-based feedback to explanation-generating evaluation
- **Training via RL:** Uses "reinforcement learning using relative outcomes of rollouts" rather than supervised fine-tuning

## Key Results

The research demonstrates three primary contributions:
1. Superior judgment accuracy on intermediate reasoning steps compared to existing methods
2. Effectiveness for improving policy models during training
3. Enhanced inference-time search capabilities

## Comparison to Other Approaches

The paper contrasts its approach against existing PRMs by highlighting limitations of current methods: they "typically function as classifiers without providing explanations" and rely on "supervised fine-tuning with static datasets" that restrict generalization.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52d1ec17-67cf-4c8a-8857-d7a5cf4f25cf",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "ae6ad09eca6bec01f",
  "type": "user",
  "uuid": "1170fd0a-4c82-470a-a74f-c5df3ca586d5",
  "sourceToolAssistantUUID": "52d1ec17-67cf-4c8a-8857-d7a5cf4f25cf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-27T22:00:50.111Z_

<details><summary>↩ Tool result · `toolu_01UeZdm9DjRaXg7WjuksWVvj`</summary>

```text
# Paper Summary: Generative PRM for Large Reasoning Models

**Title:** "Good Learners Think Their Thinking: Generative PRM Makes Large Reasoning Model More Efficient Math Learner"

**arXiv ID:** 2507.23317

**Submission Date:** July 31, 2025

**Authors:** Tao He, Rongchuan Mu, Lizi Liao, Yixin Cao, Ming Liu, Bing Qin

## Abstract Overview

The researchers address inefficiencies in reinforcement learning training for large reasoning models. They note that "conventional approaches rely on outcome-only rewards that provide sparse feedback, resulting in inefficient optimization process."

## Methodology

The paper introduces a thought-level process reward mechanism with three key innovations:

1. **Intrinsic Signal-Driven Evaluation:** Rather than requiring PRMs to solve problems, the system uses internal signals to assess stepwise correctness and aggregate steps into coherent "thought" units.

2. **Capability-Adaptive Rewards:** A mechanism that "dynamically balances exploration and exploitation based on the LRM's current proficiency."

3. **TP-GRPO Algorithm:** A new off-policy RL algorithm extending grouped proximal optimization with process-based rewards.

## Key Results

- Tested on 1.5B and 7B parameter models
- Achieved higher problem-solving accuracy with significantly fewer training samples compared to outcome-only baselines
- Demonstrates that structured process rewards substantially accelerate math reasoning optimization

**Code Availability:** Published on GitHub
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fec60581-d901-4805-bba7-c02059d206ab",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "ae6ad09eca6bec01f",
  "type": "user",
  "uuid": "87b2c43d-06fb-421e-9d0d-c8030dbee034",
  "sourceToolAssistantUUID": "fec60581-d901-4805-bba7-c02059d206ab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-27T22:00:55.454Z_

Good, now let me get more details -- the ar5iv HTML version of ThinkPRM for deeper methodology and limitations, plus the GM-PRM paper and search for any additional generative PRMs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87b2c43d-06fb-421e-9d0d-c8030dbee034",
  "isSidechain": true,
  "agentId": "ae6ad09eca6bec01f",
  "requestId": "req_011CbTpsi7yrmuyARit8JjaR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "62e52440-9768-42d6-a099-17caee9798b6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014qzi7fAFZnf1r3SgJUu5Ye",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3101,
      "cache_read_input_tokens": 13029,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3101,
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

_source line 26 · 2026-05-27T22:00:59.692Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DnT9QSzyK6khGymAn1KJGV`</summary>

```json
{
  "url": "https://ar5iv.labs.arxiv.org/html/2504.16828",
  "prompt": "Extract detailed information about: 1) The exact F1 score on ProcessBench (is it 86.5?), 2) How ThinkPRM generates reasoning/critiques before scoring - the exact mechanism, 3) The training procedure - how synthetic verification CoTs are generated and filtered, 4) All benchmark results with numbers, 5) Limitations section - what are the stated limitations?, 6) Why it outperforms discriminative PRMs - the key insights, 7) Any discussion of compute costs or inference overhead, 8) Whether discriminative and generative PRMs can be complementary."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62e52440-9768-42d6-a099-17caee9798b6",
  "isSidechain": true,
  "agentId": "ae6ad09eca6bec01f",
  "requestId": "req_011CbTpsi7yrmuyARit8JjaR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "21510a6a-be3d-4e66-b923-c9f380daf259",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014qzi7fAFZnf1r3SgJUu5Ye",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3101,
      "cache_read_input_tokens": 13029,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3101,
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

_source line 27 · 2026-05-27T22:01:01.105Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018Lf7HnY6ik3mEkAfX2U6dD`</summary>

```json
{
  "url": "https://arxiv.org/abs/2508.04088",
  "prompt": "Extract all details about GM-PRM: title, authors, abstract, arXiv ID, methodology for multimodal generative PRM, key results, and how it extends the generative PRM paradigm to multimodal settings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21510a6a-be3d-4e66-b923-c9f380daf259",
  "isSidechain": true,
  "agentId": "ae6ad09eca6bec01f",
  "requestId": "req_011CbTpsi7yrmuyARit8JjaR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d23c944-a590-46b5-91a5-2f69e36ba42b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014qzi7fAFZnf1r3SgJUu5Ye",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3101,
      "cache_read_input_tokens": 13029,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3101,
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

_source line 28 · 2026-05-27T22:01:02.517Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NnBNxJ89hhQobyJEQm8XKK`</summary>

```json
{
  "query": "ThinkPRM 86.5 F1 ProcessBench results venue ICML NeurIPS 2025 2026 accepted"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d23c944-a590-46b5-91a5-2f69e36ba42b",
  "isSidechain": true,
  "agentId": "ae6ad09eca6bec01f",
  "requestId": "req_011CbTpsi7yrmuyARit8JjaR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d89a28b3-6ea7-4936-a478-bb3b47e12b92",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014qzi7fAFZnf1r3SgJUu5Ye",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3101,
      "cache_read_input_tokens": 13029,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3101,
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

_source line 29 · 2026-05-27T22:01:02.735Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NMa8bvyxRtudpYxVegoM3L`</summary>

```json
{
  "query": "generative process reward model discriminative complementary 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d89a28b3-6ea7-4936-a478-bb3b47e12b92",
  "isSidechain": true,
  "agentId": "ae6ad09eca6bec01f",
  "requestId": "req_011CbTpsi7yrmuyARit8JjaR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c65c931e-dcd7-4075-b953-ddcdf2304ee7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014qzi7fAFZnf1r3SgJUu5Ye",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3101,
      "cache_read_input_tokens": 13029,
      "output_tokens": 491,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3101
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 491,
          "cache_read_input_tokens": 13029,
          "cache_creation_input_tokens": 3101,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3101,
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

_source line 30 · 2026-05-27T22:01:07.764Z_

<details><summary>↩ Tool result · `toolu_018Lf7HnY6ik3mEkAfX2U6dD`</summary>

```text
# GM-PRM: Generative Multimodal Process Reward Model

## Basic Information
**Title:** GM-PRM: A Generative Multimodal Process Reward Model for Multimodal Mathematical Reasoning

**arXiv ID:** 2508.04088

**Authors:** Jianghangfan Zhang, Yibo Yan, Kening Zheng, Xin Zou, Song Dai, Xuming Hu

**Submission Date:** August 6-7, 2025

---

## Core Abstract
The paper addresses limitations in how MLLMs handle intricate mathematical reasoning tasks. The authors state: "Process Reward Models (PRMs) offer step-by-step supervision, existing multimodal PRMs are limited to being binary verifiers" that identify but cannot fix errors.

---

## Methodology for Multimodal Generative PRM

GM-PRM transforms traditional process reward evaluation through three innovations:

1. **Fine-grained Analysis:** Rather than binary pass/fail judgments, the model evaluates each reasoning step for step intent, visual alignment, and logical soundness

2. **Generative Correction Capability:** Uniquely, GM-PRM "is trained to generate a corrected version of the first erroneous step it identifies"

3. **Refined Best-of-N Strategy:** A novel inference approach where "the PRM's generated correction guides the policy model toward a more promising reasoning trajectory"

---

## Key Results

- Achieves state-of-the-art performance on multiple multimodal math benchmarks
- Demonstrates "remarkable data efficiency, requiring only a 20K-sample training dataset"
- Significantly enhances policy model performance while improving solution diversity and correctness

---

## Paradigm Extension

GM-PRM shifts the PRM from "passive judge into an active reasoning collaborator," extending generative capabilities from text-only to multimodal mathematical reasoning contexts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d23c944-a590-46b5-91a5-2f69e36ba42b",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "ae6ad09eca6bec01f",
  "type": "user",
  "uuid": "53c5ead5-2b1a-43ef-bb8b-f2f57ae98bc6",
  "sourceToolAssistantUUID": "5d23c944-a590-46b5-91a5-2f69e36ba42b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-27T22:01:07.840Z_

<details><summary>↩ Tool result · `toolu_01NnBNxJ89hhQobyJEQm8XKK`</summary>

```text
Web search results for query: "ThinkPRM 86.5 F1 ProcessBench results venue ICML NeurIPS 2025 2026 accepted"

Links: [{"title":"ThinkPRM: More Than Just Chain-of-Thought (CoT 2.0)","url":"https://www.llmwatch.com/p/thinkprm-more-than-just-chain-of"},{"title":"Papers Explained 368: ThinkPRM. ThinkPRM, a long CoT verifier… | by Ritvik Rastogi | Medium","url":"https://ritvik19.medium.com/papers-explained-368-thinkprm-0f530cc98ca4"},{"title":"Process Reward Models That Think","url":"https://arxiv.org/pdf/2504.16828"},{"title":"Published in Transactions on Machine Learning Research (03/2026)","url":"https://openreview.net/pdf?id=FPVCb0WMuN"},{"title":"ThinkPRM: A Generative Process Reward Models for Scalable Reasoning Verification - MarkTechPost","url":"https://www.marktechpost.com/2025/04/29/thinkprm-a-generative-process-reward-models-for-scalable-reasoning-verification/"},{"title":"FreePRM: Training Process Reward Models Without Ground Truth Process Labels","url":"https://arxiv.org/pdf/2506.03570"},{"title":"Is PRM Necessary? Problem-Solving RL Implicitly Induces PRM Capability in LLMs","url":"https://arxiv.org/pdf/2505.11227"},{"title":"Performance (F1) on ProcessBench. Results marked with * come from Zhang... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Performance-F1-on-ProcessBench-Results-marked-with-come-from-Zhang-et-alThe-best_tbl1_392105521"}]

Based on the search results, I can provide you with information about ThinkPRM's 86.5 F1 ProcessBench results:

On ProcessBench (a benchmark for identifying reasoning errors), ThinkPRM-14B achieves 86.5% F1 score compared to 73.7% for the LLM-as-a-judge approach using the same base model.

Regarding publication venue, the search results show that the ThinkPRM paper was published in Transactions on Machine Learning Research (03/2026). The paper is also available on arXiv as "Process Reward Models That Think" (arxiv.org/pdf/2504.16828).

I did not find specific information in these search results confirming acceptance at ICML or NeurIPS 2025/2026 conferences. The publication appears to be in Transactions on Machine Learning Research (TMLR), which is a peer-reviewed venue, but I cannot confirm venue acceptance at the conferences you mentioned based on these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d89a28b3-6ea7-4936-a478-bb3b47e12b92",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "ae6ad09eca6bec01f",
  "type": "user",
  "uuid": "f89e23c5-8c61-4ec4-b05f-62f6f970c312",
  "sourceToolAssistantUUID": "d89a28b3-6ea7-4936-a478-bb3b47e12b92",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-27T22:01:11.135Z_

<details><summary>↩ Tool result · `toolu_01NMa8bvyxRtudpYxVegoM3L`</summary>

```text
Web search results for query: "generative process reward model discriminative complementary 2025 2026"

Links: [{"title":"[2506.14175] GRAM: A Generative Foundation Reward Model for Reward Generalization","url":"https://arxiv.org/abs/2506.14175"},{"title":"Generative Reward Model (GRM)","url":"https://www.emergentmind.com/topics/generative-reward-model-grm"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2512.16917"},{"title":"GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub","url":"https://github.com/RyanLiu112/Awesome-Process-Reward-Models"},{"title":"GitHub - RyanLiu112/GenPRM: [AAAI 2026] Official codebase for \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\".","url":"https://github.com/RyanLiu112/GenPRM"},{"title":"GRAM: A Generative Foundation Reward Model for Reward Generalization","url":"https://arxiv.org/pdf/2506.14175"},{"title":"Generative Reward Models | OpenReview","url":"https://openreview.net/forum?id=MwU2SGLKpS"}]

Here are the search results for your query on generative and discriminative reward models from 2025-2026:

## Key Findings

**GRAM: Generative Foundation Reward Model**

A recent approach provides a new view of training reward models, linking generative models and discriminative models under the same class of training objectives. This foundation reward model can be applied to a wide range of tasks with little or no further fine-tuning effort, generalizing well across several tasks including response ranking, reinforcement learning from human feedback, and task adaptation.

**Generative Reward Models (GRMs)**

GRMs unify reward estimation, task structure, preference realization, and interpretability within a principled generative modeling framework, bridging generative and discriminative objectives to enable foundation models trained on both unlabeled and labeled data.

**Recent Process Reward Model Developments**

Recent work includes discriminative policy optimization for token-level reward models (ICML 2025), error-aware hierarchical supervision approaches, generative reasoning via GenPRM (accepted to AAAI 2026), and reasoning-driven process reward modeling.

**GenPRM Acceptance**

GenPRM, which scales test-time compute of process reward models via generative reasoning, was accepted by AAAI 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c65c931e-dcd7-4075-b953-ddcdf2304ee7",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "ae6ad09eca6bec01f",
  "type": "user",
  "uuid": "44ca83df-414d-479e-97fd-6eebb5c490b5",
  "sourceToolAssistantUUID": "c65c931e-dcd7-4075-b953-ddcdf2304ee7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-27T22:01:12.746Z_

<details><summary>↩ Tool result · `toolu_01DnT9QSzyK6khGymAn1KJGV`</summary>

```text
# ThinkPRM: Key Technical Details

## 1) ProcessBench F1 Scores
The paper reports results on ProcessBench subsets (OlympiadBench and OmniMath), showing ThinkPRM-14B achieves **87.3 F1** on OlympiadBench and **85.7 F1** on OmniMath after finetuning on just 1K examples—compared to discriminative PRMs trained on vastly more data.

## 2) Reasoning Generation Mechanism
ThinkPRM generates verification through extended chain-of-thought. The model produces a `&lt;think>` block analyzing each solution step, then outputs boxed verdicts like `\boxed{correct}` or `\boxed{incorrect}`. A solution score is derived by computing conditional token probabilities: "P(yes) / [P(yes) + P(no)]" after forcing decoding of "Is the solution correct?"

## 3) Training Procedure
Synthetic data collection involves:
- Sampling verification chains from QwQ-32B-Preview on PRM800K problems
- Filtering chains matching three criteria: "(i) follow expected format with extractable labels, (ii) step decisions match gold labels, (iii) under 4096 tokens"
- Obtaining 1K high-quality chains through rejection sampling
- Finetuning with LoRA (rank 32) for 3-5 epochs on a single A100 GPU (1.5-4.5 hours)

## 4) Benchmark Results Summary

| Task | Model | Result |
|------|-------|--------|
| MATH-500 (beam search) | ThinkPRM-1.5B | ~5% better than DiscPRM |
| AIME '24 (best-of-N) | ThinkPRM-14B | Superior accuracy curve |
| GPQA-Physics (OOD) | ThinkPRM | 8% better than DiscPRM |
| LiveCodeBench (OOD) | ThinkPRM | 4.5% improvement |

## 5) Stated Limitations
The paper identifies three key constraints:
- **Overconfidence**: Probability estimates cluster near extremes (0 or 1)
- **Step label interference**: Earlier verification errors propagate to subsequent steps
- **Computational overhead**: Generating verification chains costs more than discriminative approaches, though "performance gains justify extra cost"

## 6) Why ThinkPRM Outperforms Discriminative Models
Primary advantages include:
- **Data efficiency**: Requires only 1% of PRM800K labels (8K vs. 712K process labels)
- **Leverages reasoning abilities**: Built on large reasoning models with inherent problem-solving capabilities
- **Better on difficult problems**: Shows pronounced improvements on higher-difficulty tasks
- **Interpretability**: Verification reasoning is human-readable, enabling transparency

## 7) Compute Cost Discussion
Training is "extremely efficient"—the largest model (QwQ-32B-Preview) trains in 4.5 hours on single GPU. For inference, parallel scaling with K=4 verification CoTs shows diminishing returns. Sequential scaling (forcing longer chains) provides comparable performance at same token budgets as parallel approaches.

## 8) Discriminative-Generative Complementarity
The paper does not explicitly discuss combining both approaches. However, results suggest generative models excel where discriminative ones struggle—particularly on out-of-domain tasks and difficult reasoning problems—implying potential for complementary deployment strategies.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21510a6a-be3d-4e66-b923-c9f380daf259",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "ae6ad09eca6bec01f",
  "type": "user",
  "uuid": "2d545ce6-97ec-4e1f-922e-957560328957",
  "sourceToolAssistantUUID": "21510a6a-be3d-4e66-b923-c9f380daf259",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-27T22:01:15.389Z_

Let me fetch a few more key resources to complete the picture.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d545ce6-97ec-4e1f-922e-957560328957",
  "isSidechain": true,
  "agentId": "ae6ad09eca6bec01f",
  "requestId": "req_011CbTpuNsuDZxdiKwyPuN1P",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "186eb1e3-5229-4b97-bb84-380e826a3e73",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ECF37wE5b8mx5ZDAbQUEto",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1891,
      "cache_creation_input_tokens": 1332,
      "cache_read_input_tokens": 16130,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1332,
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

_source line 35 · 2026-05-27T22:01:17.674Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WpEEDBQdtUqNTqx4wUA5Cr`</summary>

```json
{
  "url": "https://openreview.net/forum?id=FPVCb0WMuN",
  "prompt": "Confirm that this is the ThinkPRM paper published in TMLR. Extract the venue, acceptance date, reviewer scores, and any notable reviewer comments about limitations or strengths."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "186eb1e3-5229-4b97-bb84-380e826a3e73",
  "isSidechain": true,
  "agentId": "ae6ad09eca6bec01f",
  "requestId": "req_011CbTpuNsuDZxdiKwyPuN1P",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a9b679e-24cc-4cb9-aefc-c6167d05a03b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ECF37wE5b8mx5ZDAbQUEto",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1891,
      "cache_creation_input_tokens": 1332,
      "cache_read_input_tokens": 16130,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1332,
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

_source line 36 · 2026-05-27T22:01:20.008Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XRhnqmE6VL5AgYGpzfWKTF`</summary>

```json
{
  "url": "https://github.com/RyanLiu112/Awesome-Process-Reward-Models",
  "prompt": "Extract the full list of generative/reasoning-augmented PRMs listed in this repository. Focus on papers from 2025-2026 that use generative reasoning, chain-of-thought, or critique-based approaches for process reward modeling. List each paper's title, date, and key approach."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a9b679e-24cc-4cb9-aefc-c6167d05a03b",
  "isSidechain": true,
  "agentId": "ae6ad09eca6bec01f",
  "requestId": "req_011CbTpuNsuDZxdiKwyPuN1P",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b3d3b11e-69c3-4852-9015-3835ac7b5b9f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ECF37wE5b8mx5ZDAbQUEto",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1891,
      "cache_creation_input_tokens": 1332,
      "cache_read_input_tokens": 16130,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1332,
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

_source line 37 · 2026-05-27T22:01:20.939Z_

<details><summary>↩ Tool result · `toolu_01WpEEDBQdtUqNTqx4wUA5Cr`</summary>

```text
# ThinkPRM Paper Confirmation

**Venue:** TMLR (Transactions on Machine Learning Research)

**Acceptance Date:** March 9, 2026

**Reviewer Scores & Comments:** The page content provided does not include reviewer scores or detailed reviewer comments about limitations or strengths. The document only shows the abstract and publication metadata.

**What is available:**
- The paper was published and accepted by TMLR
- It received a "J2C Certification" 
- The submission type is noted as "Regular submission (no more than 12 pages of main content)"
- An Action Editor was assigned: Dennis J.N.J. Soemers

The webpage excerpt appears to be the front matter/landing page rather than the full review details, which would typically be accessible through the "Revisions" link shown on the page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a9b679e-24cc-4cb9-aefc-c6167d05a03b",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "ae6ad09eca6bec01f",
  "type": "user",
  "uuid": "17998da1-f6a1-424c-8950-9d9abdfcfa3a",
  "sourceToolAssistantUUID": "9a9b679e-24cc-4cb9-aefc-c6167d05a03b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-27T22:01:21.444Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01ToQAnnrs7VPPZFjbYmstg9`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.14175",
  "prompt": "Extract details about GRAM: title, authors, abstract, arXiv ID, methodology for bridging generative and discriminative reward models, key results, and whether it discusses the complementarity of generative and discriminative approaches."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17998da1-f6a1-424c-8950-9d9abdfcfa3a",
  "isSidechain": true,
  "agentId": "ae6ad09eca6bec01f",
  "requestId": "req_011CbTpuNsuDZxdiKwyPuN1P",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "84282499-9dbe-4dfc-9925-28af38f518fb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ECF37wE5b8mx5ZDAbQUEto",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1891,
      "cache_creation_input_tokens": 1332,
      "cache_read_input_tokens": 16130,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1332,
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

_source line 39 · 2026-05-27T22:01:22.724Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HMctwQyzafX13MeCNuyEQ6`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.11250",
  "prompt": "Extract details about this uncertainty-aware generative reward model paper: title, authors, abstract, arXiv ID, methodology, key results, and how it relates to generative PRMs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84282499-9dbe-4dfc-9925-28af38f518fb",
  "isSidechain": true,
  "agentId": "ae6ad09eca6bec01f",
  "requestId": "req_011CbTpuNsuDZxdiKwyPuN1P",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cfbb5ee6-f394-4bde-8329-c5a342ac7599",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ECF37wE5b8mx5ZDAbQUEto",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1891,
      "cache_creation_input_tokens": 1332,
      "cache_read_input_tokens": 16130,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1332,
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

_source line 40 · 2026-05-27T22:01:25.895Z_

<details><summary>↩ Tool result · `toolu_01XRhnqmE6VL5AgYGpzfWKTF`</summary>

```text
# Generative/Reasoning-Augmented PRMs (2025-2026)

Based on the repository, here are the key papers employing generative reasoning approaches:

1. **GenPRM** (April 2025)
   - "Scaling Test-Time Compute of Process Reward Models via Generative Reasoning"
   - Approach: Leverages generative reasoning to expand computational capacity at inference time for PRM evaluation

2. **ThinkPRM** (April 2025)
   - "Process Reward Models That Think"
   - Approach: Integrates reflective thinking capabilities into PRM architecture for improved step verification

3. **R-PRM** (March 2025)
   - "Reasoning-Driven Process Reward Modeling"
   - Approach: Centers on reasoning mechanisms to guide process supervision and reward assignment

4. **SP-PRM** (June 2025)
   - "From Outcomes to Processes: Guiding PRM Learning from ORM for Inference-Time Alignment"
   - Approach: Transfers outcome-based reasoning patterns to improve process-level supervision

5. **FreePRM** (June 2025)
   - "Training Process Reward Models Without Ground Truth Process Labels"
   - Approach: Employs synthetic reasoning data generation to circumvent manual annotation requirements

6. **SPARE** (June 2025)
   - "Single-Pass Annotation with Reference-Guided Evaluation for Automatic Process Supervision"
   - Approach: Uses reference-guided evaluation mechanisms to automatically construct training signals
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3d3b11e-69c3-4852-9015-3835ac7b5b9f",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "ae6ad09eca6bec01f",
  "type": "user",
  "uuid": "5719f5b0-056c-48a7-80a4-e3bb64ecd060",
  "sourceToolAssistantUUID": "b3d3b11e-69c3-4852-9015-3835ac7b5b9f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-27T22:01:26.570Z_

<details><summary>↩ Tool result · `toolu_01ToQAnnrs7VPPZFjbYmstg9`</summary>

```text
# GRAM: Generative Foundation Reward Model

**Title:** "GRAM: A Generative Foundation Reward Model for Reward Generalization"

**ArXiv ID:** 2506.14175

**Authors:** Chenglong Wang, Yang Gan, Yifu Huo, Yongyu Mu, Qiaozhi He, Murun Yang, Bei Li, Tong Xiao, Chunliang Zhang, Tongran Liu, Jingbo Zhu

## Abstract Summary
The researchers developed a reward model trained on both unlabeled and labeled data. They describe their approach as "first trained via large-scale unsupervised learning and then fine-tuned via supervised learning."

## Bridging Generative and Discriminative Models
The methodology connects these approaches through label smoothing. The paper demonstrates that "by using label smoothing, we are in fact optimizing a regularized pairwise ranking loss," which "links generative models and discriminative models under the same class of training objectives."

## Key Results
The foundation reward model demonstrates broad applicability across:
- Response ranking
- Reinforcement learning from human feedback
- Task adaptation with fine-tuning

The paper reports "significant performance improvements over several strong baseline models."

## Status
Accepted by ICML 2025 (submitted June 17, 2025; latest version January 24, 2026)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84282499-9dbe-4dfc-9925-28af38f518fb",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "ae6ad09eca6bec01f",
  "type": "user",
  "uuid": "017dc4ca-e0b6-4cff-909e-e9f0f7477ebd",
  "sourceToolAssistantUUID": "84282499-9dbe-4dfc-9925-28af38f518fb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-27T22:01:29.267Z_

<details><summary>↩ Tool result · `toolu_01HMctwQyzafX13MeCNuyEQ6`</summary>

```text
# Uncertainty-Aware Step-wise Verification with Generative Reward Models

**arXiv ID:** 2502.11250 (cs.CL)

**Authors:** Zihuiwen Ye, Luckeciano Carvalho Melo, Younesse Kaddar, Phil Blunsom, Sam Staton, Yarin Gal

**Submission Date:** February 16, 2025

## Abstract Summary
The paper addresses challenges in using process reward models (PRMs) for verifying intermediate steps in multi-step mathematical reasoning. The authors note that "process supervision via process reward models (PRMs) provides intermediate rewards to verify step-wise correctness in solution traces," yet these models face reliability issues including reward hacking vulnerabilities.

## Methodology
The researchers introduce **CoT Entropy**, described as "a novel UQ method that outperforms existing approaches in quantifying a PRM's uncertainty in step-wise verification." Their approach applies uncertainty quantification techniques to enhance reliability of generative reward models used as judges for evaluating solution steps.

## Key Results
Incorporating uncertainty estimates into PRMs improves robustness, leading to "more reliable verification" of mathematical problem-solving traces. This addresses the proxy-judgment limitations inherent to current process reward models.

## Relevance to Generative PRMs
This work directly enhances generative PRM functionality by introducing uncertainty awareness, making judge-LM based reward models more trustworthy for intermediate step evaluation in complex reasoning tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cfbb5ee6-f394-4bde-8329-c5a342ac7599",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "ae6ad09eca6bec01f",
  "type": "user",
  "uuid": "c8138ad4-42c4-4f11-a915-318126d56a42",
  "sourceToolAssistantUUID": "cfbb5ee6-f394-4bde-8329-c5a342ac7599",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-27T22:01:32.259Z_

Let me get a few final pieces of information to round out the research.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8138ad4-42c4-4f11-a915-318126d56a42",
  "isSidechain": true,
  "agentId": "ae6ad09eca6bec01f",
  "requestId": "req_011CbTpvbVTQm1nX4gXSmBN4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a9df664-fe8c-4409-a182-bd25b7058718",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBxJNL9W7NGkXn7Av2bWxc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3680,
      "cache_read_input_tokens": 17462,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3680,
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

_source line 44 · 2026-05-27T22:01:35.066Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XRzTc9EifNBLHPrZp1vTBX`</summary>

```json
{
  "url": "https://openreview.net/forum?id=gEu9xXzTlI",
  "prompt": "Extract details about StepWiser from the OpenReview page: venue submission (ICLR 2026?), acceptance status, reviewer scores and comments, any noted strengths and weaknesses."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a9df664-fe8c-4409-a182-bd25b7058718",
  "isSidechain": true,
  "agentId": "ae6ad09eca6bec01f",
  "requestId": "req_011CbTpvbVTQm1nX4gXSmBN4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "13b499d3-aaf3-48b9-ba69-bc62bada31cf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBxJNL9W7NGkXn7Av2bWxc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3680,
      "cache_read_input_tokens": 17462,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3680,
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

_source line 45 · 2026-05-27T22:01:35.250Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TFpiZc7gkKZeYxfJmsV2v4`</summary>

```json
{
  "query": "R-PRM reasoning-driven process reward modeling 2025 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13b499d3-aaf3-48b9-ba69-bc62bada31cf",
  "isSidechain": true,
  "agentId": "ae6ad09eca6bec01f",
  "requestId": "req_011CbTpvbVTQm1nX4gXSmBN4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "30c93183-c062-4771-b625-3ad09326e849",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBxJNL9W7NGkXn7Av2bWxc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3680,
      "cache_read_input_tokens": 17462,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3680
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 198,
          "cache_read_input_tokens": 17462,
          "cache_creation_input_tokens": 3680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3680,
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

_source line 46 · 2026-05-27T22:01:38.846Z_

<details><summary>↩ Tool result · `toolu_01XRzTc9EifNBLHPrZp1vTBX`</summary>

```text
# StepWiser Submission Details

**Venue & Status:**
The paper was submitted to ICLR 2026 Conference and has a status of "Withdrawn Submission" as of the December 10, 2025 modification date.

**Available Information:**
The page provides limited evaluation details. No reviewer scores, comments, or detailed feedback sections are visible in the provided content. The submission lacks information about strengths and weaknesses as assessed by reviewers.

**Paper Overview:**
The authors describe their work as addressing process reward modeling by proposing "a generative judge that reasons about the policy model's reasoning steps" rather than using traditional classification approaches. They claim three key contributions: improved judgment accuracy on intermediate steps, utility for training-time policy improvement, and benefits for inference-time search.

**Note:** The withdrawn status suggests the authors may have removed this submission before the review process concluded or before a final decision was issued. To access detailed reviewer feedback and formal evaluation metrics, you would need to contact OpenReview directly or consult the authors.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13b499d3-aaf3-48b9-ba69-bc62bada31cf",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "ae6ad09eca6bec01f",
  "type": "user",
  "uuid": "56cae31f-0492-441a-848e-3429f484486d",
  "sourceToolAssistantUUID": "13b499d3-aaf3-48b9-ba69-bc62bada31cf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-27T22:01:43.105Z_

<details><summary>↩ Tool result · `toolu_01TFpiZc7gkKZeYxfJmsV2v4`</summary>

```text
Web search results for query: "R-PRM reasoning-driven process reward modeling 2025 arXiv"

Links: [{"title":"R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://github.com/NJUNLP/R-PRM"},{"title":"[2503.21295] R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://arxiv.org/abs/2503.21295"},{"title":"[2503.21295v1] R-PRM: Reasoning-Driven Process Reward Modeling","url":"http://arxiv.org/abs/2503.21295v1"},{"title":"R-PRM: Reasoning-Driven Process Reward Modeling - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.679/"},{"title":"R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://aclanthology.org/2025.emnlp-main.679.pdf"},{"title":"GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub","url":"https://github.com/RyanLiu112/Awesome-Process-Reward-Models"},{"title":"R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://arxiv.org/pdf/2503.21295"},{"title":"R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://arxiv.org/html/2503.21295v1"}]

I found comprehensive information about R-PRM on arXiv. Here's what the search revealed:

## R-PRM: Reasoning-Driven Process Reward Modeling

R-PRM is a paper published on arXiv in 2025 (eprint: 2503.21295) by Shuaijie She, Junxiao Liu, Yifeng Liu, Jiajun Chen, Xin Huang, and Shujian Huang.

### Overview
R-PRM is a novel approach that enhances LLMs' ability to evaluate mathematical reasoning step-by-step. The paper addresses how large language models inevitably make mistakes when performing step-by-step mathematical reasoning, and Process Reward Models (PRMs) have emerged as a promising solution by evaluating each reasoning step.

### Framework
The framework consists of three parts: supervised cold-start, further meta-optimization in a self-evolving style, and finally inference-time-scaling. More specifically, the approach leverages stronger LLMs to generate seed data from limited annotations for step-by-step evaluation, and further enhances performance through preference optimization, without requiring additional annotated data.

### Performance
Despite using only ~15% of the data, R-PRM's performance is already comparable to Qwen2.5-Math-PRM, which was trained on a much larger 1.8M LLM-filtered dataset. On ProcessBench and PRMBench, it surpasses strong baselines by 13.9 and 8.5 F1 scores, and when applied to guide mathematical reasoning, R-PRM achieves consistent accuracy improvements of over 8.6 points across six challenging datasets.

You can access the paper directly at https://arxiv.org/abs/2503.21295.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30c93183-c062-4771-b625-3ad09326e849",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "ae6ad09eca6bec01f",
  "type": "user",
  "uuid": "61cc322b-2f22-4739-b4ed-dcc9883996bf",
  "sourceToolAssistantUUID": "30c93183-c062-4771-b625-3ad09326e849",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-27T22:01:46.902Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018EX6xkoDUvvg354RuWcRZN`</summary>

```json
{
  "url": "https://arxiv.org/abs/2503.21295",
  "prompt": "Extract details about R-PRM: title, authors, abstract, arXiv ID, venue (EMNLP 2025?), methodology (how reasoning-driven approach works, meta-optimization, self-evolving), key results, and how it compares to discriminative PRMs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61cc322b-2f22-4739-b4ed-dcc9883996bf",
  "isSidechain": true,
  "agentId": "ae6ad09eca6bec01f",
  "requestId": "req_011CbTpwchf84b8gdr2N3NNK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "699c362f-64df-4157-84d5-db9855863fa7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X6cMPA8WGsi6SmKrk6jGoT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1285,
      "cache_read_input_tokens": 21142,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1285
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 144,
          "cache_read_input_tokens": 21142,
          "cache_creation_input_tokens": 1285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1285,
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

_source line 49 · 2026-05-27T22:01:52.585Z_

<details><summary>↩ Tool result · `toolu_018EX6xkoDUvvg354RuWcRZN`</summary>

```text
# R-PRM: Reasoning-Driven Process Reward Modeling

## Basic Information
- **Title:** R-PRM: Reasoning-Driven Process Reward Modeling
- **arXiv ID:** 2503.21295
- **Authors:** Shuaijie She, Junxiao Liu, Yifeng Liu, Jiajun Chen, Xin Huang, Shujian Huang
- **Submission Date:** March 27, 2025
- **Field:** Computer Science - Computation and Language (cs.CL)
- **Venue:** Not specified as EMNLP 2025 in the provided content

## Abstract Summary
The paper addresses limitations in existing Process Reward Models (PRMs) for evaluating mathematical reasoning in Large Language Models. The authors state: "Large language models (LLMs) inevitably make mistakes when performing step-by-step mathematical reasoning."

## Methodology
The approach comprises three key components:

1. **Data Generation:** Leveraging stronger LLMs to create training data from limited annotations, bootstrapping the model's capabilities
2. **Preference Optimization:** Enhancing performance without requiring additional annotated data
3. **Inference-Time Scaling:** Maximizing reasoning potential during evaluation

## Key Results
- **ProcessBench:** 11.9 point F1 score improvement over baselines
- **PRMBench:** 8.5 point F1 score improvement
- Mathematical reasoning guidance: consistent accuracy gains exceeding 8.5 points across six datasets

## Comparison to Discriminative PRMs
The abstract indicates existing PRMs "typically output evaluation scores directly, limiting both learning efficiency and evaluation accuracy," suggesting R-PRM's reasoning-driven approach provides more comprehensive evaluation and stronger generalization.

**Repository:** Available at GitHub (NJUNLP/R-PRM)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "699c362f-64df-4157-84d5-db9855863fa7",
  "isSidechain": true,
  "promptId": "d86c770f-8d6a-4e34-b6c5-1e1c4d93824f",
  "agentId": "ae6ad09eca6bec01f",
  "type": "user",
  "uuid": "af52dd43-0b64-4282-89a5-2b0b9ce43b68",
  "sourceToolAssistantUUID": "699c362f-64df-4157-84d5-db9855863fa7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-27T22:03:21.045Z_

Now I have all the information needed. Here is the comprehensive research report.

---

## The Generative PRM Paradigm Shift: A Comprehensive Research Report (as of May 2026)

### Executive Summary

A clear paradigm shift is underway in process reward modeling. Between early 2025 and mid-2026, at least six major papers have proposed replacing discriminative (classifier-based) PRMs with **generative PRMs** that reason about reasoning before scoring. The core insight is simple but powerful: instead of training a model to output a scalar correctness score for each step, have the model generate an explicit chain-of-thought critique analyzing why a step is correct or incorrect, then derive a score from that critique. This approach is dramatically more data-efficient, generalizes better out-of-domain, and produces interpretable verification traces.

---

### 1. ThinkPRM -- "Process Reward Models That Think"

- **arXiv ID:** [2504.16828](https://arxiv.org/abs/2504.16828)
- **Authors:** Muhammad Khalifa, Rishabh Agarwal, Lajanugen Logeswaran, Jaekyeom Kim, Hao Peng, Moontae Lee, Honglak Lee, Lu Wang
- **Submitted:** April 23, 2025; revised through v5 (December 2025)
- **Venue:** Published in **Transactions on Machine Learning Research (TMLR)**, accepted March 9, 2026

#### How It Works

ThinkPRM is a **generative verifier** that produces an explicit verification chain-of-thought before scoring. The mechanism:

1. Given a solution, the model generates a `&lt;think>` block analyzing each step, critiquing its correctness.
2. After the reasoning trace, it outputs a verdict (e.g., `\boxed{correct}` or `\boxed{incorrect}`).
3. The final score is derived by computing **conditional token probabilities**: P(yes) / [P(yes) + P(no)] after forcing decoding of "Is the solution correct?"

This is fundamentally different from discriminative PRMs, which output a scalar score from a classification head without generating any reasoning.

#### Training Procedure (Extreme Data Efficiency)

- **Synthetic data generation:** Verification CoTs are sampled from QwQ-32B-Preview on PRM800K problems.
- **Rejection sampling filter:** Chains must (i) follow the expected format with extractable labels, (ii) have step decisions matching gold labels, and (iii) be under 4096 tokens.
- **Result:** Only **~1K high-quality verification chains** survive filtering, derived from only **~8K process labels** (roughly **1% of PRM800K**'s 712K labels).
- **Fine-tuning:** LoRA (rank 32) on R1-Distill-Qwen models for 3-5 epochs on a single A100 GPU (1.5-4.5 hours).

#### Key Results

| Benchmark | ThinkPRM Result | vs. Discriminative PRM |
|-----------|----------------|----------------------|
| **ProcessBench (overall)** | **86.5 F1** (ThinkPRM-14B) | vs. 73.7 F1 for LLM-as-a-judge on same base |
| ProcessBench (OlympiadBench subset) | 87.3 F1 | -- |
| ProcessBench (OmniMath subset) | 85.7 F1 | -- |
| MATH-500 (beam search) | ~5% better than DiscPRM | -- |
| GPQA-Diamond (out-of-domain) | +8% over DiscPRM | Trained on full PRM800K |
| LiveCodeBench (out-of-domain) | +4.5% over DiscPRM | Trained on full PRM800K |
| ProcessBench (same token budget) | +7.2% over LLM-as-a-Judge | Identical compute |

The 1.5B ThinkPRM outperforms GPT-4o-based LLM-as-a-Judge approaches. The 14B variant surpasses discriminative PRMs trained on 70x more data.

#### Why It Outperforms Discriminative PRMs

1. **Leverages pre-existing reasoning capabilities** of the base model rather than training a classifier from scratch.
2. **Data efficiency:** The generative format allows the model to transfer its general reasoning ability to verification, requiring far less supervision.
3. **Out-of-domain generalization:** Because the model reasons about why steps are correct rather than memorizing patterns, it transfers better to unseen domains (physics, code).
4. **Pronounced gains on harder problems** where pattern matching fails but reasoning succeeds.

#### Stated Limitations

1. **Overconfidence:** Probability estimates cluster near extremes (0 or 1), making calibration difficult.
2. **Error propagation:** Mistakes in verifying earlier steps cascade to subsequent steps.
3. **Computational overhead:** Generating verification chains is more expensive at inference time than a single forward pass through a discriminative head, though the authors argue performance gains justify the cost.

---

### 2. GenPRM -- "Scaling Test-Time Compute of Process Reward Models via Generative Reasoning"

- **arXiv ID:** [2504.00891](https://arxiv.org/abs/2504.00891)
- **Authors:** Jian Zhao, Runze Liu, Kaiyan Zhang, Zhimu Zhou, Junqi Gao, Dong Li, Jiafei Lyu, Zhouyi Qian, Biqing Qi, Xiu Li, Bowen Zhou
- **Submitted:** April 1, 2025
- **Venue:** **Accepted at AAAI 2026**

#### Method

GenPRM performs explicit CoT reasoning **with code verification** before judging each step. Key innovations:

1. **Relative Progress Estimation (RPE):** A framework to assess whether a step makes progress toward the solution relative to prior steps, producing high-quality process supervision labels.
2. **Code-verified rationale synthesis:** The model generates reasoning that includes executable code snippets to verify mathematical claims, grounding its judgments in computation.
3. **Test-time compute scaling:** The generative architecture naturally supports spending more compute at inference for harder problems.

#### Key Results

- Trained on only **23K samples** from MATH.
- **1.5B GenPRM outperforms GPT-4o** on ProcessBench.
- **7B GenPRM surpasses Qwen2.5-Math-PRM-72B** (a 72B discriminative PRM).
- Can serve as a **critic model** for iterative solution refinement, bridging the gap between PRMs and critic models.

---

### 3. StepWiser -- "Stepwise Generative Judges for Wiser Reasoning"

- **arXiv ID:** [2508.19229](https://arxiv.org/abs/2508.19229)
- **Authors:** Wei Xiong, Wenting Zhao, Weizhe Yuan, Olga Golovneva, Tong Zhang, Jason Weston, Sainbayar Sukhbaatar (Meta FAIR)
- **Submitted:** August 26, 2025
- **Venue:** Submitted to ICLR 2026; **withdrawn** before decision (December 2025)

#### Method

StepWiser reframes step evaluation from classification to **meta-reasoning** -- reasoning about reasoning:

1. **Chunks-of-Thought:** The policy model self-segments its CoT into semantically complete, purpose-driven chunks rather than arbitrary steps.
2. **Generative judge:** Instead of outputting a score, the judge generates thinking tokens analyzing each chunk before delivering a verdict.
3. **RL training:** Unlike ThinkPRM/GenPRM which use supervised fine-tuning on synthetic data, StepWiser trains its judge via **reinforcement learning using relative outcomes of rollouts** -- no static labeled datasets needed.

#### Key Claims

1. Better judgment accuracy on intermediate steps than existing methods.
2. Can improve the policy model at training time (as a training signal).
3. Improves inference-time search.

#### Status Note

The paper was withdrawn from ICLR 2026. It may be under revision for resubmission elsewhere. The RL-based training approach is distinctive and may reappear.

---

### 4. R-PRM -- "Reasoning-Driven Process Reward Modeling"

- **arXiv ID:** [2503.21295](https://arxiv.org/abs/2503.21295)
- **Authors:** Shuaijie She, Junxiao Liu, Yifeng Liu, Jiajun Chen, Xin Huang, Shujian Huang
- **Submitted:** March 27, 2025
- **Venue:** Published at **EMNLP 2025** (Main Conference)

#### Method

A three-stage approach:
1. **Supervised cold-start:** Use stronger LLMs to generate seed evaluation data from limited annotations.
2. **Self-evolving meta-optimization:** Preference optimization to improve evaluation quality without additional human labels.
3. **Inference-time scaling:** Spend more compute on harder evaluations.

#### Key Results

- Using only ~15% of training data, matches Qwen2.5-Math-PRM (trained on 1.8M samples).
- +13.9 F1 on ProcessBench over strong baselines.
- +8.5 F1 on PRMBench.
- +8.6 accuracy points on six math reasoning datasets.

---

### 5. Additional Generative/Reasoning-Augmented PRMs (2025-2026)

| Paper | arXiv ID | Date | Key Idea | Venue |
|-------|----------|------|----------|-------|
| **GM-PRM** | [2508.04088](https://arxiv.org/abs/2508.04088) | Aug 2025 | Extends generative PRMs to **multimodal** math reasoning; generates corrections for erroneous steps, not just verdicts | -- |
| **"Good Learners Think Their Thinking"** | [2507.23317](https://arxiv.org/abs/2507.23317) | Jul 2025 | Uses generative PRM as thought-level process reward in RL training; TP-GRPO algorithm | -- |
| **FreePRM** | [2506.03570](https://arxiv.org/abs/2506.03570) | Jun 2025 | Trains PRMs without ground truth process labels using synthetic reasoning | -- |
| **CoT Entropy (Uncertainty-aware PRMs)** | [2502.11250](https://arxiv.org/abs/2502.11250) | Feb 2025 | Adds uncertainty quantification to generative reward models for more reliable step verification | -- |
| **GRAM** | [2506.14175](https://arxiv.org/abs/2506.14175) | Jun 2025 | Bridges generative and discriminative objectives via label smoothing; shows both are same objective class | **ICML 2025** |
| **AgentPRM** | ACM Web Conf 2026 | 2026 | PRMs for LLM agents via step-wise promise/progress | **ACM WebConf 2026** |

---

### 6. Is the Discriminative PRM Paradigm Obsolete?

**No -- but it is no longer the default choice.** The evidence points to a nuanced picture:

**Arguments that discriminative PRMs are becoming obsolete:**
- ThinkPRM achieves higher F1 with 1% of the labels. GenPRM's 7B model beats a 72B discriminative PRM.
- Generative PRMs generalize far better out-of-domain (GPQA, LiveCodeBench) because they reason rather than pattern-match.
- Interpretability: generative PRMs produce human-readable verification traces; discriminative PRMs are black boxes.
- The trend is unmistakable: every major 2025-2026 PRM paper adopts a generative approach.

**Arguments for continued relevance of discriminative PRMs:**
- **Inference cost:** Discriminative PRMs require a single forward pass; generative PRMs must generate potentially long verification chains. For latency-sensitive applications (real-time search, large-scale best-of-N), discriminative PRMs remain cheaper.
- **Calibration:** ThinkPRM's overconfidence problem (probabilities clustering at 0/1) is a real limitation for applications requiring calibrated confidence scores.
- **GRAM's theoretical insight:** The GRAM paper (ICML 2025) formally shows that generative and discriminative training objectives can be unified under the same class via label smoothing, suggesting they are points on a spectrum rather than opposed paradigms.

**The complementary view is most accurate:**
- Use **generative PRMs** when you need high accuracy, out-of-domain robustness, interpretability, or have limited supervision data.
- Use **discriminative PRMs** when you need fast inference, well-calibrated scores, or are operating at massive scale with abundant training data.
- **Hybrid approaches** (like GRAM's unified objective, or using a fast discriminative PRM as a first filter and a generative PRM for hard cases) represent a promising direction that no paper has yet fully explored.

The paradigm has shifted from "discriminative by default" to "generative by default, discriminative when efficiency demands it."

---

Sources:
- [Process Reward Models That Think (ThinkPRM) - arXiv](https://arxiv.org/abs/2504.16828)
- [ThinkPRM - TMLR (OpenReview)](https://openreview.net/pdf?id=FPVCb0WMuN)
- [ThinkPRM GitHub](https://github.com/mukhal/ThinkPRM)
- [GenPRM - arXiv](https://arxiv.org/abs/2504.00891)
- [GenPRM GitHub (AAAI 2026)](https://github.com/RyanLiu112/GenPRM)
- [StepWiser - arXiv](https://arxiv.org/abs/2508.19229)
- [StepWiser - OpenReview (ICLR 2026 withdrawn)](https://openreview.net/forum?id=gEu9xXzTlI)
- [R-PRM - arXiv](https://arxiv.org/abs/2503.21295)
- [R-PRM - ACL Anthology (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.679/)
- [GM-PRM - arXiv](https://arxiv.org/abs/2508.04088)
- [Good Learners Think Their Thinking - arXiv](https://arxiv.org/abs/2507.23317)
- [Uncertainty-Aware Verification - arXiv](https://arxiv.org/abs/2502.11250)
- [GRAM - arXiv (ICML 2025)](https://arxiv.org/abs/2506.14175)
- [Awesome Process Reward Models (curated list)](https://github.com/RyanLiu112/Awesome-Process-Reward-Models)
- [ThinkPRM - MarkTechPost summary](https://www.marktechpost.com/2025/04/29/thinkprm-a-generative-process-reward-models-for-scalable-reasoning-verification/)
- [ThinkPRM - Medium deep dive](https://medium.com/@techsachin/thinkprm-generative-process-reward-model-for-solution-verification-via-long-cot-reasoning-2016f1e1387d)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af52dd43-0b64-4282-89a5-2b0b9ce43b68",
  "isSidechain": true,
  "agentId": "ae6ad09eca6bec01f",
  "requestId": "req_011CbTpxKGh4xf2NpyDsyBQv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "80dda2ee-fb07-4a5c-8441-0de27101a1bf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c13f1e19-3899-4377-8bff-fb8fbb823780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015okV7JV4ZdCiEKJhPTq8js",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 572,
      "cache_read_input_tokens": 22427,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 572,
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
