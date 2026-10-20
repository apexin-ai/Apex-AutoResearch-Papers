# Research conversation: I need you to extract experiment data from a large JSON file. The file is at: /home/ubuntu/.claude-account-1/projects/-h

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-aac106f26c591f937.jsonl`
- **Structured JSON:** [`92c3be41efad4aa776d6.json`](../../sessions/92/92c3be41efad4aa776d6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

15 recorded events

### User

_source line 1 · 2026-05-21T20:08:07.297Z_

I need you to extract experiment data from a large JSON file. The file is at:
/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/d6340ee6-f9f9-4ade-b37f-565650398cf3/tool-results/mcp-agent-ml-research-read_registry-1779394072534.txt

The file has schema: {result: string} where result is a JSON string containing experiment data.

I need you to:

1. First probe the structure with jq (type/length/keys)
2. Extract ALL experiments whose exp_id starts with "eval_math500" - for each, extract:
   - exp_id
   - status
   - accuracy (from metrics or results)
   - n_correct, n_total, truncated (from metrics or results)
   - model_name or checkpoint_source (from spec)
   - any info about sparsity, method (CKA, Standard, RASP, Random), stage (SFT, GRPO)
   - the full metrics/results object

3. Also extract ALL experiments whose exp_id starts with "eval_gsm8k" - same fields as above.

Return ALL extracted data verbatim in a structured format. Do not summarize - I need every field value. Group by eval_math500 vs eval_gsm8k.

Use bash with jq or python to parse the file. The file is JSON with a "result" key containing a JSON string that needs to be parsed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "1f34c4b2-9824-4de5-b2b7-5e9407290ac0",
  "agentId": "aac106f26c591f937",
  "type": "user",
  "uuid": "47e04f4f-cc69-4b18-87bc-2ec57cbaffdf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "d6340ee6-f9f9-4ade-b37f-565650398cf3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T20:08:07.302Z_

```json
{
  "parentUuid": "47e04f4f-cc69-4b18-87bc-2ec57cbaffdf",
  "isSidechain": true,
  "agentId": "aac106f26c591f937",
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
      "TodoWrite",
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
      "TodoWrite",
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
  "uuid": "62a41c90-c21f-4812-88cf-1429d7f5844b",
  "timestamp": "2026-05-21T20:08:07.302Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "d6340ee6-f9f9-4ade-b37f-565650398cf3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-21T20:08:16.221Z_



Let me start by probing the file structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62a41c90-c21f-4812-88cf-1429d7f5844b",
  "isSidechain": true,
  "agentId": "aac106f26c591f937",
  "requestId": "req_011CbGKRhZMFMqpeF3QWrns3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2cc255eb-3742-44de-bd3f-069ce999d9f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "d6340ee6-f9f9-4ade-b37f-565650398cf3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BkoKhnQApb7ht74vXrsXot",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15044,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15044,
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

_source line 4 · 2026-05-21T20:08:17.340Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01MQHQ5kmG4793KXwqPKB47n`</summary>

```json
{
  "command": "wc -c /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/d6340ee6-f9f9-4ade-b37f-565650398cf3/tool-results/mcp-agent-ml-research-read_registry-1779394072534.txt",
  "description": "Check file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cc255eb-3742-44de-bd3f-069ce999d9f8",
  "isSidechain": true,
  "agentId": "aac106f26c591f937",
  "requestId": "req_011CbGKRhZMFMqpeF3QWrns3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "904c3ed1-f675-4613-9c88-2d19c82a23a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "d6340ee6-f9f9-4ade-b37f-565650398cf3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BkoKhnQApb7ht74vXrsXot",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15044,
      "cache_read_input_tokens": 0,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15044
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 178,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15044,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15044,
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

_source line 5 · 2026-05-21T20:08:17.497Z_

<details><summary>↩ Tool result · `toolu_01MQHQ5kmG4793KXwqPKB47n`</summary>

```text
101465 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/d6340ee6-f9f9-4ade-b37f-565650398cf3/tool-results/mcp-agent-ml-research-read_registry-1779394072534.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "904c3ed1-f675-4613-9c88-2d19c82a23a8",
  "isSidechain": true,
  "promptId": "1f34c4b2-9824-4de5-b2b7-5e9407290ac0",
  "agentId": "aac106f26c591f937",
  "type": "user",
  "uuid": "58e1e435-43f7-4537-a5be-7dda935c1273",
  "sourceToolAssistantUUID": "904c3ed1-f675-4613-9c88-2d19c82a23a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "d6340ee6-f9f9-4ade-b37f-565650398cf3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T20:08:26.323Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01VuLF4afY914dmoSBmvBozG`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/d6340ee6-f9f9-4ade-b37f-565650398cf3/tool-results/mcp-agent-ml-research-read_registry-1779394072534.txt\"\npython3 -c \"\nimport json, sys\n\nwith open('$FILE') as f:\n    outer = json.load(f)\n\nprint('Outer keys:', list(outer.keys()))\nprint('Type of result:', type(outer.get('result')))\n\n# Parse the inner JSON string\ninner = json.loads(outer['result'])\nprint('Inner type:', type(inner))\nif isinstance(inner, dict):\n    print('Inner keys:', list(inner.keys())[:20])\n    print('Total keys:', len(inner.keys()))\nelif isinstance(inner, list):\n    print('Inner length:', len(inner))\n    if len(inner) > 0:\n        print('First item type:', type(inner[0]))\n        if isinstance(inner[0], dict):\n            print('First item keys:', list(inner[0].keys()))\n\"\n",
  "description": "Probe JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58e1e435-43f7-4537-a5be-7dda935c1273",
  "isSidechain": true,
  "agentId": "aac106f26c591f937",
  "requestId": "req_011CbGKST9hfkx4uZiaaXk9P",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "958f7d83-2078-4d34-9f7c-e04f9f9fe078",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "d6340ee6-f9f9-4ade-b37f-565650398cf3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MXLjxjQdEPTuabXWhnYMhk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 15044,
      "output_tokens": 365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1125
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 365,
          "cache_read_input_tokens": 15044,
          "cache_creation_input_tokens": 1125,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1125,
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

_source line 7 · 2026-05-21T20:08:26.447Z_

<details><summary>↩ Tool result · `toolu_01VuLF4afY914dmoSBmvBozG`</summary>

```text
Outer keys: ['result']
Type of result: &lt;class 'str'>
Inner type: &lt;class 'dict'>
Inner keys: ['success', 'data', 'error', 'metadata']
Total keys: 4
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "958f7d83-2078-4d34-9f7c-e04f9f9fe078",
  "isSidechain": true,
  "promptId": "1f34c4b2-9824-4de5-b2b7-5e9407290ac0",
  "agentId": "aac106f26c591f937",
  "type": "user",
  "uuid": "ba6760d7-0c53-438d-bf16-1789e8280326",
  "sourceToolAssistantUUID": "958f7d83-2078-4d34-9f7c-e04f9f9fe078",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "d6340ee6-f9f9-4ade-b37f-565650398cf3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T20:08:31.954Z_

<details open><summary>🔧 Tool call — Bash · `toolu_019mrJupmBmoZL3E5kk9JXqj`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/d6340ee6-f9f9-4ade-b37f-565650398cf3/tool-results/mcp-agent-ml-research-read_registry-1779394072534.txt\"\npython3 -c \"\nimport json\n\nwith open('$FILE') as f:\n    outer = json.load(f)\ninner = json.loads(outer['result'])\n\nprint('success:', inner.get('success'))\nprint('error:', inner.get('error'))\nprint('metadata:', json.dumps(inner.get('metadata'), indent=2))\n\ndata = inner.get('data', {})\nprint('data type:', type(data))\nif isinstance(data, dict):\n    print('data keys:', list(data.keys())[:30])\n    print('total data keys:', len(data.keys()))\n    # Check first value structure\n    for k in list(data.keys())[:1]:\n        print(f'Sample key: {k}')\n        print(f'Sample value type: {type(data[k])}')\n        if isinstance(data[k], dict):\n            print(f'Sample value keys: {list(data[k].keys())}')\nelif isinstance(data, list):\n    print('data length:', len(data))\n\"\n",
  "description": "Probe inner data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba6760d7-0c53-438d-bf16-1789e8280326",
  "isSidechain": true,
  "agentId": "aac106f26c591f937",
  "requestId": "req_011CbGKT7RaNGs1WdrjWQfn2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7384079-5d9a-4602-96fe-92b15243fe01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "d6340ee6-f9f9-4ade-b37f-565650398cf3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011aQdDRdX2Qtr5TcnXBVW6G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 430,
      "cache_read_input_tokens": 16169,
      "output_tokens": 414,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 430
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 414,
          "cache_read_input_tokens": 16169,
          "cache_creation_input_tokens": 430,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 430,
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

_source line 9 · 2026-05-21T20:08:32.034Z_

<details><summary>↩ Tool result · `toolu_019mrJupmBmoZL3E5kk9JXqj`</summary>

```text
success: True
error: None
metadata: {
  "elapsed_seconds": 0.1996
}
data type: &lt;class 'dict'>
data keys: ['experiments', 'count', 'total', 'baseline']
total data keys: 4
Sample key: experiments
Sample value type: &lt;class 'dict'>
Sample value keys: ['grpo_cka_only_25', 'eval_humaneval_sft_standard_25', 'eval_math500_sft_standard_25_v2', 'sft_alpha4_20_v2', 'eval_math500_sft_standard_25', 'eval_gsm8k_grpo_cka_only_15_seed123', 'prune_eval_cka_only_30', 'prune_eval_standard_30', 'grpo_cka_only_15_v2', 'grpo_cka_only_20_seed456', 'eval_humaneval_sft_standard_20_1p5b_2048', 'eval_humaneval_sft_standard_20_2048_v3', 'eval_humaneval_sft_cka_only_20_1p5b_2048', 'eval_humaneval_grpo_cka_only_20_1p5b_2048', 'eval_mbpp_grpo_standard_20_v3', 'eval_gsm8k_grpo_cka_only_20_seed123', 'eval_mbpp_sft_standard_20_v4', 'eval_mbpp_grpo_standard_20', 'eval_mbpp_sft_standard_20', 'rci_formalization_plan036', 'eval_mbpp_sft_standard_20_clean', 'eval_mbpp_grpo_cka_only_20', 'eval_gsm8k_sft_shortgpt_20', 'grpo_shortgpt_20', 'eval_mbpp_dense_unpruned', 'sft_shortgpt_20', 'eval_gsm8k_grpo_rasp_20_fair', 'grpo_cka_only_20_seed123', 'grpo_random_20', 'eval_gsm8k_grpo_standard_20_fair_v2', 'eval_humaneval_grpo_standard_20_fair_2048_v3', 'eval_humaneval_sft_cka_only_20_2048_v2', 'eval_humaneval_grpo_standard_20_fair_2048', 'eval_math500_sft_standard_20_2048_v2', 'eval_humaneval_grpo_cka_only_20_2048', 'eval_humaneval_sft_cka_only_20_2048', 'eval_humaneval_grpo_rasp_20_fair_2048', 'eval_gsm8k_grpo_standard_20_extended_300', 'eval_humaneval_grpo_rasp_20_512', 'eval_humaneval_grpo_standard_20_512', 'eval_humaneval_sft_rasp_20_512', 'eval_humaneval_sft_standard_20_512', 'eval_humaneval_unpruned_512', 'eval_humaneval_grpo_rasp_20_2048', 'eval_humaneval_grpo_standard_20_2048', 'eval_humaneval_sft_rasp_20_2048', 'eval_humaneval_unpruned_2048', 'grpo_unstructured_20', 'eval_gsm8k_grpo_cka_only_20_extended_300', 'eval_gsm8k_sft_standard_20_1p5b', 'eval_math500_grpo_cka_only_20_2048', 'eval_gsm8k_sft_rasp_20_1p5b', 'inference_bench_clean_v2', 'eval_math500_grpo_rasp_20_v3', 'eval_gsm8k_grpo_cka_only_20_v2', 'grpo_cka_only_20_1p5b', 'grpo_cka_only_20', 'eval_gsm8k_grpo_rasp_20_1p5b', 'eval_gsm8k_grpo_cka_only_20_1p5b', 'grpo_standard_20_extended_300', 'scoring_ablation_magnitude_20', 'eval_math500_grpo_unpruned', 'eval_humaneval_sft_standard_20_2048_v2', 'eval_humaneval_sft_standard_20_2048', 'eval_gradient_postsft_v2', 'eval_postprune_25', 'scoring_ablation_batch_v2', 'eval_sft_rasp_rlvr_20_qwen_math', 'sft_standard_20_westd_retrain', 'eval_sft_standard_20_westd_n100', 'eval_sft_rasp_20_westd_n100', 'grpo_unpruned_baseline', 'grasp_baseline_westd', 'eval_sft_alpha_0p5', 'eval_sft_grasp_20', 'eval_sft_alpha_2p0']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7384079-5d9a-4602-96fe-92b15243fe01",
  "isSidechain": true,
  "promptId": "1f34c4b2-9824-4de5-b2b7-5e9407290ac0",
  "agentId": "aac106f26c591f937",
  "type": "user",
  "uuid": "74294505-0c51-43a1-bc8d-c92c35dab903",
  "sourceToolAssistantUUID": "d7384079-5d9a-4602-96fe-92b15243fe01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "d6340ee6-f9f9-4ade-b37f-565650398cf3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-21T20:08:42.452Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0173q9Jy5GyFWUqWNk6NzAmi`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/d6340ee6-f9f9-4ade-b37f-565650398cf3/tool-results/mcp-agent-ml-research-read_registry-1779394072534.txt\"\npython3 -c \"\nimport json\n\nwith open('$FILE') as f:\n    outer = json.load(f)\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Find all eval_math500 and eval_gsm8k experiments\nmath500 = {k: v for k, v in experiments.items() if k.startswith('eval_math500')}\ngsm8k = {k: v for k, v in experiments.items() if k.startswith('eval_gsm8k')}\n\nprint(f'eval_math500 experiments: {len(math500)}')\nprint('Keys:', sorted(math500.keys()))\nprint()\nprint(f'eval_gsm8k experiments: {len(gsm8k)}')\nprint('Keys:', sorted(gsm8k.keys()))\nprint()\n\n# Show structure of one example\nif math500:\n    k = list(math500.keys())[0]\n    print(f'Sample experiment structure ({k}):')\n    print(json.dumps(math500[k], indent=2))\n\"\n",
  "description": "Find all eval_math500 and eval_gsm8k experiments and show structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74294505-0c51-43a1-bc8d-c92c35dab903",
  "isSidechain": true,
  "agentId": "aac106f26c591f937",
  "requestId": "req_011CbGKTXVBLyziZK4QP4QH2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c53dbb84-a5fd-44f7-8db0-ba5710abc708",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "d6340ee6-f9f9-4ade-b37f-565650398cf3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WAQjhe2YSK5ozvYHtUFTSR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1765,
      "cache_read_input_tokens": 16599,
      "output_tokens": 442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1765
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 442,
          "cache_read_input_tokens": 16599,
          "cache_creation_input_tokens": 1765,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1765,
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

_source line 11 · 2026-05-21T20:08:42.556Z_

<details><summary>↩ Tool result · `toolu_0173q9Jy5GyFWUqWNk6NzAmi`</summary>

```text
eval_math500 experiments: 6
Keys: ['eval_math500_grpo_cka_only_20_2048', 'eval_math500_grpo_rasp_20_v3', 'eval_math500_grpo_unpruned', 'eval_math500_sft_standard_20_2048_v2', 'eval_math500_sft_standard_25', 'eval_math500_sft_standard_25_v2']

eval_gsm8k experiments: 12
Keys: ['eval_gsm8k_grpo_cka_only_15_seed123', 'eval_gsm8k_grpo_cka_only_20_1p5b', 'eval_gsm8k_grpo_cka_only_20_extended_300', 'eval_gsm8k_grpo_cka_only_20_seed123', 'eval_gsm8k_grpo_cka_only_20_v2', 'eval_gsm8k_grpo_rasp_20_1p5b', 'eval_gsm8k_grpo_rasp_20_fair', 'eval_gsm8k_grpo_standard_20_extended_300', 'eval_gsm8k_grpo_standard_20_fair_v2', 'eval_gsm8k_sft_rasp_20_1p5b', 'eval_gsm8k_sft_shortgpt_20', 'eval_gsm8k_sft_standard_20_1p5b']

Sample experiment structure (eval_math500_sft_standard_25_v2):
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-21T02:55:44.254Z",
  "updated_at": "2026-05-21T19:55:31.110Z",
  "hypothesis": "MATH-500 eval on Standard 25% SFT checkpoint (retry with max_new_tokens=2048). v1 killed due to 320s/topic with default max_new_tokens=4096.",
  "spec": {
    "command": "python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_standard_25.json",
    "server": "westb-23072",
    "gpu": "cuda:0",
    "pid": "62714",
    "data_path": "MATH-500",
    "data_count": 500,
    "model_name": "DeepSeek-R1-Distill-Qwen-7B-pruned-standard-25pct-SFT",
    "seed": 42,
    "checkpoint_source": "sft_standard_25",
    "eval_data": "MATH-500",
    "checkpoint_path": "N/A (eval)",
    "log_path": "/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_standard_25.json"
  },
  "conclusion": "success",
  "metrics": {
    "accuracy": 0.13,
    "n_correct": 65,
    "n_total": 500,
    "truncated": 318,
    "avg_response_length": 1376
  },
  "completed_at": "2026-05-21T19:55:31.111Z"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c53dbb84-a5fd-44f7-8db0-ba5710abc708",
  "isSidechain": true,
  "promptId": "1f34c4b2-9824-4de5-b2b7-5e9407290ac0",
  "agentId": "aac106f26c591f937",
  "type": "user",
  "uuid": "0edbea8d-3abf-49bb-a348-8f344633d7d9",
  "sourceToolAssistantUUID": "c53dbb84-a5fd-44f7-8db0-ba5710abc708",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "d6340ee6-f9f9-4ade-b37f-565650398cf3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-21T20:08:45.262Z_

Now let me extract all the data for both groups.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0edbea8d-3abf-49bb-a348-8f344633d7d9",
  "isSidechain": true,
  "agentId": "aac106f26c591f937",
  "requestId": "req_011CbGKUJJhVPZ9cdjtMBXMK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc9d93bc-3f16-4b64-8718-3b5a04aab144",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "d6340ee6-f9f9-4ade-b37f-565650398cf3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012yEXEnJuc5HCJYW9m3dMkX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1362,
      "cache_read_input_tokens": 18364,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1362,
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

_source line 13 · 2026-05-21T20:08:56.993Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01T3woPAEbaEWtnNY9FDbodK`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/d6340ee6-f9f9-4ade-b37f-565650398cf3/tool-results/mcp-agent-ml-research-read_registry-1779394072534.txt\"\npython3 -c \"\nimport json\n\nwith open('$FILE') as f:\n    outer = json.load(f)\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Extract all eval_math500\nmath500 = {k: v for k, v in sorted(experiments.items()) if k.startswith('eval_math500')}\ngsm8k = {k: v for k, v in sorted(experiments.items()) if k.startswith('eval_gsm8k')}\n\nprint('=' * 80)\nprint('GROUP: eval_math500 ({} experiments)'.format(len(math500)))\nprint('=' * 80)\nfor exp_id, exp in math500.items():\n    print(json.dumps({\n        'exp_id': exp_id,\n        'status': exp.get('status'),\n        'conclusion': exp.get('conclusion'),\n        'hypothesis': exp.get('hypothesis'),\n        'spec': exp.get('spec'),\n        'metrics': exp.get('metrics'),\n        'results': exp.get('results'),\n        'created_at': exp.get('created_at'),\n        'updated_at': exp.get('updated_at'),\n        'completed_at': exp.get('completed_at'),\n        'retry_count': exp.get('retry_count'),\n    }, indent=2))\n    print('-' * 80)\n\nprint()\nprint('=' * 80)\nprint('GROUP: eval_gsm8k ({} experiments)'.format(len(gsm8k)))\nprint('=' * 80)\nfor exp_id, exp in gsm8k.items():\n    print(json.dumps({\n        'exp_id': exp_id,\n        'status': exp.get('status'),\n        'conclusion': exp.get('conclusion'),\n        'hypothesis': exp.get('hypothesis'),\n        'spec': exp.get('spec'),\n        'metrics': exp.get('metrics'),\n        'results': exp.get('results'),\n        'created_at': exp.get('created_at'),\n        'updated_at': exp.get('updated_at'),\n        'completed_at': exp.get('completed_at'),\n        'retry_count': exp.get('retry_count'),\n    }, indent=2))\n    print('-' * 80)\n\" 2>&1\n",
  "description": "Extract all eval_math500 and eval_gsm8k experiments with full details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc9d93bc-3f16-4b64-8718-3b5a04aab144",
  "isSidechain": true,
  "agentId": "aac106f26c591f937",
  "requestId": "req_011CbGKUJJhVPZ9cdjtMBXMK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c53b38c5-3baf-4171-bd09-f66a59d7accf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "d6340ee6-f9f9-4ade-b37f-565650398cf3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012yEXEnJuc5HCJYW9m3dMkX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1362,
      "cache_read_input_tokens": 18364,
      "output_tokens": 755,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1362
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 755,
          "cache_read_input_tokens": 18364,
          "cache_creation_input_tokens": 1362,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1362,
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

_source line 14 · 2026-05-21T20:08:57.114Z_

<details><summary>↩ Tool result · `toolu_01T3woPAEbaEWtnNY9FDbodK`</summary>

```text
================================================================================
GROUP: eval_math500 (6 experiments)
================================================================================
{
  "exp_id": "eval_math500_grpo_cka_only_20_2048",
  "status": "DONE",
  "conclusion": "success",
  "hypothesis": "GRPO CKA-only 20% MATH-500 @2048 accuracy. Core C1 data point: if GRPO CKA-only >> SFT CKA-only (29.0%) on MATH-500, confirms GRPO selectively benefits CKA-only pruning on harder reasoning benchmark.",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_cka_only_20_2048.json\"",
    "server": "westd-29022",
    "gpu": [
      "cuda:2"
    ],
    "pid": "36703",
    "data_path": "MATH-500",
    "data_count": 500,
    "model_name": "grpo_cka_only_20",
    "seed": 42,
    "checkpoint_source": "/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20",
    "eval_data": "MATH-500 (500 problems, max_new_tokens=2048)",
    "checkpoint_path": "/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20",
    "log_path": "/root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_cka_only_20_2048.json"
  },
  "metrics": {
    "accuracy": 0.292,
    "n_correct": 146,
    "n_total": 500,
    "stderr": 0.0203,
    "natural_eos": 390,
    "truncated": 110,
    "avg_response_length": 654.7
  },
  "results": null,
  "created_at": "2026-05-19T02:44:55.483Z",
  "updated_at": "2026-05-19T03:10:44.473Z",
  "completed_at": "2026-05-19T03:10:44.473Z",
  "retry_count": 0
}
--------------------------------------------------------------------------------
{
  "exp_id": "eval_math500_grpo_rasp_20_v3",
  "status": "DONE",
  "conclusion": "failed",
  "hypothesis": "MATH-500 accuracy for grpo_rasp_20 (grpo_stage2_rasp_20_v9). v2 timeout at 193/500 (EXIT_CODE=124, 6h limit). v3 without timeout wrapper. If GRPO RASP outperforms SFT RASP on MATH-500, GRPO adds reasoning. If not, reinforces C1 decoupling.",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_rasp_20_v3.json\"",
    "server": "westd-11672",
    "gpu": [
      "cuda:3"
    ],
    "pid": "31706",
    "log_path": "N/A - server released",
    "submitted_at": "2026-05-17T14:47:00Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "MATH-500",
    "data_count": 500,
    "model_name": "grpo_stage2_rasp_20_v9",
    "seed": 42,
    "checkpoint_source": "grpo_stage2_rasp_20_v9",
    "eval_data": "MATH-500 (500 problems, max_new_tokens=4096, no timeout)",
    "checkpoint_path": "N/A - server released",
    "failure_reason": "Server westd-11672 released before completion",
    "wall_clock_seconds": 127068.7,
    "gpu_hours": 35.3
  },
  "metrics": null,
  "results": null,
  "created_at": "2026-05-17T14:44:46.855Z",
  "updated_at": "2026-05-19T02:04:48.654Z",
  "completed_at": "2026-05-19T02:04:48.654Z",
  "retry_count": 0
}
--------------------------------------------------------------------------------
{
  "exp_id": "eval_math500_grpo_unpruned",
  "status": "DONE",
  "conclusion": "success",
  "hypothesis": "Unpruned Qwen2.5-7B-Instruct after GRPO should achieve high MATH-500 accuracy as dense upper bound for comparing pruned model recovery. Establishes ceiling for C1 reward-accuracy decoupling analysis.",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_baseline/checkpoint-100 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_unpruned.json\"",
    "server": "westd-11672",
    "data_path": "MATH-500",
    "data_count": 500,
    "model_name": "grpo_unpruned_baseline_checkpoint-100",
    "seed": 42,
    "checkpoint_source": "grpo_unpruned_baseline",
    "eval_data": "MATH-500 (500 problems)"
  },
  "metrics": {
    "accuracy": 0.69,
    "n_correct": 345,
    "n_total": 500,
    "ci_95": 0.0207,
    "truncated_pct": 0.172,
    "avg_response_length": 1768
  },
  "results": null,
  "created_at": "2026-05-18T04:57:37.652Z",
  "updated_at": "2026-05-18T05:19:28.892Z",
  "completed_at": "2026-05-18T05:19:28.892Z",
  "retry_count": 0
}
--------------------------------------------------------------------------------
{
  "exp_id": "eval_math500_sft_standard_20_2048_v2",
  "status": "DONE",
  "conclusion": "success",
  "hypothesis": "SFT Standard 20% MATH-500 @2048 with correct GSM8K-trained model (retrained on westd). Fair C1 comparison with GRPO Standard @2048 (26.4%). Previous v1 used wrong model (sft_qwen_math_standard_20).",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_sft_standard_20_2048_v2.json\"",
    "server": "westd-29022",
    "gpu": [
      "cuda:0"
    ],
    "pid": "56146",
    "data_path": "MATH-500",
    "data_count": 500,
    "model_name": "sft_standard_20",
    "seed": 42,
    "checkpoint_source": "/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20",
    "eval_data": "MATH-500 (500 problems, max_new_tokens=2048)",
    "checkpoint_path": "/root/autodl-tmp/recovery_aware_struct_prune/results/math500_sft_standard_20_2048_v2.json",
    "log_path": "/root/autodl-tmp/recovery_aware_struct_prune/results/math500_sft_standard_20_2048_v2.json"
  },
  "metrics": {
    "accuracy": 0.258,
    "n_correct": 129,
    "n_total": 500
  },
  "results": null,
  "created_at": "2026-05-19T02:44:56.424Z",
  "updated_at": "2026-05-19T11:00:21.389Z",
  "completed_at": "2026-05-19T11:00:10.658Z",
  "retry_count": 0
}
--------------------------------------------------------------------------------
{
  "exp_id": "eval_math500_sft_standard_25",
  "status": "DONE",
  "conclusion": "killed",
  "hypothesis": "MATH-500 eval on Standard 25% SFT checkpoint. Extends benchmark coverage beyond GSM8K for 25% sparsity cross-method comparison.",
  "spec": {
    "command": "python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_standard_25.json",
    "server": "westb-23072",
    "gpu": "cuda:0",
    "pid": "59502",
    "data_path": "MATH-500",
    "data_count": 500,
    "model_name": "DeepSeek-R1-Distill-Qwen-7B-pruned-standard-25pct-SFT",
    "seed": 42,
    "checkpoint_source": "sft_standard_25",
    "eval_data": "MATH-500"
  },
  "metrics": null,
  "results": null,
  "created_at": "2026-05-21T02:07:49.557Z",
  "updated_at": "2026-05-21T02:54:41.452Z",
  "completed_at": "2026-05-21T02:54:41.452Z",
  "retry_count": 0
}
--------------------------------------------------------------------------------
{
  "exp_id": "eval_math500_sft_standard_25_v2",
  "status": "DONE",
  "conclusion": "success",
  "hypothesis": "MATH-500 eval on Standard 25% SFT checkpoint (retry with max_new_tokens=2048). v1 killed due to 320s/topic with default max_new_tokens=4096.",
  "spec": {
    "command": "python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_standard_25.json",
    "server": "westb-23072",
    "gpu": "cuda:0",
    "pid": "62714",
    "data_path": "MATH-500",
    "data_count": 500,
    "model_name": "DeepSeek-R1-Distill-Qwen-7B-pruned-standard-25pct-SFT",
    "seed": 42,
    "checkpoint_source": "sft_standard_25",
    "eval_data": "MATH-500",
    "checkpoint_path": "N/A (eval)",
    "log_path": "/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_standard_25.json"
  },
  "metrics": {
    "accuracy": 0.13,
    "n_correct": 65,
    "n_total": 500,
    "truncated": 318,
    "avg_response_length": 1376
  },
  "results": null,
  "created_at": "2026-05-21T02:55:44.254Z",
  "updated_at": "2026-05-21T19:55:31.110Z",
  "completed_at": "2026-05-21T19:55:31.111Z",
  "retry_count": 0
}
--------------------------------------------------------------------------------

================================================================================
GROUP: eval_gsm8k (12 experiments)
================================================================================
{
  "exp_id": "eval_gsm8k_grpo_cka_only_15_seed123",
  "status": "DONE",
  "conclusion": "success",
  "hypothesis": "GSM8K N=1319 eval on CKA-only 15% GRPO seed123 checkpoint. Seed42 achieved 73.09%. Multi-seed validation for statistical significance of the 15% sparsity gap between CKA-only and Standard pruning.",
  "spec": {
    "command": "python eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_15_seed123/checkpoint-100 --max_samples 1319 --seed 123",
    "server": "westd-29022",
    "data_path": "gsm8k",
    "data_count": 1319,
    "model_name": "grpo_cka_only_15_seed123",
    "seed": 123,
    "checkpoint_source": "/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_15_seed123/checkpoint-100",
    "eval_data": "gsm8k"
  },
  "metrics": {
    "gsm8k_accuracy": 0.7309,
    "gsm8k_accuracy_ci": 0.0122,
    "correct": 964,
    "total": 1319,
    "eos_rate": 0.9879,
    "truncated": 16
  },
  "results": null,
  "created_at": "2026-05-21T00:17:24.819Z",
  "updated_at": "2026-05-21T00:17:53.976Z",
  "completed_at": "2026-05-21T00:17:53.976Z",
  "retry_count": 0
}
--------------------------------------------------------------------------------
{
  "exp_id": "eval_gsm8k_grpo_cka_only_20_1p5b",
  "status": "DONE",
  "conclusion": "success",
  "hypothesis": "1.5B CKA-only pruned model post-GRPO should achieve higher GSM8K accuracy than RASP due to preserved representational structure enabling better RL fine-tuning recovery. CKA-only preserves layer similarity without structural regularization overhead, potentially yielding cleaner optimization landscape for GRPO.",
  "spec": {
    "command": "python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_1p5b/checkpoint-100 --max_samples 1319 --seed 42",
    "server": "westb-23072",
    "data_path": "gsm8k",
    "data_count": 1319,
    "model_name": "grpo_cka_only_20_1p5b",
    "seed": 42,
    "checkpoint_source": "/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_1p5b/checkpoint-100",
    "eval_data": "gsm8k"
  },
  "metrics": {
    "accuracy": 0.3548,
    "n_correct": 468,
    "n_total": 1319,
    "stderr": 0.01317
  },
  "results": null,
  "created_at": "2026-05-18T19:49:00.633Z",
  "updated_at": "2026-05-18T19:49:33.438Z",
  "completed_at": "2026-05-18T19:49:33.438Z",
  "retry_count": 0
}
--------------------------------------------------------------------------------
{
  "exp_id": "eval_gsm8k_grpo_cka_only_20_extended_300",
  "status": "DONE",
  "conclusion": "negative",
  "hypothesis": "E2 extended GRPO CKA-only 300\u6b65 GSM8K accuracy (N=1319). Compare with 100\u6b65 (64.37%) to test whether extended GRPO training improves ID accuracy. E2 showed sustained reward oscillation (0.22-0.44) without collapse.",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_extended_300 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_cka_only_20_extended_300.json\"",
    "server": "westd-29022",
    "gpu": [
      "cuda:1"
    ],
    "pid": "56977",
    "data_path": "gsm8k",
    "data_count": 1319,
    "model_name": "grpo_cka_only_20_extended_300",
    "seed": 42,
    "checkpoint_source": "/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_extended_300",
    "eval_data": "GSM8K test (1319 samples)",
    "checkpoint_path": "/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_extended_300",
    "log_path": "/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_cka_only_20_extended_300.json"
  },
  "metrics": {
    "gsm8k_accuracy": 64.37,
    "n_correct": 849,
    "n_total": 1319,
    "note": "identical to 100-step result (64.37%), model saturated at 100 steps"
  },
  "results": null,
  "created_at": "2026-05-19T02:03:54.973Z",
  "updated_at": "2026-05-19T03:58:37.059Z",
  "completed_at": "2026-05-19T03:58:37.059Z",
  "retry_count": 0
}
--------------------------------------------------------------------------------
{
  "exp_id": "eval_gsm8k_grpo_cka_only_20_seed123",
  "status": "DONE",
  "conclusion": "success",
  "hypothesis": "GSM8K evaluation on seed=123 GRPO CKA-only 20% checkpoint. Multi-seed validation: compare with seed=42's 64.37% (849/1319) to confirm CKA-only advantage is robust across seeds. Strengthens C1 claim reliability.",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed123 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_grpo_cka_only_20_seed123.json\"",
    "server": "westb-23072",
    "data_path": "gsm8k",
    "data_count": 1319,
    "model_name": "grpo_cka_only_20_seed123",
    "seed": 123,
    "gpu": [
      "cuda:1"
    ],
    "checkpoint_source": "/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed123",
    "eval_data": "GSM8K test (1319 samples)",
    "checkpoint_path": "/root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_grpo_cka_only_20_seed123.json",
    "log_path": "~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_cka_only_20_seed123.log"
  },
  "metrics": {
    "accuracy": 0.6422,
    "n_correct": 847,
    "n_total": 1319
  },
  "results": null,
  "created_at": "2026-05-19T15:43:25.516Z",
  "updated_at": "2026-05-20T03:04:54.977Z",
  "completed_at": "2026-05-20T03:04:54.977Z",
  "retry_count": 0
}
--------------------------------------------------------------------------------
{
  "exp_id": "eval_gsm8k_grpo_cka_only_20_v2",
  "status": "DONE",
  "conclusion": "success",
  "hypothesis": "CKA-only pruned model after GRPO recovery should achieve meaningful GSM8K accuracy (>30%), confirming CKA-based pruning preserves structures most amenable to RLVR recovery. Core C2 evidence for Tab2. v2: re-run on westb after westd outage.",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_grpo_cka_only_20.json --device_map cuda:0\"",
    "server": "westb-23072",
    "data_path": "openai/gsm8k (local parquet)",
    "data_count": 1319,
    "model_name": "grpo_cka_only_20",
    "seed": 42,
    "checkpoint_source": "grpo_cka_only_20",
    "eval_data": "GSM8K test (1319 samples, greedy decoding, bfloat16)",
    "checkpoint_path": "/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20",
    "log_path": "/root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_grpo_cka_only_20.json"
  },
  "metrics": {
    "accuracy": 0.6437,
    "n_correct": 849,
    "n_total": 1319
  },
  "results": null,
  "created_at": "2026-05-18T05:22:59.435Z",
  "updated_at": "2026-05-19T02:04:42.155Z",
  "completed_at": "2026-05-19T02:04:42.155Z",
  "retry_count": 0
}
--------------------------------------------------------------------------------
{
  "exp_id": "eval_gsm8k_grpo_rasp_20_1p5b",
  "status": "DONE",
  "conclusion": "success",
  "hypothesis": "1.5B RASP post-GRPO GSM8K accuracy (N=1319). Cross-model generalization: 7B RASP GRPO collapsed (reward 0.01), but 1.5B RASP showed reward=0.099 without collapse. If 1.5B RASP GSM8K is lower than CKA-only but not catastrophically low, confirms scale-dependent recovery dynamics. Completes 3-method 1.5B GSM8K comparison.",
  "spec": {
    "command": "CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_20_1p5b/checkpoint-100 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_rasp_20_1p5b.json",
    "server": "westb-23072",
    "data_path": "gsm8k",
    "data_count": 1319,
    "model_name": "grpo_rasp_20_1p5b",
    "seed": 42,
    "checkpoint_source": "/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_20_1p5b/checkpoint-100",
    "eval_data": "gsm8k",
    "checkpoint_path": "/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_20_1p5b/checkpoint-100",
    "log_path": "/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_rasp_20_1p5b.json"
  },
  "metrics": {
    "accuracy": 0.2616,
    "n_correct": 345,
    "n_total": 1319
  },
  "results": null,
  "created_at": "2026-05-18T19:48:55.212Z",
  "updated_at": "2026-05-19T02:04:18.604Z",
  "completed_at": "2026-05-19T02:04:18.604Z",
  "retry_count": 0
}
--------------------------------------------------------------------------------
{
  "exp_id": "eval_gsm8k_grpo_rasp_20_fair",
  "status": "DONE",
  "conclusion": "success",
  "hypothesis": "GRPO RASP 20% fair evaluation on GSM8K (1319 samples). RASP uses recovery-aware scoring combining importance + CKA overlap. Compare with CKA-only (64.37%) and Standard (59.44%) to validate C2 recovery gradient claim.",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_20_fair --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_grpo_rasp_20_fair.json\"",
    "server": "westd-29022",
    "data_path": "gsm8k",
    "data_count": 1319,
    "model_name": "grpo_rasp_20_fair",
    "seed": 42,
    "gpu": [
      "cuda:0"
    ],
    "checkpoint_path": "/root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_grpo_rasp_20_fair.json",
    "log_path": "~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_rasp_20_fair.log"
  },
  "metrics": {
    "accuracy": 0.6088,
    "n_correct": 803,
    "n_total": 1319,
    "stderr": 0.0134,
    "eos_rate": 0.988
  },
  "results": null,
  "created_at": "2026-05-19T15:41:59.916Z",
  "updated_at": "2026-05-19T15:43:04.789Z",
  "completed_at": "2026-05-19T15:43:04.790Z",
  "retry_count": 0
}
--------------------------------------------------------------------------------
{
  "exp_id": "eval_gsm8k_grpo_standard_20_extended_300",
  "status": "DONE",
  "conclusion": "success",
  "hypothesis": "Standard extended 300\u6b65 GSM8K accuracy \u2264 Standard 100\u6b65\u6c34\u5e73 (~52-53%), \u56e0\u4e3a Standard \u5728 GRPO training \u4e2d reward \u59cb\u7ec8 collapse (0.054-0.056), 300\u6b65\u8bad\u7ec3\u4e0d\u5e94\u4ea7\u751f accuracy \u6539\u5584\u3002\u4f5c\u4e3a E2 \u5bf9\u7167\u7ec4: CKA-only 300\u6b65 interim 67.7% vs 100\u6b65 64.37% (+3.3pp) \u6301\u7eed\u63d0\u5347, \u800c Standard \u5e94\u505c\u6ede\u3002",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_extended_300 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_extended_300.json\"",
    "server": "westd-29022",
    "gpu": [
      "cuda:3"
    ],
    "pid": "59413",
    "data_path": "gsm8k",
    "data_count": 1319,
    "model_name": "grpo_standard_20_extended_300",
    "seed": 42,
    "checkpoint_source": "/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_extended_300",
    "eval_data": "GSM8K test (1319 samples, greedy decoding)",
    "checkpoint_path": "/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_extended_300",
    "log_path": "/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_extended_300.json"
  },
  "metrics": {
    "gsm8k_accuracy": 59.29,
    "n_correct": 782,
    "n_total": 1319,
    "stderr": 1.35,
    "eos_rate": 97.95,
    "avg_response_length": 229.6,
    "note": "vs 100-step fair v5: 58.91% \u2192 delta +0.38pp (within stderr). Worker incorrectly compared to old ~52-53% baseline."
  },
  "results": null,
  "created_at": "2026-05-19T02:18:09.990Z",
  "updated_at": "2026-05-19T06:01:44.453Z",
  "completed_at": "2026-05-19T06:00:10.544Z",
  "retry_count": 0
}
--------------------------------------------------------------------------------
{
  "exp_id": "eval_gsm8k_grpo_standard_20_fair_v2",
  "status": "DONE",
  "conclusion": "success",
  "hypothesis": "Verify the phantom 58.91% GSM8K accuracy for Standard GRPO fair v5 100-step model. This number was referenced in analyses but never actually evaluated. Uses correct fair checkpoint grpo_stage2_standard_20_fair.",
  "spec": {
    "command": "CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --max_samples 1319 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_fair_v2.json",
    "server": "westd-29022",
    "data_path": "gsm8k",
    "data_count": 1319,
    "model_name": "grpo_stage2_standard_20_fair",
    "seed": 42,
    "checkpoint_source": "/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair",
    "eval_data": "gsm8k",
    "checkpoint_path": "/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_fair_v2.json",
    "log_path": "/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_fair_v2.json"
  },
  "metrics": {
    "accuracy": 0.5944,
    "n_correct": 784,
    "n_total": 1319
  },
  "results": null,
  "created_at": "2026-05-19T08:57:59.458Z",
  "updated_at": "2026-05-19T12:44:16.392Z",
  "completed_at": "2026-05-19T12:44:16.393Z",
  "retry_count": 0
}
--------------------------------------------------------------------------------
{
  "exp_id": "eval_gsm8k_sft_rasp_20_1p5b",
  "status": "DONE",
  "conclusion": "success",
  "hypothesis": "1.5B SFT RASP 20% GSM8K accuracy (N=1319). Baseline for GRPO delta at 1.5B scale. If SFT \u2248 GRPO (26.16%), confirms 1.5B scale has no GRPO benefit for RASP pruning. C1 framing hard dependency.",
  "spec": {
    "command": "python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_rasp_20_1p5b.json",
    "server": "westb-23072",
    "gpu": [
      "cuda:0"
    ],
    "pid": "845212",
    "data_path": "gsm8k",
    "data_count": 1319,
    "model_name": "sft_rasp_20_1p5b",
    "seed": 42,
    "checkpoint_source": "/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b",
    "eval_data": "GSM8K test (1319 samples)",
    "checkpoint_path": "/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b",
    "log_path": "/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_rasp_20_1p5b.json"
  },
  "metrics": {
    "accuracy": 0.2691,
    "n_correct": 355,
    "n_total": 1319
  },
  "results": null,
  "created_at": "2026-05-19T02:44:33.391Z",
  "updated_at": "2026-05-19T02:45:45.950Z",
  "completed_at": "2026-05-19T02:45:45.950Z",
  "retry_count": 0
}
--------------------------------------------------------------------------------
{
  "exp_id": "eval_gsm8k_sft_shortgpt_20",
  "status": "DONE",
  "conclusion": "success",
  "hypothesis": "ShortGPT SFT checkpoint GSM8K eval. After depth pruning (5/28 layers removed) + SFT warmup, measure GSM8K accuracy. Compare with fine-grained pruning SFT results: CKA-only ~64%, Standard ~59%, RASP ~57%. ShortGPT expected lower due to coarse layer removal.",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_shortgpt_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_sft_shortgpt_20.json\"",
    "server": "westd-29022",
    "data_path": "gsm8k",
    "data_count": 1319,
    "model_name": "sft_shortgpt_20",
    "seed": 42,
    "gpu": [
      "cuda:3"
    ],
    "pid": "117124",
    "checkpoint_path": "/root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_sft_shortgpt_20.json",
    "log_path": "/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_gsm8k_sft_shortgpt_20.log"
  },
  "metrics": {
    "accuracy": 0.4473,
    "n_correct": 590,
    "n_total": 1319
  },
  "results": null,
  "created_at": "2026-05-19T17:17:17.280Z",
  "updated_at": "2026-05-19T17:17:56.066Z",
  "completed_at": "2026-05-19T17:17:56.066Z",
  "retry_count": 0
}
--------------------------------------------------------------------------------
{
  "exp_id": "eval_gsm8k_sft_standard_20_1p5b",
  "status": "DONE",
  "conclusion": "success",
  "hypothesis": "1.5B SFT Standard 20% GSM8K accuracy (N=1319). Baseline for GRPO delta at 1.5B scale. If SFT \u2248 GRPO (22.29%), confirms 1.5B scale has no GRPO benefit for Standard pruning. C1 framing hard dependency.",
  "spec": {
    "command": "python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_standard_20_1p5b.json",
    "server": "westb-23072",
    "gpu": [
      "cuda:1"
    ],
    "pid": "842784",
    "data_path": "gsm8k",
    "data_count": 1319,
    "model_name": "sft_standard_20_1p5b",
    "seed": 42,
    "checkpoint_source": "/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b",
    "eval_data": "GSM8K test (1319 samples)",
    "checkpoint_path": "/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b",
    "log_path": "/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_standard_20_1p5b.json"
  },
  "metrics": {
    "accuracy": 0.229,
    "n_correct": 302,
    "n_total": 1319,
    "stderr": 0.01157,
    "eos_rate": 0.9045,
    "avg_response_length": 516.7
  },
  "results": null,
  "created_at": "2026-05-19T02:44:56.871Z",
  "updated_at": "2026-05-19T03:54:08.362Z",
  "completed_at": "2026-05-19T03:54:08.362Z",
  "retry_count": 0
}
--------------------------------------------------------------------------------
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c53b38c5-3baf-4171-bd09-f66a59d7accf",
  "isSidechain": true,
  "promptId": "1f34c4b2-9824-4de5-b2b7-5e9407290ac0",
  "agentId": "aac106f26c591f937",
  "type": "user",
  "uuid": "933b3b5c-418d-4e93-b811-ce652a943199",
  "sourceToolAssistantUUID": "c53b38c5-3baf-4171-bd09-f66a59d7accf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "d6340ee6-f9f9-4ade-b37f-565650398cf3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-21T20:09:58.943Z_

Here is the complete extracted data from all 18 experiments (6 eval_math500 + 12 eval_gsm8k):

---

## GROUP: eval_math500 (6 experiments)

### 1. eval_math500_grpo_cka_only_20_2048
- **status**: DONE
- **conclusion**: success
- **accuracy**: 0.292
- **n_correct**: 146
- **n_total**: 500
- **truncated**: 110
- **model_name**: grpo_cka_only_20
- **checkpoint_source**: /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20
- **method**: CKA-only, **stage**: GRPO, **sparsity**: 20%
- **full metrics**: `{"accuracy": 0.292, "n_correct": 146, "n_total": 500, "stderr": 0.0203, "natural_eos": 390, "truncated": 110, "avg_response_length": 654.7}`
- **hypothesis**: "GRPO CKA-only 20% MATH-500 @2048 accuracy. Core C1 data point: if GRPO CKA-only >> SFT CKA-only (29.0%) on MATH-500, confirms GRPO selectively benefits CKA-only pruning on harder reasoning benchmark."
- **created_at**: 2026-05-19T02:44:55.483Z, **completed_at**: 2026-05-19T03:10:44.473Z

### 2. eval_math500_grpo_rasp_20_v3
- **status**: DONE
- **conclusion**: failed
- **accuracy**: N/A (metrics null)
- **n_correct**: N/A
- **n_total**: N/A
- **truncated**: N/A
- **model_name**: grpo_stage2_rasp_20_v9
- **checkpoint_source**: grpo_stage2_rasp_20_v9
- **method**: RASP, **stage**: GRPO, **sparsity**: 20%
- **full metrics**: null
- **failure_reason** (in spec): "Server westd-11672 released before completion"
- **wall_clock_seconds**: 127068.7, **gpu_hours**: 35.3
- **hypothesis**: "MATH-500 accuracy for grpo_rasp_20 (grpo_stage2_rasp_20_v9). v2 timeout at 193/500 (EXIT_CODE=124, 6h limit). v3 without timeout wrapper. If GRPO RASP outperforms SFT RASP on MATH-500, GRPO adds reasoning. If not, reinforces C1 decoupling."
- **created_at**: 2026-05-17T14:44:46.855Z, **completed_at**: 2026-05-19T02:04:48.654Z

### 3. eval_math500_grpo_unpruned
- **status**: DONE
- **conclusion**: success
- **accuracy**: 0.69
- **n_correct**: 345
- **n_total**: 500
- **truncated**: N/A (truncated_pct: 0.172)
- **model_name**: grpo_unpruned_baseline_checkpoint-100
- **checkpoint_source**: grpo_unpruned_baseline
- **method**: Unpruned (dense baseline), **stage**: GRPO, **sparsity**: 0%
- **full metrics**: `{"accuracy": 0.69, "n_correct": 345, "n_total": 500, "ci_95": 0.0207, "truncated_pct": 0.172, "avg_response_length": 1768}`
- **hypothesis**: "Unpruned Qwen2.5-7B-Instruct after GRPO should achieve high MATH-500 accuracy as dense upper bound for comparing pruned model recovery. Establishes ceiling for C1 reward-accuracy decoupling analysis."
- **created_at**: 2026-05-18T04:57:37.652Z, **completed_at**: 2026-05-18T05:19:28.892Z

### 4. eval_math500_sft_standard_20_2048_v2
- **status**: DONE
- **conclusion**: success
- **accuracy**: 0.258
- **n_correct**: 129
- **n_total**: 500
- **truncated**: N/A (not in metrics)
- **model_name**: sft_standard_20
- **checkpoint_source**: /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20
- **method**: Standard, **stage**: SFT, **sparsity**: 20%
- **full metrics**: `{"accuracy": 0.258, "n_correct": 129, "n_total": 500}`
- **hypothesis**: "SFT Standard 20% MATH-500 @2048 with correct GSM8K-trained model (retrained on westd). Fair C1 comparison with GRPO Standard @2048 (26.4%). Previous v1 used wrong model (sft_qwen_math_standard_20)."
- **created_at**: 2026-05-19T02:44:56.424Z, **completed_at**: 2026-05-19T11:00:10.658Z

### 5. eval_math500_sft_standard_25
- **status**: DONE
- **conclusion**: killed
- **accuracy**: N/A (metrics null)
- **n_correct**: N/A
- **n_total**: N/A
- **truncated**: N/A
- **model_name**: DeepSeek-R1-Distill-Qwen-7B-pruned-standard-25pct-SFT
- **checkpoint_source**: sft_standard_25
- **method**: Standard, **stage**: SFT, **sparsity**: 25%
- **full metrics**: null
- **hypothesis**: "MATH-500 eval on Standard 25% SFT checkpoint. Extends benchmark coverage beyond GSM8K for 25% sparsity cross-method comparison."
- **created_at**: 2026-05-21T02:07:49.557Z, **completed_at**: 2026-05-21T02:54:41.452Z

### 6. eval_math500_sft_standard_25_v2
- **status**: DONE
- **conclusion**: success
- **accuracy**: 0.13
- **n_correct**: 65
- **n_total**: 500
- **truncated**: 318
- **model_name**: DeepSeek-R1-Distill-Qwen-7B-pruned-standard-25pct-SFT
- **checkpoint_source**: sft_standard_25
- **method**: Standard, **stage**: SFT, **sparsity**: 25%
- **full metrics**: `{"accuracy": 0.13, "n_correct": 65, "n_total": 500, "truncated": 318, "avg_response_length": 1376}`
- **hypothesis**: "MATH-500 eval on Standard 25% SFT checkpoint (retry with max_new_tokens=2048). v1 killed due to 320s/topic with default max_new_tokens=4096."
- **created_at**: 2026-05-21T02:55:44.254Z, **completed_at**: 2026-05-21T19:55:31.111Z

---

## GROUP: eval_gsm8k (12 experiments)

### 1. eval_gsm8k_grpo_cka_only_15_seed123
- **status**: DONE
- **conclusion**: success
- **accuracy**: 0.7309 (gsm8k_accuracy key)
- **n_correct**: 964 (as "correct" key)
- **n_total**: 1319 (as "total" key)
- **truncated**: 16
- **model_name**: grpo_cka_only_15_seed123
- **checkpoint_source**: /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_15_seed123/checkpoint-100
- **method**: CKA-only, **stage**: GRPO, **sparsity**: 15%, **seed**: 123
- **full metrics**: `{"gsm8k_accuracy": 0.7309, "gsm8k_accuracy_ci": 0.0122, "correct": 964, "total": 1319, "eos_rate": 0.9879, "truncated": 16}`
- **hypothesis**: "GSM8K N=1319 eval on CKA-only 15% GRPO seed123 checkpoint. Seed42 achieved 73.09%. Multi-seed validation for statistical significance of the 15% sparsity gap between CKA-only and Standard pruning."

### 2. eval_gsm8k_grpo_cka_only_20_1p5b
- **status**: DONE
- **conclusion**: success
- **accuracy**: 0.3548
- **n_correct**: 468
- **n_total**: 1319
- **truncated**: N/A
- **model_name**: grpo_cka_only_20_1p5b
- **checkpoint_source**: /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_1p5b/checkpoint-100
- **method**: CKA-only, **stage**: GRPO, **sparsity**: 20%, **model scale**: 1.5B
- **full metrics**: `{"accuracy": 0.3548, "n_correct": 468, "n_total": 1319, "stderr": 0.01317}`

### 3. eval_gsm8k_grpo_cka_only_20_extended_300
- **status**: DONE
- **conclusion**: negative
- **accuracy**: 64.37 (note: stored as percentage, not fraction)
- **n_correct**: 849
- **n_total**: 1319
- **truncated**: N/A
- **model_name**: grpo_cka_only_20_extended_300
- **checkpoint_source**: /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_extended_300
- **method**: CKA-only, **stage**: GRPO (extended 300 steps), **sparsity**: 20%
- **full metrics**: `{"gsm8k_accuracy": 64.37, "n_correct": 849, "n_total": 1319, "note": "identical to 100-step result (64.37%), model saturated at 100 steps"}`

### 4. eval_gsm8k_grpo_cka_only_20_seed123
- **status**: DONE
- **conclusion**: success
- **accuracy**: 0.6422
- **n_correct**: 847
- **n_total**: 1319
- **truncated**: N/A
- **model_name**: grpo_cka_only_20_seed123
- **checkpoint_source**: /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed123
- **method**: CKA-only, **stage**: GRPO, **sparsity**: 20%, **seed**: 123
- **full metrics**: `{"accuracy": 0.6422, "n_correct": 847, "n_total": 1319}`

### 5. eval_gsm8k_grpo_cka_only_20_v2
- **status**: DONE
- **conclusion**: success
- **accuracy**: 0.6437
- **n_correct**: 849
- **n_total**: 1319
- **truncated**: N/A
- **model_name**: grpo_cka_only_20
- **checkpoint_source**: grpo_cka_only_20
- **method**: CKA-only, **stage**: GRPO, **sparsity**: 20%, **seed**: 42
- **full metrics**: `{"accuracy": 0.6437, "n_correct": 849, "n_total": 1319}`

### 6. eval_gsm8k_grpo_rasp_20_1p5b
- **status**: DONE
- **conclusion**: success
- **accuracy**: 0.2616
- **n_correct**: 345
- **n_total**: 1319
- **truncated**: N/A
- **model_name**: grpo_rasp_20_1p5b
- **checkpoint_source**: /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_20_1p5b/checkpoint-100
- **method**: RASP, **stage**: GRPO, **sparsity**: 20%, **model scale**: 1.5B
- **full metrics**: `{"accuracy": 0.2616, "n_correct": 345, "n_total": 1319}`

### 7. eval_gsm8k_grpo_rasp_20_fair
- **status**: DONE
- **conclusion**: success
- **accuracy**: 0.6088
- **n_correct**: 803
- **n_total**: 1319
- **truncated**: N/A
- **model_name**: grpo_rasp_20_fair
- **checkpoint_source**: N/A (not in spec)
- **method**: RASP, **stage**: GRPO, **sparsity**: 20%
- **full metrics**: `{"accuracy": 0.6088, "n_correct": 803, "n_total": 1319, "stderr": 0.0134, "eos_rate": 0.988}`

### 8. eval_gsm8k_grpo_standard_20_extended_300
- **status**: DONE
- **conclusion**: success
- **accuracy**: 59.29 (stored as percentage)
- **n_correct**: 782
- **n_total**: 1319
- **truncated**: N/A
- **model_name**: grpo_standard_20_extended_300
- **checkpoint_source**: /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_extended_300
- **method**: Standard, **stage**: GRPO (extended 300 steps), **sparsity**: 20%
- **full metrics**: `{"gsm8k_accuracy": 59.29, "n_correct": 782, "n_total": 1319, "stderr": 1.35, "eos_rate": 97.95, "avg_response_length": 229.6, "note": "vs 100-step fair v5: 58.91% → delta +0.38pp (within stderr). Worker incorrectly compared to old ~52-53% baseline."}`

### 9. eval_gsm8k_grpo_standard_20_fair_v2
- **status**: DONE
- **conclusion**: success
- **accuracy**: 0.5944
- **n_correct**: 784
- **n_total**: 1319
- **truncated**: N/A
- **model_name**: grpo_stage2_standard_20_fair
- **checkpoint_source**: /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair
- **method**: Standard, **stage**: GRPO, **sparsity**: 20%
- **full metrics**: `{"accuracy": 0.5944, "n_correct": 784, "n_total": 1319}`

### 10. eval_gsm8k_sft_rasp_20_1p5b
- **status**: DONE
- **conclusion**: success
- **accuracy**: 0.2691
- **n_correct**: 355
- **n_total**: 1319
- **truncated**: N/A
- **model_name**: sft_rasp_20_1p5b
- **checkpoint_source**: /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b
- **method**: RASP, **stage**: SFT, **sparsity**: 20%, **model scale**: 1.5B
- **full metrics**: `{"accuracy": 0.2691, "n_correct": 355, "n_total": 1319}`

### 11. eval_gsm8k_sft_shortgpt_20
- **status**: DONE
- **conclusion**: success
- **accuracy**: 0.4473
- **n_correct**: 590
- **n_total**: 1319
- **truncated**: N/A
- **model_name**: sft_shortgpt_20
- **checkpoint_source**: N/A (not in spec)
- **method**: ShortGPT (depth pruning), **stage**: SFT, **sparsity**: 20%
- **full metrics**: `{"accuracy": 0.4473, "n_correct": 590, "n_total": 1319}`

### 12. eval_gsm8k_sft_standard_20_1p5b
- **status**: DONE
- **conclusion**: success
- **accuracy**: 0.229
- **n_correct**: 302
- **n_total**: 1319
- **truncated**: N/A
- **model_name**: sft_standard_20_1p5b
- **checkpoint_source**: /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b
- **method**: Standard, **stage**: SFT, **sparsity**: 20%, **model scale**: 1.5B
- **full metrics**: `{"accuracy": 0.229, "n_correct": 302, "n_total": 1319, "stderr": 0.01157, "eos_rate": 0.9045, "avg_response_length": 516.7}`

---

**Summary counts**: 6 eval_math500 experiments (4 with successful metrics, 1 killed, 1 failed due to server release), 12 eval_gsm8k experiments (all with metrics). Note inconsistency in accuracy format: some stored as fractions (0.6437), some as percentages (64.37, 59.29). The `n_correct`/`n_total` fields are consistent and can be used to compute uniform accuracy values.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "933b3b5c-418d-4e93-b811-ce652a943199",
  "isSidechain": true,
  "agentId": "aac106f26c591f937",
  "requestId": "req_011CbGKVNWyrenWQfq6D231X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7efb25a1-0084-4b70-848d-fc7519776bd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "sessionId": "d6340ee6-f9f9-4ade-b37f-565650398cf3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KZPmakaYLwx2wvpndj1JMu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11546,
      "cache_read_input_tokens": 19726,
      "output_tokens": 4556,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11546
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4556,
          "cache_read_input_tokens": 19726,
          "cache_creation_input_tokens": 11546,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11546,
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
