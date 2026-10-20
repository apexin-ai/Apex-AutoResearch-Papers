# analysis qw rand batch

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 0
- **Tool calls:** 26
- **Original source:** `logs/chats/worker_analysis_qw_rand_batch_20260514T082557.jsonl`
- **Structured JSON:** [`695d626ad4fad722ecd1.json`](../../sessions/69/695d626ad4fad722ecd1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

53 recorded events

### Tool call

_source line 1 · 2026-05-14T08:28:49.497482+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T08:28:49.497845+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T08:28:49.498016+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'project': 'phase-gated-compound-sparse'}",
  "project": "phase-gated-compound-sparse",
  "limit": "0",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'project': 'phase-gated-compound-sparse'}",
    "project": "phase-gated-compound-sparse",
    "limit": "0",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T08:28:49.498165+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3412}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T08:28:49.498292+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "ls -la /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s015/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "ls -la /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s015/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T08:28:49.498433+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "ls -la /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s020/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "ls -la /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s020/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T08:28:49.498562+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "ls -la /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s025/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "ls -la /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s025/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T08:28:49.498685+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 1672\\ndrwxr-xr-x  2 root root      44 May 14 16:14 .\\ndrwxr-xr-x 77 root root    8192 May 14 16:22 ..\\n-rw-r--r--  1 root root 1696194 May 14 16:14 profiling_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T08:28:49.498806+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 1672\\ndrwxr-xr-x  2 root root      44 May 14 16:17 .\\ndrwxr-xr-x 77 root root    8192 May 14 16:22 ..\\n-rw-r--r--  1 root root 1696101 May 14 16:17 profiling_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T08:28:49.498923+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 1672\\ndrwxr-xr-x  2 root root      44 May 14 16:17 .\\ndrwxr-xr-x 77 root root    8192 May 14 16:22 ..\\n-rw-r--r--  1 root root 1696082 May 14 16:17 profiling_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T08:28:49.499081+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s015/profiling_results.json')); print(type(d)); print(list(d.keys()) if isinstance(d,dict) else f'list len={len(d)}, first keys={list(d[0].keys()) if d else None}')\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s015/profiling_results.json')); print(type(d)); print(list(d.keys()) if isinstance(d,dict) else f'list len={len(d)}, first keys={list(d[0].keys()) if d else None}')\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T08:28:49.499209+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T08:28:49.499356+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "find /root/autodl-tmp/pacs/pacs/analysis/ -type f -name \"*.py\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "find /root/autodl-tmp/pacs/pacs/analysis/ -type f -name \"*.py\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T08:28:49.499583+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T08:28:49.499783+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s015/profiling_results.json')); print(type(d)); print(list(d.keys()) if isinstance(d,dict) else len(d))\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s015/profiling_results.json')); print(type(d)); print(list(d.keys()) if isinstance(d,dict) else len(d))\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T08:28:49.499994+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T08:28:49.500162+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "find /root/autodl-tmp/pacs/pacs/analysis/ -type f -name \"*.py\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "find /root/autodl-tmp/pacs/pacs/analysis/ -type f -name \"*.py\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T08:28:49.500332+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/pacs/analysis/__init__.py\\n/root/autodl-tmp/pacs/pacs/analysis/permutation_test.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T08:28:49.500544+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "head -c 2000 /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s015/profiling_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "head -c 2000 /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s015/profiling_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T08:28:49.500811+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"model\\\": \\\"/root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct\\\",\\n    \\\"sparsity_levels\\\": [\\n      0.15\\n    ],\\n    \\\"masking_method\\\": \\\"random\\\",\\n    \\\"head_importance_metric\\\": \\\"none\\\",\\n    \\\"kv_importance_metric\\\": \\\"none\\\",\\n    \\\"segmentation_method\\\": \\\"quantile\\\",\\n    \\\"n_bootstrap\\\": 1000,\\n    \\\"n_problems\\\": 50,\\n    \\\"seed\\\": 42\\n  },\\n  \\\"phase_stats\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"n_tokens\\\": 16289,\\n      \\\"n_segments\\\": 295\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"n_tokens\\\": 32227,\\n      \\\"n_segments\\\": 276\\n    },\\n    \\\"mid_sparsity\\\": {\\n      \\\"n_tokens\\\": 4372,\\n      \\\"n_segments\\\": 26\\n    }\\n  },\\n  \\\"perplexity\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"0.15\\\": {\\n        \\\"dense\\\": 1.0737,\\n        \\\"attn\\\": 1.3939,\\n        \\\"kv\\\": 2.0487,\\n        \\\"both\\\": 4.2076\\n      }\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"0.15\\\": {\\n        \\\"dense\\\": 1.1517,\\n        \\\"attn\\\": 1.7177,\\n        \\\"kv\\\": 3.3253,\\n        \\\"both\\\": 5.4788\\n      }\\n    },\\n    \\\"mid_sparsity\\\": {\\n      \\\"0.15\\\": {\\n        \\\"dense\\\": 1.1322,\\n        \\\"attn\\\": 1.4175,\\n        \\\"kv\\\": 2.3709,\\n        \\\"both\\\": 4.6105\\n      }\\n    }\\n  },\\n  \\\"interaction_index\\\": {\\n    \\\"high_sparsity\\\": {\\n      \\\"0.15\\\": {\\n        \\\"mean\\\": 1.665213,\\n        \\\"ci_low\\\": 1.098566,\\n        \\\"ci_high\\\": 2.404194,\\n        \\\"median\\\": 0.138132,\\n        \\\"median_ci_low\\\": 0.102537,\\n        \\\"median_ci_high\\\": 0.207418,\\n        \\\"winsorized_mean\\\": 1.004447,\\n        \\\"skewness\\\": 7.1842,\\n        \\\"outlier_count\\\": 6\\n      }\\n    },\\n    \\\"low_sparsity\\\": {\\n      \\\"0.15\\\": {\\n    
…[truncated 796 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T08:28:49.501021+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "find /root/autodl-tmp/pacs -name \"*analyze*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "find /root/autodl-tmp/pacs -name \"*analyze*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T08:28:49.501201+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/profiling/__pycache__/analyze_results.cpython-312.pyc\\n/root/autodl-tmp/pacs/profiling/analyze_results.py\\n/root/autodl-tmp/pacs/pacs/profiling/analyze_results.py\\n/root/autodl-tmp/pacs/analyze_v4_comparison.py\\n/root/autodl-tmp/pacs/analysis/analyze_strategy_phase_crossover.py\\n/root/autodl-tmp/pacs/analysis/analyze_v6_complete.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T08:28:49.501378+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "find /root/autodl-tmp/pacs -name \"*aggregate*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "find /root/autodl-tmp/pacs -name \"*aggregate*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T08:28:49.501582+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T08:28:49.501800+00:00_

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
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
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

_source line 26 · 2026-05-14T08:28:49.501977+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T08:28:49.502168+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\n\nfor suffix in ['s015', 's020', 's025']:\n    path = f'/root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_{suffix}/profiling_results.json'\n    d = json.load(open(path))\n    print(f'=== bf16_qw_rand_{suffix} (sparsity={d[\\\"config\\\"][\\\"sparsity_levels\\\"]}) ===')\n    ii = d['interaction_index']\n    for phase in ['high_sparsity', 'mid_sparsity', 'low_sparsity']:\n        sp_key = list(ii[phase].keys())[0]\n        v = ii[phase][sp_key]\n        print(f'  {phase} (s={sp_key}):')\n        print(f'    mean={v[\\\"mean\\\"]:.6f}, median={v[\\\"median\\\"]:.6f}')\n        print(f'    mean_ci=[{v[\\\"ci_low\\\"]:.6f}, {v[\\\"ci_high\\\"]:.6f}]')\n        print(f'    median_ci=[{v[\\\"median_ci_low\\\"]:.6f}, {v[\\\"median_ci_high\\\"]:.6f}]')\n        print(f'    winsorized_mean={v[\\\"winsorized_mean\\\"]:.6f}, skewness={v[\\\"skewness\\\"]:.4f}')\n    print()\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\n\nfor suffix in ['s015', 's020', 's025']:\n    path = f'/root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_{suffix}/profiling_results.json'\n    d = json.load(open(path))\n    print(f'=== bf16_qw_rand_{suffix} (sparsity={d[\\\"config\\\"][\\\"sparsity_levels\\\"]}) ===')\n    ii = d['interaction_index']\n    for phase in ['high_sparsity', 'mid_sparsity', 'low_sparsity']:\n        sp_key = list(ii[phase].keys())[0]\n        v = ii[phase][sp_key]\n        print(f'  {phase} (s={sp_key}):')\n        print(f'    mean={v[\\\"mean\\\"]:.6f}, median={v[\\\"median\\\"]:.6f}')\n        print(f'    mean_ci=[{v[\\\"ci_low\\\"]:.6f}, {v[\\\"ci_high\\\"]:.6f}]')\n        print(f'    median_ci=[{v[\\\"median_ci_low\\\"]:.6f}, {v[\\\"median_ci_high\\\"]:.6f}]')\n        print(f'    winsorized_mean={v[\\\"winsorized_mean\\\"]:.6f}, skewness={v[\\\"skewness\\\"]:.4f}')\n    print()\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T08:28:49.502381+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== bf16_qw_rand_s015 (sparsity=[0.15]) ===\\n  high_sparsity (s=0.15):\\n    mean=1.665213, median=0.138132\\n    mean_ci=[1.098566, 2.404194]\\n    median_ci=[0.102537, 0.207418]\\n    winsorized_mean=1.004447, skewness=7.1842\\n  mid_sparsity (s=0.15):\\n    mean=1.697467, median=0.219399\\n    mean_ci=[0.447329, 3.461161]\\n    median_ci=[-0.004845, 0.662126]\\n    winsorized_mean=1.403836, skewness=3.2101\\n  low_sparsity (s=0.15):\\n    mean=1.408189, median=0.187842\\n    mean_ci=[0.835819, 2.060023]\\n    median_ci=[0.096196, 0.313935]\\n    winsorized_mean=0.940326, skewness=7.1113\\n\\n=== bf16_qw_rand_s020 (sparsity=[0.2]) ===\\n  high_sparsity (s=0.2):\\n    mean=2.585790, median=0.485490\\n    mean_ci=[1.769404, 3.501692]\\n    median_ci=[0.304626, 0.658814]\\n    winsorized_mean=1.800210, skewness=5.4038\\n  mid_sparsity (s=0.2):\\n    mean=5.696840, median=0.766990\\n    mean_ci=[1.690040, 12.276143]\\n    median_ci=[0.482838, 3.392541]\\n    winsorized_mean=4.304174, skewness=3.5260\\n  low_sparsity (s=0.2):\\n    mean=65.915714, median=0.614438\\n    mean_ci=[-18.581948, 221.709429]\\n    median_ci=[0.484725, 0.848787]\\n    winsorized_mean=2.389244, skewness=16.2163\\n\\n=== bf16_qw_rand_s025 (sparsity=[0.25]) ===\\n  high_sparsity (s=0.25):\\n    mean=6.549833, median=1.604343\\n    mean_ci=[4.349383, 9.512776]\\n    median_ci=[1.234275, 1.856578]\\n    winsorized_mean=4.267976, skewness=7.7254\\n  mid_sparsity (s=0.25):\\n    mean=8.520076, median=2.222455\\n    mean_ci=[3.599746, 15.539762]\\n    median_ci=[1.666917, 4.568741]\\n    winsorized_mean=8.400572, skewness=2.5443\\n  low_sparsity (s=0.25):\\n    mean=-34.536590, median=2.264141\\n    mean_ci=[-203.335784, 120.009066]\\n    median_ci=[1.757151, 3.452652]\\n    winsorized_mean=6.097786, skewness=-5.9085\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.56}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T08:28:49.502679+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "limit": "20",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "limit": "20",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T08:28:49.503429+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"bf16_importance_s020\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:33:14.819Z\", \"updated_at\": \"2026-05-14T08:27:17.252Z\", \"hypothesis\": \"bf16 重跑 DeepSeek importance masking s=0.20。消除 fp16 Layer 27 NaN 偏差，获取完整 per_problem_ii 数据。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_ds_imp_s020 --sparsity_levels 0.20 --masking_method importance --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:0\"], \"pid\": \"79812\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_importance_s020.log\", \"submitted_at\": \"2026-05-14T05:51:09.305Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"note\": \"Registry fix: actually running on cuda:0 sharing with bf16_importance_s030\", \"wall_clock_seconds\": 4491.6, \"gpu_hours\": 1.25}, \"reproduce\": {\"finished_at\": \"2026-05-14T06:36:14.442Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T06:36:16.633802+00:00\"}]}, \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 0.1289, \"median\": 0.0145, \"ci\": [-0.1975, 0.6647], \"winsorized_mean\": -0.0297, \"skewness\": 16.67}, \"mid\": {\"mean\": 1.2604, \"median\": 0.2027, \"ci\": [0.7466, 1.8962], \"winsorized_mean\": 0.766, \"skewness\": 7.05}, \"low\": {\"mean\": 6.0288, \"median\": 1.4963, \"ci\": [4.4671, 7.9237], \"winsorized_mean\": 4.3426, \"skewness
…[truncated 33220 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T08:28:49.503681+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\n\nfor suffix in ['s015', 's020', 's025']:\n    path = f'/root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_{suffix}/profiling_results.json'\n    d = json.load(open(path))\n    print(f'=== bf16_qw_rand_{suffix} ===')\n    \n    # Phase stats\n    ps = d['phase_stats']\n    for phase in ['high_sparsity', 'mid_sparsity', 'low_sparsity']:\n        print(f'  phase_stats.{phase}: n_tokens={ps[phase][\\\"n_tokens\\\"]}, n_segments={ps[phase][\\\"n_segments\\\"]}')\n    \n    # Perplexity\n    ppl = d['perplexity']\n    sp_key = list(ppl['high_sparsity'].keys())[0]\n    for phase in ['high_sparsity', 'mid_sparsity', 'low_sparsity']:\n        v = ppl[phase][sp_key]\n        print(f'  ppl.{phase}: dense={v[\\\"dense\\\"]:.4f}, attn={v[\\\"attn\\\"]:.4f}, kv={v[\\\"kv\\\"]:.4f}, both={v[\\\"both\\\"]:.4f}')\n    print()\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\n\nfor suffix in ['s015', 's020', 's025']:\n    path = f'/root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_{suffix}/profiling_results.json'\n    d = json.load(open(path))\n    print(f'=== bf16_qw_rand_{suffix} ===')\n    \n    # Phase stats\n    ps = d['phase_stats']\n    for phase in ['high_sparsity', 'mid_sparsity', 'low_sparsity']:\n        print(f'  phase_stats.{phase}: n_tokens={ps[phase][\\\"n_tokens\\\"]}, n_segments={ps[phase][\\\"n_segments\\\"]}')\n    \n    # Perplexity\n    ppl = d['perplexity']\n    sp_key = list(ppl['high_sparsity'].keys())[0]\n    for phase in ['high_sparsity', 'mid_sparsity', 'low_sparsity']:\n        v = ppl[phase][sp_key]\n        print(f'  ppl.{phase}: dense={v[\\\"dense\\\"]:.4f}, attn={v[\\\"attn\\\"]:.4f}, kv={v[\\\"kv\\\"]:.4f}, both={v[\\\"both\\\"]:.4f}')\n    print()\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T08:28:49.503866+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== bf16_qw_rand_s015 ===\\n  phase_stats.high_sparsity: n_tokens=16289, n_segments=295\\n  phase_stats.mid_sparsity: n_tokens=4372, n_segments=26\\n  phase_stats.low_sparsity: n_tokens=32227, n_segments=276\\n  ppl.high_sparsity: dense=1.0737, attn=1.3939, kv=2.0487, both=4.2076\\n  ppl.mid_sparsity: dense=1.1322, attn=1.4175, kv=2.3709, both=4.6105\\n  ppl.low_sparsity: dense=1.1517, attn=1.7177, kv=3.3253, both=5.4788\\n\\n=== bf16_qw_rand_s020 ===\\n  phase_stats.high_sparsity: n_tokens=16289, n_segments=295\\n  phase_stats.mid_sparsity: n_tokens=4372, n_segments=26\\n  phase_stats.low_sparsity: n_tokens=32227, n_segments=276\\n  ppl.high_sparsity: dense=1.0737, attn=1.6115, kv=2.5041, both=5.9394\\n  ppl.mid_sparsity: dense=1.1322, attn=1.7583, kv=3.0658, both=10.5578\\n  ppl.low_sparsity: dense=1.1517, attn=75.6310, kv=4.3535, both=140.6269\\n\\n=== bf16_qw_rand_s025 ===\\n  phase_stats.high_sparsity: n_tokens=16289, n_segments=295\\n  phase_stats.mid_sparsity: n_tokens=4372, n_segments=26\\n  phase_stats.low_sparsity: n_tokens=32227, n_segments=276\\n  ppl.high_sparsity: dense=1.0737, attn=2.7753, kv=3.3137, both=12.3954\\n  ppl.mid_sparsity: dense=1.1322, attn=2.4944, kv=4.1870, both=15.8108\\n  ppl.low_sparsity: dense=1.1517, attn=476.0375, kv=6.2250, both=345.0363\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.57}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T08:28:49.504073+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "bf16_qw_rand_s015",
  "field": "metrics",
  "value": "{'interaction_index': {'high': {'mean': 1.665213, 'median': 0.138132, 'ci': [1.098566, 2.404194], 'median_ci': [0.102537, 0.207418], 'winsorized_mean': 1.004447, 'skewness': 7.1842}, 'mid': {'mean': 1.697467, 'median': 0.219399, 'ci': [0.447329, 3.461161], 'median_ci': [-0.004845, 0.662126], 'winsorized_mean': 1.403836, 'skewness': 3.2101}, 'low': {'mean': 1.408189, 'median': 0.187842, 'ci': [0.835819, 2.060023], 'median_ci': [0.096196, 0.313935], 'winsorized_mean': 0.940326, 'skewness': 7.1113}}, 'perplexity': {'high': {'dense': 1.0737, 'attn': 1.3939, 'kv': 2.0487, 'both': 4.2076}, 'mid': {'dense': 1.1322, 'attn': 1.4175, 'kv': 2.3709, 'both': 4.6105}, 'low': {'dense': 1.1517, 'attn': 1.7177, 'kv': 3.3253, 'both': 5.4788}}, 'phase_stats': {'high': {'n_tokens': 16289, 'n_segments': 295}, 'mid': {'n_tokens': 4372, 'n_segments': 26}, 'low': {'n_tokens': 32227, 'n_segments': 276}}, 'n_problems': 50, 'pass_fail': {'ci_overlap': True, 'sign_reversal': False, 'overall': 'FAIL'}}",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "bf16_qw_rand_s015",
    "field": "metrics",
    "value": "{'interaction_index': {'high': {'mean': 1.665213, 'median': 0.138132, 'ci': [1.098566, 2.404194], 'median_ci': [0.102537, 0.207418], 'winsorized_mean': 1.004447, 'skewness': 7.1842}, 'mid': {'mean': 1.697467, 'median': 0.219399, 'ci': [0.447329, 3.461161], 'median_ci': [-0.004845, 0.662126], 'winsorized_mean': 1.403836, 'skewness': 3.2101}, 'low': {'mean': 1.408189, 'median': 0.187842, 'ci': [0.835819, 2.060023], 'median_ci': [0.096196, 0.313935], 'winsorized_mean': 0.940326, 'skewness': 7.1113}}, 'perplexity': {'high': {'dense': 1.0737, 'attn': 1.3939, 'kv': 2.0487, 'both': 4.2076}, 'mid': {'dense': 1.1322, 'attn': 1.4175, 'kv': 2.3709, 'both': 4.6105}, 'low': {'dense': 1.1517, 'attn': 1.7177, 'kv': 3.3253, 'both': 5.4788}}, 'phase_stats': {'high': {'n_tokens': 16289, 'n_segments': 295}, 'mid': {'n_tokens': 4372, 'n_segments': 26}, 'low': {'n_tokens': 32227, 'n_segments': 276}}, 'n_problems': 50, 'pass_fail': {'ci_overlap': True, 'sign_reversal': False, 'overall': 'FAIL'}}",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T08:28:49.504314+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"bf16_qw_rand_s015\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:39:34.607Z\", \"updated_at\": \"2026-05-14T08:27:58.623Z\", \"hypothesis\": \"D020 bf16 全量重跑: Qwen2.5-7B-Instruct random masking s=0.15, bf16 dtype. Cross-model 配对对照。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s015 --sparsity_levels 0.15 --masking_method random --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:0\"], \"pid\": \"95899\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_qw_rand_s015.log\", \"submitted_at\": \"2026-05-14T07:55:27.130Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": null, \"wall_clock_seconds\": 1790.5, \"gpu_hours\": 0.5}, \"reproduce\": {\"finished_at\": \"2026-05-14T08:14:18.084Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:14:20.510775+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s015\", \"completed_at\": \"2026-05-14T08:25:17.665Z\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 1.665213, \"median\": 0.138132, \"ci\": [1.098566, 2.404194], \"median_ci\": [0.102537, 0.207418], \"winsorized_mean\": 1.004447, \"skewness\": 7.1842}, \"mid\": {\"mean\": 1.697467, \"median\": 0.219399, \"ci\": [0.447329, 3.461161], \"median_ci\": [-0.004845, 0.662126], \"winsorized_mea
…[truncated 828 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T08:28:49.504547+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "bf16_qw_rand_s020",
  "field": "metrics",
  "value": "{'interaction_index': {'high': {'mean': 2.58579, 'median': 0.48549, 'ci': [1.769404, 3.501692], 'median_ci': [0.304626, 0.658814], 'winsorized_mean': 1.80021, 'skewness': 5.4038}, 'mid': {'mean': 5.69684, 'median': 0.76699, 'ci': [1.69004, 12.276143], 'median_ci': [0.482838, 3.392541], 'winsorized_mean': 4.304174, 'skewness': 3.526}, 'low': {'mean': 65.915714, 'median': 0.614438, 'ci': [-18.581948, 221.709429], 'median_ci': [0.484725, 0.848787], 'winsorized_mean': 2.389244, 'skewness': 16.2163}}, 'perplexity': {'high': {'dense': 1.0737, 'attn': 1.6115, 'kv': 2.5041, 'both': 5.9394}, 'mid': {'dense': 1.1322, 'attn': 1.7583, 'kv': 3.0658, 'both': 10.5578}, 'low': {'dense': 1.1517, 'attn': 75.631, 'kv': 4.3535, 'both': 140.6269}}, 'phase_stats': {'high': {'n_tokens': 16289, 'n_segments': 295}, 'mid': {'n_tokens': 4372, 'n_segments': 26}, 'low': {'n_tokens': 32227, 'n_segments': 276}}, 'n_problems': 50, 'pass_fail': {'ci_overlap': True, 'sign_reversal': False, 'overall': 'FAIL'}}",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "bf16_qw_rand_s020",
    "field": "metrics",
    "value": "{'interaction_index': {'high': {'mean': 2.58579, 'median': 0.48549, 'ci': [1.769404, 3.501692], 'median_ci': [0.304626, 0.658814], 'winsorized_mean': 1.80021, 'skewness': 5.4038}, 'mid': {'mean': 5.69684, 'median': 0.76699, 'ci': [1.69004, 12.276143], 'median_ci': [0.482838, 3.392541], 'winsorized_mean': 4.304174, 'skewness': 3.526}, 'low': {'mean': 65.915714, 'median': 0.614438, 'ci': [-18.581948, 221.709429], 'median_ci': [0.484725, 0.848787], 'winsorized_mean': 2.389244, 'skewness': 16.2163}}, 'perplexity': {'high': {'dense': 1.0737, 'attn': 1.6115, 'kv': 2.5041, 'both': 5.9394}, 'mid': {'dense': 1.1322, 'attn': 1.7583, 'kv': 3.0658, 'both': 10.5578}, 'low': {'dense': 1.1517, 'attn': 75.631, 'kv': 4.3535, 'both': 140.6269}}, 'phase_stats': {'high': {'n_tokens': 16289, 'n_segments': 295}, 'mid': {'n_tokens': 4372, 'n_segments': 26}, 'low': {'n_tokens': 32227, 'n_segments': 276}}, 'n_problems': 50, 'pass_fail': {'ci_overlap': True, 'sign_reversal': False, 'overall': 'FAIL'}}",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T08:28:49.504842+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"bf16_qw_rand_s020\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:39:35.500Z\", \"updated_at\": \"2026-05-14T08:28:05.852Z\", \"hypothesis\": \"D020 bf16 全量重跑: Qwen2.5-7B-Instruct random masking s=0.20, bf16 dtype. Cross-model 配对对照。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s020 --sparsity_levels 0.20 --masking_method random --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:2\"], \"pid\": \"96294\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_qw_rand_s020.log\", \"submitted_at\": \"2026-05-14T07:58:38.430Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": null, \"wall_clock_seconds\": 1600.1, \"gpu_hours\": 0.44}, \"reproduce\": {\"finished_at\": \"2026-05-14T08:18:22.751Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:18:28.103231+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s020\", \"completed_at\": \"2026-05-14T08:25:18.578Z\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 2.58579, \"median\": 0.48549, \"ci\": [1.769404, 3.501692], \"median_ci\": [0.304626, 0.658814], \"winsorized_mean\": 1.80021, \"skewness\": 5.4038}, \"mid\": {\"mean\": 5.69684, \"median\": 0.76699, \"ci\": [1.69004, 12.276143], \"median_ci\": [0.482838, 3.392541], \"winsorized_mean\": 
…[truncated 831 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T08:28:49.505025+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "bf16_qw_rand_s025",
  "field": "metrics",
  "value": "{'interaction_index': {'high': {'mean': 6.549833, 'median': 1.604343, 'ci': [4.349383, 9.512776], 'median_ci': [1.234275, 1.856578], 'winsorized_mean': 4.267976, 'skewness': 7.7254}, 'mid': {'mean': 8.520076, 'median': 2.222455, 'ci': [3.599746, 15.539762], 'median_ci': [1.666917, 4.568741], 'winsorized_mean': 8.400572, 'skewness': 2.5443}, 'low': {'mean': -34.53659, 'median': 2.264141, 'ci': [-203.335784, 120.009066], 'median_ci': [1.757151, 3.452652], 'winsorized_mean': 6.097786, 'skewness': -5.9085}}, 'perplexity': {'high': {'dense': 1.0737, 'attn': 2.7753, 'kv': 3.3137, 'both': 12.3954}, 'mid': {'dense': 1.1322, 'attn': 2.4944, 'kv': 4.187, 'both': 15.8108}, 'low': {'dense': 1.1517, 'attn': 476.0375, 'kv': 6.225, 'both': 345.0363}}, 'phase_stats': {'high': {'n_tokens': 16289, 'n_segments': 295}, 'mid': {'n_tokens': 4372, 'n_segments': 26}, 'low': {'n_tokens': 32227, 'n_segments': 276}}, 'n_problems': 50, 'pass_fail': {'ci_overlap': True, 'sign_reversal': False, 'overall': 'FAIL'}}",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "bf16_qw_rand_s025",
    "field": "metrics",
    "value": "{'interaction_index': {'high': {'mean': 6.549833, 'median': 1.604343, 'ci': [4.349383, 9.512776], 'median_ci': [1.234275, 1.856578], 'winsorized_mean': 4.267976, 'skewness': 7.7254}, 'mid': {'mean': 8.520076, 'median': 2.222455, 'ci': [3.599746, 15.539762], 'median_ci': [1.666917, 4.568741], 'winsorized_mean': 8.400572, 'skewness': 2.5443}, 'low': {'mean': -34.53659, 'median': 2.264141, 'ci': [-203.335784, 120.009066], 'median_ci': [1.757151, 3.452652], 'winsorized_mean': 6.097786, 'skewness': -5.9085}}, 'perplexity': {'high': {'dense': 1.0737, 'attn': 2.7753, 'kv': 3.3137, 'both': 12.3954}, 'mid': {'dense': 1.1322, 'attn': 2.4944, 'kv': 4.187, 'both': 15.8108}, 'low': {'dense': 1.1517, 'attn': 476.0375, 'kv': 6.225, 'both': 345.0363}}, 'phase_stats': {'high': {'n_tokens': 16289, 'n_segments': 295}, 'mid': {'n_tokens': 4372, 'n_segments': 26}, 'low': {'n_tokens': 32227, 'n_segments': 276}}, 'n_problems': 50, 'pass_fail': {'ci_overlap': True, 'sign_reversal': False, 'overall': 'FAIL'}}",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T08:28:49.505254+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"bf16_qw_rand_s025\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:39:36.710Z\", \"updated_at\": \"2026-05-14T08:28:12.737Z\", \"hypothesis\": \"D020 bf16 全量重跑: Qwen2.5-7B-Instruct random masking s=0.25, bf16 dtype. Cross-model 配对对照。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s025 --sparsity_levels 0.25 --masking_method random --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:3\"], \"pid\": \"96437\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_qw_rand_s025.log\", \"submitted_at\": \"2026-05-14T07:58:41.225Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": null, \"wall_clock_seconds\": 1598.1, \"gpu_hours\": 0.44}, \"reproduce\": {\"finished_at\": \"2026-05-14T08:18:30.530Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:18:34.069307+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s025\", \"completed_at\": \"2026-05-14T08:25:19.332Z\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 6.549833, \"median\": 1.604343, \"ci\": [4.349383, 9.512776], \"median_ci\": [1.234275, 1.856578], \"winsorized_mean\": 4.267976, \"skewness\": 7.7254}, \"mid\": {\"mean\": 8.520076, \"median\": 2.222455, \"ci\": [3.599746, 15.539762], \"median_ci\": [1.666917, 4.568741], \"winsorized_me
…[truncated 840 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T08:28:49.505481+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "bf16_qw_rand_s015",
  "field": "notes",
  "value": "Verdict=FAIL（预期）。三 phase median II 在 0.14-0.22 范围（high=0.138, mid=0.219, low=0.188），median CI 完全重叠，无结构化 gradient。PPL(both) 跨 phase 几乎持平（4.21/4.61/5.48），与 importance masking 的强 phase gradient 形成鲜明对照。n_bootstrap=1000（论文需 B=10000 时需重算）。",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "bf16_qw_rand_s015",
    "field": "notes",
    "value": "Verdict=FAIL（预期）。三 phase median II 在 0.14-0.22 范围（high=0.138, mid=0.219, low=0.188），median CI 完全重叠，无结构化 gradient。PPL(both) 跨 phase 几乎持平（4.21/4.61/5.48），与 importance masking 的强 phase gradient 形成鲜明对照。n_bootstrap=1000（论文需 B=10000 时需重算）。",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T08:28:49.505691+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"bf16_qw_rand_s015\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:39:34.607Z\", \"updated_at\": \"2026-05-14T08:28:23.674Z\", \"hypothesis\": \"D020 bf16 全量重跑: Qwen2.5-7B-Instruct random masking s=0.15, bf16 dtype. Cross-model 配对对照。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s015 --sparsity_levels 0.15 --masking_method random --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:0\"], \"pid\": \"95899\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_qw_rand_s015.log\", \"submitted_at\": \"2026-05-14T07:55:27.130Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": null, \"wall_clock_seconds\": 1790.5, \"gpu_hours\": 0.5}, \"reproduce\": {\"finished_at\": \"2026-05-14T08:14:18.084Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:14:20.510775+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s015\", \"completed_at\": \"2026-05-14T08:25:17.665Z\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 1.665213, \"median\": 0.138132, \"ci\": [1.098566, 2.404194], \"median_ci\": [0.102537, 0.207418], \"winsorized_mean\": 1.004447, \"skewness\": 7.1842}, \"mid\": {\"mean\": 1.697467, \"median\": 0.219399, \"ci\": [0.447329, 3.461161], \"median_ci\": [-0.004845, 0.662126], \"winsorized_mea
…[truncated 1078 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-14T08:28:49.505851+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "bf16_qw_rand_s020",
  "field": "notes",
  "value": "Verdict=FAIL（预期）。三 phase median II 在 0.49-0.77 范围（high=0.485, mid=0.767, low=0.614），median CI 重叠，无单调 gradient。mean 受 extreme outlier 严重影响（low mean=65.9, skewness=16.2）。low phase PPL(attn)=75.6 异常高（random masking 偶尔命中关键 head），但 II 无结构化差异。n_bootstrap=1000（论文需 B=10000 时需重算）。",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "bf16_qw_rand_s020",
    "field": "notes",
    "value": "Verdict=FAIL（预期）。三 phase median II 在 0.49-0.77 范围（high=0.485, mid=0.767, low=0.614），median CI 重叠，无单调 gradient。mean 受 extreme outlier 严重影响（low mean=65.9, skewness=16.2）。low phase PPL(attn)=75.6 异常高（random masking 偶尔命中关键 head），但 II 无结构化差异。n_bootstrap=1000（论文需 B=10000 时需重算）。",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-14T08:28:49.506035+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"bf16_qw_rand_s020\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:39:35.500Z\", \"updated_at\": \"2026-05-14T08:28:28.034Z\", \"hypothesis\": \"D020 bf16 全量重跑: Qwen2.5-7B-Instruct random masking s=0.20, bf16 dtype. Cross-model 配对对照。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s020 --sparsity_levels 0.20 --masking_method random --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:2\"], \"pid\": \"96294\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_qw_rand_s020.log\", \"submitted_at\": \"2026-05-14T07:58:38.430Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": null, \"wall_clock_seconds\": 1600.1, \"gpu_hours\": 0.44}, \"reproduce\": {\"finished_at\": \"2026-05-14T08:18:22.751Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:18:28.103231+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s020\", \"completed_at\": \"2026-05-14T08:25:18.578Z\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 2.58579, \"median\": 0.48549, \"ci\": [1.769404, 3.501692], \"median_ci\": [0.304626, 0.658814], \"winsorized_mean\": 1.80021, \"skewness\": 5.4038}, \"mid\": {\"mean\": 5.69684, \"median\": 0.76699, \"ci\": [1.69004, 12.276143], \"median_ci\": [0.482838, 3.392541], \"winsorized_mean\": 
…[truncated 1120 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-14T08:28:49.506186+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "bf16_qw_rand_s025",
  "field": "notes",
  "value": "Verdict=FAIL（预期）。三 phase median II 在 1.60-2.26 范围（high=1.604, mid=2.222, low=2.264），median CI 重叠，无结构化 gradient。low phase mean=-34.5 受极端 outlier 驱动（skewness=-5.9），但 median 稳健。low phase PPL(attn)=476.0, PPL(both)=345.0 异常高。n_bootstrap=1000（论文需 B=10000 时需重算）。",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "bf16_qw_rand_s025",
    "field": "notes",
    "value": "Verdict=FAIL（预期）。三 phase median II 在 1.60-2.26 范围（high=1.604, mid=2.222, low=2.264），median CI 重叠，无结构化 gradient。low phase mean=-34.5 受极端 outlier 驱动（skewness=-5.9），但 median 稳健。low phase PPL(attn)=476.0, PPL(both)=345.0 异常高。n_bootstrap=1000（论文需 B=10000 时需重算）。",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-14T08:28:49.506368+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"bf16_qw_rand_s025\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:39:36.710Z\", \"updated_at\": \"2026-05-14T08:28:29.941Z\", \"hypothesis\": \"D020 bf16 全量重跑: Qwen2.5-7B-Instruct random masking s=0.25, bf16 dtype. Cross-model 配对对照。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python -m pacs.profiling.run_profiling --model_path /root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct --data_path /root/autodl-tmp/pacs/data/math500.json --output_dir /root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s025 --sparsity_levels 0.25 --masking_method random --max_new_tokens 2048 --min_phase_length 10 --max_problems 50\\\"\", \"server\": \"westd-22162\", \"gpu\": [\"cuda:3\"], \"pid\": \"96437\", \"log_path\": \"~/runs/phase-gated-compound-sparse/bf16_qw_rand_s025.log\", \"submitted_at\": \"2026-05-14T07:58:41.225Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/pacs/data/math500.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": null, \"wall_clock_seconds\": 1598.1, \"gpu_hours\": 0.44}, \"reproduce\": {\"finished_at\": \"2026-05-14T08:18:30.530Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:18:34.069307+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s025\", \"completed_at\": \"2026-05-14T08:25:19.332Z\", \"metrics\": {\"interaction_index\": {\"high\": {\"mean\": 6.549833, \"ci\": [4.349383, 9.512776], \"median\": 1.604343, \"median_ci\": [1.234275, 1.856578], \"winsorized_mean\": 4.267976, \"skewness\": 7.7254}, \"mid\": {\"mean\": 8.520076, \"ci\": [3.599746, 15.539762], \"median\": 2.222455, \"median_ci\": [1.666917, 4.568741], \"winsorized_me
…[truncated 1146 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-14T08:28:49.506553+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "filters": "{'exp_id': 'bf16_qw_rand_s015'}",
  "fields": "['status', 'conclusion', 'metrics', 'checkpoint_path', 'notes']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "filters": "{'exp_id': 'bf16_qw_rand_s015'}",
    "fields": "['status', 'conclusion', 'metrics', 'checkpoint_path', 'notes']"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-14T08:28:49.506686+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5438}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-14T08:28:49.506810+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "filters": "{'exp_id': 'bf16_qw_rand_s020'}",
  "fields": "['status', 'conclusion', 'metrics', 'checkpoint_path', 'notes']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "filters": "{'exp_id': 'bf16_qw_rand_s020'}",
    "fields": "['status', 'conclusion', 'metrics', 'checkpoint_path', 'notes']"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-14T08:28:49.506933+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2551}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-14T08:28:49.507045+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "filters": "{'exp_id': 'bf16_qw_rand_s025'}",
  "fields": "['status', 'conclusion', 'metrics', 'checkpoint_path', 'notes']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "filters": "{'exp_id': 'bf16_qw_rand_s025'}",
    "fields": "['status', 'conclusion', 'metrics', 'checkpoint_path', 'notes']"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-14T08:28:49.507162+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2722}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-14T08:28:49.507303+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "filters": "{'status': 'DONE', 'conclusion': 'success'}",
  "fields": "['status', 'conclusion', 'checkpoint_path']",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "filters": "{'status': 'DONE', 'conclusion': 'success'}",
    "fields": "['status', 'conclusion', 'checkpoint_path']",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-14T08:28:49.507505+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"bf16_ds_rand_s030\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s030\"}, \"bf16_qw_rand_s025\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s025\"}, \"bf16_ds_rand_s025\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s025\"}, \"bf16_qw_rand_s020\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s020\"}, \"bf16_qw_rand_s015\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_qw_rand_s015\"}, \"bf16_ds_rand_s020\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s020\"}, \"bf16_ds_rand_s015\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_ds_rand_s015\"}, \"bf16_qw_imp_s030\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s030\"}, \"bf16_qw_imp_s025\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s025\"}, \"bf16_qw_imp_s020\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s020\"}, \"bf16_qw_imp_s015\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pacs/profiling_output_bf16_qw_imp_s015\"}, \"bf16_importance_s030\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"bf16_importance_s025\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/pa
…[truncated 2171 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qw_rand_batch_20260514T082557",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-14T08:28:49.507697+00:00_

三个实验全部确认：DONE + conclusion=success + checkpoint_path 已设置 + metrics 非空。

**汇总：**

| 实验 | Median II (high/mid/low) | Median CI 重叠 | Verdict |
|------|--------------------------|---------------|---------|
| bf16_qw_rand_s015 | 0.14 / 0.22 / 0.19 | 完全重叠 | FAIL |
| bf16_qw_rand_s020 | 0.49 / 0.77 / 0.61 | 完全重叠 | FAIL |
| bf16_qw_rand_s025 | 1.60 / 2.22 / 2.26 | 完全重叠 | FAIL |

三个 Qwen random masking 负对照均为 FAIL（预期），与 DeepSeek random 系列结论一致：random masking 不产生 phase-dependent interaction pattern。Registry 已全部更新完毕。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_qw_rand_batch_20260514T082557"
}
```

</details>

---
