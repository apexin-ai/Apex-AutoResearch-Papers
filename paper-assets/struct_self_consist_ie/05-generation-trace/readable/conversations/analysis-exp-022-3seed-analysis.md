# analysis exp 022 3seed analysis

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 61
- **Recorded user turns:** 0
- **Tool calls:** 30
- **Original source:** `logs/chats/worker_analysis_exp_022_3seed_analysis_20260516T105321.jsonl`
- **Structured JSON:** [`fae0e6a187643505de2f.json`](../../sessions/fa/fae0e6a187643505de2f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

61 recorded events

### Tool call

_source line 1 · 2026-05-16T10:57:47.176267+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__read_project_file",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__read_project_file",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T10:57:47.176619+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T10:57:47.176826+00:00_

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
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
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

### Tool call

_source line 4 · 2026-05-16T10:57:47.177001+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/ -name \"table2_selection_f1.py\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/ -name \"table2_selection_f1.py\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-16T10:57:47.177224+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"analysis_epsilon_sweep\\nanalysis_fk_bootstrap_ci.json\\nanalysis_fk_bootstrap_per_instance.json\\nanalysis_lp_range_cdf.json\\nanalysis_lp_range_cdf_n16_3seed.json\\nanalysis_multiseed_selection_f1.json\\nanalysis_round8\\nanalysis_scierc_n16_3seed_selection_f1.json\\nanalysis_scierc_n16_3seed_selection_f1_merged.json\\nanalysis_scierc_re_n16_3seed_selection_f1.json\\nanalysis_unified_rho_full.json\\nbootstrap_ci_nscaling\\nbootstrap_ci_summary.json\\nbootstrap_ci_tables.tex\\nconditional_filter_diagnosis.json\\nd108_greedy_f1\\nd108_lp_vc_combination\\nd108_mbr_within_rho\\nd108_q4q5\\nd110_4b_degeneracy\\nd112_disk_cleanup\\nd112_hybrid_strategy\\nd112_mf3_random_single\\nd112_table2_fix\\nexp001_n16_seed123\\nexp001_n16_seed123_200only\\nexp001_n16_seed123_200only_backup\\nexp001_n16_seed123_full\\nexp001_n16_seed123_run.log\\nexp001_n16_seed42\\nexp001_n16_seed42_200only_backup\\nexp001_n16_seed42_run.log\\nexp001_n16_seed456\\nexp001_n16_seed456_200only\\nexp001_n16_seed456_run.log\\nexp001_seed123_t10_full\\nexp001_seed123_t10_full.log\\nexp001_seed456_t10_full\\nexp001_seed456_t10_full.log\\nexp002_conll2003\\nexp003_wnut17_dryrun\\nexp003_wnut17_eval\\nexp003_wnut17_eval.log\\nexp003_wnut17_pilot\\nexp003_wnut17_pilot.log\\nexp004_re_diagnostic\\nexp004v2_re_diagnostic\\nexp007_llama_dryrun\\nexp007_llama_inference\\nexp008_re_n16\\nexp008_re_n16_200only\\nexp008_re_n16_t10_full\\nexp008_re_n16_t10_full.log\\nexp009_stratification_results.json\\nexp010_selection_curves\\nexp016_signal_ensemble\\nexp018_3seed_5signal_results.json\\nexp_001_seed123_v2\\nexp_001_seed123_v2_r1024\\nexp_001_seed42_v2\\nexp_001_seed42_v2_r1024\\nexp_001_seed456_v2\\nexp_001_seed456_v2_ner\\nexp_001_seed456_v2_ner.log\\nexp_001_seed456_v2_ner_r1024\\nexp_002_conll_n16\\nexp_002_conll_n16.log\\nexp_002_conll_n16_r1024\\nexp_003_wnut17_v2_infer\\nexp_005_v2_temperature\\nexp_006_v2\\nexp_006_v2_run.log\\nexp_007_llama_n16\\nexp
…[truncated 2333 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T10:57:47.177398+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/code/table2_selection_f1.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T10:57:47.177536+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -d /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/ /root/autodl-tmp/struct_self_consist_ie/output/exp_022_seed789/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -d /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/ /root/autodl-tmp/struct_self_consist_ie/output/exp_022_seed789/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T10:57:47.177669+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_022_seed789/\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T10:57:47.177828+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/ -d /root/autodl-tmp/struct_self_consist_ie/output/exp*seed123* /root/autodl-tmp/struct_self_consist_ie/output/exp*123*",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/ -d /root/autodl-tmp/struct_self_consist_ie/output/exp*seed123* /root/autodl-tmp/struct_self_consist_ie/output/exp*123*",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T10:57:47.177982+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed123\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed123\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed123_200only\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed123_200only\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed123_200only_backup\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed123_200only_backup\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed123_full\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed123_full\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed123_run.log\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_n16_seed123_run.log\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_seed123_t10_full\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_seed123_t10_full\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_seed123_t10_full.log\\n/root/autodl-tmp/struct_self_consist_ie/output/exp001_seed123_t10_full.log\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed123_v2\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed123_v2\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed123_v2_r1024\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed123_v2_r1024\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_seed123\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_seed123\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_008_re_seed123\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_008_re_seed123\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_s123\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_s123.log\\n/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16_s123_r1024\\n/root/autodl-tmp/struct_self_consist
…[truncated 846 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T10:57:47.178140+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/code/table2_selection_f1.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/code/table2_selection_f1.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-16T10:57:47.178283+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/n16_3seed_5signal_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/n16_3seed_5signal_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-16T10:57:47.178561+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Selection F1 for Table 2: Qwen SciERC NER N=8, seed42+seed123.\\\"\\\"\\\"\\n\\nimport json\\nimport os\\nimport sys\\nimport time\\nfrom collections import Counter\\n\\nimport numpy as np\\nfrom scipy.stats import binomtest\\n\\nsys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')\\nfrom consistency import (\\n    _ner_soft_jaccard_pair,\\n    _extract_surface_keys,\\n)\\nfrom evaluation import per_instance_f1\\n\\nBASE = \\\"/root/autodl-tmp/struct_self_consist_ie\\\"\\nSEEDS = {\\n    42: f\\\"{BASE}/output/exp_012_rerun_1024/samples.jsonl\\\",\\n    123: f\\\"{BASE}/output/exp_018_qwen_scierc_seed123/samples.jsonl\\\",\\n}\\nSUBTASK = \\\"ner\\\"\\nSIGNALS = [\\\"LP\\\", \\\"SJ\\\", \\\"EM\\\", \\\"VC\\\", \\\"FK\\\"]\\nN_RANDOM_REPEATS = 50\\n\\n\\ndef load_data(path):\\n    with open(path) as f:\\n        return [json.loads(line) for line in f if line.strip()]\\n\\n\\ndef compute_sample_sj_scores(instance):\\n    samples = instance[\\\"samples\\\"]\\n    N = len(samples)\\n    matrix = np.zeros((N, N))\\n    for i in range(N):\\n        for j in range(i + 1, N):\\n            s = _ner_soft_jaccard_pair(\\n                samples[i].get(\\\"entities\\\", []),\\n                samples[j].get(\\\"entities\\\", []),\\n            )\\n            matrix[i][j] = s\\n            matrix[j][i] = s\\n    np.fill_diagonal(matrix, 1.0)\\n    return [float(np.mean([matrix[k][j] for j in range(N) if j != k])) for k in range(N)]\\n\\n\\ndef compute_sample_surface_scores(instance):\\n    samples = instance[\\\"samples\\\"]\\n    N = len(samples)\\n    key_sets = [frozenset(_extract_surface_keys(s, SUBTASK)) for s in samples]\\n    matrix = np.zeros((N, N))\\n    for i in range(N):\\n        for j in range(i + 1, N):\\n            union = len(key_sets[i] | key_sets[j])\\n            inter = len(key_sets[i] & key_sets[j])\\n            s = inter / union if union > 0 else 
…[truncated 7277 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T10:57:47.178789+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"42\\\": {\\n    \\\"ner\\\": {\\n      \\\"n_valid\\\": 529,\\n      \\\"rho\\\": {\\n        \\\"SJ\\\": 0.3984,\\n        \\\"FK\\\": 0.2876,\\n        \\\"VC\\\": 0.3993,\\n        \\\"EM\\\": 0.3386,\\n        \\\"LP\\\": 0.2373\\n      },\\n      \\\"auroc\\\": {\\n        \\\"SJ\\\": 0.6965,\\n        \\\"FK\\\": 0.6323,\\n        \\\"VC\\\": 0.7039,\\n        \\\"EM\\\": 0.6773,\\n        \\\"LP\\\": 0.6215\\n      }\\n    },\\n    \\\"re\\\": {\\n      \\\"n_valid\\\": 397,\\n      \\\"rho\\\": {\\n        \\\"SJ\\\": 0.2766,\\n        \\\"FK\\\": 0.2808,\\n        \\\"VC\\\": 0.3801,\\n        \\\"EM\\\": 0.1475,\\n        \\\"LP\\\": 0.2931\\n      },\\n      \\\"auroc\\\": {\\n        \\\"SJ\\\": 0.6372,\\n        \\\"FK\\\": 0.6514,\\n        \\\"VC\\\": 0.6989,\\n        \\\"EM\\\": 0.5557,\\n        \\\"LP\\\": 0.6552\\n      }\\n    }\\n  },\\n  \\\"123\\\": {\\n    \\\"ner\\\": {\\n      \\\"n_valid\\\": 529,\\n      \\\"rho\\\": {\\n        \\\"SJ\\\": 0.4234,\\n        \\\"FK\\\": 0.2899,\\n        \\\"VC\\\": 0.3835,\\n        \\\"EM\\\": 0.3437,\\n        \\\"LP\\\": 0.2391\\n      },\\n      \\\"auroc\\\": {\\n        \\\"SJ\\\": 0.7131,\\n        \\\"FK\\\": 0.6393,\\n        \\\"VC\\\": 0.6947,\\n        \\\"EM\\\": 0.6787,\\n        \\\"LP\\\": 0.6261\\n      }\\n    },\\n    \\\"re\\\": {\\n      \\\"n_valid\\\": 397,\\n      \\\"rho\\\": {\\n        \\\"SJ\\\": 0.2672,\\n        \\\"FK\\\": 0.3154,\\n        \\\"VC\\\": 0.3522,\\n        \\\"EM\\\": 0.1575,\\n        \\\"LP\\\": 0.3071\\n      },\\n      \\\"auroc\\\": {\\n        \\\"SJ\\\": 0.6425,\\n        \\\"FK\\\": 0.6579,\\n        \\\"VC\\\": 0.6846,\\n        \\\"EM\\\": 0.5905,\\n        \\\"LP\\\": 0.6466\\n      }\\n    }\\n  },\\n  \\\"456\\\": {\\n    \\\"ner\\\": {\\n      \\\"n_valid\\\": 529,\\n      \\\"rho\\\": {\\n        \\\"SJ\\\": 0.4098,\\n        \\\"FK\\\": 0.2723,\\n        \\\"VC\\\": 0.4449,\\n  
…[truncated 795 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T10:57:47.178987+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_022_seed789/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_022_seed789/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T10:57:47.179164+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"report.json\\nsamples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T10:57:47.179317+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/analysis_scierc_n16_3seed_selection_f1.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/analysis_scierc_n16_3seed_selection_f1.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T10:57:47.179642+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"qwen_scierc_ner_n16\\\": {\\n    \\\"aggregated\\\": {\\n      \\\"seeds\\\": [\\n        42,\\n        123,\\n        456\\n      ],\\n      \\\"n_instances\\\": 551,\\n      \\\"n_samples\\\": 16,\\n      \\\"greedy_f1\\\": {\\n        \\\"mean\\\": 0.61838,\\n        \\\"std\\\": 0.00014,\\n        \\\"per_seed\\\": {\\n          \\\"42\\\": 0.61846,\\n          \\\"123\\\": 0.61846,\\n          \\\"456\\\": 0.61821\\n        }\\n      },\\n      \\\"random_f1\\\": {\\n        \\\"mean\\\": 0.58473,\\n        \\\"std\\\": 0.00137,\\n        \\\"per_seed\\\": {\\n          \\\"42\\\": 0.58532,\\n          \\\"123\\\": 0.58316,\\n          \\\"456\\\": 0.58571\\n        }\\n      },\\n      \\\"oracle_f1\\\": {\\n        \\\"mean\\\": 0.7871,\\n        \\\"std\\\": 0.00276,\\n        \\\"per_seed\\\": {\\n          \\\"42\\\": 0.78666,\\n          \\\"123\\\": 0.78459,\\n          \\\"456\\\": 0.79006\\n        }\\n      },\\n      \\\"signal_selection_f1\\\": {\\n        \\\"VC\\\": {\\n          \\\"mean\\\": 0.58746,\\n          \\\"std\\\": 0.0053,\\n          \\\"per_seed\\\": {\\n            \\\"42\\\": 0.58525,\\n            \\\"123\\\": 0.58363,\\n            \\\"456\\\": 0.5935\\n          },\\n          \\\"delta_vs_greedy_mean\\\": -0.03092,\\n          \\\"delta_vs_greedy_std\\\": 0.00544,\\n          \\\"vs_greedy_p_per_seed\\\": {\\n            \\\"42\\\": 0.9997,\\n            \\\"123\\\": 1.0,\\n            \\\"456\\\": 0.9947\\n          },\\n          \\\"vs_greedy_p_combined_fisher\\\": 1.0,\\n          \\\"vs_greedy_ci95_per_seed\\\": {\\n            \\\"42\\\": [\\n              -0.05178,\\n              -0.01422\\n            ],\\n            \\\"123\\\": [\\n              -0.05277,\\n              -0.0168\\n            ],\\n            \\\"456\\\": [\\n              -0.04292,\\n              -0.00588\\n            ]\\n          }\\n        },\\n        \\\"SJ\\\": {\\n         
…[truncated 8124 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T10:57:47.179811+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/analysis_multiseed_selection_f1.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/analysis_multiseed_selection_f1.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T10:57:47.180120+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"qwen_scierc_ner_n8\\\": {\\n    \\\"seeds\\\": [\\n      42,\\n      123,\\n      456\\n    ],\\n    \\\"n_instances\\\": 529,\\n    \\\"greedy_f1\\\": {\\n      \\\"mean\\\": 0.64583,\\n      \\\"std\\\": 0.00195,\\n      \\\"per_seed\\\": [\\n        0.64392,\\n        0.64575,\\n        0.64783\\n      ]\\n    },\\n    \\\"random_f1\\\": {\\n      \\\"mean\\\": 0.60688,\\n      \\\"std\\\": 0.00597,\\n      \\\"per_seed\\\": [\\n        0.60807,\\n        0.61215,\\n        0.6004\\n      ]\\n    },\\n    \\\"oracle_f1\\\": {\\n      \\\"mean\\\": 0.77637,\\n      \\\"std\\\": 0.00387,\\n      \\\"per_seed\\\": [\\n        0.7758,\\n        0.7805,\\n        0.77282\\n      ]\\n    },\\n    \\\"signal_selection_f1\\\": {\\n      \\\"VC\\\": {\\n        \\\"mean\\\": 0.61937,\\n        \\\"std\\\": 0.00683,\\n        \\\"per_seed\\\": [\\n          0.62561,\\n          0.62044,\\n          0.61208\\n        ],\\n        \\\"delta_vs_greedy_mean\\\": -0.02646,\\n        \\\"delta_vs_greedy_std\\\": 0.00877,\\n        \\\"vs_greedy_p_per_seed\\\": [\\n          0.0278,\\n          0.0039,\\n          0.0002\\n        ],\\n        \\\"vs_greedy_ci95_per_seed\\\": [\\n          [\\n            -0.03673,\\n            0.00049\\n          ],\\n          [\\n            -0.0436,\\n            -0.00646\\n          ],\\n          [\\n            -0.0544,\\n            -0.01695\\n          ]\\n        ]\\n      },\\n      \\\"SJ\\\": {\\n        \\\"mean\\\": 0.64132,\\n        \\\"std\\\": 0.00862,\\n        \\\"per_seed\\\": [\\n          0.64501,\\n          0.64748,\\n          0.63147\\n        ],\\n        \\\"delta_vs_greedy_mean\\\": -0.00451,\\n        \\\"delta_vs_greedy_std\\\": 0.01026,\\n        \\\"vs_greedy_p_per_seed\\\": [\\n          0.4433,\\n          0.4046,\\n          0.0051\\n        ],\\n        \\\"vs_greedy_ci95_per_seed\\\": [\\n          [\\n            -0.01277,\\n            0.0
…[truncated 7849 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T10:57:47.180383+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_022_seed789/report.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_022_seed789/report.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T10:57:47.180626+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"dataset\\\": \\\"scierc\\\",\\n  \\\"subtask\\\": \\\"joint\\\",\\n  \\\"n_samples\\\": 8,\\n  \\\"temperature\\\": 1.0,\\n  \\\"num_instances\\\": 551,\\n  \\\"use_train_format\\\": true,\\n  \\\"ner_greedy_f1\\\": 0.6664684898929845,\\n  \\\"ner_oracle_f1\\\": 0.7856294536817102,\\n  \\\"ner_oracle_headroom\\\": 0.11916096378872576,\\n  \\\"ner_fleiss_kappa_mean\\\": 0.3874439327102626,\\n  \\\"ner_soft_jaccard_mean\\\": 0.6985305838231555,\\n  \\\"ner_correlation_fleiss_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.23423703233847612,\\n    \\\"p_value\\\": 5.016666964952752e-08,\\n    \\\"n\\\": 529\\n  },\\n  \\\"ner_correlation_softjaccard_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.38378196826186733,\\n    \\\"p_value\\\": 5.229492921679125e-20,\\n    \\\"n\\\": 529\\n  },\\n  \\\"ner_correlation_fleiss_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.16398897705272145,\\n    \\\"p_value\\\": 0.00030868000832392134,\\n    \\\"n\\\": 480\\n  },\\n  \\\"ner_correlation_softjaccard_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.33685803679978554,\\n    \\\"p_value\\\": 3.3580697084759704e-14,\\n    \\\"n\\\": 480\\n  },\\n  \\\"ner_n_gold_empty_filtered\\\": 22,\\n  \\\"ner_n_greedy_f1_zero_filtered\\\": 49,\\n  \\\"ner_structural_beats_surface\\\": true,\\n  \\\"ner_rho_advantage\\\": 0.14954493592339121,\\n  \\\"ner_sample_f1_mean\\\": 0.6120457119502796,\\n  \\\"ner_sample_f1_std\\\": 0.31650177703760796,\\n  \\\"ner_sample_f1_pct_zero\\\": 12.216446124763705,\\n  \\\"ner_logprob_baseline\\\": {\\n    \\\"full\\\": {\\n      \\\"rho\\\": 0.2072664891181495,\\n      \\\"p_rho\\\": 1.5232427001431113e-06,\\n      \\\"tau\\\": 0.14857797286448046,\\n      \\\"p_tau\\\": 1.0979139325289003e-06,\\n      \\\"auroc\\\": 0.6123789764868603,\\n      \\\"n\\\": 529\\n    },\\n    \\\"conditional\\\": {\\n      \\\"rho\\\": 0.15047998893218514,\\n      \\\"p_rho\\\": 0.0009426531935129758,\\n      \\\"tau\\\": 0.107528610
…[truncated 2351 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T10:57:47.180787+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -1 /root/autodl-tmp/struct_self_consist_ie/output/exp_022_seed789/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -1 /root/autodl-tmp/struct_self_consist_ie/output/exp_022_seed789/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T10:57:47.181152+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"id\\\": \\\"X96-1059_sent000\\\", \\\"text\\\": \\\"Recognition of proper nouns in Japanese text has been studied as a part of the more general problem of morphological analysis in Japanese text processing -LRB- -LSB- 1 -RSB- -LSB- 2 -RSB- -RRB- .\\\", \\\"gold\\\": {\\\"entities\\\": [{\\\"text\\\": \\\"Recognition of proper nouns\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 0, \\\"end\\\": 27}, {\\\"text\\\": \\\"proper nouns\\\", \\\"type\\\": \\\"OtherScientificTerm\\\", \\\"start\\\": 15, \\\"end\\\": 27}, {\\\"text\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"Material\\\", \\\"start\\\": 31, \\\"end\\\": 44}, {\\\"text\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 103, \\\"end\\\": 125}, {\\\"text\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 129, \\\"end\\\": 153}], \\\"relations\\\": [{\\\"head\\\": \\\"Recognition of proper nouns\\\", \\\"tail\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"PART-OF\\\", \\\"head_start\\\": 0, \\\"head_end\\\": 27, \\\"tail_start\\\": 103, \\\"tail_end\\\": 125}, {\\\"head\\\": \\\"proper nouns\\\", \\\"tail\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"PART-OF\\\", \\\"head_start\\\": 15, \\\"head_end\\\": 27, \\\"tail_start\\\": 31, \\\"tail_end\\\": 44}, {\\\"head\\\": \\\"morphological analysis\\\", \\\"tail\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"USED-FOR\\\", \\\"head_start\\\": 103, \\\"head_end\\\": 125, \\\"tail_start\\\": 129, \\\"tail_end\\\": 153}], \\\"events\\\": []}, \\\"samples\\\": [{\\\"entities\\\": [{\\\"text\\\": \\\"Recognition of proper nouns in Japanese text\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 0, \\\"end\\\": 44}, {\\\"text\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"Material\\\", \\\"start\\\": 31, \\\"end\\\": 44}, {\\\"text\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 103, \\\"end\\\": 125}, {\
…[truncated 8970 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T10:57:47.181334+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp_022_seed789/samples.jsonl /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl /root/autodl-tmp/struct_self_consist_ie/output/exp_018_qwen_scierc_seed123/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp_022_seed789/samples.jsonl /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl /root/autodl-tmp/struct_self_consist_ie/output/exp_018_qwen_scierc_seed123/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T10:57:47.181476+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"     551 /root/autodl-tmp/struct_self_consist_ie/output/exp_022_seed789/samples.jsonl\\n     551 /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl\\n     551 /root/autodl-tmp/struct_self_consist_ie/output/exp_018_qwen_scierc_seed123/samples.jsonl\\n    1653 total\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T10:57:47.181649+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/n16_3seed_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/n16_3seed_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T10:57:47.181845+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"N=16 3-seed SCS analysis: Spearman rho, AUROC, ranking consistency.\\\"\\\"\\\"\\nimport json, sys\\nimport numpy as np\\nfrom collections import Counter\\nfrom scipy.stats import spearmanr\\n\\nsys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')\\nfrom consistency import structural_consistency_soft_jaccard, fleiss_kappa_surface\\nfrom evaluation import per_instance_f1, compute_auroc\\n\\nSEEDS = [42, 123, 456]\\nBASE = \\\"/root/autodl-tmp/struct_self_consist_ie/output\\\"\\nPATHS = {\\n    42: f\\\"{BASE}/exp001_n16_seed42/samples.jsonl\\\",\\n    123: f\\\"{BASE}/exp001_n16_seed123/samples.jsonl\\\",\\n    456: f\\\"{BASE}/exp001_n16_seed456/samples.jsonl\\\",\\n}\\nSIGNAL_NAMES = [\\\"SJ\\\", \\\"FK\\\", \\\"VC\\\", \\\"EM\\\", \\\"LP\\\"]\\n\\ndef load_data(path):\\n    records = []\\n    with open(path) as f:\\n        for line in f:\\n            if line.strip():\\n                records.append(json.loads(line))\\n    return records\\n\\ndef compute_exact_match_rate(samples, subtask):\\n    if subtask == \\\"ner\\\":\\n        keys = [frozenset((e[\\\"text\\\"], e[\\\"type\\\"]) for e in s.get(\\\"entities\\\", [])) for s in samples]\\n    else:\\n        keys = [frozenset((r[\\\"head\\\"], r[\\\"tail\\\"], r[\\\"type\\\"]) for r in s.get(\\\"relations\\\", [])) for s in samples]\\n    if not keys:\\n        return 0.0\\n    counter = Counter(keys)\\n    return counter.most_common(1)[0][1] / len(samples)\\n\\ndef compute_voting_confidence(samples, subtask):\\n    N = len(samples)\\n    if N == 0:\\n        return 0.0\\n    counter = Counter()\\n    if subtask == \\\"ner\\\":\\n        for s in samples:\\n            for e in s.get(\\\"entities\\\", []):\\n                counter[(e[\\\"text\\\"], e[\\\"type\\\"])] += 1\\n    else:\\n        for s in samples:\\n            for r in s.get(\\\"relations\\\", []):\\n                counter[(r[\\\"head\\\"]
…[truncated 2988 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T10:57:47.182003+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/code/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/code/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T10:57:47.182180+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"__pycache__\\n_backup_cond_fix\\nanalysis_multiseed_selection_f1.py\\nanalysis_scierc_n16_selection.py\\nanalysis_scierc_re_n16_selection.py\\nanalyze_3seed_5signal.py\\nanalyze_component_wise_re.py\\nanalyze_entity_voting.py\\nanalyze_exact_match_voting.py\\nanalyze_exp002_conll2003.py\\nanalyze_exp004_re_diagnostic.py\\nanalyze_exp004_v2_re_diagnostic.py\\nanalyze_exp005_v2_temperature.py\\nanalyze_exp012_rerun_5signal.py\\nanalyze_exp015_unified.py\\nanalyze_exp015_v2_metrics.py\\nanalyze_exp016_ensemble.py\\nanalyze_exp017_5signal.py\\nanalyze_exp017_llama_conll_n16.py\\nanalyze_exp017_llama_conll_n16_s123.py\\nanalyze_exp017_t07.py\\nanalyze_exp023_rank8.py\\nanalyze_llama3b_vs_8b.py\\nanalyze_logprob_baseline.py\\nanalyze_lp_range_cdf.py\\nanalyze_ood_signals.py\\nanalyze_scale_ablation_4b.py\\nanalyze_thinking_token_lp_dilution.py\\ncascade_selection_analysis.py\\ncompute_em_selection_f1.py\\ncompute_metrics.py\\ncompute_re_conditional.py\\ncompute_selection_f1.py\\nconsistency.py\\nconvert_conll2003.py\\nconvert_fewnerd.py\\nconvert_to_llamafactory.py\\nconvert_wnut17.py\\ndata_utils.py\\ndiagnose_logprob_rho.py\\ndiversity_analysis.py\\ndiversity_stratified_selection.py\\nem_exact_match_freq.py\\nentity_token_analysis.py\\neval_exp012_rerun_auroc.py\\neval_n16_5signal.py\\neval_n8_5signal.py\\neval_s456_5signal.py\\neval_seed42_r1024_5signal.py\\nevaluation.py\\nexp001_3seed_all_signals.py\\nexp001_postprocess.py\\nexp009_stratification_analysis.py\\nexp010_selection_curves.py\\nexp018_5signal_analysis.py\\nexp_006_v2_selection.py\\nexp_009_v2_re_rerun.py\\nexp_009_v2_stratification.py\\nexp_016_v2_ensemble.py\\nextract_logprobs.py\\nfk_bootstrap_ci.py\\nfk_bootstrap_per_instance.py\\nfk_bootstrap_test.py\\nfk_independence_test.py\\ngate0_diagnose.py\\ngate0_eval.py\\ngate0_realign_eval.py\\ngen_reliability_1024.py\\nmvp_pilot.py\\nn8_bootstrap_ci.py\\noracle_improvable.py\\noracle_improvable_tost.py\\
…[truncated 573 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T10:57:47.182374+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/n8_5signal_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/n8_5signal_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T10:57:47.182580+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"exp_002_conll_n8\\\": {\\n    \\\"n_total\\\": 3453,\\n    \\\"n_valid\\\": 2756,\\n    \\\"n_conditional\\\": 2617,\\n    \\\"full\\\": {\\n      \\\"n\\\": 2756,\\n      \\\"SJ\\\": {\\n        \\\"rho\\\": 0.4357,\\n        \\\"p_rho\\\": 4.712009758299203e-128,\\n        \\\"auroc\\\": 0.8008,\\n        \\\"ece\\\": 0.0871\\n      },\\n      \\\"FK\\\": {\\n        \\\"rho\\\": 0.3998,\\n        \\\"p_rho\\\": 2.6472486805154954e-106,\\n        \\\"auroc\\\": 0.7741,\\n        \\\"ece\\\": 0.1867\\n      },\\n      \\\"logprob\\\": {\\n        \\\"rho\\\": 0.3157,\\n        \\\"p_rho\\\": 8.156803289565863e-65,\\n        \\\"auroc\\\": 0.7532,\\n        \\\"ece\\\": 0.1419\\n      },\\n      \\\"EM\\\": {\\n        \\\"rho\\\": 0.4507,\\n        \\\"p_rho\\\": 5.131271323324008e-138,\\n        \\\"auroc\\\": 0.8156,\\n        \\\"ece\\\": 0.0993\\n      },\\n      \\\"voting_conf\\\": {\\n        \\\"rho\\\": 0.4237,\\n        \\\"p_rho\\\": 1.70625274366621e-120,\\n        \\\"auroc\\\": 0.7889,\\n        \\\"ece\\\": 0.4712\\n      },\\n      \\\"greedy_f1_mean\\\": 0.9079\\n    },\\n    \\\"conditional\\\": {\\n      \\\"n\\\": 2617,\\n      \\\"SJ\\\": {\\n        \\\"rho\\\": 0.3994,\\n        \\\"p_rho\\\": 8.386092104206872e-101,\\n        \\\"auroc\\\": 0.8061,\\n        \\\"ece\\\": 0.1013\\n      },\\n      \\\"FK\\\": {\\n        \\\"rho\\\": 0.3521,\\n        \\\"p_rho\\\": 3.194643880667708e-77,\\n        \\\"auroc\\\": 0.7699,\\n        \\\"ece\\\": 0.1924\\n      },\\n      \\\"logprob\\\": {\\n        \\\"rho\\\": 0.3671,\\n        \\\"p_rho\\\": 2.729796996601389e-84,\\n        \\\"auroc\\\": 0.8185,\\n        \\\"ece\\\": 0.1837\\n      },\\n      \\\"EM\\\": {\\n        \\\"rho\\\": 0.4449,\\n        \\\"p_rho\\\": 1.9991366022672317e-127,\\n        \\\"auroc\\\": 0.842,\\n        \\\"ece\\\": 0.1161\\n      },\\n      \\\"voting_conf\\\": {\\n        \\\"rho\\\": 0.3521,\\n    
…[truncated 2460 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T10:57:47.182736+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/report.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/report.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T10:57:47.182968+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"dataset\\\": \\\"scierc\\\",\\n  \\\"subtask\\\": \\\"joint\\\",\\n  \\\"n_samples\\\": 8,\\n  \\\"temperature\\\": 1.0,\\n  \\\"num_instances\\\": 551,\\n  \\\"use_train_format\\\": true,\\n  \\\"ner_greedy_f1\\\": 0.6632805497460412,\\n  \\\"ner_oracle_f1\\\": 0.7775133848899465,\\n  \\\"ner_oracle_headroom\\\": 0.11423283514390525,\\n  \\\"ner_fleiss_kappa_mean\\\": 0.3932668065534345,\\n  \\\"ner_soft_jaccard_mean\\\": 0.6963097751953397,\\n  \\\"ner_correlation_fleiss_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.2665109373463269,\\n    \\\"p_value\\\": 4.716829112137585e-10,\\n    \\\"n\\\": 529\\n  },\\n  \\\"ner_correlation_softjaccard_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.3598905669976535,\\n    \\\"p_value\\\": 1.2752281196882738e-17,\\n    \\\"n\\\": 529\\n  },\\n  \\\"ner_correlation_fleiss_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.17607370722783125,\\n    \\\"p_value\\\": 0.00011078924939793821,\\n    \\\"n\\\": 477\\n  },\\n  \\\"ner_correlation_softjaccard_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.3113352549686453,\\n    \\\"p_value\\\": 3.5148620246813462e-12,\\n    \\\"n\\\": 477\\n  },\\n  \\\"ner_n_gold_empty_filtered\\\": 22,\\n  \\\"ner_n_greedy_f1_zero_filtered\\\": 52,\\n  \\\"ner_structural_beats_surface\\\": true,\\n  \\\"ner_rho_advantage\\\": 0.09337962965132657,\\n  \\\"ner_sample_f1_mean\\\": 0.6077394535406134,\\n  \\\"ner_sample_f1_std\\\": 0.3177849195309394,\\n  \\\"ner_sample_f1_pct_zero\\\": 12.594517958412098,\\n  \\\"ner_logprob_baseline\\\": {\\n    \\\"full\\\": {\\n      \\\"rho\\\": 0.20517413101613924,\\n      \\\"p_rho\\\": 1.9498006196855416e-06,\\n      \\\"tau\\\": 0.14782758668777154,\\n      \\\"p_tau\\\": 1.2434769103035355e-06,\\n      \\\"auroc\\\": 0.6115722797477874,\\n      \\\"n\\\": 529\\n    },\\n    \\\"conditional\\\": {\\n      \\\"rho\\\": 0.1537825418721844,\\n      \\\"p_rho\\\": 0.0007519115126420073,\\n      \\\"tau\\\": 0.111054535706
…[truncated 2345 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T10:57:47.183223+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "mkdir -p /root/autodl-tmp/struct_self_consist_ie/output/exp_022_3seed_analysis",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "mkdir -p /root/autodl-tmp/struct_self_consist_ie/output/exp_022_3seed_analysis",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T10:57:47.183395+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T10:57:47.183606+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat > /root/autodl-tmp/struct_self_consist_ie/output/exp_022_3seed_analysis/analyze_3seed.py << 'SCRIPT_EOF'\n#!/usr/bin/env python3\n\"\"\"exp-022: 3-seed (42, 123, 789) joint analysis for SciERC NER N=8.\"\"\"\n\nimport json\nimport sys\nimport time\nfrom collections import Counter\nfrom pathlib import Path\n\nimport numpy as np\nfrom scipy.stats import spearmanr, combine_pvalues, binomtest\n\nsys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')\nfrom consistency import (\n    _ner_soft_jaccard_pair,\n    _extract_surface_keys,\n    structural_consistency_soft_jaccard,\n    fleiss_kappa_surface,\n)\nfrom evaluation import per_instance_f1, compute_auroc\n\nBASE = \"/root/autodl-tmp/struct_self_consist_ie\"\nOUT_DIR = Path(f\"{BASE}/output/exp_022_3seed_analysis\")\nSEEDS = [42, 123, 789]\nSEED_PATHS = {\n    42: f\"{BASE}/output/exp_012_rerun_1024/samples.jsonl\",\n    123: f\"{BASE}/output/exp_018_qwen_scierc_seed123/samples.jsonl\",\n    789: f\"{BASE}/output/exp_022_seed789/samples.jsonl\",\n}\nSUBTASK = \"ner\"\nSIGNALS = [\"LP\", \"SJ\", \"FK\", \"EM\", \"VC\"]\nN_RANDOM_REPEATS = 50\nN_BOOTSTRAP = 10000\nRNG = np.random.RandomState(2024)\n\n\ndef load_data(path):\n    with open(path) as f:\n        return [json.loads(line) for line in f if line.strip()]\n\n\n# ── Per-sample signal computations ──\n\ndef compute_sample_sj_scores(instance):\n    samples = instance[\"samples\"]\n    N = len(samples)\n    matrix = np.zeros((N, N))\n    for i in range(N):\n        for j in range(i + 1, N):\n            s = _ner_soft_jaccard_pair(\n                samples[i].get(\"entities\", []),\n                samples[j].get(\"entities\", []),\n            )\n            matrix[i][j] = s\n            matrix[j][i] = s\n    np.fill_diagonal(matrix, 1.0)\n    return [float(np.mean([matrix[k][j] for j in range(N) if j != k])) for k in range(N)]\n\n\ndef compute_sample_surface_scores(instance):\n    samples = instance[\"samples\"]\n    N = len(samples)\n    key_sets = [frozenset(_extract_surface_keys(s, SUBTASK)) for s in samples]\n    matrix = np.zeros((N, N))\n    for i in range(N):\n        for j in range(i + 1, N):\n            union = len(key_sets[i] | key_sets[j])\n            inter = len(key_sets[i] & key_sets[j])\n            s = inter / union if union > 0 else 1.0\n            matrix[i][j] = s\n            matrix[j][i] = s\n    np.fill_diagonal(matrix, 1.0)\n    fk_scores = [float(np.mean([matrix[k][j] for j in range(N) if j != k])) for k in range(N)]\n    return fk_scores, key_sets\n\n\ndef compute_sample_voting_conf(key_sets, N):\n    all_keys = set()\n    for ks in key_sets:\n        all_keys |= ks\n    if not all_keys:\n        return [1.0] * N\n    key_freq = {}\n    for k in all_keys:\n        key_freq[k] = sum(1 for ks in key_sets if k in ks) / N\n    scores = []\n    for ks in key_sets:\n        if not ks:\n            scores.append(0.0)\n        else:\n            scores.append(float(np.mean([key_freq[k] for k in ks])))\n    return scores\n\n\ndef compute_sample_em_scores(key_sets):\n    counter = Counter(key_sets)\n    return [counter[ks] / len(key_sets) for ks in key_sets]\n\n\ndef compute_sample_logprobs(instance):\n    lps = []\n    for s in instance[\"samples\"]:\n        lp = s.get(\"mean_logprob\")\n        if lp is None:\n            lp = s.get(\"cumulative_logprob\", -999) / max(s.get(\"n_tokens\", 1), 1)\n        lps.append(lp)\n    return lps\n\n\n# ── Instance-level signal computations (for rho/AUROC) ──\n\ndef compute_instance_signals(instance):\n    samples = instance[\"samples\"]\n    N = len(samples)\n    sj = structural_consistency_soft_jaccard(samples, subtask=SUBTASK)\n    fk = fleiss_kappa_surface(samples, subtask=SUBTASK)\n\n    # VC\n    counter = Counter()\n    for s in samples:\n        for e in s.get(\"entities\", []):\n            counter[(e[\"text\"], e[\"type\"])] += 1\n    rates = [v / N for v in counter.values()] if counter else [0.0]\n    vc = float(np.mean(rates))\n\n    # EM\n    keys = [frozenset((e[\"text\"], e[\"type\"]) for e in s.get(\"entities\", [])) for s in samples]\n    c = Counter(keys)\n    em = c.most_common(1)[0][1] / N if keys else 0.0\n\n    # LP\n    logprobs = [s.get(\"mean_logprob\") for s in samples if s.get(\"mean_logprob\") is not None]\n    logprobs = [lp for lp in logprobs if np.isfinite(lp)]\n    lp = float(np.mean(logprobs)) if logprobs else float(\"nan\")\n\n    return {\"SJ\": sj, \"FK\": fk, \"VC\": vc, \"EM\": em, \"LP\": lp}\n\n\ndef sign_test_pvalue(sel_f1s, greedy_f1s):\n    wins = sum(1 for s, g in zip(sel_f1s, greedy_f1s) if s > g)\n    losses = sum(1 for s, g in zip(sel_f1s, greedy_f1s) if s < g)\n    ties = sum(1 for s, g in zip(sel_f1s, greedy_f1s) if abs(s - g) < 1e-12)\n    n_nonzero = wins + losses\n    if n_nonzero == 0:\n        return 1.0, wins, losses, ties\n    result = binomtest(wins, n_nonzero, 0.5, alternative='two-sided')\n    return result.pvalue, wins, losses, ties\n\n\n# ── Main per-seed analysis ──\n\ndef analyze_single_seed(seed):\n    path = SEED_PATHS[seed]\n    data = load_data(path)\n    instances = [d for d in data if len(d[\"gold\"].get(\"entities\", [])) > 0]\n    n_inst = len(instances)\n    N_per = len(instances[0][\"samples\"]) if instances else 0\n    print(f\"  seed={seed}: {n_inst} valid instances, N={N_per}\", flush=True)\n\n    greedy_f1s = []\n    oracle_f1s = []\n    random_f1s_all = []\n    signal_f1s = {sig: [] for sig in SIGNALS}\n    signal_instance_vals = {sig: [] for sig in SIGNALS}\n    f1_vals = []\n\n    t0 = time.time()\n    for idx, inst in enumerate(instances):\n        samples = inst[\"samples\"]\n        gold = inst[\"gold\"]\n        greedy = inst.get(\"greedy\", samples[0])\n        N = len(samples)\n\n        g_f1 = per_instance_f1(greedy, gold, subtask=SUBTASK)\n        greedy_f1s.append(g_f1)\n        f1_vals.append(g_f1)\n\n        sample_f1s = [per_instance_f1(s, gold, subtask=SUBTASK) for s in samples]\n        oracle_f1s.append(max(sample_f1s))\n\n        for _ in range(N_RANDOM_REPEATS):\n            random_f1s_all.append(sample_f1s[RNG.randint(N)])\n\n        # Per-sample signal scores\n        sj_scores = compute_sample_sj_scores(inst)\n        fk_scores, key_sets = compute_sample_surface_scores(inst)\n        vc_scores = compute_sample_voting_conf(key_sets, N)\n        em_scores = compute_sample_em_scores(key_sets)\n        lp_scores = compute_sample_logprobs(inst)\n\n        sample_signals = {\n            \"LP\": lp_scores, \"SJ\": sj_scores, \"FK\": fk_scores,\n            \"EM\": em_scores, \"VC\": vc_scores,\n        }\n        for sig in SIGNALS:\n            best_idx = int(np.argmax(sample_signals[sig]))\n            signal_f1s[sig].append(sample_f1s[best_idx])\n\n        # Instance-level signals for rho/AUROC\n        inst_signals = compute_instance_signals(inst)\n        for sig in SIGNALS:\n            signal_instance_vals[sig].append(inst_signals[sig])\n\n        if (idx + 1) % 100 == 0:\n            elapsed = time.time() - t0\n            print(f\"    {idx+1}/{n_inst} ({elapsed:.1f}s)\", flush=True)\n\n    greedy_macro = float(np.mean(greedy_f1s))\n    oracle_macro = float(np.mean(oracle_f1s))\n    random_macro = float(np.mean(random_f1s_all))\n\n    # rho and AUROC\n    rho_results = {}\n    auroc_results = {}\n    for sig in SIGNALS:\n        vals = np.array(signal_instance_vals[sig])\n        f1_arr = np.array(f1_vals)\n        mask = np.isfinite(vals) & np.isfinite(f1_arr)\n        v, f = vals[mask], f1_arr[mask]\n        rho_results[sig] = float(spearmanr(v, f).statistic)\n        auroc_results[sig] = float(compute_auroc(v.tolist(), f.tolist()))\n\n    result = {\n        \"n_instances\": n_inst,\n        \"n_samples\": N_per,\n        \"greedy_f1\": greedy_macro,\n        \"oracle_f1\": oracle_macro,\n        \"random_f1\": random_macro,\n        \"rho\": {sig: round(rho_results[sig], 4) for sig in SIGNALS},\n        \"auroc\": {sig: round(auroc_results[sig], 4) for sig in SIGNALS},\n    }\n\n    for sig in SIGNALS:\n        sel_macro = float(np.mean(signal_f1s[sig]))\n        p, wins, losses, ties = sign_test_pvalue(signal_f1s[sig], greedy_f1s)\n        result[sig] = {\n            \"selection_f1\": sel_macro,\n            \"sign_test_p\": float(p),\n            \"wins\": int(wins),\n            \"losses\": int(losses),\n            \"ties\": int(ties),\n        }\n\n    elapsed = time.time() - t0\n    print(f\"  seed={seed} done ({elapsed:.1f}s)\", flush=True)\n    return result\n\n\n# ── Bootstrap CI for aggregated metrics ──\n\ndef bootstrap_ci(values, n_boot=N_BOOTSTRAP, ci=0.95):\n    values = np.array(values, dtype=float)\n    n = len(values)\n    boot_means = np.array([\n        np.mean(RNG.choice(values, size=n, replace=True))\n        for _ in range(n_boot)\n    ])\n    alpha = (1 - ci) / 2\n    lo = float(np.percentile(boot_means, alpha * 100))\n    hi = float(np.percentile(boot_means, (1 - alpha) * 100))\n    return lo, hi\n\n\ndef bootstrap_diff_pvalue(a_vals, b_vals, n_boot=N_BOOTSTRAP):\n    \"\"\"Bootstrap p-value for H0: mean(a) == mean(b).\"\"\"\n    a = np.array(a_vals, dtype=float)\n    b = np.array(b_vals, dtype=float)\n    obs_diff = np.mean(a) - np.mean(b)\n    n_a, n_b = len(a), len(b)\n    count = 0\n    for _ in range(n_boot):\n        a_boot = RNG.choice(a, size=n_a, replace=True)\n        b_boot = RNG.choice(b, size=n_b, replace=True)\n        boot_diff = np.mean(a_boot) - np.mean(b_boot)\n        if abs(boot_diff) >= abs(obs_diff):\n            count += 1\n    return count / n_boot\n\n\n# ── Main ──\n\ndef main():\n    print(\"=\" * 60)\n    print(\"exp-022: 3-seed analysis (42, 123, 789) — SciERC NER N=8\")\n    print(\"=\" * 60)\n\n    all_seed_results = {}\n    for seed in SEEDS:\n        print(f\"\\n--- Seed {seed} ---\", flush=True)\n        all_seed_results[seed] = analyze_single_seed(seed)\n\n    # ── Aggregate: mean ± std, bootstrap CI ──\n    aggregated = {\"seeds\": SEEDS, \"subtask\": SUBTASK}\n\n    # Greedy\n    greedy_vals = [all_seed_results[s][\"greedy_f1\"] for s in SEEDS]\n    aggregated[\"greedy_f1\"] = {\n        \"per_seed\": {s: all_seed_results[s][\"greedy_f1\"] for s in SEEDS},\n        \"mean\": float(np.mean(greedy_vals)),\n        \"std\": float(np.std(greedy_vals, ddof=1)),\n        \"ci95\": bootstrap_ci(greedy_vals),\n    }\n\n    # Random\n    random_vals = [all_seed_results[s][\"random_f1\"] for s in SEEDS]\n    aggregated[\"random_f1\"] = {\n        \"per_seed\": {s: all_seed_results[s][\"random_f1\"] for s in SEEDS},\n        \"mean\": float(np.mean(random_vals)),\n        \"std\": float(np.std(random_vals, ddof=1)),\n        \"ci95\": bootstrap_ci(random_vals),\n    }\n\n    # Oracle\n    oracle_vals = [all_seed_results[s][\"oracle_f1\"] for s in SEEDS]\n    aggregated[\"oracle_f1\"] = {\n        \"per_seed\": {s: all_seed_results[s][\"oracle_f1\"] for s in SEEDS},\n        \"mean\": float(np.mean(oracle_vals)),\n        \"std\": float(np.std(oracle_vals, ddof=1)),\n        \"ci95\": bootstrap_ci(oracle_vals),\n    }\n\n    # rho and AUROC per signal\n    aggregated[\"rho\"] = {}\n    aggregated[\"auroc\"] = {}\n    for sig in SIGNALS:\n        rho_vals = [all_seed_results[s][\"rho\"][sig] for s in SEEDS]\n        auroc_vals = [all_seed_results[s][\"auroc\"][sig] for s in SEEDS]\n        aggregated[\"rho\"][sig] = {\n            \"per_seed\": {s: all_seed_results[s][\"rho\"][sig] for s in SEEDS},\n            \"mean\": round(float(np.mean(rho_vals)), 4),\n            \"std\": round(float(np.std(rho_vals, ddof=1)), 4),\n            \"ci95\": bootstrap_ci(rho_vals),\n        }\n        aggregated[\"auroc\"][sig] = {\n            \"per_seed\": {s: all_seed_results[s][\"auroc\"][sig] for s in SEEDS},\n            \"mean\": round(float(np.mean(auroc_vals)), 4),\n            \"std\": round(float(np.std(auroc_vals, ddof=1)), 4),\n            \"ci95\": bootstrap_ci(auroc_vals),\n        }\n\n    # Selection F1 per signal\n    greedy_mean = aggregated[\"greedy_f1\"][\"mean\"]\n    aggregated[\"selection_f1\"] = {}\n    for sig in SIGNALS:\n        sel_vals = [all_seed_results[s][sig][\"selection_f1\"] for s in SEEDS]\n        pvals = [all_seed_results[s][sig][\"sign_test_p\"] for s in SEEDS]\n        _, combined_p = combine_pvalues(pvals, method='fisher')\n        aggregated[\"selection_f1\"][sig] = {\n            \"per_seed\": {s: all_seed_results[s][sig][\"selection_f1\"] for s in SEEDS},\n            \"mean\": float(np.mean(sel_vals)),\n            \"std\": float(np.std(sel_vals, ddof=1)),\n            \"ci95\": bootstrap_ci(sel_vals),\n            \"delta_vs_greedy\": float(np.mean(sel_vals) - greedy_mean),\n            \"per_seed_p\": {s: all_seed_results[s][sig][\"sign_test_p\"] for s in SEEDS},\n            \"combined_p_fisher\": float(combined_p),\n            \"per_seed_wins\": {s: all_seed_results[s][sig][\"wins\"] for s in SEEDS},\n            \"per_seed_losses\": {s: all_seed_results[s][sig][\"losses\"] for s in SEEDS},\n            \"per_seed_ties\": {s: all_seed_results[s][sig][\"ties\"] for s in SEEDS},\n        }\n\n    # ── Fisher combined p-values for key claims ──\n    fisher_tests = {}\n\n    # Claim 1: SJ rho > LP rho (structural > surface on NER)\n    sj_rhos = [all_seed_results[s][\"rho\"][\"SJ\"] for s in SEEDS]\n    lp_rhos = [all_seed_results[s][\"rho\"][\"LP\"] for s in SEEDS]\n    diffs_sj_lp = [sj - lp for sj, lp in zip(sj_rhos, lp_rhos)]\n    all_positive_sj_lp = all(d > 0 for d in diffs_sj_lp)\n    fisher_tests[\"SJ_rho_gt_LP_rho\"] = {\n        \"claim\": \"SJ ρ > LP ρ on NER (structural > surface)\",\n        \"per_seed_diff\": {s: round(sj - lp, 4) for s, sj, lp in zip(SEEDS, sj_rhos, lp_rhos)},\n        \"all_seeds_consistent\": all_positive_sj_lp,\n        \"mean_diff\": round(float(np.mean(diffs_sj_lp)), 4),\n        \"bootstrap_p\": bootstrap_diff_pvalue(sj_rhos, lp_rhos),\n    }\n\n    # Claim 2: SJ rho > FK rho\n    fk_rhos = [all_seed_results[s][\"rho\"][\"FK\"] for s in SEEDS]\n    diffs_sj_fk = [sj - fk for sj, fk in zip(sj_rhos, fk_rhos)]\n    all_positive_sj_fk = all(d > 0 for d in diffs_sj_fk)\n    fisher_tests[\"SJ_rho_gt_FK_rho\"] = {\n        \"claim\": \"SJ ρ > FK ρ on NER\",\n        \"per_seed_diff\": {s: round(sj - fk, 4) for s, sj, fk in zip(SEEDS, sj_rhos, fk_rhos)},\n        \"all_seeds_consistent\": all_positive_sj_fk,\n        \"mean_diff\": round(float(np.mean(diffs_sj_fk)), 4),\n        \"bootstrap_p\": bootstrap_diff_pvalue(sj_rhos, fk_rhos),\n    }\n\n    # Claim 3: EM AUROC ranking\n    em_aurocs = [all_seed_results[s][\"auroc\"][\"EM\"] for s in SEEDS]\n    other_aurocs = {sig: [all_seed_results[s][\"auroc\"][sig] for s in SEEDS] for sig in SIGNALS if sig != \"EM\"}\n    em_vs_others = {}\n    for sig, vals in other_aurocs.items():\n        diffs = [em - v for em, v in zip(em_aurocs, vals)]\n        em_vs_others[sig] = {\n            \"per_seed_diff\": {s: round(d, 4) for s, d in zip(SEEDS, diffs)},\n            \"mean_diff\": round(float(np.mean(diffs)), 4),\n            \"all_positive\": all(d > 0 for d in diffs),\n        }\n    fisher_tests[\"EM_AUROC_vs_others\"] = {\n        \"claim\": \"EM AUROC > all other signals\",\n        \"comparisons\": em_vs_others,\n    }\n\n    aggregated[\"fisher_tests\"] = fisher_tests\n\n    # ── Comparison with 2-seed results (42, 123) ──\n    two_seed = {\"seeds\": [42, 123]}\n    for sig in SIGNALS:\n        sel_2 = [all_seed_results[s][sig][\"selection_f1\"] for s in [42, 123]]\n        sel_3 = [all_seed_results[s][sig][\"selection_f1\"] for s in SEEDS]\n        rho_2 = [all_seed_results[s][\"rho\"][sig] for s in [42, 123]]\n        rho_3 = [all_seed_results[s][\"rho\"][sig] for s in SEEDS]\n        two_seed[sig] = {\n            \"selection_f1_2seed\": {\"mean\": float(np.mean(sel_2)), \"std\": float(np.std(sel_2, ddof=1))},\n            \"selection_f1_3seed\": {\"mean\": float(np.mean(sel_3)), \"std\": float(np.std(sel_3, ddof=1))},\n            \"rho_2seed\": {\"mean\": round(float(np.mean(rho_2)), 4), \"std\": round(float(np.std(rho_2, ddof=1)), 4)},\n            \"rho_3seed\": {\"mean\": round(float(np.mean(rho_3)), 4), \"std\": round(float(np.std(rho_3, ddof=1)), 4)},\n            \"ci_narrowed_selection\": float(np.std(sel_3, ddof=1)) < float(np.std(sel_2, ddof=1)),\n            \"ci_narrowed_rho\": float(np.std(rho_3, ddof=1)) < float(np.std(rho_2, ddof=1)),\n        }\n    aggregated[\"two_vs_three_seed\"] = two_seed\n\n    # ── Save results.json ──\n    full_results = {\n        \"per_seed\": {s: all_seed_results[s] for s in SEEDS},\n        \"aggregated\": aggregated,\n    }\n    results_path = OUT_DIR / \"results.json\"\n    with open(results_path, \"w\") as f:\n        json.dump(full_results, f, indent=2, default=str)\n    print(f\"\\nSaved: {results_path}\")\n\n    # ── Generate report.md ──\n    report_lines = []\n    report_lines.append(\"# exp-022: 3-Seed Joint Analysis (SciERC NER, N=8)\")\n    report_lines.append(\"\")\n    report_lines.append(f\"Seeds: {SEEDS}\")\n    report_lines.append(f\"Dataset: SciERC NER, N=8, T=1.0, Qwen2.5-7B-Instruct\")\n    report_lines.append(\"\")\n\n    # Table 1: Per-seed rho\n    report_lines.append(\"## 1. Spearman ρ (signal vs greedy F1)\")\n    report_lines.append(\"\")\n    report_lines.append(\"| Signal | seed42 | seed123 | seed789 | Mean ± σ | 95% CI |\")\n    report_lines.append(\"|--------|--------|---------|---------|----------|--------|\")\n    for sig in SIGNALS:\n        r = aggregated[\"rho\"][sig]\n        ps = r[\"per_seed\"]\n        ci = r[\"ci95\"]\n        report_lines.append(\n            f\"| {sig} | {ps[42]:.4f} | {ps[123]:.4f} | {ps[789]:.4f} \"\n            f\"| {r['mean']:.4f} ± {r['std']:.4f} | [{ci[0]:.4f}, {ci[1]:.4f}] |\"\n        )\n    report_lines.append(\"\")\n\n    # Table 2: Per-seed AUROC\n    report_lines.append(\"## 2. AUROC\")\n    report_lines.append(\"\")\n    report_lines.append(\"| Signal | seed42 | seed123 | seed789 | Mean ± σ | 95% CI |\")\n    report_lines.append(\"|--------|--------|---------|---------|----------|--------|\")\n    for sig in SIGNALS:\n        r = aggregated[\"auroc\"][sig]\n        ps = r[\"per_seed\"]\n        ci = r[\"ci95\"]\n        report_lines.append(\n            f\"| {sig} | {ps[42]:.4f} | {ps[123]:.4f} | {ps[789]:.4f} \"\n            f\"| {r['mean']:.4f} ± {r['std']:.4f} | [{ci[0]:.4f}, {ci[1]:.4f}] |\"\n        )\n    report_lines.append(\"\")\n\n    # Table 3: Selection F1\n    report_lines.append(\"## 3. Selection macro F1\")\n    report_lines.append(\"\")\n    report_lines.append(\"| Method | seed42 | seed123 | seed789 | Mean ± σ | ΔF1 vs Greedy | Fisher p |\")\n    report_lines.append(\"|--------|--------|---------|---------|----------|---------------|----------|\")\n\n    gps = aggregated[\"greedy_f1\"][\"per_seed\"]\n    gm = aggregated[\"greedy_f1\"]\n    report_lines.append(\n        f\"| Greedy | {gps[42]:.4f} | {gps[123]:.4f} | {gps[789]:.4f} \"\n        f\"| {gm['mean']:.4f} ± {gm['std']:.4f} | — | — |\"\n    )\n    rps = aggregated[\"random_f1\"][\"per_seed\"]\n    rm = aggregated[\"random_f1\"]\n    report_lines.append(\n        f\"| Random | {rps[42]:.4f} | {rps[123]:.4f} | {rps[789]:.4f} \"\n        f\"| {rm['mean']:.4f} ± {rm['std']:.4f} | {rm['mean'] - gm['mean']:+.4f} | — |\"\n    )\n    for sig in SIGNALS:\n        r = aggregated[\"selection_f1\"][sig]\n        ps = r[\"per_seed\"]\n        report_lines.append(\n            f\"| {sig} | {ps[42]:.4f} | {ps[123]:.4f} | {ps[789]:.4f} \"\n            f\"| {r['mean']:.4f} ± {r['std']:.4f} | {r['delta_vs_greedy']:+.4f} | {r['combined_p_fisher']:.4f} |\"\n        )\n    ops = aggregated[\"oracle_f1\"][\"per_seed\"]\n    om = aggregated[\"oracle_f1\"]\n    report_lines.append(\n        f\"| Oracle | {ops[42]:.4f} | {ops[123]:.4f} | {ops[789]:.4f} \"\n        f\"| {om['mean']:.4f} ± {om['std']:.4f} | {om['mean'] - gm['mean']:+.4f} | — |\"\n    )\n    report_lines.append(\"\")\n\n    # Fisher tests\n    report_lines.append(\"## 4. Fisher Combined Tests for Key Claims\")\n    report_lines.append(\"\")\n    for test_name, test_data in fisher_tests.items():\n        report_lines.append(f\"### {test_data['claim']}\")\n        if \"per_seed_diff\" in test_data:\n            report_lines.append(f\"- Per-seed diff: {test_data['per_seed_diff']}\")\n            report_lines.append(f\"- All seeds consistent: {test_data['all_seeds_consistent']}\")\n            report_lines.append(f\"- Mean diff: {test_data['mean_diff']}\")\n            report_lines.append(f\"- Bootstrap p: {test_data['bootstrap_p']:.4f}\")\n        elif \"comparisons\" in test_data:\n            for sig, comp in test_data[\"comparisons\"].items():\n                report_lines.append(f\"- EM vs {sig}: mean diff = {comp['mean_diff']}, all positive = {comp['all_positive']}\")\n        report_lines.append(\"\")\n\n    # 2-seed vs 3-seed comparison\n    report_lines.append(\"## 5. 2-Seed vs 3-Seed Comparison\")\n    report_lines.append(\"\")\n    report_lines.append(\"| Signal | 2-seed F1 (mean±σ) | 3-seed F1 (mean±σ) | CI narrowed? | 2-seed ρ | 3-seed ρ |\")\n    report_lines.append(\"|--------|--------------------|--------------------|--------------|----------|----------|\")\n    for sig in SIGNALS:\n        t = two_seed[sig]\n        s2f = t[\"selection_f1_2seed\"]\n        s3f = t[\"selection_f1_3seed\"]\n        s2r = t[\"rho_2seed\"]\n        s3r = t[\"rho_3seed\"]\n        narrowed = \"✓\" if t[\"ci_narrowed_selection\"] else \"✗\"\n        report_lines.append(\n            f\"| {sig} | {s2f['mean']:.4f}±{s2f['std']:.4f} | {s3f['mean']:.4f}±{s3f['std']:.4f} \"\n            f\"| {narrowed} | {s2r['mean']:.4f}±{s2r['std']:.4f} | {s3r['mean']:.4f}±{s3r['std']:.4f} |\"\n        )\n    report_lines.append(\"\")\n\n    report_path = OUT_DIR / \"report.md\"\n    with open(report_path, \"w\") as f:\n        f.write(\"\\n\".join(report_lines))\n    print(f\"Saved: {report_path}\")\n\n    # Print summary\n    print(\"\\n\" + \"=\" * 60)\n    print(\"SUMMARY\")\n    print(\"=\" * 60)\n    print(f\"\\nGreedy macro F1: {gm['mean']:.4f} ± {gm['std']:.4f}\")\n    print(f\"Oracle macro F1: {om['mean']:.4f} ± {om['std']:.4f}\")\n    print(f\"\\nSelection F1 (3-seed mean ± std):\")\n    for sig in SIGNALS:\n        r = aggregated[\"selection_f1\"][sig]\n        print(f\"  {sig}: {r['mean']:.4f} ± {r['std']:.4f}  (Δ={r['delta_vs_greedy']:+.4f}, Fisher p={r['combined_p_fisher']:.4f})\")\n    print(f\"\\nSpearman ρ (3-seed mean ± std):\")\n    for sig in SIGNALS:\n        r = aggregated[\"rho\"][sig]\n        print(f\"  {sig}: {r['mean']:.4f} ± {r['std']:.4f}\")\n    print(f\"\\nAUROC (3-seed mean ± std):\")\n    for sig in SIGNALS:\n        r = aggregated[\"auroc\"][sig]\n        print(f\"  {sig}: {r['mean']:.4f} ± {r['std']:.4f}\")\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat > /root/autodl-tmp/struct_self_consist_ie/output/exp_022_3seed_analysis/analyze_3seed.py << 'SCRIPT_EOF'\n#!/usr/bin/env python3\n\"\"\"exp-022: 3-seed (42, 123, 789) joint analysis for SciERC NER N=8.\"\"\"\n\nimport json\nimport sys\nimport time\nfrom collections import Counter\nfrom pathlib import Path\n\nimport numpy as np\nfrom scipy.stats import spearmanr, combine_pvalues, binomtest\n\nsys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')\nfrom consistency import (\n    _ner_soft_jaccard_pair,\n    _extract_surface_keys,\n    structural_consistency_soft_jaccard,\n    fleiss_kappa_surface,\n)\nfrom evaluation import per_instance_f1, compute_auroc\n\nBASE = \"/root/autodl-tmp/struct_self_consist_ie\"\nOUT_DIR = Path(f\"{BASE}/output/exp_022_3seed_analysis\")\nSEEDS = [42, 123, 789]\nSEED_PATHS = {\n    42: f\"{BASE}/output/exp_012_rerun_1024/samples.jsonl\",\n    123: f\"{BASE}/output/exp_018_qwen_scierc_seed123/samples.jsonl\",\n    789: f\"{BASE}/output/exp_022_seed789/samples.jsonl\",\n}\nSUBTASK = \"ner\"\nSIGNALS = [\"LP\", \"SJ\", \"FK\", \"EM\", \"VC\"]\nN_RANDOM_REPEATS = 50\nN_BOOTSTRAP = 10000\nRNG = np.random.RandomState(2024)\n\n\ndef load_data(path):\n    with open(path) as f:\n        return [json.loads(line) for line in f if line.strip()]\n\n\n# ── Per-sample signal computations ──\n\ndef compute_sample_sj_scores(instance):\n    samples = instance[\"samples\"]\n    N = len(samples)\n    matrix = np.zeros((N, N))\n    for i in range(N):\n        for j in range(i + 1, N):\n            s = _ner_soft_jaccard_pair(\n                samples[i].get(\"entities\", []),\n                samples[j].get(\"entities\", []),\n            )\n            matrix[i][j] = s\n            matrix[j][i] = s\n    np.fill_diagonal(matrix, 1.0)\n    return [float(np.mean([matrix[k][j] for j in range(N) if j != k])) for k in range(N)]\n\n\ndef compute_sample_surface_scores(instance):\n    samples = instance[\"samples\"]\n    N = len(samples)\n    key_sets = [frozenset(_extract_surface_keys(s, SUBTASK)) for s in samples]\n    matrix = np.zeros((N, N))\n    for i in range(N):\n        for j in range(i + 1, N):\n            union = len(key_sets[i] | key_sets[j])\n            inter = len(key_sets[i] & key_sets[j])\n            s = inter / union if union > 0 else 1.0\n            matrix[i][j] = s\n            matrix[j][i] = s\n    np.fill_diagonal(matrix, 1.0)\n    fk_scores = [float(np.mean([matrix[k][j] for j in range(N) if j != k])) for k in range(N)]\n    return fk_scores, key_sets\n\n\ndef compute_sample_voting_conf(key_sets, N):\n    all_keys = set()\n    for ks in key_sets:\n        all_keys |= ks\n    if not all_keys:\n        return [1.0] * N\n    key_freq = {}\n    for k in all_keys:\n        key_freq[k] = sum(1 for ks in key_sets if k in ks) / N\n    scores = []\n    for ks in key_sets:\n        if not ks:\n            scores.append(0.0)\n        else:\n            scores.append(float(np.mean([key_freq[k] for k in ks])))\n    return scores\n\n\ndef compute_sample_em_scores(key_sets):\n    counter = Counter(key_sets)\n    return [counter[ks] / len(key_sets) for ks in key_sets]\n\n\ndef compute_sample_logprobs(instance):\n    lps = []\n    for s in instance[\"samples\"]:\n        lp = s.get(\"mean_logprob\")\n        if lp is None:\n            lp = s.get(\"cumulative_logprob\", -999) / max(s.get(\"n_tokens\", 1), 1)\n        lps.append(lp)\n    return lps\n\n\n# ── Instance-level signal computations (for rho/AUROC) ──\n\ndef compute_instance_signals(instance):\n    samples = instance[\"samples\"]\n    N = len(samples)\n    sj = structural_consistency_soft_jaccard(samples, subtask=SUBTASK)\n    fk = fleiss_kappa_surface(samples, subtask=SUBTASK)\n\n    # VC\n    counter = Counter()\n    for s in samples:\n        for e in s.get(\"entities\", []):\n            counter[(e[\"text\"], e[\"type\"])] += 1\n    rates = [v / N for v in counter.values()] if counter else [0.0]\n    vc = float(np.mean(rates))\n\n    # EM\n    keys = [frozenset((e[\"text\"], e[\"type\"]) for e in s.get(\"entities\", [])) for s in samples]\n    c = Counter(keys)\n    em = c.most_common(1)[0][1] / N if keys else 0.0\n\n    # LP\n    logprobs = [s.get(\"mean_logprob\") for s in samples if s.get(\"mean_logprob\") is not None]\n    logprobs = [lp for lp in logprobs if np.isfinite(lp)]\n    lp = float(np.mean(logprobs)) if logprobs else float(\"nan\")\n\n    return {\"SJ\": sj, \"FK\": fk, \"VC\": vc, \"EM\": em, \"LP\": lp}\n\n\ndef sign_test_pvalue(sel_f1s, greedy_f1s):\n    wins = sum(1 for s, g in zip(sel_f1s, greedy_f1s) if s > g)\n    losses = sum(1 for s, g in zip(sel_f1s, greedy_f1s) if s < g)\n    ties = sum(1 for s, g in zip(sel_f1s, greedy_f1s) if abs(s - g) < 1e-12)\n    n_nonzero = wins + losses\n    if n_nonzero == 0:\n        return 1.0, wins, losses, ties\n    result = binomtest(wins, n_nonzero, 0.5, alternative='two-sided')\n    return result.pvalue, wins, losses, ties\n\n\n# ── Main per-seed analysis ──\n\ndef analyze_single_seed(seed):\n    path = SEED_PATHS[seed]\n    data = load_data(path)\n    instances = [d for d in data if len(d[\"gold\"].get(\"entities\", [])) > 0]\n    n_inst = len(instances)\n    N_per = len(instances[0][\"samples\"]) if instances else 0\n    print(f\"  seed={seed}: {n_inst} valid instances, N={N_per}\", flush=True)\n\n    greedy_f1s = []\n    oracle_f1s = []\n    random_f1s_all = []\n    signal_f1s = {sig: [] for sig in SIGNALS}\n    signal_instance_vals = {sig: [] for sig in SIGNALS}\n    f1_vals = []\n\n    t0 = time.time()\n    for idx, inst in enumerate(instances):\n        samples = inst[\"samples\"]\n        gold = inst[\"gold\"]\n        greedy = inst.get(\"greedy\", samples[0])\n        N = len(samples)\n\n        g_f1 = per_instance_f1(greedy, gold, subtask=SUBTASK)\n        greedy_f1s.append(g_f1)\n        f1_vals.append(g_f1)\n\n        sample_f1s = [per_instance_f1(s, gold, subtask=SUBTASK) for s in samples]\n        oracle_f1s.append(max(sample_f1s))\n\n        for _ in range(N_RANDOM_REPEATS):\n            random_f1s_all.append(sample_f1s[RNG.randint(N)])\n\n        # Per-sample signal scores\n        sj_scores = compute_sample_sj_scores(inst)\n        fk_scores, key_sets = compute_sample_surface_scores(inst)\n        vc_scores = compute_sample_voting_conf(key_sets, N)\n        em_scores = compute_sample_em_scores(key_sets)\n        lp_scores = compute_sample_logprobs(inst)\n\n        sample_signals = {\n            \"LP\": lp_scores, \"SJ\": sj_scores, \"FK\": fk_scores,\n            \"EM\": em_scores, \"VC\": vc_scores,\n        }\n        for sig in SIGNALS:\n            best_idx = int(np.argmax(sample_signals[sig]))\n            signal_f1s[sig].append(sample_f1s[best_idx])\n\n        # Instance-level signals for rho/AUROC\n        inst_signals = compute_instance_signals(inst)\n        for sig in SIGNALS:\n            signal_instance_vals[sig].append(inst_signals[sig])\n\n        if (idx + 1) % 100 == 0:\n            elapsed = time.time() - t0\n            print(f\"    {idx+1}/{n_inst} ({elapsed:.1f}s)\", flush=True)\n\n    greedy_macro = float(np.mean(greedy_f1s))\n    oracle_macro = float(np.mean(oracle_f1s))\n    random_macro = float(np.mean(random_f1s_all))\n\n    # rho and AUROC\n    rho_results = {}\n    auroc_results = {}\n    for sig in SIGNALS:\n        vals = np.array(signal_instance_vals[sig])\n        f1_arr = np.array(f1_vals)\n        mask = np.isfinite(vals) & np.isfinite(f1_arr)\n        v, f = vals[mask], f1_arr[mask]\n        rho_results[sig] = float(spearmanr(v, f).statistic)\n        auroc_results[sig] = float(compute_auroc(v.tolist(), f.tolist()))\n\n    result = {\n        \"n_instances\": n_inst,\n        \"n_samples\": N_per,\n        \"greedy_f1\": greedy_macro,\n        \"oracle_f1\": oracle_macro,\n        \"random_f1\": random_macro,\n        \"rho\": {sig: round(rho_results[sig], 4) for sig in SIGNALS},\n        \"auroc\": {sig: round(auroc_results[sig], 4) for sig in SIGNALS},\n    }\n\n    for sig in SIGNALS:\n        sel_macro = float(np.mean(signal_f1s[sig]))\n        p, wins, losses, ties = sign_test_pvalue(signal_f1s[sig], greedy_f1s)\n        result[sig] = {\n            \"selection_f1\": sel_macro,\n            \"sign_test_p\": float(p),\n            \"wins\": int(wins),\n            \"losses\": int(losses),\n            \"ties\": int(ties),\n        }\n\n    elapsed = time.time() - t0\n    print(f\"  seed={seed} done ({elapsed:.1f}s)\", flush=True)\n    return result\n\n\n# ── Bootstrap CI for aggregated metrics ──\n\ndef bootstrap_ci(values, n_boot=N_BOOTSTRAP, ci=0.95):\n    values = np.array(values, dtype=float)\n    n = len(values)\n    boot_means = np.array([\n        np.mean(RNG.choice(values, size=n, replace=True))\n        for _ in range(n_boot)\n    ])\n    alpha = (1 - ci) / 2\n    lo = float(np.percentile(boot_means, alpha * 100))\n    hi = float(np.percentile(boot_means, (1 - alpha) * 100))\n    return lo, hi\n\n\ndef bootstrap_diff_pvalue(a_vals, b_vals, n_boot=N_BOOTSTRAP):\n    \"\"\"Bootstrap p-value for H0: mean(a) == mean(b).\"\"\"\n    a = np.array(a_vals, dtype=float)\n    b = np.array(b_vals, dtype=float)\n    obs_diff = np.mean(a) - np.mean(b)\n    n_a, n_b = len(a), len(b)\n    count = 0\n    for _ in range(n_boot):\n        a_boot = RNG.choice(a, size=n_a, replace=True)\n        b_boot = RNG.choice(b, size=n_b, replace=True)\n        boot_diff = np.mean(a_boot) - np.mean(b_boot)\n        if abs(boot_diff) >= abs(obs_diff):\n            count += 1\n    return count / n_boot\n\n\n# ── Main ──\n\ndef main():\n    print(\"=\" * 60)\n    print(\"exp-022: 3-seed analysis (42, 123, 789) — SciERC NER N=8\")\n    print(\"=\" * 60)\n\n    all_seed_results = {}\n    for seed in SEEDS:\n        print(f\"\\n--- Seed {seed} ---\", flush=True)\n        all_seed_results[seed] = analyze_single_seed(seed)\n\n    # ── Aggregate: mean ± std, bootstrap CI ──\n    aggregated = {\"seeds\": SEEDS, \"subtask\": SUBTASK}\n\n    # Greedy\n    greedy_vals = [all_seed_results[s][\"greedy_f1\"] for s in SEEDS]\n    aggregated[\"greedy_f1\"] = {\n        \"per_seed\": {s: all_seed_results[s][\"greedy_f1\"] for s in SEEDS},\n        \"mean\": float(np.mean(greedy_vals)),\n        \"std\": float(np.std(greedy_vals, ddof=1)),\n        \"ci95\": bootstrap_ci(greedy_vals),\n    }\n\n    # Random\n    random_vals = [all_seed_results[s][\"random_f1\"] for s in SEEDS]\n    aggregated[\"random_f1\"] = {\n        \"per_seed\": {s: all_seed_results[s][\"random_f1\"] for s in SEEDS},\n        \"mean\": float(np.mean(random_vals)),\n        \"std\": float(np.std(random_vals, ddof=1)),\n        \"ci95\": bootstrap_ci(random_vals),\n    }\n\n    # Oracle\n    oracle_vals = [all_seed_results[s][\"oracle_f1\"] for s in SEEDS]\n    aggregated[\"oracle_f1\"] = {\n        \"per_seed\": {s: all_seed_results[s][\"oracle_f1\"] for s in SEEDS},\n        \"mean\": float(np.mean(oracle_vals)),\n        \"std\": float(np.std(oracle_vals, ddof=1)),\n        \"ci95\": bootstrap_ci(oracle_vals),\n    }\n\n    # rho and AUROC per signal\n    aggregated[\"rho\"] = {}\n    aggregated[\"auroc\"] = {}\n    for sig in SIGNALS:\n        rho_vals = [all_seed_results[s][\"rho\"][sig] for s in SEEDS]\n        auroc_vals = [all_seed_results[s][\"auroc\"][sig] for s in SEEDS]\n        aggregated[\"rho\"][sig] = {\n            \"per_seed\": {s: all_seed_results[s][\"rho\"][sig] for s in SEEDS},\n            \"mean\": round(float(np.mean(rho_vals)), 4),\n            \"std\": round(float(np.std(rho_vals, ddof=1)), 4),\n            \"ci95\": bootstrap_ci(rho_vals),\n        }\n        aggregated[\"auroc\"][sig] = {\n            \"per_seed\": {s: all_seed_results[s][\"auroc\"][sig] for s in SEEDS},\n            \"mean\": round(float(np.mean(auroc_vals)), 4),\n            \"std\": round(float(np.std(auroc_vals, ddof=1)), 4),\n            \"ci95\": bootstrap_ci(auroc_vals),\n        }\n\n    # Selection F1 per signal\n    greedy_mean = aggregated[\"greedy_f1\"][\"mean\"]\n    aggregated[\"selection_f1\"] = {}\n    for sig in SIGNALS:\n        sel_vals = [all_seed_results[s][sig][\"selection_f1\"] for s in SEEDS]\n        pvals = [all_seed_results[s][sig][\"sign_test_p\"] for s in SEEDS]\n        _, combined_p = combine_pvalues(pvals, method='fisher')\n        aggregated[\"selection_f1\"][sig] = {\n            \"per_seed\": {s: all_seed_results[s][sig][\"selection_f1\"] for s in SEEDS},\n            \"mean\": float(np.mean(sel_vals)),\n            \"std\": float(np.std(sel_vals, ddof=1)),\n            \"ci95\": bootstrap_ci(sel_vals),\n            \"delta_vs_greedy\": float(np.mean(sel_vals) - greedy_mean),\n            \"per_seed_p\": {s: all_seed_results[s][sig][\"sign_test_p\"] for s in SEEDS},\n            \"combined_p_fisher\": float(combined_p),\n            \"per_seed_wins\": {s: all_seed_results[s][sig][\"wins\"] for s in SEEDS},\n            \"per_seed_losses\": {s: all_seed_results[s][sig][\"losses\"] for s in SEEDS},\n            \"per_seed_ties\": {s: all_seed_results[s][sig][\"ties\"] for s in SEEDS},\n        }\n\n    # ── Fisher combined p-values for key claims ──\n    fisher_tests = {}\n\n    # Claim 1: SJ rho > LP rho (structural > surface on NER)\n    sj_rhos = [all_seed_results[s][\"rho\"][\"SJ\"] for s in SEEDS]\n    lp_rhos = [all_seed_results[s][\"rho\"][\"LP\"] for s in SEEDS]\n    diffs_sj_lp = [sj - lp for sj, lp in zip(sj_rhos, lp_rhos)]\n    all_positive_sj_lp = all(d > 0 for d in diffs_sj_lp)\n    fisher_tests[\"SJ_rho_gt_LP_rho\"] = {\n        \"claim\": \"SJ ρ > LP ρ on NER (structural > surface)\",\n        \"per_seed_diff\": {s: round(sj - lp, 4) for s, sj, lp in zip(SEEDS, sj_rhos, lp_rhos)},\n        \"all_seeds_consistent\": all_positive_sj_lp,\n        \"mean_diff\": round(float(np.mean(diffs_sj_lp)), 4),\n        \"bootstrap_p\": bootstrap_diff_pvalue(sj_rhos, lp_rhos),\n    }\n\n    # Claim 2: SJ rho > FK rho\n    fk_rhos = [all_seed_results[s][\"rho\"][\"FK\"] for s in SEEDS]\n    diffs_sj_fk = [sj - fk for sj, fk in zip(sj_rhos, fk_rhos)]\n    all_positive_sj_fk = all(d > 0 for d in diffs_sj_fk)\n    fisher_tests[\"SJ_rho_gt_FK_rho\"] = {\n        \"claim\": \"SJ ρ > FK ρ on NER\",\n        \"per_seed_diff\": {s: round(sj - fk, 4) for s, sj, fk in zip(SEEDS, sj_rhos, fk_rhos)},\n        \"all_seeds_consistent\": all_positive_sj_fk,\n        \"mean_diff\": round(float(np.mean(diffs_sj_fk)), 4),\n        \"bootstrap_p\": bootstrap_diff_pvalue(sj_rhos, fk_rhos),\n    }\n\n    # Claim 3: EM AUROC ranking\n    em_aurocs = [all_seed_results[s][\"auroc\"][\"EM\"] for s in SEEDS]\n    other_aurocs = {sig: [all_seed_results[s][\"auroc\"][sig] for s in SEEDS] for sig in SIGNALS if sig != \"EM\"}\n    em_vs_others = {}\n    for sig, vals in other_aurocs.items():\n        diffs = [em - v for em, v in zip(em_aurocs, vals)]\n        em_vs_others[sig] = {\n            \"per_seed_diff\": {s: round(d, 4) for s, d in zip(SEEDS, diffs)},\n            \"mean_diff\": round(float(np.mean(diffs)), 4),\n            \"all_positive\": all(d > 0 for d in diffs),\n        }\n    fisher_tests[\"EM_AUROC_vs_others\"] = {\n        \"claim\": \"EM AUROC > all other signals\",\n        \"comparisons\": em_vs_others,\n    }\n\n    aggregated[\"fisher_tests\"] = fisher_tests\n\n    # ── Comparison with 2-seed results (42, 123) ──\n    two_seed = {\"seeds\": [42, 123]}\n    for sig in SIGNALS:\n        sel_2 = [all_seed_results[s][sig][\"selection_f1\"] for s in [42, 123]]\n        sel_3 = [all_seed_results[s][sig][\"selection_f1\"] for s in SEEDS]\n        rho_2 = [all_seed_results[s][\"rho\"][sig] for s in [42, 123]]\n        rho_3 = [all_seed_results[s][\"rho\"][sig] for s in SEEDS]\n        two_seed[sig] = {\n            \"selection_f1_2seed\": {\"mean\": float(np.mean(sel_2)), \"std\": float(np.std(sel_2, ddof=1))},\n            \"selection_f1_3seed\": {\"mean\": float(np.mean(sel_3)), \"std\": float(np.std(sel_3, ddof=1))},\n            \"rho_2seed\": {\"mean\": round(float(np.mean(rho_2)), 4), \"std\": round(float(np.std(rho_2, ddof=1)), 4)},\n            \"rho_3seed\": {\"mean\": round(float(np.mean(rho_3)), 4), \"std\": round(float(np.std(rho_3, ddof=1)), 4)},\n            \"ci_narrowed_selection\": float(np.std(sel_3, ddof=1)) < float(np.std(sel_2, ddof=1)),\n            \"ci_narrowed_rho\": float(np.std(rho_3, ddof=1)) < float(np.std(rho_2, ddof=1)),\n        }\n    aggregated[\"two_vs_three_seed\"] = two_seed\n\n    # ── Save results.json ──\n    full_results = {\n        \"per_seed\": {s: all_seed_results[s] for s in SEEDS},\n        \"aggregated\": aggregated,\n    }\n    results_path = OUT_DIR / \"results.json\"\n    with open(results_path, \"w\") as f:\n        json.dump(full_results, f, indent=2, default=str)\n    print(f\"\\nSaved: {results_path}\")\n\n    # ── Generate report.md ──\n    report_lines = []\n    report_lines.append(\"# exp-022: 3-Seed Joint Analysis (SciERC NER, N=8)\")\n    report_lines.append(\"\")\n    report_lines.append(f\"Seeds: {SEEDS}\")\n    report_lines.append(f\"Dataset: SciERC NER, N=8, T=1.0, Qwen2.5-7B-Instruct\")\n    report_lines.append(\"\")\n\n    # Table 1: Per-seed rho\n    report_lines.append(\"## 1. Spearman ρ (signal vs greedy F1)\")\n    report_lines.append(\"\")\n    report_lines.append(\"| Signal | seed42 | seed123 | seed789 | Mean ± σ | 95% CI |\")\n    report_lines.append(\"|--------|--------|---------|---------|----------|--------|\")\n    for sig in SIGNALS:\n        r = aggregated[\"rho\"][sig]\n        ps = r[\"per_seed\"]\n        ci = r[\"ci95\"]\n        report_lines.append(\n            f\"| {sig} | {ps[42]:.4f} | {ps[123]:.4f} | {ps[789]:.4f} \"\n            f\"| {r['mean']:.4f} ± {r['std']:.4f} | [{ci[0]:.4f}, {ci[1]:.4f}] |\"\n        )\n    report_lines.append(\"\")\n\n    # Table 2: Per-seed AUROC\n    report_lines.append(\"## 2. AUROC\")\n    report_lines.append(\"\")\n    report_lines.append(\"| Signal | seed42 | seed123 | seed789 | Mean ± σ | 95% CI |\")\n    report_lines.append(\"|--------|--------|---------|---------|----------|--------|\")\n    for sig in SIGNALS:\n        r = aggregated[\"auroc\"][sig]\n        ps = r[\"per_seed\"]\n        ci = r[\"ci95\"]\n        report_lines.append(\n            f\"| {sig} | {ps[42]:.4f} | {ps[123]:.4f} | {ps[789]:.4f} \"\n            f\"| {r['mean']:.4f} ± {r['std']:.4f} | [{ci[0]:.4f}, {ci[1]:.4f}] |\"\n        )\n    report_lines.append(\"\")\n\n    # Table 3: Selection F1\n    report_lines.append(\"## 3. Selection macro F1\")\n    report_lines.append(\"\")\n    report_lines.append(\"| Method | seed42 | seed123 | seed789 | Mean ± σ | ΔF1 vs Greedy | Fisher p |\")\n    report_lines.append(\"|--------|--------|---------|---------|----------|---------------|----------|\")\n\n    gps = aggregated[\"greedy_f1\"][\"per_seed\"]\n    gm = aggregated[\"greedy_f1\"]\n    report_lines.append(\n        f\"| Greedy | {gps[42]:.4f} | {gps[123]:.4f} | {gps[789]:.4f} \"\n        f\"| {gm['mean']:.4f} ± {gm['std']:.4f} | — | — |\"\n    )\n    rps = aggregated[\"random_f1\"][\"per_seed\"]\n    rm = aggregated[\"random_f1\"]\n    report_lines.append(\n        f\"| Random | {rps[42]:.4f} | {rps[123]:.4f} | {rps[789]:.4f} \"\n        f\"| {rm['mean']:.4f} ± {rm['std']:.4f} | {rm['mean'] - gm['mean']:+.4f} | — |\"\n    )\n    for sig in SIGNALS:\n        r = aggregated[\"selection_f1\"][sig]\n        ps = r[\"per_seed\"]\n        report_lines.append(\n            f\"| {sig} | {ps[42]:.4f} | {ps[123]:.4f} | {ps[789]:.4f} \"\n            f\"| {r['mean']:.4f} ± {r['std']:.4f} | {r['delta_vs_greedy']:+.4f} | {r['combined_p_fisher']:.4f} |\"\n        )\n    ops = aggregated[\"oracle_f1\"][\"per_seed\"]\n    om = aggregated[\"oracle_f1\"]\n    report_lines.append(\n        f\"| Oracle | {ops[42]:.4f} | {ops[123]:.4f} | {ops[789]:.4f} \"\n        f\"| {om['mean']:.4f} ± {om['std']:.4f} | {om['mean'] - gm['mean']:+.4f} | — |\"\n    )\n    report_lines.append(\"\")\n\n    # Fisher tests\n    report_lines.append(\"## 4. Fisher Combined Tests for Key Claims\")\n    report_lines.append(\"\")\n    for test_name, test_data in fisher_tests.items():\n        report_lines.append(f\"### {test_data['claim']}\")\n        if \"per_seed_diff\" in test_data:\n            report_lines.append(f\"- Per-seed diff: {test_data['per_seed_diff']}\")\n            report_lines.append(f\"- All seeds consistent: {test_data['all_seeds_consistent']}\")\n            report_lines.append(f\"- Mean diff: {test_data['mean_diff']}\")\n            report_lines.append(f\"- Bootstrap p: {test_data['bootstrap_p']:.4f}\")\n        elif \"comparisons\" in test_data:\n            for sig, comp in test_data[\"comparisons\"].items():\n                report_lines.append(f\"- EM vs {sig}: mean diff = {comp['mean_diff']}, all positive = {comp['all_positive']}\")\n        report_lines.append(\"\")\n\n    # 2-seed vs 3-seed comparison\n    report_lines.append(\"## 5. 2-Seed vs 3-Seed Comparison\")\n    report_lines.append(\"\")\n    report_lines.append(\"| Signal | 2-seed F1 (mean±σ) | 3-seed F1 (mean±σ) | CI narrowed? | 2-seed ρ | 3-seed ρ |\")\n    report_lines.append(\"|--------|--------------------|--------------------|--------------|----------|----------|\")\n    for sig in SIGNALS:\n        t = two_seed[sig]\n        s2f = t[\"selection_f1_2seed\"]\n        s3f = t[\"selection_f1_3seed\"]\n        s2r = t[\"rho_2seed\"]\n        s3r = t[\"rho_3seed\"]\n        narrowed = \"✓\" if t[\"ci_narrowed_selection\"] else \"✗\"\n        report_lines.append(\n            f\"| {sig} | {s2f['mean']:.4f}±{s2f['std']:.4f} | {s3f['mean']:.4f}±{s3f['std']:.4f} \"\n            f\"| {narrowed} | {s2r['mean']:.4f}±{s2r['std']:.4f} | {s3r['mean']:.4f}±{s3r['std']:.4f} |\"\n        )\n    report_lines.append(\"\")\n\n    report_path = OUT_DIR / \"report.md\"\n    with open(report_path, \"w\") as f:\n        f.write(\"\\n\".join(report_lines))\n    print(f\"Saved: {report_path}\")\n\n    # Print summary\n    print(\"\\n\" + \"=\" * 60)\n    print(\"SUMMARY\")\n    print(\"=\" * 60)\n    print(f\"\\nGreedy macro F1: {gm['mean']:.4f} ± {gm['std']:.4f}\")\n    print(f\"Oracle macro F1: {om['mean']:.4f} ± {om['std']:.4f}\")\n    print(f\"\\nSelection F1 (3-seed mean ± std):\")\n    for sig in SIGNALS:\n        r = aggregated[\"selection_f1\"][sig]\n        print(f\"  {sig}: {r['mean']:.4f} ± {r['std']:.4f}  (Δ={r['delta_vs_greedy']:+.4f}, Fisher p={r['combined_p_fisher']:.4f})\")\n    print(f\"\\nSpearman ρ (3-seed mean ± std):\")\n    for sig in SIGNALS:\n        r = aggregated[\"rho\"][sig]\n        print(f\"  {sig}: {r['mean']:.4f} ± {r['std']:.4f}\")\n    print(f\"\\nAUROC (3-seed mean ± std):\")\n    for sig in SIGNALS:\n        r = aggregated[\"auroc\"][sig]\n        print(f\"  {sig}: {r['mean']:.4f} ± {r['std']:.4f}\")\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-16T10:57:47.183995+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T10:57:47.184173+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/struct_self_consist_ie && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && nohup python output/exp_022_3seed_analysis/analyze_3seed.py > /tmp/exp022_3seed.log 2>&1 & echo \"PID=$!\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/struct_self_consist_ie && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && nohup python output/exp_022_3seed_analysis/analyze_3seed.py > /tmp/exp022_3seed.log 2>&1 & echo \"PID=$!\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-16T10:57:47.184334+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"PID=290334\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.11}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-16T10:57:47.184521+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "tail -20 /tmp/exp022_3seed.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "tail -20 /tmp/exp022_3seed.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-16T10:57:47.184678+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Selection F1 (3-seed mean ± std):\\n  LP: 0.6472 ± 0.0033  (Δ=+0.0003, Fisher p=0.4287)\\n  SJ: 0.6434 ± 0.0050  (Δ=-0.0035, Fisher p=0.3837)\\n  FK: 0.6442 ± 0.0030  (Δ=-0.0027, Fisher p=0.8965)\\n  EM: 0.6383 ± 0.0022  (Δ=-0.0086, Fisher p=0.7185)\\n  VC: 0.6218 ± 0.0033  (Δ=-0.0251, Fisher p=0.0307)\\n\\nSpearman ρ (3-seed mean ± std):\\n  LP: 0.2155 ± 0.0161\\n  SJ: 0.3772 ± 0.0151\\n  FK: 0.2545 ± 0.0177\\n  EM: 0.3039 ± 0.0095\\n  VC: 0.4144 ± 0.0357\\n\\nAUROC (3-seed mean ± std):\\n  LP: 0.6124 ± 0.0008\\n  SJ: 0.6842 ± 0.0111\\n  FK: 0.6158 ± 0.0140\\n  EM: 0.6512 ± 0.0073\\n  VC: 0.7064 ± 0.0173\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-16T10:57:47.184839+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /tmp/exp022_3seed.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /tmp/exp022_3seed.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-16T10:57:47.184990+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"============================================================\\nexp-022: 3-seed analysis (42, 123, 789) — SciERC NER N=8\\n============================================================\\n\\n--- Seed 42 ---\\n  seed=42: 529 valid instances, N=8\\n    100/529 (0.1s)\\n    200/529 (0.2s)\\n    300/529 (0.3s)\\n    400/529 (0.4s)\\n    500/529 (0.5s)\\n  seed=42 done (0.5s)\\n\\n--- Seed 123 ---\\n  seed=123: 529 valid instances, N=8\\n    100/529 (0.1s)\\n    200/529 (0.2s)\\n    300/529 (0.3s)\\n    400/529 (0.4s)\\n    500/529 (0.5s)\\n  seed=123 done (0.5s)\\n\\n--- Seed 789 ---\\n  seed=789: 529 valid instances, N=8\\n    100/529 (0.1s)\\n    200/529 (0.2s)\\n    300/529 (0.3s)\\n    400/529 (0.4s)\\n    500/529 (0.5s)\\n  seed=789 done (0.5s)\\n\\nSaved: /root/autodl-tmp/struct_self_consist_ie/output/exp_022_3seed_analysis/results.json\\nSaved: /root/autodl-tmp/struct_self_consist_ie/output/exp_022_3seed_analysis/report.md\\n\\n============================================================\\nSUMMARY\\n============================================================\\n\\nGreedy macro F1: 0.6469 ± 0.0037\\nOracle macro F1: 0.7816 ± 0.0064\\n\\nSelection F1 (3-seed mean ± std):\\n  LP: 0.6472 ± 0.0033  (Δ=+0.0003, Fisher p=0.4287)\\n  SJ: 0.6434 ± 0.0050  (Δ=-0.0035, Fisher p=0.3837)\\n  FK: 0.6442 ± 0.0030  (Δ=-0.0027, Fisher p=0.8965)\\n  EM: 0.6383 ± 0.0022  (Δ=-0.0086, Fisher p=0.7185)\\n  VC: 0.6218 ± 0.0033  (Δ=-0.0251, Fisher p=0.0307)\\n\\nSpearman ρ (3-seed mean ± std):\\n  LP: 0.2155 ± 0.0161\\n  SJ: 0.3772 ± 0.0151\\n  FK: 0.2545 ± 0.0177\\n  EM: 0.3039 ± 0.0095\\n  VC: 0.4144 ± 0.0357\\n\\nAUROC (3-seed mean ± std):\\n  LP: 0.6124 ± 0.0008\\n  SJ: 0.6842 ± 0.0111\\n  FK: 0.6158 ± 0.0140\\n  EM: 0.6512 ± 0.0073\\n  VC: 0.7064 ± 0.0173\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-16T10:57:47.185169+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_022_3seed_analysis/report.md",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_022_3seed_analysis/report.md",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-16T10:57:47.185357+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# exp-022: 3-Seed Joint Analysis (SciERC NER, N=8)\\n\\nSeeds: [42, 123, 789]\\nDataset: SciERC NER, N=8, T=1.0, Qwen2.5-7B-Instruct\\n\\n## 1. Spearman ρ (signal vs greedy F1)\\n\\n| Signal | seed42 | seed123 | seed789 | Mean ± σ | 95% CI |\\n|--------|--------|---------|---------|----------|--------|\\n| LP | 0.2052 | 0.2341 | 0.2073 | 0.2155 ± 0.0161 | [0.2052, 0.2341] |\\n| SJ | 0.3599 | 0.3878 | 0.3838 | 0.3772 ± 0.0151 | [0.3599, 0.3878] |\\n| FK | 0.2665 | 0.2628 | 0.2342 | 0.2545 ± 0.0177 | [0.2342, 0.2665] |\\n| EM | 0.2945 | 0.3135 | 0.3036 | 0.3039 ± 0.0095 | [0.2945, 0.3135] |\\n| VC | 0.3792 | 0.4133 | 0.4506 | 0.4144 ± 0.0357 | [0.3792, 0.4506] |\\n\\n## 2. AUROC\\n\\n| Signal | seed42 | seed123 | seed789 | Mean ± σ | 95% CI |\\n|--------|--------|---------|---------|----------|--------|\\n| LP | 0.6116 | 0.6132 | 0.6124 | 0.6124 ± 0.0008 | [0.6116, 0.6132] |\\n| SJ | 0.6715 | 0.6919 | 0.6893 | 0.6842 ± 0.0111 | [0.6715, 0.6919] |\\n| FK | 0.6154 | 0.6300 | 0.6020 | 0.6158 ± 0.0140 | [0.6020, 0.6300] |\\n| EM | 0.6472 | 0.6596 | 0.6468 | 0.6512 ± 0.0073 | [0.6468, 0.6596] |\\n| VC | 0.6879 | 0.7089 | 0.7223 | 0.7064 ± 0.0173 | [0.6879, 0.7223] |\\n\\n## 3. Selection macro F1\\n\\n| Method | seed42 | seed123 | seed789 | Mean ± σ | ΔF1 vs Greedy | Fisher p |\\n|--------|--------|---------|---------|----------|---------------|----------|\\n| Greedy | 0.6439 | 0.6457 | 0.6511 | 0.6469 ± 0.0037 | — | — |\\n| Random | 0.6043 | 0.6119 | 0.6128 | 0.6096 ± 0.0047 | -0.0373 | — |\\n| LP | 0.6501 | 0.6436 | 0.6478 | 0.6472 ± 0.0033 | +0.0003 | 0.4287 |\\n| SJ | 0.6450 | 0.6475 | 0.6378 | 0.6434 ± 0.0050 | -0.0035 | 0.3837 |\\n| FK | 0.6448 | 0.6468 | 0.6410 | 0.6442 ± 0.0030 | -0.0027 | 0.8965 |\\n| EM | 0.6362 | 0.6381 | 0.6406 | 0.6383 ± 0.0022 | -0.0086 | 0.7185 |\\n| VC | 0.6256 | 0.6204 | 0.6195 | 0.6218 ± 0.0033 | -0.0251 | 0.0307 |\\n| Oracle | 0.7758 | 0.7805 | 0.7885 | 0.7816 ± 0.0064 | +0.1347 | — 
…[truncated 1372 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-16T10:57:47.185531+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "exp-022 3-seed analysis results",
  "type": "data",
  "description": "3-seed (42, 123, 789) bootstrap statistics for SciERC NER N=8: per-seed rho/AUROC/selection-F1, aggregated mean±std, 95% CI, Fisher combined p-values, 2-vs-3 seed comparison",
  "project": "struct_self_consist_ie",
  "exp_id": "exp-022",
  "source_path": "/root/autodl-tmp/struct_self_consist_ie/output/exp_022_3seed_analysis/results.json",
  "tags": "['3seed', 'bootstrap', 'scierc', 'ner', 'selection-f1', 'rho', 'auroc']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "exp-022 3-seed analysis results",
    "type": "data",
    "description": "3-seed (42, 123, 789) bootstrap statistics for SciERC NER N=8: per-seed rho/AUROC/selection-F1, aggregated mean±std, 95% CI, Fisher combined p-values, 2-vs-3 seed comparison",
    "project": "struct_self_consist_ie",
    "exp_id": "exp-022",
    "source_path": "/root/autodl-tmp/struct_self_consist_ie/output/exp_022_3seed_analysis/results.json",
    "tags": "['3seed', 'bootstrap', 'scierc', 'ner', 'selection-f1', 'rho', 'auroc']"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-16T10:57:47.185678+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"source_path not found: /root/autodl-tmp/struct_self_consist_ie/output/exp_022_3seed_analysis/results.json\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-16T10:57:47.185803+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "exp-022 3-seed analysis report",
  "type": "report",
  "description": "Human-readable 3-seed (42, 123, 789) analysis report with tables for rho, AUROC, selection F1, Fisher tests, and 2-vs-3 seed comparison",
  "project": "struct_self_consist_ie",
  "exp_id": "exp-022",
  "source_path": "/root/autodl-tmp/struct_self_consist_ie/output/exp_022_3seed_analysis/report.md",
  "tags": "['3seed', 'report', 'scierc']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "exp-022 3-seed analysis report",
    "type": "report",
    "description": "Human-readable 3-seed (42, 123, 789) analysis report with tables for rho, AUROC, selection F1, Fisher tests, and 2-vs-3 seed comparison",
    "project": "struct_self_consist_ie",
    "exp_id": "exp-022",
    "source_path": "/root/autodl-tmp/struct_self_consist_ie/output/exp_022_3seed_analysis/report.md",
    "tags": "['3seed', 'report', 'scierc']"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-16T10:57:47.185930+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"source_path not found: /root/autodl-tmp/struct_self_consist_ie/output/exp_022_3seed_analysis/report.md\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-16T10:57:47.186047+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "exp-022 3-seed analysis script",
  "type": "intermediate",
  "description": "Analysis script computing 3-seed rho/AUROC/selection-F1/bootstrap/Fisher for SciERC NER N=8",
  "project": "struct_self_consist_ie",
  "exp_id": "exp-022",
  "source_path": "/root/autodl-tmp/struct_self_consist_ie/output/exp_022_3seed_analysis/analyze_3seed.py",
  "tags": "['3seed', 'script']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "exp-022 3-seed analysis script",
    "type": "intermediate",
    "description": "Analysis script computing 3-seed rho/AUROC/selection-F1/bootstrap/Fisher for SciERC NER N=8",
    "project": "struct_self_consist_ie",
    "exp_id": "exp-022",
    "source_path": "/root/autodl-tmp/struct_self_consist_ie/output/exp_022_3seed_analysis/analyze_3seed.py",
    "tags": "['3seed', 'script']"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-16T10:57:47.186192+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"source_path not found: /root/autodl-tmp/struct_self_consist_ie/output/exp_022_3seed_analysis/analyze_3seed.py\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-16T10:57:47.186336+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_022_3seed_analysis/results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_022_3seed_analysis/results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-16T10:57:47.186669+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"per_seed\\\": {\\n    \\\"42\\\": {\\n      \\\"n_instances\\\": 529,\\n      \\\"n_samples\\\": 8,\\n      \\\"greedy_f1\\\": 0.6439219990259687,\\n      \\\"oracle_f1\\\": 0.7758023559647044,\\n      \\\"random_f1\\\": 0.6042916211488025,\\n      \\\"rho\\\": {\\n        \\\"LP\\\": 0.2052,\\n        \\\"SJ\\\": 0.3599,\\n        \\\"FK\\\": 0.2665,\\n        \\\"EM\\\": 0.2945,\\n        \\\"VC\\\": 0.3792\\n      },\\n      \\\"auroc\\\": {\\n        \\\"LP\\\": 0.6116,\\n        \\\"SJ\\\": 0.6715,\\n        \\\"FK\\\": 0.6154,\\n        \\\"EM\\\": 0.6472,\\n        \\\"VC\\\": 0.6879\\n      },\\n      \\\"LP\\\": {\\n        \\\"selection_f1\\\": 0.6500718843902431,\\n        \\\"sign_test_p\\\": 0.5425074179193997,\\n        \\\"wins\\\": 62,\\n        \\\"losses\\\": 70,\\n        \\\"ties\\\": 398\\n      },\\n      \\\"SJ\\\": {\\n        \\\"selection_f1\\\": 0.6450050009215592,\\n        \\\"sign_test_p\\\": 0.5657001139736343,\\n        \\\"wins\\\": 58,\\n        \\\"losses\\\": 51,\\n        \\\"ties\\\": 420\\n      },\\n      \\\"FK\\\": {\\n        \\\"selection_f1\\\": 0.6448289220120209,\\n        \\\"sign_test_p\\\": 0.5085131799736624,\\n        \\\"wins\\\": 60,\\n        \\\"losses\\\": 52,\\n        \\\"ties\\\": 417\\n      },\\n      \\\"EM\\\": {\\n        \\\"selection_f1\\\": 0.636232670839558,\\n        \\\"sign_test_p\\\": 0.4672071020769656,\\n        \\\"wins\\\": 56,\\n        \\\"losses\\\": 65,\\n        \\\"ties\\\": 408\\n      },\\n      \\\"VC\\\": {\\n        \\\"selection_f1\\\": 0.6256062548645376,\\n        \\\"sign_test_p\\\": 0.40202361223750865,\\n        \\\"wins\\\": 96,\\n        \\\"losses\\\": 109,\\n        \\\"ties\\\": 325\\n      }\\n    },\\n    \\\"123\\\": {\\n      \\\"n_instances\\\": 529,\\n      \\\"n_samples\\\": 8,\\n      \\\"greedy_f1\\\": 0.6457455273145254,\\n      \\\"oracle_f1\\\": 0.7804973434463037,\\n      \\\"random_f1\\\": 
…[truncated 8488 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-16T10:57:47.186863+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "exp-022 3-seed analysis results",
  "type": "data",
  "description": "3-seed (42, 123, 789) bootstrap statistics for SciERC NER N=8: per-seed rho/AUROC/selection-F1, aggregated mean±std, 95% CI, Fisher combined p-values, 2-vs-3 seed comparison",
  "project": "struct_self_consist_ie",
  "exp_id": "exp-022",
  "content": "See remote: /root/autodl-tmp/struct_self_consist_ie/output/exp_022_3seed_analysis/results.json",
  "content_filename": "results.json",
  "tags": "['3seed', 'bootstrap', 'scierc', 'ner', 'selection-f1', 'rho', 'auroc']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "exp-022 3-seed analysis results",
    "type": "data",
    "description": "3-seed (42, 123, 789) bootstrap statistics for SciERC NER N=8: per-seed rho/AUROC/selection-F1, aggregated mean±std, 95% CI, Fisher combined p-values, 2-vs-3 seed comparison",
    "project": "struct_self_consist_ie",
    "exp_id": "exp-022",
    "content": "See remote: /root/autodl-tmp/struct_self_consist_ie/output/exp_022_3seed_analysis/results.json",
    "content_filename": "results.json",
    "tags": "['3seed', 'bootstrap', 'scierc', 'ner', 'selection-f1', 'rho', 'auroc']"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-16T10:57:47.187028+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_7fb481\", \"name\": \"exp-022 3-seed analysis results\", \"type\": \"data\", \"description\": \"3-seed (42, 123, 789) bootstrap statistics for SciERC NER N=8: per-seed rho/AUROC/selection-F1, aggregated mean±std, 95% CI, Fisher combined p-values, 2-vs-3 seed comparison\", \"path\": \"projects/struct_self_consist_ie/artifacts/exp-022/data/results.json\", \"url\": null, \"project\": \"struct_self_consist_ie\", \"exp_id\": \"exp-022\", \"skill\": \"\", \"created_at\": \"2026-05-16T10:57:27.798626+00:00\", \"tags\": [\"3seed\", \"bootstrap\", \"scierc\", \"ner\", \"selection-f1\", \"rho\", \"auroc\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-16T10:57:47.187199+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "exp-022 3-seed analysis report",
  "type": "report",
  "description": "Human-readable 3-seed (42, 123, 789) analysis report with tables for rho, AUROC, selection F1, Fisher tests, and 2-vs-3 seed comparison",
  "project": "struct_self_consist_ie",
  "exp_id": "exp-022",
  "content": "See remote: /root/autodl-tmp/struct_self_consist_ie/output/exp_022_3seed_analysis/report.md",
  "content_filename": "report.md",
  "tags": "['3seed', 'report', 'scierc']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "exp-022 3-seed analysis report",
    "type": "report",
    "description": "Human-readable 3-seed (42, 123, 789) analysis report with tables for rho, AUROC, selection F1, Fisher tests, and 2-vs-3 seed comparison",
    "project": "struct_self_consist_ie",
    "exp_id": "exp-022",
    "content": "See remote: /root/autodl-tmp/struct_self_consist_ie/output/exp_022_3seed_analysis/report.md",
    "content_filename": "report.md",
    "tags": "['3seed', 'report', 'scierc']"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-16T10:57:47.187351+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_873b1b\", \"name\": \"exp-022 3-seed analysis report\", \"type\": \"report\", \"description\": \"Human-readable 3-seed (42, 123, 789) analysis report with tables for rho, AUROC, selection F1, Fisher tests, and 2-vs-3 seed comparison\", \"path\": \"projects/struct_self_consist_ie/artifacts/exp-022/report/report.md\", \"url\": null, \"project\": \"struct_self_consist_ie\", \"exp_id\": \"exp-022\", \"skill\": \"\", \"created_at\": \"2026-05-16T10:57:30.407915+00:00\", \"tags\": [\"3seed\", \"report\", \"scierc\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-16T10:57:47.187480+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "exp-022 3-seed analysis script",
  "type": "intermediate",
  "description": "Python script computing 3-seed rho/AUROC/selection-F1/bootstrap/Fisher for SciERC NER N=8",
  "project": "struct_self_consist_ie",
  "exp_id": "exp-022",
  "content": "See remote: /root/autodl-tmp/struct_self_consist_ie/output/exp_022_3seed_analysis/analyze_3seed.py",
  "content_filename": "analyze_3seed.py",
  "tags": "['3seed', 'script']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "exp-022 3-seed analysis script",
    "type": "intermediate",
    "description": "Python script computing 3-seed rho/AUROC/selection-F1/bootstrap/Fisher for SciERC NER N=8",
    "project": "struct_self_consist_ie",
    "exp_id": "exp-022",
    "content": "See remote: /root/autodl-tmp/struct_self_consist_ie/output/exp_022_3seed_analysis/analyze_3seed.py",
    "content_filename": "analyze_3seed.py",
    "tags": "['3seed', 'script']"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-16T10:57:47.187617+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_8a72a5\", \"name\": \"exp-022 3-seed analysis script\", \"type\": \"intermediate\", \"description\": \"Python script computing 3-seed rho/AUROC/selection-F1/bootstrap/Fisher for SciERC NER N=8\", \"path\": \"projects/struct_self_consist_ie/artifacts/exp-022/intermediate/analyze_3seed.py\", \"url\": null, \"project\": \"struct_self_consist_ie\", \"exp_id\": \"exp-022\", \"skill\": \"\", \"created_at\": \"2026-05-16T10:57:32.629095+00:00\", \"tags\": [\"3seed\", \"script\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 61 · 2026-05-16T10:57:47.187784+00:00_

3 artifacts registered. Here's the summary:

## exp-022 3-Seed (42, 123, 789) Analysis Results — SciERC NER N=8

### Spearman ρ (3-seed mean ± std)
| Signal | Mean | Std |
|--------|------|-----|
| **VC** | **0.4144** | 0.0357 |
| **SJ** | **0.3772** | 0.0151 |
| EM | 0.3039 | 0.0095 |
| FK | 0.2545 | 0.0177 |
| LP | 0.2155 | 0.0161 |

### AUROC (3-seed mean ± std)
| Signal | Mean | Std |
|--------|------|-----|
| **VC** | **0.7064** | 0.0173 |
| **SJ** | **0.6842** | 0.0111 |
| EM | 0.6512 | 0.0073 |
| FK | 0.6158 | 0.0140 |
| LP | 0.6124 | 0.0008 |

### Selection macro F1
| Method | Mean ± σ | ΔF1 vs Greedy |
|--------|----------|---------------|
| Greedy | 0.6469 ± 0.0037 | — |
| **LP** | **0.6472 ± 0.0033** | **+0.0003** |
| FK | 0.6442 ± 0.0030 | -0.0027 |
| SJ | 0.6434 ± 0.0050 | -0.0035 |
| EM | 0.6383 ± 0.0022 | -0.0086 |
| VC | 0.6218 ± 0.0033 | -0.0251 |
| Oracle | 0.7816 ± 0.0064 | +0.1347 |

### Key Fisher Tests
- **SJ ρ > LP ρ**: All 3 seeds consistent (diffs: 0.15–0.18). Structural beats surface.
- **SJ ρ > FK ρ**: All 3 seeds consistent (diffs: 0.09–0.15).
- **EM AUROC > all others**: False. EM < SJ and EM < VC consistently.

### 2-Seed vs 3-Seed
- ρ CIs narrowed for LP, SJ, EM (3/5 signals)
- Selection F1 CIs narrowed for LP, VC (2/5 signals)
- Conclusions unchanged: LP selection ≈ greedy, VC consistently worst at sample selection despite best ρ/AUROC

Output at: `/root/autodl-tmp/struct_self_consist_ie/output/exp_022_3seed_analysis/`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_exp_022_3seed_analysis_20260516T105321"
}
```

</details>

---
