# Research conversation: You are helping me verify ML paper references. Use WebSearch to check whether these papers actually exist, and verify th

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ab97e4394c082e28d.jsonl`
- **Structured JSON:** [`98f351b0451377874c6c.json`](../../sessions/98/98f351b0451377874c6c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

44 recorded events

### User

_source line 1 · 2026-05-19T16:32:06.222Z_

You are helping me verify ML paper references. Use WebSearch to check whether these papers actually exist, and verify their venues, authors, and key claims. For each paper, do a targeted web search and report what you find.

Papers to verify:
1. "Broken Tokens" - claimed NeurIPS 2025 Spotlight by Zheng, Liu, Ahia, Hayase, Choi, Smith. Claims: instruction-tuned LLMs retain ~93% perf under non-canonical tokenizations, +33.7pp arithmetic with digit grouping on Llama-3.1-8B-Instruct, random tokenization degrades Qwen-2.5-7B-Instruct GSM8k by -6.1pp
2. "Probabilistic Tokenization" - claimed NAACL 2025 Findings by Sathe, Aggarwal, Sitaram. Claims: +17.11% average across 7 base models, 4 benchmarks, using 64 random BPE tokenizations
3. "Where is the Signal in Tokenization Space?" - claimed EMNLP 2024 by Geh et al.
4. "NumeroLogic" - claimed EMNLP 2024 by Schwartz, Choshen, Shtok, Doveh, Karlinsky, Arbelle
5. "SepSeq" - claimed arXiv:2604.07737 by Sun et al., April 2026. Claims: 35.6% relative improvement across 9 LLMs
6. "The Sequential Edge" - claimed arXiv:2511.02309 by Sharma and Chopra, Nov 2025
7. "CISC" - claimed ACL 2025 Findings by Taubenfeld et al.
8. "VecCISC" - claimed arXiv:2605.08070 by Petullo et al., May 2026
9. "Dipper" - claimed EMNLP 2025
10. "EDIS" - claimed arXiv:2602.01288

For each, search with queries like: site:arxiv.org "[paper title]", "[author names] [topic] [year]", etc. Report findings concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e4dedc50-3a35-4b66-994a-d3a71a42b739",
  "agentId": "ab97e4394c082e28d",
  "type": "user",
  "uuid": "61ab97ff-42da-4508-8454-9dba4f087476",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T16:32:06.225Z_

```json
{
  "parentUuid": "61ab97ff-42da-4508-8454-9dba4f087476",
  "isSidechain": true,
  "agentId": "ab97e4394c082e28d",
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
  "uuid": "ceb599ad-c937-4001-90e4-3f9a0c28d97f",
  "timestamp": "2026-05-19T16:32:06.225Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-19T16:32:06.226Z_

```json
{
  "parentUuid": "ceb599ad-c937-4001-90e4-3f9a0c28d97f",
  "isSidechain": true,
  "agentId": "ab97e4394c082e28d",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "aa80a3aa-fc27-4833-b61c-391f0878dfe5",
  "timestamp": "2026-05-19T16:32:06.226Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 4 · 2026-05-19T16:32:08.338Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011mxL8GBb4bmo2S2WS3o8bu`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa80a3aa-fc27-4833-b61c-391f0878dfe5",
  "isSidechain": true,
  "agentId": "ab97e4394c082e28d",
  "requestId": "req_011CbCFLT7po4AbtDbbumKig",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f4b410c8-32cf-4b27-90f4-03316f8f7217",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017mwdEezFzyStKCmPAak5Cw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9540,
      "cache_read_input_tokens": 0,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9540
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 76,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 9540,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9540,
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

_source line 5 · 2026-05-19T16:32:08.343Z_

<details><summary>↩ Tool result · `toolu_011mxL8GBb4bmo2S2WS3o8bu`</summary>

````text
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
  "parentUuid": "f4b410c8-32cf-4b27-90f4-03316f8f7217",
  "isSidechain": true,
  "promptId": "e4dedc50-3a35-4b66-994a-d3a71a42b739",
  "agentId": "ab97e4394c082e28d",
  "type": "user",
  "uuid": "d9ad3c84-d9fe-4886-9b04-6eaacc8e4fad",
  "sourceToolAssistantUUID": "f4b410c8-32cf-4b27-90f4-03316f8f7217",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-19T16:32:10.669Z_

I'll search for all 10 papers in parallel to verify their existence and details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9ad3c84-d9fe-4886-9b04-6eaacc8e4fad",
  "isSidechain": true,
  "agentId": "ab97e4394c082e28d",
  "requestId": "req_011CbCFLcQRfiAgsqzHPeYuu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a3384a8-c0be-486a-bd80-3d8225bdaad5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KhmdQpuSwULQBeGJywuNid",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 605,
      "cache_read_input_tokens": 9540,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 605,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T16:32:11.628Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TbbDauB1W2FqFvaN4BGvvr`</summary>

```json
{
  "query": "Broken Tokens NeurIPS 2025 Zheng Liu Ahia Hayase Choi Smith tokenization LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a3384a8-c0be-486a-bd80-3d8225bdaad5",
  "isSidechain": true,
  "agentId": "ab97e4394c082e28d",
  "requestId": "req_011CbCFLcQRfiAgsqzHPeYuu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8fa4be43-631a-4619-8699-7db03e758d80",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KhmdQpuSwULQBeGJywuNid",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 605,
      "cache_read_input_tokens": 9540,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 605,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-19T16:32:12.007Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WqTBztfqXgFuJCCbF7T3Bw`</summary>

```json
{
  "query": "Probabilistic Tokenization NAACL 2025 Sathe Aggarwal Sitaram BPE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fa4be43-631a-4619-8699-7db03e758d80",
  "isSidechain": true,
  "agentId": "ab97e4394c082e28d",
  "requestId": "req_011CbCFLcQRfiAgsqzHPeYuu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e590e3e-6fe4-4908-8e5a-4105a22419e9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KhmdQpuSwULQBeGJywuNid",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 605,
      "cache_read_input_tokens": 9540,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 605,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T16:32:12.384Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XULV4VKfgb23kepbSbHJf6`</summary>

```json
{
  "query": "\"Where is the Signal in Tokenization Space\" EMNLP 2024 Geh"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e590e3e-6fe4-4908-8e5a-4105a22419e9",
  "isSidechain": true,
  "agentId": "ab97e4394c082e28d",
  "requestId": "req_011CbCFLcQRfiAgsqzHPeYuu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5ca67936-006d-4f20-8d64-2e259800219e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KhmdQpuSwULQBeGJywuNid",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 605,
      "cache_read_input_tokens": 9540,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 605,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-19T16:32:12.773Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JwqMo64hLFiHcmFch5Lm1r`</summary>

```json
{
  "query": "NumeroLogic EMNLP 2024 Schwartz Choshen Shtok Doveh Karlinsky Arbelle"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ca67936-006d-4f20-8d64-2e259800219e",
  "isSidechain": true,
  "agentId": "ab97e4394c082e28d",
  "requestId": "req_011CbCFLcQRfiAgsqzHPeYuu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "50688ded-4fae-48e3-b701-866521f2c31c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KhmdQpuSwULQBeGJywuNid",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 605,
      "cache_read_input_tokens": 9540,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 605,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T16:32:13.290Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FJi2Nr3LuTAvGkv9MmvJSB`</summary>

```json
{
  "query": "SepSeq arXiv 2604.07737 Sun tokenization LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50688ded-4fae-48e3-b701-866521f2c31c",
  "isSidechain": true,
  "agentId": "ab97e4394c082e28d",
  "requestId": "req_011CbCFLcQRfiAgsqzHPeYuu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e7ae1a0d-febb-46ae-a3da-cca90d3b8e89",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KhmdQpuSwULQBeGJywuNid",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 605,
      "cache_read_input_tokens": 9540,
      "output_tokens": 343,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 605
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 343,
          "cache_read_input_tokens": 9540,
          "cache_creation_input_tokens": 605,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 605,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T16:32:18.180Z_

<details><summary>↩ Tool result · `toolu_01WqTBztfqXgFuJCCbF7T3Bw`</summary>

```text
Web search results for query: "Probabilistic Tokenization NAACL 2025 Sathe Aggarwal Sitaram BPE"

Links: [{"title":"Improving Consistency in LLM Inference using Probabilistic ...","url":"https://aclanthology.org/2025.findings-naacl.268.pdf"},{"title":"Improving Consistency in LLM Inference using Probabilistic Tokenization - ACL Anthology","url":"https://aclanthology.org/2025.findings-naacl.268/"},{"title":"Improving Self Consistency in LLMs through Probabilistic Tokenization","url":"https://arxiv.org/html/2407.03678v1"},{"title":"Improving Self Consistency in LLMs through Probabilistic Tokenization","url":"https://www.researchgate.net/publication/382066000_Improving_Self_Consistency_in_LLMs_through_Probabilistic_Tokenization"},{"title":"Improving Self Consistency in LLMs through Probabilistic Tokenization","url":"https://arxiv.org/pdf/2407.03678"},{"title":"LiteToken: Removing Intermediate Merge Residues From BPE Tokenizers","url":"https://arxiv.org/pdf/2602.04706"}]

Based on the search results, I found the paper you're looking for:

"Improving Consistency in LLM Inference using Probabilistic Tokenization" by Ashutosh Sathe, Divyanshu Aggarwal, and Sunayana Sitaram was published in the Findings of the Association for Computational Linguistics: NAACL 2025, pages 4766–4778, in Albuquerque, New Mexico.

The paper introduces probabilistic tokenizations, an approach that involves employing multiple tokenizations of the same input string during the training phase of a language model. The authors propose a novel method to leverage the multiple tokenization capabilities of modern LLM tokenizers, aiming to enhance the self-consistency of LLMs in reasoning tasks.

The work focuses on BPE tokenizers (Byte-Pair Encoding with byte-fallback) that maintain the ability to generate multiple tokenizations for a given input string. The researchers conducted extensive experimentation on 5 LLM families and 4 reasoning benchmarks to study probabilistic tokenization and explain the self-consistency improvements it brings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e590e3e-6fe4-4908-8e5a-4105a22419e9",
  "isSidechain": true,
  "promptId": "e4dedc50-3a35-4b66-994a-d3a71a42b739",
  "agentId": "ab97e4394c082e28d",
  "type": "user",
  "uuid": "f3c16a19-94a5-48ff-b7cb-65962b277872",
  "sourceToolAssistantUUID": "0e590e3e-6fe4-4908-8e5a-4105a22419e9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T16:32:19.628Z_

<details><summary>↩ Tool result · `toolu_01TbbDauB1W2FqFvaN4BGvvr`</summary>

```text
Web search results for query: "Broken Tokens NeurIPS 2025 Zheng Liu Ahia Hayase Choi Smith tokenization LLM"

Links: [{"title":"NeurIPS Poster Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations","url":"https://neurips.cc/virtual/2025/poster/117561"},{"title":"[2506.19004] Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations","url":"https://arxiv.org/abs/2506.19004"},{"title":"Broken Tokens? Your Language Model can Secretly Handle No n - Ca noni cal Tokenizations","url":"https://arxiv.org/html/2506.19004v1"},{"title":"arXiv:2506.19004v1 [cs.CL] 23 Jun 2025 Broken Tokens? Your Language Model can","url":"https://arxiv.org/pdf/2506.19004"},{"title":"Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations","url":"https://www.researchgate.net/publication/392980296_Broken_Tokens_Your_Language_Model_can_Secretly_Handle_Non-Canonical_Tokenizations"},{"title":"Broken Tokens? Your Language Model can","url":"https://openreview.net/pdf?id=zpheKOg5f0"},{"title":"Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations | OpenReview","url":"https://openreview.net/forum?id=WrYWolqKh3"},{"title":"dblp: Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations.","url":"https://dblp.org/rec/journals/corr/abs-2506-19004.html"},{"title":"Broken Words, Broken Performance: Effect of Tokenization on Performance of LLMs","url":"https://arxiv.org/pdf/2512.21933"},{"title":"Broken Tokens? Your Language Model can Secretly Handle No n","url":"https://openreview.net/pdf/b001873ec0dc69deca0d93042e91329795dbfb9f.pdf"}]

Based on the search results, I found comprehensive information about this NeurIPS 2025 paper:

## "Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations"

This is a spotlight poster presentation at NeurIPS 2025 by Brian Zheng, Alisa Liu, Orevaoghene Ahia, Jonathan Hayase, Yejin Choi, and Noah Smith.

**Research Focus:**
The paper investigates how modern tokenizers use deterministic algorithms to map text into a single "canonical" token sequence, and examines the robustness of language models to text encoded with non-canonical tokenizations entirely unseen during training.

**Key Findings:**
When evaluated across 20 benchmarks, instruction-tuned models retain up to 93.4% of their original performance when given a randomly sampled tokenization, and 90.8% with character-level tokenization. Overall stronger models tend to be more robust, and robustness diminishes as the tokenization departs farther from the canonical form.

**Practical Implications:**
The researchers identified settings where non-canonical tokenization schemes can improve performance, finding that character-level segmentation improves string manipulation and code understanding tasks by up to 14%.

The paper is available on arXiv (2506.19004) and OpenReview, and was presented at NeurIPS 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8fa4be43-631a-4619-8699-7db03e758d80",
  "isSidechain": true,
  "promptId": "e4dedc50-3a35-4b66-994a-d3a71a42b739",
  "agentId": "ab97e4394c082e28d",
  "type": "user",
  "uuid": "30e908b0-c244-4213-bb6a-1bda2c8e184d",
  "sourceToolAssistantUUID": "8fa4be43-631a-4619-8699-7db03e758d80",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T16:32:20.018Z_

<details><summary>↩ Tool result · `toolu_01JwqMo64hLFiHcmFch5Lm1r`</summary>

```text
Web search results for query: "NumeroLogic EMNLP 2024 Schwartz Choshen Shtok Doveh Karlinsky Arbelle"

Links: [{"title":"NumeroLogic: Number Encoding for Enhanced LLMs’ Numerical Reasoning - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.12/"},{"title":"NumeroLogic: Number Encoding for Enhanced LLMs' Numerical Reasoning - Ben-Gurion University Research Portal","url":"https://cris.bgu.ac.il/en/publications/numerologic-number-encoding-for-enhanced-llms-numerical-reasoning/"},{"title":"Main Conference - EMNLP 2024","url":"https://2024.emnlp.org/program/accepted_main_conference/"},{"title":"EMNLP 2024: Miami, FL, USA","url":"https://dblp.org/db/conf/emnlp/emnlp2024.html"},{"title":"Aclanthology","url":"https://aclanthology.org/2024.emnlp-main.12.bib"},{"title":"[2404.00459] NumeroLogic: Number Encoding for Enhanced LLMs' Numerical Reasoning","url":"https://arxiv.org/abs/2404.00459"},{"title":"[PDF] NumeroLogic: Number Encoding for Enhanced LLMs’ Numerical Reasoning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/NumeroLogic:-Number-Encoding-for-Enhanced-LLMs%E2%80%99-Schwartz-Choshen/b9750286ba2198a406137e0dfee2d545f0d78c13"},{"title":"[Quick Review] NumeroLogic: Number Encoding for Enhanced LLMs’ Numerical Reasoning","url":"https://liner.com/review/numerologic-number-encoding-for-enhanced-llms-numerical-reasoning"},{"title":"Number Encoding for Enhanced LLMs' Numerical Reasoning","url":"https://aclanthology.org/2024.emnlp-main.12.pdf"},{"title":"NumeroLogic: Number Encoding for Enhanced LLMs’ Numerical Reasoning | Request PDF","url":"https://www.researchgate.net/publication/386193131_NumeroLogic_Number_Encoding_for_Enhanced_LLMs'_Numerical_Reasoning"}]

I found the paper! Here are the search results for NumeroLogic:

NumeroLogic: Number Encoding for Enhanced LLMs' Numerical Reasoning was published in the Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP 2024) in Miami, Florida, USA, pages 206–212.

The authors are Eli Schwartz, Leshem Choshen, Joseph Shtok, Sivan Doveh, Leonid Karlinsky, and Assaf Arbelle.

**About the paper:**

Language models struggle with handling numerical data and performing arithmetic operations, which the authors hypothesize can be partially attributed to non-intuitive textual numbers representation. To address this issue, they propose a simple adjustment to how numbers are represented by including the count of digits before each number, for instance, instead of "42", using "2:42" as the new format.

The paper is available through the ACL Anthology at: https://aclanthology.org/2024.emnlp-main.12/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50688ded-4fae-48e3-b701-866521f2c31c",
  "isSidechain": true,
  "promptId": "e4dedc50-3a35-4b66-994a-d3a71a42b739",
  "agentId": "ab97e4394c082e28d",
  "type": "user",
  "uuid": "12ab971f-3ebd-4369-ac35-9f4c9a1e6760",
  "sourceToolAssistantUUID": "50688ded-4fae-48e3-b701-866521f2c31c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-19T16:32:20.370Z_

<details><summary>↩ Tool result · `toolu_01XULV4VKfgb23kepbSbHJf6`</summary>

```text
Web search results for query: ""Where is the Signal in Tokenization Space" EMNLP 2024 Geh"

Links: [{"title":"Where is the signal in tokenization space? - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.230/"},{"title":"Broken Tokens? Your Language Model can Secretly Handle No n - Ca noni cal Tokenizations","url":"https://arxiv.org/html/2506.19004v1"},{"title":"[2408.08541v1] Where is the signal in tokenization space?","url":"https://arxiv.org/abs/2408.08541v1"},{"title":"[2408.08541] Where is the signal in tokenization space?","url":"https://arxiv.org/abs/2408.08541"},{"title":"Where is the signal in tokenization space? - Paper Reading","url":"https://www.paperreading.club/page?id=246565"},{"title":"Where is the signal in tokenization space?","url":"https://www.researchgate.net/publication/386189670_Where_is_the_signal_in_tokenization_space"},{"title":"Where is the signal in tokenization space?","url":"https://starai.cs.ucla.edu/papers/GehEMNLP24.pdf"},{"title":"Renato Lui Geh on X: \"Where is the signal in LLM tokenization space? Does it only come from the canonical (default) tokenization? The answer is no! By looking at other ways to tokenize the same text, we get a consistent boost to LLM performance! https://t.co/bbUBlotNVj 1/5 https://t.co/qqJFq5P1WO\" / X","url":"https://x.com/renatogeh/status/1833506496786927672"},{"title":"Where is the signal in tokenization space?","url":"https://arxiv.org/pdf/2408.08541"}]

Based on the search results, here's information about the paper:

"Where is the signal in tokenization space?" is a paper by Renato Geh, Honghua Zhang, Kareem Ahmed, Benjie Wang, and Guy Van Den Broeck, published in the Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP), pages 3966–3979, Miami, Florida, USA.

The paper's main contribution is investigating tokenization in Large Language Models (LLMs). LLMs are typically shipped with tokenizers that deterministically encode text into so-called canonical token sequences, to which the LLMs assign probability values, with one common assumption being that the probability of a piece of text is the probability of its canonical token sequence. However, the tokenization of a string is not unique: for example, the Llama2 tokenizer encodes "Tokens" as [Tok,ens], but [Tok,en,s] also represents the same text.

The researchers' findings show that there exists a significant amount of signal hidden within tokenization space, and by simply aggregating the probabilities of non-canonical tokenizations, they achieve improvements across a range of LLM evaluation benchmarks for a variety of architectures, including transformers and state space models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ca67936-006d-4f20-8d64-2e259800219e",
  "isSidechain": true,
  "promptId": "e4dedc50-3a35-4b66-994a-d3a71a42b739",
  "agentId": "ab97e4394c082e28d",
  "type": "user",
  "uuid": "6a04e16a-d757-41a8-a5c1-2736b291e739",
  "sourceToolAssistantUUID": "5ca67936-006d-4f20-8d64-2e259800219e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T16:32:21.961Z_

<details><summary>↩ Tool result · `toolu_01FJi2Nr3LuTAvGkv9MmvJSB`</summary>

```text
Web search results for query: "SepSeq arXiv 2604.07737 Sun tokenization LLM 2026"

Links: [{"title":"[2604.07737v1] SepSeq: A Training-Free Framework for Long Numerical Sequence Processing in LLMs","url":"https://arxiv.org/abs/2604.07737v1"},{"title":"[2604.07737] SepSeq: A Training-Free Framework for Long Numerical Sequence Processing in LLMs","url":"https://arxiv.org/abs/2604.07737"},{"title":"SepSeq: A Training-Free Framework for Long Numerical Sequence Processing in LLMs","url":"https://arxiv.org/pdf/2604.07737"},{"title":"SUN: Shared Use of Next-token Prediction for Efficient Multi-LLM Disaggregated Serving","url":"https://arxiv.org/html/2603.02599v1"},{"title":"Tokenization Multiplicity Leads to Arbitrary Price Variation in LLM-as-a-service","url":"https://arxiv.org/pdf/2506.06446"}]

Based on the search results, I found detailed information about the paper you're looking for:

SepSeq (arXiv:2604.07737) is a paper by Jie Sun and colleagues submitted on April 9, 2026, titled "SepSeq: A Training-Free Framework for Long Numerical Sequence Processing in LLMs."

**Key findings:**

The paper addresses how transformer-based LLMs suffer from severe performance degradation when processing long numerical sequences, which it attributes to attention dispersion in the Softmax mechanism.

The proposed SepSeq framework is a training-free, plug-and-play approach that mitigates dispersion by strategically inserting separator tokens.

These separator tokens act as an attention sink, recalibrating attention to focus on local segments while preserving global context.

**Results:**

Extensive evaluations on 9 widely-adopted LLMs show that SepSeq yields an average relative accuracy improvement of 35.6% across diverse domains while reducing total inference token consumption by 16.4% on average.

The paper focuses specifically on improving LLM performance on long numerical sequence tasks through the use of separator tokens in tokenization, rather than requiring any model retraining.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7ae1a0d-febb-46ae-a3da-cca90d3b8e89",
  "isSidechain": true,
  "promptId": "e4dedc50-3a35-4b66-994a-d3a71a42b739",
  "agentId": "ab97e4394c082e28d",
  "type": "user",
  "uuid": "f76fa73c-e231-43c7-b197-bd1d54feb0e9",
  "sourceToolAssistantUUID": "e7ae1a0d-febb-46ae-a3da-cca90d3b8e89",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-19T16:32:25.060Z_

Now let me search for the remaining 5 papers:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f76fa73c-e231-43c7-b197-bd1d54feb0e9",
  "isSidechain": true,
  "agentId": "ab97e4394c082e28d",
  "requestId": "req_011CbCFMcQwguVr9UT9HhMh3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7d1410b-8a4e-426d-a633-578e6007da7e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LRXzXot6nTnoHQzp28UJ2C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4762,
      "cache_read_input_tokens": 9540,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4762,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-19T16:32:25.981Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SwFBKiwAy9RvncV4EfbrLS`</summary>

```json
{
  "query": "\"The Sequential Edge\" arXiv 2511.02309 Sharma Chopra 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7d1410b-8a4e-426d-a633-578e6007da7e",
  "isSidechain": true,
  "agentId": "ab97e4394c082e28d",
  "requestId": "req_011CbCFMcQwguVr9UT9HhMh3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "becd2fa9-9538-4934-9bba-dfa06e1d7f5e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LRXzXot6nTnoHQzp28UJ2C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4762,
      "cache_read_input_tokens": 9540,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4762,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T16:32:26.797Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RU5uTzkbqBGUiJPqeD1pnG`</summary>

```json
{
  "query": "CISC ACL 2025 Findings Taubenfeld tokenization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "becd2fa9-9538-4934-9bba-dfa06e1d7f5e",
  "isSidechain": true,
  "agentId": "ab97e4394c082e28d",
  "requestId": "req_011CbCFMcQwguVr9UT9HhMh3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a4999dc-d7c1-4e83-81c0-bf0b60c806f4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LRXzXot6nTnoHQzp28UJ2C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4762,
      "cache_read_input_tokens": 9540,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4762,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-19T16:32:27.637Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EGDC9PFLU3gEovTYRGjukA`</summary>

```json
{
  "query": "VecCISC arXiv 2605.08070 Petullo 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a4999dc-d7c1-4e83-81c0-bf0b60c806f4",
  "isSidechain": true,
  "agentId": "ab97e4394c082e28d",
  "requestId": "req_011CbCFMcQwguVr9UT9HhMh3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1b5cfdd-801f-42fc-aeac-24ad93795c90",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LRXzXot6nTnoHQzp28UJ2C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4762,
      "cache_read_input_tokens": 9540,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4762,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T16:32:28.024Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ChaQ8Xj1hrzjkQGFtUkUbg`</summary>

```json
{
  "query": "Dipper EMNLP 2025 paraphrase detection tokenization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1b5cfdd-801f-42fc-aeac-24ad93795c90",
  "isSidechain": true,
  "agentId": "ab97e4394c082e28d",
  "requestId": "req_011CbCFMcQwguVr9UT9HhMh3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "336e195f-1b39-41da-a9a7-1d43d3582bd9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LRXzXot6nTnoHQzp28UJ2C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4762,
      "cache_read_input_tokens": 9540,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4762,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-19T16:32:28.561Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CnJuthvtx1P2dutyBHRuuV`</summary>

```json
{
  "query": "EDIS arXiv 2602.01288 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "336e195f-1b39-41da-a9a7-1d43d3582bd9",
  "isSidechain": true,
  "agentId": "ab97e4394c082e28d",
  "requestId": "req_011CbCFMcQwguVr9UT9HhMh3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "219450f5-7cca-4fbb-ae68-3a67f9d14108",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LRXzXot6nTnoHQzp28UJ2C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4762,
      "cache_read_input_tokens": 9540,
      "output_tokens": 296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4762
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 296,
          "cache_read_input_tokens": 9540,
          "cache_creation_input_tokens": 4762,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4762,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-19T16:32:34.588Z_

<details><summary>↩ Tool result · `toolu_01EGDC9PFLU3gEovTYRGjukA`</summary>

```text
Web search results for query: "VecCISC arXiv 2605.08070 Petullo 2026"

Links: [{"title":"[2605.08070v1] VecCISC: Improving Confidence-Informed Self-Consistency with Reasoning Trace Clustering and Candidate Answer Selection","url":"https://arxiv.org/abs/2605.08070v1"},{"title":"VecCISC: Improving Confidence-Informed Self-Consistency with Reasoning Trace Clustering and Candidate Answer Selection","url":"https://arxiv.org/html/2605.08070v1"},{"title":"New mechanism for polarization singularity of vector vortex beams","url":"https://arxiv.org/pdf/2007.00198"},{"title":"Detection of 16 Gamma-Ray Pulsars Through Blind Frequency Searches Using   the Fermi LAT","url":"https://arxiv.org/pdf/1009.0748"},{"title":"Large Language Models for Detecting CONSORT Guideline Compliance in Published Randomized Clinical Trials: A Cross-Sectional Evaluation Study","url":"https://www.medrxiv.org/content/10.1101/2025.10.03.25337291.full.pdf"},{"title":"Crystal structure of a mammalian CMTM6 and its interaction model with PD-L1","url":"https://www.biorxiv.org/content/10.1101/2023.01.03.522599.full.pdf"},{"title":"pyPatlak: Open-Source Voxel-Wise Patlak Analysis of Dynamic PET Data","url":"https://www.medrxiv.org/content/10.1101/2025.09.16.25335861.full.pdf"}]

Based on the search results, I found information about the paper you're looking for:

VecCISC is a novel method introduced by James Petullo, Sonny George, Dylan Cashman, and Nianwen Xue from Brandeis University, submitted in May 2026.

The paper addresses Self-Consistency, a standard technique for scaling inference-time reasoning where multiple candidate answers are sampled from an LLM and the most common answer is selected. More recently, weighted majority voting approaches like Confidence-Informed Self Consistency (CISC) have been shown to be more accurate on a wide range of popular benchmarks.

VecCISC proposes a lightweight, adaptive framework that uses semantic similarity to filter reasoning traces that are semantically equivalent to others, degenerate, or hallucinated, thus decreasing the number of candidate answers that must be evaluated by the critic.

The paper evaluates VecCISC on five challenging datasets spanning mathematics, chemistry, biology, commonsense reasoning, and the humanities, and demonstrates that VecCISC reduces total token usage by 47%.

The paper is available at: https://arxiv.org/abs/2605.08070v1


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1b5cfdd-801f-42fc-aeac-24ad93795c90",
  "isSidechain": true,
  "promptId": "e4dedc50-3a35-4b66-994a-d3a71a42b739",
  "agentId": "ab97e4394c082e28d",
  "type": "user",
  "uuid": "522e49e9-c9b9-4409-badc-f38530811301",
  "sourceToolAssistantUUID": "a1b5cfdd-801f-42fc-aeac-24ad93795c90",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T16:32:35.440Z_

<details><summary>↩ Tool result · `toolu_01CnJuthvtx1P2dutyBHRuuV`</summary>

```text
Web search results for query: "EDIS arXiv 2602.01288 2026"

Links: [{"title":"[2602.01288] EDIS: Diagnosing LLM Reasoning via Entropy Dynamics","url":"https://arxiv.org/abs/2602.01288"},{"title":"EDIS: Diagnosing LLM Reasoning via Entropy Dynamics","url":"https://arxiv.org/html/2602.01288"},{"title":"The SARS-CoV-2 Omicron sub-variant BA.2.86 is attenuated in hamsters","url":"https://www.biorxiv.org/content/10.1101/2023.11.10.566576.full.pdf"},{"title":"Auditor Models to Suppress Poor AI Predictions Can Improve Human-AI Collaborative Performance","url":"https://www.medrxiv.org/content/10.1101/2025.06.24.25330212.full.pdf"},{"title":"Evolution and neutralization escape of the SARS-CoV-2 BA.2.86 subvariant","url":"https://www.medrxiv.org/content/10.1101/2023.09.08.23295250.full.pdf"},{"title":"Scalable screening for emergency department missed opportunities for diagnosis using sequential eTriggers and large language models","url":"https://www.medrxiv.org/content/10.1101/2025.10.06.25337201.full.pdf"}]

Based on the search results, I found information about arXiv paper 2602.01288:

The paper introduces EDIS (Entropy Dynamics Instability Score), a trajectory-level metric quantifying instability in entropy evolution. It addresses how entropy-based confidence signals are increasingly leveraged to improve reasoning in large language models, yet existing approaches treat confidence as a static quantity—typically aggregated over tokens.

The research shows that the temporal evolution of confidence during generation carries richer information than aggregate statistics alone, and analyzing token-level entropy trajectories identifies characteristic patterns distinguishing correct from incorrect reasoning, where erroneous solutions exhibit unstable dynamics including burst spikes and peak-valley spikes.

The paper was submitted on February 1, 2026, with a revised version on March 6, 2026, and is authored by Chenghua Zhu and eight other researchers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "219450f5-7cca-4fbb-ae68-3a67f9d14108",
  "isSidechain": true,
  "promptId": "e4dedc50-3a35-4b66-994a-d3a71a42b739",
  "agentId": "ab97e4394c082e28d",
  "type": "user",
  "uuid": "509a4aed-dc63-4cf2-80ee-c3f7392af9b1",
  "sourceToolAssistantUUID": "219450f5-7cca-4fbb-ae68-3a67f9d14108",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-19T16:32:37.133Z_

<details><summary>↩ Tool result · `toolu_01ChaQ8Xj1hrzjkQGFtUkUbg`</summary>

```text
Web search results for query: "Dipper EMNLP 2025 paraphrase detection tokenization"

Links: [{"title":"Paraphrasing evades detectors of AI-generated text, but ...","url":"https://arxiv.org/pdf/2303.13408"},{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"},{"title":"Dipper: Diversity in Prompts for Producing Large Language Model Ensembles in Reasoning Tasks - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1801/"},{"title":"GitHub - jpwahle/emnlp23-paraphrase-types: The official implementation of the EMNLP 2023 paper \"Paraphrase Types for Generation and Detection\"","url":"https://github.com/jpwahle/emnlp23-paraphrase-types"},{"title":"Dipper: Diversity in Prompts for Producing Large Language Model Ensembles in Reasoning Tasks | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/2025.emnlp-main.1801@ACL"},{"title":"EMNLP 2023 Paraphrase Types for Generation and Detection","url":"https://arxiv.org/html/2310.14863v3"}]

Based on the search results, I found information about "Dipper" at EMNLP 2025, though there are actually two different papers with that name:

1. **Dipper: Diversity in Prompts for Producing Large Language Model Ensembles in Reasoning Tasks** - This paper by Hu et al. was presented at EMNLP 2025 and focuses on using diversity in prompts to produce LLM ensembles for reasoning tasks.

2. **The original DIPPER paraphraser** - An 11B parameter paraphrase generation model called DIPPER (Discourse Paraphraser) was trained to execute paraphrase attacks. DIPPER possesses two unique features: (1) Paraphrasing long-form text in context, and (2) most modern paraphrasers are exclusively trained on sentence-level data, ignoring discourse-level information.

However, I should note that the search results don't contain specific information directly linking "Dipper," "paraphrase detection," and "tokenization" together at EMNLP 2025. The Dipper paper at EMNLP 2025 appears to focus on reasoning tasks with LLM ensembles rather than paraphrase detection. If you're looking for more specific information about tokenization approaches in paraphrase detection at EMNLP 2025, you may want to check the full conference proceedings or the paper directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "336e195f-1b39-41da-a9a7-1d43d3582bd9",
  "isSidechain": true,
  "promptId": "e4dedc50-3a35-4b66-994a-d3a71a42b739",
  "agentId": "ab97e4394c082e28d",
  "type": "user",
  "uuid": "da44fae1-2006-4f54-b422-a5ae57b4a0bc",
  "sourceToolAssistantUUID": "336e195f-1b39-41da-a9a7-1d43d3582bd9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T16:32:37.430Z_

<details><summary>↩ Tool result · `toolu_01SwFBKiwAy9RvncV4EfbrLS`</summary>

```text
Web search results for query: ""The Sequential Edge" arXiv 2511.02309 Sharma Chopra 2025"

Links: [{"title":"[2511.02309] The Sequential Edge: Inverse-Entropy Voting Beats Parallel Self-Consistency at Matched Compute","url":"https://arxiv.org/abs/2511.02309"},{"title":"The Sequential Edge: Inverse-Entropy Voting Beats Parallel Self-Consistency at Matched Compute","url":"https://arxiv.org/html/2511.02309v1"},{"title":"The Sequential Edge: Inverse-Entropy Voting Beats Parallel Self-Consistency at Matched Compute","url":"https://arxiv.org/pdf/2511.02309"},{"title":"The Sequential Edge: Inverse-Entropy Voting Beats","url":"https://www.arxiv.org/pdf/2511.02309"},{"title":"A neural basis for learning sequential memory in brain loop structures","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11330804/"}]

I found the paper! Here's what I found about "The Sequential Edge" arXiv 2511.02309:

The paper, authored by Aman Sharma and Paras Chopra, asks a fundamental question about test-time scaling for language model reasoning: at equal token budget and compute, is it better to run multiple independent chains in parallel, or to run fewer chains that iteratively refine through sequential steps?

Through comprehensive evaluation across 5 state-of-the-art open source models and 3 challenging reasoning benchmarks, the authors find that sequential scaling where chains explicitly build upon previous attempts consistently outperforms the dominant parallel self-consistency paradigm in 95.6% of configurations with gains in accuracy up to 46.7%.

The paper introduces inverse-entropy weighted voting, a novel training-free method to further boost the accuracy of sequential scaling. By weighing answers in proportion to the inverse entropy of their reasoning chains, they increase their success rate over parallel majority and establish it as the optimal test-time scaling strategy.

The paper was submitted on November 4, 2025, and is available on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "becd2fa9-9538-4934-9bba-dfa06e1d7f5e",
  "isSidechain": true,
  "promptId": "e4dedc50-3a35-4b66-994a-d3a71a42b739",
  "agentId": "ab97e4394c082e28d",
  "type": "user",
  "uuid": "33a2acf9-92b6-4c34-b748-88f379a8edd4",
  "sourceToolAssistantUUID": "becd2fa9-9538-4934-9bba-dfa06e1d7f5e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-19T16:32:40.295Z_

<details><summary>↩ Tool result · `toolu_01RU5uTzkbqBGUiJPqeD1pnG`</summary>

```text
Web search results for query: "CISC ACL 2025 Findings Taubenfeld tokenization"

Links: [{"title":"Confidence Improves Self-Consistency in LLMs - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.1030/"},{"title":"GitHub - taubenfeld/CISC: Official implementation for the Confidence Improves Self-Consistency in LLMs paper (ACL 2025, Finding)","url":"https://github.com/taubenfeld/CISC"},{"title":"Confidence Improves Self-Consistency in LLMs | Request PDF","url":"https://www.researchgate.net/publication/394271906_Confidence_Improves_Self-Consistency_in_LLMs"},{"title":"Confidence Improves Self-Consistency in LLMs","url":"https://aclanthology.org/2025.findings-acl.1030.pdf"},{"title":"[ACL 2025] Tokenization is Sensitive to Language Variation - YouTube","url":"https://www.youtube.com/watch?v=GnEpTTj4fc8"},{"title":"Tokenization is Sensitive to Language Variation - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.572/"},{"title":"Accepted Findings Papers - ACL 2025","url":"https://2025.aclweb.org/program/find_papers/"},{"title":"When Large Language Models Meet Speech: A Survey on ...","url":"https://aclanthology.org/2025.findings-acl.1041.pdf"}]

Based on the search results, I found relevant information about the papers you're asking about:

## CISC (Confidence Improves Self-Consistency)

The paper introduces Confidence-Informed Self-Consistency (CISC), authored by Amir Taubenfeld, Tom Sheffer, Eran Ofek, Amir Feder, Ariel Goldstein, Zorik Gekhman, and Gal Yona. CISC performs a weighted majority vote based on confidence scores obtained directly from the model, allowing it to identify the correct answer with a significantly smaller sample size by prioritizing high-confidence paths.

The paper is in the Findings of the Association for Computational Linguistics: ACL 2025.

## Tokenization Sensitivity Paper

Interestingly, the search also returned a separate ACL 2025 Findings paper on tokenization by different authors. "Tokenization is Sensitive to Language Variation" was published in Findings of the Association for Computational Linguistics: ACL 2025. However, this paper was authored by Wegmann, Nguyen, and Jurgens—not Taubenfeld.

If you were looking for a connection between Taubenfeld's CISC paper and tokenization, the search results include a brief mention that in the models evaluated in the CISC work, "(0" and "(1" are tokenized as two separate tokens, which relates to their confidence extraction methodology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a4999dc-d7c1-4e83-81c0-bf0b60c806f4",
  "isSidechain": true,
  "promptId": "e4dedc50-3a35-4b66-994a-d3a71a42b739",
  "agentId": "ab97e4394c082e28d",
  "type": "user",
  "uuid": "204b92f8-bae5-4f77-872a-31beb52d1c35",
  "sourceToolAssistantUUID": "3a4999dc-d7c1-4e83-81c0-bf0b60c806f4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-19T16:32:43.351Z_

Now let me do a few follow-up searches to clarify specific claimed details - notably the "Broken Tokens" spotlight designation, "Probabilistic Tokenization" claim numbers, and "Dipper" authorship/topic:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "204b92f8-bae5-4f77-872a-31beb52d1c35",
  "isSidechain": true,
  "agentId": "ab97e4394c082e28d",
  "requestId": "req_011CbCFNxq4GZNw3R7MyGWGf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f08f76c-388b-40a8-81be-0e980cd75975",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019Y3fXHtUCaW2ffpU4xpbtz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2059,
      "cache_creation_input_tokens": 1621,
      "cache_read_input_tokens": 14302,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1621,
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

_source line 29 · 2026-05-19T16:32:44.231Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CFcawkjJWjUDfH337rAK6A`</summary>

```json
{
  "query": "\"Broken Tokens\" NeurIPS 2025 spotlight designation Zheng Liu arithmetic digit grouping Llama"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f08f76c-388b-40a8-81be-0e980cd75975",
  "isSidechain": true,
  "agentId": "ab97e4394c082e28d",
  "requestId": "req_011CbCFNxq4GZNw3R7MyGWGf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9d95066-f20f-4d0c-9e3f-79ac666d2824",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019Y3fXHtUCaW2ffpU4xpbtz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2059,
      "cache_creation_input_tokens": 1621,
      "cache_read_input_tokens": 14302,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1621,
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

_source line 30 · 2026-05-19T16:32:45.458Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TSSY5uuiaCceqE8pxFvBf5`</summary>

```json
{
  "query": "Probabilistic Tokenization NAACL 2025 Sathe \"17\" improvement 7 base models 64 tokenizations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9d95066-f20f-4d0c-9e3f-79ac666d2824",
  "isSidechain": true,
  "agentId": "ab97e4394c082e28d",
  "requestId": "req_011CbCFNxq4GZNw3R7MyGWGf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "267584bd-be91-4cb8-9ad5-6cc3bc507b23",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019Y3fXHtUCaW2ffpU4xpbtz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2059,
      "cache_creation_input_tokens": 1621,
      "cache_read_input_tokens": 14302,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1621,
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

_source line 31 · 2026-05-19T16:32:45.903Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SJdsdE1vrUD1WX5WMFkiVP`</summary>

```json
{
  "query": "Dipper EMNLP 2025 \"Diversity in Prompts\" authors LLM ensembles reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "267584bd-be91-4cb8-9ad5-6cc3bc507b23",
  "isSidechain": true,
  "agentId": "ab97e4394c082e28d",
  "requestId": "req_011CbCFNxq4GZNw3R7MyGWGf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9b6a1f0-5cd7-46d6-8ef9-2c2111dcb335",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019Y3fXHtUCaW2ffpU4xpbtz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2059,
      "cache_creation_input_tokens": 1621,
      "cache_read_input_tokens": 14302,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1621,
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

_source line 32 · 2026-05-19T16:32:52.661Z_

<details><summary>↩ Tool result · `toolu_01TSSY5uuiaCceqE8pxFvBf5`</summary>

```text
Web search results for query: "Probabilistic Tokenization NAACL 2025 Sathe "17" improvement 7 base models 64 tokenizations"

Links: [{"title":"Improving Consistency in LLM Inference using Probabilistic Tokenization - ACL Anthology","url":"https://aclanthology.org/2025.findings-naacl.268/"},{"title":"Improving Consistency in LLM Inference using Probabilistic ...","url":"https://aclanthology.org/2025.findings-naacl.268.pdf"},{"title":"Broken Tokens? Your Language Model can Secretly Handle No n - Ca noni cal Tokenizations","url":"https://arxiv.org/html/2506.19004v1"},{"title":"Improving Self Consistency in LLMs through Probabilistic Tokenization","url":"https://arxiv.org/html/2407.03678v1"},{"title":"[2407.03678] Improving Self Consistency in LLMs through Probabilistic Tokenization","url":"https://arxiv.org/abs/2407.03678"},{"title":"Improving Self Consistency in LLMs through Probabilistic Tokenization","url":"https://arxiv.org/pdf/2407.03678"}]

Based on the search results, I found the paper you're looking for: "Improving Consistency in LLM Inference using Probabilistic Tokenization" by Sathe et al., published in the Findings of the Association for Computational Linguistics: NAACL 2025.

The paper presents an approach that involves employing multiple tokenizations of the same input string during the training phase of a language model. The research addresses the fact that modern large language models have yet to be trained using probabilistic tokenizations, despite tokenizers having the capability to generate multiple tokenizations.

The paper is published in the ACL Anthology and explores how probabilistic tokenization can enhance the self-consistency of LLMs in reasoning tasks, with experiments indicating that LLMs generate logically diverse reasoning paths.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "267584bd-be91-4cb8-9ad5-6cc3bc507b23",
  "isSidechain": true,
  "promptId": "e4dedc50-3a35-4b66-994a-d3a71a42b739",
  "agentId": "ab97e4394c082e28d",
  "type": "user",
  "uuid": "ce063888-8742-4136-b054-4c1b43b3a7e9",
  "sourceToolAssistantUUID": "267584bd-be91-4cb8-9ad5-6cc3bc507b23",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-19T16:32:57.933Z_

<details><summary>↩ Tool result · `toolu_01CFcawkjJWjUDfH337rAK6A`</summary>

```text
Web search results for query: ""Broken Tokens" NeurIPS 2025 spotlight designation Zheng Liu arithmetic digit grouping Llama"

Links: [{"title":"Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations | OpenReview","url":"https://openreview.net/forum?id=WrYWolqKh3"},{"title":"NeurIPS Poster Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/117561"},{"title":"[2506.19004] Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations","url":"https://arxiv.org/abs/2506.19004"},{"title":"Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations","url":"https://arxiv.org/pdf/2506.19004"},{"title":"Efficient numeracy in language models through single-token number embeddings","url":"https://arxiv.org/pdf/2510.06824"}]

Based on the search results, I found information about the "Broken Tokens" paper and its NeurIPS 2025 spotlight designation:

The paper "Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations" received a NeurIPS 2025 spotlight designation. 

The paper is authored by Brian Siyuan Zheng, Alisa Liu, Orevaoghene Ahia, and others from the Allen Institute for AI and Stanford University. However, I should note that the search results show "Brian Siyuan Zheng" rather than "Zheng Liu" as the author's name.

The research found that right-aligned digit grouping enhances large-number arithmetic by +33%, which relates to the arithmetic and digit grouping aspect of your query. The findings demonstrate that character-level segmentation improves string manipulation and code understanding tasks by up to 15%, and right-aligned digit grouping enhances large-number arithmetic by over 33%.

The paper investigates how language models handle non-canonical tokenizations and when alternative tokenization schemes can actually improve performance on specific tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9d95066-f20f-4d0c-9e3f-79ac666d2824",
  "isSidechain": true,
  "promptId": "e4dedc50-3a35-4b66-994a-d3a71a42b739",
  "agentId": "ab97e4394c082e28d",
  "type": "user",
  "uuid": "48767d65-669f-44e0-94e3-87bc9d8739bd",
  "sourceToolAssistantUUID": "b9d95066-f20f-4d0c-9e3f-79ac666d2824",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T16:33:00.437Z_

<details><summary>↩ Tool result · `toolu_01SJdsdE1vrUD1WX5WMFkiVP`</summary>

```text
Web search results for query: "Dipper EMNLP 2025 "Diversity in Prompts" authors LLM ensembles reasoning"

Links: [{"title":"Dipper: Diversity in Prompts for Producing Large Language Model Ensembles in Reasoning Tasks - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1801/"},{"title":"Dipper: Diversity in Prompts for Producing Large Language Model Ensembles in Reasoning Tasks | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/2025.emnlp-main.1801@ACL"},{"title":"Dipper: Diversity in Prompts for Producing Large Language Model Ensembles in Reasoning tasks | OpenReview","url":"https://openreview.net/forum?id=0wQsCNrlFl"},{"title":"Dipper: Diversity in Prompts for Producing Large Language Model Ensembles in Reasoning tasks","url":"https://arxiv.org/html/2412.15238v1"},{"title":"[2412.15238] Dipper: Diversity in Prompts for Producing Large Language Model Ensembles in Reasoning tasks","url":"https://arxiv.org/abs/2412.15238"},{"title":"Dipper: Diversity in Prompts for Producing Large Language ...","url":"https://arxiv.org/pdf/2412.15238"},{"title":"[Literature Review] Dipper: Diversity in Prompts for Producing Large Language Model Ensembles in Reasoning tasks","url":"https://www.themoonlight.io/en/review/dipper-diversity-in-prompts-for-producing-large-language-model-ensembles-in-reasoning-tasks"},{"title":"Dipper: Diversity in Prompts for Producing Large Language Model Ensembles in Reasoning Tasks","url":"https://www.researchgate.net/publication/397423236_Dipper_Diversity_in_Prompts_for_Producing_Large_Language_Model_Ensembles_in_Reasoning_Tasks"},{"title":"Dipper: Diversity in Prompts for Producing Large Language Model","url":"https://www.comp.nus.edu.sg/~greglau/assets/pdf/arr_dipper.pdf"}]

Based on the search results, here's the information about the Dipper paper:

## Paper Details

The paper "Dipper: Diversity in Prompts for Producing Large Language Model Ensembles in Reasoning Tasks" was authored by Hu, Wenyang; Lau, Gregory Kang Ruey; Diwen, Liu; Jizhuo, Chen; Ng, See-Kiong; and Low, Bryan Kian Hsiang, and was presented at EMNLP 2025.

## Overview

DIPPER is a novel, training-free framework that transforms a single LLM into an effective inference-time ensemble by feeding the model an optimized and diverse set of prompts in parallel, which elicits varied reasoning paths, leading to performance gains.

## Key Findings

The results show that a DIPPER ensemble of three Qwen2-MATH-1.5B instances (via parallel prompting of a single model) outperforms a larger Qwen2-MATH-7B model. The DIPPER method significantly outperforms all established baselines across different ensemble sizes, illustrating the importance of using diverse prompts in ensemble learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9b6a1f0-5cd7-46d6-8ef9-2c2111dcb335",
  "isSidechain": true,
  "promptId": "e4dedc50-3a35-4b66-994a-d3a71a42b739",
  "agentId": "ab97e4394c082e28d",
  "type": "user",
  "uuid": "a002b2bb-6ff7-4964-9cd8-00325c509e9c",
  "sourceToolAssistantUUID": "d9b6a1f0-5cd7-46d6-8ef9-2c2111dcb335",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-19T16:33:04.077Z_

Now let me check a couple more specific claims - the NeurIPS 2025 "Spotlight" vs "Poster" designation for "Broken Tokens", and verify the Probabilistic Tokenization specific numbers:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a002b2bb-6ff7-4964-9cd8-00325c509e9c",
  "isSidechain": true,
  "agentId": "ab97e4394c082e28d",
  "requestId": "req_011CbCFQSv2YxdBXh6MgR4bR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "68954ed7-0330-4d95-a248-52c70df3ee77",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01D6dcQs1ZJDFcwob8hf95Rf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4279,
      "cache_read_input_tokens": 15923,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4279,
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

_source line 36 · 2026-05-19T16:33:04.875Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01En6f5h58LcxpoXgdBjSpf3`</summary>

```json
{
  "query": "arxiv 2506.19004 \"Broken Tokens\" NeurIPS spotlight poster designation openreview"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68954ed7-0330-4d95-a248-52c70df3ee77",
  "isSidechain": true,
  "agentId": "ab97e4394c082e28d",
  "requestId": "req_011CbCFQSv2YxdBXh6MgR4bR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9130ba48-78e4-4a30-8af1-a8dac6b59116",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01D6dcQs1ZJDFcwob8hf95Rf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4279,
      "cache_read_input_tokens": 15923,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4279,
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

_source line 37 · 2026-05-19T16:33:05.903Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Lrs2uP6EDMrVAHUNDAfgSy`</summary>

```json
{
  "query": "arxiv 2407.03678 probabilistic tokenization Sathe Aggarwal Sitaram \"5 LLM\" OR \"7 base\" OR \"64\" OR \"17\" benchmark results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9130ba48-78e4-4a30-8af1-a8dac6b59116",
  "isSidechain": true,
  "agentId": "ab97e4394c082e28d",
  "requestId": "req_011CbCFQSv2YxdBXh6MgR4bR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "edb19e40-3874-46ce-b978-a1022155bc47",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01D6dcQs1ZJDFcwob8hf95Rf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4279,
      "cache_read_input_tokens": 15923,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4279
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 205,
          "cache_read_input_tokens": 15923,
          "cache_creation_input_tokens": 4279,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4279,
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

_source line 38 · 2026-05-19T16:33:11.102Z_

<details><summary>↩ Tool result · `toolu_01Lrs2uP6EDMrVAHUNDAfgSy`</summary>

```text
Web search results for query: "arxiv 2407.03678 probabilistic tokenization Sathe Aggarwal Sitaram "5 LLM" OR "7 base" OR "64" OR "17" benchmark results"

Links: [{"title":"[2407.03678] Improving Self Consistency in LLMs through Probabilistic Tokenization","url":"https://arxiv.org/abs/2407.03678"},{"title":"Improving Self Consistency in LLMs through Probabilistic Tokenization","url":"https://www.researchgate.net/publication/382066000_Improving_Self_Consistency_in_LLMs_through_Probabilistic_Tokenization"},{"title":"Improving Consistency in LLM Inference using Probabilistic Tokenization - ACL Anthology","url":"https://aclanthology.org/2025.findings-naacl.268/"},{"title":"Speculative Decoding for Multi-Sample Inference | Request PDF","url":"https://www.researchgate.net/publication/389693996_Speculative_Decoding_for_Multi-Sample_Inference"},{"title":"Improving Self Consistency in LLMs through Probabilistic Tokenization","url":"https://arxiv.org/html/2407.03678v1"},{"title":"Improving Self Consistency in LLMs through Probabilistic Tokenization","url":"https://arxiv.org/pdf/2407.03678"}]

I found the paper arxiv 2407.03678. Here are the key details:

**Paper Information:**
The paper is titled "Improving Self Consistency in LLMs through Probabilistic Tokenization" by authors Ashutosh Sathe, Divyanshu Aggarwal, and Sunayana Sitaram.

**Research Focus:**
The work proposes a novel method to leverage the multiple tokenization capabilities of modern LLM tokenizers to enhance the self-consistency of LLMs in reasoning tasks, with experiments indicating that LLMs generate logically diverse reasoning paths when utilizing probabilistic tokenizations.

**Experimental Scope:**
The study involves extensive experimentation on 5 LLM families and 4 reasoning benchmarks.

However, the search results show abstract/overview pages rather than the detailed benchmark results you're looking for. To access the specific numerical results mentioned in your query (related to parameters like "5 LLM", "7 base", "64", "17"), you would need to view the full PDF of the paper directly on arXiv at https://arxiv.org/pdf/2407.03678 or through the HTML version at https://arxiv.org/html/2407.03678v1.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "edb19e40-3874-46ce-b978-a1022155bc47",
  "isSidechain": true,
  "promptId": "e4dedc50-3a35-4b66-994a-d3a71a42b739",
  "agentId": "ab97e4394c082e28d",
  "type": "user",
  "uuid": "6424e3cd-51d7-48d2-a2c9-cb58cdeae95c",
  "sourceToolAssistantUUID": "edb19e40-3874-46ce-b978-a1022155bc47",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-19T16:33:13.561Z_

<details><summary>↩ Tool result · `toolu_01En6f5h58LcxpoXgdBjSpf3`</summary>

```text
Web search results for query: "arxiv 2506.19004 "Broken Tokens" NeurIPS spotlight poster designation openreview"

Links: [{"title":"[2506.19004] Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations","url":"https://arxiv.org/abs/2506.19004"},{"title":"Broken Tokens? Your Language Model can Secretly Handle No n - Ca noni cal Tokenizations","url":"https://arxiv.org/html/2506.19004v1"},{"title":"arXiv:2506.19004v1 [cs.CL] 23 Jun 2025 Broken Tokens? Your Language Model can","url":"https://arxiv.org/pdf/2506.19004"},{"title":"dblp: Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations.","url":"https://dblp.org/rec/journals/corr/abs-2506-19004.html"},{"title":"Broken-Token: Filtering Obfuscated Prompts by Counting Characters-Per-Token","url":"https://arxiv.org/pdf/2510.26847"}]

I found information about the arxiv paper 2506.19004 titled "Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations." However, the search results don't contain specific information about its NeurIPS spotlight poster designation or OpenReview details. Let me search more specifically for that information.

Links: [{"title":"NeurIPS 2026 | OpenReview","url":"https://openreview.net/group?id=NeurIPS.cc%2F2026"},{"title":"NeurIPS 2026 Conference | OpenReview","url":"https://openreview.net/group?id=NeurIPS.cc%2F2026%2FConference"},{"title":"NeurIPS 2026 Workshop Proposals | OpenReview","url":"https://openreview.net/group?id=NeurIPS.cc%2F2026%2FWorkshop_Proposals"},{"title":"NeurIPS 2025 Poster Instructions","url":"https://neurips.cc/Conferences/2025/PosterInstructions"},{"title":"NeurIPS | OpenReview","url":"https://openreview.net/group?id=NeurIPS.cc"},{"title":"Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations","url":"https://arxiv.org/pdf/2506.19004"},{"title":"2026 Conference – NeurIPS Blog","url":"https://blog.neurips.cc/category/2026-conference/"},{"title":"NeurIPS 2026 Call for Position Papers","url":"https://neurips.cc/Conferences/2026/CallForPositionPapers"},{"title":"NeurIPS 2026","url":"https://neurips.cc/"}]

Based on my search results, I found information about the paper "Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations" by Brian Siyuan Zheng, Alisa Liu, Orevaoghene Ahia, Jonathan Hayase, Yejin Choi, and Noah A. Smith. The paper investigates instruction-tuned models' robustness to non-canonical tokenizations, finding that these models retain up to 93.4% of their original performance when given a randomly sampled tokenization, and 90.8% with character-level tokenization.

However, the search results do not contain specific information about this paper's designation as a NeurIPS spotlight poster or its OpenReview status. While NeurIPS 2026 is actively accepting submissions, the search results only provide general information about the conference and its submission process, not specific acceptance decisions or spotlight designations for individual papers at this time.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9130ba48-78e4-4a30-8af1-a8dac6b59116",
  "isSidechain": true,
  "promptId": "e4dedc50-3a35-4b66-994a-d3a71a42b739",
  "agentId": "ab97e4394c082e28d",
  "type": "user",
  "uuid": "6a88e53a-fae3-4a0e-98cd-783c340e5e97",
  "sourceToolAssistantUUID": "9130ba48-78e4-4a30-8af1-a8dac6b59116",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-19T16:33:15.688Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018mLdMz1zw9BZVFptorm5Bk`</summary>

```json
{
  "query": "neurips.cc 2025 poster 117561 \"Broken Tokens\" spotlight"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a88e53a-fae3-4a0e-98cd-783c340e5e97",
  "isSidechain": true,
  "agentId": "ab97e4394c082e28d",
  "requestId": "req_011CbCFRQziJSShGPEKTuggx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da7218f1-efce-43d9-8858-f9a128102f72",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QgifgLwXnoMRATcqic8JYS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 674,
      "cache_creation_input_tokens": 1176,
      "cache_read_input_tokens": 20202,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1176,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
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

_source line 41 · 2026-05-19T16:33:16.581Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01617hvQaR4wHC9BFVnh4naH`</summary>

```json
{
  "query": "EDIS 2602.01288 authors full list Zhu entropy dynamics LLM reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da7218f1-efce-43d9-8858-f9a128102f72",
  "isSidechain": true,
  "agentId": "ab97e4394c082e28d",
  "requestId": "req_011CbCFRQziJSShGPEKTuggx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e78c5f4-acf5-4efc-8cf1-1c384638fc81",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QgifgLwXnoMRATcqic8JYS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 674,
      "cache_creation_input_tokens": 1176,
      "cache_read_input_tokens": 20202,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1176
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 674,
          "output_tokens": 127,
          "cache_read_input_tokens": 20202,
          "cache_creation_input_tokens": 1176,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1176,
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

_source line 42 · 2026-05-19T16:33:20.516Z_

<details><summary>↩ Tool result · `toolu_018mLdMz1zw9BZVFptorm5Bk`</summary>

```text
Web search results for query: "neurips.cc 2025 poster 117561 "Broken Tokens" spotlight"

Links: [{"title":"NeurIPS Poster Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/117561"},{"title":"NeurIPS 2025 Poster Instructions","url":"https://neurips.cc/Conferences/2025/PosterInstructions"},{"title":"NeurIPS 2025 Spotlights","url":"https://neurips.cc/virtual/2025/events/spotlight"},{"title":"NeurIPS Poster Don't Just Chase “Highlighted Tokens” in MLLMs: Revisiting Visual Holistic Context Retention","url":"https://neurips.cc/virtual/2025/poster/115059"},{"title":"NeurIPS 2025 Posters","url":"https://neurips.cc/virtual/2025/loc/san-diego/events/poster"},{"title":"Poster Uploads | Wiki.EventHosts NeurIPS/ICML/ICLR/CVPR and more","url":"https://wiki.eventhosts.cc/en/reference/posteruploads"},{"title":"14 noteworthy posters to explore at NeurIPS 2025 in San Diego and Mexico City – MIT Jameel Clinic","url":"https://jclinic.mit.edu/14-must-see-posters-at-neurips-2025-in-san-diego-and-mexico-city/"},{"title":"Broken Words, Broken Performance: Effect of Tokenization on Performance of LLMs","url":"https://arxiv.org/pdf/2512.21933"}]

Based on the search results, I found the poster you're looking for:

The paper investigates the robustness of language models to input encoded with non-canonical tokenizations entirely unseen during training. When evaluated across 20 benchmarks, instruction-tuned models retain up to 93.4% of their performance with these non-canonical tokenizations.

The full title of the poster is "Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations," and it's listed as a spotlight presentation at NeurIPS 2025. Spotlight is an honor tag that is given to selected posters.

You can access the poster directly at: https://neurips.cc/virtual/2025/loc/san-diego/poster/117561


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da7218f1-efce-43d9-8858-f9a128102f72",
  "isSidechain": true,
  "promptId": "e4dedc50-3a35-4b66-994a-d3a71a42b739",
  "agentId": "ab97e4394c082e28d",
  "type": "user",
  "uuid": "fea1847d-3262-4073-850a-0547f6740e4e",
  "sourceToolAssistantUUID": "da7218f1-efce-43d9-8858-f9a128102f72",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-19T16:33:22.706Z_

<details><summary>↩ Tool result · `toolu_01617hvQaR4wHC9BFVnh4naH`</summary>

```text
Web search results for query: "EDIS 2602.01288 authors full list Zhu entropy dynamics LLM reasoning"

Links: [{"title":"[2602.01288] EDIS: Diagnosing LLM Reasoning via Entropy Dynamics","url":"https://arxiv.org/abs/2602.01288"},{"title":"EDIS: Diagnosing LLM Reasoning via Entropy Dynamics","url":"https://arxiv.org/html/2602.01288"},{"title":"EDIS: Diagnosing LLM Reasoning via Entropy Dynamics","url":"https://arxiv.org/pdf/2602.01288"},{"title":"Entropy Dynamics in LLMs: Metrics & Implications","url":"https://www.emergentmind.com/topics/entropy-dynamics-in-llms"},{"title":"On the Entropy Dynamics in Reinforcement Fine-Tuning of Large Language Models","url":"https://arxiv.org/pdf/2602.03392"}]

Based on the search results, I found the full author list for paper EDIS 2602.01288:

The authors of EDIS: Diagnosing LLM Reasoning via Entropy Dynamics are: Chenghua Zhu, Siyan Wu, Xiangkang Zeng, Zishan Xu, Zhaolu Kang, Yifu Guo, Yuquan Lu, Junduan Huang, and Guojing Zhou.

The paper introduces the Entropy Dynamics Instability Score (EDIS), a trajectory-level metric quantifying instability in entropy evolution that serves as an effective diagnostic signal for inference-time selection to improve reasoning accuracy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e78c5f4-acf5-4efc-8cf1-1c384638fc81",
  "isSidechain": true,
  "promptId": "e4dedc50-3a35-4b66-994a-d3a71a42b739",
  "agentId": "ab97e4394c082e28d",
  "type": "user",
  "uuid": "e4f86bdb-cd6e-4649-b8d4-358a0e69bd77",
  "sourceToolAssistantUUID": "1e78c5f4-acf5-4efc-8cf1-1c384638fc81",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-19T16:34:25.741Z_

I now have enough information to give a comprehensive verification report. Here are the findings for all 10 papers:

---

## Verification Report

### 1. "Broken Tokens" — VERIFIED WITH MINOR CLAIM DISCREPANCY

**Existence:** Confirmed. arXiv:2506.19004, published June 23, 2025.
**Authors:** Brian Siyuan Zheng, Alisa Liu, Orevaoghene Ahia, Jonathan Hayase, Yejin Choi, Noah A. Smith. Matches the claimed author list.
**Venue:** Confirmed at NeurIPS 2025. However, the NeurIPS virtual site page URL uses the word "Poster" (neurips.cc/virtual/2025/.../poster/117561), not "Spotlight." There is a separate NeurIPS 2025 Spotlights page, and the search AI inferred it was listed there, but the URL structure says "poster." The Spotlight designation should be verified directly on neurips.cc/virtual/2025/events/spotlight.
**Key claims:**
- ~93% performance retention: Confirmed (~93.4% with random tokenization, 90.8% with character-level).
- +33.7pp arithmetic with digit grouping on Llama-3.1-8B-Instruct: The paper confirms right-aligned digit grouping yields "+33%" arithmetic improvement — plausible match, exact figure unverified from search.
- -6.1pp Qwen-2.5-7B-Instruct GSM8k: Not found in search results; cannot confirm this specific number from available sources.

**Flag:** The venue may be "Poster" not "Spotlight." The specific -6.1pp Qwen figure was not independently confirmed.

---

### 2. "Probabilistic Tokenization" — VERIFIED WITH CLAIM DISCREPANCIES

**Existence:** Confirmed. arXiv:2407.03678, published as "Improving Consistency in LLM Inference using Probabilistic Tokenization" (also titled "Improving Self Consistency in LLMs through Probabilistic Tokenization" in the arXiv version).
**Authors:** Ashutosh Sathe, Divyanshu Aggarwal, Sunayana Sitaram. Matches claimed authors.
**Venue:** Confirmed. Findings of NAACL 2025 (ACL Anthology: 2025.findings-naacl.268). Matches.
**Key claims:**
- "+17.11% average": Not confirmed from search; no specific number surfaced.
- "7 base models": The paper reports experiments on **5 LLM families**, not 7. This is a discrepancy.
- "4 benchmarks": Confirmed (4 reasoning benchmarks mentioned).
- "64 random BPE tokenizations": Not confirmed from search.

**Flag:** The "7 base models" claim conflicts with the paper's own description of "5 LLM families." The specific +17.11% figure was not independently confirmed.

---

### 3. "Where is the Signal in Tokenization Space?" — VERIFIED

**Existence:** Confirmed. arXiv:2408.08541.
**Authors:** Renato Lui Geh, Honghua Zhang, Kareem Ahmed, Benjie Wang, Guy Van Den Broeck. The claimed "Geh et al." matches.
**Venue:** Confirmed. EMNLP 2024 main conference (ACL Anthology: 2024.emnlp-main.230), Miami, FL.
**Key claims:** The paper aggregates probabilities from non-canonical tokenizations and achieves benchmark improvements across architectures including transformers and SSMs. All verified.

**Status: All checked elements match.**

---

### 4. "NumeroLogic" — VERIFIED

**Existence:** Confirmed. arXiv:2404.00459.
**Authors:** Eli Schwartz, Leshem Choshen, Joseph Shtok, Sivan Doveh, Leonid Karlinsky, Assaf Arbelle. Exact match.
**Venue:** Confirmed. EMNLP 2024 main conference (ACL Anthology: 2024.emnlp-main.12), pages 206–212. Exact match.
**Key claims:** Proposes prefixing numbers with their digit count (e.g., "2:42" for "42") to improve numerical reasoning. Verified.

**Status: All checked elements match.**

---

### 5. "SepSeq" — VERIFIED WITH NOTABLE TOPIC DIFFERENCE FROM FRAMING

**Existence:** Confirmed. arXiv:2604.07737v1, submitted April 9, 2026.
**Authors:** Jie Sun et al. Matches "Sun et al."
**Venue:** arXiv preprint (not peer-reviewed venue at time of search). Matches claimed arXiv designation.
**Key claims:**
- 35.6% relative accuracy improvement across 9 LLMs: Confirmed exactly.
- Topic note: This paper is about inserting separator tokens for long **numerical sequence** processing (attention sink mechanism), not tokenization in the BPE/encoding sense. The framing as a "tokenization" paper needs care.

**Status: Existence and numbers verified. Correct arXiv ID and author.**

---

### 6. "The Sequential Edge" — VERIFIED WITH TOPIC DISCREPANCY

**Existence:** Confirmed. arXiv:2511.02309, submitted November 4, 2025.
**Authors:** Aman Sharma and Paras Chopra. Exact match.
**Venue:** arXiv preprint. Matches.
**Key claims:** The paper is about test-time compute scaling — sequential vs. parallel self-consistency chains — and introduces inverse-entropy weighted voting. Gains up to 46.7% accuracy, outperforming parallel self-consistency in 95.6% of configurations.

**Topic flag:** This paper is about sequential inference-time scaling / self-consistency voting, not tokenization. If it is cited in a tokenization context, the connection should be explained.

---

### 7. "CISC" — VERIFIED

**Existence:** Confirmed. "Confidence Improves Self-Consistency in LLMs."
**Authors:** Amir Taubenfeld, Tom Sheffer, Eran Ofek, Amir Feder, Ariel Goldstein, Zorik Gekhman, Gal Yona. Taubenfeld is first author — matches "Taubenfeld et al."
**Venue:** Confirmed. Findings of ACL 2025 (ACL Anthology: 2025.findings-acl.1030). Exact match.
**GitHub:** Official implementation at github.com/taubenfeld/CISC.

**Status: All checked elements match.**

---

### 8. "VecCISC" — VERIFIED

**Existence:** Confirmed. arXiv:2605.08070v1, submitted May 2026.
**Authors:** James Petullo, Sonny George, Dylan Cashman, Nianwen Xue (Brandeis University). Matches "Petullo et al."
**Venue:** arXiv preprint. Matches.
**Key claims:** Builds on CISC using semantic similarity / clustering of reasoning traces to reduce candidate answers; reduces total token usage by 47%.

**Status: Existence, arXiv ID, and authors verified.**

---

### 9. "Dipper" — VERIFIED WITH TOPIC CLARIFICATION

**Existence:** Confirmed. "Dipper: Diversity in Prompts for Producing Large Language Model Ensembles in Reasoning Tasks." arXiv:2412.15238.
**Authors:** Wenyang Hu, Gregory Kang Ruey Lau, Liu Diwen, Chen Jizhuo, See-Kiong Ng, Bryan Kian Hsiang Low.
**Venue:** Confirmed. EMNLP 2025 main conference (ACL Anthology: 2025.emnlp-main.1801). Matches.
**Key claims:** Training-free framework using diverse prompt sets to create LLM ensembles; a 3-instance Qwen2-MATH-1.5B ensemble outperforms Qwen2-MATH-7B.

**Topic note:** This "Dipper" is about prompt diversity for LLM ensembles, not paraphrase detection/watermarking. There is an older unrelated DIPPER paraphrase model (2023). If the cited paper is confused with the 2023 one, that would be a citation error.

---

### 10. "EDIS" — VERIFIED

**Existence:** Confirmed. arXiv:2602.01288, submitted February 1, 2026, revised March 6, 2026. Full title: "EDIS: Diagnosing LLM Reasoning via Entropy Dynamics."
**Authors:** Chenghua Zhu, Siyan Wu, Xiangkang Zeng, Zishan Xu, Zhaolu Kang, Yifu Guo, Yuquan Lu, Junduan Huang, Guojing Zhou (9 authors).
**Venue:** arXiv preprint. Matches.
**Key claims:** Introduces the Entropy Dynamics Instability Score (EDIS), a trajectory-level metric for token-level entropy during generation; identifies burst/peak-valley spikes in erroneous reasoning. Verified.

**Status: Existence, arXiv ID, and topic verified.**

---

## Summary Table

| # | Paper | Exists | Venue Correct | Authors Match | Claims Verified | Flags |
|---|-------|--------|--------------|---------------|-----------------|-------|
| 1 | Broken Tokens | Yes | Likely (Poster not Spotlight?) | Yes | Partial | Spotlight designation uncertain; -6.1pp Qwen figure unconfirmed |
| 2 | Probabilistic Tokenization | Yes | Yes (NAACL 2025 Findings) | Yes | Partial | "7 base models" conflicts with paper's "5 LLM families"; +17.11% unconfirmed |
| 3 | Signal in Tokenization Space | Yes | Yes (EMNLP 2024) | Yes (Geh et al.) | Yes | None |
| 4 | NumeroLogic | Yes | Yes (EMNLP 2024) | Yes (exact) | Yes | None |
| 5 | SepSeq | Yes | Yes (arXiv:2604.07737) | Yes | Yes (35.6%) | Topic is numerical sequences via separator tokens, not BPE |
| 6 | The Sequential Edge | Yes | Yes (arXiv:2511.02309) | Yes | Yes | Topic is inference-time scaling, not tokenization per se |
| 7 | CISC | Yes | Yes (ACL 2025 Findings) | Yes | Yes | None |
| 8 | VecCISC | Yes | Yes (arXiv:2605.08070) | Yes | Yes | None |
| 9 | Dipper | Yes | Yes (EMNLP 2025) | Yes | Yes | Unrelated to older 2023 DIPPER paraphrase model |
| 10 | EDIS | Yes | Yes (arXiv:2602.01288) | Yes | Yes | None |

**Key concerns to follow up:**
- Paper 1: Confirm "Spotlight" vs. "Poster" at neurips.cc/virtual/2025/events/spotlight directly.
- Paper 2: The "7 base models" claim likely overstates scope — the paper itself says 5 LLM families. The +17.11% figure needs verification from the paper PDF.

Sources:
- [NeurIPS Poster: Broken Tokens](https://neurips.cc/virtual/2025/poster/117561)
- [arXiv:2506.19004 Broken Tokens](https://arxiv.org/abs/2506.19004)
- [OpenReview: Broken Tokens](https://openreview.net/forum?id=WrYWolqKh3)
- [NAACL 2025 Findings: Probabilistic Tokenization](https://aclanthology.org/2025.findings-naacl.268/)
- [arXiv:2407.03678 Probabilistic Tokenization](https://arxiv.org/abs/2407.03678)
- [EMNLP 2024: Where is the Signal in Tokenization Space?](https://aclanthology.org/2024.emnlp-main.230/)
- [arXiv:2408.08541 Signal in Tokenization Space](https://arxiv.org/abs/2408.08541)
- [EMNLP 2024: NumeroLogic](https://aclanthology.org/2024.emnlp-main.12/)
- [arXiv:2404.00459 NumeroLogic](https://arxiv.org/abs/2404.00459)
- [arXiv:2604.07737 SepSeq](https://arxiv.org/abs/2604.07737)
- [arXiv:2511.02309 The Sequential Edge](https://arxiv.org/abs/2511.02309)
- [ACL 2025 Findings: CISC](https://aclanthology.org/2025.findings-acl.1030/)
- [GitHub: CISC](https://github.com/taubenfeld/CISC)
- [arXiv:2605.08070 VecCISC](https://arxiv.org/abs/2605.08070v1)
- [EMNLP 2025: Dipper](https://aclanthology.org/2025.emnlp-main.1801/)
- [arXiv:2412.15238 Dipper](https://arxiv.org/abs/2412.15238)
- [arXiv:2602.01288 EDIS](https://arxiv.org/abs/2602.01288)
- [NeurIPS 2025 Spotlights](https://neurips.cc/virtual/2025/events/spotlight)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4f86bdb-cd6e-4649-b8d4-358a0e69bd77",
  "isSidechain": true,
  "agentId": "ab97e4394c082e28d",
  "requestId": "req_011CbCFS67gdNv2ALRueAcKa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "06bfef2e-8740-4657-aa07-1fa8ceec3fb4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "af03741e-539d-4f33-b688-b98e1be0cf0d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015GLjVaeT92EbvwbZmgnj4S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1893,
      "cache_read_input_tokens": 21378,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1893,
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
