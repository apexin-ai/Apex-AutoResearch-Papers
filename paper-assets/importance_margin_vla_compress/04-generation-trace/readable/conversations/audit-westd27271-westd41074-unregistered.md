# audit westd27271 westd41074 unregistered

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_audit_westd27271_westd41074_unregistered_20260526T172811.jsonl`
- **Structured JSON:** [`2fdc3251b8dbcbf84dcb.json`](../../sessions/2f/2fdc3251b8dbcbf84dcb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-26T17:29:00.183556+00:00_

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
  "session": "worker_audit_westd27271_westd41074_unregistered_20260526T172811",
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

_source line 2 · 2026-05-26T17:29:00.184031+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_westd27271_westd41074_unregistered_20260526T172811",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T17:29:00.186437+00:00_

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
  "session": "worker_audit_westd27271_westd41074_unregistered_20260526T172811",
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

_source line 4 · 2026-05-26T17:29:00.186680+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_westd27271_westd41074_unregistered_20260526T172811",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T17:29:00.186917+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "nvidia-smi --query-gpu=index,utilization.gpu,memory.used,memory.total --format=csv,noheader && echo \"---APPS---\" && nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader && echo \"---CMDLINE---\" && for pid in $(nvidia-smi --query-compute-apps=pid --format=csv,noheader | tr -d ' '); do echo \"=== PID $pid ===\"; cat /proc/$pid/cmdline 2>/dev/null | tr '\\0' ' ' || echo \"DEAD\"; echo; done && echo \"---TMUX---\" && tmux ls 2>/dev/null || echo \"NO_TMUX\"",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_westd27271_westd41074_unregistered_20260526T172811",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "nvidia-smi --query-gpu=index,utilization.gpu,memory.used,memory.total --format=csv,noheader && echo \"---APPS---\" && nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader && echo \"---CMDLINE---\" && for pid in $(nvidia-smi --query-compute-apps=pid --format=csv,noheader | tr -d ' '); do echo \"=== PID $pid ===\"; cat /proc/$pid/cmdline 2>/dev/null | tr '\\0' ' ' || echo \"DEAD\"; echo; done && echo \"---TMUX---\" && tmux ls 2>/dev/null || echo \"NO_TMUX\"",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-26T17:29:00.187155+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-41074",
  "command": "nvidia-smi --query-gpu=index,utilization.gpu,memory.used,memory.total --format=csv,noheader && echo \"---APPS---\" && nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader && echo \"---CMDLINE---\" && for pid in $(nvidia-smi --query-compute-apps=pid --format=csv,noheader | tr -d ' '); do echo \"=== PID $pid ===\"; cat /proc/$pid/cmdline 2>/dev/null | tr '\\0' ' ' || echo \"DEAD\"; echo; done && echo \"---TMUX---\" && tmux ls 2>/dev/null || echo \"NO_TMUX\"",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_westd27271_westd41074_unregistered_20260526T172811",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-41074",
    "command": "nvidia-smi --query-gpu=index,utilization.gpu,memory.used,memory.total --format=csv,noheader && echo \"---APPS---\" && nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader && echo \"---CMDLINE---\" && for pid in $(nvidia-smi --query-compute-apps=pid --format=csv,noheader | tr -d ' '); do echo \"=== PID $pid ===\"; cat /proc/$pid/cmdline 2>/dev/null | tr '\\0' ' ' || echo \"DEAD\"; echo; done && echo \"---TMUX---\" && tmux ls 2>/dev/null || echo \"NO_TMUX\"",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-26T17:29:00.187497+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 71 %, 15964 MiB, 97887 MiB\\n1, 83 %, 16188 MiB, 97887 MiB\\n---APPS---\\n414927, GPU-03bc9807-5e67-1fe5-b76d-40e4382a57be, 15946 MiB\\n397225, GPU-89080d64-c240-586a-f0cc-80a7ae15413f, 16169 MiB\\n---CMDLINE---\\n=== PID 414927 ===\\n/root/miniconda3/bin/python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.75 --suite libero_goal --seed 42 --gpu 0 \\n=== PID 397225 ===\\npython -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.5 --suite libero_10 --seed 42 --gpu 0 \\n---TMUX---\\neval_attn_k05_long: 1 windows (created Tue May 26 23:57:32 2026)\\neval_openvla_l2norm_k075_goal_seed42_v2: 1 windows (created Wed May 27 00:53:33 2026)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_westd27271_westd41074_unregistered_20260526T172811",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-26T17:29:00.187763+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 85 %, 15984 MiB, 97887 MiB\\n1, 69 %, 15984 MiB, 97887 MiB\\n2, 87 %, 15980 MiB, 97887 MiB\\n3, 70 %, 15980 MiB, 97887 MiB\\n---APPS---\\n682346, GPU-b12dc93c-f616-7421-b28e-390b63a642ba, 15965 MiB\\n652888, GPU-b927bd9e-efa6-c56c-2068-1fc57e9147c6, 15965 MiB\\n755986, GPU-754fc39d-3de8-bd70-0b93-b752430ed568, 15961 MiB\\n642262, GPU-5de49e5a-94e3-c77a-dcf3-dc0cde876f0d, 15961 MiB\\n---CMDLINE---\\n=== PID 682346 ===\\npython -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.85 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object \\n=== PID 652888 ===\\npython -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.5 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object \\n=== PID 755986 ===\\npython -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.75 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object \\n=== PID 642262 ===\\npython -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.75 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object \\n---TMUX---\\neval_openvla_attn_k075_object_seed42: 1 windows (created Wed May 27 00:41:27 2026)\\neval_openvla_l2norm_k075_object_seed42: 1 windows (created Tue May 26 21:13:20 2026)\\neval_openvla_random_k085_object_seed42: 1 windows (created Tue May 26 22:32:37 2026)\\neval_pi05_attention_k0925_long_seed42: 1 windows (created Tue May 26 05:04:39 2026)\\nprofiling_pi05_latency_westd41074: 1 windows (created Tue May 26 05:04:39 2026)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_s
…[truncated 18 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_westd27271_westd41074_unregistered_20260526T172811",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-26T17:29:00.188069+00:00_

```
WESTD-27271:
GPU0: 71% util, 16.0/97.9 GB | PID=414927 | l2norm_prune k=0.75 libero_goal seed42
GPU1: 83% util, 16.2/97.9 GB | PID=397225 | attention_prune k=0.5 libero_10 seed42

WESTD-41074:
GPU0: 85% util, 16.0/97.9 GB | PID=682346 | random_prune k=0.85 libero_object seed42
GPU1: 69% util, 16.0/97.9 GB | PID=652888 | attention_prune k=0.5 libero_object seed42
GPU2: 87% util, 16.0/97.9 GB | PID=755986 | attention_prune k=0.75 libero_object seed42
GPU3: 70% util, 16.0/97.9 GB | PID=642262 | l2norm_prune k=0.75 libero_object seed42
```

所有 6 个 GPU 均在跑实验，无空闲 GPU，无未注册进程。全部都是 `eval_openvla_l2norm_libero.py` 的不同配置（mode/k_ratio/suite 组合）。

注意：westd-27271 GPU1 的 PID 397225 确认是 `attention_prune k=0.5 libero_10`（非 `libero_long`，tmux session 名为 `eval_attn_k05_long` 但实际 cmdline 参数是 `libero_10`）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_audit_westd27271_westd41074_unregistered_20260526T172811"
}
```

</details>

---
