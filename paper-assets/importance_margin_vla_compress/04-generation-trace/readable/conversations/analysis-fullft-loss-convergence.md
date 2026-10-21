# analysis fullft loss convergence

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 0
- **Tool calls:** 22
- **Original source:** `logs/chats/worker_analysis_fullft_loss_convergence_20260518T115159.jsonl`
- **Structured JSON:** [`ed5fd957fa6c63a90828.json`](../../sessions/ed/ed5fd957fa6c63a90828.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

45 recorded events

### Tool call

_source line 1 · 2026-05-18T11:53:43.690556+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T11:53:43.691008+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T11:53:43.691255+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "ls ~/runs/importance_margin_vla_compress/ 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "ls ~/runs/importance_margin_vla_compress/ 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T11:53:43.691413+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T11:53:43.691545+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "find /root/autodl-tmp/importance_margin_vla_compress -maxdepth 4 -name \"*.log\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "find /root/autodl-tmp/importance_margin_vla_compress -maxdepth 4 -name \"*.log\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T11:53:43.691671+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T11:53:43.691793+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "find /root/autodl-tmp/importance_margin_vla_compress -path \"*/wandb/*\" -name \"wandb-summary.json\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "find /root/autodl-tmp/importance_margin_vla_compress -path \"*/wandb/*\" -name \"wandb-summary.json\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T11:53:43.691915+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T11:53:43.692063+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "ls /root/runs/importance_margin_vla_compress/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "ls /root/runs/importance_margin_vla_compress/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-18T11:53:43.692255+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "find /root/autodl-tmp/importance_margin_vla_compress -maxdepth 4 -name \"*.log\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "find /root/autodl-tmp/importance_margin_vla_compress -maxdepth 4 -name \"*.log\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-18T11:53:43.692473+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"eval_acis_k07_trained_prune.log\\neval_fullft_100k.log\\neval_k03_trained_prune.log\\neval_lora_100k.log\\neval_smart_compress_m128.log\\neval_smart_compress_m16.log\\neval_smart_compress_m96.log\\nlibero_full_ft_baseline.log\\nlibero_fullft_batch64_v2.log\\nlibero_fullft_seed0.log\\nlibero_fullft_seed1.log\\nlibero_imm_fullft_100k.log\\nlibero_imm_fullft_k07.log\\nlibero_imm_fullft_seed0.log\\nlibero_lora_baseline.log\\nlibero_lora_seed0.log\\ntrain_acis_stage1only_k03.log\\ntrain_acis_stage1only_k07.log\\ntrain_smart_compress_m128.log\\ntrain_smart_compress_m128_resume.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.11}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T11:53:43.692804+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/fullft_batch64.log\\n/root/autodl-tmp/importance_margin_vla_compress/logs/batch64_v2.log\\n/root/autodl-tmp/importance_margin_vla_compress/logs/batch64_v2_resume.log\\n/root/autodl-tmp/importance_margin_vla_compress/logs/eval_geometric_prior_k07.log\\n/root/autodl-tmp/importance_margin_vla_compress/logs/geometric_prior_k09_dryrun.log\\n/root/autodl-tmp/importance_margin_vla_compress/logs/eval_geometric_prior_k09.log\\n/root/autodl-tmp/importance_margin_vla_compress/logs/eval_geometric_prior_k05.log\\n/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_baseline.log\\n/root/autodl-tmp/importance_margin_vla_compress/logs/dryrun_pi05.log\\n/root/autodl-tmp/importance_margin_vla_compress/logs/dryrun_pi05_v2.log\\n/root/autodl-tmp/importance_margin_vla_compress/logs/dryrun_pi05_v3.log\\n/root/autodl-tmp/importance_margin_vla_compress/logs/inference_latency_comparison.log\\n/root/autodl-tmp/importance_margin_vla_compress/eval_results/smolvla_entropy_perlayer.log\\n/root/autodl-tmp/importance_margin_vla_compress/wandb/offline-run-20260516_222113-z5dzg39t/logs/debug.log\\n/root/autodl-tmp/importance_margin_vla_compress/wandb/offline-run-20260516_222113-z5dzg39t/logs/debug-internal.log\\n/root/autodl-tmp/importance_margin_vla_compress/wandb/offline-run-20260516_222113-z5dzg39t/logs/debug-core.log\\n/root/autodl-tmp/importance_margin_vla_compress/wandb/debug-internal.log\\n/root/autodl-tmp/importance_margin_vla_compress/wandb/offline-run-20260516_222118-85xsww57/logs/debug.log\\n/root/autodl-tmp/importance_margin_vla_compress/wandb/offline-run-20260516_222118-85xsww57/logs/debug-internal.log\\n/root/autodl-tmp/importance_margin_vla_compress/wandb/offline-run-20260516_222118-85xsww57/logs/debug-core.log\\n/root/autodl-tmp/importance_margin_vla_compress/wandb/debug.log\\n/root/autodl-tmp/importance_margin_vla_compress/wandb/offline-run-20260516_234321-vh28w5wa/
…[truncated 6364 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T11:53:43.693036+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "find /root/autodl-tmp/importance_margin_vla_compress -path \"*/wandb/*\" -name \"wandb-summary.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "find /root/autodl-tmp/importance_margin_vla_compress -path \"*/wandb/*\" -name \"wandb-summary.json\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T11:53:43.693306+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T11:53:43.693547+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "tail -200 /root/runs/importance_margin_vla_compress/libero_full_ft_baseline.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "tail -200 /root/runs/importance_margin_vla_compress/libero_full_ft_baseline.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T11:53:43.693858+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-17 04:45:51 [INFO] step=91250/100000  loss=0.0503  lr=4.37e-06  grad=1.14  sps=4.0\\n2026-05-17 04:46:05 [INFO] step=91300/100000  loss=0.0478  lr=4.35e-06  grad=0.87  sps=4.0\\n2026-05-17 04:46:19 [INFO] step=91350/100000  loss=0.0546  lr=4.32e-06  grad=1.25  sps=4.0\\n2026-05-17 04:46:33 [INFO] step=91400/100000  loss=0.0416  lr=4.30e-06  grad=0.96  sps=4.0\\n2026-05-17 04:46:47 [INFO] step=91450/100000  loss=0.0341  lr=4.28e-06  grad=0.51  sps=4.0\\n2026-05-17 04:47:01 [INFO] step=91500/100000  loss=0.0526  lr=4.26e-06  grad=0.69  sps=4.0\\n2026-05-17 04:47:14 [INFO] step=91550/100000  loss=0.0524  lr=4.24e-06  grad=0.68  sps=4.0\\n2026-05-17 04:47:28 [INFO] step=91600/100000  loss=0.0208  lr=4.22e-06  grad=0.81  sps=4.0\\n2026-05-17 04:47:42 [INFO] step=91650/100000  loss=0.0166  lr=4.20e-06  grad=0.77  sps=4.0\\n2026-05-17 04:47:55 [INFO] step=91700/100000  loss=0.0353  lr=4.18e-06  grad=1.54  sps=4.0\\n2026-05-17 04:48:09 [INFO] step=91750/100000  loss=0.1670  lr=4.16e-06  grad=1.36  sps=4.0\\n2026-05-17 04:48:23 [INFO] step=91800/100000  loss=0.1187  lr=4.14e-06  grad=1.77  sps=4.0\\n2026-05-17 04:48:37 [INFO] step=91850/100000  loss=0.0435  lr=4.12e-06  grad=0.90  sps=4.0\\n2026-05-17 04:48:51 [INFO] step=91900/100000  loss=0.0283  lr=4.10e-06  grad=0.72  sps=4.0\\n2026-05-17 04:49:05 [INFO] step=91950/100000  loss=0.0804  lr=4.08e-06  grad=1.35  sps=4.0\\n2026-05-17 04:49:18 [INFO] step=92000/100000  loss=0.0677  lr=4.06e-06  grad=1.19  sps=4.0\\n2026-05-17 04:49:32 [INFO] step=92050/100000  loss=0.0983  lr=4.04e-06  grad=0.84  sps=4.0\\n2026-05-17 04:49:46 [INFO] step=92100/100000  loss=0.0785  lr=4.02e-06  grad=1.40  sps=4.0\\n2026-05-17 04:50:00 [INFO] step=92150/100000  loss=0.0337  lr=4.00e-06  grad=0.80  sps=4.0\\n2026-05-17 04:50:14 [INFO] step=92200/100000  loss=0.0533  lr=3.99e-06  grad=1.12  sps=4.0\\n2026-05-17 04:50:28 [INFO] step=92250/100000  loss=0.1436  lr=3.97e-06  grad=1.66  s
…[truncated 6399 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T11:53:43.694116+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "grep -i \"loss\" /root/runs/importance_margin_vla_compress/libero_full_ft_baseline.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "grep -i \"loss\" /root/runs/importance_margin_vla_compress/libero_full_ft_baseline.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-18T11:53:43.694324+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "head -50 /root/runs/importance_margin_vla_compress/libero_full_ft_baseline.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "head -50 /root/runs/importance_margin_vla_compress/libero_full_ft_baseline.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-18T11:53:43.694613+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-16 22:21:15 [INFO] step=0/100000  loss=1.1827  lr=1.00e-07  grad=12.81  sps=0.6\\n2026-05-16 22:21:28 [INFO] step=50/100000  loss=0.7795  lr=5.10e-06  grad=7.05  sps=3.6\\n2026-05-16 22:21:40 [INFO] step=100/100000  loss=0.3926  lr=1.01e-05  grad=5.26  sps=3.8\\n2026-05-16 22:21:51 [INFO] step=150/100000  loss=0.3974  lr=1.51e-05  grad=5.07  sps=4.0\\n2026-05-16 22:22:03 [INFO] step=200/100000  loss=0.4989  lr=2.01e-05  grad=5.29  sps=4.1\\n2026-05-16 22:22:15 [INFO] step=250/100000  loss=0.2968  lr=2.51e-05  grad=2.57  sps=4.1\\n2026-05-16 22:22:26 [INFO] step=300/100000  loss=0.4451  lr=3.01e-05  grad=4.36  sps=4.1\\n2026-05-16 22:22:38 [INFO] step=350/100000  loss=0.4071  lr=3.51e-05  grad=3.41  sps=4.2\\n2026-05-16 22:22:49 [INFO] step=400/100000  loss=0.2883  lr=4.01e-05  grad=4.86  sps=4.2\\n2026-05-16 22:23:01 [INFO] step=450/100000  loss=0.3978  lr=4.51e-05  grad=6.75  sps=4.2\\n2026-05-16 22:23:12 [INFO] step=500/100000  loss=0.3394  lr=5.01e-05  grad=5.67  sps=4.2\\n2026-05-16 22:23:24 [INFO] step=550/100000  loss=0.2978  lr=5.51e-05  grad=2.87  sps=4.2\\n2026-05-16 22:23:36 [INFO] step=600/100000  loss=0.2412  lr=6.01e-05  grad=3.29  sps=4.2\\n2026-05-16 22:23:47 [INFO] step=650/100000  loss=0.2831  lr=6.51e-05  grad=6.98  sps=4.2\\n2026-05-16 22:23:59 [INFO] step=700/100000  loss=0.3549  lr=7.01e-05  grad=5.51  sps=4.2\\n2026-05-16 22:24:11 [INFO] step=750/100000  loss=0.2007  lr=7.51e-05  grad=3.93  sps=4.2\\n2026-05-16 22:24:22 [INFO] step=800/100000  loss=0.2263  lr=8.01e-05  grad=4.04  sps=4.3\\n2026-05-16 22:24:34 [INFO] step=850/100000  loss=0.2039  lr=8.51e-05  grad=2.98  sps=4.3\\n2026-05-16 22:24:45 [INFO] step=900/100000  loss=0.2130  lr=9.01e-05  grad=2.65  sps=4.3\\n2026-05-16 22:24:56 [INFO] step=950/100000  loss=0.2315  lr=9.51e-05  grad=3.77  sps=4.3\\n2026-05-16 22:25:08 [INFO] step=1000/100000  loss=0.3065  lr=1.00e-04  grad=4.71  sps=4.3\\n2026-05-16 22:25:19 [INFO] step=10
…[truncated 6385 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T11:53:43.694958+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"设置成功\\n注意：仅限于学术用途和加速访问github/huggingface，不承诺稳定性保证\\n2026-05-16 22:20:19 [INFO] Device: cuda:0\\n2026-05-16 22:20:19 [INFO] Loading SmolVLA policy...\\n2026-05-16 22:20:24 [INFO] HTTP Request: HEAD https://huggingface.co/HuggingFaceTB/SmolVLM2-500M-Video-Instruct/resolve/main/config.json \\\"HTTP/1.1 307 Temporary Redirect\\\"\\nWarning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.\\n2026-05-16 22:20:24 [WARNING] Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.\\n2026-05-16 22:20:24 [INFO] HTTP Request: HEAD https://huggingface.co/api/resolve-cache/models/HuggingFaceTB/SmolVLM2-500M-Video-Instruct/7b375e1b73b11138ff12fe22c8f2822d8fe03467/config.json \\\"HTTP/1.1 200 OK\\\"\\n2026-05-16 22:20:25 [INFO] HTTP Request: HEAD https://huggingface.co/HuggingFaceTB/SmolVLM2-500M-Video-Instruct/resolve/main/adapter_config.json \\\"HTTP/1.1 404 Not Found\\\"\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n2026-05-16 22:20:26 [INFO] HTTP Request: HEAD https://huggingface.co/HuggingFaceTB/SmolVLM2-500M-Video-Instruct/resolve/main/config.json \\\"HTTP/1.1 307 Temporary Redirect\\\"\\n2026-05-16 22:20:27 [INFO] HTTP Request: HEAD https://huggingface.co/api/resolve-cache/models/HuggingFaceTB/SmolVLM2-500M-Video-Instruct/7b375e1b73b11138ff12fe22c8f2822d8fe03467/config.json \\\"HTTP/1.1 200 OK\\\"\\nLoading  HuggingFaceTB/SmolVLM2-500M-Video-Instruct weights ...\\n\\rLoading weights:   0%|          | 0/489 [00:00<?, ?it/s]\\rLoading weights:  27%|██▋       | 131/489 [00:00<00:00, 1265.54it/s]\\rLoading weights:  53%|█████▎    | 258/489 [00:00<00:00, 1155.41it/s]\\rLoading weights:  94%|█████████▎| 458/489 [00:00<00:00, 1516.23it/s]\\rLoading weights: 100%|██████████| 489/489 [00:00<00:00, 1462.49it/s]\\n2026-05-16 22:20:36 [INFO] HTTP Requ
…[truncated 6524 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T11:53:43.695242+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "grep \"eval\" /root/runs/importance_margin_vla_compress/libero_full_ft_baseline.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "grep \"eval\" /root/runs/importance_margin_vla_compress/libero_full_ft_baseline.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-18T11:53:43.695423+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "grep \"step=80000\\|step=80050\\|step=85000\\|step=85050\\|step=90000\\|step=90050\\|step=95000\\|step=95050\\|step=99950\" /root/runs/importance_margin_vla_compress/libero_full_ft_baseline.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "grep \"step=80000\\|step=80050\\|step=85000\\|step=85050\\|step=90000\\|step=90050\\|step=95000\\|step=95050\\|step=99950\" /root/runs/importance_margin_vla_compress/libero_full_ft_baseline.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-18T11:53:43.695600+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-16 22:40:40 [INFO] Running evaluation at step 5000...\\n2026-05-16 22:40:45 [INFO]   eval/action_loss: 0.1110\\n2026-05-16 23:00:34 [INFO] Running evaluation at step 10000...\\n2026-05-16 23:00:39 [INFO]   eval/action_loss: 0.1079\\n2026-05-16 23:20:48 [INFO] Running evaluation at step 15000...\\n2026-05-16 23:20:53 [INFO]   eval/action_loss: 0.0864\\n2026-05-16 23:41:20 [INFO] Running evaluation at step 20000...\\n2026-05-16 23:41:26 [INFO]   eval/action_loss: 0.0956\\n2026-05-17 00:02:34 [INFO] Running evaluation at step 25000...\\n2026-05-17 00:02:40 [INFO]   eval/action_loss: 0.0908\\n2026-05-17 00:23:16 [INFO] Running evaluation at step 30000...\\n2026-05-17 00:23:22 [INFO]   eval/action_loss: 0.0825\\n2026-05-17 00:43:53 [INFO] Running evaluation at step 35000...\\n2026-05-17 00:43:59 [INFO]   eval/action_loss: 0.1034\\n2026-05-17 01:04:52 [INFO] Running evaluation at step 40000...\\n2026-05-17 01:04:58 [INFO]   eval/action_loss: 0.0904\\n2026-05-17 01:25:35 [INFO] Running evaluation at step 45000...\\n2026-05-17 01:25:41 [INFO]   eval/action_loss: 0.0579\\n2026-05-17 01:46:21 [INFO] Running evaluation at step 50000...\\n2026-05-17 01:46:27 [INFO]   eval/action_loss: 0.0746\\n2026-05-17 02:06:46 [INFO] Running evaluation at step 55000...\\n2026-05-17 02:06:52 [INFO]   eval/action_loss: 0.0837\\n2026-05-17 02:26:43 [INFO] Running evaluation at step 60000...\\n2026-05-17 02:26:49 [INFO]   eval/action_loss: 0.0959\\n2026-05-17 02:46:23 [INFO] Running evaluation at step 65000...\\n2026-05-17 02:46:29 [INFO]   eval/action_loss: 0.0648\\n2026-05-17 03:07:45 [INFO] Running evaluation at step 70000...\\n2026-05-17 03:07:51 [INFO]   eval/action_loss: 0.0612\\n2026-05-17 03:30:55 [INFO] Running evaluation at step 75000...\\n2026-05-17 03:31:01 [INFO]   eval/action_loss: 0.0607\\n2026-05-17 03:53:52 [INFO] Running evaluation at step 80000...\\n2026-05-17 03:53:57 [INFO]   eval/action_loss: 0.0874\\n2026-05-1
…[truncated 540 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-18T11:53:43.695754+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T11:53:43.695881+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "grep \"step=50000\\|step=55000\\|step=60000\\|step=65000\\|step=70000\\|step=75000\" /root/runs/importance_margin_vla_compress/libero_full_ft_baseline.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "grep \"step=50000\\|step=55000\\|step=60000\\|step=65000\\|step=70000\\|step=75000\" /root/runs/importance_margin_vla_compress/libero_full_ft_baseline.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-18T11:53:43.696005+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-18T11:53:43.696172+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "grep -E \"step=(80000|85000|90000|95000|99950)/\" /root/runs/importance_margin_vla_compress/libero_full_ft_baseline.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "grep -E \"step=(80000|85000|90000|95000|99950)/\" /root/runs/importance_margin_vla_compress/libero_full_ft_baseline.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-18T11:53:43.696320+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-18T11:53:43.696441+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "grep -E \"step=(50000|55000|60000|65000|70000|75000)/\" /root/runs/importance_margin_vla_compress/libero_full_ft_baseline.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "grep -E \"step=(50000|55000|60000|65000|70000|75000)/\" /root/runs/importance_margin_vla_compress/libero_full_ft_baseline.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-18T11:53:43.696562+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-18T11:53:43.696690+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "grep \"step=80000/\" /root/runs/importance_margin_vla_compress/libero_full_ft_baseline.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "grep \"step=80000/\" /root/runs/importance_margin_vla_compress/libero_full_ft_baseline.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-18T11:53:43.696810+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-17 03:53:52 [INFO] step=80000/100000  loss=0.0241  lr=1.20e-05  grad=0.76  sps=4.0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-18T11:53:43.696925+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "grep \"step=85000/\" /root/runs/importance_margin_vla_compress/libero_full_ft_baseline.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "grep \"step=85000/\" /root/runs/importance_margin_vla_compress/libero_full_ft_baseline.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-18T11:53:43.697042+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-17 04:16:46 [INFO] step=85000/100000  loss=0.0158  lr=7.92e-06  grad=0.62  sps=4.0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-18T11:53:43.697236+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "grep \"step=90000/\" /root/runs/importance_margin_vla_compress/libero_full_ft_baseline.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "grep \"step=90000/\" /root/runs/importance_margin_vla_compress/libero_full_ft_baseline.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-18T11:53:43.697401+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-17 04:39:59 [INFO] step=90000/100000  loss=0.0394  lr=4.93e-06  grad=0.61  sps=4.0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-18T11:53:43.697524+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "grep \"step=95000/\" /root/runs/importance_margin_vla_compress/libero_full_ft_baseline.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "grep \"step=95000/\" /root/runs/importance_margin_vla_compress/libero_full_ft_baseline.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-18T11:53:43.697641+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-17 05:03:06 [INFO] step=95000/100000  loss=0.0858  lr=3.11e-06  grad=0.70  sps=3.9\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-18T11:53:43.697754+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "grep \"step=50000/\" /root/runs/importance_margin_vla_compress/libero_full_ft_baseline.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "grep \"step=50000/\" /root/runs/importance_margin_vla_compress/libero_full_ft_baseline.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-18T11:53:43.697870+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-17 01:46:21 [INFO] step=50000/100000  loss=0.0594  lr=5.20e-05  grad=0.89  sps=4.1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-18T11:53:43.697982+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "grep \"step=60000/\" /root/runs/importance_margin_vla_compress/libero_full_ft_baseline.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "grep \"step=60000/\" /root/runs/importance_margin_vla_compress/libero_full_ft_baseline.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-18T11:53:43.698096+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-17 02:26:43 [INFO] step=60000/100000  loss=0.0271  lr=3.68e-05  grad=1.28  sps=4.1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-18T11:53:43.698232+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-33015",
  "command": "grep \"step=70000/\" /root/runs/importance_margin_vla_compress/libero_full_ft_baseline.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-33015",
    "command": "grep \"step=70000/\" /root/runs/importance_margin_vla_compress/libero_full_ft_baseline.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-18T11:53:43.698350+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-17 03:07:45 [INFO] step=70000/100000  loss=0.0675  lr=2.30e-05  grad=1.35  sps=4.1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-18T11:53:43.698543+00:00_

数据已全部收集完毕。

## libero_full_ft baseline 收敛分析

### Train Loss（每步瞬时值，噪声大）

| Step | Train Loss | LR |
|------|-----------|-----|
| 50K | 0.0594 | 5.20e-05 |
| 60K | 0.0271 | 3.68e-05 |
| 70K | 0.0675 | 2.30e-05 |
| 80K | 0.0241 | 1.20e-05 |
| 85K | 0.0158 | 7.92e-06 |
| 90K | 0.0394 | 4.93e-06 |
| 95K | 0.0858 | 3.11e-06 |
| 100K | 0.0408 | 2.50e-06 |

### Eval Loss（每 5K 步评估）

| Step | Eval Loss |
|------|-----------|
| 45K | 0.0579 |
| 50K | 0.0746 |
| 55K | 0.0837 |
| 60K | 0.0959 |
| 65K | 0.0648 |
| 70K | 0.0612 |
| 75K | 0.0607 |
| **80K** | **0.0874** |
| **85K** | **0.0676** |
| **90K** | **0.0591** |
| **95K** | **0.0781** |
| **final** | **0.0781** |

### 判断：**已收敛**

1. **Train loss plateau**: wandb sparkline尾部为 `▂▁▁▂`，已完全走平。80K-100K 区间的瞬时值在 0.02-0.09 波动，无下降趋势。

2. **Eval loss plateau**: 从 step 45K（0.0579）到 100K（0.0781），eval loss 一直在 0.057-0.096 区间内无方向性波动。
   - 60K-80K 均值：~0.074
   - 80K-100K 均值：~0.073
   - 两个窗口几乎一致，无改善。

3. **无 overfitting 迹象**: eval loss 没有上升趋势，只是随机波动（eval set 较小导致方差大）。

4. **LR 已衰减到底**: cosine schedule 从 1e-4 衰减到 2.5e-6，LR 空间已耗尽。

**结论：44.8% baseline 是在充分训练后的结果，不存在因训练不足导致 baseline 偏弱的问题。** 后续实验解读中可以放心引用这个 baseline。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_fullft_loss_convergence_20260518T115159"
}
```

</details>

---
