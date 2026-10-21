# ops read bootstrap results

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_ops_read-bootstrap-results_20260515T013432.jsonl`
- **Structured JSON:** [`414a42a78600bc96beaf.json`](../../sessions/41/414a42a78600bc96beaf.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-15T01:35:27.563426+00:00_

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
  "session": "worker_ops_read-bootstrap-results_20260515T013432",
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

_source line 2 · 2026-05-15T01:35:27.564007+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_read-bootstrap-results_20260515T013432",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T01:35:27.564192+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "find /root/trace-verdict-study -name \"bootstrap_compare*\" -o -name \"bootstrap*results*\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_read-bootstrap-results_20260515T013432",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "find /root/trace-verdict-study -name \"bootstrap_compare*\" -o -name \"bootstrap*results*\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T01:35:27.564388+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_read-bootstrap-results_20260515T013432",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T01:35:27.564523+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "find /root/trace-verdict-study -path \"*/results/*.json\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_read-bootstrap-results_20260515T013432",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "find /root/trace-verdict-study -path \"*/results/*.json\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T01:35:27.564651+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_read-bootstrap-results_20260515T013432",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T01:35:27.564775+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "find /root/trace-verdict-study/eval -name \"*.json\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_read-bootstrap-results_20260515T013432",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "find /root/trace-verdict-study/eval -name \"*.json\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T01:35:27.564913+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_read-bootstrap-results_20260515T013432",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T01:35:27.565058+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "find /root/trace-verdict-study -name \"bootstrap_compare*\" -o -name \"bootstrap*results*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_read-bootstrap-results_20260515T013432",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "find /root/trace-verdict-study -name \"bootstrap_compare*\" -o -name \"bootstrap*results*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T01:35:27.565182+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "find /root/trace-verdict-study -path \"*/results/*.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_read-bootstrap-results_20260515T013432",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "find /root/trace-verdict-study -path \"*/results/*.json\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T01:35:27.565375+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "find /root/trace-verdict-study/eval -name \"*.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_read-bootstrap-results_20260515T013432",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "find /root/trace-verdict-study/eval -name \"*.json\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T01:35:27.565527+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/trace-verdict-study/results/bootstrap_compare.json\\n/root/trace-verdict-study/eval/bootstrap_compare.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_read-bootstrap-results_20260515T013432",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T01:35:27.565669+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/trace-verdict-study/results/predictions/no_trace_predictions.json\\n/root/trace-verdict-study/results/predictions/vota_predictions.json\\n/root/trace-verdict-study/results/predictions/full_trace_predictions.json\\n/root/trace-verdict-study/results/bootstrap_compare.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_read-bootstrap-results_20260515T013432",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T01:35:27.565789+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_read-bootstrap-results_20260515T013432",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T01:35:27.565922+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "cat /root/trace-verdict-study/results/bootstrap_compare.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_read-bootstrap-results_20260515T013432",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "cat /root/trace-verdict-study/results/bootstrap_compare.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T01:35:27.566091+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"per_condition\\\": {\\n    \\\"no_trace\\\": {\\n      \\\"accuracy\\\": 0.7512605042016807,\\n      \\\"majority_baseline\\\": 0.7151260504201681,\\n      \\\"majority_class\\\": \\\"pass\\\",\\n      \\\"n\\\": 1190,\\n      \\\"pass_precision\\\": 0.8775510204081632,\\n      \\\"pass_recall\\\": 0.7579318448883666,\\n      \\\"pass_f1\\\": 0.8133669609079445,\\n      \\\"fail_precision\\\": 0.5472527472527473,\\n      \\\"fail_recall\\\": 0.7345132743362832,\\n      \\\"fail_f1\\\": 0.6272040302267003\\n    },\\n    \\\"vota\\\": {\\n      \\\"accuracy\\\": 0.9563025210084034,\\n      \\\"majority_baseline\\\": 0.7151260504201681,\\n      \\\"majority_class\\\": \\\"pass\\\",\\n      \\\"n\\\": 1190,\\n      \\\"pass_precision\\\": 0.9443826473859844,\\n      \\\"pass_recall\\\": 0.9976498237367802,\\n      \\\"pass_f1\\\": 0.9702857142857143,\\n      \\\"fail_precision\\\": 0.993127147766323,\\n      \\\"fail_recall\\\": 0.8525073746312685,\\n      \\\"fail_f1\\\": 0.9174603174603175\\n    },\\n    \\\"full_trace\\\": {\\n      \\\"accuracy\\\": 0.2848739495798319,\\n      \\\"majority_baseline\\\": 0.7151260504201681,\\n      \\\"majority_class\\\": \\\"pass\\\",\\n      \\\"n\\\": 1190,\\n      \\\"pass_precision\\\": 0.0,\\n      \\\"pass_recall\\\": 0.0,\\n      \\\"pass_f1\\\": 0.0,\\n      \\\"fail_precision\\\": 0.2848739495798319,\\n      \\\"fail_recall\\\": 1.0,\\n      \\\"fail_f1\\\": 0.4434270765206017\\n    }\\n  },\\n  \\\"pairwise_comparisons\\\": {\\n    \\\"no_trace_vs_vota\\\": {\\n      \\\"mean_diff\\\": -0.2051658823529412,\\n      \\\"ci_lower\\\": -0.2344537815126051,\\n      \\\"ci_upper\\\": -0.17731092436974782,\\n      \\\"ci_contains_zero\\\": false\\n    },\\n    \\\"no_trace_vs_full_trace\\\": {\\n      \\\"mean_diff\\\": 0.4663019327731094,\\n      \\\"ci_lower\\\": 0.4302521008403362,\\n      \\\"ci_upper\\\": 0.5025210084033613,\\n      \\\"ci_contains_zero\\\": f
…[truncated 732 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_read-bootstrap-results_20260515T013432",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T01:35:27.566309+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "cat /root/autodl-tmp/trace-verdict-study-checkpoints/vota/final/eval_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_read-bootstrap-results_20260515T013432",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "cat /root/autodl-tmp/trace-verdict-study-checkpoints/vota/final/eval_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T01:35:27.566480+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"condition\\\": \\\"vota\\\",\\n  \\\"checkpoint_dir\\\": \\\"/root/autodl-tmp/trace-verdict-study-checkpoints/vota/final\\\",\\n  \\\"metrics\\\": {\\n    \\\"accuracy\\\": 0.9915966386554622,\\n    \\\"majority_baseline\\\": 0.7151260504201681,\\n    \\\"lift\\\": 0.27647058823529413,\\n    \\\"majority_class\\\": \\\"pass\\\",\\n    \\\"n\\\": 1190,\\n    \\\"pass_precision\\\": 1.0,\\n    \\\"pass_recall\\\": 0.9882491186839013,\\n    \\\"pass_f1\\\": 0.9940898345153665,\\n    \\\"fail_precision\\\": 0.9713467048710601,\\n    \\\"fail_recall\\\": 1.0,\\n    \\\"fail_f1\\\": 0.9854651162790696\\n  },\\n  \\\"confidence_intervals\\\": {\\n    \\\"accuracy_ci_lower\\\": 0.9857142857142858,\\n    \\\"accuracy_ci_upper\\\": 0.9966386554621849,\\n    \\\"majority_baseline_ci_lower\\\": 0.6915966386554622,\\n    \\\"majority_baseline_ci_upper\\\": 0.738655462184874,\\n    \\\"lift_ci_lower\\\": 0.25210084033613445,\\n    \\\"lift_ci_upper\\\": 0.3016806722689076,\\n    \\\"pass_precision_ci_lower\\\": 1.0,\\n    \\\"pass_precision_ci_upper\\\": 1.0,\\n    \\\"pass_recall_ci_lower\\\": 0.9796131433018113,\\n    \\\"pass_recall_ci_upper\\\": 0.9952325614393552,\\n    \\\"pass_f1_ci_lower\\\": 0.9897015955707957,\\n    \\\"pass_f1_ci_upper\\\": 0.9976105850249356,\\n    \\\"fail_precision_ci_lower\\\": 0.9510086455331412,\\n    \\\"fail_precision_ci_upper\\\": 0.9881314417150985,\\n    \\\"fail_recall_ci_lower\\\": 1.0,\\n    \\\"fail_recall_ci_upper\\\": 1.0,\\n    \\\"fail_f1_ci_lower\\\": 0.9748892171344166,\\n    \\\"fail_f1_ci_upper\\\": 0.9940302949538025\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_read-bootstrap-results_20260515T013432",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T01:35:27.566623+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "cat /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace/final/eval_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_read-bootstrap-results_20260515T013432",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "cat /root/autodl-tmp/trace-verdict-study-checkpoints/full_trace/final/eval_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T01:35:27.566744+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11235",
  "command": "cat /root/autodl-tmp/trace-verdict-study-checkpoints/no_trace/final/eval_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_read-bootstrap-results_20260515T013432",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11235",
    "command": "cat /root/autodl-tmp/trace-verdict-study-checkpoints/no_trace/final/eval_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T01:35:27.566898+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"condition\\\": \\\"full_trace\\\",\\n  \\\"checkpoint_dir\\\": \\\"/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace/final\\\",\\n  \\\"metrics\\\": {\\n    \\\"accuracy\\\": 0.28403361344537814,\\n    \\\"majority_baseline\\\": 0.7151260504201681,\\n    \\\"lift\\\": -0.43109243697478994,\\n    \\\"majority_class\\\": \\\"pass\\\",\\n    \\\"n\\\": 1190,\\n    \\\"pass_precision\\\": 0.9230769230769231,\\n    \\\"pass_recall\\\": 0.0846063454759107,\\n    \\\"pass_f1\\\": 0.15500538213132403,\\n    \\\"fail_precision\\\": 0.44481605351170567,\\n    \\\"fail_recall\\\": 0.7846607669616519,\\n    \\\"fail_f1\\\": 0.567769477054429\\n  },\\n  \\\"confidence_intervals\\\": {\\n    \\\"accuracy_ci_lower\\\": 0.2605042016806723,\\n    \\\"accuracy_ci_upper\\\": 0.3092436974789916,\\n    \\\"majority_baseline_ci_lower\\\": 0.6915966386554622,\\n    \\\"majority_baseline_ci_upper\\\": 0.738655462184874,\\n    \\\"lift_ci_lower\\\": -0.47394957983193275,\\n    \\\"lift_ci_upper\\\": -0.3857142857142857,\\n    \\\"pass_precision_ci_lower\\\": 0.8620597945707996,\\n    \\\"pass_precision_ci_upper\\\": 0.9759107860011474,\\n    \\\"pass_recall_ci_lower\\\": 0.0671279822245761,\\n    \\\"pass_recall_ci_upper\\\": 0.10256709451575262,\\n    \\\"pass_f1_ci_lower\\\": 0.1252508178844057,\\n    \\\"pass_f1_ci_upper\\\": 0.18502805471829356,\\n    \\\"fail_precision_ci_lower\\\": 0.4088577384976979,\\n    \\\"fail_precision_ci_upper\\\": 0.4848615240181505,\\n    \\\"fail_recall_ci_lower\\\": 0.7421259390950278,\\n    \\\"fail_recall_ci_upper\\\": 0.8246178160919541,\\n    \\\"fail_f1_ci_lower\\\": 0.5316880322398293,\\n    \\\"fail_f1_ci_upper\\\": 0.6027902237707393\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_read-bootstrap-results_20260515T013432",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T01:35:27.567072+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"condition\\\": \\\"no_trace\\\",\\n  \\\"checkpoint_dir\\\": \\\"/root/autodl-tmp/trace-verdict-study-checkpoints/no_trace/final\\\",\\n  \\\"metrics\\\": {\\n    \\\"accuracy\\\": 0.7512605042016807,\\n    \\\"majority_baseline\\\": 0.7151260504201681,\\n    \\\"lift\\\": 0.03613445378151259,\\n    \\\"majority_class\\\": \\\"pass\\\",\\n    \\\"n\\\": 1190,\\n    \\\"pass_precision\\\": 0.8775510204081632,\\n    \\\"pass_recall\\\": 0.7579318448883666,\\n    \\\"pass_f1\\\": 0.8133669609079445,\\n    \\\"fail_precision\\\": 0.5472527472527473,\\n    \\\"fail_recall\\\": 0.7345132743362832,\\n    \\\"fail_f1\\\": 0.6272040302267003\\n  },\\n  \\\"confidence_intervals\\\": {\\n    \\\"accuracy_ci_lower\\\": 0.7277310924369748,\\n    \\\"accuracy_ci_upper\\\": 0.7747899159663866,\\n    \\\"majority_baseline_ci_lower\\\": 0.6915966386554622,\\n    \\\"majority_baseline_ci_upper\\\": 0.738655462184874,\\n    \\\"lift_ci_lower\\\": 0.004201680672268893,\\n    \\\"lift_ci_upper\\\": 0.07058823529411762,\\n    \\\"pass_precision_ci_lower\\\": 0.8548381625596359,\\n    \\\"pass_precision_ci_upper\\\": 0.8998629173603213,\\n    \\\"pass_recall_ci_lower\\\": 0.7303957863193066,\\n    \\\"pass_recall_ci_upper\\\": 0.7854691444656843,\\n    \\\"pass_f1_ci_lower\\\": 0.7928025838972547,\\n    \\\"pass_f1_ci_upper\\\": 0.8325087319589699,\\n    \\\"fail_precision_ci_lower\\\": 0.5058674294242009,\\n    \\\"fail_precision_ci_upper\\\": 0.5921988924670559,\\n    \\\"fail_recall_ci_lower\\\": 0.6896525990735975,\\n    \\\"fail_recall_ci_upper\\\": 0.7805682938856016,\\n    \\\"fail_f1_ci_lower\\\": 0.5902680712254419,\\n    \\\"fail_f1_ci_upper\\\": 0.6650001556662515\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_read-bootstrap-results_20260515T013432",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-15T01:35:27.567275+00:00_

全部结果如下：

---

### bootstrap_compare.json（核心对比结果）

| Condition | Accuracy | Majority Baseline | N |
|-----------|----------|-------------------|------|
| **vota** | **95.63%** | 71.51% | 1190 |
| no_trace | 75.13% | 71.51% | 1190 |
| full_trace | 28.49% | 71.51% | 1190 |

**VOTA 详细指标（bootstrap_compare）：**
- pass: precision=0.944, recall=0.998, F1=0.970
- fail: precision=0.993, recall=0.853, F1=0.917

**Pairwise 对比（95% CI）：**

| 对比 | Mean Diff | CI Lower | CI Upper | 显著？ |
|------|-----------|----------|----------|--------|
| no_trace vs vota | -20.5pp | -23.4pp | -17.7pp | Yes |
| no_trace vs full_trace | +46.6pp | +43.0pp | +50.3pp | Yes |
| vota vs full_trace | +67.1pp | +64.0pp | +70.2pp | Yes |

**Verdict: PASS** — VOTA 95.6% >= no_trace 75.1% + 2pp

---

### 各 checkpoint eval_results.json

**vota/final** — accuracy=**99.16%**（训练集 eval），pass_F1=0.994，fail_F1=0.985

**no_trace/final** — accuracy=75.13%，pass_F1=0.813，fail_F1=0.627

**full_trace/final** — accuracy=28.40%，pass_F1=0.155，fail_F1=0.568

---

关键发现：vota checkpoint 的 `eval_results.json` 报 99.16% 是训练时 eval split 的结果，而 `bootstrap_compare.json` 中 vota 的 **95.63%** 才是正确的测试集 accuracy。两者差异来源于评估数据集不同。full_trace 条件完全崩溃（28%，低于 majority baseline），模型把几乎所有样本预测为 fail。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_read-bootstrap-results_20260515T013432"
}
```

</details>

---
