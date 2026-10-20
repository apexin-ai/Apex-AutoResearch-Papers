# Research conversation: I need to extract specific experiment metrics from a large registry JSON file for a paper data audit. The file is at: /h

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 55
- **Recorded user turns:** 1
- **Tool calls:** 23
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a00d6d05ce2acd01d.jsonl`
- **Structured JSON:** [`7da436c45642f5c728b3.json`](../../sessions/7d/7da436c45642f5c728b3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

55 recorded events

### User

_source line 1 · 2026-05-24T04:28:16.578Z_

I need to extract specific experiment metrics from a large registry JSON file for a paper data audit. The file is at:
/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2/tool-results/mcp-agent-ml-research-read_registry-1779596868416.txt

This is JSON with schema: {result: string}. The `result` field contains the actual registry content (likely JSON string).

I need you to:
1. First probe the structure with jq (type/length/keys)
2. Then extract ALL experiment entries. For each experiment, I need: experiment ID, status, model name, metrics (especially AUC values for different depth pairs like 0v1, 1v2, 2v3, 3v4, 4v5), K* values, and any MMLU/HellaSwag scores.

Specifically look for these experiments and their metrics:
- exp_001_pythia_depth (Pythia-1.4B AUC values)
- exp_002_olmo_depth (OLMo-1B AUC values)
- Any Qwen, Mistral, LLaMA experiments with AUC metrics
- Any filtering/downstream experiments with MMLU values
- exp_020 (Pythia decoding ablation)
- Any experiment with "contamination_rate" or "dose_response" in the name
- Any experiment with "bootstrap" or "kstar" in the name
- Any ANOVA results
- Any cross-transfer experiments (exp-013 or similar)
- Any runtime benchmark experiments

For each experiment found, report:
- Experiment ID
- Model/config description
- All numeric metrics (AUC values, MMLU, HellaSwag, etc.)
- Status and conclusion

Be thorough - extract ALL metrics from ALL experiments. This is for verifying paper numbers against ground truth data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "7d9f03b2-f13f-4ae8-b207-26c75cd900b2",
  "agentId": "a00d6d05ce2acd01d",
  "type": "user",
  "uuid": "ab3f6743-863f-4654-aa24-3d5c4f612424",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-24T04:28:16.583Z_

```json
{
  "parentUuid": "ab3f6743-863f-4654-aa24-3d5c4f612424",
  "isSidechain": true,
  "agentId": "a00d6d05ce2acd01d",
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
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only",
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
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__update_registry"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "894ff0d1-c402-45f9-aa62-1c4444f71207",
  "timestamp": "2026-05-24T04:28:16.583Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-24T04:28:24.537Z_



I'll start by reading the file to understand its structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "894ff0d1-c402-45f9-aa62-1c4444f71207",
  "isSidechain": true,
  "agentId": "a00d6d05ce2acd01d",
  "requestId": "req_011CbLmBeLHNECfzHLQ1h97o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8bd83940-9033-48e6-8f5a-30e5990a458b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SemjmLK81q8p1foXSDsYDf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15443,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15443,
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

_source line 4 · 2026-05-24T04:28:25.665Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DWv14BsRiYFYV9bpaRaF4t`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2/tool-results/mcp-agent-ml-research-read_registry-1779596868416.txt",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8bd83940-9033-48e6-8f5a-30e5990a458b",
  "isSidechain": true,
  "agentId": "a00d6d05ce2acd01d",
  "requestId": "req_011CbLmBeLHNECfzHLQ1h97o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd7c21f3-323d-40b6-99d1-0afcd6127330",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SemjmLK81q8p1foXSDsYDf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15443,
      "cache_read_input_tokens": 0,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15443
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 175,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15443,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15443,
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

_source line 5 · 2026-05-24T04:28:26.137Z_

<details><summary>↩ Tool result · reported error · `toolu_01DWv14BsRiYFYV9bpaRaF4t`</summary>

```text
File content (129319 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd7c21f3-323d-40b6-99d1-0afcd6127330",
  "isSidechain": true,
  "promptId": "7d9f03b2-f13f-4ae8-b207-26c75cd900b2",
  "agentId": "a00d6d05ce2acd01d",
  "type": "user",
  "uuid": "d5914793-8af8-4660-808f-cc348661ea14",
  "toolUseResult": "Error: File content (129319 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "cd7c21f3-323d-40b6-99d1-0afcd6127330",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-24T04:28:28.740Z_

The file is very large (129K tokens). Let me probe its structure and search for specific content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5914793-8af8-4660-808f-cc348661ea14",
  "isSidechain": true,
  "agentId": "a00d6d05ce2acd01d",
  "requestId": "req_011CbLmCMACLy1ASaYA6fVd6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a6c110db-5c23-4676-8ca5-77777388defb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JzmcYa51mQDt4KiuMWAV6d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1077,
      "cache_read_input_tokens": 15443,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1077,
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

_source line 7 · 2026-05-24T04:28:30.065Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NmLTYv4xQThLhJeewdHSde`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2/tool-results/mcp-agent-ml-research-read_registry-1779596868416.txt",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6c110db-5c23-4676-8ca5-77777388defb",
  "isSidechain": true,
  "agentId": "a00d6d05ce2acd01d",
  "requestId": "req_011CbLmCMACLy1ASaYA6fVd6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2aa1c0d5-ef65-48e5-884c-f38a35f2988d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JzmcYa51mQDt4KiuMWAV6d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1077,
      "cache_read_input_tokens": 15443,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1077
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 183,
          "cache_read_input_tokens": 15443,
          "cache_creation_input_tokens": 1077,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1077,
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

_source line 8 · 2026-05-24T04:28:30.756Z_

<details><summary>↩ Tool result · reported error · `toolu_01NmLTYv4xQThLhJeewdHSde`</summary>

```text
File content (129319 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2aa1c0d5-ef65-48e5-884c-f38a35f2988d",
  "isSidechain": true,
  "promptId": "7d9f03b2-f13f-4ae8-b207-26c75cd900b2",
  "agentId": "a00d6d05ce2acd01d",
  "type": "user",
  "uuid": "d06119e1-851c-4d8f-923a-4330bf781593",
  "toolUseResult": "Error: File content (129319 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "2aa1c0d5-ef65-48e5-884c-f38a35f2988d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-24T04:28:34.457Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01FLVQxkLAgZTVGjfmJeyPMv`</summary>

```json
{
  "command": "head -c 2000 \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2/tool-results/mcp-agent-ml-research-read_registry-1779596868416.txt\"",
  "description": "Read first 2000 bytes to understand file structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d06119e1-851c-4d8f-923a-4330bf781593",
  "isSidechain": true,
  "agentId": "a00d6d05ce2acd01d",
  "requestId": "req_011CbLmCgu6enUJqvepd8Qwc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e402662-bf43-44b9-8e4e-b89f54bf6fc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ursLLFYtLj28KTGnqppB5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 244,
      "cache_read_input_tokens": 16520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 244,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

_source line 10 · 2026-05-24T04:28:34.609Z_

<details><summary>↩ Tool result · `toolu_01FLVQxkLAgZTVGjfmJeyPMv`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"runtime_benchmark\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T13:11:11.536Z\", \"updated_at\": \"2026-05-23T13:11:11.536Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && python scripts/runtime_benchmark.py 2>&1 | tee results/runtime_benchmark/run.log\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"pid\": \"117556\", \"log_path\": \"~/runs/gen-depth-contamination/runtime_benchmark.log\", \"submitted_at\": \"2026-05-23T13:11:11.050Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"exp_015_neural_probe\": {\"status\": \"DONE\", \"retry_count\": 3, \"created_at\": \"2026-05-13T18:53:34.791Z\", \"updated_at\": \"2026-05-23T11:54:24.971Z\", \"hypothesis\": \"Learned representations (frozen LLM → MLP) 的 K* 是否高于 hand-crafted 15D features？若 K*_neural > K*_15D，说明 15D projection 是 K*=2 的部分原因；若相同，加强 information-theoretic impossibility 论证\", \"notes\": \"v4 completed successfully. 3 models: Pythia K*_neural=2, OLMo K*_neural=2, Qwen-cont K*_neural=3. Neural probe improves 2v3 AUC across all models (Pythia +0.044, OLMo +0.039, Qwen +0.055) but only Qwen-cont self-scorer crosses θ=0.60. EXIT_CODE=129 (SIGHUP after completion) did not affect results.\", \"completed_at\": \"2026-05-14T02:58:02.023Z\", \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 26.00 MiB. GPU 0 has a total capacity of 23.52 GiB of which 20.06 MiB is free. Process 55665 has 13.36 GiB memory in use. Process 56371 has 9.09 GiB memory in use. Including non-PyTorch memory, this process has 1\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"v4 run in progress (PID 108774, tmux: exp015, westc-26893). Root cause of prior failures: v2=OOM (concurrent e
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e402662-bf43-44b9-8e4e-b89f54bf6fc5",
  "isSidechain": true,
  "promptId": "7d9f03b2-f13f-4ae8-b207-26c75cd900b2",
  "agentId": "a00d6d05ce2acd01d",
  "type": "user",
  "uuid": "b80b0f0e-f438-4a78-a51a-4b56f2db4375",
  "sourceToolAssistantUUID": "1e402662-bf43-44b9-8e4e-b89f54bf6fc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-24T04:28:35.410Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01VZc99Be1n4vuoyzXoMEgff`</summary>

```json
{
  "command": "wc -c \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2/tool-results/mcp-agent-ml-research-read_registry-1779596868416.txt\"",
  "description": "Get file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b80b0f0e-f438-4a78-a51a-4b56f2db4375",
  "isSidechain": true,
  "agentId": "a00d6d05ce2acd01d",
  "requestId": "req_011CbLmCgu6enUJqvepd8Qwc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "372df0ae-dc47-4ed9-a1cf-aca6f985dab0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ursLLFYtLj28KTGnqppB5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 244,
      "cache_read_input_tokens": 16520,
      "output_tokens": 328,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 244
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 328,
          "cache_read_input_tokens": 16520,
          "cache_creation_input_tokens": 244,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 244,
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

_source line 12 · 2026-05-24T04:28:35.456Z_

<details><summary>↩ Tool result · `toolu_01VZc99Be1n4vuoyzXoMEgff`</summary>

```text
295939 /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2/tool-results/mcp-agent-ml-research-read_registry-1779596868416.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "372df0ae-dc47-4ed9-a1cf-aca6f985dab0",
  "isSidechain": true,
  "promptId": "7d9f03b2-f13f-4ae8-b207-26c75cd900b2",
  "agentId": "a00d6d05ce2acd01d",
  "type": "user",
  "uuid": "a510113f-b139-4742-9804-b88076fb0cd7",
  "sourceToolAssistantUUID": "372df0ae-dc47-4ed9-a1cf-aca6f985dab0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-24T04:28:39.389Z_

Good, the file is ~296KB. It's a JSON with `{result: string}` where the string contains the actual registry. Let me use jq to parse and extract the structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a510113f-b139-4742-9804-b88076fb0cd7",
  "isSidechain": true,
  "agentId": "a00d6d05ce2acd01d",
  "requestId": "req_011CbLmD33Z5ktxNgMs1pJXR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0233db1f-6dbb-4b0c-bbb0-0ce86c166051",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJhg7Q3bBZuGjt4f4dnavE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1268,
      "cache_read_input_tokens": 16764,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1268,
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

_source line 14 · 2026-05-24T04:28:43.225Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Ju5qENJn1iaY9u2GvGnQZm`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2/tool-results/mcp-agent-ml-research-read_registry-1779596868416.txt\"\n# Parse outer JSON, extract .result string, then parse inner JSON\ncat \"$FILE\" | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\ninner = json.loads(outer['result'])\n# Print top-level keys\nprint('Top-level keys:', list(inner.keys()))\nif 'data' in inner:\n    print('data keys:', list(inner['data'].keys()))\n    if 'experiments' in inner['data']:\n        exps = inner['data']['experiments']\n        print(f'Number of experiments: {len(exps)}')\n        print('Experiment IDs:', list(exps.keys()))\n\"",
  "description": "Parse JSON structure and list all experiment IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0233db1f-6dbb-4b0c-bbb0-0ce86c166051",
  "isSidechain": true,
  "agentId": "a00d6d05ce2acd01d",
  "requestId": "req_011CbLmD33Z5ktxNgMs1pJXR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e00d4b2a-1237-4ceb-a431-2513970694fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJhg7Q3bBZuGjt4f4dnavE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1268,
      "cache_read_input_tokens": 16764,
      "output_tokens": 369,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1268
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 369,
          "cache_read_input_tokens": 16764,
          "cache_creation_input_tokens": 1268,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1268,
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

_source line 15 · 2026-05-24T04:28:43.312Z_

<details><summary>↩ Tool result · `toolu_01Ju5qENJn1iaY9u2GvGnQZm`</summary>

```text
Top-level keys: ['success', 'data', 'error', 'metadata']
data keys: ['experiments', 'count', 'total', 'baseline']
Number of experiments: 165
Experiment IDs: ['runtime_benchmark', 'exp_015_neural_probe', 'exp_gemma2b_10k', 'seed_gemma27b_c4_s42', 'exp_olmo1b_10k', 'exp_002_olmo_depth', 'exp_001_pythia_depth', 'exp_llama8b_10k', 'exp_pythia14b_c4_10k', 'exp_qwen_cont_10k', 'exp_pythia14b_10k', 'exp_gemma27b_c4', 'seed_qwen15b_c4_s123', 'seed_qwen15b_wiki_s123', 'seed_pythia14b_wiki_s123', '7b-cross-transfer', 'arxiv_multi_source', 'sweep_r10_nofilter', 'sweep_r10_binary', 'sweep_r10_graduated', 'sweep_r30_nofilter', 'sweep_eval_r10_nofilter', 'sweep_eval_r10_binary', 'sweep_eval_r10_graduated', 'sweep_eval_r30_nofilter', 'sweep_eval_r10_nf', 'sweep_eval_r10_bin', 'sweep_eval_r10_grad', 'sweep_eval_r30_nf', 'sweep_eval_r10_nf_v2', 'sweep_r30_binary', 'sweep_r30_graduated', 'sweep_r50_nf', 'sweep_r50_binary', 'sweep_r50_graduated', 'sweep_r100_nf', 'sweep_r100_graduated', 'sweep_r100_binary', 'deberta_filtering_predict', 'deberta_filter_no_filter', 'deberta_filter_obd_binary', 'deberta_filter_deberta_binary', 'deberta_filter_deberta_graduated', 'seed2_no_filter', 'seed2_binary_ours', 'seed2_graduated', 'gsm8k_patch_nf_s0', 'gsm8k_patch_bo_s0', 'gsm8k_patch_grad_s0', 'gsm8k-serial-rerun', 'exp_008_retrain_chain', 'exp_olmo_retrain_v2', 'exp_pythia69b_c4_nuc', 'exp_pythia69b_c4_depth_chain_v3', 'exp_pythia14b_c4_rerun', 'exp_olmo1b_c4_rerun', 'exp_pythia69b_c4_depth_chain_v2', 'exp_pythia69b_c4_depth_chain', 'exp_expanded_downstream_eval', 'exp_deberta_filtering_comparison', 'exp_contamination_rate_sweep', 'exp_olmo_retrain_v3', 'exp_7b_scorer_arxiv', 'exp_014_naturalistic', 'exp_code_multi_source', 'exp_wiki_multi_source', 'exp_7b_scorer_ablation', 'exp_bootstrap_10k', 'exp-014', 'exp_gemma2b_depth', 'exp_deberta_code_qwen1b5', 'exp_multi_source_arxiv', 'exp_multi_source_detection', 'exp_changepoint_kstar', 'exp_cross_transfer_llama8b_to_qwen7b_v2', 'exp_deberta_arxiv_qwen1b5', 'exp_cross_transfer_llama8b_to_qwen7b', 'exp_cross_transfer_qwen7b_to_llama8b', 'exp_deberta_cross_transfer_gpu3', 'exp_deberta_cross_transfer_gpu2', 'exp_deberta_cross_transfer_gpu1', 'exp_deberta_cross_transfer_wiki', 'exp_deberta_c4_1b5_qwen_cont', 'exp_deberta_c4_1b5_pythia', 'exp_32b_c4_6class', 'exp_deberta_c4_1b5', 'exp_deberta_upperbound', 'exp_32b_c4', 'exp_deberta_c4', 'exp_code_qwen7b', 'exp_code_mistral7b', 'exp_code_llama8b', 'exp_code_qwen1b5_pythia_scorer', 'exp_pythia_retrain_depth7', 'exp_qwen_retrain_depth7', 'exp_code_pythia1b4', 'exp_028_power_curve', 'exp_qwen_retrain_chain', 'exp_code_qwen1b5', 'exp_olmo_retrain_chain', 'exp_028_subsampling_power', 'exp_026_arxiv_filtering', 'exp_027_latex_ablation', 'exp_025_pythia_filtering', 'exp_14b_c4', 'exp_arXiv_mistral7b_crossscorer', 'exp_arXiv_llama8b_crossscorer', 'exp_arXiv_qwen7b_crossscorer', 'exp_arXiv_qwen1b5_crossscorer', 'exp_wiki_scorer_confound_1b5', 'exp_wiki_scorer_confound', 'exp_wiki_qwen7b', 'exp_wiki_mistral7b', 'exp_wiki_llama8b', 'exp_arXiv_qwen7b', 'exp_arXiv_mistral7b', 'exp_arXiv_llama8b', 'exp_wiki_pythia_v2', 'exp_wiki_olmo_v2', 'exp_arXiv_olmo', 'exp_wiki_olmo', 'exp_wiki_pythia', 'exp_009_dose_response', 'exp_009_dose_50pct_v3', 'exp_009_dose_30pct_v3', 'exp_009_dose_10pct_v3', 'exp_027_retrain_bootstrap', 'exp_026_feature_stability_v2', 'exp_026_feature_stability', 'exp_027', 'exp_005_degradation', 'exp_024_arxiv_domain', 'exp_017_qwen_continuation', 'exp_012_binary_confidence', 'exp_C_permutation_10k', 'exp_009_dose_50pct_v2', 'exp_009_dose_30pct_v2', 'exp_009_dose_10pct_v2', 'exp_009_dose_50pct', 'exp_009_dose_30pct', 'exp_009_dose_10pct', 'exp_kstar_theta', 'exp_022_cross_scorer_matrix', 'exp_008_retrain_chain_v2', 'exp-008-retrain-chain', 'exp_025_pythia_arxiv', 'exp_020_pythia_decoding', 'exp_021_length_ablation', 'exp_018_llama8b_depth', 'exp_023_domain_ablation', 'exp_019b_mistral_cross_scorer', 'exp_019_mistral7b_depth', 'exp_016_base_vs_instruct', 'exp_003_decoding_ablation', 'exp_004_7b_crossscale', 'exp_E_paired_stats', 'exp_D_obd_n500', 'exp_B_14d_ablation', 'exp_A_alt_scorer', 'exp_006_graduated_filtering', 'exp_007_bootstrap_ci', 'exp_011_llm_zeroshot', 'exp_013_cross_transfer', 'exp_010_ordinal_baseline', 'mvp_pilot_sat_v1']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e00d4b2a-1237-4ceb-a431-2513970694fb",
  "isSidechain": true,
  "promptId": "7d9f03b2-f13f-4ae8-b207-26c75cd900b2",
  "agentId": "a00d6d05ce2acd01d",
  "type": "user",
  "uuid": "e0d3b95d-8f72-4ba8-9760-8d3c09e8296c",
  "sourceToolAssistantUUID": "e00d4b2a-1237-4ceb-a431-2513970694fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-24T04:28:46.476Z_

165 experiments. Now let me extract the detailed metrics for each of the requested experiments systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0d3b95d-8f72-4ba8-9760-8d3c09e8296c",
  "isSidechain": true,
  "agentId": "a00d6d05ce2acd01d",
  "requestId": "req_011CbLmDcautyekXoALqAG45",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f6b5e4dd-f0f7-47de-a8b8-9c0a696bfd90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015RmWpBnjeAoVj2rzbBx87K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2430,
      "cache_read_input_tokens": 18032,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2430,
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

_source line 17 · 2026-05-24T04:28:52.717Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01G6DZbz71uY6jXYvkLu7hPx`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2/tool-results/mcp-agent-ml-research-read_registry-1779596868416.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\ninner = json.loads(outer['result'])\nexp = inner['data']['experiments']['exp_001_pythia_depth']\nprint(json.dumps(exp, indent=2))\n\" 2>&1 | head -200",
  "description": "Extract exp_001_pythia_depth details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6b5e4dd-f0f7-47de-a8b8-9c0a696bfd90",
  "isSidechain": true,
  "agentId": "a00d6d05ce2acd01d",
  "requestId": "req_011CbLmDcautyekXoALqAG45",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0deede48-f6a7-47d4-bb6c-7a784f2376b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015RmWpBnjeAoVj2rzbBx87K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2430,
      "cache_read_input_tokens": 18032,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2430,
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

_source line 18 · 2026-05-24T04:28:52.820Z_

<details><summary>↩ Tool result · `toolu_01G6DZbz71uY6jXYvkLu7hPx`</summary>

```text
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-12T20:06:23.803Z",
  "updated_at": "2026-05-22T22:04:05.591Z",
  "hypothesis": "K* \u8de8\u6a21\u578b\u4e00\u81f4\u6027\u9a8c\u8bc1\uff1aPythia-1.4B \u5728\u76f8\u540c\u79cd\u5b50\u6570\u636e\u548c\u89e3\u7801\u7b56\u7565\u4e0b\u7684 K* \u662f\u5426\u4e0e Qwen2.5-1.5B \u4e00\u81f4\uff08K*=2\uff09",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo 2>/dev/null && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://hf-mirror.com && cd /root/autodl-tmp/gen-depth-contamination && python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/EleutherAI/pythia-1.4b --data_dir /root/autodl-tmp/gen-depth-contamination/data_exp001_pythia --results_dir /root/autodl-tmp/gen-depth-contamination/results_exp001_pythia --num_samples 5000 --max_depth 5 --batch_size 16 --generation_mode continuation\"",
    "server": "autodl-4090d",
    "gpu": [
      "cuda:0"
    ],
    "pid": "17138",
    "log_path": "~/runs/gen-depth-contamination/exp_001_pythia_depth.log",
    "submitted_at": "2026-05-12T20:50:31.471Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "/root/autodl-tmp/gen-depth-contamination/data_exp001_pythia",
    "data_count": 5000,
    "model_name": "EleutherAI/pythia-1.4b",
    "seed": 42,
    "checkpoint_path": "/root/autodl-tmp/gen-depth-contamination/data_exp001_pythia/",
    "wall_clock_seconds": 12344.9,
    "gpu_hours": 3.43
  },
  "conclusion": "success",
  "metrics": {
    "k_star": 2,
    "pairwise_auc": {
      "0v1": 0.9722,
      "1v2": 0.6074,
      "2v3": 0.544,
      "3v4": 0.5051,
      "4v5": 0.5079
    },
    "pairwise_auc_std": {
      "0v1": 0.0039,
      "1v2": 0.0078,
      "2v3": 0.0067,
      "3v4": 0.0032,
      "4v5": 0.0101
    },
    "bootstrap_ci": {
      "1v2": {
        "auc_oof": 0.6072,
        "boot_mean": 0.6073,
        "boot_std": 0.005,
        "ci_95": [
          0.5975,
          0.6172
        ],
        "ci_995_bonferroni": [
          0.5934,
          0.621
        ],
        "perm_p": 0.0001,
        "bonferroni_pass": false
      }
    },
    "scorer": "Qwen2.5-1.5B-Instruct",
    "note": "Updated to Qwen cross-scoring (D107). Self-scored 1v2=0.6539, Qwen-scored 1v2=0.6074."
  },
  "completed_at": "2026-05-13T00:16:16.359Z"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0deede48-f6a7-47d4-bb6c-7a784f2376b3",
  "isSidechain": true,
  "promptId": "7d9f03b2-f13f-4ae8-b207-26c75cd900b2",
  "agentId": "a00d6d05ce2acd01d",
  "type": "user",
  "uuid": "23836a89-41ea-40e9-bbcc-94599e2a601b",
  "sourceToolAssistantUUID": "0deede48-f6a7-47d4-bb6c-7a784f2376b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-24T04:28:54.465Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01LXsDRMj52Ty6P7TjwZmAPS`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2/tool-results/mcp-agent-ml-research-read_registry-1779596868416.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\ninner = json.loads(outer['result'])\nexp = inner['data']['experiments']['exp_002_olmo_depth']\nprint(json.dumps(exp, indent=2))\n\" 2>&1 | head -200",
  "description": "Extract exp_002_olmo_depth details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23836a89-41ea-40e9-bbcc-94599e2a601b",
  "isSidechain": true,
  "agentId": "a00d6d05ce2acd01d",
  "requestId": "req_011CbLmDcautyekXoALqAG45",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a8d3c2a8-63ff-4c54-99ad-19f8073d19ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015RmWpBnjeAoVj2rzbBx87K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2430,
      "cache_read_input_tokens": 18032,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2430,
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

_source line 20 · 2026-05-24T04:28:54.582Z_

<details><summary>↩ Tool result · `toolu_01LXsDRMj52Ty6P7TjwZmAPS`</summary>

```text
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-12T20:06:24.766Z",
  "updated_at": "2026-05-22T22:04:07.552Z",
  "hypothesis": "K* \u8de8\u6a21\u578b\u4e00\u81f4\u6027\u9a8c\u8bc1\uff1aOLMo-1B \u5728\u76f8\u540c\u79cd\u5b50\u6570\u636e\u548c\u89e3\u7801\u7b56\u7565\u4e0b\u7684 K* \u662f\u5426\u4e0e Qwen2.5-1.5B \u4e00\u81f4\uff08K*=2\uff09",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo 2>/dev/null && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://hf-mirror.com && cd /root/autodl-tmp/gen-depth-contamination && python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/allenai/OLMo-1B-hf --data_dir /root/autodl-tmp/gen-depth-contamination/data_exp002_olmo --results_dir /root/autodl-tmp/gen-depth-contamination/results_exp002_olmo --num_samples 5000 --max_depth 5 --batch_size 16 --generation_mode continuation\"",
    "server": "autodl-4090d",
    "gpu": [
      "cuda:0"
    ],
    "pid": "20225",
    "log_path": "~/runs/gen-depth-contamination/exp_002_olmo_depth.log",
    "submitted_at": "2026-05-13T00:16:07.960Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "/root/autodl-tmp/gen-depth-contamination/data_exp002_olmo",
    "data_count": 5000,
    "model_name": "allenai/OLMo-1B-hf",
    "seed": 42,
    "checkpoint_path": "/root/autodl-tmp/gen-depth-contamination/data_exp002_olmo/",
    "wall_clock_seconds": 8384.9,
    "gpu_hours": 2.33
  },
  "reproduce": {
    "finished_at": "2026-05-13T02:31:18.880Z"
  },
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-13T02:31:19.738113+00:00"
      }
    ]
  },
  "metrics": {
    "k_star": 1,
    "pairwise_auc": {
      "0v1": 0.9861,
      "1v2": 0.5001,
      "2v3": 0.4972,
      "3v4": 0.5034,
      "4v5": 0.4971
    },
    "scorer": "Qwen2.5-1.5B-Instruct",
    "note": "Updated to Qwen cross-scoring (D107). Self-scored 1v2=0.6145 K*=2, Qwen-scored 1v2=0.5001 K*=1."
  },
  "conclusion": "success",
  "completed_at": "2026-05-13T02:35:52.823Z",
  "parent": "exp_001_pythia_depth"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8d3c2a8-63ff-4c54-99ad-19f8073d19ee",
  "isSidechain": true,
  "promptId": "7d9f03b2-f13f-4ae8-b207-26c75cd900b2",
  "agentId": "a00d6d05ce2acd01d",
  "type": "user",
  "uuid": "9b6334b2-2f38-41d8-9a2d-99fbfb6b8f7f",
  "sourceToolAssistantUUID": "a8d3c2a8-63ff-4c54-99ad-19f8073d19ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-24T04:28:56.063Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01GDVAGAaPXzLw4po9xCoAMZ`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2/tool-results/mcp-agent-ml-research-read_registry-1779596868416.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\ninner = json.loads(outer['result'])\nexp = inner['data']['experiments']['exp_020_pythia_decoding']\nprint(json.dumps(exp, indent=2))\n\" 2>&1 | head -200",
  "description": "Extract exp_020_pythia_decoding details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b6334b2-2f38-41d8-9a2d-99fbfb6b8f7f",
  "isSidechain": true,
  "agentId": "a00d6d05ce2acd01d",
  "requestId": "req_011CbLmDcautyekXoALqAG45",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "38376b4c-2e35-4941-8070-3ad18da55138",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015RmWpBnjeAoVj2rzbBx87K",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2430,
      "cache_read_input_tokens": 18032,
      "output_tokens": 745,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2430
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 745,
          "cache_read_input_tokens": 18032,
          "cache_creation_input_tokens": 2430,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2430,
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

_source line 22 · 2026-05-24T04:28:56.154Z_

<details><summary>↩ Tool result · `toolu_01GDVAGAaPXzLw4po9xCoAMZ`</summary>

```text
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-16T04:52:13.036Z",
  "updated_at": "2026-05-16T17:18:28.366Z",
  "hypothesis": "Pythia-1.4B \u89e3\u7801\u6d88\u878d\uff1a4 \u4e2a decoding config (greedy/nuc p=0.9/T=0.7/T=1.2) \u7684 K* \u662f\u5426\u4e00\u81f4\uff1f\u4e0e exp-003 (Qwen) \u5e73\u884c\uff0c\u9a8c\u8bc1 decoding \u6548\u5e94\u8de8\u6a21\u578b\u4e00\u81f4\u6027\u3002C4 5K, depth 0-5\u3002",
  "parent": "exp_003_decoding_ablation",
  "server": "cqa1-22115",
  "gpu": "cuda:2",
  "account": "root",
  "reproduce": {
    "server": "cqa1-22115",
    "gpu": "cuda:2",
    "started_at": "2026-05-16T04:57:46.476Z"
  },
  "spec": {
    "command": "nohup bash -c 'CUDA_VISIBLE_DEVICES=2 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache bash scripts/exp020_pythia_decoding.sh' > /tmp/exp020_pythia_decoding.log 2>&1 &",
    "server": "cqa1-22115",
    "data_path": "data_exp020_pythia_{greedy,nuc09,t07,t12}/",
    "data_count": 20000,
    "model_name": "EleutherAI/pythia-1.4b (fp16)",
    "seed": 42,
    "generation_mode": "continuation (4 decoding configs: greedy/nuc09/t07/t12)",
    "pid": 14551,
    "log_path": "/tmp/exp020_pythia_decoding.log",
    "note": "Worker \u8bef\u7528 nohup \u800c\u975e submit_training_job\uff0c\u5df2\u8865\u6ce8\u518c cron \u76d1\u63a7 (PID 14551)\u3002\u539f PID 13076 \u5df2\u88ab kill\u3002"
  },
  "notes": "greedy 1v2 AUC=0.8838 \u8c03\u67e5\u5b8c\u6210\uff1a\u6839\u56e0\u4e3a Pythia-1.4B greedy \u7ea7\u8054\u91cd\u590d\u574d\u584c\uff084-gram repeat rate: d0=0.01\u2192d1=0.72\u2192d2=0.81; TTR: d0=0.72\u2192d1=0.19\u2192d2=0.14\uff09\u3002hapax_ratio (d=1.06) \u548c low_freq_ratio (d=1.03) \u662f top \u8d21\u732e\u7279\u5f81\u3002\u975e bug\uff0c\u53c2\u6570\u6b63\u786e\uff0c\u65e0\u6570\u636e\u6cc4\u6f0f\u3002K*=2 \u4e0d\u53d7\u5f71\u54cd\u3002\u5efa\u8bae\u8bba\u6587\u6807\u6ce8\u4e3a repetition-dominated regime\u3002| Bootstrap CI (10000 iter): t07 2v3 AUC=0.5939 CI [0.5855, 0.6025] BORDERLINE (CI upper crosses \u03b8); t12 1v2 AUC=0.6170 CI [0.6071, 0.6270] PASS\u3002",
  "conclusion": "success",
  "metrics": {
    "greedy": {
      "K_star": 2,
      "auc": {
        "0v1": 0.9992,
        "1v2": 0.8838,
        "2v3": 0.5342,
        "3v4": 0.5228,
        "4v5": 0.5162
      }
    },
    "nuc09": {
      "K_star": 2,
      "auc": {
        "0v1": 0.9948,
        "1v2": 0.677,
        "2v3": 0.5549,
        "3v4": 0.5299,
        "4v5": 0.5013
      }
    },
    "t07": {
      "K_star": 2,
      "auc": {
        "0v1": 0.9965,
        "1v2": 0.7265,
        "2v3": 0.5941,
        "3v4": 0.5698,
        "4v5": 0.5284
      }
    },
    "t12": {
      "K_star": 2,
      "auc": {
        "0v1": 0.9933,
        "1v2": 0.6172,
        "2v3": 0.5226,
        "3v4": 0.517,
        "4v5": 0.5051
      }
    }
  },
  "checkpoint_path": "/root/autodl-tmp/gen-depth-contamination/results_exp020_pythia_{greedy,nuc09,t07,t12}/",
  "log_path": "/tmp/exp020_pythia_decoding.log",
  "completed_at": "2026-05-16T14:41:33.153Z"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38376b4c-2e35-4941-8070-3ad18da55138",
  "isSidechain": true,
  "promptId": "7d9f03b2-f13f-4ae8-b207-26c75cd900b2",
  "agentId": "a00d6d05ce2acd01d",
  "type": "user",
  "uuid": "b37ac2a5-538b-4f0e-9876-b5e3a2b957e6",
  "sourceToolAssistantUUID": "38376b4c-2e35-4941-8070-3ad18da55138",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-24T04:28:58.597Z_

Now let me extract the remaining key experiments in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b37ac2a5-538b-4f0e-9876-b5e3a2b957e6",
  "isSidechain": true,
  "agentId": "a00d6d05ce2acd01d",
  "requestId": "req_011CbLmEZXPiBHnN4k9EzF5X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "135ad221-533a-4622-befa-af9be139fbc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SFQf1U5hYWXcPQexUa8h8A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4771,
      "cache_read_input_tokens": 20462,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4771,
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

_source line 24 · 2026-05-24T04:29:07.659Z_

<details open><summary>🔧 Tool call — Bash · `toolu_019RC7gZZPGenHCLmTPGpiYN`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2/tool-results/mcp-agent-ml-research-read_registry-1779596868416.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Qwen-related experiments\nqwen_keys = [k for k in exps if 'qwen' in k.lower()]\nprint('=== QWEN EXPERIMENTS ===')\nfor k in qwen_keys:\n    e = exps[k]\n    print(f'\\n--- {k} ---')\n    print(f'  Status: {e.get(\\\"status\\\")}')\n    print(f'  Conclusion: {e.get(\\\"conclusion\\\", \\\"N/A\\\")}')\n    if 'spec' in e:\n        print(f'  Model: {e[\\\"spec\\\"].get(\\\"model_name\\\", \\\"N/A\\\")}')\n    if 'metrics' in e:\n        print(f'  Metrics: {json.dumps(e[\\\"metrics\\\"], indent=4)}')\n    if 'notes' in e:\n        print(f'  Notes: {str(e[\\\"notes\\\"])[:300]}')\n\" 2>&1 | head -500",
  "description": "Extract all Qwen experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "135ad221-533a-4622-befa-af9be139fbc1",
  "isSidechain": true,
  "agentId": "a00d6d05ce2acd01d",
  "requestId": "req_011CbLmEZXPiBHnN4k9EzF5X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ea42629-d521-40ac-8574-e0c6cad3b717",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SFQf1U5hYWXcPQexUa8h8A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4771,
      "cache_read_input_tokens": 20462,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4771,
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

_source line 25 · 2026-05-24T04:29:07.746Z_

<details><summary>↩ Tool result · `toolu_019RC7gZZPGenHCLmTPGpiYN`</summary>

```text
=== QWEN EXPERIMENTS ===

--- exp_qwen_cont_10k ---
  Status: DONE
  Conclusion: success
  Model: Qwen/Qwen2.5-1.5B (base, continuation) + Qwen/Qwen2.5-1.5B-Instruct (scorer)
  Metrics: {
    "K_star": 2,
    "AUC_0v1": 0.9875,
    "AUC_1v2": 0.6346,
    "AUC_2v3": 0.5616,
    "AUC_3v4": 0.5451,
    "AUC_4v5": 0.5254,
    "bootstrap_1v2_95CI": [
        0.6282,
        0.6409
    ],
    "bootstrap_1v2_995CI_bonferroni": [
        0.6255,
        0.6436
    ],
    "perm_pvalue_1v2": 0.0001,
    "bonferroni_pass": true,
    "top_feature": "freq_entropy"
}

--- seed_qwen15b_c4_s123 ---
  Status: DONE
  Conclusion: success
  Model: Qwen2.5-1.5B-Instruct

--- seed_qwen15b_wiki_s123 ---
  Status: DONE
  Conclusion: negative
  Model: Qwen2.5-1.5B-Instruct

--- exp_deberta_code_qwen1b5 ---
  Status: DONE
  Conclusion: success
  Model: N/A
  Metrics: {
    "K_star": 2,
    "theta": 0.6,
    "auc_0v1": 1,
    "auc_1v2": 0.8076,
    "auc_2v3": 0.5933,
    "auc_3v4": 0.5492,
    "auc_4v5": 0.5311,
    "ci_0v1": [
        0.9999,
        1
    ],
    "ci_1v2": [
        0.8001,
        0.8147
    ],
    "ci_2v3": [
        0.5847,
        0.6018
    ],
    "ci_3v4": [
        0.541,
        0.5573
    ],
    "ci_4v5": [
        0.5235,
        0.5388
    ],
    "obd_auc_0v1": 0.9388,
    "obd_auc_1v2": 0.7382,
    "obd_auc_2v3": 0.53,
    "obd_auc_3v4": 0.5022,
    "obd_auc_4v5": 0.5219,
    "elapsed_seconds": 5780
}

--- exp_cross_transfer_llama8b_to_qwen7b_v2 ---
  Status: DONE
  Conclusion: success
  Model: DeBERTa-v3-base
  Metrics: {
    "K_star": 3,
    "2v3_auc_ci_lower": 0.6124,
    "theta": 0.6,
    "margin_pp": 1.24
}

--- exp_deberta_arxiv_qwen1b5 ---
  Status: DONE
  Conclusion: success
  Model: DeBERTa-v3-base
  Metrics: {
    "K_star": 4,
    "0v1_auc": 0.9997,
    "1v2_auc": 0.9214,
    "2v3_auc": 0.7446,
    "3v4_auc": 0.6238,
    "4v5_auc": 0.5771,
    "3v4_ci_lower": 0.6127,
    "3v4_ci_upper": 0.6349,
    "theta": 0.6
}

--- exp_cross_transfer_llama8b_to_qwen7b ---
  Status: DONE
  Conclusion: failed
  Model: DeBERTa-v3-base

--- exp_cross_transfer_qwen7b_to_llama8b ---
  Status: DONE
  Conclusion: success
  Model: DeBERTa-v3-base
  Metrics: {
    "kstar": 3,
    "kstar_indexing": "1-indexed",
    "pairwise_auc": {
        "0v1": 0.9998,
        "1v2": 0.7384,
        "2v3": 0.6278,
        "3v4": 0.587,
        "4v5": 0.5519
    },
    "elapsed_s": 3621
}

--- exp_deberta_c4_1b5_qwen_cont ---
  Status: DONE
  Conclusion: success
  Model: DeBERTa-v3-base
  Metrics: {
    "config": "qwen_cont256",
    "kstar": 2,
    "kstar_theta": 0.6,
    "pairwise_auc": {
        "0v1": 0.9955,
        "1v2": 0.7194,
        "2v3": 0.5954,
        "3v4": 0.5689,
        "4v5": 0.5502
    },
    "ci_95": {
        "0v1": [
            0.9944,
            0.9965
        ],
        "1v2": [
            0.712,
            0.7273
        ],
        "2v3": [
            0.587,
            0.6028
        ],
        "3v4": [
            0.5613,
            0.5766
        ],
        "4v5": [
            0.5431,
            0.5577
        ]
    },
    "obd_baseline": {
        "0v1": 0.9914,
        "1v2": 0.6282,
        "2v3": 0.5556,
        "3v4": 0.5298,
        "4v5": 0.5137
    },
    "delta_vs_obd": {
        "1v2": 0.0912
    },
    "key_finding": "C4 1.5B qwen_cont256 K*=2, boundary holds across continuation generation strategy."
}

--- exp_code_qwen7b ---
  Status: DONE
  Conclusion: success
  Model: Qwen2.5-7B
  Metrics: {
    "pairwise_auc": {
        "0v1": {
            "mean": 0.9051,
            "ci95_half": 0.0043,
            "folds": [
                0.9073,
                0.9012,
                0.912,
                0.9049,
                0.9003
            ]
        },
        "1v2": {
            "mean": 0.7276,
            "ci95_half": 0.0055,
            "folds": [
                0.7377,
                0.7254,
                0.724,
                0.722,
                0.7289
            ]
        },
        "2v3": {
            "mean": 0.5368,
            "ci95_half": 0.0145,
            "folds": [
                0.5179,
                0.5332,
                0.5275,
                0.5462,
                0.5593
            ]
        },
        "3v4": {
            "mean": 0.509,
            "ci95_half": 0.0055,
            "folds": [
                0.5029,
                0.5054,
                0.5085,
                0.5092,
                0.5191
            ]
        },
        "4v5": {
            "mean": 0.5139,
            "ci95_half": 0.0128,
            "folds": [
                0.5016,
                0.5317,
                0.5264,
                0.509,
                0.5007
            ]
        }
    },
    "pairwise_jsd": {
        "0v1": 0.061265,
        "1v2": 0.042256,
        "2v3": 0.00413,
        "3v4": 0.003198,
        "4v5": 0.003393
    },
    "k_star": 2,
    "ordinal": {
        "mae": 1.2651,
        "accuracy": 0.3423
    },
    "top_features": [
        {
            "name": "freq_entropy",
            "importance": 9730
        },
        {
            "name": "surp_d2_mean",
            "importance": 9236.2
        },
        {
            "name": "surp_d1_mean",
            "importance": 9126.2
        },
        {
            "name": "surp_d1_skew",
            "importance": 8833.4
        },
        {
            "name": "surp_std",
            "importance": 8110.2
        },
        {
            "name": "freq_kurtosis",
            "importance": 7838.6
        },
        {
            "name": "surp_mean",
            "importance": 7586
        },
        {
            "name": "surp_kurt",
            "importance": 6769.2
        },
        {
            "name": "hapax_ratio",
            "importance": 6636.4
        },
        {
            "name": "ttr",
            "importance": 6332.6
        }
    ]
}
  Notes: Attempts 1-3 failed: huggingface.co unreachable (000), httpx client closed during datasets.load_dataset. Attempt 4 success: copied depth_0.jsonl from exp_code_qwen1b5 (MD5 match), set HF_ENDPOINT=https://hf-mirror.com. PID 114228, GPU util 96%, 15211/24564 MiB. nvidia-smi verified.

--- exp_code_qwen1b5_pythia_scorer ---
  Status: DONE
  Conclusion: success
  Model: N/A
  Metrics: {
    "k_star": 2,
    "theta": 0.6,
    "auc_0v1": 0.9076,
    "auc_1v2": 0.7197,
    "auc_2v3": 0.5308,
    "auc_3v4": 0.5236,
    "auc_4v5": 0.5084,
    "jsd_0v1": 0.065423,
    "jsd_1v2": 0.035809,
    "jsd_2v3": 0.004315,
    "jsd_3v4": 0.003182,
    "jsd_4v5": 0.003047,
    "ordinal_mae": 1.2578,
    "ordinal_accuracy": 0.3433,
    "scorer": "pythia-1.4b"
}
  Notes: Code domain K*=2 confirmed scorer-independent. Pythia-1.4B scorer reproduces K*=2 on Qwen-1.5B Code text (same as Qwen self-scorer). AUC deltas vs original: 0v1 Δ=-0.031, 1v2 Δ=-0.019 (minor drop, Pythia slightly weaker feature extractor), 2v3 Δ=+0.001 (identical). Boundary transition 1v2→2v3 robust

--- exp_qwen_retrain_depth7 ---
  Status: DONE
  Conclusion: success
  Model: Qwen2.5-1.5B
  Metrics: {
    "k_star": 7,
    "theta": 0.6,
    "max_depth": 7,
    "analysis_method": "5-fold GroupKFold CV",
    "pairwise_auc": {
        "0v1": {
            "mean": 0.9837,
            "std": 0.0019,
            "ci_95": [
                0.9821,
                0.9854
            ],
            "folds": [
                0.9832,
                0.9821,
                0.9837,
                0.9823,
                0.9873
            ]
        },
        "1v2": {
            "mean": 0.8971,
            "std": 0.0025,
            "ci_95": [
                0.8949,
                0.8993
            ],
            "folds": [
                0.8923,
                0.8988,
                0.8986,
                0.8991,
                0.8967
            ]
        },
        "2v3": {
            "mean": 0.8098,
            "std": 0.0052,
            "ci_95": [
                0.8052,
                0.8144
            ],
            "folds": [
                0.8086,
                0.8074,
                0.818,
                0.8024,
                0.8128
            ]
        },
        "3v4": {
            "mean": 0.76,
            "std": 0.0082,
            "ci_95": [
                0.7528,
                0.7672
            ],
            "folds": [
                0.7534,
                0.7617,
                0.7753,
                0.7566,
                0.7531
            ]
        },
        "4v5": {
            "mean": 0.7459,
            "std": 0.0091,
            "ci_95": [
                0.7379,
                0.7538
            ],
            "folds": [
                0.7429,
                0.7562,
                0.7521,
                0.73,
                0.7482
            ]
        },
        "5v6": {
            "mean": 0.7017,
            "std": 0.0068,
            "ci_95": [
                0.6958,
                0.7076
            ],
            "folds": [
                0.7006,
                0.7077,
                0.7104,
                0.6915,
                0.6984
            ]
        },
        "6v7": {
            "mean": 0.641,
            "std": 0.0039,
            "ci_95": [
                0.6376,
                0.6445
            ],
            "folds": [
                0.6419,
                0.6349,
                0.6464,
                0.639,
                0.643
            ]
        }
    },
    "jsd": {
        "0v1": 0.23005,
        "1v2": 0.103924,
        "2v3": 0.075049,
        "3v4": 0.065398,
        "4v5": 0.060509,
        "5v6": 0.034998,
        "6v7": 0.017652
    }
}
  Notes: Qwen2.5-1.5B retrain-chain K*=7 (all 7 depth pairs AUC > θ=0.60). 6v7 AUC=0.641 (CI [0.638, 0.645]) is the tightest pair but still clears threshold. Depth 0-4 results consistent with exp_qwen_retrain_chain (AUC diff < 0.003). JSD decays from 0.230 (0v1) to 0.018 (6v7), suggesting convergence. AUC de

--- exp_qwen_retrain_chain ---
  Status: DONE
  Conclusion: success
  Model: N/A
  Metrics: {
    "K_star_lower_bound": 4,
    "theta": 0.6,
    "auc_0v1": 0.9838,
    "auc_1v2": 0.8969,
    "auc_2v3": 0.81,
    "auc_3v4": 0.7624,
    "ci_0v1": [
        0.982,
        0.9855
    ],
    "ci_1v2": [
        0.8937,
        0.9001
    ],
    "ci_2v3": [
        0.8052,
        0.8147
    ],
    "ci_3v4": [
        0.7543,
        0.7706
    ],
    "ci_method": "5-fold CV",
    "jsd_0v1": 0.2263,
    "jsd_1v2": 0.1046,
    "jsd_2v3": 0.0752,
    "jsd_3v4": 0.0654
}
  Notes: Qwen2.5-1.5B retrain-chain K*≥4 (all 4 pairs AUC >> θ=0.60). Bootstrap CI discarded due to data leakage (resampling broke GroupKFold structure, inflated AUC by +6.4pp). Using fold-based CI instead. Retrain-chain K*≥4 >> prompt-chain K*=2, contradicts conservative-upper-bound hypothesis but confirms 

--- exp_code_qwen1b5 ---
  Status: DONE
  Conclusion: success
  Model: N/A
  Metrics: {
    "K_star": 2,
    "theta": 0.6,
    "auc_0v1": 0.9388,
    "auc_1v2": 0.7382,
    "auc_2v3": 0.53,
    "auc_3v4": 0.5022,
    "auc_4v5": 0.5219,
    "ci_0v1": [
        0.929,
        0.949
    ],
    "ci_1v2": [
        0.709,
        0.767
    ],
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ea42629-d521-40ac-8574-e0c6cad3b717",
  "isSidechain": true,
  "promptId": "7d9f03b2-f13f-4ae8-b207-26c75cd900b2",
  "agentId": "a00d6d05ce2acd01d",
  "type": "user",
  "uuid": "49d0e685-6657-4610-a2a3-e5bc85979481",
  "sourceToolAssistantUUID": "8ea42629-d521-40ac-8574-e0c6cad3b717",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-24T04:29:11.175Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01GAPix3BWu9voev5bi8bpAz`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2/tool-results/mcp-agent-ml-research-read_registry-1779596868416.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Mistral and LLaMA experiments\nkeys = [k for k in exps if 'mistral' in k.lower() or 'llama' in k.lower()]\nprint('=== MISTRAL/LLAMA EXPERIMENTS ===')\nfor k in keys:\n    e = exps[k]\n    print(f'\\n--- {k} ---')\n    print(f'  Status: {e.get(\\\"status\\\")}')\n    print(f'  Conclusion: {e.get(\\\"conclusion\\\", \\\"N/A\\\")}')\n    if 'spec' in e:\n        print(f'  Model: {e[\\\"spec\\\"].get(\\\"model_name\\\", \\\"N/A\\\")}')\n    if 'metrics' in e:\n        print(f'  Metrics: {json.dumps(e[\\\"metrics\\\"], indent=4)}')\n    if 'notes' in e:\n        print(f'  Notes: {str(e[\\\"notes\\\"])[:300]}')\n\" 2>&1 | head -500",
  "description": "Extract Mistral and LLaMA experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49d0e685-6657-4610-a2a3-e5bc85979481",
  "isSidechain": true,
  "agentId": "a00d6d05ce2acd01d",
  "requestId": "req_011CbLmEZXPiBHnN4k9EzF5X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a33535dd-b874-4484-9c9d-f01b8c856882",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SFQf1U5hYWXcPQexUa8h8A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4771,
      "cache_read_input_tokens": 20462,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4771,
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

_source line 27 · 2026-05-24T04:29:11.263Z_

<details><summary>↩ Tool result · `toolu_01GAPix3BWu9voev5bi8bpAz`</summary>

```text
=== MISTRAL/LLAMA EXPERIMENTS ===

--- exp_llama8b_10k ---
  Status: DONE
  Conclusion: negative
  Model: N/A
  Metrics: {
    "K_star": 1,
    "AUC_0v1": 0.9282,
    "AUC_1v2": 0.6148,
    "AUC_1v2_oof": 0.588,
    "AUC_2v3": 0.5247,
    "AUC_3v4": 0.5519,
    "AUC_4v5": 0.5262,
    "bootstrap_1v2_oof_auc": 0.588,
    "bootstrap_1v2_95CI": [
        0.5809,
        0.595
    ],
    "bootstrap_1v2_995CI_bonferroni": [
        0.5776,
        0.5978
    ],
    "bonferroni_pass": false,
    "perm_pvalue_1v2": 0.0001,
    "scorer": "Qwen2.5-1.5B-Instruct",
    "note": "All pairwise AUC from Qwen cross-scoring (Phase 2). Pipeline AUC 1v2=0.6148 (mean-of-folds)."
}

--- exp_cross_transfer_llama8b_to_qwen7b_v2 ---
  Status: DONE
  Conclusion: success
  Model: DeBERTa-v3-base
  Metrics: {
    "K_star": 3,
    "2v3_auc_ci_lower": 0.6124,
    "theta": 0.6,
    "margin_pp": 1.24
}

--- exp_cross_transfer_llama8b_to_qwen7b ---
  Status: DONE
  Conclusion: failed
  Model: DeBERTa-v3-base

--- exp_cross_transfer_qwen7b_to_llama8b ---
  Status: DONE
  Conclusion: success
  Model: DeBERTa-v3-base
  Metrics: {
    "kstar": 3,
    "kstar_indexing": "1-indexed",
    "pairwise_auc": {
        "0v1": 0.9998,
        "1v2": 0.7384,
        "2v3": 0.6278,
        "3v4": 0.587,
        "4v5": 0.5519
    },
    "elapsed_s": 3621
}

--- exp_code_mistral7b ---
  Status: DONE
  Conclusion: success
  Model: Mistral-7B-v0.3
  Metrics: {
    "k_star": 2,
    "pairwise_auc": {
        "0v1": 0.9191,
        "1v2": 0.6152,
        "2v3": 0.5293,
        "3v4": 0.5286,
        "4v5": 0.5099
    },
    "pairwise_auc_ci": {
        "0v1": 0.0017,
        "1v2": 0.012,
        "2v3": 0.0091,
        "3v4": 0.0104,
        "4v5": 0.006
    },
    "pairwise_jsd": {
        "0v1": 0.046984,
        "1v2": 0.011845,
        "2v3": 0.003717,
        "3v4": 0.003206,
        "4v5": 0.003083
    },
    "ordinal_mae": 1.3191,
    "ordinal_accuracy": 0.3243,
    "top3_features": [
        "freq_entropy",
        "surp_d2_mean",
        "surp_d1_mean"
    ]
}
  Notes: Log writes to /dev/pts/3 (terminal session), not a file. Progress inferred from data dir: depth_1.jsonl done (5500 lines), depth_2 in progress. No persistent log file for post-mortem analysis.

--- exp_code_llama8b ---
  Status: DONE
  Conclusion: success
  Model: LLaMA-3.1-8B
  Metrics: {
    "K_star": 2,
    "pairwise_auc": {
        "0v1": 0.9161,
        "1v2": 0.7394,
        "2v3": 0.5112,
        "3v4": 0.52,
        "4v5": 0.4996
    },
    "pairwise_auc_std": {
        "0v1": 0.004,
        "1v2": 0.0101,
        "2v3": 0.0095,
        "3v4": 0.0137,
        "4v5": 0.0069
    },
    "pairwise_jsd": {
        "0v1": 0.060406,
        "1v2": 0.047034,
        "2v3": 0.003473,
        "3v4": 0.003026,
        "4v5": 0.002892
    },
    "ordinal_mae": 1.2542,
    "ordinal_accuracy": 0.3485,
    "top_features": [
        "freq_entropy",
        "surp_d1_mean",
        "surp_d2_mean"
    ]
}
  Notes: Generation completed normally (11.37 GPU-hours). Analysis step crashed on M010 bug (int(doc_id) on string 'code_py_0'). Bug was already patched in code (try/except at line 462-466). Worker re-ran analysis only → K*=2 confirmed. Results in results/exp_code_llama8b/.

--- exp_arXiv_mistral7b_crossscorer ---
  Status: DONE
  Conclusion: success
  Model: Mistral-7B (generator) + Pythia-1.4B (scorer)
  Metrics: {
    "k_star": 3,
    "scorer": "pythia-1.4b",
    "auc_0v1": 0.9798,
    "auc_1v2": 0.8141,
    "auc_2v3": 0.6075,
    "auc_3v4": 0.5489,
    "auc_4v5": 0.5391,
    "jsd_0v1": 0.135575,
    "jsd_1v2": 0.078,
    "jsd_2v3": 0.020452,
    "jsd_3v4": 0.010992,
    "jsd_4v5": 0.008831,
    "ordinal_mae": 0.9061,
    "ordinal_accuracy": 0.4412
}
  Notes: Pythia-1.4B cross-scorer confirms K*=3 for Mistral-7B arXiv, matching Qwen-1.5B original. Max AUC delta = 0.02 (at 2v3). arXiv Mistral K*=3 is scorer-independent. Contrasts with Wikipedia where scorer choice affected K*.

--- exp_arXiv_llama8b_crossscorer ---
  Status: DONE
  Conclusion: success
  Model: pythia-1.4b
  Metrics: {
    "k_star": 3,
    "auc_0v1": 0.9629,
    "auc_1v2": 0.8433,
    "auc_2v3": 0.6201,
    "auc_3v4": 0.523,
    "auc_4v5": 0.5245,
    "jsd_0v1": 0.1214,
    "jsd_1v2": 0.0815,
    "jsd_2v3": 0.0195,
    "jsd_3v4": 0.0083,
    "jsd_4v5": 0.0082,
    "ordinal_mae": 0.9025,
    "ordinal_accuracy": 0.4407,
    "scorer": "pythia-1.4b"
}

--- exp_wiki_mistral7b ---
  Status: DONE
  Conclusion: success
  Model: mistralai/Mistral-7B-v0.3
  Metrics: {
    "K_star": 1,
    "ordinal_mae": 1.3445,
    "ordinal_accuracy": 0.3273,
    "auc_0v1": 0.9607,
    "auc_1v2": 0.5552,
    "auc_2v3": 0.5236,
    "auc_3v4": 0.5181,
    "auc_4v5": 0.5012,
    "jsd_0v1": 0.054134,
    "jsd_1v2": 0.005678,
    "jsd_2v3": 0.003698,
    "jsd_3v4": 0.003459,
    "jsd_4v5": 0.003274
}

--- exp_wiki_llama8b ---
  Status: DONE
  Conclusion: negative
  Model: Meta-Llama-3.1-8B
  Metrics: {
    "K_star": 1,
    "ordinal_mae": 1.2954,
    "ordinal_accuracy": 0.3313,
    "auc_0v1": 0.9316,
    "auc_1v2": 0.5954,
    "auc_2v3": 0.5392,
    "auc_3v4": 0.5221,
    "auc_4v5": 0.5212,
    "jsd_0v1": 0.06169,
    "jsd_1v2": 0.00931
}

--- exp_arXiv_mistral7b ---
  Status: DONE
  Conclusion: success
  Model: mistralai/Mistral-7B-v0.3
  Metrics: {
    "k_star": 3,
    "pairwise_auc": {
        "0v1": 0.9848,
        "1v2": 0.8201,
        "2v3": 0.6275,
        "3v4": 0.5295,
        "4v5": 0.5295
    },
    "jsd": {
        "0v1": 0.14249,
        "1v2": 0.076232,
        "2v3": 0.018972,
        "3v4": 0.009908,
        "4v5": 0.008877
    },
    "ordinal_mae": 0.8958,
    "ordinal_accuracy": 0.4474,
    "top_features": [
        "freq_entropy",
        "surp_std",
        "surp_d1_skew",
        "surp_mean",
        "surp_d2_mean"
    ]
}

--- exp_arXiv_llama8b ---
  Status: DONE
  Conclusion: success
  Model: Meta-Llama-3.1-8B
  Metrics: {
    "K_star": 3,
    "auc_0v1": 0.9754,
    "auc_1v2": 0.8447,
    "auc_2v3": 0.6215,
    "auc_3v4": 0.5362,
    "auc_4v5": 0.5331,
    "jsd_0v1": 0.1296,
    "jsd_1v2": 0.0785,
    "jsd_2v3": 0.0177,
    "ordinal_acc": 0.4549,
    "ordinal_mae": 0.8806
}

--- exp_018_llama8b_depth ---
  Status: DONE
  Conclusion: success
  Model: LLaMA-3.1-8B (Meta-Llama-3.1-8B)
  Metrics: {
    "k_star": 2,
    "pairwise_auc": {
        "0v1": 0.9225,
        "1v2": 0.6123,
        "2v3": 0.5274,
        "3v4": 0.5138,
        "4v5": 0.5097
    },
    "jsd": {
        "0v1": 0.077,
        "1v2": 0.012,
        "2v3": 0.005
    },
    "bootstrap_ci": {
        "0v1": {
            "auc": 0.9224,
            "ci_lower": 0.9174,
            "ci_upper": 0.9272,
            "perm_p": 0.0001
        },
        "1v2": {
            "auc": 0.6123,
            "ci_lower": 0.6028,
            "ci_upper": 0.6216,
            "perm_p": 0.0001
        },
        "2v3": {
            "auc": 0.5273,
            "ci_lower": 0.5169,
            "ci_upper": 0.5378,
            "perm_p": 0.0001
        },
        "3v4": {
            "auc": 0.5168,
            "ci_lower": 0.5062,
            "ci_upper": 0.5275,
            "perm_p": 0.0037
        },
        "4v5": {
            "auc": 0.5159,
            "ci_lower": 0.5052,
            "ci_upper": 0.5268,
            "perm_p": 0.0035
        }
    },
    "bootstrap_resamples": 10000,
    "permutation_resamples": 10000
}
  Notes: 2026-05-16 日志诊断：实验实际已成功完成(K*=2, AUC 1v2=0.6123)，Pipeline complete 正常退出。被 cron 误判 failed 原因：进程正常结束后 PID 10403 消失，无 sentinel/W&B 信号，监控 5× 检查后 auto-resolve 为 failed。结果文件完整存在于 results/exp_018_llama8b/。应改 conclusion=success。

--- exp_019b_mistral_cross_scorer ---
  Status: DONE
  Conclusion: success
  Model: mistral-7b-cross-qwen1.5b-scorer
  Metrics: {
    "k_star": 1,
    "pairwise_auc": {
        "0v1": 0.9209,
        "1v2": 0.5695,
        "2v3": 0.5335,
        "3v4": 0.514,
        "4v5": 0.5184
    },
    "bootstrap_ci": {
        "0v1": {
            "mean": 0.9209,
            "ci_lower": 0.9189,
            "ci_upper": 0.9229,
            "pass_060": true
        },
        "1v2": {
            "mean": 0.5696,
            "ci_lower": 0.5645,
            "ci_upper": 0.5746,
            "pass_060": false
        },
        "2v3": {
            "mean": 0.5335,
            "ci_lower": 0.5283,
            "ci_upper": 0.5382,
            "pass_060": false
        },
        "3v4": {
            "mean": 0.514,
            "ci_lower": 0.5063,
            "ci_upper": 0.5213,
            "pass_060": false
        },
        "4v5": {
            "mean": 0.5183,
            "ci_lower": 0.5128,
            "ci_upper": 0.5244,
            "pass_060": false
        }
    },
    "jsd": {
        "0v1": 0.08355,
        "1v2": 0.007642,
        "2v3": 0.004752,
        "3v4": 0.004255,
        "4v5": 0.003758
    },
    "ordinal_mae": 1.3737,
    "ordinal_accuracy": 0.3179,
    "top3_features": [
        "freq_entropy",
        "surp_d1_skew",
        "surp_d1_mean"
    ],
    "key_finding": "Cross-scorer (Qwen-1.5B scoring Mistral text) confirms K*=1. 1v2 AUC=0.5695 (self-scorer was 0.5935) \u2014 cross-scorer LOWER, not higher. Mistral K*=1 is genuine (inherent to Mistral generations), NOT a self-scorer artifact."
}
  Notes: K*=1 confirmed genuine (not self-scorer artifact). Cross-scorer (Qwen-base) 1v2 AUC=0.5695 CI [0.5645, 0.5746] — 比 self-scorer (0.5935) 更低。换 scorer 后区分度下降，排除 self-scorer inflation 假说。Top-3 features 与 self-scorer 完全一致: freq_entropy, surp_d1_skew, surp_d1_mean。

--- exp_019_mistral7b_depth ---
  Status: DONE
  Conclusion: success
  Model: mistralai/Mistral-7B-v0.3 (fp16)
  Metrics: {
    "k_star": 1,
    "pairwise_auc": {
        "0v1": 0.9843,
        "1v2": 0.5935,
        "2v3": 0.5402,
        "3v4": 0.5232,
        "4v5": 0.5181
    },
    "bootstrap_ci_1v2": {
        "ci_lower": 0.5835,
        "ci_upper": 0.6032,
        "p_auc_leq_060": 0.9017
    },
    "jsd": {
        "0v1": 0.124194,
        "1v2": 0.008051,
        "2v3": 0.005047,
        "3v4": 0.004516,
        "4v5": 0.004109
    },
    "ordinal_mae": 1.2275,
    "ordinal_accuracy": 0.3567,
    "top3_features": [
        "freq_entropy",
        "surp_d1_skew",
        "surp_d1_mean"
    ]
}
  Notes: K*=1 (非预期的 K*=2)。1v2 AUC=0.5935±0.0054，低于 θ=0.60 阈值仅 0.0065。边界线结果，需 bootstrap CI 确认。0v1 AUC=0.9843 强可区分。Self-scorer (Mistral-7B)。cuda:1 已空闲。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a33535dd-b874-4484-9c9d-f01b8c856882",
  "isSidechain": true,
  "promptId": "7d9f03b2-f13f-4ae8-b207-26c75cd900b2",
  "agentId": "a00d6d05ce2acd01d",
  "type": "user",
  "uuid": "dbf2bd9c-25bf-41d0-856b-e56da1f7a5ad",
  "sourceToolAssistantUUID": "a33535dd-b874-4484-9c9d-f01b8c856882",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-24T04:29:14.479Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01DZY7gWLhQaNLYyGvNbHhfX`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2/tool-results/mcp-agent-ml-research-read_registry-1779596868416.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Dose response / contamination rate experiments\nkeys = [k for k in exps if 'dose' in k.lower() or 'contamination_rate' in k.lower()]\nprint('=== DOSE RESPONSE / CONTAMINATION RATE ===')\nfor k in sorted(keys):\n    e = exps[k]\n    print(f'\\n--- {k} ---')\n    print(f'  Status: {e.get(\\\"status\\\")}')\n    print(f'  Conclusion: {e.get(\\\"conclusion\\\", \\\"N/A\\\")}')\n    if 'metrics' in e:\n        print(f'  Metrics: {json.dumps(e[\\\"metrics\\\"], indent=4)}')\n    if 'notes' in e:\n        print(f'  Notes: {str(e[\\\"notes\\\"])[:300]}')\n\" 2>&1 | head -500",
  "description": "Extract dose response and contamination rate experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbf2bd9c-25bf-41d0-856b-e56da1f7a5ad",
  "isSidechain": true,
  "agentId": "a00d6d05ce2acd01d",
  "requestId": "req_011CbLmEZXPiBHnN4k9EzF5X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1d6b8b41-63ad-4434-953d-c42031ed8232",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SFQf1U5hYWXcPQexUa8h8A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4771,
      "cache_read_input_tokens": 20462,
      "output_tokens": 1341,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4771
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1341,
          "cache_read_input_tokens": 20462,
          "cache_creation_input_tokens": 4771,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4771,
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

_source line 29 · 2026-05-24T04:29:14.571Z_

<details><summary>↩ Tool result · `toolu_01DZY7gWLhQaNLYyGvNbHhfX`</summary>

```text
=== DOSE RESPONSE / CONTAMINATION RATE ===

--- exp_009_dose_10pct ---
  Status: DONE
  Conclusion: failed

--- exp_009_dose_10pct_v2 ---
  Status: DONE
  Conclusion: failed

--- exp_009_dose_10pct_v3 ---
  Status: DONE
  Conclusion: success
  Metrics: {
    "seeds": 5,
    "strategies": 3,
    "total_runs": 15,
    "mean_std": {
        "no_filter": {
            "mmlu": "0.6058\u00b10.0002",
            "hellaswag": "0.6689\u00b10.0007"
        },
        "binary_ours": {
            "mmlu": "0.6079\u00b10.0005",
            "hellaswag": "0.6727\u00b10.0008"
        },
        "graduated": {
            "mmlu": "0.6066\u00b10.0011",
            "hellaswag": "0.6700\u00b10.0015"
        }
    },
    "paired_ttest": {
        "binary_vs_nofilter": {
            "delta_mmlu": 0.0021,
            "p_mmlu": 0.001,
            "delta_hellaswag": 0.0038,
            "p_hellaswag": 0.0017
        },
        "graduated_vs_binary": {
            "delta_mmlu": -0.0014,
            "p_mmlu": 0.0917,
            "delta_hellaswag": -0.0027,
            "p_hellaswag": 0.0399
        },
        "graduated_vs_nofilter": {
            "delta_mmlu": 0.0008,
            "p_mmlu": 0.2706,
            "delta_hellaswag": 0.0011,
            "p_hellaswag": 0.0611
        }
    },
    "key_finding": "Binary best. Graduated \u2248 no_filter."
}

--- exp_009_dose_30pct ---
  Status: DONE
  Conclusion: failed

--- exp_009_dose_30pct_v2 ---
  Status: DONE
  Conclusion: failed

--- exp_009_dose_30pct_v3 ---
  Status: DONE
  Conclusion: success
  Metrics: {
    "seeds": 5,
    "strategies": 3,
    "total_runs": 15,
    "mean_std": {
        "no_filter": {
            "mmlu": "0.6069\u00b10.0007",
            "hellaswag": "0.6664\u00b10.0020"
        },
        "binary_ours": {
            "mmlu": "0.6082\u00b10.0012",
            "hellaswag": "0.6725\u00b10.0007"
        },
        "graduated": {
            "mmlu": "0.6072\u00b10.0008",
            "hellaswag": "0.6665\u00b10.0014"
        }
    },
    "paired_ttest": {
        "binary_vs_nofilter": {
            "delta_mmlu": 0.0013,
            "p_mmlu": 0.0739,
            "delta_hellaswag": 0.0061,
            "p_hellaswag": 0.0036
        },
        "graduated_vs_binary": {
            "delta_mmlu": -0.001,
            "p_mmlu": 0.3018,
            "delta_hellaswag": -0.006,
            "p_hellaswag": 0.0009
        },
        "graduated_vs_nofilter": {
            "delta_mmlu": 0.0003,
            "p_mmlu": 0.6638,
            "delta_hellaswag": 0.0002,
            "p_hellaswag": 0.6646
        }
    },
    "key_finding": "Binary best on HellaSwag (p=0.004). Graduated = no_filter."
}

--- exp_009_dose_50pct ---
  Status: DONE
  Conclusion: failed

--- exp_009_dose_50pct_v2 ---
  Status: DONE
  Conclusion: failed

--- exp_009_dose_50pct_v3 ---
  Status: DONE
  Conclusion: success
  Metrics: {
    "seeds": 5,
    "strategies": 3,
    "total_runs": 15,
    "mean_std": {
        "no_filter": {
            "mmlu": "0.6063\u00b10.0013",
            "hellaswag": "0.6680\u00b10.0005"
        },
        "binary_ours": {
            "mmlu": "0.6088\u00b10.0011",
            "hellaswag": "0.6731\u00b10.0004"
        },
        "graduated": {
            "mmlu": "0.6062\u00b10.0009",
            "hellaswag": "0.6679\u00b10.0002"
        }
    },
    "paired_ttest": {
        "binary_vs_nofilter": {
            "delta_mmlu": 0.0025,
            "p_mmlu": 0.0377,
            "delta_hellaswag": 0.0051,
            "p_hellaswag": 2e-05
        },
        "graduated_vs_binary": {
            "delta_mmlu": -0.0026,
            "p_mmlu": 0.0257,
            "delta_hellaswag": -0.0052,
            "p_hellaswag": 3e-05
        },
        "graduated_vs_nofilter": {
            "delta_mmlu": -0.0001,
            "p_mmlu": 0.89,
            "delta_hellaswag": -0.0001,
            "p_hellaswag": 0.706
        }
    },
    "key_finding": "Binary significantly best (HellaSwag p<0.001). Graduated = no_filter exactly."
}

--- exp_009_dose_response ---
  Status: DONE
  Conclusion: success
  Metrics: {
    "total_runs": 45,
    "seeds": 5,
    "ratios": [
        0.1,
        0.3,
        0.5
    ],
    "strategies": [
        "no_filter",
        "binary_ours",
        "graduated"
    ],
    "cross_ratio_finding": "Binary filtering consistently best across all ratios. Graduated filtering = no_filter at every ratio. Effect size of binary advantage increases with contamination ratio (HellaSwag delta: 10%=+0.38pp, 30%=+0.61pp, 50%=+0.51pp). Original C3 hypothesis (graduated > binary) rejected.",
    "gpu_hours_total": 9.9
}

--- exp_contamination_rate_sweep ---
  Status: DONE
  Conclusion: success
  Metrics: {
    "rate_10": {
        "no_filter": {
            "mmlu": 0.5878,
            "hellaswag": 0.6652,
            "arc_c": 0.4471
        },
        "binary": {
            "mmlu": 0.5868,
            "hellaswag": 0.6709,
            "arc_c": 0.4462
        },
        "graduated": {
            "mmlu": 0.5873,
            "hellaswag": 0.6672,
            "arc_c": 0.4428
        }
    },
    "rate_30": {
        "no_filter": {
            "mmlu": 0.5885,
            "hellaswag": 0.6625,
            "arc_c": 0.4334
        },
        "binary": {
            "mmlu": 0.5867,
            "hellaswag": 0.6702,
            "arc_c": 0.448
        },
        "graduated": {
            "mmlu": 0.5873,
            "hellaswag": 0.664,
            "arc_c": 0.4334
        }
    },
    "rate_50": {
        "no_filter": {
            "mmlu": 0.5858,
            "hellaswag": 0.6582,
            "arc_c": 0.43
        },
        "binary": {
            "mmlu": 0.5913,
            "hellaswag": 0.67,
            "arc_c": 0.4505
        },
        "graduated": {
            "mmlu": 0.5848,
            "hellaswag": 0.6606,
            "arc_c": 0.4292
        }
    },
    "rate_100": {
        "no_filter": {
            "mmlu": 0.5707,
            "hellaswag": 0.6217,
            "arc_c": 0.3891
        },
        "binary": null,
        "graduated": {
            "mmlu": 0.5701,
            "hellaswag": 0.6215,
            "arc_c": 0.3933
        }
    }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d6b8b41-63ad-4434-953d-c42031ed8232",
  "isSidechain": true,
  "promptId": "7d9f03b2-f13f-4ae8-b207-26c75cd900b2",
  "agentId": "a00d6d05ce2acd01d",
  "type": "user",
  "uuid": "eed23908-7b20-4687-9fe1-7b9c1088d7e1",
  "sourceToolAssistantUUID": "1d6b8b41-63ad-4434-953d-c42031ed8232",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-24T04:29:33.216Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01F1csmeS9jjviKw9edfxnFA`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2/tool-results/mcp-agent-ml-research-read_registry-1779596868416.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Bootstrap / kstar experiments\nkeys = [k for k in exps if 'bootstrap' in k.lower() or 'kstar' in k.lower()]\nprint('=== BOOTSTRAP / KSTAR EXPERIMENTS ===')\nfor k in sorted(keys):\n    e = exps[k]\n    print(f'\\n--- {k} ---')\n    print(f'  Status: {e.get(\\\"status\\\")}')\n    print(f'  Conclusion: {e.get(\\\"conclusion\\\", \\\"N/A\\\")}')\n    if 'metrics' in e:\n        print(f'  Metrics: {json.dumps(e[\\\"metrics\\\"], indent=4)}')\n    if 'notes' in e:\n        print(f'  Notes: {str(e[\\\"notes\\\"])[:400]}')\n\" 2>&1 | head -500",
  "description": "Extract bootstrap and kstar experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eed23908-7b20-4687-9fe1-7b9c1088d7e1",
  "isSidechain": true,
  "agentId": "a00d6d05ce2acd01d",
  "requestId": "req_011CbLmFvFMapEyYhJv71rbE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "402dd50d-27be-4c73-8258-509b62adb783",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E7Ujz6C2UDqVvKa2BA6ZiR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13632,
      "cache_read_input_tokens": 25233,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13632,
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

_source line 31 · 2026-05-24T04:29:33.308Z_

<details><summary>↩ Tool result · `toolu_01F1csmeS9jjviKw9edfxnFA`</summary>

```text
=== BOOTSTRAP / KSTAR EXPERIMENTS ===

--- exp_007_bootstrap_ci ---
  Status: DONE
  Conclusion: success
  Metrics: {
    "qwen_rewrite": {
        "0v1": {
            "auc": 0.9956,
            "ci_lower": 0.9946,
            "ci_upper": 0.9965,
            "perm_p": 0.002
        },
        "1v2": {
            "auc": 0.6955,
            "ci_lower": 0.6859,
            "ci_upper": 0.7041,
            "perm_p": 0.002
        },
        "2v3": {
            "auc": 0.5893,
            "ci_lower": 0.5795,
            "ci_upper": 0.5991,
            "perm_p": 0.002
        },
        "3v4": {
            "auc": 0.5435,
            "ci_lower": 0.5333,
            "ci_upper": 0.5551,
            "perm_p": 0.002
        },
        "4v5": {
            "auc": 0.534,
            "ci_lower": 0.5238,
            "ci_upper": 0.5448,
            "perm_p": 0.002
        }
    },
    "pythia_cont": {
        "0v1": {
            "auc": 0.9932,
            "ci_lower": 0.9921,
            "ci_upper": 0.9943,
            "perm_p": 0.002
        },
        "1v2": {
            "auc": 0.6539,
            "ci_lower": 0.6454,
            "ci_upper": 0.663,
            "perm_p": 0.002
        },
        "2v3": {
            "auc": 0.5514,
            "ci_lower": 0.5417,
            "ci_upper": 0.5628,
            "perm_p": 0.002
        },
        "3v4": {
            "auc": 0.5152,
            "ci_lower": 0.5041,
            "ci_upper": 0.526,
            "perm_p": 0.006
        },
        "4v5": {
            "auc": 0.5136,
            "ci_lower": 0.5021,
            "ci_upper": 0.5249,
            "perm_p": 0.008
        }
    },
    "olmo_cont": {
        "0v1": {
            "auc": 0.997,
            "ci_lower": 0.9964,
            "ci_upper": 0.9975,
            "perm_p": 0.002
        },
        "1v2": {
            "auc": 0.6145,
            "ci_lower": 0.6045,
            "ci_upper": 0.6247,
            "perm_p": 0.002
        },
        "2v3": {
            "auc": 0.5496,
            "ci_lower": 0.5399,
            "ci_upper": 0.5596,
            "perm_p": 0.002
        },
        "3v4": {
            "auc": 0.5091,
            "ci_lower": 0.4973,
            "ci_upper": 0.52,
            "perm_p": 0.064
        },
        "4v5": {
            "auc": 0.5045,
            "ci_lower": 0.4932,
            "ci_upper": 0.515,
            "perm_p": 0.232
        }
    },
    "qwen_cont": {
        "0v1": {
            "auc": 0.9971,
            "ci_lower": 0.9963,
            "ci_upper": 0.9978,
            "perm_p": 0.002
        },
        "1v2": {
            "auc": 0.6112,
            "ci_lower": 0.6015,
            "ci_upper": 0.6213,
            "perm_p": 0.002
        },
        "2v3": {
            "auc": 0.5609,
            "ci_lower": 0.5511,
            "ci_upper": 0.5712,
            "perm_p": 0.002
        },
        "3v4": {
            "auc": 0.5409,
            "ci_lower": 0.5308,
            "ci_upper": 0.5508,
            "perm_p": 0.002
        },
        "4v5": {
            "auc": 0.5141,
            "ci_lower": 0.5035,
            "ci_upper": 0.5255,
            "perm_p": 0.006
        }
    },
    "k_star_robust": true,
    "all_1v2_ci_lower_above_060": true,
    "most_marginal": "Qwen-cont CI lower=0.6015, only 0.0015 above threshold"
}

--- exp_027_retrain_bootstrap ---
  Status: DONE
  Conclusion: success
  Metrics: {
    "bootstrap_iterations": 10000,
    "pairs": {
        "0v1": {
            "auc_point": 0.9847,
            "ci_lower": 0.9828,
            "ci_upper": 0.9864,
            "perm_p": 0.0001,
            "ci_lower_gt_theta": true
        },
        "1v2": {
            "auc_point": 0.9482,
            "ci_lower": 0.9443,
            "ci_upper": 0.952,
            "perm_p": 0.0001,
            "ci_lower_gt_theta": true
        },
        "2v3": {
            "auc_point": 0.8885,
            "ci_lower": 0.8829,
            "ci_upper": 0.894,
            "perm_p": 0.0001,
            "ci_lower_gt_theta": true
        },
        "3v4": {
            "auc_point": 0.7977,
            "ci_lower": 0.7903,
            "ci_upper": 0.8051,
            "perm_p": 0.0001,
            "ci_lower_gt_theta": true
        }
    },
    "key_finding": "All 4 retrain-chain pairwise AUCs have CI_lower >> theta=0.60 (min CI_lower=0.7903). K*>=4 statistically confirmed with p<0.001."
}

--- exp_bootstrap_10k ---
  Status: DONE
  Conclusion: success
  Metrics: {
    "configs_tested": 4,
    "configs_missing": 2,
    "results": {
        "llama8b": {
            "auc": 0.6075,
            "ci_1k": [
                0.597,
                0.617
            ],
            "ci_10k": [
                0.598,
                0.617
            ],
            "verdict_1k": "BORDERLINE",
            "verdict_10k": "BORDERLINE",
            "flipped": false
        },
        "gemma2b": {
            "auc": 0.5981,
            "ci_1k": [
                0.588,
                0.608
            ],
            "ci_10k": [
                0.588,
                0.608
            ],
            "verdict_1k": "BORDERLINE",
            "verdict_10k": "BORDERLINE",
            "flipped": false
        },
        "mistral7b": {
            "auc": 0.5902,
            "ci_1k": [
                0.58,
                0.6
            ],
            "ci_10k": [
                0.58,
                0.6
            ],
            "verdict_1k": "K*=1",
            "verdict_10k": "BORDERLINE",
            "flipped_technical": true,
            "note": "CI upper 0.6000\u21920.6001 (noise, +0.01pp). Point estimate 0.5902 << theta. K*=1 unchanged."
        },
        "512tok": {
            "auc": 0.6136,
            "ci_1k": [
                0.604,
                0.623
            ],
            "ci_10k": [
                0.604,
                0.623
            ],
            "verdict_1k": "K*=2",
            "verdict_10k": "K*=2",
            "flipped": false
        }
    },
    "missing": [
        "exp_017_qwen_cont (features.csv not on disk)",
        "exp_002_olmo (features.csv not on disk)"
    ],
    "conclusion": "No substantive K* flips. 10K CI ~3% tighter. 1K resamples confirmed robust."
}

--- exp_changepoint_kstar ---
  Status: DONE
  Conclusion: success
  Metrics: {
    "exact_agreement": 0.459,
    "exact_agreement_n": "17/37",
    "within_1_agreement": 0.946,
    "within_1_agreement_n": "35/37",
    "cp_direction": "always_conservative",
    "disagreement_auc_range": [
        0.607,
        0.654
    ],
    "best_penalty": 0.1,
    "methods_tested": [
        "PELT",
        "BinSeg",
        "BottomUp"
    ],
    "bootstrap_samples": 2000
}

--- exp_kstar_theta ---
  Status: DONE
  Conclusion: success
  Metrics: {
    "output_files": [
        "kstar_theta_curve.pdf (32KB)",
        "kstar_theta_curve.png (335KB)"
    ],
    "models": [
        "Qwen-rewrite",
        "Pythia",
        "OLMo",
        "Qwen-cont"
    ],
    "depth_pairs": 5,
    "key_finding": "All 4 models show AUC \u22650.993 at 0v1, decaying to ~0.50-0.53 at 4v5. \u03b8=0.60 is justified as natural K*=2 boundary across all models. FR-1 Critical resolved."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "402dd50d-27be-4c73-8258-509b62adb783",
  "isSidechain": true,
  "promptId": "7d9f03b2-f13f-4ae8-b207-26c75cd900b2",
  "agentId": "a00d6d05ce2acd01d",
  "type": "user",
  "uuid": "17bcb07f-719b-4958-9998-3a974c1f78ee",
  "sourceToolAssistantUUID": "402dd50d-27be-4c73-8258-509b62adb783",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-24T04:29:37.677Z_

<details open><summary>🔧 Tool call — Bash · `toolu_015KSJanbgCfH4CT3WgMjsfs`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2/tool-results/mcp-agent-ml-research-read_registry-1779596868416.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Cross-transfer experiments\nkeys = [k for k in exps if 'cross_transfer' in k.lower() or k == 'exp_013_cross_transfer' or k == 'exp-013' or k == '7b-cross-transfer']\nprint('=== CROSS-TRANSFER EXPERIMENTS ===')\nfor k in sorted(keys):\n    e = exps[k]\n    print(f'\\n--- {k} ---')\n    print(f'  Status: {e.get(\\\"status\\\")}')\n    print(f'  Conclusion: {e.get(\\\"conclusion\\\", \\\"N/A\\\")}')\n    if 'spec' in e:\n        print(f'  Model: {e[\\\"spec\\\"].get(\\\"model_name\\\", \\\"N/A\\\")}')\n    if 'metrics' in e:\n        print(f'  Metrics: {json.dumps(e[\\\"metrics\\\"], indent=4)}')\n    if 'notes' in e:\n        print(f'  Notes: {str(e[\\\"notes\\\"])[:400]}')\n\" 2>&1 | head -500",
  "description": "Extract cross-transfer experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17bcb07f-719b-4958-9998-3a974c1f78ee",
  "isSidechain": true,
  "agentId": "a00d6d05ce2acd01d",
  "requestId": "req_011CbLmFvFMapEyYhJv71rbE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c8bd4b8-46ae-451d-b185-3d69e2b18af4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E7Ujz6C2UDqVvKa2BA6ZiR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13632,
      "cache_read_input_tokens": 25233,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13632,
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

_source line 33 · 2026-05-24T04:29:37.766Z_

<details><summary>↩ Tool result · `toolu_015KSJanbgCfH4CT3WgMjsfs`</summary>

```text
=== CROSS-TRANSFER EXPERIMENTS ===

--- 7b-cross-transfer ---
  Status: PREPARING
  Conclusion: killed

--- exp_013_cross_transfer ---
  Status: DONE
  Conclusion: success
  Model: N/A (CPU classifiers: OBD-LightGBM)
  Metrics: {
    "accuracy_matrix": {
        "Qwen_rw\u2192Qwen_rw": 0.4229,
        "Qwen_rw\u2192Pythia": 0.259,
        "Qwen_rw\u2192OLMo": 0.2653,
        "Qwen_rw\u2192Qwen_cont": 0.3466,
        "Pythia\u2192Qwen_rw": 0.2718,
        "Pythia\u2192Pythia": 0.3856,
        "Pythia\u2192OLMo": 0.3531,
        "Pythia\u2192Qwen_cont": 0.3287,
        "OLMo\u2192Qwen_rw": 0.2768,
        "OLMo\u2192Pythia": 0.345,
        "OLMo\u2192OLMo": 0.3822,
        "OLMo\u2192Qwen_cont": 0.3244,
        "Qwen_cont\u2192Qwen_rw": 0.344,
        "Qwen_cont\u2192Pythia": 0.3284,
        "Qwen_cont\u2192OLMo": 0.3112,
        "Qwen_cont\u2192Qwen_cont": 0.3875
    },
    "transfer_retention_accuracy": {
        "Pythia\u2194OLMo": "91-92%",
        "Qwen_rw\u2192Pythia/OLMo": "61-63%",
        "Qwen_cont\u2194Pythia": "83-85%",
        "Qwen_cont\u2194OLMo": "80-85%"
    },
    "transfer_retention_tau": {
        "Pythia\u2194OLMo": "85-86%",
        "Qwen_rw\u2192Pythia/OLMo": "45-50%",
        "Qwen_cont\u2194others": "68-83%"
    },
    "mean_pw_auc_matrix": {
        "within_avg": 0.6099,
        "cross_avg": 0.5905,
        "0v1_cross_all_above": 0.96
    },
    "key_finding": "depth signal \u2248 70-85% text-intrinsic + 15-30% model self-familiarity. Binary contamination detection (0v1) highly transferable (>0.96 AUC). Fine-grained depth transfer depends on model family similarity. Qwen-rewrite overfits style features; Qwen-cont transfers much better."
}
  Notes: depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity. Pythia↔OLMo 91-92% retention (architecture-agnostic). Qwen-rewrite catastrophic transfer to other models (61-63%), but Qwen-cont much better (80-85%). 0v1 universally transferable (>0.96 AUC), 1v2+ transfer depends on model family. Rewrite mode overfits style features → continuation mode is canonical condition for cross-model cl

--- exp_cross_transfer_llama8b_to_qwen7b ---
  Status: DONE
  Conclusion: failed
  Model: DeBERTa-v3-base

--- exp_cross_transfer_llama8b_to_qwen7b_v2 ---
  Status: DONE
  Conclusion: success
  Model: DeBERTa-v3-base
  Metrics: {
    "K_star": 3,
    "2v3_auc_ci_lower": 0.6124,
    "theta": 0.6,
    "margin_pp": 1.24
}

--- exp_cross_transfer_qwen7b_to_llama8b ---
  Status: DONE
  Conclusion: success
  Model: DeBERTa-v3-base
  Metrics: {
    "kstar": 3,
    "kstar_indexing": "1-indexed",
    "pairwise_auc": {
        "0v1": 0.9998,
        "1v2": 0.7384,
        "2v3": 0.6278,
        "3v4": 0.587,
        "4v5": 0.5519
    },
    "elapsed_s": 3621
}

--- exp_deberta_cross_transfer_gpu1 ---
  Status: DONE
  Conclusion: success
  Model: DeBERTa-v3-base

--- exp_deberta_cross_transfer_gpu2 ---
  Status: DONE
  Conclusion: success
  Model: DeBERTa-v3-base

--- exp_deberta_cross_transfer_gpu3 ---
  Status: DONE
  Conclusion: success
  Model: DeBERTa-v3-base

--- exp_deberta_cross_transfer_wiki ---
  Status: DONE
  Conclusion: success
  Model: DeBERTa-v3-base
  Metrics: {
    "total_pairs_expected": 12,
    "completed_pairs": 10,
    "missing_pairs": [
        "qwen7b\u2192llama8b",
        "llama8b\u2192qwen7b"
    ],
    "bonus_pairs": [
        "pythia\u2192mistral7b (K*=2)",
        "mistral7b\u2192pythia (K*=2)"
    ],
    "kstar_distribution": {
        "K*=1": 3,
        "K*=2": 5,
        "K*=3": 1
    },
    "kstar_1_pairs": [
        "pythia\u2192olmo",
        "qwen7b\u2192olmo",
        "llama8b\u2192olmo"
    ],
    "kstar_3_pair": "pythia\u2192qwen7b",
    "kstar_2_pairs": [
        "olmo\u2192qwen7b",
        "olmo\u2192llama8b",
        "qwen7b\u2192pythia",
        "llama8b\u2192pythia",
        "pythia\u2192llama8b"
    ],
    "pattern": "All X\u2192OLMo = K*=1. pythia\u2192qwen7b highest at K*=3. GPU3 ran mistral7b pairs instead of expected qwen7b\u2194llama8b, causing 2 missing pairs.",
    "json_kstar_fix": "3 JSONs fixed +1 (pythia\u2192olmo 0\u21921, olmo\u2192qwen7b 1\u21922, olmo\u2192llama8b 1\u21922)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c8bd4b8-46ae-451d-b185-3d69e2b18af4",
  "isSidechain": true,
  "promptId": "7d9f03b2-f13f-4ae8-b207-26c75cd900b2",
  "agentId": "a00d6d05ce2acd01d",
  "type": "user",
  "uuid": "5b10052f-957e-4da1-895e-76f0a9226186",
  "sourceToolAssistantUUID": "5c8bd4b8-46ae-451d-b185-3d69e2b18af4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-24T04:29:40.974Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01DCKe3B2YuaU74Vjb75JrdK`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2/tool-results/mcp-agent-ml-research-read_registry-1779596868416.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# ANOVA, permutation, paired stats experiments\nkeys = [k for k in exps if 'anova' in k.lower() or 'permut' in k.lower() or 'paired' in k.lower() or 'stat' in k.lower()]\nprint('=== ANOVA / STATISTICAL TESTS ===')\nfor k in sorted(keys):\n    e = exps[k]\n    print(f'\\n--- {k} ---')\n    print(f'  Status: {e.get(\\\"status\\\")}')\n    print(f'  Conclusion: {e.get(\\\"conclusion\\\", \\\"N/A\\\")}')\n    if 'metrics' in e:\n        print(f'  Metrics: {json.dumps(e[\\\"metrics\\\"], indent=4)}')\n    if 'notes' in e:\n        print(f'  Notes: {str(e[\\\"notes\\\"])[:400]}')\n\" 2>&1 | head -500",
  "description": "Extract ANOVA and statistical test experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b10052f-957e-4da1-895e-76f0a9226186",
  "isSidechain": true,
  "agentId": "a00d6d05ce2acd01d",
  "requestId": "req_011CbLmFvFMapEyYhJv71rbE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "67343454-3c17-4ddd-83c8-257a9ae8805e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E7Ujz6C2UDqVvKa2BA6ZiR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13632,
      "cache_read_input_tokens": 25233,
      "output_tokens": 1328,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13632
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1328,
          "cache_read_input_tokens": 25233,
          "cache_creation_input_tokens": 13632,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13632,
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

_source line 35 · 2026-05-24T04:29:41.065Z_

<details><summary>↩ Tool result · `toolu_01DCKe3B2YuaU74Vjb75JrdK`</summary>

```text
=== ANOVA / STATISTICAL TESTS ===

--- exp_C_permutation_10k ---
  Status: DONE
  Conclusion: success
  Metrics: {
    "resamples": 10000,
    "all_boundary_pairs_p": "<0.0001",
    "key_finding": "10K permutation confirms all boundary p-values well below 0.01. FR-11 resolved."
}

--- exp_E_paired_stats ---
  Status: DONE
  Conclusion: success
  Metrics: {
    "mmlu_significant_pairs": "8/15",
    "hellaswag_significant_pairs": "9/15",
    "binary_ours_vs_all_mmlu": "all significant",
    "max_cohen_d_mmlu": 10.8,
    "max_cohen_d_hellaswag": 8.98,
    "graduated_a09_vs_dsir_corrected_p": 0.0523,
    "cohen_d_method": "d_av (Lakens 2013)",
    "key_finding": "binary-ours significantly outperforms all alternatives on MMLU. On HellaSwag, binary-ours and graduated_a0.9 tied (p=1.0). FR-5 resolved. Holm-Bonferroni cummax bug fixed: MMLU 10/15\u21928/15. Cohen's d changed to d_av.",
    "bugfix_note": "Holm-Bonferroni cummax variable was never updated, causing 2 MMLU pairs to be incorrectly marked significant (graduated_a0.9 vs no-filter, surprisal vs dsir). Cohen's d changed from d_z to d_av (Lakens 2013)."
}
  Notes: Holm-Bonferroni bug fixed: cummax variable was never updated in loop, causing adjusted p-values to lose monotonicity. MMLU significant pairs corrected 10/15→8/15. Cohen's d changed from d_z to d_av (Lakens 2013). d values still large (10.8) due to n=5 tiny within-seed variance — recommend mean_diff as primary effect size in paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67343454-3c17-4ddd-83c8-257a9ae8805e",
  "isSidechain": true,
  "promptId": "7d9f03b2-f13f-4ae8-b207-26c75cd900b2",
  "agentId": "a00d6d05ce2acd01d",
  "type": "user",
  "uuid": "d8119653-8f11-4092-9ab5-299db6592c16",
  "sourceToolAssistantUUID": "67343454-3c17-4ddd-83c8-257a9ae8805e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-24T04:29:50.916Z_

<details open><summary>🔧 Tool call — Bash · `toolu_018Az4mV4dBtkz5v6nH9DqyS`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2/tool-results/mcp-agent-ml-research-read_registry-1779596868416.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Runtime benchmark\nprint('=== RUNTIME BENCHMARK ===')\ne = exps.get('runtime_benchmark', {})\nprint(f'Status: {e.get(\\\"status\\\")}')\nprint(f'Conclusion: {e.get(\\\"conclusion\\\", \\\"N/A\\\")}')\nif 'metrics' in e:\n    print(f'Metrics: {json.dumps(e[\\\"metrics\\\"], indent=4)}')\nif 'notes' in e:\n    print(f'Notes: {str(e[\\\"notes\\\"])[:400]}')\n\" 2>&1",
  "description": "Extract runtime benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8119653-8f11-4092-9ab5-299db6592c16",
  "isSidechain": true,
  "agentId": "a00d6d05ce2acd01d",
  "requestId": "req_011CbLmHsYh3pPNhzRK8dwAM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "10afd1ef-90ca-4c43-88b4-cd724d57e66d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jh3Ts9MPbPWXZj2c2BjdZv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6597,
      "cache_read_input_tokens": 38865,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6597,
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

### Tool result

_source line 37 · 2026-05-24T04:29:50.994Z_

<details><summary>↩ Tool result · `toolu_018Az4mV4dBtkz5v6nH9DqyS`</summary>

```text
=== RUNTIME BENCHMARK ===
Status: PREPARING
Conclusion: N/A
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10afd1ef-90ca-4c43-88b4-cd724d57e66d",
  "isSidechain": true,
  "promptId": "7d9f03b2-f13f-4ae8-b207-26c75cd900b2",
  "agentId": "a00d6d05ce2acd01d",
  "type": "user",
  "uuid": "a384d2eb-87f6-4f6c-ae48-441a5a6f1145",
  "sourceToolAssistantUUID": "10afd1ef-90ca-4c43-88b4-cd724d57e66d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-24T04:29:56.123Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RhLVHnHqLJY7vv8Qyq2Q2Y`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2/tool-results/mcp-agent-ml-research-read_registry-1779596868416.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Filtering experiments (deberta, filtering, sweep, downstream)\nkeys = [k for k in exps if 'filter' in k.lower() or 'sweep' in k.lower() or 'downstream' in k.lower() or 'degradation' in k.lower()]\nprint('=== FILTERING / SWEEP / DOWNSTREAM EXPERIMENTS ===')\nfor k in sorted(keys):\n    e = exps[k]\n    if 'metrics' not in e:\n        continue\n    print(f'\\n--- {k} ---')\n    print(f'  Status: {e.get(\\\"status\\\")}')\n    print(f'  Conclusion: {e.get(\\\"conclusion\\\", \\\"N/A\\\")}')\n    m = e['metrics']\n    # Print compact metrics\n    mstr = json.dumps(m, indent=2)\n    if len(mstr) > 600:\n        print(f'  Metrics (truncated): {mstr[:600]}...')\n    else:\n        print(f'  Metrics: {mstr}')\n\" 2>&1 | head -800",
  "description": "Extract filtering/sweep/downstream experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a384d2eb-87f6-4f6c-ae48-441a5a6f1145",
  "isSidechain": true,
  "agentId": "a00d6d05ce2acd01d",
  "requestId": "req_011CbLmHsYh3pPNhzRK8dwAM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a74680ed-d271-437d-b353-3bfeb8f19134",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jh3Ts9MPbPWXZj2c2BjdZv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6597,
      "cache_read_input_tokens": 38865,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6597,
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

### Tool result

_source line 39 · 2026-05-24T04:29:56.205Z_

<details><summary>↩ Tool result · `toolu_01RhLVHnHqLJY7vv8Qyq2Q2Y`</summary>

```text
=== FILTERING / SWEEP / DOWNSTREAM EXPERIMENTS ===

--- exp_005_degradation ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "cross_model_kendall_tau_by_first_auc": {
    "Pythia_vs_OLMo": 0.733,
    "Pythia_vs_Qwen_rewrite": 0.467,
    "Pythia_vs_Qwen_cont": 0.695,
    "OLMo_vs_Qwen_rewrite": 0.429,
    "OLMo_vs_Qwen_cont": 0.543,
    "Qwen_rewrite_vs_Qwen_cont": 0.733
  },
  "cross_model_kendall_tau_by_avg_auc": {
    "Pythia_vs_OLMo": 0.8476,
    "Pythia_vs_Qwen_cont": 0.7524,
    "OLMo_vs_Qwen_cont": 0.6762
  },
  "cross_model_spearman_rho_single_feature_auc": {
    "Pythia_vs_OLMo": 0.95,
    "Pythia_vs_Qwen_cont": 0.9143,
    "OLMo_vs_Qwen_cont": 0.85,
    "metric_definition": "Spearman \u03c1 on per-featu...

--- exp_006_graduated_filtering ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "total_runs": 51,
  "binary_ours": {
    "mmlu": "0.5941\u00b10.0008",
    "hellaswag": "0.6701\u00b10.0006"
  },
  "binary_drayson": {
    "mmlu": "0.5913\u00b10.0009",
    "hellaswag": "0.6691\u00b10.0004"
  },
  "surprisal": {
    "mmlu": "0.5894\u00b10.0009",
    "hellaswag": "0.6641\u00b10.0006"
  },
  "graduated_a09": {
    "mmlu": "0.5892\u00b10.0008",
    "hellaswag": "0.6701\u00b10.0007"
  },
  "graduated_a07": {
    "mmlu": "0.5892\u00b10.0014",
    "hellaswag": "0.6695\u00b10.0004"
  },
  "graduated_a05": {
    "mmlu": "0.5880\u00b10.0013",
    "hellaswag": "0.6687\u00b10.0008"
...

--- exp_025_pythia_filtering ---
  Status: DONE
  Conclusion: negative
  Metrics (truncated): {
  "runs_completed": "9/9",
  "strategies": [
    "no_filter",
    "binary_ours",
    "graduated_a09"
  ],
  "seeds": [
    42,
    123,
    456
  ],
  "mmlu": {
    "no_filter": "0.2568\u00b10.0012",
    "binary_ours": "0.2585\u00b10.0004",
    "graduated_a09": "0.2561\u00b10.0009"
  },
  "hellaswag": {
    "no_filter": "0.5250\u00b10.0008",
    "binary_ours": "0.5251\u00b10.0001",
    "graduated_a09": "0.5253\u00b10.0007"
  },
  "delta_vs_no_filter": {
    "binary_ours_mmlu": "+0.0017",
    "binary_ours_hellaswag": "+0.0000",
    "graduated_a09_mmlu": "-0.0007",
    "graduated_a09_hellaswag...

--- exp_026_arxiv_filtering ---
  Status: DONE
  Conclusion: negative
  Metrics (truncated): {
  "runs_completed": "15/15",
  "strategies": [
    "no_filter",
    "binary",
    "graduated_a09"
  ],
  "seeds": [
    42,
    123,
    456,
    789,
    1024
  ],
  "mmlu": {
    "no_filter": "0.5899\u00b10.0008",
    "binary": "0.5876\u00b10.0004",
    "graduated_a09": "0.5900\u00b10.0011"
  },
  "hellaswag": {
    "no_filter": "0.6600\u00b10.0002",
    "binary": "0.6642\u00b10.0004",
    "graduated_a09": "0.6599\u00b10.0003"
  },
  "delta_vs_no_filter": {
    "binary_mmlu": "-0.0023",
    "binary_hellaswag": "+0.0042",
    "graduated_mmlu": "+0.0001",
    "graduated_hellaswag": "-0.0001"...

--- exp_contamination_rate_sweep ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "rate_10": {
    "no_filter": {
      "mmlu": 0.5878,
      "hellaswag": 0.6652,
      "arc_c": 0.4471
    },
    "binary": {
      "mmlu": 0.5868,
      "hellaswag": 0.6709,
      "arc_c": 0.4462
    },
    "graduated": {
      "mmlu": 0.5873,
      "hellaswag": 0.6672,
      "arc_c": 0.4428
    }
  },
  "rate_30": {
    "no_filter": {
      "mmlu": 0.5885,
      "hellaswag": 0.6625,
      "arc_c": 0.4334
    },
    "binary": {
      "mmlu": 0.5867,
      "hellaswag": 0.6702,
      "arc_c": 0.448
    },
    "graduated": {
      "mmlu": 0.5873,
      "hellaswag": 0.664,
      "arc_c": 0.43...

--- exp_deberta_filtering_comparison ---
  Status: DONE
  Conclusion: success
  Metrics: {
  "no_filter": {
    "mmlu": 0.5895,
    "hellaswag": 0.6591,
    "arc_c": 0.4352
  },
  "obd_binary": {
    "mmlu": 0.588,
    "hellaswag": 0.6599,
    "arc_c": 0.4522
  },
  "deberta_binary": {
    "mmlu": 0.587,
    "hellaswag": 0.6593,
    "arc_c": 0.4471
  },
  "deberta_graduated": {
    "mmlu": 0.5884,
    "hellaswag": 0.6586,
    "arc_c": 0.442
  },
  "summary": "obd_binary (15D) >= deberta_binary on all 3 benchmarks. DeBERTa K*=4 does not yield better filtering than 15D K*=3. Graduated < binary for both OBD and DeBERTa."
}

--- exp_expanded_downstream_eval ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "metric_standard": "PIQA=acc_norm, ARC-C=acc_norm, WinoGrande=acc, TruthfulQA=mc2, GSM8K=exact_match(strict)",
  "base_model": {
    "piqa": 0.7612,
    "arc_c": 0.5486,
    "winogrande": 0.6456,
    "truthfulqa": 0.4659,
    "gsm8k": 0.6224
  },
  "no_filter_mean": {
    "piqa": 0.7519,
    "arc_c": 0.5193,
    "winogrande": 0.6485,
    "truthfulqa": 0.4246,
    "gsm8k": 0.5666
  },
  "binary_ours_mean": {
    "piqa": 0.7479,
    "arc_c": 0.5171,
    "winogrande": 0.6406,
    "truthfulqa": 0.4398,
    "gsm8k": 0.5858
  },
  "graduated_mean": {
    "piqa": 0.751,
    "arc_c": 0.519,
    "w...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a74680ed-d271-437d-b353-3bfeb8f19134",
  "isSidechain": true,
  "promptId": "7d9f03b2-f13f-4ae8-b207-26c75cd900b2",
  "agentId": "a00d6d05ce2acd01d",
  "type": "user",
  "uuid": "604df326-6d67-4cb9-bb0c-267d9c8955e8",
  "sourceToolAssistantUUID": "a74680ed-d271-437d-b353-3bfeb8f19134",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-24T04:30:04.732Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01BpDi2BMbvkMMtkmeSX6fx4`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2/tool-results/mcp-agent-ml-research-read_registry-1779596868416.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Gemma, decoding ablation (exp_003), 7b crossscale (exp_004), retrain chain, length ablation, domain ablation, ordinal baseline, neural probe\nspecial_keys = ['exp_gemma2b_depth', 'exp_003_decoding_ablation', 'exp_004_7b_crossscale', \n                'exp_008_retrain_chain', 'exp_021_length_ablation', 'exp_023_domain_ablation',\n                'exp_010_ordinal_baseline', 'exp_015_neural_probe', 'exp_016_base_vs_instruct',\n                'exp_017_qwen_continuation', 'exp_014_naturalistic', 'exp_012_binary_confidence',\n                'exp_011_llm_zeroshot', 'exp_B_14d_ablation', 'exp_A_alt_scorer', 'exp_D_obd_n500']\nprint('=== SPECIAL EXPERIMENTS ===')\nfor k in special_keys:\n    e = exps.get(k)\n    if not e:\n        print(f'\\n--- {k} --- NOT FOUND')\n        continue\n    print(f'\\n--- {k} ---')\n    print(f'  Status: {e.get(\\\"status\\\")}')\n    print(f'  Conclusion: {e.get(\\\"conclusion\\\", \\\"N/A\\\")}')\n    if 'metrics' in e:\n        mstr = json.dumps(e['metrics'], indent=2)\n        if len(mstr) > 800:\n            print(f'  Metrics (truncated): {mstr[:800]}...')\n        else:\n            print(f'  Metrics: {mstr}')\n    if 'notes' in e:\n        print(f'  Notes: {str(e[\\\"notes\\\"])[:300]}')\n\" 2>&1 | head -1000",
  "description": "Extract Gemma, decoding ablation, and other special experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "604df326-6d67-4cb9-bb0c-267d9c8955e8",
  "isSidechain": true,
  "agentId": "a00d6d05ce2acd01d",
  "requestId": "req_011CbLmHsYh3pPNhzRK8dwAM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2af2f083-8df1-42e6-879f-b0b6d5e15228",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jh3Ts9MPbPWXZj2c2BjdZv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6597,
      "cache_read_input_tokens": 38865,
      "output_tokens": 1496,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6597
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1496,
          "cache_read_input_tokens": 38865,
          "cache_creation_input_tokens": 6597,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6597,
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

_source line 41 · 2026-05-24T04:30:04.862Z_

<details><summary>↩ Tool result · `toolu_01BpDi2BMbvkMMtkmeSX6fx4`</summary>

```text
=== SPECIAL EXPERIMENTS ===

--- exp_gemma2b_depth ---
  Status: DONE
  Conclusion: negative
  Metrics: {
  "k_star": 1,
  "pairwise_auc": {
    "0v1": 0.9534,
    "1v2": 0.5981,
    "2v3": 0.5342,
    "3v4": 0.503,
    "4v5": 0.5026
  },
  "pairwise_auc_std": {
    "0v1": 0.003,
    "1v2": 0.008,
    "2v3": 0.013,
    "3v4": 0.003,
    "4v5": 0.013
  },
  "bootstrap_ci_1v2": {
    "ci_lower": 0.5882,
    "ci_upper": 0.6076
  },
  "jsd": {
    "0v1": 0.09882,
    "1v2": 0.008852,
    "2v3": 0.004904,
    "3v4": 0.003742,
    "4v5": 0.003167
  },
  "ordinal_mae": 1.3152,
  "ordinal_accuracy": 0.3321,
  "note": "K*=1, NOT borderline K*=2. 1v2 AUC=0.5981 < theta=0.60. CI upper=0.6076 crosses theta but point estimate below."
}

--- exp_003_decoding_ablation ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "K_star": 2,
  "K_star_robust": true,
  "bootstrap_ci": {
    "config1_greedy": {
      "0v1": {
        "auc": 0.9796,
        "ci": [
          0.9772,
          0.982
        ],
        "perm_p": 0
      },
      "1v2": {
        "auc": 0.6892,
        "ci": [
          0.6802,
          0.6982
        ],
        "perm_p": 0
      },
      "2v3": {
        "auc": 0.5612,
        "ci": [
          0.5517,
          0.5705
        ],
        "perm_p": 0
      },
      "3v4": {
        "auc": 0.5405,
        "ci": [
          0.5308,
          0.5502
        ],
        "perm_p": 0
      },
      "4v5": {
        "auc": 0.5137,
        "ci": [
          0.5033,
          0.5238
        ],
        "perm_p": 0.0082
      }
    },
    "config2_nuc09": {
      "0v1": {
        "auc": 0.9945...
  Notes: Server alias 变更 autodl-4090d → westc-26893 导致 cron 误标 failed。实际实验一直正常运行。Config 1 (greedy, K*=2), Config 2 (nuc p=0.9/T=1.0, K*=2), Config 3 (nuc p=0.95/T=0.7, K*=2) 已完成。Config 4 (nuc p=0.95/T=1.2) 运行中。深度分析: 1v2 AUC Δ<0.003 across configs, D016 universality confirmed (all 7 configs > θ=0.60), θ-sensi

--- exp_004_7b_crossscale ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "k_star": 2,
  "pairwise_auc": {
    "0v1": 0.9644,
    "1v2": 0.6178,
    "2v3": 0.546,
    "3v4": 0.5225,
    "4v5": 0.5091
  },
  "pairwise_auc_std": {
    "0v1": 0.0034,
    "1v2": 0.0081,
    "2v3": 0.0028,
    "3v4": 0.0113,
    "4v5": 0.0052
  },
  "bootstrap_ci": {
    "0v1": {
      "auc": 0.9638,
      "ci_lower": 0.9607,
      "ci_upper": 0.9665,
      "perm_p": 0.0001
    },
    "1v2": {
      "auc": 0.6168,
      "ci_lower": 0.6079,
      "ci_upper": 0.6261,
      "perm_p": 0.0001
    },
    "2v3": {
      "auc": 0.5492,
      "ci_lower": 0.5388,
      "ci_upper": 0.5594,
      "perm_p": 0.0001
    },
    "3v4": {
      "auc": 0.5276,
      "ci_lower": 0.517,
      "ci_upper": 0.5375,
      "perm_p": 0.0001
    },
    "4v5": {
      "auc": 0.5085,
      "ci_lower": 0.4988,...
  Notes: 初始运行因进程死亡 5 次被 cron 标记 failed（原 log: exp004_run.log 无 W&B sentinel）。诊断 Worker 发现数据生成已完成，重跑 feature extraction + classification（exp004_resume_feat.sh）后成功。K*=2 在 7B scale 下确认成立。0v1 AUC=0.964 低于所有 1.5B 模型（>0.99），符合预期：更大模型生成更 human-like 文本。1v2=0.618 仍 >θ=0.60。FR-4 Warning resolved。

--- exp_008_retrain_chain ---
  Status: PREPARING
  Conclusion: killed

--- exp_021_length_ablation ---
  Status: DONE
  Conclusion: success
  Metrics: {
  "128tok": {
    "K_star": 2,
    "1v2_auc": 0.6219
  },
  "256tok": {
    "K_star": 2,
    "1v2_auc": 0.6282
  },
  "512tok": {
    "K_star": 2,
    "1v2_auc": 0.6073
  },
  "all_K_star_2": true,
  "bootstrap_ci": {
    "512tok_1v2": {
      "auc": 0.6073,
      "ci_lower": 0.5979,
      "ci_upper": 0.6166,
      "perm_p": 0.0001,
      "verdict": "BORDERLINE"
    }
  }
}
  Notes: 2026-05-16 retry#2: 用本地 C4 数据修复。数据源=/root/autodl-tmp/gen-depth-contamination/data_exp016_qwen_base/depth_0.jsonl (5000行)，复制到 data/exp_021_length_{128,256,512}/。设置 HF_DATASETS_OFFLINE=1 + TRANSFORMERS_OFFLINE=1 阻断 HF 网络调用，prepare_seed_data 检测到本地文件自动跳过 streaming。PID 20982, tmux session exp_021_length_

--- exp_023_domain_ablation ---
  Status: DONE
  Conclusion: success
  Metrics: {
  "K_star": 2,
  "1v2_auc": 0.6193,
  "2v3_auc": 0.5498,
  "all_folds_above_060": true,
  "top_feature": "freq_entropy",
  "ordinal_accuracy": 0.377
}

--- exp_010_ordinal_baseline ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "qwen_rewrite": {
    "obd_lgbm": {
      "accuracy": 0.4229,
      "mae": 0.9836,
      "tau_b": 0.5518,
      "mean_pw_auc": 0.6214
    },
    "multiclass_lgbm": {
      "accuracy": 0.4182,
      "mae": 1.0163,
      "tau_b": 0.5367,
      "mean_pw_auc": 0.6246
    },
    "ordinal_logreg": {
      "accuracy": 0.3636,
      "mae": 0.9105,
      "tau_b": 0.563,
      "mean_pw_auc": 0.5022
    }
  },
  "pythia": {
    "obd_lgbm": {
      "accuracy": 0.3856,
      "mae": 1.1072,
      "tau_b": 0.4745,
      "mean_pw_auc": 0.6055
    },
    "multiclass_lgbm": {
      "accuracy": 0.3832,
      "mae": 1.1399,
      "tau_b": 0.4622,
      "mean_pw_auc": 0.6062
    },
    "ordinal_logreg": {
      "accuracy": 0.3179,
      "mae": 1.022,
      "tau_b": 0.49,
      "mean_pw_auc": 0.4767
    }
 ...
  Notes: Ordinal methods beat multiclass LightGBM on MAE across all 3 datasets. Best MAE consistently from mord LogisticAT, not OBD-LightGBM. However, ordinal_logreg has worst pairwise AUC — it reduces MAE by collapsing predictions toward the center, not by better discrimination.

--- exp_015_neural_probe ---
  Status: DONE
  Conclusion: success
  Metrics: {
  "k_star_qwen": 3,
  "k_star_pythia": 2,
  "k_star_olmo": 1,
  "qwen_pairwise_auc": {
    "0v1": 0.988,
    "1v2": 0.702,
    "2v3": 0.616,
    "3v4": 0.59,
    "4v5": 0.566
  },
  "pythia_pairwise_auc": {
    "0v1": 0.966,
    "1v2": 0.676,
    "2v3": 0.596,
    "3v4": 0.555,
    "4v5": 0.532
  },
  "olmo_pairwise_auc": {
    "0v1": 0.9773,
    "1v2": 0.5054,
    "2v3": 0.5056,
    "3v4": 0.5032,
    "4v5": 0.4999
  },
  "olmo_rerun_source": "exp015_olmo_rerun/neural_probe_results.json",
  "notes": "OLMo values updated from rerun (self-probe). Original cross-model probe had K*=2 (1v2=0.657) but was superseded by self-probe rerun (K*=1, 1v2=0.5054). Paper Table 3 correctly uses rerun values."
}
  Notes: v4 completed successfully. 3 models: Pythia K*_neural=2, OLMo K*_neural=2, Qwen-cont K*_neural=3. Neural probe improves 2v3 AUC across all models (Pythia +0.044, OLMo +0.039, Qwen +0.055) but only Qwen-cont self-scorer crosses θ=0.60. EXIT_CODE=129 (SIGHUP after completion) did not affect results.

--- exp_016_base_vs_instruct ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "k_star": 2,
  "pairwise_auc": {
    "0v1": 0.987,
    "1v2": 0.6262,
    "2v3": 0.5496,
    "3v4": 0.5294,
    "4v5": 0.5182
  },
  "pairwise_auc_std": {
    "0v1": 0.0015,
    "1v2": 0.0152,
    "2v3": 0.0067,
    "3v4": 0.0132,
    "4v5": 0.0139
  },
  "pairwise_jsd": {
    "0v1": 0.163726,
    "1v2": 0.01081,
    "2v3": 0.005311,
    "3v4": 0.003942,
    "4v5": 0.003522
  },
  "ordinal_mae": 1.1691,
  "ordinal_accuracy": 0.3719,
  "top_features": [
    "freq_entropy",
    "surp_std",
    "surp_d1_skew",
    "surp_d1_mean",
    "surp_mean"
  ],
  "n_samples": 30000,
  "bootstrap_ci": {
    "0v1": {
      "auc": 0.987,
      "ci_lower": 0.9853,
      "ci_upper": 0.9885,
      "perm_p": 0.0001
    },
    "1v2": {
      "auc": 0.626,
      "ci_lower": 0.6168,
      "ci_upper": 0.6353,
...
  Notes: 2026-05-16: Resumed on cqa1-22115 (migrated from westc-26893). Depth 0-3 complete, generating depth 4-5. PID=3442 on cuda:0.

--- exp_017_qwen_continuation ---
  Status: DONE
  Conclusion: success
  Metrics: {
  "k_star": 2,
  "pairwise_auc": {
    "0v1": 0.9972,
    "1v2": 0.6114,
    "2v3": 0.5609,
    "3v4": 0.5408,
    "4v5": 0.5139
  },
  "pairwise_jsd": {
    "0v1": 0.28627,
    "1v2": 0.005107,
    "2v3": 0.003603,
    "3v4": 0.003395,
    "4v5": 0.003085
  },
  "ordinal_mae": 1.1547,
  "ordinal_accuracy": 0.3819,
  "top3_features": [
    "freq_entropy",
    "surp_mean",
    "surp_std"
  ]
}
  Notes: dry-run passed 2026-05-13: model OK (2.9G safetensors), env OK (torch=2.10.0+cu128, transformers=4.57.6), dirs auto-create. Submit command prepared. 等 exp-002 完成后立即提交。

--- exp_014_naturalistic ---
  Status: DONE
  Conclusion: success
  Metrics: {
  "binary_auc": 0.9919,
  "cc_depth0_ratio": 0.89,
  "freq_entropy_rho": -0.78,
  "ttr_rho": 0.17,
  "note": "TTR rho=+0.17 contradicts hypothesis (expected negative). Paper should only report freq_entropy and CC classification, not TTR (or explicitly flag anomalous direction)."
}

--- exp_012_binary_confidence ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "n_samples": 500,
  "generators": [
    "qwen-rewrite",
    "pythia-1.4b",
    "olmo-1b",
    "qwen-cont"
  ],
  "6class_accuracy": {
    "qwen-rewrite": 0.1987,
    "pythia-1.4b": 0.1303,
    "olmo-1b": 0.127,
    "qwen-cont": 0.1833,
    "random_baseline": 0.1667
  },
  "spearman_rho": {
    "qwen-rewrite": {
      "log_ppl_ref": -0.1233,
      "log_ppl_obs": 0.0815,
      "ppl_ratio": 0.1185
    },
    "pythia-1.4b": {
      "log_ppl_ref": -0.2972,
      "log_ppl_obs": -0.4529,
      "ppl_ratio": -0.392
    },
    "olmo-1b": {
      "log_ppl_ref": -0.378,
      "log_ppl_obs": -0.4614,
      "ppl_ratio": -0.4068
    },
    "qwen-cont": {
      "log_ppl_ref": -0.3887,
      "log_ppl_obs": -0.162,
      "ppl_ratio": -0.058
    }
  },
  "binary_detector_kstar": 1,
  "obd_kstar": 2,
  "a...
  Notes: N=500全量运行。Binary confidence与depth的Spearman ρ弱到中等(|ρ|=0.06-0.46)，6-class accuracy全部≤random baseline。关键发现：0v1 pairwise AUC极高(0.99+)但deeper pairs塌缩到~0.5，证明binary detector只捕捉human/AI边界，无法区分generational depth。Hypothesis验证成功。可视化已生成(exp012_confidence_vs_depth.pdf)。

--- exp_011_llm_zeroshot ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "gpt55_5class_acc": 0.332,
  "gpt55_mae": 1.102,
  "gpt55_spearman": 0.383,
  "gpt55_binary_acc": 0.878,
  "claude_5class_acc": 0.331,
  "claude_mae": 1.15,
  "claude_spearman": 0.416,
  "claude_binary_acc": 0.882,
  "odb_baseline_5class_acc": 0.386,
  "odb_baseline_mae": 1.107,
  "gpt55_per_depth_acc": {
    "depth_0": 0.77,
    "depth_1": 0.19,
    "depth_2": 0.38,
    "depth_3": 0.24,
    "depth_4": 0.08
  },
  "claude_per_depth_acc": {
    "depth_0": 0.69,
    "depth_1": 0.21,
    "depth_2": 0.28,
    "depth_3": 0.101,
    "depth_4": 0.37
  },
  "n_samples_per_model": 500,
  "key_finding": "Both frontier LLMs (GPT-5.5, Claude Opus 4.6) perform WORSE than OBD-LightGBM on 5-class depth estimation (~33% vs 38.6% acc). Binary human/AI detection is high (~88%) but fine-grained depth dis...
  Notes: GPT-5.5: 500条, 0 parse failures. Claude Opus 4.6: 500条, 1 parse failure. 两个 frontier LLM 5-class accuracy (~33%) 均低于 OBD-LightGBM (38.6%)。Binary human/AI detection 高 (~88%) 但 fine-grained depth 判断失败。Claude proxy 需用 model ID 'claude-opus-4-6' (无 anthropic/ 前缀)。

--- exp_B_14d_ablation ---
  Status: DONE
  Conclusion: success
  Metrics: {
  "result": "K*=2 stable across all 4 models after removing self_BLEU (14D)",
  "key_finding": "self_BLEU removal does not change K* boundary. FR-3 resolved."
}

--- exp_A_alt_scorer ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "pythia_qwen_rw": {
    "k_star": 2,
    "auc_0v1": 0.9923,
    "auc_1v2": 0.7012,
    "auc_2v3": 0.587,
    "mae": 1.006,
    "accuracy": 0.417,
    "spearman_rho_vs_baseline": 0.906
  },
  "pythia_qwen_cont": {
    "k_star": 1,
    "auc_0v1": 0.99,
    "auc_1v2": 0.5923,
    "auc_2v3": null,
    "mae": 1.216,
    "accuracy": 0.371,
    "spearman_rho_vs_baseline": 0.942
  },
  "olmo_qwen_rw": {
    "k_star": 2,
    "auc_0v1": 0.9918,
    "auc_1v2": 0.6947,
    "auc_2v3": null,
    "mae": 1.016,
    "accuracy": 0.413,
    "spearman_rho_vs_baseline": 0.92
  },
  "olmo_qwen_cont": {
    "k_star": 1,
    "auc_0v1": 0.989,
    "auc_1v2": 0.5858,
    "auc_2v3": null,
    "mae": 1.229,
    "accuracy": 0.368,
    "spearman_rho_vs_baseline": 0.902
  },
  "key_finding": "K* splits by generator ...

--- exp_D_obd_n500 ---
  Status: DONE
  Conclusion: success
  Metrics: {
  "obd_accuracy_final": 0.38,
  "obd_ci": [
    0.34,
    0.422
  ],
  "mcnemar_vs_gpt55_p": 0.0809,
  "mcnemar_vs_claude_p": 0.0693,
  "mcnemar_significant": false,
  "multi_seed_std": 0,
  "per_depth": {
    "d0": 0.96,
    "d1": 0.39,
    "d2": 0.14,
    "d3": 0.19,
    "d4": 0.22
  },
  "prob_merge_accuracy": 0.444,
  "prob_merge_d4_bias": 0.8,
  "note": "v2 logic (6-class argmax, no capping/merge) + seed=42. McNemar not significant \u2014 supports discussion.tex narrative"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2af2f083-8df1-42e6-879f-b0b6d5e15228",
  "isSidechain": true,
  "promptId": "7d9f03b2-f13f-4ae8-b207-26c75cd900b2",
  "agentId": "a00d6d05ce2acd01d",
  "type": "user",
  "uuid": "bc77e97f-6345-4b83-b0c6-01204727633a",
  "sourceToolAssistantUUID": "2af2f083-8df1-42e6-879f-b0b6d5e15228",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-24T04:30:20.807Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Pw93NQWha1DZyWdDtHdbQE`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2/tool-results/mcp-agent-ml-research-read_registry-1779596868416.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# arXiv domain experiments\nkeys = [k for k in exps if 'arxiv' in k.lower() or 'domain' in k.lower() or 'wiki' in k.lower() or 'code' in k.lower() or 'multi_source' in k.lower()]\n# Only show ones with metrics we haven't seen\nalready_shown = {'exp_code_qwen7b','exp_code_mistral7b','exp_code_llama8b','exp_code_qwen1b5_pythia_scorer',\n                 'exp_deberta_code_qwen1b5','exp_deberta_arxiv_qwen1b5','exp_arXiv_mistral7b_crossscorer',\n                 'exp_arXiv_llama8b_crossscorer','exp_arXiv_mistral7b','exp_arXiv_llama8b',\n                 'exp_wiki_mistral7b','exp_wiki_llama8b','exp_023_domain_ablation','exp_014_naturalistic',\n                 'exp_026_arxiv_filtering','exp_deberta_cross_transfer_wiki','exp_code_qwen1b5'}\nfor k in sorted(keys):\n    if k in already_shown:\n        continue\n    e = exps[k]\n    if 'metrics' not in e:\n        continue\n    print(f'\\n--- {k} ---')\n    print(f'  Status: {e.get(\\\"status\\\")}')\n    print(f'  Conclusion: {e.get(\\\"conclusion\\\", \\\"N/A\\\")}')\n    m = e['metrics']\n    mstr = json.dumps(m, indent=2)\n    if len(mstr) > 500:\n        print(f'  Metrics (truncated): {mstr[:500]}...')\n    else:\n        print(f'  Metrics: {mstr}')\n\" 2>&1 | head -600",
  "description": "Extract remaining arXiv/wiki/code/domain experiments not yet shown"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc77e97f-6345-4b83-b0c6-01204727633a",
  "isSidechain": true,
  "agentId": "a00d6d05ce2acd01d",
  "requestId": "req_011CbLmKdknJAnEpqEJAhfgu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "67c679ab-f810-4162-ab09-31e4c7f68fa0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GJxoBAMWanKEBVywnx4Psa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10189,
      "cache_read_input_tokens": 45462,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10189,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 43 · 2026-05-24T04:30:20.908Z_

<details><summary>↩ Tool result · `toolu_01Pw93NQWha1DZyWdDtHdbQE`</summary>

```text
--- exp_024_arxiv_domain ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "K_star": 3,
  "pairwise_auc": {
    "0v1": 0.9946,
    "1v2": 0.858,
    "2v3": 0.6427,
    "3v4": 0.5437,
    "4v5": 0.5294
  },
  "bootstrap_ci": {
    "0v1": {
      "auc": 0.9946,
      "ci_lower": 0.9929,
      "ci_upper": 0.9961,
      "perm_p": 0.0001
    },
    "1v2": {
      "auc": 0.858,
      "ci_lower": 0.848,
      "ci_upper": 0.8679,
      "perm_p": 0.0001
    },
    "2v3": {
      "auc": 0.6427,
      "ci_lower": 0.6275,
      "ci_upper": 0.6575,
      "perm_p": 0.0001
    },...

--- exp_025_pythia_arxiv ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "k_star": 3,
  "pairwise_auc": {
    "0v1": 0.9877,
    "1v2": 0.8047,
    "2v3": 0.6545,
    "3v4": 0.5507,
    "4v5": 0.5287
  },
  "pairwise_jsd": {
    "0v1": 0.171338,
    "1v2": 0.057344,
    "2v3": 0.019524,
    "3v4": 0.009917,
    "4v5": 0.008846
  },
  "bootstrap_ci": {
    "0v1": {
      "auc": 0.9876,
      "ci_lower": 0.9851,
      "ci_upper": 0.99,
      "perm_p": 0.0001
    },
    "1v2": {
      "auc": 0.8047,
      "ci_lower": 0.7934,
      "ci_upper": 0.8162,
      "perm_p":...

--- exp_7b_scorer_arxiv ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "pythia_arxiv_qwen1b5": {
    "k_star": 3,
    "0v1": 0.9872,
    "1v2": 0.7938,
    "2v3": 0.6544
  },
  "olmo_arxiv_qwen1b5": {
    "k_star": 1,
    "0v1": 0.9954,
    "1v2": 0.5182,
    "2v3": 0.4956
  },
  "pythia_arxiv_qwen7b": {
    "k_star": 3,
    "0v1": 0.9844,
    "1v2": 0.7987,
    "2v3": 0.6551
  },
  "olmo_arxiv_qwen7b": {
    "k_star": 1,
    "0v1": 0.9941,
    "1v2": 0.5089,
    "2v3": 0.492
  },
  "summary": "7B scorer and 1.5B scorer yield identical K* on arXiv: Pythia=3, OL...

--- exp_arXiv_olmo ---
  Status: DONE
  Conclusion: negative
  Metrics: {
  "K_star": 1,
  "auc_0v1": 0.9958,
  "auc_1v2": 0.5034,
  "auc_2v3": 0.5069,
  "auc_3v4": 0.5021,
  "auc_4v5": 0.5037,
  "jsd_0v1": 0.329,
  "ordinal_acc": 0.33
}

--- exp_arXiv_qwen1b5_crossscorer ---
  Status: DONE
  Conclusion: success
  Metrics: {
  "k_star": 3,
  "auc_0v1": 0.9748,
  "auc_1v2": 0.8105,
  "auc_2v3": 0.6317,
  "auc_3v4": 0.5437,
  "auc_4v5": 0.5294,
  "jsd_0v1": 0.154297,
  "jsd_1v2": 0.066782,
  "jsd_2v3": 0.019268,
  "jsd_3v4": 0.008867,
  "jsd_4v5": 0.006991,
  "ordinal_mae": 0.9017,
  "ordinal_accuracy": 0.4402
}

--- exp_arXiv_qwen7b ---
  Status: DONE
  Conclusion: success
  Metrics: {
  "k_star": 3,
  "pairwise_auc": {
    "0v1": 0.983,
    "1v2": 0.835,
    "2v3": 0.626,
    "3v4": 0.544,
    "4v5": 0.513
  },
  "pairwise_jsd": {
    "0v1": 0.1656,
    "1v2": 0.0668,
    "2v3": 0.0156,
    "3v4": 0.0089,
    "4v5": 0.0061
  },
  "ordinal_mae": 0.9,
  "ordinal_accuracy": 0.446
}

--- exp_arXiv_qwen7b_crossscorer ---
  Status: DONE
  Conclusion: negative
  Metrics: {
  "k_star": 2,
  "auc_0v1": 0.9575,
  "auc_1v2": 0.8171,
  "auc_2v3": 0.5989,
  "auc_3v4": 0.5417,
  "auc_4v5": 0.5192,
  "jsd_0v1": 0.137085,
  "jsd_1v2": 0.059688,
  "jsd_2v3": 0.013508,
  "jsd_3v4": 0.009125,
  "jsd_4v5": 0.006738,
  "ordinal_mae": 0.9617,
  "ordinal_accuracy": 0.4255
}

--- exp_code_multi_source ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "k_star": 2,
  "generators": [
    "qwen7b",
    "llama8b",
    "mistral7b"
  ],
  "unified_scorer": "qwen2.5-1.5b",
  "vocab_only_no_label": {
    "0v1": 0.7891,
    "1v2": 0.6353,
    "2v3": 0.5121,
    "kstar": 2
  },
  "vocab_only_with_label": {
    "0v1": 0.79,
    "1v2": 0.644,
    "2v3": 0.5118,
    "kstar": 2
  },
  "unified_no_label": {
    "0v1": 0.9123,
    "1v2": 0.6702,
    "2v3": 0.5013,
    "kstar": 2
  },
  "unified_with_label": {
    "0v1": 0.9123,
    "1v2": 0.6803,
    "2v...

--- exp_code_pythia1b4 ---
  Status: DONE
  Conclusion: negative
  Metrics (truncated): {
  "k_star": 1,
  "theta": 0.6,
  "pairwise_auc": {
    "0v1": {
      "mean": 0.9592,
      "std": 0.0036,
      "folds": [
        0.9576,
        0.9576,
        0.9657,
        0.96,
        0.9552
      ]
    },
    "1v2": {
      "mean": 0.5983,
      "std": 0.005,
      "folds": [
        0.601,
        0.5884,
        0.6,
        0.5997,
        0.6024
      ]
    },
    "2v3": {
      "mean": 0.5215,
      "std": 0.0128,
      "folds": [
        0.5236,
        0.5124,
        0.5311,...

--- exp_multi_source_arxiv ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "domain": "arxiv",
  "generators": [
    "qwen1b5",
    "pythia1b4",
    "llama8b"
  ],
  "unified_scorer": "qwen2.5-1.5b",
  "docs_per_generator": 1000,
  "vocab_only_no_label_0v1": 0.9431,
  "vocab_only_no_label_1v2": 0.6922,
  "vocab_only_no_label_2v3": 0.589,
  "vocab_only_no_label_kstar": 2,
  "vocab_only_with_label_0v1": 0.9436,
  "vocab_only_with_label_1v2": 0.702,
  "vocab_only_with_label_2v3": 0.5883,
  "vocab_only_with_label_kstar": 2,
  "unified_no_label_0v1": 0.9899,
  "unified_n...

--- exp_multi_source_detection ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "v2_generators": [
    "qwen1b5",
    "pythia1b4",
    "llama8b"
  ],
  "v2_kstar_no_label": 2,
  "v2_kstar_with_label": 2,
  "v2_0v1_auc_no_label": 0.968,
  "v2_0v1_auc_with_label": 0.9785,
  "v2_1v2_auc_no_label": 0.7144,
  "v2_1v2_auc_with_label": 0.7251,
  "v2_2v3_auc_no_label": 0.5321,
  "v2_2v3_auc_with_label": 0.5362,
  "vocab_only_v1_0v1": 0.8675,
  "vocab_only_v1_1v2": 0.676,
  "vocab_only_v1_2v3": 0.4938,
  "vocab_only_v1_kstar": 2,
  "vocab_only_v2_0v1": 0.8296,
  "vocab_only_v2_1...

--- exp_wiki_multi_source ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "k_star": 1,
  "generators": [
    "qwen1b5",
    "llama8b",
    "mistral7b"
  ],
  "docs_per_generator": 1000,
  "total_rows": 18000,
  "unified_scorer": "qwen2.5-1.5b",
  "vocab_only_no_label": {
    "0v1": 0.7616,
    "1v2": 0.5434,
    "2v3": 0.517,
    "kstar": 1
  },
  "vocab_only_with_label": {
    "0v1": 0.7779,
    "1v2": 0.552,
    "2v3": 0.5248,
    "kstar": 1
  },
  "unified_no_label": {
    "0v1": 0.9603,
    "1v2": 0.5685,
    "2v3": 0.519,
    "kstar": 1
  },
  "unified_with_l...

--- exp_wiki_olmo_v2 ---
  Status: DONE
  Conclusion: negative
  Metrics: {
  "K_star": 1,
  "auc_0v1": 0.9932,
  "auc_1v2": 0.4986,
  "auc_2v3": 0.5012,
  "auc_3v4": 0.5057,
  "auc_4v5": 0.5009,
  "jsd_0v1": 0.1688,
  "ordinal_acc": 0.3227
}

--- exp_wiki_pythia_v2 ---
  Status: DONE
  Conclusion: negative
  Metrics: {
  "K_star": 1,
  "auc_0v1": 0.975,
  "auc_1v2": 0.5846,
  "auc_2v3": 0.5445,
  "auc_3v4": 0.5205,
  "auc_4v5": 0.5168,
  "jsd_0v1": 0.080065,
  "jsd_1v2": 0.007773,
  "ordinal_acc": 0.3503
}

--- exp_wiki_qwen7b ---
  Status: DONE
  Conclusion: success
  Metrics: {
  "K_star": 2,
  "auc_0v1": 0.9673,
  "auc_1v2": 0.6108,
  "auc_2v3": 0.5562,
  "auc_3v4": 0.5297,
  "auc_4v5": 0.529,
  "jsd_0v1": 0.083514,
  "jsd_1v2": 0.010991,
  "jsd_2v3": 0.00555,
  "jsd_3v4": 0.004611,
  "jsd_4v5": 0.003894,
  "ordinal_mae": 1.2501,
  "ordinal_accuracy": 0.3532
}

--- exp_wiki_scorer_confound ---
  Status: DONE
  Conclusion: negative
  Metrics: {
  "k_star": 1,
  "confound_verdict": "confirmed",
  "auc_0v1": 0.9404,
  "auc_1v2": 0.587,
  "auc_2v3": 0.5456,
  "auc_3v4": 0.525,
  "auc_4v5": 0.5172,
  "critical_delta_1v2": -0.0238
}

--- exp_wiki_scorer_confound_1b5 ---
  Status: DONE
  Conclusion: negative
  Metrics: {
  "k_star": 1,
  "confound_verdict": "confirmed",
  "auc_0v1": 0.9729,
  "auc_1v2": 0.5994,
  "auc_2v3": 0.533,
  "auc_3v4": 0.5214,
  "auc_4v5": 0.5068,
  "jsd_0v1": 0.0886,
  "ordinal_mae": 1.2995,
  "ordinal_accuracy": 0.3466
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67c679ab-f810-4162-ab09-31e4c7f68fa0",
  "isSidechain": true,
  "promptId": "7d9f03b2-f13f-4ae8-b207-26c75cd900b2",
  "agentId": "a00d6d05ce2acd01d",
  "type": "user",
  "uuid": "d8b0ff6f-9588-42d1-92e3-e598d2c6104e",
  "sourceToolAssistantUUID": "67c679ab-f810-4162-ab09-31e4c7f68fa0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-24T04:30:35.599Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01PqG3Xd7MREzix2N6cbd4mQ`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2/tool-results/mcp-agent-ml-research-read_registry-1779596868416.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Remaining experiments with metrics that haven't been shown\nalready_shown = {\n    'runtime_benchmark','exp_015_neural_probe','exp_gemma2b_depth','exp_002_olmo_depth',\n    'exp_001_pythia_depth','exp_qwen_cont_10k','exp_020_pythia_decoding',\n    'exp_deberta_code_qwen1b5','exp_cross_transfer_llama8b_to_qwen7b_v2',\n    'exp_deberta_arxiv_qwen1b5','exp_cross_transfer_qwen7b_to_llama8b',\n    'exp_deberta_c4_1b5_qwen_cont','exp_code_qwen7b','exp_code_qwen1b5_pythia_scorer',\n    'exp_qwen_retrain_depth7','exp_qwen_retrain_chain','exp_code_qwen1b5',\n    'exp_llama8b_10k','exp_cross_transfer_llama8b_to_qwen7b',\n    'exp_code_mistral7b','exp_code_llama8b',\n    'exp_arXiv_mistral7b_crossscorer','exp_arXiv_llama8b_crossscorer',\n    'exp_wiki_mistral7b','exp_wiki_llama8b','exp_arXiv_mistral7b','exp_arXiv_llama8b',\n    'exp_018_llama8b_depth','exp_019b_mistral_cross_scorer','exp_019_mistral7b_depth',\n    'exp_009_dose_10pct_v3','exp_009_dose_30pct_v3','exp_009_dose_50pct_v3',\n    'exp_009_dose_response','exp_contamination_rate_sweep',\n    'exp_007_bootstrap_ci','exp_027_retrain_bootstrap','exp_bootstrap_10k',\n    'exp_changepoint_kstar','exp_kstar_theta',\n    'exp_013_cross_transfer','exp_deberta_cross_transfer_wiki',\n    'exp_C_permutation_10k','exp_E_paired_stats',\n    'exp_005_degradation','exp_006_graduated_filtering',\n    'exp_025_pythia_filtering','exp_026_arxiv_filtering',\n    'exp_deberta_filtering_comparison','exp_expanded_downstream_eval',\n    'exp_003_decoding_ablation','exp_004_7b_crossscale',\n    'exp_021_length_ablation','exp_023_domain_ablation',\n    'exp_010_ordinal_baseline','exp_016_base_vs_instruct',\n    'exp_017_qwen_continuation','exp_014_naturalistic',\n    'exp_012_binary_confidence','exp_011_llm_zeroshot',\n    'exp_B_14d_ablation','exp_A_alt_scorer','exp_D_obd_n500'\n}\nremaining = [k for k in exps if k not in already_shown and 'metrics' in exps[k]]\nprint(f'Remaining experiments with metrics: {len(remaining)}')\nfor k in sorted(remaining):\n    e = exps[k]\n    print(f'\\n--- {k} ---')\n    print(f'  Status: {e.get(\\\"status\\\")}')\n    print(f'  Conclusion: {e.get(\\\"conclusion\\\", \\\"N/A\\\")}')\n    m = e['metrics']\n    mstr = json.dumps(m, indent=2)\n    if len(mstr) > 500:\n        print(f'  Metrics (truncated): {mstr[:500]}...')\n    else:\n        print(f'  Metrics: {mstr}')\n\" 2>&1 | head -1200",
  "description": "Extract all remaining experiments with metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8b0ff6f-9588-42d1-92e3-e598d2c6104e",
  "isSidechain": true,
  "agentId": "a00d6d05ce2acd01d",
  "requestId": "req_011CbLmKdknJAnEpqEJAhfgu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b55fcd58-3f83-49a3-ba58-80653231ff8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GJxoBAMWanKEBVywnx4Psa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10189,
      "cache_read_input_tokens": 45462,
      "output_tokens": 1855,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10189
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1855,
          "cache_read_input_tokens": 45462,
          "cache_creation_input_tokens": 10189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10189,
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

_source line 45 · 2026-05-24T04:30:35.714Z_

<details><summary>↩ Tool result · `toolu_01PqG3Xd7MREzix2N6cbd4mQ`</summary>

```text
Remaining experiments with metrics: 45

--- exp-014 ---
  Status: DONE
  Conclusion: success
  Metrics: {
  "superseded_by": "exp_014_naturalistic",
  "note": "Stale duplicate. All metrics and results are in exp_014_naturalistic."
}

--- exp_008_retrain_chain_v2 ---
  Status: DONE
  Conclusion: success
  Metrics: {
  "k_star": ">=4",
  "pairwise_auc": {
    "0v1": 0.9847,
    "1v2": 0.9484,
    "2v3": 0.8888,
    "3v4": 0.7982
  },
  "pairwise_jsd": {
    "0v1": 0.17,
    "1v2": 0.12,
    "2v3": 0.064,
    "3v4": 0.04
  },
  "key_finding": "Retrain-chain K*>=4, all pairs AUC>>0.60. LoRA adaptation artifacts make generations highly distinguishable. Prompt-chain K*=2 is text-intrinsic boundary."
}

--- exp_022_cross_scorer_matrix ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "total_combos": 12,
  "completed": 12,
  "K_star_distribution": {
    "K2": 11,
    "K1": 1
  },
  "matrix": {
    "pythia_greedy\u00d7olmo": {
      "K_star": 2,
      "1v2": 0.8811
    },
    "pythia_greedy\u00d7pythia": {
      "K_star": 2,
      "1v2": 0.8838
    },
    "pythia_greedy\u00d7qwen_base": {
      "K_star": 2,
      "1v2": 0.8814
    },
    "pythia_greedy\u00d7qwen_instruct": {
      "K_star": 2,
      "1v2": 0.8818
    },
    "qwen_base\u00d7olmo": {
      "K_star": 2,
     ...

--- exp_024_arxiv_domain ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "K_star": 3,
  "pairwise_auc": {
    "0v1": 0.9946,
    "1v2": 0.858,
    "2v3": 0.6427,
    "3v4": 0.5437,
    "4v5": 0.5294
  },
  "bootstrap_ci": {
    "0v1": {
      "auc": 0.9946,
      "ci_lower": 0.9929,
      "ci_upper": 0.9961,
      "perm_p": 0.0001
    },
    "1v2": {
      "auc": 0.858,
      "ci_lower": 0.848,
      "ci_upper": 0.8679,
      "perm_p": 0.0001
    },
    "2v3": {
      "auc": 0.6427,
      "ci_lower": 0.6275,
      "ci_upper": 0.6575,
      "perm_p": 0.0001
    },...

--- exp_025_pythia_arxiv ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "k_star": 3,
  "pairwise_auc": {
    "0v1": 0.9877,
    "1v2": 0.8047,
    "2v3": 0.6545,
    "3v4": 0.5507,
    "4v5": 0.5287
  },
  "pairwise_jsd": {
    "0v1": 0.171338,
    "1v2": 0.057344,
    "2v3": 0.019524,
    "3v4": 0.009917,
    "4v5": 0.008846
  },
  "bootstrap_ci": {
    "0v1": {
      "auc": 0.9876,
      "ci_lower": 0.9851,
      "ci_upper": 0.99,
      "perm_p": 0.0001
    },
    "1v2": {
      "auc": 0.8047,
      "ci_lower": 0.7934,
      "ci_upper": 0.8162,
      "perm_p":...

--- exp_026_feature_stability ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "data_source": "exp_016_qwen_base (prompt-chain, K*=2)",
  "results": {
    "15D": {
      "num_tested": 1,
      "num_kstar_2": 1,
      "min_1v2_auc": 0.6262,
      "mean_1v2_auc": 0.6262
    },
    "10D": {
      "num_tested": 5,
      "num_kstar_2": 5,
      "min_1v2_auc": 0.6153,
      "mean_1v2_auc": 0.6191
    },
    "8D": {
      "num_tested": 5,
      "num_kstar_2": 5,
      "min_1v2_auc": 0.6056,
      "mean_1v2_auc": 0.6159
    },
    "5D": {
      "num_tested": 5,
      "num_ksta...

--- exp_026_feature_stability_v2 ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "data_source": "exp_001_pythia prompt-chain (K*=2)",
  "results": {
    "15D": {
      "num_tested": 1,
      "num_pass": 1,
      "min_1v2_auc": 0.6262,
      "mean_1v2_auc": 0.6262
    },
    "10D": {
      "num_tested": 5,
      "num_pass": 5,
      "min_1v2_auc": 0.6153,
      "mean_1v2_auc": 0.6191
    },
    "8D": {
      "num_tested": 5,
      "num_pass": 5,
      "min_1v2_auc": 0.6056,
      "mean_1v2_auc": 0.6159
    },
    "5D": {
      "num_tested": 5,
      "num_pass": 2,
      "...

--- exp_027 ---
  Status: DONE
  Conclusion: success
  Metrics: {
  "kstar_ci": 4,
  "0v1_auc": 0.9847,
  "0v1_ci": [
    0.9828,
    0.9864
  ],
  "0v1_perm_p": 0.0001,
  "1v2_auc": 0.9482,
  "1v2_ci": [
    0.9443,
    0.952
  ],
  "1v2_perm_p": 0.0001,
  "2v3_auc": 0.8885,
  "2v3_ci": [
    0.8829,
    0.894
  ],
  "2v3_perm_p": 0.0001,
  "3v4_auc": 0.7977,
  "3v4_ci": [
    0.7903,
    0.8051
  ],
  "3v4_perm_p": 0.0001,
  "all_ci_lower_above_theta": true
}

--- exp_027_latex_ablation ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "k_star": 3,
  "k_star_preserved": true,
  "pairwise_auc_original": {
    "0v1": 0.9948,
    "1v2": 0.8581,
    "2v3": 0.6436,
    "3v4": 0.544,
    "4v5": 0.5299
  },
  "pairwise_auc_stripped": {
    "0v1": 0.9948,
    "1v2": 0.8297,
    "2v3": 0.6229,
    "3v4": 0.5468,
    "4v5": 0.5476
  },
  "auc_delta": {
    "0v1": 0,
    "1v2": -0.028,
    "2v3": -0.021,
    "3v4": 0.003,
    "4v5": 0.018
  },
  "latex_reduction_by_depth": {
    "depth_0": "0.6%",
    "depth_5": "4.4%"
  },
  "key_fi...

--- exp_028_power_curve ---
  Status: DONE
  Conclusion: success
  Metrics: {
  "min_n_100pct": 2000,
  "n500_auc": 0.5808,
  "n500_rate": 0.2,
  "n1000_auc": 0.5911,
  "n1000_rate": 0.3,
  "n2000_auc": 0.6101,
  "n2000_rate": 1,
  "n3000_auc": 0.6166,
  "n3000_rate": 1,
  "n4000_auc": 0.622,
  "n4000_rate": 1,
  "n5000_auc": 0.6288,
  "n5000_rate": 1
}

--- exp_028_subsampling_power ---
  Status: DONE
  Conclusion: success
  Metrics: {
  "n_1000": {
    "mean_auc": 0.608,
    "std": 0.012,
    "detection_prob": 0.9
  },
  "n_2500": {
    "mean_auc": 0.618,
    "std": 0.006,
    "detection_prob": 1
  },
  "n_5000": {
    "mean_auc": 0.629,
    "std": 0,
    "detection_prob": 1
  },
  "key_finding": "n>=2500 gives 100% reliable K*=2 detection. n=1000 already 90%. Signal is robust, not large-sample artifact."
}

--- exp_14b_c4 ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "k_star": 2,
  "pairwise_auc": {
    "0v1": 0.9598,
    "1v2": 0.621,
    "2v3": 0.5494,
    "3v4": 0.5243,
    "4v5": 0.5154
  },
  "pairwise_jsd": {
    "0v1": 0.1097,
    "1v2": 0.0112,
    "2v3": 0.0062,
    "3v4": 0.0044,
    "4v5": 0.0036
  },
  "bootstrap_ci": {
    "0v1": [
      0.9564,
      0.963
    ],
    "1v2": [
      0.6119,
      0.6304
    ],
    "2v3": [
      0.5392,
      0.5594
    ],
    "3v4": [
      0.514,
      0.5346
    ],
    "4v5": [
      0.5045,
      0.5265
...

--- exp_32b_c4 ---
  Status: DONE
  Conclusion: success
  Metrics: {
  "lgbm_kstar": 2,
  "deberta_kstar": 2,
  "kstar_theta": 0.6,
  "scale": "32B",
  "domain": "C4",
  "n_docs": 5000,
  "max_depth": 5,
  "key_finding": "Qwen2.5-32B C4 K*=2, confirming scale-invariance of K*=2 dominant mode from 1.5B to 32B. Both LightGBM and DeBERTa classifiers agree on K*=2."
}

--- exp_32b_c4_6class ---
  Status: DONE
  Conclusion: success
  Metrics: {
  "config": "exp_32b_c4",
  "kstar": 2,
  "kstar_indexing": "1-indexed",
  "num_classes": 6,
  "pairwise_auc": {
    "0v1": 0.9923,
    "1v2": 0.6945,
    "2v3": 0.5978,
    "3v4": 0.5669,
    "4v5": 0.5426
  },
  "ci_95": {
    "0v1": [
      0.991,
      0.9936
    ],
    "1v2": [
      0.6864,
      0.7026
    ],
    "2v3": [
      0.5898,
      0.6058
    ],
    "3v4": [
      0.559,
      0.5746
    ],
    "4v5": [
      0.5351,
      0.5501
    ]
  },
  "training_time_min": 48.2
}

--- exp_7b_scorer_ablation ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "pythia_c4__qwen1.5b": {
    "k_star": 2,
    "1v2_auc": 0.8928,
    "1v2_ci": [
      0.8865,
      0.8989
    ]
  },
  "olmo_c4__qwen1.5b": {
    "k_star": 1,
    "1v2_auc": 0.4977,
    "1v2_ci": [
      0.4865,
      0.509
    ]
  },
  "pythia_c4__qwen7b": {
    "k_star": 2,
    "1v2_auc": 0.8943,
    "1v2_ci": [
      0.8881,
      0.9005
    ]
  },
  "olmo_c4__qwen7b": {
    "k_star": 1,
    "1v2_auc": 0.4965,
    "1v2_ci": [
      0.485,
      0.5078
    ]
  },
  "match": "pythia K*(1....

--- exp_7b_scorer_arxiv ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "pythia_arxiv_qwen1b5": {
    "k_star": 3,
    "0v1": 0.9872,
    "1v2": 0.7938,
    "2v3": 0.6544
  },
  "olmo_arxiv_qwen1b5": {
    "k_star": 1,
    "0v1": 0.9954,
    "1v2": 0.5182,
    "2v3": 0.4956
  },
  "pythia_arxiv_qwen7b": {
    "k_star": 3,
    "0v1": 0.9844,
    "1v2": 0.7987,
    "2v3": 0.6551
  },
  "olmo_arxiv_qwen7b": {
    "k_star": 1,
    "0v1": 0.9941,
    "1v2": 0.5089,
    "2v3": 0.492
  },
  "summary": "7B scorer and 1.5B scorer yield identical K* on arXiv: Pythia=3, OL...

--- exp_arXiv_olmo ---
  Status: DONE
  Conclusion: negative
  Metrics: {
  "K_star": 1,
  "auc_0v1": 0.9958,
  "auc_1v2": 0.5034,
  "auc_2v3": 0.5069,
  "auc_3v4": 0.5021,
  "auc_4v5": 0.5037,
  "jsd_0v1": 0.329,
  "ordinal_acc": 0.33
}

--- exp_arXiv_qwen1b5_crossscorer ---
  Status: DONE
  Conclusion: success
  Metrics: {
  "k_star": 3,
  "auc_0v1": 0.9748,
  "auc_1v2": 0.8105,
  "auc_2v3": 0.6317,
  "auc_3v4": 0.5437,
  "auc_4v5": 0.5294,
  "jsd_0v1": 0.154297,
  "jsd_1v2": 0.066782,
  "jsd_2v3": 0.019268,
  "jsd_3v4": 0.008867,
  "jsd_4v5": 0.006991,
  "ordinal_mae": 0.9017,
  "ordinal_accuracy": 0.4402
}

--- exp_arXiv_qwen7b ---
  Status: DONE
  Conclusion: success
  Metrics: {
  "k_star": 3,
  "pairwise_auc": {
    "0v1": 0.983,
    "1v2": 0.835,
    "2v3": 0.626,
    "3v4": 0.544,
    "4v5": 0.513
  },
  "pairwise_jsd": {
    "0v1": 0.1656,
    "1v2": 0.0668,
    "2v3": 0.0156,
    "3v4": 0.0089,
    "4v5": 0.0061
  },
  "ordinal_mae": 0.9,
  "ordinal_accuracy": 0.446
}

--- exp_arXiv_qwen7b_crossscorer ---
  Status: DONE
  Conclusion: negative
  Metrics: {
  "k_star": 2,
  "auc_0v1": 0.9575,
  "auc_1v2": 0.8171,
  "auc_2v3": 0.5989,
  "auc_3v4": 0.5417,
  "auc_4v5": 0.5192,
  "jsd_0v1": 0.137085,
  "jsd_1v2": 0.059688,
  "jsd_2v3": 0.013508,
  "jsd_3v4": 0.009125,
  "jsd_4v5": 0.006738,
  "ordinal_mae": 0.9617,
  "ordinal_accuracy": 0.4255
}

--- exp_code_multi_source ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "k_star": 2,
  "generators": [
    "qwen7b",
    "llama8b",
    "mistral7b"
  ],
  "unified_scorer": "qwen2.5-1.5b",
  "vocab_only_no_label": {
    "0v1": 0.7891,
    "1v2": 0.6353,
    "2v3": 0.5121,
    "kstar": 2
  },
  "vocab_only_with_label": {
    "0v1": 0.79,
    "1v2": 0.644,
    "2v3": 0.5118,
    "kstar": 2
  },
  "unified_no_label": {
    "0v1": 0.9123,
    "1v2": 0.6702,
    "2v3": 0.5013,
    "kstar": 2
  },
  "unified_with_label": {
    "0v1": 0.9123,
    "1v2": 0.6803,
    "2v...

--- exp_code_pythia1b4 ---
  Status: DONE
  Conclusion: negative
  Metrics (truncated): {
  "k_star": 1,
  "theta": 0.6,
  "pairwise_auc": {
    "0v1": {
      "mean": 0.9592,
      "std": 0.0036,
      "folds": [
        0.9576,
        0.9576,
        0.9657,
        0.96,
        0.9552
      ]
    },
    "1v2": {
      "mean": 0.5983,
      "std": 0.005,
      "folds": [
        0.601,
        0.5884,
        0.6,
        0.5997,
        0.6024
      ]
    },
    "2v3": {
      "mean": 0.5215,
      "std": 0.0128,
      "folds": [
        0.5236,
        0.5124,
        0.5311,...

--- exp_deberta_c4 ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "pairwise_auc": {
    "0v1": 0.9941,
    "1v2": 0.6781,
    "2v3": 0.5895,
    "3v4": 0.5651,
    "4v5": 0.5485
  },
  "ci_95": {
    "0v1": [
      0.993,
      0.9951
    ],
    "1v2": [
      0.6696,
      0.6866
    ],
    "2v3": [
      0.5814,
      0.5979
    ],
    "3v4": [
      0.5573,
      0.5732
    ],
    "4v5": [
      0.5411,
      0.5562
    ]
  },
  "f1_at_050": {
    "0v1": 0.9352,
    "1v2": 0.6751,
    "2v3": 0.6607,
    "3v4": 0.6204,
    "4v5": 0.2869
  },
  "kstar": 2...

--- exp_deberta_c4_1b5 ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "config": "qwen_rw",
  "kstar": 2,
  "kstar_theta": 0.6,
  "pairwise_auc": {
    "0v1": 0.9923,
    "1v2": 0.7052,
    "2v3": 0.5988,
    "3v4": 0.5698,
    "4v5": 0.5475
  },
  "ci_95": {
    "0v1": [
      0.9907,
      0.9937
    ],
    "1v2": [
      0.6977,
      0.7129
    ],
    "2v3": [
      0.5905,
      0.6063
    ],
    "3v4": [
      0.5626,
      0.5774
    ],
    "4v5": [
      0.5404,
      0.5542
    ]
  },
  "obd_baseline": {
    "0v1": 0.987,
    "1v2": 0.6262,
    "2v3": ...

--- exp_deberta_c4_1b5_pythia ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "config": "pythia_greedy",
  "kstar": 2,
  "kstar_theta": 0.6,
  "pairwise_auc": {
    "0v1": 0.9998,
    "1v2": 0.9284,
    "2v3": 0.5419,
    "3v4": 0.5163,
    "4v5": 0.5098
  },
  "ci_95": {
    "0v1": [
      0.9996,
      0.9999
    ],
    "1v2": [
      0.923,
      0.9331
    ],
    "2v3": [
      0.5354,
      0.5486
    ],
    "3v4": [
      0.509,
      0.5237
    ],
    "4v5": [
      0.5037,
      0.516
    ]
  },
  "obd_baseline": {
    "0v1": 0.9992,
    "1v2": 0.8838,
    "2v...

--- exp_deberta_upperbound ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "wiki_pythia": {
    "kstar": 3,
    "0v1_auc": 0.9993,
    "1v2_auc": 0.725,
    "2v3_auc": 0.6137,
    "3v4_auc": 0.5733,
    "4v5_auc": 0.5527
  },
  "wiki_olmo": {
    "kstar": 1,
    "0v1_auc": 0.9999,
    "1v2_auc": 0.5183,
    "2v3_auc": 0.5048,
    "3v4_auc": 0.5021,
    "4v5_auc": 0.4989
  },
  "wiki_qwen7b": {
    "kstar": 3,
    "0v1_auc": 0.9998,
    "1v2_auc": 0.7619,
    "2v3_auc": 0.6108,
    "3v4_auc": 0.5587,
    "4v5_auc": 0.5412
  },
  "wiki_llama8b": {
    "kstar": 3,
   ...

--- exp_gemma2b_10k ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "K_star_self": 2,
  "K_star_qwen": 2,
  "scorer": "Qwen2.5-1.5B-Instruct (cross-scored)",
  "pairwise_auc_self": {
    "0v1": 0.9817,
    "1v2": 0.643,
    "2v3": 0.555,
    "3v4": 0.5173,
    "4v5": 0.5101
  },
  "pairwise_auc_qwen": {
    "0v1": 0.9533,
    "1v2": 0.6099,
    "2v3": 0.5409,
    "3v4": 0.5174,
    "4v5": 0.5158
  },
  "bootstrap_ci_1v2": {
    "auc_oof": 0.6099,
    "boot_std": 0.0034,
    "ci_95": [
      0.6031,
      0.6167
    ],
    "ci_995_bonferroni_pct": [
      0.5...

--- exp_multi_source_arxiv ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "domain": "arxiv",
  "generators": [
    "qwen1b5",
    "pythia1b4",
    "llama8b"
  ],
  "unified_scorer": "qwen2.5-1.5b",
  "docs_per_generator": 1000,
  "vocab_only_no_label_0v1": 0.9431,
  "vocab_only_no_label_1v2": 0.6922,
  "vocab_only_no_label_2v3": 0.589,
  "vocab_only_no_label_kstar": 2,
  "vocab_only_with_label_0v1": 0.9436,
  "vocab_only_with_label_1v2": 0.702,
  "vocab_only_with_label_2v3": 0.5883,
  "vocab_only_with_label_kstar": 2,
  "unified_no_label_0v1": 0.9899,
  "unified_n...

--- exp_multi_source_detection ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "v2_generators": [
    "qwen1b5",
    "pythia1b4",
    "llama8b"
  ],
  "v2_kstar_no_label": 2,
  "v2_kstar_with_label": 2,
  "v2_0v1_auc_no_label": 0.968,
  "v2_0v1_auc_with_label": 0.9785,
  "v2_1v2_auc_no_label": 0.7144,
  "v2_1v2_auc_with_label": 0.7251,
  "v2_2v3_auc_no_label": 0.5321,
  "v2_2v3_auc_with_label": 0.5362,
  "vocab_only_v1_0v1": 0.8675,
  "vocab_only_v1_1v2": 0.676,
  "vocab_only_v1_2v3": 0.4938,
  "vocab_only_v1_kstar": 2,
  "vocab_only_v2_0v1": 0.8296,
  "vocab_only_v2_1...

--- exp_olmo1b_10k ---
  Status: DONE
  Conclusion: success
  Metrics: {
  "pairwise_auc": {
    "0v1": 0.9871,
    "1v2": 0.4984,
    "2v3": 0.5059,
    "3v4": 0.5061,
    "4v5": 0.5074
  },
  "K_star": 1,
  "ordinal_mae": 1.4145,
  "ordinal_accuracy": 0.3152,
  "pairwise_jsd": {
    "0v1": 0.230018,
    "1v2": 0.001457,
    "2v3": 0.001512,
    "3v4": 0.001413,
    "4v5": 0.001535
  },
  "top_features": [
    "freq_entropy",
    "surp_d1_mean",
    "freq_kurtosis",
    "surp_d2_mean",
    "surp_d1_skew"
  ]
}

--- exp_olmo1b_c4_rerun ---
  Status: DONE
  Conclusion: negative
  Metrics: {
  "0v1_auc": 0.986,
  "1v2_auc": 0.508,
  "2v3_auc": 0.4973,
  "3v4_auc": 0.5024,
  "4v5_auc": 0.4942,
  "kstar_at_060": 1,
  "main_table_1v2": 0.6145,
  "delta": -0.1065
}

--- exp_olmo_retrain_v3 ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "k_star": 4,
  "pairwise_auc": {
    "0v1": 0.9873,
    "1v2": 0.8889,
    "2v3": 0.7036,
    "3v4": 0.6817
  },
  "bootstrap_ci_10k": {
    "0v1": {
      "mean": 0.9972,
      "ci_95": [
        0.9967,
        0.9977
      ]
    },
    "1v2": {
      "mean": 0.9572,
      "ci_95": [
        0.9542,
        0.9601
      ]
    },
    "2v3": {
      "mean": 0.8885,
      "ci_95": [
        0.8814,
        0.8947
      ]
    },
    "3v4": {
      "mean": 0.8772,
      "ci_95": [
        0.868...

--- exp_pythia14b_c4_10k ---
  Status: DONE
  Conclusion: success
  Metrics: {
  "K_star": 2,
  "AUC_0v1": 0.9712,
  "AUC_1v2": 0.6175,
  "AUC_2v3": 0.5364,
  "AUC_3v4": 0.5134,
  "AUC_4v5": 0.5088,
  "bootstrap_1v2_95CI": [
    0.6108,
    0.6242
  ],
  "bootstrap_1v2_995CI_bonferroni": [
    0.6078,
    0.6273
  ],
  "perm_pvalue_1v2": 0.0001,
  "bonferroni_pass": true,
  "top_feature": "freq_entropy"
}

--- exp_pythia14b_c4_rerun ---
  Status: DONE
  Conclusion: negative
  Metrics: {
  "0v1_auc": 0.9979,
  "1v2_auc": 0.8786,
  "2v3_auc": 0.5399,
  "3v4_auc": 0.5062,
  "4v5_auc": 0.5025,
  "kstar_at_060": 2,
  "0v1_jsd": 0.5844,
  "1v2_jsd": 0.0718,
  "NOTE": "GREEDY decoding -- inflated AUC, not comparable to main table"
}

--- exp_pythia69b_c4_depth_chain_v3 ---
  Status: DONE
  Conclusion: negative
  Metrics: {
  "0v1_auc": 0.9941,
  "1v2_auc": 0.8542,
  "2v3_auc": 0.5373,
  "3v4_auc": 0.5339,
  "4v5_auc": 0.5211,
  "kstar_at_060": 2,
  "0v1_jsd": 0.53459,
  "1v2_jsd": 0.06438,
  "2v3_jsd": 0.00502,
  "empty_texts_total": 144,
  "features_rows": 30000
}

--- exp_pythia69b_c4_nuc ---
  Status: DONE
  Conclusion: negative
  Metrics: {
  "K_star": 1,
  "pairwise_auc": {
    "0v1": 0.9599,
    "1v2": 0.5955,
    "2v3": 0.5298,
    "3v4": 0.5135
  },
  "scorer": "Qwen-1.5B",
  "theta": 0.6,
  "note": "1v2 AUC borderline (0.0045 below threshold)"
}

--- exp_pythia_retrain_depth7 ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "kstar": 7,
  "pairwise_auc": {
    "0v1": 0.9844,
    "1v2": 0.947,
    "2v3": 0.8891,
    "3v4": 0.7999,
    "4v5": 0.6907,
    "5v6": 0.6497,
    "6v7": 0.634
  },
  "pairwise_auc_ci": {
    "0v1": [
      0.9829,
      0.9858
    ],
    "1v2": [
      0.9418,
      0.9522
    ],
    "2v3": [
      0.8822,
      0.896
    ],
    "3v4": [
      0.7951,
      0.8047
    ],
    "4v5": [
      0.688,
      0.6934
    ],
    "5v6": [
      0.6429,
      0.6565
    ],
    "6v7": [
      0.6275,...

--- exp_wiki_multi_source ---
  Status: DONE
  Conclusion: success
  Metrics (truncated): {
  "k_star": 1,
  "generators": [
    "qwen1b5",
    "llama8b",
    "mistral7b"
  ],
  "docs_per_generator": 1000,
  "total_rows": 18000,
  "unified_scorer": "qwen2.5-1.5b",
  "vocab_only_no_label": {
    "0v1": 0.7616,
    "1v2": 0.5434,
    "2v3": 0.517,
    "kstar": 1
  },
  "vocab_only_with_label": {
    "0v1": 0.7779,
    "1v2": 0.552,
    "2v3": 0.5248,
    "kstar": 1
  },
  "unified_no_label": {
    "0v1": 0.9603,
    "1v2": 0.5685,
    "2v3": 0.519,
    "kstar": 1
  },
  "unified_with_l...

--- exp_wiki_olmo_v2 ---
  Status: DONE
  Conclusion: negative
  Metrics: {
  "K_star": 1,
  "auc_0v1": 0.9932,
  "auc_1v2": 0.4986,
  "auc_2v3": 0.5012,
  "auc_3v4": 0.5057,
  "auc_4v5": 0.5009,
  "jsd_0v1": 0.1688,
  "ordinal_acc": 0.3227
}

--- exp_wiki_pythia_v2 ---
  Status: DONE
  Conclusion: negative
  Metrics: {
  "K_star": 1,
  "auc_0v1": 0.975,
  "auc_1v2": 0.5846,
  "auc_2v3": 0.5445,
  "auc_3v4": 0.5205,
  "auc_4v5": 0.5168,
  "jsd_0v1": 0.080065,
  "jsd_1v2": 0.007773,
  "ordinal_acc": 0.3503
}

--- exp_wiki_qwen7b ---
  Status: DONE
  Conclusion: success
  Metrics: {
  "K_star": 2,
  "auc_0v1": 0.9673,
  "auc_1v2": 0.6108,
  "auc_2v3": 0.5562,
  "auc_3v4": 0.5297,
  "auc_4v5": 0.529,
  "jsd_0v1": 0.083514,
  "jsd_1v2": 0.010991,
  "jsd_2v3": 0.00555,
  "jsd_3v4": 0.004611,
  "jsd_4v5": 0.003894,
  "ordinal_mae": 1.2501,
  "ordinal_accuracy": 0.3532
}

--- exp_wiki_scorer_confound ---
  Status: DONE
  Conclusion: negative
  Metrics: {
  "k_star": 1,
  "confound_verdict": "confirmed",
  "auc_0v1": 0.9404,
  "auc_1v2": 0.587,
  "auc_2v3": 0.5456,
  "auc_3v4": 0.525,
  "auc_4v5": 0.5172,
  "critical_delta_1v2": -0.0238
}

--- exp_wiki_scorer_confound_1b5 ---
  Status: DONE
  Conclusion: negative
  Metrics: {
  "k_star": 1,
  "confound_verdict": "confirmed",
  "auc_0v1": 0.9729,
  "auc_1v2": 0.5994,
  "auc_2v3": 0.533,
  "auc_3v4": 0.5214,
  "auc_4v5": 0.5068,
  "jsd_0v1": 0.0886,
  "ordinal_mae": 1.2995,
  "ordinal_accuracy": 0.3466
}

--- mvp_pilot_sat_v1 ---
  Status: DONE
  Conclusion: success
  Metrics: {
  "pairwise_auc": {
    "0v1": 0.9956,
    "1v2": 0.6957,
    "2v3": 0.5893,
    "3v4": 0.5434,
    "4v5": 0.5343
  },
  "pairwise_auc_std": {
    "0v1": 0.0005,
    "1v2": 0.0072,
    "2v3": 0.012,
    "3v4": 0.0053,
    "4v5": 0.0091
  },
  "pairwise_jsd": {
    "0v1": 0.2669,
    "1v2": 0.0163,
    "2v3": 0.0069,
    "3v4": 0.0047,
    "4v5": 0.0041
  },
  "k_star": 2,
  "ordinal_mae": 1.0163,
  "ordinal_accuracy": 0.4182
}

--- seed_gemma27b_c4_s42 ---
  Status: DONE
  Conclusion: success
  Metrics: {
  "K_star": 1,
  "scorer": "Qwen2.5-1.5B-Instruct (cross-scored)",
  "pairwise_auc_self": {
    "0v1": 0.9695,
    "1v2": 0.6196,
    "2v3": 0.5388,
    "3v4": 0.5069,
    "4v5": 0.5124
  },
  "pairwise_auc_qwen": {
    "0v1": 0.8874,
    "1v2": 0.5894
  },
  "note": "Self-scored K*=2 (1v2=0.6196), Qwen cross-scored K*=1 (1v2=0.5894 < \u03b8=0.60). Self\u2192Cross inflation: 1v2 \u0394=-3.0pp, 0v1 \u0394=-8.2pp."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b55fcd58-3f83-49a3-ba58-80653231ff8f",
  "isSidechain": true,
  "promptId": "7d9f03b2-f13f-4ae8-b207-26c75cd900b2",
  "agentId": "a00d6d05ce2acd01d",
  "type": "user",
  "uuid": "88dfd142-34f3-41ce-a1a3-f2f52bf8e779",
  "sourceToolAssistantUUID": "b55fcd58-3f83-49a3-ba58-80653231ff8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-24T04:30:39.779Z_

Now let me get the remaining experiments and the baseline data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88dfd142-34f3-41ce-a1a3-f2f52bf8e779",
  "isSidechain": true,
  "agentId": "a00d6d05ce2acd01d",
  "requestId": "req_011CbLmMuCX7UztFi925eJoV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e081061d-f1fa-4bab-85ac-eb624ca979b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011YuVjdxpbUQkmUATqCFP8h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17749,
      "cache_read_input_tokens": 55651,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17749,
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

_source line 47 · 2026-05-24T04:30:47.840Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01VWkmnT7UzSguLLeiNuTfYo`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2/tool-results/mcp-agent-ml-research-read_registry-1779596868416.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\ninner = json.loads(outer['result'])\n\n# Check baseline and other top-level data\ndata = inner['data']\nprint('=== BASELINE ===')\nif 'baseline' in data:\n    print(json.dumps(data['baseline'], indent=2)[:2000])\nprint(f'\\nCount: {data.get(\\\"count\\\")}')\nprint(f'Total: {data.get(\\\"total\\\")}')\n\n# Check metadata\nif 'metadata' in inner:\n    print('\\n=== METADATA ===')\n    print(json.dumps(inner['metadata'], indent=2)[:500])\n\" 2>&1",
  "description": "Extract baseline data and metadata"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e081061d-f1fa-4bab-85ac-eb624ca979b3",
  "isSidechain": true,
  "agentId": "a00d6d05ce2acd01d",
  "requestId": "req_011CbLmMuCX7UztFi925eJoV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3e46df5f-0cde-47f3-a1d8-cad6db7717f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011YuVjdxpbUQkmUATqCFP8h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17749,
      "cache_read_input_tokens": 55651,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17749,
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

_source line 48 · 2026-05-24T04:30:47.931Z_

<details><summary>↩ Tool result · `toolu_01VWkmnT7UzSguLLeiNuTfYo`</summary>

```text
=== BASELINE ===
null

Count: 165
Total: 165

=== METADATA ===
{
  "elapsed_seconds": 0.5091
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e46df5f-0cde-47f3-a1d8-cad6db7717f3",
  "isSidechain": true,
  "promptId": "7d9f03b2-f13f-4ae8-b207-26c75cd900b2",
  "agentId": "a00d6d05ce2acd01d",
  "type": "user",
  "uuid": "4c7a3a77-5f3b-44f4-aa2d-fc8907a639e2",
  "sourceToolAssistantUUID": "3e46df5f-0cde-47f3-a1d8-cad6db7717f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-24T04:30:50.785Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01ML8j18cJXC5dryutZXvj3k`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2/tool-results/mcp-agent-ml-research-read_registry-1779596868416.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Get expanded downstream eval full metrics\ne = exps['exp_expanded_downstream_eval']\nprint(json.dumps(e['metrics'], indent=2))\n\" 2>&1 | head -200",
  "description": "Get full expanded downstream eval metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c7a3a77-5f3b-44f4-aa2d-fc8907a639e2",
  "isSidechain": true,
  "agentId": "a00d6d05ce2acd01d",
  "requestId": "req_011CbLmMuCX7UztFi925eJoV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e40c875-9236-4663-a08e-c321bf0352eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011YuVjdxpbUQkmUATqCFP8h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17749,
      "cache_read_input_tokens": 55651,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17749,
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

_source line 50 · 2026-05-24T04:30:50.867Z_

<details><summary>↩ Tool result · `toolu_01ML8j18cJXC5dryutZXvj3k`</summary>

```text
{
  "metric_standard": "PIQA=acc_norm, ARC-C=acc_norm, WinoGrande=acc, TruthfulQA=mc2, GSM8K=exact_match(strict)",
  "base_model": {
    "piqa": 0.7612,
    "arc_c": 0.5486,
    "winogrande": 0.6456,
    "truthfulqa": 0.4659,
    "gsm8k": 0.6224
  },
  "no_filter_mean": {
    "piqa": 0.7519,
    "arc_c": 0.5193,
    "winogrande": 0.6485,
    "truthfulqa": 0.4246,
    "gsm8k": 0.5666
  },
  "binary_ours_mean": {
    "piqa": 0.7479,
    "arc_c": 0.5171,
    "winogrande": 0.6406,
    "truthfulqa": 0.4398,
    "gsm8k": 0.5858
  },
  "graduated_mean": {
    "piqa": 0.751,
    "arc_c": 0.519,
    "winogrande": 0.6461,
    "truthfulqa": 0.4245,
    "gsm8k": 0.5613
  },
  "binary_vs_nf_delta": {
    "piqa": -0.4,
    "arc_c": -0.22,
    "winogrande": -0.79,
    "truthfulqa": 1.52,
    "gsm8k": 1.92
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e40c875-9236-4663-a08e-c321bf0352eb",
  "isSidechain": true,
  "promptId": "7d9f03b2-f13f-4ae8-b207-26c75cd900b2",
  "agentId": "a00d6d05ce2acd01d",
  "type": "user",
  "uuid": "616d7557-5d92-4e87-8d31-b336ad1e086f",
  "sourceToolAssistantUUID": "9e40c875-9236-4663-a08e-c321bf0352eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-24T04:30:52.716Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01C2XGkKE8hbUMXJ4PXh49Lu`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2/tool-results/mcp-agent-ml-research-read_registry-1779596868416.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Get full exp_006_graduated_filtering metrics\ne = exps['exp_006_graduated_filtering']\nprint(json.dumps(e['metrics'], indent=2))\n\" 2>&1 | head -200",
  "description": "Get full graduated filtering metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "616d7557-5d92-4e87-8d31-b336ad1e086f",
  "isSidechain": true,
  "agentId": "a00d6d05ce2acd01d",
  "requestId": "req_011CbLmMuCX7UztFi925eJoV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "697ab479-45cb-4f88-9b55-cad7f0138000",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011YuVjdxpbUQkmUATqCFP8h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17749,
      "cache_read_input_tokens": 55651,
      "output_tokens": 856,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17749
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 856,
          "cache_read_input_tokens": 55651,
          "cache_creation_input_tokens": 17749,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17749,
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

_source line 52 · 2026-05-24T04:30:52.799Z_

<details><summary>↩ Tool result · `toolu_01C2XGkKE8hbUMXJ4PXh49Lu`</summary>

```text
{
  "total_runs": 51,
  "binary_ours": {
    "mmlu": "0.5941\u00b10.0008",
    "hellaswag": "0.6701\u00b10.0006"
  },
  "binary_drayson": {
    "mmlu": "0.5913\u00b10.0009",
    "hellaswag": "0.6691\u00b10.0004"
  },
  "surprisal": {
    "mmlu": "0.5894\u00b10.0009",
    "hellaswag": "0.6641\u00b10.0006"
  },
  "graduated_a09": {
    "mmlu": "0.5892\u00b10.0008",
    "hellaswag": "0.6701\u00b10.0007"
  },
  "graduated_a07": {
    "mmlu": "0.5892\u00b10.0014",
    "hellaswag": "0.6695\u00b10.0004"
  },
  "graduated_a05": {
    "mmlu": "0.5880\u00b10.0013",
    "hellaswag": "0.6687\u00b10.0008"
  },
  "graduated_a03": {
    "mmlu": "0.5877\u00b10.0013",
    "hellaswag": "0.6669\u00b10.0005"
  },
  "graduated_a01": {
    "mmlu": "0.5873\u00b10.0019",
    "hellaswag": "0.6640\u00b10.0009"
  },
  "dsir": {
    "mmlu": "0.5869\u00b10.0003",
    "hellaswag": "0.6631\u00b10.0007"
  },
  "no_filter": {
    "mmlu": "0.5865\u00b10.0010",
    "hellaswag": "0.6638\u00b10.0008"
  },
  "base_model": {
    "mmlu": "0.6018",
    "hellaswag": "0.6821"
  },
  "best_strategy": "binary-ours",
  "key_finding": "binary-ours is best filtering strategy. All strategies degrade vs base_model. Graduated \u03b1 monotonically increasing confirms K*=2 boundary. DSIR below all other strategies except no-filter."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "697ab479-45cb-4f88-9b55-cad7f0138000",
  "isSidechain": true,
  "promptId": "7d9f03b2-f13f-4ae8-b207-26c75cd900b2",
  "agentId": "a00d6d05ce2acd01d",
  "type": "user",
  "uuid": "cfb1a9ef-6a2e-48d2-a5a1-5ecd938eb8d3",
  "sourceToolAssistantUUID": "697ab479-45cb-4f88-9b55-cad7f0138000",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-24T04:31:05.565Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Q6MLJBomvS32TcGKiMamxA`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2/tool-results/mcp-agent-ml-research-read_registry-1779596868416.txt\"\ncat \"$FILE\" | python3 -c \"\nimport json, sys\nouter = json.load(sys.stdin)\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Get the DeBERTa upperbound full, deberta_c4 full, retrain experiments\nfor k in ['exp_deberta_upperbound', 'exp_deberta_c4', 'exp_olmo_retrain_v3', 'exp_pythia_retrain_depth7', 'exp_022_cross_scorer_matrix']:\n    e = exps[k]\n    print(f'=== {k} ===')\n    print(json.dumps(e.get('metrics', {}), indent=2))\n    print()\n\" 2>&1 | head -400",
  "description": "Get full metrics for DeBERTa upperbound, OLMo retrain, Pythia retrain depth7, cross-scorer matrix"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cfb1a9ef-6a2e-48d2-a5a1-5ecd938eb8d3",
  "isSidechain": true,
  "agentId": "a00d6d05ce2acd01d",
  "requestId": "req_011CbLmPAERqpjRpFaucCJLc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cad1f0a3-42e2-4a7d-8712-f0afedbe9cc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KkTP3weNJtsqJvPWQAXuZZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2075,
      "cache_read_input_tokens": 73400,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2075,
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

### Tool result

_source line 54 · 2026-05-24T04:31:05.753Z_

<details><summary>↩ Tool result · `toolu_01Q6MLJBomvS32TcGKiMamxA`</summary>

```text
=== exp_deberta_upperbound ===
{
  "wiki_pythia": {
    "kstar": 3,
    "0v1_auc": 0.9993,
    "1v2_auc": 0.725,
    "2v3_auc": 0.6137,
    "3v4_auc": 0.5733,
    "4v5_auc": 0.5527
  },
  "wiki_olmo": {
    "kstar": 1,
    "0v1_auc": 0.9999,
    "1v2_auc": 0.5183,
    "2v3_auc": 0.5048,
    "3v4_auc": 0.5021,
    "4v5_auc": 0.4989
  },
  "wiki_qwen7b": {
    "kstar": 3,
    "0v1_auc": 0.9998,
    "1v2_auc": 0.7619,
    "2v3_auc": 0.6108,
    "3v4_auc": 0.5587,
    "4v5_auc": 0.5412
  },
  "wiki_llama8b": {
    "kstar": 3,
    "0v1_auc": 0.9997,
    "1v2_auc": 0.7452,
    "2v3_auc": 0.5954,
    "3v4_auc": 0.5601,
    "4v5_auc": 0.5389
  },
  "wiki_mistral7b": {
    "kstar": 3,
    "0v1_auc": 0.9998,
    "1v2_auc": 0.7483,
    "2v3_auc": 0.5552,
    "3v4_auc": 0.5434,
    "4v5_auc": 0.5298
  },
  "obd_baseline_bug_fixed": true,
  "wiki_olmo_obd_rerun": {
    "0v1": 0.9933,
    "1v2": 0.4983,
    "2v3": 0.5041,
    "3v4": 0.4986,
    "4v5": 0.5089
  },
  "key_finding": "Wiki DeBERTa K*=3 for 4/5 configs (pythia/qwen7b/llama8b/mistral7b), exceeding OBD K*=2. DeBERTa breaks OBD boundary on wiki domain. OLMo K*=1 anomalous (near-random 1v2). OBD baseline bug for olmo fixed (was copy of pythia)."
}

=== exp_deberta_c4 ===
{
  "pairwise_auc": {
    "0v1": 0.9941,
    "1v2": 0.6781,
    "2v3": 0.5895,
    "3v4": 0.5651,
    "4v5": 0.5485
  },
  "ci_95": {
    "0v1": [
      0.993,
      0.9951
    ],
    "1v2": [
      0.6696,
      0.6866
    ],
    "2v3": [
      0.5814,
      0.5979
    ],
    "3v4": [
      0.5573,
      0.5732
    ],
    "4v5": [
      0.5411,
      0.5562
    ]
  },
  "f1_at_050": {
    "0v1": 0.9352,
    "1v2": 0.6751,
    "2v3": 0.6607,
    "3v4": 0.6204,
    "4v5": 0.2869
  },
  "kstar": 2,
  "kstar_theta": 0.6,
  "config": "exp_14b_c4",
  "n_samples": 30000,
  "n_docs": 5000,
  "bootstrap_resamples": 10000,
  "training_time_min": 48.3
}

=== exp_olmo_retrain_v3 ===
{
  "k_star": 4,
  "pairwise_auc": {
    "0v1": 0.9873,
    "1v2": 0.8889,
    "2v3": 0.7036,
    "3v4": 0.6817
  },
  "bootstrap_ci_10k": {
    "0v1": {
      "mean": 0.9972,
      "ci_95": [
        0.9967,
        0.9977
      ]
    },
    "1v2": {
      "mean": 0.9572,
      "ci_95": [
        0.9542,
        0.9601
      ]
    },
    "2v3": {
      "mean": 0.8885,
      "ci_95": [
        0.8814,
        0.8947
      ]
    },
    "3v4": {
      "mean": 0.8772,
      "ci_95": [
        0.8684,
        0.8852
      ]
    }
  },
  "permutation_test": {
    "0v1": {
      "auc": 0.9988,
      "p": 0
    },
    "1v2": {
      "auc": 0.961,
      "p": 0
    },
    "2v3": {
      "auc": 0.8919,
      "p": 0.998
    },
    "3v4": {
      "auc": 0.8762,
      "p": 1
    }
  }
}

=== exp_pythia_retrain_depth7 ===
{
  "kstar": 7,
  "pairwise_auc": {
    "0v1": 0.9844,
    "1v2": 0.947,
    "2v3": 0.8891,
    "3v4": 0.7999,
    "4v5": 0.6907,
    "5v6": 0.6497,
    "6v7": 0.634
  },
  "pairwise_auc_ci": {
    "0v1": [
      0.9829,
      0.9858
    ],
    "1v2": [
      0.9418,
      0.9522
    ],
    "2v3": [
      0.8822,
      0.896
    ],
    "3v4": [
      0.7951,
      0.8047
    ],
    "4v5": [
      0.688,
      0.6934
    ],
    "5v6": [
      0.6429,
      0.6565
    ],
    "6v7": [
      0.6275,
      0.6406
    ]
  },
  "pairwise_jsd": {
    "0v1": 0.1775,
    "1v2": 0.1286,
    "2v3": 0.1069,
    "3v4": 0.0643,
    "4v5": 0.0331,
    "5v6": 0.0271,
    "6v7": 0.0138
  }
}

=== exp_022_cross_scorer_matrix ===
{
  "total_combos": 12,
  "completed": 12,
  "K_star_distribution": {
    "K2": 11,
    "K1": 1
  },
  "matrix": {
    "pythia_greedy\u00d7olmo": {
      "K_star": 2,
      "1v2": 0.8811
    },
    "pythia_greedy\u00d7pythia": {
      "K_star": 2,
      "1v2": 0.8838
    },
    "pythia_greedy\u00d7qwen_base": {
      "K_star": 2,
      "1v2": 0.8814
    },
    "pythia_greedy\u00d7qwen_instruct": {
      "K_star": 2,
      "1v2": 0.8818
    },
    "qwen_base\u00d7olmo": {
      "K_star": 2,
      "1v2": 0.6047
    },
    "qwen_base\u00d7pythia": {
      "K_star": 2,
      "1v2": 0.617
    },
    "qwen_base\u00d7qwen_base": {
      "K_star": 2,
      "1v2": 0.6262
    },
    "qwen_base\u00d7qwen_instruct": {
      "K_star": 2,
      "1v2": 0.6273
    },
    "qwen_cont256\u00d7olmo": {
      "K_star": 2,
      "1v2": 0.6028
    },
    "qwen_cont256\u00d7pythia": {
      "K_star": 1,
      "1v2": 0.5979
    },
    "qwen_cont256\u00d7qwen_base": {
      "K_star": 2,
      "1v2": 0.6282
    },
    "qwen_cont256\u00d7qwen_instruct": {
      "K_star": 2,
      "1v2": 0.6072
    }
  },
  "key_finding": "Scorer independence confirmed: K*=2 in 11/12 combos. Only exception: qwen_cont256\u00d7pythia (1v2=0.5979, borderline). Pythia-greedy 1v2~0.88 due to repetition collapse. Scorer choice \u03941v2 < 0.025 within each generator."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cad1f0a3-42e2-4a7d-8712-f0afedbe9cc5",
  "isSidechain": true,
  "promptId": "7d9f03b2-f13f-4ae8-b207-26c75cd900b2",
  "agentId": "a00d6d05ce2acd01d",
  "type": "user",
  "uuid": "3074dc4a-1fa9-4f84-b81e-372307d7ad82",
  "sourceToolAssistantUUID": "cad1f0a3-42e2-4a7d-8712-f0afedbe9cc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-24T04:33:08.296Z_

Here is the complete audit of all experiment metrics from the registry.

---

## COMPREHENSIVE REGISTRY METRICS AUDIT

**Registry:** 165 experiments total, baseline=null

---

### 1. CORE DEPTH EXPERIMENTS (C4 domain, prompt-chain)

**exp_001_pythia_depth** (Pythia-1.4B, DONE, success)
- K* = 2, Scorer: Qwen2.5-1.5B-Instruct (cross-scored)
- AUC: 0v1=0.9722, 1v2=0.6074, 2v3=0.544, 3v4=0.5051, 4v5=0.5079
- AUC std: 0v1=0.0039, 1v2=0.0078, 2v3=0.0067, 3v4=0.0032, 4v5=0.0101
- Bootstrap CI 1v2: [0.5975, 0.6172], perm_p=0.0001, bonferroni_pass=false
- Note: Self-scored 1v2=0.6539, Qwen-scored 1v2=0.6074

**exp_002_olmo_depth** (OLMo-1B, DONE, success)
- K* = 1, Scorer: Qwen2.5-1.5B-Instruct (cross-scored)
- AUC: 0v1=0.9861, 1v2=0.5001, 2v3=0.4972, 3v4=0.5034, 4v5=0.4971
- Note: Self-scored 1v2=0.6145 K*=2, Qwen-scored 1v2=0.5001 K*=1

**exp_qwen_cont_10k** (Qwen2.5-1.5B base continuation, DONE, success)
- K* = 2
- AUC: 0v1=0.9875, 1v2=0.6346, 2v3=0.5616, 3v4=0.5451, 4v5=0.5254
- Bootstrap 1v2 CI: [0.6282, 0.6409], 99.5% Bonferroni CI: [0.6255, 0.6436], bonferroni_pass=true

**exp_gemma2b_depth** (Gemma-2B, DONE, negative)
- K* = 1 (point estimate 0.5981 < theta=0.60; CI upper=0.6076 crosses)
- AUC: 0v1=0.9534, 1v2=0.5981, 2v3=0.5342, 3v4=0.503, 4v5=0.5026

**exp_018_llama8b_depth** (LLaMA-3.1-8B, DONE, success)
- K* = 2
- AUC: 0v1=0.9225, 1v2=0.6123, 2v3=0.5274, 3v4=0.5138, 4v5=0.5097
- Bootstrap CI 1v2: [0.6028, 0.6216], perm_p=0.0001

**exp_019_mistral7b_depth** (Mistral-7B-v0.3, DONE, success)
- K* = 1 (1v2=0.5935, below theta=0.60 by 0.0065)
- AUC: 0v1=0.9843, 1v2=0.5935, 2v3=0.5402, 3v4=0.5232, 4v5=0.5181

**exp_004_7b_crossscale** (Qwen2.5-7B, DONE, success)
- K* = 2
- AUC: 0v1=0.9644, 1v2=0.6178, 2v3=0.546, 3v4=0.5225, 4v5=0.5091
- Bootstrap CI 1v2: [0.6079, 0.6261]

**exp_016_base_vs_instruct** (Qwen2.5-1.5B base, DONE, success)
- K* = 2
- AUC: 0v1=0.987, 1v2=0.6262, 2v3=0.5496, 3v4=0.5294, 4v5=0.5182

**exp_017_qwen_continuation** (Qwen2.5-1.5B continuation, DONE, success)
- K* = 2
- AUC: 0v1=0.9972, 1v2=0.6114, 2v3=0.5609, 3v4=0.5408, 4v5=0.5139

**exp_14b_c4** (14B scale C4, DONE, success)
- K* = 2
- AUC: 0v1=0.9598, 1v2=0.621, 2v3=0.5494, 3v4=0.5243, 4v5=0.5154

**exp_32b_c4_6class** (Qwen2.5-32B, DONE, success)
- K* = 2
- AUC: 0v1=0.9923, 1v2=0.6945, 2v3=0.5978, 3v4=0.5669, 4v5=0.5426
- CI 95%: 1v2=[0.6864, 0.7026], 2v3=[0.5898, 0.6058]

---

### 2. DECODING ABLATION

**exp_003_decoding_ablation** (Qwen2.5-1.5B, 4 configs, DONE, success)
- K* = 2 (robust across all configs)
- Config1 greedy: 0v1=0.9796, 1v2=0.6892, 2v3=0.5612
- Config2 nuc p=0.9: 0v1=0.9945 (truncated)

**exp_020_pythia_decoding** (Pythia-1.4B, 4 configs, DONE, success)
- greedy: K*=2, AUC 0v1=0.9992, 1v2=0.8838, 2v3=0.5342 (repetition-dominated)
- nuc09: K*=2, AUC 0v1=0.9948, 1v2=0.677, 2v3=0.5549
- t07: K*=2, AUC 0v1=0.9965, 1v2=0.7265, 2v3=0.5941 (borderline)
- t12: K*=2, AUC 0v1=0.9933, 1v2=0.6172, 2v3=0.5226

---

### 3. LENGTH ABLATION

**exp_021_length_ablation** (DONE, success)
- 128tok: K*=2, 1v2 AUC=0.6219
- 256tok: K*=2, 1v2 AUC=0.6282
- 512tok: K*=2, 1v2 AUC=0.6073 (borderline; CI [0.5979, 0.6166])

---

### 4. DOMAIN EXPERIMENTS

**arXiv domain (K*=3 typically):**
- exp_024_arxiv_domain (Qwen-1.5B): K*=3, AUC 0v1=0.9946, 1v2=0.858, 2v3=0.6427, 3v4=0.5437
- exp_025_pythia_arxiv (Pythia-1.4B): K*=3, AUC 0v1=0.9877, 1v2=0.8047, 2v3=0.6545, 3v4=0.5507
- exp_arXiv_llama8b (LLaMA-3.1-8B): K*=3, AUC 0v1=0.9754, 1v2=0.8447, 2v3=0.6215
- exp_arXiv_mistral7b (Mistral-7B): K*=3, AUC 0v1=0.9848, 1v2=0.8201, 2v3=0.6275
- exp_arXiv_qwen7b (Qwen-7B): K*=3, AUC 0v1=0.983, 1v2=0.835, 2v3=0.626
- exp_arXiv_olmo (OLMo-1B): K*=1, AUC 0v1=0.9958, 1v2=0.5034 (anomalous)

**Wikipedia domain (K*=1 mostly):**
- exp_wiki_pythia_v2: K*=1, AUC 0v1=0.975, 1v2=0.5846
- exp_wiki_olmo_v2: K*=1, AUC 0v1=0.9932, 1v2=0.4986
- exp_wiki_qwen7b: K*=2, AUC 0v1=0.9673, 1v2=0.6108
- exp_wiki_llama8b: K*=1, AUC 0v1=0.9316, 1v2=0.5954
- exp_wiki_mistral7b: K*=1, AUC 0v1=0.9607, 1v2=0.5552

**Code domain (K*=2 mostly):**
- exp_code_qwen7b (Qwen-7B): K*=2, AUC 0v1=0.9051, 1v2=0.7276, 2v3=0.5368
- exp_code_llama8b (LLaMA-8B): K*=2, AUC 0v1=0.9161, 1v2=0.7394, 2v3=0.5112
- exp_code_mistral7b (Mistral-7B): K*=2, AUC 0v1=0.9191, 1v2=0.6152, 2v3=0.5293
- exp_code_qwen1b5: K*=2, AUC 0v1=0.9388, 1v2=0.7382, 2v3=0.53
- exp_code_pythia1b4: K*=1, AUC 1v2=0.5983 (borderline, below theta)

**DeBERTa arXiv:** exp_deberta_arxiv_qwen1b5: K*=4, AUC 0v1=0.9997, 1v2=0.9214, 2v3=0.7446, 3v4=0.6238, 4v5=0.5771

---

### 5. CROSS-SCORER EXPERIMENTS

**exp_022_cross_scorer_matrix** (12 combos, DONE, success)
- K*=2 in 11/12 combos; exception: qwen_cont256 x pythia (1v2=0.5979, borderline)
- pythia_greedy x {olmo, pythia, qwen_base, qwen_instruct}: 1v2 = 0.8811-0.8838 (all K*=2)
- qwen_base x {olmo, pythia, qwen_base, qwen_instruct}: 1v2 = 0.6047-0.6273 (all K*=2)

**exp_019b_mistral_cross_scorer** (Qwen-1.5B scoring Mistral text): K*=1, 1v2=0.5695 (lower than self-scorer 0.5935, confirms K*=1 genuine)

**exp_7b_scorer_ablation:**
- pythia_c4 Qwen1.5B scorer: K*=2, 1v2=0.8928
- pythia_c4 Qwen7B scorer: K*=2, 1v2=0.8943
- olmo_c4 Qwen1.5B scorer: K*=1, 1v2=0.4977
- olmo_c4 Qwen7B scorer: K*=1, 1v2=0.4965

---

### 6. CROSS-TRANSFER EXPERIMENTS

**exp_013_cross_transfer** (4x4 OBD-LightGBM matrix):
- Within-model avg mean_pw_auc: 0.6099; Cross-model avg: 0.5905
- Pythia<->OLMo retention: 91-92%
- Qwen_rw->Pythia/OLMo: 61-63% (catastrophic)
- 0v1 all cross-transfer > 0.96 AUC

**exp_cross_transfer_qwen7b_to_llama8b** (DeBERTa): K*=3, AUC 0v1=0.9998, 1v2=0.7384, 2v3=0.6278
**exp_cross_transfer_llama8b_to_qwen7b_v2** (DeBERTa): K*=3, 2v3 CI lower=0.6124

**exp_deberta_cross_transfer_wiki:** 10/12 pairs completed; K*=1 (3 pairs), K*=2 (5 pairs), K*=3 (1 pair)

---

### 7. RETRAIN-CHAIN EXPERIMENTS

**exp_008_retrain_chain_v2** (Pythia retrain-chain depth 4): K*>=4, AUC 0v1=0.9847, 1v2=0.9484, 2v3=0.8888, 3v4=0.7982

**exp_qwen_retrain_chain** (Qwen retrain depth 4): K*>=4, AUC 0v1=0.9838, 1v2=0.8969, 2v3=0.81, 3v4=0.7624

**exp_qwen_retrain_depth7** (Qwen retrain depth 7): K*=7, all pairs above theta
- AUC: 0v1=0.9837, 1v2=0.8971, 2v3=0.8098, 3v4=0.76, 4v5=0.7459, 5v6=0.7017, 6v7=0.641
- JSD: 0v1=0.23, 1v2=0.104, 2v3=0.075, 3v4=0.065, 4v5=0.061, 5v6=0.035, 6v7=0.018

**exp_pythia_retrain_depth7** (Pythia retrain depth 7): K*=7
- AUC: 0v1=0.9844, 1v2=0.947, 2v3=0.8891, 3v4=0.7999, 4v5=0.6907, 5v6=0.6497, 6v7=0.634

**exp_olmo_retrain_v3** (OLMo retrain): K*=4, AUC 0v1=0.9873, 1v2=0.8889, 2v3=0.7036, 3v4=0.6817

---

### 8. BOOTSTRAP/STATISTICAL EXPERIMENTS

**exp_007_bootstrap_ci** (4 models, DONE, success):
- All models: k_star_robust=true, all 1v2 CI lower above 0.60
- qwen_rewrite: 1v2 AUC=0.6955, CI [0.6859, 0.7041]
- pythia_cont: 1v2 AUC=0.6539, CI [0.6454, 0.663]
- olmo_cont: 1v2 AUC=0.6145, CI [0.6045, 0.6247]
- qwen_cont: 1v2 AUC=0.6112, CI [0.6015, 0.6213] (most marginal, only 0.0015 above threshold)

**exp_027_retrain_bootstrap** (10K iterations): All 4 retrain-chain pairs CI_lower >> 0.60 (min=0.7903)

**exp_C_permutation_10k**: All boundary pairs p < 0.0001

**exp_E_paired_stats**: 8/15 MMLU significant pairs, 9/15 HellaSwag; binary_ours vs all MMLU significant; max Cohen's d=10.8 (MMLU), 8.98 (HellaSwag)

**exp_changepoint_kstar**: Exact agreement with threshold K*: 17/37 (45.9%); within-1 agreement: 35/37 (94.6%)

**exp_028_power_curve**: min n for 100% detection = 2000; n=1000 gives 90% detection prob

---

### 9. DOSE RESPONSE / CONTAMINATION RATE

**exp_009_dose_10pct_v3** (5 seeds, 3 strategies):
- no_filter: MMLU=0.6058+/-0.0002, HellaSwag=0.6689+/-0.0007
- binary_ours: MMLU=0.6079+/-0.0005, HellaSwag=0.6727+/-0.0008
- graduated: MMLU=0.6066+/-0.0011, HellaSwag=0.6700+/-0.0015
- binary vs nofilter: delta MMLU=+0.0021 (p=0.001), delta HellaSwag=+0.0038 (p=0.0017)

**exp_009_dose_30pct_v3**:
- no_filter: MMLU=0.6069+/-0.0007, HellaSwag=0.6664+/-0.0020
- binary_ours: MMLU=0.6082+/-0.0012, HellaSwag=0.6725+/-0.0007
- graduated: MMLU=0.6072+/-0.0008, HellaSwag=0.6665+/-0.0014
- binary vs nofilter HellaSwag: delta=+0.0061, p=0.0036

**exp_009_dose_50pct_v3**:
- no_filter: MMLU=0.6063+/-0.0013, HellaSwag=0.6680+/-0.0005
- binary_ours: MMLU=0.6088+/-0.0011, HellaSwag=0.6731+/-0.0004
- graduated: MMLU=0.6062+/-0.0009, HellaSwag=0.6679+/-0.0002
- binary vs nofilter HellaSwag: delta=+0.0051, p=2e-05

**exp_contamination_rate_sweep** (single seed, 4 rates with ARC-C):
- rate_10: no_filter MMLU=0.5878/HS=0.6652/ARC=0.4471; binary MMLU=0.5868/HS=0.6709/ARC=0.4462
- rate_30: no_filter MMLU=0.5885/HS=0.6625/ARC=0.4334; binary MMLU=0.5867/HS=0.6702/ARC=0.448
- rate_50: no_filter MMLU=0.5858/HS=0.6582/ARC=0.43; binary MMLU=0.5913/HS=0.67/ARC=0.4505
- rate_100: no_filter MMLU=0.5707/HS=0.6217/ARC=0.3891; binary=null; graduated MMLU=0.5701/HS=0.6215/ARC=0.3933

---

### 10. FILTERING / DOWNSTREAM EXPERIMENTS

**exp_006_graduated_filtering** (51 runs, all strategies):
- binary_ours: MMLU=0.5941+/-0.0008, HellaSwag=0.6701+/-0.0006
- binary_drayson: MMLU=0.5913+/-0.0009, HellaSwag=0.6691+/-0.0004
- surprisal: MMLU=0.5894+/-0.0009, HellaSwag=0.6641+/-0.0006
- graduated_a09: MMLU=0.5892+/-0.0008, HellaSwag=0.6701+/-0.0007
- graduated_a07: MMLU=0.5892+/-0.0014, HellaSwag=0.6695+/-0.0004
- graduated_a05: MMLU=0.5880+/-0.0013, HellaSwag=0.6687+/-0.0008
- graduated_a03: MMLU=0.5877+/-0.0013, HellaSwag=0.6669+/-0.0005
- graduated_a01: MMLU=0.5873+/-0.0019, HellaSwag=0.6640+/-0.0009
- dsir: MMLU=0.5869+/-0.0003, HellaSwag=0.6631+/-0.0007
- no_filter: MMLU=0.5865+/-0.0010, HellaSwag=0.6638+/-0.0008
- base_model: MMLU=0.6018, HellaSwag=0.6821

**exp_expanded_downstream_eval** (5 benchmarks):
- base_model: PIQA=0.7612, ARC-C=0.5486, WinoGrande=0.6456, TruthfulQA=0.4659, GSM8K=0.6224
- no_filter_mean: PIQA=0.7519, ARC-C=0.5193, WinoGrande=0.6485, TruthfulQA=0.4246, GSM8K=0.5666
- binary_ours_mean: PIQA=0.7479, ARC-C=0.5171, WinoGrande=0.6406, TruthfulQA=0.4398, GSM8K=0.5858
- graduated_mean: PIQA=0.751, ARC-C=0.519, WinoGrande=0.6461, TruthfulQA=0.4245, GSM8K=0.5613
- binary vs nf delta: TruthfulQA=+1.52pp, GSM8K=+1.92pp, PIQA=-0.4pp

**exp_025_pythia_filtering** (Pythia-1.4B, DONE, negative):
- no_filter: MMLU=0.2568+/-0.0012, HellaSwag=0.5250+/-0.0008
- binary_ours: MMLU=0.2585+/-0.0004, HellaSwag=0.5251+/-0.0001
- graduated_a09: MMLU=0.2561+/-0.0009, HellaSwag=0.5253+/-0.0007

**exp_026_arxiv_filtering** (arXiv domain, DONE, negative):
- no_filter: MMLU=0.5899+/-0.0008, HellaSwag=0.6600+/-0.0002
- binary: MMLU=0.5876+/-0.0004, HellaSwag=0.6642+/-0.0004
- graduated_a09: MMLU=0.5900+/-0.0011, HellaSwag=0.6599+/-0.0003

**exp_deberta_filtering_comparison:**
- no_filter: MMLU=0.5895, HellaSwag=0.6591, ARC-C=0.4352
- obd_binary: MMLU=0.588, HellaSwag=0.6599, ARC-C=0.4522
- deberta_binary: MMLU=0.587, HellaSwag=0.6593, ARC-C=0.4471
- deberta_graduated: MMLU=0.5884, HellaSwag=0.6586, ARC-C=0.442

---

### 11. NEURAL PROBE

**exp_015_neural_probe** (3 models, DONE, success):
- Qwen-cont: K*_neural=3, AUC 0v1=0.988, 1v2=0.702, 2v3=0.616, 3v4=0.59, 4v5=0.566
- Pythia: K*_neural=2, AUC 0v1=0.966, 1v2=0.676, 2v3=0.596, 3v4=0.555, 4v5=0.532
- OLMo (self-probe rerun): K*_neural=1, AUC 0v1=0.9773, 1v2=0.5054, 2v3=0.5056

---

### 12. LLM ZERO-SHOT BASELINE

**exp_011_llm_zeroshot**:
- GPT-5.5: 5-class acc=0.332, MAE=1.102, binary acc=0.878
- Claude Opus 4.6: 5-class acc=0.331, MAE=1.15, binary acc=0.882
- ODB baseline: 5-class acc=0.386, MAE=1.107
- Both frontier LLMs worse than OBD-LightGBM on depth classification

**exp_D_obd_n500**: OBD accuracy=0.38, CI [0.34, 0.422]; McNemar vs GPT-5.5 p=0.0809, vs Claude p=0.0693 (not significant)

---

### 13. DeBERTa UPPERBOUND (wiki domain)

- wiki_pythia: K*=3, 1v2=0.725, 2v3=0.6137
- wiki_olmo: K*=1, 1v2=0.5183
- wiki_qwen7b: K*=3, 1v2=0.7619, 2v3=0.6108
- wiki_llama8b: K*=3, 1v2=0.7452, 2v3=0.5954
- wiki_mistral7b: K*=3, 1v2=0.7483, 2v3=0.5552

---

### 14. FEATURE STABILITY

**exp_026_feature_stability_v2**: 15D: K*=2 (min 1v2=0.6262); 10D: 5/5 pass (min=0.6153); 8D: 5/5 pass (min=0.6056); 5D: 2/5 pass

---

### 15. LATEX ABLATION

**exp_027_latex_ablation**: K*=3 preserved after LaTeX stripping; AUC deltas: 1v2=-0.028, 2v3=-0.021

---

### 16. MULTI-SOURCE DETECTION

**exp_multi_source_detection**: v2 K*=2 (both with/without generator label); unified no_label 0v1=0.968, 1v2=0.7144; unified with_label 0v1=0.9785, 1v2=0.7251

---

### 17. RUNTIME BENCHMARK

Status: PREPARING (no metrics yet, no conclusion)

---

### 18. MISC

- **exp_B_14d_ablation**: K*=2 stable after removing self_BLEU (14D)
- **exp_014_naturalistic**: binary AUC=0.9919, freq_entropy rho=-0.78
- **exp_012_binary_confidence**: binary detector K*=1, OBD K*=2; 6-class accuracy <= random baseline for all generators
- **exp_kstar_theta**: theta=0.60 justified as natural K*=2 boundary across all 4 models

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3074dc4a-1fa9-4f84-b81e-372307d7ad82",
  "isSidechain": true,
  "agentId": "a00d6d05ce2acd01d",
  "requestId": "req_011CbLmQ7yGmyWzahaSPCEqi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a541d946-749b-4793-8d6f-abf0e8604ef0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "5a61d3ed-30af-4d20-bc00-5c6c35fe2fa2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014L3LfLhwbZ9enRuJMWDYGo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3033,
      "cache_read_input_tokens": 75475,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3033,
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
