# analysis exp 025 n ablation

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 57
- **Recorded user turns:** 0
- **Tool calls:** 28
- **Original source:** `logs/chats/worker_analysis_exp_025_n_ablation_20260516T121619.jsonl`
- **Structured JSON:** [`7a84b7957a4f80a19325.json`](../../sessions/7a/7a84b7957a4f80a19325.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

57 recorded events

### Tool call

_source line 1 · 2026-05-16T12:20:08.980294+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__detect_image",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__detect_image",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T12:20:08.980807+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T12:20:08.981081+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T12:20:08.981410+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"analysis_epsilon_sweep\\nanalysis_fk_bootstrap_ci.json\\nanalysis_fk_bootstrap_per_instance.json\\nanalysis_lp_range_cdf.json\\nanalysis_lp_range_cdf_n16_3seed.json\\nanalysis_multiseed_selection_f1.json\\nanalysis_round8\\nanalysis_scierc_n16_3seed_selection_f1.json\\nanalysis_scierc_n16_3seed_selection_f1_merged.json\\nanalysis_scierc_re_n16_3seed_selection_f1.json\\nanalysis_unified_rho_full.json\\nbootstrap_ci_nscaling\\nbootstrap_ci_summary.json\\nbootstrap_ci_tables.tex\\nconditional_filter_diagnosis.json\\nd108_greedy_f1\\nd108_lp_vc_combination\\nd108_mbr_within_rho\\nd108_q4q5\\nd110_4b_degeneracy\\nd112_disk_cleanup\\nd112_hybrid_strategy\\nd112_mf3_random_single\\nd112_table2_fix\\nd114_auroc_investigation\\nexp001_n16_seed123\\nexp001_n16_seed123_200only\\nexp001_n16_seed123_200only_backup\\nexp001_n16_seed123_full\\nexp001_n16_seed123_run.log\\nexp001_n16_seed42\\nexp001_n16_seed42_200only_backup\\nexp001_n16_seed42_run.log\\nexp001_n16_seed456\\nexp001_n16_seed456_200only\\nexp001_n16_seed456_run.log\\nexp001_seed123_t10_full\\nexp001_seed123_t10_full.log\\nexp001_seed456_t10_full\\nexp001_seed456_t10_full.log\\nexp002_conll2003\\nexp003_wnut17_dryrun\\nexp003_wnut17_eval\\nexp003_wnut17_eval.log\\nexp003_wnut17_pilot\\nexp003_wnut17_pilot.log\\nexp004_re_diagnostic\\nexp004v2_re_diagnostic\\nexp007_llama_dryrun\\nexp007_llama_inference\\nexp008_re_n16\\nexp008_re_n16_200only\\nexp008_re_n16_t10_full\\nexp008_re_n16_t10_full.log\\nexp009_stratification_results.json\\nexp010_selection_curves\\nexp016_signal_ensemble\\nexp018_3seed_5signal_results.json\\nexp_001_seed123_v2\\nexp_001_seed123_v2_r1024\\nexp_001_seed42_v2\\nexp_001_seed42_v2_r1024\\nexp_001_seed456_v2\\nexp_001_seed456_v2_ner\\nexp_001_seed456_v2_ner.log\\nexp_001_seed456_v2_ner_r1024\\nexp_002_conll_n16\\nexp_002_conll_n16.log\\nexp_002_conll_n16_r1024\\nexp_003_wnut17_v2_infer\\nexp_005_v2_temperature\\nexp_006_v2\\nexp_006_v2_run.lo
…[truncated 2438 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T12:20:08.981669+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2 -name \"*.jsonl\" -o -name \"*samples*\" -o -name \"*signal*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2 -name \"*.jsonl\" -o -name \"*samples*\" -o -name \"*signal*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T12:20:08.981942+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2/samples.jsonl\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2/all_signals_report.json\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2/re_all_signals_report.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T12:20:08.982182+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/output/exp_023_rank8_inference -name \"*.jsonl\" -o -name \"*samples*\" -o -name \"*signal*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/output/exp_023_rank8_inference -name \"*.jsonl\" -o -name \"*samples*\" -o -name \"*signal*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T12:20:08.982407+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_023_rank8_inference/samples.jsonl\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_023_rank8_inference/all_signals_5signal.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T12:20:08.982611+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed42 -name \"*.jsonl\" -o -name \"*samples*\" -o -name \"*signal*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed42 -name \"*.jsonl\" -o -name \"*samples*\" -o -name \"*signal*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T12:20:08.982817+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed42/samples.jsonl\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed42/exp001_all_signals_report.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T12:20:08.983035+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -5 /root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -5 /root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T12:20:08.983709+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"id\\\": \\\"X96-1059_sent000\\\", \\\"text\\\": \\\"Recognition of proper nouns in Japanese text has been studied as a part of the more general problem of morphological analysis in Japanese text processing -LRB- -LSB- 1 -RSB- -LSB- 2 -RSB- -RRB- .\\\", \\\"gold\\\": {\\\"entities\\\": [{\\\"text\\\": \\\"Recognition of proper nouns\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 0, \\\"end\\\": 27}, {\\\"text\\\": \\\"proper nouns\\\", \\\"type\\\": \\\"OtherScientificTerm\\\", \\\"start\\\": 15, \\\"end\\\": 27}, {\\\"text\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"Material\\\", \\\"start\\\": 31, \\\"end\\\": 44}, {\\\"text\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 103, \\\"end\\\": 125}, {\\\"text\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 129, \\\"end\\\": 153}], \\\"relations\\\": [{\\\"head\\\": \\\"Recognition of proper nouns\\\", \\\"tail\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"PART-OF\\\", \\\"head_start\\\": 0, \\\"head_end\\\": 27, \\\"tail_start\\\": 103, \\\"tail_end\\\": 125}, {\\\"head\\\": \\\"proper nouns\\\", \\\"tail\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"PART-OF\\\", \\\"head_start\\\": 15, \\\"head_end\\\": 27, \\\"tail_start\\\": 31, \\\"tail_end\\\": 44}, {\\\"head\\\": \\\"morphological analysis\\\", \\\"tail\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"USED-FOR\\\", \\\"head_start\\\": 103, \\\"head_end\\\": 125, \\\"tail_start\\\": 129, \\\"tail_end\\\": 153}], \\\"events\\\": []}, \\\"samples\\\": [{\\\"entities\\\": [{\\\"text\\\": \\\"Recognition of proper nouns\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 0, \\\"end\\\": 27}, {\\\"text\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"Material\\\", \\\"start\\\": 31, \\\"end\\\": 44}, {\\\"text\\\": \\\"morphological analysis in Japanese text processing\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 103, \\\"end\\\
…[truncated 9102 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T12:20:08.983985+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -100 /root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2/all_signals_report.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -100 /root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2/all_signals_report.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T12:20:08.984308+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"full\\\": {\\n    \\\"n\\\": 529,\\n    \\\"pct_perfect\\\": 0.2495274102079395,\\n    \\\"greedy_f1_mean\\\": 0.6442,\\n    \\\"metrics\\\": {\\n      \\\"SJ\\\": {\\n        \\\"rho\\\": 0.428,\\n        \\\"rho_ci95\\\": [\\n          0.3426,\\n          0.5029\\n        ],\\n        \\\"p_rho\\\": 5.59950452013284e-25,\\n        \\\"auroc\\\": 0.7368,\\n        \\\"auroc_ci95\\\": [\\n          0.681,\\n          0.7886\\n        ],\\n        \\\"ece\\\": 0.4575\\n      },\\n      \\\"FK\\\": {\\n        \\\"rho\\\": 0.2809,\\n        \\\"rho_ci95\\\": [\\n          0.1856,\\n          0.3746\\n        ],\\n        \\\"p_rho\\\": 4.7946512827215673e-11,\\n        \\\"auroc\\\": 0.6099,\\n        \\\"auroc_ci95\\\": [\\n          0.5436,\\n          0.6809\\n        ],\\n        \\\"ece\\\": 0.4822\\n      },\\n      \\\"logprob\\\": {\\n        \\\"rho\\\": 0.2194,\\n        \\\"rho_ci95\\\": [\\n          0.131,\\n          0.2999\\n        ],\\n        \\\"p_rho\\\": 3.4800443839281296e-07,\\n        \\\"auroc\\\": 0.587,\\n        \\\"auroc_ci95\\\": [\\n          0.526,\\n          0.6448\\n        ],\\n        \\\"ece\\\": 0.7073\\n      },\\n      \\\"EM\\\": {\\n        \\\"rho\\\": 0.3347,\\n        \\\"rho_ci95\\\": [\\n          0.2505,\\n          0.4154\\n        ],\\n        \\\"p_rho\\\": 2.6160621283755218e-15,\\n        \\\"auroc\\\": 0.7902,\\n        \\\"auroc_ci95\\\": [\\n          0.7404,\\n          0.8354\\n        ],\\n        \\\"ece\\\": 0.332\\n      },\\n      \\\"voting_conf\\\": {\\n        \\\"rho\\\": 0.4408,\\n        \\\"rho_ci95\\\": [\\n          0.3588,\\n          0.5154\\n        ],\\n        \\\"p_rho\\\": 1.490794408703245e-26,\\n        \\\"auroc\\\": 0.734,\\n        \\\"auroc_ci95\\\": [\\n          0.6795,\\n          0.7848\\n        ],\\n        \\\"ece\\\": 0.32\\n      }\\n    }\\n  },\\n  \\\"conditional\\\": {\\n    \\\"n\\\": 477,\\n    \\\"pct_p
…[truncated 626 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T12:20:08.984565+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -100 /root/autodl-tmp/struct_self_consist_ie/output/exp_023_rank8_inference/all_signals_5signal.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -100 /root/autodl-tmp/struct_self_consist_ie/output/exp_023_rank8_inference/all_signals_5signal.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T12:20:08.984876+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"ner\\\": {\\n    \\\"full\\\": {\\n      \\\"n\\\": 529,\\n      \\\"greedy_f1_mean\\\": 0.6397455621463182,\\n      \\\"metrics\\\": {\\n        \\\"SJ\\\": {\\n          \\\"rho\\\": 0.3649,\\n          \\\"tau\\\": 0.2652,\\n          \\\"AUROC\\\": 0.689,\\n          \\\"delta_vs_r16\\\": 0.005\\n        },\\n        \\\"FK\\\": {\\n          \\\"rho\\\": 0.2838,\\n          \\\"tau\\\": 0.2096,\\n          \\\"AUROC\\\": 0.6002,\\n          \\\"delta_vs_r16\\\": 0.0173\\n        },\\n        \\\"LP\\\": {\\n          \\\"rho\\\": 0.2105,\\n          \\\"tau\\\": 0.152,\\n          \\\"AUROC\\\": 0.6054,\\n          \\\"delta_vs_r16\\\": 0.0053\\n        },\\n        \\\"EM\\\": {\\n          \\\"rho\\\": 0.2562,\\n          \\\"tau\\\": 0.1949,\\n          \\\"AUROC\\\": 0.7265,\\n          \\\"delta_vs_r16\\\": -0.0383\\n        },\\n        \\\"VC\\\": {\\n          \\\"rho\\\": 0.394,\\n          \\\"tau\\\": 0.2905,\\n          \\\"AUROC\\\": 0.6886,\\n          \\\"delta_vs_r16\\\": 0.0148\\n        }\\n      },\\n      \\\"selection\\\": {\\n        \\\"greedy_f1\\\": 0.6397455621463182,\\n        \\\"oracle_f1\\\": 0.7998047654558273,\\n        \\\"oracle_headroom\\\": 0.16005920330950918,\\n        \\\"degeneracy_rate\\\": 0.07183364839319471,\\n        \\\"n_degenerate\\\": 38,\\n        \\\"n_total\\\": 529,\\n        \\\"selection_f1\\\": {\\n          \\\"SJ\\\": 0.6306195247232721,\\n          \\\"FK\\\": 0.6264727263420692,\\n          \\\"VC\\\": 0.5918597627954906,\\n          \\\"EM\\\": 0.6073295062425498,\\n          \\\"LP\\\": 0.6350108853055589\\n        }\\n      }\\n    },\\n    \\\"conditional\\\": {\\n      \\\"n\\\": 477,\\n      \\\"greedy_f1_mean\\\": 0.709487216719921,\\n      \\\"metrics\\\": {\\n        \\\"SJ\\\": {\\n          \\\"rho\\\": 0.3056,\\n          \\\"tau\\\": 0.2196,\\n          \\\"AUROC\\\": 0.6715,\\n          \\\"delta_vs_r16\\\": -0.0057\\n     
…[truncated 1163 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T12:20:08.985180+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T12:20:08.985416+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"551 /root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2/samples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T12:20:08.985618+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp_023_rank8_inference/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp_023_rank8_inference/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T12:20:08.985823+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"551 /root/autodl-tmp/struct_self_consist_ie/output/exp_023_rank8_inference/samples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T12:20:08.986021+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "python3 -c \"import json; d=json.loads(open('/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2/samples.jsonl').readline()); print('n_samples:', len(d['samples']), 'has_greedy:', 'greedy' in d, 'has_logprobs:', 'logprobs' in d)\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "python3 -c \"import json; d=json.loads(open('/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2/samples.jsonl').readline()); print('n_samples:', len(d['samples']), 'has_greedy:', 'greedy' in d, 'has_logprobs:', 'logprobs' in d)\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T12:20:08.986254+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T12:20:08.986455+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "python3 -c \"import json; d=json.loads(open('/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2/samples.jsonl').readline()); print('n_samples:', len(d['samples']), 'has_greedy:', 'greedy' in d, 'has_logprobs:', 'logprobs' in d)\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "python3 -c \"import json; d=json.loads(open('/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2/samples.jsonl').readline()); print('n_samples:', len(d['samples']), 'has_greedy:', 'greedy' in d, 'has_logprobs:', 'logprobs' in d)\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T12:20:08.986657+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T12:20:08.986855+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "python3 -c \"import json; d=json.loads(open('/root/autodl-tmp/struct_self_consist_ie/output/exp_023_rank8_inference/samples.jsonl').readline()); print('n_samples:', len(d['samples']), 'has_greedy:', 'greedy' in d, 'has_logprobs:', 'logprobs' in d)\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "python3 -c \"import json; d=json.loads(open('/root/autodl-tmp/struct_self_consist_ie/output/exp_023_rank8_inference/samples.jsonl').readline()); print('n_samples:', len(d['samples']), 'has_greedy:', 'greedy' in d, 'has_logprobs:', 'logprobs' in d)\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T12:20:08.987067+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T12:20:08.987339+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/src -name \"*.py\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/src -name \"*.py\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T12:20:08.987549+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"find: '/root/autodl-tmp/struct_self_consist_ie/src': No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T12:20:08.987744+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie -name \"*.py\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie -name \"*.py\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T12:20:08.988082+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/data/wnut17/downsample_train.py\\n/root/autodl-tmp/struct_self_consist_ie/data/retacred_raw/C-GCN/train.py\\n/root/autodl-tmp/struct_self_consist_ie/data/retacred_raw/C-GCN/utils/category_maps.py\\n/root/autodl-tmp/struct_self_consist_ie/data/retacred_raw/C-GCN/utils/constant.py\\n/root/autodl-tmp/struct_self_consist_ie/data/retacred_raw/C-GCN/utils/scorer.py\\n/root/autodl-tmp/struct_self_consist_ie/data/retacred_raw/PALSTM/scorer.py\\n/root/autodl-tmp/struct_self_consist_ie/data/retacred_raw/PALSTM/train.py\\n/root/autodl-tmp/struct_self_consist_ie/data/retacred_raw/PALSTM/utils/category_maps.py\\n/root/autodl-tmp/struct_self_consist_ie/data/retacred_raw/PALSTM/utils/constant.py\\n/root/autodl-tmp/struct_self_consist_ie/data/retacred_raw/Re-TACRED/apply_patch.py\\n/root/autodl-tmp/struct_self_consist_ie/data/retacred_raw/SpanBERT/category_maps.py\\n/root/autodl-tmp/struct_self_consist_ie/data/retacred_raw/SpanBERT/run_tacred.py\\n/root/autodl-tmp/struct_self_consist_ie/data/retacred_raw/SpanBERT/scorer.py\\n/root/autodl-tmp/struct_self_consist_ie/output/exp010_selection_curves/plot_selection_curves.py\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/run_selection_f1.py\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/re_selection_bootstrap.py\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/re_selection_reconcile.py\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/recompute_re_selection.py\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/tost_equivalence.py\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/compute_3seed_summary.py\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/compute_llama_3seed_summary.py\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/compute_n8_seed123_rho.py\\n/root/autodl-tmp/struct_self_consist_ie/output/review_round2/plot_selection_g
…[truncated 6419 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T12:20:08.988409+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -150 /root/autodl-tmp/struct_self_consist_ie/code/consistency.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -150 /root/autodl-tmp/struct_self_consist_ie/code/consistency.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T12:20:08.988755+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Consistency metrics for structured information extraction with self-consistency.\\n\\nImplements three complementary consistency measures over N sampled extractions:\\n1. Fleiss' Kappa (surface matching) — treats N samples as N raters on entity presence\\n2. Structural soft Jaccard — span-level soft overlap with Hungarian matching\\n3. Oracle best-of-N — upper-bound F1 by selecting the best sample per instance\\n\\nKey dependencies: numpy, scipy (linear_sum_assignment).\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nfrom itertools import combinations\\nfrom typing import TYPE_CHECKING\\n\\nimport numpy as np\\nfrom scipy.optimize import linear_sum_assignment\\n\\nif TYPE_CHECKING:\\n    pass\\n\\n# ---------------------------------------------------------------------------\\n# Type aliases (mirrors shared data format)\\n# ---------------------------------------------------------------------------\\nEntity = dict       # {\\\"text\\\", \\\"type\\\", \\\"start\\\", \\\"end\\\"}\\nRelation = dict     # {\\\"head\\\", \\\"tail\\\", \\\"type\\\", ...}\\nEvent = dict        # {\\\"trigger\\\": {...}, \\\"arguments\\\": [...]}\\nExtraction = dict   # {\\\"entities\\\", \\\"relations\\\", \\\"events\\\"}\\n\\n\\n# ===================================================================\\n# 1. Fleiss' Kappa — surface-level entity agreement\\n# ===================================================================\\n\\ndef _extract_surface_keys(sample: Extraction, subtask: str) -> set[tuple]:\\n    \\\"\\\"\\\"Extract surface-level keys from a sample for Fleiss' Kappa computation.\\\"\\\"\\\"\\n    if subtask == \\\"ner\\\":\\n        return {(e[\\\"text\\\"], e[\\\"type\\\"]) for e in sample.get(\\\"entities\\\", [])}\\n    elif subtask == \\\"re\\\":\\n        return {(r[\\\"head\\\"], r[\\\"tail\\\"], r[\\\"type\\\"]) for r in sample.get(\\\"relations\\\", [])}\\n    elif subtask == \\\"eae\\\":\\n   
…[truncated 4043 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T12:20:08.989004+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -200 /root/autodl-tmp/struct_self_consist_ie/code/compute_selection_f1.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -200 /root/autodl-tmp/struct_self_consist_ie/code/compute_selection_f1.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T12:20:08.989417+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Multi-seed Selection F1 for Table 3 (C2 critical).\\n\\nFor each instance's N samples, score with 5 signals (SJ/FK/VC/EM/LP),\\nselect the top-scoring sample, compute its F1 vs gold.\\nReports 3-seed mean±σ, per-seed bootstrap p-value vs greedy, and\\na combined bootstrap p-value across seeds.\\n\\nInput: samples.jsonl files from inference experiments.\\nOutput: JSON results + markdown report.\\nDepends: consistency.py, evaluation.py (same directory).\\n\\\"\\\"\\\"\\n\\nimport json\\nimport os\\nimport sys\\nimport time\\nfrom collections import Counter\\n\\nimport numpy as np\\n\\nsys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')\\nfrom consistency import (\\n    _ner_soft_jaccard_pair,\\n    _re_soft_jaccard_pair,\\n    _extract_surface_keys,\\n)\\nfrom evaluation import per_instance_f1\\n\\nBASE = \\\"/root/autodl-tmp/struct_self_consist_ie\\\"\\n\\nEXPERIMENT_GROUPS = {\\n    # --- Qwen SciERC N=16 (v2 pipeline) ---\\n    \\\"qwen_scierc_ner_n16\\\": {\\n        \\\"subtask\\\": \\\"ner\\\",\\n        \\\"seeds\\\": {\\n            42: f\\\"{BASE}/output/exp_001_seed42_v2/samples.jsonl\\\",\\n            123: f\\\"{BASE}/output/exp_001_seed123_v2/samples.jsonl\\\",\\n            456: f\\\"{BASE}/output/exp_001_seed456_v2/samples.jsonl\\\",\\n        },\\n    },\\n    \\\"qwen_scierc_re_n16\\\": {\\n        \\\"subtask\\\": \\\"re\\\",\\n        \\\"seeds\\\": {\\n            42: f\\\"{BASE}/output/exp_001_seed42_v2/samples.jsonl\\\",\\n            123: f\\\"{BASE}/output/exp_001_seed123_v2/samples.jsonl\\\",\\n            456: f\\\"{BASE}/output/exp_001_seed456_v2/samples.jsonl\\\",\\n        },\\n    },\\n    # --- Qwen SciERC N=8 (r1024 logprobs) ---\\n    \\\"qwen_scierc_ner_n8\\\": {\\n        \\\"subtask\\\": \\\"ner\\\",\\n        \\\"seeds\\\": {\\n            42: f\\\"{BASE}/output/exp_012_rerun_1024/samples.jsonl\\\",\\n            123: f\\\"{B
…[truncated 5768 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T12:20:08.989675+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -100 /root/autodl-tmp/struct_self_consist_ie/code/evaluation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -100 /root/autodl-tmp/struct_self_consist_ie/code/evaluation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T12:20:08.989972+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Evaluation module for structured self-consistency IE experiments.\\n\\nProvides strict-match NER/EAE evaluation, per-instance F1 computation,\\ncorrelation analysis, and summary report generation.\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nimport statistics\\nfrom typing import Any\\n\\nfrom scipy.stats import kendalltau, spearmanr\\n\\n\\n# ---------------------------------------------------------------------------\\n# NER evaluation (strict match)\\n# ---------------------------------------------------------------------------\\n\\ndef entity_strict_match(\\n    pred_entities: list[dict],\\n    gold_entities: list[dict],\\n) -> tuple[int, int, int]:\\n    \\\"\\\"\\\"Compute strict entity match counts.\\n\\n    Strict match requires exact span (start, end) AND exact type.\\n\\n    Args:\\n        pred_entities: Predicted entity dicts with keys text, type, start, end.\\n        gold_entities: Gold entity dicts with the same schema.\\n\\n    Returns:\\n        (tp, fp, fn) counts.\\n    \\\"\\\"\\\"\\n    pred_set = {(e[\\\"start\\\"], e[\\\"end\\\"], e[\\\"type\\\"]) for e in pred_entities}\\n    gold_set = {(e[\\\"start\\\"], e[\\\"end\\\"], e[\\\"type\\\"]) for e in gold_entities}\\n    tp = len(pred_set & gold_set)\\n    fp = len(pred_set - gold_set)\\n    fn = len(gold_set - pred_set)\\n    return tp, fp, fn\\n\\n\\ndef compute_ner_f1(\\n    predictions: list[dict],\\n    golds: list[dict],\\n) -> dict[str, float]:\\n    \\\"\\\"\\\"Compute micro-averaged NER precision, recall, and F1.\\n\\n    Args:\\n        predictions: List of Extraction dicts (one per instance).\\n        golds: List of Extraction dicts (one per instance), aligned with predictions.\\n\\n    Returns:\\n        Dict with keys \\\"precision\\\", \\\"recall\\\", \\\"f1\\\".\\n    \\\"\\\"\\\"\\n    total_tp = total_fp = total_fn = 0\\n    for pred, gold in zip(predictions, golds):\\n        tp, fp, fn = entity_
…[truncated 1950 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T12:20:08.990241+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -n \"per_instance_f1\" /root/autodl-tmp/struct_self_consist_ie/code/evaluation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -n \"per_instance_f1\" /root/autodl-tmp/struct_self_consist_ie/code/evaluation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-16T12:20:08.990464+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"167:def per_instance_f1(\\n234:        f1s = [per_instance_f1(sample, gold, subtask) for sample in samples]\\n380:            instance_greedy_f1s.append(per_instance_f1(greedy, gold, subtask))\\n387:            best_sample = max(samples, key=lambda s: per_instance_f1(s, gold, subtask))\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T12:20:08.990669+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "tail -n +167 /root/autodl-tmp/struct_self_consist_ie/code/evaluation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "tail -n +167 /root/autodl-tmp/struct_self_consist_ie/code/evaluation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-16T12:20:08.991154+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"def per_instance_f1(\\n    pred: dict,\\n    gold: dict,\\n    subtask: str = \\\"ner\\\",\\n) -> float:\\n    \\\"\\\"\\\"Compute F1 for a single instance.\\n\\n    Args:\\n        pred: Predicted Extraction dict.\\n        gold: Gold Extraction dict.\\n        subtask: \\\"ner\\\" for entity matching, \\\"eae\\\" for argument matching.\\n\\n    Returns:\\n        F1 score (float in [0, 1]).\\n    \\\"\\\"\\\"\\n    if subtask == \\\"ner\\\":\\n        tp, fp, fn = entity_strict_match(\\n            pred.get(\\\"entities\\\", []),\\n            gold.get(\\\"entities\\\", []),\\n        )\\n    elif subtask == \\\"re\\\":\\n        tp, fp, fn = relation_strict_match(\\n            pred.get(\\\"relations\\\", []),\\n            gold.get(\\\"relations\\\", []),\\n        )\\n    elif subtask == \\\"eae\\\":\\n        tp, fp, fn = argument_match(\\n            pred.get(\\\"events\\\", []),\\n            gold.get(\\\"events\\\", []),\\n        )\\n    else:\\n        raise ValueError(f\\\"subtask must be 'ner', 're', or 'eae', got '{subtask}'\\\")\\n    return _prf(tp, fp, fn)[\\\"f1\\\"]\\n\\n\\n# ---------------------------------------------------------------------------\\n# Per-sample F1 distribution\\n# ---------------------------------------------------------------------------\\n\\ndef compute_sample_f1_distribution(\\n    sampled_instances: list[dict],\\n    subtask: str = \\\"ner\\\",\\n) -> dict:\\n    \\\"\\\"\\\"Compute per-sample F1 distribution statistics.\\n\\n    For each instance, compute F1 of each of its N samples against gold.\\n    Aggregate into distribution statistics.\\n\\n    Args:\\n        sampled_instances: List of SampledInstance dicts, each containing\\n            \\\"gold\\\" (Extraction) and \\\"samples\\\" (list of Extraction).\\n        subtask: \\\"ner\\\" or \\\"eae\\\".\\n\\n    Returns:\\n        Dict with keys:\\n            - \\\"all_sample_f1s\\\": flat list of all per-sample
…[truncated 7221 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-16T12:20:08.991486+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "mkdir -p /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n_ablation",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "mkdir -p /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n_ablation",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-16T12:20:08.991702+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-16T12:20:08.992008+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat > /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n_ablation/n_ablation.py << 'SCRIPT'\n#!/usr/bin/env python3\n\"\"\"N ablation via random subsampling from existing N=16 / N=8 data.\n\nFor each target N, subsample 10 random seeds, recompute pairwise signals\n(SJ, FK, EM, VC) on subset, select top-1 per signal, compute F1 vs gold.\n\"\"\"\n\nimport json\nimport sys\nimport os\nimport numpy as np\nfrom collections import Counter\n\nsys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')\nfrom consistency import _ner_soft_jaccard_pair, _extract_surface_keys\nfrom evaluation import per_instance_f1\n\nBASE = \"/root/autodl-tmp/struct_self_consist_ie\"\nOUT_DIR = f\"{BASE}/output/exp_025_n_ablation\"\n\nCONFIGS = {\n    \"rank32\": {\n        \"path\": f\"{BASE}/output/exp_001_seed42_v2/samples.jsonl\",\n        \"source_N\": 16,\n        \"target_Ns\": [2, 4, 8, 16],\n    },\n    \"rank8\": {\n        \"path\": f\"{BASE}/output/exp_023_rank8_inference/samples.jsonl\",\n        \"source_N\": 8,\n        \"target_Ns\": [2, 4, 8],\n    },\n}\n\nN_REPEATS = 10\nSUBTASK = \"ner\"\nSIGNALS = [\"LP\", \"SJ\", \"FK\", \"EM\", \"VC\"]\n\n\ndef load_data(path):\n    with open(path) as f:\n        return [json.loads(line) for line in f if line.strip()]\n\n\ndef compute_signals_for_subset(samples):\n    \"\"\"Compute all 5 signal scores for a subset of samples.\"\"\"\n    N = len(samples)\n    \n    # LP: per-sample, no recomputation needed\n    lp_scores = []\n    for s in samples:\n        lp = s.get(\"mean_logprob\")\n        if lp is None:\n            lp = s.get(\"cumulative_logprob\", -999) / max(s.get(\"n_tokens\", 1), 1)\n        lp_scores.append(lp)\n    \n    # Surface key sets (for FK, VC, EM)\n    key_sets = [frozenset(_extract_surface_keys(s, SUBTASK)) for s in samples]\n    \n    # FK: pairwise surface Jaccard\n    fk_matrix = np.zeros((N, N))\n    for i in range(N):\n        for j in range(i + 1, N):\n            union = len(key_sets[i] | key_sets[j])\n            inter = len(key_sets[i] & key_sets[j])\n            s = inter / union if union > 0 else 1.0\n            fk_matrix[i][j] = s\n            fk_matrix[j][i] = s\n    np.fill_diagonal(fk_matrix, 1.0)\n    fk_scores = [float(np.mean([fk_matrix[k][j] for j in range(N) if j != k])) for k in range(N)]\n    \n    # SJ: pairwise structural soft Jaccard\n    sj_matrix = np.zeros((N, N))\n    for i in range(N):\n        for j in range(i + 1, N):\n            s = _ner_soft_jaccard_pair(samples[i].get(\"entities\", []), samples[j].get(\"entities\", []))\n            sj_matrix[i][j] = s\n            sj_matrix[j][i] = s\n    np.fill_diagonal(sj_matrix, 1.0)\n    sj_scores = [float(np.mean([sj_matrix[k][j] for j in range(N) if j != k])) for k in range(N)]\n    \n    # VC: voting confidence\n    all_keys_count = Counter()\n    for ks in key_sets:\n        for key in ks:\n            all_keys_count[key] += 1\n    vc_scores = []\n    for ks in key_sets:\n        if not ks:\n            vc_scores.append(0.0)\n        else:\n            fracs = [all_keys_count[key] / N for key in ks]\n            vc_scores.append(float(np.mean(fracs)))\n    \n    # EM: exact match count\n    em_scores = [float(sum(1 for j in range(N) if j != k and key_sets[k] == key_sets[j])) for k in range(N)]\n    \n    return {\"LP\": lp_scores, \"SJ\": sj_scores, \"FK\": fk_scores, \"EM\": em_scores, \"VC\": vc_scores}\n\n\ndef run_ablation_for_N(instances, target_N, source_N, seed):\n    \"\"\"Run one subsample trial: pick target_N from source_N, compute metrics.\"\"\"\n    rng = np.random.RandomState(seed)\n    \n    greedy_f1s = []\n    oracle_f1s = []\n    signal_selected_f1s = {sig: [] for sig in SIGNALS}\n    sample_f1s_all = []  # all per-sample F1s for degeneracy\n    lp_ranges = []\n    \n    for inst in instances:\n        all_samples = inst[\"samples\"]\n        gold = inst[\"gold\"]\n        greedy = inst.get(\"greedy\", all_samples[0])\n        \n        # Subsample\n        if target_N < source_N:\n            indices = rng.choice(source_N, size=target_N, replace=False)\n            subset = [all_samples[i] for i in indices]\n        else:\n            subset = all_samples[:target_N]\n        \n        # Greedy F1 (fixed, independent of N)\n        g_f1 = per_instance_f1(greedy, gold, subtask=SUBTASK)\n        greedy_f1s.append(g_f1)\n        \n        # Per-sample F1s\n        sample_f1_list = [per_instance_f1(s, gold, subtask=SUBTASK) for s in subset]\n        sample_f1s_all.append(sample_f1_list)\n        \n        # Oracle\n        oracle_f1s.append(max(sample_f1_list))\n        \n        # Compute signals on subset\n        signals = compute_signals_for_subset(subset)\n        \n        # LP range\n        lp_vals = signals[\"LP\"]\n        lp_ranges.append(max(lp_vals) - min(lp_vals))\n        \n        # Selection: pick top-1 by each signal\n        for sig in SIGNALS:\n            best_idx = int(np.argmax(signals[sig]))\n            signal_selected_f1s[sig].append(sample_f1_list[best_idx])\n    \n    # Aggregate metrics\n    n_inst = len(instances)\n    greedy_f1_mean = float(np.mean(greedy_f1s))\n    oracle_f1_mean = float(np.mean(oracle_f1s))\n    \n    # Degeneracy: all N samples have same F1\n    n_degenerate = sum(1 for fs in sample_f1s_all if len(set(round(f, 8) for f in fs)) == 1)\n    degeneracy_rate = n_degenerate / n_inst\n    \n    # LP range median\n    lp_range_median = float(np.median(lp_ranges))\n    \n    # Selection F1s\n    selection_f1_means = {sig: float(np.mean(signal_selected_f1s[sig])) for sig in SIGNALS}\n    \n    # Best signal\n    best_sig = max(SIGNALS, key=lambda s: selection_f1_means[s])\n    \n    return {\n        \"greedy_f1\": greedy_f1_mean,\n        \"oracle_f1\": oracle_f1_mean,\n        \"degeneracy_rate\": degeneracy_rate,\n        \"lp_range_median\": lp_range_median,\n        \"selection_f1\": selection_f1_means,\n        \"best_signal\": best_sig,\n        \"best_signal_f1\": selection_f1_means[best_sig],\n        \"oracle_gap\": oracle_f1_mean - greedy_f1_mean,\n    }\n\n\ndef main():\n    results = {}\n    \n    for regime, cfg in CONFIGS.items():\n        print(f\"\\n=== Regime: {regime} ===\")\n        data = load_data(cfg[\"path\"])\n        \n        # Filter to non-empty gold\n        field = \"entities\"\n        instances = [d for d in data if len(d[\"gold\"].get(field, [])) > 0]\n        source_N = cfg[\"source_N\"]\n        \n        # Verify sample count\n        actual_N = len(instances[0][\"samples\"])\n        print(f\"  Loaded {len(instances)} instances, {actual_N} samples each (expected {source_N})\")\n        assert actual_N >= source_N, f\"Expected >= {source_N} samples, got {actual_N}\"\n        \n        regime_results = {}\n        \n        for target_N in cfg[\"target_Ns\"]:\n            print(f\"  N={target_N}...\", end=\" \", flush=True)\n            \n            if target_N == source_N:\n                # No subsampling, single run\n                trial = run_ablation_for_N(instances, target_N, actual_N, seed=0)\n                regime_results[f\"N={target_N}\"] = {\n                    \"mean\": trial,\n                    \"std\": {k: 0.0 for k in [\"degeneracy_rate\", \"lp_range_median\", \"oracle_f1\", \"best_signal_f1\"]},\n                    \"n_repeats\": 1,\n                }\n                print(f\"oracle={trial['oracle_f1']:.4f}, best_sel={trial['best_signal_f1']:.4f} ({trial['best_signal']}), degen={trial['degeneracy_rate']:.3f}\")\n            else:\n                # 10 random subsampling trials\n                trials = []\n                for seed in range(N_REPEATS):\n                    trial = run_ablation_for_N(instances, target_N, actual_N, seed)\n                    trials.append(trial)\n                \n                # Compute mean and std across trials\n                mean_result = {}\n                std_result = {}\n                for key in [\"greedy_f1\", \"oracle_f1\", \"degeneracy_rate\", \"lp_range_median\", \"oracle_gap\", \"best_signal_f1\"]:\n                    vals = [t[key] for t in trials]\n                    mean_result[key] = float(np.mean(vals))\n                    std_result[key] = float(np.std(vals))\n                \n                # Selection F1 per signal\n                mean_result[\"selection_f1\"] = {}\n                std_result[\"selection_f1\"] = {}\n                for sig in SIGNALS:\n                    vals = [t[\"selection_f1\"][sig] for t in trials]\n                    mean_result[\"selection_f1\"][sig] = float(np.mean(vals))\n                    std_result[\"selection_f1\"][sig] = float(np.std(vals))\n                \n                # Best signal (by mean across trials)\n                best_sig = max(SIGNALS, key=lambda s: mean_result[\"selection_f1\"][s])\n                mean_result[\"best_signal\"] = best_sig\n                mean_result[\"best_signal_f1\"] = mean_result[\"selection_f1\"][best_sig]\n                std_result[\"best_signal_f1\"] = std_result[\"selection_f1\"][best_sig]\n                \n                regime_results[f\"N={target_N}\"] = {\n                    \"mean\": mean_result,\n                    \"std\": std_result,\n                    \"n_repeats\": N_REPEATS,\n                }\n                print(f\"oracle={mean_result['oracle_f1']:.4f}±{std_result['oracle_f1']:.4f}, \"\n                      f\"best_sel={mean_result['best_signal_f1']:.4f}��{std_result['best_signal_f1']:.4f} ({best_sig}), \"\n                      f\"degen={mean_result['degeneracy_rate']:.3f}±{std_result['degeneracy_rate']:.3f}\")\n        \n        results[regime] = regime_results\n    \n    # Save results\n    with open(f\"{OUT_DIR}/results.json\", \"w\") as f:\n        json.dump(results, f, indent=2)\n    print(f\"\\nSaved results to {OUT_DIR}/results.json\")\n    \n    # Generate table\n    generate_table(results)\n\n\ndef generate_table(results):\n    lines = []\n    lines.append(\"| Regime | N | Degeneracy% | LP_range | Oracle_F1 | Greedy_F1 | Oracle_gap | LP_Δ | SJ_Δ | FK_Δ | EM_Δ | VC_Δ | Best_Δ |\")\n    lines.append(\"|--------|---|-------------|----------|-----------|-----------|------------|------|------|------|------|------|--------|\")\n    \n    for regime, regime_data in results.items():\n        for n_key in sorted(regime_data.keys(), key=lambda x: int(x.split(\"=\")[1])):\n            entry = regime_data[n_key]\n            m = entry[\"mean\"]\n            s = entry[\"std\"]\n            \n            greedy_f1 = m[\"greedy_f1\"] if isinstance(m.get(\"greedy_f1\"), (int, float)) else m.get(\"greedy_f1\", 0)\n            oracle_f1 = m[\"oracle_f1\"] if isinstance(m.get(\"oracle_f1\"), (int, float)) else m.get(\"oracle_f1\", 0)\n            degen = m[\"degeneracy_rate\"] if isinstance(m.get(\"degeneracy_rate\"), (int, float)) else m.get(\"degeneracy_rate\", 0)\n            lp_range = m[\"lp_range_median\"] if isinstance(m.get(\"lp_range_median\"), (int, float)) else m.get(\"lp_range_median\", 0)\n            oracle_gap = oracle_f1 - greedy_f1\n            \n            # Selection deltas (selection F1 - greedy F1)\n            sel_f1 = m.get(\"selection_f1\", {})\n            deltas = {}\n            for sig in SIGNALS:\n                if sig in sel_f1:\n                    deltas[sig] = sel_f1[sig] - greedy_f1\n                else:\n                    deltas[sig] = 0.0\n            \n            best_delta = max(deltas.values()) if deltas else 0.0\n            \n            # Format with std if available\n            degen_std = s.get(\"degeneracy_rate\", 0) if isinstance(s, dict) else 0\n            degen_str = f\"{degen*100:.1f}±{degen_std*100:.1f}\" if degen_std > 0 else f\"{degen*100:.1f}\"\n            \n            lines.append(\n                f\"| {regime} | {n_key.split('=')[1]} | {degen_str} | {lp_range:.4f} | \"\n                f\"{oracle_f1:.4f} | {greedy_f1:.4f} | {oracle_gap:.4f} | \"\n                f\"{deltas.get('LP',0)*100:+.2f} | {deltas.get('SJ',0)*100:+.2f} | \"\n                f\"{deltas.get('FK',0)*100:+.2f} | {deltas.get('EM',0)*100:+.2f} | \"\n                f\"{deltas.get('VC',0)*100:+.2f} | {best_delta*100:+.2f} |\"\n            )\n    \n    table = \"\\n\".join(lines)\n    with open(f\"{OUT_DIR}/table.md\", \"w\") as f:\n        f.write(table + \"\\n\")\n    print(f\"\\n{table}\")\n    print(f\"\\nSaved table to {OUT_DIR}/table.md\")\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat > /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n_ablation/n_ablation.py << 'SCRIPT'\n#!/usr/bin/env python3\n\"\"\"N ablation via random subsampling from existing N=16 / N=8 data.\n\nFor each target N, subsample 10 random seeds, recompute pairwise signals\n(SJ, FK, EM, VC) on subset, select top-1 per signal, compute F1 vs gold.\n\"\"\"\n\nimport json\nimport sys\nimport os\nimport numpy as np\nfrom collections import Counter\n\nsys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')\nfrom consistency import _ner_soft_jaccard_pair, _extract_surface_keys\nfrom evaluation import per_instance_f1\n\nBASE = \"/root/autodl-tmp/struct_self_consist_ie\"\nOUT_DIR = f\"{BASE}/output/exp_025_n_ablation\"\n\nCONFIGS = {\n    \"rank32\": {\n        \"path\": f\"{BASE}/output/exp_001_seed42_v2/samples.jsonl\",\n        \"source_N\": 16,\n        \"target_Ns\": [2, 4, 8, 16],\n    },\n    \"rank8\": {\n        \"path\": f\"{BASE}/output/exp_023_rank8_inference/samples.jsonl\",\n        \"source_N\": 8,\n        \"target_Ns\": [2, 4, 8],\n    },\n}\n\nN_REPEATS = 10\nSUBTASK = \"ner\"\nSIGNALS = [\"LP\", \"SJ\", \"FK\", \"EM\", \"VC\"]\n\n\ndef load_data(path):\n    with open(path) as f:\n        return [json.loads(line) for line in f if line.strip()]\n\n\ndef compute_signals_for_subset(samples):\n    \"\"\"Compute all 5 signal scores for a subset of samples.\"\"\"\n    N = len(samples)\n    \n    # LP: per-sample, no recomputation needed\n    lp_scores = []\n    for s in samples:\n        lp = s.get(\"mean_logprob\")\n        if lp is None:\n            lp = s.get(\"cumulative_logprob\", -999) / max(s.get(\"n_tokens\", 1), 1)\n        lp_scores.append(lp)\n    \n    # Surface key sets (for FK, VC, EM)\n    key_sets = [frozenset(_extract_surface_keys(s, SUBTASK)) for s in samples]\n    \n    # FK: pairwise surface Jaccard\n    fk_matrix = np.zeros((N, N))\n    for i in range(N):\n        for j in range(i + 1, N):\n            union = len(key_sets[i] | key_sets[j])\n            inter = len(key_sets[i] & key_sets[j])\n            s = inter / union if union > 0 else 1.0\n            fk_matrix[i][j] = s\n            fk_matrix[j][i] = s\n    np.fill_diagonal(fk_matrix, 1.0)\n    fk_scores = [float(np.mean([fk_matrix[k][j] for j in range(N) if j != k])) for k in range(N)]\n    \n    # SJ: pairwise structural soft Jaccard\n    sj_matrix = np.zeros((N, N))\n    for i in range(N):\n        for j in range(i + 1, N):\n            s = _ner_soft_jaccard_pair(samples[i].get(\"entities\", []), samples[j].get(\"entities\", []))\n            sj_matrix[i][j] = s\n            sj_matrix[j][i] = s\n    np.fill_diagonal(sj_matrix, 1.0)\n    sj_scores = [float(np.mean([sj_matrix[k][j] for j in range(N) if j != k])) for k in range(N)]\n    \n    # VC: voting confidence\n    all_keys_count = Counter()\n    for ks in key_sets:\n        for key in ks:\n            all_keys_count[key] += 1\n    vc_scores = []\n    for ks in key_sets:\n        if not ks:\n            vc_scores.append(0.0)\n        else:\n            fracs = [all_keys_count[key] / N for key in ks]\n            vc_scores.append(float(np.mean(fracs)))\n    \n    # EM: exact match count\n    em_scores = [float(sum(1 for j in range(N) if j != k and key_sets[k] == key_sets[j])) for k in range(N)]\n    \n    return {\"LP\": lp_scores, \"SJ\": sj_scores, \"FK\": fk_scores, \"EM\": em_scores, \"VC\": vc_scores}\n\n\ndef run_ablation_for_N(instances, target_N, source_N, seed):\n    \"\"\"Run one subsample trial: pick target_N from source_N, compute metrics.\"\"\"\n    rng = np.random.RandomState(seed)\n    \n    greedy_f1s = []\n    oracle_f1s = []\n    signal_selected_f1s = {sig: [] for sig in SIGNALS}\n    sample_f1s_all = []  # all per-sample F1s for degeneracy\n    lp_ranges = []\n    \n    for inst in instances:\n        all_samples = inst[\"samples\"]\n        gold = inst[\"gold\"]\n        greedy = inst.get(\"greedy\", all_samples[0])\n        \n        # Subsample\n        if target_N < source_N:\n            indices = rng.choice(source_N, size=target_N, replace=False)\n            subset = [all_samples[i] for i in indices]\n        else:\n            subset = all_samples[:target_N]\n        \n        # Greedy F1 (fixed, independent of N)\n        g_f1 = per_instance_f1(greedy, gold, subtask=SUBTASK)\n        greedy_f1s.append(g_f1)\n        \n        # Per-sample F1s\n        sample_f1_list = [per_instance_f1(s, gold, subtask=SUBTASK) for s in subset]\n        sample_f1s_all.append(sample_f1_list)\n        \n        # Oracle\n        oracle_f1s.append(max(sample_f1_list))\n        \n        # Compute signals on subset\n        signals = compute_signals_for_subset(subset)\n        \n        # LP range\n        lp_vals = signals[\"LP\"]\n        lp_ranges.append(max(lp_vals) - min(lp_vals))\n        \n        # Selection: pick top-1 by each signal\n        for sig in SIGNALS:\n            best_idx = int(np.argmax(signals[sig]))\n            signal_selected_f1s[sig].append(sample_f1_list[best_idx])\n    \n    # Aggregate metrics\n    n_inst = len(instances)\n    greedy_f1_mean = float(np.mean(greedy_f1s))\n    oracle_f1_mean = float(np.mean(oracle_f1s))\n    \n    # Degeneracy: all N samples have same F1\n    n_degenerate = sum(1 for fs in sample_f1s_all if len(set(round(f, 8) for f in fs)) == 1)\n    degeneracy_rate = n_degenerate / n_inst\n    \n    # LP range median\n    lp_range_median = float(np.median(lp_ranges))\n    \n    # Selection F1s\n    selection_f1_means = {sig: float(np.mean(signal_selected_f1s[sig])) for sig in SIGNALS}\n    \n    # Best signal\n    best_sig = max(SIGNALS, key=lambda s: selection_f1_means[s])\n    \n    return {\n        \"greedy_f1\": greedy_f1_mean,\n        \"oracle_f1\": oracle_f1_mean,\n        \"degeneracy_rate\": degeneracy_rate,\n        \"lp_range_median\": lp_range_median,\n        \"selection_f1\": selection_f1_means,\n        \"best_signal\": best_sig,\n        \"best_signal_f1\": selection_f1_means[best_sig],\n        \"oracle_gap\": oracle_f1_mean - greedy_f1_mean,\n    }\n\n\ndef main():\n    results = {}\n    \n    for regime, cfg in CONFIGS.items():\n        print(f\"\\n=== Regime: {regime} ===\")\n        data = load_data(cfg[\"path\"])\n        \n        # Filter to non-empty gold\n        field = \"entities\"\n        instances = [d for d in data if len(d[\"gold\"].get(field, [])) > 0]\n        source_N = cfg[\"source_N\"]\n        \n        # Verify sample count\n        actual_N = len(instances[0][\"samples\"])\n        print(f\"  Loaded {len(instances)} instances, {actual_N} samples each (expected {source_N})\")\n        assert actual_N >= source_N, f\"Expected >= {source_N} samples, got {actual_N}\"\n        \n        regime_results = {}\n        \n        for target_N in cfg[\"target_Ns\"]:\n            print(f\"  N={target_N}...\", end=\" \", flush=True)\n            \n            if target_N == source_N:\n                # No subsampling, single run\n                trial = run_ablation_for_N(instances, target_N, actual_N, seed=0)\n                regime_results[f\"N={target_N}\"] = {\n                    \"mean\": trial,\n                    \"std\": {k: 0.0 for k in [\"degeneracy_rate\", \"lp_range_median\", \"oracle_f1\", \"best_signal_f1\"]},\n                    \"n_repeats\": 1,\n                }\n                print(f\"oracle={trial['oracle_f1']:.4f}, best_sel={trial['best_signal_f1']:.4f} ({trial['best_signal']}), degen={trial['degeneracy_rate']:.3f}\")\n            else:\n                # 10 random subsampling trials\n                trials = []\n                for seed in range(N_REPEATS):\n                    trial = run_ablation_for_N(instances, target_N, actual_N, seed)\n                    trials.append(trial)\n                \n                # Compute mean and std across trials\n                mean_result = {}\n                std_result = {}\n                for key in [\"greedy_f1\", \"oracle_f1\", \"degeneracy_rate\", \"lp_range_median\", \"oracle_gap\", \"best_signal_f1\"]:\n                    vals = [t[key] for t in trials]\n                    mean_result[key] = float(np.mean(vals))\n                    std_result[key] = float(np.std(vals))\n                \n                # Selection F1 per signal\n                mean_result[\"selection_f1\"] = {}\n                std_result[\"selection_f1\"] = {}\n                for sig in SIGNALS:\n                    vals = [t[\"selection_f1\"][sig] for t in trials]\n                    mean_result[\"selection_f1\"][sig] = float(np.mean(vals))\n                    std_result[\"selection_f1\"][sig] = float(np.std(vals))\n                \n                # Best signal (by mean across trials)\n                best_sig = max(SIGNALS, key=lambda s: mean_result[\"selection_f1\"][s])\n                mean_result[\"best_signal\"] = best_sig\n                mean_result[\"best_signal_f1\"] = mean_result[\"selection_f1\"][best_sig]\n                std_result[\"best_signal_f1\"] = std_result[\"selection_f1\"][best_sig]\n                \n                regime_results[f\"N={target_N}\"] = {\n                    \"mean\": mean_result,\n                    \"std\": std_result,\n                    \"n_repeats\": N_REPEATS,\n                }\n                print(f\"oracle={mean_result['oracle_f1']:.4f}±{std_result['oracle_f1']:.4f}, \"\n                      f\"best_sel={mean_result['best_signal_f1']:.4f}��{std_result['best_signal_f1']:.4f} ({best_sig}), \"\n                      f\"degen={mean_result['degeneracy_rate']:.3f}±{std_result['degeneracy_rate']:.3f}\")\n        \n        results[regime] = regime_results\n    \n    # Save results\n    with open(f\"{OUT_DIR}/results.json\", \"w\") as f:\n        json.dump(results, f, indent=2)\n    print(f\"\\nSaved results to {OUT_DIR}/results.json\")\n    \n    # Generate table\n    generate_table(results)\n\n\ndef generate_table(results):\n    lines = []\n    lines.append(\"| Regime | N | Degeneracy% | LP_range | Oracle_F1 | Greedy_F1 | Oracle_gap | LP_Δ | SJ_Δ | FK_Δ | EM_Δ | VC_Δ | Best_Δ |\")\n    lines.append(\"|--------|---|-------------|----------|-----------|-----------|------------|------|------|------|------|------|--------|\")\n    \n    for regime, regime_data in results.items():\n        for n_key in sorted(regime_data.keys(), key=lambda x: int(x.split(\"=\")[1])):\n            entry = regime_data[n_key]\n            m = entry[\"mean\"]\n            s = entry[\"std\"]\n            \n            greedy_f1 = m[\"greedy_f1\"] if isinstance(m.get(\"greedy_f1\"), (int, float)) else m.get(\"greedy_f1\", 0)\n            oracle_f1 = m[\"oracle_f1\"] if isinstance(m.get(\"oracle_f1\"), (int, float)) else m.get(\"oracle_f1\", 0)\n            degen = m[\"degeneracy_rate\"] if isinstance(m.get(\"degeneracy_rate\"), (int, float)) else m.get(\"degeneracy_rate\", 0)\n            lp_range = m[\"lp_range_median\"] if isinstance(m.get(\"lp_range_median\"), (int, float)) else m.get(\"lp_range_median\", 0)\n            oracle_gap = oracle_f1 - greedy_f1\n            \n            # Selection deltas (selection F1 - greedy F1)\n            sel_f1 = m.get(\"selection_f1\", {})\n            deltas = {}\n            for sig in SIGNALS:\n                if sig in sel_f1:\n                    deltas[sig] = sel_f1[sig] - greedy_f1\n                else:\n                    deltas[sig] = 0.0\n            \n            best_delta = max(deltas.values()) if deltas else 0.0\n            \n            # Format with std if available\n            degen_std = s.get(\"degeneracy_rate\", 0) if isinstance(s, dict) else 0\n            degen_str = f\"{degen*100:.1f}±{degen_std*100:.1f}\" if degen_std > 0 else f\"{degen*100:.1f}\"\n            \n            lines.append(\n                f\"| {regime} | {n_key.split('=')[1]} | {degen_str} | {lp_range:.4f} | \"\n                f\"{oracle_f1:.4f} | {greedy_f1:.4f} | {oracle_gap:.4f} | \"\n                f\"{deltas.get('LP',0)*100:+.2f} | {deltas.get('SJ',0)*100:+.2f} | \"\n                f\"{deltas.get('FK',0)*100:+.2f} | {deltas.get('EM',0)*100:+.2f} | \"\n                f\"{deltas.get('VC',0)*100:+.2f} | {best_delta*100:+.2f} |\"\n            )\n    \n    table = \"\\n\".join(lines)\n    with open(f\"{OUT_DIR}/table.md\", \"w\") as f:\n        f.write(table + \"\\n\")\n    print(f\"\\n{table}\")\n    print(f\"\\nSaved table to {OUT_DIR}/table.md\")\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-16T12:20:08.992461+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-16T12:20:08.992672+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n_ablation && python n_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n_ablation && python n_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-16T12:20:08.992921+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n=== Regime: rank32 ===\\n  Loaded 529 instances, 16 samples each (expected 16)\\n  N=2... oracle=0.6846±0.0055, best_sel=0.6275��0.0060 (LP), degen=0.530±0.016\\n  N=4... oracle=0.7412±0.0043, best_sel=0.6412��0.0050 (LP), degen=0.307±0.012\\n  N=8... oracle=0.7836±0.0018, best_sel=0.6456��0.0051 (LP), degen=0.187±0.009\\n  N=16... oracle=0.8194, best_sel=0.6469 (FK), degen=0.115\\n\\n=== Regime: rank8 ===\\n  Loaded 529 instances, 8 samples each (expected 8)\\n  N=2... oracle=0.6617±0.0048, best_sel=0.5949��0.0072 (LP), degen=0.382±0.019\\n  N=4... oracle=0.7431±0.0042, best_sel=0.6176��0.0053 (LP), degen=0.157±0.009\\n  N=8... oracle=0.7998, best_sel=0.6350 (LP), degen=0.072\\n\\nSaved results to /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n_ablation/results.json\\n\\n| Regime | N | Degeneracy% | LP_range | Oracle_F1 | Greedy_F1 | Oracle_gap | LP_Δ | SJ_Δ | FK_Δ | EM_Δ | VC_Δ | Best_Δ |\\n|--------|---|-------------|----------|-----------|-----------|------------|------|------|------|------|------|--------|\\n| rank32 | 2 | 53.0±1.6 | 0.0113 | 0.6846 | 0.6442 | 0.0404 | -1.67 | -3.68 | -3.68 | -3.68 | -3.60 | -1.67 |\\n| rank32 | 4 | 30.7±1.2 | 0.0258 | 0.7412 | 0.6442 | 0.0970 | -0.30 | -1.53 | -1.54 | -2.22 | -2.80 | -0.30 |\\n| rank32 | 8 | 18.7±0.9 | 0.0408 | 0.7836 | 0.6442 | 0.1394 | +0.15 | -0.57 | -0.61 | -1.44 | -3.19 | +0.15 |\\n| rank32 | 16 | 11.5 | 0.0536 | 0.8194 | 0.6442 | 0.1752 | +0.23 | +0.20 | +0.27 | -1.30 | -3.46 | +0.27 |\\n| rank8 | 2 | 38.2±1.9 | 0.0164 | 0.6617 | 0.6397 | 0.0220 | -4.48 | -8.32 | -8.32 | -8.32 | -8.25 | -4.48 |\\n| rank8 | 4 | 15.7±0.9 | 0.0379 | 0.7431 | 0.6397 | 0.1034 | -2.22 | -3.10 | -3.26 | -6.11 | -5.10 | -2.22 |\\n| rank8 | 8 | 7.2 | 0.0564 | 0.7998 | 0.6397 | 0.1601 | -0.47 | -0.91 | -1.33 | -3.24 | -4.79 | -0.47 |\\n\\nSaved table to /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n_ablation/table.md\\n\", \"stderr\": \"\", \"return_code
…[truncated 69 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-16T12:20:08.993243+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n_ablation/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n_ablation/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-16T12:20:08.993469+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 36\\ndrwxr-xr-x   2 root root    79 May 16 20:18 .\\ndrwxr-xr-x 111 root root  8192 May 16 20:18 ..\\n-rw-r--r--   1 root root 11815 May 16 20:18 n_ablation.py\\n-rw-r--r--   1 root root  6912 May 16 20:18 results.json\\n-rw-r--r--   1 root root  1012 May 16 20:18 table.md\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-16T12:20:08.993683+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "exp_025_n_ablation",
  "type": "data",
  "description": "N ablation experiment: subsampling N∈{2,4,8,16} from rank32 (N=16) and rank8 (N=8) data, 10 seeds each. Shows degeneracy, oracle gap, and selection F1 delta vs N. LP dominates at low N; FK/SJ catch up at N≥16.",
  "project": "struct_self_consist_ie",
  "exp_id": "exp_025",
  "source_path": "/root/autodl-tmp/struct_self_consist_ie/output/exp_025_n_ablation/results.json",
  "tags": "['n_ablation', 'subsampling', 'selection_f1', 'degeneracy']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "exp_025_n_ablation",
    "type": "data",
    "description": "N ablation experiment: subsampling N∈{2,4,8,16} from rank32 (N=16) and rank8 (N=8) data, 10 seeds each. Shows degeneracy, oracle gap, and selection F1 delta vs N. LP dominates at low N; FK/SJ catch up at N≥16.",
    "project": "struct_self_consist_ie",
    "exp_id": "exp_025",
    "source_path": "/root/autodl-tmp/struct_self_consist_ie/output/exp_025_n_ablation/results.json",
    "tags": "['n_ablation', 'subsampling', 'selection_f1', 'degeneracy']"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-16T12:20:08.993899+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"source_path not found: /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n_ablation/results.json\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-16T12:20:08.994113+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n_ablation/results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n_ablation/results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-16T12:20:08.994557+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"rank32\\\": {\\n    \\\"N=2\\\": {\\n      \\\"mean\\\": {\\n        \\\"greedy_f1\\\": 0.6441821796820129,\\n        \\\"oracle_f1\\\": 0.6845551755650915,\\n        \\\"degeneracy_rate\\\": 0.5302457466918714,\\n        \\\"lp_range_median\\\": 0.011278706911152854,\\n        \\\"oracle_gap\\\": 0.04037299588307862,\\n        \\\"best_signal_f1\\\": 0.6275034484445567,\\n        \\\"selection_f1\\\": {\\n          \\\"LP\\\": 0.6275034484445567,\\n          \\\"SJ\\\": 0.607403005083387,\\n          \\\"FK\\\": 0.607403005083387,\\n          \\\"EM\\\": 0.607403005083387,\\n          \\\"VC\\\": 0.6081526893879273\\n        },\\n        \\\"best_signal\\\": \\\"LP\\\"\\n      },\\n      \\\"std\\\": {\\n        \\\"greedy_f1\\\": 0.0,\\n        \\\"oracle_f1\\\": 0.005527700692701951,\\n        \\\"degeneracy_rate\\\": 0.016001195276982596,\\n        \\\"lp_range_median\\\": 0.0007464926004543067,\\n        \\\"oracle_gap\\\": 0.005527700692701951,\\n        \\\"best_signal_f1\\\": 0.005999858204705868,\\n        \\\"selection_f1\\\": {\\n          \\\"LP\\\": 0.005999858204705868,\\n          \\\"SJ\\\": 0.005682995405252551,\\n          \\\"FK\\\": 0.005682995405252551,\\n          \\\"EM\\\": 0.005682995405252551,\\n          \\\"VC\\\": 0.005191992480575876\\n        }\\n      },\\n      \\\"n_repeats\\\": 10\\n    },\\n    \\\"N=4\\\": {\\n      \\\"mean\\\": {\\n        \\\"greedy_f1\\\": 0.6441821796820129,\\n        \\\"oracle_f1\\\": 0.7412045358092041,\\n        \\\"degeneracy_rate\\\": 0.3073724007561437,\\n        \\\"lp_range_median\\\": 0.025825508153027577,\\n        \\\"oracle_gap\\\": 0.09702235612719132,\\n        \\\"best_signal_f1\\\": 0.6411523503121113,\\n        \\\"selection_f1\\\": {\\n          \\\"LP\\\": 0.6411523503121113,\\n          \\\"SJ\\\": 0.6288426795309807,\\n          \\\"FK\\\": 0.6287628129577303,\\n          \\\"EM\\\": 0.6220221284387495,\\n          \\\"VC
…[truncated 6698 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-16T12:20:08.994857+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "exp_025_n_ablation_results",
  "type": "data",
  "description": "N ablation: subsampling N∈{2,4,8,16} from rank32 (N=16) and rank8 (N=8), 10 seeds. LP dominates at low N; FK catches up at N=16. Degeneracy: 53%→11.5% (rank32), 38%→7.2% (rank8) as N grows.",
  "project": "struct_self_consist_ie",
  "exp_id": "exp_025",
  "content": "{\"rank32\":{\"N=2\":{\"mean\":{\"greedy_f1\":0.6442,\"oracle_f1\":0.6846,\"degeneracy_rate\":0.530,\"lp_range_median\":0.0113,\"selection_f1\":{\"LP\":0.6275,\"SJ\":0.6074,\"FK\":0.6074,\"EM\":0.6074,\"VC\":0.6082},\"best_signal\":\"LP\"},\"std\":{\"oracle_f1\":0.0055,\"degeneracy_rate\":0.016,\"best_signal_f1\":0.006},\"n_repeats\":10},\"N=4\":{\"mean\":{\"greedy_f1\":0.6442,\"oracle_f1\":0.7412,\"degeneracy_rate\":0.307,\"lp_range_median\":0.0258,\"selection_f1\":{\"LP\":0.6412,\"SJ\":0.6288,\"FK\":0.6288,\"EM\":0.6220,\"VC\":0.6162},\"best_signal\":\"LP\"},\"std\":{\"oracle_f1\":0.0043,\"degeneracy_rate\":0.012,\"best_signal_f1\":0.005},\"n_repeats\":10},\"N=8\":{\"mean\":{\"greedy_f1\":0.6442,\"oracle_f1\":0.7836,\"degeneracy_rate\":0.187,\"lp_range_median\":0.0408,\"selection_f1\":{\"LP\":0.6456,\"SJ\":0.6384,\"FK\":0.6380,\"EM\":0.6297,\"VC\":0.6123},\"best_signal\":\"LP\"},\"std\":{\"oracle_f1\":0.0018,\"degeneracy_rate\":0.009,\"best_signal_f1\":0.005},\"n_repeats\":10},\"N=16\":{\"mean\":{\"greedy_f1\":0.6442,\"oracle_f1\":0.8194,\"degeneracy_rate\":0.115,\"lp_range_median\":0.0536,\"selection_f1\":{\"LP\":0.6465,\"SJ\":0.6462,\"FK\":0.6469,\"EM\":0.6312,\"VC\":0.6096},\"best_signal\":\"FK\",\"best_signal_f1\":0.6469,\"oracle_gap\":0.1752},\"n_repeats\":1}},\"rank8\":{\"N=2\":{\"mean\":{\"greedy_f1\":0.6397,\"oracle_f1\":0.6617,\"degeneracy_rate\":0.382,\"lp_range_median\":0.0164,\"selection_f1\":{\"LP\":0.5949,\"SJ\":0.5566,\"FK\":0.5566,\"EM\":0.5566,\"VC\":0.5573},\"best_signal\":\"LP\"},\"std\":{\"oracle_f1\":0.0048,\"degeneracy_rate\":0.019,\"best_signal_f1\":0.007},\"n_repeats\":10},\"N=4\":{\"mean\":{\"greedy_f1\":0.6397,\"oracle_f1\":0.7431,\"degeneracy_rate\":0.157,\"lp_range_median\":0.0379,\"selection_f1\":{\"LP\":0.6176,\"SJ\":0.6087,\"FK\":0.6072,\"EM\":0.5787,\"VC\":0.5887},\"best_signal\":\"LP\"},\"std\":{\"oracle_f1\":0.0042,\"degeneracy_rate\":0.009,\"best_signal_f1\":0.005},\"n_repeats\":10},\"N=8\":{\"mean\":{\"greedy_f1\":0.6397,\"oracle_f1\":0.7998,\"degeneracy_rate\":0.072,\"lp_range_median\":0.0564,\"selection_f1\":{\"LP\":0.6350,\"SJ\":0.6306,\"FK\":0.6265,\"EM\":0.6073,\"VC\":0.5919},\"best_signal\":\"LP\",\"best_signal_f1\":0.6350,\"oracle_gap\":0.1601},\"n_repeats\":1}}}",
  "content_filename": "results_summary.json",
  "tags": "['n_ablation', 'subsampling', 'selection_f1', 'degeneracy']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "exp_025_n_ablation_results",
    "type": "data",
    "description": "N ablation: subsampling N∈{2,4,8,16} from rank32 (N=16) and rank8 (N=8), 10 seeds. LP dominates at low N; FK catches up at N=16. Degeneracy: 53%→11.5% (rank32), 38%→7.2% (rank8) as N grows.",
    "project": "struct_self_consist_ie",
    "exp_id": "exp_025",
    "content": "{\"rank32\":{\"N=2\":{\"mean\":{\"greedy_f1\":0.6442,\"oracle_f1\":0.6846,\"degeneracy_rate\":0.530,\"lp_range_median\":0.0113,\"selection_f1\":{\"LP\":0.6275,\"SJ\":0.6074,\"FK\":0.6074,\"EM\":0.6074,\"VC\":0.6082},\"best_signal\":\"LP\"},\"std\":{\"oracle_f1\":0.0055,\"degeneracy_rate\":0.016,\"best_signal_f1\":0.006},\"n_repeats\":10},\"N=4\":{\"mean\":{\"greedy_f1\":0.6442,\"oracle_f1\":0.7412,\"degeneracy_rate\":0.307,\"lp_range_median\":0.0258,\"selection_f1\":{\"LP\":0.6412,\"SJ\":0.6288,\"FK\":0.6288,\"EM\":0.6220,\"VC\":0.6162},\"best_signal\":\"LP\"},\"std\":{\"oracle_f1\":0.0043,\"degeneracy_rate\":0.012,\"best_signal_f1\":0.005},\"n_repeats\":10},\"N=8\":{\"mean\":{\"greedy_f1\":0.6442,\"oracle_f1\":0.7836,\"degeneracy_rate\":0.187,\"lp_range_median\":0.0408,\"selection_f1\":{\"LP\":0.6456,\"SJ\":0.6384,\"FK\":0.6380,\"EM\":0.6297,\"VC\":0.6123},\"best_signal\":\"LP\"},\"std\":{\"oracle_f1\":0.0018,\"degeneracy_rate\":0.009,\"best_signal_f1\":0.005},\"n_repeats\":10},\"N=16\":{\"mean\":{\"greedy_f1\":0.6442,\"oracle_f1\":0.8194,\"degeneracy_rate\":0.115,\"lp_range_median\":0.0536,\"selection_f1\":{\"LP\":0.6465,\"SJ\":0.6462,\"FK\":0.6469,\"EM\":0.6312,\"VC\":0.6096},\"best_signal\":\"FK\",\"best_signal_f1\":0.6469,\"oracle_gap\":0.1752},\"n_repeats\":1}},\"rank8\":{\"N=2\":{\"mean\":{\"greedy_f1\":0.6397,\"oracle_f1\":0.6617,\"degeneracy_rate\":0.382,\"lp_range_median\":0.0164,\"selection_f1\":{\"LP\":0.5949,\"SJ\":0.5566,\"FK\":0.5566,\"EM\":0.5566,\"VC\":0.5573},\"best_signal\":\"LP\"},\"std\":{\"oracle_f1\":0.0048,\"degeneracy_rate\":0.019,\"best_signal_f1\":0.007},\"n_repeats\":10},\"N=4\":{\"mean\":{\"greedy_f1\":0.6397,\"oracle_f1\":0.7431,\"degeneracy_rate\":0.157,\"lp_range_median\":0.0379,\"selection_f1\":{\"LP\":0.6176,\"SJ\":0.6087,\"FK\":0.6072,\"EM\":0.5787,\"VC\":0.5887},\"best_signal\":\"LP\"},\"std\":{\"oracle_f1\":0.0042,\"degeneracy_rate\":0.009,\"best_signal_f1\":0.005},\"n_repeats\":10},\"N=8\":{\"mean\":{\"greedy_f1\":0.6397,\"oracle_f1\":0.7998,\"degeneracy_rate\":0.072,\"lp_range_median\":0.0564,\"selection_f1\":{\"LP\":0.6350,\"SJ\":0.6306,\"FK\":0.6265,\"EM\":0.6073,\"VC\":0.5919},\"best_signal\":\"LP\",\"best_signal_f1\":0.6350,\"oracle_gap\":0.1601},\"n_repeats\":1}}}",
    "content_filename": "results_summary.json",
    "tags": "['n_ablation', 'subsampling', 'selection_f1', 'degeneracy']"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-16T12:20:08.995146+00:00_

Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'rank32': {'N=2': {'mean...1601}, 'n_repeats': 1}}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-16T12:20:08.995399+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "exp_025_n_ablation_results",
  "type": "data",
  "description": "N ablation: subsampling N∈{2,4,8,16} from rank32 (N=16) and rank8 (N=8), 10 seeds. LP dominates at low N; FK catches up at N=16. Degeneracy: 53%→11.5% (rank32), 38%→7.2% (rank8) as N grows.",
  "project": "struct_self_consist_ie",
  "exp_id": "exp_025",
  "content": "| Regime | N | Degeneracy% | LP_range | Oracle_F1 | Greedy_F1 | Oracle_gap | LP_Δ | SJ_Δ | FK_Δ | EM_Δ | VC_Δ | Best_Δ |\\n|--------|---|-------------|----------|-----------|-----------|------------|------|------|------|------|------|--------|\\n| rank32 | 2 | 53.0±1.6 | 0.0113 | 0.6846 | 0.6442 | 0.0404 | -1.67 | -3.68 | -3.68 | -3.68 | -3.60 | -1.67 |\\n| rank32 | 4 | 30.7±1.2 | 0.0258 | 0.7412 | 0.6442 | 0.0970 | -0.30 | -1.53 | -1.54 | -2.22 | -2.80 | -0.30 |\\n| rank32 | 8 | 18.7±0.9 | 0.0408 | 0.7836 | 0.6442 | 0.1394 | +0.15 | -0.57 | -0.61 | -1.44 | -3.19 | +0.15 |\\n| rank32 | 16 | 11.5 | 0.0536 | 0.8194 | 0.6442 | 0.1752 | +0.23 | +0.20 | +0.27 | -1.30 | -3.46 | +0.27 |\\n| rank8 | 2 | 38.2±1.9 | 0.0164 | 0.6617 | 0.6397 | 0.0220 | -4.48 | -8.32 | -8.32 | -8.32 | -8.25 | -4.48 |\\n| rank8 | 4 | 15.7±0.9 | 0.0379 | 0.7431 | 0.6397 | 0.1034 | -2.22 | -3.10 | -3.26 | -6.11 | -5.10 | -2.22 |\\n| rank8 | 8 | 7.2 | 0.0564 | 0.7998 | 0.6397 | 0.1601 | -0.47 | -0.91 | -1.33 | -3.24 | -4.79 | -0.47 |\\n\\nKey findings:\\n- LP is the most robust signal across all N (least negative delta, first to go positive)\\n- Pairwise signals (SJ/FK/EM/VC) degrade faster at low N due to noisy pairwise statistics\\n- At N=2, SJ=FK=EM because pairwise comparison with only 1 other sample collapses to binary\\n- Oracle gap grows log-linearly with N: ~4pp@N=2 → ~17.5pp@N=16 (rank32)\\n- Degeneracy halves roughly each time N doubles\\n- rank8 shows ALL signals below greedy even at full N=8 — need N≥16 for positive selection in low-convergence regime\\n\\nScript: /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n_ablation/n_ablation.py\\nFull results: /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n_ablation/results.json",
  "content_filename": "exp_025_summary.md",
  "tags": "['n_ablation', 'subsampling', 'selection_f1', 'degeneracy']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "exp_025_n_ablation_results",
    "type": "data",
    "description": "N ablation: subsampling N∈{2,4,8,16} from rank32 (N=16) and rank8 (N=8), 10 seeds. LP dominates at low N; FK catches up at N=16. Degeneracy: 53%→11.5% (rank32), 38%→7.2% (rank8) as N grows.",
    "project": "struct_self_consist_ie",
    "exp_id": "exp_025",
    "content": "| Regime | N | Degeneracy% | LP_range | Oracle_F1 | Greedy_F1 | Oracle_gap | LP_Δ | SJ_Δ | FK_Δ | EM_Δ | VC_Δ | Best_Δ |\\n|--------|---|-------------|----------|-----------|-----------|------------|------|------|------|------|------|--------|\\n| rank32 | 2 | 53.0±1.6 | 0.0113 | 0.6846 | 0.6442 | 0.0404 | -1.67 | -3.68 | -3.68 | -3.68 | -3.60 | -1.67 |\\n| rank32 | 4 | 30.7±1.2 | 0.0258 | 0.7412 | 0.6442 | 0.0970 | -0.30 | -1.53 | -1.54 | -2.22 | -2.80 | -0.30 |\\n| rank32 | 8 | 18.7±0.9 | 0.0408 | 0.7836 | 0.6442 | 0.1394 | +0.15 | -0.57 | -0.61 | -1.44 | -3.19 | +0.15 |\\n| rank32 | 16 | 11.5 | 0.0536 | 0.8194 | 0.6442 | 0.1752 | +0.23 | +0.20 | +0.27 | -1.30 | -3.46 | +0.27 |\\n| rank8 | 2 | 38.2±1.9 | 0.0164 | 0.6617 | 0.6397 | 0.0220 | -4.48 | -8.32 | -8.32 | -8.32 | -8.25 | -4.48 |\\n| rank8 | 4 | 15.7±0.9 | 0.0379 | 0.7431 | 0.6397 | 0.1034 | -2.22 | -3.10 | -3.26 | -6.11 | -5.10 | -2.22 |\\n| rank8 | 8 | 7.2 | 0.0564 | 0.7998 | 0.6397 | 0.1601 | -0.47 | -0.91 | -1.33 | -3.24 | -4.79 | -0.47 |\\n\\nKey findings:\\n- LP is the most robust signal across all N (least negative delta, first to go positive)\\n- Pairwise signals (SJ/FK/EM/VC) degrade faster at low N due to noisy pairwise statistics\\n- At N=2, SJ=FK=EM because pairwise comparison with only 1 other sample collapses to binary\\n- Oracle gap grows log-linearly with N: ~4pp@N=2 → ~17.5pp@N=16 (rank32)\\n- Degeneracy halves roughly each time N doubles\\n- rank8 shows ALL signals below greedy even at full N=8 — need N≥16 for positive selection in low-convergence regime\\n\\nScript: /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n_ablation/n_ablation.py\\nFull results: /root/autodl-tmp/struct_self_consist_ie/output/exp_025_n_ablation/results.json",
    "content_filename": "exp_025_summary.md",
    "tags": "['n_ablation', 'subsampling', 'selection_f1', 'degeneracy']"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-16T12:20:08.995682+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_cd91c8\", \"name\": \"exp_025_n_ablation_results\", \"type\": \"data\", \"description\": \"N ablation: subsampling N∈{2,4,8,16} from rank32 (N=16) and rank8 (N=8), 10 seeds. LP dominates at low N; FK catches up at N=16. Degeneracy: 53%→11.5% (rank32), 38%→7.2% (rank8) as N grows.\", \"path\": \"projects/struct_self_consist_ie/artifacts/exp_025/data/exp_025_summary.md\", \"url\": null, \"project\": \"struct_self_consist_ie\", \"exp_id\": \"exp_025\", \"skill\": \"\", \"created_at\": \"2026-05-16T12:19:58.489997+00:00\", \"tags\": [\"n_ablation\", \"subsampling\", \"selection_f1\", \"degeneracy\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-16T12:20:08.995968+00:00_

完成。结果汇总：

**Rank32 (ft_002_v2, N=16 source)**:
| N | Degen% | Oracle_gap | Best signal | Best_Δ vs greedy |
|---|--------|------------|-------------|------------------|
| 2 | 53.0 | +4.0pp | LP | -1.67pp |
| 4 | 30.7 | +9.7pp | LP | -0.30pp |
| 8 | 18.7 | +13.9pp | LP | +0.15pp |
| 16 | 11.5 | +17.5pp | FK | +0.27pp |

**Rank8 (exp-023, N=8 source)**:
| N | Degen% | Oracle_gap | Best signal | Best_Δ vs greedy |
|---|--------|------------|-------------|------------------|
| 2 | 38.2 | +2.2pp | LP | -4.48pp |
| 4 | 15.7 | +10.3pp | LP | -2.22pp |
| 8 | 7.2 | +16.0pp | LP | -0.47pp |

关键发现：
- LP 在所有 N 值下最鲁棒，是最先转正的信号
- N=2 时 SJ=FK=EM（仅1对比较，退化为 binary）
- rank32 需要 N≥8 才能 selection > greedy；rank8 在 N=8 时仍为负
- 输出路径：`/root/autodl-tmp/struct_self_consist_ie/output/exp_025_n_ablation/`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_exp_025_n_ablation_20260516T121619"
}
```

</details>

---
