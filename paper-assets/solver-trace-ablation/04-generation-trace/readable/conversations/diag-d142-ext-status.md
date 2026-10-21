# diag d142 ext status

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 87
- **Recorded user turns:** 0
- **Tool calls:** 43
- **Original source:** `logs/chats/worker_diag_d142-ext-status_20260519T120936.jsonl`
- **Structured JSON:** [`cd0a1a10e952a2f9cf75.json`](../../sessions/cd/cd0a1a10e952a2f9cf75.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

87 recorded events

### Tool call

_source line 1 · 2026-05-19T12:12:32.664814+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__ssh_read_only",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__ssh_read_only",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T12:12:32.665176+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T12:12:32.665351+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'RUNNING'}",
  "project": "solver-trace-ablation",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'RUNNING'}",
    "project": "solver-trace-ablation",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T12:12:32.665536+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"d142-gated-isr-s55\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:55:06.673Z\", \"updated_at\": \"2026-05-19T07:59:44.061Z\", \"hypothesis\": \"Expanding gated ISR (n_components >= 2 gate, beta=0.1) to 6 seeds to verify whether TS-to-PG mode migration is systematic. D142 s52-s54 showed 2/3 PG collapse after gate eliminated TS; additional seeds test if this pattern holds with statistical power for Fisher exact test. Parent: D142.\", \"parent\": \"d142-gated-isr-s52\", \"spec\": {\"command\": \"part of d142 ext pipeline (serial s55→s56→s57)\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"pid\": 322582, \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 55, \"reward_mode\": \"additive_bonus_gated\", \"beta\": 0.1, \"steps\": 500, \"tmux_session\": \"d142ext\", \"log_path\": \"/root/autodl-tmp/d142_ext_pipeline.log\"}}}, \"count\": 1, \"total\": 1, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6278}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T12:12:32.665709+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "ls -la /root/autodl-tmp/outputs/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "ls -la /root/autodl-tmp/outputs/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-19T12:12:32.665853+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "nvidia-smi",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "nvidia-smi",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T12:12:32.665976+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "df -h /root/autodl-tmp/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "df -h /root/autodl-tmp/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T12:12:32.666171+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 9368\\ndrwxr-xr-x 50 root root   8192 May 19 07:56 .\\ndrwxr-xr-x 16 root root   4096 May 19 18:07 ..\\n-rw-r--r--  1 root root   6337 May 15 15:18 bootstrap_ci_results.json\\n-rw-r--r--  1 root root    795 May 16 17:25 classify_h7_sweep_exec_only_s45.json\\n-rw-r--r--  1 root root    780 May 16 17:35 classify_h7_sweep_exec_only_s46.json\\n-rw-r--r--  1 root root   3832 May 15 23:19 d086_missed_classify_h7.json\\ndrwxr-xr-x  2 root root   4096 May 19 02:22 d129_1.7b_isr_b01_s43\\n-rw-r--r--  1 root root 508523 May 18 06:05 d129_1.7b_isr_b01_s43.log\\ndrwxr-xr-x  2 root root   4096 May 19 02:22 d129_1.7b_isr_b01_s44\\n-rw-r--r--  1 root root 521339 May 18 07:34 d129_1.7b_isr_b01_s44.log\\ndrwxr-xr-x  3 root root   4096 May 19 02:22 d129_1.7b_isr_b03_s43\\ndrwxr-xr-x  3 root root   4096 May 19 02:22 d129_1.7b_isr_b03_s44\\ndrwxr-xr-x  2 root root   4096 May 19 02:22 d129_1.7b_random_b01_s43\\n-rw-r--r--  1 root root 528223 May 18 08:50 d129_1.7b_random_b01_s43.log\\ndrwxr-xr-x  2 root root   4096 May 19 02:22 d129_1.7b_random_b01_s44\\ndrwxr-xr-x  2 root root   4096 May 19 02:00 d134_4b_isr_b01_s47\\ndrwxr-xr-x  2 root root   4096 May 18 20:45 d134_4b_isr_b01_s48\\ndrwxr-xr-x  2 root root   4096 May 18 21:46 d134_4b_isr_b01_s49\\ndrwxr-xr-x  2 root root   4096 May 18 22:33 d134_4b_isr_b01_s50\\ndrwxr-xr-x  2 root root   4096 May 18 23:34 d134_4b_isr_b01_s51\\ndrwxr-xr-x  2 root root   4096 May 19 02:00 d134_4b_random_b01_s47\\ndrwxr-xr-x  2 root root   4096 May 19 03:59 d134_4b_random_b01_s48\\ndrwxr-xr-x  2 root root   4096 May 19 05:59 d134_4b_random_b01_s49\\ndrwxr-xr-x  2 root root   4096 May 19 07:56 d134_4b_random_b01_s50\\ndrwxr-xr-x  2 root root   4096 May 19 09:31 d134_4b_random_b01_s51\\n-rw-r--r--  1 root root 230106 May 15 07:52 eval_sta_exp1_isr_b03_s43.json\\ndrwxr-xr-x  2 root root     29 May 15 10:32 eval_sta_exp1_isr_b03_s43_r3\\n-rw-r--r--  1 root root 225558 May 15 10:23 eval_sta_exp1_isr
…[truncated 5321 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-19T12:12:32.666358+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Tue May 19 20:09:53 2026       \\n+-----------------------------------------------------------------------------------------+\\n| NVIDIA-SMI 595.58.03              Driver Version: 595.58.03      CUDA Version: 13.2     |\\n+-----------------------------------------+------------------------+----------------------+\\n| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |\\n| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |\\n|                                         |                        |               MIG M. |\\n|=========================================+========================+======================|\\n|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:A8:00.0 Off |                  Off |\\n| N/A   30C    P8             35W /  600W |       0MiB /  97887MiB |      0%      Default |\\n|                                         |                        |             Disabled |\\n+-----------------------------------------+------------------------+----------------------+\\n\\n+-----------------------------------------------------------------------------------------+\\n| Processes:                                                                              |\\n|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |\\n|        ID   ID                                                               Usage      |\\n|=========================================================================================|\\n|  No running processes found                                                             |\\n+-----------------------------------------------------------------------------------------+\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.62}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T12:12:32.666506+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Filesystem      Size  Used Avail Use% Mounted on\\n/dev/md0        250G   45G  206G  18% /root/autodl-tmp\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T12:12:32.666668+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "tail -100 /root/autodl-tmp/d142_ext_pipeline.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "tail -100 /root/autodl-tmp/d142_ext_pipeline.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T12:12:32.666905+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[70/100] id=folio_755 ... proved  ISR=0.250  gen=2.7s  eval=0.0s\\n[71/100] id=folio_167 ... proved  ISR=1.000  gen=1.3s  eval=0.0s\\n[72/100] id=folio_788 ... proved  ISR=0.200  gen=2.0s  eval=0.0s\\n[73/100] id=folio_20 ... proved  ISR=0.200  gen=1.1s  eval=0.0s\\n[74/100] id=folio_1396 ... proved  ISR=0.200  gen=1.8s  eval=0.0s\\n[75/100] id=folio_564 ... proved  ISR=0.333  gen=0.9s  eval=0.0s\\n[76/100] id=folio_40 ... FAILED  ISR=0.000  gen=1.7s  eval=0.0s\\n[77/100] id=folio_672 ... proved  ISR=0.800  gen=1.5s  eval=0.0s\\n[78/100] id=folio_212 ... proved  ISR=0.800  gen=1.8s  eval=0.0s\\n[79/100] id=folio_58 ... proved  ISR=0.667  gen=1.1s  eval=0.0s\\n[80/100] id=folio_682 ... proved  ISR=0.400  gen=0.9s  eval=0.0s\\n[81/100] id=folio_1135 ... proved  ISR=0.500  gen=2.6s  eval=0.0s\\n[82/100] id=folio_1289 ... proved  ISR=0.600  gen=1.5s  eval=0.0s\\n[83/100] id=folio_1051 ... proved  ISR=0.400  gen=1.6s  eval=0.0s\\n[84/100] id=folio_1381 ... proved  ISR=0.500  gen=1.0s  eval=0.0s\\n[85/100] id=folio_847 ... proved  ISR=0.800  gen=2.1s  eval=0.0s\\n[86/100] id=folio_832 ... proved  ISR=0.600  gen=1.2s  eval=0.0s\\n[87/100] id=folio_732 ... proved  ISR=0.400  gen=1.3s  eval=0.0s\\n[88/100] id=folio_714 ... proved  ISR=0.400  gen=1.4s  eval=0.0s\\n[89/100] id=folio_715 ... proved  ISR=0.200  gen=1.4s  eval=0.0s\\n[90/100] id=folio_990 ... proved  ISR=0.333  gen=1.3s  eval=0.0s\\n[91/100] id=folio_643 ... proved  ISR=0.200  gen=1.8s  eval=0.0s\\n[92/100] id=folio_822 ... proved  ISR=0.600  gen=1.1s  eval=0.0s\\n[93/100] id=folio_1017 ... proved  ISR=0.600  gen=1.7s  eval=0.0s\\n[94/100] id=folio_1415 ... proved  ISR=1.000  gen=1.0s  eval=0.0s\\n[95/100] id=folio_678 ... proved  ISR=1.000  gen=2.3s  eval=0.0s\\n[96/100] id=folio_650 ... proved  ISR=0.200  gen=1.7s  eval=0.0s\\n[97/100] id=folio_93 ... proved  ISR=0.000  gen=1.5s  eval=0.0s\\n[98/100] id=folio_917 ... FAILED  ISR=0.000  gen=1.9s  eval=0.0s\
…[truncated 3824 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T12:12:32.667067+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'd142-gated-isr-s56'}",
  "project": "solver-trace-ablation",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'd142-gated-isr-s56'}",
    "project": "solver-trace-ablation",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T12:12:32.667201+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5516}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T12:12:32.667324+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "find /root/autodl-tmp/ -name \"d142*\" -maxdepth 1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "find /root/autodl-tmp/ -name \"d142*\" -maxdepth 1",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T12:12:32.667452+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/d142_gated_isr_pipeline.sh\\n/root/autodl-tmp/d142_pipeline.log\\n/root/autodl-tmp/d142_gated_isr_s52\\n/root/autodl-tmp/d142_gated_isr_s53\\n/root/autodl-tmp/d142_gated_isr_s54\\n/root/autodl-tmp/d142_gated_isr_pipeline_ext.sh\\n/root/autodl-tmp/d142_ext_pipeline.log\\n/root/autodl-tmp/d142_gated_isr_s55\\n/root/autodl-tmp/d142_gated_isr_s56\\n/root/autodl-tmp/d142_gated_isr_s57\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T12:12:32.667619+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "find /root/autodl-tmp/outputs/ -name \"d142*\" -maxdepth 1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "find /root/autodl-tmp/outputs/ -name \"d142*\" -maxdepth 1",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T12:12:32.667782+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.62}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T12:12:32.667940+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "ls -la /root/autodl-tmp/d142_gated_isr_s55/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "ls -la /root/autodl-tmp/d142_gated_isr_s55/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T12:12:32.668080+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 16336\\ndrwxr-xr-x  2 root root     4096 May 19 16:51 .\\ndrwxr-xr-x 16 root root     4096 May 19 18:07 ..\\n-rw-r--r--  1 root root     1870 May 19 16:49 README.md\\n-rw-r--r--  1 root root      707 May 19 16:49 added_tokens.json\\n-rw-r--r--  1 root root     4168 May 19 16:49 chat_template.jinja\\n-rw-r--r--  1 root root      765 May 19 16:51 classify.json\\n-rw-r--r--  1 root root     2187 May 19 16:51 classify.log\\n-rw-r--r--  1 root root     1535 May 19 16:49 config.json\\n-rw-r--r--  1 root root     8221 May 19 16:51 eval.log\\n-rw-r--r--  1 root root   147357 May 19 16:51 eval_results.json\\n-rw-r--r--  1 root root      188 May 19 16:49 generation_config.json\\n-rw-r--r--  1 root root  1671853 May 19 16:49 merges.txt\\n-rw-r--r--  1 root root   123482 May 19 16:49 reward_log.jsonl\\n-rw-r--r--  1 root root      613 May 19 16:49 special_tokens_map.json\\n-rw-r--r--  1 root root 11422654 May 19 16:49 tokenizer.json\\n-rw-r--r--  1 root root     5459 May 19 16:49 tokenizer_config.json\\n-rw-r--r--  1 root root   508726 May 19 16:49 train.log\\n-rw-r--r--  1 root root  2776833 May 19 16:49 vocab.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T12:12:32.668209+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "ls -la /root/autodl-tmp/d142_gated_isr_s56/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "ls -la /root/autodl-tmp/d142_gated_isr_s56/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-19T12:12:32.668328+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "ls -la /root/autodl-tmp/d142_gated_isr_s57/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "ls -la /root/autodl-tmp/d142_gated_isr_s57/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-19T12:12:32.668461+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 16452\\ndrwxr-xr-x  2 root root     4096 May 19 18:07 .\\ndrwxr-xr-x 16 root root     4096 May 19 18:07 ..\\n-rw-r--r--  1 root root     1870 May 19 17:56 README.md\\n-rw-r--r--  1 root root      707 May 19 17:57 added_tokens.json\\n-rw-r--r--  1 root root     4168 May 19 17:57 chat_template.jinja\\n-rw-r--r--  1 root root      761 May 19 18:07 classify.json\\n-rw-r--r--  1 root root     2424 May 19 18:07 classify.log\\n-rw-r--r--  1 root root     1535 May 19 17:56 config.json\\n-rw-r--r--  1 root root     8257 May 19 18:07 eval.log\\n-rw-r--r--  1 root root   243406 May 19 18:07 eval_results.json\\n-rw-r--r--  1 root root      188 May 19 17:56 generation_config.json\\n-rw-r--r--  1 root root  1671853 May 19 17:57 merges.txt\\n-rw-r--r--  1 root root   128523 May 19 17:56 reward_log.jsonl\\n-rw-r--r--  1 root root      613 May 19 17:57 special_tokens_map.json\\n-rw-r--r--  1 root root 11422654 May 19 17:57 tokenizer.json\\n-rw-r--r--  1 root root     5459 May 19 17:57 tokenizer_config.json\\n-rw-r--r--  1 root root   521937 May 19 17:57 train.log\\n-rw-r--r--  1 root root  2776833 May 19 17:57 vocab.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T12:12:32.668608+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 16412\\ndrwxr-xr-x  2 root root     4096 May 19 19:12 .\\ndrwxr-xr-x 16 root root     4096 May 19 18:07 ..\\n-rw-r--r--  1 root root     1870 May 19 19:09 README.md\\n-rw-r--r--  1 root root      707 May 19 19:09 added_tokens.json\\n-rw-r--r--  1 root root     4168 May 19 19:09 chat_template.jinja\\n-rw-r--r--  1 root root      776 May 19 19:12 classify.json\\n-rw-r--r--  1 root root     2355 May 19 19:12 classify.log\\n-rw-r--r--  1 root root     1535 May 19 19:09 config.json\\n-rw-r--r--  1 root root     8221 May 19 19:12 eval.log\\n-rw-r--r--  1 root root   199021 May 19 19:12 eval_results.json\\n-rw-r--r--  1 root root      188 May 19 19:09 generation_config.json\\n-rw-r--r--  1 root root  1671853 May 19 19:09 merges.txt\\n-rw-r--r--  1 root root   133032 May 19 19:09 reward_log.jsonl\\n-rw-r--r--  1 root root      613 May 19 19:09 special_tokens_map.json\\n-rw-r--r--  1 root root 11422654 May 19 19:09 tokenizer.json\\n-rw-r--r--  1 root root     5459 May 19 19:09 tokenizer_config.json\\n-rw-r--r--  1 root root   525670 May 19 19:09 train.log\\n-rw-r--r--  1 root root  2776833 May 19 19:09 vocab.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T12:12:32.668819+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "cat /root/autodl-tmp/d142_gated_isr_s55/eval_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "cat /root/autodl-tmp/d142_gated_isr_s55/eval_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T12:12:32.669176+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n_problems\\\": 100,\\n    \\\"n_proved\\\": 100,\\n    \\\"prove_rate\\\": 1.0,\\n    \\\"mean_isr\\\": 0.525,\\n    \\\"isr_std\\\": 0.1578,\\n    \\\"median_isr\\\": 0.5,\\n    \\\"isr_pr_ratio\\\": 0.525,\\n    \\\"proved_only_mean_isr\\\": 0.525,\\n    \\\"min_isr\\\": 0.0,\\n    \\\"max_isr\\\": 1.0,\\n    \\\"by_answer_type\\\": {\\n      \\\"false\\\": {\\n        \\\"count\\\": 25,\\n        \\\"proved\\\": 25,\\n        \\\"prove_rate\\\": 1.0,\\n        \\\"mean_isr\\\": 0.5733333333333334\\n      },\\n      \\\"unknown\\\": {\\n        \\\"count\\\": 41,\\n        \\\"proved\\\": 41,\\n        \\\"prove_rate\\\": 1.0,\\n        \\\"mean_isr\\\": 0.532520325203252\\n      },\\n      \\\"true\\\": {\\n        \\\"count\\\": 34,\\n        \\\"proved\\\": 34,\\n        \\\"prove_rate\\\": 1.0,\\n        \\\"mean_isr\\\": 0.4803921568627451\\n      }\\n    },\\n    \\\"elapsed_seconds\\\": 79.4,\\n    \\\"avg_time_per_sample\\\": 0.8,\\n    \\\"solver\\\": \\\"Prover9Solver\\\",\\n    \\\"logic_type\\\": \\\"fol\\\",\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/d142_gated_isr_s55\\\"\\n  },\\n  \\\"results\\\": [\\n    {\\n      \\\"index\\\": 0,\\n      \\\"id\\\": \\\"folio_765\\\",\\n      \\\"context\\\": \\\"Tipped employees are not entitled to be paid the federal minimum wage by their employees. \\\\nIf a person is a white-collar worker, they are entitled to be paid the federal minimum wage by their employees. \\\\nAll lawyers are white-collar workers.\\\\nEvery advocate is a lawyer.\\\\nMary is not a lawyer or a tipped employee.\\\",\\n      \\\"question\\\": \\\"Mary is an advocate.\\\",\\n      \\\"answer\\\": \\\"false\\\",\\n      \\\"formalization\\\": \\\"Premises:\\\\n1. advocate(mary)\\\\nConclusion: advocate(mary)\\\",\\n      \\\"gen_time\\\": 0.87,\\n      \\\"eval_time\\\": 0.02,\\n      \\\"execution_reward\\\": 1.0,\\n      \\\"sta_reward\\\": 0.5
…[truncated 7951 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T12:12:32.669355+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "cat /root/autodl-tmp/d142_gated_isr_s56/eval_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "cat /root/autodl-tmp/d142_gated_isr_s56/eval_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-19T12:12:32.669490+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "cat /root/autodl-tmp/d142_gated_isr_s57/eval_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "cat /root/autodl-tmp/d142_gated_isr_s57/eval_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-19T12:12:32.669794+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n_problems\\\": 100,\\n    \\\"n_proved\\\": 36,\\n    \\\"prove_rate\\\": 0.36,\\n    \\\"mean_isr\\\": 0.2925,\\n    \\\"isr_std\\\": 0.4194,\\n    \\\"median_isr\\\": 0.0,\\n    \\\"isr_pr_ratio\\\": 0.8125,\\n    \\\"proved_only_mean_isr\\\": 0.8125,\\n    \\\"min_isr\\\": 0.0,\\n    \\\"max_isr\\\": 1.0,\\n    \\\"by_answer_type\\\": {\\n      \\\"false\\\": {\\n        \\\"count\\\": 25,\\n        \\\"proved\\\": 11,\\n        \\\"prove_rate\\\": 0.44,\\n        \\\"mean_isr\\\": 0.33\\n      },\\n      \\\"unknown\\\": {\\n        \\\"count\\\": 41,\\n        \\\"proved\\\": 12,\\n        \\\"prove_rate\\\": 0.2926829268292683,\\n        \\\"mean_isr\\\": 0.2451219512195122\\n      },\\n      \\\"true\\\": {\\n        \\\"count\\\": 34,\\n        \\\"proved\\\": 13,\\n        \\\"prove_rate\\\": 0.38235294117647056,\\n        \\\"mean_isr\\\": 0.3220588235294118\\n      }\\n    },\\n    \\\"elapsed_seconds\\\": 605.8,\\n    \\\"avg_time_per_sample\\\": 6.1,\\n    \\\"solver\\\": \\\"Prover9Solver\\\",\\n    \\\"logic_type\\\": \\\"fol\\\",\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/d142_gated_isr_s56\\\"\\n  },\\n  \\\"results\\\": [\\n    {\\n      \\\"index\\\": 0,\\n      \\\"id\\\": \\\"folio_765\\\",\\n      \\\"context\\\": \\\"Tipped employees are not entitled to be paid the federal minimum wage by their employees. \\\\nIf a person is a white-collar worker, they are entitled to be paid the federal minimum wage by their employees. \\\\nAll lawyers are white-collar workers.\\\\nEvery advocate is a lawyer.\\\\nMary is not a lawyer or a tipped employee.\\\",\\n      \\\"question\\\": \\\"Mary is an advocate.\\\",\\n      \\\"answer\\\": \\\"false\\\",\\n      \\\"formalization\\\": \\\"Premises:\\\\n1. ∀x ((Advocate(x) → WhiteCollarWorker(x)) ∧ (WhiteCollarWorker(x) → MinimumWageEntitled(x)))\\\\n2. ∀x (MinimumWageEntitled(x) → PaidFederalMinimumWage(x))\\\\nConc
…[truncated 7482 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T12:12:32.670153+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n_problems\\\": 100,\\n    \\\"n_proved\\\": 88,\\n    \\\"prove_rate\\\": 0.88,\\n    \\\"mean_isr\\\": 0.4497,\\n    \\\"isr_std\\\": 0.3136,\\n    \\\"median_isr\\\": 0.4,\\n    \\\"isr_pr_ratio\\\": 0.511,\\n    \\\"proved_only_mean_isr\\\": 0.511,\\n    \\\"min_isr\\\": 0.0,\\n    \\\"max_isr\\\": 1.0,\\n    \\\"by_answer_type\\\": {\\n      \\\"false\\\": {\\n        \\\"count\\\": 25,\\n        \\\"proved\\\": 18,\\n        \\\"prove_rate\\\": 0.72,\\n        \\\"mean_isr\\\": 0.452\\n      },\\n      \\\"unknown\\\": {\\n        \\\"count\\\": 41,\\n        \\\"proved\\\": 41,\\n        \\\"prove_rate\\\": 1.0,\\n        \\\"mean_isr\\\": 0.49065040650406505\\n      },\\n      \\\"true\\\": {\\n        \\\"count\\\": 34,\\n        \\\"proved\\\": 29,\\n        \\\"prove_rate\\\": 0.8529411764705882,\\n        \\\"mean_isr\\\": 0.3985294117647059\\n      }\\n    },\\n    \\\"elapsed_seconds\\\": 171.9,\\n    \\\"avg_time_per_sample\\\": 1.7,\\n    \\\"solver\\\": \\\"Prover9Solver\\\",\\n    \\\"logic_type\\\": \\\"fol\\\",\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/d142_gated_isr_s57\\\"\\n  },\\n  \\\"results\\\": [\\n    {\\n      \\\"index\\\": 0,\\n      \\\"id\\\": \\\"folio_765\\\",\\n      \\\"context\\\": \\\"Tipped employees are not entitled to be paid the federal minimum wage by their employees. \\\\nIf a person is a white-collar worker, they are entitled to be paid the federal minimum wage by their employees. \\\\nAll lawyers are white-collar workers.\\\\nEvery advocate is a lawyer.\\\\nMary is not a lawyer or a tipped employee.\\\",\\n      \\\"question\\\": \\\"Mary is an advocate.\\\",\\n      \\\"answer\\\": \\\"false\\\",\\n      \\\"formalization\\\": \\\"Premises:\\\\n1. advocate(mary)\\\\n2. ∀x (advocate(x) → lawyer(x))\\\\nConclusion: ∀x (advocate(x) → lawyer(x))\\\",\\n      \\\"gen_time\\\": 1.31,\\n      \\\"eval_time\\\": 0.03,\\n      \\\"e
…[truncated 7855 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-19T12:12:32.670353+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "cat /root/autodl-tmp/d142_gated_isr_s55/classify.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "cat /root/autodl-tmp/d142_gated_isr_s55/classify.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T12:12:32.670512+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"eval_results\\\": {\\n    \\\"n_total\\\": 100,\\n    \\\"n_proved\\\": 100,\\n    \\\"h7a_count\\\": 82,\\n    \\\"h7a_rate\\\": 0.82,\\n    \\\"h7b_count\\\": 0,\\n    \\\"h7b_rate\\\": 0.0,\\n    \\\"h7_total_count\\\": 82,\\n    \\\"h7_total_rate\\\": 0.82,\\n    \\\"h1_strict_count\\\": 0,\\n    \\\"h1_strict_rate\\\": 0.0,\\n    \\\"h8_conjunction_collapse_count\\\": 15,\\n    \\\"h8_conjunction_collapse_rate\\\": 0.15,\\n    \\\"conclusion_in_premise_count\\\": 82,\\n    \\\"conclusion_in_premise_rate\\\": 0.82,\\n    \\\"h7_relaxed_count\\\": 79,\\n    \\\"h7_relaxed_rate\\\": 0.79,\\n    \\\"single_premise_count\\\": 82,\\n    \\\"single_premise_rate\\\": 0.82,\\n    \\\"isr_1_count\\\": 4,\\n    \\\"isr_1_rate\\\": 0.04,\\n    \\\"content_independent_count\\\": 0,\\n    \\\"content_independent_rate\\\": 0.0,\\n    \\\"genuine_count\\\": 3,\\n    \\\"genuine_rate\\\": 0.03,\\n    \\\"h7_strict_count\\\": 82,\\n    \\\"h7_strict_rate\\\": 0.82\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-19T12:12:32.670648+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "cat /root/autodl-tmp/d142_gated_isr_s56/classify.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "cat /root/autodl-tmp/d142_gated_isr_s56/classify.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T12:12:32.670817+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"eval_results\\\": {\\n    \\\"n_total\\\": 100,\\n    \\\"n_proved\\\": 36,\\n    \\\"h7a_count\\\": 0,\\n    \\\"h7a_rate\\\": 0.0,\\n    \\\"h7b_count\\\": 0,\\n    \\\"h7b_rate\\\": 0.0,\\n    \\\"h7_total_count\\\": 0,\\n    \\\"h7_total_rate\\\": 0.0,\\n    \\\"h1_strict_count\\\": 0,\\n    \\\"h1_strict_rate\\\": 0.0,\\n    \\\"h8_conjunction_collapse_count\\\": 30,\\n    \\\"h8_conjunction_collapse_rate\\\": 0.8333,\\n    \\\"conclusion_in_premise_count\\\": 0,\\n    \\\"conclusion_in_premise_rate\\\": 0.0,\\n    \\\"h7_relaxed_count\\\": 0,\\n    \\\"h7_relaxed_rate\\\": 0.0,\\n    \\\"single_premise_count\\\": 0,\\n    \\\"single_premise_rate\\\": 0.0,\\n    \\\"isr_1_count\\\": 19,\\n    \\\"isr_1_rate\\\": 0.5278,\\n    \\\"content_independent_count\\\": 27,\\n    \\\"content_independent_rate\\\": 0.75,\\n    \\\"genuine_count\\\": 6,\\n    \\\"genuine_rate\\\": 0.1667,\\n    \\\"h7_strict_count\\\": 0,\\n    \\\"h7_strict_rate\\\": 0.0\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-19T12:12:32.670957+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "cat /root/autodl-tmp/d142_gated_isr_s57/classify.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "cat /root/autodl-tmp/d142_gated_isr_s57/classify.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T12:12:32.671107+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"eval_results\\\": {\\n    \\\"n_total\\\": 100,\\n    \\\"n_proved\\\": 88,\\n    \\\"h7a_count\\\": 1,\\n    \\\"h7a_rate\\\": 0.0114,\\n    \\\"h7b_count\\\": 0,\\n    \\\"h7b_rate\\\": 0.0,\\n    \\\"h7_total_count\\\": 1,\\n    \\\"h7_total_rate\\\": 0.0114,\\n    \\\"h1_strict_count\\\": 18,\\n    \\\"h1_strict_rate\\\": 0.2045,\\n    \\\"h8_conjunction_collapse_count\\\": 13,\\n    \\\"h8_conjunction_collapse_rate\\\": 0.1477,\\n    \\\"conclusion_in_premise_count\\\": 19,\\n    \\\"conclusion_in_premise_rate\\\": 0.2159,\\n    \\\"h7_relaxed_count\\\": 0,\\n    \\\"h7_relaxed_rate\\\": 0.0,\\n    \\\"single_premise_count\\\": 0,\\n    \\\"single_premise_rate\\\": 0.0,\\n    \\\"isr_1_count\\\": 8,\\n    \\\"isr_1_rate\\\": 0.0909,\\n    \\\"content_independent_count\\\": 0,\\n    \\\"content_independent_rate\\\": 0.0,\\n    \\\"genuine_count\\\": 56,\\n    \\\"genuine_rate\\\": 0.6364,\\n    \\\"h7_strict_count\\\": 1,\\n    \\\"h7_strict_rate\\\": 0.0114\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-19T12:12:32.671238+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "tail -30 /root/autodl-tmp/d142_gated_isr_s55/train.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "tail -30 /root/autodl-tmp/d142_gated_isr_s55/train.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T12:12:32.671421+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\r                                                 \\r\\r 98%|█████████▊| 488/500 [51:39<00:36,  3.01s/it]\\r 98%|█████████▊| 489/500 [51:44<00:38,  3.52s/it]{'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 2.5999999999999998e-08, 'num_tokens': 1229239.0, 'completions/mean_length': 49.75, 'completions/min_length': 41.5, 'completions/max_length': 54.0, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 49.75, 'completions/min_terminated_length': 41.5, 'completions/max_terminated_length': 54.0, 'rewards/reward_fn/mean': 1.0333333611488342, 'rewards/reward_fn/std': 0.0, 'reward': 1.0333333611488342, 'reward_std': 0.0, 'frac_reward_zero_std': 1.0, 'entropy': 0.051018210127949715, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'step_time': 3.5018995441496372, 'epoch': 1.95}\\n[REWARD_LOG] step=489 reward=0.9250 prove_rate=0.875 isr=0.500 parse_rate=1.000 beta_t=0.1000 gate_pass=1.000\\n\\r                                                 \\r\\r 98%|█████████▊| 489/500 [51:44<00:38,  3.52s/it]\\r 98%|█████████▊| 490/500 [51:48<00:37,  3.80s/it]{'loss': 0.0533, 'grad_norm': 35.716339111328125, 'learning_rate': 2.4e-08, 'num_tokens': 1231549.0, 'completions/mean_length': 64.75, 'completions/min_length': 57.5, 'completions/max_length': 71.0, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 64.75, 'completions/min_terminated_length': 57.5, 'completions/max_terminated_length': 71.0, 'rewards/reward_fn/mean': 0.925000011920929, 'rewards/reward_fn/std': 0.2768729021772742, 'reward': 0.925000011920929, 'reward_std': 0.2768729142844677, 'frac_reward_zero_std': 0.0, 'entropy': 0.06267471052706242, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'step_time': 4.373208342120051, 'epoch': 1.96}\\n[RE
…[truncated 6305 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-19T12:12:32.671617+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "tail -30 /root/autodl-tmp/d142_gated_isr_s56/train.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "tail -30 /root/autodl-tmp/d142_gated_isr_s56/train.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-19T12:12:32.671772+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "tail -30 /root/autodl-tmp/d142_gated_isr_s57/train.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "tail -30 /root/autodl-tmp/d142_gated_isr_s57/train.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-19T12:12:32.671960+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\r                                                   \\r\\r 98%|█████████▊| 488/500 [1:03:39<01:36,  8.08s/it]\\r 98%|█████████▊| 489/500 [1:03:44<01:18,  7.15s/it]{'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 2.5999999999999998e-08, 'num_tokens': 1290424.0, 'completions/mean_length': 84.0, 'completions/min_length': 83.0, 'completions/max_length': 85.0, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 84.0, 'completions/min_terminated_length': 83.0, 'completions/max_terminated_length': 85.0, 'rewards/reward_fn/mean': 1.100000023841858, 'rewards/reward_fn/std': 0.0, 'reward': 1.100000023841858, 'reward_std': 0.0, 'frac_reward_zero_std': 1.0, 'entropy': 0.008625882444903255, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'step_time': 5.090344392694533, 'epoch': 1.95}\\n[REWARD_LOG] step=489 reward=1.1000 prove_rate=1.000 isr=1.000 parse_rate=1.000 beta_t=0.1000 gate_pass=1.000\\n\\r                                                   \\r\\r 98%|█████████▊| 489/500 [1:03:44<01:18,  7.15s/it]\\r 98%|█████████▊| 490/500 [1:03:52<01:14,  7.43s/it]{'loss': 0.0, 'grad_norm': 0.0, 'learning_rate': 2.4e-08, 'num_tokens': 1292782.0, 'completions/mean_length': 68.25, 'completions/min_length': 64.0, 'completions/max_length': 75.0, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 68.25, 'completions/min_terminated_length': 64.0, 'completions/max_terminated_length': 75.0, 'rewards/reward_fn/mean': 1.100000023841858, 'rewards/reward_fn/std': 0.0, 'reward': 1.100000023841858, 'reward_std': 0.0, 'frac_reward_zero_std': 1.0, 'entropy': 0.04458221001550555, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'step_time': 4.6598632466048, 'epoch': 1.96}\\n[REWARD_LOG] step=490 reward=1.0900 prove_rate
…[truncated 6301 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-19T12:12:32.672170+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\r                                                   \\r\\r 98%|█████████▊| 488/500 [1:00:14<00:53,  4.49s/it]\\r 98%|█████████▊| 489/500 [1:00:20<00:54,  4.91s/it]{'loss': -0.2104, 'grad_norm': 34.55354309082031, 'learning_rate': 2.5999999999999998e-08, 'num_tokens': 1276380.0, 'completions/mean_length': 57.125, 'completions/min_length': 47.5, 'completions/max_length': 66.0, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 57.125, 'completions/min_terminated_length': 47.5, 'completions/max_terminated_length': 66.0, 'rewards/reward_fn/mean': 0.6624999642372131, 'rewards/reward_fn/std': 0.5709956288337708, 'reward': 0.6624999642372131, 'reward_std': 0.5709955990314484, 'frac_reward_zero_std': 0.0, 'entropy': 0.060875057242810726, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_mean': 0.0, 'step_time': 4.175839071162045, 'epoch': 1.95}\\n[REWARD_LOG] step=489 reward=0.6750 prove_rate=0.625 isr=0.500 parse_rate=1.000 beta_t=0.1000 gate_pass=1.000\\n\\r                                                   \\r\\r 98%|█████████▊| 489/500 [1:00:20<00:54,  4.91s/it]\\r 98%|█████████▊| 490/500 [1:00:24<00:45,  4.54s/it]{'loss': 0.11, 'grad_norm': 15.185694694519043, 'learning_rate': 2.4e-08, 'num_tokens': 1278800.0, 'completions/mean_length': 89.5, 'completions/min_length': 78.5, 'completions/max_length': 93.5, 'completions/clipped_ratio': 0.0, 'completions/mean_terminated_length': 89.5, 'completions/min_terminated_length': 78.5, 'completions/max_terminated_length': 93.5, 'rewards/reward_fn/mean': 0.6750000268220901, 'rewards/reward_fn/std': 0.27000001072883606, 'reward': 0.6750000268220901, 'reward_std': 0.27000001072883606, 'frac_reward_zero_std': 0.5, 'entropy': 0.015237221959978342, 'clip_ratio/low_mean': 0.0, 'clip_ratio/low_min': 0.0, 'clip_ratio/high_mean': 0.0, 'clip_ratio/high_max': 0.0, 'clip_ratio/region_me
…[truncated 6299 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-19T12:12:32.672355+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'd142-gated-isr-s57'}",
  "project": "solver-trace-ablation",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'd142-gated-isr-s57'}",
    "project": "solver-trace-ablation",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-19T12:12:32.672489+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'd142-gated-isr-s52'}",
  "project": "solver-trace-ablation",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'd142-gated-isr-s52'}",
    "project": "solver-trace-ablation",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-19T12:12:32.672615+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5242}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-19T12:12:32.672759+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5232}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-19T12:12:32.672897+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "solver-trace-ablation",
  "fields": "['status', 'conclusion']",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "solver-trace-ablation",
    "fields": "['status', 'conclusion']",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-19T12:12:32.673099+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"d144-llama-exec-s42\": {\"status\": \"PREPARING\"}, \"d143-pw-extended-s42\": {\"status\": \"PREPARING\"}, \"d143-pw-sft-s42\": {\"status\": \"PREPARING\"}, \"d143-pw-random-s42\": {\"status\": \"PREPARING\"}, \"d143-pw-isr-s44\": {\"status\": \"PREPARING\"}, \"d143-pw-isr-s43\": {\"status\": \"PREPARING\"}, \"d143-pw-isr-s42\": {\"status\": \"PREPARING\"}, \"d143-pw-exec-s44\": {\"status\": \"PREPARING\"}, \"d143-pw-exec-s43\": {\"status\": \"PREPARING\"}, \"d143-pw-exec-s42\": {\"status\": \"PREPARING\"}, \"d142-gated-isr-s54\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d142-gated-isr-s53\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"d142-gated-isr-s52\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"d142-gated-isr-s55\": {\"status\": \"RUNNING\"}, \"d142-gated-isr-s57\": {\"status\": \"QUEUED\"}, \"d142-gated-isr-s56\": {\"status\": \"QUEUED\"}, \"d134-4b-random-b01-s51\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d134-4b-random-b01-s50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d134-4b-random-b01-s49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d134-4b-random-b01-s48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d134-4b-random-b01-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d134-4b-isr-b01-s51\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d134-4b-isr-b01-s50\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d134-4b-isr-b01-s49\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d134-4b-isr-b01-s48\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d134-4b-isr-b01-s47\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"w2-qwen3-1.7b-isr-b03\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d129-1_7b-isr-b03-s44\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d129-1_7b-isr-b03-s43\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d129
…[truncated 1780 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-19T12:12:32.673277+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'DONE', 'exp_id': 'd142-gated-isr-s54'}",
  "project": "solver-trace-ablation",
  "fields": "['*']",
  "limit": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'DONE', 'exp_id': 'd142-gated-isr-s54'}",
    "project": "solver-trace-ablation",
    "fields": "['*']",
    "limit": "1"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-19T12:12:32.673413+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.514}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-19T12:12:32.673576+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "d142-gated-isr-s55",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/d142_gated_isr_s55",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "d142-gated-isr-s55",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/d142_gated_isr_s55",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-19T12:12:32.673754+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"d142-gated-isr-s55\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:55:06.673Z\", \"updated_at\": \"2026-05-19T12:11:04.970Z\", \"hypothesis\": \"Expanding gated ISR (n_components >= 2 gate, beta=0.1) to 6 seeds to verify whether TS-to-PG mode migration is systematic. D142 s52-s54 showed 2/3 PG collapse after gate eliminated TS; additional seeds test if this pattern holds with statistical power for Fisher exact test. Parent: D142.\", \"parent\": \"d142-gated-isr-s52\", \"spec\": {\"command\": \"part of d142 ext pipeline (serial s55→s56→s57)\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"pid\": 322582, \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 55, \"reward_mode\": \"additive_bonus_gated\", \"beta\": 0.1, \"steps\": 500, \"tmux_session\": \"d142ext\", \"log_path\": \"/root/autodl-tmp/d142_ext_pipeline.log\"}, \"checkpoint_path\": \"/root/autodl-tmp/d142_gated_isr_s55\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8786}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-19T12:12:32.673911+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "d142-gated-isr-s55",
  "field": "log_path",
  "value": "/root/autodl-tmp/d142_gated_isr_s55/train.log",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "d142-gated-isr-s55",
    "field": "log_path",
    "value": "/root/autodl-tmp/d142_gated_isr_s55/train.log",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-19T12:12:32.674070+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"d142-gated-isr-s55\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:55:06.673Z\", \"updated_at\": \"2026-05-19T12:11:06.041Z\", \"hypothesis\": \"Expanding gated ISR (n_components >= 2 gate, beta=0.1) to 6 seeds to verify whether TS-to-PG mode migration is systematic. D142 s52-s54 showed 2/3 PG collapse after gate eliminated TS; additional seeds test if this pattern holds with statistical power for Fisher exact test. Parent: D142.\", \"parent\": \"d142-gated-isr-s52\", \"spec\": {\"command\": \"part of d142 ext pipeline (serial s55→s56→s57)\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"pid\": 322582, \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 55, \"reward_mode\": \"additive_bonus_gated\", \"beta\": 0.1, \"steps\": 500, \"tmux_session\": \"d142ext\", \"log_path\": \"/root/autodl-tmp/d142_ext_pipeline.log\"}, \"checkpoint_path\": \"/root/autodl-tmp/d142_gated_isr_s55\", \"log_path\": \"/root/autodl-tmp/d142_gated_isr_s55/train.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9757}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-19T12:12:32.674220+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "d142-gated-isr-s55",
  "field": "metrics",
  "value": "{'prove_rate': 1, 'mean_isr': 0.525, 'isr_std': 0.158, 'median_isr': 0.5, 'proved_only_isr': 0.525, 'genuine_count': 3, 'genuine_rate': 0.03, 'h7_count': 82, 'h7_rate': 0.82, 'h1_count': 0, 'h1_rate': 0, 'h8_count': 15, 'h8_rate': 0.15, 'train_final_prove_rate': 0.586, 'train_final_mean_isr': 0.327, 'train_loss': 0.0128}",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "d142-gated-isr-s55",
    "field": "metrics",
    "value": "{'prove_rate': 1, 'mean_isr': 0.525, 'isr_std': 0.158, 'median_isr': 0.5, 'proved_only_isr': 0.525, 'genuine_count': 3, 'genuine_rate': 0.03, 'h7_count': 82, 'h7_rate': 0.82, 'h1_count': 0, 'h1_rate': 0, 'h8_count': 15, 'h8_rate': 0.15, 'train_final_prove_rate': 0.586, 'train_final_mean_isr': 0.327, 'train_loss': 0.0128}",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-19T12:12:32.674401+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"d142-gated-isr-s55\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:55:06.673Z\", \"updated_at\": \"2026-05-19T12:11:11.929Z\", \"hypothesis\": \"Expanding gated ISR (n_components >= 2 gate, beta=0.1) to 6 seeds to verify whether TS-to-PG mode migration is systematic. D142 s52-s54 showed 2/3 PG collapse after gate eliminated TS; additional seeds test if this pattern holds with statistical power for Fisher exact test. Parent: D142.\", \"parent\": \"d142-gated-isr-s52\", \"spec\": {\"command\": \"part of d142 ext pipeline (serial s55→s56→s57)\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"pid\": 322582, \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 55, \"reward_mode\": \"additive_bonus_gated\", \"beta\": 0.1, \"steps\": 500, \"tmux_session\": \"d142ext\", \"log_path\": \"/root/autodl-tmp/d142_ext_pipeline.log\"}, \"checkpoint_path\": \"/root/autodl-tmp/d142_gated_isr_s55\", \"log_path\": \"/root/autodl-tmp/d142_gated_isr_s55/train.log\", \"metrics\": {\"prove_rate\": 1, \"mean_isr\": 0.525, \"isr_std\": 0.158, \"median_isr\": 0.5, \"proved_only_isr\": 0.525, \"genuine_count\": 3, \"genuine_rate\": 0.03, \"h7_count\": 82, \"h7_rate\": 0.82, \"h1_count\": 0, \"h1_rate\": 0, \"h8_count\": 15, \"h8_rate\": 0.15, \"train_final_prove_rate\": 0.586, \"train_final_mean_isr\": 0.327, \"train_loss\": 0.0128}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8785}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-19T12:12:32.674553+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "d142-gated-isr-s55",
  "field": "conclusion",
  "value": "success",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "d142-gated-isr-s55",
    "field": "conclusion",
    "value": "success",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-19T12:12:32.674736+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"d142-gated-isr-s55\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:55:06.673Z\", \"updated_at\": \"2026-05-19T12:11:16.096Z\", \"hypothesis\": \"Expanding gated ISR (n_components >= 2 gate, beta=0.1) to 6 seeds to verify whether TS-to-PG mode migration is systematic. D142 s52-s54 showed 2/3 PG collapse after gate eliminated TS; additional seeds test if this pattern holds with statistical power for Fisher exact test. Parent: D142.\", \"parent\": \"d142-gated-isr-s52\", \"spec\": {\"command\": \"part of d142 ext pipeline (serial s55→s56→s57)\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"pid\": 322582, \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 55, \"reward_mode\": \"additive_bonus_gated\", \"beta\": 0.1, \"steps\": 500, \"tmux_session\": \"d142ext\", \"log_path\": \"/root/autodl-tmp/d142_ext_pipeline.log\"}, \"checkpoint_path\": \"/root/autodl-tmp/d142_gated_isr_s55\", \"log_path\": \"/root/autodl-tmp/d142_gated_isr_s55/train.log\", \"metrics\": {\"prove_rate\": 1, \"mean_isr\": 0.525, \"isr_std\": 0.158, \"median_isr\": 0.5, \"proved_only_isr\": 0.525, \"genuine_count\": 3, \"genuine_rate\": 0.03, \"h7_count\": 82, \"h7_rate\": 0.82, \"h1_count\": 0, \"h1_rate\": 0, \"h8_count\": 15, \"h8_rate\": 0.15, \"train_final_prove_rate\": 0.586, \"train_final_mean_isr\": 0.327, \"train_loss\": 0.0128}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1052}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-19T12:12:32.674897+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "d142-gated-isr-s55",
  "field": "status",
  "value": "DONE",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "d142-gated-isr-s55",
    "field": "status",
    "value": "DONE",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-19T12:12:32.675088+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"d142-gated-isr-s55\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:55:06.673Z\", \"updated_at\": \"2026-05-19T12:11:20.350Z\", \"hypothesis\": \"Expanding gated ISR (n_components >= 2 gate, beta=0.1) to 6 seeds to verify whether TS-to-PG mode migration is systematic. D142 s52-s54 showed 2/3 PG collapse after gate eliminated TS; additional seeds test if this pattern holds with statistical power for Fisher exact test. Parent: D142.\", \"parent\": \"d142-gated-isr-s52\", \"spec\": {\"command\": \"part of d142 ext pipeline (serial s55→s56→s57)\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"pid\": 322582, \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 55, \"reward_mode\": \"additive_bonus_gated\", \"beta\": 0.1, \"steps\": 500, \"tmux_session\": \"d142ext\", \"log_path\": \"/root/autodl-tmp/d142_ext_pipeline.log\"}, \"checkpoint_path\": \"/root/autodl-tmp/d142_gated_isr_s55\", \"log_path\": \"/root/autodl-tmp/d142_gated_isr_s55/train.log\", \"metrics\": {\"prove_rate\": 1, \"mean_isr\": 0.525, \"isr_std\": 0.158, \"median_isr\": 0.5, \"proved_only_isr\": 0.525, \"genuine_count\": 3, \"genuine_rate\": 0.03, \"h7_count\": 82, \"h7_rate\": 0.82, \"h1_count\": 0, \"h1_rate\": 0, \"h8_count\": 15, \"h8_rate\": 0.15, \"train_final_prove_rate\": 0.586, \"train_final_mean_isr\": 0.327, \"train_loss\": 0.0128}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T12:11:20.350Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.8242}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-19T12:12:32.675265+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "d142-gated-isr-s56",
  "field": "status",
  "value": "RUNNING",
  "project": "solver-trace-ablation",
  "spec": "{'command': 'part of d142 ext pipeline (serial s55→s56→s57)', 'server': 'westd-39279', 'gpu': 'cuda:0', 'data_path': '/root/solver-trace-ablation/data/train_500_seed42.jsonl', 'data_count': 500, 'model_name': 'Qwen/Qwen3-4B', 'seed': 56, 'reward_mode': 'additive_bonus_gated', 'beta': 0.1, 'steps': 500}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "d142-gated-isr-s56",
    "field": "status",
    "value": "RUNNING",
    "project": "solver-trace-ablation",
    "spec": "{'command': 'part of d142 ext pipeline (serial s55→s56→s57)', 'server': 'westd-39279', 'gpu': 'cuda:0', 'data_path': '/root/solver-trace-ablation/data/train_500_seed42.jsonl', 'data_count': 500, 'model_name': 'Qwen/Qwen3-4B', 'seed': 56, 'reward_mode': 'additive_bonus_gated', 'beta': 0.1, 'steps': 500}"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-19T12:12:32.675418+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Eval experiment requires additional spec fields: ['checkpoint_source', 'eval_data']. Eval spec must include: ['checkpoint_source', 'eval_data']\", \"metadata\": {\"elapsed_seconds\": 0.6225}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-19T12:12:32.675584+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "d142-gated-isr-s56",
  "field": "status",
  "value": "RUNNING",
  "project": "solver-trace-ablation",
  "spec": "{'command': 'part of d142 ext pipeline (serial s55→s56→s57)', 'server': 'westd-39279', 'gpu': 'cuda:0', 'data_path': '/root/solver-trace-ablation/data/train_500_seed42.jsonl', 'data_count': 500, 'model_name': 'Qwen/Qwen3-4B', 'seed': 56, 'reward_mode': 'additive_bonus_gated', 'beta': 0.1, 'steps': 500, 'checkpoint_source': 'trained from base', 'eval_data': 'data/proofwriter_fol_100.jsonl'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "d142-gated-isr-s56",
    "field": "status",
    "value": "RUNNING",
    "project": "solver-trace-ablation",
    "spec": "{'command': 'part of d142 ext pipeline (serial s55→s56→s57)', 'server': 'westd-39279', 'gpu': 'cuda:0', 'data_path': '/root/solver-trace-ablation/data/train_500_seed42.jsonl', 'data_count': 500, 'model_name': 'Qwen/Qwen3-4B', 'seed': 56, 'reward_mode': 'additive_bonus_gated', 'beta': 0.1, 'steps': 500, 'checkpoint_source': 'trained from base', 'eval_data': 'data/proofwriter_fol_100.jsonl'}"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-19T12:12:32.675789+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"d142-gated-isr-s56\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:55:09.394Z\", \"updated_at\": \"2026-05-19T12:11:33.193Z\", \"hypothesis\": \"Expanding gated ISR (n_components >= 2 gate, beta=0.1) to 6 seeds to verify whether TS-to-PG mode migration is systematic. D142 s52-s54 showed 2/3 PG collapse after gate eliminated TS; additional seeds test if this pattern holds with statistical power for Fisher exact test. Parent: D142.\", \"parent\": \"d142-gated-isr-s52\", \"spec\": {\"command\": \"part of d142 ext pipeline (serial s55→s56→s57)\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 56, \"reward_mode\": \"additive_bonus_gated\", \"beta\": 0.1, \"steps\": 500, \"checkpoint_source\": \"trained from base\", \"eval_data\": \"data/proofwriter_fol_100.jsonl\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.7683}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-19T12:12:32.675937+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "d142-gated-isr-s56",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/d142_gated_isr_s56",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "d142-gated-isr-s56",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/d142_gated_isr_s56",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-19T12:12:32.676060+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "d142-gated-isr-s56",
  "field": "log_path",
  "value": "/root/autodl-tmp/d142_gated_isr_s56/train.log",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "d142-gated-isr-s56",
    "field": "log_path",
    "value": "/root/autodl-tmp/d142_gated_isr_s56/train.log",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-19T12:12:32.676208+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"d142-gated-isr-s56\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:55:09.394Z\", \"updated_at\": \"2026-05-19T12:11:38.828Z\", \"hypothesis\": \"Expanding gated ISR (n_components >= 2 gate, beta=0.1) to 6 seeds to verify whether TS-to-PG mode migration is systematic. D142 s52-s54 showed 2/3 PG collapse after gate eliminated TS; additional seeds test if this pattern holds with statistical power for Fisher exact test. Parent: D142.\", \"parent\": \"d142-gated-isr-s52\", \"spec\": {\"command\": \"part of d142 ext pipeline (serial s55→s56→s57)\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 56, \"reward_mode\": \"additive_bonus_gated\", \"beta\": 0.1, \"steps\": 500, \"checkpoint_source\": \"trained from base\", \"eval_data\": \"data/proofwriter_fol_100.jsonl\"}, \"checkpoint_path\": \"/root/autodl-tmp/d142_gated_isr_s56\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8886}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-19T12:12:32.676375+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"d142-gated-isr-s56\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:55:09.394Z\", \"updated_at\": \"2026-05-19T12:11:39.697Z\", \"hypothesis\": \"Expanding gated ISR (n_components >= 2 gate, beta=0.1) to 6 seeds to verify whether TS-to-PG mode migration is systematic. D142 s52-s54 showed 2/3 PG collapse after gate eliminated TS; additional seeds test if this pattern holds with statistical power for Fisher exact test. Parent: D142.\", \"parent\": \"d142-gated-isr-s52\", \"spec\": {\"command\": \"part of d142 ext pipeline (serial s55→s56→s57)\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 56, \"reward_mode\": \"additive_bonus_gated\", \"beta\": 0.1, \"steps\": 500, \"checkpoint_source\": \"trained from base\", \"eval_data\": \"data/proofwriter_fol_100.jsonl\"}, \"checkpoint_path\": \"/root/autodl-tmp/d142_gated_isr_s56\", \"log_path\": \"/root/autodl-tmp/d142_gated_isr_s56/train.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8383}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-19T12:12:32.676522+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "d142-gated-isr-s56",
  "field": "metrics",
  "value": "{'prove_rate': 0.36, 'mean_isr': 0.293, 'isr_std': 0.419, 'median_isr': 0, 'proved_only_isr': 0.813, 'genuine_count': 6, 'genuine_rate': 0.167, 'h7_count': 0, 'h7_rate': 0, 'h1_count': 0, 'h1_rate': 0, 'h8_count': 30, 'h8_rate': 0.833, 'content_independent_count': 27, 'content_independent_rate': 0.75, 'train_final_prove_rate': 0.742, 'train_final_mean_isr': 0.618, 'train_loss': 0.031}",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "d142-gated-isr-s56",
    "field": "metrics",
    "value": "{'prove_rate': 0.36, 'mean_isr': 0.293, 'isr_std': 0.419, 'median_isr': 0, 'proved_only_isr': 0.813, 'genuine_count': 6, 'genuine_rate': 0.167, 'h7_count': 0, 'h7_rate': 0, 'h1_count': 0, 'h1_rate': 0, 'h8_count': 30, 'h8_rate': 0.833, 'content_independent_count': 27, 'content_independent_rate': 0.75, 'train_final_prove_rate': 0.742, 'train_final_mean_isr': 0.618, 'train_loss': 0.031}",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-19T12:12:32.676663+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "d142-gated-isr-s56",
  "field": "conclusion",
  "value": "success",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "d142-gated-isr-s56",
    "field": "conclusion",
    "value": "success",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-19T12:12:32.676854+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"d142-gated-isr-s56\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:55:09.394Z\", \"updated_at\": \"2026-05-19T12:11:45.780Z\", \"hypothesis\": \"Expanding gated ISR (n_components >= 2 gate, beta=0.1) to 6 seeds to verify whether TS-to-PG mode migration is systematic. D142 s52-s54 showed 2/3 PG collapse after gate eliminated TS; additional seeds test if this pattern holds with statistical power for Fisher exact test. Parent: D142.\", \"parent\": \"d142-gated-isr-s52\", \"spec\": {\"command\": \"part of d142 ext pipeline (serial s55→s56→s57)\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 56, \"reward_mode\": \"additive_bonus_gated\", \"beta\": 0.1, \"steps\": 500, \"checkpoint_source\": \"trained from base\", \"eval_data\": \"data/proofwriter_fol_100.jsonl\"}, \"checkpoint_path\": \"/root/autodl-tmp/d142_gated_isr_s56\", \"log_path\": \"/root/autodl-tmp/d142_gated_isr_s56/train.log\", \"metrics\": {\"prove_rate\": 0.36, \"mean_isr\": 0.293, \"isr_std\": 0.419, \"median_isr\": 0, \"proved_only_isr\": 0.813, \"genuine_count\": 6, \"genuine_rate\": 0.167, \"h7_count\": 0, \"h7_rate\": 0, \"h1_count\": 0, \"h1_rate\": 0, \"h8_count\": 30, \"h8_rate\": 0.833, \"content_independent_count\": 27, \"content_independent_rate\": 0.75, \"train_final_prove_rate\": 0.742, \"train_final_mean_isr\": 0.618, \"train_loss\": 0.031}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9127}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-19T12:12:32.677038+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"d142-gated-isr-s56\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:55:09.394Z\", \"updated_at\": \"2026-05-19T12:11:46.879Z\", \"hypothesis\": \"Expanding gated ISR (n_components >= 2 gate, beta=0.1) to 6 seeds to verify whether TS-to-PG mode migration is systematic. D142 s52-s54 showed 2/3 PG collapse after gate eliminated TS; additional seeds test if this pattern holds with statistical power for Fisher exact test. Parent: D142.\", \"parent\": \"d142-gated-isr-s52\", \"spec\": {\"command\": \"part of d142 ext pipeline (serial s55→s56→s57)\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 56, \"reward_mode\": \"additive_bonus_gated\", \"beta\": 0.1, \"steps\": 500, \"checkpoint_source\": \"trained from base\", \"eval_data\": \"data/proofwriter_fol_100.jsonl\"}, \"checkpoint_path\": \"/root/autodl-tmp/d142_gated_isr_s56\", \"log_path\": \"/root/autodl-tmp/d142_gated_isr_s56/train.log\", \"metrics\": {\"prove_rate\": 0.36, \"mean_isr\": 0.293, \"isr_std\": 0.419, \"median_isr\": 0, \"proved_only_isr\": 0.813, \"genuine_count\": 6, \"genuine_rate\": 0.167, \"h7_count\": 0, \"h7_rate\": 0, \"h1_count\": 0, \"h1_rate\": 0, \"h8_count\": 30, \"h8_rate\": 0.833, \"content_independent_count\": 27, \"content_independent_rate\": 0.75, \"train_final_prove_rate\": 0.742, \"train_final_mean_isr\": 0.618, \"train_loss\": 0.031}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1044}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-19T12:12:32.677182+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "d142-gated-isr-s56",
  "field": "status",
  "value": "DONE",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "d142-gated-isr-s56",
    "field": "status",
    "value": "DONE",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-19T12:12:32.677361+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"d142-gated-isr-s56\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:55:09.394Z\", \"updated_at\": \"2026-05-19T12:11:51.474Z\", \"hypothesis\": \"Expanding gated ISR (n_components >= 2 gate, beta=0.1) to 6 seeds to verify whether TS-to-PG mode migration is systematic. D142 s52-s54 showed 2/3 PG collapse after gate eliminated TS; additional seeds test if this pattern holds with statistical power for Fisher exact test. Parent: D142.\", \"parent\": \"d142-gated-isr-s52\", \"spec\": {\"command\": \"part of d142 ext pipeline (serial s55→s56→s57)\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 56, \"reward_mode\": \"additive_bonus_gated\", \"beta\": 0.1, \"steps\": 500, \"checkpoint_source\": \"trained from base\", \"eval_data\": \"data/proofwriter_fol_100.jsonl\"}, \"checkpoint_path\": \"/root/autodl-tmp/d142_gated_isr_s56\", \"log_path\": \"/root/autodl-tmp/d142_gated_isr_s56/train.log\", \"metrics\": {\"prove_rate\": 0.36, \"mean_isr\": 0.293, \"isr_std\": 0.419, \"median_isr\": 0, \"proved_only_isr\": 0.813, \"genuine_count\": 6, \"genuine_rate\": 0.167, \"h7_count\": 0, \"h7_rate\": 0, \"h1_count\": 0, \"h1_rate\": 0, \"h8_count\": 30, \"h8_rate\": 0.833, \"content_independent_count\": 27, \"content_independent_rate\": 0.75, \"train_final_prove_rate\": 0.742, \"train_final_mean_isr\": 0.618, \"train_loss\": 0.031}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T12:11:51.474Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.7484}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-19T12:12:32.677541+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "d142-gated-isr-s57",
  "field": "status",
  "value": "RUNNING",
  "project": "solver-trace-ablation",
  "spec": "{'command': 'part of d142 ext pipeline (serial s55→s56→s57)', 'server': 'westd-39279', 'gpu': 'cuda:0', 'data_path': '/root/solver-trace-ablation/data/train_500_seed42.jsonl', 'data_count': 500, 'model_name': 'Qwen/Qwen3-4B', 'seed': 57, 'reward_mode': 'additive_bonus_gated', 'beta': 0.1, 'steps': 500, 'checkpoint_source': 'trained from base', 'eval_data': 'data/proofwriter_fol_100.jsonl'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "d142-gated-isr-s57",
    "field": "status",
    "value": "RUNNING",
    "project": "solver-trace-ablation",
    "spec": "{'command': 'part of d142 ext pipeline (serial s55→s56→s57)', 'server': 'westd-39279', 'gpu': 'cuda:0', 'data_path': '/root/solver-trace-ablation/data/train_500_seed42.jsonl', 'data_count': 500, 'model_name': 'Qwen/Qwen3-4B', 'seed': 57, 'reward_mode': 'additive_bonus_gated', 'beta': 0.1, 'steps': 500, 'checkpoint_source': 'trained from base', 'eval_data': 'data/proofwriter_fol_100.jsonl'}"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-19T12:12:32.677734+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"d142-gated-isr-s57\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:55:11.226Z\", \"updated_at\": \"2026-05-19T12:11:57.668Z\", \"hypothesis\": \"Expanding gated ISR (n_components >= 2 gate, beta=0.1) to 6 seeds to verify whether TS-to-PG mode migration is systematic. D142 s52-s54 showed 2/3 PG collapse after gate eliminated TS; additional seeds test if this pattern holds with statistical power for Fisher exact test. Parent: D142.\", \"parent\": \"d142-gated-isr-s52\", \"spec\": {\"command\": \"part of d142 ext pipeline (serial s55→s56→s57)\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 57, \"reward_mode\": \"additive_bonus_gated\", \"beta\": 0.1, \"steps\": 500, \"checkpoint_source\": \"trained from base\", \"eval_data\": \"data/proofwriter_fol_100.jsonl\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.7465}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-19T12:12:32.677881+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "d142-gated-isr-s57",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/d142_gated_isr_s57",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "d142-gated-isr-s57",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/d142_gated_isr_s57",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-19T12:12:32.678007+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "d142-gated-isr-s57",
  "field": "log_path",
  "value": "/root/autodl-tmp/d142_gated_isr_s57/train.log",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "d142-gated-isr-s57",
    "field": "log_path",
    "value": "/root/autodl-tmp/d142_gated_isr_s57/train.log",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-19T12:12:32.678160+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"d142-gated-isr-s57\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:55:11.226Z\", \"updated_at\": \"2026-05-19T12:12:02.715Z\", \"hypothesis\": \"Expanding gated ISR (n_components >= 2 gate, beta=0.1) to 6 seeds to verify whether TS-to-PG mode migration is systematic. D142 s52-s54 showed 2/3 PG collapse after gate eliminated TS; additional seeds test if this pattern holds with statistical power for Fisher exact test. Parent: D142.\", \"parent\": \"d142-gated-isr-s52\", \"spec\": {\"command\": \"part of d142 ext pipeline (serial s55→s56→s57)\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 57, \"reward_mode\": \"additive_bonus_gated\", \"beta\": 0.1, \"steps\": 500, \"checkpoint_source\": \"trained from base\", \"eval_data\": \"data/proofwriter_fol_100.jsonl\"}, \"checkpoint_path\": \"/root/autodl-tmp/d142_gated_isr_s57\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8957}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-19T12:12:32.678322+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"d142-gated-isr-s57\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:55:11.226Z\", \"updated_at\": \"2026-05-19T12:12:03.676Z\", \"hypothesis\": \"Expanding gated ISR (n_components >= 2 gate, beta=0.1) to 6 seeds to verify whether TS-to-PG mode migration is systematic. D142 s52-s54 showed 2/3 PG collapse after gate eliminated TS; additional seeds test if this pattern holds with statistical power for Fisher exact test. Parent: D142.\", \"parent\": \"d142-gated-isr-s52\", \"spec\": {\"command\": \"part of d142 ext pipeline (serial s55→s56→s57)\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 57, \"reward_mode\": \"additive_bonus_gated\", \"beta\": 0.1, \"steps\": 500, \"checkpoint_source\": \"trained from base\", \"eval_data\": \"data/proofwriter_fol_100.jsonl\"}, \"checkpoint_path\": \"/root/autodl-tmp/d142_gated_isr_s57\", \"log_path\": \"/root/autodl-tmp/d142_gated_isr_s57/train.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9736}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-19T12:12:32.678467+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "d142-gated-isr-s57",
  "field": "metrics",
  "value": "{'prove_rate': 0.88, 'mean_isr': 0.45, 'isr_std': 0.314, 'median_isr': 0.4, 'proved_only_isr': 0.511, 'genuine_count': 56, 'genuine_rate': 0.636, 'h7_count': 1, 'h7_rate': 0.011, 'h1_count': 18, 'h1_rate': 0.205, 'h8_count': 13, 'h8_rate': 0.148, 'train_final_prove_rate': 0.683, 'train_final_mean_isr': 0.271, 'train_loss': 0.027}",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "d142-gated-isr-s57",
    "field": "metrics",
    "value": "{'prove_rate': 0.88, 'mean_isr': 0.45, 'isr_std': 0.314, 'median_isr': 0.4, 'proved_only_isr': 0.511, 'genuine_count': 56, 'genuine_rate': 0.636, 'h7_count': 1, 'h7_rate': 0.011, 'h1_count': 18, 'h1_rate': 0.205, 'h8_count': 13, 'h8_rate': 0.148, 'train_final_prove_rate': 0.683, 'train_final_mean_isr': 0.271, 'train_loss': 0.027}",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-19T12:12:32.678615+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "d142-gated-isr-s57",
  "field": "conclusion",
  "value": "success",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "d142-gated-isr-s57",
    "field": "conclusion",
    "value": "success",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-19T12:12:32.678794+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"d142-gated-isr-s57\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:55:11.226Z\", \"updated_at\": \"2026-05-19T12:12:11.324Z\", \"hypothesis\": \"Expanding gated ISR (n_components >= 2 gate, beta=0.1) to 6 seeds to verify whether TS-to-PG mode migration is systematic. D142 s52-s54 showed 2/3 PG collapse after gate eliminated TS; additional seeds test if this pattern holds with statistical power for Fisher exact test. Parent: D142.\", \"parent\": \"d142-gated-isr-s52\", \"spec\": {\"command\": \"part of d142 ext pipeline (serial s55→s56→s57)\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 57, \"reward_mode\": \"additive_bonus_gated\", \"beta\": 0.1, \"steps\": 500, \"checkpoint_source\": \"trained from base\", \"eval_data\": \"data/proofwriter_fol_100.jsonl\"}, \"checkpoint_path\": \"/root/autodl-tmp/d142_gated_isr_s57\", \"log_path\": \"/root/autodl-tmp/d142_gated_isr_s57/train.log\", \"metrics\": {\"prove_rate\": 0.88, \"mean_isr\": 0.45, \"isr_std\": 0.314, \"median_isr\": 0.4, \"proved_only_isr\": 0.511, \"genuine_count\": 56, \"genuine_rate\": 0.636, \"h7_count\": 1, \"h7_rate\": 0.011, \"h1_count\": 18, \"h1_rate\": 0.205, \"h8_count\": 13, \"h8_rate\": 0.148, \"train_final_prove_rate\": 0.683, \"train_final_mean_isr\": 0.271, \"train_loss\": 0.027}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1644}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-19T12:12:32.678974+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"d142-gated-isr-s57\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:55:11.226Z\", \"updated_at\": \"2026-05-19T12:12:12.199Z\", \"hypothesis\": \"Expanding gated ISR (n_components >= 2 gate, beta=0.1) to 6 seeds to verify whether TS-to-PG mode migration is systematic. D142 s52-s54 showed 2/3 PG collapse after gate eliminated TS; additional seeds test if this pattern holds with statistical power for Fisher exact test. Parent: D142.\", \"parent\": \"d142-gated-isr-s52\", \"spec\": {\"command\": \"part of d142 ext pipeline (serial s55→s56→s57)\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 57, \"reward_mode\": \"additive_bonus_gated\", \"beta\": 0.1, \"steps\": 500, \"checkpoint_source\": \"trained from base\", \"eval_data\": \"data/proofwriter_fol_100.jsonl\"}, \"checkpoint_path\": \"/root/autodl-tmp/d142_gated_isr_s57\", \"log_path\": \"/root/autodl-tmp/d142_gated_isr_s57/train.log\", \"metrics\": {\"prove_rate\": 0.88, \"mean_isr\": 0.45, \"isr_std\": 0.314, \"median_isr\": 0.4, \"proved_only_isr\": 0.511, \"genuine_count\": 56, \"genuine_rate\": 0.636, \"h7_count\": 1, \"h7_rate\": 0.011, \"h1_count\": 18, \"h1_rate\": 0.205, \"h8_count\": 13, \"h8_rate\": 0.148, \"train_final_prove_rate\": 0.683, \"train_final_mean_isr\": 0.271, \"train_loss\": 0.027}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9117}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-19T12:12:32.679123+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "d142-gated-isr-s57",
  "field": "status",
  "value": "DONE",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "d142-gated-isr-s57",
    "field": "status",
    "value": "DONE",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-19T12:12:32.679306+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"d142-gated-isr-s57\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:55:11.226Z\", \"updated_at\": \"2026-05-19T12:12:17.369Z\", \"hypothesis\": \"Expanding gated ISR (n_components >= 2 gate, beta=0.1) to 6 seeds to verify whether TS-to-PG mode migration is systematic. D142 s52-s54 showed 2/3 PG collapse after gate eliminated TS; additional seeds test if this pattern holds with statistical power for Fisher exact test. Parent: D142.\", \"parent\": \"d142-gated-isr-s52\", \"spec\": {\"command\": \"part of d142 ext pipeline (serial s55→s56→s57)\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 57, \"reward_mode\": \"additive_bonus_gated\", \"beta\": 0.1, \"steps\": 500, \"checkpoint_source\": \"trained from base\", \"eval_data\": \"data/proofwriter_fol_100.jsonl\"}, \"checkpoint_path\": \"/root/autodl-tmp/d142_gated_isr_s57\", \"log_path\": \"/root/autodl-tmp/d142_gated_isr_s57/train.log\", \"metrics\": {\"prove_rate\": 0.88, \"mean_isr\": 0.45, \"isr_std\": 0.314, \"median_isr\": 0.4, \"proved_only_isr\": 0.511, \"genuine_count\": 56, \"genuine_rate\": 0.636, \"h7_count\": 1, \"h7_rate\": 0.011, \"h1_count\": 18, \"h1_rate\": 0.205, \"h8_count\": 13, \"h8_rate\": 0.148, \"train_final_prove_rate\": 0.683, \"train_final_mean_isr\": 0.271, \"train_loss\": 0.027}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T12:12:17.369Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9261}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_d142-ext-status_20260519T120936",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 87 · 2026-05-19T12:12:32.679549+00:00_

三个实验全部更新完成。汇总报告：

## D142 Gated ISR 实验诊断结果

### 环境状态
- **GPU**: 空闲（0MiB / 97887MiB），无运行进程
- **磁盘**: 45G / 250G（18%），充裕

### 实验结果

| | s55 | s56 | s57 |
|---|---|---|---|
| **状态** | SUCCESS | SUCCESS | SUCCESS |
| **Proved** | 100/100 (100%) | 36/100 (36%) | 88/100 (88%) |
| **Mean ISR** | 0.525 | 0.293 | 0.450 |
| **Proved-only ISR** | 0.525 | 0.813 | 0.511 |
| **H7 (TS)** | **82/100 (82%)** | 0 | 1/88 (1.1%) |
| **H1 (CE)** | 0 | 0 | 18/88 (20.5%) |
| **H8 (PG)** | 15/100 (15%) | **30/36 (83.3%)** | 13/88 (14.8%) |
| **Genuine** | **3/100 (3%)** | **6/36 (16.7%)** | **56/88 (63.6%)** |
| **ContentIndep** | 0 | **27/36 (75%)** | 0 |
| **Checkpoint** | `/root/autodl-tmp/d142_gated_isr_s55` | `...s56` | `...s57` |

### 模式分析

三个 seed 展示了三种完全不同的 collapse 模式：
- **s55**: 极端 TS collapse（82% H7），gate 完全未能阻止 tautology shortcut
- **s56**: PG collapse + content-independent（83% H8, 75% CntIndep），prove rate 暴跌到 36%
- **s57**: 最健康的结果，63.6% genuine，但仍有 CE 和 PG 各约 15-20%

Registry 已全部更新为 DONE/success。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_diag_d142-ext-status_20260519T120936"
}
```

</details>

---
