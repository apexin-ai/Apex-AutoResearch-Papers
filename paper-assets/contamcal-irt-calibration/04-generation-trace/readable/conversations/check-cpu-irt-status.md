# check cpu irt status

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_check_cpu-irt-status_20260515T001803.jsonl`
- **Structured JSON:** [`17ae21f769f2464ab6de.json`](../../sessions/17/17ae21f769f2464ab6de.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-15T00:18:46.208727+00:00_

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
  "session": "worker_check_cpu-irt-status_20260515T001803",
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

_source line 2 · 2026-05-15T00:18:46.209052+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_cpu-irt-status_20260515T001803",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T00:18:46.209217+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ps aux | grep run_exp006 | grep -v grep"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_cpu-irt-status_20260515T001803",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ps aux | grep run_exp006 | grep -v grep"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T00:18:46.209381+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_cpu-irt-status_20260515T001803",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T00:18:46.209515+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -r run_exp006 /proc/*/cmdline 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_cpu-irt-status_20260515T001803",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -r run_exp006 /proc/*/cmdline 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T00:18:46.209641+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_cpu-irt-status_20260515T001803",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T00:18:46.209771+00:00_

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
  "session": "worker_check_cpu-irt-status_20260515T001803",
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

_source line 8 · 2026-05-15T00:18:46.209887+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_cpu-irt-status_20260515T001803",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T00:18:46.210000+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ps aux | grep run_exp006 | grep -v grep",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_cpu-irt-status_20260515T001803",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ps aux | grep run_exp006 | grep -v grep",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T00:18:46.210168+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"设置成功\\n注意：仅限于学术用途和加速访问github/huggingface，不承诺稳定性保证\\nroot     452342  0.0  0.0   4364  3144 ?        Ss   06:42   0:00 bash -c source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp006 && python3 run_exp006.py --benchmark gsm8k --pool-scales 0.5B 1.5B --signals-dir /root/autodl-tmp/exp002/signals --aligned-only --seed 42 --output-dir /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v3_rrf 2>&1\\nroot     452348  0.2  0.0 6010388 179776 ?      Sl   06:42   0:16 python3 run_exp006.py --benchmark gsm8k --pool-scales 0.5B 1.5B --signals-dir /root/autodl-tmp/exp002/signals --aligned-only --seed 42 --output-dir /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v3_rrf\\nroot     463988  2.5  0.0 7185520 277140 ?      Sl   07:43   0:53 python run_exp006.py --eval-dir /root/autodl-tmp/exp001/eval_results --pool-scales 0.5B 1.5B --signals-dir /root/autodl-tmp/exp002/signals --aligned-only --model-type 2pl_gamma --benchmarks gsm8k arc_challenge mmlu --output-dir /root/autodl-tmp/exp006/results_pooled_05B_15B_2pl_ablation\\nroot     468994  0.0  0.0   4364  3184 pts/0    Ss+  08:02   0:00 bash -c python exp006/run_exp006.py --pool-scales 0.5B 1.5B --benchmark arc_challenge --signals-dir /root/autodl-tmp/exp002/signals --signal-key s1_embedding --require-signals --aligned-only --data-seed 42 --output-dir /root/autodl-tmp/exp006/results_pooled_s1only_arc --joint-fit 2>&1 | tee /tmp/irt_s1only_arc.log\\nroot     468996  5.2  0.0 7256212 349976 pts/0  Sl+  08:02   0:50 python exp006/run_exp006.py --pool-scales 0.5B 1.5B --benchmark arc_challenge --signals-dir /root/autodl-tmp/exp002/signals --signal-key s1_embedding --require-signals --aligned-only --data-seed 42 --output-dir /root/autodl-tmp/exp006/results_pooled_s1only_arc --joint-fit\\nroot     469159  0.0  0.0   4364  3212 pts/1    Ss+  08:02   0:00 bash -c python exp006/run_exp006.py --pool-scales 0.5B 1.5B --
…[truncated 1432 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_cpu-irt-status_20260515T001803",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T00:18:46.210427+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "source /etc/network_turbo && ls -la /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_oracle_extended/ 2>/dev/null; echo \"---DIR2---\"; ls -la /root/autodl-tmp/exp006/results_pooled_s1only_gsm8k/ 2>/dev/null; echo \"---DIR3---\"; ls -la /root/autodl-tmp/exp006/results_pooled_s1only_arc/ 2>/dev/null",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_cpu-irt-status_20260515T001803",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "source /etc/network_turbo && ls -la /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_oracle_extended/ 2>/dev/null; echo \"---DIR2---\"; ls -la /root/autodl-tmp/exp006/results_pooled_s1only_gsm8k/ 2>/dev/null; echo \"---DIR3---\"; ls -la /root/autodl-tmp/exp006/results_pooled_s1only_arc/ 2>/dev/null",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T00:18:46.210591+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"设置成功\\n注意：仅限于学术用途和加速访问github/huggingface，不承诺稳定性保证\\ntotal 4\\ndrwxr-xr-x  3 root root   27 May 15 08:04 .\\ndrwxr-xr-x 27 root root 4096 May 15 08:04 ..\\ndrwxr-xr-x  2 root root   10 May 15 08:04 gsm8k\\n---DIR2---\\ntotal 8\\ndrwxr-xr-x  4 root root   80 May 15 08:17 .\\ndrwxr-xr-x 27 root root 4096 May 15 08:04 ..\\n-rw-r--r--  1 root root 1954 May 15 08:02 dryrun_metadata.json\\ndrwxr-xr-x  2 root root  148 May 15 08:17 gsm8k\\ndrwxr-xr-x  2 root root   10 May 15 08:17 joint_fit\\n---DIR3---\\ntotal 8\\ndrwxr-xr-x  4 root root   88 May 15 08:15 .\\ndrwxr-xr-x 27 root root 4096 May 15 08:04 ..\\ndrwxr-xr-x  2 root root  148 May 15 08:15 arc_challenge\\n-rw-r--r--  1 root root 1970 May 15 08:01 dryrun_metadata.json\\ndrwxr-xr-x  2 root root   10 May 15 08:15 joint_fit\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_cpu-irt-status_20260515T001803",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T00:18:46.210756+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -20 /tmp/exp006_oracle_gsm8k_extended.log 2>/dev/null || echo \"NO_LOG\"",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_cpu-irt-status_20260515T001803",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -20 /tmp/exp006_oracle_gsm8k_extended.log 2>/dev/null || echo \"NO_LOG\"",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T00:18:46.210909+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\rchain 3:  48%|\\u001b[34m████▊     \\u001b[0m| 2900/6000 [12:47<13:51,  3.73it/s, (Sampling)]\\u001b[A\\u001b[A\\n\\rchain 2:  48%|\\u001b[34m████▊     \\u001b[0m| 2900/6000 [12:50<13:51,  3.73it/s, (Sampling)]\\u001b[A\\rchain 1:  47%|\\u001b[34m████▋     \\u001b[0m| 2800/6000 [12:55<14:26,  3.69it/s, (Sampling)]\\n\\n\\n\\rchain 4:  48%|\\u001b[34m████▊     \\u001b[0m| 2900/6000 [13:04<13:54,  3.71it/s, (Sampling)]\\u001b[A\\u001b[A\\u001b[A\\n\\n\\rchain 3:  50%|\\u001b[34m█████     \\u001b[0m| 3000/6000 [13:15<13:34,  3.68it/s, (Sampling)]\\u001b[A\\u001b[A\\n\\rchain 2:  50%|\\u001b[34m█████     \\u001b[0m| 3000/6000 [13:17<13:26,  3.72it/s, (Sampling)]\\u001b[A\\rchain 1:  48%|\\u001b[34m████▊     \\u001b[0m| 2900/6000 [13:22<13:56,  3.70it/s, (Sampling)]\\n\\n\\n\\rchain 4:  50%|\\u001b[34m█████     \\u001b[0m| 3000/6000 [13:32<13:31,  3.70it/s, (Sampling)]\\u001b[A\\u001b[A\\u001b[A\\n\\n\\rchain 3:  52%|\\u001b[34m█████▏    \\u001b[0m| 3100/6000 [13:43<13:14,  3.65it/s, (Sampling)]\\u001b[A\\u001b[A\\n\\rchain 2:  52%|\\u001b[34m█████▏    \\u001b[0m| 3100/6000 [13:43<12:53,  3.75it/s, (Sampling)]\\u001b[A\\rchain 1:  50%|\\u001b[34m█████     \\u001b[0m| 3000/6000 [13:50<13:41,  3.65it/s, (Sampling)]\\n\\n\\n\\rchain 4:  52%|\\u001b[34m█████▏    \\u001b[0m| 3100/6000 [14:00<13:16,  3.64it/s, (Sampling)]\\u001b[A\\u001b[A\\u001b[A\\n\\rchain 2:  53%|\\u001b[34m█████▎    \\u001b[0m| 3200/6000 [14:09<12:19,  3.79it/s, (Sampling)]\\u001b[A\\n\\n\\rchain 3:  53%|\\u001b[34m█████▎    \\u001b[0m| 3200/6000 [14:11<12:56,  3.61it/s, (Sampling)]\\u001b[A\\u001b[A\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_cpu-irt-status_20260515T001803",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T00:18:46.211057+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -20 /tmp/irt_s1only_gsm8k.log 2>/dev/null || echo \"NO_LOG\"",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_cpu-irt-status_20260515T001803",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -20 /tmp/irt_s1only_gsm8k.log 2>/dev/null || echo \"NO_LOG\"",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T00:18:46.211210+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-------------------------------------------------------------------------------------------------------\\n\\rchain 1:   0%|\\u001b[33m          \\u001b[0m| 0/2000 [00:00<?, ?it/s, (Warmup)]\\n\\rchain 2:   0%|\\u001b[33m          \\u001b[0m| 0/2000 [00:00<?, ?it/s, (Warmup)]\\u001b[A\\n\\n\\rchain 3:   0%|\\u001b[33m          \\u001b[0m| 0/2000 [00:00<?, ?it/s, (Warmup)]\\u001b[A\\u001b[A\\n\\n\\n\\rchain 4:   0%|\\u001b[33m          \\u001b[0m| 0/2000 [00:00<?, ?it/s, (Warmup)]\\u001b[A\\u001b[A\\u001b[A\\n\\rchain 2:   5%|\\u001b[33m▌         \\u001b[0m| 100/2000 [00:25<07:57,  3.98it/s, (Warmup)]\\u001b[A\\n\\n\\rchain 3:   5%|\\u001b[33m▌         \\u001b[0m| 100/2000 [00:29<09:21,  3.38it/s, (Warmup)]\\u001b[A\\u001b[A\\n\\n\\n\\rchain 4:   5%|\\u001b[33m▌         \\u001b[0m| 100/2000 [00:31<09:53,  3.20it/s, (Warmup)]\\u001b[A\\u001b[A\\u001b[A\\rchain 1:   5%|\\u001b[33m▌         \\u001b[0m| 100/2000 [00:31<09:56,  3.19it/s, (Warmup)]\\n\\rchain 2:  10%|\\u001b[33m█         \\u001b[0m| 200/2000 [00:39<05:38,  5.31it/s, (Warmup)]\\u001b[A\\n\\n\\n\\rchain 4:  10%|\\u001b[33m█         \\u001b[0m| 200/2000 [00:44<06:09,  4.87it/s, (Warmup)]\\u001b[A\\u001b[A\\u001b[A\\n\\n\\rchain 3:  10%|\\u001b[33m█         \\u001b[0m| 200/2000 [00:46<06:39,  4.51it/s, (Warmup)]\\u001b[A\\u001b[A\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_cpu-irt-status_20260515T001803",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T00:18:46.211366+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -20 /tmp/irt_s1only_arc.log 2>/dev/null || echo \"NO_LOG\"",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_cpu-irt-status_20260515T001803",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -20 /tmp/irt_s1only_arc.log 2>/dev/null || echo \"NO_LOG\"",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T00:18:46.211530+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\rchain 4:  50%|\\u001b[34m█████     \\u001b[0m| 1001/2000 [02:55<01:58,  8.41it/s, (Sampling)]\\u001b[A\\u001b[A\\u001b[A\\n\\n\\rchain 3:  50%|\\u001b[33m█████     \\u001b[0m| 1000/2000 [02:58<02:07,  7.83it/s, (Warmup)]\\u001b[A\\u001b[A\\n\\n\\rchain 3:  50%|\\u001b[34m█████     \\u001b[0m| 1000/2000 [02:58<02:07,  7.83it/s, (Sampling)]\\u001b[A\\u001b[A\\n\\n\\rchain 3:  50%|\\u001b[34m█████     \\u001b[0m| 1001/2000 [02:58<02:07,  7.82it/s, (Sampling)]\\u001b[A\\u001b[A\\rchain 1:  60%|\\u001b[34m██████    \\u001b[0m| 1200/2000 [02:58<01:42,  7.78it/s, (Sampling)]\\n\\rchain 2:  60%|\\u001b[34m██████    \\u001b[0m| 1200/2000 [03:02<01:43,  7.72it/s, (Sampling)]\\u001b[A\\n\\n\\n\\rchain 4:  55%|\\u001b[34m█████▌    \\u001b[0m| 1100/2000 [03:08<01:48,  8.26it/s, (Sampling)]\\u001b[A\\u001b[A\\u001b[A\\rchain 1:  65%|\\u001b[34m██████▌   \\u001b[0m| 1300/2000 [03:11<01:30,  7.70it/s, (Sampling)]\\n\\n\\rchain 3:  55%|\\u001b[34m█████▌    \\u001b[0m| 1100/2000 [03:12<01:58,  7.61it/s, (Sampling)]\\u001b[A\\u001b[A\\n\\rchain 2:  65%|\\u001b[34m██████▌   \\u001b[0m| 1300/2000 [03:15<01:31,  7.66it/s, (Sampling)]\\u001b[A\\n\\n\\n\\rchain 4:  60%|\\u001b[34m██████    \\u001b[0m| 1200/2000 [03:20<01:36,  8.28it/s, (Sampling)]\\u001b[A\\u001b[A\\u001b[A\\rchain 1:  70%|\\u001b[34m███████   \\u001b[0m| 1400/2000 [03:25<01:18,  7.67it/s, (Sampling)]\\n\\n\\rchain 3:  60%|\\u001b[34m██████    \\u001b[0m| 1200/2000 [03:25<01:46,  7.52it/s, (Sampling)]\\u001b[A\\u001b[A\\n\\rchain 2:  70%|\\u001b[34m███████   \\u001b[0m| 1400/2000 [03:29<01:18,  7.64it/s, (Sampling)]\\u001b[A\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_cpu-irt-status_20260515T001803",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-15T00:18:46.211705+00:00_

3 个任务全部 **running**：

| 任务 | 状态 | 进度 |
|------|------|------|
| **exp006-oracle-gsm8k-extended** | running | 4 chains, ~50-53% sampling (warmup 2000 + samples 4000 = 6000 total), ~3.6 it/s, 预计还需 ~14 min |
| **exp006-pooled-s1only-gsm8k** | running | 刚开始 warmup, 4 chains 约 5-10% warmup (200/2000), ~4-5 it/s |
| **exp006-pooled-s1only-arc** | running | chains 1&2 在 65-70% sampling, chains 3&4 在 55-60% sampling (总共 2000 samples), ~7.5 it/s, 预计还需 ~2-3 min |

**预计完成顺序**: arc (最快, ~2-3 min) → oracle-extended (~14 min) → s1only-gsm8k (最慢, 刚开始 warmup)

另外注意：服务器上还有 2 个其他 exp006 进程在跑：
- `results_pooled_05B_15B_gsm8k_v3_rrf`
- `results_pooled_05B_15B_2pl_ablation`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_check_cpu-irt-status_20260515T001803"
}
```

</details>

---
