# Research conversation: I need to extract specific experiment data from a large JSON registry file for a paper number audit. The file is at: /ho

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a20fa24a4723e1d9c.jsonl`
- **Structured JSON:** [`da7b132e60893daff7a2.json`](../../sessions/da/da7b132e60893daff7a2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

23 recorded events

### User

_source line 1 · 2026-05-24T04:30:04.857Z_

I need to extract specific experiment data from a large JSON registry file for a paper number audit. The file is at:
/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/8eaa3b36-4b2e-4596-a917-3c8550c7e172/tool-results/mcp-agent-ml-research-read_registry-1779596942026.txt

This is a JSON file with schema: {result: string}. The `result` field is itself a JSON string containing an array of experiment objects.

I need you to extract and return the following information for each experiment that has metrics data:
1. experiment_id
2. name/title
3. status
4. key metrics (especially: ppl, delta, p-value, std, any perplexity values)
5. conclusion/summary

Focus especially on experiments related to:
- Adaptive b* training (3-seed, various rho values: 0.4, 0.6, 0.2)
- Uniform baseline training
- Grid search b values
- ESS-only training
- Random reweighting
- Detect & Remove (D&R)
- 1.7B scale experiments
- Detector comparison (GPT-2, N-gram)
- Batch size experiments (B=4, B=8, B=16)
- Epoch-matched comparisons
- n_min sensitivity
- tau sensitivity
- OOD evaluation
- Constraint regime analysis

Use jq or python to parse the file. First probe the structure, then extract experiments with their metrics. Return a structured summary of all experiments with their key numbers. Be thorough - I need every experiment's metrics for cross-validation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c0ee33d1-40a2-4cb8-a0f0-d28fa12f6711",
  "agentId": "a20fa24a4723e1d9c",
  "type": "user",
  "uuid": "a28ff5d3-37be-47aa-b013-11c8088804a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "8eaa3b36-4b2e-4596-a917-3c8550c7e172",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-24T04:30:04.862Z_

```json
{
  "parentUuid": "a28ff5d3-37be-47aa-b013-11c8088804a6",
  "isSidechain": true,
  "agentId": "a20fa24a4723e1d9c",
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
  "uuid": "1487f5ec-422c-4c41-85fd-4096a3c74f7d",
  "timestamp": "2026-05-24T04:30:04.862Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "8eaa3b36-4b2e-4596-a917-3c8550c7e172",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-24T04:30:07.448Z_

I'll parse the JSON registry file and extract all experiment data systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1487f5ec-422c-4c41-85fd-4096a3c74f7d",
  "isSidechain": true,
  "agentId": "a20fa24a4723e1d9c",
  "requestId": "req_011CbLmKdH1V3LqK6ipn2fQg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ef86dc64-12ea-4a43-a13b-a99c253f00d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "8eaa3b36-4b2e-4596-a917-3c8550c7e172",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UgAhKRFBBKYT5AGg4hMueK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6877,
      "cache_read_input_tokens": 8113,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6877,
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

_source line 4 · 2026-05-24T04:30:09.001Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01WtChpHh9XZBoCSVMWKWUCT`</summary>

```json
{
  "command": "wc -c /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/8eaa3b36-4b2e-4596-a917-3c8550c7e172/tool-results/mcp-agent-ml-research-read_registry-1779596942026.txt",
  "description": "Check file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef86dc64-12ea-4a43-a13b-a99c253f00d4",
  "isSidechain": true,
  "agentId": "a20fa24a4723e1d9c",
  "requestId": "req_011CbLmKdH1V3LqK6ipn2fQg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc912626-68a5-4211-b7aa-f3a0b2ec0a4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "8eaa3b36-4b2e-4596-a917-3c8550c7e172",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UgAhKRFBBKYT5AGg4hMueK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6877,
      "cache_read_input_tokens": 8113,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6877
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 182,
          "cache_read_input_tokens": 8113,
          "cache_creation_input_tokens": 6877,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6877,
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

_source line 5 · 2026-05-24T04:30:09.151Z_

<details><summary>↩ Tool result · `toolu_01WtChpHh9XZBoCSVMWKWUCT`</summary>

```text
466066 /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/8eaa3b36-4b2e-4596-a917-3c8550c7e172/tool-results/mcp-agent-ml-research-read_registry-1779596942026.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc912626-68a5-4211-b7aa-f3a0b2ec0a4e",
  "isSidechain": true,
  "promptId": "c0ee33d1-40a2-4cb8-a0f0-d28fa12f6711",
  "agentId": "a20fa24a4723e1d9c",
  "type": "user",
  "uuid": "47ebfb1a-4f24-435c-9237-ced3b746a1f0",
  "sourceToolAssistantUUID": "bc912626-68a5-4211-b7aa-f3a0b2ec0a4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "8eaa3b36-4b2e-4596-a917-3c8550c7e172",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-24T04:30:16.238Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01SuK3wKwRHH8h2dBNHq5xrB`</summary>

```json
{
  "command": "python3 - <<'EOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/8eaa3b36-4b2e-4596-a917-3c8550c7e172/tool-results/mcp-agent-ml-research-read_registry-1779596942026.txt\"\n\nwith open(fpath) as f:\n    outer = json.load(f)\n\nprint(\"Outer keys:\", list(outer.keys()))\nresult_str = outer[\"result\"]\nprint(\"Result type:\", type(result_str))\nprint(\"Result preview (first 500 chars):\", result_str[:500])\nEOF\n",
  "description": "Probe outer structure and result field"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47ebfb1a-4f24-435c-9237-ced3b746a1f0",
  "isSidechain": true,
  "agentId": "a20fa24a4723e1d9c",
  "requestId": "req_011CbLmKwb5eyqwCKn2c1XY8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "93dc1dd6-68f0-4610-933e-a5c59105e37b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "8eaa3b36-4b2e-4596-a917-3c8550c7e172",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HiDL4bkhn8htjwtBP7HJV9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1128,
      "cache_read_input_tokens": 14990,
      "output_tokens": 258,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1128
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 258,
          "cache_read_input_tokens": 14990,
          "cache_creation_input_tokens": 1128,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1128,
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

_source line 7 · 2026-05-24T04:30:16.315Z_

<details><summary>↩ Tool result · `toolu_01SuK3wKwRHH8h2dBNHq5xrB`</summary>

```text
Outer keys: ['result']
Result type: &lt;class 'str'>
Result preview (first 500 chars): {"success": true, "data": {"experiments": {"aeff_only_nmin1_seed456": {"status": "DONE", "retry_count": 0, "created_at": "2026-05-23T13:41:16.042Z", "updated_at": "2026-05-24T01:50:47.441Z", "hypothesis": "α_eff-only ablation seed456: cross-seed replicate. n_min=1 removes ESS constraint. Third seed for paired t-test vs dual-constrained baseline.", "spec": {"gpu": "cuda:1", "server": "westd-41312", "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93dc1dd6-68f0-4610-933e-a5c59105e37b",
  "isSidechain": true,
  "promptId": "c0ee33d1-40a2-4cb8-a0f0-d28fa12f6711",
  "agentId": "a20fa24a4723e1d9c",
  "type": "user",
  "uuid": "9abeb65a-77f9-4d42-9c6d-75e9b3452216",
  "sourceToolAssistantUUID": "93dc1dd6-68f0-4610-933e-a5c59105e37b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "8eaa3b36-4b2e-4596-a917-3c8550c7e172",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-24T04:30:19.775Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01DSbcR5QXSfUTh9jBRsArxe`</summary>

```json
{
  "command": "python3 - <<'EOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/8eaa3b36-4b2e-4596-a917-3c8550c7e172/tool-results/mcp-agent-ml-research-read_registry-1779596942026.txt\"\n\nwith open(fpath) as f:\n    outer = json.load(f)\n\nregistry = json.loads(outer[\"result\"])\nexperiments = registry[\"data\"][\"experiments\"]\n\nprint(f\"Total experiments: {len(experiments)}\")\nprint(\"\\nAll experiment IDs:\")\nfor eid in sorted(experiments.keys()):\n    print(\" \", eid)\nEOF\n",
  "description": "List all experiment IDs and count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9abeb65a-77f9-4d42-9c6d-75e9b3452216",
  "isSidechain": true,
  "agentId": "a20fa24a4723e1d9c",
  "requestId": "req_011CbLmLUJXjXZqwtFtUuBF9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a95a614-4f99-481d-bc0d-a690b4e138f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "8eaa3b36-4b2e-4596-a917-3c8550c7e172",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011BeJc6FWwXw7FrSvx64tMX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 480,
      "cache_read_input_tokens": 16118,
      "output_tokens": 268,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 480
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 268,
          "cache_read_input_tokens": 16118,
          "cache_creation_input_tokens": 480,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 480,
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

_source line 9 · 2026-05-24T04:30:19.864Z_

<details><summary>↩ Tool result · `toolu_01DSbcR5QXSfUTh9jBRsArxe`</summary>

```text
Total experiments: 256

All experiment IDs:
  adaptive_1_7b_planb_control
  adaptive_1_7b_seed123
  adaptive_1_7b_seed42
  adaptive_1_7b_seed42_r2
  adaptive_1_7b_seed42_v3
  adaptive_1_7b_seed42_v4
  adaptive_1_7b_seed42_v5
  adaptive_1_7b_seed456
  adaptive_fix_seed123
  adaptive_fix_seed42
  adaptive_fix_seed456
  adaptive_fromscratch_seed42
  adaptive_ood_seed123
  adaptive_ood_seed456
  adaptive_rho06_tau07_seed123
  adaptive_rho06_tau07_seed42
  adaptive_rho06_tau07_seed456
  adaptive_seed123
  adaptive_seed42
  adaptive_seed456
  adaptive_tau08_scratch_seed42
  adaptive_tau08_scratch_seed42_v2
  adaptive_tau08_scratch_seed42_v3
  adaptive_v2_seed123
  adaptive_v2_seed42
  adaptive_v2_seed456
  aeff_only_nmin1_seed123
  aeff_only_nmin1_seed42
  aeff_only_nmin1_seed456
  baseline_qwen3_0.6b
  batch_adaptive_tau_rho04_seed42
  batch_adaptive_tau_rho06_r2
  batch_adaptive_tau_rho06_r3
  batch_adaptive_tau_rho06_r5
  batch_adaptive_tau_rho06_seed42
  batchsize16_nmin8_r2
  batchsize16_nmin8_r3
  batchsize16_nmin8_seed42
  bs16_adaptive_tau07_seed123
  bs16_adaptive_tau07_seed123_r2
  bs16_adaptive_tau07_seed42
  bs16_adaptive_tau07_seed456
  bs16_uniform_seed123
  bs16_uniform_seed42
  bs16_uniform_seed456
  bs8_auto_nmin_r2
  bs8_auto_nmin_r3
  bs8_auto_nmin_r5
  bs8_auto_nmin_seed42
  bs8_nmin2_seed42
  bs8_nmin2_seed42_r2
  bs8_nmin4_adaptive_seed123
  bs8_nmin4_adaptive_seed123_r2
  bs8_nmin4_adaptive_seed42
  bs8_nmin4_adaptive_seed456
  bs8_nmin4_adaptive_seed456_r2
  bs8_nmin4_uniform_seed123
  bs8_nmin4_uniform_seed123_r2
  bs8_nmin4_uniform_seed42
  bs8_nmin4_uniform_seed456
  bs8_nmin4_uniform_seed456_r2
  bs8_seed42
  contamination_60_adaptive_seed123_tau08
  contamination_60_adaptive_seed42_tau08
  contamination_60_adaptive_seed456
  contamination_60_ess_only_seed123
  contamination_60_ess_only_seed42
  contamination_60_ess_only_seed456
  contamination_60_grid_b0_3_seed42
  contamination_60_grid_b0_5_seed42
  contamination_60_random_seed123
  contamination_60_random_seed42
  contamination_60_random_seed456
  contamination_60_seed123
  contamination_60_seed42
  contamination_60_seed42_r2
  contamination_60_tau06_seed42
  contamination_60_tau07_seed42
  contamination_60_uniform_seed123
  contamination_60_uniform_seed42
  contamination_60_uniform_seed456
  datagen_synthetic_4gpu
  detect_remove_baseline_seed42
  detect_remove_q01_epoch_matched_seed42
  detect_remove_q01_seed42
  detect_remove_q02_seed42
  detect_remove_q03_epoch_matched_seed42
  detect_remove_q03_seed123
  detect_remove_q03_seed42
  detect_remove_q03_seed42_r2
  detect_remove_q03_seed456
  detect_remove_q04_seed42
  detect_remove_q05_epoch_matched
  detect_remove_q05_epoch_matched_seed42
  detect_remove_q05_seed123
  detect_remove_q05_seed42
  detect_remove_q05_seed456
  detect_remove_q05_v2_seed123
  detect_remove_q05_v2_seed123_r2
  detect_remove_q05_v2_seed42
  detect_remove_q05_v2_seed456
  detect_remove_q06_seed42
  detect_remove_q07_epoch_matched_seed42
  detect_remove_q07_seed42
  detect_remove_q07_seed42_r2
  detect_remove_q08_seed42
  detect_remove_q09_epoch_matched_seed42
  detect_remove_q09_seed42
  detector_modernbert
  detector_tfidf_lr
  diagnostic_contamination100
  dr_epoch_matched_indep_lr_seed42
  dr_epoch_matched_indep_lr_v2_seed42
  dr_epoch_matched_seed123
  dr_epoch_matched_seed123_r2
  dr_epoch_matched_seed456
  env_probe_41312
  env_probe_41312_v2
  epoch_matched_dr_seed123
  epoch_matched_dr_seed456
  ess_only_seed123
  ess_only_seed123_r2
  ess_only_seed42
  ess_only_seed456
  ess_only_seed456_r2
  eval_adaptive_1_7b
  eval_adaptive_1_7b_seed123
  eval_adaptive_1_7b_v2
  eval_epoch_matched_seed123
  eval_epoch_matched_seed456
  eval_ngram_adaptive
  eval_ngram_uniform
  eval_q01_final
  eval_q01_final_v2
  eval_q03_r2
  eval_q04
  eval_q06
  eval_q07_final
  eval_rho06_batch_v5
  eval_rho06_batch_v6
  eval_rho06_batch_v7
  eval_uniform_1_7b_resumed
  eval_uniform_1_7b_seed123
  eval_uniform_1_7b_v2
  eval_uniform_1_7b_v3
  golden_ratio_seed42
  gpt2_adaptive_seed123
  gpt2_adaptive_seed123_v2
  gpt2_adaptive_seed123_v3
  gpt2_adaptive_seed42
  gpt2_adaptive_seed456
  gpt2_adaptive_seed456_v2
  gpt2_uniform_seed42
  grid_b0_1_seed123
  grid_b0_1_seed42
  grid_b0_1_seed456
  grid_b0_2_seed123
  grid_b0_2_seed42
  grid_b0_2_seed456
  grid_b0_3_seed123
  grid_b0_3_seed123_r2
  grid_b0_3_seed42
  grid_b0_3_seed456
  grid_b0_3_seed456_r2
  grid_b0_5_seed123
  grid_b0_5_seed456
  grid_b1_0_seed123
  grid_b1_0_seed456
  grid_b1_5_seed123
  grid_b1_5_seed456
  grid_b2_0_seed123
  grid_b2_0_seed456
  grid_b3_0_seed123
  grid_b3_0_seed456
  grid_b5_0_seed123
  grid_b5_0_seed456
  grid_b_low_seed42
  grid_b_low_seed42_r2
  grid_b_low_seed42_r3
  grid_b_low_serial_seed42
  grid_b_seed42_batch
  hybrid_rho04_seed42
  hybrid_rho06_seed42
  llama3b_adaptive_seed42
  llama3b_uniform_seed42
  ngram_adaptive_seed123
  ngram_adaptive_seed42
  ngram_adaptive_seed456
  ngram_adaptive_seed456_v2
  ngram_uniform_seed42
  nmin1_seed42
  nmin4_seed42
  nmin5_seed42
  p0_contamination_60_datagen
  qwen06b_uniform_seed42
  random_reweight_baseline_seed42
  random_reweight_seed123
  random_reweight_seed123_r2
  random_reweight_seed123_r3
  random_reweight_seed123_r4
  random_reweight_seed123_r5
  random_reweight_seed42
  random_reweight_seed456
  random_reweight_v2_seed42
  random_reweight_v2_seed456
  rho02_adaptive_tau08_seed42
  rho02_adaptive_tau09_r2
  rho02_adaptive_tau09_r3
  rho02_adaptive_tau09_r4
  rho02_adaptive_tau09_r5
  rho02_adaptive_tau09_seed42
  rho02_uniform_seed42
  rho03_adaptive_seed123
  rho03_adaptive_seed42
  rho03_adaptive_seed456
  rho03_adaptive_seed456_r2
  rho03_uniform_seed123
  rho03_uniform_seed42
  rho03_uniform_seed456
  rho06_tau07_seed123
  rho06_tau07_seed42
  rho06_tau07_seed456
  status_check_41312
  tau07_downstream_eval
  tau07_seed123
  tau07_seed42
  tau07_seed456
  tau_0.6_seed42
  tau_05_nmin2_seed42
  tau_05_seed42
  tau_06_nmin2_seed42
  tau_06_seed42
  tau_07_nmin2_seed42
  tau_07_seed42
  tau_095_nmin2_seed42
  tau_095_seed42
  tau_09_nmin2_seed42
  tau_09_seed42
  threshold_q03_seed42
  threshold_q07_seed42
  uniform_1_7b_seed123
  uniform_1_7b_seed42
  uniform_1_7b_seed42_r2
  uniform_1_7b_seed42_v3
  uniform_1_7b_seed42_v4
  uniform_1_7b_seed42_v5
  uniform_1_7b_seed456
  uniform_epoch_matched_indep_lr_seed42
  uniform_epoch_matched_seed456
  uniform_ood_seed123
  uniform_ood_seed456
  uniform_seed123
  uniform_seed42
  uniform_seed42_downstream
  uniform_seed456
  w2_distribution_matching_eval
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a95a614-4f99-481d-bc0d-a690b4e138f8",
  "isSidechain": true,
  "promptId": "c0ee33d1-40a2-4cb8-a0f0-d28fa12f6711",
  "agentId": "a20fa24a4723e1d9c",
  "type": "user",
  "uuid": "72e011c5-4199-4e22-ad88-06a36823263b",
  "sourceToolAssistantUUID": "9a95a614-4f99-481d-bc0d-a690b4e138f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "8eaa3b36-4b2e-4596-a917-3c8550c7e172",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-24T04:30:27.365Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01ScLt1M2nFac3GLQdmAJMCU`</summary>

```json
{
  "command": "python3 - <<'EOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/8eaa3b36-4b2e-4596-a917-3c8550c7e172/tool-results/mcp-agent-ml-research-read_registry-1779596942026.txt\"\n\nwith open(fpath) as f:\n    outer = json.load(f)\n\nregistry = json.loads(outer[\"result\"])\nexperiments = registry[\"data\"][\"experiments\"]\n\n# Inspect one experiment to understand metrics schema\nsample_id = \"adaptive_seed42\"\ne = experiments[sample_id]\nprint(f\"=== {sample_id} ===\")\nprint(json.dumps(e, indent=2))\nEOF\n",
  "description": "Inspect schema of one experiment with metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72e011c5-4199-4e22-ad88-06a36823263b",
  "isSidechain": true,
  "agentId": "a20fa24a4723e1d9c",
  "requestId": "req_011CbLmLjPPauEvMVSmFDPRS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b19fa05b-9322-4b60-810e-814a477a0e0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "8eaa3b36-4b2e-4596-a917-3c8550c7e172",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013aJbzD78aUn1EsYQpSTUtV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3161,
      "cache_read_input_tokens": 16598,
      "output_tokens": 284,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3161
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 284,
          "cache_read_input_tokens": 16598,
          "cache_creation_input_tokens": 3161,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3161,
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

_source line 11 · 2026-05-24T04:30:27.487Z_

<details><summary>↩ Tool result · `toolu_01ScLt1M2nFac3GLQdmAJMCU`</summary>

```text
=== adaptive_seed42 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-14T02:25:01.824Z",
  "updated_at": "2026-05-15T16:43:05.333Z",
  "hypothesis": "Adaptive b* (from \u03b1_eff theory) matches or exceeds grid-searched best-b without grid search, seed=42",
  "spec": {
    "command": "python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4",
    "server": "westd-47453",
    "gpu": [
      "cuda:1"
    ],
    "pid": "58888",
    "log_path": "~/runs/provenance_weight_training/adaptive_seed42.log",
    "submitted_at": "2026-05-14T02:46:23.000Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "data/scored_data.jsonl",
    "data_count": 371499,
    "model_name": "Qwen/Qwen3-0.6B",
    "seed": 42,
    "checkpoint_path": "output/models/adaptive_seed42/final",
    "wall_clock_seconds": 15162.9,
    "gpu_hours": 4.21
  },
  "metrics": {
    "train_loss": 9.2665,
    "train_runtime_s": 13115.09,
    "total_steps": 6103,
    "train_samples_per_second": 7.445,
    "train_steps_per_second": 0.465,
    "epoch": 0.26,
    "weighting_method": "adaptive",
    "tau": 0.8,
    "n_min": 3,
    "contamination_ratio": 0.4,
    "b_star": "per-batch adaptive (0.0-3.8)",
    "alpha_eff_range": "0.03-0.80 (capped at tau)",
    "eval_ppl_holdout": 17.644,
    "eval_loss_holdout": 2.8704,
    "eval_holdout_tokens": 4077068,
    "eval_method": "eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)",
    "eval_note": "unified post-hoc eval 2026-05-15; confirmed unchanged from prior post-hoc (was 17.644/4077068)"
  },
  "conclusion": "success",
  "completed_at": "2026-05-14T06:59:05.861Z",
  "notes": "\u26a0\ufe0f success \u4ec5\u6307\u8bad\u7ec3\u5b8c\u6210\u65e0\u62a5\u9519\u3002MVP \u5047\u8bbe\u9a8c\u8bc1\u5f85 held-out eval perplexity \u7ed3\u679c\u3002"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b19fa05b-9322-4b60-810e-814a477a0e0c",
  "isSidechain": true,
  "promptId": "c0ee33d1-40a2-4cb8-a0f0-d28fa12f6711",
  "agentId": "a20fa24a4723e1d9c",
  "type": "user",
  "uuid": "e9c4c743-6a86-4a82-9177-188d3dd33b08",
  "sourceToolAssistantUUID": "b19fa05b-9322-4b60-810e-814a477a0e0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "8eaa3b36-4b2e-4596-a917-3c8550c7e172",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-24T04:30:35.499Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01EdzKHHX8pQ2zoCxZKnTTmK`</summary>

```json
{
  "command": "python3 - <<'EOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/8eaa3b36-4b2e-4596-a917-3c8550c7e172/tool-results/mcp-agent-ml-research-read_registry-1779596942026.txt\"\n\nwith open(fpath) as f:\n    outer = json.load(f)\n\nregistry = json.loads(outer[\"result\"])\nexperiments = registry[\"data\"][\"experiments\"]\n\n# Check what metrics fields exist across all experiments\nall_metric_keys = set()\nfor eid, e in experiments.items():\n    m = e.get(\"metrics\", {})\n    if m:\n        all_metric_keys.update(m.keys())\n\nprint(\"All metric keys found across experiments:\")\nfor k in sorted(all_metric_keys):\n    print(\" \", k)\nEOF\n",
  "description": "Discover all metric key names across all experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9c4c743-6a86-4a82-9177-188d3dd33b08",
  "isSidechain": true,
  "agentId": "a20fa24a4723e1d9c",
  "requestId": "req_011CbLmMJ2Bh6M9rgocTN7gP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c48dbf0-0e59-4859-b482-a196ba85fb0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "8eaa3b36-4b2e-4596-a917-3c8550c7e172",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BNxJJdoTKGpFZRre5k59M9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1251,
      "cache_read_input_tokens": 19759,
      "output_tokens": 317,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1251
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 317,
          "cache_read_input_tokens": 19759,
          "cache_creation_input_tokens": 1251,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1251,
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

_source line 13 · 2026-05-24T04:30:35.591Z_

<details><summary>↩ Tool result · `toolu_01EdzKHHX8pQ2zoCxZKnTTmK`</summary>

```text
All metric keys found across experiments:
  accuracy
  actual_contamination_ratio
  all_completed
  alpha_eff_mean
  alpha_eff_median
  alpha_eff_pct_at_max
  alpha_eff_range
  alpha_eff_typical_range
  auc
  b0_5_completed
  b0_5_eval_ppl
  b0_5_runtime_s
  b0_5_train_loss
  b1_0_completed
  b1_0_eval_ppl
  b1_0_runtime_s
  b1_0_train_loss
  b1_5_completed
  b1_5_eval_ppl
  b1_5_runtime_s
  b1_5_train_loss
  b2_0_completed
  b2_0_current_step
  b2_0_eval_ppl
  b2_0_runtime_s
  b2_0_total_steps
  b2_0_train_loss
  b2_0_train_runtime_s
  b3_0_completed
  b3_0_eval_ppl
  b3_0_runtime_s
  b3_0_train_loss
  b3_0_train_runtime_s
  b5_0_eval_ppl
  b5_0_progress_pct
  b5_0_runtime_s
  b5_0_train_loss
  b_fixed
  b_star
  b_star_count
  b_star_max
  b_star_mean
  b_star_median
  b_star_min
  b_star_nonzero_mean
  b_star_nonzero_median
  b_star_note
  b_star_p25
  b_star_p75
  b_star_p90
  b_star_pct_0.5_to_1
  b_star_pct_1_to_2
  b_star_pct_2_to_5
  b_star_pct_above_2
  b_star_pct_above_5
  b_star_pct_below_0.5
  b_star_pct_zero
  b_star_std
  b_star_zero_frac
  b_values
  batch_size
  best_b
  best_eval_ppl
  checkpoint
  checkpoint_1500_ppl
  completed_b_values
  conclusion_note
  contamination_60_ess_only_seed123
  contamination_60_ess_only_seed456
  contamination_60_random_seed123
  contamination_60_random_seed456
  contamination_ratio
  current_b
  current_step
  data_count
  downstream_arc_challenge_acc_norm
  downstream_arc_easy_acc_norm
  downstream_eval_method
  downstream_hellaswag_acc_norm
  downstream_mean
  downstream_piqa_acc_norm
  downstream_winogrande_acc
  ece_calibrated
  ece_raw
  elapsed_seconds
  epoch
  error
  error_stage
  ess_max
  ess_mean
  ess_median
  ess_min
  ess_typical_range
  eta_minutes
  eval_checkpoint
  eval_data
  eval_docs
  eval_holdout_tokens
  eval_loss
  eval_loss_holdout
  eval_method
  eval_note
  eval_owt_tokens
  eval_ppl
  eval_ppl_holdout
  eval_ppl_openwebtext
  eval_ppl_owt
  eval_ppl_wiki
  eval_ppl_wikipedia
  eval_ppl_wikitext
  eval_results_path
  eval_source
  eval_tokens
  eval_wiki_tokens
  file_size_mb
  gpu_hours
  holdout_loss
  holdout_ppl
  human_count
  interpretation
  loss
  max_docs
  max_length
  mid_range_ratio
  n_min
  note
  num_eval_tokens
  num_tokens
  ood_eval_source
  ood_note
  ood_owt_loss
  ood_owt_ppl
  ood_wiki_loss
  ood_wiki_ppl
  owt_loss
  owt_ppl
  perplexity
  ppl
  q_score_mean
  q_score_median
  q_score_std
  re_eval_date
  re_eval_note
  rho
  synthetic_count
  tau
  temperature_T
  tokens
  total_lines
  total_steps
  train_duration_s
  train_loss
  train_loss_final
  train_loss_last500
  train_loss_weighted
  train_runtime
  train_runtime_hours
  train_runtime_s
  train_runtime_sec
  train_runtime_seconds
  train_samples_per_second
  train_steps
  train_steps_per_second
  training_completed
  training_time_s
  vs_adaptive
  vs_adaptive_bs4
  vs_adaptive_fix_ppl_delta
  vs_adaptive_fix_seed123
  vs_adaptive_fixed_tau08_rho06
  vs_adaptive_ppl_delta
  vs_bs8_nmin4
  vs_full_dr_q05
  vs_grid_b03_seed42
  vs_grid_b05_seed456
  vs_grid_best_rho06
  vs_hybrid_rho06
  vs_random_reweight_v2_seed42
  vs_rho02_uniform
  vs_rho04_uniform
  vs_uniform
  vs_uniform_ppl_delta
  vs_uniform_rho06
  vs_uniform_seed123
  weighting_method
  wiki_loss
  wiki_ppl
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c48dbf0-0e59-4859-b482-a196ba85fb0c",
  "isSidechain": true,
  "promptId": "c0ee33d1-40a2-4cb8-a0f0-d28fa12f6711",
  "agentId": "a20fa24a4723e1d9c",
  "type": "user",
  "uuid": "ebd770db-c3a4-404d-888c-32f94e3c1f2b",
  "sourceToolAssistantUUID": "3c48dbf0-0e59-4859-b482-a196ba85fb0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "8eaa3b36-4b2e-4596-a917-3c8550c7e172",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-24T04:31:01.441Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01EtRbzVgfVtK3Mam8ZwKK6b`</summary>

```json
{
  "command": "python3 - <<'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/8eaa3b36-4b2e-4596-a917-3c8550c7e172/tool-results/mcp-agent-ml-research-read_registry-1779596942026.txt\"\n\nwith open(fpath) as f:\n    outer = json.load(f)\n\nregistry = json.loads(outer[\"result\"])\nexperiments = registry[\"data\"][\"experiments\"]\n\n# Key metrics to extract\nKEY_METRICS = [\n    \"eval_ppl_holdout\", \"eval_ppl\", \"ppl\", \"holdout_ppl\", \"perplexity\",\n    \"eval_ppl_openwebtext\", \"eval_ppl_owt\", \"eval_ppl_wiki\", \"eval_ppl_wikipedia\", \"eval_ppl_wikitext\",\n    \"ood_owt_ppl\", \"ood_wiki_ppl\",\n    \"train_loss\", \"eval_loss_holdout\", \"eval_loss\",\n    \"weighting_method\", \"tau\", \"n_min\", \"rho\", \"b_star\", \"b_fixed\",\n    \"contamination_ratio\",\n    \"vs_uniform\", \"vs_adaptive\", \"vs_adaptive_ppl_delta\", \"vs_uniform_ppl_delta\",\n    \"epoch\", \"total_steps\", \"train_runtime_s\",\n    # comparison / delta metrics\n    \"vs_grid_b03_seed42\", \"vs_rho02_uniform\", \"vs_rho04_uniform\", \"vs_grid_b05_seed456\",\n    \"downstream_arc_challenge_acc_norm\", \"downstream_arc_easy_acc_norm\",\n    \"downstream_hellaswag_acc_norm\", \"downstream_mean\", \"downstream_piqa_acc_norm\", \"downstream_winogrande_acc\",\n]\n\ndef fmt_metrics(m):\n    out = {}\n    for k in KEY_METRICS:\n        if k in m:\n            out[k] = m[k]\n    # Also include any key containing \"p-value\" or \"delta\" or \"std\" or \"ppl\"\n    for k, v in m.items():\n        if any(tok in k for tok in [\"p_value\", \"pvalue\", \"delta\", \"std\", \"ppl\", \"p-value\"]) and k not in out:\n            out[k] = v\n    return out\n\n# Group experiments by category\nGROUPS = {\n    \"adaptive_bstar_main\": [],\n    \"adaptive_bstar_1_7b\": [],\n    \"uniform_main\": [],\n    \"uniform_1_7b\": [],\n    \"grid_search_b\": [],\n    \"ess_only\": [],\n    \"aeff_only\": [],\n    \"random_reweight\": [],\n    \"detect_remove\": [],\n    \"batch_size_bs8\": [],\n    \"batch_size_bs16\": [],\n    \"rho_variants\": [],\n    \"tau_sensitivity\": [],\n    \"nmin_sensitivity\": [],\n    \"ood_eval\": [],\n    \"ngram_detector\": [],\n    \"gpt2_detector\": [],\n    \"contamination_60\": [],\n    \"epoch_matched\": [],\n    \"downstream_eval\": [],\n    \"other\": [],\n}\n\ndef categorize(eid, e):\n    cats = []\n    # 1.7B scale\n    if \"1_7b\" in eid:\n        if \"adaptive\" in eid: cats.append(\"adaptive_bstar_1_7b\")\n        elif \"uniform\" in eid: cats.append(\"uniform_1_7b\")\n        else: cats.append(\"adaptive_bstar_1_7b\")\n    # grid search\n    elif eid.startswith(\"grid_\"):\n        cats.append(\"grid_search_b\")\n    # ess_only\n    elif eid.startswith(\"ess_only\") or eid.startswith(\"aeff_only\"):\n        if \"aeff_only\" in eid: cats.append(\"aeff_only\")\n        else: cats.append(\"ess_only\")\n    # random reweight\n    elif \"random_reweight\" in eid:\n        cats.append(\"random_reweight\")\n    # detect & remove\n    elif \"detect_remove\" in eid or eid.startswith(\"dr_epoch\"):\n        cats.append(\"detect_remove\")\n    # batch size\n    elif eid.startswith(\"bs16_\") or \"batchsize16\" in eid:\n        cats.append(\"batch_size_bs16\")\n    elif eid.startswith(\"bs8_\") or \"batch_adaptive\" in eid or \"batch_bs8\" in eid:\n        cats.append(\"batch_size_bs8\")\n    # rho variants\n    elif eid.startswith(\"rho0\") or eid.startswith(\"hybrid_rho\"):\n        cats.append(\"rho_variants\")\n    # tau sensitivity\n    elif eid.startswith(\"tau_\") or \"tau0\" in eid:\n        cats.append(\"tau_sensitivity\")\n    # nmin sensitivity\n    elif eid.startswith(\"nmin\"):\n        cats.append(\"nmin_sensitivity\")\n    # OOD\n    elif \"ood\" in eid:\n        cats.append(\"ood_eval\")\n    # ngram detector\n    elif \"ngram\" in eid:\n        cats.append(\"ngram_detector\")\n    # gpt2 detector\n    elif \"gpt2\" in eid:\n        cats.append(\"gpt2_detector\")\n    # contamination_60\n    elif \"contamination_60\" in eid:\n        cats.append(\"contamination_60\")\n    # epoch_matched\n    elif \"epoch_matched\" in eid:\n        cats.append(\"epoch_matched\")\n    # downstream eval\n    elif eid.startswith(\"eval_\") or \"downstream\" in eid:\n        cats.append(\"downstream_eval\")\n    # adaptive main\n    elif \"adaptive\" in eid:\n        cats.append(\"adaptive_bstar_main\")\n    # uniform main\n    elif \"uniform\" in eid:\n        cats.append(\"uniform_main\")\n    else:\n        cats.append(\"other\")\n    return cats\n\nfor eid, e in sorted(experiments.items()):\n    cats = categorize(eid, e)\n    row = {\n        \"id\": eid,\n        \"status\": e.get(\"status\"),\n        \"conclusion\": e.get(\"conclusion\"),\n        \"metrics\": fmt_metrics(e.get(\"metrics\", {})),\n        \"notes\": e.get(\"notes\", \"\")[:200] if e.get(\"notes\") else \"\",\n    }\n    for cat in cats:\n        if cat in GROUPS:\n            GROUPS[cat].append(row)\n        else:\n            GROUPS[\"other\"].append(row)\n\n# Print all groups\nfor grp, rows in GROUPS.items():\n    if not rows:\n        continue\n    print(f\"\\n{'='*70}\")\n    print(f\"GROUP: {grp}  ({len(rows)} experiments)\")\n    print('='*70)\n    for row in rows:\n        print(f\"\\n  [{row['id']}] status={row['status']} conclusion={row['conclusion']}\")\n        m = row[\"metrics\"]\n        if m:\n            for k, v in m.items():\n                print(f\"    {k}: {v}\")\n        else:\n            print(\"    (no metrics)\")\n        if row[\"notes\"]:\n            print(f\"    notes: {row['notes']}\")\nPYEOF\n",
  "description": "Extract all experiments with metrics grouped by category"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebd770db-c3a4-404d-888c-32f94e3c1f2b",
  "isSidechain": true,
  "agentId": "a20fa24a4723e1d9c",
  "requestId": "req_011CbLmMtdnRrLge6iN6sbCV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ce2455d5-fcd3-45a4-9024-6b2d2b751491",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "8eaa3b36-4b2e-4596-a917-3c8550c7e172",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KwiuW49EqbdzKb8htqnoa7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1794,
      "cache_read_input_tokens": 21010,
      "output_tokens": 1940,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1794
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1940,
          "cache_read_input_tokens": 21010,
          "cache_creation_input_tokens": 1794,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1794,
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

_source line 15 · 2026-05-24T04:31:01.549Z_

<details><summary>↩ Tool result · `toolu_01EtRbzVgfVtK3Mam8ZwKK6b`</summary>

```text
&lt;persisted-output>
Output too large (52.2KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/8eaa3b36-4b2e-4596-a917-3c8550c7e172/tool-results/bfvz4i8e3.txt

Preview (first 2KB):
======================================================================
GROUP: adaptive_bstar_main  (11 experiments)
======================================================================

  [adaptive_fix_seed123] status=DONE conclusion=success
    eval_ppl_holdout: 17.6432
    eval_loss_holdout: 2.8704
    eval_loss: 2.8704
    epoch: 0.26
    total_steps: 6103
    train_runtime_s: 10347
    b_star_std: 2.029
    notes: 最终清理后重提交。从 checkpoint-1500 恢复，无 inline eval。PID=126944

  [adaptive_fix_seed42] status=DONE conclusion=success
    eval_ppl_holdout: 17.6527
    eval_ppl_openwebtext: 18.424
    eval_ppl_wikipedia: 15.473
    downstream_arc_challenge_acc_norm: 0.343
    downstream_arc_easy_acc_norm: 0.6157
    downstream_hellaswag_acc_norm: 0.4785
    downstream_mean: 0.5403
    downstream_piqa_acc_norm: 0.6866
    downstream_winogrande_acc: 0.5777
    notes: 最终清理后重提交。从 checkpoint-1500 恢复，无 inline eval。PID=126801

  [adaptive_fix_seed456] status=DONE conclusion=success
    eval_ppl_holdout: 17.6566
    train_loss: 8.3124
    eval_loss_holdout: 2.8711
    total_steps: 6103
    b_star_std: 1.993
    notes: 最终清理后重提交。从 checkpoint-1000 恢复，无 inline eval。PID=127285

  [adaptive_fromscratch_seed42] status=DONE conclusion=success
    eval_ppl_holdout: 17.689
    eval_ppl_openwebtext: 18.37
    eval_ppl_wikipedia: 15.349
    train_loss: 9.976
    downstream_arc_challenge_acc_norm: 0.3524
    downstream_arc_easy_acc_norm: 0.6178
    downstream_hellaswag_acc_norm: 0.4806
    downstream_piqa_acc_norm: 0.6844
    downstream_winogrande_acc: 0.5801

  [adaptive_seed123] status=DONE conclusion=success
    eval_ppl_holdout: 17.6308
    train_loss: 9.2665
    eval_loss_holdout: 2.8696
    weighting_method: adaptive
    tau: 0.8
    n_min: 3
    b_star: per-batch adaptive (0.0-3.8)
    contamination_ratio: 0.4
    epoch: 0.26
    total_steps: 6103
    train_runtime_s: 13197.18
    notes: ⚠️ success 仅指训练完成无报错。MVP 假设验证待 held-out eval perplexity 结果。

...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce2455d5-fcd3-45a4-9024-6b2d2b751491",
  "isSidechain": true,
  "promptId": "c0ee33d1-40a2-4cb8-a0f0-d28fa12f6711",
  "agentId": "a20fa24a4723e1d9c",
  "type": "user",
  "uuid": "19fe8be7-9b7c-4c03-9b2e-52bf80813ee9",
  "sourceToolAssistantUUID": "ce2455d5-fcd3-45a4-9024-6b2d2b751491",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "8eaa3b36-4b2e-4596-a917-3c8550c7e172",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-24T04:31:04.993Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MfuUjVSmrFCXX3Wm7KtB5U`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/8eaa3b36-4b2e-4596-a917-3c8550c7e172/tool-results/bfvz4i8e3.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19fe8be7-9b7c-4c03-9b2e-52bf80813ee9",
  "isSidechain": true,
  "agentId": "a20fa24a4723e1d9c",
  "requestId": "req_011CbLmPodxpDFZYv7fssR54",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d2c4bd7c-e61a-4e97-a84c-cf0ff1557937",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "8eaa3b36-4b2e-4596-a917-3c8550c7e172",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NiEKrRGgBDPqRu6sTkD5m5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2864,
      "cache_read_input_tokens": 22804,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2864
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 135,
          "cache_read_input_tokens": 22804,
          "cache_creation_input_tokens": 2864,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2864,
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

_source line 17 · 2026-05-24T04:31:05.275Z_

<details><summary>↩ Tool result · `toolu_01MfuUjVSmrFCXX3Wm7KtB5U`</summary>

```text
1	
2	======================================================================
3	GROUP: adaptive_bstar_main  (11 experiments)
4	======================================================================
5	
6	  [adaptive_fix_seed123] status=DONE conclusion=success
7	    eval_ppl_holdout: 17.6432
8	    eval_loss_holdout: 2.8704
9	    eval_loss: 2.8704
10	    epoch: 0.26
11	    total_steps: 6103
12	    train_runtime_s: 10347
13	    b_star_std: 2.029
14	    notes: 最终清理后重提交。从 checkpoint-1500 恢复，无 inline eval。PID=126944
15	
16	  [adaptive_fix_seed42] status=DONE conclusion=success
17	    eval_ppl_holdout: 17.6527
18	    eval_ppl_openwebtext: 18.424
19	    eval_ppl_wikipedia: 15.473
20	    downstream_arc_challenge_acc_norm: 0.343
21	    downstream_arc_easy_acc_norm: 0.6157
22	    downstream_hellaswag_acc_norm: 0.4785
23	    downstream_mean: 0.5403
24	    downstream_piqa_acc_norm: 0.6866
25	    downstream_winogrande_acc: 0.5777
26	    notes: 最终清理后重提交。从 checkpoint-1500 恢复，无 inline eval。PID=126801
27	
28	  [adaptive_fix_seed456] status=DONE conclusion=success
29	    eval_ppl_holdout: 17.6566
30	    train_loss: 8.3124
31	    eval_loss_holdout: 2.8711
32	    total_steps: 6103
33	    b_star_std: 1.993
34	    notes: 最终清理后重提交。从 checkpoint-1000 恢复，无 inline eval。PID=127285
35	
36	  [adaptive_fromscratch_seed42] status=DONE conclusion=success
37	    eval_ppl_holdout: 17.689
38	    eval_ppl_openwebtext: 18.37
39	    eval_ppl_wikipedia: 15.349
40	    train_loss: 9.976
41	    downstream_arc_challenge_acc_norm: 0.3524
42	    downstream_arc_easy_acc_norm: 0.6178
43	    downstream_hellaswag_acc_norm: 0.4806
44	    downstream_piqa_acc_norm: 0.6844
45	    downstream_winogrande_acc: 0.5801
46	
47	  [adaptive_seed123] status=DONE conclusion=success
48	    eval_ppl_holdout: 17.6308
49	    train_loss: 9.2665
50	    eval_loss_holdout: 2.8696
51	    weighting_method: adaptive
52	    tau: 0.8
53	    n_min: 3
54	    b_star: per-batch adaptive (0.0-3.8)
55	    contamination_ratio: 0.4
56	    epoch: 0.26
57	    total_steps: 6103
58	    train_runtime_s: 13197.18
59	    notes: ⚠️ success 仅指训练完成无报错。MVP 假设验证待 held-out eval perplexity 结果。
60	
61	  [adaptive_seed42] status=DONE conclusion=success
62	    eval_ppl_holdout: 17.644
63	    train_loss: 9.2665
64	    eval_loss_holdout: 2.8704
65	    weighting_method: adaptive
66	    tau: 0.8
67	    n_min: 3
68	    b_star: per-batch adaptive (0.0-3.8)
69	    contamination_ratio: 0.4
70	    epoch: 0.26
71	    total_steps: 6103
72	    train_runtime_s: 13115.09
73	    notes: ⚠️ success 仅指训练完成无报错。MVP 假设验证待 held-out eval perplexity 结果。
74	
75	  [adaptive_seed456] status=DONE conclusion=success
76	    eval_ppl_holdout: 17.6419
77	    train_loss: 9.2354
78	    eval_loss_holdout: 2.8703
79	    weighting_method: adaptive
80	    tau: 0.8
81	    n_min: 3
82	    b_star: per-batch adaptive (0.0-3.8)
83	    contamination_ratio: 0.4
84	    epoch: 0.26
85	    total_steps: 6103
86	    train_runtime_s: 13130.09
87	    notes: ⚠️ success 仅指训练完成无报错。MVP 假设验证待 held-out eval perplexity 结果。
88	
89	  [adaptive_v2_seed123] status=DONE conclusion=killed
90	    (no metrics)
91	    notes: D012 修正：取消 v2（含 EMA），改用 adaptive_fix（仅修 n_min=2，无 EMA）
92	
93	  [adaptive_v2_seed42] status=DONE conclusion=killed
94	    (no metrics)
95	    notes: D012 修正：取消 v2（含 EMA），改用 adaptive_fix（仅修 n_min=2，无 EMA）
96	
97	  [adaptive_v2_seed456] status=DONE conclusion=killed
98	    (no metrics)
99	    notes: D012 修正：取消 v2（含 EMA），改用 adaptive_fix（仅修 n_min=2，无 EMA）
100	
101	  [llama3b_adaptive_seed42] status=DONE conclusion=negative
102	    ppl: 10.58
103	    eval_loss: 2.359
104	    notes: 诊断中: cron 报 process dead 5× + no W&B，但 memory.md 有 PPL=10.58 结论。疑似训练完成但监控缺失。Worker worker_diagnose_llama3b_adaptive_seed42_20260517T140045 正在 SSH 确认。日志文件 /root/runs/provenance_weight_training/llama3b_
105	
106	======================================================================
107	GROUP: adaptive_bstar_1_7b  (11 experiments)
108	======================================================================
109	
110	  [adaptive_1_7b_planb_control] status=PREPARING conclusion=None
111	    (no metrics)
112	
113	  [adaptive_1_7b_seed123] status=DONE conclusion=success
114	    eval_ppl_holdout: 13.25
115	    eval_ppl_openwebtext: 13.2909
116	    eval_ppl_wikipedia: 10.9521
117	    eval_loss_holdout: 2.5843
118	    downstream_arc_challenge_acc_norm: 0.4386
119	    downstream_arc_easy_acc_norm: 0.7138
120	    downstream_hellaswag_acc_norm: 0.6147
121	    downstream_mean: 0.6286
122	    downstream_piqa_acc_norm: 0.7459
123	    downstream_winogrande_acc: 0.6298
124	
125	  [adaptive_1_7b_seed42] status=DONE conclusion=success
126	    (no metrics)
127	
128	  [adaptive_1_7b_seed42_r2] status=PREPARING conclusion=None
129	    (no metrics)
130	
131	  [adaptive_1_7b_seed42_v3] status=DONE conclusion=killed
132	    (no metrics)
133	
134	  [adaptive_1_7b_seed42_v4] status=DONE conclusion=failed
135	    (no metrics)
136	
137	  [adaptive_1_7b_seed42_v5] status=DONE conclusion=success
138	    eval_ppl_holdout: 13.27
139	    eval_ppl_openwebtext: 13.282
140	    eval_ppl_wikipedia: 10.955
141	    train_loss: 9.139
142	    total_steps: 6103
143	    train_runtime_s: 18540
144	    downstream_arc_challenge_acc_norm: 0.4403
145	    downstream_arc_easy_acc_norm: 0.7176
146	    downstream_hellaswag_acc_norm: 0.6164
147	    downstream_mean: 0.6251
148	    downstream_piqa_acc_norm: 0.7443
149	    downstream_winogrande_acc: 0.6069
150	
151	  [adaptive_1_7b_seed456] status=DONE conclusion=success
152	    eval_ppl_holdout: 13.2668
153	    eval_ppl_openwebtext: 13.292
154	    eval_ppl_wikipedia: 10.947
155	    downstream_arc_challenge_acc_norm: 0.4352
156	    downstream_arc_easy_acc_norm: 0.7146
157	    downstream_hellaswag_acc_norm: 0.6133
158	    downstream_mean: 0.6259
159	    downstream_piqa_acc_norm: 0.7443
160	    downstream_winogrande_acc: 0.6219
161	
162	  [eval_adaptive_1_7b] status=PREPARING conclusion=None
163	    (no metrics)
164	
165	  [eval_adaptive_1_7b_seed123] status=PREPARING conclusion=None
166	    (no metrics)
167	
168	  [eval_adaptive_1_7b_v2] status=DONE conclusion=success
169	    eval_ppl_holdout: 13.27
170	
171	======================================================================
172	GROUP: uniform_main  (5 experiments)
173	======================================================================
174	
175	  [llama3b_uniform_seed42] status=DONE conclusion=success
176	    ppl: 10.38
177	    train_loss: 7.2987
178	    eval_loss: 2.3397
179	
180	  [qwen06b_uniform_seed42] status=DONE conclusion=success
181	    eval_ppl_holdout: 17.69
182	    eval_ppl_openwebtext: 18.365
183	    eval_ppl_wikipedia: 15.335
184	    train_loss: 1.9882
185	    eval_loss_holdout: 2.8733
186	    downstream_arc_challenge_acc_norm: 0.3481
187	    downstream_arc_easy_acc_norm: 0.6128
188	    downstream_hellaswag_acc_norm: 0.4836
189	    downstream_piqa_acc_norm: 0.6877
190	    downstream_winogrande_acc: 0.5856
191	
192	  [uniform_seed123] status=DONE conclusion=success
193	    eval_ppl_holdout: 17.6861
194	    train_loss: 7.3121
195	    eval_loss_holdout: 2.8728
196	    total_steps: 6103
197	
198	  [uniform_seed42] status=DONE conclusion=success
199	    eval_ppl_holdout: 17.6939
200	    train_loss: 7.3104
201	    eval_loss_holdout: 2.8732
202	    total_steps: 6103
203	
204	  [uniform_seed456] status=DONE conclusion=success
205	    eval_ppl_holdout: 17.7015
206	    train_loss: 7.2895
207	    eval_loss_holdout: 2.8737
208	    total_steps: 6103
209	
210	======================================================================
211	GROUP: uniform_1_7b  (11 experiments)
212	======================================================================
213	
214	  [eval_uniform_1_7b_resumed] status=PREPARING conclusion=None
215	    (no metrics)
216	
217	  [eval_uniform_1_7b_seed123] status=PREPARING conclusion=None
218	    (no metrics)
219	
220	  [eval_uniform_1_7b_v2] status=PREPARING conclusion=None
221	    (no metrics)
222	
223	  [eval_uniform_1_7b_v3] status=DONE conclusion=success
224	    eval_ppl_holdout: 13.5
225	
226	  [uniform_1_7b_seed123] status=DONE conclusion=success
227	    eval_ppl_holdout: 13.2648
228	    eval_ppl_openwebtext: 13.2918
229	    eval_ppl_wikipedia: 10.942
230	    eval_loss_holdout: 2.5851
231	    total_steps: 6103
232	    downstream_arc_challenge_acc_norm: 0.4317
233	    downstream_arc_easy_acc_norm: 0.726
234	    downstream_hellaswag_acc_norm: 0.6118
235	    downstream_mean: 0.6256
236	    downstream_piqa_acc_norm: 0.7454
237	    downstream_winogrande_acc: 0.6133
238	
239	  [uniform_1_7b_seed42] status=DONE conclusion=failed
240	    (no metrics)
241	    notes: 失败原因: FileNotFoundError — checkpoint-3000/trainer_state.json 缺失，resume 崩溃 | 已有成果: checkpoint-3000 存在但不完整 | 建议: 找有效 checkpoint 重 resume 或从头训练
242	
243	  [uniform_1_7b_seed42_r2] status=PREPARING conclusion=None
244	    (no metrics)
245	
246	  [uniform_1_7b_seed42_v3] status=DONE conclusion=killed
247	    (no metrics)
248	
249	  [uniform_1_7b_seed42_v4] status=DONE conclusion=failed
250	    (no metrics)
251	
252	  [uniform_1_7b_seed42_v5] status=DONE conclusion=success
253	    eval_ppl_holdout: 13.28
254	    eval_ppl_openwebtext: 13.291
255	    eval_ppl_wikipedia: 10.919
256	    train_loss: 7.56
257	    total_steps: 6103
258	    train_runtime_s: 17630
259	    downstream_arc_challenge_acc_norm: 0.4334
260	    downstream_arc_easy_acc_norm: 0.7235
261	    downstream_hellaswag_acc_norm: 0.6107
262	    downstream_mean: 0.6256
263	    downstream_piqa_acc_norm: 0.7432
264	    downstream_winogrande_acc: 0.6172
265	
266	  [uniform_1_7b_seed456] status=DONE conclusion=success
267	    eval_ppl_holdout: 13.28
268	    eval_ppl_openwebtext: 13.307
269	    eval_ppl_wikipedia: 10.953
270	    eval_loss_holdout: 2.5863
271	    total_steps: 6103
272	    downstream_arc_challenge_acc_norm: 0.4224
273	    downstream_arc_easy_acc_norm: 0.7113
274	    downstream_hellaswag_acc_norm: 0.6132
275	    downstream_mean: 0.6234
276	    downstream_piqa_acc_norm: 0.7448
277	    downstream_winogrande_acc: 0.6251
278	
279	======================================================================
280	GROUP: grid_search_b  (28 experiments)
281	======================================================================
282	
283	  [grid_b0_1_seed123] status=DONE conclusion=success
284	    eval_ppl_holdout: 17.646
285	    eval_loss_holdout: 2.8705
286	
287	  [grid_b0_1_seed42] status=DONE conclusion=success
288	    eval_ppl_holdout: 17.657
289	    eval_loss_holdout: 2.871
290	    notes: PPL=17.657, between uniform(17.694) and b=0.3(17.640). b=0.1 provides minimal but positive improvement over uniform, consistent with near-uniform weighting at low b.
291	
292	  [grid_b0_1_seed456] status=DONE conclusion=success
293	    eval_ppl_holdout: 17.663
294	    eval_loss_holdout: 2.8715
295	
296	  [grid_b0_2_seed123] status=DONE conclusion=success
297	    eval_ppl_holdout: 17.637
298	    eval_loss_holdout: 2.87
299	
300	  [grid_b0_2_seed42] status=DONE conclusion=success
301	    eval_ppl_holdout: 17.64
302	    eval_loss_holdout: 2.8704
303	    notes: Director 预算修正砍掉：b=0.1 和 b=0.3 两点足够推断趋势，b=0.2 不再需要。→ D042 修正：grid_b0_2 重新加入，排在 grid_b0_1/b0_3 之后的下一个空 GPU。
304	
305	  [grid_b0_2_seed456] status=DONE conclusion=success
306	    eval_ppl_holdout: 17.645
307	    eval_loss_holdout: 2.87
308	
309	  [grid_b0_3_seed123] status=DONE conclusion=failed
310	    (no metrics)
311	
312	  [grid_b0_3_seed123_r2] status=DONE conclusion=success
313	    eval_ppl_holdout: 17.5792
314	    eval_loss_holdout: 2.8667
315	
316	  [grid_b0_3_seed42] status=DONE conclusion=success
317	    eval_ppl_holdout: 17.64
318	    train_loss: 9.1154
319	    eval_loss_holdout: 2.8702
320	    b_fixed: 0.3
321	    total_steps: 6103
322	
323	  [grid_b0_3_seed456] status=DONE conclusion=killed
324	    (no metrics)
325	
326	  [grid_b0_3_seed456_r2] status=DONE conclusion=success
327	    eval_ppl_holdout: 17.64
328	    train_loss: 9.085
329	    eval_loss_holdout: 2.87
330	    vs_uniform: -0.054 (17.64 vs 17.694)
331	    total_steps: 6103
332	    vs_grid_b03_seed42: 0.000 (17.64 vs 17.640)
333	    vs_grid_b05_seed456: -0.01 (17.64 vs 17.65)
334	
335	  [grid_b0_5_seed123] status=DONE conclusion=success
336	    eval_ppl_holdout: 17.638
337	    train_loss: 9.601
338	    eval_loss: 2.87
339	    total_steps: 6103
340	    train_runtime_s: 13104
341	
342	  [grid_b0_5_seed456] status=DONE conclusion=success
343	    eval_ppl_holdout: 17.65
344	    train_loss: 9.5622
345	    eval_loss: 2.8705
346	    total_steps: 6103
347	    train_runtime_s: 12953.96
348	    notes: 重提交成功（retry_count=1）。原 OOM 因 cuda:1 残留 eval 进程。已清理 exit marker，日志重定向正常。step 56/6103, ETA ~3.5h。
349	
350	  [grid_b1_0_seed123] status=DONE conclusion=success
351	    eval_ppl_holdout: 17.674
352	    train_loss: 10.218
353	    eval_loss: 2.8721
354	    total_steps: 6103
355	    train_runtime_s: 13878
356	
357	  [grid_b1_0_seed456] status=DONE conclusion=success
358	    eval_ppl_holdout: 17.68
359	    train_loss: 10.178
360	    eval_loss_holdout: 2.8734
361	    eval_loss: 2.8725
362	    total_steps: 6103
363	    train_runtime_s: 12963.87
364	
365	  [grid_b1_5_seed123] status=DONE conclusion=success
366	    eval_ppl_holdout: 17.701
367	    train_loss: 10.4776
368	    eval_loss: 2.8736
369	    total_steps: 6103
370	    train_runtime_s: 15053.1
371	
372	  [grid_b1_5_seed456] status=DONE conclusion=success
373	    eval_ppl_holdout: 17.71
374	    train_loss: 10.435
375	    eval_loss_holdout: 2.875
376	    eval_loss: 2.8741
377	    total_steps: 6103
378	    train_runtime_s: 12950.16
379	
380	  [grid_b2_0_seed123] status=DONE conclusion=success
381	    eval_ppl_holdout: 17.725
382	    train_loss: 10.61
383	    eval_loss: 2.875
384	    total_steps: 6103
385	    train_runtime_s: 13058.8
386	
387	  [grid_b2_0_seed456] status=DONE conclusion=success
388	    eval_ppl_holdout: 17.989
389	    train_loss: 10.625
390	    eval_loss: 2.8898
391	    total_steps: 6103
392	    train_runtime_s: 12969
393	    notes: checkpoint_artifact: true. D026 决策：seed456 b≥2.0 的 PPL 异常高（checkpoint 问题），论文只报 2-seed 数据。
394	
395	  [grid_b3_0_seed123] status=DONE conclusion=success
396	    eval_ppl_holdout: 17.76
397	    train_loss: 10.7422
398	    eval_loss: 2.877
399	    total_steps: 6103
400	    train_runtime_s: 12955.83
401	    notes: 训练完成，eval 未执行（should_evaluate=false，缺少 --eval_data_path 和 --eval_steps）。Checkpoint: /root/provenance_weight_training/output/models/grid_b3_0_seed123/final/ (model.safetensors 1.19GB)。需补跑 eval。
402	
403	  [grid_b3_0_seed456] status=DONE conclusion=success
404	    eval_ppl_holdout: 17.921
405	    train_loss: 5.435
406	    eval_loss: 2.886
407	    total_steps: 6103
408	    train_runtime_s: 6602
409	    notes: checkpoint_artifact: true. D026 决策：seed456 b≥2.0 的 PPL 异常高（checkpoint 问题），论文只报 2-seed 数据。
410	
411	  [grid_b5_0_seed123] status=DONE conclusion=success
412	    eval_ppl_holdout: 17.8039
413	    train_loss: 10.8468
414	    eval_loss: 2.8794
415	    total_steps: 6103
416	    train_runtime_s: 14434
417	    notes: PID 94717 已确认存活（SSH 验证 2026-05-14T11:39）。旧 PID 92798 已 kill，cron 重新注册。
418	
419	  [grid_b5_0_seed456] status=DONE conclusion=success
420	    eval_ppl_holdout: 17.993
421	    train_loss: 5.488
422	    eval_loss: 2.89
423	    total_steps: 6103
424	    train_runtime_s: 6601
425	    notes: checkpoint_artifact: true. D026 决策：seed456 b≥2.0 的 PPL 异常高（checkpoint 问题），论文只报 2-seed 数据。
426	
427	  [grid_b_low_seed42] status=DONE conclusion=failed
428	    (no metrics)
429	    notes: cron框架误杀(infrastructure bug)。根因: WANDB_MODE=disabled + tmux wrapper PID 不匹配，reconcile_crons 判定进程死亡并发送 SIGTERM。训练实际曾完成 3 个 b 值(8477/8477×3)，但第二次重启后在 step 431 被杀，所有 checkpoint 目录丢失(grid_b0_1/0_2/0_3_see
430	
431	  [grid_b_low_seed42_r2] status=DONE conclusion=failed
432	    (no metrics)
433	    notes: 失败根因：bash -c "..." 双引号内的 $b 被外层 shell 提前展开为空字符串，导致 --grid_b_value 收到空参数，argparse 报错 "expected one argument" 立即退出。日志首行 "Training grid b= ===" 确认 $b 为空。修复方法：将 $b 转义为 \$b（如 \$b 和 \${b}），或改用 bash -c '...'
434	
435	  [grid_b_low_seed42_r3] status=DONE conclusion=failed
436	    (no metrics)
437	    notes: Worker 提交时未指定 GPU，导致与 cuda:0 上的 contamination_60_seed42_r2 冲突。PID 258500 在启动后秒级崩溃。grid_b_low 需在 GPU 释放后单独提交（每个 b 值独立实验或硬编码脚本 + 显式 CUDA_VISIBLE_DEVICES）。
438	
439	  [grid_b_low_serial_seed42] status=DONE conclusion=killed
440	    (no metrics)
441	    notes: R4 killed: cuda:2 GPU冲突，与contamination_60_ess_only_seed42双进程占满显存(93042/97887 MiB)，仅完成48/6103步。第3次因GPU冲突失败(R3=cuda:0撞contamination_60, R4=cuda:2撞ess_only)。PID 265617已确认死亡，cuda:2显存恢复至~46.5GB，ess_only速度从
442	
443	  [grid_b_seed42_batch] status=DONE conclusion=success
444	    total_steps: 6103
445	    b0_5_eval_ppl: 17.651
446	    b1_0_eval_ppl: 17.692
447	    b1_5_eval_ppl: 17.718
448	    b2_0_eval_ppl: 17.741
449	    b3_0_eval_ppl: 17.774
450	    b5_0_eval_ppl: 17.818
451	    best_eval_ppl: 17.651
452	
453	======================================================================
454	GROUP: ess_only  (5 experiments)
455	======================================================================
456	
457	  [ess_only_seed123] status=DONE conclusion=success
458	    eval_ppl_holdout: 17.72
459	    train_loss: 10.2159
460	    eval_loss_holdout: 2.8746
461	    vs_uniform_ppl_delta: +0.034
462	    b_star_std: 4.7209
463	    vs_adaptive_fix_ppl_delta: +0.077
464	
465	  [ess_only_seed123_r2] status=DONE conclusion=success
466	    eval_ppl_holdout: 17.721
467	    train_loss: 6.86
468	    eval_loss_holdout: 2.8747
469	    total_steps: 6103
470	
471	  [ess_only_seed42] status=DONE conclusion=success
472	    eval_ppl: 17.73
473	    eval_loss: 2.875
474	    vs_adaptive_ppl_delta: +0.08
475	    vs_uniform_ppl_delta: +0.038
476	
477	  [ess_only_seed456] status=DONE conclusion=success
478	    eval_ppl_holdout: 17.76
479	    train_loss: 1.9364
480	    eval_loss_holdout: 2.877
481	
482	  [ess_only_seed456_r2] status=DONE conclusion=success
483	    eval_ppl_holdout: 17.762
484	    train_loss: 5.998
485	    eval_loss_holdout: 2.877
486	    total_steps: 6103
487	
488	======================================================================
489	GROUP: aeff_only  (3 experiments)
490	======================================================================
491	
492	  [aeff_only_nmin1_seed123] status=DONE conclusion=success
493	    holdout_ppl: 17.733
494	
495	  [aeff_only_nmin1_seed42] status=DONE conclusion=success
496	    holdout_ppl: 17.75
497	
498	  [aeff_only_nmin1_seed456] status=DONE conclusion=success
499	    holdout_ppl: 17.744
500	
501	======================================================================
502	GROUP: random_reweight  (10 experiments)
503	======================================================================
504	
505	  [random_reweight_baseline_seed42] status=DONE conclusion=success
506	    holdout_ppl: 17.95829
507	    ood_owt_ppl: 18.60614
508	    ood_wiki_ppl: 15.51906
509	
510	  [random_reweight_seed123] status=DONE conclusion=success
511	    holdout_ppl: 17.945
512	    train_loss: 8.042
513	    total_steps: 6103
514	    owt_ppl: 18.622
515	    wiki_ppl: 15.562
516	
517	  [random_reweight_seed123_r2] status=DONE conclusion=failed
518	    (no metrics)
519	
520	  [random_reweight_seed123_r3] status=DONE conclusion=failed
521	    (no metrics)
522	
523	  [random_reweight_seed123_r4] status=DONE conclusion=failed
524	    (no metrics)
525	
526	  [random_reweight_seed123_r5] status=DONE conclusion=success
527	    eval_ppl_holdout: 17.8
528	    train_loss: 8.0176
529	    eval_loss_holdout: 2.8793
530	    total_steps: 6103
531	
532	  [random_reweight_seed42] status=DONE conclusion=failed
533	    (no metrics)
534	    notes: 根因诊断：实际只跑~500步(8%)，"6092/8477"是eval进度条非training。WANDB_MODE=offline写~150MB到30GB根分区→磁盘满→OOM killer在eval期间杀进程→save从未执行→零checkpoint。修复：WANDB_MODE=disabled + output_dir改数据盘。v2脚本已dry-run验证通过。
535	
536	  [random_reweight_seed456] status=DONE conclusion=success
537	    eval_ppl_holdout: 17.777
538	    train_loss: 6.657
539	    eval_loss_holdout: 2.8779
540	    total_steps: 6103
541	
542	  [random_reweight_v2_seed42] status=DONE conclusion=success
543	    eval_ppl_holdout: 17.83
544	    eval_loss_holdout: 2.8809
545	
546	  [random_reweight_v2_seed456] status=DONE conclusion=success
547	    holdout_ppl: 17.951
548	    owt_ppl: 18.602
549	    wiki_ppl: 15.503
550	
551	======================================================================
552	GROUP: detect_remove  (31 experiments)
553	======================================================================
554	
555	  [detect_remove_baseline_seed42] status=DONE conclusion=success
556	    eval_ppl_holdout: 17.29
557	    train_loss: 11.003
558	    eval_loss_holdout: 2.8499
559	    total_steps: 6103
560	    notes: 完成时 conclusion 指引: b=0 throughout; adaptive degenerates to uniform post-filtering. detect-and-remove alone sufficient — adaptive adds no value on already-clean data. 写论文时注意: filtered subset (~153K) 训练
561	
562	  [detect_remove_q01_epoch_matched_seed42] status=DONE conclusion=success
563	    eval_ppl_holdout: 18.0436
564	    eval_loss_holdout: 2.8928
565	
566	  [detect_remove_q01_seed42] status=DONE conclusion=success
567	    eval_ppl_holdout: 17.4
568	    eval_ppl_openwebtext: 18.22
569	    eval_ppl_wikitext: 28.22
570	
571	  [detect_remove_q02_seed42] status=DONE conclusion=success
572	    eval_ppl_holdout: 17.27
573	    eval_ppl_openwebtext: 18.06
574	    eval_ppl_wikitext: 27.64
575	    train_loss: 11.348
576	    eval_loss_holdout: 2.8491
577	
578	  [detect_remove_q03_epoch_matched_seed42] status=DONE conclusion=success
579	    eval_ppl_holdout: 17.74
580	    eval_loss_holdout: 2.876
581	    total_steps: 1927
582	
583	  [detect_remove_q03_seed123] status=DONE conclusion=success
584	    eval_ppl_holdout: 17.25
585	    eval_ppl_openwebtext: 18.03
586	    eval_ppl_wikitext: 27.53
587	    eval_loss_holdout: 2.8479
588	    epoch: 0.84
589	    total_steps: 6103
590	    train_runtime_s: 13059
591	
592	  [detect_remove_q03_seed42] status=DONE conclusion=failed
593	    (no metrics)
594	
595	  [detect_remove_q03_seed42_r2] status=DONE conclusion=success
596	    eval_ppl_holdout: 17.25
597	    eval_ppl_openwebtext: 18.004
598	    eval_ppl_wikipedia: 15.037
599	    eval_loss_holdout: 2.848
600	    downstream_arc_challenge_acc_norm: 0.3549
601	    downstream_arc_easy_acc_norm: 0.6301
602	    downstream_hellaswag_acc_norm: 0.4851
603	    downstream_piqa_acc_norm: 0.6872
604	    downstream_winogrande_acc: 0.5675
605	
606	  [detect_remove_q03_seed456] status=DONE conclusion=success
607	    eval_ppl_holdout: 17.2509
608	    eval_ppl_openwebtext: 18.03
609	    eval_ppl_wikitext: 27.61
610	    train_loss: 11.255
611	    eval_loss_holdout: 2.8479
612	    total_steps: 6103
613	
614	  [detect_remove_q04_seed42] status=DONE conclusion=success
615	    eval_ppl_holdout: 17.26
616	    eval_ppl_openwebtext: 18.001
617	    eval_ppl_wikipedia: 15.038
618	    eval_loss_holdout: 2.8485
619	    downstream_arc_challenge_acc_norm: 0.3567
620	    downstream_arc_easy_acc_norm: 0.6107
621	    downstream_hellaswag_acc_norm: 0.4819
622	    downstream_piqa_acc_norm: 0.6931
623	    downstream_winogrande_acc: 0.5659
624	
625	  [detect_remove_q05_epoch_matched] status=PREPARING conclusion=killed
626	    (no metrics)
627	
628	  [detect_remove_q05_epoch_matched_seed42] status=DONE conclusion=success
629	    eval_ppl_holdout: 17.65
630	    eval_loss_holdout: 2.8707
631	    vs_adaptive: -0.001 (17.650 vs 17.651, nearly identical to adaptive)
632	    total_steps: 2533
633	    notes: Content-level 1 epoch: 153K samples × ~540 avg tokens = ~83M tokens → max_steps=2533. NOT Trainer epoch (9607 steps/315M tokens).
634	
635	  [detect_remove_q05_seed123] status=DONE conclusion=success
636	    eval_ppl_holdout: 17.27
637	    eval_ppl_openwebtext: 18.01
638	    eval_ppl_wikitext: 27.75
639	    eval_loss_holdout: 2.8491
640	
641	  [detect_remove_q05_seed42] status=PREPARING conclusion=None
642	    (no metrics)
643	
644	  [detect_remove_q05_seed456] status=DONE conclusion=success
645	    eval_ppl_holdout: 17.28
646	    eval_ppl_openwebtext: 18.01
647	    eval_ppl_wikitext: 27.68
648	    eval_loss_holdout: 2.8493
649	
650	  [detect_remove_q05_v2_seed123] status=DONE conclusion=failed
651	    holdout_ppl: 17.3656
652	    train_loss: 2.76
653	    total_steps: 24414
654	    owt_ppl: 18.198
655	    wiki_ppl: 15.2318
656	
657	  [detect_remove_q05_v2_seed123_r2] status=DONE conclusion=success
658	    holdout_ppl: 17.272
659	    train_loss: 11.01
660	    total_steps: 6103
661	    owt_ppl: 18.008
662	    wiki_ppl: 15.047
663	
664	  [detect_remove_q05_v2_seed42] status=DONE conclusion=success
665	    holdout_ppl: 17.2853
666	    train_loss: 11
667	    total_steps: 6103
668	    owt_ppl: 18.0139
669	    wiki_ppl: 15.0528
670	
671	  [detect_remove_q05_v2_seed456] status=DONE conclusion=success
672	    holdout_ppl: 17.277
673	    train_loss: 11.01
674	    total_steps: 6103
675	    owt_ppl: 18.017
676	    wiki_ppl: 15.04
677	
678	  [detect_remove_q06_seed42] status=DONE conclusion=success
679	    eval_ppl_holdout: 17.3
680	    eval_loss_holdout: 2.8507
681	
682	  [detect_remove_q07_epoch_matched_seed42] status=DONE conclusion=success
683	    eval_ppl_holdout: 17.62
684	    eval_loss_holdout: 2.8689
685	    total_steps: 3047
686	    notes: 首次运行 EXIT_CODE=1 失败(~70min)，自动重试后训练完成(3047 steps, 6425s, EXIT_CODE=0)。Model saved to /root/autodl-tmp/output/models/detect_remove_q07_epoch_matched_seed42/final。等待 eval holdout PPL。
687	
688	  [detect_remove_q07_seed42] status=DONE conclusion=success
689	    eval_ppl_holdout: 17.32
690	    eval_loss_holdout: 2.8519
691	
692	  [detect_remove_q07_seed42_r2] status=PREPARING conclusion=killed
693	    (no metrics)
694	
695	  [detect_remove_q08_seed42] status=DONE conclusion=success
696	    eval_ppl_holdout: 17.3442
697	    eval_ppl_openwebtext: 18.039
698	    eval_ppl_wikipedia: 15.066
699	    eval_loss_holdout: 2.8533
700	    downstream_arc_challenge_acc_norm: 0.3592
701	    downstream_arc_easy_acc_norm: 0.6086
702	    downstream_hellaswag_acc_norm: 0.4855
703	    downstream_piqa_acc_norm: 0.6937
704	    downstream_winogrande_acc: 0.5817
705	
706	  [detect_remove_q09_epoch_matched_seed42] status=DONE conclusion=success
707	    eval_ppl_holdout: 17.628
708	    eval_loss_holdout: 2.8695
709	    total_steps: 3770
710	
711	  [detect_remove_q09_seed42] status=DONE conclusion=success
712	    eval_ppl_holdout: 17.42
713	    eval_loss_holdout: 2.8577
714	
715	  [dr_epoch_matched_indep_lr_seed42] status=DONE conclusion=failed
716	    holdout_ppl: 18.78174
717	    ood_owt_ppl: 19.23533
718	    ood_wiki_ppl: 15.95958
719	    total_steps: 2533
720	    notes: INVALIDATED: scored_data_filtered_q05.jsonl had inverted filter (kept q>0.5 = 85% synthetic instead of q≤0.5 = real data). PPL=18.782 is meaningless. Need to regenerate data and rerun.
721	
722	  [dr_epoch_matched_indep_lr_v2_seed42] status=DONE conclusion=success
723	    holdout_ppl: 17.65053
724	    ood_owt_ppl: 18.26112
725	    ood_wiki_ppl: 15.19382
726	    total_steps: 2533
727	
728	  [dr_epoch_matched_seed123] status=DONE conclusion=failed
729	    holdout_ppl: 18.332
730	    owt_ppl: 18.354
731	    wiki_ppl: 14.955
732	
733	  [dr_epoch_matched_seed123_r2] status=DONE conclusion=success
734	    holdout_ppl: 17.6591
735	    owt_ppl: 18.2991
736	    wiki_ppl: 15.1918
737	
738	  [dr_epoch_matched_seed456] status=DONE conclusion=success
739	    holdout_ppl: 17.66
740	    owt_ppl: 18.27
741	    wiki_ppl: 15.16
742	
743	======================================================================
744	GROUP: batch_size_bs8  (22 experiments)
745	======================================================================
746	
747	  [batch_adaptive_tau_rho04_seed42] status=DONE conclusion=negative
748	    eval_ppl_holdout: 17.681
749	    train_loss: 9.8206
750	    eval_loss_holdout: 2.8725
751	
752	  [batch_adaptive_tau_rho06_r2] status=DONE conclusion=failed
753	    (no metrics)
754	
755	  [batch_adaptive_tau_rho06_r3] status=DONE conclusion=failed
756	    (no metrics)
757	
758	  [batch_adaptive_tau_rho06_r5] status=DONE conclusion=negative
759	    eval_ppl_holdout: 17.73
760	    train_loss: 9.267
761	    eval_loss_holdout: 2.8754
762	    total_steps: 6103
763	
764	  [batch_adaptive_tau_rho06_seed42] status=DONE conclusion=failed
765	    (no metrics)
766	
767	  [bs8_auto_nmin_r2] status=DONE conclusion=failed
768	    (no metrics)
769	
770	  [bs8_auto_nmin_r3] status=DONE conclusion=failed
771	    (no metrics)
772	
773	  [bs8_auto_nmin_r5] status=DONE conclusion=success
774	    eval_ppl_holdout: 17.66
775	    train_loss: 5.163
776	    eval_loss_holdout: 2.8716
777	    epoch: 0.26
778	    total_steps: 6103
779	    b_star_std: 0.7563
780	
781	  [bs8_auto_nmin_seed42] status=DONE conclusion=failed
782	    (no metrics)
783	
784	  [bs8_nmin2_seed42] status=DONE conclusion=failed
785	    (no metrics)
786	    notes: OOM failed: GPU 2 was occupied by zombie PID 236702 (old bs8_seed42). Superseded by bs8_nmin2_seed42_r2. Config: n_min=2, bs=8, grad_accum=2, tau=0.8, adaptive, seed=42.
787	
788	  [bs8_nmin2_seed42_r2] status=DONE conclusion=negative
789	    eval_ppl_holdout: 17.73
790	    train_loss: 5.4065
791	    eval_loss_holdout: 2.8752
792	    notes: 训练完成 6103/6103 steps, train_loss=5.4065. EXIT_CODE=129 (SIGHUP) 发生在训练完成后 W&B finalization 阶段，不影响结果。Checkpoint 验证通过。Eval PPL=17.73 > uniform avg 17.694 (+0.036), 与 ESS-only 水平相当(~17.72)。**NEGATIVE but 
793	
794	  [bs8_nmin4_adaptive_seed123] status=DONE conclusion=failed
795	    (no metrics)
796	
797	  [bs8_nmin4_adaptive_seed123_r2] status=DONE conclusion=success
798	    eval_ppl_holdout: 17.631
799	    eval_ppl_owt: 18.338
800	    eval_ppl_wiki: 15.353
801	
802	  [bs8_nmin4_adaptive_seed42] status=DONE conclusion=success
803	    holdout_ppl: 17.650425404986372
804	    owt_ppl: 18.332103963757113
805	    wiki_ppl: 15.318017946105257
806	
807	  [bs8_nmin4_adaptive_seed456] status=DONE conclusion=killed
808	    (no metrics)
809	
810	  [bs8_nmin4_adaptive_seed456_r2] status=DONE conclusion=success
811	    holdout_ppl: 17.646
812	    owt_ppl: 18.322
813	    wiki_ppl: 15.299
814	
815	  [bs8_nmin4_uniform_seed123] status=DONE conclusion=failed
816	    (no metrics)
817	
818	  [bs8_nmin4_uniform_seed123_r2] status=DONE conclusion=success
819	    eval_ppl_holdout: 17.687
820	    eval_ppl_owt: 18.37
821	    eval_ppl_wiki: 15.385
822	
823	  [bs8_nmin4_uniform_seed42] status=DONE conclusion=success
824	    holdout_ppl: 17.694185837410274
825	    owt_ppl: 18.363068741825792
826	    wiki_ppl: 15.336710587451519
827	
828	  [bs8_nmin4_uniform_seed456] status=DONE conclusion=killed
829	    (no metrics)
830	
831	  [bs8_nmin4_uniform_seed456_r2] status=DONE conclusion=success
832	    holdout_ppl: 17.702
833	    owt_ppl: 18.393
834	    wiki_ppl: 15.354
835	
836	  [bs8_seed42] status=DONE conclusion=failed
837	    (no metrics)
838	    notes: Killed at 1% (71/6103 steps). Wrong config: n_min=4 matches same ESS/bs ratio as n_min=2/bs=4. Director instructed restart with n_min=2 + bs=8 for wider ESS dynamic range [2,8]. Replaced by bs8_nmin2_
839	
840	======================================================================
841	GROUP: batch_size_bs16  (10 experiments)
842	======================================================================
843	
844	  [batchsize16_nmin8_r2] status=DONE conclusion=killed
845	    (no metrics)
846	
847	  [batchsize16_nmin8_r3] status=DONE conclusion=success
848	    eval_ppl_holdout: 17.65
849	    train_loss: 2.6308
850	    eval_loss_holdout: 2.871
851	    n_min: 8
852	    total_steps: 6103
853	
854	  [batchsize16_nmin8_seed42] status=DONE conclusion=failed
855	    (no metrics)
856	    notes: westd-47453 permanently down (2026-05-17). Experiment was queued on 47453 (launcher PID 375555) waiting for GPU, never actually ran. Data lost. Needs migration to westd-30476.
857	
858	  [bs16_adaptive_tau07_seed123] status=DONE conclusion=failed
859	    (no metrics)
860	    notes: 失败原因: 磁盘空间不足 — torch.save(optimizer.state_dict()) 在 step 500 首次 checkpoint 时 IOException (basic_ios::clear: iostream error + enforce fail at inline_container.cc:668, unexpected pos 1513744000 vs 15137
861	
862	  [bs16_adaptive_tau07_seed123_r2] status=DONE conclusion=success
863	    holdout_ppl: 17.616
864	    owt_ppl: 18.325
865	    wiki_ppl: 15.348
866	
867	  [bs16_adaptive_tau07_seed42] status=DONE conclusion=success
868	    holdout_ppl: 17.631
869	    train_loss: 2.537
870	    owt_ppl: 18.309
871	    wiki_ppl: 15.286
872	
873	  [bs16_adaptive_tau07_seed456] status=DONE conclusion=success
874	    holdout_ppl: 17.645
875	    train_loss: 2.528
876	    total_steps: 6103
877	    owt_ppl: 18.313
878	    wiki_ppl: 15.296
879	
880	  [bs16_uniform_seed123] status=DONE conclusion=success
881	    holdout_ppl: 17.686
882	    train_loss: 1.997
883	    owt_ppl: 18.369
884	    wiki_ppl: 15.381
885	
886	  [bs16_uniform_seed42] status=DONE conclusion=success
887	    holdout_ppl: 17.694
888	    train_loss: 1.965
889	    owt_ppl: 18.364
890	    wiki_ppl: 15.337
891	
892	  [bs16_uniform_seed456] status=DONE conclusion=success
893	    holdout_ppl: 17.717
894	    train_loss: 1.991
895	    total_steps: 6103
896	    owt_ppl: 18.39
897	    wiki_ppl: 15.363
898	
899	======================================================================
900	GROUP: rho_variants  (19 experiments)
901	======================================================================
902	
903	  [hybrid_rho04_seed42] status=DONE conclusion=success
904	    eval_ppl_holdout: 17.514
905	    eval_loss_holdout: 2.863
906	
907	  [hybrid_rho06_seed42] status=DONE conclusion=success
908	    eval_ppl_holdout: 17.526
909	    eval_ppl_openwebtext: 18.208
910	    eval_ppl_wikipedia: 15.267
911	    eval_loss_holdout: 2.8637
912	    downstream_arc_challenge_acc_norm: 0.3524
913	    downstream_arc_easy_acc_norm: 0.6208
914	    downstream_hellaswag_acc_norm: 0.4801
915	    downstream_piqa_acc_norm: 0.6931
916	    downstream_winogrande_acc: 0.5785
917	
918	  [rho02_adaptive_tau08_seed42] status=DONE conclusion=negative
919	    eval_ppl_holdout: 17.382
920	    eval_loss_holdout: 2.8555
921	    tau: 0.8
922	    rho: 0.2
923	    total_steps: 6103
924	    vs_rho02_uniform: +0.046 (17.382 vs 17.336)
925	    vs_rho04_uniform: -0.312 (17.382 vs 17.694)
926	
927	  [rho02_adaptive_tau09_r2] status=DONE conclusion=failed
928	    (no metrics)
929	
930	  [rho02_adaptive_tau09_r3] status=DONE conclusion=failed
931	    (no metrics)
932	
933	  [rho02_adaptive_tau09_r4] status=DONE conclusion=failed
934	    (no metrics)
935	
936	  [rho02_adaptive_tau09_r5] status=DONE conclusion=negative
937	    eval_ppl_holdout: 17.45
938	    train_loss: 11.864
939	    eval_loss_holdout: 2.8593
940	    epoch: 0.47
941	    b_star_std: 4.3982
942	
943	  [rho02_adaptive_tau09_seed42] status=DONE conclusion=failed
944	    (no metrics)
945	    notes: Retry: first attempt failed due to CUDA_VISIBLE_DEVICES=-1 in script overriding submit_training_job env. Fixed by removing export line from script. PID 367604.
946	
947	  [rho02_uniform_seed42] status=DONE conclusion=success
948	    eval_ppl_holdout: 17.336
949	    eval_loss_holdout: 2.853
950	
951	  [rho03_adaptive_seed123] status=DONE conclusion=success
952	    eval_ppl_holdout: 17.435
953	    eval_ppl_owt: 18.148
954	    eval_ppl_wiki: 15.165
955	
956	  [rho03_adaptive_seed42] status=DONE conclusion=success
957	    eval_ppl_holdout: 17.422
958	    eval_ppl_owt: 18.123
959	    eval_ppl_wiki: 15.172
960	
961	  [rho03_adaptive_seed456] status=DONE conclusion=failed
962	    (no metrics)
963	    notes: 失败原因: FileNotFoundError — checkpoint-1000/trainer_state.json 不存在，resume_from_checkpoint 失败 | 类型: infrastructure | fix_worker_id: worker_diagnose_rho03_adaptive_seed456_20260523T032401 | 自动修复中
964	
965	  [rho03_adaptive_seed456_r2] status=DONE conclusion=success
966	    eval_ppl_holdout: 17.424
967	    eval_ppl_owt: 18.115
968	    eval_ppl_wiki: 15.161
969	
970	  [rho03_uniform_seed123] status=DONE conclusion=success
971	    eval_ppl_holdout: 17.433
972	    eval_ppl_owt: 18.126
973	    eval_ppl_wiki: 15.204
974	
975	  [rho03_uniform_seed42] status=DONE conclusion=success
976	    eval_ppl_holdout: 17.422
977	    eval_ppl_owt: 18.113
978	    eval_ppl_wiki: 15.204
979	
980	  [rho03_uniform_seed456] status=DONE conclusion=success
981	    eval_ppl_holdout: 17.419
982	    eval_ppl_owt: 18.109
983	    eval_ppl_wiki: 15.168
984	
985	  [rho06_tau07_seed123] status=DONE conclusion=killed
986	    (no metrics)
987	
988	  [rho06_tau07_seed42] status=DONE conclusion=failed
989	    eval_ppl_holdout: 17.526
990	    eval_ppl_openwebtext: 18.208
991	    eval_ppl_wikipedia: 15.267
992	    downstream_arc_challenge_acc_norm: 0.3524
993	    downstream_arc_easy_acc_norm: 0.6208
994	    downstream_hellaswag_acc_norm: 0.4801
995	    downstream_piqa_acc_norm: 0.6931
996	    downstream_winogrande_acc: 0.5785
997	
998	  [rho06_tau07_seed456] status=DONE conclusion=killed
999	    (no metrics)
1000	
1001	======================================================================
1002	GROUP: tau_sensitivity  (25 experiments)
1003	======================================================================
1004	
1005	  [adaptive_rho06_tau07_seed123] status=DONE conclusion=success
1006	    holdout_ppl: 17.727
1007	    eval_ppl_openwebtext: 18.385
1008	    eval_ppl_wikipedia: 15.329
1009	    downstream_arc_challenge_acc_norm: 0.3422
1010	    downstream_arc_easy_acc_norm: 0.5951
1011	    downstream_hellaswag_acc_norm: 0.4811
1012	    downstream_mean: 0.5361
1013	    downstream_piqa_acc_norm: 0.6866
1014	    downstream_winogrande_acc: 0.5754
1015	
1016	  [adaptive_rho06_tau07_seed42] status=DONE conclusion=success
1017	    holdout_ppl: 17.735
1018	    eval_ppl_openwebtext: 18.408
1019	    eval_ppl_wikipedia: 15.355
1020	    downstream_arc_challenge_acc_norm: 0.3422
1021	    downstream_arc_easy_acc_norm: 0.6132
1022	    downstream_hellaswag_acc_norm: 0.4807
1023	    downstream_mean: 0.5403
1024	    downstream_piqa_acc_norm: 0.6861
1025	    downstream_winogrande_acc: 0.5793
1026	
1027	  [adaptive_rho06_tau07_seed456] status=DONE conclusion=success
1028	    holdout_ppl: 17.732
1029	    eval_ppl_openwebtext: 18.411
1030	    eval_ppl_wikipedia: 15.424
1031	    downstream_arc_challenge_acc_norm: 0.3456
1032	    downstream_arc_easy_acc_norm: 0.6128
1033	    downstream_hellaswag_acc_norm: 0.4806
1034	    downstream_mean: 0.5375
1035	    downstream_piqa_acc_norm: 0.6866
1036	    downstream_winogrande_acc: 0.562
1037	
1038	  [adaptive_tau08_scratch_seed42] status=DONE conclusion=failed
1039	    (no metrics)
1040	
1041	  [adaptive_tau08_scratch_seed42_v2] status=DONE conclusion=failed
1042	    (no metrics)
1043	
1044	  [adaptive_tau08_scratch_seed42_v3] status=DONE conclusion=success
1045	    holdout_ppl: 17.6885
1046	    ood_owt_ppl: 18.37026
1047	    ood_wiki_ppl: 15.34964
1048	
1049	  [contamination_60_adaptive_seed123_tau08] status=DONE conclusion=success
1050	    holdout_ppl: 17.73
1051	    eval_ppl_openwebtext: 18.4
1052	    eval_ppl_wikipedia: 15.34
1053	    downstream_arc_challenge_acc_norm: 0.3447
1054	    downstream_arc_easy_acc_norm: 0.6014
1055	    downstream_hellaswag_acc_norm: 0.4804
1056	    downstream_mean: 0.5368
1057	    downstream_piqa_acc_norm: 0.6877
1058	    downstream_winogrande_acc: 0.5699
1059	
1060	  [contamination_60_adaptive_seed42_tau08] status=DONE conclusion=success
1061	    holdout_ppl: 17.74
1062	    eval_ppl_openwebtext: 18.42
1063	    eval_ppl_wikipedia: 15.37
1064	    downstream_arc_challenge_acc_norm: 0.3439
1065	    downstream_arc_easy_acc_norm: 0.612
1066	    downstream_hellaswag_acc_norm: 0.4802
1067	    downstream_mean: 0.5398
1068	    downstream_piqa_acc_norm: 0.685
1069	    downstream_winogrande_acc: 0.5777
1070	
1071	  [contamination_60_tau06_seed42] status=DONE conclusion=success
1072	    eval_ppl_holdout: 17.7359
1073	    train_loss: 8.9804
1074	    eval_loss_holdout: 2.8756
1075	    total_steps: 6103
1076	    notes: D045 第二数据点。GPU 队列: cuda:2 (ess_only 完成后)。脚本: scripts/run_contamination_60_tau06.sh。优先级最高。
1077	
1078	  [contamination_60_tau07_seed42] status=DONE conclusion=success
1079	    eval_ppl_holdout: 17.73
1080	    train_loss: 9.358
1081	    eval_loss_holdout: 2.875
1082	    notes: D045 最高优先级。cuda:0, PID=282223, ρ=0.6 τ=0.7 (formula τ=1-ρ×0.5)。参数确认: tau=0.7, n_min=2, ρ=0.6, data=scored_data_60.jsonl (371499 samples)。
1083	
1084	**结果分析**: PPL=17.73。vs τ=0.8(17.74): -0.01 改善，formula 方向正确。vs
1085	
1086	  [tau07_downstream_eval] status=DONE conclusion=failed
1087	    (no metrics)
1088	
1089	  [tau07_seed123] status=DONE conclusion=success
1090	    eval_ppl_holdout: 17.666
1091	    eval_ppl_openwebtext: 18.348
1092	    eval_ppl_wikipedia: 15.345
1093	    downstream_arc_challenge_acc_norm: 0.3481
1094	    downstream_arc_easy_acc_norm: 0.6309
1095	    downstream_hellaswag_acc_norm: 0.4775
1096	    downstream_piqa_acc_norm: 0.6866
1097	    downstream_winogrande_acc: 0.5675
1098	
1099	  [tau07_seed42] status=DONE conclusion=success
1100	    eval_ppl_holdout: 17.68
1101	    eval_ppl_openwebtext: 18.348
1102	    eval_ppl_wikipedia: 15.331
1103	    downstream_arc_challenge_acc_norm: 0.3473
1104	    downstream_arc_easy_acc_norm: 0.6166
1105	    downstream_hellaswag_acc_norm: 0.4795
1106	    downstream_piqa_acc_norm: 0.6861
1107	    downstream_winogrande_acc: 0.5817
1108	
1109	  [tau07_seed456] status=DONE conclusion=success
1110	    eval_ppl_holdout: 17.677
1111	    eval_ppl_openwebtext: 18.344
1112	    eval_ppl_wikipedia: 15.315
1113	    downstream_arc_challenge_acc_norm: 0.3515
1114	    downstream_arc_easy_acc_norm: 0.6111
1115	    downstream_hellaswag_acc_norm: 0.4811
1116	    downstream_piqa_acc_norm: 0.6834
1117	    downstream_winogrande_acc: 0.5722
1118	
1119	  [tau_0.6_seed42] status=DONE conclusion=killed
1120	    (no metrics)
1121	    notes: 废弃: exp_id 含点号不合法，已用 tau_06_seed42 替代
1122	
1123	  [tau_05_nmin2_seed42] status=DONE conclusion=killed
1124	    (no metrics)
1125	
1126	  [tau_05_seed42] status=DONE conclusion=success
1127	    eval_ppl_holdout: 17.688
1128	    train_loss: 8.849
1129	    eval_loss: 2.8729
1130	    epoch: 0.26
1131	    total_steps: 6103
1132	    train_runtime_s: 13431.4
1133	    b_star_std: 0.8821
1134	
1135	  [tau_06_nmin2_seed42] status=DONE conclusion=killed
1136	    (no metrics)
1137	
1138	  [tau_06_seed42] status=DONE conclusion=success
1139	    eval_ppl_holdout: 17.6805
1140	    train_loss: 9.275
1141	    eval_loss: 2.8725
1142	    total_steps: 6103
1143	    train_runtime_s: 13436.64
1144	    b_star_std: 1.0693
1145	    notes: PPL=17.681 劣于 τ=0.8 baseline (17.650)，conclusion=negative。概念修正：τ 越低 → α_eff 下界越松 → b* 更小 → 降权力度更弱（非更激进）。正确因果链：τ 越高 → α_eff 下界越严 → min-intervention 需要更大 b* 才能满足约束 → 降权力度更强。
1146	
1147	  [tau_07_nmin2_seed42] status=DONE conclusion=killed
1148	    (no metrics)
1149	
1150	  [tau_07_seed42] status=DONE conclusion=success
1151	    eval_ppl_holdout: 17.6793
1152	    train_loss: 9.6707
1153	    eval_loss: 2.8724
1154	    total_steps: 6103
1155	    train_runtime_s: 15065
1156	    b_star_std: 1.4007
1157	
1158	  [tau_095_nmin2_seed42] status=DONE conclusion=killed
1159	    (no metrics)
1160	    notes: D048: 原始 tau_095_seed42 已确认 n_min=2，数据干净。二次 killed，不重跑。
1161	
1162	  [tau_095_seed42] status=DONE conclusion=negative
1163	    eval_ppl_holdout: 17.723
1164	    train_loss: 10.198
1165	    eval_loss: 2.8749
1166	    total_steps: 6103
1167	    train_runtime_s: 13699
1168	    b_star_std: 3.9923
1169	
1170	  [tau_09_nmin2_seed42] status=DONE conclusion=killed
1171	    (no metrics)
1172	    notes: D048: 原始 tau_09_seed42 已确认 n_min=2，数据干净。二次 killed，不重跑。
1173	
1174	  [tau_09_seed42] status=DONE conclusion=negative
1175	    eval_ppl_holdout: 17.712
1176	    eval_loss: 2.8742
1177	    b_star_std: 3.04
1178	
1179	======================================================================
1180	GROUP: nmin_sensitivity  (3 experiments)
1181	======================================================================
1182	
1183	  [nmin1_seed42] status=DONE conclusion=success
1184	    eval_ppl_holdout: 17.789
1185	    eval_loss: 2.8786
1186	    b_star_std: 8.374
1187	    notes: 训练完成(EXIT_CODE=0, 4h50m)。PPL=17.789，比 adaptive_fix(n_min=2, 17.650) 差 +0.139，比 uniform(17.690) 差 +0.099。n_min=1 导致极端 b* 分布：46.7% batch b*≥2，p75=20.0(上限)，mean=7.197。ESS 约束几乎失效，over-downweighting 明显。con
1188	
1189	  [nmin4_seed42] status=DONE conclusion=success
1190	    eval_ppl_holdout: 17.6947
1191	    train_loss: 7.989
1192	    eval_loss: 2.8733
1193	    total_steps: 6103
1194	    train_runtime_s: 16231
1195	    b_star_std: 0
1196	    notes: Mid-training check @step 2036/6103: b=0.0, ess=4.0 (=n_min), weighted_loss==unweighted_loss — confirms b*=0 degenerates to uniform weighting as theoretically predicted. Eval commands prepared for post
1197	
1198	  [nmin5_seed42] status=DONE conclusion=killed
1199	    (no metrics)
1200	    notes: D047 砍掉，GPU 预算不够。
1201	
1202	======================================================================
1203	GROUP: ood_eval  (4 experiments)
1204	======================================================================
1205	
1206	  [adaptive_ood_seed123] status=DONE conclusion=success
1207	    eval_ppl_holdout: 17.677
1208	    eval_ppl_openwebtext: 18.373
1209	    eval_ppl_wikipedia: 15.37
1210	    downstream_arc_challenge_acc_norm: 0.3481
1211	    downstream_arc_easy_acc_norm: 0.6301
1212	    downstream_hellaswag_acc_norm: 0.4791
1213	    downstream_piqa_acc_norm: 0.6844
1214	    downstream_winogrande_acc: 0.5706
1215	
1216	  [adaptive_ood_seed456] status=DONE conclusion=success
1217	    eval_ppl_holdout: 17.683
1218	    eval_ppl_openwebtext: 18.366
1219	    eval_ppl_wikipedia: 15.345
1220	    downstream_arc_challenge_acc_norm: 0.3541
1221	    downstream_arc_easy_acc_norm: 0.6077
1222	    downstream_hellaswag_acc_norm: 0.48
1223	    downstream_piqa_acc_norm: 0.6806
1224	    downstream_winogrande_acc: 0.5714
1225	
1226	  [uniform_ood_seed123] status=DONE conclusion=success
1227	    eval_ppl_holdout: 17.6861
1228	    eval_ppl_openwebtext: 18.3678
1229	    eval_ppl_wikipedia: 15.3768
1230	    downstream_arc_challenge_acc_norm: 0.3507
1231	    downstream_arc_easy_acc_norm: 0.6229
1232	    downstream_hellaswag_acc_norm: 0.4797
1233	    downstream_piqa_acc_norm: 0.685
1234	    downstream_winogrande_acc: 0.5762
1235	
1236	  [uniform_ood_seed456] status=DONE conclusion=success
1237	    eval_ppl_holdout: 17.7015
1238	    eval_ppl_openwebtext: 18.3865
1239	    eval_ppl_wikipedia: 15.3594
1240	    downstream_arc_challenge_acc_norm: 0.3439
1241	    downstream_arc_easy_acc_norm: 0.6166
1242	    downstream_hellaswag_acc_norm: 0.4826
1243	    downstream_piqa_acc_norm: 0.6795
1244	    downstream_winogrande_acc: 0.5667
1245	
1246	======================================================================
1247	GROUP: ngram_detector  (7 experiments)
1248	======================================================================
1249	
1250	  [eval_ngram_adaptive] status=DONE conclusion=success
1251	    perplexity: 17.82
1252	
1253	  [eval_ngram_uniform] status=DONE conclusion=success
1254	    perplexity: 17.69
1255	
1256	  [ngram_adaptive_seed123] status=DONE conclusion=negative
1257	    eval_ppl_holdout: 17.823
1258	    train_loss: 9.289
1259	    eval_loss_holdout: 2.8805
1260	    total_steps: 6103
1261	
1262	  [ngram_adaptive_seed42] status=DONE conclusion=negative
1263	    holdout_ppl: 17.820214
1264	
1265	  [ngram_adaptive_seed456] status=DONE conclusion=failed
1266	    (no metrics)
1267	
1268	  [ngram_adaptive_seed456_v2] status=DONE conclusion=success
1269	    holdout_ppl: 17.82607
1270	
1271	  [ngram_uniform_seed42] status=DONE conclusion=success
1272	    eval_ppl_holdout: 17.69
1273	    eval_loss_holdout: 2.8733
1274	
1275	======================================================================
1276	GROUP: gpt2_detector  (7 experiments)
1277	======================================================================
1278	
1279	  [gpt2_adaptive_seed123] status=DONE conclusion=failed
1280	    (no metrics)
1281	
1282	  [gpt2_adaptive_seed123_v2] status=DONE conclusion=failed
1283	    (no metrics)
1284	
1285	  [gpt2_adaptive_seed123_v3] status=DONE conclusion=success
1286	    holdout_ppl: 17.78848
1287	
1288	  [gpt2_adaptive_seed42] status=DONE conclusion=negative
1289	    eval_ppl_holdout: 17.79
1290	    train_loss: 10.58
1291	    eval_loss_holdout: 2.879
1292	
1293	  [gpt2_adaptive_seed456] status=DONE conclusion=failed
1294	    (no metrics)
1295	
1296	  [gpt2_adaptive_seed456_v2] status=DONE conclusion=success
1297	    holdout_ppl: 17.79719
1298	
1299	  [gpt2_uniform_seed42] status=DONE conclusion=success
1300	    eval_ppl_holdout: 17.69
1301	    train_loss: 7.989
1302	    eval_loss_holdout: 2.8733
1303	
1304	======================================================================
1305	GROUP: contamination_60  (16 experiments)
1306	======================================================================
1307	
1308	  [contamination_60_adaptive_seed456] status=DONE conclusion=success
1309	    eval_ppl_holdout: 17.735
1310	    eval_loss_holdout: 2.8755
1311	
1312	  [contamination_60_ess_only_seed123] status=DONE conclusion=success
1313	    eval_ppl_holdout: 17.763
1314	    eval_loss_holdout: 2.8771
1315	
1316	  [contamination_60_ess_only_seed42] status=DONE conclusion=success
1317	    eval_ppl_holdout: 17.77
1318	    train_loss: 9.842
1319	    eval_loss_holdout: 2.8775
1320	    total_steps: 6103
1321	    notes: ρ=0.6 ESS-only PPL=17.77 ≈ uniform (17.766), max-intervention 在高 contamination 下完全失效。vs ρ=0.4 ESS-only avg 17.723 → ρ增加0.2导致+0.047退化。关键对比: dual(17.74) < ESS-only(17.77), Claim 1 在 ρ=0.6 下仍成立(gap=0.03,
1322	
1323	  [contamination_60_ess_only_seed456] status=DONE conclusion=success
1324	    eval_ppl_holdout: 17.762
1325	    eval_loss_holdout: 2.8771
1326	
1327	  [contamination_60_grid_b0_3_seed42] status=DONE conclusion=success
1328	    eval_ppl_holdout: 17.634
1329	    total_steps: 6103
1330	    checkpoint_1500_ppl: 18.583
1331	
1332	  [contamination_60_grid_b0_5_seed42] status=DONE conclusion=success
1333	    eval_ppl: 17.704
1334	    eval_loss: 2.8738
1335	    notes: 训练完成 6103/6103 steps。EXIT_CODE=129 (SIGHUP) 发生在训练完成后（与 contamination_60_uniform_seed42 同一模式）。WANDB_MODE=disabled 导致 cron 误判为 failed。实际 success，等 eval PPL。
1336	
1337	  [contamination_60_random_seed123] status=DONE conclusion=success
1338	    eval_ppl_holdout: 17.87
1339	    eval_loss_holdout: 2.8832
1340	
1341	  [contamination_60_random_seed42] status=DONE conclusion=success
1342	    eval_ppl_holdout: 17.832
1343	    total_steps: 6103
1344	
1345	  [contamination_60_random_seed456] status=DONE conclusion=success
1346	    eval_ppl_holdout: 17.88
1347	    eval_loss_holdout: 2.8837
1348	
1349	  [contamination_60_seed123] status=DONE conclusion=success
1350	    eval_ppl_holdout: 17.732
1351	    train_loss: 9.6302
1352	    eval_loss_holdout: 2.8754
1353	    total_steps: 6103
1354	
1355	  [contamination_60_seed42] status=DONE conclusion=failed
1356	    (no metrics)
1357	    notes: 数据验证通过: scored_data_60.jsonl 371,499行/907MB, synthetic=222900/human=148599, actual ρ=0.6。q_score: mean=0.6243, std=0.3703, median=0.7753。字段: text/depth/source_model/prompt_tokens/generated_tokens/deco
1358	
1359	  [contamination_60_seed42_r2] status=DONE conclusion=success
1360	    eval_ppl_holdout: 17.74
1361	    train_loss: 9.6349
1362	    eval_loss_holdout: 2.8759
1363	
1364	  [contamination_60_uniform_seed123] status=DONE conclusion=success
1365	    eval_ppl_holdout: 17.754
1366	    eval_loss_holdout: 2.8766
1367	    total_steps: 6103
1368	
1369	  [contamination_60_uniform_seed42] status=DONE conclusion=success
1370	    eval_ppl_holdout: 17.766
1371	    train_loss: 7.649
1372	    eval_loss_holdout: 2.8773
1373	    notes: 训练实际已完成 (6103/6103 steps, 3:35:04)。模型已保存到 output/models/contamination_60_uniform_seed42/final。EXIT_CODE=129 (SIGHUP) 发生在训练完成后。WANDB_MODE=disabled 导致 cron 误判为 failed。train_loss=7.649 (avg), train_runti
1374	
1375	  [contamination_60_uniform_seed456] status=DONE conclusion=success
1376	    eval_ppl_holdout: 17.77
1377	    eval_ppl_openwebtext: 18.449
1378	    eval_ppl_wikipedia: 15.42
1379	    train_loss: 7.637
1380	    eval_loss_holdout: 2.8775
1381	    total_steps: 6103
1382	
1383	  [p0_contamination_60_datagen] status=DONE conclusion=success
1384	    q_score_std: 0.3703
1385	
1386	======================================================================
1387	GROUP: epoch_matched  (6 experiments)
1388	======================================================================
1389	
1390	  [epoch_matched_dr_seed123] status=DONE conclusion=success
1391	    eval_ppl_holdout: 17.66
1392	    eval_ppl_openwebtext: 18.3
1393	    eval_ppl_wikitext: 27.9
1394	    eval_loss_holdout: 2.8713
1395	    notes: 失败原因: EXIT_CODE=127 (command not found)，训练在 step ~201/2532 后中断。wall_clock=2321s 但日志仅记录到 ~7min。已派 Worker worker_diagnose_epoch_matched_dr_seed123_20260518T145604 深查。
1396	
1397	  [epoch_matched_dr_seed456] status=DONE conclusion=success
1398	    eval_ppl_holdout: 17.66
1399	    eval_ppl_openwebtext: 18.27
1400	    eval_ppl_wikitext: 28.14
1401	    eval_loss_holdout: 2.8712
1402	
1403	  [eval_epoch_matched_seed123] status=DONE conclusion=success
1404	    perplexity: 17.6599
1405	
1406	  [eval_epoch_matched_seed456] status=DONE conclusion=success
1407	    perplexity: 17.6574
1408	
1409	  [uniform_epoch_matched_indep_lr_seed42] status=DONE conclusion=success
1410	    holdout_ppl: 18.06206
1411	    ood_owt_ppl: 18.64966
1412	    ood_wiki_ppl: 15.511
1413	    total_steps: 2533
1414	
1415	  [uniform_epoch_matched_seed456] status=DONE conclusion=success
1416	    holdout_ppl: 18.068
1417	    train_loss: 8.039
1418	    total_steps: 2533
1419	    owt_ppl: 18.66
1420	    wiki_ppl: 15.515
1421	
1422	======================================================================
1423	GROUP: downstream_eval  (10 experiments)
1424	======================================================================
1425	
1426	  [eval_q01_final] status=PREPARING conclusion=None
1427	    (no metrics)
1428	
1429	  [eval_q01_final_v2] status=DONE conclusion=success
1430	    perplexity: 17.3965
1431	
1432	  [eval_q03_r2] status=DONE conclusion=success
1433	    perplexity: 17.2538
1434	    downstream_arc_challenge_acc_norm: 0.3549
1435	    downstream_arc_easy_acc_norm: 0.6301
1436	    downstream_hellaswag_acc_norm: 0.4851
1437	    downstream_piqa_acc_norm: 0.6872
1438	    downstream_winogrande_acc: 0.5675
1439	
1440	  [eval_q04] status=DONE conclusion=success
1441	    perplexity: 17.2626
1442	    downstream_arc_challenge_acc_norm: 0.3567
1443	    downstream_arc_easy_acc_norm: 0.6107
1444	    downstream_hellaswag_acc_norm: 0.4819
1445	    downstream_piqa_acc_norm: 0.6931
1446	    downstream_winogrande_acc: 0.5659
1447	
1448	  [eval_q06] status=DONE conclusion=success
1449	    perplexity: 17.2993
1450	
1451	  [eval_q07_final] status=DONE conclusion=success
1452	    perplexity: 17.3201
1453	
1454	  [eval_rho06_batch_v5] status=PREPARING conclusion=None
1455	    (no metrics)
1456	
1457	  [eval_rho06_batch_v6] status=PREPARING conclusion=None
1458	    (no metrics)
1459	
1460	  [eval_rho06_batch_v7] status=DONE conclusion=success
1461	    (no metrics)
1462	
1463	  [uniform_seed42_downstream] status=DONE conclusion=success
1464	    downstream_arc_challenge_acc_norm: 0.3481
1465	    downstream_arc_easy_acc_norm: 0.6128
1466	    downstream_hellaswag_acc_norm: 0.4836
1467	    downstream_piqa_acc_norm: 0.6877
1468	    downstream_winogrande_acc: 0.5856
1469	
1470	======================================================================
1471	GROUP: other  (12 experiments)
1472	======================================================================
1473	
1474	  [baseline_qwen3_0.6b] status=DONE conclusion=success
1475	    eval_ppl_holdout: 22.97
1476	    eval_loss: 3.134
1477	    notes: Baseline PPL=22.9654 (loss=3.1340), tokens=4,077,068, time=249s. Weight SHA256=f47f71177f32bcd101b7573ec9171e6a57f4f4d31148d38e382306f42996874b. Pretrained weights confirmed (std ~0.02-0.03, layernorm
1478	
1479	  [datagen_synthetic_4gpu] status=DONE conclusion=success
1480	    (no metrics)
1481	
1482	  [detector_modernbert] status=DONE conclusion=killed
1483	    (no metrics)
1484	    notes: Superseded by TF-IDF detector (detector_tfidf_lr). Never ran — cancelled at QUEUED stage.
1485	
1486	  [detector_tfidf_lr] status=DONE conclusion=success
1487	    q_score_std: 0.374
1488	
1489	  [diagnostic_contamination100] status=DONE conclusion=killed
1490	    (no metrics)
1491	    notes: Director 指令 kill：GPU 2/3 显存打满影响 grid-b seed123 训练速度。诊断实验等 grid-b round 1 完成后重跑。
1492	
1493	  [env_probe_41312] status=PREPARING conclusion=None
1494	    (no metrics)
1495	
1496	  [env_probe_41312_v2] status=PREPARING conclusion=None
1497	    (no metrics)
1498	
1499	  [golden_ratio_seed42] status=DONE conclusion=success
1500	    eval_ppl_holdout: 17.654
1501	    train_loss: 2.1145
1502	    eval_loss: 2.871
1503	    total_steps: 6103
1504	    train_runtime_s: 13442
1505	
1506	  [status_check_41312] status=PREPARING conclusion=None
1507	    (no metrics)
1508	
1509	  [threshold_q03_seed42] status=DONE conclusion=success
1510	    eval_ppl_holdout: 17.253
1511	    eval_loss_holdout: 2.848
1512	    notes: Training completed successfully. 6103/6103 steps, train_loss=11.24, runtime=45076s (~12.5h). Model saved to output/models/threshold_q03_seed42/final (1.19GB safetensors). WANDB_MODE=disabled, offline 
1513	
1514	  [threshold_q07_seed42] status=DONE conclusion=failed
1515	    (no metrics)
1516	    notes: Resume r2 failed: ValueError "Your setup doesn't support bf16/gpu" — all 4x GPUs were occupied by other processes when resume script launched. Training stuck at step 5999, checkpoint-5500 intact. Need
1517	
1518	  [w2_distribution_matching_eval] status=DONE conclusion=negative
1519	    (no metrics)
1520	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2c4bd7c-e61a-4e97-a84c-cf0ff1557937",
  "isSidechain": true,
  "promptId": "c0ee33d1-40a2-4cb8-a0f0-d28fa12f6711",
  "agentId": "a20fa24a4723e1d9c",
  "type": "user",
  "uuid": "90e6f47b-ea5a-4094-999f-78e4b24f5e2e",
  "sourceToolAssistantUUID": "d2c4bd7c-e61a-4e97-a84c-cf0ff1557937",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "8eaa3b36-4b2e-4596-a917-3c8550c7e172",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-24T04:31:09.179Z_

Now let me get the remaining experiments not yet captured and compute the statistical summaries:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90e6f47b-ea5a-4094-999f-78e4b24f5e2e",
  "isSidechain": true,
  "agentId": "a20fa24a4723e1d9c",
  "requestId": "req_011CbLmQ5ZfWD9CYLNT6jTcs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d36f402c-4ca8-4e31-b875-adaad5aa64e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "8eaa3b36-4b2e-4596-a917-3c8550c7e172",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NAwY3aWa4p6ZZULqqYk3FW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24529,
      "cache_read_input_tokens": 25668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24529,
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

_source line 19 · 2026-05-24T04:32:21.362Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01VgV6zHdjy9jpFaV6q2r9MG`</summary>

```json
{
  "command": "python3 - <<'PYEOF'\nimport json\n\nfpath = \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/8eaa3b36-4b2e-4596-a917-3c8550c7e172/tool-results/mcp-agent-ml-research-read_registry-1779596942026.txt\"\n\nwith open(fpath) as f:\n    outer = json.load(f)\n\nregistry = json.loads(outer[\"result\"])\nexperiments = registry[\"data\"][\"experiments\"]\n\n# Print remaining experiments not covered by the groups above\n# Specifically: rho groups with adaptive_rho06, rho06_tau07 (some had no metrics above), \n# and some other experiments. Let's look at the ones not yet categorized or with unusual structures.\n\n# Focus on computing statistical summaries for key cross-comparisons\n\nprint(\"=\"*70)\nprint(\"STATISTICAL SUMMARIES FOR KEY EXPERIMENT GROUPS\")\nprint(\"=\"*70)\n\n# 1. Adaptive b* (main, rho=0.4, tau=0.8, n_min=2) - canonical 3-seed\nprint(\"\\n--- Canonical Adaptive b* (rho=0.4, tau=0.8, n_min=2) ---\")\nadaptive_seeds = {\n    \"seed42\": experiments[\"adaptive_fix_seed42\"][\"metrics\"].get(\"eval_ppl_holdout\"),\n    \"seed123\": experiments[\"adaptive_fix_seed123\"][\"metrics\"].get(\"eval_ppl_holdout\"),\n    \"seed456\": experiments[\"adaptive_fix_seed456\"][\"metrics\"].get(\"eval_ppl_holdout\"),\n}\nvals = list(adaptive_seeds.values())\nimport statistics\nprint(f\"  PPLs: seed42={vals[0]}, seed123={vals[1]}, seed456={vals[2]}\")\nprint(f\"  Mean: {statistics.mean(vals):.4f}, Std: {statistics.stdev(vals):.4f}\")\n\n# 2. Uniform (rho=0.4) - canonical 3-seed\nprint(\"\\n--- Canonical Uniform (rho=0.4) ---\")\nuniform_seeds = {\n    \"seed42\": experiments[\"uniform_seed42\"][\"metrics\"].get(\"eval_ppl_holdout\"),\n    \"seed123\": experiments[\"uniform_seed123\"][\"metrics\"].get(\"eval_ppl_holdout\"),\n    \"seed456\": experiments[\"uniform_seed456\"][\"metrics\"].get(\"eval_ppl_holdout\"),\n}\nvals_u = list(uniform_seeds.values())\nprint(f\"  PPLs: seed42={vals_u[0]}, seed123={vals_u[1]}, seed456={vals_u[2]}\")\nprint(f\"  Mean: {statistics.mean(vals_u):.4f}, Std: {statistics.stdev(vals_u):.4f}\")\n\n# 3. ESS-only - 3-seed canonical (use _r2 for seeds that were rerun)\nprint(\"\\n--- ESS-Only (3-seed canonical) ---\")\ness = {\n    \"seed42\": experiments[\"ess_only_seed42\"][\"metrics\"].get(\"eval_ppl\", experiments[\"ess_only_seed42\"][\"metrics\"].get(\"eval_ppl_holdout\")),\n    \"seed123\": experiments[\"ess_only_seed123_r2\"][\"metrics\"].get(\"eval_ppl_holdout\"),\n    \"seed456\": experiments[\"ess_only_seed456_r2\"][\"metrics\"].get(\"eval_ppl_holdout\"),\n}\nvals_e = list(ess.values())\nprint(f\"  PPLs: seed42={vals_e[0]}, seed123={vals_e[1]}, seed456={vals_e[2]}\")\nprint(f\"  Mean: {statistics.mean(vals_e):.4f}, Std: {statistics.stdev(vals_e):.4f}\")\n\n# 4. aeff_only (nmin=1, so ESS disabled) - 3-seed\nprint(\"\\n--- α_eff-Only (n_min=1, ESS disabled) ---\")\naeff = {\n    \"seed42\": experiments[\"aeff_only_nmin1_seed42\"][\"metrics\"].get(\"holdout_ppl\"),\n    \"seed123\": experiments[\"aeff_only_nmin1_seed123\"][\"metrics\"].get(\"holdout_ppl\"),\n    \"seed456\": experiments[\"aeff_only_nmin1_seed456\"][\"metrics\"].get(\"holdout_ppl\"),\n}\nvals_a = list(aeff.values())\nprint(f\"  PPLs: seed42={vals_a[0]}, seed123={vals_a[1]}, seed456={vals_a[2]}\")\nprint(f\"  Mean: {statistics.mean(vals_a):.4f}, Std: {statistics.stdev(vals_a):.4f}\")\n\n# 5. Random reweight - canonical runs\nprint(\"\\n--- Random Reweight ---\")\nrr = {\n    \"seed42 (v2)\": experiments[\"random_reweight_v2_seed42\"][\"metrics\"].get(\"eval_ppl_holdout\"),\n    \"seed123 (r5)\": experiments[\"random_reweight_seed123_r5\"][\"metrics\"].get(\"eval_ppl_holdout\"),\n    \"seed456\": experiments[\"random_reweight_seed456\"][\"metrics\"].get(\"eval_ppl_holdout\"),\n}\nvals_r = [v for v in rr.values() if v is not None]\nprint(f\"  PPLs: {rr}\")\nif len(vals_r) >= 2:\n    print(f\"  Mean: {statistics.mean(vals_r):.4f}, Std: {statistics.stdev(vals_r):.4f}\")\n\n# 6. D&R q=0.05 - canonical 3-seed\nprint(\"\\n--- Detect & Remove q=0.05 (canonical) ---\")\ndr_q05 = {\n    \"seed42 (v2)\": experiments[\"detect_remove_q05_v2_seed42\"][\"metrics\"].get(\"holdout_ppl\"),\n    \"seed123 (v2_r2)\": experiments[\"detect_remove_q05_v2_seed123_r2\"][\"metrics\"].get(\"holdout_ppl\"),\n    \"seed456 (v2)\": experiments[\"detect_remove_q05_v2_seed456\"][\"metrics\"].get(\"holdout_ppl\"),\n}\nvals_dr = list(dr_q05.values())\nprint(f\"  PPLs: seed42={vals_dr[0]}, seed123={vals_dr[1]}, seed456={vals_dr[2]}\")\nprint(f\"  Mean: {statistics.mean(vals_dr):.4f}, Std: {statistics.stdev(vals_dr):.4f}\")\n\n# 7. D&R q=0.03 - canonical 3-seed\nprint(\"\\n--- Detect & Remove q=0.03 (canonical) ---\")\ndr_q03 = {\n    \"seed42\": experiments[\"detect_remove_q03_seed42_r2\"][\"metrics\"].get(\"eval_ppl_holdout\"),\n    \"seed123\": experiments[\"detect_remove_q03_seed123\"][\"metrics\"].get(\"eval_ppl_holdout\"),\n    \"seed456\": experiments[\"detect_remove_q03_seed456\"][\"metrics\"].get(\"eval_ppl_holdout\"),\n}\nvals_dr3 = list(dr_q03.values())\nprint(f\"  PPLs: seed42={vals_dr3[0]}, seed123={vals_dr3[1]}, seed456={vals_dr3[2]}\")\nprint(f\"  Mean: {statistics.mean(vals_dr3):.4f}, Std: {statistics.stdev(vals_dr3):.4f}\")\n\n# 8. BS=8 n_min=4 adaptive vs uniform\nprint(\"\\n--- BS=8, n_min=4 Adaptive (3-seed) ---\")\nbs8a = {\n    \"seed42\": experiments[\"bs8_nmin4_adaptive_seed42\"][\"metrics\"].get(\"holdout_ppl\"),\n    \"seed123\": experiments[\"bs8_nmin4_adaptive_seed123_r2\"][\"metrics\"].get(\"eval_ppl_holdout\"),\n    \"seed456\": experiments[\"bs8_nmin4_adaptive_seed456_r2\"][\"metrics\"].get(\"holdout_ppl\"),\n}\nvals_bs8a = list(bs8a.values())\nprint(f\"  PPLs: seed42={vals_bs8a[0]:.4f}, seed123={vals_bs8a[1]}, seed456={vals_bs8a[2]}\")\nif all(v is not None for v in vals_bs8a):\n    print(f\"  Mean: {statistics.mean(vals_bs8a):.4f}, Std: {statistics.stdev(vals_bs8a):.4f}\")\n\nprint(\"\\n--- BS=8, n_min=4 Uniform (3-seed) ---\")\nbs8u = {\n    \"seed42\": experiments[\"bs8_nmin4_uniform_seed42\"][\"metrics\"].get(\"holdout_ppl\"),\n    \"seed123\": experiments[\"bs8_nmin4_uniform_seed123_r2\"][\"metrics\"].get(\"eval_ppl_holdout\"),\n    \"seed456\": experiments[\"bs8_nmin4_uniform_seed456_r2\"][\"metrics\"].get(\"holdout_ppl\"),\n}\nvals_bs8u = list(bs8u.values())\nprint(f\"  PPLs: seed42={vals_bs8u[0]:.4f}, seed123={vals_bs8u[1]}, seed456={vals_bs8u[2]}\")\nif all(v is not None for v in vals_bs8u):\n    print(f\"  Mean: {statistics.mean(vals_bs8u):.4f}, Std: {statistics.stdev(vals_bs8u):.4f}\")\n\n# 9. BS=16 adaptive vs uniform\nprint(\"\\n--- BS=16, tau=0.7 Adaptive (3-seed) ---\")\nbs16a = {\n    \"seed42\": experiments[\"bs16_adaptive_tau07_seed42\"][\"metrics\"].get(\"holdout_ppl\"),\n    \"seed123\": experiments[\"bs16_adaptive_tau07_seed123_r2\"][\"metrics\"].get(\"holdout_ppl\"),\n    \"seed456\": experiments[\"bs16_adaptive_tau07_seed456\"][\"metrics\"].get(\"holdout_ppl\"),\n}\nvals_bs16a = list(bs16a.values())\nprint(f\"  PPLs: seed42={vals_bs16a[0]}, seed123={vals_bs16a[1]}, seed456={vals_bs16a[2]}\")\nprint(f\"  Mean: {statistics.mean(vals_bs16a):.4f}, Std: {statistics.stdev(vals_bs16a):.4f}\")\n\nprint(\"\\n--- BS=16 Uniform (3-seed) ---\")\nbs16u = {\n    \"seed42\": experiments[\"bs16_uniform_seed42\"][\"metrics\"].get(\"holdout_ppl\"),\n    \"seed123\": experiments[\"bs16_uniform_seed123\"][\"metrics\"].get(\"holdout_ppl\"),\n    \"seed456\": experiments[\"bs16_uniform_seed456\"][\"metrics\"].get(\"holdout_ppl\"),\n}\nvals_bs16u = list(bs16u.values())\nprint(f\"  PPLs: seed42={vals_bs16u[0]}, seed123={vals_bs16u[1]}, seed456={vals_bs16u[2]}\")\nprint(f\"  Mean: {statistics.mean(vals_bs16u):.4f}, Std: {statistics.stdev(vals_bs16u):.4f}\")\n\n# 10. rho=0.2 \nprint(\"\\n--- rho=0.2 Adaptive (tau=0.8) vs Uniform ---\")\nprint(f\"  Adaptive: {experiments['rho02_adaptive_tau08_seed42']['metrics'].get('eval_ppl_holdout')}\")\nprint(f\"  Uniform: {experiments['rho02_uniform_seed42']['metrics'].get('eval_ppl_holdout')}\")\n\n# 11. rho=0.3 adaptive (3-seed) vs uniform (3-seed)\nprint(\"\\n--- rho=0.3 Adaptive (3-seed) ---\")\nrho03a = {\n    \"seed42\": experiments[\"rho03_adaptive_seed42\"][\"metrics\"].get(\"eval_ppl_holdout\"),\n    \"seed123\": experiments[\"rho03_adaptive_seed123\"][\"metrics\"].get(\"eval_ppl_holdout\"),\n    \"seed456\": experiments[\"rho03_adaptive_seed456_r2\"][\"metrics\"].get(\"eval_ppl_holdout\"),\n}\nvals_rho03a = list(rho03a.values())\nprint(f\"  PPLs: seed42={vals_rho03a[0]}, seed123={vals_rho03a[1]}, seed456={vals_rho03a[2]}\")\nprint(f\"  Mean: {statistics.mean(vals_rho03a):.4f}, Std: {statistics.stdev(vals_rho03a):.4f}\")\n\nprint(\"\\n--- rho=0.3 Uniform (3-seed) ---\")\nrho03u = {\n    \"seed42\": experiments[\"rho03_uniform_seed42\"][\"metrics\"].get(\"eval_ppl_holdout\"),\n    \"seed123\": experiments[\"rho03_uniform_seed123\"][\"metrics\"].get(\"eval_ppl_holdout\"),\n    \"seed456\": experiments[\"rho03_uniform_seed456\"][\"metrics\"].get(\"eval_ppl_holdout\"),\n}\nvals_rho03u = list(rho03u.values())\nprint(f\"  PPLs: seed42={vals_rho03u[0]}, seed123={vals_rho03u[1]}, seed456={vals_rho03u[2]}\")\nprint(f\"  Mean: {statistics.mean(vals_rho03u):.4f}, Std: {statistics.stdev(vals_rho03u):.4f}\")\n\n# 12. rho=0.6 \nprint(\"\\n--- rho=0.6 (contamination 60%) Adaptive (tau=0.8) ---\")\nrho06a = {\n    \"seed42\": experiments[\"contamination_60_seed42_r2\"][\"metrics\"].get(\"eval_ppl_holdout\"),\n    \"seed123\": experiments[\"contamination_60_seed123\"][\"metrics\"].get(\"eval_ppl_holdout\"),\n    \"seed456\": experiments[\"contamination_60_adaptive_seed456\"][\"metrics\"].get(\"eval_ppl_holdout\"),\n}\nvals_rho06a = list(rho06a.values())\nprint(f\"  PPLs: seed42={vals_rho06a[0]}, seed123={vals_rho06a[1]}, seed456={vals_rho06a[2]}\")\nprint(f\"  Mean: {statistics.mean(vals_rho06a):.4f}, Std: {statistics.stdev(vals_rho06a):.4f}\")\n\nprint(\"\\n--- rho=0.6 Uniform (3-seed) ---\")\nrho06u = {\n    \"seed42\": experiments[\"contamination_60_uniform_seed42\"][\"metrics\"].get(\"eval_ppl_holdout\"),\n    \"seed123\": experiments[\"contamination_60_uniform_seed123\"][\"metrics\"].get(\"eval_ppl_holdout\"),\n    \"seed456\": experiments[\"contamination_60_uniform_seed456\"][\"metrics\"].get(\"eval_ppl_holdout\"),\n}\nvals_rho06u = list(rho06u.values())\nprint(f\"  PPLs: seed42={vals_rho06u[0]}, seed123={vals_rho06u[1]}, seed456={vals_rho06u[2]}\")\nprint(f\"  Mean: {statistics.mean(vals_rho06u):.4f}, Std: {statistics.stdev(vals_rho06u):.4f}\")\n\n# 13. n_min sensitivity (single-seed)\nprint(\"\\n--- n_min Sensitivity (seed42, rho=0.4, tau=0.8) ---\")\nprint(f\"  n_min=1: {experiments['nmin1_seed42']['metrics'].get('eval_ppl_holdout')}\")\nprint(f\"  n_min=2 (adaptive_fix_seed42): {experiments['adaptive_fix_seed42']['metrics'].get('eval_ppl_holdout')}\")\nprint(f\"  n_min=3 (adaptive_seed42): {experiments['adaptive_seed42']['metrics'].get('eval_ppl_holdout')}\")\nprint(f\"  n_min=4: {experiments['nmin4_seed42']['metrics'].get('eval_ppl_holdout')}\")\n\n# 14. tau sensitivity (seed42)\nprint(\"\\n--- Tau Sensitivity (seed42, rho=0.4) ---\")\nprint(f\"  tau=0.5: {experiments['tau_05_seed42']['metrics'].get('eval_ppl_holdout')}\")\nprint(f\"  tau=0.6: {experiments['tau_06_seed42']['metrics'].get('eval_ppl_holdout')}\")\nprint(f\"  tau=0.7 (tau07_seed42): {experiments['tau07_seed42']['metrics'].get('eval_ppl_holdout')}\")\nprint(f\"  tau=0.8 (adaptive_fix_seed42): {experiments['adaptive_fix_seed42']['metrics'].get('eval_ppl_holdout')}\")\nprint(f\"  tau=0.9: {experiments['tau_09_seed42']['metrics'].get('eval_ppl_holdout')}\")\nprint(f\"  tau=0.95: {experiments['tau_095_seed42']['metrics'].get('eval_ppl_holdout')}\")\n\n# 15. tau sensitivity - 3-seed for tau=0.7 and rho=0.6 tau=0.7\nprint(\"\\n--- Tau=0.7 (rho=0.4) 3-seed ---\")\ntau07 = {\n    \"seed42\": experiments[\"tau07_seed42\"][\"metrics\"].get(\"eval_ppl_holdout\"),\n    \"seed123\": experiments[\"tau07_seed123\"][\"metrics\"].get(\"eval_ppl_holdout\"),\n    \"seed456\": experiments[\"tau07_seed456\"][\"metrics\"].get(\"eval_ppl_holdout\"),\n}\nvals_tau07 = list(tau07.values())\nprint(f\"  PPLs: seed42={vals_tau07[0]}, seed123={vals_tau07[1]}, seed456={vals_tau07[2]}\")\nprint(f\"  Mean: {statistics.mean(vals_tau07):.4f}, Std: {statistics.stdev(vals_tau07):.4f}\")\n\n# 16. 1.7B scale\nprint(\"\\n--- 1.7B Scale ---\")\nprint(f\"  Adaptive seed42 (v5): {experiments['adaptive_1_7b_seed42_v5']['metrics'].get('eval_ppl_holdout')}\")\nprint(f\"  Adaptive seed123: {experiments['adaptive_1_7b_seed123']['metrics'].get('eval_ppl_holdout')}\")\nprint(f\"  Adaptive seed456: {experiments['adaptive_1_7b_seed456']['metrics'].get('eval_ppl_holdout')}\")\nprint(f\"  Uniform seed42 (v5): {experiments['uniform_1_7b_seed42_v5']['metrics'].get('eval_ppl_holdout')}\")\nprint(f\"  Uniform seed123: {experiments['uniform_1_7b_seed123']['metrics'].get('eval_ppl_holdout')}\")\nprint(f\"  Uniform seed456: {experiments['uniform_1_7b_seed456']['metrics'].get('eval_ppl_holdout')}\")\n\n# Mean/std for 1.7B\na1_7b = [experiments['adaptive_1_7b_seed42_v5']['metrics'].get('eval_ppl_holdout'),\n          experiments['adaptive_1_7b_seed123']['metrics'].get('eval_ppl_holdout'),\n          experiments['adaptive_1_7b_seed456']['metrics'].get('eval_ppl_holdout')]\nu1_7b = [experiments['uniform_1_7b_seed42_v5']['metrics'].get('eval_ppl_holdout'),\n          experiments['uniform_1_7b_seed123']['metrics'].get('eval_ppl_holdout'),\n          experiments['uniform_1_7b_seed456']['metrics'].get('eval_ppl_holdout')]\nprint(f\"  Adaptive Mean: {statistics.mean(a1_7b):.4f}, Std: {statistics.stdev(a1_7b):.4f}\")\nprint(f\"  Uniform Mean: {statistics.mean(u1_7b):.4f}, Std: {statistics.stdev(u1_7b):.4f}\")\n\n# 17. Detector comparison\nprint(\"\\n--- Detector Comparison (Adaptive training, 3-seed canonical where available) ---\")\nprint(\"  N-gram detector (our q score):\")\nngram_a = {\n    \"seed42\": experiments[\"ngram_adaptive_seed42\"][\"metrics\"].get(\"holdout_ppl\"),\n    \"seed123\": experiments[\"ngram_adaptive_seed123\"][\"metrics\"].get(\"eval_ppl_holdout\"),\n    \"seed456\": experiments[\"ngram_adaptive_seed456_v2\"][\"metrics\"].get(\"holdout_ppl\"),\n}\nprint(f\"    PPLs: {ngram_a}\")\nvals_ngram = [v for v in ngram_a.values() if v is not None]\nprint(f\"    Mean: {statistics.mean(vals_ngram):.4f}, Std: {statistics.stdev(vals_ngram):.4f}\")\n\nprint(\"  GPT-2 detector:\")\ngpt2_a = {\n    \"seed42\": experiments[\"gpt2_adaptive_seed42\"][\"metrics\"].get(\"eval_ppl_holdout\"),\n    \"seed123\": experiments[\"gpt2_adaptive_seed123_v3\"][\"metrics\"].get(\"holdout_ppl\"),\n    \"seed456\": experiments[\"gpt2_adaptive_seed456_v2\"][\"metrics\"].get(\"holdout_ppl\"),\n}\nprint(f\"    PPLs: {gpt2_a}\")\nvals_gpt2 = [v for v in gpt2_a.values() if v is not None]\nprint(f\"    Mean: {statistics.mean(vals_gpt2):.4f}, Std: {statistics.stdev(vals_gpt2):.4f}\")\n\n# 18. OOD eval summary\nprint(\"\\n--- OOD Evaluation (adaptive vs uniform, rho=0.4) ---\")\nprint(\"  Adaptive OOD (seed123):\")\nm = experiments[\"adaptive_ood_seed123\"][\"metrics\"]\nprint(f\"    holdout={m.get('eval_ppl_holdout')}, OWT={m.get('eval_ppl_openwebtext')}, Wiki={m.get('eval_ppl_wikipedia')}\")\nprint(\"  Adaptive OOD (seed456):\")\nm = experiments[\"adaptive_ood_seed456\"][\"metrics\"]\nprint(f\"    holdout={m.get('eval_ppl_holdout')}, OWT={m.get('eval_ppl_openwebtext')}, Wiki={m.get('eval_ppl_wikipedia')}\")\nprint(\"  Uniform OOD (seed123):\")\nm = experiments[\"uniform_ood_seed123\"][\"metrics\"]\nprint(f\"    holdout={m.get('eval_ppl_holdout')}, OWT={m.get('eval_ppl_openwebtext')}, Wiki={m.get('eval_ppl_wikipedia')}\")\nprint(\"  Uniform OOD (seed456):\")\nm = experiments[\"uniform_ood_seed456\"][\"metrics\"]\nprint(f\"    holdout={m.get('eval_ppl_holdout')}, OWT={m.get('eval_ppl_openwebtext')}, Wiki={m.get('eval_ppl_wikipedia')}\")\n\n# 19. Grid search best b across seeds\nprint(\"\\n--- Grid Search b values (seed123 + seed456, 2-seed) ---\")\ngrid_b = {\n    \"b=0.1\": [(experiments[\"grid_b0_1_seed123\"][\"metrics\"].get(\"eval_ppl_holdout\"), \"s123\"),\n               (experiments[\"grid_b0_1_seed456\"][\"metrics\"].get(\"eval_ppl_holdout\"), \"s456\")],\n    \"b=0.2\": [(experiments[\"grid_b0_2_seed123\"][\"metrics\"].get(\"eval_ppl_holdout\"), \"s123\"),\n               (experiments[\"grid_b0_2_seed456\"][\"metrics\"].get(\"eval_ppl_holdout\"), \"s456\")],\n    \"b=0.3\": [(experiments[\"grid_b0_3_seed123_r2\"][\"metrics\"].get(\"eval_ppl_holdout\"), \"s123\"),\n               (experiments[\"grid_b0_3_seed456_r2\"][\"metrics\"].get(\"eval_ppl_holdout\"), \"s456\")],\n    \"b=0.5\": [(experiments[\"grid_b0_5_seed123\"][\"metrics\"].get(\"eval_ppl_holdout\"), \"s123\"),\n               (experiments[\"grid_b0_5_seed456\"][\"metrics\"].get(\"eval_ppl_holdout\"), \"s456\")],\n    \"b=1.0\": [(experiments[\"grid_b1_0_seed123\"][\"metrics\"].get(\"eval_ppl_holdout\"), \"s123\"),\n               (experiments[\"grid_b1_0_seed456\"][\"metrics\"].get(\"eval_ppl_holdout\"), \"s456\")],\n    \"b=1.5\": [(experiments[\"grid_b1_5_seed123\"][\"metrics\"].get(\"eval_ppl_holdout\"), \"s123\"),\n               (experiments[\"grid_b1_5_seed456\"][\"metrics\"].get(\"eval_ppl_holdout\"), \"s456\")],\n    \"b=2.0\": [(experiments[\"grid_b2_0_seed123\"][\"metrics\"].get(\"eval_ppl_holdout\"), \"s123\"),\n               (experiments[\"grid_b2_0_seed456\"][\"metrics\"].get(\"eval_ppl_holdout\"), \"s456\")],\n    \"b=3.0\": [(experiments[\"grid_b3_0_seed123\"][\"metrics\"].get(\"eval_ppl_holdout\"), \"s123\"),\n               (experiments[\"grid_b3_0_seed456\"][\"metrics\"].get(\"eval_ppl_holdout\"), \"s456\")],\n    \"b=5.0\": [(experiments[\"grid_b5_0_seed123\"][\"metrics\"].get(\"eval_ppl_holdout\"), \"s123\"),\n               (experiments[\"grid_b5_0_seed456\"][\"metrics\"].get(\"eval_ppl_holdout\"), \"s456\")],\n}\nfor b, pairs in grid_b.items():\n    ppls = [p[0] for p in pairs if p[0] is not None]\n    seeds = [p[1] for p in pairs]\n    mean = statistics.mean(ppls) if len(ppls) > 1 else ppls[0]\n    print(f\"  {b}: s123={pairs[0][0]}, s456={pairs[1][0]}, mean={mean:.4f}\")\n\n# 20. epoch-matched comparisons\nprint(\"\\n--- Epoch-Matched D&R (content-epoch = 1) ---\")\nprint(f\"  D&R q=0.05 epoch-matched seed42: {experiments['detect_remove_q05_epoch_matched_seed42']['metrics'].get('eval_ppl_holdout')}\")\nprint(f\"  D&R q=0.07 epoch-matched seed42: {experiments['detect_remove_q07_epoch_matched_seed42']['metrics'].get('eval_ppl_holdout')}\")\nprint(f\"  D&R q=0.09 epoch-matched seed42: {experiments['detect_remove_q09_epoch_matched_seed42']['metrics'].get('eval_ppl_holdout')}\")\nprint(f\"  D&R q=0.01 epoch-matched seed42: {experiments['detect_remove_q01_epoch_matched_seed42']['metrics'].get('eval_ppl_holdout')}\")\nprint(f\"  D&R q=0.03 epoch-matched seed42: {experiments['detect_remove_q03_epoch_matched_seed42']['metrics'].get('eval_ppl_holdout')}\")\n# epoch-matched D&R multiSeed \nprint(f\"  D&R epoch-matched (v2_indep_lr) seed42: {experiments['dr_epoch_matched_indep_lr_v2_seed42']['metrics'].get('holdout_ppl')}\")\nprint(f\"  D&R epoch-matched seed123 (r2): {experiments['dr_epoch_matched_seed123_r2']['metrics'].get('holdout_ppl')}\")\nprint(f\"  D&R epoch-matched seed456: {experiments['dr_epoch_matched_seed456']['metrics'].get('holdout_ppl')}\")\nprint(f\"  Epoch-matched D&R seed123: {experiments['epoch_matched_dr_seed123']['metrics'].get('eval_ppl_holdout')}\")\nprint(f\"  Epoch-matched D&R seed456: {experiments['epoch_matched_dr_seed456']['metrics'].get('eval_ppl_holdout')}\")\nprint(f\"  Adaptive (full, same steps): 17.644 (adaptive_fix_seed42)\")\nprint(f\"  Uniform epoch-matched seed42: {experiments['uniform_epoch_matched_indep_lr_seed42']['metrics'].get('holdout_ppl')}\")\nprint(f\"  Uniform epoch-matched seed456: {experiments['uniform_epoch_matched_seed456']['metrics'].get('holdout_ppl')}\")\n\nPYEOF\n",
  "description": "Compute statistical summaries for all key experiment groups"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d36f402c-4ca8-4e31-b875-adaad5aa64e1",
  "isSidechain": true,
  "agentId": "a20fa24a4723e1d9c",
  "requestId": "req_011CbLmQ5ZfWD9CYLNT6jTcs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f347b3e-4f7d-4f94-b606-a3652be0f6ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "8eaa3b36-4b2e-4596-a917-3c8550c7e172",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NAwY3aWa4p6ZZULqqYk3FW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24529,
      "cache_read_input_tokens": 25668,
      "output_tokens": 7472,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 24529
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7472,
          "cache_read_input_tokens": 25668,
          "cache_creation_input_tokens": 24529,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 24529,
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

_source line 20 · 2026-05-24T04:32:21.526Z_

<details><summary>↩ Tool result · `toolu_01VgV6zHdjy9jpFaV6q2r9MG`</summary>

```text
======================================================================
STATISTICAL SUMMARIES FOR KEY EXPERIMENT GROUPS
======================================================================

--- Canonical Adaptive b* (rho=0.4, tau=0.8, n_min=2) ---
  PPLs: seed42=17.6527, seed123=17.6432, seed456=17.6566
  Mean: 17.6508, Std: 0.0069

--- Canonical Uniform (rho=0.4) ---
  PPLs: seed42=17.6939, seed123=17.6861, seed456=17.7015
  Mean: 17.6938, Std: 0.0077

--- ESS-Only (3-seed canonical) ---
  PPLs: seed42=17.73, seed123=17.721, seed456=17.762
  Mean: 17.7377, Std: 0.0215

--- α_eff-Only (n_min=1, ESS disabled) ---
  PPLs: seed42=17.75, seed123=17.733, seed456=17.744
  Mean: 17.7423, Std: 0.0086

--- Random Reweight ---
  PPLs: {'seed42 (v2)': 17.83, 'seed123 (r5)': 17.8, 'seed456': 17.777}
  Mean: 17.8023, Std: 0.0266

--- Detect & Remove q=0.05 (canonical) ---
  PPLs: seed42=17.2853, seed123=17.272, seed456=17.277
  Mean: 17.2781, Std: 0.0067

--- Detect & Remove q=0.03 (canonical) ---
  PPLs: seed42=17.25, seed123=17.25, seed456=17.2509
  Mean: 17.2503, Std: 0.0005

--- BS=8, n_min=4 Adaptive (3-seed) ---
  PPLs: seed42=17.6504, seed123=17.631, seed456=17.646
  Mean: 17.6425, Std: 0.0102

--- BS=8, n_min=4 Uniform (3-seed) ---
  PPLs: seed42=17.6942, seed123=17.687, seed456=17.702
  Mean: 17.6944, Std: 0.0075

--- BS=16, tau=0.7 Adaptive (3-seed) ---
  PPLs: seed42=17.631, seed123=17.616, seed456=17.645
  Mean: 17.6307, Std: 0.0145

--- BS=16 Uniform (3-seed) ---
  PPLs: seed42=17.694, seed123=17.686, seed456=17.717
  Mean: 17.6990, Std: 0.0161

--- rho=0.2 Adaptive (tau=0.8) vs Uniform ---
  Adaptive: 17.382
  Uniform: 17.336

--- rho=0.3 Adaptive (3-seed) ---
  PPLs: seed42=17.422, seed123=17.435, seed456=17.424
  Mean: 17.4270, Std: 0.0070

--- rho=0.3 Uniform (3-seed) ---
  PPLs: seed42=17.422, seed123=17.433, seed456=17.419
  Mean: 17.4247, Std: 0.0074

--- rho=0.6 (contamination 60%) Adaptive (tau=0.8) ---
  PPLs: seed42=17.74, seed123=17.732, seed456=17.735
  Mean: 17.7357, Std: 0.0040

--- rho=0.6 Uniform (3-seed) ---
  PPLs: seed42=17.766, seed123=17.754, seed456=17.77
  Mean: 17.7633, Std: 0.0083

--- n_min Sensitivity (seed42, rho=0.4, tau=0.8) ---
  n_min=1: 17.789
  n_min=2 (adaptive_fix_seed42): 17.6527
  n_min=3 (adaptive_seed42): 17.644
  n_min=4: 17.6947

--- Tau Sensitivity (seed42, rho=0.4) ---
  tau=0.5: 17.688
  tau=0.6: 17.6805
  tau=0.7 (tau07_seed42): 17.68
  tau=0.8 (adaptive_fix_seed42): 17.6527
  tau=0.9: 17.712
  tau=0.95: 17.723

--- Tau=0.7 (rho=0.4) 3-seed ---
  PPLs: seed42=17.68, seed123=17.666, seed456=17.677
  Mean: 17.6743, Std: 0.0074

--- 1.7B Scale ---
  Adaptive seed42 (v5): 13.27
  Adaptive seed123: 13.25
  Adaptive seed456: 13.2668
  Uniform seed42 (v5): 13.28
  Uniform seed123: 13.2648
  Uniform seed456: 13.28
  Adaptive Mean: 13.2623, Std: 0.0107
  Uniform Mean: 13.2749, Std: 0.0088

--- Detector Comparison (Adaptive training, 3-seed canonical where available) ---
  N-gram detector (our q score):
    PPLs: {'seed42': 17.820214, 'seed123': 17.823, 'seed456': 17.82607}
    Mean: 17.8231, Std: 0.0029
  GPT-2 detector:
    PPLs: {'seed42': 17.79, 'seed123': 17.78848, 'seed456': 17.79719}
    Mean: 17.7919, Std: 0.0047

--- OOD Evaluation (adaptive vs uniform, rho=0.4) ---
  Adaptive OOD (seed123):
    holdout=17.677, OWT=18.373, Wiki=15.37
  Adaptive OOD (seed456):
    holdout=17.683, OWT=18.366, Wiki=15.345
  Uniform OOD (seed123):
    holdout=17.6861, OWT=18.3678, Wiki=15.3768
  Uniform OOD (seed456):
    holdout=17.7015, OWT=18.3865, Wiki=15.3594

--- Grid Search b values (seed123 + seed456, 2-seed) ---
  b=0.1: s123=17.646, s456=17.663, mean=17.6545
  b=0.2: s123=17.637, s456=17.645, mean=17.6410
  b=0.3: s123=17.5792, s456=17.64, mean=17.6096
  b=0.5: s123=17.638, s456=17.65, mean=17.6440
  b=1.0: s123=17.674, s456=17.68, mean=17.6770
  b=1.5: s123=17.701, s456=17.71, mean=17.7055
  b=2.0: s123=17.725, s456=17.989, mean=17.8570
  b=3.0: s123=17.76, s456=17.921, mean=17.8405
  b=5.0: s123=17.8039, s456=17.993, mean=17.8984

--- Epoch-Matched D&R (content-epoch = 1) ---
  D&R q=0.05 epoch-matched seed42: 17.65
  D&R q=0.07 epoch-matched seed42: 17.62
  D&R q=0.09 epoch-matched seed42: 17.628
  D&R q=0.01 epoch-matched seed42: 18.0436
  D&R q=0.03 epoch-matched seed42: 17.74
  D&R epoch-matched (v2_indep_lr) seed42: 17.65053
  D&R epoch-matched seed123 (r2): 17.6591
  D&R epoch-matched seed456: 17.66
  Epoch-matched D&R seed123: 17.66
  Epoch-matched D&R seed456: 17.66
  Adaptive (full, same steps): 17.644 (adaptive_fix_seed42)
  Uniform epoch-matched seed42: 18.06206
  Uniform epoch-matched seed456: 18.068
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f347b3e-4f7d-4f94-b606-a3652be0f6ad",
  "isSidechain": true,
  "promptId": "c0ee33d1-40a2-4cb8-a0f0-d28fa12f6711",
  "agentId": "a20fa24a4723e1d9c",
  "type": "user",
  "uuid": "457c1659-1580-4602-b541-e4cd6de685ca",
  "sourceToolAssistantUUID": "5f347b3e-4f7d-4f94-b606-a3652be0f6ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "8eaa3b36-4b2e-4596-a917-3c8550c7e172",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-24T04:32:53.976Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01ELQNjbY8emGbgFQawqPVZS`</summary>

```json
{
  "command": "python3 - <<'PYEOF'\nimport json, statistics\n\nfpath = \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/8eaa3b36-4b2e-4596-a917-3c8550c7e172/tool-results/mcp-agent-ml-research-read_registry-1779596942026.txt\"\n\nwith open(fpath) as f:\n    outer = json.load(f)\n\nregistry = json.loads(outer[\"result\"])\nexperiments = registry[\"data\"][\"experiments\"]\n\n# Look at any experiments with p-value, delta-related stored comparisons\nprint(\"=== Experiments with stored delta / p-value fields ===\")\nfor eid, e in sorted(experiments.items()):\n    m = e.get(\"metrics\", {})\n    delta_keys = {k: v for k, v in m.items() if any(x in k for x in [\"delta\", \"p_value\", \"pvalue\", \"vs_\", \"p-value\"])}\n    if delta_keys:\n        print(f\"\\n[{eid}]\")\n        for k, v in delta_keys.items():\n            print(f\"  {k}: {v}\")\n\nprint(\"\\n\\n=== D&R full-data single-seed scan (all q thresholds, seed42) ===\")\ndr_eids = [(eid, e) for eid, e in experiments.items() if \"detect_remove_q\" in eid and \"seed42\" in eid and \"epoch_matched\" not in eid and e.get(\"status\") == \"DONE\"]\nfor eid, e in sorted(dr_eids):\n    m = e.get(\"metrics\", {})\n    ppl = m.get(\"eval_ppl_holdout\") or m.get(\"holdout_ppl\")\n    owt = m.get(\"eval_ppl_openwebtext\") or m.get(\"owt_ppl\")\n    wiki = m.get(\"eval_ppl_wikipedia\") or m.get(\"wiki_ppl\")\n    print(f\"  {eid}: holdout={ppl}, owt={owt}, wiki={wiki} | conclusion={e.get('conclusion')}\")\n\nprint(\"\\n\\n=== rho=0.6, tau=0.7 (3-seed) ===\")\nfor eid in [\"adaptive_rho06_tau07_seed42\", \"adaptive_rho06_tau07_seed123\", \"adaptive_rho06_tau07_seed456\"]:\n    m = experiments[eid][\"metrics\"]\n    print(f\"  {eid}: holdout={m.get('holdout_ppl')}, owt={m.get('eval_ppl_openwebtext')}, wiki={m.get('eval_ppl_wikipedia')}\")\n\nprint(\"\\n\\n=== hybrid (adaptive+D&R) rho=0.4 and rho=0.6 ===\")\nfor eid in [\"hybrid_rho04_seed42\", \"hybrid_rho06_seed42\"]:\n    m = experiments[eid][\"metrics\"]\n    print(f\"  {eid}: holdout={m.get('eval_ppl_holdout')}, owt={m.get('eval_ppl_openwebtext')}, wiki={m.get('eval_ppl_wikipedia')}\")\n\nprint(\"\\n\\n=== All D&R q levels (best available) summary ===\")\ndr_q_levels = {}\nfor eid, e in experiments.items():\n    if \"detect_remove_q\" in eid and e.get(\"conclusion\") == \"success\":\n        m = e.get(\"metrics\", {})\n        ppl = m.get(\"eval_ppl_holdout\") or m.get(\"holdout_ppl\") or m.get(\"eval_ppl\")\n        if ppl:\n            # Extract q level\n            import re\n            match = re.search(r'q(\\d+)', eid)\n            if match:\n                q = int(match.group(1))\n                if q not in dr_q_levels:\n                    dr_q_levels[q] = []\n                dr_q_levels[q].append((eid, ppl))\n\nprint(\"  q_level | experiments | PPLs\")\nfor q in sorted(dr_q_levels.keys()):\n    entries = dr_q_levels[q]\n    ppls = [p[1] for p in entries]\n    print(f\"  q=0.{q:02d} | {len(entries)} runs | {[f'{p:.4f}' for p in ppls]}\")\n\nprint(\"\\n\\n=== Downstream accuracy summary for main methods ===\")\ndownstream_map = {\n    \"Adaptive (rho=0.4)\": \"adaptive_fix_seed42\",\n    \"Uniform (rho=0.4)\": \"qwen06b_uniform_seed42\",\n    \"D&R q=0.03\": \"detect_remove_q03_seed42_r2\",\n    \"D&R q=0.04\": \"detect_remove_q04_seed42\",\n    \"D&R q=0.08\": \"detect_remove_q08_seed42\",\n    \"Hybrid rho=0.6\": \"hybrid_rho06_seed42\",\n    \"Adaptive 1.7B seed123\": \"adaptive_1_7b_seed123\",\n    \"Uniform 1.7B seed123\": \"uniform_1_7b_seed123\",\n}\nds_keys = [\"downstream_arc_challenge_acc_norm\", \"downstream_arc_easy_acc_norm\",\n           \"downstream_hellaswag_acc_norm\", \"downstream_piqa_acc_norm\", \"downstream_winogrande_acc\",\n           \"downstream_mean\"]\nprint(f\"  {'Method':<30} {'ARC-C':>6} {'ARC-E':>6} {'Hella':>6} {'PIQA':>6} {'Wino':>6} {'Mean':>6}\")\nfor label, eid in downstream_map.items():\n    e = experiments[eid]\n    m = e.get(\"metrics\", {})\n    vals = [m.get(k, None) for k in ds_keys]\n    # compute mean if not stored\n    numeric = [v for v in vals[:5] if v is not None]\n    comp_mean = statistics.mean(numeric) if numeric else None\n    fmt = lambda v: f\"{v:.4f}\" if v is not None else \"  -- \"\n    mean_val = vals[5] if vals[5] is not None else comp_mean\n    print(f\"  {label:<30} {fmt(vals[0])} {fmt(vals[1])} {fmt(vals[2])} {fmt(vals[3])} {fmt(vals[4])} {fmt(mean_val)}\")\n\nPYEOF\n",
  "description": "Extract delta/p-value stored fields, D&R q-sweep, and downstream accuracy table"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "457c1659-1580-4602-b541-e4cd6de685ca",
  "isSidechain": true,
  "agentId": "a20fa24a4723e1d9c",
  "requestId": "req_011CbLmVhaVywg95LQSBJ5CH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40a79634-ebef-43bc-8660-d821677e43f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "8eaa3b36-4b2e-4596-a917-3c8550c7e172",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Sgnqd7YgCV1A1yVnK8VUmB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9833,
      "cache_read_input_tokens": 50197,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9833,
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

_source line 22 · 2026-05-24T04:32:54.114Z_

<details><summary>↩ Tool result · `toolu_01ELQNjbY8emGbgFQawqPVZS`</summary>

```text
=== Experiments with stored delta / p-value fields ===

[batch_adaptive_tau_rho06_r5]
  vs_uniform_rho06: -0.036
  vs_adaptive_fixed_tau08_rho06: -0.010
  vs_grid_best_rho06: +0.026
  vs_hybrid_rho06: +0.200

[batchsize16_nmin8_r3]
  vs_adaptive_bs4: -0.003 (17.65 vs 17.6527)
  vs_bs8_nmin4: -0.01 (17.65 vs 17.66)

[detect_remove_q05_epoch_matched_seed42]
  vs_full_dr_q05: +0.360 (17.650 vs 17.290, epoch-matched worse)
  vs_adaptive: -0.001 (17.650 vs 17.651, nearly identical to adaptive)

[ess_only_seed123]
  vs_uniform_ppl_delta: +0.034
  vs_adaptive_fix_ppl_delta: +0.077

[ess_only_seed42]
  vs_uniform_ppl_delta: +0.038
  vs_adaptive_ppl_delta: +0.08

[grid_b0_3_seed456_r2]
  vs_uniform: -0.054 (17.64 vs 17.694)
  vs_grid_b03_seed42: 0.000 (17.64 vs 17.640)
  vs_grid_b05_seed456: -0.01 (17.64 vs 17.65)

[random_reweight_seed123_r5]
  vs_uniform_seed123: +0.114
  vs_adaptive_fix_seed123: +0.157
  vs_random_reweight_v2_seed42: consistent (+0.136 seed42 vs +0.114 seed123)

[rho02_adaptive_tau08_seed42]
  vs_rho02_uniform: +0.046 (17.382 vs 17.336)
  vs_rho04_uniform: -0.312 (17.382 vs 17.694)


=== D&R full-data single-seed scan (all q thresholds, seed42) ===
  detect_remove_q01_seed42: holdout=17.4, owt=18.22, wiki=None | conclusion=success
  detect_remove_q02_seed42: holdout=17.27, owt=18.06, wiki=None | conclusion=success
  detect_remove_q03_seed42: holdout=None, owt=None, wiki=None | conclusion=failed
  detect_remove_q03_seed42_r2: holdout=17.25, owt=18.004, wiki=15.037 | conclusion=success
  detect_remove_q04_seed42: holdout=17.26, owt=18.001, wiki=15.038 | conclusion=success
  detect_remove_q05_v2_seed42: holdout=17.2853, owt=18.0139, wiki=15.0528 | conclusion=success
  detect_remove_q06_seed42: holdout=17.3, owt=None, wiki=None | conclusion=success
  detect_remove_q07_seed42: holdout=17.32, owt=None, wiki=None | conclusion=success
  detect_remove_q08_seed42: holdout=17.3442, owt=18.039, wiki=15.066 | conclusion=success
  detect_remove_q09_seed42: holdout=17.42, owt=None, wiki=None | conclusion=success


=== rho=0.6, tau=0.7 (3-seed) ===
  adaptive_rho06_tau07_seed42: holdout=17.735, owt=18.408, wiki=15.355
  adaptive_rho06_tau07_seed123: holdout=17.727, owt=18.385, wiki=15.329
  adaptive_rho06_tau07_seed456: holdout=17.732, owt=18.411, wiki=15.424


=== hybrid (adaptive+D&R) rho=0.4 and rho=0.6 ===
  hybrid_rho04_seed42: holdout=17.514, owt=None, wiki=None
  hybrid_rho06_seed42: holdout=17.526, owt=18.208, wiki=15.267


=== All D&R q levels (best available) summary ===
  q_level | experiments | PPLs
  q=0.01 | 2 runs | ['17.4000', '18.0436']
  q=0.02 | 1 runs | ['17.2700']
  q=0.03 | 4 runs | ['17.2500', '17.2509', '17.2500', '17.7400']
  q=0.04 | 1 runs | ['17.2600']
  q=0.05 | 6 runs | ['17.2770', '17.2720', '17.2853', '17.2800', '17.2700', '17.6500']
  q=0.06 | 1 runs | ['17.3000']
  q=0.07 | 2 runs | ['17.6200', '17.3200']
  q=0.08 | 1 runs | ['17.3442']
  q=0.09 | 2 runs | ['17.6280', '17.4200']


=== Downstream accuracy summary for main methods ===
  Method                          ARC-C  ARC-E  Hella   PIQA   Wino   Mean
  Adaptive (rho=0.4)             0.3430 0.6157 0.4785 0.6866 0.5777 0.5403
  Uniform (rho=0.4)              0.3481 0.6128 0.4836 0.6877 0.5856 0.5436
  D&R q=0.03                     0.3549 0.6301 0.4851 0.6872 0.5675 0.5450
  D&R q=0.04                     0.3567 0.6107 0.4819 0.6931 0.5659 0.5417
  D&R q=0.08                     0.3592 0.6086 0.4855 0.6937 0.5817 0.5457
  Hybrid rho=0.6                 0.3524 0.6208 0.4801 0.6931 0.5785 0.5450
  Adaptive 1.7B seed123          0.4386 0.7138 0.6147 0.7459 0.6298 0.6286
  Uniform 1.7B seed123           0.4317 0.7260 0.6118 0.7454 0.6133 0.6256
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40a79634-ebef-43bc-8660-d821677e43f7",
  "isSidechain": true,
  "promptId": "c0ee33d1-40a2-4cb8-a0f0-d28fa12f6711",
  "agentId": "a20fa24a4723e1d9c",
  "type": "user",
  "uuid": "6c7b874c-2c4e-440b-9348-687eef861ddf",
  "sourceToolAssistantUUID": "40a79634-ebef-43bc-8660-d821677e43f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "8eaa3b36-4b2e-4596-a917-3c8550c7e172",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-24T04:34:13.839Z_

Here is the complete structured summary of all 256 experiments with their key metrics:

---

## Experiment Registry: Full Metrics Summary

**Total experiments: 256** | File: `mcp-agent-ml-research-read_registry-1779596942026.txt`

---

### 1. Canonical Adaptive b* (rho=0.4, tau=0.8, n_min=2) — Primary Method

Uses `adaptive_fix_*` series (canonical clean reruns):

| Experiment | eval_ppl_holdout |
|---|---|
| adaptive_fix_seed42 | **17.6527** |
| adaptive_fix_seed123 | **17.6432** |
| adaptive_fix_seed456 | **17.6566** |
| **Mean ± Std** | **17.6508 ± 0.0069** |

Downstream (seed42): ARC-C=0.343, ARC-E=0.616, Hella=0.479, PIQA=0.687, Wino=0.578, Mean=0.540

Earlier `adaptive_seed{42,123,456}` (n_min=3) give PPLs: 17.644, 17.631, 17.642 — essentially equivalent.

---

### 2. Uniform Baseline (rho=0.4)

| Experiment | eval_ppl_holdout |
|---|---|
| uniform_seed42 | 17.6939 |
| uniform_seed123 | 17.6861 |
| uniform_seed456 | 17.7015 |
| **Mean ± Std** | **17.6938 ± 0.0077** |

Delta vs Adaptive: **+0.043 PPL** (adaptive is better).

---

### 3. ESS-Only Ablation (max-intervention only, no α_eff)

| Experiment | eval_ppl_holdout |
|---|---|
| ess_only_seed42 | 17.73 |
| ess_only_seed123_r2 | 17.721 |
| ess_only_seed456_r2 | 17.762 |
| **Mean ± Std** | **17.7377 ± 0.0215** |

Stored deltas: vs uniform +0.034 (seed42), +0.038 (seed123); vs adaptive_fix +0.080 (seed42), +0.077 (seed123). ESS-only is **worse than both** uniform and adaptive — maximum intervention hurts.

---

### 4. α_eff-Only Ablation (n_min=1, ESS constraint disabled)

| Experiment | holdout_ppl |
|---|---|
| aeff_only_nmin1_seed42 | 17.750 |
| aeff_only_nmin1_seed123 | 17.733 |
| aeff_only_nmin1_seed456 | 17.744 |
| **Mean ± Std** | **17.7423 ± 0.0086** |

Without ESS constraint, α_eff-only also underperforms adaptive — both components needed.

---

### 5. Random Reweighting Baseline

| Experiment | eval_ppl_holdout |
|---|---|
| random_reweight_v2_seed42 | 17.830 |
| random_reweight_seed123_r5 | 17.800 |
| random_reweight_seed456 | 17.777 |
| **Mean ± Std** | **17.8023 ± 0.0266** |

Also: `random_reweight_baseline_seed42` holdout=17.958, OWT=18.606, Wiki=15.519. Stored deltas: vs uniform_seed123 +0.114, vs adaptive_fix_seed123 +0.157. Random reweighting is **worse than uniform**.

---

### 6. Detect & Remove (D&R) — q-threshold sweep (seed42)

Full-data (6103 steps, all tokens):

| q threshold | holdout PPL | OWT PPL | Wiki PPL |
|---|---|---|---|
| q=0.01 | 17.40 | 18.22 | — |
| q=0.02 | 17.27 | 18.06 | — |
| q=0.03 | **17.25** | 18.004 | 15.037 |
| q=0.04 | 17.26 | 18.001 | 15.038 |
| q=0.05 | 17.285 | 18.014 | 15.053 |
| q=0.06 | 17.30 | — | — |
| q=0.07 | 17.32 | — | — |
| q=0.08 | 17.344 | 18.039 | 15.066 |
| q=0.09 | 17.42 | — | — |

Best at q=0.03 (removes ~3% of data). D&R q=0.03 is substantially better than adaptive (17.25 vs 17.65) **but uses fewer training tokens** (removes 3% of data → fewer total tokens).

**3-seed canonical D&R q=0.05**: 17.285 / 17.272 / 17.277 → **Mean 17.278 ± 0.007**
**3-seed canonical D&R q=0.03**: 17.25 / 17.25 / 17.251 → **Mean 17.250 ± 0.0005**

---

### 7. D&R Epoch-Matched (fair comparison: same token budget)

| Experiment | eval_ppl_holdout | steps |
|---|---|---|
| detect_remove_q05_epoch_matched_seed42 | **17.65** | 2533 |
| detect_remove_q07_epoch_matched_seed42 | 17.62 | 3047 |
| detect_remove_q09_epoch_matched_seed42 | 17.628 | 3770 |
| detect_remove_q03_epoch_matched_seed42 | 17.74 | 1927 |
| detect_remove_q01_epoch_matched_seed42 | 18.044 | 6103 |
| dr_epoch_matched_indep_lr_v2_seed42 | 17.651 | 2533 |
| dr_epoch_matched_seed123_r2 | 17.659 | — |
| dr_epoch_matched_seed456 | 17.660 | — |
| epoch_matched_dr_seed123 | 17.660 | — |
| epoch_matched_dr_seed456 | 17.660 | — |

**Key finding**: D&R q=0.05 epoch-matched PPL = 17.65 ≈ adaptive 17.65 (stored delta: vs_adaptive = -0.001). D&R's advantage disappears when matched for compute/tokens.

Uniform epoch-matched (same token budget as D&R q=0.05): seed42=18.062, seed456=18.068 — much worse (less data).

---

### 8. Batch Size Experiments

**B=4 (baseline)**: Canonical adaptive above (17.651)

**B=8, n_min=4:**
| | Adaptive | Uniform |
|---|---|---|
| seed42 | 17.650 | 17.694 |
| seed123 | 17.631 | 17.687 |
| seed456 | 17.646 | 17.702 |
| **Mean** | **17.642 ± 0.010** | **17.694 ± 0.008** |

Stored delta (bs16 vs bs4 adaptive): vs_adaptive_bs4 = -0.003 (17.65 vs 17.653); vs_bs8_nmin4 = -0.01.

**B=16, tau=0.7, n_min=8:**
| | Adaptive | Uniform |
|---|---|---|
| seed42 | 17.631 | 17.694 |
| seed123 | 17.616 | 17.686 |
| seed456 | 17.645 | 17.717 |
| **Mean** | **17.631 ± 0.015** | **17.699 ± 0.016** |

B=8 and B=16 adaptive consistently outperform uniform at the same batch size. Adaptive benefit is stable across batch sizes.

---

### 9. Rho (Contamination Rate) Sensitivity

**rho=0.2:**
- Adaptive (tau=0.8): 17.382
- Uniform: 17.336
- Delta: +0.046 (adaptive worse at low contamination — stored as negative result)

**rho=0.3:**
| | Adaptive | Uniform |
|---|---|---|
| seed42 | 17.422 | 17.422 |
| seed123 | 17.435 | 17.433 |
| seed456 | 17.424 | 17.419 |
| **Mean** | **17.427 ± 0.007** | **17.425 ± 0.007** |

At rho=0.3, adaptive ≈ uniform (no benefit).

**rho=0.4 (main):** Adaptive 17.651, Uniform 17.694 → **delta -0.043**

**rho=0.6 (contamination_60):**
| | Adaptive (tau=0.8) | Uniform |
|---|---|---|
| seed42 | 17.74 | 17.766 |
| seed123 | 17.732 | 17.754 |
| seed456 | 17.735 | 17.770 |
| **Mean** | **17.736 ± 0.004** | **17.763 ± 0.008** |

Also: rho=0.6 ESS-only: seeds 17.770, 17.763, 17.762 → Mean 17.765.

**rho=0.6, tau=0.7 (formula-based tau):**
| seed | holdout PPL |
|---|---|
| seed42 | 17.735 |
| seed123 | 17.727 |
| seed456 | 17.732 |

---

### 10. Tau Sensitivity (rho=0.4, seed42)

| tau | eval_ppl_holdout | b_star_std |
|---|---|---|
| 0.5 | 17.688 | 0.882 |
| 0.6 | 17.681 | 1.069 |
| 0.7 | 17.680 | 1.401 |
| **0.8** | **17.653** | ~2.0 |
| 0.9 | 17.712 | 3.04 |
| 0.95 | 17.723 | 3.992 |

**Tau=0.8 is optimal.** Higher tau (more aggressive) leads to over-intervention; lower tau (less aggressive) loses benefit.

Tau=0.7, 3-seed: 17.680, 17.666, 17.677 → **Mean 17.674 ± 0.007**

---

### 11. n_min Sensitivity (rho=0.4, tau=0.8, seed42)

| n_min | eval_ppl_holdout | b_star_std | note |
|---|---|---|---|
| 1 | 17.789 | 8.374 | extreme b*, 46.7% batch b*≥2, over-downweights |
| 2 | **17.653** | ~2.0 | optimal |
| 3 | 17.644 | — | nearly same as n_min=2 |
| 4 | 17.695 | 0 | degenerates to uniform (b*=0 throughout) |

n_min=1 and n_min=4 both fail; n_min=2–3 is the sweet spot.

---

### 12. 1.7B Scale (Qwen3-1.7B)

| Method | seed42 | seed123 | seed456 | Mean ± Std |
|---|---|---|---|---|
| Adaptive | 13.27 | 13.25 | 13.267 | **13.262 ± 0.011** |
| Uniform | 13.28 | 13.265 | 13.28 | **13.275 ± 0.009** |

Delta: adaptive better by **0.013 PPL** at 1.7B (vs 0.043 at 0.6B — smaller gap but consistent direction).

Downstream (1.7B, seed123): Adaptive Mean=0.6286, Uniform Mean=0.6256.

OWT PPL (1.7B): Adaptive ~13.291, Uniform ~13.292 — essentially tied on OOD.

---

### 13. Detector Comparison (all use same training procedure, different q scores)

| Detector | seed42 | seed123 | seed456 | Mean ± Std |
|---|---|---|---|---|
| **Our q score (TF-IDF/LR)** | 17.6527 | 17.6432 | 17.6566 | **17.651 ± 0.007** |
| N-gram detector | 17.820 | 17.823 | 17.826 | **17.823 ± 0.003** |
| GPT-2 perplexity | 17.790 | 17.788 | 17.797 | **17.792 ± 0.005** |

Uniform baseline: 17.694. N-gram and GPT-2 both **worse than uniform** with adaptive training, while our q score is better. This validates the quality of our detector.

Uniform trained with N-gram scores: eval_ppl=17.69 (= uniform, confirming N-gram scores add no signal for uniform either).

---

### 14. OOD Evaluation (rho=0.4)

Adaptive (seed123/456 avg) vs Uniform (seed123/456 avg):

| | Holdout | OpenWebText | Wikipedia |
|---|---|---|---|
| Adaptive | ~17.680 | ~18.370 | ~15.358 |
| Uniform | ~17.694 | ~18.377 | ~15.368 |

No OOD degradation from adaptive weighting — small improvement across all three domains.

---

### 15. Hybrid (D&R + Adaptive) — single seed

| | rho=0.4 | rho=0.6 |
|---|---|---|
| seed42 | 17.514 | 17.526 |

Hybrid substantially better than either alone, but single-seed only.

---

### 16. Grid Search b Values (2-seed: seed123 + seed456)

| b | seed123 | seed456 | Mean |
|---|---|---|---|
| 0.1 | 17.646 | 17.663 | 17.655 |
| 0.2 | 17.637 | 17.645 | 17.641 |
| **0.3** | **17.579** | **17.640** | **17.610** |
| 0.5 | 17.638 | 17.650 | 17.644 |
| 1.0 | 17.674 | 17.680 | 17.677 |
| 1.5 | 17.701 | 17.710 | 17.706 |
| 2.0 | 17.725 | 17.989* | — |
| 3.0 | 17.760 | 17.921* | — |
| 5.0 | 17.804 | 17.993* | — |

*seed456 b≥2.0 flagged as anomalous (checkpoint issue), paper uses seed123 only for b≥2.

Best fixed b ≈ 0.3 (seed123 best: 17.579). Adaptive b* auto-finds ≈ this without grid search.

Single-seed batch grid (seed42): b=0.5→17.651, b=1.0→17.692, b=1.5→17.718, b=2.0→17.741, b=3.0→17.774, b=5.0→17.818.

---

### 17. Baseline / Reference Points

| Experiment | PPL |
|---|---|
| baseline_qwen3_0.6b (pretrained, no finetuning) | 22.97 |
| golden_ratio_seed42 | 17.654 |
| threshold_q03_seed42 (hard threshold D&R) | **17.253** |
| diagnostic_contamination100 | killed |
| llama3b_adaptive_seed42 | 10.58 |
| llama3b_uniform_seed42 | 10.38 |

---

### 18. Downstream Accuracy Table (0.6B models)

| Method | ARC-C | ARC-E | Hella | PIQA | Wino | Mean |
|---|---|---|---|---|---|---|
| Adaptive (rho=0.4) | 0.343 | 0.616 | 0.479 | 0.687 | 0.578 | 0.540 |
| Uniform (rho=0.4) | 0.348 | 0.613 | 0.484 | 0.688 | 0.586 | 0.544 |
| D&R q=0.03 | 0.355 | 0.630 | 0.485 | 0.687 | 0.568 | 0.545 |
| D&R q=0.08 | 0.359 | 0.609 | 0.486 | 0.694 | 0.582 | 0.546 |
| Hybrid rho=0.6 | 0.352 | 0.621 | 0.480 | 0.693 | 0.579 | 0.545 |

All methods cluster tightly (within ~0.5% mean accuracy). PPL differences are more discriminative.

---

### Key Stored Delta/Comparison Fields

- `ess_only_seed42`: vs_uniform_ppl_delta=+0.038, vs_adaptive_ppl_delta=+0.080
- `ess_only_seed123`: vs_uniform_ppl_delta=+0.034, vs_adaptive_fix_ppl_delta=+0.077
- `grid_b0_3_seed456_r2`: vs_uniform=-0.054, vs_grid_b03_seed42=0.000
- `detect_remove_q05_epoch_matched_seed42`: vs_full_dr_q05=+0.360, vs_adaptive=-0.001
- `rho02_adaptive_tau08_seed42`: vs_rho02_uniform=+0.046, vs_rho04_uniform=-0.312
- `random_reweight_seed123_r5`: vs_uniform_seed123=+0.114, vs_adaptive_fix_seed123=+0.157
- `batch_adaptive_tau_rho06_r5`: vs_uniform_rho06=-0.036, vs_adaptive_fixed_tau08_rho06=-0.010

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c7b874c-2c4e-440b-9348-687eef861ddf",
  "isSidechain": true,
  "agentId": "a20fa24a4723e1d9c",
  "requestId": "req_011CbLmY7FaxRmZ3GtK8B5Pn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "29fdaeed-ff50-4725-ba00-6ee9acc789f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "8eaa3b36-4b2e-4596-a917-3c8550c7e172",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01CV4gSSqJ89Q3hgTt5ghUSx",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3540,
      "cache_read_input_tokens": 60030,
      "output_tokens": 4907,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3540
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4907,
          "cache_read_input_tokens": 60030,
          "cache_creation_input_tokens": 3540,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3540,
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
