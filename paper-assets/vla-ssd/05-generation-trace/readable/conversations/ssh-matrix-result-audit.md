# ssh matrix result audit

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 0
- **Tool calls:** 26
- **Original source:** `logs/chats/worker_ssh_matrix_result_audit_20260522T010700.jsonl`
- **Structured JSON:** [`6691a8540b2d0289ed4f.json`](../../sessions/66/6691a8540b2d0289ed4f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

53 recorded events

### Tool call

_source line 1 · 2026-05-22T01:10:45.168291+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T01:10:45.168642+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T01:10:45.168828+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/results/ -type f -name \"*.json\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/results/ -type f -name \"*.json\""
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-22T01:10:45.169010+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "vla-ssd",
  "limit": "0",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "vla-ssd",
    "limit": "0",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-22T01:10:45.169292+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/vla-ssd/results/dinov2/temporal_distance/layer_0.json\\n/root/autodl-tmp/vla-ssd/results/dinov2/temporal_distance/summary.json\\n/root/autodl-tmp/vla-ssd/results/dinov2/subtask_predicate/summary.json\\n/root/autodl-tmp/vla-ssd/results/dinov2/temporal_distance_old_backup/layer_0.json\\n/root/autodl-tmp/vla-ssd/results/dinov2/temporal_distance_old_backup/summary.json\\n/root/autodl-tmp/vla-ssd/results/dinov2/temporal_distance_old_backup/temporal_distance/layer_0.json\\n/root/autodl-tmp/vla-ssd/results/dinov2/temporal_distance_old_backup/temporal_distance/summary.json\\n/root/autodl-tmp/vla-ssd/results/dinov2/action_prediction/layer_0.json\\n/root/autodl-tmp/vla-ssd/results/dinov2/action_prediction/summary.json\\n/root/autodl-tmp/vla-ssd/results/dinov2/action_delta/layer_0.json\\n/root/autodl-tmp/vla-ssd/results/dinov2/action_delta/summary.json\\n/root/autodl-tmp/vla-ssd/results/oracle/oracle/layer_oracle.json\\n/root/autodl-tmp/vla-ssd/results/oracle/oracle/summary.json\\n/root/autodl-tmp/vla-ssd/results/dinov2_shuffle/temporal_distance/layer_0.json\\n/root/autodl-tmp/vla-ssd/results/dinov2_shuffle/temporal_distance/summary.json\\n/root/autodl-tmp/vla-ssd/results/untrained/temporal_distance/layer_0.json\\n/root/autodl-tmp/vla-ssd/results/untrained/temporal_distance/layer_1.json\\n/root/autodl-tmp/vla-ssd/results/untrained/temporal_distance/layer_2.json\\n/root/autodl-tmp/vla-ssd/results/untrained/temporal_distance/layer_3.json\\n/root/autodl-tmp/vla-ssd/results/untrained/temporal_distance/layer_4.json\\n/root/autodl-tmp/vla-ssd/results/untrained/temporal_distance/layer_5.json\\n/root/autodl-tmp/vla-ssd/results/untrained/temporal_distance/layer_6.json\\n/root/autodl-tmp/vla-ssd/results/untrained/temporal_distance/layer_7.json\\n/root/autodl-tmp/vla-ssd/results/untrained/temporal_distance/layer_8.json\\n/root/autodl-tmp/vla-ssd/results/untrained/temporal_distance/layer_9.json\\n/root/autodl-tmp/vla
…[truncated 6406 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T01:10:45.170638+00:00_

Error: result (254,959 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/269b335b-8109-4887-9807-ef7e6258fc6a/tool-results/mcp-agent-ml-research-read_registry-1779412036807.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/269b335b-8109-4887-9807-ef7e6258fc6a/tool-results/mcp-agent-ml-research-read_registry-1779412036807.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T01:10:45.171040+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls -d /root/autodl-tmp/vla-ssd/results/*/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls -d /root/autodl-tmp/vla-ssd/results/*/"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T01:10:45.171256+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/vla-ssd/results/ablations/\\n/root/autodl-tmp/vla-ssd/results/action_probe/\\n/root/autodl-tmp/vla-ssd/results/analysis/\\n/root/autodl-tmp/vla-ssd/results/architecture_audit/\\n/root/autodl-tmp/vla-ssd/results/attention/\\n/root/autodl-tmp/vla-ssd/results/cka/\\n/root/autodl-tmp/vla-ssd/results/counterfactual_10tasks/\\n/root/autodl-tmp/vla-ssd/results/counterfactual_spatial/\\n/root/autodl-tmp/vla-ssd/results/cross_instruction/\\n/root/autodl-tmp/vla-ssd/results/cross_instruction_dense/\\n/root/autodl-tmp/vla-ssd/results/cross_instruction_finetuned/\\n/root/autodl-tmp/vla-ssd/results/cross_instruction_spatial/\\n/root/autodl-tmp/vla-ssd/results/demo_sensitivity_25/\\n/root/autodl-tmp/vla-ssd/results/dinov2/\\n/root/autodl-tmp/vla-ssd/results/dinov2_libero_goal/\\n/root/autodl-tmp/vla-ssd/results/dinov2_libero_goal_frame0/\\n/root/autodl-tmp/vla-ssd/results/dinov2_libero_goal_linear/\\n/root/autodl-tmp/vla-ssd/results/dinov2_libero_goal_pca1024/\\n/root/autodl-tmp/vla-ssd/results/dinov2_shuffle/\\n/root/autodl-tmp/vla-ssd/results/figure_data/\\n/root/autodl-tmp/vla-ssd/results/figures/\\n/root/autodl-tmp/vla-ssd/results/functional_validation/\\n/root/autodl-tmp/vla-ssd/results/l1_head_ablation/\\n/root/autodl-tmp/vla-ssd/results/libero_closedloop_probe/\\n/root/autodl-tmp/vla-ssd/results/libero_goal/\\n/root/autodl-tmp/vla-ssd/results/libero_long/\\n/root/autodl-tmp/vla-ssd/results/libero_long_untrained/\\n/root/autodl-tmp/vla-ssd/results/libero_object/\\n/root/autodl-tmp/vla-ssd/results/libero_object_untrained/\\n/root/autodl-tmp/vla-ssd/results/llama2base_action_probe/\\n/root/autodl-tmp/vla-ssd/results/nora_goal/\\n/root/autodl-tmp/vla-ssd/results/nora_spatial/\\n/root/autodl-tmp/vla-ssd/results/oracle/\\n/root/autodl-tmp/vla-ssd/results/perlayer_rsa/\\n/root/autodl-tmp/vla-ssd/results/permutation_10k/\\n/root/autodl-tmp/vla-ssd/results/phi3v_r2_seed_expansion/\\n/root/autodl-tmp/vla-ssd/re
…[truncated 1187 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T01:10:45.171441+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/269b335b-8109-4887-9807-ef7e6258fc6a/tool-results/mcp-agent-ml-research-read_registry-1779412036807.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result.get('experiments', result) if isinstance(result, dict) else result\nif isinstance(exps, list):\n    for e in exps:\n        eid = e.get('exp_id', 'N/A')\n        status = e.get('status', 'N/A')\n        conclusion = e.get('conclusion', '')\n        suite = e.get('suite', e.get('config', {}).get('suite', ''))\n        arch = e.get('architecture', e.get('config', {}).get('architecture', ''))\n        print(f'{eid}|{status}|{conclusion}|{suite}|{arch}')\nelif isinstance(exps, dict):\n    for eid, e in exps.items():\n        status = e.get('status', 'N/A')\n        conclusion = e.get('conclusion', '')\n        suite = e.get('suite', e.get('config', {}).get('suite', ''))\n        arch = e.get('architecture', e.get('config', {}).get('architecture', ''))\n        print(f'{eid}|{status}|{conclusion}|{suite}|{arch}')\n\" 2>&1 | head -100",
  "description": "Parse registry JSON for experiment status summary"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/269b335b-8109-4887-9807-ef7e6258fc6a/tool-results/mcp-agent-ml-research-read_registry-1779412036807.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result.get('experiments', result) if isinstance(result, dict) else result\nif isinstance(exps, list):\n    for e in exps:\n        eid = e.get('exp_id', 'N/A')\n        status = e.get('status', 'N/A')\n        conclusion = e.get('conclusion', '')\n        suite = e.get('suite', e.get('config', {}).get('suite', ''))\n        arch = e.get('architecture', e.get('config', {}).get('architecture', ''))\n        print(f'{eid}|{status}|{conclusion}|{suite}|{arch}')\nelif isinstance(exps, dict):\n    for eid, e in exps.items():\n        status = e.get('status', 'N/A')\n        conclusion = e.get('conclusion', '')\n        suite = e.get('suite', e.get('config', {}).get('suite', ''))\n        arch = e.get('architecture', e.get('config', {}).get('architecture', ''))\n        print(f'{eid}|{status}|{conclusion}|{suite}|{arch}')\n\" 2>&1 | head -100",
    "description": "Parse registry JSON for experiment status summary"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T01:10:45.171623+00:00_

Traceback (most recent call last):
  File "&lt;string>", line 16, in &lt;module>
    status = e.get('status', 'N/A')
             ^^^^^
AttributeError: 'bool' object has no attribute 'get'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T01:10:45.171780+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -c 5000 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/269b335b-8109-4887-9807-ef7e6258fc6a/tool-results/mcp-agent-ml-research-read_registry-1779412036807.txt",
  "description": "Inspect registry JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "Bash",
  "tool_args": {
    "command": "head -c 5000 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/269b335b-8109-4887-9807-ef7e6258fc6a/tool-results/mcp-agent-ml-research-read_registry-1779412036807.txt",
    "description": "Inspect registry JSON structure"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T01:10:45.171998+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"openvla_spatial_standardized_v1\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T01:02:09.424Z\", \"updated_at\": \"2026-05-22T01:02:13.390Z\", \"hypothesis\": \"OpenVLA (Llama-2-7B backbone) on LIBERO-Spatial standardized 5-phase pipeline (R² probing, L1 attention, cross-instruction classification, RSA, counterfactual). Both trained and untrained conditions. Filling missing R² exit, L1 attention, and untrained CF data for Spatial cell. Expect similar patterns to Goal/Object: R² exit collapse in trained, instruction-dominant L1 heads.\"}, \"openvla_goal_standardized_v1\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T00:28:34.686Z\", \"updated_at\": \"2026-05-22T00:33:28.901Z\", \"hypothesis\": \"OpenVLA (Llama-2-7B backbone) on LIBERO-Goal standardized 5-phase pipeline (R² probing, L1 attention, cross-instruction, RSA, counterfactual). Both trained (openvla-7b-finetuned-libero-goal) and untrained (openvla-7b OXE pretrained) conditions. Replaces earlier incomplete Goal data that lacked R² probing and untrained arm.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/vla-ssd && python scripts/libero_goal_full_pipeline.py --conditions trained untrained\\\"\", \"server\": \"westd-19183\", \"gpu\": [\"cuda:1\"], \"pid\": \"591230\", \"log_path\": \"~/runs/vla-ssd/openvla_goal_standardized_v1.log\", \"submitted_at\": \"2026-05-22T00:33:00Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/vla-ssd/data/libero/libero_goal/\", \"data_count\": \"10 tasks x 10 demos x 50 timesteps\", \"model_name\": \"openvla-7b-finetuned-libero-goal / openvla-7b\", \"seed\": 42, \"checkpoint_source\": \"openvla-7b-finetuned-libero-goal (trained) + openvla-7b (untrained)\", \"checkpoint_path\": \"N/A (probing experim
…[truncated 2993 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T01:10:45.172162+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "python3 -c \"\nimport os\nbase = '/root/autodl-tmp/vla-ssd/results'\nphases = ['action_r2_probing.json', 'l1_attention_profile.json', 'cross_instruction_classification.json', 'rsa_analysis.json', 'counterfactual_combined.json']\ndirs_of_interest = [\n    'libero_goal', 'libero_object', 'libero_long',\n    'libero_long_untrained', 'libero_object_untrained',\n    'nora_goal', 'nora_spatial',\n    'tracvla_goal/trained', 'tracvla_goal/untrained',\n    'tracvla_spatial/trained', 'tracvla_spatial/untrained',\n    'tracvla_object/trained', 'tracvla_object/untrained',\n    'tracvla_long/trained', 'tracvla_long/untrained',\n]\nfor d in dirs_of_interest:\n    full = os.path.join(base, d)\n    found = []\n    missing = []\n    for p in phases:\n        if os.path.exists(os.path.join(full, p)):\n            found.append(p.replace('.json',''))\n        else:\n            missing.append(p.replace('.json',''))\n    print(f'{d}|FOUND:{len(found)}|{\",\".join(found)}|MISS:{len(missing)}|{\",\".join(missing)}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "python3 -c \"\nimport os\nbase = '/root/autodl-tmp/vla-ssd/results'\nphases = ['action_r2_probing.json', 'l1_attention_profile.json', 'cross_instruction_classification.json', 'rsa_analysis.json', 'counterfactual_combined.json']\ndirs_of_interest = [\n    'libero_goal', 'libero_object', 'libero_long',\n    'libero_long_untrained', 'libero_object_untrained',\n    'nora_goal', 'nora_spatial',\n    'tracvla_goal/trained', 'tracvla_goal/untrained',\n    'tracvla_spatial/trained', 'tracvla_spatial/untrained',\n    'tracvla_object/trained', 'tracvla_object/untrained',\n    'tracvla_long/trained', 'tracvla_long/untrained',\n]\nfor d in dirs_of_interest:\n    full = os.path.join(base, d)\n    found = []\n    missing = []\n    for p in phases:\n        if os.path.exists(os.path.join(full, p)):\n            found.append(p.replace('.json',''))\n        else:\n            missing.append(p.replace('.json',''))\n    print(f'{d}|FOUND:{len(found)}|{\",\".join(found)}|MISS:{len(missing)}|{\",\".join(missing)}')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T01:10:45.172304+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T01:10:45.172450+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/results/libero_goal /root/autodl-tmp/vla-ssd/results/libero_object /root/autodl-tmp/vla-ssd/results/libero_long /root/autodl-tmp/vla-ssd/results/libero_object_untrained /root/autodl-tmp/vla-ssd/results/libero_long_untrained -maxdepth 1 -name \"*.json\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/results/libero_goal /root/autodl-tmp/vla-ssd/results/libero_object /root/autodl-tmp/vla-ssd/results/libero_long /root/autodl-tmp/vla-ssd/results/libero_object_untrained /root/autodl-tmp/vla-ssd/results/libero_long_untrained -maxdepth 1 -name \"*.json\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T01:10:45.172599+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/vla-ssd/results/libero_goal/action_r2_probing.json\\n/root/autodl-tmp/vla-ssd/results/libero_goal/l1_attention_profile.json\\n/root/autodl-tmp/vla-ssd/results/libero_goal/cross_instruction_classification.json\\n/root/autodl-tmp/vla-ssd/results/libero_goal/rsa_analysis.json\\n/root/autodl-tmp/vla-ssd/results/libero_object/action_r2_probing.json\\n/root/autodl-tmp/vla-ssd/results/libero_object/l1_attention_profile.json\\n/root/autodl-tmp/vla-ssd/results/libero_object/cross_instruction_classification.json\\n/root/autodl-tmp/vla-ssd/results/libero_object/rsa_analysis.json\\n/root/autodl-tmp/vla-ssd/results/libero_object/counterfactual_combined.json\\n/root/autodl-tmp/vla-ssd/results/libero_long/action_r2_probing.json\\n/root/autodl-tmp/vla-ssd/results/libero_long/l1_attention_profile.json\\n/root/autodl-tmp/vla-ssd/results/libero_long/cross_instruction_classification.json\\n/root/autodl-tmp/vla-ssd/results/libero_long/rsa_analysis.json\\n/root/autodl-tmp/vla-ssd/results/libero_long/counterfactual_combined.json\\n/root/autodl-tmp/vla-ssd/results/libero_object_untrained/action_r2_probing.json\\n/root/autodl-tmp/vla-ssd/results/libero_object_untrained/l1_attention_profile.json\\n/root/autodl-tmp/vla-ssd/results/libero_object_untrained/cross_instruction_classification.json\\n/root/autodl-tmp/vla-ssd/results/libero_object_untrained/rsa_analysis.json\\n/root/autodl-tmp/vla-ssd/results/libero_object_untrained/counterfactual_combined.json\\n/root/autodl-tmp/vla-ssd/results/libero_long_untrained/action_r2_probing.json\\n/root/autodl-tmp/vla-ssd/results/libero_long_untrained/l1_attention_profile.json\\n/root/autodl-tmp/vla-ssd/results/libero_long_untrained/cross_instruction_classification.json\\n/root/autodl-tmp/vla-ssd/results/libero_long_untrained/rsa_analysis.json\\n/root/autodl-tmp/vla-ssd/results/libero_long_untrained/counterfactual_combined.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": n
…[truncated 49 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T01:10:45.172741+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/results/nora_goal /root/autodl-tmp/vla-ssd/results/nora_spatial -maxdepth 2 -name \"*.json\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/results/nora_goal /root/autodl-tmp/vla-ssd/results/nora_spatial -maxdepth 2 -name \"*.json\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T01:10:45.172893+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/vla-ssd/results/nora_goal/trained/action_r2_probing.json\\n/root/autodl-tmp/vla-ssd/results/nora_goal/trained/l1_attention_profile.json\\n/root/autodl-tmp/vla-ssd/results/nora_goal/trained/cross_instruction_classification.json\\n/root/autodl-tmp/vla-ssd/results/nora_goal/trained/counterfactual_combined.json\\n/root/autodl-tmp/vla-ssd/results/nora_goal/untrained/action_r2_probing.json\\n/root/autodl-tmp/vla-ssd/results/nora_goal/untrained/l1_attention_profile.json\\n/root/autodl-tmp/vla-ssd/results/nora_goal/untrained/cross_instruction_classification.json\\n/root/autodl-tmp/vla-ssd/results/nora_goal/untrained/counterfactual_combined.json\\n/root/autodl-tmp/vla-ssd/results/nora_spatial/trained/action_r2_probing.json\\n/root/autodl-tmp/vla-ssd/results/nora_spatial/trained/l1_attention_profile.json\\n/root/autodl-tmp/vla-ssd/results/nora_spatial/trained/cross_instruction_classification.json\\n/root/autodl-tmp/vla-ssd/results/nora_spatial/trained/counterfactual_combined.json\\n/root/autodl-tmp/vla-ssd/results/nora_spatial/untrained/action_r2_probing.json\\n/root/autodl-tmp/vla-ssd/results/nora_spatial/untrained/l1_attention_profile.json\\n/root/autodl-tmp/vla-ssd/results/nora_spatial/untrained/cross_instruction_classification.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T01:10:45.173112+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/results/tracvla_goal /root/autodl-tmp/vla-ssd/results/tracvla_spatial /root/autodl-tmp/vla-ssd/results/tracvla_object /root/autodl-tmp/vla-ssd/results/tracvla_long -maxdepth 2 -name \"*.json\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/results/tracvla_goal /root/autodl-tmp/vla-ssd/results/tracvla_spatial /root/autodl-tmp/vla-ssd/results/tracvla_object /root/autodl-tmp/vla-ssd/results/tracvla_long -maxdepth 2 -name \"*.json\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T01:10:45.173290+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/vla-ssd/results/tracvla_goal/trained/action_r2_probing.json\\n/root/autodl-tmp/vla-ssd/results/tracvla_goal/trained/l1_attention_profile.json\\n/root/autodl-tmp/vla-ssd/results/tracvla_goal/trained/cross_instruction_classification.json\\n/root/autodl-tmp/vla-ssd/results/tracvla_goal/trained/counterfactual_combined.json\\n/root/autodl-tmp/vla-ssd/results/tracvla_goal/untrained/action_r2_probing.json\\n/root/autodl-tmp/vla-ssd/results/tracvla_goal/untrained/l1_attention_profile.json\\n/root/autodl-tmp/vla-ssd/results/tracvla_goal/untrained/cross_instruction_classification.json\\n/root/autodl-tmp/vla-ssd/results/tracvla_goal/untrained/counterfactual_combined.json\\n/root/autodl-tmp/vla-ssd/results/tracvla_spatial/trained/action_r2_probing.json\\n/root/autodl-tmp/vla-ssd/results/tracvla_spatial/trained/l1_attention_profile.json\\n/root/autodl-tmp/vla-ssd/results/tracvla_spatial/trained/cross_instruction_classification.json\\n/root/autodl-tmp/vla-ssd/results/tracvla_spatial/trained/counterfactual_combined.json\\n/root/autodl-tmp/vla-ssd/results/tracvla_spatial/untrained/action_r2_probing.json\\n/root/autodl-tmp/vla-ssd/results/tracvla_spatial/untrained/l1_attention_profile.json\\n/root/autodl-tmp/vla-ssd/results/tracvla_spatial/untrained/cross_instruction_classification.json\\n/root/autodl-tmp/vla-ssd/results/tracvla_spatial/untrained/counterfactual_combined.json\\n/root/autodl-tmp/vla-ssd/results/tracvla_object/trained/action_r2_probing.json\\n/root/autodl-tmp/vla-ssd/results/tracvla_object/trained/l1_attention_profile.json\\n/root/autodl-tmp/vla-ssd/results/tracvla_object/trained/cross_instruction_classification.json\\n/root/autodl-tmp/vla-ssd/results/tracvla_object/trained/counterfactual_combined.json\\n/root/autodl-tmp/vla-ssd/results/tracvla_object/untrained/action_r2_probing.json\\n/root/autodl-tmp/vla-ssd/results/tracvla_object/untrained/l1_attention_profile.json\\n/root/autodl-tmp/vla-ssd/re
…[truncated 952 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T01:10:45.173442+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/269b335b-8109-4887-9807-ef7e6258fc6a/tool-results/mcp-agent-ml-research-read_registry-1779412036807.txt | python3 -c \"\nimport json, sys\nraw = json.loads(sys.stdin.read())\ndata = json.loads(raw['result'])\nexps = data['experiments']\nfor eid, e in exps.items():\n    if isinstance(e, dict):\n        status = e.get('status', '?')\n        conclusion = e.get('conclusion', '')\n        print(f'{eid}|{status}|{conclusion}')\n\" 2>&1",
  "description": "Parse registry experiments with status and conclusion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/269b335b-8109-4887-9807-ef7e6258fc6a/tool-results/mcp-agent-ml-research-read_registry-1779412036807.txt | python3 -c \"\nimport json, sys\nraw = json.loads(sys.stdin.read())\ndata = json.loads(raw['result'])\nexps = data['experiments']\nfor eid, e in exps.items():\n    if isinstance(e, dict):\n        status = e.get('status', '?')\n        conclusion = e.get('conclusion', '')\n        print(f'{eid}|{status}|{conclusion}')\n\" 2>&1",
    "description": "Parse registry experiments with status and conclusion"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T01:10:45.173566+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 5, in &lt;module>
    exps = data['experiments']
           ~~~~^^^^^^^^^^^^^^^
KeyError: 'experiments'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T01:10:45.173700+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/269b335b-8109-4887-9807-ef7e6258fc6a/tool-results/mcp-agent-ml-research-read_registry-1779412036807.txt') as f:\n    raw = json.load(f)\ndata = json.loads(raw['result'])\n# check top-level keys\nif isinstance(data, dict):\n    print('top keys:', list(data.keys())[:5])\n    # check if 'success' and 'data' pattern\n    if 'success' in data and 'data' in data:\n        inner = data['data']\n        if isinstance(inner, dict) and 'experiments' in inner:\n            exps = inner['experiments']\n        else:\n            exps = inner\n    elif 'experiments' in data:\n        exps = data['experiments']\n    else:\n        exps = data\n    \n    if isinstance(exps, dict):\n        for eid, e in exps.items():\n            if isinstance(e, dict):\n                status = e.get('status', '?')\n                conclusion = e.get('conclusion', '')\n                print(f'{eid}|{status}|{conclusion}')\n    elif isinstance(exps, list):\n        for e in exps:\n            eid = e.get('exp_id', '?')\n            status = e.get('status', '?')\n            conclusion = e.get('conclusion', '')\n            print(f'{eid}|{status}|{conclusion}')\n\" 2>&1",
  "description": "Parse registry JSON with correct structure detection"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/269b335b-8109-4887-9807-ef7e6258fc6a/tool-results/mcp-agent-ml-research-read_registry-1779412036807.txt') as f:\n    raw = json.load(f)\ndata = json.loads(raw['result'])\n# check top-level keys\nif isinstance(data, dict):\n    print('top keys:', list(data.keys())[:5])\n    # check if 'success' and 'data' pattern\n    if 'success' in data and 'data' in data:\n        inner = data['data']\n        if isinstance(inner, dict) and 'experiments' in inner:\n            exps = inner['experiments']\n        else:\n            exps = inner\n    elif 'experiments' in data:\n        exps = data['experiments']\n    else:\n        exps = data\n    \n    if isinstance(exps, dict):\n        for eid, e in exps.items():\n            if isinstance(e, dict):\n                status = e.get('status', '?')\n                conclusion = e.get('conclusion', '')\n                print(f'{eid}|{status}|{conclusion}')\n    elif isinstance(exps, list):\n        for e in exps:\n            eid = e.get('exp_id', '?')\n            status = e.get('status', '?')\n            conclusion = e.get('conclusion', '')\n            print(f'{eid}|{status}|{conclusion}')\n\" 2>&1",
    "description": "Parse registry JSON with correct structure detection"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-22T01:10:45.173866+00:00_

top keys: ['success', 'data', 'error', 'metadata']
openvla_spatial_standardized_v1|PREPARING|
openvla_goal_standardized_v1|RUNNING|
cf_batch_part2_v1|DONE|success
openvla_long_cf_trained|DONE|success
cf_batch_missing_v1|RUNNING|
behavioral_smoketest_diag|PREPARING|killed
behavioral_pilot_v2|PREPARING|killed
behavioral_pilot|PREPARING|killed
tracvla_spatial_full_v2|ALLOCATED|killed
openvla_long_untrained_v1|DONE|success
tracvla_goal_v1|DONE|success
tracvla_long_v1|DONE|success
tracvla_spatial_untrained_v1|DONE|success
openvla_long_pipeline_v1|DONE|failed
tracvla_object_untrained_v1|DONE|success
tracvla_object_full_v1|DONE|success
object_untrained_pipeline_v1|DONE|negative
nora_spatial_pipeline_v2|DONE|success
object_pipeline_ridge_v2|DONE|success
nora_spatial_pipeline_v1|DONE|failed
nora_goal_untrained_cf|DONE|success
object_pipeline_ridge|DONE|failed
nora_goal_pipeline_v3|DONE|success
nora_goal_pipeline_v2|DONE|killed
libero_object_full_pipeline|DONE|killed
nora_goal_full_pipeline|DONE|failed
tracvla_spatial_pipeline|DONE|failed
tracvla_spatial_trained|PREPARING|
counterfactual_10tasks_trajectory|DONE|success
counterfactual_spatial|DONE|success
behavioral_smoketest|DONE|negative
counterfactual_10tasks|DONE|success
permutation_10k|DONE|success
phi3v_untrained_seed_expansion|DONE|success
phi3v_r2_untrained_probe|DONE|success
phi3v_r2_seed_expansion|DONE|success
phi3v_r2_action_probe|DONE|success
specificity_random_seed_expansion|DONE|success
r2_probe_seed_expansion|DONE|success
phi3v_attention_untrained_10tasks|DONE|success
phi3v_attention_trained_10tasks|DONE|success
action_trajectory_cpu_analysis|DONE|success
phi3v_probe_untrained|DONE|success
phi3v_probe_trained|DONE|success
phi3v_attention_untrained|DONE|negative
phi3v_attention_trained|DONE|success
phi3v_attention_profile|DONE|success
official_checkpoint_sr_test|DONE|negative
closedloop_diagnosis|DONE|negative
finetuned_probe_profile|DONE|success
libero_finetuned_probe|PREPARING|
libero_finetuned_attention|DONE|s
…[truncated 3445 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-22T01:10:45.174084+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/results/libero_goal -maxdepth 1 -name \"counterfactual_combined.json\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/results/libero_goal -maxdepth 1 -name \"counterfactual_combined.json\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-22T01:10:45.174248+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T01:10:45.174372+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/results -maxdepth 1 -type d -name \"*goal*untrained*\" -o -name \"*spatial*untrained*\" -o -name \"*untrained*goal*\" -o -name \"*untrained*spatial*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/results -maxdepth 1 -type d -name \"*goal*untrained*\" -o -name \"*spatial*untrained*\" -o -name \"*untrained*goal*\" -o -name \"*untrained*spatial*\""
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-22T01:10:45.174500+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/vla-ssd/results/untrained_libero_goal\\n/root/autodl-tmp/vla-ssd/results/untrained_libero_goal_frame0\\n/root/autodl-tmp/vla-ssd/results/untrained_libero_goal_linear\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-22T01:10:45.174635+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/results -maxdepth 1 -type d -name \"*spatial*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/results -maxdepth 1 -type d -name \"*spatial*\""
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-22T01:10:45.174763+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/vla-ssd/results/cross_instruction_spatial\\n/root/autodl-tmp/vla-ssd/results/nora_spatial\\n/root/autodl-tmp/vla-ssd/results/counterfactual_spatial\\n/root/autodl-tmp/vla-ssd/results/tracvla_spatial\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-22T01:10:45.174894+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/results/untrained_libero_goal /root/autodl-tmp/vla-ssd/results/untrained_libero_goal_frame0 /root/autodl-tmp/vla-ssd/results/untrained_libero_goal_linear -maxdepth 1 -name \"*.json\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/results/untrained_libero_goal /root/autodl-tmp/vla-ssd/results/untrained_libero_goal_frame0 /root/autodl-tmp/vla-ssd/results/untrained_libero_goal_linear -maxdepth 1 -name \"*.json\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-22T01:10:45.175098+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-22T01:10:45.175226+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/results -maxdepth 1 -type d -name \"*openvla*\" -o -name \"*libero_spatial*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/results -maxdepth 1 -type d -name \"*openvla*\" -o -name \"*libero_spatial*\""
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-22T01:10:45.175344+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-22T01:10:45.175501+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/results/cross_instruction_spatial /root/autodl-tmp/vla-ssd/results/counterfactual_spatial -maxdepth 1 -name \"*.json\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/results/cross_instruction_spatial /root/autodl-tmp/vla-ssd/results/counterfactual_spatial -maxdepth 1 -name \"*.json\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-22T01:10:45.175667+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/vla-ssd/results/cross_instruction_spatial/classification_results.json\\n/root/autodl-tmp/vla-ssd/results/counterfactual_spatial/counterfactual_wrong.json\\n/root/autodl-tmp/vla-ssd/results/counterfactual_spatial/counterfactual_empty.json\\n/root/autodl-tmp/vla-ssd/results/counterfactual_spatial/counterfactual_shuffled.json\\n/root/autodl-tmp/vla-ssd/results/counterfactual_spatial/counterfactual_paraphrased.json\\n/root/autodl-tmp/vla-ssd/results/counterfactual_spatial/counterfactual_correct.json\\n/root/autodl-tmp/vla-ssd/results/counterfactual_spatial/counterfactual_spatial_combined.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-22T01:10:45.175793+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/results -maxdepth 1 -type d -name \"nora_object\" -o -name \"nora_long\" -o -name \"nora_object*\" -o -name \"nora_long*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/results -maxdepth 1 -type d -name \"nora_object\" -o -name \"nora_long\" -o -name \"nora_object*\" -o -name \"nora_long*\""
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-22T01:10:45.175917+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/results/trained /root/autodl-tmp/vla-ssd/results/untrained -maxdepth 1 -name \"*.json\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/results/trained /root/autodl-tmp/vla-ssd/results/untrained -maxdepth 1 -name \"*.json\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-22T01:10:45.176062+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-22T01:10:45.176177+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-22T01:10:45.176302+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls /root/autodl-tmp/vla-ssd/results/trained/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls /root/autodl-tmp/vla-ssd/results/trained/"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-22T01:10:45.176418+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"action_delta\\naction_prediction\\ntemporal_distance\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-22T01:10:45.176529+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls /root/autodl-tmp/vla-ssd/results/untrained/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls /root/autodl-tmp/vla-ssd/results/untrained/"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-22T01:10:45.176640+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"action_delta\\naction_prediction\\ntemporal_distance\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-22T01:10:45.176750+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/results/trained_libero_goal /root/autodl-tmp/vla-ssd/results/trained_libero_goal_frame0 /root/autodl-tmp/vla-ssd/results/trained_libero_goal_linear /root/autodl-tmp/vla-ssd/results/trained_libero_goal_pca1024 -maxdepth 1 -name \"*.json\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/results/trained_libero_goal /root/autodl-tmp/vla-ssd/results/trained_libero_goal_frame0 /root/autodl-tmp/vla-ssd/results/trained_libero_goal_linear /root/autodl-tmp/vla-ssd/results/trained_libero_goal_pca1024 -maxdepth 1 -name \"*.json\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-22T01:10:45.176864+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-22T01:10:45.177125+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/269b335b-8109-4887-9807-ef7e6258fc6a/tool-results/mcp-agent-ml-research-read_registry-1779412036807.txt') as f:\n    raw = json.load(f)\ndata = json.loads(raw['result'])\nexps = data['data']['experiments']\n# Get details for specific experiments\nfor eid in ['cf_batch_missing_v1', 'openvla_goal_standardized_v1', 'openvla_spatial_standardized_v1', 'openvla_long_pipeline_v1', 'openvla_long_cf_trained', 'openvla_long_untrained_v1', 'nora_spatial_pipeline_v2']:\n    e = exps.get(eid, {})\n    if isinstance(e, dict):\n        print(f'=== {eid} ===')\n        print(f'  status: {e.get(\\\"status\\\")}')\n        print(f'  conclusion: {e.get(\\\"conclusion\\\", \\\"\\\")}')\n        h = e.get('hypothesis', '')\n        if h:\n            print(f'  hypothesis: {h[:200]}')\n        spec = e.get('spec', {})\n        if spec and isinstance(spec, dict):\n            print(f'  checkpoint_path: {spec.get(\\\"checkpoint_path\\\", \\\"\\\")[:200]}')\n        print()\n\" 2>&1",
  "description": "Get details for key registry experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/269b335b-8109-4887-9807-ef7e6258fc6a/tool-results/mcp-agent-ml-research-read_registry-1779412036807.txt') as f:\n    raw = json.load(f)\ndata = json.loads(raw['result'])\nexps = data['data']['experiments']\n# Get details for specific experiments\nfor eid in ['cf_batch_missing_v1', 'openvla_goal_standardized_v1', 'openvla_spatial_standardized_v1', 'openvla_long_pipeline_v1', 'openvla_long_cf_trained', 'openvla_long_untrained_v1', 'nora_spatial_pipeline_v2']:\n    e = exps.get(eid, {})\n    if isinstance(e, dict):\n        print(f'=== {eid} ===')\n        print(f'  status: {e.get(\\\"status\\\")}')\n        print(f'  conclusion: {e.get(\\\"conclusion\\\", \\\"\\\")}')\n        h = e.get('hypothesis', '')\n        if h:\n            print(f'  hypothesis: {h[:200]}')\n        spec = e.get('spec', {})\n        if spec and isinstance(spec, dict):\n            print(f'  checkpoint_path: {spec.get(\\\"checkpoint_path\\\", \\\"\\\")[:200]}')\n        print()\n\" 2>&1",
    "description": "Get details for key registry experiments"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-22T01:10:45.177340+00:00_

=== cf_batch_missing_v1 ===
  status: RUNNING
  conclusion: 
  hypothesis: Batch counterfactual补跑：filling missing untrained CF cells in 3×4 matrix using cosine_dist method. Covers: openvla object untrained, tracvla spatial/object/goal/long untrained. cosine_dist compares hid
  checkpoint_path: 

=== openvla_goal_standardized_v1 ===
  status: RUNNING
  conclusion: 
  hypothesis: OpenVLA (Llama-2-7B backbone) on LIBERO-Goal standardized 5-phase pipeline (R² probing, L1 attention, cross-instruction, RSA, counterfactual). Both trained (openvla-7b-finetuned-libero-goal) and untra
  checkpoint_path: N/A (probing experiment)

=== openvla_spatial_standardized_v1 ===
  status: PREPARING
  conclusion: 
  hypothesis: OpenVLA (Llama-2-7B backbone) on LIBERO-Spatial standardized 5-phase pipeline (R² probing, L1 attention, cross-instruction classification, RSA, counterfactual). Both trained and untrained conditions. 

=== openvla_long_pipeline_v1 ===
  status: DONE
  conclusion: failed
  hypothesis: The convergent entry-exit routing architecture (inverted-U R² profile, instruction-dominant L1 heads, counterfactual sensitivity) observed in OpenVLA on LIBERO-Goal/Spatial/Object generalizes to LIBER
  checkpoint_path: 

=== openvla_long_cf_trained ===
  status: DONE
  conclusion: success
  hypothesis: OpenVLA Long (OFT fine-tuned) trained counterfactual sensitivity — completing the missing CF phase from openvla_long_pipeline_v1 after unnorm_key bug fix. Tests whether counterfactual ordering (empty>
  checkpoint_path: /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-oft-finetuned-libero-10

=== openvla_long_untrained_v1 ===
  status: DONE
  conclusion: success
  hypothesis: OpenVLA (openvla-7b, OXE pretrained but not LIBERO fine-tuned) untrained baseline on LIBERO-Long — full 5-phase pipeline. Tests whether the convergent routing pattern (R² exit collapse, L1 mixed heads
  checkpoint_path: N/A (probing experiment)

=== nora_spatial_pipeline_v2 ===
  status: DONE
  conclusion: success

…[truncated 280 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-22T01:10:45.177543+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-22T01:10:45.177673+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-22T01:10:45.177828+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "matrix_result_audit_20260522",
  "type": "report",
  "description": "5-phase pipeline result file completeness audit across 3×4×2 (arch×suite×condition) matrix, cross-checked with registry",
  "project": "vla-ssd",
  "content_filename": "matrix_result_audit_20260522.md",
  "tags": "['audit', 'results', 'completeness']",
  "content": "# 5-Phase Pipeline Result Audit — 2026-05-22\n\n## Phase Legend\n\n| Short | File | Phase |\n|-------|------|-------|\n| R² | `action_r2_probing.json` | Action R² probing |\n| L1 | `l1_attention_profile.json` | L1 attention profile |\n| CI | `cross_instruction_classification.json` | Cross-instruction classification |\n| RSA | `rsa_analysis.json` | RSA analysis |\n| CF | `counterfactual_combined.json` | Counterfactual sensitivity |\n\n---\n\n## Completeness Matrix\n\n### OpenVLA (Llama-2-7B backbone)\n\n| Suite | Condition | Directory | R² | L1 | CI | RSA | CF | Score |\n|-------|-----------|-----------|:--:|:--:|:--:|:---:|:--:|:-----:|\n| **Goal** | trained | `libero_goal/` | ✅ | ✅ | ✅ | ✅ | ❌ | **4/5** |\n| **Goal** | untrained | _(no standardized dir)_ | ❌ | ❌ | ❌ | ❌ | ❌ | **0/5** |\n| **Spatial** | trained | _(no standardized dir)_ | ❌ | ❌ | ❌ | ❌ | ❌ | **0/5** |\n| **Spatial** | untrained | _(no standardized dir)_ | ❌ | ❌ | ❌ | ❌ | ❌ | **0/5** |\n| **Object** | trained | `libero_object/` | ✅ | ✅ | ✅ | ✅ | ✅ | **5/5** |\n| **Object** | untrained | `libero_object_untrained/` | ✅ | ✅ | ✅ | ✅ | ✅ | **5/5** |\n| **Long** | trained | `libero_long/` | ✅ | ✅ | ✅ | ✅ | ✅ | **5/5** |\n| **Long** | untrained | `libero_long_untrained/` | ✅ | ✅ | ✅ | ✅ | ✅ | **5/5** |\n\n### TracVLA (Phi-3-Vision backbone)\n\n| Suite | Condition | Directory | R² | L1 | CI | RSA | CF | Score |\n|-------|-----------|-----------|:--:|:--:|:--:|:---:|:--:|:-----:|\n| **Goal** | trained | `tracvla_goal/trained/` | ✅ | ✅ | ✅ | ❌ | ✅ | **4/5** |\n| **Goal** | untrained | `tracvla_goal/untrained/` | ✅ | ✅ | ✅ | ❌ | ✅ | **4/5** |\n| **Spatial** | trained | `tracvla_spatial/trained/` | ✅ | ✅ | ✅ | ❌ | ✅ | **4/5** |\n| **Spatial** | untrained | `tracvla_spatial/untrained/` | ✅ | ✅ | ✅ | ❌ | ✅ | **4/5** |\n| **Object** | trained | `tracvla_object/trained/` | ✅ | ✅ | ✅ | ❌ | ✅ | **4/5** |\n| **Object** | untrained | `tracvla_object/untrained/` | ✅ | ✅ | ✅ | ❌ | ✅ | **4/5** |\n| **Long** | trained | `tracvla_long/trained/` | ✅ | ✅ | ✅ | ❌ | ✅ | **4/5** |\n| **Long** | untrained | `tracvla_long/untrained/` | ✅ | ✅ | ✅ | ❌ | ✅ | **4/5** |\n\n### NORA\n\n| Suite | Condition | Directory | R² | L1 | CI | RSA | CF | Score |\n|-------|-----------|-----------|:--:|:--:|:--:|:---:|:--:|:-----:|\n| **Goal** | trained | `nora_goal/trained/` | ✅ | ✅ | ✅ | ❌ | ✅ | **4/5** |\n| **Goal** | untrained | `nora_goal/untrained/` | ✅ | ✅ | ✅ | ❌ | ✅ | **4/5** |\n| **Spatial** | trained | `nora_spatial/trained/` | ✅ | ✅ | ✅ | ❌ | ✅ | **4/5** |\n| **Spatial** | untrained | `nora_spatial/untrained/` | ✅ | ✅ | ✅ | ❌ | ❌ | **3/5** |\n| **Object** | trained | _(no dir)_ | ❌ | ❌ | ❌ | ❌ | ❌ | **0/5** |\n| **Object** | untrained | _(no dir)_ | ❌ | ❌ | ❌ | ❌ | ❌ | **0/5** |\n| **Long** | trained | _(no dir)_ | ❌ | ❌ | ❌ | ❌ | ❌ | **0/5** |\n| **Long** | untrained | _(no dir)_ | ❌ | ❌ | ❌ | ❌ | ❌ | **0/5** |\n\n---\n\n## Aggregate Summary\n\n| Metric | Count |\n|--------|-------|\n| Total cells (3 arch × 4 suite × 2 condition) | **24** |\n| Complete (5/5) | **4** — OpenVLA Object (T+U), Long (T+U) |\n| Partial (3–4/5) | **13** |\n| Empty (0/5) | **7** — OpenVLA Goal-U, Spatial (T+U); NORA Object (T+U), Long (T+U) |\n| Total files present | **95 / 120** |\n| Total files missing | **25** |\n\n### Missing phases breakdown\n\n| Missing Phase | Affected Cells | Count |\n|---------------|----------------|-------|\n| **RSA** | All 8 TracVLA + all 4 NORA cells | **12** |\n| **CF** | OpenVLA Goal-trained, NORA Spatial-untrained | **2** |\n| **All 5 phases** | OpenVLA Goal-U, Spatial-T/U; NORA Object-T/U, Long-T/U | **7 cells × 5 = 35 missing files** |\n\n---\n\n## Registry Cross-Check\n\n### Registry DONE/success but server files incomplete\n\n| exp_id | Registry Status | Issue on Server |\n|--------|----------------|-----------------|\n| `nora_spatial_pipeline_v2` | DONE / success | `nora_spatial/untrained/` missing CF (3/5 not 5/5) |\n\n### Server has results but no corresponding single registry entry\n\nThe following directories have complete/near-complete results assembled from multiple legacy experiments rather than a single pipeline run:\n- `libero_goal/` — 4/5 files from multiple older experiments (no single \"openvla_goal\" registry entry with conclusion=success)\n- `libero_object/` + `libero_object_untrained/` — assembled across `object_pipeline_ridge_v2`, `object_untrained_pipeline_v1`, etc.\n- `libero_long/` + `libero_long_untrained/` — assembled from `openvla_long_pipeline_v1` (failed) + `openvla_long_cf_trained` (success) + `openvla_long_untrained_v1` (success)\n\n### In-progress experiments filling gaps\n\n| exp_id | Status | Target Gaps |\n|--------|--------|-------------|\n| `openvla_goal_standardized_v1` | **RUNNING** | OpenVLA Goal trained + untrained (all 5 phases) |\n| `openvla_spatial_standardized_v1` | **PREPARING** | OpenVLA Spatial trained + untrained (all 5 phases) |\n| `cf_batch_missing_v1` | **RUNNING** | Untrained CF for multiple cells (openvla object untrained, tracvla spatial/object/goal/long untrained) |\n\n---\n\n## Legacy / Non-Standard Data\n\nThese directories contain related data in older formats, **not** in the standardized 5-phase structure:\n\n| Directory | Contents | Notes |\n|-----------|----------|-------|\n| `cross_instruction_spatial/` | `classification_results.json` | OpenVLA Spatial CI (legacy format) |\n| `counterfactual_spatial/` | 6 files (per-condition + combined) | OpenVLA Spatial CF (legacy format) |\n| `trained/`, `untrained/` (top-level) | `action_delta/`, `action_prediction/`, `temporal_distance/` | Old probe format (pre-standardization) |\n| `trained_libero_goal/`, `untrained_libero_goal/` | Empty (0 json files) | Abandoned directories |\n| `dinov2/`, `dinov2_libero_goal*/`, `oracle/`, etc. | Various old baselines | Control experiments, not part of 3×4 matrix |\n\n---\n\n## Critical Gaps Requiring Action\n\n### Priority 1: Entire cells missing (0/5)\n1. **OpenVLA Spatial** (trained + untrained) — `openvla_spatial_standardized_v1` in PREPARING, needs to start\n2. **NORA Object** (trained + untrained) — no experiment registered\n3. **NORA Long** (trained + untrained) — no experiment registered\n\n### Priority 2: Phase gaps in otherwise-populated cells\n4. **RSA missing across all TracVLA (8 cells) and all NORA (4 cells)** — systematic gap, 12 cells affected\n5. **OpenVLA Goal trained** — missing CF only (1 file); `openvla_goal_standardized_v1` RUNNING should fill this\n6. **OpenVLA Goal untrained** — `openvla_goal_standardized_v1` RUNNING should create this entire cell\n7. **NORA Spatial untrained** — missing CF (registry says success but file absent)\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "matrix_result_audit_20260522",
    "type": "report",
    "description": "5-phase pipeline result file completeness audit across 3×4×2 (arch×suite×condition) matrix, cross-checked with registry",
    "project": "vla-ssd",
    "content_filename": "matrix_result_audit_20260522.md",
    "tags": "['audit', 'results', 'completeness']",
    "content": "# 5-Phase Pipeline Result Audit — 2026-05-22\n\n## Phase Legend\n\n| Short | File | Phase |\n|-------|------|-------|\n| R² | `action_r2_probing.json` | Action R² probing |\n| L1 | `l1_attention_profile.json` | L1 attention profile |\n| CI | `cross_instruction_classification.json` | Cross-instruction classification |\n| RSA | `rsa_analysis.json` | RSA analysis |\n| CF | `counterfactual_combined.json` | Counterfactual sensitivity |\n\n---\n\n## Completeness Matrix\n\n### OpenVLA (Llama-2-7B backbone)\n\n| Suite | Condition | Directory | R² | L1 | CI | RSA | CF | Score |\n|-------|-----------|-----------|:--:|:--:|:--:|:---:|:--:|:-----:|\n| **Goal** | trained | `libero_goal/` | ✅ | ✅ | ✅ | ✅ | ❌ | **4/5** |\n| **Goal** | untrained | _(no standardized dir)_ | ❌ | ❌ | ❌ | ❌ | ❌ | **0/5** |\n| **Spatial** | trained | _(no standardized dir)_ | ❌ | ❌ | ❌ | ❌ | ❌ | **0/5** |\n| **Spatial** | untrained | _(no standardized dir)_ | ❌ | ❌ | ❌ | ❌ | ❌ | **0/5** |\n| **Object** | trained | `libero_object/` | ✅ | ✅ | ✅ | ✅ | ✅ | **5/5** |\n| **Object** | untrained | `libero_object_untrained/` | ✅ | ✅ | ✅ | ✅ | ✅ | **5/5** |\n| **Long** | trained | `libero_long/` | ✅ | ✅ | ✅ | ✅ | ✅ | **5/5** |\n| **Long** | untrained | `libero_long_untrained/` | ✅ | ✅ | ✅ | ✅ | ✅ | **5/5** |\n\n### TracVLA (Phi-3-Vision backbone)\n\n| Suite | Condition | Directory | R² | L1 | CI | RSA | CF | Score |\n|-------|-----------|-----------|:--:|:--:|:--:|:---:|:--:|:-----:|\n| **Goal** | trained | `tracvla_goal/trained/` | ✅ | ✅ | ✅ | ❌ | ✅ | **4/5** |\n| **Goal** | untrained | `tracvla_goal/untrained/` | ✅ | ✅ | ✅ | ❌ | ✅ | **4/5** |\n| **Spatial** | trained | `tracvla_spatial/trained/` | ✅ | ✅ | ✅ | ❌ | ✅ | **4/5** |\n| **Spatial** | untrained | `tracvla_spatial/untrained/` | ✅ | ✅ | ✅ | ❌ | ✅ | **4/5** |\n| **Object** | trained | `tracvla_object/trained/` | ✅ | ✅ | ✅ | ❌ | ✅ | **4/5** |\n| **Object** | untrained | `tracvla_object/untrained/` | ✅ | ✅ | ✅ | ❌ | ✅ | **4/5** |\n| **Long** | trained | `tracvla_long/trained/` | ✅ | ✅ | ✅ | ❌ | ✅ | **4/5** |\n| **Long** | untrained | `tracvla_long/untrained/` | ✅ | ✅ | ✅ | ❌ | ✅ | **4/5** |\n\n### NORA\n\n| Suite | Condition | Directory | R² | L1 | CI | RSA | CF | Score |\n|-------|-----------|-----------|:--:|:--:|:--:|:---:|:--:|:-----:|\n| **Goal** | trained | `nora_goal/trained/` | ✅ | ✅ | ✅ | ❌ | ✅ | **4/5** |\n| **Goal** | untrained | `nora_goal/untrained/` | ✅ | ✅ | ✅ | ❌ | ✅ | **4/5** |\n| **Spatial** | trained | `nora_spatial/trained/` | ✅ | ✅ | ✅ | ❌ | ✅ | **4/5** |\n| **Spatial** | untrained | `nora_spatial/untrained/` | ✅ | ✅ | ✅ | ❌ | ❌ | **3/5** |\n| **Object** | trained | _(no dir)_ | ❌ | ❌ | ❌ | ❌ | ❌ | **0/5** |\n| **Object** | untrained | _(no dir)_ | ❌ | ❌ | ❌ | ❌ | ❌ | **0/5** |\n| **Long** | trained | _(no dir)_ | ❌ | ❌ | ❌ | ❌ | ❌ | **0/5** |\n| **Long** | untrained | _(no dir)_ | ❌ | ❌ | ❌ | ❌ | ❌ | **0/5** |\n\n---\n\n## Aggregate Summary\n\n| Metric | Count |\n|--------|-------|\n| Total cells (3 arch × 4 suite × 2 condition) | **24** |\n| Complete (5/5) | **4** — OpenVLA Object (T+U), Long (T+U) |\n| Partial (3–4/5) | **13** |\n| Empty (0/5) | **7** — OpenVLA Goal-U, Spatial (T+U); NORA Object (T+U), Long (T+U) |\n| Total files present | **95 / 120** |\n| Total files missing | **25** |\n\n### Missing phases breakdown\n\n| Missing Phase | Affected Cells | Count |\n|---------------|----------------|-------|\n| **RSA** | All 8 TracVLA + all 4 NORA cells | **12** |\n| **CF** | OpenVLA Goal-trained, NORA Spatial-untrained | **2** |\n| **All 5 phases** | OpenVLA Goal-U, Spatial-T/U; NORA Object-T/U, Long-T/U | **7 cells × 5 = 35 missing files** |\n\n---\n\n## Registry Cross-Check\n\n### Registry DONE/success but server files incomplete\n\n| exp_id | Registry Status | Issue on Server |\n|--------|----------------|-----------------|\n| `nora_spatial_pipeline_v2` | DONE / success | `nora_spatial/untrained/` missing CF (3/5 not 5/5) |\n\n### Server has results but no corresponding single registry entry\n\nThe following directories have complete/near-complete results assembled from multiple legacy experiments rather than a single pipeline run:\n- `libero_goal/` — 4/5 files from multiple older experiments (no single \"openvla_goal\" registry entry with conclusion=success)\n- `libero_object/` + `libero_object_untrained/` — assembled across `object_pipeline_ridge_v2`, `object_untrained_pipeline_v1`, etc.\n- `libero_long/` + `libero_long_untrained/` — assembled from `openvla_long_pipeline_v1` (failed) + `openvla_long_cf_trained` (success) + `openvla_long_untrained_v1` (success)\n\n### In-progress experiments filling gaps\n\n| exp_id | Status | Target Gaps |\n|--------|--------|-------------|\n| `openvla_goal_standardized_v1` | **RUNNING** | OpenVLA Goal trained + untrained (all 5 phases) |\n| `openvla_spatial_standardized_v1` | **PREPARING** | OpenVLA Spatial trained + untrained (all 5 phases) |\n| `cf_batch_missing_v1` | **RUNNING** | Untrained CF for multiple cells (openvla object untrained, tracvla spatial/object/goal/long untrained) |\n\n---\n\n## Legacy / Non-Standard Data\n\nThese directories contain related data in older formats, **not** in the standardized 5-phase structure:\n\n| Directory | Contents | Notes |\n|-----------|----------|-------|\n| `cross_instruction_spatial/` | `classification_results.json` | OpenVLA Spatial CI (legacy format) |\n| `counterfactual_spatial/` | 6 files (per-condition + combined) | OpenVLA Spatial CF (legacy format) |\n| `trained/`, `untrained/` (top-level) | `action_delta/`, `action_prediction/`, `temporal_distance/` | Old probe format (pre-standardization) |\n| `trained_libero_goal/`, `untrained_libero_goal/` | Empty (0 json files) | Abandoned directories |\n| `dinov2/`, `dinov2_libero_goal*/`, `oracle/`, etc. | Various old baselines | Control experiments, not part of 3×4 matrix |\n\n---\n\n## Critical Gaps Requiring Action\n\n### Priority 1: Entire cells missing (0/5)\n1. **OpenVLA Spatial** (trained + untrained) — `openvla_spatial_standardized_v1` in PREPARING, needs to start\n2. **NORA Object** (trained + untrained) — no experiment registered\n3. **NORA Long** (trained + untrained) — no experiment registered\n\n### Priority 2: Phase gaps in otherwise-populated cells\n4. **RSA missing across all TracVLA (8 cells) and all NORA (4 cells)** — systematic gap, 12 cells affected\n5. **OpenVLA Goal trained** — missing CF only (1 file); `openvla_goal_standardized_v1` RUNNING should fill this\n6. **OpenVLA Goal untrained** — `openvla_goal_standardized_v1` RUNNING should create this entire cell\n7. **NORA Spatial untrained** — missing CF (registry says success but file absent)\n"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-22T01:10:45.178149+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260522_b7e2e9\", \"name\": \"matrix_result_audit_20260522\", \"type\": \"report\", \"description\": \"5-phase pipeline result file completeness audit across 3×4×2 (arch×suite×condition) matrix, cross-checked with registry\", \"path\": \"projects/vla-ssd/artifacts/_project/report/matrix_result_audit_20260522.md\", \"url\": null, \"project\": \"vla-ssd\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-22T01:10:37.174908+00:00\", \"tags\": [\"audit\", \"results\", \"completeness\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_matrix_result_audit_20260522T010700",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-22T01:10:45.178383+00:00_

审计完成。报告已写入 `artifacts/_project/report/matrix_result_audit_20260522.md`。

核心发现：

**24 个 cell 中：4 个完整 (5/5)，13 个部分完成，7 个完全缺失。**

关键问题：

1. **RSA 系统性缺失** — 所有 TracVLA (8 cells) 和所有 NORA (4 cells) 均无 `rsa_analysis.json`，共 12 个 cell 受影响
2. **整 cell 缺失** — OpenVLA Spatial (T+U)、NORA Object (T+U)、NORA Long (T+U) 共 7 个 cell 为 0/5
3. **Registry 不一致** — `nora_spatial_pipeline_v2` 标记 success 但 untrained CF 文件实际缺失
4. **正在补跑** — `openvla_goal_standardized_v1` (RUNNING) 和 `openvla_spatial_standardized_v1` (PREPARING) 正在填补 OpenVLA Goal/Spatial 缺口；NORA Object/Long 尚无任何实验注册

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ssh_matrix_result_audit_20260522T010700"
}
```

</details>

---
