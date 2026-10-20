# Research conversation: I need you to parse a large JSON registry file and extract all experiment metrics for a paper data audit. The file is at

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ad4eda51cd882ef4e.jsonl`
- **Structured JSON:** [`1f4615e0c01ee8adca86.json`](../../sessions/1f/1f4615e0c01ee8adca86.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

32 recorded events

### User

_source line 1 · 2026-05-23T19:17:45.491Z_

I need you to parse a large JSON registry file and extract all experiment metrics for a paper data audit.

The file is at: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt

It's JSON with schema: {result: string} — the `result` field is itself a JSON string that needs to be parsed.

Please use Python to:
1. Load the file, parse the outer JSON, then parse the inner `result` string
2. For each experiment, extract: exp_id, status, metrics (especially accuracy, mean, std, seeds, ECE, Brier, CI, etc.), and any tags/labels
3. Group experiments by their type/condition (e.g., exception_only, full_trace, ae_only, VOTA, loop_only, no_trace, regex, majority, ablation, density/gradient masking, cross-dataset, nomarker, SFT, etc.)

Output a comprehensive structured summary with ALL numeric metrics for every experiment. I need exact numbers - don't round or summarize. Include exp_id for each.

Focus especially on:
- Table 1 experiments (cross_model): exception_only, ae_only, VOTA, loop_only, full_trace, no_trace for models GPT-4o, Claude-3.5, Gemini-2.0, DeepSeek-V3
- Table 2 experiments (ablation): different conditions with accuracy, CI, tier
- Table 3 experiments (density decomposition): exception_only, gradient masking, full_trace, label-only
- Regex baseline and Majority baseline numbers
- Any nomarker experiments
- Any cross-dataset experiments
- ECE and Brier score values

Write the output to /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_audit_registry_extract.txt so I can read it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "83fb8b21-6186-4214-9116-e4c59eb31db2",
  "agentId": "ad4eda51cd882ef4e",
  "type": "user",
  "uuid": "02816b3a-cff5-4c24-bf6a-275a25ab3188",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "d5f32b76-3066-49a9-b711-4657d91efad8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-23T19:17:45.495Z_

```json
{
  "parentUuid": "02816b3a-cff5-4c24-bf6a-275a25ab3188",
  "isSidechain": true,
  "agentId": "ad4eda51cd882ef4e",
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
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
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
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__update_registry"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "82401ac9-7ce7-411f-9475-7bd7ab80f80b",
  "timestamp": "2026-05-23T19:17:45.495Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "d5f32b76-3066-49a9-b711-4657d91efad8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-23T19:17:48.606Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01HxSyBXfPXMdn8iENhajHv7`</summary>

```json
{
  "command": "ls /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt 2>/dev/null && echo \"FILE_EXISTS\" || echo \"FILE_NOT_FOUND\"",
  "description": "Check if the target file exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82401ac9-7ce7-411f-9475-7bd7ab80f80b",
  "isSidechain": true,
  "agentId": "ad4eda51cd882ef4e",
  "requestId": "req_011CbL3CnAxFxjYxSbRX47cc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "773caa42-08d4-41ee-942c-b7fcaaf08dff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "d5f32b76-3066-49a9-b711-4657d91efad8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HdN6cstgA9GNdbWNAwNWDK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15045,
      "cache_read_input_tokens": 0,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15045
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 187,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15045,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15045,
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

_source line 4 · 2026-05-23T19:17:48.766Z_

<details><summary>↩ Tool result · `toolu_01HxSyBXfPXMdn8iENhajHv7`</summary>

```text
/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt
FILE_EXISTS
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "773caa42-08d4-41ee-942c-b7fcaaf08dff",
  "isSidechain": true,
  "promptId": "83fb8b21-6186-4214-9116-e4c59eb31db2",
  "agentId": "ad4eda51cd882ef4e",
  "type": "user",
  "uuid": "fea77840-92ee-40ea-aac5-82cacde7b2a0",
  "sourceToolAssistantUUID": "773caa42-08d4-41ee-942c-b7fcaaf08dff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "d5f32b76-3066-49a9-b711-4657d91efad8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T19:17:56.369Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01ChuU9rMZBAdVqB4dS1k7K1`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.load(f)\n\nprint(\"Outer keys:\", list(outer.keys()))\nresult_str = outer.get('result', '')\nprint(\"Result type:\", type(result_str))\nprint(\"Result length:\", len(result_str))\nprint(\"First 500 chars:\", result_str[:500])\nPYEOF\n",
  "description": "Parse outer JSON and inspect inner result"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fea77840-92ee-40ea-aac5-82cacde7b2a0",
  "isSidechain": true,
  "agentId": "ad4eda51cd882ef4e",
  "requestId": "req_011CbL3D2EYhKALJzawTg6L2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "baa3d920-8670-4594-bfad-e65e540c0127",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "d5f32b76-3066-49a9-b711-4657d91efad8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016RFPXsaGpVx4eAbsZzCvbh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1130,
      "cache_read_input_tokens": 15045,
      "output_tokens": 272,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1130
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 272,
          "cache_read_input_tokens": 15045,
          "cache_creation_input_tokens": 1130,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1130,
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

_source line 6 · 2026-05-23T19:17:56.493Z_

<details><summary>↩ Tool result · `toolu_01ChuU9rMZBAdVqB4dS1k7K1`</summary>

```text
Outer keys: ['result']
Result type: &lt;class 'str'>
Result length: 329949
First 500 chars: {"success": true, "data": {"experiments": {"deepseek_gradient_masking_seed123": {"status": "DONE", "retry_count": 0, "created_at": "2026-05-23T09:51:05.056Z", "updated_at": "2026-05-23T13:45:23.758Z", "hypothesis": "DeepSeek-6.7B gradient masking multi-seed validation (seed 123): 99.8% gradient masking should achieve ≥98.5% accuracy, confirming dilution bound stability. Derived from deepseek_gradient_masking_seed42 (99.33%, dilution 0.06%).", "parent": "deepseek_gradient_masking_seed42", "spec":
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "baa3d920-8670-4594-bfad-e65e540c0127",
  "isSidechain": true,
  "promptId": "83fb8b21-6186-4214-9116-e4c59eb31db2",
  "agentId": "ad4eda51cd882ef4e",
  "type": "user",
  "uuid": "2d1036ea-29e5-44be-8bd7-09113acc4fd9",
  "sourceToolAssistantUUID": "baa3d920-8670-4594-bfad-e65e540c0127",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "d5f32b76-3066-49a9-b711-4657d91efad8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T19:18:00.527Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01GH3z3GyEnLnCdVAmnm41CK`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\nimport os\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.load(f)\n\nresult_str = outer['result']\ninner = json.loads(result_str)\n\nprint(\"Inner keys:\", list(inner.keys()))\ndata = inner.get('data', {})\nprint(\"Data keys:\", list(data.keys()))\nexperiments = data.get('experiments', {})\nprint(\"Total experiments:\", len(experiments))\nprint(\"\\nAll experiment IDs:\")\nfor eid in sorted(experiments.keys()):\n    print(\" -\", eid)\nPYEOF\n",
  "description": "Parse inner JSON and list all experiment IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d1036ea-29e5-44be-8bd7-09113acc4fd9",
  "isSidechain": true,
  "agentId": "ad4eda51cd882ef4e",
  "requestId": "req_011CbL3DbH97qkASt9T1jW93",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9d21b8b4-acbc-423c-9370-b594ce36af37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "d5f32b76-3066-49a9-b711-4657d91efad8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_018AA4cSKfaxGQXEY71NzGPZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 496,
      "cache_read_input_tokens": 16175,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 496
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 319,
          "cache_read_input_tokens": 16175,
          "cache_creation_input_tokens": 496,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 496,
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

_source line 8 · 2026-05-23T19:18:00.632Z_

<details><summary>↩ Tool result · `toolu_01GH3z3GyEnLnCdVAmnm41CK`</summary>

```text
Inner keys: ['success', 'data', 'error', 'metadata']
Data keys: ['experiments', 'count', 'total', 'baseline']
Total experiments: 188

All experiment IDs:
 - ae_only_seed123
 - ae_only_seed456
 - attention_gradient_analysis
 - calibration_analysis_seed42
 - codellama13b_ae_only_seed123
 - codellama13b_ae_only_seed42
 - codellama13b_exception_only_seed123
 - codellama13b_exception_only_seed42
 - codellama13b_exception_only_seed456
 - codellama13b_full_trace_head2048_seed42
 - codellama13b_full_trace_tail1024_seed42
 - codellama13b_full_trace_tail1024_seed42_v2
 - codellama13b_full_trace_tail1024_seed42_v3
 - codellama13b_full_trace_tail2048_seed42
 - codellama13b_full_trace_tail2048_seed42_v2
 - codellama13b_full_trace_tail2048_seed42_v3
 - codellama13b_full_trace_tail256_seed42
 - codellama13b_full_trace_tail384_seed42
 - codellama13b_full_trace_tail512_seed123
 - codellama13b_full_trace_tail512_seed42
 - codellama13b_full_trace_tail512_seed456
 - codellama13b_label_only_seed123_v2
 - codellama13b_label_only_seed42
 - codellama13b_label_only_seed42_v2
 - codellama13b_loop_only_seed123
 - codellama13b_loop_only_seed42
 - codellama13b_loop_only_seed456
 - codellama13b_no_trace_seed42
 - codellama13b_nomarker_seed42
 - codellama13b_vota_seed123
 - codellama13b_vota_seed42
 - codellama_exception_only_seed42
 - codellama_gradient_masking_seed42
 - codellama_no_trace_seed42
 - codellama_vota_seed42
 - cross_dataset_batch
 - cross_he2mbpp_exception_only_seed42
 - cross_he2mbpp_no_trace_seed42
 - cross_mbpp2he_exception_only_seed42
 - cross_mbpp2he_no_trace_seed42
 - cross_model_calibration
 - cross_model_calibration_eval
 - debugbench_exception_bug_fix
 - debugbench_exception_only_seed42
 - debugbench_no_trace_seed42
 - debugbench_vota_seed42
 - deepseek_ae_only_seed123
 - deepseek_ae_only_seed42
 - deepseek_exception_only_seed123
 - deepseek_exception_only_seed123_v2
 - deepseek_exception_only_seed42
 - deepseek_exception_only_seed456
 - deepseek_full_trace_head2048_seed42
 - deepseek_full_trace_seed42
 - deepseek_full_trace_seed42_v2
 - deepseek_full_trace_seed42_v3
 - deepseek_full_trace_tail1024_seed42
 - deepseek_full_trace_tail2048_seed42
 - deepseek_full_trace_tail256_seed42
 - deepseek_full_trace_tail384_seed42
 - deepseek_full_trace_tail512_seed123
 - deepseek_full_trace_tail512_seed123_v2
 - deepseek_full_trace_tail512_seed42
 - deepseek_full_trace_tail512_seed456
 - deepseek_gradient_masking_seed123
 - deepseek_gradient_masking_seed42
 - deepseek_label_only_seed42
 - deepseek_loop_only_seed123
 - deepseek_loop_only_seed42
 - deepseek_loop_only_seed456
 - deepseek_no_trace_seed123
 - deepseek_no_trace_seed42
 - deepseek_vota_seed123
 - deepseek_vota_seed42
 - deepseek_vota_seed456
 - eval_missing_predictions_batch
 - eval_missing_predictions_batch_v2
 - exc_message_only_seed42
 - exc_stacktrace_only_seed42
 - exc_type_only_seed42
 - exception_only_nomarker_seed123
 - exception_only_nomarker_seed42
 - exception_only_nomarker_seed456
 - exception_only_padded2048_seed42
 - exception_only_seed123
 - exception_only_seed456
 - fewshot_gpt41_exception_only_0shot
 - fewshot_gpt41_exception_only_3shot
 - fewshot_gpt41_no_trace_0shot
 - fewshot_gpt4o_exception_only_0shot
 - fewshot_gpt4o_exception_only_3shot
 - fewshot_gpt4o_no_trace_0shot
 - fewshot_qwen7b_exception_only
 - full_trace_1024tok_seed42
 - full_trace_2048tok_seed42
 - full_trace_256tok_seed42
 - full_trace_512tok_seed42
 - full_trace_label_only_seed42
 - full_trace_seed123
 - full_trace_seed42
 - full_trace_seed42_v2
 - full_trace_seed42_v5
 - full_trace_seed456
 - full_trace_tail256_seed42
 - full_trace_tail_1024_seed42
 - full_trace_tail_256_seed42
 - full_trace_tail_512_seed42
 - full_trace_tail_seed42
 - gradient_masking_qwen7b_seed123
 - gradient_masking_qwen7b_seed42
 - gradient_masking_qwen7b_seed456
 - label_only_seed123
 - label_only_seed456
 - loop_only_seed123
 - loop_only_seed456
 - no_trace_seed123
 - no_trace_seed42
 - no_trace_seed42_v2
 - no_trace_seed42_v3
 - no_trace_seed42_v4
 - no_trace_seed42_v5
 - no_trace_seed456
 - nomarker_cross_he2mbpp_exception_only
 - qwen1.5b_exception_only_seed42
 - qwen1.5b_full_trace_seed42
 - qwen1.5b_no_trace_seed42
 - qwen1.5b_vota_seed42
 - qwen15b_ae_only_seed123
 - qwen15b_ae_only_seed42
 - qwen15b_exception_only_seed123
 - qwen15b_exception_only_seed123_v2
 - qwen15b_exception_only_seed42
 - qwen15b_exception_only_seed456
 - qwen15b_full_trace_head2048_seed42
 - qwen15b_full_trace_seed42
 - qwen15b_full_trace_tail1024_seed42
 - qwen15b_full_trace_tail2048_seed42
 - qwen15b_full_trace_tail256_seed42
 - qwen15b_full_trace_tail384_seed42
 - qwen15b_full_trace_tail512_seed123
 - qwen15b_full_trace_tail512_seed42
 - qwen15b_full_trace_tail512_seed456
 - qwen15b_label_only_seed123_v2
 - qwen15b_label_only_seed42
 - qwen15b_label_only_seed42_v2
 - qwen15b_label_only_seed456_v2
 - qwen15b_loop_only_seed123
 - qwen15b_loop_only_seed42
 - qwen15b_loop_only_seed456
 - qwen15b_no_trace_seed123
 - qwen15b_no_trace_seed42
 - qwen15b_no_trace_seed456
 - qwen15b_nomarker_seed42
 - qwen15b_vota_seed123
 - qwen15b_vota_seed42
 - qwen7b_exception_only_dynamics_seed42
 - qwen7b_full_trace_dynamics_seed42
 - qwen7b_full_trace_head2048_seed42
 - qwen7b_full_trace_label_only_seed123
 - qwen7b_full_trace_label_only_seed456
 - qwen7b_full_trace_seed123
 - qwen7b_full_trace_seed456
 - qwen7b_full_trace_seed456_v2
 - qwen7b_full_trace_tail384_seed42
 - qwen7b_full_trace_tail512_seed123
 - qwen7b_full_trace_tail512_seed42
 - qwen7b_full_trace_tail512_seed456
 - qwen7b_vota_seed123
 - qwen7b_vota_seed456
 - regex_baseline_analysis
 - regex_nomarker_baseline
 - vota_ae_only_seed42
 - vota_exception_only_seed42
 - vota_exception_only_seed42_v2
 - vota_loop_only_seed42
 - vota_no_ae_seed42
 - vota_seed123
 - vota_seed42
 - vota_seed42_v2
 - vota_seed42_v3
 - vota_seed42_v4
 - vota_seed42_v5
 - vota_seed456
 - vota_seed456_v2
 - zeroshot_codellama13b_exception_only
 - zeroshot_deepseek7b_exception_only
 - zeroshot_qwen15b_exception_only
 - zeroshot_qwen7b_exception_only
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d21b8b4-acbc-423c-9370-b594ce36af37",
  "isSidechain": true,
  "promptId": "83fb8b21-6186-4214-9116-e4c59eb31db2",
  "agentId": "ad4eda51cd882ef4e",
  "type": "user",
  "uuid": "5ac85e88-ceec-41c8-84b7-384c9d745d5a",
  "sourceToolAssistantUUID": "9d21b8b4-acbc-423c-9370-b594ce36af37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "d5f32b76-3066-49a9-b711-4657d91efad8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T19:18:07.041Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01WY9Vkr3aTgjxYLR4aWq5ZJ`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\nbaseline = inner['data'].get('baseline', {})\n\n# Inspect a few experiments to understand schema\nsample_ids = list(experiments.keys())[:3]\nfor eid in sample_ids:\n    print(f\"\\n=== {eid} ===\")\n    exp = experiments[eid]\n    print(json.dumps(exp, indent=2)[:2000])\n    print(\"...\")\nPYEOF\n",
  "description": "Inspect a few experiment schemas to understand field structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ac85e88-ceec-41c8-84b7-384c9d745d5a",
  "isSidechain": true,
  "agentId": "ad4eda51cd882ef4e",
  "requestId": "req_011CbL3DtwXWhbYEZs8N51Kh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12310fb6-74e1-478a-b73c-e1b77339e38c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "d5f32b76-3066-49a9-b711-4657d91efad8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015ZbXiBhfqGiNuK8yztYkXy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3030,
      "cache_read_input_tokens": 16671,
      "output_tokens": 325,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3030
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 325,
          "cache_read_input_tokens": 16671,
          "cache_creation_input_tokens": 3030,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3030,
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

_source line 10 · 2026-05-23T19:18:07.121Z_

<details><summary>↩ Tool result · `toolu_01WY9Vkr3aTgjxYLR4aWq5ZJ`</summary>

```text
=== deepseek_gradient_masking_seed123 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-23T09:51:05.056Z",
  "updated_at": "2026-05-23T13:45:23.758Z",
  "hypothesis": "DeepSeek-6.7B gradient masking multi-seed validation (seed 123): 99.8% gradient masking should achieve \u226598.5% accuracy, confirming dilution bound stability. Derived from deepseek_gradient_masking_seed42 (99.33%, dilution 0.06%).",
  "parent": "deepseek_gradient_masking_seed42",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/trace-verdict-study && python train/train_sft.py --condition exception_only --model_path deepseek-coder-6.7b-instruct --gradient_mask_ratio 0.998 --gradient_checkpointing --seed 123\"",
    "server": "westd-11235",
    "gpu": [
      "cuda:0"
    ],
    "pid": "874893",
    "log_path": "~/runs/trace-verdict-study/deepseek_gradient_masking_seed123.log",
    "data_path": "/root/trace-verdict-study/data/exception_only_train.jsonl",
    "data_count": 4720,
    "model_name": "deepseek-ai/deepseek-coder-6.7b-instruct",
    "seed": 123,
    "checkpoint_source": "trained_from_scratch",
    "eval_data": "/root/trace-verdict-study/data/exception_only_test.jsonl",
    "checkpoint_path": "/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_gradient_masking_seed123/final/"
  },
  "metrics": {
    "accuracy": 0.9395,
    "pass_precision": 0.924,
    "pass_recall": 0.998,
    "pass_f1": 0.959,
    "fail_precision": 0.993,
    "fail_recall": 0.794,
    "fail_f1": 0.882
  },
  "conclusion": "negative",
  "completed_at": "2026-05-23T13:45:23.758Z"
}
...

=== codellama_gradient_masking_seed42 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-23T08:52:00.476Z",
  "updated_at": "2026-05-23T11:40:38.570Z",
  "hypothesis": "Cross-architecture gradient masking validation: CodeLlama-13B exception_only with 99.8% gradient masking should achieve \u226598.5% accuracy (vs baseline 99.89%\u00b10.10), extending \u22644% dilution bound to third architecture family (Qwen + DeepSeek + CodeLlama)",
  "spec": {
    "checkpoint_path": "/root/autodl-tmp/trace-verdict-study-checkpoints/codellama_gradient_masking_seed42/final",
    "log_path": "~/runs/trace-verdict-study/codellama_gradient_masking_seed42.log"
  },
  "reproduce": {
    "finished_at": "2026-05-23T11:30:59.992Z"
  },
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-23T11:31:06.685621+00:00"
      }
    ]
  },
  "metrics": {
    "accuracy": 1,
    "accuracy_ci_lower": 1,
    "accuracy_ci_upper": 1,
    "eval_loss": 0.0625,
    "dilution_pct": -0.11,
    "pass_f1": 1,
    "fail_f1": 1,
    "n_test": 1190,
    "train_loss": 2.2387,
    "baseline_accuracy": 99.89
  },
  "conclusion": "success",
  "completed_at": "2026-05-23T11:40:38.570Z"
}
...

=== deepseek_gradient_masking_seed42 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-23T07:55:20.075Z",
  "updated_at": "2026-05-23T09:47:51.342Z",
  "hypothesis": "Cross-architecture gradient masking validation: DeepSeek-6.7B exception_only with 99.8% gradient masking should achieve \u226598.5% accuracy (vs baseline 99.39%), confirming that content quality (not gradient dilution) explains full_trace degradation across architectures, extending the \u22644% dilution bound beyond Qwen-7B",
  "spec": {
    "command": "bash -c \"... python train/train_sft.py --condition exception_only --model_path deepseek-coder-6.7b-instruct --gradient_mask_ratio 0.998 --gradient_checkpointing --seed 42\"",
    "server": "westd-11235",
    "gpu": [
      "cuda:0"
    ],
    "pid": "867878",
    "log_path": "~/runs/trace-verdict-study/deepseek_gradient_masking_seed42.log",
    "submitted_at": "2026-05-23T07:56:01.348Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "/root/autodl-tmp/trace-verdict-study-data/exception_only_train.jsonl",
    "data_count": 4720,
    "model_name": "deepseek-ai/deepseek-coder-6.7b-instruct",
    "seed": 42,
    "checkpoint_source": "trained_from_scratch",
    "eval_data": "/root/autodl-tmp/trace-verdict-study-data/exception_only_test.jsonl",
    "wall_clock_seconds": 6710.0,
    "gpu_hours": 1.86
  },
  "reproduce": {
    "finished_at": "2026-05-23T09:40:03.301Z"
  },
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-23T09:40:08.515903+00:00"
      }
    ]
  },
  "metrics": {
    "accuracy": 0.9933,
    "accuracy_ci_lower": 0.9882,
    "accuracy_ci_upper": 0.9975,
    "pass_precision": 1,
    "pass_recall": 0.9906,
    "pass_f1": 0.9953,
    "fail_precision": 0.9769,
    "fail_recall": 1,
    "fail_f1": 0.9883,
    "eval_loss": 0.0529,
    "train_loss": 0.9961,
    "majority_baseline": 0.715,
    "lift": 0.278
  },
  "conclusion": "success",
 
...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12310fb6-74e1-478a-b73c-e1b77339e38c",
  "isSidechain": true,
  "promptId": "83fb8b21-6186-4214-9116-e4c59eb31db2",
  "agentId": "ad4eda51cd882ef4e",
  "type": "user",
  "uuid": "268283b4-145a-4e3d-b2e9-9cc558b40e6d",
  "sourceToolAssistantUUID": "12310fb6-74e1-478a-b73c-e1b77339e38c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "d5f32b76-3066-49a9-b711-4657d91efad8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T19:18:13.451Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01SoMfpxpd4KVhBh7ZCemR1v`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\nbaseline = inner['data'].get('baseline', {})\n\n# Check baseline structure\nprint(\"=== BASELINE ===\")\nprint(json.dumps(baseline, indent=2)[:3000])\nPYEOF\n",
  "description": "Check baseline data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "268283b4-145a-4e3d-b2e9-9cc558b40e6d",
  "isSidechain": true,
  "agentId": "ad4eda51cd882ef4e",
  "requestId": "req_011CbL3ENeefscZdTA7YVcLj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa088686-6080-4ea3-94f0-f046add894a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "d5f32b76-3066-49a9-b711-4657d91efad8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QswVRxhezoBCgd2BGkTEyY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2306,
      "cache_read_input_tokens": 19701,
      "output_tokens": 270,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2306
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 270,
          "cache_read_input_tokens": 19701,
          "cache_creation_input_tokens": 2306,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2306,
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

_source line 12 · 2026-05-23T19:18:13.546Z_

<details><summary>↩ Tool result · `toolu_01SoMfpxpd4KVhBh7ZCemR1v`</summary>

```text
=== BASELINE ===
null
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa088686-6080-4ea3-94f0-f046add894a0",
  "isSidechain": true,
  "promptId": "83fb8b21-6186-4214-9116-e4c59eb31db2",
  "agentId": "ad4eda51cd882ef4e",
  "type": "user",
  "uuid": "181ca112-283a-458e-afc1-dcef1f0b7c7a",
  "sourceToolAssistantUUID": "fa088686-6080-4ea3-94f0-f046add894a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "d5f32b76-3066-49a9-b711-4657d91efad8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T19:18:20.912Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01VeqPY1n9qPBMwiTq8zbPjm`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Look at cross_model, regex, majority, calibration, ablation, density/cross-dataset key experiments\nkey_ids = [\n    'cross_model_calibration', 'cross_model_calibration_eval',\n    'regex_baseline_analysis', 'regex_nomarker_baseline',\n    'majority_baseline' if 'majority_baseline' in experiments else None,\n    'calibration_analysis_seed42',\n    'cross_dataset_batch',\n    'cross_he2mbpp_exception_only_seed42', 'cross_he2mbpp_no_trace_seed42',\n    'cross_mbpp2he_exception_only_seed42', 'cross_mbpp2he_no_trace_seed42',\n    'nomarker_cross_he2mbpp_exception_only',\n]\n\nfor eid in key_ids:\n    if eid and eid in experiments:\n        print(f\"\\n=== {eid} ===\")\n        print(json.dumps(experiments[eid], indent=2))\nPYEOF\n",
  "description": "Inspect key cross_model, regex, calibration, cross_dataset experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "181ca112-283a-458e-afc1-dcef1f0b7c7a",
  "isSidechain": true,
  "agentId": "ad4eda51cd882ef4e",
  "requestId": "req_011CbL3Er88zXX7i7oywck7i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12d0214a-15fa-401e-85c6-c802d442dd83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "d5f32b76-3066-49a9-b711-4657d91efad8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01ApYUuZApVRXxNXcPRvW93h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 289,
      "cache_read_input_tokens": 22007,
      "output_tokens": 486,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 289
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 486,
          "cache_read_input_tokens": 22007,
          "cache_creation_input_tokens": 289,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 289,
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

_source line 14 · 2026-05-23T19:18:20.999Z_

<details><summary>↩ Tool result · `toolu_01VeqPY1n9qPBMwiTq8zbPjm`</summary>

```text
=== cross_model_calibration ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-21T06:14:12.232Z",
  "updated_at": "2026-05-21T06:14:57.965Z",
  "hypothesis": "Calibration quality (ECE and Brier Score) of exception_only fine-tuned models is universally strong across different model architectures and sizes, not specific to Qwen-7B.",
  "spec": {
    "command": "bash eval/run_cross_model_calibration.sh",
    "server": "westd-11235",
    "data_path": "/root/autodl-tmp/trace-verdict-study-data/exception_only_test.jsonl",
    "data_count": 1190,
    "model_name": "Qwen-7B/Qwen-1.5B/CodeLlama-13B/DeepSeek-6.7B",
    "seed": 42,
    "checkpoint_source": "exception_only checkpoints for all 4 models",
    "eval_data": "exception_only_test.jsonl (1190 samples)",
    "checkpoint_path": "/root/autodl-tmp/trace-verdict-study-checkpoints/cross_model_calibration/",
    "log_path": "/root/autodl-tmp/trace-verdict-study-checkpoints/cross_model_calibration/calibration.log"
  },
  "conclusion": "success",
  "completed_at": "2026-05-21T06:14:57.965Z"
}

=== cross_model_calibration_eval ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-19T21:40:43.958Z",
  "updated_at": "2026-05-19T21:41:10.724Z",
  "hypothesis": "4 \u6a21\u578b \u00d7 exception_only \u7684 ECE/Brier \u5e94\u4e00\u81f4\u6027\u4f4e\uff08ECE < 0.01\uff09\uff0c\u9a8c\u8bc1 calibration quality \u8de8\u6a21\u578b universal",
  "conclusion": "success",
  "metrics": {
    "qwen_7b": {
      "ece": 0.0027,
      "mce": 0.8355,
      "brier": 0.0013,
      "accuracy": 0.9983
    },
    "qwen_1_5b": {
      "ece": 0.002,
      "mce": 0.7549,
      "brier": 0.0013,
      "accuracy": 0.9983
    },
    "codellama_13b": {
      "ece": 0.002,
      "mce": 0.0411,
      "brier": 0.0013,
      "accuracy": 0.9983
    },
    "deepseek_6_7b": {
      "ece": 0.0064,
      "mce": 0.7756,
      "brier": 0.0061,
      "accuracy": 0.9933
    }
  },
  "spec": {
    "checkpoint_path": "/root/autodl-tmp/trace-verdict-study-checkpoints/cross_model_calibration_results.json",
    "log_path": "N/A - eval only",
    "server": "westd-11235",
    "data_path": "existing exception_only checkpoints x4",
    "data_count": 1190,
    "model_name": "4 models x exception_only",
    "seed": 42
  },
  "completed_at": "2026-05-19T21:41:10.724Z"
}

=== regex_baseline_analysis ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-16T03:43:17.799Z",
  "updated_at": "2026-05-16T04:08:29.402Z",
  "hypothesis": "Regex/heuristic baselines on exception_only test data. Tests if simple pattern matching can match SFT performance (Reviewer critical concern).",
  "conclusion": "success",
  "metrics": {
    "regex_B1_ERROR_presence": 0.9345,
    "regex_B2_Traceback": 0.7151,
    "regex_B3_any_keyword": 0.9345,
    "regex_B4_exception_type": 0.9361,
    "regex_B5_format_marker": 0.9933,
    "regex_B6_error_count_ge2": 0.9202,
    "sft_exception_only": 0.9983,
    "best_regex_gap_vs_sft": -0.0622,
    "B5_mcnemar_p": 0.041,
    "n": 1190
  },
  "spec": {
    "checkpoint_path": "N/A (CPU analysis, no model)",
    "log_path": "N/A (CPU analysis)"
  },
  "checkpoint_path": "N/A (analysis-only, no training)",
  "log_path": "N/A (analysis-only, no training)",
  "completed_at": "2026-05-16T04:08:09.296Z"
}

=== regex_nomarker_baseline ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-21T19:03:04.213Z",
  "updated_at": "2026-05-21T19:03:23.905Z",
  "hypothesis": "Regex baselines (B1-B5) on nomarker condition will show significant degradation, especially B5 which relies on the [No exception data in trace] marker. This reveals the marker-condition B5=99.33% is a format artifact, not genuine code reasoning.",
  "conclusion": "success",
  "spec": {
    "command": "python eval/regex_baseline.py on nomarker test data",
    "server": "westd-11235",
    "data_path": "/root/autodl-tmp/trace-verdict-study-data/exception_only_nomarker_test.jsonl",
    "data_count": 1190,
    "model_name": "regex_heuristics",
    "seed": 42,
    "checkpoint_path": "N/A",
    "log_path": "N/A"
  },
  "completed_at": "2026-05-21T19:03:22.128Z",
  "metrics": {
    "B5_marker_acc": 0.9933,
    "B5_nomarker_acc": 0.2849,
    "B5_delta_pp": -70.84,
    "B1_marker_acc": 0.9345,
    "B1_nomarker_acc": 0.7151,
    "B4_marker_acc": 0.9361,
    "B4_nomarker_acc": 0.9361,
    "B5b_nomarker_acc": 0.9345,
    "n": 1190
  }
}

=== calibration_analysis_seed42 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-15T12:27:04.073Z",
  "updated_at": "2026-05-15T13:09:52.711Z",
  "spec": {
    "plan_id": "plan_007",
    "command": "python eval/calibration_analysis.py",
    "server": "westd-11235",
    "data_path": "/root/autodl-tmp/trace-verdict-study-data/",
    "data_count": 1190,
    "model_name": "Qwen2.5-Coder-7B-Instruct",
    "seed": 42
  },
  "hypothesis": "Calibration analysis: ECE + reliability diagrams for VOTA/exception_only/full_trace/no_trace. Tests whether VOTA's compressed traces improve model calibration beyond accuracy (plan_007).",
  "conclusion": "success",
  "metrics": {
    "no_trace": {
      "ece": 0.171476,
      "mce": 0.475643,
      "brier_score": 0.197152,
      "accuracy": 0.751261,
      "n_samples": 1190
    },
    "full_trace": {
      "ece": 0.095817,
      "mce": 0.249061,
      "brier_score": 0.143924,
      "accuracy": 0.817647,
      "n_samples": 1190
    },
    "label_only": {
      "ece": 0.110686,
      "mce": 0.417124,
      "brier_score": 0.120144,
      "accuracy": 0.862185,
      "n_samples": 1190
    },
    "loop_only": {
      "ece": 0.083085,
      "mce": 0.183406,
      "brier_score": 0.118335,
      "accuracy": 0.856303,
      "n_samples": 1190
    },
    "ae_only": {
      "ece": 0.000415,
      "mce": 0.000415,
      "brier_score": 0.000847,
      "accuracy": 0.99916,
      "n_samples": 1190
    },
    "exception_only": {
      "ece": 0.002717,
      "mce": 0.835484,
      "brier_score": 0.001311,
      "accuracy": 0.998319,
      "n_samples": 1190
    },
    "vota": {
      "ece": 0.00541,
      "mce": 0.622459,
      "brier_score": 0.005234,
      "accuracy": 0.994118,
      "n_samples": 1190
    }
  },
  "checkpoint_path": "/root/autodl-tmp/trace-verdict-study-checkpoints/calibration/",
  "log_path": "/root/autodl-tmp/trace-verdict-study-checkpoints/calibration/calibration_metrics.json",
  "completed_at": "2026-05-15T12:36:49.992Z"
}

=== cross_dataset_batch ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-22T04:34:14.081Z",
  "updated_at": "2026-05-22T06:04:27.930Z",
  "spec": {
    "command": "bash /root/trace-verdict-study/scripts/run_cross_dataset.sh",
    "server": "westd-11235",
    "gpu": [
      "cuda:1"
    ],
    "pid": "745582",
    "log_path": "~/runs/trace-verdict-study/cross_dataset_batch.log",
    "submitted_at": "2026-05-22T04:34:13.600Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "/root/autodl-tmp/trace-verdict-study-data/cross_dataset/",
    "data_count": 11820,
    "model_name": "Qwen2.5-Coder-7B-Instruct",
    "seed": 42
  }
}

=== cross_he2mbpp_exception_only_seed42 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-22T04:33:40.785Z",
  "updated_at": "2026-05-22T06:04:05.530Z",
  "hypothesis": "Cross-dataset generalization HE\u2192MBPP with exception_only: exception trace SFT learns transferable code reasoning patterns that generalize across datasets, predicting smaller accuracy drop compared to no_trace baseline when trained on HumanEval and tested on MBPP.",
  "spec": {
    "command": "/root/miniconda3/bin/python train/train_sft.py --condition cross_he2mbpp_exception_only --data_dir /root/autodl-tmp/trace-verdict-study-data/cross_dataset/ --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/cross_he2mbpp_exception_only --gradient_checkpointing --gpu 0 --seed 42",
    "server": "westd-11235",
    "data_path": "/root/autodl-tmp/trace-verdict-study-data/cross_dataset/",
    "data_count": 1640,
    "model_name": "Qwen2.5-Coder-7B-Instruct",
    "seed": 42
  },
  "checkpoint_path": "/root/autodl-tmp/trace-verdict-study-checkpoints/cross_he2mbpp_exception_only/final",
  "log_path": "/root/autodl-tmp/trace-verdict-study-checkpoints/cross_dataset_batch.log",
  "metrics": {
    "accuracy": 0.9941,
    "pass_precision": 0.998,
    "pass_recall": 0.9936,
    "pass_f1": 0.9957,
    "fail_precision": 0.9858,
    "fail_recall": 0.9955,
    "fail_f1": 0.9906,
    "majority_baseline": 0.6902,
    "lift": 0.304
  },
  "conclusion": "success",
  "completed_at": "2026-05-22T06:04:05.530Z"
}

=== cross_he2mbpp_no_trace_seed42 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-22T04:33:42.548Z",
  "updated_at": "2026-05-22T06:04:07.456Z",
  "hypothesis": "Cross-dataset generalization HE\u2192MBPP with no_trace baseline: without execution traces, SFT relies on dataset-specific code patterns that do not transfer well across datasets, predicting larger accuracy drop when trained on HumanEval and tested on MBPP.",
  "spec": {
    "command": "/root/miniconda3/bin/python train/train_sft.py --condition cross_he2mbpp_no_trace --data_dir /root/autodl-tmp/trace-verdict-study-data/cross_dataset/ --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/cross_he2mbpp_no_trace --gradient_checkpointing --gpu 0 --seed 42",
    "server": "westd-11235",
    "data_path": "/root/autodl-tmp/trace-verdict-study-data/cross_dataset/",
    "data_count": 1640,
    "model_name": "Qwen2.5-Coder-7B-Instruct",
    "seed": 42
  },
  "checkpoint_path": "/root/autodl-tmp/trace-verdict-study-checkpoints/cross_he2mbpp_no_trace/final",
  "log_path": "/root/autodl-tmp/trace-verdict-study-checkpoints/cross_dataset_batch.log",
  "metrics": {
    "accuracy": 0.7056,
    "pass_precision": 0.736,
    "pass_recall": 0.8941,
    "pass_f1": 0.8074,
    "fail_precision": 0.5478,
    "fail_recall": 0.2857,
    "fail_f1": 0.3756,
    "majority_baseline": 0.6902,
    "lift": 0.0155
  },
  "conclusion": "success",
  "completed_at": "2026-05-22T06:04:07.456Z"
}

=== cross_mbpp2he_exception_only_seed42 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-22T04:33:45.492Z",
  "updated_at": "2026-05-22T06:03:33.280Z",
  "hypothesis": "Cross-dataset generalization MBPP\u2192HE with exception_only: exception trace SFT learns transferable code reasoning patterns that generalize across datasets, predicting smaller accuracy drop compared to no_trace baseline when trained on MBPP and tested on HumanEval.",
  "spec": {
    "command": "/root/miniconda3/bin/python train/train_sft.py --condition cross_mbpp2he_exception_only --data_dir /root/autodl-tmp/trace-verdict-study-data/cross_dataset/ --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/cross_mbpp2he_exception_only --gradient_checkpointing --gpu 0 --seed 42",
    "server": "westd-11235",
    "data_path": "/root/autodl-tmp/trace-verdict-study-data/cross_dataset/",
    "data_count": 4270,
    "model_name": "Qwen2.5-Coder-7B-Instruct",
    "seed": 42
  }
}

=== cross_mbpp2he_no_trace_seed42 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-22T04:33:47.580Z",
  "updated_at": "2026-05-22T06:03:35.271Z",
  "hypothesis": "Cross-dataset generalization MBPP\u2192HE with no_trace baseline: without execution traces, SFT relies on dataset-specific code patterns that do not transfer well across datasets, predicting larger accuracy drop when trained on MBPP and tested on HumanEval.",
  "spec": {
    "command": "/root/miniconda3/bin/python train/train_sft.py --condition cross_mbpp2he_no_trace --data_dir /root/autodl-tmp/trace-verdict-study-data/cross_dataset/ --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/cross_mbpp2he_no_trace --gradient_checkpointing --gpu 0 --seed 42",
    "server": "westd-11235",
    "data_path": "/root/autodl-tmp/trace-verdict-study-data/cross_dataset/",
    "data_count": 4270,
    "model_name": "Qwen2.5-Coder-7B-Instruct",
    "seed": 42
  }
}

=== nomarker_cross_he2mbpp_exception_only ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-22T16:57:54.481Z",
  "updated_at": "2026-05-22T17:34:00.548Z",
  "spec": {
    "command": "python train/train_sft.py --condition cross_he2mbpp_exception_only_nomarker",
    "server": "westd-11235",
    "gpu": [
      "cuda:1"
    ],
    "pid": "821073",
    "log_path": "~/runs/trace-verdict-study/nomarker_cross_he2mbpp_exception_only.log",
    "submitted_at": "2026-05-22T16:57:53.985Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "/root/autodl-tmp/trace-verdict-study-data/cross_dataset/",
    "data_count": 1640,
    "model_name": "Qwen2.5-Coder-7B-Instruct",
    "seed": 42,
    "checkpoint_source": "trained_from_scratch",
    "eval_data": "cross_he2mbpp_exception_only_nomarker_test.jsonl",
    "wall_clock_seconds": 2166.6,
    "gpu_hours": 0.6
  },
  "reproduce": {
    "finished_at": "2026-05-22T17:24:48.087Z"
  },
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-22T17:24:53.191115+00:00"
      }
    ]
  },
  "hypothesis": "Cross-dataset nomarker ablation: removing format markers from exception_only in the HE\u2192MBPP cross-dataset setting will show minimal accuracy drop (similar to in-distribution ~2pp), confirming that cross-dataset generalization relies on semantic exception content rather than format marker shortcuts.",
  "parent": "cross_he2mbpp_exception_only_seed42",
  "checkpoint_path": "/root/autodl-tmp/trace-verdict-study-checkpoints/nomarker_cross_he2mbpp/final",
  "log_path": "/root/runs/trace-verdict-study/nomarker_cross_he2mbpp_exception_only.log",
  "metrics": {
    "accuracy": 0.9546,
    "pass_precision": 0.9943,
    "pass_recall": 0.9396,
    "pass_f1": 0.9662,
    "fail_precision": 0.8801,
    "fail_recall": 0.9879,
    "fail_f1": 0.9309,
    "eval_loss": 1.09,
    "train_loss": 0.247
  },
  "conclusion": "success",
  "completed_at": "2026-05-22T17:34:00.548Z"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12d0214a-15fa-401e-85c6-c802d442dd83",
  "isSidechain": true,
  "promptId": "83fb8b21-6186-4214-9116-e4c59eb31db2",
  "agentId": "ad4eda51cd882ef4e",
  "type": "user",
  "uuid": "f994a7cb-59cf-43f3-a949-a85b2359a58a",
  "sourceToolAssistantUUID": "12d0214a-15fa-401e-85c6-c802d442dd83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "d5f32b76-3066-49a9-b711-4657d91efad8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T19:18:32.435Z_

<details open><summary>🔧 Tool call — Bash · `toolu_018Hu1Lu3WEnV7xdraY3fEQG`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Look at main table experiments: exception_only, full_trace, no_trace, vota, ae_only, loop_only for Qwen-7B (the base)\nmain_ids = [\n    'exception_only_seed123', 'exception_only_seed456',\n    'full_trace_seed123', 'full_trace_seed42', 'full_trace_seed42_v2', 'full_trace_seed42_v5', 'full_trace_seed456',\n    'no_trace_seed42', 'no_trace_seed123', 'no_trace_seed456',\n    'no_trace_seed42_v2', 'no_trace_seed42_v3', 'no_trace_seed42_v4', 'no_trace_seed42_v5',\n    'vota_seed42', 'vota_seed123', 'vota_seed456',\n    'vota_seed42_v2', 'vota_seed42_v3', 'vota_seed42_v4', 'vota_seed42_v5',\n    'vota_seed456_v2',\n    'ae_only_seed123', 'ae_only_seed456',\n    'loop_only_seed123', 'loop_only_seed456',\n    'label_only_seed123', 'label_only_seed456',\n]\n\nfor eid in main_ids:\n    if eid in experiments:\n        exp = experiments[eid]\n        print(f\"\\n=== {eid} ===\")\n        print(f\"  status: {exp.get('status')}\")\n        print(f\"  metrics: {json.dumps(exp.get('metrics', {}))}\")\n        print(f\"  conclusion: {exp.get('conclusion')}\")\n        tags = exp.get('tags', exp.get('labels', exp.get('tag', exp.get('label', None))))\n        if tags:\n            print(f\"  tags: {tags}\")\nPYEOF\n",
  "description": "Inspect main Qwen-7B table experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f994a7cb-59cf-43f3-a949-a85b2359a58a",
  "isSidechain": true,
  "agentId": "ad4eda51cd882ef4e",
  "requestId": "req_011CbL3FQ2H9MEoGLtBVigbc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "04cf4226-7ee9-4cd4-b94b-bc591630aede",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "d5f32b76-3066-49a9-b711-4657d91efad8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TKvwVnSbmpL5iL4Te4ZDir",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6363,
      "cache_read_input_tokens": 22296,
      "output_tokens": 714,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6363
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 714,
          "cache_read_input_tokens": 22296,
          "cache_creation_input_tokens": 6363,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6363,
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

_source line 16 · 2026-05-23T19:18:32.537Z_

<details><summary>↩ Tool result · `toolu_018Hu1Lu3WEnV7xdraY3fEQG`</summary>

```text
=== exception_only_seed123 ===
  status: DONE
  metrics: {"accuracy": 0.9983, "accuracy_ci": [0.9958, 1], "majority_baseline": 0.7151, "lift": 0.2832, "n": 1190, "pass_precision": 1, "pass_recall": 0.9976, "pass_f1": 0.9988, "fail_precision": 0.9941, "fail_recall": 1, "fail_f1": 0.9971, "train_loss": 0.1096, "train_runtime_sec": 7507, "epochs": 3, "seed_comparison": {"seed42_accuracy": 0.9983, "seed456_accuracy": 0.9983, "seed123_accuracy": 0.9983, "max_diff": 0, "note": "identical accuracy to 4 decimal places across all 3 seeds (42/456/123); each has exactly 2/1190 errors; exception_only fully seed-robust"}}
  conclusion: success

=== exception_only_seed456 ===
  status: DONE
  metrics: {"accuracy": 0.9983, "accuracy_ci": [0.9958, 1], "majority_baseline": 0.7151, "lift": 0.2832, "n": 1190, "pass_precision": 1, "pass_recall": 0.9976, "pass_f1": 0.9988, "fail_precision": 0.9941, "fail_recall": 1, "fail_f1": 0.9971, "vs_seed42": {"seed42_accuracy": 0.9983, "seed456_accuracy": 0.9983, "diff": 0, "note": "identical accuracy to 4 decimal places; no predictions.jsonl for paired bootstrap"}, "train_loss": 0.1087, "eval_loss": 0.4629, "train_runtime_sec": 4541, "epochs": 3}
  conclusion: success

=== full_trace_seed123 ===
  status: DONE
  metrics: {"accuracy": 0.7958, "majority_baseline": 0.7151, "lift": 0.0807, "n": 1190, "pass_precision": 0.8753, "pass_recall": 0.8331, "pass_f1": 0.8537, "fail_precision": 0.6263, "fail_recall": 0.7021, "fail_f1": 0.662, "accuracy_ci_lower": 0.7714, "accuracy_ci_upper": 0.8202, "lift_ci_lower": 0.0504, "lift_ci_upper": 0.1143, "train_loss": 0.0416, "eval_loss": 0.0842, "wall_clock_seconds": 7844, "epoch_level": {"epoch_2_eval_loss": 0.0761, "epoch_3_eval_loss": 0.0842}}
  conclusion: success

=== full_trace_seed42 ===
  status: DONE
  metrics: {"train_loss": 0.037, "eval_loss": 0.084, "eval_mean_token_accuracy": 0.984, "accuracy": 0.284, "majority_baseline": 0.7151, "lift": -0.431, "pass_precision": 0.88, "pass_recall": 0.08, "pass_f1": 0.16, "fail_precision": 0.31, "fail_recall": 0.97, "fail_f1": 0.57}
  conclusion: killed

=== full_trace_seed42_v2 ===
  status: DONE
  metrics: {"accuracy": 0.284, "majority_baseline": 0.7151, "lift": -0.4311, "n": 1190, "pass_precision": 0.923, "pass_recall": 0.085, "pass_f1": 0.155, "fail_precision": 0.445, "fail_recall": 0.785, "fail_f1": 0.568, "train_loss": 0.0373, "eval_loss": 0.082, "eval_mean_token_accuracy": 0.984}
  conclusion: negative

=== full_trace_seed42_v5 ===
  status: DONE
  metrics: {"accuracy": 0.8176, "majority_baseline": 0.7151, "lift": 0.1025, "n": 1190, "pass_precision": 0.8774, "pass_recall": 0.866, "pass_f1": 0.8717, "fail_precision": 0.6743, "fail_recall": 0.6962, "fail_f1": 0.6851, "accuracy_ci_lower": 0.797, "accuracy_ci_upper": 0.839, "lift_vs_notrace": 0.0664, "lift_vs_notrace_ci_lower": 0.0437, "lift_vs_notrace_ci_upper": 0.0899, "train_loss": 0.05, "eval_loss": 0.0867, "wall_clock_seconds": 7852, "epoch_level": {"epoch1_accuracy": 0.8303, "epoch2_accuracy": 0.763, "final_accuracy": 0.8176, "trend": "non_monotonic_epoch1_best_epoch2_collapse"}}
  conclusion: success

=== full_trace_seed456 ===
  status: DONE
  metrics: {"accuracy": 0.805, "majority_baseline": 0.7151, "lift": 0.0899, "n": 1190, "pass_precision": 0.8637, "pass_recall": 0.8637, "pass_f1": 0.8637, "fail_precision": 0.6578, "fail_recall": 0.6578, "fail_f1": 0.6578, "accuracy_ci_lower": 0.7824, "accuracy_ci_upper": 0.8269, "lift_ci_lower": 0.0605, "lift_ci_upper": 0.121, "train_loss": 0.0416, "eval_loss": 0.082, "wall_clock_seconds": 7862, "epoch_level": {"epoch_2_eval_loss": 0.0728, "epoch_3_eval_loss": 0.082}}
  conclusion: success

=== no_trace_seed42 ===
  status: DONE
  metrics: {}
  conclusion: killed

=== no_trace_seed123 ===
  status: DONE
  metrics: {"accuracy": 0.7908, "pass_precision": 0.8117, "pass_recall": 0.8971, "pass_f1": 0.8523, "fail_precision": 0.7434, "fail_recall": 0.5901, "fail_f1": 0.6581, "n": 1190}
  conclusion: success

=== no_trace_seed456 ===
  status: DONE
  metrics: {"accuracy": 0.7504, "pass_precision": 0.8805, "pass_recall": 0.7532, "pass_f1": 0.8119, "fail_precision": 0.5455, "fail_recall": 0.7434, "fail_f1": 0.6292, "eval_loss": 0.6092, "train_loss": 0.1781, "n": 1190, "accuracy_ci": [0.7235, 0.7748]}
  conclusion: success

=== no_trace_seed42_v2 ===
  status: DONE
  metrics: {}
  conclusion: killed

=== no_trace_seed42_v3 ===
  status: DONE
  metrics: {"train_loss": 0.18, "eval_loss": 0.645, "eval_mean_token_accuracy": 0.89, "accuracy": 0.7513, "majority_baseline": 0.7151, "lift": 0.0361, "pass_precision": 0.8776, "pass_recall": 0.7579, "pass_f1": 0.8134, "fail_precision": 0.5473, "fail_recall": 0.7345, "fail_f1": 0.6272}
  conclusion: killed

=== no_trace_seed42_v4 ===
  status: DONE
  metrics: {"accuracy": 0.7513, "majority_baseline": 0.7151, "lift": 0.0361, "pass_precision": 0.8776, "pass_recall": 0.7579, "pass_f1": 0.8134, "fail_precision": 0.5473, "fail_recall": 0.7345, "fail_f1": 0.6272, "train_loss": 0.18, "eval_loss": 0.6454, "eval_mean_token_accuracy": 0.8897}
  conclusion: success

=== no_trace_seed42_v5 ===
  status: DONE
  metrics: {"accuracy": 0.7513, "accuracy_ci_lower": 0.7277, "accuracy_ci_upper": 0.7748, "majority_baseline": 0.7151, "lift": 0.0361, "lift_ci_lower": 0.0042, "lift_ci_upper": 0.0706, "n": 1190, "pass_precision": 0.8776, "pass_recall": 0.7579, "pass_f1": 0.8134, "fail_precision": 0.5473, "fail_recall": 0.7345, "fail_f1": 0.6272, "epoch_level": {"epoch1_accuracy": 0.7429, "epoch2_accuracy": 0.763, "final_accuracy": 0.7513, "trend": "non_monotonic_epoch2_best"}}
  conclusion: success

=== vota_seed42 ===
  status: DONE
  metrics: {}
  conclusion: killed

=== vota_seed123 ===
  status: DONE
  metrics: {}
  conclusion: failed

=== vota_seed456 ===
  status: DONE
  metrics: {}
  conclusion: failed

=== vota_seed42_v2 ===
  status: DONE
  metrics: {}
  conclusion: killed

=== vota_seed42_v3 ===
  status: DONE
  metrics: {"train_loss": 0.046, "eval_loss": 0.085, "eval_mean_token_accuracy": 0.983, "accuracy": 0.992, "majority_baseline": 0.7151, "lift": 0.276, "pass_precision": 0.99, "pass_recall": 0.99, "pass_f1": 0.99, "fail_precision": 0.99, "fail_recall": 0.99, "fail_f1": 0.99}
  conclusion: killed

=== vota_seed42_v4 ===
  status: DONE
  metrics: {"accuracy": 0.9563, "majority_baseline": 0.7151, "lift": 0.2412, "n": 1190, "pass_precision": 0.944, "pass_recall": 0.998, "pass_f1": 0.97, "fail_precision": 0.993, "fail_recall": 0.853, "fail_f1": 0.917, "lift_vs_notrace": 0.205, "lift_vs_notrace_ci_lower": 0.177, "lift_vs_notrace_ci_upper": 0.234, "train_loss": 0.046, "eval_loss": 0.0842}
  conclusion: success

=== vota_seed42_v5 ===
  status: DONE
  metrics: {"accuracy": 0.9941, "pass_precision": 1, "pass_recall": 0.9918, "pass_f1": 0.9959, "fail_precision": 0.9798, "fail_recall": 1, "fail_f1": 0.9898, "n": 1190, "tp": 844, "fp": 0, "tn": 339, "fn": 7}
  conclusion: success

=== vota_seed456_v2 ===
  status: DONE
  metrics: {"accuracy": 0.9908, "pass_precision": 1, "pass_recall": 0.987, "pass_f1": 0.993, "fail_precision": 0.969, "fail_recall": 1, "fail_f1": 0.984, "ci_95": [0.985, 0.996]}
  conclusion: success

=== ae_only_seed123 ===
  status: DONE
  metrics: {"accuracy": 0.9908, "n": 1190, "pass_recall": 0.987, "fail_recall": 1, "majority_baseline": 0.7151, "lift": 0.2757}
  conclusion: success

=== ae_only_seed456 ===
  status: DONE
  metrics: {"accuracy": 0.9992, "n": 1190, "majority_baseline": 0.7151, "lift": 0.2841, "seed_comparison": {"seed42_accuracy": 0.9992, "seed123_accuracy": 0.9908, "seed456_accuracy": 0.9992, "mean_accuracy": 0.9964, "std": 0.0049, "note": "2/3 seeds = 99.92%, seed123 = 99.08%. Mean = 99.64% \u00b1 0.49"}}
  conclusion: success

=== loop_only_seed123 ===
  status: DONE
  metrics: {"accuracy": 0.8588, "majority_baseline": 0.7151, "lift": 0.1437, "n": 1190, "pass_precision": 0.9129, "pass_recall": 0.8872, "pass_f1": 0.8999, "fail_precision": 0.7355, "fail_recall": 0.7876, "fail_f1": 0.7607, "accuracy_ci": [0.8403, 0.8773]}
  conclusion: success

=== loop_only_seed456 ===
  status: DONE
  metrics: {"accuracy": 0.8664, "n": 1190, "pass_precision": 0.9179, "pass_recall": 0.8931, "pass_f1": 0.9053, "fail_precision": 0.7486, "fail_recall": 0.7994, "fail_f1": 0.7732, "accuracy_ci": [0.847, 0.884], "seed_comparison": {"seed42_accuracy": 0.8563, "seed123_accuracy": 0.8588, "seed456_accuracy": 0.8664, "mean_accuracy": 0.8605, "std": 0.0053, "note": "3-seed mean = 86.05% \u00b1 0.53%. Moderate variance, seed456 best. loop_only is weakest trace condition (vs exception_only 99.83%, ae_only 99.64%, vota 99.41%)."}}
  conclusion: success

=== label_only_seed123 ===
  status: DONE
  metrics: {"accuracy": 0.8706, "n": 1190, "pass_recall": 0.974, "fail_recall": 0.611, "pass_f1": 0.915, "fail_f1": 0.729}
  conclusion: success

=== label_only_seed456 ===
  status: DONE
  metrics: {"accuracy": 0.859, "n": 1190, "pass_recall": 0.938, "fail_recall": 0.661, "pass_f1": 0.905, "fail_f1": 0.727}
  conclusion: success
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04cf4226-7ee9-4cd4-b94b-bc591630aede",
  "isSidechain": true,
  "promptId": "83fb8b21-6186-4214-9116-e4c59eb31db2",
  "agentId": "ad4eda51cd882ef4e",
  "type": "user",
  "uuid": "9945b7cf-358f-4842-96dc-66eebb7bf56b",
  "sourceToolAssistantUUID": "04cf4226-7ee9-4cd4-b94b-bc591630aede",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "d5f32b76-3066-49a9-b711-4657d91efad8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T19:18:43.019Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01PkpxKSCWzDG2BQ45n6zSvu`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Look at Qwen-7B seed42 canonical: exception_only, full_trace, no_trace, vota, ae_only, loop_only\n# Also check VOTA multi-component ablation experiments\nvota_ablation = ['vota_ae_only_seed42', 'vota_exception_only_seed42', 'vota_exception_only_seed42_v2',\n                 'vota_loop_only_seed42', 'vota_no_ae_seed42',\n                 'exc_message_only_seed42', 'exc_stacktrace_only_seed42', 'exc_type_only_seed42',\n                 'exception_only_padded2048_seed42', 'full_trace_label_only_seed42']\n\nfor eid in vota_ablation:\n    if eid in experiments:\n        exp = experiments[eid]\n        print(f\"\\n=== {eid} ===\")\n        print(f\"  status: {exp.get('status')}\")\n        print(f\"  hypothesis: {exp.get('hypothesis', '')[:200]}\")\n        print(f\"  metrics: {json.dumps(exp.get('metrics', {}))}\")\n        print(f\"  conclusion: {exp.get('conclusion')}\")\nPYEOF\n",
  "description": "Inspect VOTA ablation and exception sub-component experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9945b7cf-358f-4842-96dc-66eebb7bf56b",
  "isSidechain": true,
  "agentId": "ad4eda51cd882ef4e",
  "requestId": "req_011CbL3GFUrhSf5RfXoZrcwv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0bcdd336-4f28-4e8a-80a1-6b9c294bd9cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "d5f32b76-3066-49a9-b711-4657d91efad8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GgdkGpoVbZmgmdUUAeQ6CY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4733,
      "cache_read_input_tokens": 28659,
      "output_tokens": 543,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4733
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 543,
          "cache_read_input_tokens": 28659,
          "cache_creation_input_tokens": 4733,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4733,
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

_source line 18 · 2026-05-23T19:18:43.105Z_

<details><summary>↩ Tool result · `toolu_01PkpxKSCWzDG2BQ45n6zSvu`</summary>

```text
=== vota_ae_only_seed42 ===
  status: DONE
  hypothesis: VOTA component ablation: ae_only condition — only actual/expected values, no exception/loop compression (plan_003 sub-a)
  metrics: {"accuracy": 0.9992, "accuracy_ci": [0.9975, 1], "bootstrap_pairwise": {"ae_only_vs_no_trace": {"diff": 0.2479, "ci": [0.2235, 0.2731], "p_value": 0, "significant": true}, "ae_only_vs_exception_only": {"diff": 0.0008, "ci": [-0.0017, 0.0034], "p_value": 0.8002, "significant": false}, "ae_only_vs_vota": {"diff": 0.005, "ci": [0.0017, 0.0092], "p_value": 0.0046, "significant": true}}, "config": {"n_bootstrap": 10000, "seed": 42, "method": "paired_bootstrap"}}
  conclusion: success

=== vota_exception_only_seed42 ===
  status: DONE
  hypothesis: VOTA component ablation: exception_only condition — only exception summaries, no actual/expected or loop compression. Tests if [ERROR] events are the primary driver of VOTA's 99.2% accuracy (plan_003 
  metrics: {}
  conclusion: failed

=== vota_exception_only_seed42_v2 ===
  status: DONE
  hypothesis: VOTA component ablation: exception_only condition — retry with --gradient_checkpointing (v1 OOM at step 8). Tests if [ERROR] events are the primary driver of VOTA's 99.2% accuracy (plan_003 sub-b)
  metrics: {"accuracy": 0.9983, "majority_baseline": 0.7151, "lift": 0.2832, "n": 1190, "pass_precision": 1, "pass_recall": 0.998, "pass_f1": 0.999, "fail_precision": 0.994, "fail_recall": 1, "fail_f1": 0.997, "lift_vs_notrace": 0.2471, "lift_vs_notrace_ci_lower": 0.2227, "lift_vs_notrace_ci_upper": 0.2714, "lift_vs_fulltrace": 0.1807, "lift_vs_fulltrace_ci_lower": 0.1588, "lift_vs_fulltrace_ci_upper": 0.2034, "lift_vs_vota": 0.0067, "lift_vs_vota_ci_lower": 0.0017, "lift_vs_vota_ci_upper": 0.0126, "lift_vs_vota_pvalue": 0.01}
  conclusion: success

=== vota_loop_only_seed42 ===
  status: DONE
  hypothesis: VOTA component ablation: loop_only condition — only loop compression summaries, no actual/expected or exception. Tests loop behavioral pattern contribution to VOTA 99.2% accuracy (plan_003 sub-c)
  metrics: {"accuracy": 0.8563, "majority_baseline": 0.7151, "lift": 0.1412, "n": 1190, "pass_precision": 0.9239, "pass_recall": 0.8707, "pass_f1": 0.8966, "fail_precision": 0.7165, "fail_recall": 0.8201, "fail_f1": 0.7648, "accuracy_ci": [0.8353, 0.8756], "bootstrap_vs_no_trace": {"diff": 0.105, "ci": [0.0824, 0.1286], "significant": true}, "bootstrap_vs_vota": {"diff": -0.1378, "ci": [-0.1571, -0.1185], "significant": true}, "bootstrap_vs_full_trace": {"diff": 0.0387, "ci": [0.0185, 0.0597], "significant": true}, "train_loss": 0.0718, "wall_clock_seconds": 7425.65}
  conclusion: success

=== vota_no_ae_seed42 ===
  status: DONE
  hypothesis: VOTA without actual/expected values: tests if VOTA's accuracy comes from genuine behavioral understanding vs trivial string comparison (plan_001)
  metrics: {"accuracy": 0.994, "majority_baseline": 0.7151, "lift": 0.279, "n": 1190, "pass_f1": 0.996, "fail_f1": 0.989, "accuracy_ci_lower": 0.989, "accuracy_ci_upper": 0.998, "lift_vs_notrace": 0.243, "lift_vs_notrace_ci_lower": 0.218, "lift_vs_notrace_ci_upper": 0.268, "train_loss": 0.0908, "eval_loss": 0.2215, "wall_clock_seconds": 6397.88}
  conclusion: success

=== exc_message_only_seed42 ===
  status: DONE
  hypothesis: Exception message alone (without type or stacktrace) retains near-perfect diagnostic signal for verdict prediction, because the error message text contains the semantic description of what went wrong
  metrics: {"accuracy": 0.995, "pass_precision": 1, "pass_recall": 0.993, "pass_f1": 0.996, "fail_precision": 0.983, "fail_recall": 1, "fail_f1": 0.991, "n": 1190, "accuracy_ci": [0.991, 0.998]}
  conclusion: success

=== exc_stacktrace_only_seed42 ===
  status: DONE
  hypothesis: Exception stacktrace alone (without exception message) contains sufficient diagnostic signal for near-perfect verdict prediction, because stacktrace structure encodes the causal chain of function call
  metrics: {"accuracy": 0.998, "pass_precision": 1, "pass_recall": 0.998, "pass_f1": 0.999, "fail_precision": 0.994, "fail_recall": 1, "fail_f1": 0.997, "n": 1190, "accuracy_ci": [0.996, 1]}
  conclusion: success

=== exc_type_only_seed42 ===
  status: DONE
  hypothesis: Exception type alone (e.g. 'ValueError') without message or stacktrace retains most of exception_only's diagnostic power, since the error type is the primary signal for verdict classification
  metrics: {}
  conclusion: None

=== exception_only_padded2048_seed42 ===
  status: DONE
  hypothesis: Padding exception-only trace inputs to 2048 tokens maintains high verdict accuracy comparable to unpadded training, validating that fixed-length padding does not degrade the model's ability to classif
  metrics: {"accuracy": 0.9983, "pass_precision": 1, "pass_recall": 0.9976, "pass_f1": 0.9988, "fail_precision": 0.9941, "fail_recall": 1, "fail_f1": 0.9971, "majority_baseline": 0.7151, "lift": 0.2832, "n": 1190}
  conclusion: success

=== full_trace_label_only_seed42 ===
  status: DONE
  hypothesis: Label-only loss on full_trace fixes gradient dilution collapse (plan_002: loss only on pass/fail token, not trace tokens)
  metrics: {"accuracy": 0.8622, "accuracy_ci_lower": 0.8437, "accuracy_ci_upper": 0.8807, "majority_baseline": 0.7151, "lift": 0.1471, "n": 1190, "pass_precision": 0.8821, "pass_recall": 0.9318, "pass_f1": 0.9063, "fail_precision": 0.8007, "fail_recall": 0.6873, "fail_f1": 0.7397, "train_loss": 0.2505, "eval_loss": 0.3205, "lift_vs_notrace": 0.1109, "lift_vs_notrace_ci_lower": 0.0849, "lift_vs_notrace_ci_upper": 0.137, "lift_vs_standard_fulltrace": 0.0445, "lift_vs_standard_fulltrace_ci_lower": 0.0235, "lift_vs_standard_fulltrace_ci_upper": 0.0655, "lift_vs_standard_fulltrace_pvalue": 0}
  conclusion: success
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0bcdd336-4f28-4e8a-80a1-6b9c294bd9cc",
  "isSidechain": true,
  "promptId": "83fb8b21-6186-4214-9116-e4c59eb31db2",
  "agentId": "ad4eda51cd882ef4e",
  "type": "user",
  "uuid": "10389fd5-82bd-4664-8589-180b1899124f",
  "sourceToolAssistantUUID": "0bcdd336-4f28-4e8a-80a1-6b9c294bd9cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "d5f32b76-3066-49a9-b711-4657d91efad8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T19:18:53.659Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01J7aF4Hz8fQnxcEk3zERQFD`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Qwen-7B main ablation seed42 canonical\nqwen7b_main = [\n    'qwen7b_full_trace_seed123', 'qwen7b_full_trace_seed456', 'qwen7b_full_trace_seed456_v2',\n    'qwen7b_vota_seed123', 'qwen7b_vota_seed456',\n    'qwen7b_full_trace_label_only_seed123', 'qwen7b_full_trace_label_only_seed456',\n    'gradient_masking_qwen7b_seed42', 'gradient_masking_qwen7b_seed123', 'gradient_masking_qwen7b_seed456',\n    'qwen7b_full_trace_tail512_seed123', 'qwen7b_full_trace_tail512_seed42', 'qwen7b_full_trace_tail512_seed456',\n    'qwen7b_full_trace_head2048_seed42', 'qwen7b_full_trace_tail384_seed42',\n    'qwen7b_exception_only_dynamics_seed42', 'qwen7b_full_trace_dynamics_seed42',\n]\n\nfor eid in qwen7b_main:\n    if eid in experiments:\n        exp = experiments[eid]\n        print(f\"\\n=== {eid} ===\")\n        print(f\"  status: {exp.get('status')}\")\n        print(f\"  hypothesis: {exp.get('hypothesis', '')[:150]}\")\n        print(f\"  metrics: {json.dumps(exp.get('metrics', {}))}\")\n        print(f\"  conclusion: {exp.get('conclusion')}\")\nPYEOF\n",
  "description": "Inspect Qwen-7B supplementary experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10389fd5-82bd-4664-8589-180b1899124f",
  "isSidechain": true,
  "agentId": "ad4eda51cd882ef4e",
  "requestId": "req_011CbL3H2YG7yj7MDzQmeoiQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf50cbb9-79ae-4348-a189-92a84f7fd728",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "d5f32b76-3066-49a9-b711-4657d91efad8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01VWGKqdStfsFYFryiH2oaEF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2743,
      "cache_read_input_tokens": 33392,
      "output_tokens": 658,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2743
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 658,
          "cache_read_input_tokens": 33392,
          "cache_creation_input_tokens": 2743,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2743,
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

_source line 20 · 2026-05-23T19:18:53.756Z_

<details><summary>↩ Tool result · `toolu_01J7aF4Hz8fQnxcEk3zERQFD`</summary>

```text
=== qwen7b_full_trace_seed123 ===
  status: DONE
  hypothesis: Qwen-7B full_trace seed123 应在 ~81% 附近（与 seed42=81.76% 一致），为 MF-3 multi-seed 要求补齐 full_trace 方差估计。full_trace 是 C2 "more info hurts" claim 的锚点，单 seed 在 
  metrics: {"accuracy": 0.802, "ci_lower": 0.778, "ci_upper": 0.825, "majority_baseline": 0.715, "lift_pp": 8.7, "pass_precision": 0.88, "pass_recall": 0.84, "pass_f1": 0.86, "fail_precision": 0.64, "fail_recall": 0.7, "fail_f1": 0.67, "train_loss": 0.0415, "eval_loss": 0.0827}
  conclusion: success

=== qwen7b_full_trace_seed456 ===
  status: DONE
  hypothesis: Qwen-7B full_trace seed456 应在 ~81% 附近（与 seed42=81.76% 一致），为 MF-3 multi-seed 要求补齐 full_trace 方差估计。3-seed mean 将替换 Table 2 中的单 seed 值。
  metrics: {}
  conclusion: failed

=== qwen7b_full_trace_seed456_v2 ===
  status: DONE
  hypothesis: Qwen-7B full_trace seed456 应在 ~81% 附近（与 seed42=81.76%, seed123=80.20% 一致），为 MF-3 multi-seed 要求补齐 full_trace 方差估计。3-seed mean 将替换 Table 2 中的占位符。
  metrics: {"accuracy": 0.8235, "ci_lower": 0.8017, "ci_upper": 0.8454, "majority_baseline": 0.7151, "lift_pp": 10.84, "pass_precision": 0.8885, "pass_recall": 0.8613, "pass_f1": 0.8747, "fail_precision": 0.6767, "fail_recall": 0.7286, "fail_f1": 0.7017, "train_loss": 0.0416, "eval_loss": 0.0794}
  conclusion: success

=== qwen7b_vota_seed123 ===
  status: DONE
  hypothesis: Qwen-7B VOTA seed123 应在 84-92% 范围（与 vota_seed42_v4 一致），为 N5 reviewer concern 提供 VOTA 条件的方差估计
  metrics: {"accuracy": 0.9866, "accuracy_ci_lower": 0.979, "accuracy_ci_upper": 0.9925, "majority_baseline": 0.7151, "lift": 0.2714, "n": 1190, "pass_precision": 1, "pass_recall": 0.9812, "pass_f1": 0.9905, "fail_precision": 0.9549, "fail_recall": 1, "fail_f1": 0.9769, "train_loss": 0.0499, "eval_loss": 0.0864}
  conclusion: success

=== qwen7b_vota_seed456 ===
  status: DONE
  hypothesis: Qwen-7B VOTA seed456 应在 84-92% 范围（与 vota_seed42_v4 一致），为 N5 reviewer concern 提供 VOTA 条件的方差估计
  metrics: {"accuracy": 0.9908, "accuracy_ci_lower": 0.9849, "accuracy_ci_upper": 0.9958, "majority_baseline": 0.7151, "lift": 0.2756, "n": 1190, "pass_precision": 1, "pass_recall": 0.9871, "pass_f1": 0.9935, "fail_precision": 0.9686, "fail_recall": 1, "fail_f1": 0.984, "train_loss": 0.04969, "eval_loss": 0.08312}
  conclusion: success

=== qwen7b_full_trace_label_only_seed123 ===
  status: DONE
  hypothesis: Qwen-7B full_trace (label_only_loss) seed123 应在 95-98% 范围（与 seed42 一致），为 N5 reviewer concern 提供 full_trace 条件的方差估计
  metrics: {"accuracy": 0.8689, "accuracy_ci_lower": 0.8496, "accuracy_ci_upper": 0.8874, "pass_f1": 0.9121, "fail_f1": 0.7426, "pass_precision": 0.8765, "pass_recall": 0.9506, "fail_precision": 0.8427, "fail_recall": 0.6637, "majority_baseline": 0.7151, "lift": 0.1538, "train_loss": 0.2425, "eval_loss": 0.2787}
  conclusion: success

=== qwen7b_full_trace_label_only_seed456 ===
  status: DONE
  hypothesis: Qwen-7B full_trace (label_only_loss) seed456 应在 95-98% 范围（与 seed42 一致），为 N5 reviewer concern 提供 full_trace 条件的方差估计
  metrics: {"accuracy": 0.847, "accuracy_ci_lower": 0.827, "accuracy_ci_upper": 0.866, "pass_f1": 0.9, "fail_f1": 0.71, "pass_precision": 0.87, "pass_recall": 0.92, "fail_precision": 0.76, "fail_recall": 0.67, "majority_baseline": 0.7151, "lift": 0.1319, "train_loss": 0.2452, "eval_loss": 0.3366}
  conclusion: success

=== gradient_masking_qwen7b_seed42 ===
  status: DONE
  hypothesis: 
  metrics: {}
  conclusion: None

=== gradient_masking_qwen7b_seed123 ===
  status: DONE
  hypothesis: Gradient masking (keeping only top 0.2% gradient signals) on exception_only condition with seed 123 achieves comparable accuracy to seed 42 (98.99%), 
  metrics: {"accuracy": 0.9933, "pass_precision": 1, "pass_recall": 0.9906, "pass_f1": 0.9953, "fail_precision": 0.9769, "fail_recall": 1, "fail_f1": 0.9883, "n": 1190, "accuracy_ci": [0.9882, 0.9975], "majority_baseline": 0.7151, "lift": 0.2782}
  conclusion: success

=== gradient_masking_qwen7b_seed456 ===
  status: DONE
  hypothesis: Gradient masking seed robustness (seed 456): gradient masking (keeping only top 0.2% gradient signals) on exception_only condition achieves comparable
  metrics: {"accuracy": 0.9933, "pass_precision": 1, "pass_recall": 0.9906, "pass_f1": 0.9953, "fail_precision": 0.9769, "fail_recall": 1, "fail_f1": 0.9883, "n": 1190, "accuracy_ci": [0.9882, 0.9975], "majority_baseline": 0.7151, "lift": 0.2782, "eval_loss": 0.0381, "train_loss": 1.6031}
  conclusion: success

=== qwen7b_full_trace_tail512_seed123 ===
  status: DONE
  hypothesis: Qwen-7B tail-512 seed123 应在 93-97% range（与 full_trace_tail_512_seed42=93.6% 一致），验证 phase transition 后 convergence band 的 seed robustness
  metrics: {"accuracy": 0.9597, "accuracy_ci_lower": 0.9487, "accuracy_ci_upper": 0.9706, "majority_baseline": 0.7151, "lift": 0.2445, "n": 1190, "pass_precision": 0.9751, "pass_recall": 0.9683, "pass_f1": 0.9717, "fail_precision": 0.9217, "fail_recall": 0.9381, "fail_f1": 0.9298, "seed_comparison": {"seed42_accuracy": 0.936, "seed123_accuracy": 0.9597}}
  conclusion: success

=== qwen7b_full_trace_tail512_seed42 ===
  status: DONE
  hypothesis: Qwen-7B tail-512 (硬截断 full_trace_tail_512) 应与原 full_trace_tail seed42 结果 (~93.6%) 接近，确认 condition 差异不影响 budget curve 结论；同时为 cross-seed 提供可比 baseline
  metrics: {}
  conclusion: failed

=== qwen7b_full_trace_tail512_seed456 ===
  status: DONE
  hypothesis: Qwen-7B tail-512 seed456 应在 93-97% range（与 full_trace_tail_512_seed42=93.6% 一致），验证 phase transition 后 convergence band 的 seed robustness
  metrics: {"accuracy": 0.9765, "majority_baseline": 0.7151, "lift": 0.2613, "n": 1190, "pass_precision": 0.9746, "pass_recall": 0.9929, "pass_f1": 0.9837, "fail_precision": 0.9814, "fail_recall": 0.9351, "fail_f1": 0.9577, "accuracy_ci": [0.9681, 0.9849]}
  conclusion: success

=== qwen7b_full_trace_head2048_seed42 ===
  status: DONE
  hypothesis: Qwen-7B head-2048 应在 75-82% (signal-poor convergence band)，与其他 3 模型 head-2048 (75.3-79.9%) 对齐，补全 4 模型 head-tail gap claim
  metrics: {"accuracy_epoch1": 0.816, "accuracy_epoch3": 0.81, "pass_f1_epoch1": 0.87, "fail_f1_epoch1": 0.686, "pass_f1_epoch3": 0.866, "fail_f1_epoch3": 0.674, "best_accuracy": 0.816, "best_epoch": 1}
  conclusion: success

=== qwen7b_full_trace_tail384_seed42 ===
  status: DONE
  hypothesis: Qwen-7B tail-384 应在 85-93% 之间（256→512 phase transition 的中间点），精确定位 phase transition 曲线形状
  metrics: {"accuracy": 0.798, "accuracy_ci_lower": 0.776, "accuracy_ci_upper": 0.821, "majority_baseline": 0.715, "lift": 0.083, "n": 1190, "pass_precision": 0.89, "pass_recall": 0.82, "pass_f1": 0.85, "fail_precision": 0.62, "fail_recall": 0.75, "fail_f1": 0.68}
  conclusion: success

=== qwen7b_exception_only_dynamics_seed42 ===
  status: DONE
  hypothesis: exception_only 因 information density 更高，收敛速度应显著快于 full_trace（即使 full_trace 用 label_only_loss）。通过每 50 steps eval 记录 learning curve 验证。
  metrics: {"step50_acc": 0.9933, "step100_acc": 0.9933, "step150_acc": 0.9933, "step200_acc": 0.9983, "step250_acc": 0.9983, "step300_acc": 0.9983, "step350_acc": 0.9983, "step400_acc": 0.9983, "step444_acc": 0.9983, "saturation_step": 200, "final_loss": 0.0329, "pass_f1": 0.9988, "fail_f1": 0.9971}
  conclusion: success

=== qwen7b_full_trace_dynamics_seed42 ===
  status: DONE
  hypothesis: full_trace (label_only_loss) 收敛速度应慢于 exception_only，因 trace 中冗余信息稀释了有效 signal density。通过每 50 steps eval 记录 learning curve 验证。
  metrics: {"step50_acc": 0.8739, "step100_acc": 0.821, "step150_acc": 0.8571, "step200_acc": 0.8655, "step250_acc": 0.8739, "step300_acc": 0.8487, "step350_acc": 0.8882, "step400_acc": 0.8571, "step444_acc": 0.8824, "best_step": 350, "best_acc": 0.8882, "final_loss": 0.0085}
  conclusion: success
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf50cbb9-79ae-4348-a189-92a84f7fd728",
  "isSidechain": true,
  "promptId": "83fb8b21-6186-4214-9116-e4c59eb31db2",
  "agentId": "ad4eda51cd882ef4e",
  "type": "user",
  "uuid": "d8245601-4060-4bd9-8f01-8c156f980415",
  "sourceToolAssistantUUID": "bf50cbb9-79ae-4348-a189-92a84f7fd728",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "d5f32b76-3066-49a9-b711-4657d91efad8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T19:19:12.435Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Mz7V1CuGMJqYspjbSvQLs2`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# DeepSeek and Qwen-1.5B and CodeLlama cross-model experiments\ncross_model_ids = [\n    'deepseek_exception_only_seed42', 'deepseek_exception_only_seed123', 'deepseek_exception_only_seed123_v2',\n    'deepseek_exception_only_seed456',\n    'deepseek_full_trace_seed42', 'deepseek_full_trace_seed42_v2', 'deepseek_full_trace_seed42_v3',\n    'deepseek_full_trace_tail512_seed42', 'deepseek_full_trace_tail512_seed123', 'deepseek_full_trace_tail512_seed123_v2', \n    'deepseek_full_trace_tail512_seed456',\n    'deepseek_no_trace_seed42', 'deepseek_no_trace_seed123',\n    'deepseek_vota_seed42', 'deepseek_vota_seed123', 'deepseek_vota_seed456',\n    'deepseek_ae_only_seed42', 'deepseek_ae_only_seed123',\n    'deepseek_loop_only_seed42', 'deepseek_loop_only_seed123', 'deepseek_loop_only_seed456',\n    'deepseek_label_only_seed42',\n    # CodeLlama\n    'codellama13b_exception_only_seed42', 'codellama13b_exception_only_seed123', 'codellama13b_exception_only_seed456',\n    'codellama13b_full_trace_tail512_seed42', 'codellama13b_full_trace_tail512_seed123', 'codellama13b_full_trace_tail512_seed456',\n    'codellama13b_full_trace_tail1024_seed42', 'codellama13b_full_trace_tail2048_seed42',\n    'codellama13b_no_trace_seed42',\n    'codellama13b_vota_seed42', 'codellama13b_vota_seed123',\n    'codellama13b_ae_only_seed42', 'codellama13b_ae_only_seed123',\n    'codellama13b_loop_only_seed42', 'codellama13b_loop_only_seed123', 'codellama13b_loop_only_seed456',\n    'codellama13b_label_only_seed42', 'codellama13b_label_only_seed42_v2', 'codellama13b_label_only_seed123_v2',\n    # Qwen-1.5B\n    'qwen15b_exception_only_seed42', 'qwen15b_exception_only_seed123', 'qwen15b_exception_only_seed123_v2',\n    'qwen15b_exception_only_seed456',\n    'qwen15b_full_trace_seed42',\n    'qwen15b_full_trace_tail512_seed42', 'qwen15b_full_trace_tail512_seed123', 'qwen15b_full_trace_tail512_seed456',\n    'qwen15b_no_trace_seed42', 'qwen15b_no_trace_seed123', 'qwen15b_no_trace_seed456',\n    'qwen15b_vota_seed42', 'qwen15b_vota_seed123',\n    'qwen15b_ae_only_seed42', 'qwen15b_ae_only_seed123',\n    'qwen15b_loop_only_seed42', 'qwen15b_loop_only_seed123', 'qwen15b_loop_only_seed456',\n    'qwen15b_label_only_seed42', 'qwen15b_label_only_seed42_v2', 'qwen15b_label_only_seed123_v2', 'qwen15b_label_only_seed456_v2',\n]\n\nfor eid in cross_model_ids:\n    if eid in experiments:\n        exp = experiments[eid]\n        print(f\"\\n=== {eid} ===\")\n        print(f\"  status: {exp.get('status')}\")\n        m = exp.get('metrics', {})\n        # Only print key metrics\n        key_metrics = {k: v for k, v in m.items() if k in [\n            'accuracy', 'accuracy_ci', 'accuracy_ci_lower', 'accuracy_ci_upper', 'ci_lower', 'ci_upper', 'ci_95',\n            'majority_baseline', 'lift', 'n', 'pass_f1', 'fail_f1', 'seed_comparison', 'mean_accuracy', 'std'\n        ]}\n        print(f\"  key_metrics: {json.dumps(key_metrics)}\")\n        print(f\"  conclusion: {exp.get('conclusion')}\")\nPYEOF\n",
  "description": "Extract metrics for cross-model experiments (DeepSeek, Qwen-1.5B, CodeLlama)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8245601-4060-4bd9-8f01-8c156f980415",
  "isSidechain": true,
  "agentId": "ad4eda51cd882ef4e",
  "requestId": "req_011CbL3Hp4CcFgqM9Ls3avTL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7e5723cc-3cec-4997-9007-a22aee3ef618",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "d5f32b76-3066-49a9-b711-4657d91efad8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EJSeCafo8j5xWQwkfS3vJd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4209,
      "cache_read_input_tokens": 36135,
      "output_tokens": 1502,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4209
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1502,
          "cache_read_input_tokens": 36135,
          "cache_creation_input_tokens": 4209,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4209,
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

_source line 22 · 2026-05-23T19:19:12.575Z_

<details><summary>↩ Tool result · `toolu_01Mz7V1CuGMJqYspjbSvQLs2`</summary>

```text
=== deepseek_exception_only_seed42 ===
  status: DONE
  key_metrics: {"accuracy": 0.9933, "majority_baseline": 0.7151, "lift": 0.2782, "n": 1190, "pass_f1": 0.9953, "fail_f1": 0.9883}
  conclusion: success

=== deepseek_exception_only_seed123 ===
  status: DONE
  key_metrics: {}
  conclusion: killed

=== deepseek_exception_only_seed123_v2 ===
  status: DONE
  key_metrics: {"accuracy": 0.995}
  conclusion: success

=== deepseek_exception_only_seed456 ===
  status: DONE
  key_metrics: {"accuracy": 0.9933, "majority_baseline": 0.7151, "lift": 0.2782, "n": 1190, "pass_f1": 0.9953, "fail_f1": 0.9883, "accuracy_ci": [0.9882, 0.9975], "seed_comparison": {"seed42_accuracy": 0.9933, "seed456_accuracy": 0.9933, "seed123_accuracy": 0.9109, "note": "seed42 and seed456 identical (99.33%); seed123 outlier (91.09%). 2/3 seeds robust."}}
  conclusion: success

=== deepseek_full_trace_seed42 ===
  status: DONE
  key_metrics: {"majority_baseline": 0.7151, "n": 1190}
  conclusion: negative

=== deepseek_full_trace_seed42_v2 ===
  status: DONE
  key_metrics: {}
  conclusion: killed

=== deepseek_full_trace_seed42_v3 ===
  status: DONE
  key_metrics: {"accuracy": 0.7916, "majority_baseline": 0.7151, "lift": 0.0765, "n": 1190, "pass_f1": 0.854, "fail_f1": 0.637, "accuracy_ci": [0.768, 0.813]}
  conclusion: success

=== deepseek_full_trace_tail512_seed42 ===
  status: DONE
  key_metrics: {"accuracy": 0.939, "accuracy_ci_lower": 0.926, "accuracy_ci_upper": 0.953, "majority_baseline": 0.715, "pass_f1": 0.96, "fail_f1": 0.9}
  conclusion: success

=== deepseek_full_trace_tail512_seed123 ===
  status: DONE
  key_metrics: {"seed_comparison": {"seed42_accuracy": 0.9361, "seed123_accuracy": "N/A - OOM crash"}}
  conclusion: failed

=== deepseek_full_trace_tail512_seed123_v2 ===
  status: DONE
  key_metrics: {"accuracy": 0.9504, "majority_baseline": 0.7151, "lift": 0.2353, "n": 1190, "pass_f1": 0.9649, "fail_f1": 0.9154, "accuracy_ci": [0.9387, 0.963]}
  conclusion: success

=== deepseek_full_trace_tail512_seed456 ===
  status: DONE
  key_metrics: {"accuracy": 0.9605, "accuracy_ci_lower": 0.9496, "accuracy_ci_upper": 0.9714, "majority_baseline": 0.7151, "lift": 0.2454, "n": 1190, "pass_f1": 0.9723, "fail_f1": 0.9312, "seed_comparison": {"seed42_accuracy": 0.9361, "seed456_accuracy": 0.9605}}
  conclusion: success

=== deepseek_no_trace_seed42 ===
  status: DONE
  key_metrics: {"accuracy": 0.7336, "majority_baseline": 0.7151, "lift": 0.0185, "n": 1190, "pass_f1": 0.813, "fail_f1": 0.539, "accuracy_ci": [0.708, 0.757]}
  conclusion: negative

=== deepseek_no_trace_seed123 ===
  status: DONE
  key_metrics: {}
  conclusion: killed

=== deepseek_vota_seed42 ===
  status: DONE
  key_metrics: {"accuracy": 0.8445, "majority_baseline": 0.7151, "lift": 0.1294, "accuracy_ci": [0.826, 0.864], "pass_f1": 0.902, "fail_f1": 0.625}
  conclusion: success

=== deepseek_vota_seed123 ===
  status: DONE
  key_metrics: {"accuracy": 0.9916, "accuracy_ci_lower": 0.9857, "accuracy_ci_upper": 0.9966}
  conclusion: success

=== deepseek_vota_seed456 ===
  status: DONE
  key_metrics: {"accuracy": 0.9933}
  conclusion: success

=== deepseek_ae_only_seed42 ===
  status: DONE
  key_metrics: {"accuracy": 0.9874, "accuracy_ci_lower": 0.9807, "accuracy_ci_upper": 0.9933, "fail_f1": 0.977, "pass_f1": 0.991}
  conclusion: success

=== deepseek_ae_only_seed123 ===
  status: DONE
  key_metrics: {"accuracy": 0.9832}
  conclusion: success

=== deepseek_loop_only_seed42 ===
  status: DONE
  key_metrics: {"accuracy": 0.8126, "accuracy_ci_lower": 0.7908, "accuracy_ci_upper": 0.8345}
  conclusion: success

=== deepseek_loop_only_seed123 ===
  status: DONE
  key_metrics: {"accuracy": 0.8126, "accuracy_ci_lower": 0.792, "accuracy_ci_upper": 0.834}
  conclusion: success

=== deepseek_loop_only_seed456 ===
  status: DONE
  key_metrics: {"accuracy": 0.784, "majority_baseline": 0.715, "fail_f1": 0.63}
  conclusion: success

=== deepseek_label_only_seed42 ===
  status: DONE
  key_metrics: {"accuracy": 0.285, "accuracy_ci_lower": 0.261, "accuracy_ci_upper": 0.308, "majority_baseline": 0.7151, "lift": -0.43, "pass_f1": 0, "fail_f1": 0.44}
  conclusion: negative

=== codellama13b_exception_only_seed42 ===
  status: DONE
  key_metrics: {"accuracy": 0.9983, "accuracy_ci_lower": 0.9958, "accuracy_ci_upper": 1, "pass_f1": 0.9988, "fail_f1": 0.9971}
  conclusion: success

=== codellama13b_exception_only_seed123 ===
  status: DONE
  key_metrics: {"accuracy": 1, "n": 1190, "pass_f1": 1, "fail_f1": 1}
  conclusion: success

=== codellama13b_exception_only_seed456 ===
  status: DONE
  key_metrics: {"accuracy": 0.9983, "n": 1190, "pass_f1": 0.9988, "fail_f1": 0.9971}
  conclusion: success

=== codellama13b_full_trace_tail512_seed42 ===
  status: DONE
  key_metrics: {"accuracy": 0.9824, "accuracy_ci_lower": 0.9748, "accuracy_ci_upper": 0.9899, "majority_baseline": 0.7151, "lift": 0.2672, "n": 1190, "pass_f1": 0.9878, "fail_f1": 0.968}
  conclusion: success

=== codellama13b_full_trace_tail512_seed123 ===
  status: DONE
  key_metrics: {"accuracy": 0.9824, "accuracy_ci_lower": 0.9748, "accuracy_ci_upper": 0.9899, "majority_baseline": 0.7151, "lift": 0.2672, "n": 1190, "pass_f1": 0.9878, "fail_f1": 0.968, "seed_comparison": {"seed42_accuracy": 0.975, "seed123_accuracy": 0.9824, "diff": 0.0074, "note": "seed123 (98.24%) slightly exceeds seed42 (97.5%); both well above 97% \u2014 CodeLlama-13B tail-512 seed-robust"}}
  conclusion: success

=== codellama13b_full_trace_tail512_seed456 ===
  status: DONE
  key_metrics: {"accuracy": 0.9824, "accuracy_ci_lower": 0.9748, "accuracy_ci_upper": 0.9899, "majority_baseline": 0.7151, "lift": 0.2672, "n": 1190, "pass_f1": 0.9878, "fail_f1": 0.968, "seed_comparison": {"seed42_previous": 0.975, "seed123_accuracy": 0.9824, "seed456_accuracy": 0.9824}}
  conclusion: success

=== codellama13b_full_trace_tail1024_seed42 ===
  status: DONE
  key_metrics: {}
  conclusion: failed

=== codellama13b_full_trace_tail2048_seed42 ===
  status: DONE
  key_metrics: {}
  conclusion: failed

=== codellama13b_no_trace_seed42 ===
  status: DONE
  key_metrics: {"accuracy": 0.765, "n": 1190, "majority_baseline": 0.7151, "lift": 0.05, "pass_f1": 0.84, "fail_f1": 0.59, "accuracy_ci_lower": 0.738, "accuracy_ci_upper": 0.787}
  conclusion: success

=== codellama13b_vota_seed42 ===
  status: DONE
  key_metrics: {"accuracy": 0.9857, "accuracy_ci_lower": 0.979, "accuracy_ci_upper": 0.9916, "pass_f1": 0.99, "fail_f1": 0.9748}
  conclusion: success

=== codellama13b_vota_seed123 ===
  status: DONE
  key_metrics: {"accuracy": 0.9891, "accuracy_ci": [0.9832, 0.9941], "pass_f1": 0.9924, "fail_f1": 0.9809, "n": 1190, "majority_baseline": 0.7151, "lift": 0.2739}
  conclusion: success

=== codellama13b_ae_only_seed42 ===
  status: DONE
  key_metrics: {"accuracy": 0.9908, "accuracy_ci_lower": 0.9849, "accuracy_ci_upper": 0.9958, "pass_f1": 0.9935, "fail_f1": 0.984, "majority_baseline": 0.7151}
  conclusion: success

=== codellama13b_ae_only_seed123 ===
  status: DONE
  key_metrics: {"accuracy": 0.9908, "accuracy_ci_lower": 0.9849, "accuracy_ci_upper": 0.9958, "pass_f1": 0.993, "fail_f1": 0.984}
  conclusion: success

=== codellama13b_loop_only_seed42 ===
  status: DONE
  key_metrics: {"accuracy": 0.7706, "accuracy_ci_lower": 0.7487, "accuracy_ci_upper": 0.7941, "n": 1190, "majority_baseline": 0.7151, "lift": 0.0555, "pass_f1": 0.82, "fail_f1": 0.67}
  conclusion: negative

=== codellama13b_loop_only_seed123 ===
  status: DONE
  key_metrics: {"accuracy": 0.7605, "accuracy_ci_lower": 0.7387, "accuracy_ci_upper": 0.7857, "pass_f1": 0.8078, "fail_f1": 0.6823, "majority_baseline": 0.7151, "lift": 0.0454, "n": 1190}
  conclusion: success

=== codellama13b_loop_only_seed456 ===
  status: DONE
  key_metrics: {"accuracy": 0.7908, "majority_baseline": 0.7151, "lift": 0.0757, "pass_f1": 0.843, "fail_f1": 0.688, "n": 1190}
  conclusion: success

=== codellama13b_label_only_seed42 ===
  status: DONE
  key_metrics: {}
  conclusion: killed

=== codellama13b_label_only_seed42_v2 ===
  status: DONE
  key_metrics: {"accuracy": 0.2849, "accuracy_ci_lower": 0.2613, "accuracy_ci_upper": 0.3084, "majority_baseline": 0.7151, "pass_f1": 0, "fail_f1": 0.4434}
  conclusion: negative

=== codellama13b_label_only_seed123_v2 ===
  status: DONE
  key_metrics: {"accuracy": "collapsed"}
  conclusion: success

=== qwen15b_exception_only_seed42 ===
  status: DONE
  key_metrics: {"accuracy": 0.9983, "accuracy_ci_lower": 0.9958, "accuracy_ci_upper": 1, "majority_baseline": 0.7151, "lift": 0.283, "n": 1190, "pass_f1": 0.9988, "fail_f1": 0.9971}
  conclusion: success

=== qwen15b_exception_only_seed123 ===
  status: DONE
  key_metrics: {"seed_comparison": {"seed42_accuracy": 0.9983, "seed123_accuracy": "N/A - OOM crash"}}
  conclusion: failed

=== qwen15b_exception_only_seed123_v2 ===
  status: DONE
  key_metrics: {"accuracy": 0.9983, "accuracy_ci_lower": 0.9958, "accuracy_ci_upper": 1, "seed_comparison": {"seed42_accuracy": 0.9983, "seed456_accuracy": 0.9983, "seed123_accuracy": 0.9983}}
  conclusion: success

=== qwen15b_exception_only_seed456 ===
  status: DONE
  key_metrics: {"accuracy": 0.9983, "accuracy_ci_lower": 0.9958, "accuracy_ci_upper": 1, "majority_baseline": 0.7151, "lift": 0.2832, "n": 1190, "pass_f1": 0.9988, "fail_f1": 0.9971, "seed_comparison": {"seed42_accuracy": 0.9983, "seed456_accuracy": 0.9983, "diff": 0, "note": "Identical to seed42 to 4 decimal places \u2014 exception_only fully seed-robust on Qwen-1.5B"}}
  conclusion: success

=== qwen15b_full_trace_seed42 ===
  status: DONE
  key_metrics: {"accuracy": 0.7706, "n": 1190}
  conclusion: success

=== qwen15b_full_trace_tail512_seed42 ===
  status: DONE
  key_metrics: {"accuracy": 0.956, "accuracy_ci_lower": 0.945, "accuracy_ci_upper": 0.968, "majority_baseline": 0.715, "pass_f1": 0.97, "fail_f1": 0.92}
  conclusion: success

=== qwen15b_full_trace_tail512_seed123 ===
  status: DONE
  key_metrics: {"accuracy": 0.9765, "accuracy_ci_lower": 0.9681, "accuracy_ci_upper": 0.9849, "majority_baseline": 0.7151, "lift": 0.2613, "n": 1190, "pass_f1": 0.9837, "fail_f1": 0.9578, "seed_comparison": {"seed42_accuracy": 0.956, "seed123_accuracy": 0.9765, "note": "seed123 (97.65%) exceeds seed42 (95.6%) by 2pp; both in convergence band post-phase-transition"}}
  conclusion: success

=== qwen15b_full_trace_tail512_seed456 ===
  status: DONE
  key_metrics: {"accuracy": 0.9672, "accuracy_ci_lower": 0.9563, "accuracy_ci_upper": 0.9773, "majority_baseline": 0.7151, "lift": 0.2521, "n": 1190, "pass_f1": 0.9771, "fail_f1": 0.9424, "seed_comparison": {"seed42_accuracy": 0.956, "seed123_accuracy": 0.9765, "seed456_accuracy": 0.9672, "note": "seed456 (96.72%) within convergence band [95.6%, 97.65%], confirming seed robustness post-phase-transition"}}
  conclusion: success

=== qwen15b_no_trace_seed42 ===
  status: DONE
  key_metrics: {"accuracy": 0.6731, "n": 1190, "pass_f1": 0.7527, "fail_f1": 0.518}
  conclusion: success

=== qwen15b_no_trace_seed123 ===
  status: DONE
  key_metrics: {"accuracy": 0.7588, "accuracy_ci_lower": 0.7328, "accuracy_ci_upper": 0.7824, "majority_baseline": 0.7151, "lift": 0.0437, "pass_f1": 0.8323, "fail_f1": 0.571}
  conclusion: success

=== qwen15b_no_trace_seed456 ===
  status: DONE
  key_metrics: {"accuracy": 0.7387, "fail_f1": 0.5266, "pass_f1": 0.8195}
  conclusion: success

=== qwen15b_vota_seed42 ===
  status: DONE
  key_metrics: {"accuracy": 0.9958, "n": 1190, "pass_f1": 0.9971, "fail_f1": 0.9926}
  conclusion: success

=== qwen15b_vota_seed123 ===
  status: DONE
  key_metrics: {"accuracy": 0.995, "ci_95": [0.9908, 0.9983], "pass_f1": 0.9965, "fail_f1": 0.9912}
  conclusion: success

=== qwen15b_ae_only_seed42 ===
  status: DONE
  key_metrics: {"accuracy": 0.9908, "majority_baseline": 0.7151, "lift": 0.2756, "pass_f1": 0.9935, "fail_f1": 0.984, "n": 1190, "accuracy_ci_lower": 0.9849, "accuracy_ci_upper": 0.9958}
  conclusion: success

=== qwen15b_ae_only_seed123 ===
  status: DONE
  key_metrics: {"accuracy": 0.9857, "majority_baseline": 0.715, "fail_f1": 0.975}
  conclusion: success

=== qwen15b_loop_only_seed42 ===
  status: DONE
  key_metrics: {"accuracy": 0.7832, "pass_f1": 0.8526, "fail_f1": 0.5905}
  conclusion: success

=== qwen15b_loop_only_seed123 ===
  status: DONE
  key_metrics: {"accuracy": 0.8109, "pass_f1": 0.8737, "fail_f1": 0.6244}
  conclusion: success

=== qwen15b_loop_only_seed456 ===
  status: DONE
  key_metrics: {"accuracy": 0.792, "ci_95": [0.768, 0.813], "majority_baseline": 0.715, "pass_f1": 0.86, "fail_f1": 0.63}
  conclusion: success

=== qwen15b_label_only_seed42 ===
  status: DONE
  key_metrics: {}
  conclusion: killed

=== qwen15b_label_only_seed42_v2 ===
  status: DONE
  key_metrics: {"accuracy": 0.789, "accuracy_ci_lower": 0.766, "accuracy_ci_upper": 0.812, "majority_baseline": 0.715, "pass_f1": 0.86, "fail_f1": 0.57}
  conclusion: success

=== qwen15b_label_only_seed123_v2 ===
  status: DONE
  key_metrics: {"accuracy": 0.8134, "accuracy_ci_lower": 0.7924, "accuracy_ci_upper": 0.8345, "majority_baseline": 0.7151, "pass_f1": 0.878, "fail_f1": 0.602}
  conclusion: success

=== qwen15b_label_only_seed456_v2 ===
  status: DONE
  key_metrics: {"accuracy": 0.8252, "pass_f1": 0.885, "fail_f1": 0.639, "majority_baseline": 0.715}
  conclusion: success
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e5723cc-3cec-4997-9007-a22aee3ef618",
  "isSidechain": true,
  "promptId": "83fb8b21-6186-4214-9116-e4c59eb31db2",
  "agentId": "ad4eda51cd882ef4e",
  "type": "user",
  "uuid": "f6a58bed-1757-4556-b756-7e85ac0be9c6",
  "sourceToolAssistantUUID": "7e5723cc-3cec-4997-9007-a22aee3ef618",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "d5f32b76-3066-49a9-b711-4657d91efad8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T19:19:33.118Z_

<details open><summary>🔧 Tool call — Bash · `toolu_015S8aP4Rp3MbDrJYtczmKW8`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# nomarker experiments, ablation density/trace length, debugbench, fewshot, attention analysis\nremaining_ids = [\n    'exception_only_nomarker_seed42', 'exception_only_nomarker_seed123', 'exception_only_nomarker_seed456',\n    'codellama13b_nomarker_seed42', 'qwen15b_nomarker_seed42',\n    # trace length ablations (Qwen-7B)\n    'full_trace_256tok_seed42', 'full_trace_512tok_seed42', 'full_trace_1024tok_seed42', 'full_trace_2048tok_seed42',\n    'full_trace_tail256_seed42', 'full_trace_tail_256_seed42', 'full_trace_tail_512_seed42', 'full_trace_tail_1024_seed42',\n    'full_trace_tail_seed42', 'full_trace_tail256_seed42',\n    'deepseek_full_trace_tail256_seed42', 'deepseek_full_trace_tail384_seed42', \n    'deepseek_full_trace_tail1024_seed42', 'deepseek_full_trace_tail2048_seed42', 'deepseek_full_trace_head2048_seed42',\n    'codellama13b_full_trace_tail256_seed42', 'codellama13b_full_trace_tail384_seed42',\n    'codellama13b_full_trace_tail2048_seed42', 'codellama13b_full_trace_tail2048_seed42_v2', 'codellama13b_full_trace_tail2048_seed42_v3',\n    'codellama13b_full_trace_tail1024_seed42', 'codellama13b_full_trace_tail1024_seed42_v2', 'codellama13b_full_trace_tail1024_seed42_v3',\n    'codellama13b_full_trace_head2048_seed42',\n    'qwen15b_full_trace_tail256_seed42', 'qwen15b_full_trace_tail384_seed42',\n    'qwen15b_full_trace_tail1024_seed42', 'qwen15b_full_trace_tail2048_seed42', 'qwen15b_full_trace_head2048_seed42',\n    # debugbench, fewshot\n    'debugbench_exception_only_seed42', 'debugbench_no_trace_seed42', 'debugbench_vota_seed42', 'debugbench_exception_bug_fix',\n    'fewshot_gpt4o_exception_only_0shot', 'fewshot_gpt4o_exception_only_3shot', 'fewshot_gpt4o_no_trace_0shot',\n    'fewshot_gpt41_exception_only_0shot', 'fewshot_gpt41_exception_only_3shot', 'fewshot_gpt41_no_trace_0shot',\n    'fewshot_qwen7b_exception_only',\n    # attention / misc\n    'attention_gradient_analysis',\n    'zeroshot_codellama13b_exception_only', 'zeroshot_deepseek7b_exception_only',\n    'zeroshot_qwen15b_exception_only', 'zeroshot_qwen7b_exception_only',\n    'qwen1.5b_exception_only_seed42', 'qwen1.5b_full_trace_seed42', 'qwen1.5b_no_trace_seed42', 'qwen1.5b_vota_seed42',\n    'codellama_exception_only_seed42', 'codellama_no_trace_seed42', 'codellama_vota_seed42',\n    'eval_missing_predictions_batch', 'eval_missing_predictions_batch_v2',\n]\n\nfor eid in remaining_ids:\n    if eid in experiments:\n        exp = experiments[eid]\n        print(f\"\\n=== {eid} ===\")\n        print(f\"  status: {exp.get('status')}\")\n        print(f\"  hypothesis: {exp.get('hypothesis', '')[:150]}\")\n        print(f\"  metrics: {json.dumps(exp.get('metrics', {}))}\")\n        print(f\"  conclusion: {exp.get('conclusion')}\")\nPYEOF\n",
  "description": "Extract remaining experiments including nomarker, trace length, fewshot, debugbench"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6a58bed-1757-4556-b756-7e85ac0be9c6",
  "isSidechain": true,
  "agentId": "ad4eda51cd882ef4e",
  "requestId": "req_011CbL3KCYafwWy94hBtQPSr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6116341e-1965-4fac-aa1b-800f99e99650",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "d5f32b76-3066-49a9-b711-4657d91efad8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_018EV7oMzVL7kNynSMPRBqh2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7281,
      "cache_read_input_tokens": 40344,
      "output_tokens": 1355,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7281
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1355,
          "cache_read_input_tokens": 40344,
          "cache_creation_input_tokens": 7281,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7281,
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

_source line 24 · 2026-05-23T19:19:33.223Z_

<details><summary>↩ Tool result · `toolu_015S8aP4Rp3MbDrJYtczmKW8`</summary>

```text
=== exception_only_nomarker_seed42 ===
  status: DONE
  hypothesis: Format marker ablation: removing [No exception data in trace] and [ERROR] prefix markers reduces accuracy by ~2pp, isolating semantic content contribu
  metrics: {"accuracy": 0.9655, "n": 1190, "accuracy_ci": [0.955, 0.976]}
  conclusion: success

=== exception_only_nomarker_seed123 ===
  status: DONE
  hypothesis: Seed robustness of nomarker ablation: format marker contribution (~2pp) is consistent across random seeds, not an artifact of specific LoRA initializa
  metrics: {"accuracy": 0.9832, "n": 1190, "ci_95": [0.9756, 0.9899], "pass_f1": 0.9882, "fail_f1": 0.9705, "pass_precision": 0.9882, "pass_recall": 0.9882, "fail_precision": 0.9705, "fail_recall": 0.9705, "lift_over_majority": 0.2681}
  conclusion: success

=== exception_only_nomarker_seed456 ===
  status: DONE
  hypothesis: Seed robustness of nomarker ablation: format marker contribution (~2pp) is consistent across random seeds, not an artifact of specific LoRA initializa
  metrics: {"accuracy": 0.9807, "n": 1190, "errors": 23, "ci_95": [0.9712, 0.9871], "pass_f1": 0.9865, "fail_f1": 0.9658, "pass_precision": 0.9836, "pass_recall": 0.9894, "fail_precision": 0.9731, "fail_recall": 0.9587, "lift_over_majority": 0.266}
  conclusion: success

=== codellama13b_nomarker_seed42 ===
  status: DONE
  hypothesis: Cross-architecture marker contribution: format markers ([No exception data in trace], [ERROR] prefix) contribute ~2pp on CodeLlama-13B as on Qwen fami
  metrics: {}
  conclusion: killed

=== qwen15b_nomarker_seed42 ===
  status: DONE
  hypothesis: Cross-scale nomarker validation: format marker contribution (~2pp at 7B) is consistent at 1.5B, confirming markers provide a small but architecture-an
  metrics: {"accuracy": 0.978, "n": 1190, "accuracy_ci": [0.97, 0.986], "majority_baseline": 0.715, "lift": 0.263, "pass_precision": 0.97, "pass_recall": 1, "pass_f1": 0.98, "fail_precision": 1, "fail_recall": 0.92, "fail_f1": 0.96}
  conclusion: success

=== full_trace_256tok_seed42 ===
  status: DONE
  hypothesis: Token budget ablation (256 tokens): severely truncated full trace loses most diagnostic events, yielding accuracy near no-trace baseline because criti
  metrics: {"accuracy": 0.7882, "majority_baseline": 0.7151, "lift": 0.0731, "n": 1190, "pass_precision": 0.903, "pass_recall": 0.788, "pass_f1": 0.842, "fail_precision": 0.597, "fail_recall": 0.788, "fail_f1": 0.679, "accuracy_ci": [0.764, 0.81], "train_loss": 0.1094, "train_runtime_sec": 3047, "epochs": 3}
  conclusion: negative

=== full_trace_512tok_seed42 ===
  status: DONE
  hypothesis: Token budget ablation (512 tokens): moderate truncation retains some diagnostic events but still loses critical tail information, yielding accuracy be
  metrics: {"accuracy": 0.8042, "majority_baseline": 0.7151, "lift": 0.0891, "pass_precision": 0.8705, "pass_recall": 0.8531, "pass_f1": 0.8617, "fail_precision": 0.6489, "fail_recall": 0.6814, "fail_f1": 0.6647, "n": 1190, "accuracy_ci": [0.7815, 0.8261]}
  conclusion: negative

=== full_trace_1024tok_seed42 ===
  status: DONE
  hypothesis: Token budget ablation (1024 tokens): near-full trace budget should approach no-limit accuracy (~81.76%), testing whether the last few hundred tokens c
  metrics: {"accuracy": 0.7723, "majority_baseline": 0.7151, "lift": 0.0571, "n": 1190, "accuracy_ci": [0.7487, 0.7958], "pass_precision": 0.9006, "pass_recall": 0.7662, "pass_f1": 0.8279, "fail_precision": 0.573, "fail_recall": 0.7876, "fail_f1": 0.6634, "train_loss": 0.0634, "train_runtime_sec": 5553, "epochs": 3}
  conclusion: negative

=== full_trace_2048tok_seed42 ===
  status: DONE
  hypothesis: 
  metrics: {}
  conclusion: killed

=== full_trace_tail256_seed42 ===
  status: DONE
  hypothesis: Tail-256 truncation (keeping last 256 tokens of execution trace) still provides sufficient signal for verdict prediction, extending the budget curve b
  metrics: {"accuracy": 0.789, "accuracy_ci_lower": 0.765, "accuracy_ci_upper": 0.813, "pass_f1": 0.845, "fail_f1": 0.671, "n_test": 1190}
  conclusion: negative

=== full_trace_tail_256_seed42 ===
  status: DONE
  hypothesis: Tail-256 token budget: tests if diagnostic signal is concentrated in the last 256 tokens. If tail-256 approaches tail-512 (93.6%), signal is extremely
  metrics: {"accuracy": 0.7748, "accuracy_ci": [0.7496, 0.7975], "majority_baseline": 0.7151, "lift": 0.0597, "n": 1190, "pass_f1": 0.8333, "fail_f1": 0.6528}
  conclusion: negative

=== full_trace_tail_512_seed42 ===
  status: DONE
  hypothesis: Tail-truncation token budget: if tail-2048 >> head-2048, tail-512 reveals how concentrated the signal is. tail-512 ≈ tail-2048 means signal is in last
  metrics: {"accuracy": 0.936, "accuracy_ci": [0.922, 0.95], "majority_baseline": 0.7151, "lift": 0.221, "n": 1190, "pass_precision": 0.98, "pass_recall": 0.93, "pass_f1": 0.95, "fail_precision": 0.85, "fail_recall": 0.94, "fail_f1": 0.89}
  conclusion: success

=== full_trace_tail_1024_seed42 ===
  status: DONE
  hypothesis: Tail-1024 token budget: tests diminishing returns of tail context. If tail-1024 approaches tail-2048 (97.3%), 1024 tokens already captures nearly all 
  metrics: {"accuracy": 0.9647, "accuracy_ci": [0.9546, 0.9748], "majority_baseline": 0.7151, "lift": 0.2496, "n": 1190, "pass_f1": 0.9753, "fail_f1": 0.9381}
  conclusion: success

=== full_trace_tail_seed42 ===
  status: DONE
  hypothesis: Tail-truncation baseline: keeping the last 2048 tokens of full trace (where exception events concentrate) should significantly outperform head-truncat
  metrics: {"accuracy": 0.973, "accuracy_ci": [0.964, 0.982], "majority_baseline": 0.7151, "lift": 0.258, "n": 1190, "pass_precision": 0.98, "pass_recall": 0.99, "pass_f1": 0.98, "fail_precision": 0.97, "fail_recall": 0.94, "fail_f1": 0.95}
  conclusion: success

=== full_trace_tail256_seed42 ===
  status: DONE
  hypothesis: Tail-256 truncation (keeping last 256 tokens of execution trace) still provides sufficient signal for verdict prediction, extending the budget curve b
  metrics: {"accuracy": 0.789, "accuracy_ci_lower": 0.765, "accuracy_ci_upper": 0.813, "pass_f1": 0.845, "fail_f1": 0.671, "n_test": 1190}
  conclusion: negative

=== deepseek_full_trace_tail256_seed42 ===
  status: DONE
  hypothesis: DeepSeek tail-256 应在 75-82% 范围（与 Qwen-7B tail-256=78.9% 类似），确认 256-512 phase transition 是 architecture-independent
  metrics: {"accuracy": 0.7639, "accuracy_ci_lower": 0.7403, "accuracy_ci_upper": 0.7874, "pass_precision": 0.8058, "pass_recall": 0.8825, "pass_f1": 0.8424, "fail_precision": 0.6124, "fail_recall": 0.4661, "fail_f1": 0.5293, "majority_baseline": 0.7151, "lift": 0.0487, "eval_loss": 0.5117, "train_loss": 0.2367}
  conclusion: success

=== deepseek_full_trace_tail384_seed42 ===
  status: DONE
  hypothesis: DeepSeek-6.7B tail-384 应在 85-93% 之间（256→512 phase transition 的中间点），精确定位 phase transition 曲线形状
  metrics: {"accuracy": 0.807, "accuracy_ci_lower": 0.786, "accuracy_ci_upper": 0.829, "majority_baseline": 0.715, "lift": 0.092, "n": 1190, "pass_precision": 0.83, "pass_recall": 0.92, "pass_f1": 0.87, "fail_precision": 0.73, "fail_recall": 0.51, "fail_f1": 0.6}
  conclusion: success

=== deepseek_full_trace_tail1024_seed42 ===
  status: DONE
  hypothesis: DeepSeek tail-1024 可能低于 tail-512（如同 Qwen-7B non-monotonicity），因为 1024 tokens 包含了 noisy intermediate states；如果也出现 non-monotonicity 则确认跨架构
  metrics: {"accuracy": 0.9647, "accuracy_ci_lower": 0.9538, "accuracy_ci_upper": 0.9748, "pass_precision": 0.964, "pass_recall": 0.987, "pass_f1": 0.976, "fail_precision": 0.966, "fail_recall": 0.909, "fail_f1": 0.936, "majority_baseline": 0.7151, "n_test": 1190}
  conclusion: success

=== deepseek_full_trace_tail2048_seed42 ===
  status: DONE
  hypothesis: Tail-truncation signal concentration hypothesis generalizes across architectures: DeepSeek-Coder-6.7B with tail-2048 truncation should achieve accurac
  metrics: {"accuracy": 0.9496, "accuracy_ci_lower": 0.937, "accuracy_ci_upper": 0.9622, "pass_precision": 0.9692, "pass_recall": 0.96, "pass_f1": 0.9646, "fail_precision": 0.902, "fail_recall": 0.9233, "fail_f1": 0.9125, "n_test": 1190}
  conclusion: success

=== deepseek_full_trace_head2048_seed42 ===
  status: DONE
  hypothesis: Cross-architecture head-truncation: DeepSeek head-2048 should achieve 80-85% (similar to Qwen-7B 81.76%), and tail-2048 (94.96%) vs head-2048 gap shou
  metrics: {"accuracy": 0.787, "accuracy_ci_lower": 0.765, "accuracy_ci_upper": 0.81, "majority_baseline": 0.715, "lift_pp": 7.2, "pass_precision": 0.84, "pass_recall": 0.86, "pass_f1": 0.85, "fail_precision": 0.63, "fail_recall": 0.6, "fail_f1": 0.62}
  conclusion: success

=== codellama13b_full_trace_tail256_seed42 ===
  status: DONE
  hypothesis: CodeLlama-13B tail-256 应在 78-85%，与 7B 级模型 tail-256 (76-79%) 类似或略高，确认 256 tokens 信号不足是 universal 的
  metrics: {"accuracy": 0.779, "accuracy_ci_lower": 0.757, "accuracy_ci_upper": 0.803, "pass_f1": 0.843, "fail_f1": 0.626, "pass_precision": 0.856, "pass_recall": 0.831, "fail_precision": 0.604, "fail_recall": 0.649, "majority_baseline": 0.715, "lift": 0.064, "train_loss": 0.245, "eval_loss": 0.615}
  conclusion: success

=== codellama13b_full_trace_tail384_seed42 ===
  status: DONE
  hypothesis: CodeLlama-13B tail-384 (label_only_loss) 应在 85-95% 之间（256→512 phase transition 中间点），验证 label_only_loss 在短序列下也有效
  metrics: {"accuracy": 0.8269, "accuracy_ci_lower": 0.8067, "accuracy_ci_upper": 0.8471, "majority_baseline": 0.7151, "lift": 0.1118, "n": 1190, "pass_precision": 0.8314, "pass_recall": 0.9506, "pass_f1": 0.8871, "fail_precision": 0.8065, "fail_recall": 0.5162, "fail_f1": 0.6295}
  conclusion: negative

=== codellama13b_full_trace_tail2048_seed42 ===
  status: DONE
  hypothesis: CodeLlama-13B tail-2048 应在 95-98%，head-tail gap ≥15pp，确认 signal positional concentration 跨 4 模型
  metrics: {}
  conclusion: failed

=== codellama13b_full_trace_tail2048_seed42_v2 ===
  status: DONE
  hypothesis: CodeLlama-13B tail-2048 应在 95-98%，head-tail gap ≥15pp，确认 signal positional concentration 跨 4 模型
  metrics: {"accuracy_epoch1": 0.2849, "accuracy_epoch3": 0.2958, "pass_recall_epoch3": 0.016, "fail_recall_epoch3": 0.997, "majority_baseline": 0.715, "n_test": 1190, "note": "Catastrophic failure: model predicts fail for almost everything. Full-sequence loss dilution with CodeLlama tokenizer at 2048 tokens."}
  conclusion: negative

=== codellama13b_full_trace_tail2048_seed42_v3 ===
  status: DONE
  hypothesis: CodeLlama-13B tail-2048 用 label_only_loss 应恢复到 95-98%（与其他 3 模型 tail-2048 对齐），确认 v2 的 29.6% 源于 full-sequence loss 稀释
  metrics: {"accuracy_epoch1": 0.071, "accuracy_epoch3": 0.418, "pass_f1_epoch3": 0.416, "fail_f1_epoch3": 0.421, "pass_f1_epoch1": 0.035, "fail_f1_epoch1": 0.342, "train_loss": 0.785}
  conclusion: negative

=== codellama13b_full_trace_tail1024_seed42 ===
  status: DONE
  hypothesis: CodeLlama-13B tail-1024 应收敛到 96.5% 附近（与 DeepSeek 96.47%、Qwen-1.5B 96.6% 不可区分），确认 tail-1024 convergence band 跨 4 模型 universal
  metrics: {}
  conclusion: failed

=== codellama13b_full_trace_tail1024_seed42_v2 ===
  status: DONE
  hypothesis: CodeLlama-13B tail-1024 应收敛到 96.5% 附近（与 DeepSeek 96.47%、Qwen-1.5B 96.6% 不可区分），确认 tail-1024 convergence band 跨 4 模型 universal
  metrics: {"accuracy": 0.876, "accuracy_ci_lower": 0.856, "accuracy_ci_upper": 0.893, "majority_baseline": 0.715, "lift_pp": 16.1, "pass_precision": 0.85, "pass_recall": 1, "pass_f1": 0.92, "fail_precision": 1, "fail_recall": 0.56, "fail_f1": 0.72, "n_test": 1190, "train_loss": 0.0937, "eval_loss": 0.1859}
  conclusion: negative

=== codellama13b_full_trace_tail1024_seed42_v3 ===
  status: DONE
  hypothesis: CodeLlama-13B tail-1024 用 label_only_loss 应恢复到 ~96.5%（与 DeepSeek 96.47%、Qwen-1.5B 96.6% 对齐），确认 v2 的 87.6% 源于 full-sequence loss 稀释而非 tail-1024 条件本身
  metrics: {"accuracy_epoch1": 0.9824, "accuracy_epoch3": 0.9756, "pass_f1_epoch1": 0.988, "fail_f1_epoch1": 0.968, "pass_f1_epoch3": 0.983, "fail_f1_epoch3": 0.955, "best_accuracy": 0.9824, "best_epoch": 1, "overfitting": true}
  conclusion: success

=== codellama13b_full_trace_head2048_seed42 ===
  status: DONE
  hypothesis: CodeLlama-13B head-2048 truncation should yield 75-82% accuracy, confirming signal positional concentration pattern across 4 model families where tail
  metrics: {"accuracy": 0.7992, "majority_baseline": 0.7151, "lift": 0.084, "n_test": 1190, "pass_precision": 0.8566, "pass_recall": 0.8637, "pass_f1": 0.8602, "fail_precision": 0.6506, "fail_recall": 0.6372, "fail_f1": 0.6438, "train_loss": 0.0452, "eval_loss": 0.111, "accuracy_ci_lower": 0.7765, "accuracy_ci_upper": 0.8227}
  conclusion: success

=== qwen15b_full_trace_tail256_seed42 ===
  status: DONE
  hypothesis: Cross-scale tail-256: Qwen-1.5B tail-256 should show similar accuracy to 7B tail-256 (78.9%), confirming the 256-512 phase transition is signal-limite
  metrics: {"accuracy": 0.726, "accuracy_ci_lower": 0.7, "accuracy_ci_upper": 0.753, "majority_baseline": 0.715, "lift_over_majority": 0.011, "lift_ci_lower": -0.021, "lift_ci_upper": 0.044, "pass_precision": 0.82, "pass_recall": 0.79, "pass_f1": 0.8, "fail_precision": 0.52, "fail_recall": 0.57, "fail_f1": 0.54, "eval_loss": 0.5936, "train_loss": 0.2687}
  conclusion: negative

=== qwen15b_full_trace_tail384_seed42 ===
  status: DONE
  hypothesis: Qwen-1.5B tail-384 应在 80-90% 之间（小模型在 transition zone 可能更低），精确定位 phase transition 曲线形状
  metrics: {"accuracy": 0.7361, "majority_baseline": 0.7151, "lift": 0.021, "n": 1190, "pass_precision": 0.8069, "pass_recall": 0.8296, "pass_f1": 0.8181, "fail_precision": 0.5397, "fail_recall": 0.5015, "fail_f1": 0.5199, "accuracy_ci": [0.7101, 0.7622]}
  conclusion: negative

=== qwen15b_full_trace_tail1024_seed42 ===
  status: DONE
  hypothesis: 1.5B tail-1024 可能低于 tail-512 (95.6%)，如同 7B non-monotonicity；因中等长度 trace 包含 noisy intermediate states
  metrics: {"accuracy": 0.966, "accuracy_ci_low": 0.955, "accuracy_ci_high": 0.976, "pass_precision": 0.96, "pass_recall": 0.99, "pass_f1": 0.98, "fail_precision": 0.97, "fail_recall": 0.91, "fail_f1": 0.94, "eval_loss": 0.1983, "train_loss": 0.1187, "majority_baseline": 0.715, "lift_over_majority_pp": 25}
  conclusion: success

=== qwen15b_full_trace_tail2048_seed42 ===
  status: DONE
  hypothesis: Tail-truncation concentrates diagnostic signal (final execution states, exceptions) at training time. If this hypothesis holds, Qwen2.5-Coder-1.5B wit
  metrics: {"accuracy": 0.979, "accuracy_ci_lower": 0.9706, "accuracy_ci_upper": 0.9874, "pass_precision": 0.9758, "pass_recall": 0.9953, "pass_f1": 0.9855, "fail_precision": 0.9876, "fail_recall": 0.9381, "fail_f1": 0.9622, "n_test": 1190}
  conclusion: success

=== qwen15b_full_trace_head2048_seed42 ===
  status: DONE
  hypothesis: Cross-scale head-truncation: Qwen-1.5B head-2048 should achieve 75-82%, and tail-2048 (97.90%) vs head-2048 gap should be >=15pp, confirming signal po
  metrics: {"accuracy": 0.7529, "accuracy_ci_lower": 0.7286, "accuracy_ci_upper": 0.7782, "pass_precision": 0.799, "pass_recall": 0.874, "pass_f1": 0.835, "fail_precision": 0.587, "fail_recall": 0.448, "fail_f1": 0.508, "n_test": 1190}
  conclusion: success

=== debugbench_exception_only_seed42 ===
  status: DONE
  hypothesis: Out-of-distribution generalization: exception_only signal sufficiency transfers to DebugBench (different bug categories, different code styles) becaus
  metrics: {"accuracy": 1, "majority_baseline": 0.5141, "lift": 0.4859, "n": 426, "pass_precision": 1, "pass_recall": 1, "pass_f1": 1, "fail_precision": 1, "fail_recall": 1, "fail_f1": 1, "accuracy_ci_wilson": [0.9914, 1], "accuracy_ci_bootstrap": [1, 1], "train_loss": 0.2435, "eval_loss": 0.4157, "train_runtime_sec": 837}
  conclusion: success

=== debugbench_no_trace_seed42 ===
  status: DONE
  hypothesis: DebugBench no-trace baseline: without execution trace, model relies on code structure alone — on DebugBench (50/50 pass/fail) this yields higher lift 
  metrics: {"accuracy": 0.9671, "majority_baseline": 0.5141, "lift": 0.4531, "pass_precision": 1, "pass_recall": 0.936, "pass_f1": 0.967, "fail_precision": 0.937, "fail_recall": 1, "fail_f1": 0.967, "accuracy_ci": [0.948, 0.984], "train_loss": 0.249, "eval_loss": 0.532}
  conclusion: success

=== debugbench_vota_seed42 ===
  status: DONE
  hypothesis: DebugBench VOTA generalization: VOTA compressed trace maintains near-perfect accuracy on out-of-distribution bugs, confirming trace compression captur
  metrics: {"accuracy": 0.9977, "majority_baseline": 0.5141, "lift": 0.4836, "n": 426, "pass_precision": 1, "pass_recall": 1, "pass_f1": 1, "fail_precision": 1, "fail_recall": 1, "fail_f1": 1, "accuracy_ci": [0.993, 1], "train_loss": 0.098, "eval_loss": 0.1179, "eval_mean_token_accuracy": 0.9737, "errors": 1}
  conclusion: success

=== debugbench_exception_bug_fix ===
  status: DONE
  hypothesis: BUG FIX: compress_exception_only() only checked trace_raw events, missing 625/1006 empty-trace fails (syntax errors) + 5 event-capped samples. Fix: fa
  metrics: {}
  conclusion: success

=== fewshot_gpt4o_exception_only_0shot ===
  status: DONE
  hypothesis: Frontier LLM (GPT-4o) with zero-shot prompting can match SFT Qwen-7B on exception_only test verdict prediction because the task may be solvable via ge
  metrics: {"accuracy": 0.8798, "fail_f1": 0.8228}
  conclusion: negative

=== fewshot_gpt4o_exception_only_3shot ===
  status: DONE
  hypothesis: Adding 3-shot examples to GPT-4o improves exception_only verdict prediction over zero-shot by providing task format demonstrations and calibrating out
  metrics: {"accuracy": 0.8681, "fail_f1": 0.7995}
  conclusion: negative

=== fewshot_gpt4o_no_trace_0shot ===
  status: DONE
  hypothesis: GPT-4o zero-shot on no_trace condition can outperform SFT Qwen-7B because frontier LLMs have stronger code understanding that compensates for missing 
  metrics: {"accuracy": 0.8445, "fail_f1": 0.7543}
  conclusion: success

=== fewshot_gpt41_exception_only_0shot ===
  status: DONE
  hypothesis: GPT-4.1 zero-shot on exception_only condition performs comparably to GPT-4o because both are frontier models with similar code reasoning capabilities.
  metrics: {"accuracy": 0.8218, "fail_f1": 0.7452}
  conclusion: negative

=== fewshot_gpt41_exception_only_3shot ===
  status: DONE
  hypothesis: Adding 3-shot examples to GPT-4.1 improves exception_only verdict prediction over zero-shot by providing task format demonstrations.
  metrics: {"accuracy": 0.8193, "fail_f1": 0.7413}
  conclusion: negative

=== fewshot_gpt41_no_trace_0shot ===
  status: DONE
  hypothesis: GPT-4.1 zero-shot on no_trace condition can outperform SFT Qwen-7B because frontier LLMs have stronger code understanding that compensates for missing
  metrics: {"accuracy": 0.7731, "fail_f1": 0.6608}
  conclusion: success

=== fewshot_qwen7b_exception_only ===
  status: DONE
  hypothesis: Few-shot (3 examples) improves over zero-shot (89.08%) but remains far below SFT (99.83%) because 3 in-context examples cannot cover all caught except
  metrics: {"accuracy": 0.9084, "accuracy_ci_lower": 0.8908, "accuracy_ci_upper": 0.9244, "pass_precision": 0.9245, "pass_recall": 0.9495, "pass_f1": 0.9368, "fail_precision": 0.8639, "fail_recall": 0.8053, "fail_f1": 0.8336, "n_test": 1190, "n_unknown": 0}
  conclusion: success

=== attention_gradient_analysis ===
  status: DONE
  hypothesis: In the full_trace model, execution trace tokens dominate input length (~70%+ of tokens) but receive disproportionately low attention and gradient sign
  metrics: {}
  conclusion: success

=== zeroshot_codellama13b_exception_only ===
  status: DONE
  hypothesis: Zero-shot cross-scale baseline: untuned CodeLlama-13B-Instruct (largest model tested) still cannot match SFT accuracy on exception_only verdict predic
  metrics: {"accuracy": 0.5101, "accuracy_ci_lower": 0.4824, "accuracy_ci_upper": 0.5395, "pass_precision": 1, "pass_recall": 0.3502, "pass_f1": 0.5187, "fail_precision": 0.3585, "fail_recall": 0.9115, "fail_f1": 0.5146, "n_test": 1190, "n_unknown": 30}
  conclusion: success

=== zeroshot_deepseek7b_exception_only ===
  status: DONE
  hypothesis: Zero-shot cross-model baseline: untuned DeepSeek-Coder-6.7B-Instruct similarly cannot reach SFT-level accuracy on exception_only verdict prediction, c
  metrics: {"accuracy": 0.9059, "accuracy_ci_lower": 0.8899, "accuracy_ci_upper": 0.9218, "pass_precision": 0.9743, "pass_recall": 0.8919, "pass_f1": 0.9313, "fail_precision": 0.7762, "fail_recall": 0.941, "fail_f1": 0.8507, "n_test": 1190, "n_unknown": 0}
  conclusion: success

=== zeroshot_qwen15b_exception_only ===
  status: DONE
  hypothesis: Zero-shot cross-scale baseline: Qwen-1.5B zero-shot may perform poorly (similar to CodeLlama-13B) due to limited capacity, but SFT normalizes it to 99
  metrics: {"accuracy": 0.9345, "accuracy_ci_lower": 0.9202, "accuracy_ci_upper": 0.9479, "pass_f1": 0.969, "fail_f1": 0.873, "pass_recall": 0.9906, "fail_recall": 0.7935, "n_test": 1190, "n_unknown": 24}
  conclusion: success

=== zeroshot_qwen7b_exception_only ===
  status: DONE
  hypothesis: Zero-shot prompting baseline: untuned Qwen2.5-7B-Instruct cannot match SFT accuracy (99.83%) on exception_only verdict prediction because distinguishi
  metrics: {"accuracy": 0.8908, "accuracy_ci_lower": 0.8731, "accuracy_ci_upper": 0.9076, "pass_precision": 0.8815, "pass_recall": 0.9788, "pass_f1": 0.9276, "fail_precision": 0.9265, "fail_recall": 0.6696, "fail_f1": 0.7774, "n_test": 1190, "n_unknown": 0}
  conclusion: success

=== qwen1.5b_exception_only_seed42 ===
  status: DONE
  hypothesis: Qwen-1.5B exception_only 应达 ≥99% accuracy，确认 minimal sufficient signal 在 1.5B scale 有效，signal quality 主导 model capacity
  metrics: {}
  conclusion: killed

=== qwen1.5b_full_trace_seed42 ===
  status: DONE
  hypothesis: Qwen-1.5B full_trace 应达 ≥96% accuracy，确认 1.5B 小模型在 full trace 条件下与 7B 可比（trace quality 主导而非 model capacity）
  metrics: {}
  conclusion: killed

=== qwen1.5b_no_trace_seed42 ===
  status: DONE
  hypothesis: Qwen-1.5B no_trace 应在 65-75% (≈majority baseline)，确认无 trace 小模型表现更差、scale 无法补偿
  metrics: {"accuracy": 0.7261, "accuracy_ci_lower": 0.7008, "accuracy_ci_upper": 0.7529, "majority_baseline": 0.7151, "lift_pp": 1.09, "pass_precision": 0.831, "pass_recall": 0.774, "pass_f1": 0.802, "fail_precision": 0.516, "fail_recall": 0.605, "fail_f1": 0.557}
  conclusion: success

=== qwen1.5b_vota_seed42 ===
  status: DONE
  hypothesis: Qwen-1.5B VOTA 应在 82-90% accuracy，可能略低于 7B 因 VOTA 条件下 scale-sensitivity 更明显
  metrics: {}
  conclusion: killed

=== codellama_exception_only_seed42 ===
  status: DONE
  hypothesis: CodeLlama-13B exception_only 应达 ≥99.33% accuracy，与其他 3 模型一致，确认 minimal sufficient signal 跨 4 模型 3 架构 1.5B-13B universal
  metrics: {}
  conclusion: killed

=== codellama_no_trace_seed42 ===
  status: DONE
  hypothesis: CodeLlama-13B no_trace 应在 70-78% (≈majority baseline)，确认无 trace 时 13B scale 无法补偿信息缺失
  metrics: {}
  conclusion: killed

=== codellama_vota_seed42 ===
  status: DONE
  hypothesis: CodeLlama-13B VOTA 应在 85-92% accuracy，与 Qwen-7B/DeepSeek VOTA 对齐，作 rebuttal 储备验证 ablation condition 跨 scale 一致性
  metrics: {}
  conclusion: killed

=== eval_missing_predictions_batch ===
  status: DONE
  hypothesis: Utility: batch re-evaluation of checkpoints missing predictions.jsonl to complete provenance records and enable systematic cross-experiment comparison
  metrics: {}
  conclusion: success

=== eval_missing_predictions_batch_v2 ===
  status: DONE
  hypothesis: Utility: second batch re-evaluation pass for remaining checkpoints without predictions.jsonl, ensuring all DONE experiments have comparable evaluation
  metrics: {}
  conclusion: success
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6116341e-1965-4fac-aa1b-800f99e99650",
  "isSidechain": true,
  "promptId": "83fb8b21-6186-4214-9116-e4c59eb31db2",
  "agentId": "ad4eda51cd882ef4e",
  "type": "user",
  "uuid": "1ac71a31-29a9-4a83-a08b-959e3d9f5762",
  "sourceToolAssistantUUID": "6116341e-1965-4fac-aa1b-800f99e99650",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "d5f32b76-3066-49a9-b711-4657d91efad8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-23T19:19:47.658Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01XGxmUT6uV5YoqyoYQU8HNi`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Check remaining experiments I haven't fully covered\nremaining = [\n    'deepseek_full_trace_tail256_seed42', 'deepseek_full_trace_tail384_seed42',\n    'codellama13b_full_trace_tail256_seed42', 'codellama13b_full_trace_tail384_seed42',\n    'codellama13b_full_trace_tail512_seed42',\n    'vota_exception_only_seed42_v2',  # already got\n    # check for seed42 canonical Qwen-7B experiments I may have missed\n    'full_trace_seed42', 'no_trace_seed42_v4', 'no_trace_seed42_v5',\n    # exception_only seed42 canonical\n]\n\n# also let's check all Qwen-7B VOTA seed42 canonical\ncanonical_qwen7b = {\n    'exception_only': 'exception_only_seed123',  # seed42 has same accuracy, use seed123 \n    'full_trace': 'full_trace_seed123',  # canonical 3-seed\n    'no_trace': 'no_trace_seed42_v5',  # canonical\n    'vota': 'vota_seed42_v4',  # canonical\n    'ae_only': 'ae_only_seed456',  # has comparison\n    'loop_only': 'loop_only_seed456',  # has comparison\n    'label_only': 'full_trace_label_only_seed42',\n}\n\n# Also look at the exception_only seed42 canonical\neid = 'exception_only_seed123'\nexp = experiments.get(eid, {})\nprint(f\"=== exception_only_seed123 (canonical Qwen-7B) ===\")\nprint(json.dumps(exp.get('metrics', {}), indent=2))\n\n# And check if there's a canonical seed42 for exception_only Qwen-7B\nprint(\"\\n\\nSearching for Qwen-7B exception_only seed42 canonical...\")\nfor eid in ['exception_only_seed42', 'vota_exception_only_seed42_v2']:\n    if eid in experiments:\n        exp = experiments[eid]\n        print(f\"\\n=== {eid} ===\")\n        print(json.dumps(exp.get('metrics', {}), indent=2))\n        print(f\"  conclusion: {exp.get('conclusion')}\")\nPYEOF\n",
  "description": "Check Qwen-7B canonical experiment metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ac71a31-29a9-4a83-a08b-959e3d9f5762",
  "isSidechain": true,
  "agentId": "ad4eda51cd882ef4e",
  "requestId": "req_011CbL3LioHE99AtmNeRWoWS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a6a97ba-d6d2-4913-82b0-47d4f179b7b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "d5f32b76-3066-49a9-b711-4657d91efad8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01C7FKYWi72rt3Lw56qTvhyJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10828,
      "cache_read_input_tokens": 47625,
      "output_tokens": 831,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10828
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 831,
          "cache_read_input_tokens": 47625,
          "cache_creation_input_tokens": 10828,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10828,
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

_source line 26 · 2026-05-23T19:19:47.741Z_

<details><summary>↩ Tool result · `toolu_01XGxmUT6uV5YoqyoYQU8HNi`</summary>

```text
=== exception_only_seed123 (canonical Qwen-7B) ===
{
  "accuracy": 0.9983,
  "accuracy_ci": [
    0.9958,
    1
  ],
  "majority_baseline": 0.7151,
  "lift": 0.2832,
  "n": 1190,
  "pass_precision": 1,
  "pass_recall": 0.9976,
  "pass_f1": 0.9988,
  "fail_precision": 0.9941,
  "fail_recall": 1,
  "fail_f1": 0.9971,
  "train_loss": 0.1096,
  "train_runtime_sec": 7507,
  "epochs": 3,
  "seed_comparison": {
    "seed42_accuracy": 0.9983,
    "seed456_accuracy": 0.9983,
    "seed123_accuracy": 0.9983,
    "max_diff": 0,
    "note": "identical accuracy to 4 decimal places across all 3 seeds (42/456/123); each has exactly 2/1190 errors; exception_only fully seed-robust"
  }
}


Searching for Qwen-7B exception_only seed42 canonical...

=== vota_exception_only_seed42_v2 ===
{
  "accuracy": 0.9983,
  "majority_baseline": 0.7151,
  "lift": 0.2832,
  "n": 1190,
  "pass_precision": 1,
  "pass_recall": 0.998,
  "pass_f1": 0.999,
  "fail_precision": 0.994,
  "fail_recall": 1,
  "fail_f1": 0.997,
  "lift_vs_notrace": 0.2471,
  "lift_vs_notrace_ci_lower": 0.2227,
  "lift_vs_notrace_ci_upper": 0.2714,
  "lift_vs_fulltrace": 0.1807,
  "lift_vs_fulltrace_ci_lower": 0.1588,
  "lift_vs_fulltrace_ci_upper": 0.2034,
  "lift_vs_vota": 0.0067,
  "lift_vs_vota_ci_lower": 0.0017,
  "lift_vs_vota_ci_upper": 0.0126,
  "lift_vs_vota_pvalue": 0.01
}
  conclusion: success
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a6a97ba-d6d2-4913-82b0-47d4f179b7b1",
  "isSidechain": true,
  "promptId": "83fb8b21-6186-4214-9116-e4c59eb31db2",
  "agentId": "ad4eda51cd882ef4e",
  "type": "user",
  "uuid": "05bb487d-7ad6-448b-8b5b-114f3335e305",
  "sourceToolAssistantUUID": "4a6a97ba-d6d2-4913-82b0-47d4f179b7b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "d5f32b76-3066-49a9-b711-4657d91efad8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-23T19:19:49.020Z_

Now I have all the data needed. Let me compile the comprehensive audit file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05bb487d-7ad6-448b-8b5b-114f3335e305",
  "isSidechain": true,
  "agentId": "ad4eda51cd882ef4e",
  "requestId": "req_011CbL3MntsBnFfKcBroSyMQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8af5850e-034c-4da7-9043-64f3968ed194",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "d5f32b76-3066-49a9-b711-4657d91efad8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RmrSyVnwGEJUHAURegp8sK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1495,
      "cache_read_input_tokens": 58453,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1495,
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

_source line 28 · 2026-05-23T19:23:18.220Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01C9E9JJnSAWMfQ51mMNp4jB`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-4-projects-trace-verdict-study/d5f32b76-3066-49a9-b711-4657d91efad8/tool-results/mcp-agent-ml-research-read_registry-1779563834793.txt\"\n\nwith open(filepath, 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\noutput_path = \"/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_audit_registry_extract.txt\"\n\nlines = []\nlines.append(\"=\" * 100)\nlines.append(\"REGISTRY AUDIT EXTRACT — trace-verdict-study\")\nlines.append(\"Generated from: mcp-agent-ml-research-read_registry-1779563834793.txt\")\nlines.append(f\"Total experiments in registry: {len(experiments)}\")\nlines.append(\"=\" * 100)\nlines.append(\"\")\n\n# ============================================================================================\n# SECTION 1: TABLE 1 — MAIN CONDITION RESULTS (Qwen-7B canonical, all seeds)\n# ============================================================================================\nlines.append(\"=\" * 100)\nlines.append(\"SECTION 1: TABLE 1 CANDIDATES — Main SFT Conditions (Qwen2.5-Coder-7B-Instruct, n=1190)\")\nlines.append(\"=\" * 100)\nlines.append(\"\")\n\n# --- exception_only (Qwen-7B) ---\nlines.append(\"--- exception_only (Qwen-7B) ---\")\nlines.append(\"  Seed 42 accuracy: 0.9983 (from seed_comparison in exception_only_seed123)\")\nlines.append(\"  Seed 123 accuracy: 0.9983  | exp_id: exception_only_seed123\")\nlines.append(\"    accuracy_ci: [0.9958, 1.0]\")\nlines.append(\"    pass_precision: 1.0000  pass_recall: 0.9976  pass_f1: 0.9988\")\nlines.append(\"    fail_precision: 0.9941  fail_recall: 1.0000  fail_f1: 0.9971\")\nlines.append(\"    majority_baseline: 0.7151  lift: 0.2832  n: 1190\")\nlines.append(\"  Seed 456 accuracy: 0.9983  | exp_id: exception_only_seed456\")\nlines.append(\"    accuracy_ci: [0.9958, 1.0]  eval_loss: 0.4629  train_loss: 0.1087\")\nlines.append(\"  MEAN across 3 seeds: 0.9983 ± 0.0000 (all identical, max_diff=0)\")\nlines.append(\"  NOTE: each seed has exactly 2/1190 errors\")\nlines.append(\"\")\n\n# --- full_trace (Qwen-7B) ---\nlines.append(\"--- full_trace (Qwen-7B) ---\")\nlines.append(\"  Seed 123 accuracy: 0.7958  | exp_id: full_trace_seed123\")\nlines.append(\"    accuracy_ci_lower: 0.7714  accuracy_ci_upper: 0.8202\")\nlines.append(\"    pass_precision: 0.8753  pass_recall: 0.8331  pass_f1: 0.8537\")\nlines.append(\"    fail_precision: 0.6263  fail_recall: 0.7021  fail_f1: 0.6620\")\nlines.append(\"    majority_baseline: 0.7151  lift: 0.0807  n: 1190\")\nlines.append(\"  Seed 42 (v5) accuracy: 0.8176  | exp_id: full_trace_seed42_v5\")\nlines.append(\"    accuracy_ci_lower: 0.797  accuracy_ci_upper: 0.839\")\nlines.append(\"    pass_precision: 0.8774  pass_recall: 0.8660  pass_f1: 0.8717\")\nlines.append(\"    fail_precision: 0.6743  fail_recall: 0.6962  fail_f1: 0.6851\")\nlines.append(\"    lift: 0.1025  lift_vs_notrace: 0.0664  (CI: [0.0437, 0.0899])\")\nlines.append(\"    epoch_level: epoch1=0.8303 epoch2=0.7630 epoch3=0.8176 (non-monotonic)\")\nlines.append(\"  Seed 456 accuracy: 0.8050  | exp_id: full_trace_seed456\")\nlines.append(\"    accuracy_ci_lower: 0.7824  accuracy_ci_upper: 0.8269\")\nlines.append(\"    pass_f1: 0.8637  fail_f1: 0.6578\")\nlines.append(\"    lift: 0.0899\")\nlines.append(\"  Seed 123 (qwen7b_full_trace_seed123) accuracy: 0.8020  | exp_id: qwen7b_full_trace_seed123\")\nlines.append(\"    ci_lower: 0.778  ci_upper: 0.825  lift_pp: 8.7\")\nlines.append(\"  Seed 456 (v2) accuracy: 0.8235  | exp_id: qwen7b_full_trace_seed456_v2\")\nlines.append(\"    ci_lower: 0.8017  ci_upper: 0.8454  lift_pp: 10.84\")\nlines.append(\"  3-SEED MEAN (seed42=0.8176, seed123=0.8020, seed456=0.8235): ~0.814\")\nlines.append(\"\")\n\n# --- no_trace (Qwen-7B) ---\nlines.append(\"--- no_trace (Qwen-7B) ---\")\nlines.append(\"  Seed 42 (v4/v5) accuracy: 0.7513  | exp_id: no_trace_seed42_v5\")\nlines.append(\"    accuracy_ci_lower: 0.7277  accuracy_ci_upper: 0.7748\")\nlines.append(\"    pass_precision: 0.8776  pass_recall: 0.7579  pass_f1: 0.8134\")\nlines.append(\"    fail_precision: 0.5473  fail_recall: 0.7345  fail_f1: 0.6272\")\nlines.append(\"    majority_baseline: 0.7151  lift: 0.0361  (CI: [0.0042, 0.0706])\")\nlines.append(\"    epoch_level: epoch1=0.7429 epoch2=0.7630 epoch3=0.7513\")\nlines.append(\"  Seed 123 accuracy: 0.7908  | exp_id: no_trace_seed123\")\nlines.append(\"    pass_f1: 0.8523  fail_f1: 0.6581  n: 1190\")\nlines.append(\"  Seed 456 accuracy: 0.7504  | exp_id: no_trace_seed456\")\nlines.append(\"    accuracy_ci: [0.7235, 0.7748]  pass_f1: 0.8119  fail_f1: 0.6292\")\nlines.append(\"  3-SEED MEAN (seed42=0.7513, seed123=0.7908, seed456=0.7504): ~0.764\")\nlines.append(\"\")\n\n# --- VOTA (Qwen-7B) ---\nlines.append(\"--- VOTA (Qwen-7B) ---\")\nlines.append(\"  Seed 42 (v4) accuracy: 0.9563  | exp_id: vota_seed42_v4  [canonical v4]\")\nlines.append(\"    lift: 0.2412  lift_vs_notrace: 0.2050  (CI: [0.177, 0.234])\")\nlines.append(\"    pass_precision: 0.9440  pass_recall: 0.9980  pass_f1: 0.9700\")\nlines.append(\"    fail_precision: 0.9930  fail_recall: 0.8530  fail_f1: 0.9170\")\nlines.append(\"  Seed 42 (v5) accuracy: 0.9941  | exp_id: vota_seed42_v5  [note: diff script]\")\nlines.append(\"    pass_precision: 1.0000  pass_recall: 0.9918  pass_f1: 0.9959\")\nlines.append(\"    fail_precision: 0.9798  fail_recall: 1.0000  fail_f1: 0.9898  n: 1190\")\nlines.append(\"  Seed 123 accuracy: 0.9866  | exp_id: qwen7b_vota_seed123\")\nlines.append(\"    accuracy_ci_lower: 0.9790  accuracy_ci_upper: 0.9925  lift: 0.2714\")\nlines.append(\"    pass_f1: 0.9905  fail_f1: 0.9769\")\nlines.append(\"  Seed 456 accuracy: 0.9908  | exp_id: qwen7b_vota_seed456\")\nlines.append(\"    accuracy_ci_lower: 0.9849  accuracy_ci_upper: 0.9958  lift: 0.2756\")\nlines.append(\"    pass_f1: 0.9935  fail_f1: 0.9840\")\nlines.append(\"  Seed 456 v2 accuracy: 0.9908  | exp_id: vota_seed456_v2\")\nlines.append(\"    ci_95: [0.985, 0.996]  pass_f1: 0.9930  fail_f1: 0.9840\")\nlines.append(\"  3-SEED MEAN (seed42=0.9941, seed123=0.9866, seed456=0.9908): ~0.991\")\nlines.append(\"    [using v5 for seed42; note v4 gives 0.9563 — version discrepancy]\")\nlines.append(\"\")\n\n# --- ae_only (Qwen-7B) ---\nlines.append(\"--- ae_only (Qwen-7B) ---\")\nlines.append(\"  Seed 42 accuracy: 0.9992  | exp_id: vota_ae_only_seed42\")\nlines.append(\"    accuracy_ci: [0.9975, 1.0000]\")\nlines.append(\"    bootstrap vs no_trace: diff=0.2479 CI=[0.2235, 0.2731] p=0\")\nlines.append(\"    bootstrap vs exception_only: diff=0.0008 CI=[-0.0017, 0.0034] p=0.8002 (n.s.)\")\nlines.append(\"    bootstrap vs vota: diff=0.0050 CI=[0.0017, 0.0092] p=0.0046\")\nlines.append(\"  Seed 123 accuracy: 0.9908  | exp_id: ae_only_seed123\")\nlines.append(\"    pass_recall: 0.987  fail_recall: 1.0  n: 1190  lift: 0.2757\")\nlines.append(\"  Seed 456 accuracy: 0.9992  | exp_id: ae_only_seed456\")\nlines.append(\"    lift: 0.2841  n: 1190\")\nlines.append(\"    seed_comparison: seed42=0.9992 seed123=0.9908 seed456=0.9992 → mean=0.9964 ± 0.0049\")\nlines.append(\"  3-SEED MEAN: 0.9964 ± 0.0049\")\nlines.append(\"\")\n\n# --- loop_only (Qwen-7B) ---\nlines.append(\"--- loop_only (Qwen-7B) ---\")\nlines.append(\"  Seed 42 accuracy: 0.8563  | exp_id: vota_loop_only_seed42\")\nlines.append(\"    accuracy_ci: [0.8353, 0.8756]  lift: 0.1412\")\nlines.append(\"    pass_precision: 0.9239  pass_recall: 0.8707  pass_f1: 0.8966\")\nlines.append(\"    fail_precision: 0.7165  fail_recall: 0.8201  fail_f1: 0.7648\")\nlines.append(\"    bootstrap vs vota: diff=-0.1378 CI=[-0.1571, -0.1185] (sig)\")\nlines.append(\"  Seed 123 accuracy: 0.8588  | exp_id: loop_only_seed123\")\nlines.append(\"    accuracy_ci: [0.8403, 0.8773]  lift: 0.1437\")\nlines.append(\"    pass_f1: 0.8999  fail_f1: 0.7607\")\nlines.append(\"  Seed 456 accuracy: 0.8664  | exp_id: loop_only_seed456\")\nlines.append(\"    accuracy_ci: [0.8470, 0.8840]\")\nlines.append(\"    pass_f1: 0.9053  fail_f1: 0.7732\")\nlines.append(\"    seed_comparison: seed42=0.8563 seed123=0.8588 seed456=0.8664 → mean=0.8605 ± 0.0053\")\nlines.append(\"  3-SEED MEAN: 0.8605 ± 0.0053\")\nlines.append(\"\")\n\n# --- label_only / full_trace_label_only (Qwen-7B) ---\nlines.append(\"--- label_only / full_trace_label_only_loss (Qwen-7B) ---\")\nlines.append(\"  Seed 42 (full_trace, label_only_loss) accuracy: 0.8622  | exp_id: full_trace_label_only_seed42\")\nlines.append(\"    accuracy_ci_lower: 0.8437  accuracy_ci_upper: 0.8807  lift: 0.1471\")\nlines.append(\"    pass_f1: 0.9063  fail_f1: 0.7397  n: 1190\")\nlines.append(\"    lift_vs_notrace: 0.1109  CI: [0.0849, 0.1370]\")\nlines.append(\"    lift_vs_standard_fulltrace: 0.0445  CI: [0.0235, 0.0655]  p=0\")\nlines.append(\"  Seed 123 accuracy: 0.8689  | exp_id: qwen7b_full_trace_label_only_seed123\")\nlines.append(\"    accuracy_ci: [0.8496, 0.8874]  pass_f1: 0.9121  fail_f1: 0.7426  lift: 0.1538\")\nlines.append(\"  Seed 456 accuracy: 0.8470  | exp_id: qwen7b_full_trace_label_only_seed456\")\nlines.append(\"    accuracy_ci: [0.827, 0.866]  pass_f1: 0.9000  fail_f1: 0.7100  lift: 0.1319\")\nlines.append(\"  NOTE: standalone label_only seeds (no trace at all):\")\nlines.append(\"    label_only_seed123 accuracy: 0.8706  pass_f1: 0.915  fail_f1: 0.729\")\nlines.append(\"    label_only_seed456 accuracy: 0.8590  pass_f1: 0.905  fail_f1: 0.727\")\nlines.append(\"\")\n\nlines.append(\"\")\nlines.append(\"=\" * 100)\nlines.append(\"SECTION 2: CROSS-MODEL TABLE — All 4 Models × Main Conditions\")\nlines.append(\"=\" * 100)\nlines.append(\"\")\n\n# --- DeepSeek-Coder-6.7B ---\nlines.append(\"--- DeepSeek-Coder-6.7B ---\")\nlines.append(\"\")\nlines.append(\"  exception_only:\")\nlines.append(\"    Seed 42  accuracy: 0.9933  | exp_id: deepseek_exception_only_seed42\")\nlines.append(\"      pass_f1: 0.9953  fail_f1: 0.9883  n: 1190  lift: 0.2782\")\nlines.append(\"    Seed 123 accuracy: 0.9950  | exp_id: deepseek_exception_only_seed123_v2\")\nlines.append(\"    Seed 456 accuracy: 0.9933  | exp_id: deepseek_exception_only_seed456\")\nlines.append(\"      accuracy_ci: [0.9882, 0.9975]\")\nlines.append(\"      seed_comparison: seed42=0.9933 seed456=0.9933 seed123=0.9109 (outlier)\")\nlines.append(\"      NOTE: seed123 v1 was OOM-crash; seed123_v2 = 0.9950 (canonical)\")\nlines.append(\"    3-SEED MEAN (using v2 for seed123): ~0.994\")\nlines.append(\"\")\nlines.append(\"  full_trace:\")\nlines.append(\"    Seed 42 (v3) accuracy: 0.7916  | exp_id: deepseek_full_trace_seed42_v3\")\nlines.append(\"      accuracy_ci: [0.768, 0.813]  lift: 0.0765\")\nlines.append(\"      pass_f1: 0.854  fail_f1: 0.637  n: 1190\")\nlines.append(\"    (v1, v2 = killed/negative)\")\nlines.append(\"\")\nlines.append(\"  no_trace:\")\nlines.append(\"    Seed 42 accuracy: 0.7336  | exp_id: deepseek_no_trace_seed42\")\nlines.append(\"      accuracy_ci: [0.708, 0.757]  lift: 0.0185\")\nlines.append(\"      pass_f1: 0.8130  fail_f1: 0.5390  n: 1190\")\nlines.append(\"\")\nlines.append(\"  VOTA:\")\nlines.append(\"    Seed 42 accuracy: 0.8445  | exp_id: deepseek_vota_seed42  [early canonical]\")\nlines.append(\"      accuracy_ci: [0.826, 0.864]  lift: 0.1294\")\nlines.append(\"      pass_f1: 0.9020  fail_f1: 0.6250\")\nlines.append(\"    Seed 123 accuracy: 0.9916  | exp_id: deepseek_vota_seed123\")\nlines.append(\"      accuracy_ci_lower: 0.9857  accuracy_ci_upper: 0.9966\")\nlines.append(\"    Seed 456 accuracy: 0.9933  | exp_id: deepseek_vota_seed456\")\nlines.append(\"    NOTE: large seed variance — seed42 may be from different pipeline version\")\nlines.append(\"\")\nlines.append(\"  ae_only:\")\nlines.append(\"    Seed 42 accuracy: 0.9874  | exp_id: deepseek_ae_only_seed42\")\nlines.append(\"      accuracy_ci: [0.9807, 0.9933]  pass_f1: 0.9910  fail_f1: 0.9770\")\nlines.append(\"    Seed 123 accuracy: 0.9832  | exp_id: deepseek_ae_only_seed123\")\nlines.append(\"\")\nlines.append(\"  loop_only:\")\nlines.append(\"    Seed 42 accuracy: 0.8126  | exp_id: deepseek_loop_only_seed42\")\nlines.append(\"      accuracy_ci: [0.7908, 0.8345]\")\nlines.append(\"    Seed 123 accuracy: 0.8126  | exp_id: deepseek_loop_only_seed123\")\nlines.append(\"      accuracy_ci: [0.792, 0.834]\")\nlines.append(\"    Seed 456 accuracy: 0.784   | exp_id: deepseek_loop_only_seed456\")\nlines.append(\"      fail_f1: 0.63  majority_baseline: 0.715\")\nlines.append(\"\")\nlines.append(\"  label_only (full_trace_label_only_loss):\")\nlines.append(\"    Seed 42 accuracy: 0.285   | exp_id: deepseek_label_only_seed42  [COLLAPSED]\")\nlines.append(\"      accuracy_ci: [0.261, 0.308]  lift: -0.430\")\nlines.append(\"      pass_f1: 0.0  fail_f1: 0.44\")\nlines.append(\"\")\n\n# --- CodeLlama-13B ---\nlines.append(\"--- CodeLlama-13B ---\")\nlines.append(\"\")\nlines.append(\"  exception_only:\")\nlines.append(\"    Seed 42  accuracy: 0.9983  | exp_id: codellama13b_exception_only_seed42\")\nlines.append(\"      accuracy_ci: [0.9958, 1.000]  pass_f1: 0.9988  fail_f1: 0.9971\")\nlines.append(\"    Seed 123 accuracy: 1.0000  | exp_id: codellama13b_exception_only_seed123\")\nlines.append(\"      pass_f1: 1.0  fail_f1: 1.0  n: 1190\")\nlines.append(\"    Seed 456 accuracy: 0.9983  | exp_id: codellama13b_exception_only_seed456\")\nlines.append(\"      pass_f1: 0.9988  fail_f1: 0.9971  n: 1190\")\nlines.append(\"    3-SEED MEAN: 0.9989\")\nlines.append(\"\")\nlines.append(\"  full_trace (canonical tail512, label_only_loss):\")\nlines.append(\"    Seed 42  accuracy: 0.9824  | exp_id: codellama13b_full_trace_tail512_seed42\")\nlines.append(\"      accuracy_ci: [0.9748, 0.9899]  lift: 0.2672  pass_f1: 0.9878  fail_f1: 0.9680\")\nlines.append(\"    Seed 123 accuracy: 0.9824  | exp_id: codellama13b_full_trace_tail512_seed123\")\nlines.append(\"      accuracy_ci: [0.9748, 0.9899]\")\nlines.append(\"    Seed 456 accuracy: 0.9824  | exp_id: codellama13b_full_trace_tail512_seed456\")\nlines.append(\"      NOTE: all 3 seeds identical at 0.9824\")\nlines.append(\"    NOTE: full-seq loss at tail2048 collapsed (0.296); label_only_loss v3 at tail1024 = 0.9824 epoch1\")\nlines.append(\"\")\nlines.append(\"  no_trace:\")\nlines.append(\"    Seed 42 accuracy: 0.7650  | exp_id: codellama13b_no_trace_seed42\")\nlines.append(\"      accuracy_ci: [0.738, 0.787]  lift: 0.050\")\nlines.append(\"      pass_f1: 0.840  fail_f1: 0.590  n: 1190\")\nlines.append(\"\")\nlines.append(\"  VOTA:\")\nlines.append(\"    Seed 42  accuracy: 0.9857  | exp_id: codellama13b_vota_seed42\")\nlines.append(\"      accuracy_ci: [0.9790, 0.9916]  pass_f1: 0.9900  fail_f1: 0.9748\")\nlines.append(\"    Seed 123 accuracy: 0.9891  | exp_id: codellama13b_vota_seed123\")\nlines.append(\"      accuracy_ci: [0.9832, 0.9941]  pass_f1: 0.9924  fail_f1: 0.9809  n: 1190  lift: 0.2739\")\nlines.append(\"\")\nlines.append(\"  ae_only:\")\nlines.append(\"    Seed 42  accuracy: 0.9908  | exp_id: codellama13b_ae_only_seed42\")\nlines.append(\"      accuracy_ci: [0.9849, 0.9958]  pass_f1: 0.9935  fail_f1: 0.9840\")\nlines.append(\"    Seed 123 accuracy: 0.9908  | exp_id: codellama13b_ae_only_seed123\")\nlines.append(\"      accuracy_ci: [0.9849, 0.9958]  pass_f1: 0.9930  fail_f1: 0.9840\")\nlines.append(\"\")\nlines.append(\"  loop_only:\")\nlines.append(\"    Seed 42  accuracy: 0.7706  | exp_id: codellama13b_loop_only_seed42\")\nlines.append(\"      accuracy_ci: [0.7487, 0.7941]  lift: 0.0555  pass_f1: 0.820  fail_f1: 0.670\")\nlines.append(\"    Seed 123 accuracy: 0.7605  | exp_id: codellama13b_loop_only_seed123\")\nlines.append(\"      accuracy_ci: [0.7387, 0.7857]  pass_f1: 0.8078  fail_f1: 0.6823  lift: 0.0454\")\nlines.append(\"    Seed 456 accuracy: 0.7908  | exp_id: codellama13b_loop_only_seed456\")\nlines.append(\"      pass_f1: 0.843  fail_f1: 0.688  n: 1190  lift: 0.0757\")\nlines.append(\"\")\nlines.append(\"  label_only (full_trace_label_only_loss):\")\nlines.append(\"    Seed 42 (v2) accuracy: 0.2849  | exp_id: codellama13b_label_only_seed42_v2  [COLLAPSED]\")\nlines.append(\"      accuracy_ci: [0.2613, 0.3084]  pass_f1: 0.0  fail_f1: 0.4434\")\nlines.append(\"    Seed 123 (v2) accuracy: 'collapsed' | exp_id: codellama13b_label_only_seed123_v2\")\nlines.append(\"\")\n\n# --- Qwen-1.5B ---\nlines.append(\"--- Qwen2.5-Coder-1.5B ---\")\nlines.append(\"\")\nlines.append(\"  exception_only:\")\nlines.append(\"    Seed 42  accuracy: 0.9983  | exp_id: qwen15b_exception_only_seed42\")\nlines.append(\"      accuracy_ci: [0.9958, 1.000]  lift: 0.283  pass_f1: 0.9988  fail_f1: 0.9971\")\nlines.append(\"    Seed 123 accuracy: 0.9983  | exp_id: qwen15b_exception_only_seed123_v2\")\nlines.append(\"      accuracy_ci: [0.9958, 1.000]\")\nlines.append(\"    Seed 456 accuracy: 0.9983  | exp_id: qwen15b_exception_only_seed456\")\nlines.append(\"      seed_comparison: all 3 seeds identical — fully seed-robust\")\nlines.append(\"    3-SEED MEAN: 0.9983 ± 0.0000\")\nlines.append(\"\")\nlines.append(\"  full_trace:\")\nlines.append(\"    Seed 42 (full_trace, no trunc) accuracy: 0.7706  | exp_id: qwen15b_full_trace_seed42\")\nlines.append(\"    Seed 42 (tail512) accuracy: 0.956   | exp_id: qwen15b_full_trace_tail512_seed42\")\nlines.append(\"      accuracy_ci: [0.945, 0.968]  pass_f1: 0.970  fail_f1: 0.920\")\nlines.append(\"    Seed 123 (tail512) accuracy: 0.9765  | exp_id: qwen15b_full_trace_tail512_seed123\")\nlines.append(\"      accuracy_ci: [0.9681, 0.9849]  lift: 0.2613\")\nlines.append(\"    Seed 456 (tail512) accuracy: 0.9672  | exp_id: qwen15b_full_trace_tail512_seed456\")\nlines.append(\"      accuracy_ci: [0.9563, 0.9773]  lift: 0.2521\")\nlines.append(\"\")\nlines.append(\"  no_trace:\")\nlines.append(\"    Seed 42  accuracy: 0.6731  | exp_id: qwen15b_no_trace_seed42\")\nlines.append(\"      pass_f1: 0.7527  fail_f1: 0.518  n: 1190\")\nlines.append(\"    Seed 123 accuracy: 0.7588  | exp_id: qwen15b_no_trace_seed123\")\nlines.append(\"      accuracy_ci: [0.7328, 0.7824]  lift: 0.0437\")\nlines.append(\"      pass_f1: 0.8323  fail_f1: 0.571\")\nlines.append(\"    Seed 456 accuracy: 0.7387  | exp_id: qwen15b_no_trace_seed456\")\nlines.append(\"      pass_f1: 0.8195  fail_f1: 0.5266\")\nlines.append(\"\")\nlines.append(\"  VOTA:\")\nlines.append(\"    Seed 42  accuracy: 0.9958  | exp_id: qwen15b_vota_seed42\")\nlines.append(\"      pass_f1: 0.9971  fail_f1: 0.9926  n: 1190\")\nlines.append(\"    Seed 123 accuracy: 0.9950  | exp_id: qwen15b_vota_seed123\")\nlines.append(\"      ci_95: [0.9908, 0.9983]  pass_f1: 0.9965  fail_f1: 0.9912\")\nlines.append(\"\")\nlines.append(\"  ae_only:\")\nlines.append(\"    Seed 42  accuracy: 0.9908  | exp_id: qwen15b_ae_only_seed42\")\nlines.append(\"      accuracy_ci: [0.9849, 0.9958]  lift: 0.2756  pass_f1: 0.9935  fail_f1: 0.9840\")\nlines.append(\"    Seed 123 accuracy: 0.9857  | exp_id: qwen15b_ae_only_seed123\")\nlines.append(\"      majority_baseline: 0.715  fail_f1: 0.975\")\nlines.append(\"\")\nlines.append(\"  loop_only:\")\nlines.append(\"    Seed 42  accuracy: 0.7832  | exp_id: qwen15b_loop_only_seed42\")\nlines.append(\"      pass_f1: 0.8526  fail_f1: 0.5905\")\nlines.append(\"    Seed 123 accuracy: 0.8109  | exp_id: qwen15b_loop_only_seed123\")\nlines.append(\"      pass_f1: 0.8737  fail_f1: 0.6244\")\nlines.append(\"    Seed 456 accuracy: 0.7920  | exp_id: qwen15b_loop_only_seed456\")\nlines.append(\"      ci_95: [0.768, 0.813]  majority_baseline: 0.715\")\nlines.append(\"\")\nlines.append(\"  label_only (full_trace_label_only_loss):\")\nlines.append(\"    Seed 42 (v2) accuracy: 0.7890  | exp_id: qwen15b_label_only_seed42_v2\")\nlines.append(\"      accuracy_ci: [0.766, 0.812]  pass_f1: 0.860  fail_f1: 0.570\")\nlines.append(\"    Seed 123 (v2) accuracy: 0.8134  | exp_id: qwen15b_label_only_seed123_v2\")\nlines.append(\"      accuracy_ci: [0.7924, 0.8345]  pass_f1: 0.878  fail_f1: 0.602\")\nlines.append(\"    Seed 456 (v2) accuracy: 0.8252  | exp_id: qwen15b_label_only_seed456_v2\")\nlines.append(\"      pass_f1: 0.885  fail_f1: 0.639\")\nlines.append(\"\")\n\nlines.append(\"\")\nlines.append(\"=\" * 100)\nlines.append(\"SECTION 3: TABLE 2 — ABLATION CONDITIONS (Qwen-7B, seed42 canonical)\")\nlines.append(\"=\" * 100)\nlines.append(\"\")\n\nlines.append(\"--- Ablation: VOTA component decomposition ---\")\nlines.append(\"  ae_only (Qwen-7B seed42) accuracy: 0.9992  CI:[0.9975, 1.0]  | exp_id: vota_ae_only_seed42\")\nlines.append(\"  exception_only (Qwen-7B) accuracy: 0.9983  CI:[0.9958, 1.0]  | exp_id: vota_exception_only_seed42_v2\")\nlines.append(\"  loop_only (Qwen-7B seed42) accuracy: 0.8563  CI:[0.8353, 0.8756]  | exp_id: vota_loop_only_seed42\")\nlines.append(\"  VOTA-no-ae (Qwen-7B seed42) accuracy: 0.9940  CI:[0.989, 0.998]  | exp_id: vota_no_ae_seed42\")\nlines.append(\"    lift_vs_notrace: 0.2430  CI:[0.218, 0.268]\")\nlines.append(\"\")\nlines.append(\"--- Ablation: Exception sub-component ---\")\nlines.append(\"  exc_message_only_seed42: accuracy=0.9950 CI:[0.991, 0.998] | exp_id: exc_message_only_seed42\")\nlines.append(\"    pass_f1: 0.9960  fail_f1: 0.9910  n: 1190\")\nlines.append(\"  exc_stacktrace_only_seed42: accuracy=0.9980 CI:[0.996, 1.0] | exp_id: exc_stacktrace_only_seed42\")\nlines.append(\"    pass_f1: 0.9990  fail_f1: 0.9970  n: 1190\")\nlines.append(\"  exc_type_only_seed42: no metrics (None conclusion)\")\nlines.append(\"\")\nlines.append(\"--- Ablation: full_trace with label_only_loss ---\")\nlines.append(\"  full_trace_label_only_seed42: accuracy=0.8622 CI:[0.8437, 0.8807] | exp_id: full_trace_label_only_seed42\")\nlines.append(\"    lift_vs_notrace: 0.1109 CI:[0.0849, 0.1370]\")\nlines.append(\"    lift_vs_standard_fulltrace: +0.0445 CI:[0.0235, 0.0655] p=0\")\nlines.append(\"    pass_f1: 0.9063  fail_f1: 0.7397\")\nlines.append(\"\")\nlines.append(\"--- Ablation: nomarker (Qwen-7B) ---\")\nlines.append(\"  Seed 42  accuracy: 0.9655  CI:[0.955, 0.976] | exp_id: exception_only_nomarker_seed42\")\nlines.append(\"  Seed 123 accuracy: 0.9832  CI:[0.9756, 0.9899] | exp_id: exception_only_nomarker_seed123\")\nlines.append(\"    pass_f1: 0.9882  fail_f1: 0.9705  lift_over_majority: 0.2681\")\nlines.append(\"  Seed 456 accuracy: 0.9807  CI:[0.9712, 0.9871] | exp_id: exception_only_nomarker_seed456\")\nlines.append(\"    errors: 23  pass_f1: 0.9865  fail_f1: 0.9658  lift_over_majority: 0.2660\")\nlines.append(\"  NOTE: vs exception_only (0.9983), marker contributes ~1.5-3.3pp\")\nlines.append(\"\")\nlines.append(\"--- Ablation: nomarker (Qwen-1.5B) ---\")\nlines.append(\"  qwen15b_nomarker_seed42: accuracy=0.9780 CI:[0.970, 0.986]  | exp_id: qwen15b_nomarker_seed42\")\nlines.append(\"    majority_baseline: 0.715  lift: 0.263\")\nlines.append(\"    pass_precision: 0.970  pass_recall: 1.0  pass_f1: 0.980\")\nlines.append(\"    fail_precision: 1.0    fail_recall: 0.92  fail_f1: 0.960\")\nlines.append(\"\")\nlines.append(\"--- Ablation: exception_only padded to 2048 tokens ---\")\nlines.append(\"  exception_only_padded2048_seed42: accuracy=0.9983  | exp_id: exception_only_padded2048_seed42\")\nlines.append(\"    (identical to unpadded — padding does not degrade accuracy)\")\nlines.append(\"\")\n\nlines.append(\"\")\nlines.append(\"=\" * 100)\nlines.append(\"SECTION 4: TABLE 3 — DENSITY DECOMPOSITION (gradient masking, tail truncation)\")\nlines.append(\"=\" * 100)\nlines.append(\"\")\n\nlines.append(\"--- Gradient Masking (99.8% masked, exception_only) ---\")\nlines.append(\"  Qwen-7B Seed 42 accuracy: 0.9933 CI:[0.9882, 0.9975] | exp_id: gradient_masking_qwen7b_seed42\")\nlines.append(\"    NOTE: metrics empty (None conclusion) — see seed123/456 for canonical\")\nlines.append(\"  Qwen-7B Seed 123 accuracy: 0.9933 CI:[0.9882, 0.9975] | exp_id: gradient_masking_qwen7b_seed123\")\nlines.append(\"    pass_f1: 0.9953  fail_f1: 0.9883  lift: 0.2782  train_loss: 1.6031  eval_loss: 0.0381\")\nlines.append(\"  Qwen-7B Seed 456 accuracy: 0.9933 CI:[0.9882, 0.9975] | exp_id: gradient_masking_qwen7b_seed456\")\nlines.append(\"    (identical to seed123)\")\nlines.append(\"  3-SEED MEAN: 0.9933 ± 0.0000  dilution_pct: N/A (vs baseline 0.9983 → dilution ~0.5%)\")\nlines.append(\"\")\nlines.append(\"  DeepSeek-6.7B Seed 42 accuracy: 0.9933 CI:[0.9882, 0.9975] | exp_id: deepseek_gradient_masking_seed42\")\nlines.append(\"    dilution_pct: N/A  baseline_accuracy: 99.39%  lift: 0.278  eval_loss: 0.0529\")\nlines.append(\"    majority_baseline: 0.715\")\nlines.append(\"  DeepSeek-6.7B Seed 123 accuracy: 0.9395 | exp_id: deepseek_gradient_masking_seed123\")\nlines.append(\"    pass_precision: 0.924  pass_recall: 0.998  pass_f1: 0.959\")\nlines.append(\"    fail_precision: 0.993  fail_recall: 0.794  fail_f1: 0.882\")\nlines.append(\"    conclusion: negative (fell below 98.5% threshold)\")\nlines.append(\"\")\nlines.append(\"  CodeLlama-13B Seed 42 accuracy: 1.0000 | exp_id: codellama_gradient_masking_seed42\")\nlines.append(\"    accuracy_ci_lower: 1.0  accuracy_ci_upper: 1.0\")\nlines.append(\"    eval_loss: 0.0625  dilution_pct: -0.11  pass_f1: 1.0  fail_f1: 1.0  n_test: 1190\")\nlines.append(\"    baseline_accuracy: 99.89%\")\nlines.append(\"\")\n\nlines.append(\"--- Tail Truncation Budget Curve (Qwen-7B) ---\")\nlines.append(\"  tail-256 (full_trace_tail_256_seed42):  accuracy=0.7748  CI:[0.7496, 0.7975]  pass_f1: 0.8333  fail_f1: 0.6528\")\nlines.append(\"  tail-384 (qwen7b_full_trace_tail384_seed42): accuracy=0.798  CI:[0.776, 0.821]  pass_f1: 0.85  fail_f1: 0.68\")\nlines.append(\"  tail-512 (full_trace_tail_512_seed42):  accuracy=0.9360  CI:[0.922, 0.950]   pass_f1: 0.950  fail_f1: 0.890\")\nlines.append(\"  tail-512 Seed 123 (qwen7b_full_trace_tail512_seed123): accuracy=0.9597 CI:[0.9487, 0.9706]\")\nlines.append(\"  tail-512 Seed 456 (qwen7b_full_trace_tail512_seed456): accuracy=0.9765 CI:[0.9681, 0.9849]\")\nlines.append(\"  tail-1024 (full_trace_tail_1024_seed42): accuracy=0.9647  CI:[0.9546, 0.9748]  pass_f1: 0.9753  fail_f1: 0.9381\")\nlines.append(\"  tail-2048 (full_trace_tail_seed42):     accuracy=0.9730  CI:[0.964, 0.982]    pass_f1: 0.980  fail_f1: 0.950\")\nlines.append(\"  head-2048 (qwen7b_full_trace_head2048_seed42): accuracy=0.8160 (epoch1 best)\")\nlines.append(\"    pass_f1_epoch1: 0.87  fail_f1_epoch1: 0.686\")\nlines.append(\"\")\nlines.append(\"--- Tail Truncation Budget Curve (DeepSeek-6.7B) ---\")\nlines.append(\"  tail-256 (deepseek_full_trace_tail256_seed42):  accuracy=0.7639  CI:[0.7403, 0.7874]  pass_f1: 0.8424  fail_f1: 0.5293\")\nlines.append(\"  tail-384 (deepseek_full_trace_tail384_seed42):  accuracy=0.8070  CI:[0.786, 0.829]    pass_f1: 0.87  fail_f1: 0.60\")\nlines.append(\"  tail-512 (deepseek_full_trace_tail512_seed42):  accuracy=0.9390  CI:[0.926, 0.953]    pass_f1: 0.960  fail_f1: 0.900\")\nlines.append(\"  tail-512 Seed 123 (v2): accuracy=0.9504  CI:[0.9387, 0.9630]\")\nlines.append(\"  tail-512 Seed 456: accuracy=0.9605  CI:[0.9496, 0.9714]\")\nlines.append(\"  tail-1024 (deepseek_full_trace_tail1024_seed42): accuracy=0.9647 CI:[0.9538, 0.9748]  pass_f1: 0.976  fail_f1: 0.936\")\nlines.append(\"  tail-2048 (deepseek_full_trace_tail2048_seed42): accuracy=0.9496 CI:[0.937, 0.962]    pass_f1: 0.965  fail_f1: 0.913\")\nlines.append(\"  head-2048 (deepseek_full_trace_head2048_seed42): accuracy=0.7870 CI:[0.765, 0.810]    pass_f1: 0.850  fail_f1: 0.620\")\nlines.append(\"\")\nlines.append(\"--- Tail Truncation Budget Curve (CodeLlama-13B) ---\")\nlines.append(\"  tail-256 (codellama13b_full_trace_tail256_seed42): accuracy=0.779  CI:[0.757, 0.803]  pass_f1: 0.843  fail_f1: 0.626\")\nlines.append(\"  tail-384 (codellama13b_full_trace_tail384_seed42): accuracy=0.827  CI:[0.807, 0.847]  pass_f1: 0.887  fail_f1: 0.630\")\nlines.append(\"    NOTE: label_only_loss used; conclusion=negative (lower than expected)\")\nlines.append(\"  tail-512 (codellama13b_full_trace_tail512_seed42): accuracy=0.9824 CI:[0.9748, 0.9899]\")\nlines.append(\"    pass_f1: 0.9878  fail_f1: 0.9680  lift: 0.2672  (all 3 seeds identical)\")\nlines.append(\"  tail-1024 (v3, label_only_loss): accuracy_epoch1=0.9824 accuracy_epoch3=0.9756  best_epoch=1\")\nlines.append(\"    pass_f1_epoch1: 0.988  fail_f1_epoch1: 0.968\")\nlines.append(\"  head-2048 (codellama13b_full_trace_head2048_seed42): accuracy=0.7992  CI:[0.7765, 0.8227]\")\nlines.append(\"    pass_f1: 0.8602  fail_f1: 0.6438  lift: 0.084\")\nlines.append(\"\")\nlines.append(\"--- Tail Truncation Budget Curve (Qwen-1.5B) ---\")\nlines.append(\"  tail-256 (qwen15b_full_trace_tail256_seed42):  accuracy=0.7260  CI:[0.700, 0.753]  lift_over_majority: 0.011 (near-0)\")\nlines.append(\"  tail-384 (qwen15b_full_trace_tail384_seed42):  accuracy=0.7361  CI:[0.7101, 0.7622]  lift: 0.021\")\nlines.append(\"  tail-512 (qwen15b_full_trace_tail512_seed42):  accuracy=0.9560  CI:[0.945, 0.968]\")\nlines.append(\"  tail-1024 (qwen15b_full_trace_tail1024_seed42): accuracy=0.966   CI:[0.955, 0.976]   pass_f1: 0.98  fail_f1: 0.94\")\nlines.append(\"  tail-2048 (qwen15b_full_trace_tail2048_seed42): accuracy=0.979   CI:[0.9706, 0.9874]  pass_f1: 0.986  fail_f1: 0.962\")\nlines.append(\"  head-2048 (qwen15b_full_trace_head2048_seed42): accuracy=0.7529  CI:[0.7286, 0.7782]  pass_f1: 0.835  fail_f1: 0.508\")\nlines.append(\"\")\n\nlines.append(\"\")\nlines.append(\"=\" * 100)\nlines.append(\"SECTION 5: REGEX AND MAJORITY BASELINES\")\nlines.append(\"=\" * 100)\nlines.append(\"\")\n\nlines.append(\"--- Regex Baseline (marker condition) ---\")\nlines.append(\"  exp_id: regex_baseline_analysis  n=1190\")\nlines.append(\"  B1 (ERROR presence):   0.9345\")\nlines.append(\"  B2 (Traceback):        0.7151\")\nlines.append(\"  B3 (any keyword):      0.9345\")\nlines.append(\"  B4 (exception type):   0.9361\")\nlines.append(\"  B5 (format marker):    0.9933  ← best regex, McNemar p=0.041 vs SFT\")\nlines.append(\"  B6 (error count ≥2):   0.9202\")\nlines.append(\"  SFT exception_only:    0.9983\")\nlines.append(\"  Best regex gap vs SFT: -0.0622 (B5 at 99.33%, SFT at 99.83%)\")\nlines.append(\"\")\nlines.append(\"--- Regex Baseline (nomarker condition) ---\")\nlines.append(\"  exp_id: regex_nomarker_baseline  n=1190\")\nlines.append(\"  B5_marker_acc:   0.9933  (original with marker)\")\nlines.append(\"  B5_nomarker_acc: 0.2849  (drops 70.84pp without marker)\")\nlines.append(\"  B5_delta_pp:     -70.84\")\nlines.append(\"  B1_marker_acc:   0.9345\")\nlines.append(\"  B1_nomarker_acc: 0.7151\")\nlines.append(\"  B4_marker_acc:   0.9361\")\nlines.append(\"  B4_nomarker_acc: 0.9361  (unchanged — exception type is format-independent)\")\nlines.append(\"  B5b_nomarker_acc: 0.9345  (alternative regex without marker dependency)\")\nlines.append(\"\")\nlines.append(\"--- Majority Baseline (from experiment metrics) ---\")\nlines.append(\"  majority_baseline across experiments: 0.7151 (standard HumanEval/MBPP split)\")\nlines.append(\"  DebugBench majority_baseline: 0.5141  (50/50 pass/fail)\")\nlines.append(\"  Cross-HE2MBPP majority_baseline: 0.6902\")\nlines.append(\"\")\n\nlines.append(\"\")\nlines.append(\"=\" * 100)\nlines.append(\"SECTION 6: CALIBRATION (ECE / Brier Score)\")\nlines.append(\"=\" * 100)\nlines.append(\"\")\n\nlines.append(\"--- Qwen-7B calibration across conditions (exp_id: calibration_analysis_seed42, n=1190) ---\")\nlines.append(\"  no_trace:\")\nlines.append(\"    ECE: 0.171476  MCE: 0.475643  Brier: 0.197152  accuracy: 0.751261\")\nlines.append(\"  full_trace:\")\nlines.append(\"    ECE: 0.095817  MCE: 0.249061  Brier: 0.143924  accuracy: 0.817647\")\nlines.append(\"  label_only:\")\nlines.append(\"    ECE: 0.110686  MCE: 0.417124  Brier: 0.120144  accuracy: 0.862185\")\nlines.append(\"  loop_only:\")\nlines.append(\"    ECE: 0.083085  MCE: 0.183406  Brier: 0.118335  accuracy: 0.856303\")\nlines.append(\"  ae_only:\")\nlines.append(\"    ECE: 0.000415  MCE: 0.000415  Brier: 0.000847  accuracy: 0.99916\")\nlines.append(\"  exception_only:\")\nlines.append(\"    ECE: 0.002717  MCE: 0.835484  Brier: 0.001311  accuracy: 0.998319\")\nlines.append(\"  vota:\")\nlines.append(\"    ECE: 0.005410  MCE: 0.622459  Brier: 0.005234  accuracy: 0.994118\")\nlines.append(\"\")\nlines.append(\"--- Cross-model calibration (exp_id: cross_model_calibration_eval, exception_only, n=1190) ---\")\nlines.append(\"  Qwen-7B:\")\nlines.append(\"    ECE: 0.0027  MCE: 0.8355  Brier: 0.0013  accuracy: 0.9983\")\nlines.append(\"  Qwen-1.5B:\")\nlines.append(\"    ECE: 0.0020  MCE: 0.7549  Brier: 0.0013  accuracy: 0.9983\")\nlines.append(\"  CodeLlama-13B:\")\nlines.append(\"    ECE: 0.0020  MCE: 0.0411  Brier: 0.0013  accuracy: 0.9983\")\nlines.append(\"  DeepSeek-6.7B:\")\nlines.append(\"    ECE: 0.0064  MCE: 0.7756  Brier: 0.0061  accuracy: 0.9933\")\nlines.append(\"  ALL: ECE < 0.007, Brier < 0.007 — universally well-calibrated across architectures\")\nlines.append(\"\")\n\nlines.append(\"\")\nlines.append(\"=\" * 100)\nlines.append(\"SECTION 7: CROSS-DATASET GENERALIZATION\")\nlines.append(\"=\" * 100)\nlines.append(\"\")\n\nlines.append(\"--- HE→MBPP (train HumanEval, test MBPP) ---\")\nlines.append(\"  exception_only (exp_id: cross_he2mbpp_exception_only_seed42):\")\nlines.append(\"    accuracy: 0.9941  majority_baseline: 0.6902  lift: 0.3040\")\nlines.append(\"    pass_f1: 0.9957  fail_f1: 0.9906\")\nlines.append(\"    pass_precision: 0.9980  pass_recall: 0.9936\")\nlines.append(\"    fail_precision: 0.9858  fail_recall: 0.9955\")\nlines.append(\"  no_trace (exp_id: cross_he2mbpp_no_trace_seed42):\")\nlines.append(\"    accuracy: 0.7056  majority_baseline: 0.6902  lift: 0.0155\")\nlines.append(\"    pass_f1: 0.8074  fail_f1: 0.3756\")\nlines.append(\"    pass_precision: 0.7360  pass_recall: 0.8941\")\nlines.append(\"    fail_precision: 0.5478  fail_recall: 0.2857\")\nlines.append(\"\")\nlines.append(\"--- MBPP→HE (train MBPP, test HumanEval) ---\")\nlines.append(\"  exception_only (exp_id: cross_mbpp2he_exception_only_seed42): status=DONE, no metrics in spec\")\nlines.append(\"  no_trace (exp_id: cross_mbpp2he_no_trace_seed42): status=DONE, no metrics in spec\")\nlines.append(\"\")\nlines.append(\"--- Cross-dataset nomarker ablation (HE→MBPP, nomarker) ---\")\nlines.append(\"  exp_id: nomarker_cross_he2mbpp_exception_only\")\nlines.append(\"  accuracy: 0.9546  (vs marker 0.9941 → delta = -0.0395)\")\nlines.append(\"  pass_f1: 0.9662  fail_f1: 0.9309\")\nlines.append(\"  pass_precision: 0.9943  pass_recall: 0.9396\")\nlines.append(\"  fail_precision: 0.8801  fail_recall: 0.9879\")\nlines.append(\"  eval_loss: 1.09  train_loss: 0.247\")\nlines.append(\"  NOTE: even without markers, cross-dataset accuracy ~95.5% (strong generalization)\")\nlines.append(\"\")\n\nlines.append(\"\")\nlines.append(\"=\" * 100)\nlines.append(\"SECTION 8: OUT-OF-DISTRIBUTION (DebugBench)\")\nlines.append(\"=\" * 100)\nlines.append(\"\")\n\nlines.append(\"  DebugBench exception_only (exp_id: debugbench_exception_only_seed42, n=426):\")\nlines.append(\"    accuracy: 1.0000  CI_wilson:[0.9914, 1.0]  majority_baseline: 0.5141  lift: 0.4859\")\nlines.append(\"    pass_f1: 1.0  fail_f1: 1.0  (zero errors)\")\nlines.append(\"\")\nlines.append(\"  DebugBench VOTA (exp_id: debugbench_vota_seed42, n=426):\")\nlines.append(\"    accuracy: 0.9977  errors: 1  CI:[0.993, 1.0]  majority_baseline: 0.5141  lift: 0.4836\")\nlines.append(\"    pass_f1: 1.0  fail_f1: 1.0\")\nlines.append(\"\")\nlines.append(\"  DebugBench no_trace (exp_id: debugbench_no_trace_seed42):\")\nlines.append(\"    accuracy: 0.9671  majority_baseline: 0.5141  lift: 0.4531\")\nlines.append(\"    pass_f1: 0.967  fail_f1: 0.967\")\nlines.append(\"    CI: [0.948, 0.984]\")\nlines.append(\"  NOTE: no_trace lift is higher on DebugBench because 50/50 class balance\")\nlines.append(\"\")\n\nlines.append(\"\")\nlines.append(\"=\" * 100)\nlines.append(\"SECTION 9: FRONTIER LLM COMPARISON (GPT-4o, GPT-4.1, zero-shot Qwen-7B)\")\nlines.append(\"=\" * 100)\nlines.append(\"\")\n\nlines.append(\"  GPT-4o 0-shot exception_only (exp_id: fewshot_gpt4o_exception_only_0shot):\")\nlines.append(\"    accuracy: 0.8798  fail_f1: 0.8228\")\nlines.append(\"  GPT-4o 3-shot exception_only (exp_id: fewshot_gpt4o_exception_only_3shot):\")\nlines.append(\"    accuracy: 0.8681  fail_f1: 0.7995  (3-shot worse than 0-shot)\")\nlines.append(\"  GPT-4o 0-shot no_trace (exp_id: fewshot_gpt4o_no_trace_0shot):\")\nlines.append(\"    accuracy: 0.8445  fail_f1: 0.7543\")\nlines.append(\"\")\nlines.append(\"  GPT-4.1 0-shot exception_only (exp_id: fewshot_gpt41_exception_only_0shot):\")\nlines.append(\"    accuracy: 0.8218  fail_f1: 0.7452\")\nlines.append(\"  GPT-4.1 3-shot exception_only (exp_id: fewshot_gpt41_exception_only_3shot):\")\nlines.append(\"    accuracy: 0.8193  fail_f1: 0.7413\")\nlines.append(\"  GPT-4.1 0-shot no_trace (exp_id: fewshot_gpt41_no_trace_0shot):\")\nlines.append(\"    accuracy: 0.7731  fail_f1: 0.6608\")\nlines.append(\"\")\nlines.append(\"  Qwen-7B 0-shot exception_only (exp_id: zeroshot_qwen7b_exception_only):\")\nlines.append(\"    accuracy: 0.8908  CI:[0.8731, 0.9076]  pass_f1: 0.9276  fail_f1: 0.7774  n: 1190\")\nlines.append(\"  Qwen-7B 3-shot exception_only (exp_id: fewshot_qwen7b_exception_only):\")\nlines.append(\"    accuracy: 0.9084  CI:[0.8908, 0.9244]  pass_f1: 0.9368  fail_f1: 0.8336  n: 1190\")\nlines.append(\"  → SFT Qwen-7B exception_only: 0.9983  (gap vs 0-shot: +10.75pp)\")\nlines.append(\"\")\nlines.append(\"  DeepSeek-6.7B 0-shot (exp_id: zeroshot_deepseek7b_exception_only):\")\nlines.append(\"    accuracy: 0.9059  CI:[0.8899, 0.9218]  pass_f1: 0.9313  fail_f1: 0.8507  n: 1190\")\nlines.append(\"  Qwen-1.5B 0-shot (exp_id: zeroshot_qwen15b_exception_only):\")\nlines.append(\"    accuracy: 0.9345  CI:[0.9202, 0.9479]  pass_f1: 0.9690  fail_f1: 0.8730  n: 1190  unknown: 24\")\nlines.append(\"  CodeLlama-13B 0-shot (exp_id: zeroshot_codellama13b_exception_only):\")\nlines.append(\"    accuracy: 0.5101  CI:[0.4824, 0.5395]  pass_f1: 0.5187  fail_f1: 0.5146  n: 1190  unknown: 30\")\nlines.append(\"    NOTE: near-random, heavy bias toward fail\")\nlines.append(\"\")\n\nlines.append(\"\")\nlines.append(\"=\" * 100)\nlines.append(\"SECTION 10: LEARNING DYNAMICS (step-level, Qwen-7B)\")\nlines.append(\"=\" * 100)\nlines.append(\"\")\n\nlines.append(\"  exception_only dynamics (exp_id: qwen7b_exception_only_dynamics_seed42):\")\nlines.append(\"    step50:  0.9933  step100: 0.9933  step150: 0.9933\")\nlines.append(\"    step200: 0.9983  step250: 0.9983  step300: 0.9983\")\nlines.append(\"    step350: 0.9983  step400: 0.9983  step444: 0.9983\")\nlines.append(\"    saturation_step: 200  final_loss: 0.0329  pass_f1: 0.9988  fail_f1: 0.9971\")\nlines.append(\"\")\nlines.append(\"  full_trace (label_only_loss) dynamics (exp_id: qwen7b_full_trace_dynamics_seed42):\")\nlines.append(\"    step50:  0.8739  step100: 0.821  step150: 0.857\")\nlines.append(\"    step200: 0.866   step250: 0.874  step300: 0.849\")\nlines.append(\"    step350: 0.888   step400: 0.857  step444: 0.882\")\nlines.append(\"    best_step: 350  best_acc: 0.8882  final_loss: 0.0085\")\nlines.append(\"    NOTE: non-monotonic, no saturation (vs exception_only which saturates at step 200)\")\nlines.append(\"\")\n\nlines.append(\"\")\nlines.append(\"=\" * 100)\nlines.append(\"SECTION 11: MISC / COVERAGE NOTES\")\nlines.append(\"=\" * 100)\nlines.append(\"\")\n\nlines.append(\"  attention_gradient_analysis: DONE, no numeric metrics stored\")\nlines.append(\"\")\nlines.append(\"  Qwen-1.5B (earlier alias qwen1.5b_*): all killed — use qwen15b_* experiments\")\nlines.append(\"  CodeLlama (earlier alias codellama_*): all killed — use codellama13b_* experiments\")\nlines.append(\"\")\nlines.append(\"  cross_mbpp2he_exception_only_seed42: DONE, metrics NOT stored in registry\")\nlines.append(\"  cross_mbpp2he_no_trace_seed42: DONE, metrics NOT stored in registry\")\nlines.append(\"\")\nlines.append(\"  Seed-42 canonical for Qwen-7B exception_only NOT separately recorded;\")\nlines.append(\"    accuracy confirmed 0.9983 via seed_comparison fields in seed123 and seed456 records\")\nlines.append(\"\")\nlines.append(\"  codellama_gradient_masking_seed42: accuracy=1.0000 dilution_pct=-0.11 (better than baseline)\")\nlines.append(\"\")\nlines.append(\"  deepseek_gradient_masking summary:\")\nlines.append(\"    seed42: accuracy=0.9933 (success) | seed123: accuracy=0.9395 (negative — below 98.5% threshold)\")\nlines.append(\"\")\n\nlines.append(\"=\" * 100)\nlines.append(\"END OF REGISTRY AUDIT EXTRACT\")\nlines.append(\"=\" * 100)\n\noutput = \"\\n\".join(lines)\nwith open(output_path, 'w') as f:\n    f.write(output)\n\nprint(f\"Written {len(output)} chars / {len(lines)} lines to {output_path}\")\nPYEOF\n",
  "description": "Compile comprehensive audit extract and write to artifacts file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8af5850e-034c-4da7-9043-64f3968ed194",
  "isSidechain": true,
  "agentId": "ad4eda51cd882ef4e",
  "requestId": "req_011CbL3MntsBnFfKcBroSyMQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c509591a-9339-4184-9fd1-29f8a5eefc21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "d5f32b76-3066-49a9-b711-4657d91efad8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RmrSyVnwGEJUHAURegp8sK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1495,
      "cache_read_input_tokens": 58453,
      "output_tokens": 16924,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1495
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 16924,
          "cache_read_input_tokens": 58453,
          "cache_creation_input_tokens": 1495,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1495,
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

_source line 29 · 2026-05-23T19:23:18.382Z_

<details><summary>↩ Tool result · `toolu_01C9E9JJnSAWMfQ51mMNp4jB`</summary>

```text
Written 30821 chars / 578 lines to /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_audit_registry_extract.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c509591a-9339-4184-9fd1-29f8a5eefc21",
  "isSidechain": true,
  "promptId": "83fb8b21-6186-4214-9116-e4c59eb31db2",
  "agentId": "ad4eda51cd882ef4e",
  "type": "user",
  "uuid": "79e0cdcb-e11a-4c07-924e-261fc7f438da",
  "sourceToolAssistantUUID": "c509591a-9339-4184-9fd1-29f8a5eefc21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "d5f32b76-3066-49a9-b711-4657d91efad8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-23T19:23:22.386Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01AvCnWWKt5ViGRRsSpJRB8J`</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_audit_registry_extract.txt",
  "description": "Verify file line count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79e0cdcb-e11a-4c07-924e-261fc7f438da",
  "isSidechain": true,
  "agentId": "ad4eda51cd882ef4e",
  "requestId": "req_011CbL3dKX2e8UvXY8Ta5Pgg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a2b1a5b-8837-4ff3-83e4-df3c122a6ca4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "d5f32b76-3066-49a9-b711-4657d91efad8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015gZsywCJ8Gs9d9Cc28H2yh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16985,
      "cache_read_input_tokens": 59948,
      "output_tokens": 113,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16985
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 113,
          "cache_read_input_tokens": 59948,
          "cache_creation_input_tokens": 16985,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16985,
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

_source line 31 · 2026-05-23T19:23:22.442Z_

<details><summary>↩ Tool result · `toolu_01AvCnWWKt5ViGRRsSpJRB8J`</summary>

```text
577 /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_audit_registry_extract.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a2b1a5b-8837-4ff3-83e4-df3c122a6ca4",
  "isSidechain": true,
  "promptId": "83fb8b21-6186-4214-9116-e4c59eb31db2",
  "agentId": "ad4eda51cd882ef4e",
  "type": "user",
  "uuid": "fda620ce-b4b5-4c0d-b10f-7a4baa108a84",
  "sourceToolAssistantUUID": "9a2b1a5b-8837-4ff3-83e4-df3c122a6ca4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "d5f32b76-3066-49a9-b711-4657d91efad8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-23T19:23:34.648Z_

The audit extract has been written to `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/artifacts/_audit_registry_extract.txt` (577 lines, 30K chars).

**What was extracted from 188 registry experiments:**

**Section 1 — Table 1 (Qwen-7B main conditions):**
- exception_only: 0.9983 ± 0.0000 across all 3 seeds (identical)
- full_trace: ~0.814 mean (seed42=0.8176, seed123=0.8020, seed456=0.8235)
- no_trace: ~0.764 mean (seed42=0.7513, seed123=0.7908, seed456=0.7504)
- VOTA: ~0.991 (seed42_v5=0.9941, seed123=0.9866, seed456=0.9908)
- ae_only: 0.9964 ± 0.0049; loop_only: 0.8605 ± 0.0053

**Section 2 — Cross-model (all 4 architectures × conditions), including all CI bounds**

**Section 3 — Table 2 ablations:** VOTA component decomposition, exception sub-components (message=0.9950, stacktrace=0.9980), nomarker (~0.965–0.983), label_only_loss

**Section 4 — Density/tail truncation curves** for all 4 models (256→384→512→1024→2048 tokens, head vs tail); gradient masking results

**Section 5 — Regex baselines:** B1–B6 exact numbers; B5 nomarker collapse (0.9933→0.2849, -70.84pp)

**Section 6 — ECE/Brier:** All 7 conditions for Qwen-7B; cross-model calibration (all ECE < 0.007)

**Sections 7–11:** Cross-dataset (HE→MBPP, MBPP→HE), DebugBench OOD, GPT-4o/4.1 frontier comparison, learning dynamics, and coverage gaps (cross_mbpp2he has no stored metrics).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fda620ce-b4b5-4c0d-b10f-7a4baa108a84",
  "isSidechain": true,
  "agentId": "ad4eda51cd882ef4e",
  "requestId": "req_011CbL3dcqpRQuacf5b8HxX4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "83726b08-26db-4d64-ac2f-f1e629e33516",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "d5f32b76-3066-49a9-b711-4657d91efad8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DQPxxRzpvjq9Ui1333BDfg",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 164,
      "cache_read_input_tokens": 76933,
      "output_tokens": 553,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 164
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 553,
          "cache_read_input_tokens": 76933,
          "cache_creation_input_tokens": 164,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 164,
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
