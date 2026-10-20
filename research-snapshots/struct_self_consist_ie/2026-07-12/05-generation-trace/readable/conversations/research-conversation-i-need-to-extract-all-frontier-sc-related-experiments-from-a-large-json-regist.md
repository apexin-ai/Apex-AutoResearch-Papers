# Research conversation: I need to extract all frontier SC related experiments from a large JSON registry file. The file is at: /home/ubuntu/.cla

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-aa904c9d54f8cf8d3.jsonl`
- **Structured JSON:** [`076a376f394b8a5c9ab3.json`](../../sessions/07/076a376f394b8a5c9ab3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

13 recorded events

### User

_source line 1 · 2026-05-21T11:33:07.715Z_

I need to extract all frontier SC related experiments from a large JSON registry file. 

The file is at: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/b0548841-9ada-435d-86ea-ff41c7017560/tool-results/mcp-agent-ml-research-read_registry-1779363177682.txt

This file is JSON with schema: {result: string} where result is a JSON string containing experiment data.

Steps:
1. Probe the structure with jq (type/length/keys)
2. Extract the inner JSON and find ALL experiments whose exp_id contains "frontier" (case insensitive)
3. For each matching experiment, extract: exp_id, status, conclusion, metrics (full), and any other relevant fields like config/notes
4. Also search for any experiments with "ensemble" or "cross" in the exp_id

Report the full details of every matching experiment verbatim - don't summarize the metrics, give me exact numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "231b764b-2b39-49a0-b546-ab3bf4d9355b",
  "agentId": "aa904c9d54f8cf8d3",
  "type": "user",
  "uuid": "a6700ebe-5a8c-4fb1-86c2-93e7e860b4d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b0548841-9ada-435d-86ea-ff41c7017560",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T11:33:07.718Z_

```json
{
  "parentUuid": "a6700ebe-5a8c-4fb1-86c2-93e7e860b4d7",
  "isSidechain": true,
  "agentId": "aa904c9d54f8cf8d3",
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
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
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
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__update_registry"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "1e42841c-137b-4b1b-b8c1-ce80dbf7d8d3",
  "timestamp": "2026-05-21T11:33:07.718Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b0548841-9ada-435d-86ea-ff41c7017560",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-21T11:33:11.434Z_



Let me start by probing the file structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e42841c-137b-4b1b-b8c1-ce80dbf7d8d3",
  "isSidechain": true,
  "agentId": "aa904c9d54f8cf8d3",
  "requestId": "req_011CbFe9xZWNSSh3FUnyXtUV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e73db8f-89dd-4d41-a1ed-00543322d0f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b0548841-9ada-435d-86ea-ff41c7017560",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012u139EHziowhetA3W46i4M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6680,
      "cache_read_input_tokens": 8251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6680,
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

_source line 4 · 2026-05-21T11:33:12.916Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Kq5nDmqHmJnXfhBeUedTjD`</summary>

```json
{
  "command": "wc -c /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/b0548841-9ada-435d-86ea-ff41c7017560/tool-results/mcp-agent-ml-research-read_registry-1779363177682.txt",
  "description": "Check file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e73db8f-89dd-4d41-a1ed-00543322d0f5",
  "isSidechain": true,
  "agentId": "aa904c9d54f8cf8d3",
  "requestId": "req_011CbFe9xZWNSSh3FUnyXtUV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf216303-f98c-43a9-b64c-dc3719293f8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b0548841-9ada-435d-86ea-ff41c7017560",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012u139EHziowhetA3W46i4M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6680,
      "cache_read_input_tokens": 8251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6680,
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

### Tool result

_source line 5 · 2026-05-21T11:33:13.099Z_

<details><summary>↩ Tool result · `toolu_01Kq5nDmqHmJnXfhBeUedTjD`</summary>

```text
129147 /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/b0548841-9ada-435d-86ea-ff41c7017560/tool-results/mcp-agent-ml-research-read_registry-1779363177682.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf216303-f98c-43a9-b64c-dc3719293f8d",
  "isSidechain": true,
  "promptId": "231b764b-2b39-49a0-b546-ab3bf4d9355b",
  "agentId": "aa904c9d54f8cf8d3",
  "type": "user",
  "uuid": "182df242-e143-43ea-85f6-5d45f6f6bf5b",
  "sourceToolAssistantUUID": "cf216303-f98c-43a9-b64c-dc3719293f8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b0548841-9ada-435d-86ea-ff41c7017560",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T11:33:16.267Z_

<details open><summary>🔧 Tool call — Bash · `toolu_019abwChNnWipVnUSVz5vUqD`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/b0548841-9ada-435d-86ea-ff41c7017560/tool-results/mcp-agent-ml-research-read_registry-1779363177682.txt') as f:\n    outer = json.load(f)\nprint('Outer keys:', list(outer.keys()))\nprint('Type of result:', type(outer.get('result')))\ninner = json.loads(outer['result']) if isinstance(outer.get('result'), str) else outer.get('result')\nprint('Inner type:', type(inner))\nif isinstance(inner, dict):\n    print('Inner keys:', list(inner.keys())[:20])\n    print('Total keys:', len(inner.keys()))\nelif isinstance(inner, list):\n    print('Inner length:', len(inner))\n    if len(inner) > 0:\n        print('First item type:', type(inner[0]))\n        if isinstance(inner[0], dict):\n            print('First item keys:', list(inner[0].keys()))\n\" 2>&1",
  "description": "Probe JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "182df242-e143-43ea-85f6-5d45f6f6bf5b",
  "isSidechain": true,
  "agentId": "aa904c9d54f8cf8d3",
  "requestId": "req_011CbFe9xZWNSSh3FUnyXtUV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aeaa70d4-8aeb-456a-a33e-5ca55c556edc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b0548841-9ada-435d-86ea-ff41c7017560",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012u139EHziowhetA3W46i4M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6680,
      "cache_read_input_tokens": 8251,
      "output_tokens": 522,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6680
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 522,
          "cache_read_input_tokens": 8251,
          "cache_creation_input_tokens": 6680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6680,
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

_source line 7 · 2026-05-21T11:33:16.374Z_

<details><summary>↩ Tool result · `toolu_019abwChNnWipVnUSVz5vUqD`</summary>

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
  "parentUuid": "aeaa70d4-8aeb-456a-a33e-5ca55c556edc",
  "isSidechain": true,
  "promptId": "231b764b-2b39-49a0-b546-ab3bf4d9355b",
  "agentId": "aa904c9d54f8cf8d3",
  "type": "user",
  "uuid": "e00ffa74-54fa-4c2d-a8fd-09445cf9a196",
  "sourceToolAssistantUUID": "aeaa70d4-8aeb-456a-a33e-5ca55c556edc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b0548841-9ada-435d-86ea-ff41c7017560",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T11:33:22.756Z_

<details open><summary>🔧 Tool call — Bash · `toolu_015fbRZAh6VkwnsdWuSNbUjY`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/b0548841-9ada-435d-86ea-ff41c7017560/tool-results/mcp-agent-ml-research-read_registry-1779363177682.txt') as f:\n    outer = json.load(f)\ninner = json.loads(outer['result'])\nprint('success:', inner.get('success'))\nprint('error:', inner.get('error'))\nprint('metadata:', json.dumps(inner.get('metadata'), indent=2) if inner.get('metadata') else None)\ndata = inner.get('data')\nprint('data type:', type(data))\nif isinstance(data, dict):\n    print('data keys:', list(data.keys())[:30])\n    print('total data keys:', len(data.keys()))\n    # Check first entry\n    first_key = list(data.keys())[0]\n    print('First key:', first_key)\n    print('First value type:', type(data[first_key]))\n    if isinstance(data[first_key], dict):\n        print('First value keys:', list(data[first_key].keys()))\nelif isinstance(data, list):\n    print('data length:', len(data))\n\" 2>&1",
  "description": "Explore inner JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e00ffa74-54fa-4c2d-a8fd-09445cf9a196",
  "isSidechain": true,
  "agentId": "aa904c9d54f8cf8d3",
  "requestId": "req_011CbFeAbci3zvVsUzLL2RGt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a1502e6-d59a-4e08-83ed-f7a6f9a8acf0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b0548841-9ada-435d-86ea-ff41c7017560",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R3CcRAfkQNdEMaPzMhipBy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1566,
      "cache_read_input_tokens": 14931,
      "output_tokens": 408,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1566
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 408,
          "cache_read_input_tokens": 14931,
          "cache_creation_input_tokens": 1566,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1566,
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

_source line 9 · 2026-05-21T11:33:22.986Z_

<details><summary>↩ Tool result · `toolu_015fbRZAh6VkwnsdWuSNbUjY`</summary>

```text
success: True
error: None
metadata: {
  "elapsed_seconds": 0.765
}
data type: &lt;class 'dict'>
data keys: ['experiments', 'count', 'total', 'baseline']
total data keys: 4
First key: experiments
First value type: &lt;class 'dict'>
First value keys: ['exp_fewnerd_n16_s456_v2', 'exp_conll_n16_s42', 'exp_fewnerd_n16_s123', 'exp_fewnerd_n16_s42_v2', 'exp_scierc_n16_s123', 'exp_14b_inference_conll_v2', 'exp_conll_mf4_v2_s42', 'exp_frontier_sc_gemini25pro', 'exp_e2_pretrained_scierc', 'exp_e2_pretrained_conll', 'exp_scierc_mf4_v2_s42', 'exp_fewnerd_mf4v2_s123', 'exp_fewnerd_mf4v2_s42', 'exp_e2_pretrained_fewnerd_s123', 'exp_fewnerd_mf4v2_s456', 'exp_scierc_mf4_v2_s456', 'exp_scierc_mf4_v2_s123', 'exp_b1_scd', 'exp_fewnerd_mf4_v2_s456', 'exp_conll_mf4_v2_s456', 'exp_conll_mf4_v2_s123', 'exp_frontier_sc_deepseek', 'exp_conll_n16_s456_v2', 'exp_conll_n16_s123_v2', 'exp_frontier_sc_claude_sonnet4', 'exp_frontier_sc_gpt55_fewnerd_v2', 'exp_fewnerd_n16_s42', 'exp_fewnerd_t12_s456', 'exp_14b_inference_fewnerd', 'exp_fewnerd_mf4_v2_s42', 'exp_fewnerd_mf4_v2_s123', 'exp_fewnerd_7b_n16_s42', 'exp_fewnerd_n16_s456', 'exp_e2_pretrained_fewnerd', 'exp_conll_mf4_s456', 'exp_conll_mf4_s123', 'exp_fewnerd_t05_s456', 'exp_fewnerd_mf4_s456', 'exp_fewnerd_mf4_s123', 'exp_fewnerd_mf4_s42', 'exp_14b_inference_conll', 'exp_conll_n16_s456', 'exp_conll_n16_s123', 'exp_scierc_n16_s456', 'exp_scierc_t12_s456', 'exp_scierc_t08_s123', 'exp_scierc_t08_s456', 'exp_scierc_t05_s456', 'exp_scierc_t12_s123', 'exp_scierc_t05_s123', 'exp_fewnerd_t08_s456', 'exp_fewnerd_t12_s123', 'exp_fewnerd_t08_s123', 'exp_fewnerd_t05_s123', 'exp_32b_inference_fewnerd', 'exp_hidden_state_probe_fulldata', 'exp_hidden_state_probe', 'exp_conll_t10_s42', 'exp_scierc_probe', 'exp_multi_model_correlation', 'exp_conll_t12_s456', 'exp_conll_t08_s456', 'exp_conll_t05_s456', 'exp_fewnerd_t05_s42', 'exp_fewnerd_t08_s42', 'exp_fewnerd_t12_s42', 'exp_conll_t12_s123', 'exp_conll_t08_s123', 'exp_conll_t05_s123', 'exp_qwen25_32b_fewnerd', 'exp_conll_t_ablation_t12', 'exp_conll_t_ablation_t08', 'exp_conll_t_ablation_t05', 'exp_conll_t05_s42', 'exp_spider_sc_pilot', 'exp_fewrel_re_sc', 'exp_a2_humaneval_sc', 'exp_b_frontier_sc_fewnerd', 'exp_docred_re_sc', 'exp_a3_ace05_re', 'eval_scd_fewnerd_fallback', 'exp_b1_scd_fewnerd_curriculum_q', 'exp_b1_scd_fewnerd_standard', 'exp_b1_scd_threshold_ablation', 'exp_tlow_fewnerd_inference', 'exp_asb_adaptive_budget', 'exp_e_theta_adaptive', 'exp_cross_model_consistency', 'exp_backup3_distill_verifier', 'exp_backup1_het_temp', 'exp_a1_spider_sql_sc', 'exp_esj_entity_self_judgment', 'exp_b3_prompted_diversity', 'exp_mrsc_multi_round', 'exp_lsc_latent_sc', 'exp_14b_inference_scierc', 'exp_qwen25_14b_fewnerd', 'exp_b1_scd_conll_control', 'exp_b2_v4_inverse_frequency', 'exp_b2_v3_domain_invariant', 'exp_b2_v2_multi_domain_joint', 'exp_b2_entity_verifier', 'exp_a2_degen_regression', 'exp_e1_signal_routing', 'exp_pareto_diversity_quality', 'exp_adaptive_sampling_budget', 'exp_dgec_sj_construction', 'exp_dgec_vc_construction', 'exp_dgec_heterogeneous_t', 'exp_qwen25_7b_fewnerd', 'exp_qwen25_72b_fewshot', 'exp_qwen25_72b_zeroshot', 'exp_wnut17_qwen25_7b', 'exp_llama_fewnerd_inference', 'exp_entity_construction', 'exp_lp_alignment_gating', 'exp_selective_prediction', 'exp_llama_fewnerd_lora', 'hidden_state_probe_conll_full', 'hidden_state_probe_conll_v2', 'exp_031_fewnerd_t12', 'exp_030_conll_t12', 'mbr_pilot', 'dgs_pilot', 'exp_fewnerd_s789_n8', 'exp_026_t12_seed456', 'exp_026_t12_seed123', 'exp_026_t10_seed456', 'exp_026_t10_seed123', 'exp_026_t10_seed42', 'exp_026_t08_seed456', 'exp_026_t08_seed123', 'exp_026_t05_seed456', 'exp_026_t05_seed123', 'exp_029b', 'exp_029a', 'exp_021_fewnerd_n8_seed456', 'exp_021_fewnerd_n8_seed123', 'exp_002_conll_n16_seed456', 'exp_002_conll_n16_seed123', 'exp_017_llama_conll_n16_s456_r1024', 'exp_017_llama_conll_n16_r1024', 'exp_018_llama_scierc_seed456_r1024', 'exp_018_llama_scierc_seed42_r1024', 'exp_002_conll_n16', 'exp_012_rerun_1024', 'exp_llama_scierc_seed456', 'exp_007_llama_scierc_seed123', 'exp_qwen3_4b_conll_scs_inference', 'exp_qwen3_4b_conll_scs_inference_v2', 'exp_qwen3_4b_scierc_scs_inference', 'exp_027_fewnerd_n16', 'exp_026_t12', 'exp_026_t08', 'exp_026_t05', 'exp_026_T12', 'exp_026_T08', 'exp_026_T05', 'exp_017_llama_conll_n16_s123_r1024', 'exp_018_llama_scierc_seed123', 'exp_018_qwen_scierc_seed456', 'exp_018_qwen_scierc_seed123', 'exp_epoch_dgs_analysis', 'exp_diagnostic_calibration', 'exp_adaptive_temperature', 'exp_entity_consensus', 'exp_ccs_selection', 'exp_017_llama_conll', 'exp_017_llama_conll_finetune', 'exp_028_entity_token_lp', 'exp_026_t12_scierc', 'exp_026_t08_scierc', 'exp_026_t05_scierc', 'exp_027_mlp_verifier', 'exp_028_fewnerd_5epoch', 'exp_028', 'exp_024_claim_audit', 'exp_016_rerun_1024_bootstrap', 'exp_verbalized_confidence', 'exp_entity_token_lp', 'exp_freeform_ablation', 'exp_008_re_n16', 'exp_001_ner_n16_seed123', 'exp_007_ner_multi_model', 'exp_003_ner_wnut17', 'exp_001_seed456_t10_full', 'exp_001_seed123_t10_full', 'exp_008_re_n16_t10_full', 'exp_007_llama_inference', 'exp_003_wnut17_eval', 'exp_010_selection_curves', 'exp_007_llama_seed456', 'exp_007_llama_seed123', 'exp_008_re_seed123', 'exp_001_seed42_v2', 'exp_001_seed123_v2', 'exp_008_re_n16_v2', 'exp_005_v2', 'exp_006_v2', 'exp_004_v2', 'exp_009_v2', 'exp_016_v2', 'exp_001_seed456_v2', 'exp_017_llama_conll_infer', 'exp_003_wnut17_v2', 'exp_001_seed456_v2_ner', 'exp_009_v2_re_rerun', 'exp_007_llama_n16', 'exp_017_llama_conll_n16', 'exp_015_v2', 'exp_001_n16_seed456', 'exp_011_ood_scierc_to_conll', 'exp_qwen3_4b_scierc_finetune_v4', 'exp_011_ood_conll_to_scierc', 'exp_freeform_seed789_v3', 'exp_freeform_seed789', 'exp_freeform_seed456', 'exp_freeform_seed123', 'exp_009_capability_stratification', 'exp_023_lora_rank8', 'exp_022_seed789', 'exp_025_n32', 'exp_021_fewnerd_full', 'exp_015_metrics_expansion', 'exp_020_fewnerd_smoke', 'exp_vc_lp_cascade_selection', 'exp_tacred_re_benchmark', 'exp_vc_quartile_analysis', 'exp_llama3b_scierc_ablation', 'exp_freeform_conll_4seed', 'exp_qwen3_4b_conll_merge_inference_v2', 'exp_qwen3_4b_scierc_merge_inference', 'exp_qwen3_4b_scierc_finetune_v3', 'exp_qwen3_4b_conll_finetune_resume', 'exp_qwen3_4b_scierc_finetune_v2', 'exp_qwen3_4b_conll_finetune', 'exp_freeform_seed789_v2', 'exp_qwen3_4b_scierc_finetune', 'exp_lp_t07_scierc', 'exp_lp_scierc_t07', 'exp_re_scierc_seed456', 'exp_re_scierc_seed123', 'exp_017_llama_conll_n8_t07', 'exp008_re_n16', 'exp001_seed456', 'exp001_seed123', 'exp_001_n16_seed456_full', 'exp_001_n16_seed123_full', 'exp_007_ner_llama', 'exp_002_merge_conll2003', 'exp_019_supervised_verifier', 'exp_018_llama_scierc_seed456', 'exp_002_conll_n16_r1024', 'exp_007_llama_n16_r1024', 'exp_001_seed123_v2_r1024', 'exp_001_seed456_v2_ner_r1024', 'exp_001_seed42_v2_r1024', 'exp_017_llama_conll_n16_s456', 'exp_017_llama_conll_n16_s123', 'exp_008_re_n16_full', 'exp_001_n16_seed123', 'exp_016_signal_ensemble', 'exp_001_ner_n16_scierc', 'exp_002', 'exp_002_ner_conll2003', 'exp_004_re_diagnostic', 'exp_005', 'exp_014_entity_majority_voting', 'exp_013_exact_match_voting', 'exp_012_logprob_baseline', 'mvp_pilot_005', 'e1_component_wise_re_sj', 'mvp_pilot_004', 'ft_002_v2', 'mvp_pilot_002', 'ft_002', 'ft_001', 'mvp_pilot_003', 'mvp_pilot_001']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a1502e6-d59a-4e08-83ed-f7a6f9a8acf0",
  "isSidechain": true,
  "promptId": "231b764b-2b39-49a0-b546-ab3bf4d9355b",
  "agentId": "aa904c9d54f8cf8d3",
  "type": "user",
  "uuid": "6528f08b-c585-49db-a6b8-b870b123c276",
  "sourceToolAssistantUUID": "3a1502e6-d59a-4e08-83ed-f7a6f9a8acf0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b0548841-9ada-435d-86ea-ff41c7017560",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-21T11:33:26.420Z_

Now let me extract all experiments with "frontier", "ensemble", or "cross" in the exp_id.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6528f08b-c585-49db-a6b8-b870b123c276",
  "isSidechain": true,
  "agentId": "aa904c9d54f8cf8d3",
  "requestId": "req_011CbFeB5qLcwdgegmmVBwCn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7fd13f7e-51d9-4c57-a7c1-f3e30507ae2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b0548841-9ada-435d-86ea-ff41c7017560",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ETUC4Dw9chYtzZztMVW4M9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4203,
      "cache_read_input_tokens": 16497,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4203,
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

_source line 11 · 2026-05-21T11:33:34.423Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01FVQFwqDmWPZT9uLW3QBGsq`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/b0548841-9ada-435d-86ea-ff41c7017560/tool-results/mcp-agent-ml-research-read_registry-1779363177682.txt') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Find all matching experiments\nfrontier_exps = {}\nensemble_exps = {}\ncross_exps = {}\n\nfor exp_id, exp_data in experiments.items():\n    exp_lower = exp_id.lower()\n    if 'frontier' in exp_lower:\n        frontier_exps[exp_id] = exp_data\n    if 'ensemble' in exp_lower:\n        ensemble_exps[exp_id] = exp_data\n    if 'cross' in exp_lower:\n        cross_exps[exp_id] = exp_data\n\nprint(\"=\" * 80)\nprint(f\"FRONTIER experiments: {len(frontier_exps)}\")\nprint(\"=\" * 80)\nfor exp_id, data in frontier_exps.items():\n    print(f\"\\n{'='*80}\")\n    print(f\"EXP_ID: {exp_id}\")\n    print(f\"{'='*80}\")\n    print(json.dumps(data, indent=2, ensure_ascii=False))\n\nprint(\"\\n\\n\" + \"=\" * 80)\nprint(f\"ENSEMBLE experiments: {len(ensemble_exps)}\")\nprint(\"=\" * 80)\nfor exp_id, data in ensemble_exps.items():\n    print(f\"\\n{'='*80}\")\n    print(f\"EXP_ID: {exp_id}\")\n    print(f\"{'='*80}\")\n    print(json.dumps(data, indent=2, ensure_ascii=False))\n\nprint(\"\\n\\n\" + \"=\" * 80)\nprint(f\"CROSS experiments: {len(cross_exps)}\")\nprint(\"=\" * 80)\nfor exp_id, data in cross_exps.items():\n    print(f\"\\n{'='*80}\")\n    print(f\"EXP_ID: {exp_id}\")\n    print(f\"{'='*80}\")\n    print(json.dumps(data, indent=2, ensure_ascii=False))\n\nPYEOF",
  "description": "Extract all frontier/ensemble/cross experiments with full details",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7fd13f7e-51d9-4c57-a7c1-f3e30507ae2c",
  "isSidechain": true,
  "agentId": "aa904c9d54f8cf8d3",
  "requestId": "req_011CbFeB5qLcwdgegmmVBwCn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63264ba9-93dc-4d2e-9e72-b907c88d040f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b0548841-9ada-435d-86ea-ff41c7017560",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ETUC4Dw9chYtzZztMVW4M9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4203,
      "cache_read_input_tokens": 16497,
      "output_tokens": 734,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4203
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 734,
          "cache_read_input_tokens": 16497,
          "cache_creation_input_tokens": 4203,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4203,
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

_source line 12 · 2026-05-21T11:33:34.513Z_

<details><summary>↩ Tool result · `toolu_01FVQFwqDmWPZT9uLW3QBGsq`</summary>

```text
================================================================================
FRONTIER experiments: 5
================================================================================

================================================================================
EXP_ID: exp_frontier_sc_gemini25pro
================================================================================
{
  "status": "DONE",
  "conclusion": "success",
  "metrics": {
    "greedy_f1": 0.6301,
    "mv_f1": 0.6446,
    "oracle_f1": 0.7575,
    "mv_gain_pp": 1.45,
    "selection_gap_pp": 11.29,
    "mv_captures_pct": 11.4,
    "agreement_rho": 0.3887,
    "degeneracy_rate": 0.285,
    "fleiss_kappa": 0.5185,
    "soft_jaccard": 0.8023,
    "alpha_crit": 0.4756,
    "alpha_crit_eff": 0.6651,
    "parse_failure_rate": 0.119,
    "n_instances": 200,
    "mv_wins": 33,
    "mv_ties": 144,
    "mv_loses": 23,
    "verdict": "MV helps (+1.45pp), captures 11% of oracle headroom"
  }
}

================================================================================
EXP_ID: exp_frontier_sc_deepseek
================================================================================
{
  "status": "DONE",
  "metrics": {
    "greedy_f1": 0.3992,
    "mv_f1": 0.4243,
    "oracle_f1": 0.714,
    "degeneracy_rate": 0.055,
    "agreement_rho": 0.2051,
    "fleiss_kappa_rho": 0.1471,
    "sj_rho": 0.1635,
    "mv_gain_over_greedy": 0.0251,
    "selection_gap": 0.2897,
    "parse_failure_count": 751,
    "total_api_calls": 1600,
    "elapsed_s": 4043.7
  },
  "conclusion": "success"
}

================================================================================
EXP_ID: exp_frontier_sc_claude_sonnet4
================================================================================
{
  "status": "DONE",
  "conclusion": "success",
  "metrics": {
    "greedy_f1": 0.6068,
    "mv_f1": 0.6226,
    "oracle_f1": 0.6544,
    "degeneracy_rate": 0.74,
    "selection_gap": 0.0318,
    "parse_failures": 103,
    "api_calls": 1600,
    "wall_clock_seconds": 6118,
    "instances": 200
  }
}

================================================================================
EXP_ID: exp_frontier_sc_gpt55_fewnerd_v2
================================================================================
{
  "status": "DONE",
  "conclusion": "success",
  "metrics": {
    "greedy_f1": 0.6382,
    "mv_f1": 0.6521,
    "oracle_f1": 0.7203,
    "degeneracy_rate": 0.5,
    "rho_agreement": 0.3551,
    "rho_fk": 0.3515,
    "rho_sj": 0.3461,
    "instances": 200
  }
}

================================================================================
EXP_ID: exp_b_frontier_sc_fewnerd
================================================================================
{
  "status": "DONE",
  "conclusion": "failed"
}


================================================================================
ENSEMBLE experiments: 1
================================================================================

================================================================================
EXP_ID: exp_016_signal_ensemble
================================================================================
{
  "status": "DONE",
  "conclusion": "success",
  "metrics": {
    "sj_logprob_pearson_ner": 0.57,
    "sj_logprob_pearson_re": 0.42,
    "best_linear_ner": {
      "combo": "SJ+voting_conf",
      "alpha": 0.3,
      "rho": 0.489
    },
    "best_linear_re": {
      "combo": "voting_conf+logprob",
      "alpha": 0.6,
      "rho": 0.429
    },
    "ensemble_ner_auroc": 0.735,
    "ensemble_re_auroc": 0.719,
    "best_single_ner_auroc": 0.7,
    "best_single_re_auroc": 0.721,
    "ensemble_ner_delta": 0.035,
    "selection_f1_ner": {
      "greedy": 0.609,
      "logprob": 0.609,
      "sj": 0.604,
      "ensemble": 0.604,
      "voting": 0.596,
      "random": 0.58,
      "oracle": 0.769
    },
    "selection_f1_re": {
      "logprob": 0.397,
      "greedy": 0.374,
      "sj": 0.368,
      "ensemble": 0.367,
      "voting": 0.338,
      "random": 0.338,
      "oracle": 0.561
    },
    "diagnosis": "SJ+voting_conf linear combo boosts NER ρ to 0.489 (+23%). RE: logprob-best is ONLY method beating greedy (0.397 vs 0.374). Ensemble AUROC +0.035 on NER. Oracle gap still huge."
  }
}


================================================================================
CROSS experiments: 1
================================================================================

================================================================================
EXP_ID: exp_cross_model_consistency
================================================================================
{
  "status": "DONE",
  "metrics": {
    "scierc": {
      "n_filtered": 529,
      "qwen_greedy_f1": 0.6453,
      "llama_greedy_f1": 0.646,
      "degeneracy": {
        "pure_qwen": 0.1323,
        "pure_llama": 0.1777,
        "mixed": 0.0964
      },
      "construction_f1": {
        "pure_qwen_uniform": 0.6449,
        "pure_qwen_vc": 0.6413,
        "pure_llama_uniform": 0.6545,
        "pure_llama_vc": 0.649,
        "mixed_uniform": 0.6625,
        "mixed_vc": 0.6591
      },
      "bootstrap": {
        "mixed_uni_vs_pure_qwen_uni": {
          "delta_pp": 1.77,
          "p": 0.0102,
          "ci": [
            0.27,
            3.28
          ]
        },
        "mixed_vc_vs_pure_qwen_vc": {
          "delta_pp": 1.77,
          "p": 0.0093,
          "ci": [
            0.33,
            3.27
          ]
        },
        "mixed_uni_vs_pure_llama_uni": {
          "delta_pp": 0.81,
          "p": 0.1304,
          "ci": [
            -0.59,
            2.25
          ]
        },
        "mixed_vc_vs_pure_llama_vc": {
          "delta_pp": 1.01,
          "p": 0.0702,
          "ci": [
            -0.32,
            2.38
          ]
        }
      }
    },
    "fewnerd": {
      "n_filtered": 32565,
      "qwen_greedy_f1": 0.7478,
      "llama_greedy_f1": 0.7841,
      "degeneracy": {
        "pure_qwen": 0.1004,
        "pure_llama": 0.2336,
        "mixed": 0.1158
      },
      "construction_f1": {
        "pure_qwen_uniform": 0.7499,
        "pure_qwen_vc": 0.7448,
        "pure_llama_uniform": 0.7873,
        "pure_llama_vc": 0.7869,
        "mixed_uniform": 0.7916,
        "mixed_vc": 0.7898
      },
      "bootstrap": {
        "mixed_uni_vs_pure_qwen_uni": {
          "delta_pp": 4.17,
          "p": 0,
          "ci": [
            3.92,
            4.4
          ]
        },
        "mixed_vc_vs_pure_qwen_vc": {
          "delta_pp": 4.5,
          "p": 0,
          "ci": [
            4.25,
            4.75
          ]
        },
        "mixed_uni_vs_pure_llama_uni": {
          "delta_pp": 0.42,
          "p": 0,
          "ci": [
            0.27,
            0.58
          ]
        },
        "mixed_vc_vs_pure_llama_vc": {
          "delta_pp": 0.29,
          "p": 0.0001,
          "ci": [
            0.13,
            0.45
          ]
        }
      }
    }
  },
  "conclusion": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63264ba9-93dc-4d2e-9e72-b907c88d040f",
  "isSidechain": true,
  "promptId": "231b764b-2b39-49a0-b546-ab3bf4d9355b",
  "agentId": "aa904c9d54f8cf8d3",
  "type": "user",
  "uuid": "f4a318cc-3872-4797-82f8-0eaaae077457",
  "sourceToolAssistantUUID": "63264ba9-93dc-4d2e-9e72-b907c88d040f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b0548841-9ada-435d-86ea-ff41c7017560",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-21T11:33:51.881Z_

Here are all matching experiments verbatim.

---

## FRONTIER experiments (5 total)

### 1. `exp_frontier_sc_gemini25pro`
- **status**: DONE
- **conclusion**: success
- **metrics**:
  - greedy_f1: 0.6301
  - mv_f1: 0.6446
  - oracle_f1: 0.7575
  - mv_gain_pp: 1.45
  - selection_gap_pp: 11.29
  - mv_captures_pct: 11.4
  - agreement_rho: 0.3887
  - degeneracy_rate: 0.285
  - fleiss_kappa: 0.5185
  - soft_jaccard: 0.8023
  - alpha_crit: 0.4756
  - alpha_crit_eff: 0.6651
  - parse_failure_rate: 0.119
  - n_instances: 200
  - mv_wins: 33, mv_ties: 144, mv_loses: 23
  - verdict: "MV helps (+1.45pp), captures 11% of oracle headroom"

### 2. `exp_frontier_sc_deepseek`
- **status**: DONE
- **conclusion**: success
- **metrics**:
  - greedy_f1: 0.3992
  - mv_f1: 0.4243
  - oracle_f1: 0.714
  - degeneracy_rate: 0.055
  - agreement_rho: 0.2051
  - fleiss_kappa_rho: 0.1471
  - sj_rho: 0.1635
  - mv_gain_over_greedy: 0.0251
  - selection_gap: 0.2897
  - parse_failure_count: 751
  - total_api_calls: 1600
  - elapsed_s: 4043.7

### 3. `exp_frontier_sc_claude_sonnet4`
- **status**: DONE
- **conclusion**: success
- **metrics**:
  - greedy_f1: 0.6068
  - mv_f1: 0.6226
  - oracle_f1: 0.6544
  - degeneracy_rate: 0.74
  - selection_gap: 0.0318
  - parse_failures: 103
  - api_calls: 1600
  - wall_clock_seconds: 6118
  - instances: 200

### 4. `exp_frontier_sc_gpt55_fewnerd_v2`
- **status**: DONE
- **conclusion**: success
- **metrics**:
  - greedy_f1: 0.6382
  - mv_f1: 0.6521
  - oracle_f1: 0.7203
  - degeneracy_rate: 0.5
  - rho_agreement: 0.3551
  - rho_fk: 0.3515
  - rho_sj: 0.3461
  - instances: 200

### 5. `exp_b_frontier_sc_fewnerd`
- **status**: DONE
- **conclusion**: **failed**
- **metrics**: none recorded

---

## ENSEMBLE experiments (1 total)

### `exp_016_signal_ensemble`
- **status**: DONE
- **conclusion**: success
- **metrics**:
  - sj_logprob_pearson_ner: 0.57
  - sj_logprob_pearson_re: 0.42
  - best_linear_ner: combo="SJ+voting_conf", alpha=0.3, rho=0.489
  - best_linear_re: combo="voting_conf+logprob", alpha=0.6, rho=0.429
  - ensemble_ner_auroc: 0.735
  - ensemble_re_auroc: 0.719
  - best_single_ner_auroc: 0.7
  - best_single_re_auroc: 0.721
  - ensemble_ner_delta: 0.035
  - selection_f1_ner: greedy=0.609, logprob=0.609, sj=0.604, ensemble=0.604, voting=0.596, random=0.58, oracle=0.769
  - selection_f1_re: logprob=0.397, greedy=0.374, sj=0.368, ensemble=0.367, voting=0.338, random=0.338, oracle=0.561
  - diagnosis: "SJ+voting_conf linear combo boosts NER rho to 0.489 (+23%). RE: logprob-best is ONLY method beating greedy (0.397 vs 0.374). Ensemble AUROC +0.035 on NER. Oracle gap still huge."

---

## CROSS experiments (1 total)

### `exp_cross_model_consistency`
- **status**: DONE
- **conclusion**: success
- **metrics** (two datasets):

**SciERC** (n_filtered=529):
  - qwen_greedy_f1: 0.6453, llama_greedy_f1: 0.646
  - degeneracy: pure_qwen=0.1323, pure_llama=0.1777, mixed=0.0964
  - construction_f1: pure_qwen_uniform=0.6449, pure_qwen_vc=0.6413, pure_llama_uniform=0.6545, pure_llama_vc=0.649, mixed_uniform=0.6625, mixed_vc=0.6591
  - bootstrap mixed_uni vs pure_qwen_uni: delta_pp=1.77, p=0.0102, ci=[0.27, 3.28]
  - bootstrap mixed_vc vs pure_qwen_vc: delta_pp=1.77, p=0.0093, ci=[0.33, 3.27]
  - bootstrap mixed_uni vs pure_llama_uni: delta_pp=0.81, p=0.1304, ci=[-0.59, 2.25]
  - bootstrap mixed_vc vs pure_llama_vc: delta_pp=1.01, p=0.0702, ci=[-0.32, 2.38]

**FewNERD** (n_filtered=32565):
  - qwen_greedy_f1: 0.7478, llama_greedy_f1: 0.7841
  - degeneracy: pure_qwen=0.1004, pure_llama=0.2336, mixed=0.1158
  - construction_f1: pure_qwen_uniform=0.7499, pure_qwen_vc=0.7448, pure_llama_uniform=0.7873, pure_llama_vc=0.7869, mixed_uniform=0.7916, mixed_vc=0.7898
  - bootstrap mixed_uni vs pure_qwen_uni: delta_pp=4.17, p=0, ci=[3.92, 4.4]
  - bootstrap mixed_vc vs pure_qwen_vc: delta_pp=4.5, p=0, ci=[4.25, 4.75]
  - bootstrap mixed_uni vs pure_llama_uni: delta_pp=0.42, p=0, ci=[0.27, 0.58]
  - bootstrap mixed_vc vs pure_llama_vc: delta_pp=0.29, p=0.0001, ci=[0.13, 0.45]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4a318cc-3872-4797-82f8-0eaaae077457",
  "isSidechain": true,
  "agentId": "aa904c9d54f8cf8d3",
  "requestId": "req_011CbFeBw51yFgcmTRtzoRyq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "902b040e-9cd5-4fcb-bf82-0b2b8e8ad63f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b0548841-9ada-435d-86ea-ff41c7017560",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KqcoJsqp54asUwZWUUeNVZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3195,
      "cache_read_input_tokens": 20700,
      "output_tokens": 1896,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3195
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1896,
          "cache_read_input_tokens": 20700,
          "cache_creation_input_tokens": 3195,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3195,
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
