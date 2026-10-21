# analysis alpha sweep a050 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 57
- **Recorded user turns:** 0
- **Tool calls:** 28
- **Original source:** `logs/chats/worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331.jsonl`
- **Structured JSON:** [`3932428fcd1edbc1c7f8.json`](../../sessions/39/3932428fcd1edbc1c7f8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

57 recorded events

### Tool call

_source line 1 · 2026-05-19T10:06:16.339352+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T10:06:16.339628+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T10:06:16.339796+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'alpha_sweep_a050_s42_fp32'}",
  "project": "distrib_canary_collapse",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'alpha_sweep_a050_s42_fp32'}",
    "project": "distrib_canary_collapse",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T10:06:16.339952+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4582}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T10:06:16.340080+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "tail -200 ~/runs/distrib_canary_collapse/alpha_sweep_a050_s42_fp32.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "tail -200 ~/runs/distrib_canary_collapse/alpha_sweep_a050_s42_fp32.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-19T10:06:16.340201+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "ls -la ~/runs/distrib_canary_collapse/alpha_sweep_a050_s42_fp32*/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "ls -la ~/runs/distrib_canary_collapse/alpha_sweep_a050_s42_fp32*/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T10:06:16.340359+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "ls -la /root/autodl-tmp/distrib_canary_collapse/results/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "ls -la /root/autodl-tmp/distrib_canary_collapse/results/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T10:06:16.340559+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[transformers] A decoder-only architecture is being used, but right-padding was detected! For correct generation results, please set `padding_side='left'` when initializing the tokenizer.\\n[transformers] A decoder-only architecture is being used, but right-padding was detected! For correct generation results, please set `padding_side='left'` when initializing the tokenizer.\\n[transformers] A decoder-only architecture is being used, but right-padding was detected! For correct generation results, please set `padding_side='left'` when initializing the tokenizer.\\n[transformers] A decoder-only architecture is being used, but right-padding was detected! For correct generation results, please set `padding_side='left'` when initializing the tokenizer.\\n[transformers] A decoder-only architecture is being used, but right-padding was detected! For correct generation results, please set `padding_side='left'` when initializing the tokenizer.\\n[transformers] A decoder-only architecture is being used, but right-padding was detected! For correct generation results, please set `padding_side='left'` when initializing the tokenizer.\\n[transformers] A decoder-only architecture is being used, but right-padding was detected! For correct generation results, please set `padding_side='left'` when initializing the tokenizer.\\n[transformers] A decoder-only architecture is being used, but right-padding was detected! For correct generation results, please set `padding_side='left'` when initializing the tokenizer.\\n[transformers] A decoder-only architecture is being used, but right-padding was detected! For correct generation results, please set `padding_side='left'` when initializing the tokenizer.\\n[transformers] A decoder-only architecture is being used, but right-padding was detected! For correct generation results, please set `padding_side='left'` when initializing the tokenizer.\\n[transformers] A decoder-only architecture i
…[truncated 6369 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-19T10:06:16.340721+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/runs/distrib_canary_collapse/alpha_sweep_a050_s42_fp32*/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T10:06:16.340852+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 12\\ndrwxr-xr-x  8 root root  147 May 19 01:58 .\\ndrwxr-xr-x 13 root root 4096 May 19 12:51 ..\\ndrwxr-xr-x 22 root root 4096 May 19 17:55 alpha_sweep\\ndrwxr-xr-x  4 root root   55 May 19 01:26 alpha_sweep_c4\\ndrwxr-xr-x  2 root root   10 May 19 02:03 dry_run\\ndrwxr-xr-x  6 root root  158 May 19 08:29 generalize\\ndrwxr-xr-x  9 root root 4096 May 19 08:23 intervention\\ndrwxr-xr-x  4 root root   80 May 19 02:03 scale_check\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T10:06:16.341008+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/all_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/all_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T10:06:16.341229+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"token_entropy\\\": 3.23419483150593,\\n    \\\"self_bleu\\\": 0.010359298948078572,\\n    \\\"ece\\\": 0.010804557477709054,\\n    \\\"effective_rank\\\": 46.612774691899155,\\n    \\\"perplexity\\\": 26.948958972544652,\\n    \\\"distinct_1\\\": 0.09162095491577137,\\n    \\\"distinct_2\\\": 0.5038422526068081,\\n    \\\"distinct_3\\\": 0.8318077803203662,\\n    \\\"mauve\\\": 0.027018479627034072,\\n    \\\"generation\\\": 0,\\n    \\\"intervention_triggered\\\": false,\\n    \\\"trigger_gen\\\": null,\\n    \\\"effective_alpha\\\": 0.5\\n  },\\n  {\\n    \\\"token_entropy\\\": 2.513125962738291,\\n    \\\"self_bleu\\\": 0.010555916086494104,\\n    \\\"ece\\\": 0.07049489540865364,\\n    \\\"effective_rank\\\": 57.234269752802376,\\n    \\\"perplexity\\\": 23.363054161988806,\\n    \\\"distinct_1\\\": 0.09102786749549609,\\n    \\\"distinct_2\\\": 0.4993142625278961,\\n    \\\"distinct_3\\\": 0.8310637538141921,\\n    \\\"mauve\\\": 0.02764599057188057,\\n    \\\"generation\\\": 1,\\n    \\\"intervention_triggered\\\": false,\\n    \\\"trigger_gen\\\": null,\\n    \\\"effective_alpha\\\": 0.5\\n  },\\n  {\\n    \\\"token_entropy\\\": 2.5109620436644615,\\n    \\\"self_bleu\\\": 0.011337873687615017,\\n    \\\"ece\\\": 0.083974302532681,\\n    \\\"effective_rank\\\": 61.79724632725394,\\n    \\\"perplexity\\\": 26.685836557085626,\\n    \\\"distinct_1\\\": 0.0750859375,\\n    \\\"distinct_2\\\": 0.41557355916843103,\\n    \\\"distinct_3\\\": 0.763324426944171,\\n    \\\"mauve\\\": 0.026422088378369776,\\n    \\\"generation\\\": 2,\\n    \\\"intervention_triggered\\\": false,\\n    \\\"trigger_gen\\\": null,\\n    \\\"effective_alpha\\\": 0.5\\n  },\\n  {\\n    \\\"token_entropy\\\": 2.581628010409094,\\n    \\\"self_bleu\\\": 0.012628074196452673,\\n    \\\"ece\\\": 0.08206379750573295,\\n    \\\"effective_rank\\\": 62.59530155888269,\\n    \\\"perplexity\\\": 27.5971017491973,\\n    \\\"dist
…[truncated 4328 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T10:06:16.341409+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'alpha_sweep_a050_s42_fp32'}",
  "project": "distrib_canary_collapse",
  "fields": "['*']",
  "limit": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'alpha_sweep_a050_s42_fp32'}",
    "project": "distrib_canary_collapse",
    "fields": "['*']",
    "limit": "1"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T10:06:16.341541+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2724}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T10:06:16.341658+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "ls -la /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "ls -la /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T10:06:16.341787+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 40\\ndrwxr-xr-x 14 root root  4096 May 19 18:03 .\\ndrwxr-xr-x 22 root root  4096 May 19 17:55 ..\\n-rw-r--r--  1 root root     2 May 19 17:47 EXIT_CODE\\n-rw-r--r--  1 root root  4978 May 19 17:47 all_metrics.json\\ndrwxr-xr-x  2 root root    42 May 19 18:03 analysis\\n-rw-r--r--  1 root root 13863 May 19 17:59 analysis_results.json\\n-rw-r--r--  1 root root   636 May 19 13:31 config.json\\ndrwxr-xr-x  3 root root    60 May 19 13:43 gen_0\\ndrwxr-xr-x  4 root root    79 May 19 14:52 gen_1\\ndrwxr-xr-x  5 root root   101 May 19 17:47 gen_10\\ndrwxr-xr-x  4 root root    79 May 19 15:17 gen_2\\ndrwxr-xr-x  4 root root    79 May 19 15:42 gen_3\\ndrwxr-xr-x  4 root root    79 May 19 16:07 gen_4\\ndrwxr-xr-x  4 root root    79 May 19 16:32 gen_5\\ndrwxr-xr-x  4 root root    79 May 19 16:56 gen_6\\ndrwxr-xr-x  4 root root    79 May 19 17:21 gen_7\\ndrwxr-xr-x  4 root root    79 May 19 17:46 gen_8\\ndrwxr-xr-x  5 root root   101 May 19 17:22 gen_9\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T10:06:16.341943+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/analysis_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/analysis_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T10:06:16.342354+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"exp_dir\\\": \\\"results/alpha_sweep/a050_s42_fp32\\\",\\n  \\\"n_generations\\\": 11,\\n  \\\"drift_pct\\\": {\\n    \\\"token_entropy\\\": -16.29,\\n    \\\"ece\\\": 703.39,\\n    \\\"perplexity\\\": 16.75,\\n    \\\"distinct_1\\\": -29.19,\\n    \\\"distinct_2\\\": -37.3,\\n    \\\"distinct_3\\\": -32.88,\\n    \\\"effective_rank\\\": 24.81,\\n    \\\"mauve\\\": -11.76\\n  },\\n  \\\"lead_lag\\\": {\\n    \\\"naive_xcorr\\\": {\\n      \\\"forward\\\": 8,\\n      \\\"total\\\": 8\\n    },\\n    \\\"diff_xcorr\\\": {\\n      \\\"forward\\\": 7,\\n      \\\"total\\\": 8\\n    },\\n    \\\"threshold_onset\\\": {\\n      \\\"forward\\\": 8,\\n      \\\"total\\\": 8\\n    },\\n    \\\"perm_granger_fwd\\\": {\\n      \\\"sig\\\": 6,\\n      \\\"total\\\": 8\\n    },\\n    \\\"perm_granger_rev\\\": {\\n      \\\"sig\\\": 0,\\n      \\\"total\\\": 8\\n    },\\n    \\\"ty_granger\\\": {\\n      \\\"sig\\\": 4,\\n      \\\"total\\\": 8\\n    },\\n    \\\"consensus_k4\\\": {\\n      \\\"sig\\\": 6,\\n      \\\"total\\\": 8\\n    }\\n  },\\n  \\\"mmct\\\": {\\n    \\\"mode\\\": \\\"weighted_pair_forward\\\",\\n    \\\"detection_rate\\\": 0.75,\\n    \\\"note\\\": \\\"simple_consensus_k4 (no null distribution)\\\"\\n  },\\n  \\\"consensus_detail\\\": [\\n    {\\n      \\\"pair\\\": \\\"token_entropy->distinct_1\\\",\\n      \\\"votes\\\": 4,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"thresh\\\",\\n        \\\"pg_fwd\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"token_entropy->distinct_2\\\",\\n      \\\"votes\\\": 5,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"thresh\\\",\\n        \\\"pg_fwd\\\",\\n        \\\"ty\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"token_entropy->distinct_3\\\",\\n      \\\"votes\\\": 5,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n      
…[truncated 8867 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T10:06:16.342544+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/analysis/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/analysis/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T10:06:16.342678+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"5method_leadlag.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T10:06:16.342798+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/ -name \"*.pt\" -o -name \"checkpoint*\" -type d",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/ -name \"*.pt\" -o -name \"checkpoint*\" -type d",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T10:06:16.342926+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/gen_9/checkpoint\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/gen_10/checkpoint\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T10:06:16.343044+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "distrib_canary_collapse",
  "fields": "['exp_id', 'status']",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "distrib_canary_collapse",
    "fields": "['exp_id', 'status']",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T10:06:16.343210+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"padding_robustness_a100_s42_fp32\": {\"status\": \"ALLOCATED\"}, \"alpha_sweep_a075_s42_fp32\": {\"status\": \"RUNNING\"}, \"alpha_sweep_a050_s43_fp32\": {\"status\": \"DONE\"}, \"alpha_sweep_a010_s42_fp32\": {\"status\": \"DONE\"}, \"alpha_sweep_a025_s43_fp32\": {\"status\": \"RUNNING\"}, \"alpha_sweep_a025_s44_fp32\": {\"status\": \"RUNNING\"}, \"alpha_sweep_a050_s44_fp32\": {\"status\": \"DONE\"}, \"alpha_sweep_a050_s42_fp32\": {\"status\": \"ANALYZING\"}, \"alpha_sweep_a025_s42_fp32\": {\"status\": \"RUNNING\"}, \"scale_69b_a100_s42\": {\"status\": \"DONE\"}, \"interv_pred_a075_s42_fp32_v4\": {\"status\": \"DONE\"}, \"alpha_sweep_a060_s42_fp32_v3\": {\"status\": \"DONE\"}, \"alpha_sweep_a005_s42_v3\": {\"status\": \"DONE\"}, \"alpha_sweep_a010_s43_fp32\": {\"status\": \"DONE\"}, \"alpha_sweep_a005_s42\": {\"status\": \"DONE\"}, \"alpha_sweep_a060_s42_fp32_v2\": {\"status\": \"DONE\"}, \"qwen35_08b_wiki_a100_s42_v2\": {\"status\": \"RUNNING\"}, \"smollm3_3b_wiki_a100_s42_v3\": {\"status\": \"RUNNING\"}, \"alpha_sweep_a010_s43\": {\"status\": \"DONE\"}, \"qwen35_08b_wiki_a100_s42\": {\"status\": \"DONE\"}, \"smollm3_3b_wiki_a100_s42_v2\": {\"status\": \"DONE\"}, \"interv_pred_a075_s42_fp32\": {\"status\": \"DONE\"}, \"alpha_sweep_a060_s42_fp32\": {\"status\": \"DONE\"}, \"gen_gpt2m_a100_s43_fp32\": {\"status\": \"RUNNING\"}, \"scale_14b_a050_s42\": {\"status\": \"DONE\"}, \"conditional_granger_d061\": {\"status\": \"DONE\"}, \"method_ablation_phase3\": {\"status\": \"DONE\"}, \"interv_pred_a075_s42_fp32_v2\": {\"status\": \"DONE\"}, \"interv_pred_s43_bf16\": {\"status\": \"DONE\"}, \"smollm3_3b_wiki_a100_s42\": {\"status\": \"DONE\"}, \"interv_react_s43_bf16\": {\"status\": \"DONE\"}, \"gen_gpt2m_a100_s43_bf16\": {\"status\": \"DONE\"}, \"interv_pred_a075_s42\": {\"status\": \"PREPARING\"}, \"qwen35_dryrun_launch\": {\"status\": \"PREPARING\"}, \"alpha_sweep_a060_s42_bf16\": {\"status\": \"DONE\"}, \"al
…[truncated 946 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T10:06:16.343409+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/config.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/config.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-19T10:06:16.343541+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "grep -c \"right-padding was detected\" ~/runs/distrib_canary_collapse/alpha_sweep_a050_s42_fp32.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "grep -c \"right-padding was detected\" ~/runs/distrib_canary_collapse/alpha_sweep_a050_s42_fp32.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-19T10:06:16.343685+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\",\\n  \\\"data_dir\\\": \\\"data/wikitext103_5k\\\",\\n  \\\"dataset\\\": \\\"wikitext-103-v1\\\",\\n  \\\"synthetic_ratio\\\": 0.5,\\n  \\\"num_generations\\\": 10,\\n  \\\"steps_per_gen\\\": 5000,\\n  \\\"output_dir\\\": \\\"results/alpha_sweep/a050_s42_fp32\\\",\\n  \\\"seed\\\": 42,\\n  \\\"batch_size\\\": 4,\\n  \\\"max_length\\\": 512,\\n  \\\"lr\\\": 5e-05,\\n  \\\"gen_max_new_tokens\\\": 256,\\n  \\\"gen_batch_size\\\": 16,\\n  \\\"top_p\\\": 0.95,\\n  \\\"accumulate\\\": false,\\n  \\\"start_gen\\\": 0,\\n  \\\"gradient_checkpointing\\\": false,\\n  \\\"bf16\\\": false,\\n  \\\"optim\\\": \\\"adamw_torch\\\",\\n  \\\"intervention_mode\\\": \\\"none\\\",\\n  \\\"intervention_metric\\\": \\\"token_entropy\\\",\\n  \\\"intervention_threshold\\\": 0.15,\\n  \\\"intervention_alpha\\\": 0.0\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-19T10:06:16.343811+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "grep -i \"padding_side\\|n_perm\\|perm.*5000\\|left.*pad\" ~/runs/distrib_canary_collapse/alpha_sweep_a050_s42_fp32.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "grep -i \"padding_side\\|n_perm\\|perm.*5000\\|left.*pad\" ~/runs/distrib_canary_collapse/alpha_sweep_a050_s42_fp32.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-19T10:06:16.343946+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"3443\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T10:06:16.344063+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-19T10:06:16.344194+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "grep \"n_perm\" ~/runs/distrib_canary_collapse/alpha_sweep_a050_s42_fp32.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "grep \"n_perm\" ~/runs/distrib_canary_collapse/alpha_sweep_a050_s42_fp32.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T10:06:16.344362+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-19T10:06:16.344525+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "grep \"n_perm\" /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/analysis/5method_leadlag.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "grep \"n_perm\" /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/analysis/5method_leadlag.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T10:06:16.344653+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-19T10:06:16.344789+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "grep \"n_perm\" /root/autodl-tmp/distrib_canary_collapse/src/analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "grep \"n_perm\" /root/autodl-tmp/distrib_canary_collapse/src/analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T10:06:16.344910+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"grep: /root/autodl-tmp/distrib_canary_collapse/src/analysis.py: No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-19T10:06:16.345027+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "grep -r \"n_perm\" /root/autodl-tmp/distrib_canary_collapse/src/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "grep -r \"n_perm\" /root/autodl-tmp/distrib_canary_collapse/src/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T10:06:16.345146+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"grep: /root/autodl-tmp/distrib_canary_collapse/src/: No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-19T10:06:16.345281+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "find /root/autodl-tmp/distrib_canary_collapse -name \"*.py\" -maxdepth 2",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "find /root/autodl-tmp/distrib_canary_collapse -name \"*.py\" -maxdepth 2",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T10:06:16.345430+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/analysis/detrending_utils.py\\n/root/autodl-tmp/distrib_canary_collapse/configs/dryrun_6.9b.py\\n/root/autodl-tmp/distrib_canary_collapse/mmct/__init__.py\\n/root/autodl-tmp/distrib_canary_collapse/mmct/methods.py\\n/root/autodl-tmp/distrib_canary_collapse/mmct/null_distribution.py\\n/root/autodl-tmp/distrib_canary_collapse/mmct/consensus_test.py\\n/root/autodl-tmp/distrib_canary_collapse/mmct/run_mmct.py\\n/root/autodl-tmp/distrib_canary_collapse/scripts/gen_single_method_table.py\\n/root/autodl-tmp/distrib_canary_collapse/scripts/transfer_entropy_analysis.py\\n/root/autodl-tmp/distrib_canary_collapse/scripts/change_point_analysis.py\\n/root/autodl-tmp/distrib_canary_collapse/scripts/change_point_supplement.py\\n/root/autodl-tmp/distrib_canary_collapse/iterative_train.py\\n/root/autodl-tmp/distrib_canary_collapse/metrics.py\\n/root/autodl-tmp/distrib_canary_collapse/prepare_data.py\\n/root/autodl-tmp/distrib_canary_collapse/prepare_c4.py\\n/root/autodl-tmp/distrib_canary_collapse/prepare_c4_v2.py\\n/root/autodl-tmp/distrib_canary_collapse/prepare_c4_v3.py\\n/root/autodl-tmp/distrib_canary_collapse/prepare_c4_v4.py\\n/root/autodl-tmp/distrib_canary_collapse/prepare_c4_5k_fix.py\\n/root/autodl-tmp/distrib_canary_collapse/prepare_c4_5k_v5.py\\n/root/autodl-tmp/distrib_canary_collapse/run_5method_s43.py\\n/root/autodl-tmp/distrib_canary_collapse/batch_analysis.py\\n/root/autodl-tmp/distrib_canary_collapse/run_intervention_5method.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-19T10:06:16.345562+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "grep \"n_perm\" /root/autodl-tmp/distrib_canary_collapse/batch_analysis.py /root/autodl-tmp/distrib_canary_collapse/mmct/methods.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "grep \"n_perm\" /root/autodl-tmp/distrib_canary_collapse/batch_analysis.py /root/autodl-tmp/distrib_canary_collapse/mmct/methods.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-19T10:06:16.345683+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/batch_analysis.py:def perm_granger(x, y, max_lag=1, n_perm=N_PERM, seed=42, difference=True):\\n/root/autodl-tmp/distrib_canary_collapse/batch_analysis.py:    null_f = np.empty(n_perm)\\n/root/autodl-tmp/distrib_canary_collapse/batch_analysis.py:    for i in range(n_perm):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-19T10:06:16.345798+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "grep \"N_PERM\" /root/autodl-tmp/distrib_canary_collapse/batch_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "grep \"N_PERM\" /root/autodl-tmp/distrib_canary_collapse/batch_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-19T10:06:16.345914+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"N_PERM = 5000\\ndef perm_granger(x, y, max_lag=1, n_perm=N_PERM, seed=42, difference=True):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-19T10:06:16.346082+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "alpha_sweep_a050_s42_fp32",
  "field": "metrics",
  "value": "{'token_entropy_gen0': 3.2342, 'token_entropy_gen10': 2.7075, 'token_entropy_drift_pct': -16.3, 'distinct_1_gen0': 0.0916, 'distinct_1_gen10': 0.0649, 'distinct_1_drift_pct': -29.2, 'perplexity_gen0': 26.95, 'perplexity_gen10': 31.46, 'perplexity_drift_pct': 16.8, 'ece_gen0': 0.0108, 'ece_gen10': 0.0868, 'ece_drift_pct': 703.4, 'perm_granger_fwd': '6/8', 'perm_granger_rev': '0/8', 'ty_granger_fwd': '4/8', 'consensus_k4': '6/8', 'mmct_wpair_fwd': '6/8', 'precision': 'fp32', 'n_perm': 5000, 'padding_side': 'right (D093 fix NOT applied)'}",
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "alpha_sweep_a050_s42_fp32",
    "field": "metrics",
    "value": "{'token_entropy_gen0': 3.2342, 'token_entropy_gen10': 2.7075, 'token_entropy_drift_pct': -16.3, 'distinct_1_gen0': 0.0916, 'distinct_1_gen10': 0.0649, 'distinct_1_drift_pct': -29.2, 'perplexity_gen0': 26.95, 'perplexity_gen10': 31.46, 'perplexity_drift_pct': 16.8, 'ece_gen0': 0.0108, 'ece_gen10': 0.0868, 'ece_drift_pct': 703.4, 'perm_granger_fwd': '6/8', 'perm_granger_rev': '0/8', 'ty_granger_fwd': '4/8', 'consensus_k4': '6/8', 'mmct_wpair_fwd': '6/8', 'precision': 'fp32', 'n_perm': 5000, 'padding_side': 'right (D093 fix NOT applied)'}",
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-19T10:06:16.346318+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"alpha_sweep_a050_s42_fp32\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:30:58.574Z\", \"updated_at\": \"2026-05-19T10:05:46.265Z\", \"spec\": {\"command\": \"iterative_train.py --model_name EleutherAI/pythia-410m --seed 42 --synthetic_ratio 0.50\", \"server\": \"westd-17855\", \"gpu\": [\"cuda:2\"], \"pid\": \"96513\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a050_s42_fp32.log\", \"submitted_at\": \"2026-05-19T05:30:58.346Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/wikitext103_5k\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 42, \"checkpoint_source\": \"EleutherAI/pythia-410m\", \"eval_data\": \"data/wikitext103_5k\"}, \"hypothesis\": \"D091: α=0.50 fp32 s42 boundary regime. Pre-D080 data was fp16. fp32 rerun confirms PermG step function lower bound at boundary regime. 3-seed parallel with s43/s44.\", \"reproduce\": {\"finished_at\": \"2026-05-19T09:48:21.596Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T09:48:25.167829+00:00\"}]}, \"metrics\": {\"token_entropy_gen0\": 3.2342, \"token_entropy_gen10\": 2.7075, \"token_entropy_drift_pct\": -16.3, \"distinct_1_gen0\": 0.0916, \"distinct_1_gen10\": 0.0649, \"distinct_1_drift_pct\": -29.2, \"perplexity_gen0\": 26.95, \"perplexity_gen10\": 31.46, \"perplexity_drift_pct\": 16.8, \"ece_gen0\": 0.0108, \"ece_gen10\": 0.0868, \"ece_drift_pct\": 703.4, \"perm_granger_fwd\": \"6/8\", \"perm_granger_rev\": \"0/8\", \"ty_granger_fwd\": \"4/8\", \"consensus_k4\": \"6/8\", \"mmct_wpair_fwd\": \"6/8\", \"precision\": \"fp32\", \"n_perm\": 5000, \"padding_side\": \"right (D093 fix NOT applied)\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5617}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-19T10:06:16.346561+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "alpha_sweep_a050_s42_fp32",
  "field": "checkpoint_path",
  "value": "results/alpha_sweep/a050_s42_fp32/gen_10/checkpoint",
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "alpha_sweep_a050_s42_fp32",
    "field": "checkpoint_path",
    "value": "results/alpha_sweep/a050_s42_fp32/gen_10/checkpoint",
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-19T10:06:16.346820+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"alpha_sweep_a050_s42_fp32\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:30:58.574Z\", \"updated_at\": \"2026-05-19T10:05:47.027Z\", \"spec\": {\"command\": \"iterative_train.py --model_name EleutherAI/pythia-410m --seed 42 --synthetic_ratio 0.50\", \"server\": \"westd-17855\", \"gpu\": [\"cuda:2\"], \"pid\": \"96513\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a050_s42_fp32.log\", \"submitted_at\": \"2026-05-19T05:30:58.346Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/wikitext103_5k\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 42, \"checkpoint_source\": \"EleutherAI/pythia-410m\", \"eval_data\": \"data/wikitext103_5k\"}, \"hypothesis\": \"D091: α=0.50 fp32 s42 boundary regime. Pre-D080 data was fp16. fp32 rerun confirms PermG step function lower bound at boundary regime. 3-seed parallel with s43/s44.\", \"reproduce\": {\"finished_at\": \"2026-05-19T09:48:21.596Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T09:48:25.167829+00:00\"}]}, \"metrics\": {\"token_entropy_gen0\": 3.2342, \"token_entropy_gen10\": 2.7075, \"token_entropy_drift_pct\": -16.3, \"distinct_1_gen0\": 0.0916, \"distinct_1_gen10\": 0.0649, \"distinct_1_drift_pct\": -29.2, \"perplexity_gen0\": 26.95, \"perplexity_gen10\": 31.46, \"perplexity_drift_pct\": 16.8, \"ece_gen0\": 0.0108, \"ece_gen10\": 0.0868, \"ece_drift_pct\": 703.4, \"perm_granger_fwd\": \"6/8\", \"perm_granger_rev\": \"0/8\", \"ty_granger_fwd\": \"4/8\", \"consensus_k4\": \"6/8\", \"mmct_wpair_fwd\": \"6/8\", \"precision\": \"fp32\", \"n_perm\": 5000, \"padding_side\": \"right (D093 fix NOT applied)\"}, \"checkpoint_path\": \"results/alpha_sweep/a050_s42_fp32/gen_10/checkpoint\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4618}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-19T10:06:16.347047+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "alpha_sweep_a050_s42_fp32",
  "field": "log_path",
  "value": "~/runs/distrib_canary_collapse/alpha_sweep_a050_s42_fp32.log",
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "alpha_sweep_a050_s42_fp32",
    "field": "log_path",
    "value": "~/runs/distrib_canary_collapse/alpha_sweep_a050_s42_fp32.log",
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-19T10:06:16.347325+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"alpha_sweep_a050_s42_fp32\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:30:58.574Z\", \"updated_at\": \"2026-05-19T10:05:47.936Z\", \"spec\": {\"command\": \"iterative_train.py --model_name EleutherAI/pythia-410m --seed 42 --synthetic_ratio 0.50\", \"server\": \"westd-17855\", \"gpu\": [\"cuda:2\"], \"pid\": \"96513\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a050_s42_fp32.log\", \"submitted_at\": \"2026-05-19T05:30:58.346Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/wikitext103_5k\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 42, \"checkpoint_source\": \"EleutherAI/pythia-410m\", \"eval_data\": \"data/wikitext103_5k\"}, \"hypothesis\": \"D091: α=0.50 fp32 s42 boundary regime. Pre-D080 data was fp16. fp32 rerun confirms PermG step function lower bound at boundary regime. 3-seed parallel with s43/s44.\", \"reproduce\": {\"finished_at\": \"2026-05-19T09:48:21.596Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T09:48:25.167829+00:00\"}]}, \"metrics\": {\"token_entropy_gen0\": 3.2342, \"token_entropy_gen10\": 2.7075, \"token_entropy_drift_pct\": -16.3, \"distinct_1_gen0\": 0.0916, \"distinct_1_gen10\": 0.0649, \"distinct_1_drift_pct\": -29.2, \"perplexity_gen0\": 26.95, \"perplexity_gen10\": 31.46, \"perplexity_drift_pct\": 16.8, \"ece_gen0\": 0.0108, \"ece_gen10\": 0.0868, \"ece_drift_pct\": 703.4, \"perm_granger_fwd\": \"6/8\", \"perm_granger_rev\": \"0/8\", \"ty_granger_fwd\": \"4/8\", \"consensus_k4\": \"6/8\", \"mmct_wpair_fwd\": \"6/8\", \"precision\": \"fp32\", \"n_perm\": 5000, \"padding_side\": \"right (D093 fix NOT applied)\"}, \"checkpoint_path\": \"results/alpha_sweep/a050_s42_fp32/gen_10/checkpoint\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a050_s42_fp3
…[truncated 74 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-19T10:06:16.347583+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "alpha_sweep_a050_s42_fp32",
  "field": "conclusion",
  "value": "success: PermG fwd=6/8 (rev=0/8) confirms directional canary lead-lag at boundary α=0.50 in fp32. Consensus_k4=6/8, MMCT=6/8. Entropy drift -16.3%, distinct_1 -29.2%, PPL +16.8%, ECE +703.4%. Results consistent with s43/s44 (both PermG=6/8). TY=4/8 (C003: unreliable at α≤0.50). Note: D093 padding_side fix not applied (right-padding), consistent with s43/s44 runs.",
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "alpha_sweep_a050_s42_fp32",
    "field": "conclusion",
    "value": "success: PermG fwd=6/8 (rev=0/8) confirms directional canary lead-lag at boundary α=0.50 in fp32. Consensus_k4=6/8, MMCT=6/8. Entropy drift -16.3%, distinct_1 -29.2%, PPL +16.8%, ECE +703.4%. Results consistent with s43/s44 (both PermG=6/8). TY=4/8 (C003: unreliable at α≤0.50). Note: D093 padding_side fix not applied (right-padding), consistent with s43/s44 runs.",
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-19T10:06:16.347790+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid conclusion 'success: PermG fwd=6/8 (rev=0/8) confirms directional canary lead-lag at boundary α=0.50 in fp32. Consensus_k4=6/8, MMCT=6/8. Entropy drift -16.3%, distinct_1 -29.2%, PPL +16.8%, ECE +703.4%. Results consistent with s43/s44 (both PermG=6/8). TY=4/8 (C003: unreliable at α≤0.50). Note: D093 padding_side fix not applied (right-padding), consistent with s43/s44 runs.'. Valid: ['failed', 'killed', 'negative', 'success']\", \"metadata\": {\"elapsed_seconds\": 0.4292}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-19T10:06:16.347989+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "alpha_sweep_a050_s42_fp32",
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
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "alpha_sweep_a050_s42_fp32",
    "field": "conclusion",
    "value": "success",
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-19T10:06:16.348237+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"alpha_sweep_a050_s42_fp32\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:30:58.574Z\", \"updated_at\": \"2026-05-19T10:05:59.351Z\", \"spec\": {\"command\": \"iterative_train.py --model_name EleutherAI/pythia-410m --seed 42 --synthetic_ratio 0.50\", \"server\": \"westd-17855\", \"gpu\": [\"cuda:2\"], \"pid\": \"96513\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a050_s42_fp32.log\", \"submitted_at\": \"2026-05-19T05:30:58.346Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/wikitext103_5k\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 42, \"checkpoint_source\": \"EleutherAI/pythia-410m\", \"eval_data\": \"data/wikitext103_5k\"}, \"hypothesis\": \"D091: α=0.50 fp32 s42 boundary regime. Pre-D080 data was fp16. fp32 rerun confirms PermG step function lower bound at boundary regime. 3-seed parallel with s43/s44.\", \"reproduce\": {\"finished_at\": \"2026-05-19T09:48:21.596Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T09:48:25.167829+00:00\"}]}, \"metrics\": {\"token_entropy_gen0\": 3.2342, \"token_entropy_gen10\": 2.7075, \"token_entropy_drift_pct\": -16.3, \"distinct_1_gen0\": 0.0916, \"distinct_1_gen10\": 0.0649, \"distinct_1_drift_pct\": -29.2, \"perplexity_gen0\": 26.95, \"perplexity_gen10\": 31.46, \"perplexity_drift_pct\": 16.8, \"ece_gen0\": 0.0108, \"ece_gen10\": 0.0868, \"ece_drift_pct\": 703.4, \"perm_granger_fwd\": \"6/8\", \"perm_granger_rev\": \"0/8\", \"ty_granger_fwd\": \"4/8\", \"consensus_k4\": \"6/8\", \"mmct_wpair_fwd\": \"6/8\", \"precision\": \"fp32\", \"n_perm\": 5000, \"padding_side\": \"right (D093 fix NOT applied)\"}, \"checkpoint_path\": \"results/alpha_sweep/a050_s42_fp32/gen_10/checkpoint\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a050_s42_fp3
…[truncated 103 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-19T10:06:16.348491+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "alpha_sweep_a050_s42_fp32",
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
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "alpha_sweep_a050_s42_fp32",
    "field": "status",
    "value": "DONE",
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-19T10:06:16.348758+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"alpha_sweep_a050_s42_fp32\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T05:30:58.574Z\", \"updated_at\": \"2026-05-19T10:06:02.951Z\", \"spec\": {\"command\": \"iterative_train.py --model_name EleutherAI/pythia-410m --seed 42 --synthetic_ratio 0.50\", \"server\": \"westd-17855\", \"gpu\": [\"cuda:2\"], \"pid\": \"96513\", \"log_path\": \"~/runs/distrib_canary_collapse/alpha_sweep_a050_s42_fp32.log\", \"submitted_at\": \"2026-05-19T05:30:58.346Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/wikitext103_5k\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 42, \"checkpoint_source\": \"EleutherAI/pythia-410m\", \"eval_data\": \"data/wikitext103_5k\", \"wall_clock_seconds\": 16504.6, \"gpu_hours\": 4.58}, \"hypothesis\": \"D091: α=0.50 fp32 s42 boundary regime. Pre-D080 data was fp16. fp32 rerun confirms PermG step function lower bound at boundary regime. 3-seed parallel with s43/s44.\", \"reproduce\": {\"finished_at\": \"2026-05-19T09:48:21.596Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T09:48:25.167829+00:00\"}]}, \"metrics\": {\"token_entropy_gen0\": 3.2342, \"token_entropy_gen10\": 2.7075, \"token_entropy_drift_pct\": -16.3, \"distinct_1_gen0\": 0.0916, \"distinct_1_gen10\": 0.0649, \"distinct_1_drift_pct\": -29.2, \"perplexity_gen0\": 26.95, \"perplexity_gen10\": 31.46, \"perplexity_drift_pct\": 16.8, \"ece_gen0\": 0.0108, \"ece_gen10\": 0.0868, \"ece_drift_pct\": 703.4, \"perm_granger_fwd\": \"6/8\", \"perm_granger_rev\": \"0/8\", \"ty_granger_fwd\": \"4/8\", \"consensus_k4\": \"6/8\", \"mmct_wpair_fwd\": \"6/8\", \"precision\": \"fp32\", \"n_perm\": 5000, \"padding_side\": \"right (D093 fix NOT applied)\"}, \"checkpoint_path\": \"results/alpha_sweep/a050_s42_fp32/gen_10/checkpoint\", \"log_path\": \"~/runs
…[truncated 251 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-19T10:06:16.348968+00:00_

Registry 已更新为 DONE。

## 汇总：α=0.50 fp32 三种子对比

| Metric | s42 | s43 | s44 |
|---|---|---|---|
| token_entropy_gen0 | 3.2342 | 3.2342 | 3.2342 |
| token_entropy_gen10 | 2.7075 | 2.7227 | 2.7252 |
| token_entropy_drift | -16.3% | -15.8% | -15.7% |
| distinct_1_gen0 | 0.0916 | 0.0929 | 0.0929 |
| distinct_1_gen10 | 0.0649 | 0.0660 | 0.0669 |
| distinct_1_drift | -29.2% | -29.0% | -28.0% |
| perplexity_gen0 | 26.95 | 26.95 | 26.95 |
| perplexity_gen10 | 31.46 | 31.58 | 31.10 |
| perplexity_drift | +16.8% | +17.2% | +15.4% |
| ece_gen0 | 0.0108 | 0.0108 | 0.0108 |
| ece_gen10 | 0.0868 | 0.0842 | 0.0890 |
| ece_drift | +703.4% | +679.6% | +724.1% |
| **perm_granger_fwd** | **6/8** | **6/8** | **6/8** |
| perm_granger_rev | 0/8 | 0/8 | 0/8 |
| ty_granger_fwd | 4/8 | 5/8 | — |
| **consensus_k4** | **6/8** | **6/8** | **6/8** |
| mmct_wpair_fwd | 6/8 | 6/8 | 6/8 |

**结论**：3-seed 完全一致。PermG fwd=6/8、consensus_k4=6/8、MMCT=6/8 跨种子稳定复现，rev=0/8 确认方向性。α=0.50 boundary regime 的 canary lead-lag 信号在 fp32 下稳健成立。

**注意事项**：
- TY Granger 跨种子不稳定（4/8 vs 5/8），符合 C003 约束（α≤0.50 下 TY 不可靠）
- D093 padding_side fix 未应用（3443 次 right-padding 警告），三个种子条件一致
- Wall clock: 4.58 GPU-hours，EXIT_CODE=0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331"
}
```

</details>

---
