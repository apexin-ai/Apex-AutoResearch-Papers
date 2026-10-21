# analysis seed level stats

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 87
- **Recorded user turns:** 0
- **Tool calls:** 43
- **Original source:** `logs/chats/worker_analysis_seed-level-stats_20260517T114905.jsonl`
- **Structured JSON:** [`8c343956d2f3e6c51297.json`](../../sessions/8c/8c343956d2f3e6c51297.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

87 recorded events

### Tool call

_source line 1 · 2026-05-17T11:55:39.201659+00:00_

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
  "session": "worker_analysis_seed-level-stats_20260517T114905",
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

_source line 2 · 2026-05-17T11:55:39.202039+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T11:55:39.202212+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "find /root/autodl-tmp/outputs -name \"eval_sta_results.json\" -path \"*plan002*b01*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "find /root/autodl-tmp/outputs -name \"eval_sta_results.json\" -path \"*plan002*b01*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-17T11:55:39.202346+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "find /root/autodl-tmp/outputs -name \"eval_sta_results.json\" -path \"*plan018*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "find /root/autodl-tmp/outputs -name \"eval_sta_results.json\" -path \"*plan018*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T11:55:39.202470+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "find /root/autodl-tmp/eval_archive -name \"*.json\" -path \"*plan002*b01*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "find /root/autodl-tmp/eval_archive -name \"*.json\" -path \"*plan002*b01*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T11:55:39.202597+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.93}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-17T11:55:39.202828+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/outputs/plan018_additive_random_b01_s44_r2/eval_sta_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T11:55:39.202965+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/eval_archive/plan002_additive_b01_s45/eval_results.json\\n/root/autodl-tmp/eval_archive/plan002_additive_b01_s45/h7_classification.json\\n/root/autodl-tmp/eval_archive/plan002_additive_b01_s46/eval_results.json\\n/root/autodl-tmp/eval_archive/plan002_additive_b01_s46/h7_classification.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.29}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T11:55:39.203086+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "find /root/autodl-tmp/eval_archive -name \"*.json\" -path \"*plan018*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "find /root/autodl-tmp/eval_archive -name \"*.json\" -path \"*plan018*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-17T11:55:39.203204+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "find /root/autodl-tmp/outputs -type d -name \"*plan002*b01*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "find /root/autodl-tmp/outputs -type d -name \"*plan002*b01*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-17T11:55:39.203325+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/eval_archive/plan018_random_b01_s45/eval_results.json\\n/root/autodl-tmp/eval_archive/plan018_random_b01_s45/h7_classification.json\\n/root/autodl-tmp/eval_archive/plan018_random_b01_s46/eval_results.json\\n/root/autodl-tmp/eval_archive/plan018_random_b01_s46/h7_classification.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.11}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-17T11:55:39.203470+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "find /root/autodl-tmp/outputs -type d -name \"*plan018*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "find /root/autodl-tmp/outputs -type d -name \"*plan018*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-17T11:55:39.203616+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.91}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T11:55:39.203781+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/outputs/plan018_additive_random_b01_s44_r2\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.99}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T11:55:39.203914+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "cat /root/autodl-tmp/eval_archive/plan002_additive_b01_s45/eval_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "cat /root/autodl-tmp/eval_archive/plan002_additive_b01_s45/eval_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-17T11:55:39.204035+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "cat /root/autodl-tmp/eval_archive/plan002_additive_b01_s46/eval_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "cat /root/autodl-tmp/eval_archive/plan002_additive_b01_s46/eval_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T11:55:39.204150+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "cat /root/autodl-tmp/eval_archive/plan018_random_b01_s45/eval_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "cat /root/autodl-tmp/eval_archive/plan018_random_b01_s45/eval_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-17T11:55:39.204263+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "cat /root/autodl-tmp/eval_archive/plan018_random_b01_s46/eval_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "cat /root/autodl-tmp/eval_archive/plan018_random_b01_s46/eval_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-17T11:55:39.204545+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n_problems\\\": 100,\\n    \\\"n_proved\\\": 42,\\n    \\\"prove_rate\\\": 0.42,\\n    \\\"mean_isr\\\": 0.2542,\\n    \\\"isr_std\\\": 0.3261,\\n    \\\"median_isr\\\": 0.0,\\n    \\\"isr_pr_ratio\\\": 0.6052,\\n    \\\"proved_only_mean_isr\\\": 0.6052,\\n    \\\"min_isr\\\": 0.0,\\n    \\\"max_isr\\\": 0.8889,\\n    \\\"by_answer_type\\\": {\\n      \\\"false\\\": {\\n        \\\"count\\\": 25,\\n        \\\"proved\\\": 10,\\n        \\\"prove_rate\\\": 0.4,\\n        \\\"mean_isr\\\": 0.21333333333333332\\n      },\\n      \\\"unknown\\\": {\\n        \\\"count\\\": 41,\\n        \\\"proved\\\": 10,\\n        \\\"prove_rate\\\": 0.24390243902439024,\\n        \\\"mean_isr\\\": 0.13995354239256677\\n      },\\n      \\\"true\\\": {\\n        \\\"count\\\": 34,\\n        \\\"proved\\\": 22,\\n        \\\"prove_rate\\\": 0.6470588235294118,\\n        \\\"mean_isr\\\": 0.4219421101774043\\n      }\\n    },\\n    \\\"elapsed_seconds\\\": 236.5,\\n    \\\"avg_time_per_sample\\\": 2.4,\\n    \\\"solver\\\": \\\"Prover9Solver\\\",\\n    \\\"logic_type\\\": \\\"fol\\\",\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/outputs/plan002_additive_b01_s45/checkpoint-500\\\"\\n  },\\n  \\\"results\\\": [\\n    {\\n      \\\"index\\\": 0,\\n      \\\"id\\\": \\\"folio_765\\\",\\n      \\\"context\\\": \\\"Tipped employees are not entitled to be paid the federal minimum wage by their employees. \\\\nIf a person is a white-collar worker, they are entitled to be paid the federal minimum wage by their employees. \\\\nAll lawyers are white-collar workers.\\\\nEvery advocate is a lawyer.\\\\nMary is not a lawyer or a tipped employee.\\\",\\n      \\\"question\\\": \\\"Mary is an advocate.\\\",\\n      \\\"answer\\\": \\\"false\\\",\\n      \\\"formalization\\\": \\\"Premises:\\\\n1. ∀x (WhiteCollarWorker(x) → EntitledToMinimumWage(x))\\\\n2. ∀x (Lawyer(x) → WhiteCollarWorker(x))\\\\n3. ∀x (Advocat
…[truncated 7704 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T11:55:39.204898+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n_problems\\\": 100,\\n    \\\"n_proved\\\": 77,\\n    \\\"prove_rate\\\": 0.77,\\n    \\\"mean_isr\\\": 0.3164,\\n    \\\"isr_std\\\": 0.2959,\\n    \\\"median_isr\\\": 0.25,\\n    \\\"isr_pr_ratio\\\": 0.411,\\n    \\\"proved_only_mean_isr\\\": 0.411,\\n    \\\"min_isr\\\": 0.0,\\n    \\\"max_isr\\\": 0.8,\\n    \\\"by_answer_type\\\": {\\n      \\\"false\\\": {\\n        \\\"count\\\": 25,\\n        \\\"proved\\\": 18,\\n        \\\"prove_rate\\\": 0.72,\\n        \\\"mean_isr\\\": 0.33125396825396825\\n      },\\n      \\\"unknown\\\": {\\n        \\\"count\\\": 41,\\n        \\\"proved\\\": 28,\\n        \\\"prove_rate\\\": 0.6829268292682927,\\n        \\\"mean_isr\\\": 0.25634304719670575\\n      },\\n      \\\"true\\\": {\\n        \\\"count\\\": 34,\\n        \\\"proved\\\": 31,\\n        \\\"prove_rate\\\": 0.9117647058823529,\\n        \\\"mean_isr\\\": 0.37804621848739495\\n      }\\n    },\\n    \\\"elapsed_seconds\\\": 260.6,\\n    \\\"avg_time_per_sample\\\": 2.6,\\n    \\\"solver\\\": \\\"Prover9Solver\\\",\\n    \\\"logic_type\\\": \\\"fol\\\",\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/outputs/plan002_additive_b01_s46/checkpoint-500\\\"\\n  },\\n  \\\"results\\\": [\\n    {\\n      \\\"index\\\": 0,\\n      \\\"id\\\": \\\"folio_765\\\",\\n      \\\"context\\\": \\\"Tipped employees are not entitled to be paid the federal minimum wage by their employees. \\\\nIf a person is a white-collar worker, they are entitled to be paid the federal minimum wage by their employees. \\\\nAll lawyers are white-collar workers.\\\\nEvery advocate is a lawyer.\\\\nMary is not a lawyer or a tipped employee.\\\",\\n      \\\"question\\\": \\\"Mary is an advocate.\\\",\\n      \\\"answer\\\": \\\"false\\\",\\n      \\\"formalization\\\": \\\"Premises:  \\\\n1. all x (isLawyer(x) → isWhiteCollarWorker(x))  \\\\n2. all x (isWhiteCollarWorker(x) → entitledToMinimumWage(x))  \\\\
…[truncated 7807 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-17T11:55:39.205261+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n_problems\\\": 100,\\n    \\\"n_proved\\\": 58,\\n    \\\"prove_rate\\\": 0.58,\\n    \\\"mean_isr\\\": 0.0096,\\n    \\\"isr_std\\\": 0.0237,\\n    \\\"median_isr\\\": 0.0,\\n    \\\"isr_pr_ratio\\\": 0.0166,\\n    \\\"proved_only_mean_isr\\\": 0.0166,\\n    \\\"min_isr\\\": 0.0,\\n    \\\"max_isr\\\": 0.1,\\n    \\\"by_answer_type\\\": {\\n      \\\"false\\\": {\\n        \\\"count\\\": 25,\\n        \\\"proved\\\": 14,\\n        \\\"prove_rate\\\": 0.56,\\n        \\\"mean_isr\\\": 0.013643578643578643\\n      },\\n      \\\"unknown\\\": {\\n        \\\"count\\\": 41,\\n        \\\"proved\\\": 23,\\n        \\\"prove_rate\\\": 0.5609756097560976,\\n        \\\"mean_isr\\\": 0.006230517450029645\\n      },\\n      \\\"true\\\": {\\n        \\\"count\\\": 34,\\n        \\\"proved\\\": 21,\\n        \\\"prove_rate\\\": 0.6176470588235294,\\n        \\\"mean_isr\\\": 0.010732580505598409\\n      }\\n    },\\n    \\\"elapsed_seconds\\\": 775.3,\\n    \\\"avg_time_per_sample\\\": 7.8,\\n    \\\"solver\\\": \\\"Prover9Solver\\\",\\n    \\\"logic_type\\\": \\\"fol\\\",\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/outputs/plan018_random_b01_s45/checkpoint-500\\\"\\n  },\\n  \\\"results\\\": [\\n    {\\n      \\\"index\\\": 0,\\n      \\\"id\\\": \\\"folio_765\\\",\\n      \\\"context\\\": \\\"Tipped employees are not entitled to be paid the federal minimum wage by their employees. \\\\nIf a person is a white-collar worker, they are entitled to be paid the federal minimum wage by their employees. \\\\nAll lawyers are white-collar workers.\\\\nEvery advocate is a lawyer.\\\\nMary is not a lawyer or a tipped employee.\\\",\\n      \\\"question\\\": \\\"Mary is an advocate.\\\",\\n      \\\"answer\\\": \\\"false\\\",\\n      \\\"formalization\\\": \\\"Premises:\\\\n1. ∀x (IsTipped(x) → NotEntitled(x))\\\\n2. ∀x (IsWhiteCollar(x) → Entitled(x))\\\\n3. ∀x (IsLawyer(x) → IsWhiteCollar(x
…[truncated 7517 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-17T11:55:39.205645+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n_problems\\\": 100,\\n    \\\"n_proved\\\": 94,\\n    \\\"prove_rate\\\": 0.94,\\n    \\\"mean_isr\\\": 0.0424,\\n    \\\"isr_std\\\": 0.1451,\\n    \\\"median_isr\\\": 0.0,\\n    \\\"isr_pr_ratio\\\": 0.0451,\\n    \\\"proved_only_mean_isr\\\": 0.0451,\\n    \\\"min_isr\\\": 0.0,\\n    \\\"max_isr\\\": 0.6667,\\n    \\\"by_answer_type\\\": {\\n      \\\"false\\\": {\\n        \\\"count\\\": 25,\\n        \\\"proved\\\": 23,\\n        \\\"prove_rate\\\": 0.92,\\n        \\\"mean_isr\\\": 0.016\\n      },\\n      \\\"unknown\\\": {\\n        \\\"count\\\": 41,\\n        \\\"proved\\\": 38,\\n        \\\"prove_rate\\\": 0.926829268292683,\\n        \\\"mean_isr\\\": 0.02666188426590148\\n      },\\n      \\\"true\\\": {\\n        \\\"count\\\": 34,\\n        \\\"proved\\\": 33,\\n        \\\"prove_rate\\\": 0.9705882352941176,\\n        \\\"mean_isr\\\": 0.08088235294117646\\n      }\\n    },\\n    \\\"elapsed_seconds\\\": 136.4,\\n    \\\"avg_time_per_sample\\\": 1.4,\\n    \\\"solver\\\": \\\"Prover9Solver\\\",\\n    \\\"logic_type\\\": \\\"fol\\\",\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/outputs/plan018_random_b01_s46/checkpoint-500\\\"\\n  },\\n  \\\"results\\\": [\\n    {\\n      \\\"index\\\": 0,\\n      \\\"id\\\": \\\"folio_765\\\",\\n      \\\"context\\\": \\\"Tipped employees are not entitled to be paid the federal minimum wage by their employees. \\\\nIf a person is a white-collar worker, they are entitled to be paid the federal minimum wage by their employees. \\\\nAll lawyers are white-collar workers.\\\\nEvery advocate is a lawyer.\\\\nMary is not a lawyer or a tipped employee.\\\",\\n      \\\"question\\\": \\\"Mary is an advocate.\\\",\\n      \\\"answer\\\": \\\"false\\\",\\n      \\\"formalization\\\": \\\"Premises:\\\\n1. Advocate(mary)\\\\n2. Advocate(mary)\\\\nConclusion: Advocate(mary)\\\",\\n      \\\"gen_time\\\": 0.97,\\n      \\\"eval_time\\\": 
…[truncated 7952 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T11:55:39.205892+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "cat /root/autodl-tmp/eval_archive/plan002_additive_b01_s45/h7_classification.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "cat /root/autodl-tmp/eval_archive/plan002_additive_b01_s45/h7_classification.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-17T11:55:39.206027+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "cat /root/autodl-tmp/eval_archive/plan002_additive_b01_s46/h7_classification.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "cat /root/autodl-tmp/eval_archive/plan002_additive_b01_s46/h7_classification.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T11:55:39.206147+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "cat /root/autodl-tmp/eval_archive/plan018_random_b01_s45/h7_classification.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "cat /root/autodl-tmp/eval_archive/plan018_random_b01_s45/h7_classification.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-17T11:55:39.206260+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "cat /root/autodl-tmp/eval_archive/plan018_random_b01_s46/h7_classification.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "cat /root/autodl-tmp/eval_archive/plan018_random_b01_s46/h7_classification.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-17T11:55:39.206399+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"eval_results\\\": {\\n    \\\"n_total\\\": 100,\\n    \\\"n_proved\\\": 42,\\n    \\\"h7a_count\\\": 16,\\n    \\\"h7a_rate\\\": 0.381,\\n    \\\"h7b_count\\\": 0,\\n    \\\"h7b_rate\\\": 0.0,\\n    \\\"h7_total_count\\\": 16,\\n    \\\"h7_total_rate\\\": 0.381,\\n    \\\"h1_strict_count\\\": 2,\\n    \\\"h1_strict_rate\\\": 0.0476,\\n    \\\"h8_conjunction_collapse_count\\\": 1,\\n    \\\"h8_conjunction_collapse_rate\\\": 0.0238,\\n    \\\"conclusion_in_premise_count\\\": 18,\\n    \\\"conclusion_in_premise_rate\\\": 0.4286,\\n    \\\"h7_relaxed_count\\\": 15,\\n    \\\"h7_relaxed_rate\\\": 0.3571,\\n    \\\"single_premise_count\\\": 16,\\n    \\\"single_premise_rate\\\": 0.381,\\n    \\\"isr_1_count\\\": 0,\\n    \\\"isr_1_rate\\\": 0.0,\\n    \\\"content_independent_count\\\": 1,\\n    \\\"content_independent_rate\\\": 0.0238,\\n    \\\"genuine_count\\\": 23,\\n    \\\"genuine_rate\\\": 0.5476,\\n    \\\"h7_strict_count\\\": 16,\\n    \\\"h7_strict_rate\\\": 0.381\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.58}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-17T11:55:39.206553+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"eval_results\\\": {\\n    \\\"n_total\\\": 100,\\n    \\\"n_proved\\\": 77,\\n    \\\"h7a_count\\\": 11,\\n    \\\"h7a_rate\\\": 0.1429,\\n    \\\"h7b_count\\\": 0,\\n    \\\"h7b_rate\\\": 0.0,\\n    \\\"h7_total_count\\\": 11,\\n    \\\"h7_total_rate\\\": 0.1429,\\n    \\\"h1_strict_count\\\": 20,\\n    \\\"h1_strict_rate\\\": 0.2597,\\n    \\\"h8_conjunction_collapse_count\\\": 4,\\n    \\\"h8_conjunction_collapse_rate\\\": 0.0519,\\n    \\\"conclusion_in_premise_count\\\": 31,\\n    \\\"conclusion_in_premise_rate\\\": 0.4026,\\n    \\\"h7_relaxed_count\\\": 11,\\n    \\\"h7_relaxed_rate\\\": 0.1429,\\n    \\\"single_premise_count\\\": 11,\\n    \\\"single_premise_rate\\\": 0.1429,\\n    \\\"isr_1_count\\\": 0,\\n    \\\"isr_1_rate\\\": 0.0,\\n    \\\"content_independent_count\\\": 2,\\n    \\\"content_independent_rate\\\": 0.026,\\n    \\\"genuine_count\\\": 42,\\n    \\\"genuine_rate\\\": 0.5455,\\n    \\\"h7_strict_count\\\": 11,\\n    \\\"h7_strict_rate\\\": 0.1429\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.58}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-17T11:55:39.206716+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"eval_results\\\": {\\n    \\\"n_total\\\": 100,\\n    \\\"n_proved\\\": 58,\\n    \\\"h7a_count\\\": 0,\\n    \\\"h7a_rate\\\": 0.0,\\n    \\\"h7b_count\\\": 0,\\n    \\\"h7b_rate\\\": 0.0,\\n    \\\"h7_total_count\\\": 0,\\n    \\\"h7_total_rate\\\": 0.0,\\n    \\\"h1_strict_count\\\": 53,\\n    \\\"h1_strict_rate\\\": 0.9138,\\n    \\\"h8_conjunction_collapse_count\\\": 0,\\n    \\\"h8_conjunction_collapse_rate\\\": 0.0,\\n    \\\"conclusion_in_premise_count\\\": 53,\\n    \\\"conclusion_in_premise_rate\\\": 0.9138,\\n    \\\"h7_relaxed_count\\\": 0,\\n    \\\"h7_relaxed_rate\\\": 0.0,\\n    \\\"single_premise_count\\\": 0,\\n    \\\"single_premise_rate\\\": 0.0,\\n    \\\"isr_1_count\\\": 0,\\n    \\\"isr_1_rate\\\": 0.0,\\n    \\\"content_independent_count\\\": 0,\\n    \\\"content_independent_rate\\\": 0.0,\\n    \\\"genuine_count\\\": 5,\\n    \\\"genuine_rate\\\": 0.0862,\\n    \\\"h7_strict_count\\\": 0,\\n    \\\"h7_strict_rate\\\": 0.0\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-17T11:55:39.206874+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"eval_results\\\": {\\n    \\\"n_total\\\": 100,\\n    \\\"n_proved\\\": 94,\\n    \\\"h7a_count\\\": 86,\\n    \\\"h7a_rate\\\": 0.9149,\\n    \\\"h7b_count\\\": 0,\\n    \\\"h7b_rate\\\": 0.0,\\n    \\\"h7_total_count\\\": 86,\\n    \\\"h7_total_rate\\\": 0.9149,\\n    \\\"h1_strict_count\\\": 2,\\n    \\\"h1_strict_rate\\\": 0.0213,\\n    \\\"h8_conjunction_collapse_count\\\": 4,\\n    \\\"h8_conjunction_collapse_rate\\\": 0.0426,\\n    \\\"conclusion_in_premise_count\\\": 88,\\n    \\\"conclusion_in_premise_rate\\\": 0.9362,\\n    \\\"h7_relaxed_count\\\": 0,\\n    \\\"h7_relaxed_rate\\\": 0.0,\\n    \\\"single_premise_count\\\": 0,\\n    \\\"single_premise_rate\\\": 0.0,\\n    \\\"isr_1_count\\\": 0,\\n    \\\"isr_1_rate\\\": 0.0,\\n    \\\"content_independent_count\\\": 4,\\n    \\\"content_independent_rate\\\": 0.0426,\\n    \\\"genuine_count\\\": 2,\\n    \\\"genuine_rate\\\": 0.0213,\\n    \\\"h7_strict_count\\\": 86,\\n    \\\"h7_strict_rate\\\": 0.9149\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.87}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-17T11:55:39.207025+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "find /root/autodl-tmp -name \"h7_classification*.json\" -path \"*plan002*b01*s42*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "find /root/autodl-tmp -name \"h7_classification*.json\" -path \"*plan002*b01*s42*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-17T11:55:39.207145+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "find /root/autodl-tmp -name \"h7_classification*.json\" -path \"*plan002*b01*s43*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "find /root/autodl-tmp -name \"h7_classification*.json\" -path \"*plan002*b01*s43*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-17T11:55:39.207262+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-17T11:55:39.207374+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "find /root/autodl-tmp -name \"h7_classification*.json\" -path \"*plan002*b01*s44*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "find /root/autodl-tmp -name \"h7_classification*.json\" -path \"*plan002*b01*s44*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-17T11:55:39.207485+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "find /root/autodl-tmp -name \"h7_classification*.json\" -path \"*plan018*s42*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "find /root/autodl-tmp -name \"h7_classification*.json\" -path \"*plan018*s42*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-17T11:55:39.207634+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.92}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-17T11:55:39.207773+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "find /root/autodl-tmp -name \"h7_classification*.json\" -path \"*plan018*s43*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "find /root/autodl-tmp -name \"h7_classification*.json\" -path \"*plan018*s43*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-17T11:55:39.207893+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "find /root/autodl-tmp -name \"h7_classification*.json\" -path \"*plan018*s44*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "find /root/autodl-tmp -name \"h7_classification*.json\" -path \"*plan018*s44*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-17T11:55:39.208008+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.66}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-17T11:55:39.208120+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.26}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-17T11:55:39.208230+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.58}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-17T11:55:39.208340+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/outputs/plan018_additive_random_b01_s44_r2/h7_classification.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-17T11:55:39.208450+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "cat /root/autodl-tmp/outputs/plan018_additive_random_b01_s44_r2/h7_classification.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "cat /root/autodl-tmp/outputs/plan018_additive_random_b01_s44_r2/h7_classification.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-17T11:55:39.208601+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"results\\\": {\\n    \\\"n_total\\\": 100,\\n    \\\"n_proved\\\": 89,\\n    \\\"h7a_count\\\": 0,\\n    \\\"h7a_rate\\\": 0.0,\\n    \\\"h7b_count\\\": 0,\\n    \\\"h7b_rate\\\": 0.0,\\n    \\\"h7_total_count\\\": 0,\\n    \\\"h7_total_rate\\\": 0.0,\\n    \\\"h1_strict_count\\\": 73,\\n    \\\"h1_strict_rate\\\": 0.8202,\\n    \\\"h8_conjunction_collapse_count\\\": 16,\\n    \\\"h8_conjunction_collapse_rate\\\": 0.1798,\\n    \\\"conclusion_in_premise_count\\\": 73,\\n    \\\"conclusion_in_premise_rate\\\": 0.8202,\\n    \\\"h7_relaxed_count\\\": 0,\\n    \\\"h7_relaxed_rate\\\": 0.0,\\n    \\\"single_premise_count\\\": 0,\\n    \\\"single_premise_rate\\\": 0.0,\\n    \\\"isr_1_count\\\": 2,\\n    \\\"isr_1_rate\\\": 0.0225,\\n    \\\"content_independent_count\\\": 18,\\n    \\\"content_independent_rate\\\": 0.2022,\\n    \\\"genuine_count\\\": 6,\\n    \\\"genuine_rate\\\": 0.0674,\\n    \\\"h7_strict_count\\\": 0,\\n    \\\"h7_strict_rate\\\": 0.0\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.76}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-17T11:55:39.208744+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "find /root/solver-trace-ablation/analysis -name \"*.json\" -o -name \"*.csv\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "find /root/solver-trace-ablation/analysis -name \"*.json\" -o -name \"*.csv\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-17T11:55:39.208869+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/solver-trace-ablation/analysis/d093_h7_subtype_analysis.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.16}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-17T11:55:39.209005+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "find /root/solver-trace-ablation/analysis -type f -name \"*.py\" -o -name \"*.md\" -o -name \"*.txt\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "find /root/solver-trace-ablation/analysis -type f -name \"*.py\" -o -name \"*.md\" -o -name \"*.txt\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-17T11:55:39.209120+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "find /root/autodl-tmp -name \"h7_classification*.json\" -path \"*plan002*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "find /root/autodl-tmp -name \"h7_classification*.json\" -path \"*plan002*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-17T11:55:39.209236+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/solver-trace-ablation/analysis/h7_convergence_timing.md\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.07}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-17T11:55:39.209349+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/eval_archive/plan002_additive_b01_s45/h7_classification.json\\n/root/autodl-tmp/eval_archive/plan002_additive_b01_s46/h7_classification.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.89}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-17T11:55:39.209494+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "find /root/autodl-tmp -name \"h7_classification*.json\" -path \"*plan018*s42*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "find /root/autodl-tmp -name \"h7_classification*.json\" -path \"*plan018*s42*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-17T11:55:39.209610+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "find /root/autodl-tmp -name \"h7_classification*.json\" -path \"*plan018*s43*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "find /root/autodl-tmp -name \"h7_classification*.json\" -path \"*plan018*s43*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-17T11:55:39.209744+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "find /root/solver-trace-ablation -name \"*.json\" -path \"*h7*\" -o -name \"*.json\" -path \"*h8*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "find /root/solver-trace-ablation -name \"*.json\" -path \"*h7*\" -o -name \"*.json\" -path \"*h8*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-17T11:55:39.209868+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.27}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-17T11:55:39.209979+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.6}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-17T11:55:39.210089+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/solver-trace-ablation/outputs/classify_h7_plan016_s42_1000.json\\n/root/solver-trace-ablation/analysis/d093_h7_subtype_analysis.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.58}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-17T11:55:39.210211+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "cat /root/solver-trace-ablation/analysis/d093_h7_subtype_analysis.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "cat /root/solver-trace-ablation/analysis/d093_h7_subtype_analysis.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-17T11:55:39.210404+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"analysis_id\\\": \\\"D093-H7-subtype-analysis\\\",\\n  \\\"date\\\": \\\"2026-05-15\\\",\\n  \\\"purpose\\\": \\\"Classify H7 subtypes for Random s43-r3, verify exec-only s43 H7 data from D089\\\",\\n\\n  \\\"random_s43r3_h7_subtypes\\\": {\\n    \\\"exp_id\\\": \\\"plan018-additive-random-b01-s43-r3\\\",\\n    \\\"reward_mode\\\": \\\"additive_random\\\",\\n    \\\"beta\\\": 0.1,\\n    \\\"seed\\\": 43,\\n    \\\"steps\\\": 500,\\n    \\\"n_proved\\\": 94,\\n    \\\"h7a_count\\\": 36,\\n    \\\"h7b_count\\\": 0,\\n    \\\"total_h7\\\": 36,\\n    \\\"h7_rate\\\": 0.383,\\n    \\\"h1_strict_count\\\": 56,\\n    \\\"h8_count\\\": 1,\\n    \\\"genuine_count\\\": 1,\\n    \\\"genuine_rate\\\": 0.0106,\\n    \\\"single_premise_count\\\": 0,\\n    \\\"conclusion_in_premise_count\\\": 92,\\n    \\\"details\\\": \\\"All 36 H7 cases are H7a (text-match tautology). Zero H7b (obfuscated tautology via vacuous quantifier). Notable: single_premise_count=0, so H7a cases here are multi-premise proofs where one premise exactly text-matches the conclusion. H7a examples: folio_207 (5 premises), folio_304 (2 premises), folio_402 (6 premises).\\\"\\n  },\\n\\n  \\\"exec_only_s43_verification\\\": {\\n    \\\"exp_id\\\": \\\"plan001-exec-only-s43-1000-r2\\\",\\n    \\\"is_exec_only\\\": true,\\n    \\\"verification_evidence\\\": {\\n      \\\"reward_log_random_mean\\\": null,\\n      \\\"reward_log_beta_t\\\": null,\\n      \\\"training_args_beta\\\": 0.0,\\n      \\\"training_args_reward_weights\\\": null,\\n      \\\"reward_equals_prove_rate\\\": true,\\n      \\\"note\\\": \\\"reward_log step 1: reward_mean=0.375 matches prove_rate=0.375 exactly. No STA or random bonus components.\\\"\\n    },\\n    \\\"config_used\\\": {\\n      \\\"seed\\\": 43,\\n      \\\"max_steps\\\": 1000,\\n      \\\"loss_type\\\": \\\"dapo\\\",\\n      \\\"learning_rate\\\": 1e-6,\\n      \\\"output_dir\\\": \\\"/root/autodl-tmp/outputs/plan001
…[truncated 2145 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-17T11:55:39.210579+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "plan002.*b01.*s42|ISR.*s42.*H8|seed.*42.*H8",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "glob": "*.{md,yaml,tex}",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "Grep",
  "tool_args": {
    "pattern": "plan002.*b01.*s42|ISR.*s42.*H8|seed.*42.*H8",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
    "glob": "*.{md,yaml,tex}",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-17T11:55:39.210746+00:00_

Found 108 files
ROADMAP.md
decisions.yaml
registry.yaml
artifacts/review_reports/round_4.md
paper/experiments.tex
paper/appendix.tex
artifacts/4b_dose_response_summary.md
artifacts/manifest.yaml
docs/paper/appendix.tex
docs/paper/experiments.tex
artifacts/sweep-isr-b01-s45/analysis_report.md
artifacts/sweep-isr-b01-s45/report/analysis_report.md
artifacts/submission/experiments.tex
artifacts/submission/appendix.tex
artifacts/submission_package/experiments.tex
artifacts/submission_package/appendix.tex
task_context/history/agent/loop_14_1778885190.md
task_context/history/agent/loop_14_1778883679.md
task_context/history/agent/loop_14_1778882039.md
task_context/history/agent/loop_14.md
task_context/history/agent/loop_13_1778880047.md
task_context/history/agent/loop_13_1778880025.md
docs/paper/experiments.md
paper_provenance.yaml
artifacts/_project/paper/experiments_da3450.tex
artifacts/_project/paper/experiments.tex
task_context/history/agent/loop_13_1778873197.md
artifacts/_project/report/3seed_comparison_table.md
artifacts/3seed_comparison_table.md
task_context/history/agent/loop_13.md
task_context/history/agent/loop_12_1778868309.md
task_context/history/agent/loop_12_1778868094.md
task_context/history/agent/loop_12_1778863924.md
task_context/history/agent/loop_12_1778863156.md
experiment_plan.yaml
artifacts/_project/report/tex_number_audit_20260515.md
artifacts/tex_number_audit_20260515.md
task_context/history/reviewer/loop_9.md
task_context/history/director/loop_6.md
task_context/history/agent/loop_11_1778848870.md
task_context/history/agent/loop_11_1778847699.md
task_context/history/agent/loop_11_1778847578.md
task_context/history/agent/loop_11.md
task_context/history/reviewer/loop_8.md
artifacts/_project/paper/experiments_49ea86.tex
artifacts/_project/paper/experiments_76b47a.tex
paper/experiments.md
paper_review_loop10.md
artifacts/data_consistency_report.md
artifacts/_project/report/paper_number_audit.md
artifacts/paper_number_audit.md
writing_plan.yaml
artifacts
…[truncated 2607 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-17T11:55:39.210894+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "find /root/solver-trace-ablation -name \"*.md\" -path \"*analysis*\" -o -name \"*.yaml\" -path \"*analysis*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "find /root/solver-trace-ablation -name \"*.md\" -path \"*analysis*\" -o -name \"*.yaml\" -path \"*analysis*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-17T11:55:39.211019+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/solver-trace-ablation/analysis/h7_convergence_timing.md\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.18}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-17T11:55:39.211144+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "offset": "1",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
    "offset": "1",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-17T11:55:39.211306+00:00_

1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
9	
10	\begin{table}[h]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\footnotesize
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 4 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Evaluation exception.}
53	FOL exec-only seed~43 (\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.
54	Its PR and ISR values are included for completeness but are not strictly comparable with other se
…[truncated 3709 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-17T11:55:39.211462+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "H8|h8_conjunction|seed.*42.*43.*44.*45.*46",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "Grep",
  "tool_args": {
    "pattern": "H8|h8_conjunction|seed.*42.*43.*44.*45.*46",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-17T11:55:39.211641+00:00_

89:\caption{Fisher exact tests across conditions. Non-hacking rate reported at 5-seed (primary) and 3-seed with H8+FN corrections (sensitivity); H7 comparison at 5-seed (primary) and 3-seed (sensitivity).}
99:\multicolumn{5}{@{}l}{\textit{Non-hacking rate (3-seed, H8+FN corrected)}} \\
174:H8 & Premise-subset gaming & 6 & 5 & -- & 0 \\
182:[Omitted long matching line]
197:\subsection{H8 --- Premise-Subset Gaming}
201:We term this \textbf{H8 (premise-subset gaming)}: formalizations where each component is LOO-necessary but the premise set is a strict subset of what the NL problem requires, inflating ISR without faithful reasoning.
203:\paragraph{Detection.} H8 is identified by manual inspection of non-hacking samples with unusually low premise counts ($n_{\text{prem}} \leq 3$) that nonetheless achieve high ISR.
204:Automated detection is not currently feasible because H8 requires comparing the generated premise set against the gold premises.
207:Full H8 audit was completed for ISR $\beta{=}0.1$ seed~42 only.
209:Random $\beta{=}0.1$ does not produce H8 by mechanism (no ISR optimization pressure); seed~42 audit confirmed H8${=}0$.
219:After H8 reclassification and H7 false-negative correction: ISR non-hacking $= 14/231 = 6.06\%$ vs.\ random non-hacking $= 25/262 = 9.5\%$ (Fisher $p{=}0.182$, n.s.; Wilson 95\% CI: ISR [3.6\%, 9.9\%], Random [6.5\%, 13.7\%]).
220:The direction is consistent with ISR-amplified gaming modes (H7, H8) displacing non-hacking output, but the effect is not statistically significant at the conventional $\alpha{=}0.05$ threshold.
449:[Omitted long matching line]
472:  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 7.5 & H8${=}6.5\%$ \\
477:  & 44 & 1000 & 1.00 & 0.002 & 0 & 85 & 0$^\ddagger$ & H8${=}15\%$ \\
483:  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \textbf{17.3} & Mixed H1+H7+H8 \\
493:  & 42 & 500 & 0.79 & 0.131 & 0 & 73.4 & 22.8 & H8${=}4$ \\
494:  & 43 & 500 & 0.94 & 0.150 & \textbf{38.3} & 59.6 & 1.1 & H7a${=}36$; H8${=}1$ \\
495:  & 44 & 500
…[truncated 148 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-17T11:55:39.211820+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "5-seed|five.seed|tab:fol-beta01",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "Grep",
  "tool_args": {
    "pattern": "5-seed|five.seed|tab:fol-beta01",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-17T11:55:39.211955+00:00_

61:ISR & 0.1 & 70{\scriptsize$\pm$19} & --- & \textbf{54} & 18 & 23$^\star$ \\ %% registry: plan002-additive-b01-s42/s43-r2/s44/s45/s46 (5-seed, D124)
62:Random & 0.1 & \textbf{83}{\scriptsize$\pm$15} & 0.080{\scriptsize$\pm$.06} & 30 & 59 & 8 \\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2/s45/s46 (5-seed)
74:[Omitted long matching line]
81:The 5-seed pooled non-hacking rate is ${\sim}23\%$ at 500 steps, with the collapsed seeds pulling down the average; the 3 non-collapsed seeds individually range from $17\%$ to $55\%$ genuine.
93:During the transient window, ISR-trained seeds produce significantly more genuine proofs than random controls (5-seed pooled: $22.6\%$ vs.\ $7.7\%$; $\text{OR}{=}3.48$, $p{<}10^{-8}$; Appendix Table~\ref{tab:bootstrap-ci}), confirming that ISR increases the proportion of genuine proofs.
224:The three dominant modes, \textbf{H1} (conclusion embedding, GRPO-universal at $68$--$100\%$), \textbf{H7} (conclusion duplication, ISR-amplified; $\text{OR}{=}2.84$, Fisher $p{<}5{\times}10^{-12}$, 5-seed; Appendix Table~\ref{tab:bootstrap-ci}), and \textbf{H8} (premise-subset gaming; Appendix~\ref{app:h8}), account for $>90\%$ of hacking.
227:ISR modestly increases the probability of H7 convergence ($\text{OR}{=}2.84$, $p{<}5{\times}10^{-12}$, 5-seed), but per-seed variance dominates: Random s46 reaches $91.5\%$ H7 while ISR s46 shows $14.3\%$, reversing the direction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-17T11:55:39.212083+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "offset": "440",
  "limit": "70"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
    "offset": "440",
    "limit": "70"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-17T11:55:39.212239+00:00_

440	\section{Per-Seed Detailed Results}
441	\label{app:detailed-results}
442	
443	Tables~\ref{tab:fol-beta01-detailed} and \ref{tab:prolog-detailed} report full per-seed results.
444	All metrics are computed by \texttt{eval\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.
445	ISR values are proved-only ISR$^*$.
446	
447	\begin{table*}[t]
448	\centering
449	\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\beta{=}0.1$ breakdown referenced from Table~\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H\ = percentage among proved samples. ``---'' indicates data not available. $^\dagger$s43 uses sampling eval ($T{=}0.7$). $^\ddagger$Three s44-1000 samples escape text-match heuristics (H1/H8 classifiers) but exhibit ISR${=}0$ and functionally degenerate proof structures: disjunctive conclusions that bypass H8 detection and commuted premises that bypass H1 detection; reclassified as degenerate. $^\S$s43-1000 raw ISR (0.531) includes ${+}12\%$ inflation from \texttt{decompose\_fol()} splitting $\exists x(\ldots)$ conclusions into quantifier + body as separate ablatable components; corrected ISR removes this artifact.}
450	\label{tab:fol-detailed}
451	\label{tab:fol-beta01-detailed}
452	\footnotesize
453	\setlength{\tabcolsep}{3pt}
454	\begin{tabular}{@{}llccccccl@{}}
455	\toprule
456	\textbf{Condition} & \textbf{Seed} & \textbf{Steps} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} & \textbf{Notes} \\
457	\midrule
458	\multicolumn{9}{@{}l}{\textit{Baselines}} \\
459	Base model (no training)
460	  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\
461	Ground-truth FOL
462	  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\
463	SFT
464	  & 42 & 1000 & 0.13 & 0.568 & 0 & 7.7 & \textbf{92.3} & Supervised, no RL \\
465	  & 43 & 1000 & 0.11 & 0.635 & 0 & 9.1 & \textbf{90.9} & \\
466	  & 44 & 1000 & 0.15 & 
…[truncated 2776 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-17T11:55:39.212439+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-39279",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && pip list 2>/dev/null | grep -i statsmodels",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-39279",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && pip list 2>/dev/null | grep -i statsmodels",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-17T11:55:39.212573+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"statsmodels                              0.14.6\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.65}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-17T11:55:39.212719+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-39279",
  "command": "mkdir -p /root/solver-trace-ablation/analysis",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-39279",
    "command": "mkdir -p /root/solver-trace-ablation/analysis",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-17T11:55:39.212846+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.11}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-17T11:55:39.212999+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-39279",
  "command": "cat > /root/solver-trace-ablation/analysis/seed_level_stats.py << 'SCRIPT'\n\"\"\"\nSeed-Level Statistical Analysis: ISR β=0.1 vs Random β=0.1 (5-seed)\nCluster-aware statistics addressing pooled Fisher test limitations.\n\"\"\"\nimport numpy as np\nfrom scipy import stats\nfrom statsmodels.stats.contingency_tables import StratifiedTable\nfrom statsmodels.stats.proportion import proportion_confint\n\n# =============================================================================\n# DATA (C013 taxonomy: genuine = proved - H7 - H1 - H8)\n# =============================================================================\n\nisr_data = {\n    # seed: (proved, H7, H1, H8, genuine)\n    42: (81, 13, 42, 12, 14),\n    43: (61, 59,  0,  0,  2),\n    44: (89, 89,  0,  0,  0),\n    45: (42, 16,  2,  1, 23),\n    46: (77, 11, 20,  4, 42),\n}\n\nrandom_data = {\n    # seed: (proved, H7, H1, H8, genuine)\n    42: (79,  0, 58,  4, 18),\n    43: (94, 36, 56,  1,  1),\n    44: (89,  0, 73, 16,  6),\n    45: (58,  0, 53,  0,  5),\n    46: (94, 86,  2,  4,  2),\n}\n\nseeds = [42, 43, 44, 45, 46]\n\nprint(\"=\" * 70)\nprint(\"SEED-LEVEL STATISTICAL ANALYSIS: ISR β=0.1 vs Random β=0.1\")\nprint(\"=\" * 70)\n\n# =============================================================================\n# 2a. CMH Test (Cochran-Mantel-Haenszel)\n# =============================================================================\nprint(\"\\n\" + \"=\" * 70)\nprint(\"2a. COCHRAN-MANTEL-HAENSZEL (CMH) TEST\")\nprint(\"=\" * 70)\n\n# --- H7 rate comparison ---\n# For each seed stratum, build 2x2 table:\n#   ISR:    [H7, non-H7]\n#   Random: [H7, non-H7]\ntables_h7 = []\nfor s in seeds:\n    ip, ih7, _, _, _ = isr_data[s]\n    rp, rh7, _, _, _ = random_data[s]\n    table = np.array([[ih7, ip - ih7],\n                      [rh7, rp - rh7]])\n    tables_h7.append(table)\n\nst_h7 = StratifiedTable(tables_h7)\ncmh_h7 = st_h7.test_null_odds()\nprint(f\"\\n--- H7 Rate: ISR vs Random (stratified by seed) ---\")\nprint(f\"  Common OR:  {st_h7.common_odds_ratio:.4f}\")\nci_h7 = st_h7.oddsratio_pooled_confint()\nprint(f\"  95% CI:     [{ci_h7[0]:.4f}, {ci_h7[1]:.4f}]\")\nprint(f\"  CMH stat:   {cmh_h7.statistic:.4f}\")\nprint(f\"  p-value:    {cmh_h7.pvalue:.6e}\")\n\n# --- Genuine rate comparison ---\ntables_gen = []\nfor s in seeds:\n    ip, _, _, _, ig = isr_data[s]\n    rp, _, _, _, rg = random_data[s]\n    table = np.array([[ig, ip - ig],\n                      [rg, rp - rg]])\n    tables_gen.append(table)\n\nst_gen = StratifiedTable(tables_gen)\ncmh_gen = st_gen.test_null_odds()\nprint(f\"\\n--- Genuine Rate: ISR vs Random (stratified by seed) ---\")\nprint(f\"  Common OR:  {st_gen.common_odds_ratio:.4f}\")\nci_gen = st_gen.oddsratio_pooled_confint()\nprint(f\"  95% CI:     [{ci_gen[0]:.4f}, {ci_gen[1]:.4f}]\")\nprint(f\"  CMH stat:   {cmh_gen.statistic:.4f}\")\nprint(f\"  p-value:    {cmh_gen.pvalue:.6e}\")\n\n# =============================================================================\n# 2b. Permutation Test\n# =============================================================================\nprint(\"\\n\" + \"=\" * 70)\nprint(\"2b. PERMUTATION TEST (seed-level rates as units)\")\nprint(\"=\" * 70)\n\nnp.random.seed(2024)\nn_perm = 10000\n\n# H7 rates per seed\nisr_h7_rates = np.array([isr_data[s][1] / isr_data[s][0] for s in seeds])\nrand_h7_rates = np.array([random_data[s][1] / random_data[s][0] for s in seeds])\n\nobs_diff_h7 = np.mean(isr_h7_rates) - np.mean(rand_h7_rates)\ncombined_h7 = np.concatenate([isr_h7_rates, rand_h7_rates])\n\ncount_h7 = 0\nfor _ in range(n_perm):\n    perm = np.random.permutation(combined_h7)\n    perm_diff = np.mean(perm[:5]) - np.mean(perm[5:])\n    if abs(perm_diff) >= abs(obs_diff_h7):\n        count_h7 += 1\n\nperm_p_h7 = count_h7 / n_perm\n\nprint(f\"\\n--- H7 Rate Permutation Test ---\")\nprint(f\"  ISR H7 rates per seed:    {[f'{r:.4f}' for r in isr_h7_rates]}\")\nprint(f\"  Random H7 rates per seed: {[f'{r:.4f}' for r in rand_h7_rates]}\")\nprint(f\"  ISR mean H7 rate:         {np.mean(isr_h7_rates):.4f}\")\nprint(f\"  Random mean H7 rate:      {np.mean(rand_h7_rates):.4f}\")\nprint(f\"  Observed difference:      {obs_diff_h7:.4f}\")\nprint(f\"  Permutation p-value:      {perm_p_h7:.4f} (two-sided, {n_perm} perms)\")\n\n# Genuine rates per seed\nisr_gen_rates = np.array([isr_data[s][4] / isr_data[s][0] for s in seeds])\nrand_gen_rates = np.array([random_data[s][4] / random_data[s][0] for s in seeds])\n\nobs_diff_gen = np.mean(isr_gen_rates) - np.mean(rand_gen_rates)\ncombined_gen = np.concatenate([isr_gen_rates, rand_gen_rates])\n\ncount_gen = 0\nfor _ in range(n_perm):\n    perm = np.random.permutation(combined_gen)\n    perm_diff = np.mean(perm[:5]) - np.mean(perm[5:])\n    if abs(perm_diff) >= abs(obs_diff_gen):\n        count_gen += 1\n\nperm_p_gen = count_gen / n_perm\n\nprint(f\"\\n--- Genuine Rate Permutation Test ---\")\nprint(f\"  ISR genuine rates per seed:    {[f'{r:.4f}' for r in isr_gen_rates]}\")\nprint(f\"  Random genuine rates per seed: {[f'{r:.4f}' for r in rand_gen_rates]}\")\nprint(f\"  ISR mean genuine rate:         {np.mean(isr_gen_rates):.4f}\")\nprint(f\"  Random mean genuine rate:      {np.mean(rand_gen_rates):.4f}\")\nprint(f\"  Observed difference:           {obs_diff_gen:.4f}\")\nprint(f\"  Permutation p-value:           {perm_p_gen:.4f} (two-sided, {n_perm} perms)\")\n\n# Non-hacking rate (genuine / proved, same as genuine rate)\n# Also do H7+H8 hacking combined\nisr_hack_rates = np.array([(isr_data[s][1] + isr_data[s][3]) / isr_data[s][0] for s in seeds])\nrand_hack_rates = np.array([(random_data[s][1] + random_data[s][3]) / random_data[s][0] for s in seeds])\n\nobs_diff_hack = np.mean(isr_hack_rates) - np.mean(rand_hack_rates)\ncombined_hack = np.concatenate([isr_hack_rates, rand_hack_rates])\n\ncount_hack = 0\nfor _ in range(n_perm):\n    perm = np.random.permutation(combined_hack)\n    perm_diff = np.mean(perm[:5]) - np.mean(perm[5:])\n    if abs(perm_diff) >= abs(obs_diff_hack):\n        count_hack += 1\n\nperm_p_hack = count_hack / n_perm\n\nprint(f\"\\n--- H7+H8 Combined Hacking Rate Permutation Test ---\")\nprint(f\"  ISR (H7+H8)/proved per seed:    {[f'{r:.4f}' for r in isr_hack_rates]}\")\nprint(f\"  Random (H7+H8)/proved per seed: {[f'{r:.4f}' for r in rand_hack_rates]}\")\nprint(f\"  Observed difference:            {obs_diff_hack:.4f}\")\nprint(f\"  Permutation p-value:            {perm_p_hack:.4f} (two-sided, {n_perm} perms)\")\n\n# =============================================================================\n# 2c. Wilson CI for Per-Seed Percentages\n# =============================================================================\nprint(\"\\n\" + \"=\" * 70)\nprint(\"2c. WILSON 95% CI FOR PER-SEED METRICS\")\nprint(\"=\" * 70)\n\nprint(f\"\\n{'Cond':<8} {'Seed':<5} {'Proved':<7} {'H7%':<18} {'Genuine%':<18} {'Non-hack%':<18}\")\nprint(\"-\" * 75)\n\nfor cond_name, data in [(\"ISR\", isr_data), (\"Random\", random_data)]:\n    for s in seeds:\n        proved, h7, h1, h8, genuine = data[s]\n        non_hack = genuine  # non-hacking = genuine per C013\n        \n        # H7%\n        h7_lo, h7_hi = proportion_confint(h7, proved, alpha=0.05, method='wilson')\n        # Genuine%\n        gen_lo, gen_hi = proportion_confint(genuine, proved, alpha=0.05, method='wilson')\n        # Non-hacking% (same as genuine%)\n        nh_lo, nh_hi = gen_lo, gen_hi\n        \n        h7_pct = h7 / proved * 100\n        gen_pct = genuine / proved * 100\n        \n        print(f\"{cond_name:<8} {s:<5} {proved:<7} \"\n              f\"{h7_pct:5.1f} [{h7_lo*100:4.1f},{h7_hi*100:4.1f}]  \"\n              f\"{gen_pct:5.1f} [{gen_lo*100:4.1f},{gen_hi*100:4.1f}]  \"\n              f\"{gen_pct:5.1f} [{nh_lo*100:4.1f},{nh_hi*100:4.1f}]\")\n    print()\n\n# =============================================================================\n# 2d. 5-Seed Pooled Summary\n# =============================================================================\nprint(\"=\" * 70)\nprint(\"2d. 5-SEED POOLED SUMMARY + FISHER EXACT TEST\")\nprint(\"=\" * 70)\n\nisr_proved_total = sum(isr_data[s][0] for s in seeds)\nisr_h7_total = sum(isr_data[s][1] for s in seeds)\nisr_gen_total = sum(isr_data[s][4] for s in seeds)\nisr_h8_total = sum(isr_data[s][3] for s in seeds)\nisr_h1_total = sum(isr_data[s][2] for s in seeds)\n\nrand_proved_total = sum(random_data[s][0] for s in seeds)\nrand_h7_total = sum(random_data[s][1] for s in seeds)\nrand_gen_total = sum(random_data[s][4] for s in seeds)\nrand_h8_total = sum(random_data[s][3] for s in seeds)\nrand_h1_total = sum(random_data[s][2] for s in seeds)\n\nprint(f\"\\n  {'Metric':<20} {'ISR β=0.1':<20} {'Random β=0.1':<20}\")\nprint(f\"  {'-'*60}\")\nprint(f\"  {'Proved (total)':<20} {isr_proved_total:<20} {rand_proved_total:<20}\")\nprint(f\"  {'H7 (total)':<20} {isr_h7_total:<20} {rand_h7_total:<20}\")\nprint(f\"  {'H1 (total)':<20} {isr_h1_total:<20} {rand_h1_total:<20}\")\nprint(f\"  {'H8 (total)':<20} {isr_h8_total:<20} {rand_h8_total:<20}\")\nprint(f\"  {'Genuine (total)':<20} {isr_gen_total:<20} {rand_gen_total:<20}\")\nprint(f\"  {'H7 rate':<20} {isr_h7_total/isr_proved_total:.4f} ({isr_h7_total}/{isr_proved_total}){'':<5} {rand_h7_total/rand_proved_total:.4f} ({rand_h7_total}/{rand_proved_total})\")\nprint(f\"  {'Genuine rate':<20} {isr_gen_total/isr_proved_total:.4f} ({isr_gen_total}/{isr_proved_total}){'':<5} {rand_gen_total/rand_proved_total:.4f} ({rand_gen_total}/{rand_proved_total})\")\n\n# Pooled Fisher: H7\ntable_h7_pooled = np.array([[isr_h7_total, isr_proved_total - isr_h7_total],\n                            [rand_h7_total, rand_proved_total - rand_h7_total]])\nor_h7, p_h7 = stats.fisher_exact(table_h7_pooled)\nprint(f\"\\n  --- Pooled Fisher Exact: H7 ---\")\nprint(f\"  OR = {or_h7:.4f}, p = {p_h7:.6e}\")\n\n# Pooled Fisher: Genuine\ntable_gen_pooled = np.array([[isr_gen_total, isr_proved_total - isr_gen_total],\n                             [rand_gen_total, rand_proved_total - rand_gen_total]])\nor_gen, p_gen = stats.fisher_exact(table_gen_pooled)\nprint(f\"\\n  --- Pooled Fisher Exact: Genuine ---\")\nprint(f\"  OR = {or_gen:.4f}, p = {p_gen:.6e}\")\n\n# Wilson CI for pooled rates\nisr_gen_lo, isr_gen_hi = proportion_confint(isr_gen_total, isr_proved_total, alpha=0.05, method='wilson')\nrand_gen_lo, rand_gen_hi = proportion_confint(rand_gen_total, rand_proved_total, alpha=0.05, method='wilson')\nprint(f\"\\n  --- Pooled Wilson 95% CI ---\")\nprint(f\"  ISR genuine rate:    {isr_gen_total/isr_proved_total:.4f} [{isr_gen_lo:.4f}, {isr_gen_hi:.4f}]\")\nprint(f\"  Random genuine rate: {rand_gen_total/rand_proved_total:.4f} [{rand_gen_lo:.4f}, {rand_gen_hi:.4f}]\")\n\n# =============================================================================\n# SUMMARY\n# =============================================================================\nprint(\"\\n\" + \"=\" * 70)\nprint(\"SUMMARY TABLE\")\nprint(\"=\" * 70)\n\nprint(f\"\\n  {'Test':<40} {'Statistic':<15} {'p-value':<15} {'Significant?'}\")\nprint(f\"  {'-'*80}\")\nprint(f\"  {'CMH: H7 rate':<40} {'OR='+f'{st_h7.common_odds_ratio:.3f}':<15} {cmh_h7.pvalue:<15.4e} {'Yes' if cmh_h7.pvalue < 0.05 else 'No'}\")\nprint(f\"  {'CMH: Genuine rate':<40} {'OR='+f'{st_gen.common_odds_ratio:.3f}':<15} {cmh_gen.pvalue:<15.4e} {'Yes' if cmh_gen.pvalue < 0.05 else 'No'}\")\nprint(f\"  {'Permutation: H7 rate diff':<40} {'Δ='+f'{obs_diff_h7:.4f}':<15} {perm_p_h7:<15.4f} {'Yes' if perm_p_h7 < 0.05 else 'No'}\")\nprint(f\"  {'Permutation: Genuine rate diff':<40} {'Δ='+f'{obs_diff_gen:.4f}':<15} {perm_p_gen:<15.4f} {'Yes' if perm_p_gen < 0.05 else 'No'}\")\nprint(f\"  {'Permutation: H7+H8 hacking diff':<40} {'Δ='+f'{obs_diff_hack:.4f}':<15} {perm_p_hack:<15.4f} {'Yes' if perm_p_hack < 0.05 else 'No'}\")\nprint(f\"  {'Pooled Fisher: H7':<40} {'OR='+f'{or_h7:.3f}':<15} {p_h7:<15.4e} {'Yes' if p_h7 < 0.05 else 'No'}\")\nprint(f\"  {'Pooled Fisher: Genuine':<40} {'OR='+f'{or_gen:.3f}':<15} {p_gen:<15.4e} {'Yes' if p_gen < 0.05 else 'No'}\")\n\nprint(\"\\n\\nNote: With only 5 seeds per group, permutation tests have limited resolution\")\nprint(\"(minimum possible p-value = 2/C(10,5) = 2/252 ≈ 0.008 for exact permutation).\")\nprint(\"CMH accounts for seed-level clustering in a sample-level framework.\")\nSCRIPT",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-39279",
    "command": "cat > /root/solver-trace-ablation/analysis/seed_level_stats.py << 'SCRIPT'\n\"\"\"\nSeed-Level Statistical Analysis: ISR β=0.1 vs Random β=0.1 (5-seed)\nCluster-aware statistics addressing pooled Fisher test limitations.\n\"\"\"\nimport numpy as np\nfrom scipy import stats\nfrom statsmodels.stats.contingency_tables import StratifiedTable\nfrom statsmodels.stats.proportion import proportion_confint\n\n# =============================================================================\n# DATA (C013 taxonomy: genuine = proved - H7 - H1 - H8)\n# =============================================================================\n\nisr_data = {\n    # seed: (proved, H7, H1, H8, genuine)\n    42: (81, 13, 42, 12, 14),\n    43: (61, 59,  0,  0,  2),\n    44: (89, 89,  0,  0,  0),\n    45: (42, 16,  2,  1, 23),\n    46: (77, 11, 20,  4, 42),\n}\n\nrandom_data = {\n    # seed: (proved, H7, H1, H8, genuine)\n    42: (79,  0, 58,  4, 18),\n    43: (94, 36, 56,  1,  1),\n    44: (89,  0, 73, 16,  6),\n    45: (58,  0, 53,  0,  5),\n    46: (94, 86,  2,  4,  2),\n}\n\nseeds = [42, 43, 44, 45, 46]\n\nprint(\"=\" * 70)\nprint(\"SEED-LEVEL STATISTICAL ANALYSIS: ISR β=0.1 vs Random β=0.1\")\nprint(\"=\" * 70)\n\n# =============================================================================\n# 2a. CMH Test (Cochran-Mantel-Haenszel)\n# =============================================================================\nprint(\"\\n\" + \"=\" * 70)\nprint(\"2a. COCHRAN-MANTEL-HAENSZEL (CMH) TEST\")\nprint(\"=\" * 70)\n\n# --- H7 rate comparison ---\n# For each seed stratum, build 2x2 table:\n#   ISR:    [H7, non-H7]\n#   Random: [H7, non-H7]\ntables_h7 = []\nfor s in seeds:\n    ip, ih7, _, _, _ = isr_data[s]\n    rp, rh7, _, _, _ = random_data[s]\n    table = np.array([[ih7, ip - ih7],\n                      [rh7, rp - rh7]])\n    tables_h7.append(table)\n\nst_h7 = StratifiedTable(tables_h7)\ncmh_h7 = st_h7.test_null_odds()\nprint(f\"\\n--- H7 Rate: ISR vs Random (stratified by seed) ---\")\nprint(f\"  Common OR:  {st_h7.common_odds_ratio:.4f}\")\nci_h7 = st_h7.oddsratio_pooled_confint()\nprint(f\"  95% CI:     [{ci_h7[0]:.4f}, {ci_h7[1]:.4f}]\")\nprint(f\"  CMH stat:   {cmh_h7.statistic:.4f}\")\nprint(f\"  p-value:    {cmh_h7.pvalue:.6e}\")\n\n# --- Genuine rate comparison ---\ntables_gen = []\nfor s in seeds:\n    ip, _, _, _, ig = isr_data[s]\n    rp, _, _, _, rg = random_data[s]\n    table = np.array([[ig, ip - ig],\n                      [rg, rp - rg]])\n    tables_gen.append(table)\n\nst_gen = StratifiedTable(tables_gen)\ncmh_gen = st_gen.test_null_odds()\nprint(f\"\\n--- Genuine Rate: ISR vs Random (stratified by seed) ---\")\nprint(f\"  Common OR:  {st_gen.common_odds_ratio:.4f}\")\nci_gen = st_gen.oddsratio_pooled_confint()\nprint(f\"  95% CI:     [{ci_gen[0]:.4f}, {ci_gen[1]:.4f}]\")\nprint(f\"  CMH stat:   {cmh_gen.statistic:.4f}\")\nprint(f\"  p-value:    {cmh_gen.pvalue:.6e}\")\n\n# =============================================================================\n# 2b. Permutation Test\n# =============================================================================\nprint(\"\\n\" + \"=\" * 70)\nprint(\"2b. PERMUTATION TEST (seed-level rates as units)\")\nprint(\"=\" * 70)\n\nnp.random.seed(2024)\nn_perm = 10000\n\n# H7 rates per seed\nisr_h7_rates = np.array([isr_data[s][1] / isr_data[s][0] for s in seeds])\nrand_h7_rates = np.array([random_data[s][1] / random_data[s][0] for s in seeds])\n\nobs_diff_h7 = np.mean(isr_h7_rates) - np.mean(rand_h7_rates)\ncombined_h7 = np.concatenate([isr_h7_rates, rand_h7_rates])\n\ncount_h7 = 0\nfor _ in range(n_perm):\n    perm = np.random.permutation(combined_h7)\n    perm_diff = np.mean(perm[:5]) - np.mean(perm[5:])\n    if abs(perm_diff) >= abs(obs_diff_h7):\n        count_h7 += 1\n\nperm_p_h7 = count_h7 / n_perm\n\nprint(f\"\\n--- H7 Rate Permutation Test ---\")\nprint(f\"  ISR H7 rates per seed:    {[f'{r:.4f}' for r in isr_h7_rates]}\")\nprint(f\"  Random H7 rates per seed: {[f'{r:.4f}' for r in rand_h7_rates]}\")\nprint(f\"  ISR mean H7 rate:         {np.mean(isr_h7_rates):.4f}\")\nprint(f\"  Random mean H7 rate:      {np.mean(rand_h7_rates):.4f}\")\nprint(f\"  Observed difference:      {obs_diff_h7:.4f}\")\nprint(f\"  Permutation p-value:      {perm_p_h7:.4f} (two-sided, {n_perm} perms)\")\n\n# Genuine rates per seed\nisr_gen_rates = np.array([isr_data[s][4] / isr_data[s][0] for s in seeds])\nrand_gen_rates = np.array([random_data[s][4] / random_data[s][0] for s in seeds])\n\nobs_diff_gen = np.mean(isr_gen_rates) - np.mean(rand_gen_rates)\ncombined_gen = np.concatenate([isr_gen_rates, rand_gen_rates])\n\ncount_gen = 0\nfor _ in range(n_perm):\n    perm = np.random.permutation(combined_gen)\n    perm_diff = np.mean(perm[:5]) - np.mean(perm[5:])\n    if abs(perm_diff) >= abs(obs_diff_gen):\n        count_gen += 1\n\nperm_p_gen = count_gen / n_perm\n\nprint(f\"\\n--- Genuine Rate Permutation Test ---\")\nprint(f\"  ISR genuine rates per seed:    {[f'{r:.4f}' for r in isr_gen_rates]}\")\nprint(f\"  Random genuine rates per seed: {[f'{r:.4f}' for r in rand_gen_rates]}\")\nprint(f\"  ISR mean genuine rate:         {np.mean(isr_gen_rates):.4f}\")\nprint(f\"  Random mean genuine rate:      {np.mean(rand_gen_rates):.4f}\")\nprint(f\"  Observed difference:           {obs_diff_gen:.4f}\")\nprint(f\"  Permutation p-value:           {perm_p_gen:.4f} (two-sided, {n_perm} perms)\")\n\n# Non-hacking rate (genuine / proved, same as genuine rate)\n# Also do H7+H8 hacking combined\nisr_hack_rates = np.array([(isr_data[s][1] + isr_data[s][3]) / isr_data[s][0] for s in seeds])\nrand_hack_rates = np.array([(random_data[s][1] + random_data[s][3]) / random_data[s][0] for s in seeds])\n\nobs_diff_hack = np.mean(isr_hack_rates) - np.mean(rand_hack_rates)\ncombined_hack = np.concatenate([isr_hack_rates, rand_hack_rates])\n\ncount_hack = 0\nfor _ in range(n_perm):\n    perm = np.random.permutation(combined_hack)\n    perm_diff = np.mean(perm[:5]) - np.mean(perm[5:])\n    if abs(perm_diff) >= abs(obs_diff_hack):\n        count_hack += 1\n\nperm_p_hack = count_hack / n_perm\n\nprint(f\"\\n--- H7+H8 Combined Hacking Rate Permutation Test ---\")\nprint(f\"  ISR (H7+H8)/proved per seed:    {[f'{r:.4f}' for r in isr_hack_rates]}\")\nprint(f\"  Random (H7+H8)/proved per seed: {[f'{r:.4f}' for r in rand_hack_rates]}\")\nprint(f\"  Observed difference:            {obs_diff_hack:.4f}\")\nprint(f\"  Permutation p-value:            {perm_p_hack:.4f} (two-sided, {n_perm} perms)\")\n\n# =============================================================================\n# 2c. Wilson CI for Per-Seed Percentages\n# =============================================================================\nprint(\"\\n\" + \"=\" * 70)\nprint(\"2c. WILSON 95% CI FOR PER-SEED METRICS\")\nprint(\"=\" * 70)\n\nprint(f\"\\n{'Cond':<8} {'Seed':<5} {'Proved':<7} {'H7%':<18} {'Genuine%':<18} {'Non-hack%':<18}\")\nprint(\"-\" * 75)\n\nfor cond_name, data in [(\"ISR\", isr_data), (\"Random\", random_data)]:\n    for s in seeds:\n        proved, h7, h1, h8, genuine = data[s]\n        non_hack = genuine  # non-hacking = genuine per C013\n        \n        # H7%\n        h7_lo, h7_hi = proportion_confint(h7, proved, alpha=0.05, method='wilson')\n        # Genuine%\n        gen_lo, gen_hi = proportion_confint(genuine, proved, alpha=0.05, method='wilson')\n        # Non-hacking% (same as genuine%)\n        nh_lo, nh_hi = gen_lo, gen_hi\n        \n        h7_pct = h7 / proved * 100\n        gen_pct = genuine / proved * 100\n        \n        print(f\"{cond_name:<8} {s:<5} {proved:<7} \"\n              f\"{h7_pct:5.1f} [{h7_lo*100:4.1f},{h7_hi*100:4.1f}]  \"\n              f\"{gen_pct:5.1f} [{gen_lo*100:4.1f},{gen_hi*100:4.1f}]  \"\n              f\"{gen_pct:5.1f} [{nh_lo*100:4.1f},{nh_hi*100:4.1f}]\")\n    print()\n\n# =============================================================================\n# 2d. 5-Seed Pooled Summary\n# =============================================================================\nprint(\"=\" * 70)\nprint(\"2d. 5-SEED POOLED SUMMARY + FISHER EXACT TEST\")\nprint(\"=\" * 70)\n\nisr_proved_total = sum(isr_data[s][0] for s in seeds)\nisr_h7_total = sum(isr_data[s][1] for s in seeds)\nisr_gen_total = sum(isr_data[s][4] for s in seeds)\nisr_h8_total = sum(isr_data[s][3] for s in seeds)\nisr_h1_total = sum(isr_data[s][2] for s in seeds)\n\nrand_proved_total = sum(random_data[s][0] for s in seeds)\nrand_h7_total = sum(random_data[s][1] for s in seeds)\nrand_gen_total = sum(random_data[s][4] for s in seeds)\nrand_h8_total = sum(random_data[s][3] for s in seeds)\nrand_h1_total = sum(random_data[s][2] for s in seeds)\n\nprint(f\"\\n  {'Metric':<20} {'ISR β=0.1':<20} {'Random β=0.1':<20}\")\nprint(f\"  {'-'*60}\")\nprint(f\"  {'Proved (total)':<20} {isr_proved_total:<20} {rand_proved_total:<20}\")\nprint(f\"  {'H7 (total)':<20} {isr_h7_total:<20} {rand_h7_total:<20}\")\nprint(f\"  {'H1 (total)':<20} {isr_h1_total:<20} {rand_h1_total:<20}\")\nprint(f\"  {'H8 (total)':<20} {isr_h8_total:<20} {rand_h8_total:<20}\")\nprint(f\"  {'Genuine (total)':<20} {isr_gen_total:<20} {rand_gen_total:<20}\")\nprint(f\"  {'H7 rate':<20} {isr_h7_total/isr_proved_total:.4f} ({isr_h7_total}/{isr_proved_total}){'':<5} {rand_h7_total/rand_proved_total:.4f} ({rand_h7_total}/{rand_proved_total})\")\nprint(f\"  {'Genuine rate':<20} {isr_gen_total/isr_proved_total:.4f} ({isr_gen_total}/{isr_proved_total}){'':<5} {rand_gen_total/rand_proved_total:.4f} ({rand_gen_total}/{rand_proved_total})\")\n\n# Pooled Fisher: H7\ntable_h7_pooled = np.array([[isr_h7_total, isr_proved_total - isr_h7_total],\n                            [rand_h7_total, rand_proved_total - rand_h7_total]])\nor_h7, p_h7 = stats.fisher_exact(table_h7_pooled)\nprint(f\"\\n  --- Pooled Fisher Exact: H7 ---\")\nprint(f\"  OR = {or_h7:.4f}, p = {p_h7:.6e}\")\n\n# Pooled Fisher: Genuine\ntable_gen_pooled = np.array([[isr_gen_total, isr_proved_total - isr_gen_total],\n                             [rand_gen_total, rand_proved_total - rand_gen_total]])\nor_gen, p_gen = stats.fisher_exact(table_gen_pooled)\nprint(f\"\\n  --- Pooled Fisher Exact: Genuine ---\")\nprint(f\"  OR = {or_gen:.4f}, p = {p_gen:.6e}\")\n\n# Wilson CI for pooled rates\nisr_gen_lo, isr_gen_hi = proportion_confint(isr_gen_total, isr_proved_total, alpha=0.05, method='wilson')\nrand_gen_lo, rand_gen_hi = proportion_confint(rand_gen_total, rand_proved_total, alpha=0.05, method='wilson')\nprint(f\"\\n  --- Pooled Wilson 95% CI ---\")\nprint(f\"  ISR genuine rate:    {isr_gen_total/isr_proved_total:.4f} [{isr_gen_lo:.4f}, {isr_gen_hi:.4f}]\")\nprint(f\"  Random genuine rate: {rand_gen_total/rand_proved_total:.4f} [{rand_gen_lo:.4f}, {rand_gen_hi:.4f}]\")\n\n# =============================================================================\n# SUMMARY\n# =============================================================================\nprint(\"\\n\" + \"=\" * 70)\nprint(\"SUMMARY TABLE\")\nprint(\"=\" * 70)\n\nprint(f\"\\n  {'Test':<40} {'Statistic':<15} {'p-value':<15} {'Significant?'}\")\nprint(f\"  {'-'*80}\")\nprint(f\"  {'CMH: H7 rate':<40} {'OR='+f'{st_h7.common_odds_ratio:.3f}':<15} {cmh_h7.pvalue:<15.4e} {'Yes' if cmh_h7.pvalue < 0.05 else 'No'}\")\nprint(f\"  {'CMH: Genuine rate':<40} {'OR='+f'{st_gen.common_odds_ratio:.3f}':<15} {cmh_gen.pvalue:<15.4e} {'Yes' if cmh_gen.pvalue < 0.05 else 'No'}\")\nprint(f\"  {'Permutation: H7 rate diff':<40} {'Δ='+f'{obs_diff_h7:.4f}':<15} {perm_p_h7:<15.4f} {'Yes' if perm_p_h7 < 0.05 else 'No'}\")\nprint(f\"  {'Permutation: Genuine rate diff':<40} {'Δ='+f'{obs_diff_gen:.4f}':<15} {perm_p_gen:<15.4f} {'Yes' if perm_p_gen < 0.05 else 'No'}\")\nprint(f\"  {'Permutation: H7+H8 hacking diff':<40} {'Δ='+f'{obs_diff_hack:.4f}':<15} {perm_p_hack:<15.4f} {'Yes' if perm_p_hack < 0.05 else 'No'}\")\nprint(f\"  {'Pooled Fisher: H7':<40} {'OR='+f'{or_h7:.3f}':<15} {p_h7:<15.4e} {'Yes' if p_h7 < 0.05 else 'No'}\")\nprint(f\"  {'Pooled Fisher: Genuine':<40} {'OR='+f'{or_gen:.3f}':<15} {p_gen:<15.4e} {'Yes' if p_gen < 0.05 else 'No'}\")\n\nprint(\"\\n\\nNote: With only 5 seeds per group, permutation tests have limited resolution\")\nprint(\"(minimum possible p-value = 2/C(10,5) = 2/252 ≈ 0.008 for exact permutation).\")\nprint(\"CMH accounts for seed-level clustering in a sample-level framework.\")\nSCRIPT",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-17T11:55:39.213247+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.16}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-17T11:55:39.213373+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-39279",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python analysis/seed_level_stats.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-39279",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python analysis/seed_level_stats.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-17T11:55:39.213512+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python analysis/seed_level_stats.py'\\n\\nExit code: 1\\n\\nStdout:\\n\\n======================================================================\\nSEED-LEVEL STATISTICAL ANALYSIS: ISR β=0.1 vs Random β=0.1\\n======================================================================\\n\\n======================================================================\\n2a. COCHRAN-MANTEL-HAENSZEL (CMH) TEST\\n======================================================================\\n\\n--- H7 Rate: ISR vs Random (stratified by seed) ---\\n\\nStderr:\\n\\nTraceback (most recent call last):\\n  File \\\"/root/solver-trace-ablation/analysis/seed_level_stats.py\\\", line 60, in &lt;module>\\n    print(f\\\"  Common OR:  {st_h7.common_odds_ratio:.4f}\\\")\\n                           ^^^^^^^^^^^^^^^^^^^^^^^\\nAttributeError: 'StratifiedTable' object has no attribute 'common_odds_ratio'\\n\\n\", \"metadata\": {\"elapsed_seconds\": 4.58}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-17T11:55:39.213656+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-39279",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"from statsmodels.stats.contingency_tables import StratifiedTable; import numpy as np; t = StratifiedTable([np.array([[10,20],[5,25]])]); print(dir(t))\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-39279",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"from statsmodels.stats.contingency_tables import StratifiedTable; import numpy as np; t = StratifiedTable([np.array([[10,20],[5,25]])]); print(dir(t))\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-17T11:55:39.213807+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_ad', '_apb', '_apc', '_apd', '_bc', '_bpd', '_cache', '_cpd', '_dma', '_n', 'from_data', 'logodds_pooled', 'logodds_pooled_confint', 'logodds_pooled_se', 'oddsratio_pooled', 'oddsratio_pooled_confint', 'riskratio_pooled', 'summary', 'table', 'test_equal_odds', 'test_null_odds']\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.02}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-17T11:55:39.213929+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-39279",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"\nfrom statsmodels.stats.contingency_tables import StratifiedTable\nimport numpy as np\nt = StratifiedTable([np.array([[10,20],[5,25]])])\nprint('oddsratio_pooled:', t.oddsratio_pooled)\nprint('oddsratio_pooled_confint:', t.oddsratio_pooled_confint())\nr = t.test_null_odds()\nprint('test_null_odds:', r.statistic, r.pvalue)\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-39279",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"\nfrom statsmodels.stats.contingency_tables import StratifiedTable\nimport numpy as np\nt = StratifiedTable([np.array([[10,20],[5,25]])])\nprint('oddsratio_pooled:', t.oddsratio_pooled)\nprint('oddsratio_pooled_confint:', t.oddsratio_pooled_confint())\nr = t.test_null_odds()\nprint('test_null_odds:', r.statistic, r.pvalue)\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-17T11:55:39.214056+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"oddsratio_pooled: 2.5\\noddsratio_pooled_confint: (np.float64(0.735131132465979), np.float64(8.50188452641712))\\ntest_null_odds: 2.185185185185185 0.13934430324163394\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.18}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-17T11:55:39.214217+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-39279",
  "command": "cat > /root/solver-trace-ablation/analysis/seed_level_stats.py << 'SCRIPT'\n\"\"\"\nSeed-Level Statistical Analysis: ISR beta=0.1 vs Random beta=0.1 (5-seed)\nCluster-aware statistics addressing pooled Fisher test limitations.\n\"\"\"\nimport numpy as np\nfrom scipy import stats\nfrom statsmodels.stats.contingency_tables import StratifiedTable\nfrom statsmodels.stats.proportion import proportion_confint\n\n# =============================================================================\n# DATA (C013 taxonomy: genuine = proved - H7 - H1 - H8)\n# =============================================================================\n\nisr_data = {\n    # seed: (proved, H7, H1, H8, genuine)\n    42: (81, 13, 42, 12, 14),\n    43: (61, 59,  0,  0,  2),\n    44: (89, 89,  0,  0,  0),\n    45: (42, 16,  2,  1, 23),\n    46: (77, 11, 20,  4, 42),\n}\n\nrandom_data = {\n    # seed: (proved, H7, H1, H8, genuine)\n    42: (79,  0, 58,  4, 18),\n    43: (94, 36, 56,  1,  1),\n    44: (89,  0, 73, 16,  6),\n    45: (58,  0, 53,  0,  5),\n    46: (94, 86,  2,  4,  2),\n}\n\nseeds = [42, 43, 44, 45, 46]\n\nprint(\"=\" * 70)\nprint(\"SEED-LEVEL STATISTICAL ANALYSIS: ISR beta=0.1 vs Random beta=0.1\")\nprint(\"=\" * 70)\n\n# =============================================================================\n# 2a. CMH Test (Cochran-Mantel-Haenszel)\n# =============================================================================\nprint(\"\\n\" + \"=\" * 70)\nprint(\"2a. COCHRAN-MANTEL-HAENSZEL (CMH) TEST\")\nprint(\"=\" * 70)\n\n# --- H7 rate comparison ---\ntables_h7 = []\nfor s in seeds:\n    ip, ih7, _, _, _ = isr_data[s]\n    rp, rh7, _, _, _ = random_data[s]\n    table = np.array([[ih7, ip - ih7],\n                      [rh7, rp - rh7]])\n    tables_h7.append(table)\n\nst_h7 = StratifiedTable(tables_h7)\ncmh_h7 = st_h7.test_null_odds()\nci_h7 = st_h7.oddsratio_pooled_confint()\nprint(f\"\\n--- H7 Rate: ISR vs Random (stratified by seed) ---\")\nprint(f\"  Pooled OR:  {st_h7.oddsratio_pooled:.4f}\")\nprint(f\"  95% CI:     [{ci_h7[0]:.4f}, {ci_h7[1]:.4f}]\")\nprint(f\"  CMH chi2:   {cmh_h7.statistic:.4f}\")\nprint(f\"  p-value:    {cmh_h7.pvalue:.6e}\")\n\n# --- Genuine rate comparison ---\ntables_gen = []\nfor s in seeds:\n    ip, _, _, _, ig = isr_data[s]\n    rp, _, _, _, rg = random_data[s]\n    table = np.array([[ig, ip - ig],\n                      [rg, rp - rg]])\n    tables_gen.append(table)\n\nst_gen = StratifiedTable(tables_gen)\ncmh_gen = st_gen.test_null_odds()\nci_gen = st_gen.oddsratio_pooled_confint()\nprint(f\"\\n--- Genuine Rate: ISR vs Random (stratified by seed) ---\")\nprint(f\"  Pooled OR:  {st_gen.oddsratio_pooled:.4f}\")\nprint(f\"  95% CI:     [{ci_gen[0]:.4f}, {ci_gen[1]:.4f}]\")\nprint(f\"  CMH chi2:   {cmh_gen.statistic:.4f}\")\nprint(f\"  p-value:    {cmh_gen.pvalue:.6e}\")\n\n# =============================================================================\n# 2b. Permutation Test\n# =============================================================================\nprint(\"\\n\" + \"=\" * 70)\nprint(\"2b. PERMUTATION TEST (seed-level rates as units)\")\nprint(\"=\" * 70)\n\nnp.random.seed(2024)\nn_perm = 10000\n\n# H7 rates per seed\nisr_h7_rates = np.array([isr_data[s][1] / isr_data[s][0] for s in seeds])\nrand_h7_rates = np.array([random_data[s][1] / random_data[s][0] for s in seeds])\n\nobs_diff_h7 = np.mean(isr_h7_rates) - np.mean(rand_h7_rates)\ncombined_h7 = np.concatenate([isr_h7_rates, rand_h7_rates])\n\ncount_h7 = 0\nfor _ in range(n_perm):\n    perm = np.random.permutation(combined_h7)\n    perm_diff = np.mean(perm[:5]) - np.mean(perm[5:])\n    if abs(perm_diff) >= abs(obs_diff_h7):\n        count_h7 += 1\n\nperm_p_h7 = count_h7 / n_perm\n\nprint(f\"\\n--- H7 Rate Permutation Test ---\")\nprint(f\"  ISR H7 rates per seed:    {[f'{r:.4f}' for r in isr_h7_rates]}\")\nprint(f\"  Random H7 rates per seed: {[f'{r:.4f}' for r in rand_h7_rates]}\")\nprint(f\"  ISR mean H7 rate:         {np.mean(isr_h7_rates):.4f}\")\nprint(f\"  Random mean H7 rate:      {np.mean(rand_h7_rates):.4f}\")\nprint(f\"  Observed difference:      {obs_diff_h7:+.4f}\")\nprint(f\"  Permutation p-value:      {perm_p_h7:.4f} (two-sided, {n_perm} perms)\")\n\n# Genuine rates per seed\nisr_gen_rates = np.array([isr_data[s][4] / isr_data[s][0] for s in seeds])\nrand_gen_rates = np.array([random_data[s][4] / random_data[s][0] for s in seeds])\n\nobs_diff_gen = np.mean(isr_gen_rates) - np.mean(rand_gen_rates)\ncombined_gen = np.concatenate([isr_gen_rates, rand_gen_rates])\n\ncount_gen = 0\nfor _ in range(n_perm):\n    perm = np.random.permutation(combined_gen)\n    perm_diff = np.mean(perm[:5]) - np.mean(perm[5:])\n    if abs(perm_diff) >= abs(obs_diff_gen):\n        count_gen += 1\n\nperm_p_gen = count_gen / n_perm\n\nprint(f\"\\n--- Genuine Rate Permutation Test ---\")\nprint(f\"  ISR genuine rates per seed:    {[f'{r:.4f}' for r in isr_gen_rates]}\")\nprint(f\"  Random genuine rates per seed: {[f'{r:.4f}' for r in rand_gen_rates]}\")\nprint(f\"  ISR mean genuine rate:         {np.mean(isr_gen_rates):.4f}\")\nprint(f\"  Random mean genuine rate:      {np.mean(rand_gen_rates):.4f}\")\nprint(f\"  Observed difference:           {obs_diff_gen:+.4f}\")\nprint(f\"  Permutation p-value:           {perm_p_gen:.4f} (two-sided, {n_perm} perms)\")\n\n# H7+H8 combined hacking\nisr_hack_rates = np.array([(isr_data[s][1] + isr_data[s][3]) / isr_data[s][0] for s in seeds])\nrand_hack_rates = np.array([(random_data[s][1] + random_data[s][3]) / random_data[s][0] for s in seeds])\n\nobs_diff_hack = np.mean(isr_hack_rates) - np.mean(rand_hack_rates)\ncombined_hack = np.concatenate([isr_hack_rates, rand_hack_rates])\n\ncount_hack = 0\nfor _ in range(n_perm):\n    perm = np.random.permutation(combined_hack)\n    perm_diff = np.mean(perm[:5]) - np.mean(perm[5:])\n    if abs(perm_diff) >= abs(obs_diff_hack):\n        count_hack += 1\n\nperm_p_hack = count_hack / n_perm\n\nprint(f\"\\n--- H7+H8 Combined Hacking Rate Permutation Test ---\")\nprint(f\"  ISR (H7+H8)/proved per seed:    {[f'{r:.4f}' for r in isr_hack_rates]}\")\nprint(f\"  Random (H7+H8)/proved per seed: {[f'{r:.4f}' for r in rand_hack_rates]}\")\nprint(f\"  ISR mean (H7+H8) rate:          {np.mean(isr_hack_rates):.4f}\")\nprint(f\"  Random mean (H7+H8) rate:       {np.mean(rand_hack_rates):.4f}\")\nprint(f\"  Observed difference:            {obs_diff_hack:+.4f}\")\nprint(f\"  Permutation p-value:            {perm_p_hack:.4f} (two-sided, {n_perm} perms)\")\n\n# =============================================================================\n# 2c. Wilson CI for Per-Seed Percentages\n# =============================================================================\nprint(\"\\n\" + \"=\" * 70)\nprint(\"2c. WILSON 95% CI FOR PER-SEED METRICS\")\nprint(\"=\" * 70)\n\nprint(f\"\\n{'Cond':<8} {'Seed':<5} {'n':<4} {'H7%':<22} {'Genuine%':<22}\")\nprint(\"-\" * 65)\n\nfor cond_name, data in [(\"ISR\", isr_data), (\"Random\", random_data)]:\n    for s in seeds:\n        proved, h7, h1, h8, genuine = data[s]\n        \n        h7_lo, h7_hi = proportion_confint(h7, proved, alpha=0.05, method='wilson')\n        gen_lo, gen_hi = proportion_confint(genuine, proved, alpha=0.05, method='wilson')\n        \n        h7_pct = h7 / proved * 100\n        gen_pct = genuine / proved * 100\n        \n        print(f\"{cond_name:<8} {s:<5} {proved:<4} \"\n              f\"{h7_pct:5.1f}% [{h7_lo*100:5.1f},{h7_hi*100:5.1f}]  \"\n              f\"{gen_pct:5.1f}% [{gen_lo*100:5.1f},{gen_hi*100:5.1f}]\")\n    print()\n\n# =============================================================================\n# 2d. 5-Seed Pooled Summary\n# =============================================================================\nprint(\"=\" * 70)\nprint(\"2d. 5-SEED POOLED SUMMARY + FISHER EXACT TEST\")\nprint(\"=\" * 70)\n\nisr_proved_total = sum(isr_data[s][0] for s in seeds)\nisr_h7_total = sum(isr_data[s][1] for s in seeds)\nisr_gen_total = sum(isr_data[s][4] for s in seeds)\nisr_h8_total = sum(isr_data[s][3] for s in seeds)\nisr_h1_total = sum(isr_data[s][2] for s in seeds)\n\nrand_proved_total = sum(random_data[s][0] for s in seeds)\nrand_h7_total = sum(random_data[s][1] for s in seeds)\nrand_gen_total = sum(random_data[s][4] for s in seeds)\nrand_h8_total = sum(random_data[s][3] for s in seeds)\nrand_h1_total = sum(random_data[s][2] for s in seeds)\n\nprint(f\"\\n  {'Metric':<20} {'ISR beta=0.1':<20} {'Random beta=0.1':<20}\")\nprint(f\"  {'-'*58}\")\nprint(f\"  {'Proved (total)':<20} {isr_proved_total:<20} {rand_proved_total:<20}\")\nprint(f\"  {'H7 (total)':<20} {isr_h7_total:<20} {rand_h7_total:<20}\")\nprint(f\"  {'H1 (total)':<20} {isr_h1_total:<20} {rand_h1_total:<20}\")\nprint(f\"  {'H8 (total)':<20} {isr_h8_total:<20} {rand_h8_total:<20}\")\nprint(f\"  {'Genuine (total)':<20} {isr_gen_total:<20} {rand_gen_total:<20}\")\nprint(f\"  {'H7 rate':<20} {isr_h7_total/isr_proved_total:.4f} ({isr_h7_total}/{isr_proved_total}){'':<3} {rand_h7_total/rand_proved_total:.4f} ({rand_h7_total}/{rand_proved_total})\")\nprint(f\"  {'Genuine rate':<20} {isr_gen_total/isr_proved_total:.4f} ({isr_gen_total}/{isr_proved_total}){'':<3} {rand_gen_total/rand_proved_total:.4f} ({rand_gen_total}/{rand_proved_total})\")\n\n# Pooled Fisher: H7\ntable_h7_pooled = np.array([[isr_h7_total, isr_proved_total - isr_h7_total],\n                            [rand_h7_total, rand_proved_total - rand_h7_total]])\nor_h7, p_h7 = stats.fisher_exact(table_h7_pooled)\nprint(f\"\\n  --- Pooled Fisher Exact: H7 ---\")\nprint(f\"  OR = {or_h7:.4f}, p = {p_h7:.6e}\")\n\n# Pooled Fisher: Genuine\ntable_gen_pooled = np.array([[isr_gen_total, isr_proved_total - isr_gen_total],\n                             [rand_gen_total, rand_proved_total - rand_gen_total]])\nor_gen, p_gen = stats.fisher_exact(table_gen_pooled)\nprint(f\"\\n  --- Pooled Fisher Exact: Genuine ---\")\nprint(f\"  OR = {or_gen:.4f}, p = {p_gen:.6e}\")\n\n# Wilson CI for pooled rates\nisr_gen_lo, isr_gen_hi = proportion_confint(isr_gen_total, isr_proved_total, alpha=0.05, method='wilson')\nrand_gen_lo, rand_gen_hi = proportion_confint(rand_gen_total, rand_proved_total, alpha=0.05, method='wilson')\nisr_h7_lo, isr_h7_hi = proportion_confint(isr_h7_total, isr_proved_total, alpha=0.05, method='wilson')\nrand_h7_lo, rand_h7_hi = proportion_confint(rand_h7_total, rand_proved_total, alpha=0.05, method='wilson')\nprint(f\"\\n  --- Pooled Wilson 95% CI ---\")\nprint(f\"  ISR H7 rate:       {isr_h7_total/isr_proved_total:.4f} [{isr_h7_lo:.4f}, {isr_h7_hi:.4f}]\")\nprint(f\"  Random H7 rate:    {rand_h7_total/rand_proved_total:.4f} [{rand_h7_lo:.4f}, {rand_h7_hi:.4f}]\")\nprint(f\"  ISR genuine rate:  {isr_gen_total/isr_proved_total:.4f} [{isr_gen_lo:.4f}, {isr_gen_hi:.4f}]\")\nprint(f\"  Random genuine:    {rand_gen_total/rand_proved_total:.4f} [{rand_gen_lo:.4f}, {rand_gen_hi:.4f}]\")\n\n# =============================================================================\n# SUMMARY\n# =============================================================================\nprint(\"\\n\" + \"=\" * 70)\nprint(\"SUMMARY TABLE\")\nprint(\"=\" * 70)\n\nprint(f\"\\n  {'Test':<42} {'Stat':<15} {'p-value':<12} {'Sig?'}\")\nprint(f\"  {'-'*75}\")\nprint(f\"  {'CMH: H7 (seed-stratified)':<42} {'OR='+f'{st_h7.oddsratio_pooled:.3f}':<15} {cmh_h7.pvalue:<12.4e} {'Yes' if cmh_h7.pvalue < 0.05 else 'No'}\")\nprint(f\"  {'CMH: Genuine (seed-stratified)':<42} {'OR='+f'{st_gen.oddsratio_pooled:.3f}':<15} {cmh_gen.pvalue:<12.4e} {'Yes' if cmh_gen.pvalue < 0.05 else 'No'}\")\nprint(f\"  {'Permutation: H7 rate (n=5 per group)':<42} {'d='+f'{obs_diff_h7:+.4f}':<15} {perm_p_h7:<12.4f} {'Yes' if perm_p_h7 < 0.05 else 'No'}\")\nprint(f\"  {'Permutation: Genuine rate':<42} {'d='+f'{obs_diff_gen:+.4f}':<15} {perm_p_gen:<12.4f} {'Yes' if perm_p_gen < 0.05 else 'No'}\")\nprint(f\"  {'Permutation: H7+H8 hacking rate':<42} {'d='+f'{obs_diff_hack:+.4f}':<15} {perm_p_hack:<12.4f} {'Yes' if perm_p_hack < 0.05 else 'No'}\")\nprint(f\"  {'Pooled Fisher: H7 (ignores clustering)':<42} {'OR='+f'{or_h7:.3f}':<15} {p_h7:<12.4e} {'Yes' if p_h7 < 0.05 else 'No'}\")\nprint(f\"  {'Pooled Fisher: Genuine (ignores clustering)':<42} {'OR='+f'{or_gen:.3f}':<15} {p_gen:<12.4e} {'Yes' if p_gen < 0.05 else 'No'}\")\n\nprint(\"\\n\\nNote: With only 5 seeds per group, permutation tests have limited resolution\")\nprint(\"(minimum achievable two-sided p = 2/C(10,5) = 2/252 = 0.0079).\")\nprint(\"CMH properly accounts for seed-level clustering in sample-level comparisons.\")\nprint(\"Pooled Fisher included for reference but ignores within-seed correlation.\")\nSCRIPT",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-39279",
    "command": "cat > /root/solver-trace-ablation/analysis/seed_level_stats.py << 'SCRIPT'\n\"\"\"\nSeed-Level Statistical Analysis: ISR beta=0.1 vs Random beta=0.1 (5-seed)\nCluster-aware statistics addressing pooled Fisher test limitations.\n\"\"\"\nimport numpy as np\nfrom scipy import stats\nfrom statsmodels.stats.contingency_tables import StratifiedTable\nfrom statsmodels.stats.proportion import proportion_confint\n\n# =============================================================================\n# DATA (C013 taxonomy: genuine = proved - H7 - H1 - H8)\n# =============================================================================\n\nisr_data = {\n    # seed: (proved, H7, H1, H8, genuine)\n    42: (81, 13, 42, 12, 14),\n    43: (61, 59,  0,  0,  2),\n    44: (89, 89,  0,  0,  0),\n    45: (42, 16,  2,  1, 23),\n    46: (77, 11, 20,  4, 42),\n}\n\nrandom_data = {\n    # seed: (proved, H7, H1, H8, genuine)\n    42: (79,  0, 58,  4, 18),\n    43: (94, 36, 56,  1,  1),\n    44: (89,  0, 73, 16,  6),\n    45: (58,  0, 53,  0,  5),\n    46: (94, 86,  2,  4,  2),\n}\n\nseeds = [42, 43, 44, 45, 46]\n\nprint(\"=\" * 70)\nprint(\"SEED-LEVEL STATISTICAL ANALYSIS: ISR beta=0.1 vs Random beta=0.1\")\nprint(\"=\" * 70)\n\n# =============================================================================\n# 2a. CMH Test (Cochran-Mantel-Haenszel)\n# =============================================================================\nprint(\"\\n\" + \"=\" * 70)\nprint(\"2a. COCHRAN-MANTEL-HAENSZEL (CMH) TEST\")\nprint(\"=\" * 70)\n\n# --- H7 rate comparison ---\ntables_h7 = []\nfor s in seeds:\n    ip, ih7, _, _, _ = isr_data[s]\n    rp, rh7, _, _, _ = random_data[s]\n    table = np.array([[ih7, ip - ih7],\n                      [rh7, rp - rh7]])\n    tables_h7.append(table)\n\nst_h7 = StratifiedTable(tables_h7)\ncmh_h7 = st_h7.test_null_odds()\nci_h7 = st_h7.oddsratio_pooled_confint()\nprint(f\"\\n--- H7 Rate: ISR vs Random (stratified by seed) ---\")\nprint(f\"  Pooled OR:  {st_h7.oddsratio_pooled:.4f}\")\nprint(f\"  95% CI:     [{ci_h7[0]:.4f}, {ci_h7[1]:.4f}]\")\nprint(f\"  CMH chi2:   {cmh_h7.statistic:.4f}\")\nprint(f\"  p-value:    {cmh_h7.pvalue:.6e}\")\n\n# --- Genuine rate comparison ---\ntables_gen = []\nfor s in seeds:\n    ip, _, _, _, ig = isr_data[s]\n    rp, _, _, _, rg = random_data[s]\n    table = np.array([[ig, ip - ig],\n                      [rg, rp - rg]])\n    tables_gen.append(table)\n\nst_gen = StratifiedTable(tables_gen)\ncmh_gen = st_gen.test_null_odds()\nci_gen = st_gen.oddsratio_pooled_confint()\nprint(f\"\\n--- Genuine Rate: ISR vs Random (stratified by seed) ---\")\nprint(f\"  Pooled OR:  {st_gen.oddsratio_pooled:.4f}\")\nprint(f\"  95% CI:     [{ci_gen[0]:.4f}, {ci_gen[1]:.4f}]\")\nprint(f\"  CMH chi2:   {cmh_gen.statistic:.4f}\")\nprint(f\"  p-value:    {cmh_gen.pvalue:.6e}\")\n\n# =============================================================================\n# 2b. Permutation Test\n# =============================================================================\nprint(\"\\n\" + \"=\" * 70)\nprint(\"2b. PERMUTATION TEST (seed-level rates as units)\")\nprint(\"=\" * 70)\n\nnp.random.seed(2024)\nn_perm = 10000\n\n# H7 rates per seed\nisr_h7_rates = np.array([isr_data[s][1] / isr_data[s][0] for s in seeds])\nrand_h7_rates = np.array([random_data[s][1] / random_data[s][0] for s in seeds])\n\nobs_diff_h7 = np.mean(isr_h7_rates) - np.mean(rand_h7_rates)\ncombined_h7 = np.concatenate([isr_h7_rates, rand_h7_rates])\n\ncount_h7 = 0\nfor _ in range(n_perm):\n    perm = np.random.permutation(combined_h7)\n    perm_diff = np.mean(perm[:5]) - np.mean(perm[5:])\n    if abs(perm_diff) >= abs(obs_diff_h7):\n        count_h7 += 1\n\nperm_p_h7 = count_h7 / n_perm\n\nprint(f\"\\n--- H7 Rate Permutation Test ---\")\nprint(f\"  ISR H7 rates per seed:    {[f'{r:.4f}' for r in isr_h7_rates]}\")\nprint(f\"  Random H7 rates per seed: {[f'{r:.4f}' for r in rand_h7_rates]}\")\nprint(f\"  ISR mean H7 rate:         {np.mean(isr_h7_rates):.4f}\")\nprint(f\"  Random mean H7 rate:      {np.mean(rand_h7_rates):.4f}\")\nprint(f\"  Observed difference:      {obs_diff_h7:+.4f}\")\nprint(f\"  Permutation p-value:      {perm_p_h7:.4f} (two-sided, {n_perm} perms)\")\n\n# Genuine rates per seed\nisr_gen_rates = np.array([isr_data[s][4] / isr_data[s][0] for s in seeds])\nrand_gen_rates = np.array([random_data[s][4] / random_data[s][0] for s in seeds])\n\nobs_diff_gen = np.mean(isr_gen_rates) - np.mean(rand_gen_rates)\ncombined_gen = np.concatenate([isr_gen_rates, rand_gen_rates])\n\ncount_gen = 0\nfor _ in range(n_perm):\n    perm = np.random.permutation(combined_gen)\n    perm_diff = np.mean(perm[:5]) - np.mean(perm[5:])\n    if abs(perm_diff) >= abs(obs_diff_gen):\n        count_gen += 1\n\nperm_p_gen = count_gen / n_perm\n\nprint(f\"\\n--- Genuine Rate Permutation Test ---\")\nprint(f\"  ISR genuine rates per seed:    {[f'{r:.4f}' for r in isr_gen_rates]}\")\nprint(f\"  Random genuine rates per seed: {[f'{r:.4f}' for r in rand_gen_rates]}\")\nprint(f\"  ISR mean genuine rate:         {np.mean(isr_gen_rates):.4f}\")\nprint(f\"  Random mean genuine rate:      {np.mean(rand_gen_rates):.4f}\")\nprint(f\"  Observed difference:           {obs_diff_gen:+.4f}\")\nprint(f\"  Permutation p-value:           {perm_p_gen:.4f} (two-sided, {n_perm} perms)\")\n\n# H7+H8 combined hacking\nisr_hack_rates = np.array([(isr_data[s][1] + isr_data[s][3]) / isr_data[s][0] for s in seeds])\nrand_hack_rates = np.array([(random_data[s][1] + random_data[s][3]) / random_data[s][0] for s in seeds])\n\nobs_diff_hack = np.mean(isr_hack_rates) - np.mean(rand_hack_rates)\ncombined_hack = np.concatenate([isr_hack_rates, rand_hack_rates])\n\ncount_hack = 0\nfor _ in range(n_perm):\n    perm = np.random.permutation(combined_hack)\n    perm_diff = np.mean(perm[:5]) - np.mean(perm[5:])\n    if abs(perm_diff) >= abs(obs_diff_hack):\n        count_hack += 1\n\nperm_p_hack = count_hack / n_perm\n\nprint(f\"\\n--- H7+H8 Combined Hacking Rate Permutation Test ---\")\nprint(f\"  ISR (H7+H8)/proved per seed:    {[f'{r:.4f}' for r in isr_hack_rates]}\")\nprint(f\"  Random (H7+H8)/proved per seed: {[f'{r:.4f}' for r in rand_hack_rates]}\")\nprint(f\"  ISR mean (H7+H8) rate:          {np.mean(isr_hack_rates):.4f}\")\nprint(f\"  Random mean (H7+H8) rate:       {np.mean(rand_hack_rates):.4f}\")\nprint(f\"  Observed difference:            {obs_diff_hack:+.4f}\")\nprint(f\"  Permutation p-value:            {perm_p_hack:.4f} (two-sided, {n_perm} perms)\")\n\n# =============================================================================\n# 2c. Wilson CI for Per-Seed Percentages\n# =============================================================================\nprint(\"\\n\" + \"=\" * 70)\nprint(\"2c. WILSON 95% CI FOR PER-SEED METRICS\")\nprint(\"=\" * 70)\n\nprint(f\"\\n{'Cond':<8} {'Seed':<5} {'n':<4} {'H7%':<22} {'Genuine%':<22}\")\nprint(\"-\" * 65)\n\nfor cond_name, data in [(\"ISR\", isr_data), (\"Random\", random_data)]:\n    for s in seeds:\n        proved, h7, h1, h8, genuine = data[s]\n        \n        h7_lo, h7_hi = proportion_confint(h7, proved, alpha=0.05, method='wilson')\n        gen_lo, gen_hi = proportion_confint(genuine, proved, alpha=0.05, method='wilson')\n        \n        h7_pct = h7 / proved * 100\n        gen_pct = genuine / proved * 100\n        \n        print(f\"{cond_name:<8} {s:<5} {proved:<4} \"\n              f\"{h7_pct:5.1f}% [{h7_lo*100:5.1f},{h7_hi*100:5.1f}]  \"\n              f\"{gen_pct:5.1f}% [{gen_lo*100:5.1f},{gen_hi*100:5.1f}]\")\n    print()\n\n# =============================================================================\n# 2d. 5-Seed Pooled Summary\n# =============================================================================\nprint(\"=\" * 70)\nprint(\"2d. 5-SEED POOLED SUMMARY + FISHER EXACT TEST\")\nprint(\"=\" * 70)\n\nisr_proved_total = sum(isr_data[s][0] for s in seeds)\nisr_h7_total = sum(isr_data[s][1] for s in seeds)\nisr_gen_total = sum(isr_data[s][4] for s in seeds)\nisr_h8_total = sum(isr_data[s][3] for s in seeds)\nisr_h1_total = sum(isr_data[s][2] for s in seeds)\n\nrand_proved_total = sum(random_data[s][0] for s in seeds)\nrand_h7_total = sum(random_data[s][1] for s in seeds)\nrand_gen_total = sum(random_data[s][4] for s in seeds)\nrand_h8_total = sum(random_data[s][3] for s in seeds)\nrand_h1_total = sum(random_data[s][2] for s in seeds)\n\nprint(f\"\\n  {'Metric':<20} {'ISR beta=0.1':<20} {'Random beta=0.1':<20}\")\nprint(f\"  {'-'*58}\")\nprint(f\"  {'Proved (total)':<20} {isr_proved_total:<20} {rand_proved_total:<20}\")\nprint(f\"  {'H7 (total)':<20} {isr_h7_total:<20} {rand_h7_total:<20}\")\nprint(f\"  {'H1 (total)':<20} {isr_h1_total:<20} {rand_h1_total:<20}\")\nprint(f\"  {'H8 (total)':<20} {isr_h8_total:<20} {rand_h8_total:<20}\")\nprint(f\"  {'Genuine (total)':<20} {isr_gen_total:<20} {rand_gen_total:<20}\")\nprint(f\"  {'H7 rate':<20} {isr_h7_total/isr_proved_total:.4f} ({isr_h7_total}/{isr_proved_total}){'':<3} {rand_h7_total/rand_proved_total:.4f} ({rand_h7_total}/{rand_proved_total})\")\nprint(f\"  {'Genuine rate':<20} {isr_gen_total/isr_proved_total:.4f} ({isr_gen_total}/{isr_proved_total}){'':<3} {rand_gen_total/rand_proved_total:.4f} ({rand_gen_total}/{rand_proved_total})\")\n\n# Pooled Fisher: H7\ntable_h7_pooled = np.array([[isr_h7_total, isr_proved_total - isr_h7_total],\n                            [rand_h7_total, rand_proved_total - rand_h7_total]])\nor_h7, p_h7 = stats.fisher_exact(table_h7_pooled)\nprint(f\"\\n  --- Pooled Fisher Exact: H7 ---\")\nprint(f\"  OR = {or_h7:.4f}, p = {p_h7:.6e}\")\n\n# Pooled Fisher: Genuine\ntable_gen_pooled = np.array([[isr_gen_total, isr_proved_total - isr_gen_total],\n                             [rand_gen_total, rand_proved_total - rand_gen_total]])\nor_gen, p_gen = stats.fisher_exact(table_gen_pooled)\nprint(f\"\\n  --- Pooled Fisher Exact: Genuine ---\")\nprint(f\"  OR = {or_gen:.4f}, p = {p_gen:.6e}\")\n\n# Wilson CI for pooled rates\nisr_gen_lo, isr_gen_hi = proportion_confint(isr_gen_total, isr_proved_total, alpha=0.05, method='wilson')\nrand_gen_lo, rand_gen_hi = proportion_confint(rand_gen_total, rand_proved_total, alpha=0.05, method='wilson')\nisr_h7_lo, isr_h7_hi = proportion_confint(isr_h7_total, isr_proved_total, alpha=0.05, method='wilson')\nrand_h7_lo, rand_h7_hi = proportion_confint(rand_h7_total, rand_proved_total, alpha=0.05, method='wilson')\nprint(f\"\\n  --- Pooled Wilson 95% CI ---\")\nprint(f\"  ISR H7 rate:       {isr_h7_total/isr_proved_total:.4f} [{isr_h7_lo:.4f}, {isr_h7_hi:.4f}]\")\nprint(f\"  Random H7 rate:    {rand_h7_total/rand_proved_total:.4f} [{rand_h7_lo:.4f}, {rand_h7_hi:.4f}]\")\nprint(f\"  ISR genuine rate:  {isr_gen_total/isr_proved_total:.4f} [{isr_gen_lo:.4f}, {isr_gen_hi:.4f}]\")\nprint(f\"  Random genuine:    {rand_gen_total/rand_proved_total:.4f} [{rand_gen_lo:.4f}, {rand_gen_hi:.4f}]\")\n\n# =============================================================================\n# SUMMARY\n# =============================================================================\nprint(\"\\n\" + \"=\" * 70)\nprint(\"SUMMARY TABLE\")\nprint(\"=\" * 70)\n\nprint(f\"\\n  {'Test':<42} {'Stat':<15} {'p-value':<12} {'Sig?'}\")\nprint(f\"  {'-'*75}\")\nprint(f\"  {'CMH: H7 (seed-stratified)':<42} {'OR='+f'{st_h7.oddsratio_pooled:.3f}':<15} {cmh_h7.pvalue:<12.4e} {'Yes' if cmh_h7.pvalue < 0.05 else 'No'}\")\nprint(f\"  {'CMH: Genuine (seed-stratified)':<42} {'OR='+f'{st_gen.oddsratio_pooled:.3f}':<15} {cmh_gen.pvalue:<12.4e} {'Yes' if cmh_gen.pvalue < 0.05 else 'No'}\")\nprint(f\"  {'Permutation: H7 rate (n=5 per group)':<42} {'d='+f'{obs_diff_h7:+.4f}':<15} {perm_p_h7:<12.4f} {'Yes' if perm_p_h7 < 0.05 else 'No'}\")\nprint(f\"  {'Permutation: Genuine rate':<42} {'d='+f'{obs_diff_gen:+.4f}':<15} {perm_p_gen:<12.4f} {'Yes' if perm_p_gen < 0.05 else 'No'}\")\nprint(f\"  {'Permutation: H7+H8 hacking rate':<42} {'d='+f'{obs_diff_hack:+.4f}':<15} {perm_p_hack:<12.4f} {'Yes' if perm_p_hack < 0.05 else 'No'}\")\nprint(f\"  {'Pooled Fisher: H7 (ignores clustering)':<42} {'OR='+f'{or_h7:.3f}':<15} {p_h7:<12.4e} {'Yes' if p_h7 < 0.05 else 'No'}\")\nprint(f\"  {'Pooled Fisher: Genuine (ignores clustering)':<42} {'OR='+f'{or_gen:.3f}':<15} {p_gen:<12.4e} {'Yes' if p_gen < 0.05 else 'No'}\")\n\nprint(\"\\n\\nNote: With only 5 seeds per group, permutation tests have limited resolution\")\nprint(\"(minimum achievable two-sided p = 2/C(10,5) = 2/252 = 0.0079).\")\nprint(\"CMH properly accounts for seed-level clustering in sample-level comparisons.\")\nprint(\"Pooled Fisher included for reference but ignores within-seed correlation.\")\nSCRIPT",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-17T11:55:39.214452+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-17T11:55:39.214584+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-39279",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python analysis/seed_level_stats.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-39279",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python analysis/seed_level_stats.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-17T11:55:39.214761+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"======================================================================\\nSEED-LEVEL STATISTICAL ANALYSIS: ISR beta=0.1 vs Random beta=0.1\\n======================================================================\\n\\n======================================================================\\n2a. COCHRAN-MANTEL-HAENSZEL (CMH) TEST\\n======================================================================\\n\\n--- H7 Rate: ISR vs Random (stratified by seed) ---\\n  Pooled OR:  2.4598\\n  95% CI:     [1.8515, 3.2680]\\n  CMH chi2:   65.6276\\n  p-value:    5.551115e-16\\n\\n--- Genuine Rate: ISR vs Random (stratified by seed) ---\\n  Pooled OR:  3.3658\\n  95% CI:     [2.2102, 5.1257]\\n  CMH chi2:   38.8791\\n  p-value:    4.508908e-10\\n\\n======================================================================\\n2b. PERMUTATION TEST (seed-level rates as units)\\n======================================================================\\n\\n--- H7 Rate Permutation Test ---\\n  ISR H7 rates per seed:    ['0.1605', '0.9672', '1.0000', '0.3810', '0.1429']\\n  Random H7 rates per seed: ['0.0000', '0.3830', '0.0000', '0.0000', '0.9149']\\n  ISR mean H7 rate:         0.5303\\n  Random mean H7 rate:      0.2596\\n  Observed difference:      +0.2707\\n  Permutation p-value:      0.2810 (two-sided, 10000 perms)\\n\\n--- Genuine Rate Permutation Test ---\\n  ISR genuine rates per seed:    ['0.1728', '0.0328', '0.0000', '0.5476', '0.5455']\\n  Random genuine rates per seed: ['0.2278', '0.0106', '0.0674', '0.0862', '0.0213']\\n  ISR mean genuine rate:         0.2597\\n  Random mean genuine rate:      0.0827\\n  Observed difference:           +0.1771\\n  Permutation p-value:           0.2623 (two-sided, 10000 perms)\\n\\n--- H7+H8 Combined Hacking Rate Permutation Test ---\\n  ISR (H7+H8)/proved per seed:    ['0.3086', '0.9672', '1.0000', '0.4048', '0.1948']\\n  Random (H7+H8)/proved per seed: ['0.0506', '0.3936', '0.1798', '0.0000', '
…[truncated 3649 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_seed-level-stats_20260517T114905",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 87 · 2026-05-17T11:55:39.214983+00:00_

Script ran successfully. Here are the complete results:

---

## Results

### 2a. CMH Test (seed-stratified, sample-level)

| Comparison | Pooled OR | 95% CI | CMH chi2 | p-value |
|---|---|---|---|---|
| H7 rate | 2.460 | [1.852, 3.268] | 65.63 | 5.55e-16 |
| Genuine rate | 3.366 | [2.210, 5.126] | 38.88 | 4.51e-10 |

Both significant even after accounting for seed clustering.

### 2b. Permutation Test (seed as unit, n=5 per group)

| Comparison | ISR mean | Random mean | Δ | p-value |
|---|---|---|---|---|
| H7 rate | 0.530 | 0.260 | +0.271 | 0.281 |
| Genuine rate | 0.260 | 0.083 | +0.177 | 0.262 |
| H7+H8 hacking | 0.575 | 0.316 | +0.259 | 0.242 |

None significant at seed level (n=5 per group is underpowered; min possible p = 0.0079).

### 2c. Wilson 95% CI per seed

Key observations: ISR seeds 45/46 have 55% genuine (CI: [40-69%]), while ISR seeds 43/44 have ~0% genuine (100% H7 collapse). Massive inter-seed variance.

### 2d. Pooled 5-seed summary

| | ISR β=0.1 | Random β=0.1 |
|---|---|---|
| Proved | 350 | 414 |
| H7 | 188 (53.7%) | 122 (29.5%) |
| Genuine | 81 (23.1%) | 32 (7.7%) |
| Pooled Fisher: H7 | OR=2.778, p=1.32e-11 | |
| Pooled Fisher: Genuine | OR=3.595, p=2.78e-9 | |

### Key takeaway

CMH (sample-level, seed-stratified) confirms both effects are significant (p<1e-9). Permutation tests (seed as unit) are non-significant due to n=5 power limitation combined with extreme bimodality (collapsed vs non-collapsed seeds). This is the expected pattern: the effect is real at the sample level even accounting for clustering, but per-seed variance is too high relative to group size for seed-level tests to reach significance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_seed-level-stats_20260517T114905"
}
```

</details>

---
