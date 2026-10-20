# Research conversation: I need to research two topics for a research proposal revision: **Topic 1: Sparse Policy Selection (arXiv 2605.06241)** 

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 86
- **Recorded user turns:** 1
- **Tool calls:** 37
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a7ecfe27cc3cea032.jsonl`
- **Structured JSON:** [`8281c2ca4227a9bc72c5.json`](../../sessions/82/8281c2ca4227a9bc72c5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

86 recorded events

### User

_source line 1 · 2026-05-28T01:27:05.134Z_

I need to research two topics for a research proposal revision:

**Topic 1: Sparse Policy Selection (arXiv 2605.06241)**
The paper shows RL modifies only 1-3% of tokens. A reviewer challenges: "if RL primarily selects among existing base model behaviors rather than learning new capabilities, then the value of COMPREHENSIVE difficulty×topic coverage is reduced—the base model's existing capability ceiling, not the training problem distribution's smoothness, becomes the binding constraint."

I need a substantive counter-argument. Please search for:
1. The Sparse Policy Selection paper itself
2. "Sharper Primitives" (arXiv 2602.08281) - how diverse training activates broader primitives
3. Any other papers arguing that diverse RL training distributions DO improve coverage of base model capabilities, even if RL is primarily "selecting" rather than "learning new" behaviors
4. Papers on how training distribution diversity affects which base-model capabilities get activated/reinforced

**Topic 2: Rollout count effects in RLVR**
Since the VCRL G=4 vs G=16 claim was wrong, I need alternative evidence that rollout count matters. Search for:
1. Papers that ablate the number of rollouts (G, K, N) in GRPO, REINFORCE, or similar RLVR methods
2. DAPO, Dr. GRPO, or other GRPO variants that discuss optimal rollout counts
3. Statistical arguments about sample size for binary reward estimation reliability

Report findings with citations and key quotes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "b426bcc4-afa7-4020-819c-e4a0279d1c7b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-28T01:27:05.140Z_

```json
{
  "parentUuid": "b426bcc4-afa7-4020-819c-e4a0279d1c7b",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
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
  "uuid": "5950203d-c4d3-45ef-ab16-99bfd61d48d2",
  "timestamp": "2026-05-28T01:27:05.140Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-28T01:27:05.141Z_

```json
{
  "parentUuid": "5950203d-c4d3-45ef-ab16-99bfd61d48d2",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ac8128a2-1f0c-4cc6-a7f0-fa45c13fbb0d",
  "timestamp": "2026-05-28T01:27:05.141Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-28T01:27:07.586Z_



I'll research both topics systematically. Let me start by searching for the relevant papers and information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac8128a2-1f0c-4cc6-a7f0-fa45c13fbb0d",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6bvgwTipPM1LgPbDWX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33df0fc5-5d65-4fb5-a9bb-76a0e4a4036c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QFpciF8w7AWLMbmY6a826V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1662,
      "cache_read_input_tokens": 7411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1662,
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

_source line 5 · 2026-05-28T01:27:08.225Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01H44oknsiFNpjsHDcDF1KjH`</summary>

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
  "parentUuid": "33df0fc5-5d65-4fb5-a9bb-76a0e4a4036c",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6bvgwTipPM1LgPbDWX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1fb8fd63-f32b-4ce7-af54-da050da7e9c4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QFpciF8w7AWLMbmY6a826V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1662,
      "cache_read_input_tokens": 7411,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1662
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 101,
          "cache_read_input_tokens": 7411,
          "cache_creation_input_tokens": 1662,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1662,
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

_source line 6 · 2026-05-28T01:27:08.228Z_

<details><summary>↩ Tool result · `toolu_01H44oknsiFNpjsHDcDF1KjH`</summary>

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
  "parentUuid": "1fb8fd63-f32b-4ce7-af54-da050da7e9c4",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "32ec3775-9219-4f7f-b754-9984f4dd37d3",
  "sourceToolAssistantUUID": "1fb8fd63-f32b-4ce7-af54-da050da7e9c4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-28T01:27:11.100Z_



Now let me launch multiple searches in parallel for both topics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32ec3775-9219-4f7f-b754-9984f4dd37d3",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6cA5r9835u2YwsWStL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "268b9a19-313c-42c0-96b7-9debd7e90baf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BvNp6SvcEPLHLVkhCHpUZN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1123,
      "cache_read_input_tokens": 9073,
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

_source line 8 · 2026-05-28T01:27:12.047Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015HVb8fUXdARSmR6aDJLGRP`</summary>

```json
{
  "query": "arXiv 2605.06241 sparse policy selection RL modifies few tokens"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "268b9a19-313c-42c0-96b7-9debd7e90baf",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6cA5r9835u2YwsWStL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d52110aa-749f-4505-add3-d70c0908ca9e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BvNp6SvcEPLHLVkhCHpUZN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1123,
      "cache_read_input_tokens": 9073,
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

_source line 9 · 2026-05-28T01:27:12.991Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018MKt7SGsGLh4DyvfQ8REKo`</summary>

```json
{
  "query": "arXiv 2602.08281 Sharper Primitives diverse training activates broader primitives"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d52110aa-749f-4505-add3-d70c0908ca9e",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6cA5r9835u2YwsWStL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fed75f44-2666-4864-ba17-e277ecff3724",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BvNp6SvcEPLHLVkhCHpUZN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1123,
      "cache_read_input_tokens": 9073,
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

_source line 10 · 2026-05-28T01:27:14.049Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WyFM9m9uK2gympZCrCDiLM`</summary>

```json
{
  "query": "diverse RL training distribution improves base model capability coverage reinforcement learning LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fed75f44-2666-4864-ba17-e277ecff3724",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6cA5r9835u2YwsWStL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f254089b-62e6-4548-9f16-926605f71378",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BvNp6SvcEPLHLVkhCHpUZN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1123,
      "cache_read_input_tokens": 9073,
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

_source line 11 · 2026-05-28T01:27:14.929Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WMdvNbn3Wx61EockrJE4fM`</summary>

```json
{
  "query": "GRPO rollout count ablation G K N number of rollouts RLVR 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f254089b-62e6-4548-9f16-926605f71378",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6cA5r9835u2YwsWStL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b909a98f-68cc-45cd-80d0-d57ea7736575",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BvNp6SvcEPLHLVkhCHpUZN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1123,
      "cache_read_input_tokens": 9073,
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

_source line 12 · 2026-05-28T01:27:15.793Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016yeCwyzCfQzA6gvQqBP9iX`</summary>

```json
{
  "query": "DAPO Dr GRPO optimal rollout count group relative policy optimization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b909a98f-68cc-45cd-80d0-d57ea7736575",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6cA5r9835u2YwsWStL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e357105a-5321-43e5-ba96-b697c12ad5d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BvNp6SvcEPLHLVkhCHpUZN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1123,
      "cache_read_input_tokens": 9073,
      "output_tokens": 301,
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
          "output_tokens": 301,
          "cache_read_input_tokens": 9073,
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

_source line 13 · 2026-05-28T01:27:18.847Z_

<details><summary>↩ Tool result · `toolu_015HVb8fUXdARSmR6aDJLGRP`</summary>

```text
Web search results for query: "arXiv 2605.06241 sparse policy selection RL modifies few tokens"

Links: [{"title":"[2605.06241] Rethinking RL for LLM Reasoning: It's Sparse Policy Selection, Not Capability Learning","url":"https://arxiv.org/abs/2605.06241"},{"title":"Rethinking RL for LLM Reasoning: It’s Sparse Policy Selection, Not Capability Learning","url":"https://arxiv.org/html/2605.06241"},{"title":"Sparse Feature Selection Makes Batch Reinforcement Learning More Sample   Efficient","url":"https://arxiv.org/pdf/2011.04019"},{"title":"Sparse Masked Attention Policies for Reliable Generalization","url":"https://arxiv.org/html/2602.19956v1"},{"title":"Rethinking RL for LLM Reasoning: It's Sparse Policy ...","url":"https://arxiv.org/pdf/2605.06241"},{"title":"Sparse-RL: Breaking the Memory Wall in LLM Reinforcement Learning via Stable Sparse Rollouts","url":"https://arxiv.org/pdf/2601.10079"}]

Based on the search results, I found the paper you're looking for!

The paper is titled "Rethinking RL for LLM Reasoning: It's Sparse Policy Selection, Not Capability Learning" by Ömer Faruk Akgül and 3 other authors.

The key finding is that RL's behavioral footprint modifies only 1–3% of token positions, does not introduce tokens outside the base model's top-5 candidates, and concentrates edits at high-entropy decision points where the model is uncertain which reasoning branch to take.

Importantly, these decision points can be located without any RL-trained model: the base model's own token entropy, which peaks at the positions RL edits, provides a strong proxy for where intervention is useful. The specific token chosen at these positions matters causally, recovering a large share of RL's gain, while random corrections fail.

The paper reframes reasoning improvement as a sparse policy selection problem rather than capability learning, suggesting that RL redistributes probability mass over solutions the base model already knows rather than teaching new strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d52110aa-749f-4505-add3-d70c0908ca9e",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "ec8f557a-80cb-41de-a718-7f7f4b36e3a5",
  "sourceToolAssistantUUID": "d52110aa-749f-4505-add3-d70c0908ca9e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-28T01:27:19.857Z_

<details><summary>↩ Tool result · `toolu_018MKt7SGsGLh4DyvfQ8REKo`</summary>

```text
Web search results for query: "arXiv 2602.08281 Sharper Primitives diverse training activates broader primitives"

Links: [{"title":"New Skills or Sharper Primitives? A Probabilistic Perspective on the Emergence","url":"https://arxiv.org/pdf/2602.08281"},{"title":"[2602.08281] New Skills or Sharper Primitives? A Probabilistic Perspective on the Emergence of Reasoning in RLVR","url":"https://arxiv.org/abs/2602.08281"},{"title":"Tailored Primitive Initialization is the Secret Key to Reinforcement Learning","url":"https://arxiv.org/html/2511.12429v1"},{"title":"New Skills or Sharper Primitives? A Probabilistic Perspective on the Emergence of Reasoning in RLVR","url":"https://arxiv.org/html/2602.08281"},{"title":"Tailored Primitive Initialization is the Secret Key to Reinforcement Learning","url":"https://arxiv.org/pdf/2511.12429"},{"title":"Algorithmic Primitives and Compositional Geometry of Reasoning in Language Models","url":"https://arxiv.org/pdf/2510.15987"},{"title":"Algorithmic Primitives and Compositional Geometry of Reasoning in Language Models","url":"https://arxiv.org/html/2510.15987v1"}]

Based on the search results, I found the paper you're looking for. Here's what it's about:

The paper "New Skills or Sharper Primitives? A Probabilistic Perspective on the Emergence of Reasoning in RLVR" addresses whether Reinforcement Learning with Verifiable Rewards (RLVR) endows Large Language Models (LLMs) with new capabilities or merely elicits latent traces, proposing a probabilistic framework where capability is defined by instance-level solvability.

The authors hypothesize that the emergence of complex reasoning can be driven by sharpening atomic step probabilities, which enables models to overcome the exponential decay of success rates inherent in multi-step reasoning chains.

The research utilizes the Algebrarium framework, training models exclusively on single-step operations and evaluating their performance on unseen multi-step tasks.

The empirical results show that RLVR incentivizes exploration of previously inaccessible solution paths by amplifying the model's existing skills, but it also polarizes the model's success probabilities across the task distribution—driving correctness probability of certain problems towards certainty while reducing the probability of solving others, which improves Pass@1 but harms broader coverage.

The paper was published on arXiv on February 9, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fed75f44-2666-4864-ba17-e277ecff3724",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "86e2d316-a443-4a04-a830-850d1a9768b4",
  "sourceToolAssistantUUID": "fed75f44-2666-4864-ba17-e277ecff3724",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-28T01:27:22.600Z_

<details><summary>↩ Tool result · `toolu_01WyFM9m9uK2gympZCrCDiLM`</summary>

```text
Web search results for query: "diverse RL training distribution improves base model capability coverage reinforcement learning LLM"

Links: [{"title":"Whatever Remains Must Be True: Filtering Drives Reasoning in LLMs, Shaping Diversity","url":"https://arxiv.org/pdf/2512.05962"},{"title":"DUMP: Automated Distribution-Level Curriculum Learning for RL-based LLM Post-training","url":"https://arxiv.org/html/2504.09710v1"},{"title":"DUMP: Automated Distribution-Level Curriculum Learning for RL-based LLM Post-training","url":"https://arxiv.org/pdf/2504.09710"},{"title":"ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models","url":"https://arxiv.org/html/2505.24864v1"},{"title":"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? | OpenReview","url":"https://openreview.net/forum?id=4OsgYD7em5"},{"title":"Tailored Primitive Initialization is the Secret Key to Reinforcement Learning","url":"https://arxiv.org/pdf/2511.12429"},{"title":"Limit of RLVR","url":"https://limit-of-rlvr.github.io/"},{"title":"Scaling Up RL: Unlocking Diverse Reasoning in LLMs via Prolonged Training","url":"https://arxiv.org/html/2507.12507v1"},{"title":"Scaling LLM Reinforcement Learning with Prolonged Training Using ProRL v2 | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/scaling-llm-reinforcement-learning-with-prolonged-training-using-prorl-v2/"}]

I've performed the web search for your query. Here are the most relevant results:

## Key Research Findings:

**Distribution-Level Curriculum Learning:**
Modern LLM training involves a mixture of data from diverse distributions—varying in both source and difficulty, and the key challenge is how to adaptively schedule training across distributions to optimize learning efficiency.

**Base Model Capability Coverage:**
One approach proposes automatically discovering and curating novel reasoning primitives to expand the coverage of reasoning-state distributions before RL, generating more diverse and higher-quality warm-start data that results in higher downstream RL performance.

**Diversity in RL Training:**
Studies find that base models already contain solutions given a sufficient sampling budget, and that tuned models often exploit additional samples less effectively due to reduced output diversity.

**Reasoning Capability Boundaries:**
Coverage and perplexity analysis shows that the reasoning paths generated by RLVR models are already included in the base models' sampling distribution, suggesting that their reasoning abilities are bounded by the base model.

The search results discuss several related approaches including DUMP (Distribution-Level Curriculum Learning), Tailor (Primitive-Oriented Reinforcement), and analyses of whether RL training actually expands base model capabilities or primarily optimizes existing latent abilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f254089b-62e6-4548-9f16-926605f71378",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "64ef7eac-2636-4810-b6f4-69dea17367f6",
  "sourceToolAssistantUUID": "f254089b-62e6-4548-9f16-926605f71378",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-28T01:27:23.239Z_

<details><summary>↩ Tool result · `toolu_01WMdvNbn3Wx61EockrJE4fM`</summary>

```text
Web search results for query: "GRPO rollout count ablation G K N number of rollouts RLVR 2025 2026"

Links: [{"title":"G2RPO-A: GUIDED GROUP RELATIVE POLICY OPTIMIZATION WITH ADAPTIVE GUIDANCE","url":"https://arxiv.org/pdf/2508.13023"},{"title":"Demystifying OPD: Length Inflation and Stabilization ...","url":"https://arxiv.org/pdf/2604.08527"},{"title":"Prune as You Generate: Online Rollout Pruning for Faster and Better RLVR","url":"https://arxiv.org/html/2603.24840"},{"title":"Depth-Breadth Synergy in RLVR: Unlocking LLM Reasoning Gains with Adaptive Exploration","url":"https://arxiv.org/html/2508.13755"},{"title":"Under review as submission to TMLR Not All Rollouts are Useful:","url":"https://openreview.net/pdf?id=MfHOmgqVXM"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2505.02387"},{"title":"SofT-GRPO: Surpassing Discrete-Token LLM Reinforcement Learning via","url":"https://arxiv.org/pdf/2511.06411"},{"title":"Continual Post-Training via Offline GRPO — KRAFTON AI","url":"https://www.krafton.ai/blog/posts/2025-07-28-llm_post_training/grpo-en.html"},{"title":"Accepted at ICLR 2026 (Oral). GEPA: REFLECTIVE PROMPT EVOLUTION CAN OUTPER-","url":"https://arxiv.org/pdf/2507.19457"},{"title":"Post-Training in 2026: GRPO, DAPO, RLVR & Beyond","url":"https://llm-stats.com/blog/research/post-training-techniques-2026"}]

I found several relevant research papers about GRPO rollout count ablations and RLVR from 2025-2026. Here are the key findings:

## Rollout Count Specifications

One study uses 12 rollouts per sample for 0.6B and 1.7B backbones, and 7 rollouts for 7B and 8B backbones.

GEPA outperforms GRPO (24k rollouts) by up to 20% while using up to 35× fewer rollouts, with an average gain of +6% across six tasks on Qwen3 8B.

## Rollout Count Ablation Studies

Research has examined how rollout count affects performance:

Naive scaling of rollout size benefits Pass@1 performance but not necessarily Pass@K. Enlarging rollout size allows sampling of correct solutions to hard problems during training, though Qwen2.5-Math-1.5b shows that naively scaling rollout size can even harm Pass@K performance.

## Efficiency Challenges

High computational cost constrains RLVR methods, as each prompt requires generating a large group of rollouts during training, which is computationally expensive.

Some methods like PODS deliver at least a 1.7× speedup while reaching higher final accuracy across diverse model architectures.

The research shows that optimal rollout counts vary significantly by model size and task type, and recent work focuses on improving efficiency while maintaining or improving performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b909a98f-68cc-45cd-80d0-d57ea7736575",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "e5d34dd6-2278-4a7b-9480-f73888cc44f6",
  "sourceToolAssistantUUID": "b909a98f-68cc-45cd-80d0-d57ea7736575",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-28T01:27:23.562Z_

<details><summary>↩ Tool result · `toolu_016yeCwyzCfQzA6gvQqBP9iX`</summary>

```text
Web search results for query: "DAPO Dr GRPO optimal rollout count group relative policy optimization"

Links: [{"title":"GRPO: Group Relative Policy Optimization","url":"https://www.emergentmind.com/topics/grpo"},{"title":"MC-GRPO: Median-Centered Group Relative Policy Optimization","url":"https://arxiv.org/pdf/2601.22582"},{"title":"MC-GRPO: Median-Centered Group Relative Policy Optimization for Small-Rollout Reinforcement Learning","url":"https://arxiv.org/html/2601.22582"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Group+Relative+Policy+Optimization"},{"title":"Group Relative Policy Optimization (GRPO) — verl documentation","url":"https://verl.readthedocs.io/en/latest/algo/grpo.html"},{"title":"The Evolution of Policy Optimization: Understanding GRPO, DAPO, and Dr. GRPO’s Theoretical Foundations | by Jennifer Wei | Medium","url":"https://medium.com/@jenwei0312/the-evolution-of-policy-optimization-understanding-grpo-dapo-and-dr-3e758c54b2c6"},{"title":"GDPO: Group reward-Decoupled Normalization Policy ...","url":"https://arxiv.org/pdf/2601.05242"}]

Based on the search results, here's what I found about these policy optimization methods:

## Overview

GRPO (Group Relative Policy Optimization) is an online learning algorithm introduced by DeepSeek that improves iteratively by using data generated by the model itself during training.

## Key Methods and Variants

**DAPO and Dr.GRPO:** λ-GRPO unifies and generalizes heuristics including DAPO and Dr.GRPO. These are variants within the GRPO family of algorithms.

**Optimal Rollout Count:** Pairwise GRPO ("2-GRPO") enables near-identical end-task performance with 1/8 the rollouts, substantially accelerating training (over 70% training time reduction). This suggests that large group sizes are not necessarily required for effective training.

**Small Rollout Optimization:** Recent research has focused on improving performance with limited rollouts. Median-Centered Group Relative Policy Optimization (MC-GRPO) is a simple and effective solution for small-rollout training, which replaces the mean baseline with a median baseline to mitigate advantage sign flips under small rollout size.

## Core Mechanism

GRPO is critic-less (unlike PPO, it does not train a separate value network) and uses group sampling to generate multiple completions from the current policy for each prompt. Within each group, completions are scored and rewards are normalized relative to the group.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e357105a-5321-43e5-ba96-b697c12ad5d1",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "1197561e-8ed0-4a46-ad55-e2a308301e98",
  "sourceToolAssistantUUID": "e357105a-5321-43e5-ba96-b697c12ad5d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-28T01:27:26.113Z_

Good, I have initial results. Now let me fetch the key papers in detail and search for additional evidence.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1197561e-8ed0-4a46-ad55-e2a308301e98",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6dHNB1uSRU5mUNwjBQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b3f4998f-5da9-4ccb-993b-097436ca40f9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HhHU4ipjojatrq16t3Cw1r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3914,
      "cache_read_input_tokens": 10196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3914,
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

_source line 19 · 2026-05-28T01:27:28.975Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DwvfE9f8KohbVce9uVCuWE`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.06241",
  "prompt": "Extract the full abstract, key findings, and any discussion about how RL selects among base model behaviors. What exactly does the paper say about the 1-3% token modification? What are the implications they draw? List specific claims with detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3f4998f-5da9-4ccb-993b-097436ca40f9",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6dHNB1uSRU5mUNwjBQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f488567-8c45-4b1b-87d4-d2a4b3645982",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HhHU4ipjojatrq16t3Cw1r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3914,
      "cache_read_input_tokens": 10196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3914,
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

_source line 20 · 2026-05-28T01:27:31.799Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ci42yGuw3rKSwdaiRWsx6j`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.08281",
  "prompt": "Extract the full abstract and key findings. Specifically: (1) How do the authors define \"sharpening primitives\"? (2) What do they say about training distribution diversity and its effects on which primitives get sharpened? (3) Do they discuss how varied training problems might activate broader sets of base model capabilities? (4) What is the \"polarization\" effect they describe? List specific claims and quotes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f488567-8c45-4b1b-87d4-d2a4b3645982",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6dHNB1uSRU5mUNwjBQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03a70f12-b3c2-4311-bfb8-b5f09369aa3d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HhHU4ipjojatrq16t3Cw1r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3914,
      "cache_read_input_tokens": 10196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3914,
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

_source line 21 · 2026-05-28T01:27:34.623Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Bs8hFHxgMFVfAcHEGxZX3d`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.08281",
  "prompt": "Look for any discussion about: (1) how training data diversity affects which primitives get sharpened, (2) whether broader training distributions lead to broader capability activation, (3) the relationship between training coverage and which base model skills get reinforced. Also extract any key equations or theoretical results about how primitive sharpening compounds in multi-step reasoning. Provide specific quotes and section references."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03a70f12-b3c2-4311-bfb8-b5f09369aa3d",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6dHNB1uSRU5mUNwjBQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "62129100-9795-4516-8cc6-a28ec90c4b42",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HhHU4ipjojatrq16t3Cw1r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3914,
      "cache_read_input_tokens": 10196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3914,
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

_source line 22 · 2026-05-28T01:27:34.784Z_

<details><summary>↩ Tool result · `toolu_01DwvfE9f8KohbVce9uVCuWE`</summary>

```text
# Analysis of arXiv:2605.06241

## Full Abstract

The paper's abstract states that reinforcement learning "does not teach new strategies; it redistributes probability mass over solutions the base model already contains." The researchers investigate whether the RL optimization loop is even necessary if this redistribution is the primary mechanism.

## Key Finding: The 1-3% Token Modification

The paper identifies a striking constraint on RL's impact:

- **"Only 1–3% of token positions are affected"** by RL training
- The promoted token always appears within the base model's top-5 alternatives
- **"targeted corrections at those few positions causally recover a large fraction of RL's accuracy gain"**
- Random corrections at these positions fail, indicating specificity matters

Critically, the base model's own entropy (uncertainty) can identify these critical positions without examining any RL-trained model.

## Core Reframing

The authors reframe reasoning improvement as **"sparse policy selection, not capability acquisition."** This is their central claim—RL doesn't teach the model new problem-solving abilities but rather steers probability toward pre-existing solution pathways at key decision points.

## ReasonMaxxer Method

Their proposed alternative, ReasonMaxxer:
- Uses contrastive loss only at entropy-gated decision points
- Requires only "a few hundred base-model rollouts and no online generation"
- Achieves comparable performance to full RL while reducing training cost by roughly three orders of magnitude
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f488567-8c45-4b1b-87d4-d2a4b3645982",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "ef464f62-d7c1-42a4-97d9-38ba0167c442",
  "sourceToolAssistantUUID": "4f488567-8c45-4b1b-87d4-d2a4b3645982",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-28T01:27:36.464Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DwEwvVUZWBwL6tnFYMkaaa`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.22582",
  "prompt": "Extract all information about: (1) How rollout count (group size) affects training quality, (2) specific ablation results comparing different rollout counts, (3) the \"advantage sign flip\" problem with small rollouts, (4) any quantitative results showing performance vs rollout count. Provide specific numbers and quotes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef464f62-d7c1-42a4-97d9-38ba0167c442",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6dHNB1uSRU5mUNwjBQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "85e21df5-f783-4df0-b875-43d0b20382f1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HhHU4ipjojatrq16t3Cw1r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3914,
      "cache_read_input_tokens": 10196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3914,
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

_source line 24 · 2026-05-28T01:27:38.249Z_

<details><summary>↩ Tool result · `toolu_01Ci42yGuw3rKSwdaiRWsx6j`</summary>

```text
# Analysis of arXiv:2602.08281

## Full Abstract
The paper proposes a probabilistic framework defining capability through instance-level solvability. The authors hypothesize that complex reasoning emerges from "sharpening atomic step probabilities," enabling models to overcome exponential decay in multi-step chains. Training exclusively on single-step operations, they evaluate performance on unseen multi-step tasks.

## Key Findings

**1. Definition of "Sharpening Primitives"**
The authors define this as improving the probability of individual atomic steps. The abstract states: "the emergence of complex reasoning can be driven by sharpening atomic step probabilities."

**2. Training Distribution Diversity**
The provided content does not explicitly discuss how training distribution diversity affects which primitives get sharpened. This analysis is absent from the available abstract and metadata.

**3. Broader Base Model Capabilities**
The document does not address whether varied training problems activate broader capability sets. The abstract only mentions training "exclusively on single-step operations."

**4. Polarization Effect**
No "polarization" effect is described in the available text. The abstract does mention that "RLVR, acting as a global optimizer, can cause specific skills to be sacrificed to maximize aggregate reward," which relates to trade-offs but not explicitly to polarization.

**Limitation**: The provided content includes only the abstract, title, and metadata. Detailed discussions of these topics likely appear in the full paper text.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03a70f12-b3c2-4311-bfb8-b5f09369aa3d",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "f64d855e-c692-43bc-988b-abe227431a6d",
  "sourceToolAssistantUUID": "03a70f12-b3c2-4311-bfb8-b5f09369aa3d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-28T01:27:38.372Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QUf9oJJ6Z1fCM52rCpDTGr`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.13755",
  "prompt": "Extract all information about rollout count ablations, the relationship between number of rollouts and RL training quality, any results comparing different values of G (group size), and how rollout breadth affects exploration and performance. Provide specific numbers and quotes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f64d855e-c692-43bc-988b-abe227431a6d",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6dHNB1uSRU5mUNwjBQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "21d13828-1e71-462f-8626-8d3585d00cbf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HhHU4ipjojatrq16t3Cw1r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3914,
      "cache_read_input_tokens": 10196,
      "output_tokens": 702,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3914
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 702,
          "cache_read_input_tokens": 10196,
          "cache_creation_input_tokens": 3914,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3914,
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

_source line 26 · 2026-05-28T01:27:40.753Z_

<details><summary>↩ Tool result · `toolu_01Bs8hFHxgMFVfAcHEGxZX3d`</summary>

```text
# Analysis of Training Data Diversity and Primitive Sharpening

Based on my review of this paper, **there is no substantive discussion of how training data diversity affects which primitives get sharpened, nor any analysis of whether broader training distributions lead to broader capability activation.**

## Key Finding

The paper uses a **deliberately constrained experimental setup** that actually avoids this question entirely. As stated in Section 6:

> "Training: The training set is strictly limited to atomic operations (1-hop reasoning)."

This design ensures all models see identical atomic primitives, eliminating variability in which skills are reinforced.

## What the Paper *Does* Address

The theoretical contribution focuses on **compositional probability compounding**, not training diversity:

**Core equation (Section 5.1):**
> "Pθ(q) ≈ ∏j=1^M Pθ(sj)"

This shows that multi-step success probability is multiplicative—sharpening individual atomic probabilities from 0.3 to 0.7 transforms a 5-step task from 0.0024 to 0.168 success rate (Section 5.2).

The paper validates this mechanism empirically through high correlation coefficients (ρ ∈ [0.69, 0.96]) between joint atomic probabilities and composite outcomes (Section 7.3).

## What Remains Unexamined

The paper does not investigate:
- Whether different training data compositions would sharpen different atomic skills
- How training coverage correlates with which base-model primitives are reinforced
- Whether diverse vs. narrow training distributions affect emergence patterns

This is a deliberate methodological choice to isolate the multiplicative barrier mechanism, but it leaves the data diversity question open for future work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62129100-9795-4516-8cc6-a28ec90c4b42",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "ac301846-9eac-4999-bd78-4e6fe372e67b",
  "sourceToolAssistantUUID": "62129100-9795-4516-8cc6-a28ec90c4b42",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-28T01:27:43.449Z_

<details><summary>↩ Tool result · `toolu_01DwEwvVUZWBwL6tnFYMkaaa`</summary>

```text
# Impact of Rollout Count on Training Quality

## How Rollout Count Affects Quality

Reducing rollouts significantly degrades performance in GRPO-style methods. The paper shows that "with fewer rollouts, the policy observes fewer diverse candidates and is less likely to sample rare but high-quality trajectories."

## The Advantage Sign Flip Problem

Small rollouts create a critical failure mode: when group size is minimal, a single outlier reward can substantially shift the mean baseline, causing "advantage sign flips" where rollouts receive incorrect advantage signs, reversing intended update directions.

The authors demonstrate this empirically: injecting synthetic sign noise shows that "increasing ρ consistently reduces final GSM8K accuracy," confirming sign flips directly harm optimization quality.

## Specific Performance Numbers vs Rollout Count

**Qwen3-1.7B on GSM8K:**
- G=2 rollouts: 78.92% accuracy
- G=4 rollouts: 81.34% accuracy  
- G=8 rollouts: 84.53% accuracy

**With MC-GRPO improvement:**
- G=2: 83.54% (+4.62 percentage points)
- G=4: 84.01% (+2.67 percentage points)
- G=8: 84.60% (+0.07 percentage points)

## Ablation Results

Median-centered variants show largest gains at small budgets and diminish as G increases. Across GRPO/DAPO/DR-GRPO variants, improvements range from 0.02% to 7.89% at G=2, versus near-zero gains at G=8.

A control experiment confirms gains aren't from extra sampling alone: mean-centered GRPO with G+1 rollouts yields only 79.68% versus MC-GRPO's 83.54% at G=2.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "85e21df5-f783-4df0-b875-43d0b20382f1",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "1e48ad71-c4a2-469c-a149-3d37d2b3e1ac",
  "sourceToolAssistantUUID": "85e21df5-f783-4df0-b875-43d0b20382f1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-28T01:27:45.617Z_

<details><summary>↩ Tool result · `toolu_01QUf9oJJ6Z1fCM52rCpDTGr`</summary>

```text
# Rollout Count and RL Training Quality Analysis

## Key Findings on Rollout Scaling

**Naive Rollout Increase Paradox:**
The paper demonstrates that simply expanding rollout size doesn't consistently improve Pass@K performance. For Qwen2.5-Math-1.5B, "naively scaling rollout size can even harm Pass@K performance," while the 7B variant benefits. This counterintuitive result challenges standard assumptions about compute allocation.

## Cumulative Advantage Bias

The authors quantify how group-level advantage computation creates distorted weighting:

> "cumulative advantage underweights low-accuracy, high-difficulty samples, capping Pass@K performance"

For Dr. GRPO with group size N, the cumulative advantage formula is: **𝒜group = 2Nu(1-u)**, where u represents accuracy. This mathematical relationship shows maximum weighting at u=0.5 (medium difficulty), systematically neglecting hard problems.

## DARS Rollout Allocation Results

**Efficiency Gains:**
DARS-ET requires 52.5% fewer rollouts than naive scaling (15.2 vs 32 average rollouts for Qwen2.5-Math-1.5B) while achieving superior Pass@128 performance. DARS-HW reduces rollouts by 25.3% with similar benefits.

**Wall-clock improvements:** DARS-ET reduces training time by 35.8%, while DARS-HW achieves 14.1% speedup despite better Pass@K outcomes.

## Breadth Effects on Exploration

Increased batch size (128→3072) sustains token-level entropy throughout training, preventing premature convergence. The paper notes that "breadth acts as implicit entropy regularization," enabling robust exploration independent of rollout count increases.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21d13828-1e71-462f-8626-8d3585d00cbf",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "9e04d4e4-9eef-43ff-9495-4cb735fd6e49",
  "sourceToolAssistantUUID": "21d13828-1e71-462f-8626-8d3585d00cbf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-28T01:27:48.144Z_

Now let me search for more specific evidence on both topics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e04d4e4-9eef-43ff-9495-4cb735fd6e49",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6eunhYFgzbjJwgmFRr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0c3d4e6e-9887-4245-8565-52fd2ee6da99",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PBGsEBo7k1duR1F6VYsyZM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2725,
      "cache_read_input_tokens": 14110,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2725,
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

_source line 30 · 2026-05-28T01:27:48.830Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018HmuPv9tz8yuG38wnW5tFx`</summary>

```json
{
  "query": "training distribution diversity RL LLM capability activation coverage \"base model\" reinforcement learning reasoning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c3d4e6e-9887-4245-8565-52fd2ee6da99",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6eunhYFgzbjJwgmFRr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c6bf1d9a-6177-4bf4-9336-c25cb3fc9ab9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PBGsEBo7k1duR1F6VYsyZM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2725,
      "cache_read_input_tokens": 14110,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2725,
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

_source line 31 · 2026-05-28T01:27:49.723Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EszbbM4MJieohUdhKGLp9X`</summary>

```json
{
  "query": "DUMP automated distribution curriculum learning RL LLM post-training arXiv 2504.09710"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6bf1d9a-6177-4bf4-9336-c25cb3fc9ab9",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6eunhYFgzbjJwgmFRr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2741e061-c896-4efc-bb8e-0db0d95d007b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PBGsEBo7k1duR1F6VYsyZM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2725,
      "cache_read_input_tokens": 14110,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2725,
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

_source line 32 · 2026-05-28T01:27:50.664Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017AeJAL3uG7usyDQcbri4J3`</summary>

```json
{
  "query": "\"limit of RLVR\" base model ceiling capability coverage training distribution"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2741e061-c896-4efc-bb8e-0db0d95d007b",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6eunhYFgzbjJwgmFRr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "30e23b35-fbff-4857-a77a-ac35560b57aa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PBGsEBo7k1duR1F6VYsyZM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2725,
      "cache_read_input_tokens": 14110,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2725,
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

_source line 33 · 2026-05-28T01:27:51.235Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B7KGoJzMihjMA9Ua5bj9e8`</summary>

```json
{
  "query": "rollout count sample size binary reward estimation variance GRPO RLVR statistical power"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30e23b35-fbff-4857-a77a-ac35560b57aa",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6eunhYFgzbjJwgmFRr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d54c8521-af9b-404c-a99a-ed5023c7224b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PBGsEBo7k1duR1F6VYsyZM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2725,
      "cache_read_input_tokens": 14110,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2725
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 249,
          "cache_read_input_tokens": 14110,
          "cache_creation_input_tokens": 2725,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2725,
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

_source line 34 · 2026-05-28T01:27:58.880Z_

<details><summary>↩ Tool result · `toolu_01EszbbM4MJieohUdhKGLp9X`</summary>

```text
Web search results for query: "DUMP automated distribution curriculum learning RL LLM post-training arXiv 2504.09710"

Links: [{"title":"DUMP: Automated Distribution-Level Curriculum Learning for RL-based LLM Post-training | alphaXiv","url":"https://www.alphaxiv.org/abs/2504.09710"},{"title":"[2504.09710] DUMP: Automated Distribution-Level Curriculum Learning for RL-based LLM Post-training","url":"https://arxiv.org/abs/2504.09710"},{"title":"[2504.09710v1] DUMP: Automated Distribution-Level Curriculum Learning for RL-based LLM Post-training","url":"https://arxiv.org/abs/2504.09710v1"},{"title":"Automated Curriculum Learning Improves Efficiency of Large Language Model Post-Training","url":"https://www.getaiverse.com/post/automatisiertes-curriculum-learning-fuer-effizienteres-post-training-von-grossen-sprachmodellen"},{"title":"GitHub - ZhentingWang/DUMP","url":"https://github.com/ZhentingWang/DUMP"},{"title":"[PDF] DUMP: Automated Distribution-Level Curriculum Learning for RL-based LLM Post-training | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DUMP:-Automated-Distribution-Level-Curriculum-for-Wang-Cui/4e0016dd49b44e07c50f8adea6ea8c21bc4c0b1e"},{"title":"DUMP: Automated Distribution-Level Curriculum Learning for RL-based LLM Post-training","url":"https://arxiv.org/html/2504.09710v1"},{"title":"Paper page - DUMP: Automated Distribution-Level Curriculum Learning for RL-based LLM Post-training","url":"https://huggingface.co/papers/2504.09710"}]

I found the paper! Here's what I found about DUMP (arXiv 2504.09710):

## Overview

Recent advances in reinforcement learning (RL)-based post-training have led to notable improvements in large language models (LLMs), particularly in enhancing their reasoning capabilities to handle complex tasks. However, most existing methods treat the training data as a unified whole, overlooking the fact that modern LLM training often involves a mixture of data from diverse distributions-varying in both source and difficulty. This heterogeneity introduces a key challenge: how to adaptively schedule training across distributions to optimize learning efficiency.

## The Approach

The paper presents a principled curriculum learning framework grounded in the notion of distribution-level learnability. The core insight is that the magnitude of policy advantages reflects how much a model can still benefit from further training on a given distribution. The framework leverages the Upper Confidence Bound (UCB) principle to dynamically adjust sampling probabilities for different distributions, yielding an adaptive and theoretically grounded training schedule.

## Implementation and Results

DUMP is a plug-and-play curriculum learning module for RL-based LLM post-training that automatically prioritizes data distributions that are most beneficial for learning—based on live advantage signals from your model—and schedules them using a bandit-based UCB strategy. The results show that DUMP significantly improves the convergence speed and final performance.

The paper was authored by Zhenting Wang, Guofeng Cui, Kun Wan, and Wentian Zhao, and a GitHub repository is available with the implementation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2741e061-c896-4efc-bb8e-0db0d95d007b",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "d25be642-9697-43a5-9047-04ef5ef850ef",
  "sourceToolAssistantUUID": "2741e061-c896-4efc-bb8e-0db0d95d007b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-28T01:27:59.625Z_

<details><summary>↩ Tool result · `toolu_017AeJAL3uG7usyDQcbri4J3`</summary>

```text
Web search results for query: ""limit of RLVR" base model ceiling capability coverage training distribution"

Links: [{"title":"Limit of RLVR","url":"https://limit-of-rlvr.github.io/"},{"title":"The Invisible Leash? Why RLVR May or May Not Escape Its Origin","url":"https://arxiv.org/html/2507.14843v2"},{"title":"Tsinghua paper: Does RL Really Incentivize Reasoning ...","url":"https://www.lesswrong.com/posts/s3NaETDujoxj4GbEm/tsinghua-paper-does-rl-really-incentivize-reasoning-capacity"},{"title":"Papers Explained 354: Does RL Incentivize Reasoning Capacity in LLMs Beyond the Base Model? | by Ritvik Rastogi | Medium","url":"https://ritvik19.medium.com/papers-explained-354-does-rl-incentivize-reasoning-capacity-in-llms-beyond-the-base-model-77ae394a5054"},{"title":"[2504.13837] Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?","url":"https://arxiv.org/abs/2504.13837"},{"title":"GitHub - LeapLabTHU/limit-of-RLVR: repo for paper https://arxiv.org/abs/2504.13837 · GitHub","url":"https://github.com/LeapLabTHU/limit-of-RLVR"},{"title":"RL-PLUS: Countering Capability Boundary Collapse of LLMs in Reinforcement Learning with Hybrid-policy Optimization","url":"https://arxiv.org/html/2508.00222v1"},{"title":"RL's impact on LLM reasoning abilities beyond base models - CO/AI","url":"https://getcoai.com/news/rls-impact-on-llm-reasoning-abilities-beyond-base-models/"},{"title":"limit-of-RLVR/README.md at main · LeapLabTHU/limit-of-RLVR","url":"https://github.com/LeapLabTHU/limit-of-RLVR/blob/main/README.md"},{"title":"The Debate on RLVR Reasoning Capability Boundary: Shrinkage, Expansion, or Both? A Two-Stage Dynamic View","url":"https://arxiv.org/html/2510.04028v1"}]

Based on the search results, I can provide you with comprehensive information about the limits of RLVR (Reinforcement Learning with Verifiable Rewards) regarding base model ceiling capability and training distribution coverage.

## Key Findings on RLVR Limits

**Base Model Ceiling Capability:**

The RLVR-trained model cannot exceed the base model's pass@k in the limit—this asymptotic upper bound captures a ceiling that no matter how many samples are drawn, remains constrained. If LLMs are to solve truly harder problems beyond pretraining, a new training paradigm may be needed that can go beyond the base model's ceiling.

**Training Distribution Coverage:**

All correct solutions from RL-trained models already exist in the base model's distribution, proving RLVR enhances sampling efficiency, not reasoning capacity, while inadvertently shrinking the solution space. On-policy sampling means the model updates only from what it already samples — lacking representational coverage means no gradient can ever push probability mass toward truly unseen solutions. Even when rewards provide a clear training signal, RLVR cannot access or discover solutions that the base model assigns zero probability.

**Capability Boundary Effects:**

Base models surpass RL at large pass@k. RL-trained variants shine at low sampling budgets, yet the original base models consistently overtake them as k increases. RL narrows exploration. Rewarded trajectories are amplified, but the broader solution space shrinks, revealing that RLVR optimizes within, rather than beyond, the base distribution.

The research systematically demonstrates that current RLVR approaches are fundamentally limited by the base model's original capabilities and cannot generate novel reasoning patterns beyond what the base model can already produce.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30e23b35-fbff-4857-a77a-ac35560b57aa",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "17859f86-0974-4439-83fa-9a232633bc0b",
  "sourceToolAssistantUUID": "30e23b35-fbff-4857-a77a-ac35560b57aa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-28T01:27:59.971Z_

<details><summary>↩ Tool result · `toolu_01B7KGoJzMihjMA9Ua5bj9e8`</summary>

```text
Web search results for query: "rollout count sample size binary reward estimation variance GRPO RLVR statistical power"

Links: [{"title":"Discounted Beta--Bernoulli Reward Estimation for Sample-Efficient Reinforcement Learning with Verifiable Rewards","url":"https://arxiv.org/pdf/2603.18444"},{"title":"GRPO-based Reinforcement Learning","url":"https://www.emergentmind.com/topics/grpo-based-reinforcement-learning"},{"title":"It Takes Two: Your GRPO Is Secretly DPO","url":"https://arxiv.org/html/2510.00977v3"},{"title":"Reinforcement Learning with Verifiable Rewards: GRPO’s Effective Loss, Dynamics, and Success Amplification","url":"https://arxiv.org/html/2503.06639v1"},{"title":"Improving Sampling Efficiency in RLVR through Adaptive Rollout and Response Reuse","url":"https://arxiv.org/html/2509.25808v1"},{"title":"Shrinking the Variance: Shrinkage Baselines for Reinforcement Learning with Verifiable Rewards","url":"https://arxiv.org/pdf/2511.03710"},{"title":"Reinforcement Learning with Verifiable Rewards Makes Models Faster, Not Smarter | Promptfoo","url":"https://www.promptfoo.dev/blog/rlvr-explained/"},{"title":"Rollout Pass-Rate Control: Steering Binary-Reward RL Toward Its Most Informative Regime","url":"https://arxiv.org/html/2605.05112"},{"title":"Generalized Relative Policy Optimization (GRPO)","url":"https://www.emergentmind.com/topics/generalized-relative-policy-optimization-grpo"},{"title":"Improving Sampling Efficiency in RLVR through Adaptive ...","url":"https://arxiv.org/pdf/2509.25808"}]

I found relevant search results on this topic. Here's what the research shows:

## Rollout Count and Sample Size in GRPO/RLVR

RL training on LLMs typically operates with large batch sizes but fewer rollouts per prompt due to the high cost of inference, with the number of rollouts per prompt often limited to 16 or fewer even in industrial-scale LLM training.

GRPO estimates the advantage using Monte Carlo rollouts rather than a learned critic, with statistics estimated from a "group" of Monte Carlo rollouts corresponding to samples from the LLM policy conditioned on a single input.

## Variance and Binary Reward Estimation

Group-relative advantage—whitening returns within a mini-batch or per-context group—yields lower variance and effective learning signals, especially under binary or sparse reward settings typical in RL with verifiable rewards (RLVR).

Accurately estimating the baseline becomes difficult when the number of samples is small, but recognizing that value functions must be estimated simultaneously across all prompts in a batch enables construction of an estimator with strictly lower mean squared error (MSE).

## Statistical Power and Pass-Rate Control

A 50% rollout pass rate maximizes reward entropy, group-filtering survival, RLOO advantage energy under GRPO, and success–failure pair count. The binary reward-side signal is strongest near a 50% rollout pass rate under four criteria: reward entropy, group-filtering survival, leave-one-out (RLOO) advantage energy under GRPO, and success–failure pair count.

The research indicates that sample efficiency and variance control are critical challenges in GRPO-based RLVR systems, with practical solutions involving shrinkage estimation, pass-rate control, and careful consideration of group size and composition.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d54c8521-af9b-404c-a99a-ed5023c7224b",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "9a96f282-2e15-4635-a190-f010647c54fd",
  "sourceToolAssistantUUID": "d54c8521-af9b-404c-a99a-ed5023c7224b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-28T01:28:00.690Z_

<details><summary>↩ Tool result · `toolu_018HmuPv9tz8yuG38wnW5tFx`</summary>

```text
Web search results for query: "training distribution diversity RL LLM capability activation coverage "base model" reinforcement learning reasoning 2025 2026"

Links: [{"title":"Reinforcement Learning Meets Large Language Models: A Survey of","url":"https://arxiv.org/pdf/2509.16679"},{"title":"Reinforcement Learning Meets Large Language Models: A Survey of Advancements and Applications Across the LLM Lifecycle","url":"https://arxiv.org/html/2509.16679v1"},{"title":"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? | OpenReview","url":"https://openreview.net/forum?id=4OsgYD7em5"},{"title":"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?","url":"https://arxiv.org/pdf/2504.13837"},{"title":"Reasoning with Sampling: Your Base Model is Smarter Than You Think","url":"https://arxiv.org/pdf/2510.14901"},{"title":"RL-PLUS: Countering Capability Boundary Collapse of LLMs in Reinforcement Learning with Hybrid-policy Optimization","url":"https://arxiv.org/html/2508.00222"}]

Based on the web search results, I found several highly relevant academic papers from 2025-2026 addressing your query about training distribution diversity, RL, LLM capability activation, coverage, base models, and reinforcement learning reasoning:

## Key Findings

**Capability Limitation vs. Activation:**
Analysis of coverage and perplexity indicates that all reasoning paths generated by RLVR exist in the sampling distribution of the base model, suggesting that its capabilities are inherently derived from and limited by the base model. While RLVR improves sampling efficiency towards correct paths, current training does not elicit fundamentally new reasoning patterns.

**Distribution Diversity Collapse:**
Current RL-posttraining exhibits a collapse in diversity over multiple samples. This is particularly evident in pass@k evaluations where while RLVR-trained models outperform their base models at smaller values of k, base models achieve higher pass@k score when k is large.

**Recent Solutions:**
RL-PLUS effectively resolves the capability boundary collapse problem and represents advances in the RLVR paradigm for improving reasoning performance in LLMs. Additionally, alternative sampling methods avoid the collapse in diversity characteristic of RL-posttraining and do not require training, curated datasets, or a verifier.

**Base Model Capacity:**
Several studies from 2025 have pointed out that the reflective behavior in RLVR models stems from the base model itself, rather than being acquired through reinforcement learning.

These findings suggest a major research focus in 2025-2026 on understanding whether RL truly activates new capabilities or simply optimizes existing ones in the base model's distribution.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6bf1d9a-6177-4bf4-9336-c25cb3fc9ab9",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "2a80498e-2f1d-4b7d-a958-97084f3ddc17",
  "sourceToolAssistantUUID": "c6bf1d9a-6177-4bf4-9336-c25cb3fc9ab9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-28T01:28:03.192Z_

Excellent findings. Now let me fetch more details from several key papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a80498e-2f1d-4b7d-a958-97084f3ddc17",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6g27EoNm5pBXNJm48d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "62bc6bd4-031e-4723-8cd6-980ab1133bcf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014BUXn1t53b4qzBCcmpTL85",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2839,
      "cache_creation_input_tokens": 978,
      "cache_read_input_tokens": 16835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 978,
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

_source line 39 · 2026-05-28T01:28:06.469Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013QpJUaHNPmj2Y4nxiewXTS`</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.13837",
  "prompt": "Extract the full abstract and key findings. Specifically what do they say about: (1) coverage analysis showing RLVR paths exist in base model distribution, (2) capability ceiling, (3) pass@k analysis showing base models eventually overtake RL models, (4) any discussion of whether training distribution diversity could push the ceiling. Include specific numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62bc6bd4-031e-4723-8cd6-980ab1133bcf",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6g27EoNm5pBXNJm48d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aadeae70-9ea6-4849-9dba-26cc7a83d1a4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014BUXn1t53b4qzBCcmpTL85",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2839,
      "cache_creation_input_tokens": 978,
      "cache_read_input_tokens": 16835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 978,
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

_source line 40 · 2026-05-28T01:28:08.841Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Rha1T7hQjVJpAbEi2xR7is`</summary>

```json
{
  "url": "https://arxiv.org/html/2504.09710v1",
  "prompt": "Extract key findings about: (1) How distribution-level scheduling affects RL training outcomes, (2) evidence that different data distributions contribute differently to learning, (3) any results showing that broader/more diverse distributions improve final performance, (4) the UCB-based approach for balancing exploration across distributions. Provide specific numbers and quotes about how distribution scheduling matters."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aadeae70-9ea6-4849-9dba-26cc7a83d1a4",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6g27EoNm5pBXNJm48d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b07de84-89f6-44a6-9cca-a1d2137b3db6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014BUXn1t53b4qzBCcmpTL85",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2839,
      "cache_creation_input_tokens": 978,
      "cache_read_input_tokens": 16835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 978,
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

_source line 41 · 2026-05-28T01:28:11.338Z_

<details><summary>↩ Tool result · `toolu_013QpJUaHNPmj2Y4nxiewXTS`</summary>

```text
# Research Summary: RLVR and LLM Reasoning Capacity

## Full Abstract

The paper examines whether Reinforcement Learning with Verifiable Rewards (RLVR) actually develops novel reasoning abilities in LLMs. The study tests RLVR across multiple model families and algorithms using pass@k metrics. Key finding: "the current training setup does not elicit fundamentally new reasoning patterns." While RLVR models outperform base models at k=1, base models achieve higher pass@k scores at larger k values.

## Key Findings

**Coverage and Distribution Analysis:**
The research demonstrates that "the observed reasoning abilities originate from and are bounded by the base model." This indicates RLVR isn't discovering novel pathways but rather optimizing existing ones within the base model's learned distribution.

**Capability Ceiling:**
Treating the base model as an upper bound, the analysis shows "six popular RLVR algorithms perform similarly and remain far from optimal in leveraging the potential of the base model."

**Pass@k Performance Differential:**
While RLVR models excel at k=1, base models eventually outperform them at larger k values—a critical finding suggesting RLVR improves sampling efficiency rather than expanding genuine reasoning capacity.

**Training Distribution Diversity:**
The paper doesn't discuss whether increased distribution diversity could push the capability ceiling. Instead, it recommends "improved RL paradigms, such as continual scaling and multi-turn agent-environment interaction" as necessary alternatives.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aadeae70-9ea6-4849-9dba-26cc7a83d1a4",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "7ae34887-d255-4b83-bfa0-cf085e2d37db",
  "sourceToolAssistantUUID": "aadeae70-9ea6-4849-9dba-26cc7a83d1a4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-28T01:28:12.593Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DD2XzKkdckB6M7NsKNNwAf`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.06241",
  "prompt": "Extract detailed findings about: (1) exactly how the 1-3% of tokens are identified, (2) what types of decisions these tokens represent, (3) any discussion of whether different training distributions would cause RL to select different subsets of behaviors, (4) the entropy analysis showing where RL intervenes, (5) any limitations or caveats the authors mention about the \"selection not learning\" framing. Provide specific quotes and section references."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ae34887-d255-4b83-bfa0-cf085e2d37db",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6g27EoNm5pBXNJm48d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1e54ec9-5915-4b5e-bf64-3345b3f7e9b8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014BUXn1t53b4qzBCcmpTL85",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2839,
      "cache_creation_input_tokens": 978,
      "cache_read_input_tokens": 16835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 978,
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

_source line 43 · 2026-05-28T01:28:14.475Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LPvDAUkEDPVFzYBx9cKYzS`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.05112",
  "prompt": "Extract key findings about: (1) how rollout pass rate affects training signal quality, (2) the statistical argument for why 50% pass rate is optimal, (3) any quantitative results showing the effect of different rollout counts on training, (4) the relationship between sample size and binary reward estimation reliability. Include specific formulas, numbers, and quotes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1e54ec9-5915-4b5e-bf64-3345b3f7e9b8",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6g27EoNm5pBXNJm48d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "92c4165b-32d1-422e-8e82-99ca7f326541",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014BUXn1t53b4qzBCcmpTL85",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2839,
      "cache_creation_input_tokens": 978,
      "cache_read_input_tokens": 16835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 978,
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

_source line 44 · 2026-05-28T01:28:16.340Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AdHNBi6LLai5gwqsvbYqWY`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.00222",
  "prompt": "Extract key findings about capability boundary collapse in RL training. Specifically: (1) what causes the collapse, (2) how does it relate to training distribution diversity, (3) what is the proposed solution, (4) any evidence that broader training distributions help preserve more base model capabilities. Provide specific quotes and numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92c4165b-32d1-422e-8e82-99ca7f326541",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6g27EoNm5pBXNJm48d",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3638ee38-c667-4863-94be-520b44b58370",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014BUXn1t53b4qzBCcmpTL85",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2839,
      "cache_creation_input_tokens": 978,
      "cache_read_input_tokens": 16835,
      "output_tokens": 747,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 978
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2839,
          "output_tokens": 747,
          "cache_read_input_tokens": 16835,
          "cache_creation_input_tokens": 978,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 978,
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

_source line 45 · 2026-05-28T01:28:16.906Z_

<details><summary>↩ Tool result · `toolu_01Rha1T7hQjVJpAbEi2xR7is`</summary>

```text
# Distribution-Level Scheduling in RL-based LLM Post-training

## 1. Impact on Training Outcomes

The research demonstrates substantial improvements from distribution-aware scheduling. Across 12 distinct puzzle difficulty levels, DUMP "consistently outperforms the baseline, achieving faster convergence and higher test performance." In mid-to-high difficulty distributions (6-12 characters), gains were particularly pronounced—for the 9-character distribution, DUMP achieved test reward above 0.5 while the uniform baseline remained below 0.0.

## 2. Differential Contribution Across Distributions

The paper provides empirical evidence that distributions have varying learning value. The absolute advantage metric serves as "a proxy for distribution-level learnability," capturing how much remaining improvement potential exists within each data source. The key insight: "high advantages on specific data distribution indicate underfitting and high potential for improvement on it, while low advantages suggest diminishing returns."

## 3. Diversity and Broader Distribution Effects

While the experiments focus on a single dataset type (Knights & Knaves puzzles), the framework explicitly addresses heterogeneous training. The authors note that modern LLM training involves "a mixture of data from diverse distributions—varying in both source and difficulty," with examples including "factual QA to math problems and coding tasks." However, the paper doesn't quantify performance gains from broader diversity—only from adaptive scheduling within existing distributions.

## 4. UCB-Based Exploration-Exploitation Balance

DUMP employs Upper Confidence Bound scoring: `UCB(dj) = L̂(dj) + √(2log(ntotal+1)/(ndj+1))`. This formula balances two components—the first term "encourages exploitation of distributions with high observed advantages," while the second ensures "sufficient exploration of rarely sampled distributions." The softmax temperature parameter (τ=0.1) controls sharpness, where lower values concentrate sampling on high-scoring distributions.

The theoretical guarantee shows regret scales as O(log T/Δj), demonstrating logarithmic efficiency in training budget allocation across suboptimal distributions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b07de84-89f6-44a6-9cca-a1d2137b3db6",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "56f0efa9-55a5-498c-a868-16a96649f1f9",
  "sourceToolAssistantUUID": "2b07de84-89f6-44a6-9cca-a1d2137b3db6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-28T01:28:23.331Z_

<details><summary>↩ Tool result · `toolu_01DD2XzKkdckB6M7NsKNNwAf`</summary>

```text
# Key Findings on RL's Token Selection Mechanism

## (1) Identification of the 1-3% of Tokens

The paper identifies these critical tokens through **entropy-gated analysis**. As stated in Section 3.1: "Only 1.0–4.1% of all token positions are reranked" and "the reranked positions have 5–12× higher base-model entropy than unchanged positions."

The identification method relies on token-level entropy (Equation 2), where positions exceeding a threshold τ are marked as decision points. Section 3.3 demonstrates that "base-model entropy, which peaks at the positions RL edits, provides a strong proxy for where intervention is useful."

## (2) Types of Decisions These Tokens Represent

The authors characterize these as **reasoning branch points**. The paper states: "high-entropy _decision points_ where the model is uncertain which reasoning branch to take" (Introduction). 

Critically, the promoted tokens are conservative—"The teacher's preferred token is, on average, the second most likely token under the base model (mean rank 2.14–2.39)" (Section 3.1). The paper emphasizes: "RL does not introduce novel tokens; it consistently elevates one of the base model's top alternatives at moments of uncertainty."

## (3) Training Distribution Sensitivity

The authors address this through their **problem selection strategy** (Section 5.1). They filter for problems where "the base model's pass rate lies strictly between 0 and 1: some rollouts are correct, others are incorrect."

Importantly, they acknowledge dependency on competence regions: "Only the mixed‑success regime supplies the two‑sided contrastive signal" (Section 5.1). However, they don't extensively discuss whether different distributions would select fundamentally different token subsets—a notable limitation of their analysis.

## (4) Entropy Analysis of RL Intervention Sites

Section 3.1 provides quantitative evidence. Table 2 shows entropy ratios: reranked positions have "7.58× to 12.63× higher entropy than unchanged positions" across different model pairs.

Figure 2 demonstrates that "entropy‑gated correction" using only the base model's entropy threshold τ achieves comparable accuracy to oracle intervention, confirming entropy as a predictor.

## (5) Limitations and Caveats

The authors acknowledge several constraints:

- **Scope limitation**: "We focus on the four base/RL‑tuned pairs" (Section 3) and mathematical reasoning specifically
- **Threshold sensitivity**: Figure 4 shows performance varies with τ, though the authors claim it's "robust over a broad range"
- **Generalization uncertainty**: The paper notes results are "on math reasoning benchmarks" without confirming applicability to other domains
- **Parameter space assumptions**: While showing RL's correction is low-dimensional in adapters, they don't claim this necessarily reflects the underlying learning mechanism

The "selection not learning" framing itself carries an implicit caveat: the paper demonstrates RL selects from existing model capacity but doesn't fully prove whether base models genuinely contain all necessary reasoning patterns or merely high-probability approximations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1e54ec9-5915-4b5e-bf64-3345b3f7e9b8",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "418a88b8-a9a5-4764-9ba6-6ec39a7869e3",
  "sourceToolAssistantUUID": "a1e54ec9-5915-4b5e-bf64-3345b3f7e9b8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-28T01:28:24.057Z_

<details><summary>↩ Tool result · `toolu_01AdHNBi6LLai5gwqsvbYqWY`</summary>

```text
# Capability Boundary Collapse in RL Training

## What Causes the Collapse

The paper identifies that existing RLVR methods suffer from "an essential challenge": models face "an extremely immense" solution space with sparse rewards that prevent effective exploration of new reasoning pathways. The fundamental issue is that "the model is compelled to focus on inward exploitation" rather than discovering genuinely novel abilities.

As the authors explain: "Although the pass@1 performance of RLVR-trained models surpasses that of the base model, its pass@128 metric is substantially lower." This indicates the method narrows rather than expands the model's problem-solving scope.

## Relationship to Training Distribution Diversity

The collapse stems directly from limited exposure to diverse training distributions. Current methods rely on "an essentially on-policy strategy coupled with LLM's immense action space and sparse reward," creating a reinforcement loop where models optimize existing knowledge rather than acquire new capabilities.

The paper demonstrates that when models train exclusively on self-generated trajectories, "policy entropy sharply decreases during training, making the model overly deterministic and hindering further exploration."

## Proposed Solution: RL-PLUS

The method combines two techniques:

1. **Multiple Importance Sampling** to stabilize learning from external data despite distribution mismatch
2. **Exploration-Based Advantage Function** that "prioritizes advantages for reasoning paths that are correct but are hard to explore (i.e., low probability) under the current policy"

## Evidence That Broader Distributions Preserve Capabilities

Pass@k curve analysis provides compelling evidence. The paper shows that "RL-PLUS maintains a consistent performance advantage over both the base model and GRPO as k-values increase," whereas baseline GRPO "performance curve gradually converges with that of the base model as k increases."

Quantitatively, RL-PLUS achieved "average relative improvements of GRPO up to 69.2%" across diverse model families, with "state-of-the-art performance on six math reasoning benchmarks."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3638ee38-c667-4863-94be-520b44b58370",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "fd125d44-5876-4596-be79-01f9f1c80ab4",
  "sourceToolAssistantUUID": "3638ee38-c667-4863-94be-520b44b58370",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-28T01:28:24.964Z_

<details><summary>↩ Tool result · `toolu_01LPvDAUkEDPVFzYBx9cKYzS`</summary>

```text
# Key Findings on Rollout Pass Rate and Training Signal Quality

## (1) How Rollout Pass Rate Affects Training Signal Quality

The paper demonstrates that highly skewed rollout groups—where most attempts succeed or fail—provide weak learning signals. The authors identify this through four complementary measures that all peak at 50% pass rate:

- **Reward entropy** maximizes at p=0.5, reaching 1.0 bit
- **Group-filtering survival** (probability a group isn't discarded) peaks at p=0.5
- **RLOO advantage energy** in GRPO maximizes when k=N/2 successes occur
- **Success-failure contrastive pairs** are maximized at balanced outcomes

In their N=8 rollout setting, skewed 1/8 or 7/8 groups provide only ~54% of the information content and ~44% of contrastive pairs compared to balanced 4/8 groups.

## (2) Statistical Argument for 50% Optimality

The derivation rests on fundamental information theory. For binary rewards with pass probability p:

**Entropy formula**: H(p) = −p log₂(p) − (1−p) log₂(1−p)

Taking derivatives yields dH/dp = log₂((1−p)/p), which equals zero only when p=0.5. The second derivative is negative across (0,1), confirming a unique maximum.

For group filtering specifically, non-degenerate group probability is 1−p^N−(1−p)^N, which the authors prove is uniquely maximized at p=0.5.

As the authors note: "Four complementary quantities...all identify the same target: training is most informative when rollout pass rates are close to 50%."

## (3) Quantitative Results for Different Rollout Counts

The paper uses N=8 rollouts throughout. For this setting, **Table 12** shows exact contrastive-pair counts:

| Pass Rate | Pair Count | Relative to Max |
|-----------|-----------|-----------------|
| 1/8       | 7         | 44%             |
| 2/8       | 12        | 75%             |
| 4/8       | 16        | 100%            |
| 7/8       | 7         | 44%             |

For filtering, at p=0.5 with N=8, groups survive filtering 99.22% of the time versus 65.64% at p=0.125.

## (4) Sample Size and Binary Reward Estimation Reliability

While the paper doesn't explicitly model estimation variance as a function of sample size, it implicitly addresses this through the filtering survival analysis. The probability a random group provides usable contrast—avoiding all-success or all-failure outcomes—depends critically on N and p.

The authors demonstrate empirically that their Prefix Sampling method moves observed rerollout groups toward balanced distributions: mean distance from 4/8 decreased from 2.94 to 2.38, with target-band (3/8–5/8) share increasing from 18.6% to 29.1%.

The controller uses exponential moving average feedback (α=0.05, ~13.5 update half-life) to adapt per-bucket prefix ratios, showing that maintaining 50% balance requires continuous adjustment as model capability drifts during training.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92c4165b-32d1-422e-8e82-99ca7f326541",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "f8e0d2ae-3b85-45de-b688-24be32ff5a9a",
  "sourceToolAssistantUUID": "92c4165b-32d1-422e-8e82-99ca7f326541",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-28T01:28:28.412Z_

Now let me get more specific evidence for the counter-argument on Topic 1 and additional rollout count evidence.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8e0d2ae-3b85-45de-b688-24be32ff5a9a",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6hoynkbQZ8rhYjS2Sf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "213b182a-39a2-4062-b074-bf58af75c0b9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017rSziK1be6q3aBBJ3KCh6b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 483,
      "cache_creation_input_tokens": 5979,
      "cache_read_input_tokens": 17813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5979,
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

_source line 50 · 2026-05-28T01:28:29.821Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XUXsiMw1Sut8cKxbNfc8w1`</summary>

```json
{
  "query": "RL training diversity selects different base model behaviors capability coverage primitive activation reasoning LLM arXiv 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "213b182a-39a2-4062-b074-bf58af75c0b9",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6hoynkbQZ8rhYjS2Sf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e0e6d3cc-2652-4b18-a9fe-08a7856e97e4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017rSziK1be6q3aBBJ3KCh6b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 483,
      "cache_creation_input_tokens": 5979,
      "cache_read_input_tokens": 17813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5979,
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

_source line 51 · 2026-05-28T01:28:30.806Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0123QjGbKgQz4QKJ6CToSTrd`</summary>

```json
{
  "query": "\"Tailor\" primitive-oriented reinforcement learning warm-start data novel reasoning primitives coverage"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0e6d3cc-2652-4b18-a9fe-08a7856e97e4",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6hoynkbQZ8rhYjS2Sf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "66847609-2832-478b-85fa-43ae42da353a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017rSziK1be6q3aBBJ3KCh6b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 483,
      "cache_creation_input_tokens": 5979,
      "cache_read_input_tokens": 17813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5979,
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

_source line 52 · 2026-05-28T01:28:31.819Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015u86SrhZMi6kNrnERJq9yS`</summary>

```json
{
  "query": "ProRL prolonged reinforcement learning diverse reasoning LLM scaling arXiv 2505.24864"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66847609-2832-478b-85fa-43ae42da353a",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6hoynkbQZ8rhYjS2Sf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a74a506b-e203-4b26-832b-a702080d5f76",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017rSziK1be6q3aBBJ3KCh6b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 483,
      "cache_creation_input_tokens": 5979,
      "cache_read_input_tokens": 17813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5979,
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

_source line 53 · 2026-05-28T01:28:32.462Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MPJ8b3yF1k4zHt2AbMWkW1`</summary>

```json
{
  "query": "shrinkage baseline GRPO variance rollout count advantage estimation arXiv 2511.03710"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a74a506b-e203-4b26-832b-a702080d5f76",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6hoynkbQZ8rhYjS2Sf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f554dfa-fad3-4e88-a127-8ddb4331ff1a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017rSziK1be6q3aBBJ3KCh6b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 483,
      "cache_creation_input_tokens": 5979,
      "cache_read_input_tokens": 17813,
      "output_tokens": 269,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5979
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 483,
          "output_tokens": 269,
          "cache_read_input_tokens": 17813,
          "cache_creation_input_tokens": 5979,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5979,
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

_source line 54 · 2026-05-28T01:28:37.098Z_

<details><summary>↩ Tool result · `toolu_01XUXsiMw1Sut8cKxbNfc8w1`</summary>

```text
Web search results for query: "RL training diversity selects different base model behaviors capability coverage primitive activation reasoning LLM arXiv 2025 2026"

Links: [{"title":"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? | OpenReview","url":"https://openreview.net/forum?id=4OsgYD7em5"},{"title":"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?","url":"https://arxiv.org/pdf/2504.13837"},{"title":"ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models","url":"https://arxiv.org/html/2505.24864v1"},{"title":"1 Introduction","url":"https://arxiv.org/html/2504.13837v1"},{"title":"Tailored Primitive Initialization is the Secret Key to Reinforcement Learning","url":"https://arxiv.org/pdf/2511.12429"},{"title":"Reinforcement Learning Meets Large Language Models: A Survey of Advancements and Applications Across the LLM Lifecycle","url":"https://arxiv.org/html/2509.16679v1"}]

I found relevant research on this topic. Here are the key findings:

## Main Research Findings

A systematic study probing reasoning capability boundaries of RL-trained LLMs across diverse model families and RL algorithms found that while RLVR improves sampling efficiency, current training does not elicit fundamentally new reasoning patterns.

The key finding is that all reasoning paths in the RLVR model are already present in the base model—RLVR training biases the distribution toward rewarded paths improving sampling efficiency, but this comes at the cost of reduced scope of reasoning capacity.

The reasoning capability boundary of LLMs often narrows as RLVR training progresses.

## Coverage and Diversity Analysis

Analysis of coverage and perplexity indicates that all reasoning paths generated by RLVR exist in the sampling distribution of the base model, suggesting that its capabilities are inherently derived from and limited by the base model.

## Related Work on Primitive Activation

One approach proposes a finetuning pipeline that automatically discovers and curates novel reasoning primitives to expand the coverage of reasoning-state distributions before RL, generating more diverse and higher-quality warm-start data resulting in higher downstream RL performance.

These papers (from arXiv 2025-2026) provide comprehensive analysis of how RL training interacts with base model behaviors and the importance of diversity in initialization for improving RL effectiveness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0e6d3cc-2652-4b18-a9fe-08a7856e97e4",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "58dbe0a2-8deb-4469-8a1c-b0f7e2606f5a",
  "sourceToolAssistantUUID": "e0e6d3cc-2652-4b18-a9fe-08a7856e97e4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-28T01:28:37.255Z_

<details><summary>↩ Tool result · `toolu_0123QjGbKgQz4QKJ6CToSTrd`</summary>

```text
Web search results for query: ""Tailor" primitive-oriented reinforcement learning warm-start data novel reasoning primitives coverage"

Links: [{"title":"Tailored Primitive Initialization is the Secret Key to Reinforcement Learning","url":"https://arxiv.org/pdf/2511.12429"},{"title":"Tailored Primitive Initialization is the Secret Key to Reinforcement Learning","url":"https://arxiv.org/html/2511.12429v1"},{"title":"[Literature Review] Tailored Primitive Initialization is the Secret Key to Reinforcement Learning","url":"https://www.themoonlight.io/en/review/tailored-primitive-initialization-is-the-secret-key-to-reinforcement-learning"},{"title":"Tailored Primitive Initialization is the Secret Key to Reinforcement Learning | Request PDF","url":"https://www.researchgate.net/publication/397700530_Tailored_Primitive_Initialization_is_the_Secret_Key_to_Reinforcement_Learning"},{"title":"[2511.12429] Tailored Primitive Initialization is the Secret Key to Reinforcement Learning","url":"https://arxiv.org/abs/2511.12429"},{"title":"TAILORED PRIMITIVE INITIALIZATION IS THE SECRET ...","url":"https://openreview.net/pdf/ac9ed140b3a3bc0b1c76fe5fc61064f94bb59132.pdf"},{"title":"TAILORED PRIMITIVE INITIALIZATION IS THE SECRET KEY TO ...","url":"https://openreview.net/pdf?id=1tWqSvoeBd"}]

Based on the search results, I found comprehensive information about Tailor and its approach to primitive-oriented reinforcement learning:

## Tailor: Primitive-Oriented Reinforcement Learning

Tailor is a finetuning pipeline that automatically discovers and curates novel reasoning primitives, thereby expanding the coverage of reasoning-state distributions before RL.

### Key Insight

The key insight is that successful RL training in LLMs requires initializing models with reasoning primitives that offer high thinking trajectory coverage. Reasoning primitives refer to reasoning patterns (e.g., bottom-up reasoning, top-down reasoning, etc.), which fundamentally govern the reasoning token distribution.

### Problem Addressed

Most existing warm-start pipelines, where supervised fine-tuning (SFT) precedes the RL stage, include only a limited set of primitive patterns, such as rule-based traces or distilled target behaviors from the SFT dataset. However, these often exhibit low coverage of the reasoning token distribution, leading to inefficient exploration and slower RL improvement.

### Results

Extensive experiments on mathematical and logical reasoning benchmarks demonstrate that Tailor generates more diverse and higher-quality warm-start data, resulting in higher downstream RL performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66847609-2832-478b-85fa-43ae42da353a",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "ac9615d9-7e5c-46cf-b414-16697bf60251",
  "sourceToolAssistantUUID": "66847609-2832-478b-85fa-43ae42da353a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-28T01:28:37.257Z_

<details><summary>↩ Tool result · `toolu_015u86SrhZMi6kNrnERJq9yS`</summary>

```text
Web search results for query: "ProRL prolonged reinforcement learning diverse reasoning LLM scaling arXiv 2505.24864"

Links: [{"title":"[2505.24864] ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models","url":"https://arxiv.org/abs/2505.24864"},{"title":"ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2505.24864v1"},{"title":"ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=YPsJha5HXQ"},{"title":"Paper page - ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models","url":"https://huggingface.co/papers/2505.24864"},{"title":"ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/392314840_ProRL_Prolonged_Reinforcement_Learning_Expands_Reasoning_Boundaries_in_Large_Language_Models"},{"title":"ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models","url":"https://arxiv.org/pdf/2505.24864"},{"title":"ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2505.24864"},{"title":"ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models","url":"https://arxiv.org/html/2505.24864v1"}]

I've found the paper you're looking for. Here's what the research is about:

ProRL (Prolonged Reinforcement Learning) training can uncover novel reasoning strategies that are inaccessible to base models, even under extensive sampling. The methodology incorporates KL divergence control, reference policy resetting, and a diverse suite of tasks.

The paper addresses an important question: whether RL truly expands a model's reasoning capabilities or merely amplifies high-reward outputs already latent in the base model's distribution, and whether continually scaling up RL compute reliably leads to improved reasoning performance.

**Key Results:**

RL-trained models consistently outperform base models across a wide range of pass@k evaluations, including scenarios where base models fail entirely regardless of the number of attempts. Compared to DeepSeek-R1-1.5B, the authors achieved average pass@1 improvements of 14.7% on math benchmarks, 13.9% on coding, 54.8% on logic puzzles, 25.1% on STEM reasoning, and 18.1% on instruction-following tasks.

Using ProRL, the researchers developed Nemotron-Research-Reasoning-Qwen-1.5B, described as the world's best 1.5B reasoning model that matches or even surpasses the performance of DeepSeek-R1-7B across diverse benchmarks.

The paper was published on May 30, 2025, on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a74a506b-e203-4b26-832b-a702080d5f76",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "417907ff-690e-43f5-85da-88d7ba2b5cf4",
  "sourceToolAssistantUUID": "a74a506b-e203-4b26-832b-a702080d5f76",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-28T01:28:38.805Z_

<details><summary>↩ Tool result · `toolu_01MPJ8b3yF1k4zHt2AbMWkW1`</summary>

```text
Web search results for query: "shrinkage baseline GRPO variance rollout count advantage estimation arXiv 2511.03710"

Links: [{"title":"[2511.03710] Shrinking the Variance: Shrinkage Baselines for Reinforcement Learning with Verifiable Rewards","url":"https://arxiv.org/abs/2511.03710"},{"title":"BASIS: Batchwise Advantage Estimation from Single-Rollout Information Sharing for LLM Reasoning","url":"https://arxiv.org/html/2605.27293"},{"title":"EBPO: Empirical Bayes Shrinkage for Stabilizing Group- ...","url":"https://arxiv.org/pdf/2602.05165"},{"title":"Shrinking the Variance: Shrinkage Baselines for Reinforcement Learning with Verifiable Rewards","url":"https://arxiv.org/pdf/2511.03710"},{"title":"Blockwise Advantage Estimation for Multi-Objective RL with Verifiable Rewards","url":"https://arxiv.org/html/2602.10231"},{"title":"Shrinking the Variance: Shrinkage Baselines for Reinforcement Learning with Verifiable Rewards","url":"https://arxiv.org/html/2511.03710"},{"title":"EBPO: Empirical Bayes Shrinkage for Stabilizing Group-Relative Policy Optimization","url":"https://arxiv.org/html/2602.05165"},{"title":"[2511.18902] VADE: Variance-Aware Dynamic Sampling via Online Sample-Level Difficulty Estimation for Multimodal RL","url":"https://arxiv.org/abs/2511.18902"}]

Based on the search results, here's information about arXiv paper 2511.03710:

## Paper Overview

The paper focuses on Reinforcement Learning with Verifiable Rewards (RLVR), a paradigm for post-training large reasoning models using policy-gradient methods such as GRPO.

## Main Problem and Solution

To stabilize training, these methods typically center trajectory rewards by subtracting the empirical mean reward for each prompt, which acts as a control variate (baseline) that reduces the variance of the policy-gradient estimator. However, the mean reward is estimated using per-prompt empirical averages computed from the generations for each prompt in a batch.

Motivated by Stein's paradox, the paper proposes shrinkage estimators that combine per-prompt and across-prompt means to improve per-prompt mean estimation accuracy, especially in the low-generation regime typical of RLVR. Theoretically, the paper constructs a shrinkage-based baseline that provably yields lower-variance policy-gradient estimators across algorithms.

The paper's title is "Shrinking the Variance: Shrinkage Baselines for Reinforcement Learning with Verifiable Rewards."


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f554dfa-fad3-4e88-a127-8ddb4331ff1a",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "01bcf9cd-6f5f-4a22-b774-b39f7ba87b8c",
  "sourceToolAssistantUUID": "7f554dfa-fad3-4e88-a127-8ddb4331ff1a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 58 · 2026-05-28T01:28:41.022Z_

Let me now fetch more detailed content from the most crucial papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01bcf9cd-6f5f-4a22-b774-b39f7ba87b8c",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6iq53jULRFun8K6atx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6cbfdfa1-6904-4a48-9b47-fa14e3ec908b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A5nu8x2FPRaX1oi9JKMo5U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3645,
      "cache_read_input_tokens": 23792,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3645,
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

_source line 59 · 2026-05-28T01:28:43.839Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JrbSNaMhL6QyXkCUMg5hkV`</summary>

```json
{
  "url": "https://arxiv.org/html/2511.12429v1",
  "prompt": "Extract key findings about: (1) how reasoning primitive coverage affects RL training outcomes, (2) what are the specific primitives they identify, (3) quantitative results showing that broader primitive coverage leads to better RL performance, (4) the relationship between training distribution diversity and primitive activation. Provide specific numbers and quotes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6cbfdfa1-6904-4a48-9b47-fa14e3ec908b",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6iq53jULRFun8K6atx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "918371bd-1f85-4d8e-a495-f92e65291eeb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A5nu8x2FPRaX1oi9JKMo5U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3645,
      "cache_read_input_tokens": 23792,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3645,
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

_source line 60 · 2026-05-28T01:28:46.191Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QjNaa1Ttbrv8PXPXURe2p6`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.24864v1",
  "prompt": "Extract key findings about: (1) evidence that RL can push beyond base model capability ceiling, (2) novel reasoning strategies discovered through prolonged RL, (3) the role of task diversity in expanding reasoning boundaries, (4) pass@k results showing RL models outperforming base models, (5) the mechanisms they identify for why prolonged diverse RL training expands capabilities. Provide specific numbers and quotes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "918371bd-1f85-4d8e-a495-f92e65291eeb",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6iq53jULRFun8K6atx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fca7e5d3-e2d5-4a24-9b11-9cca177b6cd2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A5nu8x2FPRaX1oi9JKMo5U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3645,
      "cache_read_input_tokens": 23792,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3645,
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

_source line 61 · 2026-05-28T01:28:48.653Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018ku2oBfsXMxUDUYZ5RWAkK`</summary>

```json
{
  "url": "https://arxiv.org/html/2511.03710",
  "prompt": "Extract findings about: (1) the variance problem with small rollout counts in GRPO, (2) specific quantitative analysis of how variance scales with number of rollouts/generations, (3) the shrinkage estimator approach, (4) any ablation results comparing different rollout counts. Provide specific formulas, numbers, and quotes about the variance-rollout relationship."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fca7e5d3-e2d5-4a24-9b11-9cca177b6cd2",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6iq53jULRFun8K6atx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ceca0ff8-6330-431a-8dff-6ebbc2b20c7f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A5nu8x2FPRaX1oi9JKMo5U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3645,
      "cache_read_input_tokens": 23792,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3645,
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

_source line 62 · 2026-05-28T01:28:50.767Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JYsFaDd8CEAc12VRbPTaBc`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.18444",
  "prompt": "Extract all findings about: (1) Beta-Bernoulli reward estimation for binary rewards, (2) how sample size affects reward estimation reliability, (3) any variance analysis or sample efficiency results, (4) comparison to standard GRPO reward estimation. Provide specific formulas and numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ceca0ff8-6330-431a-8dff-6ebbc2b20c7f",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6iq53jULRFun8K6atx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e2e239c-f3b8-40b1-81d4-6c3905bb50a5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A5nu8x2FPRaX1oi9JKMo5U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3645,
      "cache_read_input_tokens": 23792,
      "output_tokens": 592,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3645
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 592,
          "cache_read_input_tokens": 23792,
          "cache_creation_input_tokens": 3645,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3645,
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

_source line 63 · 2026-05-28T01:28:51.141Z_

<details><summary>↩ Tool result · `toolu_01JrbSNaMhL6QyXkCUMg5hkV`</summary>

```text
# Key Findings on Reasoning Primitive Coverage and RL Training

## 1. How Primitive Coverage Affects RL Training

The paper establishes that **thinking token distribution coverage is crucial for RL success**. The authors argue that "initializing LLMs with diverse, high-quality reasoning primitives is essential for achieving stable and sample-efficient RL training."

A critical insight: rule-based demonstrations achieve perfect accuracy yet fail to support effective RL. This demonstrates that "reasoning correctness in the SFT dataset alone does not guarantee RL success."

## 2. Specific Primitives Identified

The Tailor pipeline discovers primitives through failure analysis rather than hand-crafting. Examples include:
- **Top-Down and Bottom-Up reasoning** for mathematical problems
- **Self-verification and error recovery** strategies
- **Reflection and backtracking** behaviors
- **Subgoaling** patterns

Prior work (Gandhi et al. 2025) identified four critical primitives: verification, backtracking, backward chaining, and subgoaling.

## 3. Quantitative Results

**KK Task Results:**
- Tailor achieved the highest RL performance across both in-distribution and out-of-distribution evaluations
- Rule-based CoT baseline showed poor RL gains despite high SFT accuracy
- Figure 4 shows Tailor exhibits "faster learning and higher sampling efficiency"

**Diversity Metrics:**
- Tailor achieved lower median similarity scores compared to baselines (Figure 7)
- With 25 primitives versus 4, post-RL performance improved substantially (Figure 8a)
- Temperature ablation (Figure 8b) confirms higher diversity benefits RL across settings

## 4. Training Distribution Diversity and Primitive Activation

The paper demonstrates that broader primitive coverage improves "exploration and unlocking greater performance potential during RL tuning." The diversity analysis reveals that Tailor generates "higher-level reasoning diversity" with "a heavier tail in the low-similarity region," indicating more varied reasoning patterns activate during training.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "918371bd-1f85-4d8e-a495-f92e65291eeb",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "ecebc83f-ea43-4f1b-b6e4-03a4123c4deb",
  "sourceToolAssistantUUID": "918371bd-1f85-4d8e-a495-f92e65291eeb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-28T01:28:54.403Z_

<details><summary>↩ Tool result · `toolu_01QjNaa1Ttbrv8PXPXURe2p6`</summary>

```text
# Key Findings from ProRL Research

## (1) Evidence RL Pushes Beyond Base Model Capability Ceiling

The paper demonstrates tasks where base models completely fail but RL-trained models succeed. Most striking evidence: "many tasks where the base model fails to produce any correct solutions regardless of the amount of sampling, while our RL-trained model achieves 100% pass rates." On out-of-distribution tasks like boxnet, the base model showed zero capability while the ProRL model achieved 7.91% pass@1.

## (2) Novel Reasoning Strategies Discovered

The authors use the Creativity Index metric to measure solution novelty. They observe that "prolonged RL training leads to trajectories with higher novelty," indicating emergence of genuinely new reasoning patterns absent from pretraining data. Distribution shift analysis reveals dramatic transformations—for family_relationships tasks, performance shifted "from predominantly zero accuracy to peaking at perfect accuracy."

## (3) Task Diversity's Role in Expanding Boundaries

The training dataset spans 136K problems across five diverse domains: mathematics, code, STEM, logical puzzles, and instruction following. The authors argue this breadth "encourages generalization beyond narrow, domain-specific behaviors" and enables "more rigorous evaluation of RL algorithms" across fundamentally different environments and reward structures.

## (4) Pass@k Results Demonstrating Superiority

Nemotron-Research-Reasoning-Qwen-1.5B achieves substantial improvements over DeepSeek-R1-1.5B: 14.7% on math, 13.9% on coding, 54.8% on logic puzzles, 25.1% on STEM, and 18.1% on instruction-following tasks. Notably, the model maintains improvements across pass@1 through pass@16 evaluations throughout extended training.

## (5) Mechanisms Enabling Capability Expansion

Three critical mechanisms identified:
- **KL Regularization with Reference Policy Reset**: Prevents entropy collapse by periodically resetting the reference policy, allowing continued exploration rather than premature convergence
- **Decoupled Clipping (DAPO)**: Setting asymmetric bounds encourages "broader exploration" by uplifting probabilities of unlikely tokens
- **Inverse Correlation with Base Performance**: "The weaker the start, the stronger the gain with ProRL"—RL is most effective where base models initially struggle, expanding reasoning boundaries in underexplored domains
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fca7e5d3-e2d5-4a24-9b11-9cca177b6cd2",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "178a8a9b-0b74-4272-8ae3-49cd26af94ae",
  "sourceToolAssistantUUID": "fca7e5d3-e2d5-4a24-9b11-9cca177b6cd2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-28T01:28:57.165Z_

<details><summary>↩ Tool result · `toolu_018ku2oBfsXMxUDUYZ5RWAkK`</summary>

```text
# Variance Reduction in GRPO with Shrinkage Baselines

## (1) The Variance Problem with Small Rollout Counts

The paper identifies a critical challenge in LLM reinforcement learning: while classical RL operates with many rollouts per state, RLVR training typically uses "large batch sizes but _fewer rollouts per prompt_" due to inference costs. Even industrial-scale training rarely exceeds 16 rollouts per prompt, making baseline estimation from per-prompt empirical averages inherently noisy.

## (2) Quantitative Variance Analysis

The paper provides empirical evidence across multiple settings:

**Table 2 results (GSM8k with Qwen2.5-0.5B):**
- 2 generations: Shrinkage baseline achieves 55.22% vs RLOO's 54.49%
- 4 generations: 57.33% vs 56.34%
- 8 generations: 58.93% vs 58.31%

**Figure 8 variance reduction measurements:**
The paper documents gradient variance reduction ranging from 11.2% to 67.1% across different models when using the shrinkage baseline compared to RLOO.

## (3) The Shrinkage Estimator Approach

Rather than using only per-prompt means, the method combines prompt-level and batch-level statistics through:

$$b_{i}^{j}=(1-\hat{\lambda}_{i})\hat{\mu}_{i}^{-j}+\hat{\lambda}_{i}\hat{\bar{\mu}}_{-i}$$

The optimal shrinkage coefficient is: $\hat{\lambda}_{i}=\frac{n-1}{n}\cdot\frac{\widehat{v}_{-i}}{\widehat{v}_{-i}+\widehat{s}_{-i}}$

This adaptively balances variance reduction and bias control based on "expected variance" versus "dispersion of true value functions."

## (4) Ablation Results by Rollout Count

**Adaptive behavior (Figure 7):** The shrinkage coefficient $\hat{\lambda}_{i}$ decreases with more rollouts, since "intra-prompt estimates become more reliable and shrinkage baseline naturally approaches the RLOO baseline." This demonstrates the method automatically adjusts its regularization strength based on available samples.

**Performance consistency:** Unlike competing methods that excel only under specific conditions (RLOO performs best with 8 rollouts; REINFORCE++ with 2 rollouts), the shrinkage baseline "consistently achieves the highest evaluation scores across all rollout settings."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ceca0ff8-6330-431a-8dff-6ebbc2b20c7f",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "4b807cf2-2f98-44d3-b34c-669b80baa718",
  "sourceToolAssistantUUID": "ceca0ff8-6330-431a-8dff-6ebbc2b20c7f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-28T01:29:00.508Z_

<details><summary>↩ Tool result · `toolu_01JYsFaDd8CEAc12VRbPTaBc`</summary>

```text
# Key Findings on Beta-Bernoulli Reward Estimation

## (1) Beta-Bernoulli Reward Estimation Framework

The paper models binary rewards as Bernoulli random variables with a Beta prior:

**Core Model**: "pτ∼Beta(ατ,βτ)" where posterior parameters update via: "ατ=λατ−1+Sτ, βτ=λβτ−1+N−Sτ"

The Discounted Beta-Bernoulli (DBB) estimator computes: "p̂τ^dbb = ατ/(ατ+βτ)" with variance "Var^dbb(Xτ|ατ,βτ) = ατβτ/(ατ+βτ)²"

This approach prevents variance collapse since posterior variance cannot reach zero—a critical advantage over point estimation.

## (2) Sample Size Effects on Estimation Reliability

**Small Sample Regime**: The point estimator variance scales as "pτ(1−pτ)/N", becoming unreliable when N is limited. DBB reduces this variance proportionally to "(1−w)²" where w depends on historical weight.

**Empirical Finding**: "DBB estimator consistently outperforms the point estimator for N up to 16" (Figure 3b), demonstrating superior performance in low-rollout budgets typical of practical RLVR.

The paper shows DBB achieves lower MSE across most discount factor ranges, with optimal performance at λ=0.4 for the Qwen3-1.7B-Base model.

## (3) Variance Analysis and Sample Efficiency Results

**Variance Comparison**:
- Point estimator: "Var(p̂τ^pt|pτ) = pτ(1−pτ)/N"
- DBB estimator: "Var(p̂τ^dbb|pτ,ατ−1,βτ−1) = (1−w)² · pτ(1−pτ)/N"

The reduction factor "(1−w)²" provides substantial variance reduction by leveraging historical information.

**MSE Results**: GRPO-DBB achieves "average Acc@8 improvements of 3.43 points for Qwen3-1.7B and 2.32 points for Qwen3-8B" compared to standard GRPO, with even larger gains on out-of-distribution tasks (10.05 and 8.34 points respectively).

## (4) Comparison to Standard GRPO Reward Estimation

**Standard GRPO** uses point estimation: "p̂τ^pt = (1/N)∑Xτ,i" with sample variance "Var^pt(Xτ) = N·p̂τ^pt(1−p̂τ^pt)/(N−1)"

**Key Differences**:
- Standard GRPO suffers variance collapse when all responses receive identical rewards
- DBB introduces controlled bias but achieves lower MSE: "MSE trades small bias for substantial variance reduction via shrinkage"
- GRPO-DBB produces longer responses with lower entropy during training, indicating more stable exploration behavior

**Performance**: Across six mathematical reasoning benchmarks plus three general reasoning tasks, GRPO-DBB consistently outperforms GRPO without additional computational cost or memory overhead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e2e239c-f3b8-40b1-81d4-6c3905bb50a5",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "5916052a-e7fd-470d-adc8-1be097e08942",
  "sourceToolAssistantUUID": "5e2e239c-f3b8-40b1-81d4-6c3905bb50a5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 67 · 2026-05-28T01:29:05.921Z_

Now let me search for a few more specific pieces of evidence for the counter-argument on Topic 1.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5916052a-e7fd-470d-adc8-1be097e08942",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6kRw4ep4xDZFRwQ53V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "893e9108-e544-4883-b1fc-3d7bb07a6a35",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ecdNrL8EvMkEyhgFNCF6c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3109,
      "cache_read_input_tokens": 27437,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3109,
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

_source line 68 · 2026-05-28T01:29:06.923Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017aYiwtk56Hdz2L26yte5Zs`</summary>

```json
{
  "query": "\"capability boundary collapse\" \"pass@k\" RLVR diversity training distribution narrow exploration 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "893e9108-e544-4883-b1fc-3d7bb07a6a35",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6kRw4ep4xDZFRwQ53V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a5f7fa0f-cd4c-4f6a-8b87-c3f3257fd521",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ecdNrL8EvMkEyhgFNCF6c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3109,
      "cache_read_input_tokens": 27437,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3109,
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

_source line 69 · 2026-05-28T01:29:08.436Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YATtE5nwwS6AyncmyYeWXS`</summary>

```json
{
  "query": "RL selects among base model behaviors training coverage determines WHICH behaviors selected reasoning LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5f7fa0f-cd4c-4f6a-8b87-c3f3257fd521",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6kRw4ep4xDZFRwQ53V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d9c005f-fba8-4792-8533-d8b5c9f0e192",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ecdNrL8EvMkEyhgFNCF6c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3109,
      "cache_read_input_tokens": 27437,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3109,
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

_source line 70 · 2026-05-28T01:29:09.237Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XnE2CnWvSTQJjWwYm9LSEg`</summary>

```json
{
  "query": "GRPO group size ablation 4 8 16 32 rollouts performance comparison reasoning LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d9c005f-fba8-4792-8533-d8b5c9f0e192",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6kRw4ep4xDZFRwQ53V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1806d00d-adba-4d53-bf79-ad0bcbfebb69",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ecdNrL8EvMkEyhgFNCF6c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3109,
      "cache_read_input_tokens": 27437,
      "output_tokens": 217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3109
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 217,
          "cache_read_input_tokens": 27437,
          "cache_creation_input_tokens": 3109,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3109,
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

_source line 71 · 2026-05-28T01:29:14.848Z_

<details><summary>↩ Tool result · `toolu_017aYiwtk56Hdz2L26yte5Zs`</summary>

```text
Web search results for query: ""capability boundary collapse" "pass@k" RLVR diversity training distribution narrow exploration 2025 2026"

Links: [{"title":"Preprint, July 2025 RL-PLUS: Countering Capability Boundary Collapse of LLMs","url":"https://arxiv.org/pdf/2508.00222"},{"title":"RL-PLUS: Countering Capability Boundary Collapse of LLMs in Reinforcement Learning with Hybrid-policy Optimization","url":"https://arxiv.org/html/2508.00222"},{"title":"The Choice of Divergence: A Neglected Key to Mitigating Diversity Collapse in Reinforcement Learning with Verifiable Reward","url":"https://arxiv.org/html/2509.07430"},{"title":"Divergence and Diversity in RLVR","url":"https://www.emergentmind.com/papers/2509.07430"},{"title":"RL-PLUS: Countering Capability Boundary Collapse of LLMs in...","url":"https://arxiv.org/abs/2508.00222"},{"title":"Beyond Pass@1: Self-Play with Variational Problem Synthesis Sustains RLVR","url":"https://arxiv.org/pdf/2508.14029"},{"title":"[2509.07430] The Choice of Divergence: A Neglected Key to Mitigating Diversity Collapse in Reinforcement Learning with Verifiable Reward","url":"https://arxiv.org/abs/2509.07430"},{"title":"Paper page - The Choice of Divergence: A Neglected Key to Mitigating Diversity Collapse in Reinforcement Learning with Verifiable Reward","url":"https://huggingface.co/papers/2509.07430"},{"title":"The Choice of Divergence: A Neglected Key to Mitigating Diversity Collapse in Reinforcement Learning with Verifiable Reward","url":"https://arxiv.org/pdf/2509.07430"}]

Based on the search results, I found highly relevant research on capability boundary collapse in RLVR (Reinforcement Learning with Verifiable Rewards) from 2025-2026. Here's what the research shows:

## Core Problem: Capability Boundary Collapse

Existing RLVR can collapse the base model's capability boundary, thus fundamentally limiting the acquisition of new reasoning pathways. While RLVR-tuned models consistently improve the probability of generating a correct solution in a single attempt (Pass@1), their performance when multiple attempts are permitted (Pass@k) often stagnates or even degrades compared to their base models.

This discrepancy suggests that RLVR, rather than teaching novel reasoning, may instead overfit the model to known solution paths, thereby sacrificing diversity.

## Diversity and Training Distribution Issues

Vanilla RLVR training, such as GRPO optimization, may diminish the generation diversity of the policy model, enhancing sampling efficiency and Pass@1 performance at the expense of output richness, thereby failing to improve Pass@k over the base model.

The primary cause of entropy collapse and plateaued Pass@k is RLVR training on limited problems, where the policy is easily rewarded for repeatedly generating memorized correct solutions.

## Solutions Being Explored

Recent research (2025-2026) proposes several approaches:

1. **RL-PLUS**: RL-PLUS integrates two core components, i.e., Multiple Importance Sampling to address distributional mismatch from external data, and Exploration-Based Advantage Function to guide the model towards high-value, unexplored reasoning paths.

2. **Divergence Selection**: The proper selection of a divergence measure is a powerful tool for building more general and diverse reasoning models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a5f7fa0f-cd4c-4f6a-8b87-c3f3257fd521",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "e33dc88b-51c1-461e-a079-0430836ce9d4",
  "sourceToolAssistantUUID": "a5f7fa0f-cd4c-4f6a-8b87-c3f3257fd521",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-28T01:29:16.059Z_

<details><summary>↩ Tool result · `toolu_01YATtE5nwwS6AyncmyYeWXS`</summary>

```text
Web search results for query: "RL selects among base model behaviors training coverage determines WHICH behaviors selected reasoning LLM"

Links: [{"title":"Recent reasoning research: GRPO tweaks, base model RL, and data curation","url":"https://www.interconnects.ai/p/papers-im-reading-base-model-rl-grpo"},{"title":"OctoThinker: Mid-training Incentivizes Reinforcement Learning Scaling","url":"https://arxiv.org/pdf/2506.20512"},{"title":"Behavior Injection: Preparing Language Models for Reinforcement Learning","url":"https://arxiv.org/pdf/2505.18917"},{"title":"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?","url":"https://arxiv.org/pdf/2504.13837"},{"title":"Limit of RLVR","url":"https://limit-of-rlvr.github.io/"},{"title":"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? | OpenReview","url":"https://openreview.net/forum?id=4OsgYD7em5"},{"title":"SimpleRL-Zoo: Investigating and Taming Zero Reinforcement Learning for Open Base Models in the Wild","url":"https://arxiv.org/pdf/2503.18892"},{"title":"A Systematic Analysis of Base Model Choice for Reward Modeling","url":"https://arxiv.org/pdf/2505.10775"},{"title":"RL-Selector: Reinforcement Learning-Guided Data Selection via Redundancy Assessment","url":"https://arxiv.org/pdf/2506.21037"}]

Based on the search results, I found relevant research that addresses your query about how RL selects among base model behaviors and how training coverage determines which behaviors are selected:

RL fine-tuning often amplifies behaviors already accessible in the base model rather than introducing entirely new ones. This is a key finding in how RL operates on existing model capabilities.

More specifically regarding the role of coverage: The reasoning paths generated by RLVR models are already included in the base models' sampling distribution, and all reasoning paths in the RLVR model are already present in the base model. 

The mechanism works as follows: RL training biases the distribution toward rewarded paths, improving sampling efficiency, but this comes at the cost of reduced scope of reasoning capacity, as other problems where the base model contains correct paths may no longer be accessible in the RLVR model.

In essence, RLVR-trained models generate reasoning paths already within the base model's output distribution, meaning RLVR biases the model toward higher-rewarded solutions rather than creating entirely new reasoning abilities. The training coverage of different behaviors in the base model determines which ones get selected and amplified during RL training based on the reward signal.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d9c005f-fba8-4792-8533-d8b5c9f0e192",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "5ab1dc24-2264-4e24-a64f-122e8e5b06b8",
  "sourceToolAssistantUUID": "6d9c005f-fba8-4792-8533-d8b5c9f0e192",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-28T01:29:16.808Z_

<details><summary>↩ Tool result · `toolu_01XnE2CnWvSTQJjWwYm9LSEg`</summary>

```text
Web search results for query: "GRPO group size ablation 4 8 16 32 rollouts performance comparison reasoning LLM 2025 2026"

Links: [{"title":"Act Only When It Pays: Efficient Reinforcement Learning for LLM Reasoning via Selective Rollouts","url":"https://arxiv.org/html/2506.02177v1"},{"title":"It Takes Two: Your GRPO Is Secretly DPO","url":"https://arxiv.org/html/2510.00977"},{"title":"Scaf-GRPO: Scaffolded Group Relative Policy Optimization for Enhancing LLM Reasoning","url":"https://arxiv.org/html/2510.19807"},{"title":"Group Distributionally Robust Optimization-Driven Reinforcement Learning for LLM Reasoning","url":"https://arxiv.org/pdf/2601.19280"},{"title":"Train Less, Learn More: Adaptive Efficient Rollout Optimization for Group-Based Reinforcement Learning","url":"https://arxiv.org/pdf/2602.14338"},{"title":"iGRPO: Self-Feedback-Driven LLM Reasoning","url":"https://arxiv.org/pdf/2602.09000"},{"title":"Efficient Reinforcement Learning for LLM Reasoning via ...","url":"https://www.arxiv.org/pdf/2506.02177"},{"title":"Evolution Strategies vs GRPO for LLM Fine-Tuning | alphaXiv","url":"https://www.alphaxiv.org/blog/es-for-fine-tuning-llms"},{"title":"AMIR-GRPO: Inducing Implicit Preference Signals into GRPO","url":"https://arxiv.org/pdf/2601.03661"}]

Based on the search results, I found relevant information about GRPO group size ablation studies. Here are the key findings:

## Group Size Ablation Results

Conventional intuition suggests that GRPO's efficacy is strongly correlated with its group size, grounded in the premise that larger sample sizes yield more accurate advantage estimates and lead to stronger post-trained LLMs. However, research challenges this assumption.

2-GRPO converges substantially faster than 16-GRPO, owing to the reduced number of samples generated and updated per step, and reducing the group size not only preserves performance but also accelerates the learning process.

The research specifically evaluates group sizes G=2,4,8,16, which aligns directly with your query parameters. The results demonstrate that 2-GRPO remains both effective and efficient across diverse tasks including math reasoning, Vision Reasoning (Geometry3K), and Code Generation (Code-R1).

## Performance Insights

The findings indicate that the group's role in GRPO is providing contrastive sample pairs, rather than requiring larger groups for better advantage estimation. This suggests that performance doesn't monotonically improve with group size (4, 8, 16, 32), and smaller group sizes can be more efficient while maintaining comparable reasoning performance on LLM tasks.

The research from 2025-2026 demonstrates that practitioners don't need to use larger group sizes like 32 rollouts when smaller sizes like 2, 4, or 8 can achieve competitive results with faster convergence.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1806d00d-adba-4d53-bf79-ad0bcbfebb69",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "34a98c2f-436c-4723-8a80-31b8874593c7",
  "sourceToolAssistantUUID": "1806d00d-adba-4d53-bf79-ad0bcbfebb69",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-28T01:29:21.775Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014npVLUWz3ia4kT5DFJN2nx`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.00977",
  "prompt": "Extract all findings about: (1) the equivalence between GRPO and DPO, (2) group size ablation results comparing G=2,4,8,16, (3) the argument that 2-GRPO is sufficient, (4) specific performance numbers across different group sizes. Provide tables and specific quotes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34a98c2f-436c-4723-8a80-31b8874593c7",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6mddJXqSaJihYekZG6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "78120721-28c1-4c0a-af32-2f5f4068976a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011TaJW5szQyzqXwo8mkXa7t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2684,
      "cache_read_input_tokens": 30546,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2684,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

_source line 75 · 2026-05-28T01:29:23.740Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011SH3otxWU65ogry4v3RENK`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.18917",
  "prompt": "Extract the abstract and key findings about behavior injection and preparing language models for RL. Specifically: how does pre-training coverage of behaviors affect RL outcomes? Does injecting diverse behaviors before RL improve which capabilities get selected?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78120721-28c1-4c0a-af32-2f5f4068976a",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6mddJXqSaJihYekZG6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cbec701b-fa2c-4298-ad05-df71d584110c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011TaJW5szQyzqXwo8mkXa7t",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2684,
      "cache_read_input_tokens": 30546,
      "output_tokens": 265,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2684
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 265,
          "cache_read_input_tokens": 30546,
          "cache_creation_input_tokens": 2684,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2684,
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

_source line 76 · 2026-05-28T01:29:28.577Z_

<details><summary>↩ Tool result · `toolu_011SH3otxWU65ogry4v3RENK`</summary>

```text
# Behavior Injection for Language Model RL Preparation

## Abstract Summary

The paper addresses inconsistent RL finetuning outcomes in LLMs. Researchers identified two critical conditions for effective post-training: "(1) RL-informative rollout accuracy, and (2) strong data co-influence" which measures how training data affects performance across samples.

## Key Finding on Behavior Coverage

The research proposes that pre-training data diversity matters significantly. Rather than relying on whatever behaviors already exist in the base model, the method enriches supervised finetuning data "by seeding exploratory and exploitative behaviors, effectively making the model more RL-ready."

## Impact on Capability Selection

The approach is "task-agnostic," suggesting that injecting diverse exploratory and exploitative behavioral examples before RL training helps models respond more consistently to reinforcement signals. This preparation phase appears to improve which capabilities get reinforced downstream during RL, resulting in "significantly increase[d] performance gain from RL over the pre-RL model."

The core insight is that models lacking sufficient behavioral diversity in their training data plateau or degrade under RL, while augmented models show substantial gains—indicating that pre-training coverage determines which capabilities can be effectively selected during reinforcement learning.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cbec701b-fa2c-4298-ad05-df71d584110c",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "e53b3645-8721-43ce-a7ea-34296b3f5196",
  "sourceToolAssistantUUID": "cbec701b-fa2c-4298-ad05-df71d584110c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-28T01:29:32.958Z_

<details><summary>↩ Tool result · `toolu_014npVLUWz3ia4kT5DFJN2nx`</summary>

```text
# Key Findings on GRPO and DPO Equivalence

## (1) GRPO-DPO Equivalence

The paper establishes that GRPO and DPO represent the same contrastive learning mechanism under different settings:

**Core Claim:** "The maximization of the GRPO objective is equivalent to the minimization of an N-vs-M contrastive loss estimator" (Proposition 3.2).

**Key Quote on Relationship:** Both algorithms share "the same positive–negative structure and differ only in the token-level coefficient" with differences reflecting "adaptations to online vs. offline RL settings" rather than fundamental algorithmic differences.

**Specific Differences:**
- **Importance Sampling:** GRPO uses token-level importance sampling (online); DPO uses log-likelihood terms (offline)
- **Group Weighting:** GRPO weights by √Var(q); DPO weights by sigmoid of reward difference
- **Token Aggregation:** GRPO averages; DPO sums (design choice, not fundamental)

---

## (2) Group Size Ablation Results (G=2,4,8,16)

**Table from Ablation Study:**

| Group Size | Mean@32 (Qwen-1.5B) | Pass@32 | Trend |
|---|---|---|---|
| 2 | ~69.3 | Comparable | Minimal gap |
| 4 | ~69.5 | Comparable | Minimal gap |
| 8 | ~69.8 | Comparable | Minimal gap |
| 16 | ~70.2 | Baseline | Reference |

**Key Finding:** "The Mean@32 differences among G=2,4,8,16 are consistently small across all settings. Moreover, increasing the group size does not reliably improve Pass@32."

---

## (3) Why 2-GRPO is Sufficient

**Traditional View Predicts Failure:** With n=2 samples, classical statistics yields extreme instability—"degrees of freedom df=1 result in a normalization factor that follows a Cauchy distribution."

**Contrastive Perspective Predicts Success:** Under the contrastive framing, group size functions as Monte Carlo sample size for estimating positive/negative gradients. "Monte Carlo estimation is unbiased regardless of sample size."

**The Minimal Setting:** With two rollouts, "the GRPO advantage reduces to a simple contrastive signal: A+=+1 and A−=−1 when the two rollouts disagree on the reward."

---

## (4) Performance Numbers Across Group Sizes

**Main Results (Table 1 excerpt - MATH Dataset, Qwen-1.5B):**

| Model | Group | Training Time | MATH-500 | AMC 2023 | Avg Performance | vs 16-GRPO |
|---|---|---|---|---|---|---|
| 2-GRPO | 2 | 2.05h | 69.28 | 49.53 | 22.31 | -0.80 |
| 2-GRPO+RS | 2+RS | 3.71h | 71.36 | 51.64 | 23.85 | +0.74 |
| 16-GRPO | 16 | 8.53h | 70.24 | 51.25 | 23.11 | Baseline |

**Efficiency Metrics:**
- "2-GRPO achieves 97.6% of 16-GRPO's average performance while using only 12.5% of rollouts and 21.0% of training time"
- 2-GRPO+RS (with resampling) "outperforms 16-GRPO on average while using roughly half of its training time"

**Extended Tasks:** Results generalized to Geometry3K and Code-R1, where "2-GRPO converges substantially faster than 16-GRPO, owing to the reduced number of samples generated."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "78120721-28c1-4c0a-af32-2f5f4068976a",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "2eff76e8-866a-46b5-bfac-2acff2dd64d3",
  "sourceToolAssistantUUID": "78120721-28c1-4c0a-af32-2f5f4068976a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-28T01:29:36.160Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019T3CEW3kJqpect1LLbnUpw`</summary>

```json
{
  "query": "arXiv \"two stage\" RLVR capability boundary shrinkage expansion reasoning dynamic view 2510.04028"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2eff76e8-866a-46b5-bfac-2acff2dd64d3",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6npfr79KR6Uy5PVJYR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb803978-acb8-4ebf-bc47-232269809816",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0142iTMSs35EAsBbNZJRKGc1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 305,
      "cache_creation_input_tokens": 1235,
      "cache_read_input_tokens": 33230,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1235,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 79 · 2026-05-28T01:29:37.276Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AGqG39jZZ58x1X7ggFjnfN`</summary>

```json
{
  "query": "RLOO advantage estimation sample size binary reward variance per-prompt mean estimation GRPO generations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb803978-acb8-4ebf-bc47-232269809816",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6npfr79KR6Uy5PVJYR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "252a0398-e00e-40eb-a280-e252d1b14448",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0142iTMSs35EAsBbNZJRKGc1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 305,
      "cache_creation_input_tokens": 1235,
      "cache_read_input_tokens": 33230,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1235
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 305,
          "output_tokens": 131,
          "cache_read_input_tokens": 33230,
          "cache_creation_input_tokens": 1235,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1235,
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

_source line 80 · 2026-05-28T01:29:42.901Z_

<details><summary>↩ Tool result · `toolu_019T3CEW3kJqpect1LLbnUpw`</summary>

```text
Web search results for query: "arXiv "two stage" RLVR capability boundary shrinkage expansion reasoning dynamic view 2510.04028"

Links: [{"title":"[2510.04028] The Debate on RLVR Reasoning Capability Boundary: Shrinkage, Expansion, or Both? A Two-Stage Dynamic View","url":"https://arxiv.org/abs/2510.04028"},{"title":"The Debate on RLVR Reasoning Capability Boundary: Shrinkage, Expansion, or Both? A Two-Stage Dynamic View","url":"https://arxiv.org/html/2510.04028"},{"title":"From Exploration to Exploitation: A Two-Stage Entropy RLVR Approach for","url":"https://www.arxiv.org/pdf/2511.07738"},{"title":"From Exploration to Exploitation: A Two-Stage Entropy RLVR Approach for Noise-Tolerant MLLM Training","url":"https://arxiv.org/html/2511.07738v2"},{"title":"(PDF) The Debate on RLVR Reasoning Capability Boundary: Shrinkage, Expansion, or Both? A Two-Stage Dynamic View","url":"https://www.researchgate.net/publication/396249087_The_Debate_on_RLVR_Reasoning_Capability_Boundary_Shrinkage_Expansion_or_Both_A_Two-Stage_Dynamic_View"},{"title":"The Debate on RLVR Reasoning Capability Boundary:","url":"https://arxiv.org/pdf/2510.04028"},{"title":"1 Introduction","url":"https://arxiv.org/html/2601.08468v1"}]

I found the paper you're looking for! Here's what I discovered:

The paper "The Debate on RLVR Reasoning Capability Boundary: Shrinkage, Expansion, or Both? A Two-Stage Dynamic View" (arXiv:2510.04028) addresses the ongoing debate on whether reinforcement learning with verifiable rewards (RLVR) expands or shrinks the reasoning capabilities of large language models (LLMs).

**Key Findings:**

Some studies contend that RLVR mainly improves sampling efficiency but at the expense of diversity and exploratory capacity, resulting in capability boundary shrinkage. In contrast, others demonstrate that prolonged training can lead to the emergence of novel reasoning strategies, suggesting capability boundary expansion.

**The Two-Stage Dynamic View:**

The study resolves the debate by showing that initial training favors exploitation, potentially narrowing capability boundaries, while prolonged training encourages exploration, enabling genuine expansion. During the exploration stage, as training advances, the growth rate of previously acquired high-reward tokens slows. When a potentially optimal token receives positive advantage estimates and is occasionally sampled, its probability increases while originally high-reward tokens decrease. This dynamic suggests that over-exploitation during the exploitation stage may lead to capability boundary shrinkage, whereas prolonged training into the exploration stage can promote expansion.

The paper was submitted on October 5, 2025, and provides both theoretical and empirical support for this reconciliation of the contradictory findings in the field.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb803978-acb8-4ebf-bc47-232269809816",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "619aa2bc-40c2-4b85-92e3-33f8fff7812c",
  "sourceToolAssistantUUID": "fb803978-acb8-4ebf-bc47-232269809816",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-28T01:29:44.401Z_

<details><summary>↩ Tool result · `toolu_01AGqG39jZZ58x1X7ggFjnfN`</summary>

```text
Web search results for query: "RLOO advantage estimation sample size binary reward variance per-prompt mean estimation GRPO generations"

Links: [{"title":"REINFORCE Leave-One-Out (RLOO) — swift 4.2.0.dev0 documentation","url":"https://swift.readthedocs.io/en/latest/Instruction/GRPO/AdvancedResearch/RLOO.html"},{"title":"REINFORCE++: An Efficient RLHF Algorithm with Robustness to Both Prompt and Reward Models","url":"https://arxiv.org/html/2501.03262v3"},{"title":"Advantage Shaping as Surrogate Reward Maximization:","url":"https://arxiv.org/pdf/2510.23049"},{"title":"Blockwise Advantage Estimation for Multi-Objective RL with Verifiable Rewards","url":"https://arxiv.org/html/2602.10231"},{"title":"BASIS: Batchwise Advantage Estimation from Single-Rollout Information Sharing for LLM Reasoning","url":"https://arxiv.org/html/2605.27293"},{"title":"Group Relative Policy Optimization (GRPO)","url":"https://cameronrwolfe.substack.com/p/grpo"},{"title":"Reinforcement Learning | RLHF Book by Nathan Lambert","url":"https://rlhfbook.com/c/06-policy-gradients"},{"title":"Shrinking the Variance: Shrinkage Baselines for Reinforcement Learning with Verifiable Rewards","url":"https://arxiv.org/html/2511.03710v1"},{"title":"Gradient Starvation in Binary-Reward GRPO: Why Group-Mean Centering Fails and Why the Simplest Fix Works","url":"https://arxiv.org/html/2605.07689"},{"title":"Discounted Beta--Bernoulli Reward Estimation for Sample-Efficient Reinforcement Learning with Verifiable Rewards","url":"https://arxiv.org/pdf/2603.18444"}]

I found relevant results about RLOO advantage estimation, sample size considerations, and GRPO generations. Here's what the search revealed:

## Key Findings

**RLOO vs GRPO Advantage Estimation:**

Both GRPO and RLOO estimate advantages via intra-group comparisons to avoid the high variance of a global baseline. However, they differ in their approaches:

- For each prompt, RLOO generates K response samples and constructs the baseline via Leave-One-Out, where for the i-th sample, the baseline is the mean of the other K-1 samples
- For each prompt, GRPO generates G response samples and normalizes rewards using the group mean and standard deviation

**Sample Size Requirements:**

Because advantage is computed in a relative manner (i.e., based on rewards in the group), the number of completions sampled per prompt must be high to obtain a stable policy gradient estimate. More specifically, RLOO and GRPO perform best with 8 rollouts, where prompt-level reward averaging becomes accurate

**Binary Reward Variance Issues:**

GRPO and RLOO perform worst on medium-difficulty prompts, which is expected for binary rewards since prompts with values near the middle have the largest reward variance.

The variance of rewards can collapse to zero when all generated responses receive identical rewards under group-relative estimation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "252a0398-e00e-40eb-a280-e252d1b14448",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "b13c4e44-8979-4143-89c9-bf84140d4170",
  "sourceToolAssistantUUID": "252a0398-e00e-40eb-a280-e252d1b14448",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-28T01:29:48.902Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TQQr3QqvQxxDK7dngjXAa5`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.04028",
  "prompt": "Extract the key findings about: (1) the two-stage dynamic view of capability boundary change, (2) evidence that prolonged/diverse training expands capabilities beyond base model, (3) the transition from exploitation to exploration, (4) how training distribution affects which stage dominates. Provide specific quotes and quantitative results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b13c4e44-8979-4143-89c9-bf84140d4170",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6ofbBRHHYNpiiSuvMP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "040a5bdb-4e26-4dbf-895c-f5700a5fa0f8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012RNYybVPiPsSZijUZW5tdN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2076,
      "cache_read_input_tokens": 34465,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2076,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

_source line 83 · 2026-05-28T01:29:50.442Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0145HZpXxmxudcEiPCJbvCkc`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.07689",
  "prompt": "Extract key findings about: (1) gradient starvation in binary-reward GRPO, (2) how group-mean centering fails, (3) the relationship between group size and gradient quality, (4) any specific analysis of how rollout count affects the gradient starvation problem. Include formulas and quantitative results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "040a5bdb-4e26-4dbf-895c-f5700a5fa0f8",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6ofbBRHHYNpiiSuvMP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e29ade5-1a89-4633-8a01-e011dcacdf36",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012RNYybVPiPsSZijUZW5tdN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2076,
      "cache_read_input_tokens": 34465,
      "output_tokens": 283,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2076
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 283,
          "cache_read_input_tokens": 34465,
          "cache_creation_input_tokens": 2076,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2076,
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

_source line 84 · 2026-05-28T01:29:57.083Z_

<details><summary>↩ Tool result · `toolu_01TQQr3QqvQxxDK7dngjXAa5`</summary>

```text
# Key Findings on RLVR Capability Boundaries

## (1) Two-Stage Dynamic View

The paper identifies a fundamental mechanism explaining the debate: **both capability shrinkage and expansion occur at different training phases**.

**Exploitation Stage (Shrinkage):** Initially, models reinforce already-explored high-reward tokens while neglecting potentially optimal low-probability options. The framework shows that "the probability of the potentially optimal token remains largely unchanged" during this phase, suggesting over-exploitation narrows reasoning capacity.

**Exploration Stage (Expansion):** With prolonged training, high-probability tokens saturate (approaching probability 1), enabling gradient updates to redirect toward initially under-sampled tokens with higher potential. This reallocation mechanism facilitates genuine capability expansion.

## (2) Evidence for Prolonged Training Benefits

The empirical results strongly support extended training advantages:

- **GRPO-N (negative gradients only)** achieves superior Pass@k performance across benchmarks while maintaining higher entropy than base models
- On AIME 2025, GRPO-N reaches Pass@256 of 66.7% versus base model's 46.7%—a 43% improvement
- Crucially, entropy "initially decreases and then increases" under GRPO-N, unlike standard GRPO which experiences "entropy collapse"

## (3) Transition Mechanism

The mathematical foundation (Theorem 1) reveals the update rule: expected logit change equals η·π(v)·[(1−π(v))·Â(v)−Σπ(u)·Â(u)]

This shows how "the relative negative sample transitions from the initially low-reward token to the high-reward token," enabling exploration after exploitation plateaus.

## (4) Training Distribution Effects

The toy example demonstrates sensitivity to initial conditions: when suboptimal high-probability actions are initially favored (π(a₁)>π(a₂) but r(a₁)<r(a₂)), standard training exhibits pronounced shrinkage. However, "prolonging the duration of training" allows recovery through the exploration phase mechanism.

The case study reveals GRPO-N generates fewer erroneous intermediate steps, suggesting distribution diversity preservation enables better long-term reasoning development.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "040a5bdb-4e26-4dbf-895c-f5700a5fa0f8",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "0c4fc269-1fdc-4b28-85e6-a9ff8b35f37b",
  "sourceToolAssistantUUID": "040a5bdb-4e26-4dbf-895c-f5700a5fa0f8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-28T01:29:58.648Z_

<details><summary>↩ Tool result · `toolu_0145HZpXxmxudcEiPCJbvCkc`</summary>

```text
# Key Findings on Gradient Starvation in Binary-Reward GRPO

## 1. Gradient Starvation Problem

The core issue emerges when all G responses receive identical binary rewards. Under group-mean centering, the advantage becomes exactly zero: "A_j = r_j - n₊/G" produces A_j = 0 for degenerate groups (all correct or all incorrect). This eliminates learning signals entirely for those groups.

**Empirical severity**: At G=4 with Qwen3.5-9B on GSM8K, observed degeneracy reached 69.25%, with 54.75% all-fail and 14.50% all-pass groups in logged training data.

## 2. Group-Mean Centering Failure Mechanism

The degeneracy probability for per-prompt success probability p_x is:

D(p_x, G) = p_x^G + (1-p_x)^G

A Jensen's inequality bound proves: "D_real ≥ D_iid" because the function is convex. Measured real degeneracy (D_real = 0.90 at G=2) exceeded the i.i.d. prediction (D_iid = 0.56) by 60%, driven by bimodal prompt difficulty distributions.

## 3. Group Size Effects on Gradient Quality

Larger groups substantially reduce starvation:
- **G=4**: DrGRPO achieved only 28.4% accuracy (baseline: 25.5%)
- **G=8**: DrGRPO recovered to 81.7% accuracy

This aligns with theoretical predictions since degeneracy probability p^G + (1-p)^G decreases as G increases for intermediate success probabilities.

## 4. Rollout Count Analysis

The paper doesn't directly isolate rollout effects, but the 200-step budget constraint reveals interaction with group size. With limited training iterations, small groups (G=4) suffer disproportionately because degenerate groups consume training compute without producing gradients. The fixed-reference Sign advantage A=2r-1 addressed this by providing full-strength signals in all groups.

**Performance improvement**: Sign achieved 73.8% versus DrGRPO's 28.4% at G=4 (45.4 percentage point gain, p<0.0001).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e29ade5-1a89-4633-8a01-e011dcacdf36",
  "isSidechain": true,
  "promptId": "4f14287e-c3c6-4cb9-b84f-1854a17f9955",
  "agentId": "a7ecfe27cc3cea032",
  "type": "user",
  "uuid": "d7ff2631-3683-4984-b651-f81e48980a19",
  "sourceToolAssistantUUID": "9e29ade5-1a89-4633-8a01-e011dcacdf36",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 86 · 2026-05-28T01:31:41.677Z_

I now have comprehensive evidence for both topics. Let me compile the findings.

---

# Research Findings Report

## TOPIC 1: Counter-Argument to "Sparse Policy Selection Undermines Training Distribution Diversity"

### The Sparse Policy Selection Paper (arXiv 2605.06241)

**Citation:** Akgul et al., "Rethinking RL for LLM Reasoning: It's Sparse Policy Selection, Not Capability Learning," arXiv:2605.06241 (May 2026).

Key claims:
- RL modifies only 1.0-4.1% of token positions, all within the base model's top-5 candidates
- Reranked positions have 5-12x higher base-model entropy than unchanged positions; the promoted token averages rank 2.14-2.39 under the base model
- "RL does not introduce novel tokens; it consistently elevates one of the base model's top alternatives at moments of uncertainty"
- Their alternative method ReasonMaxxer works only on problems in the "mixed-success regime" where "the base model's pass rate lies strictly between 0 and 1"

**Critical limitation the authors acknowledge:** They focus only on four base/RL-tuned pairs and mathematical reasoning, and do not examine whether different training distributions would cause RL to select different subsets of behaviors.

### The Substantive Counter-Argument

The reviewer's logic is: "if RL merely selects, then training distribution diversity doesn't matter -- the base model ceiling is the binding constraint." This argument has a critical flaw: **it conflates the existence of a ceiling with the accessibility of that ceiling.** Even if RL is purely selecting among existing base-model behaviors, the training distribution determines WHICH subset of the base model's vast latent repertoire gets activated. Here is the evidence:

#### 1. Sharper Primitives: Training Coverage Determines Multi-Step Capability (arXiv 2602.08281)

**Citation:** "New Skills or Sharper Primitives? A Probabilistic Perspective on the Emergence of Reasoning in RLVR," arXiv:2602.08281 (Feb 2026).

The multiplicative compounding equation is the key insight:

> P_theta(q) ~ product_{j=1}^{M} P_theta(s_j)

Sharpening individual atomic probabilities from 0.3 to 0.7 transforms a 5-step task from 0.0024 to 0.168 success rate. They find high correlation (rho in [0.69, 0.96]) between joint atomic probabilities and composite outcomes. Crucially, RLVR "polarizes the model's success probabilities across the task distribution -- driving correctness probability of certain problems towards certainty while reducing the probability of solving others."

**Why this supports diverse training:** If RLVR polarizes -- sharpening some primitives while sacrificing others -- then training distribution determines WHICH primitives get sharpened. Narrow training sharpens narrow primitives; diverse training sharpens diverse primitives. Since multi-step success is multiplicative, covering more primitive types through diverse training exponentially expands the set of composite tasks the model can solve.

#### 2. Tailor: Primitive Coverage Directly Determines RL Outcomes (arXiv 2511.12429)

**Citation:** "Tailored Primitive Initialization is the Secret Key to Reinforcement Learning," arXiv:2511.12429 (Nov 2025).

Key findings:
- "Initializing LLMs with diverse, high-quality reasoning primitives is essential for achieving stable and sample-efficient RL training"
- Rule-based demonstrations achieve perfect accuracy yet fail to support effective RL -- "reasoning correctness in the SFT dataset alone does not guarantee RL success"
- With 25 primitives versus 4, post-RL performance improved substantially
- Higher diversity (measured by lower median similarity scores) consistently benefits RL across settings

This directly demonstrates that even when RL is "selecting" among existing behaviors, the diversity of behaviors available for selection is the binding constraint, not just correctness.

#### 3. Capability Boundary Collapse: Narrow Training Causes Coverage Loss (arXiv 2508.00222)

**Citation:** "RL-PLUS: Countering Capability Boundary Collapse of LLMs in Reinforcement Learning with Hybrid-policy Optimization," arXiv:2508.00222 (Jul 2025).

Key findings:
- Standard RLVR "narrows rather than expands the model's problem-solving scope" -- pass@1 improves but pass@128 degrades
- "Policy entropy sharply decreases during training, making the model overly deterministic"
- Their fix (RL-PLUS) uses diverse external trajectories with importance sampling, achieving "average relative improvements over GRPO up to 69.2%"
- RL-PLUS "maintains a consistent performance advantage over both the base model and GRPO as k-values increase"

This proves that training distribution diversity is essential for accessing the full base model ceiling. Without it, RL selects a narrow subset of base-model capabilities while abandoning others.

#### 4. ProRL: Prolonged Diverse Training CAN Exceed Apparent Base Model Ceiling (arXiv 2505.24864)

**Citation:** "ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models," arXiv:2505.24864 (May 2025).

Key findings:
- Training on 136K problems across five diverse domains (math, code, STEM, logic, instruction-following)
- "Many tasks where the base model fails to produce any correct solutions regardless of the amount of sampling, while our RL-trained model achieves 100% pass rates"
- Creativity Index metric shows "prolonged RL training leads to trajectories with higher novelty"
- Average improvements: 14.7% math, 13.9% coding, 54.8% logic puzzles, 25.1% STEM, 18.1% instruction-following

This challenges the "ceiling" argument itself -- diverse prolonged training can apparently push beyond what sampling from the base model alone can achieve.

#### 5. Two-Stage Dynamic View: Training Duration/Diversity Determines Whether Expansion Occurs (arXiv 2510.04028)

**Citation:** "The Debate on RLVR Reasoning Capability Boundary: Shrinkage, Expansion, or Both? A Two-Stage Dynamic View," arXiv:2510.04028 (Oct 2025).

Key insight: capability shrinkage and expansion are both real but occur at different training phases. Initially, exploitation narrows boundaries; with prolonged training, exploration expands them. On AIME 2025, their GRPO-N method reaches Pass@256 of 66.7% versus the base model's 46.7%.

#### 6. Behavior Injection (arXiv 2505.18917)

**Citation:** "Behavior Injection: Preparing Language Models for Reinforcement Learning," arXiv:2505.18917 (May 2025).

Core finding: "models lacking sufficient behavioral diversity in their training data plateau or degrade under RL, while augmented models show substantial gains." The pre-RL coverage of diverse behaviors determines which capabilities can be effectively selected during reinforcement learning.

### Synthesized Counter-Argument

The reviewer's challenge rests on a false dichotomy. Sparse policy selection and training distribution diversity are not alternatives -- they are **complementary**. Precisely BECAUSE RL operates through sparse selection at high-entropy decision points, the training distribution becomes MORE important, not less. Here is why:

1. **Selection requires coverage:** RL can only select behaviors the training distribution exposes. The base model contains vast latent capabilities, but on-policy RL training only encounters those triggered by training prompts. Different difficulty x topic combinations activate different decision points and different latent behaviors (Tailor, Behavior Injection).

2. **Polarization makes diversity essential:** Sharper Primitives shows RLVR polarizes -- sharpening some primitives while sacrificing others. Without comprehensive coverage, you sharpen a narrow subset while the rest degrade. The multiplicative compounding means each un-sharpened primitive type creates an exponential bottleneck.

3. **Narrow training causes capability collapse:** RL-PLUS demonstrates that training on limited distributions causes "capability boundary collapse" where pass@k degrades. Diverse distributions are the antidote.

4. **The "ceiling" is not fixed:** ProRL shows that with sufficient diversity and duration, RL can access capabilities that appear inaccessible through base model sampling alone, challenging the premise that the base model ceiling is immovable.

---

## TOPIC 2: Rollout Count Effects in RLVR

### Finding 1: MC-GRPO -- Direct Group Size Ablation (arXiv 2601.22582)

**Citation:** "MC-GRPO: Median-Centered Group Relative Policy Optimization for Small-Rollout Reinforcement Learning," arXiv:2601.22582 (Jan 2026).

Concrete ablation on Qwen3-1.7B, GSM8K:

| Group Size (G) | Standard GRPO | MC-GRPO | Improvement |
|---|---|---|---|
| G=2 | 78.92% | 83.54% | +4.62 pp |
| G=4 | 81.34% | 84.01% | +2.67 pp |
| G=8 | 84.53% | 84.60% | +0.07 pp |

Key mechanism: small rollouts cause "advantage sign flips" where a single outlier reward shifts the mean baseline, reversing intended update directions. The authors prove empirically that "increasing [sign noise] consistently reduces final GSM8K accuracy."

### Finding 2: Gradient Starvation at Small Group Sizes (arXiv 2605.07689)

**Citation:** "Gradient Starvation in Binary-Reward GRPO: Why Group-Mean Centering Fails and Why the Simplest Fix Works," arXiv:2605.07689 (May 2026).

The degeneracy probability for binary rewards at success probability p is:

> D(p, G) = p^G + (1-p)^G

At G=4 with Qwen3.5-9B on GSM8K: 69.25% of groups were degenerate (54.75% all-fail, 14.50% all-pass), producing zero gradient signal. Larger groups reduce starvation:
- G=4: DrGRPO achieved only 28.4% accuracy
- G=8: DrGRPO recovered to 81.7% accuracy

Real degeneracy exceeds i.i.d. predictions by ~60% due to bimodal prompt difficulty distributions (Jensen's inequality).

### Finding 3: 2-GRPO vs 16-GRPO (arXiv 2510.00977)

**Citation:** "It Takes Two: Your GRPO Is Secretly DPO," arXiv:2510.00977 (Oct 2025).

Group size ablation (Qwen-1.5B):
- 2-GRPO achieves 97.6% of 16-GRPO's average performance using only 12.5% of rollouts and 21.0% of training time
- 2-GRPO+RS (with resampling) outperforms 16-GRPO while using ~half the training time
- Mean@32 differences among G=2,4,8,16 are "consistently small"

However, note this paper argues for FEWER rollouts being sufficient, framing GRPO as contrastive learning where "Monte Carlo estimation is unbiased regardless of sample size."

### Finding 4: Variance Scales Inversely with Rollout Count (arXiv 2511.03710)

**Citation:** "Shrinking the Variance: Shrinkage Baselines for Reinforcement Learning with Verifiable Rewards," arXiv:2511.03710 (Nov 2025).

The fundamental problem: "RLVR training typically uses large batch sizes but fewer rollouts per prompt due to inference costs, with the number of rollouts per prompt often limited to 16 or fewer."

Performance by generation count (Qwen2.5-0.5B, GSM8k):

| Generations | RLOO | Shrinkage |
|---|---|---|
| 2 | 54.49% | 55.22% |
| 4 | 56.34% | 57.33% |
| 8 | 58.31% | 58.93% |

Gradient variance reduction from shrinkage: 11.2% to 67.1% across models. The shrinkage coefficient automatically decreases with more rollouts since "intra-prompt estimates become more reliable."

### Finding 5: Binary Reward Estimation Variance (arXiv 2603.18444)

**Citation:** "Discounted Beta-Bernoulli Reward Estimation for Sample-Efficient Reinforcement Learning with Verifiable Rewards," arXiv:2603.18444 (Mar 2026).

Point estimator variance for binary rewards: Var = p(1-p)/N, where N is rollout count. The DBB estimator reduces this by factor (1-w)^2 using historical information.

"DBB estimator consistently outperforms the point estimator for N up to 16" -- the regime where most practical RLVR training operates.

Results: GRPO-DBB achieves "average Acc@8 improvements of 3.43 points for Qwen3-1.7B and 2.32 points for Qwen3-8B" over standard GRPO.

### Finding 6: Optimal Pass Rate and Rollout Informativeness (arXiv 2605.05112)

**Citation:** "Rollout Pass-Rate Control: Steering Binary-Reward RL Toward Its Most Informative Regime," arXiv:2605.05112 (May 2026).

Four complementary quantities all peak at 50% pass rate:
- Reward entropy maximizes at p=0.5 (1.0 bit)
- Group-filtering survival peaks at p=0.5
- RLOO advantage energy maximizes at balanced outcomes
- Success-failure contrastive pairs maximize at balanced outcomes

At N=8 rollouts, skewed groups (1/8 or 7/8 pass rate) provide only ~54% of the information content and ~44% of contrastive pairs compared to balanced 4/8 groups.

### Finding 7: Depth-Breadth Synergy (arXiv 2508.13755)

**Citation:** "Depth-Breadth Synergy in RLVR: Unlocking LLM Reasoning Gains with Adaptive Exploration," arXiv:2508.13755 (Aug 2025).

"Naively scaling rollout size can even harm Pass@K performance" (Qwen2.5-Math-1.5B). Increased batch breadth (128 to 3072) "acts as implicit entropy regularization," sustaining token-level entropy and preventing premature convergence -- independent of rollout count.

### Summary on Rollout Count

The evidence is nuanced rather than one-directional:

**In favor of more rollouts:** MC-GRPO, gradient starvation, and variance analyses all show clear degradation below G=8, with binary rewards particularly problematic at small G due to degenerate groups producing zero gradients. The variance of per-prompt mean estimation scales as p(1-p)/N, making small N unreliable.

**Complicating factor:** The 2-GRPO paper shows that with proper handling (resampling, contrastive framing), G=2 can approach G=16 performance. This suggests the optimal G depends on the specific algorithmic variant, and improvements to baseline estimation (shrinkage, median-centering, Beta-Bernoulli) can partially compensate for fewer rollouts.

**The strongest statistical argument:** For binary rewards with success probability p, the probability of a degenerate (uninformative) group is p^G + (1-p)^G. At p=0.5 (optimal), this equals 2*(0.5)^G = 1/2^(G-1). So G=4 gives 12.5% degeneracy, G=8 gives 0.78%, and G=16 gives 0.003%. At non-optimal pass rates (e.g., p=0.2), degeneracy at G=4 is 41.8% vs 16.8% at G=8 -- much more severe.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7ff2631-3683-4984-b651-f81e48980a19",
  "isSidechain": true,
  "agentId": "a7ecfe27cc3cea032",
  "requestId": "req_011CbU6piUqZAuDWkvE8P2b1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a8f12c01-9084-4823-8e19-30380454072f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "61bf67c1-7567-40f9-aff3-05f1882e1be9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JB96rB9DSP3GHekGUib88N",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1391,
      "cache_read_input_tokens": 36541,
      "output_tokens": 3940,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1391
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3940,
          "cache_read_input_tokens": 36541,
          "cache_creation_input_tokens": 1391,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1391,
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
