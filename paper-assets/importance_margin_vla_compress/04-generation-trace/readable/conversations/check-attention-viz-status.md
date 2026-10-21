# check attention viz status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_check_attention_viz_status_20260517T111707.jsonl`
- **Structured JSON:** [`a77d29fac259bce7d7f7.json`](../../sessions/a7/a77d29fac259bce7d7f7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-17T11:17:45.321111+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_attention_viz_status_20260517T111707",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T11:17:45.321571+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_attention_viz_status_20260517T111707",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T11:17:45.321743+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "tmux has-session -t attention_viz 2>/dev/null && echo \"running\" || echo \"done\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_attention_viz_status_20260517T111707",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "tmux has-session -t attention_viz 2>/dev/null && echo \"running\" || echo \"done\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-17T11:17:45.321876+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "nvidia-smi --query-gpu=index,memory.used,utilization.gpu --format=csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_attention_viz_status_20260517T111707",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "nvidia-smi --query-gpu=index,memory.used,utilization.gpu --format=csv",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-17T11:17:45.322009+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"done\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.95}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_attention_viz_status_20260517T111707",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-17T11:17:45.322133+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "ls -la /root/autodl-tmp/importance_margin_vla_compress/artifacts/attention_*.* 2>/dev/null; ls -la /root/autodl-tmp/importance_margin_vla_compress/artifacts/*heatmap* 2>/dev/null; ls -la /root/autodl-tmp/importance_margin_vla_compress/artifacts/*distribution* 2>/dev/null; ls -la /root/autodl-tmp/importance_margin_vla_compress/artifacts/*.npz 2>/dev/null; ls -la /root/autodl-tmp/importance_margin_vla_compress/artifacts/*.pdf 2>/dev/null; echo \"---ALL FILES---\"; ls -la /root/autodl-tmp/importance_margin_vla_compress/artifacts/ 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_attention_viz_status_20260517T111707",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "ls -la /root/autodl-tmp/importance_margin_vla_compress/artifacts/attention_*.* 2>/dev/null; ls -la /root/autodl-tmp/importance_margin_vla_compress/artifacts/*heatmap* 2>/dev/null; ls -la /root/autodl-tmp/importance_margin_vla_compress/artifacts/*distribution* 2>/dev/null; ls -la /root/autodl-tmp/importance_margin_vla_compress/artifacts/*.npz 2>/dev/null; ls -la /root/autodl-tmp/importance_margin_vla_compress/artifacts/*.pdf 2>/dev/null; echo \"---ALL FILES---\"; ls -la /root/autodl-tmp/importance_margin_vla_compress/artifacts/ 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-17T11:17:45.322320+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"index, memory.used [MiB], utilization.gpu [%]\\n0, 1 MiB, 0 %\\n1, 3332 MiB, 31 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.93}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_attention_viz_status_20260517T111707",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T11:17:45.322479+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 34222340 May 17 18:34 /root/autodl-tmp/importance_margin_vla_compress/artifacts/attention_data.npz\\n-rw-r--r-- 1 root root    28024 May 17 18:34 /root/autodl-tmp/importance_margin_vla_compress/artifacts/attention_distribution.pdf\\n-rw-r--r-- 1 root root   196407 May 17 18:34 /root/autodl-tmp/importance_margin_vla_compress/artifacts/attention_distribution.png\\n-rw-r--r-- 1 root root   139964 May 17 18:34 /root/autodl-tmp/importance_margin_vla_compress/artifacts/attention_heatmap.pdf\\n-rw-r--r-- 1 root root   415638 May 17 18:34 /root/autodl-tmp/importance_margin_vla_compress/artifacts/attention_heatmap.png\\n-rw-r--r-- 1 root root      500 May 17 18:34 /root/autodl-tmp/importance_margin_vla_compress/artifacts/attention_metadata.json\\n-rw-r--r-- 1 root root    24187 May 17 18:34 /root/autodl-tmp/importance_margin_vla_compress/artifacts/attention_per_task.pdf\\n-rw-r--r-- 1 root root    52485 May 17 18:34 /root/autodl-tmp/importance_margin_vla_compress/artifacts/attention_per_task.png\\n-rw-r--r-- 1 root root     3248 May 17 18:34 /root/autodl-tmp/importance_margin_vla_compress/artifacts/attention_viz.log\\n-rw-r--r-- 1 root root 139964 May 17 18:34 /root/autodl-tmp/importance_margin_vla_compress/artifacts/attention_heatmap.pdf\\n-rw-r--r-- 1 root root 415638 May 17 18:34 /root/autodl-tmp/importance_margin_vla_compress/artifacts/attention_heatmap.png\\n-rw-r--r-- 1 root root  28024 May 17 18:34 /root/autodl-tmp/importance_margin_vla_compress/artifacts/attention_distribution.pdf\\n-rw-r--r-- 1 root root 196407 May 17 18:34 /root/autodl-tmp/importance_margin_vla_compress/artifacts/attention_distribution.png\\n-rw-r--r-- 1 root root 34222340 May 17 18:34 /root/autodl-tmp/importance_margin_vla_compress/artifacts/attention_data.npz\\n-rw-r--r-- 1 root root  68438 May 17 18:31 /root/autodl-tmp/importance_margin_vla_compress/artifacts/action_divergence_curve.pdf\\n-rw-r--r-- 1 root root  17598
…[truncated 2294 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_attention_viz_status_20260517T111707",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T11:17:45.322648+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "cat /root/autodl-tmp/importance_margin_vla_compress/artifacts/attention_metadata.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_attention_viz_status_20260517T111707",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "cat /root/autodl-tmp/importance_margin_vla_compress/artifacts/attention_metadata.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T11:17:45.322789+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"checkpoint\\\": \\\"checkpoints/libero_full_ft_100k/checkpoint.pt\\\",\\n  \\\"config\\\": \\\"configs/libero_full_ft.yaml\\\",\\n  \\\"suite\\\": \\\"libero_object\\\",\\n  \\\"task_ids\\\": [\\n    0,\\n    3,\\n    7\\n  ],\\n  \\\"n_vis_per_cam\\\": 64,\\n  \\\"n_cameras\\\": 2,\\n  \\\"num_attention_heads\\\": 15,\\n  \\\"num_vlm_layers\\\": 16,\\n  \\\"overall_entropy\\\": 6.8599025181657876,\\n  \\\"max_entropy\\\": 7.0,\\n  \\\"uniformity_ratio\\\": 0.979986074023684,\\n  \\\"cam1_fraction\\\": 0.5382907390594482,\\n  \\\"n_attention_captures\\\": 2400,\\n  \\\"stacked_shape\\\": [\\n    2400,\\n    15,\\n    128\\n  ]\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.72}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_attention_viz_status_20260517T111707",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-17T11:17:45.322952+00:00_

## attention_viz 状态：已完成

**tmux session**: `attention_viz` 已退出，GPU 0 空闲 (1 MiB)。

### 产出文件（全部生成于 18:34）

| 文件 | 大小 |
|------|------|
| `attention_data.npz` | 32.6 MB |
| `attention_heatmap.pdf` / `.png` | 137 KB / 406 KB |
| `attention_distribution.pdf` / `.png` | 27 KB / 192 KB |
| `attention_per_task.pdf` / `.png` | 24 KB / 51 KB |
| `attention_metadata.json` | 500 B |
| `attention_viz.log` | 3.2 KB |

### Metadata 摘要

- **Checkpoint**: `checkpoints/libero_full_ft_100k/checkpoint.pt`
- **Suite**: `libero_object`, tasks [0, 3, 7]
- **Attention captures**: 2400 samples, shape `[2400, 15, 128]` (15 heads, 128 tokens)
- **Overall entropy**: 6.86 / 7.0 (uniformity ratio **0.98**) — attention 分布接近均匀
- **Cam1 fraction**: 0.538 — 两个相机的 attention 近乎均分

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_check_attention_viz_status_20260517T111707"
}
```

</details>

---
