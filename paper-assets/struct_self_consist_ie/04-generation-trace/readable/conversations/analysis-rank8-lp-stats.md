# analysis rank8 lp stats

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/chats/worker_analysis_rank8_lp_stats_20260518T005609.jsonl`
- **Structured JSON:** [`9d9fae1facad829bc459.json`](../../sessions/9d/9d9fae1facad829bc459.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

33 recorded events

### Tool call

_source line 1 · 2026-05-18T00:58:57.685798+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rank8_lp_stats_20260518T005609",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T00:58:57.686103+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rank8_lp_stats_20260518T005609",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T00:58:57.686340+00:00_

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
  "session": "worker_analysis_rank8_lp_stats_20260518T005609",
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

_source line 4 · 2026-05-18T00:58:57.686485+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/output/ -name \"*023*\" -o -name \"*rank8*\" -o -name \"*rank_8*\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rank8_lp_stats_20260518T005609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/output/ -name \"*023*\" -o -name \"*rank8*\" -o -name \"*rank_8*\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-18T00:58:57.686678+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"adalp_analysis_results.json\\nanalysis_epsilon_sweep\\nanalysis_fk_bootstrap_ci.json\\nanalysis_fk_bootstrap_per_instance.json\\nanalysis_lp_range_cdf.json\\nanalysis_lp_range_cdf_n16_3seed.json\\nanalysis_multiseed_selection_f1.json\\nanalysis_round8\\nanalysis_scierc_n16_3seed_selection_f1.json\\nanalysis_scierc_n16_3seed_selection_f1_merged.json\\nanalysis_scierc_re_n16_3seed_selection_f1.json\\nanalysis_unified_rho_full.json\\nbootstrap_ci_nscaling\\nbootstrap_ci_summary.json\\nbootstrap_ci_tables.tex\\ncalibration_baseline_results.json\\nconditional_filter_diagnosis.json\\nd108_greedy_f1\\nd108_lp_vc_combination\\nd108_mbr_within_rho\\nd108_q4q5\\nd110_4b_degeneracy\\nd112_disk_cleanup\\nd112_hybrid_strategy\\nd112_mf3_random_single\\nd112_table2_fix\\nd114_auroc_investigation\\nexp001_n16_seed123\\nexp001_n16_seed123_200only\\nexp001_n16_seed123_200only_backup\\nexp001_n16_seed123_full\\nexp001_n16_seed123_run.log\\nexp001_n16_seed42\\nexp001_n16_seed42_200only_backup\\nexp001_n16_seed42_run.log\\nexp001_n16_seed456\\nexp001_n16_seed456_200only\\nexp001_n16_seed456_run.log\\nexp001_seed123_t10_full\\nexp001_seed123_t10_full.log\\nexp001_seed456_t10_full\\nexp001_seed456_t10_full.log\\nexp002_conll2003\\nexp003_wnut17_dryrun\\nexp003_wnut17_eval\\nexp003_wnut17_eval.log\\nexp003_wnut17_pilot\\nexp003_wnut17_pilot.log\\nexp004_re_diagnostic\\nexp004v2_re_diagnostic\\nexp007_llama_dryrun\\nexp007_llama_inference\\nexp008_re_n16\\nexp008_re_n16_200only\\nexp008_re_n16_t10_full\\nexp008_re_n16_t10_full.log\\nexp009_stratification_results.json\\nexp010_selection_curves\\nexp016_signal_ensemble\\nexp018_3seed_5signal_results.json\\nexp_001_seed123_v2\\nexp_001_seed123_v2_r1024\\nexp_001_seed42_v2\\nexp_001_seed42_v2_r1024\\nexp_001_seed456_v2\\nexp_001_seed456_v2_ner\\nexp_001_seed456_v2_ner.log\\nexp_001_seed456_v2_ner_r1024\\nexp_002_conll_n16\\nexp_002_conll_n16.log\\nexp_002_conll_n16_r1024\\nexp_003_wnut17_
…[truncated 2939 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rank8_lp_stats_20260518T005609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T00:58:57.686831+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rank8_lp_stats_20260518T005609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T00:58:57.686966+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/output/ -name \"*012*\" -o -name \"*rank32*\" -o -name \"*rank_32*\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rank8_lp_stats_20260518T005609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/output/ -name \"*012*\" -o -name \"*rank32*\" -o -name \"*rank_32*\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T00:58:57.687102+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rank8_lp_stats_20260518T005609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T00:58:57.687302+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/output/exp_023_rank8_inference/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rank8_lp_stats_20260518T005609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/output/exp_023_rank8_inference/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-18T00:58:57.687434+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/output/exp_012_logprob/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rank8_lp_stats_20260518T005609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/output/exp_012_logprob/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-18T00:58:57.687572+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 21956\\ndrwxr-xr-x   2 root root      119 May 16 19:21 .\\ndrwxr-xr-x 124 root root     8192 May 18 04:06 ..\\n-rw-r--r--   1 root root     4163 May 16 19:21 all_signals_5signal.json\\n-rw-r--r--   1 root root     1968 May 16 19:21 comparison.md\\n-rw-r--r--   1 root root     3375 May 16 19:21 report.json\\n-rw-r--r--   1 root root 22453970 May 16 19:21 samples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rank8_lp_stats_20260518T005609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T00:58:57.687704+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 3276\\ndrwxr-xr-x   2 root root      81 May 14 19:06 .\\ndrwxr-xr-x 124 root root    8192 May 18 04:06 ..\\n-rw-r--r--   1 root root    6196 May 14 19:06 analysis_report.json\\n-rw-r--r--   1 root root 3333863 May 14 19:04 samples_with_logprobs.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rank8_lp_stats_20260518T005609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T00:58:57.687825+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -5 /root/autodl-tmp/struct_self_consist_ie/output/exp_023_rank8_inference/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rank8_lp_stats_20260518T005609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -5 /root/autodl-tmp/struct_self_consist_ie/output/exp_023_rank8_inference/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-18T00:58:57.687950+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -3 /root/autodl-tmp/struct_self_consist_ie/output/exp_012_logprob/samples_with_logprobs.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rank8_lp_stats_20260518T005609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -3 /root/autodl-tmp/struct_self_consist_ie/output/exp_012_logprob/samples_with_logprobs.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-18T00:58:57.688295+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"id\\\": \\\"X96-1059_sent000\\\", \\\"text\\\": \\\"Recognition of proper nouns in Japanese text has been studied as a part of the more general problem of morphological analysis in Japanese text processing -LRB- -LSB- 1 -RSB- -LSB- 2 -RSB- -RRB- .\\\", \\\"gold\\\": {\\\"entities\\\": [{\\\"text\\\": \\\"Recognition of proper nouns\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 0, \\\"end\\\": 27}, {\\\"text\\\": \\\"proper nouns\\\", \\\"type\\\": \\\"OtherScientificTerm\\\", \\\"start\\\": 15, \\\"end\\\": 27}, {\\\"text\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"Material\\\", \\\"start\\\": 31, \\\"end\\\": 44}, {\\\"text\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 103, \\\"end\\\": 125}, {\\\"text\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 129, \\\"end\\\": 153}], \\\"relations\\\": [{\\\"head\\\": \\\"Recognition of proper nouns\\\", \\\"tail\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"PART-OF\\\", \\\"head_start\\\": 0, \\\"head_end\\\": 27, \\\"tail_start\\\": 103, \\\"tail_end\\\": 125}, {\\\"head\\\": \\\"proper nouns\\\", \\\"tail\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"PART-OF\\\", \\\"head_start\\\": 15, \\\"head_end\\\": 27, \\\"tail_start\\\": 31, \\\"tail_end\\\": 44}, {\\\"head\\\": \\\"morphological analysis\\\", \\\"tail\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"USED-FOR\\\", \\\"head_start\\\": 103, \\\"head_end\\\": 125, \\\"tail_start\\\": 129, \\\"tail_end\\\": 153}], \\\"events\\\": []}, \\\"samples\\\": [{\\\"entities\\\": [{\\\"text\\\": \\\"Recognition of proper nouns in Japanese text\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 0, \\\"end\\\": 44}, {\\\"text\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"Material\\\", \\\"start\\\": 31, \\\"end\\\": 44}, {\\\"text\\\": \\\"morphological analysis in Japanese text processing\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\"
…[truncated 8821 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rank8_lp_stats_20260518T005609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T00:58:57.688712+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"id\\\": \\\"X96-1059_sent000\\\", \\\"text\\\": \\\"Recognition of proper nouns in Japanese text has been studied as a part of the more general problem of morphological analysis in Japanese text processing -LRB- -LSB- 1 -RSB- -LSB- 2 -RSB- -RRB- .\\\", \\\"gold\\\": {\\\"entities\\\": [{\\\"text\\\": \\\"Recognition of proper nouns\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 0, \\\"end\\\": 27}, {\\\"text\\\": \\\"proper nouns\\\", \\\"type\\\": \\\"OtherScientificTerm\\\", \\\"start\\\": 15, \\\"end\\\": 27}, {\\\"text\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"Material\\\", \\\"start\\\": 31, \\\"end\\\": 44}, {\\\"text\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 103, \\\"end\\\": 125}, {\\\"text\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 129, \\\"end\\\": 153}], \\\"relations\\\": [{\\\"head\\\": \\\"Recognition of proper nouns\\\", \\\"tail\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"PART-OF\\\", \\\"head_start\\\": 0, \\\"head_end\\\": 27, \\\"tail_start\\\": 103, \\\"tail_end\\\": 125}, {\\\"head\\\": \\\"proper nouns\\\", \\\"tail\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"PART-OF\\\", \\\"head_start\\\": 15, \\\"head_end\\\": 27, \\\"tail_start\\\": 31, \\\"tail_end\\\": 44}, {\\\"head\\\": \\\"morphological analysis\\\", \\\"tail\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"USED-FOR\\\", \\\"head_start\\\": 103, \\\"head_end\\\": 125, \\\"tail_start\\\": 129, \\\"tail_end\\\": 153}], \\\"events\\\": []}, \\\"samples\\\": [{\\\"entities\\\": [{\\\"text\\\": \\\"Recognition of proper nouns in Japanese text\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 0, \\\"end\\\": 44}, {\\\"text\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 129, \\\"end\\\": 153}], \\\"relations\\\": [{\\\"head\\\": \\\"Recognition of proper nouns in Japanese text\\\", \\\"tail\\\": \\\
…[truncated 9195 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rank8_lp_stats_20260518T005609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T00:58:57.688916+00:00_

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
  "session": "worker_analysis_rank8_lp_stats_20260518T005609",
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

_source line 18 · 2026-05-18T00:58:57.689067+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"551 /root/autodl-tmp/struct_self_consist_ie/output/exp_023_rank8_inference/samples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rank8_lp_stats_20260518T005609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T00:58:57.689233+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp_012_logprob/samples_with_logprobs.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rank8_lp_stats_20260518T005609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp_012_logprob/samples_with_logprobs.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T00:58:57.689363+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"551 /root/autodl-tmp/struct_self_consist_ie/output/exp_012_logprob/samples_with_logprobs.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rank8_lp_stats_20260518T005609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T00:58:57.689529+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -1 /root/autodl-tmp/struct_self_consist_ie/output/exp_023_rank8_inference/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rank8_lp_stats_20260518T005609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -1 /root/autodl-tmp/struct_self_consist_ie/output/exp_023_rank8_inference/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T00:58:57.689892+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"id\\\": \\\"X96-1059_sent000\\\", \\\"text\\\": \\\"Recognition of proper nouns in Japanese text has been studied as a part of the more general problem of morphological analysis in Japanese text processing -LRB- -LSB- 1 -RSB- -LSB- 2 -RSB- -RRB- .\\\", \\\"gold\\\": {\\\"entities\\\": [{\\\"text\\\": \\\"Recognition of proper nouns\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 0, \\\"end\\\": 27}, {\\\"text\\\": \\\"proper nouns\\\", \\\"type\\\": \\\"OtherScientificTerm\\\", \\\"start\\\": 15, \\\"end\\\": 27}, {\\\"text\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"Material\\\", \\\"start\\\": 31, \\\"end\\\": 44}, {\\\"text\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 103, \\\"end\\\": 125}, {\\\"text\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 129, \\\"end\\\": 153}], \\\"relations\\\": [{\\\"head\\\": \\\"Recognition of proper nouns\\\", \\\"tail\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"PART-OF\\\", \\\"head_start\\\": 0, \\\"head_end\\\": 27, \\\"tail_start\\\": 103, \\\"tail_end\\\": 125}, {\\\"head\\\": \\\"proper nouns\\\", \\\"tail\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"PART-OF\\\", \\\"head_start\\\": 15, \\\"head_end\\\": 27, \\\"tail_start\\\": 31, \\\"tail_end\\\": 44}, {\\\"head\\\": \\\"morphological analysis\\\", \\\"tail\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"USED-FOR\\\", \\\"head_start\\\": 103, \\\"head_end\\\": 125, \\\"tail_start\\\": 129, \\\"tail_end\\\": 153}], \\\"events\\\": []}, \\\"samples\\\": [{\\\"entities\\\": [{\\\"text\\\": \\\"Recognition of proper nouns in Japanese text\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 0, \\\"end\\\": 44}, {\\\"text\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"Material\\\", \\\"start\\\": 31, \\\"end\\\": 44}, {\\\"text\\\": \\\"morphological analysis in Japanese text processing\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\"
…[truncated 9375 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rank8_lp_stats_20260518T005609",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T00:58:57.690116+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat << 'PYEOF' > /root/autodl-tmp/struct_self_consist_ie/output/lp_rank_comparison.py\nimport json\nimport numpy as np\nfrom scipy import stats\n\ndef compute_entity_f1(pred_entities, gold_entities):\n    \"\"\"Compute entity-level F1 (exact match on text+type+start+end).\"\"\"\n    pred_set = set()\n    for e in pred_entities:\n        pred_set.add((e.get(\"text\",\"\"), e.get(\"type\",\"\"), e.get(\"start\",-1), e.get(\"end\",-1)))\n    gold_set = set()\n    for e in gold_entities:\n        gold_set.add((e.get(\"text\",\"\"), e.get(\"type\",\"\"), e.get(\"start\",-1), e.get(\"end\",-1)))\n    \n    if len(pred_set) == 0 and len(gold_set) == 0:\n        return 1.0\n    if len(pred_set) == 0 or len(gold_set) == 0:\n        return 0.0\n    \n    tp = len(pred_set & gold_set)\n    precision = tp / len(pred_set) if len(pred_set) > 0 else 0.0\n    recall = tp / len(gold_set) if len(gold_set) > 0 else 0.0\n    if precision + recall == 0:\n        return 0.0\n    return 2 * precision * recall / (precision + recall)\n\ndef analyze_file(path, label):\n    lp_ranges = []\n    tied_count = 0\n    total_count = 0\n    within_rhos = []\n    n_samples_list = []\n    \n    with open(path) as f:\n        for line in f:\n            row = json.loads(line)\n            samples = row[\"samples\"]\n            gold = row[\"gold\"]\n            n = len(samples)\n            n_samples_list.append(n)\n            \n            lps = [s[\"mean_logprob\"] for s in samples]\n            f1s = [compute_entity_f1(s.get(\"entities\", []), gold.get(\"entities\", [])) for s in samples]\n            \n            lp_arr = np.array(lps)\n            f1_arr = np.array(f1s)\n            \n            # LP range\n            lp_range = lp_arr.max() - lp_arr.min()\n            lp_ranges.append(lp_range)\n            \n            # Tied?\n            total_count += 1\n            if lp_range == 0:\n                tied_count += 1\n            \n            # Within-instance rho(LP, F1)\n            if len(set(lps)) > 1 and len(set(f1s)) > 1:\n                rho, _ = stats.spearmanr(lp_arr, f1_arr)\n                if not np.isnan(rho):\n                    within_rhos.append(rho)\n    \n    lp_ranges = np.array(lp_ranges)\n    \n    print(f\"\\n{'='*60}\")\n    print(f\"  {label}\")\n    print(f\"{'='*60}\")\n    print(f\"  Instances: {total_count}\")\n    print(f\"  Samples/instance: min={min(n_samples_list)}, max={max(n_samples_list)}, median={np.median(n_samples_list)}\")\n    print(f\"  LP median within-instance range: {np.median(lp_ranges):.6f}\")\n    print(f\"  LP mean within-instance range:   {np.mean(lp_ranges):.6f}\")\n    print(f\"  LP tied fraction:                {tied_count}/{total_count} = {tied_count/total_count:.4f}\")\n    print(f\"  Within-instance rho(LP,F1):\")\n    print(f\"    valid instances: {len(within_rhos)}/{total_count}\")\n    print(f\"    mean:   {np.mean(within_rhos):.4f}\")\n    print(f\"    median: {np.median(within_rhos):.4f}\")\n    print(f\"    std:    {np.std(within_rhos):.4f}\")\n    \n    return {\n        \"label\": label,\n        \"n_instances\": total_count,\n        \"lp_median_range\": float(np.median(lp_ranges)),\n        \"lp_mean_range\": float(np.mean(lp_ranges)),\n        \"lp_tied_fraction\": tied_count / total_count,\n        \"lp_tied_count\": tied_count,\n        \"rho_valid\": len(within_rhos),\n        \"rho_mean\": float(np.mean(within_rhos)) if within_rhos else None,\n        \"rho_median\": float(np.median(within_rhos)) if within_rhos else None,\n        \"rho_std\": float(np.std(within_rhos)) if within_rhos else None,\n    }\n\nrank8 = analyze_file(\n    \"/root/autodl-tmp/struct_self_consist_ie/output/exp_023_rank8_inference/samples.jsonl\",\n    \"Rank=8 (exp-023)\"\n)\nrank32 = analyze_file(\n    \"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_logprob/samples_with_logprobs.jsonl\",\n    \"Rank=32 (exp-012)\"\n)\n\nprint(f\"\\n{'='*60}\")\nprint(f\"  COMPARISON TABLE\")\nprint(f\"{'='*60}\")\nprint(f\"{'Metric':<35} {'Rank=8':>12} {'Rank=32':>12}\")\nprint(f\"{'-'*60}\")\nprint(f\"{'LP median range':<35} {rank8['lp_median_range']:>12.6f} {rank32['lp_median_range']:>12.6f}\")\nprint(f\"{'LP mean range':<35} {rank8['lp_mean_range']:>12.6f} {rank32['lp_mean_range']:>12.6f}\")\nprint(f\"{'LP tied fraction':<35} {rank8['lp_tied_fraction']:>12.4f} {rank32['lp_tied_fraction']:>12.4f}\")\nprint(f\"{'Within-inst rho(LP,F1) mean':<35} {rank8['rho_mean']:>12.4f} {rank32['rho_mean']:>12.4f}\")\nprint(f\"{'Within-inst rho(LP,F1) median':<35} {rank8['rho_median']:>12.4f} {rank32['rho_median']:>12.4f}\")\nprint(f\"{'rho valid instances':<35} {rank8['rho_valid']:>12d} {rank32['rho_valid']:>12d}\")\n\n# Save results\nresults = {\"rank8\": rank8, \"rank32\": rank32}\nwith open(\"/root/autodl-tmp/struct_self_consist_ie/output/lp_rank_comparison_results.json\", \"w\") as f:\n    json.dump(results, f, indent=2)\nprint(\"\\nResults saved to lp_rank_comparison_results.json\")\nPYEOF\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rank8_lp_stats_20260518T005609",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat << 'PYEOF' > /root/autodl-tmp/struct_self_consist_ie/output/lp_rank_comparison.py\nimport json\nimport numpy as np\nfrom scipy import stats\n\ndef compute_entity_f1(pred_entities, gold_entities):\n    \"\"\"Compute entity-level F1 (exact match on text+type+start+end).\"\"\"\n    pred_set = set()\n    for e in pred_entities:\n        pred_set.add((e.get(\"text\",\"\"), e.get(\"type\",\"\"), e.get(\"start\",-1), e.get(\"end\",-1)))\n    gold_set = set()\n    for e in gold_entities:\n        gold_set.add((e.get(\"text\",\"\"), e.get(\"type\",\"\"), e.get(\"start\",-1), e.get(\"end\",-1)))\n    \n    if len(pred_set) == 0 and len(gold_set) == 0:\n        return 1.0\n    if len(pred_set) == 0 or len(gold_set) == 0:\n        return 0.0\n    \n    tp = len(pred_set & gold_set)\n    precision = tp / len(pred_set) if len(pred_set) > 0 else 0.0\n    recall = tp / len(gold_set) if len(gold_set) > 0 else 0.0\n    if precision + recall == 0:\n        return 0.0\n    return 2 * precision * recall / (precision + recall)\n\ndef analyze_file(path, label):\n    lp_ranges = []\n    tied_count = 0\n    total_count = 0\n    within_rhos = []\n    n_samples_list = []\n    \n    with open(path) as f:\n        for line in f:\n            row = json.loads(line)\n            samples = row[\"samples\"]\n            gold = row[\"gold\"]\n            n = len(samples)\n            n_samples_list.append(n)\n            \n            lps = [s[\"mean_logprob\"] for s in samples]\n            f1s = [compute_entity_f1(s.get(\"entities\", []), gold.get(\"entities\", [])) for s in samples]\n            \n            lp_arr = np.array(lps)\n            f1_arr = np.array(f1s)\n            \n            # LP range\n            lp_range = lp_arr.max() - lp_arr.min()\n            lp_ranges.append(lp_range)\n            \n            # Tied?\n            total_count += 1\n            if lp_range == 0:\n                tied_count += 1\n            \n            # Within-instance rho(LP, F1)\n            if len(set(lps)) > 1 and len(set(f1s)) > 1:\n                rho, _ = stats.spearmanr(lp_arr, f1_arr)\n                if not np.isnan(rho):\n                    within_rhos.append(rho)\n    \n    lp_ranges = np.array(lp_ranges)\n    \n    print(f\"\\n{'='*60}\")\n    print(f\"  {label}\")\n    print(f\"{'='*60}\")\n    print(f\"  Instances: {total_count}\")\n    print(f\"  Samples/instance: min={min(n_samples_list)}, max={max(n_samples_list)}, median={np.median(n_samples_list)}\")\n    print(f\"  LP median within-instance range: {np.median(lp_ranges):.6f}\")\n    print(f\"  LP mean within-instance range:   {np.mean(lp_ranges):.6f}\")\n    print(f\"  LP tied fraction:                {tied_count}/{total_count} = {tied_count/total_count:.4f}\")\n    print(f\"  Within-instance rho(LP,F1):\")\n    print(f\"    valid instances: {len(within_rhos)}/{total_count}\")\n    print(f\"    mean:   {np.mean(within_rhos):.4f}\")\n    print(f\"    median: {np.median(within_rhos):.4f}\")\n    print(f\"    std:    {np.std(within_rhos):.4f}\")\n    \n    return {\n        \"label\": label,\n        \"n_instances\": total_count,\n        \"lp_median_range\": float(np.median(lp_ranges)),\n        \"lp_mean_range\": float(np.mean(lp_ranges)),\n        \"lp_tied_fraction\": tied_count / total_count,\n        \"lp_tied_count\": tied_count,\n        \"rho_valid\": len(within_rhos),\n        \"rho_mean\": float(np.mean(within_rhos)) if within_rhos else None,\n        \"rho_median\": float(np.median(within_rhos)) if within_rhos else None,\n        \"rho_std\": float(np.std(within_rhos)) if within_rhos else None,\n    }\n\nrank8 = analyze_file(\n    \"/root/autodl-tmp/struct_self_consist_ie/output/exp_023_rank8_inference/samples.jsonl\",\n    \"Rank=8 (exp-023)\"\n)\nrank32 = analyze_file(\n    \"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_logprob/samples_with_logprobs.jsonl\",\n    \"Rank=32 (exp-012)\"\n)\n\nprint(f\"\\n{'='*60}\")\nprint(f\"  COMPARISON TABLE\")\nprint(f\"{'='*60}\")\nprint(f\"{'Metric':<35} {'Rank=8':>12} {'Rank=32':>12}\")\nprint(f\"{'-'*60}\")\nprint(f\"{'LP median range':<35} {rank8['lp_median_range']:>12.6f} {rank32['lp_median_range']:>12.6f}\")\nprint(f\"{'LP mean range':<35} {rank8['lp_mean_range']:>12.6f} {rank32['lp_mean_range']:>12.6f}\")\nprint(f\"{'LP tied fraction':<35} {rank8['lp_tied_fraction']:>12.4f} {rank32['lp_tied_fraction']:>12.4f}\")\nprint(f\"{'Within-inst rho(LP,F1) mean':<35} {rank8['rho_mean']:>12.4f} {rank32['rho_mean']:>12.4f}\")\nprint(f\"{'Within-inst rho(LP,F1) median':<35} {rank8['rho_median']:>12.4f} {rank32['rho_median']:>12.4f}\")\nprint(f\"{'rho valid instances':<35} {rank8['rho_valid']:>12d} {rank32['rho_valid']:>12d}\")\n\n# Save results\nresults = {\"rank8\": rank8, \"rank32\": rank32}\nwith open(\"/root/autodl-tmp/struct_self_consist_ie/output/lp_rank_comparison_results.json\", \"w\") as f:\n    json.dump(results, f, indent=2)\nprint(\"\\nResults saved to lp_rank_comparison_results.json\")\nPYEOF\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-18T00:58:57.690356+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rank8_lp_stats_20260518T005609",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T00:58:57.690495+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie/output && python lp_rank_comparison.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rank8_lp_stats_20260518T005609",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie/output && python lp_rank_comparison.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-18T00:58:57.690641+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n============================================================\\n  Rank=8 (exp-023)\\n============================================================\\n  Instances: 551\\n  Samples/instance: min=8, max=8, median=8.0\\n  LP median within-instance range: 0.056931\\n  LP mean within-instance range:   0.075814\\n  LP tied fraction:                0/551 = 0.0000\\n  Within-instance rho(LP,F1):\\n    valid instances: 506/551\\n    mean:   0.2395\\n    median: 0.3164\\n    std:    0.4364\\n\\n============================================================\\n  Rank=32 (exp-012)\\n============================================================\\n  Instances: 551\\n  Samples/instance: min=8, max=8, median=8.0\\n  LP median within-instance range: 0.042857\\n  LP mean within-instance range:   0.059754\\n  LP tied fraction:                1/551 = 0.0018\\n  Within-instance rho(LP,F1):\\n    valid instances: 451/551\\n    mean:   0.1532\\n    median: 0.2474\\n    std:    0.5052\\n\\n============================================================\\n  COMPARISON TABLE\\n============================================================\\nMetric                                    Rank=8      Rank=32\\n------------------------------------------------------------\\nLP median range                         0.056931     0.042857\\nLP mean range                           0.075814     0.059754\\nLP tied fraction                          0.0000       0.0018\\nWithin-inst rho(LP,F1) mean               0.2395       0.1532\\nWithin-inst rho(LP,F1) median             0.3164       0.2474\\nrho valid instances                          506          451\\n\\nResults saved to lp_rank_comparison_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.72}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rank8_lp_stats_20260518T005609",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-18T00:58:57.690805+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "memory.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rank8_lp_stats_20260518T005609",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "memory.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-18T00:58:57.691018+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\", \"content\": \"# 项目记忆\\n\\n## 易混淆指标辨析（2026-05-17）\\n\\n**ρ=-0.881 (p=0.004)** = KeySet degeneracy vs **oracle headroom**（论文 L171 / appendix:1121）\\n**ρ=-0.381 (p=0.352)** = KeySet degeneracy vs **LP Δ**（selection improvement）\\n\\n这是两个不同的 y 轴变量。论文中的 ρ=-0.881 是正确的，已被 Reviewer 确认。不要再混淆。\\n\\n## SciERC LP Δ 两个版本（2026-05-17）\\n\\n- **+0.42pp** = full-set (n=551)，论文全文统一使用此值\\n- **+0.62pp** = gold-filtered (n=529)\\n\\nFigure 3 和正文保持一致用 full-set +0.42。\\n\\n## Cross-model Degeneracy 规律（2026-05-17）\\n\\nDegeneracy 由 **model capability × task difficulty × training convergence** 共同决定：\\n- Stronger model + easy task → 极端 degen（LLaMA-CoNLL 89.2%）\\n- Weaker model + hard task → low degen（Qwen3-SciERC 17.8%）\\n- CoNLL 是 high-degen regime 不论 backbone（Qwen3 47.4%, LLaMA 89.2%）\\n- Training convergence 调控 degen: Few-NERD 3-epoch 11.1% → 5-epoch 31.3%（+20pp）\\n- **Alignment (within-instance ρ) 是 dataset-intrinsic**: median ρ 不随 epoch 显著变化 (0.6667→0.6151)\\n\\nLLaMA on CoNLL headroom 仅 1.84pp（greedy 0.9242, oracle 0.9426），使得 selection 评估无意义。但 structural signals 的 QE diagnostic ρ≈0.43 仍显著优于 LP ρ=0.31，证明诊断价值是 model-agnostic 的。\\n\\nLP range median=0.0002 at 89% degen — LP 在极端 degen 下完全无法区分 samples。\\n\\n## exp_021 vs exp_028 within-instance ρ(LP, F1) 对比（2026-05-18）\\n\\n### 配对对比（同 5000 实例子集，N=8）\\n\\n| Metric | 3-epoch (exp_027) | 5-epoch (exp_028) | Delta |\\n|--------|-------------------|-------------------|-------|\\n| ρ mean | **0.5241** | 0.4066 | -0.1175 |\\n| ρ median | **0.6667** | 0.6151 | -0.0516 |\\n| ρ std | 0.4673 | 0.5506 | +0.0833 |\\n| Valid instances | 3723/4351 (85.6%) | 2988/4351 (68.7%) | -16.9pp |\\n\\n### 全量 exp_021（37648 实例，N=8）\\n- Mean ρ: 0.5106, Median ρ: 0.6667, Std: 0.4749\\n- Valid: 28086/32565 (86.3%)\\n\\n### 结论\\n1. **Median ρ 几乎不变** (0.6667→0.6151, Δ=-0.05): 非 degenerate 实例上 LP-F1 alignment 不受 training conver
…[truncated 7697 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rank8_lp_stats_20260518T005609",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-18T00:58:57.691225+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "memory.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rank8_lp_stats_20260518T005609",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "memory.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-18T00:58:57.691444+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\", \"content\": \"# 项目记忆\\n\\n## 易混淆指标辨析（2026-05-17）\\n\\n**ρ=-0.881 (p=0.004)** = KeySet degeneracy vs **oracle headroom**（论文 L171 / appendix:1121）\\n**ρ=-0.381 (p=0.352)** = KeySet degeneracy vs **LP Δ**（selection improvement）\\n\\n这是两个不同的 y 轴变量。论文中的 ρ=-0.881 是正确的，已被 Reviewer 确认。不要再混淆。\\n\\n## SciERC LP Δ 两个版本（2026-05-17）\\n\\n- **+0.42pp** = full-set (n=551)，论文全文统一使用此值\\n- **+0.62pp** = gold-filtered (n=529)\\n\\nFigure 3 和正文保持一致用 full-set +0.42。\\n\\n## Cross-model Degeneracy 规律（2026-05-17）\\n\\nDegeneracy 由 **model capability × task difficulty × training convergence** 共同决定：\\n- Stronger model + easy task → 极端 degen（LLaMA-CoNLL 89.2%）\\n- Weaker model + hard task → low degen（Qwen3-SciERC 17.8%）\\n- CoNLL 是 high-degen regime 不论 backbone（Qwen3 47.4%, LLaMA 89.2%）\\n- Training convergence 调控 degen: Few-NERD 3-epoch 11.1% → 5-epoch 31.3%（+20pp）\\n- **Alignment (within-instance ρ) 是 dataset-intrinsic**: median ρ 不随 epoch 显著变化 (0.6667→0.6151)\\n\\nLLaMA on CoNLL headroom 仅 1.84pp（greedy 0.9242, oracle 0.9426），使得 selection 评估无意义。但 structural signals 的 QE diagnostic ρ≈0.43 仍显著优于 LP ρ=0.31，证明诊断价值是 model-agnostic 的。\\n\\nLP range median=0.0002 at 89% degen — LP 在极端 degen 下完全无法区分 samples。\\n\\n## exp_021 vs exp_028 within-instance ρ(LP, F1) 对比（2026-05-18）\\n\\n### 配对对比（同 5000 实例子集，N=8）\\n\\n| Metric | 3-epoch (exp_027) | 5-epoch (exp_028) | Delta |\\n|--------|-------------------|-------------------|-------|\\n| ρ mean | **0.5241** | 0.4066 | -0.1175 |\\n| ρ median | **0.6667** | 0.6151 | -0.0516 |\\n| ρ std | 0.4673 | 0.5506 | +0.0833 |\\n| Valid instances | 3723/4351 (85.6%) | 2988/4351 (68.7%) | -16.9pp |\\n\\n### 全量 exp_021（37648 实例，N=8）\\n- Mean ρ: 0.5106, Median ρ: 0.6667, Std: 0.4749\\n- Valid: 28086/32565 (86.3%)\\n\\n### 结论\\n1. **Median ρ 几乎不变** (0.6667→0.6151, Δ=-0.05): 非 degenerate 实例上 LP-F1 alignment 不受 training conver
…[truncated 7697 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rank8_lp_stats_20260518T005609",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-18T00:58:57.691631+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "memory.md",
  "content": "# 项目记忆\n\n## 易混淆指标辨析（2026-05-17）\n\n**ρ=-0.881 (p=0.004)** = KeySet degeneracy vs **oracle headroom**（论文 L171 / appendix:1121）\n**ρ=-0.381 (p=0.352)** = KeySet degeneracy vs **LP Δ**（selection improvement）\n\n这是两个不同的 y 轴变量。论文中的 ρ=-0.881 是正确的，已被 Reviewer 确认。不要再混淆。\n\n## SciERC LP Δ 两个版本（2026-05-17）\n\n- **+0.42pp** = full-set (n=551)，论文全文统一使用此值\n- **+0.62pp** = gold-filtered (n=529)\n\nFigure 3 和正文保持一致用 full-set +0.42。\n\n## Cross-model Degeneracy 规律（2026-05-17）\n\nDegeneracy 由 **model capability × task difficulty × training convergence** 共同决定：\n- Stronger model + easy task → 极端 degen（LLaMA-CoNLL 89.2%）\n- Weaker model + hard task → low degen（Qwen3-SciERC 17.8%）\n- CoNLL 是 high-degen regime 不论 backbone（Qwen3 47.4%, LLaMA 89.2%）\n- Training convergence 调控 degen: Few-NERD 3-epoch 11.1% → 5-epoch 31.3%（+20pp）\n- **Alignment (within-instance ρ) 是 dataset-intrinsic**: median ρ 不随 epoch 显著变化 (0.6667→0.6151)\n\nLLaMA on CoNLL headroom 仅 1.84pp（greedy 0.9242, oracle 0.9426），使得 selection 评估无意义。但 structural signals 的 QE diagnostic ρ≈0.43 仍显著优于 LP ρ=0.31，证明诊断价值是 model-agnostic 的。\n\nLP range median=0.0002 at 89% degen — LP 在极端 degen 下完全无法区分 samples。\n\n## exp_021 vs exp_028 within-instance ρ(LP, F1) 对比（2026-05-18）\n\n### 配对对比（同 5000 实例子集，N=8）\n\n| Metric | 3-epoch (exp_027) | 5-epoch (exp_028) | Delta |\n|--------|-------------------|-------------------|-------|\n| ρ mean | **0.5241** | 0.4066 | -0.1175 |\n| ρ median | **0.6667** | 0.6151 | -0.0516 |\n| ρ std | 0.4673 | 0.5506 | +0.0833 |\n| Valid instances | 3723/4351 (85.6%) | 2988/4351 (68.7%) | -16.9pp |\n\n### 全量 exp_021（37648 实例，N=8）\n- Mean ρ: 0.5106, Median ρ: 0.6667, Std: 0.4749\n- Valid: 28086/32565 (86.3%)\n\n### 结论\n1. **Median ρ 几乎不变** (0.6667→0.6151, Δ=-0.05): 非 degenerate 实例上 LP-F1 alignment 不受 training convergence 显著影响 → **alignment IS dataset-intrinsic**\n2. **Mean ρ 下降较多** (0.5241→0.4066, Δ=-0.12): 主要因为 valid instances 从 85.6%→68.7%——更多实例变 degenerate，拉低 mean\n3. **两个条件的 driver 不同**: degeneracy 受 training convergence 调控，alignment 则是 dataset-intrinsic（median ρ 稳定）\n4. **Practitioner lever**: early stopping 控制 degeneracy，从而决定 LP selection 的有效性窗口\n5. **⚠️ 之前 exp_028 分析报告中 exp_021 ρ=0.6226 是错误值**（可能来自 N=16 分析），正确 N=8 同子集值: mean=0.5241, median=0.6667\n\n## exp_028 结果：5-epoch Few-NERD 收敛测试（2026-05-18）\n\n### 实验配置\n- Model: Qwen3-8B + LoRA, Few-NERD, 5 epochs (vs exp-021 3 epochs)\n- Inference: N=8, T=1.0, logprobs collected\n- Gold-filtered instances: 4351/5000\n\n### 核心结果\n\n| Metric | 3-epoch (exp-021) | 5-epoch (exp-028) | Delta |\n|--------|-------------------|-------------------|-------|\n| Degeneracy (CF1) % | 11.1% | **31.3%** | +20.2pp |\n| Greedy F1 | 0.7478 | 0.7773 | +2.95pp |\n| Oracle F1 | — | 0.8723 | — |\n| Headroom (pp) | — | 9.50pp | — |\n| LP sel F1 | 0.7614 | 0.7835 | +2.21pp |\n| LP sel delta (pp) | +1.37 | **+0.62** | -0.75 |\n\n### QE Signals (5-epoch)\n\n| Signal | AUROC | ρ (global) | Sel F1 | Delta |\n|--------|-------|------------|--------|-------|\n| LP | 0.5234 | **0.4495** | 0.7835 | +0.62pp |\n| SJ | 0.4988 | 0.3777 | 0.7697 | -0.77pp |\n| FK | 0.4985 | 0.3892 | 0.7693 | -0.80pp |\n| EM | 0.4951 | 0.3893 | 0.7663 | -1.10pp |\n| VC | 0.5006 | 0.3585 | 0.7576 | -1.97pp |\n\n### Within-instance LP-F1 correlation\n- Mean ρ: 0.4066, Median ρ: 0.6151, Std: 0.5506\n- Valid instances: 2988/4351 (68.7%)\n\n### LP Range\n- Mean: 0.0514, Std: 0.0673, Median: 0.0318\n\n### Report.json 补充（inference-level stats）\n- Greedy F1 (raw, pre-gold-filter): 0.7940\n- Oracle F1 (raw): 0.8770\n- FK mean: 0.5284, SJ mean: 0.8070\n- LP baseline ρ (full): 0.3319, AUROC: 0.6806\n- SJ vs F1 ρ (full): 0.3716\n- FK vs F1 ρ (full): 0.2760\n- Structural > Surface confirmed (ρ advantage = +0.096)\n- Sample F1 mean: 0.7269, std: 0.3416, pct_zero: 12.3%\n\n### 结论：NEGATIVE\n**5-epoch degeneracy 31.3% 远超 3-epoch 的 11.1%（+20.2pp）。** Few-NERD 的低 degeneracy 可能源于模型 under-convergence 而非数据集/任务本质特性。\n\n关键影响：\n1. LP selection delta 从 +1.37pp 降至 +0.62pp（更多 degenerate instances 压缩了 selection 空间）\n2. 结构信号（SJ/FK/EM/VC）在 5-epoch 上 selection delta 全为负，仅 LP 正\n3. 但 LP global ρ=0.4495 仍显著（p≈0），within-instance median ρ=0.6151 说明非 degenerate 实例上 LP 仍有区分力\n4. **论文叙事需修正**：不能以 Few-NERD low degeneracy 作为\"结构化任务天然适合 self-consistency\"的证据\n\n## Rank=8 vs Rank=32 LP 统计对比 (2026-05-18)\n\n数据来源: exp-023 (rank=8) vs exp-012 (rank=32), SciERC, N=8, T=1.0, 551 instances\n\n| Metric | Rank=8 (exp-023) | Rank=32 (exp-012) |\n|--------|------------------|-------------------|\n| LP median within-instance range | 0.056931 | 0.042857 |\n| LP mean within-instance range | 0.075814 | 0.059754 |\n| LP tied fraction | 0/551 (0.00%) | 1/551 (0.18%) |\n| Within-instance ρ(LP,F1) mean | 0.2395 | 0.1532 |\n| Within-instance ρ(LP,F1) median | 0.3164 | 0.2474 |\n| ρ valid instances | 506/551 (91.8%) | 451/551 (81.9%) |\n\n### 关键发现\n1. **Rank=8 的 LP 变异性更大**: median range 0.057 vs 0.043（+33%），说明低 rank adapter 产生更多样化的 log-probability 分布\n2. **Rank=8 的 LP-F1 alignment 更强**: within-instance ρ median 0.32 vs 0.25（+28%），mean 0.24 vs 0.15（+56%）\n3. **两者 tied fraction 都极低**: rank=8 为 0%，rank=32 为 0.18%，LP degeneracy 不是 SciERC 上的问题\n4. **Rank=8 有更多 valid ρ 实例**: 91.8% vs 81.9%，因为更大的 LP range 使得更多实例有足够变异性来计算 correlation\n5. **结论**: 低 rank adapter 反而提升了 LP 作为 QE 信号的质量，可能因为 rank=8 的 under-parameterization 迫使模型在 uncertain instances 上产生更有区分性的 logprob 分布\n\n## 文献调研：一致性 ≠ 正确性（2026-05-16）\n\n### 调研背景\nFew-NERD（8类粗粒度NER）上，结构一致性信号（SJ/FK/EM/VC）的 global ρ 为负或近零，selection delta 全为负。根因：模型存在 systematic bias（类型语义重叠 → 8 samples 一致但全错），暴露 self-consistency 的根本假设缺陷。\n\n### 最相关论文（5篇）\n\n#### 1. Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems\n- **Authors**: Adam Byerly, Daniel Khashabi\n- **Year/Venue**: 2024, TACL (arXiv: 2411.01101)\n- **关系**: **最强验证**。正式证明当 errors correlated 时，self-consistency 放大而非纠正错误\n- **Key insight**: 长上下文任务中，positional bias 导致所有 samples 产生相关错误，违反 self-consistency 的核心假设（error independence）。Self-consistency 不仅无效，反而 actively degrades performance。实验覆盖 GPT-4o、LLaMA-3.3-70B、Qwen-2.5-72B\n- **与我们的平行关系**: 他们的 \"positional bias → correlated errors\" 对应我们的 \"type semantic overlap → systematic misclassification\"。机制不同但失败模式完全相同\n\n#### 2. Consistency–Accuracy Correlation in Hard-Prompted LLMs for Entity and Relation Extraction\n- **Venue**: PMC (PMC12888769), 2025\n- **关系**: **IE 领域直接验证**\n- **Key insight**: 在 EPOP 语料（植物健康数据，实体+关系抽取）上测试 GPT/DeepSeek/Qwen/Kimi 四个模型，发现 high consistency does NOT strongly correlate with high accuracy。相关性是 model-dependent 且随 task complexity 变化。在 relational IE 中，consistency alone 不应被用作 prediction quality 的 proxy\n- **与我们的关系**: 直接在 IE 任务上验证了我们在 NER 上的发现——一致性不等于正确性\n\n#### 3. Beyond Majority Voting: SCOPE (Subgroup-specific Confidence-weighted Pseudo-label Estimation)\n- **Year/Venue**: 2024, arXiv: 2512.15146\n- **关系**: **提出解决方案**\n- **Key insight**: Majority voting 的问题：(1) 所有 votes 权重相同，忽略 confidence；(2) binary voting 无法捕获 fine-grained signals；(3) confirmation bias——模型强化自身错误。SCOPE 用 step-wise confidence 加权替代简单 frequency count，并通过 dynamic subgroup partitioning 平衡 quality 与 diversity\n- **可借鉴**: confidence weighting + subgroup partitioning 思路可用于我们的结构一致性信号设计\n\n#### 4. Diversified Sampling Improves Scaling LLM Inference\n- **Year**: 2025, arXiv: 2502.11027\n- **关系**: **互补——从 sampling 端解决 correlated errors**\n- **Key insight**: 同一 prompt 反复 sampling 导致输出 \"trapped\" 在 local cluster 中。通过 diversified prompts（role perturbation、instruction variation、jabberwocky perturbation）可以打破 error correlation，提升 coverage。在 reasoning/math/code 任务上显著提升\n- **可借鉴**: 如果我们在 NER 中使用多样化 prompt 策略（不同 instruction 模板、不同 few-shot examples、不同 entity type 描述），可能减少 systematic bias 导致的 correlated errors\n\n#### 5. The Hidden Strength of Disagreement: Consensus-Diversity Tradeoff in Adaptive Multi-Agent Systems\n- **Authors**: Wu & Ito\n- **Year/Venue**: 2025, EMNLP (arXiv: 2502.16565)\n- **关系**: **理论框架**\n- **Key insight**: 显式 consensus（voting/prompting）有 premature homogenization 风险。隐式 consensus（agents 独立决策但共享信息）保留了 diversity，在动态环境中优于显式 voting。形式化了 consensus-diversity tradeoff\n- **与我们的关系**: 我们的结构一致性信号是显式 consensus measure，当模型有 systematic bias 时导致 premature homogenization（全部 samples 一致地错）\n\n### 补充相关工作\n\n#### 6. Don't Always Pick the Highest-Performing Model: Information Theoretic View of LLM Ensemble Selection\n- **Year**: 2026, arXiv: 2602.08003\n- 用 Gaussian-copula 建模 correlated errors，证明 ensemble 存在 information-theoretic error floor\n\n#### 7. Wang et al. 2023 Self-Consistency (ICLR 2023, arXiv: 2203.11171)\n- 原文假设 diverse reasoning paths → correct answer 更可能被多数路径选中\n- **未显式讨论** systematic bias 导致所有路径收敛到同一错误答案的 failure mode\n\n#### 8. LLM-TOPLA: Efficient LLM Ensemble by Maximising Diversity\n- **Year/Venue**: 2024, EMNLP Findings\n- 用 focal diversity metric 选择互补性强的 ensemble 成员，减少 error correlation\n\n### 核心结论\n\n#### Q1: 有没有人正式分析过 self-consistency 在什么条件下失败？\n**有。** Byerly & Khashabi (2024, TACL) 是最系统的分析，证明 positional bias 导致 correlated errors 时 self-consistency 失败。但他们聚焦 long-context + positional bias，没有覆盖 structured prediction 中 semantic overlap 导致的 systematic bias。\n\n#### Q2: \"Correlated failures\" 如何破坏 voting-based 方法？\n多篇论文从不同角度论证：error correlation 违反了 voting 的 independence 假设。当 errors correlated，增加 samples 不能提升 accuracy（有 information-theoretic floor），甚至可能 amplify errors。\n\n#### Q3: 有没有人提出过针对 systematic bias 的改进？\n- **Confidence weighting** (SCOPE): 用 confidence 加权替代 equal voting\n- **Diversified sampling**: 用不同 prompt 变体打破 local cluster\n- **Subgroup partitioning**: 将 samples 分组，组间保持 diversity\n- **Cross-model probing**: 用不同模型交叉验证（但成本高）\n\n#### Q4: 结构化预测中 self-consistency 的特殊挑战？\nConsistency-accuracy correlation 论文（PMC12888769）在 IE 任务上直接验证了一致性≠正确性。但目前 **没有** 专门针对 NER/结构化预测中 self-consistency failure modes 的系统性研究——这是我们的 contribution gap。\n\n### 对我们下一步的启示\n\n1. **论文 framing**: 我们的发现（结构一致性在 systematic bias 下失败）有文献支撑但 **在 structured IE 领域是新的**。Byerly & Khashabi 做了 long-context，我们做 structured prediction，互补\n2. **可借鉴技术**：\n   - Confidence-weighted consistency（替代 raw agreement）\n   - Diversified prompting（不同 instruction/few-shot 模板减少 correlated errors）\n   - Adaptive stopping（当 consistency 低时增加 samples，但当 consistency 高且可能是 systematic bias 时需要 different strategy）\n3. **Discussion 要写的**: 引用 Byerly & Khashabi 说明这是 self-consistency 的 general failure mode，我们在 IE 领域首次系统性展示，并分析了结构化预测特有的原因（type semantic overlap、span boundary ambiguity）\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_rank8_lp_stats_20260518T005609",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "memory.md",
    "content": "# 项目记忆\n\n## 易混淆指标辨析（2026-05-17）\n\n**ρ=-0.881 (p=0.004)** = KeySet degeneracy vs **oracle headroom**（论文 L171 / appendix:1121）\n**ρ=-0.381 (p=0.352)** = KeySet degeneracy vs **LP Δ**（selection improvement）\n\n这是两个不同的 y 轴变量。论文中的 ρ=-0.881 是正确的，已被 Reviewer 确认。不要再混淆。\n\n## SciERC LP Δ 两个版本（2026-05-17）\n\n- **+0.42pp** = full-set (n=551)，论文全文统一使用此值\n- **+0.62pp** = gold-filtered (n=529)\n\nFigure 3 和正文保持一致用 full-set +0.42。\n\n## Cross-model Degeneracy 规律（2026-05-17）\n\nDegeneracy 由 **model capability × task difficulty × training convergence** 共同决定：\n- Stronger model + easy task → 极端 degen（LLaMA-CoNLL 89.2%）\n- Weaker model + hard task → low degen（Qwen3-SciERC 17.8%）\n- CoNLL 是 high-degen regime 不论 backbone（Qwen3 47.4%, LLaMA 89.2%）\n- Training convergence 调控 degen: Few-NERD 3-epoch 11.1% → 5-epoch 31.3%（+20pp）\n- **Alignment (within-instance ρ) 是 dataset-intrinsic**: median ρ 不随 epoch 显著变化 (0.6667→0.6151)\n\nLLaMA on CoNLL headroom 仅 1.84pp（greedy 0.9242, oracle 0.9426），使得 selection 评估无意义。但 structural signals 的 QE diagnostic ρ≈0.43 仍显著优于 LP ρ=0.31，证明诊断价值是 model-agnostic 的。\n\nLP range median=0.0002 at 89% degen — LP 在极端 degen 下完全无法区分 samples。\n\n## exp_021 vs exp_028 within-instance ρ(LP, F1) 对比（2026-05-18）\n\n### 配对对比（同 5000 实例子集，N=8）\n\n| Metric | 3-epoch (exp_027) | 5-epoch (exp_028) | Delta |\n|--------|-------------------|-------------------|-------|\n| ρ mean | **0.5241** | 0.4066 | -0.1175 |\n| ρ median | **0.6667** | 0.6151 | -0.0516 |\n| ρ std | 0.4673 | 0.5506 | +0.0833 |\n| Valid instances | 3723/4351 (85.6%) | 2988/4351 (68.7%) | -16.9pp |\n\n### 全量 exp_021（37648 实例，N=8）\n- Mean ρ: 0.5106, Median ρ: 0.6667, Std: 0.4749\n- Valid: 28086/32565 (86.3%)\n\n### 结论\n1. **Median ρ 几乎不变** (0.6667→0.6151, Δ=-0.05): 非 degenerate 实例上 LP-F1 alignment 不受 training convergence 显著影响 → **alignment IS dataset-intrinsic**\n2. **Mean ρ 下降较多** (0.5241→0.4066, Δ=-0.12): 主要因为 valid instances 从 85.6%→68.7%——更多实例变 degenerate，拉低 mean\n3. **两个条件的 driver 不同**: degeneracy 受 training convergence 调控，alignment 则是 dataset-intrinsic（median ρ 稳定）\n4. **Practitioner lever**: early stopping 控制 degeneracy，从而决定 LP selection 的有效性窗口\n5. **⚠️ 之前 exp_028 分析报告中 exp_021 ρ=0.6226 是错误值**（可能来自 N=16 分析），正确 N=8 同子集值: mean=0.5241, median=0.6667\n\n## exp_028 结果：5-epoch Few-NERD 收敛测试（2026-05-18）\n\n### 实验配置\n- Model: Qwen3-8B + LoRA, Few-NERD, 5 epochs (vs exp-021 3 epochs)\n- Inference: N=8, T=1.0, logprobs collected\n- Gold-filtered instances: 4351/5000\n\n### 核心结果\n\n| Metric | 3-epoch (exp-021) | 5-epoch (exp-028) | Delta |\n|--------|-------------------|-------------------|-------|\n| Degeneracy (CF1) % | 11.1% | **31.3%** | +20.2pp |\n| Greedy F1 | 0.7478 | 0.7773 | +2.95pp |\n| Oracle F1 | — | 0.8723 | — |\n| Headroom (pp) | — | 9.50pp | — |\n| LP sel F1 | 0.7614 | 0.7835 | +2.21pp |\n| LP sel delta (pp) | +1.37 | **+0.62** | -0.75 |\n\n### QE Signals (5-epoch)\n\n| Signal | AUROC | ρ (global) | Sel F1 | Delta |\n|--------|-------|------------|--------|-------|\n| LP | 0.5234 | **0.4495** | 0.7835 | +0.62pp |\n| SJ | 0.4988 | 0.3777 | 0.7697 | -0.77pp |\n| FK | 0.4985 | 0.3892 | 0.7693 | -0.80pp |\n| EM | 0.4951 | 0.3893 | 0.7663 | -1.10pp |\n| VC | 0.5006 | 0.3585 | 0.7576 | -1.97pp |\n\n### Within-instance LP-F1 correlation\n- Mean ρ: 0.4066, Median ρ: 0.6151, Std: 0.5506\n- Valid instances: 2988/4351 (68.7%)\n\n### LP Range\n- Mean: 0.0514, Std: 0.0673, Median: 0.0318\n\n### Report.json 补充（inference-level stats）\n- Greedy F1 (raw, pre-gold-filter): 0.7940\n- Oracle F1 (raw): 0.8770\n- FK mean: 0.5284, SJ mean: 0.8070\n- LP baseline ρ (full): 0.3319, AUROC: 0.6806\n- SJ vs F1 ρ (full): 0.3716\n- FK vs F1 ρ (full): 0.2760\n- Structural > Surface confirmed (ρ advantage = +0.096)\n- Sample F1 mean: 0.7269, std: 0.3416, pct_zero: 12.3%\n\n### 结论：NEGATIVE\n**5-epoch degeneracy 31.3% 远超 3-epoch 的 11.1%（+20.2pp）。** Few-NERD 的低 degeneracy 可能源于模型 under-convergence 而非数据集/任务本质特性。\n\n关键影响：\n1. LP selection delta 从 +1.37pp 降至 +0.62pp（更多 degenerate instances 压缩了 selection 空间）\n2. 结构信号（SJ/FK/EM/VC）在 5-epoch 上 selection delta 全为负，仅 LP 正\n3. 但 LP global ρ=0.4495 仍显著（p≈0），within-instance median ρ=0.6151 说明非 degenerate 实例上 LP 仍有区分力\n4. **论文叙事需修正**：不能以 Few-NERD low degeneracy 作为\"结构化任务天然适合 self-consistency\"的证据\n\n## Rank=8 vs Rank=32 LP 统计对比 (2026-05-18)\n\n数据来源: exp-023 (rank=8) vs exp-012 (rank=32), SciERC, N=8, T=1.0, 551 instances\n\n| Metric | Rank=8 (exp-023) | Rank=32 (exp-012) |\n|--------|------------------|-------------------|\n| LP median within-instance range | 0.056931 | 0.042857 |\n| LP mean within-instance range | 0.075814 | 0.059754 |\n| LP tied fraction | 0/551 (0.00%) | 1/551 (0.18%) |\n| Within-instance ρ(LP,F1) mean | 0.2395 | 0.1532 |\n| Within-instance ρ(LP,F1) median | 0.3164 | 0.2474 |\n| ρ valid instances | 506/551 (91.8%) | 451/551 (81.9%) |\n\n### 关键发现\n1. **Rank=8 的 LP 变异性更大**: median range 0.057 vs 0.043（+33%），说明低 rank adapter 产生更多样化的 log-probability 分布\n2. **Rank=8 的 LP-F1 alignment 更强**: within-instance ρ median 0.32 vs 0.25（+28%），mean 0.24 vs 0.15（+56%）\n3. **两者 tied fraction 都极低**: rank=8 为 0%，rank=32 为 0.18%，LP degeneracy 不是 SciERC 上的问题\n4. **Rank=8 有更多 valid ρ 实例**: 91.8% vs 81.9%，因为更大的 LP range 使得更多实例有足够变异性来计算 correlation\n5. **结论**: 低 rank adapter 反而提升了 LP 作为 QE 信号的质量，可能因为 rank=8 的 under-parameterization 迫使模型在 uncertain instances 上产生更有区分性的 logprob 分布\n\n## 文献调研：一致性 ≠ 正确性（2026-05-16）\n\n### 调研背景\nFew-NERD（8类粗粒度NER）上，结构一致性信号（SJ/FK/EM/VC）的 global ρ 为负或近零，selection delta 全为负。根因：模型存在 systematic bias（类型语义重叠 → 8 samples 一致但全错），暴露 self-consistency 的根本假设缺陷。\n\n### 最相关论文（5篇）\n\n#### 1. Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems\n- **Authors**: Adam Byerly, Daniel Khashabi\n- **Year/Venue**: 2024, TACL (arXiv: 2411.01101)\n- **关系**: **最强验证**。正式证明当 errors correlated 时，self-consistency 放大而非纠正错误\n- **Key insight**: 长上下文任务中，positional bias 导致所有 samples 产生相关错误，违反 self-consistency 的核心假设（error independence）。Self-consistency 不仅无效，反而 actively degrades performance。实验覆盖 GPT-4o、LLaMA-3.3-70B、Qwen-2.5-72B\n- **与我们的平行关系**: 他们的 \"positional bias → correlated errors\" 对应我们的 \"type semantic overlap → systematic misclassification\"。机制不同但失败模式完全相同\n\n#### 2. Consistency–Accuracy Correlation in Hard-Prompted LLMs for Entity and Relation Extraction\n- **Venue**: PMC (PMC12888769), 2025\n- **关系**: **IE 领域直接验证**\n- **Key insight**: 在 EPOP 语料（植物健康数据，实体+关系抽取）上测试 GPT/DeepSeek/Qwen/Kimi 四个模型，发现 high consistency does NOT strongly correlate with high accuracy。相关性是 model-dependent 且随 task complexity 变化。在 relational IE 中，consistency alone 不应被用作 prediction quality 的 proxy\n- **与我们的关系**: 直接在 IE 任务上验证了我们在 NER 上的发现——一致性不等于正确性\n\n#### 3. Beyond Majority Voting: SCOPE (Subgroup-specific Confidence-weighted Pseudo-label Estimation)\n- **Year/Venue**: 2024, arXiv: 2512.15146\n- **关系**: **提出解决方案**\n- **Key insight**: Majority voting 的问题：(1) 所有 votes 权重相同，忽略 confidence；(2) binary voting 无法捕获 fine-grained signals；(3) confirmation bias——模型强化自身错误。SCOPE 用 step-wise confidence 加权替代简单 frequency count，并通过 dynamic subgroup partitioning 平衡 quality 与 diversity\n- **可借鉴**: confidence weighting + subgroup partitioning 思路可用于我们的结构一致性信号设计\n\n#### 4. Diversified Sampling Improves Scaling LLM Inference\n- **Year**: 2025, arXiv: 2502.11027\n- **关系**: **互补——从 sampling 端解决 correlated errors**\n- **Key insight**: 同一 prompt 反复 sampling 导致输出 \"trapped\" 在 local cluster 中。通过 diversified prompts（role perturbation、instruction variation、jabberwocky perturbation）可以打破 error correlation，提升 coverage。在 reasoning/math/code 任务上显著提升\n- **可借鉴**: 如果我们在 NER 中使用多样化 prompt 策略（不同 instruction 模板、不同 few-shot examples、不同 entity type 描述），可能减少 systematic bias 导致的 correlated errors\n\n#### 5. The Hidden Strength of Disagreement: Consensus-Diversity Tradeoff in Adaptive Multi-Agent Systems\n- **Authors**: Wu & Ito\n- **Year/Venue**: 2025, EMNLP (arXiv: 2502.16565)\n- **关系**: **理论框架**\n- **Key insight**: 显式 consensus（voting/prompting）有 premature homogenization 风险。隐式 consensus（agents 独立决策但共享信息）保留了 diversity，在动态环境中优于显式 voting。形式化了 consensus-diversity tradeoff\n- **与我们的关系**: 我们的结构一致性信号是显式 consensus measure，当模型有 systematic bias 时导致 premature homogenization（全部 samples 一致地错）\n\n### 补充相关工作\n\n#### 6. Don't Always Pick the Highest-Performing Model: Information Theoretic View of LLM Ensemble Selection\n- **Year**: 2026, arXiv: 2602.08003\n- 用 Gaussian-copula 建模 correlated errors，证明 ensemble 存在 information-theoretic error floor\n\n#### 7. Wang et al. 2023 Self-Consistency (ICLR 2023, arXiv: 2203.11171)\n- 原文假设 diverse reasoning paths → correct answer 更可能被多数路径选中\n- **未显式讨论** systematic bias 导致所有路径收敛到同一错误答案的 failure mode\n\n#### 8. LLM-TOPLA: Efficient LLM Ensemble by Maximising Diversity\n- **Year/Venue**: 2024, EMNLP Findings\n- 用 focal diversity metric 选择互补性强的 ensemble 成员，减少 error correlation\n\n### 核心结论\n\n#### Q1: 有没有人正式分析过 self-consistency 在什么条件下失败？\n**有。** Byerly & Khashabi (2024, TACL) 是最系统的分析，证明 positional bias 导致 correlated errors 时 self-consistency 失败。但他们聚焦 long-context + positional bias，没有覆盖 structured prediction 中 semantic overlap 导致的 systematic bias。\n\n#### Q2: \"Correlated failures\" 如何破坏 voting-based 方法？\n多篇论文从不同角度论证：error correlation 违反了 voting 的 independence 假设。当 errors correlated，增加 samples 不能提升 accuracy（有 information-theoretic floor），甚至可能 amplify errors。\n\n#### Q3: 有没有人提出过针对 systematic bias 的改进？\n- **Confidence weighting** (SCOPE): 用 confidence 加权替代 equal voting\n- **Diversified sampling**: 用不同 prompt 变体打破 local cluster\n- **Subgroup partitioning**: 将 samples 分组，组间保持 diversity\n- **Cross-model probing**: 用不同模型交叉验证（但成本高）\n\n#### Q4: 结构化预测中 self-consistency 的特殊挑战？\nConsistency-accuracy correlation 论文（PMC12888769）在 IE 任务上直接验证了一致性≠正确性。但目前 **没有** 专门针对 NER/结构化预测中 self-consistency failure modes 的系统性研究——这是我们的 contribution gap。\n\n### 对我们下一步的启示\n\n1. **论文 framing**: 我们的发现（结构一致性在 systematic bias 下失败）有文献支撑但 **在 structured IE 领域是新的**。Byerly & Khashabi 做了 long-context，我们做 structured prediction，互补\n2. **可借鉴技术**：\n   - Confidence-weighted consistency（替代 raw agreement）\n   - Diversified prompting（不同 instruction/few-shot 模板减少 correlated errors）\n   - Adaptive stopping（当 consistency 低时增加 samples，但当 consistency 高且可能是 systematic bias 时需要 different strategy）\n3. **Discussion 要写的**: 引用 Byerly & Khashabi 说明这是 self-consistency 的 general failure mode，我们在 IE 领域首次系统性展示，并分析了结构化预测特有的原因（type semantic overlap、span boundary ambiguity）\n"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-18T00:58:57.691878+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_rank8_lp_stats_20260518T005609",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-18T00:58:57.692047+00:00_

完成。结果摘要：

| Metric | Rank=8 (exp-023) | Rank=32 (exp-012) |
|--------|------------------|-------------------|
| LP median range | **0.0569** | 0.0429 |
| LP mean range | **0.0758** | 0.0598 |
| LP tied fraction | 0/551 (0.00%) | 1/551 (0.18%) |
| Within-inst ρ(LP,F1) mean | **0.2395** | 0.1532 |
| Within-inst ρ(LP,F1) median | **0.3164** | 0.2474 |
| ρ valid instances | 506/551 (91.8%) | 451/551 (81.9%) |

Rank=8 在所有 LP 指标上优于 rank=32：更大的 within-instance range（+33%）、更强的 LP-F1 alignment（median ρ +28%）、更多 valid instances（+10pp）。低 rank adapter 的 under-parameterization 反而产生了更有区分性的 logprob 分布，对 W2 的 "LoRA rank sensitivity" 问题是正面回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_rank8_lp_stats_20260518T005609"
}
```

</details>

---
