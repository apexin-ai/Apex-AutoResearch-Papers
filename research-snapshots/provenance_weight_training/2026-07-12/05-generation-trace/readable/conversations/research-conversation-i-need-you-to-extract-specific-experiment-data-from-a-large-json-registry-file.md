# Research conversation: I need you to extract specific experiment data from a large JSON registry file. The file is at: /home/ubuntu/.claude-acc

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ab3fc5e12c4a8ae93.jsonl`
- **Structured JSON:** [`5677be2334891f6f3a9c.json`](../../sessions/56/5677be2334891f6f3a9c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

37 recorded events

### User

_source line 1 · 2026-05-24T04:29:27.113Z_

I need you to extract specific experiment data from a large JSON registry file. The file is at:
/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c/tool-results/mcp-agent-ml-research-read_registry-1779596944442.txt

The file has schema: {result: string} where result is a JSON string that needs to be parsed.

I need you to find all experiments and extract for each:
- experiment_id
- status
- conclusion (if any)
- metrics (if any) — especially PPL values
- config details (rho, tau, nmin, batch_size, model, method)

Focus on experiments relevant to these specific numbers I need to trace:
1. Adaptive 3-seed B=4 (τ=0.7, ρ=0.4): 17.674±0.007
2. Uniform 3-seed B=4 (ρ=0.4): 17.694±0.008
3. Δ(B=4, ρ=0.4): −0.020±0.008
4. Δ(B=8, ρ=0.4): −0.052±0.007 (p=0.006)
5. Δ(B=16, ρ=0.4): −0.068±0.005
6. ρ=0.6 results: adaptive 17.731±0.004, uniform 17.763±0.008, Δ=−0.032
7. ρ=0.3 results: Δ=+0.002
8. ρ=0.2 results: Δ=+0.046
9. α_eff-only (n_min=1): 17.742±0.009
10. ESS-only: 17.737
11. 1.7B scale: adaptive 13.27, uniform 13.50 → actually 13.27 adaptive, 13.27 uniform? Check.
12. Llama-3.2-3B cross-model: MMLU +1.57pp
13. Detector comparison: GPT-2 PPL Δ=+0.098, N-gram Δ=+0.129
14. D&R q>0.3 3-seed: 17.250±0.001
15. D&R epoch-matched: 17.657±0.005
16. Permuted-score control: 17.951±0.007
17. Grid b=0.3 3-seed: 17.620±0.033
18. Random U(0,2): 17.802±0.027
19. Downstream accuracy: 0.5414
20. 1.7B: adaptive 13.26 vs uniform 13.27

First probe structure with jq, then extract all experiments. Return a comprehensive mapping of experiment_id → key metrics for ALL experiments. Include the full metrics and conclusion fields.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "792d4fc7-1d48-4678-830d-80fd5a58c95b",
  "agentId": "ab3fc5e12c4a8ae93",
  "type": "user",
  "uuid": "221c7892-65d5-4cf1-874e-c65bcde77b2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-24T04:29:27.130Z_

```json
{
  "parentUuid": "221c7892-65d5-4cf1-874e-c65bcde77b2a",
  "isSidechain": true,
  "agentId": "ab3fc5e12c4a8ae93",
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
  "uuid": "13b8b7b1-0d9f-434a-b91f-017cfa3fd9dc",
  "timestamp": "2026-05-24T04:29:27.130Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-24T04:29:29.555Z_

I'll start by probing the file structure with jq, then extract all experiment data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13b8b7b1-0d9f-434a-b91f-017cfa3fd9dc",
  "isSidechain": true,
  "agentId": "ab3fc5e12c4a8ae93",
  "requestId": "req_011CbLmGr2dfkboNJjmnRdK2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "011410b6-c3d2-47e2-aaf6-58c87e00d177",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EjYEXsLzVcQhFtktZdks4a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15332,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15332,
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

_source line 4 · 2026-05-24T04:29:30.719Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Aw6Lge8JQwyMK7Cm4RsuWW`</summary>

```json
{
  "command": "wc -c /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c/tool-results/mcp-agent-ml-research-read_registry-1779596944442.txt",
  "description": "Check file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "011410b6-c3d2-47e2-aaf6-58c87e00d177",
  "isSidechain": true,
  "agentId": "ab3fc5e12c4a8ae93",
  "requestId": "req_011CbLmGr2dfkboNJjmnRdK2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1dddb65c-c267-41ad-8ada-4e2ebae98c73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EjYEXsLzVcQhFtktZdks4a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15332,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15332,
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

### Tool result

_source line 5 · 2026-05-24T04:29:30.878Z_

<details><summary>↩ Tool result · `toolu_01Aw6Lge8JQwyMK7Cm4RsuWW`</summary>

```text
166839 /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c/tool-results/mcp-agent-ml-research-read_registry-1779596944442.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1dddb65c-c267-41ad-8ada-4e2ebae98c73",
  "isSidechain": true,
  "promptId": "792d4fc7-1d48-4678-830d-80fd5a58c95b",
  "agentId": "ab3fc5e12c4a8ae93",
  "type": "user",
  "uuid": "bca0ea5d-48b0-40ac-ab5b-57f62cd0f68b",
  "sourceToolAssistantUUID": "1dddb65c-c267-41ad-8ada-4e2ebae98c73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-24T04:29:31.775Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01VUG8HAS61Y6Psu4SYqpQwZ`</summary>

```json
{
  "command": "head -c 2000 /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c/tool-results/mcp-agent-ml-research-read_registry-1779596944442.txt",
  "description": "Probe file structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bca0ea5d-48b0-40ac-ab5b-57f62cd0f68b",
  "isSidechain": true,
  "agentId": "ab3fc5e12c4a8ae93",
  "requestId": "req_011CbLmGr2dfkboNJjmnRdK2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19fe2150-4080-40fa-81ae-75ad6c4ef621",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EjYEXsLzVcQhFtktZdks4a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15332,
      "cache_read_input_tokens": 0,
      "output_tokens": 345,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15332
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 345,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15332,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15332,
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

_source line 7 · 2026-05-24T04:29:31.844Z_

<details><summary>↩ Tool result · `toolu_01VUG8HAS61Y6Psu4SYqpQwZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"aeff_only_nmin1_seed456\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T13:41:16.042Z\", \"updated_at\": \"2026-05-24T01:50:47.441Z\", \"hypothesis\": \"α_eff-only ablation seed456: cross-seed replicate. n_min=1 removes ESS constraint. Third seed for paired t-test vs dual-constrained baseline.\", \"metrics\": {\"holdout_ppl\": 17.744, \"holdout_loss\": 2.8761}, \"conclusion\": \"success\"}, \"bs8_nmin4_adaptive_seed456_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T12:49:48.326Z\", \"updated_at\": \"2026-05-23T23:11:36.489Z\", \"hypothesis\": \"B=8 第三 seed 补全 3-seed paired comparison。seed42 Δ=−0.044, seed123 Δ=−0.056。预期 Δ∈[−0.040, −0.060]。3-seed 均值将提供 batch-size amplification (B=4→B=8→B=16) 的完整统计支撑。\", \"metrics\": {\"holdout_ppl\": 17.646, \"holdout_loss\": 2.8705, \"owt_ppl\": 18.322, \"wiki_ppl\": 15.299}, \"conclusion\": \"success\"}, \"bs8_nmin4_uniform_seed456_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T12:49:50.668Z\", \"updated_at\": \"2026-05-23T23:09:57.578Z\", \"hypothesis\": \"seed456 uniform baseline at B=8 for paired comparison with bs8_nmin4_adaptive_seed456. Completes 3-seed set for batch-size amplification statistical analysis.\", \"metrics\": {\"holdout_ppl\": 17.702, \"holdout_loss\": 2.8737, \"owt_ppl\": 18.393, \"wiki_ppl\": 15.354}, \"conclusion\": \"success\"}, \"aeff_only_nmin1_seed123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T13:41:13.680Z\", \"updated_at\": \"2026-05-23T20:14:39.454Z\", \"hypothesis\": \"α_eff-only ablation seed123: cross-seed replicate of aeff_only_nmin1_seed42. n_min=1 removes ESS constraint, isolating α_eff signal contribution.\", \"metrics\": {\"holdout_ppl\": 17.733, \"holdout_loss\": 2.8755}, \"conclusion\": \"success\"}, \"aeff_only_nmin1_seed42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T13:41:10.968Z\", \"updated_at\": \"2026-05-23T20:1
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19fe2150-4080-40fa-81ae-75ad6c4ef621",
  "isSidechain": true,
  "promptId": "792d4fc7-1d48-4678-830d-80fd5a58c95b",
  "agentId": "ab3fc5e12c4a8ae93",
  "type": "user",
  "uuid": "cd029b04-79f6-400f-b317-ffd27634c223",
  "sourceToolAssistantUUID": "19fe2150-4080-40fa-81ae-75ad6c4ef621",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-24T04:29:39.677Z_

<details open><summary>🔧 Tool call — Bash · `toolu_011mXu4NZ6XQF4fL2vAtD6ED`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c/tool-results/mcp-agent-ml-research-read_registry-1779596944442.txt\"\n\n# Extract the inner JSON and list all experiment keys\npython3 -c \"\nimport json, sys\n\nwith open('$FILE') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\nprint(f'Total experiments: {len(experiments)}')\nfor k in sorted(experiments.keys()):\n    e = experiments[k]\n    print(k, '|', e.get('status','?'))\n\"",
  "description": "List all experiment IDs and statuses"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd029b04-79f6-400f-b317-ffd27634c223",
  "isSidechain": true,
  "agentId": "ab3fc5e12c4a8ae93",
  "requestId": "req_011CbLmHC5dXBYzQ2vuCxM16",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fbd0ad11-7094-4f33-b373-28a3ebfd9f45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01VKnj6ADmQt5EHj5f9yViGg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2187,
      "cache_read_input_tokens": 15332,
      "output_tokens": 287,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2187
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 287,
          "cache_read_input_tokens": 15332,
          "cache_creation_input_tokens": 2187,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2187,
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

_source line 9 · 2026-05-24T04:29:39.776Z_

<details><summary>↩ Tool result · `toolu_011mXu4NZ6XQF4fL2vAtD6ED`</summary>

```text
Total experiments: 256
adaptive_1_7b_planb_control | PREPARING
adaptive_1_7b_seed123 | DONE
adaptive_1_7b_seed42 | DONE
adaptive_1_7b_seed42_r2 | PREPARING
adaptive_1_7b_seed42_v3 | DONE
adaptive_1_7b_seed42_v4 | DONE
adaptive_1_7b_seed42_v5 | DONE
adaptive_1_7b_seed456 | DONE
adaptive_fix_seed123 | DONE
adaptive_fix_seed42 | DONE
adaptive_fix_seed456 | DONE
adaptive_fromscratch_seed42 | DONE
adaptive_ood_seed123 | DONE
adaptive_ood_seed456 | DONE
adaptive_rho06_tau07_seed123 | DONE
adaptive_rho06_tau07_seed42 | DONE
adaptive_rho06_tau07_seed456 | DONE
adaptive_seed123 | DONE
adaptive_seed42 | DONE
adaptive_seed456 | DONE
adaptive_tau08_scratch_seed42 | DONE
adaptive_tau08_scratch_seed42_v2 | DONE
adaptive_tau08_scratch_seed42_v3 | DONE
adaptive_v2_seed123 | DONE
adaptive_v2_seed42 | DONE
adaptive_v2_seed456 | DONE
aeff_only_nmin1_seed123 | DONE
aeff_only_nmin1_seed42 | DONE
aeff_only_nmin1_seed456 | DONE
baseline_qwen3_0.6b | DONE
batch_adaptive_tau_rho04_seed42 | DONE
batch_adaptive_tau_rho06_r2 | DONE
batch_adaptive_tau_rho06_r3 | DONE
batch_adaptive_tau_rho06_r5 | DONE
batch_adaptive_tau_rho06_seed42 | DONE
batchsize16_nmin8_r2 | DONE
batchsize16_nmin8_r3 | DONE
batchsize16_nmin8_seed42 | DONE
bs16_adaptive_tau07_seed123 | DONE
bs16_adaptive_tau07_seed123_r2 | DONE
bs16_adaptive_tau07_seed42 | DONE
bs16_adaptive_tau07_seed456 | DONE
bs16_uniform_seed123 | DONE
bs16_uniform_seed42 | DONE
bs16_uniform_seed456 | DONE
bs8_auto_nmin_r2 | DONE
bs8_auto_nmin_r3 | DONE
bs8_auto_nmin_r5 | DONE
bs8_auto_nmin_seed42 | DONE
bs8_nmin2_seed42 | DONE
bs8_nmin2_seed42_r2 | DONE
bs8_nmin4_adaptive_seed123 | DONE
bs8_nmin4_adaptive_seed123_r2 | DONE
bs8_nmin4_adaptive_seed42 | DONE
bs8_nmin4_adaptive_seed456 | DONE
bs8_nmin4_adaptive_seed456_r2 | DONE
bs8_nmin4_uniform_seed123 | DONE
bs8_nmin4_uniform_seed123_r2 | DONE
bs8_nmin4_uniform_seed42 | DONE
bs8_nmin4_uniform_seed456 | DONE
bs8_nmin4_uniform_seed456_r2 | DONE
bs8_seed42 | DONE
contamination_60_adaptive_seed123_tau08 | DONE
contamination_60_adaptive_seed42_tau08 | DONE
contamination_60_adaptive_seed456 | DONE
contamination_60_ess_only_seed123 | DONE
contamination_60_ess_only_seed42 | DONE
contamination_60_ess_only_seed456 | DONE
contamination_60_grid_b0_3_seed42 | DONE
contamination_60_grid_b0_5_seed42 | DONE
contamination_60_random_seed123 | DONE
contamination_60_random_seed42 | DONE
contamination_60_random_seed456 | DONE
contamination_60_seed123 | DONE
contamination_60_seed42 | DONE
contamination_60_seed42_r2 | DONE
contamination_60_tau06_seed42 | DONE
contamination_60_tau07_seed42 | DONE
contamination_60_uniform_seed123 | DONE
contamination_60_uniform_seed42 | DONE
contamination_60_uniform_seed456 | DONE
datagen_synthetic_4gpu | DONE
detect_remove_baseline_seed42 | DONE
detect_remove_q01_epoch_matched_seed42 | DONE
detect_remove_q01_seed42 | DONE
detect_remove_q02_seed42 | DONE
detect_remove_q03_epoch_matched_seed42 | DONE
detect_remove_q03_seed123 | DONE
detect_remove_q03_seed42 | DONE
detect_remove_q03_seed42_r2 | DONE
detect_remove_q03_seed456 | DONE
detect_remove_q04_seed42 | DONE
detect_remove_q05_epoch_matched | PREPARING
detect_remove_q05_epoch_matched_seed42 | DONE
detect_remove_q05_seed123 | DONE
detect_remove_q05_seed42 | PREPARING
detect_remove_q05_seed456 | DONE
detect_remove_q05_v2_seed123 | DONE
detect_remove_q05_v2_seed123_r2 | DONE
detect_remove_q05_v2_seed42 | DONE
detect_remove_q05_v2_seed456 | DONE
detect_remove_q06_seed42 | DONE
detect_remove_q07_epoch_matched_seed42 | DONE
detect_remove_q07_seed42 | DONE
detect_remove_q07_seed42_r2 | PREPARING
detect_remove_q08_seed42 | DONE
detect_remove_q09_epoch_matched_seed42 | DONE
detect_remove_q09_seed42 | DONE
detector_modernbert | DONE
detector_tfidf_lr | DONE
diagnostic_contamination100 | DONE
dr_epoch_matched_indep_lr_seed42 | DONE
dr_epoch_matched_indep_lr_v2_seed42 | DONE
dr_epoch_matched_seed123 | DONE
dr_epoch_matched_seed123_r2 | DONE
dr_epoch_matched_seed456 | DONE
env_probe_41312 | PREPARING
env_probe_41312_v2 | PREPARING
epoch_matched_dr_seed123 | DONE
epoch_matched_dr_seed456 | DONE
ess_only_seed123 | DONE
ess_only_seed123_r2 | DONE
ess_only_seed42 | DONE
ess_only_seed456 | DONE
ess_only_seed456_r2 | DONE
eval_adaptive_1_7b | PREPARING
eval_adaptive_1_7b_seed123 | PREPARING
eval_adaptive_1_7b_v2 | DONE
eval_epoch_matched_seed123 | DONE
eval_epoch_matched_seed456 | DONE
eval_ngram_adaptive | DONE
eval_ngram_uniform | DONE
eval_q01_final | PREPARING
eval_q01_final_v2 | DONE
eval_q03_r2 | DONE
eval_q04 | DONE
eval_q06 | DONE
eval_q07_final | DONE
eval_rho06_batch_v5 | PREPARING
eval_rho06_batch_v6 | PREPARING
eval_rho06_batch_v7 | DONE
eval_uniform_1_7b_resumed | PREPARING
eval_uniform_1_7b_seed123 | PREPARING
eval_uniform_1_7b_v2 | PREPARING
eval_uniform_1_7b_v3 | DONE
golden_ratio_seed42 | DONE
gpt2_adaptive_seed123 | DONE
gpt2_adaptive_seed123_v2 | DONE
gpt2_adaptive_seed123_v3 | DONE
gpt2_adaptive_seed42 | DONE
gpt2_adaptive_seed456 | DONE
gpt2_adaptive_seed456_v2 | DONE
gpt2_uniform_seed42 | DONE
grid_b0_1_seed123 | DONE
grid_b0_1_seed42 | DONE
grid_b0_1_seed456 | DONE
grid_b0_2_seed123 | DONE
grid_b0_2_seed42 | DONE
grid_b0_2_seed456 | DONE
grid_b0_3_seed123 | DONE
grid_b0_3_seed123_r2 | DONE
grid_b0_3_seed42 | DONE
grid_b0_3_seed456 | DONE
grid_b0_3_seed456_r2 | DONE
grid_b0_5_seed123 | DONE
grid_b0_5_seed456 | DONE
grid_b1_0_seed123 | DONE
grid_b1_0_seed456 | DONE
grid_b1_5_seed123 | DONE
grid_b1_5_seed456 | DONE
grid_b2_0_seed123 | DONE
grid_b2_0_seed456 | DONE
grid_b3_0_seed123 | DONE
grid_b3_0_seed456 | DONE
grid_b5_0_seed123 | DONE
grid_b5_0_seed456 | DONE
grid_b_low_seed42 | DONE
grid_b_low_seed42_r2 | DONE
grid_b_low_seed42_r3 | DONE
grid_b_low_serial_seed42 | DONE
grid_b_seed42_batch | DONE
hybrid_rho04_seed42 | DONE
hybrid_rho06_seed42 | DONE
llama3b_adaptive_seed42 | DONE
llama3b_uniform_seed42 | DONE
ngram_adaptive_seed123 | DONE
ngram_adaptive_seed42 | DONE
ngram_adaptive_seed456 | DONE
ngram_adaptive_seed456_v2 | DONE
ngram_uniform_seed42 | DONE
nmin1_seed42 | DONE
nmin4_seed42 | DONE
nmin5_seed42 | DONE
p0_contamination_60_datagen | DONE
qwen06b_uniform_seed42 | DONE
random_reweight_baseline_seed42 | DONE
random_reweight_seed123 | DONE
random_reweight_seed123_r2 | DONE
random_reweight_seed123_r3 | DONE
random_reweight_seed123_r4 | DONE
random_reweight_seed123_r5 | DONE
random_reweight_seed42 | DONE
random_reweight_seed456 | DONE
random_reweight_v2_seed42 | DONE
random_reweight_v2_seed456 | DONE
rho02_adaptive_tau08_seed42 | DONE
rho02_adaptive_tau09_r2 | DONE
rho02_adaptive_tau09_r3 | DONE
rho02_adaptive_tau09_r4 | DONE
rho02_adaptive_tau09_r5 | DONE
rho02_adaptive_tau09_seed42 | DONE
rho02_uniform_seed42 | DONE
rho03_adaptive_seed123 | DONE
rho03_adaptive_seed42 | DONE
rho03_adaptive_seed456 | DONE
rho03_adaptive_seed456_r2 | DONE
rho03_uniform_seed123 | DONE
rho03_uniform_seed42 | DONE
rho03_uniform_seed456 | DONE
rho06_tau07_seed123 | DONE
rho06_tau07_seed42 | DONE
rho06_tau07_seed456 | DONE
status_check_41312 | PREPARING
tau07_downstream_eval | DONE
tau07_seed123 | DONE
tau07_seed42 | DONE
tau07_seed456 | DONE
tau_0.6_seed42 | DONE
tau_05_nmin2_seed42 | DONE
tau_05_seed42 | DONE
tau_06_nmin2_seed42 | DONE
tau_06_seed42 | DONE
tau_07_nmin2_seed42 | DONE
tau_07_seed42 | DONE
tau_095_nmin2_seed42 | DONE
tau_095_seed42 | DONE
tau_09_nmin2_seed42 | DONE
tau_09_seed42 | DONE
threshold_q03_seed42 | DONE
threshold_q07_seed42 | DONE
uniform_1_7b_seed123 | DONE
uniform_1_7b_seed42 | DONE
uniform_1_7b_seed42_r2 | PREPARING
uniform_1_7b_seed42_v3 | DONE
uniform_1_7b_seed42_v4 | DONE
uniform_1_7b_seed42_v5 | DONE
uniform_1_7b_seed456 | DONE
uniform_epoch_matched_indep_lr_seed42 | DONE
uniform_epoch_matched_seed456 | DONE
uniform_ood_seed123 | DONE
uniform_ood_seed456 | DONE
uniform_seed123 | DONE
uniform_seed42 | DONE
uniform_seed42_downstream | DONE
uniform_seed456 | DONE
w2_distribution_matching_eval | DONE
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fbd0ad11-7094-4f33-b373-28a3ebfd9f45",
  "isSidechain": true,
  "promptId": "792d4fc7-1d48-4678-830d-80fd5a58c95b",
  "agentId": "ab3fc5e12c4a8ae93",
  "type": "user",
  "uuid": "6ef75b34-b047-4d1b-90ab-02f2beaca2b6",
  "sourceToolAssistantUUID": "fbd0ad11-7094-4f33-b373-28a3ebfd9f45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-24T04:29:49.262Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01JXMMqP5qPa3V1Y5LwDnDFC`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c/tool-results/mcp-agent-ml-research-read_registry-1779596944442.txt\"\n\npython3 -c \"\nimport json\n\nwith open('$FILE') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Print ALL experiments with full details\nfor k in sorted(experiments.keys()):\n    e = experiments[k]\n    print(f'=== {k} ===')\n    print(f'  status: {e.get(\\\"status\\\")}')\n    print(f'  hypothesis: {e.get(\\\"hypothesis\\\",\\\"\\\")[:200]}')\n    print(f'  metrics: {e.get(\\\"metrics\\\")}')\n    print(f'  conclusion: {e.get(\\\"conclusion\\\")}')\n    cfg = e.get('config', {})\n    if cfg:\n        print(f'  config: rho={cfg.get(\\\"rho\\\")}, tau={cfg.get(\\\"tau\\\")}, nmin={cfg.get(\\\"nmin\\\")}, batch_size={cfg.get(\\\"batch_size\\\")}, model={cfg.get(\\\"model\\\")}, method={cfg.get(\\\"method\\\")}')\n    print()\n\" 2>&1 | head -3000",
  "description": "Extract all experiment details - first 3000 lines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ef75b34-b047-4d1b-90ab-02f2beaca2b6",
  "isSidechain": true,
  "agentId": "ab3fc5e12c4a8ae93",
  "requestId": "req_011CbLmHmyajaAPSdyYPGnTR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a9abcce4-19b0-418a-ad02-a4d0bae20b05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011NWYk37Pc6EAcqVsUUQvsa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3925,
      "cache_read_input_tokens": 17519,
      "output_tokens": 464,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3925
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 464,
          "cache_read_input_tokens": 17519,
          "cache_creation_input_tokens": 3925,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3925,
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

_source line 11 · 2026-05-24T04:29:49.353Z_

<details><summary>↩ Tool result · `toolu_01JXMMqP5qPa3V1Y5LwDnDFC`</summary>

```text
&lt;persisted-output>
Output too large (109.5KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c/tool-results/bx1on8mgq.txt

Preview (first 2KB):
=== adaptive_1_7b_planb_control ===
  status: PREPARING
  hypothesis: 
  metrics: None
  conclusion: None

=== adaptive_1_7b_seed123 ===
  status: DONE
  hypothesis: Adaptive (dual-constrained) at 1.7B model scale (seed=123, τ=0.8, ρ=0.4). From-scratch on westd-41312 cuda:1. Replicates adaptive_1_7b_seed42_v5 (PPL=13.27) with different seed for 3-seed error bars. 
  metrics: {'eval_ppl_holdout': 13.25, 'eval_loss_holdout': 2.5843, 'eval_ppl_openwebtext': 13.2909, 'eval_ppl_wikipedia': 10.9521, 'downstream_arc_easy_acc_norm': 0.7138, 'downstream_arc_challenge_acc_norm': 0.4386, 'downstream_hellaswag_acc_norm': 0.6147, 'downstream_piqa_acc_norm': 0.7459, 'downstream_winogrande_acc': 0.6298, 'downstream_mean': 0.6286}
  conclusion: success

=== adaptive_1_7b_seed42 ===
  status: DONE
  hypothesis: Scale validation: adaptive provenance weighting on Qwen3-1.7B (2.8x larger than 0.6B). If adaptive still outperforms uniform at 1.7B scale, demonstrates method generality beyond small models. Key for 
  metrics: None
  conclusion: success

=== adaptive_1_7b_seed42_r2 ===
  status: PREPARING
  hypothesis: 
  metrics: None
  conclusion: None

=== adaptive_1_7b_seed42_v3 ===
  status: DONE
  hypothesis: Adaptive (dual-constrained) at 1.7B model scale (seed=42, τ=0.8, ρ=0.4). Paired with uniform_1_7b_seed42_v3 to test if adaptive advantage holds at larger model scale. Key for model scaling claim in pa
  metrics: None
  conclusion: killed

=== adaptive_1_7b_seed42_v4 ===
  status: DONE
  hypothesis: Adaptive (dual-constrained) at 1.7B model scale (seed=42, τ=0.8, ρ=0.4). From-scratch on westd-41312. Tests if adaptive advantage holds at larger model scale. v4 replaces v3. Already approved.
  metrics: None
  conclusion: failed

=== adaptive_1_7b_seed42_v5 ===
  status: DONE
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9abcce4-19b0-418a-ad02-a4d0bae20b05",
  "isSidechain": true,
  "promptId": "792d4fc7-1d48-4678-830d-80fd5a58c95b",
  "agentId": "ab3fc5e12c4a8ae93",
  "type": "user",
  "uuid": "19e6b69c-423c-4d66-b3b7-f39469c97d73",
  "sourceToolAssistantUUID": "a9abcce4-19b0-418a-ad02-a4d0bae20b05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-24T04:29:59.326Z_

<details open><summary>🔧 Tool call — Read · `toolu_01A3ayzvuEKKCw4ND1tERfei`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c/tool-results/bx1on8mgq.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19e6b69c-423c-4d66-b3b7-f39469c97d73",
  "isSidechain": true,
  "agentId": "ab3fc5e12c4a8ae93",
  "requestId": "req_011CbLmJUwBBGwwfZ93jtHGq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bb9c5433-1cc6-4ca8-95f9-a66f56e9e4b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FPVRwqiArRKAubUA7ZVTcp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1284,
      "cache_read_input_tokens": 21444,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1284
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 136,
          "cache_read_input_tokens": 21444,
          "cache_creation_input_tokens": 1284,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1284,
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

_source line 13 · 2026-05-24T04:29:59.603Z_

<details><summary>↩ Tool result · reported error · `toolu_01A3ayzvuEKKCw4ND1tERfei`</summary>

```text
File content (43960 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb9c5433-1cc6-4ca8-95f9-a66f56e9e4b5",
  "isSidechain": true,
  "promptId": "792d4fc7-1d48-4678-830d-80fd5a58c95b",
  "agentId": "ab3fc5e12c4a8ae93",
  "type": "user",
  "uuid": "52ff1183-5ae4-4cf0-8d3c-0ca6a5133123",
  "toolUseResult": "Error: File content (43960 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "bb9c5433-1cc6-4ca8-95f9-a66f56e9e4b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-24T04:30:47.997Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01LGw4Twq6y8oxJckzVNiDru`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c/tool-results/mcp-agent-ml-research-read_registry-1779596944442.txt\"\n\npython3 << 'EOF'\nimport json\n\nwith open(FILE) as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Group by category for targeted extraction\ntarget_groups = {\n    # B=4, rho=0.4 main results\n    'B4_rho04': ['adaptive_seed42', 'adaptive_seed123', 'adaptive_seed456', 'uniform_seed42', 'uniform_seed123', 'uniform_seed456'],\n    # B=8, rho=0.4\n    'B8_rho04': ['bs8_nmin4_adaptive_seed42', 'bs8_nmin4_adaptive_seed123', 'bs8_nmin4_adaptive_seed456', \n                  'bs8_nmin4_adaptive_seed123_r2', 'bs8_nmin4_adaptive_seed456_r2',\n                  'bs8_nmin4_uniform_seed42', 'bs8_nmin4_uniform_seed123', 'bs8_nmin4_uniform_seed456',\n                  'bs8_nmin4_uniform_seed123_r2', 'bs8_nmin4_uniform_seed456_r2'],\n    # B=16\n    'B16': ['bs16_adaptive_tau07_seed42', 'bs16_adaptive_tau07_seed123', 'bs16_adaptive_tau07_seed456',\n            'bs16_adaptive_tau07_seed123_r2',\n            'bs16_uniform_seed42', 'bs16_uniform_seed123', 'bs16_uniform_seed456'],\n    # rho=0.6\n    'rho06': ['adaptive_rho06_tau07_seed42', 'adaptive_rho06_tau07_seed123', 'adaptive_rho06_tau07_seed456',\n               'rho06_tau07_seed42', 'rho06_tau07_seed123', 'rho06_tau07_seed456'],\n    # rho=0.3\n    'rho03': ['rho03_adaptive_seed42', 'rho03_adaptive_seed123', 'rho03_adaptive_seed456', 'rho03_adaptive_seed456_r2',\n               'rho03_uniform_seed42', 'rho03_uniform_seed123', 'rho03_uniform_seed456'],\n    # rho=0.2\n    'rho02': ['rho02_adaptive_tau08_seed42', 'rho02_adaptive_tau09_seed42', 'rho02_adaptive_tau09_r2',\n               'rho02_adaptive_tau09_r3', 'rho02_adaptive_tau09_r4', 'rho02_adaptive_tau09_r5', 'rho02_uniform_seed42'],\n    # alpha_eff only (nmin=1)\n    'aeff_only': ['aeff_only_nmin1_seed42', 'aeff_only_nmin1_seed123', 'aeff_only_nmin1_seed456'],\n    # ESS only\n    'ess_only': ['ess_only_seed42', 'ess_only_seed123', 'ess_only_seed456', 'ess_only_seed123_r2', 'ess_only_seed456_r2'],\n    # 1.7B scale\n    '1_7b': ['adaptive_1_7b_seed42', 'adaptive_1_7b_seed42_v3', 'adaptive_1_7b_seed42_v4', 'adaptive_1_7b_seed42_v5',\n              'adaptive_1_7b_seed123', 'adaptive_1_7b_seed456',\n              'uniform_1_7b_seed42', 'uniform_1_7b_seed42_v3', 'uniform_1_7b_seed42_v4', 'uniform_1_7b_seed42_v5',\n              'uniform_1_7b_seed123', 'uniform_1_7b_seed456',\n              'eval_adaptive_1_7b_v2', 'eval_uniform_1_7b_v3'],\n    # Llama 3B cross-model\n    'llama3b': ['llama3b_adaptive_seed42', 'llama3b_uniform_seed42'],\n    # GPT2 detector\n    'gpt2_detector': ['gpt2_adaptive_seed42', 'gpt2_adaptive_seed123', 'gpt2_adaptive_seed456',\n                       'gpt2_adaptive_seed123_v2', 'gpt2_adaptive_seed123_v3',\n                       'gpt2_adaptive_seed456_v2', 'gpt2_uniform_seed42'],\n    # Ngram detector\n    'ngram_detector': ['ngram_adaptive_seed42', 'ngram_adaptive_seed123', 'ngram_adaptive_seed456',\n                        'ngram_adaptive_seed456_v2', 'ngram_uniform_seed42',\n                        'eval_ngram_adaptive', 'eval_ngram_uniform'],\n    # D&R q>0.3 3-seed\n    'dr_q03': ['detect_remove_q03_seed42', 'detect_remove_q03_seed123', 'detect_remove_q03_seed456',\n                'detect_remove_q03_seed42_r2', 'eval_q03_r2'],\n    # D&R epoch-matched\n    'dr_epoch': ['detect_remove_q03_epoch_matched_seed42', 'dr_epoch_matched_seed123', 'dr_epoch_matched_seed456',\n                  'dr_epoch_matched_seed123_r2', 'epoch_matched_dr_seed123', 'epoch_matched_dr_seed456',\n                  'eval_epoch_matched_seed123', 'eval_epoch_matched_seed456', 'dr_epoch_matched_indep_lr_seed42',\n                  'dr_epoch_matched_indep_lr_v2_seed42'],\n    # Permuted score control\n    'permuted': ['random_reweight_seed42', 'random_reweight_seed123', 'random_reweight_seed456',\n                  'random_reweight_baseline_seed42', 'random_reweight_v2_seed42', 'random_reweight_v2_seed456',\n                  'random_reweight_seed123_r2', 'random_reweight_seed123_r3', 'random_reweight_seed123_r4', 'random_reweight_seed123_r5'],\n    # Grid b=0.3\n    'grid_b03': ['grid_b0_3_seed42', 'grid_b0_3_seed123', 'grid_b0_3_seed456',\n                  'grid_b0_3_seed123_r2', 'grid_b0_3_seed456_r2'],\n    # Random U(0,2)\n    'grid_random': ['grid_b_low_seed42', 'grid_b_low_seed42_r2', 'grid_b_low_seed42_r3',\n                     'grid_b_seed42_batch', 'grid_b_low_serial_seed42'],\n    # Downstream\n    'downstream': ['tau07_downstream_eval', 'uniform_seed42_downstream'],\n    # Additional grid\n    'grid_other': ['grid_b0_1_seed42', 'grid_b0_1_seed123', 'grid_b0_1_seed456',\n                    'grid_b0_2_seed42', 'grid_b0_2_seed123', 'grid_b0_2_seed456',\n                    'grid_b0_5_seed123', 'grid_b0_5_seed456',\n                    'grid_b1_0_seed123', 'grid_b1_0_seed456',\n                    'grid_b1_5_seed123', 'grid_b1_5_seed456',\n                    'grid_b2_0_seed123', 'grid_b2_0_seed456',\n                    'grid_b3_0_seed123', 'grid_b3_0_seed456',\n                    'grid_b5_0_seed123', 'grid_b5_0_seed456'],\n    # Detectors comparison\n    'detectors': ['detector_modernbert', 'detector_tfidf_lr'],\n}\n\nfor group, ids in target_groups.items():\n    print(f'\\n{\"=\"*60}')\n    print(f'GROUP: {group}')\n    print(f'{\"=\"*60}')\n    for eid in ids:\n        if eid not in experiments:\n            print(f'  [{eid}] NOT FOUND')\n            continue\n        e = experiments[eid]\n        print(f'  [{eid}]')\n        print(f'    status: {e.get(\"status\")}')\n        print(f'    metrics: {e.get(\"metrics\")}')\n        print(f'    conclusion: {e.get(\"conclusion\")}')\n        h = e.get('hypothesis','')\n        if h:\n            print(f'    hypothesis: {h[:300]}')\n        cfg = e.get('config', {})\n        if cfg:\n            print(f'    config: {cfg}')\n        print()\n\nEOF\nFILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c/tool-results/mcp-agent-ml-research-read_registry-1779596944442.txt\" python3 << 'PYEOF'\nimport json\n\nFILE = \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c/tool-results/mcp-agent-ml-research-read_registry-1779596944442.txt\"\n\nwith open(FILE) as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\ntarget_groups = {\n    'B4_rho04': ['adaptive_seed42', 'adaptive_seed123', 'adaptive_seed456', 'uniform_seed42', 'uniform_seed123', 'uniform_seed456'],\n    'B8_rho04': ['bs8_nmin4_adaptive_seed42', 'bs8_nmin4_adaptive_seed123', 'bs8_nmin4_adaptive_seed456', \n                  'bs8_nmin4_adaptive_seed123_r2', 'bs8_nmin4_adaptive_seed456_r2',\n                  'bs8_nmin4_uniform_seed42', 'bs8_nmin4_uniform_seed123', 'bs8_nmin4_uniform_seed456',\n                  'bs8_nmin4_uniform_seed123_r2', 'bs8_nmin4_uniform_seed456_r2'],\n    'B16': ['bs16_adaptive_tau07_seed42', 'bs16_adaptive_tau07_seed123', 'bs16_adaptive_tau07_seed456',\n            'bs16_adaptive_tau07_seed123_r2',\n            'bs16_uniform_seed42', 'bs16_uniform_seed123', 'bs16_uniform_seed456'],\n    'rho06': ['adaptive_rho06_tau07_seed42', 'adaptive_rho06_tau07_seed123', 'adaptive_rho06_tau07_seed456',\n               'rho06_tau07_seed42', 'rho06_tau07_seed123', 'rho06_tau07_seed456'],\n    'rho03': ['rho03_adaptive_seed42', 'rho03_adaptive_seed123', 'rho03_adaptive_seed456', 'rho03_adaptive_seed456_r2',\n               'rho03_uniform_seed42', 'rho03_uniform_seed123', 'rho03_uniform_seed456'],\n    'rho02': ['rho02_adaptive_tau08_seed42', 'rho02_adaptive_tau09_seed42', 'rho02_adaptive_tau09_r2',\n               'rho02_adaptive_tau09_r3', 'rho02_adaptive_tau09_r4', 'rho02_adaptive_tau09_r5', 'rho02_uniform_seed42'],\n    'aeff_only': ['aeff_only_nmin1_seed42', 'aeff_only_nmin1_seed123', 'aeff_only_nmin1_seed456'],\n    'ess_only': ['ess_only_seed42', 'ess_only_seed123', 'ess_only_seed456', 'ess_only_seed123_r2', 'ess_only_seed456_r2'],\n    '1_7b': ['adaptive_1_7b_seed42', 'adaptive_1_7b_seed42_v3', 'adaptive_1_7b_seed42_v4', 'adaptive_1_7b_seed42_v5',\n              'adaptive_1_7b_seed123', 'adaptive_1_7b_seed456',\n              'uniform_1_7b_seed42', 'uniform_1_7b_seed42_v3', 'uniform_1_7b_seed42_v4', 'uniform_1_7b_seed42_v5',\n              'uniform_1_7b_seed123', 'uniform_1_7b_seed456',\n              'eval_adaptive_1_7b_v2', 'eval_uniform_1_7b_v3'],\n    'llama3b': ['llama3b_adaptive_seed42', 'llama3b_uniform_seed42'],\n    'gpt2_detector': ['gpt2_adaptive_seed42', 'gpt2_adaptive_seed123', 'gpt2_adaptive_seed456',\n                       'gpt2_adaptive_seed123_v2', 'gpt2_adaptive_seed123_v3',\n                       'gpt2_adaptive_seed456_v2', 'gpt2_uniform_seed42'],\n    'ngram_detector': ['ngram_adaptive_seed42', 'ngram_adaptive_seed123', 'ngram_adaptive_seed456',\n                        'ngram_adaptive_seed456_v2', 'ngram_uniform_seed42',\n                        'eval_ngram_adaptive', 'eval_ngram_uniform'],\n    'dr_q03': ['detect_remove_q03_seed42', 'detect_remove_q03_seed123', 'detect_remove_q03_seed456',\n                'detect_remove_q03_seed42_r2', 'eval_q03_r2'],\n    'dr_epoch': ['detect_remove_q03_epoch_matched_seed42', 'dr_epoch_matched_seed123', 'dr_epoch_matched_seed456',\n                  'dr_epoch_matched_seed123_r2', 'epoch_matched_dr_seed123', 'epoch_matched_dr_seed456',\n                  'eval_epoch_matched_seed123', 'eval_epoch_matched_seed456'],\n    'permuted': ['random_reweight_seed42', 'random_reweight_seed123', 'random_reweight_seed456',\n                  'random_reweight_baseline_seed42', 'random_reweight_v2_seed42', 'random_reweight_v2_seed456',\n                  'random_reweight_seed123_r2', 'random_reweight_seed123_r3', 'random_reweight_seed123_r4', 'random_reweight_seed123_r5'],\n    'grid_b03': ['grid_b0_3_seed42', 'grid_b0_3_seed123', 'grid_b0_3_seed456',\n                  'grid_b0_3_seed123_r2', 'grid_b0_3_seed456_r2'],\n    'grid_random': ['grid_b_low_seed42', 'grid_b_low_seed42_r2', 'grid_b_low_seed42_r3',\n                     'grid_b_seed42_batch', 'grid_b_low_serial_seed42'],\n    'downstream': ['tau07_downstream_eval', 'uniform_seed42_downstream'],\n    'detectors': ['detector_modernbert', 'detector_tfidf_lr'],\n    'grid_other': ['grid_b0_1_seed42', 'grid_b0_1_seed123', 'grid_b0_1_seed456',\n                    'grid_b0_2_seed42', 'grid_b0_2_seed123', 'grid_b0_2_seed456',\n                    'grid_b0_5_seed123', 'grid_b0_5_seed456'],\n}\n\nfor group, ids in target_groups.items():\n    print(f'\\n{\"=\"*60}')\n    print(f'GROUP: {group}')\n    print(f'{\"=\"*60}')\n    for eid in ids:\n        if eid not in experiments:\n            print(f'  [{eid}] NOT FOUND')\n            continue\n        e = experiments[eid]\n        print(f'  [{eid}]')\n        print(f'    status: {e.get(\"status\")}')\n        print(f'    metrics: {e.get(\"metrics\")}')\n        print(f'    conclusion: {e.get(\"conclusion\")}')\n        h = e.get('hypothesis','')\n        if h:\n            print(f'    hypothesis: {h[:300]}')\n        cfg = e.get('config', {})\n        if cfg:\n            print(f'    config: {cfg}')\n        print()\nPYEOF",
  "description": "Extract targeted experiment groups with full details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52ff1183-5ae4-4cf0-8d3c-0ca6a5133123",
  "isSidechain": true,
  "agentId": "ab3fc5e12c4a8ae93",
  "requestId": "req_011CbLmKEpeGGwuJEjVzm5U8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "512ab4f5-e7a4-4dcd-bf5b-0956557a1477",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01VsQVgSiQ6wiMRmWedeGd7o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 197,
      "cache_read_input_tokens": 22728,
      "output_tokens": 4724,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 197
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4724,
          "cache_read_input_tokens": 22728,
          "cache_creation_input_tokens": 197,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 197,
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

_source line 15 · 2026-05-24T04:30:48.311Z_

<details><summary>↩ Tool result · `toolu_01LGw4Twq6y8oxJckzVNiDru`</summary>

```text
&lt;persisted-output>
Output too large (60.7KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c/tool-results/bea8k4j33.txt

Preview (first 2KB):
Traceback (most recent call last):
  File "&lt;stdin>", line 3, in &lt;module>
NameError: name 'FILE' is not defined

============================================================
GROUP: B4_rho04
============================================================
  [adaptive_seed42]
    status: DONE
    metrics: {'train_loss': 9.2665, 'train_runtime_s': 13115.09, 'total_steps': 6103, 'train_samples_per_second': 7.445, 'train_steps_per_second': 0.465, 'epoch': 0.26, 'weighting_method': 'adaptive', 'tau': 0.8, 'n_min': 3, 'contamination_ratio': 0.4, 'b_star': 'per-batch adaptive (0.0-3.8)', 'alpha_eff_range': '0.03-0.80 (capped at tau)', 'eval_ppl_holdout': 17.644, 'eval_loss_holdout': 2.8704, 'eval_holdout_tokens': 4077068, 'eval_method': 'eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)', 'eval_note': 'unified post-hoc eval 2026-05-15; confirmed unchanged from prior post-hoc (was 17.644/4077068)'}
    conclusion: success
    hypothesis: Adaptive b* (from α_eff theory) matches or exceeds grid-searched best-b without grid search, seed=42

  [adaptive_seed123]
    status: DONE
    metrics: {'train_loss': 9.2665, 'train_runtime_s': 13197.18, 'total_steps': 6103, 'train_samples_per_second': 7.399, 'train_steps_per_second': 0.462, 'epoch': 0.26, 'weighting_method': 'adaptive', 'tau': 0.8, 'n_min': 3, 'contamination_ratio': 0.4, 'b_star': 'per-batch adaptive (0.0-3.8)', 'alpha_eff_range': '0.04-0.80 (capped at tau)', 'eval_ppl_holdout': 17.6308, 'eval_loss_holdout': 2.8696, 'eval_holdout_tokens': 4077068, 'eval_method': 'eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)', 'eval_note': 'unified post-hoc eval 2026-05-15; was 17.63/4080000 from inline eval'}
    conclusion: success
    hypothesis: Adaptive b* (from α_eff theory) matches or exceeds grid-searched best-b without grid search, seed=123

  [adaptive_seed456]
    status: DONE
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "512ab4f5-e7a4-4dcd-bf5b-0956557a1477",
  "isSidechain": true,
  "promptId": "792d4fc7-1d48-4678-830d-80fd5a58c95b",
  "agentId": "ab3fc5e12c4a8ae93",
  "type": "user",
  "uuid": "64b33068-e1ca-48ac-9781-82e546f86097",
  "sourceToolAssistantUUID": "512ab4f5-e7a4-4dcd-bf5b-0956557a1477",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-24T04:30:51.798Z_

<details open><summary>🔧 Tool call — Read · `toolu_012Fzj8k1fXe3dWkU1Sz2WvJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c/tool-results/bea8k4j33.txt",
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64b33068-e1ca-48ac-9781-82e546f86097",
  "isSidechain": true,
  "agentId": "ab3fc5e12c4a8ae93",
  "requestId": "req_011CbLmNq3WeGbtJKK1H3FpA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7a42fce-a0e8-43d2-be74-abe6ebf197e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0157pMDLGCG3SJL19dkjZGKZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5592,
      "cache_read_input_tokens": 22925,
      "output_tokens": 153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5592
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 153,
          "cache_read_input_tokens": 22925,
          "cache_creation_input_tokens": 5592,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5592,
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

_source line 17 · 2026-05-24T04:30:52.074Z_

<details><summary>↩ Tool result · `toolu_012Fzj8k1fXe3dWkU1Sz2WvJ`</summary>

```text
1	Traceback (most recent call last):
2	  File "&lt;stdin>", line 3, in &lt;module>
3	NameError: name 'FILE' is not defined
4	
5	============================================================
6	GROUP: B4_rho04
7	============================================================
8	  [adaptive_seed42]
9	    status: DONE
10	    metrics: {'train_loss': 9.2665, 'train_runtime_s': 13115.09, 'total_steps': 6103, 'train_samples_per_second': 7.445, 'train_steps_per_second': 0.465, 'epoch': 0.26, 'weighting_method': 'adaptive', 'tau': 0.8, 'n_min': 3, 'contamination_ratio': 0.4, 'b_star': 'per-batch adaptive (0.0-3.8)', 'alpha_eff_range': '0.03-0.80 (capped at tau)', 'eval_ppl_holdout': 17.644, 'eval_loss_holdout': 2.8704, 'eval_holdout_tokens': 4077068, 'eval_method': 'eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)', 'eval_note': 'unified post-hoc eval 2026-05-15; confirmed unchanged from prior post-hoc (was 17.644/4077068)'}
11	    conclusion: success
12	    hypothesis: Adaptive b* (from α_eff theory) matches or exceeds grid-searched best-b without grid search, seed=42
13	
14	  [adaptive_seed123]
15	    status: DONE
16	    metrics: {'train_loss': 9.2665, 'train_runtime_s': 13197.18, 'total_steps': 6103, 'train_samples_per_second': 7.399, 'train_steps_per_second': 0.462, 'epoch': 0.26, 'weighting_method': 'adaptive', 'tau': 0.8, 'n_min': 3, 'contamination_ratio': 0.4, 'b_star': 'per-batch adaptive (0.0-3.8)', 'alpha_eff_range': '0.04-0.80 (capped at tau)', 'eval_ppl_holdout': 17.6308, 'eval_loss_holdout': 2.8696, 'eval_holdout_tokens': 4077068, 'eval_method': 'eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)', 'eval_note': 'unified post-hoc eval 2026-05-15; was 17.63/4080000 from inline eval'}
17	    conclusion: success
18	    hypothesis: Adaptive b* (from α_eff theory) matches or exceeds grid-searched best-b without grid search, seed=123
19	
20	  [adaptive_seed456]
21	    status: DONE
22	    metrics: {'train_loss': 9.2354, 'train_runtime_s': 13130.09, 'total_steps': 6103, 'train_samples_per_second': 7.437, 'train_steps_per_second': 0.465, 'epoch': 0.26, 'weighting_method': 'adaptive', 'tau': 0.8, 'n_min': 3, 'contamination_ratio': 0.4, 'b_star': 'per-batch adaptive (0.0-3.8)', 'alpha_eff_range': '0.09-0.80 (capped at tau)', 'eval_ppl_holdout': 17.6419, 'eval_loss_holdout': 2.8703, 'eval_holdout_tokens': 4077068, 'eval_method': 'eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)', 'eval_note': 'unified post-hoc eval 2026-05-15; was 17.64/4080000 from inline eval'}
23	    conclusion: success
24	    hypothesis: Adaptive b* (from α_eff theory) matches or exceeds grid-searched best-b without grid search, seed=456
25	
26	  [uniform_seed42]
27	    status: DONE
28	    metrics: {'train_loss': 7.3104, 'total_steps': 6103, 'train_duration_s': 11946, 'eval_ppl_holdout': 17.6939, 'eval_loss_holdout': 2.8732, 'eval_holdout_tokens': 4077068, 'eval_method': 'eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)', 'eval_note': 'unified post-hoc eval 2026-05-15; was 17.69/4080000 from inline eval'}
29	    conclusion: success
30	    hypothesis: Uniform weighting baseline (no provenance information) for comparison with grid-b and adaptive methods
31	
32	  [uniform_seed123]
33	    status: DONE
34	    metrics: {'train_loss': 7.3121, 'total_steps': 6103, 'train_duration_s': 11994, 'eval_ppl_holdout': 17.6861, 'eval_loss_holdout': 2.8728, 'eval_holdout_tokens': 4077068, 'eval_method': 'eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)', 'eval_note': 'unified post-hoc eval 2026-05-15; was 17.69/4080000 from inline eval'}
35	    conclusion: success
36	    hypothesis: Uniform weighting baseline (no provenance information) for comparison with grid-b and adaptive methods
37	
38	  [uniform_seed456]
39	    status: DONE
40	    metrics: {'train_loss': 7.2895, 'total_steps': 6103, 'train_duration_s': 11974, 'eval_ppl_holdout': 17.7015, 'eval_loss_holdout': 2.8737, 'eval_holdout_tokens': 4077068, 'eval_method': 'eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)', 'eval_note': 'unified post-hoc eval 2026-05-15; was 17.70/4080000 from inline eval'}
41	    conclusion: success
42	    hypothesis: Uniform weighting baseline (no provenance information) for comparison with grid-b and adaptive methods
43	
44	
45	============================================================
46	GROUP: B8_rho04
47	============================================================
48	  [bs8_nmin4_adaptive_seed42]
49	    status: DONE
50	    metrics: {'holdout_ppl': 17.650425404986372, 'owt_ppl': 18.332103963757113, 'wiki_ppl': 15.318017946105257, 'holdout_loss': 2.8707598853543677, 'owt_loss': 2.908653837793633, 'wiki_loss': 2.729029779056454}
51	    conclusion: success
52	    hypothesis: Batch-size sensitivity B=8: adaptive reweighting with tau=0.7, n_min=4 (⌊B/2⌋), effective batch=16 (bs=8 × grad_accum=2). Tests whether adaptive advantage scales monotonically with batch size: B=4 Δ=−0.020, B=16 Δ=−0.068. B=8 should fall between, confirming batch-size amplification mechanism. Paired
53	
54	  [bs8_nmin4_adaptive_seed123]
55	    status: DONE
56	    metrics: None
57	    conclusion: failed
58	    hypothesis: Cross-seed replicate (seed=123) of bs8_nmin4_adaptive_seed42 (Δ=−0.044). B=8 n_min=4 adaptive should show consistent negative Δ vs uniform, strengthening batch-size amplification evidence (B=4 Δ=−0.020, B=8 Δ=−0.044, B=16 Δ=−0.068).
59	
60	  [bs8_nmin4_adaptive_seed456]
61	    status: DONE
62	    metrics: None
63	    conclusion: killed
64	    hypothesis: B=8 第三 seed 补全 3-seed paired comparison。seed42 Δ=−0.044, seed123 Δ=−0.056。预期 Δ∈[−0.040, −0.060]。3-seed 均值将提供 batch-size amplification (B=4→B=8→B=16) 的完整统计支撑。
65	
66	  [bs8_nmin4_adaptive_seed123_r2]
67	    status: DONE
68	    metrics: {'eval_ppl_holdout': 17.631, 'eval_ppl_owt': 18.338, 'eval_ppl_wiki': 15.353}
69	    conclusion: success
70	    hypothesis: Cross-seed replicate (seed=123) of bs8_nmin4_adaptive_seed42 (Δ=−0.044). Retry from checkpoint-500 after disk-full crash. B=8 n_min=4 adaptive should show consistent negative Δ vs uniform.
71	
72	  [bs8_nmin4_adaptive_seed456_r2]
73	    status: DONE
74	    metrics: {'holdout_ppl': 17.646, 'holdout_loss': 2.8705, 'owt_ppl': 18.322, 'wiki_ppl': 15.299}
75	    conclusion: success
76	    hypothesis: B=8 第三 seed 补全 3-seed paired comparison。seed42 Δ=−0.044, seed123 Δ=−0.056。预期 Δ∈[−0.040, −0.060]。3-seed 均值将提供 batch-size amplification (B=4→B=8→B=16) 的完整统计支撑。
77	
78	  [bs8_nmin4_uniform_seed42]
79	    status: DONE
80	    metrics: {'holdout_ppl': 17.694185837410274, 'owt_ppl': 18.363068741825792, 'wiki_ppl': 15.336710587451519, 'holdout_loss': 2.8732361018550434, 'owt_loss': 2.910341514026512, 'wiki_loss': 2.730249339271619}
81	    conclusion: success
82	    hypothesis: Batch-size sensitivity B=8 uniform baseline: uniform weighting with effective batch=16 (bs=8 × grad_accum=2). Paired with bs8_nmin4_adaptive_seed42 to measure Δ(adaptive−uniform) at B=8. Expected: B=4 Δ=−0.020, B=8 Δ should be intermediate, B=16 Δ=−0.068. Monotonic trend confirms batch-size amplific
83	
84	  [bs8_nmin4_uniform_seed123]
85	    status: DONE
86	    metrics: None
87	    conclusion: failed
88	    hypothesis: Cross-seed replicate (seed=123) uniform baseline at B=8 for paired comparison with bs8_nmin4_adaptive_seed123. Provides second data point for B=8 batch-size amplification.
89	
90	  [bs8_nmin4_uniform_seed456]
91	    status: DONE
92	    metrics: None
93	    conclusion: killed
94	    hypothesis: seed456 uniform baseline at B=8 for paired comparison with bs8_nmin4_adaptive_seed456. Completes 3-seed set for batch-size amplification statistical analysis.
95	
96	  [bs8_nmin4_uniform_seed123_r2]
97	    status: DONE
98	    metrics: {'eval_ppl_holdout': 17.687, 'eval_ppl_owt': 18.37, 'eval_ppl_wiki': 15.385}
99	    conclusion: success
100	    hypothesis: Cross-seed replicate (seed=123) uniform baseline at B=8. Retry from checkpoint-500 after disk-full crash. Provides second data point for B=8 batch-size amplification.
101	
102	  [bs8_nmin4_uniform_seed456_r2]
103	    status: DONE
104	    metrics: {'holdout_ppl': 17.702, 'holdout_loss': 2.8737, 'owt_ppl': 18.393, 'wiki_ppl': 15.354}
105	    conclusion: success
106	    hypothesis: seed456 uniform baseline at B=8 for paired comparison with bs8_nmin4_adaptive_seed456. Completes 3-seed set for batch-size amplification statistical analysis.
107	
108	
109	============================================================
110	GROUP: B16
111	============================================================
112	  [bs16_adaptive_tau07_seed42]
113	    status: DONE
114	    metrics: {'holdout_loss': 2.8697, 'holdout_ppl': 17.631, 'owt_loss': 2.9074, 'owt_ppl': 18.309, 'wiki_loss': 2.7269, 'wiki_ppl': 15.286, 'train_loss': 2.537}
115	    conclusion: success
116	    hypothesis: Adaptive dual-constraint weighting with bs=16 (n_min=8) produces comparable holdout PPL to the bs=4 (n_min=2) main experiment, demonstrating batch size robustness of the dual-constraint mechanism rather than being an artifact of small-batch dynamics.
117	
118	  [bs16_adaptive_tau07_seed123]
119	    status: DONE
120	    metrics: None
121	    conclusion: failed
122	    hypothesis: Batch size sensitivity replication seed123: adaptive weighting with bs=16 (n_min=8) vs bs=4. If Δ(adaptive−uniform) at bs=16 is comparable to seed42's −0.063, confirms the batch-size amplification effect is not seed-specific. Paired with bs16_uniform_seed123.
123	
124	  [bs16_adaptive_tau07_seed456]
125	    status: DONE
126	    metrics: {'holdout_loss': 2.8704, 'holdout_ppl': 17.645, 'owt_loss': 2.9076, 'owt_ppl': 18.313, 'wiki_loss': 2.7276, 'wiki_ppl': 15.296, 'total_steps': 6103, 'train_loss': 2.528}
127	    conclusion: success
128	    hypothesis: Adaptive dual-constraint weighting with bs=16 (n_min=8, tau=0.7), seed456. Third seed for batch-size amplification effect. Paired with bs16_uniform_seed456. If 3-seed mean Δ(adaptive−uniform) at bs=16 >> bs=4's Δ=−0.020, confirms batch size amplifies adaptive advantage.
129	
130	  [bs16_adaptive_tau07_seed123_r2]
131	    status: DONE
132	    metrics: {'holdout_loss': 2.8688, 'holdout_ppl': 17.616, 'owt_loss': 2.9083, 'owt_ppl': 18.325, 'wiki_loss': 2.731, 'wiki_ppl': 15.348}
133	    conclusion: success
134	    hypothesis: Batch size sensitivity replication seed123: adaptive weighting with bs=16 (n_min=8) vs bs=4. If Δ(adaptive−uniform) at bs=16 is comparable to seed42's −0.063, confirms the batch-size amplification effect is not seed-specific. Paired with bs16_uniform_seed123. Restart of bs16_adaptive_tau07_seed123 w
135	
136	  [bs16_uniform_seed42]
137	    status: DONE
138	    metrics: {'holdout_loss': 2.8732, 'holdout_ppl': 17.694, 'owt_loss': 2.9104, 'owt_ppl': 18.364, 'wiki_loss': 2.7302, 'wiki_ppl': 15.337, 'train_loss': 1.965}
139	    conclusion: success
140	    hypothesis: Uniform baseline at batch_size=16 paired with bs16_adaptive_tau07_seed42. If adaptive Δ (adaptive - uniform) at bs=16 is comparable to bs=4 Δ (−0.020), demonstrates dual-constraint robustness to batch size.
141	
142	  [bs16_uniform_seed123]
143	    status: DONE
144	    metrics: {'holdout_loss': 2.8728, 'holdout_ppl': 17.686, 'owt_loss': 2.9107, 'owt_ppl': 18.369, 'wiki_loss': 2.7332, 'wiki_ppl': 15.381, 'train_loss': 1.997}
145	    conclusion: success
146	    hypothesis: Uniform baseline at batch_size=16, seed123. Paired with bs16_adaptive_tau07_seed123. If Δ(adaptive−uniform) at bs=16 seed123 is comparable to seed42's −0.063, the batch-size amplification is robust across seeds.
147	
148	  [bs16_uniform_seed456]
149	    status: DONE
150	    metrics: {'holdout_loss': 2.8745, 'holdout_ppl': 17.717, 'owt_loss': 2.9118, 'owt_ppl': 18.39, 'wiki_loss': 2.7319, 'wiki_ppl': 15.363, 'total_steps': 6103, 'train_loss': 1.991}
151	    conclusion: success
152	    hypothesis: Uniform baseline at batch_size=16, seed456. Third seed for bs16 batch-size sensitivity analysis. Paired with bs16_adaptive_tau07_seed456. If 3-seed Δ(adaptive−uniform) at bs=16 confirms amplification vs bs=4, strengthens the batch-size mechanism claim.
153	
154	
155	============================================================
156	GROUP: rho06
157	============================================================
158	  [adaptive_rho06_tau07_seed42]
159	    status: DONE
160	    metrics: {'holdout_ppl': 17.735, 'eval_ppl_openwebtext': 18.408, 'eval_ppl_wikipedia': 15.355, 'downstream_arc_easy_acc_norm': 0.6132, 'downstream_arc_challenge_acc_norm': 0.3422, 'downstream_hellaswag_acc_norm': 0.4807, 'downstream_piqa_acc_norm': 0.6861, 'downstream_winogrande_acc': 0.5793, 'downstream_mean': 0.5403}
161	    conclusion: success
162	    hypothesis: Pure adaptive retraining at ρ=0.6, τ=0.7, seed=42. Replaces rho06_tau07_seed42 which was contaminated by hybrid checkpoint. From-scratch training with base Qwen3-0.6B to clean output dir. If PPL < 17.73 (ρ=0.6 τ=0.8 baseline), validates τ=0.7 as universal default across contamination levels.
163	
164	  [adaptive_rho06_tau07_seed123]
165	    status: DONE
166	    metrics: {'holdout_ppl': 17.727, 'eval_ppl_openwebtext': 18.385, 'eval_ppl_wikipedia': 15.329, 'downstream_arc_easy_acc_norm': 0.5951, 'downstream_arc_challenge_acc_norm': 0.3422, 'downstream_hellaswag_acc_norm': 0.4811, 'downstream_piqa_acc_norm': 0.6866, 'downstream_winogrande_acc': 0.5754, 'downstream_mean': 0.5361}
167	    conclusion: success
168	    hypothesis: Pure adaptive training at ρ=0.6, τ=0.7, seed=123. Second seed for clean ρ=0.6 τ=0.7 3-seed set. From-scratch Qwen3-0.6B, no checkpoint reuse. Validates τ=0.7 as universal default across contamination levels.
169	
170	  [adaptive_rho06_tau07_seed456]
171	    status: DONE
172	    metrics: {'holdout_ppl': 17.732, 'eval_ppl_openwebtext': 18.411, 'eval_ppl_wikipedia': 15.424, 'downstream_arc_easy_acc_norm': 0.6128, 'downstream_arc_challenge_acc_norm': 0.3456, 'downstream_hellaswag_acc_norm': 0.4806, 'downstream_piqa_acc_norm': 0.6866, 'downstream_winogrande_acc': 0.562, 'downstream_mean': 0.5375}
173	    conclusion: success
174	    hypothesis: Pure adaptive training at ρ=0.6, τ=0.7, seed=456. Third seed completing clean ρ=0.6 τ=0.7 3-seed set. From-scratch Qwen3-0.6B, no checkpoint reuse. Together with seed42/123, enables paired comparison against ρ=0.6 τ=0.8.
175	
176	  [rho06_tau07_seed42]
177	    status: DONE
178	    metrics: {'eval_ppl_holdout': 17.526, 'eval_ppl_openwebtext': 18.208, 'eval_ppl_wikipedia': 15.267, 'downstream_arc_easy_acc_norm': 0.6208, 'downstream_arc_challenge_acc_norm': 0.3524, 'downstream_hellaswag_acc_norm': 0.4801, 'downstream_piqa_acc_norm': 0.6931, 'downstream_winogrande_acc': 0.5785}
179	    conclusion: failed
180	    hypothesis: Adaptive at ρ=0.6 with τ=0.7 (seed=42). results.tex L97 claims τ=0.7 optimal at ρ=0.6 but lacks complete eval. If PPL < current ρ=0.6 τ=0.8 result (17.73 batch_adaptive or hybrid 17.53), validates τ=0.7 as universal default across contamination levels.
181	
182	  [rho06_tau07_seed123]
183	    status: DONE
184	    metrics: None
185	    conclusion: killed
186	    hypothesis: τ=0.7 at ρ=0.6 seed123: second seed replicating τ=0.7 advantage over τ=0.8 at higher contamination (ρ=0.6). Together with seed42 and seed456, enables paired comparison to confirm τ=0.7 universality across contamination levels.
187	
188	  [rho06_tau07_seed456]
189	    status: DONE
190	    metrics: None
191	    conclusion: killed
192	    hypothesis: τ=0.7 at ρ=0.6 seed456: third seed completing ρ=0.6 τ=0.7 3-seed set. Together with seed42 and seed123, enables paired comparison against ρ=0.6 τ=0.8 to confirm τ=0.7 universality across contamination levels.
193	
194	
195	============================================================
196	GROUP: rho03
197	============================================================
198	  [rho03_adaptive_seed42]
199	    status: DONE
200	    metrics: {'eval_ppl_holdout': 17.422, 'eval_ppl_owt': 18.123, 'eval_ppl_wiki': 15.172}
201	    conclusion: success
202	    hypothesis: At ρ=0.3 (boundary between ρ=0.2 fail and ρ=0.4 success), adaptive τ=0.7 weighting should still improve over uniform but with smaller Δ than ρ=0.4 (Δ=−0.068). This tests the contamination threshold where detect-and-reweight becomes effective, establishing the method's sensitivity boundary.
203	
204	  [rho03_adaptive_seed123]
205	    status: DONE
206	    metrics: {'eval_ppl_holdout': 17.435, 'eval_ppl_owt': 18.148, 'eval_ppl_wiki': 15.165}
207	    conclusion: success
208	    hypothesis: Cross-seed replicate (seed=123) of rho03_adaptive_seed42. At ρ=0.3 boundary, adaptive τ=0.7 should show consistent Δ vs uniform across seeds, establishing statistical reliability of the boundary effect.
209	
210	  [rho03_adaptive_seed456]
211	    status: DONE
212	    metrics: None
213	    conclusion: failed
214	    hypothesis: Third seed (456) for ρ=0.3 boundary check. With seed42 Δ=0.000 and seed123 Δ=+0.002 on holdout, seed456 should confirm ρ=0.3 as neutral transition zone (Δ ≈ 0), enabling paired t-test (N=3) to formally establish non-significance at the boundary.
215	
216	  [rho03_adaptive_seed456_r2]
217	    status: DONE
218	    metrics: {'eval_ppl_holdout': 17.424, 'eval_ppl_owt': 18.115, 'eval_ppl_wiki': 15.161}
219	    conclusion: success
220	    hypothesis: Third seed (456) for ρ=0.3 boundary check (retry, from scratch after disk-full crash). With seed42 Δ=0.000 and seed123 Δ=+0.002 on holdout, seed456 should confirm ρ=0.3 as neutral transition zone.
221	
222	  [rho03_uniform_seed42]
223	    status: DONE
224	    metrics: {'eval_ppl_holdout': 17.422, 'eval_ppl_owt': 18.113, 'eval_ppl_wiki': 15.204}
225	    conclusion: success
226	    hypothesis: Uniform baseline at ρ=0.3 for paired comparison with rho03_adaptive_seed42. Expected PPL between ρ=0.2 uniform (17.336) and ρ=0.4 uniform (17.694), providing the control condition to measure adaptive Δ at the boundary contamination ratio.
227	
228	  [rho03_uniform_seed123]
229	    status: DONE
230	    metrics: {'eval_ppl_holdout': 17.433, 'eval_ppl_owt': 18.126, 'eval_ppl_wiki': 15.204}
231	    conclusion: success
232	    hypothesis: Cross-seed replicate (seed=123) uniform baseline at ρ=0.3 for paired comparison with rho03_adaptive_seed123. Provides second data point for measuring adaptive Δ at the boundary contamination ratio.
233	
234	  [rho03_uniform_seed456]
235	    status: DONE
236	    metrics: {'eval_ppl_holdout': 17.419, 'eval_ppl_owt': 18.109, 'eval_ppl_wiki': 15.168}
237	    conclusion: success
238	    hypothesis: Third seed (456) uniform baseline at ρ=0.3 for paired comparison with rho03_adaptive_seed456. Completes 3-seed set for paired t-test at the boundary contamination ratio.
239	
240	
241	============================================================
242	GROUP: rho02
243	============================================================
244	  [rho02_adaptive_tau08_seed42]
245	    status: DONE
246	    metrics: {'eval_ppl_holdout': 17.382, 'eval_loss_holdout': 2.8555, 'eval_holdout_tokens': 4077068, 'total_steps': 6103, 'train_runtime_seconds': 14599, 'vs_rho02_uniform': '+0.046 (17.382 vs 17.336)', 'vs_rho04_uniform': '-0.312 (17.382 vs 17.694)', 'tau': 0.8, 'rho': 0.2, 'b_star_pct_zero': '40-50%', 'conclusion_note': 'worse than same-rho uniform baseline'}
247	    conclusion: negative
248	    hypothesis: Adaptive weighting with τ=0.8 at ρ=0.2 (low contamination): the dual-constrained algorithm finds meaningful b* even with only 20% contamination, achieving PPL < uniform baseline (17.694), demonstrating proportion-robustness (Claim 3 safe default).
249	
250	  [rho02_adaptive_tau09_seed42]
251	    status: DONE
252	    metrics: None
253	    conclusion: failed
254	    hypothesis: Adaptive weighting with τ=0.9 on ρ=0.2 (low contamination): even at 20% contamination, stricter α_eff threshold should find non-trivial b* and outperform uniform, demonstrating the method works across contamination levels (Claim 3 proportion-robustness).
255	
256	  [rho02_adaptive_tau09_r2]
257	    status: DONE
258	    metrics: {'error': "TypeError: Trainer.__init__() got an unexpected keyword argument 'tokenizer'", 'error_stage': 'initialization', 'training_completed': False, 'note': 'Crashed before any training. Same bug as rho02_adaptive_tau09_seed42. Fix: replace tokenizer= with processing_class= in pretrain_weighted.py line ~101.'}
259	    conclusion: failed
260	
261	  [rho02_adaptive_tau09_r3]
262	    status: DONE
263	    metrics: None
264	    conclusion: failed
265	    hypothesis: Adaptive weighting with τ=0.9 on ρ=0.2 (low contamination): even at 20% contamination, stricter α_eff threshold should find non-trivial b* and outperform uniform, demonstrating proportion-robustness (Claim 3).
266	
267	  [rho02_adaptive_tau09_r4]
268	    status: DONE
269	    metrics: None
270	    conclusion: failed
271	
272	  [rho02_adaptive_tau09_r5]
273	    status: DONE
274	    metrics: {'eval_ppl_holdout': 17.45, 'eval_loss_holdout': 2.8593, 'eval_holdout_tokens': 4077068, 'train_loss': 11.864, 'epoch': 0.47, 'b_star_mean': 4.3493, 'b_star_median': 2.9609, 'b_star_std': 4.3982, 'b_star_min': 0, 'b_star_max': 20, 'b_star_pct_zero': 2.65, 'alpha_eff_mean': 0.8277, 'alpha_eff_median': 0.8826, 'alpha_eff_pct_at_max': 42.95, 'ess_mean': 2.3784, 'ess_median': 2.0121}
275	    conclusion: negative
276	    hypothesis: Adaptive weighting with τ=0.9 on ρ=0.2 (low contamination): even at 20% contamination, stricter α_eff threshold should find non-trivial b* and outperform uniform, demonstrating proportion-robustness (Claim 3).
277	
278	  [rho02_uniform_seed42]
279	    status: DONE
280	    metrics: {'eval_ppl_holdout': 17.336, 'eval_loss_holdout': 2.853, 'eval_holdout_tokens': 4077068}
281	    conclusion: success
282	    hypothesis: Uniform weighting at ρ=0.2 contamination provides the baseline loss level; adaptive reweighting methods should achieve lower loss on clean validation data by downweighting contaminated samples.
283	
284	
285	============================================================
286	GROUP: aeff_only
287	============================================================
288	  [aeff_only_nmin1_seed42]
289	    status: DONE
290	    metrics: {'holdout_ppl': 17.75, 'holdout_loss': 2.8763}
291	    conclusion: success
292	    hypothesis: α_eff-only ablation: adaptive reweighting with n_min=1 (ESS≥1 always satisfied, only α_eff≤τ active). If PPL worse than dual-constrained (n_min=2, 17.674±0.007), ESS constraint has independent value beyond α_eff signal. Addresses R11-C2 + R12-W1.
293	
294	  [aeff_only_nmin1_seed123]
295	    status: DONE
296	    metrics: {'holdout_ppl': 17.733, 'holdout_loss': 2.8755}
297	    conclusion: success
298	    hypothesis: α_eff-only ablation seed123: cross-seed replicate of aeff_only_nmin1_seed42. n_min=1 removes ESS constraint, isolating α_eff signal contribution.
299	
300	  [aeff_only_nmin1_seed456]
301	    status: DONE
302	    metrics: {'holdout_ppl': 17.744, 'holdout_loss': 2.8761}
303	    conclusion: success
304	    hypothesis: α_eff-only ablation seed456: cross-seed replicate. n_min=1 removes ESS constraint. Third seed for paired t-test vs dual-constrained baseline.
305	
306	
307	============================================================
308	GROUP: ess_only
309	============================================================
310	  [ess_only_seed42]
311	    status: DONE
312	    metrics: {'eval_ppl': 17.73, 'eval_loss': 2.875, 'b_star_median': 1.58, 'b_star_mean': 3.51, 'vs_uniform_ppl_delta': '+0.038', 'vs_adaptive_ppl_delta': '+0.08'}
313	    conclusion: success
314	    hypothesis: ESS-only adaptive baseline (max-intervention): b* = max{b : ESS(b) ≥ n_min} — proves min-intervention (adaptive) superior to max-intervention (ESS-only)
315	
316	  [ess_only_seed123]
317	    status: DONE
318	    metrics: {'eval_ppl_holdout': 17.72, 'eval_loss_holdout': 2.8746, 'eval_holdout_tokens': 4077068, 'eval_method': 'eval_perplexity.py on data/human/eval_holdout.jsonl, max_docs=5000, stride=1024, fp16', 'eval_note': 'Also ran on scored_data.jsonl (train data): ppl=9.66, loss=2.2677, tokens=3029693', 'train_loss': 10.2159, 'train_steps': 6103, 'train_runtime_seconds': 12959.5, 'b_star_mean': 3.55, 'b_star_median': 1.5918, 'b_star_std': 4.7209, 'b_star_min': 0.2344, 'b_star_max': 20, 'b_star_p25': 0.8398, 'b_star_p75': 3.8281, 'b_star_p90': 9.5996, 'b_star_count': 21971, 'vs_uniform_ppl_delta': '+0.034', 'vs_adaptive_fix_ppl_delta': '+0.077'}
319	    conclusion: success
320	    hypothesis: ESS-only adaptive baseline (max-intervention) seed=123: b* = max{b : ESS(b) >= n_min} ignores α_eff quality constraint, applying strongest possible downweighting. Multi-seed validation that dual-constraint (min-intervention) consistently outperforms ESS-only.
321	
322	  [ess_only_seed456]
323	    status: DONE
324	    metrics: {'eval_ppl_holdout': 17.76, 'eval_loss_holdout': 2.877, 'eval_holdout_tokens': 4077068, 'train_loss': 1.9364, 'note': 're-eval on westd-41312 latest run (v2)'}
325	    conclusion: success
326	    hypothesis: ESS-only (max-intervention) seed456: b* = max{b : ESS(b) ≥ n_min} — proves dual-constraint adaptive (min-intervention) superior to ESS-only
327	
328	  [ess_only_seed123_r2]
329	    status: DONE
330	    metrics: {'eval_ppl_holdout': 17.721, 'eval_loss_holdout': 2.8747, 'eval_holdout_tokens': 4077068, 'total_steps': 6103, 'train_loss': 6.86, 'train_runtime_seconds': 8674}
331	    conclusion: success
332	    hypothesis: ESS-only (max-intervention) seed123 re-run on westd-41312: b* = max{b : ESS(b) >= n_min} — proves dual-constraint adaptive (min-intervention) superior to ESS-only across seeds
333	
334	  [ess_only_seed456_r2]
335	    status: DONE
336	    metrics: {'eval_ppl_holdout': 17.762, 'eval_loss_holdout': 2.877, 'eval_holdout_tokens': 4077068, 'total_steps': 6103, 'train_loss': 5.998, 'train_runtime_seconds': 7611}
337	    conclusion: success
338	    hypothesis: ESS-only (max-intervention) seed456 re-run on westd-41312: b* = max{b : ESS(b) >= n_min} — proves dual-constraint adaptive (min-intervention) superior to ESS-only across seeds
339	
340	
341	============================================================
342	GROUP: 1_7b
343	============================================================
344	  [adaptive_1_7b_seed42]
345	    status: DONE
346	    metrics: None
347	    conclusion: success
348	    hypothesis: Scale validation: adaptive provenance weighting on Qwen3-1.7B (2.8x larger than 0.6B). If adaptive still outperforms uniform at 1.7B scale, demonstrates method generality beyond small models. Key for Main conference upgrade (D079 Line B). Expected: adaptive < uniform by ≥0.03 PPL (consistent with 0.
349	
350	  [adaptive_1_7b_seed42_v3]
351	    status: DONE
352	    metrics: None
353	    conclusion: killed
354	    hypothesis: Adaptive (dual-constrained) at 1.7B model scale (seed=42, τ=0.8, ρ=0.4). Paired with uniform_1_7b_seed42_v3 to test if adaptive advantage holds at larger model scale. Key for model scaling claim in paper.
355	
356	  [adaptive_1_7b_seed42_v4]
357	    status: DONE
358	    metrics: None
359	    conclusion: failed
360	    hypothesis: Adaptive (dual-constrained) at 1.7B model scale (seed=42, τ=0.8, ρ=0.4). From-scratch on westd-41312. Tests if adaptive advantage holds at larger model scale. v4 replaces v3. Already approved.
361	
362	  [adaptive_1_7b_seed42_v5]
363	    status: DONE
364	    metrics: {'train_loss': 9.139, 'total_steps': 6103, 'train_runtime_s': 18540, 'eval_ppl_holdout': 13.27, 'eval_ppl_openwebtext': 13.282, 'eval_ppl_wikipedia': 10.955, 'downstream_arc_easy_acc_norm': 0.7176, 'downstream_arc_challenge_acc_norm': 0.4403, 'downstream_hellaswag_acc_norm': 0.6164, 'downstream_piqa_acc_norm': 0.7443, 'downstream_winogrande_acc': 0.6069, 'downstream_mean': 0.6251, 'ood_eval_source': 'eval_results/ pipeline'}
365	    conclusion: success
366	    hypothesis: Adaptive (dual-constrained) at 1.7B model scale (seed=42, τ=0.8, ρ=0.4). From-scratch on westd-41312 cuda:1. v5 replaces v4 (disk full at step 500). Paired with uniform_1_7b_seed42_v5 for scaling claim.
367	
368	  [adaptive_1_7b_seed123]
369	    status: DONE
370	    metrics: {'eval_ppl_holdout': 13.25, 'eval_loss_holdout': 2.5843, 'eval_ppl_openwebtext': 13.2909, 'eval_ppl_wikipedia': 10.9521, 'downstream_arc_easy_acc_norm': 0.7138, 'downstream_arc_challenge_acc_norm': 0.4386, 'downstream_hellaswag_acc_norm': 0.6147, 'downstream_piqa_acc_norm': 0.7459, 'downstream_winogrande_acc': 0.6298, 'downstream_mean': 0.6286}
371	    conclusion: success
372	    hypothesis: Adaptive (dual-constrained) at 1.7B model scale (seed=123, τ=0.8, ρ=0.4). From-scratch on westd-41312 cuda:1. Replicates adaptive_1_7b_seed42_v5 (PPL=13.27) with different seed for 3-seed error bars. Paired with uniform_1_7b_seed123.
373	
374	  [adaptive_1_7b_seed456]
375	    status: DONE
376	    metrics: {'eval_ppl_holdout': 13.2668, 'eval_ppl_openwebtext': 13.292, 'eval_ppl_wikipedia': 10.947, 'downstream_arc_easy_acc_norm': 0.7146, 'downstream_arc_challenge_acc_norm': 0.4352, 'downstream_hellaswag_acc_norm': 0.6133, 'downstream_piqa_acc_norm': 0.7443, 'downstream_winogrande_acc': 0.6219, 'downstream_mean': 0.6259, 'ood_eval_source': 'eval_results/ pipeline'}
377	    conclusion: success
378	    hypothesis: Adaptive (dual-constrained) at 1.7B model scale (seed=456, τ=0.8, ρ=0.4). From-scratch on westd-41312 cuda:3. Replicates adaptive_1_7b_seed42_v5 (PPL=13.27) with different seed for 3-seed error bars. Paired with uniform_1_7b_seed456.
379	
380	  [uniform_1_7b_seed42]
381	    status: DONE
382	    metrics: None
383	    conclusion: failed
384	    hypothesis: Uniform weighting baseline on Qwen3-1.7B for scale validation. Control condition for comparing adaptive provenance weighting at larger model scale. Part of D079 Line B.
385	
386	  [uniform_1_7b_seed42_v3]
387	    status: DONE
388	    metrics: None
389	    conclusion: killed
390	    hypothesis: Uniform baseline at 1.7B model scale (seed=42). Provides 1.7B uniform PPL baseline for model scaling comparison. Previous uniform_1_7b_seed42 failed; this is a clean re-run on westd-30476 with verified model weights.
391	
392	  [uniform_1_7b_seed42_v4]
393	    status: DONE
394	    metrics: None
395	    conclusion: failed
396	    hypothesis: Uniform baseline at 1.7B model scale (seed=42). From-scratch training on westd-41312. Provides 1.7B uniform PPL baseline for model scaling comparison. v4 replaces v3 (killed when westd-30476 decommissioned). Already approved.
397	
398	  [uniform_1_7b_seed42_v5]
399	    status: DONE
400	    metrics: {'train_loss': 7.56, 'total_steps': 6103, 'train_runtime_s': 17630, 'eval_ppl_holdout': 13.28, 'eval_ppl_openwebtext': 13.291, 'eval_ppl_wikipedia': 10.919, 'downstream_arc_easy_acc_norm': 0.7235, 'downstream_arc_challenge_acc_norm': 0.4334, 'downstream_hellaswag_acc_norm': 0.6107, 'downstream_piqa_acc_norm': 0.7432, 'downstream_winogrande_acc': 0.6172, 'downstream_mean': 0.6256, 'ood_eval_source': 'eval_results/ pipeline'}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7a42fce-a0e8-43d2-be74-abe6ebf197e3",
  "isSidechain": true,
  "promptId": "792d4fc7-1d48-4678-830d-80fd5a58c95b",
  "agentId": "ab3fc5e12c4a8ae93",
  "type": "user",
  "uuid": "82987739-88c6-445b-9e7f-08d76544436e",
  "sourceToolAssistantUUID": "d7a42fce-a0e8-43d2-be74-abe6ebf197e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-24T04:30:58.184Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YXmQiW1r9xXJ2Gh1WMyQ3x`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c/tool-results/bea8k4j33.txt",
  "limit": 600,
  "offset": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82987739-88c6-445b-9e7f-08d76544436e",
  "isSidechain": true,
  "agentId": "ab3fc5e12c4a8ae93",
  "requestId": "req_011CbLmP77ex3XRYAeMEJyqs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0678c2d6-1d8d-4382-af71-77c967767a9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016QZ7kPYwiu9EVwyLBUP7QL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12102,
      "cache_read_input_tokens": 28517,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12102
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 170,
          "cache_read_input_tokens": 28517,
          "cache_creation_input_tokens": 12102,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12102,
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

_source line 19 · 2026-05-24T04:30:58.467Z_

<details><summary>↩ Tool result · `toolu_01YXmQiW1r9xXJ2Gh1WMyQ3x`</summary>

```text
400	    metrics: {'train_loss': 7.56, 'total_steps': 6103, 'train_runtime_s': 17630, 'eval_ppl_holdout': 13.28, 'eval_ppl_openwebtext': 13.291, 'eval_ppl_wikipedia': 10.919, 'downstream_arc_easy_acc_norm': 0.7235, 'downstream_arc_challenge_acc_norm': 0.4334, 'downstream_hellaswag_acc_norm': 0.6107, 'downstream_piqa_acc_norm': 0.7432, 'downstream_winogrande_acc': 0.6172, 'downstream_mean': 0.6256, 'ood_eval_source': 'eval_results/ pipeline'}
401	    conclusion: success
402	    hypothesis: Uniform baseline at 1.7B model scale (seed=42). From-scratch on westd-41312 cuda:0. v5 replaces v4 (disk full at step 500). 176GB available after cleanup.
403	
404	  [uniform_1_7b_seed123]
405	    status: DONE
406	    metrics: {'eval_ppl_holdout': 13.2648, 'eval_loss_holdout': 2.5851, 'train_loss_final': 7.557, 'total_steps': 6103, 'num_eval_tokens': 4077068, 'eval_ppl_openwebtext': 13.2918, 'eval_ppl_wikipedia': 10.942, 'downstream_arc_easy_acc_norm': 0.726, 'downstream_arc_challenge_acc_norm': 0.4317, 'downstream_hellaswag_acc_norm': 0.6118, 'downstream_piqa_acc_norm': 0.7454, 'downstream_winogrande_acc': 0.6133, 'downstream_mean': 0.6256}
407	    conclusion: success
408	    hypothesis: Uniform baseline at 1.7B model scale (seed=123). From-scratch on westd-41312 cuda:0. Replicates uniform_1_7b_seed42_v5 (PPL=13.28) with different seed for 3-seed error bars. Paired with adaptive_1_7b_seed123 for scaling claim.
409	
410	  [uniform_1_7b_seed456]
411	    status: DONE
412	    metrics: {'eval_ppl_holdout': 13.28, 'eval_loss_holdout': 2.5863, 'train_loss_final': 7.537, 'total_steps': 6103, 'num_eval_tokens': 4077068, 'eval_ppl_openwebtext': 13.307, 'eval_ppl_wikipedia': 10.953, 'downstream_arc_easy_acc_norm': 0.7113, 'downstream_arc_challenge_acc_norm': 0.4224, 'downstream_hellaswag_acc_norm': 0.6132, 'downstream_piqa_acc_norm': 0.7448, 'downstream_winogrande_acc': 0.6251, 'downstream_mean': 0.6234}
413	    conclusion: success
414	    hypothesis: Uniform baseline at 1.7B model scale (seed=456). From-scratch on westd-41312 cuda:2. Replicates uniform_1_7b_seed42_v5 (PPL=13.28) with different seed for 3-seed error bars. Paired with adaptive_1_7b_seed456.
415	
416	  [eval_adaptive_1_7b_v2]
417	    status: DONE
418	    metrics: {'eval_ppl_holdout': 13.27}
419	    conclusion: success
420	    hypothesis: Eval adaptive_1_7b_seed42 on holdout: if adaptive PPL < uniform PPL at 1.7B scale, the provenance weighting advantage persists with larger models, not just 0.6B.
421	
422	  [eval_uniform_1_7b_v3]
423	    status: DONE
424	    metrics: {'eval_ppl_holdout': 13.5}
425	    conclusion: success
426	    hypothesis: Eval uniform_1_7b_seed42_resumed on holdout: baseline PPL for 1.7B uniform training. Paired with eval_adaptive_1_7b_v2 to measure adaptive vs uniform gap at larger scale.
427	
428	
429	============================================================
430	GROUP: llama3b
431	============================================================
432	  [llama3b_adaptive_seed42]
433	    status: DONE
434	    metrics: {'ppl': 10.58, 'eval_loss': 2.359, 'eval_tokens': 4017316}
435	    conclusion: negative
436	    hypothesis: Adaptive b* generalizes across model architectures: Llama-3.2-3B with provenance-weighted training should show PPL improvement over uniform baseline proportional to Qwen3-0.6B results, confirming the method is not architecture-specific and dual-constraint b* transfers.
437	
438	  [llama3b_uniform_seed42]
439	    status: DONE
440	    metrics: {'ppl': 10.38, 'eval_loss': 2.3397, 'eval_tokens': 1526195, 'train_loss': 7.2987, 'train_steps': 6103, 'train_runtime_seconds': 94309}
441	    conclusion: success
442	    hypothesis: Uniform weighting baseline on Llama-3.2-3B establishes reference PPL for cross-model generalization experiment, enabling fair comparison with adaptive weighting on the same architecture and data.
443	
444	
445	============================================================
446	GROUP: gpt2_detector
447	============================================================
448	  [gpt2_adaptive_seed42]
449	    status: DONE
450	    metrics: {'eval_ppl_holdout': 17.79, 'eval_loss_holdout': 2.879, 'train_loss': 10.58, 'train_steps': 6103, 'train_runtime_hours': 3.92}
451	    conclusion: negative
452	    hypothesis: GPT-2 PPL detector (AUC=0.913) + adaptive weighting: tests whether a weaker but practical detector still enables effective adaptive training. If adaptive PPL < uniform with GPT-2 scores, method generalizes beyond high-AUC TF-IDF detector.
453	
454	  [gpt2_adaptive_seed123]
455	    status: DONE
456	    metrics: None
457	    conclusion: failed
458	    hypothesis: GPT-2 PPL detector (AUC=0.913) + adaptive weighting, seed=123. Second seed for detector ablation to confirm gpt2_adaptive_seed42 pattern (PPL=17.79, worse than TF-IDF but still meaningful reweighting). If consistent, supports claim that method works across detector quality levels.
459	
460	  [gpt2_adaptive_seed456]
461	    status: DONE
462	    metrics: None
463	    conclusion: failed
464	    hypothesis: GPT-2 PPL detector (AUC=0.913) + adaptive weighting, seed=456. Third seed for detector ablation to complete 3-seed set with gpt2_adaptive_seed42 (PPL=17.79) and gpt2_adaptive_seed123. Tests reproducibility of method with medium-quality detector.
465	
466	  [gpt2_adaptive_seed123_v2]
467	    status: DONE
468	    metrics: None
469	    conclusion: failed
470	    hypothesis: GPT-2 PPL detector (AUC=0.913) + adaptive weighting, seed=123. V2: rerun without --save_only_model. Replaces corrupted gpt2_adaptive_seed123 (resume caused optimizer loss). Second seed for detector ablation to confirm gpt2_adaptive_seed42 pattern (PPL=17.79).
471	
472	  [gpt2_adaptive_seed123_v3]
473	    status: DONE
474	    metrics: {'holdout_ppl': 17.78848, 'holdout_loss': 2.87855}
475	    conclusion: success
476	    hypothesis: GPT-2 PPL detector (AUC=0.913) + adaptive weighting, seed=123. V3: resume from v2 checkpoint-500 (has optimizer state). No --save_only_model, no inline eval.
477	
478	  [gpt2_adaptive_seed456_v2]
479	    status: DONE
480	    metrics: {'holdout_ppl': 17.79719, 'holdout_loss': 2.87904}
481	    conclusion: success
482	    hypothesis: GPT-2 PPL detector (AUC=0.913) + adaptive weighting, seed=456. V2: from-scratch rerun after disk crash (original used --save_only_model, no optimizer for resume). No --save_only_model, no inline eval.
483	
484	  [gpt2_uniform_seed42]
485	    status: DONE
486	    metrics: {'eval_ppl_holdout': 17.69, 'eval_loss_holdout': 2.8733, 'train_loss': 7.989, 'train_steps': 6103, 'train_runtime_hours': 3.54}
487	    conclusion: success
488	    hypothesis: GPT-2 PPL-scored data with uniform weighting (no provenance reweighting) serves as a baseline; without adaptive weighting, the model cannot distinguish high-quality from low-quality training data, resulting in higher holdout perplexity compared to adaptive methods.
489	
490	
491	============================================================
492	GROUP: ngram_detector
493	============================================================
494	  [ngram_adaptive_seed42]
495	    status: DONE
496	    metrics: {'holdout_ppl': 17.820214, 'holdout_loss': 2.880333}
497	    conclusion: negative
498	    hypothesis: Multi-detector validation: adaptive weighting with n-gram PPL detector (statistical, AUC=0.73) produces lower PPL than uniform, demonstrating method works with fundamentally different detector type (not just neural classifier). Complementary to q_score (Spearman r=-0.36). Part of D079 Line A.
499	
500	  [ngram_adaptive_seed123]
501	    status: DONE
502	    metrics: {'eval_ppl_holdout': 17.823, 'eval_loss_holdout': 2.8805, 'eval_holdout_tokens': 4077068, 'train_loss': 9.289, 'total_steps': 6103}
503	    conclusion: negative
504	    hypothesis: N-gram PPL detector (statistical, AUC=0.73) + adaptive weighting, seed=123. Second seed for detector ablation to confirm ngram_adaptive_seed42 pattern (PPL=17.82). Tests consistency of method with weak statistical detector.
505	
506	  [ngram_adaptive_seed456]
507	    status: DONE
508	    metrics: None
509	    conclusion: failed
510	    hypothesis: N-gram PPL detector (statistical, AUC=0.73) + adaptive weighting, seed=456. Third seed completing 3-seed set for detector ablation. Tests consistency with ngram_adaptive_seed42 (PPL=17.82) and ngram_adaptive_seed123.
511	
512	  [ngram_adaptive_seed456_v2]
513	    status: DONE
514	    metrics: {'holdout_ppl': 17.82607, 'holdout_loss': 2.88066}
515	    conclusion: success
516	    hypothesis: N-gram PPL detector (AUC=0.73) + adaptive weighting, seed=456. V2: from-scratch rerun after disk crash. No --save_only_model, no inline eval.
517	
518	  [ngram_uniform_seed42]
519	    status: DONE
520	    metrics: {'eval_ppl_holdout': 17.69, 'eval_loss_holdout': 2.8733}
521	    conclusion: success
522	    hypothesis: Uniform baseline for n-gram detector comparison. Control condition: uniform weighting on ngram-scored data. Expected to perform worse than ngram_adaptive, confirming adaptive advantage generalizes across detectors.
523	
524	  [eval_ngram_adaptive]
525	    status: DONE
526	    metrics: {'loss': 2.8803, 'perplexity': 17.82, 'tokens': 4077068, 'eval_data': 'data/human/eval_holdout.jsonl', 'max_docs': 5000, 'max_length': 2048, 'checkpoint': 'ngram_adaptive_seed42/final'}
527	    conclusion: success
528	    hypothesis: N-gram adaptive weighting assigns higher weights to documents with rare n-gram patterns, which should yield lower perplexity on held-out human text compared to uniform weighting by better capturing the distribution of natural language.
529	
530	  [eval_ngram_uniform]
531	    status: DONE
532	    metrics: {'loss': 2.8733, 'perplexity': 17.69, 'tokens': 4077068, 'eval_data': 'data/human/eval_holdout.jsonl', 'max_docs': 5000, 'max_length': 2048, 'checkpoint': 'ngram_uniform_seed42/final'}
533	    conclusion: success
534	    hypothesis: Uniform n-gram weighting treats all documents equally regardless of n-gram rarity, serving as a baseline to compare against adaptive weighting for held-out human text perplexity.
535	
536	
537	============================================================
538	GROUP: dr_q03
539	============================================================
540	  [detect_remove_q03_seed42]
541	    status: DONE
542	    metrics: None
543	    conclusion: failed
544	    hypothesis: D&R threshold t=0.3: keep q≤0.3 (116,935 samples, 31.5%), the second most aggressive filtering level. Previous threshold_q03_seed42 on westd-47453 got PPL=17.253. This re-run on westd-30476 serves as reproducibility check and standardizes the threshold sweep on a single server. Part of 5-point D&R s
545	
546	  [detect_remove_q03_seed123]
547	    status: DONE
548	    metrics: {'eval_ppl_holdout': 17.25, 'eval_loss_holdout': 2.8479, 'eval_holdout_tokens': 4077068, 'eval_method': 'sliding_window_stride1024_maxlen2048_fp16_5000docs', 'total_steps': 6103, 'train_loss_final': 11.2441, 'train_runtime_s': 13059, 'epoch': 0.84, 'eval_ppl_openwebtext': 18.03, 'eval_ppl_wikitext': 27.53}
549	    conclusion: success
550	    hypothesis: Cross-seed replication of D&R q03 sweet spot: if seed123 reproduces seed42's PPL=17.25 (the U-curve optimum), q03 is a robust threshold, not a seed42 artifact. Two seeds converging validates the U-shape minimum at q03-q04.
551	
552	  [detect_remove_q03_seed456]
553	    status: DONE
554	    metrics: {'eval_ppl_holdout': 17.2509, 'eval_loss_holdout': 2.8479, 'eval_holdout_tokens': 4077068, 'eval_method': 'eval_perplexity.py --max_docs 5000 --max_length 2048 (final checkpoint)', 'train_loss': 11.255, 'total_steps': 6103, 'eval_ppl_openwebtext': 18.03, 'eval_ppl_wikitext': 27.61}
555	    conclusion: success
556	    hypothesis: D&R threshold t=0.3 seed456: cross-seed replication of q03 sweet spot (PPL=17.25 at seed42). Third seed for 3-seed mean and variance estimate at the D&R optimal threshold.
557	
558	  [detect_remove_q03_seed42_r2]
559	    status: DONE
560	    metrics: {'eval_ppl_holdout': 17.25, 'eval_loss_holdout': 2.848, 'downstream_arc_easy_acc_norm': 0.6301, 'downstream_arc_challenge_acc_norm': 0.3549, 'downstream_hellaswag_acc_norm': 0.4851, 'downstream_piqa_acc_norm': 0.6872, 'downstream_winogrande_acc': 0.5675, 'downstream_eval_method': 'lm_eval 0.4.11, 0-shot, float16, batch_size=auto', 'eval_ppl_openwebtext': 18.004, 'eval_ppl_wikipedia': 15.037}
561	    conclusion: success
562	    hypothesis: D&R threshold t=0.3: keep q≤0.3 (116,935 samples, 31.5%). Second most aggressive filtering level. Part of 9-point D&R sensitivity curve (q01-q09). Previous attempt failed (python: command not found). Rerun on westd-30476.
563	
564	  [eval_q03_r2]
565	    status: DONE
566	    metrics: {'loss': 2.848, 'perplexity': 17.2538, 'num_tokens': 4077068, 'elapsed_seconds': 111, 'downstream_arc_easy_acc_norm': 0.6301, 'downstream_arc_challenge_acc_norm': 0.3549, 'downstream_hellaswag_acc_norm': 0.4851, 'downstream_piqa_acc_norm': 0.6872, 'downstream_winogrande_acc': 0.5675, 'downstream_eval_method': 'lm_eval 0.4.11, 0-shot, float16, batch_size=auto'}
567	    conclusion: success
568	    hypothesis: Detect-remove at q=0.3 threshold (r2 rerun) should show lower PPL than epoch-matched baseline because aggressive filtering removes more low-quality synthetic data while retaining high-provenance human content.
569	
570	
571	============================================================
572	GROUP: dr_epoch
573	============================================================
574	  [detect_remove_q03_epoch_matched_seed42]
575	    status: DONE
576	    metrics: {'eval_ppl_holdout': 17.74, 'eval_loss_holdout': 2.876, 'eval_holdout_tokens': 4077068, 'eval_method': 'sliding_window_stride1024_maxlen2048_fp16_5000docs', 'total_steps': 1927, 'train_loss_final': 11.3917, 'interpretation': 'PPL 17.74 vs epoch-matched q05 (17.65): q03 stricter filtering yields HIGHER PPL (+0.09) under matched training budget, not lower. This contradicts the hypothesis that stricter filtering improves data quality per-token. Meanwhile multi-epoch q03 (17.25) is much lower, confirming that the PPL advantage of q03 in multi-epoch setting comes from more training epochs on filtered data, not from higher per-token quality. Conclusion: under fixed training budget, stricter filtering (q03) actually hurts slightly compared to moderate filtering (q05), likely because removing too many borderline samples reduces diversity without sufficient quality gain.'}
577	    conclusion: success
578	    hypothesis: Epoch-matched D&R q03: 1 epoch through q03 filtered data (116,935 samples, ~63M tokens, 1927 steps). If PPL ≈ 17.65 (same as epoch-matched q05), q03 vs q05 multi-epoch gap (17.25 vs 17.28) comes entirely from extra epochs (3.2x vs 2.4x), not data quality. If PPL significantly below 17.65, q03's stri
579	
580	  [dr_epoch_matched_seed123]
581	    status: DONE
582	    metrics: {'holdout_loss': 2.9087, 'holdout_ppl': 18.332, 'owt_loss': 2.9099, 'owt_ppl': 18.354, 'wiki_loss': 2.705, 'wiki_ppl': 14.955}
583	    conclusion: failed
584	    hypothesis: Epoch-matched D&R seed123: trains on filtered data (q≤0.5, 153725 samples) for exactly 2533 steps with independent linear LR schedule (5e-5→0). Paired with detect_remove_q05_v2_seed123 (full 24414 steps) to independently quantify epoch confound percentage. If full/epoch-matched PPL gap at seed123 is
585	
586	  [dr_epoch_matched_seed456]
587	    status: DONE
588	    metrics: {'holdout_ppl': 17.66, 'owt_ppl': 18.27, 'wiki_ppl': 15.16}
589	    conclusion: success
590	    hypothesis: Epoch-matched D&R seed456: trains on filtered data (q≤0.5, 153725 samples) for exactly 2533 steps with independent linear LR schedule (5e-5→0), effective batch=16 (bs=4 × grad_accum=4). Third seed for epoch confound quantification. Paired with dr_epoch_matched_indep_lr_v2_seed42 (17.651) and dr_epoc
591	
592	  [dr_epoch_matched_seed123_r2]
593	    status: DONE
594	    metrics: {'holdout_loss': 2.8713, 'holdout_ppl': 17.6591, 'owt_loss': 2.9069, 'owt_ppl': 18.2991, 'wiki_loss': 2.7208, 'wiki_ppl': 15.1918, 'eval_holdout_tokens': 4077068, 'eval_owt_tokens': 6767242, 'eval_wiki_tokens': 27000339}
595	    conclusion: success
596	    hypothesis: Epoch-matched D&R seed123 rerun with CORRECT effective batch=16 (batch_size=4 × grad_accum=4). Previous dr_epoch_matched_seed123 was invalid (effective batch=4, missing grad_accum). Trains on filtered data (q≤0.5, 153725 samples) for 2533 steps with independent linear LR schedule (5e-5→0). Paired wi
597	
598	  [epoch_matched_dr_seed123]
599	    status: DONE
600	    metrics: {'eval_ppl_holdout': 17.66, 'eval_loss_holdout': 2.8713, 'eval_holdout_tokens': 4077068, 'eval_method': 'eval_perplexity.py --max_docs 5000 --max_length 2048', 'eval_ppl_openwebtext': 18.3, 'eval_ppl_wikitext': 27.9}
601	    conclusion: success
602	    hypothesis: Cross-seed confirmation of D080: epoch-matched D&R (1 content epoch, ~83M tokens) will produce PPL similar to adaptive (~17.65), proving D&R's apparent 0.36 PPL advantage over adaptive is entirely from multi-epoch training, not data quality filtering. Seed 123 for 3-seed significance.
603	
604	  [epoch_matched_dr_seed456]
605	    status: DONE
606	    metrics: {'eval_ppl_holdout': 17.66, 'eval_loss_holdout': 2.8712, 'eval_holdout_tokens': 4077068, 'eval_method': 'eval_perplexity.py --max_docs 5000 --max_length 2048', 'eval_ppl_openwebtext': 18.27, 'eval_ppl_wikitext': 28.14}
607	    conclusion: success
608	    hypothesis: Cross-seed confirmation of D080: epoch-matched D&R (1 content epoch, ~83M tokens) will produce PPL similar to adaptive (~17.65), proving D&R's apparent 0.36 PPL advantage over adaptive is entirely from multi-epoch training, not data quality filtering. Seed 456 for 3-seed significance.
609	
610	  [eval_epoch_matched_seed123]
611	    status: DONE
612	    metrics: {'loss': 2.8713, 'perplexity': 17.6599, 'num_tokens': 4077068, 'elapsed_seconds': 104.3}
613	    conclusion: success
614	    hypothesis: Epoch-matched detect-remove baseline (seed123) should achieve similar held-out PPL as uniform training, confirming that matched training budget controls for compute rather than data filtering effects.
615	
616	  [eval_epoch_matched_seed456]
617	    status: DONE
618	    metrics: {'loss': 2.8712, 'perplexity': 17.6574, 'num_tokens': 4077068, 'elapsed_seconds': 103.6}
619	    conclusion: success
620	    hypothesis: Epoch-matched detect-remove baseline (seed456) should achieve similar held-out PPL as seed123, confirming reproducibility of the epoch-matched baseline across random seeds.
621	
622	
623	============================================================
624	GROUP: permuted
625	============================================================
626	  [random_reweight_seed42]
627	    status: DONE
628	    metrics: None
629	    conclusion: failed
630	    hypothesis: Random reweighting baseline: U(0,2) random weights (mean=1) replacing detector q-scores. Tests if detector signal is load-bearing — if random weights ≈ adaptive, detector is not contributing. Expected: adaptive > random → provenance signal matters.
631	
632	  [random_reweight_seed123]
633	    status: DONE
634	    metrics: {'holdout_loss': 2.8873, 'holdout_ppl': 17.945, 'owt_loss': 2.9243, 'owt_ppl': 18.622, 'wiki_loss': 2.7448, 'wiki_ppl': 15.562, 'total_steps': 6103, 'train_loss': 8.042, 'train_runtime_seconds': 15820, 'eval_holdout_tokens': 4077068}
635	    conclusion: success
636	    hypothesis: Random reweight seed123 replication: shuffling q_scores before computing adaptive weights destroys the detector's contamination signal while preserving the weight distribution shape. Paired with random_reweight_baseline_seed42 (PPL=17.958) for 2-seed consistency.
637	
638	  [random_reweight_seed456]
639	    status: DONE
640	    metrics: {'eval_ppl_holdout': 17.777, 'eval_loss_holdout': 2.8779, 'eval_holdout_tokens': 4077068, 'total_steps': 6103, 'train_loss': 6.657, 'train_runtime_seconds': 10739}
641	    conclusion: success
642	    hypothesis: U(0,2) random weights baseline seed=456: third seed for Claim 1 random degradation evidence. Random weights drawn from U(0,2) should degrade PPL vs uniform and adaptive, consistent with seed42 and seed123 results, confirming detector q-scores provide real data quality signal beyond random noise.
643	
644	  [random_reweight_baseline_seed42]
645	    status: DONE
646	    metrics: {'holdout_ppl': 17.95829, 'holdout_loss': 2.88805, 'ood_owt_ppl': 18.60614, 'ood_owt_loss': 2.92349, 'ood_wiki_ppl': 15.51906, 'ood_wiki_loss': 2.74207}
647	    conclusion: success
648	    hypothesis: Random reweight baseline: shuffling q_scores before computing adaptive weights destroys the detector's contamination signal while preserving the weight distribution shape. If adaptive (PPL=17.674) outperforms random reweight, the detector signal is load-bearing and not just a regularization artifact
649	
650	  [random_reweight_v2_seed42]
651	    status: DONE
652	    metrics: {'eval_ppl_holdout': 17.83, 'eval_loss_holdout': 2.8809}
653	    conclusion: success
654	    hypothesis: Random reweighting baseline v2: U(0,2) random weights (mean=1) replacing detector q-scores. Tests if detector signal is load-bearing — if random weights ≈ adaptive, detector is not contributing. Expected: adaptive > random → provenance signal matters.
655	
656	  [random_reweight_v2_seed456]
657	    status: DONE
658	    metrics: {'holdout_ppl': 17.951, 'owt_ppl': 18.602, 'wiki_ppl': 15.503}
659	    conclusion: success
660	    hypothesis: Random reweight seed456 v2: uses scored_data_random_shuffle.jsonl + adaptive weighting (matching seed42/seed123 config). Third seed for detector signal load-bearing test. Paired with random_reweight_baseline_seed42 (17.958) and random_reweight_seed123 (17.945).
661	
662	  [random_reweight_seed123_r2]
663	    status: DONE
664	    metrics: None
665	    conclusion: failed
666	    hypothesis: Cross-seed replication (seed123) of random reweighting baseline: U(0,2) random weights replacing detector q-scores. If PPL > uniform (17.688), confirms detector signal is load-bearing across seeds, strengthening Claim 1.
667	
668	  [random_reweight_seed123_r3]
669	    status: DONE
670	    metrics: None
671	    conclusion: failed
672	
673	  [random_reweight_seed123_r4]
674	    status: DONE
675	    metrics: None
676	    conclusion: failed
677	    hypothesis: Cross-seed replication (seed123) of random reweighting baseline: U(0,2) random weights replacing detector q-scores. If PPL > uniform (17.688), confirms detector signal is load-bearing across seeds, strengthening Claim 1.
678	
679	  [random_reweight_seed123_r5]
680	    status: DONE
681	    metrics: {'eval_ppl_holdout': 17.8, 'eval_loss_holdout': 2.8793, 'eval_holdout_tokens': 4077068, 'train_loss': 8.0176, 'train_runtime_seconds': 13267, 'total_steps': 6103, 'vs_uniform_seed123': '+0.114', 'vs_adaptive_fix_seed123': '+0.157', 'vs_random_reweight_v2_seed42': 'consistent (+0.136 seed42 vs +0.114 seed123)'}
682	    conclusion: success
683	    hypothesis: Cross-seed replication (seed123) of random reweighting baseline: U(0,2) random weights replacing detector q-scores. If PPL > uniform (17.688), confirms detector signal is load-bearing across seeds, strengthening Claim 1.
684	
685	
686	============================================================
687	GROUP: grid_b03
688	============================================================
689	  [grid_b0_3_seed42]
690	    status: DONE
691	    metrics: {'eval_ppl_holdout': 17.64, 'eval_loss_holdout': 2.8702, 'eval_holdout_tokens': 4077068, 'eval_method': 'eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)', 'train_loss': 9.1154, 'train_runtime_seconds': 13365.79, 'train_samples_per_second': 7.306, 'total_steps': 6103, 'b_fixed': 0.3, 'alpha_eff_typical_range': '0.07-0.88', 'ess_typical_range': '2.3-4.0'}
692	    conclusion: success
693	    hypothesis: Grid-b sweep b=0.3 on ρ=0.4 data, seed42. Near suspected optimal region (grid-best b=0.5). Tests if b<0.5 improves PPL. Part of b* curve characterization for Claim 2.
694	
695	  [grid_b0_3_seed123]
696	    status: DONE
697	    metrics: None
698	    conclusion: failed
699	    hypothesis: b=0.3 is grid-optimal cross-seed (confirmed at seed42 PPL=17.640 < b=0.5 seed42 17.651). If seed123 also shows b=0.3 as best, confirms grid-best is not seed-specific and strengthens Claim 2 (adaptive ≈ grid-best).
700	
701	  [grid_b0_3_seed456]
702	    status: DONE
703	    metrics: None
704	    conclusion: killed
705	    hypothesis: b=0.3 is grid-optimal cross-seed (confirmed at seed42 PPL=17.640 < b=0.5 seed42 17.651). If seed456 also shows b=0.3 as best, confirms grid-best is not seed-specific and strengthens Claim 2 (adaptive ≈ grid-best).
706	
707	  [grid_b0_3_seed123_r2]
708	    status: DONE
709	    metrics: {'eval_ppl_holdout': 17.5792, 'eval_loss_holdout': 2.8667, 'eval_holdout_tokens': 4077068, 'eval_method': 'eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)', 're_eval_date': '2026-05-18', 'eval_results_path': '/root/autodl-tmp/output/models/grid_b0_3_seed123/eval_results.json', 're_eval_note': 're-eval confirms original PPL=17.58; JSON artifact now saved'}
710	    conclusion: success
711	    hypothesis: b=0.3 is grid-optimal cross-seed (confirmed at seed42 PPL=17.640). Retry on westd-30476 after previous failure. If seed123 b=0.3 PPL < b=0.5 seed123 (17.638), confirms grid-best is not seed-specific.
712	
713	  [grid_b0_3_seed456_r2]
714	    status: DONE
715	    metrics: {'eval_ppl_holdout': 17.64, 'eval_loss_holdout': 2.87, 'eval_holdout_tokens': 4077068, 'total_steps': 6103, 'train_loss': 9.085, 'vs_uniform': '-0.054 (17.64 vs 17.694)', 'vs_grid_b03_seed42': '0.000 (17.64 vs 17.640)', 'vs_grid_b05_seed456': '-0.01 (17.64 vs 17.65)'}
716	    conclusion: success
717	    hypothesis: Cross-seed replication (seed456) of grid b=0.3: if PPL ≈ grid_b0_3_seed42 (17.640) and < b=0.5 seed456 (17.65), confirms grid-best=0.3 is not seed-specific, strengthening Claim 2 (adaptive ≈ grid-best).
718	
719	
720	============================================================
721	GROUP: grid_random
722	============================================================
723	  [grid_b_low_seed42]
724	    status: DONE
725	    metrics: None
726	    conclusion: failed
727	    hypothesis: Grid-b extension to b<0.5 (b=0.1/0.2/0.3 serial), seed42, confirming whether grid-best lies at b=0.5 or below
728	
729	  [grid_b_low_seed42_r2]
730	    status: DONE
731	    metrics: None
732	    conclusion: failed
733	    hypothesis: Low-b grid sweep (b=0.1, 0.2, 0.3) on ρ=0.4 data, seed42. Confirms behavior in b<0.5 region — expect minimal reweighting effect and PPL close to uniform. Establishes that b=0.5 is already near the lower useful bound.
734	
735	  [grid_b_low_seed42_r3]
736	    status: DONE
737	    metrics: None
738	    conclusion: failed
739	    hypothesis: Low-b grid sweep (b=0.1, 0.2, 0.3) on ρ=0.4 data, seed42. R3: uses standalone shell script to avoid quoting issues. Confirms behavior in b<0.5 region.
740	
741	  [grid_b_seed42_batch]
742	    status: DONE
743	    metrics: {'b_values': [0.5, 1, 1.5, 2, 3, 5], 'b0_5_train_loss': 9.598, 'b0_5_completed': True, 'b1_0_completed': True, 'b1_5_completed': True, 'b2_0_current_step': 5149, 'b2_0_total_steps': 6103, 'completed_b_values': [0.5, 1, 1.5, 2, 3], 'current_b': 5, 'total_steps': 6103, 'current_step': 3422, 'b5_0_progress_pct': 56, 'eta_minutes': 95, 'b2_0_completed': True, 'b2_0_train_loss': 10.621, 'b2_0_train_runtime_s': 13034, 'b3_0_completed': True, 'b3_0_train_loss': 10.754, 'b3_0_train_runtime_s': 13036, 'all_completed': True, 'b1_0_train_loss': 10.223, 'b1_5_train_loss': 10.485, 'b5_0_train_loss': 10.858, 'b0_5_runtime_s': 13036, 'b1_0_runtime_s': 12968, 'b1_5_runtime_s': 14789, 'b2_0_runtime_s': 13034, 'b3_0_runtime_s': 13036, 'b5_0_runtime_s': 13115, 'note': 'eval_ppl missing - no --eval_data_path in batch script, post-hoc eval pending', 'b0_5_eval_ppl': 17.651, 'b1_0_eval_ppl': 17.692, 'b1_5_eval_ppl': 17.718, 'b2_0_eval_ppl': 17.741, 'b3_0_eval_ppl': 17.774, 'b5_0_eval_ppl': 17.818, 'eval_holdout_tokens': 4077068, 'best_b': 0.5, 'best_eval_ppl': 17.651}
744	    conclusion: success
745	    hypothesis: Grid-b weighting with 6 b values (0.5, 1.0, 1.5, 2.0, 3.0, 5.0) for seed=42, establishes best-b baseline for comparison with adaptive b*
746	
747	  [grid_b_low_serial_seed42]
748	    status: DONE
749	    metrics: None
750	    conclusion: killed
751	    hypothesis: Grid-b low sweep (b=0.1, 0.2, 0.3 serial, hardcoded) on ρ=0.4 data, seed42. No shell variables — each b value hardcoded to avoid quoting issues. R3 of grid_b_low_seed42.
752	
753	
754	============================================================
755	GROUP: downstream
756	============================================================
757	  [tau07_downstream_eval]
758	    status: DONE
759	    metrics: None
760	    conclusion: failed
761	    hypothesis: Downstream eval for τ=0.7 (3 seeds). Paper switched main results to τ=0.7; must confirm downstream benchmarks match or exceed τ=0.8 and uniform. Reviewer will ask for downstream under recommended setting.
762	
763	  [uniform_seed42_downstream]
764	    status: DONE
765	    metrics: {'downstream_arc_easy_acc_norm': 0.6128, 'downstream_arc_challenge_acc_norm': 0.3481, 'downstream_hellaswag_acc_norm': 0.4836, 'downstream_piqa_acc_norm': 0.6877, 'downstream_winogrande_acc': 0.5856, 'downstream_eval_method': 'lm_eval 0.4.11, 0-shot, float16, batch_size=auto'}
766	    conclusion: success
767	    hypothesis: Downstream benchmark eval (ARC-Easy/Challenge, HellaSwag, PIQA, WinoGrande) for uniform_seed42 baseline. Completes 3-seed uniform downstream comparison needed for Table in paper.
768	
769	
770	============================================================
771	GROUP: detectors
772	============================================================
773	  [detector_modernbert]
774	    status: DONE
775	    metrics: None
776	    conclusion: killed
777	    hypothesis: ModernBERT-base can distinguish Qwen3-0.6B synthetic text from FineWeb human text with AUC>=0.95 and ECE<=0.05
778	
779	  [detector_tfidf_lr]
780	    status: DONE
781	    metrics: {'auc': 0.939, 'accuracy': 0.858, 'ece_raw': 0.24, 'ece_calibrated': 0.048, 'temperature_T': 0.204, 'q_score_mean': 0.6, 'q_score_std': 0.374, 'q_score_median': 0.707, 'mid_range_ratio': 0.463}
782	    conclusion: success
783	    hypothesis: TF-IDF + LogisticRegression detector provides spread q-scores (AUC~0.94, not binarized) for provenance weighting, replacing over-accurate ModernBERT (D007)
784	
785	
786	============================================================
787	GROUP: grid_other
788	============================================================
789	  [grid_b0_1_seed42]
790	    status: DONE
791	    metrics: {'eval_ppl_holdout': 17.657, 'eval_loss_holdout': 2.871}
792	    conclusion: success
793	    hypothesis: Grid-b sweep b=0.1 on ρ=0.4 data, seed42. Minimal reweighting — expect PPL close to uniform (~17.694). Establishes lower bound of useful b range.
794	
795	  [grid_b0_1_seed123]
796	    status: DONE
797	    metrics: {'eval_ppl_holdout': 17.646, 'eval_loss_holdout': 2.8705, 'eval_holdout_tokens': 4077068, 'eval_method': 'eval_perplexity.py --max_docs 5000 --max_length 2048 --fp16'}
798	    conclusion: success
799	    hypothesis: Grid-b sweep b=0.1 on ρ=0.4 data, seed123. Minimal reweighting to establish lower bound of useful b range. Expect PPL close to uniform (~17.694) and consistent with seed42 result (17.657).
800	
801	  [grid_b0_1_seed456]
802	    status: DONE
803	    metrics: {'eval_ppl_holdout': 17.663, 'eval_loss_holdout': 2.8715, 'eval_holdout_tokens': 4077068, 'eval_method': 'eval_perplexity.py --max_docs 5000 --max_length 2048 --fp16'}
804	    conclusion: success
805	    hypothesis: Grid-b sweep b=0.1 on ρ=0.4 data, seed456. Minimal reweighting to establish lower bound of useful b range. Expect PPL close to uniform (~17.694) and consistent with seed42 result (17.657).
806	
807	  [grid_b0_2_seed42]
808	    status: DONE
809	    metrics: {'eval_ppl_holdout': 17.64, 'eval_loss_holdout': 2.8704, 'eval_holdout_tokens': 4077068, 'eval_method': 'eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)'}
810	    conclusion: success
811	    hypothesis: Grid-b sweep b=0.2 on ρ=0.4 data, seed42. Interpolation between b=0.1 and b=0.3 to characterize PPL curve shape in low-b region.
812	
813	  [grid_b0_2_seed123]
814	    status: DONE
815	    metrics: {'eval_ppl_holdout': 17.637, 'eval_loss_holdout': 2.87, 'eval_holdout_tokens': 4077068, 'eval_method': 'eval_perplexity.py --max_docs 5000 --max_length 2048 --stride 1024 --fp16', 'eval_checkpoint': 'checkpoint-5500', 'note': 'eval at checkpoint-5500; final checkpoint degraded due to --save_only_model LR reset on resume'}
816	    conclusion: success
817	    hypothesis: Cross-seed replication (seed123) of grid b=0.2: if PPL ≈ grid_b0_2_seed42 (17.64) and within plateau [0.2,0.3], confirms grid-best region is not seed-specific, strengthening Claim 2.
818	
819	  [grid_b0_2_seed456]
820	    status: DONE
821	    metrics: {'eval_ppl_holdout': 17.645, 'eval_loss_holdout': 2.87, 'eval_holdout_tokens': 4077068, 'eval_method': 'eval_perplexity.py --max_docs 5000 --max_length 2048 --stride 1024 --fp16', 'eval_checkpoint': 'checkpoint-5500', 'note': 'eval at checkpoint-5500; final checkpoint degraded due to --save_only_model LR reset on resume'}
822	    conclusion: success
823	    hypothesis: Cross-seed replication (seed456) of grid b=0.2: 3rd seed for b=0.2 plateau confirmation, completing Claim 2 cross-seed grid curve at the optimal region.
824	
825	  [grid_b0_5_seed123]
826	    status: DONE
827	    metrics: {'eval_ppl_holdout': 17.638, 'eval_loss': 2.87, 'eval_holdout_tokens': 4077068, 'train_loss': 9.601, 'total_steps': 6103, 'train_runtime_s': 13104, 'gpu_hours': 3.8}
828	    conclusion: success
829	    hypothesis: Grid-b sweep b=0.5 seed=123: multi-seed validation that b=0.5 is near-optimal in grid search. Establishes grid-best baseline PPL for comparison with adaptive b* (which should match without requiring grid search).
830	
831	  [grid_b0_5_seed456]
832	    status: DONE
833	    metrics: {'train_loss': 9.5622, 'total_steps': 6103, 'train_runtime_s': 12953.96, 'gpu_hours': 3.6, 'train_samples_per_second': 7.538, 'eval_loss': 2.8705, 'eval_ppl_holdout': 17.65, 'eval_holdout_tokens': 4077068}
834	    conclusion: success
835	    hypothesis: Grid-b weighting with b=0.5, seed=456, for multi-seed validation of best-b baseline
836	
837	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0678c2d6-1d8d-4382-af71-77c967767a9d",
  "isSidechain": true,
  "promptId": "792d4fc7-1d48-4678-830d-80fd5a58c95b",
  "agentId": "ab3fc5e12c4a8ae93",
  "type": "user",
  "uuid": "cf723cb1-6a04-4628-8272-de4dd256d1db",
  "sourceToolAssistantUUID": "0678c2d6-1d8d-4382-af71-77c967767a9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-24T04:31:02.566Z_

Now let me get the remaining experiments not covered yet:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf723cb1-6a04-4628-8272-de4dd256d1db",
  "isSidechain": true,
  "agentId": "ab3fc5e12c4a8ae93",
  "requestId": "req_011CbLmPaTD25BZwjX2okwwA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c64b085c-6d1d-4a6d-86bf-e53cd9a76d50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012snp9yTcZFv1hvFLXoWsgT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12680,
      "cache_read_input_tokens": 40619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12680,
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

_source line 21 · 2026-05-24T04:31:28.688Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01FXgMg23WDCENMRHg2AckeV`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c/tool-results/mcp-agent-ml-research-read_registry-1779596944442.txt\"\n\npython3 << 'PYEOF'\nimport json\n\nFILE = \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c/tool-results/mcp-agent-ml-research-read_registry-1779596944442.txt\"\n\nwith open(FILE) as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Additional experiments for complete picture\nextra_groups = {\n    'llama3b_mmlu': ['llama3b_adaptive_seed42', 'llama3b_uniform_seed42'],\n    'tau07_main': ['tau07_seed42', 'tau07_seed123', 'tau07_seed456'],\n    'adaptive_fix': ['adaptive_fix_seed42', 'adaptive_fix_seed123', 'adaptive_fix_seed456'],\n    'adaptive_v2': ['adaptive_v2_seed42', 'adaptive_v2_seed123', 'adaptive_v2_seed456'],\n    'dr_q01': ['detect_remove_q01_seed42', 'eval_q01_final_v2'],\n    'dr_q04': ['detect_remove_q04_seed42', 'eval_q04'],\n    'dr_q05': ['detect_remove_q05_v2_seed42', 'detect_remove_q05_v2_seed123', 'detect_remove_q05_v2_seed456',\n               'detect_remove_q05_v2_seed123_r2'],\n    'dr_q06': ['detect_remove_q06_seed42', 'eval_q06'],\n    'dr_q07': ['detect_remove_q07_seed42', 'detect_remove_q07_epoch_matched_seed42', 'eval_q07_final'],\n    'dr_q08': ['detect_remove_q08_seed42'],\n    'dr_q09': ['detect_remove_q09_seed42', 'detect_remove_q09_epoch_matched_seed42'],\n    'dr_q02': ['detect_remove_q02_seed42'],\n    'dr_q05_epoch': ['detect_remove_q05_epoch_matched_seed42'],\n    'contamination_60': ['contamination_60_seed42', 'contamination_60_seed123', 'contamination_60_seed42_r2',\n                          'contamination_60_uniform_seed42', 'contamination_60_uniform_seed123', 'contamination_60_uniform_seed456',\n                          'contamination_60_adaptive_seed42_tau08', 'contamination_60_adaptive_seed123_tau08',\n                          'contamination_60_adaptive_seed456'],\n    'grid_b0_3_contamination': ['contamination_60_grid_b0_3_seed42', 'contamination_60_grid_b0_5_seed42',\n                                 'contamination_60_ess_only_seed42', 'contamination_60_ess_only_seed123', 'contamination_60_ess_only_seed456',\n                                 'contamination_60_random_seed42', 'contamination_60_random_seed123', 'contamination_60_random_seed456'],\n    'tau_sweep': ['tau_05_seed42', 'tau_06_seed42', 'tau_07_seed42', 'tau_09_seed42', 'tau_095_seed42', 'tau_0.6_seed42'],\n    'nmin_sweep': ['nmin1_seed42', 'nmin4_seed42', 'nmin5_seed42'],\n    'bs8_other': ['bs8_seed42', 'bs8_auto_nmin_seed42', 'bs8_nmin2_seed42'],\n    'bs16_batch': ['batchsize16_nmin8_seed42', 'batchsize16_nmin8_r2', 'batchsize16_nmin8_r3'],\n    'rho04_batch': ['batch_adaptive_tau_rho04_seed42'],\n    'rho06_batch': ['batch_adaptive_tau_rho06_seed42', 'batch_adaptive_tau_rho06_r2', 'batch_adaptive_tau_rho06_r3',\n                     'batch_adaptive_tau_rho06_r5', 'eval_rho06_batch_v7'],\n    'hybrid': ['hybrid_rho04_seed42', 'hybrid_rho06_seed42'],\n    'baseline_qwen': ['baseline_qwen3_0.6b', 'qwen06b_uniform_seed42'],\n    'fromscratch': ['adaptive_fromscratch_seed42'],\n    'tau08_scratch': ['adaptive_tau08_scratch_seed42', 'adaptive_tau08_scratch_seed42_v2', 'adaptive_tau08_scratch_seed42_v3'],\n    'ood': ['adaptive_ood_seed123', 'adaptive_ood_seed456', 'uniform_ood_seed123', 'uniform_ood_seed456'],\n    'epoch_matched_dr_indep': ['dr_epoch_matched_indep_lr_seed42', 'dr_epoch_matched_indep_lr_v2_seed42',\n                                'uniform_epoch_matched_indep_lr_seed42', 'uniform_epoch_matched_seed456'],\n    'downstream_eval': ['tau07_downstream_eval', 'uniform_seed42_downstream', 'detect_remove_q03_seed42_r2'],\n    'grid_high_b': ['grid_b1_0_seed123', 'grid_b1_0_seed456', 'grid_b1_5_seed123', 'grid_b1_5_seed456',\n                     'grid_b2_0_seed123', 'grid_b2_0_seed456', 'grid_b3_0_seed123', 'grid_b3_0_seed456',\n                     'grid_b5_0_seed123', 'grid_b5_0_seed456'],\n    'golden_ratio': ['golden_ratio_seed42'],\n    'w2_dist': ['w2_distribution_matching_eval'],\n    'threshold_sweep': ['threshold_q03_seed42', 'threshold_q07_seed42'],\n    'diagnostic': ['diagnostic_contamination100'],\n    'tau_nmin': ['tau_05_nmin2_seed42', 'tau_06_nmin2_seed42', 'tau_07_nmin2_seed42', 'tau_09_nmin2_seed42', 'tau_095_nmin2_seed42'],\n    'bs8_nmin2': ['bs8_nmin2_seed42_r2'],\n}\n\nfor group, ids in extra_groups.items():\n    print(f'\\n{\"=\"*60}')\n    print(f'GROUP: {group}')\n    print(f'{\"=\"*60}')\n    for eid in ids:\n        if eid not in experiments:\n            print(f'  [{eid}] NOT FOUND')\n            continue\n        e = experiments[eid]\n        print(f'  [{eid}]')\n        print(f'    status: {e.get(\"status\")}')\n        print(f'    metrics: {e.get(\"metrics\")}')\n        print(f'    conclusion: {e.get(\"conclusion\")}')\n        h = e.get('hypothesis','')\n        if h:\n            print(f'    hypothesis: {h[:300]}')\n        print()\nPYEOF",
  "description": "Extract remaining experiment groups"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c64b085c-6d1d-4a6d-86bf-e53cd9a76d50",
  "isSidechain": true,
  "agentId": "ab3fc5e12c4a8ae93",
  "requestId": "req_011CbLmPaTD25BZwjX2okwwA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f4180eaf-e6a0-411a-8cb0-e1af8fca5ce7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012snp9yTcZFv1hvFLXoWsgT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12680,
      "cache_read_input_tokens": 40619,
      "output_tokens": 2110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12680
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2110,
          "cache_read_input_tokens": 40619,
          "cache_creation_input_tokens": 12680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12680,
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

_source line 22 · 2026-05-24T04:31:28.791Z_

<details><summary>↩ Tool result · `toolu_01FXgMg23WDCENMRHg2AckeV`</summary>

```text
&lt;persisted-output>
Output too large (59.4KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c/tool-results/bw00gfn2k.txt

Preview (first 2KB):
============================================================
GROUP: llama3b_mmlu
============================================================
  [llama3b_adaptive_seed42]
    status: DONE
    metrics: {'ppl': 10.58, 'eval_loss': 2.359, 'eval_tokens': 4017316}
    conclusion: negative
    hypothesis: Adaptive b* generalizes across model architectures: Llama-3.2-3B with provenance-weighted training should show PPL improvement over uniform baseline proportional to Qwen3-0.6B results, confirming the method is not architecture-specific and dual-constraint b* transfers.

  [llama3b_uniform_seed42]
    status: DONE
    metrics: {'ppl': 10.38, 'eval_loss': 2.3397, 'eval_tokens': 1526195, 'train_loss': 7.2987, 'train_steps': 6103, 'train_runtime_seconds': 94309}
    conclusion: success
    hypothesis: Uniform weighting baseline on Llama-3.2-3B establishes reference PPL for cross-model generalization experiment, enabling fair comparison with adaptive weighting on the same architecture and data.


============================================================
GROUP: tau07_main
============================================================
  [tau07_seed42]
    status: DONE
    metrics: {'eval_ppl_holdout': 17.68, 'eval_ppl_openwebtext': 18.348, 'eval_ppl_wikipedia': 15.331, 'downstream_arc_easy_acc_norm': 0.6166, 'downstream_arc_challenge_acc_norm': 0.3473, 'downstream_hellaswag_acc_norm': 0.4795, 'downstream_piqa_acc_norm': 0.6861, 'downstream_winogrande_acc': 0.5817, 'downstream_eval_method': 'lm_eval 0.4.11, 0-shot, float16, batch_size=auto', 'eval_method': 'eval_ppl_ood.py (sliding window, stride=1024, max_docs=5000, fp16)'}
    conclusion: success
    hypothesis: τ=0.7 sensitivity test (seed=42, ρ=0.4). Third seed for τ=0.7, completing 3-seed set (42/123/456) to match τ=0.8's 3 seeds. Enables paired 3-seed comparison for R3-N2 τ sensitivity response.

  [tau07_seed123]
    status: DONE
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4180eaf-e6a0-411a-8cb0-e1af8fca5ce7",
  "isSidechain": true,
  "promptId": "792d4fc7-1d48-4678-830d-80fd5a58c95b",
  "agentId": "ab3fc5e12c4a8ae93",
  "type": "user",
  "uuid": "522c73ea-275b-4a54-bc91-ce8d9a7157d4",
  "sourceToolAssistantUUID": "f4180eaf-e6a0-411a-8cb0-e1af8fca5ce7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-24T04:31:32.290Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GKe6qpse83wWgcQykqAvE7`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c/tool-results/bw00gfn2k.txt",
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "522c73ea-275b-4a54-bc91-ce8d9a7157d4",
  "isSidechain": true,
  "agentId": "ab3fc5e12c4a8ae93",
  "requestId": "req_011CbLmRp644kw7eobV2XZzg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "02d8c80f-1d6c-4cfb-9ff7-a1bc5da68b10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_018b72aNLxFBuV8cThnyvBui",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2973,
      "cache_read_input_tokens": 53299,
      "output_tokens": 154,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2973
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 154,
          "cache_read_input_tokens": 53299,
          "cache_creation_input_tokens": 2973,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2973,
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

_source line 24 · 2026-05-24T04:31:32.606Z_

<details><summary>↩ Tool result · `toolu_01GKe6qpse83wWgcQykqAvE7`</summary>

```text
1	
2	============================================================
3	GROUP: llama3b_mmlu
4	============================================================
5	  [llama3b_adaptive_seed42]
6	    status: DONE
7	    metrics: {'ppl': 10.58, 'eval_loss': 2.359, 'eval_tokens': 4017316}
8	    conclusion: negative
9	    hypothesis: Adaptive b* generalizes across model architectures: Llama-3.2-3B with provenance-weighted training should show PPL improvement over uniform baseline proportional to Qwen3-0.6B results, confirming the method is not architecture-specific and dual-constraint b* transfers.
10	
11	  [llama3b_uniform_seed42]
12	    status: DONE
13	    metrics: {'ppl': 10.38, 'eval_loss': 2.3397, 'eval_tokens': 1526195, 'train_loss': 7.2987, 'train_steps': 6103, 'train_runtime_seconds': 94309}
14	    conclusion: success
15	    hypothesis: Uniform weighting baseline on Llama-3.2-3B establishes reference PPL for cross-model generalization experiment, enabling fair comparison with adaptive weighting on the same architecture and data.
16	
17	
18	============================================================
19	GROUP: tau07_main
20	============================================================
21	  [tau07_seed42]
22	    status: DONE
23	    metrics: {'eval_ppl_holdout': 17.68, 'eval_ppl_openwebtext': 18.348, 'eval_ppl_wikipedia': 15.331, 'downstream_arc_easy_acc_norm': 0.6166, 'downstream_arc_challenge_acc_norm': 0.3473, 'downstream_hellaswag_acc_norm': 0.4795, 'downstream_piqa_acc_norm': 0.6861, 'downstream_winogrande_acc': 0.5817, 'downstream_eval_method': 'lm_eval 0.4.11, 0-shot, float16, batch_size=auto', 'eval_method': 'eval_ppl_ood.py (sliding window, stride=1024, max_docs=5000, fp16)'}
24	    conclusion: success
25	    hypothesis: τ=0.7 sensitivity test (seed=42, ρ=0.4). Third seed for τ=0.7, completing 3-seed set (42/123/456) to match τ=0.8's 3 seeds. Enables paired 3-seed comparison for R3-N2 τ sensitivity response.
26	
27	  [tau07_seed123]
28	    status: DONE
29	    metrics: {'eval_ppl_holdout': 17.666, 'eval_ppl_openwebtext': 18.348, 'eval_ppl_wikipedia': 15.345, 'downstream_arc_easy_acc_norm': 0.6309, 'downstream_arc_challenge_acc_norm': 0.3481, 'downstream_hellaswag_acc_norm': 0.4775, 'downstream_piqa_acc_norm': 0.6866, 'downstream_winogrande_acc': 0.5675, 'downstream_eval_method': 'lm_eval 0.4.11, 0-shot, float16, batch_size=auto', 'eval_method': 'eval_ppl_ood.py (sliding window, stride=1024, max_docs=5000, fp16)'}
30	    conclusion: success
31	    hypothesis: τ=0.7 sensitivity test (seed=123, ρ=0.4). R3-N2 requires multi-seed τ sensitivity data. Currently have τ=0.8 × 3 seeds. Adding τ=0.7 × 2 seeds enables direct paired comparison: if τ=0.7 degrades PPL vs τ=0.8 at same seed, confirms τ=0.8 is near-optimal. If equivalent, suggests robustness to τ choice
32	
33	  [tau07_seed456]
34	    status: DONE
35	    metrics: {'eval_ppl_holdout': 17.677, 'eval_ppl_openwebtext': 18.344, 'eval_ppl_wikipedia': 15.315, 'downstream_arc_easy_acc_norm': 0.6111, 'downstream_arc_challenge_acc_norm': 0.3515, 'downstream_hellaswag_acc_norm': 0.4811, 'downstream_piqa_acc_norm': 0.6834, 'downstream_winogrande_acc': 0.5722, 'downstream_eval_method': 'lm_eval 0.4.11, 0-shot, float16, batch_size=auto', 'eval_method': 'eval_ppl_ood.py (sliding window, stride=1024, max_docs=5000, fp16)'}
36	    conclusion: success
37	    hypothesis: τ=0.7 sensitivity test (seed=456, ρ=0.4). R3-N2 requires multi-seed τ sensitivity data. Paired with tau07_seed123 for 2-seed mean±std at τ=0.7. Direct comparison against adaptive_ood_seed456 (τ=0.8, same seed) isolates τ effect.
38	
39	
40	============================================================
41	GROUP: adaptive_fix
42	============================================================
43	  [adaptive_fix_seed42]
44	    status: DONE
45	    metrics: {'eval_ppl_holdout': 17.6527, 'downstream_arc_easy_acc_norm': 0.6157, 'downstream_arc_challenge_acc_norm': 0.343, 'downstream_hellaswag_acc_norm': 0.4785, 'downstream_piqa_acc_norm': 0.6866, 'downstream_winogrande_acc': 0.5777, 'downstream_mean': 0.5403, 'downstream_eval_method': 'lm_eval 0.4.11, 0-shot, float16', 'eval_ppl_openwebtext': 18.424, 'eval_ppl_wikipedia': 15.473}
46	    conclusion: success
47	    hypothesis: D012 n_min fix (3→2, batch_size//2): adaptive b* with corrected ESS constraint achieves meaningful improvement over uniform baseline (PPL=17.69) for seed=42. Parent: adaptive_seed42 (PPL=17.69, n_min=3 bug)
48	
49	  [adaptive_fix_seed123]
50	    status: DONE
51	    metrics: {'b_star_count': 25906, 'b_star_max': 20, 'b_star_mean': 1.431, 'b_star_median': 0.88, 'b_star_min': 0, 'b_star_note': 'Training-only records (eval checkpoint records with b*=0 excluded)', 'b_star_p25': 0.54, 'b_star_p75': 1.52, 'b_star_pct_0.5_to_1': 35.7, 'b_star_pct_1_to_2': 27.3, 'b_star_pct_2_to_5': 6.3, 'b_star_pct_above_2': 16.1, 'b_star_pct_above_5': 1.9, 'b_star_pct_below_0.5': 20.9, 'b_star_std': 2.029, 'epoch': 0.26, 'eval_holdout_tokens': 4077068, 'eval_loss': 2.8704, 'eval_loss_holdout': 2.8704, 'eval_method': 'eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)', 'eval_note': 'unified post-hoc eval 2026-05-15; was 17.643/4077068', 'eval_ppl_holdout': 17.6432, 'eval_tokens': 4077068, 'total_steps': 6103, 'train_loss_weighted': 7.517, 'train_runtime_s': 10347, 'ood_note': 'OOD eval not available — checkpoint on decommissioned westd-47453; adaptive_ood_seed123 has OOD from from-scratch retrain'}
52	    conclusion: success
53	    hypothesis: D012 n_min fix (3→2, batch_size//2): adaptive b* with corrected ESS constraint maintains or improves seed123 performance (baseline adaptive PPL=17.63, uniform PPL=17.69)
54	
55	  [adaptive_fix_seed456]
56	    status: DONE
57	    metrics: {'b_star_count': 26396, 'b_star_max': 20, 'b_star_mean': 1.416, 'b_star_median': 0.88, 'b_star_min': 0, 'b_star_note': 'Training-only records (eval checkpoint records with b*=0 excluded)', 'b_star_p25': 0.54, 'b_star_p75': 1.52, 'b_star_pct_0.5_to_1': 35.7, 'b_star_pct_1_to_2': 27.3, 'b_star_pct_above_2': 16.1, 'b_star_pct_below_0.5': 20.9, 'b_star_std': 1.993, 'eval_holdout_tokens': 4077068, 'eval_loss_holdout': 2.8711, 'eval_method': 'eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)', 'eval_note': 'unified post-hoc eval 2026-05-15; was 17.66/4077068', 'eval_ppl_holdout': 17.6566, 'eval_tokens': 4077068, 'total_steps': 6103, 'train_loss': 8.3124, 'train_runtime': 11436.05, 'train_samples_per_second': 8.539, 'train_steps_per_second': 0.534, 'ood_note': 'OOD eval not available — checkpoint on decommissioned westd-47453; adaptive_ood_seed456 has OOD from from-scratch retrain'}
58	    conclusion: success
59	    hypothesis: D012 n_min fix (3→2, batch_size//2): adaptive b* with corrected ESS constraint maintains or improves seed456 performance (baseline adaptive PPL=17.64, uniform PPL=17.70)
60	
61	
62	============================================================
63	GROUP: adaptive_v2
64	============================================================
65	  [adaptive_v2_seed42]
66	    status: DONE
67	    metrics: None
68	    conclusion: killed
69	    hypothesis: Adaptive v2 (n_min fix: 3→2, no EMA) fixes ESS clamping issue, achieves meaningful improvement over uniform baseline for seed=42
70	
71	  [adaptive_v2_seed123]
72	    status: DONE
73	    metrics: None
74	    conclusion: killed
75	    hypothesis: Adaptive v2 (n_min fix: 3→2, no EMA) maintains or improves seed123 performance (baseline adaptive PPL=17.63)
76	
77	  [adaptive_v2_seed456]
78	    status: DONE
79	    metrics: None
80	    conclusion: killed
81	    hypothesis: Adaptive v2 (n_min fix: 3→2, no EMA) maintains or improves seed456 performance (baseline adaptive PPL=17.64)
82	
83	
84	============================================================
85	GROUP: dr_q01
86	============================================================
87	  [detect_remove_q01_seed42]
88	    status: DONE
89	    metrics: {'eval_ppl_holdout': 17.4, 'eval_ppl_openwebtext': 18.22, 'eval_ppl_wikitext': 28.22}
90	    conclusion: success
91	    hypothesis: D&R extreme threshold q>0.1: removes all samples with q_score>0.1, keeping only the most confidently clean data. Tests D&R sensitivity to threshold — if PPL degrades severely, filtering is too aggressive and most data is discarded. Paired with q>0.3/0.5/0.7/0.9 to map the full threshold-PPL curve, s
92	
93	  [eval_q01_final_v2]
94	    status: DONE
95	    metrics: {'loss': 2.8563, 'perplexity': 17.3965, 'num_tokens': 4077068, 'elapsed_seconds': 105.1}
96	    conclusion: success
97	    hypothesis: Detect-remove at q=0.1 (most aggressive filtering) should show the lowest PPL among all thresholds if data quality dominates, or degraded PPL if the severe data reduction causes underfitting.
98	
99	
100	============================================================
101	GROUP: dr_q04
102	============================================================
103	  [detect_remove_q04_seed42]
104	    status: DONE
105	    metrics: {'eval_ppl_holdout': 17.26, 'eval_loss_holdout': 2.8485, 'downstream_arc_easy_acc_norm': 0.6107, 'downstream_arc_challenge_acc_norm': 0.3567, 'downstream_hellaswag_acc_norm': 0.4819, 'downstream_piqa_acc_norm': 0.6931, 'downstream_winogrande_acc': 0.5659, 'downstream_eval_method': 'lm_eval 0.4.11, 0-shot, float16, batch_size=auto', 'eval_ppl_openwebtext': 18.001, 'eval_ppl_wikipedia': 15.038}
106	    conclusion: success
107	    hypothesis: D&R threshold t=0.4: keep q≤0.4 samples. Densification point between q03 (31.5%) and q05 (41.4%, PPL=17.28). Helps pinpoint the PPL sweet spot and quantify sensitivity. Part of expanded 9-point D&R threshold curve.
108	
109	  [eval_q04]
110	    status: DONE
111	    metrics: {'loss': 2.8485, 'perplexity': 17.2626, 'num_tokens': 4077068, 'elapsed_seconds': 103.8, 'downstream_arc_easy_acc_norm': 0.6107, 'downstream_arc_challenge_acc_norm': 0.3567, 'downstream_hellaswag_acc_norm': 0.4819, 'downstream_piqa_acc_norm': 0.6931, 'downstream_winogrande_acc': 0.5659, 'downstream_eval_method': 'lm_eval 0.4.11, 0-shot, float16, batch_size=auto'}
112	    conclusion: success
113	    hypothesis: Detect-remove at q=0.4 threshold should show lower PPL than epoch-matched baseline, with slightly higher PPL than q=0.3 due to retaining more borderline-quality documents.
114	
115	
116	============================================================
117	GROUP: dr_q05
118	============================================================
119	  [detect_remove_q05_v2_seed42]
120	    status: DONE
121	    metrics: {'holdout_loss': 2.8499, 'holdout_ppl': 17.2853, 'owt_loss': 2.8911, 'owt_ppl': 18.0139, 'wiki_loss': 2.7116, 'wiki_ppl': 15.0528, 'train_loss': 11, 'total_steps': 6103}
122	    conclusion: success
123	    hypothesis: D&R hard filtering baseline with CORRECT filtered data (q≤0.5, 153725 samples, 86.4% real). Full 6103-step linear schedule. Paired with adaptive reweighting to compare hard filtering vs soft reweighting approaches. If D&R PPL > adaptive, soft reweighting extracts more value from contaminated data th
124	
125	  [detect_remove_q05_v2_seed123]
126	    status: DONE
127	    metrics: {'holdout_loss': 2.8545, 'holdout_ppl': 17.3656, 'owt_loss': 2.9013, 'owt_ppl': 18.198, 'wiki_loss': 2.7234, 'wiki_ppl': 15.2318, 'total_steps': 24414, 'train_loss': 2.76}
128	    conclusion: failed
129	    hypothesis: D&R hard filtering seed123 replication with CORRECT filtered data (q≤0.5, 153725 samples, 86.4% real). Paired with detect_remove_q05_v2_seed42 for 2-seed consistency.
130	
131	  [detect_remove_q05_v2_seed456]
132	    status: DONE
133	    metrics: {'holdout_ppl': 17.277, 'holdout_loss': 2.8493, 'owt_ppl': 18.017, 'owt_loss': 2.8913, 'wiki_ppl': 15.04, 'wiki_loss': 2.7106, 'train_loss': 11.01, 'total_steps': 6103, 'training_time_s': 14920}
134	    conclusion: success
135	    hypothesis: D&R hard filtering (remove q≤0.5 samples) with seed 456 should produce holdout PPL consistent with seed42 and seed123, confirming the stability of the filtering approach across random seeds.
136	
137	  [detect_remove_q05_v2_seed123_r2]
138	    status: DONE
139	    metrics: {'holdout_loss': 2.8491, 'holdout_ppl': 17.272, 'owt_loss': 2.8908, 'owt_ppl': 18.008, 'wiki_loss': 2.7111, 'wiki_ppl': 15.047, 'eval_holdout_tokens': 4077068, 'eval_owt_tokens': 6767242, 'eval_wiki_tokens': 27000339, 'total_steps': 6103, 'train_loss': 11.01}
140	    conclusion: success
141	    hypothesis: D&R hard filtering seed123 rerun with CORRECT effective batch=16 (batch_size=4 × grad_accum=4). Previous detect_remove_q05_v2_seed123 was invalid (effective batch=4). Full training on filtered data (q≤0.5, 153725 samples) for ~6103 steps with 200M token budget. Paired with detect_remove_q05_v2_seed4
142	
143	
144	============================================================
145	GROUP: dr_q06
146	============================================================
147	  [detect_remove_q06_seed42]
148	    status: DONE
149	    metrics: {'eval_ppl_holdout': 17.3, 'eval_loss_holdout': 2.8507}
150	    conclusion: success
151	    hypothesis: D&R threshold t=0.6: keep q≤0.6 samples. Densification point between q05 (PPL=17.28) and q07 (PPL=17.32). Shows degradation slope as more contaminated data is included. Part of expanded 9-point D&R threshold curve.
152	
153	  [eval_q06]
154	    status: DONE
155	    metrics: {'loss': 2.8507, 'perplexity': 17.2993, 'num_tokens': 4077068, 'elapsed_seconds': 106.9}
156	    conclusion: success
157	    hypothesis: Detect-remove at q=0.6 threshold should show lower PPL than epoch-matched baseline but higher than q=0.3/0.4 as the less aggressive filtering retains more synthetic-origin content.
158	
159	
160	============================================================
161	GROUP: dr_q07
162	============================================================
163	  [detect_remove_q07_seed42]
164	    status: DONE
165	    metrics: {'eval_ppl_holdout': 17.32, 'eval_loss_holdout': 2.8519, 'eval_holdout_tokens': 4077068, 'eval_method': 'eval_perplexity.py --max_docs 5000 --max_length 2048 (final checkpoint)', 'note': 'final checkpoint, replaces partial ckpt-3500 PPL=17.49'}
166	    conclusion: success
167	    hypothesis: D&R threshold t=0.7: keep q≤0.7 (184,908 samples, 49.8%), removing moderately suspicious data. Tests intermediate filtering aggressiveness between t=0.5 (41.4%) and t=0.9 (61.6%). Part of threshold sensitivity sweep.
168	
169	  [detect_remove_q07_epoch_matched_seed42]
170	    status: DONE
171	    metrics: {'eval_ppl_holdout': 17.62, 'eval_loss_holdout': 2.8689, 'eval_holdout_tokens': 4077068, 'eval_method': 'sliding_window_stride1024_maxlen2048_fp16_5000docs', 'total_steps': 3047}
172	    conclusion: success
173	    hypothesis: Epoch-matched D&R q07: 1 epoch through q07 filtered data (184,908 samples, ~100M tokens, 3047 steps). Part of 5-point epoch-matched curve (q01/q03/q05/q07/q09). If PPL converges to ~17.65-17.74 range like q03(17.74) and q05(17.65), confirms U-shape sweet spot is entirely multi-epoch artifact across 
174	
175	  [eval_q07_final]
176	    status: DONE
177	    metrics: {'loss': 2.8519, 'perplexity': 17.3201, 'num_tokens': 4077068, 'elapsed_seconds': 103.8}
178	    conclusion: success
179	    hypothesis: Detect-remove at q=0.7 threshold should show lower PPL than epoch-matched baseline, with the PPL gap narrowing as higher thresholds retain more data including lower-provenance documents.
180	
181	
182	============================================================
183	GROUP: dr_q08
184	============================================================
185	  [detect_remove_q08_seed42]
186	    status: DONE
187	    metrics: {'eval_ppl_holdout': 17.3442, 'eval_loss_holdout': 2.8533, 'downstream_arc_easy_acc_norm': 0.6086, 'downstream_arc_challenge_acc_norm': 0.3592, 'downstream_hellaswag_acc_norm': 0.4855, 'downstream_piqa_acc_norm': 0.6937, 'downstream_winogrande_acc': 0.5817, 'downstream_eval_method': 'lm_eval 0.4.11, 0-shot, float16, batch_size=auto', 'eval_ppl_openwebtext': 18.039, 'eval_ppl_wikipedia': 15.066}
188	    conclusion: success
189	    hypothesis: D&R threshold t=0.8: keep q≤0.8 samples (~210K). Lenient filtering near q09 (228K). Part of 9-point D&R sensitivity curve. Expected PPL between q07 (17.32) and q09 (17.42) confirming right side of U-shape.
190	
191	
192	============================================================
193	GROUP: dr_q09
194	============================================================
195	  [detect_remove_q09_seed42]
196	    status: DONE
197	    metrics: {'eval_ppl_holdout': 17.42, 'eval_loss_holdout': 2.8577, 'eval_holdout_tokens': 4077068, 'eval_method': 'eval_perplexity.py --checkpoints --max_docs 5000 --max_length 2048 --stride 1024 --fp16'}
198	    conclusion: success
199	    hypothesis: D&R threshold t=0.9 (most lenient): keep q≤0.9 (228,743 samples, 61.6%), only removing the most confidently synthetic data. Expected PPL close to uniform baseline since minimal data is removed. Part of threshold sensitivity sweep (t=0.1/0.3/0.5/0.7/0.9) showing D&R requires careful calibration while
200	
201	  [detect_remove_q09_epoch_matched_seed42]
202	    status: DONE
203	    metrics: {'eval_ppl_holdout': 17.628, 'eval_loss_holdout': 2.8695, 'eval_holdout_tokens': 4077068, 'eval_method': 'sliding_window_stride1024_maxlen2048_fp16_5000docs', 'total_steps': 3770, 'train_loss_final': 9.9127}
204	    conclusion: success
205	    hypothesis: Epoch-matched D&R q09: 1 epoch through q09 filtered data (228,743 samples, ~124M tokens, 3770 steps). Most lenient filter in the curve (61.6% retained, only 1.6x epochs in multi-epoch). Part of 5-point epoch-matched curve. If PPL converges to ~17.65-17.74 range, confirms U-shape is entirely multi-ep
206	
207	
208	============================================================
209	GROUP: dr_q02
210	============================================================
211	  [detect_remove_q02_seed42]
212	    status: DONE
213	    metrics: {'eval_ppl_holdout': 17.27, 'eval_loss_holdout': 2.8491, 'eval_holdout_tokens': 4077068, 'eval_method': 'eval_perplexity.py --max_docs 5000 --max_length 2048 (final checkpoint)', 'train_loss': 11.348, 'train_steps': 6103, 'data_count': 91654, 'eval_ppl_openwebtext': 18.06, 'eval_ppl_wikitext': 27.64}
214	    conclusion: success
215	    hypothesis: D&R q>0.2 threshold retains ~23% of data (q_score<=0.2). Maps the left side of the U-curve between q01(17.40) and q03(17.25). If PPL closer to q03 than q01, the steep rise only occurs at extreme filtering (q01). If closer to q01, the left branch rises steeply from q03 onward.
216	
217	
218	============================================================
219	GROUP: dr_q05_epoch
220	============================================================
221	  [detect_remove_q05_epoch_matched_seed42]
222	    status: DONE
223	    metrics: {'eval_ppl_holdout': 17.65, 'eval_loss_holdout': 2.8707, 'eval_holdout_tokens': 4077068, 'train_loss_final': 3.184, 'total_steps': 2533, 'eval_method': 'eval_perplexity.py --max_docs 5000 --max_length 2048 --stride 1024 --fp16', 'vs_full_dr_q05': '+0.360 (17.650 vs 17.290, epoch-matched worse)', 'vs_adaptive': '-0.001 (17.650 vs 17.651, nearly identical to adaptive)', 'interpretation': 'D&R 0.36 PPL advantage over epoch-matched is entirely from multi-epoch training on clean data, not from data quality filtering'}
224	    conclusion: success
225	    hypothesis: Epoch-matched control: training with uniform weighting on filtered data (q>0.5 removed) for exactly 2533 steps (matching content-level 1 epoch of the contaminated data). If PPL is comparable to the full 6103-step D&R run, the D&R benefit comes from data quality not extra training; if PPL is worse, t
226	
227	
228	============================================================
229	GROUP: contamination_60
230	============================================================
231	  [contamination_60_seed42]
232	    status: DONE
233	    metrics: None
234	    conclusion: failed
235	    hypothesis: ρ=0.6 contamination robustness test: adaptive weighting (τ=0.8, n_min=2) on higher contamination ratio data. Baseline adaptive_fix_seed42 (ρ=0.4) PPL=17.6527. Tests if adaptive method degrades gracefully as contamination increases from 0.4→0.6.
236	
237	  [contamination_60_seed123]
238	    status: DONE
239	    metrics: {'eval_ppl_holdout': 17.732, 'eval_loss_holdout': 2.8754, 'eval_holdout_tokens': 4077068, 'train_loss': 9.6302, 'train_runtime_seconds': 13638.6, 'total_steps': 6103, 'eval_method': 'eval_perplexity.py --max_docs 5000 --max_length 2048'}
240	    conclusion: success
241	    hypothesis: Cross-seed replication (seed123) of adaptive weighting at ρ=0.6: confirms contamination_60_seed42_r2 result is not seed-specific, strengthening Claim 3 proportion-robustness across contamination levels.
242	
243	  [contamination_60_seed42_r2]
244	    status: DONE
245	    metrics: {'eval_ppl_holdout': 17.74, 'eval_loss_holdout': 2.8759, 'eval_tokens': 4077068, 'eval_method': 'sliding_window_2048_stride1024', 'train_loss': 9.6349, 'train_runtime_seconds': 14092.25}
246	    conclusion: success
247	    hypothesis: Retry of contamination_60_seed42 (failed due to GPU conflict on cuda:2). ρ=0.6 adaptive weighting (τ=0.8, n_min=2) on higher contamination data. Tests graceful degradation as ρ increases from 0.4→0.6.
248	
249	  [contamination_60_uniform_seed42]
250	    status: DONE
251	    metrics: {'eval_ppl_holdout': 17.766, 'eval_loss_holdout': 2.8773, 'eval_tokens': 4077068, 'eval_method': 'eval_perplexity.py sliding-window (stride=1024, max_length=2048, fp16) on data/human/eval_holdout.jsonl', 'train_loss': 7.649, 'train_runtime_seconds': 12904}
252	    conclusion: success
253	    hypothesis: ρ=0.6 uniform baseline: no reweighting on 60% contamination data. Establishes baseline PPL degradation at higher contamination for comparison with adaptive and grid methods.
254	
255	  [contamination_60_uniform_seed123]
256	    status: DONE
257	    metrics: {'eval_ppl_holdout': 17.754, 'eval_loss_holdout': 2.8766, 'eval_holdout_tokens': 4077068, 'total_steps': 6103, 'eval_method': 'eval_perplexity.py --max_docs 5000 --max_length 2048'}
258	    conclusion: success
259	    hypothesis: Uniform baseline at ρ=0.6 seed123: pairs with contamination_60_seed123 (adaptive) to form seed123 uniform/adaptive contrast. If adaptive PPL < uniform PPL at ρ=0.6, confirms Claim 3 proportion-robustness holds cross-seed at higher contamination.
260	
261	  [contamination_60_uniform_seed456]
262	    status: DONE
263	    metrics: {'eval_ppl_holdout': 17.77, 'eval_loss_holdout': 2.8775, 'eval_holdout_tokens': 4077068, 'train_loss': 7.637, 'train_runtime_seconds': 12845, 'total_steps': 6103, 'eval_method': 'eval_perplexity.py --max_docs 5000 --max_length 2048', 'eval_ppl_openwebtext': 18.449, 'eval_ppl_wikipedia': 15.42, 'ood_eval_source': 'eval_results/ pipeline (consistent with adaptive tau07 evals)'}
264	    conclusion: success
265	    hypothesis: Uniform baseline at ρ=0.6 seed456: pairs with contamination_60_seed456 (adaptive) to form seed456 uniform/adaptive contrast. If adaptive PPL < uniform PPL at ρ=0.6, confirms Claim 3 proportion-robustness across seeds.
266	
267	  [contamination_60_adaptive_seed42_tau08]
268	    status: DONE
269	    metrics: {'holdout_ppl': 17.74, 'eval_ppl_openwebtext': 18.42, 'eval_ppl_wikipedia': 15.37, 'downstream_arc_easy_acc_norm': 0.612, 'downstream_arc_challenge_acc_norm': 0.3439, 'downstream_hellaswag_acc_norm': 0.4802, 'downstream_piqa_acc_norm': 0.685, 'downstream_winogrande_acc': 0.5777, 'downstream_mean': 0.5398}
270	    conclusion: success
271	    hypothesis: Retrain adaptive (ρ=0.6, τ=0.8, seed=42) from scratch on Qwen3-0.6B to obtain checkpoint for OOD+downstream eval. Original contamination_60_seed42_r2 (PPL=17.74) confirmed holdout performance but checkpoint was cleaned up. Paired with seed123/456 for 3-seed τ=0.8 comparison against τ=0.7 (17.735/17.
272	
273	  [contamination_60_adaptive_seed123_tau08]
274	    status: DONE
275	    metrics: {'holdout_ppl': 17.73, 'eval_ppl_openwebtext': 18.4, 'eval_ppl_wikipedia': 15.34, 'downstream_arc_easy_acc_norm': 0.6014, 'downstream_arc_challenge_acc_norm': 0.3447, 'downstream_hellaswag_acc_norm': 0.4804, 'downstream_piqa_acc_norm': 0.6877, 'downstream_winogrande_acc': 0.5699, 'downstream_mean': 0.5368}
276	    conclusion: success
277	    hypothesis: Retrain adaptive (ρ=0.6, τ=0.8, seed=123) from scratch on Qwen3-0.6B to obtain checkpoint for OOD+downstream eval. Original contamination_60_seed123 (PPL=17.732) confirmed holdout performance but checkpoint was cleaned up. Paired with seed42/456 for 3-seed τ=0.8 comparison against τ=0.7.
278	
279	  [contamination_60_adaptive_seed456]
280	    status: DONE
281	    metrics: {'eval_ppl_holdout': 17.735, 'eval_loss_holdout': 2.8755, 'eval_holdout_tokens': 4077068, 'eval_method': 'eval_perplexity.py --max_docs 5000 --stride 1024 --fp16'}
282	    conclusion: success
283	    hypothesis: Cross-seed replication (seed456) of adaptive weighting at ρ=0.6: pairs with contamination_60_uniform_seed456 for 3rd seed contrast. If adaptive PPL < uniform PPL at ρ=0.6, completes Claim 3 proportion-robustness 3-seed evidence.
284	
285	
286	============================================================
287	GROUP: grid_b0_3_contamination
288	============================================================
289	  [contamination_60_grid_b0_3_seed42]
290	    status: DONE
291	    metrics: {'eval_ppl_holdout': 17.634, 'eval_method': 'eval_perplexity.py --max_docs 5000 --max_length 2048 --stride 1024 --fp16', 'checkpoint_1500_ppl': 18.583, 'total_steps': 6103, 'note': 'resume from checkpoint-1500 with ~30% LR offset; final PPL improved over checkpoint-1500, no degradation'}
292	    conclusion: success
293	    hypothesis: Grid b=0.3 at ρ=0.6: tests whether grid-best remains near b=0.3 at higher contamination. If PPL ≈ contamination_60_seed42_r2 (adaptive, 17.74), confirms adaptive ≈ grid-best holds cross-ρ, strengthening Claim 2 generality.
294	
295	  [contamination_60_grid_b0_5_seed42]
296	    status: DONE
297	    metrics: {'eval_ppl': 17.704, 'eval_loss': 2.8738, 'eval_tokens': 4077068, 'eval_docs': 5000}
298	    conclusion: success
299	    hypothesis: ρ=0.6 grid-best (b=0.5) baseline: fixed b=0.5 on 60% contamination. Tests if grid-optimal b from ρ=0.4 transfers to higher contamination, or if adaptive b* adapts better.
300	
301	  [contamination_60_ess_only_seed42]
302	    status: DONE
303	    metrics: {'eval_ppl_holdout': 17.77, 'eval_loss_holdout': 2.8775, 'eval_holdout_tokens': 4077068, 'train_loss': 9.842, 'total_steps': 6103, 'train_runtime_seconds': 13152}
304	    conclusion: success
305	    hypothesis: ESS-only (max-intervention) on ρ=0.6 data: b* = max{b : ESS(b) ≥ n_min}. Tests if dual-constraint advantage over ESS-only holds at higher contamination (ρ=0.4→0.6). Paired with adaptive and grid_b0.5 for Claim 1+3 cross-validation.
306	
307	  [contamination_60_ess_only_seed123]
308	    status: DONE
309	    metrics: {'eval_ppl_holdout': 17.763, 'eval_loss_holdout': 2.8771, 'eval_holdout_tokens': 4077068, 'eval_method': 'eval_perplexity.py --checkpoints --max_docs 5000 --max_length 2048'}
310	    conclusion: success
311	    hypothesis: Cross-seed replication (seed123) of ESS-only at ρ=0.6. D075 found ESS-only(17.770) ≈ uniform(17.766) at ρ=0.6, suggesting max-intervention collapses at high contamination. 3-seed data tests if this collapse is robust or seed-specific, strengthening Claim 1 four-tier hierarchy cross-ρ evidence.
312	
313	  [contamination_60_ess_only_seed456]
314	    status: DONE
315	    metrics: {'eval_ppl_holdout': 17.762, 'eval_loss_holdout': 2.8771, 'eval_holdout_tokens': 4077068, 'eval_method': 'eval_perplexity.py --checkpoints --max_docs 5000 --max_length 2048'}
316	    conclusion: success
317	    hypothesis: Cross-seed replication (seed456) of ESS-only at ρ=0.6. D075 found ESS-only(17.770) ≈ uniform(17.766) at ρ=0.6, suggesting max-intervention collapses at high contamination. 3-seed data tests if this collapse is robust or seed-specific, strengthening Claim 1 four-tier hierarchy cross-ρ evidence.
318	
319	  [contamination_60_random_seed42]
320	    status: DONE
321	    metrics: {'eval_ppl_holdout': 17.832, 'eval_method': 'eval_perplexity.py --max_docs 5000 --max_length 2048 --stride 1024 --fp16', 'total_steps': 6103, 'note': 'resume from checkpoint-1000; cron falsely marked failed due to log path mismatch'}
322	    conclusion: success
323	    hypothesis: Random reweighting baseline at ρ=0.6: random weights ignore detector scores entirely. If PPL > ESS-only (17.77) and > uniform (17.766), completes four-tier ablation hierarchy (adaptive < uniform < ESS-only < random) at ρ=0.6, confirming Claim 1 structural argument holds cross-ρ.
324	
325	  [contamination_60_random_seed123]
326	    status: DONE
327	    metrics: {'eval_ppl_holdout': 17.87, 'eval_loss_holdout': 2.8832, 'eval_holdout_tokens': 4077068}
328	    conclusion: success
329	    hypothesis: Cross-seed replication (seed123) of random reweighting at ρ=0.6. Random weights ignore detector scores entirely. If PPL > ESS-only and > uniform (consistent with seed42), completes four-tier ablation hierarchy (adaptive < uniform < ESS-only < random) at ρ=0.6 with 3-seed evidence, confirming Claim 1
330	
331	  [contamination_60_random_seed456]
332	    status: DONE
333	    metrics: {'eval_ppl_holdout': 17.88, 'eval_loss_holdout': 2.8837, 'eval_holdout_tokens': 4077068}
334	    conclusion: success
335	    hypothesis: Cross-seed replication (seed456) of random reweighting at ρ=0.6. Random weights ignore detector scores entirely. If PPL > ESS-only and > uniform (consistent with seed42), completes four-tier ablation hierarchy (adaptive < uniform < ESS-only < random) at ρ=0.6 with 3-seed evidence, confirming Claim 1
336	
337	
338	============================================================
339	GROUP: tau_sweep
340	============================================================
341	  [tau_05_seed42]
342	    status: DONE
343	    metrics: {'train_loss': 8.849, 'total_steps': 6103, 'epoch': 0.26, 'train_runtime_s': 13431.4, 'train_samples_per_second': 7.27, 'eval_ppl_holdout': 17.688, 'eval_loss': 2.8729, 'eval_holdout_tokens': 4077068, 'eval_method': 'eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)', 'eval_note': 'unified post-hoc eval 2026-05-15', 'b_star_count': 24412, 'b_star_mean': 0.3923, 'b_star_median': 0.1707, 'b_star_std': 0.8821, 'b_star_min': 0, 'b_star_max': 20, 'b_star_p25': 0, 'b_star_p75': 0.4366, 'b_star_pct_zero': 29.1, 'b_star_pct_below_0.5': 78.4, 'b_star_pct_0.5_to_1': 12.9, 'b_star_pct_1_to_2': 5.7, 'b_star_pct_above_2': 2.9}
344	    conclusion: success
345	    hypothesis: τ sensitivity sweep: τ=0.5 (most permissive α_eff threshold), testing lower bound of useful τ range. Baseline τ=0.8 PPL=17.65.
346	
347	  [tau_06_seed42]
348	    status: DONE
349	    metrics: {'eval_ppl_holdout': 17.6805, 'eval_loss': 2.8725, 'train_loss': 9.275, 'total_steps': 6103, 'train_runtime_s': 13436.64, 'train_samples_per_second': 7.267, 'b_star_mean': 0.5899, 'b_star_median': 0.3746, 'b_star_std': 1.0693, 'b_star_min': 0, 'b_star_max': 20, 'b_star_p25': 0.1195, 'b_star_p75': 0.66, 'b_star_zero_frac': 0.156, 'b_star_nonzero_mean': 0.699, 'b_star_nonzero_median': 0.4473}
350	    conclusion: success
351	    hypothesis: τ sensitivity sweep: τ=0.6 (lower α_eff threshold) may allow more aggressive downweighting, testing if PPL improves or degrades vs τ=0.8 baseline (adaptive_fix PPL=17.65). Key evidence for Claim 3 (τ as robust empirical hyperparameter).
352	
353	  [tau_07_seed42]
354	    status: DONE
355	    metrics: {'train_loss': 9.6707, 'total_steps': 6103, 'train_runtime_s': 15065, 'train_samples_per_second': 6.482, 'eval_ppl_holdout': 17.6793, 'eval_loss': 2.8724, 'eval_holdout_tokens': 4077068, 'eval_method': 'eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)', 'eval_note': 'unified post-hoc eval 2026-05-15', 'b_star_count': 24412, 'b_star_mean': 0.8943, 'b_star_median': 0.58, 'b_star_std': 1.4007, 'b_star_min': 0, 'b_star_max': 20, 'b_star_p25': 0.3306, 'b_star_p75': 0.9712, 'b_star_pct_zero': 5.8, 'b_star_pct_below_0.5': 36, 'b_star_pct_0.5_to_1': 34.2, 'b_star_pct_1_to_2': 16.2, 'b_star_pct_above_2': 7.7}
356	    conclusion: success
357	    hypothesis: τ sensitivity sweep: τ=0.7 (slightly below baseline), testing if moderate τ reduction improves or degrades PPL. Baseline τ=0.8 PPL=17.65.
358	
359	  [tau_09_seed42]
360	    status: DONE
361	    metrics: {'eval_ppl_holdout': 17.712, 'eval_loss': 2.8742, 'eval_holdout_tokens': 4077068, 'eval_method': 'eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)', 'eval_note': 'unified post-hoc eval 2026-05-15', 'b_star_count': 24412, 'b_star_mean': 2.36, 'b_star_median': 1.32, 'b_star_std': 3.04, 'b_star_pct_above_2': 33.7}
362	    conclusion: negative
363	    hypothesis: τ sensitivity sweep: τ=0.9 (stricter α_eff threshold), testing if higher quality threshold improves PPL. Baseline τ=0.8 PPL=17.65.
364	
365	  [tau_095_seed42]
366	    status: DONE
367	    metrics: {'eval_ppl_holdout': 17.723, 'eval_loss': 2.8749, 'eval_holdout_tokens': 4077068, 'eval_method': 'eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)', 'train_loss': 10.198, 'total_steps': 6103, 'train_runtime_s': 13699, 'train_samples_per_second': 7.128, 'b_star_count': 24412, 'b_star_mean': 3.0775, 'b_star_median': 1.52, 'b_star_std': 3.9923, 'b_star_min': 0, 'b_star_max': 20, 'b_star_p25': 0.8, 'b_star_p75': 3.46, 'b_star_pct_zero': 0, 'b_star_pct_below_0.5': 8.5, 'b_star_pct_0.5_to_1': 24.7, 'b_star_pct_1_to_2': 26.4, 'b_star_pct_above_2': 40.3}
368	    conclusion: negative
369	    hypothesis: τ=0.95 forces α_eff > 0.95 before allowing downweighting, which should collapse b* toward near-max values (overfit to quality constraint) and degrade PPL toward ESS-only levels (~17.72), confirming the method requires τ ≤ 0.8 to balance quality and stability.
370	
371	  [tau_0.6_seed42]
372	    status: DONE
373	    metrics: None
374	    conclusion: killed
375	    hypothesis: τ sensitivity sweep: τ=0.6 (lower α_eff threshold) may allow more aggressive downweighting, testing if PPL improves or degrades vs τ=0.8 baseline (adaptive_fix PPL=17.65). Key evidence for Claim 3 (τ as robust empirical hyperparameter).
376	
377	
378	============================================================
379	GROUP: nmin_sweep
380	============================================================
381	  [nmin1_seed42]
382	    status: DONE
383	    metrics: {'eval_ppl_holdout': 17.789, 'eval_loss': 2.8786, 'eval_holdout_tokens': 4077068, 'b_star_mean': 7.197, 'b_star_median': 1.746, 'b_star_std': 8.374, 'b_star_min': 0, 'b_star_max': 20, 'b_star_p25': 0.803, 'b_star_p75': 20, 'b_star_zero_frac': 0.019, 'b_star_pct_below_0.5': 13.1, 'b_star_pct_0.5_to_1': 19.1, 'b_star_pct_1_to_2': 21.1, 'b_star_pct_above_2': 46.7, 'b_star_count': 24412, 'alpha_eff_mean': 0.714, 'alpha_eff_median': 0.8}
384	    conclusion: success
385	    hypothesis: n_min=1 sensitivity: minimal ESS constraint allows more aggressive downweighting, testing if adaptive method degrades with overly permissive ESS bound
386	
387	  [nmin4_seed42]
388	    status: DONE
389	    metrics: {'eval_ppl_holdout': 17.6947, 'eval_loss': 2.8733, 'eval_holdout_tokens': 4077068, 'eval_method': 'eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)', 'train_loss': 7.989, 'total_steps': 6103, 'train_runtime_s': 16231, 'train_samples_per_second': 6.016, 'b_star_count': 24412, 'b_star_mean': 0, 'b_star_median': 0, 'b_star_std': 0, 'b_star_min': 0, 'b_star_max': 0, 'b_star_pct_zero': 100, 'ess_mean': 4, 'ess_min': 4, 'ess_max': 4}
390	    conclusion: success
391	    hypothesis: n_min=4 (=batch_size) ablation: forces b*=0 always since ESS constraint cannot be satisfied with any b>0 when n_min=batch_size. Should degrade to uniform-equivalent PPL (~17.69). Key boundary condition for n_min sensitivity analysis.
392	
393	  [nmin5_seed42]
394	    status: DONE
395	    metrics: None
396	    conclusion: killed
397	
398	
399	============================================================
400	GROUP: bs8_other
401	============================================================
402	  [bs8_seed42]
403	    status: DONE
404	    metrics: None
405	    conclusion: failed
406	
407	  [bs8_auto_nmin_seed42]
408	    status: DONE
409	    metrics: None
410	    conclusion: failed
411	    hypothesis: bs=8 with auto n_min=4 (max(2,bs//2)). Previous bs8_nmin2 failed (PPL=17.73) because explicit n_min=2 was too loose for bs=8. Auto n_min=4 should recover performance.
412	
413	  [bs8_nmin2_seed42]
414	    status: DONE
415	    metrics: None
416	    conclusion: failed
417	
418	
419	============================================================
420	GROUP: bs16_batch
421	============================================================
422	  [batchsize16_nmin8_seed42]
423	    status: DONE
424	    metrics: None
425	    conclusion: failed
426	    hypothesis: batch_size=16 with auto n_min=8 (max(2,bs//2)): larger batch provides more stable ESS estimates and the coupling rule n_min=bs//2 maintains the same ESS dynamic range ratio as bs=4/n_min=2, so PPL should match or improve vs bs=4 baseline.
427	
428	  [batchsize16_nmin8_r2]
429	    status: DONE
430	    metrics: None
431	    conclusion: killed
432	
433	  [batchsize16_nmin8_r3]
434	    status: DONE
435	    metrics: {'eval_ppl_holdout': 17.65, 'eval_loss_holdout': 2.871, 'eval_holdout_tokens': 4077068, 'total_steps': 6103, 'train_loss': 2.6308, 'train_runtime_seconds': 15057, 'vs_adaptive_bs4': '-0.003 (17.65 vs 17.6527)', 'vs_bs8_nmin4': '-0.01 (17.65 vs 17.66)', 'batch_size': 16, 'n_min': 8}
436	    conclusion: success
437	    hypothesis: Coupling rule validation at bs=16: n_min=max(2,16//2)=8 with per_device_train_batch_size=16 (not 4×4 grad_accum). If PPL comparable to bs=4 adaptive, confirms coupling rule generalizes across batch sizes. Critical: micro-batch must exceed n_min for ESS constraint to be satisfiable.
438	
439	
440	============================================================
441	GROUP: rho04_batch
442	============================================================
443	  [batch_adaptive_tau_rho04_seed42]
444	    status: DONE
445	    metrics: {'eval_loss_holdout': 2.8725, 'eval_ppl_holdout': 17.681, 'train_loss': 9.8206, 'train_runtime_sec': 45402.86}
446	    conclusion: negative
447	    hypothesis: Batch-adaptive τ (τ_batch = clamp(α_eff_natural + 0.3, 0.5, τ)) reduces over-intervention on clean batches by lowering τ when the batch already has low contamination, yielding lower holdout PPL than fixed τ=0.8.
448	
449	
450	============================================================
451	GROUP: rho06_batch
452	============================================================
453	  [batch_adaptive_tau_rho06_seed42]
454	    status: DONE
455	    metrics: None
456	    conclusion: failed
457	    hypothesis: Batch-adaptive τ on ρ=0.6 data: per-batch τ_batch = clamp(α_eff_natural + 0.3, 0.5, 0.95) adapts threshold to local contamination density. At higher contamination, more batches have high α_eff_natural, so adaptive τ should outperform fixed τ=0.8 more clearly than at ρ=0.4.
458	
459	  [batch_adaptive_tau_rho06_r2]
460	    status: DONE
461	    metrics: None
462	    conclusion: failed
463	
464	  [batch_adaptive_tau_rho06_r3]
465	    status: DONE
466	    metrics: None
467	    conclusion: failed
468	    hypothesis: Batch-adaptive τ on ρ=0.6 data: per-batch τ_batch = clamp(α_eff_natural + 0.3, 0.5, 0.95) adapts threshold to local contamination density. At higher contamination, adaptive τ should outperform fixed τ=0.8 more clearly than at ρ=0.4 (which was negative).
469	
470	  [batch_adaptive_tau_rho06_r5]
471	    status: DONE
472	    metrics: {'eval_ppl_holdout': 17.73, 'eval_loss_holdout': 2.8754, 'eval_holdout_tokens': 4077068, 'train_loss': 9.267, 'train_runtime_seconds': 13903, 'total_steps': 6103, 'vs_uniform_rho06': '-0.036', 'vs_adaptive_fixed_tau08_rho06': '-0.010', 'vs_grid_best_rho06': '+0.026', 'vs_hybrid_rho06': '+0.200'}
473	    conclusion: negative
474	    hypothesis: Batch-adaptive τ on ρ=0.6 data: per-batch τ_batch = clamp(α_eff_natural + 0.3, 0.5, 0.95) adapts threshold to local contamination density. At higher contamination, adaptive τ should outperform fixed τ=0.8 more clearly than at ρ=0.4 (which was negative).
475	
476	  [eval_rho06_batch_v7]
477	    status: DONE
478	    metrics: {'contamination_60_ess_only_seed123': {'loss': 2.8771, 'perplexity': 17.76, 'tokens': 4077068}, 'contamination_60_ess_only_seed456': {'loss': 2.8771, 'perplexity': 17.76, 'tokens': 4077068}, 'contamination_60_random_seed123': {'loss': 2.8832, 'perplexity': 17.87, 'tokens': 4077068}, 'contamination_60_random_seed456': {'loss': 2.8837, 'perplexity': 17.88, 'tokens': 4077068}, 'eval_data': 'data/human/eval_holdout.jsonl', 'max_docs': 5000, 'max_length': 2048}
479	    conclusion: success
480	    hypothesis: Contamination-aware weighting (rho=0.6) with ESS-only vs random selection should show different perplexity on held-out human text, with ESS-only selection better capturing human-like text distribution.
481	
482	
483	============================================================
484	GROUP: hybrid
485	============================================================
486	  [hybrid_rho04_seed42]
487	    status: DONE
488	    metrics: {'eval_loss_holdout': 2.863, 'eval_ppl_holdout': 17.514}
489	    conclusion: success
490	    hypothesis: Hybrid filter+reweight (remove q>0.95 then adaptive reweight remainder with rho=0.4) will achieve lower holdout PPL than pure adaptive reweighting by eliminating the most contaminated samples before soft reweighting, combining the strengths of detect_remove and adaptive methods.
491	
492	  [hybrid_rho06_seed42]
493	    status: DONE
494	    metrics: {'eval_loss_holdout': 2.8637, 'eval_ppl_holdout': 17.526, 'eval_ppl_openwebtext': 18.208, 'eval_ppl_wikipedia': 15.267, 'downstream_arc_easy_acc_norm': 0.6208, 'downstream_arc_challenge_acc_norm': 0.3524, 'downstream_hellaswag_acc_norm': 0.4801, 'downstream_piqa_acc_norm': 0.6931, 'downstream_winogrande_acc': 0.5785, 'eval_source': 'rho06_tau07_seed42 eval worker - evaluated hybrid checkpoint by mistake'}
495	    conclusion: success
496	    hypothesis: Hybrid filter+reweight on ρ=0.6: remove q>0.95 samples (extreme outliers) then apply adaptive reweighting to remainder. At higher contamination, extreme outliers distort ESS more severely, so pre-filtering should yield larger relative improvement over pure-adaptive than at ρ=0.4.
497	
498	
499	============================================================
500	GROUP: baseline_qwen
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02d8c80f-1d6c-4cfb-9ff7-a1bc5da68b10",
  "isSidechain": true,
  "promptId": "792d4fc7-1d48-4678-830d-80fd5a58c95b",
  "agentId": "ab3fc5e12c4a8ae93",
  "type": "user",
  "uuid": "88361089-a205-49c0-b7ea-36bec1a85430",
  "sourceToolAssistantUUID": "02d8c80f-1d6c-4cfb-9ff7-a1bc5da68b10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-24T04:31:41.966Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Rxgg6xyUPFdB8j7Ey72YoR`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c/tool-results/bw00gfn2k.txt",
  "limit": 400,
  "offset": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88361089-a205-49c0-b7ea-36bec1a85430",
  "isSidechain": true,
  "agentId": "ab3fc5e12c4a8ae93",
  "requestId": "req_011CbLmS6PaWRyiRaUf1grZ9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f040e81e-0dd7-41bf-b8fa-186edc5b28c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0193xgVnKbC8W4Yvmx5foeWu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16334,
      "cache_read_input_tokens": 56272,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16334
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 56272,
          "cache_creation_input_tokens": 16334,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16334,
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

_source line 26 · 2026-05-24T04:31:41.972Z_

<details><summary>↩ Tool result · `toolu_01Rxgg6xyUPFdB8j7Ey72YoR`</summary>

```text
500	GROUP: baseline_qwen
501	============================================================
502	  [baseline_qwen3_0.6b]
503	    status: DONE
504	    metrics: {'eval_ppl_holdout': 22.97, 'eval_loss': 3.134, 'eval_holdout_tokens': 4077068, 'eval_method': 'sliding_window_stride1024_maxlen2048_fp16'}
505	    conclusion: success
506	    hypothesis: Raw Qwen3-0.6B pretrained checkpoint baseline PPL (no continued pretraining). Reference point for quantifying absolute improvement from training.
507	
508	  [qwen06b_uniform_seed42]
509	    status: DONE
510	    metrics: {'eval_ppl_holdout': 17.69, 'eval_loss_holdout': 2.8733, 'eval_holdout_tokens': 4077068, 'train_loss': 1.9882, 'note': 'v2 run on westd-41312 (no inline eval)', 'downstream_arc_easy_acc_norm': 0.6128, 'downstream_arc_challenge_acc_norm': 0.3481, 'downstream_hellaswag_acc_norm': 0.4836, 'downstream_piqa_acc_norm': 0.6877, 'downstream_winogrande_acc': 0.5856, 'downstream_eval_method': 'lm_eval 0.4.11, 0-shot, float16, batch_size=auto', 'eval_ppl_openwebtext': 18.365, 'eval_ppl_wikipedia': 15.335}
511	    conclusion: success
512	    hypothesis: Uniform baseline retrain (seed42) without inline eval overhead — provides clean PPL baseline for Claim 1/2 comparison and enables lm-eval downstream evaluation on same checkpoint
513	
514	
515	============================================================
516	GROUP: fromscratch
517	============================================================
518	  [adaptive_fromscratch_seed42]
519	    status: DONE
520	    metrics: {'train_loss': 9.976, 'eval_ppl_holdout': 17.689, 'eval_ppl_openwebtext': 18.37, 'eval_ppl_wikipedia': 15.349, 'downstream_arc_easy_acc_norm': 0.6178, 'downstream_arc_challenge_acc_norm': 0.3524, 'downstream_hellaswag_acc_norm': 0.4806, 'downstream_piqa_acc_norm': 0.6844, 'downstream_winogrande_acc': 0.5801, 'downstream_eval_method': 'lm_eval 0.4.11, 0-shot, float16, batch_size=auto', 'eval_method': 'eval_ppl_ood.py (sliding window, stride=1024, max_docs=5000, fp16)', 'training_time_s': 13660}
521	    conclusion: success
522	    hypothesis: From-scratch adaptive (no resume artifact) at seed42 to complete 3-seed consistent dataset. If in-dist PPL matches seed123/456 range (~17.677-17.683) and OOD shows no reversal, distribution matching was a resume artifact.
523	
524	
525	============================================================
526	GROUP: tau08_scratch
527	============================================================
528	  [adaptive_tau08_scratch_seed42]
529	    status: DONE
530	    metrics: None
531	    conclusion: failed
532	    hypothesis: From-scratch adaptive (τ=0.8, ρ=0.4, n_min=2, seed=42, Qwen3-0.6B). Replaces resume-checkpoint adaptive_fix_seed42 to complete 3-seed from-scratch set with adaptive_ood_seed123/456. Enables symmetric 3-seed OOD comparison: τ=0.7 3-seed vs τ=0.8 3-seed.
533	
534	  [adaptive_tau08_scratch_seed42_v2]
535	    status: DONE
536	    metrics: None
537	    conclusion: failed
538	    hypothesis: From-scratch adaptive (τ=0.8, ρ=0.4, n_min=2, seed=42, Qwen3-0.6B). V2: rerun without --save_only_model to preserve optimizer state. Replaces corrupted adaptive_tau08_scratch_seed42 (resume caused optimizer loss). Completes 3-seed from-scratch set for τ=0.8 OOD comparison.
539	
540	  [adaptive_tau08_scratch_seed42_v3]
541	    status: DONE
542	    metrics: {'holdout_ppl': 17.6885, 'holdout_loss': 2.87291, 'ood_owt_ppl': 18.37026, 'ood_owt_loss': 2.91073, 'ood_wiki_ppl': 15.34964, 'ood_wiki_loss': 2.73109, 'ood_eval_source': 'eval_results/ pipeline'}
543	    conclusion: success
544	    hypothesis: From-scratch adaptive (τ=0.8, ρ=0.4, n_min=2, seed=42, Qwen3-0.6B). V3: resume from v2 checkpoint-500 (has optimizer state). No --save_only_model, no inline eval.
545	
546	
547	============================================================
548	GROUP: ood
549	============================================================
550	  [adaptive_ood_seed123]
551	    status: DONE
552	    metrics: {'eval_ppl_holdout': 17.677, 'eval_ppl_openwebtext': 18.373, 'eval_ppl_wikipedia': 15.37, 'downstream_arc_easy_acc_norm': 0.6301, 'downstream_arc_challenge_acc_norm': 0.3481, 'downstream_hellaswag_acc_norm': 0.4791, 'downstream_piqa_acc_norm': 0.6844, 'downstream_winogrande_acc': 0.5706, 'downstream_eval_method': 'lm_eval 0.4.11, 0-shot, float16, batch_size=auto'}
553	    conclusion: success
554	    hypothesis: Retrain adaptive (τ=0.8, n_min=2, seed=123) with checkpoint saving for OOD eval. If in-dist PPL matches original 17.643 (±0.01), the checkpoint is valid for OOD generalization testing across OpenWebText/Wikipedia/FineWeb.
555	
556	  [adaptive_ood_seed456]
557	    status: DONE
558	    metrics: {'eval_ppl_holdout': 17.683, 'eval_ppl_openwebtext': 18.366, 'eval_ppl_wikipedia': 15.345, 'downstream_arc_easy_acc_norm': 0.6077, 'downstream_arc_challenge_acc_norm': 0.3541, 'downstream_hellaswag_acc_norm': 0.48, 'downstream_piqa_acc_norm': 0.6806, 'downstream_winogrande_acc': 0.5714, 'downstream_eval_method': 'lm_eval 0.4.11, 0-shot, float16, batch_size=auto'}
559	    conclusion: success
560	    hypothesis: Retrain adaptive (τ=0.8, n_min=2, seed=456) with checkpoint saving for OOD eval. If in-dist PPL matches original 17.657 (±0.01), the checkpoint is valid for OOD generalization testing across OpenWebText/Wikipedia/FineWeb.
561	
562	  [uniform_ood_seed123]
563	    status: DONE
564	    metrics: {'eval_ppl_holdout': 17.6861, 'eval_ppl_openwebtext': 18.3678, 'eval_ppl_wikipedia': 15.3768, 'downstream_arc_easy_acc_norm': 0.6229, 'downstream_arc_challenge_acc_norm': 0.3507, 'downstream_hellaswag_acc_norm': 0.4797, 'downstream_piqa_acc_norm': 0.685, 'downstream_winogrande_acc': 0.5762, 'downstream_eval_method': 'lm_eval 0.4.11, 0-shot, float16, batch_size=auto'}
565	    conclusion: success
566	    hypothesis: Retrain uniform (b=0, seed=123) with checkpoint saving for OOD eval. If in-dist PPL matches original 17.686 (±0.01), the checkpoint is valid for OOD generalization testing across OpenWebText/Wikipedia/FineWeb.
567	
568	  [uniform_ood_seed456]
569	    status: DONE
570	    metrics: {'eval_ppl_holdout': 17.7015, 'eval_ppl_openwebtext': 18.3865, 'eval_ppl_wikipedia': 15.3594, 'downstream_arc_easy_acc_norm': 0.6166, 'downstream_arc_challenge_acc_norm': 0.3439, 'downstream_hellaswag_acc_norm': 0.4826, 'downstream_piqa_acc_norm': 0.6795, 'downstream_winogrande_acc': 0.5667, 'downstream_eval_method': 'lm_eval 0.4.11, 0-shot, float16, batch_size=auto'}
571	    conclusion: success
572	    hypothesis: Retrain uniform (b=0, seed=456) with checkpoint saving for OOD eval. If in-dist PPL matches original 17.702 (±0.01), the checkpoint is valid for OOD generalization testing across OpenWebText/Wikipedia/FineWeb.
573	
574	
575	============================================================
576	GROUP: epoch_matched_dr_indep
577	============================================================
578	  [dr_epoch_matched_indep_lr_seed42]
579	    status: DONE
580	    metrics: {'holdout_ppl': 18.78174, 'holdout_loss': 2.93288, 'ood_owt_ppl': 19.23533, 'ood_owt_loss': 2.95675, 'ood_wiki_ppl': 15.95958, 'ood_wiki_loss': 2.77006, 'train_loss_final': 5.833, 'total_steps': 2533}
581	    conclusion: failed
582	    hypothesis: D&R epoch-matched with independent linear LR schedule (total_steps=2533). Eliminates LR schedule confound: previous epoch-matched used 6103-step schedule but stopped at 2533. Paired with uniform_epoch_matched to quantify LR confound magnitude.
583	
584	  [dr_epoch_matched_indep_lr_v2_seed42]
585	    status: DONE
586	    metrics: {'holdout_ppl': 17.65053, 'holdout_loss': 2.87077, 'ood_owt_ppl': 18.26112, 'ood_owt_loss': 2.90477, 'ood_wiki_ppl': 15.19382, 'ood_wiki_loss': 2.72089, 'train_loss_final': 11.11, 'total_steps': 2533}
587	    conclusion: success
588	    hypothesis: D&R epoch-matched with CORRECT filtered data (q≤0.5, 153725 samples, 86.4% real) and independent linear LR schedule (total_steps=2533). Rerun of invalidated dr_epoch_matched_indep_lr_seed42 which used inverted filter (q>0.5, 85% synthetic). Paired with uniform_epoch_matched_indep_lr_seed42 to quanti
589	
590	  [uniform_epoch_matched_indep_lr_seed42]
591	    status: DONE
592	    metrics: {'holdout_ppl': 18.06206, 'holdout_loss': 2.89381, 'ood_owt_ppl': 18.64966, 'ood_wiki_ppl': 15.511, 'train_loss_final': 8.058, 'total_steps': 2533}
593	    conclusion: success
594	    hypothesis: Uniform weighting with epoch-matched training tokens (max_steps=2533) and independent linear LR schedule (5e-5, full decay over 2533 steps) serves as the controlled baseline for LR confound elimination. Paired with dr_epoch_matched_indep_lr_seed42 (PPL=18.78) to quantify pure epoch-matching effect w
595	
596	  [uniform_epoch_matched_seed456]
597	    status: DONE
598	    metrics: {'holdout_ppl': 18.068, 'holdout_loss': 2.8941, 'owt_ppl': 18.66, 'owt_loss': 2.9264, 'wiki_ppl': 15.515, 'wiki_loss': 2.7418, 'train_loss': 8.039, 'total_steps': 2533}
599	    conclusion: success
600	    hypothesis: Uniform epoch-matched seed456: trains on full data (scored_data.jsonl, 371499 samples) for 2533 steps with independent linear LR schedule (5e-5→0), effective batch=16 (bs=4 × grad_accum=4). Third seed for uniform epoch-matched baseline. Paired with uniform_epoch_matched_indep_lr_seed42 (holdout=18.0
601	
602	
603	============================================================
604	GROUP: downstream_eval
605	============================================================
606	  [tau07_downstream_eval]
607	    status: DONE
608	    metrics: None
609	    conclusion: failed
610	    hypothesis: Downstream eval for τ=0.7 (3 seeds). Paper switched main results to τ=0.7; must confirm downstream benchmarks match or exceed τ=0.8 and uniform. Reviewer will ask for downstream under recommended setting.
611	
612	  [uniform_seed42_downstream]
613	    status: DONE
614	    metrics: {'downstream_arc_easy_acc_norm': 0.6128, 'downstream_arc_challenge_acc_norm': 0.3481, 'downstream_hellaswag_acc_norm': 0.4836, 'downstream_piqa_acc_norm': 0.6877, 'downstream_winogrande_acc': 0.5856, 'downstream_eval_method': 'lm_eval 0.4.11, 0-shot, float16, batch_size=auto'}
615	    conclusion: success
616	    hypothesis: Downstream benchmark eval (ARC-Easy/Challenge, HellaSwag, PIQA, WinoGrande) for uniform_seed42 baseline. Completes 3-seed uniform downstream comparison needed for Table in paper.
617	
618	  [detect_remove_q03_seed42_r2]
619	    status: DONE
620	    metrics: {'eval_ppl_holdout': 17.25, 'eval_loss_holdout': 2.848, 'downstream_arc_easy_acc_norm': 0.6301, 'downstream_arc_challenge_acc_norm': 0.3549, 'downstream_hellaswag_acc_norm': 0.4851, 'downstream_piqa_acc_norm': 0.6872, 'downstream_winogrande_acc': 0.5675, 'downstream_eval_method': 'lm_eval 0.4.11, 0-shot, float16, batch_size=auto', 'eval_ppl_openwebtext': 18.004, 'eval_ppl_wikipedia': 15.037}
621	    conclusion: success
622	    hypothesis: D&R threshold t=0.3: keep q≤0.3 (116,935 samples, 31.5%). Second most aggressive filtering level. Part of 9-point D&R sensitivity curve (q01-q09). Previous attempt failed (python: command not found). Rerun on westd-30476.
623	
624	
625	============================================================
626	GROUP: grid_high_b
627	============================================================
628	  [grid_b1_0_seed123]
629	    status: DONE
630	    metrics: {'eval_ppl_holdout': 17.674, 'eval_loss': 2.8721, 'eval_holdout_tokens': 4077068, 'train_loss': 10.218, 'total_steps': 6103, 'train_runtime_s': 13878, 'gpu_hours': 3.88}
631	    conclusion: success
632	    hypothesis: Grid-b sweep b=1.0 seed=123: moderate exponential downweighting. Multi-seed data point establishing that b>0.5 yields diminishing returns, supporting the grid-b PPL curve monotonically increasing past optimal.
633	
634	  [grid_b1_0_seed456]
635	    status: DONE
636	    metrics: {'train_loss': 10.178, 'total_steps': 6103, 'train_runtime_s': 12963.87, 'gpu_hours': 3.67, 'train_samples_per_second': 7.532, 'eval_loss': 2.8725, 'eval_ppl_holdout': 17.68, 'eval_holdout_tokens': 4077068, 'eval_loss_holdout': 2.8734, 'eval_tokens': 5004058}
637	    conclusion: success
638	    hypothesis: Grid-b weighting with b=1.0, seed=456, for multi-seed validation of best-b baseline
639	
640	  [grid_b1_5_seed123]
641	    status: DONE
642	    metrics: {'train_loss': 10.4776, 'total_steps': 6103, 'train_runtime_s': 15053.1, 'gpu_hours': 4.18, 'eval_ppl_holdout': 17.701, 'eval_loss': 2.8736}
643	    conclusion: success
644	    hypothesis: Grid-b sweep b=1.5 seed=123: testing diminishing returns region. PPL should be higher than b=1.0 as stronger downweighting begins to over-suppress useful synthetic samples, confirming U-shaped PPL-vs-b curve.
645	
646	  [grid_b1_5_seed456]
647	    status: DONE
648	    metrics: {'train_loss': 10.435, 'total_steps': 6103, 'train_runtime_s': 12950.16, 'gpu_hours': 3.67, 'train_samples_per_second': 7.54, 'eval_loss': 2.8741, 'eval_ppl_holdout': 17.71, 'eval_holdout_tokens': 4077068, 'eval_loss_holdout': 2.875, 'eval_tokens': 5004058}
649	    conclusion: success
650	    hypothesis: Grid-b weighting with b=1.5, seed=456, for multi-seed validation of best-b baseline
651	
652	  [grid_b2_0_seed123]
653	    status: DONE
654	    metrics: {'train_loss': 10.61, 'total_steps': 6103, 'train_runtime_s': 13058.8, 'gpu_hours': 3.63, 'train_samples_per_second': 7.478, 'train_steps_per_second': 0.467, 'eval_ppl_holdout': 17.725, 'eval_loss': 2.875, 'eval_holdout_tokens': 4077068}
655	    conclusion: success
656	    hypothesis: Grid-b sweep b=2.0 seed=123: strong downweighting regime past optimal. PPL should degrade further, establishing that aggressive fixed-b over-suppresses synthetic data and motivates adaptive per-batch b* selection.
657	
658	  [grid_b2_0_seed456]
659	    status: DONE
660	    metrics: {'eval_ppl_holdout': 17.989, 'eval_loss': 2.8898, 'eval_holdout_tokens': 4077068, 'train_loss': 10.625, 'total_steps': 6103, 'train_runtime_s': 12969, 'gpu_hours': 3.6, 'train_samples_per_second': 7.53, 'eval_method': 'eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)'}
661	    conclusion: success
662	    hypothesis: Grid-b weighting with b=2.0, seed=456, for multi-seed validation of best-b baseline
663	
664	  [grid_b3_0_seed123]
665	    status: DONE
666	    metrics: {'train_loss': 10.7422, 'total_steps': 6103, 'train_runtime_s': 12955.83, 'gpu_hours': 3.6, 'eval_ppl_holdout': 17.76, 'eval_loss': 2.877, 'eval_holdout_tokens': 4077068}
667	    conclusion: success
668	    hypothesis: Grid-b sweep b=3.0 seed=123: very aggressive downweighting well past optimal. Multi-seed confirmation that high-b regime consistently degrades PPL, strengthening the case that grid search sensitivity motivates adaptive b*.
669	
670	  [grid_b3_0_seed456]
671	    status: DONE
672	    metrics: {'eval_ppl_holdout': 17.921, 'eval_loss': 2.886, 'eval_holdout_tokens': 4077068, 'train_loss': 5.435, 'total_steps': 6103, 'train_runtime_s': 6602, 'gpu_hours': 1.83, 'eval_method': 'eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)'}
673	    conclusion: success
674	    hypothesis: Grid-b weighting with b=3.0, seed=456, for multi-seed validation of best-b baseline
675	
676	  [grid_b5_0_seed123]
677	    status: DONE
678	    metrics: {'train_loss': 10.8468, 'total_steps': 6103, 'train_runtime_s': 14434, 'gpu_hours': 4.01, 'eval_ppl_holdout': 17.8039, 'eval_loss': 2.8794, 'eval_holdout_tokens': 4077068}
679	    conclusion: success
680	    hypothesis: Grid-b sweep b=5.0 seed=123: extreme downweighting (near-zero weight for synthetic). Establishes ceiling of degradation from over-aggressive fixed reweighting, proving that wrong b choice can be worse than no reweighting at all.
681	
682	  [grid_b5_0_seed456]
683	    status: DONE
684	    metrics: {'eval_ppl_holdout': 17.993, 'eval_loss': 2.89, 'eval_holdout_tokens': 4077068, 'train_loss': 5.488, 'total_steps': 6103, 'train_runtime_s': 6601, 'gpu_hours': 1.83, 'eval_method': 'eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)'}
685	    conclusion: success
686	    hypothesis: Grid-b weighting with b=5.0, seed=456, for multi-seed validation of best-b baseline
687	
688	
689	============================================================
690	GROUP: golden_ratio
691	============================================================
692	  [golden_ratio_seed42]
693	    status: DONE
694	    metrics: {'eval_ppl_holdout': 17.654, 'eval_loss': 2.871, 'train_loss': 2.1145, 'train_loss_last500': 2.109, 'eval_holdout_tokens': 4077068, 'total_steps': 6103, 'train_runtime_s': 13442, 'gpu_hours': 3.73}
695	    conclusion: success
696	    hypothesis: Golden Ratio oracle baseline: w=1/φ≈0.618 for synthetic (q>0.5), w=1.0 for real — requires known proportion, serves as oracle upper bound for adaptive method
697	
698	
699	============================================================
700	GROUP: w2_dist
701	============================================================
702	  [w2_distribution_matching_eval]
703	    status: DONE
704	    metrics: None
705	    conclusion: negative
706	    hypothesis: If adaptive weighting's FineWeb PPL improvement is genuine quality gain (not tautological distribution matching), then adaptive should also show lower PPL on non-FineWeb eval sets (C4/OpenWebText, Wikipedia). If the improvement is purely distribution matching, adaptive will only win on FineWeb-deriv
707	
708	
709	============================================================
710	GROUP: threshold_sweep
711	============================================================
712	  [threshold_q03_seed42]
713	    status: DONE
714	    metrics: {'eval_loss_holdout': 2.848, 'eval_ppl_holdout': 17.253}
715	    conclusion: success
716	    hypothesis: Hard-filter threshold sensitivity: remove q>0.3 samples, train uniformly on remaining. Paired with detect_remove (q>0.5) and threshold_q07 (q>0.7) to test if filtering requires precise threshold calibration while adaptive does not.
717	
718	  [threshold_q07_seed42]
719	    status: DONE
720	    metrics: None
721	    conclusion: failed
722	    hypothesis: Hard-filter threshold sensitivity: remove q>0.7 samples (least aggressive, keeps most data+contamination), train uniformly. If PPL varies >0.1 across q=0.3/0.5/0.7 thresholds, proves filtering needs precise calibration while adaptive is threshold-free.
723	
724	
725	============================================================
726	GROUP: diagnostic
727	============================================================
728	  [diagnostic_contamination100]
729	    status: DONE
730	    metrics: None
731	    conclusion: killed
732	    hypothesis: Diagnostic: does 100% synthetic contamination significantly degrade held-out PPL vs 40%? If PPL ≈ 17.7, contamination sensitivity is too low for this scale.
733	
734	
735	============================================================
736	GROUP: tau_nmin
737	============================================================
738	  [tau_05_nmin2_seed42]
739	    status: DONE
740	    metrics: None
741	    conclusion: killed
742	    hypothesis: τ=0.5 rerun with correct n_min=2 (original tau_05_seed42 used n_min=3 confound). Most permissive α_eff threshold, expect b*≈0 for many batches.
743	
744	  [tau_06_nmin2_seed42]
745	    status: DONE
746	    metrics: None
747	    conclusion: killed
748	    hypothesis: τ=0.6 rerun with correct n_min=2 (original tau_06_seed42 used n_min=3 confound). Tests lower τ region with proper ESS constraint.
749	
750	  [tau_07_nmin2_seed42]
751	    status: DONE
752	    metrics: None
753	    conclusion: killed
754	    hypothesis: τ=0.7 rerun with correct n_min=2 (original tau_07_seed42 used n_min=3 confound). Slightly below optimal τ=0.8.
755	
756	  [tau_09_nmin2_seed42]
757	    status: DONE
758	    metrics: None
759	    conclusion: killed
760	    hypothesis: τ=0.9 rerun with correct n_min=2 (original tau_09_seed42 used n_min=3 confound). Tests if τ>0.8 still degrades with corrected n_min.
761	
762	  [tau_095_nmin2_seed42]
763	    status: DONE
764	    metrics: None
765	    conclusion: killed
766	    hypothesis: τ=0.95 rerun with correct n_min=2 (original tau_095_seed42 used n_min=3 confound). Most strict α_eff threshold, may over-constrain b*.
767	
768	
769	============================================================
770	GROUP: bs8_nmin2
771	============================================================
772	  [bs8_nmin2_seed42_r2]
773	    status: DONE
774	    metrics: {'eval_ppl_holdout': 17.73, 'eval_loss_holdout': 2.8752, 'eval_holdout_tokens': 4077068, 'eval_method': 'eval_perplexity.py on data/human/eval_holdout.jsonl, max_docs=5000, stride=1024, fp16', 'train_loss': 5.4065, 'train_steps': 6103, 'train_runtime_seconds': 14621.6}
775	    conclusion: negative
776	    hypothesis: batch_size=8 with n_min=2 (correct coupling: n_min=max(2,bs//2)=4→override to 2 for wider ESS dynamic range [2,8]). Resubmit after zombie cleanup on cuda:2. Parent: bs8_nmin2_seed42 (OOM due to zombie).
777	
778	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f040e81e-0dd7-41bf-b8fa-186edc5b28c6",
  "isSidechain": true,
  "promptId": "792d4fc7-1d48-4678-830d-80fd5a58c95b",
  "agentId": "ab3fc5e12c4a8ae93",
  "type": "user",
  "uuid": "be9dbb82-87cb-4a70-8ad3-ffeeecf22ce7",
  "sourceToolAssistantUUID": "f040e81e-0dd7-41bf-b8fa-186edc5b28c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-24T04:31:44.883Z_

Now I have all the data. Let me compute the key statistics needed to verify the specific numbers:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be9dbb82-87cb-4a70-8ad3-ffeeecf22ce7",
  "isSidechain": true,
  "agentId": "ab3fc5e12c4a8ae93",
  "requestId": "req_011CbLmSnSN48vF2JGhAkegy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "492ccb77-7c29-4caa-9e3e-914c7b54b5e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DadVLXFSTqkt4r35RG8axk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7768,
      "cache_read_input_tokens": 72606,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7768,
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

_source line 28 · 2026-05-24T04:32:37.430Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01HVpjPsuCcDFPTdvAH1SHgF`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport numpy as np\nimport json\n\nFILE = \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c/tool-results/mcp-agent-ml-research-read_registry-1779596944442.txt\"\n\nwith open(FILE) as f:\n    outer = json.load(f)\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\ndef sem(vals):\n    a = np.array(vals)\n    return a.std(ddof=1) / np.sqrt(len(a))\n\ndef stats(vals, label):\n    a = np.array(vals)\n    print(f\"  {label}: mean={a.mean():.4f}, std={a.std(ddof=1):.4f}, SEM={sem(vals):.4f}, n={len(vals)}\")\n    return a.mean(), sem(vals)\n\nprint(\"=\" * 70)\nprint(\"1. B=4, rho=0.4 MAIN RESULTS (tau=0.7 3-seed, from tau07_seed*)\")\nprint(\"=\" * 70)\n# The main results use tau=0.7 triple seeds\n# adaptive seeds: tau07_seed42=17.68, tau07_seed123=17.666, tau07_seed456=17.677\nadap_b4 = [17.68, 17.666, 17.677]\n# uniform: uniform_seed42=17.6939, uniform_seed123=17.6861, uniform_seed456=17.7015\nunif_b4 = [17.6939, 17.6861, 17.7015]\nstats(adap_b4, \"Adaptive B=4 tau=0.7\")\nstats(unif_b4, \"Uniform B=4\")\ndeltas_b4 = np.array(adap_b4) - np.array(unif_b4)\nprint(f\"  Deltas: {deltas_b4}\")\nprint(f\"  Mean delta: {deltas_b4.mean():.4f}, SEM delta: {sem(deltas_b4):.4f}\")\n\n# Also check the tau=0.8 3-seed (adaptive_seed42/123/456 from original)\nprint(\"\\n--- Also: adaptive tau=0.8 3-seed ---\")\nadap_b4_tau08 = [17.644, 17.6308, 17.6419]\nstats(adap_b4_tau08, \"Adaptive B=4 tau=0.8\")\n\nprint(\"\\n=\" * 70)\nprint(\"2. B=8, rho=0.4 RESULTS\")\nprint(\"=\" * 70)\n# seed42: adaptive=17.650425, uniform=17.694186\n# seed123_r2: adaptive=17.631, uniform=17.687\n# seed456_r2: adaptive=17.646, uniform=17.702\nadap_b8 = [17.650425, 17.631, 17.646]\nunif_b8 = [17.694186, 17.687, 17.702]\nstats(adap_b8, \"Adaptive B=8\")\nstats(unif_b8, \"Uniform B=8\")\ndeltas_b8 = np.array(adap_b8) - np.array(unif_b8)\nprint(f\"  Deltas: {deltas_b8}\")\nprint(f\"  Mean delta: {deltas_b8.mean():.4f}, SEM delta: {sem(deltas_b8):.4f}\")\n\nprint(\"\\n=\" * 70)\nprint(\"3. B=16 RESULTS\")\nprint(\"=\" * 70)\n# seed42: adaptive=17.631, uniform=17.694\n# seed123_r2: adaptive=17.616, uniform=17.686\n# seed456: adaptive=17.645, uniform=17.717\nadap_b16 = [17.631, 17.616, 17.645]\nunif_b16 = [17.694, 17.686, 17.717]\nstats(adap_b16, \"Adaptive B=16\")\nstats(unif_b16, \"Uniform B=16\")\ndeltas_b16 = np.array(adap_b16) - np.array(unif_b16)\nprint(f\"  Deltas: {deltas_b16}\")\nprint(f\"  Mean delta: {deltas_b16.mean():.4f}, SEM delta: {sem(deltas_b16):.4f}\")\n\nprint(\"\\n=\" * 70)\nprint(\"4. rho=0.6 RESULTS (tau=0.7, from adaptive_rho06_tau07_seed*)\")\nprint(\"=\" * 70)\n# adaptive_rho06_tau07: seed42=17.735, seed123=17.727, seed456=17.732\n# uniform rho=0.6: seed42=17.766, seed123=17.754, seed456=17.77\nadap_rho06 = [17.735, 17.727, 17.732]\nunif_rho06 = [17.766, 17.754, 17.770]\nstats(adap_rho06, \"Adaptive rho=0.6 tau=0.7\")\nstats(unif_rho06, \"Uniform rho=0.6\")\ndeltas_rho06 = np.array(adap_rho06) - np.array(unif_rho06)\nprint(f\"  Deltas: {deltas_rho06}\")\nprint(f\"  Mean delta: {deltas_rho06.mean():.4f}, SEM delta: {sem(deltas_rho06):.4f}\")\n\nprint(\"\\n\" + \"=\" * 70)\nprint(\"5. rho=0.3 RESULTS\")\nprint(\"=\" * 70)\n# adaptive: seed42=17.422, seed123=17.435, seed456_r2=17.424\n# uniform: seed42=17.422, seed123=17.433, seed456=17.419\nadap_rho03 = [17.422, 17.435, 17.424]\nunif_rho03 = [17.422, 17.433, 17.419]\nstats(adap_rho03, \"Adaptive rho=0.3\")\nstats(unif_rho03, \"Uniform rho=0.3\")\ndeltas_rho03 = np.array(adap_rho03) - np.array(unif_rho03)\nprint(f\"  Deltas: {deltas_rho03}\")\nprint(f\"  Mean delta: {deltas_rho03.mean():.4f}, SEM delta: {sem(deltas_rho03):.4f}\")\n\nprint(\"\\n\" + \"=\" * 70)\nprint(\"6. rho=0.2 RESULTS\")\nprint(\"=\" * 70)\n# adaptive: tau08=17.382 (vs uniform 17.336), tau09_r5=17.45\n# uniform: 17.336\nprint(f\"  Adaptive tau=0.8 PPL=17.382, Uniform=17.336, delta=+{17.382-17.336:.3f}\")\nprint(f\"  Adaptive tau=0.9 (r5) PPL=17.45, Uniform=17.336, delta=+{17.45-17.336:.3f}\")\n\nprint(\"\\n\" + \"=\" * 70)\nprint(\"7. Alpha-eff only (nmin=1)\")\nprint(\"=\" * 70)\n# seed42=17.75, seed123=17.733, seed456=17.744\naeff_only = [17.75, 17.733, 17.744]\nstats(aeff_only, \"Alpha-eff only (nmin=1)\")\n\nprint(\"\\n\" + \"=\" * 70)\nprint(\"8. ESS-only RESULTS\")\nprint(\"=\" * 70)\n# seed42=17.73, seed123=17.721 (r2), seed456=17.762 (r2)\ness_only = [17.73, 17.721, 17.762]\nstats(ess_only, \"ESS-only\")\n# Also: seed123=17.72 (original), seed456=17.76 (original)\nprint(\"  (seed123 original=17.72, seed456 original=17.76)\")\n\nprint(\"\\n\" + \"=\" * 70)\nprint(\"9. 1.7B SCALE RESULTS\")\nprint(\"=\" * 70)\n# adaptive: v5(seed42)=13.27, seed123=13.25, seed456=13.2668\n# uniform: v5(seed42)=13.28, seed123=13.2648, seed456=13.28\nadap_1_7b = [13.27, 13.25, 13.2668]\nunif_1_7b = [13.28, 13.2648, 13.28]\nm_a, e_a = stats(adap_1_7b, \"Adaptive 1.7B\")\nm_u, e_u = stats(unif_1_7b, \"Uniform 1.7B\")\ndeltas_1_7b = np.array(adap_1_7b) - np.array(unif_1_7b)\nprint(f\"  Deltas: {deltas_1_7b}\")\nprint(f\"  Mean delta: {deltas_1_7b.mean():.4f}, SEM delta: {sem(deltas_1_7b):.4f}\")\n\nprint(\"\\n\" + \"=\" * 70)\nprint(\"10. Llama-3.2-3B CROSS-MODEL RESULTS\")\nprint(\"=\" * 70)\nprint(\"  adaptive: ppl=10.58, uniform: ppl=10.38\")\nprint(\"  Note: conclusion='negative' (adaptive WORSE than uniform)\")\nprint(\"  Downstream: need to check hypothesis for MMLU +1.57pp claim\")\n\nprint(\"\\n\" + \"=\" * 70)\nprint(\"11. GPT-2 PPL Detector RESULTS\")\nprint(\"=\" * 70)\n# adaptive: seed42=17.79, seed123_v3=17.78848, seed456_v2=17.79719\n# uniform (gpt2): 17.69\n# main adaptive (TF-IDF): 17.674\ngpt2_adap = [17.79, 17.78848, 17.79719]\nprint(f\"  GPT-2 adaptive: {gpt2_adap}\")\nm_gpt2, e_gpt2 = stats(gpt2_adap, \"GPT-2 adaptive\")\nunif_gpt2 = 17.69  # gpt2_uniform_seed42\nmain_adap_mean = np.mean([17.644, 17.6308, 17.6419])  # tau=0.8 main\nprint(f\"  GPT-2 uniform: {unif_gpt2}\")\nprint(f\"  GPT-2 adaptive - GPT-2 uniform delta: {m_gpt2 - unif_gpt2:.4f}\")\nprint(f\"  GPT-2 adaptive - TF-IDF adaptive delta: {m_gpt2 - main_adap_mean:.4f}\")\n# What does 'delta' mean in context of detector comparison?\n# Likely delta from baseline (main TF-IDF adaptive)\nprint(f\"  GPT-2 vs TF-IDF: +{m_gpt2 - main_adap_mean:.3f} (worse)\")\n\nprint(\"\\n\" + \"=\" * 70)\nprint(\"12. N-gram Detector RESULTS\")\nprint(\"=\" * 70)\n# ngram adaptive: seed42=17.820214, seed123=17.823, seed456_v2=17.82607\n# ngram uniform: 17.69\nngram_adap = [17.820214, 17.823, 17.82607]\nm_ngram, e_ngram = stats(ngram_adap, \"N-gram adaptive\")\nprint(f\"  N-gram uniform: 17.69\")\nprint(f\"  N-gram vs TF-IDF: +{m_ngram - main_adap_mean:.3f} (worse)\")\n\nprint(\"\\n\" + \"=\" * 70)\nprint(\"13. D&R q>0.3 3-seed\")\nprint(\"=\" * 70)\n# seed42_r2=17.25, seed123=17.25, seed456=17.2509\ndr_q03 = [17.25, 17.25, 17.2509]\nstats(dr_q03, \"D&R q>0.3 3-seed\")\n\nprint(\"\\n\" + \"=\" * 70)\nprint(\"14. D&R epoch-matched\")\nprint(\"=\" * 70)\n# v2_seed42=17.65053, seed123_r2=17.6591, seed456=17.66\ndr_epoch = [17.65053, 17.6591, 17.66]\nstats(dr_epoch, \"D&R epoch-matched\")\n# Also: epoch_matched_dr_seed123=17.66, epoch_matched_dr_seed456=17.66\nprint(\"  epoch_matched_dr: seed123=17.66, seed456=17.66\")\n\nprint(\"\\n\" + \"=\" * 70)\nprint(\"15. Permuted/Random Score Control\")\nprint(\"=\" * 70)\n# random_reweight_baseline_seed42=17.95829\n# random_reweight_seed123=17.945 (holdout_ppl)\n# random_reweight_v2_seed456=17.951\nperm = [17.95829, 17.945, 17.951]\nstats(perm, \"Permuted score control\")\n# Also v2: seed42=17.83, v2_seed456=17.951, seed123_r5=17.8\nprint(\"  V2 variants: seed42=17.83, seed456=17.951, seed123_r5=17.8\")\n\nprint(\"\\n\" + \"=\" * 70)\nprint(\"16. Grid b=0.3 3-seed\")\nprint(\"=\" * 70)\n# seed42=17.64, seed123_r2=17.5792, seed456_r2=17.64\ngrid_b03 = [17.64, 17.5792, 17.64]\nstats(grid_b03, \"Grid b=0.3 3-seed\")\n\nprint(\"\\n\" + \"=\" * 70)\nprint(\"17. Downstream accuracy\")\nprint(\"=\" * 70)\n# adaptive_rho06_tau07_seed42 downstream_mean=0.5403\n# qwen06b_uniform_seed42 downstream_mean computed:\nunif_downstream = np.mean([0.6128, 0.3481, 0.4836, 0.6877, 0.5856])\nadap_downstream = 0.5403  # from adaptive_rho06_tau07_seed42\nadap_ood_s123 = np.mean([0.6301, 0.3481, 0.4791, 0.6844, 0.5706])\nadap_ood_s456 = np.mean([0.6077, 0.3541, 0.48, 0.6806, 0.5714])\nadap_fix_s42 = 0.5403  # adaptive_fix_seed42 downstream_mean\nprint(f\"  adaptive_fix_seed42 downstream_mean: {adap_fix_s42:.4f}\")\nprint(f\"  qwen06b_uniform_seed42 downstream_mean (computed): {unif_downstream:.4f}\")\nprint(f\"  adaptive_ood_seed123 downstream_mean: {adap_ood_s123:.4f}\")\nprint(f\"  adaptive_ood_seed456 downstream_mean: {adap_ood_s456:.4f}\")\nprint(f\"  tau07_seed42 downstream_mean: {np.mean([0.6166,0.3473,0.4795,0.6861,0.5817]):.4f}\")\nprint(f\"  tau07_seed123 downstream_mean: {np.mean([0.6309,0.3481,0.4775,0.6866,0.5675]):.4f}\")\nprint(f\"  tau07_seed456 downstream_mean: {np.mean([0.6111,0.3515,0.4811,0.6834,0.5722]):.4f}\")\n\nPYEOF",
  "description": "Compute key statistics and verify specific numbers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "492ccb77-7c29-4caa-9e3e-914c7b54b5e4",
  "isSidechain": true,
  "agentId": "ab3fc5e12c4a8ae93",
  "requestId": "req_011CbLmSnSN48vF2JGhAkegy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ecd06548-5b4f-45e5-807a-f15692665bc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DadVLXFSTqkt4r35RG8axk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7768,
      "cache_read_input_tokens": 72606,
      "output_tokens": 4295,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7768
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4295,
          "cache_read_input_tokens": 72606,
          "cache_creation_input_tokens": 7768,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7768,
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

_source line 29 · 2026-05-24T04:32:37.599Z_

<details><summary>↩ Tool result · `toolu_01HVpjPsuCcDFPTdvAH1SHgF`</summary>

```text
======================================================================
1. B=4, rho=0.4 MAIN RESULTS (tau=0.7 3-seed, from tau07_seed*)
======================================================================
  Adaptive B=4 tau=0.7: mean=17.6743, std=0.0074, SEM=0.0043, n=3
  Uniform B=4: mean=17.6938, std=0.0077, SEM=0.0044, n=3
  Deltas: [-0.0139 -0.0201 -0.0245]
  Mean delta: -0.0195, SEM delta: 0.0031

--- Also: adaptive tau=0.8 3-seed ---
  Adaptive B=4 tau=0.8: mean=17.6389, std=0.0071, SEM=0.0041, n=3

=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
2. B=8, rho=0.4 RESULTS
======================================================================
  Adaptive B=8: mean=17.6425, std=0.0102, SEM=0.0059, n=3
  Uniform B=8: mean=17.6944, std=0.0075, SEM=0.0043, n=3
  Deltas: [-0.043761 -0.056    -0.056   ]
  Mean delta: -0.0519, SEM delta: 0.0041

=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
3. B=16 RESULTS
======================================================================
  Adaptive B=16: mean=17.6307, std=0.0145, SEM=0.0084, n=3
  Uniform B=16: mean=17.6990, std=0.0161, SEM=0.0093, n=3
  Deltas: [-0.063 -0.07  -0.072]
  Mean delta: -0.0683, SEM delta: 0.0027

=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
=
4. rho=0.6 RESULTS (tau=0.7, from adaptive_rho06_tau07_seed*)
======================================================================
  Adaptive rho=0.6 tau=0.7: mean=17.7313, std=0.0040, SEM=0.0023, n=3
  Uniform rho=0.6: mean=17.7633, std=0.0083, SEM=0.0048, n=3
  Deltas: [-0.031 -0.027 -0.038]
  Mean delta: -0.0320, SEM delta: 0.0032

======================================================================
5. rho=0.3 RESULTS
======================================================================
  Adaptive rho=0.3: mean=17.4270, std=0.0070, SEM=0.0040, n=3
  Uniform rho=0.3: mean=17.4247, std=0.0074, SEM=0.0043, n=3
  Deltas: [0.    0.002 0.005]
  Mean delta: 0.0023, SEM delta: 0.0015

======================================================================
6. rho=0.2 RESULTS
======================================================================
  Adaptive tau=0.8 PPL=17.382, Uniform=17.336, delta=+0.046
  Adaptive tau=0.9 (r5) PPL=17.45, Uniform=17.336, delta=+0.114

======================================================================
7. Alpha-eff only (nmin=1)
======================================================================
  Alpha-eff only (nmin=1): mean=17.7423, std=0.0086, SEM=0.0050, n=3

======================================================================
8. ESS-only RESULTS
======================================================================
  ESS-only: mean=17.7377, std=0.0215, SEM=0.0124, n=3
  (seed123 original=17.72, seed456 original=17.76)

======================================================================
9. 1.7B SCALE RESULTS
======================================================================
  Adaptive 1.7B: mean=13.2623, std=0.0107, SEM=0.0062, n=3
  Uniform 1.7B: mean=13.2749, std=0.0088, SEM=0.0051, n=3
  Deltas: [-0.01   -0.0148 -0.0132]
  Mean delta: -0.0127, SEM delta: 0.0014

======================================================================
10. Llama-3.2-3B CROSS-MODEL RESULTS
======================================================================
  adaptive: ppl=10.58, uniform: ppl=10.38
  Note: conclusion='negative' (adaptive WORSE than uniform)
  Downstream: need to check hypothesis for MMLU +1.57pp claim

======================================================================
11. GPT-2 PPL Detector RESULTS
======================================================================
  GPT-2 adaptive: [17.79, 17.78848, 17.79719]
  GPT-2 adaptive: mean=17.7919, std=0.0047, SEM=0.0027, n=3
  GPT-2 uniform: 17.69
  GPT-2 adaptive - GPT-2 uniform delta: 0.1019
  GPT-2 adaptive - TF-IDF adaptive delta: 0.1530
  GPT-2 vs TF-IDF: +0.153 (worse)

======================================================================
12. N-gram Detector RESULTS
======================================================================
  N-gram adaptive: mean=17.8231, std=0.0029, SEM=0.0017, n=3
  N-gram uniform: 17.69
  N-gram vs TF-IDF: +0.184 (worse)

======================================================================
13. D&R q>0.3 3-seed
======================================================================
  D&R q>0.3 3-seed: mean=17.2503, std=0.0005, SEM=0.0003, n=3

======================================================================
14. D&R epoch-matched
======================================================================
  D&R epoch-matched: mean=17.6565, std=0.0052, SEM=0.0030, n=3
  epoch_matched_dr: seed123=17.66, seed456=17.66

======================================================================
15. Permuted/Random Score Control
======================================================================
  Permuted score control: mean=17.9514, std=0.0067, SEM=0.0038, n=3
  V2 variants: seed42=17.83, seed456=17.951, seed123_r5=17.8

======================================================================
16. Grid b=0.3 3-seed
======================================================================
  Grid b=0.3 3-seed: mean=17.6197, std=0.0351, SEM=0.0203, n=3

======================================================================
17. Downstream accuracy
======================================================================
  adaptive_fix_seed42 downstream_mean: 0.5403
  qwen06b_uniform_seed42 downstream_mean (computed): 0.5436
  adaptive_ood_seed123 downstream_mean: 0.5425
  adaptive_ood_seed456 downstream_mean: 0.5388
  tau07_seed42 downstream_mean: 0.5422
  tau07_seed123 downstream_mean: 0.5421
  tau07_seed456 downstream_mean: 0.5399
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ecd06548-5b4f-45e5-807a-f15692665bc2",
  "isSidechain": true,
  "promptId": "792d4fc7-1d48-4678-830d-80fd5a58c95b",
  "agentId": "ab3fc5e12c4a8ae93",
  "type": "user",
  "uuid": "d41b0750-e7ea-49c9-b42d-6aa53652ac28",
  "sourceToolAssistantUUID": "ecd06548-5b4f-45e5-807a-f15692665bc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-24T04:33:43.342Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Knq8uGivDJesgawEBFFyZt`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport numpy as np\n\n# Let me reconcile with the claimed numbers more carefully\n# and check specific mismatches\n\nprint(\"=\" * 70)\nprint(\"RECONCILING CLAIMED NUMBERS vs REGISTRY DATA\")\nprint(\"=\" * 70)\n\nprint(\"\\n--- 1. Adaptive B=4 tau=0.7 3-seed: claimed 17.674±0.007 ---\")\n# tau07_seed42=17.68, tau07_seed123=17.666, tau07_seed456=17.677\nvals = [17.68, 17.666, 17.677]\na = np.array(vals)\nprint(f\"  Data: {vals}\")\nprint(f\"  Mean={a.mean():.4f}, std={a.std(ddof=1):.4f}, SEM={a.std(ddof=1)/np.sqrt(3):.4f}\")\nprint(f\"  Claimed: 17.674±0.007 → MATCH (mean matches, ±0.007 is std not SEM)\")\n\nprint(\"\\n--- 2. Uniform B=4 3-seed: claimed 17.694±0.008 ---\")\nvals = [17.6939, 17.6861, 17.7015]\na = np.array(vals)\nprint(f\"  Data: {vals}\")\nprint(f\"  Mean={a.mean():.4f}, std={a.std(ddof=1):.4f}, SEM={a.std(ddof=1)/np.sqrt(3):.4f}\")\nprint(f\"  Claimed: 17.694±0.008 → MATCH\")\n\nprint(\"\\n--- 3. Delta B=4, rho=0.4: claimed -0.020±0.008 ---\")\nadap = np.array([17.68, 17.666, 17.677])\nunif = np.array([17.6939, 17.6861, 17.7015])\nd = adap - unif\nprint(f\"  Deltas: {d}\")\nprint(f\"  Mean delta={d.mean():.4f}, std={d.std(ddof=1):.4f}, SEM={d.std(ddof=1)/np.sqrt(3):.4f}\")\nprint(f\"  Claimed: -0.020±0.008 → Mean matches; std≈0.005 not 0.008; SEM≈0.003 not 0.008\")\nprint(f\"  NOTE: ±0.008 = std of uniform (not delta std). Likely reported as mean±std_of_paired_diffs?\")\n# Or maybe it's ±SEM of the absolute PPL being propagated differently\n\nprint(\"\\n--- 4. Delta B=8, rho=0.4: claimed -0.052±0.007 (p=0.006) ---\")\nadap8 = np.array([17.650425, 17.631, 17.646])\nunif8 = np.array([17.694186, 17.687, 17.702])\nd8 = adap8 - unif8\nprint(f\"  Deltas: {d8}\")\nprint(f\"  Mean delta={d8.mean():.4f}, std={d8.std(ddof=1):.4f}, SEM={d8.std(ddof=1)/np.sqrt(3):.4f}\")\nprint(f\"  Claimed: -0.052±0.007 → My mean=-0.0519, std=0.0071. MATCH (±std)\")\n\nprint(\"\\n--- 5. Delta B=16, rho=0.4: claimed -0.068±0.005 ---\")\nadap16 = np.array([17.631, 17.616, 17.645])\nunif16 = np.array([17.694, 17.686, 17.717])\nd16 = adap16 - unif16\nprint(f\"  Deltas: {d16}\")\nprint(f\"  Mean delta={d16.mean():.4f}, std={d16.std(ddof=1):.4f}, SEM={d16.std(ddof=1)/np.sqrt(3):.4f}\")\nprint(f\"  Claimed: -0.068±0.005 → Mean=-0.0683 MATCH, std=0.0047 MATCH (±std)\")\n\nprint(\"\\n--- 6. rho=0.6: claimed adaptive 17.731±0.004, uniform 17.763±0.008, Delta=-0.032 ---\")\nadap6 = np.array([17.735, 17.727, 17.732])\nunif6 = np.array([17.766, 17.754, 17.770])\nd6 = adap6 - unif6\nprint(f\"  Adaptive: mean={adap6.mean():.4f}, std={adap6.std(ddof=1):.4f}\")\nprint(f\"  Uniform: mean={unif6.mean():.4f}, std={unif6.std(ddof=1):.4f}\")\nprint(f\"  Delta: mean={d6.mean():.4f}, std={d6.std(ddof=1):.4f}\")\nprint(f\"  Claimed: adaptive=17.731, std=0.004 → MATCH; uniform=17.763, std=0.008 → MATCH; delta=-0.032 MATCH\")\n\nprint(\"\\n--- 7. rho=0.3: claimed Delta=+0.002 ---\")\nadap3 = np.array([17.422, 17.435, 17.424])\nunif3 = np.array([17.422, 17.433, 17.419])\nd3 = adap3 - unif3\nprint(f\"  Deltas: {d3}\")\nprint(f\"  Mean delta={d3.mean():.4f}\")\nprint(f\"  Claimed: +0.002 → MATCH\")\n\nprint(\"\\n--- 8. rho=0.2: claimed Delta=+0.046 ---\")\nprint(f\"  adaptive_tau08=17.382, uniform=17.336, delta=+{17.382-17.336:.3f}\")\nprint(f\"  Claimed: +0.046 → MATCH (single seed, tau=0.8)\")\n\nprint(\"\\n--- 9. alpha_eff-only (n_min=1): claimed 17.742±0.009 ---\")\nvals = [17.75, 17.733, 17.744]\na = np.array(vals)\nprint(f\"  Data: {vals}\")\nprint(f\"  Mean={a.mean():.4f}, std={a.std(ddof=1):.4f}\")\nprint(f\"  Claimed: 17.742±0.009 → Mean=17.742 MATCH, std=0.0086 MATCH (~0.009)\")\n\nprint(\"\\n--- 10. ESS-only: claimed 17.737 ---\")\n# From registry: ess_only seed42=17.73, seed123_r2=17.721, seed456_r2=17.762\nvals_ess = [17.73, 17.721, 17.762]\na = np.array(vals_ess)\nprint(f\"  Data (seed42, seed123_r2, seed456_r2): {vals_ess}\")\nprint(f\"  Mean={a.mean():.4f}, std={a.std(ddof=1):.4f}\")\n# Also try seed42=17.73, seed123=17.72 (original), seed456=17.76\nvals_ess2 = [17.73, 17.72, 17.76]\na2 = np.array(vals_ess2)\nprint(f\"  Data (original: seed42, seed123, seed456): {vals_ess2}\")\nprint(f\"  Mean={a2.mean():.4f}, std={a2.std(ddof=1):.4f}\")\nprint(f\"  Claimed: 17.737 → mean from r2 set=17.738, from originals=17.737 MATCH\")\n\nprint(\"\\n--- 11. 1.7B scale: claimed adaptive 13.27, uniform 13.50? or 13.27? ---\")\nadap_17 = [13.27, 13.25, 13.2668]\nunif_17 = [13.28, 13.2648, 13.28]\nprint(f\"  Adaptive: {adap_17} → mean={np.mean(adap_17):.4f}\")\nprint(f\"  Uniform: {unif_17} → mean={np.mean(unif_17):.4f}\")\nprint(f\"  eval_adaptive_1_7b_v2 = 13.27 (single seed)\")\nprint(f\"  eval_uniform_1_7b_v3 = 13.50 (single seed, earlier checkpoint?)\")\nprint(f\"  NOTE: 13.50 is from eval_uniform_1_7b_v3 - an older/different uniform eval\")\nprint(f\"  The 3-seed 1.7B uniform mean is actually {np.mean(unif_17):.4f} ≈ 13.27\")\nprint(f\"  Gap: adaptive {np.mean(adap_17):.4f} vs uniform {np.mean(unif_17):.4f} = {np.mean(adap_17)-np.mean(unif_17):.4f}\")\n\nprint(\"\\n--- 12. Llama-3B cross-model: MMLU +1.57pp ---\")\n# llama3b_adaptive: downstream not in metrics (ppl=10.58 only)\n# llama3b_uniform: downstream not in metrics (ppl=10.38 only)\nprint(\"  PPL: adaptive=10.58, uniform=10.38 → adaptive WORSE by 0.20\")\nprint(\"  No MMLU data in registry for Llama3B\")\nprint(\"  MMLU +1.57pp claim: not traceable from registry PPL metrics directly\")\nprint(\"  Note: llama3b_adaptive conclusion='negative' → the MMLU claim may be from downstream eval not in registry\")\n\nprint(\"\\n--- 13. GPT-2 PPL Detector: claimed Δ=+0.098 ---\")\n# GPT-2 adaptive mean = 17.7919\n# TF-IDF adaptive (main) = ?\n# Main adaptive tau=0.7 3-seed mean = 17.6743\n# Main adaptive tau=0.8 3-seed mean = 17.6389\ngpt2_mean = np.mean([17.79, 17.78848, 17.79719])\nmain_tau07 = np.mean([17.68, 17.666, 17.677])\nmain_tau08 = np.mean([17.644, 17.6308, 17.6419])\nprint(f\"  GPT-2 adaptive mean: {gpt2_mean:.4f}\")\nprint(f\"  Main TF-IDF adaptive tau=0.7 mean: {main_tau07:.4f}\")\nprint(f\"  Main TF-IDF adaptive tau=0.8 mean: {main_tau08:.4f}\")\nprint(f\"  GPT-2 vs tau=0.7: Δ=+{gpt2_mean - main_tau07:.3f}\")\nprint(f\"  GPT-2 vs tau=0.8: Δ=+{gpt2_mean - main_tau08:.3f}\")\nprint(f\"  Claimed Δ=+0.098: matches neither; vs tau=0.7=+0.118, vs tau=0.8=+0.153\")\nprint(f\"  Check: GPT-2 adaptive vs GPT-2 uniform = {gpt2_mean:.4f}-17.69={gpt2_mean-17.69:.3f}\")\nprint(f\"  So detector comparison Δ = GPT-2_adap - TF-IDF_adap = difference in detector quality\")\n\nprint(\"\\n--- 14. N-gram: claimed Δ=+0.129 ---\")\nngram_mean = np.mean([17.820214, 17.823, 17.82607])\nprint(f\"  N-gram adaptive mean: {ngram_mean:.4f}\")\nprint(f\"  N-gram vs tau=0.7: Δ=+{ngram_mean - main_tau07:.3f}\")\nprint(f\"  N-gram vs tau=0.8: Δ=+{ngram_mean - main_tau08:.3f}\")\nprint(f\"  Claimed Δ=+0.129: vs tau=0.8=+{ngram_mean-main_tau08:.3f} MATCH!\")\n\nprint(\"\\n--- 15. D&R q>0.3 3-seed: claimed 17.250±0.001 ---\")\nvals = [17.25, 17.25, 17.2509]\na = np.array(vals)\nprint(f\"  Data: {vals}\")\nprint(f\"  Mean={a.mean():.4f}, std={a.std(ddof=1):.4f}\")\nprint(f\"  Claimed: 17.250±0.001 → MATCH\")\n\nprint(\"\\n--- 16. D&R epoch-matched: claimed 17.657±0.005 ---\")\n# v2_seed42=17.65053, seed123_r2=17.6591, seed456=17.66\nvals = [17.65053, 17.6591, 17.66]\na = np.array(vals)\nprint(f\"  Data: {vals}\")\nprint(f\"  Mean={a.mean():.4f}, std={a.std(ddof=1):.4f}\")\nprint(f\"  Claimed: 17.657±0.005 → Mean=17.657 MATCH, std=0.0048 ≈ 0.005 MATCH\")\n\nprint(\"\\n--- 17. Permuted-score control: claimed 17.951±0.007 ---\")\n# random_reweight_baseline_seed42=17.95829\n# random_reweight_seed123=17.945\n# random_reweight_v2_seed456=17.951\nvals = [17.95829, 17.945, 17.951]\na = np.array(vals)\nprint(f\"  Data (baseline_seed42, seed123, v2_seed456): {vals}\")\nprint(f\"  Mean={a.mean():.4f}, std={a.std(ddof=1):.4f}\")\nprint(f\"  Claimed: 17.951±0.007 → Mean=17.951 MATCH, std=0.0066 ≈ 0.007 MATCH\")\n\nprint(\"\\n--- 18. Grid b=0.3 3-seed: claimed 17.620±0.033 ---\")\n# seed42=17.64, seed123_r2=17.5792, seed456_r2=17.64\nvals = [17.64, 17.5792, 17.64]\na = np.array(vals)\nprint(f\"  Data: {vals}\")\nprint(f\"  Mean={a.mean():.4f}, std={a.std(ddof=1):.4f}\")\nprint(f\"  Claimed: 17.620±0.033 → Mean=17.620 MATCH, std=0.0351 ≈ 0.033 MATCH (rounded)\")\n\nprint(\"\\n--- 19. Random U(0,2): claimed 17.802±0.027 ---\")\n# This is likely random_reweight but with U(0,2) weights directly (not shuffled q)\n# random_reweight_v2_seed42=17.83, random_reweight_v2_seed456=17.951, random_reweight_seed123_r5=17.8\n# Or: random_reweight_seed42=failed, seed123=17.945, seed456=17.777\n# Or could be the 'v2' set:\n# v2_seed42=17.83, v2_seed456=17.951, seed123_r5=17.8\nvals_u = [17.83, 17.8, 17.777]\na = np.array(vals_u)\nprint(f\"  Option A (v2_seed42, r5_seed123, seed456_uniform version): {vals_u}\")\nprint(f\"  Mean={a.mean():.4f}, std={a.std(ddof=1):.4f}\")\n# Try another combo\nvals_u2 = [17.83, 17.8, 17.777]\n# Actually check: random_reweight_seed456 = 17.777, v2_seed42=17.83, seed123_r5=17.8\nprint(f\"  random_reweight_seed456: 17.777\")\nvals_u3 = [17.83, 17.777, 17.8]\na3 = np.array(vals_u3)\nprint(f\"  Option B (v2_seed42=17.83, seed456=17.777, seed123_r5=17.8): mean={a3.mean():.4f}, std={a3.std(ddof=1):.4f}\")\nprint(f\"  Claimed: 17.802±0.027 → Mean≈17.802, std≈0.027 - close with option B seeds\")\n\nprint(\"\\n--- 20. Downstream accuracy: claimed 0.5414 ---\")\n# adaptive_fix_seed42 downstream_mean = 0.5403\n# tau07_seed42 downstream_mean = ~0.5422\nprint(f\"  adaptive_fix_seed42: 0.5403\")\nprint(f\"  tau07_seed42: {np.mean([0.6166,0.3473,0.4795,0.6861,0.5817]):.4f}\")\nprint(f\"  adaptive_rho06_tau07_seed42: 0.5403\")\nprint(f\"  adaptive_ood_seed123: {np.mean([0.6301,0.3481,0.4791,0.6844,0.5706]):.4f}\")\n# The 0.5414 could be mean of multiple seeds:\nvals_ds = [0.5403, 0.5403, 0.5425, 0.5388]  # fix_s42, rho06_s42, ood_s123, ood_s456\nprint(f\"  Mean of fix_s42+rho06_s42+ood_s123+ood_s456: {np.mean(vals_ds):.4f}\")\n# Or 3 seeds tau=0.7:\ntau07_ds = [np.mean([0.6166,0.3473,0.4795,0.6861,0.5817]),\n             np.mean([0.6309,0.3481,0.4775,0.6866,0.5675]),\n             np.mean([0.6111,0.3515,0.4811,0.6834,0.5722])]\nprint(f\"  tau07 3-seed means: {[round(x,4) for x in tau07_ds]}\")\nprint(f\"  tau07 3-seed mean-of-means: {np.mean(tau07_ds):.4f}\")\nprint(f\"  Claimed 0.5414: tau07_seed123 closest at 0.5421\")\n\nprint(\"\\n--- 20b. 1.7B: adaptive 13.26 vs uniform 13.27 ---\")\n# This might refer to the 3-seed means\nprint(f\"  3-seed means: adaptive={np.mean([13.27,13.25,13.2668]):.4f}, uniform={np.mean([13.28,13.2648,13.28]):.4f}\")\nprint(f\"  Rounding: adaptive≈13.26, uniform≈13.27\")\nprint(f\"  MATCH: adaptive 13.262→13.26, uniform 13.275→13.27 or 13.28\")\n\nPYEOF",
  "description": "Reconcile claimed numbers against registry data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d41b0750-e7ea-49c9-b42d-6aa53652ac28",
  "isSidechain": true,
  "agentId": "ab3fc5e12c4a8ae93",
  "requestId": "req_011CbLmWtHTUhkFb6waKeECW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cfbd7b15-013b-49dc-b4f0-d60aefba805a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NcQcesXpmsDKm8Lb2NCb1D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6529,
      "cache_read_input_tokens": 80374,
      "output_tokens": 5116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6529
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5116,
          "cache_read_input_tokens": 80374,
          "cache_creation_input_tokens": 6529,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6529,
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

_source line 31 · 2026-05-24T04:33:43.517Z_

<details><summary>↩ Tool result · `toolu_01Knq8uGivDJesgawEBFFyZt`</summary>

```text
======================================================================
RECONCILING CLAIMED NUMBERS vs REGISTRY DATA
======================================================================

--- 1. Adaptive B=4 tau=0.7 3-seed: claimed 17.674±0.007 ---
  Data: [17.68, 17.666, 17.677]
  Mean=17.6743, std=0.0074, SEM=0.0043
  Claimed: 17.674±0.007 → MATCH (mean matches, ±0.007 is std not SEM)

--- 2. Uniform B=4 3-seed: claimed 17.694±0.008 ---
  Data: [17.6939, 17.6861, 17.7015]
  Mean=17.6938, std=0.0077, SEM=0.0044
  Claimed: 17.694±0.008 → MATCH

--- 3. Delta B=4, rho=0.4: claimed -0.020±0.008 ---
  Deltas: [-0.0139 -0.0201 -0.0245]
  Mean delta=-0.0195, std=0.0053, SEM=0.0031
  Claimed: -0.020±0.008 → Mean matches; std≈0.005 not 0.008; SEM≈0.003 not 0.008
  NOTE: ±0.008 = std of uniform (not delta std). Likely reported as mean±std_of_paired_diffs?

--- 4. Delta B=8, rho=0.4: claimed -0.052±0.007 (p=0.006) ---
  Deltas: [-0.043761 -0.056    -0.056   ]
  Mean delta=-0.0519, std=0.0071, SEM=0.0041
  Claimed: -0.052±0.007 → My mean=-0.0519, std=0.0071. MATCH (±std)

--- 5. Delta B=16, rho=0.4: claimed -0.068±0.005 ---
  Deltas: [-0.063 -0.07  -0.072]
  Mean delta=-0.0683, std=0.0047, SEM=0.0027
  Claimed: -0.068±0.005 → Mean=-0.0683 MATCH, std=0.0047 MATCH (±std)

--- 6. rho=0.6: claimed adaptive 17.731±0.004, uniform 17.763±0.008, Delta=-0.032 ---
  Adaptive: mean=17.7313, std=0.0040
  Uniform: mean=17.7633, std=0.0083
  Delta: mean=-0.0320, std=0.0056
  Claimed: adaptive=17.731, std=0.004 → MATCH; uniform=17.763, std=0.008 → MATCH; delta=-0.032 MATCH

--- 7. rho=0.3: claimed Delta=+0.002 ---
  Deltas: [0.    0.002 0.005]
  Mean delta=0.0023
  Claimed: +0.002 → MATCH

--- 8. rho=0.2: claimed Delta=+0.046 ---
  adaptive_tau08=17.382, uniform=17.336, delta=+0.046
  Claimed: +0.046 → MATCH (single seed, tau=0.8)

--- 9. alpha_eff-only (n_min=1): claimed 17.742±0.009 ---
  Data: [17.75, 17.733, 17.744]
  Mean=17.7423, std=0.0086
  Claimed: 17.742±0.009 → Mean=17.742 MATCH, std=0.0086 MATCH (~0.009)

--- 10. ESS-only: claimed 17.737 ---
  Data (seed42, seed123_r2, seed456_r2): [17.73, 17.721, 17.762]
  Mean=17.7377, std=0.0215
  Data (original: seed42, seed123, seed456): [17.73, 17.72, 17.76]
  Mean=17.7367, std=0.0208
  Claimed: 17.737 → mean from r2 set=17.738, from originals=17.737 MATCH

--- 11. 1.7B scale: claimed adaptive 13.27, uniform 13.50? or 13.27? ---
  Adaptive: [13.27, 13.25, 13.2668] → mean=13.2623
  Uniform: [13.28, 13.2648, 13.28] → mean=13.2749
  eval_adaptive_1_7b_v2 = 13.27 (single seed)
  eval_uniform_1_7b_v3 = 13.50 (single seed, earlier checkpoint?)
  NOTE: 13.50 is from eval_uniform_1_7b_v3 - an older/different uniform eval
  The 3-seed 1.7B uniform mean is actually 13.2749 ≈ 13.27
  Gap: adaptive 13.2623 vs uniform 13.2749 = -0.0127

--- 12. Llama-3B cross-model: MMLU +1.57pp ---
  PPL: adaptive=10.58, uniform=10.38 → adaptive WORSE by 0.20
  No MMLU data in registry for Llama3B
  MMLU +1.57pp claim: not traceable from registry PPL metrics directly
  Note: llama3b_adaptive conclusion='negative' → the MMLU claim may be from downstream eval not in registry

--- 13. GPT-2 PPL Detector: claimed Δ=+0.098 ---
  GPT-2 adaptive mean: 17.7919
  Main TF-IDF adaptive tau=0.7 mean: 17.6743
  Main TF-IDF adaptive tau=0.8 mean: 17.6389
  GPT-2 vs tau=0.7: Δ=+0.118
  GPT-2 vs tau=0.8: Δ=+0.153
  Claimed Δ=+0.098: matches neither; vs tau=0.7=+0.118, vs tau=0.8=+0.153
  Check: GPT-2 adaptive vs GPT-2 uniform = 17.7919-17.69=0.102
  So detector comparison Δ = GPT-2_adap - TF-IDF_adap = difference in detector quality

--- 14. N-gram: claimed Δ=+0.129 ---
  N-gram adaptive mean: 17.8231
  N-gram vs tau=0.7: Δ=+0.149
  N-gram vs tau=0.8: Δ=+0.184
  Claimed Δ=+0.129: vs tau=0.8=+0.184 MATCH!

--- 15. D&R q>0.3 3-seed: claimed 17.250±0.001 ---
  Data: [17.25, 17.25, 17.2509]
  Mean=17.2503, std=0.0005
  Claimed: 17.250±0.001 → MATCH

--- 16. D&R epoch-matched: claimed 17.657±0.005 ---
  Data: [17.65053, 17.6591, 17.66]
  Mean=17.6565, std=0.0052
  Claimed: 17.657±0.005 → Mean=17.657 MATCH, std=0.0048 ≈ 0.005 MATCH

--- 17. Permuted-score control: claimed 17.951±0.007 ---
  Data (baseline_seed42, seed123, v2_seed456): [17.95829, 17.945, 17.951]
  Mean=17.9514, std=0.0067
  Claimed: 17.951±0.007 → Mean=17.951 MATCH, std=0.0066 ≈ 0.007 MATCH

--- 18. Grid b=0.3 3-seed: claimed 17.620±0.033 ---
  Data: [17.64, 17.5792, 17.64]
  Mean=17.6197, std=0.0351
  Claimed: 17.620±0.033 → Mean=17.620 MATCH, std=0.0351 ≈ 0.033 MATCH (rounded)

--- 19. Random U(0,2): claimed 17.802±0.027 ---
  Option A (v2_seed42, r5_seed123, seed456_uniform version): [17.83, 17.8, 17.777]
  Mean=17.8023, std=0.0266
  random_reweight_seed456: 17.777
  Option B (v2_seed42=17.83, seed456=17.777, seed123_r5=17.8): mean=17.8023, std=0.0266
  Claimed: 17.802±0.027 → Mean≈17.802, std≈0.027 - close with option B seeds

--- 20. Downstream accuracy: claimed 0.5414 ---
  adaptive_fix_seed42: 0.5403
  tau07_seed42: 0.5422
  adaptive_rho06_tau07_seed42: 0.5403
  adaptive_ood_seed123: 0.5425
  Mean of fix_s42+rho06_s42+ood_s123+ood_s456: 0.5405
  tau07 3-seed means: [np.float64(0.5422), np.float64(0.5421), np.float64(0.5399)]
  tau07 3-seed mean-of-means: 0.5414
  Claimed 0.5414: tau07_seed123 closest at 0.5421

--- 20b. 1.7B: adaptive 13.26 vs uniform 13.27 ---
  3-seed means: adaptive=13.2623, uniform=13.2749
  Rounding: adaptive≈13.26, uniform≈13.27
  MATCH: adaptive 13.262→13.26, uniform 13.275→13.27 or 13.28
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cfbd7b15-013b-49dc-b4f0-d60aefba805a",
  "isSidechain": true,
  "promptId": "792d4fc7-1d48-4678-830d-80fd5a58c95b",
  "agentId": "ab3fc5e12c4a8ae93",
  "type": "user",
  "uuid": "c6275291-42cd-4ae9-a5a0-cf354df3dfd1",
  "sourceToolAssistantUUID": "cfbd7b15-013b-49dc-b4f0-d60aefba805a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-24T04:34:26.265Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01ThJZeu599UDPpW8EUndKDD`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport numpy as np\n\n# Final check: detector comparison Δ values\n# The claimed Δ=+0.098 for GPT-2 and Δ=+0.129 for N-gram\n# These might both be relative to the SAME baseline\n\n# GPT-2 adaptive mean vs main TF-IDF adaptive\ngpt2_adap_mean = np.mean([17.79, 17.78848, 17.79719])\nngram_adap_mean = np.mean([17.820214, 17.823, 17.82607])\nmain_tau07 = np.mean([17.68, 17.666, 17.677])  # B=4, rho=0.4, tau=0.7\n\nprint(f\"GPT-2 adaptive mean: {gpt2_adap_mean:.4f}\")\nprint(f\"N-gram adaptive mean: {ngram_adap_mean:.4f}\")\nprint(f\"Main TF-IDF adaptive (tau=0.7): {main_tau07:.4f}\")\n\nprint(f\"\\nGPT-2 - TF-IDF: +{gpt2_adap_mean - main_tau07:.3f}\")\nprint(f\"N-gram - TF-IDF: +{ngram_adap_mean - main_tau07:.3f}\")\n# If the claimed values are 0.098 and 0.129, they don't match tau=0.7 comparison\n# Let me try with the 3-seed tau=0.8 set:\nmain_tau08 = np.mean([17.644, 17.6308, 17.6419])\nprint(f\"\\nMain TF-IDF adaptive (tau=0.8): {main_tau08:.4f}\")\nprint(f\"GPT-2 - TF-IDF (tau=0.8): +{gpt2_adap_mean - main_tau08:.3f}\")\nprint(f\"N-gram - TF-IDF (tau=0.8): +{ngram_adap_mean - main_tau08:.3f}\")\n\n# Also check if comparing to adaptive_fix\nadap_fix = np.mean([17.6527, 17.6432, 17.6566])  # fix seed42/123/456\nprint(f\"\\nMain adaptive_fix (tau=0.8, nmin=2) mean: {adap_fix:.4f}\")\nprint(f\"GPT-2 - adaptive_fix: +{gpt2_adap_mean - adap_fix:.3f}\")\nprint(f\"N-gram - adaptive_fix: +{ngram_adap_mean - adap_fix:.3f}\")\n\n# The claimed Δ=+0.098 is for GPT-2 and Δ=+0.129 for N-gram\n# vs adaptive_fix: +0.137 and +0.170 → nope\n# vs tau=0.7: +0.118 and +0.149 → nope\n# What if it's a single-seed comparison (seed42 only)?\nprint(\"\\n--- Single seed42 comparison ---\")\ngpt2_s42 = 17.79  # gpt2_adaptive_seed42\nngram_s42 = 17.820214  # ngram_adaptive_seed42\nadap_s42_tau07 = 17.68  # tau07_seed42\nadap_s42_tau08 = 17.644  # adaptive_seed42 (tau=0.8)\nadap_fix_s42 = 17.6527\nprint(f\"GPT-2 seed42 vs tau07 seed42: +{gpt2_s42 - adap_s42_tau07:.3f}\")\nprint(f\"GPT-2 seed42 vs tau08 seed42: +{gpt2_s42 - adap_s42_tau08:.3f}\")\nprint(f\"GPT-2 seed42 vs fix seed42: +{gpt2_s42 - adap_fix_s42:.3f}\")\nprint(f\"N-gram seed42 vs tau07 seed42: +{ngram_s42 - adap_s42_tau07:.3f}\")\nprint(f\"N-gram seed42 vs tau08 seed42: +{ngram_s42 - adap_s42_tau08:.3f}\")\nprint(f\"N-gram seed42 vs fix seed42: +{ngram_s42 - adap_fix_s42:.3f}\")\nprint(f\"N-gram seed42 vs tau08 (3-seed mean): +{ngram_s42 - main_tau08:.3f}\")\n# The Δ=0.129 for ngram: ngram_s42(17.820) - fix_s42(17.6527) = +0.167; vs tau08 single = +0.176\n# Hmm let me try: Δ = GPT2 - uniform baseline (17.694)\nprint(\"\\n--- vs uniform B=4 ---\")\nunif_mean = np.mean([17.6939, 17.6861, 17.7015])\nprint(f\"GPT-2 - uniform: +{gpt2_adap_mean - unif_mean:.3f}\")\nprint(f\"N-gram - uniform: +{ngram_adap_mean - unif_mean:.3f}\")\n# vs GPT-2 uniform\ngpt2_unif = 17.69\nngram_unif = 17.69  # ngram_uniform_seed42\nprint(f\"\\nGPT-2: adaptive-uniform = {gpt2_adap_mean:.4f} - {gpt2_unif:.4f} = +{gpt2_adap_mean-gpt2_unif:.3f}\")\nprint(f\"Ngram: adaptive-uniform = {ngram_adap_mean:.4f} - {ngram_unif:.4f} = +{ngram_adap_mean-ngram_unif:.3f}\")\nprint(\"NOTE: Both detectors use same uniform baseline 17.69 (matching main uniform)\")\nprint(f\"GPT-2 Δ(adap-unif) = +{gpt2_adap_mean-gpt2_unif:.3f} vs main TF-IDF Δ=-0.020\")\nprint(f\"Ngram Δ(adap-unif) = +{ngram_adap_mean-ngram_unif:.3f} vs main TF-IDF Δ=-0.020\")\n# So relative to TF-IDF's Δ=-0.020:\n# GPT-2's Δ change = +0.102 - (-0.020) = +0.122\n# But claimed +0.098...\n# Or maybe the Δ is just the raw PPL difference from TF-IDF adaptive\n# GPT-2_adap(17.792) - TF-IDF_adap(17.674) = +0.118 (vs tau=0.7 mean)\n# Actually let me recalculate: tau07 mean = 17.6743\ndelta_gpt2_from_main = gpt2_adap_mean - main_tau07\ndelta_ngram_from_main = ngram_adap_mean - main_tau07\nprint(f\"\\nGPT-2 from main tau=0.7: +{delta_gpt2_from_main:.3f}\")\nprint(f\"Ngram from main tau=0.7: +{delta_ngram_from_main:.3f}\")\n# +0.118 and +0.149 - not matching 0.098 and 0.129\n# Difference: 0.098 = 0.118 - 0.020 (the B=4 delta)? \n# Or: tau=0.7 mean = 17.6743 but if we use 17.6944 (which is adaptive_fix mean ~ 17.652)\n# Let me try: gpt2_adap - gpt2_uniform - (main_adap - main_unif) comparison\nmain_delta = -0.01952  # B=4 adaptive-uniform\ngpt2_delta = gpt2_adap_mean - gpt2_unif\nngram_delta = ngram_adap_mean - ngram_unif\nprint(f\"\\nGPT-2 Δ(adap-unif) with GPT-2 scores: {gpt2_delta:.3f}\")\nprint(f\"N-gram Δ(adap-unif) with ngram scores: {ngram_delta:.3f}\")\nprint(f\"Main TF-IDF Δ: {main_delta:.3f}\")\n# If comparison is: GPT-2 Δ - main Δ (how much worse the detector is)\nprint(f\"GPT-2 relative degradation vs TF-IDF: {gpt2_delta - main_delta:.3f}\")\nprint(f\"Ngram relative degradation vs TF-IDF: {ngram_delta - main_delta:.3f}\")\n# gpt2_delta - main_delta = +0.102 - (-0.020) = +0.122 → not 0.098\n# Or maybe comparing with adaptive (not Δ):\n# The Δ=+0.098 and Δ=+0.129 might just be raw PPL compared to TF-IDF MAIN adaptive\n# where \"main\" = adaptive_fix 3-seed mean\nadap_fix_3seed = adap_fix\nprint(f\"\\nadaptive_fix 3-seed mean: {adap_fix_3seed:.4f}\")\nprint(f\"GPT-2 - adaptive_fix: +{gpt2_adap_mean - adap_fix_3seed:.3f}\")\nprint(f\"Ngram - adaptive_fix: +{ngram_adap_mean - adap_fix_3seed:.3f}\")\n# +0.137 and +0.170 → nope\n# Let me try: \n# the table in paper shows detector comparison where Δ = PPL(alt_detector) - PPL(TF-IDF)\n# If TF-IDF adaptive = 17.6943 (which seed42 only?), then:\n# GPT2 17.79 - 17.6943 = +0.096 ≈ 0.098 CHECK!\n# ngram 17.820 - 17.6943 = +0.126 CHECK!\nadap_fix_s42_val = 17.6527  # adaptive_fix_seed42\nprint(f\"\\nIf using adaptive_fix_seed42 = 17.6527:\")\nprint(f\"GPT-2 mean - fix_s42: +{gpt2_adap_mean - adap_fix_s42_val:.3f}\")\nprint(f\"Ngram mean - fix_s42: +{ngram_adap_mean - adap_fix_s42_val:.3f}\")\n# or tau07_seed42 = 17.68:\nprint(f\"\\nIf using tau07_seed42 = 17.68:\")\nprint(f\"GPT-2 mean - 17.68: +{gpt2_adap_mean - 17.68:.3f}\")\nprint(f\"Ngram mean - 17.68: +{ngram_adap_mean - 17.68:.3f}\")\n# +0.112 and +0.143 → nope\n\n# Try: GPT2 seed42 - adaptive B=4 tau=0.7 seed42 = 17.79-17.68=+0.11\n# N-gram seed42 - adaptive B=4 tau=0.7 seed42 = 17.82-17.68=+0.14\n# Hmm still not matching\n\n# Let me try: What if the detector comparison is mean(GPT2) - mean(uniform B=4)?\n# GPT-2 adaptive mean vs main UNIFORM\nprint(f\"\\nGPT-2 adaptive - uniform B=4 mean: +{gpt2_adap_mean - unif_mean:.3f}\")  # +0.098!\nprint(f\"Ngram adaptive - uniform B=4 mean: +{ngram_adap_mean - unif_mean:.3f}\")   # +0.129!\nprint(\"FOUND: Δ compared to UNIFORM baseline (not to TF-IDF adaptive)\")\nprint(f\"  GPT-2 adaptive(17.792) - uniform(17.694) = +{gpt2_adap_mean - unif_mean:.3f}\")\nprint(f\"  N-gram adaptive(17.823) - uniform(17.694) = +{ngram_adap_mean - unif_mean:.3f}\")\n\nPYEOF",
  "description": "Resolve detector comparison delta interpretation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6275291-42cd-4ae9-a5a0-cf354df3dfd1",
  "isSidechain": true,
  "agentId": "ab3fc5e12c4a8ae93",
  "requestId": "req_011CbLmbk7i2nAFAoke1J9AN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0044eeed-d7c9-40f7-adb9-200a74422f49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015gRHiPhBtAEa4bKjctxhug",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7763,
      "cache_read_input_tokens": 86903,
      "output_tokens": 3257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7763
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3257,
          "cache_read_input_tokens": 86903,
          "cache_creation_input_tokens": 7763,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7763,
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

_source line 33 · 2026-05-24T04:34:26.437Z_

<details><summary>↩ Tool result · `toolu_01ThJZeu599UDPpW8EUndKDD`</summary>

```text
GPT-2 adaptive mean: 17.7919
N-gram adaptive mean: 17.8231
Main TF-IDF adaptive (tau=0.7): 17.6743

GPT-2 - TF-IDF: +0.118
N-gram - TF-IDF: +0.149

Main TF-IDF adaptive (tau=0.8): 17.6389
GPT-2 - TF-IDF (tau=0.8): +0.153
N-gram - TF-IDF (tau=0.8): +0.184

Main adaptive_fix (tau=0.8, nmin=2) mean: 17.6508
GPT-2 - adaptive_fix: +0.141
N-gram - adaptive_fix: +0.172

--- Single seed42 comparison ---
GPT-2 seed42 vs tau07 seed42: +0.110
GPT-2 seed42 vs tau08 seed42: +0.146
GPT-2 seed42 vs fix seed42: +0.137
N-gram seed42 vs tau07 seed42: +0.140
N-gram seed42 vs tau08 seed42: +0.176
N-gram seed42 vs fix seed42: +0.168
N-gram seed42 vs tau08 (3-seed mean): +0.181

--- vs uniform B=4 ---
GPT-2 - uniform: +0.098
N-gram - uniform: +0.129

GPT-2: adaptive-uniform = 17.7919 - 17.6900 = +0.102
Ngram: adaptive-uniform = 17.8231 - 17.6900 = +0.133
NOTE: Both detectors use same uniform baseline 17.69 (matching main uniform)
GPT-2 Δ(adap-unif) = +0.102 vs main TF-IDF Δ=-0.020
Ngram Δ(adap-unif) = +0.133 vs main TF-IDF Δ=-0.020

GPT-2 from main tau=0.7: +0.118
Ngram from main tau=0.7: +0.149

GPT-2 Δ(adap-unif) with GPT-2 scores: 0.102
N-gram Δ(adap-unif) with ngram scores: 0.133
Main TF-IDF Δ: -0.020
GPT-2 relative degradation vs TF-IDF: 0.121
Ngram relative degradation vs TF-IDF: 0.153

adaptive_fix 3-seed mean: 17.6508
GPT-2 - adaptive_fix: +0.141
Ngram - adaptive_fix: +0.172

If using adaptive_fix_seed42 = 17.6527:
GPT-2 mean - fix_s42: +0.139
Ngram mean - fix_s42: +0.170

If using tau07_seed42 = 17.68:
GPT-2 mean - 17.68: +0.112
Ngram mean - 17.68: +0.143

GPT-2 adaptive - uniform B=4 mean: +0.098
Ngram adaptive - uniform B=4 mean: +0.129
FOUND: Δ compared to UNIFORM baseline (not to TF-IDF adaptive)
  GPT-2 adaptive(17.792) - uniform(17.694) = +0.098
  N-gram adaptive(17.823) - uniform(17.694) = +0.129
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0044eeed-d7c9-40f7-adb9-200a74422f49",
  "isSidechain": true,
  "promptId": "792d4fc7-1d48-4678-830d-80fd5a58c95b",
  "agentId": "ab3fc5e12c4a8ae93",
  "type": "user",
  "uuid": "91b285ce-734c-47e0-97b2-8d17d5825709",
  "sourceToolAssistantUUID": "0044eeed-d7c9-40f7-adb9-200a74422f49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-24T04:34:30.038Z_

Now let me also check the Llama-3B MMLU claim and downstream accuracy 0.5414:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91b285ce-734c-47e0-97b2-8d17d5825709",
  "isSidechain": true,
  "agentId": "ab3fc5e12c4a8ae93",
  "requestId": "req_011CbLmeucnxeYGvy9NVnQzC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d94949bc-145f-4f97-baf3-4a4f8743d0fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UZ8qwFxdriQRDvHfhyN1QH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4162,
      "cache_read_input_tokens": 94666,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4162,
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

_source line 35 · 2026-05-24T04:34:52.887Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01U1rZYSuaGp9LbJkTyMdHb8`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport numpy as np\nimport json\n\nFILE = \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c/tool-results/mcp-agent-ml-research-read_registry-1779596944442.txt\"\n\nwith open(FILE) as f:\n    outer = json.load(f)\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Check all experiments containing MMLU data\nprint(\"=== Searching for MMLU data across all experiments ===\")\nfor k, e in experiments.items():\n    m = e.get('metrics', {})\n    if m and isinstance(m, dict):\n        for key in m:\n            if 'mmlu' in key.lower():\n                print(f\"  [{k}] {key}={m[key]}\")\n\n# Check Llama3B more carefully\nprint(\"\\n=== Llama3B full metrics ===\")\nfor k in ['llama3b_adaptive_seed42', 'llama3b_uniform_seed42']:\n    e = experiments[k]\n    print(f\"  [{k}]\")\n    print(f\"    metrics: {e.get('metrics')}\")\n    print(f\"    hypothesis: {e.get('hypothesis', '')[:400]}\")\n    print(f\"    conclusion: {e.get('conclusion')}\")\n\n# Check downstream accuracy 0.5414 - tau07 3-seed mean\nprint(\"\\n=== Downstream accuracy tau07 3-seed ===\")\ntau07_s42 = [0.6166, 0.3473, 0.4795, 0.6861, 0.5817]\ntau07_s123 = [0.6309, 0.3481, 0.4775, 0.6866, 0.5675]\ntau07_s456 = [0.6111, 0.3515, 0.4811, 0.6834, 0.5722]\nmeans = [np.mean(tau07_s42), np.mean(tau07_s123), np.mean(tau07_s456)]\nprint(f\"  seed42 mean: {means[0]:.4f}\")\nprint(f\"  seed123 mean: {means[1]:.4f}\")\nprint(f\"  seed456 mean: {means[2]:.4f}\")\nprint(f\"  Overall mean: {np.mean(means):.4f}\")\n\n# Check uniform downstream\nunif_s42 = [0.6128, 0.3481, 0.4836, 0.6877, 0.5856]\nunif_s123 = [0.6229, 0.3507, 0.4797, 0.685, 0.5762]\nunif_s456 = [0.6166, 0.3439, 0.4826, 0.6795, 0.5667]\nunif_means = [np.mean(unif_s42), np.mean(unif_s123), np.mean(unif_s456)]\nprint(f\"\\n=== Uniform downstream 3-seed ===\")\nprint(f\"  seed42 mean: {unif_means[0]:.4f}\")\nprint(f\"  seed123 mean: {unif_means[1]:.4f}\")\nprint(f\"  seed456 mean: {unif_means[2]:.4f}\")\nprint(f\"  Overall mean: {np.mean(unif_means):.4f}\")\nprint(f\"  Δ(adaptive tau07 - uniform): {np.mean(means) - np.mean(unif_means):.4f}\")\n\n# The 0.5414 claimed\nprint(f\"\\n  tau07 3-seed mean = {np.mean(means):.4f} → claimed 0.5414 = MATCH\")\nprint(f\"  uniform 3-seed mean = {np.mean(unif_means):.4f}\")\n\n# Also check if downstream 0.5414 is the adaptive mean\nprint(f\"\\n  Also check: adaptive_rho06_tau07 seeds downstream\")\nrho06_s42 = [0.6132, 0.3422, 0.4807, 0.6861, 0.5793]\nrho06_s123 = [0.5951, 0.3422, 0.4811, 0.6866, 0.5754]\nrho06_s456 = [0.6128, 0.3456, 0.4806, 0.6866, 0.5620]\nrho06_means = [np.mean(rho06_s42), np.mean(rho06_s123), np.mean(rho06_s456)]\nprint(f\"  rho06 tau07 seed42 mean: {rho06_means[0]:.4f}\")\nprint(f\"  rho06 tau07 seed123 mean: {rho06_means[1]:.4f}\")\nprint(f\"  rho06 tau07 seed456 mean: {rho06_means[2]:.4f}\")\nprint(f\"  rho06 overall mean: {np.mean(rho06_means):.4f}\")\n\n# Final summary for 1.7B scale\nprint(\"\\n=== 1.7B SCALE DOWNSTREAM ===\")\nadap_17b_s42 = experiments['adaptive_1_7b_seed42_v5']['metrics']\nadap_17b_s123 = experiments['adaptive_1_7b_seed123']['metrics']\nadap_17b_s456 = experiments['adaptive_1_7b_seed456']['metrics']\nunif_17b_s42 = experiments['uniform_1_7b_seed42_v5']['metrics']\nunif_17b_s123 = experiments['uniform_1_7b_seed123']['metrics']\nunif_17b_s456 = experiments['uniform_1_7b_seed456']['metrics']\n\nadap_17b_ds = [adap_17b_s42['downstream_mean'], adap_17b_s123['downstream_mean'], adap_17b_s456['downstream_mean']]\nunif_17b_ds = [unif_17b_s42['downstream_mean'], unif_17b_s123['downstream_mean'], unif_17b_s456['downstream_mean']]\nprint(f\"  Adaptive 1.7B downstream means: {adap_17b_ds} → overall: {np.mean(adap_17b_ds):.4f}\")\nprint(f\"  Uniform 1.7B downstream means: {unif_17b_ds} → overall: {np.mean(unif_17b_ds):.4f}\")\nprint(f\"  Δ: {np.mean(adap_17b_ds) - np.mean(unif_17b_ds):.4f}\")\n\nPYEOF",
  "description": "Check MMLU data and downstream accuracy 0.5414"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d94949bc-145f-4f97-baf3-4a4f8743d0fc",
  "isSidechain": true,
  "agentId": "ab3fc5e12c4a8ae93",
  "requestId": "req_011CbLmeucnxeYGvy9NVnQzC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ed16b03-aa51-4c3f-897e-5672c2dac2dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UZ8qwFxdriQRDvHfhyN1QH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4162,
      "cache_read_input_tokens": 94666,
      "output_tokens": 1870,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4162
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1870,
          "cache_read_input_tokens": 94666,
          "cache_creation_input_tokens": 4162,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4162,
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

_source line 36 · 2026-05-24T04:34:53.122Z_

<details><summary>↩ Tool result · `toolu_01U1rZYSuaGp9LbJkTyMdHb8`</summary>

```text
=== Searching for MMLU data across all experiments ===

=== Llama3B full metrics ===
  [llama3b_adaptive_seed42]
    metrics: {'ppl': 10.58, 'eval_loss': 2.359, 'eval_tokens': 4017316}
    hypothesis: Adaptive b* generalizes across model architectures: Llama-3.2-3B with provenance-weighted training should show PPL improvement over uniform baseline proportional to Qwen3-0.6B results, confirming the method is not architecture-specific and dual-constraint b* transfers.
    conclusion: negative
  [llama3b_uniform_seed42]
    metrics: {'ppl': 10.38, 'eval_loss': 2.3397, 'eval_tokens': 1526195, 'train_loss': 7.2987, 'train_steps': 6103, 'train_runtime_seconds': 94309}
    hypothesis: Uniform weighting baseline on Llama-3.2-3B establishes reference PPL for cross-model generalization experiment, enabling fair comparison with adaptive weighting on the same architecture and data.
    conclusion: success

=== Downstream accuracy tau07 3-seed ===
  seed42 mean: 0.5422
  seed123 mean: 0.5421
  seed456 mean: 0.5399
  Overall mean: 0.5414

=== Uniform downstream 3-seed ===
  seed42 mean: 0.5436
  seed123 mean: 0.5429
  seed456 mean: 0.5379
  Overall mean: 0.5414
  Δ(adaptive tau07 - uniform): -0.0000

  tau07 3-seed mean = 0.5414 → claimed 0.5414 = MATCH
  uniform 3-seed mean = 0.5414

  Also check: adaptive_rho06_tau07 seeds downstream
  rho06 tau07 seed42 mean: 0.5403
  rho06 tau07 seed123 mean: 0.5361
  rho06 tau07 seed456 mean: 0.5375
  rho06 overall mean: 0.5380

=== 1.7B SCALE DOWNSTREAM ===
  Adaptive 1.7B downstream means: [0.6251, 0.6286, 0.6259] → overall: 0.6265
  Uniform 1.7B downstream means: [0.6256, 0.6256, 0.6234] → overall: 0.6249
  Δ: 0.0017
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ed16b03-aa51-4c3f-897e-5672c2dac2dd",
  "isSidechain": true,
  "promptId": "792d4fc7-1d48-4678-830d-80fd5a58c95b",
  "agentId": "ab3fc5e12c4a8ae93",
  "type": "user",
  "uuid": "8b735d2b-b60a-44b5-ac43-8de212c78fc0",
  "sourceToolAssistantUUID": "1ed16b03-aa51-4c3f-897e-5672c2dac2dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-24T04:35:48.041Z_

I now have a complete picture of all 256 experiments. Here is the comprehensive mapping:

---

## Registry Extraction: Complete Experiment → Metrics Mapping

**Total experiments: 256** (DONE, PREPARING, failed, killed)

---

### MAIN RESULTS: B=4, ρ=0.4

**Adaptive τ=0.7, 3-seed** (`tau07_seed42/123/456`):
- seed42: holdout_ppl = **17.680**, seed123: **17.666**, seed456: **17.677**
- **3-seed mean = 17.674 ± 0.007** (±std) — MATCHES claimed #1

**Uniform B=4** (`uniform_seed42/123/456`):
- seed42: 17.6939, seed123: 17.6861, seed456: 17.7015
- **3-seed mean = 17.694 ± 0.008** — MATCHES claimed #2

**Δ(B=4, ρ=0.4)**: paired deltas = [−0.014, −0.020, −0.025], mean = **−0.020**, delta-std = 0.005 (not 0.008)
- Note: the ±0.008 in "#3: Δ=−0.020±0.008" appears to be the std of the uniform series, not the paired-delta std. Paired delta std = 0.005, SEM = 0.003.

**Adaptive τ=0.8, 3-seed** (`adaptive_seed42/123/456`):
- seed42: 17.644, seed123: 17.6308, seed456: 17.6419 → mean = 17.639 ± 0.007

---

### B=8, ρ=0.4

**Adaptive** (`bs8_nmin4_adaptive_seed42` + `_seed123_r2` + `_seed456_r2`):
- 17.650, 17.631, 17.646 → mean = 17.642, std = 0.010

**Uniform** (`bs8_nmin4_uniform_seed42` + `_seed123_r2` + `_seed456_r2`):
- 17.694, 17.687, 17.702 → mean = 17.694, std = 0.008

**Δ(B=8)**: [−0.044, −0.056, −0.056] → **mean = −0.052 ± 0.007** — MATCHES claimed #4

---

### B=16, ρ=0.4

**Adaptive** (`bs16_adaptive_tau07_seed42` + `_seed123_r2` + `_seed456`):
- 17.631, 17.616, 17.645 → mean = 17.631, std = 0.015

**Uniform** (`bs16_uniform_seed42/123/456`):
- 17.694, 17.686, 17.717 → mean = 17.699, std = 0.016

**Δ(B=16)**: [−0.063, −0.070, −0.072] → **mean = −0.068 ± 0.005** — MATCHES claimed #5

---

### ρ=0.6 (τ=0.7, from-scratch, `adaptive_rho06_tau07_seed*`)

**Adaptive**: seed42=17.735, seed123=17.727, seed456=17.732 → **mean=17.731 ± 0.004** — MATCHES #6
**Uniform** (`contamination_60_uniform_seed42/123/456`): 17.766, 17.754, 17.770 → **mean=17.763 ± 0.008** — MATCHES #6
**Δ = −0.032** (paired: [−0.031, −0.027, −0.038]) — MATCHES #6

---

### ρ=0.3

**Adaptive** (`rho03_adaptive_seed42/123/456_r2`): 17.422, 17.435, 17.424
**Uniform** (`rho03_uniform_seed42/123/456`): 17.422, 17.433, 17.419
**Δ = +0.002** (mean of [0.000, +0.002, +0.005]) — MATCHES #7

---

### ρ=0.2

- `rho02_adaptive_tau08_seed42`: PPL=**17.382** vs `rho02_uniform_seed42`: **17.336** → **Δ=+0.046** — MATCHES #8
- `rho02_adaptive_tau09_r5`: PPL=17.450 → Δ=+0.114

---

### α_eff-only (n_min=1)

`aeff_only_nmin1_seed42/123/456`: 17.750, 17.733, 17.744 → **mean=17.742 ± 0.009** — MATCHES #9

---

### ESS-only

`ess_only_seed42/123/456` (using r2 for 123 and 456): 17.730, 17.721, 17.762 → **mean=17.738** ≈ 17.737
Using original seeds: 17.730, 17.720, 17.760 → **mean=17.737** — MATCHES #10

---

### 1.7B Scale

**Adaptive** (`adaptive_1_7b_seed42_v5/seed123/seed456`): 13.27, 13.25, 13.2668 → **mean=13.262 → rounds to 13.26**
**Uniform** (`uniform_1_7b_seed42_v5/seed123/seed456`): 13.28, 13.2648, 13.28 → **mean=13.275 → rounds to 13.27 or 13.28**
- **13.26 adaptive vs 13.27 uniform** — MATCHES claimed #20
- `eval_adaptive_1_7b_v2` = 13.27 (single seed42), `eval_uniform_1_7b_v3` = 13.50 (older checkpoint) — explains why #11 says "adaptive 13.27, uniform 13.50" from early single-seed runs; superseded by 3-seed results

**Downstream 1.7B**: adaptive 3-seed mean = 0.6265, uniform = 0.6249, Δ=+0.0017 (negligible)

---

### Llama-3.2-3B Cross-Model (`llama3b_*_seed42`)

- `llama3b_adaptive_seed42`: PPL=**10.58**, conclusion=**negative**
- `llama3b_uniform_seed42`: PPL=**10.38**
- Adaptive is **WORSE** by 0.20 PPL on Llama-3B
- **No MMLU data anywhere in the registry** — the "+1.57pp MMLU" claim (#12) is not traceable from registry metrics (likely in external eval logs not in registry)

---

### Detector Comparison

**Key insight**: Δ values are computed as `PPL(alt_detector_adaptive) − PPL(uniform_B4_mean)`, where uniform mean = 17.694.

- `gpt2_adaptive_seed42/123_v3/456_v2`: 17.790, 17.788, 17.797 → mean = **17.792**
  - **Δ(GPT-2) = 17.792 − 17.694 = +0.098** — MATCHES #13
- `ngram_adaptive_seed42/123/456_v2`: 17.820, 17.823, 17.826 → mean = **17.823**
  - **Δ(N-gram) = 17.823 − 17.694 = +0.129** — MATCHES #14
- `gpt2_uniform_seed42` = 17.690, `ngram_uniform_seed42` = 17.690

So detector comparison Δ = how much worse the weaker detector is vs uniform (main TF-IDF adaptive achieves −0.020 vs uniform, while GPT-2/N-gram achieve +0.098/+0.129 vs that same uniform — meaning they're worse than doing nothing).

---

### D&R q>0.3, 3-seed

`detect_remove_q03_seed42_r2/seed123/seed456`: 17.250, 17.250, 17.251 → **mean=17.250 ± 0.001** — MATCHES #15

---

### D&R Epoch-matched

`dr_epoch_matched_indep_lr_v2_seed42` + `dr_epoch_matched_seed123_r2` + `epoch_matched_dr_seed456`:
- 17.651, 17.659, 17.660 → **mean=17.657 ± 0.005** — MATCHES #16

---

### Permuted-score Control

`random_reweight_baseline_seed42` + `random_reweight_seed123` + `random_reweight_v2_seed456`:
- 17.958, 17.945, 17.951 → **mean=17.951 ± 0.007** — MATCHES #17

---

### Grid b=0.3, 3-seed

`grid_b0_3_seed42` + `grid_b0_3_seed123_r2` + `grid_b0_3_seed456_r2`:
- 17.640, 17.579, 17.640 → **mean=17.620 ± 0.033** — MATCHES #18

---

### Random U(0,2), 3-seed

`random_reweight_v2_seed42` + `random_reweight_seed123_r5` + `random_reweight_seed456`:
- 17.830, 17.800, 17.777 → **mean=17.802 ± 0.027** — MATCHES #19

---

### Downstream Accuracy 0.5414

`tau07_seed42/123/456` downstream means: 0.5422, 0.5421, 0.5399 → **grand mean = 0.5414** — MATCHES #20
Notably, **uniform 3-seed downstream** (`uniform_ood_seed123/456` + `qwen06b_uniform_seed42`) also = **0.5414** (coincident tie).

---

### Additional notable experiments

**D&R full sweep** (9-point, seed42 only):
- q01: 17.400, q02: 17.270, q03: 17.250, q04: 17.260, q05: 17.285, q06: 17.299, q07: 17.320, q08: 17.344, q09: 17.420
- Epoch-matched at q05: 17.650 (confirms multi-epoch is the source of D&R's apparent advantage)

**Hybrid filter+reweight**: ρ=0.4 seed42 PPL=17.514; ρ=0.6 seed42 PPL=17.526

**Baseline Qwen3-0.6B** (no training): PPL=22.97

**Grid b sweep** (seed42 batch): b=0.5→17.651, b=1.0→17.692, b=1.5→17.718, b=2.0→17.741, b=3.0→17.774, b=5.0→17.818 (best-b=0.5)

**Grid b=0.2/0.1 (3-seed)**: b=0.2 seeds = 17.640/17.637/17.645, b=0.1 seeds = 17.657/17.646/17.663 (slightly above b=0.2/0.3 optimum)

**τ sensitivity sweep** (seed42, τ=0.8 is main): τ=0.5→17.688, τ=0.6→17.681, τ=0.7→17.679, τ=0.9→17.712, τ=0.95→17.723

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b735d2b-b60a-44b5-ac43-8de212c78fc0",
  "isSidechain": true,
  "agentId": "ab3fc5e12c4a8ae93",
  "requestId": "req_011CbLmgsiFnNPRedKAsjV5k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b1154f71-5ccf-42df-a763-2a3d5e3f8d6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "f533e7f3-1a76-44f6-8f47-2a11d2d6ff8c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QSqdf4hLmqJQHwiyKEXLwd",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2530,
      "cache_read_input_tokens": 98828,
      "output_tokens": 3074,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2530
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3074,
          "cache_read_input_tokens": 98828,
          "cache_creation_input_tokens": 2530,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2530,
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
