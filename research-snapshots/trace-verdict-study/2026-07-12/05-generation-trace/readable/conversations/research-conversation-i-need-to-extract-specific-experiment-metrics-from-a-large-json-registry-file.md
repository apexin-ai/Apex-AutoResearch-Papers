# Research conversation: I need to extract specific experiment metrics from a large JSON registry file at: /home/ubuntu/.claude-account-3/project

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a86b080f191dc2217.jsonl`
- **Structured JSON:** [`339fd1a3ea4cdeb34cf3.json`](../../sessions/33/339fd1a3ea4cdeb34cf3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

32 recorded events

### User

_source line 1 · 2026-05-21T19:04:24.911Z_

I need to extract specific experiment metrics from a large JSON registry file at:
/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/f5f4efcf-b091-4929-abdf-35aa1152d6be/tool-results/mcp-agent-ml-research-read_registry-1779390254681.txt

The file has schema: {result: string} — meaning the actual JSON content is a string inside the "result" field.

I need metrics (especially accuracy, eval_accuracy, best_accuracy, or similar) for these experiments:
1. All experiments with IDs starting with "qwen15b_" (Qwen-1.5B experiments)
2. All experiments with IDs starting with "vota_" (Qwen-7B experiments)
3. Experiments: codellama13b_ae_only_seed42, codellama13b_loop_only_seed42, deepseek_ae_only_seed42, deepseek_loop_only_seed42
4. Any experiment related to "full_trace" or "no_trace" for any model
5. Any experiment with "exception_only" in the name

Use jq or python to parse. First probe the structure, then extract just these experiments. For each matching experiment, report:
- exp_id
- status
- conclusion (if any)
- All metrics (the full metrics dict)
- model name if available

Return ALL the data verbatim — don't summarize or omit fields. I need exact numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "d3a99d3c-02c3-4d5e-9ec2-b28e1b492d4b",
  "agentId": "a86b080f191dc2217",
  "type": "user",
  "uuid": "dbd62a76-51b4-42a4-ab61-acfd589a6f43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "f5f4efcf-b091-4929-abdf-35aa1152d6be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T19:04:24.916Z_

```json
{
  "parentUuid": "dbd62a76-51b4-42a4-ab61-acfd589a6f43",
  "isSidechain": true,
  "agentId": "a86b080f191dc2217",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__update_registry"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__update_registry"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "2b722aef-958a-4d2c-9dd3-dd0bbac39d26",
  "timestamp": "2026-05-21T19:04:24.916Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "f5f4efcf-b091-4929-abdf-35aa1152d6be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-21T19:04:27.613Z_



Let me start by probing the file structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b722aef-958a-4d2c-9dd3-dd0bbac39d26",
  "isSidechain": true,
  "agentId": "a86b080f191dc2217",
  "requestId": "req_011CbGEZwDH5i5sw1Q5sfKr8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3e0d46a9-a1fc-41bf-8249-91875e7a4eb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "f5f4efcf-b091-4929-abdf-35aa1152d6be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ep4yxMQoXCJik467Whk5ZE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15032,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15032,
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

_source line 4 · 2026-05-21T19:04:28.700Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HfkV8Ngjau1uc4gdgDgGWR`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/f5f4efcf-b091-4929-abdf-35aa1152d6be/tool-results/mcp-agent-ml-research-read_registry-1779390254681.txt",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e0d46a9-a1fc-41bf-8249-91875e7a4eb9",
  "isSidechain": true,
  "agentId": "a86b080f191dc2217",
  "requestId": "req_011CbGEZwDH5i5sw1Q5sfKr8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3cfba444-5fa9-40c4-b413-0aaa9f5bf755",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "f5f4efcf-b091-4929-abdf-35aa1152d6be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ep4yxMQoXCJik467Whk5ZE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15032,
      "cache_read_input_tokens": 0,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15032
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 170,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15032,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15032,
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

_source line 5 · 2026-05-21T19:04:29.063Z_

<details><summary>↩ Tool result · reported error · `toolu_01HfkV8Ngjau1uc4gdgDgGWR`</summary>

```text
File content (130361 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3cfba444-5fa9-40c4-b413-0aaa9f5bf755",
  "isSidechain": true,
  "promptId": "d3a99d3c-02c3-4d5e-9ec2-b28e1b492d4b",
  "agentId": "a86b080f191dc2217",
  "type": "user",
  "uuid": "975c5fa8-da94-40e1-9876-e706e250eeb3",
  "toolUseResult": "Error: File content (130361 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "3cfba444-5fa9-40c4-b413-0aaa9f5bf755",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "f5f4efcf-b091-4929-abdf-35aa1152d6be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-21T19:04:31.777Z_

The file is very large. Let me probe its structure with Python to understand the format, then extract targeted experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "975c5fa8-da94-40e1-9876-e706e250eeb3",
  "isSidechain": true,
  "agentId": "a86b080f191dc2217",
  "requestId": "req_011CbGEaEsfDkibJJuC3KCGY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb0709a9-adfd-42ee-a451-3ec95cb92fc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "f5f4efcf-b091-4929-abdf-35aa1152d6be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ememug693uz3wCDy87zDMT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1072,
      "cache_read_input_tokens": 15032,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1072,
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

_source line 7 · 2026-05-21T19:04:32.598Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Y219x8512tAxGeuVwwkqAD`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/f5f4efcf-b091-4929-abdf-35aa1152d6be/tool-results/mcp-agent-ml-research-read_registry-1779390254681.txt",
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb0709a9-adfd-42ee-a451-3ec95cb92fc6",
  "isSidechain": true,
  "agentId": "a86b080f191dc2217",
  "requestId": "req_011CbGEaEsfDkibJJuC3KCGY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b1f6ab7-25d4-4f25-a3d5-a3bf81cc4037",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "f5f4efcf-b091-4929-abdf-35aa1152d6be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ememug693uz3wCDy87zDMT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1072,
      "cache_read_input_tokens": 15032,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1072
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 182,
          "cache_read_input_tokens": 15032,
          "cache_creation_input_tokens": 1072,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1072,
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

_source line 8 · 2026-05-21T19:04:32.984Z_

<details><summary>↩ Tool result · reported error · `toolu_01Y219x8512tAxGeuVwwkqAD`</summary>

```text
File content (130361 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b1f6ab7-25d4-4f25-a3d5-a3bf81cc4037",
  "isSidechain": true,
  "promptId": "d3a99d3c-02c3-4d5e-9ec2-b28e1b492d4b",
  "agentId": "a86b080f191dc2217",
  "type": "user",
  "uuid": "4c4c0f1b-10ac-4447-b292-1d179f3317aa",
  "toolUseResult": "Error: File content (130361 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "2b1f6ab7-25d4-4f25-a3d5-a3bf81cc4037",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "f5f4efcf-b091-4929-abdf-35aa1152d6be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T19:04:36.846Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01CcaoDrzczNfZoNmLUVkKEw`</summary>

```json
{
  "command": "head -c 2000 \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/f5f4efcf-b091-4929-abdf-35aa1152d6be/tool-results/mcp-agent-ml-research-read_registry-1779390254681.txt\"",
  "description": "Probe first 2000 bytes of the large JSON file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c4c0f1b-10ac-4447-b292-1d179f3317aa",
  "isSidechain": true,
  "agentId": "a86b080f191dc2217",
  "requestId": "req_011CbGEaXeU17UXML3AX1ELT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "59ef7014-a874-4d1f-8907-111aea5297bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "f5f4efcf-b091-4929-abdf-35aa1152d6be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018qXzgvxmWyGzHUKxgYPBg5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 243,
      "cache_read_input_tokens": 16104,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 243,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 61,
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

_source line 10 · 2026-05-21T19:04:37.061Z_

<details><summary>↩ Tool result · `toolu_01CcaoDrzczNfZoNmLUVkKEw`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"regex_nomarker_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T19:03:04.213Z\", \"updated_at\": \"2026-05-21T19:03:23.905Z\", \"hypothesis\": \"Regex baselines (B1-B5) on nomarker condition will show significant degradation, especially B5 which relies on the [No exception data in trace] marker. This reveals the marker-condition B5=99.33% is a format artifact, not genuine code reasoning.\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python eval/regex_baseline.py on nomarker test data\", \"server\": \"westd-11235\", \"data_path\": \"/root/autodl-tmp/trace-verdict-study-data/exception_only_nomarker_test.jsonl\", \"data_count\": 1190, \"model_name\": \"regex_heuristics\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"completed_at\": \"2026-05-21T19:03:22.128Z\", \"metrics\": {\"B5_marker_acc\": 0.9933, \"B5_nomarker_acc\": 0.2849, \"B5_delta_pp\": -70.84, \"B1_marker_acc\": 0.9345, \"B1_nomarker_acc\": 0.7151, \"B4_marker_acc\": 0.9361, \"B4_nomarker_acc\": 0.9361, \"B5b_nomarker_acc\": 0.9345, \"n\": 1190}}, \"exception_only_padded2048_seed42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T18:24:05.794Z\", \"updated_at\": \"2026-05-21T18:31:17.479Z\", \"hypothesis\": \"Padding exception_only traces to 2048 tokens (matching full_trace length) with neutral tokens should preserve ~99% accuracy, proving performance gap between exception_only and full_trace is due to information noise not sequence length. Controls for the 13x length confound (150 vs 2048 tokens).\", \"spec\": {\"command\": \"/root/miniconda3/bin/python train/train_sft.py --condition exception_only_padded2048 --gradient_checkpointing --gpu 0 --seed 42 --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_padded2048_seed42 --wandb_project trace-verdict-study --wandb_run_name exception_only_padded2048_seed42\", \"server\": \"w
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59ef7014-a874-4d1f-8907-111aea5297bb",
  "isSidechain": true,
  "promptId": "d3a99d3c-02c3-4d5e-9ec2-b28e1b492d4b",
  "agentId": "a86b080f191dc2217",
  "type": "user",
  "uuid": "33f2d7bb-c0ac-488e-85c8-c67db44c4f6a",
  "sourceToolAssistantUUID": "59ef7014-a874-4d1f-8907-111aea5297bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "f5f4efcf-b091-4929-abdf-35aa1152d6be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T19:04:37.710Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01BbNyMG5uAXy4mnyP6pvuz5`</summary>

```json
{
  "command": "wc -c \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/f5f4efcf-b091-4929-abdf-35aa1152d6be/tool-results/mcp-agent-ml-research-read_registry-1779390254681.txt\"",
  "description": "Get file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33f2d7bb-c0ac-488e-85c8-c67db44c4f6a",
  "isSidechain": true,
  "agentId": "a86b080f191dc2217",
  "requestId": "req_011CbGEaXeU17UXML3AX1ELT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9517bd85-905d-4693-bac3-680a7b542aa5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "f5f4efcf-b091-4929-abdf-35aa1152d6be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018qXzgvxmWyGzHUKxgYPBg5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 243,
      "cache_read_input_tokens": 16104,
      "output_tokens": 324,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 243
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 324,
          "cache_read_input_tokens": 16104,
          "cache_creation_input_tokens": 243,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 243,
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

_source line 12 · 2026-05-21T19:04:37.766Z_

<details><summary>↩ Tool result · `toolu_01BbNyMG5uAXy4mnyP6pvuz5`</summary>

```text
323997 /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/f5f4efcf-b091-4929-abdf-35aa1152d6be/tool-results/mcp-agent-ml-research-read_registry-1779390254681.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9517bd85-905d-4693-bac3-680a7b542aa5",
  "isSidechain": true,
  "promptId": "d3a99d3c-02c3-4d5e-9ec2-b28e1b492d4b",
  "agentId": "a86b080f191dc2217",
  "type": "user",
  "uuid": "bd4b79d1-ebee-4d12-8bb4-59f2490ccabf",
  "sourceToolAssistantUUID": "9517bd85-905d-4693-bac3-680a7b542aa5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "f5f4efcf-b091-4929-abdf-35aa1152d6be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-21T19:04:41.751Z_

Good. The file is ~324KB. The outer structure is `{result: "&lt;escaped JSON string>"}` and the inner JSON has `data.experiments` with experiment objects. Let me now extract all matching experiments with Python.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd4b79d1-ebee-4d12-8bb4-59f2490ccabf",
  "isSidechain": true,
  "agentId": "a86b080f191dc2217",
  "requestId": "req_011CbGEat91asuQ9Sv3wot3T",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b72182b-fea9-4c71-a8ed-7d7d53eb6c82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "f5f4efcf-b091-4929-abdf-35aa1152d6be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KiNfT9qP1MugFvWHT2wNz6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1227,
      "cache_read_input_tokens": 16347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1227,
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

_source line 14 · 2026-05-21T19:04:44.268Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01UwoocVGCXi8KoA8bJxhc9V`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/f5f4efcf-b091-4929-abdf-35aa1152d6be/tool-results/mcp-agent-ml-research-read_registry-1779390254681.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw[\"result\"])\nexperiments = inner[\"data\"][\"experiments\"]\n\n# Print all experiment IDs to understand the full set\nprint(f\"Total experiments: {len(experiments)}\")\nprint(\"\\nAll experiment IDs:\")\nfor eid in sorted(experiments.keys()):\n    print(f\"  {eid}\")\nPYEOF",
  "description": "Parse the JSON and list all experiment IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b72182b-fea9-4c71-a8ed-7d7d53eb6c82",
  "isSidechain": true,
  "agentId": "a86b080f191dc2217",
  "requestId": "req_011CbGEat91asuQ9Sv3wot3T",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "56f0f747-80b5-4165-899b-570a6784ae83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "f5f4efcf-b091-4929-abdf-35aa1152d6be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KiNfT9qP1MugFvWHT2wNz6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1227,
      "cache_read_input_tokens": 16347,
      "output_tokens": 338,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1227
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 338,
          "cache_read_input_tokens": 16347,
          "cache_creation_input_tokens": 1227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1227,
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

_source line 15 · 2026-05-21T19:04:44.358Z_

<details><summary>↩ Tool result · `toolu_01UwoocVGCXi8KoA8bJxhc9V`</summary>

```text
Total experiments: 168

All experiment IDs:
  ae_only_seed123
  ae_only_seed456
  calibration_analysis_seed42
  codellama13b_ae_only_seed123
  codellama13b_ae_only_seed42
  codellama13b_exception_only_seed123
  codellama13b_exception_only_seed42
  codellama13b_exception_only_seed456
  codellama13b_full_trace_head2048_seed42
  codellama13b_full_trace_tail1024_seed42
  codellama13b_full_trace_tail1024_seed42_v2
  codellama13b_full_trace_tail1024_seed42_v3
  codellama13b_full_trace_tail2048_seed42
  codellama13b_full_trace_tail2048_seed42_v2
  codellama13b_full_trace_tail2048_seed42_v3
  codellama13b_full_trace_tail256_seed42
  codellama13b_full_trace_tail384_seed42
  codellama13b_full_trace_tail512_seed123
  codellama13b_full_trace_tail512_seed42
  codellama13b_full_trace_tail512_seed456
  codellama13b_label_only_seed123_v2
  codellama13b_label_only_seed42
  codellama13b_label_only_seed42_v2
  codellama13b_loop_only_seed123
  codellama13b_loop_only_seed42
  codellama13b_loop_only_seed456
  codellama13b_no_trace_seed42
  codellama13b_nomarker_seed42
  codellama13b_vota_seed123
  codellama13b_vota_seed42
  codellama_exception_only_seed42
  codellama_no_trace_seed42
  codellama_vota_seed42
  cross_model_calibration
  cross_model_calibration_eval
  debugbench_exception_bug_fix
  debugbench_exception_only_seed42
  debugbench_no_trace_seed42
  debugbench_vota_seed42
  deepseek_ae_only_seed123
  deepseek_ae_only_seed42
  deepseek_exception_only_seed123
  deepseek_exception_only_seed123_v2
  deepseek_exception_only_seed42
  deepseek_exception_only_seed456
  deepseek_full_trace_head2048_seed42
  deepseek_full_trace_seed42
  deepseek_full_trace_seed42_v2
  deepseek_full_trace_seed42_v3
  deepseek_full_trace_tail1024_seed42
  deepseek_full_trace_tail2048_seed42
  deepseek_full_trace_tail256_seed42
  deepseek_full_trace_tail384_seed42
  deepseek_full_trace_tail512_seed123
  deepseek_full_trace_tail512_seed123_v2
  deepseek_full_trace_tail512_seed42
  deepseek_full_trace_tail512_seed456
  deepseek_label_only_seed42
  deepseek_loop_only_seed123
  deepseek_loop_only_seed42
  deepseek_loop_only_seed456
  deepseek_no_trace_seed123
  deepseek_no_trace_seed42
  deepseek_vota_seed123
  deepseek_vota_seed42
  deepseek_vota_seed456
  eval_missing_predictions_batch
  eval_missing_predictions_batch_v2
  exception_only_nomarker_seed123
  exception_only_nomarker_seed42
  exception_only_nomarker_seed456
  exception_only_padded2048_seed42
  exception_only_seed123
  exception_only_seed456
  fewshot_gpt41_exception_only_0shot
  fewshot_gpt41_exception_only_3shot
  fewshot_gpt41_no_trace_0shot
  fewshot_gpt4o_exception_only_0shot
  fewshot_gpt4o_exception_only_3shot
  fewshot_gpt4o_no_trace_0shot
  fewshot_qwen7b_exception_only
  full_trace_1024tok_seed42
  full_trace_2048tok_seed42
  full_trace_256tok_seed42
  full_trace_512tok_seed42
  full_trace_label_only_seed42
  full_trace_seed42
  full_trace_seed42_v2
  full_trace_seed42_v5
  full_trace_tail256_seed42
  full_trace_tail_1024_seed42
  full_trace_tail_256_seed42
  full_trace_tail_512_seed42
  full_trace_tail_seed42
  label_only_seed123
  label_only_seed456
  loop_only_seed123
  loop_only_seed456
  no_trace_seed42
  no_trace_seed42_v2
  no_trace_seed42_v3
  no_trace_seed42_v4
  no_trace_seed42_v5
  qwen1.5b_exception_only_seed42
  qwen1.5b_full_trace_seed42
  qwen1.5b_no_trace_seed42
  qwen1.5b_vota_seed42
  qwen15b_ae_only_seed123
  qwen15b_ae_only_seed42
  qwen15b_exception_only_seed123
  qwen15b_exception_only_seed123_v2
  qwen15b_exception_only_seed42
  qwen15b_exception_only_seed456
  qwen15b_full_trace_head2048_seed42
  qwen15b_full_trace_seed42
  qwen15b_full_trace_tail1024_seed42
  qwen15b_full_trace_tail2048_seed42
  qwen15b_full_trace_tail256_seed42
  qwen15b_full_trace_tail384_seed42
  qwen15b_full_trace_tail512_seed123
  qwen15b_full_trace_tail512_seed42
  qwen15b_full_trace_tail512_seed456
  qwen15b_label_only_seed123_v2
  qwen15b_label_only_seed42
  qwen15b_label_only_seed42_v2
  qwen15b_label_only_seed456_v2
  qwen15b_loop_only_seed123
  qwen15b_loop_only_seed42
  qwen15b_loop_only_seed456
  qwen15b_no_trace_seed123
  qwen15b_no_trace_seed42
  qwen15b_no_trace_seed456
  qwen15b_nomarker_seed42
  qwen15b_vota_seed123
  qwen15b_vota_seed42
  qwen7b_exception_only_dynamics_seed42
  qwen7b_full_trace_dynamics_seed42
  qwen7b_full_trace_head2048_seed42
  qwen7b_full_trace_label_only_seed123
  qwen7b_full_trace_label_only_seed456
  qwen7b_full_trace_seed123
  qwen7b_full_trace_seed456
  qwen7b_full_trace_seed456_v2
  qwen7b_full_trace_tail384_seed42
  qwen7b_full_trace_tail512_seed123
  qwen7b_full_trace_tail512_seed42
  qwen7b_full_trace_tail512_seed456
  qwen7b_vota_seed123
  qwen7b_vota_seed456
  regex_baseline_analysis
  regex_nomarker_baseline
  vota_ae_only_seed42
  vota_exception_only_seed42
  vota_exception_only_seed42_v2
  vota_loop_only_seed42
  vota_no_ae_seed42
  vota_seed123
  vota_seed42
  vota_seed42_v2
  vota_seed42_v3
  vota_seed42_v4
  vota_seed42_v5
  vota_seed456
  vota_seed456_v2
  zeroshot_codellama13b_exception_only
  zeroshot_deepseek7b_exception_only
  zeroshot_qwen15b_exception_only
  zeroshot_qwen7b_exception_only
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56f0f747-80b5-4165-899b-570a6784ae83",
  "isSidechain": true,
  "promptId": "d3a99d3c-02c3-4d5e-9ec2-b28e1b492d4b",
  "agentId": "a86b080f191dc2217",
  "type": "user",
  "uuid": "9edae522-916a-4781-bc0e-adb746573aa3",
  "sourceToolAssistantUUID": "56f0f747-80b5-4165-899b-570a6784ae83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "f5f4efcf-b091-4929-abdf-35aa1152d6be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-21T19:04:46.894Z_

Now let me extract all matching experiments with full details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9edae522-916a-4781-bc0e-adb746573aa3",
  "isSidechain": true,
  "agentId": "a86b080f191dc2217",
  "requestId": "req_011CbGEbNJfWZfAd8dFvu7iX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5cc18cc-ab03-4e64-99b0-af229c032a5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "f5f4efcf-b091-4929-abdf-35aa1152d6be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HfpYnaVUuBeaux9CaS3MVP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2588,
      "cache_read_input_tokens": 17574,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2588,
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

_source line 17 · 2026-05-21T19:04:54.822Z_

<details open><summary>🔧 Tool call — Bash · `toolu_013M1L22E49ccshmwUJNk481`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/f5f4efcf-b091-4929-abdf-35aa1152d6be/tool-results/mcp-agent-ml-research-read_registry-1779390254681.txt\"\n\nwith open(fpath, 'r') as f:\n    raw = json.load(f)\n\ninner = json.loads(raw[\"result\"])\nexperiments = inner[\"data\"][\"experiments\"]\n\ndef matches(eid):\n    # 1. qwen15b_ prefix\n    if eid.startswith(\"qwen15b_\"):\n        return True\n    # Also match qwen1.5b_ prefix (different naming)\n    if eid.startswith(\"qwen1.5b_\"):\n        return True\n    # 2. vota_ prefix\n    if eid.startswith(\"vota_\"):\n        return True\n    # 3. Specific experiments\n    if eid in (\"codellama13b_ae_only_seed42\", \"codellama13b_loop_only_seed42\",\n               \"deepseek_ae_only_seed42\", \"deepseek_loop_only_seed42\"):\n        return True\n    # 4. full_trace or no_trace for any model\n    if \"full_trace\" in eid or \"no_trace\" in eid:\n        return True\n    # 5. exception_only\n    if \"exception_only\" in eid:\n        return True\n    return False\n\nmatched = {}\nfor eid, edata in sorted(experiments.items()):\n    if matches(eid):\n        matched[eid] = edata\n\nprint(f\"Matched {len(matched)} experiments out of {len(experiments)} total.\\n\")\n\nfor eid, edata in sorted(matched.items()):\n    print(\"=\" * 80)\n    print(f\"EXP_ID: {eid}\")\n    print(f\"STATUS: {edata.get('status', 'N/A')}\")\n    print(f\"CONCLUSION: {edata.get('conclusion', 'N/A')}\")\n    \n    # Extract model name from spec if available\n    spec = edata.get('spec', {})\n    model_name = spec.get('model_name', 'N/A')\n    print(f\"MODEL_NAME: {model_name}\")\n    \n    # Full metrics\n    metrics = edata.get('metrics', {})\n    if metrics:\n        print(f\"METRICS: {json.dumps(metrics, indent=2)}\")\n    else:\n        print(\"METRICS: (none)\")\n    print()\n\nPYEOF",
  "description": "Extract all matching experiments with full details",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5cc18cc-ab03-4e64-99b0-af229c032a5e",
  "isSidechain": true,
  "agentId": "a86b080f191dc2217",
  "requestId": "req_011CbGEbNJfWZfAd8dFvu7iX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7e1f7064-0e7b-46d0-a54a-df1ff941275b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "f5f4efcf-b091-4929-abdf-35aa1152d6be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HfpYnaVUuBeaux9CaS3MVP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2588,
      "cache_read_input_tokens": 17574,
      "output_tokens": 777,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2588
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 777,
          "cache_read_input_tokens": 17574,
          "cache_creation_input_tokens": 2588,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2588,
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

_source line 18 · 2026-05-21T19:04:54.923Z_

<details><summary>↩ Tool result · `toolu_013M1L22E49ccshmwUJNk481`</summary>

```text
&lt;persisted-output>
Output too large (58.2KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/f5f4efcf-b091-4929-abdf-35aa1152d6be/tool-results/b7t9ioqmo.txt

Preview (first 2KB):
Matched 134 experiments out of 168 total.

================================================================================
EXP_ID: codellama13b_ae_only_seed42
STATUS: DONE
CONCLUSION: success
MODEL_NAME: CodeLlama-13b-Instruct-hf
METRICS: {
  "accuracy": 0.9908,
  "accuracy_ci_lower": 0.9849,
  "accuracy_ci_upper": 0.9958,
  "pass_f1": 0.9935,
  "fail_f1": 0.984,
  "majority_baseline": 0.7151
}

================================================================================
EXP_ID: codellama13b_exception_only_seed123
STATUS: DONE
CONCLUSION: success
MODEL_NAME: CodeLlama-13b-Instruct-hf
METRICS: {
  "accuracy": 1,
  "n": 1190,
  "errors": 0,
  "pass_precision": 1,
  "pass_recall": 1,
  "pass_f1": 1,
  "fail_precision": 1,
  "fail_recall": 1,
  "fail_f1": 1,
  "lift_over_majority": 0.2849
}

================================================================================
EXP_ID: codellama13b_exception_only_seed42
STATUS: DONE
CONCLUSION: success
MODEL_NAME: N/A
METRICS: {
  "accuracy": 0.9983,
  "accuracy_ci_lower": 0.9958,
  "accuracy_ci_upper": 1,
  "pass_f1": 0.9988,
  "fail_f1": 0.9971,
  "n_test": 1190
}

================================================================================
EXP_ID: codellama13b_exception_only_seed456
STATUS: DONE
CONCLUSION: success
MODEL_NAME: CodeLlama-13b-Instruct-hf
METRICS: {
  "accuracy": 0.9983,
  "n": 1190,
  "errors": 2,
  "pass_precision": 1,
  "pass_recall": 0.9976,
  "pass_f1": 0.9988,
  "fail_precision": 0.9941,
  "fail_recall": 1,
  "fail_f1": 0.9971
}

================================================================================
EXP_ID: codellama13b_full_trace_head2048_seed42
STATUS: DONE
CONCLUSION: success
MODEL_NAME: CodeLlama-13b-Instruct-hf
METRICS: {
  "accuracy": 0.7992,
  "majority_baseline": 0.7151,
  "lift": 0.084,
  "n_test": 1190,
  "pass_precision": 0.8566,
  "pass_recall": 0.8637,
  "pass_f1": 0.8602,
  "fail_precision": 0.6506,
  "fail_recall": 0.6372,
  "fail_f1": 0.6438,
  "train_loss": 0.0452,
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e1f7064-0e7b-46d0-a54a-df1ff941275b",
  "isSidechain": true,
  "promptId": "d3a99d3c-02c3-4d5e-9ec2-b28e1b492d4b",
  "agentId": "a86b080f191dc2217",
  "type": "user",
  "uuid": "427d129f-b1c3-42b3-aaf8-924883bf4c5e",
  "sourceToolAssistantUUID": "7e1f7064-0e7b-46d0-a54a-df1ff941275b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "f5f4efcf-b091-4929-abdf-35aa1152d6be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-21T19:04:57.205Z_

The output is large. Let me read the full file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "427d129f-b1c3-42b3-aaf8-924883bf4c5e",
  "isSidechain": true,
  "agentId": "a86b080f191dc2217",
  "requestId": "req_011CbGEc9aDvt6YkrMzMdtp9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5018d384-a8e8-4ece-8f4f-22917e89b2ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "f5f4efcf-b091-4929-abdf-35aa1152d6be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015LN7JFKt78qSXcKuTNJryk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1695,
      "cache_read_input_tokens": 20162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1695,
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

_source line 20 · 2026-05-21T19:04:58.029Z_

<details open><summary>🔧 Tool call — Read · `toolu_01L2WvFkHKUvCGSnax1gfhDW`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/f5f4efcf-b091-4929-abdf-35aa1152d6be/tool-results/b7t9ioqmo.txt",
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5018d384-a8e8-4ece-8f4f-22917e89b2ca",
  "isSidechain": true,
  "agentId": "a86b080f191dc2217",
  "requestId": "req_011CbGEc9aDvt6YkrMzMdtp9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a04929f5-e085-44a2-ab99-0da20867c42f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "f5f4efcf-b091-4929-abdf-35aa1152d6be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015LN7JFKt78qSXcKuTNJryk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1695,
      "cache_read_input_tokens": 20162,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1695
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 20162,
          "cache_creation_input_tokens": 1695,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1695,
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

_source line 21 · 2026-05-21T19:04:58.043Z_

<details><summary>↩ Tool result · `toolu_01L2WvFkHKUvCGSnax1gfhDW`</summary>

```text
1	Matched 134 experiments out of 168 total.
2	
3	================================================================================
4	EXP_ID: codellama13b_ae_only_seed42
5	STATUS: DONE
6	CONCLUSION: success
7	MODEL_NAME: CodeLlama-13b-Instruct-hf
8	METRICS: {
9	  "accuracy": 0.9908,
10	  "accuracy_ci_lower": 0.9849,
11	  "accuracy_ci_upper": 0.9958,
12	  "pass_f1": 0.9935,
13	  "fail_f1": 0.984,
14	  "majority_baseline": 0.7151
15	}
16	
17	================================================================================
18	EXP_ID: codellama13b_exception_only_seed123
19	STATUS: DONE
20	CONCLUSION: success
21	MODEL_NAME: CodeLlama-13b-Instruct-hf
22	METRICS: {
23	  "accuracy": 1,
24	  "n": 1190,
25	  "errors": 0,
26	  "pass_precision": 1,
27	  "pass_recall": 1,
28	  "pass_f1": 1,
29	  "fail_precision": 1,
30	  "fail_recall": 1,
31	  "fail_f1": 1,
32	  "lift_over_majority": 0.2849
33	}
34	
35	================================================================================
36	EXP_ID: codellama13b_exception_only_seed42
37	STATUS: DONE
38	CONCLUSION: success
39	MODEL_NAME: N/A
40	METRICS: {
41	  "accuracy": 0.9983,
42	  "accuracy_ci_lower": 0.9958,
43	  "accuracy_ci_upper": 1,
44	  "pass_f1": 0.9988,
45	  "fail_f1": 0.9971,
46	  "n_test": 1190
47	}
48	
49	================================================================================
50	EXP_ID: codellama13b_exception_only_seed456
51	STATUS: DONE
52	CONCLUSION: success
53	MODEL_NAME: CodeLlama-13b-Instruct-hf
54	METRICS: {
55	  "accuracy": 0.9983,
56	  "n": 1190,
57	  "errors": 2,
58	  "pass_precision": 1,
59	  "pass_recall": 0.9976,
60	  "pass_f1": 0.9988,
61	  "fail_precision": 0.9941,
62	  "fail_recall": 1,
63	  "fail_f1": 0.9971
64	}
65	
66	================================================================================
67	EXP_ID: codellama13b_full_trace_head2048_seed42
68	STATUS: DONE
69	CONCLUSION: success
70	MODEL_NAME: CodeLlama-13b-Instruct-hf
71	METRICS: {
72	  "accuracy": 0.7992,
73	  "majority_baseline": 0.7151,
74	  "lift": 0.084,
75	  "n_test": 1190,
76	  "pass_precision": 0.8566,
77	  "pass_recall": 0.8637,
78	  "pass_f1": 0.8602,
79	  "fail_precision": 0.6506,
80	  "fail_recall": 0.6372,
81	  "fail_f1": 0.6438,
82	  "train_loss": 0.0452,
83	  "eval_loss": 0.111,
84	  "accuracy_ci_lower": 0.7765,
85	  "accuracy_ci_upper": 0.8227
86	}
87	
88	================================================================================
89	EXP_ID: codellama13b_full_trace_tail1024_seed42
90	STATUS: DONE
91	CONCLUSION: failed
92	MODEL_NAME: CodeLlama-13b-Instruct-hf
93	METRICS: (none)
94	
95	================================================================================
96	EXP_ID: codellama13b_full_trace_tail1024_seed42_v2
97	STATUS: DONE
98	CONCLUSION: negative
99	MODEL_NAME: CodeLlama-13b-Instruct-hf
100	METRICS: {
101	  "accuracy": 0.876,
102	  "accuracy_ci_lower": 0.856,
103	  "accuracy_ci_upper": 0.893,
104	  "majority_baseline": 0.715,
105	  "lift_pp": 16.1,
106	  "pass_precision": 0.85,
107	  "pass_recall": 1,
108	  "pass_f1": 0.92,
109	  "fail_precision": 1,
110	  "fail_recall": 0.56,
111	  "fail_f1": 0.72,
112	  "n_test": 1190,
113	  "train_loss": 0.0937,
114	  "eval_loss": 0.1859
115	}
116	
117	================================================================================
118	EXP_ID: codellama13b_full_trace_tail1024_seed42_v3
119	STATUS: DONE
120	CONCLUSION: success
121	MODEL_NAME: N/A
122	METRICS: {
123	  "accuracy_epoch1": 0.9824,
124	  "accuracy_epoch3": 0.9756,
125	  "pass_f1_epoch1": 0.988,
126	  "fail_f1_epoch1": 0.968,
127	  "pass_f1_epoch3": 0.983,
128	  "fail_f1_epoch3": 0.955,
129	  "best_accuracy": 0.9824,
130	  "best_epoch": 1,
131	  "overfitting": true
132	}
133	
134	================================================================================
135	EXP_ID: codellama13b_full_trace_tail2048_seed42
136	STATUS: DONE
137	CONCLUSION: failed
138	MODEL_NAME: CodeLlama-13b-Instruct-hf
139	METRICS: (none)
140	
141	================================================================================
142	EXP_ID: codellama13b_full_trace_tail2048_seed42_v2
143	STATUS: DONE
144	CONCLUSION: negative
145	MODEL_NAME: CodeLlama-13b-Instruct-hf
146	METRICS: {
147	  "accuracy_epoch1": 0.2849,
148	  "accuracy_epoch3": 0.2958,
149	  "pass_recall_epoch3": 0.016,
150	  "fail_recall_epoch3": 0.997,
151	  "majority_baseline": 0.715,
152	  "n_test": 1190,
153	  "note": "Catastrophic failure: model predicts fail for almost everything. Full-sequence loss dilution with CodeLlama tokenizer at 2048 tokens."
154	}
155	
156	================================================================================
157	EXP_ID: codellama13b_full_trace_tail2048_seed42_v3
158	STATUS: DONE
159	CONCLUSION: negative
160	MODEL_NAME: N/A
161	METRICS: {
162	  "accuracy_epoch1": 0.071,
163	  "accuracy_epoch3": 0.418,
164	  "pass_f1_epoch3": 0.416,
165	  "fail_f1_epoch3": 0.421,
166	  "pass_f1_epoch1": 0.035,
167	  "fail_f1_epoch1": 0.342,
168	  "train_loss": 0.785
169	}
170	
171	================================================================================
172	EXP_ID: codellama13b_full_trace_tail256_seed42
173	STATUS: DONE
174	CONCLUSION: success
175	MODEL_NAME: CodeLlama-13b-Instruct-hf
176	METRICS: {
177	  "accuracy": 0.779,
178	  "accuracy_ci_lower": 0.757,
179	  "accuracy_ci_upper": 0.803,
180	  "pass_f1": 0.843,
181	  "fail_f1": 0.626,
182	  "pass_precision": 0.856,
183	  "pass_recall": 0.831,
184	  "fail_precision": 0.604,
185	  "fail_recall": 0.649,
186	  "majority_baseline": 0.715,
187	  "lift": 0.064,
188	  "train_loss": 0.245,
189	  "eval_loss": 0.615
190	}
191	
192	================================================================================
193	EXP_ID: codellama13b_full_trace_tail384_seed42
194	STATUS: DONE
195	CONCLUSION: negative
196	MODEL_NAME: CodeLlama-13b-Instruct-hf
197	METRICS: {
198	  "accuracy": 0.8269,
199	  "accuracy_ci_lower": 0.8067,
200	  "accuracy_ci_upper": 0.8471,
201	  "majority_baseline": 0.7151,
202	  "lift": 0.1118,
203	  "n": 1190,
204	  "pass_precision": 0.8314,
205	  "pass_recall": 0.9506,
206	  "pass_f1": 0.8871,
207	  "fail_precision": 0.8065,
208	  "fail_recall": 0.5162,
209	  "fail_f1": 0.6295
210	}
211	
212	================================================================================
213	EXP_ID: codellama13b_full_trace_tail512_seed123
214	STATUS: DONE
215	CONCLUSION: success
216	MODEL_NAME: CodeLlama-13b-Instruct-hf
217	METRICS: {
218	  "accuracy": 0.9824,
219	  "accuracy_ci_lower": 0.9748,
220	  "accuracy_ci_upper": 0.9899,
221	  "majority_baseline": 0.7151,
222	  "lift": 0.2672,
223	  "n": 1190,
224	  "pass_precision": 0.9759,
225	  "pass_recall": 1,
226	  "pass_f1": 0.9878,
227	  "fail_precision": 1,
228	  "fail_recall": 0.9381,
229	  "fail_f1": 0.968,
230	  "seed_comparison": {
231	    "seed42_accuracy": 0.975,
232	    "seed123_accuracy": 0.9824,
233	    "diff": 0.0074,
234	    "note": "seed123 (98.24%) slightly exceeds seed42 (97.5%); both well above 97% \u2014 CodeLlama-13B tail-512 seed-robust"
235	  }
236	}
237	
238	================================================================================
239	EXP_ID: codellama13b_full_trace_tail512_seed42
240	STATUS: DONE
241	CONCLUSION: success
242	MODEL_NAME: N/A
243	METRICS: {
244	  "accuracy": 0.9824,
245	  "accuracy_ci_lower": 0.9748,
246	  "accuracy_ci_upper": 0.9899,
247	  "majority_baseline": 0.7151,
248	  "lift": 0.2672,
249	  "n": 1190,
250	  "pass_precision": 0.9759,
251	  "pass_recall": 1,
252	  "pass_f1": 0.9878,
253	  "fail_precision": 1,
254	  "fail_recall": 0.9381,
255	  "fail_f1": 0.968
256	}
257	
258	================================================================================
259	EXP_ID: codellama13b_full_trace_tail512_seed456
260	STATUS: DONE
261	CONCLUSION: success
262	MODEL_NAME: N/A
263	METRICS: {
264	  "accuracy": 0.9824,
265	  "accuracy_ci_lower": 0.9748,
266	  "accuracy_ci_upper": 0.9899,
267	  "majority_baseline": 0.7151,
268	  "lift": 0.2672,
269	  "n": 1190,
270	  "pass_precision": 0.9759,
271	  "pass_recall": 1,
272	  "pass_f1": 0.9878,
273	  "fail_precision": 1,
274	  "fail_recall": 0.9381,
275	  "fail_f1": 0.968,
276	  "seed_comparison": {
277	    "seed42_previous": 0.975,
278	    "seed123_accuracy": 0.9824,
279	    "seed456_accuracy": 0.9824
280	  }
281	}
282	
283	================================================================================
284	EXP_ID: codellama13b_loop_only_seed42
285	STATUS: DONE
286	CONCLUSION: negative
287	MODEL_NAME: N/A
288	METRICS: {
289	  "accuracy": 0.7706,
290	  "accuracy_ci_lower": 0.7487,
291	  "accuracy_ci_upper": 0.7941,
292	  "n": 1190,
293	  "majority_baseline": 0.7151,
294	  "lift": 0.0555,
295	  "fail_recall": 0.826,
296	  "pass_recall": 0.7485,
297	  "pass_precision": 0.92,
298	  "fail_precision": 0.57,
299	  "pass_f1": 0.82,
300	  "fail_f1": 0.67
301	}
302	
303	================================================================================
304	EXP_ID: codellama13b_no_trace_seed42
305	STATUS: DONE
306	CONCLUSION: success
307	MODEL_NAME: codellama/CodeLlama-13b-Instruct-hf
308	METRICS: {
309	  "accuracy": 0.765,
310	  "n": 1190,
311	  "majority_baseline": 0.7151,
312	  "lift": 0.05,
313	  "pass_precision": 0.84,
314	  "pass_recall": 0.83,
315	  "pass_f1": 0.84,
316	  "fail_precision": 0.59,
317	  "fail_recall": 0.59,
318	  "fail_f1": 0.59,
319	  "accuracy_ci_lower": 0.738,
320	  "accuracy_ci_upper": 0.787
321	}
322	
323	================================================================================
324	EXP_ID: codellama_exception_only_seed42
325	STATUS: DONE
326	CONCLUSION: killed
327	MODEL_NAME: CodeLlama-13b-Instruct-hf
328	METRICS: (none)
329	
330	================================================================================
331	EXP_ID: codellama_no_trace_seed42
332	STATUS: DONE
333	CONCLUSION: killed
334	MODEL_NAME: CodeLlama-13b-Instruct-hf
335	METRICS: (none)
336	
337	================================================================================
338	EXP_ID: debugbench_exception_only_seed42
339	STATUS: DONE
340	CONCLUSION: success
341	MODEL_NAME: N/A
342	METRICS: {
343	  "accuracy": 1,
344	  "majority_baseline": 0.5141,
345	  "lift": 0.4859,
346	  "n": 426,
347	  "pass_precision": 1,
348	  "pass_recall": 1,
349	  "pass_f1": 1,
350	  "fail_precision": 1,
351	  "fail_recall": 1,
352	  "fail_f1": 1,
353	  "accuracy_ci_wilson": [
354	    0.9914,
355	    1
356	  ],
357	  "accuracy_ci_bootstrap": [
358	    1,
359	    1
360	  ],
361	  "train_loss": 0.2435,
362	  "eval_loss": 0.4157,
363	  "train_runtime_sec": 837
364	}
365	
366	================================================================================
367	EXP_ID: debugbench_no_trace_seed42
368	STATUS: DONE
369	CONCLUSION: success
370	MODEL_NAME: Qwen/Qwen2.5-Coder-7B-Instruct
371	METRICS: {
372	  "accuracy": 0.9671,
373	  "majority_baseline": 0.5141,
374	  "lift": 0.4531,
375	  "pass_precision": 1,
376	  "pass_recall": 0.936,
377	  "pass_f1": 0.967,
378	  "fail_precision": 0.937,
379	  "fail_recall": 1,
380	  "fail_f1": 0.967,
381	  "accuracy_ci": [
382	    0.948,
383	    0.984
384	  ],
385	  "train_loss": 0.249,
386	  "eval_loss": 0.532
387	}
388	
389	================================================================================
390	EXP_ID: deepseek_ae_only_seed42
391	STATUS: DONE
392	CONCLUSION: success
393	MODEL_NAME: deepseek-ai/deepseek-coder-6.7b-instruct
394	METRICS: {
395	  "accuracy": 0.9874,
396	  "accuracy_ci_lower": 0.9807,
397	  "accuracy_ci_upper": 0.9933,
398	  "fail_recall": 0.959,
399	  "pass_recall": 0.999,
400	  "fail_f1": 0.977,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a04929f5-e085-44a2-ab99-0da20867c42f",
  "isSidechain": true,
  "promptId": "d3a99d3c-02c3-4d5e-9ec2-b28e1b492d4b",
  "agentId": "a86b080f191dc2217",
  "type": "user",
  "uuid": "8c4ee783-3e2f-41e1-9542-ac744fc5b14a",
  "sourceToolAssistantUUID": "a04929f5-e085-44a2-ab99-0da20867c42f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "f5f4efcf-b091-4929-abdf-35aa1152d6be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T19:05:03.813Z_

<details open><summary>🔧 Tool call — Read · `toolu_015bqJWc321q6Y7GcqL2W1ov`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/f5f4efcf-b091-4929-abdf-35aa1152d6be/tool-results/b7t9ioqmo.txt",
  "offset": 400,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c4ee783-3e2f-41e1-9542-ac744fc5b14a",
  "isSidechain": true,
  "agentId": "a86b080f191dc2217",
  "requestId": "req_011CbGEcNuuX5xvNT7AyAtrJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b438d440-dddb-479d-b197-0ab4cb6a91cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "f5f4efcf-b091-4929-abdf-35aa1152d6be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CmKeGcu6rix4H9sXsVcRPC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4978,
      "cache_read_input_tokens": 21857,
      "output_tokens": 165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4978
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 165,
          "cache_read_input_tokens": 21857,
          "cache_creation_input_tokens": 4978,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4978,
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

_source line 23 · 2026-05-21T19:05:03.819Z_

<details><summary>↩ Tool result · `toolu_015bqJWc321q6Y7GcqL2W1ov`</summary>

```text
400	  "fail_f1": 0.977,
401	  "pass_f1": 0.991
402	}
403	
404	================================================================================
405	EXP_ID: deepseek_exception_only_seed123
406	STATUS: DONE
407	CONCLUSION: killed
408	MODEL_NAME: N/A
409	METRICS: (none)
410	
411	================================================================================
412	EXP_ID: deepseek_exception_only_seed123_v2
413	STATUS: DONE
414	CONCLUSION: success
415	MODEL_NAME: deepseek-ai/deepseek-coder-6.7b-instruct
416	METRICS: {
417	  "accuracy": 0.995
418	}
419	
420	================================================================================
421	EXP_ID: deepseek_exception_only_seed42
422	STATUS: DONE
423	CONCLUSION: success
424	MODEL_NAME: deepseek-ai/deepseek-coder-6.7b-instruct
425	METRICS: {
426	  "accuracy": 0.9933,
427	  "majority_baseline": 0.7151,
428	  "lift": 0.2782,
429	  "n": 1190,
430	  "pass_precision": 1,
431	  "pass_recall": 0.9906,
432	  "pass_f1": 0.9953,
433	  "fail_precision": 0.9769,
434	  "fail_recall": 1,
435	  "fail_f1": 0.9883,
436	  "epoch1_checkpoint_eval": {
437	    "accuracy": 0.9983,
438	    "fail_recall": 1,
439	    "fail_precision": 0.9941,
440	    "pass_recall": 0.9976,
441	    "conclusion": "epoch1_better_by_0.50pp"
442	  }
443	}
444	
445	================================================================================
446	EXP_ID: deepseek_exception_only_seed456
447	STATUS: DONE
448	CONCLUSION: success
449	MODEL_NAME: deepseek-ai/deepseek-coder-6.7b-instruct
450	METRICS: {
451	  "accuracy": 0.9933,
452	  "majority_baseline": 0.7151,
453	  "lift": 0.2782,
454	  "n": 1190,
455	  "pass_precision": 1,
456	  "pass_recall": 0.9906,
457	  "pass_f1": 0.9953,
458	  "fail_precision": 0.9769,
459	  "fail_recall": 1,
460	  "fail_f1": 0.9883,
461	  "accuracy_ci": [
462	    0.9882,
463	    0.9975
464	  ],
465	  "train_loss": 0.1225,
466	  "eval_loss": 0.4824,
467	  "train_runtime_sec": 6246,
468	  "seed_comparison": {
469	    "seed42_accuracy": 0.9933,
470	    "seed456_accuracy": 0.9933,
471	    "seed123_accuracy": 0.9109,
472	    "note": "seed42 and seed456 identical (99.33%); seed123 outlier (91.09%). 2/3 seeds robust."
473	  },
474	  "epoch1_checkpoint_eval": {
475	    "accuracy": 0.993,
476	    "accuracy_ci": [
477	      0.988,
478	      0.997
479	    ],
480	    "fail_f1": 0.99,
481	    "fail_precision": 0.98,
482	    "fail_recall": 1,
483	    "pass_f1": 1,
484	    "pass_precision": 1,
485	    "pass_recall": 0.99,
486	    "conclusion": "epoch1 (99.3%) \u2248 epoch3 (99.33%), 1 epoch convergence confirmed"
487	  }
488	}
489	
490	================================================================================
491	EXP_ID: deepseek_full_trace_head2048_seed42
492	STATUS: DONE
493	CONCLUSION: success
494	MODEL_NAME: deepseek-coder-6.7b-instruct
495	METRICS: {
496	  "accuracy": 0.787,
497	  "accuracy_ci_lower": 0.765,
498	  "accuracy_ci_upper": 0.81,
499	  "majority_baseline": 0.715,
500	  "lift_pp": 7.2,
501	  "pass_precision": 0.84,
502	  "pass_recall": 0.86,
503	  "pass_f1": 0.85,
504	  "fail_precision": 0.63,
505	  "fail_recall": 0.6,
506	  "fail_f1": 0.62
507	}
508	
509	================================================================================
510	EXP_ID: deepseek_full_trace_seed42
511	STATUS: DONE
512	CONCLUSION: negative
513	MODEL_NAME: deepseek-ai/deepseek-coder-6.7b-instruct
514	METRICS: {
515	  "accuracy_no_truncation": 0.2849,
516	  "accuracy_with_truncation_fix": 0.1059,
517	  "accuracy_with_truncation_fix_ci": [
518	    0.089,
519	    0.123
520	  ],
521	  "majority_baseline": 0.7151,
522	  "n": 1190,
523	  "note": "Both evals show model failure. No-truncation: all predict fail. With-truncation: garbage tokens. LoRA training itself failed due to label truncation during training."
524	}
525	
526	================================================================================
527	EXP_ID: deepseek_full_trace_seed42_v2
528	STATUS: DONE
529	CONCLUSION: killed
530	MODEL_NAME: deepseek-ai/deepseek-coder-6.7b-instruct
531	METRICS: (none)
532	
533	================================================================================
534	EXP_ID: deepseek_full_trace_seed42_v3
535	STATUS: DONE
536	CONCLUSION: success
537	MODEL_NAME: deepseek-ai/deepseek-coder-6.7b-instruct
538	METRICS: {
539	  "accuracy": 0.7916,
540	  "majority_baseline": 0.7151,
541	  "lift": 0.0765,
542	  "n": 1190,
543	  "pass_precision": 0.857,
544	  "pass_recall": 0.851,
545	  "pass_f1": 0.854,
546	  "fail_precision": 0.632,
547	  "fail_recall": 0.643,
548	  "fail_f1": 0.637,
549	  "accuracy_ci": [
550	    0.768,
551	    0.813
552	  ],
553	  "train_loss": 0.0547,
554	  "train_runtime_seconds": 8891,
555	  "epochs": 3,
556	  "reeval_discrepancy": {
557	    "reeval_accuracy": 0.285,
558	    "reeval_note": "RESOLVED: 28.5% was caused by eval max_length=16384 (OOD). Re-eval with max_length=2048 reproduces 79.16%. predictions.jsonl updated to maxlen2048 results.",
559	    "status": "RESOLVED"
560	  }
561	}
562	
563	================================================================================
564	EXP_ID: deepseek_full_trace_tail1024_seed42
565	STATUS: DONE
566	CONCLUSION: success
567	MODEL_NAME: N/A
568	METRICS: {
569	  "accuracy": 0.9647,
570	  "accuracy_ci_lower": 0.9538,
571	  "accuracy_ci_upper": 0.9748,
572	  "pass_precision": 0.964,
573	  "pass_recall": 0.987,
574	  "pass_f1": 0.976,
575	  "fail_precision": 0.966,
576	  "fail_recall": 0.909,
577	  "fail_f1": 0.936,
578	  "majority_baseline": 0.7151,
579	  "n_test": 1190
580	}
581	
582	================================================================================
583	EXP_ID: deepseek_full_trace_tail2048_seed42
584	STATUS: DONE
585	CONCLUSION: success
586	MODEL_NAME: DeepSeek-Coder-6.7B-Instruct
587	METRICS: {
588	  "accuracy": 0.9496,
589	  "accuracy_ci_lower": 0.937,
590	  "accuracy_ci_upper": 0.9622,
591	  "pass_precision": 0.9692,
592	  "pass_recall": 0.96,
593	  "pass_f1": 0.9646,
594	  "fail_precision": 0.902,
595	  "fail_recall": 0.9233,
596	  "fail_f1": 0.9125,
597	  "n_test": 1190
598	}
599	
600	================================================================================
601	EXP_ID: deepseek_full_trace_tail256_seed42
602	STATUS: DONE
603	CONCLUSION: success
604	MODEL_NAME: deepseek-coder-6.7b-instruct
605	METRICS: {
606	  "accuracy": 0.7639,
607	  "accuracy_ci_lower": 0.7403,
608	  "accuracy_ci_upper": 0.7874,
609	  "pass_precision": 0.8058,
610	  "pass_recall": 0.8825,
611	  "pass_f1": 0.8424,
612	  "fail_precision": 0.6124,
613	  "fail_recall": 0.4661,
614	  "fail_f1": 0.5293,
615	  "majority_baseline": 0.7151,
616	  "lift": 0.0487,
617	  "eval_loss": 0.5117,
618	  "train_loss": 0.2367
619	}
620	
621	================================================================================
622	EXP_ID: deepseek_full_trace_tail384_seed42
623	STATUS: DONE
624	CONCLUSION: success
625	MODEL_NAME: deepseek-coder-6.7b-instruct
626	METRICS: {
627	  "accuracy": 0.807,
628	  "accuracy_ci_lower": 0.786,
629	  "accuracy_ci_upper": 0.829,
630	  "majority_baseline": 0.715,
631	  "lift": 0.092,
632	  "n": 1190,
633	  "pass_precision": 0.83,
634	  "pass_recall": 0.92,
635	  "pass_f1": 0.87,
636	  "fail_precision": 0.73,
637	  "fail_recall": 0.51,
638	  "fail_f1": 0.6
639	}
640	
641	================================================================================
642	EXP_ID: deepseek_full_trace_tail512_seed123
643	STATUS: DONE
644	CONCLUSION: failed
645	MODEL_NAME: N/A
646	METRICS: {
647	  "error": "CUDA OOM at step 0/444",
648	  "exit_code": 1,
649	  "failure_time": "2026-05-18T15:49:48Z",
650	  "cause": "GPU 0 memory exhausted (43.45 GiB PyTorch allocated, only 167.56 MiB free when trying to allocate 178 MiB)",
651	  "seed_comparison": {
652	    "seed42_accuracy": 0.9361,
653	    "seed123_accuracy": "N/A - OOM crash"
654	  }
655	}
656	
657	================================================================================
658	EXP_ID: deepseek_full_trace_tail512_seed123_v2
659	STATUS: DONE
660	CONCLUSION: success
661	MODEL_NAME: deepseek-coder-6.7b-instruct
662	METRICS: {
663	  "accuracy": 0.9504,
664	  "majority_baseline": 0.7151,
665	  "lift": 0.2353,
666	  "n": 1190,
667	  "pass_precision": 0.976,
668	  "pass_recall": 0.9542,
669	  "pass_f1": 0.9649,
670	  "fail_precision": 0.8911,
671	  "fail_recall": 0.941,
672	  "fail_f1": 0.9154,
673	  "accuracy_ci": [
674	    0.9387,
675	    0.963
676	  ]
677	}
678	
679	================================================================================
680	EXP_ID: deepseek_full_trace_tail512_seed42
681	STATUS: DONE
682	CONCLUSION: success
683	MODEL_NAME: deepseek-coder-6.7b-instruct
684	METRICS: {
685	  "accuracy": 0.939,
686	  "accuracy_ci_lower": 0.926,
687	  "accuracy_ci_upper": 0.953,
688	  "majority_baseline": 0.715,
689	  "lift_over_majority": 0.224,
690	  "pass_precision": 0.97,
691	  "pass_recall": 0.94,
692	  "pass_f1": 0.96,
693	  "fail_precision": 0.86,
694	  "fail_recall": 0.94,
695	  "fail_f1": 0.9,
696	  "n_test": 1190
697	}
698	
699	================================================================================
700	EXP_ID: deepseek_full_trace_tail512_seed456
701	STATUS: DONE
702	CONCLUSION: success
703	MODEL_NAME: N/A
704	METRICS: {
705	  "accuracy": 0.9605,
706	  "accuracy_ci_lower": 0.9496,
707	  "accuracy_ci_upper": 0.9714,
708	  "majority_baseline": 0.7151,
709	  "lift": 0.2454,
710	  "n": 1190,
711	  "pass_precision": 0.9752,
712	  "pass_recall": 0.9694,
713	  "pass_f1": 0.9723,
714	  "fail_precision": 0.9244,
715	  "fail_recall": 0.9381,
716	  "fail_f1": 0.9312,
717	  "seed_comparison": {
718	    "seed42_accuracy": 0.9361,
719	    "seed456_accuracy": 0.9605
720	  }
721	}
722	
723	================================================================================
724	EXP_ID: deepseek_loop_only_seed42
725	STATUS: DONE
726	CONCLUSION: success
727	MODEL_NAME: deepseek-ai/deepseek-coder-6.7b-instruct
728	METRICS: {
729	  "accuracy": 0.8126,
730	  "accuracy_ci_lower": 0.7908,
731	  "accuracy_ci_upper": 0.8345,
732	  "fail_recall": 0.6372,
733	  "pass_recall": 0.8825
734	}
735	
736	================================================================================
737	EXP_ID: deepseek_no_trace_seed123
738	STATUS: DONE
739	CONCLUSION: killed
740	MODEL_NAME: N/A
741	METRICS: (none)
742	
743	================================================================================
744	EXP_ID: deepseek_no_trace_seed42
745	STATUS: DONE
746	CONCLUSION: negative
747	MODEL_NAME: deepseek-ai/deepseek-coder-6.7b-instruct
748	METRICS: {
749	  "accuracy": 0.7336,
750	  "majority_baseline": 0.7151,
751	  "lift": 0.0185,
752	  "n": 1190,
753	  "pass_precision": 0.817,
754	  "pass_recall": 0.808,
755	  "pass_f1": 0.813,
756	  "fail_precision": 0.532,
757	  "fail_recall": 0.546,
758	  "fail_f1": 0.539,
759	  "accuracy_ci": [
760	    0.708,
761	    0.757
762	  ],
763	  "lift_ci": [
764	    -0.009,
765	    0.046
766	  ]
767	}
768	
769	================================================================================
770	EXP_ID: exception_only_nomarker_seed123
771	STATUS: DONE
772	CONCLUSION: success
773	MODEL_NAME: Qwen2.5-Coder-7B-Instruct
774	METRICS: {
775	  "accuracy": 0.9832,
776	  "n": 1190,
777	  "ci_95": [
778	    0.9756,
779	    0.9899
780	  ],
781	  "pass_f1": 0.9882,
782	  "fail_f1": 0.9705,
783	  "pass_precision": 0.9882,
784	  "pass_recall": 0.9882,
785	  "fail_precision": 0.9705,
786	  "fail_recall": 0.9705,
787	  "lift_over_majority": 0.2681
788	}
789	
790	================================================================================
791	EXP_ID: exception_only_nomarker_seed42
792	STATUS: DONE
793	CONCLUSION: success
794	MODEL_NAME: Qwen2.5-Coder-7B-Instruct
795	METRICS: {
796	  "accuracy": 0.9655,
797	  "n": 1190,
798	  "accuracy_ci": [
799	    0.955,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b438d440-dddb-479d-b197-0ab4cb6a91cc",
  "isSidechain": true,
  "promptId": "d3a99d3c-02c3-4d5e-9ec2-b28e1b492d4b",
  "agentId": "a86b080f191dc2217",
  "type": "user",
  "uuid": "59145f42-3069-4dde-ae14-2108c28c0a44",
  "sourceToolAssistantUUID": "b438d440-dddb-479d-b197-0ab4cb6a91cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "f5f4efcf-b091-4929-abdf-35aa1152d6be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T19:05:09.582Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Rj7KL8dtqGKPh4WawnGSFF`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/f5f4efcf-b091-4929-abdf-35aa1152d6be/tool-results/b7t9ioqmo.txt",
  "offset": 800,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59145f42-3069-4dde-ae14-2108c28c0a44",
  "isSidechain": true,
  "agentId": "a86b080f191dc2217",
  "requestId": "req_011CbGEcoq7CBfWQiWEBeLzU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18c25535-7f8e-4013-9921-833b0201e8b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "f5f4efcf-b091-4929-abdf-35aa1152d6be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FzzmopVFEnx83iP73o1hE2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5010,
      "cache_read_input_tokens": 26835,
      "output_tokens": 165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5010
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 165,
          "cache_read_input_tokens": 26835,
          "cache_creation_input_tokens": 5010,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5010,
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

_source line 25 · 2026-05-21T19:05:09.605Z_

<details><summary>↩ Tool result · `toolu_01Rj7KL8dtqGKPh4WawnGSFF`</summary>

```text
800	    0.976
801	  ]
802	}
803	
804	================================================================================
805	EXP_ID: exception_only_nomarker_seed456
806	STATUS: DONE
807	CONCLUSION: success
808	MODEL_NAME: Qwen2.5-Coder-7B-Instruct
809	METRICS: {
810	  "accuracy": 0.9807,
811	  "n": 1190,
812	  "errors": 23,
813	  "ci_95": [
814	    0.9712,
815	    0.9871
816	  ],
817	  "pass_f1": 0.9865,
818	  "fail_f1": 0.9658,
819	  "pass_precision": 0.9836,
820	  "pass_recall": 0.9894,
821	  "fail_precision": 0.9731,
822	  "fail_recall": 0.9587,
823	  "lift_over_majority": 0.266
824	}
825	
826	================================================================================
827	EXP_ID: exception_only_padded2048_seed42
828	STATUS: RUNNING
829	CONCLUSION: N/A
830	MODEL_NAME: Qwen2.5-Coder-7B-Instruct
831	METRICS: (none)
832	
833	================================================================================
834	EXP_ID: exception_only_seed123
835	STATUS: DONE
836	CONCLUSION: success
837	MODEL_NAME: Qwen2.5-Coder-7B-Instruct
838	METRICS: {
839	  "accuracy": 0.9983,
840	  "accuracy_ci": [
841	    0.9958,
842	    1
843	  ],
844	  "majority_baseline": 0.7151,
845	  "lift": 0.2832,
846	  "n": 1190,
847	  "pass_precision": 1,
848	  "pass_recall": 0.9976,
849	  "pass_f1": 0.9988,
850	  "fail_precision": 0.9941,
851	  "fail_recall": 1,
852	  "fail_f1": 0.9971,
853	  "train_loss": 0.1096,
854	  "train_runtime_sec": 7507,
855	  "epochs": 3,
856	  "seed_comparison": {
857	    "seed42_accuracy": 0.9983,
858	    "seed456_accuracy": 0.9983,
859	    "seed123_accuracy": 0.9983,
860	    "max_diff": 0,
861	    "note": "identical accuracy to 4 decimal places across all 3 seeds (42/456/123); each has exactly 2/1190 errors; exception_only fully seed-robust"
862	  }
863	}
864	
865	================================================================================
866	EXP_ID: exception_only_seed456
867	STATUS: DONE
868	CONCLUSION: success
869	MODEL_NAME: Qwen2.5-Coder-7B-Instruct
870	METRICS: {
871	  "accuracy": 0.9983,
872	  "accuracy_ci": [
873	    0.9958,
874	    1
875	  ],
876	  "majority_baseline": 0.7151,
877	  "lift": 0.2832,
878	  "n": 1190,
879	  "pass_precision": 1,
880	  "pass_recall": 0.9976,
881	  "pass_f1": 0.9988,
882	  "fail_precision": 0.9941,
883	  "fail_recall": 1,
884	  "fail_f1": 0.9971,
885	  "vs_seed42": {
886	    "seed42_accuracy": 0.9983,
887	    "seed456_accuracy": 0.9983,
888	    "diff": 0,
889	    "note": "identical accuracy to 4 decimal places; no predictions.jsonl for paired bootstrap"
890	  },
891	  "train_loss": 0.1087,
892	  "eval_loss": 0.4629,
893	  "train_runtime_sec": 4541,
894	  "epochs": 3
895	}
896	
897	================================================================================
898	EXP_ID: fewshot_gpt41_exception_only_0shot
899	STATUS: DONE
900	CONCLUSION: negative
901	MODEL_NAME: gpt-4.1
902	METRICS: {
903	  "accuracy": 0.8218,
904	  "fail_f1": 0.7452
905	}
906	
907	================================================================================
908	EXP_ID: fewshot_gpt41_exception_only_3shot
909	STATUS: DONE
910	CONCLUSION: negative
911	MODEL_NAME: gpt-4.1
912	METRICS: {
913	  "accuracy": 0.8193,
914	  "fail_f1": 0.7413
915	}
916	
917	================================================================================
918	EXP_ID: fewshot_gpt41_no_trace_0shot
919	STATUS: DONE
920	CONCLUSION: success
921	MODEL_NAME: gpt-4.1
922	METRICS: {
923	  "accuracy": 0.7731,
924	  "fail_f1": 0.6608
925	}
926	
927	================================================================================
928	EXP_ID: fewshot_gpt4o_exception_only_0shot
929	STATUS: DONE
930	CONCLUSION: negative
931	MODEL_NAME: gpt-4o
932	METRICS: {
933	  "accuracy": 0.8798,
934	  "fail_f1": 0.8228
935	}
936	
937	================================================================================
938	EXP_ID: fewshot_gpt4o_exception_only_3shot
939	STATUS: DONE
940	CONCLUSION: negative
941	MODEL_NAME: gpt-4o
942	METRICS: {
943	  "accuracy": 0.8681,
944	  "fail_f1": 0.7995
945	}
946	
947	================================================================================
948	EXP_ID: fewshot_gpt4o_no_trace_0shot
949	STATUS: DONE
950	CONCLUSION: success
951	MODEL_NAME: gpt-4o
952	METRICS: {
953	  "accuracy": 0.8445,
954	  "fail_f1": 0.7543
955	}
956	
957	================================================================================
958	EXP_ID: fewshot_qwen7b_exception_only
959	STATUS: DONE
960	CONCLUSION: success
961	MODEL_NAME: Qwen2.5-Coder-7B-Instruct
962	METRICS: {
963	  "accuracy": 0.9084,
964	  "accuracy_ci_lower": 0.8908,
965	  "accuracy_ci_upper": 0.9244,
966	  "pass_precision": 0.9245,
967	  "pass_recall": 0.9495,
968	  "pass_f1": 0.9368,
969	  "fail_precision": 0.8639,
970	  "fail_recall": 0.8053,
971	  "fail_f1": 0.8336,
972	  "n_test": 1190,
973	  "n_unknown": 0
974	}
975	
976	================================================================================
977	EXP_ID: full_trace_1024tok_seed42
978	STATUS: DONE
979	CONCLUSION: negative
980	MODEL_NAME: Qwen/Qwen2.5-Coder-7B-Instruct
981	METRICS: {
982	  "accuracy": 0.7723,
983	  "majority_baseline": 0.7151,
984	  "lift": 0.0571,
985	  "n": 1190,
986	  "accuracy_ci": [
987	    0.7487,
988	    0.7958
989	  ],
990	  "pass_precision": 0.9006,
991	  "pass_recall": 0.7662,
992	  "pass_f1": 0.8279,
993	  "fail_precision": 0.573,
994	  "fail_recall": 0.7876,
995	  "fail_f1": 0.6634,
996	  "train_loss": 0.0634,
997	  "train_runtime_sec": 5553,
998	  "epochs": 3
999	}
1000	
1001	================================================================================
1002	EXP_ID: full_trace_2048tok_seed42
1003	STATUS: DONE
1004	CONCLUSION: killed
1005	MODEL_NAME: N/A
1006	METRICS: (none)
1007	
1008	================================================================================
1009	EXP_ID: full_trace_256tok_seed42
1010	STATUS: DONE
1011	CONCLUSION: negative
1012	MODEL_NAME: Qwen/Qwen2.5-Coder-7B-Instruct
1013	METRICS: {
1014	  "accuracy": 0.7882,
1015	  "majority_baseline": 0.7151,
1016	  "lift": 0.0731,
1017	  "n": 1190,
1018	  "pass_precision": 0.903,
1019	  "pass_recall": 0.788,
1020	  "pass_f1": 0.842,
1021	  "fail_precision": 0.597,
1022	  "fail_recall": 0.788,
1023	  "fail_f1": 0.679,
1024	  "accuracy_ci": [
1025	    0.764,
1026	    0.81
1027	  ],
1028	  "train_loss": 0.1094,
1029	  "train_runtime_sec": 3047,
1030	  "epochs": 3
1031	}
1032	
1033	================================================================================
1034	EXP_ID: full_trace_512tok_seed42
1035	STATUS: DONE
1036	CONCLUSION: negative
1037	MODEL_NAME: Qwen/Qwen2.5-Coder-7B-Instruct
1038	METRICS: {
1039	  "accuracy": 0.8042,
1040	  "majority_baseline": 0.7151,
1041	  "lift": 0.0891,
1042	  "pass_precision": 0.8705,
1043	  "pass_recall": 0.8531,
1044	  "pass_f1": 0.8617,
1045	  "fail_precision": 0.6489,
1046	  "fail_recall": 0.6814,
1047	  "fail_f1": 0.6647,
1048	  "n": 1190,
1049	  "accuracy_ci": [
1050	    0.7815,
1051	    0.8261
1052	  ]
1053	}
1054	
1055	================================================================================
1056	EXP_ID: full_trace_label_only_seed42
1057	STATUS: DONE
1058	CONCLUSION: success
1059	MODEL_NAME: N/A
1060	METRICS: {
1061	  "accuracy": 0.8622,
1062	  "accuracy_ci_lower": 0.8437,
1063	  "accuracy_ci_upper": 0.8807,
1064	  "majority_baseline": 0.7151,
1065	  "lift": 0.1471,
1066	  "n": 1190,
1067	  "pass_precision": 0.8821,
1068	  "pass_recall": 0.9318,
1069	  "pass_f1": 0.9063,
1070	  "fail_precision": 0.8007,
1071	  "fail_recall": 0.6873,
1072	  "fail_f1": 0.7397,
1073	  "train_loss": 0.2505,
1074	  "eval_loss": 0.3205,
1075	  "lift_vs_notrace": 0.1109,
1076	  "lift_vs_notrace_ci_lower": 0.0849,
1077	  "lift_vs_notrace_ci_upper": 0.137,
1078	  "lift_vs_standard_fulltrace": 0.0445,
1079	  "lift_vs_standard_fulltrace_ci_lower": 0.0235,
1080	  "lift_vs_standard_fulltrace_ci_upper": 0.0655,
1081	  "lift_vs_standard_fulltrace_pvalue": 0
1082	}
1083	
1084	================================================================================
1085	EXP_ID: full_trace_seed42
1086	STATUS: DONE
1087	CONCLUSION: killed
1088	MODEL_NAME: Qwen2.5-Coder-7B-Instruct
1089	METRICS: {
1090	  "train_loss": 0.037,
1091	  "eval_loss": 0.084,
1092	  "eval_mean_token_accuracy": 0.984,
1093	  "accuracy": 0.284,
1094	  "majority_baseline": 0.7151,
1095	  "lift": -0.431,
1096	  "pass_precision": 0.88,
1097	  "pass_recall": 0.08,
1098	  "pass_f1": 0.16,
1099	  "fail_precision": 0.31,
1100	  "fail_recall": 0.97,
1101	  "fail_f1": 0.57
1102	}
1103	
1104	================================================================================
1105	EXP_ID: full_trace_seed42_v2
1106	STATUS: DONE
1107	CONCLUSION: negative
1108	MODEL_NAME: N/A
1109	METRICS: {
1110	  "accuracy": 0.284,
1111	  "majority_baseline": 0.7151,
1112	  "lift": -0.4311,
1113	  "n": 1190,
1114	  "pass_precision": 0.923,
1115	  "pass_recall": 0.085,
1116	  "pass_f1": 0.155,
1117	  "fail_precision": 0.445,
1118	  "fail_recall": 0.785,
1119	  "fail_f1": 0.568,
1120	  "train_loss": 0.0373,
1121	  "eval_loss": 0.082,
1122	  "eval_mean_token_accuracy": 0.984
1123	}
1124	
1125	================================================================================
1126	EXP_ID: full_trace_seed42_v5
1127	STATUS: DONE
1128	CONCLUSION: success
1129	MODEL_NAME: N/A
1130	METRICS: {
1131	  "accuracy": 0.8176,
1132	  "majority_baseline": 0.7151,
1133	  "lift": 0.1025,
1134	  "n": 1190,
1135	  "pass_precision": 0.8774,
1136	  "pass_recall": 0.866,
1137	  "pass_f1": 0.8717,
1138	  "fail_precision": 0.6743,
1139	  "fail_recall": 0.6962,
1140	  "fail_f1": 0.6851,
1141	  "accuracy_ci_lower": 0.797,
1142	  "accuracy_ci_upper": 0.839,
1143	  "lift_vs_notrace": 0.0664,
1144	  "lift_vs_notrace_ci_lower": 0.0437,
1145	  "lift_vs_notrace_ci_upper": 0.0899,
1146	  "train_loss": 0.05,
1147	  "eval_loss": 0.0867,
1148	  "wall_clock_seconds": 7852,
1149	  "epoch_level": {
1150	    "epoch1_accuracy": 0.8303,
1151	    "epoch2_accuracy": 0.763,
1152	    "final_accuracy": 0.8176,
1153	    "trend": "non_monotonic_epoch1_best_epoch2_collapse"
1154	  }
1155	}
1156	
1157	================================================================================
1158	EXP_ID: full_trace_tail256_seed42
1159	STATUS: DONE
1160	CONCLUSION: negative
1161	MODEL_NAME: Qwen2.5-Coder-7B-Instruct
1162	METRICS: {
1163	  "accuracy": 0.789,
1164	  "accuracy_ci_lower": 0.765,
1165	  "accuracy_ci_upper": 0.813,
1166	  "pass_f1": 0.845,
1167	  "fail_f1": 0.671,
1168	  "n_test": 1190
1169	}
1170	
1171	================================================================================
1172	EXP_ID: full_trace_tail_1024_seed42
1173	STATUS: DONE
1174	CONCLUSION: success
1175	MODEL_NAME: Qwen2.5-Coder-7B-Instruct
1176	METRICS: {
1177	  "accuracy": 0.9647,
1178	  "accuracy_ci": [
1179	    0.9546,
1180	    0.9748
1181	  ],
1182	  "majority_baseline": 0.7151,
1183	  "lift": 0.2496,
1184	  "n": 1190,
1185	  "pass_f1": 0.9753,
1186	  "fail_f1": 0.9381
1187	}
1188	
1189	================================================================================
1190	EXP_ID: full_trace_tail_256_seed42
1191	STATUS: DONE
1192	CONCLUSION: negative
1193	MODEL_NAME: Qwen2.5-Coder-7B-Instruct
1194	METRICS: {
1195	  "accuracy": 0.7748,
1196	  "accuracy_ci": [
1197	    0.7496,
1198	    0.7975
1199	  ],
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18c25535-7f8e-4013-9921-833b0201e8b3",
  "isSidechain": true,
  "promptId": "d3a99d3c-02c3-4d5e-9ec2-b28e1b492d4b",
  "agentId": "a86b080f191dc2217",
  "type": "user",
  "uuid": "31b9542e-cc34-4641-ac13-446d16a2df40",
  "sourceToolAssistantUUID": "18c25535-7f8e-4013-9921-833b0201e8b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "f5f4efcf-b091-4929-abdf-35aa1152d6be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-21T19:05:15.470Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UzvkEiaw2GDpBMYLkRm8fR`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/f5f4efcf-b091-4929-abdf-35aa1152d6be/tool-results/b7t9ioqmo.txt",
  "offset": 1200,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31b9542e-cc34-4641-ac13-446d16a2df40",
  "isSidechain": true,
  "agentId": "a86b080f191dc2217",
  "requestId": "req_011CbGEdEWRE3s9b4RD3q8FX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "925a3cde-239a-4740-a25e-f3da147f239d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "f5f4efcf-b091-4929-abdf-35aa1152d6be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TYuMCzS7NmeeTGTzjNThjB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5019,
      "cache_read_input_tokens": 31845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5019,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 27 · 2026-05-21T19:05:15.480Z_

<details><summary>↩ Tool result · `toolu_01UzvkEiaw2GDpBMYLkRm8fR`</summary>

```text
1200	  "majority_baseline": 0.7151,
1201	  "lift": 0.0597,
1202	  "n": 1190,
1203	  "pass_f1": 0.8333,
1204	  "fail_f1": 0.6528
1205	}
1206	
1207	================================================================================
1208	EXP_ID: full_trace_tail_512_seed42
1209	STATUS: DONE
1210	CONCLUSION: success
1211	MODEL_NAME: Qwen/Qwen2.5-Coder-7B-Instruct
1212	METRICS: {
1213	  "accuracy": 0.936,
1214	  "accuracy_ci": [
1215	    0.922,
1216	    0.95
1217	  ],
1218	  "majority_baseline": 0.7151,
1219	  "lift": 0.221,
1220	  "n": 1190,
1221	  "pass_precision": 0.98,
1222	  "pass_recall": 0.93,
1223	  "pass_f1": 0.95,
1224	  "fail_precision": 0.85,
1225	  "fail_recall": 0.94,
1226	  "fail_f1": 0.89
1227	}
1228	
1229	================================================================================
1230	EXP_ID: full_trace_tail_seed42
1231	STATUS: DONE
1232	CONCLUSION: success
1233	MODEL_NAME: Qwen/Qwen2.5-Coder-7B-Instruct
1234	METRICS: {
1235	  "accuracy": 0.973,
1236	  "accuracy_ci": [
1237	    0.964,
1238	    0.982
1239	  ],
1240	  "majority_baseline": 0.7151,
1241	  "lift": 0.258,
1242	  "n": 1190,
1243	  "pass_precision": 0.98,
1244	  "pass_recall": 0.99,
1245	  "pass_f1": 0.98,
1246	  "fail_precision": 0.97,
1247	  "fail_recall": 0.94,
1248	  "fail_f1": 0.95
1249	}
1250	
1251	================================================================================
1252	EXP_ID: no_trace_seed42
1253	STATUS: DONE
1254	CONCLUSION: killed
1255	MODEL_NAME: N/A
1256	METRICS: (none)
1257	
1258	================================================================================
1259	EXP_ID: no_trace_seed42_v2
1260	STATUS: DONE
1261	CONCLUSION: killed
1262	MODEL_NAME: N/A
1263	METRICS: (none)
1264	
1265	================================================================================
1266	EXP_ID: no_trace_seed42_v3
1267	STATUS: DONE
1268	CONCLUSION: killed
1269	MODEL_NAME: Qwen2.5-Coder-7B-Instruct
1270	METRICS: {
1271	  "train_loss": 0.18,
1272	  "eval_loss": 0.645,
1273	  "eval_mean_token_accuracy": 0.89,
1274	  "accuracy": 0.7513,
1275	  "majority_baseline": 0.7151,
1276	  "lift": 0.0361,
1277	  "pass_precision": 0.8776,
1278	  "pass_recall": 0.7579,
1279	  "pass_f1": 0.8134,
1280	  "fail_precision": 0.5473,
1281	  "fail_recall": 0.7345,
1282	  "fail_f1": 0.6272
1283	}
1284	
1285	================================================================================
1286	EXP_ID: no_trace_seed42_v4
1287	STATUS: DONE
1288	CONCLUSION: success
1289	MODEL_NAME: N/A
1290	METRICS: {
1291	  "accuracy": 0.7513,
1292	  "majority_baseline": 0.7151,
1293	  "lift": 0.0361,
1294	  "pass_precision": 0.8776,
1295	  "pass_recall": 0.7579,
1296	  "pass_f1": 0.8134,
1297	  "fail_precision": 0.5473,
1298	  "fail_recall": 0.7345,
1299	  "fail_f1": 0.6272,
1300	  "train_loss": 0.18,
1301	  "eval_loss": 0.6454,
1302	  "eval_mean_token_accuracy": 0.8897
1303	}
1304	
1305	================================================================================
1306	EXP_ID: no_trace_seed42_v5
1307	STATUS: DONE
1308	CONCLUSION: success
1309	MODEL_NAME: Qwen2.5-Coder-7B-Instruct
1310	METRICS: {
1311	  "accuracy": 0.7513,
1312	  "accuracy_ci_lower": 0.7277,
1313	  "accuracy_ci_upper": 0.7748,
1314	  "majority_baseline": 0.7151,
1315	  "lift": 0.0361,
1316	  "lift_ci_lower": 0.0042,
1317	  "lift_ci_upper": 0.0706,
1318	  "n": 1190,
1319	  "pass_precision": 0.8776,
1320	  "pass_recall": 0.7579,
1321	  "pass_f1": 0.8134,
1322	  "fail_precision": 0.5473,
1323	  "fail_recall": 0.7345,
1324	  "fail_f1": 0.6272,
1325	  "epoch_level": {
1326	    "epoch1_accuracy": 0.7429,
1327	    "epoch2_accuracy": 0.763,
1328	    "final_accuracy": 0.7513,
1329	    "trend": "non_monotonic_epoch2_best"
1330	  }
1331	}
1332	
1333	================================================================================
1334	EXP_ID: qwen1.5b_exception_only_seed42
1335	STATUS: DONE
1336	CONCLUSION: killed
1337	MODEL_NAME: Qwen2.5-Coder-1.5B-Instruct
1338	METRICS: (none)
1339	
1340	================================================================================
1341	EXP_ID: qwen1.5b_full_trace_seed42
1342	STATUS: DONE
1343	CONCLUSION: killed
1344	MODEL_NAME: Qwen2.5-Coder-1.5B-Instruct
1345	METRICS: (none)
1346	
1347	================================================================================
1348	EXP_ID: qwen1.5b_no_trace_seed42
1349	STATUS: DONE
1350	CONCLUSION: success
1351	MODEL_NAME: Qwen2.5-Coder-1.5B-Instruct
1352	METRICS: {
1353	  "accuracy": 0.7261,
1354	  "accuracy_ci_lower": 0.7008,
1355	  "accuracy_ci_upper": 0.7529,
1356	  "majority_baseline": 0.7151,
1357	  "lift_pp": 1.09,
1358	  "pass_precision": 0.831,
1359	  "pass_recall": 0.774,
1360	  "pass_f1": 0.802,
1361	  "fail_precision": 0.516,
1362	  "fail_recall": 0.605,
1363	  "fail_f1": 0.557
1364	}
1365	
1366	================================================================================
1367	EXP_ID: qwen1.5b_vota_seed42
1368	STATUS: DONE
1369	CONCLUSION: killed
1370	MODEL_NAME: Qwen2.5-Coder-1.5B-Instruct
1371	METRICS: (none)
1372	
1373	================================================================================
1374	EXP_ID: qwen15b_ae_only_seed123
1375	STATUS: DONE
1376	CONCLUSION: success
1377	MODEL_NAME: Qwen2.5-Coder-1.5B-Instruct
1378	METRICS: {
1379	  "accuracy": 0.9857,
1380	  "majority_baseline": 0.715,
1381	  "lift_pp": 27.1,
1382	  "fail_f1": 0.975
1383	}
1384	
1385	================================================================================
1386	EXP_ID: qwen15b_ae_only_seed42
1387	STATUS: DONE
1388	CONCLUSION: success
1389	MODEL_NAME: Qwen2.5-Coder-1.5B-Instruct
1390	METRICS: {
1391	  "accuracy": 0.9908,
1392	  "majority_baseline": 0.7151,
1393	  "lift": 0.2756,
1394	  "pass_precision": 1,
1395	  "pass_recall": 0.987,
1396	  "pass_f1": 0.9935,
1397	  "fail_precision": 0.9686,
1398	  "fail_recall": 1,
1399	  "fail_f1": 0.984,
1400	  "n": 1190,
1401	  "accuracy_ci_lower": 0.9849,
1402	  "accuracy_ci_upper": 0.9958
1403	}
1404	
1405	================================================================================
1406	EXP_ID: qwen15b_exception_only_seed123
1407	STATUS: DONE
1408	CONCLUSION: failed
1409	MODEL_NAME: N/A
1410	METRICS: {
1411	  "error": "CUDA OOM at step 3/444",
1412	  "exit_code": 1,
1413	  "cause": "GPU 0 had 45.15 GiB PyTorch allocated (likely concurrent model loading with codellama13b), only 1.80 GiB free when trying to allocate 4.64 GiB",
1414	  "seed_comparison": {
1415	    "seed42_accuracy": 0.9983,
1416	    "seed123_accuracy": "N/A - OOM crash"
1417	  }
1418	}
1419	
1420	================================================================================
1421	EXP_ID: qwen15b_exception_only_seed123_v2
1422	STATUS: DONE
1423	CONCLUSION: success
1424	MODEL_NAME: N/A
1425	METRICS: {
1426	  "accuracy": 0.9983,
1427	  "accuracy_ci_lower": 0.9958,
1428	  "accuracy_ci_upper": 1,
1429	  "seed_comparison": {
1430	    "seed42_accuracy": 0.9983,
1431	    "seed456_accuracy": 0.9983,
1432	    "seed123_accuracy": 0.9983
1433	  }
1434	}
1435	
1436	================================================================================
1437	EXP_ID: qwen15b_exception_only_seed42
1438	STATUS: DONE
1439	CONCLUSION: success
1440	MODEL_NAME: N/A
1441	METRICS: {
1442	  "accuracy": 0.9983,
1443	  "accuracy_ci_lower": 0.9958,
1444	  "accuracy_ci_upper": 1,
1445	  "majority_baseline": 0.7151,
1446	  "lift": 0.283,
1447	  "n": 1190,
1448	  "pass_precision": 1,
1449	  "pass_recall": 0.9976,
1450	  "pass_f1": 0.9988,
1451	  "fail_precision": 0.9941,
1452	  "fail_recall": 1,
1453	  "fail_f1": 0.9971,
1454	  "train_loss": 0.1347,
1455	  "eval_loss": 0.5761,
1456	  "wall_clock_seconds": 1762
1457	}
1458	
1459	================================================================================
1460	EXP_ID: qwen15b_exception_only_seed456
1461	STATUS: DONE
1462	CONCLUSION: success
1463	MODEL_NAME: Qwen2.5-Coder-1.5B-Instruct
1464	METRICS: {
1465	  "accuracy": 0.9983,
1466	  "accuracy_ci_lower": 0.9958,
1467	  "accuracy_ci_upper": 1,
1468	  "majority_baseline": 0.7151,
1469	  "lift": 0.2832,
1470	  "n": 1190,
1471	  "pass_precision": 1,
1472	  "pass_recall": 0.9976,
1473	  "pass_f1": 0.9988,
1474	  "fail_precision": 0.9941,
1475	  "fail_recall": 1,
1476	  "fail_f1": 0.9971,
1477	  "seed_comparison": {
1478	    "seed42_accuracy": 0.9983,
1479	    "seed456_accuracy": 0.9983,
1480	    "diff": 0,
1481	    "note": "Identical to seed42 to 4 decimal places \u2014 exception_only fully seed-robust on Qwen-1.5B"
1482	  }
1483	}
1484	
1485	================================================================================
1486	EXP_ID: qwen15b_full_trace_head2048_seed42
1487	STATUS: DONE
1488	CONCLUSION: success
1489	MODEL_NAME: Qwen2.5-Coder-1.5B-Instruct
1490	METRICS: {
1491	  "accuracy": 0.7529,
1492	  "accuracy_ci_lower": 0.7286,
1493	  "accuracy_ci_upper": 0.7782,
1494	  "pass_precision": 0.799,
1495	  "pass_recall": 0.874,
1496	  "pass_f1": 0.835,
1497	  "fail_precision": 0.587,
1498	  "fail_recall": 0.448,
1499	  "fail_f1": 0.508,
1500	  "n_test": 1190
1501	}
1502	
1503	================================================================================
1504	EXP_ID: qwen15b_full_trace_seed42
1505	STATUS: DONE
1506	CONCLUSION: success
1507	MODEL_NAME: N/A
1508	METRICS: {
1509	  "accuracy": 0.7706,
1510	  "n": 1190
1511	}
1512	
1513	================================================================================
1514	EXP_ID: qwen15b_full_trace_tail1024_seed42
1515	STATUS: DONE
1516	CONCLUSION: success
1517	MODEL_NAME: Qwen2.5-Coder-1.5B-Instruct
1518	METRICS: {
1519	  "accuracy": 0.966,
1520	  "accuracy_ci_low": 0.955,
1521	  "accuracy_ci_high": 0.976,
1522	  "pass_precision": 0.96,
1523	  "pass_recall": 0.99,
1524	  "pass_f1": 0.98,
1525	  "fail_precision": 0.97,
1526	  "fail_recall": 0.91,
1527	  "fail_f1": 0.94,
1528	  "eval_loss": 0.1983,
1529	  "train_loss": 0.1187,
1530	  "majority_baseline": 0.715,
1531	  "lift_over_majority_pp": 25
1532	}
1533	
1534	================================================================================
1535	EXP_ID: qwen15b_full_trace_tail2048_seed42
1536	STATUS: DONE
1537	CONCLUSION: success
1538	MODEL_NAME: Qwen2.5-Coder-1.5B-Instruct
1539	METRICS: {
1540	  "accuracy": 0.979,
1541	  "accuracy_ci_lower": 0.9706,
1542	  "accuracy_ci_upper": 0.9874,
1543	  "pass_precision": 0.9758,
1544	  "pass_recall": 0.9953,
1545	  "pass_f1": 0.9855,
1546	  "fail_precision": 0.9876,
1547	  "fail_recall": 0.9381,
1548	  "fail_f1": 0.9622,
1549	  "n_test": 1190
1550	}
1551	
1552	================================================================================
1553	EXP_ID: qwen15b_full_trace_tail256_seed42
1554	STATUS: DONE
1555	CONCLUSION: negative
1556	MODEL_NAME: Qwen2.5-Coder-1.5B-Instruct
1557	METRICS: {
1558	  "accuracy": 0.726,
1559	  "accuracy_ci_lower": 0.7,
1560	  "accuracy_ci_upper": 0.753,
1561	  "majority_baseline": 0.715,
1562	  "lift_over_majority": 0.011,
1563	  "lift_ci_lower": -0.021,
1564	  "lift_ci_upper": 0.044,
1565	  "pass_precision": 0.82,
1566	  "pass_recall": 0.79,
1567	  "pass_f1": 0.8,
1568	  "fail_precision": 0.52,
1569	  "fail_recall": 0.57,
1570	  "fail_f1": 0.54,
1571	  "eval_loss": 0.5936,
1572	  "train_loss": 0.2687
1573	}
1574	
1575	================================================================================
1576	EXP_ID: qwen15b_full_trace_tail384_seed42
1577	STATUS: DONE
1578	CONCLUSION: negative
1579	MODEL_NAME: Qwen2.5-Coder-1.5B-Instruct
1580	METRICS: {
1581	  "accuracy": 0.7361,
1582	  "majority_baseline": 0.7151,
1583	  "lift": 0.021,
1584	  "n": 1190,
1585	  "pass_precision": 0.8069,
1586	  "pass_recall": 0.8296,
1587	  "pass_f1": 0.8181,
1588	  "fail_precision": 0.5397,
1589	  "fail_recall": 0.5015,
1590	  "fail_f1": 0.5199,
1591	  "accuracy_ci": [
1592	    0.7101,
1593	    0.7622
1594	  ]
1595	}
1596	
1597	================================================================================
1598	EXP_ID: qwen15b_full_trace_tail512_seed123
1599	STATUS: DONE
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "925a3cde-239a-4740-a25e-f3da147f239d",
  "isSidechain": true,
  "promptId": "d3a99d3c-02c3-4d5e-9ec2-b28e1b492d4b",
  "agentId": "a86b080f191dc2217",
  "type": "user",
  "uuid": "f99dc285-916f-4216-a01a-bbe2940c2d75",
  "sourceToolAssistantUUID": "925a3cde-239a-4740-a25e-f3da147f239d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "f5f4efcf-b091-4929-abdf-35aa1152d6be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-21T19:05:20.903Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NCSEX5Hzn2vb2eQBtkETKi`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/f5f4efcf-b091-4929-abdf-35aa1152d6be/tool-results/b7t9ioqmo.txt",
  "offset": 1598,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f99dc285-916f-4216-a01a-bbe2940c2d75",
  "isSidechain": true,
  "agentId": "a86b080f191dc2217",
  "requestId": "req_011CbGEdfqRQoQz12xBBvQff",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d062284c-8834-4746-a010-b0f4c9d32745",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "f5f4efcf-b091-4929-abdf-35aa1152d6be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0167KhL7u1xmtXQzTKXVpYVC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5390,
      "cache_read_input_tokens": 36864,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5390
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 166,
          "cache_read_input_tokens": 36864,
          "cache_creation_input_tokens": 5390,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5390,
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

_source line 29 · 2026-05-21T19:05:20.910Z_

<details><summary>↩ Tool result · `toolu_01NCSEX5Hzn2vb2eQBtkETKi`</summary>

```text
1598	EXP_ID: qwen15b_full_trace_tail512_seed123
1599	STATUS: DONE
1600	CONCLUSION: success
1601	MODEL_NAME: N/A
1602	METRICS: {
1603	  "accuracy": 0.9765,
1604	  "accuracy_ci_lower": 0.9681,
1605	  "accuracy_ci_upper": 0.9849,
1606	  "majority_baseline": 0.7151,
1607	  "lift": 0.2613,
1608	  "n": 1190,
1609	  "pass_precision": 0.9757,
1610	  "pass_recall": 0.9918,
1611	  "pass_f1": 0.9837,
1612	  "fail_precision": 0.9785,
1613	  "fail_recall": 0.9381,
1614	  "fail_f1": 0.9578,
1615	  "seed_comparison": {
1616	    "seed42_accuracy": 0.956,
1617	    "seed123_accuracy": 0.9765,
1618	    "note": "seed123 (97.65%) exceeds seed42 (95.6%) by 2pp; both in convergence band post-phase-transition"
1619	  }
1620	}
1621	
1622	================================================================================
1623	EXP_ID: qwen15b_full_trace_tail512_seed42
1624	STATUS: DONE
1625	CONCLUSION: success
1626	MODEL_NAME: N/A
1627	METRICS: {
1628	  "accuracy": 0.956,
1629	  "accuracy_ci_lower": 0.945,
1630	  "accuracy_ci_upper": 0.968,
1631	  "majority_baseline": 0.715,
1632	  "lift_over_majority": 0.241,
1633	  "eval_loss": 0.263,
1634	  "train_loss": 0.154,
1635	  "pass_precision": 0.98,
1636	  "pass_recall": 0.96,
1637	  "pass_f1": 0.97,
1638	  "fail_precision": 0.91,
1639	  "fail_recall": 0.94,
1640	  "fail_f1": 0.92,
1641	  "eval_mean_token_accuracy": 0.949
1642	}
1643	
1644	================================================================================
1645	EXP_ID: qwen15b_full_trace_tail512_seed456
1646	STATUS: DONE
1647	CONCLUSION: success
1648	MODEL_NAME: N/A
1649	METRICS: {
1650	  "accuracy": 0.9672,
1651	  "accuracy_ci_lower": 0.9563,
1652	  "accuracy_ci_upper": 0.9773,
1653	  "majority_baseline": 0.7151,
1654	  "lift": 0.2521,
1655	  "n": 1190,
1656	  "pass_precision": 0.9765,
1657	  "pass_recall": 0.9777,
1658	  "pass_f1": 0.9771,
1659	  "fail_precision": 0.9438,
1660	  "fail_recall": 0.941,
1661	  "fail_f1": 0.9424,
1662	  "seed_comparison": {
1663	    "seed42_accuracy": 0.956,
1664	    "seed123_accuracy": 0.9765,
1665	    "seed456_accuracy": 0.9672,
1666	    "note": "seed456 (96.72%) within convergence band [95.6%, 97.65%], confirming seed robustness post-phase-transition"
1667	  }
1668	}
1669	
1670	================================================================================
1671	EXP_ID: qwen15b_label_only_seed123_v2
1672	STATUS: DONE
1673	CONCLUSION: success
1674	MODEL_NAME: Qwen2.5-Coder-1.5B-Instruct
1675	METRICS: {
1676	  "accuracy": 0.8134,
1677	  "accuracy_ci_lower": 0.7924,
1678	  "accuracy_ci_upper": 0.8345,
1679	  "majority_baseline": 0.7151,
1680	  "lift_pp": 9.83,
1681	  "pass_recall": 0.94,
1682	  "pass_precision": 0.824,
1683	  "pass_f1": 0.878,
1684	  "fail_recall": 0.496,
1685	  "fail_precision": 0.767,
1686	  "fail_f1": 0.602
1687	}
1688	
1689	================================================================================
1690	EXP_ID: qwen15b_label_only_seed42
1691	STATUS: DONE
1692	CONCLUSION: killed
1693	MODEL_NAME: N/A
1694	METRICS: (none)
1695	
1696	================================================================================
1697	EXP_ID: qwen15b_label_only_seed42_v2
1698	STATUS: DONE
1699	CONCLUSION: success
1700	MODEL_NAME: Qwen2.5-Coder-1.5B-Instruct
1701	METRICS: {
1702	  "accuracy": 0.789,
1703	  "accuracy_ci_lower": 0.766,
1704	  "accuracy_ci_upper": 0.812,
1705	  "majority_baseline": 0.715,
1706	  "lift_pp": 7.4,
1707	  "pass_recall": 0.91,
1708	  "pass_precision": 0.82,
1709	  "pass_f1": 0.86,
1710	  "fail_recall": 0.5,
1711	  "fail_precision": 0.68,
1712	  "fail_f1": 0.57
1713	}
1714	
1715	================================================================================
1716	EXP_ID: qwen15b_label_only_seed456_v2
1717	STATUS: DONE
1718	CONCLUSION: success
1719	MODEL_NAME: Qwen2.5-Coder-1.5B-Instruct
1720	METRICS: {
1721	  "accuracy": 0.8252,
1722	  "pass_f1": 0.885,
1723	  "fail_f1": 0.639,
1724	  "pass_precision": 0.837,
1725	  "pass_recall": 0.938,
1726	  "fail_precision": 0.776,
1727	  "fail_recall": 0.543,
1728	  "train_loss": 0.2394,
1729	  "eval_loss": 0.3064,
1730	  "majority_baseline": 0.715
1731	}
1732	
1733	================================================================================
1734	EXP_ID: qwen15b_loop_only_seed123
1735	STATUS: DONE
1736	CONCLUSION: success
1737	MODEL_NAME: Qwen2.5-Coder-1.5B-Instruct
1738	METRICS: {
1739	  "accuracy": 0.8109,
1740	  "pass_f1": 0.8737,
1741	  "fail_f1": 0.6244,
1742	  "pass_precision": 0.8366,
1743	  "pass_recall": 0.9142,
1744	  "fail_precision": 0.7192,
1745	  "fail_recall": 0.5516,
1746	  "train_loss": 0.0843,
1747	  "train_runtime_sec": 2659.73
1748	}
1749	
1750	================================================================================
1751	EXP_ID: qwen15b_loop_only_seed42
1752	STATUS: DONE
1753	CONCLUSION: success
1754	MODEL_NAME: Qwen2.5-Coder-1.5B-Instruct
1755	METRICS: {
1756	  "accuracy": 0.7832,
1757	  "pass_f1": 0.8526,
1758	  "fail_f1": 0.5905,
1759	  "pass_precision": 0.8298,
1760	  "pass_recall": 0.8766,
1761	  "fail_precision": 0.6392,
1762	  "fail_recall": 0.5487,
1763	  "train_loss": 0.0847,
1764	  "train_runtime_sec": 2679
1765	}
1766	
1767	================================================================================
1768	EXP_ID: qwen15b_loop_only_seed456
1769	STATUS: DONE
1770	CONCLUSION: success
1771	MODEL_NAME: Qwen2.5-Coder-1.5B-Instruct
1772	METRICS: {
1773	  "accuracy": 0.792,
1774	  "ci_95": [
1775	    0.768,
1776	    0.813
1777	  ],
1778	  "majority_baseline": 0.715,
1779	  "lift_pp": 7.6,
1780	  "pass_precision": 0.85,
1781	  "pass_recall": 0.86,
1782	  "pass_f1": 0.86,
1783	  "fail_precision": 0.64,
1784	  "fail_recall": 0.62,
1785	  "fail_f1": 0.63
1786	}
1787	
1788	================================================================================
1789	EXP_ID: qwen15b_no_trace_seed123
1790	STATUS: DONE
1791	CONCLUSION: success
1792	MODEL_NAME: Qwen2.5-Coder-1.5B-Instruct
1793	METRICS: {
1794	  "accuracy": 0.7588,
1795	  "accuracy_ci_lower": 0.7328,
1796	  "accuracy_ci_upper": 0.7824,
1797	  "majority_baseline": 0.7151,
1798	  "lift": 0.0437,
1799	  "pass_precision": 0.8279,
1800	  "pass_recall": 0.8367,
1801	  "pass_f1": 0.8323,
1802	  "fail_precision": 0.5788,
1803	  "fail_recall": 0.5634,
1804	  "fail_f1": 0.571,
1805	  "train_loss": 0.2221,
1806	  "eval_loss": 0.7838
1807	}
1808	
1809	================================================================================
1810	EXP_ID: qwen15b_no_trace_seed42
1811	STATUS: DONE
1812	CONCLUSION: success
1813	MODEL_NAME: N/A
1814	METRICS: {
1815	  "accuracy": 0.6731,
1816	  "n": 1190,
1817	  "pass_f1": 0.7527,
1818	  "fail_f1": 0.518,
1819	  "lift_over_majority": -0.042,
1820	  "training_time_sec": 851
1821	}
1822	
1823	================================================================================
1824	EXP_ID: qwen15b_no_trace_seed456
1825	STATUS: DONE
1826	CONCLUSION: success
1827	MODEL_NAME: Qwen2.5-Coder-1.5B-Instruct
1828	METRICS: {
1829	  "accuracy": 0.7387,
1830	  "fail_f1": 0.5266,
1831	  "pass_f1": 0.8195,
1832	  "eval_loss": 0.7725,
1833	  "train_loss": 0.2226,
1834	  "fail_precision": 0.544,
1835	  "fail_recall": 0.5103,
1836	  "pass_precision": 0.8096,
1837	  "pass_recall": 0.8296
1838	}
1839	
1840	================================================================================
1841	EXP_ID: qwen15b_nomarker_seed42
1842	STATUS: DONE
1843	CONCLUSION: success
1844	MODEL_NAME: Qwen2.5-Coder-1.5B-Instruct
1845	METRICS: {
1846	  "accuracy": 0.978,
1847	  "n": 1190,
1848	  "accuracy_ci": [
1849	    0.97,
1850	    0.986
1851	  ],
1852	  "majority_baseline": 0.715,
1853	  "lift": 0.263,
1854	  "pass_precision": 0.97,
1855	  "pass_recall": 1,
1856	  "pass_f1": 0.98,
1857	  "fail_precision": 1,
1858	  "fail_recall": 0.92,
1859	  "fail_f1": 0.96
1860	}
1861	
1862	================================================================================
1863	EXP_ID: qwen15b_vota_seed123
1864	STATUS: DONE
1865	CONCLUSION: success
1866	MODEL_NAME: Qwen2.5-Coder-1.5B-Instruct
1867	METRICS: {
1868	  "accuracy": 0.995,
1869	  "ci_95": [
1870	    0.9908,
1871	    0.9983
1872	  ],
1873	  "pass_f1": 0.9965,
1874	  "fail_f1": 0.9912,
1875	  "lift_pp": 28,
1876	  "n_samples": 1190
1877	}
1878	
1879	================================================================================
1880	EXP_ID: qwen15b_vota_seed42
1881	STATUS: DONE
1882	CONCLUSION: success
1883	MODEL_NAME: N/A
1884	METRICS: {
1885	  "accuracy": 0.9958,
1886	  "n": 1190,
1887	  "pass_recall": 0.9976,
1888	  "fail_recall": 0.9912,
1889	  "pass_f1": 0.9971,
1890	  "fail_f1": 0.9926,
1891	  "training_time_sec": 2922
1892	}
1893	
1894	================================================================================
1895	EXP_ID: qwen7b_exception_only_dynamics_seed42
1896	STATUS: DONE
1897	CONCLUSION: success
1898	MODEL_NAME: Qwen2.5-Coder-7B-Instruct
1899	METRICS: {
1900	  "step50_acc": 0.9933,
1901	  "step100_acc": 0.9933,
1902	  "step150_acc": 0.9933,
1903	  "step200_acc": 0.9983,
1904	  "step250_acc": 0.9983,
1905	  "step300_acc": 0.9983,
1906	  "step350_acc": 0.9983,
1907	  "step400_acc": 0.9983,
1908	  "step444_acc": 0.9983,
1909	  "saturation_step": 200,
1910	  "final_loss": 0.0329,
1911	  "pass_f1": 0.9988,
1912	  "fail_f1": 0.9971
1913	}
1914	
1915	================================================================================
1916	EXP_ID: qwen7b_full_trace_dynamics_seed42
1917	STATUS: DONE
1918	CONCLUSION: success
1919	MODEL_NAME: Qwen2.5-Coder-7B-Instruct
1920	METRICS: {
1921	  "step50_acc": 0.8739,
1922	  "step100_acc": 0.821,
1923	  "step150_acc": 0.8571,
1924	  "step200_acc": 0.8655,
1925	  "step250_acc": 0.8739,
1926	  "step300_acc": 0.8487,
1927	  "step350_acc": 0.8882,
1928	  "step400_acc": 0.8571,
1929	  "step444_acc": 0.8824,
1930	  "best_step": 350,
1931	  "best_acc": 0.8882,
1932	  "final_loss": 0.0085
1933	}
1934	
1935	================================================================================
1936	EXP_ID: qwen7b_full_trace_head2048_seed42
1937	STATUS: DONE
1938	CONCLUSION: success
1939	MODEL_NAME: N/A
1940	METRICS: {
1941	  "accuracy_epoch1": 0.816,
1942	  "accuracy_epoch3": 0.81,
1943	  "pass_f1_epoch1": 0.87,
1944	  "fail_f1_epoch1": 0.686,
1945	  "pass_f1_epoch3": 0.866,
1946	  "fail_f1_epoch3": 0.674,
1947	  "best_accuracy": 0.816,
1948	  "best_epoch": 1
1949	}
1950	
1951	================================================================================
1952	EXP_ID: qwen7b_full_trace_label_only_seed123
1953	STATUS: DONE
1954	CONCLUSION: success
1955	MODEL_NAME: Qwen2.5-Coder-7B-Instruct
1956	METRICS: {
1957	  "accuracy": 0.8689,
1958	  "accuracy_ci_lower": 0.8496,
1959	  "accuracy_ci_upper": 0.8874,
1960	  "pass_f1": 0.9121,
1961	  "fail_f1": 0.7426,
1962	  "pass_precision": 0.8765,
1963	  "pass_recall": 0.9506,
1964	  "fail_precision": 0.8427,
1965	  "fail_recall": 0.6637,
1966	  "majority_baseline": 0.7151,
1967	  "lift": 0.1538,
1968	  "train_loss": 0.2425,
1969	  "eval_loss": 0.2787
1970	}
1971	
1972	================================================================================
1973	EXP_ID: qwen7b_full_trace_label_only_seed456
1974	STATUS: DONE
1975	CONCLUSION: success
1976	MODEL_NAME: Qwen2.5-Coder-7B-Instruct
1977	METRICS: {
1978	  "accuracy": 0.847,
1979	  "accuracy_ci_lower": 0.827,
1980	  "accuracy_ci_upper": 0.866,
1981	  "pass_f1": 0.9,
1982	  "fail_f1": 0.71,
1983	  "pass_precision": 0.87,
1984	  "pass_recall": 0.92,
1985	  "fail_precision": 0.76,
1986	  "fail_recall": 0.67,
1987	  "majority_baseline": 0.7151,
1988	  "lift": 0.1319,
1989	  "train_loss": 0.2452,
1990	  "eval_loss": 0.3366
1991	}
1992	
1993	================================================================================
1994	EXP_ID: qwen7b_full_trace_seed123
1995	STATUS: DONE
1996	CONCLUSION: success
1997	MODEL_NAME: Qwen2.5-Coder-7B-Instruct
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d062284c-8834-4746-a010-b0f4c9d32745",
  "isSidechain": true,
  "promptId": "d3a99d3c-02c3-4d5e-9ec2-b28e1b492d4b",
  "agentId": "a86b080f191dc2217",
  "type": "user",
  "uuid": "1ce0089f-b57d-41c8-b96e-2de89c5f8fe9",
  "sourceToolAssistantUUID": "d062284c-8834-4746-a010-b0f4c9d32745",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "f5f4efcf-b091-4929-abdf-35aa1152d6be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-21T19:05:26.750Z_

<details open><summary>🔧 Tool call — Read · `toolu_01E1sMNFZehHaofYKStNx7kq`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/f5f4efcf-b091-4929-abdf-35aa1152d6be/tool-results/b7t9ioqmo.txt",
  "offset": 1997,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ce0089f-b57d-41c8-b96e-2de89c5f8fe9",
  "isSidechain": true,
  "agentId": "a86b080f191dc2217",
  "requestId": "req_011CbGEe4YfQoj3nnyzenpgK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58051e01-f22c-4ab6-85eb-09aa7788a48a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "f5f4efcf-b091-4929-abdf-35aa1152d6be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XKwtgnLHXXo5bgZGovNTHw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5511,
      "cache_read_input_tokens": 42254,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5511,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 31 · 2026-05-21T19:05:26.760Z_

<details><summary>↩ Tool result · `toolu_01E1sMNFZehHaofYKStNx7kq`</summary>

```text
1997	MODEL_NAME: Qwen2.5-Coder-7B-Instruct
1998	METRICS: {
1999	  "accuracy": 0.802,
2000	  "ci_lower": 0.778,
2001	  "ci_upper": 0.825,
2002	  "majority_baseline": 0.715,
2003	  "lift_pp": 8.7,
2004	  "pass_precision": 0.88,
2005	  "pass_recall": 0.84,
2006	  "pass_f1": 0.86,
2007	  "fail_precision": 0.64,
2008	  "fail_recall": 0.7,
2009	  "fail_f1": 0.67,
2010	  "train_loss": 0.0415,
2011	  "eval_loss": 0.0827
2012	}
2013	
2014	================================================================================
2015	EXP_ID: qwen7b_full_trace_seed456
2016	STATUS: DONE
2017	CONCLUSION: failed
2018	MODEL_NAME: Qwen2.5-Coder-7B-Instruct
2019	METRICS: (none)
2020	
2021	================================================================================
2022	EXP_ID: qwen7b_full_trace_seed456_v2
2023	STATUS: DONE
2024	CONCLUSION: success
2025	MODEL_NAME: Qwen2.5-Coder-7B-Instruct
2026	METRICS: {
2027	  "accuracy": 0.8235,
2028	  "ci_lower": 0.8017,
2029	  "ci_upper": 0.8454,
2030	  "majority_baseline": 0.7151,
2031	  "lift_pp": 10.84,
2032	  "pass_precision": 0.8885,
2033	  "pass_recall": 0.8613,
2034	  "pass_f1": 0.8747,
2035	  "fail_precision": 0.6767,
2036	  "fail_recall": 0.7286,
2037	  "fail_f1": 0.7017,
2038	  "train_loss": 0.0416,
2039	  "eval_loss": 0.0794
2040	}
2041	
2042	================================================================================
2043	EXP_ID: qwen7b_full_trace_tail384_seed42
2044	STATUS: DONE
2045	CONCLUSION: success
2046	MODEL_NAME: Qwen2.5-Coder-7B-Instruct
2047	METRICS: {
2048	  "accuracy": 0.798,
2049	  "accuracy_ci_lower": 0.776,
2050	  "accuracy_ci_upper": 0.821,
2051	  "majority_baseline": 0.715,
2052	  "lift": 0.083,
2053	  "n": 1190,
2054	  "pass_precision": 0.89,
2055	  "pass_recall": 0.82,
2056	  "pass_f1": 0.85,
2057	  "fail_precision": 0.62,
2058	  "fail_recall": 0.75,
2059	  "fail_f1": 0.68
2060	}
2061	
2062	================================================================================
2063	EXP_ID: qwen7b_full_trace_tail512_seed123
2064	STATUS: DONE
2065	CONCLUSION: success
2066	MODEL_NAME: N/A
2067	METRICS: {
2068	  "accuracy": 0.9597,
2069	  "accuracy_ci_lower": 0.9487,
2070	  "accuracy_ci_upper": 0.9706,
2071	  "majority_baseline": 0.7151,
2072	  "lift": 0.2445,
2073	  "n": 1190,
2074	  "pass_precision": 0.9751,
2075	  "pass_recall": 0.9683,
2076	  "pass_f1": 0.9717,
2077	  "fail_precision": 0.9217,
2078	  "fail_recall": 0.9381,
2079	  "fail_f1": 0.9298,
2080	  "seed_comparison": {
2081	    "seed42_accuracy": 0.936,
2082	    "seed123_accuracy": 0.9597
2083	  }
2084	}
2085	
2086	================================================================================
2087	EXP_ID: qwen7b_full_trace_tail512_seed42
2088	STATUS: DONE
2089	CONCLUSION: failed
2090	MODEL_NAME: Qwen2.5-Coder-7B-Instruct
2091	METRICS: (none)
2092	
2093	================================================================================
2094	EXP_ID: qwen7b_full_trace_tail512_seed456
2095	STATUS: DONE
2096	CONCLUSION: success
2097	MODEL_NAME: Qwen2.5-Coder-7B-Instruct
2098	METRICS: {
2099	  "accuracy": 0.9765,
2100	  "majority_baseline": 0.7151,
2101	  "lift": 0.2613,
2102	  "n": 1190,
2103	  "pass_precision": 0.9746,
2104	  "pass_recall": 0.9929,
2105	  "pass_f1": 0.9837,
2106	  "fail_precision": 0.9814,
2107	  "fail_recall": 0.9351,
2108	  "fail_f1": 0.9577,
2109	  "accuracy_ci": [
2110	    0.9681,
2111	    0.9849
2112	  ]
2113	}
2114	
2115	================================================================================
2116	EXP_ID: vota_ae_only_seed42
2117	STATUS: DONE
2118	CONCLUSION: success
2119	MODEL_NAME: Qwen2.5-Coder-7B-Instruct
2120	METRICS: {
2121	  "accuracy": 0.9992,
2122	  "accuracy_ci": [
2123	    0.9975,
2124	    1
2125	  ],
2126	  "bootstrap_pairwise": {
2127	    "ae_only_vs_no_trace": {
2128	      "diff": 0.2479,
2129	      "ci": [
2130	        0.2235,
2131	        0.2731
2132	      ],
2133	      "p_value": 0,
2134	      "significant": true
2135	    },
2136	    "ae_only_vs_exception_only": {
2137	      "diff": 0.0008,
2138	      "ci": [
2139	        -0.0017,
2140	        0.0034
2141	      ],
2142	      "p_value": 0.8002,
2143	      "significant": false
2144	    },
2145	    "ae_only_vs_vota": {
2146	      "diff": 0.005,
2147	      "ci": [
2148	        0.0017,
2149	        0.0092
2150	      ],
2151	      "p_value": 0.0046,
2152	      "significant": true
2153	    }
2154	  },
2155	  "config": {
2156	    "n_bootstrap": 10000,
2157	    "seed": 42,
2158	    "method": "paired_bootstrap"
2159	  }
2160	}
2161	
2162	================================================================================
2163	EXP_ID: vota_exception_only_seed42
2164	STATUS: DONE
2165	CONCLUSION: failed
2166	MODEL_NAME: Qwen2.5-Coder-7B-Instruct
2167	METRICS: (none)
2168	
2169	================================================================================
2170	EXP_ID: vota_exception_only_seed42_v2
2171	STATUS: DONE
2172	CONCLUSION: success
2173	MODEL_NAME: Qwen2.5-Coder-7B-Instruct
2174	METRICS: {
2175	  "accuracy": 0.9983,
2176	  "majority_baseline": 0.7151,
2177	  "lift": 0.2832,
2178	  "n": 1190,
2179	  "pass_precision": 1,
2180	  "pass_recall": 0.998,
2181	  "pass_f1": 0.999,
2182	  "fail_precision": 0.994,
2183	  "fail_recall": 1,
2184	  "fail_f1": 0.997,
2185	  "lift_vs_notrace": 0.2471,
2186	  "lift_vs_notrace_ci_lower": 0.2227,
2187	  "lift_vs_notrace_ci_upper": 0.2714,
2188	  "lift_vs_fulltrace": 0.1807,
2189	  "lift_vs_fulltrace_ci_lower": 0.1588,
2190	  "lift_vs_fulltrace_ci_upper": 0.2034,
2191	  "lift_vs_vota": 0.0067,
2192	  "lift_vs_vota_ci_lower": 0.0017,
2193	  "lift_vs_vota_ci_upper": 0.0126,
2194	  "lift_vs_vota_pvalue": 0.01
2195	}
2196	
2197	================================================================================
2198	EXP_ID: vota_loop_only_seed42
2199	STATUS: DONE
2200	CONCLUSION: success
2201	MODEL_NAME: Qwen2.5-Coder-7B-Instruct
2202	METRICS: {
2203	  "accuracy": 0.8563,
2204	  "majority_baseline": 0.7151,
2205	  "lift": 0.1412,
2206	  "n": 1190,
2207	  "pass_precision": 0.9239,
2208	  "pass_recall": 0.8707,
2209	  "pass_f1": 0.8966,
2210	  "fail_precision": 0.7165,
2211	  "fail_recall": 0.8201,
2212	  "fail_f1": 0.7648,
2213	  "accuracy_ci": [
2214	    0.8353,
2215	    0.8756
2216	  ],
2217	  "bootstrap_vs_no_trace": {
2218	    "diff": 0.105,
2219	    "ci": [
2220	      0.0824,
2221	      0.1286
2222	    ],
2223	    "significant": true
2224	  },
2225	  "bootstrap_vs_vota": {
2226	    "diff": -0.1378,
2227	    "ci": [
2228	      -0.1571,
2229	      -0.1185
2230	    ],
2231	    "significant": true
2232	  },
2233	  "bootstrap_vs_full_trace": {
2234	    "diff": 0.0387,
2235	    "ci": [
2236	      0.0185,
2237	      0.0597
2238	    ],
2239	    "significant": true
2240	  },
2241	  "train_loss": 0.0718,
2242	  "wall_clock_seconds": 7425.65
2243	}
2244	
2245	================================================================================
2246	EXP_ID: vota_no_ae_seed42
2247	STATUS: DONE
2248	CONCLUSION: success
2249	MODEL_NAME: Qwen2.5-Coder-7B-Instruct
2250	METRICS: {
2251	  "accuracy": 0.994,
2252	  "majority_baseline": 0.7151,
2253	  "lift": 0.279,
2254	  "n": 1190,
2255	  "pass_f1": 0.996,
2256	  "fail_f1": 0.989,
2257	  "accuracy_ci_lower": 0.989,
2258	  "accuracy_ci_upper": 0.998,
2259	  "lift_vs_notrace": 0.243,
2260	  "lift_vs_notrace_ci_lower": 0.218,
2261	  "lift_vs_notrace_ci_upper": 0.268,
2262	  "train_loss": 0.0908,
2263	  "eval_loss": 0.2215,
2264	  "wall_clock_seconds": 6397.88
2265	}
2266	
2267	================================================================================
2268	EXP_ID: vota_seed123
2269	STATUS: DONE
2270	CONCLUSION: failed
2271	MODEL_NAME: Qwen2.5-Coder-7B-Instruct
2272	METRICS: (none)
2273	
2274	================================================================================
2275	EXP_ID: vota_seed42
2276	STATUS: DONE
2277	CONCLUSION: killed
2278	MODEL_NAME: N/A
2279	METRICS: (none)
2280	
2281	================================================================================
2282	EXP_ID: vota_seed42_v2
2283	STATUS: DONE
2284	CONCLUSION: killed
2285	MODEL_NAME: N/A
2286	METRICS: (none)
2287	
2288	================================================================================
2289	EXP_ID: vota_seed42_v3
2290	STATUS: DONE
2291	CONCLUSION: killed
2292	MODEL_NAME: Qwen2.5-Coder-7B-Instruct
2293	METRICS: {
2294	  "train_loss": 0.046,
2295	  "eval_loss": 0.085,
2296	  "eval_mean_token_accuracy": 0.983,
2297	  "accuracy": 0.992,
2298	  "majority_baseline": 0.7151,
2299	  "lift": 0.276,
2300	  "pass_precision": 0.99,
2301	  "pass_recall": 0.99,
2302	  "pass_f1": 0.99,
2303	  "fail_precision": 0.99,
2304	  "fail_recall": 0.99,
2305	  "fail_f1": 0.99
2306	}
2307	
2308	================================================================================
2309	EXP_ID: vota_seed42_v4
2310	STATUS: DONE
2311	CONCLUSION: success
2312	MODEL_NAME: N/A
2313	METRICS: {
2314	  "accuracy": 0.9563,
2315	  "majority_baseline": 0.7151,
2316	  "lift": 0.2412,
2317	  "n": 1190,
2318	  "pass_precision": 0.944,
2319	  "pass_recall": 0.998,
2320	  "pass_f1": 0.97,
2321	  "fail_precision": 0.993,
2322	  "fail_recall": 0.853,
2323	  "fail_f1": 0.917,
2324	  "lift_vs_notrace": 0.205,
2325	  "lift_vs_notrace_ci_lower": 0.177,
2326	  "lift_vs_notrace_ci_upper": 0.234,
2327	  "train_loss": 0.046,
2328	  "eval_loss": 0.0842
2329	}
2330	
2331	================================================================================
2332	EXP_ID: vota_seed42_v5
2333	STATUS: DONE
2334	CONCLUSION: success
2335	MODEL_NAME: Qwen2.5-Coder-7B-Instruct
2336	METRICS: {
2337	  "accuracy": 0.9941,
2338	  "pass_precision": 1,
2339	  "pass_recall": 0.9918,
2340	  "pass_f1": 0.9959,
2341	  "fail_precision": 0.9798,
2342	  "fail_recall": 1,
2343	  "fail_f1": 0.9898,
2344	  "n": 1190,
2345	  "tp": 844,
2346	  "fp": 0,
2347	  "tn": 339,
2348	  "fn": 7
2349	}
2350	
2351	================================================================================
2352	EXP_ID: vota_seed456
2353	STATUS: DONE
2354	CONCLUSION: failed
2355	MODEL_NAME: N/A
2356	METRICS: (none)
2357	
2358	================================================================================
2359	EXP_ID: vota_seed456_v2
2360	STATUS: DONE
2361	CONCLUSION: success
2362	MODEL_NAME: Qwen2.5-Coder-7B-Instruct
2363	METRICS: {
2364	  "accuracy": 0.9908,
2365	  "pass_precision": 1,
2366	  "pass_recall": 0.987,
2367	  "pass_f1": 0.993,
2368	  "fail_precision": 0.969,
2369	  "fail_recall": 1,
2370	  "fail_f1": 0.984,
2371	  "ci_95": [
2372	    0.985,
2373	    0.996
2374	  ]
2375	}
2376	
2377	================================================================================
2378	EXP_ID: zeroshot_codellama13b_exception_only
2379	STATUS: DONE
2380	CONCLUSION: success
2381	MODEL_NAME: CodeLlama-13B-Instruct
2382	METRICS: {
2383	  "accuracy": 0.5101,
2384	  "accuracy_ci_lower": 0.4824,
2385	  "accuracy_ci_upper": 0.5395,
2386	  "pass_precision": 1,
2387	  "pass_recall": 0.3502,
2388	  "pass_f1": 0.5187,
2389	  "fail_precision": 0.3585,
2390	  "fail_recall": 0.9115,
2391	  "fail_f1": 0.5146,
2392	  "n_test": 1190,
2393	  "n_unknown": 30
2394	}
2395	
2396	================================================================================
2397	EXP_ID: zeroshot_deepseek7b_exception_only
2398	STATUS: DONE
2399	CONCLUSION: success
2400	MODEL_NAME: DeepSeek-Coder-6.7B-Instruct
2401	METRICS: {
2402	  "accuracy": 0.9059,
2403	  "accuracy_ci_lower": 0.8899,
2404	  "accuracy_ci_upper": 0.9218,
2405	  "pass_precision": 0.9743,
2406	  "pass_recall": 0.8919,
2407	  "pass_f1": 0.9313,
2408	  "fail_precision": 0.7762,
2409	  "fail_recall": 0.941,
2410	  "fail_f1": 0.8507,
2411	  "n_test": 1190,
2412	  "n_unknown": 0
2413	}
2414	
2415	================================================================================
2416	EXP_ID: zeroshot_qwen15b_exception_only
2417	STATUS: DONE
2418	CONCLUSION: success
2419	MODEL_NAME: Qwen2.5-Coder-1.5B-Instruct
2420	METRICS: {
2421	  "accuracy": 0.9345,
2422	  "accuracy_ci_lower": 0.9202,
2423	  "accuracy_ci_upper": 0.9479,
2424	  "pass_f1": 0.969,
2425	  "fail_f1": 0.873,
2426	  "pass_recall": 0.9906,
2427	  "fail_recall": 0.7935,
2428	  "n_test": 1190,
2429	  "n_unknown": 24
2430	}
2431	
2432	================================================================================
2433	EXP_ID: zeroshot_qwen7b_exception_only
2434	STATUS: DONE
2435	CONCLUSION: success
2436	MODEL_NAME: Qwen2.5-Coder-7B-Instruct
2437	METRICS: {
2438	  "accuracy": 0.8908,
2439	  "accuracy_ci_lower": 0.8731,
2440	  "accuracy_ci_upper": 0.9076,
2441	  "pass_precision": 0.8815,
2442	  "pass_recall": 0.9788,
2443	  "pass_f1": 0.9276,
2444	  "fail_precision": 0.9265,
2445	  "fail_recall": 0.6696,
2446	  "fail_f1": 0.7774,
2447	  "n_test": 1190,
2448	  "n_unknown": 0
2449	}
2450	
2451	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58051e01-f22c-4ab6-85eb-09aa7788a48a",
  "isSidechain": true,
  "promptId": "d3a99d3c-02c3-4d5e-9ec2-b28e1b492d4b",
  "agentId": "a86b080f191dc2217",
  "type": "user",
  "uuid": "055a4e4f-6a84-4ae5-8d9a-5aecf90eb6a6",
  "sourceToolAssistantUUID": "58051e01-f22c-4ab6-85eb-09aa7788a48a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "f5f4efcf-b091-4929-abdf-35aa1152d6be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-21T19:09:43.173Z_

That covers the complete output. Here is the full verbatim extraction of all 134 matching experiments:

---

**134 experiments matched out of 168 total.** All data below is verbatim from the registry.

---

### codellama13b_ae_only_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** CodeLlama-13b-Instruct-hf
- **METRICS:** `{"accuracy": 0.9908, "accuracy_ci_lower": 0.9849, "accuracy_ci_upper": 0.9958, "pass_f1": 0.9935, "fail_f1": 0.984, "majority_baseline": 0.7151}`

### codellama13b_exception_only_seed123
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** CodeLlama-13b-Instruct-hf
- **METRICS:** `{"accuracy": 1, "n": 1190, "errors": 0, "pass_precision": 1, "pass_recall": 1, "pass_f1": 1, "fail_precision": 1, "fail_recall": 1, "fail_f1": 1, "lift_over_majority": 0.2849}`

### codellama13b_exception_only_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** N/A
- **METRICS:** `{"accuracy": 0.9983, "accuracy_ci_lower": 0.9958, "accuracy_ci_upper": 1, "pass_f1": 0.9988, "fail_f1": 0.9971, "n_test": 1190}`

### codellama13b_exception_only_seed456
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** CodeLlama-13b-Instruct-hf
- **METRICS:** `{"accuracy": 0.9983, "n": 1190, "errors": 2, "pass_precision": 1, "pass_recall": 0.9976, "pass_f1": 0.9988, "fail_precision": 0.9941, "fail_recall": 1, "fail_f1": 0.9971}`

### codellama13b_full_trace_head2048_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** CodeLlama-13b-Instruct-hf
- **METRICS:** `{"accuracy": 0.7992, "majority_baseline": 0.7151, "lift": 0.084, "n_test": 1190, "pass_precision": 0.8566, "pass_recall": 0.8637, "pass_f1": 0.8602, "fail_precision": 0.6506, "fail_recall": 0.6372, "fail_f1": 0.6438, "train_loss": 0.0452, "eval_loss": 0.111, "accuracy_ci_lower": 0.7765, "accuracy_ci_upper": 0.8227}`

### codellama13b_full_trace_tail1024_seed42
- **STATUS:** DONE
- **CONCLUSION:** failed
- **MODEL_NAME:** CodeLlama-13b-Instruct-hf
- **METRICS:** (none)

### codellama13b_full_trace_tail1024_seed42_v2
- **STATUS:** DONE
- **CONCLUSION:** negative
- **MODEL_NAME:** CodeLlama-13b-Instruct-hf
- **METRICS:** `{"accuracy": 0.876, "accuracy_ci_lower": 0.856, "accuracy_ci_upper": 0.893, "majority_baseline": 0.715, "lift_pp": 16.1, "pass_precision": 0.85, "pass_recall": 1, "pass_f1": 0.92, "fail_precision": 1, "fail_recall": 0.56, "fail_f1": 0.72, "n_test": 1190, "train_loss": 0.0937, "eval_loss": 0.1859}`

### codellama13b_full_trace_tail1024_seed42_v3
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** N/A
- **METRICS:** `{"accuracy_epoch1": 0.9824, "accuracy_epoch3": 0.9756, "pass_f1_epoch1": 0.988, "fail_f1_epoch1": 0.968, "pass_f1_epoch3": 0.983, "fail_f1_epoch3": 0.955, "best_accuracy": 0.9824, "best_epoch": 1, "overfitting": true}`

### codellama13b_full_trace_tail2048_seed42
- **STATUS:** DONE
- **CONCLUSION:** failed
- **MODEL_NAME:** CodeLlama-13b-Instruct-hf
- **METRICS:** (none)

### codellama13b_full_trace_tail2048_seed42_v2
- **STATUS:** DONE
- **CONCLUSION:** negative
- **MODEL_NAME:** CodeLlama-13b-Instruct-hf
- **METRICS:** `{"accuracy_epoch1": 0.2849, "accuracy_epoch3": 0.2958, "pass_recall_epoch3": 0.016, "fail_recall_epoch3": 0.997, "majority_baseline": 0.715, "n_test": 1190, "note": "Catastrophic failure: model predicts fail for almost everything. Full-sequence loss dilution with CodeLlama tokenizer at 2048 tokens."}`

### codellama13b_full_trace_tail2048_seed42_v3
- **STATUS:** DONE
- **CONCLUSION:** negative
- **MODEL_NAME:** N/A
- **METRICS:** `{"accuracy_epoch1": 0.071, "accuracy_epoch3": 0.418, "pass_f1_epoch3": 0.416, "fail_f1_epoch3": 0.421, "pass_f1_epoch1": 0.035, "fail_f1_epoch1": 0.342, "train_loss": 0.785}`

### codellama13b_full_trace_tail256_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** CodeLlama-13b-Instruct-hf
- **METRICS:** `{"accuracy": 0.779, "accuracy_ci_lower": 0.757, "accuracy_ci_upper": 0.803, "pass_f1": 0.843, "fail_f1": 0.626, "pass_precision": 0.856, "pass_recall": 0.831, "fail_precision": 0.604, "fail_recall": 0.649, "majority_baseline": 0.715, "lift": 0.064, "train_loss": 0.245, "eval_loss": 0.615}`

### codellama13b_full_trace_tail384_seed42
- **STATUS:** DONE
- **CONCLUSION:** negative
- **MODEL_NAME:** CodeLlama-13b-Instruct-hf
- **METRICS:** `{"accuracy": 0.8269, "accuracy_ci_lower": 0.8067, "accuracy_ci_upper": 0.8471, "majority_baseline": 0.7151, "lift": 0.1118, "n": 1190, "pass_precision": 0.8314, "pass_recall": 0.9506, "pass_f1": 0.8871, "fail_precision": 0.8065, "fail_recall": 0.5162, "fail_f1": 0.6295}`

### codellama13b_full_trace_tail512_seed123
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** CodeLlama-13b-Instruct-hf
- **METRICS:** `{"accuracy": 0.9824, "accuracy_ci_lower": 0.9748, "accuracy_ci_upper": 0.9899, "majority_baseline": 0.7151, "lift": 0.2672, "n": 1190, "pass_precision": 0.9759, "pass_recall": 1, "pass_f1": 0.9878, "fail_precision": 1, "fail_recall": 0.9381, "fail_f1": 0.968, "seed_comparison": {"seed42_accuracy": 0.975, "seed123_accuracy": 0.9824, "diff": 0.0074, "note": "seed123 (98.24%) slightly exceeds seed42 (97.5%); both well above 97% - CodeLlama-13B tail-512 seed-robust"}}`

### codellama13b_full_trace_tail512_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** N/A
- **METRICS:** `{"accuracy": 0.9824, "accuracy_ci_lower": 0.9748, "accuracy_ci_upper": 0.9899, "majority_baseline": 0.7151, "lift": 0.2672, "n": 1190, "pass_precision": 0.9759, "pass_recall": 1, "pass_f1": 0.9878, "fail_precision": 1, "fail_recall": 0.9381, "fail_f1": 0.968}`

### codellama13b_full_trace_tail512_seed456
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** N/A
- **METRICS:** `{"accuracy": 0.9824, "accuracy_ci_lower": 0.9748, "accuracy_ci_upper": 0.9899, "majority_baseline": 0.7151, "lift": 0.2672, "n": 1190, "pass_precision": 0.9759, "pass_recall": 1, "pass_f1": 0.9878, "fail_precision": 1, "fail_recall": 0.9381, "fail_f1": 0.968, "seed_comparison": {"seed42_previous": 0.975, "seed123_accuracy": 0.9824, "seed456_accuracy": 0.9824}}`

### codellama13b_loop_only_seed42
- **STATUS:** DONE
- **CONCLUSION:** negative
- **MODEL_NAME:** N/A
- **METRICS:** `{"accuracy": 0.7706, "accuracy_ci_lower": 0.7487, "accuracy_ci_upper": 0.7941, "n": 1190, "majority_baseline": 0.7151, "lift": 0.0555, "fail_recall": 0.826, "pass_recall": 0.7485, "pass_precision": 0.92, "fail_precision": 0.57, "pass_f1": 0.82, "fail_f1": 0.67}`

### codellama13b_no_trace_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** codellama/CodeLlama-13b-Instruct-hf
- **METRICS:** `{"accuracy": 0.765, "n": 1190, "majority_baseline": 0.7151, "lift": 0.05, "pass_precision": 0.84, "pass_recall": 0.83, "pass_f1": 0.84, "fail_precision": 0.59, "fail_recall": 0.59, "fail_f1": 0.59, "accuracy_ci_lower": 0.738, "accuracy_ci_upper": 0.787}`

### codellama_exception_only_seed42
- **STATUS:** DONE
- **CONCLUSION:** killed
- **MODEL_NAME:** CodeLlama-13b-Instruct-hf
- **METRICS:** (none)

### codellama_no_trace_seed42
- **STATUS:** DONE
- **CONCLUSION:** killed
- **MODEL_NAME:** CodeLlama-13b-Instruct-hf
- **METRICS:** (none)

### debugbench_exception_only_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** N/A
- **METRICS:** `{"accuracy": 1, "majority_baseline": 0.5141, "lift": 0.4859, "n": 426, "pass_precision": 1, "pass_recall": 1, "pass_f1": 1, "fail_precision": 1, "fail_recall": 1, "fail_f1": 1, "accuracy_ci_wilson": [0.9914, 1], "accuracy_ci_bootstrap": [1, 1], "train_loss": 0.2435, "eval_loss": 0.4157, "train_runtime_sec": 837}`

### debugbench_no_trace_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen/Qwen2.5-Coder-7B-Instruct
- **METRICS:** `{"accuracy": 0.9671, "majority_baseline": 0.5141, "lift": 0.4531, "pass_precision": 1, "pass_recall": 0.936, "pass_f1": 0.967, "fail_precision": 0.937, "fail_recall": 1, "fail_f1": 0.967, "accuracy_ci": [0.948, 0.984], "train_loss": 0.249, "eval_loss": 0.532}`

### deepseek_ae_only_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** deepseek-ai/deepseek-coder-6.7b-instruct
- **METRICS:** `{"accuracy": 0.9874, "accuracy_ci_lower": 0.9807, "accuracy_ci_upper": 0.9933, "fail_recall": 0.959, "pass_recall": 0.999, "fail_f1": 0.977, "pass_f1": 0.991}`

### deepseek_exception_only_seed123
- **STATUS:** DONE
- **CONCLUSION:** killed
- **MODEL_NAME:** N/A
- **METRICS:** (none)

### deepseek_exception_only_seed123_v2
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** deepseek-ai/deepseek-coder-6.7b-instruct
- **METRICS:** `{"accuracy": 0.995}`

### deepseek_exception_only_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** deepseek-ai/deepseek-coder-6.7b-instruct
- **METRICS:** `{"accuracy": 0.9933, "majority_baseline": 0.7151, "lift": 0.2782, "n": 1190, "pass_precision": 1, "pass_recall": 0.9906, "pass_f1": 0.9953, "fail_precision": 0.9769, "fail_recall": 1, "fail_f1": 0.9883, "epoch1_checkpoint_eval": {"accuracy": 0.9983, "fail_recall": 1, "fail_precision": 0.9941, "pass_recall": 0.9976, "conclusion": "epoch1_better_by_0.50pp"}}`

### deepseek_exception_only_seed456
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** deepseek-ai/deepseek-coder-6.7b-instruct
- **METRICS:** `{"accuracy": 0.9933, "majority_baseline": 0.7151, "lift": 0.2782, "n": 1190, "pass_precision": 1, "pass_recall": 0.9906, "pass_f1": 0.9953, "fail_precision": 0.9769, "fail_recall": 1, "fail_f1": 0.9883, "accuracy_ci": [0.9882, 0.9975], "train_loss": 0.1225, "eval_loss": 0.4824, "train_runtime_sec": 6246, "seed_comparison": {"seed42_accuracy": 0.9933, "seed456_accuracy": 0.9933, "seed123_accuracy": 0.9109, "note": "seed42 and seed456 identical (99.33%); seed123 outlier (91.09%). 2/3 seeds robust."}, "epoch1_checkpoint_eval": {"accuracy": 0.993, "accuracy_ci": [0.988, 0.997], "fail_f1": 0.99, "fail_precision": 0.98, "fail_recall": 1, "pass_f1": 1, "pass_precision": 1, "pass_recall": 0.99, "conclusion": "epoch1 (99.3%) ~ epoch3 (99.33%), 1 epoch convergence confirmed"}}`

### deepseek_full_trace_head2048_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** deepseek-coder-6.7b-instruct
- **METRICS:** `{"accuracy": 0.787, "accuracy_ci_lower": 0.765, "accuracy_ci_upper": 0.81, "majority_baseline": 0.715, "lift_pp": 7.2, "pass_precision": 0.84, "pass_recall": 0.86, "pass_f1": 0.85, "fail_precision": 0.63, "fail_recall": 0.6, "fail_f1": 0.62}`

### deepseek_full_trace_seed42
- **STATUS:** DONE
- **CONCLUSION:** negative
- **MODEL_NAME:** deepseek-ai/deepseek-coder-6.7b-instruct
- **METRICS:** `{"accuracy_no_truncation": 0.2849, "accuracy_with_truncation_fix": 0.1059, "accuracy_with_truncation_fix_ci": [0.089, 0.123], "majority_baseline": 0.7151, "n": 1190, "note": "Both evals show model failure. No-truncation: all predict fail. With-truncation: garbage tokens. LoRA training itself failed due to label truncation during training."}`

### deepseek_full_trace_seed42_v2
- **STATUS:** DONE
- **CONCLUSION:** killed
- **MODEL_NAME:** deepseek-ai/deepseek-coder-6.7b-instruct
- **METRICS:** (none)

### deepseek_full_trace_seed42_v3
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** deepseek-ai/deepseek-coder-6.7b-instruct
- **METRICS:** `{"accuracy": 0.7916, "majority_baseline": 0.7151, "lift": 0.0765, "n": 1190, "pass_precision": 0.857, "pass_recall": 0.851, "pass_f1": 0.854, "fail_precision": 0.632, "fail_recall": 0.643, "fail_f1": 0.637, "accuracy_ci": [0.768, 0.813], "train_loss": 0.0547, "train_runtime_seconds": 8891, "epochs": 3, "reeval_discrepancy": {"reeval_accuracy": 0.285, "reeval_note": "RESOLVED: 28.5% was caused by eval max_length=16384 (OOD). Re-eval with max_length=2048 reproduces 79.16%. predictions.jsonl updated to maxlen2048 results.", "status": "RESOLVED"}}`

### deepseek_full_trace_tail1024_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** N/A
- **METRICS:** `{"accuracy": 0.9647, "accuracy_ci_lower": 0.9538, "accuracy_ci_upper": 0.9748, "pass_precision": 0.964, "pass_recall": 0.987, "pass_f1": 0.976, "fail_precision": 0.966, "fail_recall": 0.909, "fail_f1": 0.936, "majority_baseline": 0.7151, "n_test": 1190}`

### deepseek_full_trace_tail2048_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** DeepSeek-Coder-6.7B-Instruct
- **METRICS:** `{"accuracy": 0.9496, "accuracy_ci_lower": 0.937, "accuracy_ci_upper": 0.9622, "pass_precision": 0.9692, "pass_recall": 0.96, "pass_f1": 0.9646, "fail_precision": 0.902, "fail_recall": 0.9233, "fail_f1": 0.9125, "n_test": 1190}`

### deepseek_full_trace_tail256_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** deepseek-coder-6.7b-instruct
- **METRICS:** `{"accuracy": 0.7639, "accuracy_ci_lower": 0.7403, "accuracy_ci_upper": 0.7874, "pass_precision": 0.8058, "pass_recall": 0.8825, "pass_f1": 0.8424, "fail_precision": 0.6124, "fail_recall": 0.4661, "fail_f1": 0.5293, "majority_baseline": 0.7151, "lift": 0.0487, "eval_loss": 0.5117, "train_loss": 0.2367}`

### deepseek_full_trace_tail384_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** deepseek-coder-6.7b-instruct
- **METRICS:** `{"accuracy": 0.807, "accuracy_ci_lower": 0.786, "accuracy_ci_upper": 0.829, "majority_baseline": 0.715, "lift": 0.092, "n": 1190, "pass_precision": 0.83, "pass_recall": 0.92, "pass_f1": 0.87, "fail_precision": 0.73, "fail_recall": 0.51, "fail_f1": 0.6}`

### deepseek_full_trace_tail512_seed123
- **STATUS:** DONE
- **CONCLUSION:** failed
- **MODEL_NAME:** N/A
- **METRICS:** `{"error": "CUDA OOM at step 0/444", "exit_code": 1, "cause": "GPU 0 memory exhausted", "seed_comparison": {"seed42_accuracy": 0.9361, "seed123_accuracy": "N/A - OOM crash"}}`

### deepseek_full_trace_tail512_seed123_v2
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** deepseek-coder-6.7b-instruct
- **METRICS:** `{"accuracy": 0.9504, "majority_baseline": 0.7151, "lift": 0.2353, "n": 1190, "pass_precision": 0.976, "pass_recall": 0.9542, "pass_f1": 0.9649, "fail_precision": 0.8911, "fail_recall": 0.941, "fail_f1": 0.9154, "accuracy_ci": [0.9387, 0.963]}`

### deepseek_full_trace_tail512_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** deepseek-coder-6.7b-instruct
- **METRICS:** `{"accuracy": 0.939, "accuracy_ci_lower": 0.926, "accuracy_ci_upper": 0.953, "majority_baseline": 0.715, "lift_over_majority": 0.224, "pass_precision": 0.97, "pass_recall": 0.94, "pass_f1": 0.96, "fail_precision": 0.86, "fail_recall": 0.94, "fail_f1": 0.9, "n_test": 1190}`

### deepseek_full_trace_tail512_seed456
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** N/A
- **METRICS:** `{"accuracy": 0.9605, "accuracy_ci_lower": 0.9496, "accuracy_ci_upper": 0.9714, "majority_baseline": 0.7151, "lift": 0.2454, "n": 1190, "pass_precision": 0.9752, "pass_recall": 0.9694, "pass_f1": 0.9723, "fail_precision": 0.9244, "fail_recall": 0.9381, "fail_f1": 0.9312, "seed_comparison": {"seed42_accuracy": 0.9361, "seed456_accuracy": 0.9605}}`

### deepseek_loop_only_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** deepseek-ai/deepseek-coder-6.7b-instruct
- **METRICS:** `{"accuracy": 0.8126, "accuracy_ci_lower": 0.7908, "accuracy_ci_upper": 0.8345, "fail_recall": 0.6372, "pass_recall": 0.8825}`

### deepseek_no_trace_seed123
- **STATUS:** DONE
- **CONCLUSION:** killed
- **MODEL_NAME:** N/A
- **METRICS:** (none)

### deepseek_no_trace_seed42
- **STATUS:** DONE
- **CONCLUSION:** negative
- **MODEL_NAME:** deepseek-ai/deepseek-coder-6.7b-instruct
- **METRICS:** `{"accuracy": 0.7336, "majority_baseline": 0.7151, "lift": 0.0185, "n": 1190, "pass_precision": 0.817, "pass_recall": 0.808, "pass_f1": 0.813, "fail_precision": 0.532, "fail_recall": 0.546, "fail_f1": 0.539, "accuracy_ci": [0.708, 0.757], "lift_ci": [-0.009, 0.046]}`

### exception_only_nomarker_seed123
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-7B-Instruct
- **METRICS:** `{"accuracy": 0.9832, "n": 1190, "ci_95": [0.9756, 0.9899], "pass_f1": 0.9882, "fail_f1": 0.9705, "pass_precision": 0.9882, "pass_recall": 0.9882, "fail_precision": 0.9705, "fail_recall": 0.9705, "lift_over_majority": 0.2681}`

### exception_only_nomarker_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-7B-Instruct
- **METRICS:** `{"accuracy": 0.9655, "n": 1190, "accuracy_ci": [0.955, 0.976]}`

### exception_only_nomarker_seed456
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-7B-Instruct
- **METRICS:** `{"accuracy": 0.9807, "n": 1190, "errors": 23, "ci_95": [0.9712, 0.9871], "pass_f1": 0.9865, "fail_f1": 0.9658, "pass_precision": 0.9836, "pass_recall": 0.9894, "fail_precision": 0.9731, "fail_recall": 0.9587, "lift_over_majority": 0.266}`

### exception_only_padded2048_seed42
- **STATUS:** RUNNING
- **CONCLUSION:** N/A
- **MODEL_NAME:** Qwen2.5-Coder-7B-Instruct
- **METRICS:** (none)

### exception_only_seed123
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-7B-Instruct
- **METRICS:** `{"accuracy": 0.9983, "accuracy_ci": [0.9958, 1], "majority_baseline": 0.7151, "lift": 0.2832, "n": 1190, "pass_precision": 1, "pass_recall": 0.9976, "pass_f1": 0.9988, "fail_precision": 0.9941, "fail_recall": 1, "fail_f1": 0.9971, "train_loss": 0.1096, "train_runtime_sec": 7507, "epochs": 3, "seed_comparison": {"seed42_accuracy": 0.9983, "seed456_accuracy": 0.9983, "seed123_accuracy": 0.9983, "max_diff": 0, "note": "identical accuracy to 4 decimal places across all 3 seeds (42/456/123); each has exactly 2/1190 errors; exception_only fully seed-robust"}}`

### exception_only_seed456
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-7B-Instruct
- **METRICS:** `{"accuracy": 0.9983, "accuracy_ci": [0.9958, 1], "majority_baseline": 0.7151, "lift": 0.2832, "n": 1190, "pass_precision": 1, "pass_recall": 0.9976, "pass_f1": 0.9988, "fail_precision": 0.9941, "fail_recall": 1, "fail_f1": 0.9971, "vs_seed42": {"seed42_accuracy": 0.9983, "seed456_accuracy": 0.9983, "diff": 0, "note": "identical accuracy to 4 decimal places"}, "train_loss": 0.1087, "eval_loss": 0.4629, "train_runtime_sec": 4541, "epochs": 3}`

### fewshot_gpt41_exception_only_0shot
- **STATUS:** DONE
- **CONCLUSION:** negative
- **MODEL_NAME:** gpt-4.1
- **METRICS:** `{"accuracy": 0.8218, "fail_f1": 0.7452}`

### fewshot_gpt41_exception_only_3shot
- **STATUS:** DONE
- **CONCLUSION:** negative
- **MODEL_NAME:** gpt-4.1
- **METRICS:** `{"accuracy": 0.8193, "fail_f1": 0.7413}`

### fewshot_gpt41_no_trace_0shot
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** gpt-4.1
- **METRICS:** `{"accuracy": 0.7731, "fail_f1": 0.6608}`

### fewshot_gpt4o_exception_only_0shot
- **STATUS:** DONE
- **CONCLUSION:** negative
- **MODEL_NAME:** gpt-4o
- **METRICS:** `{"accuracy": 0.8798, "fail_f1": 0.8228}`

### fewshot_gpt4o_exception_only_3shot
- **STATUS:** DONE
- **CONCLUSION:** negative
- **MODEL_NAME:** gpt-4o
- **METRICS:** `{"accuracy": 0.8681, "fail_f1": 0.7995}`

### fewshot_gpt4o_no_trace_0shot
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** gpt-4o
- **METRICS:** `{"accuracy": 0.8445, "fail_f1": 0.7543}`

### fewshot_qwen7b_exception_only
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-7B-Instruct
- **METRICS:** `{"accuracy": 0.9084, "accuracy_ci_lower": 0.8908, "accuracy_ci_upper": 0.9244, "pass_precision": 0.9245, "pass_recall": 0.9495, "pass_f1": 0.9368, "fail_precision": 0.8639, "fail_recall": 0.8053, "fail_f1": 0.8336, "n_test": 1190, "n_unknown": 0}`

### full_trace_1024tok_seed42
- **STATUS:** DONE
- **CONCLUSION:** negative
- **MODEL_NAME:** Qwen/Qwen2.5-Coder-7B-Instruct
- **METRICS:** `{"accuracy": 0.7723, "majority_baseline": 0.7151, "lift": 0.0571, "n": 1190, "accuracy_ci": [0.7487, 0.7958], "pass_precision": 0.9006, "pass_recall": 0.7662, "pass_f1": 0.8279, "fail_precision": 0.573, "fail_recall": 0.7876, "fail_f1": 0.6634, "train_loss": 0.0634, "train_runtime_sec": 5553, "epochs": 3}`

### full_trace_2048tok_seed42
- **STATUS:** DONE
- **CONCLUSION:** killed
- **MODEL_NAME:** N/A
- **METRICS:** (none)

### full_trace_256tok_seed42
- **STATUS:** DONE
- **CONCLUSION:** negative
- **MODEL_NAME:** Qwen/Qwen2.5-Coder-7B-Instruct
- **METRICS:** `{"accuracy": 0.7882, "majority_baseline": 0.7151, "lift": 0.0731, "n": 1190, "pass_precision": 0.903, "pass_recall": 0.788, "pass_f1": 0.842, "fail_precision": 0.597, "fail_recall": 0.788, "fail_f1": 0.679, "accuracy_ci": [0.764, 0.81], "train_loss": 0.1094, "train_runtime_sec": 3047, "epochs": 3}`

### full_trace_512tok_seed42
- **STATUS:** DONE
- **CONCLUSION:** negative
- **MODEL_NAME:** Qwen/Qwen2.5-Coder-7B-Instruct
- **METRICS:** `{"accuracy": 0.8042, "majority_baseline": 0.7151, "lift": 0.0891, "pass_precision": 0.8705, "pass_recall": 0.8531, "pass_f1": 0.8617, "fail_precision": 0.6489, "fail_recall": 0.6814, "fail_f1": 0.6647, "n": 1190, "accuracy_ci": [0.7815, 0.8261]}`

### full_trace_label_only_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** N/A
- **METRICS:** `{"accuracy": 0.8622, "accuracy_ci_lower": 0.8437, "accuracy_ci_upper": 0.8807, "majority_baseline": 0.7151, "lift": 0.1471, "n": 1190, "pass_precision": 0.8821, "pass_recall": 0.9318, "pass_f1": 0.9063, "fail_precision": 0.8007, "fail_recall": 0.6873, "fail_f1": 0.7397, "train_loss": 0.2505, "eval_loss": 0.3205, "lift_vs_notrace": 0.1109, "lift_vs_notrace_ci_lower": 0.0849, "lift_vs_notrace_ci_upper": 0.137, "lift_vs_standard_fulltrace": 0.0445, "lift_vs_standard_fulltrace_ci_lower": 0.0235, "lift_vs_standard_fulltrace_ci_upper": 0.0655, "lift_vs_standard_fulltrace_pvalue": 0}`

### full_trace_seed42
- **STATUS:** DONE
- **CONCLUSION:** killed
- **MODEL_NAME:** Qwen2.5-Coder-7B-Instruct
- **METRICS:** `{"train_loss": 0.037, "eval_loss": 0.084, "eval_mean_token_accuracy": 0.984, "accuracy": 0.284, "majority_baseline": 0.7151, "lift": -0.431, "pass_precision": 0.88, "pass_recall": 0.08, "pass_f1": 0.16, "fail_precision": 0.31, "fail_recall": 0.97, "fail_f1": 0.57}`

### full_trace_seed42_v2
- **STATUS:** DONE
- **CONCLUSION:** negative
- **MODEL_NAME:** N/A
- **METRICS:** `{"accuracy": 0.284, "majority_baseline": 0.7151, "lift": -0.4311, "n": 1190, "pass_precision": 0.923, "pass_recall": 0.085, "pass_f1": 0.155, "fail_precision": 0.445, "fail_recall": 0.785, "fail_f1": 0.568, "train_loss": 0.0373, "eval_loss": 0.082, "eval_mean_token_accuracy": 0.984}`

### full_trace_seed42_v5
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** N/A
- **METRICS:** `{"accuracy": 0.8176, "majority_baseline": 0.7151, "lift": 0.1025, "n": 1190, "pass_precision": 0.8774, "pass_recall": 0.866, "pass_f1": 0.8717, "fail_precision": 0.6743, "fail_recall": 0.6962, "fail_f1": 0.6851, "accuracy_ci_lower": 0.797, "accuracy_ci_upper": 0.839, "lift_vs_notrace": 0.0664, "lift_vs_notrace_ci_lower": 0.0437, "lift_vs_notrace_ci_upper": 0.0899, "train_loss": 0.05, "eval_loss": 0.0867, "wall_clock_seconds": 7852, "epoch_level": {"epoch1_accuracy": 0.8303, "epoch2_accuracy": 0.763, "final_accuracy": 0.8176, "trend": "non_monotonic_epoch1_best_epoch2_collapse"}}`

### full_trace_tail256_seed42
- **STATUS:** DONE
- **CONCLUSION:** negative
- **MODEL_NAME:** Qwen2.5-Coder-7B-Instruct
- **METRICS:** `{"accuracy": 0.789, "accuracy_ci_lower": 0.765, "accuracy_ci_upper": 0.813, "pass_f1": 0.845, "fail_f1": 0.671, "n_test": 1190}`

### full_trace_tail_1024_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-7B-Instruct
- **METRICS:** `{"accuracy": 0.9647, "accuracy_ci": [0.9546, 0.9748], "majority_baseline": 0.7151, "lift": 0.2496, "n": 1190, "pass_f1": 0.9753, "fail_f1": 0.9381}`

### full_trace_tail_256_seed42
- **STATUS:** DONE
- **CONCLUSION:** negative
- **MODEL_NAME:** Qwen2.5-Coder-7B-Instruct
- **METRICS:** `{"accuracy": 0.7748, "accuracy_ci": [0.7496, 0.7975], "majority_baseline": 0.7151, "lift": 0.0597, "n": 1190, "pass_f1": 0.8333, "fail_f1": 0.6528}`

### full_trace_tail_512_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen/Qwen2.5-Coder-7B-Instruct
- **METRICS:** `{"accuracy": 0.936, "accuracy_ci": [0.922, 0.95], "majority_baseline": 0.7151, "lift": 0.221, "n": 1190, "pass_precision": 0.98, "pass_recall": 0.93, "pass_f1": 0.95, "fail_precision": 0.85, "fail_recall": 0.94, "fail_f1": 0.89}`

### full_trace_tail_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen/Qwen2.5-Coder-7B-Instruct
- **METRICS:** `{"accuracy": 0.973, "accuracy_ci": [0.964, 0.982], "majority_baseline": 0.7151, "lift": 0.258, "n": 1190, "pass_precision": 0.98, "pass_recall": 0.99, "pass_f1": 0.98, "fail_precision": 0.97, "fail_recall": 0.94, "fail_f1": 0.95}`

### no_trace_seed42
- **STATUS:** DONE
- **CONCLUSION:** killed
- **MODEL_NAME:** N/A
- **METRICS:** (none)

### no_trace_seed42_v2
- **STATUS:** DONE
- **CONCLUSION:** killed
- **MODEL_NAME:** N/A
- **METRICS:** (none)

### no_trace_seed42_v3
- **STATUS:** DONE
- **CONCLUSION:** killed
- **MODEL_NAME:** Qwen2.5-Coder-7B-Instruct
- **METRICS:** `{"train_loss": 0.18, "eval_loss": 0.645, "eval_mean_token_accuracy": 0.89, "accuracy": 0.7513, "majority_baseline": 0.7151, "lift": 0.0361, "pass_precision": 0.8776, "pass_recall": 0.7579, "pass_f1": 0.8134, "fail_precision": 0.5473, "fail_recall": 0.7345, "fail_f1": 0.6272}`

### no_trace_seed42_v4
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** N/A
- **METRICS:** `{"accuracy": 0.7513, "majority_baseline": 0.7151, "lift": 0.0361, "pass_precision": 0.8776, "pass_recall": 0.7579, "pass_f1": 0.8134, "fail_precision": 0.5473, "fail_recall": 0.7345, "fail_f1": 0.6272, "train_loss": 0.18, "eval_loss": 0.6454, "eval_mean_token_accuracy": 0.8897}`

### no_trace_seed42_v5
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-7B-Instruct
- **METRICS:** `{"accuracy": 0.7513, "accuracy_ci_lower": 0.7277, "accuracy_ci_upper": 0.7748, "majority_baseline": 0.7151, "lift": 0.0361, "lift_ci_lower": 0.0042, "lift_ci_upper": 0.0706, "n": 1190, "pass_precision": 0.8776, "pass_recall": 0.7579, "pass_f1": 0.8134, "fail_precision": 0.5473, "fail_recall": 0.7345, "fail_f1": 0.6272, "epoch_level": {"epoch1_accuracy": 0.7429, "epoch2_accuracy": 0.763, "final_accuracy": 0.7513, "trend": "non_monotonic_epoch2_best"}}`

### qwen1.5b_exception_only_seed42
- **STATUS:** DONE
- **CONCLUSION:** killed
- **MODEL_NAME:** Qwen2.5-Coder-1.5B-Instruct
- **METRICS:** (none)

### qwen1.5b_full_trace_seed42
- **STATUS:** DONE
- **CONCLUSION:** killed
- **MODEL_NAME:** Qwen2.5-Coder-1.5B-Instruct
- **METRICS:** (none)

### qwen1.5b_no_trace_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-1.5B-Instruct
- **METRICS:** `{"accuracy": 0.7261, "accuracy_ci_lower": 0.7008, "accuracy_ci_upper": 0.7529, "majority_baseline": 0.7151, "lift_pp": 1.09, "pass_precision": 0.831, "pass_recall": 0.774, "pass_f1": 0.802, "fail_precision": 0.516, "fail_recall": 0.605, "fail_f1": 0.557}`

### qwen1.5b_vota_seed42
- **STATUS:** DONE
- **CONCLUSION:** killed
- **MODEL_NAME:** Qwen2.5-Coder-1.5B-Instruct
- **METRICS:** (none)

### qwen15b_ae_only_seed123
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-1.5B-Instruct
- **METRICS:** `{"accuracy": 0.9857, "majority_baseline": 0.715, "lift_pp": 27.1, "fail_f1": 0.975}`

### qwen15b_ae_only_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-1.5B-Instruct
- **METRICS:** `{"accuracy": 0.9908, "majority_baseline": 0.7151, "lift": 0.2756, "pass_precision": 1, "pass_recall": 0.987, "pass_f1": 0.9935, "fail_precision": 0.9686, "fail_recall": 1, "fail_f1": 0.984, "n": 1190, "accuracy_ci_lower": 0.9849, "accuracy_ci_upper": 0.9958}`

### qwen15b_exception_only_seed123
- **STATUS:** DONE
- **CONCLUSION:** failed
- **MODEL_NAME:** N/A
- **METRICS:** `{"error": "CUDA OOM at step 3/444", "exit_code": 1, "cause": "GPU 0 had 45.15 GiB PyTorch allocated", "seed_comparison": {"seed42_accuracy": 0.9983, "seed123_accuracy": "N/A - OOM crash"}}`

### qwen15b_exception_only_seed123_v2
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** N/A
- **METRICS:** `{"accuracy": 0.9983, "accuracy_ci_lower": 0.9958, "accuracy_ci_upper": 1, "seed_comparison": {"seed42_accuracy": 0.9983, "seed456_accuracy": 0.9983, "seed123_accuracy": 0.9983}}`

### qwen15b_exception_only_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** N/A
- **METRICS:** `{"accuracy": 0.9983, "accuracy_ci_lower": 0.9958, "accuracy_ci_upper": 1, "majority_baseline": 0.7151, "lift": 0.283, "n": 1190, "pass_precision": 1, "pass_recall": 0.9976, "pass_f1": 0.9988, "fail_precision": 0.9941, "fail_recall": 1, "fail_f1": 0.9971, "train_loss": 0.1347, "eval_loss": 0.5761, "wall_clock_seconds": 1762}`

### qwen15b_exception_only_seed456
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-1.5B-Instruct
- **METRICS:** `{"accuracy": 0.9983, "accuracy_ci_lower": 0.9958, "accuracy_ci_upper": 1, "majority_baseline": 0.7151, "lift": 0.2832, "n": 1190, "pass_precision": 1, "pass_recall": 0.9976, "pass_f1": 0.9988, "fail_precision": 0.9941, "fail_recall": 1, "fail_f1": 0.9971, "seed_comparison": {"seed42_accuracy": 0.9983, "seed456_accuracy": 0.9983, "diff": 0, "note": "Identical to seed42 to 4 decimal places - exception_only fully seed-robust on Qwen-1.5B"}}`

### qwen15b_full_trace_head2048_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-1.5B-Instruct
- **METRICS:** `{"accuracy": 0.7529, "accuracy_ci_lower": 0.7286, "accuracy_ci_upper": 0.7782, "pass_precision": 0.799, "pass_recall": 0.874, "pass_f1": 0.835, "fail_precision": 0.587, "fail_recall": 0.448, "fail_f1": 0.508, "n_test": 1190}`

### qwen15b_full_trace_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** N/A
- **METRICS:** `{"accuracy": 0.7706, "n": 1190}`

### qwen15b_full_trace_tail1024_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-1.5B-Instruct
- **METRICS:** `{"accuracy": 0.966, "accuracy_ci_low": 0.955, "accuracy_ci_high": 0.976, "pass_precision": 0.96, "pass_recall": 0.99, "pass_f1": 0.98, "fail_precision": 0.97, "fail_recall": 0.91, "fail_f1": 0.94, "eval_loss": 0.1983, "train_loss": 0.1187, "majority_baseline": 0.715, "lift_over_majority_pp": 25}`

### qwen15b_full_trace_tail2048_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-1.5B-Instruct
- **METRICS:** `{"accuracy": 0.979, "accuracy_ci_lower": 0.9706, "accuracy_ci_upper": 0.9874, "pass_precision": 0.9758, "pass_recall": 0.9953, "pass_f1": 0.9855, "fail_precision": 0.9876, "fail_recall": 0.9381, "fail_f1": 0.9622, "n_test": 1190}`

### qwen15b_full_trace_tail256_seed42
- **STATUS:** DONE
- **CONCLUSION:** negative
- **MODEL_NAME:** Qwen2.5-Coder-1.5B-Instruct
- **METRICS:** `{"accuracy": 0.726, "accuracy_ci_lower": 0.7, "accuracy_ci_upper": 0.753, "majority_baseline": 0.715, "lift_over_majority": 0.011, "lift_ci_lower": -0.021, "lift_ci_upper": 0.044, "pass_precision": 0.82, "pass_recall": 0.79, "pass_f1": 0.8, "fail_precision": 0.52, "fail_recall": 0.57, "fail_f1": 0.54, "eval_loss": 0.5936, "train_loss": 0.2687}`

### qwen15b_full_trace_tail384_seed42
- **STATUS:** DONE
- **CONCLUSION:** negative
- **MODEL_NAME:** Qwen2.5-Coder-1.5B-Instruct
- **METRICS:** `{"accuracy": 0.7361, "majority_baseline": 0.7151, "lift": 0.021, "n": 1190, "pass_precision": 0.8069, "pass_recall": 0.8296, "pass_f1": 0.8181, "fail_precision": 0.5397, "fail_recall": 0.5015, "fail_f1": 0.5199, "accuracy_ci": [0.7101, 0.7622]}`

### qwen15b_full_trace_tail512_seed123
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** N/A
- **METRICS:** `{"accuracy": 0.9765, "accuracy_ci_lower": 0.9681, "accuracy_ci_upper": 0.9849, "majority_baseline": 0.7151, "lift": 0.2613, "n": 1190, "pass_precision": 0.9757, "pass_recall": 0.9918, "pass_f1": 0.9837, "fail_precision": 0.9785, "fail_recall": 0.9381, "fail_f1": 0.9578, "seed_comparison": {"seed42_accuracy": 0.956, "seed123_accuracy": 0.9765, "note": "seed123 (97.65%) exceeds seed42 (95.6%) by 2pp; both in convergence band post-phase-transition"}}`

### qwen15b_full_trace_tail512_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** N/A
- **METRICS:** `{"accuracy": 0.956, "accuracy_ci_lower": 0.945, "accuracy_ci_upper": 0.968, "majority_baseline": 0.715, "lift_over_majority": 0.241, "eval_loss": 0.263, "train_loss": 0.154, "pass_precision": 0.98, "pass_recall": 0.96, "pass_f1": 0.97, "fail_precision": 0.91, "fail_recall": 0.94, "fail_f1": 0.92, "eval_mean_token_accuracy": 0.949}`

### qwen15b_full_trace_tail512_seed456
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** N/A
- **METRICS:** `{"accuracy": 0.9672, "accuracy_ci_lower": 0.9563, "accuracy_ci_upper": 0.9773, "majority_baseline": 0.7151, "lift": 0.2521, "n": 1190, "pass_precision": 0.9765, "pass_recall": 0.9777, "pass_f1": 0.9771, "fail_precision": 0.9438, "fail_recall": 0.941, "fail_f1": 0.9424, "seed_comparison": {"seed42_accuracy": 0.956, "seed123_accuracy": 0.9765, "seed456_accuracy": 0.9672, "note": "seed456 (96.72%) within convergence band [95.6%, 97.65%], confirming seed robustness post-phase-transition"}}`

### qwen15b_label_only_seed123_v2
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-1.5B-Instruct
- **METRICS:** `{"accuracy": 0.8134, "accuracy_ci_lower": 0.7924, "accuracy_ci_upper": 0.8345, "majority_baseline": 0.7151, "lift_pp": 9.83, "pass_recall": 0.94, "pass_precision": 0.824, "pass_f1": 0.878, "fail_recall": 0.496, "fail_precision": 0.767, "fail_f1": 0.602}`

### qwen15b_label_only_seed42
- **STATUS:** DONE
- **CONCLUSION:** killed
- **MODEL_NAME:** N/A
- **METRICS:** (none)

### qwen15b_label_only_seed42_v2
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-1.5B-Instruct
- **METRICS:** `{"accuracy": 0.789, "accuracy_ci_lower": 0.766, "accuracy_ci_upper": 0.812, "majority_baseline": 0.715, "lift_pp": 7.4, "pass_recall": 0.91, "pass_precision": 0.82, "pass_f1": 0.86, "fail_recall": 0.5, "fail_precision": 0.68, "fail_f1": 0.57}`

### qwen15b_label_only_seed456_v2
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-1.5B-Instruct
- **METRICS:** `{"accuracy": 0.8252, "pass_f1": 0.885, "fail_f1": 0.639, "pass_precision": 0.837, "pass_recall": 0.938, "fail_precision": 0.776, "fail_recall": 0.543, "train_loss": 0.2394, "eval_loss": 0.3064, "majority_baseline": 0.715}`

### qwen15b_loop_only_seed123
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-1.5B-Instruct
- **METRICS:** `{"accuracy": 0.8109, "pass_f1": 0.8737, "fail_f1": 0.6244, "pass_precision": 0.8366, "pass_recall": 0.9142, "fail_precision": 0.7192, "fail_recall": 0.5516, "train_loss": 0.0843, "train_runtime_sec": 2659.73}`

### qwen15b_loop_only_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-1.5B-Instruct
- **METRICS:** `{"accuracy": 0.7832, "pass_f1": 0.8526, "fail_f1": 0.5905, "pass_precision": 0.8298, "pass_recall": 0.8766, "fail_precision": 0.6392, "fail_recall": 0.5487, "train_loss": 0.0847, "train_runtime_sec": 2679}`

### qwen15b_loop_only_seed456
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-1.5B-Instruct
- **METRICS:** `{"accuracy": 0.792, "ci_95": [0.768, 0.813], "majority_baseline": 0.715, "lift_pp": 7.6, "pass_precision": 0.85, "pass_recall": 0.86, "pass_f1": 0.86, "fail_precision": 0.64, "fail_recall": 0.62, "fail_f1": 0.63}`

### qwen15b_no_trace_seed123
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-1.5B-Instruct
- **METRICS:** `{"accuracy": 0.7588, "accuracy_ci_lower": 0.7328, "accuracy_ci_upper": 0.7824, "majority_baseline": 0.7151, "lift": 0.0437, "pass_precision": 0.8279, "pass_recall": 0.8367, "pass_f1": 0.8323, "fail_precision": 0.5788, "fail_recall": 0.5634, "fail_f1": 0.571, "train_loss": 0.2221, "eval_loss": 0.7838}`

### qwen15b_no_trace_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** N/A
- **METRICS:** `{"accuracy": 0.6731, "n": 1190, "pass_f1": 0.7527, "fail_f1": 0.518, "lift_over_majority": -0.042, "training_time_sec": 851}`

### qwen15b_no_trace_seed456
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-1.5B-Instruct
- **METRICS:** `{"accuracy": 0.7387, "fail_f1": 0.5266, "pass_f1": 0.8195, "eval_loss": 0.7725, "train_loss": 0.2226, "fail_precision": 0.544, "fail_recall": 0.5103, "pass_precision": 0.8096, "pass_recall": 0.8296}`

### qwen15b_nomarker_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-1.5B-Instruct
- **METRICS:** `{"accuracy": 0.978, "n": 1190, "accuracy_ci": [0.97, 0.986], "majority_baseline": 0.715, "lift": 0.263, "pass_precision": 0.97, "pass_recall": 1, "pass_f1": 0.98, "fail_precision": 1, "fail_recall": 0.92, "fail_f1": 0.96}`

### qwen15b_vota_seed123
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-1.5B-Instruct
- **METRICS:** `{"accuracy": 0.995, "ci_95": [0.9908, 0.9983], "pass_f1": 0.9965, "fail_f1": 0.9912, "lift_pp": 28, "n_samples": 1190}`

### qwen15b_vota_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** N/A
- **METRICS:** `{"accuracy": 0.9958, "n": 1190, "pass_recall": 0.9976, "fail_recall": 0.9912, "pass_f1": 0.9971, "fail_f1": 0.9926, "training_time_sec": 2922}`

### qwen7b_exception_only_dynamics_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-7B-Instruct
- **METRICS:** `{"step50_acc": 0.9933, "step100_acc": 0.9933, "step150_acc": 0.9933, "step200_acc": 0.9983, "step250_acc": 0.9983, "step300_acc": 0.9983, "step350_acc": 0.9983, "step400_acc": 0.9983, "step444_acc": 0.9983, "saturation_step": 200, "final_loss": 0.0329, "pass_f1": 0.9988, "fail_f1": 0.9971}`

### qwen7b_full_trace_dynamics_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-7B-Instruct
- **METRICS:** `{"step50_acc": 0.8739, "step100_acc": 0.821, "step150_acc": 0.8571, "step200_acc": 0.8655, "step250_acc": 0.8739, "step300_acc": 0.8487, "step350_acc": 0.8882, "step400_acc": 0.8571, "step444_acc": 0.8824, "best_step": 350, "best_acc": 0.8882, "final_loss": 0.0085}`

### qwen7b_full_trace_head2048_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** N/A
- **METRICS:** `{"accuracy_epoch1": 0.816, "accuracy_epoch3": 0.81, "pass_f1_epoch1": 0.87, "fail_f1_epoch1": 0.686, "pass_f1_epoch3": 0.866, "fail_f1_epoch3": 0.674, "best_accuracy": 0.816, "best_epoch": 1}`

### qwen7b_full_trace_label_only_seed123
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-7B-Instruct
- **METRICS:** `{"accuracy": 0.8689, "accuracy_ci_lower": 0.8496, "accuracy_ci_upper": 0.8874, "pass_f1": 0.9121, "fail_f1": 0.7426, "pass_precision": 0.8765, "pass_recall": 0.9506, "fail_precision": 0.8427, "fail_recall": 0.6637, "majority_baseline": 0.7151, "lift": 0.1538, "train_loss": 0.2425, "eval_loss": 0.2787}`

### qwen7b_full_trace_label_only_seed456
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-7B-Instruct
- **METRICS:** `{"accuracy": 0.847, "accuracy_ci_lower": 0.827, "accuracy_ci_upper": 0.866, "pass_f1": 0.9, "fail_f1": 0.71, "pass_precision": 0.87, "pass_recall": 0.92, "fail_precision": 0.76, "fail_recall": 0.67, "majority_baseline": 0.7151, "lift": 0.1319, "train_loss": 0.2452, "eval_loss": 0.3366}`

### qwen7b_full_trace_seed123
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-7B-Instruct
- **METRICS:** `{"accuracy": 0.802, "ci_lower": 0.778, "ci_upper": 0.825, "majority_baseline": 0.715, "lift_pp": 8.7, "pass_precision": 0.88, "pass_recall": 0.84, "pass_f1": 0.86, "fail_precision": 0.64, "fail_recall": 0.7, "fail_f1": 0.67, "train_loss": 0.0415, "eval_loss": 0.0827}`

### qwen7b_full_trace_seed456
- **STATUS:** DONE
- **CONCLUSION:** failed
- **MODEL_NAME:** Qwen2.5-Coder-7B-Instruct
- **METRICS:** (none)

### qwen7b_full_trace_seed456_v2
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-7B-Instruct
- **METRICS:** `{"accuracy": 0.8235, "ci_lower": 0.8017, "ci_upper": 0.8454, "majority_baseline": 0.7151, "lift_pp": 10.84, "pass_precision": 0.8885, "pass_recall": 0.8613, "pass_f1": 0.8747, "fail_precision": 0.6767, "fail_recall": 0.7286, "fail_f1": 0.7017, "train_loss": 0.0416, "eval_loss": 0.0794}`

### qwen7b_full_trace_tail384_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-7B-Instruct
- **METRICS:** `{"accuracy": 0.798, "accuracy_ci_lower": 0.776, "accuracy_ci_upper": 0.821, "majority_baseline": 0.715, "lift": 0.083, "n": 1190, "pass_precision": 0.89, "pass_recall": 0.82, "pass_f1": 0.85, "fail_precision": 0.62, "fail_recall": 0.75, "fail_f1": 0.68}`

### qwen7b_full_trace_tail512_seed123
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** N/A
- **METRICS:** `{"accuracy": 0.9597, "accuracy_ci_lower": 0.9487, "accuracy_ci_upper": 0.9706, "majority_baseline": 0.7151, "lift": 0.2445, "n": 1190, "pass_precision": 0.9751, "pass_recall": 0.9683, "pass_f1": 0.9717, "fail_precision": 0.9217, "fail_recall": 0.9381, "fail_f1": 0.9298, "seed_comparison": {"seed42_accuracy": 0.936, "seed123_accuracy": 0.9597}}`

### qwen7b_full_trace_tail512_seed42
- **STATUS:** DONE
- **CONCLUSION:** failed
- **MODEL_NAME:** Qwen2.5-Coder-7B-Instruct
- **METRICS:** (none)

### qwen7b_full_trace_tail512_seed456
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-7B-Instruct
- **METRICS:** `{"accuracy": 0.9765, "majority_baseline": 0.7151, "lift": 0.2613, "n": 1190, "pass_precision": 0.9746, "pass_recall": 0.9929, "pass_f1": 0.9837, "fail_precision": 0.9814, "fail_recall": 0.9351, "fail_f1": 0.9577, "accuracy_ci": [0.9681, 0.9849]}`

### qwen7b_vota_seed123
- **STATUS:** DONE (note: matched via category 2 "vota_" prefix -- but this is qwen7b_vota, not vota_ prefix; included because it contains "full_trace"/"no_trace"/"exception_only" -- actually included because it was in the qwen7b group via full_trace/exception_only matching)

Actually let me clarify: qwen7b_vota_seed123 and qwen7b_vota_seed456 were NOT matched by the filter criteria (they don't start with "qwen15b_" or "vota_", don't contain "full_trace", "no_trace", or "exception_only", and aren't in the specific named list). Let me verify which ones were actually output.

Looking back at the Python script output, the matching function does not match `qwen7b_vota_*` -- those were not in the output. The complete list continues with:

### vota_ae_only_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-7B-Instruct
- **METRICS:** `{"accuracy": 0.9992, "accuracy_ci": [0.9975, 1], "bootstrap_pairwise": {"ae_only_vs_no_trace": {"diff": 0.2479, "ci": [0.2235, 0.2731], "p_value": 0, "significant": true}, "ae_only_vs_exception_only": {"diff": 0.0008, "ci": [-0.0017, 0.0034], "p_value": 0.8002, "significant": false}, "ae_only_vs_vota": {"diff": 0.005, "ci": [0.0017, 0.0092], "p_value": 0.0046, "significant": true}}, "config": {"n_bootstrap": 10000, "seed": 42, "method": "paired_bootstrap"}}`

### vota_exception_only_seed42
- **STATUS:** DONE
- **CONCLUSION:** failed
- **MODEL_NAME:** Qwen2.5-Coder-7B-Instruct
- **METRICS:** (none)

### vota_exception_only_seed42_v2
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-7B-Instruct
- **METRICS:** `{"accuracy": 0.9983, "majority_baseline": 0.7151, "lift": 0.2832, "n": 1190, "pass_precision": 1, "pass_recall": 0.998, "pass_f1": 0.999, "fail_precision": 0.994, "fail_recall": 1, "fail_f1": 0.997, "lift_vs_notrace": 0.2471, "lift_vs_notrace_ci_lower": 0.2227, "lift_vs_notrace_ci_upper": 0.2714, "lift_vs_fulltrace": 0.1807, "lift_vs_fulltrace_ci_lower": 0.1588, "lift_vs_fulltrace_ci_upper": 0.2034, "lift_vs_vota": 0.0067, "lift_vs_vota_ci_lower": 0.0017, "lift_vs_vota_ci_upper": 0.0126, "lift_vs_vota_pvalue": 0.01}`

### vota_loop_only_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-7B-Instruct
- **METRICS:** `{"accuracy": 0.8563, "majority_baseline": 0.7151, "lift": 0.1412, "n": 1190, "pass_precision": 0.9239, "pass_recall": 0.8707, "pass_f1": 0.8966, "fail_precision": 0.7165, "fail_recall": 0.8201, "fail_f1": 0.7648, "accuracy_ci": [0.8353, 0.8756], "bootstrap_vs_no_trace": {"diff": 0.105, "ci": [0.0824, 0.1286], "significant": true}, "bootstrap_vs_vota": {"diff": -0.1378, "ci": [-0.1571, -0.1185], "significant": true}, "bootstrap_vs_full_trace": {"diff": 0.0387, "ci": [0.0185, 0.0597], "significant": true}, "train_loss": 0.0718, "wall_clock_seconds": 7425.65}`

### vota_no_ae_seed42
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-7B-Instruct
- **METRICS:** `{"accuracy": 0.994, "majority_baseline": 0.7151, "lift": 0.279, "n": 1190, "pass_f1": 0.996, "fail_f1": 0.989, "accuracy_ci_lower": 0.989, "accuracy_ci_upper": 0.998, "lift_vs_notrace": 0.243, "lift_vs_notrace_ci_lower": 0.218, "lift_vs_notrace_ci_upper": 0.268, "train_loss": 0.0908, "eval_loss": 0.2215, "wall_clock_seconds": 6397.88}`

### vota_seed123
- **STATUS:** DONE
- **CONCLUSION:** failed
- **MODEL_NAME:** Qwen2.5-Coder-7B-Instruct
- **METRICS:** (none)

### vota_seed42
- **STATUS:** DONE
- **CONCLUSION:** killed
- **MODEL_NAME:** N/A
- **METRICS:** (none)

### vota_seed42_v2
- **STATUS:** DONE
- **CONCLUSION:** killed
- **MODEL_NAME:** N/A
- **METRICS:** (none)

### vota_seed42_v3
- **STATUS:** DONE
- **CONCLUSION:** killed
- **MODEL_NAME:** Qwen2.5-Coder-7B-Instruct
- **METRICS:** `{"train_loss": 0.046, "eval_loss": 0.085, "eval_mean_token_accuracy": 0.983, "accuracy": 0.992, "majority_baseline": 0.7151, "lift": 0.276, "pass_precision": 0.99, "pass_recall": 0.99, "pass_f1": 0.99, "fail_precision": 0.99, "fail_recall": 0.99, "fail_f1": 0.99}`

### vota_seed42_v4
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** N/A
- **METRICS:** `{"accuracy": 0.9563, "majority_baseline": 0.7151, "lift": 0.2412, "n": 1190, "pass_precision": 0.944, "pass_recall": 0.998, "pass_f1": 0.97, "fail_precision": 0.993, "fail_recall": 0.853, "fail_f1": 0.917, "lift_vs_notrace": 0.205, "lift_vs_notrace_ci_lower": 0.177, "lift_vs_notrace_ci_upper": 0.234, "train_loss": 0.046, "eval_loss": 0.0842}`

### vota_seed42_v5
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-7B-Instruct
- **METRICS:** `{"accuracy": 0.9941, "pass_precision": 1, "pass_recall": 0.9918, "pass_f1": 0.9959, "fail_precision": 0.9798, "fail_recall": 1, "fail_f1": 0.9898, "n": 1190, "tp": 844, "fp": 0, "tn": 339, "fn": 7}`

### vota_seed456
- **STATUS:** DONE
- **CONCLUSION:** failed
- **MODEL_NAME:** N/A
- **METRICS:** (none)

### vota_seed456_v2
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-7B-Instruct
- **METRICS:** `{"accuracy": 0.9908, "pass_precision": 1, "pass_recall": 0.987, "pass_f1": 0.993, "fail_precision": 0.969, "fail_recall": 1, "fail_f1": 0.984, "ci_95": [0.985, 0.996]}`

### zeroshot_codellama13b_exception_only
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** CodeLlama-13B-Instruct
- **METRICS:** `{"accuracy": 0.5101, "accuracy_ci_lower": 0.4824, "accuracy_ci_upper": 0.5395, "pass_precision": 1, "pass_recall": 0.3502, "pass_f1": 0.5187, "fail_precision": 0.3585, "fail_recall": 0.9115, "fail_f1": 0.5146, "n_test": 1190, "n_unknown": 30}`

### zeroshot_deepseek7b_exception_only
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** DeepSeek-Coder-6.7B-Instruct
- **METRICS:** `{"accuracy": 0.9059, "accuracy_ci_lower": 0.8899, "accuracy_ci_upper": 0.9218, "pass_precision": 0.9743, "pass_recall": 0.8919, "pass_f1": 0.9313, "fail_precision": 0.7762, "fail_recall": 0.941, "fail_f1": 0.8507, "n_test": 1190, "n_unknown": 0}`

### zeroshot_qwen15b_exception_only
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-1.5B-Instruct
- **METRICS:** `{"accuracy": 0.9345, "accuracy_ci_lower": 0.9202, "accuracy_ci_upper": 0.9479, "pass_f1": 0.969, "fail_f1": 0.873, "pass_recall": 0.9906, "fail_recall": 0.7935, "n_test": 1190, "n_unknown": 24}`

### zeroshot_qwen7b_exception_only
- **STATUS:** DONE
- **CONCLUSION:** success
- **MODEL_NAME:** Qwen2.5-Coder-7B-Instruct
- **METRICS:** `{"accuracy": 0.8908, "accuracy_ci_lower": 0.8731, "accuracy_ci_upper": 0.9076, "pass_precision": 0.8815, "pass_recall": 0.9788, "pass_f1": 0.9276, "fail_precision": 0.9265, "fail_recall": 0.6696, "fail_f1": 0.7774, "n_test": 1190, "n_unknown": 0}`

---

**Summary of the extraction:**

- **134 experiments matched** out of 168 total
- The complete verbatim data for all 5 categories is above: qwen15b_* (32 experiments including qwen1.5b_* variants), vota_* (14 experiments), the 4 specifically named experiments (codellama13b_ae_only_seed42, codellama13b_loop_only_seed42, deepseek_ae_only_seed42, deepseek_loop_only_seed42), all full_trace/no_trace experiments (across all models), and all exception_only experiments (across all models including fewshot/zeroshot variants)
- The full output was persisted at `/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/f5f4efcf-b091-4929-abdf-35aa1152d6be/tool-results/b7t9ioqmo.txt` (2450 lines)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "055a4e4f-6a84-4ae5-8d9a-5aecf90eb6a6",
  "isSidechain": true,
  "agentId": "a86b080f191dc2217",
  "requestId": "req_011CbGEeW2bUXFt48hW6nJTF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b9e0586-128c-40b7-8979-8a468bc42860",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "f5f4efcf-b091-4929-abdf-35aa1152d6be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015TitX86XuEKypqwVAYXcbv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5904,
      "cache_read_input_tokens": 47765,
      "output_tokens": 21692,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5904
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 21692,
          "cache_read_input_tokens": 47765,
          "cache_creation_input_tokens": 5904,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5904,
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
