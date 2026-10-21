# code alpha sweep aggregation script

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/chats/worker_code_alpha_sweep_aggregation_script_20260514T211956.jsonl`
- **Structured JSON:** [`9272dcb0bd575d0079fe.json`](../../sessions/92/9272dcb0bd575d0079fe.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

41 recorded events

### Tool call

_source line 1 · 2026-05-14T21:22:25.769875+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__save_project_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__save_project_file",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T21:22:25.770136+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T21:22:25.770313+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls -la /root/autodl-tmp/distrib_canary_collapse/results/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls -la /root/autodl-tmp/distrib_canary_collapse/results/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T21:22:25.770458+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-14T21:22:25.770590+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 8\\ndrwxr-xr-x  4 root root   48 May 15 03:01 .\\ndrwxr-xr-x  6 root root 4096 May 15 05:11 ..\\ndrwxr-xr-x  4 root root   83 May 15 05:11 alpha_sweep\\ndrwxr-xr-x 10 root root 4096 May 15 03:00 mvp\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.21}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T21:22:25.770718+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"alpha_sweep\\nmvp\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T21:22:25.770851+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/ -maxdepth 2 -type f -name \"*.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/ -maxdepth 2 -type f -name \"*.json\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T21:22:25.770973+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/config.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s42/config.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/analysis_summary.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T21:22:25.771093+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls -la /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls -la /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T21:22:25.771211+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 4\\ndrwxr-xr-x 4 root root   83 May 15 05:11 .\\ndrwxr-xr-x 4 root root   48 May 15 03:01 ..\\ndrwxr-xr-x 9 root root  152 May 15 05:19 a000_s42\\ndrwxr-xr-x 4 root root   67 May 15 05:19 a025_s42\\n-rw-r--r-- 1 root root 3410 May 15 05:11 analysis_summary.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T21:22:25.771376+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/analyze_mvp.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/analyze_mvp.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T21:22:25.771654+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Analyze MVP experiment: metric trends, cross-correlation, lead time.\\n\\nReads all_metrics.json from each rep, produces:\\n  - metric_trends.png : canary + downstream metrics vs generation\\n  - cross_correlation.png : cross-correlation heatmap\\n  - lead_time_table.csv : lead time estimates per canary-downstream pair\\n  - analysis_summary.json : machine-readable summary with graded verdict\\n\\nEvaluation pipeline (per mvp_evaluation_criteria.md):\\n  1. MAUVE floor effect detection (§4) — demote if Gen 0 < 0.10 and CV < 0.50\\n  2. effective_rank monotonicity check (§3) — Gen 4-9 OLS slope consistency\\n  3. Permutation test (§1) — per-triplet significance via 10k permutations\\n  4. Per-seed significance filtering (§2) — 3/3 consistency requirement\\n  5. Graded verdict (§5) — STRONG PASS / PASS / CONDITIONAL PASS / FAIL\\n  6. Lag dispersion statistics — mean, std, min, max per consistent pair\\n\\nUsage:\\n    python analyze_mvp.py --results_dir results/mvp --seeds 42 43 44\\n    python analyze_mvp.py --results_dir results/mvp --n_permutations 5000\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport sys\\n\\nimport matplotlib.pyplot as plt\\nimport numpy as np\\nimport pandas as pd\\n\\n\\nCANARY_METRICS = [\\\"token_entropy\\\", \\\"self_bleu\\\", \\\"ece\\\", \\\"effective_rank\\\"]\\nDOWNSTREAM_METRICS = [\\\"perplexity\\\", \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\", \\\"mauve\\\"]\\n\\nHIGHER_IS_WORSE = {\\\"self_bleu\\\", \\\"ece\\\", \\\"perplexity\\\"}\\nLOWER_IS_WORSE = {\\\"token_entropy\\\", \\\"effective_rank\\\", \\\"distinct_1\\\", \\\"distinct_2\\\",\\n                   \\\"distinct_3\\\", \\\"mauve\\\"}\\n\\n\\ndef load_metrics(results_dir, seeds):\\n    \\\"\\\"\\\"Load all_metrics.json from each rep, return dict {seed: [metrics_per_gen]}.\\\"\\\"\\\"\\n    data = {}\\n    for seed in seeds:\\n        path = os.path.join(results_dir, f\\\"r
…[truncated 7376 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T21:22:25.771850+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/analysis_summary.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/analysis_summary.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T21:22:25.772062+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"meta\\\": {\\n    \\\"test\\\": \\\"toda_yamamoto\\\",\\n    \\\"alpha_stat\\\": 0.05,\\n    \\\"min_gens\\\": 5,\\n    \\\"valid_pairs\\\": [\\n      [\\n        \\\"ece\\\",\\n        \\\"distinct_1\\\"\\n      ],\\n      [\\n        \\\"token_entropy\\\",\\n        \\\"distinct_1\\\"\\n      ],\\n      [\\n        \\\"token_entropy\\\",\\n        \\\"distinct_2\\\"\\n      ],\\n      [\\n        \\\"token_entropy\\\",\\n        \\\"distinct_3\\\"\\n      ],\\n      [\\n        \\\"token_entropy\\\",\\n        \\\"perplexity\\\"\\n      ]\\n    ]\\n  },\\n  \\\"runs\\\": {\\n    \\\"a000_s42\\\": {\\n      \\\"alpha\\\": 0.0,\\n      \\\"seed\\\": 42,\\n      \\\"n_gens\\\": 5,\\n      \\\"analyzed\\\": true\\n    },\\n    \\\"a025_s42\\\": {\\n      \\\"alpha\\\": 0.25,\\n      \\\"seed\\\": 42,\\n      \\\"n_gens\\\": 0,\\n      \\\"analyzed\\\": false\\n    }\\n  },\\n  \\\"by_alpha\\\": {\\n    \\\"0.00\\\": {\\n      \\\"ece_to_distinct_1\\\": {\\n        \\\"n_seeds\\\": 1,\\n        \\\"n_significant\\\": 0,\\n        \\\"sig_rate\\\": 0.0,\\n        \\\"p_median\\\": null,\\n        \\\"p_mean\\\": null,\\n        \\\"F_mean\\\": null,\\n        \\\"F_std\\\": null,\\n        \\\"per_seed\\\": [\\n          {\\n            \\\"p\\\": 1,\\n            \\\"d_max\\\": 1,\\n            \\\"k\\\": 2,\\n            \\\"wald_F\\\": null,\\n            \\\"p_value\\\": null,\\n            \\\"significant\\\": false,\\n            \\\"note\\\": \\\"no residual df (T_eff=3, params=5)\\\",\\n            \\\"d_canary\\\": 1,\\n            \\\"d_downstream\\\": 1\\n          }\\n        ]\\n      },\\n      \\\"token_entropy_to_distinct_1\\\": {\\n        \\\"n_seeds\\\": 1,\\n        \\\"n_significant\\\": 0,\\n        \\\"sig_rate\\\": 0.0,\\n        \\\"p_median\\\": null,\\n        \\\"p_mean\\\": null,\\n        \\\"F_mean\\\": null,\\n        \\\"F_std\\\": null,\\n        \\\"per_seed\\\": [\\n   
…[truncated 2626 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T21:22:25.772231+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/ -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/ -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T21:22:25.772419+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/config.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_0/synthetic_data/data-00000-of-00001.arrow\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_0/synthetic_data/state.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_0/synthetic_data/dataset_info.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_0/metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_1/synthetic_data/data-00000-of-00001.arrow\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_1/synthetic_data/state.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_1/synthetic_data/dataset_info.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_1/checkpoint/config.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_1/checkpoint/generation_config.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_1/checkpoint/model.safetensors\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_1/checkpoint/tokenizer_config.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_1/checkpoint/special_tokens_map.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_1/checkpoint/tokenizer.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_1/metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_2/synthetic_data/data-00000-of-00001.arrow\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_2/synthetic_data/state.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_2/synthetic_data/dataset_info.json\\n/root/autodl-tmp/distrib_can
…[truncated 4628 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T21:22:25.772568+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/config.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/config.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T21:22:25.772721+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\",\\n  \\\"data_dir\\\": \\\"data/wikitext103_5k\\\",\\n  \\\"dataset\\\": \\\"wikitext-103-v1\\\",\\n  \\\"synthetic_ratio\\\": 0.0,\\n  \\\"num_generations\\\": 10,\\n  \\\"steps_per_gen\\\": 5000,\\n  \\\"output_dir\\\": \\\"results/alpha_sweep/a000_s42\\\",\\n  \\\"seed\\\": 42,\\n  \\\"batch_size\\\": 4,\\n  \\\"max_length\\\": 512,\\n  \\\"lr\\\": 5e-05,\\n  \\\"gen_max_new_tokens\\\": 256,\\n  \\\"gen_batch_size\\\": 16,\\n  \\\"top_p\\\": 0.95,\\n  \\\"accumulate\\\": false\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T21:22:25.772873+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_0/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_0/metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T21:22:25.773003+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"token_entropy\\\": 3.2341948700181407,\\n  \\\"self_bleu\\\": 0.010194395218435404,\\n  \\\"distinct_1\\\": 0.0982156685333268,\\n  \\\"distinct_2\\\": 0.5178027030111348,\\n  \\\"distinct_3\\\": 0.8127277321747353,\\n  \\\"ece\\\": 0.010804557477709054,\\n  \\\"effective_rank\\\": 46.612774691899155,\\n  \\\"perplexity\\\": 26.948958972544652,\\n  \\\"mauve\\\": 0.03406737671684175,\\n  \\\"generation\\\": 0\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T21:22:25.773121+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_4/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_4/metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-14T21:22:25.773240+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -80 /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -80 /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T21:22:25.773389+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"token_entropy\\\": 3.040745918964843,\\n  \\\"self_bleu\\\": 0.011961223108689292,\\n  \\\"distinct_1\\\": 0.08683875960422309,\\n  \\\"distinct_2\\\": 0.47219590006001455,\\n  \\\"distinct_3\\\": 0.7801871520511707,\\n  \\\"ece\\\": 0.011429671611937243,\\n  \\\"effective_rank\\\": 47.36696539761295,\\n  \\\"perplexity\\\": 20.524123476072038,\\n  \\\"mauve\\\": 0.027979995177423035,\\n  \\\"generation\\\": 4\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T21:22:25.773568+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Method ablation: compare four lead-lag estimation methods.\\n\\nCompares naive vs robust approaches to detect canary->downstream lead-lag,\\nquantifying the spurious regression rate when non-stationary series are\\ncorrelated without proper detrending.\\n\\nInput:  results/mvp/rep_{seed}/all_metrics.json (seeds 42-45)\\nOutput: results/mvp/analysis/method_ablation.json\\n\\nMethods:\\n  1. Naive Pearson lag-correlation (raw levels)\\n  2. Differenced cross-correlation (first-differenced series)\\n  3. Threshold-based lead time (2-sigma onset detection)\\n  4. Toda-Yamamoto augmented-lag Granger causality\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport warnings\\nfrom itertools import product\\n\\nimport numpy as np\\nfrom scipy import stats\\nfrom statsmodels.tsa.stattools import adfuller\\n\\nwarnings.filterwarnings(\\\"ignore\\\")\\n\\nCANARY = [\\\"token_entropy\\\", \\\"self_bleu\\\", \\\"ece\\\", \\\"effective_rank\\\"]\\nDOWNSTREAM = [\\\"perplexity\\\", \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\"]\\n\\n# Sign conventions: \\\"higher is worse\\\" kept as-is; \\\"lower is worse\\\" negated\\n# so that degradation = positive direction in all analyses.\\nHIGHER_IS_WORSE = {\\\"self_bleu\\\", \\\"ece\\\", \\\"perplexity\\\"}\\nLOWER_IS_WORSE = {\\\"token_entropy\\\", \\\"effective_rank\\\",\\n                   \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\"}\\n\\nALPHA = 0.05\\n\\n\\ndef load_metrics(data_dir, seeds):\\n    \\\"\\\"\\\"Load all_metrics.json for each seed.\\\"\\\"\\\"\\n    data = {}\\n    for s in seeds:\\n        path = os.path.join(data_dir, f\\\"rep_{s}\\\", \\\"all_metrics.json\\\")\\n        with open(path) as f:\\n            data[s] = json.load(f)\\n    return data\\n\\n\\ndef extract(metrics_list, name):\\n    \\\"\\\"\\\"Extract a single metric as numpy array, sorted by generation.\\\"\\\"\\\"\\n    return np.array([m[name
…[truncated 1217 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T21:22:25.773762+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n \"def \" /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep -n \"def \" /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T21:22:25.773897+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"41:def load_metrics(data_dir, seeds):\\n51:def extract(metrics_list, name):\\n57:def orient(series, name):\\n66:def naive_pearson(c, d, cn, dn, max_lag=3):\\n95:def diff_xcorr(c, d, cn, dn, max_lag=3):\\n126:def _onset_gen(series, name):\\n139:def threshold_lead(c, d, cn, dn):\\n174:def _adf_order(series, max_d=2):\\n190:def toda_yamamoto(c, d, cn, dn):\\n280:def main():\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T21:22:25.774018+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/all_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/all_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T21:22:25.774135+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/all_metrics.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T21:22:25.774248+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -3 /root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/all_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -3 /root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/all_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T21:22:25.774388+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"token_entropy\\\": 3.2341948700181407,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T21:22:25.774500+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "python3 -c \"import sys; sys.path.insert(0,'.'); print('ok')\" 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "python3 -c \"import sys; sys.path.insert(0,'.'); print('ok')\" 2>&1",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T21:22:25.774612+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T21:22:25.774804+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "cat << 'PYTHON_EOF' > /root/autodl-tmp/distrib_canary_collapse/analyze_alpha_sweep.py\n\"\"\"Alpha-sweep aggregation analysis for distributional canary collapse.\n\nScans results/alpha_sweep/ for completed runs, computes cross-correlation\nlead-lag estimates across multiple canary→downstream channels, and outputs\nphase diagram data.\n\nInput:  results/alpha_sweep/{a*_s*}/gen_N/metrics.json\nOutput: results/alpha_sweep_analysis/{phase_diagram.csv, phase_diagram.json,\n        summary_by_alpha.json}\n\nDependencies: numpy, scipy, pandas\n\"\"\"\n\nimport argparse\nimport json\nimport os\nimport re\nimport sys\nfrom collections import defaultdict\nfrom glob import glob\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\n\n\n# --- Constants ---\n\nHIGHER_IS_WORSE = {\"self_bleu\", \"ece\", \"perplexity\"}\nLOWER_IS_WORSE = {\"token_entropy\", \"effective_rank\",\n                   \"distinct_1\", \"distinct_2\", \"distinct_3\", \"mauve\"}\n\nCHANNELS = [\n    (\"token_entropy\", \"distinct_1\"),\n    (\"token_entropy\", \"distinct_2\"),\n    (\"token_entropy\", \"distinct_3\"),\n    (\"token_entropy\", \"perplexity\"),\n    (\"token_entropy\", \"ece\"),\n    (\"ece\", \"perplexity\"),\n    (\"ece\", \"distinct_1\"),\n]\n\nMIN_GENERATIONS = 4\n\n\n# --- Data loading ---\n\ndef discover_runs(results_dir):\n    \"\"\"Scan results_dir for alpha_sweep run directories.\n\n    Returns list of dicts: {path, alpha, seed, run_id}.\n    \"\"\"\n    runs = []\n    pattern = re.compile(r\"^a(\\d{3})_s(\\d+)(_v\\d+)?$\")\n    if not os.path.isdir(results_dir):\n        print(f\"WARNING: results dir not found: {results_dir}\", file=sys.stderr)\n        return runs\n    for name in sorted(os.listdir(results_dir)):\n        m = pattern.match(name)\n        if not m:\n            continue\n        run_path = os.path.join(results_dir, name)\n        if not os.path.isdir(run_path):\n            continue\n        alpha_int = int(m.group(1))\n        alpha = alpha_int / 100.0\n        seed = int(m.group(2))\n        config_path = os.path.join(run_path, \"config.json\")\n        if os.path.isfile(config_path):\n            with open(config_path) as f:\n                cfg = json.load(f)\n            alpha = cfg.get(\"synthetic_ratio\", alpha)\n            seed = cfg.get(\"seed\", seed)\n        runs.append({\n            \"path\": run_path,\n            \"alpha\": alpha,\n            \"seed\": seed,\n            \"run_id\": name,\n        })\n    return runs\n\n\ndef load_run_metrics(run_path):\n    \"\"\"Load per-generation metrics from gen_N/metrics.json files.\n\n    Returns sorted list of metric dicts, or None if no data.\n    \"\"\"\n    metrics = []\n    for entry in os.listdir(run_path):\n        m = re.match(r\"^gen_(\\d+)$\", entry)\n        if not m:\n            continue\n        mpath = os.path.join(run_path, entry, \"metrics.json\")\n        if not os.path.isfile(mpath):\n            continue\n        with open(mpath) as f:\n            data = json.load(f)\n        data[\"generation\"] = int(m.group(1))\n        metrics.append(data)\n    if not metrics:\n        return None\n    metrics.sort(key=lambda x: x[\"generation\"])\n    return metrics\n\n\ndef extract(metrics_list, name):\n    \"\"\"Extract a single metric as numpy array, sorted by generation.\"\"\"\n    return np.array([m[name] for m in metrics_list])\n\n\ndef orient(series, name):\n    \"\"\"Orient so degradation = positive direction.\"\"\"\n    return -series.copy() if name in LOWER_IS_WORSE else series.copy()\n\n\n# --- Cross-correlation ---\n\ndef cross_correlate(x, y, max_lag=5):\n    \"\"\"Cross-correlation at lags -max_lag..+max_lag.\n\n    Returns dict {lag: correlation}. Negative lag = x leads y.\n    \"\"\"\n    x = (x - x.mean()) / (x.std() + 1e-12)\n    y = (y - y.mean()) / (y.std() + 1e-12)\n    n = len(x)\n    correlations = {}\n    for lag in range(-max_lag, max_lag + 1):\n        if lag >= 0:\n            c = np.corrcoef(x[lag:], y[:n - lag])[0, 1] if n - lag > 2 else 0.0\n        else:\n            c = np.corrcoef(x[:n + lag], y[-lag:])[0, 1] if n + lag > 2 else 0.0\n        correlations[lag] = float(c) if np.isfinite(c) else 0.0\n    return correlations\n\n\ndef permutation_test(canary, downstream, canary_name, downstream_name,\n                     max_lag=5, n_permutations=5000, rng_seed=0):\n    \"\"\"Permutation test for cross-correlation significance.\n\n    Returns (peak_lag, peak_r, p_value).\n    \"\"\"\n    c = orient(canary, canary_name)\n    d = orient(downstream, downstream_name)\n\n    corrs = cross_correlate(c, d, max_lag=max_lag)\n    peak_lag = max(corrs, key=lambda k: abs(corrs[k]))\n    observed_r = abs(corrs[peak_lag])\n\n    rng = np.random.RandomState(rng_seed)\n    count_ge = 0\n    for _ in range(n_permutations):\n        d_perm = rng.permutation(d)\n        perm_corrs = cross_correlate(c, d_perm, max_lag=max_lag)\n        perm_max = max(abs(v) for v in perm_corrs.values())\n        if perm_max >= observed_r:\n            count_ge += 1\n    p_value = (count_ge + 1) / (n_permutations + 1)\n    return peak_lag, corrs[peak_lag], p_value\n\n\ndef analyze_channel(metrics_list, canary_name, downstream_name, max_lag=5,\n                    n_permutations=5000, rng_seed=0):\n    \"\"\"Analyze one canary→downstream channel for a single run.\n\n    Returns dict with lag, r, p_value, etc. or None if insufficient data.\n    \"\"\"\n    if canary_name not in metrics_list[0] or downstream_name not in metrics_list[0]:\n        return None\n\n    canary = extract(metrics_list, canary_name)\n    downstream = extract(metrics_list, downstream_name)\n\n    if len(canary) < MIN_GENERATIONS:\n        return None\n\n    if np.std(canary) < 1e-10 or np.std(downstream) < 1e-10:\n        return {\"lag\": 0, \"r_value\": 0.0, \"p_value\": 1.0,\n                \"is_significant\": False, \"note\": \"constant_series\"}\n\n    peak_lag, peak_r, p_value = permutation_test(\n        canary, downstream, canary_name, downstream_name,\n        max_lag=max_lag, n_permutations=n_permutations, rng_seed=rng_seed)\n\n    canary_leads = peak_lag < 0\n    lead_time = abs(peak_lag) if canary_leads else 0\n\n    return {\n        \"lag\": int(peak_lag),\n        \"r_value\": round(float(peak_r), 4),\n        \"p_value\": round(float(p_value), 4),\n        \"is_significant\": p_value < 0.05,\n        \"canary_leads\": bool(canary_leads),\n        \"lead_time_generations\": int(lead_time),\n        \"n_generations\": len(canary),\n    }\n\n\n# --- Phase boundary detection ---\n\ndef detect_phase_boundary(df, channel_col=\"channel\", alpha_col=\"alpha\",\n                          sig_col=\"is_significant\"):\n    \"\"\"Find α threshold where canary lead transitions from significant to not.\n\n    For each channel, find the smallest α where significance rate drops below 50%.\n    Returns dict {channel: boundary_alpha or None}.\n    \"\"\"\n    boundaries = {}\n    for channel in df[channel_col].unique():\n        sub = df[df[channel_col] == channel]\n        alpha_groups = sub.groupby(alpha_col)[sig_col].mean().sort_index()\n        boundary = None\n        for i in range(len(alpha_groups) - 1):\n            a_curr = alpha_groups.index[i]\n            a_next = alpha_groups.index[i + 1]\n            if alpha_groups.iloc[i] >= 0.5 and alpha_groups.iloc[i + 1] < 0.5:\n                boundary = round((a_curr + a_next) / 2, 3)\n                break\n        if boundary is None and len(alpha_groups) > 0:\n            if alpha_groups.iloc[-1] >= 0.5:\n                boundary = \"above_max\"\n            elif alpha_groups.iloc[0] < 0.5:\n                boundary = \"below_min\"\n        boundaries[channel] = boundary\n    return boundaries\n\n\n# --- Main ---\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Alpha-sweep aggregation analysis for canary collapse\")\n    parser.add_argument(\"--results-dir\", default=\"results/alpha_sweep\",\n                        help=\"Directory containing alpha_sweep run dirs\")\n    parser.add_argument(\"--output-dir\", default=\"results/alpha_sweep_analysis\",\n                        help=\"Output directory\")\n    parser.add_argument(\"--max-lag\", type=int, default=5,\n                        help=\"Maximum lag for cross-correlation\")\n    parser.add_argument(\"--n-permutations\", type=int, default=5000,\n                        help=\"Number of permutations for significance test\")\n    args = parser.parse_args()\n\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    # 1. Discover runs\n    runs = discover_runs(args.results_dir)\n    if not runs:\n        print(f\"No runs found in {args.results_dir}\")\n        sys.exit(1)\n\n    print(f\"Discovered {len(runs)} runs:\")\n    for r in runs:\n        print(f\"  {r['run_id']}: alpha={r['alpha']}, seed={r['seed']}\")\n\n    # 2. Load and analyze\n    all_rows = []\n    skipped = []\n\n    for run in runs:\n        metrics = load_run_metrics(run[\"path\"])\n        if metrics is None or len(metrics) < MIN_GENERATIONS:\n            n = len(metrics) if metrics else 0\n            skipped.append({\"run_id\": run[\"run_id\"], \"reason\": f\"too_few_gens ({n})\"})\n            print(f\"  SKIP {run['run_id']}: only {n} generations (need {MIN_GENERATIONS})\")\n            continue\n\n        print(f\"\\nAnalyzing {run['run_id']} ({len(metrics)} generations)...\")\n\n        for canary_name, downstream_name in CHANNELS:\n            channel = f\"{canary_name}_to_{downstream_name}\"\n            result = analyze_channel(\n                metrics, canary_name, downstream_name,\n                max_lag=args.max_lag,\n                n_permutations=args.n_permutations,\n                rng_seed=run[\"seed\"])\n\n            if result is None:\n                continue\n\n            row = {\n                \"alpha\": run[\"alpha\"],\n                \"seed\": run[\"seed\"],\n                \"run_id\": run[\"run_id\"],\n                \"channel\": channel,\n                \"canary\": canary_name,\n                \"downstream\": downstream_name,\n                **result,\n            }\n            all_rows.append(row)\n            sig_marker = \"*\" if result[\"is_significant\"] else \" \"\n            print(f\"  {sig_marker} {channel}: lag={result['lag']}, \"\n                  f\"r={result['r_value']:.3f}, p={result['p_value']:.4f}\")\n\n    if not all_rows:\n        print(\"\\nNo analyzable runs found.\")\n        sys.exit(1)\n\n    # 3. Build DataFrame\n    df = pd.DataFrame(all_rows)\n\n    # 4. Save phase diagram CSV\n    csv_path = os.path.join(args.output_dir, \"phase_diagram.csv\")\n    df.to_csv(csv_path, index=False)\n    print(f\"\\nSaved {csv_path} ({len(df)} rows)\")\n\n    # 5. Summary by alpha\n    summary_by_alpha = {}\n    for alpha, grp in df.groupby(\"alpha\"):\n        alpha_key = f\"{alpha:.2f}\"\n        channel_summaries = {}\n        for channel, ch_grp in grp.groupby(\"channel\"):\n            channel_summaries[channel] = {\n                \"n_seeds\": len(ch_grp),\n                \"n_significant\": int(ch_grp[\"is_significant\"].sum()),\n                \"sig_rate\": round(float(ch_grp[\"is_significant\"].mean()), 3),\n                \"mean_lag\": round(float(ch_grp[\"lag\"].mean()), 2),\n                \"std_lag\": round(float(ch_grp[\"lag\"].std()), 2) if len(ch_grp) > 1 else 0.0,\n                \"mean_r\": round(float(ch_grp[\"r_value\"].mean()), 4),\n                \"mean_lead_time\": round(float(ch_grp[\"lead_time_generations\"].mean()), 2),\n                \"mean_p\": round(float(ch_grp[\"p_value\"].mean()), 4),\n            }\n        summary_by_alpha[alpha_key] = {\n            \"n_runs\": len(grp[\"run_id\"].unique()),\n            \"n_total_pairs\": len(grp),\n            \"overall_sig_rate\": round(float(grp[\"is_significant\"].mean()), 3),\n            \"channels\": channel_summaries,\n        }\n\n    # 6. Phase boundary detection\n    boundaries = detect_phase_boundary(df)\n\n    # 7. Build full output JSON\n    output = {\n        \"meta\": {\n            \"n_runs_total\": len(runs),\n            \"n_runs_analyzed\": len(df[\"run_id\"].unique()),\n            \"n_runs_skipped\": len(skipped),\n            \"skipped\": skipped,\n            \"channels\": [f\"{c}_to_{d}\" for c, d in CHANNELS],\n            \"max_lag\": args.max_lag,\n            \"n_permutations\": args.n_permutations,\n            \"significance_threshold\": 0.05,\n        },\n        \"summary_by_alpha\": summary_by_alpha,\n        \"phase_boundaries\": {k: v for k, v in boundaries.items()},\n        \"per_run\": all_rows,\n    }\n\n    json_path = os.path.join(args.output_dir, \"phase_diagram.json\")\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2, default=str)\n    print(f\"Saved {json_path}\")\n\n    # 8. Console summary\n    print(\"\\n\" + \"=\" * 60)\n    print(\"ALPHA-SWEEP ANALYSIS SUMMARY\")\n    print(\"=\" * 60)\n    print(f\"Runs analyzed: {len(df['run_id'].unique())}/{len(runs)}\")\n    print(f\"Alpha values: {sorted(df['alpha'].unique())}\")\n\n    print(\"\\nSignificance rate by alpha:\")\n    for alpha_key in sorted(summary_by_alpha.keys()):\n        s = summary_by_alpha[alpha_key]\n        print(f\"  alpha={alpha_key}: {s['overall_sig_rate']:.0%} \"\n              f\"({s['n_runs']} runs)\")\n\n    print(\"\\nPhase boundaries (canary lead sig → not-sig):\")\n    for channel, boundary in sorted(boundaries.items()):\n        print(f\"  {channel}: alpha = {boundary}\")\n\n    print(f\"\\nResults saved to {args.output_dir}/\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYTHON_EOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat << 'PYTHON_EOF' > /root/autodl-tmp/distrib_canary_collapse/analyze_alpha_sweep.py\n\"\"\"Alpha-sweep aggregation analysis for distributional canary collapse.\n\nScans results/alpha_sweep/ for completed runs, computes cross-correlation\nlead-lag estimates across multiple canary→downstream channels, and outputs\nphase diagram data.\n\nInput:  results/alpha_sweep/{a*_s*}/gen_N/metrics.json\nOutput: results/alpha_sweep_analysis/{phase_diagram.csv, phase_diagram.json,\n        summary_by_alpha.json}\n\nDependencies: numpy, scipy, pandas\n\"\"\"\n\nimport argparse\nimport json\nimport os\nimport re\nimport sys\nfrom collections import defaultdict\nfrom glob import glob\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\n\n\n# --- Constants ---\n\nHIGHER_IS_WORSE = {\"self_bleu\", \"ece\", \"perplexity\"}\nLOWER_IS_WORSE = {\"token_entropy\", \"effective_rank\",\n                   \"distinct_1\", \"distinct_2\", \"distinct_3\", \"mauve\"}\n\nCHANNELS = [\n    (\"token_entropy\", \"distinct_1\"),\n    (\"token_entropy\", \"distinct_2\"),\n    (\"token_entropy\", \"distinct_3\"),\n    (\"token_entropy\", \"perplexity\"),\n    (\"token_entropy\", \"ece\"),\n    (\"ece\", \"perplexity\"),\n    (\"ece\", \"distinct_1\"),\n]\n\nMIN_GENERATIONS = 4\n\n\n# --- Data loading ---\n\ndef discover_runs(results_dir):\n    \"\"\"Scan results_dir for alpha_sweep run directories.\n\n    Returns list of dicts: {path, alpha, seed, run_id}.\n    \"\"\"\n    runs = []\n    pattern = re.compile(r\"^a(\\d{3})_s(\\d+)(_v\\d+)?$\")\n    if not os.path.isdir(results_dir):\n        print(f\"WARNING: results dir not found: {results_dir}\", file=sys.stderr)\n        return runs\n    for name in sorted(os.listdir(results_dir)):\n        m = pattern.match(name)\n        if not m:\n            continue\n        run_path = os.path.join(results_dir, name)\n        if not os.path.isdir(run_path):\n            continue\n        alpha_int = int(m.group(1))\n        alpha = alpha_int / 100.0\n        seed = int(m.group(2))\n        config_path = os.path.join(run_path, \"config.json\")\n        if os.path.isfile(config_path):\n            with open(config_path) as f:\n                cfg = json.load(f)\n            alpha = cfg.get(\"synthetic_ratio\", alpha)\n            seed = cfg.get(\"seed\", seed)\n        runs.append({\n            \"path\": run_path,\n            \"alpha\": alpha,\n            \"seed\": seed,\n            \"run_id\": name,\n        })\n    return runs\n\n\ndef load_run_metrics(run_path):\n    \"\"\"Load per-generation metrics from gen_N/metrics.json files.\n\n    Returns sorted list of metric dicts, or None if no data.\n    \"\"\"\n    metrics = []\n    for entry in os.listdir(run_path):\n        m = re.match(r\"^gen_(\\d+)$\", entry)\n        if not m:\n            continue\n        mpath = os.path.join(run_path, entry, \"metrics.json\")\n        if not os.path.isfile(mpath):\n            continue\n        with open(mpath) as f:\n            data = json.load(f)\n        data[\"generation\"] = int(m.group(1))\n        metrics.append(data)\n    if not metrics:\n        return None\n    metrics.sort(key=lambda x: x[\"generation\"])\n    return metrics\n\n\ndef extract(metrics_list, name):\n    \"\"\"Extract a single metric as numpy array, sorted by generation.\"\"\"\n    return np.array([m[name] for m in metrics_list])\n\n\ndef orient(series, name):\n    \"\"\"Orient so degradation = positive direction.\"\"\"\n    return -series.copy() if name in LOWER_IS_WORSE else series.copy()\n\n\n# --- Cross-correlation ---\n\ndef cross_correlate(x, y, max_lag=5):\n    \"\"\"Cross-correlation at lags -max_lag..+max_lag.\n\n    Returns dict {lag: correlation}. Negative lag = x leads y.\n    \"\"\"\n    x = (x - x.mean()) / (x.std() + 1e-12)\n    y = (y - y.mean()) / (y.std() + 1e-12)\n    n = len(x)\n    correlations = {}\n    for lag in range(-max_lag, max_lag + 1):\n        if lag >= 0:\n            c = np.corrcoef(x[lag:], y[:n - lag])[0, 1] if n - lag > 2 else 0.0\n        else:\n            c = np.corrcoef(x[:n + lag], y[-lag:])[0, 1] if n + lag > 2 else 0.0\n        correlations[lag] = float(c) if np.isfinite(c) else 0.0\n    return correlations\n\n\ndef permutation_test(canary, downstream, canary_name, downstream_name,\n                     max_lag=5, n_permutations=5000, rng_seed=0):\n    \"\"\"Permutation test for cross-correlation significance.\n\n    Returns (peak_lag, peak_r, p_value).\n    \"\"\"\n    c = orient(canary, canary_name)\n    d = orient(downstream, downstream_name)\n\n    corrs = cross_correlate(c, d, max_lag=max_lag)\n    peak_lag = max(corrs, key=lambda k: abs(corrs[k]))\n    observed_r = abs(corrs[peak_lag])\n\n    rng = np.random.RandomState(rng_seed)\n    count_ge = 0\n    for _ in range(n_permutations):\n        d_perm = rng.permutation(d)\n        perm_corrs = cross_correlate(c, d_perm, max_lag=max_lag)\n        perm_max = max(abs(v) for v in perm_corrs.values())\n        if perm_max >= observed_r:\n            count_ge += 1\n    p_value = (count_ge + 1) / (n_permutations + 1)\n    return peak_lag, corrs[peak_lag], p_value\n\n\ndef analyze_channel(metrics_list, canary_name, downstream_name, max_lag=5,\n                    n_permutations=5000, rng_seed=0):\n    \"\"\"Analyze one canary→downstream channel for a single run.\n\n    Returns dict with lag, r, p_value, etc. or None if insufficient data.\n    \"\"\"\n    if canary_name not in metrics_list[0] or downstream_name not in metrics_list[0]:\n        return None\n\n    canary = extract(metrics_list, canary_name)\n    downstream = extract(metrics_list, downstream_name)\n\n    if len(canary) < MIN_GENERATIONS:\n        return None\n\n    if np.std(canary) < 1e-10 or np.std(downstream) < 1e-10:\n        return {\"lag\": 0, \"r_value\": 0.0, \"p_value\": 1.0,\n                \"is_significant\": False, \"note\": \"constant_series\"}\n\n    peak_lag, peak_r, p_value = permutation_test(\n        canary, downstream, canary_name, downstream_name,\n        max_lag=max_lag, n_permutations=n_permutations, rng_seed=rng_seed)\n\n    canary_leads = peak_lag < 0\n    lead_time = abs(peak_lag) if canary_leads else 0\n\n    return {\n        \"lag\": int(peak_lag),\n        \"r_value\": round(float(peak_r), 4),\n        \"p_value\": round(float(p_value), 4),\n        \"is_significant\": p_value < 0.05,\n        \"canary_leads\": bool(canary_leads),\n        \"lead_time_generations\": int(lead_time),\n        \"n_generations\": len(canary),\n    }\n\n\n# --- Phase boundary detection ---\n\ndef detect_phase_boundary(df, channel_col=\"channel\", alpha_col=\"alpha\",\n                          sig_col=\"is_significant\"):\n    \"\"\"Find α threshold where canary lead transitions from significant to not.\n\n    For each channel, find the smallest α where significance rate drops below 50%.\n    Returns dict {channel: boundary_alpha or None}.\n    \"\"\"\n    boundaries = {}\n    for channel in df[channel_col].unique():\n        sub = df[df[channel_col] == channel]\n        alpha_groups = sub.groupby(alpha_col)[sig_col].mean().sort_index()\n        boundary = None\n        for i in range(len(alpha_groups) - 1):\n            a_curr = alpha_groups.index[i]\n            a_next = alpha_groups.index[i + 1]\n            if alpha_groups.iloc[i] >= 0.5 and alpha_groups.iloc[i + 1] < 0.5:\n                boundary = round((a_curr + a_next) / 2, 3)\n                break\n        if boundary is None and len(alpha_groups) > 0:\n            if alpha_groups.iloc[-1] >= 0.5:\n                boundary = \"above_max\"\n            elif alpha_groups.iloc[0] < 0.5:\n                boundary = \"below_min\"\n        boundaries[channel] = boundary\n    return boundaries\n\n\n# --- Main ---\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Alpha-sweep aggregation analysis for canary collapse\")\n    parser.add_argument(\"--results-dir\", default=\"results/alpha_sweep\",\n                        help=\"Directory containing alpha_sweep run dirs\")\n    parser.add_argument(\"--output-dir\", default=\"results/alpha_sweep_analysis\",\n                        help=\"Output directory\")\n    parser.add_argument(\"--max-lag\", type=int, default=5,\n                        help=\"Maximum lag for cross-correlation\")\n    parser.add_argument(\"--n-permutations\", type=int, default=5000,\n                        help=\"Number of permutations for significance test\")\n    args = parser.parse_args()\n\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    # 1. Discover runs\n    runs = discover_runs(args.results_dir)\n    if not runs:\n        print(f\"No runs found in {args.results_dir}\")\n        sys.exit(1)\n\n    print(f\"Discovered {len(runs)} runs:\")\n    for r in runs:\n        print(f\"  {r['run_id']}: alpha={r['alpha']}, seed={r['seed']}\")\n\n    # 2. Load and analyze\n    all_rows = []\n    skipped = []\n\n    for run in runs:\n        metrics = load_run_metrics(run[\"path\"])\n        if metrics is None or len(metrics) < MIN_GENERATIONS:\n            n = len(metrics) if metrics else 0\n            skipped.append({\"run_id\": run[\"run_id\"], \"reason\": f\"too_few_gens ({n})\"})\n            print(f\"  SKIP {run['run_id']}: only {n} generations (need {MIN_GENERATIONS})\")\n            continue\n\n        print(f\"\\nAnalyzing {run['run_id']} ({len(metrics)} generations)...\")\n\n        for canary_name, downstream_name in CHANNELS:\n            channel = f\"{canary_name}_to_{downstream_name}\"\n            result = analyze_channel(\n                metrics, canary_name, downstream_name,\n                max_lag=args.max_lag,\n                n_permutations=args.n_permutations,\n                rng_seed=run[\"seed\"])\n\n            if result is None:\n                continue\n\n            row = {\n                \"alpha\": run[\"alpha\"],\n                \"seed\": run[\"seed\"],\n                \"run_id\": run[\"run_id\"],\n                \"channel\": channel,\n                \"canary\": canary_name,\n                \"downstream\": downstream_name,\n                **result,\n            }\n            all_rows.append(row)\n            sig_marker = \"*\" if result[\"is_significant\"] else \" \"\n            print(f\"  {sig_marker} {channel}: lag={result['lag']}, \"\n                  f\"r={result['r_value']:.3f}, p={result['p_value']:.4f}\")\n\n    if not all_rows:\n        print(\"\\nNo analyzable runs found.\")\n        sys.exit(1)\n\n    # 3. Build DataFrame\n    df = pd.DataFrame(all_rows)\n\n    # 4. Save phase diagram CSV\n    csv_path = os.path.join(args.output_dir, \"phase_diagram.csv\")\n    df.to_csv(csv_path, index=False)\n    print(f\"\\nSaved {csv_path} ({len(df)} rows)\")\n\n    # 5. Summary by alpha\n    summary_by_alpha = {}\n    for alpha, grp in df.groupby(\"alpha\"):\n        alpha_key = f\"{alpha:.2f}\"\n        channel_summaries = {}\n        for channel, ch_grp in grp.groupby(\"channel\"):\n            channel_summaries[channel] = {\n                \"n_seeds\": len(ch_grp),\n                \"n_significant\": int(ch_grp[\"is_significant\"].sum()),\n                \"sig_rate\": round(float(ch_grp[\"is_significant\"].mean()), 3),\n                \"mean_lag\": round(float(ch_grp[\"lag\"].mean()), 2),\n                \"std_lag\": round(float(ch_grp[\"lag\"].std()), 2) if len(ch_grp) > 1 else 0.0,\n                \"mean_r\": round(float(ch_grp[\"r_value\"].mean()), 4),\n                \"mean_lead_time\": round(float(ch_grp[\"lead_time_generations\"].mean()), 2),\n                \"mean_p\": round(float(ch_grp[\"p_value\"].mean()), 4),\n            }\n        summary_by_alpha[alpha_key] = {\n            \"n_runs\": len(grp[\"run_id\"].unique()),\n            \"n_total_pairs\": len(grp),\n            \"overall_sig_rate\": round(float(grp[\"is_significant\"].mean()), 3),\n            \"channels\": channel_summaries,\n        }\n\n    # 6. Phase boundary detection\n    boundaries = detect_phase_boundary(df)\n\n    # 7. Build full output JSON\n    output = {\n        \"meta\": {\n            \"n_runs_total\": len(runs),\n            \"n_runs_analyzed\": len(df[\"run_id\"].unique()),\n            \"n_runs_skipped\": len(skipped),\n            \"skipped\": skipped,\n            \"channels\": [f\"{c}_to_{d}\" for c, d in CHANNELS],\n            \"max_lag\": args.max_lag,\n            \"n_permutations\": args.n_permutations,\n            \"significance_threshold\": 0.05,\n        },\n        \"summary_by_alpha\": summary_by_alpha,\n        \"phase_boundaries\": {k: v for k, v in boundaries.items()},\n        \"per_run\": all_rows,\n    }\n\n    json_path = os.path.join(args.output_dir, \"phase_diagram.json\")\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2, default=str)\n    print(f\"Saved {json_path}\")\n\n    # 8. Console summary\n    print(\"\\n\" + \"=\" * 60)\n    print(\"ALPHA-SWEEP ANALYSIS SUMMARY\")\n    print(\"=\" * 60)\n    print(f\"Runs analyzed: {len(df['run_id'].unique())}/{len(runs)}\")\n    print(f\"Alpha values: {sorted(df['alpha'].unique())}\")\n\n    print(\"\\nSignificance rate by alpha:\")\n    for alpha_key in sorted(summary_by_alpha.keys()):\n        s = summary_by_alpha[alpha_key]\n        print(f\"  alpha={alpha_key}: {s['overall_sig_rate']:.0%} \"\n              f\"({s['n_runs']} runs)\")\n\n    print(\"\\nPhase boundaries (canary lead sig → not-sig):\")\n    for channel, boundary in sorted(boundaries.items()):\n        print(f\"  {channel}: alpha = {boundary}\")\n\n    print(f\"\\nResults saved to {args.output_dir}/\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYTHON_EOF",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T21:22:25.775113+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T21:22:25.775272+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "cd /root/autodl-tmp/distrib_canary_collapse && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python analyze_alpha_sweep.py --help",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "cd /root/autodl-tmp/distrib_canary_collapse && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python analyze_alpha_sweep.py --help",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T21:22:25.775412+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"usage: analyze_alpha_sweep.py [-h] [--results-dir RESULTS_DIR]\\n                              [--output-dir OUTPUT_DIR] [--max-lag MAX_LAG]\\n                              [--n-permutations N_PERMUTATIONS]\\n\\nAlpha-sweep aggregation analysis for canary collapse\\n\\noptions:\\n  -h, --help            show this help message and exit\\n  --results-dir RESULTS_DIR\\n                        Directory containing alpha_sweep run dirs\\n  --output-dir OUTPUT_DIR\\n                        Output directory\\n  --max-lag MAX_LAG     Maximum lag for cross-correlation\\n  --n-permutations N_PERMUTATIONS\\n                        Number of permutations for significance test\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.26}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T21:22:25.775550+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "cd /root/autodl-tmp/distrib_canary_collapse && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python analyze_alpha_sweep.py --n-permutations 1000",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "cd /root/autodl-tmp/distrib_canary_collapse && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python analyze_alpha_sweep.py --n-permutations 1000",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T21:22:25.775701+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Discovered 2 runs:\\n  a000_s42: alpha=0.0, seed=42\\n  a025_s42: alpha=0.25, seed=42\\n\\nAnalyzing a000_s42 (6 generations)...\\n    token_entropy_to_distinct_1: lag=2, r=-0.925, p=0.5704\\n    token_entropy_to_distinct_2: lag=2, r=-0.917, p=0.5435\\n    token_entropy_to_distinct_3: lag=2, r=-0.924, p=0.5834\\n    token_entropy_to_perplexity: lag=0, r=-0.996, p=0.1698\\n    token_entropy_to_ece: lag=2, r=-0.829, p=0.8352\\n    ece_to_perplexity: lag=-3, r=0.980, p=0.3077\\n    ece_to_distinct_1: lag=-2, r=0.987, p=0.3297\\n  SKIP a025_s42: only 1 generations (need 4)\\n\\nSaved results/alpha_sweep_analysis/phase_diagram.csv (7 rows)\\nSaved results/alpha_sweep_analysis/phase_diagram.json\\n\\n============================================================\\nALPHA-SWEEP ANALYSIS SUMMARY\\n============================================================\\nRuns analyzed: 1/2\\nAlpha values: [np.float64(0.0)]\\n\\nSignificance rate by alpha:\\n  alpha=0.00: 0% (1 runs)\\n\\nPhase boundaries (canary lead sig → not-sig):\\n  ece_to_distinct_1: alpha = below_min\\n  ece_to_perplexity: alpha = below_min\\n  token_entropy_to_distinct_1: alpha = below_min\\n  token_entropy_to_distinct_2: alpha = below_min\\n  token_entropy_to_distinct_3: alpha = below_min\\n  token_entropy_to_ece: alpha = below_min\\n  token_entropy_to_perplexity: alpha = below_min\\n\\nResults saved to results/alpha_sweep_analysis/\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T21:22:25.775851+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep_analysis/phase_diagram.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep_analysis/phase_diagram.csv",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T21:22:25.775979+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"alpha,seed,run_id,channel,canary,downstream,lag,r_value,p_value,is_significant,canary_leads,lead_time_generations,n_generations\\n0.0,42,a000_s42,token_entropy_to_distinct_1,token_entropy,distinct_1,2,-0.9255,0.5704,False,False,0,6\\n0.0,42,a000_s42,token_entropy_to_distinct_2,token_entropy,distinct_2,2,-0.9166,0.5435,False,False,0,6\\n0.0,42,a000_s42,token_entropy_to_distinct_3,token_entropy,distinct_3,2,-0.9239,0.5834,False,False,0,6\\n0.0,42,a000_s42,token_entropy_to_perplexity,token_entropy,perplexity,0,-0.9962,0.1698,False,False,0,6\\n0.0,42,a000_s42,token_entropy_to_ece,token_entropy,ece,2,-0.8293,0.8352,False,False,0,6\\n0.0,42,a000_s42,ece_to_perplexity,ece,perplexity,-3,0.9797,0.3077,False,True,3,6\\n0.0,42,a000_s42,ece_to_distinct_1,ece,distinct_1,-2,0.9873,0.3297,False,True,2,6\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-14T21:22:25.776130+00:00_

脚本已部署并验证通过。

**输出**:
- `results/alpha_sweep_analysis/phase_diagram.csv` — 每行一个 (α, seed, channel) 组合，包含 lag, r_value, p_value, is_significant, lead_time_generations
- `results/alpha_sweep_analysis/phase_diagram.json` — 完整结果 + 按 α 分组汇总 + phase boundary 检测

**当前状态**: 只有 `a000_s42`（6 代）可分析，`a025_s42` 仅 1 代被跳过。α=0.0 下所有 channel 的 permutation test 均不显著（样本量太小，只有 6 个时间点）。等更多 α 和 seed 的实验跑完后，重新执行即可获得完整 phase diagram 数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_alpha_sweep_aggregation_script_20260514T211956"
}
```

</details>

---
