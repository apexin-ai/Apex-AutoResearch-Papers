# Research conversation: I need to research the paper "Navigating the Alignment-Calibration Trade-off" (arXiv 2510.17426, Hu et al. 2025) which s

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a89ea087990aa2200.jsonl`
- **Structured JSON:** [`b4a9f840ad75136c3c1d.json`](../../sessions/b4/b4a9f840ad75136c3c1d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

42 recorded events

### User

_source line 1 · 2026-05-19T23:06:40.614Z_

I need to research the paper "Navigating the Alignment-Calibration Trade-off" (arXiv 2510.17426, Hu et al. 2025) which shows that simple weight interpolation between base and post-trained models achieves Pareto-dominant calibration-accuracy tradeoffs.

Also search for and read the Dual-Align paper (arXiv 2601.04277) which addresses confidence-drift between base and post-trained models.

For each paper, I need:
1. The exact method proposed (how weight interpolation / dual-alignment works)
2. Key results — what calibration improvements do they achieve?
3. What benchmarks do they use?
4. What are the limitations?
5. How could a mechanistic circuit-level approach improve upon them?

Search queries to use:
- "weight interpolation base model post-trained calibration alignment trade-off 2510.17426"
- "Dual-Align confidence drift calibration LLM 2601.04277"
- "model merging calibration LLM weight averaging"
- "BaseCal base model signals calibration 2601.03042"

Fetch the actual papers if you can find arxiv URLs. Report in detail — I need to understand these methods deeply to position against them as baselines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8c21e000-65bc-4fe4-b616-175d69471633",
  "agentId": "a89ea087990aa2200",
  "type": "user",
  "uuid": "06971185-5cd9-45b2-a70d-db7e7cba5ee1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T23:06:40.618Z_

```json
{
  "parentUuid": "06971185-5cd9-45b2-a70d-db7e7cba5ee1",
  "isSidechain": true,
  "agentId": "a89ea087990aa2200",
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
  "uuid": "76286a89-302a-481f-936e-258284c5935e",
  "timestamp": "2026-05-19T23:06:40.618Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-19T23:06:40.618Z_

```json
{
  "parentUuid": "76286a89-302a-481f-936e-258284c5935e",
  "isSidechain": true,
  "agentId": "a89ea087990aa2200",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "94aacdca-ee6d-4d0c-9b22-c40675a3b155",
  "timestamp": "2026-05-19T23:06:40.618Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-19T23:06:43.308Z_



I'll research these papers by fetching them from arXiv. Let me start by loading the WebFetch and WebSearch tools, then fetch the papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94aacdca-ee6d-4d0c-9b22-c40675a3b155",
  "isSidechain": true,
  "agentId": "a89ea087990aa2200",
  "requestId": "req_011CbCmRbKZvWL8ytV4kKV5j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5bb10698-ff79-4bb1-8bc5-d1af732da6fd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nxu9CfvGsRRzcgaw8p5t7C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1631,
      "cache_read_input_tokens": 7773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1631,
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

_source line 5 · 2026-05-19T23:06:43.588Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016PLFZAZtdmTW5pnCz8yDhq`</summary>

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
  "parentUuid": "5bb10698-ff79-4bb1-8bc5-d1af732da6fd",
  "isSidechain": true,
  "agentId": "a89ea087990aa2200",
  "requestId": "req_011CbCmRbKZvWL8ytV4kKV5j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c81dbb0-5ea6-4ddc-8df2-241d49126368",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nxu9CfvGsRRzcgaw8p5t7C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1631,
      "cache_read_input_tokens": 7773,
      "output_tokens": 114,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1631
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 114,
          "cache_read_input_tokens": 7773,
          "cache_creation_input_tokens": 1631,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1631,
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

_source line 6 · 2026-05-19T23:06:43.593Z_

<details><summary>↩ Tool result · `toolu_016PLFZAZtdmTW5pnCz8yDhq`</summary>

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
  "parentUuid": "3c81dbb0-5ea6-4ddc-8df2-241d49126368",
  "isSidechain": true,
  "promptId": "8c21e000-65bc-4fe4-b616-175d69471633",
  "agentId": "a89ea087990aa2200",
  "type": "user",
  "uuid": "d21025da-4200-45c8-ba76-c1c091b4e8ac",
  "sourceToolAssistantUUID": "3c81dbb0-5ea6-4ddc-8df2-241d49126368",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-19T23:06:45.892Z_



Now let me fetch the papers and run searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d21025da-4200-45c8-ba76-c1c091b4e8ac",
  "isSidechain": true,
  "agentId": "a89ea087990aa2200",
  "requestId": "req_011CbCmRpGBohgpzcHQH7jEp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4b4ef00a-1ac8-4c60-ae09-95ddc096e586",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SFSSHuPgouqXXT8Te5Y5WU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1136,
      "cache_read_input_tokens": 9404,
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

_source line 8 · 2026-05-19T23:06:47.363Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01ALehQvVPkxnoa36hvZxqgc`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.17426",
  "prompt": "Extract the full title, all authors, abstract, and any details about the method, results, benchmarks, and limitations from this paper page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b4ef00a-1ac8-4c60-ae09-95ddc096e586",
  "isSidechain": true,
  "agentId": "a89ea087990aa2200",
  "requestId": "req_011CbCmRpGBohgpzcHQH7jEp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9d0c74a5-2019-4f05-9546-af47a946e1e0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SFSSHuPgouqXXT8Te5Y5WU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1136,
      "cache_read_input_tokens": 9404,
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

_source line 9 · 2026-05-19T23:06:47.869Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WXPH7dPR9wZ3R5TDa3jp6D`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.04277",
  "prompt": "Extract the full title, all authors, abstract, and any details about the method, results, benchmarks, and limitations from this paper page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d0c74a5-2019-4f05-9546-af47a946e1e0",
  "isSidechain": true,
  "agentId": "a89ea087990aa2200",
  "requestId": "req_011CbCmRpGBohgpzcHQH7jEp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1a569338-6513-4eb9-b1e9-0eada6664bfc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SFSSHuPgouqXXT8Te5Y5WU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1136,
      "cache_read_input_tokens": 9404,
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

_source line 10 · 2026-05-19T23:06:48.731Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YKv7dVH4QpZaERAXFBijXC`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.03042",
  "prompt": "Extract the full title, all authors, abstract, and any details about the method, results, benchmarks, and limitations from this paper page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a569338-6513-4eb9-b1e9-0eada6664bfc",
  "isSidechain": true,
  "agentId": "a89ea087990aa2200",
  "requestId": "req_011CbCmRpGBohgpzcHQH7jEp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cc335b90-e5f4-4f0b-969b-543dfc3621b4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SFSSHuPgouqXXT8Te5Y5WU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1136,
      "cache_read_input_tokens": 9404,
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

_source line 11 · 2026-05-19T23:06:48.737Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NA6RK6d1qeptPPGBxGvJT5`</summary>

```json
{
  "query": "weight interpolation base model post-trained calibration alignment trade-off 2510.17426"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc335b90-e5f4-4f0b-969b-543dfc3621b4",
  "isSidechain": true,
  "agentId": "a89ea087990aa2200",
  "requestId": "req_011CbCmRpGBohgpzcHQH7jEp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f97548b-b89e-494b-ac06-aacc52a6e475",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SFSSHuPgouqXXT8Te5Y5WU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1136,
      "cache_read_input_tokens": 9404,
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

_source line 12 · 2026-05-19T23:06:49.124Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Nxx4Cm4okVC1UxBVt2Le1Q`</summary>

```json
{
  "query": "Dual-Align confidence drift calibration LLM 2601.04277"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f97548b-b89e-494b-ac06-aacc52a6e475",
  "isSidechain": true,
  "agentId": "a89ea087990aa2200",
  "requestId": "req_011CbCmRpGBohgpzcHQH7jEp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bba55e02-4be8-4f2e-a58f-4e721bd6ac7c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SFSSHuPgouqXXT8Te5Y5WU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1136,
      "cache_read_input_tokens": 9404,
      "output_tokens": 416,
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
          "output_tokens": 416,
          "cache_read_input_tokens": 9404,
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

_source line 13 · 2026-05-19T23:06:52.831Z_

<details><summary>↩ Tool result · `toolu_01WXPH7dPR9wZ3R5TDa3jp6D`</summary>

```text
# Paper Summary: Dual-Alignment Calibrator for Post-Trained LLMs

## Title
"Unlocking the Pre-Trained Model as a Dual-Alignment Calibrator for Post-Trained LLMs"

## Authors
- Beier Luo
- Cheng Wang
- Hongxin Wei
- Sharon Li
- Xuefeng Du

## Abstract
The paper addresses a critical issue: while post-training enhances LLM performance, it degrades confidence calibration, causing systematic overconfidence. The authors identify two distinct error sources: "confidence drift" (inflated final confidence despite consistent intermediate decisions) and "process drift" (divergent inference pathways). They propose Dual-Align, an unsupervised post-hoc framework combining confidence alignment and process alignment strategies to correct both drift types.

## Key Method Details
The approach uses a single temperature parameter to realign model confidence without sacrificing post-training gains. Process alignment specifically identifies the layer where inference trajectories diverge and stabilizes subsequent computation.

## Results & Performance
Experiments demonstrate consistent improvements over existing baselines, reducing calibration errors while approaching performance levels of supervised oracles.

## Limitations
The abstract notes the framework addresses unsupervised calibration, suggesting potential constraints in supervised settings or scenarios requiring labeled data for validation.

**Submission Date:** January 7, 2026
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1a569338-6513-4eb9-b1e9-0eada6664bfc",
  "isSidechain": true,
  "promptId": "8c21e000-65bc-4fe4-b616-175d69471633",
  "agentId": "a89ea087990aa2200",
  "type": "user",
  "uuid": "f7ca7d11-e93b-445b-b9a0-db43fc5d717a",
  "sourceToolAssistantUUID": "1a569338-6513-4eb9-b1e9-0eada6664bfc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T23:06:53.069Z_

<details><summary>↩ Tool result · `toolu_01ALehQvVPkxnoa36hvZxqgc`</summary>

```text
# Paper Summary: Alignment-Calibration Trade-off via Model Merging

## Title
"Navigating the Alignment-Calibration Trade-off: A Pareto-Superior Frontier via Model Merging"

## Authors
- Tiancheng Hu
- Benjamin Minixhofer
- Nigel Collier

## Abstract
The researchers identify a previously underexamined cost of alignment training: "a severe loss of calibration, making models overconfident, less reliable, and model outputs less diverse." They propose that interpolating model weights between pre- and post-alignment versions can navigate this trade-off effectively through a computationally efficient post-hoc intervention.

## Method
The core approach involves simple model merging—blending weights between an unaligned and aligned model to find optimal interpolation points that improve both metrics simultaneously.

## Key Results
The study reveals that this merging process consistently uncovers Pareto-optimal configurations where models demonstrate "improved accuracy beyond both parents while substantially recovering the calibration lost during alignment." This suggests the alignment-calibration tension is not inherently unavoidable.

## Significance
The work demonstrates that straightforward weight interpolation provides an efficient mitigation strategy for what practitioners call the "alignment tax," producing models that achieve better capability and reliability without intensive retraining.

## Field
Computer Science (Computation and Language, Artificial Intelligence, Machine Learning)

**Submission:** October 20, 2025 | **Latest revision:** October 30, 2025
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d0c74a5-2019-4f05-9546-af47a946e1e0",
  "isSidechain": true,
  "promptId": "8c21e000-65bc-4fe4-b616-175d69471633",
  "agentId": "a89ea087990aa2200",
  "type": "user",
  "uuid": "36999602-b901-4ff2-ba28-0be3822ff5b6",
  "sourceToolAssistantUUID": "9d0c74a5-2019-4f05-9546-af47a946e1e0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-19T23:06:53.931Z_

<details><summary>↩ Tool result · `toolu_01YKv7dVH4QpZaERAXFBijXC`</summary>

```text
# BaseCal: Unsupervised Confidence Calibration via Base Model Signals

## Full Title
"BaseCal: Unsupervised Confidence Calibration via Base Model Signals"

## Authors
Hexiang Tan, Wanli Yang, Junwei Zhang, Xin Chen, Rui Tang, Du Su, Jingang Wang, Yuanzhuo Wang, Fei Sun, Xueqi Cheng

## Abstract
The paper addresses overconfidence in post-trained large language models by leveraging their base model counterparts as calibration references. The authors note that "base LLMs often remain well-calibrated" while their fine-tuned versions exhibit severe overconfidence issues.

## Methods

**BaseCal-ReEval:** A straightforward approach that feeds post-trained LLM responses to the base model to obtain confidence scores via average probabilities.

**BaseCal-Proj:** A lightweight projection mechanism that maps final-layer hidden states from post-trained models back to base model representations, then uses the base model's output layer to derive calibrated confidence.

Both methods operate as "an unsupervised, plug-and-play solution" requiring no human annotations or model modifications.

## Results
The approach achieved notable improvements: "reducing Expected Calibration Error (ECE) by an average of 42.90%" compared to comparable unsupervised baselines.

## Benchmarks & Scope
- Five datasets evaluated
- Three LLM families tested

## Publication
Accepted to ACL 2026 Main conference
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc335b90-e5f4-4f0b-969b-543dfc3621b4",
  "isSidechain": true,
  "promptId": "8c21e000-65bc-4fe4-b616-175d69471633",
  "agentId": "a89ea087990aa2200",
  "type": "user",
  "uuid": "1f1fb298-6afa-473d-b57c-f2b6b8178ad7",
  "sourceToolAssistantUUID": "cc335b90-e5f4-4f0b-969b-543dfc3621b4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T23:06:56.666Z_

<details><summary>↩ Tool result · `toolu_01NA6RK6d1qeptPPGBxGvJT5`</summary>

```text
Web search results for query: "weight interpolation base model post-trained calibration alignment trade-off 2510.17426"

Links: [{"title":"[2510.17426] Navigating the Alignment-Calibration Trade-off: A Pareto-Superior Frontier via Model Merging","url":"https://arxiv.org/abs/2510.17426"},{"title":"Navigating the Alignment-Calibration Trade-off: A Pareto-Superior Frontier via Model Merging","url":"https://arxiv.org/pdf/2510.17426"},{"title":"Navigating the Alignment-Calibration Trade-off: A Pareto-Superior Frontier via Model Merging","url":"https://arxiv.org/html/2510.17426"},{"title":"Navigating the Alignment-Calibration Trade-off: A Pareto-Superior","url":"https://www.arxiv.org/pdf/2510.17426"},{"title":"Unlocking the Pre-Trained Model as a Dual-Alignment Calibrator for Post-Trained LLMs","url":"https://arxiv.org/pdf/2601.04277"},{"title":"Gradient-Aligned Calibration for Post-Training Quantization of Diffusion Models","url":"https://arxiv.org/pdf/2602.01289"}]

Based on the search results, I found the paper you're looking for:

**Paper: "Navigating the Alignment-Calibration Trade-off: A Pareto-Superior Frontier via Model Merging"** (arXiv:2510.17426)

**Authors:** Tiancheng Hu, Benjamin Minixhofer, and Nigel Collier (University of Cambridge)

**Key Findings:**

The "alignment tax" of post-training involves not just a drop in task accuracy but also a severe loss of calibration, making models overconfident, less reliable, and model outputs less diverse.

The paper shows that this trade-off can be navigated effectively via a simple post-hoc intervention: interpolating between a model's weights before and after alignment. The process consistently reveals Pareto-optimal interpolations—models that improve accuracy beyond both parents while substantially recovering the calibration lost during alignment.

The work demonstrates that simple model merging provides a computationally efficient method for mitigating the full scope of the alignment tax, yielding models that are more capable and more reliable.

The paper was published in October 2025 and uses model families like Gemma-3 and Qwen2.5 for their experimental analysis.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f97548b-b89e-494b-ac06-aacc52a6e475",
  "isSidechain": true,
  "promptId": "8c21e000-65bc-4fe4-b616-175d69471633",
  "agentId": "a89ea087990aa2200",
  "type": "user",
  "uuid": "9a903802-4b31-419e-8996-5ab2f655bf8b",
  "sourceToolAssistantUUID": "2f97548b-b89e-494b-ac06-aacc52a6e475",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-19T23:06:57.365Z_

<details><summary>↩ Tool result · `toolu_01Nxx4Cm4okVC1UxBVt2Le1Q`</summary>

```text
Web search results for query: "Dual-Align confidence drift calibration LLM 2601.04277"

Links: [{"title":"[2601.04277] Unlocking the Pre-Trained Model as a Dual-Alignment Calibrator for Post-Trained LLMs","url":"https://arxiv.org/abs/2601.04277"},{"title":"Unlocking the Pre-Trained Model as a Dual-Alignment Calibrator for Post-Trained LLMs","url":"https://arxiv.org/pdf/2601.04277"},{"title":"Unlocking the Pre-Trained Model as a Dual-Alignment Calibrator for Post-Trained LLMs","url":"https://arxiv.org/html/2601.04277"},{"title":"Unlocking the Pre-Trained Model as a Dual-Alignment ...","url":"https://www.arxiv.org/pdf/2601.04277"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/pdf/2505.21772"}]

Based on the search results, here's what I found about arXiv paper 2601.04277:

**Paper Title:** Unlocking the Pre-Trained Model as a Dual-Alignment Calibrator for Post-Trained LLMs

**Problem:** Post-training improves large language models (LLMs) but often worsens confidence calibration, leading to systematic overconfidence.

**Key Insight:** Calibration errors arise from two regimes: (i) confidence drift, where final confidence inflates despite largely consistent intermediate decision processes, and (ii) process drift, where intermediate inference pathways diverge.

**Proposed Solution:** Dual-Align is an unsupervised post-hoc framework for dual alignment in confidence calibration that performs confidence alignment to correct confidence drift via final-distribution matching, and introduces process alignment to address process drift by locating the layer where trajectories diverge and realigning the stability of subsequent inference.

**Results:** This dual strategy learns a single temperature parameter that corrects both drift types without sacrificing post-training performance gains, with experiments showing consistent improvements over baselines and reducing calibration errors.

The paper was published on January 7, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bba55e02-4be8-4f2e-a58f-4e721bd6ac7c",
  "isSidechain": true,
  "promptId": "8c21e000-65bc-4fe4-b616-175d69471633",
  "agentId": "a89ea087990aa2200",
  "type": "user",
  "uuid": "205b5872-d4df-46ed-8c0e-b0e3d9bab373",
  "sourceToolAssistantUUID": "bba55e02-4be8-4f2e-a58f-4e721bd6ac7c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-19T23:07:00.481Z_

Good, I have the abstracts. Now let me fetch the full HTML versions of the two primary papers and the BaseCal paper for deeper technical details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "205b5872-d4df-46ed-8c0e-b0e3d9bab373",
  "isSidechain": true,
  "agentId": "a89ea087990aa2200",
  "requestId": "req_011CbCmSpyda2QAuQCtvU4Xr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e350e07d-8725-453a-b457-b583cc9c3dac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W5rSbrFHtVTA68VC5Jn6ZP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2704,
      "cache_read_input_tokens": 10540,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2704,
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

_source line 19 · 2026-05-19T23:07:03.775Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01N5PwbFTBffUjexQnEyuPQ6`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.17426",
  "prompt": "Extract ALL technical details about the method: 1) How exactly does weight interpolation work? What is the formula? What is the interpolation coefficient alpha? 2) What models are tested (exact model names and sizes)? 3) What benchmarks are used? 4) What are the exact calibration metrics (ECE, MCE, Brier score, etc.)? 5) What are the key numerical results - how much does calibration improve? 6) What are the stated limitations? 7) How do they define and measure the alignment-calibration trade-off? 8) What baselines do they compare against? Report everything in maximum detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e350e07d-8725-453a-b457-b583cc9c3dac",
  "isSidechain": true,
  "agentId": "a89ea087990aa2200",
  "requestId": "req_011CbCmSpyda2QAuQCtvU4Xr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca48ac3e-32aa-4537-966b-21c387e2cfad",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W5rSbrFHtVTA68VC5Jn6ZP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2704,
      "cache_read_input_tokens": 10540,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2704,
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

_source line 20 · 2026-05-19T23:07:05.682Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PaBsSmCJuXC3pFbHBbP9oJ`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.04277",
  "prompt": "Extract ALL technical details: 1) How exactly does Dual-Align work? What is confidence alignment vs process alignment? What are the formulas? 2) How do they identify confidence drift vs process drift? 3) What is the single temperature parameter approach? 4) What models are tested? 5) What benchmarks are used? 6) What are the exact numerical results? 7) What baselines do they compare against? 8) What are the stated limitations? 9) How does it compare to weight interpolation approaches? Report everything in maximum detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca48ac3e-32aa-4537-966b-21c387e2cfad",
  "isSidechain": true,
  "agentId": "a89ea087990aa2200",
  "requestId": "req_011CbCmSpyda2QAuQCtvU4Xr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b407b4ca-d5dc-4ae6-b60c-fd1c903b58ec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W5rSbrFHtVTA68VC5Jn6ZP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2704,
      "cache_read_input_tokens": 10540,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2704,
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

_source line 21 · 2026-05-19T23:07:07.142Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GCAdQ1WHN1GZFbdtxjNcCF`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.03042",
  "prompt": "Extract ALL technical details: 1) How exactly does BaseCal work? What are BaseCal-ReEval and BaseCal-Proj? What are the formulas? 2) What models are tested? 3) What benchmarks are used? 4) What are the exact numerical results for ECE reduction? 5) What baselines do they compare against? 6) What are the stated limitations? Report everything in maximum detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b407b4ca-d5dc-4ae6-b60c-fd1c903b58ec",
  "isSidechain": true,
  "agentId": "a89ea087990aa2200",
  "requestId": "req_011CbCmSpyda2QAuQCtvU4Xr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a4d43489-1f6b-4105-afed-fe307456a6a8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W5rSbrFHtVTA68VC5Jn6ZP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2704,
      "cache_read_input_tokens": 10540,
      "output_tokens": 654,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2704
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 654,
          "cache_read_input_tokens": 10540,
          "cache_creation_input_tokens": 2704,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2704,
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

_source line 22 · 2026-05-19T23:07:07.798Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WSsFjZ2Hqc92CcWiX1xBW2`</summary>

```json
{
  "query": "model merging calibration LLM weight averaging SLERP TIES alignment tax"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4d43489-1f6b-4105-afed-fe307456a6a8",
  "isSidechain": true,
  "agentId": "a89ea087990aa2200",
  "requestId": "req_011CbCmSpyda2QAuQCtvU4Xr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad60dffd-2007-402f-8553-1fb16f249e75",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W5rSbrFHtVTA68VC5Jn6ZP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2704,
      "cache_read_input_tokens": 10540,
      "output_tokens": 654,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2704
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 654,
          "cache_read_input_tokens": 10540,
          "cache_creation_input_tokens": 2704,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2704,
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

_source line 23 · 2026-05-19T23:07:15.478Z_

<details><summary>↩ Tool result · `toolu_01WSsFjZ2Hqc92CcWiX1xBW2`</summary>

```text
Web search results for query: "model merging calibration LLM weight averaging SLERP TIES alignment tax"

Links: [{"title":"Model Merging: Weight Averaging, Task Arithmetic, TIES, and DARE - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/model-merging-weight-averaging-task-arithmetic-ties-dare"},{"title":"Beyond Fine-Tuning: Merging Specialized LLMs Without the Data Burden | by Elahe Aghapour | TDS Archive | Medium","url":"https://medium.com/data-science/beyond-fine-tuning-merging-specialized-llms-without-the-data-burden-1c449c2060c4"},{"title":"Model merging | AI Wiki","url":"https://aiwiki.ai/wiki/model_merging"},{"title":"Supercharging Large Language Models through Model Merging | by J.RAI | TAI Blog","url":"https://blog.tai.com.np/supercharging-large-language-models-through-model-merging-85e080b48b16?gi=67a75ac5dc5b"},{"title":"Papers Explained Review 13: Model Merging | by Ritvik Rastogi | Medium","url":"https://ritvik19.medium.com/papers-explained-review-13-model-merging-d0db49797b90"},{"title":"A Comprehensive Guide on Merging Language Models","url":"https://www.ionio.ai/blog/merge-ai-models-using-mergekit"},{"title":"Merge Large Language Models with mergekit","url":"https://huggingface.co/blog/mlabonne/merge-models"},{"title":"An Introduction to Model Merging for LLMs | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/an-introduction-to-model-merging-for-llms/"},{"title":"Model Merging: A Survey - by Cameron R. Wolfe, Ph.D.","url":"https://cameronrwolfe.substack.com/p/model-merging"},{"title":"An Empirical Survey of Model Merging Algorithms for Social Bias Mitigation","url":"https://arxiv.org/html/2512.02689"}]

I found comprehensive search results about model merging with calibration, weight averaging, SLERP, and TIES techniques for LLMs. Here's what the web search returned:

## Key Concepts Found:

**Model Merging Overview**: Model merging is a family of techniques that combine the weights of multiple models into one. It combines the weights of multiple customized LLMs to increase resource utilization and add value to successful models, reducing experimentation waste and offering a cost-effective alternative to joint training.

**Weight Averaging**: Model Soups proposed the most fundamental merging technique, which adds and averages the weights of fine-tuned models with scaling parameters, yielding consistent performance at low cost.

**SLERP (Spherical Linear Interpolation)**: It merges two sets of model parameters by interpolating along a spherical path instead of a straight line. SLERP performs interpolation along a great circle on the sphere of normalized weight vectors, preserving angular relationships rather than straight (Euclidean) interpolation.

**TIES**: The trim percentage in TIES affects merge quality substantially. TIES-Merging is used to merge models, with methods varying in complexity and effectiveness in addressing issues like Task Interference.

**Alignment Challenges**: Techniques like SLERP and model permutation alignment, which finds permutations of hidden units that improve alignment before merging, are active research areas, addressing the harder case of merging models that were not trained from the same starting point.

The search results didn't specifically mention "alignment tax" calibration methods, though the results cover the core techniques you inquired about.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad60dffd-2007-402f-8553-1fb16f249e75",
  "isSidechain": true,
  "promptId": "8c21e000-65bc-4fe4-b616-175d69471633",
  "agentId": "a89ea087990aa2200",
  "type": "user",
  "uuid": "a25f8e5f-fc31-483e-a724-f615d2d2d808",
  "sourceToolAssistantUUID": "ad60dffd-2007-402f-8553-1fb16f249e75",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T23:07:17.540Z_

<details><summary>↩ Tool result · `toolu_01N5PwbFTBffUjexQnEyuPQ6`</summary>

```text
# Technical Details Extraction

## 1. Weight Interpolation Method

**Formula & Coefficient:**
The paper uses coefficient λ ∈ [0,1] to interpolate between pre-trained (PT) and instruction-tuned (IT) models: "λ=0 recovers the pure PT model and λ=1 yields the pure IT model." Three interpolation techniques are employed:

- **Spherical Linear Interpolation (SLERP)** - primary method
- **Linear Interpolation** - robustness check
- **DARE-TIES** (density 0.9) - alternative validation

All operations performed using MergeKit. Crucially, "this is a post-hoc procedure that requires no additional training or gradient-based optimization."

## 2. Models Tested

**Exact specifications:**
- **Gemma-3 family:** 1B, 4B, 12B, 27B (both PT and IT versions)
- **Qwen2.5 family:** 1.5B, 3B, 7B (both PT and IT versions)

## 3. Benchmarks

Five primary discriminative benchmarks: MMLU-Pro (5-shot), GPQA (0-shot), Big-Bench Hard/BBH (3-shot), MATH Level 5 (4-shot), IFEval (0-shot)

Two generative benchmarks: NoveltyBench (diversity metrics), SimBench (distributional prediction)

## 4. Calibration Metrics

**Primary metric:** Expected Calibration Error (ECE) - "a measure of miscalibration where higher values are worse"

The paper focuses predominantly on ECE. Mean prediction confidence is also analyzed to explain calibration degradation mechanisms.

## 5. Key Numerical Results

**Calibration improvements:**
- ECE values increase "by an order of magnitude" after instruction tuning (example: Gemma-3-12B shows 0.024 PT vs. 0.533 IT on MMLU-Pro)
- Merged models recover "a substantial portion of the calibration lost"
- Accuracy gains reach "up to >4 percentage points" for larger models (12B, 27B)
- Optimal λ* converges toward 0.4-0.5 for knowledge tasks at larger scales

**Confidence inflation:** Mean prediction confidence surges from ~40% to >90% on GPQA without commensurate accuracy improvement.

## 6. Stated Limitations

Three key constraints acknowledged:

1. **Weight access requirement:** "A key prerequisite...is full access to the model weights. Consequently, our findings are most directly relevant to the open-source ecosystem."

2. **Method simplicity:** Authors didn't perform exhaustive hyperparameter searches for complex merging methods or explore hierarchical layer-specific merging.

3. **Safety concerns:** "Merging...inherently re-introduces weights from a model that has not undergone full safety fine-tuning. This process could potentially dilute...safety guardrails."

## 7. Alignment-Calibration Trade-off Definition

The paper frames the "alignment tax" as twofold: degraded task accuracy AND "a severe loss of calibration, making models overconfident, less reliable, and model outputs less diverse."

The fundamental observation: instruction tuning induces "mode collapse leading to overconfident, low-diversity outputs" while harming the "model's ability to represent uncertainty."

## 8. Baselines & Comparisons

**Baselines:** Direct comparison against unmerged PT and IT endpoints (λ=0 and λ=1).

**Key finding:** Merged models "Pareto-dominate the instruction-tuned parent, simultaneously achieving high accuracy while partially restoring calibration" - superior to both parents on both dimensions simultaneously, not a simple trade-off continuation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca48ac3e-32aa-4537-966b-21c387e2cfad",
  "isSidechain": true,
  "promptId": "8c21e000-65bc-4fe4-b616-175d69471633",
  "agentId": "a89ea087990aa2200",
  "type": "user",
  "uuid": "74a5afbb-9cbb-4046-bcb3-a7b3f653585a",
  "sourceToolAssistantUUID": "ca48ac3e-32aa-4537-966b-21c387e2cfad",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-19T23:07:18.301Z_

<details><summary>↩ Tool result · `toolu_01GCAdQ1WHN1GZFbdtxjNcCF`</summary>

```text
# BaseCal: Technical Details Summary

## Core Methods

**BaseCal-ReEval**: Feeds a post-trained LLM's (PoLLM's) generated response into its base LLM counterpart to extract confidence scores. The base LLM assigns probabilities to each token, which are then averaged: "c_b(x,y^p) = 1/T ∑ P_ℳ_b(y_t^p|x,y_<t^p)"

**BaseCal-Proj**: A lightweight alternative using a learned projection. It maps PoLLM's final-layer hidden states to base LLM representations via: "φ_θ(h_t-1^p) = W·h_t-1^p + b" trained with MSE loss, then passes projected states through the base output layer for confidence estimation.

## Models Tested

Three model families with multiple sizes:
- Qwen2.5 (7B, 14B, 32B, 72B instruct variants)
- Llama3.1 (8B instruct)
- OLMo2 (7B with SFT/DPO/Instruct checkpoints)

## Benchmarks

Five datasets evaluated:
- **Free-form QA**: TriviaQA, Natural Questions, SQuAD, WebQuestions
- **Multiple-choice**: MMLU (57 subjects)

Training utilized 10,000 questions per dataset; validation used 2,000.

## Numerical Results (ECE Reduction)

- BaseCal-ReEval: 55.65% average ECE reduction versus Vanilla baseline
- BaseCal-Proj: 49.78% average ECE reduction versus Vanilla
- Compared to best unsupervised methods: "42.90% average reduction" for ReEval; 35.32% for Proj

Specific example (Llama3.1-8B on TriviaQA): Vanilla ECE 0.1725 → Proj 0.0387 → ReEval 0.0309

## Baseline Comparisons

Six unsupervised baselines:
1. **Vanilla**: Aggregated token probabilities
2. **P(true)**: Model self-assessment prompting
3. **Verbalization**: Natural language confidence expression
4. **Semantic Entropy**: Multi-sample consistency measurement
5. **DACA**: Probability-level temperature scaling (Luo et al., 2025)
6. **Temperature Scaling** (supervised): Post-hoc rescaling baseline

BaseCal-Proj achieved best performance in "29 out of 30 experimental settings" (5 datasets × 3 models × 2 metrics).

## Stated Limitations

- "Focuses on providing practical calibration without theoretical analysis of underlying mechanisms"
- Limited to "mainstream factual QA tasks," excluding long-form generation and complex reasoning
- Requires "access to base LLM's output layer," incompatible with "closed-source API-based models"
- Evaluation uses LLM-as-judge rather than exclusive human annotation

## Key Findings

The core insight: base LLMs remain well-calibrated despite post-training degradation. "A simple linear projection is already sufficient to effectively recover calibration" with negligible inference overhead compared to ReEval's additional forward pass.

Human validation confirmed "1% disagreement rate" with manual annotation of 100 test instances.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4d43489-1f6b-4105-afed-fe307456a6a8",
  "isSidechain": true,
  "promptId": "8c21e000-65bc-4fe4-b616-175d69471633",
  "agentId": "a89ea087990aa2200",
  "type": "user",
  "uuid": "3027f371-b198-4535-a27b-976515650b41",
  "sourceToolAssistantUUID": "a4d43489-1f6b-4105-afed-fe307456a6a8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T23:07:28.555Z_

<details><summary>↩ Tool result · `toolu_01PaBsSmCJuXC3pFbHBbP9oJ`</summary>

````text
# Dual-Align: Technical Framework for LLM Calibration

## 1. Core Methodology

**Dual-Align** addresses post-training miscalibration through two complementary mechanisms:

### Confidence Alignment
Matches final-layer output distributions between post-trained and pre-trained models using KL divergence:
- Formula: `ℒConf(τ;x) = D_KL(p_g^L(x) || p_f^L(x,τ))`
- Corrects surface-level overconfidence where intermediate processes remain consistent
- Applies temperature scaling: `p(y=j|x,τ) = softmax(z_j^L(x)/τ)`

### Process Alignment
Addresses deeper inference divergence by:
1. **Identifying Peak Divergence Layer (PDL)**: `l*(x) = arg max_l (d^l(x) - d^(l-1)(x))` using Jensen-Shannon Divergence
2. **Computing Inferential Stability Entropy (ISE)**: `ISE(x) = -∑_{l=l*}^L q^l(x)log q^l(x)` where `q^l(x) = exp(v^l(x))/∑_j exp(v^j(x))`
3. **Aligning stability**: `ℒProcess(τ;x) = (ISE_f(x,τ) - ISE_g(x))^2`

### Unified Objective
Dynamically interpolates both losses per-sample:
```
ℒDual(τ;x) = (1 - ΔD_JS^l*(x)) · ℒConf(τ;x) + ΔD_JS^l*(x) · ℒProcess(τ;x)
```
Weight coefficient `ΔD_JS^l*(x)` measures divergence magnitude at PDL.

## 2. Identifying Drift Types

**Confidence Drift Detection:**
- Analyzed via layer-wise Jensen-Shannon Divergence between models
- Agreement samples show minimal differences across early layers
- Final confidence inflates despite consistent intermediate decisions

**Process Drift Detection:**
- Disagreement samples exhibit sharp JSD spike at specific intermediate layer
- PDL represents bifurcation point where inference pathways diverge
- Different downstream predictions despite similar early-layer processing

Figure 2 visualization shows: agreed samples remain near-zero divergence throughout; disagreed samples display dramatic spike at PDL.

## 3. Temperature Parameter Approach

Single learnable parameter `τ*` optimized via:
- Minimizing expected loss: `E_x∈D[ℒDual-Align(τ;x)]` over unlabeled dataset
- Learns optimal scaling through Adam optimizer (learning rate 0.05, 300 epochs)
- Applied only at inference to final-layer logits; preserves predictions and post-training gains
- No modification of model parameters or architecture

## 4. Models Evaluated

**Model Families:**
- Llama-3.1: 8B (pre-trained and instruct versions)
- Qwen-2.5: 7B, 14B, 32B variants with instruct versions
- Gemma-3: 27B with both pre-trained and instruction-tuned versions

## 5. Benchmarks

**Primary Datasets:**
- MMLU: Massive multitask language understanding
- MedMCQA: Medical domain multiple-choice questions
- TruthfulQA: Open-ended generation tasks (via p(true) framework)

**Data Split:** 30% for calibration training, 70% for testing

**Metrics:**
- Expected Calibration Error (ECE)
- Maximum Calibration Error (MCE)
- Adaptive Calibration Error (ACE)
- Brier Score

## 6. Quantitative Results (Main Findings)

**MMLU Performance (Table 1):**

| Model | Method | ECE (%) | MCE (%) |
|-------|--------|---------|---------|
| Llama-3.1-8B | Vanilla | 10.81 | 18.60 |
| | DACA | 7.81 | 13.82 |
| | **Dual-Align** | **2.87** | **5.59** |
| | TS Oracle | 1.53 | 4.79 |
| Qwen2.5-14B | Vanilla | 23.84 | 58.23 |
| | DACA | 5.15 | 8.87 |
| | **Dual-Align** | **2.42** | **11.24** |
| | TS Oracle | 2.30 | 11.41 |
| Gemma-3-27B | Vanilla | 23.84 | 58.23 |
| | DACA | 16.84 | 35.21 |
| | **Dual-Align** | **5.25** | **18.07** |
| | TS Oracle | 5.23 | 18.07 |

**Improvement Over DACA:** >50% ECE reduction across all tested models

**Model Size Scaling (Qwen2.5):**
- 7B: Dual-Align 9.41% vs DACA 10.31%
- 14B: Dual-Align 2.42% vs DACA 5.15%
- 32B: Dual-Align 9.20% vs DACA 10.96%

## 7. Baseline Comparisons

**Unsupervised Methods:**
- **DACA**: Aligns confidence on agreement samples only (data-inefficient)
- **Internal Consistency (IC)**: Hidden-state layer consistency ratios
- **CAPE**: Prompt reordering for bias mitigation
- **Elicitation**: Verbalized confidence prompting

**Supervised Oracle:**
- **Temperature Scaling (TS)**: Requires labeled validation data

**Ablation Results (Table 3):**
- Conf Only: 10.27% ECE (worse than DACA's 7.81%)
- Process Only: 6.08% ECE (substantial improvement)
- Simple Stratify: 5.55% ECE (separate handling of agreement/disagreement)
- **Full Dual-Align: 2.87% ECE** (best unsupervised)

**Layer Selection Ablation (Table 4):**
- Fixed L/4: 4.72% ECE
- Fixed L/2: 4.86% ECE
- Fixed 3L/4: 2.85% ECE
- **Dynamic PDL: 2.38% ECE** (optimal)

## 8. Stated Limitations

Explicitly acknowledged constraints:

1. **Pre-trained Model Dependency**: "Performs post-hoc confidence calibration by learning temperature conditioned on predictions of a pretrained LLM"

2. **Scope Limitation**: Method requires access to both pre-trained and post-trained versions; cannot operate with arbitrary reference models

3. **Primary Focus**: Designed for multiple-choice question answering; open-ended extension requires reformulation using p(true) framework

4. **Trust Risk**: Improved calibration may increase unwarranted user confidence in incorrect outputs

## 9. Weight Interpolation Design

**Novel Aspect:** Dynamic per-sample weighting rather than static strategy

**Comparison to Simple Stratification:**
- Simple approach: `if agree then ℒConf else ℒProcess`
- Dual-Align: Continuous weighting using `ΔD_JS^l*(x)` ∈ [0,1]
- Advantage: Captures gradient of divergence severity, not binary classification

**Why This Matters:**
Samples exist on spectrum between pure confidence drift (low divergence) and pure process drift (high divergence). Weight coefficient naturally captures this continuum, enabling finer calibration adaptation than discrete categorization.

**Theoretical Justification (Proposition 1):**
Bounded ISE mismatch controls calibration error: `ℰ_f(τ) ≤ E_x[w(x)(ISE_f(x,τ) - ISE_g(x))^2] + C_g`
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b407b4ca-d5dc-4ae6-b60c-fd1c903b58ec",
  "isSidechain": true,
  "promptId": "8c21e000-65bc-4fe4-b616-175d69471633",
  "agentId": "a89ea087990aa2200",
  "type": "user",
  "uuid": "155bf422-be4a-4261-9fa0-22542f9ed6e9",
  "sourceToolAssistantUUID": "b407b4ca-d5dc-4ae6-b60c-fd1c903b58ec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-19T23:07:32.072Z_

Now let me get additional details on specific aspects I need to fill in -- the exact Pareto frontier results from the weight interpolation paper, and any comparison between these approaches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "155bf422-be4a-4261-9fa0-22542f9ed6e9",
  "isSidechain": true,
  "agentId": "a89ea087990aa2200",
  "requestId": "req_011CbCmV8JyULZdFGTwhteDv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ac42555-748f-4e97-a14e-3f26cc9f46bc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JuDdJYYcBNKamNLbZFpnva",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1791,
      "cache_creation_input_tokens": 3586,
      "cache_read_input_tokens": 13244,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3586,
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

_source line 28 · 2026-05-19T23:07:35.982Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PgkiL7dKoEgLNkTHDq856R`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.17426",
  "prompt": "Focus on extracting: 1) The exact ECE numbers for each model at different lambda values, especially the optimal lambda. 2) The accuracy numbers at optimal lambda vs pure IT model. 3) The Pareto frontier -- what exact points are on it? 4) The diversity metrics from NovelityBench and SimBench. 5) Any analysis of WHY merging works mechanistically -- do they discuss what happens at the representation level? 6) The confidence inflation numbers -- mean confidence vs actual accuracy. 7) Any comparison to temperature scaling or other calibration baselines. 8) Scaling behavior across model sizes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ac42555-748f-4e97-a14e-3f26cc9f46bc",
  "isSidechain": true,
  "agentId": "a89ea087990aa2200",
  "requestId": "req_011CbCmV8JyULZdFGTwhteDv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25327def-cd06-4d1a-8e05-45b50b0d8e7e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JuDdJYYcBNKamNLbZFpnva",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1791,
      "cache_creation_input_tokens": 3586,
      "cache_read_input_tokens": 13244,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3586,
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

_source line 29 · 2026-05-19T23:07:39.604Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YEQYUybF6iKm5yHrnKVDU5`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.04277",
  "prompt": "Focus on extracting: 1) The exact layer-wise analysis -- what happens at each layer? What does the JSD look like layer by layer? 2) The MedMCQA and TruthfulQA results specifically. 3) How does Dual-Align compare to simple weight interpolation / model merging? Do they discuss Hu et al. 2025? 4) What is the computational cost? 5) The p(true) framework for open-ended generation -- how does it work? 6) Any mechanistic insights about WHY post-training damages calibration at the representation level. 7) The exact PDL identification process and what layers typically become the PDL."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25327def-cd06-4d1a-8e05-45b50b0d8e7e",
  "isSidechain": true,
  "agentId": "a89ea087990aa2200",
  "requestId": "req_011CbCmV8JyULZdFGTwhteDv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff7ffb37-b606-43ba-b84d-adf1673c5e7c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JuDdJYYcBNKamNLbZFpnva",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1791,
      "cache_creation_input_tokens": 3586,
      "cache_read_input_tokens": 13244,
      "output_tokens": 471,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3586
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1791,
          "output_tokens": 471,
          "cache_read_input_tokens": 13244,
          "cache_creation_input_tokens": 3586,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3586,
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

_source line 30 · 2026-05-19T23:07:47.472Z_

<details><summary>↩ Tool result · `toolu_01PgkiL7dKoEgLNkTHDq856R`</summary>

```text
# Alignment-Calibration Trade-off via Model Merging: Key Findings

## 1) ECE Numbers and Optimal Lambda

The paper provides extensive calibration data across models. For **Gemma-3-12B on MMLU-Pro**:
- Base PT: ECE = 0.024
- Base IT: ECE = 0.533
- Optimal merge (λ=0.4, SLERP): ECE = 0.219, Accuracy = 44.25%

The "sweet spot" interpolations consistently reduce miscalibration by roughly 50-60% compared to instruction-tuned versions while maintaining competitive accuracy.

## 2) Accuracy at Optimal Lambda vs Pure IT

For Gemma-3-12B SLERP merges on multiple benchmarks:
- **MMLU-Pro**: Optimal (λ=0.4) achieves 44.25% vs IT's 39.82% (+4.43 points)
- **BBH**: Optimal (λ=0.4) achieves 61.08% vs IT's 63.27% (slight tradeoff)
- **GPQA**: Optimal (λ=0.4) achieves 35.32% vs IT's 33.64% (+1.68 points)

Larger models show stronger Pareto improvements.

## 3) Pareto Frontier Analysis

The authors don't explicitly enumerate frontier points but show that "interpolated models (solid lines) strictly dominate the naïve linear interpolation between base and instruct models." The frontier emerges naturally—not every λ value lies on it, but optimal merges consistently achieve higher accuracy AND better calibration than the instruction-tuned parent.

## 4) Diversity Metrics

**NoveltyBench** (generative diversity):
- The optimal merged model resolved the "trade-off between the over-confident IT model's low diversity (mode collapse) and the PT model's diffuse outputs"

**SimBench** (behavioral prediction):
- Optimal merge scored 20.4 vs PT's 7.7 and IT's 18.2—demonstrating meaningful improvements in distributional prediction tasks

## 5) Mechanistic Analysis

The paper identifies a root cause: **confidence inflation**. On GPQA, instruction-tuned models show "mean prediction confidence surges from around 40% to over 90%." This dramatic overconfidence—without accuracy improvement—directly drives miscalibration. However, the authors don't analyze representation-level changes or probe why merging reverses this effect.

## 6) Confidence Inflation Data

For **Gemma-3 models on GPQA**:
- Base models: ~40% mean confidence
- Instruction-tuned models: >90% mean confidence

This inflation occurs despite minimal accuracy changes, indicating that alignment induces systematic overconfidence rather than genuine capability gains.

## 7) Calibration Baselines

The paper does **not** compare against temperature scaling, post-hoc calibration methods, or other established baselines. The focus is exclusively on merging as the intervention. This represents a significant limitation—temperature scaling alone might achieve similar calibration improvements.

## 8) Scaling Behavior

Clear scaling trends emerge from Gemma-3 family analysis:
- **Peak accuracy gains** from merging over IT increase with scale (marginal for 1B, >4 points for 12B/27B models)
- **Optimal λ* convergence**: Converges toward 0.4-0.5 for larger models, becoming more predictable
- **Landscape smoothness**: Larger models show concave performance curves, making λ selection robust; smaller models exhibit volatility

The authors note that "merging becomes more effective and robust at scale," with the 27B model showing the most pronounced Pareto improvements.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25327def-cd06-4d1a-8e05-45b50b0d8e7e",
  "isSidechain": true,
  "promptId": "8c21e000-65bc-4fe4-b616-175d69471633",
  "agentId": "a89ea087990aa2200",
  "type": "user",
  "uuid": "4457cb76-f2f9-4fa8-aa98-2f4f12f05210",
  "sourceToolAssistantUUID": "25327def-cd06-4d1a-8e05-45b50b0d8e7e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-19T23:07:51.810Z_

<details><summary>↩ Tool result · `toolu_01YEQYUybF6iKm5yHrnKVDU5`</summary>

```text
# Analysis of Dual-Align Paper

## 1) Layer-wise Analysis & JSD Behavior

The paper examines predictive distribution divergence across transformer layers using Jensen-Shannon Divergence (JSD). Key findings:

- **Early layers**: JSD remains "negligible" between PLM and PoLM regardless of final agreement
- **Agreement samples**: Minimal divergence throughout all layers (indicating confidence drift)
- **Disagreement samples**: Sharp JSD spike at a specific intermediate layer termed the Peak Divergence Layer (PDL)

The PDL is formally defined as the layer maximizing the JSD increase: "l∗(x) = argmax_{l∈{2,...,L}} (d^l(x) - d^{l-1}(x))"

Figure 2 visualizes this pattern on Llama-3.1-8B with MMLU, showing disagreed samples display "a sharp spike at an intermediate layer."

## 2) MedMCQA and TruthfulQA Results

**MedMCQA** (Appendix D, Table 6): Dual-Align substantially outperforms baselines across tested models, though specific results are referenced but full table not provided in excerpt.

**TruthfulQA** (open-ended generation via p(true) framework):
- Llama-3.1-8B: Dual-Align reduces both ECE and MCE compared to DACA
- Qwen2.5-14B: Consistent improvements demonstrated
- The paper notes this "successfully adapts to open-ended generation, outperforming the strong DACA baseline"

## 3) Comparison to Model Merging/Interpolation

The paper does **not discuss** simple weight interpolation or model merging approaches. No reference to "Hu et al. 2025" appears in the provided content. The method focuses specifically on temperature scaling through dual alignment objectives rather than parameter-level model combination.

## 4) Computational Cost

The paper provides **minimal computational analysis**. Key statement: "During inference, we apply the learned τ* to calibrate PoLMs in their final outputs, which does not require additional computational cost or access to PLMs."

This suggests inference overhead is negligible (single temperature parameter application), but training costs for optimization aren't detailed.

## 5) The p(true) Framework for Open-Ended Tasks

The method enables open-ended generation via reformulation: "the model generates a free-form answer and then self-evaluates it, enabling calibration without modifying the core method."

This leverages the p(true) approach from Kadavath et al. (2022), where models assess answer correctness probabilistically, converting open-ended problems into evaluable confidence tasks without structural method changes.

## 6) Mechanistic Insights on Post-Training Damage

The paper identifies two damage mechanisms rather than deep representational analysis:

- **Confidence drift**: "intermediate decision process of the PoLM remains consistent...but the output confidence level is inflated"
- **Process drift**: "divergence between the prediction distributions...following the PDL"

Figure 3 reveals post-training creates "abnormally low ISE values" coupled with extreme confidence—described as "overly rigid decision-making processes." The mechanistic cause remains unexplored; the paper documents the phenomenon rather than explaining underlying representation degradation.

## 7) PDL Identification & Typical Layers

The paper does **not specify typical PDL depths**. Ablation studies (Table 4) compare fixed positions (L/4, L/2, 3L/4) but report only that dynamic PDL selection outperforms these baselines without revealing empirical layer statistics across models.

The PDL is identified per-sample using JSD peaks—inherently dynamic—but aggregate distribution of PDL positions across datasets remains unreported.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff7ffb37-b606-43ba-b84d-adf1673c5e7c",
  "isSidechain": true,
  "promptId": "8c21e000-65bc-4fe4-b616-175d69471633",
  "agentId": "a89ea087990aa2200",
  "type": "user",
  "uuid": "d7e39dc2-3efa-481b-a072-8d67887782fd",
  "sourceToolAssistantUUID": "ff7ffb37-b606-43ba-b84d-adf1673c5e7c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-19T23:07:54.971Z_

Let me search for one more thing -- any direct comparisons between these methods and any discussion of mechanistic/circuit-level calibration approaches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7e39dc2-3efa-481b-a072-8d67887782fd",
  "isSidechain": true,
  "agentId": "a89ea087990aa2200",
  "requestId": "req_011CbCmWqjP5JGTHzHutPcMM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e8829b2-30b8-48c6-9983-243211870492",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013bZwzqQ2dFvedLH9BK8nTk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4070,
      "cache_read_input_tokens": 16830,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4070,
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

_source line 33 · 2026-05-19T23:07:55.460Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013gZ72FgqvMn9zcHxUyBdAi`</summary>

```json
{
  "query": "mechanistic interpretability calibration LLM circuit-level confidence representation probing 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e8829b2-30b8-48c6-9983-243211870492",
  "isSidechain": true,
  "agentId": "a89ea087990aa2200",
  "requestId": "req_011CbCmWqjP5JGTHzHutPcMM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e70bb83-0c2c-4253-9e73-c63080d87c94",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013bZwzqQ2dFvedLH9BK8nTk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4070,
      "cache_read_input_tokens": 16830,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4070,
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

_source line 34 · 2026-05-19T23:07:56.305Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019WuMWB1WQg1Juzk3Dzqp4d`</summary>

```json
{
  "query": "BaseCal base model calibration projection hidden states 2601.03042 ACL 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e70bb83-0c2c-4253-9e73-c63080d87c94",
  "isSidechain": true,
  "agentId": "a89ea087990aa2200",
  "requestId": "req_011CbCmWqjP5JGTHzHutPcMM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2eec814e-a4be-4211-b93b-602288a116c8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013bZwzqQ2dFvedLH9BK8nTk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4070,
      "cache_read_input_tokens": 16830,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4070,
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

### Tool result

_source line 35 · 2026-05-19T23:08:03.273Z_

<details><summary>↩ Tool result · `toolu_019WuMWB1WQg1Juzk3Dzqp4d`</summary>

```text
Web search results for query: "BaseCal base model calibration projection hidden states 2601.03042 ACL 2026"

Links: [{"title":"[2601.03042] BaseCal: Unsupervised Confidence Calibration via Base Model Signals","url":"https://arxiv.org/abs/2601.03042"},{"title":"BaseCal: Unsupervised Confidence Calibration via Base Model Signals","url":"https://arxiv.org/html/2601.03042"},{"title":"[2601.03042v2] BaseCal: Unsupervised Confidence Calibration via Base Model Signals","url":"https://arxiv.org/abs/2601.03042v2"},{"title":"BaseCal: Unsupervised Confidence Calibration via Base Model Signals Hexiang Tan","url":"https://arxiv.org/pdf/2601.03042"},{"title":"BaseCal: Unsupervised Confidence Calibration via Base Model Signals | OpenReview","url":"https://openreview.net/forum?id=QwGdjqq2pp"},{"title":"Xueqi Cheng's research works | University of Chinese Academy of Sciences and other places","url":"https://www.researchgate.net/scientific-contributions/Xueqi-Cheng-13941402"},{"title":"Computer Science","url":"https://www.arxiv.org/list/cs/recent?skip=1106&show=250"}]

I found the paper! Here's information about BaseCal (arXiv:2601.03042):

**Paper Title:** BaseCal: Unsupervised Confidence Calibration via Base Model Signals

**Key Findings:**

Post-trained LLMs (PoLLMs) typically suffer from severe overconfidence, while their corresponding base LLMs often remain well-calibrated. This motivates calibrating PoLLM confidence using the base LLM as a reference.

**Two Approaches Proposed:**

1. BaseCal-ReEval evaluates PoLLM's responses by feeding them into the base LLM to get average probabilities as confidence.

2. BaseCal-Proj trains a lightweight projection to map the final-layer hidden states of PoLLMs back to those of their base LLMs. These projected states are then processed by the base LLM's output layer to derive base-calibrated confidence for PoLLM's responses.

**Results:**

BaseCal is an unsupervised, plug-and-play solution that operates without human labels or LLM modifications, reducing Expected Calibration Error (ECE) by an average of 42.90% compared to the best unsupervised baselines.

The paper was submitted on January 6, 2026, and appears to be under review for ACL 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2eec814e-a4be-4211-b93b-602288a116c8",
  "isSidechain": true,
  "promptId": "8c21e000-65bc-4fe4-b616-175d69471633",
  "agentId": "a89ea087990aa2200",
  "type": "user",
  "uuid": "7d6ca091-9393-4de4-a519-b211c5a9a218",
  "sourceToolAssistantUUID": "2eec814e-a4be-4211-b93b-602288a116c8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T23:08:03.537Z_

<details><summary>↩ Tool result · `toolu_013gZ72FgqvMn9zcHxUyBdAi`</summary>

```text
Web search results for query: "mechanistic interpretability calibration LLM circuit-level confidence representation probing 2025 2026"

Links: [{"title":"How do LLMs Compute Verbal Confidence?","url":"https://arxiv.org/html/2603.17839v1"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/pdf/2505.21772"},{"title":"Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation","url":"https://arxiv.org/pdf/2512.22245"},{"title":"Wired for Overconfidence: A Mechanistic Perspective on Inflated Verbalized Confidence in LLMs","url":"https://arxiv.org/pdf/2604.01457"},{"title":"Internal Mechanisms of LLMs","url":"https://www.emergentmind.com/topics/internal-mechanisms-of-llms"},{"title":"Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs","url":"https://www.medrxiv.org/content/10.1101/2025.09.17.25336018v2.full.pdf"},{"title":"Closing the Confidence-Faithfulness Gap in Large Language Models","url":"https://arxiv.org/pdf/2603.25052"}]

I've found several highly relevant research papers on mechanistic interpretability, calibration, and confidence representation in LLMs. Here are the key findings:

## Recent Research on LLM Confidence and Calibration

**Circuit-level Analysis of Confidence:**

Recent work identifies that a compact set of MLP blocks and attention heads in middle-to-late layers consistently write the confidence-inflation signal, and targeted inference-time interventions on these circuits substantially improve calibration.

**Representation Probing Methods:**

Activation steering, patching, noising, and swap experiments reveal that confidence representations emerge at answer-adjacent positions before appearing at the verbalization site, with attention blocking pinpointing that confidence is gathered from answer tokens, cached at the first post-answer position, then retrieved for output. Linear probing and variance partitioning reveal that these cached representations explain substantial variance in verbal confidence beyond token log-probabilities, suggesting a richer answer-quality evaluation.

**Perturbation-based Calibration:**

CCPS (Calibrating LLM Confidence by Probing Perturbed Representation Stability) analyzes internal representational stability by applying targeted adversarial perturbations to final hidden states and extracting features reflecting the model's response to predict answer correctness.

**Geometric Structure of Confidence:**

Mechanistic interpretability analysis using linear probes and contrastive activation addition steering shows that calibration and verbalized confidence signals are encoded linearly but are orthogonal to one another.

These papers represent cutting-edge research from 2025-2026 on understanding LLM confidence mechanisms at the circuit level.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e70bb83-0c2c-4253-9e73-c63080d87c94",
  "isSidechain": true,
  "promptId": "8c21e000-65bc-4fe4-b616-175d69471633",
  "agentId": "a89ea087990aa2200",
  "type": "user",
  "uuid": "005aa6fa-590a-4adc-8690-e9327d75cd92",
  "sourceToolAssistantUUID": "1e70bb83-0c2c-4253-9e73-c63080d87c94",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-19T23:08:06.153Z_

Let me fetch a couple of the mechanistic interpretability papers to understand the landscape for positioning.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "005aa6fa-590a-4adc-8690-e9327d75cd92",
  "isSidechain": true,
  "agentId": "a89ea087990aa2200",
  "requestId": "req_011CbCmXhre4zsG4aknLTypQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "80fbea36-5ab1-4aca-9d13-a56ccaf90505",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S74YXVnebNLqW8iepjG2v7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 717,
      "cache_creation_input_tokens": 900,
      "cache_read_input_tokens": 20900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 900,
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

_source line 38 · 2026-05-19T23:08:07.567Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QZA3SG2EtiZqwRALd9vvJj`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.01457",
  "prompt": "Extract the full title, authors, abstract, method, and key findings about mechanistic analysis of overconfidence in LLMs. What circuits do they identify? What interventions do they propose?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80fbea36-5ab1-4aca-9d13-a56ccaf90505",
  "isSidechain": true,
  "agentId": "a89ea087990aa2200",
  "requestId": "req_011CbCmXhre4zsG4aknLTypQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a43a666c-8ebe-439a-93b4-64c9af99022d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S74YXVnebNLqW8iepjG2v7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 717,
      "cache_creation_input_tokens": 900,
      "cache_read_input_tokens": 20900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 900,
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

_source line 39 · 2026-05-19T23:08:08.317Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PjHLsRen8o6QnYQjpjLXt5`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.21772",
  "prompt": "Extract the full title, authors, abstract, method, and key findings about probing perturbed representation stability for calibration. How does it work? What results do they achieve?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a43a666c-8ebe-439a-93b4-64c9af99022d",
  "isSidechain": true,
  "agentId": "a89ea087990aa2200",
  "requestId": "req_011CbCmXhre4zsG4aknLTypQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "152ad96a-0c8d-4621-bc14-67f882c77d2a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S74YXVnebNLqW8iepjG2v7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 717,
      "cache_creation_input_tokens": 900,
      "cache_read_input_tokens": 20900,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 900
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 717,
          "output_tokens": 244,
          "cache_read_input_tokens": 20900,
          "cache_creation_input_tokens": 900,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 900,
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

_source line 40 · 2026-05-19T23:08:12.821Z_

<details><summary>↩ Tool result · `toolu_01QZA3SG2EtiZqwRALd9vvJj`</summary>

```text
# Analysis of "Wired for Overconfidence" Paper

**Full Title:** "Wired for Overconfidence: A Mechanistic Perspective on Inflated Verbalized Confidence in LLMs"

**Authors:** Tianyi Zhao, Yinhan He, Wendy Zheng, Yujie Zhang, Chen Chen

## Abstract Summary
The researchers investigate why LLMs produce "confidently wrong" answers rather than expressing uncertainty. They conduct circuit-level analysis to understand this phenomenon across three dimensions: measuring confidence as a differentiable signal, identifying circuits that amplify it, and developing targeted interventions.

## Key Findings

**Circuits Identified:**
The team discovered that "a compact set of MLP blocks and attention heads, concentrated in middle-to-late layers" consistently write the confidence-inflation signal at the final token position. This concentrated locus of overconfidence-related computation suggests the phenomenon stems from specific, identifiable neural structures rather than distributed processes.

**Proposed Interventions:**
The researchers propose "targeted inference-time interventions on these circuits" to improve calibration. By surgically modifying activity in the identified circuits, they demonstrate substantial improvements in how well the model's expressed confidence aligns with actual accuracy.

## Significance
The work reveals that overconfidence in LLMs is mechanistically driven and addressable through targeted techniques, offering a pathway toward more reliable uncertainty signals in language models.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a43a666c-8ebe-439a-93b4-64c9af99022d",
  "isSidechain": true,
  "promptId": "8c21e000-65bc-4fe4-b616-175d69471633",
  "agentId": "a89ea087990aa2200",
  "type": "user",
  "uuid": "64d598b3-2e57-4359-af1c-e05d60445d2d",
  "sourceToolAssistantUUID": "a43a666c-8ebe-439a-93b4-64c9af99022d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-19T23:08:13.992Z_

<details><summary>↩ Tool result · `toolu_01PjHLsRen8o6QnYQjpjLXt5`</summary>

```text
# CCPS: Calibrating LLM Confidence Through Representation Stability

## Title
"Calibrating LLM Confidence by Probing Perturbed Representation Stability"

## Authors
Reza Khanmohammadi, Erfan Miahi, Mehrsa Mardikoraem, Simerjot Kaur, Ivan Brugere, Charese H. Smiley, Kundan Thind, and Mohammad M. Ghassemi

## How It Works
CCPS addresses LLM confidence miscalibration by examining how model representations respond to intentional disruptions. The method applies targeted adversarial perturbations to the final hidden states, then extracts features describing the model's response characteristics. These features feed into a lightweight classifier tasked with predicting whether answers are correct.

## Key Findings
The approach was tested on models ranging from 8B to 32B parameters (Llama, Qwen, Mistral families) using MMLU benchmarks in multiple formats. Results demonstrate substantial improvements:

- Expected Calibration Error reduced by approximately 55%
- Brier score decreased by 21%
- Accuracy improved by 5 percentage points
- Area Under Precision-Recall Curve increased by 4 percentage points
- Area Under Receiver Operating Characteristic Curve increased by 6 percentage points

These gains surpassed the strongest existing methods, positioning CCPS as an "efficient, broadly applicable" solution for improving LLM trustworthiness through better confidence estimation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "152ad96a-0c8d-4621-bc14-67f882c77d2a",
  "isSidechain": true,
  "promptId": "8c21e000-65bc-4fe4-b616-175d69471633",
  "agentId": "a89ea087990aa2200",
  "type": "user",
  "uuid": "486b2fe3-2b70-44c8-888c-6871d290fc6d",
  "sourceToolAssistantUUID": "152ad96a-0c8d-4621-bc14-67f882c77d2a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-19T23:09:38.527Z_

I now have comprehensive information on all the papers. Here is the detailed research report.

---

## Research Report: Calibration Methods for Post-Trained LLMs

### Paper 1: "Navigating the Alignment-Calibration Trade-off: A Pareto-Superior Frontier via Model Merging" (arXiv 2510.17426, Hu et al., October 2025)

**Authors:** Tiancheng Hu, Benjamin Minixhofer, Nigel Collier (University of Cambridge)

#### 1. Exact Method

The method is straightforward weight interpolation between a pre-trained (PT) and instruction-tuned (IT) model using a coefficient lambda in [0,1]:

- lambda=0 recovers the pure PT model; lambda=1 yields the pure IT model.
- Three interpolation techniques tested: **SLERP** (spherical linear interpolation, primary method), **linear interpolation**, and **DARE-TIES** (density 0.9).
- All operations performed using MergeKit. No training, no gradient-based optimization -- purely post-hoc.
- The key finding is that an optimal lambda* (typically 0.4-0.5 for larger models on knowledge tasks) yields a model that Pareto-dominates the IT parent on both accuracy and calibration simultaneously.

#### 2. Key Results

**Calibration degradation from alignment is severe:**
- Gemma-3-12B on MMLU-Pro: ECE goes from 0.024 (PT) to 0.533 (IT) -- an order of magnitude increase.
- On GPQA, mean prediction confidence surges from ~40% to >90% after instruction tuning, with minimal accuracy improvement.

**Merging recovers calibration while improving accuracy:**
- Gemma-3-12B SLERP at lambda=0.4: ECE = 0.219 (vs 0.533 IT), Accuracy = 44.25% (vs 39.82% IT, a +4.43 point gain).
- On GPQA: +1.68 points accuracy over IT while substantially reducing overconfidence.
- Larger models (12B, 27B) show strongest Pareto improvements (>4 accuracy points).
- Optimal lambda* converges predictably to 0.4-0.5 at scale.
- SimBench (distributional prediction): merged model scores 20.4 vs PT 7.7, IT 18.2.

**Scaling behavior:** Merging becomes more effective and robust at scale. Larger models show smooth, concave performance curves making lambda selection robust; smaller models exhibit volatility.

#### 3. Benchmarks

- Discriminative: MMLU-Pro (5-shot), GPQA (0-shot), BBH (3-shot), MATH Level 5 (4-shot), IFEval (0-shot)
- Generative: NoveltyBench (diversity), SimBench (distributional prediction)
- Primary metric: ECE

#### 4. Limitations

1. **Requires full weight access** -- only applicable to open-source models.
2. **No comparison to calibration baselines** -- does NOT compare against temperature scaling, Platt scaling, or any other established post-hoc calibration method. This is a critical gap.
3. **Safety concerns** -- merging re-introduces weights from a model without safety fine-tuning, potentially diluting safety guardrails.
4. **No mechanistic understanding** -- documents confidence inflation but does not explain WHY merging reverses it at the representation level.
5. **Coarse-grained** -- single global lambda, no layer-specific or component-specific merging explored.

---

### Paper 2: "Unlocking the Pre-Trained Model as a Dual-Alignment Calibrator for Post-Trained LLMs" (arXiv 2601.04277, Luo et al., January 2026)

**Authors:** Beier Luo, Cheng Wang, Hongxin Wei, Sharon Li, Xuefeng Du

#### 1. Exact Method

Dual-Align is an unsupervised post-hoc framework that learns a single temperature parameter tau* through two complementary alignment objectives:

**Confidence Alignment** (for confidence drift):
- Matches final-layer output distributions via KL divergence: L_Conf(tau; x) = D_KL(p_g^L(x) || p_f^L(x, tau))
- Applies temperature scaling: p(y=j|x, tau) = softmax(z_j^L(x) / tau)
- Targets samples where intermediate processing is consistent but final confidence is inflated.

**Process Alignment** (for process drift):
- Identifies the **Peak Divergence Layer (PDL)**: l*(x) = argmax_l (d^l(x) - d^{l-1}(x)) using Jensen-Shannon Divergence between pre-trained and post-trained model distributions at each layer.
- Computes **Inferential Stability Entropy (ISE)**: ISE(x) = -sum_{l=l*}^{L} q^l(x) log q^l(x), measuring how stable the inference process is from the PDL onward.
- Aligns stability: L_Process(tau; x) = (ISE_f(x, tau) - ISE_g(x))^2
- Targets samples where inference pathways diverge at an intermediate layer.

**Unified objective with dynamic per-sample weighting:**
- L_Dual(tau; x) = (1 - Delta_JSD^{l*}(x)) * L_Conf(tau; x) + Delta_JSD^{l*}(x) * L_Process(tau; x)
- The weight coefficient Delta_JSD^{l*}(x) naturally places samples on a continuum between pure confidence drift and pure process drift.

Optimization: Adam optimizer, lr=0.05, 300 epochs on unlabeled data (30% train, 70% test split). At inference, only applies the learned tau* to final logits -- zero additional cost, no access to PT model needed at inference.

#### 2. Key Results

**MMLU (ECE %)**:
| Model | Vanilla | DACA | Dual-Align | TS Oracle (supervised) |
|---|---|---|---|---|
| Llama-3.1-8B | 10.81 | 7.81 | **2.87** | 1.53 |
| Qwen2.5-14B | 23.84 | 5.15 | **2.42** | 2.30 |
| Gemma-3-27B | 23.84 | 16.84 | **5.25** | 5.23 |

- Consistently >50% ECE reduction over DACA (previous best unsupervised method).
- On Qwen2.5-14B and Gemma-3-27B, Dual-Align essentially matches the supervised temperature scaling oracle.
- Extends to open-ended generation via p(true) framework (model generates answer, then self-evaluates), outperforming DACA on TruthfulQA.

**Ablation results (Llama-3.1-8B, MMLU):**
- Confidence alignment only: 10.27% ECE (worse than DACA)
- Process alignment only: 6.08% ECE
- Simple stratification (if agree then L_Conf else L_Process): 5.55% ECE
- Full Dual-Align with dynamic weighting: 2.87% ECE -- the dynamic weighting is crucial.

**Layer selection ablation:**
- Fixed L/4: 4.72% | Fixed L/2: 4.86% | Fixed 3L/4: 2.85% | Dynamic PDL: 2.38% -- dynamic selection matters.

#### 3. Benchmarks
- MMLU, MedMCQA, TruthfulQA
- Metrics: ECE, MCE, ACE, Brier Score
- Models: Llama-3.1-8B, Qwen2.5-7B/14B/32B, Gemma-3-27B

#### 4. Limitations
1. **Requires access to pre-trained model during training** (though not at inference).
2. **Primarily designed for MCQ** -- open-ended tasks require p(true) reformulation.
3. **Does not compare to weight interpolation approaches** (Hu et al. not cited).
4. **Single global temperature** -- cannot adapt per-sample at inference time; the per-sample analysis only guides the training objective.
5. **No mechanistic explanation** of WHY post-training creates confidence/process drift -- documents the phenomenon via JSD analysis but does not explain root causes.

---

### Paper 3 (Bonus): "BaseCal: Unsupervised Confidence Calibration via Base Model Signals" (arXiv 2601.03042, Tan et al., January 2026, ACL 2026)

**Authors:** Hexiang Tan, Wanli Yang, Junwei Zhang, Xin Chen, Rui Tang, Du Su, Jingang Wang, Yuanzhuo Wang, Fei Sun, Xueqi Cheng

#### 1. Exact Method

**BaseCal-ReEval:** Feeds the post-trained model's response into the base model and takes the average token probability as the confidence score: c_b(x, y^p) = (1/T) * sum P_{M_b}(y_t^p | x, y_{<t}^p). Requires a full additional forward pass through the base model.

**BaseCal-Proj:** Trains a lightweight linear projection W*h + b that maps post-trained model final-layer hidden states to base model hidden states, then passes them through the base model's output layer. Trained with MSE loss on 10K examples per dataset. Negligible inference overhead.

#### 2. Key Results
- BaseCal-ReEval: 55.65% average ECE reduction vs vanilla; 42.90% vs best unsupervised baselines.
- BaseCal-Proj: 49.78% vs vanilla; 35.32% vs best unsupervised baselines.
- Proj achieves best performance in 29/30 experimental settings.
- Example: Llama3.1-8B on TriviaQA: ECE from 0.1725 (vanilla) to 0.0309 (ReEval).

#### 3. Benchmarks
- TriviaQA, Natural Questions, SQuAD, WebQuestions (free-form QA), MMLU (MCQ)
- Models: Qwen2.5 (7B-72B), Llama3.1-8B, OLMo2-7B

#### 4. Limitations
- No theoretical analysis of underlying mechanisms.
- Limited to factual QA; excludes long-form generation and complex reasoning.
- Requires access to base model's output layer -- incompatible with closed-source APIs.
- BaseCal-ReEval requires storing and running two models simultaneously.

---

### Cross-Paper Comparison and Positioning for a Mechanistic Circuit-Level Approach

#### What These Methods Have in Common
All three methods share a core insight: **base/pre-trained models are well-calibrated, and post-training destroys calibration**. They all use the base model as a reference signal. They differ in HOW they use it:

| Method | Approach | Modifies Weights? | Needs Base Model at Inference? | Per-Sample Adaptive? |
|---|---|---|---|---|
| Hu et al. (Weight Interp.) | Global weight merging | Yes (creates new model) | No | No |
| Dual-Align | Temperature scaling with dual objectives | No | No (only during training) | Training-only |
| BaseCal | Confidence re-scoring / projection | No | Yes (ReEval) or partially (Proj) | Yes |

#### How a Mechanistic Circuit-Level Approach Could Improve Upon Them

**Gap 1: None of these methods understand WHY calibration degrades.**
- Hu et al. document confidence inflation but not its mechanism.
- Dual-Align identifies confidence drift vs process drift at the layer level but does not explain what computations change.
- BaseCal explicitly states it provides "practical calibration without theoretical analysis of underlying mechanisms."
- A circuit-level approach (following the direction of Zhao et al. "Wired for Overconfidence", arXiv 2604.01457, which identifies compact MLP blocks and attention heads in middle-to-late layers that write the confidence-inflation signal) could identify the *specific circuits* that post-training modifies and intervene surgically.

**Gap 2: Global vs. targeted intervention.**
- Weight interpolation uses a single global lambda. Dual-Align uses a single global temperature. Neither can target specific failure modes.
- A circuit-level approach could apply targeted interventions only to the identified overconfidence circuits while leaving capability-related circuits intact. This could achieve better Pareto frontiers than global interpolation.

**Gap 3: The confidence and calibration signals appear to be linearly separable in representation space.**
- Recent work (CCPS, arXiv 2505.21772) shows that probing perturbed representations achieves ~55% ECE reduction with 5-point accuracy gains.
- The "Wired for Overconfidence" paper finds that confidence-inflation signals are concentrated in identifiable components.
- This suggests a **surgical activation-editing** approach: identify the direction in representation space corresponding to overconfidence (added by post-training), and subtract it -- akin to contrastive activation addition but specifically targeting the calibration-accuracy orthogonal subspace.

**Gap 4: No method adapts per-instance at the representation level.**
- Dual-Align's per-sample weighting only operates during training; at inference it applies a fixed temperature.
- BaseCal-Proj applies a fixed linear projection.
- A mechanistic approach could detect per-instance whether the model is in a "confidence drift" or "process drift" regime *by examining activations at runtime* and apply different interventions accordingly -- essentially a dynamic, representation-aware calibration.

**Gap 5: The relationship between safety and calibration is unexplored.**
- Hu et al. note that weight merging may dilute safety guardrails.
- A circuit-level approach could disentangle the safety circuits from the calibration circuits, enabling calibration recovery without safety degradation -- a critical advantage for deployment.

**Gap 6: Theoretical grounding.**
- Weight interpolation has no theory for why it works.
- Dual-Align has a proposition bounding calibration error via ISE mismatch but no circuit-level theory.
- A mechanistic approach could provide a causal account: "post-training amplifies activity in circuits X, Y, Z; suppressing them by amount delta provably improves ECE by f(delta)" -- enabling principled, predictable calibration interventions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "486b2fe3-2b70-44c8-888c-6871d290fc6d",
  "isSidechain": true,
  "agentId": "a89ea087990aa2200",
  "requestId": "req_011CbCmYUbStwY7c7LmFSzxx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6e04309e-bd97-4f23-8598-54e9e2a9cd56",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "2bacb8ee-797d-491d-b933-3966ce40bc7f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DPFHrGNveAahvMXzccLcXU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1682,
      "cache_read_input_tokens": 21800,
      "output_tokens": 3585,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1682
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3585,
          "cache_read_input_tokens": 21800,
          "cache_creation_input_tokens": 1682,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1682,
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
