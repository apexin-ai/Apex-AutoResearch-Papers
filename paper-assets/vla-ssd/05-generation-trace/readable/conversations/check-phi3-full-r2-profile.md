# check phi3 full r2 profile

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_check_phi3_full_r2_profile_20260523T235913.jsonl`
- **Structured JSON:** [`016159329b625d6a2cbc.json`](../../sessions/01/016159329b625d6a2cbc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-24T00:00:16.005991+00:00_

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
  "session": "worker_check_phi3_full_r2_profile_20260523T235913",
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

_source line 2 · 2026-05-24T00:00:16.006474+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_phi3_full_r2_profile_20260523T235913",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-24T00:00:16.006802+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/phi3_nlp_control/summary.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_phi3_full_r2_profile_20260523T235913",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/phi3_nlp_control/summary.json"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-24T00:00:16.007058+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls -la /root/autodl-tmp/vla-ssd/results/phi3_nlp_control/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_phi3_full_r2_profile_20260523T235913",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls -la /root/autodl-tmp/vla-ssd/results/phi3_nlp_control/"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-24T00:00:16.007258+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"Phi-3-mini-4k-instruct\\\",\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/models/Phi-3-mini-4k-instruct\\\",\\n  \\\"readout\\\": \\\"last_token\\\",\\n  \\\"n_layers\\\": 32,\\n  \\\"hidden_dim\\\": 3072,\\n  \\\"n_samples\\\": 5000,\\n  \\\"n_unique_hidden_states\\\": 10,\\n  \\\"note\\\": \\\"text-only NLP control: hidden states constant per task, actions vary across timesteps\\\",\\n  \\\"per_layer_r2\\\": {\\n    \\\"L0\\\": 0.1555,\\n    \\\"L1\\\": 0.1552,\\n    \\\"L2\\\": 0.1555,\\n    \\\"L3\\\": 0.1553,\\n    \\\"L4\\\": 0.1554,\\n    \\\"L5\\\": 0.1555,\\n    \\\"L6\\\": 0.1554,\\n    \\\"L7\\\": 0.1554,\\n    \\\"L8\\\": 0.1555,\\n    \\\"L9\\\": 0.1555,\\n    \\\"L10\\\": 0.1552,\\n    \\\"L11\\\": 0.1552,\\n    \\\"L12\\\": 0.1554,\\n    \\\"L13\\\": 0.1555,\\n    \\\"L14\\\": 0.1555,\\n    \\\"L15\\\": 0.1555,\\n    \\\"L16\\\": 0.1555,\\n    \\\"L17\\\": 0.1555,\\n    \\\"L18\\\": 0.1555,\\n    \\\"L19\\\": 0.1555,\\n    \\\"L20\\\": 0.1555,\\n    \\\"L21\\\": 0.1555,\\n    \\\"L22\\\": 0.1555,\\n    \\\"L23\\\": 0.1555,\\n    \\\"L24\\\": 0.1555,\\n    \\\"L25\\\": 0.1555,\\n    \\\"L26\\\": 0.1555,\\n    \\\"L27\\\": 0.1555,\\n    \\\"L28\\\": 0.1555,\\n    \\\"L29\\\": 0.1555,\\n    \\\"L30\\\": 0.1555,\\n    \\\"L31\\\": 0.1555\\n  },\\n  \\\"peak_layer\\\": 0,\\n  \\\"peak_r2\\\": 0.1555,\\n  \\\"exit_r2\\\": 0.1555,\\n  \\\"exit_collapse\\\": 0.0,\\n  \\\"mean_r2\\\": 0.1555\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.07}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_phi3_full_r2_profile_20260523T235913",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-24T00:00:16.007409+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls /root/autodl-tmp/vla-ssd/results/nlp_control/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_phi3_full_r2_profile_20260523T235913",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls /root/autodl-tmp/vla-ssd/results/nlp_control/"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-24T00:00:16.007610+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 24\\ndrwxr-xr-x  2 root root   87 May 24 07:56 .\\ndrwxr-xr-x 66 root root 8192 May 24 07:29 ..\\n-rw-r--r--  1 root root 3128 May 24 07:56 action_r2_probing.json\\n-rw-r--r--  1 root root 2484 May 24 07:56 run.log\\n-rw-r--r--  1 root root 1052 May 24 07:56 summary.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_phi3_full_r2_profile_20260523T235913",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-24T00:00:16.007773+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/vla-ssd/results/nlp_control/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_phi3_full_r2_profile_20260523T235913",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-24T00:00:16.007943+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/results/ -maxdepth 1 -type d -name \"*llama*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_phi3_full_r2_profile_20260523T235913",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/results/ -maxdepth 1 -type d -name \"*llama*\""
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-24T00:00:16.008104+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/vla-ssd/results/llama2base_action_probe\\n/root/autodl-tmp/vla-ssd/results/llama2chat_action_probe\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_phi3_full_r2_profile_20260523T235913",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-24T00:00:16.008232+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/results/ -maxdepth 1 -type d -name \"*nlp*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_phi3_full_r2_profile_20260523T235913",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/results/ -maxdepth 1 -type d -name \"*nlp*\""
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-24T00:00:16.008358+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/vla-ssd/results/phi3_nlp_control\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_phi3_full_r2_profile_20260523T235913",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-24T00:00:16.008498+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls -la /root/autodl-tmp/vla-ssd/results/llama2chat_action_probe/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_phi3_full_r2_profile_20260523T235913",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls -la /root/autodl-tmp/vla-ssd/results/llama2chat_action_probe/"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-24T00:00:16.008629+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 28\\ndrwxr-xr-x  2 root root   87 May 22 20:48 .\\ndrwxr-xr-x 66 root root 8192 May 24 07:29 ..\\n-rw-r--r--  1 root root 3128 May 22 20:48 action_r2_probing.json\\n-rw-r--r--  1 root root 4401 May 22 20:48 run.log\\n-rw-r--r--  1 root root  999 May 22 20:48 summary.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_phi3_full_r2_profile_20260523T235913",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-24T00:00:16.008752+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/phi3_nlp_control/action_r2_probing.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_phi3_full_r2_profile_20260523T235913",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/phi3_nlp_control/action_r2_probing.json"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-24T00:00:16.009091+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"L0_last_token\\\": {\\n    \\\"mean\\\": 0.1555,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.1555\\n    ]\\n  },\\n  \\\"L1_last_token\\\": {\\n    \\\"mean\\\": 0.1552,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.1552\\n    ]\\n  },\\n  \\\"L2_last_token\\\": {\\n    \\\"mean\\\": 0.1555,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.1555\\n    ]\\n  },\\n  \\\"L3_last_token\\\": {\\n    \\\"mean\\\": 0.1553,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.1553\\n    ]\\n  },\\n  \\\"L4_last_token\\\": {\\n    \\\"mean\\\": 0.1554,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.1554\\n    ]\\n  },\\n  \\\"L5_last_token\\\": {\\n    \\\"mean\\\": 0.1555,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.1555\\n    ]\\n  },\\n  \\\"L6_last_token\\\": {\\n    \\\"mean\\\": 0.1554,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.1554\\n    ]\\n  },\\n  \\\"L7_last_token\\\": {\\n    \\\"mean\\\": 0.1554,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.1554\\n    ]\\n  },\\n  \\\"L8_last_token\\\": {\\n    \\\"mean\\\": 0.1555,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.1555\\n    ]\\n  },\\n  \\\"L9_last_token\\\": {\\n    \\\"mean\\\": 0.1555,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.1555\\n    ]\\n  },\\n  \\\"L10_last_token\\\": {\\n    \\\"mean\\\": 0.1552,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.1552\\n    ]\\n  },\\n  \\\"L11_last_token\\\": {\\n    \\\"mean\\\": 0.1552,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.1552\\n    ]\\n  },\\n  \\\"L12_last_token\\\": {\\n    \\\"mean\\\": 0.1554,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.1554\\n    ]\\n  },\\n  \\\"L13_last_token\\\": {\\n    \\\"mean\\\": 0.1555,\\n    \\\"std\\\": 0.0,\\n    \\\"values\\\": [\\n      0.1555\\n    ]\\n  },\\n  \\\"L14_last_token\\\": {\\n    \\\"mean\\\"
…[truncated 2506 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_phi3_full_r2_profile_20260523T235913",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-24T00:00:16.009368+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/llama2chat_action_probe/summary.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_phi3_full_r2_profile_20260523T235913",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/llama2chat_action_probe/summary.json"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-24T00:00:16.009638+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"Llama-2-7b-chat-hf\\\",\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/models/Llama-2-7b-chat-hf\\\",\\n  \\\"readout\\\": \\\"last_token\\\",\\n  \\\"n_samples\\\": 5000,\\n  \\\"n_unique_hidden_states\\\": 10,\\n  \\\"note\\\": \\\"text-only model: hidden states constant per task, actions vary across timesteps\\\",\\n  \\\"per_layer_r2\\\": {\\n    \\\"L0\\\": 0.1553,\\n    \\\"L1\\\": 0.1554,\\n    \\\"L2\\\": 0.1551,\\n    \\\"L3\\\": 0.1554,\\n    \\\"L4\\\": 0.1552,\\n    \\\"L5\\\": 0.1554,\\n    \\\"L6\\\": 0.1547,\\n    \\\"L7\\\": 0.1551,\\n    \\\"L8\\\": 0.1552,\\n    \\\"L9\\\": 0.1553,\\n    \\\"L10\\\": 0.1553,\\n    \\\"L11\\\": 0.1553,\\n    \\\"L12\\\": 0.1554,\\n    \\\"L13\\\": 0.1554,\\n    \\\"L14\\\": 0.1554,\\n    \\\"L15\\\": 0.1555,\\n    \\\"L16\\\": 0.1551,\\n    \\\"L17\\\": 0.1552,\\n    \\\"L18\\\": 0.1553,\\n    \\\"L19\\\": 0.1553,\\n    \\\"L20\\\": 0.1554,\\n    \\\"L21\\\": 0.1555,\\n    \\\"L22\\\": 0.1555,\\n    \\\"L23\\\": 0.1555,\\n    \\\"L24\\\": 0.1555,\\n    \\\"L25\\\": 0.1555,\\n    \\\"L26\\\": 0.1555,\\n    \\\"L27\\\": 0.1555,\\n    \\\"L28\\\": 0.1555,\\n    \\\"L29\\\": 0.1555,\\n    \\\"L30\\\": 0.1555,\\n    \\\"L31\\\": 0.1555\\n  },\\n  \\\"peak_layer\\\": 15,\\n  \\\"peak_r2\\\": 0.1555,\\n  \\\"exit_r2\\\": 0.1555,\\n  \\\"exit_collapse\\\": 0.0,\\n  \\\"mean_r2\\\": 0.1553\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_phi3_full_r2_profile_20260523T235913",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-24T00:00:16.009988+00:00_

Llama-2-chat 也有 NLP control 数据（在 `llama2chat_action_probe/` 目录下，note 同样标注 "text-only model"）。

## Phi-3-mini-instruct (L0–L31)

| Layer | R² |
|-------|------|
| L0 | 0.1555 |
| L1 | 0.1552 |
| L2 | 0.1555 |
| L3 | 0.1553 |
| L4 | 0.1554 |
| L5 | 0.1555 |
| L6 | 0.1554 |
| L7 | 0.1554 |
| L8 | 0.1555 |
| L9 | 0.1555 |
| L10 | 0.1552 |
| L11 | 0.1552 |
| L12 | 0.1554 |
| L13 | 0.1555 |
| L14 | 0.1555 |
| L15 | 0.1555 |
| L16 | 0.1555 |
| L17 | 0.1555 |
| L18 | 0.1555 |
| L19 | 0.1555 |
| L20 | 0.1555 |
| L21 | 0.1555 |
| L22 | 0.1555 |
| L23 | 0.1555 |
| L24 | 0.1555 |
| L25 | 0.1555 |
| L26 | 0.1555 |
| L27 | 0.1555 |
| L28 | 0.1555 |
| L29 | 0.1555 |
| L30 | 0.1555 |
| L31 | 0.1555 |

- **Peak**: L0 (R²=0.1555) — 多层并列
- **Exit**: L31 (R²=0.1555)
- **ΔR² (peak–exit)**: 0.0000
- **ΔR² (max–min)**: 0.0003 (0.1555 − 0.1552)
- **Mean R²**: 0.1555

## Llama-2-7b-chat (L0–L31)

| Layer | R² |
|-------|------|
| L0 | 0.1553 |
| L1 | 0.1554 |
| L2 | 0.1551 |
| L3 | 0.1554 |
| L4 | 0.1552 |
| L5 | 0.1554 |
| L6 | 0.1547 |
| L7 | 0.1551 |
| L8 | 0.1552 |
| L9 | 0.1553 |
| L10 | 0.1553 |
| L11 | 0.1553 |
| L12 | 0.1554 |
| L13 | 0.1554 |
| L14 | 0.1554 |
| L15 | 0.1555 |
| L16 | 0.1551 |
| L17 | 0.1552 |
| L18 | 0.1553 |
| L19 | 0.1553 |
| L20 | 0.1554 |
| L21–L31 | 0.1555 |

- **Peak**: L15 (R²=0.1555) — L21+ 并列
- **Exit**: L31 (R²=0.1555)
- **ΔR² (peak–exit)**: 0.0000
- **ΔR² (max–min)**: 0.0008 (0.1555 − 0.1547)
- **Mean R²**: 0.1553

## 对比

两个 backbone 的 NLP control R² profile 完全一致：

1. **所有层 R² ≈ 0.1555**，波动在 ±0.0003（Phi-3）和 ±0.0008（Llama-2）范围内，本质上是噪声。
2. **无 layer-wise 变化趋势**：没有 peak、没有 exit collapse、没有单调递增/递减。R² 完全 flat。
3. **std = 0.0**（action_r2_probing.json），说明单次 seed 运行，数值波动来自 Ridge 回归的数值精度而非实质性差异。
4. **n_unique_hidden_states = 10**：text-only model 对同一 task instruction 每个 timestep 产生相同 hidden state，hidden state 只有 10 个唯一值（对应 10 个 task），线性 probe 无法从中预测 action → R² ≈ baseline 水平，符合预期。

结论：NLP control 验证通过——纯文本 LLM 的 hidden states 不包含 action-predictive 信息，R² 在所有层均为 chance level (~0.155)，跨两个 backbone 结果一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_check_phi3_full_r2_profile_20260523T235913"
}
```

</details>

---
