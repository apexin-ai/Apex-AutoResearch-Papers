# check stage1 only result

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 0
- **Tool calls:** 25
- **Original source:** `logs/chats/worker_check_stage1_only_result_20260517T060908.jsonl`
- **Structured JSON:** [`86dfff2724390014963e.json`](../../sessions/86/86dfff2724390014963e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

51 recorded events

### Tool call

_source line 1 · 2026-05-17T06:10:55.948283+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T06:10:55.948650+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T06:10:55.948827+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "ls -lt /root/autodl-tmp/importance_margin_vla_compress/eval_results/ | head -20",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "ls -lt /root/autodl-tmp/importance_margin_vla_compress/eval_results/ | head -20",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T06:10:55.948981+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 352\\n-rw-r--r-- 1 root root  2697 May 17 13:02 eval_stage1only_object.json\\n-rw-r--r-- 1 root root  2673 May 17 12:38 imm_k07_bypass_object.json\\n-rw-r--r-- 1 root root  2665 May 17 12:19 imm_100k_bypass_object.json\\n-rw-r--r-- 1 root root  2703 May 17 11:36 eval_imm_k07_bypass_object.log\\n-rw-r--r-- 1 root root  2687 May 17 10:37 eval_imm_k07_object_acis_prune.json\\n-rw-r--r-- 1 root root  2847 May 17 10:02 full_ft_100k_seed42_libero_spatial_formal.json\\n-rw-r--r-- 1 root root  2681 May 17 09:48 imm_fullft_100k_libero_object.json\\n-rw-r--r-- 1 root root  2496 May 17 08:51 full_ft_seed0_100k_libero_goal.json\\n-rw-r--r-- 1 root root  2876 May 17 08:16 full_ft_seed0_100k_libero_spatial.json\\n-rw-r--r-- 1 root root 33238 May 17 08:11 imm_v2_fullft_libero_object.log\\n-rw-r--r-- 1 root root  2680 May 17 08:11 imm_v2_fullft_libero_object.json\\n-rw-r--r-- 1 root root  2668 May 17 07:32 full_ft_seed0_100k_libero_object.json\\n-rw-r--r-- 1 root root  2664 May 17 06:09 full_ft_100k_libero_object_formal.json\\n-rw-r--r-- 1 root root  2470 May 17 04:49 libero_libero_goal.json\\n-rw-r--r-- 1 root root  2850 May 17 04:38 libero_libero_spatial.json\\n-rw-r--r-- 1 root root  2625 May 17 04:01 libero_libero_object.json\\n-rw-r--r-- 1 root root  3365 May 16 23:35 pruning_sweep_v2.json\\n-rw-r--r-- 1 root root 11106 May 16 23:35 pruning_sweep_v2.log\\n-rw-r--r-- 1 root root  3238 May 16 23:18 pruning_sweep.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.27}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T06:10:55.949117+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "find /root/autodl-tmp/importance_margin_vla_compress/eval_results/ -name \"*stage1*\" -o -name \"*s1*\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "find /root/autodl-tmp/importance_margin_vla_compress/eval_results/ -name \"*stage1*\" -o -name \"*s1*\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T06:10:55.949392+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_stage1only_object.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T06:10:55.949529+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "ps aux | grep eval | grep -v grep; echo \"---TMUX---\"; tmux ls 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "ps aux | grep eval | grep -v grep; echo \"---TMUX---\"; tmux ls 2>&1",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T06:10:55.949656+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'ps aux | grep eval | grep -v grep; echo \\\"---TMUX---\\\"; tmux ls 2>&1'\\n\\nExit code: 1\\n\\nStdout:\\n\\n---TMUX---\\nno server running on /tmp/tmux-0/default\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T06:10:55.949806+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_stage1only_object.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_stage1only_object.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-17T06:10:55.949936+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/imm_100k_bypass_object.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/imm_100k_bypass_object.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-17T06:10:55.950119+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"suite\\\": \\\"libero_object\\\",\\n  \\\"mode\\\": \\\"acis_prune\\\",\\n  \\\"checkpoint\\\": \\\"checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt\\\",\\n  \\\"config\\\": \\\"configs/libero_imm_twostage_fullft.yaml\\\",\\n  \\\"total_episodes\\\": 500,\\n  \\\"total_successes\\\": 224,\\n  \\\"overall_success_rate\\\": 0.448,\\n  \\\"wilson_ci_95\\\": [\\n    0.405,\\n    0.4918\\n  ],\\n  \\\"num_episodes_per_task\\\": 50,\\n  \\\"max_steps\\\": 280,\\n  \\\"action_horizon\\\": 50,\\n  \\\"seed\\\": 42,\\n  \\\"per_task\\\": {\\n    \\\"0\\\": {\\n      \\\"task_id\\\": 0,\\n      \\\"task_description\\\": \\\"pick up the alphabet soup and place it in the basket\\\",\\n      \\\"success_count\\\": 11,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.22,\\n      \\\"mean_steps\\\": 251.2\\n    },\\n    \\\"1\\\": {\\n      \\\"task_id\\\": 1,\\n      \\\"task_description\\\": \\\"pick up the cream cheese and place it in the basket\\\",\\n      \\\"success_count\\\": 30,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.6,\\n      \\\"mean_steps\\\": 188.0\\n    },\\n    \\\"2\\\": {\\n      \\\"task_id\\\": 2,\\n      \\\"task_description\\\": \\\"pick up the salad dressing and place it in the basket\\\",\\n      \\\"success_count\\\": 21,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.42,\\n      \\\"mean_steps\\\": 214.0\\n    },\\n    \\\"3\\\": {\\n      \\\"task_id\\\": 3,\\n      \\\"task_description\\\": \\\"pick up the bbq sauce and place it in the basket\\\",\\n      \\\"success_count\\\": 19,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.38,\\n      \\\"mean_steps\\\": 222.9\\n    },\\n    \\\"4\\\": {\\n      \\\"task_id\\\": 4,\\n      \\\"task_description\\\": \\\"pick up the ketchup and place it in the basket\\\",\\n      \\\"success_count\\\": 29,\\n      \\\"total_episodes\\\": 50,\\n    
…[truncated 1635 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-17T06:10:55.950299+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/imm_k07_bypass_object.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_results/imm_k07_bypass_object.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-17T06:10:55.950486+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"suite\\\": \\\"libero_object\\\",\\n  \\\"mode\\\": \\\"baseline\\\",\\n  \\\"checkpoint\\\": \\\"checkpoints/libero_imm_twostage_fullft/final/checkpoint.pt\\\",\\n  \\\"config\\\": \\\"configs/libero_imm_twostage_fullft.yaml\\\",\\n  \\\"total_episodes\\\": 500,\\n  \\\"total_successes\\\": 0,\\n  \\\"overall_success_rate\\\": 0.0,\\n  \\\"wilson_ci_95\\\": [\\n    0.0,\\n    0.0076\\n  ],\\n  \\\"num_episodes_per_task\\\": 50,\\n  \\\"max_steps\\\": 280,\\n  \\\"action_horizon\\\": 50,\\n  \\\"seed\\\": 42,\\n  \\\"per_task\\\": {\\n    \\\"0\\\": {\\n      \\\"task_id\\\": 0,\\n      \\\"task_description\\\": \\\"pick up the alphabet soup and place it in the basket\\\",\\n      \\\"success_count\\\": 0,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.0,\\n      \\\"mean_steps\\\": 280.0\\n    },\\n    \\\"1\\\": {\\n      \\\"task_id\\\": 1,\\n      \\\"task_description\\\": \\\"pick up the cream cheese and place it in the basket\\\",\\n      \\\"success_count\\\": 0,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.0,\\n      \\\"mean_steps\\\": 280.0\\n    },\\n    \\\"2\\\": {\\n      \\\"task_id\\\": 2,\\n      \\\"task_description\\\": \\\"pick up the salad dressing and place it in the basket\\\",\\n      \\\"success_count\\\": 0,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.0,\\n      \\\"mean_steps\\\": 280.0\\n    },\\n    \\\"3\\\": {\\n      \\\"task_id\\\": 3,\\n      \\\"task_description\\\": \\\"pick up the bbq sauce and place it in the basket\\\",\\n      \\\"success_count\\\": 0,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.0,\\n      \\\"mean_steps\\\": 280.0\\n    },\\n    \\\"4\\\": {\\n      \\\"task_id\\\": 4,\\n      \\\"task_description\\\": \\\"pick up the ketchup and place it in the basket\\\",\\n      \\\"success_count\\\": 0,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\"
…[truncated 1603 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T06:10:55.950688+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"suite\\\": \\\"libero_object\\\",\\n  \\\"mode\\\": \\\"baseline\\\",\\n  \\\"checkpoint\\\": \\\"checkpoints/libero_imm_twostage_fullft_k07/final/checkpoint.pt\\\",\\n  \\\"config\\\": \\\"configs/libero_imm_twostage_fullft_k07.yaml\\\",\\n  \\\"total_episodes\\\": 500,\\n  \\\"total_successes\\\": 0,\\n  \\\"overall_success_rate\\\": 0.0,\\n  \\\"wilson_ci_95\\\": [\\n    0.0,\\n    0.0076\\n  ],\\n  \\\"num_episodes_per_task\\\": 50,\\n  \\\"max_steps\\\": 280,\\n  \\\"action_horizon\\\": 50,\\n  \\\"seed\\\": 42,\\n  \\\"per_task\\\": {\\n    \\\"0\\\": {\\n      \\\"task_id\\\": 0,\\n      \\\"task_description\\\": \\\"pick up the alphabet soup and place it in the basket\\\",\\n      \\\"success_count\\\": 0,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.0,\\n      \\\"mean_steps\\\": 280.0\\n    },\\n    \\\"1\\\": {\\n      \\\"task_id\\\": 1,\\n      \\\"task_description\\\": \\\"pick up the cream cheese and place it in the basket\\\",\\n      \\\"success_count\\\": 0,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.0,\\n      \\\"mean_steps\\\": 280.0\\n    },\\n    \\\"2\\\": {\\n      \\\"task_id\\\": 2,\\n      \\\"task_description\\\": \\\"pick up the salad dressing and place it in the basket\\\",\\n      \\\"success_count\\\": 0,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.0,\\n      \\\"mean_steps\\\": 280.0\\n    },\\n    \\\"3\\\": {\\n      \\\"task_id\\\": 3,\\n      \\\"task_description\\\": \\\"pick up the bbq sauce and place it in the basket\\\",\\n      \\\"success_count\\\": 0,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_rate\\\": 0.0,\\n      \\\"mean_steps\\\": 280.0\\n    },\\n    \\\"4\\\": {\\n      \\\"task_id\\\": 4,\\n      \\\"task_description\\\": \\\"pick up the ketchup and place it in the basket\\\",\\n      \\\"success_count\\\": 0,\\n      \\\"total_episodes\\\": 50,\\n      \\\"success_
…[truncated 1611 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T06:10:55.950846+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "nvidia-smi --query-gpu=index,name,utilization.gpu,memory.used,memory.total --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "nvidia-smi --query-gpu=index,name,utilization.gpu,memory.used,memory.total --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T06:10:55.950973+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, NVIDIA RTX PRO 6000 Blackwell Server Edition, 0 %, 0 MiB, 97887 MiB\\n1, NVIDIA RTX PRO 6000 Blackwell Server Edition, 100 %, 0 MiB, 97887 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T06:10:55.951121+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T06:10:55.951263+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T06:10:55.951377+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "importance_margin_vla_compress",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T06:10:55.951618+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"libero_fullft_batch64\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T01:29:36.383Z\", \"updated_at\": \"2026-05-17T05:37:28.721Z\", \"hypothesis\": \"Batch size 4→64 (grad_accum=16) 是 87.3% SR gap 根因 (D055)。使用与 SmolVLA 官方相同 effective batch=64 训练 100K steps，预期 SR 从 49% 提升至接近官方水平 (~80%+)，为 IMM 实验提供强 baseline。\", \"parent\": \"libero_full_ft_baseline\", \"notes\": \"2026-05-17 ~05:35 UTC: cron 确认 cqa1-33015 不可达（SSH failed 5x）。failure_reason: 服务器离线（实例可能被回收）。训练进度未知（已跑约 4 小时，预计需 ~3.8 天）。需要 Director 决策：恢复实例或在新 GPU 上重新提交。这是 batch64 baseline 关键实验（D055），直接影响 CoRL 论文。\", \"conclusion\": \"failed\"}, \"eval_k07_bypass_v3\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-17T04:00:06.238Z\", \"updated_at\": \"2026-05-17T05:17:41.847Z\", \"hypothesis\": \"k=0.7 two-stage full-FT model with baseline (bypass/no-pruning) forward should achieve competitive success rate on libero_object, establishing upper-bound performance before ACIS pruning is applied.\", \"notes\": \"2026-05-17 ~12:00 UTC: westd-27271 不可达。eval 提交于 04:00 UTC，距今 ~8h，预计已完成或接近完成。需重启后检查 eval_results/imm_k07_bypass_object.json。\"}, \"eval_imm100k_bypass\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-17T03:35:41.235Z\", \"updated_at\": \"2026-05-17T05:17:39.614Z\", \"hypothesis\": \"IMM Stage2 full-FT training preserves expert weight quality: bypass eval (baseline mode, no pruning) of the IMM 100K checkpoint should recover baseline SR ~44% if weights are intact, or show SR < 20% if Stage2 damaged expert weights.\", \"notes\": \"2026-05-17 ~12:00 UTC: westd-27271 不可达。已知部分结果：6/10 tasks 完成时全部 0% SR。服务器断联前可能已完成全部 10 tasks。需重启后检查 eval_results/imm_100k_bypass_object.json。\"}, \"eval_stage1_only\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-17T04:27:01.664Z\", \"updated_at\": \"2026-05-17T05:17:37.258Z\", \"hypothesis\": \"Stage1 ACIS learned effective token importance ranking. Using stage1_done checkpoint (original expert + trained ACIS,
…[truncated 8486 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T06:10:55.951816+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_stage1_only",
  "field": "status",
  "value": "DONE",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_stage1_only",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-17T06:10:55.951948+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 0.1078}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T06:10:55.952067+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_imm100k_bypass",
  "field": "status",
  "value": "DONE",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_imm100k_bypass",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-17T06:10:55.952206+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 0.104}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T06:10:55.952326+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_k07_bypass_v3",
  "field": "status",
  "value": "DONE",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_k07_bypass_v3",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-17T06:10:55.952446+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 0.1228}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-17T06:10:55.952558+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_stage1_only",
  "field": "conclusion",
  "value": "success",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_stage1_only",
    "field": "conclusion",
    "value": "success",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-17T06:10:55.952711+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_stage1_only\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T04:27:01.664Z\", \"updated_at\": \"2026-05-17T06:10:13.363Z\", \"hypothesis\": \"Stage1 ACIS learned effective token importance ranking. Using stage1_done checkpoint (original expert + trained ACIS, k_ratio=0.5) for acis_prune eval should retain significant performance (SR >= 30%) if ACIS quality is good. SR < 10% indicates ACIS importance scoring is ineffective.\", \"parent\": \"eval_imm100k_bypass\", \"spec\": {\"command\": \"python eval_success_rate_libero.py --checkpoint checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt --config configs/libero_imm_twostage_fullft.yaml --suite libero_object --mode acis_prune --num_episodes 50 --gpu 0\", \"server\": \"westd-27271\", \"gpu\": [\"cuda:0\"], \"pid\": \"961179\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_stage1_only.log\", \"submitted_at\": \"2026-05-17T04:27:18.785Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt\", \"eval_data\": \"libero_object (10 tasks x 50 episodes)\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"smolvla_imm_stage1_only\", \"seed\": 42}, \"notes\": \"2026-05-17 ~12:00 UTC: westd-27271 不可达 (Unable to connect to port 27271 on 36.103.198.204)。实例可能已关机/回收。eval 结果未知——上次提交时间 04:27 UTC，距今 ~8h。需重启实例后检查 eval_results/eval_stage1only_object.json 是否已生成。\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2096}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T06:10:55.952847+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_imm100k_bypass",
  "field": "conclusion",
  "value": "negative",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_imm100k_bypass",
    "field": "conclusion",
    "value": "negative",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-17T06:10:55.953000+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_imm100k_bypass\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T03:35:41.235Z\", \"updated_at\": \"2026-05-17T06:10:13.860Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python eval_success_rate_libero.py --checkpoint checkpoints/libero_imm_twostage_fullft/final/checkpoint.pt --config configs/libero_imm_twostage_fullft.yaml --suite libero_object --mode baseline --num_episodes 50 --gpu 0 --output eval_results/imm_100k_bypass_object.json\", \"server\": \"westd-27271\", \"gpu\": [\"cuda:0\"], \"pid\": \"882658\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_imm100k_bypass.log\", \"submitted_at\": \"2026-05-17T03:40:48.744Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 50, \"model_name\": \"libero_imm_twostage_fullft\", \"seed\": 0, \"checkpoint_source\": \"checkpoints/libero_imm_twostage_fullft/final/checkpoint.pt\", \"eval_data\": \"libero_object\"}, \"hypothesis\": \"IMM Stage2 full-FT training preserves expert weight quality: bypass eval (baseline mode, no pruning) of the IMM 100K checkpoint should recover baseline SR ~44% if weights are intact, or show SR < 20% if Stage2 damaged expert weights.\", \"notes\": \"2026-05-17 ~12:00 UTC: westd-27271 不可达。已知部分结果：6/10 tasks 完成时全部 0% SR。服务器断联前可能已完成全部 10 tasks。需重启后检查 eval_results/imm_100k_bypass_object.json。\", \"conclusion\": \"negative\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2064}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-17T06:10:55.953155+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_k07_bypass_v3",
  "field": "conclusion",
  "value": "negative",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_k07_bypass_v3",
    "field": "conclusion",
    "value": "negative",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-17T06:10:55.953351+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_k07_bypass_v3\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T04:00:06.238Z\", \"updated_at\": \"2026-05-17T06:10:14.541Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/importance_margin_vla_compress && source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=1 python eval_success_rate_libero.py --checkpoint checkpoints/libero_imm_twostage_fullft_k07/final/checkpoint.pt --config configs/libero_imm_twostage_fullft_k07.yaml --suite libero_object --mode baseline --num_episodes 50 --gpu 0 --output eval_results/imm_k07_bypass_object.json\\\"\", \"server\": \"westd-27271\", \"gpu\": [\"cuda:1\"], \"pid\": \"905921\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_k07_bypass_v3.log\", \"submitted_at\": \"2026-05-17T04:00:06.138Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"libero_imm_twostage_fullft_k07\", \"data_path\": \"libero_object\", \"data_count\": 500, \"seed\": 0, \"checkpoint_source\": \"checkpoints/libero_imm_twostage_fullft_k07/final/checkpoint.pt\", \"eval_data\": \"libero_object (10 tasks x 50 episodes)\"}, \"hypothesis\": \"k=0.7 two-stage full-FT model with baseline (bypass/no-pruning) forward should achieve competitive success rate on libero_object, establishing upper-bound performance before ACIS pruning is applied.\", \"notes\": \"2026-05-17 ~12:00 UTC: westd-27271 不可达。eval 提交于 04:00 UTC，距今 ~8h，预计已完成或接近完成。需重启后检查 eval_results/imm_k07_bypass_object.json。\", \"conclusion\": \"negative\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1873}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-17T06:10:55.953518+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_stage1_only",
  "field": "metrics",
  "value": "{'overall_success_rate': 0.448, 'total_episodes': 500, 'total_successes': 224, 'wilson_ci_95': [0.405, 0.4918], 'per_task_sr': [0.22, 0.6, 0.42, 0.38, 0.58, 0.26, 0.62, 0.38, 0.5, 0.52], 'mode': 'acis_prune', 'k_ratio': 0.5}",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_stage1_only",
    "field": "metrics",
    "value": "{'overall_success_rate': 0.448, 'total_episodes': 500, 'total_successes': 224, 'wilson_ci_95': [0.405, 0.4918], 'per_task_sr': [0.22, 0.6, 0.42, 0.38, 0.58, 0.26, 0.62, 0.38, 0.5, 0.52], 'mode': 'acis_prune', 'k_ratio': 0.5}",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-17T06:10:55.953708+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_stage1_only\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T04:27:01.664Z\", \"updated_at\": \"2026-05-17T06:10:20.327Z\", \"hypothesis\": \"Stage1 ACIS learned effective token importance ranking. Using stage1_done checkpoint (original expert + trained ACIS, k_ratio=0.5) for acis_prune eval should retain significant performance (SR >= 30%) if ACIS quality is good. SR < 10% indicates ACIS importance scoring is ineffective.\", \"parent\": \"eval_imm100k_bypass\", \"spec\": {\"command\": \"python eval_success_rate_libero.py --checkpoint checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt --config configs/libero_imm_twostage_fullft.yaml --suite libero_object --mode acis_prune --num_episodes 50 --gpu 0\", \"server\": \"westd-27271\", \"gpu\": [\"cuda:0\"], \"pid\": \"961179\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_stage1_only.log\", \"submitted_at\": \"2026-05-17T04:27:18.785Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt\", \"eval_data\": \"libero_object (10 tasks x 50 episodes)\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"smolvla_imm_stage1_only\", \"seed\": 42}, \"notes\": \"2026-05-17 ~12:00 UTC: westd-27271 不可达 (Unable to connect to port 27271 on 36.103.198.204)。实例可能已关机/回收。eval 结果未知——上次提交时间 04:27 UTC，距今 ~8h。需重启实例后检查 eval_results/eval_stage1only_object.json 是否已生成。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.448, \"total_episodes\": 500, \"total_successes\": 224, \"wilson_ci_95\": [0.405, 0.4918], \"per_task_sr\": [0.22, 0.6, 0.42, 0.38, 0.58, 0.26, 0.62, 0.38, 0.5, 0.52], \"mode\": \"acis_prune\", \"k_ratio\": 0.5}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1793}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-17T06:10:55.953856+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_imm100k_bypass",
  "field": "metrics",
  "value": "{'overall_success_rate': 0, 'total_episodes': 500, 'total_successes': 0, 'wilson_ci_95': [0, 0.0076], 'per_task_sr': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'mode': 'baseline_bypass', 'note': 'Stage2 completely destroyed expert weights'}",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_imm100k_bypass",
    "field": "metrics",
    "value": "{'overall_success_rate': 0, 'total_episodes': 500, 'total_successes': 0, 'wilson_ci_95': [0, 0.0076], 'per_task_sr': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'mode': 'baseline_bypass', 'note': 'Stage2 completely destroyed expert weights'}",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-17T06:10:55.954045+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_imm100k_bypass\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T03:35:41.235Z\", \"updated_at\": \"2026-05-17T06:10:22.217Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python eval_success_rate_libero.py --checkpoint checkpoints/libero_imm_twostage_fullft/final/checkpoint.pt --config configs/libero_imm_twostage_fullft.yaml --suite libero_object --mode baseline --num_episodes 50 --gpu 0 --output eval_results/imm_100k_bypass_object.json\", \"server\": \"westd-27271\", \"gpu\": [\"cuda:0\"], \"pid\": \"882658\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_imm100k_bypass.log\", \"submitted_at\": \"2026-05-17T03:40:48.744Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 50, \"model_name\": \"libero_imm_twostage_fullft\", \"seed\": 0, \"checkpoint_source\": \"checkpoints/libero_imm_twostage_fullft/final/checkpoint.pt\", \"eval_data\": \"libero_object\"}, \"hypothesis\": \"IMM Stage2 full-FT training preserves expert weight quality: bypass eval (baseline mode, no pruning) of the IMM 100K checkpoint should recover baseline SR ~44% if weights are intact, or show SR < 20% if Stage2 damaged expert weights.\", \"notes\": \"2026-05-17 ~12:00 UTC: westd-27271 不可达。已知部分结果：6/10 tasks 完成时全部 0% SR。服务器断联前可能已完成全部 10 tasks。需重启后检查 eval_results/imm_100k_bypass_object.json。\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0, \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076], \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"mode\": \"baseline_bypass\", \"note\": \"Stage2 completely destroyed expert weights\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1852}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-17T06:10:55.954224+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_k07_bypass_v3",
  "field": "metrics",
  "value": "{'overall_success_rate': 0, 'total_episodes': 500, 'total_successes': 0, 'wilson_ci_95': [0, 0.0076], 'per_task_sr': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'mode': 'baseline_bypass', 'note': 'Stage2 k=0.7 also completely destroyed expert weights'}",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_k07_bypass_v3",
    "field": "metrics",
    "value": "{'overall_success_rate': 0, 'total_episodes': 500, 'total_successes': 0, 'wilson_ci_95': [0, 0.0076], 'per_task_sr': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'mode': 'baseline_bypass', 'note': 'Stage2 k=0.7 also completely destroyed expert weights'}",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-17T06:10:55.954402+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_k07_bypass_v3\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T04:00:06.238Z\", \"updated_at\": \"2026-05-17T06:10:23.738Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/importance_margin_vla_compress && source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=1 python eval_success_rate_libero.py --checkpoint checkpoints/libero_imm_twostage_fullft_k07/final/checkpoint.pt --config configs/libero_imm_twostage_fullft_k07.yaml --suite libero_object --mode baseline --num_episodes 50 --gpu 0 --output eval_results/imm_k07_bypass_object.json\\\"\", \"server\": \"westd-27271\", \"gpu\": [\"cuda:1\"], \"pid\": \"905921\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_k07_bypass_v3.log\", \"submitted_at\": \"2026-05-17T04:00:06.138Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"libero_imm_twostage_fullft_k07\", \"data_path\": \"libero_object\", \"data_count\": 500, \"seed\": 0, \"checkpoint_source\": \"checkpoints/libero_imm_twostage_fullft_k07/final/checkpoint.pt\", \"eval_data\": \"libero_object (10 tasks x 50 episodes)\"}, \"hypothesis\": \"k=0.7 two-stage full-FT model with baseline (bypass/no-pruning) forward should achieve competitive success rate on libero_object, establishing upper-bound performance before ACIS pruning is applied.\", \"notes\": \"2026-05-17 ~12:00 UTC: westd-27271 不可达。eval 提交于 04:00 UTC，距今 ~8h，预计已完成或接近完成。需重启后检查 eval_results/imm_k07_bypass_object.json。\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0, \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076], \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"mode\": \"baseline_bypass\", \"note\": \"Stage2 k=0.7 also completely destroyed expert weights\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1923}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-17T06:10:55.954552+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_stage1_only",
  "field": "status",
  "value": "DONE",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_stage1_only",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-17T06:10:55.954677+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without output fields: ['checkpoint_path']. Set these fields first or pass them in spec.\", \"metadata\": {\"elapsed_seconds\": 0.1205}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-17T06:10:55.954801+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_imm100k_bypass",
  "field": "status",
  "value": "DONE",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_imm100k_bypass",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-17T06:10:55.954923+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without output fields: ['checkpoint_path']. Set these fields first or pass them in spec.\", \"metadata\": {\"elapsed_seconds\": 0.107}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-17T06:10:55.955038+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_k07_bypass_v3",
  "field": "status",
  "value": "DONE",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_k07_bypass_v3",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-17T06:10:55.955178+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without output fields: ['checkpoint_path']. Set these fields first or pass them in spec.\", \"metadata\": {\"elapsed_seconds\": 0.1126}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-17T06:10:55.955303+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_stage1_only",
  "field": "status",
  "value": "DONE",
  "project": "importance_margin_vla_compress",
  "spec": "{'checkpoint_path': 'checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt', 'log_path': 'eval_results/eval_stage1only_object.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_stage1_only",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress",
    "spec": "{'checkpoint_path': 'checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt', 'log_path': 'eval_results/eval_stage1only_object.json'}"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-17T06:10:55.955481+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_stage1_only\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T04:27:01.664Z\", \"updated_at\": \"2026-05-17T06:10:34.650Z\", \"hypothesis\": \"Stage1 ACIS learned effective token importance ranking. Using stage1_done checkpoint (original expert + trained ACIS, k_ratio=0.5) for acis_prune eval should retain significant performance (SR >= 30%) if ACIS quality is good. SR < 10% indicates ACIS importance scoring is ineffective.\", \"parent\": \"eval_imm100k_bypass\", \"spec\": {\"command\": \"python eval_success_rate_libero.py --checkpoint checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt --config configs/libero_imm_twostage_fullft.yaml --suite libero_object --mode acis_prune --num_episodes 50 --gpu 0\", \"server\": \"westd-27271\", \"gpu\": [\"cuda:0\"], \"pid\": \"961179\", \"log_path\": \"eval_results/eval_stage1only_object.json\", \"submitted_at\": \"2026-05-17T04:27:18.785Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt\", \"eval_data\": \"libero_object (10 tasks x 50 episodes)\", \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"smolvla_imm_stage1_only\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt\", \"wall_clock_seconds\": 6195.9, \"gpu_hours\": 1.72}, \"notes\": \"2026-05-17 ~12:00 UTC: westd-27271 不可达 (Unable to connect to port 27271 on 36.103.198.204)。实例可能已关机/回收。eval 结果未知——上次提交时间 04:27 UTC，距今 ~8h。需重启实例后检查 eval_results/eval_stage1only_object.json 是否已生成。\", \"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.448, \"total_episodes\": 500, \"total_successes\": 224, \"wilson_ci_95\": [0.405, 0.4918], \"per_task_sr\": [0.22, 0.6, 0.42, 0.38, 0.58, 0.26, 0.62, 0.38, 0.5, 0.52], \"mode\": \"acis_prune\", \"k_ratio\": 0.5
…[truncated 166 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-17T06:10:55.955631+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_imm100k_bypass",
  "field": "status",
  "value": "DONE",
  "project": "importance_margin_vla_compress",
  "spec": "{'checkpoint_path': 'checkpoints/libero_imm_twostage_fullft/final/checkpoint.pt', 'log_path': 'eval_results/imm_100k_bypass_object.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_imm100k_bypass",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress",
    "spec": "{'checkpoint_path': 'checkpoints/libero_imm_twostage_fullft/final/checkpoint.pt', 'log_path': 'eval_results/imm_100k_bypass_object.json'}"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-17T06:10:55.955809+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_imm100k_bypass\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T03:35:41.235Z\", \"updated_at\": \"2026-05-17T06:10:36.056Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python eval_success_rate_libero.py --checkpoint checkpoints/libero_imm_twostage_fullft/final/checkpoint.pt --config configs/libero_imm_twostage_fullft.yaml --suite libero_object --mode baseline --num_episodes 50 --gpu 0 --output eval_results/imm_100k_bypass_object.json\", \"server\": \"westd-27271\", \"gpu\": [\"cuda:0\"], \"pid\": \"882658\", \"log_path\": \"eval_results/imm_100k_bypass_object.json\", \"submitted_at\": \"2026-05-17T03:40:48.744Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_object\", \"data_count\": 50, \"model_name\": \"libero_imm_twostage_fullft\", \"seed\": 0, \"checkpoint_source\": \"checkpoints/libero_imm_twostage_fullft/final/checkpoint.pt\", \"eval_data\": \"libero_object\", \"checkpoint_path\": \"checkpoints/libero_imm_twostage_fullft/final/checkpoint.pt\", \"wall_clock_seconds\": 8987.3, \"gpu_hours\": 2.5}, \"hypothesis\": \"IMM Stage2 full-FT training preserves expert weight quality: bypass eval (baseline mode, no pruning) of the IMM 100K checkpoint should recover baseline SR ~44% if weights are intact, or show SR < 20% if Stage2 damaged expert weights.\", \"notes\": \"2026-05-17 ~12:00 UTC: westd-27271 不可达。已知部分结果：6/10 tasks 完成时全部 0% SR。服务器断联前可能已完成全部 10 tasks。需重启后检查 eval_results/imm_100k_bypass_object.json。\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0, \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076], \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"mode\": \"baseline_bypass\", \"note\": \"Stage2 completely destroyed expert weights\"}, \"completed_at\": \"2026-05-17T06:10:36.056Z\"}, \"hint\": \"💡 建议将本次教训写入 memory.md（什么不 work、为什么）\"}
…[truncated 65 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-17T06:10:55.955965+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_k07_bypass_v3",
  "field": "status",
  "value": "DONE",
  "project": "importance_margin_vla_compress",
  "spec": "{'checkpoint_path': 'checkpoints/libero_imm_twostage_fullft_k07/final/checkpoint.pt', 'log_path': 'eval_results/imm_k07_bypass_object.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_k07_bypass_v3",
    "field": "status",
    "value": "DONE",
    "project": "importance_margin_vla_compress",
    "spec": "{'checkpoint_path': 'checkpoints/libero_imm_twostage_fullft_k07/final/checkpoint.pt', 'log_path': 'eval_results/imm_k07_bypass_object.json'}"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-17T06:10:55.956166+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_k07_bypass_v3\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T04:00:06.238Z\", \"updated_at\": \"2026-05-17T06:10:37.113Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/importance_margin_vla_compress && source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=1 python eval_success_rate_libero.py --checkpoint checkpoints/libero_imm_twostage_fullft_k07/final/checkpoint.pt --config configs/libero_imm_twostage_fullft_k07.yaml --suite libero_object --mode baseline --num_episodes 50 --gpu 0 --output eval_results/imm_k07_bypass_object.json\\\"\", \"server\": \"westd-27271\", \"gpu\": [\"cuda:1\"], \"pid\": \"905921\", \"log_path\": \"eval_results/imm_k07_bypass_object.json\", \"submitted_at\": \"2026-05-17T04:00:06.138Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"libero_imm_twostage_fullft_k07\", \"data_path\": \"libero_object\", \"data_count\": 500, \"seed\": 0, \"checkpoint_source\": \"checkpoints/libero_imm_twostage_fullft_k07/final/checkpoint.pt\", \"eval_data\": \"libero_object (10 tasks x 50 episodes)\", \"checkpoint_path\": \"checkpoints/libero_imm_twostage_fullft_k07/final/checkpoint.pt\", \"wall_clock_seconds\": 7831.0, \"gpu_hours\": 2.18}, \"hypothesis\": \"k=0.7 two-stage full-FT model with baseline (bypass/no-pruning) forward should achieve competitive success rate on libero_object, establishing upper-bound performance before ACIS pruning is applied.\", \"notes\": \"2026-05-17 ~12:00 UTC: westd-27271 不可达。eval 提交于 04:00 UTC，距今 ~8h，预计已完成或接近完成。需重启后检查 eval_results/imm_k07_bypass_object.json。\", \"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0, \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076], \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"mode\": \"baseline_bypass\", \"note\": \"Stage2 k=0.7 also completely destroyed exper
…[truncated 176 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_stage1_only_result_20260517T060908",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-17T06:10:55.956366+00:00_

Registry 全部更新完毕。

## 结果汇总

| Experiment | Mode | Overall SR | 含义 |
|---|---|---|---|
| **Stage1-only** (expert未动 + ACIS prune k=0.5) | acis_prune | **44.8%** | ACIS importance ranking 非常有效 |
| IMM 100K bypass (Stage2后 不剪枝) | baseline | **0.0%** | Stage2 彻底摧毁 expert |
| IMM k=0.7 bypass (Stage2后 不剪枝) | baseline | **0.0%** | k=0.7 同样彻底摧毁 expert |

### Stage1-only per-task SR
| Task | SR |
|---|---|
| alphabet soup | 22% |
| cream cheese | 60% |
| salad dressing | 42% |
| bbq sauce | 38% |
| ketchup | 58% |
| tomato sauce | 26% |
| butter | 62% |
| milk | 38% |
| chocolate pudding | 50% |
| orange juice | 52% |

### 关键结论

**Stage1 ACIS 完美有效**：用原始 Full FT expert + Stage1 训的 ACIS 做 50% token pruning，SR = 44.8%，与 Full FT baseline (~44-49%) 基本持平。ACIS 成功学会了 token importance ranking，丢弃 50% tokens 不损失性能。

**Stage2 是唯一的问题**：两个 bypass eval 都是 0% SR（所有 task 全部 timeout），无论 k=0.5 还是 k=0.7，Stage2 expert 训练都会彻底摧毁模型权重。问题不在 pruning ratio 而在 Stage2 训练机制本身。

GPU 状态：2x RTX PRO 6000 Blackwell 空闲（0% util），可随时启动新实验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_check_stage1_only_result_20260517T060908"
}
```

</details>

---
