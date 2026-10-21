# check freeform seed123 completion

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 57
- **Recorded user turns:** 0
- **Tool calls:** 28
- **Original source:** `logs/chats/worker_check_freeform_seed123_completion_20260515T183847.jsonl`
- **Structured JSON:** [`5c78dfbdc1511811082a.json`](../../sessions/5c/5c78dfbdc1511811082a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

57 recorded events

### Tool call

_source line 1 · 2026-05-15T18:41:04.230348+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__delete_cron",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__delete_cron",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T18:41:04.230695+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T18:41:04.230882+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "tmux list-sessions 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "tmux list-sessions 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T18:41:04.231025+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T18:41:04.231194+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ps aux | grep \"seed 123\" | grep -v grep",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ps aux | grep \"seed 123\" | grep -v grep",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T18:41:04.231356+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T18:41:04.231479+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/results/exp_freeform_ablation_seed123/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/results/exp_freeform_ablation_seed123/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T18:41:04.231605+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 7004\\ndrwxr-xr-x 2 root root      63 May 16 01:18 .\\ndrwxr-xr-x 5 root root     125 May 16 01:14 ..\\n-rw-r--r-- 1 root root     345 May 16 01:18 run_summary.json\\n-rw-r--r-- 1 root root 7164248 May 16 01:18 samples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T18:41:04.231753+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "tmux list-sessions",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "tmux list-sessions",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T18:41:04.231876+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'tmux' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T18:41:04.231993+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/results/exp_freeform_ablation_seed123/run_summary.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/results/exp_freeform_ablation_seed123/run_summary.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T18:41:04.232155+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp_freeform_ablation\\\",\\n  \\\"model\\\": \\\"checkpoints/qwen3-8b-scierc-merged-v2\\\",\\n  \\\"dataset\\\": \\\"scierc\\\",\\n  \\\"n_instances\\\": 551,\\n  \\\"n_samples\\\": 8,\\n  \\\"temperature\\\": 1.0,\\n  \\\"max_tokens\\\": 1024,\\n  \\\"seed\\\": 123,\\n  \\\"use_grammar\\\": false,\\n  \\\"total_samples\\\": 4408,\\n  \\\"total_parsed\\\": 4406,\\n  \\\"parse_rate_pct\\\": 99.95,\\n  \\\"elapsed_seconds\\\": 228.1\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T18:41:04.232291+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/results/exp_freeform_ablation_seed123/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/results/exp_freeform_ablation_seed123/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T18:41:04.232421+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"551 /root/autodl-tmp/struct_self_consist_ie/results/exp_freeform_ablation_seed123/samples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T18:41:04.232575+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/results/exp_freeform_ablation_seed123/ -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/results/exp_freeform_ablation_seed123/ -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T18:41:04.232700+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/results/exp_freeform_ablation_seed123/samples.jsonl\\n/root/autodl-tmp/struct_self_consist_ie/results/exp_freeform_ablation_seed123/run_summary.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T18:41:04.233043+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -1 /root/autodl-tmp/struct_self_consist_ie/results/exp_freeform_ablation_seed123/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -1 /root/autodl-tmp/struct_self_consist_ie/results/exp_freeform_ablation_seed123/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T18:41:04.233491+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"id\\\": \\\"X96-1059_sent000\\\", \\\"text\\\": \\\"Recognition of proper nouns in Japanese text has been studied as a part of the more general problem of morphological analysis in Japanese text processing -LRB- -LSB- 1 -RSB- -LSB- 2 -RSB- -RRB- .\\\", \\\"gold\\\": {\\\"entities\\\": [{\\\"text\\\": \\\"Recognition of proper nouns\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 0, \\\"end\\\": 27}, {\\\"text\\\": \\\"proper nouns\\\", \\\"type\\\": \\\"OtherScientificTerm\\\", \\\"start\\\": 15, \\\"end\\\": 27}, {\\\"text\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"Material\\\", \\\"start\\\": 31, \\\"end\\\": 44}, {\\\"text\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 103, \\\"end\\\": 125}, {\\\"text\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 129, \\\"end\\\": 153}], \\\"relations\\\": [{\\\"head\\\": \\\"Recognition of proper nouns\\\", \\\"tail\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"PART-OF\\\", \\\"head_start\\\": 0, \\\"head_end\\\": 27, \\\"tail_start\\\": 103, \\\"tail_end\\\": 125}, {\\\"head\\\": \\\"proper nouns\\\", \\\"tail\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"PART-OF\\\", \\\"head_start\\\": 15, \\\"head_end\\\": 27, \\\"tail_start\\\": 31, \\\"tail_end\\\": 44}, {\\\"head\\\": \\\"morphological analysis\\\", \\\"tail\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"USED-FOR\\\", \\\"head_start\\\": 103, \\\"head_end\\\": 125, \\\"tail_start\\\": 129, \\\"tail_end\\\": 153}], \\\"events\\\": []}, \\\"samples\\\": [{\\\"entities\\\": [{\\\"text\\\": \\\"Recognition of proper nouns\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 0, \\\"end\\\": 27}, {\\\"text\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"Material\\\", \\\"start\\\": 31, \\\"end\\\": 44}, {\\\"text\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 103, \\\"end\\\": 125}, {\\\"text\\\": \\\"
…[truncated 10076 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T18:41:04.233667+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/results/exp_freeform_ablation/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/results/exp_freeform_ablation/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T18:41:04.233805+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 7020\\ndrwxr-xr-x 2 root root     133 May 15 18:33 .\\ndrwxr-xr-x 5 root root     125 May 16 01:14 ..\\n-rw-r--r-- 1 root root    3519 May 15 17:58 ablation_report.json\\n-rw-r--r-- 1 root root    9245 May 15 18:33 deep_analysis_results.json\\n-rw-r--r-- 1 root root     344 May 15 17:46 run_summary.json\\n-rw-r--r-- 1 root root 7165184 May 15 17:46 samples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T18:41:04.233961+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/results/exp_freeform_ablation/ablation_report.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/results/exp_freeform_ablation/ablation_report.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T18:41:04.234237+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"constrained\\\": {\\n    \\\"logprob_variance\\\": {\\n      \\\"mean_std\\\": 0.020589,\\n      \\\"median_std\\\": 0.013616,\\n      \\\"mean_range\\\": 0.062305,\\n      \\\"median_range\\\": 0.041348,\\n      \\\"tied_pct\\\": 59.7,\\n      \\\"n\\\": 551\\n    },\\n    \\\"selection_ner\\\": {\\n      \\\"greedy\\\": 0.6182,\\n      \\\"selected\\\": 0.6241,\\n      \\\"gap\\\": 0.0059\\n    },\\n    \\\"selection_re\\\": {\\n      \\\"greedy\\\": 0.2913,\\n      \\\"selected\\\": 0.2845,\\n      \\\"gap\\\": -0.0068\\n    },\\n    \\\"qe_ner\\\": {\\n      \\\"n\\\": 529,\\n      \\\"signals\\\": {\\n        \\\"SJ\\\": {\\n          \\\"rho\\\": 0.359891,\\n          \\\"p_rho\\\": 0.0,\\n          \\\"auroc\\\": 0.717989\\n        },\\n        \\\"FK\\\": {\\n          \\\"rho\\\": 0.266511,\\n          \\\"p_rho\\\": 0.0,\\n          \\\"auroc\\\": 0.747783\\n        },\\n        \\\"logprob\\\": {\\n          \\\"rho\\\": 0.205174,\\n          \\\"p_rho\\\": 2e-06,\\n          \\\"auroc\\\": 0.654773\\n        },\\n        \\\"EM\\\": {\\n          \\\"rho\\\": 0.294549,\\n          \\\"p_rho\\\": 0.0,\\n          \\\"auroc\\\": 0.499819\\n        },\\n        \\\"voting_conf\\\": {\\n          \\\"rho\\\": 0.379176,\\n          \\\"p_rho\\\": 0.0,\\n          \\\"auroc\\\": 0.772093\\n        }\\n      }\\n    },\\n    \\\"qe_re\\\": {\\n      \\\"n\\\": 397,\\n      \\\"signals\\\": {\\n        \\\"SJ\\\": {\\n          \\\"rho\\\": 0.250336,\\n          \\\"p_rho\\\": 0.0,\\n          \\\"auroc\\\": 0.609931\\n        },\\n        \\\"FK\\\": {\\n          \\\"rho\\\": 0.275204,\\n          \\\"p_rho\\\": 0.0,\\n          \\\"auroc\\\": 0.663813\\n        },\\n        \\\"logprob\\\": {\\n          \\\"rho\\\": 0.266245,\\n          \\\"p_rho\\\": 0.0,\\n          \\\"auroc\\\": 0.67803\\n        },\\n        \\\"EM\\\": {\\n          \\\"rho\\\": 0.134388,\\n          \\\"p_rho\\\": 0.00
…[truncated 2821 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T18:41:04.234427+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/ -maxdepth 1 -name \"*.py\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/ -maxdepth 1 -name \"*.py\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T18:41:04.234572+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/merge_lora.py\\n/root/autodl-tmp/struct_self_consist_ie/run_bootstrap_loo.py\\n/root/autodl-tmp/struct_self_consist_ie/run_loo_v2.py\\n/root/autodl-tmp/struct_self_consist_ie/patch_scripts.py\\n/root/autodl-tmp/struct_self_consist_ie/run_llama_conll_bootstrap.py\\n/root/autodl-tmp/struct_self_consist_ie/bootstrap_analysis.py\\n/root/autodl-tmp/struct_self_consist_ie/bootstrap_analysis2.py\\n/root/autodl-tmp/struct_self_consist_ie/logprob_tie_analysis.py\\n/root/autodl-tmp/struct_self_consist_ie/logprob_tie_structural.py\\n/root/autodl-tmp/struct_self_consist_ie/run_freeform_inference.py\\n/root/autodl-tmp/struct_self_consist_ie/analyze_freeform_ablation.py\\n/root/autodl-tmp/struct_self_consist_ie/train_supervised_verifier.py\\n/root/autodl-tmp/struct_self_consist_ie/evaluate_verifier.py\\n/root/autodl-tmp/struct_self_consist_ie/deep_freeform_analysis.py\\n/root/autodl-tmp/struct_self_consist_ie/multiseed_flip_analysis.py\\n/root/autodl-tmp/struct_self_consist_ie/multiseed_flip_analysis_part2.py\\n/root/autodl-tmp/struct_self_consist_ie/compute_fk_excess.py\\n/root/autodl-tmp/struct_self_consist_ie/rho_audit.py\\n/root/autodl-tmp/struct_self_consist_ie/compute_missing_n8.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T18:41:04.234746+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -50 /root/autodl-tmp/struct_self_consist_ie/analyze_freeform_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -50 /root/autodl-tmp/struct_self_consist_ie/analyze_freeform_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T18:41:04.234894+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Analyze free-form vs constrained decoding ablation.\\n\\nCompares logprob variance, selection performance, QE signals, and parse rate\\nbetween constrained (exp_012_rerun_1024) and free-form (exp_freeform_ablation).\\n\\nInput:\\n  - output/exp_012_rerun_1024/samples.jsonl (constrained baseline)\\n  - results/exp_freeform_ablation/samples.jsonl (free-form)\\nOutput:\\n  - results/exp_freeform_ablation/ablation_report.json\\nDependencies: code/{consistency,evaluation}.py\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport os\\nimport sys\\nfrom collections import Counter\\n\\nimport numpy as np\\nfrom scipy.stats import spearmanr, rankdata\\n\\nsys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), \\\"code\\\"))\\n\\nfrom consistency import (\\n    fleiss_kappa_surface,\\n    structural_consistency_soft_jaccard,\\n)\\nfrom evaluation import per_instance_f1\\n\\n\\nCONSTRAINED_PATH = \\\"output/exp_012_rerun_1024/samples.jsonl\\\"\\nFREEFORM_PATH = \\\"results/exp_freeform_ablation/samples.jsonl\\\"\\n\\n\\ndef load_data(path):\\n    with open(path) as f:\\n        return [json.loads(line) for line in f if line.strip()]\\n\\n\\ndef safe_spearman(x, y):\\n    x, y = np.asarray(x, float), np.asarray(y, float)\\n    m = np.isfinite(x) & np.isfinite(y)\\n    x, y = x[m], y[m]\\n    if len(x) < 3:\\n        return float(\\\"nan\\\"), float(\\\"nan\\\")\\n    r = spearmanr(x, y)\\n    return float(r.statistic), float(r.pvalue)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T18:41:04.235043+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -n \"argparse\\|add_argument\\|parse_args\\|__main__\" /root/autodl-tmp/struct_self_consist_ie/analyze_freeform_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -n \"argparse\\|add_argument\\|parse_args\\|__main__\" /root/autodl-tmp/struct_self_consist_ie/analyze_freeform_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T18:41:04.235205+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T18:41:04.235339+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -n \"argparse\\|add_argument\\|parse_args\\|__main__\" /root/autodl-tmp/struct_self_consist_ie/analyze_freeform_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -n \"argparse\\|add_argument\\|parse_args\\|__main__\" /root/autodl-tmp/struct_self_consist_ie/analyze_freeform_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T18:41:04.235462+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T18:41:04.235579+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -n \"argparse\" /root/autodl-tmp/struct_self_consist_ie/analyze_freeform_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -n \"argparse\" /root/autodl-tmp/struct_self_consist_ie/analyze_freeform_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T18:41:04.235698+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"16:import argparse\\n196:    p = argparse.ArgumentParser()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T18:41:04.235813+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -n \"__main__\" /root/autodl-tmp/struct_self_consist_ie/analyze_freeform_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -n \"__main__\" /root/autodl-tmp/struct_self_consist_ie/analyze_freeform_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T18:41:04.235930+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"298:if __name__ == \\\"__main__\\\":\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T18:41:04.236043+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "tail -30 /root/autodl-tmp/struct_self_consist_ie/analyze_freeform_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "tail -30 /root/autodl-tmp/struct_self_consist_ie/analyze_freeform_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T18:41:04.236204+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"        print(f\\\"  {'Signal':<12} {'C_rho':>8} {'C_AUROC':>8} {'F_rho':>8} {'F_AUROC':>8} {'delta_rho':>10}\\\")\\n        for sig in [\\\"SJ\\\", \\\"FK\\\", \\\"logprob\\\", \\\"EM\\\", \\\"voting_conf\\\"]:\\n            cr, ca = c_qe[sig][\\\"rho\\\"], c_qe[sig][\\\"auroc\\\"]\\n            fr, fa = f_qe[sig][\\\"rho\\\"], f_qe[sig][\\\"auroc\\\"]\\n            dr = fr - cr if np.isfinite(fr) and np.isfinite(cr) else float(\\\"nan\\\")\\n            print(f\\\"  {sig:<12} {cr:>8.4f} {ca:>8.4f} {fr:>8.4f} {fa:>8.4f} {dr:>+10.4f}\\\")\\n\\n    # 5. Comparison summary\\n    report[\\\"comparison\\\"] = {\\n        \\\"variance_ratio_std\\\": round(float(np.mean(f_stds) / max(np.mean(c_stds), 1e-8)), 2),\\n        \\\"variance_ratio_range\\\": round(float(np.mean(f_ranges) / max(np.mean(c_ranges), 1e-8)), 2),\\n        \\\"tied_reduction_pp\\\": round((c_tied - f_tied) * 100, 1),\\n        \\\"parse_rate_pct\\\": round(parse_rate, 2),\\n    }\\n\\n    os.makedirs(args.output_dir, exist_ok=True)\\n    report_path = os.path.join(args.output_dir, \\\"ablation_report.json\\\")\\n    with open(report_path, \\\"w\\\") as f:\\n        json.dump(report, f, indent=2)\\n\\n    print(f\\\"\\\\n=== Summary ===\\\")\\n    print(f\\\"Variance ratio (std):   {report['comparison']['variance_ratio_std']}x\\\")\\n    print(f\\\"Variance ratio (range): {report['comparison']['variance_ratio_range']}x\\\")\\n    print(f\\\"Tied reduction:         {report['comparison']['tied_reduction_pp']:+.1f}pp\\\")\\n    print(f\\\"Parse rate:             {parse_rate:.1f}%\\\")\\n    print(f\\\"\\\\nReport: {report_path}\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T18:41:04.236349+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "sed -n '190,210p' /root/autodl-tmp/struct_self_consist_ie/analyze_freeform_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "sed -n '190,210p' /root/autodl-tmp/struct_self_consist_ie/analyze_freeform_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T18:41:04.236471+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T18:41:04.236586+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -210 /root/autodl-tmp/struct_self_consist_ie/analyze_freeform_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -210 /root/autodl-tmp/struct_self_consist_ie/analyze_freeform_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T18:41:04.236792+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Analyze free-form vs constrained decoding ablation.\\n\\nCompares logprob variance, selection performance, QE signals, and parse rate\\nbetween constrained (exp_012_rerun_1024) and free-form (exp_freeform_ablation).\\n\\nInput:\\n  - output/exp_012_rerun_1024/samples.jsonl (constrained baseline)\\n  - results/exp_freeform_ablation/samples.jsonl (free-form)\\nOutput:\\n  - results/exp_freeform_ablation/ablation_report.json\\nDependencies: code/{consistency,evaluation}.py\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport os\\nimport sys\\nfrom collections import Counter\\n\\nimport numpy as np\\nfrom scipy.stats import spearmanr, rankdata\\n\\nsys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), \\\"code\\\"))\\n\\nfrom consistency import (\\n    fleiss_kappa_surface,\\n    structural_consistency_soft_jaccard,\\n)\\nfrom evaluation import per_instance_f1\\n\\n\\nCONSTRAINED_PATH = \\\"output/exp_012_rerun_1024/samples.jsonl\\\"\\nFREEFORM_PATH = \\\"results/exp_freeform_ablation/samples.jsonl\\\"\\n\\n\\ndef load_data(path):\\n    with open(path) as f:\\n        return [json.loads(line) for line in f if line.strip()]\\n\\n\\ndef safe_spearman(x, y):\\n    x, y = np.asarray(x, float), np.asarray(y, float)\\n    m = np.isfinite(x) & np.isfinite(y)\\n    x, y = x[m], y[m]\\n    if len(x) < 3:\\n        return float(\\\"nan\\\"), float(\\\"nan\\\")\\n    r = spearmanr(x, y)\\n    return float(r.statistic), float(r.pvalue)\\n\\n\\ndef safe_auroc(scores, labels):\\n    scores, labels = np.asarray(scores, float), np.asarray(labels, int)\\n    if len(np.unique(labels)) < 2:\\n        return float(\\\"nan\\\")\\n    n_pos = int((labels == 1).sum())\\n    n_neg = int((labels == 0).sum())\\n    if n_pos == 0 or n_neg == 0:\\n        return float(\\\"nan\\\")\\n    ranks = rankdata(scores)\\n    u = ranks[labels == 1].sum() - n_pos * (n_pos +
…[truncated 5881 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T18:41:04.237001+00:00_

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
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
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

_source line 42 · 2026-05-15T18:41:04.237147+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T18:41:04.237272+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/struct_self_consist_ie && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python analyze_freeform_ablation.py --freeform results/exp_freeform_ablation_seed123/samples.jsonl --output_dir results/exp_freeform_ablation_seed123",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/struct_self_consist_ie && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python analyze_freeform_ablation.py --freeform results/exp_freeform_ablation_seed123/samples.jsonl --output_dir results/exp_freeform_ablation_seed123",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T18:41:04.237415+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loading data...\\n  Constrained: 551 | Free-form: 551\\n\\n=== Logprob Variance ===\\n  Constrained: std=0.0206 range=0.0623 tied=59.7%\\n  Free-form:   std=0.0199 range=0.0599 tied=57.7%\\n\\n=== Parse Rate: 100.0% (4406/4408) ===\\n\\n=== Selection F1 ===\\n  [NER] Con: 0.6182 -> 0.6241 (+0.0059) | Free: 0.6194 -> 0.6222 (+0.0028)\\n  [RE] Con: 0.2913 -> 0.2845 (-0.0068) | Free: 0.2874 -> 0.3050 (+0.0176)\\n\\n=== QE Metrics ===\\n\\n  [NER] n_con=529 n_free=529\\n  Signal          C_rho  C_AUROC    F_rho  F_AUROC  delta_rho\\n  SJ             0.3599   0.7180   0.3842   0.7487    +0.0243\\n  FK             0.2665   0.7478   0.3240   0.7660    +0.0574\\n  logprob        0.2052   0.6548   0.2173   0.7017    +0.0121\\n  EM             0.2945   0.4998   0.3269   0.5253    +0.0323\\n  voting_conf    0.3792   0.7721   0.4079   0.7997    +0.0287\\n\\n  [RE] n_con=397 n_free=397\\n  Signal          C_rho  C_AUROC    F_rho  F_AUROC  delta_rho\\n  SJ             0.2503   0.6099   0.2728   0.6141    +0.0224\\n  FK             0.2752   0.6638   0.3144   0.6785    +0.0392\\n  logprob        0.2662   0.6780   0.3097   0.7041    +0.0434\\n  EM             0.1344   0.4886   0.1372   0.4873    +0.0028\\n  voting_conf    0.3498   0.6820   0.3167   0.6474    -0.0331\\n\\n=== Summary ===\\nVariance ratio (std):   0.97x\\nVariance ratio (range): 0.96x\\nTied reduction:         +2.0pp\\nParse rate:             100.0%\\n\\nReport: results/exp_freeform_ablation_seed123/ablation_report.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.99}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-15T18:41:04.237588+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -30 /root/autodl-tmp/struct_self_consist_ie/deep_freeform_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -30 /root/autodl-tmp/struct_self_consist_ie/deep_freeform_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T18:41:04.237734+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Deep analysis of constrained vs free-form decoding ablation.\\n\\nFocuses on:\\n1. RE LP Selection Flip: why LP selection fails for RE in constrained but works in free-form\\n2. Non-Tied Subset Overlap: how the tied/non-tied instance sets differ between conditions\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\nimport json\\nimport os\\nimport sys\\nimport numpy as np\\nfrom collections import Counter, defaultdict\\nfrom scipy.stats import spearmanr, mannwhitneyu\\n\\nsys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), \\\"code\\\"))\\nfrom evaluation import per_instance_f1, entity_strict_match, relation_strict_match\\n\\nCONSTRAINED_PATH = \\\"output/exp_012_rerun_1024/samples.jsonl\\\"\\nFREEFORM_PATH = \\\"results/exp_freeform_ablation/samples.jsonl\\\"\\n\\ndef load_data(path):\\n    with open(path) as f:\\n        return [json.loads(line) for line in f if line.strip()]\\n\\ndef safe_spearman(x, y):\\n    x, y = np.asarray(x, float), np.asarray(y, float)\\n    m = np.isfinite(x) & np.isfinite(y)\\n    x, y = x[m], y[m]\\n    if len(x) < 3:\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T18:41:04.237864+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/results/exp_freeform_ablation_seed123/ablation_report.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/results/exp_freeform_ablation_seed123/ablation_report.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-15T18:41:04.238071+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"constrained\\\": {\\n    \\\"logprob_variance\\\": {\\n      \\\"mean_std\\\": 0.020589,\\n      \\\"median_std\\\": 0.013616,\\n      \\\"mean_range\\\": 0.062305,\\n      \\\"median_range\\\": 0.041348,\\n      \\\"tied_pct\\\": 59.7,\\n      \\\"n\\\": 551\\n    },\\n    \\\"selection_ner\\\": {\\n      \\\"greedy\\\": 0.6182,\\n      \\\"selected\\\": 0.6241,\\n      \\\"gap\\\": 0.0059\\n    },\\n    \\\"selection_re\\\": {\\n      \\\"greedy\\\": 0.2913,\\n      \\\"selected\\\": 0.2845,\\n      \\\"gap\\\": -0.0068\\n    },\\n    \\\"qe_ner\\\": {\\n      \\\"n\\\": 529,\\n      \\\"signals\\\": {\\n        \\\"SJ\\\": {\\n          \\\"rho\\\": 0.359891,\\n          \\\"p_rho\\\": 0.0,\\n          \\\"auroc\\\": 0.717989\\n        },\\n        \\\"FK\\\": {\\n          \\\"rho\\\": 0.266511,\\n          \\\"p_rho\\\": 0.0,\\n          \\\"auroc\\\": 0.747783\\n        },\\n        \\\"logprob\\\": {\\n          \\\"rho\\\": 0.205174,\\n          \\\"p_rho\\\": 2e-06,\\n          \\\"auroc\\\": 0.654773\\n        },\\n        \\\"EM\\\": {\\n          \\\"rho\\\": 0.294549,\\n          \\\"p_rho\\\": 0.0,\\n          \\\"auroc\\\": 0.499819\\n        },\\n        \\\"voting_conf\\\": {\\n          \\\"rho\\\": 0.379176,\\n          \\\"p_rho\\\": 0.0,\\n          \\\"auroc\\\": 0.772093\\n        }\\n      }\\n    },\\n    \\\"qe_re\\\": {\\n      \\\"n\\\": 397,\\n      \\\"signals\\\": {\\n        \\\"SJ\\\": {\\n          \\\"rho\\\": 0.250336,\\n          \\\"p_rho\\\": 0.0,\\n          \\\"auroc\\\": 0.609931\\n        },\\n        \\\"FK\\\": {\\n          \\\"rho\\\": 0.275204,\\n          \\\"p_rho\\\": 0.0,\\n          \\\"auroc\\\": 0.663813\\n        },\\n        \\\"logprob\\\": {\\n          \\\"rho\\\": 0.266245,\\n          \\\"p_rho\\\": 0.0,\\n          \\\"auroc\\\": 0.67803\\n        },\\n        \\\"EM\\\": {\\n          \\\"rho\\\": 0.134388,\\n          \\\"p_rho\\\": 0.00
…[truncated 2819 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-15T18:41:04.238282+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_freeform_seed123",
  "field": "status",
  "value": "ANALYZING",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_freeform_seed123",
    "field": "status",
    "value": "ANALYZING",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T18:41:04.238430+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_freeform_seed123\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:14:47.765Z\", \"updated_at\": \"2026-05-15T18:40:37.078Z\", \"spec\": {\"hypothesis\": \"Multi-seed free-form ablation (seed=123): verify RE LP flip and NER gap stability\", \"command\": \"python run_freeform_inference.py --seed 123 --num_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir results/exp_freeform_ablation_seed123\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 123, \"gpu\": \"cuda:1\", \"tmux_session\": \"exp_freeform_seed123\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.4138}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-15T18:41:04.238594+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_freeform_seed123",
  "field": "metrics",
  "value": "{'inference': {'n_instances': 551, 'n_samples': 8, 'total_samples': 4408, 'total_parsed': 4406, 'parse_rate_pct': 99.95, 'elapsed_seconds': 228.1}, 'freeform': {'selection_ner': {'greedy': 0.6194, 'selected': 0.6222, 'gap': 0.0028}, 'selection_re': {'greedy': 0.2874, 'selected': 0.305, 'gap': 0.0176}, 'logprob_variance': {'mean_std': 0.019881, 'mean_range': 0.059864, 'tied_pct': 57.7}, 'qe_ner': {'n': 529, 'SJ': {'rho': 0.384214, 'auroc': 0.748728}, 'FK': {'rho': 0.323956, 'auroc': 0.766039}, 'logprob': {'rho': 0.217297, 'auroc': 0.701657}, 'EM': {'rho': 0.326887, 'auroc': 0.52533}, 'voting_conf': {'rho': 0.407893, 'auroc': 0.799676}}, 'qe_re': {'n': 397, 'SJ': {'rho': 0.272776, 'auroc': 0.614056}, 'FK': {'rho': 0.314429, 'auroc': 0.678534}, 'logprob': {'rho': 0.309673, 'auroc': 0.70414}, 'EM': {'rho': 0.137216, 'auroc': 0.487342}, 'voting_conf': {'rho': 0.316667, 'auroc': 0.647442}}}, 'constrained_ref': {'selection_ner': {'greedy': 0.6182, 'selected': 0.6241, 'gap': 0.0059}, 'selection_re': {'greedy': 0.2913, 'selected': 0.2845, 'gap': -0.0068}}, 'comparison': {'variance_ratio_std': 0.97, 'variance_ratio_range': 0.96, 'tied_reduction_pp': 2}}",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_freeform_seed123",
    "field": "metrics",
    "value": "{'inference': {'n_instances': 551, 'n_samples': 8, 'total_samples': 4408, 'total_parsed': 4406, 'parse_rate_pct': 99.95, 'elapsed_seconds': 228.1}, 'freeform': {'selection_ner': {'greedy': 0.6194, 'selected': 0.6222, 'gap': 0.0028}, 'selection_re': {'greedy': 0.2874, 'selected': 0.305, 'gap': 0.0176}, 'logprob_variance': {'mean_std': 0.019881, 'mean_range': 0.059864, 'tied_pct': 57.7}, 'qe_ner': {'n': 529, 'SJ': {'rho': 0.384214, 'auroc': 0.748728}, 'FK': {'rho': 0.323956, 'auroc': 0.766039}, 'logprob': {'rho': 0.217297, 'auroc': 0.701657}, 'EM': {'rho': 0.326887, 'auroc': 0.52533}, 'voting_conf': {'rho': 0.407893, 'auroc': 0.799676}}, 'qe_re': {'n': 397, 'SJ': {'rho': 0.272776, 'auroc': 0.614056}, 'FK': {'rho': 0.314429, 'auroc': 0.678534}, 'logprob': {'rho': 0.309673, 'auroc': 0.70414}, 'EM': {'rho': 0.137216, 'auroc': 0.487342}, 'voting_conf': {'rho': 0.316667, 'auroc': 0.647442}}}, 'constrained_ref': {'selection_ner': {'greedy': 0.6182, 'selected': 0.6241, 'gap': 0.0059}, 'selection_re': {'greedy': 0.2913, 'selected': 0.2845, 'gap': -0.0068}}, 'comparison': {'variance_ratio_std': 0.97, 'variance_ratio_range': 0.96, 'tied_reduction_pp': 2}}",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-15T18:41:04.238822+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_freeform_seed123\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:14:47.765Z\", \"updated_at\": \"2026-05-15T18:40:48.101Z\", \"spec\": {\"hypothesis\": \"Multi-seed free-form ablation (seed=123): verify RE LP flip and NER gap stability\", \"command\": \"python run_freeform_inference.py --seed 123 --num_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir results/exp_freeform_ablation_seed123\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 123, \"gpu\": \"cuda:1\", \"tmux_session\": \"exp_freeform_seed123\"}, \"metrics\": {\"inference\": {\"n_instances\": 551, \"n_samples\": 8, \"total_samples\": 4408, \"total_parsed\": 4406, \"parse_rate_pct\": 99.95, \"elapsed_seconds\": 228.1}, \"freeform\": {\"selection_ner\": {\"greedy\": 0.6194, \"selected\": 0.6222, \"gap\": 0.0028}, \"selection_re\": {\"greedy\": 0.2874, \"selected\": 0.305, \"gap\": 0.0176}, \"logprob_variance\": {\"mean_std\": 0.019881, \"mean_range\": 0.059864, \"tied_pct\": 57.7}, \"qe_ner\": {\"n\": 529, \"SJ\": {\"rho\": 0.384214, \"auroc\": 0.748728}, \"FK\": {\"rho\": 0.323956, \"auroc\": 0.766039}, \"logprob\": {\"rho\": 0.217297, \"auroc\": 0.701657}, \"EM\": {\"rho\": 0.326887, \"auroc\": 0.52533}, \"voting_conf\": {\"rho\": 0.407893, \"auroc\": 0.799676}}, \"qe_re\": {\"n\": 397, \"SJ\": {\"rho\": 0.272776, \"auroc\": 0.614056}, \"FK\": {\"rho\": 0.314429, \"auroc\": 0.678534}, \"logprob\": {\"rho\": 0.309673, \"auroc\": 0.70414}, \"EM\": {\"rho\": 0.137216, \"auroc\": 0.487342}, \"voting_conf\": {\"rho\": 0.316667, \"auroc\": 0.647442}}}, \"constrained_ref\": {\"selection_ner\": {\"greedy\": 0.6182, \"selected\": 0.6241, \"gap\": 0.0059}, \"selection_re\": {\"greedy\": 0.2913, \"selected\": 0.2845, \"gap\": -0.0068}}, \"comparison\": {\"variance_ratio_std\": 0.97, \"variance
…[truncated 115 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-15T18:41:04.238981+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_freeform_seed123",
  "field": "spec",
  "value": "{'hypothesis': 'Multi-seed free-form ablation (seed=123): verify RE LP flip and NER gap stability', 'command': 'python run_freeform_inference.py --seed 123 --num_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir results/exp_freeform_ablation_seed123', 'server': 'autodl-5090', 'data_path': 'data/scierc/processed_data', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 123, 'gpu': 'cuda:1', 'tmux_session': 'exp_freeform_seed123', 'log_path': 'results/exp_freeform_ablation_seed123/run_summary.json', 'checkpoint_path': 'results/exp_freeform_ablation_seed123'}",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_freeform_seed123",
    "field": "spec",
    "value": "{'hypothesis': 'Multi-seed free-form ablation (seed=123): verify RE LP flip and NER gap stability', 'command': 'python run_freeform_inference.py --seed 123 --num_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir results/exp_freeform_ablation_seed123', 'server': 'autodl-5090', 'data_path': 'data/scierc/processed_data', 'data_count': 551, 'model_name': 'qwen3-8b-scierc-merged-v2', 'seed': 123, 'gpu': 'cuda:1', 'tmux_session': 'exp_freeform_seed123', 'log_path': 'results/exp_freeform_ablation_seed123/run_summary.json', 'checkpoint_path': 'results/exp_freeform_ablation_seed123'}",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-15T18:41:04.239178+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_freeform_seed123\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:14:47.765Z\", \"updated_at\": \"2026-05-15T18:40:50.485Z\", \"spec\": {\"hypothesis\": \"Multi-seed free-form ablation (seed=123): verify RE LP flip and NER gap stability\", \"command\": \"python run_freeform_inference.py --seed 123 --num_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir results/exp_freeform_ablation_seed123\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 123, \"gpu\": \"cuda:1\", \"tmux_session\": \"exp_freeform_seed123\", \"log_path\": \"results/exp_freeform_ablation_seed123/run_summary.json\", \"checkpoint_path\": \"results/exp_freeform_ablation_seed123\"}, \"metrics\": {\"inference\": {\"n_instances\": 551, \"n_samples\": 8, \"total_samples\": 4408, \"total_parsed\": 4406, \"parse_rate_pct\": 99.95, \"elapsed_seconds\": 228.1}, \"freeform\": {\"selection_ner\": {\"greedy\": 0.6194, \"selected\": 0.6222, \"gap\": 0.0028}, \"selection_re\": {\"greedy\": 0.2874, \"selected\": 0.305, \"gap\": 0.0176}, \"logprob_variance\": {\"mean_std\": 0.019881, \"mean_range\": 0.059864, \"tied_pct\": 57.7}, \"qe_ner\": {\"n\": 529, \"SJ\": {\"rho\": 0.384214, \"auroc\": 0.748728}, \"FK\": {\"rho\": 0.323956, \"auroc\": 0.766039}, \"logprob\": {\"rho\": 0.217297, \"auroc\": 0.701657}, \"EM\": {\"rho\": 0.326887, \"auroc\": 0.52533}, \"voting_conf\": {\"rho\": 0.407893, \"auroc\": 0.799676}}, \"qe_re\": {\"n\": 397, \"SJ\": {\"rho\": 0.272776, \"auroc\": 0.614056}, \"FK\": {\"rho\": 0.314429, \"auroc\": 0.678534}, \"logprob\": {\"rho\": 0.309673, \"auroc\": 0.70414}, \"EM\": {\"rho\": 0.137216, \"auroc\": 0.487342}, \"voting_conf\": {\"rho\": 0.316667, \"auroc\": 0.647442}}}, \"constrained_ref\": {\"selection_ner\": {\"greedy\": 0.6182, \"selected\": 0.6241, \"gap\": 0.0059}, 
…[truncated 253 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-15T18:41:04.239340+00:00_

called mcp__agent-ml-research__delete_cron

<details open><summary>🔧 Tool call — mcp__agent-ml-research__delete_cron</summary>

```json
{
  "exp_id": "exp_freeform_seed123"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__delete_cron",
  "tool_args": {
    "exp_id": "exp_freeform_seed123"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-15T18:41:04.239469+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No cron found for 'exp_freeform_seed123'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_freeform_seed123_completion_20260515T183847",
  "tool": "mcp__agent-ml-research__delete_cron",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-15T18:41:04.239630+00:00_

Cron 已不存在（可能已被之前清除）。Registry 已更新完毕。

## 实验结果摘要：exp_freeform_seed123

**状态**：成功完成，228s，551 instances × 8 samples，parse rate 99.95%

### Selection F1（seed123 freeform vs constrained baseline）

| Subtask | Constrained (greedy→sel) | Freeform seed123 (greedy→sel) |
|---------|--------------------------|-------------------------------|
| **NER** | 0.6182 → 0.6241 (+0.006) | 0.6194 → 0.6222 (+0.003) |
| **RE**  | 0.2913 → 0.2845 (**-0.007**) | 0.2874 → 0.3050 (**+0.018**) |

**RE LP flip 在 seed123 复现**：constrained RE selection 仍然为负（-0.007），freeform 翻正（+0.018），与 seed42 一致。

### QE Signals（freeform seed123 vs seed42 对比）

| Signal | NER AUROC (s42/s123) | RE AUROC (s42/s123) |
|--------|---------------------|---------------------|
| SJ | 0.746 / 0.749 | 0.617 / 0.614 |
| FK | 0.762 / 0.766 | 0.684 / 0.679 |
| logprob | 0.698 / 0.702 | 0.702 / 0.704 |
| voting_conf | 0.796 / 0.800 | 0.655 / 0.647 |

seed123 和 seed42 的 QE 指标高度一致，差异均在 ±0.01 以内，证实结果稳定。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_check_freeform_seed123_completion_20260515T183847"
}
```

</details>

---
