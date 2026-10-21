# analysis collect probe results

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/chats/worker_analysis_collect_probe_results_20260519T074812.jsonl`
- **Structured JSON:** [`3277ce0ca2bcb1286bf9.json`](../../sessions/32/3277ce0ca2bcb1286bf9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

41 recorded events

### Tool call

_source line 1 · 2026-05-19T07:51:42.807558+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T07:51:42.808121+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T07:51:42.808391+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T07:51:42.808815+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"openvla-7b-finetuned-libero-goal\\\",\\n  \\\"method\\\": \\\"PCA256+LogReg, LOOCV (10-fold leave-one-task-out)\\\",\\n  \\\"token_position\\\": \\\"last_preaction\\\",\\n  \\\"per_layer_accuracy\\\": {\\n    \\\"L0\\\": 0.1,\\n    \\\"L1\\\": 0.997,\\n    \\\"L2\\\": 1.0,\\n    \\\"L3\\\": 1.0,\\n    \\\"L4\\\": 1.0,\\n    \\\"L5\\\": 1.0,\\n    \\\"L6\\\": 1.0,\\n    \\\"L7\\\": 1.0,\\n    \\\"L8\\\": 1.0,\\n    \\\"L9\\\": 1.0,\\n    \\\"L10\\\": 1.0,\\n    \\\"L11\\\": 1.0,\\n    \\\"L12\\\": 1.0,\\n    \\\"L13\\\": 1.0,\\n    \\\"L14\\\": 1.0,\\n    \\\"L15\\\": 1.0,\\n    \\\"L16\\\": 1.0,\\n    \\\"L17\\\": 1.0,\\n    \\\"L18\\\": 1.0,\\n    \\\"L19\\\": 1.0,\\n    \\\"L20\\\": 1.0,\\n    \\\"L21\\\": 1.0,\\n    \\\"L22\\\": 1.0,\\n    \\\"L23\\\": 1.0,\\n    \\\"L24\\\": 1.0,\\n    \\\"L25\\\": 1.0,\\n    \\\"L26\\\": 1.0,\\n    \\\"L27\\\": 1.0,\\n    \\\"L28\\\": 1.0,\\n    \\\"L29\\\": 1.0,\\n    \\\"L30\\\": 1.0,\\n    \\\"L31\\\": 1.0\\n  },\\n  \\\"loocv_results\\\": {\\n    \\\"L0\\\": {\\n      \\\"mean\\\": 0.1,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L1\\\": {\\n      \\\"mean\\\": 0.997,\\n      \\\"std\\\": 0.0033\\n    },\\n    \\\"L2\\\": {\\n      \\\"mean\\\": 1.0,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L3\\\": {\\n      \\\"mean\\\": 1.0,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L4\\\": {\\n      \\\"mean\\\": 1.0,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L5\\\": {\\n      \\\"mean\\\": 1.0,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L6\\\": {\\n      \\\"mean\\\": 1.0,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L7\\\": {\\n      \\\"mean\\\": 1.0,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L8\\\": {\\n      \\\"mean\\\": 1.0,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L9\\\": {\\n      \\\"mean\\\": 1.0,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L10\\\": {\\n      \\\"mean\\\": 1.0,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L11\\\": {\\n 
…[truncated 8656 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T07:51:42.809076+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "wc -c /root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "wc -c /root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T07:51:42.809248+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"19174 /root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T07:51:42.809395+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json')); print(json.dumps(d, indent=2))\" "
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json')); print(json.dumps(d, indent=2))\" "
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T07:51:42.809559+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T07:51:42.809690+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "head -n 200 /root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "head -n 200 /root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-19T07:51:42.809813+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "tail -n 400 /root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "tail -n 400 /root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-19T07:51:42.810062+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"openvla-7b-finetuned-libero-goal\\\",\\n  \\\"method\\\": \\\"PCA256+LogReg, LOOCV (10-fold leave-one-task-out)\\\",\\n  \\\"token_position\\\": \\\"last_preaction\\\",\\n  \\\"per_layer_accuracy\\\": {\\n    \\\"L0\\\": 0.1,\\n    \\\"L1\\\": 0.997,\\n    \\\"L2\\\": 1.0,\\n    \\\"L3\\\": 1.0,\\n    \\\"L4\\\": 1.0,\\n    \\\"L5\\\": 1.0,\\n    \\\"L6\\\": 1.0,\\n    \\\"L7\\\": 1.0,\\n    \\\"L8\\\": 1.0,\\n    \\\"L9\\\": 1.0,\\n    \\\"L10\\\": 1.0,\\n    \\\"L11\\\": 1.0,\\n    \\\"L12\\\": 1.0,\\n    \\\"L13\\\": 1.0,\\n    \\\"L14\\\": 1.0,\\n    \\\"L15\\\": 1.0,\\n    \\\"L16\\\": 1.0,\\n    \\\"L17\\\": 1.0,\\n    \\\"L18\\\": 1.0,\\n    \\\"L19\\\": 1.0,\\n    \\\"L20\\\": 1.0,\\n    \\\"L21\\\": 1.0,\\n    \\\"L22\\\": 1.0,\\n    \\\"L23\\\": 1.0,\\n    \\\"L24\\\": 1.0,\\n    \\\"L25\\\": 1.0,\\n    \\\"L26\\\": 1.0,\\n    \\\"L27\\\": 1.0,\\n    \\\"L28\\\": 1.0,\\n    \\\"L29\\\": 1.0,\\n    \\\"L30\\\": 1.0,\\n    \\\"L31\\\": 1.0\\n  },\\n  \\\"loocv_results\\\": {\\n    \\\"L0\\\": {\\n      \\\"mean\\\": 0.1,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L1\\\": {\\n      \\\"mean\\\": 0.997,\\n      \\\"std\\\": 0.0033\\n    },\\n    \\\"L2\\\": {\\n      \\\"mean\\\": 1.0,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L3\\\": {\\n      \\\"mean\\\": 1.0,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L4\\\": {\\n      \\\"mean\\\": 1.0,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L5\\\": {\\n      \\\"mean\\\": 1.0,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L6\\\": {\\n      \\\"mean\\\": 1.0,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L7\\\": {\\n      \\\"mean\\\": 1.0,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L8\\\": {\\n      \\\"mean\\\": 1.0,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L9\\\": {\\n      \\\"mean\\\": 1.0,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L10\\\": {\\n      \\\"mean\\\": 1.0,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L11\\\": {\\n 
…[truncated 2465 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T07:51:42.810358+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1\\n        ]\\n      },\\n      \\\"L10\\\": {\\n        \\\"mean\\\": 0.1,\\n        \\\"std\\\": 0.0,\\n        \\\"per_fold\\\": [\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1\\n        ]\\n      },\\n      \\\"L11\\\": {\\n        \\\"mean\\\": 0.1,\\n        \\\"std\\\": 0.0,\\n        \\\"per_fold\\\": [\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1\\n        ]\\n      },\\n      \\\"L12\\\": {\\n        \\\"mean\\\": 0.1,\\n        \\\"std\\\": 0.0,\\n        \\\"per_fold\\\": [\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1\\n        ]\\n      },\\n      \\\"L13\\\": {\\n        \\\"mean\\\": 0.1,\\n        \\\"std\\\": 0.0,\\n        \\\"per_fold\\\": [\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1\\n        ]\\n      },\\n      \\\"L14\\\": {\\n        \\\"mean\\\": 0.1,\\n        \\\"std\\\": 0.0,\\n        \\\"per_fold\\\": [\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1\\n        ]\\n      },\\n      \\\"L15\\\": {\\n        \\\"mean\\\": 0.1,\\n        \\\"std\\\": 0.0,\\n        \\\"per_fold\\\": [\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1,\\n          0.1
…[truncated 6097 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T07:51:42.810546+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"action_token\\|first_token\\|last_token\\|middle\\|full_results\" /root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "grep -n \"action_token\\|first_token\\|last_token\\|middle\\|full_results\" /root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T07:51:42.810686+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T07:51:42.810813+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"action_token\" /root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "grep -n \"action_token\" /root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T07:51:42.810965+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T07:51:42.811108+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"full_results\" /root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "grep -n \"full_results\" /root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T07:51:42.811236+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"169:  \\\"full_results\\\": {\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T07:51:42.811356+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"first_action\" /root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "grep -n \"first_action\" /root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T07:51:42.811478+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T07:51:42.811594+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -nc \"\\\"L0\\\"\" /root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "grep -nc \"\\\"L0\\\"\" /root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T07:51:42.811715+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"5\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T07:51:42.811844+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "head -n 520 /root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "head -n 520 /root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T07:51:42.812174+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"openvla-7b-finetuned-libero-goal\\\",\\n  \\\"method\\\": \\\"PCA256+LogReg, LOOCV (10-fold leave-one-task-out)\\\",\\n  \\\"token_position\\\": \\\"last_preaction\\\",\\n  \\\"per_layer_accuracy\\\": {\\n    \\\"L0\\\": 0.1,\\n    \\\"L1\\\": 0.997,\\n    \\\"L2\\\": 1.0,\\n    \\\"L3\\\": 1.0,\\n    \\\"L4\\\": 1.0,\\n    \\\"L5\\\": 1.0,\\n    \\\"L6\\\": 1.0,\\n    \\\"L7\\\": 1.0,\\n    \\\"L8\\\": 1.0,\\n    \\\"L9\\\": 1.0,\\n    \\\"L10\\\": 1.0,\\n    \\\"L11\\\": 1.0,\\n    \\\"L12\\\": 1.0,\\n    \\\"L13\\\": 1.0,\\n    \\\"L14\\\": 1.0,\\n    \\\"L15\\\": 1.0,\\n    \\\"L16\\\": 1.0,\\n    \\\"L17\\\": 1.0,\\n    \\\"L18\\\": 1.0,\\n    \\\"L19\\\": 1.0,\\n    \\\"L20\\\": 1.0,\\n    \\\"L21\\\": 1.0,\\n    \\\"L22\\\": 1.0,\\n    \\\"L23\\\": 1.0,\\n    \\\"L24\\\": 1.0,\\n    \\\"L25\\\": 1.0,\\n    \\\"L26\\\": 1.0,\\n    \\\"L27\\\": 1.0,\\n    \\\"L28\\\": 1.0,\\n    \\\"L29\\\": 1.0,\\n    \\\"L30\\\": 1.0,\\n    \\\"L31\\\": 1.0\\n  },\\n  \\\"loocv_results\\\": {\\n    \\\"L0\\\": {\\n      \\\"mean\\\": 0.1,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L1\\\": {\\n      \\\"mean\\\": 0.997,\\n      \\\"std\\\": 0.0033\\n    },\\n    \\\"L2\\\": {\\n      \\\"mean\\\": 1.0,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L3\\\": {\\n      \\\"mean\\\": 1.0,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L4\\\": {\\n      \\\"mean\\\": 1.0,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L5\\\": {\\n      \\\"mean\\\": 1.0,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L6\\\": {\\n      \\\"mean\\\": 1.0,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L7\\\": {\\n      \\\"mean\\\": 1.0,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L8\\\": {\\n      \\\"mean\\\": 1.0,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L9\\\": {\\n      \\\"mean\\\": 1.0,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L10\\\": {\\n      \\\"mean\\\": 1.0,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L11\\\": {\\n 
…[truncated 8497 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T07:51:42.812362+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "head -n 560 /root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "head -n 560 /root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T07:51:42.812712+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"openvla-7b-finetuned-libero-goal\\\",\\n  \\\"method\\\": \\\"PCA256+LogReg, LOOCV (10-fold leave-one-task-out)\\\",\\n  \\\"token_position\\\": \\\"last_preaction\\\",\\n  \\\"per_layer_accuracy\\\": {\\n    \\\"L0\\\": 0.1,\\n    \\\"L1\\\": 0.997,\\n    \\\"L2\\\": 1.0,\\n    \\\"L3\\\": 1.0,\\n    \\\"L4\\\": 1.0,\\n    \\\"L5\\\": 1.0,\\n    \\\"L6\\\": 1.0,\\n    \\\"L7\\\": 1.0,\\n    \\\"L8\\\": 1.0,\\n    \\\"L9\\\": 1.0,\\n    \\\"L10\\\": 1.0,\\n    \\\"L11\\\": 1.0,\\n    \\\"L12\\\": 1.0,\\n    \\\"L13\\\": 1.0,\\n    \\\"L14\\\": 1.0,\\n    \\\"L15\\\": 1.0,\\n    \\\"L16\\\": 1.0,\\n    \\\"L17\\\": 1.0,\\n    \\\"L18\\\": 1.0,\\n    \\\"L19\\\": 1.0,\\n    \\\"L20\\\": 1.0,\\n    \\\"L21\\\": 1.0,\\n    \\\"L22\\\": 1.0,\\n    \\\"L23\\\": 1.0,\\n    \\\"L24\\\": 1.0,\\n    \\\"L25\\\": 1.0,\\n    \\\"L26\\\": 1.0,\\n    \\\"L27\\\": 1.0,\\n    \\\"L28\\\": 1.0,\\n    \\\"L29\\\": 1.0,\\n    \\\"L30\\\": 1.0,\\n    \\\"L31\\\": 1.0\\n  },\\n  \\\"loocv_results\\\": {\\n    \\\"L0\\\": {\\n      \\\"mean\\\": 0.1,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L1\\\": {\\n      \\\"mean\\\": 0.997,\\n      \\\"std\\\": 0.0033\\n    },\\n    \\\"L2\\\": {\\n      \\\"mean\\\": 1.0,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L3\\\": {\\n      \\\"mean\\\": 1.0,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L4\\\": {\\n      \\\"mean\\\": 1.0,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L5\\\": {\\n      \\\"mean\\\": 1.0,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L6\\\": {\\n      \\\"mean\\\": 1.0,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L7\\\": {\\n      \\\"mean\\\": 1.0,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L8\\\": {\\n      \\\"mean\\\": 1.0,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L9\\\": {\\n      \\\"mean\\\": 1.0,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L10\\\": {\\n      \\\"mean\\\": 1.0,\\n      \\\"std\\\": 0.0\\n    },\\n    \\\"L11\\\": {\\n 
…[truncated 8614 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T07:51:42.812896+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"preaction\\|first_action\\|last_action\\|comparison\" /root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "grep -n \"preaction\\|first_action\\|last_action\\|comparison\" /root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T07:51:42.813056+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T07:51:42.813182+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"first_action_token\" /root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "grep -n \"first_action_token\" /root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T07:51:42.813307+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-19T07:51:42.813448+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "wc -l /root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "wc -l /root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T07:51:42.813591+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"1232 /root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-19T07:51:42.813713+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"action\" /root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "grep -n \"action\" /root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T07:51:42.813839+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"4:  \\\"token_position\\\": \\\"last_preaction\\\",\\n170:    \\\"last_preaction\\\": {\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-19T07:51:42.813988+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"mean\" /root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "grep -n \"mean\" /root/autodl-tmp/vla-ssd/results/libero_finetuned_probe_profile.json"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T07:51:42.814168+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"41:      \\\"mean\\\": 0.1,\\n45:      \\\"mean\\\": 0.997,\\n49:      \\\"mean\\\": 1.0,\\n53:      \\\"mean\\\": 1.0,\\n57:      \\\"mean\\\": 1.0,\\n61:      \\\"mean\\\": 1.0,\\n65:      \\\"mean\\\": 1.0,\\n69:      \\\"mean\\\": 1.0,\\n73:      \\\"mean\\\": 1.0,\\n77:      \\\"mean\\\": 1.0,\\n81:      \\\"mean\\\": 1.0,\\n85:      \\\"mean\\\": 1.0,\\n89:      \\\"mean\\\": 1.0,\\n93:      \\\"mean\\\": 1.0,\\n97:      \\\"mean\\\": 1.0,\\n101:      \\\"mean\\\": 1.0,\\n105:      \\\"mean\\\": 1.0,\\n109:      \\\"mean\\\": 1.0,\\n113:      \\\"mean\\\": 1.0,\\n117:      \\\"mean\\\": 1.0,\\n121:      \\\"mean\\\": 1.0,\\n125:      \\\"mean\\\": 1.0,\\n129:      \\\"mean\\\": 1.0,\\n133:      \\\"mean\\\": 1.0,\\n137:      \\\"mean\\\": 1.0,\\n141:      \\\"mean\\\": 1.0,\\n145:      \\\"mean\\\": 1.0,\\n149:      \\\"mean\\\": 1.0,\\n153:      \\\"mean\\\": 1.0,\\n157:      \\\"mean\\\": 1.0,\\n161:      \\\"mean\\\": 1.0,\\n165:      \\\"mean\\\": 1.0,\\n172:        \\\"mean\\\": 0.1,\\n188:        \\\"mean\\\": 0.997,\\n204:        \\\"mean\\\": 1.0,\\n220:        \\\"mean\\\": 1.0,\\n236:        \\\"mean\\\": 1.0,\\n252:        \\\"mean\\\": 1.0,\\n268:        \\\"mean\\\": 1.0,\\n284:        \\\"mean\\\": 1.0,\\n300:        \\\"mean\\\": 1.0,\\n316:        \\\"mean\\\": 1.0,\\n332:        \\\"mean\\\": 1.0,\\n348:        \\\"mean\\\": 1.0,\\n364:        \\\"mean\\\": 1.0,\\n380:        \\\"mean\\\": 1.0,\\n396:        \\\"mean\\\": 1.0,\\n412:        \\\"mean\\\": 1.0,\\n428:        \\\"mean\\\": 1.0,\\n444:        \\\"mean\\\": 1.0,\\n460:        \\\"mean\\\": 1.0,\\n476:        \\\"mean\\\": 1.0,\\n492:        \\\"mean\\\": 1.0,\\n508:        \\\"mean\\\": 1.0,\\n524:        \\\"mean\\\": 1.0,\\n540:        \\\"mean\\\": 1.0,\\n556:        \\\"mean\\\": 1.0,\\n572:        \\\"mean\\\": 1.0,\\n588:        \\\"mean\\\": 1.0,\\n604:        \\\"mean\\\": 1.0,\\n620:        \\\"mean\\\": 1.0,\\n636:  
…[truncated 1306 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-19T07:51:42.814348+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T07:51:42.814486+00:00_

_project
ablation_narrative_playbook.md
action_metrics_extended
action_probe_design.md
analyze_ablation_50demos.py
attention
attention_decomposition
attention_decomposition_and_r2.py
attention_normalization_entropy
attention_normalization_entropy.py
behavioral_pilot_w4_diagnosis.md
branch_split_rsa_results.md
citation_verification_2026.md
controlb_analysis
counterfactual_instruction.py
counterfactual_token_overlap
cross_inst_extract_phase2
cross_instruction
definitive_rsa_results.md
demo_sensitivity.py
demo_standardized_rsa.md
dinov2_baseline
dream_reports
extract_fused_backbone.py
fig2_cross_instruction_heatmap.pdf
fig_ood_diagnostics.png
fig_rsa_perlayer_curve.pdf
fig_rsa_perlayer_curve.png
figures
fulllayer_action_probe.py
groundtruth_action_error
l1_ablation_action_probe_50demos.py
layer_stability_analysis.md
libero_finetuned_attention
libero_goal_feasibility.md
literature_map.yaml
literature_map_probing.md
literature_survey_instruction_probing.md
llama2base_action_probe.py
manifest.yaml
matched_ablation_controls.py
matched_ablation_controls_diagnosis.md
mvp_controlb_trained
mvp_probe_trained
openvla_libero_goal_compat.md
paper_consistency_report.md
patch_probes.py
pca_linear_probe_gc.py
pca_linear_probe_perlayer.py
permutation_test_I2.py
pipeline_audit_libero_goal.md
plan_010_libero_spatial
plan_011_fulllayer_r2
plan_012_clip_vit_control
plot_dose_response.py
probe_design_plan.md
qa_probe_classification.py
random_subset_ablation.py
redream_evidence_v2.md
review_issues.yaml
review_reports
rsa_analysis.py
rsa_branch_split.py
rsa_definitive.py
rsa_method_audit_report.md
rsa_unified_vla.py
task_complexity_routing
task_routing_loo_sensitivity
unified_action_probe.py
unified_rsa_summary.md
untrained_last_preaction_probe.json
vla-ssd_round12_2026-05-19.pdf
vla_rsa_method_audit.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-19T07:51:42.814660+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/libero_finetuned_probe_profile.json",
  "content": "{\n  \"model\": \"openvla-7b-finetuned-libero-goal\",\n  \"method\": \"PCA256+LogReg, LOOCV (10-fold leave-one-task-out)\",\n  \"token_position\": \"last_preaction\",\n  \"per_layer_accuracy\": {\n    \"L0\": 0.1,\n    \"L1\": 0.997,\n    \"L2\": 1.0,\n    \"L3\": 1.0,\n    \"L4\": 1.0,\n    \"L5\": 1.0,\n    \"L6\": 1.0,\n    \"L7\": 1.0,\n    \"L8\": 1.0,\n    \"L9\": 1.0,\n    \"L10\": 1.0,\n    \"L11\": 1.0,\n    \"L12\": 1.0,\n    \"L13\": 1.0,\n    \"L14\": 1.0,\n    \"L15\": 1.0,\n    \"L16\": 1.0,\n    \"L17\": 1.0,\n    \"L18\": 1.0,\n    \"L19\": 1.0,\n    \"L20\": 1.0,\n    \"L21\": 1.0,\n    \"L22\": 1.0,\n    \"L23\": 1.0,\n    \"L24\": 1.0,\n    \"L25\": 1.0,\n    \"L26\": 1.0,\n    \"L27\": 1.0,\n    \"L28\": 1.0,\n    \"L29\": 1.0,\n    \"L30\": 1.0,\n    \"L31\": 1.0\n  },\n  \"loocv_results\": {\n    \"L0\": {\"mean\": 0.1, \"std\": 0.0},\n    \"L1\": {\"mean\": 0.997, \"std\": 0.0033},\n    \"L2\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L3\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L4\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L5\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L6\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L7\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L8\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L9\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L10\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L11\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L12\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L13\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L14\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L15\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L16\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L17\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L18\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L19\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L20\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L21\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L22\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L23\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L24\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L25\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L26\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L27\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L28\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L29\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L30\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L31\": {\"mean\": 1.0, \"std\": 0.0}\n  },\n  \"full_results\": {\n    \"last_preaction\": {\n      \"L0\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L1\": {\"mean\": 0.997, \"std\": 0.0033, \"per_fold\": [0.994, 0.994, 0.996, 1.0, 1.0, 0.99, 0.998, 0.998, 1.0, 1.0]},\n      \"L2\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L3\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L4\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L5\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L6\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L7\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L8\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L9\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L10\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L11\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L12\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L13\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L14\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L15\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L16\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L17\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L18\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L19\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L20\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L21\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L22\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L23\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L24\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L25\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L26\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L27\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L28\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L29\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L30\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L31\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]}\n    },\n    \"image_mean\": {\n      \"L0\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L1\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L2\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L3\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L4\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L5\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L6\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L7\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L8\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L9\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L10\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L11\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L12\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L13\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L14\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L15\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L16\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L17\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L18\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L19\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L20\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L21\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L22\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L23\": {\"mean\": 0.0998, \"std\": 0.0006, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.098, 0.1, 0.1]},\n      \"L24\": {\"mean\": 0.0998, \"std\": 0.0006, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.098, 0.1, 0.1]},\n      \"L25\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L26\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L27\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L28\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L29\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L30\": {\"mean\": 0.0998, \"std\": 0.0006, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.098, 0.1, 0.1, 0.1]},\n      \"L31\": {\"mean\": 0.1, \"std\": 0.0015, \"per_fold\": [0.1, 0.098, 0.1, 0.1, 0.098, 0.104, 0.1, 0.1, 0.1, 0.1]}\n    }\n  },\n  \"comparison_4conditions\": {\n    \"L0\": {\"untrained\": 0.1, \"llama2base\": 0.1, \"openvla7b\": 0.1, \"libero_finetuned\": 0.1},\n    \"L1\": {\"untrained\": 1.0, \"llama2base\": 0.802, \"openvla7b\": 0.996, \"libero_finetuned\": 0.997},\n    \"L8\": {\"untrained\": 0.986, \"llama2base\": 0.999, \"openvla7b\": 1.0, \"libero_finetuned\": 1.0},\n    \"L31\": {\"untrained\": 0.82, \"llama2base\": 1.0, \"openvla7b\": 1.0, \"libero_finetuned\": 1.0}\n  },\n  \"metadata\": {\n    \"n_folds\": 10,\n    \"samples_per_task\": 500,\n    \"pca_components\": 256,\n    \"classifier\": \"LogisticRegression(max_iter=2000, C=1.0)\",\n    \"seed\": 42,\n    \"features_path\": \"/root/autodl-tmp/vla-ssd/results/cross_instruction_finetuned/finetuned_cross_inst_L0-L31.h5\"\n  }\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/libero_finetuned_probe_profile.json",
    "content": "{\n  \"model\": \"openvla-7b-finetuned-libero-goal\",\n  \"method\": \"PCA256+LogReg, LOOCV (10-fold leave-one-task-out)\",\n  \"token_position\": \"last_preaction\",\n  \"per_layer_accuracy\": {\n    \"L0\": 0.1,\n    \"L1\": 0.997,\n    \"L2\": 1.0,\n    \"L3\": 1.0,\n    \"L4\": 1.0,\n    \"L5\": 1.0,\n    \"L6\": 1.0,\n    \"L7\": 1.0,\n    \"L8\": 1.0,\n    \"L9\": 1.0,\n    \"L10\": 1.0,\n    \"L11\": 1.0,\n    \"L12\": 1.0,\n    \"L13\": 1.0,\n    \"L14\": 1.0,\n    \"L15\": 1.0,\n    \"L16\": 1.0,\n    \"L17\": 1.0,\n    \"L18\": 1.0,\n    \"L19\": 1.0,\n    \"L20\": 1.0,\n    \"L21\": 1.0,\n    \"L22\": 1.0,\n    \"L23\": 1.0,\n    \"L24\": 1.0,\n    \"L25\": 1.0,\n    \"L26\": 1.0,\n    \"L27\": 1.0,\n    \"L28\": 1.0,\n    \"L29\": 1.0,\n    \"L30\": 1.0,\n    \"L31\": 1.0\n  },\n  \"loocv_results\": {\n    \"L0\": {\"mean\": 0.1, \"std\": 0.0},\n    \"L1\": {\"mean\": 0.997, \"std\": 0.0033},\n    \"L2\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L3\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L4\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L5\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L6\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L7\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L8\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L9\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L10\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L11\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L12\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L13\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L14\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L15\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L16\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L17\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L18\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L19\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L20\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L21\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L22\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L23\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L24\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L25\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L26\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L27\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L28\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L29\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L30\": {\"mean\": 1.0, \"std\": 0.0},\n    \"L31\": {\"mean\": 1.0, \"std\": 0.0}\n  },\n  \"full_results\": {\n    \"last_preaction\": {\n      \"L0\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L1\": {\"mean\": 0.997, \"std\": 0.0033, \"per_fold\": [0.994, 0.994, 0.996, 1.0, 1.0, 0.99, 0.998, 0.998, 1.0, 1.0]},\n      \"L2\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L3\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L4\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L5\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L6\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L7\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L8\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L9\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L10\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L11\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L12\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L13\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L14\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L15\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L16\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L17\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L18\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L19\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L20\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L21\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L22\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L23\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L24\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L25\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L26\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L27\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L28\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L29\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L30\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},\n      \"L31\": {\"mean\": 1.0, \"std\": 0.0, \"per_fold\": [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]}\n    },\n    \"image_mean\": {\n      \"L0\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L1\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L2\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L3\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L4\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L5\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L6\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L7\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L8\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L9\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L10\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L11\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L12\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L13\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L14\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L15\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L16\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L17\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L18\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L19\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L20\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L21\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L22\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L23\": {\"mean\": 0.0998, \"std\": 0.0006, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.098, 0.1, 0.1]},\n      \"L24\": {\"mean\": 0.0998, \"std\": 0.0006, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.098, 0.1, 0.1]},\n      \"L25\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L26\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L27\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L28\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L29\": {\"mean\": 0.1, \"std\": 0.0, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},\n      \"L30\": {\"mean\": 0.0998, \"std\": 0.0006, \"per_fold\": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.098, 0.1, 0.1, 0.1]},\n      \"L31\": {\"mean\": 0.1, \"std\": 0.0015, \"per_fold\": [0.1, 0.098, 0.1, 0.1, 0.098, 0.104, 0.1, 0.1, 0.1, 0.1]}\n    }\n  },\n  \"comparison_4conditions\": {\n    \"L0\": {\"untrained\": 0.1, \"llama2base\": 0.1, \"openvla7b\": 0.1, \"libero_finetuned\": 0.1},\n    \"L1\": {\"untrained\": 1.0, \"llama2base\": 0.802, \"openvla7b\": 0.996, \"libero_finetuned\": 0.997},\n    \"L8\": {\"untrained\": 0.986, \"llama2base\": 0.999, \"openvla7b\": 1.0, \"libero_finetuned\": 1.0},\n    \"L31\": {\"untrained\": 0.82, \"llama2base\": 1.0, \"openvla7b\": 1.0, \"libero_finetuned\": 1.0}\n  },\n  \"metadata\": {\n    \"n_folds\": 10,\n    \"samples_per_task\": 500,\n    \"pca_components\": 256,\n    \"classifier\": \"LogisticRegression(max_iter=2000, C=1.0)\",\n    \"seed\": 42,\n    \"features_path\": \"/root/autodl-tmp/vla-ssd/results/cross_instruction_finetuned/finetuned_cross_inst_L0-L31.h5\"\n  }\n}\n"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T07:51:42.814907+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/libero_finetuned_probe_profile.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_collect_probe_results_20260519T074812",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-19T07:51:42.815108+00:00_

结果已保存到本地 `artifacts/libero_finetuned_probe_profile.json`。

## 关键数据摘要

**模型**: openvla-7b-finetuned-libero-goal | **方法**: PCA256 + LogReg, 10-fold LOOCV

### Cross-instruction probe (last_preaction token)

| Layer | Accuracy | Std |
|-------|----------|-----|
| L0 | 0.100 | 0.000 |
| L1 | 0.997 | 0.003 |
| L2-L31 | **1.000** | 0.000 |

Fine-tuning 后 L1 起即近乎完美分类，L2+ 全部 100%，零方差。

### image_mean token (控制)

所有层 ~0.1 (chance, 10 tasks)。图像 token 均值不携带 instruction-discriminative 信息。

### 四条件对比 (last_preaction)

| Layer | Untrained | Llama2-base | OpenVLA-7B | LIBERO-finetuned |
|-------|-----------|-------------|------------|------------------|
| L0 | 0.100 | 0.100 | 0.100 | 0.100 |
| L1 | **1.000** | 0.802 | 0.996 | 0.997 |
| L8 | 0.986 | 0.999 | 1.000 | 1.000 |
| L31 | **0.820** | 1.000 | 1.000 | 1.000 |

关键发现：fine-tuned 模型的 cross-instruction probe profile 与 OpenVLA-7B pretrained 几乎完全一致（L1+ 均饱和于 1.0），task-specific fine-tuning 没有显著改变 instruction 的线性可分性 pattern。Untrained 模型 L31 只有 0.82 仍然是最显著的差异点。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_collect_probe_results_20260519T074812"
}
```

</details>

---
