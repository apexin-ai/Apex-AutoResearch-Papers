# infra verify 50k checkpoints

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_infra_verify-50k-checkpoints_20260521T152543.jsonl`
- **Structured JSON:** [`97b17c01945ce76e4c9d.json`](../../sessions/97/97b17c01945ce76e4c9d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-21T15:26:51.339796+00:00_

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
  "session": "worker_infra_verify-50k-checkpoints_20260521T152543",
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

_source line 2 · 2026-05-21T15:26:51.340098+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_verify-50k-checkpoints_20260521T152543",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T15:26:51.340291+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34685",
  "command": "ls -la /root/autodl-tmp/checkpoints/occ_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_verify-50k-checkpoints_20260521T152543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34685",
    "command": "ls -la /root/autodl-tmp/checkpoints/occ_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T15:26:51.340428+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34685",
  "command": "ls -la /root/autodl-tmp/checkpoints/occ_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_verify-50k-checkpoints_20260521T152543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34685",
    "command": "ls -la /root/autodl-tmp/checkpoints/occ_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-21T15:26:51.340597+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 365320\\ndrwxr-xr-x 3 root root      4096 May 21 20:26 .\\ndrwxr-xr-x 6 root root      4096 May 21 15:02 ..\\n-rw-r--r-- 1 root root 302243095 May 21 14:56 action_head--50000_checkpoint.pt\\nlrwxrwxrwx 1 root root       146 May 21 15:03 added_tokens.json -> /root/autodl-tmp/checkpoints/occ_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--47500_chkpt/added_tokens.json\\nlrwxrwxrwx 1 root root       140 May 21 15:03 config.json -> /root/autodl-tmp/checkpoints/occ_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--47500_chkpt/config.json\\n-rw-r--r-- 1 root root     60863 May 21 14:16 config.json.back.20260521_150358\\n-rw-r--r-- 1 root root     60862 May 21 15:04 config.json.back.20260521_161804\\n-rw-r--r-- 1 root root     60862 May 21 16:18 config.json.back.20260521_202630\\n-rw-r--r-- 1 root root      5865 May 20 19:34 configuration_prismatic.py\\n-rw-r--r-- 1 root root      2957 May 21 14:56 dataset_statistics.json\\nlrwxrwxrwx 1 root root       151 May 21 15:03 generation_config.json -> /root/autodl-tmp/checkpoints/occ_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--47500_chkpt/generation_config.json\\ndrwxr-xr-x 2 root root        99 May 21 14:56 lora_adapter\\nlrwxrwxrwx 1 root root       161 May 21 15:03 model-00001-of-00004.safetensors -> /root/autodl-tmp/checkpoints/occ_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--47500_chkpt/model-00001-of-00004.safetensors\\nlrwxrwxrwx 1 root root       161 May 21 15:03 model-00002-of-00004.safetensors -> /root/autodl-tmp/checkpoints/occ_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--47500_chkpt/model-00002-of-00004.safetensors\\nlrwxrwxrwx 1 root root       161 May 21 15:03 model-00003-of-00004.safetensors -> /root/autodl-tmp/checkpoints/occ_s0/openvla-7b+libero_spatial_no_noops+b8+lr
…[truncated 1543 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_verify-50k-checkpoints_20260521T152543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T15:26:51.340808+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 365320\\ndrwxr-xr-x 3 root root      4096 May 21 20:43 .\\ndrwxr-xr-x 6 root root      4096 May 21 15:02 ..\\n-rw-r--r-- 1 root root 302243095 May 21 14:56 action_head--50000_checkpoint.pt\\nlrwxrwxrwx 1 root root       146 May 21 15:03 added_tokens.json -> /root/autodl-tmp/checkpoints/occ_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--47500_chkpt/added_tokens.json\\nlrwxrwxrwx 1 root root       140 May 21 15:03 config.json -> /root/autodl-tmp/checkpoints/occ_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--47500_chkpt/config.json\\n-rw-r--r-- 1 root root     60863 May 21 14:17 config.json.back.20260521_150429\\n-rw-r--r-- 1 root root     60862 May 21 15:05 config.json.back.20260521_161835\\n-rw-r--r-- 1 root root     60862 May 21 16:18 config.json.back.20260521_204346\\n-rw-r--r-- 1 root root      5865 May 20 19:34 configuration_prismatic.py\\n-rw-r--r-- 1 root root      2957 May 21 14:56 dataset_statistics.json\\nlrwxrwxrwx 1 root root       151 May 21 15:03 generation_config.json -> /root/autodl-tmp/checkpoints/occ_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--47500_chkpt/generation_config.json\\ndrwxr-xr-x 2 root root        99 May 21 14:56 lora_adapter\\nlrwxrwxrwx 1 root root       161 May 21 15:03 model-00001-of-00004.safetensors -> /root/autodl-tmp/checkpoints/occ_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--47500_chkpt/model-00001-of-00004.safetensors\\nlrwxrwxrwx 1 root root       161 May 21 15:03 model-00002-of-00004.safetensors -> /root/autodl-tmp/checkpoints/occ_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--47500_chkpt/model-00002-of-00004.safetensors\\nlrwxrwxrwx 1 root root       161 May 21 15:03 model-00003-of-00004.safetensors -> /root/autodl-tmp/checkpoints/occ_s2/openvla-7b+libero_spatial_no_noops+b8+lr
…[truncated 1543 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_verify-50k-checkpoints_20260521T152543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T15:26:51.340966+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34685",
  "command": "ls -la /root/autodl-tmp/checkpoints/occ_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--47500_chkpt/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_verify-50k-checkpoints_20260521T152543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34685",
    "command": "ls -la /root/autodl-tmp/checkpoints/occ_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--47500_chkpt/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T15:26:51.341117+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 15095028\\ndrwxr-xr-x 3 root root       4096 May 21 22:47 .\\ndrwxr-xr-x 6 root root       4096 May 21 15:02 ..\\n-rw-r--r-- 1 root root  302243095 May 21 14:16 action_head--47500_checkpoint.pt\\n-rw-r--r-- 1 root root         21 May 21 14:16 added_tokens.json\\n-rw-r--r-- 1 root root      60862 May 21 22:47 config.json\\n-rw-r--r-- 1 root root      60862 May 21 15:03 config.json.back.20260521_150420\\n-rw-r--r-- 1 root root      60862 May 21 20:26 config.json.back.20260521_224749\\n-rw-r--r-- 1 root root       5865 May 21 14:16 configuration_prismatic.py\\n-rw-r--r-- 1 root root       2957 May 21 14:16 dataset_statistics.json\\n-rw-r--r-- 1 root root        136 May 21 14:16 generation_config.json\\ndrwxr-xr-x 2 root root         99 May 21 14:16 lora_adapter\\n-rw-r--r-- 1 root root 4925122448 May 21 14:17 model-00001-of-00004.safetensors\\n-rw-r--r-- 1 root root 4947392496 May 21 14:17 model-00002-of-00004.safetensors\\n-rw-r--r-- 1 root root 4947417456 May 21 14:17 model-00003-of-00004.safetensors\\n-rw-r--r-- 1 root root  262668432 May 21 14:17 model-00004-of-00004.safetensors\\n-rw-r--r-- 1 root root      94764 May 21 14:17 model.safetensors.index.json\\n-rw-r--r-- 1 root root      49036 May 21 14:16 modeling_prismatic.py\\n-rw-r--r-- 1 root root    2434741 May 21 14:16 occ_head--47500_checkpoint.pt\\n-rw-r--r-- 1 root root       1650 May 21 14:16 preprocessor_config.json\\n-rw-r--r-- 1 root root      12718 May 21 14:16 processing_prismatic.py\\n-rw-r--r-- 1 root root        130 May 21 14:16 processor_config.json\\n-rw-r--r-- 1 root root   67275701 May 21 14:16 proprio_projector--47500_checkpoint.pt\\n-rw-r--r-- 1 root root        552 May 21 14:16 special_tokens_map.json\\n-rw-r--r-- 1 root root    1842976 May 21 14:16 tokenizer.json\\n-rw-r--r-- 1 root root     499723 May 21 14:16 tokenizer.model\\n-rw-r--r-- 1 root root       1192 May 21 14:16 tokenizer_config.json\\n\", \"stderr\": \"\", \"return_c
…[truncated 72 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_verify-50k-checkpoints_20260521T152543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T15:26:51.341265+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34685",
  "command": "ls -la /root/autodl-tmp/checkpoints/occ_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--47500_chkpt/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_verify-50k-checkpoints_20260521T152543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34685",
    "command": "ls -la /root/autodl-tmp/checkpoints/occ_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--47500_chkpt/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T15:26:51.341411+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 15095028\\ndrwxr-xr-x 3 root root       4096 May 21 22:53 .\\ndrwxr-xr-x 6 root root       4096 May 21 15:02 ..\\n-rw-r--r-- 1 root root  302243095 May 21 14:17 action_head--47500_checkpoint.pt\\n-rw-r--r-- 1 root root         21 May 21 14:17 added_tokens.json\\n-rw-r--r-- 1 root root      60862 May 21 22:53 config.json\\n-rw-r--r-- 1 root root      60862 May 21 15:04 config.json.back.20260521_150502\\n-rw-r--r-- 1 root root      60862 May 21 20:43 config.json.back.20260521_225318\\n-rw-r--r-- 1 root root       5865 May 21 14:17 configuration_prismatic.py\\n-rw-r--r-- 1 root root       2957 May 21 14:17 dataset_statistics.json\\n-rw-r--r-- 1 root root        136 May 21 14:17 generation_config.json\\ndrwxr-xr-x 2 root root         99 May 21 14:17 lora_adapter\\n-rw-r--r-- 1 root root 4925122448 May 21 14:17 model-00001-of-00004.safetensors\\n-rw-r--r-- 1 root root 4947392496 May 21 14:17 model-00002-of-00004.safetensors\\n-rw-r--r-- 1 root root 4947417456 May 21 14:17 model-00003-of-00004.safetensors\\n-rw-r--r-- 1 root root  262668432 May 21 14:17 model-00004-of-00004.safetensors\\n-rw-r--r-- 1 root root      94764 May 21 14:17 model.safetensors.index.json\\n-rw-r--r-- 1 root root      49036 May 21 14:17 modeling_prismatic.py\\n-rw-r--r-- 1 root root    2434741 May 21 14:17 occ_head--47500_checkpoint.pt\\n-rw-r--r-- 1 root root       1650 May 21 14:17 preprocessor_config.json\\n-rw-r--r-- 1 root root      12718 May 21 14:17 processing_prismatic.py\\n-rw-r--r-- 1 root root        130 May 21 14:17 processor_config.json\\n-rw-r--r-- 1 root root   67275701 May 21 14:17 proprio_projector--47500_checkpoint.pt\\n-rw-r--r-- 1 root root        552 May 21 14:17 special_tokens_map.json\\n-rw-r--r-- 1 root root    1842976 May 21 14:17 tokenizer.json\\n-rw-r--r-- 1 root root     499723 May 21 14:17 tokenizer.model\\n-rw-r--r-- 1 root root       1192 May 21 14:17 tokenizer_config.json\\n\", \"stderr\": \"\", \"return_c
…[truncated 72 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_verify-50k-checkpoints_20260521T152543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T15:26:51.341592+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34685",
  "command": "ls -la /root/autodl-tmp/checkpoints/occ_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt/lora_adapter/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_verify-50k-checkpoints_20260521T152543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34685",
    "command": "ls -la /root/autodl-tmp/checkpoints/occ_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt/lora_adapter/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T15:26:51.341818+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 473124\\ndrwxr-xr-x 2 root root        99 May 21 14:56 .\\ndrwxr-xr-x 3 root root      4096 May 21 20:26 ..\\n-rw-r--r-- 1 root root      5202 May 21 14:56 README.md\\n-rw-r--r-- 1 root root      1131 May 21 14:56 adapter_config.json\\n-rw-r--r-- 1 root root 484458600 May 21 14:56 adapter_model.safetensors\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_verify-50k-checkpoints_20260521T152543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T15:26:51.342024+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34685",
  "command": "ls -la /root/autodl-tmp/checkpoints/occ_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt/lora_adapter/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_verify-50k-checkpoints_20260521T152543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34685",
    "command": "ls -la /root/autodl-tmp/checkpoints/occ_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt/lora_adapter/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T15:26:51.342231+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 473124\\ndrwxr-xr-x 2 root root        99 May 21 14:56 .\\ndrwxr-xr-x 3 root root      4096 May 21 20:43 ..\\n-rw-r--r-- 1 root root      5202 May 21 14:56 README.md\\n-rw-r--r-- 1 root root      1131 May 21 14:56 adapter_config.json\\n-rw-r--r-- 1 root root 484458600 May 21 14:56 adapter_model.safetensors\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_verify-50k-checkpoints_20260521T152543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T15:26:51.342424+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34685",
  "command": "ls -la /root/autodl-tmp/checkpoints/occ_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--47500_chkpt/lora_adapter/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_verify-50k-checkpoints_20260521T152543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34685",
    "command": "ls -la /root/autodl-tmp/checkpoints/occ_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--47500_chkpt/lora_adapter/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T15:26:51.342637+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 473124\\ndrwxr-xr-x 2 root root        99 May 21 14:16 .\\ndrwxr-xr-x 3 root root      4096 May 21 22:47 ..\\n-rw-r--r-- 1 root root      5202 May 21 14:16 README.md\\n-rw-r--r-- 1 root root      1131 May 21 14:16 adapter_config.json\\n-rw-r--r-- 1 root root 484458600 May 21 14:16 adapter_model.safetensors\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_verify-50k-checkpoints_20260521T152543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T15:26:51.342850+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34685",
  "command": "ls -la /root/autodl-tmp/checkpoints/occ_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--47500_chkpt/lora_adapter/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_verify-50k-checkpoints_20260521T152543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34685",
    "command": "ls -la /root/autodl-tmp/checkpoints/occ_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--47500_chkpt/lora_adapter/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T15:26:51.343045+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 473124\\ndrwxr-xr-x 2 root root        99 May 21 14:17 .\\ndrwxr-xr-x 3 root root      4096 May 21 22:53 ..\\n-rw-r--r-- 1 root root      5202 May 21 14:17 README.md\\n-rw-r--r-- 1 root root      1131 May 21 14:17 adapter_config.json\\n-rw-r--r-- 1 root root 484458600 May 21 14:17 adapter_model.safetensors\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_verify-50k-checkpoints_20260521T152543",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-21T15:26:51.343333+00:00_

## 判定结果

### occ_s0 50K: **COMPLETE**
### occ_s2 50K: **COMPLETE**

两个 50K checkpoint 结构完全一致，采用了 **symlink 节省空间策略**：基础模型权重（safetensors）符号链接到 47500 checkpoint，可训练组件为独立文件。

---

### 文件大小对比

**可训练组件（50K 独立文件）vs 47500 参考：**

| 文件 | occ_s0 50K | occ_s0 47500 | occ_s2 50K | occ_s2 47500 |
|------|-----------|-------------|-----------|-------------|
| action_head .pt | 302,243,095 | 302,243,095 | 302,243,095 | 302,243,095 |
| occ_head .pt | 2,434,741 | 2,434,741 | 2,434,741 | 2,434,741 |
| proprio_projector .pt | 67,275,701 | 67,275,701 | 67,275,701 | 67,275,701 |
| lora_adapter/adapter_model.safetensors | 484,458,600 | 484,458,600 | 484,458,600 | 484,458,600 |

文件大小完全一致——这是预期行为，因为模型架构不变，safetensors/pt 格式的文件大小由 tensor shape 和 dtype 决定，与权重值无关。

**基础模型（50K 通过 symlink 引用 47500 的实际文件）：**

| 文件 | 47500 实际大小 |
|------|--------------|
| model-00001-of-00004.safetensors | 4,925,122,448 (~4.59GB) |
| model-00002-of-00004.safetensors | 4,947,392,496 (~4.61GB) |
| model-00003-of-00004.safetensors | 4,947,417,456 (~4.61GB) |
| model-00004-of-00004.safetensors | 262,668,432 (~250MB) |

**注意事项：** 50K checkpoint 依赖 47500 checkpoint 的 symlink 目标。如果 47500 被删除，50K 将不可用。目前 47500 完好。

### 结构说明

50K checkpoint 没有独立的 `action_head/` 或 `occ_head/` 目录，而是用 `action_head--50000_checkpoint.pt` 和 `occ_head--50000_checkpoint.pt` 等独立 .pt 文件保存，与 47500 格式一致。`lora_adapter/` 目录包含完整的 adapter（README.md + adapter_config.json + adapter_model.safetensors）。不存在文件截断或缺失的迹象。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_infra_verify-50k-checkpoints_20260521T152543"
}
```

</details>

---
