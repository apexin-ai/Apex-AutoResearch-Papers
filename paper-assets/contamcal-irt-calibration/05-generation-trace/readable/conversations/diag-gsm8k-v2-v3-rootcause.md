# diag gsm8k v2 v3 rootcause

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 85
- **Recorded user turns:** 0
- **Tool calls:** 42
- **Original source:** `logs/chats/worker_diag_gsm8k-v2-v3-rootcause_20260514T231051.jsonl`
- **Structured JSON:** [`aaa27751883d075eb9af.json`](../../sessions/aa/aaa27751883d075eb9af.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

85 recorded events

### Tool call

_source line 1 · 2026-05-14T23:19:01.830360+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T23:19:01.830908+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T23:19:01.831252+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2/exp006_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2/exp006_results.json"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T23:19:01.831501+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v3_rrf/exp006_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v3_rrf/exp006_results.json"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T23:19:01.831711+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2/ -type f -name \"*.json\" -o -name \"*.csv\" -o -name \"*.npy\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2/ -type f -name \"*.json\" -o -name \"*.csv\" -o -name \"*.npy\""
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T23:19:01.831931+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v3_rrf/ -type f -name \"*.json\" -o -name \"*.csv\" -o -name \"*.npy\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v3_rrf/ -type f -name \"*.json\" -o -name \"*.csv\" -o -name \"*.npy\""
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T23:19:01.832134+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -n \"def build_exposure\\|def load.*signal\\|def.*rrf\\|exposure_matrix\\|tau_matrix\\|def.*dosage\\|signal_type\\|exposure_type\" /root/contamcal-irt-calibration/exp006/run_exp006.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -n \"def build_exposure\\|def load.*signal\\|def.*rrf\\|exposure_matrix\\|tau_matrix\\|def.*dosage\\|signal_type\\|exposure_type\" /root/contamcal-irt-calibration/exp006/run_exp006.py"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T23:19:01.832801+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"metadata\\\": {\\n    \\\"eval_dir\\\": \\\"/root/autodl-tmp/exp001/eval_results\\\",\\n    \\\"model_type\\\": \\\"4pl_gamma\\\",\\n    \\\"dry_run\\\": false,\\n    \\\"models\\\": [\\n      {\\n        \\\"dirname\\\": \\\"Qwen2.5-0.5B_d000_s42_aligned\\\",\\n        \\\"model_name\\\": \\\"Qwen2.5-0.5B\\\",\\n        \\\"dosage\\\": 0,\\n        \\\"seed\\\": 42\\n      },\\n      {\\n        \\\"dirname\\\": \\\"Qwen2.5-0.5B_d005_s42_aligned\\\",\\n        \\\"model_name\\\": \\\"Qwen2.5-0.5B\\\",\\n        \\\"dosage\\\": 5,\\n        \\\"seed\\\": 42\\n      },\\n      {\\n        \\\"dirname\\\": \\\"Qwen2.5-0.5B_d025_s42_aligned\\\",\\n        \\\"model_name\\\": \\\"Qwen2.5-0.5B\\\",\\n        \\\"dosage\\\": 25,\\n        \\\"seed\\\": 42\\n      },\\n      {\\n        \\\"dirname\\\": \\\"Qwen2.5-0.5B_d100_s42_aligned\\\",\\n        \\\"model_name\\\": \\\"Qwen2.5-0.5B\\\",\\n        \\\"dosage\\\": 100,\\n        \\\"seed\\\": 42\\n      },\\n      {\\n        \\\"dirname\\\": \\\"Qwen2.5-1.5B_d000_s42_aligned\\\",\\n        \\\"model_name\\\": \\\"Qwen2.5-1.5B\\\",\\n        \\\"dosage\\\": 0,\\n        \\\"seed\\\": 42\\n      },\\n      {\\n        \\\"dirname\\\": \\\"Qwen2.5-1.5B_d005_s42_aligned\\\",\\n        \\\"model_name\\\": \\\"Qwen2.5-1.5B\\\",\\n        \\\"dosage\\\": 5,\\n        \\\"seed\\\": 42\\n      },\\n      {\\n        \\\"dirname\\\": \\\"Qwen2.5-1.5B_d025_s42_aligned\\\",\\n        \\\"model_name\\\": \\\"Qwen2.5-1.5B\\\",\\n        \\\"dosage\\\": 25,\\n        \\\"seed\\\": 42\\n      },\\n      {\\n        \\\"dirname\\\": \\\"Qwen2.5-1.5B_d100_s42_aligned\\\",\\n        \\\"model_name\\\": \\\"Qwen2.5-1.5B\\\",\\n        \\\"dosage\\\": 100,\\n        \\\"seed\\\": 42\\n      }\\n    ],\\n    \\\"dosages\\\": [\\n      0,\\n      5,\\n      25,\\n      100,\\n      0,\\n      5,\\n      25,\\n      100\\n    ],\\n    \\\"benchmarks\\\": [\\n      \\\"gsm8k\\\
…[truncated 8215 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T23:19:01.833596+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"metadata\\\": {\\n    \\\"eval_dir\\\": \\\"/root/autodl-tmp/exp001/eval_results\\\",\\n    \\\"model_type\\\": \\\"4pl_gamma\\\",\\n    \\\"dry_run\\\": false,\\n    \\\"models\\\": [\\n      {\\n        \\\"dirname\\\": \\\"Qwen2.5-0.5B_d000_s42_aligned\\\",\\n        \\\"model_name\\\": \\\"Qwen2.5-0.5B\\\",\\n        \\\"dosage\\\": 0,\\n        \\\"seed\\\": 42\\n      },\\n      {\\n        \\\"dirname\\\": \\\"Qwen2.5-0.5B_d005_s42_aligned\\\",\\n        \\\"model_name\\\": \\\"Qwen2.5-0.5B\\\",\\n        \\\"dosage\\\": 5,\\n        \\\"seed\\\": 42\\n      },\\n      {\\n        \\\"dirname\\\": \\\"Qwen2.5-0.5B_d025_s42_aligned\\\",\\n        \\\"model_name\\\": \\\"Qwen2.5-0.5B\\\",\\n        \\\"dosage\\\": 25,\\n        \\\"seed\\\": 42\\n      },\\n      {\\n        \\\"dirname\\\": \\\"Qwen2.5-0.5B_d100_s42_aligned\\\",\\n        \\\"model_name\\\": \\\"Qwen2.5-0.5B\\\",\\n        \\\"dosage\\\": 100,\\n        \\\"seed\\\": 42\\n      },\\n      {\\n        \\\"dirname\\\": \\\"Qwen2.5-1.5B_d000_s42_aligned\\\",\\n        \\\"model_name\\\": \\\"Qwen2.5-1.5B\\\",\\n        \\\"dosage\\\": 0,\\n        \\\"seed\\\": 42\\n      },\\n      {\\n        \\\"dirname\\\": \\\"Qwen2.5-1.5B_d005_s42_aligned\\\",\\n        \\\"model_name\\\": \\\"Qwen2.5-1.5B\\\",\\n        \\\"dosage\\\": 5,\\n        \\\"seed\\\": 42\\n      },\\n      {\\n        \\\"dirname\\\": \\\"Qwen2.5-1.5B_d025_s42_aligned\\\",\\n        \\\"model_name\\\": \\\"Qwen2.5-1.5B\\\",\\n        \\\"dosage\\\": 25,\\n        \\\"seed\\\": 42\\n      },\\n      {\\n        \\\"dirname\\\": \\\"Qwen2.5-1.5B_d100_s42_aligned\\\",\\n        \\\"model_name\\\": \\\"Qwen2.5-1.5B\\\",\\n        \\\"dosage\\\": 100,\\n        \\\"seed\\\": 42\\n      }\\n    ],\\n    \\\"dosages\\\": [\\n      0,\\n      5,\\n      25,\\n      100,\\n      0,\\n      5,\\n      25,\\n      100\\n    ],\\n    \\\"benchmarks\\\": [\\n      \\\"gsm8k\\\
…[truncated 8169 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T23:19:01.833882+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2/gsm8k/irt_4pl_gamma.json\\n/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2/gsm8k/baselines.json\\n/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2/gsm8k/ground_truth.json\\n/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2/gsm8k/evaluation.json\\n/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2/joint_fit/joint_fit_results.json\\n/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2/exp006_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T23:19:01.834116+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v3_rrf/gsm8k/irt_4pl_gamma.json\\n/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v3_rrf/gsm8k/baselines.json\\n/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v3_rrf/gsm8k/ground_truth.json\\n/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v3_rrf/gsm8k/evaluation.json\\n/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v3_rrf/exp006_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T23:19:01.834335+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T23:19:01.834647+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -200 /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2/gsm8k/irt_4pl_gamma.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -200 /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2/gsm8k/irt_4pl_gamma.json"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T23:19:01.835116+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"benchmark\\\": \\\"gsm8k\\\",\\n  \\\"model_type\\\": \\\"4pl_gamma\\\",\\n  \\\"method\\\": \\\"nuts\\\",\\n  \\\"stan_file\\\": \\\"contam_irt_4pl_simple.stan\\\",\\n  \\\"n_models\\\": 8,\\n  \\\"n_items\\\": 1319,\\n  \\\"fit_time_sec\\\": 304.6,\\n  \\\"config\\\": {\\n    \\\"chains\\\": 4,\\n    \\\"warmup\\\": 1000,\\n    \\\"samples\\\": 1000,\\n    \\\"adapt_delta\\\": 0.95,\\n    \\\"max_treedepth\\\": 12\\n  },\\n  \\\"diagnostics\\\": {\\n    \\\"max_rhat\\\": 1.0148,\\n    \\\"rhat_ok\\\": false,\\n    \\\"min_ess\\\": 330.2,\\n    \\\"ess_ok\\\": false,\\n    \\\"divergent_count\\\": 0,\\n    \\\"divergent_pct\\\": 0.0,\\n    \\\"divergent_ok\\\": true,\\n    \\\"total_draws\\\": 4000,\\n    \\\"all_ok\\\": false\\n  },\\n  \\\"posterior_predictive\\\": {\\n    \\\"overall_ppp\\\": 0.336,\\n    \\\"obs_mean_acc\\\": 0.5086,\\n    \\\"pred_mean_acc\\\": 0.4995,\\n    \\\"residual_mae\\\": 0.0367\\n  },\\n  \\\"parameters\\\": {\\n    \\\"gamma\\\": {\\n      \\\"mean\\\": 0.1871,\\n      \\\"sd\\\": 0.5687,\\n      \\\"q025\\\": -0.9172,\\n      \\\"q975\\\": 1.3294,\\n      \\\"q10\\\": -0.5196,\\n      \\\"q90\\\": 0.9096,\\n      \\\"q25\\\": -0.1868,\\n      \\\"q75\\\": 0.5454,\\n      \\\"ci_excludes_zero\\\": false\\n    },\\n    \\\"theta\\\": {\\n      \\\"mean\\\": [\\n        -0.8586,\\n        -0.894,\\n        -0.9199,\\n        -1.0198,\\n        0.9938,\\n        0.9195,\\n        0.9131,\\n        0.7995\\n      ],\\n      \\\"sd\\\": [\\n        0.1032,\\n        0.1219,\\n        0.2022,\\n        0.4859,\\n        0.1041,\\n        0.1176,\\n        0.2005,\\n        0.4733\\n      ]\\n    },\\n    \\\"a\\\": {\\n      \\\"mean\\\": [\\n        1.218,\\n        1.3046,\\n        1.3136,\\n        1.0967,\\n        1.2999,\\n        1.314,\\n        1.3168,\\n        1.3228,\\n        1.3346,\\n        1.4589,\\n        0.9852,\\n        0.9657,\\n        1.2318,\\n    
…[truncated 2228 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T23:19:01.835414+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -200 /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v3_rrf/gsm8k/irt_4pl_gamma.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -200 /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v3_rrf/gsm8k/irt_4pl_gamma.json"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T23:19:01.835739+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"benchmark\\\": \\\"gsm8k\\\",\\n  \\\"model_type\\\": \\\"4pl_gamma\\\",\\n  \\\"method\\\": \\\"nuts\\\",\\n  \\\"stan_file\\\": \\\"contam_irt_4pl_simple.stan\\\",\\n  \\\"n_models\\\": 8,\\n  \\\"n_items\\\": 1319,\\n  \\\"fit_time_sec\\\": 303.5,\\n  \\\"config\\\": {\\n    \\\"chains\\\": 4,\\n    \\\"warmup\\\": 1000,\\n    \\\"samples\\\": 1000,\\n    \\\"adapt_delta\\\": 0.95,\\n    \\\"max_treedepth\\\": 12\\n  },\\n  \\\"diagnostics\\\": {\\n    \\\"max_rhat\\\": 1.0085,\\n    \\\"rhat_ok\\\": true,\\n    \\\"min_ess\\\": 491.8,\\n    \\\"ess_ok\\\": true,\\n    \\\"divergent_count\\\": 0,\\n    \\\"divergent_pct\\\": 0.0,\\n    \\\"divergent_ok\\\": true,\\n    \\\"total_draws\\\": 4000,\\n    \\\"all_ok\\\": true\\n  },\\n  \\\"posterior_predictive\\\": {\\n    \\\"overall_ppp\\\": 0.0,\\n    \\\"obs_mean_acc\\\": 0.5086,\\n    \\\"pred_mean_acc\\\": 0.442,\\n    \\\"residual_mae\\\": 0.0786\\n  },\\n  \\\"parameters\\\": {\\n    \\\"gamma\\\": {\\n      \\\"mean\\\": 2.0959,\\n      \\\"sd\\\": 0.6062,\\n      \\\"q025\\\": 0.9681,\\n      \\\"q975\\\": 3.3043,\\n      \\\"q10\\\": 1.3337,\\n      \\\"q90\\\": 2.8867,\\n      \\\"q25\\\": 1.6809,\\n      \\\"q75\\\": 2.4934,\\n      \\\"ci_excludes_zero\\\": true\\n    },\\n    \\\"theta\\\": {\\n      \\\"mean\\\": [\\n        -0.925,\\n        -0.952,\\n        -2.1216,\\n        -1.1375,\\n        0.8814,\\n        0.1463,\\n        0.5974,\\n        -0.6969\\n      ],\\n      \\\"sd\\\": [\\n        0.102,\\n        0.1041,\\n        0.4021,\\n        0.1298,\\n        0.1002,\\n        0.2388,\\n        0.138,\\n        0.466\\n      ]\\n    },\\n    \\\"a\\\": {\\n      \\\"mean\\\": [\\n        1.0248,\\n        1.1637,\\n        1.5148,\\n        1.0734,\\n        1.2281,\\n        1.5279,\\n        1.1495,\\n        1.507,\\n        1.5016,\\n        1.3443,\\n        1.0194,\\n        0.8456,\\n        1.4259,\\n        1.5303,\
…[truncated 2215 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T23:19:01.836011+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -n \"exposure\\|tau\\|signal\\|rrf\\|dosage\" /root/contamcal-irt-calibration/exp006/run_exp006.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -n \"exposure\\|tau\\|signal\\|rrf\\|dosage\" /root/contamcal-irt-calibration/exp006/run_exp006.py"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T23:19:01.836241+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T23:19:01.836507+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -300 /root/contamcal-irt-calibration/exp006/run_exp006.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -300 /root/contamcal-irt-calibration/exp006/run_exp006.py"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T23:19:01.836898+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nexp-006 end-to-end pipeline: IRT calibration + 7 baselines + evaluation.\\n\\nLoads exp-001 eval results and exp-002/003 exposure scores,\\nruns IRT 4PL+gamma calibration and all baselines per benchmark,\\nevaluates against ground-truth clean scores (dosage=0 models).\\n\\nUsage:\\n    python run_exp006.py --help\\n    python run_exp006.py --dry-run --skip-stan --max-items 20    # quick test\\n    python run_exp006.py                                         # full run\\n\\nDependencies: cmdstanpy, numpy, scipy\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport sys\\nimport time\\nfrom pathlib import Path\\n\\nimport numpy as np\\n\\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\\nfrom run_irt_calibration import (\\n    load_eval_results,\\n    load_pooled_eval_results,\\n    load_exposure_scores,\\n    build_exposure_matrix,\\n    run_benchmark_fit,\\n    STAN_MODELS,\\n)\\nfrom baselines import run_all_baselines\\nfrom evaluate_calibration import (\\n    evaluate_method,\\n    format_text_table,\\n    format_latex_table,\\n)\\nfrom joint_fit import run_joint_fit\\n\\nlog = logging.getLogger(__name__)\\n\\n# D018: 3B GSM8K excluded from dose-response analysis\\nD018_EXCLUDE = [(\\\"3B\\\", \\\"gsm8k\\\")]\\nD018_EXCLUDE_RULES = [\\n    {\\\"model\\\": \\\"3B\\\", \\\"benchmark\\\": \\\"gsm8k\\\", \\\"reason\\\": \\\"D018 LoRA damage\\\"},\\n]\\n\\n\\ndef should_exclude_dose_response(model_name, benchmark, rules=D018_EXCLUDE):\\n    \\\"\\\"\\\"Check D018 exclusion rules for dose-response analysis.\\\"\\\"\\\"\\n    for pattern, bench in rules:\\n        if pattern in model_name and benchmark == bench:\\n            return True\\n    return False\\n\\n\\ndef compute_ground_truth(responses, dosages, models=None):\\n    \\\"\\\"\\\"Ground truth = accuracy of dosage-0 models (uncontaminated).\\n\\n    For dosage-0 models, raw accuracy IS the clean
…[truncated 7214 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T23:19:01.837178+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -n \"exposure\\|tau\\|signal\\|rrf\\|dosage\\|delta\" /root/contamcal-irt-calibration/exp006/run_exp006.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -n \"exposure\\|tau\\|signal\\|rrf\\|dosage\\|delta\" /root/contamcal-irt-calibration/exp006/run_exp006.py"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T23:19:01.837445+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T23:19:01.837680+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2/ -name \"*stan*\" -o -name \"*data*\" -o -name \"*input*\" -o -name \"*tau*\" -o -name \"*exposure*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2/ -name \"*stan*\" -o -name \"*data*\" -o -name \"*input*\" -o -name \"*tau*\" -o -name \"*exposure*\""
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T23:19:01.837923+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T23:19:01.838121+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v3_rrf/ -name \"*stan*\" -o -name \"*data*\" -o -name \"*input*\" -o -name \"*tau*\" -o -name \"*exposure*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v3_rrf/ -name \"*stan*\" -o -name \"*data*\" -o -name \"*input*\" -o -name \"*tau*\" -o -name \"*exposure*\""
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T23:19:01.838342+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T23:19:01.838583+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat -n /root/contamcal-irt-calibration/exp006/run_exp006.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat -n /root/contamcal-irt-calibration/exp006/run_exp006.py"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T23:19:01.838982+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"     1\\t\\\"\\\"\\\"\\n     2\\texp-006 end-to-end pipeline: IRT calibration + 7 baselines + evaluation.\\n     3\\t\\n     4\\tLoads exp-001 eval results and exp-002/003 exposure scores,\\n     5\\truns IRT 4PL+gamma calibration and all baselines per benchmark,\\n     6\\tevaluates against ground-truth clean scores (dosage=0 models).\\n     7\\t\\n     8\\tUsage:\\n     9\\t    python run_exp006.py --help\\n    10\\t    python run_exp006.py --dry-run --skip-stan --max-items 20    # quick test\\n    11\\t    python run_exp006.py                                         # full run\\n    12\\t\\n    13\\tDependencies: cmdstanpy, numpy, scipy\\n    14\\t\\\"\\\"\\\"\\n    15\\t\\n    16\\timport argparse\\n    17\\timport json\\n    18\\timport logging\\n    19\\timport os\\n    20\\timport sys\\n    21\\timport time\\n    22\\tfrom pathlib import Path\\n    23\\t\\n    24\\timport numpy as np\\n    25\\t\\n    26\\tsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\\n    27\\tfrom run_irt_calibration import (\\n    28\\t    load_eval_results,\\n    29\\t    load_pooled_eval_results,\\n    30\\t    load_exposure_scores,\\n    31\\t    build_exposure_matrix,\\n    32\\t    run_benchmark_fit,\\n    33\\t    STAN_MODELS,\\n    34\\t)\\n    35\\tfrom baselines import run_all_baselines\\n    36\\tfrom evaluate_calibration import (\\n    37\\t    evaluate_method,\\n    38\\t    format_text_table,\\n    39\\t    format_latex_table,\\n    40\\t)\\n    41\\tfrom joint_fit import run_joint_fit\\n    42\\t\\n    43\\tlog = logging.getLogger(__name__)\\n    44\\t\\n    45\\t# D018: 3B GSM8K excluded from dose-response analysis\\n    46\\tD018_EXCLUDE = [(\\\"3B\\\", \\\"gsm8k\\\")]\\n    47\\tD018_EXCLUDE_RULES = [\\n    48\\t    {\\\"model\\\": \\\"3B\\\", \\\"benchmark\\\": \\\"gsm8k\\\", \\\"reason\\\": \\\"D018 LoRA damage\\\"},\\n    49\\t]\\n    50\\t\\n    51\\t\\n    52\\tdef should_exclude_dose_response(m
…[truncated 7428 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T23:19:01.839237+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -n \"def build_exposure_matrix\\|def load_exposure_scores\\|def.*exposure\" /root/contamcal-irt-calibration/exp006/run_irt_calibration.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -n \"def build_exposure_matrix\\|def load_exposure_scores\\|def.*exposure\" /root/contamcal-irt-calibration/exp006/run_irt_calibration.py"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T23:19:01.839523+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T23:19:01.839786+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "sed -n '100,250p' /root/contamcal-irt-calibration/exp006/run_exp006.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "sed -n '100,250p' /root/contamcal-irt-calibration/exp006/run_exp006.py"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T23:19:01.840041+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T23:19:01.840256+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "sed -n '300,500p' /root/contamcal-irt-calibration/exp006/run_exp006.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "sed -n '300,500p' /root/contamcal-irt-calibration/exp006/run_exp006.py"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T23:19:01.840471+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T23:19:01.840801+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -n \"def build_exposure_matrix\\|def load_exposure\" /root/contamcal-irt-calibration/exp006/run_irt_calibration.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -n \"def build_exposure_matrix\\|def load_exposure\" /root/contamcal-irt-calibration/exp006/run_irt_calibration.py"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T23:19:01.841017+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T23:19:01.841253+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/exp006/run_exp006.py",
  "offset": "100",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/exp006/run_exp006.py",
    "offset": "100",
    "limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T23:19:01.841485+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T23:19:01.841677+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/run_irt_calibration.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/exp006"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/run_irt_calibration.py",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/exp006"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T23:19:01.841862+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/exp006. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-14T23:19:01.842154+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -250 /root/contamcal-irt-calibration/exp006/run_exp006.py | tail -150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -250 /root/contamcal-irt-calibration/exp006/run_exp006.py | tail -150"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-14T23:19:01.842653+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"                log.info(\\\"Ground truth [%s]: d0 mean=%.4f (n=%d)\\\",\\n                         sc, float(raw_acc[sc_d0].mean()), len(sc_d0))\\n    else:\\n        ground_truth = np.full(len(dosages), global_d0_mean)\\n        ground_truth[d0_mask] = raw_acc[d0_mask]\\n\\n    return ground_truth\\n\\n\\ndef load_exp002_signals(signals_dir, models, benchmark, signal_key=None,\\n                        pool_mode=False):\\n    \\\"\\\"\\\"Load exp-002 merged signals -> per-model contamination score.\\n    D023/D030: 3-signal RRF fusion (S1+S2+S4), S2 polarity flipped.\\n    \\\"\\\"\\\"\\n    scores = []\\n    for m in models:\\n        # Strip _aligned/_para suffixes to match signal directory naming\\n        sig_dirname = m[\\\"dirname\\\"].replace(\\\"_para_aligned\\\", \\\"\\\").replace(\\\"_aligned\\\", \\\"\\\").replace(\\\"_para\\\", \\\"\\\")\\n        merged = os.path.join(signals_dir, sig_dirname,\\n                              \\\"signals_merged_{}.json\\\".format(benchmark))\\n        if os.path.exists(merged):\\n            with open(merged) as f:\\n                items = json.load(f)\\n            n = len(items)\\n            rrf = np.zeros(n)\\n            for sig in (\\\"s1_embedding\\\", \\\"s2_minkpp\\\", \\\"s4_selfcritique\\\"):\\n                v = np.array([it.get(sig, 0.0) or 0.0 for it in items])\\n                if sig == \\\"s2_minkpp\\\":\\n                    v = -v\\n                order = np.argsort(-v)\\n                ranks = np.empty(n)\\n                ranks[order] = np.arange(1, n + 1)\\n                rrf += 1.0 / (60 + ranks)\\n            mn, mx = rrf.min(), rrf.max()\\n            rrf = (rrf - mn) / (mx - mn) if mx > mn else rrf\\n            scores.append(float(rrf.mean()))\\n        else:\\n            if pool_mode:\\n                raise RuntimeError(\\n                    f\\\"Signal homogeneity violation: no signals for \\\"\\n                    f\\\"{m['di
…[truncated 6204 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-14T23:19:01.842946+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -500 /root/contamcal-irt-calibration/exp006/run_exp006.py | tail -200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -500 /root/contamcal-irt-calibration/exp006/run_exp006.py | tail -200"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-14T23:19:01.843401+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n    for bench, bench_data in data[\\\"benchmarks\\\"].items():\\n        log.info(\\\"\\\\n\\\" + \\\"=\\\" * 60)\\n        log.info(\\\"BENCHMARK: %s\\\", bench)\\n        log.info(\\\"=\\\" * 60)\\n\\n        responses = bench_data[\\\"responses\\\"]\\n        valid = bench_data[\\\"valid_mask\\\"]\\n        tau = exposure_scores[bench]\\n        n_items = bench_data[\\\"n_items\\\"]\\n\\n        # Filter to valid models\\n        if not valid.all():\\n            responses = responses[valid]\\n            dosages_bench = dosages[valid]\\n            models_bench = [m for m, v in zip(data[\\\"models\\\"], valid) if v]\\n            log.info(\\\"Filtered to %d valid models (of %d)\\\",\\n                     responses.shape[0], len(valid))\\n        else:\\n            dosages_bench = dosages\\n            models_bench = list(data[\\\"models\\\"])\\n\\n        # D018: per-benchmark model exclusion (e.g., 3B excluded from gsm8k)\\n        d018_keep = [i for i, m in enumerate(models_bench)\\n                     if not should_exclude_dose_response(\\n                         m.get(\\\"model_name\\\", m[\\\"dirname\\\"]), bench)]\\n        if len(d018_keep) < len(models_bench):\\n            n_excluded = len(models_bench) - len(d018_keep)\\n            for i, m in enumerate(models_bench):\\n                if i not in d018_keep:\\n                    log.info(\\\"D018: excluding %s from %s\\\", m[\\\"dirname\\\"], bench)\\n            d018_idx = np.array(d018_keep)\\n            responses = responses[d018_idx]\\n            dosages_bench = dosages_bench[d018_idx]\\n            models_bench = [models_bench[i] for i in d018_keep]\\n            log.info(\\\"D018: %d models excluded, %d remaining for %s\\\",\\n                     n_excluded, len(models_bench), bench)\\n\\n        # D023: use exp-002 signals if --signals-dir provided, else oracle dosage\\n        if args.signals_dir:\\n            signal_scores = 
…[truncated 7082 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-14T23:19:01.843662+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -n \"def build_exposure_matrix\\|def load_exposure\" /root/contamcal-irt-calibration/exp006/run_irt_calibration.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -n \"def build_exposure_matrix\\|def load_exposure\" /root/contamcal-irt-calibration/exp006/run_irt_calibration.py"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-14T23:19:01.843870+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"152:def load_exposure_scores(exposure_file, benchmarks_data, model_id=None):\\n195:def build_exposure_matrix(dosages, tau):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-14T23:19:01.844153+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -230 /root/contamcal-irt-calibration/exp006/run_irt_calibration.py | tail -80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -230 /root/contamcal-irt-calibration/exp006/run_irt_calibration.py | tail -80"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-14T23:19:01.844467+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\ndef load_exposure_scores(exposure_file, benchmarks_data, model_id=None):\\n    \\\"\\\"\\\"Load per-benchmark per-item exposure scores tau.\\n\\n    Three tau sources:\\n    1. model_id specified -> extract that model from nested format\\n    2. Flat {bench: [floats]} -> use directly (aggregated or oracle)\\n    3. Nested without model_id -> raise ValueError\\n    \\\"\\\"\\\"\\n    if exposure_file and os.path.exists(exposure_file):\\n        with open(exposure_file) as f:\\n            raw = json.load(f)\\n\\n        first_val = next(iter(raw.values()), None) if raw else None\\n        if isinstance(first_val, dict):\\n            if \\\"exposure_scores\\\" in first_val:\\n                raw = {k: v[\\\"exposure_scores\\\"] for k, v in raw.items()}\\n            else:\\n                if model_id:\\n                    if model_id not in raw:\\n                        raise ValueError(\\n                            f\\\"model_id '{model_id}' not found in exposure file. \\\"\\n                            f\\\"Available: {list(raw.keys())}\\\")\\n                    model_data = raw[model_id]\\n                else:\\n                    raise ValueError(\\n                        f\\\"Nested exposure format with models {list(raw.keys())}. \\\"\\n                        f\\\"Specify --tau-model-id to select one, or use aggregated/oracle tau.\\\")\\n                inner_val = next(iter(model_data.values()), None)\\n                if isinstance(inner_val, dict) and \\\"exposure_scores\\\" in inner_val:\\n                    raw = {b: d[\\\"exposure_scores\\\"] for b, d in model_data.items()}\\n                elif isinstance(inner_val, list):\\n                    raw = model_data\\n\\n        exposure = {}\\n        for bench in benchmarks_data:\\n            if bench in raw:\\n                exposure[bench] = np.array(raw[bench], dtype=float)\\n            else:\\n                exposure[bench] = np.on
…[truncated 2015 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-14T23:19:01.844717+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cd /root/contamcal-irt-calibration && git log --oneline -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cd /root/contamcal-irt-calibration && git log --oneline -30"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-14T23:19:01.844925+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"cfd317e fix: clean dead code and add valid-mask assertion in joint_fit.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-14T23:19:01.845137+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "python3 -c \"\nimport json, numpy as np, os\n\n# Load v2 evaluation to find calibrated scores\nv2_eval = '/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2/gsm8k/evaluation.json'\nv3_eval = '/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v3_rrf/gsm8k/evaluation.json'\n\nfor ver, path in [('v2', v2_eval), ('v3_rrf', v3_eval)]:\n    if os.path.exists(path):\n        with open(path) as f:\n            data = json.load(f)\n        for m in data:\n            if 'IRT' in m.get('method',''):\n                print(f'{ver} IRT: scores={m.get(\\\"calibrated_scores\\\",\\\"N/A\\\")[:8]}...')\n                break\n    else:\n        print(f'{ver}: no evaluation.json')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "python3 -c \"\nimport json, numpy as np, os\n\n# Load v2 evaluation to find calibrated scores\nv2_eval = '/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2/gsm8k/evaluation.json'\nv3_eval = '/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v3_rrf/gsm8k/evaluation.json'\n\nfor ver, path in [('v2', v2_eval), ('v3_rrf', v3_eval)]:\n    if os.path.exists(path):\n        with open(path) as f:\n            data = json.load(f)\n        for m in data:\n            if 'IRT' in m.get('method',''):\n                print(f'{ver} IRT: scores={m.get(\\\"calibrated_scores\\\",\\\"N/A\\\")[:8]}...')\n                break\n    else:\n        print(f'{ver}: no evaluation.json')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-14T23:19:01.845391+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'python3 -c \\\"\\\\nimport json, numpy as np, os\\\\n\\\\n# Load v2 evaluation to find calibrated scores\\\\nv2_eval = \\\\'/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2/gsm8k/evaluation.json\\\\'\\\\nv3_eval = \\\\'/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v3_rrf/gsm8k/evaluation.json\\\\'\\\\n\\\\nfor ver, path in [(\\\\'v2\\\\', v2_eval), (\\\\'v3_rrf\\\\', v3_eval)]:\\\\n    if os.path.exists(path):\\\\n        with open(path) as f:\\\\n            data = json.load(f)\\\\n        for m in data:\\\\n            if \\\\'IRT\\\\' in m.get(\\\\'method\\\\',\\\\'\\\\'):\\\\n                print(f\\\\'{ver} IRT: scores={m.get(\\\\\\\\\\\"calibrated_scores\\\\\\\\\\\",\\\\\\\\\\\"N/A\\\\\\\\\\\")[:8]}...\\\\')\\\\n                break\\\\n    else:\\\\n        print(f\\\\'{ver}: no evaluation.json\\\\')\\\\n\\\"\\\\n'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-14T23:19:01.845728+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cd /root/contamcal-irt-calibration && git log --all --oneline | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cd /root/contamcal-irt-calibration && git log --all --oneline | head -50"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-14T23:19:01.845945+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"cfd317e fix: clean dead code and add valid-mask assertion in joint_fit.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.82}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-14T23:19:01.846157+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json, numpy as np, os, sys\nsys.path.insert(0, '/root/contamcal-irt-calibration/exp006')\n\nsignals_dir = '/root/autodl-tmp/exp002/signals'\nmodels = [\n    {'dirname': 'Qwen2.5-0.5B_d000_s42_aligned', 'model_name': 'Qwen2.5-0.5B', 'dosage': 0, 'scale': '0.5B'},\n    {'dirname': 'Qwen2.5-0.5B_d005_s42_aligned', 'model_name': 'Qwen2.5-0.5B', 'dosage': 5, 'scale': '0.5B'},\n    {'dirname': 'Qwen2.5-0.5B_d025_s42_aligned', 'model_name': 'Qwen2.5-0.5B', 'dosage': 25, 'scale': '0.5B'},\n    {'dirname': 'Qwen2.5-0.5B_d100_s42_aligned', 'model_name': 'Qwen2.5-0.5B', 'dosage': 100, 'scale': '0.5B'},\n    {'dirname': 'Qwen2.5-1.5B_d000_s42_aligned', 'model_name': 'Qwen2.5-1.5B', 'dosage': 0, 'scale': '1.5B'},\n    {'dirname': 'Qwen2.5-1.5B_d005_s42_aligned', 'model_name': 'Qwen2.5-1.5B', 'dosage': 5, 'scale': '1.5B'},\n    {'dirname': 'Qwen2.5-1.5B_d025_s42_aligned', 'model_name': 'Qwen2.5-1.5B', 'dosage': 25, 'scale': '1.5B'},\n    {'dirname': 'Qwen2.5-1.5B_d100_s42_aligned', 'model_name': 'Qwen2.5-1.5B', 'dosage': 100, 'scale': '1.5B'},\n]\n\nbenchmark = 'gsm8k'\n\n# Compute RRF scores (same as load_exp002_signals)\nraw_scores = []\nfor m in models:\n    sig_dirname = m['dirname'].replace('_para_aligned', '').replace('_aligned', '').replace('_para', '')\n    merged = os.path.join(signals_dir, sig_dirname, f'signals_merged_{benchmark}.json')\n    if os.path.exists(merged):\n        with open(merged) as f:\n            items = json.load(f)\n        n = len(items)\n        rrf = np.zeros(n)\n        for sig in ('s1_embedding', 's2_minkpp', 's4_selfcritique'):\n            v = np.array([it.get(sig, 0.0) or 0.0 for it in items])\n            if sig == 's2_minkpp':\n                v = -v\n            order = np.argsort(-v)\n            ranks = np.empty(n)\n            ranks[order] = np.arange(1, n + 1)\n            rrf += 1.0 / (60 + ranks)\n        mn, mx = rrf.min(), rrf.max()\n        rrf_norm = (rrf - mn) / (mx - mn) if mx > mn else rrf\n        raw_scores.append(float(rrf_norm.mean()))\n        print(f'{m[\\\"dirname\\\"]}: raw_rrf_mean={rrf_norm.mean():.6f}')\n    else:\n        print(f'{m[\\\"dirname\\\"]}: MISSING signal file at {merged}')\n        raw_scores.append(None)\n\nscores = np.array(raw_scores)\n\n# D024 delta per scale\nprint()\nfor sc in ['0.5B', '1.5B']:\n    s_mask = np.array([m.get('scale','') == sc for m in models])\n    d0s_mask = np.array([m['dosage'] == 0 and m.get('scale','') == sc for m in models])\n    bl = float(scores[d0s_mask].mean())\n    print(f'D024 delta [{sc}]: d000 baseline = {bl:.6f}')\n    delta = scores[s_mask] - bl\n    delta_clipped = np.clip(delta, 0, None)\n    for i, idx in enumerate(np.where(s_mask)[0]):\n        print(f'  {models[idx][\\\"dirname\\\"]}: raw={scores[idx]:.6f}, delta={delta[i]:.6f}, clipped={delta_clipped[i]:.6f}')\n\n# Final exposure (after delta + clip)\ndelta_scores = scores.copy()\nfor sc in ['0.5B', '1.5B']:\n    s_mask = np.array([m.get('scale','') == sc for m in models])\n    d0s_mask = np.array([m['dosage'] == 0 and m.get('scale','') == sc for m in models])\n    bl = float(scores[d0s_mask].mean())\n    delta_scores[s_mask] -= bl\ndelta_scores = np.clip(delta_scores, 0, None)\n\nprint(f'\\nFinal signal exposure values: {delta_scores.tolist()}')\nprint(f'Max signal: {delta_scores.max():.6f}')\nprint(f'Normalized: {(delta_scores / delta_scores.max()).tolist() if delta_scores.max() > 0 else delta_scores.tolist()}')\n\n# Compare with oracle dosage\noracle = np.array([0, 5, 25, 100, 0, 5, 25, 100], dtype=float)\noracle_norm = oracle / oracle.max()\nprint(f'\\nOracle dosage normalized: {oracle_norm.tolist()}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json, numpy as np, os, sys\nsys.path.insert(0, '/root/contamcal-irt-calibration/exp006')\n\nsignals_dir = '/root/autodl-tmp/exp002/signals'\nmodels = [\n    {'dirname': 'Qwen2.5-0.5B_d000_s42_aligned', 'model_name': 'Qwen2.5-0.5B', 'dosage': 0, 'scale': '0.5B'},\n    {'dirname': 'Qwen2.5-0.5B_d005_s42_aligned', 'model_name': 'Qwen2.5-0.5B', 'dosage': 5, 'scale': '0.5B'},\n    {'dirname': 'Qwen2.5-0.5B_d025_s42_aligned', 'model_name': 'Qwen2.5-0.5B', 'dosage': 25, 'scale': '0.5B'},\n    {'dirname': 'Qwen2.5-0.5B_d100_s42_aligned', 'model_name': 'Qwen2.5-0.5B', 'dosage': 100, 'scale': '0.5B'},\n    {'dirname': 'Qwen2.5-1.5B_d000_s42_aligned', 'model_name': 'Qwen2.5-1.5B', 'dosage': 0, 'scale': '1.5B'},\n    {'dirname': 'Qwen2.5-1.5B_d005_s42_aligned', 'model_name': 'Qwen2.5-1.5B', 'dosage': 5, 'scale': '1.5B'},\n    {'dirname': 'Qwen2.5-1.5B_d025_s42_aligned', 'model_name': 'Qwen2.5-1.5B', 'dosage': 25, 'scale': '1.5B'},\n    {'dirname': 'Qwen2.5-1.5B_d100_s42_aligned', 'model_name': 'Qwen2.5-1.5B', 'dosage': 100, 'scale': '1.5B'},\n]\n\nbenchmark = 'gsm8k'\n\n# Compute RRF scores (same as load_exp002_signals)\nraw_scores = []\nfor m in models:\n    sig_dirname = m['dirname'].replace('_para_aligned', '').replace('_aligned', '').replace('_para', '')\n    merged = os.path.join(signals_dir, sig_dirname, f'signals_merged_{benchmark}.json')\n    if os.path.exists(merged):\n        with open(merged) as f:\n            items = json.load(f)\n        n = len(items)\n        rrf = np.zeros(n)\n        for sig in ('s1_embedding', 's2_minkpp', 's4_selfcritique'):\n            v = np.array([it.get(sig, 0.0) or 0.0 for it in items])\n            if sig == 's2_minkpp':\n                v = -v\n            order = np.argsort(-v)\n            ranks = np.empty(n)\n            ranks[order] = np.arange(1, n + 1)\n            rrf += 1.0 / (60 + ranks)\n        mn, mx = rrf.min(), rrf.max()\n        rrf_norm = (rrf - mn) / (mx - mn) if mx > mn else rrf\n        raw_scores.append(float(rrf_norm.mean()))\n        print(f'{m[\\\"dirname\\\"]}: raw_rrf_mean={rrf_norm.mean():.6f}')\n    else:\n        print(f'{m[\\\"dirname\\\"]}: MISSING signal file at {merged}')\n        raw_scores.append(None)\n\nscores = np.array(raw_scores)\n\n# D024 delta per scale\nprint()\nfor sc in ['0.5B', '1.5B']:\n    s_mask = np.array([m.get('scale','') == sc for m in models])\n    d0s_mask = np.array([m['dosage'] == 0 and m.get('scale','') == sc for m in models])\n    bl = float(scores[d0s_mask].mean())\n    print(f'D024 delta [{sc}]: d000 baseline = {bl:.6f}')\n    delta = scores[s_mask] - bl\n    delta_clipped = np.clip(delta, 0, None)\n    for i, idx in enumerate(np.where(s_mask)[0]):\n        print(f'  {models[idx][\\\"dirname\\\"]}: raw={scores[idx]:.6f}, delta={delta[i]:.6f}, clipped={delta_clipped[i]:.6f}')\n\n# Final exposure (after delta + clip)\ndelta_scores = scores.copy()\nfor sc in ['0.5B', '1.5B']:\n    s_mask = np.array([m.get('scale','') == sc for m in models])\n    d0s_mask = np.array([m['dosage'] == 0 and m.get('scale','') == sc for m in models])\n    bl = float(scores[d0s_mask].mean())\n    delta_scores[s_mask] -= bl\ndelta_scores = np.clip(delta_scores, 0, None)\n\nprint(f'\\nFinal signal exposure values: {delta_scores.tolist()}')\nprint(f'Max signal: {delta_scores.max():.6f}')\nprint(f'Normalized: {(delta_scores / delta_scores.max()).tolist() if delta_scores.max() > 0 else delta_scores.tolist()}')\n\n# Compare with oracle dosage\noracle = np.array([0, 5, 25, 100, 0, 5, 25, 100], dtype=float)\noracle_norm = oracle / oracle.max()\nprint(f'\\nOracle dosage normalized: {oracle_norm.tolist()}')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-14T23:19:01.846452+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Qwen2.5-0.5B_d000_s42_aligned: raw_rrf_mean=0.188196\\nQwen2.5-0.5B_d005_s42_aligned: raw_rrf_mean=0.153421\\nQwen2.5-0.5B_d025_s42_aligned: raw_rrf_mean=0.209440\\nQwen2.5-0.5B_d100_s42_aligned: raw_rrf_mean=0.191921\\nQwen2.5-1.5B_d000_s42_aligned: raw_rrf_mean=0.163701\\nQwen2.5-1.5B_d005_s42_aligned: raw_rrf_mean=0.177263\\nQwen2.5-1.5B_d025_s42_aligned: raw_rrf_mean=0.168537\\nQwen2.5-1.5B_d100_s42_aligned: raw_rrf_mean=0.194634\\n\\nD024 delta [0.5B]: d000 baseline = 0.188196\\n  Qwen2.5-0.5B_d000_s42_aligned: raw=0.188196, delta=0.000000, clipped=0.000000\\n  Qwen2.5-0.5B_d005_s42_aligned: raw=0.153421, delta=-0.034776, clipped=0.000000\\n  Qwen2.5-0.5B_d025_s42_aligned: raw=0.209440, delta=0.021244, clipped=0.021244\\n  Qwen2.5-0.5B_d100_s42_aligned: raw=0.191921, delta=0.003724, clipped=0.003724\\nD024 delta [1.5B]: d000 baseline = 0.163701\\n  Qwen2.5-1.5B_d000_s42_aligned: raw=0.163701, delta=0.000000, clipped=0.000000\\n  Qwen2.5-1.5B_d005_s42_aligned: raw=0.177263, delta=0.013563, clipped=0.013563\\n  Qwen2.5-1.5B_d025_s42_aligned: raw=0.168537, delta=0.004837, clipped=0.004837\\n  Qwen2.5-1.5B_d100_s42_aligned: raw=0.194634, delta=0.030933, clipped=0.030933\\n\\nFinal signal exposure values: [0.0, 0.0, 0.02124370865044528, 0.003724473286148, 0.0, 0.013562952154610147, 0.0048367790126401244, 0.03093336697462057]\\nMax signal: 0.030933\\nNormalized: [0.0, 0.0, 0.6867570758745657, 0.12040310028985084, 0.0, 0.43845702815790916, 0.1563612204454977, 1.0]\\n\\nOracle dosage normalized: [0.0, 0.05, 0.25, 1.0, 0.0, 0.05, 0.25, 1.0]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-14T23:19:01.846804+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -la /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2/exp006_results.json /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v3_rrf/exp006_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -la /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2/exp006_results.json /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v3_rrf/exp006_results.json"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-14T23:19:01.847060+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 269767 May 15 06:22 /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2/exp006_results.json\\n-rw-r--r-- 1 root root 271547 May 15 06:57 /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v3_rrf/exp006_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-14T23:19:01.847293+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cd /root/contamcal-irt-calibration && git log --all --format='%H %ai %s' | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cd /root/contamcal-irt-calibration && git log --all --format='%H %ai %s' | head -20"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-14T23:19:01.847553+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"cfd317ead11afa179904125571c9ce8e3acbe382 2026-05-15 06:55:28 +0800 fix: clean dead code and add valid-mask assertion in joint_fit.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-14T23:19:01.847752+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cd /root/contamcal-irt-calibration && git reflog | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cd /root/contamcal-irt-calibration && git reflog | head -20"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-14T23:19:01.848042+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"cfd317e HEAD@{0}: commit (initial): fix: clean dead code and add valid-mask assertion in joint_fit.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-14T23:19:01.848290+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -n \"exposure_file\\|tau.model.id\" /root/contamcal-irt-calibration/exp006/run_exp006.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -n \"exposure_file\\|tau.model.id\" /root/contamcal-irt-calibration/exp006/run_exp006.py"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-14T23:19:01.848526+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"189:        args.exposure_file, data[\\\"benchmarks\\\"], model_id=args.tau_model_id)\\n284:        print(f\\\"[DRY-RUN] Exposure file: {args.exposure_file or 'None (oracle dosage)'}\\\")\\n512:            args.eval_dir, args.exposure_file, str(joint_dir),\\n519:            tau_model_id=args.tau_model_id,\\n564:        \\\"--tau-model-id\\\", type=str, default=None,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-14T23:19:01.848848+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -570 /root/contamcal-irt-calibration/exp006/run_exp006.py | tail -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -570 /root/contamcal-irt-calibration/exp006/run_exp006.py | tail -30"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-14T23:19:01.849348+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    log.info(\\\"Pipeline complete in %.1fs\\\", total_time)\\n    log.info(\\\"Results saved to %s\\\", output_dir)\\n    log.info(\\\"=\\\" * 60)\\n\\n    return combined\\n\\n\\n# ── CLI ──\\n\\ndef main():\\n    parser = argparse.ArgumentParser(\\n        description=\\\"exp-006: IRT calibration + baselines + evaluation\\\")\\n\\n    # Data\\n    parser.add_argument(\\n        \\\"--eval-dir\\\", type=str,\\n        default=\\\"/root/autodl-tmp/exp001/eval_results\\\",\\n        help=\\\"exp-001 eval results directory\\\")\\n    parser.add_argument(\\n        \\\"--exposure-file\\\", type=str, default=None,\\n        help=\\\"exp-002/003 exposure scores JSON \\\"\\n             \\\"(per-benchmark per-item tau)\\\")\\n    parser.add_argument(\\n        \\\"--tau-model-id\\\", type=str, default=None,\\n        help=\\\"Model ID for exposure tau (e.g. Qwen2.5-0.5B_d100_s42)\\\")\\n    # D023: exp-002 signal-based exposure\\n    parser.add_argument(\\n        \\\"--signals-dir\\\", type=str, default=None,\\n        help=\\\"exp-002 signals directory. When set, uses detected contamination \\\"\\n             \\\"signals instead of oracle dosage for exposure (D023)\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-14T23:19:01.849630+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp006/ -name \"*.log\" -newer /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2/exp006_results.json -o -name \"*.sh\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/exp006/ -name \"*.log\" -newer /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2/exp006_results.json -o -name \"*.sh\" | head -20"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-14T23:19:01.849872+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp006/results_pooled_05B_15B_arc_v2/run.log\\n/root/autodl-tmp/exp006/results_pooled_05B_15B_mmlu_v2/run.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-14T23:19:01.850103+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp006/ -maxdepth 1 -name \"run_*.sh\" -o -name \"*.sh\" -o -name \"*.log\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/exp006/ -maxdepth 1 -name \"run_*.sh\" -o -name \"*.sh\" -o -name \"*.log\" | head -20"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-14T23:19:01.850332+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp006/exp006_05B_v1.log\\n/root/autodl-tmp/exp006/exp006_sanity_300.log\\n/root/autodl-tmp/exp006/exp006_gsm8k_nuts.log\\n/root/autodl-tmp/exp006/exp006_arc_nuts.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-14T23:19:01.850812+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2/ -name \"*.log\" && find /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v3_rrf/ -name \"*.log\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2/ -name \"*.log\" && find /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v3_rrf/ -name \"*.log\""
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-14T23:19:01.851029+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2/run.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-14T23:19:01.851229+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2/run.log 2>/dev/null | head -30; echo \"---\"; cat /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v3_rrf/run.log 2>/dev/null | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2/run.log 2>/dev/null | head -30; echo \"---\"; cat /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v3_rrf/run.log 2>/dev/null | head -30"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-14T23:19:01.851489+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-15 06:00:24,881 [INFO] Cross-scale pooling: scales=['0.5B', '1.5B']\\n2026-05-15 06:00:24,883 [INFO] Skipping non-aligned dir: Qwen2.5-0.5B_d000_s123\\n2026-05-15 06:00:24,883 [INFO] Skipping non-aligned dir: Qwen2.5-0.5B_d000_s42\\n2026-05-15 06:00:24,883 [INFO] Skipping non-aligned dir: Qwen2.5-0.5B_d005_s42\\n2026-05-15 06:00:24,883 [INFO] Skipping non-aligned dir: Qwen2.5-0.5B_d100_s42\\n2026-05-15 06:00:24,883 [INFO] Skipping non-aligned dir: Qwen2.5-1.5B_d000_s123\\n2026-05-15 06:00:24,883 [INFO] Skipping non-aligned dir: Qwen2.5-1.5B_d000_s42\\n2026-05-15 06:00:24,883 [INFO] Skipping dir (scale mismatch): Qwen2.5-1.5B_d000_s42_aligned\\n2026-05-15 06:00:24,883 [INFO] Skipping dir (scale mismatch): Qwen2.5-1.5B_d005_s42_aligned\\n2026-05-15 06:00:24,883 [INFO] Skipping dir (scale mismatch): Qwen2.5-1.5B_d025_s42_aligned\\n2026-05-15 06:00:24,883 [INFO] Skipping non-aligned dir: Qwen2.5-1.5B_d100_s42\\n2026-05-15 06:00:24,883 [INFO] Skipping dir (scale mismatch): Qwen2.5-1.5B_d100_s42_aligned\\n2026-05-15 06:00:24,883 [INFO] Skipping non-aligned dir: Qwen2.5-3B_d000_s123\\n2026-05-15 06:00:24,883 [INFO] Skipping non-aligned dir: Qwen2.5-3B_d000_s42\\n2026-05-15 06:00:24,883 [INFO] Skipping dir (scale mismatch): Qwen2.5-3B_d000_s42_aligned\\n2026-05-15 06:00:24,883 [INFO] Skipping dir (scale mismatch): Qwen2.5-3B_d005_s42_aligned\\n2026-05-15 06:00:24,883 [INFO] Skipping dir (scale mismatch): Qwen2.5-3B_d100_s42_aligned\\n2026-05-15 06:00:24,883 [WARNING] Skipping unrecognized dir: Qwen2.5-3B_raw\\n2026-05-15 06:00:24,883 [INFO] Found 4 model evaluations\\n2026-05-15 06:00:24,906 [INFO] Benchmarks: ['gsm8k']\\n2026-05-15 06:00:25,016 [INFO] Pool scale 0.5B: 4 models, dosages=[0, 5, 25, 100]\\n2026-05-15 06:00:25,017 [INFO] Skipping non-aligned dir: Qwen2.5-0.5B_d000_s123\\n2026-05-15 06:00:25,017 [INFO] Skipping non-aligned dir: Qwen2.5-0.5B_d000_s42\\n2026-05-15 06:00:25,017 [INFO] Skipping dir (sc
…[truncated 683 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-14T23:19:01.851709+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2/ /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v3_rrf/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2/ /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v3_rrf/"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-14T23:19:01.851896+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2/:\\nexp006_results.json\\ngsm8k\\njoint_fit\\nrun.log\\n\\n/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v3_rrf/:\\nexp006_results.json\\ngsm8k\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-14T23:19:01.852146+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -i \"exposure\\|signal\\|tau\\|D024\\|dosage\\|oracle\" /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2/run.log | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -i \"exposure\\|signal\\|tau\\|D024\\|dosage\\|oracle\" /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2/run.log | head -30"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-14T23:19:01.852373+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-15 06:00:25,016 [INFO] Pool scale 0.5B: 4 models, dosages=[0, 5, 25, 100]\\n2026-05-15 06:00:25,122 [INFO] Pool scale 1.5B: 4 models, dosages=[0, 5, 25, 100]\\n2026-05-15 06:00:25,122 [INFO] Dosages: [0, 5, 25, 100, 0, 5, 25, 100]\\n2026-05-15 06:00:25,152 [INFO] D024 delta [1.5B]: d000 baseline = 0.6131\\n2026-05-15 06:00:25,152 [INFO] D024 delta [0.5B]: d000 baseline = 0.6131\\n2026-05-15 06:00:25,152 [INFO] Using exp-002 signals as exposure (D024 delta): [0.0, 0.016035002456459613, 0.06481043706345135, 0.1972007393565839, 0.0, 0.016035002456459613, 0.06481043706345135, 0.1972007393565839]\\n2026-05-15 06:07:25,993 [INFO] Running B2_2pl_gamma: Single-signal 2PL+gamma IRT\\n2026-05-15 06:14:36,922 [INFO] Running B4_linear_regression: Linear exposure regression + bootstrap CI\\n2026-05-15 06:14:37,125 [INFO] B5: exposure-weighted downweighting (no rephrased data)\\n2026-05-15 06:14:40,203 [INFO] Pool scale 0.5B: 4 models, dosages=[0, 5, 25, 100]\\n2026-05-15 06:14:40,264 [INFO] Pool scale 1.5B: 4 models, dosages=[0, 5, 25, 100]\\nMethod                              MAE      ECE    Brier    C50    C80    C95      S95    tau  gamma>0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-14T23:19:01.852567+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -80 /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2/run.log | tail -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -80 /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2/run.log | tail -50"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-14T23:19:01.852832+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-15 06:00:25,018 [INFO] Skipping non-aligned dir: Qwen2.5-1.5B_d000_s42\\n2026-05-15 06:00:25,018 [INFO] Skipping non-aligned dir: Qwen2.5-1.5B_d100_s42\\n2026-05-15 06:00:25,018 [INFO] Skipping non-aligned dir: Qwen2.5-3B_d000_s123\\n2026-05-15 06:00:25,018 [INFO] Skipping non-aligned dir: Qwen2.5-3B_d000_s42\\n2026-05-15 06:00:25,018 [INFO] Skipping dir (scale mismatch): Qwen2.5-3B_d000_s42_aligned\\n2026-05-15 06:00:25,018 [INFO] Skipping dir (scale mismatch): Qwen2.5-3B_d005_s42_aligned\\n2026-05-15 06:00:25,018 [INFO] Skipping dir (scale mismatch): Qwen2.5-3B_d100_s42_aligned\\n2026-05-15 06:00:25,018 [WARNING] Skipping unrecognized dir: Qwen2.5-3B_raw\\n2026-05-15 06:00:25,018 [INFO] Found 4 model evaluations\\n2026-05-15 06:00:25,035 [INFO] Benchmarks: ['gsm8k']\\n2026-05-15 06:00:25,122 [INFO] Pool scale 1.5B: 4 models, dosages=[0, 5, 25, 100]\\n2026-05-15 06:00:25,122 [INFO] Models: 8 | Benchmarks: ['gsm8k']\\n2026-05-15 06:00:25,122 [INFO] Dosages: [0, 5, 25, 100, 0, 5, 25, 100]\\n2026-05-15 06:00:25,122 [INFO] \\n============================================================\\n2026-05-15 06:00:25,122 [INFO] BENCHMARK: gsm8k\\n2026-05-15 06:00:25,122 [INFO] ============================================================\\n2026-05-15 06:00:25,152 [INFO] D024 delta [1.5B]: d000 baseline = 0.6131\\n2026-05-15 06:00:25,152 [INFO] D024 delta [0.5B]: d000 baseline = 0.6131\\n2026-05-15 06:00:25,152 [INFO] Using exp-002 signals as exposure (D024 delta): [0.0, 0.016035002456459613, 0.06481043706345135, 0.1972007393565839, 0.0, 0.016035002456459613, 0.06481043706345135, 0.1972007393565839]\\n2026-05-15 06:00:25,153 [INFO] --- IRT Calibration (4pl_gamma) ---\\n2026-05-15 06:00:25,153 [INFO] === gsm8k: 8 models x 1319 items ===\\n2026-05-15 06:00:25,153 [INFO] Mean accuracy: 0.509\\n2026-05-15 06:00:25,153 [INFO] Compiling Stan model: contam_irt_4pl_simple.stan\\n2026-05-15 06:00:25,186 [INFO] Fitting: 8 model
…[truncated 2117 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-14T23:19:01.853152+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json, numpy as np\n\n# v2 run.log shows these exposure values:\nv2_exposure = [0.0, 0.016035, 0.064810, 0.197201, 0.0, 0.016035, 0.064810, 0.197201]\n# v3_rrf computed from current code:\nv3_exposure = [0.0, 0.0, 0.021244, 0.003724, 0.0, 0.013563, 0.004837, 0.030933]\n\nlabels = ['0.5B_d000', '0.5B_d005', '0.5B_d025', '0.5B_d100',\n          '1.5B_d000', '1.5B_d005', '1.5B_d025', '1.5B_d100']\n\nprint('Model           v2_exposure   v3_exposure   v2_norm       v3_norm')\nprint('-'*75)\nmax_v2 = max(v2_exposure)\nmax_v3 = max(v3_exposure)\nfor i, label in enumerate(labels):\n    v2n = v2_exposure[i] / max_v2 if max_v2 > 0 else 0\n    v3n = v3_exposure[i] / max_v3 if max_v3 > 0 else 0\n    print(f'{label:15s} {v2_exposure[i]:.6f}     {v3_exposure[i]:.6f}     {v2n:.4f}       {v3n:.4f}')\n\n# Check monotonicity\nprint()\noracle = [0, 5, 25, 100, 0, 5, 25, 100]\nfor name, vals in [('v2', v2_exposure), ('v3_rrf', v3_exposure), ('oracle', oracle)]:\n    mono_05 = all(vals[i] <= vals[i+1] for i in range(3))\n    mono_15 = all(vals[i] <= vals[i+1] for i in range(4,7))\n    print(f'{name}: 0.5B monotonic={mono_05}, 1.5B monotonic={mono_15}')\n\n# Spearman correlation with oracle\nfrom scipy.stats import spearmanr\noracle_arr = np.array(oracle, dtype=float)\nfor name, vals in [('v2', v2_exposure), ('v3_rrf', v3_exposure)]:\n    r, p = spearmanr(oracle_arr, vals)\n    print(f'{name} vs oracle: Spearman r={r:.4f}, p={p:.4f}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json, numpy as np\n\n# v2 run.log shows these exposure values:\nv2_exposure = [0.0, 0.016035, 0.064810, 0.197201, 0.0, 0.016035, 0.064810, 0.197201]\n# v3_rrf computed from current code:\nv3_exposure = [0.0, 0.0, 0.021244, 0.003724, 0.0, 0.013563, 0.004837, 0.030933]\n\nlabels = ['0.5B_d000', '0.5B_d005', '0.5B_d025', '0.5B_d100',\n          '1.5B_d000', '1.5B_d005', '1.5B_d025', '1.5B_d100']\n\nprint('Model           v2_exposure   v3_exposure   v2_norm       v3_norm')\nprint('-'*75)\nmax_v2 = max(v2_exposure)\nmax_v3 = max(v3_exposure)\nfor i, label in enumerate(labels):\n    v2n = v2_exposure[i] / max_v2 if max_v2 > 0 else 0\n    v3n = v3_exposure[i] / max_v3 if max_v3 > 0 else 0\n    print(f'{label:15s} {v2_exposure[i]:.6f}     {v3_exposure[i]:.6f}     {v2n:.4f}       {v3n:.4f}')\n\n# Check monotonicity\nprint()\noracle = [0, 5, 25, 100, 0, 5, 25, 100]\nfor name, vals in [('v2', v2_exposure), ('v3_rrf', v3_exposure), ('oracle', oracle)]:\n    mono_05 = all(vals[i] <= vals[i+1] for i in range(3))\n    mono_15 = all(vals[i] <= vals[i+1] for i in range(4,7))\n    print(f'{name}: 0.5B monotonic={mono_05}, 1.5B monotonic={mono_15}')\n\n# Spearman correlation with oracle\nfrom scipy.stats import spearmanr\noracle_arr = np.array(oracle, dtype=float)\nfor name, vals in [('v2', v2_exposure), ('v3_rrf', v3_exposure)]:\n    r, p = spearmanr(oracle_arr, vals)\n    print(f'{name} vs oracle: Spearman r={r:.4f}, p={p:.4f}')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-14T23:19:01.853432+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Model           v2_exposure   v3_exposure   v2_norm       v3_norm\\n---------------------------------------------------------------------------\\n0.5B_d000       0.000000     0.000000     0.0000       0.0000\\n0.5B_d005       0.016035     0.000000     0.0813       0.0000\\n0.5B_d025       0.064810     0.021244     0.3286       0.6868\\n0.5B_d100       0.197201     0.003724     1.0000       0.1204\\n1.5B_d000       0.000000     0.000000     0.0000       0.0000\\n1.5B_d005       0.016035     0.013563     0.0813       0.4385\\n1.5B_d025       0.064810     0.004837     0.3286       0.1564\\n1.5B_d100       0.197201     0.030933     1.0000       1.0000\\n\\nv2: 0.5B monotonic=True, 1.5B monotonic=True\\nv3_rrf: 0.5B monotonic=False, 1.5B monotonic=False\\noracle: 0.5B monotonic=True, 1.5B monotonic=True\\nv2 vs oracle: Spearman r=1.0000, p=0.0000\\nv3_rrf vs oracle: Spearman r=0.7000, p=0.0532\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.56}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-14T23:19:01.853700+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json, os\n\nsignals_dir = '/root/autodl-tmp/exp002/signals'\nmodels = [\n    'Qwen2.5-0.5B_d000_s42',\n    'Qwen2.5-0.5B_d005_s42',\n    'Qwen2.5-0.5B_d025_s42',\n    'Qwen2.5-0.5B_d100_s42',\n    'Qwen2.5-1.5B_d000_s42',\n    'Qwen2.5-1.5B_d005_s42',\n    'Qwen2.5-1.5B_d025_s42',\n    'Qwen2.5-1.5B_d100_s42',\n]\n\nfor m in models:\n    path = os.path.join(signals_dir, m, 'signals_merged_gsm8k.json')\n    if os.path.exists(path):\n        with open(path) as f:\n            items = json.load(f)\n        # Check first item for available signals\n        if items:\n            keys = sorted(items[0].keys())\n            has_s1 = any('s1' in it for it in items if it.get('s1_embedding') is not None)\n            has_s2 = any('s2' in it for it in items if it.get('s2_minkpp') is not None)\n            has_s4 = any('s4' in it for it in items if it.get('s4_selfcritique') is not None)\n            print(f'{m}: {len(items)} items, keys={keys}')\n    else:\n        print(f'{m}: MISSING at {path}')\n        # Check what signal directories exist\n        parent = os.path.join(signals_dir, m)\n        if os.path.exists(parent):\n            files = os.listdir(parent)\n            print(f'  Available files: {files}')\n        else:\n            print(f'  Directory does not exist')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json, os\n\nsignals_dir = '/root/autodl-tmp/exp002/signals'\nmodels = [\n    'Qwen2.5-0.5B_d000_s42',\n    'Qwen2.5-0.5B_d005_s42',\n    'Qwen2.5-0.5B_d025_s42',\n    'Qwen2.5-0.5B_d100_s42',\n    'Qwen2.5-1.5B_d000_s42',\n    'Qwen2.5-1.5B_d005_s42',\n    'Qwen2.5-1.5B_d025_s42',\n    'Qwen2.5-1.5B_d100_s42',\n]\n\nfor m in models:\n    path = os.path.join(signals_dir, m, 'signals_merged_gsm8k.json')\n    if os.path.exists(path):\n        with open(path) as f:\n            items = json.load(f)\n        # Check first item for available signals\n        if items:\n            keys = sorted(items[0].keys())\n            has_s1 = any('s1' in it for it in items if it.get('s1_embedding') is not None)\n            has_s2 = any('s2' in it for it in items if it.get('s2_minkpp') is not None)\n            has_s4 = any('s4' in it for it in items if it.get('s4_selfcritique') is not None)\n            print(f'{m}: {len(items)} items, keys={keys}')\n    else:\n        print(f'{m}: MISSING at {path}')\n        # Check what signal directories exist\n        parent = os.path.join(signals_dir, m)\n        if os.path.exists(parent):\n            files = os.listdir(parent)\n            print(f'  Available files: {files}')\n        else:\n            print(f'  Directory does not exist')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-14T23:19:01.853960+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Qwen2.5-0.5B_d000_s42: 1319 items, keys=['benchmark', 'index', 's1_embedding', 's2_minkpp', 's3_constat', 's4_selfcritique']\\nQwen2.5-0.5B_d005_s42: 1319 items, keys=['benchmark', 'index', 's1_embedding', 's2_minkpp', 's3_constat', 's4_selfcritique']\\nQwen2.5-0.5B_d025_s42: 1319 items, keys=['benchmark', 'index', 's1_embedding', 's2_minkpp', 's3_constat', 's4_selfcritique']\\nQwen2.5-0.5B_d100_s42: 1319 items, keys=['benchmark', 'index', 's1_embedding', 's2_minkpp', 's3_constat', 's4_selfcritique']\\nQwen2.5-1.5B_d000_s42: 1319 items, keys=['benchmark', 'index', 's1_embedding', 's2_minkpp', 's3_constat', 's4_selfcritique']\\nQwen2.5-1.5B_d005_s42: 1319 items, keys=['benchmark', 'index', 's1_embedding', 's2_minkpp', 's3_constat', 's4_selfcritique']\\nQwen2.5-1.5B_d025_s42: 1319 items, keys=['benchmark', 'index', 's1_embedding', 's2_minkpp', 's3_constat', 's4_selfcritique']\\nQwen2.5-1.5B_d100_s42: 1319 items, keys=['benchmark', 'index', 's1_embedding', 's2_minkpp', 's3_constat', 's4_selfcritique']\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.59}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 85 · 2026-05-14T23:19:01.854389+00:00_

数据齐全，以下是根因分析结论。

---

## GSM8K v2 vs v3_rrf Gamma 矛盾根因分析

### 1. Exposure 值对比

| Model | v2 exposure | v3_rrf exposure | v2 normalized | v3_rrf normalized |
|-------|------------|----------------|--------------|------------------|
| 0.5B_d000 | 0.000 | 0.000 | 0.00 | 0.00 |
| 0.5B_d005 | 0.016 | 0.000 | 0.08 | 0.00 |
| 0.5B_d025 | 0.065 | 0.021 | 0.33 | **0.69** |
| 0.5B_d100 | 0.197 | 0.004 | 1.00 | **0.12** |
| 1.5B_d000 | 0.000 | 0.000 | 0.00 | 0.00 |
| 1.5B_d005 | 0.016 | 0.014 | 0.08 | **0.44** |
| 1.5B_d025 | 0.065 | 0.005 | 0.33 | **0.16** |
| 1.5B_d100 | 0.197 | 0.031 | 1.00 | 1.00 |

- v2 单调性：0.5B ✓, 1.5B ✓ | Spearman vs oracle = **1.000**
- v3_rrf 单调性：0.5B **✗**, 1.5B **✗** | Spearman vs oracle = **0.700**

### 2. 根因：`load_exp002_signals` 代码在两次运行之间被修改

时间线：
- **06:00–06:22**：v2 运行（使用旧版代码）
- **06:55**：git initial commit（代码已被修改）
- **06:57**：v3_rrf 运行（使用新版代码 = D023/D030 3-signal RRF fusion）

证据：
- v2 baseline = 0.6131（两个 scale 相同）
- v3_rrf baseline = 0.188 (0.5B) / 0.164 (1.5B) — 完全不同的数值范围
- Git 只有 1 个 initial commit，无法追溯旧代码

### 3. 为什么 gamma 差 10 倍

当前代码的 3-signal RRF fusion (S1+S2_flipped+S4) 产生的 per-model mean RRF 几乎是噪声：

```
Raw RRF means: 0.153 ~ 0.209 (range=0.056, 全部在 0.15~0.21 窄带内)
```

D024 delta 减去 d000 baseline 后，微小的正负波动被 clip 到 0，产生完全非单调的 exposure：
- **0.5B: d025 (0.021) >> d100 (0.004)** — d100 反而比 d025 低！
- **1.5B: d005 (0.014) >> d025 (0.005)** — d025 反而比 d005 低！

IRT 模型面对这种自相矛盾的 exposure：
- 被迫把 gamma 推高到 2.1 来放大微弱信号
- 扭曲 theta（0.5B d025: -2.12 vs v2 的 -0.92）
- PPP = 0.0（模型完全无法拟合数据）

### 4. 哪个版本正确（D027 同源 signal 约束）

**两个都有问题**：
- **v2**：exposure 单调，但两个 scale 值完全相同（可疑，暗示旧代码有 scale 处理 bug 或使用了非 scale-specific 的信号）
- **v3_rrf**：3-signal RRF mean 在 model-level 基本是噪声，不能作为 contamination exposure

核心问题是 **per-model mean RRF 不是有效的 contamination proxy**。item-level RRF 能区分被污染和未被污染的 item，但对所有 item 取 mean 后，信号被大量 clean item 稀释（d005 只有 5% item 被污染，mean 几乎不变），导致 model-level 分辨率丧失。

### 5. 建议修复方向

RRF signal 应该用作 **per-item tau**（哪些 item 更可能被污染），而不是 per-model exposure（哪个模型被污染多少）。Per-model exposure 应回退到 oracle dosage 或使用 top-K% RRF 分位数代替 mean。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_diag_gsm8k-v2-v3-rootcause_20260514T231051"
}
```

</details>

---
