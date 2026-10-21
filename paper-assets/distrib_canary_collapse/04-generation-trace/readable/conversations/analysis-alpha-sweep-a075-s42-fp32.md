# analysis alpha sweep a075 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 0
- **Tool calls:** 23
- **Original source:** `logs/chats/worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135.jsonl`
- **Structured JSON:** [`2e2e905185fbe4ff4504.json`](../../sessions/2e/2e2e905185fbe4ff4504.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

47 recorded events

### Tool call

_source line 1 · 2026-05-19T14:24:36.316507+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__read_registry",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__read_registry",
    "max_results": "7"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T14:24:36.316838+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T14:24:36.317004+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "tail -30 /root/runs/distrib_canary_collapse/alpha_sweep_a075_s42_fp32.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "tail -30 /root/runs/distrib_canary_collapse/alpha_sweep_a075_s42_fp32.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-19T14:24:36.317132+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "ls -la /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s42_fp32/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "ls -la /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s42_fp32/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-19T14:24:36.317373+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\r 66%|██████▌   | 3300/5000 [07:10<03:42,  7.65it/s]\\r 66%|██████▌   | 3301/5000 [07:10<03:42,  7.65it/s]\\r 66%|██████▌   | 3302/5000 [07:10<03:43,  7.58it/s]\\r 66%|██████▌   | 3303/5000 [07:10<03:42,  7.62it/s]\\r 66%|██████▌   | 3304/5000 [07:10<03:42,  7.64it/s]\\r 66%|██████▌   | 3305/5000 [07:10<03:43,  7.59it/s]\\r 66%|██████▌   | 3306/5000 [07:11<03:41,  7.64it/s]\\r 66%|██████▌   | 3307/5000 [07:11<03:41,  7.64it/s]\\r 66%|██████▌   | 3308/5000 [07:11<03:41,  7.63it/s]\\r 66%|██████▌   | 3309/5000 [07:11<03:40,  7.65it/s]\\r 66%|██████▌   | 3310/5000 [07:11<03:40,  7.66it/s]\\r 66%|██████▌   | 3311/5000 [07:11<03:40,  7.65it/s]\\r 66%|██████▌   | 3312/5000 [07:11<03:40,  7.67it/s]\\r 66%|██████▋   | 3313/5000 [07:11<03:39,  7.68it/s]\\r 66%|██████▋   | 3314/5000 [07:12<03:39,  7.68it/s]\\r 66%|█���████▋   | 3315/5000 [07:12<03:40,  7.66it/s]\\r 66%|██████▋   | 3316/5000 [07:12<03:39,  7.68it/s]\\r 66%|██████▋   | 3317/5000 [07:12<03:39,  7.66it/s]\\r 66%|██████▋   | 3318/5000 [07:12<03:41,  7.58it/s]\\r 66%|██████▋   | 3319/5000 [07:12<03:39,  7.66it/s]\\r 66%|██████▋   | 3320/5000 [07:12<03:38,  7.67it/s]\\r 66%|██████▋   | 3321/5000 [07:12<03:39,  7.64it/s]\\r 66%|██████▋   | 3322/5000 [07:13<03:38,  7.68it/s]\\r 66%|██████▋   | 3323/5000 [07:13<03:38,  7.69it/s]\\r 66%|██████▋   | 3324/5000 [07:13<03:38,  7.69it/s]\\r 66%|██████▋   | 3325/5000 [07:13<03:38,  7.68it/s]\\r 67%|██████▋   | 3326/5000 [07:13<03:37,  7.68it/s]\\r 67%|██████▋   | 3327/5000 [07:13<03:37,  7.68it/s]\\r 67%|██████▋   | 3328/5000 [07:13<03:39,  7.63it/s]\\r 67%|██████▋   | 3329/5000 [07:14<03:37,  7.67it/s]\\r 67%|████��█▋   | 3330/5000 [07:14<03:37,  7.66it/s]\\r 67%|██████▋   | 3331/5000 [07:14<03:38,  7.65it/s]\\r 67%|██████▋   | 3332/5000 [07:14<03:37,  7.68it/s]\\r 67%|██████▋   | 3333/5000 [07:14<03:36,  7.68it/s]\\r 67%|██████▋   | 3334/5000 [07:14<03:36,  7.68it/s]\\r 67%|██████▋   | 3335/5000 [07:14<03:37,  7.67it
…[truncated 6479 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-19T14:24:36.317562+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "distrib_canary_collapse",
  "filters": "{'exp_id': 'alpha_sweep_a075_s42_fp32'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "distrib_canary_collapse",
    "filters": "{'exp_id': 'alpha_sweep_a075_s42_fp32'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-19T14:24:36.317708+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 44\\ndrwxr-xr-x 13 root root  4096 May 19 22:18 .\\ndrwxr-xr-x 25 root root  4096 May 19 22:16 ..\\n-rw-r--r--  1 root root     2 May 19 22:18 EXIT_CODE\\n-rw-r--r--  1 root root  4975 May 19 22:18 all_metrics.json\\n-rw-r--r--  1 root root  1822 May 19 19:45 all_metrics.json.stale_4gen_bak\\n-rw-r--r--  1 root root 13902 May 19 19:45 analysis_results.json.stale_4gen_bak\\n-rw-r--r--  1 root root   637 May 19 17:58 config.json\\ndrwxr-xr-x  3 root root    60 May 19 18:11 gen_0\\ndrwxr-xr-x  4 root root    79 May 19 19:24 gen_1\\ndrwxr-xr-x  5 root root   101 May 19 22:18 gen_10\\ndrwxr-xr-x  4 root root    79 May 19 19:49 gen_2\\ndrwxr-xr-x  4 root root    79 May 19 20:13 gen_3\\ndrwxr-xr-x  4 root root    89 May 19 21:17 gen_4\\ndrwxr-xr-x  4 root root    79 May 19 21:03 gen_5\\ndrwxr-xr-x  4 root root    79 May 19 21:28 gen_6\\ndrwxr-xr-x  4 root root    79 May 19 21:52 gen_7\\ndrwxr-xr-x  4 root root    79 May 19 22:17 gen_8\\ndrwxr-xr-x  5 root root   101 May 19 21:54 gen_9\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T14:24:36.317839+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.276}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T14:24:36.317990+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s42_fp32/all_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s42_fp32/all_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T14:24:36.318218+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"token_entropy\\\": 3.23419483150593,\\n    \\\"self_bleu\\\": 0.011078699301381554,\\n    \\\"ece\\\": 0.010804557477709054,\\n    \\\"effective_rank\\\": 46.612774691899155,\\n    \\\"perplexity\\\": 26.948958972544652,\\n    \\\"distinct_1\\\": 0.0979600146585773,\\n    \\\"distinct_2\\\": 0.5141374985748489,\\n    \\\"distinct_3\\\": 0.8127010497341054,\\n    \\\"mauve\\\": 0.031110582626136873,\\n    \\\"generation\\\": 0,\\n    \\\"intervention_triggered\\\": false,\\n    \\\"trigger_gen\\\": null,\\n    \\\"effective_alpha\\\": 0.75\\n  },\\n  {\\n    \\\"token_entropy\\\": 2.1737574601166205,\\n    \\\"self_bleu\\\": 0.01181542928801186,\\n    \\\"ece\\\": 0.13495560422313238,\\n    \\\"effective_rank\\\": 69.94078030681871,\\n    \\\"perplexity\\\": 31.798856175084083,\\n    \\\"distinct_1\\\": 0.09759209446336131,\\n    \\\"distinct_2\\\": 0.5124500211292787,\\n    \\\"distinct_3\\\": 0.8121673127402459,\\n    \\\"mauve\\\": 0.0314065242440103,\\n    \\\"generation\\\": 1,\\n    \\\"intervention_triggered\\\": false,\\n    \\\"trigger_gen\\\": null,\\n    \\\"effective_alpha\\\": 0.75\\n  },\\n  {\\n    \\\"token_entropy\\\": 2.105473003087621,\\n    \\\"self_bleu\\\": 0.012090258112174944,\\n    \\\"ece\\\": 0.1779500537358194,\\n    \\\"effective_rank\\\": 79.7007388564995,\\n    \\\"perplexity\\\": 44.309865144199506,\\n    \\\"distinct_1\\\": 0.0838515625,\\n    \\\"distinct_2\\\": 0.44422222048609755,\\n    \\\"distinct_3\\\": 0.7376990265472898,\\n    \\\"mauve\\\": 0.03220706380808024,\\n    \\\"generation\\\": 2,\\n    \\\"intervention_triggered\\\": false,\\n    \\\"trigger_gen\\\": null,\\n    \\\"effective_alpha\\\": 0.75\\n  },\\n  {\\n    \\\"token_entropy\\\": 2.0912935053356088,\\n    \\\"self_bleu\\\": 0.012363725950916941,\\n    \\\"ece\\\": 0.18826733518407487,\\n    \\\"effective_rank\\\": 81.14340988552406,\\n    \\\"perplexity\\\": 50.52814774519698,\\n    \\\"dis
…[truncated 4325 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T14:24:36.318438+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s42_fp32/EXIT_CODE",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s42_fp32/EXIT_CODE",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T14:24:36.318575+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T14:24:36.318738+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s42_fp32/gen_10/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s42_fp32/gen_10/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-19T14:24:36.318862+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/src -name \"*.py\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/src -name \"*.py\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-19T14:24:36.318984+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"checkpoint\\nmetrics.json\\nsynthetic_data\\ntrainer\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-19T14:24:36.319099+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s42_fp32/gen_9/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s42_fp32/gen_9/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-19T14:24:36.319217+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"find: '/root/autodl-tmp/distrib_canary_collapse/src': No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T14:24:36.319386+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"checkpoint\\nmetrics.json\\nsynthetic_data\\ntrainer\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T14:24:36.319519+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "find /root/autodl-tmp/distrib_canary_collapse -maxdepth 2 -name \"*.py\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "find /root/autodl-tmp/distrib_canary_collapse -maxdepth 2 -name \"*.py\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T14:24:36.319649+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/analysis/detrending_utils.py\\n/root/autodl-tmp/distrib_canary_collapse/configs/dryrun_6.9b.py\\n/root/autodl-tmp/distrib_canary_collapse/mmct/__init__.py\\n/root/autodl-tmp/distrib_canary_collapse/mmct/methods.py\\n/root/autodl-tmp/distrib_canary_collapse/mmct/null_distribution.py\\n/root/autodl-tmp/distrib_canary_collapse/mmct/consensus_test.py\\n/root/autodl-tmp/distrib_canary_collapse/mmct/run_mmct.py\\n/root/autodl-tmp/distrib_canary_collapse/scripts/gen_single_method_table.py\\n/root/autodl-tmp/distrib_canary_collapse/scripts/transfer_entropy_analysis.py\\n/root/autodl-tmp/distrib_canary_collapse/scripts/change_point_analysis.py\\n/root/autodl-tmp/distrib_canary_collapse/scripts/change_point_supplement.py\\n/root/autodl-tmp/distrib_canary_collapse/iterative_train.py\\n/root/autodl-tmp/distrib_canary_collapse/metrics.py\\n/root/autodl-tmp/distrib_canary_collapse/prepare_data.py\\n/root/autodl-tmp/distrib_canary_collapse/prepare_c4.py\\n/root/autodl-tmp/distrib_canary_collapse/prepare_c4_v2.py\\n/root/autodl-tmp/distrib_canary_collapse/prepare_c4_v3.py\\n/root/autodl-tmp/distrib_canary_collapse/prepare_c4_v4.py\\n/root/autodl-tmp/distrib_canary_collapse/prepare_c4_5k_fix.py\\n/root/autodl-tmp/distrib_canary_collapse/prepare_c4_5k_v5.py\\n/root/autodl-tmp/distrib_canary_collapse/run_5method_s43.py\\n/root/autodl-tmp/distrib_canary_collapse/batch_analysis.py\\n/root/autodl-tmp/distrib_canary_collapse/run_intervention_5method.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T14:24:36.319785+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "head -80 /root/autodl-tmp/distrib_canary_collapse/batch_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "head -80 /root/autodl-tmp/distrib_canary_collapse/batch_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T14:24:36.319948+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Batch lead-lag analysis for distributional canary collapse experiments.\\n\\nReads all_metrics.json from an experiment directory, runs 5-method lead-lag\\nanalysis on all canary-diversity pairs, computes K>=4 consensus, and optionally\\nruns full MMCT if null directories are provided.\\n\\nUsage:\\n    python batch_analysis.py --exp_dir results/alpha_sweep/a010_s43_bf16\\n    python batch_analysis.py --exp_dir results/alpha_sweep/a010_s43_bf16 \\\\\\n        --null_dirs results/alpha_sweep/a000_s42 results/alpha_sweep/a000_s43\\n\\nInput:  {exp_dir}/all_metrics.json\\nOutput: {exp_dir}/analysis_results.json (or --output path)\\n\\nDependencies: numpy, scipy, statsmodels\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport sys\\nimport traceback\\nimport numpy as np\\nfrom scipy import stats\\nfrom statsmodels.tsa.stattools import adfuller\\n\\nN_PERM = 5000\\nALPHA_SIG = 0.05\\n\\nCANARIES = [\\\"token_entropy\\\", \\\"ece\\\"]\\nDOWNSTREAMS = [\\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\", \\\"mauve\\\"]\\n\\nHIGHER_IS_WORSE = {\\\"ece\\\", \\\"perplexity\\\"}\\nLOWER_IS_WORSE = {\\\"token_entropy\\\", \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\", \\\"mauve\\\"}\\n\\nALL_METRICS = [\\\"token_entropy\\\", \\\"ece\\\", \\\"perplexity\\\", \\\"distinct_1\\\", \\\"distinct_2\\\",\\n               \\\"distinct_3\\\", \\\"effective_rank\\\", \\\"mauve\\\"]\\n\\n\\ndef load_series(data_dir):\\n    path = os.path.join(data_dir, \\\"all_metrics.json\\\")\\n    with open(path) as f:\\n        data = json.load(f)\\n    data.sort(key=lambda x: x[\\\"generation\\\"])\\n    out = {}\\n    for k in ALL_METRICS:\\n        vals = []\\n        for d in data:\\n            v = d.get(k)\\n            vals.append(v if v is not None else np.nan)\\n        out[k] = np.array(vals, dtype=float)\\n    return out, len(data)\\n\\n\\ndef orient(series, name):\\n    return -series.co
…[truncated 817 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T14:24:36.320147+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T14:24:36.320334+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"a005_s42_fp32\\na005_s42_fp32_v2\\na005_s42_fp32_v3\\na005_s42_fp32_v3_d080\\na010_s42_bf16\\na010_s42_fp32\\na010_s43_bf16\\na010_s43_fp32\\na025_s42_fp32\\na025_s43_fp32\\na025_s44_fp32\\na030_s42_fp32\\na040_s42_fp32\\na050_s42_fp32\\na050_s43_fp32\\na050_s44_fp32\\na060_s42\\na060_s42_bf16\\na060_s42_fp32\\na060_s42_fp32_v2\\na060_s42_fp32_v3_d080\\na060_s43_fp32\\na075_s42_fp32\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T14:24:36.320507+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-17855",
  "command": "cd /root/autodl-tmp/distrib_canary_collapse && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1 python batch_analysis.py --exp_dir results/alpha_sweep/a075_s42_fp32",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-17855",
    "command": "cd /root/autodl-tmp/distrib_canary_collapse && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1 python batch_analysis.py --exp_dir results/alpha_sweep/a075_s42_fp32",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T14:24:36.320649+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loading data from results/alpha_sweep/a075_s42_fp32\\n  11 generations loaded\\nComputing drift...\\nRunning 5-method lead-lag analysis...\\nNo null_dirs provided, using simple K>=4 consensus as MMCT proxy\\n\\nSaved: results/alpha_sweep/a075_s42_fp32/analysis_results.json\\n\\n============================================================\\nSUMMARY: results/alpha_sweep/a075_s42_fp32\\n============================================================\\nGenerations: 11\\n\\nDrift (gen0->gen10):\\n  token_entropy       : -29.41%\\n  ece                 : +1885.41%\\n  perplexity          : +188.31%\\n  distinct_1          : -25.38%\\n  distinct_2          : -30.55%\\n  distinct_3          : -26.70%\\n  effective_rank      : +67.47%\\n  mauve               : -3.73%\\n\\nLead-lag (forward significant / total):\\n  naive_xcorr         : 7/8\\n  diff_xcorr          : 6/8\\n  threshold_onset     : 8/8\\n  perm_granger_fwd    : 6/8\\n  perm_granger_rev    : 0/8\\n  ty_granger          : 8/8\\n  consensus_k4        : 6/8\\n\\nMMCT: weighted_pair_forward, detection_rate=0.75\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.76}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T14:24:36.320819+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s42_fp32/analysis_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s42_fp32/analysis_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T14:24:36.321194+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"exp_dir\\\": \\\"results/alpha_sweep/a075_s42_fp32\\\",\\n  \\\"n_generations\\\": 11,\\n  \\\"drift_pct\\\": {\\n    \\\"token_entropy\\\": -29.41,\\n    \\\"ece\\\": 1885.41,\\n    \\\"perplexity\\\": 188.31,\\n    \\\"distinct_1\\\": -25.38,\\n    \\\"distinct_2\\\": -30.55,\\n    \\\"distinct_3\\\": -26.7,\\n    \\\"effective_rank\\\": 67.47,\\n    \\\"mauve\\\": -3.73\\n  },\\n  \\\"lead_lag\\\": {\\n    \\\"naive_xcorr\\\": {\\n      \\\"forward\\\": 7,\\n      \\\"total\\\": 8\\n    },\\n    \\\"diff_xcorr\\\": {\\n      \\\"forward\\\": 6,\\n      \\\"total\\\": 8\\n    },\\n    \\\"threshold_onset\\\": {\\n      \\\"forward\\\": 8,\\n      \\\"total\\\": 8\\n    },\\n    \\\"perm_granger_fwd\\\": {\\n      \\\"sig\\\": 6,\\n      \\\"total\\\": 8\\n    },\\n    \\\"perm_granger_rev\\\": {\\n      \\\"sig\\\": 0,\\n      \\\"total\\\": 8\\n    },\\n    \\\"ty_granger\\\": {\\n      \\\"sig\\\": 8,\\n      \\\"total\\\": 8\\n    },\\n    \\\"consensus_k4\\\": {\\n      \\\"sig\\\": 6,\\n      \\\"total\\\": 8\\n    }\\n  },\\n  \\\"mmct\\\": {\\n    \\\"mode\\\": \\\"weighted_pair_forward\\\",\\n    \\\"detection_rate\\\": 0.75,\\n    \\\"note\\\": \\\"simple_consensus_k4 (no null distribution)\\\"\\n  },\\n  \\\"consensus_detail\\\": [\\n    {\\n      \\\"pair\\\": \\\"token_entropy->distinct_1\\\",\\n      \\\"votes\\\": 5,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"thresh\\\",\\n        \\\"pg_fwd\\\",\\n        \\\"ty\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"token_entropy->distinct_2\\\",\\n      \\\"votes\\\": 5,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"thresh\\\",\\n        \\\"pg_fwd\\\",\\n        \\\"ty\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"token_entropy->distinct_3\\\",\\n      \\\"votes\\\": 5,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n       
…[truncated 8875 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T14:24:36.321472+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "alpha_sweep_a075_s42_fp32",
  "field": "hypothesis",
  "value": "α=0.75 pre-D080 was fp16; fp32 rerun provides D079-compliant authoritative data. PermG expected ~83% (high regime), drift magnitude may change with fp32 precision.",
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "alpha_sweep_a075_s42_fp32",
    "field": "hypothesis",
    "value": "α=0.75 pre-D080 was fp16; fp32 rerun provides D079-compliant authoritative data. PermG expected ~83% (high regime), drift magnitude may change with fp32 precision.",
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T14:24:36.321648+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"alpha_sweep_a075_s42_fp32\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T06:18:30.958Z\", \"updated_at\": \"2026-05-19T14:23:30.876Z\", \"hypothesis\": \"α=0.75 pre-D080 was fp16; fp32 rerun provides D079-compliant authoritative data. PermG expected ~83% (high regime), drift magnitude may change with fp32 precision.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python -u iterative_train.py --model_name EleutherAI/pythia-410m --data_dir data/wikitext103_5k --synthetic_ratio 0.75 --num_generations 10 --steps_per_gen 5000 --output_dir results/alpha_sweep/a075_s42_fp32 --seed 42 --batch_size 4 --max_length 512 --lr 5e-5 --gen_max_new_tokens 256 --gen_batch_size 16 --top_p 0.95 --optim adamw_torch 2>&1 | tee /root/runs/distrib_canary_collapse/alpha_sweep_a075_s42_fp32.log\\\"\", \"server\": \"westd-17855\", \"gpu\": [\"cuda:5\"], \"pid\": \"121667\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a075_s42_fp32.log\", \"submitted_at\": \"2026-05-19T09:33:47.560Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/wikitext103_5k\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 42, \"precision\": \"fp32\", \"padding_side_fix\": \"D093 applied\"}, \"metrics\": {\"partial\": true, \"n_generations_completed\": 4, \"n_generations_planned\": 10, \"note\": \"Partial metrics from first run (gen 4 crash). Restarted with --start_gen 4 + TRANSFORMERS_OFFLINE=1, now at gen 7/10. Will be overwritten on completion.\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T13:51:04.701Z\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.457}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-19T14:24:36.321805+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "alpha_sweep_a075_s42_fp32",
  "field": "status",
  "value": "DONE",
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "alpha_sweep_a075_s42_fp32",
    "field": "status",
    "value": "DONE",
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T14:24:36.321982+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 0.461}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-19T14:24:36.322114+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "alpha_sweep_a075_s42_fp32",
  "field": "conclusion",
  "value": "success",
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "alpha_sweep_a075_s42_fp32",
    "field": "conclusion",
    "value": "success",
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T14:24:36.322297+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"alpha_sweep_a075_s42_fp32\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T06:18:30.958Z\", \"updated_at\": \"2026-05-19T14:23:38.229Z\", \"hypothesis\": \"α=0.75 pre-D080 was fp16; fp32 rerun provides D079-compliant authoritative data. PermG expected ~83% (high regime), drift magnitude may change with fp32 precision.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python -u iterative_train.py --model_name EleutherAI/pythia-410m --data_dir data/wikitext103_5k --synthetic_ratio 0.75 --num_generations 10 --steps_per_gen 5000 --output_dir results/alpha_sweep/a075_s42_fp32 --seed 42 --batch_size 4 --max_length 512 --lr 5e-5 --gen_max_new_tokens 256 --gen_batch_size 16 --top_p 0.95 --optim adamw_torch 2>&1 | tee /root/runs/distrib_canary_collapse/alpha_sweep_a075_s42_fp32.log\\\"\", \"server\": \"westd-17855\", \"gpu\": [\"cuda:5\"], \"pid\": \"121667\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a075_s42_fp32.log\", \"submitted_at\": \"2026-05-19T09:33:47.560Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/wikitext103_5k\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 42, \"precision\": \"fp32\", \"padding_side_fix\": \"D093 applied\"}, \"metrics\": {\"partial\": true, \"n_generations_completed\": 4, \"n_generations_planned\": 10, \"note\": \"Partial metrics from first run (gen 4 crash). Restarted with --start_gen 4 + TRANSFORMERS_OFFLINE=1, now at gen 7/10. Will be overwritten on completion.\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T13:51:04.701Z\"}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.473}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-19T14:24:36.322460+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "alpha_sweep_a075_s42_fp32",
  "field": "status",
  "value": "DONE",
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "alpha_sweep_a075_s42_fp32",
    "field": "status",
    "value": "DONE",
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T14:24:36.322584+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without output fields: ['checkpoint_path']. Set these fields first or pass them in spec.\", \"metadata\": {\"elapsed_seconds\": 0.3425}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-19T14:24:36.322714+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "alpha_sweep_a075_s42_fp32",
  "field": "metrics",
  "value": "{'n_generations': 11, 'gen0': {'token_entropy': 3.2342, 'ece': 0.0108, 'perplexity': 26.949, 'distinct_1': 0.098, 'distinct_2': 0.5141, 'distinct_3': 0.8127, 'effective_rank': 46.613, 'mauve': 0.0311}, 'gen10': {'token_entropy': 2.283, 'ece': 0.2145, 'perplexity': 77.697, 'distinct_1': 0.0731, 'distinct_2': 0.357, 'distinct_3': 0.5957, 'effective_rank': 78.06, 'mauve': 0.0299}, 'drift_pct': {'token_entropy': -29.41, 'ece': 1885.41, 'perplexity': 188.31, 'distinct_1': -25.38, 'distinct_2': -30.55, 'distinct_3': -26.7, 'effective_rank': 67.47, 'mauve': -3.73}, 'lead_lag': {'PermG_fwd': '6/8', 'PermG_rev': '0/8', 'K_ge_4': '6/8', 'MMCT_detection': 0.75, 'TY_granger': '8/8', 'naive_xcorr': '7/8', 'diff_xcorr': '6/8', 'threshold_onset': '8/8'}, 'asymmetry': 'strong (fwd=6, rev=0)'}",
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "alpha_sweep_a075_s42_fp32",
    "field": "metrics",
    "value": "{'n_generations': 11, 'gen0': {'token_entropy': 3.2342, 'ece': 0.0108, 'perplexity': 26.949, 'distinct_1': 0.098, 'distinct_2': 0.5141, 'distinct_3': 0.8127, 'effective_rank': 46.613, 'mauve': 0.0311}, 'gen10': {'token_entropy': 2.283, 'ece': 0.2145, 'perplexity': 77.697, 'distinct_1': 0.0731, 'distinct_2': 0.357, 'distinct_3': 0.5957, 'effective_rank': 78.06, 'mauve': 0.0299}, 'drift_pct': {'token_entropy': -29.41, 'ece': 1885.41, 'perplexity': 188.31, 'distinct_1': -25.38, 'distinct_2': -30.55, 'distinct_3': -26.7, 'effective_rank': 67.47, 'mauve': -3.73}, 'lead_lag': {'PermG_fwd': '6/8', 'PermG_rev': '0/8', 'K_ge_4': '6/8', 'MMCT_detection': 0.75, 'TY_granger': '8/8', 'naive_xcorr': '7/8', 'diff_xcorr': '6/8', 'threshold_onset': '8/8'}, 'asymmetry': 'strong (fwd=6, rev=0)'}",
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T14:24:36.322918+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"alpha_sweep_a075_s42_fp32\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T06:18:30.958Z\", \"updated_at\": \"2026-05-19T14:23:46.724Z\", \"hypothesis\": \"α=0.75 pre-D080 was fp16; fp32 rerun provides D079-compliant authoritative data. PermG expected ~83% (high regime), drift magnitude may change with fp32 precision.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python -u iterative_train.py --model_name EleutherAI/pythia-410m --data_dir data/wikitext103_5k --synthetic_ratio 0.75 --num_generations 10 --steps_per_gen 5000 --output_dir results/alpha_sweep/a075_s42_fp32 --seed 42 --batch_size 4 --max_length 512 --lr 5e-5 --gen_max_new_tokens 256 --gen_batch_size 16 --top_p 0.95 --optim adamw_torch 2>&1 | tee /root/runs/distrib_canary_collapse/alpha_sweep_a075_s42_fp32.log\\\"\", \"server\": \"westd-17855\", \"gpu\": [\"cuda:5\"], \"pid\": \"121667\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a075_s42_fp32.log\", \"submitted_at\": \"2026-05-19T09:33:47.560Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/wikitext103_5k\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 42, \"precision\": \"fp32\", \"padding_side_fix\": \"D093 applied\"}, \"metrics\": {\"n_generations\": 11, \"gen0\": {\"token_entropy\": 3.2342, \"ece\": 0.0108, \"perplexity\": 26.949, \"distinct_1\": 0.098, \"distinct_2\": 0.5141, \"distinct_3\": 0.8127, \"effective_rank\": 46.613, \"mauve\": 0.0311}, \"gen10\": {\"token_entropy\": 2.283, \"ece\": 0.2145, \"perplexity\": 77.697, \"distinct_1\": 0.0731, \"distinct_2\": 0.357, \"distinct_3\": 0.5957, \"effective_rank\": 78.06, \"mauve\": 0.0299}, \"drift_pct\": {\"token_entropy\": -29.41, \"ece\": 1885.41, \"perplexity\": 188.31, \
…[truncated 534 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-19T14:24:36.323066+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "alpha_sweep_a075_s42_fp32",
  "field": "checkpoint_path",
  "value": "results/alpha_sweep/a075_s42_fp32/gen_10/checkpoint",
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "alpha_sweep_a075_s42_fp32",
    "field": "checkpoint_path",
    "value": "results/alpha_sweep/a075_s42_fp32/gen_10/checkpoint",
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T14:24:36.323234+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"alpha_sweep_a075_s42_fp32\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T06:18:30.958Z\", \"updated_at\": \"2026-05-19T14:23:50.500Z\", \"hypothesis\": \"α=0.75 pre-D080 was fp16; fp32 rerun provides D079-compliant authoritative data. PermG expected ~83% (high regime), drift magnitude may change with fp32 precision.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python -u iterative_train.py --model_name EleutherAI/pythia-410m --data_dir data/wikitext103_5k --synthetic_ratio 0.75 --num_generations 10 --steps_per_gen 5000 --output_dir results/alpha_sweep/a075_s42_fp32 --seed 42 --batch_size 4 --max_length 512 --lr 5e-5 --gen_max_new_tokens 256 --gen_batch_size 16 --top_p 0.95 --optim adamw_torch 2>&1 | tee /root/runs/distrib_canary_collapse/alpha_sweep_a075_s42_fp32.log\\\"\", \"server\": \"westd-17855\", \"gpu\": [\"cuda:5\"], \"pid\": \"121667\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a075_s42_fp32.log\", \"submitted_at\": \"2026-05-19T09:33:47.560Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/wikitext103_5k\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 42, \"precision\": \"fp32\", \"padding_side_fix\": \"D093 applied\"}, \"metrics\": {\"n_generations\": 11, \"gen0\": {\"token_entropy\": 3.2342, \"ece\": 0.0108, \"perplexity\": 26.949, \"distinct_1\": 0.098, \"distinct_2\": 0.5141, \"distinct_3\": 0.8127, \"effective_rank\": 46.613, \"mauve\": 0.0311}, \"gen10\": {\"token_entropy\": 2.283, \"ece\": 0.2145, \"perplexity\": 77.697, \"distinct_1\": 0.0731, \"distinct_2\": 0.357, \"distinct_3\": 0.5957, \"effective_rank\": 78.06, \"mauve\": 0.0299}, \"drift_pct\": {\"token_entropy\": -29.41, \"ece\": 1885.41, \"perplexity\": 188.31, \
…[truncated 612 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-19T14:24:36.323426+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "alpha_sweep_a075_s42_fp32",
  "field": "log_path",
  "value": "~/runs/distrib_canary_collapse/alpha_sweep_a075_s42_fp32.log",
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "alpha_sweep_a075_s42_fp32",
    "field": "log_path",
    "value": "~/runs/distrib_canary_collapse/alpha_sweep_a075_s42_fp32.log",
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-19T14:24:36.323603+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"alpha_sweep_a075_s42_fp32\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T06:18:30.958Z\", \"updated_at\": \"2026-05-19T14:23:51.450Z\", \"hypothesis\": \"α=0.75 pre-D080 was fp16; fp32 rerun provides D079-compliant authoritative data. PermG expected ~83% (high regime), drift magnitude may change with fp32 precision.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python -u iterative_train.py --model_name EleutherAI/pythia-410m --data_dir data/wikitext103_5k --synthetic_ratio 0.75 --num_generations 10 --steps_per_gen 5000 --output_dir results/alpha_sweep/a075_s42_fp32 --seed 42 --batch_size 4 --max_length 512 --lr 5e-5 --gen_max_new_tokens 256 --gen_batch_size 16 --top_p 0.95 --optim adamw_torch 2>&1 | tee /root/runs/distrib_canary_collapse/alpha_sweep_a075_s42_fp32.log\\\"\", \"server\": \"westd-17855\", \"gpu\": [\"cuda:5\"], \"pid\": \"121667\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a075_s42_fp32.log\", \"submitted_at\": \"2026-05-19T09:33:47.560Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/wikitext103_5k\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 42, \"precision\": \"fp32\", \"padding_side_fix\": \"D093 applied\"}, \"metrics\": {\"n_generations\": 11, \"gen0\": {\"token_entropy\": 3.2342, \"ece\": 0.0108, \"perplexity\": 26.949, \"distinct_1\": 0.098, \"distinct_2\": 0.5141, \"distinct_3\": 0.8127, \"effective_rank\": 46.613, \"mauve\": 0.0311}, \"gen10\": {\"token_entropy\": 2.283, \"ece\": 0.2145, \"perplexity\": 77.697, \"distinct_1\": 0.0731, \"distinct_2\": 0.357, \"distinct_3\": 0.5957, \"effective_rank\": 78.06, \"mauve\": 0.0299}, \"drift_pct\": {\"token_entropy\": -29.41, \"ece\": 1885.41, \"perplexity\": 188.31, \
…[truncated 692 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-19T14:24:36.323751+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "alpha_sweep_a075_s42_fp32",
  "field": "status",
  "value": "DONE",
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "alpha_sweep_a075_s42_fp32",
    "field": "status",
    "value": "DONE",
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-19T14:24:36.323960+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"alpha_sweep_a075_s42_fp32\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T06:18:30.958Z\", \"updated_at\": \"2026-05-19T14:23:55.350Z\", \"hypothesis\": \"α=0.75 pre-D080 was fp16; fp32 rerun provides D079-compliant authoritative data. PermG expected ~83% (high regime), drift magnitude may change with fp32 precision.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python -u iterative_train.py --model_name EleutherAI/pythia-410m --data_dir data/wikitext103_5k --synthetic_ratio 0.75 --num_generations 10 --steps_per_gen 5000 --output_dir results/alpha_sweep/a075_s42_fp32 --seed 42 --batch_size 4 --max_length 512 --lr 5e-5 --gen_max_new_tokens 256 --gen_batch_size 16 --top_p 0.95 --optim adamw_torch 2>&1 | tee /root/runs/distrib_canary_collapse/alpha_sweep_a075_s42_fp32.log\\\"\", \"server\": \"westd-17855\", \"gpu\": [\"cuda:5\"], \"pid\": \"121667\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a075_s42_fp32.log\", \"submitted_at\": \"2026-05-19T09:33:47.560Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/wikitext103_5k\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 42, \"precision\": \"fp32\", \"padding_side_fix\": \"D093 applied\", \"wall_clock_seconds\": 17407.8, \"gpu_hours\": 4.84}, \"metrics\": {\"n_generations\": 11, \"gen0\": {\"token_entropy\": 3.2342, \"ece\": 0.0108, \"perplexity\": 26.949, \"distinct_1\": 0.098, \"distinct_2\": 0.5141, \"distinct_3\": 0.8127, \"effective_rank\": 46.613, \"mauve\": 0.0311}, \"gen10\": {\"token_entropy\": 2.283, \"ece\": 0.2145, \"perplexity\": 77.697, \"distinct_1\": 0.0731, \"distinct_2\": 0.357, \"distinct_3\": 0.5957, \"effective_rank\": 78.06, \"mauve\": 0.0299}, \"drift_pct\": {\"token_entropy\": -2
…[truncated 840 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-19T14:24:36.324232+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "alpha_sweep_a075_s42_fp32_analysis",
  "type": "report",
  "description": "Full analysis of α=0.75 fp32 seed=42 experiment: drift metrics, 5-method lead-lag, K≥4 consensus, dose-response comparison",
  "project": "distrib_canary_collapse",
  "exp_id": "alpha_sweep_a075_s42_fp32",
  "content_filename": "alpha_sweep_a075_s42_fp32_analysis.md",
  "content": "# Analysis: alpha_sweep_a075_s42_fp32\n\n**Date:** 2026-05-19  \n**Model:** EleutherAI/pythia-410m | **Seed:** 42 | **α:** 0.75 | **Precision:** fp32  \n**Generations:** 11 (gen_0–gen_10) | **Server:** westd-17855 | **Wall-clock:** ~4.84 GPU-hours  \n**Config:** left-padding (D093), 5000 steps/gen, lr=5e-5, top_p=0.95\n\n## 1. Drift Summary (gen_0 → gen_10)\n\n| Metric | gen_0 | gen_10 | Drift % |\n|--------|-------|--------|---------|\n| token_entropy | 3.2342 | 2.2830 | **−29.41%** |\n| ece | 0.0108 | 0.2145 | **+1885.41%** |\n| perplexity | 26.949 | 77.697 | **+188.31%** |\n| distinct_1 | 0.0980 | 0.0731 | **−25.38%** |\n| distinct_2 | 0.5141 | 0.3570 | **−30.55%** |\n| distinct_3 | 0.8127 | 0.5957 | **−26.70%** |\n| effective_rank | 46.613 | 78.060 | **+67.47%** |\n| mauve | 0.0311 | 0.0299 | **−3.73%** |\n\nCollapse pattern clear: entropy ↓, calibration (ECE) degrades massively, perplexity nearly triples, diversity (distinct-n) drops ~25-30%. MAUVE near-flat (already low baseline at 0.03).\n\n## 2. Lead-Lag Analysis (5-Method)\n\n| Method | Sig/Total |\n|--------|-----------|\n| naive_xcorr | 7/8 |\n| diff_xcorr | 6/8 |\n| threshold_onset | 8/8 |\n| perm_granger_fwd | **6/8** |\n| perm_granger_rev | **0/8** |\n| ty_granger | 8/8 |\n| **K≥4 consensus** | **6/8** |\n| MMCT detection | **75%** |\n\n**PermG asymmetry: fwd=6, rev=0** — strong unidirectional canary→downstream signal.\n\n## 3. Pair-Level Consensus\n\n| Pair | Votes | K≥4 | Methods |\n|------|-------|------|---------|\n| token_entropy→distinct_1 | 5/5 | ✓ | naive, diff, thresh, pg_fwd, ty |\n| token_entropy→distinct_2 | 5/5 | ✓ | naive, diff, thresh, pg_fwd, ty |\n| token_entropy→distinct_3 | 5/5 | ✓ | naive, diff, thresh, pg_fwd, ty |\n| token_entropy→mauve | 2/5 | ✗ | thresh, ty |\n| ece→distinct_1 | 5/5 | ✓ | naive, diff, thresh, pg_fwd, ty |\n| ece→distinct_2 | 5/5 | ✓ | naive, diff, thresh, pg_fwd, ty |\n| ece→distinct_3 | 5/5 | ✓ | naive, diff, thresh, pg_fwd, ty |\n| ece→mauve | 3/5 | ✗ | naive, thresh, ty |\n\n6/8 pairs reach K≥4. The 2 failing pairs are both →mauve, explained by MAUVE's near-flat trajectory (−3.73% drift).\n\n## 4. Dose-Response Comparison\n\n| α | PermG fwd | K≥4 | MMCT | Regime |\n|---|-----------|------|------|--------|\n| 0.50 fp32 | 6/8 | 6/8 | 6/8 | mid-high |\n| 0.60 fp32 | 3/8 | 7/8 | 7/8 | mid |\n| **0.75 fp32** | **6/8** | **6/8** | **75%** | **high** |\n| 1.00 fp32 | ~75% | ~6.5/8 | — | high |\n\nα=0.75 fits the high-regime bracket. PermG at 75% (6/8) is slightly below the hypothesized ~83% but within expected single-seed variance. K≥4 and MMCT are consistent with dose-response expectations.\n\n## 5. TY Granger Note\n\nTY shows 8/8 significant. α=0.75 > 0.50 threshold (C003 compliant). Most pairs have d_max=0, df_resid=7 (well-conditioned). Exception: ece→mauve has d_max=2, df_resid=1 — borderline but not flagged since the pair fails K≥4 anyway.\n\n## 6. Conclusion\n\n**SUCCESS.** α=0.75 fp32 confirms high-regime canary lead-lag behavior with D079-compliant fp32 precision. Key findings:\n- Strong collapse (ppl +188%, ECE +1885%, entropy −29%)\n- Robust lead-lag: PermG 6/8 fwd, 0/8 rev (perfect asymmetry)\n- K≥4 consensus 6/8, consistent with dose-response curve\n- MAUVE pairs are the sole non-significant pairs due to flat MAUVE trajectory\n",
  "tags": "['alpha_sweep', 'fp32', 'lead-lag', 'dose-response', 'D079']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "alpha_sweep_a075_s42_fp32_analysis",
    "type": "report",
    "description": "Full analysis of α=0.75 fp32 seed=42 experiment: drift metrics, 5-method lead-lag, K≥4 consensus, dose-response comparison",
    "project": "distrib_canary_collapse",
    "exp_id": "alpha_sweep_a075_s42_fp32",
    "content_filename": "alpha_sweep_a075_s42_fp32_analysis.md",
    "content": "# Analysis: alpha_sweep_a075_s42_fp32\n\n**Date:** 2026-05-19  \n**Model:** EleutherAI/pythia-410m | **Seed:** 42 | **α:** 0.75 | **Precision:** fp32  \n**Generations:** 11 (gen_0–gen_10) | **Server:** westd-17855 | **Wall-clock:** ~4.84 GPU-hours  \n**Config:** left-padding (D093), 5000 steps/gen, lr=5e-5, top_p=0.95\n\n## 1. Drift Summary (gen_0 → gen_10)\n\n| Metric | gen_0 | gen_10 | Drift % |\n|--------|-------|--------|---------|\n| token_entropy | 3.2342 | 2.2830 | **−29.41%** |\n| ece | 0.0108 | 0.2145 | **+1885.41%** |\n| perplexity | 26.949 | 77.697 | **+188.31%** |\n| distinct_1 | 0.0980 | 0.0731 | **−25.38%** |\n| distinct_2 | 0.5141 | 0.3570 | **−30.55%** |\n| distinct_3 | 0.8127 | 0.5957 | **−26.70%** |\n| effective_rank | 46.613 | 78.060 | **+67.47%** |\n| mauve | 0.0311 | 0.0299 | **−3.73%** |\n\nCollapse pattern clear: entropy ↓, calibration (ECE) degrades massively, perplexity nearly triples, diversity (distinct-n) drops ~25-30%. MAUVE near-flat (already low baseline at 0.03).\n\n## 2. Lead-Lag Analysis (5-Method)\n\n| Method | Sig/Total |\n|--------|-----------|\n| naive_xcorr | 7/8 |\n| diff_xcorr | 6/8 |\n| threshold_onset | 8/8 |\n| perm_granger_fwd | **6/8** |\n| perm_granger_rev | **0/8** |\n| ty_granger | 8/8 |\n| **K≥4 consensus** | **6/8** |\n| MMCT detection | **75%** |\n\n**PermG asymmetry: fwd=6, rev=0** — strong unidirectional canary→downstream signal.\n\n## 3. Pair-Level Consensus\n\n| Pair | Votes | K≥4 | Methods |\n|------|-------|------|---------|\n| token_entropy→distinct_1 | 5/5 | ✓ | naive, diff, thresh, pg_fwd, ty |\n| token_entropy→distinct_2 | 5/5 | ✓ | naive, diff, thresh, pg_fwd, ty |\n| token_entropy→distinct_3 | 5/5 | ✓ | naive, diff, thresh, pg_fwd, ty |\n| token_entropy→mauve | 2/5 | ✗ | thresh, ty |\n| ece→distinct_1 | 5/5 | ✓ | naive, diff, thresh, pg_fwd, ty |\n| ece→distinct_2 | 5/5 | ✓ | naive, diff, thresh, pg_fwd, ty |\n| ece→distinct_3 | 5/5 | ✓ | naive, diff, thresh, pg_fwd, ty |\n| ece→mauve | 3/5 | ✗ | naive, thresh, ty |\n\n6/8 pairs reach K≥4. The 2 failing pairs are both →mauve, explained by MAUVE's near-flat trajectory (−3.73% drift).\n\n## 4. Dose-Response Comparison\n\n| α | PermG fwd | K≥4 | MMCT | Regime |\n|---|-----------|------|------|--------|\n| 0.50 fp32 | 6/8 | 6/8 | 6/8 | mid-high |\n| 0.60 fp32 | 3/8 | 7/8 | 7/8 | mid |\n| **0.75 fp32** | **6/8** | **6/8** | **75%** | **high** |\n| 1.00 fp32 | ~75% | ~6.5/8 | — | high |\n\nα=0.75 fits the high-regime bracket. PermG at 75% (6/8) is slightly below the hypothesized ~83% but within expected single-seed variance. K≥4 and MMCT are consistent with dose-response expectations.\n\n## 5. TY Granger Note\n\nTY shows 8/8 significant. α=0.75 > 0.50 threshold (C003 compliant). Most pairs have d_max=0, df_resid=7 (well-conditioned). Exception: ece→mauve has d_max=2, df_resid=1 — borderline but not flagged since the pair fails K≥4 anyway.\n\n## 6. Conclusion\n\n**SUCCESS.** α=0.75 fp32 confirms high-regime canary lead-lag behavior with D079-compliant fp32 precision. Key findings:\n- Strong collapse (ppl +188%, ECE +1885%, entropy −29%)\n- Robust lead-lag: PermG 6/8 fwd, 0/8 rev (perfect asymmetry)\n- K≥4 consensus 6/8, consistent with dose-response curve\n- MAUVE pairs are the sole non-significant pairs due to flat MAUVE trajectory\n",
    "tags": "['alpha_sweep', 'fp32', 'lead-lag', 'dose-response', 'D079']"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-19T14:24:36.324538+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_7d0a70\", \"name\": \"alpha_sweep_a075_s42_fp32_analysis\", \"type\": \"report\", \"description\": \"Full analysis of α=0.75 fp32 seed=42 experiment: drift metrics, 5-method lead-lag, K≥4 consensus, dose-response comparison\", \"path\": \"projects/distrib_canary_collapse/artifacts/alpha_sweep_a075_s42_fp32/report/alpha_sweep_a075_s42_fp32_analysis.md\", \"url\": null, \"project\": \"distrib_canary_collapse\", \"exp_id\": \"alpha_sweep_a075_s42_fp32\", \"skill\": \"\", \"created_at\": \"2026-05-19T14:24:26.086497+00:00\", \"tags\": [\"alpha_sweep\", \"fp32\", \"lead-lag\", \"dose-response\", \"D079\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-19T14:24:36.324726+00:00_

分析完成。汇总：

## alpha_sweep_a075_s42_fp32 — SUCCESS

**Drift (gen_0→gen_10):**
| Metric | Drift |
|--------|-------|
| token_entropy | −29.4% |
| ECE | +1885% |
| perplexity | +188% |
| distinct_1/2/3 | −25~31% |
| effective_rank | +67.5% |
| mauve | −3.7% (near-flat) |

**Lead-Lag:**
- **PermG: 6/8 fwd, 0/8 rev** — perfect asymmetry
- **K≥4 consensus: 6/8** — 6 pairs with 5/5 unanimous agreement (all canary→distinct-n)
- **MMCT detection: 75%**
- TY Granger: 8/8 (C003 compliant, α=0.75 > 0.50)

**Dose-response:** α=0.75 fits high regime。PermG=75% 略低于预期的 ~83% 但在单 seed 方差范围内。唯二未通过 K≥4 的 pair 都是 →mauve（MAUVE 仅 −3.73% drift，信号不足）。

Registry 已更新为 DONE/success，artifact 已注册 (`art_20260519_7d0a70`)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_alpha_sweep_a075_s42_fp32_20260519T142135"
}
```

</details>

---
