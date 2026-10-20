# analysis qwen random results

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/chats/worker_analysis_qwen_random_results_20260514T082541.jsonl`
- **Structured JSON:** [`0ecded3be8857c9de3d3.json`](../../sessions/0e/0ecded3be8857c9de3d3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

29 recorded events

### Tool call

_source line 1 · 2026-05-14T08:28:28.829127+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen_random_results_20260514T082541",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T08:28:28.829693+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen_random_results_20260514T082541",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T08:28:28.829968+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "ls /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s015",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen_random_results_20260514T082541",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "ls /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s015",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T08:28:28.830176+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "ls /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s020",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen_random_results_20260514T082541",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "ls /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s020",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T08:28:28.830364+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "ls /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s025",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen_random_results_20260514T082541",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "ls /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s025",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T08:28:28.830583+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"profiling_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen_random_results_20260514T082541",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T08:28:28.830767+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"profiling_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen_random_results_20260514T082541",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T08:28:28.830937+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"profiling_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen_random_results_20260514T082541",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T08:28:28.831131+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s015/profiling_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen_random_results_20260514T082541",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "cat /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s015/profiling_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T08:28:28.831327+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s020/profiling_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen_random_results_20260514T082541",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "cat /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s020/profiling_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T08:28:28.831542+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "cat /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s025/profiling_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen_random_results_20260514T082541",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "cat /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s025/profiling_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T08:28:28.832303+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"model\\\": \\\"/root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct\\\",\\n    \\\"sparsity_levels\\\": [\\n      0.15\\n    ],\\n    \\\"masking_method\\\": \\\"random\\\",\\n    \\\"head_importance_metric\\\": \\\"none\\\",\\n    \\\"kv_importance_metric\\\": \\\"none\\\",\\n    \\\"segmentation_method\\\": \\\"quantile\\\",\\n    \\\"n_bootstrap\\\": 1000,\\n    \\\"n_problems\\\": 50,\\n    \\\"seed\\\": 42\\n  },\\n  \\\"phase_stats\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"n_tokens\\\": 16289,\\n      \\\"n_segments\\\": 295\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"n_tokens\\\": 32227,\\n      \\\"n_segments\\\": 276\\n    },\\n    \\\"mid_sparsity\\\": {\\n      \\\"n_tokens\\\": 4372,\\n      \\\"n_segments\\\": 26\\n    }\\n  },\\n  \\\"perplexity\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"0.15\\\": {\\n        \\\"dense\\\": 1.0737,\\n        \\\"attn\\\": 1.3939,\\n        \\\"kv\\\": 2.0487,\\n        \\\"both\\\": 4.2076\\n      }\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"0.15\\\": {\\n        \\\"dense\\\": 1.1517,\\n        \\\"attn\\\": 1.7177,\\n        \\\"kv\\\": 3.3253,\\n        \\\"both\\\": 5.4788\\n      }\\n    },\\n    \\\"mid_sparsity\\\": {\\n      \\\"0.15\\\": {\\n        \\\"dense\\\": 1.1322,\\n        \\\"attn\\\": 1.4175,\\n        \\\"kv\\\": 2.3709,\\n        \\\"both\\\": 4.6105\\n      }\\n    }\\n  },\\n  \\\"interaction_index\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"0.15\\\": {\\n        \\\"mean\\\": 1.665213,\\n        \\\"ci_low\\\": 1.098566,\\n        \\\"ci_high\\\": 2.404194,\\n        \\\"median\\\": 0.138132,\\n        \\\"median_ci_low\\\": 0.102537,\\n        \\\"median_ci_high\\\": 0.207418,\\n        \\\"winsorized_mean\\\": 1.004447,\\n        \\\"skewness\\\": 7.1842,\\n        \\\"outlier_count\\\": 6\\n      }\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"0.15\\\": {\\n    
…[truncated 8120 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen_random_results_20260514T082541",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T08:28:28.833025+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"model\\\": \\\"/root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct\\\",\\n    \\\"sparsity_levels\\\": [\\n      0.2\\n    ],\\n    \\\"masking_method\\\": \\\"random\\\",\\n    \\\"head_importance_metric\\\": \\\"none\\\",\\n    \\\"kv_importance_metric\\\": \\\"none\\\",\\n    \\\"segmentation_method\\\": \\\"quantile\\\",\\n    \\\"n_bootstrap\\\": 1000,\\n    \\\"n_problems\\\": 50,\\n    \\\"seed\\\": 42\\n  },\\n  \\\"phase_stats\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"n_tokens\\\": 16289,\\n      \\\"n_segments\\\": 295\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"n_tokens\\\": 32227,\\n      \\\"n_segments\\\": 276\\n    },\\n    \\\"mid_sparsity\\\": {\\n      \\\"n_tokens\\\": 4372,\\n      \\\"n_segments\\\": 26\\n    }\\n  },\\n  \\\"perplexity\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"0.2\\\": {\\n        \\\"dense\\\": 1.0737,\\n        \\\"attn\\\": 1.6115,\\n        \\\"kv\\\": 2.5041,\\n        \\\"both\\\": 5.9394\\n      }\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"0.2\\\": {\\n        \\\"dense\\\": 1.1517,\\n        \\\"attn\\\": 75.631,\\n        \\\"kv\\\": 4.3535,\\n        \\\"both\\\": 140.6269\\n      }\\n    },\\n    \\\"mid_sparsity\\\": {\\n      \\\"0.2\\\": {\\n        \\\"dense\\\": 1.1322,\\n        \\\"attn\\\": 1.7583,\\n        \\\"kv\\\": 3.0658,\\n        \\\"both\\\": 10.5578\\n      }\\n    }\\n  },\\n  \\\"interaction_index\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"0.2\\\": {\\n        \\\"mean\\\": 2.58579,\\n        \\\"ci_low\\\": 1.769404,\\n        \\\"ci_high\\\": 3.501692,\\n        \\\"median\\\": 0.48549,\\n        \\\"median_ci_low\\\": 0.304626,\\n        \\\"median_ci_high\\\": 0.658814,\\n        \\\"winsorized_mean\\\": 1.80021,\\n        \\\"skewness\\\": 5.4038,\\n        \\\"outlier_count\\\": 6\\n      }\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"0.2\\\": {\\n        \\
…[truncated 8123 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen_random_results_20260514T082541",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T08:28:28.833577+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"model\\\": \\\"/root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct\\\",\\n    \\\"sparsity_levels\\\": [\\n      0.25\\n    ],\\n    \\\"masking_method\\\": \\\"random\\\",\\n    \\\"head_importance_metric\\\": \\\"none\\\",\\n    \\\"kv_importance_metric\\\": \\\"none\\\",\\n    \\\"segmentation_method\\\": \\\"quantile\\\",\\n    \\\"n_bootstrap\\\": 1000,\\n    \\\"n_problems\\\": 50,\\n    \\\"seed\\\": 42\\n  },\\n  \\\"phase_stats\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"n_tokens\\\": 16289,\\n      \\\"n_segments\\\": 295\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"n_tokens\\\": 32227,\\n      \\\"n_segments\\\": 276\\n    },\\n    \\\"mid_sparsity\\\": {\\n      \\\"n_tokens\\\": 4372,\\n      \\\"n_segments\\\": 26\\n    }\\n  },\\n  \\\"perplexity\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"0.25\\\": {\\n        \\\"dense\\\": 1.0737,\\n        \\\"attn\\\": 2.7753,\\n        \\\"kv\\\": 3.3137,\\n        \\\"both\\\": 12.3954\\n      }\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"0.25\\\": {\\n        \\\"dense\\\": 1.1517,\\n        \\\"attn\\\": 476.0375,\\n        \\\"kv\\\": 6.225,\\n        \\\"both\\\": 345.0363\\n      }\\n    },\\n    \\\"mid_sparsity\\\": {\\n      \\\"0.25\\\": {\\n        \\\"dense\\\": 1.1322,\\n        \\\"attn\\\": 2.4944,\\n        \\\"kv\\\": 4.187,\\n        \\\"both\\\": 15.8108\\n      }\\n    }\\n  },\\n  \\\"interaction_index\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"0.25\\\": {\\n        \\\"mean\\\": 6.549833,\\n        \\\"ci_low\\\": 4.349383,\\n        \\\"ci_high\\\": 9.512776,\\n        \\\"median\\\": 1.604343,\\n        \\\"median_ci_low\\\": 1.234275,\\n        \\\"median_ci_high\\\": 1.856578,\\n        \\\"winsorized_mean\\\": 4.267976,\\n        \\\"skewness\\\": 7.7254,\\n        \\\"outlier_count\\\": 7\\n      }\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"0.25\\\": {\\n
…[truncated 8123 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen_random_results_20260514T082541",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T08:28:28.833965+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "bf16_qw_rand_s015",
  "field": "metrics",
  "value": "{'interaction_index': {'high': {'mean': 1.665213, 'ci': [1.098566, 2.404194], 'median': 0.138132, 'median_ci': [0.102537, 0.207418], 'winsorized_mean': 1.004447, 'skewness': 7.1842}, 'mid': {'mean': 1.697467, 'ci': [0.447329, 3.461161], 'median': 0.219399, 'median_ci': [-0.004845, 0.662126], 'winsorized_mean': 1.403836, 'skewness': 3.2101}, 'low': {'mean': 1.408189, 'ci': [0.835819, 2.060023], 'median': 0.187842, 'median_ci': [0.096196, 0.313935], 'winsorized_mean': 0.940326, 'skewness': 7.1113}}, 'perplexity': {'high': {'dense': 1.0737, 'attn': 1.3939, 'kv': 2.0487, 'both': 4.2076}, 'mid': {'dense': 1.1322, 'attn': 1.4175, 'kv': 2.3709, 'both': 4.6105}, 'low': {'dense': 1.1517, 'attn': 1.7177, 'kv': 3.3253, 'both': 5.4788}}, 'phase_stats': {'high': {'n_tokens': 16289, 'n_segments': 295}, 'mid': {'n_tokens': 4372, 'n_segments': 26}, 'low': {'n_tokens': 32227, 'n_segments': 276}}, 'n_problems': 50, 'pass_fail': {'ci_overlap': True, 'sign_reversal': True, 'overall': 'FAIL'}, 'median_difference': 0.04971}",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen_random_results_20260514T082541",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "bf16_qw_rand_s015",
    "field": "metrics",
    "value": "{'interaction_index': {'high': {'mean': 1.665213, 'ci': [1.098566, 2.404194], 'median': 0.138132, 'median_ci': [0.102537, 0.207418], 'winsorized_mean': 1.004447, 'skewness': 7.1842}, 'mid': {'mean': 1.697467, 'ci': [0.447329, 3.461161], 'median': 0.219399, 'median_ci': [-0.004845, 0.662126], 'winsorized_mean': 1.403836, 'skewness': 3.2101}, 'low': {'mean': 1.408189, 'ci': [0.835819, 2.060023], 'median': 0.187842, 'median_ci': [0.096196, 0.313935], 'winsorized_mean': 0.940326, 'skewness': 7.1113}}, 'perplexity': {'high': {'dense': 1.0737, 'attn': 1.3939, 'kv': 2.0487, 'both': 4.2076}, 'mid': {'dense': 1.1322, 'attn': 1.4175, 'kv': 2.3709, 'both': 4.6105}, 'low': {'dense': 1.1517, 'attn': 1.7177, 'kv': 3.3253, 'both': 5.4788}}, 'phase_stats': {'high': {'n_tokens': 16289, 'n_segments': 295}, 'mid': {'n_tokens': 4372, 'n_segments': 26}, 'low': {'n_tokens': 32227, 'n_segments': 276}}, 'n_problems': 50, 'pass_fail': {'ci_overlap': True, 'sign_reversal': True, 'overall': 'FAIL'}, 'median_difference': 0.04971}",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T08:28:28.834328+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"bf16_qw_rand_s015\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:39:34.607Z\", \"updated_at\": \"2026-05-14T08:27:21.728Z\", \"hypothesis\": \"D020 bf16 全量重跑: Qwen2.5-7B-Instruct random masking s=0.15, bf16 dtype. Cross-model 配对对照。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s015 --sparsity_levels 0.15 --masking_method random --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:0\"], \"pid\": \"95899\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_qw_rand_s015.log\", \"submitted_at\": \"2026-05-14T07:55:27.130Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": null, \"wall_clock_seconds\": 1790.5, \"gpu_hours\": 0.5}, \"reproduce\": {\"finished_at\": \"2026-05-14T08:14:18.084Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:14:20.510775+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s015\", \"completed_at\": \"2026-05-14T08:25:17.665Z\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 1.665213, \"ci\": [1.098566, 2.404194], \"median\": 0.138132, \"median_ci\": [0.102537, 0.207418], \"winsorized_mean\": 1.004447, \"skewness\": 7.1842}, \"mid\": {\"mean\": 1.697467, \"ci\": [0.447329, 3.461161], \"median\": 0.219399, \"median_ci\": [-0.004845, 0.662126], \"winsorized_me
…[truncated 860 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen_random_results_20260514T082541",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T08:28:28.834641+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "bf16_qw_rand_s020",
  "field": "metrics",
  "value": "{'interaction_index': {'high': {'mean': 2.58579, 'ci': [1.769404, 3.501692], 'median': 0.48549, 'median_ci': [0.304626, 0.658814], 'winsorized_mean': 1.80021, 'skewness': 5.4038}, 'mid': {'mean': 5.69684, 'ci': [1.69004, 12.276143], 'median': 0.76699, 'median_ci': [0.482838, 3.392541], 'winsorized_mean': 4.304174, 'skewness': 3.526}, 'low': {'mean': 65.915714, 'ci': [-18.581948, 221.709429], 'median': 0.614438, 'median_ci': [0.484725, 0.848787], 'winsorized_mean': 2.389244, 'skewness': 16.2163}}, 'perplexity': {'high': {'dense': 1.0737, 'attn': 1.6115, 'kv': 2.5041, 'both': 5.9394}, 'mid': {'dense': 1.1322, 'attn': 1.7583, 'kv': 3.0658, 'both': 10.5578}, 'low': {'dense': 1.1517, 'attn': 75.631, 'kv': 4.3535, 'both': 140.6269}}, 'phase_stats': {'high': {'n_tokens': 16289, 'n_segments': 295}, 'mid': {'n_tokens': 4372, 'n_segments': 26}, 'low': {'n_tokens': 32227, 'n_segments': 276}}, 'n_problems': 50, 'pass_fail': {'ci_overlap': True, 'sign_reversal': True, 'overall': 'FAIL'}, 'median_difference': 0.128948}",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen_random_results_20260514T082541",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "bf16_qw_rand_s020",
    "field": "metrics",
    "value": "{'interaction_index': {'high': {'mean': 2.58579, 'ci': [1.769404, 3.501692], 'median': 0.48549, 'median_ci': [0.304626, 0.658814], 'winsorized_mean': 1.80021, 'skewness': 5.4038}, 'mid': {'mean': 5.69684, 'ci': [1.69004, 12.276143], 'median': 0.76699, 'median_ci': [0.482838, 3.392541], 'winsorized_mean': 4.304174, 'skewness': 3.526}, 'low': {'mean': 65.915714, 'ci': [-18.581948, 221.709429], 'median': 0.614438, 'median_ci': [0.484725, 0.848787], 'winsorized_mean': 2.389244, 'skewness': 16.2163}}, 'perplexity': {'high': {'dense': 1.0737, 'attn': 1.6115, 'kv': 2.5041, 'both': 5.9394}, 'mid': {'dense': 1.1322, 'attn': 1.7583, 'kv': 3.0658, 'both': 10.5578}, 'low': {'dense': 1.1517, 'attn': 75.631, 'kv': 4.3535, 'both': 140.6269}}, 'phase_stats': {'high': {'n_tokens': 16289, 'n_segments': 295}, 'mid': {'n_tokens': 4372, 'n_segments': 26}, 'low': {'n_tokens': 32227, 'n_segments': 276}}, 'n_problems': 50, 'pass_fail': {'ci_overlap': True, 'sign_reversal': True, 'overall': 'FAIL'}, 'median_difference': 0.128948}",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T08:28:28.835025+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"bf16_qw_rand_s020\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:39:35.500Z\", \"updated_at\": \"2026-05-14T08:27:28.862Z\", \"hypothesis\": \"D020 bf16 全量重跑: Qwen2.5-7B-Instruct random masking s=0.20, bf16 dtype. Cross-model 配对对照。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s020 --sparsity_levels 0.20 --masking_method random --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:2\"], \"pid\": \"96294\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_qw_rand_s020.log\", \"submitted_at\": \"2026-05-14T07:58:38.430Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": null, \"wall_clock_seconds\": 1600.1, \"gpu_hours\": 0.44}, \"reproduce\": {\"finished_at\": \"2026-05-14T08:18:22.751Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:18:28.103231+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s020\", \"completed_at\": \"2026-05-14T08:25:18.578Z\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 2.58579, \"ci\": [1.769404, 3.501692], \"median\": 0.48549, \"median_ci\": [0.304626, 0.658814], \"winsorized_mean\": 1.80021, \"skewness\": 5.4038}, \"mid\": {\"mean\": 5.69684, \"ci\": [1.69004, 12.276143], \"median\": 0.76699, \"median_ci\": [0.482838, 3.392541], \"winsorized_mean\":
…[truncated 864 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen_random_results_20260514T082541",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T08:28:28.835312+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "bf16_qw_rand_s025",
  "field": "metrics",
  "value": "{'interaction_index': {'high': {'mean': 6.549833, 'ci': [4.349383, 9.512776], 'median': 1.604343, 'median_ci': [1.234275, 1.856578], 'winsorized_mean': 4.267976, 'skewness': 7.7254}, 'mid': {'mean': 8.520076, 'ci': [3.599746, 15.539762], 'median': 2.222455, 'median_ci': [1.666917, 4.568741], 'winsorized_mean': 8.400572, 'skewness': 2.5443}, 'low': {'mean': -34.53659, 'ci': [-203.335784, 120.009066], 'median': 2.264141, 'median_ci': [1.757151, 3.452652], 'winsorized_mean': 6.097786, 'skewness': -5.9085}}, 'perplexity': {'high': {'dense': 1.0737, 'attn': 2.7753, 'kv': 3.3137, 'both': 12.3954}, 'mid': {'dense': 1.1322, 'attn': 2.4944, 'kv': 4.187, 'both': 15.8108}, 'low': {'dense': 1.1517, 'attn': 476.0375, 'kv': 6.225, 'both': 345.0363}}, 'phase_stats': {'high': {'n_tokens': 16289, 'n_segments': 295}, 'mid': {'n_tokens': 4372, 'n_segments': 26}, 'low': {'n_tokens': 32227, 'n_segments': 276}}, 'n_problems': 50, 'pass_fail': {'ci_overlap': False, 'sign_reversal': False, 'overall': 'FAIL'}, 'median_difference': 0.659798}",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen_random_results_20260514T082541",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "bf16_qw_rand_s025",
    "field": "metrics",
    "value": "{'interaction_index': {'high': {'mean': 6.549833, 'ci': [4.349383, 9.512776], 'median': 1.604343, 'median_ci': [1.234275, 1.856578], 'winsorized_mean': 4.267976, 'skewness': 7.7254}, 'mid': {'mean': 8.520076, 'ci': [3.599746, 15.539762], 'median': 2.222455, 'median_ci': [1.666917, 4.568741], 'winsorized_mean': 8.400572, 'skewness': 2.5443}, 'low': {'mean': -34.53659, 'ci': [-203.335784, 120.009066], 'median': 2.264141, 'median_ci': [1.757151, 3.452652], 'winsorized_mean': 6.097786, 'skewness': -5.9085}}, 'perplexity': {'high': {'dense': 1.0737, 'attn': 2.7753, 'kv': 3.3137, 'both': 12.3954}, 'mid': {'dense': 1.1322, 'attn': 2.4944, 'kv': 4.187, 'both': 15.8108}, 'low': {'dense': 1.1517, 'attn': 476.0375, 'kv': 6.225, 'both': 345.0363}}, 'phase_stats': {'high': {'n_tokens': 16289, 'n_segments': 295}, 'mid': {'n_tokens': 4372, 'n_segments': 26}, 'low': {'n_tokens': 32227, 'n_segments': 276}}, 'n_problems': 50, 'pass_fail': {'ci_overlap': False, 'sign_reversal': False, 'overall': 'FAIL'}, 'median_difference': 0.659798}",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T08:28:28.835720+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"bf16_qw_rand_s025\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:39:36.710Z\", \"updated_at\": \"2026-05-14T08:27:36.320Z\", \"hypothesis\": \"D020 bf16 全量重跑: Qwen2.5-7B-Instruct random masking s=0.25, bf16 dtype. Cross-model 配对对照。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s025 --sparsity_levels 0.25 --masking_method random --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:3\"], \"pid\": \"96437\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_qw_rand_s025.log\", \"submitted_at\": \"2026-05-14T07:58:41.225Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": null, \"wall_clock_seconds\": 1598.1, \"gpu_hours\": 0.44}, \"reproduce\": {\"finished_at\": \"2026-05-14T08:18:30.530Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:18:34.069307+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s025\", \"completed_at\": \"2026-05-14T08:25:19.332Z\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 6.549833, \"ci\": [4.349383, 9.512776], \"median\": 1.604343, \"median_ci\": [1.234275, 1.856578], \"winsorized_mean\": 4.267976, \"skewness\": 7.7254}, \"mid\": {\"mean\": 8.520076, \"ci\": [3.599746, 15.539762], \"median\": 2.222455, \"median_ci\": [1.666917, 4.568741], \"winsorized_m
…[truncated 874 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen_random_results_20260514T082541",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T08:28:28.835967+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "bf16_qw_rand_s015",
  "field": "conclusion",
  "value": "success",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen_random_results_20260514T082541",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "bf16_qw_rand_s015",
    "field": "conclusion",
    "value": "success",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T08:28:28.836239+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"bf16_qw_rand_s015\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:39:34.607Z\", \"updated_at\": \"2026-05-14T08:27:37.248Z\", \"hypothesis\": \"D020 bf16 全量重跑: Qwen2.5-7B-Instruct random masking s=0.15, bf16 dtype. Cross-model 配对对照。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s015 --sparsity_levels 0.15 --masking_method random --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:0\"], \"pid\": \"95899\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_qw_rand_s015.log\", \"submitted_at\": \"2026-05-14T07:55:27.130Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": null, \"wall_clock_seconds\": 1790.5, \"gpu_hours\": 0.5}, \"reproduce\": {\"finished_at\": \"2026-05-14T08:14:18.084Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:14:20.510775+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s015\", \"completed_at\": \"2026-05-14T08:25:17.665Z\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 1.665213, \"ci\": [1.098566, 2.404194], \"median\": 0.138132, \"median_ci\": [0.102537, 0.207418], \"winsorized_mean\": 1.004447, \"skewness\": 7.1842}, \"mid\": {\"mean\": 1.697467, \"ci\": [0.447329, 3.461161], \"median\": 0.219399, \"median_ci\": [-0.004845, 0.662126], \"winsorized_mea
…[truncated 859 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen_random_results_20260514T082541",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T08:28:28.836489+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "bf16_qw_rand_s020",
  "field": "conclusion",
  "value": "success",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen_random_results_20260514T082541",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "bf16_qw_rand_s020",
    "field": "conclusion",
    "value": "success",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-14T08:28:28.836680+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "bf16_qw_rand_s025",
  "field": "conclusion",
  "value": "success",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen_random_results_20260514T082541",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "bf16_qw_rand_s025",
    "field": "conclusion",
    "value": "success",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T08:28:28.836959+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"bf16_qw_rand_s020\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:39:35.500Z\", \"updated_at\": \"2026-05-14T08:27:38.167Z\", \"hypothesis\": \"D020 bf16 全量重跑: Qwen2.5-7B-Instruct random masking s=0.20, bf16 dtype. Cross-model 配对对照。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s020 --sparsity_levels 0.20 --masking_method random --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:2\"], \"pid\": \"96294\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_qw_rand_s020.log\", \"submitted_at\": \"2026-05-14T07:58:38.430Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": null, \"wall_clock_seconds\": 1600.1, \"gpu_hours\": 0.44}, \"reproduce\": {\"finished_at\": \"2026-05-14T08:18:22.751Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:18:28.103231+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s020\", \"completed_at\": \"2026-05-14T08:25:18.578Z\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 2.58579, \"ci\": [1.769404, 3.501692], \"median\": 0.48549, \"median_ci\": [0.304626, 0.658814], \"winsorized_mean\": 1.80021, \"skewness\": 5.4038}, \"mid\": {\"mean\": 5.69684, \"ci\": [1.69004, 12.276143], \"median\": 0.76699, \"median_ci\": [0.482838, 3.392541], \"winsorized_mean\": 
…[truncated 862 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen_random_results_20260514T082541",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T08:28:28.837459+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"bf16_qw_rand_s025\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:39:36.710Z\", \"updated_at\": \"2026-05-14T08:27:38.764Z\", \"hypothesis\": \"D020 bf16 全量重跑: Qwen2.5-7B-Instruct random masking s=0.25, bf16 dtype. Cross-model 配对对照。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s025 --sparsity_levels 0.25 --masking_method random --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:3\"], \"pid\": \"96437\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_qw_rand_s025.log\", \"submitted_at\": \"2026-05-14T07:58:41.225Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": null, \"wall_clock_seconds\": 1598.1, \"gpu_hours\": 0.44}, \"reproduce\": {\"finished_at\": \"2026-05-14T08:18:30.530Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:18:34.069307+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s025\", \"completed_at\": \"2026-05-14T08:25:19.332Z\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 6.549833, \"ci\": [4.349383, 9.512776], \"median\": 1.604343, \"median_ci\": [1.234275, 1.856578], \"winsorized_mean\": 4.267976, \"skewness\": 7.7254}, \"mid\": {\"mean\": 8.520076, \"ci\": [3.599746, 15.539762], \"median\": 2.222455, \"median_ci\": [1.666917, 4.568741], \"winsorized_me
…[truncated 874 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen_random_results_20260514T082541",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T08:28:28.837812+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "bf16_qw_rand_s025",
  "field": "metrics",
  "value": "{'interaction_index': {'high': {'mean': 6.549833, 'ci': [4.349383, 9.512776], 'median': 1.604343, 'median_ci': [1.234275, 1.856578], 'winsorized_mean': 4.267976, 'skewness': 7.7254}, 'mid': {'mean': 8.520076, 'ci': [3.599746, 15.539762], 'median': 2.222455, 'median_ci': [1.666917, 4.568741], 'winsorized_mean': 8.400572, 'skewness': 2.5443}, 'low': {'mean': -34.53659, 'ci': [-203.335784, 120.009066], 'median': 2.264141, 'median_ci': [1.757151, 3.452652], 'winsorized_mean': 6.097786, 'skewness': -5.9085}}, 'perplexity': {'high': {'dense': 1.0737, 'attn': 2.7753, 'kv': 3.3137, 'both': 12.3954}, 'mid': {'dense': 1.1322, 'attn': 2.4944, 'kv': 4.187, 'both': 15.8108}, 'low': {'dense': 1.1517, 'attn': 476.0375, 'kv': 6.225, 'both': 345.0363}}, 'phase_stats': {'high': {'n_tokens': 16289, 'n_segments': 295}, 'mid': {'n_tokens': 4372, 'n_segments': 26}, 'low': {'n_tokens': 32227, 'n_segments': 276}}, 'n_problems': 50, 'pass_fail': {'ci_overlap': True, 'sign_reversal': False, 'overall': 'FAIL'}, 'median_difference': 0.659798}",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen_random_results_20260514T082541",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "bf16_qw_rand_s025",
    "field": "metrics",
    "value": "{'interaction_index': {'high': {'mean': 6.549833, 'ci': [4.349383, 9.512776], 'median': 1.604343, 'median_ci': [1.234275, 1.856578], 'winsorized_mean': 4.267976, 'skewness': 7.7254}, 'mid': {'mean': 8.520076, 'ci': [3.599746, 15.539762], 'median': 2.222455, 'median_ci': [1.666917, 4.568741], 'winsorized_mean': 8.400572, 'skewness': 2.5443}, 'low': {'mean': -34.53659, 'ci': [-203.335784, 120.009066], 'median': 2.264141, 'median_ci': [1.757151, 3.452652], 'winsorized_mean': 6.097786, 'skewness': -5.9085}}, 'perplexity': {'high': {'dense': 1.0737, 'attn': 2.7753, 'kv': 3.3137, 'both': 12.3954}, 'mid': {'dense': 1.1322, 'attn': 2.4944, 'kv': 4.187, 'both': 15.8108}, 'low': {'dense': 1.1517, 'attn': 476.0375, 'kv': 6.225, 'both': 345.0363}}, 'phase_stats': {'high': {'n_tokens': 16289, 'n_segments': 295}, 'mid': {'n_tokens': 4372, 'n_segments': 26}, 'low': {'n_tokens': 32227, 'n_segments': 276}}, 'n_problems': 50, 'pass_fail': {'ci_overlap': True, 'sign_reversal': False, 'overall': 'FAIL'}, 'median_difference': 0.659798}",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T08:28:28.838171+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"bf16_qw_rand_s025\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:39:36.710Z\", \"updated_at\": \"2026-05-14T08:28:15.934Z\", \"hypothesis\": \"D020 bf16 全量重跑: Qwen2.5-7B-Instruct random masking s=0.25, bf16 dtype. Cross-model 配对对照。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s025 --sparsity_levels 0.25 --masking_method random --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:3\"], \"pid\": \"96437\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_qw_rand_s025.log\", \"submitted_at\": \"2026-05-14T07:58:41.225Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": null, \"wall_clock_seconds\": 1598.1, \"gpu_hours\": 0.44}, \"reproduce\": {\"finished_at\": \"2026-05-14T08:18:30.530Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:18:34.069307+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s025\", \"completed_at\": \"2026-05-14T08:25:19.332Z\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 6.549833, \"ci\": [4.349383, 9.512776], \"median\": 1.604343, \"median_ci\": [1.234275, 1.856578], \"winsorized_mean\": 4.267976, \"skewness\": 7.7254}, \"mid\": {\"mean\": 8.520076, \"ci\": [3.599746, 15.539762], \"median\": 2.222455, \"median_ci\": [1.666917, 4.568741], \"winsorized_me
…[truncated 873 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen_random_results_20260514T082541",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-14T08:28:28.838488+00:00_

Registry 全部更新完成。汇总：

| exp_id | sparsity | median (high→mid→low) | median_diff | pass_fail | n_problems |
|--------|----------|----------------------|-------------|-----------|------------|
| bf16_qw_rand_s015 | 0.15 | 0.138 → 0.219 → 0.188 | **+0.050** | **FAIL** (sign_reversal + ci_overlap) | 50 |
| bf16_qw_rand_s020 | 0.20 | 0.485 → 0.767 → 0.614 | **+0.129** | **FAIL** (sign_reversal + ci_overlap) | 50 |
| bf16_qw_rand_s025 | 0.25 | 1.604 → 2.222 → 2.264 | **+0.660** | **FAIL** (ci_overlap, no sign reversal) | 50 |

符合预期：random masking 在 Qwen2.5-7B-Instruct 上全部 FAIL。

- s015/s020 存在 sign reversal（mid > low，违反单调递增），且 CI 重叠严重
- s025 的 median 碰巧单调递增，但各 phase CI 大幅重叠，无统计显著性
- median_difference 均为小正值（0.05~0.66），远小于 importance-based masking 实验中的差异
- 与 DeepSeek random 实验结果一致：random masking 不产生有意义的 phase 间单调效应

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_qwen_random_results_20260514T082541"
}
```

</details>

---
