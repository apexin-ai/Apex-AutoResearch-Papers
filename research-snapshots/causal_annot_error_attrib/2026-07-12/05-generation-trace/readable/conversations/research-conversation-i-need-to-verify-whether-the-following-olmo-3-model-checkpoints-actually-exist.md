# Research conversation: I need to verify whether the following OLMo 3 model checkpoints actually exist on HuggingFace: 1. Olmo-3-7B (base) 2. Ol

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a20b342945e200ee4.jsonl`
- **Structured JSON:** [`ffdcb6cf856cf4952423.json`](../../sessions/ff/ffdcb6cf856cf4952423.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

31 recorded events

### User

_source line 1 · 2026-05-19T23:39:01.742Z_

I need to verify whether the following OLMo 3 model checkpoints actually exist on HuggingFace:
1. Olmo-3-7B (base)
2. Olmo-3-7B-Instruct-SFT (SFT-only)
3. Olmo-3-7B-Instruct-DPO (SFT+DPO)
4. Olmo-3-7B-Instruct (full instruct, SFT+DPO+RLVR)
5. Olmo-3-7B-RL-Zero-General (GRPO from base without SFT)

Also check if there are other RL-Zero variants like -Code, -Math, -Mix, -IF.

Use web search to verify these exist on HuggingFace. Search for "site:huggingface.co OLMo-3-7B" and "OLMo 3 RL-Zero huggingface" and "allenai OLMo 3 checkpoints". Report exactly which models exist and which don't.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "eec20fb0-9336-4e73-a283-089bd6e9bec5",
  "agentId": "a20b342945e200ee4",
  "type": "user",
  "uuid": "43b83b26-4d4e-4e39-982d-feec3a1d3958",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T23:39:01.746Z_

```json
{
  "parentUuid": "43b83b26-4d4e-4e39-982d-feec3a1d3958",
  "isSidechain": true,
  "agentId": "a20b342945e200ee4",
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
  "uuid": "d08975c5-5d07-4372-908b-8bc0e9629396",
  "timestamp": "2026-05-19T23:39:01.746Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-19T23:39:01.747Z_

```json
{
  "parentUuid": "d08975c5-5d07-4372-908b-8bc0e9629396",
  "isSidechain": true,
  "agentId": "a20b342945e200ee4",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "6a12da8e-1734-4483-9db2-116753eee155",
  "timestamp": "2026-05-19T23:39:01.747Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-19T23:39:04.639Z_



I'll search for these OLMo 3 model checkpoints on HuggingFace. Let me load the WebSearch tool first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a12da8e-1734-4483-9db2-116753eee155",
  "isSidechain": true,
  "agentId": "a20b342945e200ee4",
  "requestId": "req_011CbCotgVbtgbp4c6qiFJLD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c09f81c5-32d9-4864-aa3d-73b1c7a84ad6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XPtaxSEpcLuYHJaa3Rj6nr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9369,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9369,
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

_source line 5 · 2026-05-19T23:39:05.199Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JRN9faqY34FGmu8H7nCye9`</summary>

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
  "parentUuid": "c09f81c5-32d9-4864-aa3d-73b1c7a84ad6",
  "isSidechain": true,
  "agentId": "a20b342945e200ee4",
  "requestId": "req_011CbCotgVbtgbp4c6qiFJLD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7530719-ebdf-4681-bfbf-3c7678bb20e7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XPtaxSEpcLuYHJaa3Rj6nr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9369,
      "cache_read_input_tokens": 0,
      "output_tokens": 113,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9369
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 113,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 9369,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9369,
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

_source line 6 · 2026-05-19T23:39:05.205Z_

<details><summary>↩ Tool result · `toolu_01JRN9faqY34FGmu8H7nCye9`</summary>

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
  "parentUuid": "f7530719-ebdf-4681-bfbf-3c7678bb20e7",
  "isSidechain": true,
  "promptId": "eec20fb0-9336-4e73-a283-089bd6e9bec5",
  "agentId": "a20b342945e200ee4",
  "type": "user",
  "uuid": "3a4c5b9c-84e6-45dd-8c16-8a1dd8794358",
  "sourceToolAssistantUUID": "f7530719-ebdf-4681-bfbf-3c7678bb20e7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-19T23:39:08.362Z_



Now let me run multiple searches in parallel to find information about these OLMo 3 checkpoints.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a4c5b9c-84e6-45dd-8c16-8a1dd8794358",
  "isSidechain": true,
  "agentId": "a20b342945e200ee4",
  "requestId": "req_011CbCotwJbGYjXkT7yTVpGd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d134ca6-1507-4d82-8c2e-e7b17278d8d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ACgnpmoHTwnippJ5NHt8nw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1135,
      "cache_read_input_tokens": 9369,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1135,
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

_source line 8 · 2026-05-19T23:39:08.838Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X5FF4d8jzLGHj57LsLmshz`</summary>

```json
{
  "query": "site:huggingface.co OLMo-3-7B allenai",
  "allowed_domains": [
    "huggingface.co"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d134ca6-1507-4d82-8c2e-e7b17278d8d1",
  "isSidechain": true,
  "agentId": "a20b342945e200ee4",
  "requestId": "req_011CbCotwJbGYjXkT7yTVpGd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac95e0b2-334f-45e5-84be-9e9c8c05ac24",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ACgnpmoHTwnippJ5NHt8nw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1135,
      "cache_read_input_tokens": 9369,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1135,
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

_source line 9 · 2026-05-19T23:39:09.313Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UncvDrvmVa9DUz2sE9KoEe`</summary>

```json
{
  "query": "OLMo 3 RL-Zero huggingface allenai",
  "allowed_domains": [
    "huggingface.co"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac95e0b2-334f-45e5-84be-9e9c8c05ac24",
  "isSidechain": true,
  "agentId": "a20b342945e200ee4",
  "requestId": "req_011CbCotwJbGYjXkT7yTVpGd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9e816a7-f10c-4785-b465-e3f390e152f3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ACgnpmoHTwnippJ5NHt8nw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1135,
      "cache_read_input_tokens": 9369,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1135,
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

_source line 10 · 2026-05-19T23:39:09.650Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014Po9RqVWj1rygzUAssKU3z`</summary>

```json
{
  "query": "allenai OLMo 3 checkpoints huggingface models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9e816a7-f10c-4785-b465-e3f390e152f3",
  "isSidechain": true,
  "agentId": "a20b342945e200ee4",
  "requestId": "req_011CbCotwJbGYjXkT7yTVpGd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3f5b9972-1903-40af-ba2f-776a9d864aff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ACgnpmoHTwnippJ5NHt8nw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1135,
      "cache_read_input_tokens": 9369,
      "output_tokens": 251,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1135
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 251,
          "cache_read_input_tokens": 9369,
          "cache_creation_input_tokens": 1135,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1135,
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

_source line 11 · 2026-05-19T23:39:14.250Z_

<details><summary>↩ Tool result · `toolu_01X5FF4d8jzLGHj57LsLmshz`</summary>

```text
Web search results for query: "site:huggingface.co OLMo-3-7B allenai"

Links: [{"title":"allenai/Olmo-3-7B-Think · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-Think"},{"title":"allenai/Olmo-3-7B-RLZero-Mix · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-RLZero-Mix"},{"title":"allenai/Olmo-3-7B-RL-Zero-Math · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-Math"},{"title":"allenai/Olmo-3-7B-RL-Zero-Code · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-Code"},{"title":"allenai/Olmo-3-7B-Instruct · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-Instruct"},{"title":"allenai/Olmo-3-7B-Instruct-DPO · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-Instruct-DPO"},{"title":"allenai/Olmo-3-7B-Instruct-SFT · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-Instruct-SFT"},{"title":"allenai/Olmo-3.1-32B-Think · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3.1-32B-Think"},{"title":"allenai/Olmo-3-7B-Think-DPO · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-Think-DPO"},{"title":"allenai/Olmo-3-32B-Think · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-32B-Think"}]

The search found several Olmo 3 models from Allen AI on Hugging Face. Here are the key results:

The Olmo 3 family includes 7B and 32B models with both Instruct and Think variants. Long chain-of-thought thinking improves reasoning tasks like math and coding.

Several specific Olmo-3-7B variants are available on Hugging Face, including:

1. **Olmo-3-7B-Think** - a thinking/reasoning-focused variant
2. **Olmo-3-7B-Instruct** - an instruction-tuned variant
3. **Olmo-3-7B-Instruct-SFT** - instruction-tuned with Supervised Fine-Tuning
4. **Olmo-3-7B-Instruct-DPO** - instruction-tuned with Direct Preference Optimization
5. **Olmo-3-7B-Think-DPO** - thinking variant with DPO
6. **Olmo-3-7B-RL-Zero-Code** - specialized for coding with reinforcement learning
7. **Olmo-3-7B-RL-Zero-Math** - specialized for math with reinforcement learning
8. **Olmo-3-7B-RLZero-Mix** - mixed domain reinforcement learning variant

These models are pre-trained on the Dolma 3 dataset and post-trained on the Dolci datasets. The models are licensed under Apache 2.0 and intended for research and educational use in accordance with Ai2's Responsible Use Guidelines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac95e0b2-334f-45e5-84be-9e9c8c05ac24",
  "isSidechain": true,
  "promptId": "eec20fb0-9336-4e73-a283-089bd6e9bec5",
  "agentId": "a20b342945e200ee4",
  "type": "user",
  "uuid": "f9c37258-7bbd-45d4-96b5-a60c51d1763a",
  "sourceToolAssistantUUID": "ac95e0b2-334f-45e5-84be-9e9c8c05ac24",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T23:39:14.358Z_

<details><summary>↩ Tool result · `toolu_01UncvDrvmVa9DUz2sE9KoEe`</summary>

```text
Web search results for query: "OLMo 3 RL-Zero huggingface allenai"

Links: [{"title":"allenai/Olmo-3-7B-RL-Zero-General · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-General"},{"title":"allenai/Olmo-3-7B-RLZero-Mix · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-RLZero-Mix"},{"title":"allenai/Olmo-3-7B-RL-Zero-Code · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-Code"},{"title":"allenai/Olmo-3-7B-RL-Zero-Mix · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-Mix"},{"title":"allenai/Olmo-3-7B-RL-Zero-IF · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-IF"},{"title":"allenai/Olmo-3-7B-RL-Zero-Math · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-Math"},{"title":"allenai/Olmo-3.1-7B-RL-Zero-Code · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3.1-7B-RL-Zero-Code"}]

Based on the search results, I found information about OLMo 3 RL-Zero models from Allen AI on Hugging Face:

The RL-Zero family of models is an experimental set of model for the scientific exploration of RLVR training. These are available through the Allen AI organization on Hugging Face under various specialized variants:

- **General**: Models trained with reinforcement learning from verifiable rewards on the Dolci-RL-Zero-General-7B dataset which consists of general chat queries, where reward is derived from a LM-judge.

- **Code**: Models trained with reinforcement learning from verifiable rewards on the Dolci-RL-Zero-Code-7B dataset which consists of coding queries.

- **Math**: Models trained with reinforcement learning from verifiable rewards on the Dolci-RL-Zero-Math-7B dataset which consists of math queries.

- **Mixed**: Models trained with reinforcement learning from verifiable rewards on the Dolci-RL-Zero-Mix-7B dataset which consists of math, coding, and instruction-following queries.

- **Instruction-Following**: Models trained with reinforcement learning from verifiable rewards on the Dolci-RL-Zero-IF-7B dataset which consists of instruction-following queries.

All these models are available on Hugging Face under the Allen AI organization and can be loaded using the standard transformers library.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9e816a7-f10c-4785-b465-e3f390e152f3",
  "isSidechain": true,
  "promptId": "eec20fb0-9336-4e73-a283-089bd6e9bec5",
  "agentId": "a20b342945e200ee4",
  "type": "user",
  "uuid": "56dc0aab-e408-41b7-8da6-ac971336b65f",
  "sourceToolAssistantUUID": "d9e816a7-f10c-4785-b465-e3f390e152f3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T23:39:16.305Z_

<details><summary>↩ Tool result · `toolu_014Po9RqVWj1rygzUAssKU3z`</summary>

```text
Web search results for query: "allenai OLMo 3 checkpoints huggingface models"

Links: [{"title":"allenai/Olmo-3-1125-32B · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-1125-32B"},{"title":"allenai/Olmo-3-7B-Instruct · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-Instruct"},{"title":"allenai/Olmo-3.1-32B-Instruct · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3.1-32B-Instruct"},{"title":"allenai/Olmo-3-7B-Think · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-Think"},{"title":"allenai/Olmo-3-32B-Think · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-32B-Think"},{"title":"allenai/Olmo-3.1-32B-Think · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3.1-32B-Think"},{"title":"Olmo 3: Charting a path through the model flow to lead open-source AI | Ai2","url":"https://allenai.org/blog/olmo3"},{"title":"allenai/Olmo-3-1025-7B · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-1025-7B"},{"title":"allenai/Olmo-3-7B-RL-Zero-Mix · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-Mix"},{"title":"Olmo 3: America’s truly open reasoning models","url":"https://www.interconnects.ai/p/olmo-3-americas-truly-open-reasoning"}]

Based on the search results, here's what I found about Allen AI OLMo 3 checkpoints on Hugging Face:

## Available Models and Checkpoints

Allen AI has released checkpoints for OLMo 3 models, with naming conventions: stage1-stepXXX for pretraining, stage2-ingredientY-stepXXX for midtraining, and stage3-stepXXX for long context.

## Core Models Available

The main OLMo 3 models available on Hugging Face include:

- **OLMo-3-1125-32B** - A 32B base model
- **OLMo-3-7B-Instruct** - A 7B instruction-tuned model
- **OLMo-3-7B-Think** - A 7B reasoning model
- **OLMo-3-32B-Think** - A 32B reasoning model
- **OLMo-3.1-32B-Instruct** - An instruction-tuned model described as the strongest fully open 32B-scale instruct model
- **OLMo-3.1-32B-Think** - Extended reinforcement learning checkpoint representing improved reasoning capabilities

## Accessing Specific Checkpoints

To load a specific model revision with HuggingFace, simply add the revision argument, and you can access all revisions via the list_repo_refs function.

## General Release Information

Allen AI is releasing all code, checkpoints, and associated training details, and the models are licensed under Apache 2.0. You can find all artifacts at the [Allen AI OLMo 3 Hugging Face collection](https://huggingface.co/collections/allenai/olmo-3).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f5b9972-1903-40af-ba2f-776a9d864aff",
  "isSidechain": true,
  "promptId": "eec20fb0-9336-4e73-a283-089bd6e9bec5",
  "agentId": "a20b342945e200ee4",
  "type": "user",
  "uuid": "0667d87c-9c0c-4071-bc91-67fbe2c03b8d",
  "sourceToolAssistantUUID": "3f5b9972-1903-40af-ba2f-776a9d864aff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-19T23:39:19.022Z_

Now let me search specifically for the base model `Olmo-3-7B` (without any suffix) to confirm it exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0667d87c-9c0c-4071-bc91-67fbe2c03b8d",
  "isSidechain": true,
  "agentId": "a20b342945e200ee4",
  "requestId": "req_011CbCoukkN861jpjJ9Jf4yJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a6a5057-4096-470c-8233-4db55b547a4d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDjEWZkfaTeFZ4AgemmVpz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3072,
      "cache_read_input_tokens": 10504,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3072,
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

_source line 15 · 2026-05-19T23:39:20.014Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AtRrhLZd68uRej6MNXV41x`</summary>

```json
{
  "query": "site:huggingface.co \"allenai/Olmo-3-7B\"",
  "allowed_domains": [
    "huggingface.co"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a6a5057-4096-470c-8233-4db55b547a4d",
  "isSidechain": true,
  "agentId": "a20b342945e200ee4",
  "requestId": "req_011CbCoukkN861jpjJ9Jf4yJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9945e25-8eb0-474e-91b3-bd04aed2b351",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDjEWZkfaTeFZ4AgemmVpz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3072,
      "cache_read_input_tokens": 10504,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3072,
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

_source line 16 · 2026-05-19T23:39:20.901Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0124JbCmGXmRcX6ygZrDK8C3`</summary>

```json
{
  "url": "https://huggingface.co/allenai/Olmo-3-7B",
  "prompt": "Does this model page exist? What is the model name and description? Or does it show a 404 / not found error?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9945e25-8eb0-474e-91b3-bd04aed2b351",
  "isSidechain": true,
  "agentId": "a20b342945e200ee4",
  "requestId": "req_011CbCoukkN861jpjJ9Jf4yJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fc3183a7-a464-4564-bd95-37a7d9f9a4d8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDjEWZkfaTeFZ4AgemmVpz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3072,
      "cache_read_input_tokens": 10504,
      "output_tokens": 228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3072
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 228,
          "cache_read_input_tokens": 10504,
          "cache_creation_input_tokens": 3072,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3072,
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

_source line 17 · 2026-05-19T23:39:21.291Z_

<details><summary>↩ Tool result · `toolu_0124JbCmGXmRcX6ygZrDK8C3`</summary>

```text
The server returned HTTP 401 Unauthorized.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc3183a7-a464-4564-bd95-37a7d9f9a4d8",
  "isSidechain": true,
  "promptId": "eec20fb0-9336-4e73-a283-089bd6e9bec5",
  "agentId": "a20b342945e200ee4",
  "type": "user",
  "uuid": "b174535a-0dd3-4464-8226-d6983db9e1ee",
  "sourceToolAssistantUUID": "fc3183a7-a464-4564-bd95-37a7d9f9a4d8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T23:39:24.890Z_

<details><summary>↩ Tool result · `toolu_01AtRrhLZd68uRej6MNXV41x`</summary>

```text
Web search results for query: "site:huggingface.co "allenai/Olmo-3-7B""

Links: [{"title":"allenai/Olmo-3-7B-Instruct · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-Instruct"},{"title":"allenai/Olmo-3-1125-32B · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-1125-32B"},{"title":"Olmo 3 - a allenai Collection","url":"https://huggingface.co/collections/allenai/olmo-3"},{"title":"allenai/Olmo-3-7B-Think · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-Think"},{"title":"allenai/Olmo-3-32B-Think · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-32B-Think"},{"title":"allenai/Olmo-3-7B-RL-Zero-Math · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-Math"},{"title":"allenai/Olmo-3-1025-7B · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-1025-7B"},{"title":"allenai/Olmo-3-7B-RL-Zero-Mix · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-Mix"},{"title":"allenai/Olmo-3-7B-Think-SFT · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-Think-SFT"},{"title":"allenai/Olmo-3-7B-RL-Zero-Code · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-Code"}]

Based on the web search results, I found information about the Olmo 3 models from Allen AI on Hugging Face. While the search didn't return a specific page for "allenai/Olmo-3-7B" exactly, it did return several related Olmo 3 7B model variants:

## Olmo 3 7B Model Family

Olmo 3 is a new family of 7B and 32B models with both Instruct and Think variants. Olmo is a series of Open language models designed to enable the science of language models, pre-trained on the Dolma 3 dataset and post-trained on the Dolci datasets.

The available 7B variants include:
- **Olmo-3-7B-Instruct** - An instruction-tuned variant
- **Olmo-3-7B-Think** - A variant optimized for reasoning tasks
- **Olmo-3-7B-Think-SFT** - A supervised fine-tuned variant of the Think model
- Various RL-Zero experimental variants for scientific exploration

## Key Features

Long chain-of-thought thinking improves reasoning tasks like math and coding. All code, checkpoints, logs (coming soon), and associated training details are being released.

Olmo 3 is supported in transformers 4.57.0 or higher.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9945e25-8eb0-474e-91b3-bd04aed2b351",
  "isSidechain": true,
  "promptId": "eec20fb0-9336-4e73-a283-089bd6e9bec5",
  "agentId": "a20b342945e200ee4",
  "type": "user",
  "uuid": "dd6ed7a2-0532-43d8-a280-0ff9ad5bb014",
  "sourceToolAssistantUUID": "d9945e25-8eb0-474e-91b3-bd04aed2b351",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-19T23:39:27.599Z_

Let me try fetching the collection page and also check for the base model with a different approach.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd6ed7a2-0532-43d8-a280-0ff9ad5bb014",
  "isSidechain": true,
  "agentId": "a20b342945e200ee4",
  "requestId": "req_011CbCovPSyxqG1utGc6TqQz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "28d8d1b2-c45e-4ae2-bbb6-7a4c324708b5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bvp2RcehJpvEsuWNxJxYKr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 1151,
      "cache_read_input_tokens": 13576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1151,
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

_source line 20 · 2026-05-19T23:39:30.441Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LnSJsMmGTLQFXxeU2CBd7b`</summary>

```json
{
  "url": "https://huggingface.co/collections/allenai/olmo-3",
  "prompt": "List ALL model names/IDs in this OLMo 3 collection. I need to know every model listed here, especially: Is there a plain \"Olmo-3-7B\" base model (no suffix like Instruct, Think, etc.)? Also list all RL-Zero variants."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28d8d1b2-c45e-4ae2-bbb6-7a4c324708b5",
  "isSidechain": true,
  "agentId": "a20b342945e200ee4",
  "requestId": "req_011CbCovPSyxqG1utGc6TqQz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34f1c9dd-dc6a-47d0-838c-d798a4b24eb5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bvp2RcehJpvEsuWNxJxYKr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 1151,
      "cache_read_input_tokens": 13576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1151,
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

_source line 21 · 2026-05-19T23:39:30.518Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B8f7SQiaZQaHCQvbLe4esg`</summary>

```json
{
  "query": "huggingface.co allenai Olmo-3-1025-7B base model pretrained",
  "allowed_domains": [
    "huggingface.co"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34f1c9dd-dc6a-47d0-838c-d798a4b24eb5",
  "isSidechain": true,
  "agentId": "a20b342945e200ee4",
  "requestId": "req_011CbCovPSyxqG1utGc6TqQz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3bbca7ab-c993-4414-9e54-602afb8ed0cc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bvp2RcehJpvEsuWNxJxYKr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 1151,
      "cache_read_input_tokens": 13576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1151,
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

_source line 22 · 2026-05-19T23:39:34.590Z_

<details><summary>↩ Tool result · `toolu_01LnSJsMmGTLQFXxeU2CBd7b`</summary>

```text
# OLMo 3 Collection - Complete Model List

Based on the webpage content provided, here are ALL the models listed in the OLMo 3 collection:

## Explicitly Listed Models

1. **allenai/Olmo-3-1125-32B** - Base version (32B)
2. **allenai/Olmo-3-32B-Think** - Think version (32B, for reasoning)
3. **allenai/Olmo-3-1025-7B** - Base version (7B)
4. **allenai/Olmo-3-7B-Think** - Think version (7B, for reasoning)
5. **allenai/Olmo-3-7B-Instruct** - Instruct version (7B, for chat)

## Collections Referenced
- Olmo 3 Pre-training (10 items)
- Olmo 3 Post-training (32 items)

## Answer to Your Specific Questions

❌ **NO plain "Olmo-3-7B" base model** - The base 7B model is named **Olmo-3-1025-7B**, not a plain variant.

❌ **NO RL-Zero variants** are listed in the provided content.

---

**Note:** The webpage shows this is just a summary view of the collection. The full details of all 10 pre-training and 32 post-training artifacts are in the referenced sub-collections, but their specific names are not displayed on this page excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34f1c9dd-dc6a-47d0-838c-d798a4b24eb5",
  "isSidechain": true,
  "promptId": "eec20fb0-9336-4e73-a283-089bd6e9bec5",
  "agentId": "a20b342945e200ee4",
  "type": "user",
  "uuid": "61e1db51-e3a5-455b-ac19-87a7dbf74232",
  "sourceToolAssistantUUID": "34f1c9dd-dc6a-47d0-838c-d798a4b24eb5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-19T23:39:36.416Z_

<details><summary>↩ Tool result · `toolu_01B8f7SQiaZQaHCQvbLe4esg`</summary>

```text
Web search results for query: "huggingface.co allenai Olmo-3-1025-7B base model pretrained"

Links: [{"title":"allenai/Olmo-3-1025-7B · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-1025-7B"},{"title":"Mungert/Olmo-3-1025-7B-GGUF · Hugging Face","url":"https://huggingface.co/Mungert/Olmo-3-1025-7B-GGUF"},{"title":"allenai/Olmo-3-1125-32B · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-1125-32B"},{"title":"allenai/OLMo-7B-Instruct · Hugging Face","url":"https://huggingface.co/allenai/OLMo-7B-Instruct"},{"title":"allenai/Olmo-3-7B-Instruct · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-Instruct"},{"title":"allenai/Olmo-3-7B-Think · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-Think"},{"title":"allenai/Olmo-Hybrid-7B · Hugging Face","url":"https://huggingface.co/allenai/Olmo-Hybrid-7B"}]

Based on the search results, here's what I found about the allenai/Olmo-3-1025-7B base model on Hugging Face:

## Model Overview

Olmo 3 is a new family of 7B and 32B models that includes Base, Instruct, and Think variants. The Base models were trained using a staged training approach.

## Training Details

Olmo is a series of Open language models designed to enable the science of language models, and these models are trained on the Dolma 3 dataset. 

The primary dataset is dolma3_6T-mix-1025 with 5.93T tokens and 97.53%+ coverage of the total pretraining budget. The dataset mix consists of 20% code, 28% web pages, 19% math, 14% QA, 8% thinking, 6% instruction, and 5% PDFs.

## Model Access

All code, checkpoints, and associated training details are being released. Olmo 3 is supported in transformers v4.57.0 or higher.

You can access the full model card and additional information directly at: https://huggingface.co/allenai/Olmo-3-1025-7B


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3bbca7ab-c993-4414-9e54-602afb8ed0cc",
  "isSidechain": true,
  "promptId": "eec20fb0-9336-4e73-a283-089bd6e9bec5",
  "agentId": "a20b342945e200ee4",
  "type": "user",
  "uuid": "5daa0415-b285-45b8-9789-fc18aac6347a",
  "sourceToolAssistantUUID": "3bbca7ab-c993-4414-9e54-602afb8ed0cc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-19T23:39:40.969Z_

Now let me check the post-training collection to get the full list, and also verify the RL-Zero variants.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5daa0415-b285-45b8-9789-fc18aac6347a",
  "isSidechain": true,
  "agentId": "a20b342945e200ee4",
  "requestId": "req_011CbCowGKPZtEREeD9nVMTJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1581a21d-51f9-461a-9182-86343808b475",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013e7KDhYkARvPvUwZU2Uipx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1468,
      "cache_read_input_tokens": 14727,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1468,
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

_source line 25 · 2026-05-19T23:39:41.909Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TgLRZkJrXgvdQZhPavcbRy`</summary>

```json
{
  "query": "site:huggingface.co/collections/allenai \"olmo-3\" post-training",
  "allowed_domains": [
    "huggingface.co"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1581a21d-51f9-461a-9182-86343808b475",
  "isSidechain": true,
  "agentId": "a20b342945e200ee4",
  "requestId": "req_011CbCowGKPZtEREeD9nVMTJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bb5db937-9eca-49c6-b432-13b253d1301b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013e7KDhYkARvPvUwZU2Uipx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1468,
      "cache_read_input_tokens": 14727,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1468,
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

_source line 26 · 2026-05-19T23:39:42.446Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Dw6o4btmWeNXEfbkdHZFu9`</summary>

```json
{
  "query": "site:huggingface.co allenai Olmo-3-7B-RL-Zero-IF",
  "allowed_domains": [
    "huggingface.co"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb5db937-9eca-49c6-b432-13b253d1301b",
  "isSidechain": true,
  "agentId": "a20b342945e200ee4",
  "requestId": "req_011CbCowGKPZtEREeD9nVMTJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ebd1d74-87be-4bd2-a21b-8e5c69db5592",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013e7KDhYkARvPvUwZU2Uipx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1468,
      "cache_read_input_tokens": 14727,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1468,
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

_source line 27 · 2026-05-19T23:39:43.218Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K5WShmGcaot5TcDnsKSGPL`</summary>

```json
{
  "query": "site:huggingface.co allenai \"Olmo-3-7B-RLZero\" OR \"Olmo-3-7B-RL-Zero\"",
  "allowed_domains": [
    "huggingface.co"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ebd1d74-87be-4bd2-a21b-8e5c69db5592",
  "isSidechain": true,
  "agentId": "a20b342945e200ee4",
  "requestId": "req_011CbCowGKPZtEREeD9nVMTJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f28b1380-3401-42e9-88c0-9a9daa62bb0b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013e7KDhYkARvPvUwZU2Uipx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1468,
      "cache_read_input_tokens": 14727,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1468,
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

_source line 28 · 2026-05-19T23:39:47.568Z_

<details><summary>↩ Tool result · `toolu_01Dw6o4btmWeNXEfbkdHZFu9`</summary>

```text
Web search results for query: "site:huggingface.co allenai Olmo-3-7B-RL-Zero-IF"

Links: [{"title":"allenai/Olmo-3-7B-RL-Zero-IF · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-IF"},{"title":"README.md · allenai/Olmo-3-7B-RL-Zero-IF at main","url":"https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-IF/blob/main/README.md"},{"title":"allenai/Olmo-3-7B-RL-Zero-General · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-General"},{"title":"allenai/Olmo-3-7B-RL-Zero-Mix · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-Mix"},{"title":"allenai/Olmo-3.1-7B-RL-Zero-Code · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3.1-7B-RL-Zero-Code"},{"title":"allenai/Olmo-3-7B-RLZero-Mix · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-RLZero-Mix"},{"title":"allenai/Olmo-3-7B-RL-Zero-Math · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-Math"},{"title":"allenai/Olmo-3-7B-RL-Zero-Code · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-Code"},{"title":"allenai/Dolci-RL-Zero-IF-7B · Datasets at Hugging Face","url":"https://huggingface.co/datasets/allenai/Dolci-RL-Zero-IF-7B"},{"title":"allenai/Olmo-3-7B-RLZero-Math · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-RLZero-Math"}]

I found the model on Hugging Face! Here's information about the **allenai/Olmo-3-7B-RL-Zero-IF** model:

The RL-Zero family of models is an experimental set of model for the scientific exploration of RLVR training. This specific model is part of the OLMo 3 family.

**Key Details:**

- The model was trained through reinforcement learning from verifiable rewards on the Dolci-RL-Zero-IF-7B dataset which consists of instruction-following queries.
- These models are pre-trained on the Dolma 3 dataset and post-trained on the Dolci datasets.
- All code, checkpoints, logs (coming soon), and associated training details are being released.
- The date cutoff is Dec. 2023.

**Important Notes:**
Like any base language model or fine-tuned model without safety filtering, these models can easily be prompted by users to generate harmful and sensitive content, and such content may also be produced unintentionally, especially in cases involving bias.

For technical inquiries, you can contact olmo@allenai.org. The model is available for download from the Hugging Face hub at: https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-IF


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ebd1d74-87be-4bd2-a21b-8e5c69db5592",
  "isSidechain": true,
  "promptId": "eec20fb0-9336-4e73-a283-089bd6e9bec5",
  "agentId": "a20b342945e200ee4",
  "type": "user",
  "uuid": "e0282ac6-8da9-489a-8842-1d660a9e10ae",
  "sourceToolAssistantUUID": "9ebd1d74-87be-4bd2-a21b-8e5c69db5592",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-19T23:39:48.511Z_

<details><summary>↩ Tool result · `toolu_01TgLRZkJrXgvdQZhPavcbRy`</summary>

```text
Web search results for query: "site:huggingface.co/collections/allenai "olmo-3" post-training"

Links: [{"title":"Olmo 3 - a allenai Collection","url":"https://huggingface.co/collections/allenai/olmo-3"},{"title":"allenai/Olmo-3-7B-Think · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-Think"},{"title":"Olmo 3 Post-training - a allenai Collection","url":"https://huggingface.co/collections/allenai/olmo-3-post-training"},{"title":"allenai/Olmo-3-32B-Think · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-32B-Think"},{"title":"allenai/Olmo-3-7B-Instruct · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-Instruct"},{"title":"allenai/Olmo-3-7B-RL-Zero-Math · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-Math"},{"title":"allenai/Olmo-3.1-32B-Instruct · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3.1-32B-Instruct"},{"title":"Olmo 3.1 - a allenai Collection","url":"https://huggingface.co/collections/allenai/olmo-31"},{"title":"allenai/Olmo-3-7B-RL-Zero-Code · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-Code"},{"title":"OLMo Suite - a allenai Collection","url":"https://huggingface.co/collections/allenai/olmo-suite"}]

The search has returned relevant results about OLMo 3 post-training on Hugging Face. Here are the key findings:

All artifacts for post-training Olmo 3 are available in a dedicated collection, with datasets following the model that resulted from training on them.

The OLMo 3 Post-training collection includes various components:

- Base versions of OLMo 3 (both 32B and 7B) are available for use as foundations for post-training.
- Think versions of OLMo 3 are best used for complex reasoning applications.
- Instruct versions are best suited for chat applications.

The post-training approach includes multiple techniques:

- The models are pre-trained on the Dolma 3 dataset and post-trained on the Dolci datasets.
- Post-training uses supervised fine-tuning on datasets consisting of math, code, chat, and general knowledge queries.
- Direct preference optimization and reinforcement learning from verifiable rewards are also applied using domain-specific datasets for math, code, instruction-following, and general chat queries.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb5db937-9eca-49c6-b432-13b253d1301b",
  "isSidechain": true,
  "promptId": "eec20fb0-9336-4e73-a283-089bd6e9bec5",
  "agentId": "a20b342945e200ee4",
  "type": "user",
  "uuid": "cee53689-8a30-44ce-b237-24790d1c3e6f",
  "sourceToolAssistantUUID": "bb5db937-9eca-49c6-b432-13b253d1301b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T23:39:48.758Z_

<details><summary>↩ Tool result · `toolu_01K5WShmGcaot5TcDnsKSGPL`</summary>

```text
Web search results for query: "site:huggingface.co allenai "Olmo-3-7B-RLZero" OR "Olmo-3-7B-RL-Zero""

Links: [{"title":"allenai/Olmo-3-7B-RLZero-Math · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-RLZero-Math"},{"title":"allenai/Olmo-3-7B-RLZero-Mix · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-RLZero-Mix"},{"title":"mradermacher/Olmo-3-7B-RL-Zero-Code-GGUF · Hugging Face","url":"https://huggingface.co/mradermacher/Olmo-3-7B-RL-Zero-Code-GGUF"},{"title":"allenai/Olmo-3-7B-RL-Zero-General · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-General"},{"title":"allenai/Olmo-3-7B-RL-Zero-Math · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-Math"},{"title":"allenai/Olmo-3-7B-RL-Zero-Mix · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-Mix"},{"title":"allenai/Olmo-3-7B-RL-Zero-Code · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-Code"},{"title":"allenai/Olmo-3-7B-RL-Zero-IF · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-IF"}]

The search found several models from Allen AI on Hugging Face matching your query. Here are the results:

## Results Found:

1. **Olmo-3-7B-RLZero-Math** - Allen AI is releasing all code, checkpoints, logs (coming soon), and associated training details

2. **Olmo-3-7B-RLZero-Mix** (updated November 19, 2025)

3. **Olmo-3-7B-RL-Zero-General** - The RL-Zero family of models is an experimental set of model for the scientific exploration of RLVR training (updated December 1, 2025)

4. **Olmo-3-7B-RL-Zero-Math** - The RL-Zero family of models is an experimental set of model for the scientific exploration of RLVR training (updated December 15, 2025)

5. **Olmo-3-7B-RL-Zero-Mix** - part of a new family of 7B and 32B models, trained using reinforcement learning from verifiable rewards on the Dolci-RL-Zero-Mix-7B dataset which consists of math, coding, and instruction-following queries

6. **Olmo-3-7B-RL-Zero-Code** - The RL-Zero family is releasing all code and checkpoints, trained using reinforcement learning from verifiable rewards on the Dolci-RL-Zero-Code-7B dataset which consists of coding queries

7. **Olmo-3-7B-RL-Zero-IF** - The RL-Zero family is releasing all code and checkpoints, trained using reinforcement learning from verifiable rewards on the Dolci-RL-Zero-IF-7B dataset which consists of instruction-following queries


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f28b1380-3401-42e9-88c0-9a9daa62bb0b",
  "isSidechain": true,
  "promptId": "eec20fb0-9336-4e73-a283-089bd6e9bec5",
  "agentId": "a20b342945e200ee4",
  "type": "user",
  "uuid": "403fb191-da4a-4e84-b2e7-6952b2b39482",
  "sourceToolAssistantUUID": "f28b1380-3401-42e9-88c0-9a9daa62bb0b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-19T23:40:11.810Z_

I now have comprehensive information. Let me compile the findings.

Here is the full verification report for OLMo 3 model checkpoints on HuggingFace:

---

## Your 5 Requested Models

**1. Olmo-3-7B (base)** -- DOES NOT EXIST under that exact name. The base 7B model is named **`allenai/Olmo-3-1025-7B`** (the "1025" is a date-based identifier). There is no `allenai/Olmo-3-7B` repo.

**2. Olmo-3-7B-Instruct-SFT (SFT-only)** -- EXISTS at [allenai/Olmo-3-7B-Instruct-SFT](https://huggingface.co/allenai/Olmo-3-7B-Instruct-SFT)

**3. Olmo-3-7B-Instruct-DPO (SFT+DPO)** -- EXISTS at [allenai/Olmo-3-7B-Instruct-DPO](https://huggingface.co/allenai/Olmo-3-7B-Instruct-DPO)

**4. Olmo-3-7B-Instruct (full instruct, SFT+DPO+RLVR)** -- EXISTS at [allenai/Olmo-3-7B-Instruct](https://huggingface.co/allenai/Olmo-3-7B-Instruct)

**5. Olmo-3-7B-RL-Zero-General (GRPO from base without SFT)** -- EXISTS at [allenai/Olmo-3-7B-RL-Zero-General](https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-General)

---

## RL-Zero Variants -- All Exist

The RL-Zero family is described as "an experimental set of models for the scientific exploration of RLVR training." All of the following exist on HuggingFace:

| Variant | URL | Training Data Domain |
|---|---|---|
| **RL-Zero-Code** | [allenai/Olmo-3-7B-RL-Zero-Code](https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-Code) | Coding queries |
| **RL-Zero-Math** | [allenai/Olmo-3-7B-RL-Zero-Math](https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-Math) | Math queries |
| **RL-Zero-Mix** | [allenai/Olmo-3-7B-RL-Zero-Mix](https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-Mix) | Math + coding + instruction-following |
| **RL-Zero-IF** | [allenai/Olmo-3-7B-RL-Zero-IF](https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-IF) | Instruction-following queries |
| **RL-Zero-General** | [allenai/Olmo-3-7B-RL-Zero-General](https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-General) | General chat queries (LM-judge reward) |

Note: There are also older naming variants (`Olmo-3-7B-RLZero-Math`, `Olmo-3-7B-RLZero-Mix` -- without hyphens around "Zero") that appear to be earlier uploads of the same models.

---

## Additional OLMo 3 Models Discovered

Beyond what you asked about, these also exist:
- **`allenai/Olmo-3-7B-Think`** -- reasoning/thinking variant
- **`allenai/Olmo-3-7B-Think-SFT`** -- SFT checkpoint of the Think variant
- **`allenai/Olmo-3-7B-Think-DPO`** -- DPO checkpoint of the Think variant
- **`allenai/Olmo-3-1025-7B`** -- the actual base 7B pretrained model
- **`allenai/Olmo-3-1125-32B`** -- 32B base model
- **`allenai/Olmo-3-32B-Think`** -- 32B Think variant

---

## Summary

4 out of 5 of your requested models exist exactly as named. The one exception is the base model: there is no `Olmo-3-7B` -- the correct name is **`Olmo-3-1025-7B`**. All 5 RL-Zero variants (Code, Math, Mix, IF, General) exist on HuggingFace.

Sources:
- [allenai/Olmo-3-1025-7B](https://huggingface.co/allenai/Olmo-3-1025-7B)
- [allenai/Olmo-3-7B-Instruct](https://huggingface.co/allenai/Olmo-3-7B-Instruct)
- [allenai/Olmo-3-7B-Instruct-SFT](https://huggingface.co/allenai/Olmo-3-7B-Instruct-SFT)
- [allenai/Olmo-3-7B-Instruct-DPO](https://huggingface.co/allenai/Olmo-3-7B-Instruct-DPO)
- [allenai/Olmo-3-7B-RL-Zero-General](https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-General)
- [allenai/Olmo-3-7B-RL-Zero-Code](https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-Code)
- [allenai/Olmo-3-7B-RL-Zero-Math](https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-Math)
- [allenai/Olmo-3-7B-RL-Zero-Mix](https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-Mix)
- [allenai/Olmo-3-7B-RL-Zero-IF](https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-IF)
- [allenai/Olmo-3-7B-Think](https://huggingface.co/allenai/Olmo-3-7B-Think)
- [OLMo 3 Collection](https://huggingface.co/collections/allenai/olmo-3)
- [OLMo 3 Post-training Collection](https://huggingface.co/collections/allenai/olmo-3-post-training)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "403fb191-da4a-4e84-b2e7-6952b2b39482",
  "isSidechain": true,
  "agentId": "a20b342945e200ee4",
  "requestId": "req_011CbCox9V9gQAbyotKgQQF4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b4e4b3b1-cf92-4cd6-b031-50cf302defe4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NEsSLKJU3hYihGmDTmdsQr",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3126,
      "cache_read_input_tokens": 16195,
      "output_tokens": 1817,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3126
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1817,
          "cache_read_input_tokens": 16195,
          "cache_creation_input_tokens": 3126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3126,
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
