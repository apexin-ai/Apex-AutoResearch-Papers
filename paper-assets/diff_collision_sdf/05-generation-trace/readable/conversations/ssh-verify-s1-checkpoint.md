# ssh verify s1 checkpoint

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_ssh_verify_s1_checkpoint_20260528T195044.jsonl`
- **Structured JSON:** [`5b01c1a6ba67ef4ffe3a.json`](../../sessions/5b/5b01c1a6ba67ef4ffe3a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-28T19:52:01.200934+00:00_

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
  "session": "worker_ssh_verify_s1_checkpoint_20260528T195044",
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

_source line 2 · 2026-05-28T19:52:01.201263+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_verify_s1_checkpoint_20260528T195044",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-28T19:52:01.201496+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-35807",
  "command": "ls -la /root/colliforce-vla/checkpoints/pi05_lora_baseline_object_pudding_seed1/30000/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_verify_s1_checkpoint_20260528T195044",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-35807",
    "command": "ls -la /root/colliforce-vla/checkpoints/pi05_lora_baseline_object_pudding_seed1/30000/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-28T19:52:01.201679+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/colliforce-vla/checkpoints/pi05_lora_baseline_object_pudding_seed1/30000/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 1.15}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_verify_s1_checkpoint_20260528T195044",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-28T19:52:01.201821+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-35807",
  "command": "ls -la /root/colliforce-vla/checkpoints/pi05_lora_baseline_object_pudding_seed0/30000/model.safetensors",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_verify_s1_checkpoint_20260528T195044",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-35807",
    "command": "ls -la /root/colliforce-vla/checkpoints/pi05_lora_baseline_object_pudding_seed0/30000/model.safetensors",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-28T19:52:01.201957+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/colliforce-vla/checkpoints/pi05_lora_baseline_object_pudding_seed0/30000/model.safetensors': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_verify_s1_checkpoint_20260528T195044",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-28T19:52:01.202082+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-35807",
  "command": "find /root/colliforce-vla/checkpoints/ -path \"*seed1*\" -name \"*.safetensors\" -ls",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_verify_s1_checkpoint_20260528T195044",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-35807",
    "command": "find /root/colliforce-vla/checkpoints/ -path \"*seed1*\" -name \"*.safetensors\" -ls",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-28T19:52:01.202205+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"find: '/root/colliforce-vla/checkpoints/': No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_verify_s1_checkpoint_20260528T195044",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-28T19:52:01.202324+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-35807",
  "command": "find /root/autodl-tmp/checkpoints/ -path \"*seed1*\" -name \"*.safetensors\" -ls",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_verify_s1_checkpoint_20260528T195044",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-35807",
    "command": "find /root/autodl-tmp/checkpoints/ -path \"*seed1*\" -name \"*.safetensors\" -ls",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-28T19:52:01.202504+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"33288629011 7363396 -rw-r--r--   1 root     root     7540115784 May 24 03:21 /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed1_l005/best/model_lora.safetensors\\n33289058625 7297944 -rw-r--r--   1 root     root     7473091320 May 25 13:06 /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed1_l005/best/model_base_backup.safetensors\\n33289631997       0 lrwxrwxrwx   1 root     root             22 May 26 01:02 /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed1_l005/best/model.safetensors -> model_lora.safetensors\\n 8596893559 7363396 -rw-r--r--   1 root     root     7540115784 May 24 21:24 /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed1_l005/29999/model.safetensors\\n11818173113 7363396 -rw-r--r--   1 root     root     7540115784 May 24 21:24 /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed1_l005/30000/model.safetensors\\n 5385359606 7363396 -rw-r--r--   1 root     root     7540115784 May 24 03:22 /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed1_l01/best/model_lora.safetensors\\n 5385376067 7297944 -rw-r--r--   1 root     root     7473091320 May 25 13:06 /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed1_l01/best/model_base_backup.safetensors\\n 5385359553       0 lrwxrwxrwx   1 root     root             22 May 26 01:02 /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed1_l01/best/model.safetensors -> model_lora.safetensors\\n15045213630 7363396 -rw-r--r--   1 root     root     7540115784 May 24 21:24 /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed1_l01/29999/model.safetensors\\n18255453026 7363396 -rw-r--r--   1 root     root     7540115784 May 24 21:24 /root/autodl-tmp/c
…[truncated 988 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_verify_s1_checkpoint_20260528T195044",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-28T19:52:01.202693+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-45947",
  "command": "ls -la /root/diff_collision_sdf/checkpoints/pi05_lora_baseline_s1/step_30000/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_verify_s1_checkpoint_20260528T195044",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-45947",
    "command": "ls -la /root/diff_collision_sdf/checkpoints/pi05_lora_baseline_s1/step_30000/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-28T19:52:01.202825+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/diff_collision_sdf/checkpoints/pi05_lora_baseline_s1/step_30000/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.88}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_verify_s1_checkpoint_20260528T195044",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-28T19:52:01.202947+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-45947",
  "command": "ls -la /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/pi05_lora_baseline_object_pudding_seed1/30000/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_verify_s1_checkpoint_20260528T195044",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-45947",
    "command": "ls -la /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/pi05_lora_baseline_object_pudding_seed1/30000/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-28T19:52:01.203076+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 7490864\\ndrwxr-xr-x 3 root root        136 May 26 09:32 .\\ndrwxr-xr-x 4 root root         92 May 26 16:29 ..\\ndrwxr-xr-x 3 root root         39 May 26 09:32 assets\\n-rw-r--r-- 1 root root       1321 May 26 09:32 baseline_metadata.pt\\n-rw-r--r-- 1 root root       3059 May 26 09:32 metadata.pt\\n-rw-r--r-- 1 root root 7540115784 May 26 09:32 model.safetensors\\n-rw-r--r-- 1 root root  130517622 May 26 09:32 optimizer.pt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_verify_s1_checkpoint_20260528T195044",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-28T19:52:01.203199+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-45947",
  "command": "find /root/ -path \"*lora*seed1*\" -name \"*.safetensors\" -ls",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_verify_s1_checkpoint_20260528T195044",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-45947",
    "command": "find /root/ -path \"*lora*seed1*\" -name \"*.safetensors\" -ls",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-28T19:52:01.203325+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-45947",
  "command": "find /root/ -path \"*lora*baseline*s1*\" -name \"*.safetensors\" -ls",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_verify_s1_checkpoint_20260528T195044",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-45947",
    "command": "find /root/ -path \"*lora*baseline*s1*\" -name \"*.safetensors\" -ls",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-28T19:52:01.203484+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"8595395467 7363396 -rw-r--r--   1 root     root     7540115784 May 25 08:43 /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/pi05_lora_baseline_object_pudding_seed1/best/model.safetensors\\n26850941904 7363396 -rw-r--r--   1 root     root     7540115784 May 26 09:32 /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/pi05_lora_baseline_object_pudding_seed1/30000/model.safetensors\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.74}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_verify_s1_checkpoint_20260528T195044",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-28T19:52:01.203626+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.79}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_verify_s1_checkpoint_20260528T195044",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-28T19:52:01.203798+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-45947",
  "command": "find /root/diff_collision_sdf/checkpoints/ -name \"*.safetensors\" -ls",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_verify_s1_checkpoint_20260528T195044",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-45947",
    "command": "find /root/diff_collision_sdf/checkpoints/ -name \"*.safetensors\" -ls",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-28T19:52:01.203934+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"find: '/root/diff_collision_sdf/checkpoints/': No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_verify_s1_checkpoint_20260528T195044",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-28T19:52:01.204053+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-35807",
  "command": "ls -la /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/pi05_lora_baseline_object_pudding_seed1/30000/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_verify_s1_checkpoint_20260528T195044",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-35807",
    "command": "ls -la /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/pi05_lora_baseline_object_pudding_seed1/30000/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-28T19:52:01.204175+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 1552\\ndrwxr-xr-x 2 root root      39 May 26 09:32 .\\ndrwxr-xr-x 3 root root      27 May 28 18:19 ..\\n-rw-r--r-- 1 root root 1589248 May 26 09:32 model.safetensors\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_verify_s1_checkpoint_20260528T195044",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-28T19:52:01.204291+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-35807",
  "command": "ls -la /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/pi05_lora_baseline_object_pudding_seed0/30000/model.safetensors",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_verify_s1_checkpoint_20260528T195044",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-35807",
    "command": "ls -la /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/pi05_lora_baseline_object_pudding_seed0/30000/model.safetensors",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-28T19:52:01.204443+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 7540115784 May 27 17:48 /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/pi05_lora_baseline_object_pudding_seed0/30000/model.safetensors\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_verify_s1_checkpoint_20260528T195044",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-28T19:52:01.204657+00:00_

## 检查结果汇总

### westd-35807 — ⚠️ 确认存在损坏 checkpoint

| 路径 (均在 `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/` 下) | 大小 | 修改时间 | 状态 |
|---|---|---|---|
| `pi05_lora_baseline_object_pudding_seed1/30000/model.safetensors` | **1,589,248 (1.52 MB)** | May 26 09:32 | **⚠️ 损坏** |
| `pi05_lora_baseline_object_pudding_seed0/30000/model.safetensors` | 7,540,115,784 (7.02 GB) | May 27 17:48 | ✅ 正常 |
| `a1_sdf_pi05_object_pudding_seed1_l005/30000/model.safetensors` | 7,540,115,784 | May 24 21:24 | ✅ 正常 |
| `a1_sdf_pi05_object_pudding_seed1_l01/30000/model.safetensors` | 7,540,115,784 | May 24 21:24 | ✅ 正常 |
| `a1_sdf_pi05_object_pudding_seed1_l1/30000/model.safetensors` | 7,540,115,784 | May 27 17:50 | ✅ 正常 |

损坏目录下**只有 model.safetensors 一个文件**（无 optimizer.pt、metadata.pt），说明这是一个不完整的拷贝/同步产物。

### westd-45947 — ✅ 完好

| 路径 (均在 `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/` 下) | 大小 | 修改时间 | 状态 |
|---|---|---|---|
| `pi05_lora_baseline_object_pudding_seed1/30000/model.safetensors` | 7,540,115,784 (7.02 GB) | May 26 09:32 | ✅ 正常 |
| `pi05_lora_baseline_object_pudding_seed1/best/model.safetensors` | 7,540,115,784 | May 25 08:43 | ✅ 正常 |

该目录包含完整文件集（model.safetensors + optimizer.pt + metadata.pt + baseline_metadata.pt）。

### 关键结论

1. **损坏确认**：westd-35807 上 `pi05_lora_baseline_object_pudding_seed1/30000/model.safetensors` 确实损坏，仅 1.52 MB（正常应为 7.02 GB），且目录不完整
2. **完好副本存在**：westd-45947 上**同路径**的 checkpoint 完好（7.02 GB），可直接用于恢复
3. **Table 4 eval 路径**：`/root/diff_collision_sdf/checkpoints/pi05_lora_baseline_s1/step_30000/` 在 westd-45947 上**不存在**（`/root/diff_collision_sdf/checkpoints/` 整个目录不存在）。实际 eval 用的应该是 `/root/autodl-tmp/checkpoints/...` 路径下的那个，该 checkpoint 完好
4. **其他 seed1 变体**（l005/l01/l1）在 westd-35807 上全部正常（7.02 GB）

**修复方案**：从 westd-45947 的完好副本 scp 到 westd-35807 覆盖损坏文件即可。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ssh_verify_s1_checkpoint_20260528T195044"
}
```

</details>

---
