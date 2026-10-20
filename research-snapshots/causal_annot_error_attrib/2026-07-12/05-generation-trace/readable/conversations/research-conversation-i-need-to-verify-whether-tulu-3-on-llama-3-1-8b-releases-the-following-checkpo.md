# Research conversation: I need to verify whether Tulu 3 on LLaMA 3.1-8B releases the following checkpoints on HuggingFace: 1. Base LLaMA 3.1-8B 

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a470d481c389b3356.jsonl`
- **Structured JSON:** [`3984ab50d6b5a1c882d3.json`](../../sessions/39/3984ab50d6b5a1c882d3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

24 recorded events

### User

_source line 1 · 2026-05-19T23:40:43.207Z_

I need to verify whether Tulu 3 on LLaMA 3.1-8B releases the following checkpoints on HuggingFace:
1. Base LLaMA 3.1-8B
2. Llama-3.1-Tulu-3-8B-SFT (SFT checkpoint)
3. Llama-3.1-Tulu-3-8B-DPO (DPO checkpoint)  
4. A full "Instruct" variant

Search for:
- "site:huggingface.co Tulu-3 LLaMA 3.1 8B"
- "allenai Tulu 3 LLaMA checkpoints"
- "Tulu 3 post-training checkpoints SFT DPO"

Also verify: does Tulu 3 release intermediate SFT and DPO checkpoints, or only the final model? The proposal claims it releases Base, SFT, DPO, and Instruct checkpoints via Allen AI. Report exactly what exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "eec20fb0-9336-4e73-a283-089bd6e9bec5",
  "agentId": "a470d481c389b3356",
  "type": "user",
  "uuid": "e27ce89c-bd30-4e83-b33a-1cc721fd0497",
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

_source line 2 · 2026-05-19T23:40:43.210Z_

```json
{
  "parentUuid": "e27ce89c-bd30-4e83-b33a-1cc721fd0497",
  "isSidechain": true,
  "agentId": "a470d481c389b3356",
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
  "uuid": "70fb95e1-9e03-45fe-b772-35d687823692",
  "timestamp": "2026-05-19T23:40:43.210Z",
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

_source line 3 · 2026-05-19T23:40:43.211Z_

```json
{
  "parentUuid": "70fb95e1-9e03-45fe-b772-35d687823692",
  "isSidechain": true,
  "agentId": "a470d481c389b3356",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4b073add-97da-4259-ab5c-fafb840c3a54",
  "timestamp": "2026-05-19T23:40:43.211Z",
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

_source line 4 · 2026-05-19T23:40:45.270Z_



I'll search for information about Tulu 3 checkpoints on HuggingFace using multiple queries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b073add-97da-4259-ab5c-fafb840c3a54",
  "isSidechain": true,
  "agentId": "a470d481c389b3356",
  "requestId": "req_011CbCp2AHdmTxnH15iePsN5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0be7801a-28d6-40fa-a4a2-88edf0dc3db3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MEqH1LTqotp1PxmrvevqY3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1586,
      "cache_read_input_tokens": 7773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1586,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 5 · 2026-05-19T23:40:45.758Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RX8X8d9HnAWnGN7FmtA8mK`</summary>

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
  "parentUuid": "0be7801a-28d6-40fa-a4a2-88edf0dc3db3",
  "isSidechain": true,
  "agentId": "a470d481c389b3356",
  "requestId": "req_011CbCp2AHdmTxnH15iePsN5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e24a89c1-1240-4e28-912f-ba7e823e1823",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MEqH1LTqotp1PxmrvevqY3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1586,
      "cache_read_input_tokens": 7773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1586,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 6 · 2026-05-19T23:40:45.762Z_

<details><summary>↩ Tool result · `toolu_01RX8X8d9HnAWnGN7FmtA8mK`</summary>

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
  "parentUuid": "e24a89c1-1240-4e28-912f-ba7e823e1823",
  "isSidechain": true,
  "promptId": "eec20fb0-9336-4e73-a283-089bd6e9bec5",
  "agentId": "a470d481c389b3356",
  "type": "user",
  "uuid": "31e9cbfe-7000-4c23-bcf3-69500819238a",
  "sourceToolAssistantUUID": "e24a89c1-1240-4e28-912f-ba7e823e1823",
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

_source line 7 · 2026-05-19T23:40:48.416Z_



Now let me run multiple searches in parallel to gather comprehensive information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31e9cbfe-7000-4c23-bcf3-69500819238a",
  "isSidechain": true,
  "agentId": "a470d481c389b3356",
  "requestId": "req_011CbCp2MSbqTEr75wTKVoJm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5cb4807b-fe1d-4ae8-9848-fdcbd8c0f3cc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UCiNkMqyU28MqLDfnXbVE1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 9359,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 632,
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

_source line 8 · 2026-05-19T23:40:49.211Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015HgoPtAdtmqRAzfmU6GM2b`</summary>

```json
{
  "query": "site:huggingface.co Tulu-3 LLaMA 3.1 8B"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5cb4807b-fe1d-4ae8-9848-fdcbd8c0f3cc",
  "isSidechain": true,
  "agentId": "a470d481c389b3356",
  "requestId": "req_011CbCp2MSbqTEr75wTKVoJm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c1e73a2-53f6-4d62-bf7f-9639309eebee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UCiNkMqyU28MqLDfnXbVE1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 9359,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 632,
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

_source line 9 · 2026-05-19T23:40:49.430Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BJMqHt3ZBBxCwtTwiw8Rcz`</summary>

```json
{
  "query": "allenai Tulu 3 LLaMA checkpoints huggingface"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c1e73a2-53f6-4d62-bf7f-9639309eebee",
  "isSidechain": true,
  "agentId": "a470d481c389b3356",
  "requestId": "req_011CbCp2MSbqTEr75wTKVoJm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "84deefdd-1ec7-4280-a54b-9157c917d82c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UCiNkMqyU28MqLDfnXbVE1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 9359,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 632,
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

_source line 10 · 2026-05-19T23:40:49.736Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017qgduvkjaPk7LUAHdo1avg`</summary>

```json
{
  "query": "Tulu 3 post-training checkpoints SFT DPO intermediate release"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84deefdd-1ec7-4280-a54b-9157c917d82c",
  "isSidechain": true,
  "agentId": "a470d481c389b3356",
  "requestId": "req_011CbCp2MSbqTEr75wTKVoJm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dd06218c-a12a-41e0-a160-f23376a4c188",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UCiNkMqyU28MqLDfnXbVE1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 9359,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 632
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 197,
          "cache_read_input_tokens": 9359,
          "cache_creation_input_tokens": 632,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 632,
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

_source line 11 · 2026-05-19T23:40:55.044Z_

<details><summary>↩ Tool result · `toolu_015HgoPtAdtmqRAzfmU6GM2b`</summary>

```text
Web search results for query: "site:huggingface.co Tulu-3 LLaMA 3.1 8B"

Links: [{"title":"allenai/Llama-3.1-Tulu-3-8B · Hugging Face","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B"},{"title":"allenai/Llama-3.1-Tulu-3.1-8B · Hugging Face","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3.1-8B"},{"title":"allenai/Llama-3.1-Tulu-3-8B-RM · Hugging Face","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B-RM"},{"title":"allenai/Llama-3.1-Tulu-3-8B-SFT · Hugging Face","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B-SFT"},{"title":"allenai/llama-3.1-tulu-3-8b-preference-mixture · Datasets at Hugging Face","url":"https://huggingface.co/datasets/allenai/llama-3.1-tulu-3-8b-preference-mixture"},{"title":"bartowski/Llama-3.1-Tulu-3-8B-GGUF · Hugging Face","url":"https://huggingface.co/bartowski/Llama-3.1-Tulu-3-8B-GGUF"},{"title":"README.md · allenai/Llama-3.1-Tulu-3.1-8B at 2f0b4fd3822f0c938f02ea199c4a202cadcd8224","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3.1-8B/blob/2f0b4fd3822f0c938f02ea199c4a202cadcd8224/README.md"},{"title":"allenai/Llama-3.1-Tulu-3-8B-DPO · Batch Size","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B-DPO/discussions/4"},{"title":"bartowski/allenai_Llama-3.1-Tulu-3.1-8B-GGUF · Hugging Face","url":"https://huggingface.co/bartowski/allenai_Llama-3.1-Tulu-3.1-8B-GGUF"},{"title":"tensorblock/Llama-3.1-Tulu-3-8B-GGUF · Hugging Face","url":"https://huggingface.co/tensorblock/Llama-3.1-Tulu-3-8B-GGUF"}]

I've successfully performed the web search for "site:huggingface.co Tulu-3 LLaMA 3.1 8B". Here are the key results:

## Main Results:

1. **allenai/Llama-3.1-Tulu-3-8B** - The original Tulu-3 model based on LLaMA 3.1 8B, available at https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B

2. **Llama-3.1-Tulu-3.1-8B** - An improved version 3.1 update where they switched from PPO to GRPO (no reward model) and did further hyperparameter tuning to achieve substantial performance improvements, available at https://huggingface.co/allenai/Llama-3.1-Tulu-3.1-8B

3. **Variant Models:**
   - Llama-3.1-Tulu-3-8B-SFT (Supervised Fine-Tuning variant)
   - Llama-3.1-Tulu-3-8B-RM (Reward Model variant)
   - DPO (Direct Preference Optimization) variant

4. **Quantized Versions:** Several community-created GGUF quantized versions are available from contributors like bartowski and tensorblock.

Tülu3 is a leading instruction following model family, offering fully open-source data, code, and recipes designed to serve as a comprehensive guide for modern post-training techniques.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c1e73a2-53f6-4d62-bf7f-9639309eebee",
  "isSidechain": true,
  "promptId": "eec20fb0-9336-4e73-a283-089bd6e9bec5",
  "agentId": "a470d481c389b3356",
  "type": "user",
  "uuid": "94ab61f8-14fc-4940-914d-05518e6cb6a6",
  "sourceToolAssistantUUID": "3c1e73a2-53f6-4d62-bf7f-9639309eebee",
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

_source line 12 · 2026-05-19T23:40:55.382Z_

<details><summary>↩ Tool result · `toolu_01BJMqHt3ZBBxCwtTwiw8Rcz`</summary>

```text
Web search results for query: "allenai Tulu 3 LLaMA checkpoints huggingface"

Links: [{"title":"allenai/Llama-3.1-Tulu-3-8B · Hugging Face","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B"},{"title":"allenai/Llama-3.1-Tulu-3-8B-RM · Hugging Face","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B-RM"},{"title":"allenai/Llama-3.1-Tulu-3.1-8B · Hugging Face","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3.1-8B"},{"title":"allenai/Llama-3.1-Tulu-3-70B-broken · Hugging Face","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3-70B-broken"},{"title":"allenai/llama-3-tulu-2-8b · Hugging Face","url":"https://huggingface.co/allenai/llama-3-tulu-2-8b"},{"title":"allenai/Llama-3.1-Tulu-3-405B · Hugging Face","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3-405B"},{"title":"allenai/Llama-3.1-Tulu-3-70B-DPO · Hugging Face","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3-70B-DPO"},{"title":"Triangle104/Llama-3.1-Tulu-3-8B-Q8_0-GGUF · Hugging Face","url":"https://huggingface.co/Triangle104/Llama-3.1-Tulu-3-8B-Q8_0-GGUF"},{"title":"allenai/Llama-3.1-Tulu-3-70B-SFT · Hugging Face","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3-70B-SFT"},{"title":"allenai/llama-3.1-tulu-3-70b-preference-mixture · Datasets at Hugging Face","url":"https://huggingface.co/datasets/allenai/llama-3.1-tulu-3-70b-preference-mixture"}]

Based on the search results, here are the key findings about Allen AI's Tulu 3 LLaMA checkpoints on Hugging Face:

## Available Tulu 3 Checkpoints

Tulu 3 includes multiple models released with state-of-the-art open post-training recipes. The main Llama 3.1-based Tulu 3 checkpoints available on Hugging Face include:

**Base Models:**
- allenai/Llama-3.1-Tulu-3-8B
- allenai/Llama-3.1-Tulu-3-405B

**SFT (Supervised Fine-Tuning) Variants:**
- allenai/Llama-3.1-Tulu-3-70B-SFT

**DPO (Direct Preference Optimization) Variants:**
- allenai/Llama-3.1-Tulu-3-70B-DPO

**Reward Models:**
- allenai/Llama-3.1-Tulu-3-8B-RM

**Updated Version:**
- allenai/Llama-3.1-Tulu-3.1-8B

## Model Description

Tülu3 is a leading instruction following model family, offering fully open-source data, code, and recipes designed to serve as a comprehensive guide for modern post-training techniques, and is designed for state-of-the-art performance on a diversity of tasks in addition to chat, such as MATH, GSM8K, and IFEval.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84deefdd-1ec7-4280-a54b-9157c917d82c",
  "isSidechain": true,
  "promptId": "eec20fb0-9336-4e73-a283-089bd6e9bec5",
  "agentId": "a470d481c389b3356",
  "type": "user",
  "uuid": "18dc2d68-10fd-4cba-9c39-506c54e08d87",
  "sourceToolAssistantUUID": "84deefdd-1ec7-4280-a54b-9157c917d82c",
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

_source line 13 · 2026-05-19T23:40:56.399Z_

<details><summary>↩ Tool result · `toolu_017qgduvkjaPk7LUAHdo1avg`</summary>

```text
Web search results for query: "Tulu 3 post-training checkpoints SFT DPO intermediate release"

Links: [{"title":"(PDF) Tulu 3: Pushing Frontiers in Open Language Model Post-Training","url":"https://www.researchgate.net/publication/386093659_TULU_3_Pushing_Frontiers_in_Open_Language_Model_Post-Training"},{"title":"Tülu 3: Pushing Frontiers in Open Language Model Post-Training","url":"https://arxiv.org/html/2411.15124v3"},{"title":"Tülu 3: The next era in open post-training | Ai2","url":"https://allenai.org/blog/tulu-3-technical"},{"title":"Tulu 3: Pushing Frontiers in Open Language Model Post-Training","url":"https://arxiv.org/pdf/2411.15124"},{"title":"Scaling the Tülu 3 post-training recipes to surpass the performance of DeepSeek V3 | Ai2","url":"https://allenai.org/blog/tulu-3-405B"},{"title":"[2411.15124] Tulu 3: Pushing Frontiers in Open Language Model Post-Training","url":"https://arxiv.org/abs/2411.15124"},{"title":"GitHub - allenai/open-instruct: AllenAI's post-training codebase · GitHub","url":"https://github.com/allenai/open-instruct"},{"title":"Papers Explained 283: Tulu V3. TÜLU 3 is a family of fully-open… | by Ritvik Rastogi | Medium","url":"https://ritvik19.medium.com/papers-explained-183-tulu-v3-fc7758b18724"}]

Based on the search results, here's information about Tulu 3 post-training checkpoints:

## Overview
Tülu 3 is a family of fully-open state-of-the-art post-trained models, alongside its data, code, and training recipes, serving as a comprehensive guide for modern post-training techniques.

## Training Stages and Checkpoints
The Tülu 3 training recipe involves multiple stages, with each stage building upon the previous model and focusing on different types of data — namely, prompt-completion instances for supervised finetuning, preferences for preference tuning, or verifiable rewards for reinforcement learning.

Tülu 3 releases all artifacts associated with the training recipe – including SFT, DPO, and RL model checkpoints, along with new SFT and DPO datasets.

## Training Algorithms
The training algorithms include supervised finetuning (SFT), Direct Preference Optimization (DPO), and a novel method called Reinforcement Learning with Verifiable Rewards (RLVR).

## Intermediate Checkpoint Performance
The highest final models were from training with DPO before RLVR. Integrating RLVR as a component of the generalist training pipeline can gain up to 1.7, 3.3, and 1.3 points improvement over the DPO checkpoint on MATH, GSM8K and IFEval.

The Tülu 3 release includes checkpoints for both 8B and 70B model sizes (with 405B following later), with intermediate checkpoints available at the SFT and DPO stages before the final RLVR-trained models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd06218c-a12a-41e0-a160-f23376a4c188",
  "isSidechain": true,
  "promptId": "eec20fb0-9336-4e73-a283-089bd6e9bec5",
  "agentId": "a470d481c389b3356",
  "type": "user",
  "uuid": "ab0b24d4-4af5-4501-a342-8aec68d331f3",
  "sourceToolAssistantUUID": "dd06218c-a12a-41e0-a160-f23376a4c188",
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

_source line 14 · 2026-05-19T23:40:59.908Z_

Let me now verify the specific 8B checkpoints directly and check whether a separate "Instruct" variant exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab0b24d4-4af5-4501-a342-8aec68d331f3",
  "isSidechain": true,
  "agentId": "a470d481c389b3356",
  "requestId": "req_011CbCp38gfxLZYmictjAy3s",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a8b2c78e-98c4-47a7-b584-8bd6798f7318",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cj7VomPWX7r9TidtP2cEXq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3396,
      "cache_read_input_tokens": 9991,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3396,
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

_source line 15 · 2026-05-19T23:41:00.387Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01W5KLM1GhJTNk9XYr4z1rYE`</summary>

```json
{
  "query": "site:huggingface.co allenai/Llama-3.1-Tulu-3-8B-DPO"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8b2c78e-98c4-47a7-b584-8bd6798f7318",
  "isSidechain": true,
  "agentId": "a470d481c389b3356",
  "requestId": "req_011CbCp38gfxLZYmictjAy3s",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "26b25327-2ba2-4fb9-8403-0a38eb0c7f7b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cj7VomPWX7r9TidtP2cEXq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3396,
      "cache_read_input_tokens": 9991,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3396,
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

_source line 16 · 2026-05-19T23:41:00.854Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SuSrX7irGR7XbM1oTbNHnR`</summary>

```json
{
  "query": "site:huggingface.co \"allenai/Llama-3.1-Tulu-3-8B\" instruct"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26b25327-2ba2-4fb9-8403-0a38eb0c7f7b",
  "isSidechain": true,
  "agentId": "a470d481c389b3356",
  "requestId": "req_011CbCp38gfxLZYmictjAy3s",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d6a9cdd8-180f-421d-bafa-e55668a43fa9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cj7VomPWX7r9TidtP2cEXq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3396,
      "cache_read_input_tokens": 9991,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3396,
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

_source line 17 · 2026-05-19T23:41:01.530Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Nkpj3ATbSz8UznkPFDPE9h`</summary>

```json
{
  "query": "Tulu 3 8B all released checkpoints allenai huggingface SFT DPO RL RLVR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6a9cdd8-180f-421d-bafa-e55668a43fa9",
  "isSidechain": true,
  "agentId": "a470d481c389b3356",
  "requestId": "req_011CbCp38gfxLZYmictjAy3s",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f06b03db-1207-4040-a859-b7560d16e3fb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cj7VomPWX7r9TidtP2cEXq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3396,
      "cache_read_input_tokens": 9991,
      "output_tokens": 241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3396
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 241,
          "cache_read_input_tokens": 9991,
          "cache_creation_input_tokens": 3396,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3396,
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

_source line 18 · 2026-05-19T23:41:06.205Z_

<details><summary>↩ Tool result · `toolu_01W5KLM1GhJTNk9XYr4z1rYE`</summary>

```text
Web search results for query: "site:huggingface.co allenai/Llama-3.1-Tulu-3-8B-DPO"

Links: [{"title":"allenai/Llama-3.1-Tulu-3-8B-DPO · Hugging Face","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B-DPO"},{"title":"allenai/Llama-3.1-Tulu-3-8B-DPO-RM-RB2 · Hugging Face","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B-DPO-RM-RB2"},{"title":"allenai/Llama-3.1-Tulu-3-8B · Hugging Face","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B"},{"title":"Update README.md (#1) · allenai/Llama-3.1-Tulu-3-8B-DPO at 0023470","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B-DPO/commit/002347006131d85678ea3865520bc9caad69869a"},{"title":"allenai/Llama-3.1-Tulu-3-8B-DPO · Batch Size","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B-DPO/discussions/4"},{"title":"allenai/llama-3.1-tulu-3-8b-preference-mixture · Datasets at Hugging Face","url":"https://huggingface.co/datasets/allenai/llama-3.1-tulu-3-8b-preference-mixture"},{"title":"README.md · allenai/Llama-3.1-Tulu-3.1-8B at 2f0b4fd3822f0c938f02ea199c4a202cadcd8224","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3.1-8B/blob/2f0b4fd3822f0c938f02ea199c4a202cadcd8224/README.md"},{"title":"allenai/Llama-3.1-Tulu-3-70B-DPO · Hugging Face","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3-70B-DPO"},{"title":"allenai/Llama-3.1-Tulu-3-405B-DPO · Hugging Face","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3-405B-DPO"},{"title":"math-extraction-comp/allenai__Llama-3.1-Tulu-3-8B-DPO · Datasets at Hugging Face","url":"https://huggingface.co/datasets/math-extraction-comp/allenai__Llama-3.1-Tulu-3-8B-DPO/viewer"}]

I've successfully performed the web search for the model `allenai/Llama-3.1-Tulu-3-8B-DPO` on Hugging Face. Here are the key findings:

## Model Overview

The Llama-3.1-Tulu-3-8B-DPO is a helpful and harmless AI Assistant built by the Allen Institute for AI. Tülu3 is a leading instruction following model family, offering fully open-source data, code, and recipes designed to serve as a comprehensive guide for modern post-training techniques.

## Training Details

This preference mixture was used for DPO on the Llama 3.1 Tulu 3 8B SFT checkpoint to obtain Llama 3.1 Tulu 3 8B DPO. The model contains 272,898 generation pairs obtained using various models including Google Gemma 2, InternLM2.5, Llama 3.1, and proprietary models like GPT-4 and Claude.

## Usage

The model can be loaded with: `from transformers import AutoModelForCausalLM tulu_model = AutoModelForCausalLM.from_pretrained("allenai/Llama-3.1-Tulu-3-8B-DPO")`.

The model card and repository are available directly at https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B-DPO.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26b25327-2ba2-4fb9-8403-0a38eb0c7f7b",
  "isSidechain": true,
  "promptId": "eec20fb0-9336-4e73-a283-089bd6e9bec5",
  "agentId": "a470d481c389b3356",
  "type": "user",
  "uuid": "8c8eb19d-6c5a-44eb-b9db-1ae4f9d31405",
  "sourceToolAssistantUUID": "26b25327-2ba2-4fb9-8403-0a38eb0c7f7b",
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

_source line 19 · 2026-05-19T23:41:07.264Z_

<details><summary>↩ Tool result · `toolu_01SuSrX7irGR7XbM1oTbNHnR`</summary>

```text
Web search results for query: "site:huggingface.co "allenai/Llama-3.1-Tulu-3-8B" instruct"

Links: [{"title":"allenai/Llama-3.1-Tulu-3-8B · Hugging Face","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B"},{"title":"allenai/Llama-3.1-Tulu-3-8B-RM · Hugging Face","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B-RM"},{"title":"allenai/Llama-3.1-Tulu-3-8B-SFT · Hugging Face","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B-SFT"},{"title":"allenai/Llama-3.1-Tulu-3.1-8B · Hugging Face","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3.1-8B"},{"title":"allenai/Llama-3.1-Tulu-3-8B-DPO · Hugging Face","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B-DPO"},{"title":"README.md · allenai/Llama-3.1-Tulu-3.1-8B at 2f0b4fd3822f0c938f02ea199c4a202cadcd8224","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3.1-8B/blob/2f0b4fd3822f0c938f02ea199c4a202cadcd8224/README.md"},{"title":"allenai/Llama-3.1-Tulu-3-8B-RL-RM-RB2 · Hugging Face","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B-RL-RM-RB2"},{"title":"allenai/Llama-3.1-Tulu-3-8B-DPO-RM-RB2 · Hugging Face","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B-DPO-RM-RB2"},{"title":"Update README.md (#1) · allenai/Llama-3.1-Tulu-3-8B-RM at 76247c0","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B-RM/commit/76247c00745747f820f1712949b5b37901d0f9c4"},{"title":"allenai/Llama-3.1-Tulu-3-8B-DPO · Batch Size","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B-DPO/discussions/4"}]

I found several results related to the Llama-3.1-Tulu-3-8B model on Hugging Face. Here's what the search revealed:

## Main Model Page

The primary result shows the Tülu 3 is a leading instruction following model family, offering a post-training package with fully open-source data, code, and recipes designed to serve as a comprehensive guide for modern techniques. 

## Model Capabilities and Design

Tülu 3 is designed for state-of-the-art performance on a diversity of tasks in addition to chat, such as MATH, GSM8K, and IFEval. The model type is a model trained on a mix of publicly available, synthetic and human-created datasets.

## Related Model Variants

The search results also revealed several related variants:
- **Tülu-3-8B-SFT** (Supervised Fine-Tuning)
- **Tülu-3-8B-DPO** (Direct Preference Optimization)
- **Tülu-3-8B-RM** (Reward Model)
- **Tülu-3.1-8B** (updated version with improvements)

## Licensing

All Llama 3.1 Tülu3 models are released under Meta's Llama 3.1 Community License Agreement, and Tülu3 is intended for research and educational use.

The models can be loaded using the Hugging Face Transformers library with `AutoModelForCausalLM.from_pretrained()`.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d6a9cdd8-180f-421d-bafa-e55668a43fa9",
  "isSidechain": true,
  "promptId": "eec20fb0-9336-4e73-a283-089bd6e9bec5",
  "agentId": "a470d481c389b3356",
  "type": "user",
  "uuid": "43093d33-554e-47e9-8d0f-50f369720e27",
  "sourceToolAssistantUUID": "d6a9cdd8-180f-421d-bafa-e55668a43fa9",
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

_source line 20 · 2026-05-19T23:41:08.726Z_

<details><summary>↩ Tool result · `toolu_01Nkpj3ATbSz8UznkPFDPE9h`</summary>

```text
Web search results for query: "Tulu 3 8B all released checkpoints allenai huggingface SFT DPO RL RLVR"

Links: [{"title":"Tulu 3 Datasets - a allenai Collection","url":"https://huggingface.co/collections/allenai/tulu-3-datasets"},{"title":"allenai/Llama-3.1-Tulu-3-8B · Hugging Face","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B"},{"title":"allenai/Llama-3.1-Tulu-3.1-8B · Hugging Face","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3.1-8B"},{"title":"allenai/Llama-3.1-Tulu-3-8B-DPO-RM-RB2 · Hugging Face","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B-DPO-RM-RB2"},{"title":"allenai/tulu-3-wildchat-if-on-policy-8b · Datasets at Hugging Face","url":"https://huggingface.co/datasets/allenai/tulu-3-wildchat-if-on-policy-8b"},{"title":"allenai/Llama-3.1-Tulu-3-8B-RL-RM-RB2 · Hugging Face","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B-RL-RM-RB2"},{"title":"allenai/Llama-3.1-Tulu-3-8B-RM · Hugging Face","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B-RM"},{"title":"allenai/Llama-3.1-Tulu-3-8B-SFT · Hugging Face","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B-SFT"},{"title":"allenai/Llama-3.1-Tulu-3-70B-broken · Hugging Face","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3-70B-broken"},{"title":"allenai/llama-3-tulu-2-8b · Hugging Face","url":"https://huggingface.co/allenai/llama-3-tulu-2-8b"}]

Based on the search results, here's what I found about the Tulu 3 8B released checkpoints from Allen AI on Hugging Face:

## Tulu 3 8B Checkpoint Releases

Allen AI has released multiple models with Tulu 3 -- state of the art open post-training recipes.

The main Tulu 3 8B checkpoints available include:

1. **Base Model**: Llama-3.1-Tulu-3-8B - The primary instruction-following model

2. **SFT Checkpoint**: Llama-3.1-Tulu-3-8B-SFT - The supervised fine-tuned version

3. **DPO Checkpoints**: The full preference mixture used for DPO on the 8B SFT checkpoint

4. **Reward Models**: 
   - Llama-3.1-Tulu-3-8B-RM (standard reward model)
   - Llama-3.1-Tulu-3-8B-DPO-RM-RB2 and Llama-3.1-Tulu-3-8B-RL-RM-RB2 (reward models released with Reward Bench 2)

5. **Tulu 3.1 Update**: The new version (3.1) comes from an improvement only in the final RL stage of training, switching from PPO to GRPO (no reward model) with further hyperparameter tuning to achieve substantial performance improvements

The checkpoints represent different stages of post-training, from SFT through DPO and RL stages, along with associated reward models for preference training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f06b03db-1207-4040-a859-b7560d16e3fb",
  "isSidechain": true,
  "promptId": "eec20fb0-9336-4e73-a283-089bd6e9bec5",
  "agentId": "a470d481c389b3356",
  "type": "user",
  "uuid": "c5434fdd-3ecf-4f20-ad05-14c601635f1b",
  "sourceToolAssistantUUID": "f06b03db-1207-4040-a859-b7560d16e3fb",
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

_source line 21 · 2026-05-19T23:41:11.528Z_

Let me do one more search to confirm whether there is any explicit "Instruct" variant and to understand the exact naming of the final model.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5434fdd-3ecf-4f20-ad05-14c601635f1b",
  "isSidechain": true,
  "agentId": "a470d481c389b3356",
  "requestId": "req_011CbCp43NxxkkFzYG6hA5gq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61033efe-68fa-4423-8aa6-7759ca3cb681",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PH1FRXaKwaUiZBAS4VM5ug",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3871,
      "cache_read_input_tokens": 13387,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3871,
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

_source line 22 · 2026-05-19T23:41:12.142Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ejqvw3LEDEw1yaBqF6vnvx`</summary>

```json
{
  "query": "allenai Llama-3.1-Tulu-3-8B final model RLVR training pipeline stages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61033efe-68fa-4423-8aa6-7759ca3cb681",
  "isSidechain": true,
  "agentId": "a470d481c389b3356",
  "requestId": "req_011CbCp43NxxkkFzYG6hA5gq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6403e67-13a6-47d1-a7c1-db3a56c4d2bf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PH1FRXaKwaUiZBAS4VM5ug",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3871,
      "cache_read_input_tokens": 13387,
      "output_tokens": 111,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3871
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 111,
          "cache_read_input_tokens": 13387,
          "cache_creation_input_tokens": 3871,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3871,
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

_source line 23 · 2026-05-19T23:41:18.491Z_

<details><summary>↩ Tool result · `toolu_01Ejqvw3LEDEw1yaBqF6vnvx`</summary>

```text
Web search results for query: "allenai Llama-3.1-Tulu-3-8B final model RLVR training pipeline stages"

Links: [{"title":"Llama-3.1-Tulu-3-8B","url":"https://www.promptlayer.com/models/llama-31-tulu-3-8b"},{"title":"README.md · allenai/Llama-3.1-Tulu-3.1-8B at 2f0b4fd3822f0c938f02ea199c4a202cadcd8224","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3.1-8B/blob/2f0b4fd3822f0c938f02ea199c4a202cadcd8224/README.md"},{"title":"open-instruct/docs/tulu3.md at main · allenai/open-instruct","url":"https://github.com/allenai/open-instruct/blob/main/docs/tulu3.md"},{"title":"allenai/Llama-3.1-Tulu-3-8B · Hugging Face","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B"},{"title":"Tülu 3: The next era in open post-training | Ai2","url":"https://allenai.org/blog/tulu-3-technical"},{"title":"allenai/Llama-3.1-Tulu-3-8B-RL-RM-RB2 · Hugging Face","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B-RL-RM-RB2"},{"title":"allenai/Llama-3.1-Tulu-3-8B-RM · Hugging Face","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B-RM"},{"title":"README.md · allenai/Llama-3.1-Tulu-3-405B at 267ec6d55c866f2ce7f038130dfd1fe1e731f6dd","url":"https://huggingface.co/allenai/Llama-3.1-Tulu-3-405B/blob/267ec6d55c866f2ce7f038130dfd1fe1e731f6dd/README.md"}]

Based on the search results, here's information about the Allen AI Llama-3.1-Tulu-3-8B final model and its RLVR training pipeline stages:

## Training Pipeline Stages

The Llama-3.1-Tulu-3-8B model represents the culmination of a sophisticated training pipeline that includes Supervised Fine-Tuning (SFT), Direct Preference Optimization (DPO), and RLVR training stages.

The Tülu 3 models are produced through a five-part post-training recipe on top of pre-trained language models (namely Llama 3 Base).

## RLVR Training Details

Integrating RLVR as a component of the generalist training pipeline can gain up to 1.7, 3.3, and 1.3 points improvement over the DPO checkpoint on MATH, GSM8K and IFEval.

Starting RLVR from SFT results in bigger gains, but the highest final models were from training with DPO before RLVR.

The model also demonstrates broader benefits: RLVR also led to improvements on other tasks that it was not optimized for including BigBenchHard, Drop, and AlpacaEval 2.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6403e67-13a6-47d1-a7c1-db3a56c4d2bf",
  "isSidechain": true,
  "promptId": "eec20fb0-9336-4e73-a283-089bd6e9bec5",
  "agentId": "a470d481c389b3356",
  "type": "user",
  "uuid": "12a303e4-6fe8-432f-a7ac-b788549f9810",
  "sourceToolAssistantUUID": "b6403e67-13a6-47d1-a7c1-db3a56c4d2bf",
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

_source line 24 · 2026-05-19T23:41:45.978Z_

Here are my findings:

## Tulu 3 on LLaMA 3.1-8B: Checkpoint Verification

### What actually exists on HuggingFace (all under the `allenai` organization):

1. **`allenai/Llama-3.1-Tulu-3-8B`** -- This is the **final** model, the result of the complete post-training pipeline (SFT -> DPO -> RLVR). It is NOT a "base" checkpoint; it is the fully trained end product.

2. **`allenai/Llama-3.1-Tulu-3-8B-SFT`** -- Yes, this exists. It is the intermediate checkpoint after the supervised fine-tuning stage.

3. **`allenai/Llama-3.1-Tulu-3-8B-DPO`** -- Yes, this exists. It is the intermediate checkpoint after the DPO stage (trained on top of the SFT checkpoint).

4. **`allenai/Llama-3.1-Tulu-3-8B-RM`** -- The reward model used during training also exists.

### What does NOT exist:

- **No separate "Instruct" variant.** There is no model called `Llama-3.1-Tulu-3-8B-Instruct` on HuggingFace. The final model is simply named `Llama-3.1-Tulu-3-8B` (without any "Instruct" suffix).

- **No "Base LLaMA 3.1-8B" released by Allen AI.** The base LLaMA 3.1-8B is Meta's model (`meta-llama/Llama-3.1-8B`), not an Allen AI release. Tulu 3 starts from Meta's base model and applies post-training. Allen AI does not re-release Meta's base checkpoint under their own namespace.

### Correcting the proposal's claims:

The proposal claims Tulu 3 releases four checkpoints: Base, SFT, DPO, and Instruct. This is **partially accurate but mislabeled**:

| Proposal's claim | What actually exists | Accurate? |
|---|---|---|
| "Base LLaMA 3.1-8B" | Meta's `meta-llama/Llama-3.1-8B` (not an Allen AI release) | Misleading -- this is Meta's model, not a Tulu 3 artifact |
| "Llama-3.1-Tulu-3-8B-SFT" | `allenai/Llama-3.1-Tulu-3-8B-SFT` | **Correct** |
| "Llama-3.1-Tulu-3-8B-DPO" | `allenai/Llama-3.1-Tulu-3-8B-DPO` | **Correct** |
| "Full Instruct variant" | `allenai/Llama-3.1-Tulu-3-8B` (the final model after SFT+DPO+RLVR) | **Partially correct** -- the final model exists but is NOT called "Instruct" |

### Key detail: Tulu 3's training pipeline has THREE stages, not two

The pipeline is: **SFT -> DPO -> RLVR** (Reinforcement Learning with Verifiable Rewards). The final model (`Llama-3.1-Tulu-3-8B`) is the output after all three stages. Allen AI releases intermediate checkpoints at each stage (SFT and DPO), plus the final model and a reward model. This is a notable strength of Tulu 3 -- they release the full chain of intermediate artifacts, not just the final model.

There is also a newer `allenai/Llama-3.1-Tulu-3.1-8B` (note "3.1" not "3") which is an updated version that replaced PPO with GRPO in the RL stage.

Sources:
- [allenai/Llama-3.1-Tulu-3-8B](https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B)
- [allenai/Llama-3.1-Tulu-3-8B-SFT](https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B-SFT)
- [allenai/Llama-3.1-Tulu-3-8B-DPO](https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B-DPO)
- [allenai/Llama-3.1-Tulu-3-8B-RM](https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B-RM)
- [allenai/Llama-3.1-Tulu-3.1-8B](https://huggingface.co/allenai/Llama-3.1-Tulu-3.1-8B)
- [Tulu 3 paper (arXiv)](https://arxiv.org/abs/2411.15124)
- [Tulu 3 technical blog (Allen AI)](https://allenai.org/blog/tulu-3-technical)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12a303e4-6fe8-432f-a7ac-b788549f9810",
  "isSidechain": true,
  "agentId": "a470d481c389b3356",
  "requestId": "req_011CbCp4n2kuzmDh8tdi7B9T",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0adc1813-4114-4b33-9af8-e8016dca3df3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "b89f7886-bb1e-46f5-8067-f36e58028d73",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BhgaH94Mm6ezidUyHcJtVd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1078,
      "cache_read_input_tokens": 17258,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1078,
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
