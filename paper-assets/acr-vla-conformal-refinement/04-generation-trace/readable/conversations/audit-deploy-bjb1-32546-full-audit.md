# audit deploy bjb1 32546 full audit

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 69
- **Recorded user turns:** 0
- **Tool calls:** 34
- **Original source:** `logs/chats/worker_audit-deploy_bjb1-32546-full-audit_20260523T101221.jsonl`
- **Structured JSON:** [`9a25196867d0e97d25f9.json`](../../sessions/9a/9a25196867d0e97d25f9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

69 recorded events

### Tool call

_source line 1 · 2026-05-23T10:17:41.082339+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__detect_image",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__detect_image",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T10:17:41.082796+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T10:17:41.083036+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "nvidia-smi --query-gpu=index,utilization.gpu,memory.used,memory.total --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "nvidia-smi --query-gpu=index,utilization.gpu,memory.used,memory.total --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T10:17:41.083251+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 21 %, 2848 MiB, 24564 MiB\\n1, 29 %, 2448 MiB, 24564 MiB\\n2, 22 %, 2354 MiB, 24564 MiB\\n3, 24 %, 5607 MiB, 24564 MiB\\n4, 37 %, 2942 MiB, 24564 MiB\\n5, 20 %, 3257 MiB, 24564 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T10:17:41.083491+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T10:17:41.083714+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"818121, GPU-220671b6-4e9c-db2d-1361-6ed090a1f3af, 2828 MiB\\n818386, GPU-ade291cb-7e13-f292-1714-09ef80919436, 2429 MiB\\n818658, GPU-4f00bf04-f4ff-96b6-3f56-723337f44abf, 2335 MiB\\n848576, GPU-00ae24f3-53b1-cd05-f561-fe7adbb64e72, 5587 MiB\\n818928, GPU-563702d3-df96-d375-0303-c9b9f202bdd2, 2922 MiB\\n835200, GPU-6d1331f1-8f19-df6c-71d5-e8ca2f3e2178, 3238 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T10:17:41.083918+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ps aux --no-headers -o pid,cmd --sort=-start_time",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "ps aux --no-headers -o pid,cmd --sort=-start_time",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T10:17:41.084122+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"error: conflicting format options\\n\\nUsage:\\n ps [options]\\n\\n Try 'ps --help &lt;simple|list|output|threads|misc|all>'\\n  or 'ps --help &lt;s|l|o|t|m|a>'\\n for additional help text.\\n\\nFor more details see ps(1).\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T10:17:41.084361+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'server': 'bjb1-32546'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'server': 'bjb1-32546'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T10:17:41.085136+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-obs-only-object-norm005-seed67\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:35:00.000Z\", \"updated_at\": \"2026-05-21T04:50:15.572Z\", \"hypothesis\": \"CRM obs_only (ε=0.05) K=10 on LIBERO-Object seed67. Norm sweep seed balance for ε=0.05.\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:2\", \"pid\": 805840, \"seed\": 67, \"spec\": {\"command\": \"detected on GPU, submitted by prior Worker but not registered\", \"server\": \"bjb1-32546\", \"data_path\": \"/root/autodl-tmp/acr-vla-conformal-refinement/\", \"data_count\": \"100 rollouts\", \"model_name\": \"crm_v3_norm/obs_only\", \"seed\": 67, \"gpu\": \"cuda:2\"}, \"reproduce\": {\"finished_at\": \"2026-05-21T04:43:57.464Z\"}, \"failure_reason\": \"null - completed successfully, SR=10.0%\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T04:44:08.410Z\", \"metrics\": {\"overall_success_rate\": 0.1}, \"notes\": \"监控误报为 failed。实际正常完成 SR=10.0% (10/100)。JSON: /root/logs/eval_object_crm_obs_only_norm0.05_seed67.json (bjb1-32546，注意保存在 /root/logs/ 而非项目 logs/)。日志: /root/autodl-tmp/logs/norm005_seed67.log。\"}, \"eval-obs-only-object-norm003-seed45\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-18T15:16:07.852Z\", \"updated_at\": \"2026-05-21T03:28:51.768Z\", \"hypothesis\": \"obs_only CRM (ε=0.03) seed45 on LIBERO-Object. 补 magnitude curve 最薄数据点：obs_only ε=0.03 当前 n=1，seed43/44 已在跑。第 4 个 seed 确保极低 norm 端有可靠 error bars。\", \"server\": \"bjb1-32546\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-32546\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-18T15:16:41.398Z\", \"command\": \"cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 45 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_ob
…[truncated 22092 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T10:17:41.085485+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "tmux ls",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "tmux ls",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T10:17:41.085700+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'tmux' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T10:17:41.085894+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "ps -p 818121,818386,818658,818928,848576,835200 -o pid,etimes,cmd --no-headers",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "ps -p 818121,818386,818658,818928,848576,835200 -o pid,etimes,cmd --no-headers",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T10:17:41.086098+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"818121    5577 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2\\n818386    5574 python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.05\\n818658    5571 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2\\n818928    5569 python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.05\\n835200    4094 python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark goal --seed 44 --n_rollouts 20 --max_correction_norm 0.2 --K 2\\n848576    2865 python -u src/evaluate.py --mode vla_only --benchmark long --seed 42 --n_rollouts 20\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T10:17:41.086401+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'status': 'RUNNING'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'status': 'RUNNING'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-23T10:17:41.086617+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'status': 'PREPARING'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'status': 'PREPARING'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-23T10:17:41.087025+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-supp-k2mean-goal-s42-r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T08:33:20.623Z\", \"updated_at\": \"2026-05-23T10:10:52.074Z\", \"spec\": {\"command\": \"python src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --benchmark goal --n_rollouts 20 --seed 42\", \"server\": \"bjb2-40593\", \"data_path\": \"/root/acr-vla-conformal-refinement/src/evaluate.py\", \"data_count\": 20, \"model_name\": \"smolvla\", \"seed\": 42, \"checkpoint_source\": \"eval-supp-k2mean-goal-s42\", \"eval_data\": \"goal\"}, \"hypothesis\": \"K=2 mean baseline on Goal seed42 (retry). Goal VLA-only baseline = 83.5%. Isolates multi-sample averaging effect on Goal tasks.\"}, \"eval-supp-k2mean-goal-s43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T07:38:57.518Z\", \"updated_at\": \"2026-05-23T10:10:46.253Z\", \"hypothesis\": \"K=2 mean baseline on Goal seed43. Goal VLA-only baseline = 83.5%. Isolates multi-sample averaging effect on Goal tasks. Second seed for 3-seed mean±std.\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=4 python src/evaluate.py --mode vla_only --baseline_mode mean --K 2 --suite goal --n_rollouts 20 --seed 43\", \"server\": \"cqa1-32758\", \"data_path\": \"/root/acr-vla-conformal-refinement\", \"data_count\": 200, \"model_name\": \"smolvla\", \"seed\": 43, \"checkpoint_source\": \"n/a\", \"eval_data\": \"LIBERO-Goal\", \"gpu\": \"cuda:4\", \"pid\": 16445}}, \"eval-supp-goal-reconvla-s43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T08:19:47.656Z\", \"updated_at\": \"2026-05-23T10:10:40.768Z\", \"hypothesis\": \"Reconvla K=10 argmin on Goal seed43. Goal VLA-only baseline = 83.5%. s42=81.0% (-2.5pp negative). Second seed for Goal reconvla multi-seed validation.\", \"spec\": {\"command\": \"sourc
…[truncated 6473 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T10:17:41.087893+00:00_

Error: result (92,054 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/4294b235-1b87-40b4-afe2-9e7ed46ec777/tool-results/mcp-agent-ml-research-read_registry-1779531206092.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/4294b235-1b87-40b4-afe2-9e7ed46ec777/tool-results/mcp-agent-ml-research-read_registry-1779531206092.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/4294b235-1b87-40b4-afe2-9e7ed46ec777/tool-results/mcp-agent-ml-research-read_registry-1779531206092.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T10:17:41.088251+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_registry",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__update_registry",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T10:17:41.088499+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T10:17:41.088772+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-obj-s43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2', 'server': 'bjb1-32546', 'gpu_ids': ['cuda:0'], 'pid': 818121, 'seed': 43, 'model_name': 'smolvla+crm_adaptive_tau025', 'data_path': 'LIBERO-Object', 'data_count': 200, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Object'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau025-obj-s43",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2', 'server': 'bjb1-32546', 'gpu_ids': ['cuda:0'], 'pid': 818121, 'seed': 43, 'model_name': 'smolvla+crm_adaptive_tau025', 'data_path': 'LIBERO-Object', 'data_count': 200, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Object'}"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-23T10:17:41.089002+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-goal-s43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.05', 'server': 'bjb1-32546', 'gpu_ids': ['cuda:1'], 'pid': 818386, 'seed': 43, 'model_name': 'smolvla+crm_obs_only_norm005', 'data_path': 'LIBERO-Goal', 'data_count': 200, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Goal'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-goal-s43",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.05', 'server': 'bjb1-32546', 'gpu_ids': ['cuda:1'], 'pid': 818386, 'seed': 43, 'model_name': 'smolvla+crm_obs_only_norm005', 'data_path': 'LIBERO-Goal', 'data_count': 200, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Goal'}"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T10:17:41.089250+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-goal-s43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2', 'server': 'bjb1-32546', 'gpu_ids': ['cuda:2'], 'pid': 818658, 'seed': 43, 'model_name': 'smolvla+crm_adaptive_tau025', 'data_path': 'LIBERO-Goal', 'data_count': 200, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Goal'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau025-goal-s43",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2', 'server': 'bjb1-32546', 'gpu_ids': ['cuda:2'], 'pid': 818658, 'seed': 43, 'model_name': 'smolvla+crm_adaptive_tau025', 'data_path': 'LIBERO-Goal', 'data_count': 200, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Goal'}"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-23T10:17:41.089510+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-obj-s43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.05', 'server': 'bjb1-32546', 'gpu_ids': ['cuda:4'], 'pid': 818928, 'seed': 43, 'model_name': 'smolvla+crm_obs_only_norm005', 'data_path': 'LIBERO-Object', 'data_count': 200, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Object'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-obj-s43",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.05', 'server': 'bjb1-32546', 'gpu_ids': ['cuda:4'], 'pid': 818928, 'seed': 43, 'model_name': 'smolvla+crm_obs_only_norm005', 'data_path': 'LIBERO-Object', 'data_count': 200, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Object'}"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-23T10:17:41.089738+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 11.3965}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-23T10:17:41.089941+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 3.3328}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-23T10:17:41.090140+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 10.1165}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-23T10:17:41.090356+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 3.0729}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-23T10:17:41.090643+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-obj-s43",
  "field": "status",
  "value": "PENDING",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau025-obj-s43",
    "field": "status",
    "value": "PENDING",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-23T10:17:41.090849+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-goal-s43",
  "field": "status",
  "value": "PENDING",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-goal-s43",
    "field": "status",
    "value": "PENDING",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-23T10:17:41.091048+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-goal-s43",
  "field": "status",
  "value": "PENDING",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau025-goal-s43",
    "field": "status",
    "value": "PENDING",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-23T10:17:41.091244+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-obj-s43",
  "field": "status",
  "value": "PENDING",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-obj-s43",
    "field": "status",
    "value": "PENDING",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-23T10:17:41.091475+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-obj-s43\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:14:52.970Z\", \"updated_at\": \"2026-05-23T10:14:52.970Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 12.5166}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-23T10:17:41.091680+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-goal-s43\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:15:08.681Z\", \"updated_at\": \"2026-05-23T10:15:08.681Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 16.5291}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-23T10:17:41.091885+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-goal-s43\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:15:23.340Z\", \"updated_at\": \"2026-05-23T10:15:23.340Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.9069}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-23T10:17:41.092082+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-obj-s43\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:15:30.412Z\", \"updated_at\": \"2026-05-23T10:15:30.412Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.4853}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-23T10:17:41.092353+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-obj-s43",
  "field": "hypothesis",
  "value": "Adaptive CRM tau=0.25 on Object seed43. Tests cross-benchmark transfer of adaptive conformal CRM with 3-suite checkpoint on Object tasks.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau025-obj-s43",
    "field": "hypothesis",
    "value": "Adaptive CRM tau=0.25 on Object seed43. Tests cross-benchmark transfer of adaptive conformal CRM with 3-suite checkpoint on Object tasks.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-23T10:17:41.092594+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-goal-s43",
  "field": "hypothesis",
  "value": "CRM norm=0.05 on Goal seed43. Goal VLA-only baseline = 83.5%. s42=85.5% (+2.0pp). Second seed for Goal CRM 3-seed validation.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-goal-s43",
    "field": "hypothesis",
    "value": "CRM norm=0.05 on Goal seed43. Goal VLA-only baseline = 83.5%. s42=85.5% (+2.0pp). Second seed for Goal CRM 3-seed validation.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-23T10:17:41.092807+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-obj-s43\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:14:52.970Z\", \"updated_at\": \"2026-05-23T10:15:47.533Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Object seed43. Tests cross-benchmark transfer of adaptive conformal CRM with 3-suite checkpoint on Object tasks.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.7604}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-23T10:17:41.093007+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-goal-s43",
  "field": "hypothesis",
  "value": "Adaptive CRM tau=0.25 on Goal seed43. Goal VLA-only baseline = 83.5%. s42=84.0% (+0.5pp weak positive). Second seed for Goal Adaptive validation.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau025-goal-s43",
    "field": "hypothesis",
    "value": "Adaptive CRM tau=0.25 on Goal seed43. Goal VLA-only baseline = 83.5%. s42=84.0% (+0.5pp weak positive). Second seed for Goal Adaptive validation.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-23T10:17:41.093216+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-goal-s43\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:15:08.681Z\", \"updated_at\": \"2026-05-23T10:15:50.398Z\", \"hypothesis\": \"CRM norm=0.05 on Goal seed43. Goal VLA-only baseline = 83.5%. s42=85.5% (+2.0pp). Second seed for Goal CRM 3-seed validation.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.9133}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-23T10:17:41.093438+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-obj-s43",
  "field": "hypothesis",
  "value": "CRM norm=0.05 on Object seed43. Tests static CRM correction with low norm constraint on Object tasks. Second seed for Object CRM norm=0.05 validation.",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-obj-s43",
    "field": "hypothesis",
    "value": "CRM norm=0.05 on Object seed43. Tests static CRM correction with low norm constraint on Object tasks. Second seed for Object CRM norm=0.05 validation.",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-23T10:17:41.093653+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-goal-s43\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:15:23.340Z\", \"updated_at\": \"2026-05-23T10:15:53.458Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Goal seed43. Goal VLA-only baseline = 83.5%. s42=84.0% (+0.5pp weak positive). Second seed for Goal Adaptive validation.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.9901}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-23T10:17:41.093873+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-obj-s43\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:15:30.412Z\", \"updated_at\": \"2026-05-23T10:15:56.371Z\", \"hypothesis\": \"CRM norm=0.05 on Object seed43. Tests static CRM correction with low norm constraint on Object tasks. Second seed for Object CRM norm=0.05 validation.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.8979}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-23T10:17:41.094076+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-obj-s43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2', 'server': 'bjb1-32546', 'gpu_ids': ['cuda:0'], 'pid': 818121, 'seed': 43, 'model_name': 'smolvla+crm_adaptive_tau025', 'data_path': 'LIBERO-Object', 'data_count': 200, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Object'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau025-obj-s43",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2', 'server': 'bjb1-32546', 'gpu_ids': ['cuda:0'], 'pid': 818121, 'seed': 43, 'model_name': 'smolvla+crm_adaptive_tau025', 'data_path': 'LIBERO-Object', 'data_count': 200, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Object'}"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-23T10:17:41.094316+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 1.7213}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-23T10:17:41.094536+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-goal-s43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.05', 'server': 'bjb1-32546', 'gpu_ids': ['cuda:1'], 'pid': 818386, 'seed': 43, 'model_name': 'smolvla+crm_obs_only_norm005', 'data_path': 'LIBERO-Goal', 'data_count': 200, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Goal'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-goal-s43",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.05', 'server': 'bjb1-32546', 'gpu_ids': ['cuda:1'], 'pid': 818386, 'seed': 43, 'model_name': 'smolvla+crm_obs_only_norm005', 'data_path': 'LIBERO-Goal', 'data_count': 200, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Goal'}"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-23T10:17:41.094761+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-goal-s43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2', 'server': 'bjb1-32546', 'gpu_ids': ['cuda:2'], 'pid': 818658, 'seed': 43, 'model_name': 'smolvla+crm_adaptive_tau025', 'data_path': 'LIBERO-Goal', 'data_count': 200, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Goal'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau025-goal-s43",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2', 'server': 'bjb1-32546', 'gpu_ids': ['cuda:2'], 'pid': 818658, 'seed': 43, 'model_name': 'smolvla+crm_adaptive_tau025', 'data_path': 'LIBERO-Goal', 'data_count': 200, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Goal'}"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-23T10:17:41.094983+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 3.2765}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-23T10:17:41.095194+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-obj-s43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.05', 'server': 'bjb1-32546', 'gpu_ids': ['cuda:4'], 'pid': 818928, 'seed': 43, 'model_name': 'smolvla+crm_obs_only_norm005', 'data_path': 'LIBERO-Object', 'data_count': 200, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Object'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-obj-s43",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.05', 'server': 'bjb1-32546', 'gpu_ids': ['cuda:4'], 'pid': 818928, 'seed': 43, 'model_name': 'smolvla+crm_obs_only_norm005', 'data_path': 'LIBERO-Object', 'data_count': 200, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Object'}"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-23T10:17:41.095432+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 3.066}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-23T10:17:41.095632+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 3.2754}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-23T10:17:41.095881+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-obj-s43",
  "field": "status",
  "value": "QUEUED",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau025-obj-s43",
    "field": "status",
    "value": "QUEUED",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-23T10:17:41.096081+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-goal-s43",
  "field": "status",
  "value": "QUEUED",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-goal-s43",
    "field": "status",
    "value": "QUEUED",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-23T10:17:41.096307+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-goal-s43",
  "field": "status",
  "value": "QUEUED",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau025-goal-s43",
    "field": "status",
    "value": "QUEUED",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-23T10:17:41.096514+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-obj-s43",
  "field": "status",
  "value": "QUEUED",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-obj-s43",
    "field": "status",
    "value": "QUEUED",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-23T10:17:41.096720+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-obj-s43\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:14:52.970Z\", \"updated_at\": \"2026-05-23T10:16:25.410Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Object seed43. Tests cross-benchmark transfer of adaptive conformal CRM with 3-suite checkpoint on Object tasks.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.9933}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-23T10:17:41.096939+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-goal-s43\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:15:08.681Z\", \"updated_at\": \"2026-05-23T10:16:34.711Z\", \"hypothesis\": \"CRM norm=0.05 on Goal seed43. Goal VLA-only baseline = 83.5%. s42=85.5% (+2.0pp). Second seed for Goal CRM 3-seed validation.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.9783}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-23T10:17:41.097142+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-goal-s43\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:15:23.340Z\", \"updated_at\": \"2026-05-23T10:16:42.856Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Goal seed43. Goal VLA-only baseline = 83.5%. s42=84.0% (+0.5pp weak positive). Second seed for Goal Adaptive validation.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.63}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-23T10:17:41.097368+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-obj-s43\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:15:30.412Z\", \"updated_at\": \"2026-05-23T10:16:48.441Z\", \"hypothesis\": \"CRM norm=0.05 on Object seed43. Tests static CRM correction with low norm constraint on Object tasks. Second seed for Object CRM norm=0.05 validation.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.5698}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-23T10:17:41.097589+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-obj-s43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2', 'server': 'bjb1-32546', 'gpu_ids': ['cuda:0'], 'pid': 818121, 'seed': 43, 'model_name': 'smolvla+crm_adaptive_tau025', 'data_path': 'LIBERO-Object', 'data_count': 200, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Object'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau025-obj-s43",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2', 'server': 'bjb1-32546', 'gpu_ids': ['cuda:0'], 'pid': 818121, 'seed': 43, 'model_name': 'smolvla+crm_adaptive_tau025', 'data_path': 'LIBERO-Object', 'data_count': 200, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Object'}"
  }
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-23T10:17:41.097823+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-goal-s43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.05', 'server': 'bjb1-32546', 'gpu_ids': ['cuda:1'], 'pid': 818386, 'seed': 43, 'model_name': 'smolvla+crm_obs_only_norm005', 'data_path': 'LIBERO-Goal', 'data_count': 200, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Goal'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-goal-s43",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.05', 'server': 'bjb1-32546', 'gpu_ids': ['cuda:1'], 'pid': 818386, 'seed': 43, 'model_name': 'smolvla+crm_obs_only_norm005', 'data_path': 'LIBERO-Goal', 'data_count': 200, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Goal'}"
  }
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-23T10:17:41.098055+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-adapt-tau025-goal-s43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2', 'server': 'bjb1-32546', 'gpu_ids': ['cuda:2'], 'pid': 818658, 'seed': 43, 'model_name': 'smolvla+crm_adaptive_tau025', 'data_path': 'LIBERO-Goal', 'data_count': 200, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Goal'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-adapt-tau025-goal-s43",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2', 'server': 'bjb1-32546', 'gpu_ids': ['cuda:2'], 'pid': 818658, 'seed': 43, 'model_name': 'smolvla+crm_adaptive_tau025', 'data_path': 'LIBERO-Goal', 'data_count': 200, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Goal'}"
  }
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-23T10:17:41.098298+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-supp-crm-norm005-obj-s43",
  "field": "status",
  "value": "RUNNING",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'command': 'python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.05', 'server': 'bjb1-32546', 'gpu_ids': ['cuda:4'], 'pid': 818928, 'seed': 43, 'model_name': 'smolvla+crm_obs_only_norm005', 'data_path': 'LIBERO-Object', 'data_count': 200, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Object'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-supp-crm-norm005-obj-s43",
    "field": "status",
    "value": "RUNNING",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'command': 'python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.05', 'server': 'bjb1-32546', 'gpu_ids': ['cuda:4'], 'pid': 818928, 'seed': 43, 'model_name': 'smolvla+crm_obs_only_norm005', 'data_path': 'LIBERO-Object', 'data_count': 200, 'checkpoint_source': '/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt', 'eval_data': 'LIBERO-Object'}"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-23T10:17:41.098546+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-obj-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:14:52.970Z\", \"updated_at\": \"2026-05-23T10:17:04.537Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Object seed43. Tests cross-benchmark transfer of adaptive conformal CRM with 3-suite checkpoint on Object tasks.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2\", \"server\": \"bjb1-32546\", \"gpu_ids\": [\"cuda:0\"], \"pid\": 818121, \"seed\": 43, \"model_name\": \"smolvla+crm_adaptive_tau025\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.7019}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-23T10:17:41.098780+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-goal-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:15:08.681Z\", \"updated_at\": \"2026-05-23T10:17:12.777Z\", \"hypothesis\": \"CRM norm=0.05 on Goal seed43. Goal VLA-only baseline = 83.5%. s42=85.5% (+2.0pp). Second seed for Goal CRM 3-seed validation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.05\", \"server\": \"bjb1-32546\", \"gpu_ids\": [\"cuda:1\"], \"pid\": 818386, \"seed\": 43, \"model_name\": \"smolvla+crm_obs_only_norm005\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Goal\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.587}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-23T10:17:41.099010+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-adapt-tau025-goal-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:15:23.340Z\", \"updated_at\": \"2026-05-23T10:17:18.363Z\", \"hypothesis\": \"Adaptive CRM tau=0.25 on Goal seed43. Goal VLA-only baseline = 83.5%. s42=84.0% (+0.5pp weak positive). Second seed for Goal Adaptive validation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark goal --seed 43 --n_rollouts 20 --max_correction_norm 0.2 --K 2\", \"server\": \"bjb1-32546\", \"gpu_ids\": [\"cuda:2\"], \"pid\": 818658, \"seed\": 43, \"model_name\": \"smolvla+crm_adaptive_tau025\", \"data_path\": \"LIBERO-Goal\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Goal\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.6357}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-23T10:17:41.099242+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-supp-crm-norm005-obj-s43\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T10:15:30.412Z\", \"updated_at\": \"2026-05-23T10:17:24.007Z\", \"hypothesis\": \"CRM norm=0.05 on Object seed43. Tests static CRM correction with low norm constraint on Object tasks. Second seed for Object CRM norm=0.05 validation.\", \"spec\": {\"command\": \"python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark object --seed 43 --n_rollouts 20 --max_correction_norm 0.05\", \"server\": \"bjb1-32546\", \"gpu_ids\": [\"cuda:4\"], \"pid\": 818928, \"seed\": 43, \"model_name\": \"smolvla+crm_obs_only_norm005\", \"data_path\": \"LIBERO-Object\", \"data_count\": 200, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\", \"eval_data\": \"LIBERO-Object\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.6149}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 69 · 2026-05-23T10:17:41.099540+00:00_

4 个实验已全部注册为 RUNNING。

## 审计结果汇总

**bjb1-32546 全部 6 GPU 占满，无空闲 GPU 可部署新实验。**

| GPU | exp_id | 实验 | 状态 | 运行时长 |
|-----|--------|------|------|---------|
| cuda:0 | eval-supp-adapt-tau025-obj-s43 | Object Adaptive tau=0.25 s43 | RUNNING (新注册) | ~1.5h |
| cuda:1 | eval-supp-crm-norm005-goal-s43 | Goal CRM norm=0.05 s43 | RUNNING (新注册) | ~1.5h |
| cuda:2 | eval-supp-adapt-tau025-goal-s43 | Goal Adaptive tau=0.25 s43 | RUNNING (新注册) | ~1.5h |
| cuda:3 | eval-supp-long-vla-only-s42 | Long VLA-only s42 | RUNNING (已注册) | ~48min |
| cuda:4 | eval-supp-crm-norm005-obj-s43 | Object CRM norm=0.05 s43 | RUNNING (新注册) | ~1.5h |
| cuda:5 | eval-supp-adapt-tau025-goal-s44 | Goal Adaptive tau=0.25 s44 | RUNNING (已注册) | ~1.1h |

**P1 部署选项对照：**
- #1 Long K=2 mean s42 — **无空闲 GPU，无法部署**
- #2 Goal CRM norm=0.05 s43 — **已在 cuda:1 运行**（由之前 Worker 启动）
- #3 Goal Adaptive tau=0.25 s43 — **已在 cuda:2 运行**（由之前 Worker 启动）
- #4 Goal Reconvla s44 — **无空闲 GPU，无法部署**

已为 cuda:0/1/2/4 上的 4 个未注册实验补建了 registry 条目（RUNNING）。这些实验预计还需 ~10-12h 完成（20 rollouts × 10 tasks 的 eval 通常需 12-14h）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_audit-deploy_bjb1-32546-full-audit_20260523T101221"
}
```

</details>

---
