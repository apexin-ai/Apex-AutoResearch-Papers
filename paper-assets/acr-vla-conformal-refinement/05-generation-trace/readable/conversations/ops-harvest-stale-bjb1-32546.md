# ops harvest stale bjb1 32546

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 75
- **Recorded user turns:** 0
- **Tool calls:** 37
- **Original source:** `logs/chats/worker_ops_harvest-stale-bjb1-32546_20260519T112208.jsonl`
- **Structured JSON:** [`9944327ac90475e3f3a8.json`](../../sessions/99/9944327ac90475e3f3a8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

75 recorded events

### Tool call

_source line 1 · 2026-05-19T11:25:37.876982+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T11:25:37.877479+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T11:25:37.877736+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'RUNNING'}",
  "project": "acr-vla-conformal-refinement",
  "limit": "0",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'RUNNING'}",
    "project": "acr-vla-conformal-refinement",
    "limit": "0",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T11:25:37.878575+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-lto-splitA-vla-only-v2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:19:21.005Z\", \"updated_at\": \"2026-05-19T05:20:25.784Z\", \"hypothesis\": \"VLA-only baseline on LTO held-out 5 tasks (ketchup, milk, orange_juice, salad_dressing, tomato_sauce). Control group for Leave-Task-Out Split A eval. Retry after .replace task matching bug fix.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement/src && CUDA_VISIBLE_DEVICES=2 timeout 57600 python -u evaluate.py --benchmark object --mode vla_only --task_names 'ketchup,milk,orange_juice,salad_dressing,tomato_sauce' --n_rollouts 10 --seed 42 --output_file logs/eval_lto_splitA_vla_only_r2.json\\\"\", \"server\": \"bjb1-18228\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/acr-vla-conformal-refinement/eval-lto-splitA-vla-only-r2.log\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"tmux_session\": \"eval-lto-splitA-vla-only-r2\", \"data_path\": \"LIBERO-Object\", \"data_count\": 50, \"model_name\": \"SmolVLA_vla_only\", \"seed\": 42, \"checkpoint_source\": \"N/A\", \"eval_data\": \"LIBERO-Object held-out (5 tasks x 10 rollouts)\"}}, \"eval-lto-splitA-heldout-v2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:19:18.968Z\", \"updated_at\": \"2026-05-19T05:20:22.689Z\", \"hypothesis\": \"Leave-Task-Out generalization: CRM trained on Split A (5 tasks) evaluated on held-out 5 tasks (ketchup, milk, orange_juice, salad_dressing, tomato_sauce). K=5 ε=0.2. Retry after .replace task matching bug fix.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement/src && CUDA_VISIBLE_DEVICES=1 timeout 57600 python -u evaluate.py --benchmark object --mode crm_obs_only --checkpoint /root/autodl-tmp/checkpoints/crm_lto_splitA_fixed/cr
…[truncated 25230 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T11:25:37.878865+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cd /root/acr-vla-conformal-refinement && echo \"=== logs/ ===\" && ls -la logs/ 2>/dev/null || echo \"no logs/ dir\" && echo \"=== src/logs/ ===\" && ls -la src/logs/ 2>/dev/null || echo \"no src/logs/ dir\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cd /root/acr-vla-conformal-refinement && echo \"=== logs/ ===\" && ls -la logs/ 2>/dev/null || echo \"no logs/ dir\" && echo \"=== src/logs/ ===\" && ls -la src/logs/ 2>/dev/null || echo \"no src/logs/ dir\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T11:25:37.879188+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== logs/ ===\\ntotal 572\\ndrwxr-xr-x 3 root root  8192 May 19 18:47 .\\ndrwxr-xr-x 7 root root    99 May 16 00:52 ..\\n-rw-r--r-- 1 root root  3948 May 17 16:41 eval_argmin_object_seed46.log\\n-rw-r--r-- 1 root root 11209 May 17 12:46 eval_direct_correction_object_seed42.log\\n-rw-r--r-- 1 root root  1489 May 18 01:17 eval_k1_crm_accg_object_seed42.json\\n-rw-r--r-- 1 root root 11171 May 18 01:17 eval_k1_crm_accg_object_seed42.log\\n-rw-r--r-- 1 root root  1489 May 18 01:10 eval_k1_crm_accg_object_seed43.json\\n-rw-r--r-- 1 root root 11257 May 18 01:10 eval_k1_crm_accg_object_seed43.log\\n-rw-r--r-- 1 root root  1489 May 18 01:19 eval_k1_crm_accg_object_seed44.json\\n-rw-r--r-- 1 root root 11168 May 18 01:19 eval_k1_crm_accg_object_seed44.log\\n-rw-r--r-- 1 root root  1489 May 18 04:24 eval_k1_crm_multiscale_object_seed43.json\\n-rw-r--r-- 1 root root 11271 May 18 04:24 eval_k1_crm_multiscale_object_seed43.log\\n-rw-r--r-- 1 root root  1488 May 18 04:20 eval_k1_crm_multiscale_object_seed44.json\\n-rw-r--r-- 1 root root 11273 May 18 04:20 eval_k1_crm_multiscale_object_seed44.log\\n-rw-r--r-- 1 root root  1490 May 16 00:08 eval_object_obs_only.json\\n-rw-r--r-- 1 root root  1490 May 16 14:39 eval_object_obs_only_default_norm.json\\n-rw-r--r-- 1 root root  1490 May 17 04:34 eval_object_obs_only_default_seed44.json\\n-rw-r--r-- 1 root root  1490 May 18 08:10 eval_object_obs_only_default_seed46.json\\n-rw-r--r-- 1 root root 11146 May 18 08:10 eval_object_obs_only_default_seed46.log\\n-rw-r--r-- 1 root root  1490 May 19 13:50 eval_object_obs_only_default_seed47.json\\n-rw-r--r-- 1 root root 11145 May 19 13:50 eval_object_obs_only_default_seed47.log\\n-rw-r--r-- 1 root root  1490 May 16 13:33 eval_object_obs_only_norm003.json\\n-rw-r--r-- 1 root root  1470 May 17 19:57 eval_object_obs_only_norm005_seed43.log\\n-rw-r--r-- 1 root root  1490 May 18 08:41 eval_object_obs_only_norm005_seed43_r2.json\\n-rw-r--r-- 1 root r
…[truncated 5713 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T11:25:37.879530+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cd /root/acr-vla-conformal-refinement && python3 -c \"\nimport json, os\nfiles = [\n    ('eval-obs-only-object-norm01-seed47', 'logs/eval_object_obs_only_norm01_seed47.json'),\n    ('eval-scalar-object-seed46', 'logs/eval_object_scalar_seed46.json'),\n    ('eval-obs-only-object-norm03-seed46', 'logs/eval_object_obs_only_norm03_seed46.json'),\n    ('eval-perdof-object-norm03-seed46', 'logs/eval_object_perdof_norm03_seed46.json'),\n    ('eval-obs-only-object-default-seed47', 'logs/eval_object_obs_only_default_seed47.json'),\n    ('eval-perdof-object-norm005-seed46', 'logs/eval_object_perdof_norm005_seed46.json'),\n]\nfor exp_id, path in files:\n    if os.path.exists(path):\n        d = json.load(open(path))\n        sr = d.get('overall_success_rate', d.get('success_rate', 'NOT_FOUND'))\n        total = d.get('total_rollouts', d.get('total', 'N/A'))\n        print(f'{exp_id} | sr={sr} | total={total}')\n    else:\n        print(f'{exp_id} | FILE_NOT_FOUND')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cd /root/acr-vla-conformal-refinement && python3 -c \"\nimport json, os\nfiles = [\n    ('eval-obs-only-object-norm01-seed47', 'logs/eval_object_obs_only_norm01_seed47.json'),\n    ('eval-scalar-object-seed46', 'logs/eval_object_scalar_seed46.json'),\n    ('eval-obs-only-object-norm03-seed46', 'logs/eval_object_obs_only_norm03_seed46.json'),\n    ('eval-perdof-object-norm03-seed46', 'logs/eval_object_perdof_norm03_seed46.json'),\n    ('eval-obs-only-object-default-seed47', 'logs/eval_object_obs_only_default_seed47.json'),\n    ('eval-perdof-object-norm005-seed46', 'logs/eval_object_perdof_norm005_seed46.json'),\n]\nfor exp_id, path in files:\n    if os.path.exists(path):\n        d = json.load(open(path))\n        sr = d.get('overall_success_rate', d.get('success_rate', 'NOT_FOUND'))\n        total = d.get('total_rollouts', d.get('total', 'N/A'))\n        print(f'{exp_id} | sr={sr} | total={total}')\n    else:\n        print(f'{exp_id} | FILE_NOT_FOUND')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T11:25:37.879795+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/acr-vla-conformal-refinement && python3 -c \\\"\\\\nimport json, os\\\\nfiles = [\\\\n    (\\\\'eval-obs-only-object-norm01-seed47\\\\', \\\\'logs/eval_object_obs_only_norm01_seed47.json\\\\'),\\\\n    (\\\\'eval-scalar-object-seed46\\\\', \\\\'logs/eval_object_scalar_seed46.json\\\\'),\\\\n    (\\\\'eval-obs-only-object-norm03-seed46\\\\', \\\\'logs/eval_object_obs_only_norm03_seed46.json\\\\'),\\\\n    (\\\\'eval-perdof-object-norm03-seed46\\\\', \\\\'logs/eval_object_perdof_norm03_seed46.json\\\\'),\\\\n    (\\\\'eval-obs-only-object-default-seed47\\\\', \\\\'logs/eval_object_obs_only_default_seed47.json\\\\'),\\\\n    (\\\\'eval-perdof-object-norm005-seed46\\\\', \\\\'logs/eval_object_perdof_norm005_seed46.json\\\\'),\\\\n]\\\\nfor exp_id, path in files:\\\\n    if os.path.exists(path):\\\\n        d = json.load(open(path))\\\\n        sr = d.get(\\\\'overall_success_rate\\\\', d.get(\\\\'success_rate\\\\', \\\\'NOT_FOUND\\\\'))\\\\n        total = d.get(\\\\'total_rollouts\\\\', d.get(\\\\'total\\\\', \\\\'N/A\\\\'))\\\\n        print(f\\\\'{exp_id} | sr={sr} | total={total}\\\\')\\\\n    else:\\\\n        print(f\\\\'{exp_id} | FILE_NOT_FOUND\\\\')\\\\n\\\"\\\\n'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T11:25:37.880041+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cd /root/acr-vla-conformal-refinement && echo \"=== perdof_norm003_seed48 ===\" && ls -la logs/*perdof*norm003*seed48* 2>/dev/null && echo \"--- log tail ---\" && tail -30 logs/eval_object_perdof_norm003_seed48.log 2>/dev/null && echo \"=== perdof_norm01_seed48 ===\" && ls -la logs/*perdof*norm01*seed48* 2>/dev/null && echo \"--- check ~/runs ---\" && ls -la ~/runs/acr-vla-conformal-refinement/*perdof*norm01*seed48* 2>/dev/null && ls -la ~/runs/acr-vla-conformal-refinement/*perdof*norm003*seed48* 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cd /root/acr-vla-conformal-refinement && echo \"=== perdof_norm003_seed48 ===\" && ls -la logs/*perdof*norm003*seed48* 2>/dev/null && echo \"--- log tail ---\" && tail -30 logs/eval_object_perdof_norm003_seed48.log 2>/dev/null && echo \"=== perdof_norm01_seed48 ===\" && ls -la logs/*perdof*norm01*seed48* 2>/dev/null && echo \"--- check ~/runs ---\" && ls -la ~/runs/acr-vla-conformal-refinement/*perdof*norm01*seed48* 2>/dev/null && ls -la ~/runs/acr-vla-conformal-refinement/*perdof*norm003*seed48* 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T11:25:37.880299+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/acr-vla-conformal-refinement && echo \\\"=== perdof_norm003_seed48 ===\\\" && ls -la logs/*perdof*norm003*seed48* 2>/dev/null && echo \\\"--- log tail ---\\\" && tail -30 logs/eval_object_perdof_norm003_seed48.log 2>/dev/null && echo \\\"=== perdof_norm01_seed48 ===\\\" && ls -la logs/*perdof*norm01*seed48* 2>/dev/null && echo \\\"--- check ~/runs ---\\\" && ls -la ~/runs/acr-vla-conformal-refinement/*perdof*norm01*seed48* 2>/dev/null && ls -la ~/runs/acr-vla-conformal-refinement/*perdof*norm003*seed48* 2>/dev/null'\\n\\nExit code: 2\\n\\nStdout:\\n\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 1/10, success so far: 1/1\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 2/10, success so far: 2/2\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 3/10, success so far: 2/3\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 4/10, success so far: 2/4\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 5/10, success so far: 2/5\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 6/10, success so far: 3/6\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 7/10, success so far: 3/7\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 8/10, success so far: 3/8\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 9/10, success so far: 3/9\\n=== perdof_norm01_seed48 ===\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.84}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T11:25:37.880588+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -c \"\nimport json, os\nfiles = [\n    ('eval-obs-only-object-norm01-seed47', 'logs/eval_object_obs_only_norm01_seed47.json'),\n    ('eval-scalar-object-seed46', 'logs/eval_object_scalar_seed46.json'),\n    ('eval-obs-only-object-norm03-seed46', 'logs/eval_object_obs_only_norm03_seed46.json'),\n    ('eval-perdof-object-norm03-seed46', 'logs/eval_object_perdof_norm03_seed46.json'),\n    ('eval-obs-only-object-default-seed47', 'logs/eval_object_obs_only_default_seed47.json'),\n    ('eval-perdof-object-norm005-seed46', 'logs/eval_object_perdof_norm005_seed46.json'),\n]\nfor exp_id, path in files:\n    if os.path.exists(path):\n        d = json.load(open(path))\n        sr = d.get('overall_success_rate', d.get('success_rate', 'NOT_FOUND'))\n        total = d.get('total_rollouts', d.get('total', 'N/A'))\n        print(f'{exp_id} | sr={sr} | total={total}')\n    else:\n        print(f'{exp_id} | FILE_NOT_FOUND')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cd /root/acr-vla-conformal-refinement && /root/miniconda3/bin/python -c \"\nimport json, os\nfiles = [\n    ('eval-obs-only-object-norm01-seed47', 'logs/eval_object_obs_only_norm01_seed47.json'),\n    ('eval-scalar-object-seed46', 'logs/eval_object_scalar_seed46.json'),\n    ('eval-obs-only-object-norm03-seed46', 'logs/eval_object_obs_only_norm03_seed46.json'),\n    ('eval-perdof-object-norm03-seed46', 'logs/eval_object_perdof_norm03_seed46.json'),\n    ('eval-obs-only-object-default-seed47', 'logs/eval_object_obs_only_default_seed47.json'),\n    ('eval-perdof-object-norm005-seed46', 'logs/eval_object_perdof_norm005_seed46.json'),\n]\nfor exp_id, path in files:\n    if os.path.exists(path):\n        d = json.load(open(path))\n        sr = d.get('overall_success_rate', d.get('success_rate', 'NOT_FOUND'))\n        total = d.get('total_rollouts', d.get('total', 'N/A'))\n        print(f'{exp_id} | sr={sr} | total={total}')\n    else:\n        print(f'{exp_id} | FILE_NOT_FOUND')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T11:25:37.880841+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"eval-obs-only-object-norm01-seed47 | sr=0.17 | total=N/A\\neval-scalar-object-seed46 | sr=0.09 | total=N/A\\neval-obs-only-object-norm03-seed46 | sr=0.17 | total=N/A\\neval-perdof-object-norm03-seed46 | sr=0.04 | total=N/A\\neval-obs-only-object-default-seed47 | sr=0.16 | total=N/A\\neval-perdof-object-norm005-seed46 | sr=0.11 | total=N/A\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T11:25:37.881049+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cd /root/acr-vla-conformal-refinement && echo \"=== tmux sessions ===\" && tmux ls 2>/dev/null | grep -E \"perdof.*(norm003.*seed48|norm01.*seed48)\" && echo \"=== GPU check ===\" && nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader 2>/dev/null | head -20 && echo \"=== perdof_norm003_seed48 log last line ===\" && wc -l logs/eval_object_perdof_norm003_seed48.log && echo \"=== perdof_norm01_seed48 search ===\" && find /root -maxdepth 4 -name \"*perdof*norm01*seed48*\" -type f 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cd /root/acr-vla-conformal-refinement && echo \"=== tmux sessions ===\" && tmux ls 2>/dev/null | grep -E \"perdof.*(norm003.*seed48|norm01.*seed48)\" && echo \"=== GPU check ===\" && nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader 2>/dev/null | head -20 && echo \"=== perdof_norm003_seed48 log last line ===\" && wc -l logs/eval_object_perdof_norm003_seed48.log && echo \"=== perdof_norm01_seed48 search ===\" && find /root -maxdepth 4 -name \"*perdof*norm01*seed48*\" -type f 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T11:25:37.881283+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== tmux sessions ===\\neval-perdof-norm003-seed48-t16: 1 windows (created Tue May 19 05:29:23 2026)\\n=== GPU check ===\\n758847, GPU-ade291cb-7e13-f292-1714-09ef80919436, 1987 MiB\\n719459, GPU-00ae24f3-53b1-cd05-f561-fe7adbb64e72, 1923 MiB\\n755612, GPU-563702d3-df96-d375-0303-c9b9f202bdd2, 2392 MiB\\n755878, GPU-563702d3-df96-d375-0303-c9b9f202bdd2, 2392 MiB\\n=== perdof_norm003_seed48 log last line ===\\n121 logs/eval_object_perdof_norm003_seed48.log\\n=== perdof_norm01_seed48 search ===\\n/root/logs/eval_object_perdof_norm01_seed48.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T11:25:37.881564+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cd /root && /root/miniconda3/bin/python -c \"\nimport json\nd = json.load(open('logs/eval_object_perdof_norm01_seed48.json'))\nsr = d.get('overall_success_rate', d.get('success_rate', 'NOT_FOUND'))\nprint(f'sr={sr}')\nprint(json.dumps(d, indent=2)[:500])\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cd /root && /root/miniconda3/bin/python -c \"\nimport json\nd = json.load(open('logs/eval_object_perdof_norm01_seed48.json'))\nsr = d.get('overall_success_rate', d.get('success_rate', 'NOT_FOUND'))\nprint(f'sr={sr}')\nprint(json.dumps(d, indent=2)[:500])\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T11:25:37.881803+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"sr=0.12\\n{\\n  \\\"mode\\\": \\\"crm_perdof\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.12,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rat\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T11:25:37.882011+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cd /root/acr-vla-conformal-refinement && echo \"=== perdof_norm003_seed48 still running? ===\" && ps aux | grep \"perdof.*norm003.*seed48\\|norm003.*seed48\" | grep -v grep && echo \"=== tmux capture ===\" && tmux capture-pane -t eval-perdof-norm003-seed48-t16 -p 2>/dev/null | tail -10",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "cd /root/acr-vla-conformal-refinement && echo \"=== perdof_norm003_seed48 still running? ===\" && ps aux | grep \"perdof.*norm003.*seed48\\|norm003.*seed48\" | grep -v grep && echo \"=== tmux capture ===\" && tmux capture-pane -t eval-perdof-norm003-seed48-t16 -p 2>/dev/null | tail -10",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T11:25:37.882233+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== perdof_norm003_seed48 still running? ===\\nroot     719455  0.0  0.0   4364  3200 pts/10   Ss+  05:29   0:00 bash -c CUDA_VISIBLE_DEVICES=3 timeout 57600 /root/miniconda3/bin/python -u /root/acr-vla-conformal-refinement/src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_perdof_norm003_seed48.json 2>&1 | tee logs/eval_object_perdof_norm003_seed48.log\\nroot     719457  0.0  0.0   2800  1028 pts/10   S    05:29   0:00 timeout 57600 /root/miniconda3/bin/python -u /root/acr-vla-conformal-refinement/src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_perdof_norm003_seed48.json\\nroot     719458  0.0  0.0   2796  1060 pts/10   S+   05:29   0:00 tee logs/eval_object_perdof_norm003_seed48.log\\nroot     719459  136  0.9 61519784 9774408 pts/10 Rl 05:29 1137:15 /root/miniconda3/bin/python -u /root/acr-vla-conformal-refinement/src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 48 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_object_perdof_norm003_seed48.json\\n=== tmux capture ===\\nfar: 2/5\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 6/10, success so\\nfar: 3/6\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 7/10, success so\\nfar: 3/7\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 8/10, success so\\nfar: 3/8\\n  pick_up_the_orange_juice_and_place_it_in_the_basket: rollout 9/10, success so\\nfar: 3/9\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T11:25:37.882590+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm01-seed47",
  "field": "metrics",
  "value": "{'success_rate': 0.17, 'total_rollouts': 100}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm01-seed47",
    "field": "metrics",
    "value": "{'success_rate': 0.17, 'total_rollouts': 100}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-19T11:25:37.882983+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-scalar-object-seed46",
  "field": "metrics",
  "value": "{'success_rate': 0.09, 'total_rollouts': 100}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-scalar-object-seed46",
    "field": "metrics",
    "value": "{'success_rate': 0.09, 'total_rollouts': 100}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-19T11:25:37.883280+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm01-seed47\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-17T06:51:15.721Z\", \"updated_at\": \"2026-05-19T11:24:04.451Z\", \"hypothesis\": \"Obs-only CRM (ε=0.1) seed47 on LIBERO-Object. GPU 双跑补 seed。\", \"reproduce\": {\"finished_at\": \"2026-05-17T19:11:17.010Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T19:11:22.018666+00:00\"}], \"previous_failure\": {\"conclusion\": \"killed\"}}, \"completed_at\": \"2026-05-17T19:14:25.783Z\", \"failure_reason\": \"Evaluation killed mid-run: only 2/10 tasks completed (task0: 0/10, task1: 1/10). No JSON output saved. EXIT_CODE=0 but incomplete. Previously marked killed in batch cleanup. Data not usable for magnitude curve.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed47.json\", \"server\": \"bjb1-32546\", \"seed\": 47, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}, \"metrics\": {\"success_rate\": 0.17, \"total_rollouts\": 100}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.4335}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-19T11:25:37.883697+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm03-seed46",
  "field": "metrics",
  "value": "{'success_rate': 0.17, 'total_rollouts': 100}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm03-seed46",
    "field": "metrics",
    "value": "{'success_rate': 0.17, 'total_rollouts': 100}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T11:25:37.883924+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-perdof-object-norm03-seed46",
  "field": "metrics",
  "value": "{'success_rate': 0.04, 'total_rollouts': 100}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-perdof-object-norm03-seed46",
    "field": "metrics",
    "value": "{'success_rate': 0.04, 'total_rollouts': 100}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T11:25:37.884176+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-scalar-object-seed46\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:46.008Z\", \"updated_at\": \"2026-05-19T11:24:06.332Z\", \"hypothesis\": \"Scalar CRM (ε=0.1) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed46.json\", \"server\": \"bjb1-32546\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM_scalar\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}, \"metrics\": {\"success_rate\": 0.09, \"total_rollouts\": 100}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.8543}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T11:25:37.884433+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-default-seed47",
  "field": "metrics",
  "value": "{'success_rate': 0.16, 'total_rollouts': 100}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-default-seed47",
    "field": "metrics",
    "value": "{'success_rate': 0.16, 'total_rollouts': 100}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-19T11:25:37.884649+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-perdof-object-norm005-seed46",
  "field": "metrics",
  "value": "{'success_rate': 0.11, 'total_rollouts': 100}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-perdof-object-norm005-seed46",
    "field": "metrics",
    "value": "{'success_rate': 0.11, 'total_rollouts': 100}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-19T11:25:37.884917+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm03-seed46\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-17T10:28:22.831Z\", \"updated_at\": \"2026-05-19T11:24:08.280Z\", \"hypothesis\": \"Obs-only CRM (ε=0.3) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"completed_at\": \"2026-05-17T23:30:58.329Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.17, \"successes\": 17, \"total\": 100}}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed46.json\", \"server\": \"bjb1-32546\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}, \"metrics\": {\"success_rate\": 0.17, \"total_rollouts\": 100}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9146}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-19T11:25:37.885139+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-perdof-object-norm01-seed48",
  "field": "metrics",
  "value": "{'success_rate': 0.12, 'total_rollouts': 100}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-perdof-object-norm01-seed48",
    "field": "metrics",
    "value": "{'success_rate': 0.12, 'total_rollouts': 100}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-19T11:25:37.885409+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-perdof-object-norm03-seed46\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-17T11:21:58.288Z\", \"updated_at\": \"2026-05-19T11:24:09.487Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.3) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"completed_at\": \"2026-05-17T11:26:50.317Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"metrics\": {\"failure_reason\": \"Process exited after ~2 min during env loading, no evaluation results produced. No JSON output. Likely OOM or SIGHUP kill (exit code 129).\", \"n_rollouts\": 0}}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed46.json\", \"server\": \"bjb1-32546\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}, \"metrics\": {\"success_rate\": 0.04, \"total_rollouts\": 100}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2256}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T11:25:37.885781+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-default-seed47\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:37.333Z\", \"updated_at\": \"2026-05-19T11:24:10.732Z\", \"hypothesis\": \"Obs-only CRM (ε=default) seed47 on LIBERO-Object. GPU 双跑补 seed。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed47.json\", \"server\": \"bjb1-32546\", \"seed\": 47, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}, \"metrics\": {\"success_rate\": 0.16, \"total_rollouts\": 100}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2014}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-19T11:25:37.886031+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-perdof-object-norm005-seed46\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:34.428Z\", \"updated_at\": \"2026-05-19T11:24:11.963Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.05) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed46.json\", \"server\": \"bjb1-32546\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}, \"metrics\": {\"success_rate\": 0.11, \"total_rollouts\": 100}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2245}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T11:25:37.886311+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-perdof-object-norm01-seed48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:57:04.076Z\", \"updated_at\": \"2026-05-19T11:24:13.167Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.1) seed48 on LIBERO-Object. 补 perdof ε=0.1 至 n=7，替代被 kill 的 obs_only_norm03_seed46 重复实验的 GPU slot。\", \"spec\": {\"command\": \"crm_perdof --benchmark object --seed 48 --K 10 --max_correction_norm 0.1 --n_rollouts 10\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"crm_perdof\", \"seed\": 48, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\"}, \"metrics\": {\"success_rate\": 0.12, \"total_rollouts\": 100}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1981}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-19T11:25:37.886596+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm01-seed47",
  "field": "notes",
  "value": "采集时间 2026-05-19, 进程已自然结束",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm01-seed47",
    "field": "notes",
    "value": "采集时间 2026-05-19, 进程已自然结束",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-19T11:25:37.886810+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-scalar-object-seed46",
  "field": "notes",
  "value": "采集时间 2026-05-19, 进程已自然结束",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-scalar-object-seed46",
    "field": "notes",
    "value": "采集时间 2026-05-19, 进程已自然结束",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-19T11:25:37.887065+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm01-seed47\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-17T06:51:15.721Z\", \"updated_at\": \"2026-05-19T11:24:20.505Z\", \"hypothesis\": \"Obs-only CRM (ε=0.1) seed47 on LIBERO-Object. GPU 双跑补 seed。\", \"reproduce\": {\"finished_at\": \"2026-05-17T19:11:17.010Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T19:11:22.018666+00:00\"}], \"previous_failure\": {\"conclusion\": \"killed\"}}, \"completed_at\": \"2026-05-17T19:14:25.783Z\", \"failure_reason\": \"Evaluation killed mid-run: only 2/10 tasks completed (task0: 0/10, task1: 1/10). No JSON output saved. EXIT_CODE=0 but incomplete. Previously marked killed in batch cleanup. Data not usable for magnitude curve.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed47.json\", \"server\": \"bjb1-32546\", \"seed\": 47, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}, \"metrics\": {\"success_rate\": 0.17, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9543}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-19T11:25:37.887316+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm03-seed46",
  "field": "notes",
  "value": "采集时间 2026-05-19, 进程已自然结束",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm03-seed46",
    "field": "notes",
    "value": "采集时间 2026-05-19, 进程已自然结束",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-19T11:25:37.887867+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-perdof-object-norm03-seed46",
  "field": "notes",
  "value": "采集时间 2026-05-19, 进程已自然结束",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-perdof-object-norm03-seed46",
    "field": "notes",
    "value": "采集时间 2026-05-19, 进程已自然结束",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-19T11:25:37.888103+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-default-seed47",
  "field": "notes",
  "value": "采集时间 2026-05-19, 进程已自然结束",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-default-seed47",
    "field": "notes",
    "value": "采集时间 2026-05-19, 进程已自然结束",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-19T11:25:37.888393+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-scalar-object-seed46\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:46.008Z\", \"updated_at\": \"2026-05-19T11:24:23.639Z\", \"hypothesis\": \"Scalar CRM (ε=0.1) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed46.json\", \"server\": \"bjb1-32546\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM_scalar\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}, \"metrics\": {\"success_rate\": 0.09, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.1618}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-19T11:25:37.888716+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-perdof-object-norm005-seed46",
  "field": "notes",
  "value": "采集时间 2026-05-19, 进程已自然结束",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-perdof-object-norm005-seed46",
    "field": "notes",
    "value": "采集时间 2026-05-19, 进程已自然结束",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-19T11:25:37.888983+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm03-seed46\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-17T10:28:22.831Z\", \"updated_at\": \"2026-05-19T11:24:25.261Z\", \"hypothesis\": \"Obs-only CRM (ε=0.3) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"completed_at\": \"2026-05-17T23:30:58.329Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.17, \"successes\": 17, \"total\": 100}}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed46.json\", \"server\": \"bjb1-32546\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}, \"metrics\": {\"success_rate\": 0.17, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9558}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-19T11:25:37.889233+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-perdof-object-norm01-seed48",
  "field": "notes",
  "value": "采集时间 2026-05-19, 进程已自然结束. JSON 位于 /root/logs/ 而非项目 logs/ 目录",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-perdof-object-norm01-seed48",
    "field": "notes",
    "value": "采集时间 2026-05-19, 进程已自然结束. JSON 位于 /root/logs/ 而非项目 logs/ 目录",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-19T11:25:37.889470+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm01-seed47",
  "field": "conclusion",
  "value": "success",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm01-seed47",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-19T11:25:37.889672+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-scalar-object-seed46",
  "field": "conclusion",
  "value": "success",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-scalar-object-seed46",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-19T11:25:37.889918+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-perdof-object-norm03-seed46\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-17T11:21:58.288Z\", \"updated_at\": \"2026-05-19T11:24:27.546Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.3) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"completed_at\": \"2026-05-17T11:26:50.317Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"metrics\": {\"failure_reason\": \"Process exited after ~2 min during env loading, no evaluation results produced. No JSON output. Likely OOM or SIGHUP kill (exit code 129).\", \"n_rollouts\": 0}}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed46.json\", \"server\": \"bjb1-32546\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}, \"metrics\": {\"success_rate\": 0.04, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.1597}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-19T11:25:37.890149+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm03-seed46",
  "field": "conclusion",
  "value": "success",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm03-seed46",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-19T11:25:37.890364+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-perdof-object-norm03-seed46",
  "field": "conclusion",
  "value": "success",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-perdof-object-norm03-seed46",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-19T11:25:37.890569+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-default-seed47",
  "field": "conclusion",
  "value": "success",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-default-seed47",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-19T11:25:37.890803+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-default-seed47\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:37.333Z\", \"updated_at\": \"2026-05-19T11:24:30.401Z\", \"hypothesis\": \"Obs-only CRM (ε=default) seed47 on LIBERO-Object. GPU 双跑补 seed。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed47.json\", \"server\": \"bjb1-32546\", \"seed\": 47, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}, \"metrics\": {\"success_rate\": 0.16, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.0003}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-19T11:25:37.891010+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-perdof-object-norm005-seed46",
  "field": "conclusion",
  "value": "success",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-perdof-object-norm005-seed46",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-19T11:25:37.891199+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-perdof-object-norm01-seed48",
  "field": "conclusion",
  "value": "success",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-perdof-object-norm01-seed48",
    "field": "conclusion",
    "value": "success",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-19T11:25:37.891464+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-perdof-object-norm005-seed46\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:34.428Z\", \"updated_at\": \"2026-05-19T11:24:33.442Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.05) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed46.json\", \"server\": \"bjb1-32546\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}, \"metrics\": {\"success_rate\": 0.11, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.6808}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-19T11:25:37.891731+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-perdof-object-norm01-seed48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:57:04.076Z\", \"updated_at\": \"2026-05-19T11:24:35.449Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.1) seed48 on LIBERO-Object. 补 perdof ε=0.1 至 n=7，替代被 kill 的 obs_only_norm03_seed46 重复实验的 GPU slot。\", \"spec\": {\"command\": \"crm_perdof --benchmark object --seed 48 --K 10 --max_correction_norm 0.1 --n_rollouts 10\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"crm_perdof\", \"seed\": 48, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\"}, \"metrics\": {\"success_rate\": 0.12, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束. JSON 位于 /root/logs/ 而非项目 logs/ 目录\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.8868}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-19T11:25:37.892004+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm01-seed47\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-17T06:51:15.721Z\", \"updated_at\": \"2026-05-19T11:24:37.408Z\", \"hypothesis\": \"Obs-only CRM (ε=0.1) seed47 on LIBERO-Object. GPU 双跑补 seed。\", \"reproduce\": {\"finished_at\": \"2026-05-17T19:11:17.010Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T19:11:22.018666+00:00\"}], \"previous_failure\": {\"conclusion\": \"killed\"}}, \"completed_at\": \"2026-05-17T19:14:25.783Z\", \"failure_reason\": \"Evaluation killed mid-run: only 2/10 tasks completed (task0: 0/10, task1: 1/10). No JSON output saved. EXIT_CODE=0 but incomplete. Previously marked killed in batch cleanup. Data not usable for magnitude curve.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed47.json\", \"server\": \"bjb1-32546\", \"seed\": 47, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}, \"metrics\": {\"success_rate\": 0.17, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9495}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-19T11:25:37.892282+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-scalar-object-seed46\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:46.008Z\", \"updated_at\": \"2026-05-19T11:24:39.245Z\", \"hypothesis\": \"Scalar CRM (ε=0.1) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed46.json\", \"server\": \"bjb1-32546\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM_scalar\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}, \"metrics\": {\"success_rate\": 0.09, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.8259}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-19T11:25:37.892570+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm03-seed46\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-17T10:28:22.831Z\", \"updated_at\": \"2026-05-19T11:24:41.156Z\", \"hypothesis\": \"Obs-only CRM (ε=0.3) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"completed_at\": \"2026-05-17T23:30:58.329Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.17, \"successes\": 17, \"total\": 100}}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed46.json\", \"server\": \"bjb1-32546\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}, \"metrics\": {\"success_rate\": 0.17, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.8814}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-19T11:25:37.892872+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-perdof-object-norm03-seed46\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 1, \"created_at\": \"2026-05-17T11:21:58.288Z\", \"updated_at\": \"2026-05-19T11:24:42.323Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.3) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"completed_at\": \"2026-05-17T11:26:50.317Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"metrics\": {\"failure_reason\": \"Process exited after ~2 min during env loading, no evaluation results produced. No JSON output. Likely OOM or SIGHUP kill (exit code 129).\", \"n_rollouts\": 0}}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed46.json\", \"server\": \"bjb1-32546\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}, \"metrics\": {\"success_rate\": 0.04, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1612}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-19T11:25:37.893143+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-default-seed47\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:37.333Z\", \"updated_at\": \"2026-05-19T11:24:43.523Z\", \"hypothesis\": \"Obs-only CRM (ε=default) seed47 on LIBERO-Object. GPU 双跑补 seed。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed47.json\", \"server\": \"bjb1-32546\", \"seed\": 47, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}, \"metrics\": {\"success_rate\": 0.16, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2005}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-19T11:25:37.893433+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-perdof-object-norm005-seed46\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:34.428Z\", \"updated_at\": \"2026-05-19T11:24:44.719Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.05) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed46.json\", \"server\": \"bjb1-32546\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}, \"metrics\": {\"success_rate\": 0.11, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.221}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-19T11:25:37.893696+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-perdof-object-norm01-seed48\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:57:04.076Z\", \"updated_at\": \"2026-05-19T11:24:45.966Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.1) seed48 on LIBERO-Object. 补 perdof ε=0.1 至 n=7，替代被 kill 的 obs_only_norm03_seed46 重复实验的 GPU slot。\", \"spec\": {\"command\": \"crm_perdof --benchmark object --seed 48 --K 10 --max_correction_norm 0.1 --n_rollouts 10\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"crm_perdof\", \"seed\": 48, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\"}, \"metrics\": {\"success_rate\": 0.12, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束. JSON 位于 /root/logs/ 而非项目 logs/ 目录\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2112}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-19T11:25:37.893979+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm01-seed47",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'checkpoint_path': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'log_path': 'logs/eval_object_obs_only_norm01_seed47.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm01-seed47",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'checkpoint_path': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'log_path': 'logs/eval_object_obs_only_norm01_seed47.log'}"
  }
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-19T11:25:37.894305+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-scalar-object-seed46",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'checkpoint_path': '/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt', 'log_path': 'logs/eval_object_scalar_seed46.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-scalar-object-seed46",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'checkpoint_path': '/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt', 'log_path': 'logs/eval_object_scalar_seed46.log'}"
  }
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-19T11:25:37.894545+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-norm03-seed46",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'checkpoint_path': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'log_path': 'logs/eval_object_obs_only_norm03_seed46.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-norm03-seed46",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'checkpoint_path': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'log_path': 'logs/eval_object_obs_only_norm03_seed46.log'}"
  }
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-19T11:25:37.894750+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-perdof-object-norm03-seed46",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'checkpoint_path': '/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt', 'log_path': 'logs/eval_object_perdof_norm03_seed46.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-perdof-object-norm03-seed46",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'checkpoint_path': '/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt', 'log_path': 'logs/eval_object_perdof_norm03_seed46.log'}"
  }
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-19T11:25:37.894958+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-obs-only-object-default-seed47",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'checkpoint_path': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'log_path': 'logs/eval_object_obs_only_default_seed47.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-obs-only-object-default-seed47",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'checkpoint_path': '/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt', 'log_path': 'logs/eval_object_obs_only_default_seed47.log'}"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-19T11:25:37.895250+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm01-seed47\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-17T06:51:15.721Z\", \"updated_at\": \"2026-05-19T11:25:01.605Z\", \"hypothesis\": \"Obs-only CRM (ε=0.1) seed47 on LIBERO-Object. GPU 双跑补 seed。\", \"reproduce\": {\"finished_at\": \"2026-05-17T19:11:17.010Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T19:11:22.018666+00:00\"}], \"previous_failure\": {\"conclusion\": \"killed\"}}, \"completed_at\": \"2026-05-17T19:14:25.783Z\", \"failure_reason\": \"Evaluation killed mid-run: only 2/10 tasks completed (task0: 0/10, task1: 1/10). No JSON output saved. EXIT_CODE=0 but incomplete. Previously marked killed in batch cleanup. Data not usable for magnitude curve.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_obs_only_norm01_seed47.json\", \"server\": \"bjb1-32546\", \"seed\": 47, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"logs/eval_object_obs_only_norm01_seed47.log\"}, \"metrics\": {\"success_rate\": 0.17, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.989}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-19T11:25:37.895518+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-perdof-object-norm005-seed46",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'checkpoint_path': '/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt', 'log_path': 'logs/eval_object_perdof_norm005_seed46.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-perdof-object-norm005-seed46",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'checkpoint_path': '/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt', 'log_path': 'logs/eval_object_perdof_norm005_seed46.log'}"
  }
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-19T11:25:37.895730+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval-perdof-object-norm01-seed48",
  "field": "status",
  "value": "DONE",
  "project": "acr-vla-conformal-refinement",
  "spec": "{'checkpoint_path': '/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt', 'log_path': '/root/logs/eval_object_perdof_norm01_seed48.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval-perdof-object-norm01-seed48",
    "field": "status",
    "value": "DONE",
    "project": "acr-vla-conformal-refinement",
    "spec": "{'checkpoint_path': '/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt', 'log_path': '/root/logs/eval_object_perdof_norm01_seed48.json'}"
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-19T11:25:37.896016+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-scalar-object-seed46\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:46.008Z\", \"updated_at\": \"2026-05-19T11:25:07.860Z\", \"hypothesis\": \"Scalar CRM (ε=0.1) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_scalar --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt --max_correction_norm 0.1 --output_file logs/eval_object_scalar_seed46.json\", \"server\": \"bjb1-32546\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM_scalar\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt\", \"log_path\": \"logs/eval_object_scalar_seed46.log\"}, \"metrics\": {\"success_rate\": 0.09, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:25:07.860Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.8455}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-19T11:25:37.896329+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-norm03-seed46\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-17T10:28:22.831Z\", \"updated_at\": \"2026-05-19T11:25:11.008Z\", \"hypothesis\": \"Obs-only CRM (ε=0.3) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"completed_at\": \"2026-05-17T23:30:58.329Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.17, \"successes\": 17, \"total\": 100}}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_obs_only_norm03_seed46.json\", \"server\": \"bjb1-32546\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"logs/eval_object_obs_only_norm03_seed46.log\"}, \"metrics\": {\"success_rate\": 0.17, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.5335}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-19T11:25:37.896640+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-perdof-object-norm03-seed46\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-17T11:21:58.288Z\", \"updated_at\": \"2026-05-19T11:25:13.541Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.3) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"completed_at\": \"2026-05-17T11:26:50.317Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"metrics\": {\"failure_reason\": \"Process exited after ~2 min during env loading, no evaluation results produced. No JSON output. Likely OOM or SIGHUP kill (exit code 129).\", \"n_rollouts\": 0}}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.3 --output_file logs/eval_object_perdof_norm03_seed46.json\", \"server\": \"bjb1-32546\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"logs/eval_object_perdof_norm03_seed46.log\"}, \"metrics\": {\"success_rate\": 0.04, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.7942}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-19T11:25:37.896954+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-obs-only-object-default-seed47\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:37.333Z\", \"updated_at\": \"2026-05-19T11:25:18.480Z\", \"hypothesis\": \"Obs-only CRM (ε=default) seed47 on LIBERO-Object. GPU 双跑补 seed。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 47 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --output_file logs/eval_object_obs_only_default_seed47.json\", \"server\": \"bjb1-32546\", \"seed\": 47, \"model_name\": \"SmolVLA+CRM_obs_only\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"log_path\": \"logs/eval_object_obs_only_default_seed47.log\"}, \"metrics\": {\"success_rate\": 0.16, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:25:18.480Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.756}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-19T11:25:37.897240+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-perdof-object-norm005-seed46\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:32:34.428Z\", \"updated_at\": \"2026-05-19T11:25:23.296Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.05) seed46 on LIBERO-Object. GPU 双跑补 seed。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 46 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt --max_correction_norm 0.05 --output_file logs/eval_object_perdof_norm005_seed46.json\", \"server\": \"bjb1-32546\", \"seed\": 46, \"model_name\": \"SmolVLA+CRM_perdof\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"logs/eval_object_perdof_norm005_seed46.log\"}, \"metrics\": {\"success_rate\": 0.11, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:25:23.296Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.7188}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-19T11:25:37.897565+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval-perdof-object-norm01-seed48\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:57:04.076Z\", \"updated_at\": \"2026-05-19T11:25:28.189Z\", \"hypothesis\": \"Per-DoF CRM (ε=0.1) seed48 on LIBERO-Object. 补 perdof ε=0.1 至 n=7，替代被 kill 的 obs_only_norm03_seed46 重复实验的 GPU slot。\", \"spec\": {\"command\": \"crm_perdof --benchmark object --seed 48 --K 10 --max_correction_norm 0.1 --n_rollouts 10\", \"server\": \"bjb1-32546\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"crm_perdof\", \"seed\": 48, \"eval_data\": \"LIBERO-Object\", \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt\", \"log_path\": \"/root/logs/eval_object_perdof_norm01_seed48.json\"}, \"metrics\": {\"success_rate\": 0.12, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束. JSON 位于 /root/logs/ 而非项目 logs/ 目录\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:25:28.189Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.7838}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Assistant

_source line 75 · 2026-05-19T11:25:37.899588+00:00_

7/8 实验全部更新为 DONE。汇总：

| exp_id | success_rate | conclusion |
|--------|-------------|------------|
| eval-obs-only-object-norm01-seed47 | 17% | success |
| eval-scalar-object-seed46 | 9% | success |
| eval-obs-only-object-norm03-seed46 | 17% | success |
| eval-perdof-object-norm03-seed46 | 4% | success |
| eval-obs-only-object-default-seed47 | 16% | success |
| eval-perdof-object-norm005-seed46 | 11% | success |
| eval-perdof-object-norm01-seed48 | 12% | success |
| eval-perdof-object-norm003-seed48 | **仍在运行** | — |

**eval-perdof-object-norm003-seed48** 仍有活跃 tmux session 和 GPU 进程（pid 719459），正在跑 orange_juice 任务 rollout 9/10，尚未生成 JSON。保持 RUNNING 状态不动。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_harvest-stale-bjb1-32546_20260519T112208"
}
```

</details>

---
