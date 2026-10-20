# Research conversation: I need to research the MJ1 paper (arXiv:2603.07990, March 2026) which trains a 3B multimodal judge using RL with a struc

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a6589c8efaffe0a5d.jsonl`
- **Structured JSON:** [`b439483b19694729b687.json`](../../sessions/b4/b439483b19694729b687.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

32 recorded events

### User

_source line 1 · 2026-05-27T21:44:48.968Z_

I need to research the MJ1 paper (arXiv:2603.07990, March 2026) which trains a 3B multimodal judge using RL with a structured grounded verification chain. The paper reportedly uses a chain of: observations → claims → verification → evaluation → scoring.

1. Search for and read the MJ1 paper to understand:
   - Its structured verification chain format
   - How it compares to explicit &lt;observe>/&lt;reason evidence=''> citation format
   - Its performance (reportedly 77.0% on MMRB2)
   - Whether it's used as an evaluation judge or training-time reward
   - Whether it checks integration completeness

Use WebSearch and WebFetch:
- "MJ1 multimodal judge reinforcement learning 2603.07990"
- "MJ1 structured grounded verification chain multimodal 2026"
- "multimodal judge RL training structured verification 2026"

Report specific details about the paper's method, format, and how it differs from using a distilled verifier as a training-time reward signal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "6aa519f5-8af9-4603-83c1-2d796119e096",
  "agentId": "a6589c8efaffe0a5d",
  "type": "user",
  "uuid": "9d4b197d-8dcb-4994-b86e-f1c1a1e5d482",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58eb7456-8a8b-483b-ad8a-0b4e10704882",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-27T21:44:48.971Z_

```json
{
  "parentUuid": "9d4b197d-8dcb-4994-b86e-f1c1a1e5d482",
  "isSidechain": true,
  "agentId": "a6589c8efaffe0a5d",
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
  "uuid": "80e4f772-df07-4651-bac8-60a169462a56",
  "timestamp": "2026-05-27T21:44:48.971Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58eb7456-8a8b-483b-ad8a-0b4e10704882",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-27T21:44:48.972Z_

```json
{
  "parentUuid": "80e4f772-df07-4651-bac8-60a169462a56",
  "isSidechain": true,
  "agentId": "a6589c8efaffe0a5d",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "9419fedc-4130-46f5-9b63-1af179e09352",
  "timestamp": "2026-05-27T21:44:48.972Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58eb7456-8a8b-483b-ad8a-0b4e10704882",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-27T21:44:51.779Z_



I'll research the MJ1 paper by searching for it online and fetching relevant content. Let me start by loading the necessary tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9419fedc-4130-46f5-9b63-1af179e09352",
  "isSidechain": true,
  "agentId": "a6589c8efaffe0a5d",
  "requestId": "req_011CbToerpdMUoDPUeWdek7K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "033ee5a8-614d-4f51-b408-5c53f5ddfb99",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58eb7456-8a8b-483b-ad8a-0b4e10704882",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bh8nM7UuLYdrkPpT1VHrMr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1592,
      "cache_read_input_tokens": 7411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1592,
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

_source line 5 · 2026-05-27T21:44:51.988Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019pLGqyS6ML7LSws71vJXQU`</summary>

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
  "parentUuid": "033ee5a8-614d-4f51-b408-5c53f5ddfb99",
  "isSidechain": true,
  "agentId": "a6589c8efaffe0a5d",
  "requestId": "req_011CbToerpdMUoDPUeWdek7K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9fb9dac-a566-4abe-9480-38cc999ae04a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58eb7456-8a8b-483b-ad8a-0b4e10704882",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bh8nM7UuLYdrkPpT1VHrMr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1592,
      "cache_read_input_tokens": 7411,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1592
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 110,
          "cache_read_input_tokens": 7411,
          "cache_creation_input_tokens": 1592,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1592,
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

_source line 6 · 2026-05-27T21:44:51.991Z_

<details><summary>↩ Tool result · `toolu_019pLGqyS6ML7LSws71vJXQU`</summary>

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
  "parentUuid": "e9fb9dac-a566-4abe-9480-38cc999ae04a",
  "isSidechain": true,
  "promptId": "6aa519f5-8af9-4603-83c1-2d796119e096",
  "agentId": "a6589c8efaffe0a5d",
  "type": "user",
  "uuid": "7761d9b0-2381-44ac-bed7-d66e7b0ab696",
  "sourceToolAssistantUUID": "e9fb9dac-a566-4abe-9480-38cc999ae04a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58eb7456-8a8b-483b-ad8a-0b4e10704882",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-27T21:44:54.217Z_



Now let me search for the MJ1 paper using multiple queries in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7761d9b0-2381-44ac-bed7-d66e7b0ab696",
  "isSidechain": true,
  "agentId": "a6589c8efaffe0a5d",
  "requestId": "req_011CbTof5ztK6PkBWqy34xvi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25d9fae0-bda1-49db-bf89-a7737bdcc7b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58eb7456-8a8b-483b-ad8a-0b4e10704882",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y9XZ65425BW7GvZutoJHHa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 9003,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1132,
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

_source line 8 · 2026-05-27T21:44:55.174Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FDyrgvWuEmRuPuo5eMVauW`</summary>

```json
{
  "query": "MJ1 multimodal judge reinforcement learning 2603.07990"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25d9fae0-bda1-49db-bf89-a7737bdcc7b0",
  "isSidechain": true,
  "agentId": "a6589c8efaffe0a5d",
  "requestId": "req_011CbTof5ztK6PkBWqy34xvi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc906b91-5159-47ea-bdcd-6ef044af8985",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58eb7456-8a8b-483b-ad8a-0b4e10704882",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y9XZ65425BW7GvZutoJHHa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 9003,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1132,
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

_source line 9 · 2026-05-27T21:44:55.634Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XqcrNTQijggGS1hjeyUigz`</summary>

```json
{
  "query": "MJ1 structured grounded verification chain multimodal 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc906b91-5159-47ea-bdcd-6ef044af8985",
  "isSidechain": true,
  "agentId": "a6589c8efaffe0a5d",
  "requestId": "req_011CbTof5ztK6PkBWqy34xvi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2d09b9ae-0eb0-4d8e-885e-d2d700730fbb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58eb7456-8a8b-483b-ad8a-0b4e10704882",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y9XZ65425BW7GvZutoJHHa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 9003,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1132,
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

_source line 10 · 2026-05-27T21:44:56.018Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TkNN2zKkcQV9WrXd5ciaoh`</summary>

```json
{
  "query": "multimodal judge RL training structured verification 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d09b9ae-0eb0-4d8e-885e-d2d700730fbb",
  "isSidechain": true,
  "agentId": "a6589c8efaffe0a5d",
  "requestId": "req_011CbTof5ztK6PkBWqy34xvi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d149dc11-840e-4740-9ee0-ee3b2ecd041d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58eb7456-8a8b-483b-ad8a-0b4e10704882",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y9XZ65425BW7GvZutoJHHa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 9003,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1132
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 182,
          "cache_read_input_tokens": 9003,
          "cache_creation_input_tokens": 1132,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1132,
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

_source line 11 · 2026-05-27T21:45:00.410Z_

<details><summary>↩ Tool result · `toolu_01XqcrNTQijggGS1hjeyUigz`</summary>

```text
Web search results for query: "MJ1 structured grounded verification chain multimodal 2026"

Links: [{"title":"[2603.07990] MJ1: Multimodal Judgment via Grounded Verification","url":"https://arxiv.org/abs/2603.07990"},{"title":"MJ1: Multimodal Judgment via Grounded Verification","url":"https://arxiv.org/pdf/2603.07990"},{"title":": Multimodal Judgment via Grounded Verification","url":"https://arxiv.org/html/2603.07990v1"},{"title":"MJ1: Multimodal Judgment via Grounded Verification","url":"https://mj1.haizelabs.com/"},{"title":"CoRGI: Verified Chain-of-Thought Reasoning with Post-hoc Visual Grounding","url":"https://arxiv.org/pdf/2508.00378"}]

Based on the search results, here's what I found:

MJ1 is a multimodal judge trained with reinforcement learning that enforces visual grounding through a structured grounded verification chain (observations → claims → verification → evaluation → scoring) and a counterfactual consistency reward that penalizes position bias.

Key achievements of MJ1 include:

- Without training, the mechanism improves base-model accuracy on MMRB2 by +3.8 points on Image Editing and +1.7 on Multimodal Reasoning.

- After training, MJ1, with only 3B active parameters, achieves 77.0% accuracy on MMRB2 and surpasses orders-of-magnitude larger models like Gemini-3-Pro.

These results show that grounded verification and consistency-based training substantially improve multimodal judgment without increasing model scale.

The research was published in March 2026 by researchers from Haize Labs (Bhavesh Kumar, Dylan Feng, and Leonard Tang).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d09b9ae-0eb0-4d8e-885e-d2d700730fbb",
  "isSidechain": true,
  "promptId": "6aa519f5-8af9-4603-83c1-2d796119e096",
  "agentId": "a6589c8efaffe0a5d",
  "type": "user",
  "uuid": "4277877d-2d84-4c9d-be4f-e42d811e179b",
  "sourceToolAssistantUUID": "2d09b9ae-0eb0-4d8e-885e-d2d700730fbb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58eb7456-8a8b-483b-ad8a-0b4e10704882",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-27T21:45:01.190Z_

<details><summary>↩ Tool result · `toolu_01FDyrgvWuEmRuPuo5eMVauW`</summary>

```text
Web search results for query: "MJ1 multimodal judge reinforcement learning 2603.07990"

Links: [{"title":"[2603.07990] MJ1: Multimodal Judgment via Grounded Verification","url":"https://arxiv.org/abs/2603.07990"},{"title":"MJ1: Multimodal Judgment via Grounded Verification","url":"https://arxiv.org/pdf/2603.07990"},{"title":": Multimodal Judgment via Grounded Verification","url":"https://arxiv.org/html/2603.07990"},{"title":"[2603.11665] Multi-Task Reinforcement Learning for Enhanced Multimodal LLM-as-a-Judge","url":"https://arxiv.org/abs/2603.11665"},{"title":"J1: Incentivizing Thinking in LLM-as-a-Judge via Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=dnJEHl6DI1"},{"title":"[2505.10320] J1: Incentivizing Thinking in LLM-as-a-Judge via Reinforcement Learning","url":"https://arxiv.org/abs/2505.10320"},{"title":"Multi-Task Reinforcement Learning for Enhanced Multimodal LLM-as-a-Judge","url":"https://arxiv.org/pdf/2603.11665"}]

Based on the search results, I found detailed information about the paper:

MJ1 is a multimodal judge trained with reinforcement learning that enforces visual grounding through a structured grounded verification chain (observations → claims → verification → evaluation → scoring) and a counterfactual consistency reward that penalizes position bias.

**Key Results:**

Without training, the mechanism improves base-model accuracy on MMRB2 by +3.8 points on Image Editing and +1.7 on Multimodal Reasoning. After training, MJ1, with only 3B active parameters, achieves 77.0% accuracy on MMRB2 and surpasses orders-of-magnitude larger models like Gemini-3-Pro.

**Authors and Source:**

The paper was submitted on March 9, 2026 by Bhavesh Kumar, Dylan Feng, and Leonard Tang from Haize Labs. The arXiv identifier is 2603.07990. A demo of MJ1 can be found at mj1.haizelabs.com.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc906b91-5159-47ea-bdcd-6ef044af8985",
  "isSidechain": true,
  "promptId": "6aa519f5-8af9-4603-83c1-2d796119e096",
  "agentId": "a6589c8efaffe0a5d",
  "type": "user",
  "uuid": "8b44b63e-2247-4e27-b3fe-ebf04f46313a",
  "sourceToolAssistantUUID": "dc906b91-5159-47ea-bdcd-6ef044af8985",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58eb7456-8a8b-483b-ad8a-0b4e10704882",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-27T21:45:02.326Z_

<details><summary>↩ Tool result · `toolu_01TkNN2zKkcQV9WrXd5ciaoh`</summary>

```text
Web search results for query: "multimodal judge RL training structured verification 2026"

Links: [{"title":"[2603.07990] MJ1: Multimodal Judgment via Grounded Verification","url":"https://arxiv.org/abs/2603.07990"},{"title":": Multimodal Judgment via Grounded Verification","url":"https://arxiv.org/html/2603.07990v1"},{"title":"MJ1: Multimodal Judgment via Grounded Verification","url":"https://arxiv.org/pdf/2603.07990"},{"title":"LLM as a Judge: A 2026 Guide to Automated Model Assessment | Label Your Data","url":"https://labelyourdata.com/articles/llm-as-a-judge"},{"title":"Advancing Multimodal Judge Models through a Capability-Oriented Benchmark and MCTS-Driven Data Generation","url":"https://arxiv.org/html/2603.00546"},{"title":"Multi-Task Reinforcement Learning for Enhanced Multimodal LLM-as-a-Judge","url":"https://arxiv.org/pdf/2603.11665"}]

I found several highly relevant results for your search query. Here's what the web search revealed:

## MJ1: Multimodal Judgment via Grounded Verification

MJ1 is a multimodal judge trained with reinforcement learning that enforces visual grounding through a structured grounded verification chain (observations → claims → verification → evaluation → scoring) and a counterfactual consistency reward that penalizes position bias. 

With only 3B active parameters, MJ1 achieves 77.0% accuracy on MMRB2 and surpasses orders-of-magnitude larger models like Gemini-3-Pro. Grounded verification and consistency-based training substantially improve multimodal judgment without increasing model scale.

## Related Research in 2026

Beyond MJ1, there are other recent approaches in this area:

- Incorporating MCTS pairwise data leads to performance improvements on multimodal judgment tasks, with structured, multi-step reasoning pairs providing essential signals for enhancing judgment capabilities.

- MT-RL-Judge is a unified reinforcement learning framework that leverages multi-task RL to train a comprehensive model capable of simultaneously handling diverse tasks with varying input-output formats.

All of these papers were published in March 2026 and represent cutting-edge research in applying RL training with structured verification mechanisms to improve multimodal judgment systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d149dc11-840e-4740-9ee0-ee3b2ecd041d",
  "isSidechain": true,
  "promptId": "6aa519f5-8af9-4603-83c1-2d796119e096",
  "agentId": "a6589c8efaffe0a5d",
  "type": "user",
  "uuid": "38cf5e05-e2fa-4e7e-9167-225e2995c220",
  "sourceToolAssistantUUID": "d149dc11-840e-4740-9ee0-ee3b2ecd041d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58eb7456-8a8b-483b-ad8a-0b4e10704882",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-27T21:45:04.840Z_

Good, I found the paper. Now let me fetch the full content from the arXiv HTML version and the paper's project page for detailed information about the method.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38cf5e05-e2fa-4e7e-9167-225e2995c220",
  "isSidechain": true,
  "agentId": "a6589c8efaffe0a5d",
  "requestId": "req_011CbTofqwpZqScHVyRjFzpi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "515c22d0-9bd2-4d78-a875-4ce9c10822e1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58eb7456-8a8b-483b-ad8a-0b4e10704882",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D4Yi9oY2WCBfwkUyFsEHXq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1962,
      "cache_read_input_tokens": 10135,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1962,
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

_source line 15 · 2026-05-27T21:45:11.078Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GUMkTezW8ovvNApxN6PgZf`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.07990",
  "prompt": "Extract all details about:\n1. The structured grounded verification chain format (observations, claims, verification, evaluation, scoring) - what exactly is each step, what format/tags does each step use?\n2. How the model is trained - what RL algorithm, what reward signals, what is the counterfactual consistency reward?\n3. Performance numbers - especially on MMRB2 (77.0%) and comparisons to other models\n4. Whether MJ1 is used as an evaluation judge or as a training-time reward signal\n5. Whether it checks \"integration completeness\"\n6. The exact output format/template the model produces\n7. How it compares to citation-based formats like explicit observe/reason with evidence tags\n8. Base model used (3B parameters)\n9. Any details about grounding - how observations reference specific visual content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "515c22d0-9bd2-4d78-a875-4ce9c10822e1",
  "isSidechain": true,
  "agentId": "a6589c8efaffe0a5d",
  "requestId": "req_011CbTofqwpZqScHVyRjFzpi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d5a3faaf-d309-47a7-b03a-45e8b6894923",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58eb7456-8a8b-483b-ad8a-0b4e10704882",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D4Yi9oY2WCBfwkUyFsEHXq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1962,
      "cache_read_input_tokens": 10135,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1962,
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

_source line 16 · 2026-05-27T21:45:12.737Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AJhtk6jgsuFgnvXacUMgZw`</summary>

```json
{
  "url": "https://mj1.haizelabs.com/",
  "prompt": "Extract all details about MJ1's method, its structured verification chain format, how it works, performance results, and how it is used (as a judge or as a reward signal). Include any details about the output format, grounding mechanism, and comparison to other approaches."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5a3faaf-d309-47a7-b03a-45e8b6894923",
  "isSidechain": true,
  "agentId": "a6589c8efaffe0a5d",
  "requestId": "req_011CbTofqwpZqScHVyRjFzpi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8c663756-0d25-47bc-a426-41d6f9e87e86",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58eb7456-8a8b-483b-ad8a-0b4e10704882",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D4Yi9oY2WCBfwkUyFsEHXq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1962,
      "cache_read_input_tokens": 10135,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1962,
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

_source line 17 · 2026-05-27T21:45:16.569Z_

<details><summary>↩ Tool result · `toolu_01AJhtk6jgsuFgnvXacUMgZw`</summary>

```text
# MJ1: Multimodal Judgment via Grounded Verification

I appreciate your request, but I need to note that the content provided consists only of a title. To extract the comprehensive details you've requested about MJ1's method, verification chain format, performance results, usage as a judge, output format, grounding mechanism, and comparisons to other approaches, I would need access to the full research paper or documentation.

From the title alone, I can only infer that:

- **MJ1** appears to be a system for making judgments across multiple modalities (likely text and images, given the "multimodal" designation)
- It employs a **verification mechanism** that is "grounded" in some way—possibly meaning it references concrete evidence or sources
- The approach likely addresses evaluation or assessment tasks in AI systems

To provide the detailed extraction you need about methodology, structured formats, performance metrics, and comparative analysis, please share the full document or paper content. I'm ready to analyze it thoroughly while maintaining the guidelines you've specified.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c663756-0d25-47bc-a426-41d6f9e87e86",
  "isSidechain": true,
  "promptId": "6aa519f5-8af9-4603-83c1-2d796119e096",
  "agentId": "a6589c8efaffe0a5d",
  "type": "user",
  "uuid": "056de689-10ce-440f-aea5-375a6cde88b5",
  "sourceToolAssistantUUID": "8c663756-0d25-47bc-a426-41d6f9e87e86",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58eb7456-8a8b-483b-ad8a-0b4e10704882",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-27T21:45:22.194Z_

<details><summary>↩ Tool result · `toolu_01GUMkTezW8ovvNApxN6PgZf`</summary>

```text
# MJ1: Multimodal Judgment via Grounded Verification - Key Details

## 1. Grounded Verification Chain Structure

The model generates outputs through five sequential stages:

**(p, R_A, R_B) → O → C → V → E → s**

- **Observations (O)**: Model describes visual content from prompt and both responses
- **Claims (C)**: Extracts verifiable claims from each response
- **Verification (V)**: "checks whether each claim is consistent with your observations" using binary signals (1 or 0)
- **Evaluation (E)**: Assesses responses against task-specific criteria
- **Scoring (s)**: Produces integer scores [1,10] where s_A ≠ s_B

XML tags structure each section with nested sub-tags for Response A and B components.

## 2. Training Approach

**Algorithm**: GRPO (Generalized Reward Policy Optimization) following cold-start SFT

**Composite Reward Function**:
R(J) = R_format + R_correct + R_cons

- **R_format** [0, 0.2]: XML structure compliance (0.2/11 per correct tag)
- **R_correct** {0, 1}: Preference accuracy matching ground truth
- **R_cons** {0, 1}: Counterfactual consistency reward

**Consistency Reward Mechanism**: Swaps image inputs (A↔B) and all response references in reasoning sections, regenerating only evaluation/scoring stages. Rewards only if preference correctly inverts.

## 3. Performance Metrics

**MMRB2 Results (77.0% overall)**:
- Text-to-Image: 80.2%
- Image Editing: 78.1%
- Interleaved Generation: 73.5%
- Multimodal Reasoning: 76.4%

Surpasses Gemini-3-Pro (76.3%) with only 3B active parameters versus larger models.

## 4. Primary Use Case

MJ1 functions as an **evaluation judge** for comparing multimodal responses, not primarily as a training-time reward signal for other models.

## 5. Integration Completeness

The paper doesn't explicitly use term "integration completeness" as a specific check, though evaluation criteria assess "image faithfulness," "text-image alignment," and requirement preservation.

## 6. Output Format

Structured XML template with sections:
- `&lt;prompt_img_understanding>`
- `&lt;response_a/b_img_understanding>`
- `&lt;response_claims>` (nested A/B)
- `&lt;consistency_verification>` (nested A/B)
- `&lt;evaluate_criteria>`
- `&lt;scores>` boxed format

## 7. Citation/Evidence Format Comparison

MJ1 uses embedded visual grounding via observation extraction rather than explicit "evidence citation" tags. The verification step implicitly anchors claims to observations without separate citation markup.

## 8. Base Model

**Qwen3-VL-30B-A3B** (mixture-of-experts: 30B total, 3B active parameters per token)

## 9. Grounding Mechanism Details

Observations must describe specific visual content from images. Verification forces "back-reference" to these observations when evaluating claims, creating "computational structure" that prevents bypassing visual content during scoring stages.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5a3faaf-d309-47a7-b03a-45e8b6894923",
  "isSidechain": true,
  "promptId": "6aa519f5-8af9-4603-83c1-2d796119e096",
  "agentId": "a6589c8efaffe0a5d",
  "type": "user",
  "uuid": "b182e200-be7b-4c20-8830-350844523d5d",
  "sourceToolAssistantUUID": "d5a3faaf-d309-47a7-b03a-45e8b6894923",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58eb7456-8a8b-483b-ad8a-0b4e10704882",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-27T21:45:25.886Z_

The HTML version gave excellent detail. Let me now fetch the PDF for any additional specifics about the verification chain format, the exact XML tags used, and more details about how it differs from citation-based approaches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b182e200-be7b-4c20-8830-350844523d5d",
  "isSidechain": true,
  "agentId": "a6589c8efaffe0a5d",
  "requestId": "req_011CbTohJps3RKRSfAXKwQtd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc6e0fcc-3bdc-4428-aba0-54cd8ec06076",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58eb7456-8a8b-483b-ad8a-0b4e10704882",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014quUgtRvwqS4ksw2RAn3qt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 255,
      "cache_creation_input_tokens": 1241,
      "cache_read_input_tokens": 12097,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1241,
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

_source line 20 · 2026-05-27T21:45:28.237Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017UqcXRqzB2bVCRenmYhXYA`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.07990",
  "prompt": "Extract the full abstract, any details about the structured verification chain, the exact format template used, the reward function details, and any comparisons to other judge approaches. Also extract details about how observations are grounded in visual content and how verification works."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc6e0fcc-3bdc-4428-aba0-54cd8ec06076",
  "isSidechain": true,
  "agentId": "a6589c8efaffe0a5d",
  "requestId": "req_011CbTohJps3RKRSfAXKwQtd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "848538df-feb0-460e-83b3-60e04f42b489",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58eb7456-8a8b-483b-ad8a-0b4e10704882",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014quUgtRvwqS4ksw2RAn3qt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 255,
      "cache_creation_input_tokens": 1241,
      "cache_read_input_tokens": 12097,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1241,
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

_source line 21 · 2026-05-27T21:45:28.977Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VHa338EunEmoztCYnaumNB`</summary>

```json
{
  "query": "MJ1 Haize Labs \"grounded verification\" XML format observations claims verification evaluation scoring template"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "848538df-feb0-460e-83b3-60e04f42b489",
  "isSidechain": true,
  "agentId": "a6589c8efaffe0a5d",
  "requestId": "req_011CbTohJps3RKRSfAXKwQtd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b0cf450e-3a40-4511-bd4d-e7f161db28b3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58eb7456-8a8b-483b-ad8a-0b4e10704882",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014quUgtRvwqS4ksw2RAn3qt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 255,
      "cache_creation_input_tokens": 1241,
      "cache_read_input_tokens": 12097,
      "output_tokens": 230,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1241
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 255,
          "output_tokens": 230,
          "cache_read_input_tokens": 12097,
          "cache_creation_input_tokens": 1241,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1241,
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

_source line 22 · 2026-05-27T21:45:33.498Z_

<details><summary>↩ Tool result · `toolu_017UqcXRqzB2bVCRenmYhXYA`</summary>

```text
# MJ1: Multimodal Judgment via Grounded Verification - Key Details

## Full Abstract
"Multimodal judges struggle to ground decisions in visual evidence. We present MJ1, a multimodal judge trained with reinforcement learning that enforces visual grounding through a structured grounded verification chain (observations → claims → verification → evaluation → scoring) and a counterfactual consistency reward that penalizes position bias."

The abstract continues noting that without training, the mechanism improves base-model accuracy on MMRB2 by +3.8 points on Image Editing and +1.7 on Multimodal Reasoning. With training, MJ1 achieves 77.0% accuracy on MMRB2 with only 3B active parameters, surpassing much larger models like Gemini-3-Pro.

## Structured Verification Chain
The paper specifies a five-stage chain: observations → claims → verification → evaluation → scoring. This sequential approach ensures decisions remain anchored to visual evidence throughout the reasoning process.

## Training Methodology
The model employs reinforcement learning combined with a counterfactual consistency reward mechanism designed to reduce position bias in multimodal judgment tasks.

## Performance Comparisons
MJ1 demonstrates competitive results against significantly larger models, achieving strong accuracy while maintaining a relatively modest parameter count of 3 billion active parameters.

**Note:** The available excerpt does not contain details about specific format templates, granular reward function specifications, or technical mechanisms for grounding observations in visual content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "848538df-feb0-460e-83b3-60e04f42b489",
  "isSidechain": true,
  "promptId": "6aa519f5-8af9-4603-83c1-2d796119e096",
  "agentId": "a6589c8efaffe0a5d",
  "type": "user",
  "uuid": "9a5d9e82-07a8-4827-8fe1-97b82bfbfef9",
  "sourceToolAssistantUUID": "848538df-feb0-460e-83b3-60e04f42b489",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58eb7456-8a8b-483b-ad8a-0b4e10704882",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-27T21:45:34.911Z_

<details><summary>↩ Tool result · `toolu_01VHa338EunEmoztCYnaumNB`</summary>

```text
Web search results for query: "MJ1 Haize Labs "grounded verification" XML format observations claims verification evaluation scoring template"

Links: [{"title":"MJ1: Multimodal Judgment via Grounded Verification","url":"https://mj1.haizelabs.com/"},{"title":"Leonard Tang - Haize Labs | LinkedIn","url":"https://www.linkedin.com/in/leonard-tang"},{"title":"Haize Labs","url":"https://platform.haizelabs.com/"},{"title":"Conformance testing without reference implementation of an XML standard","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8214421"},{"title":"Rewrite based Verification of XML Updates","url":"https://arxiv.org/pdf/0907.5125"},{"title":"Single-pass translation of flat-file documents into XML format including validation, ambiguity resolution, and acknowledgement generation","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7587415"},{"title":"Haize Labs Email Format | haizelabs.com Emails","url":"https://rocketreach.co/haize-labs-email-format_b6d7f870c74140d4"},{"title":"Haize Labs - Build Reliable Enterprise Intelligence","url":"https://haizelabs.com/get-haize"}]

I found information about MJ1: Multimodal Judgment via Grounded Verification from Haize Labs. MJ1 is a model described as having the best taste in the world, and it outperforms frontier models from Google (Gemini 3 Pro), OpenAI (GPT 5), and Anthropic (Claude 4.5) at measuring visual quality with less than 1% of the parameters. MJ1 excels particularly at measuring difficult-to-articulate aesthetic criteria, or human taste, and enables agents to accomplish tasks such as generating PowerPoint decks using reference templates, complex technical drawings, architecture diagrams, design assets, and websites adhering to design systems.

However, my search results don't contain specific information about XML format observations, claims verification, evaluation scoring templates, or other detailed technical specifications you mentioned. For more detailed technical documentation about MJ1's implementation and evaluation framework, you may want to check the research paper at https://mj1.haizelabs.com/ or contact Haize Labs directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0cf450e-3a40-4511-bd4d-e7f161db28b3",
  "isSidechain": true,
  "promptId": "6aa519f5-8af9-4603-83c1-2d796119e096",
  "agentId": "a6589c8efaffe0a5d",
  "type": "user",
  "uuid": "282eb0f1-5cec-44e4-9da9-ecb54e593a5c",
  "sourceToolAssistantUUID": "b0cf450e-3a40-4511-bd4d-e7f161db28b3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58eb7456-8a8b-483b-ad8a-0b4e10704882",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-27T21:45:39.364Z_

Let me get more details from the full HTML paper, specifically about the exact XML template and the comparison to other approaches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "282eb0f1-5cec-44e4-9da9-ecb54e593a5c",
  "isSidechain": true,
  "agentId": "a6589c8efaffe0a5d",
  "requestId": "req_011CbToiMcaSy1aGbjf57QAf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e060e068-8598-494e-bb61-534dde80fad2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58eb7456-8a8b-483b-ad8a-0b4e10704882",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KDc1prU87h3YfzMjLSPPSA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1563,
      "cache_read_input_tokens": 13338,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1563,
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

_source line 25 · 2026-05-27T21:45:46.997Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0193bEKXtQBc8TzkZfkTyh9X`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.07990v1",
  "prompt": "I need very specific details. Extract:\n1. The EXACT XML tags used in the verification chain template - what are the tag names like prompt_img_understanding, response_a_img_understanding, response_claims, consistency_verification, evaluate_criteria, scores? List every XML/structured tag.\n2. What exactly goes inside each tag? What does an observation look like? What does a claim look like? What does a verification step look like?\n3. The exact reward function formula - R_format, R_correct, R_cons details\n4. How the counterfactual consistency reward works step by step\n5. The cold-start SFT details - what data was used?\n6. Ablation results - what happens without verification, without consistency reward?\n7. Any example outputs showing the full chain\n8. Comparison to other judge models (GPT-5, Claude 4.5, Gemini-3-Pro scores)\n9. Whether they discuss using MJ1 as a reward model for training other models\n10. The GRPO training details - learning rate, batch size, number of steps"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e060e068-8598-494e-bb61-534dde80fad2",
  "isSidechain": true,
  "agentId": "a6589c8efaffe0a5d",
  "requestId": "req_011CbToiMcaSy1aGbjf57QAf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0d438bd8-c54b-4a59-b653-1acedba44a87",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58eb7456-8a8b-483b-ad8a-0b4e10704882",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KDc1prU87h3YfzMjLSPPSA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1563,
      "cache_read_input_tokens": 13338,
      "output_tokens": 353,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1563
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 353,
          "cache_read_input_tokens": 13338,
          "cache_creation_input_tokens": 1563,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1563,
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

_source line 26 · 2026-05-27T21:45:58.201Z_

<details><summary>↩ Tool result · `toolu_0193bEKXtQBc8TzkZfkTyh9X`</summary>

```text
# MJ1 Technical Details Extraction

## 1. XML Tags in Verification Chain

The template uses these exact tags:
- `&lt;prompt_img_understanding>`
- `&lt;response_a_img_understanding>`
- `&lt;response_b_img_understanding>`
- `&lt;response_claims>` (containing `&lt;response_a_claims>` and `&lt;response_b_claims>`)
- `&lt;consistency_verification>` (containing `&lt;response_a_verification>` and `&lt;response_b_verification>`)
- `&lt;evaluate_criteria>`
- `&lt;scores>` (with boxed format)

## 2. Content Inside Each Tag

**Observations**: "Describe what the prompt image shows" and similar descriptions for response images

**Claims**: "Verifiable claims from response A/B" extracted from the responses

**Verification**: "Verify Response A's claims against observations" — binary consistency checking

**Evaluation**: "For each criterion, evaluate both responses and explain which performs better based on observations"

## 3. Exact Reward Function

The composite reward is: `R(J) = R_format(J) + R_correct(J,y*) + R_cons(J,J',y*)`

- **R_format ∈ [0,0.2]**: "0.2/11 per correctly formed tag across 11 required tags"
- **R_correct ∈ {0,1}**: Whether sign(s_A - s_B) matches ground truth
- **R_cons ∈ {0,1}**: Binary signal for counterfactual flip correctness

## 4. Counterfactual Consistency Mechanism

During GRPO training:
1. Generate 32 completions at temperature 0.7
2. Swap inputs (A ↔ B) in all response references
3. Regenerate only evaluation and scoring stages (temperature 0)
4. Check: "whether the preference correctly inverts"
5. R_cons = 1 if verdict inverts correctly; 0 otherwise
6. Total group size becomes 64 (32 original + 32 flipped)

## 5. Cold-Start SFT Details

Training data composition:
- Text-to-Image: 12K samples (Rapidata Coherence)
- Image Editing: 38K samples (EditReward)
- Reasoning: 20K samples (RLAIF-V)
- **Total: 70K distilled reasoning traces**

## 6. Ablation Results

The paper provides limited ablations:
- **Without grounding chain**: 62.4% (Image Editing) vs 66.2% with (+3.8 point gain)
- **Without grounding chain**: 53.4% (Multimodal Reasoning) vs 55.1% with (+1.7 point gain)

No explicit ablation removing only consistency reward shown.

## 7. Example Outputs

The paper provides the prompt template structure but no complete worked example of actual model outputs through all five stages.

## 8. Comparison to Other Models

MJ1 vs frontier models on MMRB2 (77.0% avg):
- GPT-5: 72.2%
- Gemini-3-Pro: 76.3%
- Gemini-2.5-Pro: 70.9%
- GPT-4.1: 63.5%

MJ1 uses 3B active parameters vs orders-of-magnitude larger models.

## 9. Using MJ1 as Reward Model

The paper does not discuss applying MJ1 as a reward model for training other generative models beyond its evaluation role.

## 10. GRPO Training Specifics

- **Learning rate**: 5×10⁻⁵ → 1×10⁻⁷ (cosine schedule, 10% warmup)
- **Batch size**: 16
- **Completions per prompt**: 32 (temperature 0.7)
- **LoRA rank**: 64
- **Training duration**: 1 epoch
- **Max tokens**: 6,144
- **Filtering**: Sequences with |Â_i| > 0.01; skip samples with all-zero accuracy
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d438bd8-c54b-4a59-b653-1acedba44a87",
  "isSidechain": true,
  "promptId": "6aa519f5-8af9-4603-83c1-2d796119e096",
  "agentId": "a6589c8efaffe0a5d",
  "type": "user",
  "uuid": "e0094a8d-c536-4454-8dd3-42093b957b84",
  "sourceToolAssistantUUID": "0d438bd8-c54b-4a59-b653-1acedba44a87",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58eb7456-8a8b-483b-ad8a-0b4e10704882",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-27T21:46:00.888Z_

Excellent. Now let me search for any additional discussion about how MJ1 compares to citation-based verification approaches and whether it's been discussed as a training-time reward signal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0094a8d-c536-4454-8dd3-42093b957b84",
  "isSidechain": true,
  "agentId": "a6589c8efaffe0a5d",
  "requestId": "req_011CbTojxnhHDAkEb6PtSeEC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c6b2537-0036-47f2-9315-587a9e16d6a4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58eb7456-8a8b-483b-ad8a-0b4e10704882",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WQ2LbX473pekZRH2yyyp3A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1359,
      "cache_read_input_tokens": 14901,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1359,
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

_source line 28 · 2026-05-27T21:46:01.839Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DCDBgYyo1vdu3hgCNnjzkF`</summary>

```json
{
  "query": "MJ1 multimodal judge reward model training signal generative models verification grounding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c6b2537-0036-47f2-9315-587a9e16d6a4",
  "isSidechain": true,
  "agentId": "a6589c8efaffe0a5d",
  "requestId": "req_011CbTojxnhHDAkEb6PtSeEC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ecc96b1c-3ceb-49d7-8773-1e31f1516726",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58eb7456-8a8b-483b-ad8a-0b4e10704882",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WQ2LbX473pekZRH2yyyp3A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1359,
      "cache_read_input_tokens": 14901,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1359,
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

_source line 29 · 2026-05-27T21:46:02.679Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AUqmJBkXseotEydn4aBBFg`</summary>

```json
{
  "query": "\"grounded verification\" multimodal judge citation evidence tags observe reason compare 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ecc96b1c-3ceb-49d7-8773-1e31f1516726",
  "isSidechain": true,
  "agentId": "a6589c8efaffe0a5d",
  "requestId": "req_011CbTojxnhHDAkEb6PtSeEC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "84fbe97c-b905-474d-8e7b-57e844bb58b3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58eb7456-8a8b-483b-ad8a-0b4e10704882",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WQ2LbX473pekZRH2yyyp3A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1359,
      "cache_read_input_tokens": 14901,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1359
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 14901,
          "cache_creation_input_tokens": 1359,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1359,
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

_source line 30 · 2026-05-27T21:46:08.631Z_

<details><summary>↩ Tool result · `toolu_01DCDBgYyo1vdu3hgCNnjzkF`</summary>

```text
Web search results for query: "MJ1 multimodal judge reward model training signal generative models verification grounding"

Links: [{"title":"MJ1: Multimodal Judgment via Grounded Verification","url":"https://arxiv.org/pdf/2603.07990"},{"title":"[2603.07990] MJ1: Multimodal Judgment via Grounded Verification","url":"https://arxiv.org/abs/2603.07990"},{"title":": Multimodal Judgment via Grounded Verification","url":"https://arxiv.org/html/2603.07990"},{"title":"You Only Judge Once: Multi-response Reward Modeling in a Single Forward Pass","url":"https://arxiv.org/html/2604.10966"},{"title":"MJ-Bench: Is Your Multimodal Reward Model Really a Good Judge for   Text-to-Image Generation?","url":"https://arxiv.org/pdf/2407.04842"},{"title":"MJ-Bench: Is Your Multimodal Reward Model Really a Good Judge for Text-to-Image Generation?","url":"https://arxiv.org/html/2407.04842v1"},{"title":"Generative Reward Models: LLM-as-a-Judge","url":"https://www.emergentmind.com/topics/generative-reward-models-llm-as-a-judge"}]

Based on the search results, here's what I found about MJ1:

## MJ1: Multimodal Judgment via Grounded Verification

MJ1 is a multimodal judge trained with reinforcement learning that enforces visual grounding through a structured grounded verification chain (observations → claims → verification → evaluation → scoring) and a counterfactual consistency reward that penalizes position bias.

### Key Features and Training Approach

The model (Qwen3-VL-30B-A3B) is trained via SFT on distilled reasoning traces followed by GRPO with a three-component reward covering format compliance, correctness, and counterfactual consistency.

### Performance

With only 3B active parameters, MJ1 achieves 77.0% accuracy on MMRB2 and surpasses orders-of-magnitude larger models like Gemini-3-Pro. Even without training, the mechanism improves base-model accuracy on MMRB2 by +3.8 points on Image Editing and +1.7 on Multimodal Reasoning.

### The Problem It Solves

Multimodal judge performance lags behind text judges, with the bottleneck being not model scale but rather a mechanical failure in how VLMs process and reason about visual evidence.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ecc96b1c-3ceb-49d7-8773-1e31f1516726",
  "isSidechain": true,
  "promptId": "6aa519f5-8af9-4603-83c1-2d796119e096",
  "agentId": "a6589c8efaffe0a5d",
  "type": "user",
  "uuid": "8c99475b-a220-41b7-8d78-93c2274c72c6",
  "sourceToolAssistantUUID": "ecc96b1c-3ceb-49d7-8773-1e31f1516726",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58eb7456-8a8b-483b-ad8a-0b4e10704882",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-27T21:46:09.122Z_

<details><summary>↩ Tool result · `toolu_01AUqmJBkXseotEydn4aBBFg`</summary>

```text
Web search results for query: ""grounded verification" multimodal judge citation evidence tags observe reason compare 2026"

Links: [{"title":"[2603.07990] MJ1: Multimodal Judgment via Grounded Verification","url":"https://arxiv.org/abs/2603.07990"},{"title":": Multimodal Judgment via Grounded Verification","url":"https://arxiv.org/html/2603.07990v1"},{"title":"MJ1: Multimodal Judgment via Grounded Verification","url":"https://arxiv.org/pdf/2603.07990"},{"title":"BRIDGE: Benchmark for multi-hop Reasoning In long multimodal Documents with Grounded Evidence","url":"https://arxiv.org/html/2603.07931"},{"title":"RW-Post: Auditable Evidence-Grounded Multimodal Fact-Checking in the Wild","url":"https://arxiv.org/html/2605.10357v1"}]

Based on the search results, I found relevant information about grounded verification in multimodal systems. Here are the key findings:

## MJ1: Multimodal Judgment via Grounded Verification

MJ1 is a multimodal judge trained with reinforcement learning that addresses the challenge of grounding decisions in visual evidence through a structured grounded verification chain (observations → claims → verification → evaluation → scoring) and a counterfactual consistency reward that penalizes position bias.

Even without training, this mechanism improves base-model accuracy on MMRB2 by +3.8 points on Image Editing and +1.7 on Multimodal Reasoning, and after training, MJ1 with only 3B active parameters achieves 77.0% accuracy on MMRB2 and surpasses larger models like Gemini-3-Pro.

## Related Work on Evidence-Grounded Multimodal Systems

RW-Post is a benchmark for multimodal fact-checking with auditable annotations that links posts with reasoning traces and explicitly linked evidence items, supporting evaluation across different regimes to enable systematic diagnosis of visual grounding and evidence utilization.

Evidence-grounded explainability involves organizing reasoning results and supporting evidence into structured explanations with explicit evidence-ID citations, assessing whether reasoning and key points are supported by verifiable evidence.

These papers from 2026 demonstrate active research into improving how multimodal AI systems ground their decisions in visual evidence and justify their outputs through structured reasoning and citations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84fbe97c-b905-474d-8e7b-57e844bb58b3",
  "isSidechain": true,
  "promptId": "6aa519f5-8af9-4603-83c1-2d796119e096",
  "agentId": "a6589c8efaffe0a5d",
  "type": "user",
  "uuid": "fc4e6579-3a03-4c5a-9172-6a7cc4e692c4",
  "sourceToolAssistantUUID": "84fbe97c-b905-474d-8e7b-57e844bb58b3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58eb7456-8a8b-483b-ad8a-0b4e10704882",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-27T21:46:59.130Z_

I now have comprehensive information about the MJ1 paper. Here is my detailed report.

---

## MJ1: Multimodal Judgment via Grounded Verification (arXiv:2603.07990)

**Authors**: Bhavesh Kumar, Dylan Feng, Leonard Tang (Haize Labs)
**Submitted**: March 9, 2026

### Core Problem

Multimodal judge performance lags behind text judges. The paper argues the bottleneck is not model scale but a "mechanical failure" in how VLMs process and reason about visual evidence -- they tend to bypass actually looking at images when scoring.

### Structured Grounded Verification Chain

MJ1 enforces a five-stage sequential chain:

**(p, R_A, R_B) -> O -> C -> V -> E -> s**

Each stage is wrapped in XML tags:

1. **Observations (O)**: Tags `&lt;prompt_img_understanding>`, `&lt;response_a_img_understanding>`, `&lt;response_b_img_understanding>`. The model must describe the actual visual content it sees in the prompt image and in each response's images. This forces the model to actually process the visual inputs before reasoning.

2. **Claims (C)**: Tag `&lt;response_claims>` containing `&lt;response_a_claims>` and `&lt;response_b_claims>`. Extracts verifiable claims from each response.

3. **Verification (V)**: Tag `&lt;consistency_verification>` containing `&lt;response_a_verification>` and `&lt;response_b_verification>`. Each claim is checked against the observations using binary signals (1 = consistent, 0 = inconsistent). This is the key grounding step -- it forces back-reference to observations.

4. **Evaluation (E)**: Tag `&lt;evaluate_criteria>`. For each criterion, evaluates both responses and explains which performs better, based on the verified observations.

5. **Scoring (s)**: Tag `&lt;scores>` with boxed format. Produces integer scores on [1,10] where s_A must not equal s_B.

There are **11 required XML tags** total across these stages.

### Comparison to Explicit `&lt;observe>`/`&lt;reason evidence=''>` Citation Format

MJ1's approach differs from explicit citation-based formats in important ways:

- **MJ1 uses stage-separated grounding**: Observations are extracted upfront in a dedicated stage, then claims are extracted separately, then verification cross-references them. This is a **pipeline** approach where grounding is structurally enforced by stage ordering.
- **Citation formats** (like `&lt;observe>` / `&lt;reason evidence='...'>`) embed evidence references **inline** within the reasoning, linking each reasoning step directly to its supporting evidence at the point of use.
- **MJ1's verification is binary**: Each claim gets a 1 or 0 against observations. There is no nuanced evidence weighting or partial citation.
- **MJ1 does not use explicit citation markup**: There are no evidence-ID citations or pointers back to specific observation text. The verification step implicitly anchors claims to observations without formal citation tags. The grounding is structural (stage ordering forces it) rather than referential (explicit pointers).

### Training Pipeline

**Stage 1 - Cold-Start SFT**: Trained on 70K distilled reasoning traces:
- Text-to-Image: 12K samples (Rapidata Coherence)
- Image Editing: 38K samples (EditReward)
- Reasoning: 20K samples (RLAIF-V)

**Stage 2 - GRPO (Generalized Reward Policy Optimization)** with composite reward:

`R(J) = R_format(J) + R_correct(J, y*) + R_cons(J, J', y*)`

- **R_format in [0, 0.2]**: XML structure compliance, 0.2/11 per correctly formed tag across 11 required tags.
- **R_correct in {0, 1}**: Whether sign(s_A - s_B) matches ground truth preference.
- **R_cons in {0, 1}**: Counterfactual consistency -- swap A and B inputs, regenerate evaluation/scoring, check that preference correctly inverts. Penalizes position bias.

**GRPO details**: LR 5e-5 -> 1e-7 cosine schedule with 10% warmup, batch size 16, 32 completions per prompt at temperature 0.7, LoRA rank 64, 1 epoch, max 6144 tokens. Group size effectively 64 (32 original + 32 counterfactual flipped).

**Base model**: Qwen3-VL-30B-A3B (mixture-of-experts, 30B total parameters, 3B active per token).

### Performance

**MMRB2 overall: 77.0%** broken down by category:
- Text-to-Image: 80.2%
- Image Editing: 78.1%
- Interleaved Generation: 73.5%
- Multimodal Reasoning: 76.4%

**Comparisons to larger models on MMRB2**:
- MJ1 (3B active): **77.0%**
- Gemini-3-Pro: 76.3%
- GPT-5: 72.2%
- Gemini-2.5-Pro: 70.9%
- GPT-4.1: 63.5%

Even without RL training, just applying the verification chain template at inference improves base model accuracy by +3.8 on Image Editing and +1.7 on Multimodal Reasoning.

### Role: Evaluation Judge, Not Training-Time Reward

MJ1 is designed and evaluated as an **evaluation-time judge** for comparing multimodal responses. The paper does **not** discuss or propose using MJ1 as a training-time reward model for other generative models. Its purpose is to produce structured, grounded pairwise judgments at evaluation time.

This is a significant distinction from using a distilled verifier as a training-time reward signal. A training-time reward model would need to:
- Run efficiently at scale during RL training loops
- Provide differentiable or at least frequent scalar feedback
- Be robust to distribution shift as the policy model improves

MJ1's 5-stage chain with 6144 max tokens is designed for evaluation quality, not training-loop throughput. Using it as a reward signal would be computationally expensive (32 completions per judgment in the counterfactual setup) and the binary correctness signal would need adaptation for reward shaping.

### Integration Completeness

The paper does **not** explicitly discuss "integration completeness" as a named concept or check. However, the evaluation criteria within the `&lt;evaluate_criteria>` stage do assess related properties like "image faithfulness," "text-image alignment," and whether the response preserves all requirements from the prompt. These are task-specific criteria rather than a formal integration completeness verification.

### Key Takeaways for Comparison

| Dimension | MJ1 Verification Chain | Explicit Citation Format (observe/reason evidence) |
|---|---|---|
| Grounding mechanism | Stage-separated pipeline | Inline evidence references |
| Evidence linking | Implicit (stage ordering) | Explicit (evidence IDs/pointers) |
| Verification granularity | Binary per-claim (1/0) | Can be nuanced/weighted |
| Position bias mitigation | Counterfactual consistency reward | Not inherently addressed |
| Primary use | Evaluation judge | Can serve as judge or reward |
| Output overhead | 5 XML stages, up to 6144 tokens | Variable, typically lighter |

Sources:
- [MJ1: Multimodal Judgment via Grounded Verification (arXiv abstract)](https://arxiv.org/abs/2603.07990)
- [MJ1 Full Paper (HTML)](https://arxiv.org/html/2603.07990)
- [MJ1 Paper (PDF)](https://arxiv.org/pdf/2603.07990)
- [MJ1 Project Page - Haize Labs](https://mj1.haizelabs.com/)
- [MT-RL-Judge: Multi-Task RL for Multimodal LLM-as-a-Judge](https://arxiv.org/abs/2603.11665)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc4e6579-3a03-4c5a-9172-6a7cc4e692c4",
  "isSidechain": true,
  "agentId": "a6589c8efaffe0a5d",
  "requestId": "req_011CbTokmXZ24f3q63pp8q5k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5a695a92-db5f-44d8-8bdd-479545fec153",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58eb7456-8a8b-483b-ad8a-0b4e10704882",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KGtPX7CGrsVJtXqxoRG3Dx",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1466,
      "cache_read_input_tokens": 16260,
      "output_tokens": 1977,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1466
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1977,
          "cache_read_input_tokens": 16260,
          "cache_creation_input_tokens": 1466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1466,
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
