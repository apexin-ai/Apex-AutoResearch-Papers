# analysis r5 equal weight mmct

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 57
- **Recorded user turns:** 0
- **Tool calls:** 28
- **Original source:** `logs/chats/worker_analysis_r5_equal_weight_mmct_20260520T204829.jsonl`
- **Structured JSON:** [`34c4f8ccff250d14d700.json`](../../sessions/34/34c4f8ccff250d14d700.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

57 recorded events

### Tool call

_source line 1 · 2026-05-20T20:54:17.728935+00:00_

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
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
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

_source line 2 · 2026-05-20T20:54:17.729441+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T20:54:17.729646+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/artifacts/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/artifacts/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T20:54:17.729875+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"d127_ccm\\nd127_csd\\nd127_spec_curve\\nd127_wasserstein\\ndose_response_m035\\nfig_consensus_heatmap.pdf\\nfig_consensus_heatmap.png\\nt20_a050_s42_fp32\\nt20_predictions_locked_v2.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.99}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T20:54:17.730031+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "find /root/autodl-tmp/distrib_canary_collapse -name \"5method_leadlag.json\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "find /root/autodl-tmp/distrib_canary_collapse -name \"5method_leadlag.json\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T20:54:17.730198+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/intervention/reactive_d1_s43_bf16/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/intervention/predictive_te_s43_bf16/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a010_s43_bf16/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a005_s42_fp32_v3_d080/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a060_s42_fp32_v3_d080/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a010_s43_fp32/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a010_s42_fp32/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s43_fp32/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s44_fp32/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s42_fp32/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s42_fp32/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43_fp32/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s44_fp32/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a060_s43_fp32/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a040_s42_fp32/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a030_s42_fp32/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/c4_a075_s42_fp32/analysis/5met
…[truncated 2547 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T20:54:17.730517+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "head -200 /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/analysis/5method_leadlag.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "head -200 /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/analysis/5method_leadlag.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T20:54:17.730774+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"meta\\\": {\\n    \\\"alpha\\\": 0.5,\\n    \\\"seed\\\": 42,\\n    \\\"n_gens\\\": 11,\\n    \\\"data_dir\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32\\\",\\n    \\\"methods\\\": [\\n      \\\"naive_xcorr\\\",\\n      \\\"diff_xcorr\\\",\\n      \\\"threshold_onset\\\",\\n      \\\"perm_granger\\\",\\n      \\\"ty_granger\\\"\\n    ],\\n    \\\"n_perm\\\": 5000,\\n    \\\"canaries\\\": [\\n      \\\"token_entropy\\\",\\n      \\\"ece\\\"\\n    ],\\n    \\\"downstreams\\\": [\\n      \\\"distinct_1\\\",\\n      \\\"distinct_2\\\",\\n      \\\"distinct_3\\\",\\n      \\\"mauve\\\"\\n    ],\\n    \\\"threshold_criterion\\\": \\\"true_3sigma_d105\\\"\\n  },\\n  \\\"pairs\\\": [\\n    {\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"forward\\\": {\\n        \\\"naive_xcorr\\\": {\\n          \\\"method\\\": \\\"naive_xcorr\\\",\\n          \\\"peak_lag\\\": 5,\\n          \\\"r\\\": -0.9395,\\n          \\\"p_value\\\": 0.005382,\\n          \\\"significant\\\": true,\\n          \\\"all_lags\\\": [\\n            {\\n              \\\"lag\\\": -5,\\n              \\\"r\\\": 0.5073,\\n              \\\"p\\\": 0.304328\\n            },\\n            {\\n              \\\"lag\\\": -4,\\n              \\\"r\\\": 0.4893,\\n              \\\"p\\\": 0.265137\\n            },\\n            {\\n              \\\"lag\\\": -3,\\n              \\\"r\\\": 0.3849,\\n              \\\"p\\\": 0.346371\\n            },\\n            {\\n              \\\"lag\\\": -2,\\n              \\\"r\\\": 0.6828,\\n              \\\"p\\\": 0.042658\\n            },\\n            {\\n              \\\"lag\\\": -1,\\n              \\\"r\\\": 0.8089,\\n              \\\"p\\\": 0.004604\\n            },\\n            {\\n              \\\"lag\\\": 0,\\n              \\\"r\\\": 0.4368,\\n              \\\"p\\\": 0.179219\\n            },\\n 
…[truncated 4005 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T20:54:17.730938+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "tail -80 /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/analysis/5method_leadlag.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "tail -80 /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/analysis/5method_leadlag.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T20:54:17.731115+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"consensus\\\": [\\n    {\\n      \\\"pair\\\": \\\"token_entropy<distinct_1\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"diff\\\",\\n        \\\"perm\\\",\\n        \\\"ty\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"token_entropy<distinct_2\\\",\\n      \\\"votes\\\": 4,\\n      \\\"methods\\\": [\\n        \\\"diff\\\",\\n        \\\"threshold\\\",\\n        \\\"perm\\\",\\n        \\\"ty\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"token_entropy<distinct_3\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"diff\\\",\\n        \\\"threshold\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"token_entropy<mauve\\\",\\n      \\\"votes\\\": 0,\\n      \\\"methods\\\": []\\n    },\\n    {\\n      \\\"pair\\\": \\\"ece<distinct_1\\\",\\n      \\\"votes\\\": 3,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"ece<distinct_2\\\",\\n      \\\"votes\\\": 4,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"threshold\\\",\\n        \\\"perm\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"ece<distinct_3\\\",\\n      \\\"votes\\\": 5,\\n      \\\"methods\\\": [\\n        \\\"naive\\\",\\n        \\\"diff\\\",\\n        \\\"threshold\\\",\\n        \\\"perm\\\",\\n        \\\"ty\\\"\\n      ]\\n    },\\n    {\\n      \\\"pair\\\": \\\"ece<mauve\\\",\\n      \\\"votes\\\": 0,\\n      \\\"methods\\\": []\\n    }\\n  ],\\n  \\\"summary\\\": {\\n    \\\"perm_granger_fdr_forward_sig\\\": 6,\\n    \\\"perm_granger_fdr_reverse_sig\\\": 0,\\n    \\\"diff_xcorr_fdr_forward_sig\\\": 7,\\n    \\\"diff_xcorr_fdr_reverse_sig\\\": 7,\\n    \\\"threshold_forward_sig\\\": 4,\\n    \\\"ty_forward_sig\\\": 3,\\n    \\\"robust_pairs\\\": 6\\n  }\\n}\", \"stderr\": \"\", \"return_code\"
…[truncated 67 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T20:54:17.731395+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "find /root/autodl-tmp/distrib_canary_collapse -name \"*.py\" -path \"*/analysis*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "find /root/autodl-tmp/distrib_canary_collapse -name \"*.py\" -path \"*/analysis*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T20:54:17.731567+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "grep -r \"robust_pairs\" /root/autodl-tmp/distrib_canary_collapse/src/ --include=\"*.py\" -l",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "grep -r \"robust_pairs\" /root/autodl-tmp/distrib_canary_collapse/src/ --include=\"*.py\" -l",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-20T20:54:17.731726+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/analysis/detrending_utils.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T20:54:17.731860+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"grep: /root/autodl-tmp/distrib_canary_collapse/src/: No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T20:54:17.731993+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "grep -rn \"robust_pairs\" /root/autodl-tmp/distrib_canary_collapse/ --include=\"*.py\" -l",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "grep -rn \"robust_pairs\" /root/autodl-tmp/distrib_canary_collapse/ --include=\"*.py\" -l",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T20:54:17.732170+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/scripts/t20_post_analysis.py\\n/root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T20:54:17.732626+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "grep -n \"robust_pairs\\|consensus\\|votes\\|FPR\\|fpr\\|weight\" /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "grep -n \"robust_pairs\\|consensus\\|votes\\|FPR\\|fpr\\|weight\" /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T20:54:17.732852+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T20:54:17.733046+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "grep -n \"robust_pairs\" /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "grep -n \"robust_pairs\" /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T20:54:17.733245+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"404:        \\\"robust_pairs\\\": sum(1 for c in consensus if c[\\\"votes\\\"] >= 3),\\n406:    print(f\\\"\\\\n  Robust pairs (>=3/5 methods): {all_results['summary']['robust_pairs']}/8\\\")\\n437:        f.write(f\\\"Robust pairs (>=3/5 methods agree): {all_results['summary']['robust_pairs']}/8\\\\n\\\\n\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T20:54:17.733554+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "grep -n \"consensus\" /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "grep -n \"consensus\" /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T20:54:17.733755+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"377:    consensus = []\\n393:        consensus.append({\\\"pair\\\": label, \\\"votes\\\": votes, \\\"methods\\\": methods_sig})\\n396:    all_results[\\\"consensus\\\"] = consensus\\n404:        \\\"robust_pairs\\\": sum(1 for c in consensus if c[\\\"votes\\\"] >= 3),\\n444:        for c in consensus:\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T20:54:17.733955+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "command": "grep -n \"weight\" /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
  "server": "westd-17855",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "command": "grep -n \"weight\" /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
    "server": "westd-17855",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T20:54:17.734139+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T20:54:17.734355+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "cat -n /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "cat -n /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T20:54:17.734776+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"     1\\t\\\"\\\"\\\"5-method lead-lag analysis: generalized CLI version.\\n     2\\t\\n     3\\tUsage:\\n     4\\t    python run_5method_analysis.py --data_dir results/alpha_sweep/a000_s43 --alpha 0.0 --seed 43\\n     5\\t    python run_5method_analysis.py --data_dir results/alpha_sweep/a000_s43 --alpha 0.0 --seed 43 --dry-run\\n     6\\t\\\"\\\"\\\"\\n     7\\t\\n     8\\timport argparse\\n     9\\timport json\\n    10\\timport os\\n    11\\timport sys\\n    12\\timport glob as glob_module\\n    13\\timport numpy as np\\n    14\\tfrom scipy import stats\\n    15\\tfrom statsmodels.tsa.stattools import adfuller\\n    16\\t\\n    17\\tsys.path.insert(0, \\\"/root/autodl-tmp/distrib_canary_collapse\\\")\\n    18\\tfrom permutation_granger import permutation_granger_test\\n    19\\t\\n    20\\tN_PERM = 5000\\n    21\\tALPHA = 0.05\\n    22\\t\\n    23\\tCANARIES = [\\\"token_entropy\\\", \\\"ece\\\"]\\n    24\\tDOWNSTREAMS = [\\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\", \\\"mauve\\\"]\\n    25\\t\\n    26\\tHIGHER_IS_WORSE = {\\\"ece\\\"}\\n    27\\tLOWER_IS_WORSE = {\\\"token_entropy\\\", \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\", \\\"mauve\\\"}\\n    28\\t\\n    29\\t\\n    30\\tdef load_series(data_dir):\\n    31\\t    \\\"\\\"\\\"Load metrics - from all_metrics.json if available, else aggregate gen_X/metrics.json.\\\"\\\"\\\"\\n    32\\t    all_path = os.path.join(data_dir, \\\"all_metrics.json\\\")\\n    33\\t    if os.path.exists(all_path):\\n    34\\t        with open(all_path) as f:\\n    35\\t            data = json.load(f)\\n    36\\t    else:\\n    37\\t        # Aggregate from per-generation metrics\\n    38\\t        gen_dirs = sorted(glob_module.glob(os.path.join(data_dir, \\\"gen_*\\\")),\\n    39\\t                         key=lambda x: int(os.path.basename(x).split(\\\"_\\\")[1]))\\n    40\\t        data = []\\n    41\\t        for gd in gen_dirs:\\n    42\\t      
…[truncated 7426 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T20:54:17.735074+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "sed -n '370,395p' /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "sed -n '370,395p' /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T20:54:17.735300+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T20:54:17.735580+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "grep -n \"votes\\|methods_sig\\|consensus\\|peak_lag\\|significant\" /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "grep -n \"votes\\|methods_sig\\|consensus\\|peak_lag\\|significant\" /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T20:54:17.735721+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T20:54:17.735849+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "grep -n \"votes\" /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "grep -n \"votes\" /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T20:54:17.735989+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"380:        votes = 0\\n383:            votes += 1; methods_sig.append(\\\"naive\\\")\\n385:            votes += 1; methods_sig.append(\\\"diff\\\")\\n387:            votes += 1; methods_sig.append(\\\"threshold\\\")\\n389:            votes += 1; methods_sig.append(\\\"perm\\\")\\n391:            votes += 1; methods_sig.append(\\\"ty\\\")\\n393:        consensus.append({\\\"pair\\\": label, \\\"votes\\\": votes, \\\"methods\\\": methods_sig})\\n394:        print(f\\\"  {label:<25} {votes}/5  [{', '.join(methods_sig) if methods_sig else 'none'}]\\\")\\n404:        \\\"robust_pairs\\\": sum(1 for c in consensus if c[\\\"votes\\\"] >= 3),\\n445:            f.write(f\\\"  {c['pair']:<25} {c['votes']}/5  [{', '.join(c['methods']) if c['methods'] else 'none'}]\\\\n\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T20:54:17.736159+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "grep -n -A1 \"votes += 1\" /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "grep -n -A1 \"votes += 1\" /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T20:54:17.736332+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"383:            votes += 1; methods_sig.append(\\\"naive\\\")\\n384-        if f[\\\"diff_xcorr\\\"].get(\\\"significant_fdr\\\", False) and f[\\\"diff_xcorr\\\"][\\\"peak_lag\\\"] < 0:\\n385:            votes += 1; methods_sig.append(\\\"diff\\\")\\n386-        if f[\\\"threshold_onset\\\"][\\\"significant\\\"]:\\n387:            votes += 1; methods_sig.append(\\\"threshold\\\")\\n388-        if f[\\\"perm_granger\\\"].get(\\\"significant_fdr\\\", False):\\n389:            votes += 1; methods_sig.append(\\\"perm\\\")\\n390-        if f[\\\"ty_granger\\\"][\\\"significant\\\"]:\\n391:            votes += 1; methods_sig.append(\\\"ty\\\")\\n392-        label = f\\\"{pair['canary']}<{pair['downstream']}\\\"\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T20:54:17.736490+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "grep -n -B1 \"votes += 1\" /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "grep -n -B1 \"votes += 1\" /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T20:54:17.736635+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"382-        if f[\\\"naive_xcorr\\\"][\\\"significant\\\"] and f[\\\"naive_xcorr\\\"][\\\"peak_lag\\\"] < 0:\\n383:            votes += 1; methods_sig.append(\\\"naive\\\")\\n384-        if f[\\\"diff_xcorr\\\"].get(\\\"significant_fdr\\\", False) and f[\\\"diff_xcorr\\\"][\\\"peak_lag\\\"] < 0:\\n385:            votes += 1; methods_sig.append(\\\"diff\\\")\\n386-        if f[\\\"threshold_onset\\\"][\\\"significant\\\"]:\\n387:            votes += 1; methods_sig.append(\\\"threshold\\\")\\n388-        if f[\\\"perm_granger\\\"].get(\\\"significant_fdr\\\", False):\\n389:            votes += 1; methods_sig.append(\\\"perm\\\")\\n390-        if f[\\\"ty_granger\\\"][\\\"significant\\\"]:\\n391:            votes += 1; methods_sig.append(\\\"ty\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T20:54:17.736837+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-17855",
  "command": "cat > /root/autodl-tmp/distrib_canary_collapse/scripts/equal_weight_comparison.py << 'PYEOF'\n\"\"\"Compare equal-weight K>=3 vs current consensus K>=3 across experiments.\"\"\"\nimport json\nimport os\nimport sys\n\nBASE = \"/root/autodl-tmp/distrib_canary_collapse/results\"\n\nEXPERIMENTS = [\n    (\"a000_s42_fp32\", \"alpha_sweep\", 0.00, 10),\n    (\"a010_s42_fp32\", \"alpha_sweep\", 0.10, 10),\n    (\"a025_s42_fp32\", \"alpha_sweep\", 0.25, 10),\n    (\"a025_s43_fp32\", \"alpha_sweep\", 0.25, 10),\n    (\"a045_s42_fp32\", \"alpha_sweep\", 0.45, 10),\n    (\"a045_s43_fp32\", \"alpha_sweep\", 0.45, 10),\n    (\"a050_s42_fp32\", \"alpha_sweep\", 0.50, 10),\n    (\"a060_s42_fp32_v4\", \"alpha_sweep\", 0.60, 10),\n    (\"a075_s42_fp32\", \"alpha_sweep\", 0.75, 10),\n    (\"a100_s42_fp32\", \"t20\", 1.00, 20),\n    (\"a045_s42_fp32\", \"t20\", 0.45, 20),\n]\n\nresults = []\n\nfor exp_id, subdir, alpha, T in EXPERIMENTS:\n    json_path = os.path.join(BASE, subdir, exp_id, \"analysis\", \"5method_leadlag.json\")\n    if not os.path.exists(json_path):\n        print(f\"MISSING: {json_path}\", file=sys.stderr)\n        continue\n\n    with open(json_path) as f:\n        data = json.load(f)\n\n    pair_details = []\n    equal_weight_k3_count = 0\n\n    for pair in data[\"pairs\"]:\n        fwd = pair[\"forward\"]\n        label = f\"{pair['canary']}<{pair['downstream']}\"\n\n        # Equal-weight: just significance, NO direction filter\n        methods = {\n            \"permg\": fwd[\"perm_granger\"].get(\"significant_fdr\", False),\n            \"diffxcorr\": fwd[\"diff_xcorr\"].get(\"significant_fdr\", False),\n            \"naive\": fwd[\"naive_xcorr\"][\"significant\"],\n            \"threshold\": fwd[\"threshold_onset\"][\"significant\"],\n            \"ty\": fwd[\"ty_granger\"][\"significant\"],\n        }\n        equal_k = sum(1 for v in methods.values() if v)\n        equal_sig = equal_k >= 3\n\n        if equal_sig:\n            equal_weight_k3_count += 1\n\n        pair_details.append({\n            \"pair\": label,\n            \"methods\": methods,\n            \"equal_weight_K\": equal_k,\n            \"equal_weight_sig\": equal_sig,\n        })\n\n    # Current consensus from JSON (uses direction filters)\n    current_k3 = data[\"summary\"][\"robust_pairs\"]\n\n    # Also recompute current consensus from consensus section for verification\n    current_consensus_k3 = sum(1 for c in data[\"consensus\"] if c[\"votes\"] >= 3)\n\n    # For each pair, also get current consensus votes\n    for i, pd in enumerate(pair_details):\n        pd[\"current_consensus_votes\"] = data[\"consensus\"][i][\"votes\"]\n        pd[\"current_consensus_methods\"] = data[\"consensus\"][i][\"methods\"]\n\n    full_label = f\"{subdir}/{exp_id}\" if subdir != \"alpha_sweep\" else exp_id\n    diff = equal_weight_k3_count - current_k3\n\n    results.append({\n        \"exp_id\": full_label,\n        \"alpha\": alpha,\n        \"T\": T,\n        \"pairs\": pair_details,\n        \"equal_weight_K3\": equal_weight_k3_count,\n        \"current_K3\": current_k3,\n        \"current_K3_verify\": current_consensus_k3,\n        \"difference\": diff,\n    })\n\n    print(f\"{full_label:30s}  alpha={alpha:.2f} T={T:2d}  \"\n          f\"equal_K3={equal_weight_k3_count}  current_K3={current_k3}  diff={diff:+d}\")\n\n    # Show per-pair differences\n    for pd in pair_details:\n        if pd[\"equal_weight_K\"] != pd[\"current_consensus_votes\"]:\n            print(f\"    {pd['pair']:30s}  equal_K={pd['equal_weight_K']}  \"\n                  f\"current_K={pd['current_consensus_votes']}  \"\n                  f\"methods_equal={[k for k,v in pd['methods'].items() if v]}  \"\n                  f\"methods_current={pd['current_consensus_methods']}\")\n\n# Summary\nexperiments_with_diff = sum(1 for r in results if r[\"difference\"] != 0)\nmax_diff = max(abs(r[\"difference\"]) for r in results) if results else 0\ntotal_pair_diffs = sum(\n    1 for r in results for p in r[\"pairs\"]\n    if p[\"equal_weight_K\"] != p[\"current_consensus_votes\"]\n)\n\nprint(f\"\\n{'='*70}\")\nprint(f\"Total experiments: {len(results)}\")\nprint(f\"Experiments with K3 difference: {experiments_with_diff}\")\nprint(f\"Max absolute difference: {max_diff}\")\nprint(f\"Total pair-level vote differences: {total_pair_diffs}\")\n\n# Save output JSON\noutput = {\n    \"experiments\": results,\n    \"summary\": {\n        \"total_experiments\": len(results),\n        \"experiments_with_difference\": experiments_with_diff,\n        \"max_difference\": max_diff,\n        \"total_pair_vote_differences\": total_pair_diffs,\n        \"note\": \"equal-weight = significance only (no direction filter); current = significance + direction filter for xcorr methods\",\n    }\n}\n\nout_path = \"/root/autodl-tmp/distrib_canary_collapse/artifacts/equal_weight_vs_current_k3.json\"\nwith open(out_path, \"w\") as f:\n    json.dump(output, f, indent=2)\nprint(f\"\\nSaved: {out_path}\")\nPYEOF\necho \"Script written\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-17855",
    "command": "cat > /root/autodl-tmp/distrib_canary_collapse/scripts/equal_weight_comparison.py << 'PYEOF'\n\"\"\"Compare equal-weight K>=3 vs current consensus K>=3 across experiments.\"\"\"\nimport json\nimport os\nimport sys\n\nBASE = \"/root/autodl-tmp/distrib_canary_collapse/results\"\n\nEXPERIMENTS = [\n    (\"a000_s42_fp32\", \"alpha_sweep\", 0.00, 10),\n    (\"a010_s42_fp32\", \"alpha_sweep\", 0.10, 10),\n    (\"a025_s42_fp32\", \"alpha_sweep\", 0.25, 10),\n    (\"a025_s43_fp32\", \"alpha_sweep\", 0.25, 10),\n    (\"a045_s42_fp32\", \"alpha_sweep\", 0.45, 10),\n    (\"a045_s43_fp32\", \"alpha_sweep\", 0.45, 10),\n    (\"a050_s42_fp32\", \"alpha_sweep\", 0.50, 10),\n    (\"a060_s42_fp32_v4\", \"alpha_sweep\", 0.60, 10),\n    (\"a075_s42_fp32\", \"alpha_sweep\", 0.75, 10),\n    (\"a100_s42_fp32\", \"t20\", 1.00, 20),\n    (\"a045_s42_fp32\", \"t20\", 0.45, 20),\n]\n\nresults = []\n\nfor exp_id, subdir, alpha, T in EXPERIMENTS:\n    json_path = os.path.join(BASE, subdir, exp_id, \"analysis\", \"5method_leadlag.json\")\n    if not os.path.exists(json_path):\n        print(f\"MISSING: {json_path}\", file=sys.stderr)\n        continue\n\n    with open(json_path) as f:\n        data = json.load(f)\n\n    pair_details = []\n    equal_weight_k3_count = 0\n\n    for pair in data[\"pairs\"]:\n        fwd = pair[\"forward\"]\n        label = f\"{pair['canary']}<{pair['downstream']}\"\n\n        # Equal-weight: just significance, NO direction filter\n        methods = {\n            \"permg\": fwd[\"perm_granger\"].get(\"significant_fdr\", False),\n            \"diffxcorr\": fwd[\"diff_xcorr\"].get(\"significant_fdr\", False),\n            \"naive\": fwd[\"naive_xcorr\"][\"significant\"],\n            \"threshold\": fwd[\"threshold_onset\"][\"significant\"],\n            \"ty\": fwd[\"ty_granger\"][\"significant\"],\n        }\n        equal_k = sum(1 for v in methods.values() if v)\n        equal_sig = equal_k >= 3\n\n        if equal_sig:\n            equal_weight_k3_count += 1\n\n        pair_details.append({\n            \"pair\": label,\n            \"methods\": methods,\n            \"equal_weight_K\": equal_k,\n            \"equal_weight_sig\": equal_sig,\n        })\n\n    # Current consensus from JSON (uses direction filters)\n    current_k3 = data[\"summary\"][\"robust_pairs\"]\n\n    # Also recompute current consensus from consensus section for verification\n    current_consensus_k3 = sum(1 for c in data[\"consensus\"] if c[\"votes\"] >= 3)\n\n    # For each pair, also get current consensus votes\n    for i, pd in enumerate(pair_details):\n        pd[\"current_consensus_votes\"] = data[\"consensus\"][i][\"votes\"]\n        pd[\"current_consensus_methods\"] = data[\"consensus\"][i][\"methods\"]\n\n    full_label = f\"{subdir}/{exp_id}\" if subdir != \"alpha_sweep\" else exp_id\n    diff = equal_weight_k3_count - current_k3\n\n    results.append({\n        \"exp_id\": full_label,\n        \"alpha\": alpha,\n        \"T\": T,\n        \"pairs\": pair_details,\n        \"equal_weight_K3\": equal_weight_k3_count,\n        \"current_K3\": current_k3,\n        \"current_K3_verify\": current_consensus_k3,\n        \"difference\": diff,\n    })\n\n    print(f\"{full_label:30s}  alpha={alpha:.2f} T={T:2d}  \"\n          f\"equal_K3={equal_weight_k3_count}  current_K3={current_k3}  diff={diff:+d}\")\n\n    # Show per-pair differences\n    for pd in pair_details:\n        if pd[\"equal_weight_K\"] != pd[\"current_consensus_votes\"]:\n            print(f\"    {pd['pair']:30s}  equal_K={pd['equal_weight_K']}  \"\n                  f\"current_K={pd['current_consensus_votes']}  \"\n                  f\"methods_equal={[k for k,v in pd['methods'].items() if v]}  \"\n                  f\"methods_current={pd['current_consensus_methods']}\")\n\n# Summary\nexperiments_with_diff = sum(1 for r in results if r[\"difference\"] != 0)\nmax_diff = max(abs(r[\"difference\"]) for r in results) if results else 0\ntotal_pair_diffs = sum(\n    1 for r in results for p in r[\"pairs\"]\n    if p[\"equal_weight_K\"] != p[\"current_consensus_votes\"]\n)\n\nprint(f\"\\n{'='*70}\")\nprint(f\"Total experiments: {len(results)}\")\nprint(f\"Experiments with K3 difference: {experiments_with_diff}\")\nprint(f\"Max absolute difference: {max_diff}\")\nprint(f\"Total pair-level vote differences: {total_pair_diffs}\")\n\n# Save output JSON\noutput = {\n    \"experiments\": results,\n    \"summary\": {\n        \"total_experiments\": len(results),\n        \"experiments_with_difference\": experiments_with_diff,\n        \"max_difference\": max_diff,\n        \"total_pair_vote_differences\": total_pair_diffs,\n        \"note\": \"equal-weight = significance only (no direction filter); current = significance + direction filter for xcorr methods\",\n    }\n}\n\nout_path = \"/root/autodl-tmp/distrib_canary_collapse/artifacts/equal_weight_vs_current_k3.json\"\nwith open(out_path, \"w\") as f:\n    json.dump(output, f, indent=2)\nprint(f\"\\nSaved: {out_path}\")\nPYEOF\necho \"Script written\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T20:54:17.737022+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T20:54:17.737151+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-17855",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python scripts/equal_weight_comparison.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-17855",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python scripts/equal_weight_comparison.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T20:54:17.737383+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"a000_s42_fp32                   alpha=0.00 T=10  equal_K3=2  current_K3=0  diff=+2\\n    token_entropy<distinct_2        equal_K=3  current_K=2  methods_equal=['diffxcorr', 'naive', 'threshold']  methods_current=['diff', 'threshold']\\n    token_entropy<distinct_3        equal_K=3  current_K=2  methods_equal=['diffxcorr', 'naive', 'threshold']  methods_current=['diff', 'threshold']\\n    token_entropy<mauve             equal_K=2  current_K=1  methods_equal=['naive', 'threshold']  methods_current=['threshold']\\n    ece<distinct_2                  equal_K=1  current_K=0  methods_equal=['naive']  methods_current=[]\\n    ece<distinct_3                  equal_K=2  current_K=1  methods_equal=['naive', 'ty']  methods_current=['ty']\\n    ece<mauve                       equal_K=2  current_K=1  methods_equal=['diffxcorr', 'naive']  methods_current=['diff']\\na010_s42_fp32                   alpha=0.10 T=10  equal_K3=2  current_K3=0  diff=+2\\n    token_entropy<distinct_3        equal_K=3  current_K=2  methods_equal=['diffxcorr', 'naive', 'ty']  methods_current=['diff', 'ty']\\n    token_entropy<mauve             equal_K=1  current_K=0  methods_equal=['diffxcorr']  methods_current=[]\\n    ece<distinct_1                  equal_K=2  current_K=1  methods_equal=['diffxcorr', 'naive']  methods_current=['diff']\\n    ece<distinct_2                  equal_K=3  current_K=2  methods_equal=['diffxcorr', 'naive', 'ty']  methods_current=['diff', 'ty']\\n    ece<distinct_3                  equal_K=2  current_K=1  methods_equal=['naive', 'ty']  methods_current=['ty']\\na025_s42_fp32                   alpha=0.25 T=10  equal_K3=0  current_K3=0  diff=+0\\n    token_entropy<distinct_1        equal_K=2  current_K=1  methods_equal=['diffxcorr', 'naive']  methods_current=['diff']\\n    token_entropy<distinct_2        equal_K=1  current_K=0  methods_equal=['naive']  methods_current=[]\\n    token_entropy<distinct_3        equal_K=1  current
…[truncated 6346 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T20:54:17.737596+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/artifacts/equal_weight_vs_current_k3.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/artifacts/equal_weight_vs_current_k3.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-20T20:54:17.737936+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiments\\\": [\\n    {\\n      \\\"exp_id\\\": \\\"a000_s42_fp32\\\",\\n      \\\"alpha\\\": 0.0,\\n      \\\"T\\\": 10,\\n      \\\"pairs\\\": [\\n        {\\n          \\\"pair\\\": \\\"token_entropy<distinct_1\\\",\\n          \\\"methods\\\": {\\n            \\\"permg\\\": false,\\n            \\\"diffxcorr\\\": true,\\n            \\\"naive\\\": true,\\n            \\\"threshold\\\": false,\\n            \\\"ty\\\": false\\n          },\\n          \\\"equal_weight_K\\\": 2,\\n          \\\"equal_weight_sig\\\": false,\\n          \\\"current_consensus_votes\\\": 2,\\n          \\\"current_consensus_methods\\\": [\\n            \\\"naive\\\",\\n            \\\"diff\\\"\\n          ]\\n        },\\n        {\\n          \\\"pair\\\": \\\"token_entropy<distinct_2\\\",\\n          \\\"methods\\\": {\\n            \\\"permg\\\": false,\\n            \\\"diffxcorr\\\": true,\\n            \\\"naive\\\": true,\\n            \\\"threshold\\\": true,\\n            \\\"ty\\\": false\\n          },\\n          \\\"equal_weight_K\\\": 3,\\n          \\\"equal_weight_sig\\\": true,\\n          \\\"current_consensus_votes\\\": 2,\\n          \\\"current_consensus_methods\\\": [\\n            \\\"diff\\\",\\n            \\\"threshold\\\"\\n          ]\\n        },\\n        {\\n          \\\"pair\\\": \\\"token_entropy<distinct_3\\\",\\n          \\\"methods\\\": {\\n            \\\"permg\\\": false,\\n            \\\"diffxcorr\\\": true,\\n            \\\"naive\\\": true,\\n            \\\"threshold\\\": true,\\n            \\\"ty\\\": false\\n          },\\n          \\\"equal_weight_K\\\": 3,\\n          \\\"equal_weight_sig\\\": true,\\n          \\\"current_consensus_votes\\\": 2,\\n          \\\"current_consensus_methods\\\": [\\n            \\\"diff\\\",\\n            \\\"threshold\\\"\\n          ]\\n        },\\n        {\\n          \\\"pair\\\": \\\"token_entropy<mauve\\\",\\n          \\\"metho
…[truncated 8385 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T20:54:17.738153+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-17855",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\nwith open('/root/autodl-tmp/distrib_canary_collapse/artifacts/equal_weight_vs_current_k3.json') as f:\n    data = json.load(f)\n\n# Add conclusion\ndata['summary']['conclusion'] = (\n    'Equal-weight (no direction filter) vs current (with D111 direction filter) differs in 3/11 experiments. '\n    'The difference is driven by NaiveXCorr having significance with peak_lag > 0 (reverse direction), '\n    'which passes significance-only check but is filtered by D111. '\n    'Critical: null experiment (a=0.00) inflates from 0 to 2 K>=3 pairs without direction filter. '\n    'Direction filtering is essential for FPR control. '\n    'At strong signal (a>=0.50 T=10), both methods agree perfectly at K3 level. '\n    'Largest divergence at t20/a045 (+4 pairs) where NaiveXCorr is broadly significant but often in wrong direction.'\n)\n\n# Add direction analysis\nnaive_inflations = 0\ndiff_inflations = 0\nfor exp in data['experiments']:\n    for p in exp['pairs']:\n        eq_k = p['equal_weight_K']\n        cur_k = p['current_consensus_votes']\n        if eq_k > cur_k:\n            eq_methods = set(k for k,v in p['methods'].items() if v)\n            cur_methods = set(p['current_consensus_methods'])\n            # Map method names\n            cur_mapped = set()\n            for m in cur_methods:\n                if m == 'diff': cur_mapped.add('diffxcorr')\n                elif m == 'perm': cur_mapped.add('permg')\n                else: cur_mapped.add(m)\n            extra = eq_methods - cur_mapped\n            if 'naive' in extra:\n                naive_inflations += 1\n            if 'diffxcorr' in extra:\n                diff_inflations += 1\n\ndata['summary']['naive_xcorr_direction_filtered_count'] = naive_inflations\ndata['summary']['diff_xcorr_direction_filtered_count'] = diff_inflations\n\nwith open('/root/autodl-tmp/distrib_canary_collapse/artifacts/equal_weight_vs_current_k3.json', 'w') as f:\n    json.dump(data, f, indent=2)\nprint(f'NaiveXCorr filtered by direction: {naive_inflations} pairs')\nprint(f'DiffXCorr filtered by direction: {diff_inflations} pairs')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-17855",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\nwith open('/root/autodl-tmp/distrib_canary_collapse/artifacts/equal_weight_vs_current_k3.json') as f:\n    data = json.load(f)\n\n# Add conclusion\ndata['summary']['conclusion'] = (\n    'Equal-weight (no direction filter) vs current (with D111 direction filter) differs in 3/11 experiments. '\n    'The difference is driven by NaiveXCorr having significance with peak_lag > 0 (reverse direction), '\n    'which passes significance-only check but is filtered by D111. '\n    'Critical: null experiment (a=0.00) inflates from 0 to 2 K>=3 pairs without direction filter. '\n    'Direction filtering is essential for FPR control. '\n    'At strong signal (a>=0.50 T=10), both methods agree perfectly at K3 level. '\n    'Largest divergence at t20/a045 (+4 pairs) where NaiveXCorr is broadly significant but often in wrong direction.'\n)\n\n# Add direction analysis\nnaive_inflations = 0\ndiff_inflations = 0\nfor exp in data['experiments']:\n    for p in exp['pairs']:\n        eq_k = p['equal_weight_K']\n        cur_k = p['current_consensus_votes']\n        if eq_k > cur_k:\n            eq_methods = set(k for k,v in p['methods'].items() if v)\n            cur_methods = set(p['current_consensus_methods'])\n            # Map method names\n            cur_mapped = set()\n            for m in cur_methods:\n                if m == 'diff': cur_mapped.add('diffxcorr')\n                elif m == 'perm': cur_mapped.add('permg')\n                else: cur_mapped.add(m)\n            extra = eq_methods - cur_mapped\n            if 'naive' in extra:\n                naive_inflations += 1\n            if 'diffxcorr' in extra:\n                diff_inflations += 1\n\ndata['summary']['naive_xcorr_direction_filtered_count'] = naive_inflations\ndata['summary']['diff_xcorr_direction_filtered_count'] = diff_inflations\n\nwith open('/root/autodl-tmp/distrib_canary_collapse/artifacts/equal_weight_vs_current_k3.json', 'w') as f:\n    json.dump(data, f, indent=2)\nprint(f'NaiveXCorr filtered by direction: {naive_inflations} pairs')\nprint(f'DiffXCorr filtered by direction: {diff_inflations} pairs')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-20T20:54:17.738336+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"NaiveXCorr filtered by direction: 57 pairs\\nDiffXCorr filtered by direction: 10 pairs\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-20T20:54:17.738495+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "scp westd-17855:/root/autodl-tmp/distrib_canary_collapse/artifacts/equal_weight_vs_current_k3.json /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/",
  "description": "Copy artifact from remote server"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "Bash",
  "tool_args": {
    "command": "scp westd-17855:/root/autodl-tmp/distrib_canary_collapse/artifacts/equal_weight_vs_current_k3.json /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/",
    "description": "Copy artifact from remote server"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T20:54:17.738620+00:00_

Exit code 255
ssh: Could not resolve hostname westd-17855: Temporary failure in name resolution
scp: Connection closed

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-20T20:54:17.738741+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/artifacts/equal_weight_vs_current_k3.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/artifacts/equal_weight_vs_current_k3.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-20T20:54:17.739078+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiments\\\": [\\n    {\\n      \\\"exp_id\\\": \\\"a000_s42_fp32\\\",\\n      \\\"alpha\\\": 0.0,\\n      \\\"T\\\": 10,\\n      \\\"pairs\\\": [\\n        {\\n          \\\"pair\\\": \\\"token_entropy<distinct_1\\\",\\n          \\\"methods\\\": {\\n            \\\"permg\\\": false,\\n            \\\"diffxcorr\\\": true,\\n            \\\"naive\\\": true,\\n            \\\"threshold\\\": false,\\n            \\\"ty\\\": false\\n          },\\n          \\\"equal_weight_K\\\": 2,\\n          \\\"equal_weight_sig\\\": false,\\n          \\\"current_consensus_votes\\\": 2,\\n          \\\"current_consensus_methods\\\": [\\n            \\\"naive\\\",\\n            \\\"diff\\\"\\n          ]\\n        },\\n        {\\n          \\\"pair\\\": \\\"token_entropy<distinct_2\\\",\\n          \\\"methods\\\": {\\n            \\\"permg\\\": false,\\n            \\\"diffxcorr\\\": true,\\n            \\\"naive\\\": true,\\n            \\\"threshold\\\": true,\\n            \\\"ty\\\": false\\n          },\\n          \\\"equal_weight_K\\\": 3,\\n          \\\"equal_weight_sig\\\": true,\\n          \\\"current_consensus_votes\\\": 2,\\n          \\\"current_consensus_methods\\\": [\\n            \\\"diff\\\",\\n            \\\"threshold\\\"\\n          ]\\n        },\\n        {\\n          \\\"pair\\\": \\\"token_entropy<distinct_3\\\",\\n          \\\"methods\\\": {\\n            \\\"permg\\\": false,\\n            \\\"diffxcorr\\\": true,\\n            \\\"naive\\\": true,\\n            \\\"threshold\\\": true,\\n            \\\"ty\\\": false\\n          },\\n          \\\"equal_weight_K\\\": 3,\\n          \\\"equal_weight_sig\\\": true,\\n          \\\"current_consensus_votes\\\": 2,\\n          \\\"current_consensus_methods\\\": [\\n            \\\"diff\\\",\\n            \\\"threshold\\\"\\n          ]\\n        },\\n        {\\n          \\\"pair\\\": \\\"token_entropy<mauve\\\",\\n          \\\"metho
…[truncated 8212 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-20T20:54:17.739302+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-17855",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\nwith open('/root/autodl-tmp/distrib_canary_collapse/artifacts/equal_weight_vs_current_k3.json') as f:\n    data = json.load(f)\n\n# Print compact per-experiment summary\nfor exp in data['experiments']:\n    print(f\\\"{exp['exp_id']}|{exp['alpha']}|{exp['T']}|{exp['equal_weight_K3']}|{exp['current_K3']}|{exp['difference']}\\\")\n    for p in exp['pairs']:\n        m = p['methods']\n        sig_str = ''.join(['1' if m[k] else '0' for k in ['permg','diffxcorr','naive','threshold','ty']])\n        print(f\\\"  {p['pair']}|{sig_str}|{p['equal_weight_K']}|{p['current_consensus_votes']}\\\")\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-17855",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\nwith open('/root/autodl-tmp/distrib_canary_collapse/artifacts/equal_weight_vs_current_k3.json') as f:\n    data = json.load(f)\n\n# Print compact per-experiment summary\nfor exp in data['experiments']:\n    print(f\\\"{exp['exp_id']}|{exp['alpha']}|{exp['T']}|{exp['equal_weight_K3']}|{exp['current_K3']}|{exp['difference']}\\\")\n    for p in exp['pairs']:\n        m = p['methods']\n        sig_str = ''.join(['1' if m[k] else '0' for k in ['permg','diffxcorr','naive','threshold','ty']])\n        print(f\\\"  {p['pair']}|{sig_str}|{p['equal_weight_K']}|{p['current_consensus_votes']}\\\")\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-20T20:54:17.739526+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"a000_s42_fp32|0.0|10|2|0|2\\n  token_entropy<distinct_1|01100|2|2\\n  token_entropy<distinct_2|01110|3|2\\n  token_entropy<distinct_3|01110|3|2\\n  token_entropy<mauve|00110|2|1\\n  ece<distinct_1|00101|2|2\\n  ece<distinct_2|00100|1|0\\n  ece<distinct_3|00101|2|1\\n  ece<mauve|01100|2|1\\na010_s42_fp32|0.1|10|2|0|2\\n  token_entropy<distinct_1|01100|2|2\\n  token_entropy<distinct_2|01100|2|2\\n  token_entropy<distinct_3|01101|3|2\\n  token_entropy<mauve|01000|1|0\\n  ece<distinct_1|01100|2|1\\n  ece<distinct_2|01101|3|2\\n  ece<distinct_3|00101|2|1\\n  ece<mauve|00101|2|2\\na025_s42_fp32|0.25|10|0|0|0\\n  token_entropy<distinct_1|01100|2|1\\n  token_entropy<distinct_2|00100|1|0\\n  token_entropy<distinct_3|00100|1|0\\n  token_entropy<mauve|00101|2|1\\n  ece<distinct_1|00100|1|0\\n  ece<distinct_2|01100|2|0\\n  ece<distinct_3|01100|2|0\\n  ece<mauve|00100|1|1\\na025_s43_fp32|0.25|10|0|0|0\\n  token_entropy<distinct_1|00101|2|1\\n  token_entropy<distinct_2|00100|1|0\\n  token_entropy<distinct_3|00100|1|0\\n  token_entropy<mauve|00100|1|0\\n  ece<distinct_1|00100|1|0\\n  ece<distinct_2|00100|1|0\\n  ece<distinct_3|00100|1|0\\n  ece<mauve|00100|1|0\\na045_s42_fp32|0.45|10|0|0|0\\n  token_entropy<distinct_1|01100|2|1\\n  token_entropy<distinct_2|01100|2|1\\n  token_entropy<distinct_3|01100|2|0\\n  token_entropy<mauve|00100|1|0\\n  ece<distinct_1|01100|2|1\\n  ece<distinct_2|01100|2|0\\n  ece<distinct_3|01100|2|0\\n  ece<mauve|00100|1|1\\na045_s43_fp32|0.45|10|0|0|0\\n  token_entropy<distinct_1|01100|2|1\\n  token_entropy<distinct_2|00100|1|0\\n  token_entropy<distinct_3|00101|2|1\\n  token_entropy<mauve|00100|1|0\\n  ece<distinct_1|01100|2|0\\n  ece<distinct_2|01100|2|0\\n  ece<distinct_3|00101|2|1\\n  ece<mauve|00100|1|1\\na050_s42_fp32|0.5|10|6|6|0\\n  token_entropy<distinct_1|11101|4|3\\n  token_entropy<distinct_2|11111|5|4\\n  token_entropy<distinct_3|11110|4|3\\n  token_entropy<mauve|01100|2|0\\n  ece<distinct
…[truncated 1378 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-20T20:54:17.739818+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/equal_weight_vs_current_k3.json",
  "content": "{\n  \"experiments\": [\n    {\n      \"exp_id\": \"a000_s42_fp32\",\n      \"alpha\": 0.0,\n      \"T\": 10,\n      \"pairs\": [\n        {\"pair\": \"token_entropy&lt;distinct_1\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 2},\n        {\"pair\": \"token_entropy&lt;distinct_2\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": true, \"ty\": false}, \"equal_weight_K\": 3, \"equal_weight_sig\": true, \"current_consensus_votes\": 2},\n        {\"pair\": \"token_entropy&lt;distinct_3\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": true, \"ty\": false}, \"equal_weight_K\": 3, \"equal_weight_sig\": true, \"current_consensus_votes\": 2},\n        {\"pair\": \"token_entropy&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": true, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"ece&lt;distinct_1\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": true}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 2},\n        {\"pair\": \"ece&lt;distinct_2\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"ece&lt;distinct_3\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": true}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"ece&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1}\n      ],\n      \"equal_weight_K3\": 2,\n      \"current_K3\": 0,\n      \"difference\": 2\n    },\n    {\n      \"exp_id\": \"a010_s42_fp32\",\n      \"alpha\": 0.1,\n      \"T\": 10,\n      \"pairs\": [\n        {\"pair\": \"token_entropy&lt;distinct_1\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 2},\n        {\"pair\": \"token_entropy&lt;distinct_2\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 2},\n        {\"pair\": \"token_entropy&lt;distinct_3\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": true}, \"equal_weight_K\": 3, \"equal_weight_sig\": true, \"current_consensus_votes\": 2},\n        {\"pair\": \"token_entropy&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": false, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"ece&lt;distinct_1\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"ece&lt;distinct_2\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": true}, \"equal_weight_K\": 3, \"equal_weight_sig\": true, \"current_consensus_votes\": 2},\n        {\"pair\": \"ece&lt;distinct_3\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": true}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"ece&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": true}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 2}\n      ],\n      \"equal_weight_K3\": 2,\n      \"current_K3\": 0,\n      \"difference\": 2\n    },\n    {\n      \"exp_id\": \"a025_s42_fp32\",\n      \"alpha\": 0.25,\n      \"T\": 10,\n      \"pairs\": [\n        {\"pair\": \"token_entropy&lt;distinct_1\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"token_entropy&lt;distinct_2\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"token_entropy&lt;distinct_3\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"token_entropy&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": true}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"ece&lt;distinct_1\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"ece&lt;distinct_2\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"ece&lt;distinct_3\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"ece&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 1}\n      ],\n      \"equal_weight_K3\": 0,\n      \"current_K3\": 0,\n      \"difference\": 0\n    },\n    {\n      \"exp_id\": \"a025_s43_fp32\",\n      \"alpha\": 0.25,\n      \"T\": 10,\n      \"pairs\": [\n        {\"pair\": \"token_entropy&lt;distinct_1\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": true}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"token_entropy&lt;distinct_2\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"token_entropy&lt;distinct_3\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"token_entropy&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"ece&lt;distinct_1\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"ece&lt;distinct_2\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"ece&lt;distinct_3\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"ece&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 0}\n      ],\n      \"equal_weight_K3\": 0,\n      \"current_K3\": 0,\n      \"difference\": 0\n    },\n    {\n      \"exp_id\": \"a045_s42_fp32\",\n      \"alpha\": 0.45,\n      \"T\": 10,\n      \"pairs\": [\n        {\"pair\": \"token_entropy&lt;distinct_1\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"token_entropy&lt;distinct_2\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"token_entropy&lt;distinct_3\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"token_entropy&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"ece&lt;distinct_1\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"ece&lt;distinct_2\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"ece&lt;distinct_3\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"ece&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 1}\n      ],\n      \"equal_weight_K3\": 0,\n      \"current_K3\": 0,\n      \"difference\": 0\n    },\n    {\n      \"exp_id\": \"a045_s43_fp32\",\n      \"alpha\": 0.45,\n      \"T\": 10,\n      \"pairs\": [\n        {\"pair\": \"token_entropy&lt;distinct_1\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"token_entropy&lt;distinct_2\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"token_entropy&lt;distinct_3\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": true}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"token_entropy&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"ece&lt;distinct_1\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"ece&lt;distinct_2\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"ece&lt;distinct_3\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": true}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"ece&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 1}\n      ],\n      \"equal_weight_K3\": 0,\n      \"current_K3\": 0,\n      \"difference\": 0\n    },\n    {\n      \"exp_id\": \"a050_s42_fp32\",\n      \"alpha\": 0.5,\n      \"T\": 10,\n      \"pairs\": [\n        {\"pair\": \"token_entropy&lt;distinct_1\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": true}, \"equal_weight_K\": 4, \"equal_weight_sig\": true, \"current_consensus_votes\": 3},\n        {\"pair\": \"token_entropy&lt;distinct_2\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": true, \"ty\": true}, \"equal_weight_K\": 5, \"equal_weight_sig\": true, \"current_consensus_votes\": 4},\n        {\"pair\": \"token_entropy&lt;distinct_3\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": true, \"ty\": false}, \"equal_weight_K\": 4, \"equal_weight_sig\": true, \"current_consensus_votes\": 3},\n        {\"pair\": \"token_entropy&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"ece&lt;distinct_1\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 3, \"equal_weight_sig\": true, \"current_consensus_votes\": 3},\n        {\"pair\": \"ece&lt;distinct_2\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": true, \"ty\": false}, \"equal_weight_K\": 4, \"equal_weight_sig\": true, \"current_consensus_votes\": 4},\n        {\"pair\": \"ece&lt;distinct_3\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": true, \"ty\": true}, \"equal_weight_K\": 5, \"equal_weight_sig\": true, \"current_consensus_votes\": 5},\n        {\"pair\": \"ece&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 0}\n      ],\n      \"equal_weight_K3\": 6,\n      \"current_K3\": 6,\n      \"difference\": 0\n    },\n    {\n      \"exp_id\": \"a060_s42_fp32_v4\",\n      \"alpha\": 0.6,\n      \"T\": 10,\n      \"pairs\": [\n        {\"pair\": \"token_entropy&lt;distinct_1\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"token_entropy&lt;distinct_2\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"token_entropy&lt;distinct_3\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"token_entropy&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": true}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 2},\n        {\"pair\": \"ece&lt;distinct_1\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"ece&lt;distinct_2\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"ece&lt;distinct_3\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"ece&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 1}\n      ],\n      \"equal_weight_K3\": 0,\n      \"current_K3\": 0,\n      \"difference\": 0\n    },\n    {\n      \"exp_id\": \"a075_s42_fp32\",\n      \"alpha\": 0.75,\n      \"T\": 10,\n      \"pairs\": [\n        {\"pair\": \"token_entropy&lt;distinct_1\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 3, \"equal_weight_sig\": true, \"current_consensus_votes\": 3},\n        {\"pair\": \"token_entropy&lt;distinct_2\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 3, \"equal_weight_sig\": true, \"current_consensus_votes\": 3},\n        {\"pair\": \"token_entropy&lt;distinct_3\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 3, \"equal_weight_sig\": true, \"current_consensus_votes\": 3},\n        {\"pair\": \"token_entropy&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": false, \"threshold\": false, \"ty\": true}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"ece&lt;distinct_1\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 3, \"equal_weight_sig\": true, \"current_consensus_votes\": 3},\n        {\"pair\": \"ece&lt;distinct_2\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 3, \"equal_weight_sig\": true, \"current_consensus_votes\": 3},\n        {\"pair\": \"ece&lt;distinct_3\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 3, \"equal_weight_sig\": true, \"current_consensus_votes\": 3},\n        {\"pair\": \"ece&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": true}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 2}\n      ],\n      \"equal_weight_K3\": 6,\n      \"current_K3\": 6,\n      \"difference\": 0\n    },\n    {\n      \"exp_id\": \"t20/a100_s42_fp32\",\n      \"alpha\": 1.0,\n      \"T\": 20,\n      \"pairs\": [\n        {\"pair\": \"token_entropy&lt;distinct_1\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": true, \"ty\": false}, \"equal_weight_K\": 4, \"equal_weight_sig\": true, \"current_consensus_votes\": 4},\n        {\"pair\": \"token_entropy&lt;distinct_2\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": true, \"ty\": false}, \"equal_weight_K\": 4, \"equal_weight_sig\": true, \"current_consensus_votes\": 4},\n        {\"pair\": \"token_entropy&lt;distinct_3\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": true, \"ty\": false}, \"equal_weight_K\": 4, \"equal_weight_sig\": true, \"current_consensus_votes\": 4},\n        {\"pair\": \"token_entropy&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"ece&lt;distinct_1\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": true, \"ty\": true}, \"equal_weight_K\": 5, \"equal_weight_sig\": true, \"current_consensus_votes\": 5},\n        {\"pair\": \"ece&lt;distinct_2\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": true, \"ty\": true}, \"equal_weight_K\": 5, \"equal_weight_sig\": true, \"current_consensus_votes\": 5},\n        {\"pair\": \"ece&lt;distinct_3\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": true, \"ty\": false}, \"equal_weight_K\": 4, \"equal_weight_sig\": true, \"current_consensus_votes\": 4},\n        {\"pair\": \"ece&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 1}\n      ],\n      \"equal_weight_K3\": 6,\n      \"current_K3\": 6,\n      \"difference\": 0\n    },\n    {\n      \"exp_id\": \"t20/a045_s42_fp32\",\n      \"alpha\": 0.45,\n      \"T\": 20,\n      \"pairs\": [\n        {\"pair\": \"token_entropy&lt;distinct_1\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": true, \"ty\": false}, \"equal_weight_K\": 3, \"equal_weight_sig\": true, \"current_consensus_votes\": 2},\n        {\"pair\": \"token_entropy&lt;distinct_2\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": true, \"ty\": true}, \"equal_weight_K\": 5, \"equal_weight_sig\": true, \"current_consensus_votes\": 4},\n        {\"pair\": \"token_entropy&lt;distinct_3\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 3, \"equal_weight_sig\": true, \"current_consensus_votes\": 2},\n        {\"pair\": \"token_entropy&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"ece&lt;distinct_1\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": true, \"ty\": false}, \"equal_weight_K\": 4, \"equal_weight_sig\": true, \"current_consensus_votes\": 3},\n        {\"pair\": \"ece&lt;distinct_2\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": true, \"ty\": false}, \"equal_weight_K\": 4, \"equal_weight_sig\": true, \"current_consensus_votes\": 3},\n        {\"pair\": \"ece&lt;distinct_3\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 3, \"equal_weight_sig\": true, \"current_consensus_votes\": 2},\n        {\"pair\": \"ece&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": true}, \"equal_weight_K\": 3, \"equal_weight_sig\": true, \"current_consensus_votes\": 2}\n      ],\n      \"equal_weight_K3\": 7,\n      \"current_K3\": 3,\n      \"difference\": 4\n    }\n  ],\n  \"summary\": {\n    \"total_experiments\": 11,\n    \"experiments_with_difference\": 3,\n    \"max_difference\": 4,\n    \"total_pair_vote_differences\": 59,\n    \"naive_xcorr_direction_filtered_count\": 57,\n    \"diff_xcorr_direction_filtered_count\": 10,\n    \"note\": \"equal-weight = significance only (no direction filter); current = significance + direction filter (D111: peak_lag < 0) for xcorr methods\",\n    \"conclusion\": \"Equal-weight (no direction filter) vs current (with D111 direction filter) differs in 3/11 experiments. The difference is driven by NaiveXCorr having significance with peak_lag > 0 (reverse direction), which passes significance-only check but is filtered by D111. Critical: null experiment (a=0.00) inflates from 0 to 2 K>=3 pairs without direction filter. Direction filtering is essential for FPR control. At strong signal (a>=0.50 T=10), both methods agree perfectly at K3 level. Largest divergence at t20/a045 (+4 pairs) where NaiveXCorr is broadly significant but often in wrong direction.\"\n  }\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/equal_weight_vs_current_k3.json",
    "content": "{\n  \"experiments\": [\n    {\n      \"exp_id\": \"a000_s42_fp32\",\n      \"alpha\": 0.0,\n      \"T\": 10,\n      \"pairs\": [\n        {\"pair\": \"token_entropy&lt;distinct_1\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 2},\n        {\"pair\": \"token_entropy&lt;distinct_2\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": true, \"ty\": false}, \"equal_weight_K\": 3, \"equal_weight_sig\": true, \"current_consensus_votes\": 2},\n        {\"pair\": \"token_entropy&lt;distinct_3\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": true, \"ty\": false}, \"equal_weight_K\": 3, \"equal_weight_sig\": true, \"current_consensus_votes\": 2},\n        {\"pair\": \"token_entropy&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": true, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"ece&lt;distinct_1\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": true}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 2},\n        {\"pair\": \"ece&lt;distinct_2\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"ece&lt;distinct_3\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": true}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"ece&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1}\n      ],\n      \"equal_weight_K3\": 2,\n      \"current_K3\": 0,\n      \"difference\": 2\n    },\n    {\n      \"exp_id\": \"a010_s42_fp32\",\n      \"alpha\": 0.1,\n      \"T\": 10,\n      \"pairs\": [\n        {\"pair\": \"token_entropy&lt;distinct_1\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 2},\n        {\"pair\": \"token_entropy&lt;distinct_2\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 2},\n        {\"pair\": \"token_entropy&lt;distinct_3\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": true}, \"equal_weight_K\": 3, \"equal_weight_sig\": true, \"current_consensus_votes\": 2},\n        {\"pair\": \"token_entropy&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": false, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"ece&lt;distinct_1\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"ece&lt;distinct_2\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": true}, \"equal_weight_K\": 3, \"equal_weight_sig\": true, \"current_consensus_votes\": 2},\n        {\"pair\": \"ece&lt;distinct_3\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": true}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"ece&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": true}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 2}\n      ],\n      \"equal_weight_K3\": 2,\n      \"current_K3\": 0,\n      \"difference\": 2\n    },\n    {\n      \"exp_id\": \"a025_s42_fp32\",\n      \"alpha\": 0.25,\n      \"T\": 10,\n      \"pairs\": [\n        {\"pair\": \"token_entropy&lt;distinct_1\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"token_entropy&lt;distinct_2\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"token_entropy&lt;distinct_3\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"token_entropy&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": true}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"ece&lt;distinct_1\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"ece&lt;distinct_2\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"ece&lt;distinct_3\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"ece&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 1}\n      ],\n      \"equal_weight_K3\": 0,\n      \"current_K3\": 0,\n      \"difference\": 0\n    },\n    {\n      \"exp_id\": \"a025_s43_fp32\",\n      \"alpha\": 0.25,\n      \"T\": 10,\n      \"pairs\": [\n        {\"pair\": \"token_entropy&lt;distinct_1\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": true}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"token_entropy&lt;distinct_2\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"token_entropy&lt;distinct_3\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"token_entropy&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"ece&lt;distinct_1\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"ece&lt;distinct_2\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"ece&lt;distinct_3\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"ece&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 0}\n      ],\n      \"equal_weight_K3\": 0,\n      \"current_K3\": 0,\n      \"difference\": 0\n    },\n    {\n      \"exp_id\": \"a045_s42_fp32\",\n      \"alpha\": 0.45,\n      \"T\": 10,\n      \"pairs\": [\n        {\"pair\": \"token_entropy&lt;distinct_1\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"token_entropy&lt;distinct_2\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"token_entropy&lt;distinct_3\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"token_entropy&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"ece&lt;distinct_1\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"ece&lt;distinct_2\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"ece&lt;distinct_3\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"ece&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 1}\n      ],\n      \"equal_weight_K3\": 0,\n      \"current_K3\": 0,\n      \"difference\": 0\n    },\n    {\n      \"exp_id\": \"a045_s43_fp32\",\n      \"alpha\": 0.45,\n      \"T\": 10,\n      \"pairs\": [\n        {\"pair\": \"token_entropy&lt;distinct_1\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"token_entropy&lt;distinct_2\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"token_entropy&lt;distinct_3\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": true}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"token_entropy&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"ece&lt;distinct_1\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"ece&lt;distinct_2\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"ece&lt;distinct_3\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": true}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"ece&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 1}\n      ],\n      \"equal_weight_K3\": 0,\n      \"current_K3\": 0,\n      \"difference\": 0\n    },\n    {\n      \"exp_id\": \"a050_s42_fp32\",\n      \"alpha\": 0.5,\n      \"T\": 10,\n      \"pairs\": [\n        {\"pair\": \"token_entropy&lt;distinct_1\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": true}, \"equal_weight_K\": 4, \"equal_weight_sig\": true, \"current_consensus_votes\": 3},\n        {\"pair\": \"token_entropy&lt;distinct_2\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": true, \"ty\": true}, \"equal_weight_K\": 5, \"equal_weight_sig\": true, \"current_consensus_votes\": 4},\n        {\"pair\": \"token_entropy&lt;distinct_3\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": true, \"ty\": false}, \"equal_weight_K\": 4, \"equal_weight_sig\": true, \"current_consensus_votes\": 3},\n        {\"pair\": \"token_entropy&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"ece&lt;distinct_1\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 3, \"equal_weight_sig\": true, \"current_consensus_votes\": 3},\n        {\"pair\": \"ece&lt;distinct_2\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": true, \"ty\": false}, \"equal_weight_K\": 4, \"equal_weight_sig\": true, \"current_consensus_votes\": 4},\n        {\"pair\": \"ece&lt;distinct_3\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": true, \"ty\": true}, \"equal_weight_K\": 5, \"equal_weight_sig\": true, \"current_consensus_votes\": 5},\n        {\"pair\": \"ece&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 0}\n      ],\n      \"equal_weight_K3\": 6,\n      \"current_K3\": 6,\n      \"difference\": 0\n    },\n    {\n      \"exp_id\": \"a060_s42_fp32_v4\",\n      \"alpha\": 0.6,\n      \"T\": 10,\n      \"pairs\": [\n        {\"pair\": \"token_entropy&lt;distinct_1\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"token_entropy&lt;distinct_2\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"token_entropy&lt;distinct_3\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"token_entropy&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": true}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 2},\n        {\"pair\": \"ece&lt;distinct_1\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"ece&lt;distinct_2\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"ece&lt;distinct_3\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"ece&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 1}\n      ],\n      \"equal_weight_K3\": 0,\n      \"current_K3\": 0,\n      \"difference\": 0\n    },\n    {\n      \"exp_id\": \"a075_s42_fp32\",\n      \"alpha\": 0.75,\n      \"T\": 10,\n      \"pairs\": [\n        {\"pair\": \"token_entropy&lt;distinct_1\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 3, \"equal_weight_sig\": true, \"current_consensus_votes\": 3},\n        {\"pair\": \"token_entropy&lt;distinct_2\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 3, \"equal_weight_sig\": true, \"current_consensus_votes\": 3},\n        {\"pair\": \"token_entropy&lt;distinct_3\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 3, \"equal_weight_sig\": true, \"current_consensus_votes\": 3},\n        {\"pair\": \"token_entropy&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": false, \"threshold\": false, \"ty\": true}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"ece&lt;distinct_1\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 3, \"equal_weight_sig\": true, \"current_consensus_votes\": 3},\n        {\"pair\": \"ece&lt;distinct_2\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 3, \"equal_weight_sig\": true, \"current_consensus_votes\": 3},\n        {\"pair\": \"ece&lt;distinct_3\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 3, \"equal_weight_sig\": true, \"current_consensus_votes\": 3},\n        {\"pair\": \"ece&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": true}, \"equal_weight_K\": 2, \"equal_weight_sig\": false, \"current_consensus_votes\": 2}\n      ],\n      \"equal_weight_K3\": 6,\n      \"current_K3\": 6,\n      \"difference\": 0\n    },\n    {\n      \"exp_id\": \"t20/a100_s42_fp32\",\n      \"alpha\": 1.0,\n      \"T\": 20,\n      \"pairs\": [\n        {\"pair\": \"token_entropy&lt;distinct_1\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": true, \"ty\": false}, \"equal_weight_K\": 4, \"equal_weight_sig\": true, \"current_consensus_votes\": 4},\n        {\"pair\": \"token_entropy&lt;distinct_2\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": true, \"ty\": false}, \"equal_weight_K\": 4, \"equal_weight_sig\": true, \"current_consensus_votes\": 4},\n        {\"pair\": \"token_entropy&lt;distinct_3\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": true, \"ty\": false}, \"equal_weight_K\": 4, \"equal_weight_sig\": true, \"current_consensus_votes\": 4},\n        {\"pair\": \"token_entropy&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 1},\n        {\"pair\": \"ece&lt;distinct_1\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": true, \"ty\": true}, \"equal_weight_K\": 5, \"equal_weight_sig\": true, \"current_consensus_votes\": 5},\n        {\"pair\": \"ece&lt;distinct_2\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": true, \"ty\": true}, \"equal_weight_K\": 5, \"equal_weight_sig\": true, \"current_consensus_votes\": 5},\n        {\"pair\": \"ece&lt;distinct_3\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": true, \"ty\": false}, \"equal_weight_K\": 4, \"equal_weight_sig\": true, \"current_consensus_votes\": 4},\n        {\"pair\": \"ece&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 1}\n      ],\n      \"equal_weight_K3\": 6,\n      \"current_K3\": 6,\n      \"difference\": 0\n    },\n    {\n      \"exp_id\": \"t20/a045_s42_fp32\",\n      \"alpha\": 0.45,\n      \"T\": 20,\n      \"pairs\": [\n        {\"pair\": \"token_entropy&lt;distinct_1\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": true, \"ty\": false}, \"equal_weight_K\": 3, \"equal_weight_sig\": true, \"current_consensus_votes\": 2},\n        {\"pair\": \"token_entropy&lt;distinct_2\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": true, \"ty\": true}, \"equal_weight_K\": 5, \"equal_weight_sig\": true, \"current_consensus_votes\": 4},\n        {\"pair\": \"token_entropy&lt;distinct_3\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 3, \"equal_weight_sig\": true, \"current_consensus_votes\": 2},\n        {\"pair\": \"token_entropy&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": false, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 1, \"equal_weight_sig\": false, \"current_consensus_votes\": 0},\n        {\"pair\": \"ece&lt;distinct_1\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": true, \"ty\": false}, \"equal_weight_K\": 4, \"equal_weight_sig\": true, \"current_consensus_votes\": 3},\n        {\"pair\": \"ece&lt;distinct_2\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": true, \"ty\": false}, \"equal_weight_K\": 4, \"equal_weight_sig\": true, \"current_consensus_votes\": 3},\n        {\"pair\": \"ece&lt;distinct_3\", \"methods\": {\"permg\": true, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": false}, \"equal_weight_K\": 3, \"equal_weight_sig\": true, \"current_consensus_votes\": 2},\n        {\"pair\": \"ece&lt;mauve\", \"methods\": {\"permg\": false, \"diffxcorr\": true, \"naive\": true, \"threshold\": false, \"ty\": true}, \"equal_weight_K\": 3, \"equal_weight_sig\": true, \"current_consensus_votes\": 2}\n      ],\n      \"equal_weight_K3\": 7,\n      \"current_K3\": 3,\n      \"difference\": 4\n    }\n  ],\n  \"summary\": {\n    \"total_experiments\": 11,\n    \"experiments_with_difference\": 3,\n    \"max_difference\": 4,\n    \"total_pair_vote_differences\": 59,\n    \"naive_xcorr_direction_filtered_count\": 57,\n    \"diff_xcorr_direction_filtered_count\": 10,\n    \"note\": \"equal-weight = significance only (no direction filter); current = significance + direction filter (D111: peak_lag < 0) for xcorr methods\",\n    \"conclusion\": \"Equal-weight (no direction filter) vs current (with D111 direction filter) differs in 3/11 experiments. The difference is driven by NaiveXCorr having significance with peak_lag > 0 (reverse direction), which passes significance-only check but is filtered by D111. Critical: null experiment (a=0.00) inflates from 0 to 2 K>=3 pairs without direction filter. Direction filtering is essential for FPR control. At strong signal (a>=0.50 T=10), both methods agree perfectly at K3 level. Largest divergence at t20/a045 (+4 pairs) where NaiveXCorr is broadly significant but often in wrong direction.\"\n  }\n}\n"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-20T20:54:17.740232+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/equal_weight_vs_current_k3.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-20T20:54:17.740411+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-20T20:54:17.740542+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-20T20:54:17.740671+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "equal_weight_vs_current_k3",
  "type": "data",
  "description": "Equal-weight K≥3 (no direction filter) vs current consensus K≥3 (with D111 direction filter) comparison across 11 experiments. Key finding: both systems are equal-weight; the real difference is D111 direction filtering on xcorr methods. Without it, null (α=0.00) inflates from 0→2 K≥3 pairs. NaiveXCorr is the main driver (57/59 pair-level differences).",
  "project": "distrib_canary_collapse",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/equal_weight_vs_current_k3.json",
  "tags": "['mmct', 'consensus', 'direction_filter', 'c2', 'fpr']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "equal_weight_vs_current_k3",
    "type": "data",
    "description": "Equal-weight K≥3 (no direction filter) vs current consensus K≥3 (with D111 direction filter) comparison across 11 experiments. Key finding: both systems are equal-weight; the real difference is D111 direction filtering on xcorr methods. Without it, null (α=0.00) inflates from 0→2 K≥3 pairs. NaiveXCorr is the main driver (57/59 pair-level differences).",
    "project": "distrib_canary_collapse",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/equal_weight_vs_current_k3.json",
    "tags": "['mmct', 'consensus', 'direction_filter', 'c2', 'fpr']"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-20T20:54:17.740830+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260520_75160c\", \"name\": \"equal_weight_vs_current_k3\", \"type\": \"data\", \"description\": \"Equal-weight K≥3 (no direction filter) vs current consensus K≥3 (with D111 direction filter) comparison across 11 experiments. Key finding: both systems are equal-weight; the real difference is D111 direction filtering on xcorr methods. Without it, null (α=0.00) inflates from 0→2 K≥3 pairs. NaiveXCorr is the main driver (57/59 pair-level differences).\", \"path\": \"projects/distrib_canary_collapse/artifacts/_project/data/equal_weight_vs_current_k3.json\", \"url\": null, \"project\": \"distrib_canary_collapse\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-20T20:54:01.308941+00:00\", \"tags\": [\"mmct\", \"consensus\", \"direction_filter\", \"c2\", \"fpr\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-20T20:54:17.741008+00:00_

分析完成。核心发现：

**当前 consensus 系统已经是 equal-weight（每方法 1 票），不存在 FPR-inverse weighting。** 实际差异来自 D111 方向过滤（xcorr 方法要求 `peak_lag < 0`）。

### K≥3 对比汇总

| 实验 | α | T | Equal-weight K3 | Current K3 | Diff |
|------|-----|-----|-----------------|------------|------|
| a000_s42 | 0.00 | 10 | **2** | 0 | **+2** |
| a010_s42 | 0.10 | 10 | **2** | 0 | **+2** |
| a025_s42 | 0.25 | 10 | 0 | 0 | 0 |
| a025_s43 | 0.25 | 10 | 0 | 0 | 0 |
| a045_s42 | 0.45 | 10 | 0 | 0 | 0 |
| a045_s43 | 0.45 | 10 | 0 | 0 | 0 |
| a050_s42 | 0.50 | 10 | 6 | 6 | 0 |
| a060_s42_v4 | 0.60 | 10 | 0 | 0 | 0 |
| a075_s42 | 0.75 | 10 | 6 | 6 | 0 |
| t20/a100 | 1.00 | 20 | 6 | 6 | 0 |
| t20/a045 | 0.45 | 20 | **7** | 3 | **+4** |

### 关键结论

1. **3/11 实验有 K3 差异**，全部方向为 equal-weight 更高（去掉方向过滤 = 更多 false positives）
2. **NaiveXCorr 是主要驱动因素**：59 个 pair-level vote 差异中，57 个来自 NaiveXCorr 被方向过滤掉（它在大量 pair 上 significant 但 peak_lag > 0，即反向因果）
3. **null 实验 FPR 失控**：α=0.00 从 0→2 K≥3 pairs — 去掉方向过滤直接破坏 type-I error control
4. **强信号实验完全一致**：α≥0.50 T=10 的 K3 count 在两种方案下完全相同
5. **t20/a045 差异最大**（+4）：T=20 给 NaiveXCorr 更多 lag 组合空间，方向错误的显著性更多

**结论：不应采用去掉方向过滤的 equal-weight。当前系统（equal-weight + D111 方向过滤）已是最合理方案。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_r5_equal_weight_mmct_20260520T204829"
}
```

</details>

---
