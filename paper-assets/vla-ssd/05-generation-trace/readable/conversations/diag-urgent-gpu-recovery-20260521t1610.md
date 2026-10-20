# diag urgent gpu recovery 20260521T1610

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 0
- **Tool calls:** 26
- **Original source:** `logs/chats/worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754.jsonl`
- **Structured JSON:** [`31c4e4328a98c692a5cf.json`](../../sessions/31/31c4e4328a98c692a5cf.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

53 recorded events

### Tool call

_source line 1 · 2026-05-21T16:19:59.550686+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__detect_image",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__detect_image",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T16:19:59.551075+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T16:19:59.551273+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls -la /root/autodl-tmp/vla-ssd/results/libero_long/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls -la /root/autodl-tmp/vla-ssd/results/libero_long/"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T16:19:59.551410+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /tmp/exp_openvla_long_pipeline_v1.log 2>/dev/null | tail -100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /tmp/exp_openvla_long_pipeline_v1.log 2>/dev/null | tail -100"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-21T16:19:59.551568+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 40\\ndrwxr-xr-x  2 root root  159 May 22 00:13 .\\ndrwxr-xr-x 55 root root 8192 May 22 00:11 ..\\n-rw-r--r--  1 root root 6372 May 21 23:55 action_r2_probing.json\\n-rw-r--r--  1 root root 1727 May 21 23:59 cross_instruction_classification.json\\n-rw-r--r--  1 root root 4665 May 21 23:55 l1_attention_profile.json\\n-rw-r--r--  1 root root 7360 May 21 23:59 rsa_analysis.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T16:19:59.551719+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T16:19:59.551846+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls -la /root/autodl-tmp/vla-ssd/results/tracvla_spatial/untrained/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls -la /root/autodl-tmp/vla-ssd/results/tracvla_spatial/untrained/"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T16:19:59.552010+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 20\\ndrwxr-xr-x 2 root root  130 May 22 00:06 .\\ndrwxr-xr-x 4 root root   50 May 21 23:44 ..\\n-rw-r--r-- 1 root root 6376 May 22 00:01 action_r2_probing.json\\n-rw-r--r-- 1 root root 1729 May 22 00:06 cross_instruction_classification.json\\n-rw-r--r-- 1 root root 5087 May 22 00:01 l1_attention_profile.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T16:19:59.552148+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ps -p 521837 -o pid= 2>/dev/null && echo \"STILL_RUNNING\" || echo \"DEAD\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ps -p 521837 -o pid= 2>/dev/null && echo \"STILL_RUNNING\" || echo \"DEAD\""
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T16:19:59.552277+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '&&' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T16:19:59.552411+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls -la /root/autodl-tmp/vla-ssd/results/tracvla_spatial/trained/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls -la /root/autodl-tmp/vla-ssd/results/tracvla_spatial/trained/"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T16:19:59.552536+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "nvidia-smi --query-gpu=index,utilization.gpu,memory.used,memory.total --format=csv,noheader"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "nvidia-smi --query-gpu=index,utilization.gpu,memory.used,memory.total --format=csv,noheader"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-21T16:19:59.552665+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 52\\ndrwxr-xr-x 2 root root   170 May 21 10:04 .\\ndrwxr-xr-x 4 root root    50 May 21 23:44 ..\\n-rw-r--r-- 1 root root  6360 May 21 18:57 action_r2_probing.json\\n-rw-r--r-- 1 root root 31744 May 21 21:21 counterfactual_combined.json\\n-rw-r--r-- 1 root root  1731 May 21 19:09 cross_instruction_classification.json\\n-rw-r--r-- 1 root root  5040 May 21 18:57 l1_attention_profile.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T16:19:59.552789+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 0 %, 0 MiB, 97887 MiB\\n1, 0 %, 0 MiB, 97887 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.58}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T16:19:59.552950+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls -la /root/autodl-tmp/vla-ssd/scripts/tracvla_long_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls -la /root/autodl-tmp/vla-ssd/scripts/tracvla_long_full_pipeline.py"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T16:19:59.553102+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls -la /root/autodl-tmp/vla-ssd/scripts/tracvla_goal_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls -la /root/autodl-tmp/vla-ssd/scripts/tracvla_goal_full_pipeline.py"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-21T16:19:59.553231+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 24747 May 22 00:00 /root/autodl-tmp/vla-ssd/scripts/tracvla_long_full_pipeline.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T16:19:59.553353+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 23334 May 22 00:00 /root/autodl-tmp/vla-ssd/scripts/tracvla_goal_full_pipeline.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T16:19:59.553515+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "tail -100 /tmp/exp_openvla_long_pipeline_v1.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "tail -100 /tmp/exp_openvla_long_pipeline_v1.log"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T16:19:59.553645+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"tail: cannot open '/tmp/exp_openvla_long_pipeline_v1.log' for reading: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T16:19:59.553764+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls /tmp/exp_openvla_long_pipeline_v1*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls /tmp/exp_openvla_long_pipeline_v1*"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T16:19:59.553885+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/tmp/exp_openvla_long_pipeline_v1*': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T16:19:59.554076+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ps -p 521837 -o pid="
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ps -p 521837 -o pid="
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-21T16:19:59.554235+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.47}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T16:19:59.554357+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/tracvla_spatial/untrained/action_r2_probing.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/tracvla_spatial/untrained/action_r2_probing.json"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-21T16:19:59.554475+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/tracvla_spatial/untrained/l1_attention_profile.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/tracvla_spatial/untrained/l1_attention_profile.json"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-21T16:19:59.554747+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"L0_image_mean\\\": {\\n    \\\"mean\\\": 0.7761,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.7761\\n    ]\\n  },\\n  \\\"L0_last_preaction\\\": {\\n    \\\"mean\\\": 0.5911,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.5911\\n    ]\\n  },\\n  \\\"L1_image_mean\\\": {\\n    \\\"mean\\\": 0.7761,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.7761\\n    ]\\n  },\\n  \\\"L1_last_preaction\\\": {\\n    \\\"mean\\\": 0.6226,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.6226\\n    ]\\n  },\\n  \\\"L2_image_mean\\\": {\\n    \\\"mean\\\": 0.7779,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.7779\\n    ]\\n  },\\n  \\\"L2_last_preaction\\\": {\\n    \\\"mean\\\": 0.6833,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.6833\\n    ]\\n  },\\n  \\\"L3_image_mean\\\": {\\n    \\\"mean\\\": 0.7789,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.7789\\n    ]\\n  },\\n  \\\"L3_last_preaction\\\": {\\n    \\\"mean\\\": 0.6868,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.6868\\n    ]\\n  },\\n  \\\"L4_image_mean\\\": {\\n    \\\"mean\\\": 0.7812,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.7812\\n    ]\\n  },\\n  \\\"L4_last_preaction\\\": {\\n    \\\"mean\\\": 0.7132,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.7132\\n    ]\\n  },\\n  \\\"L5_image_mean\\\": {\\n    \\\"mean\\\": 0.7839,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.7839\\n    ]\\n  },\\n  \\\"L5_last_preaction\\\": {\\n    \\\"mean\\\": 0.7177,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.7177\\n    ]\\n  },\\n  \\\"L6_image_mean\\\": {\\n    \\\"mean\\\": 0.7856,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.7856\\n    ]\\n  },\\n  \\\"L6_last_preaction\\\": {\\n    \\\"mean\\\": 0.7189,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.7189\\n    ]\\n  },\\n  \\\"L7_image_mean\\\
…[truncated 6970 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T16:19:59.555076+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"per_head\\\": {\\n    \\\"head_0\\\": {\\n      \\\"instruction_ratio_mean\\\": 0.9532,\\n      \\\"instruction_ratio_std\\\": 0.0028,\\n      \\\"category\\\": \\\"instruction_dominant\\\"\\n    },\\n    \\\"head_1\\\": {\\n      \\\"instruction_ratio_mean\\\": 0.9592,\\n      \\\"instruction_ratio_std\\\": 0.0038,\\n      \\\"category\\\": \\\"instruction_dominant\\\"\\n    },\\n    \\\"head_2\\\": {\\n      \\\"instruction_ratio_mean\\\": 0.569,\\n      \\\"instruction_ratio_std\\\": 0.0111,\\n      \\\"category\\\": \\\"instruction_dominant\\\"\\n    },\\n    \\\"head_3\\\": {\\n      \\\"instruction_ratio_mean\\\": 0.7949,\\n      \\\"instruction_ratio_std\\\": 0.0128,\\n      \\\"category\\\": \\\"instruction_dominant\\\"\\n    },\\n    \\\"head_4\\\": {\\n      \\\"instruction_ratio_mean\\\": 0.7255,\\n      \\\"instruction_ratio_std\\\": 0.0106,\\n      \\\"category\\\": \\\"instruction_dominant\\\"\\n    },\\n    \\\"head_5\\\": {\\n      \\\"instruction_ratio_mean\\\": 0.6261,\\n      \\\"instruction_ratio_std\\\": 0.0288,\\n      \\\"category\\\": \\\"instruction_dominant\\\"\\n    },\\n    \\\"head_6\\\": {\\n      \\\"instruction_ratio_mean\\\": 0.7003,\\n      \\\"instruction_ratio_std\\\": 0.0164,\\n      \\\"category\\\": \\\"instruction_dominant\\\"\\n    },\\n    \\\"head_7\\\": {\\n      \\\"instruction_ratio_mean\\\": 0.7976,\\n      \\\"instruction_ratio_std\\\": 0.009,\\n      \\\"category\\\": \\\"instruction_dominant\\\"\\n    },\\n    \\\"head_8\\\": {\\n      \\\"instruction_ratio_mean\\\": 0.9961,\\n      \\\"instruction_ratio_std\\\": 0.0004,\\n      \\\"category\\\": \\\"instruction_dominant\\\"\\n    },\\n    \\\"head_9\\\": {\\n      \\\"instruction_ratio_mean\\\": 0.912,\\n      \\\"instruction_ratio_std\\\": 0.0042,\\n      \\\"category\\\": \\\"instruction_dominant\\\"\\n    },\\n    \\\"head_10\\\": {\\n      \\\"instruction_ratio_mean\\\": 0.8347,\\n      \\\"instru
…[truncated 4655 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T16:19:59.555272+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/tracvla_spatial/untrained/cross_instruction_classification.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/tracvla_spatial/untrained/cross_instruction_classification.json"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-21T16:19:59.555409+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/tracvla_spatial/trained/action_r2_probing.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/tracvla_spatial/trained/action_r2_probing.json"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-21T16:19:59.555604+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"chance\\\": 0.1,\\n  \\\"L0_image_mean\\\": 1.0,\\n  \\\"L0_last_preaction\\\": 0.977,\\n  \\\"L1_image_mean\\\": 1.0,\\n  \\\"L1_last_preaction\\\": 1.0,\\n  \\\"L2_image_mean\\\": 1.0,\\n  \\\"L2_last_preaction\\\": 1.0,\\n  \\\"L3_image_mean\\\": 1.0,\\n  \\\"L3_last_preaction\\\": 1.0,\\n  \\\"L4_image_mean\\\": 1.0,\\n  \\\"L4_last_preaction\\\": 1.0,\\n  \\\"L5_image_mean\\\": 1.0,\\n  \\\"L5_last_preaction\\\": 1.0,\\n  \\\"L6_image_mean\\\": 1.0,\\n  \\\"L6_last_preaction\\\": 1.0,\\n  \\\"L7_image_mean\\\": 1.0,\\n  \\\"L7_last_preaction\\\": 1.0,\\n  \\\"L8_image_mean\\\": 1.0,\\n  \\\"L8_last_preaction\\\": 1.0,\\n  \\\"L9_image_mean\\\": 1.0,\\n  \\\"L9_last_preaction\\\": 1.0,\\n  \\\"L10_image_mean\\\": 1.0,\\n  \\\"L10_last_preaction\\\": 1.0,\\n  \\\"L11_image_mean\\\": 1.0,\\n  \\\"L11_last_preaction\\\": 1.0,\\n  \\\"L12_image_mean\\\": 1.0,\\n  \\\"L12_last_preaction\\\": 1.0,\\n  \\\"L13_image_mean\\\": 1.0,\\n  \\\"L13_last_preaction\\\": 1.0,\\n  \\\"L14_image_mean\\\": 1.0,\\n  \\\"L14_last_preaction\\\": 1.0,\\n  \\\"L15_image_mean\\\": 1.0,\\n  \\\"L15_last_preaction\\\": 1.0,\\n  \\\"L16_image_mean\\\": 1.0,\\n  \\\"L16_last_preaction\\\": 1.0,\\n  \\\"L17_image_mean\\\": 1.0,\\n  \\\"L17_last_preaction\\\": 1.0,\\n  \\\"L18_image_mean\\\": 1.0,\\n  \\\"L18_last_preaction\\\": 1.0,\\n  \\\"L19_image_mean\\\": 1.0,\\n  \\\"L19_last_preaction\\\": 1.0,\\n  \\\"L20_image_mean\\\": 1.0,\\n  \\\"L20_last_preaction\\\": 1.0,\\n  \\\"L21_image_mean\\\": 1.0,\\n  \\\"L21_last_preaction\\\": 1.0,\\n  \\\"L22_image_mean\\\": 1.0,\\n  \\\"L22_last_preaction\\\": 1.0,\\n  \\\"L23_image_mean\\\": 1.0,\\n  \\\"L23_last_preaction\\\": 1.0,\\n  \\\"L24_image_mean\\\": 1.0,\\n  \\\"L24_last_preaction\\\": 1.0,\\n  \\\"L25_image_mean\\\": 1.0,\\n  \\\"L25_last_preaction\\\": 1.0,\\n  \\\"L26_image_mean\\\": 1.0,\\n  \\\"L26_last_preaction\\\": 1.0,\\n  \\\"L27_image_mean\\\": 1.0,\\n  \\\"L27_
…[truncated 411 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T16:19:59.555940+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"L0_image_mean\\\": {\\n    \\\"mean\\\": 0.8059,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.8059\\n    ]\\n  },\\n  \\\"L0_last_preaction\\\": {\\n    \\\"mean\\\": 0.6656,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.6656\\n    ]\\n  },\\n  \\\"L1_image_mean\\\": {\\n    \\\"mean\\\": 0.8055,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.8055\\n    ]\\n  },\\n  \\\"L1_last_preaction\\\": {\\n    \\\"mean\\\": 0.7359,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.7359\\n    ]\\n  },\\n  \\\"L2_image_mean\\\": {\\n    \\\"mean\\\": 0.8053,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.8053\\n    ]\\n  },\\n  \\\"L2_last_preaction\\\": {\\n    \\\"mean\\\": 0.7681,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.7681\\n    ]\\n  },\\n  \\\"L3_image_mean\\\": {\\n    \\\"mean\\\": 0.8064,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.8064\\n    ]\\n  },\\n  \\\"L3_last_preaction\\\": {\\n    \\\"mean\\\": 0.791,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.791\\n    ]\\n  },\\n  \\\"L4_image_mean\\\": {\\n    \\\"mean\\\": 0.8091,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.8091\\n    ]\\n  },\\n  \\\"L4_last_preaction\\\": {\\n    \\\"mean\\\": 0.7954,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.7954\\n    ]\\n  },\\n  \\\"L5_image_mean\\\": {\\n    \\\"mean\\\": 0.8117,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.8117\\n    ]\\n  },\\n  \\\"L5_last_preaction\\\": {\\n    \\\"mean\\\": 0.794,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.794\\n    ]\\n  },\\n  \\\"L6_image_mean\\\": {\\n    \\\"mean\\\": 0.8145,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.8145\\n    ]\\n  },\\n  \\\"L6_last_preaction\\\": {\\n    \\\"mean\\\": 0.8009,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.8009\\n    ]\\n  },\\n  \\\"L7_image_mean\\\": {
…[truncated 6954 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T16:19:59.556110+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/tracvla_spatial/trained/l1_attention_profile.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/tracvla_spatial/trained/l1_attention_profile.json"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-21T16:19:59.556340+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"per_head\\\": {\\n    \\\"head_0\\\": {\\n      \\\"instruction_ratio_mean\\\": 0.7358,\\n      \\\"instruction_ratio_std\\\": 0.0169,\\n      \\\"category\\\": \\\"instruction_dominant\\\"\\n    },\\n    \\\"head_1\\\": {\\n      \\\"instruction_ratio_mean\\\": 0.8394,\\n      \\\"instruction_ratio_std\\\": 0.0111,\\n      \\\"category\\\": \\\"instruction_dominant\\\"\\n    },\\n    \\\"head_2\\\": {\\n      \\\"instruction_ratio_mean\\\": 0.5141,\\n      \\\"instruction_ratio_std\\\": 0.0301,\\n      \\\"category\\\": \\\"instruction_dominant\\\"\\n    },\\n    \\\"head_3\\\": {\\n      \\\"instruction_ratio_mean\\\": 0.5214,\\n      \\\"instruction_ratio_std\\\": 0.011,\\n      \\\"category\\\": \\\"instruction_dominant\\\"\\n    },\\n    \\\"head_4\\\": {\\n      \\\"instruction_ratio_mean\\\": 0.7419,\\n      \\\"instruction_ratio_std\\\": 0.016,\\n      \\\"category\\\": \\\"instruction_dominant\\\"\\n    },\\n    \\\"head_5\\\": {\\n      \\\"instruction_ratio_mean\\\": 0.5683,\\n      \\\"instruction_ratio_std\\\": 0.0152,\\n      \\\"category\\\": \\\"instruction_dominant\\\"\\n    },\\n    \\\"head_6\\\": {\\n      \\\"instruction_ratio_mean\\\": 0.5244,\\n      \\\"instruction_ratio_std\\\": 0.0288,\\n      \\\"category\\\": \\\"instruction_dominant\\\"\\n    },\\n    \\\"head_7\\\": {\\n      \\\"instruction_ratio_mean\\\": 0.5983,\\n      \\\"instruction_ratio_std\\\": 0.0159,\\n      \\\"category\\\": \\\"instruction_dominant\\\"\\n    },\\n    \\\"head_8\\\": {\\n      \\\"instruction_ratio_mean\\\": 0.9451,\\n      \\\"instruction_ratio_std\\\": 0.0044,\\n      \\\"category\\\": \\\"instruction_dominant\\\"\\n    },\\n    \\\"head_9\\\": {\\n      \\\"instruction_ratio_mean\\\": 0.7804,\\n      \\\"instruction_ratio_std\\\": 0.009,\\n      \\\"category\\\": \\\"instruction_dominant\\\"\\n    },\\n    \\\"head_10\\\": {\\n      \\\"instruction_ratio_mean\\\": 0.6205,\\n      \\\"instru
…[truncated 4604 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T16:19:59.556499+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/tracvla_spatial/trained/cross_instruction_classification.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/tracvla_spatial/trained/cross_instruction_classification.json"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-21T16:19:59.556670+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"chance\\\": 0.1,\\n  \\\"L0_image_mean\\\": 1.0,\\n  \\\"L0_last_preaction\\\": 0.923,\\n  \\\"L1_image_mean\\\": 1.0,\\n  \\\"L1_last_preaction\\\": 0.998,\\n  \\\"L2_image_mean\\\": 1.0,\\n  \\\"L2_last_preaction\\\": 1.0,\\n  \\\"L3_image_mean\\\": 1.0,\\n  \\\"L3_last_preaction\\\": 1.0,\\n  \\\"L4_image_mean\\\": 1.0,\\n  \\\"L4_last_preaction\\\": 1.0,\\n  \\\"L5_image_mean\\\": 1.0,\\n  \\\"L5_last_preaction\\\": 1.0,\\n  \\\"L6_image_mean\\\": 1.0,\\n  \\\"L6_last_preaction\\\": 1.0,\\n  \\\"L7_image_mean\\\": 1.0,\\n  \\\"L7_last_preaction\\\": 1.0,\\n  \\\"L8_image_mean\\\": 1.0,\\n  \\\"L8_last_preaction\\\": 1.0,\\n  \\\"L9_image_mean\\\": 1.0,\\n  \\\"L9_last_preaction\\\": 1.0,\\n  \\\"L10_image_mean\\\": 1.0,\\n  \\\"L10_last_preaction\\\": 1.0,\\n  \\\"L11_image_mean\\\": 1.0,\\n  \\\"L11_last_preaction\\\": 1.0,\\n  \\\"L12_image_mean\\\": 1.0,\\n  \\\"L12_last_preaction\\\": 1.0,\\n  \\\"L13_image_mean\\\": 1.0,\\n  \\\"L13_last_preaction\\\": 1.0,\\n  \\\"L14_image_mean\\\": 1.0,\\n  \\\"L14_last_preaction\\\": 1.0,\\n  \\\"L15_image_mean\\\": 1.0,\\n  \\\"L15_last_preaction\\\": 1.0,\\n  \\\"L16_image_mean\\\": 1.0,\\n  \\\"L16_last_preaction\\\": 1.0,\\n  \\\"L17_image_mean\\\": 1.0,\\n  \\\"L17_last_preaction\\\": 1.0,\\n  \\\"L18_image_mean\\\": 1.0,\\n  \\\"L18_last_preaction\\\": 1.0,\\n  \\\"L19_image_mean\\\": 1.0,\\n  \\\"L19_last_preaction\\\": 1.0,\\n  \\\"L20_image_mean\\\": 1.0,\\n  \\\"L20_last_preaction\\\": 1.0,\\n  \\\"L21_image_mean\\\": 1.0,\\n  \\\"L21_last_preaction\\\": 1.0,\\n  \\\"L22_image_mean\\\": 1.0,\\n  \\\"L22_last_preaction\\\": 1.0,\\n  \\\"L23_image_mean\\\": 1.0,\\n  \\\"L23_last_preaction\\\": 1.0,\\n  \\\"L24_image_mean\\\": 1.0,\\n  \\\"L24_last_preaction\\\": 1.0,\\n  \\\"L25_image_mean\\\": 1.0,\\n  \\\"L25_last_preaction\\\": 1.0,\\n  \\\"L26_image_mean\\\": 1.0,\\n  \\\"L26_last_preaction\\\": 1.0,\\n  \\\"L27_image_mean\\\": 1.0,\\n  \\\"L2
…[truncated 413 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-21T16:19:59.556819+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/tracvla_spatial/trained/counterfactual_combined.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/tracvla_spatial/trained/counterfactual_combined.json"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-21T16:19:59.557129+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"experiment\\\": \\\"counterfactual_tracvla_spatial\\\",\\n    \\\"conditions\\\": [\\n      \\\"wrong\\\",\\n      \\\"empty\\\",\\n      \\\"shuffled\\\",\\n      \\\"paraphrased\\\"\\n    ],\\n    \\\"n_tasks\\\": 10,\\n    \\\"n_demos_per_task\\\": 10,\\n    \\\"n_timesteps_per_demo\\\": 50,\\n    \\\"model\\\": \\\"tracevla-phi3v\\\",\\n    \\\"action_space\\\": \\\"normalized_bins\\\",\\n    \\\"seed\\\": 42,\\n    \\\"task_names\\\": [\\n      \\\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\\\",\\n      \\\"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\\\",\\n      \\\"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\\\",\\n      \\\"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\\\",\\n      \\\"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\\\",\\n      \\\"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\\\",\\n      \\\"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\\\",\\n      \\\"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\\\",\\n      \\\"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\\\",\\n      \\\"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\\\"\\n    ]\\n  },\\n  \\\"wrong\\\": {\\n    \\\"global_metrics\\\": {\\n      \\\"paired_mse\\\": {\\n        \\\"mean\\\": 0.079477,\\n        \\\"std\\\": 0.067782,\\n        \\\"cohens_d\\\": 1.1724\\n      },\\n      \\\"per_dim_shift\\\": {\\n        \\\"means\\\": [\\n          0.152259,\\n          0.187868,\\n          0.236215,\\n          0.206971,\\n          0.226334,\\n          0.209435,\\n          0.170693\\n        ],\\n        \\\"stds\\\": [\\n          0.166715,\\n          0.187695,\\n          0.218717,\\n          0.177879,\\n          0.188311,\\n         
…[truncated 7644 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-21T16:19:59.557300+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "head -30 /root/autodl-tmp/vla-ssd/scripts/tracvla_long_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "head -30 /root/autodl-tmp/vla-ssd/scripts/tracvla_long_full_pipeline.py"
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-21T16:19:59.557434+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls -la /root/autodl-tmp/vla-ssd/results/libero_long/trained/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls -la /root/autodl-tmp/vla-ssd/results/libero_long/trained/"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-21T16:19:59.557573+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nLIBERO-Long Full Analysis Pipeline for TracVLA-Phi3V\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer Ridge probe\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d\\n\\nRuns both trained (TracVLA-Phi3V) and untrained (base Phi-3-Vision) sequentially.\\nAll results -> RESULTS_DIR/{trained,untrained}/*.json\\nNo intermediate features saved to disk.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.linear_model import RidgeCV\\nfrom transformers import AutoModelForCausalLM, AutoProcessor\\n\\n# --- Checkpoints ---\\nTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/\\\"\\nUNTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/\\\"\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-21T16:19:59.557727+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/vla-ssd/results/libero_long/trained/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-21T16:19:59.557890+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/results/libero_long/ -type f -name \"*.json\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/results/libero_long/ -type f -name \"*.json\""
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-21T16:19:59.558047+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/vla-ssd/results/libero_long/action_r2_probing.json\\n/root/autodl-tmp/vla-ssd/results/libero_long/l1_attention_profile.json\\n/root/autodl-tmp/vla-ssd/results/libero_long/cross_instruction_classification.json\\n/root/autodl-tmp/vla-ssd/results/libero_long/rsa_analysis.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-21T16:19:59.558180+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/ -name \"*.log\" -newer /root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/ -name \"*.log\" -newer /root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-21T16:19:59.558308+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-21T16:19:59.558426+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/libero_long/action_r2_probing.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/libero_long/action_r2_probing.json"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-21T16:19:59.558693+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"L0_image_mean\\\": {\\n    \\\"mean\\\": 0.8762,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.8762\\n    ]\\n  },\\n  \\\"L0_last_preaction\\\": {\\n    \\\"mean\\\": 0.6539,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.6539\\n    ]\\n  },\\n  \\\"L1_image_mean\\\": {\\n    \\\"mean\\\": 0.8779,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.8779\\n    ]\\n  },\\n  \\\"L1_last_preaction\\\": {\\n    \\\"mean\\\": 0.7726,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.7726\\n    ]\\n  },\\n  \\\"L2_image_mean\\\": {\\n    \\\"mean\\\": 0.8805,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.8805\\n    ]\\n  },\\n  \\\"L2_last_preaction\\\": {\\n    \\\"mean\\\": 0.7898,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.7898\\n    ]\\n  },\\n  \\\"L3_image_mean\\\": {\\n    \\\"mean\\\": 0.8822,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.8822\\n    ]\\n  },\\n  \\\"L3_last_preaction\\\": {\\n    \\\"mean\\\": 0.817,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.817\\n    ]\\n  },\\n  \\\"L4_image_mean\\\": {\\n    \\\"mean\\\": 0.8832,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.8832\\n    ]\\n  },\\n  \\\"L4_last_preaction\\\": {\\n    \\\"mean\\\": 0.8369,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.8369\\n    ]\\n  },\\n  \\\"L5_image_mean\\\": {\\n    \\\"mean\\\": 0.8839,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.8839\\n    ]\\n  },\\n  \\\"L5_last_preaction\\\": {\\n    \\\"mean\\\": 0.8438,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.8438\\n    ]\\n  },\\n  \\\"L6_image_mean\\\": {\\n    \\\"mean\\\": 0.8841,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.8841\\n    ]\\n  },\\n  \\\"L6_last_preaction\\\": {\\n    \\\"mean\\\": 0.857,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.857\\n    ]\\n  },\\n  \\\"L7_image_mean\\\": {
…[truncated 6966 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-21T16:19:59.558854+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/libero_long/rsa_analysis.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/libero_long/rsa_analysis.json"
  }
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-21T16:19:59.559254+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "head -50 /root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "head -50 /root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-21T16:19:59.559655+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"method\\\": {\\n    \\\"pairing\\\": \\\"within-task\\\",\\n    \\\"rep_distance\\\": \\\"cosine\\\",\\n    \\\"act_distance\\\": \\\"euclidean\\\",\\n    \\\"n_sample\\\": 20,\\n    \\\"bootstrap_n\\\": 1000,\\n    \\\"seed\\\": 42,\\n    \\\"n_tasks\\\": 10,\\n    \\\"layers\\\": [\\n      0,\\n      4,\\n      8,\\n      12,\\n      16,\\n      20,\\n      24,\\n      28,\\n      31\\n    ]\\n  },\\n  \\\"per_layer\\\": {\\n    \\\"L0_image_mean\\\": {\\n      \\\"mean_rsa\\\": 0.519261,\\n      \\\"std\\\": 0.146152,\\n      \\\"ci_95\\\": [\\n        0.428582,\\n        0.609341\\n      ],\\n      \\\"per_task\\\": [\\n        0.59533,\\n        0.650666,\\n        0.381413,\\n        0.494977,\\n        0.577478,\\n        0.211929,\\n        0.776646,\\n        0.526206,\\n        0.439044,\\n        0.538924\\n      ],\\n      \\\"n_tasks\\\": 10\\n    },\\n    \\\"L0_last_preaction\\\": {\\n      \\\"mean_rsa\\\": 0.42861,\\n      \\\"std\\\": 0.134213,\\n      \\\"ci_95\\\": [\\n        0.348132,\\n        0.511807\\n      ],\\n      \\\"per_task\\\": [\\n        0.555489,\\n        0.670944,\\n        0.433498,\\n        0.36115,\\n        0.447906,\\n        0.284433,\\n        0.52498,\\n        0.345059,\\n        0.182368,\\n        0.480271\\n      ],\\n      \\\"n_tasks\\\": 10\\n    },\\n    \\\"L4_image_mean\\\": {\\n      \\\"mean_rsa\\\": 0.507422,\\n      \\\"std\\\": 0.103031,\\n      \\\"ci_95\\\": [\\n        0.442222,\\n        0.572744\\n      ],\\n      \\\"per_task\\\": [\\n        0.57655,\\n        0.57203,\\n        0.471975,\\n        0.348504,\\n        0.444316,\\n        0.600327,\\n        0.697471,\\n        0.359654,\\n        0.496385,\\n        0.507008\\n      ],\\n      \\\"n_tasks\\\": 10\\n    },\\n    \\\"L4_last_preaction\\\": {\\n      \\\"mean_rsa\\\": 0.522269,\\n      \\\"std\\\": 0.143728,\\n      \\\"ci_95\\\": [\\n        0.429641,\\n        0.6048
…[truncated 7140 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-21T16:19:59.559867+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nLIBERO-Long Full Analysis Pipeline (Streaming)\\n\\nPhases:\\n  1. Representation extraction: forward passes -> hidden states + L1 attention\\n  2. Action R2 probing: per-layer Ridge probe\\n  3. L1 attention profile: per-head instruction/image attention classification\\n  4. Cross-instruction classification: 10-way per-layer\\n  5. RSA: representational similarity across conditions\\n  6. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d\\n\\nAll results -> RESULTS_DIR/*.json\\nNo intermediate features saved to disk.\\n\\\"\\\"\\\"\\n\\nimport argparse, json, os, random, sys, time\\nfrom collections import defaultdict\\n\\nimport h5py\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\nfrom sklearn.linear_model import LogisticRegression\\nfrom sklearn.linear_model import RidgeCV\\nfrom transformers import AutoModelForVision2Seq, AutoProcessor\\n\\nTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-oft-finetuned-libero-10\\\"\\nUNTRAINED_CKPT = \\\"/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b\\\"\\nDATA = \\\"/root/autodl-tmp/vla-ssd/data/libero/libero_10\\\"\\nRESULTS_BASE = \\\"/root/autodl-tmp/vla-ssd/results/libero_long\\\"\\nDEVICE = \\\"cuda:0\\\"\\nUNNORM_TRAINED = \\\"libero_10_no_noops\\\"\\nUNNORM_UNTRAINED = \\\"bridge_orig\\\"\\nUNNORM = UNNORM_TRAINED\\n\\nTASKS = [\\n    \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\",\\n    \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\",\\n    \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\",\\n    \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\",\\n    \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\",\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\",\\n    \\\"LIVING_ROOM_S
…[truncated 597 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-21T16:19:59.560160+00:00_

全部数据已收集。汇总如下：

---

## 任务 1: openvla_long_pipeline_v1 诊断

**状态：部分完成，非完全失败**

- `/tmp/exp_openvla_long_pipeline_v1.log` 不存在，无日志可查
- `results/libero_long/` 下有 **4 个 JSON**（无 trained/untrained 子目录）：
  - `action_r2_probing.json` ✓
  - `l1_attention_profile.json` ✓
  - `cross_instruction_classification.json` ✓
  - `rsa_analysis.json` ✓
- **缺失**：`counterfactual_combined.json` — 第 6 阶段（counterfactual）未完成
- **关键问题**：脚本定义了 trained/untrained 两个 condition，但结果直接写入 `RESULTS_BASE/` 而非子目录。目前只有一组数据，推测**第一个 condition 的前 4/5 阶段完成后崩溃**，第二个 condition 未开始
- R2 probing 数值特征（image_mean ~0.87-0.88，very flat across layers）符合 **trained OpenVLA** 的模式

---

## 任务 2: tracvla_spatial_untrained_v1 结果

**状态：3/4 阶段完成，缺 counterfactual**

### R2 Probing (untrained)

| Layer | image_mean | last_preaction |
|-------|-----------|---------------|
| L0 | 0.7761 | 0.5911 |
| L4 | 0.7812 | 0.7132 |
| L8 | 0.7892 | 0.6942 |
| L12 | 0.7806 | 0.7195 |
| L16 | 0.7961 | 0.7207 |
| L20 | 0.7814 | 0.7139 |
| L24 | 0.7694 | 0.7116 |
| L28 | 0.7714 | 0.7036 |
| L31 | 0.7589 | 0.7065 |

Pattern: image R2 高且平（~0.76-0.80），last_preaction 从 L0 的 0.59 快速升至 L4 的 0.71 后也趋于平坦。

### L1 Attention (untrained)
- **32/32 heads instruction-dominant**（0 mixed, 0 image-dominant）
- Top 5: head_8 (0.996), head_26 (0.984), head_19 (0.983), head_1 (0.959), head_28 (0.955)
- 最低: head_2 (0.569), head_24 (0.602)

### Cross-instruction Classification (untrained)
- 所有层 image_mean = 1.0, last_preaction = 1.0（仅 L0_last_preaction = 0.977）
- 近乎完美的 10-way 分类 → 每层表征都能完美区分不同指令

### Counterfactual: **未完成**（文件不存在）

---

## 任务 3: tracvla_spatial_full_v2 (trained)

**PID 521837 已结束。结果完整 — 4/4 JSON 齐全。**

### R2 Probing (trained)

| Layer | image_mean | last_preaction |
|-------|-----------|---------------|
| L0 | 0.8059 | 0.6656 |
| L4 | 0.8091 | 0.7954 |
| L8 | 0.8134 | 0.7908 |
| L12 | 0.8231 | 0.7980 |
| L16 | 0.8311 | 0.8035 |
| L20 | 0.8310 | 0.7981 |
| L24 | 0.8169 | 0.7463 |
| L28 | 0.8223 | **0.6150** |
| L29 | 0.8136 | **0.5040** |
| L30 | 0.7970 | **0.4472** |
| L31 | 0.7907 | 0.6712 |

**关键发现**：trained 模型 last_preaction R2 在 L28-L30 急剧下降（0.80→0.45），L31 部分回升至 0.67。Image R2 保持高位。这个 "action token R2 collapse" 在 untrained 中不存在。

### L1 Attention (trained)
- 30/32 instruction-dominant, **2 mixed** (head_13: 0.450, head_22: 0.474), 0 image-dominant
- Training 使部分 heads 从 instruction-dominant 转向 mixed

### Cross-instruction Classification (trained)
- 所有层 ≥ L1: image_mean=1.0, last_preaction=1.0
- L0: image=1.0, last_preaction=0.923

### Counterfactual (trained) — **完整**

| Condition | Cohen's d | MSE |
|-----------|----------|-----|
| empty | 1.327 | 0.107 |
| shuffled | 1.295 | 0.094 |
| paraphrased | 1.183 | 0.072 |
| wrong | 1.172 | 0.080 |

所有条件 d>1（大效应量），wrong condition token_divergence_rate=1.0。

---

## 任务 4: 下一批脚本就绪状态

| 脚本 | 存在 | 大小 |
|------|------|------|
| tracvla_long_full_pipeline.py | ✓ | 24.7KB |
| tracvla_goal_full_pipeline.py | ✓ | 23.3KB |

tracvla_long 配置确认正确：TracVLA-Phi3V + Phi-3-Vision base，输出到 `{trained,untrained}/` 子目录，包含完整 5 阶段。

---

## 任务 5: GPU 状态

| GPU | Utilization | Memory |
|-----|------------|--------|
| 0 | 0% | 0 / 97887 MiB |
| 1 | 0% | 0 / 97887 MiB |

**两卡完全空闲，可立即启动下一批实验。**

---

## 行动建议摘要

1. **openvla_long**：部分完成（4/5 阶段 × 1 condition），且没有 trained/untrained 分目录。需检查脚本是否有 bug 导致两个 condition 写到同一目录互相覆盖，以及 counterfactual 阶段崩溃原因
2. **tracvla_spatial untrained**：缺 counterfactual。可单独补跑 counterfactual 阶段
3. **tracvla_spatial trained**：**完整可用**，数据质量好
4. GPU 空闲，可启动 tracvla_long 或 tracvla_goal

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_diag_urgent_gpu_recovery_20260521T1610_20260521T161754"
}
```

</details>

---
