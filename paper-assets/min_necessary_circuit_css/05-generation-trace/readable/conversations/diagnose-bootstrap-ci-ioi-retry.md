# diagnose bootstrap ci ioi retry

**Transformer Model EAP-IG** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_diagnose_bootstrap_ci_ioi_retry_20260513T152642.jsonl`
- **Structured JSON:** [`fa97bd234746f77193f2.json`](../../sessions/fa/fa97bd234746f77193f2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-13T15:27:59.970525+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__detect_image",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_bootstrap_ci_ioi_retry_20260513T152642",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__detect_image",
    "max_results": "6"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-13T15:27:59.970872+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_bootstrap_ci_ioi_retry_20260513T152642",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-13T15:27:59.971040+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-pro6000",
  "command": "tail -80 /root/runs/min_necessary_circuit_css/bootstrap_ci_ioi.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_bootstrap_ci_ioi_retry_20260513T152642",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-pro6000",
    "command": "tail -80 /root/runs/min_necessary_circuit_css/bootstrap_ci_ioi.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-13T15:27:59.971177+00:00_

Error executing tool ssh_read_only: Unknown server 'westd-pro6000'. Available: ['cqa1-21977', 'home-1x5090', 'westd-39279']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_bootstrap_ci_ioi_retry_20260513T152642",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-13T15:27:59.971301+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-pro6000",
  "command": "ls -la /root/min_necessary_circuit_css/cache_acdc.json /root/min_necessary_circuit_css/cache_eap_ig.json /root/min_necessary_circuit_css/cache_edge_pruning.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_bootstrap_ci_ioi_retry_20260513T152642",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-pro6000",
    "command": "ls -la /root/min_necessary_circuit_css/cache_acdc.json /root/min_necessary_circuit_css/cache_eap_ig.json /root/min_necessary_circuit_css/cache_edge_pruning.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-13T15:27:59.971421+00:00_

Error executing tool ssh_read_only: Unknown server 'westd-pro6000'. Available: ['cqa1-21977', 'home-1x5090', 'westd-39279']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_bootstrap_ci_ioi_retry_20260513T152642",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-13T15:27:59.971535+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "min_necessary_circuit_css",
  "filters": "{'exp_id': 'bootstrap_ci_ioi'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_bootstrap_ci_ioi_retry_20260513T152642",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "min_necessary_circuit_css",
    "filters": "{'exp_id': 'bootstrap_ci_ioi'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-13T15:27:59.971657+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0487}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_bootstrap_ci_ioi_retry_20260513T152642",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-13T15:27:59.971832+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "tail -80 /root/runs/min_necessary_circuit_css/bootstrap_ci_ioi.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_bootstrap_ci_ioi_retry_20260513T152642",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "tail -80 /root/runs/min_necessary_circuit_css/bootstrap_ci_ioi.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-13T15:27:59.971955+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "ls -la /root/min_necessary_circuit_css/cache_acdc.json /root/min_necessary_circuit_css/cache_eap_ig.json /root/min_necessary_circuit_css/cache_edge_pruning.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_bootstrap_ci_ioi_retry_20260513T152642",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "ls -la /root/min_necessary_circuit_css/cache_acdc.json /root/min_necessary_circuit_css/cache_eap_ig.json /root/min_necessary_circuit_css/cache_edge_pruning.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-13T15:27:59.972076+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"tail: cannot open '/root/runs/min_necessary_circuit_css/bootstrap_ci_ioi.log' for reading: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 1.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_bootstrap_ci_ioi_retry_20260513T152642",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T15:27:59.972204+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/min_necessary_circuit_css/cache_acdc.json': No such file or directory\\nls: cannot access '/root/min_necessary_circuit_css/cache_eap_ig.json': No such file or directory\\nls: cannot access '/root/min_necessary_circuit_css/cache_edge_pruning.json': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.78}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_bootstrap_ci_ioi_retry_20260513T152642",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-13T15:27:59.972353+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "ls -la /root/min_necessary_circuit_css/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_bootstrap_ci_ioi_retry_20260513T152642",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "ls -la /root/min_necessary_circuit_css/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-13T15:27:59.972473+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '||' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_bootstrap_ci_ioi_retry_20260513T152642",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T15:27:59.972587+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "ls -la /root/structfuse-context/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_bootstrap_ci_ioi_retry_20260513T152642",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "ls -la /root/structfuse-context/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-13T15:27:59.972723+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "ls /root/runs/min_necessary_circuit_css/ 2>/dev/null || echo \"RUNS_DIR_NOT_FOUND\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_bootstrap_ci_ioi_retry_20260513T152642",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "ls /root/runs/min_necessary_circuit_css/ 2>/dev/null || echo \"RUNS_DIR_NOT_FOUND\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-13T15:27:59.972883+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 12316\\ndrwxr-xr-x 6 root root    4096 May 13 19:44 .\\ndrwx------ 1 root root    4096 May 13 16:28 ..\\ndrwxr-xr-x 2 root root    4096 May 13 16:55 __pycache__\\n-rw-r--r-- 1 root root     482 May 13 18:41 _gen_arith_caches.py\\n-rw-r--r-- 1 root root    5822 May 13 14:28 acdc_topk_sweep.py\\n-rw-r--r-- 1 root root   12959 May 13 14:28 analysis_fix_v3.py\\n-rw-r--r-- 1 root root     382 May 13 18:42 arith_cache_rebuild.log\\n-rw-r--r-- 1 root root     900 May 13 19:50 bootstrap_ci_results.json\\ndrwxr-xr-x 3 root root      39 May 13 15:24 cache\\n-rw-r--r-- 1 root root 1307718 May 13 19:44 cache_acdc.json\\n-rw-r--r-- 1 root root 1307929 May 13 17:18 cache_acdc_fr.json\\n-rw-r--r-- 1 root root 1307849 May 13 15:56 cache_acdc_sva.json\\n-rw-r--r-- 1 root root 1368604 May 13 17:18 cache_eap_ig.json\\n-rw-r--r-- 1 root root 1368627 May 13 16:28 cache_eap_ig_fr.json\\n-rw-r--r-- 1 root root 1368547 May 13 15:23 cache_eap_ig_sva.json\\n-rw-r--r-- 1 root root 1346598 May 13 17:19 cache_edge_pruning.json\\n-rw-r--r-- 1 root root 1349157 May 13 16:58 cache_ep_fr.json\\n-rw-r--r-- 1 root root 1352131 May 13 15:25 cache_ep_sva.json\\n-rw-r--r-- 1 root root    6533 May 13 14:28 circuit_discovery.py\\n-rw-r--r-- 1 root root    6001 May 13 14:28 circus.py\\n-rw-r--r-- 1 root root     868 May 13 14:28 config.py\\n-rw-r--r-- 1 root root    4091 May 13 14:28 cross_tabulate.py\\n-rw-r--r-- 1 root root    5443 May 13 14:28 css.py\\n-rw-r--r-- 1 root root    7526 May 13 15:36 diagnose_ifr_perhead.py\\n-rw-r--r-- 1 root root    4767 May 13 15:55 diagnose_proportional_binarize.py\\n-rw-r--r-- 1 root root    8146 May 13 15:16 e2e_validate.py\\n-rw-r--r-- 1 root root    9819 May 13 14:28 edge_pruning_l0.py\\n-rw-r--r-- 1 root root    5787 May 13 14:28 eval_faithfulness.py\\n-rw-r--r-- 1 root root   15176 May 13 14:28 eval_mean_ablation.py\\n-rw-r--r-- 1 root root   17573 May 13 14:28 eval_topk_faithfulness.py\\n-rw-r--r-- 1 ro
…[truncated 1637 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_bootstrap_ci_ioi_retry_20260513T152642",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-13T15:27:59.973029+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '||' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_bootstrap_ci_ioi_retry_20260513T152642",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-13T15:27:59.973180+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "cat /root/structfuse-context/bootstrap_ci_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_bootstrap_ci_ioi_retry_20260513T152642",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "cat /root/structfuse-context/bootstrap_ci_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-13T15:27:59.973352+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"ioi\\\": {\\n    \\\"task\\\": \\\"ioi\\\",\\n    \\\"ablation\\\": \\\"zero\\\",\\n    \\\"n_prompts\\\": 100,\\n    \\\"css_10\\\": {\\n      \\\"num_edges\\\": 16,\\n      \\\"cpr\\\": 0.02947526052594185\\n    },\\n    \\\"best_single\\\": {\\n      \\\"method\\\": \\\"edge_pruning\\\",\\n      \\\"num_edges\\\": 100,\\n      \\\"cpr\\\": 0.08292677253484726\\n    },\\n    \\\"all_methods\\\": {\\n      \\\"eap_ig\\\": {\\n        \\\"edges\\\": 100,\\n        \\\"cpr\\\": -0.10921436548233032\\n      },\\n      \\\"edge_pruning\\\": {\\n        \\\"edges\\\": 100,\\n        \\\"cpr\\\": 0.08292677253484726\\n      },\\n      \\\"acdc\\\": {\\n        \\\"edges\\\": 16,\\n        \\\"cpr\\\": 0.02947526052594185\\n      }\\n    },\\n    \\\"delta\\\": -0.05345151200890541,\\n    \\\"bootstrap\\\": {\\n      \\\"observed_delta\\\": -0.05345151200890541,\\n      \\\"bootstrap_mean\\\": -0.0424281507730484,\\n      \\\"bootstrap_std\\\": 0.1454060971736908,\\n      \\\"ci_lo\\\": -0.29016661643981934,\\n      \\\"ci_hi\\\": 0.2586621046066284,\\n      \\\"p_value\\\": 0.342,\\n      \\\"n_valid\\\": 1000\\n    },\\n    \\\"significant\\\": false\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_bootstrap_ci_ioi_retry_20260513T152642",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-13T15:27:59.973486+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "ls -la /root/structfuse-context/logs/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_bootstrap_ci_ioi_retry_20260513T152642",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "ls -la /root/structfuse-context/logs/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-13T15:27:59.973608+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 1964\\ndrwxr-xr-x 2 root root      75 May 13 16:30 .\\ndrwxr-xr-x 6 root root    4096 May 13 19:44 ..\\n-rw-r--r-- 1 root root 2000823 May 13 15:56 mvp_sva_gpt2_k3_topk.log\\n-rw-r--r-- 1 root root    3636 May 13 16:31 qwen_ioi_acdc.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_bootstrap_ci_ioi_retry_20260513T152642",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-13T15:27:59.973751+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "cat /root/structfuse-context/ioi_size_controlled_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diagnose_bootstrap_ci_ioi_retry_20260513T152642",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "cat /root/structfuse-context/ioi_size_controlled_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-13T15:27:59.974224+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"N\\\": 16,\\n  \\\"css_10_edges\\\": [\\n    \\\"a0.h1->a9.h9.v\\\",\\n    \\\"a10.h0->logits\\\",\\n    \\\"a10.h10->logits\\\",\\n    \\\"a10.h6->logits\\\",\\n    \\\"a10.h7->logits\\\",\\n    \\\"a9.h6->logits\\\",\\n    \\\"a9.h9->a10.h7.q\\\",\\n    \\\"a9.h9->logits\\\",\\n    \\\"input->a0.h1.v\\\",\\n    \\\"input->m0\\\",\\n    \\\"m0->a10.h7.k\\\",\\n    \\\"m0->a9.h6.v\\\",\\n    \\\"m0->a9.h9.v\\\",\\n    \\\"m4->a9.h9.v\\\",\\n    \\\"m5->a9.h9.v\\\",\\n    \\\"m6->a9.h9.v\\\"\\n  ],\\n  \\\"binarization\\\": {\\n    \\\"acdc\\\": \\\"isinf\\\",\\n    \\\"eap_ig\\\": \\\"top-100\\\",\\n    \\\"ep\\\": \\\"top-100\\\"\\n  },\\n  \\\"results\\\": {\\n    \\\"CSS=1.0\\\": {\\n      \\\"num_edges\\\": 16,\\n      \\\"zero\\\": {\\n        \\\"num_edges\\\": 16,\\n        \\\"cpr\\\": 0.0295,\\n        \\\"cmd\\\": 0.9929\\n      },\\n      \\\"mean\\\": {\\n        \\\"num_edges\\\": 16,\\n        \\\"cpr\\\": 0.177,\\n        \\\"cmd\\\": 0.842\\n      }\\n    },\\n    \\\"EAP-IG top-N\\\": {\\n      \\\"num_edges\\\": 16,\\n      \\\"zero\\\": {\\n        \\\"num_edges\\\": 16,\\n        \\\"cpr\\\": -0.0585,\\n        \\\"cmd\\\": 1.0829\\n      },\\n      \\\"mean\\\": {\\n        \\\"num_edges\\\": 16,\\n        \\\"cpr\\\": 0.182,\\n        \\\"cmd\\\": 0.8369\\n      }\\n    },\\n    \\\"EP top-N\\\": {\\n      \\\"num_edges\\\": 16,\\n      \\\"zero\\\": {\\n        \\\"num_edges\\\": 16,\\n        \\\"cpr\\\": -0.0091,\\n        \\\"cmd\\\": 1.0323\\n      },\\n      \\\"mean\\\": {\\n        \\\"num_edges\\\": 16,\\n        \\\"cpr\\\": 0.1832,\\n        \\\"cmd\\\": 0.8356\\n      }\\n    },\\n    \\\"ACDC top-N\\\": {\\n      \\\"num_edges\\\": 16,\\n      \\\"zero\\\": {\\n        \\\"num_edges\\\": 16,\\n        \\\"cpr\\\": 0.0295,\\n        \\\"cmd\\\": 0.9929\\n      },\\n      \\\"mean\\\": {\\n        \\\"num_edges\\\": 16,\\n        \\\"cpr\\\": 0.177,\\n        \\\"cmd\\
…[truncated 8919 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diagnose_bootstrap_ci_ioi_retry_20260513T152642",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-13T15:27:59.974455+00:00_

**实验已完成。** `bootstrap_ci_results.json` 已存在且包含完整的 IOI Bootstrap CI 结果（n_valid=1000）：

| 指标 | 值 |
|------|-----|
| CSS=1.0 CPR | 0.0295 (16 edges, ACDC) |
| Best single (EP) CPR | 0.0829 (100 edges) |
| observed delta | -0.0535 |
| bootstrap CI | [-0.290, 0.259] |
| **p-value** | **0.342** |
| significant | **false** |

实验没有失败——结果文件在 `19:50` 已写入完毕，1000 个 bootstrap 样本全部完成。任务描述中的 "westd-pro6000" 服务器不存在于当前可用列表（实际是 westd-39279），可能是旧信息。

**结论**：CSS=1.0 在 IOI 任务上相对 best single method 的 advantage 不显著（p=0.342, CI 包含 0，delta 为负），即 CSS 共识电路在 IOI 上没有统计显著的优势。这与 SVA 的结果（p=0.099）方向一致——CSS 在这些任务上并未展现出显著优势。

无需重跑实验。需要我将结果注册到 registry 吗？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_diagnose_bootstrap_ci_ioi_retry_20260513T152642"
}
```

</details>

---
