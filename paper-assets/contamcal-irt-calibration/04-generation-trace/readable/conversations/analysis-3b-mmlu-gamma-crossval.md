# analysis 3B mmlu gamma crossval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/chats/worker_analysis_3B_mmlu_gamma_crossval_20260515T160046.jsonl`
- **Structured JSON:** [`62cb34928f566aeeb950.json`](../../sessions/62/62cb34928f566aeeb950.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

37 recorded events

### Tool call

_source line 1 · 2026-05-15T16:02:48.690747+00:00_

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
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046",
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

_source line 2 · 2026-05-15T16:02:48.691198+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T16:02:48.691508+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp001/eval_results/ -type d -name \"Qwen2.5-3B*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/exp001/eval_results/ -type d -name \"Qwen2.5-3B*\""
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T16:02:48.691717+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp006/ -type f -name \"*.json\" -path \"*3B*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/exp006/ -type f -name \"*.json\" -path \"*3B*\""
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-15T16:02:48.691996+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_raw\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned_v2\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned_v3\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v1_s42_aligned_DEPRECATED\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_v1_s42_aligned_DEPRECATED\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v1_s42_aligned_DEPRECATED\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v1_s123_DEPRECATED\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_v3_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v3_s42_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_para_aligned\\n/root/aut
…[truncated 168 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T16:02:48.692251+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp006/results_stratified_irt/scheme_B/scale_3B/mmlu_results.json\\n/root/autodl-tmp/exp006/results_stratified_irt/scheme_B/scale_3B/arc_challenge_results.json\\n/root/autodl-tmp/exp006/results_stratified_irt/scheme_B/scale_3B/humaneval_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T16:02:48.692492+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/autodl-tmp/exp006/results_stratified_irt/scheme_B/scale_3B/mmlu_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/autodl-tmp/exp006/results_stratified_irt/scheme_B/scale_3B/mmlu_results.json"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T16:02:48.692792+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"stratum\\\": \\\"B_scale_3B\\\",\\n  \\\"benchmark\\\": \\\"mmlu\\\",\\n  \\\"n_models\\\": 4,\\n  \\\"n_items\\\": 2000,\\n  \\\"original_n_items\\\": 14042,\\n  \\\"subsampled\\\": true,\\n  \\\"unique_dosages\\\": [\\n    0,\\n    100\\n  ],\\n  \\\"has_dosage_variation\\\": true,\\n  \\\"models\\\": [\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-3B_d000_v2_s123_aligned\\\",\\n      \\\"dosage\\\": 0,\\n      \\\"scale\\\": \\\"3B\\\"\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-3B_d000_v2_s42_aligned\\\",\\n      \\\"dosage\\\": 0,\\n      \\\"scale\\\": \\\"3B\\\"\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-3B_d100_v2_s123_aligned\\\",\\n      \\\"dosage\\\": 100,\\n      \\\"scale\\\": \\\"3B\\\"\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-3B_d100_v2_s42_aligned\\\",\\n      \\\"dosage\\\": 100,\\n      \\\"scale\\\": \\\"3B\\\"\\n    }\\n  ],\\n  \\\"dosages\\\": [\\n    0,\\n    0,\\n    100,\\n    100\\n  ],\\n  \\\"fit_time_sec\\\": 690.0,\\n  \\\"diagnostics\\\": {\\n    \\\"max_rhat\\\": 1.0081,\\n    \\\"rhat_ok\\\": true,\\n    \\\"min_ess\\\": 1058.6,\\n    \\\"ess_ok\\\": true,\\n    \\\"divergent_count\\\": 0,\\n    \\\"divergent_pct\\\": 0.0,\\n    \\\"divergent_ok\\\": true,\\n    \\\"total_draws\\\": 4000,\\n    \\\"all_ok\\\": true\\n  },\\n  \\\"posterior_predictive\\\": {\\n    \\\"overall_ppp\\\": 1.0,\\n    \\\"obs_mean_acc\\\": 0.6266,\\n    \\\"pred_mean_acc\\\": 0.8434,\\n    \\\"residual_mae\\\": 0.2168\\n  },\\n  \\\"gamma\\\": {\\n    \\\"mean\\\": -5.7036,\\n    \\\"sd\\\": 0.3428,\\n    \\\"q025\\\": -6.4061,\\n    \\\"q975\\\": -5.0391,\\n    \\\"q10\\\": -6.1367,\\n    \\\"q90\\\": -5.2713,\\n    \\\"q25\\\": -5.9264,\\n    \\\"q75\\\": -5.471,\\n    \\\"ci_excludes_zero\\\": true\\n  },\\n  \\\"calibrated_scores\\\": {\\n    \\\"mean\\\": [\\n      0.7026,\\n      0.7011,\\n      0.9853,\\n      0.9846\\n    ],\\n    \\\"sd\\\": [\\n    
…[truncated 733 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T16:02:48.693033+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42 -name \"*mmlu*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42 -name \"*mmlu*\""
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T16:02:48.693233+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T16:02:48.693510+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_aligned -name \"*mmlu*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_aligned -name \"*mmlu*\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T16:02:48.693716+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T16:02:48.693912+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_aligned -name \"*mmlu*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_aligned -name \"*mmlu*\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T16:02:48.694111+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.65}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T16:02:48.694303+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_aligned/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_aligned/"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T16:02:48.694528+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"correctness_matrix.json\\neval_results.json\\nitem_responses.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T16:02:48.694740+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_aligned/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_aligned/"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T16:02:48.694954+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"correctness_matrix.json\\neval_results.json\\nitem_responses.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T16:02:48.695152+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_aligned/eval_results.json')); print(json.dumps({k:v for k,v in d.items() if 'mmlu' in k.lower() or 'accuracy' in k.lower() or 'acc' in k.lower()}, indent=2)[:2000])\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_aligned/eval_results.json')); print(json.dumps({k:v for k,v in d.items() if 'mmlu' in k.lower() or 'accuracy' in k.lower() or 'acc' in k.lower()}, indent=2)[:2000])\""
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T16:02:48.695370+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T16:02:48.695584+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_aligned/eval_results.json')); print(json.dumps({k:v for k,v in d.items() if 'mmlu' in k.lower() or 'accuracy' in k.lower() or 'acc' in k.lower()}, indent=2)[:2000])\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_aligned/eval_results.json')); print(json.dumps({k:v for k,v in d.items() if 'mmlu' in k.lower() or 'accuracy' in k.lower() or 'acc' in k.lower()}, indent=2)[:2000])\""
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T16:02:48.695785+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T16:02:48.695996+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_aligned/eval_results.json')); print(json.dumps(d, indent=2)[:3000])\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_aligned/eval_results.json')); print(json.dumps(d, indent=2)[:3000])\""
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T16:02:48.696198+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T16:02:48.696418+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_aligned/eval_results.json')); print(json.dumps(d, indent=2)[:3000])\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_aligned/eval_results.json')); print(json.dumps(d, indent=2)[:3000])\""
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T16:02:48.696622+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T16:02:48.696844+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -100 /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_aligned/eval_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -100 /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_aligned/eval_results.json"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T16:02:48.697152+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B\\\",\\n  \\\"paraphrased\\\": false,\\n  \\\"benchmarks\\\": {\\n    \\\"mmlu\\\": {\\n      \\\"accuracy\\\": 0.6294687366472013,\\n      \\\"correct\\\": 8839,\\n      \\\"total\\\": 14042,\\n      \\\"per_item\\\": [\\n        {\\n          \\\"index\\\": 0,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n        {\\n          \\\"index\\\": 1,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 2,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"D\\\"\\n        },\\n        {\\n          \\\"index\\\": 3,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n        {\\n          \\\"index\\\": 4,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n        {\\n          \\\"index\\\": 5,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"A\\\"\\n        },\\n        {\\n          \\\"index\\\": 6,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"A\\\"\\n        },\\n        {\\n          \\\"index\\\": 7,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"D\\\"\\n        },\\n        {\\n          \\\"index\\\": 8,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n        {\\n          \\\"index\\\": 9,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n   
…[truncated 924 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T16:02:48.697423+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -100 /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_aligned/eval_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -100 /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_aligned/eval_results.json"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T16:02:48.697739+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B\\\",\\n  \\\"paraphrased\\\": false,\\n  \\\"benchmarks\\\": {\\n    \\\"mmlu\\\": {\\n      \\\"accuracy\\\": 0.6319612590799032,\\n      \\\"correct\\\": 8874,\\n      \\\"total\\\": 14042,\\n      \\\"per_item\\\": [\\n        {\\n          \\\"index\\\": 0,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n        {\\n          \\\"index\\\": 1,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 2,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"D\\\"\\n        },\\n        {\\n          \\\"index\\\": 3,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n        {\\n          \\\"index\\\": 4,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n        {\\n          \\\"index\\\": 5,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"A\\\"\\n        },\\n        {\\n          \\\"index\\\": 6,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"A\\\"\\n        },\\n        {\\n          \\\"index\\\": 7,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"D\\\"\\n        },\\n        {\\n          \\\"index\\\": 8,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n        {\\n          \\\"index\\\": 9,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n  
…[truncated 924 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T16:02:48.697984+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -100 /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_aligned/eval_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -100 /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_aligned/eval_results.json"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T16:02:48.698284+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B\\\",\\n  \\\"paraphrased\\\": false,\\n  \\\"benchmarks\\\": {\\n    \\\"mmlu\\\": {\\n      \\\"accuracy\\\": 0.6313915396667141,\\n      \\\"correct\\\": 8866,\\n      \\\"total\\\": 14042,\\n      \\\"per_item\\\": [\\n        {\\n          \\\"index\\\": 0,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n        {\\n          \\\"index\\\": 1,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 2,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"D\\\"\\n        },\\n        {\\n          \\\"index\\\": 3,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n        {\\n          \\\"index\\\": 4,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n        {\\n          \\\"index\\\": 5,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"A\\\"\\n        },\\n        {\\n          \\\"index\\\": 6,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"A\\\"\\n        },\\n        {\\n          \\\"index\\\": 7,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"D\\\"\\n        },\\n        {\\n          \\\"index\\\": 8,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n        {\\n          \\\"index\\\": 9,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n   
…[truncated 923 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T16:02:48.698558+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -100 /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s123_aligned/eval_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -100 /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s123_aligned/eval_results.json"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T16:02:48.698864+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B\\\",\\n  \\\"paraphrased\\\": false,\\n  \\\"benchmarks\\\": {\\n    \\\"mmlu\\\": {\\n      \\\"accuracy\\\": 0.6318900441532546,\\n      \\\"correct\\\": 8873,\\n      \\\"total\\\": 14042,\\n      \\\"per_item\\\": [\\n        {\\n          \\\"index\\\": 0,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n        {\\n          \\\"index\\\": 1,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 2,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"D\\\"\\n        },\\n        {\\n          \\\"index\\\": 3,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n        {\\n          \\\"index\\\": 4,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n        {\\n          \\\"index\\\": 5,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"A\\\"\\n        },\\n        {\\n          \\\"index\\\": 6,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"A\\\"\\n        },\\n        {\\n          \\\"index\\\": 7,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"D\\\"\\n        },\\n        {\\n          \\\"index\\\": 8,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n        {\\n          \\\"index\\\": 9,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n  
…[truncated 924 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T16:02:48.699186+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/autodl-tmp/exp006/results_stratified_irt/scheme_B/scale_1.5B/mmlu_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/autodl-tmp/exp006/results_stratified_irt/scheme_B/scale_1.5B/mmlu_results.json"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T16:02:48.699566+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"stratum\\\": \\\"B_scale_1.5B\\\",\\n  \\\"benchmark\\\": \\\"mmlu\\\",\\n  \\\"n_models\\\": 6,\\n  \\\"n_items\\\": 2000,\\n  \\\"original_n_items\\\": 14042,\\n  \\\"subsampled\\\": true,\\n  \\\"unique_dosages\\\": [\\n    0,\\n    5,\\n    25,\\n    100\\n  ],\\n  \\\"has_dosage_variation\\\": true,\\n  \\\"models\\\": [\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d000_s123_aligned\\\",\\n      \\\"dosage\\\": 0,\\n      \\\"scale\\\": \\\"1.5B\\\"\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d000_s42_aligned\\\",\\n      \\\"dosage\\\": 0,\\n      \\\"scale\\\": \\\"1.5B\\\"\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d005_s42_aligned\\\",\\n      \\\"dosage\\\": 5,\\n      \\\"scale\\\": \\\"1.5B\\\"\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d025_s42_aligned\\\",\\n      \\\"dosage\\\": 25,\\n      \\\"scale\\\": \\\"1.5B\\\"\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d100_s123_aligned\\\",\\n      \\\"dosage\\\": 100,\\n      \\\"scale\\\": \\\"1.5B\\\"\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d100_s42_aligned\\\",\\n      \\\"dosage\\\": 100,\\n      \\\"scale\\\": \\\"1.5B\\\"\\n    }\\n  ],\\n  \\\"dosages\\\": [\\n    0,\\n    0,\\n    5,\\n    25,\\n    100,\\n    100\\n  ],\\n  \\\"fit_time_sec\\\": 1106.2,\\n  \\\"diagnostics\\\": {\\n    \\\"max_rhat\\\": 1.0165,\\n    \\\"rhat_ok\\\": false,\\n    \\\"min_ess\\\": 115.2,\\n    \\\"ess_ok\\\": false,\\n    \\\"divergent_count\\\": 0,\\n    \\\"divergent_pct\\\": 0.0,\\n    \\\"divergent_ok\\\": true,\\n    \\\"total_draws\\\": 4000,\\n    \\\"all_ok\\\": false\\n  },\\n  \\\"posterior_predictive\\\": {\\n    \\\"overall_ppp\\\": 0.0005,\\n    \\\"obs_mean_acc\\\": 0.5772,\\n    \\\"pred_mean_acc\\\": 0.4844,\\n    \\\"residual_mae\\\": 0.0927\\n  },\\n  \\\"gamma\\\": {\\n    \\\"mean\\\": 1.4733,\\n    \\\"sd\\\": 0.5028,\\n    \\\"q025\\\": 0.5516,\
…[truncated 1321 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-15T16:02:48.699979+00:00_

All data collected. Here's the summary:

## 3B MMLU gamma=-5.70 交叉验证报告

### Raw Accuracy

| Model | MMLU Acc |
|-------|---------|
| d000_v2_s42 | 0.6295 |
| d000_v2_s123 | 0.6314 |
| d100_v2_s42 | 0.6320 |
| d100_v2_s123 | 0.6319 |

d000 均值 0.6304，d100 均值 0.6320，差异仅 **+0.16 pp**——几乎持平。

### MCMC 诊断

| 指标 | 3B | 1.5B |
|------|-----|------|
| max_rhat | 1.008 (OK) | 1.017 (NOT OK) |
| min_ess | 1059 (OK) | 115 (NOT OK) |
| divergences | 0 | 0 |
| **residual_mae** | **0.2168** | 0.0927 |
| obs vs pred acc | 0.627 vs **0.843** | 0.577 vs 0.484 |

3B 的 MCMC 采样本身收敛良好，但 **posterior predictive 严重失败**——模型预测均准 0.843，实际 0.627，系统性高估 22 pp。

### 数据不足

- 3B 只有 **4 个模型、2 个 dosage 水平**（d000, d100），无 d005/d025
- 1.5B 有 6 个模型、4 个 dosage 水平，且呈现清晰的剂量-反应关系

### 结论：**(c) 数据不足 + 模型误配导致的噪声**

gamma=-5.70 **不可信**。原因：
1. Raw accuracy 在 d000→d100 几乎无变化（+0.16 pp），不支持任何方向的强效应
2. 仅 2 个 dosage 水平、4 个模型，自由度不足以约束 IRT 参数
3. posterior predictive residual_mae=0.217 暴露严重模型误配——MCMC 收敛到了错误的解
4. 对比 1.5B（4 个 dosage、6 个模型、MAE=0.093），3B 的数据条件远不够支撑 stratified IRT

**建议**：补充 3B d005/d025 的 eval 数据后重新拟合，或对 3B 该 stratum 标记为 "insufficient data"。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_3B_mmlu_gamma_crossval_20260515T160046"
}
```

</details>

---
