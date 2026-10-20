# Research conversation: I need you to extract specific experiment entries from a large JSON registry file. The file is at: /home/ubuntu/.claude-

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a55231259953ee2cc.jsonl`
- **Structured JSON:** [`455840da6d682639606b.json`](../../sessions/45/455840da6d682639606b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

12 recorded events

### User

_source line 1 · 2026-05-22T08:26:30.460Z_

I need you to extract specific experiment entries from a large JSON registry file. The file is at:
/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/bc94af32-4f18-47ef-82eb-b2e18fce9e57/tool-results/mcp-agent-ml-research-read_registry-1779438364142.txt

The file has schema: {result: string} where result is a JSON string.

I need you to extract the full content (all fields) for these experiment IDs:
- eval_llama_ar_n20
- eval_llama_lora_only_s42
- llama_eval_s42
- llama_ar_matched_eval
- eval_v7_tg_s123
- eval_v8b_ss_s123
- phase2_4way_eval
- phase2_4way_eval_heldout
- phase2_tg_s42_v7
- phase2_tg_s42_v9_pcgrad
- phase2_lora_only_s42
- phase2_ug_s42
- attention_steering_gen_n50
- attention_steering_v7_tg_gen
- phase1_gar_diag
- llama_phase1_gar_diag

For each entry, output: exp_id, metrics (full), notes (full), and any field that mentions "mid" or "turn". 

Use jq or python to parse the file. Output the results verbatim - do not summarize or truncate.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "d6038c84-bd9d-43b7-9ec0-15fb7e7a361e",
  "agentId": "a55231259953ee2cc",
  "type": "user",
  "uuid": "7e34ccf5-2178-46a3-862a-924303c91877",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "bc94af32-4f18-47ef-82eb-b2e18fce9e57",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-22T08:26:30.463Z_

```json
{
  "parentUuid": "7e34ccf5-2178-46a3-862a-924303c91877",
  "isSidechain": true,
  "agentId": "a55231259953ee2cc",
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
      "TodoWrite",
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
  "uuid": "b79fbd3d-9142-46a5-8b27-b1ea6ea9cc72",
  "timestamp": "2026-05-22T08:26:30.463Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "bc94af32-4f18-47ef-82eb-b2e18fce9e57",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-22T08:26:32.997Z_



Let me first read the file to understand its structure, then extract the requested entries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b79fbd3d-9142-46a5-8b27-b1ea6ea9cc72",
  "isSidechain": true,
  "agentId": "a55231259953ee2cc",
  "requestId": "req_011CbHHjUZXtvkT2ntpBoSxa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5898e7e2-fe4d-49ec-b630-7129d1d8da01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "bc94af32-4f18-47ef-82eb-b2e18fce9e57",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012XJb6eSfk8gZd4tVfhbEPe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16107,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16107,
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

_source line 4 · 2026-05-22T08:26:34.000Z_

<details open><summary>🔧 Tool call — Bash · `toolu_013jVzonWTdm86y9CSUM8fht`</summary>

```json
{
  "command": "head -c 2000 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/bc94af32-4f18-47ef-82eb-b2e18fce9e57/tool-results/mcp-agent-ml-research-read_registry-1779438364142.txt",
  "description": "Check file structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5898e7e2-fe4d-49ec-b630-7129d1d8da01",
  "isSidechain": true,
  "agentId": "a55231259953ee2cc",
  "requestId": "req_011CbHHjUZXtvkT2ntpBoSxa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3eac6266-bc31-4e6f-aff2-76a62616c5ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "bc94af32-4f18-47ef-82eb-b2e18fce9e57",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012XJb6eSfk8gZd4tVfhbEPe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16107,
      "cache_read_input_tokens": 0,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16107
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 187,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16107,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16107,
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

_source line 5 · 2026-05-22T08:26:34.168Z_

<details><summary>↩ Tool result · `toolu_013jVzonWTdm86y9CSUM8fht`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval_llama_ar_n20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T07:52:04.543Z\", \"updated_at\": \"2026-05-22T08:25:04.827Z\", \"hypothesis\": \"N=20 AR eval stabilizes Llama 3-way (Base/TG/LoRA-only) autoregressive GAR estimates. N=5 suffered from outlier influence (3/5 conv had GAR>0.4 outlier turns); N=20 provides robust mean±std.\", \"parent\": \"eval_llama_lora_only_s42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && bash scripts/eval_llama_ar_n20.sh\\\"\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": \"312592\", \"log_path\": \"~/runs/turn_residual_gating/eval_llama_ar_n20.log\", \"submitted_at\": \"2026-05-22T07:52:13.830Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"ultrachat_200k + model-gen AR\", \"data_count\": 20, \"model_name\": \"Llama-3.1-8B-Instruct (Base/TG/LoRA-only)\", \"seed\": 42, \"checkpoint_source\": \"llama_tg_s42 + llama_lora_only_s42\", \"eval_data\": \"AR-generated 20 conversations x 4 turns\", \"wall_clock_seconds\": 1435.6, \"gpu_hours\": 0.4}, \"reproduce\": {\"finished_at\": \"2026-05-22T08:09:48.181Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T08:09:50.100538+00:00\"}]}, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/runs/turn_residual_gating/eval_llama_ar_n20.log\", \"metrics\": {\"base\": {\"gar_ours_mid\": 0.0088, \"gar_dongre_mid\": 0.0049, \"ngar_ours_mid\": 0.1019, \"ngar_dongre_mid\": 0.1171, \"ppl\": 1.293, \"ntp_loss\": 0.2552}, \"tg\": {\"gar_ours_mid\": 0.0434, \"gar_dongre_mid\": 0.0183, \"ngar_ours_mid\": 0.5357, \"ngar_dongre_mid\": 0.4436, \"ppl\": 1.437, \"ntp_loss\": 0.3612}, \"lora_only\": {\"gar_ours_mid\": 0.0284, \"gar_dongre_mid\": 0.0205, \"ngar_ours_mid\": 0.3488, \"ngar_dongr
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3eac6266-bc31-4e6f-aff2-76a62616c5ad",
  "isSidechain": true,
  "promptId": "d6038c84-bd9d-43b7-9ec0-15fb7e7a361e",
  "agentId": "a55231259953ee2cc",
  "type": "user",
  "uuid": "7ce08a47-c05d-499e-9622-fba2caf4e5fb",
  "sourceToolAssistantUUID": "3eac6266-bc31-4e6f-aff2-76a62616c5ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "bc94af32-4f18-47ef-82eb-b2e18fce9e57",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-22T08:26:38.609Z_

The file is large and contains nested JSON. Let me use Python to extract all the requested entries properly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ce08a47-c05d-499e-9622-fba2caf4e5fb",
  "isSidechain": true,
  "agentId": "a55231259953ee2cc",
  "requestId": "req_011CbHHjkSWfCFfzAvnZQdk3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f2417ea-e30a-41c3-a585-12f55ae42452",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "bc94af32-4f18-47ef-82eb-b2e18fce9e57",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014GuXiPCZoXtUHzrmYQMu4o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1950,
      "cache_read_input_tokens": 16107,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1950,
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

_source line 7 · 2026-05-22T08:26:49.911Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01VpPCRHpR1x1QuBLt6wjA44`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open(\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/bc94af32-4f18-47ef-82eb-b2e18fce9e57/tool-results/mcp-agent-ml-research-read_registry-1779438364142.txt\", \"r\") as f:\n    raw = json.load(f)\n\ndata = json.loads(raw[\"result\"])\nexperiments = data[\"data\"][\"experiments\"]\n\ntarget_ids = [\n    \"eval_llama_ar_n20\",\n    \"eval_llama_lora_only_s42\",\n    \"llama_eval_s42\",\n    \"llama_ar_matched_eval\",\n    \"eval_v7_tg_s123\",\n    \"eval_v8b_ss_s123\",\n    \"phase2_4way_eval\",\n    \"phase2_4way_eval_heldout\",\n    \"phase2_tg_s42_v7\",\n    \"phase2_tg_s42_v9_pcgrad\",\n    \"phase2_lora_only_s42\",\n    \"phase2_ug_s42\",\n    \"attention_steering_gen_n50\",\n    \"attention_steering_v7_tg_gen\",\n    \"phase1_gar_diag\",\n    \"llama_phase1_gar_diag\",\n]\n\nfor eid in target_ids:\n    if eid in experiments:\n        print(f\"{'='*80}\")\n        print(f\"EXP_ID: {eid}\")\n        print(f\"{'='*80}\")\n        print(json.dumps(experiments[eid], indent=2))\n        print()\n    else:\n        print(f\"{'='*80}\")\n        print(f\"EXP_ID: {eid} — NOT FOUND\")\n        print(f\"{'='*80}\")\n        print()\n\nPYEOF",
  "description": "Extract all requested experiment entries from registry JSON",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f2417ea-e30a-41c3-a585-12f55ae42452",
  "isSidechain": true,
  "agentId": "a55231259953ee2cc",
  "requestId": "req_011CbHHjkSWfCFfzAvnZQdk3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "355a12b7-9ba7-4722-856f-cff508db8243",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "bc94af32-4f18-47ef-82eb-b2e18fce9e57",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014GuXiPCZoXtUHzrmYQMu4o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1950,
      "cache_read_input_tokens": 16107,
      "output_tokens": 617,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1950
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 617,
          "cache_read_input_tokens": 16107,
          "cache_creation_input_tokens": 1950,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1950,
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

_source line 8 · 2026-05-22T08:26:50.016Z_

<details><summary>↩ Tool result · `toolu_01VpPCRHpR1x1QuBLt6wjA44`</summary>

```text
&lt;persisted-output>
Output too large (43.2KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/bc94af32-4f18-47ef-82eb-b2e18fce9e57/tool-results/bjjin8psg.txt

Preview (first 2KB):
================================================================================
EXP_ID: eval_llama_ar_n20
================================================================================
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-22T07:52:04.543Z",
  "updated_at": "2026-05-22T08:25:04.827Z",
  "hypothesis": "N=20 AR eval stabilizes Llama 3-way (Base/TG/LoRA-only) autoregressive GAR estimates. N=5 suffered from outlier influence (3/5 conv had GAR>0.4 outlier turns); N=20 provides robust mean\u00b1std.",
  "parent": "eval_llama_lora_only_s42",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && bash scripts/eval_llama_ar_n20.sh\"",
    "server": "westd-20861",
    "gpu": [
      "cuda:0"
    ],
    "pid": "312592",
    "log_path": "~/runs/turn_residual_gating/eval_llama_ar_n20.log",
    "submitted_at": "2026-05-22T07:52:13.830Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "ultrachat_200k + model-gen AR",
    "data_count": 20,
    "model_name": "Llama-3.1-8B-Instruct (Base/TG/LoRA-only)",
    "seed": 42,
    "checkpoint_source": "llama_tg_s42 + llama_lora_only_s42",
    "eval_data": "AR-generated 20 conversations x 4 turns",
    "wall_clock_seconds": 1435.6,
    "gpu_hours": 0.4
  },
  "reproduce": {
    "finished_at": "2026-05-22T08:09:48.181Z"
  },
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-22T08:09:50.100538+00:00"
      }
    ]
  },
  "checkpoint_path": "N/A",
  "log_path": "/root/runs/turn_residual_gating/eval_llama_ar_n20.log",
  "metrics": {
    "base": {
      "gar_ours_mid": 0.0088,
      "gar_dongre_mid": 0.0049,
      "ngar_ours_mid": 0.1019,
      "ngar_dongre_mid": 0.1171,
      "ppl": 1.293,
      "ntp_loss": 0.2552
    },
    "tg": {
      "gar_ours_mid": 0.0434,
      "gar_dongre_mid": 0.0183,
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "355a12b7-9ba7-4722-856f-cff508db8243",
  "isSidechain": true,
  "promptId": "d6038c84-bd9d-43b7-9ec0-15fb7e7a361e",
  "agentId": "a55231259953ee2cc",
  "type": "user",
  "uuid": "67696b58-30a2-437b-b80a-2a5bcd013533",
  "sourceToolAssistantUUID": "355a12b7-9ba7-4722-856f-cff508db8243",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "bc94af32-4f18-47ef-82eb-b2e18fce9e57",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-22T08:26:53.738Z_

The output was too large for the preview. Let me read the full output file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67696b58-30a2-437b-b80a-2a5bcd013533",
  "isSidechain": true,
  "agentId": "a55231259953ee2cc",
  "requestId": "req_011CbHHkvDAHHFkHRBDReEHx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9a79457-02ec-4c6d-9751-4c1119454a3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "bc94af32-4f18-47ef-82eb-b2e18fce9e57",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D2Vi4B5oCHBeqN9PFwWKRk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1571,
      "cache_read_input_tokens": 18057,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1571,
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

_source line 10 · 2026-05-22T08:26:54.454Z_

<details open><summary>🔧 Tool call — Read · `toolu_01J8X2o6e5jQsjtEmgNwBqj3`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/bc94af32-4f18-47ef-82eb-b2e18fce9e57/tool-results/bjjin8psg.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9a79457-02ec-4c6d-9751-4c1119454a3a",
  "isSidechain": true,
  "agentId": "a55231259953ee2cc",
  "requestId": "req_011CbHHkvDAHHFkHRBDReEHx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a5808c0-25fd-4384-99be-e39641fa38b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "bc94af32-4f18-47ef-82eb-b2e18fce9e57",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D2Vi4B5oCHBeqN9PFwWKRk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1571,
      "cache_read_input_tokens": 18057,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1571
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 149,
          "cache_read_input_tokens": 18057,
          "cache_creation_input_tokens": 1571,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1571,
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

_source line 11 · 2026-05-22T08:26:54.757Z_

<details><summary>↩ Tool result · `toolu_01J8X2o6e5jQsjtEmgNwBqj3`</summary>

```text
1	================================================================================
2	EXP_ID: eval_llama_ar_n20
3	================================================================================
4	{
5	  "status": "DONE",
6	  "retry_count": 0,
7	  "created_at": "2026-05-22T07:52:04.543Z",
8	  "updated_at": "2026-05-22T08:25:04.827Z",
9	  "hypothesis": "N=20 AR eval stabilizes Llama 3-way (Base/TG/LoRA-only) autoregressive GAR estimates. N=5 suffered from outlier influence (3/5 conv had GAR>0.4 outlier turns); N=20 provides robust mean\u00b1std.",
10	  "parent": "eval_llama_lora_only_s42",
11	  "spec": {
12	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && bash scripts/eval_llama_ar_n20.sh\"",
13	    "server": "westd-20861",
14	    "gpu": [
15	      "cuda:0"
16	    ],
17	    "pid": "312592",
18	    "log_path": "~/runs/turn_residual_gating/eval_llama_ar_n20.log",
19	    "submitted_at": "2026-05-22T07:52:13.830Z",
20	    "submitted_via": "submit_training_job",
21	    "backend": "tmux",
22	    "account": "root",
23	    "data_path": "ultrachat_200k + model-gen AR",
24	    "data_count": 20,
25	    "model_name": "Llama-3.1-8B-Instruct (Base/TG/LoRA-only)",
26	    "seed": 42,
27	    "checkpoint_source": "llama_tg_s42 + llama_lora_only_s42",
28	    "eval_data": "AR-generated 20 conversations x 4 turns",
29	    "wall_clock_seconds": 1435.6,
30	    "gpu_hours": 0.4
31	  },
32	  "reproduce": {
33	    "finished_at": "2026-05-22T08:09:48.181Z"
34	  },
35	  "extra": {
36	    "hook_events": [
37	      {
38	        "event": "on_complete",
39	        "action": "agent",
40	        "ts": "2026-05-22T08:09:50.100538+00:00"
41	      }
42	    ]
43	  },
44	  "checkpoint_path": "N/A",
45	  "log_path": "/root/runs/turn_residual_gating/eval_llama_ar_n20.log",
46	  "metrics": {
47	    "base": {
48	      "gar_ours_mid": 0.0088,
49	      "gar_dongre_mid": 0.0049,
50	      "ngar_ours_mid": 0.1019,
51	      "ngar_dongre_mid": 0.1171,
52	      "ppl": 1.293,
53	      "ntp_loss": 0.2552
54	    },
55	    "tg": {
56	      "gar_ours_mid": 0.0434,
57	      "gar_dongre_mid": 0.0183,
58	      "ngar_ours_mid": 0.5357,
59	      "ngar_dongre_mid": 0.4436,
60	      "ppl": 1.437,
61	      "ntp_loss": 0.3612
62	    },
63	    "lora_only": {
64	      "gar_ours_mid": 0.0284,
65	      "gar_dongre_mid": 0.0205,
66	      "ngar_ours_mid": 0.3488,
67	      "ngar_dongre_mid": 0.4997,
68	      "ppl": 1.419,
69	      "ntp_loss": 0.3483
70	    },
71	    "n_conversations": 20,
72	    "n_turns": 4,
73	    "ranking_gar_ours": "TG(0.0434) > LO(0.0284) > Base(0.0088)",
74	    "ranking_gar_dongre": "LO(0.0205) > TG(0.0183) > Base(0.0049)"
75	  },
76	  "notes": "N=20 AR eval stabilizes estimates. Mean difference (TG 0.0434 > LO 0.0284) is driven by outlier spikes (5-8% of turns with GAR>0.4); **median shows TG \u2248 LO (0.018 vs 0.018), consistent with zero-increment finding from Qwen**. Gate provides no incremental GAR benefit over LoRA-only on Llama, same as Qwen. PPL ordering preserved: Base(1.29) < LO(1.42) < TG(1.44). T=4, outlier turns still present in N=20 (TG conv9/15/18 have GAR>0.4 single turns, LO conv10/12/18/20 similar) but diluted by 4x larger sample vs N=5.",
77	  "conclusion": "success",
78	  "completed_at": "2026-05-22T08:16:09.384Z"
79	}
80	
81	================================================================================
82	EXP_ID: eval_llama_lora_only_s42
83	================================================================================
84	{
85	  "status": "DONE",
86	  "retry_count": 0,
87	  "created_at": "2026-05-22T07:40:25.352Z",
88	  "updated_at": "2026-05-22T07:51:32.758Z",
89	  "hypothesis": "LoRA-only ablation (no gate) on Llama-3.1-8B: if TG's GAR improvement comes from the gate, LoRA-only should show minimal GAR recovery vs base.",
90	  "parent": "llama_lora_only_s42",
91	  "spec": {
92	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && bash scripts/eval_llama_lora_only_s42.sh\"",
93	    "server": "westd-20861",
94	    "gpu": [
95	      "cuda:0"
96	    ],
97	    "pid": "309670",
98	    "log_path": "/root/runs/turn_residual_gating/eval_llama_lora_only_s42.log",
99	    "submitted_at": "2026-05-22T07:40:34.437Z",
100	    "submitted_via": "submit_training_job",
101	    "backend": "tmux",
102	    "account": "root",
103	    "data_path": "ultrachat_200k + model-gen",
104	    "data_count": 55,
105	    "model_name": "Llama-3.1-8B-Instruct + LoRA-only checkpoint",
106	    "seed": 42,
107	    "checkpoint_source": "llama_lora_only_s42",
108	    "eval_data": "IID heldout 50 + model-gen 5",
109	    "checkpoint_path": "runs/phase2_llama_lora_only_s42/epoch_2",
110	    "wall_clock_seconds": 650.8,
111	    "gpu_hours": 0.18
112	  },
113	  "reproduce": {
114	    "finished_at": "2026-05-22T07:45:28.637Z"
115	  },
116	  "extra": {
117	    "hook_events": [
118	      {
119	        "event": "on_complete",
120	        "action": "agent",
121	        "ts": "2026-05-22T07:45:30.556207+00:00"
122	      }
123	    ]
124	  },
125	  "metrics": {
126	    "tf": {
127	      "gar_ours": 0.4807,
128	      "gar_dongre": 0.0188,
129	      "ngar_ours": 11.8031,
130	      "ngar_dongre": 0.8261,
131	      "ppl": 2.6,
132	      "ntp_loss": 0.9366,
133	      "n_conversations": 50,
134	      "n_turns": 4
135	    },
136	    "ar": {
137	      "gar_ours": 0.0617,
138	      "gar_dongre": 0.0226,
139	      "ngar_ours": 0.6065,
140	      "ngar_dongre": 0.2537,
141	      "ppl": 1.32,
142	      "ntp_loss": 0.2787,
143	      "n_conversations": 5,
144	      "n_turns": 10
145	    },
146	    "gap_ratio_gar_ours": 7.79
147	  },
148	  "conclusion": "success",
149	  "completed_at": "2026-05-22T07:51:25.244Z"
150	}
151	
152	================================================================================
153	EXP_ID: llama_eval_s42
154	================================================================================
155	{
156	  "status": "DONE",
157	  "retry_count": 0,
158	  "created_at": "2026-05-21T03:29:51.255Z",
159	  "updated_at": "2026-05-21T03:46:58.167Z",
160	  "hypothesis": "Llama-3.1-8B TG eval: \u5982\u679c Llama TG \u6a21\u578b\u5728 TF \u6a21\u5f0f\u4e0b GAR-ours \u663e\u8457\u9ad8\u4e8e AR \u6a21\u5f0f\uff08\u5982 Qwen v7 \u7684 20-33x gap\uff09\uff0c\u5219\u786e\u8ba4 training-inference GAR gap \u8de8\u6a21\u578b\u6cdb\u5316\uff08C5\uff09\u3002\u540c\u65f6\u6d4b\u91cf base model \u4f5c\u4e3a control\u3002",
161	  "parent": "llama_tg_s42",
162	  "spec": {
163	    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && bash scripts/eval_llama_tg_s42.sh 2>&1 | tee runs/eval_llama_tg_s42.log",
164	    "server": "westd-20861",
165	    "data_path": "data/ultrachat_eval_sample.json",
166	    "data_count": 50,
167	    "model_name": "Llama-3.1-8B-Instruct",
168	    "seed": 42,
169	    "checkpoint_source": "runs/phase2_llama_tg_s42/epoch_2",
170	    "eval_data": "ultrachat_eval_sample"
171	  },
172	  "checkpoint_path": "runs/phase2_llama_tg_s42/epoch_2",
173	  "log_path": "runs/eval_llama_tg_s42.log",
174	  "metrics": {
175	    "tf_base": {
176	      "gar_ours": 0.0166,
177	      "ngar_ours": 0.3882,
178	      "gar_dongre": 0.0038,
179	      "ngar_dongre": 0.163,
180	      "ppl": 3.45,
181	      "N": 50,
182	      "T": 4
183	    },
184	    "tf_tg": {
185	      "gar_ours": 0.4836,
186	      "ngar_ours": 11.8818,
187	      "gar_dongre": 0.018,
188	      "ngar_dongre": 0.7922,
189	      "ppl": 2.57,
190	      "N": 50,
191	      "T": 4
192	    },
193	    "ar_base": {
194	      "gar_ours": 0.0086,
195	      "ngar_ours": 0.0798,
196	      "gar_dongre": 0.0118,
197	      "ngar_dongre": 0.1265,
198	      "ppl": 1.24,
199	      "N": 5,
200	      "T": 10
201	    },
202	    "ar_tg": {
203	      "gar_ours": 0.0304,
204	      "ngar_ours": 0.2632,
205	      "gar_dongre": 0.0217,
206	      "ngar_dongre": 0.2459,
207	      "ppl": 1.32,
208	      "N": 5,
209	      "T": 10
210	    },
211	    "gap_ratio_tg_ours": 15.9,
212	    "gap_ratio_base_ours": 1.93,
213	    "gap_ratio_tg_dongre": 0.83,
214	    "vs_qwen_v7_gap_ratio": 32.1,
215	    "baseline_mid_gar": 0.0122
216	  },
217	  "conclusion": "success",
218	  "notes": "C5 \u8de8\u6a21\u578b\u6cdb\u5316\u786e\u8ba4\u3002Llama TG GAR-ours gap 16x (TF 0.484 vs AR 0.030)\uff0c\u4f4e\u4e8e Qwen v7 \u7684 32x \u4f46\u4ecd\u975e\u5e38\u663e\u8457\u3002Base model gap \u4ec5 1.9x\uff08control \u901a\u8fc7\uff09\u3002\u6ce8\u610f TF/AR eval \u8bbe\u5b9a\u4e0d\u540c (N=50/T=4 vs N=5/T=10)\uff0c\u53ef\u80fd\u5f71\u54cd\u7edd\u5bf9\u503c\u5bf9\u6bd4\u3002GAR-dongre \u65e0\u660e\u663e gap (ratio 0.83x, AR \u2265 TF)\uff0c\u4ec5 GAR-ours \u5c55\u73b0 exposure bias \u6548\u5e94\u3002Gate dynamic range: L24/L28/L30 diff \u6700\u5927 (0.23-0.38)\uff0c\u4e0e Qwen \u7c7b\u4f3c\u96c6\u4e2d\u5728\u4e2d\u9ad8\u5c42\u3002",
219	  "completed_at": "2026-05-21T03:46:58.167Z"
220	}
221	
222	================================================================================
223	EXP_ID: llama_ar_matched_eval
224	================================================================================
225	{
226	  "status": "DONE",
227	  "retry_count": 0,
228	  "created_at": "2026-05-21T03:59:40.918Z",
229	  "updated_at": "2026-05-21T04:36:23.237Z",
230	  "hypothesis": "\u7528 matched \u8bbe\u7f6e (N=50/T=4) \u91cd\u8dd1 Llama AR eval\uff0c\u6d88\u9664 TF/AR \u8bbe\u7f6e\u5dee\u5f02\u3002\u4e0e TF \u7ed3\u679c\u5bf9\u6bd4\u5f97\u5230\u53ef\u76f4\u63a5\u5199\u5165\u8bba\u6587\u7684 gap ratio\uff0c\u9a8c\u8bc1 TG \u5728 AR \u6a21\u5f0f\u4e0b\u4ecd\u80fd\u63d0\u5347 GAR\u3002",
231	  "parent": "llama_eval_s42",
232	  "spec": {
233	    "command": "bash scripts/eval_llama_ar_matched.sh",
234	    "server": "westd-20861",
235	    "data_path": "data/ultrachat_eval_sample.json",
236	    "data_count": 50,
237	    "model_name": "Meta-Llama-3.1-8B-Instruct + TG LoRA",
238	    "seed": 42,
239	    "checkpoint_source": "phase2_llama_tg_s42",
240	    "eval_data": "50 UltraChat convs, T=4, AR generation, 4 conditions (base/TG x ours/Dongre)",
241	    "checkpoint_path": "N/A (eval)",
242	    "log_path": "runs/eval_llama_ar_matched.log"
243	  },
244	  "log_path": "/root/turn_residual_gating/runs/eval_llama_ar_matched.log",
245	  "conclusion": "success",
246	  "metrics": {
247	    "ar_base_ours": {
248	      "mid_gar": 0.0082,
249	      "ngar": 0.1,
250	      "ppl": 1.267
251	    },
252	    "ar_tg_ours": {
253	      "mid_gar": 0.0388,
254	      "ngar": 0.493,
255	      "ppl": 1.413
256	    },
257	    "ar_base_dongre": {
258	      "mid_gar": 0.0051,
259	      "ngar": 0.12,
260	      "ppl": 1.267
261	    },
262	    "ar_tg_dongre": {
263	      "mid_gar": 0.018,
264	      "ngar": 0.431,
265	      "ppl": 1.413
266	    },
267	    "tf_reference": {
268	      "tf_tg_ours_ngar": 11.88,
269	      "tf_base_ours_ngar": 0.388,
270	      "tf_tg_ours_raw": 0.4836,
271	      "tf_tg_dongre_raw": 0.018
272	    },
273	    "matched_gap_analysis": {
274	      "gar_ours_raw_gap": "12.5x (TF 0.484 / AR 0.039)",
275	      "gar_ours_ngar_gap": "24.1x (TF 11.88 / AR 0.493)",
276	      "gar_dongre_raw_gap": "1.002x (TF 0.018 / AR 0.018) \u2014 zero gap",
277	      "tg_over_base_ar_ours": "4.71x",
278	      "tg_over_base_ar_dongre": "3.54x",
279	      "conclusion": "GAR-ours TF-AR gap 12.5x (raw) / 24x (nGAR) is genuine exposure bias. GAR-Dongre zero gap (1.002x) confirms mechanism specificity: exposure bias selectively destroys learned goal-attention routing while leaving content-overlap-based attention unaffected."
280	    }
281	  },
282	  "completed_at": "2026-05-21T04:28:38.504Z",
283	  "notes": "CORRECTION (2026-05-21 04:36): Agent \u4e4b\u524d\u9519\u8bef\u5730\u5c06 AR TG nGAR (0.493) \u4e0e TF TG raw GAR (0.484) \u5bf9\u6bd4\uff0c\u8bef\u5224\u4e3a 'nGAR aligns, gap is normalization artifact'\u3002Reviewer \u6838\u5b9e\uff1aTF TG ours nGAR = 11.88\uff08\u975e 0.48\uff09\u3002nGAR gap = 11.88 / 0.493 = 24.1\u00d7\uff0c\u6bd4 raw gap (12.5\u00d7) \u8fd8\u5927\u3002'Normalization artifact' \u5206\u6790\u5b8c\u5168\u9519\u8bef\u2014\u2014GAR-ours \u7684 gap \u662f\u771f\u5b9e\u7684 exposure bias\u3002\u8bba\u6587\u7edd\u5bf9\u4e0d\u80fd\u4f7f\u7528 normalization artifact \u53d9\u4e8b\u3002"
284	}
285	
286	================================================================================
287	EXP_ID: eval_v7_tg_s123
288	================================================================================
289	{
290	  "status": "DONE",
291	  "retry_count": 0,
292	  "created_at": "2026-05-21T22:53:18.163Z",
293	  "updated_at": "2026-05-22T00:30:49.653Z",
294	  "spec": {
295	    "command": "bash scripts/eval_v7_tg_s123.sh",
296	    "server": "westd-20861",
297	    "gpu": [
298	      "cuda:0"
299	    ],
300	    "pid": "264869",
301	    "log_path": "/root/turn_residual_gating/logs/v7_tg_s123.log",
302	    "submitted_at": "2026-05-21T22:53:18.065Z",
303	    "submitted_via": "submit_training_job",
304	    "backend": "tmux",
305	    "account": "root",
306	    "data_path": "data/ultrachat_8k",
307	    "data_count": 8000,
308	    "model_name": "Qwen2.5-7B-Instruct",
309	    "seed": 123,
310	    "checkpoint_source": "v7_tg_s123",
311	    "eval_data": "data/ultrachat_8k",
312	    "checkpoint_path": "/root/turn_residual_gating/runs/phase2_tg_s123_v7/epoch_2",
313	    "wall_clock_seconds": 5844.5,
314	    "gpu_hours": 1.62
315	  },
316	  "hypothesis": "v7 TG s123 eval: \u9a8c\u8bc1 s123 seed \u7684 TF-AR GAR gap \u4e0e s42 \u4e00\u81f4\uff08~32\u00d7\uff09\uff0c\u786e\u8ba4 multi-seed robustness",
317	  "parent": "v7_tg_s123",
318	  "conclusion": "success",
319	  "completed_at": "2026-05-22T00:30:42.606Z",
320	  "metrics": {
321	    "iid_tf": {
322	      "gar_ours_mid": 0.5052,
323	      "gar_dongre_mid": 0.0119,
324	      "ppl": 2.7802,
325	      "ntp": 0.9752
326	    },
327	    "modelgen_ar": {
328	      "gar_ours_mid": 0.0165,
329	      "gar_dongre_mid": 0.0177,
330	      "ppl": 1.3855,
331	      "ntp": 0.3223
332	    },
333	    "gap_ratio": 30.6,
334	    "comparison_s42": {
335	      "tf_gar_ours_delta": 0.0017,
336	      "ar_gar_ours_delta": 0.0008,
337	      "gap_ratio_delta": -1.4
338	    }
339	  }
340	}
341	
342	================================================================================
343	EXP_ID: eval_v8b_ss_s123
344	================================================================================
345	{
346	  "status": "DONE",
347	  "retry_count": 0,
348	  "created_at": "2026-05-21T21:15:52.880Z",
349	  "updated_at": "2026-05-21T22:53:15.356Z",
350	  "spec": {
351	    "command": "bash scripts/eval_v8b_ss_s123.sh",
352	    "server": "westd-20861",
353	    "gpu": [
354	      "cuda:0"
355	    ],
356	    "pid": 259767,
357	    "log_path": "runs/eval_v8b_ss_s123/",
358	    "submitted_at": "2026-05-21T21:15:52.785Z",
359	    "submitted_via": "submit_training_job",
360	    "backend": "tmux",
361	    "account": "root",
362	    "data_path": "data/ultrachat_eval_heldout.json",
363	    "data_count": 50,
364	    "model_name": "Qwen2.5-7B-Instruct",
365	    "seed": 123,
366	    "gpu_index": 0,
367	    "checkpoint_source": "checkpoints/tg_v8b_ss_s123/epoch_2",
368	    "eval_data": "ultrachat_eval_heldout + model-gen",
369	    "checkpoint_path": "checkpoints/tg_v8b_ss_s123/epoch_2",
370	    "wall_clock_seconds": 5835.7,
371	    "gpu_hours": 1.62
372	  },
373	  "hypothesis": "v8b SS model trained with s123 seed should reproduce s42 GAR metrics within acceptable gap_ratio [1.2x-2.5x] and no PPL degradation, confirming seed robustness of the scheduled sampling approach",
374	  "parent": "v7_tg_s123",
375	  "log_path": "~/runs/turn_residual_gating/eval_v8b_ss_s123.log",
376	  "conclusion": "success",
377	  "completed_at": "2026-05-21T22:53:08.443Z",
378	  "metrics": {
379	    "iid": {
380	      "gar_ours": 0.503,
381	      "gar_dongre": 0.394,
382	      "ppl": 2.781,
383	      "ntp_loss": 0.976,
384	      "n_conv": 50,
385	      "n_turns": 3
386	    },
387	    "modelgen": {
388	      "gar_ours": 0.418,
389	      "gar_dongre": 0.441,
390	      "ppl": 1.389,
391	      "ntp_loss": 0.325,
392	      "n_conv": 5,
393	      "n_turns": 10
394	    },
395	    "gap_ratio": 1.2,
396	    "base_iid_ppl": 4.338,
397	    "base_modelgen_ppl": 1.351
398	  }
399	}
400	
401	================================================================================
402	EXP_ID: phase2_4way_eval
403	================================================================================
404	{
405	  "status": "DONE",
406	  "retry_count": 0,
407	  "created_at": "2026-05-19T13:07:30.673Z",
408	  "updated_at": "2026-05-19T13:15:39.947Z",
409	  "hypothesis": "Turn-residual gating (TRG) improves multi-turn response quality over LoRA-only and base model baselines because it selectively amplifies conversational context signals, which should manifest as higher GAR scores across 4 conditions (base, base+TRG, LoRA, LoRA+TRG).",
410	  "spec": {
411	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && bash scripts/run_4way_eval.sh 2>&1 | tee runs/4way_eval.log\"",
412	    "server": "westd-20861",
413	    "gpu": [
414	      "cuda:0"
415	    ],
416	    "pid": "60024",
417	    "log_path": "/root/turn_residual_gating/runs/4way_eval.log",
418	    "submitted_at": "2026-05-19T13:07:37.380Z",
419	    "submitted_via": "submit_training_job",
420	    "backend": "tmux",
421	    "account": "root",
422	    "data_path": "/root/turn_residual_gating/data/ultrachat_8k",
423	    "data_count": 8000,
424	    "model_name": "Qwen2.5-7B-Instruct",
425	    "seed": 42,
426	    "checkpoint_source": "phase2_tg_s42_v7 + phase2_ug_s42 + phase2_lora_only_s42",
427	    "eval_data": "ultrachat_8k eval split",
428	    "checkpoint_path": "/root/turn_residual_gating/runs/4way_eval/",
429	    "wall_clock_seconds": 447.0,
430	    "gpu_hours": 0.12
431	  },
432	  "parent": "phase2_tg_s42_v7",
433	  "conclusion": "negative",
434	  "completed_at": "2026-05-19T13:15:04.405Z",
435	  "metrics": {
436	    "base_ours_mid_gar": 0.0107,
437	    "base_ours_recovery_pp": -0.15,
438	    "base_dongre_mid_gar": 0.003,
439	    "base_dongre_recovery_pp": -0.92,
440	    "base_ppl": 4.23,
441	    "base_ntp": 1.4162,
442	    "tg_ours_mid_gar": 0.4866,
443	    "tg_ours_recovery_pp": 47.44,
444	    "tg_dongre_mid_gar": 0.0157,
445	    "tg_dongre_recovery_pp": 0.35,
446	    "tg_ppl": 2.63,
447	    "tg_ntp": 0.9484,
448	    "ug_ours_mid_gar": 0.4923,
449	    "ug_ours_recovery_pp": 48.01,
450	    "ug_dongre_mid_gar": 0.013,
451	    "ug_dongre_recovery_pp": 0.08,
452	    "ug_ppl": 2.62,
453	    "ug_ntp": 0.9433,
454	    "lora_ours_mid_gar": 0.486,
455	    "lora_ours_recovery_pp": 47.39,
456	    "lora_dongre_mid_gar": 0.0137,
457	    "lora_dongre_recovery_pp": 0.15,
458	    "lora_ppl": 2.63,
459	    "lora_ntp": 0.9482,
460	    "route_b_confirmed": true,
461	    "gating_incremental_benefit": "none"
462	  },
463	  "notes": "\u56db\u8def eval \u5b8c\u6210\uff0cRoute B \u51b3\u5b9a\u6027\u786e\u8ba4\u3002\u4e09\u79cd\u8bad\u7ec3\u65b9\u6cd5\uff08TG/UG/LoRA-only\uff09\u5728\u63a8\u7406\u7aef\u5b8c\u5168\u8d8b\u540c\uff1aours GAR recovery ~47-48pp\uff08vs base -0.15pp\uff09\uff0cdongre GAR recovery 0.08-0.35pp\uff0cPPL 2.62-2.63\uff0cNTP 0.943-0.948\u3002Gating \u673a\u5236\uff08\u65e0\u8bba turn-conditioned \u8fd8\u662f uniform\uff09\u76f8\u6bd4\u7eaf LoRA \u5fae\u8c03\u96f6\u589e\u91cf\u3002LoRA fine-tuning \u662f GAR recovery \u7684\u552f\u4e00\u6765\u6e90\u3002hypothesis \u88ab\u8bc1\u4f2a\uff1aTRG \u4e0d\u6bd4 LoRA-only \u66f4\u597d\u3002"
464	}
465	
466	================================================================================
467	EXP_ID: phase2_4way_eval_heldout
468	================================================================================
469	{
470	  "status": "DONE",
471	  "retry_count": 0,
472	  "created_at": "2026-05-19T13:58:59.269Z",
473	  "updated_at": "2026-05-19T14:35:47.201Z",
474	  "hypothesis": "\u56db\u8def\u6d88\u878d\u7684\u4e09\u8def\u8d8b\u540c\u7ed3\u8bba\uff08TG\u2248UG\u2248LoRA-only\uff0cgating \u96f6\u589e\u91cf\uff09\u5728 held-out eval \u6570\u636e\uff08idx\u22658000\uff0c\u4e0e\u8bad\u7ec3\u96c6\u65e0\u91cd\u53e0\uff09\u4e0a\u590d\u73b0\uff0c\u6392\u9664\u6570\u636e\u91cd\u53e0 confound\u3002\u9884\u671f\uff1a\u76f8\u5bf9\u6bd4\u8f83\u4fdd\u6301\uff08\u4e09\u8def\u8d8b\u540c\uff09\uff0c\u7edd\u5bf9 GAR \u503c\u53ef\u80fd\u53d8\u5316\u3002",
475	  "parent": "phase2_4way_eval",
476	  "spec": {
477	    "command": "bash -c \"cd /root/turn_residual_gating && bash scripts/run_4way_eval_heldout.sh\"",
478	    "server": "westd-20861",
479	    "gpu": "cuda:0",
480	    "pid": 67204,
481	    "log_path": "~/runs/turn_residual_gating/phase2_4way_eval_heldout.log",
482	    "submitted_at": "2026-05-19T14:01:00.965Z",
483	    "submitted_via": "submit_training_job",
484	    "backend": "tmux",
485	    "account": "root",
486	    "data_path": "/root/turn_residual_gating/data/ultrachat_eval_heldout.json",
487	    "data_count": 50,
488	    "model_name": "Qwen2.5-7B-Instruct",
489	    "seed": 42,
490	    "checkpoint_source": "phase2_tg_s42_v7 + phase2_ug_s42 + phase2_lora_only_s42",
491	    "eval_data": "ultrachat_eval_heldout.json (50 convs, idx 8843-68199, no overlap with training 0-7999)",
492	    "configs": "4 models (Base/TG_v7/UG/LoRA-only) x 2 GAR variants (ours/Dongre) = 8 eval runs",
493	    "checkpoint_path": "N/A (eval-only)",
494	    "wall_clock_seconds": 2086.2,
495	    "gpu_hours": 0.58
496	  },
497	  "reproduce": {
498	    "finished_at": "2026-05-19T14:32:09.481Z"
499	  },
500	  "metrics": {
501	    "base_ours_mid_gar": 0.0128,
502	    "base_ours_recovery_pp": 0.06,
503	    "base_dongre_mid_gar": 0.0031,
504	    "base_dongre_recovery_pp": -0.91,
505	    "base_ppl": 4.34,
506	    "base_ntp": 1.4045,
507	    "tg_ours_mid_gar": 0.5035,
508	    "tg_ours_recovery_pp": 49.13,
509	    "tg_dongre_mid_gar": 0.0152,
510	    "tg_dongre_recovery_pp": 0.3,
511	    "tg_ppl": 2.78,
512	    "tg_ntp": 0.9771,
513	    "ug_ours_mid_gar": 0.5053,
514	    "ug_ours_recovery_pp": 49.31,
515	    "ug_dongre_mid_gar": 0.0124,
516	    "ug_dongre_recovery_pp": 0.02,
517	    "ug_ppl": 2.78,
518	    "ug_ntp": 0.9752,
519	    "lora_ours_mid_gar": 0.4978,
520	    "lora_ours_recovery_pp": 48.56,
521	    "lora_dongre_mid_gar": 0.0132,
522	    "lora_dongre_recovery_pp": 0.1,
523	    "lora_ppl": 2.78,
524	    "lora_ntp": 0.9771,
525	    "three_way_convergence_confirmed": true,
526	    "gar_ours_spread_pp": 0.75,
527	    "ppl_spread": 0,
528	    "data_overlap": false
529	  },
530	  "conclusion": "success",
531	  "notes": "Held-out eval \u4e09\u8def\u8d8b\u540c\u5b8c\u5168\u590d\u73b0\u3002TG/UG/LoRA-only GAR-ours: 0.504/0.505/0.498 (spread 0.75pp), PPL \u5747\u4e3a 2.78\u3002\u4e0e overlap \u6570\u636e\u76f8\u6bd4\u7edd\u5bf9\u503c\u7565\u9ad8\uff08GAR +1-2pp, PPL +0.15\uff09\uff0c\u5c5e\u6b63\u5e38\u6cdb\u5316\u504f\u79fb\uff0c\u76f8\u5bf9\u6bd4\u8f83\u5b8c\u5168\u4e00\u81f4\u3002\u6570\u636e\u5b8c\u6574\u6027 confound \u5df2\u6392\u9664\u3002",
532	  "completed_at": "2026-05-19T14:35:47.202Z"
533	}
534	
535	================================================================================
536	EXP_ID: phase2_tg_s42_v7
537	================================================================================
538	{
539	  "status": "DONE",
540	  "retry_count": 0,
541	  "created_at": "2026-05-18T18:17:45.739Z",
542	  "updated_at": "2026-05-20T03:04:19.923Z",
543	  "hypothesis": "MSE \u53cc\u5411 loss (mean_GAR - target)\u00b2 + gate diversity \u6b63\u5219 F.relu(min_std - gate_std) \u4ece\u7ed3\u6784\u4e0a\u89e3\u51b3\u6052\u7b49\u9000\u5316\uff1aMSE \u5728 GAR > target \u65f6\u53cd\u5411\u60e9\u7f5a\uff08\u4e0d\u518d\u5355\u8c03\u63a8\u9ad8\uff09\uff0cgate_div \u76f4\u63a5\u5f3a\u5236\u5c42\u95f4\u5206\u5316\u3002\u9884\u671f\uff1agate_std \u7a33\u5b9a >0.05 + GAR \u6536\u655b\u5230 target=0.5 \u9644\u8fd1 + NTP \u6b63\u5e38\u6536\u655b\u3002",
544	  "parent": "phase2_tg_s42_v6",
545	  "metrics": {
546	    "eval_iid_ours_mid_gar": 0.5035,
547	    "eval_iid_dongre_mid_gar": 0.0152,
548	    "eval_iid_ppl": 2.784,
549	    "eval_heldout_ours_mid_gar": 0.5035,
550	    "eval_heldout_dongre_mid_gar": 0.0152,
551	    "eval_heldout_ppl": 2.78,
552	    "eval_modelgen_ours_mid_gar": 0.0157,
553	    "eval_modelgen_dongre_mid_gar": 0.0194,
554	    "eval_modelgen_ppl": 1.36,
555	    "gate_mean_final": 0.9336,
556	    "gate_std_final": 0.0492
557	  },
558	  "spec": {
559	    "checkpoint_source": "from_scratch",
560	    "eval_data": "N/A",
561	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && PYTHONUNBUFFERED=1 python src/train_phase2.py --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --min-gate-std 0.05 --init-bias 1.5 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_tg_s42_v7 --data-dir /root/turn_residual_gating/data/ultrachat_8k --epochs 3\"",
562	    "server": "westd-20861",
563	    "gpu": "cuda:0",
564	    "data_path": "/root/turn_residual_gating/data/ultrachat_8k",
565	    "data_count": 8000,
566	    "model_name": "Qwen2.5-7B-Instruct",
567	    "seed": 42,
568	    "checkpoint_path": "/root/turn_residual_gating/runs/phase2_tg_s42_v7",
569	    "log_path": "/root/turn_residual_gating/runs/phase2_tg_s42_v7.log"
570	  },
571	  "reproduce": {
572	    "finished_at": "2026-05-19T00:48:47.275Z"
573	  },
574	  "failure_reason": "process dead 5\u00d7 with no sentinel/W&B \u2014 auto-resolved as failed",
575	  "conclusion": "success",
576	  "completed_at": "2026-05-19T00:48:47.463Z",
577	  "extra": {
578	    "hook_events": [
579	      {
580	        "event": "on_failed",
581	        "action": "agent",
582	        "ts": "2026-05-19T00:48:48.850580+00:00"
583	      }
584	    ]
585	  },
586	  "notes": "\u8bad\u7ec3 3 epoch \u5b8c\u6210 (21352s/5.9h)\u3002\u6700\u7ec8 gate: mean=0.9336, std=0.0492, L3=0.801 L4=0.789 \u6700\u4f4e\u3002Eval \u5b8c\u6210\uff1aGAR-ours recovery +0.35pp (mid 0.0157 vs baseline 0.0122), GAR-Dongre recovery +0.72pp (mid 0.0194 vs baseline 0.0122)\u3002Gate dynamic range \u6700\u5927\u5c42: L23 diff=-0.2100, L14 diff=-0.1803\u3002"
587	}
588	
589	================================================================================
590	EXP_ID: phase2_tg_s42_v9_pcgrad
591	================================================================================
592	{
593	  "status": "DONE",
594	  "retry_count": 2,
595	  "created_at": "2026-05-19T16:13:21.907Z",
596	  "updated_at": "2026-05-20T03:04:17.171Z",
597	  "hypothesis": "PCGrad (Yu et al. NeurIPS 2020) \u6d88\u9664 NTP-GAR \u68af\u5ea6\u65b9\u5411\u51b2\u7a81\u540e\uff08\u4ec5\u5bf9 gate \u53c2\u6570\u6295\u5f71 NTP \u68af\u5ea6\u5230 GAR \u68af\u5ea6\u6b63\u4ea4\u5e73\u9762\uff09\uff0c\u5982\u679c 30x training-inference GAR gap \u4ecd\u5728 \u2192 \u56e0\u679c\u8bc1\u636e\u8bc1\u660e exposure bias\uff08\u975e\u68af\u5ea6\u7ade\u4e89\uff09\u662f gap \u6839\u56e0\u3002\u4e0e v7 \u5bf9\u6bd4\uff1a\u76f8\u540c\u8d85\u53c2\uff08lambda_gar=1.0, MSE+gate_div\uff09\uff0c\u552f\u4e00\u53d8\u91cf\u662f\u68af\u5ea6\u5904\u7406\u65b9\u5f0f\u3002\u6210\u529f\u6807\u51c6\uff1a(1) \u68af\u5ea6 cos_sim \u663e\u8457\u6539\u5584\uff08\u4ece v7 \u7684 -0.089 \u63d0\u5347\u5230 \u22650\uff09\uff0c(2) \u4f46\u63a8\u7406 GAR \u4ecd \u2248 v7 \u6c34\u5e73\uff080.016\uff09\uff0c\u8bc1\u660e\u68af\u5ea6\u51b2\u7a81\u4e0d\u662f gap \u7684\u56e0\u3002",
598	  "parent": "phase2_tg_s42_v7",
599	  "spec": {
600	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && PYTHONUNBUFFERED=1 python src/train_phase2_v9_pcgrad.py --model /root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct --data-dir data/ultrachat_8k --output-dir checkpoints/tg_v9_pcgrad_s42 --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --lr 2e-4 --epochs 3 --batch-size 1 --grad-accum 8 --seed 42\"",
601	    "server": "westd-20861",
602	    "gpu": [
603	      "cuda:0"
604	    ],
605	    "pid": "83860",
606	    "log_path": "/root/turn_residual_gating/logs/phase2_tg_v9_pcgrad_s42.log",
607	    "submitted_at": "2026-05-19T17:42:10.820Z",
608	    "submitted_via": "submit_training_job",
609	    "backend": "tmux",
610	    "account": "root",
611	    "checkpoint_path": "/root/turn_residual_gating/checkpoints/tg_v9_pcgrad_s42",
612	    "wall_clock_seconds": 30601.5,
613	    "gpu_hours": 8.5
614	  },
615	  "reproduce": {
616	    "finished_at": "2026-05-20T01:42:12.536Z"
617	  },
618	  "failure_reason": null,
619	  "conclusion": "success",
620	  "extra": {
621	    "hook_events": [
622	      {
623	        "event": "on_failed",
624	        "action": "agent",
625	        "ts": "2026-05-19T17:35:39.776243+00:00",
626	        "note": "\u7b2c1\u6b21\u63d0\u4ea4 EXIT_CODE=2 \u6b8b\u7559\u4e8b\u4ef6"
627	      },
628	      {
629	        "event": "on_complete",
630	        "action": "agent",
631	        "ts": "2026-05-20T01:42:14.275822+00:00"
632	      }
633	    ]
634	  },
635	  "completed_at": null,
636	  "notes": "D028 \u56e0\u679c\u6392\u9664\u786e\u8ba4\uff08M017 \u4fee\u6b63\u540e\uff09\u3002\u8bad\u7ec3: EXIT_CODE=0, 7.98h, 3 epochs\u3002PCGrad cos_sim \u4ece -0.061\u2192+0.055\u2192-0.035 (\u56f4\u7ed5 0 \u632f\u8361), NTP mag_ratio 2.8\u219228.8 \u6301\u7eed\u589e\u957f\u3002L_GAR \u6709 0-350 step \u9ad8\u539f\u671f\u540e\u4ecd\u574d\u584c\u5230\u22480\u3002IID eval (\u540c protocol 50 heldout convs): GAR-ours=0.5002 (vs v7 0.5035, diff -0.33pp), GAR-Dongre=0.0123 (vs v7 0.0152), PPL=2.780 (vs v7 2.784, diff 0.004, \u65e0\u6539\u5584)\u3002Model-gen eval (5 convs): GAR-ours=0.0151, PPL=1.50\u3002\u7ed3\u8bba: PCGrad \u6d88\u9664\u68af\u5ea6\u65b9\u5411\u51b2\u7a81\u540e\u6240\u6709 IID \u6307\u6807\u5747 \u2248 v7\uff08GAR\u3001PPL\u3001NTP \u65e0\u53d8\u5316\uff09\uff0c\u65b9\u5411\u51b2\u7a81\u56e0 NTP \u5e45\u5ea6\u4e3b\u5bfc (10-40x) \u800c inconsequential\u3002Exposure bias \u662f 30x gap \u6839\u56e0\u3002",
637	  "metrics": {
638	    "eval_iid_ours_mid_gar": 0.5002,
639	    "eval_iid_dongre_mid_gar": 0.0123,
640	    "eval_iid_ppl": 2.78,
641	    "eval_iid_ntp": 0.9752,
642	    "eval_heldout_ours_mid_gar": 0.5002,
643	    "eval_heldout_dongre_mid_gar": 0.0123,
644	    "eval_heldout_ppl": 2.78,
645	    "eval_heldout_ntp": 0.9752,
646	    "eval_modelgen_ours_mid_gar": 0.0151,
647	    "eval_modelgen_dongre_mid_gar": 0.0173,
648	    "eval_modelgen_ppl": 1.5,
649	    "vs_v7_iid_ppl_diff": 0.004,
650	    "vs_v7_iid_gar_diff": -0.0033
651	  }
652	}
653	
654	================================================================================
655	EXP_ID: phase2_lora_only_s42
656	================================================================================
657	{
658	  "status": "DONE",
659	  "retry_count": 1,
660	  "created_at": "2026-05-18T20:36:32.506Z",
661	  "updated_at": "2026-05-20T02:15:18.992Z",
662	  "hypothesis": "LoRA-only baseline (gate \u56fa\u5b9a 1.0\uff0c\u65e0 gating \u673a\u5236) \u5728\u76f8\u540c MSE+NTP loss \u4e0b GAR \u5e94\u4f4e\u4e8e ThreadGate (v7)\u3002\u5982\u679c LoRA-only \u4e5f\u80fd\u8bad\u5230 GAR~0.5\uff0c\u5219 gating \u673a\u5236\u8d21\u732e\u4e3a\u96f6\uff0cpaper story \u4e0d\u6210\u7acb\u3002\u5173\u952e\u5bf9\u6bd4\uff1aLoRA-only \u7684 GAR \u6536\u655b\u503c vs v7 \u7684 0.48\u3002",
663	  "parent": "phase2_tg_s42_v7",
664	  "failure_reason": "EXIT_CODE=1 (generic error \u2014 check log tail)",
665	  "completed_at": "2026-05-19T12:44:29.475Z",
666	  "extra": {
667	    "previous_failure": {
668	      "conclusion": "failed"
669	    },
670	    "hook_events": [
671	      {
672	        "event": "on_failed",
673	        "action": "agent",
674	        "ts": "2026-05-19T13:04:35.644174+00:00"
675	      }
676	    ]
677	  },
678	  "spec": {
679	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && PYTHONUNBUFFERED=1 python src/train_phase2.py --gate-type lora_only --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 0.0 --init-bias 1.5 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_lora_only_s42 --data-dir /root/turn_residual_gating/data/ultrachat_8k --epochs 3\"",
680	    "server": "westd-20861",
681	    "gpu": "cuda:0",
682	    "data_path": "/root/turn_residual_gating/data/ultrachat_8k",
683	    "data_count": 8000,
684	    "model_name": "Qwen2.5-7B-Instruct",
685	    "seed": 42,
686	    "checkpoint_path": "/root/turn_residual_gating/runs/phase2_lora_only_s42",
687	    "log_path": "/root/turn_residual_gating/runs/phase2_lora_only_s42.log",
688	    "checkpoint_source": "from_scratch",
689	    "eval_data": "N/A"
690	  },
691	  "reproduce": {
692	    "finished_at": "2026-05-19T13:04:33.523Z"
693	  },
694	  "conclusion": "success",
695	  "metrics": {
696	    "epochs_completed": 3,
697	    "global_steps": 3000,
698	    "training_time_seconds": 20588.6,
699	    "training_time_hours": 5.7,
700	    "gate_fixed": 1,
701	    "gate_type_actual": "none",
702	    "final_lora_size_mb": 20,
703	    "eval_modelgen_ours_mid_gar": 0.0245,
704	    "eval_modelgen_dongre_mid_gar": 0.0185,
705	    "eval_modelgen_ppl": 1.371
706	  },
707	  "checkpoint_path": "/root/runs/turn_residual_gating/runs/phase2_lora_only_s42/lora/",
708	  "log_path": "/root/runs/turn_residual_gating/phase2_lora_only_s42.log",
709	  "notes": "\u8bca\u65ad\u786e\u8ba4\uff1aEXIT_CODE=1 \u56e0 argparse \u4e0d\u8ba4 lora_only \u9009\u9879\uff08choices \u53ea\u6709 threadgate/uniform/none\uff09\u3002\u8bad\u7ec3\u5b9e\u9645\u5df2\u7528 --gate-type none \u5b8c\u6210 3 epoch (3000 steps, 20588.6s/5.7h)\u3002Gate \u5168\u7a0b\u56fa\u5b9a 1.0\uff08\u7b26\u5408 lora_only \u8bed\u4e49\uff09\u3002Checkpoint \u53ef\u7528\uff0c\u65e0\u9700\u91cd\u8dd1\u3002\u4fee\u590d\uff1adispatch \u547d\u4ee4\u6539\u7528 --gate-type none \u6216\u5728 train_phase2.py \u6dfb\u52a0 lora_only choice\u3002"
710	}
711	
712	================================================================================
713	EXP_ID: phase2_ug_s42
714	================================================================================
715	{
716	  "status": "DONE",
717	  "retry_count": 0,
718	  "created_at": "2026-05-18T06:04:17.643Z",
719	  "updated_at": "2026-05-20T02:15:15.775Z",
720	  "hypothesis": "Uniform gating baseline: per-layer independent gates without turn conditioning (content-dependent only), to isolate whether ThreadGate's turn-conditioned gating provides benefit over content-only residual scaling. Same training setup as v7 but with gate-type=uniform.",
721	  "parent": "phase1_gar_diag",
722	  "notes": "3 epoch \u5b8c\u6210 (21994.5s/6.1h)\u3002\u6700\u7ec8 gate: mean=0.9598, std=0.0518, L3=0.777 L5=0.812 \u6700\u4f4e\u3002\u91cd\u8981\u53d1\u73b0\uff1auniform gate \u6a21\u5f0f\u4e0b\u5404\u5c42\u4ecd\u5b66\u51fa per-layer \u5206\u5316\uff08L3=0.777 vs L27=1.000\uff09\uff0c\u4e0e ThreadGate v7 \u7684 L3/L4 \u6700\u4f4e\u6a21\u5f0f\u4e00\u81f4\u3002\u8fd9\u8bf4\u660e per-layer variation \u53ef\u80fd\u6765\u81ea LoRA+GAR loss \u800c\u975e gate architecture\u3002",
723	  "spec": {
724	    "command": "python src/train_phase2.py --gate-type uniform --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --min-gate-std 0.05 --init-bias 1.5 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_ug_s42 --data-dir /root/turn_residual_gating/data/ultrachat_8k --epochs 3",
725	    "server": "westd-20861",
726	    "data_path": "/root/turn_residual_gating/data/ultrachat_8k",
727	    "data_count": 8000,
728	    "model_name": "Qwen2.5-7B-Instruct",
729	    "seed": 42,
730	    "checkpoint_path": "/root/turn_residual_gating/runs/phase2_ug_s42",
731	    "log_path": "/root/turn_residual_gating/runs/phase2_ug_s42.log",
732	    "checkpoint_source": "from_scratch",
733	    "eval_data": "N/A"
734	  },
735	  "conclusion": "success",
736	  "completed_at": "2026-05-19T06:53:13.931Z",
737	  "metrics": {
738	    "epoch0_avg_loss": 1.0019,
739	    "epoch0_avg_ntp": 0.9755,
740	    "epoch0_avg_gar": 0.0259,
741	    "epoch0_avg_div": 0.0005,
742	    "epoch1_avg_loss": 0.9447,
743	    "epoch1_avg_ntp": 0.9435,
744	    "epoch1_avg_gar": 0.0013,
745	    "epoch1_avg_div": 0,
746	    "epoch2_avg_loss": 0.9319,
747	    "epoch2_avg_ntp": 0.9309,
748	    "epoch2_avg_gar": 0.001,
749	    "epoch2_avg_div": 0,
750	    "final_gate_mean": 0.9598,
751	    "final_gate_std": 0.0518,
752	    "final_gate_min": 0.7773,
753	    "final_gate_max": 1,
754	    "final_profile_L3": 0.777,
755	    "final_profile_L5": 0.812,
756	    "final_profile_L0": 0.875,
757	    "final_profile_L27": 1,
758	    "training_time_seconds": 21994.5,
759	    "training_time_hours": 6.1,
760	    "global_steps": 7950,
761	    "unexpected_per_layer_variation": true,
762	    "eval_modelgen_ours_mid_gar": 0.0149,
763	    "eval_modelgen_dongre_mid_gar": 0.0185,
764	    "eval_modelgen_ppl": 1.396
765	  },
766	  "checkpoint_path": "/root/turn_residual_gating/runs/phase2_ug_s42",
767	  "log_path": "/root/turn_residual_gating/runs/phase2_ug_s42.log"
768	}
769	
770	================================================================================
771	EXP_ID: attention_steering_gen_n50
772	================================================================================
773	{
774	  "status": "DONE",
775	  "retry_count": 0,
776	  "created_at": "2026-05-20T19:04:17.455Z",
777	  "updated_at": "2026-05-21T01:59:57.100Z",
778	  "hypothesis": "N=5 gen steering \u663e\u793a \u03b2\u2208[2,5] phase transition (GAR 0.06\u21920.68)\uff0c\u4f46\u6837\u672c\u91cf\u4e0d\u8db3\u4ee5\u62a5\u544a\u7f6e\u4fe1\u533a\u95f4\u3002N=50 conversations \u5e94\u91cd\u73b0\u540c\u4e00 phase transition pattern \u5e76\u63d0\u4f9b\u7edf\u8ba1\u9c81\u68d2\u7684 mean\u00b1std\uff0c\u52a0\u56fa C6 claim (attention steering as causal mechanism proof)\u3002",
779	  "parent": "attention_steering_v7_tg_gen",
780	  "spec": {
781	    "command": "CUDA_VISIBLE_DEVICES=0 python src/eval_attention_steering.py --checkpoint runs/phase2_tg_s42_v7 --mode gen --data-file data/eval_200/eval_200.json --max-convs 50 --beta 0 2 3 4 5 10 --output-dir runs/attention_steering/ --output-name attention_steering_gen_n50",
782	    "server": "westd-20861",
783	    "gpu": [
784	      "cuda:0"
785	    ],
786	    "data_path": "data/eval_200/eval_200.json",
787	    "data_count": 50,
788	    "model_name": "Qwen2.5-7B-Instruct + v7 TG LoRA",
789	    "seed": "N/A (eval)",
790	    "checkpoint_source": "phase2_tg_s42_v7",
791	    "eval_data": "50 conversations from eval_200.json, gen mode autoregressive",
792	    "checkpoint_path": "N/A (eval experiment)",
793	    "log_path": "/root/turn_residual_gating/runs/attention_steering/attention_steering_gen_n50.json"
794	  },
795	  "metrics": {
796	    "corrected": true,
797	    "aggregation": "per-conv mid_gar(turns 2-7), >=3 turns only",
798	    "beta_0.0": {
799	      "mid_gar": 0.0641,
800	      "mid_gar_std": 0.0809,
801	      "ppl": 1.4324,
802	      "ppl_std": 0.1029,
803	      "n_valid": 39
804	    },
805	    "beta_2.0": {
806	      "mid_gar": 0.128,
807	      "mid_gar_std": 0.1101,
808	      "ppl": 1.4822,
809	      "ppl_std": 0.1385,
810	      "n_valid": 39
811	    },
812	    "beta_3.0": {
813	      "mid_gar": 0.5558,
814	      "mid_gar_std": 0.0601,
815	      "ppl": 1.5605,
816	      "ppl_std": 0.1719,
817	      "n_valid": 39
818	    },
819	    "beta_4.0": {
820	      "mid_gar": 0.6439,
821	      "mid_gar_std": 0.0607,
822	      "ppl": 1.6674,
823	      "ppl_std": 0.2241,
824	      "n_valid": 39
825	    },
826	    "beta_5.0": {
827	      "mid_gar": 0.7271,
828	      "mid_gar_std": 0.0605,
829	      "ppl": 1.7723,
830	      "ppl_std": 0.2693,
831	      "n_valid": 38
832	    },
833	    "beta_10.0": {
834	      "mid_gar": 0.9612,
835	      "mid_gar_std": 0.0152,
836	      "ppl": 3.4517,
837	      "ppl_std": 1.7813,
838	      "n_valid": 39
839	    },
840	    "n_convs_total": 50,
841	    "n_convs_valid": 39,
842	    "mode": "gen",
843	    "phase_transition_range": "[2, 3]"
844	  },
845	  "conclusion": "success",
846	  "notes": "\u539f\u59cb\u805a\u5408\u6709 min_turns \u622a\u65ad bug\uff08\u622a\u5230 2 turns\uff09\uff0c\u4fee\u6b63\u540e\u7528 per-conv mid_gar(turns 2-7)\u300239/50 \u5bf9\u8bdd\u6709 \u22653 turns \u53c2\u4e0e\u7edf\u8ba1\u3002\u4fee\u6b63\u540e baseline \u03b2=0 GAR \u4ece 0.101 \u964d\u5230 0.064\uff08median 0.031 \u4e0e N=5 \u7684 0.028 \u4e00\u81f4\uff09\u3002Phase transition \u5728 \u03b2\u2208[2,3] \u91cd\u73b0\u3002\u03b2=10 corrected 0.961 \u2248 N=5 \u7684 0.959\u3002",
847	  "completed_at": "2026-05-20T19:55:34.383Z"
848	}
849	
850	================================================================================
851	EXP_ID: attention_steering_v7_tg_gen
852	================================================================================
853	{
854	  "status": "DONE",
855	  "retry_count": 0,
856	  "created_at": "2026-05-20T07:07:20.607Z",
857	  "updated_at": "2026-05-20T09:30:17.530Z",
858	  "hypothesis": "\u63a8\u7406\u65f6\u5411 attention logits \u6ce8\u5165 goal-position bias \u03b2 \u53ef\u6062\u590d autoregressive GAR\u3002\u5982\u679c GAR \u4ece 0.015 \u663e\u8457\u63d0\u5347 \u2192 \u95ed\u5408\u56e0\u679c\u73af\uff1aexposure bias \u2192 attention \u504f\u79fb \u2192 GAR \u574d\u584c \u2192 \u624b\u52a8\u4fee\u6b63\u6ce8\u610f\u529b \u2192 GAR \u6062\u590d\u3002\u626b\u63cf \u03b2 \u2208 {0, 0.5, 1.0, 2.0, 5.0, 10.0}\uff0c\u6210\u529f\u6807\u51c6\uff1aGAR > 0.1 \u4e14 PPL \u4e0d\u4e25\u91cd\u6076\u5316\u3002",
859	  "parent": "phase2_tg_s42_v7",
860	  "spec": {
861	    "command": "bash scripts/launch_attention_steering.sh gen",
862	    "server": "westd-20861",
863	    "gpu": [
864	      "cuda:0"
865	    ],
866	    "pid": "157657",
867	    "log_path": "runs/attention_steering/phase2_tg_s42_v7_attention_steering.json",
868	    "submitted_at": "2026-05-20T07:07:27.678Z",
869	    "submitted_via": "submit_training_job",
870	    "backend": "tmux",
871	    "account": "root",
872	    "data_path": "data/ShareGPT_V3_format_5convs.json",
873	    "data_count": 5,
874	    "model_name": "Qwen/Qwen2.5-7B-Instruct",
875	    "seed": 42,
876	    "checkpoint_source": "phase2_tg_s42_v7",
877	    "eval_data": "data/ShareGPT_V3_format_5convs.json",
878	    "checkpoint_path": "checkpoints/tg_v7_s42/final",
879	    "wall_clock_seconds": 8551.2,
880	    "gpu_hours": 2.38
881	  },
882	  "conclusion": "success",
883	  "completed_at": "2026-05-20T09:29:58.880Z",
884	  "metrics": {
885	    "beta_0.0": {
886	      "mid_turns_avg_gar": 0.028,
887	      "avg_ppl": 1.409
888	    },
889	    "beta_0.5": {
890	      "mid_turns_avg_gar": 0.0287,
891	      "avg_ppl": 1.387
892	    },
893	    "beta_1.0": {
894	      "mid_turns_avg_gar": 0.0349,
895	      "avg_ppl": 1.36
896	    },
897	    "beta_2.0": {
898	      "mid_turns_avg_gar": 0.062,
899	      "avg_ppl": 1.411
900	    },
901	    "beta_5.0": {
902	      "mid_turns_avg_gar": 0.6795,
903	      "avg_ppl": 1.908
904	    },
905	    "beta_10.0": {
906	      "mid_turns_avg_gar": 0.959,
907	      "avg_ppl": 4.22
908	    },
909	    "phase_transition_range": "[2, 5]",
910	    "baseline_gar": 0.028,
911	    "max_gar_at_acceptable_ppl": 0.6795,
912	    "max_gar_at_acceptable_ppl_beta": 5
913	  },
914	  "notes": "Attention steering \u95ed\u5408\u56e0\u679c\u73af\u3002\u03b2=0\u21922: GAR \u7f13\u5347 (0.028\u21920.062), PPL \u4e0d\u53d8 (~1.4); \u03b2=5: phase transition, GAR \u8df3\u81f3 0.68, PPL \u5347\u81f3 1.91; \u03b2=10: GAR \u9971\u548c 0.96, PPL \u6076\u5316 4.22\u3002\u6210\u529f\u6807\u51c6 (GAR>0.1 \u4e14 PPL \u4e0d\u4e25\u91cd\u6076\u5316) \u5728 \u03b2=2 \u5373\u6ee1\u8db3\u3002\u03b2\u2208[2,5] \u5b58\u5728 phase transition\u3002\u8bc1\u660e\uff1a\u624b\u52a8\u4fee\u6b63 attention \u6307\u5411 goal tokens \u2192 \u76f4\u63a5\u6062\u590d GAR \u2192 \u786e\u8ba4 exposure bias \u901a\u8fc7 attention \u504f\u79fb\u5bfc\u81f4 GAR \u574d\u584c\u3002"
915	}
916	
917	================================================================================
918	EXP_ID: phase1_gar_diag
919	================================================================================
920	{
921	  "status": "DONE",
922	  "retry_count": 0,
923	  "created_at": "2026-05-18T05:24:07.903Z",
924	  "updated_at": "2026-05-18T05:59:25.324Z",
925	  "hypothesis": "Qwen2.5-7B-Instruct \u5728 10-turn \u591a\u8f6e\u5bf9\u8bdd\u4e2d\uff0c\u4e2d\u95f4 turns (3-8) \u7684 GAR (Goal Accessibility Ratio) \u76f8\u5bf9 turn-1 \u4e0b\u964d \u226515%\uff0c\u8868\u660e\u6a21\u578b\u5bf9 system prompt \u4e2d\u76ee\u6807 token \u7684\u6ce8\u610f\u529b\u968f\u5bf9\u8bdd\u8fdb\u884c\u663e\u8457\u8870\u51cf",
926	  "spec": {
927	    "command": "python run_phase1_gar.py --results-dir /root/turn_residual_gating/results",
928	    "server": "westd-20861",
929	    "model_name": "Qwen/Qwen2.5-7B-Instruct",
930	    "data_path": "built-in 5 conversations (knowledge_qa, coding_help, creative_writing, math_reasoning, roleplay_advisor)",
931	    "data_count": 5,
932	    "seed": 0,
933	    "checkpoint_path": "N/A",
934	    "log_path": "/root/turn_residual_gating/results/phase1_run.log"
935	  },
936	  "conclusion": "success",
937	  "metrics": {
938	    "turn1_avg_gar": 0.0418,
939	    "mid_turns_avg_gar": 0.0122,
940	    "relative_drop": 0.708,
941	    "num_conversations": 5,
942	    "num_turns": 10,
943	    "per_turn_avg_gar": [
944	      0.0418,
945	      0.0241,
946	      0.0224,
947	      0.013,
948	      0.0133,
949	      0.0086,
950	      0.0078,
951	      0.008,
952	      0.0157,
953	      0.0064
954	    ]
955	  },
956	  "completed_at": "2026-05-18T05:59:25.325Z"
957	}
958	
959	================================================================================
960	EXP_ID: llama_phase1_gar_diag
961	================================================================================
962	{
963	  "status": "DONE",
964	  "retry_count": 0,
965	  "created_at": "2026-05-20T19:39:25.751Z",
966	  "updated_at": "2026-05-21T01:34:36.417Z",
967	  "hypothesis": "Llama-3.1-8B-Instruct \u5728 multi-turn dialogue \u4e2d\u4e5f\u5e94\u51fa\u73b0 goal attention decay\uff08\u4e0e Qwen-2.5-7B \u7c7b\u4f3c\uff09\uff0c\u786e\u8ba4 attention decay \u662f transformer \u67b6\u6784\u901a\u7528\u73b0\u8c61\u800c\u975e\u6a21\u578b\u7279\u6709\u3002Phase 1 \u8bca\u65ad\uff1a\u6d4b\u91cf base Llama \u7684 per-turn GAR profile\u3002",
968	  "spec": {
969	    "server": "westd-20861",
970	    "gpu": [
971	      "cuda:0"
972	    ],
973	    "account": "local",
974	    "command": "CUDA_VISIBLE_DEVICES=0 python src/run_phase1_gar_llama.py --model /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/ --output-dir /root/turn_residual_gating/runs/phase1_llama_gar_diag --max-new-tokens 256",
975	    "pid": "198817",
976	    "data_path": "built-in 5 conversations (knowledge_qa, coding_help, creative_writing, math_reasoning, debate)",
977	    "data_count": 5,
978	    "model_name": "Meta-Llama-3.1-8B-Instruct",
979	    "seed": 42,
980	    "checkpoint_source": "N/A (base model, no fine-tuning)",
981	    "eval_data": "5 built-in conversations x 10 turns each, gen mode",
982	    "checkpoint_path": "N/A",
983	    "log_path": "/root/turn_residual_gating/logs/llama_phase1_gar_diag.log"
984	  },
985	  "conclusion": "success",
986	  "metrics": {
987	    "per_turn_gar": {
988	      "turn_1": 0.0263,
989	      "turn_2": 0.0183,
990	      "turn_3": 0.0087,
991	      "turn_4": 0.0055,
992	      "turn_5": 0.006,
993	      "turn_6": 0.0035,
994	      "turn_7": 0.0038,
995	      "turn_8": 0.0037,
996	      "turn_9": 0.005,
997	      "turn_10": 0.0026
998	    },
999	    "t1_t10_decay_pct": 90.1,
1000	    "t1_mid38_drop_pct": 80.2,
1001	    "n_topics": 5,
1002	    "model": "Meta-Llama-3.1-8B-Instruct",
1003	    "mode": "gen",
1004	    "n_conversations": 5,
1005	    "n_turns": 10
1006	  },
1007	  "completed_at": "2026-05-21T01:34:36.417Z"
1008	}
1009	
1010	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a5808c0-25fd-4384-99be-e39641fa38b7",
  "isSidechain": true,
  "promptId": "d6038c84-bd9d-43b7-9ec0-15fb7e7a361e",
  "agentId": "a55231259953ee2cc",
  "type": "user",
  "uuid": "181c6e48-d211-46a8-81d5-d5d7c99e77c4",
  "sourceToolAssistantUUID": "7a5808c0-25fd-4384-99be-e39641fa38b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "bc94af32-4f18-47ef-82eb-b2e18fce9e57",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-22T08:29:20.313Z_

Here are the full extracted entries for all 16 experiment IDs:

---

**eval_llama_ar_n20**
- **metrics**: `base: {gar_ours_mid: 0.0088, gar_dongre_mid: 0.0049, ngar_ours_mid: 0.1019, ngar_dongre_mid: 0.1171, ppl: 1.293, ntp_loss: 0.2552}`, `tg: {gar_ours_mid: 0.0434, gar_dongre_mid: 0.0183, ngar_ours_mid: 0.5357, ngar_dongre_mid: 0.4436, ppl: 1.437, ntp_loss: 0.3612}`, `lora_only: {gar_ours_mid: 0.0284, gar_dongre_mid: 0.0205, ngar_ours_mid: 0.3488, ngar_dongre_mid: 0.4997, ppl: 1.419, ntp_loss: 0.3483}`, `n_conversations: 20, n_turns: 4`, `ranking_gar_ours: "TG(0.0434) > LO(0.0284) > Base(0.0088)"`, `ranking_gar_dongre: "LO(0.0205) > TG(0.0183) > Base(0.0049)"`
- **notes**: `"N=20 AR eval stabilizes estimates. Mean difference (TG 0.0434 > LO 0.0284) is driven by outlier spikes (5-8% of turns with GAR>0.4); **median shows TG ≈ LO (0.018 vs 0.018), consistent with zero-increment finding from Qwen**. Gate provides no incremental GAR benefit over LoRA-only on Llama, same as Qwen. PPL ordering preserved: Base(1.29) < LO(1.42) < TG(1.44). T=4, outlier turns still present in N=20 (TG conv9/15/18 have GAR>0.4 single turns, LO conv10/12/18/20 similar) but diluted by 4x larger sample vs N=5."`
- **"mid"/"turn" fields**: metrics keys contain `gar_ours_mid`, `gar_dongre_mid`, `ngar_ours_mid`, `ngar_dongre_mid` for all three conditions; `n_turns: 4`; notes mention "turns with GAR>0.4", "outlier turns"

---

**eval_llama_lora_only_s42**
- **metrics**: `tf: {gar_ours: 0.4807, gar_dongre: 0.0188, ngar_ours: 11.8031, ngar_dongre: 0.8261, ppl: 2.6, ntp_loss: 0.9366, n_conversations: 50, n_turns: 4}`, `ar: {gar_ours: 0.0617, gar_dongre: 0.0226, ngar_ours: 0.6065, ngar_dongre: 0.2537, ppl: 1.32, ntp_loss: 0.2787, n_conversations: 5, n_turns: 10}`, `gap_ratio_gar_ours: 7.79`
- **notes**: (none)
- **"mid"/"turn" fields**: `n_turns: 4` (tf), `n_turns: 10` (ar)

---

**llama_eval_s42**
- **metrics**: `tf_base: {gar_ours: 0.0166, ngar_ours: 0.3882, gar_dongre: 0.0038, ngar_dongre: 0.163, ppl: 3.45, N: 50, T: 4}`, `tf_tg: {gar_ours: 0.4836, ngar_ours: 11.8818, gar_dongre: 0.018, ngar_dongre: 0.7922, ppl: 2.57, N: 50, T: 4}`, `ar_base: {gar_ours: 0.0086, ngar_ours: 0.0798, gar_dongre: 0.0118, ngar_dongre: 0.1265, ppl: 1.24, N: 5, T: 10}`, `ar_tg: {gar_ours: 0.0304, ngar_ours: 0.2632, gar_dongre: 0.0217, ngar_dongre: 0.2459, ppl: 1.32, N: 5, T: 10}`, `gap_ratio_tg_ours: 15.9`, `gap_ratio_base_ours: 1.93`, `gap_ratio_tg_dongre: 0.83`, `vs_qwen_v7_gap_ratio: 32.1`, `baseline_mid_gar: 0.0122`
- **notes**: `"C5 跨模型泛化确认。Llama TG GAR-ours gap 16x (TF 0.484 vs AR 0.030)，低于 Qwen v7 的 32x 但仍非常显著。Base model gap 仅 1.9x（control 通过）。注意 TF/AR eval 设定不同 (N=50/T=4 vs N=5/T=10)，可能影响绝对值对比。GAR-dongre 无明显 gap (ratio 0.83x, AR ≥ TF)，仅 GAR-ours 展现 exposure bias 效应。Gate dynamic range: L24/L28/L30 diff 最大 (0.23-0.38)，与 Qwen 类似集中在中高层。"`
- **"mid"/"turn" fields**: `baseline_mid_gar: 0.0122`; notes mention "中高层" (mid-high layers)

---

**llama_ar_matched_eval**
- **metrics**: `ar_base_ours: {mid_gar: 0.0082, ngar: 0.1, ppl: 1.267}`, `ar_tg_ours: {mid_gar: 0.0388, ngar: 0.493, ppl: 1.413}`, `ar_base_dongre: {mid_gar: 0.0051, ngar: 0.12, ppl: 1.267}`, `ar_tg_dongre: {mid_gar: 0.018, ngar: 0.431, ppl: 1.413}`, `tf_reference: {tf_tg_ours_ngar: 11.88, tf_base_ours_ngar: 0.388, tf_tg_ours_raw: 0.4836, tf_tg_dongre_raw: 0.018}`, `matched_gap_analysis: {gar_ours_raw_gap: "12.5x (TF 0.484 / AR 0.039)", gar_ours_ngar_gap: "24.1x (TF 11.88 / AR 0.493)", gar_dongre_raw_gap: "1.002x (TF 0.018 / AR 0.018) — zero gap", tg_over_base_ar_ours: "4.71x", tg_over_base_ar_dongre: "3.54x", conclusion: "GAR-ours TF-AR gap 12.5x (raw) / 24x (nGAR) is genuine exposure bias. GAR-Dongre zero gap (1.002x) confirms mechanism specificity: exposure bias selectively destroys learned goal-attention routing while leaving content-overlap-based attention unaffected."}`
- **notes**: `"CORRECTION (2026-05-21 04:36): Agent 之前错误地将 AR TG nGAR (0.493) 与 TF TG raw GAR (0.484) 对比，误判为 'nGAR aligns, gap is normalization artifact'。Reviewer 核实：TF TG ours nGAR = 11.88（非 0.48）。nGAR gap = 11.88 / 0.493 = 24.1×，比 raw gap (12.5×) 还大。'Normalization artifact' 分析完全错误——GAR-ours 的 gap 是真实的 exposure bias。论文绝对不能使用 normalization artifact 叙事。"`
- **"mid"/"turn" fields**: all metrics sub-objects contain `mid_gar` keys

---

**eval_v7_tg_s123**
- **metrics**: `iid_tf: {gar_ours_mid: 0.5052, gar_dongre_mid: 0.0119, ppl: 2.7802, ntp: 0.9752}`, `modelgen_ar: {gar_ours_mid: 0.0165, gar_dongre_mid: 0.0177, ppl: 1.3855, ntp: 0.3223}`, `gap_ratio: 30.6`, `comparison_s42: {tf_gar_ours_delta: 0.0017, ar_gar_ours_delta: 0.0008, gap_ratio_delta: -1.4}`
- **notes**: (none)
- **"mid"/"turn" fields**: `gar_ours_mid`, `gar_dongre_mid` in both iid_tf and modelgen_ar

---

**eval_v8b_ss_s123**
- **metrics**: `iid: {gar_ours: 0.503, gar_dongre: 0.394, ppl: 2.781, ntp_loss: 0.976, n_conv: 50, n_turns: 3}`, `modelgen: {gar_ours: 0.418, gar_dongre: 0.441, ppl: 1.389, ntp_loss: 0.325, n_conv: 5, n_turns: 10}`, `gap_ratio: 1.2`, `base_iid_ppl: 4.338`, `base_modelgen_ppl: 1.351`
- **notes**: (none)
- **"mid"/"turn" fields**: `n_turns: 3` (iid), `n_turns: 10` (modelgen)

---

**phase2_4way_eval**
- **metrics**: `base_ours_mid_gar: 0.0107`, `base_ours_recovery_pp: -0.15`, `base_dongre_mid_gar: 0.003`, `base_dongre_recovery_pp: -0.92`, `base_ppl: 4.23`, `base_ntp: 1.4162`, `tg_ours_mid_gar: 0.4866`, `tg_ours_recovery_pp: 47.44`, `tg_dongre_mid_gar: 0.0157`, `tg_dongre_recovery_pp: 0.35`, `tg_ppl: 2.63`, `tg_ntp: 0.9484`, `ug_ours_mid_gar: 0.4923`, `ug_ours_recovery_pp: 48.01`, `ug_dongre_mid_gar: 0.013`, `ug_dongre_recovery_pp: 0.08`, `ug_ppl: 2.62`, `ug_ntp: 0.9433`, `lora_ours_mid_gar: 0.486`, `lora_ours_recovery_pp: 47.39`, `lora_dongre_mid_gar: 0.0137`, `lora_dongre_recovery_pp: 0.15`, `lora_ppl: 2.63`, `lora_ntp: 0.9482`, `route_b_confirmed: true`, `gating_incremental_benefit: "none"`
- **notes**: `"四路 eval 完成，Route B 决定性确认。三种训练方法（TG/UG/LoRA-only）在推理端完全趋同：ours GAR recovery ~47-48pp（vs base -0.15pp），dongre GAR recovery 0.08-0.35pp，PPL 2.62-2.63，NTP 0.943-0.948。Gating 机制（无论 turn-conditioned 还是 uniform）相比纯 LoRA 微调零增量。LoRA fine-tuning 是 GAR recovery 的唯一来源。hypothesis 被证伪：TRG 不比 LoRA-only 更好。"`
- **"mid"/"turn" fields**: all `*_mid_gar` keys; notes mention "turn-conditioned"

---

**phase2_4way_eval_heldout**
- **metrics**: `base_ours_mid_gar: 0.0128`, `base_ours_recovery_pp: 0.06`, `base_dongre_mid_gar: 0.0031`, `base_dongre_recovery_pp: -0.91`, `base_ppl: 4.34`, `base_ntp: 1.4045`, `tg_ours_mid_gar: 0.5035`, `tg_ours_recovery_pp: 49.13`, `tg_dongre_mid_gar: 0.0152`, `tg_dongre_recovery_pp: 0.3`, `tg_ppl: 2.78`, `tg_ntp: 0.9771`, `ug_ours_mid_gar: 0.5053`, `ug_ours_recovery_pp: 49.31`, `ug_dongre_mid_gar: 0.0124`, `ug_dongre_recovery_pp: 0.02`, `ug_ppl: 2.78`, `ug_ntp: 0.9752`, `lora_ours_mid_gar: 0.4978`, `lora_ours_recovery_pp: 48.56`, `lora_dongre_mid_gar: 0.0132`, `lora_dongre_recovery_pp: 0.1`, `lora_ppl: 2.78`, `lora_ntp: 0.9771`, `three_way_convergence_confirmed: true`, `gar_ours_spread_pp: 0.75`, `ppl_spread: 0`, `data_overlap: false`
- **notes**: `"Held-out eval 三路趋同完全复现。TG/UG/LoRA-only GAR-ours: 0.504/0.505/0.498 (spread 0.75pp), PPL 均为 2.78。与 overlap 数据相比绝对值略高（GAR +1-2pp, PPL +0.15），属正常泛化偏移，相对比较完全一致。数据完整性 confound 已排除。"`
- **"mid"/"turn" fields**: all `*_mid_gar` keys

---

**phase2_tg_s42_v7**
- **metrics**: `eval_iid_ours_mid_gar: 0.5035`, `eval_iid_dongre_mid_gar: 0.0152`, `eval_iid_ppl: 2.784`, `eval_heldout_ours_mid_gar: 0.5035`, `eval_heldout_dongre_mid_gar: 0.0152`, `eval_heldout_ppl: 2.78`, `eval_modelgen_ours_mid_gar: 0.0157`, `eval_modelgen_dongre_mid_gar: 0.0194`, `eval_modelgen_ppl: 1.36`, `gate_mean_final: 0.9336`, `gate_std_final: 0.0492`
- **notes**: `"训练 3 epoch 完成 (21352s/5.9h)。最终 gate: mean=0.9336, std=0.0492, L3=0.801 L4=0.789 最低。Eval 完成：GAR-ours recovery +0.35pp (mid 0.0157 vs baseline 0.0122), GAR-Dongre recovery +0.72pp (mid 0.0194 vs baseline 0.0122)。Gate dynamic range 最大层: L23 diff=-0.2100, L14 diff=-0.1803。"`
- **"mid"/"turn" fields**: all `*_mid_gar` keys; notes mention "mid 0.0157 vs baseline 0.0122"

---

**phase2_tg_s42_v9_pcgrad**
- **metrics**: `eval_iid_ours_mid_gar: 0.5002`, `eval_iid_dongre_mid_gar: 0.0123`, `eval_iid_ppl: 2.78`, `eval_iid_ntp: 0.9752`, `eval_heldout_ours_mid_gar: 0.5002`, `eval_heldout_dongre_mid_gar: 0.0123`, `eval_heldout_ppl: 2.78`, `eval_heldout_ntp: 0.9752`, `eval_modelgen_ours_mid_gar: 0.0151`, `eval_modelgen_dongre_mid_gar: 0.0173`, `eval_modelgen_ppl: 1.5`, `vs_v7_iid_ppl_diff: 0.004`, `vs_v7_iid_gar_diff: -0.0033`
- **notes**: `"D028 因果排除确认（M017 修正后）。训练: EXIT_CODE=0, 7.98h, 3 epochs。PCGrad cos_sim 从 -0.061→+0.055→-0.035 (围绕 0 振荡), NTP mag_ratio 2.8→28.8 持续增长。L_GAR 有 0-350 step 高原期后仍坍塌到≈0。IID eval (同 protocol 50 heldout convs): GAR-ours=0.5002 (vs v7 0.5035, diff -0.33pp), GAR-Dongre=0.0123 (vs v7 0.0152), PPL=2.780 (vs v7 2.784, diff 0.004, 无改善)。Model-gen eval (5 convs): GAR-ours=0.0151, PPL=1.50。结论: PCGrad 消除梯度方向冲突后所有 IID 指标均 ≈ v7（GAR、PPL、NTP 无变化），方向冲突因 NTP 幅度主导 (10-40x) 而 inconsequential。Exposure bias 是 30x gap 根因。"`
- **"mid"/"turn" fields**: all `*_mid_gar` keys

---

**phase2_lora_only_s42**
- **metrics**: `epochs_completed: 3`, `global_steps: 3000`, `training_time_seconds: 20588.6`, `training_time_hours: 5.7`, `gate_fixed: 1`, `gate_type_actual: "none"`, `final_lora_size_mb: 20`, `eval_modelgen_ours_mid_gar: 0.0245`, `eval_modelgen_dongre_mid_gar: 0.0185`, `eval_modelgen_ppl: 1.371`
- **notes**: `"诊断确认：EXIT_CODE=1 因 argparse 不认 lora_only 选项（choices 只有 threadgate/uniform/none）。训练实际已用 --gate-type none 完成 3 epoch (3000 steps, 20588.6s/5.7h)。Gate 全程固定 1.0（符合 lora_only 语义）。Checkpoint 可用，无需重跑。修复：dispatch 命令改用 --gate-type none 或在 train_phase2.py 添加 lora_only choice。"`
- **"mid"/"turn" fields**: `eval_modelgen_ours_mid_gar`, `eval_modelgen_dongre_mid_gar`

---

**phase2_ug_s42**
- **metrics**: `epoch0_avg_loss: 1.0019`, `epoch0_avg_ntp: 0.9755`, `epoch0_avg_gar: 0.0259`, `epoch0_avg_div: 0.0005`, `epoch1_avg_loss: 0.9447`, `epoch1_avg_ntp: 0.9435`, `epoch1_avg_gar: 0.0013`, `epoch1_avg_div: 0`, `epoch2_avg_loss: 0.9319`, `epoch2_avg_ntp: 0.9309`, `epoch2_avg_gar: 0.001`, `epoch2_avg_div: 0`, `final_gate_mean: 0.9598`, `final_gate_std: 0.0518`, `final_gate_min: 0.7773`, `final_gate_max: 1`, `final_profile_L3: 0.777`, `final_profile_L5: 0.812`, `final_profile_L0: 0.875`, `final_profile_L27: 1`, `training_time_seconds: 21994.5`, `training_time_hours: 6.1`, `global_steps: 7950`, `unexpected_per_layer_variation: true`, `eval_modelgen_ours_mid_gar: 0.0149`, `eval_modelgen_dongre_mid_gar: 0.0185`, `eval_modelgen_ppl: 1.396`
- **notes**: `"3 epoch 完成 (21994.5s/6.1h)。最终 gate: mean=0.9598, std=0.0518, L3=0.777 L5=0.812 最低。重要发现：uniform gate 模式下各层仍学出 per-layer 分化（L3=0.777 vs L27=1.000），与 ThreadGate v7 的 L3/L4 最低模式一致。这说明 per-layer variation 可能来自 LoRA+GAR loss 而非 gate architecture。"`
- **"mid"/"turn" fields**: `eval_modelgen_ours_mid_gar`, `eval_modelgen_dongre_mid_gar`; notes mention "turn-conditioned" is absent (uniform gate)

---

**attention_steering_gen_n50**
- **metrics**: `corrected: true`, `aggregation: "per-conv mid_gar(turns 2-7), >=3 turns only"`, `beta_0.0: {mid_gar: 0.0641, mid_gar_std: 0.0809, ppl: 1.4324, ppl_std: 0.1029, n_valid: 39}`, `beta_2.0: {mid_gar: 0.128, mid_gar_std: 0.1101, ppl: 1.4822, ppl_std: 0.1385, n_valid: 39}`, `beta_3.0: {mid_gar: 0.5558, mid_gar_std: 0.0601, ppl: 1.5605, ppl_std: 0.1719, n_valid: 39}`, `beta_4.0: {mid_gar: 0.6439, mid_gar_std: 0.0607, ppl: 1.6674, ppl_std: 0.2241, n_valid: 39}`, `beta_5.0: {mid_gar: 0.7271, mid_gar_std: 0.0605, ppl: 1.7723, ppl_std: 0.2693, n_valid: 38}`, `beta_10.0: {mid_gar: 0.9612, mid_gar_std: 0.0152, ppl: 3.4517, ppl_std: 1.7813, n_valid: 39}`, `n_convs_total: 50`, `n_convs_valid: 39`, `mode: "gen"`, `phase_transition_range: "[2, 3]"`
- **notes**: `"原始聚合有 min_turns 截断 bug（截到 2 turns），修正后用 per-conv mid_gar(turns 2-7)。39/50 对话有 ≥3 turns 参与统计。修正后 baseline β=0 GAR 从 0.101 降到 0.064（median 0.031 与 N=5 的 0.028 一致）。Phase transition 在 β∈[2,3] 重现。β=10 corrected 0.961 ≈ N=5 的 0.959。"`
- **"mid"/"turn" fields**: all beta sub-objects contain `mid_gar`, `mid_gar_std`; aggregation says "mid_gar(turns 2-7)"; notes mention "turns"

---

**attention_steering_v7_tg_gen**
- **metrics**: `beta_0.0: {mid_turns_avg_gar: 0.028, avg_ppl: 1.409}`, `beta_0.5: {mid_turns_avg_gar: 0.0287, avg_ppl: 1.387}`, `beta_1.0: {mid_turns_avg_gar: 0.0349, avg_ppl: 1.36}`, `beta_2.0: {mid_turns_avg_gar: 0.062, avg_ppl: 1.411}`, `beta_5.0: {mid_turns_avg_gar: 0.6795, avg_ppl: 1.908}`, `beta_10.0: {mid_turns_avg_gar: 0.959, avg_ppl: 4.22}`, `phase_transition_range: "[2, 5]"`, `baseline_gar: 0.028`, `max_gar_at_acceptable_ppl: 0.6795`, `max_gar_at_acceptable_ppl_beta: 5`
- **notes**: `"Attention steering 闭合因果环。β=0→2: GAR 缓升 (0.028→0.062), PPL 不变 (~1.4); β=5: phase transition, GAR 跳至 0.68, PPL 升至 1.91; β=10: GAR 饱和 0.96, PPL 恶化 4.22。成功标准 (GAR>0.1 且 PPL 不严重恶化) 在 β=2 即满足。β∈[2,5] 存在 phase transition。证明：手动修正 attention 指向 goal tokens → 直接恢复 GAR → 确认 exposure bias 通过 attention 偏移导致 GAR 坍塌。"`
- **"mid"/"turn" fields**: all beta sub-objects contain `mid_turns_avg_gar`

---

**phase1_gar_diag**
- **metrics**: `turn1_avg_gar: 0.0418`, `mid_turns_avg_gar: 0.0122`, `relative_drop: 0.708`, `num_conversations: 5`, `num_turns: 10`, `per_turn_avg_gar: [0.0418, 0.0241, 0.0224, 0.013, 0.0133, 0.0086, 0.0078, 0.008, 0.0157, 0.0064]`
- **notes**: (none)
- **"mid"/"turn" fields**: `mid_turns_avg_gar: 0.0122`, `turn1_avg_gar: 0.0418`, `num_turns: 10`, `per_turn_avg_gar` array

---

**llama_phase1_gar_diag**
- **metrics**: `per_turn_gar: {turn_1: 0.0263, turn_2: 0.0183, turn_3: 0.0087, turn_4: 0.0055, turn_5: 0.006, turn_6: 0.0035, turn_7: 0.0038, turn_8: 0.0037, turn_9: 0.005, turn_10: 0.0026}`, `t1_t10_decay_pct: 90.1`, `t1_mid38_drop_pct: 80.2`, `n_topics: 5`, `model: "Meta-Llama-3.1-8B-Instruct"`, `mode: "gen"`, `n_conversations: 5`, `n_turns: 10`
- **notes**: (none)
- **"mid"/"turn" fields**: all `per_turn_gar` keys are `turn_1` through `turn_10`; `t1_mid38_drop_pct: 80.2` (mid-turn drop); `n_turns: 10`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "181c6e48-d211-46a8-81d5-d5d7c99e77c4",
  "isSidechain": true,
  "agentId": "a55231259953ee2cc",
  "requestId": "req_011CbHHmR31QiyzuuCkN3YAm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f256c3b9-8e94-46a1-b8a5-53ab516ace32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "bc94af32-4f18-47ef-82eb-b2e18fce9e57",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01296pPeVbqUZocqwHUpnnUe",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23484,
      "cache_read_input_tokens": 19628,
      "output_tokens": 7550,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 23484
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7550,
          "cache_read_input_tokens": 19628,
          "cache_creation_input_tokens": 23484,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 23484,
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
