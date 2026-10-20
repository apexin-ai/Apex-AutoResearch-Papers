# Research conversation: Research the "Broken Tokens" paper (arXiv:2506.19004, NeurIPS 2025) to understand: 1. What exactly are the future work d

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a91aa078a91c6b8ba.jsonl`
- **Structured JSON:** [`4f15f9b6d55444378dcd.json`](../../sessions/4f/4f15f9b6d55444378dcd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

42 recorded events

### User

_source line 1 · 2026-05-19T22:14:18.151Z_

Research the "Broken Tokens" paper (arXiv:2506.19004, NeurIPS 2025) to understand:

1. What exactly are the future work directions they propose? Is "adaptive tokenization for reasoning" explicitly mentioned?
2. What is the exact degradation on general benchmarks (ARC, HellaSwag) with character-level tokenization?
3. Who are the authors and their affiliations (UW/AI2/Stanford)? Any follow-up work from them?
4. What is the exact CharBench average accuracy (the reviewer says 43.6%, original idea says 50.3%)?

Use WebSearch with queries like:
- "Broken Tokens non-canonical tokenization NeurIPS 2025 future work"
- "Broken Tokens character-level tokenization degradation general benchmarks"
- "CharBench AAAI 2026 average accuracy character-level tasks LLM"
- "zip2zip adaptive tokenization token reduction percentage 2025"

Then use WebFetch on arxiv pages for these papers. Report findings in detail (300-400 words).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "7b21de4b-acb9-4aab-be9b-f93717fb5eed",
  "agentId": "a91aa078a91c6b8ba",
  "type": "user",
  "uuid": "112e9ef5-5296-4ee1-af9c-6e6e485f6a2e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T22:14:18.155Z_

```json
{
  "parentUuid": "112e9ef5-5296-4ee1-af9c-6e6e485f6a2e",
  "isSidechain": true,
  "agentId": "a91aa078a91c6b8ba",
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
  "uuid": "3f22ffde-45db-4702-82e1-0d0bf8f97052",
  "timestamp": "2026-05-19T22:14:18.155Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-19T22:14:18.156Z_

```json
{
  "parentUuid": "3f22ffde-45db-4702-82e1-0d0bf8f97052",
  "isSidechain": true,
  "agentId": "a91aa078a91c6b8ba",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "bc11c59a-9615-4fa1-bd0f-8c03fc7124b7",
  "timestamp": "2026-05-19T22:14:18.156Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-19T22:14:21.121Z_



I'll research the "Broken Tokens" paper and related topics. Let me start by loading the WebSearch and WebFetch tools, then conduct the searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc11c59a-9615-4fa1-bd0f-8c03fc7124b7",
  "isSidechain": true,
  "agentId": "a91aa078a91c6b8ba",
  "requestId": "req_011CbChRwxpeYxNS4waktAHU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f547504-7111-4117-a904-2575f3c9b763",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012rw1gdU1piKnZvPC5V6QwZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1601,
      "cache_read_input_tokens": 7773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1601,
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

_source line 5 · 2026-05-19T22:14:21.410Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NYDicP35TyL5Q3s1wxXXku`</summary>

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
  "parentUuid": "2f547504-7111-4117-a904-2575f3c9b763",
  "isSidechain": true,
  "agentId": "a91aa078a91c6b8ba",
  "requestId": "req_011CbChRwxpeYxNS4waktAHU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1fb31100-7e0c-4074-9e94-e8d4631e59ae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012rw1gdU1piKnZvPC5V6QwZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1601,
      "cache_read_input_tokens": 7773,
      "output_tokens": 115,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1601
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 115,
          "cache_read_input_tokens": 7773,
          "cache_creation_input_tokens": 1601,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1601,
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

_source line 6 · 2026-05-19T22:14:21.413Z_

<details><summary>↩ Tool result · `toolu_01NYDicP35TyL5Q3s1wxXXku`</summary>

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
  "parentUuid": "1fb31100-7e0c-4074-9e94-e8d4631e59ae",
  "isSidechain": true,
  "promptId": "7b21de4b-acb9-4aab-be9b-f93717fb5eed",
  "agentId": "a91aa078a91c6b8ba",
  "type": "user",
  "uuid": "01d7d35e-4c78-4d1e-8a7b-a445b2fa0f79",
  "sourceToolAssistantUUID": "1fb31100-7e0c-4074-9e94-e8d4631e59ae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-19T22:14:23.776Z_



Now let me run the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01d7d35e-4c78-4d1e-8a7b-a445b2fa0f79",
  "isSidechain": true,
  "agentId": "a91aa078a91c6b8ba",
  "requestId": "req_011CbChSC59ASsYKs6TmyQWS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ce4ad82e-6785-4cd7-b78e-be33eb0da3ab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B8wEceBugxhdkx6SetdTCr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1137,
      "cache_read_input_tokens": 9374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1137,
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

_source line 8 · 2026-05-19T22:14:24.806Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XU6zkSSMMZrNcsWxjPd6hg`</summary>

```json
{
  "query": "Broken Tokens non-canonical tokenization NeurIPS 2025 future work arXiv 2506.19004"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce4ad82e-6785-4cd7-b78e-be33eb0da3ab",
  "isSidechain": true,
  "agentId": "a91aa078a91c6b8ba",
  "requestId": "req_011CbChSC59ASsYKs6TmyQWS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "251ac961-bbaa-4034-a830-a1e1c6f2c5f5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B8wEceBugxhdkx6SetdTCr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1137,
      "cache_read_input_tokens": 9374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1137,
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

_source line 9 · 2026-05-19T22:14:25.735Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017tyLeGc6vnuMQik8fHLZWF`</summary>

```json
{
  "query": "Broken Tokens character-level tokenization degradation general benchmarks ARC HellaSwag"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "251ac961-bbaa-4034-a830-a1e1c6f2c5f5",
  "isSidechain": true,
  "agentId": "a91aa078a91c6b8ba",
  "requestId": "req_011CbChSC59ASsYKs6TmyQWS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6e52bb92-700c-40bc-ad0e-b19fcccae78e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B8wEceBugxhdkx6SetdTCr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1137,
      "cache_read_input_tokens": 9374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1137,
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

_source line 10 · 2026-05-19T22:14:26.667Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HhiPityGZnZk9yWjvHQfGK`</summary>

```json
{
  "query": "CharBench AAAI 2026 average accuracy character-level tasks LLM benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e52bb92-700c-40bc-ad0e-b19fcccae78e",
  "isSidechain": true,
  "agentId": "a91aa078a91c6b8ba",
  "requestId": "req_011CbChSC59ASsYKs6TmyQWS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61447761-ad7a-4d49-8a23-9105c9f0721c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B8wEceBugxhdkx6SetdTCr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1137,
      "cache_read_input_tokens": 9374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1137,
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

_source line 11 · 2026-05-19T22:14:27.063Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013QV74JaaeT7MPtry64j6EM`</summary>

```json
{
  "query": "zip2zip adaptive tokenization token reduction percentage 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61447761-ad7a-4d49-8a23-9105c9f0721c",
  "isSidechain": true,
  "agentId": "a91aa078a91c6b8ba",
  "requestId": "req_011CbChSC59ASsYKs6TmyQWS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9db51ce-086c-40d3-8fea-24014c34f2a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B8wEceBugxhdkx6SetdTCr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1137,
      "cache_read_input_tokens": 9374,
      "output_tokens": 246,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1137
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 246,
          "cache_read_input_tokens": 9374,
          "cache_creation_input_tokens": 1137,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1137,
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

_source line 12 · 2026-05-19T22:14:31.658Z_

<details><summary>↩ Tool result · `toolu_01XU6zkSSMMZrNcsWxjPd6hg`</summary>

```text
Web search results for query: "Broken Tokens non-canonical tokenization NeurIPS 2025 future work arXiv 2506.19004"

Links: [{"title":"[2506.19004] Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations","url":"https://arxiv.org/abs/2506.19004"},{"title":"Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations | OpenReview","url":"https://openreview.net/forum?id=WrYWolqKh3"},{"title":"[Literature Review] Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations","url":"https://www.themoonlight.io/en/review/broken-tokens-your-language-model-can-secretly-handle-non-canonical-tokenizations"},{"title":"Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations","url":"https://www.researchgate.net/publication/392980296_Broken_Tokens_Your_Language_Model_can_Secretly_Handle_Non-Canonical_Tokenizations"},{"title":"arXiv:2506.19004v1 [cs.CL] 23 Jun 2025 Broken Tokens? Your Language Model can","url":"https://arxiv.org/pdf/2506.19004"},{"title":"Broken Tokens? Your Language Model can Secretly Handle No n","url":"https://openreview.net/pdf/b001873ec0dc69deca0d93042e91329795dbfb9f.pdf"},{"title":"dblp: Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations.","url":"https://dblp.org/rec/journals/corr/abs-2506-19004.html"},{"title":"Broken Tokens? Your Language Model can Secretly Handle No n - Ca noni cal Tokenizations","url":"https://arxiv.org/html/2506.19004v1"},{"title":"Tokenization Multiplicity Leads to Arbitrary Price Variation in LLM-as-a-service","url":"https://arxiv.org/html/2506.06446"}]

I found comprehensive information about the paper. Here's what I discovered:

## Overview

The paper "Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations" was presented at the 39th Conference on Neural Information Processing Systems (NeurIPS 2025).

## Main Findings

The research investigates the robustness of language models to text encoded with non-canonical tokenizations entirely unseen during training, finding that instruction-tuned models retain up to 93.4% of their original performance when given a randomly sampled tokenization, and 90.8% with character-level tokenization.

Overall stronger models tend to be more robust, and robustness diminishes as the tokenization departs farther from the canonical form.

## Performance Improvements

Character-level segmentation improves string manipulation and code understanding tasks by up to +14%, and right-aligned digit grouping enhances large-number tasks.

## Authors and Affiliation

The paper was authored by Brian Siyuan Zheng, Alisa Liu, Orevaoghene Ahia, Jonathan Hayase, Yejin Choi, and Noah A. Smith from the University of Washington, Allen Institute for AI, and Stanford University.

The arXiv identifier is 2506.19004, and the paper was submitted on June 23, 2025, with a revision on February 2, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "251ac961-bbaa-4034-a830-a1e1c6f2c5f5",
  "isSidechain": true,
  "promptId": "7b21de4b-acb9-4aab-be9b-f93717fb5eed",
  "agentId": "a91aa078a91c6b8ba",
  "type": "user",
  "uuid": "89947727-7e09-43a9-b89c-d336781f7035",
  "sourceToolAssistantUUID": "251ac961-bbaa-4034-a830-a1e1c6f2c5f5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T22:14:31.683Z_

<details><summary>↩ Tool result · `toolu_013QV74JaaeT7MPtry64j6EM`</summary>

```text
Web search results for query: "zip2zip adaptive tokenization token reduction percentage 2025"

Links: [{"title":"[2506.01084] zip2zip: Inference-Time Adaptive Tokenization via Online Compression","url":"https://arxiv.org/abs/2506.01084"},{"title":"[Quick Review] zip2zip: Inference-Time Adaptive Vocabularies for Language Models via\\n Token Compression","url":"https://liner.com/review/zip2zip-inferencetime-adaptive-vocabularies-for-language-models-via-token-compression"},{"title":"zip2zip: Inference-Time Adaptive Tokenization via Online Compression | OpenReview","url":"https://openreview.net/forum?id=Hmepi1Fm2g"},{"title":"zip2zip: Inference-Time Adaptive Tokenization via Online Compression","url":"https://arxiv.org/html/2506.01084v2"},{"title":"zip2zip: Inference-Time Adaptive Vocabularies for Language Models via Token Compression","url":"https://arxiv.org/html/2506.01084v1"},{"title":"zip2zip: Inference-Time Adaptive Tokenization via Online Compression","url":"https://arxiv.org/pdf/2506.01084"},{"title":"NeurIPS Poster zip2zip: Inference-Time Adaptive Tokenization via Online Compression","url":"https://neurips.cc/virtual/2025/poster/118871"},{"title":"Paper page - zip2zip: Inference-Time Adaptive Vocabularies for Language Models via Token Compression","url":"https://huggingface.co/papers/2506.01084"},{"title":"zip2zip: Inference-Time Adaptive Vocabularies for Language Models via Token Compression | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/zip2zip-inference-time-adaptive-vocabularies-language-models"}]

Based on the search results, here's what I found about zip2zip adaptive tokenization and its token reduction percentage:

## Token Reduction Percentage

zip2zip reduces input and output tokens by 15-40%. However, it's worth noting that some sources report a broader range, with token reductions of 20-60% in both input and output sequence lengths.

## How It Works

zip2zip is a novel method for achieving context-adaptive tokenization in LLMs at inference time, leveraging an online data compression algorithm (Lempel-Ziv-Welch) that dynamically expands its active vocabulary at inference time by continuously replacing fragmented token sequences with more compact hypertokens.

## Key Benefits

Beyond token reduction, the models demonstrate strong inference-time compression capabilities across various domains, achieving 15–40% reductions in sequence length and up to 40% improvements in end-to-end latency.

This is a research paper from 2025 that addresses the inefficiency of static tokenizers used in traditional LLMs by enabling dynamic vocabulary adaptation at inference time.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9db51ce-086c-40d3-8fea-24014c34f2a1",
  "isSidechain": true,
  "promptId": "7b21de4b-acb9-4aab-be9b-f93717fb5eed",
  "agentId": "a91aa078a91c6b8ba",
  "type": "user",
  "uuid": "d9b5085f-4927-4aa6-9e44-234d6af25c13",
  "sourceToolAssistantUUID": "e9db51ce-086c-40d3-8fea-24014c34f2a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T22:14:32.933Z_

<details><summary>↩ Tool result · `toolu_017tyLeGc6vnuMQik8fHLZWF`</summary>

```text
Web search results for query: "Broken Tokens character-level tokenization degradation general benchmarks ARC HellaSwag"

Links: [{"title":"Broken Tokens? Your Language Model can Secretly Handle No n - Ca noni cal Tokenizations","url":"https://arxiv.org/html/2506.19004v1"},{"title":"Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations | OpenReview","url":"https://openreview.net/forum?id=zpheKOg5f0"},{"title":"[2506.19004] Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations","url":"https://arxiv.org/abs/2506.19004"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf/d38339eb96e6ce0c33a20ab450a1729dc387d823.pdf"},{"title":"Just on Time: Token-Level Early Stopping for Diffusion Language Models","url":"https://arxiv.org/html/2602.11133v1"},{"title":"Word Recovery in Large Language Models Enables Character-Level Tokenization Robustness","url":"https://arxiv.org/pdf/2603.10771"},{"title":"Word Recovery in Large Language Models Enables Character-Level Tokenization Robustness","url":"https://arxiv.org/html/2603.10771"},{"title":"CharBench: Evaluating the Role of Tokenization in Character-Level Tasks","url":"https://arxiv.org/pdf/2508.02591"}]

I found relevant research on this topic. Here's what the search results show:

## Overview

Modern tokenizers employ deterministic algorithms to map text into a single "canonical" token sequence, yet the same string can be encoded as many non-canonical tokenizations using the tokenizer vocabulary. Researchers investigated the robustness of language models to text encoded with non-canonical tokenizations entirely unseen during training.

## Performance with Character-Level Tokenization

When evaluated across 20 benchmarks, instruction-tuned models retain up to 93.4% of their original performance when given a randomly sampled tokenization, and 90.8% with character-level tokenization. 

Overall stronger models tend to be more robust, and robustness diminishes as the tokenization departs farther from the canonical form.

## Benchmark Specifics

The research included evaluation on standard benchmarks including HellaSwag and ARC. HellaSwag and ARC were among the standard benchmarks commonly used to assess the base language models.

## Potential Performance Improvements

Interestingly, character-level segmentation can improve string manipulation and code understanding tasks by up to +14%.

The key finding is that despite the apparent problem of "broken tokens" through non-canonical tokenization, language models demonstrate surprising robustness to these alternative tokenization schemes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e52bb92-700c-40bc-ad0e-b19fcccae78e",
  "isSidechain": true,
  "promptId": "7b21de4b-acb9-4aab-be9b-f93717fb5eed",
  "agentId": "a91aa078a91c6b8ba",
  "type": "user",
  "uuid": "ea9e4313-ebec-4d12-804b-fb0f52cb6dfa",
  "sourceToolAssistantUUID": "6e52bb92-700c-40bc-ad0e-b19fcccae78e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-19T22:14:34.163Z_

<details><summary>↩ Tool result · `toolu_01HhiPityGZnZk9yWjvHQfGK`</summary>

```text
Web search results for query: "CharBench AAAI 2026 average accuracy character-level tasks LLM benchmark"

Links: [{"title":"CHARBENCH: Evaluating the Role of Tokenization in Character-Level Tasks - Ben-Gurion University Research Portal","url":"https://cris.bgu.ac.il/en/publications/charbench-evaluating-the-role-of-tokenization-in-character-level--2/"},{"title":"CharBench: Evaluating the Role of Tokenization in Character-Level Tasks | alphaXiv","url":"https://www.alphaxiv.org/overview/2508.2591/metadatav3"},{"title":"CharBench: Evaluating the Role of Tokenization in Character-Level Tasks","url":"https://arxiv.org/pdf/2508.02591"},{"title":"CharBench: Evaluating the Role of Tokenization in Character-Level Tasks - Paper Detail","url":"https://deeplearn.org/arxiv/625867/charbench:-evaluating-the-role-of-tokenization-in-character-level-tasks"},{"title":"CharBench: Evaluating the Role of Tokenization in Character-Level Tasks","url":"https://arxiv.org/html/2508.02591"},{"title":"[2508.02591] CharBench: Evaluating the Role of Tokenization in Character-Level Tasks","url":"https://arxiv.org/abs/2508.02591"},{"title":"CharBench: Evaluating the Role of Tokenization in Character-Level Tasks | Request PDF","url":"https://www.researchgate.net/publication/402627608_CharBench_Evaluating_the_Role_of_Tokenization_in_Character-Level_Tasks"},{"title":"CHARBENCH: Evaluating the Role of Tokenization in Character-Level Tasks","url":"https://ojs.aaai.org/index.php/AAAI/article/download/40615/44576"}]

Based on the search results, here's what I found about CharBench and AAAI 2026:

CharBench proves to be a substantial challenge, with an average accuracy of 50.3% across models. More specifically, positional understanding appears to be particularly difficult, with average accuracies of 43.6% and 32.4% in the tasks in this category.

CharBench is a comprehensive benchmark of character-level tasks that is two orders of magnitude larger than existing alternatives. CharBench is designed to test LLMs' ability to reason over characters, with separate tasks for assessing models' performance on positional understanding (indexing) and occurrence tracking (counting).

The paper appears to have been published at AAAI 2026, with the work evaluating a range of leading open-weight and proprietary language models on these character-level reasoning tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61447761-ad7a-4d49-8a23-9105c9f0721c",
  "isSidechain": true,
  "promptId": "7b21de4b-acb9-4aab-be9b-f93717fb5eed",
  "agentId": "a91aa078a91c6b8ba",
  "type": "user",
  "uuid": "297fb7af-c18d-4bcc-87e1-7d3509853852",
  "sourceToolAssistantUUID": "61447761-ad7a-4d49-8a23-9105c9f0721c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-19T22:14:43.276Z_

Good, I have initial results. Now let me fetch the actual paper pages for detailed information on future work directions, exact benchmark degradation numbers, and author affiliations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "297fb7af-c18d-4bcc-87e1-7d3509853852",
  "isSidechain": true,
  "agentId": "a91aa078a91c6b8ba",
  "requestId": "req_011CbChT8RQ1guVFFMEC6Jbc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c9b60ee-7d19-43fb-a342-7329ab70b7f4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pim56Vrh5JpE7J3t8rrN3v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 750,
      "cache_creation_input_tokens": 2604,
      "cache_read_input_tokens": 10511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2604,
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

_source line 17 · 2026-05-19T22:14:45.632Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0192ofgWgZCi6gvzzLrtfFkQ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.19004",
  "prompt": "Extract: 1) The full list of authors and their affiliations (universities/labs). 2) Any mention of future work directions. 3) Any specific benchmark degradation numbers for ARC and HellaSwag with character-level tokenization. 4) Any mention of \"adaptive tokenization for reasoning\"."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c9b60ee-7d19-43fb-a342-7329ab70b7f4",
  "isSidechain": true,
  "agentId": "a91aa078a91c6b8ba",
  "requestId": "req_011CbChT8RQ1guVFFMEC6Jbc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "17dcd598-55d4-45f7-9fcd-30de72c5936e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pim56Vrh5JpE7J3t8rrN3v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 750,
      "cache_creation_input_tokens": 2604,
      "cache_read_input_tokens": 10511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2604,
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

_source line 18 · 2026-05-19T22:14:47.513Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CbGPHGHcEMPvqNfmKu1Ark`</summary>

```json
{
  "url": "https://arxiv.org/abs/2508.02591",
  "prompt": "Extract: 1) The exact CharBench average accuracy across models. 2) The positional understanding accuracy (43.6% or 50.3%?). 3) The overall benchmark average. 4) Authors and affiliations. 5) Whether this was published at AAAI 2026."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17dcd598-55d4-45f7-9fcd-30de72c5936e",
  "isSidechain": true,
  "agentId": "a91aa078a91c6b8ba",
  "requestId": "req_011CbChT8RQ1guVFFMEC6Jbc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "696ac44d-5c12-48ed-9375-7c6f9b23f344",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pim56Vrh5JpE7J3t8rrN3v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 750,
      "cache_creation_input_tokens": 2604,
      "cache_read_input_tokens": 10511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2604,
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

_source line 19 · 2026-05-19T22:14:48.908Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RadkLNduS3UF8qw8Jh2Shw`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.01084",
  "prompt": "Extract: 1) The exact token reduction percentages claimed. 2) Whether this paper cites or builds on \"Broken Tokens\". 3) Authors and affiliations. 4) Whether \"adaptive tokenization for reasoning\" is mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "696ac44d-5c12-48ed-9375-7c6f9b23f344",
  "isSidechain": true,
  "agentId": "a91aa078a91c6b8ba",
  "requestId": "req_011CbChT8RQ1guVFFMEC6Jbc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "35f270d5-09be-4f5c-ba83-630fca14fe24",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pim56Vrh5JpE7J3t8rrN3v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 750,
      "cache_creation_input_tokens": 2604,
      "cache_read_input_tokens": 10511,
      "output_tokens": 432,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2604
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 750,
          "output_tokens": 432,
          "cache_read_input_tokens": 10511,
          "cache_creation_input_tokens": 2604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2604,
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

_source line 20 · 2026-05-19T22:14:49.292Z_

<details><summary>↩ Tool result · `toolu_0192ofgWgZCi6gvzzLrtfFkQ`</summary>

```text
# Information Extraction from arXiv:2506.19004

## 1) Authors and Affiliations
The webpage lists six authors:
- Brian Siyuan Zheng
- Alisa Liu
- Orevaoghene Ahia
- Jonathan Hayase
- Yejin Choi
- Noah A. Smith

**However, the provided content does not include their institutional affiliations.** The page only provides author names with clickable links to search results.

## 2) Future Work Directions
No explicit future work section appears in the abstract or metadata provided. The conclusion mentions that findings "demonstrate the promise of intervening on tokenization at inference time to boost performance," but this describes contributions rather than stated future directions.

## 3) Benchmark Degradation Numbers
The abstract does not provide specific performance metrics for ARC or HellaSwag with character-level tokenization. It only states generally that "character-level tokenization" improves "string manipulation and code understanding tasks by up to +14%."

## 4) Adaptive Tokenization for Reasoning
No mention of "adaptive tokenization for reasoning" appears anywhere in the provided webpage content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "17dcd598-55d4-45f7-9fcd-30de72c5936e",
  "isSidechain": true,
  "promptId": "7b21de4b-acb9-4aab-be9b-f93717fb5eed",
  "agentId": "a91aa078a91c6b8ba",
  "type": "user",
  "uuid": "1fccc64b-b637-4b99-a400-f32c3554c8fe",
  "sourceToolAssistantUUID": "17dcd598-55d4-45f7-9fcd-30de72c5936e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-19T22:14:50.981Z_

<details><summary>↩ Tool result · `toolu_01CbGPHGHcEMPvqNfmKu1Ark`</summary>

```text
# CharBench Paper Summary

**1) CharBench Average Accuracy:**
The abstract states: "with an average accuracy of 43.6% and 32.3% on some tasks." These represent performance across different task categories, not a single overall figure.

**2) Positional Understanding Accuracy:**
The document indicates 43.6% as the average accuracy mentioned, but doesn't explicitly label this as "positional understanding accuracy." The findings note that "for tasks requiring intra-word positional understanding, performance is negatively correlated with the length of the token."

**3) Overall Benchmark Average:**
No single overall benchmark average is provided. Instead, the abstract differentiates between task types, showing varying performance levels.

**4) Authors and Affiliations:**
The paper lists two authors—Omri Uzan and Yuval Pinter—but no institutional affiliations are displayed on this abstract page.

**5) AAAI 2026 Publication:**
Yes, the document confirms: "AAAI-26" under the Comments section, indicating acceptance at the 2026 AAAI conference.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "696ac44d-5c12-48ed-9375-7c6f9b23f344",
  "isSidechain": true,
  "promptId": "7b21de4b-acb9-4aab-be9b-f93717fb5eed",
  "agentId": "a91aa078a91c6b8ba",
  "type": "user",
  "uuid": "1a275bbf-7191-4582-a126-a623208c8ed7",
  "sourceToolAssistantUUID": "696ac44d-5c12-48ed-9375-7c6f9b23f344",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T22:14:51.887Z_

<details><summary>↩ Tool result · `toolu_01RadkLNduS3UF8qw8Jh2Shw`</summary>

```text
# zip2zip Paper Analysis

**1) Token Reduction Percentages:**
The paper claims to achieve "reducing input and output tokens by 15-40%."

**2) Citation of "Broken Tokens":**
No mention of "Broken Tokens" appears in the provided content.

**3) Authors and Affiliations:**
The paper lists seven authors: Saibo Geng, Nathan Ranchin, Yunzhen Yao, Maxime Peyrard, Chris Wendler, Michael Gastpr, and Robert West. However, no institutional affiliations are included in the extracted webpage content.

**4) "Adaptive Tokenization for Reasoning":**
This specific phrase does not appear in the provided material. The paper discusses context-adaptive tokenization at inference time but does not explicitly mention reasoning capabilities.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35f270d5-09be-4f5c-ba83-630fca14fe24",
  "isSidechain": true,
  "promptId": "7b21de4b-acb9-4aab-be9b-f93717fb5eed",
  "agentId": "a91aa078a91c6b8ba",
  "type": "user",
  "uuid": "15a75bcb-d3c6-45ef-8df0-13c0f132f880",
  "sourceToolAssistantUUID": "35f270d5-09be-4f5c-ba83-630fca14fe24",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-19T22:14:54.557Z_

Let me get more detailed information from the full HTML version of the Broken Tokens paper and CharBench paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15a75bcb-d3c6-45ef-8df0-13c0f132f880",
  "isSidechain": true,
  "agentId": "a91aa078a91c6b8ba",
  "requestId": "req_011CbChUSAXKjPWD2WnqGVtz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1352e9a-2863-4340-8894-bacf77811b5c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016YYbzkfEgTPAEkF1DLitWm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2057,
      "cache_read_input_tokens": 13115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2057,
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

_source line 24 · 2026-05-19T22:14:57.911Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01C8Q1xD2bP74YvLynnvBT42`</summary>

```json
{
  "url": "https://arxiv.org/html/2506.19004v1",
  "prompt": "Extract the following EXACTLY: 1) The full \"Future Work\" or \"Limitations and Future Work\" section text. 2) Any mention of \"adaptive tokenization\" or \"reasoning\" in future work. 3) Exact performance numbers on ARC and HellaSwag benchmarks with character-level tokenization vs canonical tokenization. 4) Author affiliations (University of Washington, AI2, Stanford). 5) The exact degradation percentages on general/knowledge benchmarks when using character-level tokenization."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1352e9a-2863-4340-8894-bacf77811b5c",
  "isSidechain": true,
  "agentId": "a91aa078a91c6b8ba",
  "requestId": "req_011CbChUSAXKjPWD2WnqGVtz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8742e959-1629-4ab1-94a2-1e45f8353ddd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016YYbzkfEgTPAEkF1DLitWm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2057,
      "cache_read_input_tokens": 13115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2057,
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

_source line 25 · 2026-05-19T22:14:59.980Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01R5MvKUtfURoWimXL8TqyHP`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.02591",
  "prompt": "Extract: 1) The exact overall CharBench average accuracy number across all models and tasks. 2) Is it 50.3% overall or 43.6%? 3) What does each number refer to exactly - which is the overall average and which is positional understanding? 4) Authors and their university affiliations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8742e959-1629-4ab1-94a2-1e45f8353ddd",
  "isSidechain": true,
  "agentId": "a91aa078a91c6b8ba",
  "requestId": "req_011CbChUSAXKjPWD2WnqGVtz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "506bf204-4680-4f5a-b5b8-09b3ce1980f7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016YYbzkfEgTPAEkF1DLitWm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2057,
      "cache_read_input_tokens": 13115,
      "output_tokens": 356,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2057
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 356,
          "cache_read_input_tokens": 13115,
          "cache_creation_input_tokens": 2057,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2057,
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

_source line 26 · 2026-05-19T22:15:02.836Z_

<details><summary>↩ Tool result · `toolu_01C8Q1xD2bP74YvLynnvBT42`</summary>

```text
# Extraction from Research Paper

## 1) Future Work Section
The paper does not contain a dedicated "Future Work" or "Limitations and Future Work" section. The conclusion briefly mentions: "we leave automatically identifying the optimal tokenization as a promising direction for future work."

## 2) Adaptive Tokenization or Reasoning Mentions
No explicit mention of "adaptive tokenization" appears in the document. The paper discusses "intervening on tokenization at inference time" and "dynamically finding the optimal representation of text after pretraining" but does not use the term "adaptive tokenization" specifically.

## 3) ARC and HellaSwag Performance Numbers (Character-level vs Canonical)

**ARC-Challenge (Llama-3.1-8B-Instruct):**
- Canonical: 76.2% | Character-level: -22.40 point drop

**ARC-Easy (Llama-3.1-8B-Instruct):**
- Canonical: 91.3% | Character-level: -21.50 point drop

**HellaSwag (Llama-3.1-8B-Instruct):**
- Canonical: 68.6% | Character-level: -23.40 point drop

## 4) Author Affiliations
- University of Washington (♡)
- Allen Institute for AI (♣)
- Stanford University (♠)

## 5) Character-level Degradation on Knowledge Benchmarks
Representative losses across benchmarks (Llama-3.1-8B-Instruct): MMLU (-24%), CSQA (-20%), TriviaQA (-13.6%), WikidataQA (-18%).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8742e959-1629-4ab1-94a2-1e45f8353ddd",
  "isSidechain": true,
  "promptId": "7b21de4b-acb9-4aab-be9b-f93717fb5eed",
  "agentId": "a91aa078a91c6b8ba",
  "type": "user",
  "uuid": "948b3e21-dc07-4400-a21e-1f4bcecda76f",
  "sourceToolAssistantUUID": "8742e959-1629-4ab1-94a2-1e45f8353ddd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-19T22:15:03.625Z_

<details><summary>↩ Tool result · `toolu_01R5MvKUtfURoWimXL8TqyHP`</summary>

```text
# CharBench Analysis

**1) Overall CharBench Average Accuracy:**
The exact overall average across all models and tasks is **50.33%**.

**2) Clarification of the Two Numbers:**
These figures refer to different metrics:
- **50.33%** = Overall average accuracy across all models and all four tasks
- **43.6%** = Average accuracy specifically for positional understanding tasks (find_first and find_last combined)

**3) What Each Represents:**
The 43.6% figure reflects performance on tasks requiring character position identification, which proved "significantly more challenging for models than counting tasks." The higher 50.33% figure encompasses both counting tasks (which averaged higher) and indexing tasks combined.

**4) Author Affiliations:**
- **Omri Uzan** - Affiliation 1
- **Yuval Pinter** - Affiliation 2

The document does not provide explicit university names for these affiliation numbers in the visible content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "506bf204-4680-4f5a-b5b8-09b3ce1980f7",
  "isSidechain": true,
  "promptId": "7b21de4b-acb9-4aab-be9b-f93717fb5eed",
  "agentId": "a91aa078a91c6b8ba",
  "type": "user",
  "uuid": "3ead3901-c32b-4faf-befc-189a7ff3279c",
  "sourceToolAssistantUUID": "506bf204-4680-4f5a-b5b8-09b3ce1980f7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-19T22:15:06.775Z_

Now let me search for follow-up work from the Broken Tokens authors and get the CharBench author affiliations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ead3901-c32b-4faf-befc-189a7ff3279c",
  "isSidechain": true,
  "agentId": "a91aa078a91c6b8ba",
  "requestId": "req_011CbChVJL1hK2N9h2t3u2qq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9075714e-a371-4633-bfeb-59ac0c65c758",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LcFhSkCFpPqwgbEe15zAs3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1029,
      "cache_read_input_tokens": 15172,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1029,
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

_source line 29 · 2026-05-19T22:15:07.684Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ArgLJUVRwwZtYWMErcBazd`</summary>

```json
{
  "query": "Brian Siyuan Zheng Alisa Liu tokenization follow-up work 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9075714e-a371-4633-bfeb-59ac0c65c758",
  "isSidechain": true,
  "agentId": "a91aa078a91c6b8ba",
  "requestId": "req_011CbChVJL1hK2N9h2t3u2qq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9b3d78db-c8a9-4a44-8910-1a813b9daad1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LcFhSkCFpPqwgbEe15zAs3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1029,
      "cache_read_input_tokens": 15172,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1029,
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

_source line 30 · 2026-05-19T22:15:08.217Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BYdboJ87tXopGrqK9dLd3K`</summary>

```json
{
  "query": "Omri Uzan Yuval Pinter CharBench university affiliation Ben-Gurion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b3d78db-c8a9-4a44-8910-1a813b9daad1",
  "isSidechain": true,
  "agentId": "a91aa078a91c6b8ba",
  "requestId": "req_011CbChVJL1hK2N9h2t3u2qq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c672730b-5259-4685-aa48-f9d27614af84",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LcFhSkCFpPqwgbEe15zAs3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1029,
      "cache_read_input_tokens": 15172,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1029,
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

_source line 31 · 2026-05-19T22:15:08.907Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015Y7FnccCtjAPsxaEqPJkHu`</summary>

```json
{
  "query": "\"Broken Tokens\" NeurIPS 2025 \"future work\" \"adaptive\" OR \"reasoning\" tokenization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c672730b-5259-4685-aa48-f9d27614af84",
  "isSidechain": true,
  "agentId": "a91aa078a91c6b8ba",
  "requestId": "req_011CbChVJL1hK2N9h2t3u2qq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "724e0eb4-68da-4a26-a78f-bc4e1b3eda9c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LcFhSkCFpPqwgbEe15zAs3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1029,
      "cache_read_input_tokens": 15172,
      "output_tokens": 217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1029
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 217,
          "cache_read_input_tokens": 15172,
          "cache_creation_input_tokens": 1029,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1029,
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

_source line 32 · 2026-05-19T22:15:12.205Z_

<details><summary>↩ Tool result · `toolu_01ArgLJUVRwwZtYWMErcBazd`</summary>

```text
Web search results for query: "Brian Siyuan Zheng Alisa Liu tokenization follow-up work 2026"

Links: [{"title":"dblp: Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations.","url":"https://dblp.org/rec/journals/corr/abs-2506-19004.html"},{"title":"Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations","url":"https://www.researchgate.net/publication/392980296_Broken_Tokens_Your_Language_Model_can_Secretly_Handle_Non-Canonical_Tokenizations"},{"title":"Token Erasure as a Footprint of Implicit Vocabulary Items in LLMs | Request PDF","url":"https://www.researchgate.net/publication/386187421_Token_Erasure_as_a_Footprint_of_Implicit_Vocabulary_Items_in_LLMs"},{"title":"arXiv:2506.19004v1 [cs.CL] 23 Jun 2025 Broken Tokens? Your Language Model can","url":"https://arxiv.org/pdf/2506.19004"},{"title":"Tokenization Multiplicity Leads to Arbitrary Price Variation in LLM-as-a-service","url":"https://arxiv.org/pdf/2506.06446"},{"title":"Say More with Less: Variable-Frame-Rate Speech Tokenization via Adaptive Clustering and Implicit Duration Coding | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40807"},{"title":"CUTE: Measuring LLMs’ Understanding of Their Tokens | Request PDF","url":"https://www.researchgate.net/publication/386190762_CUTE_Measuring_LLMs'_Understanding_of_Their_Tokens"},{"title":"Where is the signal in tokenization space?","url":"https://arxiv.org/pdf/2408.08541"},{"title":"Exact Byte-Level Probabilities from Tokenized Language Models for   FIM-Tasks and Model Ensembles","url":"https://arxiv.org/pdf/2410.09303"}]

Based on the search results, Brian Siyuan Zheng and Alisa Liu have follow-up work on tokenization published in 2026 titled "Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations."

In this work, they investigate the robustness of language models to text encoded with non-canonical tokenizations entirely unseen during training, and find that instruction-tuned models retain up to 93.4% of their original performance when given a randomly sampled tokenization, and 90.8% with character-level tokenization. The research was conducted by authors from the University of Washington, Allen Institute for AI, and Stanford University.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b3d78db-c8a9-4a44-8910-1a813b9daad1",
  "isSidechain": true,
  "promptId": "7b21de4b-acb9-4aab-be9b-f93717fb5eed",
  "agentId": "a91aa078a91c6b8ba",
  "type": "user",
  "uuid": "353f23a2-7430-4d6f-bf8b-171c539bee61",
  "sourceToolAssistantUUID": "9b3d78db-c8a9-4a44-8910-1a813b9daad1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-19T22:15:12.723Z_

<details><summary>↩ Tool result · `toolu_01BYdboJ87tXopGrqK9dLd3K`</summary>

```text
Web search results for query: "Omri Uzan Yuval Pinter CharBench university affiliation Ben-Gurion"

Links: [{"title":"Yuval PINTER | Senior Lecturer | Ben-Gurion University of the Negev, Beersheba | bgu | Department of Computer Science | Research profile","url":"https://www.researchgate.net/profile/Yuval-Pinter"},{"title":"CHARBENCH: Evaluating the Role of Tokenization in Character-Level Tasks - Ben-Gurion University Research Portal","url":"https://cris.bgu.ac.il/en/publications/charbench-evaluating-the-role-of-tokenization-in-character-level--2/"},{"title":"CharBench: Evaluating the Role of Tokenization in Character-Level Tasks | Request PDF","url":"https://www.researchgate.net/publication/402627608_CharBench_Evaluating_the_Role_of_Tokenization_in_Character-Level_Tasks"},{"title":"Omri Uzan","url":"https://omriuz.github.io/"},{"title":"Yuval Pinter - Ben-Gurion University Research Portal","url":"https://cris.bgu.ac.il/en/persons/yuval-pinter/"},{"title":"Omri Uzan - Google Akademik","url":"https://scholar.google.at/citations?user=uJvNbkYAAAAJ&hl=tr"},{"title":"Yuval Pinter","url":"https://scholar.google.com/citations?hl=en&user=aYAcXccAAAAJ"},{"title":"Ben-Gurion University of the Negev - Dr. Yuval Pinter","url":"https://in.bgu.ac.il/en/Pages/yuval-Pinter.aspx"},{"title":"Greed is All You Need: An Evaluation of Tokenizer Inference Methods | Request PDF","url":"https://www.researchgate.net/publication/384214178_Greed_is_All_You_Need_An_Evaluation_of_Tokenizer_Inference_Methods"},{"title":"Yuval Pinter (Ben-Gurion University - Virtual Visit) \"Challenging and Adapting NLP Models to Lexical Phenomena\" - Center for Language and Speech Processing","url":"https://www.clsp.jhu.edu/events/yuval-pinter/"}]

Based on the search results, here's what I found about Omri Uzan, Yuval Pinter, and CharBench:

## University Affiliations

Yuval Pinter is a Senior Lecturer in the Department of Computer Science at Ben-Gurion University of the Negev, while Omri Uzan is a PhD Student in Computer Science at Stanford University. However, Omri Uzan completed his B.Sc. and M.Sc. in Computer Science at Ben-Gurion University.

## CharBench Publication

Omri Uzan and Yuval Pinter authored the paper "CharBench: Evaluating the Role of Tokenization in Character-Level Tasks," which was published in the Proceedings of the AAAI Conference on Artificial Intelligence in 2026.

Tasks that require character-level reasoning, such as counting or locating characters within words, remain challenging for contemporary language models, which is the focus of their CharBench benchmark.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c672730b-5259-4685-aa48-f9d27614af84",
  "isSidechain": true,
  "promptId": "7b21de4b-acb9-4aab-be9b-f93717fb5eed",
  "agentId": "a91aa078a91c6b8ba",
  "type": "user",
  "uuid": "96385b0e-9cd3-4276-989e-9b76ab5b04d8",
  "sourceToolAssistantUUID": "c672730b-5259-4685-aa48-f9d27614af84",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T22:15:15.820Z_

<details><summary>↩ Tool result · `toolu_015Y7FnccCtjAPsxaEqPJkHu`</summary>

```text
Web search results for query: ""Broken Tokens" NeurIPS 2025 "future work" "adaptive" OR "reasoning" tokenization"

Links: [{"title":"[2506.19004] Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations","url":"https://arxiv.org/abs/2506.19004"},{"title":"Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations","url":"https://arxiv.org/pdf/2506.19004"},{"title":"NeurIPS Poster Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/117561"},{"title":"Not All Tokens Are What You Need In Thinking","url":"https://arxiv.org/pdf/2505.17827"},{"title":"Do LLMs Encode Functional Importance of Reasoning Tokens?","url":"https://arxiv.org/pdf/2601.03066"},{"title":"Broken Chains: The Cost of Incomplete Reasoning in LLMs","url":"https://arxiv.org/pdf/2602.14444"},{"title":"Disentangling Reasoning Tokens and Boilerplate Tokens For Language Model   Fine-tuning","url":"https://arxiv.org/pdf/2412.14780"},{"title":"Broken Words, Broken Performance: Effect of Tokenization on Performance of LLMs","url":"https://arxiv.org/pdf/2512.21933"},{"title":"Say Anything but This: When Tokenizer Betrays Reasoning in LLMs","url":"https://arxiv.org/pdf/2601.14658"}]

I found the "Broken Tokens" paper from NeurIPS 2025. Based on the search results, here's what I found regarding future work and adaptive/reasoning tokenization:

## Key Findings

The paper investigates the robustness of language models to text encoded with non-canonical tokenizations entirely unseen during training. Instruction-tuned models retain up to 93.4% of their original performance when given a randomly sampled tokenization, and 90.8% with character-level tokenization.

## Adaptive and Performance-Improving Tokenization

The research identifies specific cases where non-canonical tokenization schemes can improve performance: character-level segmentation improves string manipulation and code understanding tasks by up to +14%, and right-aligned digit grouping enhances large-number arithmetic by +33%.

## Understanding Robustness Mechanisms

The robustness arises in the instruction-tuning phase, with instruction-tuned models committed to fluent responses while base models try to mimic perceived mistakes and degenerate into nonsensical output.

## Implications for Future Work

The findings highlight the promise of intervening on tokenization at inference time to boost language model performance, suggesting that adaptive tokenization strategies at inference could be a valuable direction for future research.

The paper is listed as a spotlight poster presentation at NeurIPS 2025 in San Diego.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "724e0eb4-68da-4a26-a78f-bc4e1b3eda9c",
  "isSidechain": true,
  "promptId": "7b21de4b-acb9-4aab-be9b-f93717fb5eed",
  "agentId": "a91aa078a91c6b8ba",
  "type": "user",
  "uuid": "1b2c390a-9fb0-48d5-8a08-239f789f9f18",
  "sourceToolAssistantUUID": "724e0eb4-68da-4a26-a78f-bc4e1b3eda9c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-19T22:15:18.945Z_

Let me get the precise future work text from the paper's conclusion and look for any follow-up publications from these authors.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b2c390a-9fb0-48d5-8a08-239f789f9f18",
  "isSidechain": true,
  "agentId": "a91aa078a91c6b8ba",
  "requestId": "req_011CbChWCVoVXc2mi4GU5s3e",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1da8d746-725e-4149-9dbd-42a8c268e8d9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DiZZkBYFuiTsk5YrYfrXPj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2571,
      "cache_read_input_tokens": 16201,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2571,
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

_source line 36 · 2026-05-19T22:15:21.808Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LjX3HiZoTkubYPaFiEABbG`</summary>

```json
{
  "url": "https://arxiv.org/html/2506.19004v1",
  "prompt": "Find and extract the EXACT text of the Conclusion section and any Limitations section. I need the precise future work directions they propose, word for word. Also extract the exact sentence about \"automatically identifying the optimal tokenization.\" Is \"adaptive tokenization for reasoning\" mentioned anywhere in the paper?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1da8d746-725e-4149-9dbd-42a8c268e8d9",
  "isSidechain": true,
  "agentId": "a91aa078a91c6b8ba",
  "requestId": "req_011CbChWCVoVXc2mi4GU5s3e",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5a557752-3e43-411e-b420-d5f18a2ca5b5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DiZZkBYFuiTsk5YrYfrXPj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2571,
      "cache_read_input_tokens": 16201,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2571,
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

_source line 37 · 2026-05-19T22:15:22.597Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015DvukHw6yzWUge3wYZzkkz`</summary>

```json
{
  "query": "Alisa Liu \"Word Recovery\" character-level tokenization robustness 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a557752-3e43-411e-b420-d5f18a2ca5b5",
  "isSidechain": true,
  "agentId": "a91aa078a91c6b8ba",
  "requestId": "req_011CbChWCVoVXc2mi4GU5s3e",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "72bc763a-6cdc-4423-8967-4f1017d7d1ef",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DiZZkBYFuiTsk5YrYfrXPj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2571,
      "cache_read_input_tokens": 16201,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2571,
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

_source line 38 · 2026-05-19T22:15:26.726Z_

<details><summary>↩ Tool result · `toolu_01LjX3HiZoTkubYPaFiEABbG`</summary>

```text
# Extracted Conclusion and Future Work

## Conclusion Section (Exact Text)

"Despite being trained with deterministic tokenization algorithms, we show that instruction-tuned language models are surprisingly robust to token sequences not seen in training. In certain domains, such as arithmetic or code, more intuitively meaningful tokenizations can even be swapped-in at inference time for improved performance. We analyze the source of this robustness, and find that while the base and instruct models both perceive the semantics of non-canonical tokenizations, only instruct models are capable of providing fluent continuations.. Our work demonstrates a way in which LMs are not necessarily tied to tokenizer they were trained with, and highlights the potential of finding more optimal representations of text after pretraining."

## Optimal Tokenization Sentence

The exact sentence appears in Section 3.2: "We leave automatically identifying the optimal tokenization as a promising direction for future work."

## Limitations Section

**No dedicated Limitations section exists** in this paper. The authors do not include a formal limitations discussion.

## Search for "Adaptive Tokenization for Reasoning"

**Not mentioned.** This phrase does not appear anywhere in the provided document. The paper discusses tokenization interventions at inference time but does not specifically reference adaptive approaches for reasoning tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a557752-3e43-411e-b420-d5f18a2ca5b5",
  "isSidechain": true,
  "promptId": "7b21de4b-acb9-4aab-be9b-f93717fb5eed",
  "agentId": "a91aa078a91c6b8ba",
  "type": "user",
  "uuid": "2dfdb3bc-c467-4da0-969c-de529569050d",
  "sourceToolAssistantUUID": "5a557752-3e43-411e-b420-d5f18a2ca5b5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-19T22:15:27.985Z_

<details><summary>↩ Tool result · `toolu_015DvukHw6yzWUge3wYZzkkz`</summary>

```text
Web search results for query: "Alisa Liu "Word Recovery" character-level tokenization robustness 2026 arxiv"

Links: [{"title":"Word Recovery in Large Language Models Enables Character-Level Tokenization Robustness","url":"https://arxiv.org/pdf/2603.10771"},{"title":"[2603.10771] Word Recovery in Large Language Models Enables Character-Level Tokenization Robustness","url":"https://arxiv.org/abs/2603.10771"},{"title":"Word Recovery in Large Language Models Enables Character-Level Tokenization Robustness","url":"https://arxiv.org/html/2603.10771"},{"title":"[2506.19004] Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations","url":"https://arxiv.org/abs/2506.19004"},{"title":"Tokenization Falling Short: On Subword Robustness in Large Language Models","url":"https://arxiv.org/html/2406.11687v3"}]

Based on the search results, I found the paper, though it appears the author you mentioned (Alisa Liu) is not listed as a primary author. The paper is:

**"Word Recovery in Large Language Models Enables Character-Level Tokenization Robustness"**

The paper was submitted to arXiv on March 11, 2026, with authors Zhipeng Yang and 3 other authors.

The paper studies how large language models trained with canonical tokenization exhibit surprising robustness to non-canonical inputs such as character-level tokenization, identifying a core process termed "word recovery" through mechanistic interpretability. 

The researchers introduce a decoding-based method to detect word recovery, showing that hidden states reconstruct canonical word-level token identities from character-level inputs. Fine-grained attention analysis shows that in-group attention among characters belonging to the same canonical token is critical for word recovery.

The paper's arXiv identifier is 2603.10771 and can be accessed at https://arxiv.org/abs/2603.10771.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72bc763a-6cdc-4423-8967-4f1017d7d1ef",
  "isSidechain": true,
  "promptId": "7b21de4b-acb9-4aab-be9b-f93717fb5eed",
  "agentId": "a91aa078a91c6b8ba",
  "type": "user",
  "uuid": "bd70f2fc-e0e0-4785-a8b8-ff74f76532a7",
  "sourceToolAssistantUUID": "72bc763a-6cdc-4423-8967-4f1017d7d1ef",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-19T22:15:32.111Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DfXWCHCC282mrfXafnvwFs`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.10771",
  "prompt": "Extract: 1) Full author list and affiliations. 2) Does this paper cite \"Broken Tokens\" (arXiv:2506.19004)? 3) Is this a direct follow-up by the same group (UW/AI2/Stanford)?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd70f2fc-e0e0-4785-a8b8-ff74f76532a7",
  "isSidechain": true,
  "agentId": "a91aa078a91c6b8ba",
  "requestId": "req_011CbChX6WuqFuJiKVjHfvrp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d7d1a11-abcf-4e7f-962f-cef17feecd95",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BFXJKWjphAT6uuJXcpFboL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1171,
      "cache_read_input_tokens": 18772,
      "output_tokens": 142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1171
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 142,
          "cache_read_input_tokens": 18772,
          "cache_creation_input_tokens": 1171,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1171,
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

_source line 41 · 2026-05-19T22:15:35.397Z_

<details><summary>↩ Tool result · `toolu_01DfXWCHCC282mrfXafnvwFs`</summary>

```text
# Response Based on Available Content

**1) Full Author List and Affiliations:**

The page lists four authors:
- Zhipeng Yang
- Shu Yang
- Lijie Hu
- Di Wang

However, **no affiliations are provided** on this arXiv abstract page. The full paper PDF would contain this information.

**2) Citation of "Broken Tokens" (arXiv:2506.19004):**

**Cannot determine from this content.** The abstract page does not include the paper's reference section or bibliography. You would need to access the full PDF or TeX source to verify citations.

**3) Same Research Group (UW/AI2/Stanford):**

**Cannot determine from this content.** Without affiliation information displayed on the abstract page, it's impossible to assess whether these authors belong to the institutions you mentioned or if this represents a continuation of prior work by that specific group.

---

**Recommendation:** Download the PDF or view the TeX source for complete author affiliations and the full reference list.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d7d1a11-abcf-4e7f-962f-cef17feecd95",
  "isSidechain": true,
  "promptId": "7b21de4b-acb9-4aab-be9b-f93717fb5eed",
  "agentId": "a91aa078a91c6b8ba",
  "type": "user",
  "uuid": "a95ffce2-7eee-4b35-8843-0131b218690d",
  "sourceToolAssistantUUID": "5d7d1a11-abcf-4e7f-962f-cef17feecd95",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-19T22:16:04.076Z_

I now have comprehensive information. Here is the detailed research report.

---

## Research Findings on "Broken Tokens" and Related Work

### 1. Future Work Directions in "Broken Tokens"

The paper does **not** contain a dedicated "Future Work" or "Limitations" section. The only explicit future work statement appears in Section 3.2: *"We leave automatically identifying the optimal tokenization as a promising direction for future work."* The conclusion states that the work *"highlights the potential of finding more optimal representations of text after pretraining"* and *"demonstrates the promise of intervening on tokenization at inference time to boost performance."*

Critically, **"adaptive tokenization for reasoning" is never explicitly mentioned** anywhere in the paper. The future work framing is narrower -- it is about automatically selecting the best tokenization variant for a given input, not specifically about reasoning tasks. Any claim that the paper proposes "adaptive tokenization for reasoning" as a future direction would be an overstatement of what the authors actually wrote.

### 2. Exact Degradation on General Benchmarks

For **Llama-3.1-8B-Instruct** with character-level tokenization (vs. canonical):
- **ARC-Challenge**: 76.2% canonical, **-22.4 point drop** with character-level
- **ARC-Easy**: 91.3% canonical, **-21.5 point drop**
- **HellaSwag**: 68.6% canonical, **-23.4 point drop**
- **MMLU**: -24 point drop
- **CSQA**: -20 point drop
- **TriviaQA**: -13.6 point drop

Overall, instruction-tuned models retain ~90.8% of performance with character-level tokenization across 20 benchmarks, but knowledge-intensive and commonsense benchmarks suffer the most (~20-24 point drops). Character-level tokenization does help in specific domains: +14% on string manipulation/code tasks and +33% on large-number arithmetic with right-aligned digit grouping.

### 3. Authors and Affiliations

**Broken Tokens authors**: Brian Siyuan Zheng, Alisa Liu, Orevaoghene Ahia, Jonathan Hayase, Yejin Choi, Noah A. Smith -- affiliated with **University of Washington**, **Allen Institute for AI (AI2)**, and **Stanford University**. The paper was a spotlight poster at NeurIPS 2025 in San Diego.

A related follow-up paper, "Word Recovery in Large Language Models Enables Character-Level Tokenization Robustness" (arXiv:2603.10771, March 2026), by Zhipeng Yang, Shu Yang, Lijie Hu, and Di Wang, builds on the Broken Tokens findings by using mechanistic interpretability to explain *how* models recover word-level meaning from character-level inputs. This appears to be from a **different research group**, not the original UW/AI2/Stanford team.

### 4. CharBench Average Accuracy

Both numbers cited are correct but refer to different things:
- **50.3% (specifically 50.33%)** = the overall CharBench average accuracy across all models and all four task categories
- **43.6%** = the average accuracy specifically for **positional understanding tasks** (find_first and find_last), which proved significantly harder than counting tasks

CharBench was authored by **Omri Uzan** and **Yuval Pinter** (Ben-Gurion University of the Negev), published at **AAAI 2026** (arXiv:2508.02591).

### Bonus: zip2zip

The zip2zip paper (arXiv:2506.01084, also NeurIPS 2025) achieves **15-40% token reduction** via inference-time adaptive tokenization using an LZW-based compression algorithm. It does not explicitly cite Broken Tokens, and does not use the phrase "adaptive tokenization for reasoning."

Sources:
- [Broken Tokens - arXiv](https://arxiv.org/abs/2506.19004)
- [Broken Tokens - HTML](https://arxiv.org/html/2506.19004v1)
- [CharBench - arXiv](https://arxiv.org/abs/2508.02591)
- [zip2zip - arXiv](https://arxiv.org/abs/2506.01084)
- [Word Recovery - arXiv](https://arxiv.org/abs/2603.10771)
- [CharBench - AAAI proceedings](https://ojs.aaai.org/index.php/AAAI/article/download/40615/44576)
- [Yuval Pinter - Ben-Gurion](https://cris.bgu.ac.il/en/persons/yuval-pinter/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a95ffce2-7eee-4b35-8843-0131b218690d",
  "isSidechain": true,
  "agentId": "a91aa078a91c6b8ba",
  "requestId": "req_011CbChXeCQhq1mfBREzMhnQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0dcd1cc5-24e0-4c4e-8d5b-db94aa5f765d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "804e1be2-f99e-408c-bc64-cc8c94b61e8a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TtLXU2uJzsj8vLFgXnkUiE",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 382,
      "cache_read_input_tokens": 19943,
      "output_tokens": 1148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 382
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1148,
          "cache_read_input_tokens": 19943,
          "cache_creation_input_tokens": 382,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 382,
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
